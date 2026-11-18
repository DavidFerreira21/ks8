# Lab — ResourceQuota e LimitRange

[← Camada 02](../../README.md) · [Conceito](../../resourcequota-limitrange/README.md)

## Objetivo

Observar a aplicação de defaults por container e o bloqueio de novos Pods quando o namespace atinge a quota agregada.

**Requisitos:** cluster Kind `dev` e contexto `kind-dev`. Este laboratório utiliza namespace exclusivo `lab-ops-quota`.

## Etapa 1 — Preparação

A partir da pasta deste lab:

```bash
kubectl config current-context
# esperado: kind-dev
kubectl apply -f namespace.yaml
kubectl apply -f policy.yaml
kubectl get resourcequota,limitrange -n lab-ops-quota
```

## Etapa 2 — Pod aceito

```bash
kubectl apply -f pod-ok.yaml
kubectl get pod demo-1 -n lab-ops-quota -o yaml
kubectl describe resourcequota pod-count -n lab-ops-quota
```

**Observe:** `LimitRange` preenche requests/limits ausentes do manifesto na admissão, enquanto `ResourceQuota` controla o total de Pods não terminados no namespace.

## Etapa 3 — Pod rejeitado

```bash
kubectl apply -f pod-rejected.yaml
```

**Resultado esperado:** erro de admissão informando que a quota de Pods foi excedida (`pods=1`). Essa falha é intencional. Se o primeiro Pod não existir ou não ocupar quota, o segundo pode ser aceito: confira o estado antes da tentativa.

```bash
kubectl describe resourcequota pod-count -n lab-ops-quota
kubectl get pods -n lab-ops-quota
```

## Diagnóstico e limpeza

```bash
kubectl describe limitrange container-defaults -n lab-ops-quota
kubectl get events -n lab-ops-quota --sort-by=.lastTimestamp
kubectl delete -f pod-ok.yaml -f pod-rejected.yaml --ignore-not-found
kubectl delete -f policy.yaml --ignore-not-found
```

Preserve o namespace. Apague-o somente após confirmar que pertence exclusivamente a este lab: `kubectl delete -f namespace.yaml`.

## Referências oficiais

- [Resource Quotas](https://kubernetes.io/docs/concepts/policy/resource-quotas/)
- [Limit Ranges](https://kubernetes.io/docs/concepts/policy/limit-range/)
