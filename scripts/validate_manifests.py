#!/usr/bin/env python3
"""Verificação estática dos exemplos principais; não substitui validação por schema."""
from pathlib import Path
import sys

try:
    import yaml
except ImportError:
    sys.exit("PyYAML não instalado. Execute: python3 -m pip install 'PyYAML>=6,<7'")

ROOT = Path(__file__).resolve().parent.parent
FILES = {
    "kind-config.yaml": ("Cluster", None),
    "trilhas/01-fundamentos/labs/primeira-aplicacao/pod.yaml": ("Pod", "k8s-lab"),
    "trilhas/01-fundamentos/labs/primeira-aplicacao/deployment.yaml": ("Deployment", "k8s-lab"),
    "trilhas/01-fundamentos/labs/primeira-aplicacao/service.yaml": ("Service", "k8s-lab"),
}

errors = []
for relative, (expected_kind, expected_namespace) in FILES.items():
    path = ROOT / relative
    if not path.exists():
        errors.append(f"{relative}: arquivo não encontrado")
        continue
    try:
        with path.open(encoding="utf-8") as f:
            docs = list(yaml.safe_load_all(f))
    except yaml.YAMLError as exc:
        errors.append(f"{relative}: YAML inválido ({exc})")
        continue
    if len(docs) != 1 or not isinstance(docs[0], dict):
        errors.append(f"{relative}: esperado exatamente um documento YAML de objeto")
        continue
    obj = docs[0]
    if obj.get("kind") != expected_kind:
        errors.append(f"{relative}: kind esperado {expected_kind}")
    if not isinstance(obj.get("apiVersion"), str):
        errors.append(f"{relative}: apiVersion ausente")
    if expected_namespace and obj.get("metadata", {}).get("namespace") != expected_namespace:
        errors.append(f"{relative}: namespace esperado {expected_namespace}")
    if expected_kind == "Deployment":
        spec = obj.get("spec", {})
        if spec.get("replicas") != 3:
            errors.append(f"{relative}: o lab espera três réplicas")
        if spec.get("selector", {}).get("matchLabels") != spec.get("template", {}).get("metadata", {}).get("labels"):
            errors.append(f"{relative}: selector e labels do Pod não correspondem")
    if expected_kind == "Service" and obj.get("spec", {}).get("selector") != {"app": "web"}:
        errors.append(f"{relative}: selector do Service deve ser app=web")
    print(f"{'ERRO' if any(e.startswith(relative + ':') for e in errors) else 'OK'}  {relative}")

if errors:
    print("\n".join(errors), file=sys.stderr)
    sys.exit(1)
print("Validação estática concluída. Não substitui kubectl dry-run nem testes em Kind.")
