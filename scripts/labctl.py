#!/usr/bin/env python3
"""Catálogo declarativo de labs. Execução e observação entram nos PRs seguintes."""
from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path
import re
import shutil
import subprocess
import sys

try:
    import yaml
except ImportError:
    sys.exit("Dependência ausente: python3 -m pip install 'PyYAML>=6,<7'")

ROOT = Path(__file__).resolve().parents[1]
TRILHAS = ROOT / "trilhas"
ID_PATTERN = re.compile(r"^\d{2}\.\d{2}$")
SAFE_NAME = re.compile(r"^[a-z0-9][a-z0-9-]{0,62}$")
SUPPORTED_CHECKS = {"deployment", "service", "rbac", "rbac-deny", "quota"}
SUPPORTED_EXPERIMENTS = {"expect-rejected-manifest"}


@dataclass(frozen=True)
class Lab:
    identifier: str
    title: str
    namespace: str
    directory: Path
    apply: tuple[Path, ...]
    checks: tuple[dict, ...]
    experiments: tuple[dict, ...]


def load_labs() -> dict[str, Lab]:
    labs: dict[str, Lab] = {}
    for metadata in sorted(TRILHAS.glob("*/labs/*/lab.yaml")):
        with metadata.open(encoding="utf-8") as stream:
            data = yaml.safe_load(stream)
        if not isinstance(data, dict):
            raise ValueError(f"{metadata}: esperado um objeto YAML")
        identifier, title, namespace = (data.get(k) for k in ("id", "title", "namespace"))
        if not isinstance(identifier, str) or not ID_PATTERN.fullmatch(identifier):
            raise ValueError(f"{metadata}: id deve seguir formato 01.06")
        if identifier in labs:
            raise ValueError(f"ID duplicado: {identifier}")
        if not isinstance(title, str) or not title.strip():
            raise ValueError(f"{metadata}: title obrigatório")
        if not isinstance(namespace, str) or not SAFE_NAME.fullmatch(namespace):
            raise ValueError(f"{metadata}: namespace inválido")
        filenames = data.get("apply")
        if not isinstance(filenames, list) or not filenames:
            raise ValueError(f"{metadata}: apply deve listar manifests")
        def manifest(filename: str) -> Path:
            if not isinstance(filename, str) or not filename.endswith((".yaml", ".yml")):
                raise ValueError(f"{metadata}: caminho YAML inválido: {filename!r}")
            candidate = (metadata.parent / filename).resolve()
            if not candidate.is_relative_to(metadata.parent.resolve()) or not candidate.is_file():
                raise ValueError(f"{metadata}: arquivo fora do lab ou inexistente: {filename}")
            return candidate
        apply = tuple(manifest(name) for name in filenames)
        checks = data.get("checks", [])
        if not isinstance(checks, list) or any(not isinstance(x, dict) or x.get("type") not in SUPPORTED_CHECKS for x in checks):
            raise ValueError(f"{metadata}: checks não suportados")
        experiments = data.get("experiments", [])
        if not isinstance(experiments, list) or any(not isinstance(x, dict) or x.get("type") not in SUPPORTED_EXPERIMENTS for x in experiments):
            raise ValueError(f"{metadata}: experiments não suportados")
        for experiment in experiments:
            manifest(experiment.get("manifest"))
        labs[identifier] = Lab(identifier, title, namespace, metadata.parent, apply, tuple(checks), tuple(experiments))
    return labs


def run_command(args: list[str]) -> int:
    return subprocess.run(args, check=False).returncode


def doctor() -> int:
    print("Ferramentas necessárias:")
    required = ("python3", "docker", "kind", "kubectl")
    missing = [tool for tool in required if not shutil.which(tool)]
    for tool in required:
        print(f"  {'OK' if tool not in missing else 'FALTA'} {tool}")
    if missing:
        return 1
    return run_command(["docker", "info", "--format", "{{.ServerVersion}}"])



def checked_cluster() -> None:
    expected = "kind-" + __import__("os").environ.get("CLUSTER_NAME", "dev")
    current = subprocess.run(["kubectl", "config", "current-context"], capture_output=True, text=True, check=False)
    if current.returncode or current.stdout.strip() != expected:
        raise ValueError(f"Contexto incorreto: {current.stdout.strip()!r}; esperado {expected!r}")
    clusters = subprocess.run(["kind", "get", "clusters"], capture_output=True, text=True, check=False)
    if clusters.returncode or expected[5:] not in clusters.stdout.splitlines():
        raise ValueError(f"Cluster Kind {expected[5:]} não encontrado")


