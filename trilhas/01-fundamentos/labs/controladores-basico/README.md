# Lab 01.04 — Controladores

[← Aula 01.04](../../controladores/README.md) · [↑ Camada 01](../../README.md) · [🧪 Índice dos labs](../../../../docs/labs.md)
> **MODO DESAFIO:** execute `make lab-prepare LAB=01.04` para preparar o namespace e criar o arquivo `.labs/01.04/resources.yaml`. Complete o YAML com base no objetivo desta aula. Execute `kubectl apply -f .labs/01.04/` e depois `make lab-test LAB=01.04`. **`make lab-up` é exclusivo da CI** e aplica a solução, portanto não é o fluxo do aluno. `make lab-solution LAB=01.04` mostra onde consultar a referência.


## Objetivo e hipótese

Compare três padrões de gerenciamento de Pods: réplicas intercambiáveis, um Pod por nó elegível e identidade estável.

**Pré-requisitos:** Kind `dev` ativo, `kubectl`, `make`; namespace exclusivo `lab-01-04`.

## Fase 1 — Inspecionar o que será aplicado

```bash
kubectl config current-context
kubectl get nodes
make lab-prepare LAB=01.04
cat .labs/01.04/resources.yaml
```

Antes de executar, anote quais objetos e controladores devem aparecer.

## Fase 2 — Aplicar e validar

```bash
make lab-prepare LAB=01.04
# Complete os campos TODO do arquivo local
kubectl apply -f .labs/01.04/
make lab-test LAB=01.04
make lab-observe LAB=01.04
```

**Compare os controladores:**

```bash
kubectl get daemonset,statefulset,replicaset,pods -n lab-01-04 -o wide
kubectl rollout status statefulset/stateful-demo -n lab-01-04 --timeout=180s
kubectl get pods -n lab-01-04 --show-labels
```

**Experimento — identidade vs distribuição:** observe os nomes ordenados `stateful-demo-0`, `stateful-demo-1` e os nós que receberam o DaemonSet. Exclua `stateful-demo-0` e observe seu retorno com o **mesmo nome**, mas com outro UID:

```bash
kubectl get pod stateful-demo-0 -n lab-01-04 -o jsonpath='{.metadata.uid}{"\n"}'
kubectl delete pod stateful-demo-0 -n lab-01-04
kubectl rollout status statefulset/stateful-demo -n lab-01-04 --timeout=180s
kubectl get pod stateful-demo-0 -n lab-01-04 -o jsonpath='{.metadata.uid}{"\n"}'
```

O DaemonSet pode executar em apenas parte dos nós se houver taints e restrições. O ReplicaSet é visto no laboratório 01.03, sob controle de um Deployment.

## Fase 3 — Diagnóstico

```bash
kubectl get events -n lab-01-04 --sort-by=.lastTimestamp
kubectl get all -n lab-01-04
```

Compare `spec` e `status`, consulte `describe` e explique qualquer divergência. Os checks automáticos cobrem condições básicas, não o raciocínio do experimento.

## Fase 4 — Limpeza

```bash
make lab-down LAB=01.04
make lab-status LAB=01.04
```

O namespace é preservado. Não use `make down` para excluir um único lab.

## Checklist

- [ ] Previ os recursos criados e conferi o resultado.
- [ ] Executei e expliquei o experimento.
- [ ] Investiguei eventos e condições.
- [ ] Limpei os recursos sem afetar outros labs.

---

[← Lab 01.03](../deployments-basico/README.md) · [↑ Aula 01.04](../../controladores/README.md) · [Próximo: Lab 01.05 →](../services-basico/README.md)
