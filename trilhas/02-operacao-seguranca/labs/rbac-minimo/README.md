# Lab — RBAC e ServiceAccount com menor privilégio

[← Camada 02](../../README.md) · [Conceito](../../rbac-serviceaccount/README.md)

## Objetivo

Criar uma identidade para um workload e autorizar apenas leitura de Pods em um namespace. Verificar permissões positivas e negativas sem distribuir credenciais.

**Requisitos:** cluster Kind `dev`, contexto `kind-dev`, `kubectl` com acesso administrativo ao cluster local. Não executar em clusters corporativos ou compartilhados.

## Preparação

Na pasta deste lab, confirme:

```bash
kubectl config current-context
# Deve retornar kind-dev
kubectl apply -f namespace.yaml
kubectl apply -f rbac.yaml
```

## Experimento

A identidade será `system:serviceaccount:lab-ops-rbac:lab-reader`.

```bash
kubectl auth can-i get pods -n lab-ops-rbac --as=system:serviceaccount:lab-ops-rbac:lab-reader
# esperado: yes

kubectl auth can-i list pods -n lab-ops-rbac --as=system:serviceaccount:lab-ops-rbac:lab-reader
# esperado: yes

kubectl auth can-i list secrets -n lab-ops-rbac --as=system:serviceaccount:lab-ops-rbac:lab-reader
# esperado: no

kubectl auth can-i delete pods -n lab-ops-rbac --as=system:serviceaccount:lab-ops-rbac:lab-reader
# esperado: no
```

**Observe:** ServiceAccount identifica o sujeito, Role descreve permissões e RoleBinding associa ambos. A flag `--as` utiliza impersonação do usuário que executa o comando; ela exige autorização para impersonate. O Kind local é o alvo deste exercício.

## Diagnóstico

```bash
kubectl describe role pod-reader -n lab-ops-rbac
kubectl describe rolebinding pod-reader-binding -n lab-ops-rbac
kubectl get sa lab-reader -n lab-ops-rbac
```

## Limpeza

```bash
kubectl delete -f rbac.yaml --ignore-not-found
```

O namespace é preservado. Somente remova o namespace com `kubectl delete -f namespace.yaml` se foi criado exclusivamente para este lab e não contém outros recursos relevantes.

## Referência

[Using RBAC Authorization](https://kubernetes.io/docs/reference/access-authn-authz/rbac/)
