# Complementar 04.02 — Validação CEL e migração de políticas

[← Aula 04.02](../README.md) · [🧪 Lab 04.02](../../labs/kyverno-basico/README.md) · [↑ Camada 04](../../README.md)

> **Leitura opcional:** matriz de decisão e diagnóstico para consulta. Não é pré-requisito para executar o laboratório.

## Quando consultar

Ao escrever políticas de admissão, migrar ClusterPolicies legadas ou investigar negações inesperadas.

| Recurso | Âmbito | Ação principal |
| --- | --- | --- |
| `NamespacedValidatingPolicy` | Namespace | CEL Deny/Audit conforme config |
| `ValidatingPolicy` | Cluster | Validação ampla |
| Políticas mutating/generating | Conforme tipo | Transformar ou criar recursos |
| PolicyException | Conforme alcance | Exceções controladas |

## Checklist para ativação

1. **Teste sem bloqueio** quando possível; observe efeitos.
2. **Restrinja escopo** inicialmente ao namespace de estudo.
3. **Teste casos positivo e negativo** com `--dry-run=server`.
4. **Documente exceções e rollback.**
5. **Evite políticas cluster-wide** antes de homologação.

Kyverno 1.19 anunciou paridade de APIs CEL e depreciação das políticas legadas. Escolha a API compatível com sua instalação.

## Referências oficiais

[ValidatingPolicy](https://kyverno.io/docs/policy-types/validating-policy/) · [Migração CEL](https://kyverno.io/docs/guides/migration-to-cel/)

---

[↑ Aula 04.02](../README.md) · [↑ Camada 04](../../README.md)
