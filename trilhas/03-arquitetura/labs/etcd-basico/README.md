# Lab 03.03 — etcd

[← Aula 03.03](../../etcd/README.md) · [↑ Camada 03](../../README.md) · [🧪 Índice dos labs](../../../../docs/labs.md)

> **MODO DESAFIO:** execute `make lab-prepare LAB=03.03`, complete `.labs/03.03/resources.yaml`, aplique com `kubectl apply -f .labs/03.03/` e só então use `make lab-test LAB=03.03`. O comando `make lab-up` usa a solução de referência e fica reservado à CI.

## Objetivo e hipótese

Observar versões do estado persistido via API e explicar a função de `resourceVersion`.

**Pré-requisitos:** cluster Kind `dev`, contexto `kind-dev`, `kubectl` e `make`. Namespace de estudo `lab-03-03`. 

## Desafio — o que você vai construir

Escreva um ConfigMap `registro` com `data.revisao: primeira`.

**Antes de começar:** escreva sua hipótese para cada etapa. A solução em `solution/` existe para conferência posterior, não para ser copiada.

## Fase 1 — Preparar e prever

```bash
kubectl config current-context
make lab-prepare LAB=03.03
cat .labs/03.03/resources.yaml
```

Verifique se o namespace foi criado, sem aplicar a solução.

## Fase 2 — Aplicar e observar

Complete todos os TODOs no starter e aplique:

```bash
kubectl apply -f .labs/03.03/
make lab-test LAB=03.03
make lab-observe LAB=03.03
```

Execute `kubectl get cm registro -n lab-03-03 -o jsonpath='{.metadata.resourceVersion}'` e registre a versão inicial.

## Fase 3 — Experimento controlado

Atualize temporariamente com `kubectl patch configmap registro -n lab-03-03 --type merge -p '{"data":{"revisao":"segunda"}}'`; compare `resourceVersion` e conteúdo. Reaplique o YAML local para restaurar `primeira`.

### Antes, durante e depois da persistência

```bash
kubectl get cm registro -n lab-03-03 -o jsonpath='{.metadata.resourceVersion}{"\n"}{.data.revisao}{"\n"}'
kubectl patch cm registro -n lab-03-03 --type merge -p '{"data":{"revisao":"segunda"}}'
kubectl get cm registro -n lab-03-03 -o jsonpath='{.metadata.resourceVersion}{"\n"}{.data.revisao}{"\n"}'
kubectl apply -f .labs/03.03/resources.yaml
kubectl get cm registro -n lab-03-03 -o jsonpath='{.data.revisao}'
```

**Evidência:** `resourceVersion` muda e não volta ao valor anterior ao restaurar o conteúdo. O experimento observa armazenamento **via API**, não operações diretas de etcd.

## Resultado esperado e evidências

A atualização altera o valor persistido e a `resourceVersion`. Reaplicar o manifesto original reverte os dados por nova operação, não pelo retorno ao mesmo número de versão.

**Evidências específicas:** registre os dois valores de `data.revisao` e versões observadas, explicando que não se acessou etcd diretamente.

## Fase 4 — Diagnosticar

Compare contexto, campos do objeto, condições e eventos. Uma falha de admissão, um erro de scheduling e uma falha de container ocorrem em etapas diferentes; use `kubectl describe` e a documentação para sustentar sua hipótese.

## Fase 5 — Limpar com segurança

```bash
make lab-down LAB=03.03
make lab-status LAB=03.03
```

**Segurança:** o namespace é preservado. Remova recursos temporários que criou fora do contrato; em 03.03 a limpeza não deve afetar outros labs. Não execute `make down`.

## Critérios de conclusão

- [ ] Completei o YAML por conta própria e confirmei `kind-dev`.
- [ ] **Critério exclusivo 03.03:** registre os dois valores de `data.revisao` e versões observadas, explicando que não se acessou etcd diretamente.
- [ ] Registrei hipótese, comparação esperado/observado e explicação causal.
- [ ] Restaurei alterações temporárias e executei a limpeza do lab.

## Perguntas de diagnóstico e reflexão

- Por que `resourceVersion` não é contador de cada Pod ou timestamp?
- O que é persistido: execução de containers ou declaração dos objetos?
- Por que restaurar o conteúdo não restaura o número de versão?

## Aprofunde seus conhecimentos

[Documentação oficial](https://kubernetes.io/docs/tasks/administer-cluster/configure-upgrade-etcd/) · [Aula 03.03](../../etcd/README.md)

---

[← Lab 03.02](../kube-apiserver-basico/README.md) · [↑ Aula 03.03](../../etcd/README.md) · [↑ Camada 03](../../README.md) · [Próximo: Lab 03.04 →](../admission-controllers-basico/README.md)
