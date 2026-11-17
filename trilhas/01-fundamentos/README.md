# Camada 01 — Fundamentos e recursos essenciais

[← Roadmap](../../docs/roadmap.md) · [Início](../../README.md)

**Objetivo:** compreender os objetos centrais do Kubernetes, executar uma aplicação, expô-la e inspecionar seu comportamento. A recomendação é fazer os exercícios no cluster Kind local.

## Como estudar

Comece pelo [guia de instalação do Kind](../../install-kind.md), depois siga as aulas abaixo. Cada nova página contém o objetivo, o resultado esperado, comandos de inspeção, referência oficial e vínculo com a aula legada.

**Lab integrado:** [Primeira aplicação — Pod → Deployment → Service](labs/primeira-aplicacao/README.md). O laboratório tem YAMLs próprios para evitar conflitos com os exemplos originais.

## Roteiro de estudo

| Tópico | Nova entrada | Conteúdo prático |
| --- | --- | --- |
| Fundamentos | [Conceitos, cluster e kubectl](fundamentos/README.md) | [Aula legada](../../1-fundamentos/README.md) |
| Pods | [Pods](pods/README.md) | [Aula legada](../../2-pod/README.md) |
| Deployments | [Deployments](deployments/README.md) | [Aula legada](../../3-deployment/README.md) |
| ReplicaSet, DaemonSet e StatefulSet | [Controladores](controladores/README.md) | [Aula legada](../../4-replicaSet-daemonSet-statefulSet/README.md) |
| Probes | [Probes](probes/README.md) | [Aula legada](../../5-probes/README.md) |
| Volumes | A migrar após localização do conteúdo original | [Conceitos no resumo](../../resume.md) |
| Services | [Services](services/README.md) | [Aula legada](../../7-services/README.md) |
| Namespace | A estruturar | [Lab integrado usa namespace](labs/primeira-aplicacao/README.md) |
| Ingress | A estruturar | Consulte a documentação oficial |
| ConfigMap | A estruturar | Consulte a documentação oficial |
| Secret | A estruturar | Consulte a documentação oficial |
| HPA | A estruturar | Consulte a documentação oficial |
| Requests e Limits | A estruturar | [Exemplos na aula de Pods](../../2-pod/README.md) |

> **Status:** as seis páginas de entrada e o lab integrado foram incluídos no PR 2. Os 44 infográficos ainda não foram adicionados ao GitHub. A pasta antiga de Volumes, mencionada no índice histórico, não foi encontrada pelo conector e não foi recriada.

## Percurso prático sugerido

1. Suba o cluster [Kind](../../install-kind.md) e confira os nós.
2. [Crie um Pod](labs/primeira-aplicacao/README.md#etapa-1--namespace-e-pod-individual), verifique eventos e identifique em qual nó está.
3. [Crie um Deployment](labs/primeira-aplicacao/README.md#etapa-2--deployment-e-replicaset) e observe a reconciliação de réplicas.
4. [Exponha os Pods por Service](labs/primeira-aplicacao/README.md#etapa-3--service-e-descoberta) e teste conectividade.
5. [Inspecione o rollout](labs/primeira-aplicacao/README.md#etapa-4--rollout-e-rollback).
6. Retorne às aulas originais de Probes, controladores e armazenamento.

## Referências oficiais

- [Kubernetes Basics](https://kubernetes.io/docs/tutorials/kubernetes-basics/)
- [Pods](https://kubernetes.io/docs/concepts/workloads/pods/)
- [Deployments](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/)
- [Services](https://kubernetes.io/docs/concepts/services-networking/service/)
- [ConfigMaps](https://kubernetes.io/docs/concepts/configuration/configmap/)
- [Secrets](https://kubernetes.io/docs/concepts/configuration/secret/)

**Próxima camada:** [Operação, governança e segurança](../02-operacao-seguranca/README.md).
