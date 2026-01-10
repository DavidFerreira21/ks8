# Deployment

Guia rapido para aplicar, verificar e gerenciar o rollout de um Deployment.

## Aplicar e verificar

- Aplicar o Deployment definido em `deployment.yaml`

```bash
 kubectl apply -f deployment.yaml
```

- Verificar se o Deployment foi criado e esta saudavel

```bash
 kubectl get deployments -l app=nginx-deployment
```

```bash
 kubectl get pods -l app=nginx
```

```bash
 kubectl describe deployment nginx-deployment
```

- Listar os ReplicaSets gerados pelo Deployment

```bash
kubectl get replicasets -l app=nginx
```

## Estratégias de atualização do Deployment
O Kubernetes possui 2 estrategias de atualizacao para os Deployments:

- RollingUpdate (padrao): substitui os Pods aos poucos, mantendo parte das replicas antigas ativas para evitar indisponibilidade.
- Recreate: encerra todas as replicas antigas primeiro e depois cria as novas, causando indisponibilidade temporaria.

## Rollout (atualizacoes)

- Acompanhar o status do rollout

```bash
kubectl rollout status
```

```bash
kubectl rollout status deployment nginx-deployment
```

- Ver o historico de revisoes do Deployment

```bash
kubectl rollout history
```

```bash
kubectl rollout history deployment nginx-deployment --revision=1
```

- Voltar para a versao anterior do Deployment

```bash
kubectl rollout undo
```

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

```bash
kubectl rollout restart deployment nginx-deployment
```
