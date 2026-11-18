# Lab 01.09 — Requests e Limits

[← Aula 01.09](../../requests-limits/README.md) · [↑ Camada 01](../../README.md) · [🧪 Índice dos labs](../../../../docs/labs.md)

> **MODO DESAFIO:** execute `make lab-prepare LAB=01.09` para criar o namespace e copiar um arquivo incompleto para `.labs/01.09/resources.yaml`. **Escreva os campos TODO, aplique você mesmo com `kubectl apply -f .labs/01.09/` e valide com `make lab-test LAB=01.09`**. `make lab-up` é só para CI. Use `make lab-solution LAB=01.09` apenas depois de tentar.


## Objetivo e hipótese

O Scheduler usa requests para decidir elegibilidade de nós, enquanto limits restringem consumo. Hipótese: um Pod pedindo 1000 CPUs entra em Running?

**Escopo:** cluster Kind `dev`, namespace exclusivo `lab-01-09`.

## Desafio — o que você vai construir

Crie o Deployment `recursos` com nginx e defina `resources.requests` para CPU/memória e `resources.limits` para ambos. Em seguida, compare os recursos configurados com a capacidade dos nós e provoque um Pod temporário **Pending** por request exagerado.

**Antes de aplicar:** use o arquivo incompleto em `.labs/01.09/` como ponto de partida. Confira campos com `kubectl explain`; não abra a solução antes de formular uma tentativa.

## Fase 1 — Preparar

```bash
kubectl config current-context
kubectl get nodes
make lab-prepare LAB=01.09
cat .labs/01.09/resources.yaml
```

Preveja os objetos criados e seus estados.

## Fase 2 — Executar

```bash
# Complete o manifesto em .labs/01.09/resources.yaml
kubectl apply -f .labs/01.09/
make lab-test LAB=01.09
make lab-observe LAB=01.09
```

**Observe o orçamento:**

```bash
kubectl describe deployment recursos -n lab-01-09
kubectl describe pod -n lab-01-09 -l app=recursos-demo
kubectl get pod -n lab-01-09 -o wide
kubectl top pod -n lab-01-09  # requer Metrics Server, opcional neste lab
```

**Experimento — Pod impossível de agendar:** crie um Pod temporário solicitando CPU maior que a capacidade de um nó (sem modificar os manifests versionados):

```bash
kubectl run pedido-exagerado -n lab-01-09 --image=busybox:1.36 --overrides='{"spec":{"containers":[{"name":"pedido-exagerado","image":"busybox:1.36","command":["sh","-c","sleep 3600"],"resources":{"requests":{"cpu":"1000","memory":"16Mi"}}}]}}' --restart=Never
kubectl describe pod pedido-exagerado -n lab-01-09
kubectl delete pod pedido-exagerado -n lab-01-09 --ignore-not-found
```

O evento `FailedScheduling` deverá indicar recursos insuficientes; observe que um request não garante consumo real, e limites CPU e memória têm efeitos diferentes.

## Resultado esperado e evidências

- O Deployment simples deve ficar `Available`, com CPU/memória em `kubectl describe pod`.
- O Pod `pedido-exagerado` permanece `Pending`; em eventos, normalmente aparecerá `FailedScheduling`/`Insufficient cpu` porque `1000` CPUs excedem a capacidade do nó.
- A ausência de `kubectl top` não impede o lab básico: métricas de consumo requerem Metrics Server, opcional aqui. Diferencie `requests` (scheduling) e `limits` (execução).

**Se o resultado divergir:** confirme contexto, namespace, eventos e o YAML escrito. Diferencie comportamento intencional do experimento e erro na sua configuração.

## Fase 3 — Diagnosticar

```bash
kubectl get events -n lab-01-09 --sort-by=.lastTimestamp
kubectl get all -n lab-01-09
```

Leia `describe`, compare `spec` e `status` e explique eventos. Testes automatizados conferem existência e readiness quando indicado, não o experimento pedagógico.

## Fase 4 — Limpeza

```bash
make lab-down LAB=01.09
make lab-status LAB=01.09
```

Namespace preservado intencionalmente. Nunca apague o cluster inteiro para limpar só um lab.

## Critérios de conclusão

- [ ] Defini requests e limits para CPU e memória.
- [ ] Identifiquei os recursos do container em `kubectl describe`.
- [ ] Expliquei o `Pending` e o evento `FailedScheduling` do Pod exagerado.
- [ ] Removi o Pod temporário e os objetos do lab.

## Aprofunde seus conhecimentos

[Gerenciamento de recursos](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/) · [Scheduler e recursos](https://kubernetes.io/docs/concepts/scheduling-eviction/resource-bin-packing/) · [Diagnóstico de Pods Pending](https://kubernetes.io/docs/tasks/debug/debug-application/debug-pods/).

Releia a [aula teórica](../../requests-limits/README.md) e compare os exemplos com o que você observou no cluster.

---

[← Lab 01.08](../secrets-basico/README.md) · [↑ Aula 01.09](../../requests-limits/README.md) · [Próximo: Lab 01.10 →](../probes-basico/README.md)
