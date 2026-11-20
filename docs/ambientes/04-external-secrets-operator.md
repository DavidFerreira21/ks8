# Preparação 04.04 — External Secrets Operator sem credenciais

[↑ Ambientes](README.md) · [🧪 Lab 04.04](../../trilhas/04-platform-engineering/labs/external-secrets-operator-basico/README.md)

> **Objetivo:** provar sincronização entre SecretStore Fake e Kubernetes Secret sem expor valores. Não conecte Secrets Manager/Vault nem copie tokens reais.

## Instalar ESO

```bash
kubectl config current-context # kind-dev
helm repo add external-secrets https://charts.external-secrets.io
helm repo update
helm search repo external-secrets/external-secrets --versions | head
export ESO_CHART_VERSION=VERSAO_COMPATIVEL
: "${ESO_CHART_VERSION:?Defina versão do ESO}"
helm install external-secrets external-secrets/external-secrets -n external-secrets --create-namespace --version "$ESO_CHART_VERSION"
kubectl get pods -n external-secrets
kubectl api-resources --api-group=external-secrets.io
```

Confirme que a versão instalada serve `external-secrets.io/v1` para SecretStore e ExternalSecret. Fake Provider não precisa de identidade cloud.

## Teste seguro

```bash
make lab-prepare LAB=04.04
kubectl apply -f .labs/04.04/
kubectl get secretstore,externalsecret -n lab-04-04
kubectl describe externalsecret demo -n lab-04-04
kubectl get secret segredo-didatico -n lab-04-04 -o jsonpath='{.metadata.name}'
```

Observe o status Ready, timestamps e existência do Secret. Não use `kubectl get secret -o yaml` nem publique o conteúdo base64 em screenshots/logs. Altere `remoteRef.key` para chave inexistente **apenas no lab** e restaure o arquivo original.

**Limpeza:** `make lab-down LAB=04.04`, confira o Secret alvo e remova-o explicitamente se persistir; depois `helm uninstall external-secrets -n external-secrets` somente se a instalação era dedicada e outras instâncias não dependem dela.

[Getting Started oficial](https://external-secrets.io/latest/introduction/getting-started/) · [Fake Provider](https://external-secrets.io/latest/provider/fake/)