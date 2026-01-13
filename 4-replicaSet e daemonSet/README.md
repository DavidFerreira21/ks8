# ReplicaSet,Daemonsets e Probs

## Indice

- [O que e um ReplicaSet](#o-que-e-um-replicaset)
- [Comandos (ReplicaSet)](#comandos-replicaset)
- [O que e um DaemonSet](#o-que-e-um-daemonset)
- [Casos de uso comuns](#casos-de-uso-comuns)
- [Comandos (DaemonSet)](#comandos-daemonset)

## O que e um ReplicaSet:

O ReplicaSet garante que uma quantidade desejada de replicas de um Pod esteja sempre em execucao. Em geral ele e criado e gerenciado por um Deployment.

## Comandos (ReplicaSet)

- Aplicar o Deployment (gera o ReplicaSet definido no manifesto)

```bash
kubectl apply -f deployment.yaml
```

- Listar ReplicaSets

```bash
kubectl get rs
```

- Detalhar um ReplicaSet (status, eventos e pods associados)

```bash
kubectl describe rs
```

- Remover um ReplicaSet pelo nome

```bash
kubectl delete replicaset nginx-replicaset
```

- Remover o ReplicaSet definido em um arquivo

```bash
kubectl delete -f nginx-replicaset.yaml
```

# DaemonSet

O que e um DaemonSet:

O DaemonSet garante que todos os nos do cluster executem uma replica de um Pod. Isso e util para agentes que precisam rodar em cada no.

## Casos de uso comuns

- Agentes de monitoramento (ex: Prometheus Node Exporter, Fluentd).
- Proxy de rede em todos os nos (ex: kube-proxy, Weave Net, Calico, Flannel).
- Agentes de seguranca em cada no (ex: Falco, Sysdig).

## Comandos (DaemonSet)

- Aplicar o manifesto do DaemonSet

```bash
kubectl apply -f node-exporter-daemonset.yaml
```

- Listar DaemonSets

```bash
kubectl get daemonset
```

- Listar os Pods do DaemonSet pelo label

```bash
kubectl get pods -l app=node-exporter
```

- Listar os nos do cluster (para conferir onde o DaemonSet vai rodar)

```bash
kubectl get nodes
```

- Escalar um nodegroup no EKS (exemplo para aumentar a quantidade de nos)

```bash
eksctl scale nodegroup --cluster=eks-cluster --nodes 3 --name eks-cluster-nodegroup
```

- Remover o DaemonSet pelo nome

```bash
kubectl delete daemonset node-exporter
```

- Remover o DaemonSet definido em um arquivo

```bash
kubectl delete -f node-exporter-daemonset.yaml
```
