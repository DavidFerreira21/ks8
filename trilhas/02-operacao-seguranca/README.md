# Camada 02 — Operação, governança e segurança

[← Roadmap](../../docs/roadmap.md) · [Início](../../README.md)

**Objetivo:** operar workloads de maneira previsível, aplicar controles de acesso, limitar consumo e proteger comunicação e disponibilidade.

## Roteiro de estudo

| Tópico | Pergunta central | Situação |
| --- | --- | --- |
| RBAC e ServiceAccount | Quem pode executar quais ações? | Aula/lab a estruturar |
| Jobs e CronJobs | Como executar tarefas pontuais e periódicas? | Aula/lab a estruturar |
| NetworkPolicy | Quais fluxos entre Pods são permitidos? | Aula/lab a estruturar |
| Labels, Selectors e Annotations | Como identificar, filtrar e descrever recursos? | Exemplos espalhados pelas aulas existentes |
| Taints, Tolerations e Node Affinity | Onde um Pod pode ser agendado? | Aula/lab a estruturar |
| ResourceQuota e LimitRange | Como controlar consumo por namespace? | Aula/lab a estruturar |
| PodDisruptionBudget | Como limitar interrupções voluntárias? | Aula/lab a estruturar |
| PriorityClass e Preemption | Como priorizar workloads quando faltam recursos? | Aula/lab a estruturar |
| Init Containers e Sidecars | Como preparar e complementar containers? | [Base no módulo Pods](../../2-pod/README.md) |

## Labs integrados sugeridos (ainda não implementados)

- **Segurança:** ServiceAccount + Role + RoleBinding, incluindo teste de acesso negado.
- **Rede:** NetworkPolicy com um fluxo permitido e outro bloqueado. Requer CNI com suporte a NetworkPolicy.
- **Governança:** namespace com ResourceQuota e LimitRange, inspecionando uma criação rejeitada.
- **Resiliência:** Deployment com PDB e interrupção voluntária controlada.

## Referências oficiais

- [RBAC](https://kubernetes.io/docs/reference/access-authn-authz/rbac/)
- [Network Policies](https://kubernetes.io/docs/concepts/services-networking/network-policies/)
- [Assigning Pods to Nodes](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/)
- [Resource Quotas](https://kubernetes.io/docs/concepts/policy/resource-quotas/)
- [Pod Disruptions](https://kubernetes.io/docs/concepts/workloads/pods/disruptions/)

**Próxima camada:** [Arquitetura e infraestrutura](../03-arquitetura/README.md).
