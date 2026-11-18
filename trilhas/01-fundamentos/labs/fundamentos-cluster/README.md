# Lab 01.01 — Fundamentos Kubernetes

[← Aula 01.01](../../fundamentos/README.md) · [↑ Camada 01](../../README.md) · [🧪 Índice dos labs](../../../../docs/labs.md)

> **MODO DESAFIO — o aluno constrói:** `make lab-prepare LAB=01.01` cria apenas o namespace e copia um YAML incompleto para `.labs/01.01/`. **Complete o arquivo usando o objetivo abaixo**, aplique você mesmo com `kubectl apply -f .labs/01.01/` e só então execute `make lab-test LAB=01.01`. O comando `make lab-up` é reservado à CI. `make lab-solution LAB=01.01` mostra o caminho da referência quando você quiser conferir.


## Objetivo

Explorar um cluster Kind com Control Plane e Workers, identificar a API do Kubernetes e executar o ciclo **declarar → aplicar → observar → alterar → reaplicar → limpar**. Este laboratório começa com um ConfigMap, pois ainda não pressupõe conhecimento de Pods e Deployments.

**Ambiente:** Kind `dev`, contexto `kind-dev`, namespace `lab-fundamentos`. **Duração sugerida:** 15–25 minutos.

## Desafio — o que você vai construir

Crie um `ConfigMap` chamado `estado-desejado`, no namespace `lab-fundamentos`, com a chave `data.etapa` igual a `primeira-versao`. Reconheça `apiVersion`, `kind`, `metadata` e `data`; não há `spec.containers` nesse objeto.

**Antes de aplicar:** tente explicar o comportamento esperado sem consultar `solution/`. Se precisar, use `kubectl explain` ou a documentação abaixo. A solução de referência só deve ser consultada depois da tentativa.

## Fase 1 — Conhecer o cluster

Antes de aplicar algo, responda: quem recebe requisições Kubernetes? Onde os workloads rodam? O que diferencia Control Plane de Worker?

```bash
make doctor
kubectl config current-context
kubectl cluster-info
kubectl get nodes -o wide
kubectl get pods -A
```

**Observe:** quantos nós estão `Ready`? Qual é o Control Plane? Quais componentes aparecem em `kube-system`? No perfil Kind padrão deste projeto, são esperados um Control Plane e dois Workers.

## Fase 2 — Conhecer os objetos da API

```bash
make lab-prepare LAB=01.01
kubectl api-resources | head -25
kubectl explain configmap
kubectl explain configmap.data
```

Leia o arquivo incompleto `.labs/01.01/configmap.yaml` (gerado pelo comando da fase anterior). Identifique `apiVersion`, `kind`, `metadata.name`, `metadata.namespace` e `data`.

**Conceito:** nem todo recurso tem `spec` e `status`; este ConfigMap contém dados de configuração e não cria um Pod.

## Fase 3 — Aplicar e testar

```bash
# Complete primeiro o arquivo em .labs/01.01/
kubectl apply -f .labs/01.01/
make lab-test LAB=01.01
kubectl get configmap estado-desejado -n lab-fundamentos -o yaml
```

**Observe:** o nome, o namespace, os valores de `data` e os metadados gerados pelo servidor. O teste automático comprova que o ConfigMap existe — a interpretação do resultado é sua.

## Fase 4 — Experimento: mudança manual vs manifesto

Faça uma hipótese: se alterarmos os dados diretamente no cluster, o arquivo YAML local reverterá a mudança sozinho?

```bash
kubectl patch configmap estado-desejado -n lab-fundamentos --type merge -p '{"data":{"etapa":"alteracao-manual"}}'
kubectl get configmap estado-desejado -n lab-fundamentos -o jsonpath='{.data.etapa}{"\n"}'
```

Espere alguns segundos e consulte o valor novamente. **Ele não será revertido espontaneamente apenas porque existe um YAML no Git**. Neste lab não há um reconciliador GitOps observando o arquivo.

Agora reaplique a intenção local:

```bash
kubectl apply --server-side --force-conflicts -f .labs/01.01/configmap.yaml
kubectl get configmap estado-desejado -n lab-fundamentos -o jsonpath='{.data.etapa}{"\n"}'
```

**Resultado esperado:** `primeira-versao`. Usamos server-side apply com `--force-conflicts` para explicitar que os campos declarados devem prevalecer sobre a alteração manual; o apply client-side normal pode não reverter drift em um campo que não mudou no arquivo desde a última aplicação. Compare com o arquivo. Explique a diferença entre **reaplicar manualmente** e **reconciliação contínua**, que estudaremos em controllers e GitOps. Este experimento é manual e não aparece em `make lab-experiment`.

## Resultado esperado e evidências

- `kubectl get configmap estado-desejado -n lab-fundamentos` retorna o recurso, mas **nenhum Pod novo** é criado.
- Após o patch, `data.etapa` mostra `alteracao-manual`; esperar não muda o valor por conta própria.
- Após reaplicar o YAML com server-side apply conforme o roteiro, o valor retorna a `primeira-versao`. Registre os dois valores como evidência.

**Se o resultado divergir:** consulte `kubectl describe`, `kubectl get events` e os logs quando existirem Pods. Diferencie erro de YAML, problema no cluster e comportamento intencional do experimento.

## Fase 5 — Observar, diagnosticar e limpar

```bash
make lab-observe LAB=01.01
kubectl describe configmap estado-desejado -n lab-fundamentos
kubectl get events -n lab-fundamentos
make lab-down LAB=01.01
make lab-status LAB=01.01
```

É normal não haver novos Pods nem eventos de scheduling: o objeto aplicado é um ConfigMap. O namespace permanece, mas o ConfigMap é removido. Se receber `Forbidden` ou falha de conexão, não confunda com `NotFound`.

## Critérios de conclusão

- [ ] Identifiquei Control Plane, Workers e o contexto `kind-dev`.
- [ ] Criei um ConfigMap e confirmei `data.etapa=primeira-versao`.
- [ ] Expliquei por que a alteração manual não foi revertida automaticamente.
- [ ] Reapliquei o YAML, confirmei o valor original e removi apenas o ConfigMap.

**Próxima aula:** [Aula 01.02 — Pods](../../pods/README.md). O [🧪 Lab 01.05](../services-basico/README.md) aborda Services e descoberta de backends.

## Perguntas de diagnóstico e reflexão

- Qual evidência mostra que um objeto foi aceito pelo API Server, mas o estado esperado ainda não foi observado?
- Como a leitura de `spec` e `status` mudou sua hipótese sobre reconciliação?

**Evidências específicas:** capture o contexto e os nós do Kind, o objeto declarado e seu `spec`/`status` antes e depois da alteração manual. Explique a reconciliação observada.

## Aprofunde seus conhecimentos

[Conceitos básicos e arquitetura](https://kubernetes.io/docs/concepts/overview/) · [ConfigMaps](https://kubernetes.io/docs/concepts/configuration/configmap/) · [Gerenciamento declarativo de objetos](https://kubernetes.io/docs/tasks/manage-kubernetes-objects/declarative-config/).

Use essas referências para entender **por que** o Kubernetes se comportou assim; depois compare com a [aula teórica](../../fundamentos/README.md).

---

[↑ Aula 01.01](../../fundamentos/README.md) · [Próximo: Lab 01.02 →](../pods-basico/README.md)
