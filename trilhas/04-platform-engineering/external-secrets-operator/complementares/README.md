# Complementar 04.04 — Segredos: identidade, refresh e governança

[← Aula 04.04](../README.md) · [↑ Camada 04](../../README.md)

> **Leitura opcional:** matriz de decisão e diagnóstico para consulta. Não há laboratório 04.04 nesta trilha: use esta página como referência opcional.

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
kubectl api-resources --api-group=external-secrets.io
# Em um ambiente já autorizado com ESO, somente metadados:
kubectl get secretstore,externalsecret -A
```

**Nunca** execute `kubectl get secret -o yaml` para capturar evidências em logs ou documentos compartilhados.

## Referências oficiais

[ESO](https://external-secrets.io/latest/) · [Fake provider](https://external-secrets.io/latest/provider/fake/)

---

[↑ Aula 04.04](../README.md) · [↑ Camada 04](../../README.md)
