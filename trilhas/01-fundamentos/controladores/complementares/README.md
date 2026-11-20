# Complementar 01.04 — Quando escolher cada controlador

[← Aula 01.04](../README.md) · [🧪 Lab 01.04](../../labs/controladores-basico/README.md) · [↑ Camada 01](../../README.md)

> **Leitura opcional:** Compare semântica de identidade, agendamento e recuperação antes de selecionar um workload controller. Não substitui a aula nem o desafio do laboratório.

## Decisões e sintomas

| Situação | Leitura técnica |
| --- | --- |
| **Deployment/ReplicaSet** | Réplicas intercambiáveis; rollout e disponibilidade. |
| **DaemonSet** | Uma instância nos nós elegíveis; adequado a agentes por nó. |
| **StatefulSet** | Identidade ordinal estável e associação ordenada a storage/endereços. |
| **Job** | Trabalho finito; não deve ser usado como daemon permanente. |

## Como interpretar as evidências

Se `stateful-demo-0` for recriado, seu nome ordinal permanece, mas o UID muda. Isso não garante dados preservados sem volume estável.

## Referência histórica preservada

O [material complementar original](../../../../4-replicaSet-daemonSet-statefulSet/README.md) permanece acessível, com exemplos e comandos adicionais. Esta página reúne a comparação rápida no padrão editorial das demais camadas, sem duplicar todo o material antigo.

## Referências oficiais

[Documentação Kubernetes — Conceitos](https://kubernetes.io/docs/concepts/) · [Debugging](https://kubernetes.io/docs/tasks/debug/)

---

[↑ Aula 01.04](../README.md) · [↑ Camada 01](../../README.md)
