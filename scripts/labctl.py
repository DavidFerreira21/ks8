#!/usr/bin/env python3
"""Catálogo declarativo de labs. Execução e observação entram nos PRs seguintes."""
from __future__ import annotations

import argparse
import base64
import json
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
SUPPORTED_CHECKS = {"deployment", "service", "rbac", "rbac-deny", "quota", "configmap", "resource", "pod-ready", "pvc-bound"}
SUPPORTED_EXPERIMENTS = {"expect-rejected-manifest", "rollout-restart"}


@dataclass(frozen=True)
class Lab:
    identifier: str
    title: str
    namespace: str
    directory: Path
    apply: tuple[Path, ...]
    checks: tuple[dict, ...]
    experiments: tuple[dict, ...]
    setup: tuple[Path, ...] = ()
    starter: tuple[Path, ...] = ()


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
        setup_names = data.get("setup", [])
        starter_names = data.get("starter", [])
        if not isinstance(setup_names, list) or not isinstance(starter_names, list):
            raise ValueError(f"{metadata}: setup/starter devem ser listas")
        setup = tuple(manifest(name) for name in setup_names)
        starter = tuple(manifest(name) for name in starter_names)
        if starter and len(starter) != len(apply):
            raise ValueError(f"{metadata}: starter e apply devem ter mesmo numero de arquivos")
        checks = data.get("checks", [])
        if not isinstance(checks, list) or any(not isinstance(x, dict) or x.get("type") not in SUPPORTED_CHECKS for x in checks):
            raise ValueError(f"{metadata}: checks não suportados")
        experiments = data.get("experiments", [])
        if not isinstance(experiments, list) or any(not isinstance(x, dict) or x.get("type") not in SUPPORTED_EXPERIMENTS for x in experiments):
            raise ValueError(f"{metadata}: experiments não suportados")
        for experiment in experiments:
            if not isinstance(experiment.get("id"), str) or not SAFE_NAME.fullmatch(experiment["id"]):
                raise ValueError(f"{metadata}: id de experimento inválido")
            if experiment["type"] == "expect-rejected-manifest":
                manifest(experiment.get("manifest"))
            elif experiment["type"] == "rollout-restart":
                name = experiment.get("deployment")
                if not isinstance(name, str) or not SAFE_NAME.fullmatch(name):
                    raise ValueError(f"{metadata}: nome de Deployment inválido")
                if not any(x.get("type") == "deployment" and x.get("name") == name for x in checks):
                    raise ValueError(f"{metadata}: rollout deve referenciar Deployment declarado nos checks")
        for check in checks:
            if check["type"] in {"resource", "pod-ready", "pvc-bound"}:
                if not isinstance(check.get("name"), str) or not SAFE_NAME.fullmatch(check["name"]):
                    raise ValueError(f"{metadata}: nome de check inválido")
                if check["type"] == "resource":
                    allowed = {"daemonset", "statefulset", "ingress", "hpa", "secret", "namespace", "configmap", "service", "deployment", "pvc", "pod", "limitRange", "job", "cronjob", "networkpolicy", "appenvironments.learning.example", "applications.argoproj.io", "compositeresourcedefinition", "namespacedvalidatingpolicy", "secretstore", "externalsecret", "nodepool", "ciliumnetworkpolicy", "servicemonitor"}
                    if check.get("kind") not in allowed:
                        raise ValueError(f"{metadata}: kind de check não permitido")
        labs[identifier] = Lab(identifier, title, namespace, metadata.parent, apply, tuple(checks), tuple(experiments), setup, starter)
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
    # Namespace ausente e falha no API Server sao casos diferentes.
    result = subprocess.run(
        ["kubectl", "get", "namespace", namespace, "--ignore-not-found", "-o", "name"],
        capture_output=True, text=True, check=False,
    )
    if result.returncode != 0:
        print(f"Erro ao consultar namespace {namespace}: {result.stderr.strip()}", file=sys.stderr)
        return result.returncode
    if result.stdout.strip():
        return 0
    print(f"Criando namespace de estudo: {namespace}")
    return kubectl("create", "namespace", namespace).returncode


def observe_lab(lab: Lab) -> int:
    print(f"\n=== {lab.identifier}: {lab.title} ===")
    print(f"Namespace: {lab.namespace}")
    kubectl("get", "pods,deployments,replicasets,daemonsets,statefulsets,services,ingresses,hpa,pvc,configmaps,secrets,serviceaccounts,resourcequotas", "-n",
            lab.namespace, "--ignore-not-found", "-o", "wide")
    print("\n=== Eventos ===")
    kubectl("get", "events", "-n", lab.namespace, "--sort-by=.lastTimestamp")
    for check in lab.checks:
        if check["type"] in ("deployment", "quota"):
            kind = "deployment" if check["type"] == "deployment" else "resourcequota"
            kubectl("describe", kind, check["name"], "-n", lab.namespace)
        if check["type"] == "service":
            kubectl("get", "endpointslices", "-n", lab.namespace,
                    "-l", f"kubernetes.io/service-name={check['name']}")
    print("\nPerguntas: o estado observado atende à intenção? Que eventos explicam divergências?")
    print("Para acompanhar a reconciliação ao vivo, abra outro terminal e execute kubectl get pods -w -n", lab.namespace)
    return 0


