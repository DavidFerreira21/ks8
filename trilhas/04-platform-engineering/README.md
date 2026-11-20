# 🧰 Camada 04 · Ferramentas do ecossistema Kubernetes

[⌂ Início](../../README.md) · [🗺️ Roadmap](../../docs/roadmap.md) · [🧪 Guia dos labs](../../docs/labs.md)

> **Objetivo da camada:** compreender, configurar e investigar ferramentas de GitOps, políticas, redes e métricas, sem confundir YAML válido com controladores realmente instalados.

**4 aulas com infográfico e teoria** · **4 labs com desafios de YAML real** · **4 complementares opcionais de arquitetura e diagnóstico**

## 🧭 Capacidades por domínio

| GitOps | Governança |
| --- | --- |
| Argo CD reconcilia o estado desejado em Git com os recursos do cluster. | Kyverno aplica políticas de admissão com CEL. |
| Rede e segurança | Observabilidade |
| Cilium oferece networking, políticas e observabilidade eBPF. | Prometheus coleta métricas; Grafana consulta séries e fornece dashboards/alertas. |

## 📚 Catálogo oficial da Camada 04

| Aula | Conceito | Aula | Lab | Complementares |
| --- | --- | --- | --- | --- |
| 04.01 | **Argo CD** | [📖 Estudar](argo-cd/README.md) | [🧪 Lab 04.01](labs/argo-cd-basico/README.md) | [Consultar](argo-cd/complementares/README.md) |
| 04.02 | **Kyverno** | [📖 Estudar](kyverno/README.md) | [🧪 Lab 04.02](labs/kyverno-basico/README.md) | [Consultar](kyverno/complementares/README.md) |
| 04.03 | **Cilium** | [📖 Estudar](cilium/README.md) | [🧪 Lab 04.03](labs/cilium-basico/README.md) | [Consultar](cilium/complementares/README.md) |
| 04.04 | **Prometheus + Grafana** | [📖 Estudar](prometheus-grafana/README.md) | [🧪 Lab 04.04](labs/prometheus-grafana-basico/README.md) | [Consultar](prometheus-grafana/complementares/README.md) |

## 🧪 Como estudar

Siga o [contrato editorial](../../docs/padrao-editorial.md). Comece pela aula, preveja o comportamento, complete o starter do lab e consulte os complementares **apenas quando fizer sentido**.

Os labs usam tipos de **API próprios das ferramentas**. Em geral, é necessário **instalar o controlador e as CRDs** antes do `kubectl apply`; `make lab-prepare LAB=04.XX` apenas cria o namespace local e copia o YAML incompleto. `make lab-up` é caminho da CI com addons, não do estudante.

[🛠️ Preparar ambientes da Camada 04](../../docs/ambientes/README.md) · [📊 Matriz dos 49 labs](../../docs/matriz-homologacao.md)

## ⚠️ Matriz de dependências e homologação

| Lab | Recurso real | Dependência para teste funcional | Kind padrão |
| --- | --- | --- | --- |
| 04.01 | Argo CD Application | Argo CD instalado e autorizado a observar namespace do lab | Não |
| 04.02 | Kyverno NamespacedValidatingPolicy | Kyverno compatível com API CEL estável e admission controller | Não |
| 04.03 | Cilium CiliumNetworkPolicy | Kind dedicado com Cilium funcionando como CNI | Não |
| 04.04 | Prometheus Operator ServiceMonitor | Prometheus Operator, seleção de ServiceMonitor e datasource Grafana | Não |

**Exclusão segura:** o motor de laboratórios verifica instâncias existentes antes de excluir CRDs usadas pelos labs; a exclusão é bloqueada se houver recursos dependentes.

**Níveis de evidência:**
- **Editorial/contrato:** conteúdo, links, starter, schema básico e checks do motor.
- **Declarativo:** recurso aceito pelo API Server **com a CRD instalada**.
- **Funcional:** reconciliação, tráfego, scrape ou aplicação de políticas observados em ambiente adequado.
- **Diagnóstico:** uma falha reproduzida foi explicada e revertida.

Um teste estático aprovado **não homologa** os quatro cenários de ferramentas. Nunca adicione credenciais reais aos manifests e não altere cloud/CNI de um ambiente compartilhado.

## ✅ Checklist de conclusão

- [ ] Expliquei como Argo CD reconcilia recursos declarados no Git e identifica drift.
- [ ] Identifiquei quais políticas são validadas por Kyverno CEL e quais são suas condições de admissão.
- [ ] Expliquei quando Cilium realmente aplica uma NetworkPolicy.
- [ ] Relacionei endpoint /metrics, ServiceMonitor, Prometheus targets e painéis Grafana.
- [ ] Registrei evidências específicas e dependências não atendidas, sem afirmar sucesso inexistente.

---

[← Camada 03](../03-arquitetura/README.md) · [↑ Roadmap](../../docs/roadmap.md) · [↑ Catálogo](../../docs/catalogo.md)
