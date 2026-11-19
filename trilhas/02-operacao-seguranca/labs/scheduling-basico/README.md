# Lab 02.07 — Taints, Tolerations e Node Affinity

[← Aula 02.07](../../taints-tolerations-affinity/README.md) · [↑ Camada 02](../../README.md) · [🧪 Índice dos labs](../../../../docs/labs.md)

> **MODO DESAFIO:** `make lab-prepare LAB=02.07` cria o namespace e copia o starter **incompleto** em `.labs/02.07/resources.yaml`. Complete-o, execute `kubectl apply -f .labs/02.07/`, depois `make lab-test LAB=02.07` e `make lab-observe LAB=02.07`. **`make lab-up` aplica a solução e é exclusivo da CI.**

## Objetivo e hipótese

Demonstrar node affinity, o efeito de um taint NoSchedule e o papel de uma toleration para admitir o Pod no worker escolhido.

**Pré-requisitos:** Kind `dev`, contexto `kind-dev`, `kubectl` e `make`; namespace exclusivo `lab-02-07`. O laboratório depende de um Kind denominado `dev` com worker `dev-worker`, como no `kind-config.yaml` do projeto.

## Desafio — o que você vai construir

Escreva um Pod `afinidade` com BusyBox e `nodeAffinity.requiredDuringSchedulingIgnoredDuringExecution`, exigindo `kubernetes.io/hostname In [dev-worker]`. Acrescente uma toleration para `estudo=true:NoSchedule`; o Pod deve permanecer ativo.

Preveja o que deve acontecer antes de abrir `solution/`. Use `kubectl explain` e a aula para esclarecer a API.

## Fase 1 — Preparar e prever

```bash
kubectl config current-context
make lab-prepare LAB=02.07
cat .labs/02.07/resources.yaml
```

## Fase 2 — Aplicar e observar

Complete os TODOs e execute:

```bash
kubectl apply -f .labs/02.07/
make lab-test LAB=02.07
make lab-observe LAB=02.07
```

Confira `kubectl get nodes -L kubernetes.io/hostname` e `kubectl get pods -n lab-02-07 -o wide`. O Pod deve indicar o nó `dev-worker`.

## Fase 3 — Experimento controlado

**Somente no Kind descartável:** marque temporariamente `dev-worker` com um taint e recrie o Pod tolerante. Depois crie outro Pod sem toleration, exigindo o mesmo worker, para observar `FailedScheduling`.

```bash
kubectl taint node dev-worker estudo=true:NoSchedule
kubectl delete pod afinidade -n lab-02-07
kubectl apply -f .labs/02.07/resources.yaml
kubectl get pod afinidade -n lab-02-07 -o wide
kubectl run sem-toleration -n lab-02-07 --image=busybox:1.36 --restart=Never --overrides='{"spec":{"nodeSelector":{"kubernetes.io/hostname":"dev-worker"}}}' -- sleep 3600
kubectl describe pod sem-toleration -n lab-02-07
```

O Pod com toleration pode executar em `dev-worker`; o Pod sem toleration deve ficar Pending por taint não tolerado. **Reverta obrigatoriamente** — inclusive após uma falha:

```bash
kubectl delete pod sem-toleration -n lab-02-07 --ignore-not-found
kubectl taint node dev-worker estudo=true:NoSchedule-
```

Não avance para outro lab enquanto o taint de teste permanecer no nó.

## Resultado esperado e evidências

Com worker Ready e capacidade suficiente, o Pod tolerante agenda em `dev-worker` mesmo sob taint; o Pod sem toleration recebe `FailedScheduling`. Affinity seleciona o nó, toleration remove uma restrição, mas não define destino.

**Evidências específicas:** registre affinity e toleration no YAML, taint temporário, `spec.nodeName` do Pod tolerante, evento `FailedScheduling` do Pod sem toleration e a reversão do taint.

## Fase 4 — Diagnosticar

`kubectl describe pod afinidade -n lab-02-07` e `kubectl describe node dev-worker`; diferencie capacidade insuficiente de falta de label correspondente.

Quando a observação não corresponder à hipótese, compare contexto, objetos, eventos e condições antes de modificar os manifests.

## Fase 5 — Limpar com segurança

```bash
make lab-down LAB=02.07
make lab-status LAB=02.07
```

O namespace é preservado; desfaça **separadamente** alterações manuais de nó, policies, Pods temporários e outros recursos criados fora do contrato. Não execute `make down`.

## Critérios de conclusão

- [ ] **Evidência funcional do Lab 02.07:** um Pod tolerou o taint temporário, outro ficou Pending, e o worker voltou ao estado original.
- [ ] Completei o YAML sem copiar a solução e validei o contexto `kind-dev`.
- [ ] Observei a condição específica descrita no resultado esperado.
- [ ] Registrei a hipótese inicial, evidências e explicação técnica.
- [ ] Fiz a limpeza e desmanchei todas as alterações manuais.

## Perguntas de diagnóstico e reflexão

- Por que toleration não escolheria esse mesmo nó por si só?
- O que o scheduler faz se `dev-worker` estiver indisponível?

- Por que nodeAffinity e toleration precisam ser avaliadas juntas?

## Aprofunde seus conhecimentos

[Documentação Kubernetes](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/) · [Aula 02.07](../../taints-tolerations-affinity/README.md)

---

[← Lab 02.06](../jobs-cronjobs-basico/README.md) · [↑ Aula 02.07](../../taints-tolerations-affinity/README.md) · [↑ Camada 02](../../README.md) · [Próximo: Lab 02.08 →](../topology-spread-basico/README.md)
