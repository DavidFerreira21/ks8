# Preparação 04.05 — Karpenter com segurança de custos

[↑ Ambientes](README.md) · [🧪 Lab 04.05](../../trilhas/04-platform-engineering/labs/karpenter-basico/README.md)

> **Não instale Karpenter no Kind padrão para simular nós AWS.** A primeira etapa do aprendizado é offline; execução do controller depende de **EKS sandbox autorizado**, conta isolada, IAM, rede, orçamento e permissões.

## Etapa 1 — Validar o arquivo local (sem AWS)

```bash
kubectl config current-context    # kind-dev
make lab-prepare LAB=04.05
# Complete todos os TODOs em .labs/04.05/resources.yaml
python3 scripts/validate_karpenter_lab.py .labs/04.05/resources.yaml
```

O validador exige `limits.nodes: 0` e `EC2NodeClass` propositalmente inexistente. Não cria Nodes ou NodeClaims.

## Etapa 2 — Pré-requisitos EKS (opcional)

Defina região, conta sandbox, tags de descoberta, IAM e limites de gastos antes da instalação. Use o [guia oficial de Karpenter para EKS](https://karpenter.sh/docs/getting-started/getting-started-with-karpenter/) para instalar versão compatível de controller e EC2NodeClass. Não misture o provider Karpenter AWS com a `NodeClass` nativa do EKS Auto Mode.

```bash
kubectl --context CONTEXTO_EKS_SANDBOX api-resources --api-group=karpenter.sh
kubectl --context CONTEXTO_EKS_SANDBOX get nodepools,nodeclaims
# Só após revisão de permissões, cluster e limites:
# kubectl --context CONTEXTO_EKS_SANDBOX apply -f .labs/04.05/resources.yaml
```

Não execute `make lab-up` ou `make lab-down` em EKS; o motor só aceita Kind. Como a NodeClass é inexistente e o limite é zero, o **comportamento esperado** é não provisionar, não testar autoscaling.

## Evidência e reversão

Registre `kubectl get nodepool -o yaml` (sem credenciais), condições e número de NodeClaims. Antes de sair, se o NodePool opcional foi aplicado no EKS, remova-o explicitamente com `kubectl --context CONTEXTO_EKS_SANDBOX delete -f .labs/04.05/resources.yaml` e verifique recursos remanescentes. **Nunca aumente o limite de nós neste lab**.

[NodePool](https://karpenter.sh/docs/concepts/nodepools/) · [NodeClass](https://karpenter.sh/docs/concepts/nodeclasses/)