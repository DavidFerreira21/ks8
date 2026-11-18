# Lab 01.01 — Fundamentos: primeiro contato com a API Kubernetes

[← Aula 01.01](../../fundamentos/README.md) · [Guia de labs](../../../../docs/labs.md)

## Objetivo

Explorar um cluster Kind com Control Plane e Workers, identificar a API do Kubernetes e executar o ciclo **declarar → aplicar → observar → alterar → reaplicar → limpar**. Este laboratório começa com um ConfigMap, pois ainda não pressupõe conhecimento de Pods e Deployments.

**Ambiente:** Kind `dev`, contexto `kind-dev`, namespace `lab-fundamentos`. **Duração sugerida:** 15–25 minutos.

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
kubectl api-resources | head -25
kubectl explain configmap
kubectl explain configmap.data
```

Leia [configmap.yaml](configmap.yaml). Identifique `apiVersion`, `kind`, `metadata.name`, `metadata.namespace` e `data`.

**Conceito:** nem todo recurso tem `spec` e `status`; este ConfigMap contém dados de configuração e não cria um Pod.

## Fase 3 — Aplicar e testar

```bash
make lab-up LAB=01.01
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
kubectl apply --server-side --force-conflicts -f trilhas/01-fundamentos/labs/fundamentos-cluster/configmap.yaml
kubectl get configmap estado-desejado -n lab-fundamentos -o jsonpath='{.data.etapa}{"\n"}'
```

**Resultado esperado:** `primeira-versao`. Usamos server-side apply com `--force-conflicts` para explicitar que os campos declarados devem prevalecer sobre a alteração manual; o apply client-side normal pode não reverter drift em um campo que não mudou no arquivo desde a última aplicação. Compare com o arquivo. Explique a diferença entre **reaplicar manualmente** e **reconciliação contínua**, que estudaremos em controllers e GitOps. Este experimento é manual e não aparece em `make lab-experiment`.

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

- [ ] Identifico o Control Plane, os Workers e o contexto ativo.
- [ ] Sei consultar recursos e campos conhecidos pela API.
- [ ] Explico a diferença entre arquivo local e objeto persistido no cluster.
- [ ] Observei a alteração manual e sua reversão após reaplicar o manifesto.
- [ ] Limpei apenas o recurso criado neste laboratório.

**Próxima aula:** [01.02 — Pods](../../pods/README.md). Mais adiante, o [Lab 01.05](../primeira-aplicacao/README.md) demonstra controllers e réplicas.

[Referência oficial — Kubernetes Overview](https://kubernetes.io/docs/concepts/overview/) · [ConfigMaps](https://kubernetes.io/docs/concepts/configuration/configmap/)
