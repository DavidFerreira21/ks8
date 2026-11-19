# Lab 03.02 — kube-apiserver

[← Aula 03.02](../../kube-apiserver/README.md) · [↑ Camada 03](../../README.md) · [🧪 Índice dos labs](../../../../docs/labs.md)

> **MODO DESAFIO:** execute `make lab-prepare LAB=03.02`, complete `.labs/03.02/resources.yaml`, aplique com `kubectl apply -f .labs/03.02/` e só então use `make lab-test LAB=03.02`. O comando `make lab-up` usa a solução de referência e fica reservado à CI.

## Objetivo e hipótese

Diferenciar validação da API e persistência de recursos usando requisições válidas e inválidas.

**Pré-requisitos:** cluster Kind `dev`, contexto `kind-dev`, `kubectl` e `make`. Namespace de estudo `lab-03-02`. 

## Desafio — o que você vai construir

Escreva um ConfigMap `api-demo` com `data.revisao: v1` no namespace didático.

**Antes de começar:** escreva sua hipótese para cada etapa. A solução em `solution/` existe para conferência posterior, não para ser copiada.

## Fase 1 — Preparar e prever

```bash
kubectl config current-context
make lab-prepare LAB=03.02
cat .labs/03.02/resources.yaml
```

Verifique se o namespace foi criado, sem aplicar a solução.

## Fase 2 — Aplicar e observar

Complete todos os TODOs no starter e aplique:

```bash
kubectl apply -f .labs/03.02/
make lab-test LAB=03.02
make lab-observe LAB=03.02
```

Inspecione o campo `data` com `kubectl get configmap api-demo -n lab-03-02 -o yaml` e consulte `kubectl explain configmap.data`.

## Fase 3 — Experimento controlado

Produza um YAML temporário com campo inválido `spec.naoExiste`, usando `kubectl apply --dry-run=server --validate=strict -f ARQUIVO`. Compare a rejeição da API com o ConfigMap existente, sem modificar a solução principal.

## Resultado esperado e evidências

O ConfigMap correto é persistido; o YAML inválido recebe erro de validação no servidor e não cria objeto adicional.

**Evidências específicas:** registe a operação aceita, a mensagem de erro de campo inválido, o contexto e por que nenhuma mudança foi persistida.

## Fase 4 — Diagnosticar

Compare contexto, campos do objeto, condições e eventos. Uma falha de admissão, um erro de scheduling e uma falha de container ocorrem em etapas diferentes; use `kubectl describe` e a documentação para sustentar sua hipótese.

## Fase 5 — Limpar com segurança

```bash
make lab-down LAB=03.02
make lab-status LAB=03.02
```

**Segurança:** o namespace é preservado. Remova recursos temporários que criou fora do contrato; em 03.02 a limpeza não deve afetar outros labs. Não execute `make down`.

## Critérios de conclusão

- [ ] Completei o YAML por conta própria e confirmei `kind-dev`.
- [ ] **Critério exclusivo 03.02:** registe a operação aceita, a mensagem de erro de campo inválido, o contexto e por que nenhuma mudança foi persistida.
- [ ] Registrei hipótese, comparação esperado/observado e explicação causal.
- [ ] Restaurei alterações temporárias e executei a limpeza do lab.

## Perguntas de diagnóstico e reflexão

- Qual a diferença entre API discovery e aplicação do objeto?
- Por que `--dry-run=server` é mais adequado que teste puramente local?
- Como um 403 difere de falha de conexão com o API Server?

## Aprofunde seus conhecimentos

[Documentação oficial](https://kubernetes.io/docs/reference/using-api/) · [Aula 03.02](../../kube-apiserver/README.md)

---

[← Lab 03.01](../arquitetura-cluster-basico/README.md) · [↑ Aula 03.02](../../kube-apiserver/README.md) · [↑ Camada 03](../../README.md) · [Próximo: Lab 03.03 →](../etcd-basico/README.md)
