# Lab 03.08 — kube-scheduler

[← Aula 03.08](../../kube-scheduler/README.md) · [↑ Camada 03](../../README.md) · [🧪 Índice dos labs](../../../../docs/labs.md)

> **MODO DESAFIO:** execute `make lab-prepare LAB=03.08`, complete `.labs/03.08/resources.yaml`, aplique com `kubectl apply -f .labs/03.08/` e só então use `make lab-test LAB=03.08`. O comando `make lab-up` usa a solução de referência e fica reservado à CI.

## Objetivo e hipótese

Comprovar que um nodeSelector impossível gera Pod Pending e eventos de FailedScheduling.

**Pré-requisitos:** cluster Kind `dev`, contexto `kind-dev`, `kubectl` e `make`. Namespace de estudo `lab-03-08`. `make lab-test` verifica apenas existência do Pod, porque **Pending é resultado intencional**.

## Desafio — o que você vai construir

Crie Pod `sem-no` com nodeSelector `estudo: inexistente` e um container BusyBox persistente.

**Antes de começar:** escreva sua hipótese para cada etapa. A solução em `solution/` existe para conferência posterior, não para ser copiada.

## Fase 1 — Preparar e prever

```bash
kubectl config current-context
make lab-prepare LAB=03.08
cat .labs/03.08/resources.yaml
```

Verifique se o namespace foi criado, sem aplicar a solução.

## Fase 2 — Aplicar e observar

Complete todos os TODOs no starter e aplique:

```bash
kubectl apply -f .labs/03.08/
make lab-test LAB=03.08
make lab-observe LAB=03.08
```

O Pod deve existir na API mesmo que não seja Ready. Use `kubectl describe pod sem-no -n lab-03-08` e compare labels dos nós.

## Fase 3 — Experimento controlado

Sem alterar labels dos nós, identifique a condição `PodScheduled` e evento de scheduling. Para recuperar o Pod, apague a instância e reaplique uma cópia local sem o nodeSelector; antes do cleanup restaure e inspecione o YAML original.

## Resultado esperado e evidências

Pod Pending com motivo `Unschedulable` enquanto nenhum nó satisfaz a restrição. Um YAML válido não implica scheduling bem-sucedido.

**Evidências específicas:** capture nodeSelector, labels de Node, fase do Pod e evento FailedScheduling/Unschedulable.

## Fase 4 — Diagnosticar

Compare contexto, campos do objeto, condições e eventos. Uma falha de admissão, um erro de scheduling e uma falha de container ocorrem em etapas diferentes; use `kubectl describe` e a documentação para sustentar sua hipótese.

## Fase 5 — Limpar com segurança

```bash
make lab-down LAB=03.08
make lab-status LAB=03.08
```

**Segurança:** o namespace é preservado. Remova recursos temporários que criou fora do contrato; em 03.08 a limpeza não deve afetar outros labs. Não execute `make down`.

## Critérios de conclusão

- [ ] Completei o YAML por conta própria e confirmei `kind-dev`.
- [ ] **Critério exclusivo 03.08:** capture nodeSelector, labels de Node, fase do Pod e evento FailedScheduling/Unschedulable.
- [ ] Registrei hipótese, comparação esperado/observado e explicação causal.
- [ ] Restaurei alterações temporárias e executei a limpeza do lab.

## Perguntas de diagnóstico e reflexão

- Que campo deixa o Pod inelegível a todos os nós?
- Por que o API Server não rejeita o YAML?
- Como distinguir falta de CPU de selector sem correspondência?

## Aprofunde seus conhecimentos

[Documentação oficial](https://kubernetes.io/docs/concepts/scheduling-eviction/kube-scheduler/) · [Aula 03.08](../../kube-scheduler/README.md)

---

[← Lab 03.07](../custom-controllers-operators-basico/README.md) · [↑ Aula 03.08](../../kube-scheduler/README.md) · [↑ Camada 03](../../README.md) · [Próximo: Lab 03.09 →](../cloud-controller-manager-basico/README.md)
