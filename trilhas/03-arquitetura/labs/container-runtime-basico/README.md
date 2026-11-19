# Lab 03.11 — Container Runtime

[← Aula 03.11](../../container-runtime/README.md) · [↑ Camada 03](../../README.md) · [🧪 Índice dos labs](../../../../docs/labs.md)

> **MODO DESAFIO:** `make lab-prepare LAB=03.11` prepara namespace e starter incompleto. Complete `.labs/03.11/resources.yaml`, aplique com `kubectl apply -f .labs/03.11/`, observe e valide. `make lab-up` usa a solução e é exclusivo da CI.

## Objetivo e hipótese

Examinar imagem e containerID e distinguir erro de pull de falha do processo depois do início.

**Pré-requisitos:** `kind-dev`, `kubectl`, `make`, namespace `lab-03-11`. 

## Desafio — o que você vai construir

Crie Pod `runtime-demo` com BusyBox e comando `sleep 3600`, sem imagens privadas.

Preveja o resultado antes de consultar `solution/`. A documentação oficial é a referência para esclarecer recursos e campos.

## Fase 1 — Preparar e prever

```bash
kubectl config current-context
make lab-prepare LAB=03.11
cat .labs/03.11/resources.yaml
```

## Fase 2 — Aplicar e observar

Complete os TODOs e execute:

```bash
kubectl apply -f .labs/03.11/
make lab-test LAB=03.11
make lab-observe LAB=03.11
```

Use `kubectl get pod runtime-demo -n lab-03-11 -o jsonpath='{.status.containerStatuses}'` e `kubectl get node dev-worker -o jsonpath='{.status.nodeInfo.containerRuntimeVersion}'`.

## Fase 3 — Experimento controlado

Em um Pod **temporário** `kubectl run imagem-invalida -n lab-03-11 --image=busybox:tag-ficticia-lab --restart=Never -- sleep 3600`, observe eventos de pull e remova com `kubectl delete pod imagem-invalida -n lab-03-11 --ignore-not-found`. Não modifique o runtime do nó.

## Resultado esperado e evidências

O Pod principal mostra `containerID` e `imageID`. O segundo Pod fica sem processo iniciado por falha de pull; não é CrashLoopBackOff.

**Evidências específicas:** registre imagem declarada, imageID/containerID, versão de runtime reportada pelo Node e erro do Pod temporário.

## Fase 4 — Diagnosticar

Investigue `kubectl describe`, eventos, status, selectors e dependências do ambiente. Identifique o primeiro sinal causal; não confunda ausência de um addon com erro do YAML principal.

## Fase 5 — Limpar com segurança

```bash
make lab-down LAB=03.11
make lab-status LAB=03.11
```

O namespace permanece preservado. Reverta recursos temporários não declarados no contrato; não execute `make down`.

## Critérios de conclusão

- [ ] Escrevi o YAML sem copiar a solução.
- [ ] **Critério exclusivo 03.11:** registre imagem declarada, imageID/containerID, versão de runtime reportada pelo Node e erro do Pod temporário.
- [ ] Expliquei a diferença entre estado declarado e comportamento comprovado.
- [ ] Reverti experimentos e limpei o laboratório.

## Perguntas de diagnóstico e reflexão

- Como distinguir ImagePullBackOff de CrashLoopBackOff?
- Quem solicita início do container ao runtime?
- Qual campo relaciona o Pod ao container efetivamente executado?

## Aprofunde seus conhecimentos

[Documentação Kubernetes](https://kubernetes.io/docs/setup/production-environment/container-runtimes/) · [Aula 03.11](../../container-runtime/README.md)

---

[← Lab 03.10](../kubelet-basico/README.md) · [↑ Aula 03.11](../../container-runtime/README.md) · [↑ Camada 03](../../README.md) · [Próximo: Lab 03.12 →](../cni-comunicacao-basico/README.md)
