# Lab 01.12 — Estratégias de Deployment

[← Aula 01.12](../../estrategias-deployment/README.md) · [↑ Camada 01](../../README.md) · [🧪 Índice dos labs](../../../../docs/labs.md)

> **MODO DESAFIO:** execute `make lab-prepare LAB=01.12`, complete `.labs/01.12/resources.yaml` e execute **`kubectl apply -f .labs/01.12/`**. Só depois valide com `make lab-test LAB=01.12`. `make lab-up` aplica a solução completa e fica reservado à CI; `make lab-solution LAB=01.12` revela seus arquivos para estudo posterior.


## Objetivo e hipótese

RollingUpdate cria nova revisão de Pod template; rollback recupera uma revisão anterior. Se a imagem mudar, a disponibilidade depende de readiness e capacidade.

**Escopo:** cluster Kind `dev` e namespace `lab-01-12`.

## Desafio — o que você vai construir

Crie o Deployment `web` com **3 réplicas** de nginx, `RollingUpdate`, `maxSurge: 1` e `maxUnavailable: 0`; configure selector/labels, recursos e readiness HTTP. Depois execute um rollout de nova revisão e retorne à versão anterior.

**Antes de aplicar:** confirme os pré-requisitos, complete o YAML em `.labs/01.12/` e faça uma hipótese sobre o resultado. Recorra a `kubectl explain` ou às referências abaixo; não copie a solução antes de tentar.

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

## Resultado esperado e evidências

- O Deployment inicial fica disponível com 3 Pods; `kubectl rollout history` lista a revisão inicial.
- Ao reiniciar ou mudar a imagem, aparece novo ReplicaSet/revisão; durante um RollingUpdate saudável, os limites de `maxSurge`/`maxUnavailable` controlam a transição.
- `kubectl rollout undo` restaura a revisão anterior. Se a imagem não puder ser baixada, o status mostra falha de pull e o rollback é o caminho de recuperação.

**Se o resultado divergir:** investigue `describe`, eventos e componentes de suporte. Um check que aprova o manifesto não substitui a observação funcional.

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

## Critérios de conclusão

- [ ] Configurei a estratégia RollingUpdate e seus limites.
- [ ] Observei ao menos duas revisões do Deployment no histórico.
- [ ] Executei uma atualização, acompanhei a disponibilidade e fiz rollback.
- [ ] Conferi a versão final e removi os recursos do lab.

## Aprofunde seus conhecimentos

[Estratégia de Deployment](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/#strategy) · [Atualizar Deployment](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/#updating-a-deployment) · [Reverter Deployment](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/#rolling-back-a-deployment).

Volte à [aula teórica](../../estrategias-deployment/README.md) e relacione os mecanismos com os eventos e estados vistos no Kind.

---

[← Lab 01.11](../volumes-basico/README.md) · [↑ Aula 01.12](../../estrategias-deployment/README.md) · [Próximo: Lab 01.13 →](../ingress-basico/README.md)
