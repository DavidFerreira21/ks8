# Complementar 03.06 — Design de CRDs e contratos de API

[← Aula 03.06](../README.md) · [🧪 Lab 03.06](../../labs/crds-custom-resources-basico/README.md) · [↑ Camada 03](../../README.md)

> **Leitura opcional:** referência de arquitetura, comparação e diagnóstico; não substitui o percurso prático da aula e do lab.

## Quando consultar

Ao criar APIs internas, versionar contratos ou decidir quais responsabilidades pertencem ao controller.

| Elemento | Propósito | Exemplo |
| --- | --- | --- |
| CRD | Registra tipo, escopo e schema | `AppEnvironment` |
| CR | Declara uma instância | `metadata.name=demonstra` |
| OpenAPI schema | Valida campos, tipos e defaults | `spec.tier` enum |
| Reconciler | Produz mudanças observadas e status | Um controller próprio, fora deste lab |

## Evolução de API

Não modifique uma versão servida sem planejar compatibilidade. Evite alterar um campo de string para objeto no mesmo contrato sem migração; mantenha versões e conversões adequadas. Finalizers e status podem demandar RBAC separado para o controller.

```bash
kubectl get crd appenvironments.learning.example
kubectl api-resources --api-group=learning.example
kubectl explain appenvironment.spec
```

**Segurança:** apagar uma CRD remove os recursos do tipo; instale apenas no Kind isolado.

## Referências oficiais

[CustomResourceDefinitions](https://kubernetes.io/docs/tasks/extend-kubernetes/custom-resources/custom-resource-definitions/)

---

[↑ Aula 03.06](../README.md) · [↑ Camada 03](../../README.md)
