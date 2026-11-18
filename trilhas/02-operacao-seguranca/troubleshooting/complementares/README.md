# Complementar 02.14 — Troubleshooting: mapa de sintomas

[← Aula 02.14](../README.md) · [🧪 Lab 02.14](../../labs/troubleshooting-basico/README.md) · [↑ Camada 02](../../README.md)

> **Leitura opcional.** Referência para consulta após a aula e o lab; não é pré-requisito e não repete o desafio YAML.

## Quando consultar

Para diagnosticar sem começar com reinícios, exclusões ou correções especulativas.

| Sintoma | Evidência primária |
| --- | --- |
| `Pending` | Eventos do scheduler, PVC e quotas |
| `ImagePullBackOff` | Eventos de pull, nome/tag e acesso ao registry |
| `CrashLoopBackOff` | Logs anteriores e código de saída |
| Running sem Ready | Condições e probes |
| Service sem backend | Selectors e EndpointSlices |
| HPA com `<unknown>` | Metrics Server e requests CPU |

```bash
kubectl config current-context
kubectl describe pod POD -n NAMESPACE
kubectl get events -n NAMESPACE --sort-by=.lastTimestamp
kubectl logs POD -n NAMESPACE --previous
```

Um Pod sem container iniciado pode não ter logs. Registre sintomas, impacto, evidência, hipótese, mudança controlada e resultado antes de encerrar um incidente.

## Referências oficiais

[Debug Applications](https://kubernetes.io/docs/tasks/debug/debug-application/)

---

[↑ Aula 02.14](../README.md) · [↑ Camada 02](../../README.md)
