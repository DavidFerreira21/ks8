# Deployment

## Indice

- [O que e um Deployment](#o-que-e-um-deployment)
- [Aplicar e verificar](#aplicar-e-verificar)
- [Estrategias de atualizacao do Deployment](#estrategias-de-atualizacao-do-deployment)
- [Rollout (atualizacoes)](#rollout-atualizacoes)
- [Remover o Deployment](#remover-o-deployment)

## O que e um Deployment:

O Deployment gerencia o ciclo de vida de Pods por meio de ReplicaSets. Ele permite criar, atualizar (rollout) e reverter versoes (rollback) de forma controlada.

## Aplicar e verificar

- Aplicar o Deployment definido em `deployment.yaml`

```bash
kubectl apply -f deployment.yaml
```

- Verificar se o Deployment foi criado e esta saudavel

```bash
kubectl get deployments -l app=nginx-deployment
```

- Listar os Pods criados pelo Deployment

```bash
kubectl get pods -l app=nginx
```

- Detalhar o Deployment (status, eventos e estrategia)

```bash
kubectl describe deployment nginx-deployment
```

- Listar os ReplicaSets gerados pelo Deployment

```bash
kubectl get replicasets -l app=nginx
```

## Estrategias de atualizacao do Deployment

O Kubernetes possui 2 estrategias de atualizacao para Deployments:

- RollingUpdate (padrao): substitui os Pods aos poucos, mantendo parte das replicas antigas ativas para evitar indisponibilidade.
- Recreate: encerra todas as replicas antigas primeiro e depois cria as novas, causando indisponibilidade temporaria.

## Rollout (atualizacoes)

- Acompanhar o status do rollout (geral)

```bash
kubectl rollout status
```

- Acompanhar o status do rollout de um Deployment especifico

```bash
kubectl rollout status deployment nginx-deployment
```

- Ver o historico de revisoes do Deployment (geral)

```bash
kubectl rollout history
```

- Ver o historico detalhado de uma revisao

```bash
kubectl rollout history deployment nginx-deployment --revision=1
```

- Voltar para a versao anterior do Deployment (geral)

```bash
kubectl rollout undo
```

- Voltar para a versao anterior de um Deployment especifico

```bash
kubectl rollout undo deployment nginx-deployment
```

- Pausar temporariamente o rollout do Deployment

```bash
kubectl rollout pause
```

- Retomar o rollout do Deployment apos a pausa

```bash
kubectl rollout resume
```

- Reiniciar o rollout do Deployment (forca nova atualizacao sem alterar a imagem)

```bash
kubectl rollout restart
```

- Reiniciar o rollout de um Deployment especifico

```bash
kubectl rollout restart deployment nginx-deployment
```

## Remover o Deployment

- Remover o Deployment pelo nome

```bash
kubectl delete deployment nginx-deployment
```

- Remover o Deployment definido em um arquivo

```bash
kubectl delete -f deployment.yaml
```
