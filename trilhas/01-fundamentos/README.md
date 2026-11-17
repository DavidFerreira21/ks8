# 📦 Camada 01 · Fundamentos e recursos essenciais

[⌂ Início](../../README.md) · [🗺️ Roadmap](../../docs/roadmap.md) · [🧪 Labs](../../docs/labs.md)

> **Objetivo da camada**  
> Entender os objetos essenciais do Kubernetes, publicar uma aplicação e observar como o cluster mantém o estado desejado.

**14 aulas no catálogo · infográficos publicados progressivamente** · **6 guias de entrada disponíveis** · **1 lab integrado com manifests**

---

## 🚀 Seu primeiro percurso

| **01 · Preparar o ambiente** | **02 · Entender o workload** |
| :--- | :--- |
| ⚙️ Instale o Kind, verifique o contexto e conheça os nós do cluster.<br><br>**[Preparar Kind →](../../install-kind.md)** | 📖 Comece pelos fundamentos e pelos Pods. Entenda o que Kubernetes executa e supervisiona.<br><br>**[Fundamentos →](fundamentos/README.md)** · [Pods](pods/README.md) |
| **03 · Controlar e expor** | **04 · Observar e experimentar** |
| 🔁 Aprenda Deployments, ReplicaSets e Services: como atualizar e acessar aplicações.<br><br>**[Deployments →](deployments/README.md)** | 🧪 Execute o lab integrado e investigue réplicas, Service e eventos.<br><br>**[Primeira aplicação →](labs/primeira-aplicacao/README.md)** |

## 📚 Catálogo de aulas — ordem oficial

A sequência abaixo acompanha o [catálogo curricular de 52 aulas](../../docs/catalogo.md). Guias e laboratórios são publicados progressivamente, sem remover o material complementar existente.

| Aula | Conceito | Aula teórica | Material de apoio |
| --- | --- | --- | --- |
| 01.01 | **Fundamentos Kubernetes** | [📖 Estudar](fundamentos/README.md) | [Anotações e exemplos](../../1-fundamentos/README.md) |
| 01.02 | **Namespaces** | [🎨 Infográfico · teoria em preparação](namespaces/README.md) | — |
| 01.03 | **Pods** | [📖 Estudar](pods/README.md) | [Anotações e exemplos](../../2-pod/README.md) |
| 01.04 | **Requests e Limits** | [🎨 Infográfico · teoria em preparação](requests-limits/README.md) | [Anotações e exemplos](../../2-pod/README.md) |
| 01.05 | **Probes — Liveness, Readiness e Startup** | [📖 Estudar](probes/README.md) | [Anotações e exemplos](../../5-probes/README.md) |
| 01.06 | **Deployments** | [📖 Estudar](deployments/README.md) | [Anotações e exemplos](../../3-deployment/README.md) · [🧪 Lab](labs/primeira-aplicacao/README.md) |
| 01.07 | **ReplicaSet, DaemonSet e StatefulSet** | [📖 Estudar](controladores/README.md) | [Anotações e exemplos](../../4-replicaSet-daemonSet-statefulSet/README.md) |
| 01.08 | **Estratégias avançadas de Deployment** | [🎨 Infográfico · teoria em preparação](estrategias-deployment/README.md) | — |
| 01.09 | **Services** | [📖 Estudar](services/README.md) | [Anotações e exemplos](../../7-services/README.md) · [🧪 Lab](labs/primeira-aplicacao/README.md) |
| 01.10 | **ConfigMaps** | [🎨 Infográfico · teoria em preparação](configmaps/README.md) | — |
| 01.11 | **Secrets** | [🎨 Infográfico · teoria em preparação](secrets/README.md) | — |
| 01.12 | **Volumes** | [🎨 Infográfico · teoria em preparação](volumes/README.md) | — |
| 01.13 | **Ingress** | [🎨 Infográfico · teoria em preparação](ingress/README.md) | — |
| 01.14 | **Horizontal Pod Autoscaler (HPA)** | [🎨 Infográfico · teoria em preparação](hpa/README.md) | — |

## 🧪 Laboratório em destaque

| **Primeira aplicação · Pod → Deployment → Service** | |
| :--- | :--- |
| **O que você pratica** | Criar um Pod, gerenciar três réplicas com Deployment, disponibilizar um Service e inspecionar a reconciliação. |
| **O que observar** | Pods recriados, ReplicaSet, EndpointSlices, rollout e eventos. |
| **Ambiente** | Kind local, namespace de laboratório isolado. |
| **Começar** | **[Abrir laboratório →](labs/primeira-aplicacao/README.md)** |

> **Importante:** manifests e roteiro estão disponíveis, mas a execução ponta a ponta no Kind ainda precisa de validação. O conteúdo de Volumes ainda não tem uma página completa identificada no repositório; os conceitos disponíveis continuam acessíveis pelo resumo.

## 🎯 Checklist de aprendizado

- [ ] Diferenciar Pod, Deployment, ReplicaSet e Service.
- [ ] Explicar por que um Pod controlado é recriado após exclusão.
- [ ] Consultar logs, eventos e status de readiness.
- [ ] Executar o lab integrado e limpar somente os recursos criados.

## 🔗 Continue aprendendo

[Documentação Kubernetes Basics](https://kubernetes.io/docs/tutorials/kubernetes-basics/) · [Guia de labs](../../docs/labs.md) · [Resumo histórico](../../resume.md)

---

[⌂ Início](../../README.md) · [↑ Roadmap](../../docs/roadmap.md) · **[Próxima: 02 · Operação e Segurança →](../02-operacao-seguranca/README.md)**
