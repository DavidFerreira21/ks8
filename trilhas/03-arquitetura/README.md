# 🧩 Camada 03 · Arquitetura e infraestrutura

[⌂ Início](../../README.md) · [🗺️ Roadmap](../../docs/roadmap.md) · [⚙️ Kind](../../kind-config.yaml)

> **Objetivo da camada**  
> Investigar como Control Plane, Workers, rede e armazenamento cooperam para transformar objetos declarativos em aplicações executadas.

**14 temas planejados** · **visão arquitetural e referências oficiais** · **labs de observação em planejamento**

---

## 🧭 Mapa dos componentes

| **CONTROL PLANE** | **WORKER NODES** |
| :--- | :--- |
| 🎛️ **Decidem, coordenam e reconciliam.**<br>API Server, etcd, Scheduler e Controller Manager.<br><br>[**Conhecer os componentes oficiais →**](https://kubernetes.io/docs/concepts/overview/components/) | ⚙️ **Executam e conectam os Pods.**<br>kubelet, container runtime e mecanismos de rede.<br><br>[**Explorar a arquitetura de nós →**](https://kubernetes.io/docs/concepts/architecture/nodes/) |
| **REDE E DESCOBERTA** | **ARMAZENAMENTO E EXTENSÃO** |
| 🌐 CNI, Service networking, CoreDNS, Gateway API e opções de dataplane.<br><br>[**Entender a rede →**](https://kubernetes.io/docs/concepts/cluster-administration/networking/) | 💾 CSI, provisionamento de volumes, Kustomize e Helm.<br><br>[**Conceitos de storage →**](https://kubernetes.io/docs/concepts/storage/) |

## 📚 Catálogo de arquitetura

### 🎛️ Control Plane — decisão e reconciliação

| Componente | Responsabilidade | Referência |
| --- | --- | --- |
| **Arquitetura do cluster** | Fluxo entre Control Plane e Workers | [Visão geral](https://kubernetes.io/docs/concepts/overview/components/) |
| **kube-apiserver** | Interface da API, autenticação, autorização e admission | [Componentes](https://kubernetes.io/docs/concepts/overview/components/#kube-apiserver) |
| **etcd** | Persistência consistente do estado de configuração do cluster | [Componentes](https://kubernetes.io/docs/concepts/overview/components/#etcd) |
| **kube-scheduler** | Escolha de nó para Pods ainda não agendados | [Scheduling](https://kubernetes.io/docs/concepts/scheduling-eviction/kube-scheduler/) |
| **kube-controller-manager** | Loops de controle e reconciliação | [Componentes](https://kubernetes.io/docs/concepts/overview/components/#kube-controller-manager) |
| **cloud-controller-manager** | Integração com recursos de um provedor cloud, quando disponível | [Cloud Controller Manager](https://kubernetes.io/docs/concepts/architecture/cloud-controller/) |

### ⚙️ Workers — execução de containers

| Componente | Responsabilidade | Referência |
| --- | --- | --- |
| **kubelet** | Agente que gerencia Pods atribuídos ao nó | [Componentes](https://kubernetes.io/docs/concepts/overview/components/#kubelet) |
| **Container Runtime** | Execução de containers via CRI | [Container Runtimes](https://kubernetes.io/docs/setup/production-environment/container-runtimes/) |

### 🌐 Rede, storage e configuração

| Componente | Responsabilidade | Referência |
| --- | --- | --- |
| **kube-proxy e eBPF** | Implementações possíveis do dataplane para Services; variam por cluster | [Service Virtual IPs](https://kubernetes.io/docs/reference/networking/virtual-ips/) |
| **CNI e comunicação** | Rede dos Pods e conectividade entre nós | [Networking](https://kubernetes.io/docs/concepts/cluster-administration/networking/) |
| **CoreDNS e Service Discovery** | Resolução de nomes dentro do cluster | [DNS for Services](https://kubernetes.io/docs/concepts/services-networking/dns-pod-service/) |
| **CSI e Storage** | Integração e provisionamento de armazenamento | [CSI](https://kubernetes.io/docs/concepts/storage/volumes/#csi) |
| **Gateway API** | APIs de roteamento e configuração de tráfego | [Gateway API](https://kubernetes.io/docs/concepts/services-networking/gateway/) |
| **Kustomize e Helm** | Customização e empacotamento de manifests | [Kustomize](https://kubernetes.io/docs/tasks/manage-kubernetes-objects/kustomization/) · [Helm](https://helm.sh/docs/) |

> **Status:** estes tópicos estão reunidos como roteiro de arquitetura e links oficiais. Ainda não existem páginas individuais ou labs executáveis desta camada no repositório.

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

## 🔗 Materiais relacionados

[Fundamentos originais](../../1-fundamentos/README.md) · [Topologia Kind](../../kind-config.yaml) · [Documentação Kubernetes Components](https://kubernetes.io/docs/concepts/overview/components/)

---

[**← 02 · Operação e Segurança**](../02-operacao-seguranca/README.md) · [↑ Roadmap](../../docs/roadmap.md) · **[04 · Platform Engineering →](../04-platform-engineering/README.md)**