def kubectl(*args: str, quiet: bool = False) -> subprocess.CompletedProcess[str]:
    command = ["kubectl", *args]
    result = subprocess.run(command, text=True, capture_output=quiet, check=False)
    if result.returncode != 0 and quiet:
        print(result.stderr.strip() or "Falha em kubectl", file=sys.stderr)
    return result


def ensure_namespace(namespace: str) -> int:
    if kubectl("get", "namespace", namespace, quiet=True).returncode == 0:
        return 0
    print(f"Criando namespace de estudo: {namespace}")
    return kubectl("create", "namespace", namespace).returncode


def execute_lab(lab: Lab, action: str) -> int:
    checked_cluster()  # Também para comandos somente de leitura.
    if action == "lab-status":
        return kubectl("get", "pods,deployments,services,serviceaccounts,resourcequotas", "-n",
                       lab.namespace, "--ignore-not-found", "-o", "wide").returncode
    if action == "lab-up":
        if ensure_namespace(lab.namespace):
            return 1
        for manifest in lab.apply:
            if kubectl("apply", "-f", str(manifest)).returncode:
                return 1
        return 0
    if action == "lab-down":
        # Não apague o namespace: ele pode conter recursos de outras pessoas.
        for manifest in reversed(lab.apply):
            if manifest.name == "namespace.yaml":
                continue
            if kubectl("delete", "-f", str(manifest), "--ignore-not-found").returncode:
                return 1
        print(f"Namespace {lab.namespace} preservado. Revise seus recursos antes de removê-lo.")
        return 0
    if action == "lab-test":
        if not lab.checks:
            print("Lab sem checks: inconclusivo", file=sys.stderr)
            return 2
        for check in lab.checks:
            typ = check["type"]
            if typ == "deployment":
                name = check["name"]
                if kubectl("rollout", "status", f"deployment/{name}", "-n", lab.namespace,
                           "--timeout=120s").returncode:
                    return 1
            elif typ == "service":
                if kubectl("get", "service", check["name"], "-n", lab.namespace).returncode:
                    return 1
            elif typ in ("rbac", "rbac-deny"):
                account = f"system:serviceaccount:{lab.namespace}:{check['service_account']}"
                args = ("auth", "can-i", check["verb"], check["resource"], "-n",
                        lab.namespace, f"--as={account}", "--quiet")
                result = kubectl(*args)
                if typ == "rbac" and result.returncode != 0:
                    return 1
                if typ == "rbac-deny" and result.returncode != 1:
                    # Can-i retorna 1 para 'no'; outros erros também exigem diagnóstico.
                    print("Permissão negativa não confirmada; revise RBAC/impersonation", file=sys.stderr)
                    return 1
            elif typ == "quota":
                if kubectl("get", "resourcequota", check["name"], "-n", lab.namespace).returncode:
                    return 1
                if kubectl("get", "pod", check["pod"], "-n", lab.namespace).returncode:
                    return 1
        print(f"PASS: checks declarados para {lab.identifier}")
        return 0
    raise ValueError(f"Ação não suportada: {action}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Kubernetes Visual Guide — gerenciador de labs")
    parser.add_argument("action", choices=("labs", "doctor", "validate", "lab-up", "lab-test", "lab-status", "lab-down"))
    parser.add_argument("--lab", help="ID do lab, por exemplo 01.06")
    args = parser.parse_args()
    if args.action == "doctor":
        return doctor()
    try:
        labs = load_labs()
    except (ValueError, yaml.YAMLError, OSError) as exc:
        print(f"Erro no catálogo: {exc}", file=sys.stderr)
        return 1
    if args.action.startswith("lab-"):
        if not args.lab or args.lab not in labs:
            print("Informe --lab com um ID válido (consulte make labs)", file=sys.stderr)
            return 2
        try:
            return execute_lab(labs[args.lab], args.action)
        except (ValueError, OSError) as exc:
            print(f"Erro: {exc}", file=sys.stderr)
            return 1
    if args.action == "labs":
        for lab in labs.values():
            print(f"{lab.identifier:6} | {lab.title} | {lab.namespace}")
    else:
        print(f"{len(labs)} laboratórios com contrato válido")
    return 0


if __name__ == "__main__":
    sys.exit(main())
