# Lab 03.06 — CRDs e Custom Resources

[← Aula 03.06](../../crds-custom-resources/README.md) · [↑ Camada 03](../../README.md) · [🧪 Índice dos labs](../../../../docs/labs.md)

> **MODO DESAFIO:** execute `make lab-prepare LAB=03.06`, complete `.labs/03.06/resources.yaml`, aplique com `kubectl apply -f .labs/03.06/` e só então use `make lab-test LAB=03.06`. O comando `make lab-up` usa a solução de referência e fica reservado à CI.

## Objetivo e hipótese

Registrar o tipo AppEnvironment e demonstrar validação de schema sobre uma instância.

**Pré-requisitos:** cluster Kind `dev`, contexto `kind-dev`, `kubectl` e `make`. Namespace de estudo `lab-03-06`. CRDs têm escopo do cluster; preparar o lab instala uma CRD local. **Eliminar essa CRD apaga todas as instâncias do tipo**, razão para usar apenas ambiente descartável.

## Desafio — o que você vai construir

O setup do lab registra uma CRD **somente no Kind descartável**. Depois escreva um `AppEnvironment` `demonstra` com `spec.tier: sandbox` no namespace.

**Antes de começar:** escreva sua hipótese para cada etapa. A solução em `solution/` existe para conferência posterior, não para ser copiada.

**Definição global:** o setup instala a CRD com a anotação didática `learning-path.example/lab-id: "03.06"`. Se ela já existir sem essa propriedade, a preparação será recusada. Não remova manualmente uma CRD compartilhada para contornar a proteção.

## Fase 1 — Preparar e prever

```bash
kubectl config current-context
make lab-prepare LAB=03.06
cat .labs/03.06/resources.yaml
```

**Atenção:** este lab instala uma CRD didática com escopo de cluster durante a preparação. Aguarde `kubectl wait --for=condition=Established crd/appenvironments.learning.example --timeout=120s` antes do apply.

## Fase 2 — Aplicar e observar

Complete todos os TODOs no starter e aplique:

```bash
kubectl apply -f .labs/03.06/
make lab-test LAB=03.06
make lab-observe LAB=03.06
```

Depois de preparar, aguarde `kubectl wait --for=condition=Established crd/appenvironments.learning.example --timeout=120s`. Execute `kubectl api-resources --api-group=learning.example`, crie a CR e consulte seus campos.

## Fase 3 — Experimento controlado

Copie o manifesto para arquivo temporário com `spec.tier: numero-invalido`? Isso ainda é string; use `tier: 123` e `kubectl apply --dry-run=server --validate=strict` para observar rejeição de tipo. Não crie recursos de infraestrutura.

### Testar uma CR que viola o schema

Depois de registrar a CRD e criar a instância válida, compare com um exemplar que define `spec.tier` como número, em vez de string:

```bash
kubectl wait --for=condition=Established crd/appenvironments.learning.example --timeout=120s
kubectl apply --dry-run=server --validate=strict \
  -f trilhas/03-arquitetura/labs/crds-custom-resources-basico/experiments/appenv-invalido.yaml
kubectl get appenvironments.learning.example -n lab-03-06
```

A falha de schema é **esperada** e a CR `demonstra` não deve ser alterada. Em seguida, registre também o que **não** foi criado: CRD + CR sem controller não geram infraestrutura por conta própria.

## Resultado esperado e evidências

O tipo aparece no discovery, o recurso válido pode ser criado e valores de tipo errado são rejeitados. Nenhum Deployment é gerado sem controller próprio.

**Evidências específicas:** registre a condição Established, discovery, CR válida e mensagem de rejeição do schema para o valor numérico.

## Fase 4 — Diagnosticar

Compare contexto, campos do objeto, condições e eventos. Uma falha de admissão, um erro de scheduling e uma falha de container ocorrem em etapas diferentes; use `kubectl describe` e a documentação para sustentar sua hipótese.

## Fase 5 — Limpar com segurança

```bash
make lab-down LAB=03.06
make lab-status LAB=03.06
```

**Segurança:** o namespace é preservado. A limpeza apaga primeiro a Custom Resource `demonstra`, consulta todas as instâncias `AppEnvironment` no cluster e **recusa apagar a CRD se restarem instâncias**. Não use `kubectl delete crd` manualmente para contornar essa proteção; verifique dependências de outros namespaces.

## Critérios de conclusão

- [ ] Completei o YAML por conta própria e confirmei `kind-dev`.
- [ ] **Critério exclusivo 03.06:** registre a condição Established, discovery, CR válida e mensagem de rejeição do schema para o valor numérico.
- [ ] Registrei hipótese, comparação esperado/observado e explicação causal.
- [ ] Restaurei alterações temporárias e executei a limpeza do lab.

## Perguntas de diagnóstico e reflexão

- Qual diferença existe entre CRD e CR?
- Por que `status` não muda automaticamente sem reconciler?
- Por que excluir uma CRD pode afetar outras instâncias?

## Aprofunde seus conhecimentos

[Documentação oficial](https://kubernetes.io/docs/tasks/extend-kubernetes/custom-resources/custom-resource-definitions/) · [Aula 03.06](../../crds-custom-resources/README.md)

---

[← Lab 03.05](../kube-controller-manager-basico/README.md) · [↑ Aula 03.06](../../crds-custom-resources/README.md) · [↑ Camada 03](../../README.md) · [Próximo: Lab 03.07 →](../custom-controllers-operators-basico/README.md)
