# Complementar 03.02 — Trilha de uma requisição à API

[← Aula 03.02](../README.md) · [🧪 Lab 03.02](../../labs/kube-apiserver-basico/README.md) · [↑ Camada 03](../../README.md)

> **Leitura opcional:** referência de arquitetura, comparação e diagnóstico; não substitui o percurso prático da aula e do lab.

## Quando consultar

Ao diferenciar erro de conexão, autenticação, autorização, validação e falha após persistência.

| Resposta/observação | Interpretação inicial | Próxima evidência |
| --- | --- | --- |
| API inacessível | Rede/TLS/endpoint | `kubectl cluster-info`, contexto |
| 401 | Autenticação insuficiente | Token/identidade, sem expor credenciais |
| 403 | Falha de autorização | RBAC/`kubectl auth can-i` |
| 422/validation | Schema, admission ou objeto inválido | Detalhes da resposta e policies |
| Objeto criado, Pod Pending | Scheduling/volume, não erro da escrita na API | Events e condições |

## Diagnóstico prático

```bash
kubectl config current-context
kubectl api-resources
kubectl auth can-i create configmaps -n lab-03-02
kubectl explain configmap.data
```

**Decisão:** compare `--dry-run=server` e `--dry-run=client` para identificar onde ocorre a validação. Não use credenciais reais em exemplos.

## Referências oficiais

[Kubernetes API](https://kubernetes.io/docs/reference/using-api/) · [Access control](https://kubernetes.io/docs/reference/access-authn-authz/)

---

[↑ Aula 03.02](../README.md) · [↑ Camada 03](../../README.md)
