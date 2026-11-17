# 🧩 Camada 03 · Arquitetura e infraestrutura

[⌂ Início](../../README.md) · [🗺️ Roadmap](../../docs/roadmap.md) · [⚙️ Kind](../../kind-config.yaml)

> **Objetivo da camada**  
> Investigar como Control Plane, Workers, rede e armazenamento cooperam para transformar objetos declarativos em aplicações executadas.

**17 temas no catálogo (2 guias publicados)** · **visão arquitetural e referências oficiais** · **labs de observação em planejamento**

---

## 🧭 Mapa dos componentes

| **CONTROL PLANE** | **WORKER NODES** |
| :--- | :--- |
| 🎛️ **Decidem, coordenam e reconciliam.**<br>API Server, etcd, Scheduler, Controller Manager, CRDs e reconciliação personalizada.<br><br>[**Conhecer os componentes oficiais →**](https://kubernetes.io/docs/concepts/overview/components/) | ⚙️ **Executam e conectam os Pods.**<br>kubelet, container runtime e mecanismos de rede.<br><br>[**Explorar a arquitetura de nós →**](https://kubernetes.io/docs/concepts/architecture/nodes/) |
| **REDE E DESCOBERTA** | **ARMAZENAMENTO E EXTENSÃO** |
| 🌐 CNI, Service networking, CoreDNS, Gateway API e opções de dataplane.<br><br>[**Entender a rede →**](https://kubernetes.io/docs/concepts/cluster-administration/networking/) | 💾 CSI, provisionamento de volumes, extensibilidade da API, Kustomize e Helm.<br><br>[**Conceitos de storage →**](https://kubernetes.io/docs/concepts/storage/) |

## 📚 Catálogo de arquitetura — ordem de estudo

Os números refletem a sequência didática. **Guias próprios** existem, nesta camada, apenas para 03.06 e 03.07; as demais entradas continuam com referências oficiais e aulas detalhadas planejadas.

| Aula | Conceito | O que aprender | Material |
| --- | --- | --- | --- |
| 03.01 | Arquitetura do Cluster Kubernetes | Control Plane e Workers | [Referência](https://kubernetes.io/docs/concepts/overview/components/) |
| 03.02 | kube-apiserver | API, autenticação e autorização | [Referência](https://kubernetes.io/docs/concepts/overview/components/#kube-apiserver) |
| 03.03 | etcd | Persistência do estado | [Referência](https://kubernetes.io/docs/concepts/overview/components/#etcd) |
| 03.04 | Admission Controllers | Validação e mutação de requisições | [Referência](https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers/) |
| 03.05 | kube-controller-manager | Loops de reconciliação nativos | [Referência](https://kubernetes.io/docs/concepts/overview/components/#kube-controller-manager) |
| **03.06** | **CRDs e Custom Resources** | **Estender a API Kubernetes** | **[📖 Estudar](crds-custom-resources/README.md)** |
| **03.07** | **Custom Controllers e Operators** | **Implementar reconciliação própria** | **[📖 Estudar](custom-controllers-operators/README.md)** |
| 03.08 | kube-scheduler | Agendamento de Pods | [Referência](https://kubernetes.io/docs/concepts/scheduling-eviction/kube-scheduler/) |
| 03.09 | cloud-controller-manager | Integração com provedores cloud | [Referência](https://kubernetes.io/docs/concepts/architecture/cloud-controller/) |
| 03.10 | kubelet | Agente em cada nó | [Referência](https://kubernetes.io/docs/concepts/overview/components/#kubelet) |
| 03.11 | Container Runtime | Execução via CRI | [Referência](https://kubernetes.io/docs/setup/production-environment/container-runtimes/) |
| 03.12 | CNI e comunicação de rede | Conectividade dos Pods | [Referência](https://kubernetes.io/docs/concepts/cluster-administration/networking/) |
| 03.13 | kube-proxy e eBPF | Dataplane de Services | [Referência](https://kubernetes.io/docs/reference/networking/virtual-ips/) |
| 03.14 | CoreDNS e Service Discovery | DNS de serviços e Pods | [Referência](https://kubernetes.io/docs/concepts/services-networking/dns-pod-service/) |
| 03.15 | CSI e Storage | Integração de volumes e drivers | [Referência](https://kubernetes.io/docs/concepts/storage/volumes/#csi) |
| 03.16 | Gateway API | APIs de roteamento de tráfego | [Referência](https://gateway-api.sigs.k8s.io/) |
| 03.17 | Kustomize e Helm | Customização e empacotamento | [Kustomize](https://kubernetes.io/docs/tasks/manage-kubernetes-objects/kustomization/) · [Helm](https://helm.sh/docs/) |

> **Status:** 17 tópicos catalogados; dois guias de introdução publicados. Os labs de observação, CRDs e controllers ainda são roteiros, não exercícios validados.

## 🔎 Observação guiada — próximos labs

| Etapa | Pergunta para investigar | Ponto de observação |
| :---: | --- | --- |
| **01** | Onde ficam os componentes do Control Plane no Kind? | Pods do namespace `kube-system` |
| **02** | O que acontece com um Pod sem nó elegível? | Pending e eventos de scheduling |
| **03** | Como identificar em qual Worker um Pod roda? | `kubectl get pods -o wide` e Node |
| **04** | Como um Service é descoberto por DNS? | CoreDNS e consultas internas |
| **05** | Qual a diferença entre Service e implementação do dataplane? | kube-proxy ou solução alternativa instalada |

Esses são **roteiros de investigação**, não scripts testados. O cloud-controller-manager pode não existir no Kind, e a implementação de rede depende da configuração do cluster.

## 🎯 Checklist de aprendizado

- [ ] Explicar o fluxo `kubectl → API Server → controllers/scheduler → kubelet`.
- [ ] Distinguir estado persistido no etcd e execução dos containers.
- [ ] Identificar responsabilidades de CNI, CoreDNS, kube-proxy e CSI.
- [ ] Descrever as diferenças entre arquitetura local e gerenciada em cloud.
- [ ] Diferenciar CRDs, Custom Resources e controladores que reconciliam o estado.

## 🔗 Materiais relacionados

[Fundamentos originais](../../1-fundamentos/README.md) · [Topologia Kind](../../kind-config.yaml) · [Documentação Kubernetes Components](https://kubernetes.io/docs/concepts/overview/components/)

---

[**← 02 · Operação e Segurança**](../02-operacao-seguranca/README.md) · [↑ Roadmap](../../docs/roadmap.md) · **[04 · Platform Engineering →](../04-platform-engineering/README.md)**
