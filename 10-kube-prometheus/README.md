# Kube Prometheus

## O que e o kube-prometheus?

`kube-prometheus` e um conjunto de manifestos para Kubernetes que instala e configura uma stack completa de observabilidade baseada no Prometheus Operator.

Principais componentes:

- Prometheus Operator
- Prometheus
- Alertmanager
- Grafana
- kube-state-metrics
- node-exporter
- Prometheus Adapter (em alguns cenarios)

Com isso, voce passa a ter:

- Coleta de metricas do cluster e workloads
- Dashboards prontos no Grafana
- Regras de alerta com Alertmanager
- Base para autoscaling com metricas customizadas

## Conceitos rapidos

### Prometheus

Banco de metricas em series temporais. Coleta dados de endpoints `/metrics`, armazena e permite consultas via PromQL.

### Grafana

Camada de visualizacao. Consome dados do Prometheus e apresenta dashboards para CPU, memoria, rede, pods, nodes e aplicacoes.

### Alertmanager

Gerencia alertas disparados pelo Prometheus. Faz agrupamento, silenciamento e roteamento para canais como Slack, email, etc.

### ServiceMonitor

CRD do Prometheus Operator que define como um Service deve ser monitorado (endpoints, intervalo, labels, namespace, etc).

## Instalacao (local com Kind)

```bash
git clone https://github.com/prometheus-operator/kube-prometheus.git
cd kube-prometheus

# 1) Instala CRDs e recursos base
kubectl apply --server-side -f manifests/setup

# Aguarda CRDs ficarem disponiveis
until kubectl get servicemonitors.monitoring.coreos.com >/dev/null 2>&1; do
  echo "Aguardando CRDs..."
  sleep 2
done

# 2) Instala stack completa
kubectl apply -f manifests/
```

## Validacao

```bash
kubectl get pods -n monitoring
kubectl get servicemonitors -n monitoring
kubectl get prometheus,alertmanager -n monitoring
```

## Acesso local (port-forward)

### Grafana

```bash
kubectl port-forward -n monitoring svc/grafana 3000:3000
```

Acesse: `http://localhost:3000`

### Prometheus

```bash
kubectl port-forward -n monitoring svc/prometheus-k8s 9090:9090
```

Acesse: `http://localhost:9090`

### Alertmanager

```bash
kubectl port-forward -n monitoring svc/alertmanager-main 9093:9093
```

Acesse: `http://localhost:9093`

## Exemplo de consulta PromQL

Uso de CPU por container:

```promql
sum(rate(container_cpu_usage_seconds_total{container!=""}[5m])) by (namespace, pod)
```

## Exemplo de ServiceMonitor

```yaml
apiVersion: monitoring.coreos.com/v1
kind: ServiceMonitor
metadata:
  name: meu-app-monitor
  namespace: monitoring
spec:
  selector:
    matchLabels:
      app: meu-app
  namespaceSelector:
    matchNames:
    - default
  endpoints:
  - port: http
    interval: 30s
    path: /metrics
```

## Troubleshooting rapido

- Ver eventos do namespace: `kubectl get events -n monitoring --sort-by=.lastTimestamp`
- Ver logs do operador: `kubectl logs -n monitoring deploy/prometheus-operator`
- Conferir status dos CRDs: `kubectl get crd | grep monitoring.coreos.com`

## Remocao

```bash
kubectl delete -f manifests/
kubectl delete -f manifests/setup
```
