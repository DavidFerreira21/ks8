# Complementar 02.10 — QoS e eviction: diagnóstico

[← Aula 02.10](../README.md) · [🧪 Lab 02.10](../../labs/qos-eviction-basico/README.md) · [↑ Camada 02](../../README.md)

> **Leitura opcional.** Referência para consulta após a aula e o lab; não é pré-requisito e não repete o desafio YAML.

## Quando consultar

Para diferenciar pressão de nó, OOM de container e falhas de agendamento.

## Diagnóstico por sintoma

| Sinal | Interpretação | Evidência |
| --- | --- | --- |
| `OOMKilled` | Processo encerrado por memória | `lastState.terminated.reason` |
| `Evicted` | Kubelet removeu Pod por pressão | `describe pod` e condições do nó |
| `Pending` | Scheduler não achou nó elegível | `FailedScheduling` |
| CPU throttling | Limitação de tempo de CPU | Métricas; não implica restart |

**Guaranteed** requer requests=limits de CPU e memória em cada container. **BestEffort** não declara nenhum deles; os demais geralmente são **Burstable**. A decisão de eviction considera também consumo acima de requests e prioridade, não apenas QoS.

```bash
kubectl get pod POD -n NAMESPACE -o jsonpath='{.status.qosClass}'
kubectl describe node NODE
```

## Referências oficiais

[Pod QoS](https://kubernetes.io/docs/concepts/workloads/pods/pod-qos/) · [Node Pressure Eviction](https://kubernetes.io/docs/concepts/scheduling-eviction/node-pressure-eviction/)

---

[↑ Aula 02.10](../README.md) · [↑ Camada 02](../../README.md)
