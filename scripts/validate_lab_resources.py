#!/usr/bin/env python3
"""Valida todos os manifests registrados nos contratos dos labs sem um cluster."""
from pathlib import Path
import sys
import yaml

ROOT = Path(__file__).resolve().parents[1]
LABS = ROOT / "trilhas"
CLUSTER_SCOPED = {"Namespace", "Node", "PersistentVolume", "StorageClass",
                  "ClusterRole", "ClusterRoleBinding", "CustomResourceDefinition"}

def validate() -> list[str]:
    errors = []
    found = 0
    for contract in sorted(LABS.glob("*/labs/*/lab.yaml")):
        found += 1
        try:
            data = yaml.safe_load(contract.read_text(encoding="utf-8"))
            if not isinstance(data, dict):
                raise ValueError("contrato não é um mapeamento")
            namespace = data.get("namespace")
            for name in data.get("apply", []):
                manifest = (contract.parent / name).resolve()
                if not manifest.is_relative_to(contract.parent.resolve()) or not manifest.is_file():
                    raise ValueError(f"manifest inválido: {name}")
                documents = list(yaml.safe_load_all(manifest.read_text(encoding="utf-8")))
                if not documents or any(not isinstance(obj, dict) for obj in documents):
                    raise ValueError(f"{name}: documentos YAML vazios ou inválidos")
                for i, obj in enumerate(documents, 1):
                    kind = obj.get("kind")
                    metadata = obj.get("metadata")
                    if not isinstance(obj.get("apiVersion"), str) or not isinstance(kind, str):
                        errors.append(f"{manifest}: documento {i}: apiVersion/kind ausente")
                    if not isinstance(metadata, dict) or not metadata.get("name"):
                        errors.append(f"{manifest}: documento {i}: metadata.name ausente")
                    elif kind not in CLUSTER_SCOPED and metadata.get("namespace") != namespace:
                        errors.append(f"{manifest}: documento {i}: namespace deve ser {namespace}")
                    if kind in {"Deployment", "DaemonSet", "StatefulSet"}:
                        spec = obj.get("spec") or {}
                        selector = (spec.get("selector") or {}).get("matchLabels")
                        labels = ((spec.get("template") or {}).get("metadata") or {}).get("labels")
                        if not selector or not labels or any(labels.get(k) != v for k, v in selector.items()):
                            errors.append(f"{manifest}: documento {i}: selector não coincide com labels do template")
        except (yaml.YAMLError, OSError, ValueError, TypeError) as exc:
            errors.append(f"{contract}: {exc}")
    if not found:
        errors.append("Nenhum contrato encontrado")
    print(f"Validacao de manifests registrados: {found} labs")
    return errors

if __name__ == "__main__":
    messages = validate()
    if messages:
        print("\n".join(messages), file=sys.stderr)
        sys.exit(1)
    print("PASS: manifests dos labs possuem estrutura basica valida")
