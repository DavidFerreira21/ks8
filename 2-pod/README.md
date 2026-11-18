# Complementar 01.02 — Inspeção e diagnóstico de Pods

[← Aula 01.02](../trilhas/01-fundamentos/pods/README.md) · [🧪 Lab 01.02](../trilhas/01-fundamentos/labs/pods-basico/README.md) · [↑ Camada 01](../trilhas/01-fundamentos/README.md)

> **Leitura opcional:** referência operacional para investigar um Pod depois de estudar o conceito. A aula ensina o objeto; o lab ensina a criá-lo e observar seu comportamento. Aqui reunimos comandos e situações adicionais, não um segundo roteiro de lab.

## Quando consultar

- Quando um container não inicia ou reinicia repetidamente.
- Quando precisar obter logs de um container específico ou anterior.
- Para decidir entre `logs`, `exec`, `attach` e `debug`.

## Referência de comandos

Substitua `NAMESPACE`, `POD` e `CONTAINER` por nomes reais. Confirme o contexto antes de investigar.

```bash
kubectl config current-context
kubectl get pods -n NAMESPACE -o wide
kubectl describe pod POD -n NAMESPACE
kubectl get pod POD -n NAMESPACE -o yaml
kubectl logs POD -n NAMESPACE -c CONTAINER --tail=100
kubectl logs POD -n NAMESPACE -c CONTAINER --previous --tail=100
kubectl exec -it POD -n NAMESPACE -c CONTAINER -- /bin/sh
kubectl get events -n NAMESPACE --sort-by=.lastTimestamp
```

| Comando | Quando usar | Limitação |
| --- | --- | --- |
| `logs` | Ler a saída do processo do container | Não mostra todos os eventos do scheduler/kubelet |
| `logs --previous` | Investigar a execução anterior após restart | Só funciona quando há container anterior com logs disponíveis |
| `exec` | Executar um comando dentro de container já ativo | Imagens mínimas podem não ter shell |
| `attach` | Conectar à entrada/saída do processo principal | Não substitui um shell; pode interferir em sessão interativa |
| `debug` | Diagnóstico com container efêmero, quando permitido | Exige permissões e suporte no cluster; pode ter limitações de isolamento |

## Diagnóstico por sintoma

| Sintoma observado | Hipóteses para investigar | Evidência |
| --- | --- | --- |
| `Pending` | Falta de recursos, restrições de agendamento, volumes | `describe pod`, eventos e condições |
| `ImagePullBackOff` | Tag incorreta, acesso ao registry, autenticação | Eventos de pull e `imagePullSecrets` |
| `CrashLoopBackOff` | Processo encerra, configuração incorreta, falha da aplicação | `logs --previous`, exit code, eventos |
| `Running` mas não pronto | Readiness falha ou container ainda inicializando | `get pod`, condições e `describe` |

**Não confunda:** `ImagePullBackOff` e `CrashLoopBackOff` são motivos exibidos para containers, não valores de `status.phase` do Pod.

## Exemplo complementar: containers no mesmo Pod

Um sidecar pode operar ao lado do container principal, compartilhando o namespace de rede e, quando declarados, volumes. **Compartilhar Pod não significa compartilhar filesystem por padrão**; isso depende de `volumeMounts`. Evite adicionar containers apenas para simular dois serviços independentes.

Para experimentar esse cenário, consulte a [documentação oficial de sidecars](https://kubernetes.io/docs/concepts/workloads/pods/sidecar-containers/) após concluir o lab básico.

## Limites deste documento

- CPU e memória são tratados na [Aula 01.09 — Requests e Limits](../trilhas/01-fundamentos/requests-limits/README.md).
- Armazenamento `emptyDir` e PVCs são tratados na [Aula 01.11 — Volumes](../trilhas/01-fundamentos/volumes/README.md).
- Probes são tratados na [Aula 01.10](../trilhas/01-fundamentos/probes/README.md).

Não execute comandos de exclusão como parte de um diagnóstico sem entender o controlador que recriará os Pods.

## Referências oficiais

- [Debug Pods](https://kubernetes.io/docs/tasks/debug/debug-application/debug-pods/)
- [kubectl logs](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_logs/)
- [Debugging with ephemeral containers](https://kubernetes.io/docs/tasks/debug/debug-application/debug-running-pod/)
