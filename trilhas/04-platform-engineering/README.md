# 🧰 Camada 04 · Ferramentas do ecossistema Kubernetes

[⌂ Início](../../README.md) · [🗺️ Roadmap](../../docs/roadmap.md) · [🧪 Labs](../../docs/labs.md)

> **Objetivo da camada**  
> Conhecer sete conjuntos de ferramentas relevantes do ecossistema cloud-native e compreender quais problemas resolvem no Kubernetes. O estudo aprofundado de Platform Engineering como disciplina pertence ao laboratório dedicado.

**7 infográficos publicados** · **roteiro de ferramentas** · **labs introdutórios ainda não implementados**

---

## 🧭 Mapa de capacidades

| **ENTREGA E INFRAESTRUTURA** | **GOVERNANÇA E SEGREDOS** |
| :--- | :--- |
| 🔁 **GitOps e reconciliação**<br>Argo CD aplica configurações declarativas. Crossplane estende Kubernetes para recursos de infraestrutura. | 🛡️ **Políticas e integrações**<br>Kyverno aplica políticas; External Secrets Operator sincroniza segredos externos. |
| **CAPACIDADE E REDE** | **OBSERVABILIDADE** |
| ☁️ **Nódulos e conectividade**<br>Karpenter ajusta capacidade em clouds compatíveis. Cilium combina networking, eBPF e políticas. | 📊 **Sinais operacionais**<br>Prometheus coleta métricas; Grafana permite explorá-las em dashboards e alertas. |

## 📚 Sete ferramentas para conhecer — ordem de estudo

| Aula | Ferramenta | Capacidade | Referência |
| --- | --- | --- | --- |
| 04.01 | **[Argo CD](argo-cd/README.md)** | GitOps e entrega contínua | [Documentação](https://argo-cd.readthedocs.io/en/stable/) |
| 04.02 | **[Crossplane](crossplane/README.md)** | Infraestrutura declarativa via Kubernetes | [Documentação](https://docs.crossplane.io/) |
| 04.03 | **[Kyverno](kyverno/README.md)** | Policy as Code e governança | [Documentação](https://kyverno.io/docs/) |
| 04.04 | **[External Secrets Operator](external-secrets-operator/README.md)** | Integração com provedores de segredos | [Documentação](https://external-secrets.io/latest/) |
| 04.05 | **[Karpenter](karpenter/README.md)** | Provisionamento e autoscaling de nós | [Documentação](https://karpenter.sh/docs/) |
| 04.06 | **[Cilium](cilium/README.md)** | Networking, eBPF e segurança | [Documentação](https://docs.cilium.io/) |
| 04.07 | **[Prometheus + Grafana](prometheus-grafana/README.md)** | Métricas, dashboards e alertas | [Prometheus](https://prometheus.io/docs/) · [Grafana](https://grafana.com/docs/) |

**Pré-requisito recomendado:** estudar [CRDs e Custom Resources](../03-arquitetura/crds-custom-resources/README.md) e [Custom Controllers e Operators](../03-arquitetura/custom-controllers-operators/README.md), na Camada 03, antes de aprofundar Crossplane e outros operadores.

## 🧪 Ideias de laboratórios introdutórios

| Ferramenta | Experimento proposto | Observação |
| --- | --- | --- |
| Argo CD | Sincronizar um Deployment a partir de Git | Estado desejado e drift |
| Crossplane | Declarar e reconciliar recurso de exemplo | Escolher provider apropriado ao ambiente |
| Kyverno | Impedir criação de recurso sem label | Admission e política |
| External Secrets | Sincronizar um segredo de provedor de testes | Evitar credenciais de produção |
| Karpenter | Inspecionar NodePool e escalabilidade | Requer cloud/provedor compatível; não é lab Kind puro |
| Cilium | Validar políticas de rede e observar fluxos | Exige CNI configurado |
| Prometheus + Grafana | Coletar métricas e construir dashboard | Diferenciar métricas, logs e traces |

> **Status:** este é um catálogo de estudo. Os sete labs não foram implementados nem testados neste PR; os sete infográficos estão publicados nas páginas respectivas; a revisão técnica e os laboratórios completos permanecem pendentes.

## 🎯 Checklist de aprendizado

- [ ] Associar cada ferramenta ao problema que resolve.
- [ ] Explicar a diferença entre sincronização GitOps e reconciliação de recursos externos.
- [ ] Reconhecer políticas, sincronização de segredos, rede e escalabilidade como capacidades distintas.
- [ ] Identificar quais ferramentas podem ser experimentadas localmente e quais requerem cloud.

---

[**← 03 · Arquitetura**](../03-arquitetura/README.md) · [↑ Roadmap](../../docs/roadmap.md) · [⌂ Início](../../README.md)
