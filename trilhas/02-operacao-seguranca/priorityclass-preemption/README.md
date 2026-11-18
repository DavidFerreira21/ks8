# PriorityClass e Preemption

[← Camada 02](../README.md) · [Roadmap](../../../docs/roadmap.md)

## 🎨 Infográfico

![02.09 — PriorityClass e Preemption](images/priorityclass-preemption.png)

> Imagem disponível no repositório; confira detalhes técnicos na documentação da aula.


## O que você vai aprender

PriorityClass atribui prioridade de agendamento a Pods. Sob pressão por capacidade, o Scheduler pode preemptar Pods de menor prioridade, conforme política.

## Como funciona

priorityClassName referencia classe; priority value afeta ordem e, conforme preemptionPolicy, pode permitir preempção.

## Experimento recomendado

Simule escassez de CPU em laboratório isolado e inspecione Pending e eventos; não force preempção em clusters compartilhados.

**Status do lab:** roteiro conceitual; manifests e validação prática serão adicionados em uma etapa posterior.

## O que observar

- Resultado e eventos dos recursos envolvidos.
- Diferença entre configuração desejada, decisão do Control Plane e resultado observado.
- Regras, condições e pré-requisitos particulares deste mecanismo.



## Referência oficial

- [Documentação Kubernetes — PriorityClass e Preemption](https://kubernetes.io/docs/concepts/scheduling-eviction/pod-priority-preemption/)

**Próxima etapa:** [índice completo da Camada 02](../README.md).


---

### Navegação

[← Anterior](../pdb/README.md) · [↑ Voltar à camada](../README.md) · [Próximo →](../init-sidecars/README.md)
