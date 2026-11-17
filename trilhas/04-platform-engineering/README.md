# 🔀 Camada 04 · Platform Engineering e GitOps

[⌂ Início](../../README.md) · [🗺️ Roadmap](../../docs/roadmap.md) · [🧪 Labs](../../docs/labs.md)

> **Objetivo da camada**  
> Entender como Kubernetes pode oferecer APIs declarativas, reconciliação, políticas e GitOps como capacidades de uma plataforma.

**8 conceitos planejados** · **roteiro de estudo** · **laboratórios a implementar**

---

## 🧭 Mapa de capacidades da plataforma

| **EXTENSIBILIDADE** | **ENTREGA DECLARATIVA** |
| :--- | :--- |
| 🧩 **Novos tipos de recursos e controladores.**<br>CRDs e Operators ampliam o comportamento da API.<br><br>[**Custom Resources →**](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/) | 🔁 **Git e estado desejado.**<br>Argo CD reconcilia workloads; Crossplane aplica o mesmo modelo a recursos de infraestrutura.<br><br>[**GitOps / Argo CD →**](https://argo-cd.readthedocs.io/en/stable/) |
| **SEGURANÇA E SEGREDOS** | **CAPACIDADE E OBSERVABILIDADE** |
| 🛡️ **Políticas e integrações externas.**<br>Kyverno estabelece guardrails; External Secrets gerencia sincronização de segredos.<br><br>[**Kyverno →**](https://kyverno.io/docs/) | 📈 **Nós e sinais operacionais.**<br>Karpenter provisiona capacidade em ambientes compatíveis; observabilidade explica o comportamento dos sistemas.<br><br>[**OpenTelemetry →**](https://opentelemetry.io/docs/) |

## 📚 Catálogo de tecnologias e conceitos

### 🧩 Extensibilidade da API

| Conceito | Papel na plataforma | Documentação |
| --- | --- | --- |
| **CRD e Custom Controllers** | Criar novos recursos e reconciliar estados | [Kubernetes Custom Resources](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/) |
| **Kubernetes Operators** | Encapsular conhecimento operacional em controladores | [Operator Pattern](https://kubernetes.io/docs/concepts/extend-kubernetes/operator/) |

### 🔁 GitOps e infraestrutura declarativa

| Conceito | Papel na plataforma | Documentação |
| --- | --- | --- |
| **Argo CD e GitOps** | Sincronizar configuração declarativa a partir do Git | [Argo CD](https://argo-cd.readthedocs.io/en/stable/) |
| **Crossplane** | Compor APIs de infraestrutura e reconciliar recursos | [Crossplane](https://docs.crossplane.io/) |

### 🛡️ Governança, operação e automação

| Conceito | Papel na plataforma | Documentação |
| --- | --- | --- |
| **Kyverno e Policy as Code** | Aplicar e auditar políticas declarativas | [Kyverno](https://kyverno.io/docs/) |
| **External Secrets Operator** | Sincronizar dados de provedores de segredos | [External Secrets](https://external-secrets.io/latest/) |
| **Karpenter** | Provisionar nós conforme demanda e restrições em provedores compatíveis | [Karpenter](https://karpenter.sh/docs/) |
| **Observabilidade** | Correlacionar métricas, logs e traces | [OpenTelemetry](https://opentelemetry.io/docs/) |

**Estado atual:** estas são **páginas de orientação e referências**, não labs implementados. A camada não pressupõe que todos os componentes funcionem no Kind sem dependências adicionais.

## 🧪 Evolução prática sugerida

| Fase | O que construir | Aprendizado principal |
| :---: | --- | --- |
| **01** | Argo CD reconciliando uma aplicação local | Estado desejado e drift |
| **02** | Policy com Kyverno para labels obrigatórias | Guardrails declarativos |
| **03** | CRD simples com controller ou Operator de exemplo | API estendida e reconciliação |
| **04** | Crossplane com provider apropriado para ambiente local | Recursos compostos e APIs de plataforma |
| **05** | Pipeline de sinais e instrumentação de aplicação | Métricas, logs, traces e diagnóstico |

> **Princípio:** primeiro observar a reconciliação, depois automatizar. Crossplane e Karpenter exigem requisitos específicos; evite associar credenciais de nuvem a exercícios locais sem necessidade.

## 🎯 Checklist de aprendizado

- [ ] Explicar por que CRDs sozinhas não executam reconciliação.
- [ ] Diferenciar GitOps de uma pipeline imperativa de deploy.
- [ ] Identificar o papel de Policy as Code e gestão de segredos.
- [ ] Descrever como uma plataforma oferece capacidades reutilizáveis em vez de expor apenas ferramentas.

## 🎨 Material visual

A coleção de infográficos foi produzida, mas os PNGs ainda não estão no GitHub. Confira a [convenção de publicação e revisão](../../docs/infograficos.md).

---

[**← 03 · Arquitetura**](../03-arquitetura/README.md) · [↑ Roadmap](../../docs/roadmap.md) · **[⌂ Voltar ao início](../../README.md)**
