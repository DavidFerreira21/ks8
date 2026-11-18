# Lab 02.06 — Jobs e CronJobs

[← Aula 02.06](../../jobs-cronjobs/README.md) · [↑ Camada 02](../../README.md) · [🧪 Índice dos labs](../../../../docs/labs.md)

> **MODO DESAFIO:** `make lab-prepare LAB=02.06` cria o namespace e copia um **starter incompleto** para `.labs/02.06/resources.yaml`. Você completa o YAML e executa `kubectl apply -f .labs/02.06/`. Só então use `make lab-test LAB=02.06` e `make lab-observe LAB=02.06`. **`make lab-up` aplica a solução e é reservado à CI.**

## Objetivo e hipótese

Concluir um Job e compreender como um CronJob cria execuções programadas.

**Pré-requisitos:** Kind `dev`, contexto `kind-dev`, `kubectl`, `make`; namespace isolado `lab-02-06`. 

## Desafio — o que você vai construir

Crie Job `tarefa` com BusyBox que escreve mensagem e encerra com código zero; crie CronJob `agenda` agendado a cada cinco minutos, com `concurrencyPolicy: Forbid` e JobTemplate equivalente.

Antes de olhar `solution/`, formule uma hipótese sobre o comportamento e consulte `kubectl explain` quando necessário.

## Fase 1 — Preparar e prever

```bash
kubectl config current-context
make lab-prepare LAB=02.06
cat .labs/02.06/resources.yaml
```

Descreva quais objetos devem aparecer e qual observação confirmará sua hipótese.

## Fase 2 — Aplicar e observar

Complete os campos TODO no starter e execute:

```bash
kubectl apply -f .labs/02.06/
make lab-test LAB=02.06
make lab-observe LAB=02.06
```

Execute `kubectl get jobs,cronjobs -n lab-02-06` e `kubectl logs job/tarefa -n lab-02-06`. Aguarde `kubectl wait --for=condition=complete job/tarefa -n lab-02-06 --timeout=120s`.

## Fase 3 — Experimento controlado

Para não esperar o relógio, crie uma execução pontual com `kubectl create job agenda-manual -n lab-02-06 --from=cronjob/agenda`; observe sua conclusão e remova com `kubectl delete job agenda-manual -n lab-02-06`. Essa execução não altera o CronJob.

## Resultado esperado e evidências

Job `tarefa` aparece `Complete`; CronJob tem agenda configurada; a execução manual cria outro Job e Pod, com ownerReferences adequados.

**Evidências específicas:** registre condição Complete, logs de Job, expressão cron, política de concorrência e a criação/remoção da execução manual.

## Fase 4 — Diagnosticar

Se um Job não completar, veja `kubectl describe job tarefa -n lab-02-06` e logs do Pod correspondente; não espere que o CronJob execute imediatamente.

Se a observação divergir, identifique primeiro **contexto → namespace → objeto → eventos → hipótese**, sem aplicar soluções aleatórias.

## Fase 5 — Limpar com segurança

```bash
make lab-down LAB=02.06
make lab-status LAB=02.06
```

A limpeza remove os objetos declarados no contrato e preserva o namespace. Desfaça explicitamente alterações manuais do experimento. **Não execute `make down`**, que remove o cluster Kind.

## Critérios de conclusão

- [ ] Completei o YAML sem copiar a solução e confirmei o contexto esperado.
- [ ] Observei o comportamento específico descrito em **Resultado esperado**.
- [ ] Registrei o resultado do experimento, uma hipótese e a explicação técnica.
- [ ] Removi os recursos do lab e revi qualquer alteração manual.

## Perguntas de diagnóstico e reflexão

- Por que Job terminado não deve ser transformado em Deployment?
- Qual risco operacional é mitigado por `concurrencyPolicy: Forbid`?

## Aprofunde seus conhecimentos

[Documentação oficial](https://kubernetes.io/docs/concepts/workloads/controllers/cron-jobs/) · [Aula 02.06](../../jobs-cronjobs/README.md)

---

[← Lab 02.05](../init-sidecars-basico/README.md) · [↑ Camada 02](../../README.md) · [Próximo: Lab 02.07 →](../scheduling-basico/README.md)
