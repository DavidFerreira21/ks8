# Complementar 04.07 — Observabilidade: scrape, PromQL e dashboards

[← Aula 04.07](../README.md) · [🧪 Lab 04.07](../../labs/prometheus-grafana-basico/README.md) · [↑ Camada 04](../../README.md)

> **Leitura opcional:** matriz de decisão e diagnóstico para consulta. Não é pré-requisito para executar o laboratório.

## Quando consultar

Quando ServiceMonitor existe, mas o target não aparece no Prometheus ou o Grafana não mostra dados.

| Etapa | Evidência | Diagnóstico |
| --- | --- | --- |
| Endpoint | `/metrics` responde | Container, Service, porta |
| ServiceMonitor | Selector e endpoint port nomeada | Labels, namespaceSelector |
| Prometheus | Target aparece e `up=1` | serviceMonitorSelector, logs |
| Grafana | Datasource conectado e painel | Query, tempo, labels |

## Exemplo de consulta

```promql
up{namespace="lab-04-07"}
```

Adapte labels ao target real descoberto; a presença de `up` depende do Prometheus configurado. Um ServiceMonitor pode estar válido na API, mas não ser selecionado por instância alguma. Grafana consulta séries e apresenta dashboards, não é o backend coletor.

## Referências oficiais

[Prometheus Operator](https://prometheus-operator.dev/docs/) · [Prometheus Querying](https://prometheus.io/docs/prometheus/latest/querying/basics/) · [Grafana](https://grafana.com/docs/)

---

[↑ Aula 04.07](../README.md) · [↑ Camada 04](../../README.md)
