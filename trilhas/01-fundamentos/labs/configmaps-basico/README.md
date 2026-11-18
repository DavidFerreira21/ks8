# Lab 01.07 — ConfigMaps: configuracao da aplicacao

[← Camada 01](../../README.md) · [Labs](../../../../docs/labs.md)

## Hipótese e objetivo

ConfigMaps desacoplam a configuração da imagem; variáveis de ambiente de Pods existentes não se atualizam automaticamente.

**Ambiente:** Kind `dev` em namespace `lab-01-07`. Execute somente no cluster de estudos.

## Fase 1 — Inspecionar

```bash
kubectl config current-context
kubectl get nodes
cat trilhas/01-fundamentos/labs/configmaps-basico/resources.yaml
```

Preveja quais recursos aparecerão.

## Fase 2 — Aplicar e testar

```bash
make lab-up LAB=01.07
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
kubectl apply --server-side --force-conflicts -f trilhas/01-fundamentos/labs/configmaps-basico/resources.yaml
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
