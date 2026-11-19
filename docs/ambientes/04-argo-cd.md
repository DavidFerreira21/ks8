# Preparação 04.01 — Argo CD no Kind

[↑ Ambientes](README.md) · [🧪 Lab 04.01](../../trilhas/04-platform-engineering/labs/argo-cd-basico/README.md)

> **Isolamento:** cluster descartável `kind-dev`; Helm chart e versão escolhidos explicitamente. Este guia instala o Argo CD no **mesmo namespace da Application** (`lab-04-01`), evitando exigir "Applications in any namespace".

## Pré-requisitos e versão

```bash
kubectl config current-context   # deve mostrar kind-dev
helm version
helm repo add argo https://argoproj.github.io/argo-helm
helm repo update
helm search repo argo/argo-cd --versions | head
# Após revisar uma versão compatível, defina:
export ARGO_CD_CHART_VERSION=VERSAO_ESCOLHIDA
: "${ARGO_CD_CHART_VERSION:?Defina versão de chart revisada}"
```

Não use a string literal `VERSAO_ESCOLHIDA`: substitua-a por uma versão real. Registre o chart e a versão usada na evidência.

## Instalar e comprovar API

```bash
helm install argocd argo/argo-cd --namespace lab-04-01 --create-namespace --version "$ARGO_CD_CHART_VERSION"
kubectl get pods -n lab-04-01
kubectl get crd applications.argoproj.io
kubectl get appprojects.argoproj.io -n lab-04-01
helm status argocd -n lab-04-01
```

Confirme todos os componentes essenciais do Argo CD como Ready antes do lab. O projeto `default` e o destino precisam estar permitidos. O repositório de exemplo do lab é público; verificar sua disponibilidade e pin de revisão faz parte da prática.

## Executar, diagnosticar e limpar

```bash
make lab-prepare LAB=04.01
kubectl apply -f .labs/04.01/
kubectl get applications.argoproj.io -n lab-04-01
kubectl describe application guestbook-estudo -n lab-04-01
```

Sincronize manualmente na UI/CLI após confirmar acesso. Registre `sync.status`, `health.status` e um diff antes/depois de alterar um recurso gerenciado no lab. `Synced` e `Healthy` são sinais diferentes.

**Limpeza:** primeiro remova a Application e quaisquer recursos filhos criados por ela de forma controlada, observando política de finalizer/prune; só então execute `helm uninstall argocd -n lab-04-01`. Inspecione CRDs globais remanescentes — nunca apague CRDs compartilhadas por outros estudos.

[Instalação oficial](https://argo-cd.readthedocs.io/en/stable/getting_started/) · [Applications in any namespace](https://argo-cd.readthedocs.io/en/stable/operator-manual/app-any-namespace/)