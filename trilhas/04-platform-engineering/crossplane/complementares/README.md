# Complementar 04.02 — API de plataforma: XRD, Composition e Functions

[← Aula 04.02](../README.md) · [🧪 Lab 04.02](../../labs/crossplane-basico/README.md) · [↑ Camada 04](../../README.md)

> **Leitura opcional:** matriz de decisão e diagnóstico para consulta. Não é pré-requisito para executar o laboratório.

## Quando consultar

Ao definir contratos internos, capacidade self-service e separação entre consumidores e implementação.

| Recurso | Quem consome | Quem implementa |
| --- | --- | --- |
| XRD | Arquiteto da plataforma | Define schema, escopo, versionamento |
| XR | Time consumidor | Declara estado desejado |
| Composition | Plataforma | Define pipeline de recursos |
| Function | Pipeline de composição | Renderiza/transforma recursos desejados |
| Provider | Controller da plataforma | Reconciliador de recurso externo |

## Diferença entre Crossplane v1 e v2

Na v2, APIs de XRD mudaram e XR namespaced é o padrão. Não use exemplos que dependem de Claims/Composition nativa legada sem verificar a versão. Um XR sem Composition **não cria recursos**, e status Ready depende de reconciliação real.

```bash
kubectl get xrd
kubectl get compositions
kubectl get functions.pkg.crossplane.io
kubectl get providers.pkg.crossplane.io
```

**Segurança:** XRD/Compositions têm implicações de escopo e permissões, mesmo sem cloud. Trate versões como contratos de API.

## Referências oficiais

[Crossplane v2](https://docs.crossplane.io/latest/whats-new/) · [XRD](https://docs.crossplane.io/latest/composition/composite-resource-definitions/)

---

[↑ Aula 04.02](../README.md) · [↑ Camada 04](../../README.md)
