# Pods

[← Camada 01](../README.md) · [Roadmap](../../../docs/roadmap.md) · [Início](../../../README.md)

> **Migração progressiva:** este é o ponto de entrada da aula. A explicação e os exercícios originais seguem preservados em [2-pod/README.md](../../../2-pod/README.md). Não movemos nem alteramos os manifests existentes neste PR.

## Objetivo

Compreender a menor unidade implantável do Kubernetes e seus containers.

## Ao concluir, você deverá conseguir

- Criar e consultar um Pod
- Observar logs, eventos e status
- Explorar múltiplos containers, requests/limits e emptyDir

## Estude o conceito

Leia a [aula original](../../../2-pod/README.md), que contém os exemplos, explicações e comandos já presentes na trilha.

**Infográfico:** espaço reservado; o PNG será incluído em um PR posterior, após revisão editorial/técnica.

## Laboratório e observação

**Pré-requisito:** [Kind configurado](../../../install-kind.md) e contexto correto selecionado. Confira `kubectl config current-context` antes de executar comandos que alterem o cluster.

Use os manifests e exemplos da [aula original](../../../2-pod/README.md). Para observar o cluster:

```bash
kubectl get pods -A
kubectl describe pod <nome-do-pod>
kubectl logs <nome-do-pod>
kubectl get pod <nome-do-pod> -o yaml
```

> Substitua os valores entre `<...>` pelos recursos realmente criados. Os comandos acima são referências para estudo; a execução não foi testada neste PR.

Também há um [lab integrado Pod → Deployment → Service](../labs/primeira-aplicacao/README.md) com arquivos completos e procedimentos de validação.

## Documentação oficial

- [Kubernetes — Pods](https://kubernetes.io/docs/concepts/workloads/pods/)

**Próximo tópico:** [Deployments](../deployments/README.md).


---

### Navegação

[← Anterior](../fundamentos/README.md) · [↑ Voltar à camada](../README.md) · [Próximo →](../deployments/README.md)
