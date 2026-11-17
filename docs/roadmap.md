# 🗺️ Roadmap · Kubernetes Visual Guide

[⌂ Início](../README.md) · [🧪 Labs](labs.md) · [☸️ Kind](../install-kind.md)

> **Sua jornada:** fundamentos → operação → arquitetura → Platform Engineering. Os 44 conceitos compõem o catálogo visual; **laboratórios e PNGs são adicionados progressivamente**.

## Visão geral da jornada

| **01 · Fundamentos** | **02 · Operação e Segurança** |
| :--- | :--- |
| 📦 **13 temas**<br>Crie e exponha aplicações. Aprenda os objetos mais usados.<br><br>[**Entrar na Camada 01 →**](../trilhas/01-fundamentos/README.md) | 🛡️ **9 temas**<br>Controle quem acessa, onde executa e quanto consome.<br><br>[**Entrar na Camada 02 →**](../trilhas/02-operacao-seguranca/README.md) |


| **03 · Arquitetura e Infraestrutura** | **04 · Platform Engineering e GitOps** |
| :--- | :--- |
| 🧩 **14 temas**<br>Investigue Control Plane, Workers, rede e storage.<br><br>[**Entrar na Camada 03 →**](../trilhas/03-arquitetura/README.md) | 🔀 **8 temas**<br>Trabalhe com reconciliação, extensibilidade e políticas.<br><br>[**Entrar na Camada 04 →**](../trilhas/04-platform-engineering/README.md) |

## Método de estudo

```text
COMPREENDER  →  PREPARAR  →  EXECUTAR  →  OBSERVAR
                                       ↓
REFERÊNCIAS  ←  LIMPEZA  ←  DIAGNÓSTICO / EXPERIMENTO
```

| Etapa | O que fazer |
| :---: | --- |
| **01** 📖 | Leia a explicação do conceito e consulte o infográfico quando publicado |
| **02** ⚙️ | Verifique os pré-requisitos e confirme o contexto do cluster |
| **03** 🧪 | Aplique os manifests e execute os comandos descritos |
| **04** 🔎 | Inspecione estado, eventos, logs, endpoints e controller, conforme o caso |
| **05** 🔁 | Altere propositalmente uma configuração e observe a reconciliação |
| **06** 🧹 | Remova somente os recursos criados pelo exercício |
| **07** 🔗 | Consulte a documentação oficial do componente |

## Marcos recomendados

**Após a Camada 01:** você consegue criar, atualizar, inspecionar e expor uma aplicação usando recursos nativos.

**Após a Camada 02:** você entende políticas de acesso, limites, scheduling e disponibilidade.

**Após a Camada 03:** você explica os componentes internos do Kubernetes e como eles colaboram.

**Após a Camada 04:** você compreende extensibilidade e GitOps como fundamentos de uma plataforma.

Esses marcos são **objetivos de aprendizado**, não certificações de execução ou testes concluídos.

## Infraestrutura do laboratório

| Recurso | Acesso |
| --- | --- |
| 🚀 Instalar o ambiente Kind / WSL | [Guia de instalação](../install-kind.md) |
| ⚙️ Revisar a topologia (1 Control Plane + 2 Workers) | [kind-config.yaml](../kind-config.yaml) |
| 🧪 Executar e validar labs | [Guia dos laboratórios](labs.md) |
| 📚 Consultar conceitos históricos | [Resumo do projeto](../resume.md) |
| 🎨 Preparar infográficos | [Convenção visual](infograficos.md) |

> **Estado do projeto:** as anotações e os exemplos práticos continuam disponíveis nas suas páginas atuais, integrados à trilha de estudo, e **não há comprovação de execução dos labs em cluster real** apenas pela presença dos arquivos.

## Padrão de uma aula completa

- [ ] Objetivo e pré-requisitos claros
- [ ] Explicação objetiva e arquitetura/fluxo
- [ ] Manifestos ou comandos reproduzíveis
- [ ] Critérios de sucesso e observabilidade
- [ ] Um experimento de alteração, falha ou reconciliação, quando aplicável
- [ ] Diagnóstico e limpeza segura
- [ ] Referências oficiais e link para a próxima etapa

## Documentação oficial

[Conceitos Kubernetes](https://kubernetes.io/docs/concepts/) · [Tutoriais Kubernetes](https://kubernetes.io/docs/tutorials/) · [Referência kubectl](https://kubernetes.io/docs/reference/kubectl/) · [Kind](https://kind.sigs.k8s.io/)

---

[⌂ Início](../README.md) · [**Começar pelos Fundamentos →**](../trilhas/01-fundamentos/README.md)
