# Lab 01.12 — Estratégias de Deployment

[← Aula 01.12](../../estrategias-deployment/README.md) · [↑ Camada 01](../../README.md) · [🧪 Índice dos labs](../../../../docs/labs.md)

> **MODO DESAFIO:** execute `make lab-prepare LAB=01.12`, complete `.labs/01.12/resources.yaml` e execute **`kubectl apply -f .labs/01.12/`**. Só depois valide com `make lab-test LAB=01.12`. `make lab-up` aplica a solução completa e fica reservado à CI; `make lab-solution LAB=01.12` revela seus arquivos para estudo posterior.


## Objetivo e hipótese

RollingUpdate cria nova revisão de Pod template; rollback recupera uma revisão anterior. Se a imagem mudar, a disponibilidade depende de readiness e capacidade.

**Escopo:** cluster Kind `dev` e namespace `lab-01-12`.

## Fase 1 — Preparar e prever

```bash
kubectl config current-context
kubectl get nodes
make lab-prepare LAB=01.12
cat .labs/01.12/resources.yaml
```

Preveja o comportamento dos controladores e componentes envolvidos.

## Fase 2 — Aplicar e testar

```bash
make lab-prepare LAB=01.12
# Preencha os arquivos de trabalho
kubectl apply -f .labs/01.12/
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

---

[← Lab 01.11](../volumes-basico/README.md) · [↑ Aula 01.12](../../estrategias-deployment/README.md) · [Próximo: Lab 01.13 →](../ingress-basico/README.md)
