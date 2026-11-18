# 📦 Camada 01 · Fundamentos e recursos essenciais

[⌂ Início](../../README.md) · [🗺️ Roadmap](../../docs/roadmap.md) · [🧪 Labs](../../docs/labs.md)

> **Objetivo da camada**  
> Entender os objetos essenciais do Kubernetes, publicar uma aplicação e observar como o cluster mantém o estado desejado.

**14 aulas com teoria e infográfico publicados** · **14 labs com manifests**

---

## 🚀 Seu primeiro percurso

| **01 · Preparar o ambiente** | **02 · Entender o workload** |
| :--- | :--- |
| ⚙️ Instale o Kind, verifique o contexto e conheça os nós do cluster.<br><br>**[Preparar Kind →](../../install-kind.md)** | 📖 Comece pelos fundamentos e pelos Pods. Entenda o que Kubernetes executa e supervisiona.<br><br>**[Fundamentos →](fundamentos/README.md)** · [Pods](pods/README.md) |
| **03 · Controlar e expor** | **04 · Observar e experimentar** |
| 🔁 Aprenda Deployments, ReplicaSets e Services: como atualizar e acessar aplicações.<br><br>**[Deployments →](deployments/README.md)** | 🧪 Execute o lab de Services e investigue selectors, EndpointSlices e acesso HTTP.<br><br>**[Services →](labs/services-basico/README.md)** |

[**Consultar tabela de migração dos IDs antigos →**](../../docs/migracao-ids-fundamentos.md)

## 📚 Catálogo de aulas — ordem oficial

A sequência abaixo acompanha o [catálogo curricular de 52 aulas](../../docs/catalogo.md). As **14 aulas já possuem explicação teórica e infográfico**. Laboratórios executáveis continuam em evolução, sem remover o material complementar existente.

| Aula | Conceito | Aula teórica | Material de apoio |
| --- | --- | --- | --- |
| 01.01 | **Fundamentos Kubernetes** | [📖 Estudar](fundamentos/README.md) | [🧪 Lab 01.01](labs/fundamentos-cluster/README.md) · [Anotações](../../1-fundamentos/README.md) |
| 01.02 | **Pods** | [📖 Estudar](pods/README.md) | [🧪 Lab 01.02](labs/pods-basico/README.md) · [Anotações](../../2-pod/README.md) |
| 01.03 | **Deployments** | [📖 Estudar](deployments/README.md) | [🧪 Lab 01.03](labs/deployments-basico/README.md) · [Anotações](../../3-deployment/README.md) |
| 01.04 | **ReplicaSet, DaemonSet e StatefulSet** | [📖 Estudar](controladores/README.md) | [🧪 Lab 01.04](labs/controladores-basico/README.md) · [Anotações](../../4-replicaSet-daemonSet-statefulSet/README.md) |
| 01.05 | **Services** | [📖 Estudar](services/README.md) | [🧪 Lab 01.05 — Services](labs/services-basico/README.md) · [Anotações](../../7-services/README.md) |
| 01.06 | **Namespaces** | [📖 Estudar](namespaces/README.md) | [🧪 Lab 01.06](labs/namespaces-basico/README.md) |
| 01.07 | **ConfigMaps** | [📖 Estudar](configmaps/README.md) | [🧪 Lab 01.07](labs/configmaps-basico/README.md) |
| 01.08 | **Secrets** | [📖 Estudar](secrets/README.md) | [🧪 Lab 01.08](labs/secrets-basico/README.md) |
| 01.09 | **Requests e Limits** | [📖 Estudar](requests-limits/README.md) | [🧪 Lab 01.09](labs/requests-limits-basico/README.md) · [Anotações](../../2-pod/README.md) |
| 01.10 | **Probes — Liveness, Readiness e Startup** | [📖 Estudar](probes/README.md) | [🧪 Lab 01.10](labs/probes-basico/README.md) · [Anotações](../../5-probes/README.md) |
| 01.11 | **Volumes** | [📖 Estudar](volumes/README.md) | [🧪 Lab 01.11](labs/volumes-basico/README.md) |
| 01.12 | **Estratégias avançadas de Deployment** | [📖 Estudar](estrategias-deployment/README.md) | [🧪 Lab 01.12](labs/estrategias-deployment-basico/README.md) |
| 01.13 | **Ingress** | [📖 Estudar](ingress/README.md) | [🧪 Lab 01.13](labs/ingress-basico/README.md) |
| 01.14 | **Horizontal Pod Autoscaler (HPA)** | [📖 Estudar](hpa/README.md) | [🧪 Lab 01.14](labs/hpa-basico/README.md) |

## 🧪 Laboratórios

Cada aula da Camada 01 tem agora um lab próprio. Os labs de 01.13 e 01.14 exigem addons e validação funcional adicionais. Comece pelo [**Lab 01.01 — Explorar o cluster e a API**](labs/fundamentos-cluster/README.md), que ensina a observar o Control Plane e os Workers e a aplicar um objeto declarativo.

### Aplicação integrada

| **Lab 01.05 · Services e descoberta** | |
| :--- | :--- |
| **O que você pratica** | Publicar um Service ClusterIP sobre dois Pods de apoio e testar como o selector controla seus endpoints. |
| **O que observar** | ClusterIP, selector, EndpointSlices, resolução DNS e conectividade. |
| **Ambiente** | Kind local, namespace de laboratório isolado. |
| **Começar** | **[Abrir laboratório →](labs/services-basico/README.md)** |

> **Importante:** os 14 labs da camada possuem contratos executáveis; valide-os em seu Kind. O conteúdo de Volumes está na aula 01.11; o Lab 01.11 está disponível.

## 🎯 Checklist de aprendizado

- [ ] Diferenciar Pod, Deployment, ReplicaSet e Service.
- [ ] Explicar por que um Pod controlado é recriado após exclusão.
- [ ] Consultar logs, eventos e status de readiness.
- [ ] Executar o lab de Services e limpar somente os recursos criados.

## 🔗 Continue aprendendo

[Documentação Kubernetes Basics](https://kubernetes.io/docs/tutorials/kubernetes-basics/) · [Guia de labs](../../docs/labs.md) · [Resumo histórico](../../resume.md)

---

[⌂ Início](../../README.md) · [↑ Roadmap](../../docs/roadmap.md) · **[Próxima: 02 · Operação e Segurança →](../02-operacao-seguranca/README.md)**
