# Lab 02.01 — Labels e seleção de Pods

[← Aula 02.01](../../labels-selectors-annotations/README.md) · [↑ Camada 02](../../README.md) · [🧪 Índice dos labs](../../../../docs/labs.md)

> **MODO DESAFIO:** `make lab-prepare LAB=02.01` cria o namespace e copia um **starter incompleto** para `.labs/02.01/resources.yaml`. Você completa o YAML e executa `kubectl apply -f .labs/02.01/`. Só então use `make lab-test LAB=02.01` e `make lab-observe LAB=02.01`. **`make lab-up` aplica a solução e é reservado à CI.**

## Objetivo e hipótese

Comprovar que label selectors selecionam Pods, enquanto annotations não influenciam a seleção.

**Pré-requisitos:** Kind `dev`, contexto `kind-dev`, `kubectl`, `make`; namespace isolado `lab-02-01`. 

## Desafio — o que você vai construir

Escreva um Pod `rotulado` com labels `app: demo` e `tier: backend` e annotation `estudo: labels`. O container BusyBox deve permanecer ativo para inspeção.

Antes de olhar `solution/`, formule uma hipótese sobre o comportamento e consulte `kubectl explain` quando necessário.

## Fase 1 — Preparar e prever

```bash
kubectl config current-context
make lab-prepare LAB=02.01
cat .labs/02.01/resources.yaml
```

Descreva quais objetos devem aparecer e qual observação confirmará sua hipótese.

## Fase 2 — Aplicar e observar

Complete os campos TODO no starter e execute:

```bash
kubectl apply -f .labs/02.01/
make lab-test LAB=02.01
make lab-observe LAB=02.01
```

`kubectl get pods -n lab-02-01 --show-labels` e `kubectl get pods -n lab-02-01 -l app=demo` devem incluir o Pod.

## Fase 3 — Experimento controlado

Compare `kubectl get pods -n lab-02-01 -l tier=backend` com `-l tier=frontend`. Consulte a annotation em `kubectl get pod rotulado -n lab-02-01 -o yaml`; depois altere temporariamente a label com `kubectl label pod rotulado tier=frontend -n lab-02-01 --overwrite` e repita os selectors. Restaure `tier=backend` antes de validar novamente.

## Resultado esperado e evidências

O selector correspondente retorna `rotulado`; o não correspondente retorna zero. A annotation permanece visível como metadata sem afetar a seleção.

**Evidências específicas:** guarde o YAML do Pod, resultados de `--show-labels` e das duas consultas de selector antes e depois da alteração; explique por que a annotation não participa.

## Fase 4 — Diagnosticar

`kubectl describe pod rotulado -n lab-02-01` e `kubectl get pod rotulado -n lab-02-01 -o yaml`.

Se a observação divergir, identifique primeiro **contexto → namespace → objeto → eventos → hipótese**, sem aplicar soluções aleatórias.

## Fase 5 — Limpar com segurança

```bash
make lab-down LAB=02.01
make lab-status LAB=02.01
```

A limpeza remove os objetos declarados no contrato e preserva o namespace. Desfaça explicitamente alterações manuais do experimento. **Não execute `make down`**, que remove o cluster Kind.

## Critérios de conclusão

- [ ] Completei o YAML sem copiar a solução e confirmei o contexto esperado.
- [ ] Observei o comportamento específico descrito em **Resultado esperado**.
- [ ] Registrei o resultado do experimento, uma hipótese e a explicação técnica.
- [ ] Removi os recursos do lab e revi qualquer alteração manual.

## Perguntas de diagnóstico e reflexão

- Por que uma annotation não faz parte do selector?
- O que acontece com a seleção quando a label muda?

## Aprofunde seus conhecimentos

[Documentação oficial](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/) · [Aula 02.01](../../labels-selectors-annotations/README.md)

---

[← Camada 01](../../../01-fundamentos/README.md) · [↑ Camada 02](../../README.md) · [Próximo: Lab 02.02 →](../rbac-minimo/README.md)
