# Complementar 01.01 — Ecossistema e ambiente Kubernetes

[← Aula 01.01](../trilhas/01-fundamentos/fundamentos/README.md) · [🧪 Lab 01.01](../trilhas/01-fundamentos/labs/fundamentos-cluster/README.md) · [↑ Camada 01](../trilhas/01-fundamentos/README.md)

> **Leitura opcional:** referência para entender tecnologias ao redor do Kubernetes e escolher ferramentas locais. A [aula](../trilhas/01-fundamentos/fundamentos/README.md) explica o funcionamento do cluster; o [lab](../trilhas/01-fundamentos/labs/fundamentos-cluster/README.md) conduz a prática com Kind. Não é necessário estudar este texto para concluir o lab.

## Quando consultar

- Ao diferenciar Docker/Podman, imagens OCI e container runtimes usados pelo Kubernetes.
- Ao comparar opções de cluster local para estudo e CI.
- Ao investigar conexões e portas entre os componentes do cluster.

## Engine, runtime, CRI e OCI: não são a mesma coisa

| Elemento | Papel | Exemplos |
| --- | --- | --- |
| Ferramenta/engine de containers | Constrói imagens, gerencia containers locais e outras funcionalidades | Docker, Podman |
| Runtime compatível com CRI | Interface de execução de containers consumida pelo kubelet | containerd, CRI-O |
| Runtime de baixo nível | Cria e executa processos de containers sob o sistema operacional | runc, crun |
| Padrões OCI | Definem formatos e interfaces portáveis para imagens e execução | OCI Image Specification, OCI Runtime Specification |

A **OCI** padroniza formatos e especificações; a **CRI** é a interface entre o kubelet e o runtime no nó. Docker pode ser usado no host do Kind para hospedar os nós, enquanto o Kubernetes dentro desses nós usa seu próprio runtime. Nem toda ferramenta listada na tabela implementa a mesma interface.

**Limitação importante:** um container estar saudável no Docker do computador não garante que o Pod esteja pronto no Kubernetes. São ambientes, mecanismos de rede e políticas de controle diferentes.

## Quando usar cada ambiente local?

| Ferramenta | Valor para estudo | Atenção |
| --- | --- | --- |
| [Kind](https://kind.sigs.k8s.io/docs/user/quick-start/) | Clusters descartáveis em containers; adequado a labs e CI | Nós são containers, não equivalem a VMs/hosts de produção |
| [Minikube](https://minikube.sigs.k8s.io/docs/start/) | Desenvolvimento local e experimentos com addons | Drivers e recursos disponíveis variam por host |
| [k3s](https://docs.k3s.io/) | Distribuição leve para laboratório e casos de edge | Difere da instalação upstream em componentes e defaults |
| [MicroK8s](https://microk8s.io/docs) | Ambiente local/edge com gerenciamento de addons | Requisitos e comportamento dependem do sistema |
| [k0s](https://docs.k0sproject.io/) | Distribuição compacta para diferentes topologias | Exige planejamento de operação conforme o cenário |

**Neste Learning Path, use Kind.** Os demais são alternativas de aprofundamento, não pré-requisitos.

## Portas e conectividade: consulta rápida

| Porta | Uso típico | Observação |
| --- | --- | --- |
| TCP 6443 | Kubernetes API Server | Pode ser alterada conforme a configuração |
| TCP 2379–2380 | etcd | Relevante para topologias com etcd |
| TCP 10250 | kubelet API | Deve ter acesso cuidadosamente controlado |
| TCP 10257 | kube-controller-manager seguro | Depende da topologia |
| TCP 10259 | kube-scheduler seguro | Depende da topologia |
| TCP 30000–32767 | Faixa padrão de NodePort | Configurável no API Server |

As portas não são uma receita de regras abertas no firewall. Verifique [portas e protocolos oficiais](https://kubernetes.io/docs/reference/networking/ports-and-protocols/) e a topologia específica; não utilize como referência portas legadas inseguras 10251/10252.

## Referência de inspeção (somente leitura)

```bash
kubectl config current-context
kubectl cluster-info
kubectl get nodes -o wide
kubectl get --raw /readyz
kubectl api-resources
```

Se uma consulta falhar, diferencie contexto errado, API inacessível e falta de permissão. Um `kubectl apply` bem-sucedido não atesta sozinho a saúde do workload.

## Referências oficiais

- [OCI — especificações](https://opencontainers.org/)
- [Container Runtime Interface](https://kubernetes.io/docs/concepts/architecture/cri/)
- [Kind — configuração](https://kind.sigs.k8s.io/docs/user/configuration/)
- [Ferramentas kubectl](https://kubernetes.io/docs/tasks/tools/)
- [Cheat sheet kubectl](https://kubernetes.io/docs/reference/kubectl/cheatsheet/)
