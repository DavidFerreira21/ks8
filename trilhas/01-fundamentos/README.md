# 📦 Camada 01 · Fundamentos e recursos essenciais

[⌂ Início](../../README.md) · [🗺️ Roadmap](../../docs/roadmap.md) · [🧪 Labs](../../docs/labs.md)

> **Objetivo da camada**  
> Entender os objetos essenciais do Kubernetes, publicar uma aplicação e observar como o cluster mantém o estado desejado.

**14 aulas com teoria e infográfico publicados** · **2 labs com manifests**

---

## 🚀 Seu primeiro percurso

| **01 · Preparar o ambiente** | **02 · Entender o workload** |
| :--- | :--- |
| ⚙️ Instale o Kind, verifique o contexto e conheça os nós do cluster.<br><br>**[Preparar Kind →](../../install-kind.md)** | 📖 Comece pelos fundamentos e pelos Pods. Entenda o que Kubernetes executa e supervisiona.<br><br>**[Fundamentos →](fundamentos/README.md)** · [Pods](pods/README.md) |
| **03 · Controlar e expor** | **04 · Observar e experimentar** |
| 🔁 Aprenda Deployments, ReplicaSets e Services: como atualizar e acessar aplicações.<br><br>**[Deployments →](deployments/README.md)** | 🧪 Execute o lab integrado e investigue réplicas, Service e eventos.<br><br>**[Primeira aplicação →](labs/primeira-aplicacao/README.md)** |

## 📚 Catálogo de aulas — ordem oficial

A sequência abaixo acompanha o [catálogo curricular de 52 aulas](../../docs/catalogo.md). As **14 aulas já possuem explicação teórica e infográfico**. Laboratórios executáveis continuam em evolução, sem remover o material complementar existente.

| Aula | Conceito | Aula teórica | Material de apoio |
| --- | --- | --- | --- |
| 01.01 | **Fundamentos Kubernetes** | [📖 Estudar](fundamentos/README.md) | [🧪 Lab 01.01](labs/fundamentos-cluster/README.md) · [Anotações e exemplos](../../1-fundamentos/README.md) |
| 01.02 | **Namespaces** | [📖 Estudar](namespaces/README.md) | — |
| 01.03 | **Pods** | [📖 Estudar](pods/README.md) | [Anotações e exemplos](../../2-pod/README.md) |
| 01.04 | **Requests e Limits** | [📖 Estudar](requests-limits/README.md) | [Anotações e exemplos](../../2-pod/README.md) |
| 01.05 | **Probes — Liveness, Readiness e Startup** | [📖 Estudar](probes/README.md) | [Anotações e exemplos](../../5-probes/README.md) |
| 01.06 | **Deployments** | [📖 Estudar](deployments/README.md) | [Anotações e exemplos](../../3-deployment/README.md) · [🧪 Lab](labs/primeira-aplicacao/README.md) |
| 01.07 | **ReplicaSet, DaemonSet e StatefulSet** | [📖 Estudar](controladores/README.md) | [Anotações e exemplos](../../4-replicaSet-daemonSet-statefulSet/README.md) |
| 01.08 | **Estratégias avançadas de Deployment** | [📖 Estudar](estrategias-deployment/README.md) | — |
| 01.09 | **Services** | [📖 Estudar](services/README.md) | [Anotações e exemplos](../../7-services/README.md) · [🧪 Lab](labs/primeira-aplicacao/README.md) |
| 01.10 | **ConfigMaps** | [📖 Estudar](configmaps/README.md) | — |
| 01.11 | **Secrets** | [📖 Estudar](secrets/README.md) | — |
| 01.12 | **Volumes** | [📖 Estudar](volumes/README.md) | — |
| 01.13 | **Ingress** | [📖 Estudar](ingress/README.md) | — |
| 01.14 | **Horizontal Pod Autoscaler (HPA)** | [📖 Estudar](hpa/README.md) | — |

## 🧪 Laboratórios

Comece pelo [**Lab 01.01 — Explorar o cluster e a API**](labs/fundamentos-cluster/README.md), que ensina a observar o Control Plane e os Workers e a aplicar um objeto declarativo.

### Aplicação integrada

| **Primeira aplicação · Pod → Deployment → Service** | |
| :--- | :--- |
| **O que você pratica** | Criar um Pod, gerenciar três réplicas com Deployment, disponibilizar um Service e inspecionar a reconciliação. |
| **O que observar** | Pods recriados, ReplicaSet, EndpointSlices, rollout e eventos. |
| **Ambiente** | Kind local, namespace de laboratório isolado. |
| **Começar** | **[Abrir laboratório →](labs/primeira-aplicacao/README.md)** |

> **Importante:** os manifests do lab integrado estão disponíveis, mas a execução ponta a ponta no Kind ainda precisa de validação. A teoria de Volumes está na aula 01.12; não existe um laboratório específico validado para o tema.

## 🎯 Checklist de aprendizado

- [ ] Diferenciar Pod, Deployment, ReplicaSet e Service.
- [ ] Explicar por que um Pod controlado é recriado após exclusão.
- [ ] Consultar logs, eventos e status de readiness.
- [ ] Executar o lab integrado e limpar somente os recursos criados.

## 🔗 Continue aprendendo

[Documentação Kubernetes Basics](https://kubernetes.io/docs/tutorials/kubernetes-basics/) · [Guia de labs](../../docs/labs.md) · [Resumo histórico](../../resume.md)

---

[⌂ Início](../../README.md) · [↑ Roadmap](../../docs/roadmap.md) · **[Próxima: 02 · Operação e Segurança →](../02-operacao-seguranca/README.md)**
