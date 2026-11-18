# Lab 01.02 — Pods

[← Aula 01.02](../../pods/README.md) · [↑ Camada 01](../../README.md) · [🧪 Índice dos labs](../../../../docs/labs.md)

> **MODO DESAFIO — o aluno constrói:** `make lab-prepare LAB=01.02` cria apenas o namespace e copia um YAML incompleto para `.labs/01.02/`. **Complete o arquivo usando o objetivo abaixo**, aplique você mesmo com `kubectl apply -f .labs/01.02/` e só então execute `make lab-test LAB=01.02`. O comando `make lab-up` é reservado à CI. `make lab-solution LAB=01.02` mostra o caminho da referência quando você quiser conferir.


## Objetivo e hipótese

Pod é a unidade mínima de execução agendada. Hipótese: se eu excluir um Pod isolado, ele será recriado automaticamente?

**Ambiente:** cluster Kind `dev`, namespace isolado `lab-01-02`. Leia primeiro a aula teórica correspondente. Os experimentos são locais e manuais para você observar cada transição.

## Desafio — o que você vai construir

Escreva um `Pod` chamado `pod-demo`, no namespace `lab-01-02`, com um container `principal` usando `busybox:1.36`, comando que registre `pod-iniciado` e permaneça ativo, e `requests/limits` de CPU e memória. O Pod deve ser criado **sem Deployment ou ReplicaSet**.

**Antes de aplicar:** tente explicar o comportamento esperado sem consultar `solution/`. Se precisar, use `kubectl explain` ou a documentação abaixo. A solução de referência só deve ser consultada depois da tentativa.

## Fase 1 — Preparar e inspecionar

```bash
make doctor
kubectl config current-context
kubectl get nodes
make lab-prepare LAB=01.02
cat .labs/01.02/resources.yaml
```

Antes de aplicar, preveja quais objetos serão criados e quais controladores participarão.

## Fase 2 — Aplicar e observar

```bash
# Você já preparou o ambiente na Fase 1; complete agora o YAML local.
kubectl apply -f .labs/01.02/
make lab-test LAB=01.02
make lab-observe LAB=01.02
```

**Observe o agendamento:**

```bash
kubectl get pod pod-demo -n lab-01-02 -o wide
kubectl describe pod pod-demo -n lab-01-02
kubectl logs pod-demo -n lab-01-02
```

**Experimento — Pod sem controlador:** exclua apenas o Pod e observe que não reaparece sozinho:

```bash
kubectl delete pod pod-demo -n lab-01-02
kubectl get pods -n lab-01-02
kubectl apply -f .labs/01.02/
make lab-test LAB=01.02
```

Por que o Deployment da aula seguinte responde de forma diferente?

## Resultado esperado e evidências

- Antes da exclusão, `pod-demo` fica `Running` e `Ready` (após o agendamento); os logs contêm `pod-iniciado`.
- Depois de `kubectl delete pod`, o recurso desaparece e **nenhum controlador recria outro**; `make lab-test` falharia nesse momento.
- Reaplicar seu próprio YAML recria o Pod e permite passar no teste. Compare o comportamento com o Lab 01.03.

**Se o resultado divergir:** consulte `kubectl describe`, `kubectl get events` e os logs quando existirem Pods. Diferencie erro de YAML, problema no cluster e comportamento intencional do experimento.

## Fase 3 — Diagnosticar

```bash
kubectl get events -n lab-01-02 --sort-by=.lastTimestamp
kubectl get all -n lab-01-02
```

Investigue com `kubectl describe` e, quando houver Pod, `kubectl logs`. Compare estado desejado, readiness e eventos. `make lab-test` confere os checks e os campos declarados na solução de referência, mas não substitui sua investigação.

## Fase 4 — Limpar com segurança

```bash
make lab-down LAB=01.02
make lab-status LAB=01.02
```

O namespace é preservado por segurança. Não use `make down` para limpar um único lab.

## Critérios de conclusão

- [ ] Escrevi o manifesto `Pod` sem copiar a solução.
- [ ] Identifiquei nó, status e mensagem de log do `pod-demo`.
- [ ] Confirmei que um Pod isolado não é recriado após a exclusão.
- [ ] Reapliquei meu YAML e fiz a limpeza do lab.

## Perguntas de diagnóstico e reflexão

- Qual o efeito de excluir um Pod avulso e como isso contrasta com um Pod gerenciado por controlador?
- Que evento ou campo permitiu identificar o motivo de o container estar pronto (ou não)?

**Evidências específicas:** registre o YAML do Pod, seu estado/eventos e o comportamento após exclusão ou alteração. Diferencie Pod avulso de Pod sob controlador.

## Aprofunde seus conhecimentos

[Pods](https://kubernetes.io/docs/concepts/workloads/pods/) · [Ciclo de vida do Pod](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/) · [Depuração de Pods](https://kubernetes.io/docs/tasks/debug/debug-application/debug-pods/).

Use essas referências para entender **por que** o Kubernetes se comportou assim; depois compare com a [aula teórica](../../pods/README.md).

---

[← Lab 01.01](../fundamentos-cluster/README.md) · [↑ Aula 01.02](../../pods/README.md) · [Próximo: Lab 01.03 →](../deployments-basico/README.md)
