# Lab 01.09 — Requests e Limits: recursos e scheduler

[← Camada 01](../../README.md) · [Labs](../../../../docs/labs.md)

## Objetivo e hipótese

O Scheduler usa requests para decidir elegibilidade de nós, enquanto limits restringem consumo. Hipótese: um Pod pedindo 1000 CPUs entra em Running?

**Escopo:** cluster Kind `dev`, namespace exclusivo `lab-01-09`.

## Fase 1 — Preparar

```bash
kubectl config current-context
kubectl get nodes
cat trilhas/01-fundamentos/labs/requests-limits-basico/resources.yaml
```

Preveja os objetos criados e seus estados.

## Fase 2 — Executar

```bash
make lab-up LAB=01.09
make lab-test LAB=01.09
make lab-observe LAB=01.09
```

**Observe o orçamento:**

```bash
kubectl describe deployment recursos -n lab-01-09
kubectl describe pod -n lab-01-09 -l app=recursos-demo
kubectl get pod -n lab-01-09 -o wide
kubectl top pod -n lab-01-09  # requer Metrics Server, opcional neste lab
```

**Experimento — Pod impossível de agendar:** crie um Pod temporário solicitando CPU maior que a capacidade de um nó (sem modificar os manifests versionados):

```bash
kubectl run pedido-exagerado -n lab-01-09 --image=busybox:1.36 --overrides='{"spec":{"containers":[{"name":"pedido-exagerado","image":"busybox:1.36","command":["sh","-c","sleep 3600"],"resources":{"requests":{"cpu":"1000","memory":"16Mi"}}}]}}' --restart=Never
kubectl describe pod pedido-exagerado -n lab-01-09
kubectl delete pod pedido-exagerado -n lab-01-09 --ignore-not-found
```

O evento `FailedScheduling` deverá indicar recursos insuficientes; observe que um request não garante consumo real, e limites CPU e memória têm efeitos diferentes.

## Fase 3 — Diagnosticar

```bash
kubectl get events -n lab-01-09 --sort-by=.lastTimestamp
kubectl get all -n lab-01-09
```

Leia `describe`, compare `spec` e `status` e explique eventos. Testes automatizados conferem existência e readiness quando indicado, não o experimento pedagógico.

## Fase 4 — Limpeza

```bash
make lab-down LAB=01.09
make lab-status LAB=01.09
```

Namespace preservado intencionalmente. Nunca apague o cluster inteiro para limpar só um lab.

## Checklist

- [ ] Fiz uma hipótese antes de aplicar.
- [ ] Identifiquei o comportamento do recurso.
- [ ] Executei o experimento e interpretei eventos.
- [ ] Removi os recursos do exercício.
