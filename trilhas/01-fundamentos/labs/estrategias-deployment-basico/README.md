# Lab 01.12 — Deployment: rollout e rollback

[← Camada 01](../../README.md) · [Guia de labs](../../../../docs/labs.md)

## Objetivo e hipótese

RollingUpdate cria nova revisão de Pod template; rollback recupera uma revisão anterior. Se a imagem mudar, a disponibilidade depende de readiness e capacidade.

**Escopo:** cluster Kind `dev` e namespace `lab-01-12`.

## Fase 1 — Preparar e prever

```bash
kubectl config current-context
kubectl get nodes
cat trilhas/01-fundamentos/labs/estrategias-deployment-basico/resources.yaml
```

Preveja o comportamento dos controladores e componentes envolvidos.

## Fase 2 — Aplicar e testar

```bash
make lab-up LAB=01.12
make lab-test LAB=01.12
make lab-observe LAB=01.12
```

**Observe revisão e estratégia:**

```bash
kubectl rollout history deployment/web -n lab-01-12
kubectl get deployment,replicaset,pods -n lab-01-12 -w
```

**Experimento — rollout controlado:** interrompa o watch com Ctrl+C e, em outro terminal, execute:

```bash
make lab-experiment LAB=01.12 EXPERIMENT=controlled-rollout
kubectl rollout history deployment/web -n lab-01-12
kubectl get replicasets -n lab-01-12
```

**Experimento — revisão de imagem e rollback:**

```bash
kubectl set image deployment/web -n lab-01-12 nginx=nginx:1.27-alpine
kubectl rollout status deployment/web -n lab-01-12 --timeout=120s
kubectl rollout history deployment/web -n lab-01-12
kubectl rollout undo deployment/web -n lab-01-12
kubectl rollout status deployment/web -n lab-01-12 --timeout=120s
```

Se a imagem não estiver acessível, diagnostique ImagePullBackOff e reverta com `rollout undo`. Compare `maxSurge` e `maxUnavailable` com as transições observadas.

## Fase 3 — Diagnosticar

```bash
kubectl get events -n lab-01-12 --sort-by=.lastTimestamp
kubectl get all -n lab-01-12
```

Observe eventos, `spec` e `status`; anote evidências do experimento. O check automático não é uma prova de comportamento de ponta a ponta.

## Fase 4 — Limpar

```bash
make lab-down LAB=01.12
make lab-status LAB=01.12
```

O namespace é preservado; não utilize `make down` para limpar um único exercício.

## Checklist

- [ ] Expliquei os objetos do manifesto.
- [ ] Comparei hipótese com observação real.
- [ ] Investiguei eventos e condições relevantes.
- [ ] Limpei os recursos do exercício.
