# Complementar 01.10 — Readiness, liveness e startup em produção

[← Aula 01.10](../README.md) · [🧪 Lab 01.10](../../labs/probes-basico/README.md) · [↑ Camada 01](../../README.md)

> **Leitura opcional:** Use para escolher que tipo de falha deve retirar o Pod de tráfego e qual deve reiniciar o container. Não substitui a aula nem o desafio do laboratório.

## Decisões e sintomas

| Situação | Leitura técnica |
| --- | --- |
| **readiness** | Controla prontidão do destino; falhar não reinicia o processo. |
| **liveness** | Indica execução irrecuperável; falha repetida pode reiniciar container. |
| **startup** | Protege aplicações com inicialização lenta de liveness/readiness prematuros. |
| **initialDelay + thresholds** | Precisam representar tempo de inicialização e falha reais; não mascarar saturação. |

## Como interpretar as evidências

Valide o efeito nos `containerStatuses.restartCount` e na condição Ready: ambos não reagem da mesma forma.

## Referência histórica preservada

O [material complementar original](../../../../5-probes/README.md) permanece acessível, com exemplos e comandos adicionais. Esta página reúne a comparação rápida no padrão editorial das demais camadas, sem duplicar todo o material antigo.

## Referências oficiais

[Documentação Kubernetes — Conceitos](https://kubernetes.io/docs/concepts/) · [Debugging](https://kubernetes.io/docs/tasks/debug/)

---

[↑ Aula 01.10](../README.md) · [↑ Camada 01](../../README.md)
