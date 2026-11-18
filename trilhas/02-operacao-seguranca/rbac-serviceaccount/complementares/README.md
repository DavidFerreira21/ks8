# Complementar 02.02 — RBAC: matriz de permissões

[← Aula 02.02](../README.md) · [🧪 Lab 02.02](../../labs/rbac-minimo/README.md) · [↑ Camada 02](../../README.md)

> **Leitura opcional.** Referência para consulta após a aula e o lab; não é pré-requisito e não repete o desafio YAML.

## Quando consultar

Ao auditar escopo de permissões ou investigar uma ServiceAccount com acesso excessivo.

## Comparação de objetos

| Recurso | Escopo | Finalidade |
| --- | --- | --- |
| ServiceAccount | Namespace | Identidade de workload |
| Role | Namespace | Regras de verbos/recursos |
| RoleBinding | Namespace | Atribuição de Role ou ClusterRole naquele namespace |
| ClusterRole | Cluster | Regras reutilizáveis ou globais |
| ClusterRoleBinding | Cluster | Atribuição de ClusterRole com escopo do cluster |

## Diagnóstico

```bash
kubectl auth can-i list pods -n NAMESPACE --as=system:serviceaccount:NAMESPACE:SA
kubectl auth can-i list secrets -n NAMESPACE --as=system:serviceaccount:NAMESPACE:SA
kubectl describe rolebinding NOME -n NAMESPACE
```

Impersonation exige autorização do executor. Não atribua `cluster-admin` para eliminar uma falha didática; identifique o sujeito, verbos, recursos e escopo do binding.

## Referências oficiais

[RBAC](https://kubernetes.io/docs/reference/access-authn-authz/rbac/) · [ServiceAccounts](https://kubernetes.io/docs/concepts/security/service-accounts/)

---

[↑ Aula 02.02](../README.md) · [↑ Camada 02](../../README.md)
