# Camada 01 — Fundamentos e recursos essenciais

[← Roadmap](../../docs/roadmap.md) · [Início](../../README.md)

**Objetivo:** compreender os objetos centrais do Kubernetes, executar uma aplicação, expô-la e inspecionar seu comportamento. A recomendação é fazer os exercícios no cluster Kind local.

## Roteiro de estudo

| Tópico | Para entender | Aula prática existente |
| --- | --- | --- |
| Fundamentos | Cluster, objetos, kubectl e primeiros comandos | [Fundamentos](../../1-fundamentos/README.md) |
| Pods | Unidade implantável, containers e ciclo de vida | [Pods](../../2-pod/README.md) |
| Deployments | Estado desejado, réplicas, rollout e rollback | [Deployment](../../3-deployment/README.md) |
| ReplicaSet, DaemonSet e StatefulSet | Três modelos de controle de Pods | [Controladores](../../4-replicaSet-daemonSet-statefulSet/README.md) |
| Probes | Startup, readiness e liveness | [Probes](../../5-probes/README.md) |
| Volumes | Armazenamento efêmero, PV/PVC e StorageClass | A localizar/revisar na migração |
| Services | Descoberta e acesso estável aos Pods | [Services](../../7-services/README.md) |
| Namespace | Escopo lógico de recursos | Conteúdo a estruturar |
| Ingress | Roteamento HTTP/HTTPS e controller | Conteúdo a estruturar |
| ConfigMap | Configurações não sensíveis | Conteúdo a estruturar |
| Secret | Dados sensíveis e distribuição a workloads | Conteúdo a estruturar |
| HPA | Escala horizontal orientada por métricas | Conteúdo a estruturar |
| Requests e Limits | Requisitos e limites de CPU/memória | [Exemplos no módulo Pods](../../2-pod/README.md) |

> Este índice inclui tópicos com infográficos já produzidos na conversa, mas **os arquivos de imagem ainda não estão publicados aqui**. Os links práticos apontam apenas para conteúdo que foi identificado com segurança.

## Percurso prático sugerido

1. Preparar o [Kind](../../install-kind.md) e conferir os nós.
2. Criar um Pod simples e observar seu estado.
3. Criar um Deployment com réplicas, alterar a imagem e verificar o rollout.
4. Expor os Pods por um Service e testar a descoberta dentro do cluster.
5. Introduzir probes e uma configuração de recursos; observar diferenças no status.
6. Revisitar o armazenamento e os tipos de controladores.

## Referências oficiais

- [Kubernetes Basics](https://kubernetes.io/docs/tutorials/kubernetes-basics/)
- [Pods](https://kubernetes.io/docs/concepts/workloads/pods/)
- [Deployments](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/)
- [Services](https://kubernetes.io/docs/concepts/services-networking/service/)
- [ConfigMaps](https://kubernetes.io/docs/concepts/configuration/configmap/)
- [Secrets](https://kubernetes.io/docs/concepts/configuration/secret/)

**Próxima camada:** [Operação, governança e segurança](../02-operacao-seguranca/README.md).
