# 04.04 · External Secrets Operator

[⌂ Início](../../../README.md) · [↑ Camada 04](../README.md) · [📚 Catálogo](../../../docs/catalogo.md)

> **Ao concluir esta aula, você será capaz de:** Explicar Store, ExternalSecret, Secret resultante e refresh, sem confundir sincronização de segredos com criptografia automática.

## 🎨 Infográfico

![04.04 — External Secrets Operator](images/external-secrets-operator.png)

## 📖 Aula teórica

### Capacidade da ferramenta

External Secrets Operator (ESO) reconcilia recursos ExternalSecret e busca dados em um provedor configurado por SecretStore ou ClusterSecretStore. O resultado pode ser um Secret Kubernetes consumido por workloads. O ESO não é um cofre por si só, nem transforma dados sensíveis em públicos por estarem codificados em base64.

### Como a reconciliação funciona

A API da ferramenta descreve referência remota, chave/versão, intervalo de refresh e target. O controller autentica no provedor, busca o valor e escreve o Secret de destino. Um `SecretStore` namespaced limita escopo; produção exige identidade mínima e integração real com Secrets Manager, Vault ou outro provedor. O **Fake Provider** é apropriado para testes sem credenciais reais.

### Exemplo interpretado (trecho)

```yaml
apiVersion: external-secrets.io/v1
kind: ExternalSecret
spec:
  refreshInterval: 1h
  secretStoreRef:
    kind: SecretStore
    name: simulado
  target:
    name: segredo-didatico
```

**Interpretação:** o trecho ilustra parte do contrato declarativo, não uma implantação pronta. A aula diferencia a sintaxe aceita pela API das consequências reais produzidas pelo controlador instalado.

### Inspeção no cluster

```bash
kubectl config current-context
kubectl api-resources --api-group=external-secrets.io
kubectl get secretstore,externalsecret -A  # apenas se ESO já estiver instalado em cluster autorizado
```

**Como interpretar:** em um ambiente que já utilize ESO, condições Ready de SecretStore/ExternalSecret e a existência do Secret alvo são sinais úteis. Isso não constitui laboratório nesta trilha; não instale o controlador nem exiba valores de Secrets para completar a aula.

### Limites e segurança

Use **somente valores fictícios** no Fake Provider. Mesmo em testes, evite imprimir conteúdo de Secrets em logs ou colocar tokens reais no Git. `Secret` em etcd requer política de criptografia/segurança separada.

## 🧪 Aplicação prática

**Sem laboratório nesta etapa.** Analise um cenário fictício: uma aplicação precisa receber um Secret de um cofre externo. Identifique a responsabilidade de `SecretStore`, `ExternalSecret` e Secret de destino; explique como tratar identidade, refresh, revogação e falha de sincronização. Não utilize credenciais reais nem crie recursos em cluster.

**Complementar opcional:** [Aprofundamento e diagnóstico](complementares/README.md) para decisões e falhas comuns, sem exigir execução prática.

## ✅ Revisão do aprendizado

- Qual recurso guarda a referência do provedor e qual define o target?
- Por que base64 não oferece confidencialidade?
- Como distinguir erro de autenticação no provider de falha de criação do Secret?

## 🔗 Referências oficiais

- [Documentação oficial de External Secrets Operator](https://external-secrets.io/latest/)

---

[← Aula 04.03](../kyverno/README.md) · [↑ Camada 04](../README.md) · [Próxima: Aula 04.05 →](../karpenter/README.md)
