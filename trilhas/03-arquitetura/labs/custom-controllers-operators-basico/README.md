# Lab 03.07 — Custom Controllers e Operators

[← Aula 03.07](../../custom-controllers-operators/README.md) · [↑ Camada 03](../../README.md) · [🧪 Índice dos labs](../../../../docs/labs.md)

> **MODO DESAFIO:** execute `make lab-prepare LAB=03.07`, complete `.labs/03.07/resources.yaml`, aplique com `kubectl apply -f .labs/03.07/` e só então use `make lab-test LAB=03.07`. O comando `make lab-up` usa a solução de referência e fica reservado à CI.

## Objetivo e hipótese

Observar reconciliação nativa e distinguir esse sinal de implementação de um Operator próprio.

**Pré-requisitos:** cluster Kind `dev`, contexto `kind-dev`, `kubectl` e `make`. Namespace de estudo `lab-03-07`. **Analogia intencional:** o lab exercita um controlador nativo; não afirma criar Operator personalizado.

## Desafio — o que você vai construir

Defina Deployment `operator-demo` com duas réplicas, label `app: operator-demo` e container nginx.

**Antes de começar:** escreva sua hipótese para cada etapa. A solução em `solution/` existe para conferência posterior, não para ser copiada.

## Fase 1 — Preparar e prever

```bash
kubectl config current-context
make lab-prepare LAB=03.07
cat .labs/03.07/resources.yaml
```

Verifique se o namespace foi criado, sem aplicar a solução.

## Fase 2 — Aplicar e observar

Complete todos os TODOs no starter e aplique:

```bash
kubectl apply -f .labs/03.07/
make lab-test LAB=03.07
make lab-observe LAB=03.07
```

Inspecione `kubectl get deployment,replicaset,pods -n lab-03-07 -o wide` e ownerReferences do ReplicaSet.

## Fase 3 — Experimento controlado

Escalone temporariamente o Deployment para 3 com `kubectl scale deploy/operator-demo -n lab-03-07 --replicas=3`; observe o novo Pod e restaure `--replicas=2`, verificando status novamente.

## Resultado esperado e evidências

A reconciliação nativa atualiza a quantidade de réplicas, sem instalar um Operator customizado. A observação é uma analogia do mecanismo de reconciliação.

**Evidências específicas:** registre geração observada, ownerReferences e condições antes/durante/depois da escala; destaque o que não foi testado (controller próprio).

## Fase 4 — Diagnosticar

Compare contexto, campos do objeto, condições e eventos. Uma falha de admissão, um erro de scheduling e uma falha de container ocorrem em etapas diferentes; use `kubectl describe` e a documentação para sustentar sua hipótese.

## Fase 5 — Limpar com segurança

```bash
make lab-down LAB=03.07
make lab-status LAB=03.07
```

**Segurança:** o namespace é preservado. Remova recursos temporários que criou fora do contrato; em 03.07 a limpeza não deve afetar outros labs. Não execute `make down`.

## Critérios de conclusão

- [ ] Completei o YAML por conta própria e confirmei `kind-dev`.
- [ ] **Critério exclusivo 03.07:** registre geração observada, ownerReferences e condições antes/durante/depois da escala; destaque o que não foi testado (controller próprio).
- [ ] Registrei hipótese, comparação esperado/observado e explicação causal.
- [ ] Restaurei alterações temporárias e executei a limpeza do lab.

## Perguntas de diagnóstico e reflexão

- Por que um operador é mais do que registrar uma CRD?
- Que sinal prova o vínculo de propriedade entre recursos?
- Por que scale não testa lógica de um Operator customizado?

## Aprofunde seus conhecimentos

[Documentação oficial](https://kubernetes.io/docs/concepts/extend-kubernetes/operator/) · [Aula 03.07](../../custom-controllers-operators/README.md)

---

[← Lab 03.06](../crds-custom-resources-basico/README.md) · [↑ Aula 03.07](../../custom-controllers-operators/README.md) · [↑ Camada 03](../../README.md) · [Próximo: Lab 03.08 →](../kube-scheduler-basico/README.md)
