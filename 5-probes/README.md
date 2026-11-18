# Complementar 01.10 — Ajuste e diagnóstico de Probes

[← Aula 01.10](../trilhas/01-fundamentos/probes/README.md) · [🧪 Lab 01.10](../trilhas/01-fundamentos/labs/probes-basico/README.md) · [↑ Camada 01](../trilhas/01-fundamentos/README.md)

> **Leitura opcional:** padrões de configuração, sinais de falha e decisões operacionais sobre probes. A aula explica liveness, readiness e startup; o lab permite observar os efeitos. Aqui o foco é escolher parâmetros e diagnosticar divergências.

## Quando ajustar

- Aplicações com tempo de inicialização elevado ou variável.
- Containers que reiniciam quando uma dependência externa está indisponível.
- Workloads marcados como `Running`, mas ainda não prontos para tráfego.

## Escolha da verificação

| Probe | Pergunta respondida | Consequência após falhas |
| --- | --- | --- |
| `livenessProbe` | O processo ainda consegue funcionar? | Container reiniciado pelo kubelet |
| `readinessProbe` | A aplicação pode receber tráfego agora? | Pod deixa de ser considerado pronto; endpoints refletem o estado |
| `startupProbe` | A inicialização terminou? | Enquanto não tiver sucesso, liveness/readiness não são executadas; falhas excessivas podem reiniciar o container |

Uma dependência externa temporariamente indisponível costuma ser sinal inadequado para liveness: reiniciar containers em massa pode piorar o incidente.

## Exemplo complementar: app com inicialização demorada

O trecho abaixo pertence ao item de um container dentro de `spec.containers`; **não é um manifesto completo**.

```yaml
startupProbe:
  httpGet:
    path: /startup
    port: 8080
  periodSeconds: 5
  failureThreshold: 24
readinessProbe:
  httpGet:
    path: /ready
    port: 8080
  periodSeconds: 5
  failureThreshold: 2
livenessProbe:
  httpGet:
    path: /live
    port: 8080
  periodSeconds: 10
  failureThreshold: 3
```

A combinação `periodSeconds: 5` e `failureThreshold: 24` permite aproximadamente 120 segundos para a startup probe obter sucesso, desconsiderando particularidades de agendamento e execução. As rotas HTTP precisam existir de fato na aplicação; não copie esses caminhos automaticamente para nginx.

## Como investigar falhas

```bash
kubectl get pods -n NAMESPACE
kubectl describe pod POD -n NAMESPACE
kubectl logs POD -n NAMESPACE -c CONTAINER --previous
kubectl get events -n NAMESPACE --sort-by=.lastTimestamp
```

| Sintoma | Hipótese de diagnóstico |
| --- | --- |
| Restarts frequentes | Liveness/startup agressiva, falha de processo ou OOM |
| Pod `Running` e `0/1 Ready` | Readiness falhando, container ainda iniciando |
| HTTP 404 em probe | Caminho incorreto ou handler não implementado |
| Timeout | Aplicação lenta, porta incorreta, saturação ou problemas de conectividade |

**Cuidados:** `initialDelaySeconds`, `periodSeconds`, `timeoutSeconds`, `failureThreshold` e `successThreshold` devem refletir o comportamento real. A startup probe não elimina a necessidade de readiness. Probes não substituem monitoramento e SLOs.

## Referências oficiais

- [Configure Liveness, Readiness and Startup Probes](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/)
- [Pod Lifecycle](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/)
