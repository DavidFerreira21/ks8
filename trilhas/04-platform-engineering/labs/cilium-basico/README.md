# Lab 04.06 — Cilium

[← Aula 04.06](../../cilium/README.md) · [↑ Camada 04](../../README.md) · [🧪 Índice dos labs](../../../../docs/labs.md)

> **MODO DESAFIO — Kind Cilium dedicado:** siga primeiro o [guia de preparação](../../../../docs/ambientes/04-cilium.md). No contexto `kind-cilium-lab`, use `make lab-prepare LAB=04.06 CLUSTER_NAME=cilium-lab`, complete o starter e aplique seu YAML. O motor de labs **não** deve ser executado contra cluster compartilhado.

## Objetivo e hipótese

Permitir ingress ao Pod backend apenas de cliente rotulado, comprovando policy via tráfego se Cilium estiver instalado.

**Contexto:** cluster Kind isolado `cilium-lab`, contexto `kind-cilium-lab`, namespace de estudo `lab-04-06`. `make lab-test` verifica objetos, **não prova sozinho a funcionalidade do controller**.

## Pré-requisitos da ferramenta

**Guia de instalação, versões e reversão:** [🛠️ Preparar Cilium](../../../../docs/ambientes/04-cilium.md). Siga-o antes de aplicar Custom Resources; a CI padrão não instala esse controlador.

**Requer Kind dedicado com Cilium instalado e operando como CNI**, conforme guia oficial; Kind padrão não oferece `CiliumNetworkPolicy`. Instalar Cilium significa preparar cluster compatível, não adicionar policy sobre CNI desconhecida.

**Segurança:** Não substitua a CNI de um cluster compartilhado para executar este laboratório.

## Desafio — o que você vai construir

Escreva Pod `backend` nginx com label `app: backend`, Pod `frontend` BusyBox com `role: frontend`, Pod `externo` BusyBox com `role: outsider` e `CiliumNetworkPolicy` `apenas-frontend` permitindo ingress do frontend para backend.

Defina sua hipótese antes de consultar `solution/`. Se o tipo não aparecer em `kubectl api-resources`, registre dependência ausente e não tente contornar com recursos fictícios.

## Fase 1 — Preparar e prever

```bash
kubectl config current-context  # esperado kind-cilium-lab
make lab-prepare LAB=04.06 CLUSTER_NAME=cilium-lab
cat .labs/04.06/resources.yaml
```

Confirme disponibilidade da API específica da ferramenta e o namespace alvo antes de aplicar.

## Fase 2 — Aplicar e observar

Complete os TODOs:

```bash
kubectl apply --dry-run=server --validate=strict -f .labs/04.06/
kubectl apply -f .labs/04.06/
make lab-test LAB=04.06 CLUSTER_NAME=cilium-lab
make lab-observe LAB=04.06 CLUSTER_NAME=cilium-lab
```

Depois do apply, `kubectl get cnp -n lab-04-06` e `kubectl get pods -n lab-04-06 -o wide`; capture IP do backend.

## Fase 3 — Experimento controlado

Teste `kubectl exec -n lab-04-06 frontend -- wget -T 3 -qO- http://BACKEND_POD_IP` e compare com `kubectl exec -n lab-04-06 externo -- wget -T 3 -qO- http://BACKEND_POD_IP`. O primeiro deve funcionar; o segundo deve falhar por policy quando todos os endpoints estiverem gerenciados pelo Cilium.

## Resultado esperado e evidências

Com Cilium efetivamente aplicando a policy, ingress de frontend é permitido e outsider bloqueado. Se ambos funcionarem, não declare isolamento; revise endpoints e status do agente.

**Evidências específicas:** registre IPs, selectors, status da CiliumNetworkPolicy e respostas distintas dos dois clientes; quando disponível, agregue evidências Hubble.

## Fase 4 — Diagnosticar

Investigue CRDs, condições dos custom resources, logs do controller instalado e permissões. Diferencie **rejeição de API**, **ausência de controller**, **reconciliação não pronta** e **falta de dependência externa**.

## Fase 5 — Limpar com segurança

```bash
make lab-down LAB=04.06 CLUSTER_NAME=cilium-lab
make lab-status LAB=04.06 CLUSTER_NAME=cilium-lab
```

A limpeza remove os objetos declarados neste contrato, **não desinstala automaticamente o addon**. Revise recursos filhos, credenciais e qualquer custo externo antes de excluir a instalação. Na ausência do addon, não tente remoção indiscriminada.

## Critérios de conclusão

- [ ] Escrevi o manifesto principal sem copiar a solução e validei as APIs necessárias.
- [ ] **Critério exclusivo 04.06:** registre IPs, selectors, status da CiliumNetworkPolicy e respostas distintas dos dois clientes; quando disponível, agregue evidências Hubble.
- [ ] Diferenciei validação declarativa de comportamento funcional realmente observado.
- [ ] Reverti mudanças temporárias e executei a limpeza segura.

## Perguntas de diagnóstico e reflexão

- Por que uma CiliumNetworkPolicy aceita não prova enforcement?
- Qual é a diferença entre endpointSelector e fromEndpoints?
- Como separar falha de rede de falha do processo nginx?

## Aprofunde seus conhecimentos

[Documentação oficial](https://docs.cilium.io/en/stable/security/policy/layer3/) · [Aula 04.06](../../cilium/README.md)

---

[← Lab 04.05](../karpenter-basico/README.md) · [↑ Aula 04.06](../../cilium/README.md) · [↑ Camada 04](../../README.md) · [Próximo: Lab 04.07 →](../prometheus-grafana-basico/README.md)
