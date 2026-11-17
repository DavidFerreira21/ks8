# Fundamentos

[← Camada 01](../README.md) · [Roadmap](../../../docs/roadmap.md) · [Início](../../../README.md)

> **Migração progressiva:** este é o ponto de entrada da aula. A explicação e os exercícios originais seguem preservados em [1-fundamentos/README.md](../../../1-fundamentos/README.md). Não movemos nem alteramos os manifests existentes neste PR.

## Objetivo

Conhecer containers, kubectl, o cluster Kubernetes e os primeiros objetos.

## Ao concluir, você deverá conseguir

- Identificar Control Plane e Worker Nodes
- Criar e inspecionar recursos com kubectl
- Preparar o Kind para os próximos exercícios

## Estude o conceito

Leia a [aula original](../../../1-fundamentos/README.md), que contém os exemplos, explicações e comandos já presentes na trilha.

**Infográfico:** espaço reservado; o PNG será incluído em um PR posterior, após revisão editorial/técnica.

## Laboratório e observação

**Pré-requisito:** [Kind configurado](../../../install-kind.md) e contexto correto selecionado. Confira `kubectl config current-context` antes de executar comandos que alterem o cluster.

Use os manifests e exemplos da [aula original](../../../1-fundamentos/README.md). Para observar o cluster:

```bash
kubectl config current-context
kubectl get nodes -o wide
kubectl get namespaces
kubectl get pods -A
```

> Substitua os valores entre `<...>` pelos recursos realmente criados. Os comandos acima são referências para estudo; a execução não foi testada neste PR.

Os exercícios com falhas intencionais e critérios de aceitação serão padronizados nas próximas etapas.

## Documentação oficial

- [Kubernetes — Fundamentos](https://kubernetes.io/docs/tutorials/kubernetes-basics/)

**Próximo tópico:** [Pods](../pods/README.md).
