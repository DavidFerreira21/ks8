# Preparação 04.07 — Prometheus Operator e Grafana

[↑ Ambientes](README.md) · [🧪 Lab 04.07](../../trilhas/04-platform-engineering/labs/prometheus-grafana-basico/README.md)

> **Versão, Helm release e selectors importam.** A solução usa `ServiceMonitor.metadata.labels.release: prometheus`. Instale o Helm release com o nome **prometheus** ou atualize o label e o selector coerentemente.

## Instalar stack em Kind descartável

```bash
kubectl config current-context # kind-dev
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update
helm search repo prometheus-community/kube-prometheus-stack --versions | head
export MONITORING_CHART_VERSION=VERSAO_COMPATIVEL
: "${MONITORING_CHART_VERSION:?Defina chart stack}"
helm install prometheus prometheus-community/kube-prometheus-stack -n monitoring --create-namespace --version "$MONITORING_CHART_VERSION"
kubectl get pods -n monitoring
kubectl get prometheus -n monitoring
kubectl api-resources --api-group=monitoring.coreos.com
```

A stack pode exigir recursos importantes de CPU/memória; verifique capacidade do Kind antes de instalar.

## Diferenciar recurso, scrape e visualização

```bash
make lab-prepare LAB=04.07
kubectl apply -f .labs/04.07/
kubectl get servicemonitor metrics-demo -n lab-04-07 -o yaml
kubectl get endpointslices -n lab-04-07
kubectl get prometheus -n monitoring -o yaml
```

Confirme que o Prometheus seleciona **ServiceMonitors no namespace de estudo** e com o label de release correspondente. Teste `/metrics`, depois consulte Targets no Prometheus. Só declare scrape quando houver target **UP**, e só declare Grafana funcional quando o datasource estiver configurado e a consulta retornar uma série. O nome do Service de Grafana e endpoints pode variar com a versão/chart.

**Limpeza:** remova ServiceMonitor, Service e Deployment pelo lab; confira Targets ausentes; `helm uninstall prometheus -n monitoring` somente no Kind dedicado. Não exclua CRDs globais nem PVCs persistentes compartilhados sem inventário.

[Prometheus Operator](https://prometheus-operator.dev/docs/) · [Helm charts](https://github.com/prometheus-community/helm-charts) · [Grafana](https://grafana.com/docs/)