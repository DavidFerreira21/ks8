# Complementar 03.13 — Dataplane de Service e eBPF

[← Aula 03.13](../README.md) · [🧪 Lab 03.13](../../labs/kube-proxy-ebpf-basico/README.md) · [↑ Camada 03](../../README.md)

> **Leitura opcional:** referência de arquitetura, comparação e diagnóstico; não substitui o percurso prático da aula e do lab.

## Quando consultar

Ao avaliar migração de kube-proxy para dataplane alternativo ou investigar conexão por ClusterIP.

## Separação de responsabilidades

- **Service e EndpointSlice:** estado declarativo da API e backends observados.
- **kube-proxy:** implementação de regras de encaminhamento quando usado pela distribuição.
- **eBPF:** mecanismo no kernel utilizado por soluções especializadas para rede, observabilidade e políticas.

| Cenário | Interpretação |
| --- | --- |
| Service sem endpoints | Selector/readiness; não comprova erro no dataplane |
| EndpointSlice correto mas timeout | Investigar dataplane, portas e aplicação |
| kube-proxy ausente | Pode haver dataplane substituto ou configuração específica |
| eBPF habilitado | Não elimina API Service e descoberta de endpoints |

## Inspeção segura

```bash
kubectl get svc,endpointslices -n lab-03-13
kubectl get ds -n kube-system
```

Não edite iptables/nftables no host nem substitua o dataplane no Kind durante este lab.

## Referências oficiais

[Virtual IPs e Service proxies](https://kubernetes.io/docs/reference/networking/virtual-ips/)

---

[↑ Aula 03.13](../README.md) · [↑ Camada 03](../../README.md)
