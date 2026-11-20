# Lab 02.09 — PriorityClass sem preempção

[← Aula 02.09](../../priorityclass-preemption/README.md) · [↑ Camada 02](../../README.md) · [🧪 Índice dos labs](../../../../docs/labs.md)

> **MODO DESAFIO:** `make lab-prepare LAB=02.09` cria o namespace e copia o starter **incompleto** em `.labs/02.09/resources.yaml`. Complete-o, execute `make lab-apply LAB=02.09`, depois `make lab-test LAB=02.09` e `make lab-observe LAB=02.09`. **`make lab-up` aplica a solução e é exclusivo da CI.**

## Objetivo e hipótese

Criar uma PriorityClass de baixo valor sem preempção e observar sua associação a um Pod.

**Pré-requisitos:** Kind `dev`, contexto `kind-dev`, `kubectl` e `make`; namespace exclusivo `lab-02-09`. **Atenção:** PriorityClass tem escopo do cluster. Confirme Kind descartável e não use esse nome em ambientes compartilhados.

## Desafio — o que você vai construir

Crie PriorityClass `lab-02-priority` com valor 1000, `globalDefault: false`, `preemptionPolicy: Never`, e Pod `prioritario` que referencia a classe. O Pod deve executar BusyBox com sleep.

**Segurança de escopo global:** no YAML da PriorityClass, declare `metadata.annotations.learning-path.example/lab-id: "02.09"`. O motor verifica se já existe uma PriorityClass com o mesmo nome antes de aplicar ou excluir; se pertencer a outro uso, interrompe a operação sem sobrescrever.

Preveja o que deve acontecer antes de abrir `solution/`. Use `kubectl explain` e a aula para esclarecer a API.

## Fase 1 — Preparar e prever

```bash
kubectl config current-context
make lab-prepare LAB=02.09
cat .labs/02.09/resources.yaml
```

**Por segurança, use `make lab-apply LAB=02.09` no lugar de `kubectl apply` direto. O comando verifica propriedade e escopo da definição global antes da aplicação.**

## Fase 2 — Aplicar e observar

Complete os TODOs e execute:

```bash
make lab-apply LAB=02.09
make lab-test LAB=02.09
make lab-observe LAB=02.09
```

Execute `kubectl get priorityclass lab-02-priority` e `kubectl get pod prioritario -n lab-02-09 -o yaml`; confira `spec.priorityClassName` e a prioridade efetiva.

## Fase 3 — Experimento controlado

Compare a prioridade do Pod principal com a de um Pod temporário sem PriorityClass, sem gerar pressão de recursos:

```bash
kubectl run sem-classe -n lab-02-09 --image=busybox:1.36 --restart=Never -- sleep 3600
kubectl get pod prioritario sem-classe -n lab-02-09 -o custom-columns=NAME:.metadata.name,CLASS:.spec.priorityClassName,PRIORIDADE:.spec.priority
kubectl get priorityclass lab-02-priority -o yaml
kubectl delete pod sem-classe -n lab-02-09 --ignore-not-found
```

**Conclusão:** valores diferentes de prioridade são observáveis mesmo sem executar preempção. A ausência de preempção neste ambiente **não valida** a política sob saturação.

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

- [ ] **Evidência funcional do Lab 02.09:** priorityClassName alterou a prioridade efetiva comparada ao Pod temporário sem classe, sem causar preempção.
- [ ] Completei o YAML sem copiar a solução e validei o contexto `kind-dev`.
- [ ] Observei a condição específica descrita no resultado esperado.
- [ ] Registrei a hipótese inicial, evidências e explicação técnica.
- [ ] Fiz a limpeza e desmanchei todas as alterações manuais.

## Perguntas de diagnóstico e reflexão

- Qual diferença existe entre prioridade de agendamento e preempção?
- Por que `globalDefault: false` é importante para este lab?

- Por que `preemptionPolicy: Never` não remove a prioridade de fila?

## Aprofunde seus conhecimentos

[Documentação Kubernetes](https://kubernetes.io/docs/concepts/scheduling-eviction/pod-priority-preemption/) · [Aula 02.09](../../priorityclass-preemption/README.md)

---

[← Lab 02.08](../topology-spread-basico/README.md) · [↑ Aula 02.09](../../priorityclass-preemption/README.md) · [↑ Camada 02](../../README.md) · [Próximo: Lab 02.10 →](../qos-eviction-basico/README.md)
