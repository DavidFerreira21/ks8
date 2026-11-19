# Complementar 03.12 — Matriz de investigação de rede

[← Aula 03.12](../README.md) · [🧪 Lab 03.12](../../labs/cni-comunicacao-basico/README.md) · [↑ Camada 03](../../README.md)

> **Leitura opcional:** referência de arquitetura, comparação e diagnóstico; não substitui o percurso prático da aula e do lab.

## Quando consultar

Quando Pod resolve DNS, mas não consegue conectar ao destino, ou quando uma policy parece não ter efeito.

| Camada | Sinal | Investigação |
| --- | --- | --- |
| Pod IP | `status.podIP` preenchido | CNI e alocação de rede |
| Endereço do nó | `spec.nodeName` | Caminho entre workers |
| Service | ClusterIP e EndpointSlices | Selector e readiness |
| DNS | `nslookup` resolve nome | CoreDNS e `resolv.conf` |
| Policy | Conexão permitida/bloqueada | CNI com enforcement e policies de origem/destino |

## Sequência de diagnóstico

Teste primeiro IP do Pod, depois ClusterIP do Service, depois nome DNS. Uma falha pode acontecer em apenas uma etapa. Não atribua todo timeout ao CNI; pode haver processo sem listener.

```bash
kubectl get pods -A -o wide
kubectl get endpointslices -A
kubectl get networkpolicy -A
```

## Referências oficiais

[Cluster networking](https://kubernetes.io/docs/concepts/cluster-administration/networking/)

---

[↑ Aula 03.12](../README.md) · [↑ Camada 03](../../README.md)
