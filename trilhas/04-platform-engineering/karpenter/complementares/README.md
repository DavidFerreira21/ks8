# Complementar 04.05 — Capacidade: NodePool e custo

[← Aula 04.05](../README.md) · [↑ Camada 04](../../README.md)

> **Leitura opcional:** matriz de decisão e diagnóstico para consulta. Não há laboratório 04.05 nesta trilha: esta é uma leitura conceitual opcional.

## Quando consultar

Ao avaliar pools de nós, consolidar capacidade, restringir custos e escolher entre autoscaling gerenciado e self-managed.

| Conceito | Função | Limite |
| --- | --- | --- |
| Pod Pending | Demanda por capacidade | Pode ser restrição de selector, não falta de nó |
| NodePool | Regras/capacidade permitida | Pode ser NotReady |
| NodeClass | Configuração do provedor | Requer rede/IAM válida |
| NodeClaim | Pedido e lifecycle do nó | Não garante Node Ready |
| HPA | Quantidade de Pods | Não aumenta nós por si só |

## Separação de produtos

**Karpenter AWS provider:** usa `EC2NodeClass` e `karpenter.k8s.aws`. **EKS Auto Mode:** expõe NodeClass gerenciada no grupo `eks.amazonaws.com`; configuração e responsabilidades diferem. Não misture os dois manifests.

Em qualquer análise real, `limits.nodes` restringe capacidade, mas não substitui controle de custos, quotas ou a revisão da `EC2NodeClass`. Provisionamento real exige conta de sandbox, IAM, orçamento e aprovação; **não é objeto de exercício nesta trilha**.

## Referências oficiais

[Karpenter NodePool](https://karpenter.sh/docs/concepts/nodepools/) · [NodeClass](https://karpenter.sh/docs/concepts/nodeclasses/)

---

[↑ Aula 04.05](../README.md) · [↑ Camada 04](../../README.md)
