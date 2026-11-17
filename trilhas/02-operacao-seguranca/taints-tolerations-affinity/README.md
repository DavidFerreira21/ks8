# Taints, Tolerations e Node Affinity

[← Camada 02](../README.md) · [Roadmap](../../../docs/roadmap.md)

## O que você vai aprender

Taints afastam Pods sem tolerations compatíveis; tolerations permitem agendamento, mas não escolhem um nó por si; affinity expressa exigências ou preferências.

## Como funciona

Scheduler filtra e pontua nós com base em recursos, restrições e preferências.

## Experimento recomendado

Rotule um worker e compare Pod com nodeAffinity; depois observe efeito de taint NoSchedule em Pods ainda não agendados.

**Status do lab:** roteiro conceitual; manifests e validação prática serão adicionados em uma etapa posterior.

## O que observar

- Resultado e eventos dos recursos envolvidos.
- Diferença entre configuração desejada, decisão do Control Plane e resultado observado.
- Regras, condições e pré-requisitos particulares deste mecanismo.

## Infográfico

O infográfico correspondente foi criado na coleção visual, mas **a imagem PNG ainda não foi enviada ao repositório**. Após revisão técnica será incluída no diretório `images/` deste tópico.

## Referência oficial

- [Documentação Kubernetes — Taints, Tolerations e Node Affinity](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/)

**Próxima etapa:** [índice completo da Camada 02](../README.md).
