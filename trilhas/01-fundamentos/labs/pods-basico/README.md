# Lab 01.02 — Pods

[← Aula 01.02](../../pods/README.md) · [↑ Camada 01](../../README.md) · [🧪 Índice dos labs](../../../../docs/labs.md)

> **MODO DESAFIO — o aluno constrói:** `make lab-prepare LAB=01.02` cria apenas o namespace e copia um YAML incompleto para `.labs/01.02/`. **Complete o arquivo usando o objetivo abaixo**, aplique você mesmo com `kubectl apply -f .labs/01.02/` e só então execute `make lab-test LAB=01.02`. O comando `make lab-up` é reservado à CI. `make lab-solution LAB=01.02` mostra o caminho da referência quando você quiser conferir.


## Objetivo e hipótese

Pod é a unidade mínima de execução agendada. Hipótese: se eu excluir um Pod isolado, ele será recriado automaticamente?

**Ambiente:** cluster Kind `dev`, namespace isolado `lab-01-02`. Leia primeiro a aula teórica correspondente. Os experimentos são locais e manuais para você observar cada transição.

## Fase 1 — Preparar e inspecionar

```bash
make doctor
kubectl config current-context
kubectl get nodes
make lab-prepare LAB=01.02
cat .labs/01.02/resources.yaml
```

Antes de aplicar, preveja quais objetos serão criados e quais controladores participarão.

## Fase 2 — Aplicar e observar

```bash
make lab-prepare LAB=01.02
# Complete primeiro o arquivo em .labs/01.02/
kubectl apply -f .labs/01.02/
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
make lab-prepare LAB=01.02
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

---

[← Lab 01.01](../fundamentos-cluster/README.md) · [↑ Aula 01.02](../../pods/README.md) · [Próximo: Lab 01.03 →](../deployments-basico/README.md)
