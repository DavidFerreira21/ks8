# 🧩 Camada 03 · Arquitetura e infraestrutura

[⌂ Início](../../README.md) · [🗺️ Roadmap](../../docs/roadmap.md) · [🧪 Guia dos labs](../../docs/labs.md)

> **Objetivo da camada:** compreender como o Control Plane, os workers, a rede, a persistência e os mecanismos de extensão cooperam para transformar estado declarado em comportamento observado.

**17 aulas com infográfico e teoria** · **17 labs com YAML escrito pelo aluno** · **9 complementares opcionais**

## 🧭 Sequência de aprendizagem

1. **API e reconciliação:** arquitetura, API Server, etcd, admission, controllers, CRDs e Operators.
2. **Decisões e execução:** scheduler, cloud-controller-manager, kubelet e runtime.
3. **Rede e armazenamento:** CNI, Service dataplane, CoreDNS e CSI.
4. **Extensão e entrega:** Gateway API, Kustomize e Helm.

## 📚 Catálogo oficial da Camada 03

| Aula | Conceito | Aula | Lab | Complementares |
| --- | --- | --- | --- | --- |
| 03.01 | **Arquitetura do Cluster Kubernetes** | [📖 Estudar](arquitetura-cluster/README.md) | [🧪 Lab 03.01](labs/arquitetura-cluster-basico/README.md) | — |
| 03.02 | **kube-apiserver** | [📖 Estudar](kube-apiserver/README.md) | [🧪 Lab 03.02](labs/kube-apiserver-basico/README.md) | [Consultar](kube-apiserver/complementares/README.md) |
| 03.03 | **etcd** | [📖 Estudar](etcd/README.md) | [🧪 Lab 03.03](labs/etcd-basico/README.md) | [Consultar](etcd/complementares/README.md) |
| 03.04 | **Admission Controllers** | [📖 Estudar](admission-controllers/README.md) | [🧪 Lab 03.04](labs/admission-controllers-basico/README.md) | — |
| 03.05 | **kube-controller-manager** | [📖 Estudar](kube-controller-manager/README.md) | [🧪 Lab 03.05](labs/kube-controller-manager-basico/README.md) | — |
| 03.06 | **CRDs e Custom Resources** | [📖 Estudar](crds-custom-resources/README.md) | [🧪 Lab 03.06](labs/crds-custom-resources-basico/README.md) | [Consultar](crds-custom-resources/complementares/README.md) |
| 03.07 | **Custom Controllers e Operators** | [📖 Estudar](custom-controllers-operators/README.md) | [🧪 Lab 03.07](labs/custom-controllers-operators-basico/README.md) | [Consultar](custom-controllers-operators/complementares/README.md) |
| 03.08 | **kube-scheduler** | [📖 Estudar](kube-scheduler/README.md) | [🧪 Lab 03.08](labs/kube-scheduler-basico/README.md) | — |
| 03.09 | **cloud-controller-manager** | [📖 Estudar](cloud-controller-manager/README.md) | [🧪 Lab 03.09](labs/cloud-controller-manager-basico/README.md) | — |
| 03.10 | **kubelet** | [📖 Estudar](kubelet/README.md) | [🧪 Lab 03.10](labs/kubelet-basico/README.md) | — |
| 03.11 | **Container Runtime** | [📖 Estudar](container-runtime/README.md) | [🧪 Lab 03.11](labs/container-runtime-basico/README.md) | — |
| 03.12 | **CNI e comunicação de rede** | [📖 Estudar](cni-comunicacao/README.md) | [🧪 Lab 03.12](labs/cni-comunicacao-basico/README.md) | [Consultar](cni-comunicacao/complementares/README.md) |
| 03.13 | **kube-proxy e eBPF** | [📖 Estudar](kube-proxy-ebpf/README.md) | [🧪 Lab 03.13](labs/kube-proxy-ebpf-basico/README.md) | [Consultar](kube-proxy-ebpf/complementares/README.md) |
| 03.14 | **CoreDNS e Service Discovery** | [📖 Estudar](coredns/README.md) | [🧪 Lab 03.14](labs/coredns-basico/README.md) | — |
| 03.15 | **CSI e Storage** | [📖 Estudar](csi-storage/README.md) | [🧪 Lab 03.15](labs/csi-storage-basico/README.md) | [Consultar](csi-storage/complementares/README.md) |
| 03.16 | **Gateway API** | [📖 Estudar](gateway-api/README.md) | [🧪 Lab 03.16](labs/gateway-api-basico/README.md) | [Consultar](gateway-api/complementares/README.md) |
| 03.17 | **Kustomize e Helm** | [📖 Estudar](kustomize-helm/README.md) | [🧪 Lab 03.17](labs/kustomize-helm-basico/README.md) | [Consultar](kustomize-helm/complementares/README.md) |