def perform_experiment(lab: Lab, experiment_id: str | None, confirm: bool) -> int:
    experiment = next((x for x in lab.experiments if x["id"] == experiment_id), None)
    if experiment is None:
        available = ", ".join(x["id"] for x in lab.experiments) or "(nenhum)"
        print(f"Experimento inválido. Disponíveis: {available}", file=sys.stderr)
        return 2
    if not confirm:
        print("Experimento modifica recursos. Repita com --confirm depois de revisar o lab.yaml.", file=sys.stderr)
        return 2
    if experiment["type"] == "rollout-restart":
        deployment = experiment["deployment"]
        print(f"Experimento: reiniciar o Deployment {deployment} em {lab.namespace}")
        if kubectl("get", "deployment", deployment, "-n", lab.namespace).returncode:
            return 1
        if kubectl("rollout", "restart", f"deployment/{deployment}", "-n", lab.namespace).returncode:
            return 1
        return kubectl("rollout", "status", f"deployment/{deployment}", "-n",
                       lab.namespace, "--timeout=120s").returncode
    if experiment["type"] == "expect-rejected-manifest":
        name = experiment["manifest"]
        manifest = (lab.directory / name).resolve()
        print(f"Experimento: esperar rejeição de admissão para {name}")
        proc = subprocess.run(["kubectl", "apply", "-f", str(manifest)],
                              capture_output=True, text=True, check=False)
        output = (proc.stdout + proc.stderr).lower()
        if proc.returncode != 0 and ("exceeded quota" in output or "excedeu" in output):
            print("PASS: falha de admissão por quota observada\n" + proc.stderr.strip())
            return 0
        if proc.returncode == 0:
            print("FAIL: manifesto foi admitido; revise quota e Pods existentes", file=sys.stderr)
        else:
            print("FAIL: erro diferente de quota; confira os detalhes:\n" + proc.stderr, file=sys.stderr)
        return 1
    return 2


def prepare_lab(lab: Lab) -> int:
    """Prepara namespace, backends de apoio e arquivos locais sem aplicar a solucao."""
    if ensure_namespace(lab.namespace):
        return 1
    for manifest in lab.setup:
        if kubectl("apply", "-f", str(manifest)).returncode:
            return 1
    if lab.starter:
        workspace = ROOT / ".labs" / lab.identifier
        workspace.mkdir(parents=True, exist_ok=True)
        for template in lab.starter:
            target = workspace / template.name
            if not target.exists():
                shutil.copyfile(template, target)
                print(f"Arquivo de exercicio criado: {target.relative_to(ROOT)}")
            else:
                print(f"Arquivo existente preservado: {target.relative_to(ROOT)}")
        print(f"Edite .labs/{lab.identifier}/ e execute kubectl apply -f .labs/{lab.identifier}/")
        print(f"Depois valide: make lab-test LAB={lab.identifier}")
    return 0


def remove_lab_objects(lab: Lab) -> int:
    for manifest in reversed((*lab.setup, *lab.apply)):
        if manifest.name == "namespace.yaml":
            continue
        if kubectl("delete", "-f", str(manifest), "--ignore-not-found").returncode:
            return 1
    return 0


def expected_subset(actual, expected, prefix: str = "") -> list[str]:
    """Compara somente os campos requeridos na solucao, ignorando defaults da API."""
    if isinstance(expected, dict):
        if not isinstance(actual, dict):
            return [f"{prefix}: mapeamento esperado"]
        issues = []
        for key, value in expected.items():
            location = f"{prefix}.{key}" if prefix else key
            if key not in actual:
                issues.append(f"{location}: campo ausente")
            else:
                issues.extend(expected_subset(actual[key], value, location))
        return issues
    if isinstance(expected, list):
        if not isinstance(actual, list) or len(actual) < len(expected):
            return [f"{prefix}: quantidade de itens insuficiente"]
        issues = []
        for i, item in enumerate(expected):
            issues.extend(expected_subset(actual[i], item, f"{prefix}[{i}]"))
        return issues
    return [] if actual == expected else [f"{prefix}: esperado {expected!r}, observado {actual!r}"]


