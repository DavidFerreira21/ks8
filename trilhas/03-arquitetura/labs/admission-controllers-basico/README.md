# Lab 03.04 — Admission Controllers

[← Aula 03.04](../../admission-controllers/README.md) · [↑ Camada 03](../../README.md) · [🧪 Índice dos labs](../../../../docs/labs.md)

> **MODO DESAFIO:** execute `make lab-prepare LAB=03.04`, complete `.labs/03.04/resources.yaml`, aplique com `kubectl apply -f .labs/03.04/` e só então use `make lab-test LAB=03.04`. O comando `make lab-up` usa a solução de referência e fica reservado à CI.

## Objetivo e hipótese

Demonstrar rejeição por quota no API Server sem atribuir o erro ao scheduler.

**Pré-requisitos:** cluster Kind `dev`, contexto `kind-dev`, `kubectl` e `make`. Namespace de estudo `lab-03-04`. 

## Desafio — o que você vai construir

Crie ResourceQuota `limites` com `hard.pods: '1'` e Pod `admitido` com imagem BusyBox em execução contínua.

**Antes de começar:** escreva sua hipótese para cada etapa. A solução em `solution/` existe para conferência posterior, não para ser copiada.

## Fase 1 — Preparar e prever

```bash
kubectl config current-context
make lab-prepare LAB=03.04
cat .labs/03.04/resources.yaml
```

Verifique se o namespace foi criado, sem aplicar a solução.

## Fase 2 — Aplicar e observar

Complete todos os TODOs no starter e aplique:

```bash
kubectl apply -f .labs/03.04/
make lab-test LAB=03.04
make lab-observe LAB=03.04
```

`kubectl describe quota limites -n lab-03-04` mostra `used/hard`; `kubectl get pods -n lab-03-04` mostra o Pod admitido.

## Fase 3 — Experimento controlado

Tente criar `kubectl run extra -n lab-03-04 --image=busybox:1.36 --restart=Never -- sleep 3600`. Registre o erro esperado de quota excedida; se inesperadamente admitido, exclua o Pod extra e investigue. Não modifique a quota global.

### Comparação de admissão com scheduling

```bash
kubectl describe resourcequota limites -n lab-03-04
kubectl run extra -n lab-03-04 --restart=Never --image=busybox:1.36 -- sleep 3600
kubectl get pod extra -n lab-03-04 --ignore-not-found
```

A segunda criação deve receber um erro de quota. **Esse erro é esperado**: o Pod adicional não deve existir na API. Se existir, apague-o explicitamente e investigue a ResourceQuota antes de marcar o experimento como aprovado. Compare com o Pod `admitido`: não houve tentativa de scheduling para `extra`.

## Resultado esperado e evidências

A segunda criação é rejeitada diretamente pela admissão por exceder quota, sem produzir Pod extra Pending.

**Evidências específicas:** capture `used/hard` e a resposta da API para a tentativa rejeitada; explique por que não há evento de scheduling do segundo Pod.

## Fase 4 — Diagnosticar

Compare contexto, campos do objeto, condições e eventos. Uma falha de admissão, um erro de scheduling e uma falha de container ocorrem em etapas diferentes; use `kubectl describe` e a documentação para sustentar sua hipótese.

## Fase 5 — Limpar com segurança

```bash
make lab-down LAB=03.04
make lab-status LAB=03.04
```

**Segurança:** o namespace é preservado. Remova recursos temporários que criou fora do contrato; em 03.04 a limpeza não deve afetar outros labs. Não execute `make down`.

## Critérios de conclusão

- [ ] Completei o YAML por conta própria e confirmei `kind-dev`.
- [ ] **Critério exclusivo 03.04:** capture `used/hard` e a resposta da API para a tentativa rejeitada; explique por que não há evento de scheduling do segundo Pod.
- [ ] Registrei hipótese, comparação esperado/observado e explicação causal.
- [ ] Restaurei alterações temporárias e executei a limpeza do lab.

## Perguntas de diagnóstico e reflexão

- Qual é a evidência de rejeição na API?
- Por que a disponibilidade do nó não anula a quota?
- Que diferença existe entre controlador mutating e validating?

## Aprofunde seus conhecimentos

[Documentação oficial](https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers/) · [Aula 03.04](../../admission-controllers/README.md)

---

[← Lab 03.03](../etcd-basico/README.md) · [↑ Aula 03.04](../../admission-controllers/README.md) · [↑ Camada 03](../../README.md) · [Próximo: Lab 03.05 →](../kube-controller-manager-basico/README.md)
