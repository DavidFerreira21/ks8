# Lab 01.04 — Controladores

[← Aula 01.04](../../controladores/README.md) · [↑ Camada 01](../../README.md) · [🧪 Índice dos labs](../../../../docs/labs.md)

> **MODO DESAFIO:** execute `make lab-prepare LAB=01.04` para preparar o namespace e criar o arquivo `.labs/01.04/resources.yaml`. Complete o YAML com base no objetivo desta aula. Execute `kubectl apply -f .labs/01.04/` e depois `make lab-test LAB=01.04`. **`make lab-up` é exclusivo da CI** e aplica a solução, portanto não é o fluxo do aluno. `make lab-solution LAB=01.04` mostra onde consultar a referência.


## Objetivo e hipótese

Compare três padrões de gerenciamento de Pods: réplicas intercambiáveis, um Pod por nó elegível e identidade estável.

**Pré-requisitos:** Kind `dev` ativo, `kubectl`, `make`; namespace exclusivo `lab-01-04`.

## Desafio — o que você vai construir

No mesmo arquivo, crie um `DaemonSet` chamado `observador` (container BusyBox), um Service **headless** chamado `stateful-headless` (`clusterIP: None`) e um `StatefulSet` chamado `stateful-demo` com 2 réplicas, usando esse Service. As labels e selectors precisam corresponder.

**Antes de aplicar:** tente explicar o comportamento esperado sem consultar `solution/`. Se precisar, use `kubectl explain` ou a documentação abaixo. A solução de referência só deve ser consultada depois da tentativa.

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
# Você já preparou o ambiente na Fase 1; complete agora o YAML local.
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

## Resultado esperado e evidências

- O DaemonSet cria **um Pod por nó elegível**; taints do Control Plane podem reduzir a quantidade esperada (não presuma sempre 3).
- O StatefulSet cria Pods com nomes previsíveis `stateful-demo-0` e `stateful-demo-1`, normalmente de forma ordenada.
- Ao excluir `stateful-demo-0`, seu nome retorna **com outro UID**. Compare isso com os nomes intercambiáveis gerados por ReplicaSets.

**Se o resultado divergir:** consulte `kubectl describe`, `kubectl get events` e os logs quando existirem Pods. Diferencie erro de YAML, problema no cluster e comportamento intencional do experimento.

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

## Critérios de conclusão

- [ ] Distingui o papel de ReplicaSet, DaemonSet e StatefulSet.
- [ ] Expliquei por que o DaemonSet não precisa executar em todos os nós.
- [ ] Observei os nomes estáveis e a troca do UID do StatefulSet.
- [ ] Confirmei a função do Service headless e removi o lab.

## Perguntas de diagnóstico e reflexão

- Como você identificou quais nós são elegíveis para o DaemonSet?
- O que mudou e o que permaneceu após excluir e recriar `stateful-demo-0`?

**Evidências específicas:** registre os nós elegíveis ao DaemonSet e os Pods com seus nós; compare nome e UID de `stateful-demo-0` antes e depois da recriação.

- Por que o StatefulSet preserva a identidade ordinal `stateful-demo-0` mesmo quando seu Pod recebe um UID novo?

## Aprofunde seus conhecimentos

[DaemonSet](https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/) · [StatefulSet](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/) · [ReplicaSet](https://kubernetes.io/docs/concepts/workloads/controllers/replicaset/).

Use essas referências para entender **por que** o Kubernetes se comportou assim; depois compare com a [aula teórica](../../controladores/README.md).

---

[← Lab 01.03](../deployments-basico/README.md) · [↑ Aula 01.04](../../controladores/README.md) · [Próximo: Lab 01.05 →](../services-basico/README.md)
