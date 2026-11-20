# Complementar 04.03 — Cilium e enforcement: evidências

[← Aula 04.03](../README.md) · [🧪 Lab 04.03](../../labs/cilium-basico/README.md) · [↑ Camada 04](../../README.md)

> **Leitura opcional:** matriz de decisão e diagnóstico para consulta. Não é pré-requisito para executar o laboratório.

## Quando consultar

Ao substituir kube-proxy, implantar eBPF, criar políticas ou investigar tráfego negado.

| Dimensão | Declaração | Prova funcional |
| --- | --- | --- |
| Cilium CNI | Pods Cilium Ready | Conectividade Pod-to-Pod |
| CiliumNetworkPolicy | Objeto aceito | Origem permitida conecta, negada não conecta |
| eBPF dataplane | Configuração em Cilium | Fluxos/estado, de acordo com modo instalado |
| Hubble | Relay/UI configurados | Eventos de fluxo ou métricas de rede |

## Método de troubleshooting

Confirme que os endpoints pertencem ao Cilium, os labels selecionam os Pods certos e não há outra policy permitindo tráfego. Compare conexão direta por IP antes/depois. Falha de DNS ou de processo não é prova de enforcement.

```bash
kubectl get ciliumendpoints -n lab-04-06
kubectl get ciliumnetworkpolicies -n lab-04-06 -o yaml
```

Não instale Cilium sobre CNI padrão de cluster compartilhado apenas para executar teste.

## Referências oficiais

[Cilium Policy](https://docs.cilium.io/en/stable/security/policy/)

---

[↑ Aula 04.03](../README.md) · [↑ Camada 04](../../README.md)
