# Preparação 04.02 — Kyverno e políticas CEL

[↑ Ambientes](README.md) · [🧪 Lab 04.02](../../trilhas/04-platform-engineering/labs/kyverno-basico/README.md)

> **Escopo:** policies em `lab-04-02`; nunca comece com validação `Deny` em todo o cluster. Use Kyverno **compatível com `policies.kyverno.io/v1`**.

## Instalar controlador e CRDs

```bash
kubectl config current-context # kind-dev
helm repo add kyverno https://kyverno.github.io/kyverno/
helm repo update
helm search repo kyverno/kyverno --versions | head
export KYVERNO_CHART_VERSION=VERSAO_CEL_COMPATIVEL
: "${KYVERNO_CHART_VERSION:?Defina versão Kyverno compatível}"
helm install kyverno kyverno/kyverno --namespace kyverno --create-namespace --version "$KYVERNO_CHART_VERSION"
kubectl get pods -n kyverno
kubectl api-resources --api-group=policies.kyverno.io
kubectl get crd namespacedvalidatingpolicies.policies.kyverno.io
```

Verifique `NamespacedValidatingPolicy` em v1 e webhooks/controladores saudáveis. A documentação oficial indica Kyverno 1.17+ para essa família; prefira uma versão estável compatível revisada.

## Testar admissão, não apenas YAML

```bash
make lab-prepare LAB=04.02
kubectl apply -f .labs/04.02/
kubectl get namespacedvalidatingpolicy requer-equipe -n lab-04-02
kubectl apply --dry-run=server -f trilhas/04-platform-engineering/labs/kyverno-basico/examples/sem-label.yaml
kubectl apply --dry-run=server -f trilhas/04-platform-engineering/labs/kyverno-basico/examples/com-label.yaml
```

A primeira requisição deve **falhar** por admissão; a segunda deve passar. Se ambas passarem, investigue readiness, matching e webhooks — não declare enforcement.

**Limpeza:** `make lab-down LAB=04.02` remove a policy namespaced. Depois de revisar outras policies e o uso do addon, `helm uninstall kyverno -n kyverno` somente no cluster descartável. CRDs restantes exigem inventário.

[Quick Start oficial](https://kyverno.io/docs/introduction/quick-start/) · [Policies CEL](https://kyverno.io/docs/policy-types/validating-policy/)