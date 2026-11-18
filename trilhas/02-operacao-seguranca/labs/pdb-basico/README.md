# Lab 02.11 — PodDisruptionBudget

[← Aula 02.11](../../pdb/README.md) · [↑ Camada 02](../../README.md) · [🧪 Índice dos labs](../../../../docs/labs.md)

> **MODO DESAFIO:** `make lab-prepare LAB=02.11` cria o namespace e copia o starter **incompleto** em `.labs/02.11/resources.yaml`. Complete-o, execute `kubectl apply -f .labs/02.11/`, depois `make lab-test LAB=02.11` e `make lab-observe LAB=02.11`. **`make lab-up` aplica a solução e é exclusivo da CI.**

## Objetivo e hipótese

Observar `disruptionsAllowed` de um PDB que protege um Deployment e explicar interrupções voluntárias.

**Pré-requisitos:** Kind `dev`, contexto `kind-dev`, `kubectl` e `make`; namespace exclusivo `lab-02-11`. 

## Desafio — o que você vai construir

Crie Deployment `replicas` com três Pods nginx e PodDisruptionBudget `disponibilidade` com `minAvailable: 2` e selector compatível.

Preveja o que deve acontecer antes de abrir `solution/`. Use `kubectl explain` e a aula para esclarecer a API.

## Fase 1 — Preparar e prever

```bash
kubectl config current-context
make lab-prepare LAB=02.11
cat .labs/02.11/resources.yaml
```

## Fase 2 — Aplicar e observar

Complete os TODOs e execute:

```bash
kubectl apply -f .labs/02.11/
make lab-test LAB=02.11
make lab-observe LAB=02.11
```

Aguarde `kubectl rollout status deployment/replicas -n lab-02-11`; em seguida `kubectl get pdb disponibilidade -n lab-02-11 -o yaml`.

## Fase 3 — Experimento controlado

Reduza **temporariamente** a réplicas 2 com `kubectl scale deployment/replicas --replicas=2 -n lab-02-11`. Compare `disruptionsAllowed` após estabilizar; restaure `--replicas=3` antes de rodar `make lab-test` novamente. Não execute drain neste lab.

## Resultado esperado e evidências

Com três réplicas saudáveis e `minAvailable: 2`, normalmente `disruptionsAllowed: 1`; com apenas duas saudáveis, tende a zero. O valor depende da prontidão real.

**Evidências específicas:** registre `currentHealthy`, `desiredHealthy` e `disruptionsAllowed` antes/depois da escala e explique o limite de eviction voluntária.

## Fase 4 — Diagnosticar

`kubectl describe pdb disponibilidade -n lab-02-11` e `kubectl get pods -n lab-02-11 -o wide`.

Quando a observação não corresponder à hipótese, compare contexto, objetos, eventos e condições antes de modificar os manifests.

## Fase 5 — Limpar com segurança

```bash
make lab-down LAB=02.11
make lab-status LAB=02.11
```

O namespace é preservado; desfaça **separadamente** alterações manuais de nó, policies, Pods temporários e outros recursos criados fora do contrato. Não execute `make down`.

## Critérios de conclusão

- [ ] **Evidência funcional do Lab 02.11:** o PDB passou de orçamento disponível para zero após reduzir réplicas saudáveis e foi restaurado.
- [ ] Completei o YAML sem copiar a solução e validei o contexto `kind-dev`.
- [ ] Observei a condição específica descrita no resultado esperado.
- [ ] Registrei a hipótese inicial, evidências e explicação técnica.
- [ ] Fiz a limpeza e desmanchei todas as alterações manuais.

## Perguntas de diagnóstico e reflexão

- Por que um PDB não impede falhas involuntárias?
- Como readiness influencia `disruptionsAllowed`?

- Por que apagar diretamente um Pod não equivale a uma eviction protegida pelo PDB?

## Aprofunde seus conhecimentos

[Documentação Kubernetes](https://kubernetes.io/docs/concepts/workloads/pods/disruptions/) · [Aula 02.11](../../pdb/README.md)

---

[← Lab 02.10](../qos-eviction-basico/README.md) · [↑ Camada 02](../../README.md) · [Próximo: Lab 02.12 →](../node-maintenance-basico/README.md)
