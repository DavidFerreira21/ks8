# Preparação 04.03 — Cilium em Kind dedicado

[↑ Ambientes](README.md) · [🧪 Lab 04.03](../../trilhas/04-platform-engineering/labs/cilium-basico/README.md)

> **CNI é componente do cluster.** Não tente instalar Cilium em cima da CNI padrão de um cluster compartilhado. Crie um **Kind separado** `cilium-lab`, com `disableDefaultCNI: true`.

## Preparar cluster separado

```bash
kind create cluster --name cilium-lab --config docs/ambientes/kind-cilium-config.yaml
kubectl config use-context kind-cilium-lab
kubectl get nodes
```

Os nós podem ficar NotReady até a instalação da CNI. Instale **Cilium CLI** conforme [documentação oficial](https://docs.cilium.io/en/stable/installation/kind/) e selecione uma versão compatível com o Kubernetes do Kind. O procedimento recomendado utiliza a CLI:

```bash
cilium install --context kind-cilium-lab
cilium status --context kind-cilium-lab --wait
kubectl --context kind-cilium-lab get ciliumnetworkpolicies -A
```

## Exercício com prova funcional

O motor de lab suporta Kind com nome diferente quando `CLUSTER_NAME` é informado em todos os comandos:

```bash
make lab-prepare LAB=04.03 CLUSTER_NAME=cilium-lab
kubectl apply --context kind-cilium-lab -f .labs/04.03/
make lab-test LAB=04.03 CLUSTER_NAME=cilium-lab
```

Teste o IP do Pod `backend` a partir de `frontend` e `externo`. Só declare enforcement se o frontend conectar e o externo falhar de forma reproduzível. Registre labels e estado do CiliumEndpoint; Hubble é opcional.

**Limpeza:** `make lab-down LAB=04.03 CLUSTER_NAME=cilium-lab` e, após conferir que o cluster é dedicado, `kind delete cluster --name cilium-lab`. Restaure o contexto `kind-dev` antes de executar labs anteriores. Nunca altere diretamente iptables/eBPF do host neste roteiro.

[Instalação no Kind](https://docs.cilium.io/en/stable/installation/kind/) · [NetworkPolicy](https://docs.cilium.io/en/stable/security/policy/)