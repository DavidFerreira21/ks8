# Lab 04.07 — Prometheus + Grafana

[← Aula 04.07](../../prometheus-grafana/README.md) · [↑ Camada 04](../../README.md) · [🧪 Índice dos labs](../../../../docs/labs.md)

> **MODO DESAFIO:** `make lab-prepare LAB=04.07` cria o namespace e copia um starter incompleto para `.labs/04.07/resources.yaml`. **Instale previamente o controlador/CRD do produto** de acordo com o procedimento documentado; complete o YAML e execute `kubectl apply --dry-run=server --validate=strict -f .labs/04.07/
kubectl apply -f .labs/04.07/`. O comando `make lab-up` usa a solução e é exclusivo de CI com os addons adequados.

## Objetivo e hipótese

Criar endpoint de métricas e ServiceMonitor, distinguindo presença do recurso de scrape e visualização reais.

**Contexto:** `kind-dev` ou cluster de sandbox explicitamente autorizado, namespace de estudo `lab-04-07`. `make lab-test` verifica objetos, **não prova sozinho a funcionalidade do controller**.

## Pré-requisitos da ferramenta

**Guia de instalação, versões e reversão:** [🛠️ Preparar Prometheus + Grafana](../../../../docs/ambientes/04-prometheus-grafana.md). Siga-o antes de aplicar Custom Resources; a CI padrão não instala esse controlador.

**Instale Prometheus Operator ou kube-prometheus-stack e Grafana** conforme as instruções oficiais, com descoberta de ServiceMonitors do namespace `lab-04-07`. A label `release: prometheus` é ilustrativa; o selector da instância Prometheus deve corresponder.

**Segurança:** Requer Operator, Prometheus configurado e Grafana; Kind padrão não executa scrape por instalar só ServiceMonitor.

## Desafio — o que você vai construir

Escreva Deployment `metrics-demo` com Node Exporter em porta 9100, Service `metrics-demo` com porta nomeada `metrics` e ServiceMonitor `metrics-demo` que selecione o Service por label e referencie a porta pelo nome.

Defina sua hipótese antes de consultar `solution/`. Se o tipo não aparecer em `kubectl api-resources`, registre dependência ausente e não tente contornar com recursos fictícios.

## Fase 1 — Preparar e prever

```bash
kubectl config current-context
make lab-prepare LAB=04.07
cat .labs/04.07/resources.yaml
```

Confirme disponibilidade da API específica da ferramenta e o namespace alvo antes de aplicar.

## Fase 2 — Aplicar e observar

Complete os TODOs:

```bash
kubectl apply -f .labs/04.07/
make lab-test LAB=04.07
make lab-observe LAB=04.07
```

`kubectl get servicemonitor -n lab-04-07`, `kubectl get endpointslices -n lab-04-07` e `kubectl port-forward -n lab-04-07 svc/metrics-demo 9100:9100` para verificar `/metrics` localmente.

## Fase 3 — Experimento controlado

Confirme endpoint `/metrics` do exporter, encontre o target na página de Targets do Prometheus e execute PromQL `up` filtrando pela identidade adequada. No Grafana conectado ao Prometheus, crie painel de uma série simples. Se ServiceMonitor não for selecionado, ajuste somente labels/selectors em ambiente de estudo.

## Resultado esperado e evidências

Endpoint responde métricas no formato Prometheus. **Scrape e visualização só ficam validados** se a instância Prometheus realmente selecionar ServiceMonitor e o datasource Grafana consultar as séries.

**Evidências específicas:** registre resposta `/metrics` sem dados sensíveis, alvo UP, consulta PromQL e painel Grafana (quando disponível). Apenas existência do ServiceMonitor é validação declarativa.

## Fase 4 — Diagnosticar

Investigue CRDs, condições dos custom resources, logs do controller instalado e permissões. Diferencie **rejeição de API**, **ausência de controller**, **reconciliação não pronta** e **falta de dependência externa**.

## Fase 5 — Limpar com segurança

```bash
make lab-down LAB=04.07
make lab-status LAB=04.07
```

A limpeza remove os objetos declarados neste contrato, **não desinstala automaticamente o addon**. Revise recursos filhos, credenciais e qualquer custo externo antes de excluir a instalação. Na ausência do addon, não tente remoção indiscriminada.

## Critérios de conclusão

- [ ] Escrevi o manifesto principal sem copiar a solução e validei as APIs necessárias.
- [ ] **Critério exclusivo 04.07:** registre resposta `/metrics` sem dados sensíveis, alvo UP, consulta PromQL e painel Grafana (quando disponível). Apenas existência do ServiceMonitor é validação declarativa.
- [ ] Diferenciei validação declarativa de comportamento funcional realmente observado.
- [ ] Reverti mudanças temporárias e executei a limpeza segura.

## Perguntas de diagnóstico e reflexão

- Por que endpoints.port referencia o nome da porta do Service?
- Como diagnosticar ServiceMonitor não selecionado?
- Qual papel de Grafana em relação ao Prometheus?

## Aprofunde seus conhecimentos

[Documentação oficial](https://prometheus-operator.dev/docs/) · [Aula 04.07](../../prometheus-grafana/README.md)

---

[← Lab 04.06](../cilium-basico/README.md) · [↑ Aula 04.07](../../prometheus-grafana/README.md) · [↑ Camada 04](../../README.md) · [↑ Catálogo](../../../../docs/catalogo.md)
