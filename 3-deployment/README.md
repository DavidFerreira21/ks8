# Complementar 01.03 — Operação e investigação de Deployments

[← Aula 01.03](../trilhas/01-fundamentos/deployments/README.md) · [🧪 Lab 01.03](../trilhas/01-fundamentos/labs/deployments-basico/README.md) · [↑ Camada 01](../trilhas/01-fundamentos/README.md)

> **Leitura opcional:** referência de comandos e sinais operacionais para Deployments. A criação declarativa pertence ao lab; os experimentos de atualização/rollback pertencem ao [Lab 01.12](../trilhas/01-fundamentos/labs/estrategias-deployment-basico/README.md).

## Quando consultar

- Quando um rollout está parado ou demora mais que o esperado.
- Quando precisar identificar qual ReplicaSet pertence a uma revisão.
- Ao comparar reinício, atualização e rollback antes de operar um ambiente.

## Comandos de consulta

```bash
kubectl get deployment web -n NAMESPACE
kubectl describe deployment web -n NAMESPACE
kubectl get rs,pods -n NAMESPACE -l app=web
kubectl rollout status deployment/web -n NAMESPACE --timeout=120s
kubectl rollout history deployment/web -n NAMESPACE
kubectl get deployment web -n NAMESPACE -o yaml
```

Os nomes são ilustrativos: ajuste `NAMESPACE`, `web` e labels ao Deployment real.

## Referência de operações que modificam estado

| Operação | Comando | Efeito |
| --- | --- | --- |
| Alterar imagem | `kubectl set image deployment/web nginx=nginx:VERSAO -n NAMESPACE` | Altera o Pod template, iniciando nova revisão |
| Reiniciar Pods | `kubectl rollout restart deployment/web -n NAMESPACE` | Atualiza o template com anotação de restart; recria Pods sem necessariamente mudar imagem |
| Desfazer revisão | `kubectl rollout undo deployment/web -n NAMESPACE` | Restaura template de uma revisão anterior |
| Pausar atualização | `kubectl rollout pause deployment/web -n NAMESPACE` | Suspende progresso de atualização do Deployment |
| Retomar atualização | `kubectl rollout resume deployment/web -n NAMESPACE` | Retoma o rollout pausado |

**Atenção:** os comandos acima alteram recursos. Execute-os apenas no seu cluster de estudo ou com autorização apropriada. Não use comandos incompletos como `kubectl rollout undo` sem indicar o recurso.

## Por que um rollout pode travar?

| Sinal | O que investigar |
| --- | --- |
| `ProgressDeadlineExceeded` | Readiness, pull de imagem, recursos, quotas e erros nos novos Pods |
| Novo ReplicaSet com réplicas indisponíveis | `kubectl describe pod`, eventos e logs |
| ReplicaSets antigos e novos coexistem | Estratégia de RollingUpdate e quantidade de Pods prontos |
| Histórico sem `change-cause` | O Kubernetes não registra automaticamente uma justificativa humana para cada revisão |

O número de revisão está associado a mudanças no **Pod template**, não a qualquer edição de metadata do Deployment.

## Boas práticas e limitações

- Compare `spec.replicas`, `status.readyReplicas` e `status.updatedReplicas` antes de concluir que terminou.
- Em ambientes GitOps, alterações imperativas podem sofrer reconciliação de volta ao estado declarado no Git.
- Rollback não corrige automaticamente falhas externas, como indisponibilidade de registry, volumes ou rede.

## Referências oficiais

- [Deployments](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/)
- [kubectl rollout](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_rollout/)
- [Aula 01.12 — Estratégias de Deployment](../trilhas/01-fundamentos/estrategias-deployment/README.md)
