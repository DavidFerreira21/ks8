# 📦 Camada 01 · Fundamentos e recursos essenciais

[⌂ Início](../../README.md) · [🗺️ Roadmap](../../docs/roadmap.md) · [🧪 Labs](../../docs/labs.md)

> **Objetivo da camada**  
> Entender os objetos essenciais do Kubernetes, publicar uma aplicação e observar como o cluster mantém o estado desejado.

**13 temas planejados** · **6 guias de entrada disponíveis** · **1 lab integrado com manifests**

---

## 🚀 Seu primeiro percurso

| **01 · Preparar o ambiente** | **02 · Entender o workload** |
| :--- | :--- |
| ⚙️ Instale o Kind, verifique o contexto e conheça os nós do cluster.<br><br>**[Preparar Kind →](../../install-kind.md)** | 📖 Comece pelos fundamentos e pelos Pods. Entenda o que Kubernetes executa e supervisiona.<br><br>**[Fundamentos →](fundamentos/README.md)** · [Pods](pods/README.md) |
| **03 · Controlar e expor** | **04 · Observar e experimentar** |
| 🔁 Aprenda Deployments, ReplicaSets e Services: como atualizar e acessar aplicações.<br><br>**[Deployments →](deployments/README.md)** | 🧪 Execute o lab integrado e investigue réplicas, Service e eventos.<br><br>**[Primeira aplicação →](labs/primeira-aplicacao/README.md)** |

## 📚 Catálogo de conceitos

Os links **Estudar** abrem as páginas novas; **Aula original** mantém acesso aos exemplos já produzidos. Temas sem página própria ficam identificados como planejados, sem sugerir que um lab exista.

### Workloads · como executar aplicações

| Conceito | Guia | Experiência prática |
| --- | --- | --- |
| **01. Fundamentos** | [📖 Estudar](fundamentos/README.md) | [Aula original](../../1-fundamentos/README.md) |
| **02. Pods** | [📖 Estudar](pods/README.md) | [Aula original](../../2-pod/README.md) |
| **03. Deployments** | [📖 Estudar](deployments/README.md) | [Aula original](../../3-deployment/README.md) · [🧪 Lab](labs/primeira-aplicacao/README.md) |
| **04. Services** | [📖 Estudar](services/README.md) | [Aula original](../../7-services/README.md) · [🧪 Lab](labs/primeira-aplicacao/README.md) |
| **05. ReplicaSet, DaemonSet e StatefulSet** | [📖 Estudar](controladores/README.md) | [Aula original](../../4-replicaSet-daemonSet-statefulSet/README.md) |
| **06. Probes** | [📖 Estudar](probes/README.md) | [Aula original](../../5-probes/README.md) |

### Configuração, recursos e acesso · aprofundamento

| Conceito | Status do material | Ponto de partida |
| --- | --- | --- |
| **07. Volumes** | 🚧 Página de aula pendente | [Armazenamento no resumo](../../resume.md) · [Documentação oficial](https://kubernetes.io/docs/concepts/storage/volumes/) |
| **08. Namespace** | 🚧 Guia a estruturar | [🧪 Namespace no lab integrado](labs/primeira-aplicacao/README.md) |
| **09. Ingress** | 🚧 Guia a estruturar | [Documentação oficial](https://kubernetes.io/docs/concepts/services-networking/ingress/) |
| **10. ConfigMap** | 🚧 Guia a estruturar | [Documentação oficial](https://kubernetes.io/docs/concepts/configuration/configmap/) |
| **11. Secret** | 🚧 Guia a estruturar | [Documentação oficial](https://kubernetes.io/docs/concepts/configuration/secret/) |
| **12. HPA** | 🚧 Guia a estruturar | [Documentação oficial](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/) |
| **13. Requests e Limits** | 📖 Exemplos existentes | [Aula de Pods](../../2-pod/README.md) · [Documentação oficial](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/) |

## 🧪 Laboratório em destaque

| **Primeira aplicação · Pod → Deployment → Service** | |
| :--- | :--- |
| **O que você pratica** | Criar um Pod, gerenciar três réplicas com Deployment, disponibilizar um Service e inspecionar a reconciliação. |
| **O que observar** | Pods recriados, ReplicaSet, EndpointSlices, rollout e eventos. |
| **Ambiente** | Kind local, namespace de laboratório isolado. |
| **Começar** | **[Abrir laboratório →](labs/primeira-aplicacao/README.md)** |

> **Importante:** manifests e roteiro estão disponíveis, mas a execução ponta a ponta no Kind ainda precisa de validação. O material de Volumes citado em índices históricos continua sem um README original localizado; não foi recriado neste ajuste visual.

## 🎯 Checklist de aprendizado

- [ ] Diferenciar Pod, Deployment, ReplicaSet e Service.
- [ ] Explicar por que um Pod controlado é recriado após exclusão.
- [ ] Consultar logs, eventos e status de readiness.
- [ ] Executar o lab integrado e limpar somente os recursos criados.

## 🔗 Continue aprendendo

[Documentação Kubernetes Basics](https://kubernetes.io/docs/tutorials/kubernetes-basics/) · [Guia de labs](../../docs/labs.md) · [Resumo histórico](../../resume.md)

---

[⌂ Início](../../README.md) · [↑ Roadmap](../../docs/roadmap.md) · **[Próxima: 02 · Operação e Segurança →](../02-operacao-seguranca/README.md)**
