# Lab 01.06 — Namespaces

[← Aula 01.06](../../namespaces/README.md) · [↑ Camada 01](../../README.md) · [🧪 Índice dos labs](../../../../docs/labs.md)

> **MODO DESAFIO:** execute `make lab-prepare LAB=01.06` para preparar o namespace e criar o arquivo `.labs/01.06/resources.yaml`. Complete o YAML com base no objetivo desta aula. Execute `kubectl apply -f .labs/01.06/` e depois `make lab-test LAB=01.06`. **`make lab-up` é exclusivo da CI** e aplica a solução, portanto não é o fluxo do aluno. `make lab-solution LAB=01.06` mostra onde consultar a referência.


## Objetivo e hipótese

Namespaces isolam nomes de objetos e definem escopo de políticas, mas não são clusters nem segurança de rede por padrão.

**Pré-requisitos:** Kind `dev` ativo, `kubectl`, `make`; namespace exclusivo `lab-01-06`.

## Desafio — o que você vai construir

Crie um `ConfigMap` chamado `identidade` em `lab-01-06`, com `data.ambiente: aula-0106`. Depois compare o objeto com outro `ConfigMap` chamado `identidade` em um **segundo namespace criado somente para o experimento**. Entenda que namespace organiza nomes, não isola rede automaticamente.

**Antes de aplicar:** use o arquivo incompleto em `.labs/01.06/` como ponto de partida. Confira campos com `kubectl explain`; não abra a solução antes de formular uma tentativa.

## Fase 1 — Inspecionar o que será aplicado

```bash
kubectl config current-context
kubectl get nodes
make lab-prepare LAB=01.06
cat .labs/01.06/resources.yaml
```

Antes de executar, anote quais objetos e controladores devem aparecer.

## Fase 2 — Aplicar e validar

```bash
# Complete os campos TODO do arquivo local
kubectl apply -f .labs/01.06/
make lab-test LAB=01.06
make lab-observe LAB=01.06
```

**Observe escopo e identidade:**

```bash
kubectl get configmap identidade -n lab-01-06
kubectl get configmap identidade -n default --ignore-not-found
kubectl get namespaces
kubectl api-resources --namespaced=false | head -20
```

**Experimento — mesmo nome em outro namespace:**

```bash
kubectl create namespace lab-01-06-extra
kubectl create configmap identidade --from-literal=ambiente=outro -n lab-01-06-extra
kubectl get configmap identidade -n lab-01-06 -o yaml
kubectl get configmap identidade -n lab-01-06-extra -o yaml
kubectl delete configmap identidade -n lab-01-06-extra
kubectl delete namespace lab-01-06-extra
```

**Atenção:** a exclusão do namespace secundário só é segura se você o criou exclusivamente para este experimento e ele não contém recursos de terceiros. O namespace principal do lab permanece após `lab-down`.

## Resultado esperado e evidências

- O ConfigMap `identidade` existe em `lab-01-06` e não aparece no namespace `default` a menos que alguém o tenha criado lá.
- Dois ConfigMaps com o **mesmo nome** podem coexistir em namespaces diferentes, com `data.ambiente` distinto.
- `kubectl api-resources --namespaced=false` mostra tipos de recurso cujo escopo é o cluster, não um namespace.

**Se o resultado divergir:** confirme contexto, namespace, eventos e o YAML escrito. Diferencie comportamento intencional do experimento e erro na sua configuração.

## Fase 3 — Diagnóstico

```bash
kubectl get events -n lab-01-06 --sort-by=.lastTimestamp
kubectl get all -n lab-01-06
```

Compare `spec` e `status`, consulte `describe` e explique qualquer divergência. Os checks automáticos cobrem condições básicas, não o raciocínio do experimento.

## Fase 4 — Limpeza

```bash
make lab-down LAB=01.06
make lab-status LAB=01.06
```

O namespace é preservado. Não use `make down` para excluir um único lab.

## Critérios de conclusão

- [ ] Criei e inspecionei `identidade` no namespace correto.
- [ ] Criei o mesmo nome em outro namespace e comparei os valores.
- [ ] Expliquei por que namespaces não equivalem a clusters ou isolamento de rede.
- [ ] Apaguei somente o namespace extra que eu mesmo criei e limpei o lab.

## Perguntas de diagnóstico e reflexão

- Que consulta demonstra que um recurso com namespace não aparece automaticamente em outro?
- Por que namespaces sozinhos não são uma política de isolamento de rede?

**Evidências específicas:** registre recursos consultados em namespaces distintos e demonstre qual consulta foi limitada por namespace; explique o escopo observado.

## Aprofunde seus conhecimentos

[Namespaces](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/) · [Organização de objetos](https://kubernetes.io/docs/concepts/overview/working-with-objects/) · [DNS e Namespaces](https://kubernetes.io/docs/concepts/services-networking/dns-pod-service/).

Releia a [aula teórica](../../namespaces/README.md) e compare os exemplos com o que você observou no cluster.

---

[← Lab 01.05](../services-basico/README.md) · [↑ Aula 01.06](../../namespaces/README.md) · [Próximo: Lab 01.07 →](../configmaps-basico/README.md)
