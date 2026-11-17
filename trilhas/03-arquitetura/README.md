# Camada 03 — Arquitetura e infraestrutura

[← Roadmap](../../docs/roadmap.md) · [Início](../../README.md)

**Objetivo:** entender como o cluster funciona internamente, separando responsabilidades do Control Plane, dos nós e das integrações de rede e armazenamento.

## Roteiro de estudo

| Grupo | Componente ou conceito | O que observar |
| --- | --- | --- |
| Visão geral | Arquitetura do cluster | Relação entre Control Plane e Workers |
| Control Plane | kube-apiserver | API, autenticação, autorização e admission |
| Control Plane | etcd | Persistência e consistência do estado do cluster |
| Control Plane | kube-scheduler | Escolha do nó para Pods pendentes |
| Control Plane | kube-controller-manager | Loops de reconciliação |
| Integração cloud | cloud-controller-manager | Integração com APIs do provedor, quando presente |
| Worker | kubelet | Execução e status dos Pods no nó |
| Worker | Container Runtime | Execução de containers via CRI |
| Rede | kube-proxy e eBPF | Diferentes implementações do encaminhamento para Services |
| Rede | CNI e comunicação | Rede dos Pods e conectividade entre nós |
| Rede | CoreDNS e Service Discovery | Resolução de nomes dos Services |
| Armazenamento | CSI e Storage | Integração com sistemas de armazenamento |
| Entrada | Gateway API | Recursos para roteamento de tráfego |
| Manifests | Kustomize e Helm | Customização e empacotamento de configurações |

O [módulo original de Fundamentos](../../1-fundamentos/README.md) já introduz parte da arquitetura. Aqui o estudo será aprofundado por componente, sem duplicar a aula introdutória.

## Labs de observação sugeridos (ainda não implementados)

1. Localizar componentes do Control Plane no Kind e inspecionar os Pods de sistema.
2. Observar um Pod Pending e os eventos de scheduling.
3. Relacionar o status de um Pod ao kubelet do nó escolhido.
4. Consultar a resolução DNS de um Service a partir de um Pod.
5. Comparar a abstração Service com o dataplane implementado pelo cluster.

> **Atenção:** componentes gerenciados, como o cloud-controller-manager, podem não estar disponíveis no Kind. Os labs distinguirão demonstração local de estudo conceitual.

## Referências oficiais

- [Kubernetes Components](https://kubernetes.io/docs/concepts/overview/components/)
- [Scheduling](https://kubernetes.io/docs/concepts/scheduling-eviction/kube-scheduler/)
- [Cluster Networking](https://kubernetes.io/docs/concepts/cluster-administration/networking/)
- [Storage](https://kubernetes.io/docs/concepts/storage/)
- [Gateway API](https://kubernetes.io/docs/concepts/services-networking/gateway/)

**Próxima camada:** [Platform Engineering e GitOps](../04-platform-engineering/README.md).
