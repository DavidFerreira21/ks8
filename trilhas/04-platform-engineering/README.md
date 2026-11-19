# 🧰 Camada 04 · Ferramentas do ecossistema Kubernetes

[⌂ Início](../../README.md) · [🗺️ Roadmap](../../docs/roadmap.md) · [🧪 Guia dos labs](../../docs/labs.md)

> **Objetivo da camada:** compreender, configurar e investigar ferramentas de GitOps, API de plataforma, políticas, segredos, capacidade, rede e métricas, sem confundir YAML válido com controladores realmente instalados.

**7 aulas com infográfico e teoria** · **7 labs com desafios de YAML real** · **7 complementares opcionais de arquitetura e diagnóstico**

## 🧭 Capacidades por domínio

| GitOps e infraestrutura | Governança e segredos |
| --- | --- |
| Argo CD reconcilia Git/cluster; Crossplane define APIs de plataforma e composições. | Kyverno aplica políticas CEL; External Secrets Operator sincroniza dados de stores externos. |
| Capacidade e comunicação | Observabilidade |
| Karpenter provisiona nós em clouds compatíveis; Cilium oferece networking, políticas e observabilidade eBPF. | Prometheus coleta métricas; Grafana consulta séries e fornece dashboards/alertas. |

## 📚 Catálogo oficial da Camada 04

| Aula | Conceito | Aula | Lab | Complementares |
| --- | --- | --- | --- | --- |
| 04.01 | **Argo CD** | [📖 Estudar](argo-cd/README.md) | [🧪 Lab 04.01](labs/argo-cd-basico/README.md) | [Consultar](argo-cd/complementares/README.md) |
| 04.02 | **Crossplane** | [📖 Estudar](crossplane/README.md) | [🧪 Lab 04.02](labs/crossplane-basico/README.md) | [Consultar](crossplane/complementares/README.md) |
| 04.03 | **Kyverno** | [📖 Estudar](kyverno/README.md) | [🧪 Lab 04.03](labs/kyverno-basico/README.md) | [Consultar](kyverno/complementares/README.md) |
| 04.04 | **External Secrets Operator** | [📖 Estudar](external-secrets-operator/README.md) | [🧪 Lab 04.04](labs/external-secrets-operator-basico/README.md) | [Consultar](external-secrets-operator/complementares/README.md) |
| 04.05 | **Karpenter** | [📖 Estudar](karpenter/README.md) | [🧪 Lab 04.05](labs/karpenter-basico/README.md) | [Consultar](karpenter/complementares/README.md) |
| 04.06 | **Cilium** | [📖 Estudar](cilium/README.md) | [🧪 Lab 04.06](labs/cilium-basico/README.md) | [Consultar](cilium/complementares/README.md) |
| 04.07 | **Prometheus + Grafana** | [📖 Estudar](prometheus-grafana/README.md) | [🧪 Lab 04.07](labs/prometheus-grafana-basico/README.md) | [Consultar](prometheus-grafana/complementares/README.md) |

## 🧪 Como estudar

Siga o [contrato editorial](../../docs/padrao-editorial.md). Comece pela aula, preveja o comportamento, complete o starter do lab e consulte os complementares **apenas quando fizer sentido**.

Os labs usam tipos de **API próprios das ferramentas**. Em geral, é necessário **instalar o controlador e as CRDs** antes do `kubectl apply`; `make lab-prepare LAB=04.XX` apenas cria o namespace local e copia o YAML incompleto. `make lab-up` é caminho da CI com addons, não do estudante. Para Karpenter há um **roteiro especial de análise offline** no Kind, porque o motor local bloqueia contextos não Kind.

## ⚠️ Matriz de dependências e homologação

| Lab | Recurso real | Dependência para teste funcional | Kind padrão |
| --- | --- | --- | --- |
| 04.01 | Argo CD Application | Argo CD instalado e autorizado a observar namespace do lab | Não |
| 04.02 | Crossplane XRD v2 | Crossplane v2, registro da XRD; Composition separada para recursos derivados | Não |
| 04.03 | Kyverno NamespacedValidatingPolicy | Kyverno compatível com API CEL estável e admission controller | Não |
| 04.04 | ESO SecretStore e ExternalSecret | External Secrets Operator e Fake Provider | Não |
| 04.05 | Karpenter NodePool | EKS AWS sandbox e provider, com **aprovação/custos** | Não (design offline) |
| 04.06 | Cilium CiliumNetworkPolicy | Kind dedicado com Cilium funcionando como CNI | Não |
| 04.07 | Prometheus Operator ServiceMonitor | Prometheus Operator, seleção de ServiceMonitor e datasource Grafana | Não |

**Exclusão segura:** o motor de laboratórios verifica instâncias existentes antes de excluir CRD/XRD; a exclusão é bloqueada se houver recursos dependentes. A prática do Karpenter é validada offline contra o arquivo escrito pelo aluno e nunca aplica NodePool por meio do motor no EKS.

**Níveis de evidência:**
- **Editorial/contrato:** conteúdo, links, starter, schema básico e checks do motor.
- **Declarativo:** recurso aceito pelo API Server **com a CRD instalada**.
- **Funcional:** reconciliação, tráfego, scrape, segredo ou capacidade observados em ambiente adequado.
- **Diagnóstico:** uma falha reproduzida foi explicada e revertida.

Um teste estático aprovado **não homologa** os sete cenários de ferramentas. Nunca adicione credenciais reais aos manifests e não altere cloud/CNI de um ambiente compartilhado.

## ✅ Checklist de conclusão

- [ ] Diferenciei Argo CD GitOps de reconciliação Crossplane de recursos compostos.
- [ ] Identifiquei quais políticas são validadas por Kyverno CEL e quais são suas condições de admissão.
- [ ] Sincronizei valores fictícios com ESO sem imprimir dados de Secrets.
- [ ] Comparei NodePool, NodeClass, NodeClaim e limites de custo sem provisionar cloud involuntariamente.
- [ ] Expliquei quando Cilium realmente aplica uma NetworkPolicy.
- [ ] Relacionei endpoint /metrics, ServiceMonitor, Prometheus targets e painéis Grafana.
- [ ] Registrei evidências específicas e dependências não atendidas, sem afirmar sucesso inexistente.

---

[← Camada 03](../03-arquitetura/README.md) · [↑ Roadmap](../../docs/roadmap.md) · [↑ Catálogo](../../docs/catalogo.md)
