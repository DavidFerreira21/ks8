# Kubernetes Visual Guide — Estudos e Labs (ks8)

Uma trilha de Kubernetes em português, organizada para conectar **conceitos**, **arquitetura**, **exercícios práticos** e **documentação oficial**.

> **Em evolução:** a nova navegação está organizada em quatro camadas. As aulas e os manifests originais continuam nos mesmos caminhos; a migração e a inclusão dos infográficos acontecerão em etapas posteriores.

## Comece por aqui

1. Consulte o [roadmap de aprendizado](docs/roadmap.md).
2. Prepare o [ambiente Kind no WSL](install-kind.md) e confira o [kind-config.yaml](kind-config.yaml).
3. Escolha uma camada e avance pelos tópicos.
4. Execute os labs existentes e compare o resultado com os comandos de diagnóstico.
5. Aprofunde o tema usando as referências oficiais de cada guia.

## Trilha de aprendizado

| Camada | O que você vai aprender | Acessar |
| --- | --- | --- |
| **01 — Fundamentos** | Pods, Deployments, Services, Probes, Volumes e outros objetos essenciais | [Estudar](trilhas/01-fundamentos/README.md) |
| **02 — Operação e segurança** | RBAC, NetworkPolicy, agendamento, quotas e resiliência | [Estudar](trilhas/02-operacao-seguranca/README.md) |
| **03 — Arquitetura** | API Server, etcd, Scheduler, kubelet, rede, storage e componentes internos | [Estudar](trilhas/03-arquitetura/README.md) |
| **04 — Platform Engineering** | CRDs, Operators, Argo CD, Crossplane, Kyverno, GitOps e observabilidade | [Estudar](trilhas/04-platform-engineering/README.md) |

**[Ver o roadmap completo](docs/roadmap.md)**

## Aulas e laboratórios existentes

Estes links continuam apontando para as pastas originais. O conteúdo será reorganizado gradualmente, **sem descartar os exercícios**.

| Aula existente | Conteúdo |
| --- | --- |
| [Fundamentos](1-fundamentos/README.md) | Conceitos e primeiros comandos |
| [Pods](2-pod/README.md) | Criar, inspecionar e diagnosticar Pods |
| [Deployment](3-deployment/README.md) | Réplicas, estratégias e rollout |
| [ReplicaSet, DaemonSet e StatefulSet](4-replicaSet-daemonSet-statefulSet/README.md) | Modelos de controladores e manifests |
| [Probes](5-probes/README.md) | Liveness, readiness e startup |
| Volumes | Caminho original do README pendente de conferência durante a migração |
| [Services](7-services/README.md) | Tipos de Service e exposição de aplicações |

Também estão disponíveis o [resumo dos conceitos](resume.md) e o [guia de instalação](install-kind.md).

## Ambiente de laboratório

O repositório utiliza **Kind**, com configuração de um **Control Plane e dois Worker Nodes**, conforme o [manifest do cluster](kind-config.yaml). O guia atual descreve Windows, WSL2, Ubuntu e Docker Desktop.

Algumas instruções antigas citam comandos `make`; a existência e a compatibilidade desses alvos ainda precisam ser verificadas na padronização dos labs. Antes disso, use os comandos explícitos disponíveis nas aulas ou o [guia de instalação](install-kind.md), observando as versões indicadas.

## Como serão as novas aulas

Cada tema passará a trazer, conforme aplicável: **objetivo e pré-requisitos → explicação e diagrama → YAML/comandos → validação → experimento → troubleshooting → limpeza → referências oficiais**.

A trilha visual foi planejada com 44 temas. **Os infográficos ainda não foram adicionados aos diretórios do GitHub**; esta etapa estabelece a navegação que irá recebê-los.

## Fontes oficiais

- [Documentação Kubernetes](https://kubernetes.io/docs/home/)
- [Conceitos Kubernetes](https://kubernetes.io/docs/concepts/)
- [Tutoriais Kubernetes](https://kubernetes.io/docs/tutorials/)
- [Kind](https://kind.sigs.k8s.io/)

---

**Próximo passo da evolução do repositório:** migrar o conteúdo existente para os novos diretórios, revisar os laboratórios e integrar os infográficos por tópico.
