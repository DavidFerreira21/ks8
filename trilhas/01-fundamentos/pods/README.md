# Pods

[← Camada 01](../README.md) · [Roadmap](../../../docs/roadmap.md) · [Início](../../../README.md)

> **Material de apoio:** este guia organiza o estudo do conceito. Veja também as anotações, os comandos e os exercícios em [material complementar](../../../2-pod/README.md).

## 🎨 Infográfico

![01.03 — Pods](images/pods.png)

> **Revisão editorial:** o infográfico está disponível no repositório; confirme os detalhes técnicos com a documentação da aula.


## Objetivo

Compreender a menor unidade implantável do Kubernetes e seus containers.

## Ao concluir, você deverá conseguir

- Criar e consultar um Pod
- Observar logs, eventos e status
- Explorar múltiplos containers, requests/limits e emptyDir

## Estude o conceito

Consulte as [anotações e exemplos práticos](../../../2-pod/README.md), com explicações, exemplos e comandos para aprofundar o conceito.


## Laboratório e observação

**Pré-requisito:** [Kind configurado](../../../install-kind.md) e contexto correto selecionado. Confira `kubectl config current-context` antes de executar comandos que alterem o cluster.

Utilize os manifests e exemplos das [anotações e exemplos práticos](../../../2-pod/README.md). Para observar o cluster:

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
