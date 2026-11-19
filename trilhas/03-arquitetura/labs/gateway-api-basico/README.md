# Lab 03.16 — Gateway API

[← Aula 03.16](../../gateway-api/README.md) · [↑ Camada 03](../../README.md) · [🧪 Índice dos labs](../../../../docs/labs.md)

> **MODO DESAFIO:** `make lab-prepare LAB=03.16` prepara namespace e starter incompleto. Complete `.labs/03.16/resources.yaml`, aplique com `kubectl apply -f .labs/03.16/`, observe e valide. `make lab-up` usa a solução e é exclusivo da CI.

## Objetivo e hipótese

Distinguir configuração de Service de HTTPRoute dependente de Gateway Controller e interpretar recursos ausentes.

**Pré-requisitos:** `kind-dev`, `kubectl`, `make`, namespace `lab-03-16`. O contrato Kind testa o backend nativo; o manifesto de rota em `examples/` é opcional e não instalado automaticamente.

## Desafio — o que você vai construir

Crie Deployment `web` nginx e Service `web` ClusterIP. **Não** aplique HTTPRoute automaticamente: os CRDs e o controlador podem não existir no Kind.

Preveja o resultado antes de consultar `solution/`. A documentação oficial é a referência para esclarecer recursos e campos.

## Fase 1 — Preparar e prever

```bash
kubectl config current-context
make lab-prepare LAB=03.16
cat .labs/03.16/resources.yaml
```

## Fase 2 — Aplicar e observar

Complete os TODOs e execute:

```bash
kubectl apply -f .labs/03.16/
make lab-test LAB=03.16
make lab-observe LAB=03.16
```

Confirme Service/EndpointSlices e execute `kubectl api-resources --api-group=gateway.networking.k8s.io` para investigar descoberta dos tipos.

## Fase 3 — Experimento controlado

Leia `examples/httproute.yaml` e identifique parentRefs/backendRefs. **Somente se CRDs Gateway API e Gateway Controller estiverem instalados**, crie Gateway apropriado e aplique a rota; caso contrário, registre ausência de dependência e NÃO afirme teste de HTTPRoute.

## Resultado esperado e evidências

Backend nativo pode ser testado no Kind. Uma HTTPRoute sem API/controller não resulta em tráfego; existência do YAML não é prova de programação.

**Evidências específicas:** registre endpoints do Service, discovery da API Gateway, ausência/presença do controlador e condições de HTTPRoute se instalado.

## Fase 4 — Diagnosticar

Investigue `kubectl describe`, eventos, status, selectors e dependências do ambiente. Identifique o primeiro sinal causal; não confunda ausência de um addon com erro do YAML principal.

## Fase 5 — Limpar com segurança

```bash
make lab-down LAB=03.16
make lab-status LAB=03.16
```

O namespace permanece preservado. Reverta recursos temporários não declarados no contrato; não execute `make down`.

## Critérios de conclusão

- [ ] Escrevi o YAML sem copiar a solução.
- [ ] **Critério exclusivo 03.16:** registre endpoints do Service, discovery da API Gateway, ausência/presença do controlador e condições de HTTPRoute se instalado.
- [ ] Expliquei a diferença entre estado declarado e comportamento comprovado.
- [ ] Reverti experimentos e limpei o laboratório.

## Perguntas de diagnóstico e reflexão

- Por que HTTPRoute não substitui Service?
- Que componente publica estado Programmed de um Gateway?
- Que etapa depende de CRDs e controller adicionais?

## Aprofunde seus conhecimentos

[Documentação Kubernetes](https://gateway-api.sigs.k8s.io/) · [Aula 03.16](../../gateway-api/README.md)

---

[← Lab 03.15](../csi-storage-basico/README.md) · [↑ Aula 03.16](../../gateway-api/README.md) · [↑ Camada 03](../../README.md) · [Próximo: Lab 03.17 →](../kustomize-helm-basico/README.md)