def check_student_manifest(lab: Lab) -> int:
    """Verifica campos funcionais da API contra a solucao, nao apenas existencia."""
    for manifest in lab.apply:
        for expected in yaml.safe_load_all(manifest.read_text(encoding="utf-8")):
            metadata = expected["metadata"]
            kind, name = expected["kind"], metadata["name"]
            proc = subprocess.run(
                ["kubectl", "get", kind, name, "-n", lab.namespace, "-o", "json"],
                capture_output=True, text=True, check=False,
            )
            if proc.returncode:
                print(f"FAIL: {kind}/{name} nao encontrado em {lab.namespace}", file=sys.stderr)
                return 1
            actual = json.loads(proc.stdout)
            fields = {}
            for field in ("spec", "data", "type"):
                if field in expected:
                    fields[field] = expected[field]
            # Labels e annotations fazem parte do contrato quando declaradas
            # na solucao, mas metadados gerados pelo API Server sao ignorados.
            expected_metadata = {
                key: metadata[key]
                for key in ("labels", "annotations")
                if key in metadata
            }
            if expected_metadata:
                fields["metadata"] = expected_metadata
            if kind in {"Role", "ClusterRole", "RoleBinding", "ClusterRoleBinding"}:
                for key in ("rules", "subjects", "roleRef"):
                    if key in expected:
                        fields[key] = expected[key]
            if kind == "PriorityClass":
                for key in ("value", "globalDefault", "preemptionPolicy"):
                    if key in expected:
                        fields[key] = expected[key]
            if kind == "Secret" and "stringData" in expected:
                fields["data"] = {
                    k: base64.b64encode(str(v).encode("utf-8")).decode("ascii")
                    for k, v in expected["stringData"].items()
                }
            problems = expected_subset(actual, fields)
            if problems:
                print(f"FAIL: {kind}/{name} divergente da especificacao do desafio:", file=sys.stderr)
                for issue in problems[:12]:
                    print(f"  - {issue}", file=sys.stderr)
                return 1
    return 0


def execute_lab(lab: Lab, action: str) -> int:
    if action == "lab-solution":
        for path in lab.apply:
            print(path.relative_to(ROOT))
        print("Solucao de referencia: nao aplicada.")
        return 0
    checked_cluster()
    if action == "lab-observe":
        return observe_lab(lab)
    if action == "lab-status":
        return kubectl("get", "pods,deployments,daemonsets,statefulsets,services,ingresses,hpa,pvc,configmaps,serviceaccounts,resourcequotas", "-n",
                       lab.namespace, "--ignore-not-found", "-o", "wide").returncode
    if action == "lab-prepare":
        return prepare_lab(lab)
    if action == "lab-reset":
        if remove_lab_objects(lab):
            return 1
        print("Recursos removidos; seus arquivos em .labs/ foram preservados.")
        return prepare_lab(lab)
    if action == "lab-up":
        if ensure_namespace(lab.namespace):
            return 1
        for manifest in (*lab.setup, *lab.apply):
            if kubectl("apply", "-f", str(manifest)).returncode:
                return 1
        return 0
    if action == "lab-down":
        # Não apague o namespace: ele pode conter recursos de outras pessoas.
        if remove_lab_objects(lab):
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
                        lab.namespace, f"--as={account}")
                result = subprocess.run(["kubectl", *args], capture_output=True, text=True, check=False)
                expected_answer = "yes" if typ == "rbac" else "no"
                # Um erro de impersonation não equivale a uma negativa RBAC.
                if result.returncode not in (0, 1) or result.stdout.strip().lower() != expected_answer:
                    print(f"Falha RBAC ({expected_answer} esperado): {result.stdout} {result.stderr}", file=sys.stderr)
                    return 1
            elif typ == "resource":
                if kubectl("get", check["kind"], check["name"], "-n", lab.namespace).returncode:
                    return 1
            elif typ == "pod-ready":
                if kubectl("wait", "--for=condition=Ready", f"pod/{check['name']}", "-n",
                           lab.namespace, "--timeout=120s").returncode:
                    return 1
            elif typ == "pvc-bound":
                if kubectl("wait", "--for=jsonpath={.status.phase}=Bound",
                           f"pvc/{check['name']}", "-n", lab.namespace, "--timeout=120s").returncode:
                    return 1
            elif typ == "configmap":
                if kubectl("get", "configmap", check["name"], "-n", lab.namespace).returncode:
                    return 1
            elif typ == "quota":
                if kubectl("get", "resourcequota", check["name"], "-n", lab.namespace).returncode:
                    return 1
                if kubectl("get", "pod", check["pod"], "-n", lab.namespace).returncode:
                    return 1
        if lab.starter and check_student_manifest(lab):
            return 1
        print(f"PASS: checks declarados para {lab.identifier}")
        return 0
    raise ValueError(f"Ação não suportada: {action}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Kubernetes Visual Guide — gerenciador de labs")
    parser.add_argument("action", choices=("labs", "doctor", "validate", "lab-prepare", "lab-solution", "lab-reset", "lab-up", "lab-test", "lab-status", "lab-down", "lab-observe", "lab-experiment"))
    parser.add_argument("--lab", help="ID do lab, por exemplo 01.06")
    parser.add_argument("--experiment", help="ID do experimento definido no lab.yaml")
    parser.add_argument("--confirm", action="store_true", help="Confirma a mutação do experimento")
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
            if args.action == "lab-experiment":
                checked_cluster()
                return perform_experiment(labs[args.lab], args.experiment, args.confirm)
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
