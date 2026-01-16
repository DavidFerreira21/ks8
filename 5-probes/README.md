# Probes

## Indice

- [O que sao Probes](#o-que-sao-probes)
- [Tipos de probes e quando usar](#tipos-de-probes-e-quando-usar)
- [Liveness Probe](#liveness-probe)
- [Readiness Probe](#readiness-probe)
- [Startup Probe](#startup-probe)
- [Comandos rapidos](#comandos-rapidos)

## O que sao Probes

Probes sao verificacoes de saude que o Kubernetes executa dentro do container para
decidir se ele deve reiniciar o Pod, remover do Service ou aguardar a inicializacao.
Elas sao definidas no nivel do container e podem usar tres mecanismos:

- `httpGet`: testa um endpoint HTTP.
- `tcpSocket`: testa abertura de porta TCP.
- `exec`: executa um comando dentro do container.

## Tipos de probes e quando usar

- `livenessProbe`: detecta se o container travou ou ficou inconsistente. Falha gera restart.
- `readinessProbe`: indica se o container esta pronto para receber trafego.
- `startupProbe`: garante que o container finalize o bootstrap antes de ativar a liveness/readiness.

## Liveness Probe

Verifica se o processo esta saudavel. Se falhar repetidamente, o Pod e reiniciado.

Exemplo (arquivo `nginx-liveness.yaml`):

```yaml
        livenessProbe:
          tcpSocket:
            port: 80
          initialDelaySeconds: 10
          periodSeconds: 10
          timeoutSeconds: 5
          failureThreshold: 3
```

## Readiness Probe

Controla quando o Pod entra no balanceamento de carga do Service. Se falhar, o Pod
fica indisponivel para trafego, mas nao reinicia.

Exemplo (arquivo `nginx-readiness.yaml`):

```yaml
        readinessProbe:
          httpGet:
            path: /
            port: 80
          initialDelaySeconds: 10
          periodSeconds: 10
          timeoutSeconds: 5
          successThreshold: 2
          failureThreshold: 3
```

## Startup Probe

Usada para containers que demoram a subir. Enquanto ela nao passar, liveness/readiness
ficam desativadas.

Exemplo (arquivo `nginx-startup.yaml`):

```yaml
        startupProbe:
          httpGet:
            path: /
            port: 80
          initialDelaySeconds: 10
          periodSeconds: 10
          timeoutSeconds: 5
          successThreshold: 2
          failureThreshold: 3
```

## Comandos rapidos

- Aplicar o manifesto da liveness probe

```bash
kubectl apply -f nginx-liveness.yaml
```

- Aplicar o manifesto da readiness probe

```bash
kubectl apply -f nginx-readiness.yaml
```

- Aplicar o manifesto da startup probe

```bash
kubectl apply -f nginx-startup.yaml
```

- Verificar pods e status das probes

```bash
kubectl get pods
```

- Ver detalhes e eventos do pod

```bash
kubectl describe pod <nome-do-pod>
```
