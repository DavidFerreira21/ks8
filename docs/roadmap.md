# Roadmap — Kubernetes Visual Guide

[← Início](../README.md)

Esta trilha combina **conceitos**, **diagramas/infográficos**, **laboratórios** e **documentação oficial**. O objetivo é aprender a usar Kubernetes e, depois, entender seu funcionamento interno e sua aplicação em Platform Engineering.

> **Status da migração:** esta primeira etapa reorganiza a navegação. As aulas e os manifests existentes permanecem nos caminhos originais. Os infográficos produzidos ainda serão incorporados ao repositório em uma etapa posterior. Um tópico listado não significa que já existe um lab completo.

## As quatro camadas

| Camada | Foco | Guia |
| --- | --- | --- |
| 01 | Fundamentos e recursos essenciais | [Acessar](../trilhas/01-fundamentos/README.md) |
| 02 | Operação, governança e segurança | [Acessar](../trilhas/02-operacao-seguranca/README.md) |
| 03 | Arquitetura e infraestrutura | [Acessar](../trilhas/03-arquitetura/README.md) |
| 04 | Platform Engineering e GitOps | [Acessar](../trilhas/04-platform-engineering/README.md) |

## Como estudar cada tópico

1. **Entenda:** leia a explicação e consulte o infográfico, quando disponível no GitHub.
2. **Prepare:** verifique os pré-requisitos e suba o cluster de laboratório.
3. **Pratique:** aplique o YAML e execute os comandos do exercício.
4. **Observe:** inspecione o estado com `kubectl get`, `describe`, `logs` e `events`, conforme o tema.
5. **Experimente:** altere uma configuração e observe o comportamento do controlador.
6. **Limpe:** remova os recursos do exercício, sem apagar outros workloads.
7. **Aprofunde:** consulte a documentação oficial vinculada ao tópico.

## Laboratório existente

- [Instalação local com Kind e WSL](../install-kind.md)
- [Configuração do cluster Kind](../kind-config.yaml): um nó control-plane e dois workers, com portas 80/443 mapeadas.
- [Resumo de conceitos já documentados](../resume.md)
- [Aulas atuais](../README.md#aulas-e-laboratorios-existentes)

O conteúdo atual será migrado gradualmente para dentro de cada camada **sem apagar exercícios ou substituir manifests sem revisão**. Os exemplos de comandos devem ser validados no ambiente antes de serem declarados como testes automatizados.

## Critérios para considerar uma aula completa

- Conceito objetivo e arquitetura ou fluxo ilustrado
- Pré-requisitos verificáveis
- Manifests ou comandos reproduzíveis
- Resultado esperado e como inspecioná-lo
- Experimento de alteração, falha ou reconciliação, quando aplicável
- Comandos de limpeza
- Referência oficial e próxima aula

## Referências gerais

- [Kubernetes — documentação oficial](https://kubernetes.io/docs/home/)
- [Kubernetes — conceitos](https://kubernetes.io/docs/concepts/)
- [Kubernetes — tutoriais](https://kubernetes.io/docs/tutorials/)
- [kind — Quick Start](https://kind.sigs.k8s.io/docs/user/quick-start/)
