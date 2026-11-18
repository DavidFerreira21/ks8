<div align="center">

# ☸️ Kubernetes Visual Guide

**Dos fundamentos às ferramentas do ecossistema Kubernetes — uma trilha prática e visual em português.**

Aprenda os conceitos, execute laboratórios com **Kind**, investigue o comportamento do cluster e avance até **extensibilidade, GitOps e ferramentas cloud-native**.

![Kubernetes](https://img.shields.io/badge/Kubernetes-Learning%20Path-326CE5?style=flat-square&logo=kubernetes&logoColor=white)
![Tópicos](https://img.shields.io/badge/52%20aulas-no%20cat%C3%A1logo-334155?style=flat-square)
![Camadas](https://img.shields.io/badge/4%20camadas-de%20estudo-0F766E?style=flat-square)
![Ambiente](https://img.shields.io/badge/Labs-Kind-8B5CF6?style=flat-square)
![Status](https://img.shields.io/badge/Projeto-em%20evolu%C3%A7%C3%A3o-D97706?style=flat-square)

[**Catálogo de 52 aulas e imagens**](docs/catalogo.md) · [**Começar a estudar**](docs/roadmap.md) · [**Preparar o Kind**](install-kind.md) · [**Explorar os labs**](docs/labs.md)

</div>

---

## 🧭 Escolha sua trilha

Quatro camadas complementares: **usar → operar → compreender → explorar ferramentas**.

| **01 · Fundamentos** | **02 · Operação e Segurança** |
| :--- | :--- |
| 📦 **Workloads, configuração e acesso**<br>Pods, Deployments, Services, Probes, Volumes e mais.<br><br>**[Explorar fundamentos →](trilhas/01-fundamentos/README.md)** | 🛡️ **Confiabilidade e governança**<br>RBAC, NetworkPolicy, Scheduling, Quotas e PDB.<br><br>**[Explorar operação →](trilhas/02-operacao-seguranca/README.md)** |


| **03 · Arquitetura e Infraestrutura** | **04 · Ferramentas do Ecossistema** |
| :--- | :--- |
| 🧩 **Como o cluster funciona**<br>API Server, etcd, Scheduler, kubelet, CNI, CSI e DNS.<br><br>**[Explorar arquitetura →](trilhas/03-arquitetura/README.md)** | 🧰 **Ferramentas cloud-native**<br>Argo CD, Crossplane, Kyverno, External Secrets, Karpenter, Cilium e Prometheus/Grafana.<br><br>**[Explorar ferramentas →](trilhas/04-platform-engineering/README.md)** |

> **Como interpretar a trilha:** as **52 aulas** formam o catálogo curricular, com guias publicados e outros planejados; nem todos possuem laboratório executável. **Os 52 infográficos PNG estão no repositório**, integrados às páginas das aulas. A revisão técnica das ilustrações continua recomendada. As páginas mostram o estado real de cada exercício.

## 🚀 Comece em 3 passos

| Passo | Sua ação | Material |
| :---: | --- | --- |
| **01** | Configure o cluster local com um Control Plane e dois Workers | [Guia Kind + WSL](install-kind.md) |
| **02** | Explore a API e o estado declarativo, começando pelo Lab 01.01 | [Lab 01.01 — Fundamentos](trilhas/01-fundamentos/labs/fundamentos-cluster/README.md) |
| **03** | Após Pods e Deployments, estude como Services descobrem e acessam os backends | [Lab 01.05 — Services](trilhas/01-fundamentos/labs/services-basico/README.md) |

```bash
make up          # Cria o cluster Kind local
make nodes       # Confere os nós
make validate    # Executa validação estática dos exemplos
make lab-up      # Aplica ConfigMap do primeiro lab (01.01)
make lab-test    # Confere o recurso registrado no lab
make lab-down    # Remove apenas recursos do lab
```

> **Antes de executar:** confira `kubectl config current-context`. `make down` é diferente de `make lab-down`: o primeiro apaga o cluster Kind inteiro.

## 🧰 Interface de laboratórios

O projeto agora oferece uma interface única para descobrir, executar e diagnosticar os labs registrados em `lab.yaml`:

```bash
make doctor
make up
make labs
make lab-up LAB=01.01
make lab-observe LAB=01.01
make lab-test LAB=01.01
make lab-down LAB=01.01
# Após a aula 01.05: make lab-up LAB=01.05
```

Os exercícios são executados em um **Kind local** com verificação de contexto e limpeza restrita aos manifests registrados; namespaces são preservados. Para criar um novo exercício, use `make new-lab LAB_ID=01.07 LAB_SLUG=configmaps-basico` e revise o contrato antes de publicá-lo. Veja o [guia dos laboratórios](docs/labs.md).

> O motor automatiza tarefas repetitivas, mas mantém a análise de eventos, hipóteses e experimentos como parte essencial do aprendizado. Resultados de execução devem ser conferidos no GitHub Actions e no cluster local.

## 🧪 Laboratórios disponíveis

A **Camada 01 agora reúne 14 laboratórios (01.01–01.14)**, cada um com contrato, manifests e roteiro de observação por etapas. Os exercícios 01.13 (Ingress) e 01.14 (HPA) requerem addons para testes funcionais. [**Abrir índice completo da Camada 01**](trilhas/01-fundamentos/README.md).

| Laboratório | O que demonstra | Situação |
| --- | --- | --- |
| [Fundamentos — primeiro contato com a API](trilhas/01-fundamentos/labs/fundamentos-cluster/README.md) | Control Plane, Workers, ConfigMap e estado declarativo | 🧪 Manifestos disponíveis |
| [Lab 01.05 — Services](trilhas/01-fundamentos/labs/services-basico/README.md) | ClusterIP, selectors, EndpointSlices e descoberta DNS | 🧪 Manifestos disponíveis |
| [RBAC mínimo](trilhas/02-operacao-seguranca/labs/rbac-minimo/README.md) | ServiceAccount, Role, RoleBinding e permissões | 🧪 Manifestos disponíveis |
| [Quotas e limites](trilhas/02-operacao-seguranca/labs/quota-namespace/README.md) | LimitRange e rejeição por ResourceQuota | 🧪 Manifestos disponíveis |
| [Arquitetura](trilhas/03-arquitetura/README.md) | Observação dos componentes internos | 📘 Roteiro conceitual |
| [Ferramentas do ecossistema](trilhas/04-platform-engineering/README.md) | GitOps, governança, networking e observabilidade | 📘 Roteiro conceitual |

**Legenda:** 🧪 possui contrato e manifests (execução depende do ambiente e dos testes do PR) · 📘 conteúdo ou roteiro de estudo · 🚧 planejado.

## 📚 Anotações e exemplos práticos

Consulte as explicações, os comandos e os manifests que complementam os guias da trilha. Todo esse material faz parte do mesmo percurso de estudo.

<details>
<summary><strong>Mostrar anotações e exemplos complementares</strong></summary>

| Aula | Conteúdo |
| --- | --- |
| [Fundamentos](1-fundamentos/README.md) | Conceitos, cluster e primeiros comandos |
| [Pods](2-pod/README.md) | Criação, inspeção e diagnóstico |
| [Deployment](3-deployment/README.md) | Estratégias, rollout e rollback |
| [ReplicaSet, DaemonSet e StatefulSet](4-replicaSet-daemonSet-statefulSet/README.md) | Controladores e manifests |
| [Probes](5-probes/README.md) | Startup, readiness e liveness |
| Volumes | Material original ainda não localizado para vinculação |
| [Services](7-services/README.md) | Tipos de exposição e descoberta |

[Resumo de conceitos](resume.md) · [Configuração do Kind](kind-config.yaml)

</details>

## 🗺️ Como usar este repositório

**Leia → aplique → observe → experimente → investigue → limpe.**

- **Conceito:** entenda o comportamento esperado e os objetos envolvidos.
- **Prática:** execute um lab quando disponível; não apenas copie o YAML.
- **Observação:** compare estado desejado, eventos e recursos criados.
- **Aprofundamento:** use as fontes oficiais vinculadas em cada módulo.

[**Ver o roadmap completo →**](docs/roadmap.md) · [**Entender a convenção visual →**](docs/infograficos.md)

## 🔗 Fontes oficiais

[Documentação Kubernetes](https://kubernetes.io/docs/home/) · [Kubernetes Concepts](https://kubernetes.io/docs/concepts/) · [Kubernetes Tutorials](https://kubernetes.io/docs/tutorials/) · [Kind](https://kind.sigs.k8s.io/)

---

<div align="center">

**Construído para aprender Kubernetes na prática — e entender o porquê de cada comando.**

[↑ Voltar ao início](README.md)

</div>
