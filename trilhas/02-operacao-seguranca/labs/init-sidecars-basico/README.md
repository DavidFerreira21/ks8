# Lab 02.05 — Init Containers e sidecar nativo

[← Aula 02.05](../../init-sidecars/README.md) · [↑ Camada 02](../../README.md) · [🧪 Índice dos labs](../../../../docs/labs.md)

> **MODO DESAFIO:** `make lab-prepare LAB=02.05` cria o namespace e copia um **starter incompleto** para `.labs/02.05/resources.yaml`. Você completa o YAML e executa `kubectl apply -f .labs/02.05/`. Só então use `make lab-test LAB=02.05` e `make lab-observe LAB=02.05`. **`make lab-up` aplica a solução e é reservado à CI.**

## Objetivo e hipótese

Comprovar a ordem de inicialização de um init container comum e a permanência do sidecar nativo.

**Pré-requisitos:** Kind `dev`, contexto `kind-dev`, `kubectl`, `make`; namespace isolado `lab-02-05`. 

## Desafio — o que você vai construir

Crie um Pod `auxiliares` com um init container `preparo` que termina com sucesso, um sidecar nativo `observador` com `restartPolicy: Always` e um container principal `app`.

Antes de olhar `solution/`, formule uma hipótese sobre o comportamento e consulte `kubectl explain` quando necessário.

## Fase 1 — Preparar e prever

```bash
kubectl config current-context
make lab-prepare LAB=02.05
cat .labs/02.05/resources.yaml
```

Descreva quais objetos devem aparecer e qual observação confirmará sua hipótese.

## Fase 2 — Aplicar e observar

Complete os campos TODO no starter e execute:

```bash
kubectl apply -f .labs/02.05/
make lab-test LAB=02.05
make lab-observe LAB=02.05
```

Use `kubectl get pod auxiliares -n lab-02-05 -o yaml` e inspecione `status.initContainerStatuses`, `containerStatuses` e `kubectl logs auxiliares -c preparo -n lab-02-05`.

## Fase 3 — Experimento controlado

Registre os status inicial e os logs do init comum. **Recrie apenas o Pod didático** para observar novamente o ciclo de vida e compare as condições antes e depois:

```bash
kubectl get pod auxiliares -n lab-02-05 -o yaml
kubectl logs auxiliares -n lab-02-05 -c preparo
kubectl delete pod auxiliares -n lab-02-05
kubectl apply -f .labs/02.05/resources.yaml
kubectl get pod auxiliares -n lab-02-05 -w
```

Interrompa o `-w` com Ctrl+C quando o Pod estiver pronto. Depois inspecione `initContainerStatuses` e `containerStatuses`: o init comum deve terminar de novo, enquanto o sidecar nativo continua ativo. Essa recriação não exige encerrar outros workloads.

## Resultado esperado e evidências

`preparo` terminou com sucesso; o sidecar nativo e `app` continuam ativos. O sidecar aparece entre os initContainerStatuses por semântica nativa.

**Evidências específicas:** registre os status de cada container, o log de preparo e o estado do Pod para explicar a ordem da inicialização.

## Fase 4 — Diagnosticar

Se `app` não iniciar, inspecione eventos e o status do init; confira `restartPolicy` do sidecar e a versão da API do cluster.

Se a observação divergir, identifique primeiro **contexto → namespace → objeto → eventos → hipótese**, sem aplicar soluções aleatórias.

## Fase 5 — Limpar com segurança

```bash
make lab-down LAB=02.05
make lab-status LAB=02.05
```

A limpeza remove os objetos declarados no contrato e preserva o namespace. Desfaça explicitamente alterações manuais do experimento. **Não execute `make down`**, que remove o cluster Kind.

## Critérios de conclusão

- [ ] **Evidência funcional do Lab 02.05:** init container comum terminou duas vezes após a recriação, enquanto o sidecar nativo permaneceu ativo após cada inicialização.
- [ ] Completei o YAML sem copiar a solução e confirmei o contexto esperado.
- [ ] Observei o comportamento específico descrito em **Resultado esperado**.
- [ ] Registrei o resultado do experimento, uma hipótese e a explicação técnica.
- [ ] Removi os recursos do lab e revi qualquer alteração manual.

## Perguntas de diagnóstico e reflexão

- Por que um init container comum precisa terminar?
- Por que um sidecar nativo é definido em `initContainers`?

- Qual status evidencia que o sidecar nativo continua ativo após o init comum concluir?

## Aprofunde seus conhecimentos

[Documentação Kubernetes](https://kubernetes.io/docs/concepts/workloads/pods/sidecar-containers/) · [Aula 02.05](../../init-sidecars/README.md)

---

[← Lab 02.04](../quota-namespace/README.md) · [↑ Aula 02.05](../../init-sidecars/README.md) · [↑ Camada 02](../../README.md) · [Próximo: Lab 02.06 →](../jobs-cronjobs-basico/README.md)
