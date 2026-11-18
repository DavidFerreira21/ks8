# Lab 02.08 — Topology Spread Constraints

[← Aula 02.08](../../topology-spread/README.md) · [↑ Camada 02](../../README.md) · [🧪 Índice dos labs](../../../../docs/labs.md)

> **MODO DESAFIO:** `make lab-prepare LAB=02.08` cria o namespace e copia o starter **incompleto** em `.labs/02.08/resources.yaml`. Complete-o, execute `kubectl apply -f .labs/02.08/`, depois `make lab-test LAB=02.08` e `make lab-observe LAB=02.08`. **`make lab-up` aplica a solução e é exclusivo da CI.**

## Objetivo e hipótese

Distribuir duas réplicas de Deployment por hostname e observar decisões do scheduler.

**Pré-requisitos:** Kind `dev`, contexto `kind-dev`, `kubectl` e `make`; namespace exclusivo `lab-02-08`. 

## Desafio — o que você vai construir

Escreva Deployment `distribuida` com duas réplicas de nginx, selector e labels `app: distribuida` e topologySpreadConstraint para `kubernetes.io/hostname`, `maxSkew: 1`, `whenUnsatisfiable: DoNotSchedule`.

Preveja o que deve acontecer antes de abrir `solution/`. Use `kubectl explain` e a aula para esclarecer a API.

## Fase 1 — Preparar e prever

```bash
kubectl config current-context
make lab-prepare LAB=02.08
cat .labs/02.08/resources.yaml
```

## Fase 2 — Aplicar e observar

Complete os TODOs e execute:

```bash
kubectl apply -f .labs/02.08/
make lab-test LAB=02.08
make lab-observe LAB=02.08
```

Execute `kubectl rollout status deployment/distribuida -n lab-02-08 --timeout=180s`, seguido de `kubectl get pods -n lab-02-08 -o wide`.

## Fase 3 — Experimento controlado

Compare quantos Pods existem por worker. Depois reduza a réplicas 1 com `kubectl scale deployment/distribuida -n lab-02-08 --replicas=1` e observe a redistribuição; **restaure `--replicas=2`** antes de validar novamente.

## Resultado esperado e evidências

Com dois workers elegíveis e Ready, as duas réplicas tendem a ocupar hostnames distintos. Restrições e capacidade podem mudar o agendamento.

**Evidências específicas:** registre Deployment, hostnames efetivos das duas réplicas, a regra de `maxSkew` e a distribuição antes/depois da escala.

## Fase 4 — Diagnosticar

`kubectl describe pod -n lab-02-08 -l app=distribuida` e `kubectl get nodes --show-labels` para investigar domínios insuficientes.

Quando a observação não corresponder à hipótese, compare contexto, objetos, eventos e condições antes de modificar os manifests.

## Fase 5 — Limpar com segurança

```bash
make lab-down LAB=02.08
make lab-status LAB=02.08
```

O namespace é preservado; desfaça **separadamente** alterações manuais de nó, policies, Pods temporários e outros recursos criados fora do contrato. Não execute `make down`.

## Critérios de conclusão

- [ ] Completei o YAML sem copiar a solução e validei o contexto `kind-dev`.
- [ ] Observei a condição específica descrita no resultado esperado.
- [ ] Registrei a hipótese inicial, evidências e explicação técnica.
- [ ] Fiz a limpeza e desmanchei todas as alterações manuais.

## Perguntas de diagnóstico e reflexão

- Por que a restrição pode deixar um Pod Pending?
- Qual diferença há entre domínios por hostname e zonas de disponibilidade?

## Aprofunde seus conhecimentos

[Documentação Kubernetes](https://kubernetes.io/docs/concepts/scheduling-eviction/topology-spread-constraints/) · [Aula 02.08](../../topology-spread/README.md)

---

[← Lab 02.07](../scheduling-basico/README.md) · [↑ Camada 02](../../README.md) · [Próximo: Lab 02.09 →](../priorityclass-basico/README.md)
