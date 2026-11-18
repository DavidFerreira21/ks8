# Lab 01.07 — ConfigMaps

[← Aula 01.07](../../configmaps/README.md) · [↑ Camada 01](../../README.md) · [🧪 Índice dos labs](../../../../docs/labs.md)

> **MODO DESAFIO:** execute `make lab-prepare LAB=01.07` para criar o namespace e copiar um arquivo incompleto para `.labs/01.07/resources.yaml`. **Escreva os campos TODO, aplique você mesmo com `kubectl apply -f .labs/01.07/` e valide com `make lab-test LAB=01.07`**. `make lab-up` é só para CI. Use `make lab-solution LAB=01.07` apenas depois de tentar.


## Objetivo e hipótese

ConfigMaps desacoplam a configuração da imagem; variáveis de ambiente de Pods existentes não se atualizam automaticamente.

**Ambiente:** Kind `dev` em namespace `lab-01-07`. Execute somente no cluster de estudos.

## Desafio — o que você vai construir

No arquivo de exercício, escreva **dois documentos YAML**: um `ConfigMap` chamado `app-config` com `MENSAGEM: versao-1` e um Deployment `consumidor` que lê essa chave por `envFrom.configMapRef`. O container deve registrar o valor no log e permanecer ativo.

**Antes de aplicar:** use o arquivo incompleto em `.labs/01.07/` como ponto de partida. Confira campos com `kubectl explain`; não abra a solução antes de formular uma tentativa.

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

## Resultado esperado e evidências

- No primeiro log do Deployment aparece `MENSAGEM=versao-1`.
- Alterar o ConfigMap para `versao-2` **não modifica variáveis de ambiente de containers já iniciados**; o log anterior permanece.
- Após reiniciar o Deployment, os Pods novos recebem `versao-2`. Reaplicar o valor original e reiniciar novamente restaura `versao-1`.

**Se o resultado divergir:** confirme contexto, namespace, eventos e o YAML escrito. Diferencie comportamento intencional do experimento e erro na sua configuração.

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

## Critérios de conclusão

- [ ] Criei ConfigMap e Deployment com referência válida.
- [ ] Vi `MENSAGEM=versao-1` nos logs iniciais.
- [ ] Confirmei a necessidade de reiniciar Pods que consomem ConfigMap como variável de ambiente.
- [ ] Restaurei o conteúdo do YAML e removi os recursos declarados.

## Perguntas de diagnóstico e reflexão

- Por que um Pod já existente não recebeu automaticamente a nova variável de ambiente?
- O que mudou nos logs após reiniciar o Deployment e como você registrou a diferença?

**Evidências mínimas:** manifeste o recurso criado, registre um resultado observável do experimento e explique a causa desse comportamento. Se divergir, documente o diagnóstico antes da limpeza.

## Aprofunde seus conhecimentos

[ConfigMaps](https://kubernetes.io/docs/concepts/configuration/configmap/) · [Configurar Pod com ConfigMap](https://kubernetes.io/docs/tasks/configure-pod-container/configure-pod-configmap/) · [Variáveis de ambiente no Pod](https://kubernetes.io/docs/tasks/inject-data-application/define-environment-variable-container/).

Releia a [aula teórica](../../configmaps/README.md) e compare os exemplos com o que você observou no cluster.

---

[← Lab 01.06](../namespaces-basico/README.md) · [↑ Aula 01.07](../../configmaps/README.md) · [Próximo: Lab 01.08 →](../secrets-basico/README.md)
