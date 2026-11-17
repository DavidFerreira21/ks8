# Probes

[← Camada 01](../README.md) · [Roadmap](../../../docs/roadmap.md) · [Início](../../../README.md)

> **Migração progressiva:** este é o ponto de entrada da aula. A explicação e os exercícios originais seguem preservados em [5-probes/README.md](../../../5-probes/README.md). Não movemos nem alteramos os manifests existentes neste PR.

## Objetivo

Distinguir verificações de inicialização, prontidão e saúde dos containers.

## Ao concluir, você deverá conseguir

- Distinguir liveness, readiness e startup
- Inspecionar eventos e condições do Pod
- Observar o efeito da readiness sobre os destinos de um Service

## Estude o conceito

Leia a [aula original](../../../5-probes/README.md), que contém os exemplos, explicações e comandos já presentes na trilha.

**Infográfico:** espaço reservado; o PNG será incluído em um PR posterior, após revisão editorial/técnica.

## Laboratório e observação

**Pré-requisito:** [Kind configurado](../../../install-kind.md) e contexto correto selecionado. Confira `kubectl config current-context` antes de executar comandos que alterem o cluster.

Use os manifests e exemplos da [aula original](../../../5-probes/README.md). Para observar o cluster:

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
