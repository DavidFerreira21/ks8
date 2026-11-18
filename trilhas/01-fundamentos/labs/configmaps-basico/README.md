# Lab 01.07 — ConfigMaps

[← Aula 01.07](../../configmaps/README.md) · [↑ Camada 01](../../README.md) · [🧪 Índice dos labs](../../../../docs/labs.md)

> **MODO DESAFIO:** execute `make lab-prepare LAB=01.07` para criar o namespace e copiar um arquivo incompleto para `.labs/01.07/resources.yaml`. **Escreva os campos TODO, aplique você mesmo com `kubectl apply -f .labs/01.07/` e valide com `make lab-test LAB=01.07`**. `make lab-up` é só para CI. Use `make lab-solution LAB=01.07` apenas depois de tentar.


## Hipótese e objetivo

ConfigMaps desacoplam a configuração da imagem; variáveis de ambiente de Pods existentes não se atualizam automaticamente.

**Ambiente:** Kind `dev` em namespace `lab-01-07`. Execute somente no cluster de estudos.

## Fase 1 — Inspecionar

```bash
kubectl config current-context
kubectl get nodes
make lab-prepare LAB=01.07
cat .labs/01.07/resources.yaml
```

Preveja quais recursos aparecerão.

## Fase 2 — Aplicar e testar

```bash
make lab-prepare LAB=01.07
# Complete o manifesto em .labs/01.07/resources.yaml
kubectl apply -f .labs/01.07/
make lab-test LAB=01.07
make lab-observe LAB=01.07
```

**Observe o valor injetado no Pod:**

```bash
kubectl logs deployment/consumidor -n lab-01-07
kubectl get configmap app-config -n lab-01-07 -o yaml
```

**Experimento — configuração muda, ambiente do container não:**

```bash
kubectl patch configmap app-config -n lab-01-07 --type merge -p '{"data":{"MENSAGEM":"versao-2"}}'
kubectl logs deployment/consumidor -n lab-01-07
kubectl rollout restart deployment/consumidor -n lab-01-07
kubectl rollout status deployment/consumidor -n lab-01-07
kubectl logs deployment/consumidor -n lab-01-07
```

Ao fazer restart, a nova variável de ambiente deve ser consumida. Para restaurar `versao-1` após o patch, use **server-side apply com resolução explícita de conflito**, pois o apply client-side pode manter campos alterados fora do histórico local:

```bash
kubectl apply --server-side --force-conflicts -f .labs/01.07/resources.yaml
kubectl rollout restart deployment/consumidor -n lab-01-07
kubectl rollout status deployment/consumidor -n lab-01-07
kubectl logs deployment/consumidor -n lab-01-07
```

## Fase 3 — Diagnóstico

```bash
kubectl get events -n lab-01-07 --sort-by=.lastTimestamp
kubectl get all -n lab-01-07
```

Compare os campos do YAML com o comportamento observado. A verificação automática não substitui a análise do aluno.

## Fase 4 — Limpeza

```bash
make lab-down LAB=01.07
make lab-status LAB=01.07
```

Namespace preservado; não use `make down` para limpar um único exercício.

## Conclusão

- [ ] Identifiquei recursos e suas dependências.
- [ ] Executei a experiência e comparei resultados.
- [ ] Consultei eventos e conditions quando aplicáveis.
- [ ] Limpei os recursos criados.

---

[← Lab 01.06](../namespaces-basico/README.md) · [↑ Aula 01.07](../../configmaps/README.md) · [Próximo: Lab 01.08 →](../secrets-basico/README.md)
