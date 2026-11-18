# Lab 01.06 — Namespaces: isolamento logico

> **MODO DESAFIO:** execute `make lab-prepare LAB=01.06` para preparar o namespace e criar o arquivo `.labs/01.06/resources.yaml`. Complete o YAML com base no objetivo desta aula. Execute `kubectl apply -f .labs/01.06/` e depois `make lab-test LAB=01.06`. **`make lab-up` é exclusivo da CI** e aplica a solução, portanto não é o fluxo do aluno. `make lab-solution LAB=01.06` mostra onde consultar a referência.

[← Camada 01](../../README.md) · [Guia dos labs](../../../../docs/labs.md)

## Objetivo e hipótese

Namespaces isolam nomes de objetos e definem escopo de políticas, mas não são clusters nem segurança de rede por padrão.

**Pré-requisitos:** Kind `dev` ativo, `kubectl`, `make`; namespace exclusivo `lab-01-06`.

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
make lab-prepare LAB=01.06
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

## Checklist

- [ ] Previ os recursos criados e conferi o resultado.
- [ ] Executei e expliquei o experimento.
- [ ] Investiguei eventos e condições.
- [ ] Limpei os recursos sem afetar outros labs.
