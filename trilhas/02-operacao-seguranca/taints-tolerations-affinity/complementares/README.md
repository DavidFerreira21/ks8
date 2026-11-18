# Complementar 02.07 — Scheduling: matriz de decisão

[← Aula 02.07](../README.md) · [🧪 Lab 02.07](../../labs/scheduling-basico/README.md) · [↑ Camada 02](../../README.md)

> **Leitura opcional.** Referência para consulta após a aula e o lab; não é pré-requisito e não repete o desafio YAML.

## Quando consultar

Para diagnosticar `FailedScheduling` e selecionar estratégia de alocação.

## Comparação de estratégias

| Configuração | Resultado |
| --- | --- |
| `nodeSelector` | Requer label do nó |
| Node affinity `required` | Restringe agendamento |
| Node affinity `preferred` | Expressa preferência |
| Taint `NoSchedule` | Repele novos Pods sem toleration |
| Toleration | Permite agendamento, não escolhe nó |
| TopologySpread | Tenta distribuir réplicas entre domínios |

## Diagnóstico

```bash
kubectl get nodes --show-labels
kubectl describe node NODE
kubectl describe pod POD -n NAMESPACE
kubectl get events -n NAMESPACE --sort-by=.lastTimestamp
```

A falta de capacidade, labels, tolerations ou políticas pode produzir o mesmo sintoma Pending. Nunca modifique taints do cluster compartilhado para contornar o exercício.

## Referências oficiais

[Assign Pods to Nodes](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/) · [Taints](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/)

---

[↑ Aula 02.07](../README.md) · [↑ Camada 02](../../README.md)
