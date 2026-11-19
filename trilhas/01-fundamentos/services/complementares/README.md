# Complementar 01.05 — Caminho da requisição e pontos de falha

[← Aula 01.05](../README.md) · [🧪 Lab 01.05](../../labs/services-basico/README.md) · [↑ Camada 01](../../README.md)

> **Leitura opcional:** Consulte ao investigar tráfego para um Service que existe, mas não responde. Não substitui a aula nem o desafio do laboratório.

## Decisões e sintomas

| Situação | Leitura técnica |
| --- | --- |
| **Service sem EndpointSlice pronto** | Selector, labels e readiness dos Pods. |
| **EndpointSlice correto, HTTP falha** | Port/targetPort, listener do container e dataplane. |
| **ClusterIP responde, nome não resolve** | CoreDNS, search domains e políticas de DNS. |
| **LoadBalancer sem IP externo no Kind** | Ausência de controlador compatível, não necessariamente erro do Service. |

## Como interpretar as evidências

Faça testes de Pod IP, Service IP e DNS separadamente; o resultado de cada etapa elimina hipóteses diferentes.

## Referência histórica preservada

O [material complementar original](../../../../7-services/README.md) permanece acessível, com exemplos e comandos adicionais. Esta página reúne a comparação rápida no padrão editorial das demais camadas, sem duplicar todo o material antigo.

## Referências oficiais

[Documentação Kubernetes — Conceitos](https://kubernetes.io/docs/concepts/) · [Debugging](https://kubernetes.io/docs/tasks/debug/)

---

[↑ Aula 01.05](../README.md) · [↑ Camada 01](../../README.md)
