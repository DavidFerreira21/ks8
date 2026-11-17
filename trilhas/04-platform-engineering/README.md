# Camada 04 — Platform Engineering e GitOps

[← Roadmap](../../docs/roadmap.md) · [Início](../../README.md)

> 🔀 **CAMADA 04 · TRILHA KUBERNETES**  
> Explore reconciliação, extensibilidade, políticas e GitOps.

### Acesso rápido

[**🗺️ Roadmap**](../../docs/roadmap.md) · [**🧪 Laboratórios**](../../docs/labs.md) · [**🎨 Convenção visual**](../../docs/infograficos.md)

---

**Objetivo:** evoluir dos recursos nativos do Kubernetes para extensibilidade, políticas, automação, GitOps e uma abordagem de plataforma como produto.

## Roteiro de estudo

| Tópico | Conceito principal | Situação |
| --- | --- | --- |
| CRDs e Custom Controllers | Estender a API e reconciliar novos recursos | Aula/lab a estruturar |
| Operators | Automatizar operações de ciclo de vida | Aula/lab a estruturar |
| Argo CD e GitOps | Git como fonte declarativa do estado desejado | Aula/lab a estruturar |
| Crossplane | APIs de infraestrutura e composições | Aula/lab a estruturar |
| Kyverno e Policy as Code | Guardrails declarativos | Aula/lab a estruturar |
| External Secrets Operator | Sincronização controlada de segredos externos | Aula/lab a estruturar |
| Karpenter | Provisionamento dinâmico de nós | Estudo conceitual primeiro; demanda ambiente compatível |
| Observabilidade | Métricas, logs, traces e alertas | Aula/lab a estruturar |

## Evolução prática sugerida (ainda não implementada)

- Instalar Argo CD no ambiente local e reconciliar uma aplicação de exemplo.
- Criar uma política Kyverno para exigir labels.
- Explorar um recurso customizado e o comportamento de seu controller.
- Demonstrar Crossplane com um provider adequado ao laboratório, sem exigir uma conta cloud nos exercícios iniciais.
- Instrumentar uma aplicação e observar métricas, logs e traces.

**Princípio do lab:** primeiro entender a reconciliação e observar seu funcionamento; somente depois adicionar automação e camadas de abstração. Exercícios que exigem serviços externos devem ter pré-requisitos explícitos.

## Referências oficiais

- [Custom Resources](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/)
- [Operator Pattern](https://kubernetes.io/docs/concepts/extend-kubernetes/operator/)
- [Argo CD](https://argo-cd.readthedocs.io/en/stable/)
- [Crossplane](https://docs.crossplane.io/)
- [Kyverno](https://kyverno.io/docs/)
- [External Secrets Operator](https://external-secrets.io/latest/)
- [Karpenter](https://karpenter.sh/docs/)
- [OpenTelemetry](https://opentelemetry.io/docs/)

**Voltar ao** [Roadmap](../../docs/roadmap.md).


---

### Continue estudando

[← 03 · Arquitetura](../03-arquitetura/README.md) · [↑ Índice da trilha](../../docs/roadmap.md) · [⌂ Voltar ao início](../../README.md)
