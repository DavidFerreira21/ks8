# Lab 03.01 — Arquitetura do Cluster

[← Aula 03.01](../../arquitetura-cluster/README.md) · [↑ Camada 03](../../README.md) · [🧪 Índice dos labs](../../../../docs/labs.md)

> **MODO DESAFIO:** execute `make lab-prepare LAB=03.01`, complete `.labs/03.01/resources.yaml`, aplique com `kubectl apply -f .labs/03.01/` e só então use `make lab-test LAB=03.01`. O comando `make lab-up` usa a solução de referência e fica reservado à CI.

## Objetivo e hipótese

Relacionar API Server, controllers, scheduler e workers ao ciclo de criação de um Deployment.

**Pré-requisitos:** cluster Kind `dev`, contexto `kind-dev`, `kubectl` e `make`. Namespace de estudo `lab-03-01`. 

## Desafio — o que você vai construir

Escreva um Deployment `percurso` com duas réplicas de nginx, label e selector `app: percurso` e readiness garantida pela resposta HTTP na porta 80.

**Antes de começar:** escreva sua hipótese para cada etapa. A solução em `solution/` existe para conferência posterior, não para ser copiada.

## Fase 1 — Preparar e prever

```bash
kubectl config current-context
make lab-prepare LAB=03.01
cat .labs/03.01/resources.yaml
```

Verifique se o namespace foi criado, sem aplicar a solução.

## Fase 2 — Aplicar e observar

Complete todos os TODOs no starter e aplique:

```bash
kubectl apply -f .labs/03.01/
make lab-test LAB=03.01
make lab-observe LAB=03.01
```

Use `kubectl get deploy,rs,pods -n lab-03-01 -o wide`; compare nós, owners e geração observada pelo Deployment.

## Fase 3 — Experimento controlado

Exclua somente um dos Pods gerenciados usando o nome retornado por `kubectl get pod -n lab-03-01`; observe a recriação e a volta para duas réplicas prontas. Não exclua o Deployment.

## Resultado esperado e evidências

O API Server aceita a declaração; um ReplicaSet mantém o número desejado e o scheduler registra os nós dos Pods. A identidade do Pod excluído muda.

**Evidências específicas:** registre `spec.replicas`, `availableReplicas`, o ReplicaSet, o nó de cada Pod e o UID antes/depois da substituição.

## Fase 4 — Diagnosticar

Compare contexto, campos do objeto, condições e eventos. Uma falha de admissão, um erro de scheduling e uma falha de container ocorrem em etapas diferentes; use `kubectl describe` e a documentação para sustentar sua hipótese.

## Fase 5 — Limpar com segurança

```bash
make lab-down LAB=03.01
make lab-status LAB=03.01
```

**Segurança:** o namespace é preservado. Remova recursos temporários que criou fora do contrato; em 03.01 a limpeza não deve afetar outros labs. Não execute `make down`.

## Critérios de conclusão

- [ ] Completei o YAML por conta própria e confirmei `kind-dev`.
- [ ] **Critério exclusivo 03.01:** registre `spec.replicas`, `availableReplicas`, o ReplicaSet, o nó de cada Pod e o UID antes/depois da substituição.
- [ ] Registrei hipótese, comparação esperado/observado e explicação causal.
- [ ] Restaurei alterações temporárias e executei a limpeza do lab.

## Perguntas de diagnóstico e reflexão

- Que etapa ocorreu após o objeto ser persistido na API?
- Por que o novo Pod pode ir para outro nó?
- Por que ver um Deployment não prova que seus dois Pods estão Ready?

## Aprofunde seus conhecimentos

[Documentação oficial](https://kubernetes.io/docs/concepts/overview/components/) · [Aula 03.01](../../arquitetura-cluster/README.md)

---

[← Camada 02](../../../02-operacao-seguranca/README.md) · [↑ Aula 03.01](../../arquitetura-cluster/README.md) · [↑ Camada 03](../../README.md) · [Próximo: Lab 03.02 →](../kube-apiserver-basico/README.md)
