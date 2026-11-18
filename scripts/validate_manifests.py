#!/usr/bin/env python3
"""Validação estática de exemplos selecionados; não equivale ao schema Kubernetes."""
from pathlib import Path
import sys

try:
    import yaml
except ImportError:
    sys.exit("PyYAML não instalado. Execute: python3 -m pip install 'PyYAML>=6,<7'")

ROOT = Path(__file__).resolve().parent.parent

# path -> (kinds esperados em ordem, namespace dos recursos namespaced)
FILES = {
    "kind-config.yaml": (["Cluster"], None),
    "trilhas/01-fundamentos/labs/primeira-aplicacao/pod.yaml": (["Pod"], "k8s-lab"),
    "trilhas/01-fundamentos/labs/primeira-aplicacao/deployment.yaml": (["Deployment"], "k8s-lab"),
    "trilhas/01-fundamentos/labs/primeira-aplicacao/service.yaml": (["Service"], "k8s-lab"),
    "trilhas/02-operacao-seguranca/labs/rbac-minimo/namespace.yaml": (["Namespace"], None),
    "trilhas/02-operacao-seguranca/labs/rbac-minimo/rbac.yaml": (["ServiceAccount", "Role", "RoleBinding"], "lab-ops-rbac"),
    "trilhas/02-operacao-seguranca/labs/quota-namespace/namespace.yaml": (["Namespace"], None),
    "trilhas/02-operacao-seguranca/labs/quota-namespace/policy.yaml": (["ResourceQuota", "LimitRange"], "lab-ops-quota"),
    "trilhas/02-operacao-seguranca/labs/quota-namespace/pod-ok.yaml": (["Pod"], "lab-ops-quota"),
    "trilhas/02-operacao-seguranca/labs/quota-namespace/pod-rejected.yaml": (["Pod"], "lab-ops-quota"),
}

errors = []
for relative, (expected_kinds, namespace) in FILES.items():
    path = ROOT / relative
    if not path.is_file():
        errors.append(f"{relative}: arquivo não encontrado")
        continue
    try:
        with path.open(encoding="utf-8") as stream:
            docs = list(yaml.safe_load_all(stream))
    except yaml.YAMLError as exc:
        errors.append(f"{relative}: YAML inválido ({exc})")
        continue
    if len(docs) != len(expected_kinds) or not all(isinstance(d, dict) for d in docs):
        errors.append(f"{relative}: estrutura ou quantidade de documentos inesperada")
        continue
    for index, (doc, kind) in enumerate(zip(docs, expected_kinds), start=1):
        prefix = f"{relative}: documento {index}"
        if doc.get("kind") != kind:
            errors.append(f"{prefix}: esperado kind={kind}")
        if not isinstance(doc.get("apiVersion"), str):
            errors.append(f"{prefix}: apiVersion ausente")
        metadata = doc.get("metadata")
        if kind != "Cluster" and not isinstance(metadata, dict):
            errors.append(f"{prefix}: metadata ausente")
            continue
        if namespace and metadata.get("namespace") != namespace:
            errors.append(f"{prefix}: namespace esperado {namespace}")
        if kind == "Deployment":
            spec = doc.get("spec") or {}
            if spec.get("replicas") != 3:
                errors.append(f"{prefix}: esperado replicas=3")
            if (spec.get("selector") or {}).get("matchLabels") != ((spec.get("template") or {}).get("metadata") or {}).get("labels"):
                errors.append(f"{prefix}: selector diverge das labels do template")
        if kind == "Service" and (doc.get("spec") or {}).get("selector") != {"app": "web"}:
            errors.append(f"{prefix}: esperado selector app=web")
        if kind == "Namespace" and metadata.get("name") not in {"lab-ops-rbac", "lab-ops-quota"}:
            errors.append(f"{prefix}: nome de namespace inesperado")
        if kind == "ResourceQuota" and (doc.get("spec") or {}).get("hard", {}).get("pods") != "1":
            errors.append(f"{prefix}: esperado quota de um Pod")
        if kind == "Role":
            rules = doc.get("rules") or []
            if len(rules) != 1 or rules[0].get("resources") != ["pods"] or set(rules[0].get("verbs", [])) != {"get", "list"}:
                errors.append(f"{prefix}: Role deveria permitir somente get/list de pods")
        if kind == "RoleBinding":
            if (doc.get("roleRef") or {}).get("name") != "pod-reader":
                errors.append(f"{prefix}: RoleBinding deve referenciar pod-reader")
    print(f"{'ERRO' if any(e.startswith(relative + ':') for e in errors) else 'OK'}  {relative}")

if errors:
    print("\n".join(errors), file=sys.stderr)
    sys.exit(1)
print("Validação estática concluída. Não substitui validação de schema ou execução em Kind.")
