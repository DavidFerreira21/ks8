# Camada 02 — Operação, governança e segurança

[← Roadmap](../../docs/roadmap.md) · [Início](../../README.md)

**Objetivo:** executar aplicações com controles claros de acesso, consumo, agendamento, conectividade e disponibilidade. Recomendação: terminar o [lab de primeira aplicação](../01-fundamentos/labs/primeira-aplicacao/README.md) antes de avançar.

## Conteúdos

| Tópico | Guia | Prática |
| --- | --- | --- |
| RBAC e ServiceAccount | [Estudar](rbac-serviceaccount/README.md) | [Lab mínimo](labs/rbac-minimo/README.md) |
| Jobs e CronJobs | [Estudar](jobs-cronjobs/README.md) | Roteiro de laboratório futuro |
| NetworkPolicy | [Estudar](networkpolicy/README.md) | Requer CNI com enforcement |
| Labels, Selectors e Annotations | [Estudar](labels-selectors-annotations/README.md) | Exemplos de seleção |
| Taints, Tolerations e Node Affinity | [Estudar](taints-tolerations-affinity/README.md) | Roteiro de scheduling |
| ResourceQuota e LimitRange | [Estudar](resourcequota-limitrange/README.md) | [Lab de quota](labs/quota-namespace/README.md) |
| PodDisruptionBudget (PDB) | [Estudar](pdb/README.md) | Roteiro de resiliência |
| PriorityClass e Preemption | [Estudar](priorityclass-preemption/README.md) | Roteiro de prioridades |
| Init Containers e Sidecars | [Estudar](init-sidecars/README.md) | Roteiro de ciclo de vida |

Os nove guias seguem o formato **conceito → funcionamento → experimento → observação → documentação oficial**.

## Laboratórios disponíveis

### 1. RBAC e ServiceAccount

[Executar laboratório de menor privilégio](labs/rbac-minimo/README.md): cria ServiceAccount, Role e RoleBinding em namespace isolado; usa `kubectl auth can-i --as=...` para demonstrar permissão concedida e negada.

### 2. ResourceQuota e LimitRange

[Executar laboratório de quota por namespace](labs/quota-namespace/README.md): configura defaults para containers, admite o primeiro Pod e demonstra rejeição intencional do segundo por exceder a quota.

> **Ambiente:** os labs foram preparados para Kind local. Os comandos precisam ser executados e validados no cluster; os testes no GitHub Actions checam apenas aspectos estáticos dos YAMLs.

## Próximos exercícios sugeridos

- **Rede:** NetworkPolicy com tráfego permitido/bloqueado, após configurar CNI que implemente enforcement. O Kind padrão não atende automaticamente a esse requisito.
- **Resiliência:** Deployment com PDB e teste de Eviction API durante manutenção.
- **Scheduling:** Node Affinity e Taints/Tolerations em Workers rotulados.
- **Prioridades:** PriorityClass e análise de comportamento sob falta de recursos.

## Infográficos

A coleção visual tem imagens para os nove tópicos desta camada. **Os PNGs ainda não estão no repositório.** Consulte a [convenção para integração de imagens](../../docs/infograficos.md).

## Referências oficiais

- [RBAC](https://kubernetes.io/docs/reference/access-authn-authz/rbac/)
- [NetworkPolicy](https://kubernetes.io/docs/concepts/services-networking/network-policies/)
- [ResourceQuota](https://kubernetes.io/docs/concepts/policy/resource-quotas/)
- [Scheduling](https://kubernetes.io/docs/concepts/scheduling-eviction/)
- [Pod Disruptions](https://kubernetes.io/docs/concepts/workloads/pods/disruptions/)

**Próxima camada:** [Arquitetura e infraestrutura](../03-arquitetura/README.md).
