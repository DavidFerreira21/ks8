# Lab 03.13 — kube-proxy e eBPF

[← Aula 03.13](../../kube-proxy-ebpf/README.md) · [↑ Camada 03](../../README.md) · [🧪 Índice dos labs](../../../../docs/labs.md)

> **MODO DESAFIO:** `make lab-prepare LAB=03.13` prepara namespace e starter incompleto. Complete `.labs/03.13/resources.yaml`, aplique com `kubectl apply -f .labs/03.13/`, observe e valide. `make lab-up` usa a solução e é exclusivo da CI.

## Objetivo e hipótese

Observar um Service e seus EndpointSlices e explicar a independência entre declaração e dataplane.

**Pré-requisitos:** `kind-dev`, `kubectl`, `make`, namespace `lab-03-13`. 

## Desafio — o que você vai construir

Crie Deployment `web` (duas réplicas nginx) e Service `web` ClusterIP com selector `app: web` e porta 80.

Preveja o resultado antes de consultar `solution/`. A documentação oficial é a referência para esclarecer recursos e campos.

## Fase 1 — Preparar e prever

```bash
kubectl config current-context
make lab-prepare LAB=03.13
cat .labs/03.13/resources.yaml
```

## Fase 2 — Aplicar e observar

Complete os TODOs e execute:

```bash
kubectl apply -f .labs/03.13/
make lab-test LAB=03.13
make lab-observe LAB=03.13
```

Veja `kubectl get svc,endpointslices -n lab-03-13 -o wide` e `kubectl describe service web -n lab-03-13`.

## Fase 3 — Experimento controlado

Altere o selector `kubectl patch svc web -n lab-03-13 -p '{"spec":{"selector":{"app":"nao-existe"}}}'`; compare EndpointSlices. Reaplique o YAML para restaurar o backend.

### Verificar EndpointSlices, seletor e dataplane

```bash
kubectl get service web -n lab-03-13 -o jsonpath='{.spec.clusterIP}{"\n"}'
kubectl get endpointslices -n lab-03-13 -l kubernetes.io/service-name=web -o wide
kubectl patch service web -n lab-03-13 -p '{"spec":{"selector":{"app":"nao-existe"}}}'
kubectl get endpointslices -n lab-03-13 -l kubernetes.io/service-name=web -o wide
kubectl apply -f .labs/03.13/resources.yaml
```

**Evidência:** endpoints desaparecem/ficam vazios quando o selector não corresponde e voltam após a restauração. Para testar Cilium eBPF como dataplane real, use o [experimento avançado opcional em Kind com Cilium](experiments/README.md); somente esse segundo ambiente permite avaliar Cilium instalado, e substituição de kube-proxy exige configuração adicional.

## Resultado esperado e evidências

Service continua existindo enquanto os endpoints deixam de corresponder; depois retornam. A API não informa se o dataplane usa kube-proxy ou alternativa eBPF.

**Evidências específicas:** registre ClusterIP e endpoints antes/depois, selector, recuperação e a implementação real do dataplane detectada no Kind.

## Fase 4 — Diagnosticar

Investigue `kubectl describe`, eventos, status, selectors e dependências do ambiente. Identifique o primeiro sinal causal; não confunda ausência de um addon com erro do YAML principal.

## Fase 5 — Limpar com segurança

```bash
make lab-down LAB=03.13
make lab-status LAB=03.13
```

O namespace permanece preservado. Reverta recursos temporários não declarados no contrato; não execute `make down`.

## Critérios de conclusão

- [ ] Escrevi o YAML sem copiar a solução.
- [ ] **Critério exclusivo 03.13:** registre ClusterIP e endpoints antes/depois, selector, recuperação e a implementação real do dataplane detectada no Kind.
- [ ] Expliquei a diferença entre estado declarado e comportamento comprovado.
- [ ] Reverti experimentos e limpei o laboratório.

## Perguntas de diagnóstico e reflexão

- Por que um Service pode existir sem endpoints?
- Como o EndpointSlice influencia o encaminhamento?
- Por que esse teste não prova uso de eBPF?

## Aprofunde seus conhecimentos

[Documentação Kubernetes](https://kubernetes.io/docs/reference/networking/virtual-ips/) · [Aula 03.13](../../kube-proxy-ebpf/README.md)

---

[← Lab 03.12](../cni-comunicacao-basico/README.md) · [↑ Aula 03.13](../../kube-proxy-ebpf/README.md) · [↑ Camada 03](../../README.md) · [Próximo: Lab 03.14 →](../coredns-basico/README.md)
