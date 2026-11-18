# Lab 01.02 — Pods: ciclo de vida e diagnostico

[← Camada 01](../../README.md) · [Guia de labs](../../../../docs/labs.md)

## Objetivo e hipótese

Pod é a unidade mínima de execução agendada. Hipótese: se eu excluir um Pod isolado, ele será recriado automaticamente?

**Ambiente:** cluster Kind `dev`, namespace isolado `lab-01-02`. Leia primeiro a aula teórica correspondente. Os experimentos são locais e manuais para você observar cada transição.

## Fase 1 — Preparar e inspecionar

```bash
make doctor
kubectl config current-context
kubectl get nodes
cat trilhas/01-fundamentos/labs/pods-basico/resources.yaml
```

Antes de aplicar, preveja quais objetos serão criados e quais controladores participarão.

## Fase 2 — Aplicar e observar

```bash
make lab-up LAB=01.02
make lab-test LAB=01.02
make lab-observe LAB=01.02
```

**Observe o agendamento:**

```bash
kubectl get pod pod-demo -n lab-01-02 -o wide
kubectl describe pod pod-demo -n lab-01-02
kubectl logs pod-demo -n lab-01-02
```

**Experimento — Pod sem controlador:** exclua apenas o Pod e observe que não reaparece sozinho:

```bash
kubectl delete pod pod-demo -n lab-01-02
kubectl get pods -n lab-01-02
make lab-up LAB=01.02
make lab-test LAB=01.02
```

Por que o Deployment da aula seguinte responde de forma diferente?

## Fase 3 — Diagnosticar

```bash
kubectl get events -n lab-01-02 --sort-by=.lastTimestamp
kubectl get all -n lab-01-02
```

Investigue com `kubectl describe` e, quando houver Pod, `kubectl logs`. Compare estado desejado, readiness e eventos. `make lab-test` valida checks básicos, não substitui sua investigação.

## Fase 4 — Limpar com segurança

```bash
make lab-down LAB=01.02
make lab-status LAB=01.02
```

O namespace é preservado por segurança. Não use `make down` para limpar um único lab.

## Critérios de conclusão

- [ ] Expliquei a função dos objetos do manifesto.
- [ ] Executei a observação antes e depois do experimento.
- [ ] Comparei hipótese e resultado e identifiquei evidências.
- [ ] Removi os recursos do lab sem apagar o cluster.
