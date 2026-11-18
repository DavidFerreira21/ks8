# Lab 02.07 — Taints, Tolerations e Node Affinity

[← Aula 02.07](../../taints-tolerations-affinity/README.md) · [↑ Camada 02](../../README.md) · [🧪 Índice dos labs](../../../../docs/labs.md)

> **MODO DESAFIO:** `make lab-prepare LAB=02.07` cria o namespace e copia o starter **incompleto** em `.labs/02.07/resources.yaml`. Complete-o, execute `kubectl apply -f .labs/02.07/`, depois `make lab-test LAB=02.07` e `make lab-observe LAB=02.07`. **`make lab-up` aplica a solução e é exclusivo da CI.**

## Objetivo e hipótese

Aplicar node affinity em um Pod e verificar o agendamento sobre um worker específico do Kind.

**Pré-requisitos:** Kind `dev`, contexto `kind-dev`, `kubectl` e `make`; namespace exclusivo `lab-02-07`. O laboratório depende de um Kind denominado `dev` com worker `dev-worker`, como no `kind-config.yaml` do projeto.

## Desafio — o que você vai construir

Escreva um Pod `afinidade` com BusyBox e `nodeAffinity.requiredDuringSchedulingIgnoredDuringExecution`, exigindo `kubernetes.io/hostname In [dev-worker]`. O Pod deve permanecer ativo.

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

**Sem modificar os nós**, consulte com `kubectl describe pod afinidade -n lab-02-07` as restrições efetivas. Discuta: se o worker não existir, o Pod permanece Pending. Para observar taints existentes, use `kubectl describe node dev-worker` e identifique `Taints`.

## Resultado esperado e evidências

O Pod é agendado em `dev-worker` se ele estiver Ready e tiver capacidade. Affinity exigida não é substituída por tolerations.

**Evidências específicas:** registre labels dos nós, nodeAffinity do Pod, valor de `spec.nodeName` e eventuais `FailedScheduling` se a restrição não for atendida.

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

- [ ] Completei o YAML sem copiar a solução e validei o contexto `kind-dev`.
- [ ] Observei a condição específica descrita no resultado esperado.
- [ ] Registrei a hipótese inicial, evidências e explicação técnica.
- [ ] Fiz a limpeza e desmanchei todas as alterações manuais.

## Perguntas de diagnóstico e reflexão

- Por que toleration não escolheria esse mesmo nó por si só?
- O que o scheduler faz se `dev-worker` estiver indisponível?

## Aprofunde seus conhecimentos

[Documentação Kubernetes](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/) · [Aula 02.07](../../taints-tolerations-affinity/README.md)

---

[← Lab 02.06](../jobs-cronjobs-basico/README.md) · [↑ Camada 02](../../README.md) · [Próximo: Lab 02.08 →](../topology-spread-basico/README.md)
