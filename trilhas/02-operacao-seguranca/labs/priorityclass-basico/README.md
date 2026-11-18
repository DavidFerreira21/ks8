# Lab 02.09 — PriorityClass sem preempção

[← Aula 02.09](../../priorityclass-preemption/README.md) · [↑ Camada 02](../../README.md) · [🧪 Índice dos labs](../../../../docs/labs.md)

> **MODO DESAFIO:** `make lab-prepare LAB=02.09` cria o namespace e copia o starter **incompleto** em `.labs/02.09/resources.yaml`. Complete-o, execute `kubectl apply -f .labs/02.09/`, depois `make lab-test LAB=02.09` e `make lab-observe LAB=02.09`. **`make lab-up` aplica a solução e é exclusivo da CI.**

## Objetivo e hipótese

Criar uma PriorityClass de baixo valor sem preempção e observar sua associação a um Pod.

**Pré-requisitos:** Kind `dev`, contexto `kind-dev`, `kubectl` e `make`; namespace exclusivo `lab-02-09`. **Atenção:** PriorityClass tem escopo do cluster. Confirme Kind descartável e não use esse nome em ambientes compartilhados.

## Desafio — o que você vai construir

Crie PriorityClass `lab-02-priority` com valor 1000, `globalDefault: false`, `preemptionPolicy: Never`, e Pod `prioritario` que referencia a classe. O Pod deve executar BusyBox com sleep.

Preveja o que deve acontecer antes de abrir `solution/`. Use `kubectl explain` e a aula para esclarecer a API.

## Fase 1 — Preparar e prever

```bash
kubectl config current-context
make lab-prepare LAB=02.09
cat .labs/02.09/resources.yaml
```

## Fase 2 — Aplicar e observar

Complete os TODOs e execute:

```bash
kubectl apply -f .labs/02.09/
make lab-test LAB=02.09
make lab-observe LAB=02.09
```

Execute `kubectl get priorityclass lab-02-priority` e `kubectl get pod prioritario -n lab-02-09 -o yaml`; confira `spec.priorityClassName` e a prioridade efetiva.

## Fase 3 — Experimento controlado

Compare `kubectl get priorityclass lab-02-priority -o yaml` com `kubectl describe pod prioritario -n lab-02-09`. **Não gere pressão de CPU e não provoque preempção real**; o objetivo é diferenciar prioridade de preempção.

## Resultado esperado e evidências

PriorityClass é recurso **de escopo de cluster**. O Pod referencia a classe e a política `Never` evita que ele inicie preempção de outros Pods.

**Evidências específicas:** registre PriorityClass, valor/prioridade do Pod e `preemptionPolicy`; explique por que isso não prova comportamento sob saturação.

## Fase 4 — Diagnosticar

Se a classe estiver ausente, verifique o nome exato antes de criar o Pod. Se a execução falhar, inspecione eventos e recursos.

Quando a observação não corresponder à hipótese, compare contexto, objetos, eventos e condições antes de modificar os manifests.

## Fase 5 — Limpar com segurança

```bash
make lab-down LAB=02.09
make lab-status LAB=02.09
```

O namespace é preservado; desfaça **separadamente** alterações manuais de nó, policies, Pods temporários e outros recursos criados fora do contrato. Não execute `make down`.

## Critérios de conclusão

- [ ] Completei o YAML sem copiar a solução e validei o contexto `kind-dev`.
- [ ] Observei a condição específica descrita no resultado esperado.
- [ ] Registrei a hipótese inicial, evidências e explicação técnica.
- [ ] Fiz a limpeza e desmanchei todas as alterações manuais.

## Perguntas de diagnóstico e reflexão

- Qual diferença existe entre prioridade de agendamento e preempção?
- Por que `globalDefault: false` é importante para este lab?

## Aprofunde seus conhecimentos

[Documentação Kubernetes](https://kubernetes.io/docs/concepts/scheduling-eviction/pod-priority-preemption/) · [Aula 02.09](../../priorityclass-preemption/README.md)

---

[← Lab 02.08](../topology-spread-basico/README.md) · [↑ Camada 02](../../README.md) · [Próximo: Lab 02.10 →](../qos-eviction-basico/README.md)
