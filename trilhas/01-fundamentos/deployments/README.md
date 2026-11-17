# Deployments

[← Camada 01](../README.md) · [Roadmap](../../../docs/roadmap.md) · [Início](../../../README.md)

> **Material de apoio:** este guia organiza o estudo do conceito. Veja também as anotações, os comandos e os exercícios em [material complementar](../../../3-deployment/README.md).

## 🎨 Infográfico

![01.06 — Deployments](images/deployments.png)

> A imagem ilustra o conceito; consulte a documentação oficial para detalhes técnicos.


## Objetivo

Entender como um Deployment gerencia ReplicaSets, réplicas e atualizações.

## Ao concluir, você deverá conseguir

- Criar e inspecionar um Deployment
- Observar a relação Deployment → ReplicaSet → Pods
- Executar rollout e rollback de forma controlada

## Estude o conceito

Consulte as [anotações e exemplos práticos](../../../3-deployment/README.md), com explicações, exemplos e comandos para aprofundar o conceito.


## Laboratório e observação

**Pré-requisito:** [Kind configurado](../../../install-kind.md) e contexto correto selecionado. Confira `kubectl config current-context` antes de executar comandos que alterem o cluster.

Utilize os manifests e exemplos das [anotações e exemplos práticos](../../../3-deployment/README.md). Para observar o cluster:

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


---

### Navegação

[← Anterior](../pods/README.md) · [↑ Voltar à camada](../README.md) · [Próximo →](../controladores/README.md)
