# Lab 03.05 — kube-controller-manager

[← Aula 03.05](../../kube-controller-manager/README.md) · [↑ Camada 03](../../README.md) · [🧪 Índice dos labs](../../../../docs/labs.md)

> **MODO DESAFIO:** execute `make lab-prepare LAB=03.05`, complete `.labs/03.05/resources.yaml`, aplique com `kubectl apply -f .labs/03.05/` e só então use `make lab-test LAB=03.05`. O comando `make lab-up` usa a solução de referência e fica reservado à CI.

## Objetivo e hipótese

Demonstrar que um controlador converge réplicas após exclusão manual de um Pod.

**Pré-requisitos:** cluster Kind `dev`, contexto `kind-dev`, `kubectl` e `make`. Namespace de estudo `lab-03-05`. 

## Desafio — o que você vai construir

Defina Deployment `controlador` com duas réplicas de nginx e labels/selectors `app: controlador`.

**Antes de começar:** escreva sua hipótese para cada etapa. A solução em `solution/` existe para conferência posterior, não para ser copiada.

## Fase 1 — Preparar e prever

```bash
kubectl config current-context
make lab-prepare LAB=03.05
cat .labs/03.05/resources.yaml
```

Verifique se o namespace foi criado, sem aplicar a solução.

## Fase 2 — Aplicar e observar

Complete todos os TODOs no starter e aplique:

```bash
kubectl apply -f .labs/03.05/
make lab-test LAB=03.05
make lab-observe LAB=03.05
```

Identifique ReplicaSet, owners, UID e status de `kubectl get pods -n lab-03-05 -o wide`.

## Fase 3 — Experimento controlado

Registre o UID de um Pod, exclua-o manualmente e observe a recuperação via `kubectl rollout status deploy/controlador -n lab-03-05`. Compare ownerReferences e UIDs antes/depois.

## Resultado esperado e evidências

O controlador restaura o número de Pods sem que o usuário reaplique o Deployment. O processo não garante a identidade original do Pod.

**Evidências específicas:** registe UID anterior, novo UID, ReplicaSet proprietário, desired/available replicas e tempo até recuperação.

## Fase 4 — Diagnosticar

Compare contexto, campos do objeto, condições e eventos. Uma falha de admissão, um erro de scheduling e uma falha de container ocorrem em etapas diferentes; use `kubectl describe` e a documentação para sustentar sua hipótese.

## Fase 5 — Limpar com segurança

```bash
make lab-down LAB=03.05
make lab-status LAB=03.05
```

**Segurança:** o namespace é preservado. Remova recursos temporários que criou fora do contrato; em 03.05 a limpeza não deve afetar outros labs. Não execute `make down`.

## Critérios de conclusão

- [ ] Completei o YAML por conta própria e confirmei `kind-dev`.
- [ ] **Critério exclusivo 03.05:** registe UID anterior, novo UID, ReplicaSet proprietário, desired/available replicas e tempo até recuperação.
- [ ] Registrei hipótese, comparação esperado/observado e explicação causal.
- [ ] Restaurei alterações temporárias e executei a limpeza do lab.

## Perguntas de diagnóstico e reflexão

- Por que um Pod do Deployment não é igual a Pod avulso?
- Que objeto é o owner do Pod?
- O que a ausência de `availableReplicas` indica sobre reconciliação?

## Aprofunde seus conhecimentos

[Documentação oficial](https://kubernetes.io/docs/concepts/architecture/controller/) · [Aula 03.05](../../kube-controller-manager/README.md)

---

[← Lab 03.04](../admission-controllers-basico/README.md) · [↑ Aula 03.05](../../kube-controller-manager/README.md) · [↑ Camada 03](../../README.md) · [Próximo: Lab 03.06 →](../crds-custom-resources-basico/README.md)
