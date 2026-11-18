# Lab 01.03 — Deployments: replicas e self-healing

> **MODO DESAFIO — o aluno constrói:** `make lab-prepare LAB=01.03` cria apenas o namespace e copia um YAML incompleto para `.labs/01.03/`. **Complete o arquivo usando o objetivo abaixo**, aplique você mesmo com `kubectl apply -f .labs/01.03/` e só então execute `make lab-test LAB=01.03`. O comando `make lab-up` é reservado à CI. `make lab-solution LAB=01.03` mostra o caminho da referência quando você quiser conferir.

[← Camada 01](../../README.md) · [Guia de labs](../../../../docs/labs.md)

## Objetivo e hipótese

O Deployment controla um ReplicaSet, que mantém a quantidade declarada de Pods. Hipótese: excluir uma réplica resulta na criação de outra?

**Ambiente:** cluster Kind `dev`, namespace isolado `lab-01-03`. Leia primeiro a aula teórica correspondente. Os experimentos são locais e manuais para você observar cada transição.

## Fase 1 — Preparar e inspecionar

```bash
make doctor
kubectl config current-context
kubectl get nodes
make lab-prepare LAB=01.03
cat .labs/01.03/resources.yaml
```

Antes de aplicar, preveja quais objetos serão criados e quais controladores participarão.

## Fase 2 — Aplicar e observar

```bash
make lab-prepare LAB=01.03
# Complete primeiro o arquivo em .labs/01.03/
kubectl apply -f .labs/01.03/
make lab-test LAB=01.03
make lab-observe LAB=01.03
```

**Observe a cadeia Deployment → ReplicaSet → Pods:**

```bash
kubectl get deployment,replicaset,pods -n lab-01-03 -o wide
kubectl describe deployment web -n lab-01-03
```

**Experimento — recuperar uma réplica:** em outro terminal, execute `kubectl get pods -n lab-01-03 -w`. Depois exclua somente o primeiro Pod retornado:

```bash
POD=$(kubectl get pods -n lab-01-03 -l app=web-0103 -o jsonpath='{.items[0].metadata.name}')
kubectl delete pod "$POD" -n lab-01-03
kubectl rollout status deployment/web -n lab-01-03
kubectl get pods,replicasets -n lab-01-03
```

Compare com o Pod isolado do lab 01.02. Para observar escalabilidade, execute `kubectl scale deployment/web -n lab-01-03 --replicas=2`; depois reaplique `resources.yaml` e confirme o estado desejado.

## Fase 3 — Diagnosticar

```bash
kubectl get events -n lab-01-03 --sort-by=.lastTimestamp
kubectl get all -n lab-01-03
```

Investigue com `kubectl describe` e, quando houver Pod, `kubectl logs`. Compare estado desejado, readiness e eventos. `make lab-test` valida checks básicos, não substitui sua investigação.

## Fase 4 — Limpar com segurança

```bash
make lab-down LAB=01.03
make lab-status LAB=01.03
```

O namespace é preservado por segurança. Não use `make down` para limpar um único lab.

## Critérios de conclusão

- [ ] Expliquei a função dos objetos do manifesto.
- [ ] Executei a observação antes e depois do experimento.
- [ ] Comparei hipótese e resultado e identifiquei evidências.
- [ ] Removi os recursos do lab sem apagar o cluster.
