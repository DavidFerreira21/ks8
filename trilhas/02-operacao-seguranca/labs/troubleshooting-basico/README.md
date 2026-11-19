# Lab 02.14 — Diagnóstico orientado a evidências

[← Aula 02.14](../../troubleshooting/README.md) · [↑ Camada 02](../../README.md) · [🧪 Índice dos labs](../../../../docs/labs.md)

> **MODO DESAFIO:** `make lab-prepare LAB=02.14` cria o namespace e copia o starter **incompleto** em `.labs/02.14/resources.yaml`. Complete-o, execute `kubectl apply -f .labs/02.14/`, depois `make lab-test LAB=02.14` e `make lab-observe LAB=02.14`. **`make lab-up` aplica a solução e é exclusivo da CI.**

## Objetivo e hipótese

Identificar uma falha intencional de pull de imagem e formular uma correção comprovável, sem apagar o Pod automaticamente.

**Pré-requisitos:** Kind `dev`, contexto `kind-dev`, `kubectl` e `make`; namespace exclusivo `lab-02-14`. O erro de imagem é intencional. **Não interprete `make lab-test` como prova de readiness** neste lab.

## Desafio — o que você vai construir

Crie Pod `diagnostico` com imagem propositalmente inválida `busybox:versao-inexistente-para-lab`, de modo que o container não consiga iniciar. O erro faz parte do experimento.

Preveja o que deve acontecer antes de abrir `solution/`. Use `kubectl explain` e a aula para esclarecer a API.

## Fase 1 — Preparar e prever

```bash
kubectl config current-context
make lab-prepare LAB=02.14
cat .labs/02.14/resources.yaml
```

## Fase 2 — Aplicar e observar

Complete os TODOs e execute:

```bash
kubectl apply -f .labs/02.14/
make lab-test LAB=02.14
make lab-observe LAB=02.14
```

`kubectl get pod diagnostico -n lab-02-14` eventualmente mostrará `ErrImagePull` ou `ImagePullBackOff`; `kubectl describe pod diagnostico -n lab-02-14` explica a tentativa de pull.

## Fase 3 — Experimento controlado

Após registrar o problema e executar `make lab-test` com o manifesto intencionalmente inválido, corrija **apenas no seu manifesto local** para `busybox:1.36` e reaplique. Observe a transição para Running. Antes de encerrar, lembre que o estado corrigido difere do manifesto de solução usado no teste didático inicial.

## Resultado esperado e evidências

O Pod pode permanecer `Pending` na fase, com container em estado de espera por pull. Corrigir a tag e reaplicar deve permitir iniciar o container quando houver acesso ao registry.

**Evidências específicas:** registre fase do Pod, motivo do container, evento exato de erro e estado após correção; diferencie `ImagePullBackOff` de `CrashLoopBackOff`.

## Fase 4 — Diagnosticar

`kubectl get pod diagnostico -n lab-02-14 -o yaml`; `kubectl describe pod diagnostico -n lab-02-14`; `kubectl get events -n lab-02-14 --sort-by=.lastTimestamp`.

Quando a observação não corresponder à hipótese, compare contexto, objetos, eventos e condições antes de modificar os manifests.

## Fase 5 — Limpar com segurança

```bash
make lab-down LAB=02.14
make lab-status LAB=02.14
```

O namespace é preservado; desfaça **separadamente** alterações manuais de nó, policies, Pods temporários e outros recursos criados fora do contrato. Não execute `make down`.

## Critérios de conclusão

- [ ] **Evidência funcional do Lab 02.14:** um erro de imagem impediu o início, os eventos identificaram a causa e a correção permitiu o Pod ficar Running.
- [ ] Completei o YAML sem copiar a solução e validei o contexto `kind-dev`.
- [ ] Observei a condição específica descrita no resultado esperado.
- [ ] Registrei a hipótese inicial, evidências e explicação técnica.
- [ ] Fiz a limpeza e desmanchei todas as alterações manuais.

## Perguntas de diagnóstico e reflexão

- Por que um Pod Pending pode não ter logs de aplicação?
- Como diferenciar erro de imagem de falha da aplicação após iniciar?

- Por que `ImagePullBackOff` não é o mesmo que `CrashLoopBackOff`?

## Aprofunde seus conhecimentos

[Documentação Kubernetes](https://kubernetes.io/docs/tasks/debug/debug-application/debug-pods/) · [Aula 02.14](../../troubleshooting/README.md)

---

[← Lab 02.13](../networkpolicy-basico/README.md) · [↑ Aula 02.14](../../troubleshooting/README.md) · [↑ Camada 02](../../README.md) · [Próxima: Camada 03 →](../../../03-arquitetura/README.md)