## 🧪 Como estudar

Em cada aula, leia o conceito e o exemplo interpretado, depois abra o lab. O aluno executa `make lab-prepare LAB=03.XX`, preenche o starter em `.labs/03.XX/`, aplica com `kubectl apply`, observa, executa `make lab-test` e remove recursos com `make lab-down`. `make lab-up` usa a solução e **não é a prática inicial do aluno**.

**Evidência obrigatória:** estado declarado, comportamento observado, interpretação causal e cleanup. **Complementares não são pré-requisitos**: existem somente quando oferecem comparações, matrizes de decisão ou diagnóstico adicional.

[📊 Matriz de homologação dos 52 labs](../../docs/matriz-homologacao.md) · [🧪 Experimento real de Operator](labs/custom-controllers-operators-basico/examples/reconciler-real/README.md)

## ⚠️ Limites da prática

- **03.03:** o lab observa persistência via API; não acessa diretamente as chaves do etcd nem executa restore.
- **03.06:** instala CRD didática de escopo do cluster. Use **somente Kind descartável**; a exclusão de uma CRD pode excluir suas instâncias.
- **03.07:** usa Deployment para observar **reconciliação nativa**. Não implementa um Operator personalizado.
- **03.08:** Pod Pending é o resultado esperado do exercício de scheduler, não um erro do lab.
- **03.09:** Kind sem integração cloud não fornece LoadBalancer externo, e isso é esperado.
- **03.13:** declarar Service e observar EndpointSlices não prova implementação eBPF.
- **03.15:** exige StorageClass funcional; o Kind pode usar provisionador local em vez de CSI.
- **03.16:** sem CRDs/controlador Gateway, a experiência funcional de HTTPRoute é **dependência não atendida**. O lab básico valida somente backend nativo.
- **03.17:** `kubectl kustomize` funciona sem Helm; comparação com Helm depende do binário e chart inspecionado.

**Homologação:** arquivos e contratos não são equivalentes a execução funcional. A CI verifica construção, schema básico, links e um smoke Kind definido por versão. Experimentos guiados só podem ser considerados homologados com evidências específicas.

## ✅ Conclusão da camada

- [ ] Expliquei separadamente persistência, reconciliação, scheduling e execução.
- [ ] Observei recursos de Control Plane e Workers sem alterar componentes do sistema.
- [ ] Criei e consultei uma CR, distinguindo a API customizada de seu controlador.
- [ ] Comparei Pod IP, Service, EndpointSlices e DNS com resultados reais.
- [ ] Demonstrei persistência de PVC e distingui CSI de provisionador local.
- [ ] Identifiquei pré-requisitos ausentes para cloud-controller e Gateway API.
- [ ] Registrei hipótese, evidência, interpretação e limpeza de cada lab.

## 🔗 Referências oficiais

[Componentes Kubernetes](https://kubernetes.io/docs/concepts/overview/components/) · [Extensão da API](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/) · [Rede](https://kubernetes.io/docs/concepts/cluster-administration/networking/) · [Storage](https://kubernetes.io/docs/concepts/storage/)

---

[← Camada 02](../02-operacao-seguranca/README.md) · [↑ Roadmap](../../docs/roadmap.md) · [Próxima: Camada 04 →](../04-platform-engineering/README.md)
