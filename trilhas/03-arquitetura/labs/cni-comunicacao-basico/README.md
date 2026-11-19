# Lab 03.12 — CNI e comunicação de rede

[← Aula 03.12](../../cni-comunicacao/README.md) · [↑ Camada 03](../../README.md) · [🧪 Índice dos labs](../../../../docs/labs.md)

> **MODO DESAFIO:** `make lab-prepare LAB=03.12` prepara namespace e starter incompleto. Complete `.labs/03.12/resources.yaml`, aplique com `kubectl apply -f .labs/03.12/`, observe e valide. `make lab-up` usa a solução e é exclusivo da CI.

## Objetivo e hipótese

Verificar IPs de Pods e conectividade direta, distinguindo esse resultado do funcionamento de Services.

**Pré-requisitos:** `kind-dev`, `kubectl`, `make`, namespace `lab-03-12`. 

## Desafio — o que você vai construir

Crie Deployment `web` com uma réplica nginx e Pod `cliente` com BusyBox executando `sleep 3600`.

Preveja o resultado antes de consultar `solution/`. A documentação oficial é a referência para esclarecer recursos e campos.

## Fase 1 — Preparar e prever

```bash
kubectl config current-context
make lab-prepare LAB=03.12
cat .labs/03.12/resources.yaml
```

## Fase 2 — Aplicar e observar

Complete os TODOs e execute:

```bash
kubectl apply -f .labs/03.12/
make lab-test LAB=03.12
make lab-observe LAB=03.12
```

Anote IP e nó do Pod nginx via `kubectl get pods -n lab-03-12 -o wide`.

## Fase 3 — Experimento controlado

Use `kubectl exec -n lab-03-12 cliente -- wget -qO- http://IP_DO_POD_NGINX` substituindo pelo IP observado. Compare o resultado com o estado do Pod, sem criar um Service.

## Resultado esperado e evidências

Com processo nginx disponível e rede Pod funcional, o cliente alcança o IP do Pod. Isso **não** testa NetworkPolicy ou DNS.

**Evidências específicas:** registre IPs, nós e resposta HTTP do IP direto; explique qual parte depende de CNI e qual depende do processo nginx.

## Fase 4 — Diagnosticar

Investigue `kubectl describe`, eventos, status, selectors e dependências do ambiente. Identifique o primeiro sinal causal; não confunda ausência de um addon com erro do YAML principal.

## Fase 5 — Limpar com segurança

```bash
make lab-down LAB=03.12
make lab-status LAB=03.12
```

O namespace permanece preservado. Reverta recursos temporários não declarados no contrato; não execute `make down`.

## Critérios de conclusão

- [ ] Escrevi o YAML sem copiar a solução.
- [ ] **Critério exclusivo 03.12:** registre IPs, nós e resposta HTTP do IP direto; explique qual parte depende de CNI e qual depende do processo nginx.
- [ ] Expliquei a diferença entre estado declarado e comportamento comprovado.
- [ ] Reverti experimentos e limpei o laboratório.

## Perguntas de diagnóstico e reflexão

- Por que Pod IP e Service ClusterIP têm finalidades diferentes?
- O que o teste por IP direto não valida?
- Como distinguir falha do processo de falha da comunicação entre Pods?

## Aprofunde seus conhecimentos

[Documentação Kubernetes](https://kubernetes.io/docs/concepts/cluster-administration/networking/) · [Aula 03.12](../../cni-comunicacao/README.md)

---

[← Lab 03.11](../container-runtime-basico/README.md) · [↑ Aula 03.12](../../cni-comunicacao/README.md) · [↑ Camada 03](../../README.md) · [Próximo: Lab 03.13 →](../kube-proxy-ebpf-basico/README.md)
