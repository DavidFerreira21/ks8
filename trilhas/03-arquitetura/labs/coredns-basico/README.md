# Lab 03.14 — CoreDNS e Service Discovery

[← Aula 03.14](../../coredns/README.md) · [↑ Camada 03](../../README.md) · [🧪 Índice dos labs](../../../../docs/labs.md)

> **MODO DESAFIO:** `make lab-prepare LAB=03.14` prepara namespace e starter incompleto. Complete `.labs/03.14/resources.yaml`, aplique com `kubectl apply -f .labs/03.14/`, observe e valide. `make lab-up` usa a solução e é exclusivo da CI.

## Objetivo e hipótese

Resolver nome de Service dentro do cluster e diferenciar DNS funcional de backends prontos.

**Pré-requisitos:** `kind-dev`, `kubectl`, `make`, namespace `lab-03-14`. 

## Desafio — o que você vai construir

Crie Deployment `web` nginx, Service ClusterIP `web` e Pod cliente BusyBox que permanece ativo.

Preveja o resultado antes de consultar `solution/`. A documentação oficial é a referência para esclarecer recursos e campos.

## Fase 1 — Preparar e prever

```bash
kubectl config current-context
make lab-prepare LAB=03.14
cat .labs/03.14/resources.yaml
```

## Fase 2 — Aplicar e observar

Complete os TODOs e execute:

```bash
kubectl apply -f .labs/03.14/
make lab-test LAB=03.14
make lab-observe LAB=03.14
```

Execute `kubectl exec cliente -n lab-03-14 -- nslookup web.lab-03-14.svc.cluster.local` e compare com `kubectl get svc web -n lab-03-14`.

## Fase 3 — Experimento controlado

Após confirmar resposta DNS e HTTP (`kubectl exec cliente -n lab-03-14 -- wget -qO- http://web:80`), altere temporariamente selector do Service para `app=nenhum`. DNS deve continuar resolvendo ClusterIP, mas o backend pode ficar indisponível. Restaure com apply.

## Resultado esperado e evidências

DNS retorna endereço do Service enquanto os endpoints podem deixar de apontar para Pods. Isso diferencia resolução de nome de roteamento/aplicação.

**Evidências específicas:** registre FQDN, ClusterIP resolvido, resposta HTTP inicial e endpoints antes/depois do selector inválido.

## Fase 4 — Diagnosticar

Investigue `kubectl describe`, eventos, status, selectors e dependências do ambiente. Identifique o primeiro sinal causal; não confunda ausência de um addon com erro do YAML principal.

## Fase 5 — Limpar com segurança

```bash
make lab-down LAB=03.14
make lab-status LAB=03.14
```

O namespace permanece preservado. Reverta recursos temporários não declarados no contrato; não execute `make down`.

## Critérios de conclusão

- [ ] Escrevi o YAML sem copiar a solução.
- [ ] **Critério exclusivo 03.14:** registre FQDN, ClusterIP resolvido, resposta HTTP inicial e endpoints antes/depois do selector inválido.
- [ ] Expliquei a diferença entre estado declarado e comportamento comprovado.
- [ ] Reverti experimentos e limpei o laboratório.

## Perguntas de diagnóstico e reflexão

- Por que resolver DNS não comprova backend saudável?
- Que parte do nome identifica o namespace?
- Qual componente mantém registros DNS e qual implementa ClusterIP?

## Aprofunde seus conhecimentos

[Documentação Kubernetes](https://kubernetes.io/docs/concepts/services-networking/dns-pod-service/) · [Aula 03.14](../../coredns/README.md)

---

[← Lab 03.13](../kube-proxy-ebpf-basico/README.md) · [↑ Aula 03.14](../../coredns/README.md) · [↑ Camada 03](../../README.md) · [Próximo: Lab 03.15 →](../csi-storage-basico/README.md)
