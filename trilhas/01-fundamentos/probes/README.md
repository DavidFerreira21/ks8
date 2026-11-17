# Probes

[← Camada 01](../README.md) · [Roadmap](../../../docs/roadmap.md) · [Início](../../../README.md)

> **Material de apoio:** este guia organiza o estudo do conceito. Veja também as anotações, os comandos e os exercícios em [material complementar](../../../5-probes/README.md).

## Objetivo

Distinguir verificações de inicialização, prontidão e saúde dos containers.

## Ao concluir, você deverá conseguir

- Distinguir liveness, readiness e startup
- Inspecionar eventos e condições do Pod
- Observar o efeito da readiness sobre os destinos de um Service

## Estude o conceito

Consulte as [anotações e exemplos práticos](../../../5-probes/README.md), com explicações, exemplos e comandos para aprofundar o conceito.

**Infográfico:** espaço reservado; o PNG será incluído em um PR posterior, após revisão editorial/técnica.

## Laboratório e observação

**Pré-requisito:** [Kind configurado](../../../install-kind.md) e contexto correto selecionado. Confira `kubectl config current-context` antes de executar comandos que alterem o cluster.

Utilize os manifests e exemplos das [anotações e exemplos práticos](../../../5-probes/README.md). Para observar o cluster:

```bash
kubectl get pods
kubectl describe pod <nome-do-pod>
kubectl get endpointslices
```

> Substitua os valores entre `<...>` pelos recursos realmente criados. Os comandos acima são referências para estudo; a execução não foi testada neste PR.

Os exercícios com falhas intencionais e critérios de aceitação serão padronizados nas próximas etapas.

## Documentação oficial

- [Kubernetes — Probes](https://kubernetes.io/docs/concepts/configuration/liveness-readiness-startup-probes/)

**Próximo tópico:** [Services](../services/README.md).


---

### Navegação

[← Anterior](../controladores/README.md) · [↑ Voltar à camada](../README.md) · [Próximo →](../services/README.md)
