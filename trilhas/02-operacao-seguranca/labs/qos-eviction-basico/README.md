# Lab 02.10 — QoS Classes e Eviction

[← Aula 02.10](../../qos-eviction/README.md) · [↑ Camada 02](../../README.md) · [🧪 Índice dos labs](../../../../docs/labs.md)

> **MODO DESAFIO:** `make lab-prepare LAB=02.10` cria o namespace e copia o starter **incompleto** em `.labs/02.10/resources.yaml`. Complete-o, execute `kubectl apply -f .labs/02.10/`, depois `make lab-test LAB=02.10` e `make lab-observe LAB=02.10`. **`make lab-up` aplica a solução e é exclusivo da CI.**

## Objetivo e hipótese

Produzir e comparar um Pod BestEffort, Burstable e Guaranteed sem provocar pressão artificial nos nós.

**Pré-requisitos:** Kind `dev`, contexto `kind-dev`, `kubectl` e `make`; namespace exclusivo `lab-02-10`. 

## Desafio — o que você vai construir

Crie três Pods BusyBox: `sem-recursos` sem requests/limits; `variavel` com request CPU menor que limit; `garantido` com requests iguais a limits de CPU e memória.

Preveja o que deve acontecer antes de abrir `solution/`. Use `kubectl explain` e a aula para esclarecer a API.

## Fase 1 — Preparar e prever

```bash
kubectl config current-context
make lab-prepare LAB=02.10
cat .labs/02.10/resources.yaml
```

## Fase 2 — Aplicar e observar

Complete os TODOs e execute:

```bash
kubectl apply -f .labs/02.10/
make lab-test LAB=02.10
make lab-observe LAB=02.10
```

`kubectl get pods -n lab-02-10 -o custom-columns=NAME:.metadata.name,QOS:.status.qosClass` deve mostrar as três classes, após admitidos os Pods.

## Fase 3 — Experimento controlado

Além dos três perfis iniciais, crie um quarto Pod temporário com **request e limit iguais apenas para CPU, sem definição de memória**. Antes de aplicar, preveja a QoS; depois compare a classe calculada:

```bash
kubectl apply -f trilhas/02-operacao-seguranca/labs/qos-eviction-basico/experiments/qos-parcial.yaml
kubectl get pods -n lab-02-10 -o custom-columns=NAME:.metadata.name,QOS:.status.qosClass
kubectl get pod qos-parcial -n lab-02-10 -o yaml
kubectl delete -f trilhas/02-operacao-seguranca/labs/qos-eviction-basico/experiments/qos-parcial.yaml --ignore-not-found
```

**Resultado:** `qos-parcial` deve ser **Burstable**, porque a categoria Guaranteed exige requests=limits para **CPU e memória**. Não provoque eviction ou OOM no cluster. Confirme via `kubectl describe node dev-worker` que pressão de nó é um fenômeno distinto.

## Resultado esperado e evidências

`sem-recursos` = BestEffort, `variavel` = Burstable e `garantido` = Guaranteed. Não é obrigatório provocar uma eviction real.

**Evidências específicas:** registre recursos declarados de cada Pod e o status QoS observado; diferencie a classificação de um evento real de eviction.

## Fase 4 — Diagnosticar

Se a classificação for inesperada, inspecione os resources efetivamente admitidos, LimitRanges do namespace e status dos containers.

Quando a observação não corresponder à hipótese, compare contexto, objetos, eventos e condições antes de modificar os manifests.

## Fase 5 — Limpar com segurança

```bash
make lab-down LAB=02.10
make lab-status LAB=02.10
```

O namespace é preservado; desfaça **separadamente** alterações manuais de nó, policies, Pods temporários e outros recursos criados fora do contrato. Não execute `make down`.

## Critérios de conclusão

- [ ] **Evidência funcional do Lab 02.10:** as classes QoS foram identificadas e o perfil parcial permaneceu Burstable sem gerar pressão artificial no nó.
- [ ] Completei o YAML sem copiar a solução e validei o contexto `kind-dev`.
- [ ] Observei a condição específica descrita no resultado esperado.
- [ ] Registrei a hipótese inicial, evidências e explicação técnica.
- [ ] Fiz a limpeza e desmanchei todas as alterações manuais.

## Perguntas de diagnóstico e reflexão

- O que diferencia Guaranteed de Burstable?
- Por que OOMKilled não é sinônimo de Pod Evicted?

- Como você distinguiria `Evicted` de `OOMKilled`?

## Aprofunde seus conhecimentos

[Documentação Kubernetes](https://kubernetes.io/docs/concepts/workloads/pods/pod-qos/) · [Aula 02.10](../../qos-eviction/README.md)

---

[← Lab 02.09](../priorityclass-basico/README.md) · [↑ Aula 02.10](../../qos-eviction/README.md) · [↑ Camada 02](../../README.md) · [Próximo: Lab 02.11 →](../pdb-basico/README.md)
