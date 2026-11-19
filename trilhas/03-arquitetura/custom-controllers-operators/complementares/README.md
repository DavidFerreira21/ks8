# Complementar 03.07 — Contrato do reconciler

[← Aula 03.07](../README.md) · [🧪 Lab 03.07](../../labs/custom-controllers-operators-basico/README.md) · [↑ Camada 03](../../README.md)

> **Leitura opcional:** referência de arquitetura, comparação e diagnóstico; não substitui o percurso prático da aula e do lab.

## Quando consultar

Ao desenhar um Operator, instrumentar reconciliação ou avaliar o que significa estado convergido.

| Etapa | Responsabilidade | Possível erro |
| --- | --- | --- |
| Watch/read | Obter Custom Resource e dependências | Cache/stale object |
| Compare | Medir diferença entre `spec` e estado real | Drift não detectado |
| Apply/patch | Reconciliar recursos filhos | Conflitos, permissões |
| Status | Publicar condições observadas | Status antigo ou ambíguo |
| Finalize | Coordenar exclusão e limpeza externa | Recurso órfão |

## Regras operacionais

O reconciler deve ser **idempotente**: eventos repetidos não podem duplicar efeitos. Não use ownerReferences para recursos cross-namespace de forma inválida. `finalizers` não são bloqueio permanente: representam obrigação de limpeza que pode falhar e precisa de observabilidade.

**Atenção:** o lab 03.07 demonstra *reconciliação nativa* de Deployment, não implementa Operator. Para um Operator real, seria preciso criar controller, RBAC, eventos e status.

## Referências oficiais

[Operator pattern](https://kubernetes.io/docs/concepts/extend-kubernetes/operator/)

---

[↑ Aula 03.07](../README.md) · [↑ Camada 03](../../README.md)
