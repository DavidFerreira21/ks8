# Deployments

[← Camada 01](../README.md) · [Roadmap](../../../docs/roadmap.md) · [Início](../../../README.md)

> **Migração progressiva:** este é o ponto de entrada da aula. A explicação e os exercícios originais seguem preservados em [3-deployment/README.md](../../../3-deployment/README.md). Não movemos nem alteramos os manifests existentes neste PR.

## Objetivo

Entender como um Deployment gerencia ReplicaSets, réplicas e atualizações.

## Ao concluir, você deverá conseguir

- Criar e inspecionar um Deployment
- Observar a relação Deployment → ReplicaSet → Pods
- Executar rollout e rollback de forma controlada

## Estude o conceito

Leia a [aula original](../../../3-deployment/README.md), que contém os exemplos, explicações e comandos já presentes na trilha.

**Infográfico:** espaço reservado; o PNG será incluído em um PR posterior, após revisão editorial/técnica.

## Laboratório e observação

**Pré-requisito:** [Kind configurado](../../../install-kind.md) e contexto correto selecionado. Confira `kubectl config current-context` antes de executar comandos que alterem o cluster.

Use os manifests e exemplos da [aula original](../../../3-deployment/README.md). Para observar o cluster:

```bash
kubectl get deployment,rs,pods
kubectl rollout status deployment/<nome>
kubectl rollout history deployment/<nome>
kubectl rollout undo deployment/<nome>
```

> Substitua os valores entre `<...>` pelos recursos realmente criados. Os comandos acima são referências para estudo; a execução não foi testada neste PR.

Também há um [lab integrado Pod → Deployment → Service](../labs/primeira-aplicacao/README.md) com arquivos completos e procedimentos de validação.

## Documentação oficial

- [Kubernetes — Deployments](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/)

**Próximo tópico:** [ReplicaSet, DaemonSet e StatefulSet](../controladores/README.md).
