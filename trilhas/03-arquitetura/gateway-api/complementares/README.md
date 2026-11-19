# Complementar 03.16 — Gateway API: responsabilidade e status

[← Aula 03.16](../README.md) · [🧪 Lab 03.16](../../labs/gateway-api-basico/README.md) · [↑ Camada 03](../../README.md)

> **Leitura opcional:** referência de arquitetura, comparação e diagnóstico; não substitui o percurso prático da aula e do lab.

## Quando consultar

Ao comparar Ingress e Gateway API ou investigar uma rota declarada que não recebe tráfego.

| Objeto | Responsabilidade | Observação |
| --- | --- | --- |
| GatewayClass | Identifica implementação/controller | Accepted/status da classe |
| Gateway | Listeners, TLS, endereços | Programmed, Accepted |
| HTTPRoute | Matches, filtros e backends | Accepted, ResolvedRefs |
| Service | Endereço interno do backend | EndpointSlices/Ready |

## Diagnóstico em duas etapas

Primeiro confirme CRDs: `kubectl api-resources --api-group=gateway.networking.k8s.io`. Depois procure controller compatível, objeto GatewayClass e condições de HTTPRoute. A falta de CRD causa erro de tipo desconhecido; a falta de controlador pode deixar objetos declarados sem configuração efetiva do dataplane.

**O lab principal valida backend nativo no Kind.** Não confunda a existência de `examples/httproute.yaml` com execução funcional do Gateway API.

## Referências oficiais

[Gateway API](https://gateway-api.sigs.k8s.io/)

---

[↑ Aula 03.16](../README.md) · [↑ Camada 03](../../README.md)
