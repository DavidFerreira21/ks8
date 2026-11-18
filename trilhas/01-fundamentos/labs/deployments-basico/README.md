# Lab 01.03 — Deployments

[← Aula 01.03](../../deployments/README.md) · [↑ Camada 01](../../README.md) · [🧪 Índice dos labs](../../../../docs/labs.md)

> **MODO DESAFIO — o aluno constrói:** `make lab-prepare LAB=01.03` cria apenas o namespace e copia um YAML incompleto para `.labs/01.03/`. **Complete o arquivo usando o objetivo abaixo**, aplique você mesmo com `kubectl apply -f .labs/01.03/` e só então execute `make lab-test LAB=01.03`. O comando `make lab-up` é reservado à CI. `make lab-solution LAB=01.03` mostra o caminho da referência quando você quiser conferir.


## Objetivo e hipótese

O Deployment controla um ReplicaSet, que mantém a quantidade declarada de Pods. Hipótese: excluir uma réplica resulta na criação de outra?

**Ambiente:** cluster Kind `dev`, namespace isolado `lab-01-03`. Leia primeiro a aula teórica correspondente. Os experimentos são locais e manuais para você observar cada transição.

## Desafio — o que você vai construir

Escreva um `Deployment` chamado `web`, com **3 réplicas**, container `nginx:1.27`, porta 80 e labels/selector compatíveis (`app: web-0103`). Defina recursos mínimos de CPU/memória. O cluster deve criar os Pods via ReplicaSet, não manualmente.

**Antes de aplicar:** tente explicar o comportamento esperado sem consultar `solution/`. Se precisar, use `kubectl explain` ou a documentação abaixo. A solução de referência só deve ser consultada depois da tentativa.

## Fase 1 — Preparar e inspecionar

```bash
make doctor
kubectl config current-context
kubectl get nodes
make lab-prepare LAB=01.03
cat .labs/01.03/resources.yaml
```

Antes de aplicar, preveja quais objetos serão criados e quais controladores participarão.

## Fase 2 — Aplicar e observar

```bash
# Você já preparou o ambiente na Fase 1; complete agora o YAML local.
kubectl apply -f .labs/01.03/
make lab-test LAB=01.03
make lab-observe LAB=01.03
```

**Observe a cadeia Deployment → ReplicaSet → Pods:**

```bash
kubectl get deployment,replicaset,pods -n lab-01-03 -o wide
kubectl describe deployment web -n lab-01-03
```

**Experimento — recuperar uma réplica:** em outro terminal, execute `kubectl get pods -n lab-01-03 -w`. Depois exclua somente o primeiro Pod retornado:

```bash
POD=$(kubectl get pods -n lab-01-03 -l app=web-0103 -o jsonpath='{.items[0].metadata.name}')
kubectl delete pod "$POD" -n lab-01-03
kubectl rollout status deployment/web -n lab-01-03
kubectl get pods,replicasets -n lab-01-03
```

Compare com o Pod isolado do lab 01.02. Para observar escalabilidade, execute `kubectl scale deployment/web -n lab-01-03 --replicas=2`; depois restaure com `kubectl scale deployment/web -n lab-01-03 --replicas=3` e confirme o estado desejado.

## Resultado esperado e evidências

- `kubectl get deployment,replicaset,pods` mostra **1 Deployment, 1 ReplicaSet e 3 Pods disponíveis** após o rollout.
- Ao excluir um dos Pods, outro é criado com **nome/UID diferente**, mantendo a contagem desejada em 3.
- Se fizer o experimento de `kubectl scale ... --replicas=2`, verá 2 Pods; reconfigure de volta para 3 e aguarde `kubectl rollout status` antes de validar.

**Se o resultado divergir:** consulte `kubectl describe`, `kubectl get events` e os logs quando existirem Pods. Diferencie erro de YAML, problema no cluster e comportamento intencional do experimento.

## Fase 3 — Diagnosticar

```bash
kubectl get events -n lab-01-03 --sort-by=.lastTimestamp
kubectl get all -n lab-01-03
```

Investigue com `kubectl describe` e, quando houver Pod, `kubectl logs`. Compare estado desejado, readiness e eventos. `make lab-test` confere os checks e os campos declarados na solução de referência, mas não substitui sua investigação.

## Fase 4 — Limpar com segurança

```bash
make lab-down LAB=01.03
make lab-status LAB=01.03
```

O namespace é preservado por segurança. Não use `make down` para limpar um único lab.

## Critérios de conclusão

- [ ] Expliquei a relação Deployment → ReplicaSet → Pods.
- [ ] Vi três réplicas disponíveis no estado inicial.
- [ ] Excluí um Pod e identifiquei o Pod substituto.
- [ ] Restaurei as três réplicas e limpei os recursos do lab.

## Perguntas de diagnóstico e reflexão

- Que recurso recriou o Pod após a exclusão, e como você comprovou isso?
- Como `readyReplicas` se relaciona ao número de réplicas desejadas do Deployment?

**Evidências mínimas:** manifeste o recurso criado, registre um resultado observável do experimento e explique a causa desse comportamento. Se divergir, documente o diagnóstico antes da limpeza.

## Aprofunde seus conhecimentos

[Deployments](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/) · [ReplicaSet](https://kubernetes.io/docs/concepts/workloads/controllers/replicaset/) · [Operações de atualização](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/#updating-a-deployment).

Use essas referências para entender **por que** o Kubernetes se comportou assim; depois compare com a [aula teórica](../../deployments/README.md).

---

[← Lab 01.02](../pods-basico/README.md) · [↑ Aula 01.03](../../deployments/README.md) · [Próximo: Lab 01.04 →](../controladores-basico/README.md)
