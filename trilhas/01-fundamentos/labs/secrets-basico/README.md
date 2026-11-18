# Lab 01.08 — Secrets: referencia e consumo seguro

> **MODO DESAFIO:** execute `make lab-prepare LAB=01.08` para criar o namespace e copiar um arquivo incompleto para `.labs/01.08/resources.yaml`. **Escreva os campos TODO, aplique você mesmo com `kubectl apply -f .labs/01.08/` e valide com `make lab-test LAB=01.08`**. `make lab-up` é só para CI. Use `make lab-solution LAB=01.08` apenas depois de tentar.

[← Camada 01](../../README.md) · [Labs](../../../../docs/labs.md)

## Hipótese e objetivo

Um Secret permite referenciar informações sensíveis sem embuti-las no Pod spec, mas sua existência não implica armazenamento criptografado por padrão.

**Ambiente:** Kind `dev` em namespace `lab-01-08`. Execute somente no cluster de estudos.

## Fase 1 — Inspecionar

```bash
kubectl config current-context
kubectl get nodes
cat .labs/01.08/resources.yaml
```

Preveja quais recursos aparecerão.

## Fase 2 — Aplicar e testar

```bash
make lab-prepare LAB=01.08
# Complete o manifesto em .labs/01.08/resources.yaml
kubectl apply -f .labs/01.08/
make lab-test LAB=01.08
make lab-observe LAB=01.08
```

**Observe a referência sem imprimir o valor:**

```bash
kubectl get secret exemplo-ficticio -n lab-01-08
kubectl describe deployment consumidor -n lab-01-08
kubectl logs deployment/consumidor -n lab-01-08
kubectl exec -n lab-01-08 deployment/consumidor -- sh -c 'test -n "$TOKEN_DEMO" && echo variavel-presente'
```

**Experimento — dependência:** remova temporariamente apenas o Secret após criar o Deployment; reinicie o Deployment e observe eventos indicando a chave ausente. Reaplique o manifesto e faça outro restart para recuperar:

```bash
kubectl delete secret exemplo-ficticio -n lab-01-08
kubectl rollout restart deployment/consumidor -n lab-01-08
kubectl get pods -n lab-01-08
kubectl get events -n lab-01-08 --sort-by=.lastTimestamp
kubectl apply -f .labs/01.08/resources.yaml
kubectl rollout restart deployment/consumidor -n lab-01-08
make lab-test LAB=01.08
```

**Segurança:** o manifesto contém somente dado fictício, público e sem valor. Nunca versione credenciais reais; base64 não é criptografia e a proteção de Secrets depende de RBAC, criptografia em repouso e controles operacionais.

## Fase 3 — Diagnóstico

```bash
kubectl get events -n lab-01-08 --sort-by=.lastTimestamp
kubectl get all -n lab-01-08
```

Compare os campos do YAML com o comportamento observado. A verificação automática não substitui a análise do aluno.

## Fase 4 — Limpeza

```bash
make lab-down LAB=01.08
make lab-status LAB=01.08
```

Namespace preservado; não use `make down` para limpar um único exercício.

## Conclusão

- [ ] Identifiquei recursos e suas dependências.
- [ ] Executei a experiência e comparei resultados.
- [ ] Consultei eventos e conditions quando aplicáveis.
- [ ] Limpei os recursos criados.
