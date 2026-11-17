# ReplicaSet, DaemonSet e StatefulSet

[← Camada 01](../README.md) · [Roadmap](../../../docs/roadmap.md) · [Início](../../../README.md)

> **Material de apoio:** este guia organiza o estudo do conceito. Veja também as anotações, os comandos e os exercícios em [material complementar](../../../4-replicaSet-daemonSet-statefulSet/README.md).

## 🎨 Infográfico

![01.07 — ReplicaSet, DaemonSet e StatefulSet](../replicaset-daemonset-statefulset/images/replicaset-daemonset-statefulset.png)

> **Revisão editorial:** o infográfico está disponível no repositório; confirme os detalhes técnicos com a documentação da aula.


## Objetivo

Comparar três mecanismos de controle de Pods com requisitos de execução diferentes.

## Ao concluir, você deverá conseguir

- Entender a função do ReplicaSet e sua relação com Deployment
- Identificar quando DaemonSet executa Pods por nó elegível
- Explorar identidade persistente de Pods em StatefulSet

## Estude o conceito

Consulte as [anotações e exemplos práticos](../../../4-replicaSet-daemonSet-statefulSet/README.md), com explicações, exemplos e comandos para aprofundar o conceito.


## Laboratório e observação

**Pré-requisito:** [Kind configurado](../../../install-kind.md) e contexto correto selecionado. Confira `kubectl config current-context` antes de executar comandos que alterem o cluster.

Utilize os manifests e exemplos das [anotações e exemplos práticos](../../../4-replicaSet-daemonSet-statefulSet/README.md). Para observar o cluster:

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


---

### Navegação

[← Anterior](../deployments/README.md) · [↑ Voltar à camada](../README.md) · [Próximo →](../probes/README.md)
