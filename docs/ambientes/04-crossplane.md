# Preparação 04.02 — Crossplane v2 no Kind

[↑ Ambientes](README.md) · [🧪 Lab 04.02](../../trilhas/04-platform-engineering/labs/crossplane-basico/README.md)

> **Isolamento:** cluster `kind-dev` descartável, sem Providers cloud nem credenciais. XRD, Function e Composition são objetos globais; inventarie dependências antes de excluí-los.

## Instalação com versão fixada

```bash
kubectl config current-context # kind-dev
helm repo add crossplane-stable https://charts.crossplane.io/stable
helm repo update
helm search repo crossplane-stable/crossplane --versions | head
export CROSSPLANE_CHART_VERSION=VERSAO_V2_COMPATIVEL
: "${CROSSPLANE_CHART_VERSION:?Defina chart Crossplane v2}"
helm install crossplane crossplane-stable/crossplane -n crossplane-system --create-namespace --version "$CROSSPLANE_CHART_VERSION"
kubectl get pods -n crossplane-system
kubectl api-resources --api-group=apiextensions.crossplane.io
kubectl get xrd
```

Escolha e registre uma versão real do chart compatível com Crossplane v2; confirme o campo `apiVersion: apiextensions.crossplane.io/v2` no lab antes de prosseguir.

## Exercício básico e avançado

```bash
make lab-prepare LAB=04.02
kubectl apply -f .labs/04.02/resources.yaml
kubectl get xrd xenvironments.platform.example.org
kubectl api-resources --api-group=platform.example.org
```

O básico valida **XRD + XR e schema**. A [Fase opcional com Function e Composition](../../trilhas/04-platform-engineering/labs/crossplane-basico/examples/composition-avancada/README.md) instala uma Function de Go templates e reconcilia um ConfigMap namespaced; não precisa de Provider AWS.

## Evidências e reversão

Registre `Established`, `Ready`, Function `HEALTHY`, Composition selecionada e ConfigMap gerado. Não chame uma XR isolada de infraestrutura provisionada.

Remova primeiro as XRs didáticas, confirme a ausência de instâncias em **todos os namespaces**, depois Composition/Function **somente se criadas para este lab**, depois XRD, e só então `helm uninstall crossplane -n crossplane-system`. Não force finalizers ou exclusões globais em clusters compartilhados.

[Instalação oficial](https://docs.crossplane.io/latest/get-started/install/) · [Compositions](https://docs.crossplane.io/latest/composition/compositions/)