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


def main() -> int:
    parser = argparse.ArgumentParser(description="Kubernetes Visual Guide — gerenciador de labs")
    parser.add_argument("action", choices=("labs", "doctor", "validate"))
    args = parser.parse_args()
    if args.action == "doctor":
        return doctor()
    try:
        labs = load_labs()
    except (ValueError, yaml.YAMLError, OSError) as exc:
        print(f"Erro no catálogo: {exc}", file=sys.stderr)
        return 1
    if args.action == "labs":
        for lab in labs.values():
            print(f"{lab.identifier:6} | {lab.title} | {lab.namespace}")
    else:
        print(f"{len(labs)} laboratórios com contrato válido")
    return 0


if __name__ == "__main__":
    sys.exit(main())
