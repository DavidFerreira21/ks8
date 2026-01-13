# Pods

## Indice

- [O que e um Pod](#o-que-e-um-pod)
- [Consultar Pods](#consultar-pods)
- [Criar e remover Pods](#criar-e-remover-pods)
- [Logs](#logs)
- [Acesso ao container](#acesso-ao-container)
- [Limites de CPU e memoria](#limites-de-cpu-e-memoria)
- [Volume EmptyDir no Pod](#volume-emptydir-no-pod)

## O que e um Pod:

O Pod e a menor unidade do Kubernetes. Ele pode conter um ou mais containers que compartilham rede e volumes.

## Consultar Pods

- Listar Pods de um namespace especifico

```bash
kubectl get pods -n <namespace>
```

- Ver detalhes do Pod em YAML

```bash
kubectl get pods <nome-do-pod> -o yaml
```

- Inspecionar eventos e status do Pod

```bash
kubectl describe pod <nome-do-pod>
```

## Criar e remover Pods

- Criar um Pod a partir de manifesto

```bash
kubectl apply -f pod.yaml
```

- Criar Pod com multiplos containers

```bash
kubectl apply -f pod-mult-container.yaml
```

- Remover um Pod pelo nome

```bash
kubectl delete pod <nome-do-pod>
```

- Remover o Pod definido em um arquivo

```bash
kubectl delete -f pod.yaml
```

## Logs

- Ver logs de um Pod

```bash
kubectl logs <nome-do-pod>
```

- Acompanhar logs em tempo real

```bash
kubectl logs -f <nome-do-pod>
```

- Ver logs de um container especifico dentro do Pod

```bash
kubectl logs <nome-do-pod> -c <container-name>
```

## Acesso ao container

O comando `attach` conecta ao processo principal do container em execucao.

```bash
kubectl attach <pod-name> -c <container-name>
```

O comando `exec` executa comandos dentro do container.

```bash
kubectl exec <pod-name> -c <container-name> -- <comando>
```

- Abrir shell interativo no container

```bash
kubectl exec -it ubuntu -- bash
```

## Limites de CPU e memoria

- Aplicar manifesto com limites de recursos

```bash
kubectl apply -f pod-limits.yaml
```

- Validar Pods criados

```bash
kubectl get pods
```

- Instalar e executar `stress` para testar consumo

```bash
apt update
apt install -y stress
```

```bash
stress --vm 1 --vm-bytes 100M
```

## Volume EmptyDir no Pod

- Criar Pod com volume EmptyDir

```bash
kubectl apply -f pod-emptydir.yaml
```
