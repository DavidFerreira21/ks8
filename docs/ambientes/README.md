# Ambientes de homologação — Camada 04

[⌂ Início](../../README.md) · [↑ Camada 04](../../trilhas/04-platform-engineering/README.md) · [🧪 Guia geral](../labs.md)

> **Objetivo:** tornar cada controlador instalável de forma consciente e seu resultado verificável. A execução da CI Kind padrão **não substitui** esta preparação com addon. Escolha uma versão estável real, registre-a e execute no ambiente descartável.

| Lab | Ferramenta | Guia | Principal evidência |
| --- | --- | --- | --- |
| 04.01 | Argo CD | [Preparar](04-argo-cd.md) | Application Synced/Healthy |
| 04.02 | Kyverno CEL | [Preparar](04-kyverno.md) | Deny vs permitido |
| 04.03 | Cilium CNI | [Preparar](04-cilium.md) | Ingress permitido e bloqueado |
| 04.04 | Prometheus + Grafana | [Preparar](04-prometheus-grafana.md) | Target UP e consulta no Grafana |

## Contrato de homologação

1. Identifique cluster/contexto e registre versões do Kubernetes, Helm e addon.
2. Instale CRDs e controlador **no cluster de estudo** e com permissões mínimas.
3. Confirme health dos componentes e discovery do tipo de recurso.
4. Execute o desafio YAML do lab, teste hipótese e compare resultado com o esperado.
5. Documente evidência **declarativa**, **funcional**, **diagnóstica** e cleanup.
6. Desinstale somente recursos e addons exclusivos do seu ambiente.

**Cuidado:** um recurso CRD aceito pode permanecer sem reconciliação; um Helm install bem-sucedido não prova que todos os pods do controlador estão Ready. Cilium requer Kind dedicado com outra configuração de CNI.

[Contrato editorial](../padrao-editorial.md) · [Matriz de homologação de 49 labs](../matriz-homologacao.md)
