# 🧰 Camada 04 · Ferramentas do ecossistema Kubernetes

[⌂ Início](../../README.md) · [🗺️ Roadmap](../../docs/roadmap.md) · [🧪 Guia dos labs](../../docs/labs.md)

> **Objetivo da camada:** compreender, configurar e investigar ferramentas de GitOps, API de plataforma, políticas, segredos, capacidade, rede e métricas, sem confundir YAML válido com controladores realmente instalados.

**7 aulas com infográfico e teoria** · **5 labs práticos** · **7 complementares opcionais de arquitetura e diagnóstico**

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
| 04.04 | **External Secrets Operator** | [📖 Estudar](external-secrets-operator/README.md) | — *Aula teórica, sem lab* | [Consultar](external-secrets-operator/complementares/README.md) |
| 04.05 | **Karpenter** | [📖 Estudar](karpenter/README.md) | — *Aula teórica, sem lab* | [Consultar](karpenter/complementares/README.md) |
| 04.06 | **Cilium** | [📖 Estudar](cilium/README.md) | [🧪 Lab 04.06](labs/cilium-basico/README.md) | [Consultar](cilium/complementares/README.md) |
| 04.07 | **Prometheus + Grafana** | [📖 Estudar](prometheus-grafana/README.md) | [🧪 Lab 04.07](labs/prometheus-grafana-basico/README.md) | [Consultar](prometheus-grafana/complementares/README.md) |

## 🧪 Como estudar

Siga o [contrato editorial](../../docs/padrao-editorial.md). Comece pela aula e consulte os complementares **apenas quando fizer sentido**. Nos cinco temas com laboratório (04.01, 04.02, 04.03, 04.06 e 04.07), preveja o comportamento, complete o starter e valide suas evidências. **04.04 (ESO) e 04.05 (Karpenter) são aulas teóricas, sem laboratório executável.**

Os cinco labs existentes usam **APIs reais das ferramentas** e exigem controladores/CRDs compatíveis. `make lab-prepare LAB=04.XX` prepara apenas labs registrados; `make lab-up` é reservado à CI. **Não existem `make lab-prepare LAB=04.04` ou `LAB=04.05`.** Para ESO e Karpenter, estude conceitos, exemplos interpretados e complementares, sem instalar addons ou provisionar infraestrutura.

[🛠️ Preparar ambientes da Camada 04](../../docs/ambientes/README.md) · [📊 Matriz dos 50 labs](../../docs/matriz-homologacao.md)

## ⚠️ Matriz de dependências e homologação

| Lab | Recurso real | Dependência para teste funcional | Kind padrão |
| --- | --- | --- | --- |
| 04.01 | Argo CD Application | Argo CD instalado e autorizado a observar namespace do lab | Não |
| 04.02 | Crossplane XRD v2 | Crossplane v2, registro da XRD; Composition separada para recursos derivados | Não |
| 04.03 | Kyverno NamespacedValidatingPolicy | Kyverno compatível com API CEL estável e admission controller | Não |
| 04.06 | Cilium CiliumNetworkPolicy | Kind dedicado com Cilium funcionando como CNI | Não |
| 04.07 | Prometheus Operator ServiceMonitor | Prometheus Operator, seleção de ServiceMonitor e datasource Grafana | Não |

**Exclusão segura:** o motor protege definições globais como CRD/XRD e não permite exclusão enquanto houver recursos dependentes. Não existem labs de ESO ou Karpenter nesta camada; nenhum exercício deste currículo cria NodePools ou conecta stores de segredos.

**Níveis de evidência:**
- **Editorial/contrato:** conteúdo, links, starter, schema básico e checks do motor.
- **Declarativo:** recurso aceito pelo API Server **com a CRD instalada**.
- **Funcional:** reconciliação, tráfego, scrape, segredo ou capacidade observados em ambiente adequado.
- **Diagnóstico:** uma falha reproduzida foi explicada e revertida.

Um teste estático aprovado **não homologa** os cinco cenários práticos de ferramentas. Nunca adicione credenciais reais aos manifests e não altere cloud/CNI de um ambiente compartilhado.

## ✅ Checklist de conclusão

- [ ] Diferenciei Argo CD GitOps de reconciliação Crossplane de recursos compostos.
- [ ] Identifiquei quais políticas são validadas por Kyverno CEL e quais são suas condições de admissão.
- [ ] Expliquei como o ESO sincroniza segredos, quais permissões requer e como evitar exposição de dados; esta aula não tem lab.
- [ ] Comparei conceitualmente NodePool, NodeClass, NodeClaim, HPA e custos do Karpenter; esta aula não tem lab.
- [ ] Expliquei quando Cilium realmente aplica uma NetworkPolicy.
- [ ] Relacionei endpoint /metrics, ServiceMonitor, Prometheus targets e painéis Grafana.
- [ ] Registrei evidências específicas e dependências não atendidas, sem afirmar sucesso inexistente.

---

[← Camada 03](../03-arquitetura/README.md) · [↑ Roadmap](../../docs/roadmap.md) · [↑ Catálogo](../../docs/catalogo.md)
