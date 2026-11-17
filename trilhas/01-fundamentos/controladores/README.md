# ReplicaSet, DaemonSet e StatefulSet

[← Camada 01](../README.md) · [Roadmap](../../../docs/roadmap.md) · [Início](../../../README.md)

> **Migração progressiva:** este é o ponto de entrada da aula. A explicação e os exercícios originais seguem preservados em [4-replicaSet-daemonSet-statefulSet/README.md](../../../4-replicaSet-daemonSet-statefulSet/README.md). Não movemos nem alteramos os manifests existentes neste PR.

## Objetivo

Comparar três mecanismos de controle de Pods com requisitos de execução diferentes.

## Ao concluir, você deverá conseguir

- Entender a função do ReplicaSet e sua relação com Deployment
- Identificar quando DaemonSet executa Pods por nó elegível
- Explorar identidade persistente de Pods em StatefulSet

## Estude o conceito

Leia a [aula original](../../../4-replicaSet-daemonSet-statefulSet/README.md), que contém os exemplos, explicações e comandos já presentes na trilha.

**Infográfico:** espaço reservado; o PNG será incluído em um PR posterior, após revisão editorial/técnica.

## Laboratório e observação

**Pré-requisito:** [Kind configurado](../../../install-kind.md) e contexto correto selecionado. Confira `kubectl config current-context` antes de executar comandos que alterem o cluster.

Use os manifests e exemplos da [aula original](../../../4-replicaSet-daemonSet-statefulSet/README.md). Para observar o cluster:

```bash
kubectl get replicasets
kubectl get daemonsets -A
kubectl get statefulsets -A
kubectl get pods -o wide
```

> Substitua os valores entre `<...>` pelos recursos realmente criados. Os comandos acima são referências para estudo; a execução não foi testada neste PR.

Os exercícios com falhas intencionais e critérios de aceitação serão padronizados nas próximas etapas.

## Documentação oficial

- [Kubernetes — ReplicaSet, DaemonSet e StatefulSet](https://kubernetes.io/docs/concepts/workloads/controllers/)

**Próximo tópico:** [Probes](../probes/README.md).
