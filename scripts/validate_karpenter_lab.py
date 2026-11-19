#!/usr/bin/env python3
"""Confere o desafio Karpenter 04.05 sem cluster AWS e sem executar apply."""
from __future__ import annotations
import argparse
from pathlib import Path
import sys
import yaml

def validate(manifest: Path) -> list[str]:
    errors: list[str] = []
    try:
        docs = list(yaml.safe_load_all(manifest.read_text(encoding="utf-8")))
    except (OSError, yaml.YAMLError) as exc:
        return [f"Não foi possível ler YAML: {exc}"]
    if len(docs) != 1 or not isinstance(docs[0], dict):
        return ["Esperado um único NodePool YAML"]
    doc = docs[0]
    if doc.get("apiVersion") != "karpenter.sh/v1" or doc.get("kind") != "NodePool":
        errors.append("Esperado karpenter.sh/v1 NodePool")
    if (doc.get("metadata") or {}).get("name") != "estudo-sem-provisionar":
        errors.append("Nome NodePool deve ser estudo-sem-provisionar")
    spec = doc.get("spec") or {}
    if (spec.get("limits") or {}).get("nodes") != 0:
        errors.append("SEGURANÇA: limits.nodes deve ser número 0")
    tpl = ((spec.get("template") or {}).get("spec") or {})
    ref = tpl.get("nodeClassRef") or {}
    if ref != {"group": "karpenter.k8s.aws", "kind": "EC2NodeClass", "name": "nao-configurada"}:
        errors.append("NodeClass precisa apontar exatamente para EC2NodeClass nao-configurada")
    req = tpl.get("requirements") or []
    expected = {"kubernetes.io/arch": "amd64", "karpenter.sh/capacity-type": "on-demand"}
    for key, value in expected.items():
        matches = [r for r in req if isinstance(r, dict) and r.get("key") == key
                   and r.get("operator") == "In" and value in r.get("values", [])]
        if not matches:
            errors.append(f"Requirement ausente ou errado: {key} In [{value}]")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Validação offline e segura do Lab 04.05")
    parser.add_argument("manifest", type=Path, help="Arquivo YAML do aluno, não solution/")
    args = parser.parse_args()
    errors = validate(args.manifest)
    if errors:
        for error in errors:
            print(f"FAIL: {error}", file=sys.stderr)
        return 1
    print("PASS: NodePool didático atende ao contrato sem criar recursos AWS.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
