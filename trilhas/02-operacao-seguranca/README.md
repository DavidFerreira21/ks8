# 🛡️ Camada 02 · Operação, governança e segurança

[⌂ Início](../../README.md) · [🗺️ Roadmap](../../docs/roadmap.md) · [🧪 Labs](../../docs/labs.md)

> **Objetivo da camada**  
> Executar workloads com controles de acesso, limites de consumo, agendamento previsível e disponibilidade.

**14 aulas no catálogo · 9 guias teóricos · infográficos publicados progressivamente** · **2 labs com manifests** · **exercícios adicionais planejados**

---

## 🧭 Por onde começar?

| **01 · Identidade e permissões** | **02 · Governança de recursos** |
| :--- | :--- |
| 🔐 Descubra quem pode ler, criar ou excluir recursos. Aplique menor privilégio com ServiceAccount e RBAC.<br><br>**[Estudar RBAC →](rbac-serviceaccount/README.md)** | 📏 Observe defaults de recursos e limites por namespace.<br><br>**[Estudar ResourceQuota →](resourcequota-limitrange/README.md)** |
| **03 · Agendamento e resiliência** | **04 · Tráfego e execução** |
| 🧩 Investigue Taints, Affinity, PDB e prioridades.<br><br>**[Estudar scheduling →](taints-tolerations-affinity/README.md)** | 🌐 Explore NetworkPolicy, Jobs, CronJobs e padrões de containers.<br><br>**[Estudar NetworkPolicy →](networkpolicy/README.md)** |

## 📚 Catálogo de aulas — ordem oficial

A sequência abaixo acompanha o [catálogo curricular de 52 aulas](../../docs/catalogo.md). Guias e laboratórios são publicados progressivamente, sem remover o material complementar existente.

| Aula | Conceito | Aula teórica | Material de apoio |
| --- | --- | --- | --- |
| 02.01 | **Labels, Selectors e Annotations** | [📖 Estudar](labels-selectors-annotations/README.md) | — |
| 02.02 | **RBAC e ServiceAccount** | [📖 Estudar](rbac-serviceaccount/README.md) | — · [🧪 Lab](labs/rbac-minimo/README.md) |
| 02.03 | **SecurityContext e Pod Security Admission** | [🎨 Infográfico · teoria em preparação](securitycontext-pod-security/README.md) | — |
| 02.04 | **ResourceQuota e LimitRange** | [📖 Estudar](resourcequota-limitrange/README.md) | — · [🧪 Lab](labs/quota-namespace/README.md) |
| 02.05 | **Init Containers e Sidecars** | [📖 Estudar](init-sidecars/README.md) | — |
| 02.06 | **Jobs e CronJobs** | [📖 Estudar](jobs-cronjobs/README.md) | — |
| 02.07 | **Taints, Tolerations e Node Affinity** | [📖 Estudar](taints-tolerations-affinity/README.md) | — |
| 02.08 | **Topology Spread Constraints** | [🎨 Infográfico · teoria em preparação](topology-spread/README.md) | — |
| 02.09 | **PriorityClass e Preemption** | [📖 Estudar](priorityclass-preemption/README.md) | — |
| 02.10 | **QoS Classes e Eviction** | [🎨 Infográfico · teoria em preparação](qos-eviction/README.md) | — |
| 02.11 | **PodDisruptionBudget (PDB)** | [📖 Estudar](pdb/README.md) | — |
| 02.12 | **Node Maintenance — Cordon, Drain e Uncordon** | [🎨 Infográfico · teoria em preparação](node-maintenance/README.md) | — |
| 02.13 | **NetworkPolicy** | [📖 Estudar](networkpolicy/README.md) | — |
| 02.14 | **Kubernetes Troubleshooting** | [🎨 Infográfico · teoria em preparação](troubleshooting/README.md) | — |

## 🧪 Labs disponíveis agora

| **🔐 RBAC · Menor privilégio** | **📏 ResourceQuota · Controle por namespace** |
| :--- | :--- |
| Crie ServiceAccount, Role e RoleBinding. Compare permissões concedidas e negadas com `kubectl auth can-i`.<br><br>**[Executar lab RBAC →](labs/rbac-minimo/README.md)** | Configure LimitRange e ResourceQuota, admita um Pod e observe a rejeição intencional de um segundo.<br><br>**[Executar lab de Quotas →](labs/quota-namespace/README.md)** |

> **Ambiente de teste:** Kind local. Os manifests foram adicionados à trilha, mas **os exercícios ainda precisam de validação real no cluster**. O CI faz verificações estáticas; não executa esses labs.

## 🔎 Experimentos para a próxima evolução

| Domínio | Experimento proposto | Pré-requisito |
| --- | --- | --- |
| **NetworkPolicy** | Comparar comunicação permitida e bloqueada | Plugin CNI com suporte a policies |
| **Resiliência** | Observar `disruptionsAllowed` em um PDB | Ambiente de testes para evictions |
| **Scheduling** | Comparar Pod com e sem affinity/tolerations | Workers com labels e taints controlados |
| **Prioridades** | Investigar Pods Pending sob pressão de recursos | Cluster descartável |

## 🎯 Checklist de aprendizado

- [ ] Explicar a diferença entre ServiceAccount, Role e RoleBinding.
- [ ] Interpretar uma criação negada pela ResourceQuota.
- [ ] Distinguir permissão de agendamento de preferência de nó.
- [ ] Explicar quando PDB restringe interrupções voluntárias.
- [ ] Identificar a dependência do CNI para aplicar NetworkPolicy.

## 🎨 Coleção visual e fontes

**Os 14 infográficos da camada estão publicados e vinculados às aulas.** A revisão técnica das imagens e a evolução dos labs continuam em andamento. Consulte a [convenção visual](../../docs/infograficos.md).

[RBAC oficial](https://kubernetes.io/docs/reference/access-authn-authz/rbac/) · [Scheduling](https://kubernetes.io/docs/concepts/scheduling-eviction/) · [NetworkPolicy](https://kubernetes.io/docs/concepts/services-networking/network-policies/) · [ResourceQuota](https://kubernetes.io/docs/concepts/policy/resource-quotas/) · [Pod Disruptions](https://kubernetes.io/docs/concepts/workloads/pods/disruptions/)

---

[**← 01 · Fundamentos**](../01-fundamentos/README.md) · [↑ Roadmap](../../docs/roadmap.md) · **[03 · Arquitetura →](../03-arquitetura/README.md)**
