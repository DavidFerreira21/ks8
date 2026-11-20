#!/usr/bin/env python3
"""Validacao semantica adicional de todos os contratos, sem acesso ao cluster.

A validacao YAML/semantica NAO e substituta do OpenAPI server-side; a CI
Kind executa --dry-run=server para os labs nativos da Camada 03.
"""
from __future__ import annotations

from pathlib import Path
import sys
import yaml

ROOT = Path(__file__).resolve().parents[1]
LABS = ROOT / "trilhas"
CHECKS_WITH_NAME = {"deployment", "service", "resource", "pod-ready", "pvc-bound", "configmap", "quota"}


def documents(path: Path):
    result = list(yaml.safe_load_all(path.read_text(encoding="utf-8")))
    return result


def check_solution(solution: list[dict], label: str) -> list[str]:
    errors: list[str] = []
    objects = {(o.get("kind"), (o.get("metadata") or {}).get("name")): o
               for o in solution if isinstance(o, dict)}
    for obj in solution:
        if not isinstance(obj, dict):
            errors.append(f"{label}: documento invalido")
            continue
        kind = obj.get("kind")
        metadata = obj.get("metadata") or {}
        spec = obj.get("spec") or {}
        prefix = f"{label} {kind}/{metadata.get('name', '?')}"
        if kind in {"Deployment", "DaemonSet", "StatefulSet"}:
            template = spec.get("template") or {}
            template_spec = template.get("spec") or {}
            selector = (spec.get("selector") or {}).get("matchLabels") or {}
            labels = (template.get("metadata") or {}).get("labels") or {}
            if not selector or any(labels.get(k) != v for k, v in selector.items()):
                errors.append(f"{prefix}: selector/template.labels divergentes")
            containers = template_spec.get("containers") or []
            if not containers or any(not isinstance(c, dict) or not c.get("image")
                                     for c in containers):
                errors.append(f"{prefix}: containers/image ausentes")
        if kind == "Pod":
            containers = spec.get("containers") or []
            if not containers or any(not isinstance(c, dict) or not c.get("image")
                                     for c in containers):
                errors.append(f"{prefix}: containers/image ausentes")
        if kind == "Service" and spec.get("type") != "ExternalName":
            if not (spec.get("ports") or []):
                errors.append(f"{prefix}: Service sem porta")
            if not (spec.get("selector") or {}):
                errors.append(f"{prefix}: Service sem selector explicado")
        if kind == "CustomResourceDefinition":
            if not spec.get("group") or not (spec.get("names") or {}).get("plural"):
                errors.append(f"{prefix}: CRD sem grupo/plural")
            if not any(v.get("served") and v.get("storage") and
                       (v.get("schema") or {}).get("openAPIV3Schema")
                       for v in spec.get("versions", [])):
                errors.append(f"{prefix}: CRD sem versao storage+schema")
        if kind == "NamespacedValidatingPolicy":
            if "Deny" not in spec.get("validationActions", []):
                errors.append(f"{prefix}: policy nao demonstra Deny")
            if not spec.get("validations") or not spec.get("matchConstraints"):
                errors.append(f"{prefix}: policy sem expressao/matching")
        if kind == "CiliumNetworkPolicy":
            if not (spec.get("endpointSelector") or {}).get("matchLabels"):
                errors.append(f"{prefix}: sem endpoints selecionados")
            if not spec.get("ingress"):
                errors.append(f"{prefix}: sem ingress")
        if kind == "ServiceMonitor":
            selector = (spec.get("selector") or {}).get("matchLabels") or {}
            endpoints = spec.get("endpoints") or []
            if not selector or not endpoints:
                errors.append(f"{prefix}: selector/endpoints ausentes")
            else:
                candidates = [o for o in solution if isinstance(o, dict)
                              and o.get("kind") == "Service"]
                for port in [x.get("port") for x in endpoints if isinstance(x, dict)]:
                    if not any(all((srv.get("metadata") or {}).get("labels", {}).get(k) == v
                                   for k, v in selector.items())
                               and any(p.get("name") == port
                                       for p in (srv.get("spec") or {}).get("ports", []))
                               for srv in candidates):
                        errors.append(f"{prefix}: endpoint.port nao corresponde a uma porta nomeada de Service com selector compatível ({port})")
    return errors


def validate(root: Path = LABS) -> list[str]:
    errors: list[str] = []
    count = 0
    for contract in sorted(root.glob("*/labs/*/lab.yaml")):
        count += 1
        try:
            meta = yaml.safe_load(contract.read_text(encoding="utf-8"))
            solution = []
            for rel in meta.get("apply", []):
                solution.extend(documents(contract.parent / rel))
            errors.extend(check_solution(solution, meta.get("id", str(contract))))
            names = {(o.get("metadata") or {}).get("name") for o in solution
                     if isinstance(o, dict)}
            for check in meta.get("checks", []):
                if check.get("type") in CHECKS_WITH_NAME and check.get("name") not in names:
                    errors.append(f"{contract}: check {check.get('name')} nao aparece na solucao")
            for directory in ("examples", "experiments"):
                path = contract.parent / directory
                for manifest in path.rglob("*.yaml") if path.is_dir() else []:
                    if not documents(manifest):
                        errors.append(f"{manifest}: YAML de exemplo vazio")
        except (OSError, ValueError, TypeError, yaml.YAMLError, AttributeError) as exc:
            errors.append(f"{contract}: {exc}")
    if count != 49:
        errors.append(f"Esperados 49 contratos, encontrados {count}")
    return errors


if __name__ == "__main__":
    problems = validate()
    if problems:
        print("\n".join(problems), file=sys.stderr)
        sys.exit(1)
    print("PASS: 49 contratos, semantica de APIs e YAMLs opcionais validos; "
          "schema da API exige dry-run de servidor.")
