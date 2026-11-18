# Complementar 01.04 — Comparação operacional dos controladores

[← Aula 01.04](../trilhas/01-fundamentos/controladores/README.md) · [🧪 Lab 01.04](../trilhas/01-fundamentos/labs/controladores-basico/README.md) · [↑ Camada 01](../trilhas/01-fundamentos/README.md)

> **Leitura opcional:** comparação de casos de uso e procedimentos de inspeção para ReplicaSet, DaemonSet e StatefulSet. Não substitui a explicação da aula nem o desafio YAML do lab.

## Quando usar cada controlador?

| Recurso | Finalidade operacional | Exemplos de uso | Cuidado |
| --- | --- | --- | --- |
| ReplicaSet | Manter um número desejado de Pods equivalentes | Normalmente gerenciado por Deployment | Evite gerenciá-lo manualmente quando um Deployment resolve |
| DaemonSet | Executar Pods em nós elegíveis | Agentes de observabilidade, rede e segurança | Taints, selectors e tolerations afetam a distribuição |
| StatefulSet | Manter identidade estável e ordem de Pods | Sistemas que precisam de nomes previsíveis ou armazenamento por réplica | Não fornece por si só replicação de dados nem backup |

Um DaemonSet **não garante um Pod em todo nó indiscriminadamente**: seleção de nós, taints, tolerations e condições de agendamento precisam ser consideradas. Um StatefulSet pode usar `volumeClaimTemplates`, mas a persistência depende da infraestrutura de storage.

## Comandos para identificar controladores e seus Pods

```bash
kubectl get deployments,replicasets,daemonsets,statefulsets -n NAMESPACE
kubectl get pods -n NAMESPACE -o wide
kubectl describe replicaset NOME -n NAMESPACE
kubectl describe daemonset NOME -n NAMESPACE
kubectl describe statefulset NOME -n NAMESPACE
kubectl get pvc -n NAMESPACE
```

Substitua `NAMESPACE` e `NOME`. Para entender quem controla um Pod, inspecione `metadata.ownerReferences` com `kubectl get pod POD -n NAMESPACE -o yaml`. Um ReplicaSet controlado por Deployment possui, por sua vez, seu próprio `ownerReferences`.

## Cenários complementares de diagnóstico

| Observação | Investigue |
| --- | --- |
| DaemonSet com Pods desejados diferentes do número de nós | Node selectors, taints, tolerations e nós elegíveis |
| StatefulSet sem todas as réplicas prontas | Ordem de criação, readiness, PVCs e eventos |
| ReplicaSet antigo permanece no cluster | Histórico de revisões mantido pelo Deployment |
| PVC de StatefulSet permanece após remover Pods | Política de retenção de PVCs e StorageClass |

## Boas práticas e limitações

- Não delete ReplicaSets de um Deployment como forma de atualizar a aplicação.
- Não faça escala de nós do EKS como parte deste lab: o objetivo é observar o controlador, não modificar infraestrutura cloud.
- Remover um StatefulSet não implica necessariamente apagar PVCs; revise a política de retenção antes de excluir armazenamento.

## Referências oficiais

- [ReplicaSet](https://kubernetes.io/docs/concepts/workloads/controllers/replicaset/)
- [DaemonSet](https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/)
- [StatefulSet](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/)
