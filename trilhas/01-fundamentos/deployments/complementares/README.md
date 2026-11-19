# Complementar 01.03 — Rollout e sinais de convergência

[← Aula 01.03](../README.md) · [🧪 Lab 01.03](../../labs/deployments-basico/README.md) · [↑ Camada 01](../../README.md)

> **Leitura opcional:** Use para decidir quando um Deployment convergiu e como diagnosticar rollout parado. Não substitui a aula nem o desafio do laboratório.

## Decisões e sintomas

| Situação | Leitura técnica |
| --- | --- |
| **generation > observedGeneration** | Controlador ainda não observou a última especificação. |
| **updatedReplicas abaixo do desejado** | Novos Pods ainda não foram criados/agendados. |
| **readyReplicas abaixo do desejado** | Investigue probes, imagem, recursos e eventos. |
| **ProgressDeadlineExceeded** | Rollout não fez progresso no prazo configurado; não implica rollback automático. |

## Como interpretar as evidências

`kubectl rollout status` é apenas a evidência de estado da implantação; capture condições e ReplicaSets antes de alterar a estratégia.

## Referência histórica preservada

O [material complementar original](../../../../3-deployment/README.md) permanece acessível, com exemplos e comandos adicionais. Esta página reúne a comparação rápida no padrão editorial das demais camadas, sem duplicar todo o material antigo.

## Referências oficiais

[Documentação Kubernetes — Conceitos](https://kubernetes.io/docs/concepts/) · [Debugging](https://kubernetes.io/docs/tasks/debug/)

---

[↑ Aula 01.03](../README.md) · [↑ Camada 01](../../README.md)
