# Experimento avançado 03.13 — Service dataplane com Cilium

[← Lab 03.13](../README.md) · [↑ Preparação do Cilium](../../../../../docs/ambientes/04-cilium.md)

> **Opcional:** use um Kind dedicado `cilium-lab` com Cilium instalado como CNI. Não altere CNI ou kube-proxy de clusters compartilhados.

## Hipótese

A API Service/EndpointSlice continua existindo com ou sem dataplane eBPF. A conectividade HTTP via ClusterIP confirma encaminhamento; `cilium status` identifica se o Cilium está realmente no caminho. **Isso não comprova substituição do kube-proxy se a função não estiver habilitada.**

## Preparar e inspecionar

```bash
kubectl config use-context kind-cilium-lab
cilium status --context kind-cilium-lab --wait
make lab-prepare LAB=03.13 CLUSTER_NAME=cilium-lab
kubectl apply --context kind-cilium-lab -f .labs/03.13/
make lab-test LAB=03.13 CLUSTER_NAME=cilium-lab
kubectl --context kind-cilium-lab get ciliumendpoints -n lab-03-13
kubectl --context kind-cilium-lab get svc,endpointslices -n lab-03-13
```

## Criar cliente e testar dataplane

```bash
kubectl --context kind-cilium-lab apply -f trilhas/03-arquitetura/labs/kube-proxy-ebpf-basico/experiments/cliente.yaml
kubectl --context kind-cilium-lab wait -n lab-03-13 --for=condition=Ready pod/cliente --timeout=120s
kubectl --context kind-cilium-lab exec -n lab-03-13 cliente -- wget -T 5 -qO- http://web
cilium status --context kind-cilium-lab --verbose
```

Faça o experimento de selector do Lab 03.13 e repita o HTTP antes/depois de restaurá-lo. Se o HTTP falhar, investigue EndpointSlices, porta 80, readiness de nginx e status do Cilium. Para verificar dataplane eBPF, registre a saída de `cilium status` e dos endpoints Cilium, não apenas a existência da API Service.

**Kube-proxy replacement:** só marque como validado se o **Cilium reportar replacement ativo** e o cluster tiver sido criado com essa configuração seguindo o procedimento oficial. O Kind com Cilium padrão pode continuar usando kube-proxy; nesse caso a observação confirma Cilium como CNI e não substituição total de Service proxy.

## Limpeza

```bash
kubectl --context kind-cilium-lab delete -f trilhas/03-arquitetura/labs/kube-proxy-ebpf-basico/experiments/cliente.yaml --ignore-not-found
make lab-down LAB=03.13 CLUSTER_NAME=cilium-lab
```

Não exclua a CNI ou o cluster se outros labs estiverem em uso. Registre a versão do Cilium e o modo de dataplane.

[Cilium no Kind](https://docs.cilium.io/en/stable/installation/kind/) · [Service proxy](https://kubernetes.io/docs/reference/networking/virtual-ips/)
