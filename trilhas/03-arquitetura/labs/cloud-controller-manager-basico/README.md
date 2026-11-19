# Lab 03.09 — cloud-controller-manager

[← Aula 03.09](../../cloud-controller-manager/README.md) · [↑ Camada 03](../../README.md) · [🧪 Índice dos labs](../../../../docs/labs.md)

> **MODO DESAFIO:** execute `make lab-prepare LAB=03.09`, complete `.labs/03.09/resources.yaml`, aplique com `kubectl apply -f .labs/03.09/` e só então use `make lab-test LAB=03.09`. O comando `make lab-up` usa a solução de referência e fica reservado à CI.

## Objetivo e hipótese

Distinguir Service LoadBalancer declarado de implementação de balanceador externo.

**Pré-requisitos:** cluster Kind `dev`, contexto `kind-dev`, `kubectl` e `make`. Namespace de estudo `lab-03-09`. **Sem provedor cloud:** este lab só valida a intenção declarativa, não o provisionamento externo.

## Desafio — o que você vai construir

Escreva um Deployment `web` com 1 réplica nginx e Service `exposicao` com `type: LoadBalancer`, selector `app: web` e porta 80.

**Antes de começar:** escreva sua hipótese para cada etapa. A solução em `solution/` existe para conferência posterior, não para ser copiada.

## Fase 1 — Preparar e prever

```bash
kubectl config current-context
make lab-prepare LAB=03.09
cat .labs/03.09/resources.yaml
```

Verifique se o namespace foi criado, sem aplicar a solução.

## Fase 2 — Aplicar e observar

Complete todos os TODOs no starter e aplique:

```bash
kubectl apply -f .labs/03.09/
make lab-test LAB=03.09
make lab-observe LAB=03.09
```

Execute `kubectl get svc exposicao -n lab-03-09 -o yaml` e confira `status.loadBalancer.ingress`, além de EndpointSlices para validar a seleção.

## Fase 3 — Experimento controlado

Compare `kubectl get service exposicao -n lab-03-09` com `kubectl get endpointslices -n lab-03-09 -l kubernetes.io/service-name=exposicao`. Discuta o que falta para prover IP externo sem instalar componente cloud.

## Resultado esperado e evidências

Service e endpoint podem existir, mas o endereço externo não é provisionado no Kind padrão. Isso não invalida o manifesto.

**Evidências específicas:** registre `spec.type`, `status.loadBalancer`, EndpointSlices e a presença/ausência de controlador cloud.

## Fase 4 — Diagnosticar

Compare contexto, campos do objeto, condições e eventos. Uma falha de admissão, um erro de scheduling e uma falha de container ocorrem em etapas diferentes; use `kubectl describe` e a documentação para sustentar sua hipótese.

## Fase 5 — Limpar com segurança

```bash
make lab-down LAB=03.09
make lab-status LAB=03.09
```

**Segurança:** o namespace é preservado. Remova recursos temporários que criou fora do contrato; em 03.09 a limpeza não deve afetar outros labs. Não execute `make down`.

## Critérios de conclusão

- [ ] Completei o YAML por conta própria e confirmei `kind-dev`.
- [ ] **Critério exclusivo 03.09:** registre `spec.type`, `status.loadBalancer`, EndpointSlices e a presença/ausência de controlador cloud.
- [ ] Registrei hipótese, comparação esperado/observado e explicação causal.
- [ ] Restaurei alterações temporárias e executei a limpeza do lab.

## Perguntas de diagnóstico e reflexão

- Que componente cloud pode preencher status de um Service LoadBalancer?
- Por que ClusterIP e LoadBalancer são responsabilidades distintas?
- Como distinguir falta de IP externo de ausência de backend?

## Aprofunde seus conhecimentos

[Documentação oficial](https://kubernetes.io/docs/concepts/architecture/cloud-controller/) · [Aula 03.09](../../cloud-controller-manager/README.md)

---

[← Lab 03.08](../kube-scheduler-basico/README.md) · [↑ Aula 03.09](../../cloud-controller-manager/README.md) · [↑ Camada 03](../../README.md) · [Próximo: Lab 03.10 →](../kubelet-basico/README.md)
