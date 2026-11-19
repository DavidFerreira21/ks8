# Complementar 01.02 — Diagnóstico diferencial de estados de Pod

[← Aula 01.02](../README.md) · [🧪 Lab 01.02](../../labs/pods-basico/README.md) · [↑ Camada 01](../../README.md)

> **Leitura opcional:** Consulte ao decidir se a falha está antes do start, no processo ou na readiness. Não substitui a aula nem o desafio do laboratório.

## Decisões e sintomas

| Situação | Leitura técnica |
| --- | --- |
| **Pending + FailedScheduling** | Verifique requests, affinities, taints e PVC. |
| **ImagePullBackOff** | Investigue pull, credenciais e tag de imagem; processo ainda não iniciou. |
| **CrashLoopBackOff** | Processo iniciou e encerrou repetidas vezes; procure logs e lastState. |
| **Running / Ready=False** | Examine readinessProbe e condições; o processo pode estar saudável. |

## Como interpretar as evidências

Compare `kubectl describe pod` e `kubectl logs --previous` antes de reiniciar o workload indiscriminadamente.

## Referência histórica preservada

O [material complementar original](../../../../2-pod/README.md) permanece acessível, com exemplos e comandos adicionais. Esta página reúne a comparação rápida no padrão editorial das demais camadas, sem duplicar todo o material antigo.

## Referências oficiais

[Documentação Kubernetes — Conceitos](https://kubernetes.io/docs/concepts/) · [Debugging](https://kubernetes.io/docs/tasks/debug/)

---

[↑ Aula 01.02](../README.md) · [↑ Camada 01](../../README.md)
