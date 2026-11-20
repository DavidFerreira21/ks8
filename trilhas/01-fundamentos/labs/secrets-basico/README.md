# Lab 01.08 — Secrets

[← Aula 01.08](../../secrets/README.md) · [↑ Camada 01](../../README.md) · [🧪 Índice dos labs](../../../../docs/labs.md)

> **MODO DESAFIO:** execute `make lab-prepare LAB=01.08` para criar o namespace e copiar um arquivo incompleto para `.labs/01.08/resources.yaml`. **Escreva os campos TODO, aplique você mesmo com `kubectl apply -f .labs/01.08/` e valide com `make lab-test LAB=01.08`**. `make lab-up` é só para CI. Use `make lab-solution LAB=01.08` apenas depois de tentar.


## Objetivo e hipótese

Um Secret permite referenciar informações sensíveis sem embuti-las no Pod spec, mas sua existência não implica armazenamento criptografado por padrão.

**Ambiente:** Kind `dev` em namespace `lab-01-08`. Execute somente no cluster de estudos.

## Desafio — o que você vai construir

Escreva um `Secret` Opaque chamado `exemplo-ficticio`, usando **apenas** o valor fictício `valor-ficticio-para-estudo` na chave `TOKEN_DEMO` (nenhuma credencial real), e um Deployment `consumidor` que injeta `TOKEN_DEMO` por `secretKeyRef`. O container **não deve imprimir o token** em logs ou comandos do roteiro.

**Antes de aplicar:** use o arquivo incompleto em `.labs/01.08/` como ponto de partida. Confira campos com `kubectl explain`; não abra a solução antes de formular uma tentativa.

## Fase 1 — Inspecionar

```bash
kubectl config current-context
kubectl get nodes
make lab-prepare LAB=01.08
cat .labs/01.08/resources.yaml
```

Preveja quais recursos aparecerão.

## Fase 2 — Aplicar e testar

```bash
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

## Resultado esperado e evidências

- O Secret existe e o Deployment consegue iniciar seu container consumindo a variável; o comando de teste imprime somente `variavel-presente`.
- Se o Secret for excluído e um novo Pod precisar iniciar, podem aparecer eventos como `CreateContainerConfigError` ou falha de resolução da referência.
- Recriar o Secret fictício e reiniciar/reconciliar os Pods restaura o funcionamento. **Base64 não garante sigilo** nem substitui RBAC e criptografia em repouso.

**Se o resultado divergir:** confirme contexto, namespace, eventos e o YAML escrito. Diferencie comportamento intencional do experimento e erro na sua configuração.

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

## Critérios de conclusão

- [ ] Usei somente dados fictícios no Secret de estudo.
- [ ] Configurei `secretKeyRef` para a chave `TOKEN_DEMO` sem registrar o valor.
- [ ] Observei a falha da dependência ausente e a recuperação.
- [ ] Identifiquei controles adicionais necessários para Secrets em produção.

## Perguntas de diagnóstico e reflexão

- Qual evidência mostra que o Secret foi consumido sem expor o valor em logs ou em arquivos versionados?
- Por que base64 não protege uma credencial contra alguém autorizado a ler o Secret?

**Evidências específicas:** registre a criação e o consumo do Secret usando somente metadados, status e verificações que não revelem seu valor; explique por que base64 não é criptografia.

- Qual risco existe ao imprimir `kubectl get secret -o yaml` no terminal de uma pipeline, mesmo sem decodificar base64?

## Aprofunde seus conhecimentos

[Secrets](https://kubernetes.io/docs/concepts/configuration/secret/) · [Distribuir credenciais com segurança](https://kubernetes.io/docs/tasks/inject-data-application/distribute-credentials-secure/) · [Boas práticas para Secrets](https://kubernetes.io/docs/concepts/security/secrets-good-practices/).

Releia a [aula teórica](../../secrets/README.md) e compare os exemplos com o que você observou no cluster.

---

[← Lab 01.07](../configmaps-basico/README.md) · [↑ Aula 01.08](../../secrets/README.md) · [Próximo: Lab 01.09 →](../requests-limits-basico/README.md)
