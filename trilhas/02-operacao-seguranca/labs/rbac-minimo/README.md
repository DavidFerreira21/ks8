# Lab 02.02 — RBAC e ServiceAccount com menor privilégio

[← Aula 02.02](../../rbac-serviceaccount/README.md) · [↑ Camada 02](../../README.md) · [🧪 Índice dos labs](../../../../docs/labs.md)

> **MODO DESAFIO:** `make lab-prepare LAB=02.02` cria o namespace e copia um **starter incompleto** para `.labs/02.02/resources.yaml`. Você completa o YAML e executa `kubectl apply -f .labs/02.02/`. Só então use `make lab-test LAB=02.02` e `make lab-observe LAB=02.02`. **`make lab-up` aplica a solução e é reservado à CI.**

## Objetivo e hipótese

Autorizar somente leitura de Pods a uma ServiceAccount e demonstrar autorização concedida e negada.

**Pré-requisitos:** Kind `dev`, contexto `kind-dev`, `kubectl`, `make`; namespace isolado `lab-02-02`. 

## Desafio — o que você vai construir

Crie uma ServiceAccount `lab-reader`, uma Role `pod-reader` permitindo apenas `get` e `list` sobre Pods e RoleBinding `pod-reader-binding` associando a identidade no namespace.

Antes de olhar `solution/`, formule uma hipótese sobre o comportamento e consulte `kubectl explain` quando necessário.

## Fase 1 — Preparar e prever

```bash
kubectl config current-context
make lab-prepare LAB=02.02
cat .labs/02.02/resources.yaml
```

Descreva quais objetos devem aparecer e qual observação confirmará sua hipótese.

## Fase 2 — Aplicar e observar

Complete os campos TODO no starter e execute:

```bash
kubectl apply -f .labs/02.02/
make lab-test LAB=02.02
make lab-observe LAB=02.02
```

Use `kubectl get sa,role,rolebinding -n lab-02-02` e `kubectl describe rolebinding pod-reader-binding -n lab-02-02`.

## Fase 3 — Experimento controlado

Execute `kubectl auth can-i list pods -n lab-02-02 --as=system:serviceaccount:lab-02-02:lab-reader` e depois troque `pods` por `secrets`. A impersonation exige credenciais locais com permissão apropriada.

## Resultado esperado e evidências

`list pods` retorna `yes`; `list secrets` retorna `no`. A ServiceAccount não recebe token compartilhado nem permissões globais.

**Evidências específicas:** registre o Role/RoleBinding criado e ambas as respostas de `can-i`, com namespace e identidade explícitos.

## Fase 4 — Diagnosticar

`kubectl describe role pod-reader -n lab-02-02` e `kubectl describe rolebinding pod-reader-binding -n lab-02-02`; confira o sujeito e as verbs.

Se a observação divergir, identifique primeiro **contexto → namespace → objeto → eventos → hipótese**, sem aplicar soluções aleatórias.

## Fase 5 — Limpar com segurança

```bash
make lab-down LAB=02.02
make lab-status LAB=02.02
```

A limpeza remove os objetos declarados no contrato e preserva o namespace. Desfaça explicitamente alterações manuais do experimento. **Não execute `make down`**, que remove o cluster Kind.

## Critérios de conclusão

- [ ] Completei o YAML sem copiar a solução e confirmei o contexto esperado.
- [ ] Observei o comportamento específico descrito em **Resultado esperado**.
- [ ] Registrei o resultado do experimento, uma hipótese e a explicação técnica.
- [ ] Removi os recursos do lab e revi qualquer alteração manual.

## Perguntas de diagnóstico e reflexão

- Por que uma Role não concede permissão sozinha?
- Como a identidade e o namespace afetam a resposta de `can-i`?

## Aprofunde seus conhecimentos

[Documentação oficial](https://kubernetes.io/docs/reference/access-authn-authz/rbac/) · [Aula 02.02](../../rbac-serviceaccount/README.md)

---

[← Lab 02.01](../labels-selectors-basico/README.md) · [↑ Camada 02](../../README.md) · [Próximo: Lab 02.03 →](../securitycontext-psa-basico/README.md)
