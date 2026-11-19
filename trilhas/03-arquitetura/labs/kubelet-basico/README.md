# Lab 03.10 — kubelet

[← Aula 03.10](../../kubelet/README.md) · [↑ Camada 03](../../README.md) · [🧪 Índice dos labs](../../../../docs/labs.md)

> **MODO DESAFIO:** `make lab-prepare LAB=03.10` prepara namespace e starter incompleto. Complete `.labs/03.10/resources.yaml`, aplique com `kubectl apply -f .labs/03.10/`, observe e valide. `make lab-up` usa a solução e é exclusivo da CI.

## Objetivo e hipótese

Conectar a atuação do kubelet aos estados do container e ao resultado de readiness.

**Pré-requisitos:** `kind-dev`, `kubectl`, `make`, namespace `lab-03-10`. 

## Desafio — o que você vai construir

Crie Pod `agente-demo` com BusyBox. O comando deve criar `/tmp/pronto` e manter o processo ativo; uma readinessProbe `exec` deve verificar a existência desse arquivo.

Preveja o resultado antes de consultar `solution/`. A documentação oficial é a referência para esclarecer recursos e campos.

## Fase 1 — Preparar e prever

```bash
kubectl config current-context
make lab-prepare LAB=03.10
cat .labs/03.10/resources.yaml
```

## Fase 2 — Aplicar e observar

Complete os TODOs e execute:

```bash
kubectl apply -f .labs/03.10/
make lab-test LAB=03.10
make lab-observe LAB=03.10
```

Compare `status.containerStatuses`, `Ready`, `spec.nodeName` e `kubectl describe pod agente-demo -n lab-03-10`.

## Fase 3 — Experimento controlado

Execute `kubectl exec -n lab-03-10 agente-demo -- rm /tmp/pronto` e observe `Ready` ficar False; recrie o arquivo com `kubectl exec -n lab-03-10 agente-demo -- touch /tmp/pronto` e espere a condição voltar. O kubelet avalia a probe.

## Resultado esperado e evidências

O processo continua executando, mas a readiness muda conforme o arquivo. Kubelet publica status; isso não é ação do scheduler.

**Evidências específicas:** registre status Ready antes/depois, nó, eventos e estado do container sem confundir processo em execução com prontidão.

## Fase 4 — Diagnosticar

Investigue `kubectl describe`, eventos, status, selectors e dependências do ambiente. Identifique o primeiro sinal causal; não confunda ausência de um addon com erro do YAML principal.

## Fase 5 — Limpar com segurança

```bash
make lab-down LAB=03.10
make lab-status LAB=03.10
```

O namespace permanece preservado. Reverta recursos temporários não declarados no contrato; não execute `make down`.

## Critérios de conclusão

- [ ] Escrevi o YAML sem copiar a solução.
- [ ] **Critério exclusivo 03.10:** registre status Ready antes/depois, nó, eventos e estado do container sem confundir processo em execução com prontidão.
- [ ] Expliquei a diferença entre estado declarado e comportamento comprovado.
- [ ] Reverti experimentos e limpei o laboratório.

## Perguntas de diagnóstico e reflexão

- Qual responsabilidade é do kubelet, e qual do scheduler?
- Por que o container pode estar Running e o Pod não Ready?
- Que ação devolve Ready sem recriar o Pod?

## Aprofunde seus conhecimentos

[Documentação Kubernetes](https://kubernetes.io/docs/concepts/architecture/nodes/) · [Aula 03.10](../../kubelet/README.md)

---

[← Lab 03.09](../cloud-controller-manager-basico/README.md) · [↑ Aula 03.10](../../kubelet/README.md) · [↑ Camada 03](../../README.md) · [Próximo: Lab 03.11 →](../container-runtime-basico/README.md)
