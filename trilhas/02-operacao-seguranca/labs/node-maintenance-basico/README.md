# Lab 02.12 — Node Maintenance — Cordon e Uncordon

[← Aula 02.12](../../node-maintenance/README.md) · [↑ Camada 02](../../README.md) · [🧪 Índice dos labs](../../../../docs/labs.md)

> **MODO DESAFIO:** `make lab-prepare LAB=02.12` cria o namespace e copia o starter **incompleto** em `.labs/02.12/resources.yaml`. Complete-o, execute `kubectl apply -f .labs/02.12/`, depois `make lab-test LAB=02.12` e `make lab-observe LAB=02.12`. **`make lab-up` aplica a solução e é exclusivo da CI.**

## Objetivo e hipótese

Observar um worker marcado como unschedulable e restaurá-lo, distinguindo cordon de drain.

**Pré-requisitos:** Kind `dev`, contexto `kind-dev`, `kubectl` e `make`; namespace exclusivo `lab-02-12`. **Ação em nó:** execute somente no cluster descartável. Este lab faz cordon/uncordon manual e não simula drain; exige worker `dev-worker`.

## Desafio — o que você vai construir

Crie Pod `manutencao` com BusyBox agendável no worker `dev-worker` por `nodeSelector`. O experimento de cordon/uncordon ocorrerá separadamente sobre o nó Kind.

Preveja o que deve acontecer antes de abrir `solution/`. Use `kubectl explain` e a aula para esclarecer a API.

## Fase 1 — Preparar e prever

```bash
kubectl config current-context
make lab-prepare LAB=02.12
cat .labs/02.12/resources.yaml
```

## Fase 2 — Aplicar e observar

Complete os TODOs e execute:

```bash
kubectl apply -f .labs/02.12/
make lab-test LAB=02.12
make lab-observe LAB=02.12
```

`kubectl get pod manutencao -n lab-02-12 -o wide` deve indicar `dev-worker` antes do experimento.

## Fase 3 — Experimento controlado

**Somente no Kind local**, execute `kubectl cordon dev-worker`; compare `kubectl get nodes` e observe que o Pod existente não é removido. **Obrigatoriamente** execute `kubectl uncordon dev-worker` em seguida, mesmo se a observação falhar. Não execute drain automático, que pode atingir Pods de outros labs.

## Resultado esperado e evidências

O nó fica `SchedulingDisabled` após cordon, mas o Pod existente permanece. Após uncordon, o worker volta a aceitar agendamentos.

**Evidências específicas:** registre status do nó antes/depois de cordon e depois de uncordon, bem como o estado do Pod existente; explique que cordon não equivale a drain.

## Fase 4 — Diagnosticar

`kubectl describe node dev-worker` e `kubectl get pods -n lab-02-12 -o wide`; se o worker continuar indisponível, execute uncordon antes de prosseguir.

Quando a observação não corresponder à hipótese, compare contexto, objetos, eventos e condições antes de modificar os manifests.

## Fase 5 — Limpar com segurança

```bash
make lab-down LAB=02.12
make lab-status LAB=02.12
```

O namespace é preservado; desfaça **separadamente** alterações manuais de nó, policies, Pods temporários e outros recursos criados fora do contrato. Não execute `make down`.

## Critérios de conclusão

- [ ] Completei o YAML sem copiar a solução e validei o contexto `kind-dev`.
- [ ] Observei a condição específica descrita no resultado esperado.
- [ ] Registrei a hipótese inicial, evidências e explicação técnica.
- [ ] Fiz a limpeza e desmanchei todas as alterações manuais.

## Perguntas de diagnóstico e reflexão

- Qual diferença existe entre cordon e drain?
- Por que uncordon não move automaticamente Pods?

## Aprofunde seus conhecimentos

[Documentação Kubernetes](https://kubernetes.io/docs/tasks/administer-cluster/safely-drain-node/) · [Aula 02.12](../../node-maintenance/README.md)

---

[← Lab 02.11](../pdb-basico/README.md) · [↑ Camada 02](../../README.md) · [Próximo: Lab 02.13 →](../networkpolicy-basico/README.md)
