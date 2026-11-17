# 🛡️ Camada 02 · Operação, governança e segurança

[⌂ Início](../../README.md) · [🗺️ Roadmap](../../docs/roadmap.md) · [🧪 Labs](../../docs/labs.md)

> **Objetivo da camada**  
> Executar workloads com controles de acesso, limites de consumo, agendamento previsível e disponibilidade.

**9 temas com guias publicados** · **2 labs com manifests** · **exercícios adicionais planejados**

---

## 🧭 Por onde começar?

| **01 · Identidade e permissões** | **02 · Governança de recursos** |
| :--- | :--- |
| 🔐 Descubra quem pode ler, criar ou excluir recursos. Aplique menor privilégio com ServiceAccount e RBAC.<br><br>**[Estudar RBAC →](rbac-serviceaccount/README.md)** | 📏 Observe defaults de recursos e limites por namespace.<br><br>**[Estudar ResourceQuota →](resourcequota-limitrange/README.md)** |
| **03 · Agendamento e resiliência** | **04 · Tráfego e execução** |
| 🧩 Investigue Taints, Affinity, PDB e prioridades.<br><br>**[Estudar scheduling →](taints-tolerations-affinity/README.md)** | 🌐 Explore NetworkPolicy, Jobs, CronJobs e padrões de containers.<br><br>**[Estudar NetworkPolicy →](networkpolicy/README.md)** |

## 📚 Catálogo de conceitos

### 🔐 Acesso e governança

| Tópico | Para aprender | Prática |
| --- | --- | --- |
| **RBAC e ServiceAccount** | [📖 Guia](rbac-serviceaccount/README.md) | [🧪 Lab de menor privilégio](labs/rbac-minimo/README.md) |
| **ResourceQuota e LimitRange** | [📖 Guia](resourcequota-limitrange/README.md) | [🧪 Lab de quota](labs/quota-namespace/README.md) |
| **Labels, Selectors e Annotations** | [📖 Guia](labels-selectors-annotations/README.md) | Exemplos e comandos de seleção |

### 🧩 Scheduling e disponibilidade

| Tópico | Para aprender | Prática |
| --- | --- | --- |
| **Taints, Tolerations e Node Affinity** | [📖 Guia](taints-tolerations-affinity/README.md) | 🚧 Lab futuro |
| **PodDisruptionBudget (PDB)** | [📖 Guia](pdb/README.md) | 🚧 Lab futuro |
| **PriorityClass e Preemption** | [📖 Guia](priorityclass-preemption/README.md) | 🚧 Lab futuro |

### 🌐 Rede e execução

| Tópico | Para aprender | Prática |
| --- | --- | --- |
| **NetworkPolicy** | [📖 Guia](networkpolicy/README.md) | ⚠️ Lab exige CNI com enforcement |
| **Jobs e CronJobs** | [📖 Guia](jobs-cronjobs/README.md) | 🚧 Lab futuro |
| **Init Containers e Sidecars** | [📖 Guia](init-sidecars/README.md) | 🚧 Lab futuro; [base em Pods](../../2-pod/README.md) |

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

Os infográficos desses nove conceitos **ainda não foram enviados ao GitHub**. Confira a [convenção para integração](../../docs/infograficos.md).

[RBAC oficial](https://kubernetes.io/docs/reference/access-authn-authz/rbac/) · [Scheduling](https://kubernetes.io/docs/concepts/scheduling-eviction/) · [NetworkPolicy](https://kubernetes.io/docs/concepts/services-networking/network-policies/) · [ResourceQuota](https://kubernetes.io/docs/concepts/policy/resource-quotas/) · [Pod Disruptions](https://kubernetes.io/docs/concepts/workloads/pods/disruptions/)

---

[**← 01 · Fundamentos**](../01-fundamentos/README.md) · [↑ Roadmap](../../docs/roadmap.md) · **[03 · Arquitetura →](../03-arquitetura/README.md)**
