# 🛡️ Camada 02 · Operação, governança e segurança

[⌂ Início](../../README.md) · [🗺️ Roadmap](../../docs/roadmap.md) · [🧪 Labs](../../docs/labs.md)

> **Objetivo da camada:** operar workloads com controle de acesso, políticas de segurança, governança de recursos, scheduling, resiliência e diagnóstico orientado por evidências.

**14 aulas com teoria e infográfico** · **14 labs com desafios YAML e soluções separadas** · **6 complementares opcionais**

O [padrão editorial](../../docs/padrao-editorial.md) é o mesmo da Camada 01. Os labs possuem contratos e validação estática; **não confunda publicação com homologação funcional integral**. A CI Kind atual só executa os labs 02.02 e 02.04; os demais aguardam execução específica e evidências.

## 🚀 Percurso recomendado

| 01 · Identidade e segurança | 02 · Execução e governança |
| :--- | :--- |
| Labels → RBAC → SecurityContext/PSA → Quotas. Pratique escopo, admissão e permissões. | Init/sidecars → Jobs/CronJobs. Observe ciclo de vida e terminação. |
| 03 · Scheduling e disponibilidade | 04 · Tráfego e diagnóstico |
| Taints/Affinity → Spread → Priority → QoS → PDB → Manutenção. | NetworkPolicy → Troubleshooting. Separe APIs declarativas de efeitos reais no cluster. |

## 📚 Catálogo — ordem oficial

| Aula | Conceito | Aula | Lab | Complementares |
| --- | --- | --- | --- | --- |
| 02.01 | **Labels, Selectors e Annotations** | [📖 Estudar](labels-selectors-annotations/README.md) | [🧪 Lab 02.01](labs/labels-selectors-basico/README.md) | — |
| 02.02 | **RBAC e ServiceAccount** | [📖 Estudar](rbac-serviceaccount/README.md) | [🧪 Lab 02.02](labs/rbac-minimo/README.md) | [Consultar](rbac-serviceaccount/complementares/README.md) |
| 02.03 | **SecurityContext e Pod Security Admission** | [📖 Estudar](securitycontext-pod-security/README.md) | [🧪 Lab 02.03](labs/securitycontext-psa-basico/README.md) | [Consultar](securitycontext-pod-security/complementares/README.md) |
| 02.04 | **ResourceQuota e LimitRange** | [📖 Estudar](resourcequota-limitrange/README.md) | [🧪 Lab 02.04](labs/quota-namespace/README.md) | — |
| 02.05 | **Init Containers e Sidecars** | [📖 Estudar](init-sidecars/README.md) | [🧪 Lab 02.05](labs/init-sidecars-basico/README.md) | — |
| 02.06 | **Jobs e CronJobs** | [📖 Estudar](jobs-cronjobs/README.md) | [🧪 Lab 02.06](labs/jobs-cronjobs-basico/README.md) | — |
| 02.07 | **Taints, Tolerations e Node Affinity** | [📖 Estudar](taints-tolerations-affinity/README.md) | [🧪 Lab 02.07](labs/scheduling-basico/README.md) | [Consultar](taints-tolerations-affinity/complementares/README.md) |
| 02.08 | **Topology Spread Constraints** | [📖 Estudar](topology-spread/README.md) | [🧪 Lab 02.08](labs/topology-spread-basico/README.md) | — |
| 02.09 | **PriorityClass e Preemption** | [📖 Estudar](priorityclass-preemption/README.md) | [🧪 Lab 02.09](labs/priorityclass-basico/README.md) | — |
| 02.10 | **QoS Classes e Eviction** | [📖 Estudar](qos-eviction/README.md) | [🧪 Lab 02.10](labs/qos-eviction-basico/README.md) | [Consultar](qos-eviction/complementares/README.md) |
| 02.11 | **PodDisruptionBudget (PDB)** | [📖 Estudar](pdb/README.md) | [🧪 Lab 02.11](labs/pdb-basico/README.md) | — |
| 02.12 | **Node Maintenance — Cordon, Drain e Uncordon** | [📖 Estudar](node-maintenance/README.md) | [🧪 Lab 02.12](labs/node-maintenance-basico/README.md) | — |
| 02.13 | **NetworkPolicy** | [📖 Estudar](networkpolicy/README.md) | [🧪 Lab 02.13](labs/networkpolicy-basico/README.md) | [Consultar](networkpolicy/complementares/README.md) |
| 02.14 | **Kubernetes Troubleshooting** | [📖 Estudar](troubleshooting/README.md) | [🧪 Lab 02.14](labs/troubleshooting-basico/README.md) | [Consultar](troubleshooting/complementares/README.md) |

## 📚 Como usar os complementares

A **aula** ensina o conceito e suas decisões; o **lab** orienta a prática e a coleta de evidências; o **complementar** é consulta opcional para comparação, comandos e troubleshooting. Não há complementar artificial para preencher a tabela.

## 🧪 Contrato dos laboratórios

Em cada lab, execute `make lab-prepare LAB=02.XX`, complete o YAML em `.labs/02.XX/`, aplique usando `kubectl apply`, observe com `make lab-observe` e valide com `make lab-test`. O comando `make lab-up` **aplica a solução e pertence à CI**, nunca ao fluxo inicial do aluno. Use `make lab-down` para limpar recursos declarados; não execute `make down`.

**Limitações e segurança:**

- **02.03:** PSA deve ser testado em namespace exclusivo e preferencialmente no modo `warn`.
- **02.07–02.08:** dependem dos dois workers do Kind e das respectivas labels.
- **02.09:** cria PriorityClass com escopo do cluster; limpe-a após usar.
- **02.11–02.12:** PDB e manutenção devem ser observados no Kind, sem drenagem de nós compartilhados.
- **02.13:** NetworkPolicy aceita pela API não demonstra bloqueio sem CNI com enforcement.
- **02.14:** erro de imagem é intencional para estudo de diagnóstico.

## 🎯 Checklist de conclusão

- [ ] Expliquei e demonstrei menor privilégio RBAC e diferenças entre contexto de segurança e PSA.
- [ ] Observei admissão por quota, init containers, Jobs/CronJobs e decisões de agendamento.
- [ ] Interpretei QoS, PDB, prioridade e estado de manutenção dos nós.
- [ ] Diferenciei NetworkPolicy declarativa de enforcement funcional.
- [ ] Registrei sintomas, eventos, hipótese, causa e reversão nos laboratórios.
- [ ] Limpei recursos e desfiz operações manuais de cada exercício.

## 🔗 Documentação oficial

[Autorização](https://kubernetes.io/docs/reference/access-authn-authz/rbac/) · [Segurança](https://kubernetes.io/docs/concepts/security/) · [Scheduling](https://kubernetes.io/docs/concepts/scheduling-eviction/) · [NetworkPolicy](https://kubernetes.io/docs/concepts/services-networking/network-policies/)

---

[← Camada 01](../01-fundamentos/README.md) · [↑ Roadmap](../../docs/roadmap.md) · [Próxima: 03 · Arquitetura →](../03-arquitetura/README.md)
