# Complementar 04.04 — Segredos: identidade, refresh e governança

[← Aula 04.04](../README.md) · [🧪 Lab 04.04](../../labs/external-secrets-operator-basico/README.md) · [↑ Camada 04](../../README.md)

> **Leitura opcional:** matriz de decisão e diagnóstico para consulta. Não é pré-requisito para executar o laboratório.

## Quando consultar

Ao migrar tokens de scripts para store externo, planejar credenciais mínimas ou investigar Secret não sincronizado.

| Recurso | Responsabilidade | Evidência |
| --- | --- | --- |
| SecretStore | Provedor e autenticação namespaced | Ready/errors |
| ExternalSecret | Referência, transformação, refresh | Ready/Sync status |
| Kubernetes Secret | Objeto de destino | Metadata e timestamps |
| Store externo | Origem autoritativa dos dados | Auditoria e IAM do provedor |

## Segurança e rotação

Use credenciais de curto prazo e identidade de workload quando suportadas. RBAC de leitura de Secrets Kubernetes continua relevante; base64 não protege dados. Definir intervalo de refresh não prova atualização instantânea nem revogação da credencial antiga.

```bash
kubectl describe secretstore simulado -n lab-04-04
kubectl describe externalsecret demo -n lab-04-04
kubectl get secret segredo-didatico -n lab-04-04 -o jsonpath='{.metadata.name}'
```

**Nunca** execute `kubectl get secret -o yaml` para capturar evidências em logs ou documentos compartilhados.

## Referências oficiais

[ESO](https://external-secrets.io/latest/) · [Fake provider](https://external-secrets.io/latest/provider/fake/)

---

[↑ Aula 04.04](../README.md) · [↑ Camada 04](../../README.md)
