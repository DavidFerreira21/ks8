# Exercício avançado 03.07 — Reconciler real de AppEnvironment

[← Lab 03.07](../../README.md) · [← Aula 03.07](../../../../custom-controllers-operators/README.md)

> **Opcional:** este é um controlador mínimo, escrito em Python padrão, que faz polling da API Kubernetes e reconcilia ConfigMaps a partir de uma Custom Resource. **É uma demonstração de aprendizado, não um Operator production-ready.** Não é parte da CI Kind padrão.

## Objetivo

A aula demonstrou reconciliação nativa com um Deployment. Agora você vai observar a diferença fundamental: um **controller customizado** lê um `AppEnvironment` e cria/atualiza um ConfigMap correspondente. Se você alterar a intenção ou apagar o ConfigMap gerado, o reconciler deve recriar o estado desejado.

**O que aprender:** descoberta de CRD, permissão RBAC namespaced, polling, idempotência, `ownerReferences`, logs e falhas. Este exemplo **não** implementa watch eficiente, leader election, metrics, status nem finalizer, que seriam preocupações de produção.

## Fase 1 — Preparar CRD e namespace

```bash
kubectl config current-context # kind-dev
make lab-prepare LAB=03.06
make lab-prepare LAB=03.07
kubectl wait --for=condition=Established crd/appenvironments.learning.example --timeout=120s
```

Preparar 03.06 registra uma **CRD global** em Kind descartável. Não exclua definições de tipos existentes em um cluster compartilhado.

## Fase 2 — Implantar reconciler com RBAC mínimo

```bash
kubectl create configmap appenv-reconciler-source -n lab-03-07 \
  --from-file=controller.py=trilhas/03-arquitetura/labs/custom-controllers-operators-basico/examples/reconciler-real/controller.py \
  --dry-run=client -o yaml | kubectl apply -f -
kubectl apply -f trilhas/03-arquitetura/labs/custom-controllers-operators-basico/examples/reconciler-real/controller.yaml
kubectl rollout status deploy/appenv-reconciler -n lab-03-07 --timeout=180s
kubectl auth can-i list appenvironments.learning.example \
  -n lab-03-07 --as=system:serviceaccount:lab-03-07:appenv-reconciler
```

Leia o código antes de aplicar. Ele consulta somente o namespace `lab-03-07` e utiliza um ServiceAccount dedicado.

## Fase 3 — Testar reconciliação de verdade

```bash
kubectl apply -f trilhas/03-arquitetura/labs/custom-controllers-operators-basico/examples/reconciler-real/appenvironment.yaml
kubectl get configmap environment-demo -n lab-03-07 -o yaml
kubectl patch appenvironments.learning.example demo -n lab-03-07 --type merge -p '{"spec":{"tier":"staging"}}'
kubectl get cm environment-demo -n lab-03-07 -o jsonpath='{.data.tier}'
kubectl delete cm environment-demo -n lab-03-07
kubectl get cm environment-demo -n lab-03-07 --watch
```

O ConfigMap deve surgir com `sandbox`, mudar para `staging` e ser **recriado** após exclusão, normalmente em até um ciclo de polling. Interrompa o `--watch` com Ctrl+C. Inspecione `kubectl logs deploy/appenv-reconciler -n lab-03-07` se a reconciliação falhar.

## Fase 4 — Diagnosticar e refletir

- Qual diferença existe entre CRD registrada e controller efetivamente operando?
- Por que apagar o ConfigMap não resolve o drift enquanto a XR continua declarando sua existência?
- O que o `ownerReferences.uid` evita quando alguém recria um objeto com o mesmo nome?
- Como este exemplo mudaria se milhares de CRs existissem, exigindo watch, rate limits e retry/backoff?

**Evidência funcional:** capture Custom Resource `spec.tier`, ConfigMap `data.tier` e logs antes/depois do patch e da recriação. Um Deployment do reconciler em Ready **não prova** que ele gerencia recursos.

## Fase 5 — Limpar

```bash
kubectl delete -f trilhas/03-arquitetura/labs/custom-controllers-operators-basico/examples/reconciler-real/appenvironment.yaml --ignore-not-found
kubectl delete -f trilhas/03-arquitetura/labs/custom-controllers-operators-basico/examples/reconciler-real/controller.yaml --ignore-not-found
kubectl delete configmap appenv-reconciler-source -n lab-03-07 --ignore-not-found
kubectl get cm environment-demo -n lab-03-07 --ignore-not-found
```

Verifique que o ConfigMap composto foi removido pela garbage collection do owner. A CRD permanece como artefato do Lab 03.06 — **não a exclua sem inventário de todas as instâncias**.

[Operator pattern](https://kubernetes.io/docs/concepts/extend-kubernetes/operator/) · [Custom controllers](https://kubernetes.io/docs/concepts/architecture/controller/)
