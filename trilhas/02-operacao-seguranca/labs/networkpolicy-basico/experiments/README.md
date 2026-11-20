# Experimento avançado 02.13 — NetworkPolicy com enforcement real

[← Lab 02.13](../README.md) · [↑ Camada 02](../../../README.md) · [🛠️ Preparar Cilium](../../../../../docs/ambientes/04-cilium.md)

> **Opcional e funcional:** use **exclusivamente** o Kind `cilium-lab` criado com `disableDefaultCNI: true` e com Cilium saudável. Não instale outra CNI em cluster compartilhado. Este experimento testa **NetworkPolicy nativa** do Kubernetes (não CiliumNetworkPolicy).

## Hipótese e pré-requisitos

Um Pod selecionado por `podSelector.app=policy-server` recebe default-deny ingress quando a primeira NetworkPolicy é aplicada. Uma segunda política **aditiva** libera somente conexões TCP/80 vindas do Pod `role=allowed`. O cliente `role=blocked` deve continuar sem acesso.

Prepare conforme o [guia Cilium](../../../../../docs/ambientes/04-cilium.md). Confirme:

```bash
kubectl config use-context kind-cilium-lab
cilium status --context kind-cilium-lab --wait
kubectl --context kind-cilium-lab get nodes
make lab-prepare LAB=02.13 CLUSTER_NAME=cilium-lab
kubectl --context kind-cilium-lab apply -f trilhas/02-operacao-seguranca/labs/networkpolicy-basico/experiments/participants.yaml
kubectl --context kind-cilium-lab wait --for=condition=Ready pod/policy-server pod/client-allowed pod/client-blocked -n lab-02-13 --timeout=180s
```

## Fase A — Linha de base antes das policies

```bash
SERVER_IP="$(kubectl --context kind-cilium-lab get pod policy-server -n lab-02-13 -o jsonpath='{.status.podIP}')"
kubectl --context kind-cilium-lab exec -n lab-02-13 client-allowed -- wget -T 3 -qO- "http://$SERVER_IP"
kubectl --context kind-cilium-lab exec -n lab-02-13 client-blocked -- wget -T 3 -qO- "http://$SERVER_IP"
```

Ambos devem obter HTTP. Se algum falhar **antes** de aplicar policy, corrija CNI/nginx antes de atribuir a falha a isolamento.

## Fase B — Bloquear todas as origens

```bash
kubectl --context kind-cilium-lab apply -f trilhas/02-operacao-seguranca/labs/networkpolicy-basico/experiments/deny-server.yaml
kubectl --context kind-cilium-lab get networkpolicy -n lab-02-13
kubectl --context kind-cilium-lab exec -n lab-02-13 client-allowed -- wget -T 3 -qO- "http://$SERVER_IP"
kubectl --context kind-cilium-lab exec -n lab-02-13 client-blocked -- wget -T 3 -qO- "http://$SERVER_IP"
```

**Esperado:** os dois `wget` falham por timeout/negação de rede; o **exit code não zero é esperado**. Aguarde alguns segundos se os endpoints ainda estiverem atualizando. Não trate falha do processo nginx ou resolução DNS como prova de isolamento — aqui usamos IP direto.

## Fase C — Liberar apenas uma origem

```bash
kubectl --context kind-cilium-lab apply -f trilhas/02-operacao-seguranca/labs/networkpolicy-basico/experiments/allow-role.yaml
kubectl --context kind-cilium-lab exec -n lab-02-13 client-allowed -- wget -T 3 -qO- "http://$SERVER_IP"
kubectl --context kind-cilium-lab exec -n lab-02-13 client-blocked -- wget -T 3 -qO- "http://$SERVER_IP"
kubectl --context kind-cilium-lab get networkpolicy deny-server allow-only-role -n lab-02-13 -o yaml
```

**Esperado:** a origem `allowed` volta a conectar, `blocked` permanece negada. A combinação das policies é aditiva: a deny ingress sem regras não anula a permissão explícita concedida pela segunda policy.

## Evidência e limpeza

Registre os três momentos: **ambos conectam → ambos negados → somente allowed conecta**. Inclua labels, endereço IP observado, status Cilium, exit codes e condições. Não marque funcional se houver falhas de baseline ou tráfego de ambos permitido após as policies.

```bash
kubectl --context kind-cilium-lab delete -f trilhas/02-operacao-seguranca/labs/networkpolicy-basico/experiments/allow-role.yaml --ignore-not-found
kubectl --context kind-cilium-lab delete -f trilhas/02-operacao-seguranca/labs/networkpolicy-basico/experiments/deny-server.yaml --ignore-not-found
kubectl --context kind-cilium-lab delete -f trilhas/02-operacao-seguranca/labs/networkpolicy-basico/experiments/participants.yaml --ignore-not-found
make lab-down LAB=02.13 CLUSTER_NAME=cilium-lab
```

Só elimine o Kind `cilium-lab` quando confirmar que nenhum outro experimento depende dele.

[NetworkPolicy oficial](https://kubernetes.io/docs/concepts/services-networking/network-policies/) · [Cilium NetworkPolicy](https://docs.cilium.io/en/stable/security/policy/)
