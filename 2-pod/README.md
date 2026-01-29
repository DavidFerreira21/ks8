# Pods

Este guia resume o que e um Pod, como criar/remover, consultar, acessar logs, entrar no container e usar recursos como limites e volumes.

## Indice

- [O que e um Pod](#o-que-e-um-pod)
- [Consultar Pods](#consultar-pods)
- [Criar e remover Pods](#criar-e-remover-pods)
- [Logs](#logs)
- [Acesso ao container](#acesso-ao-container)
- [Limites de CPU e memoria](#limites-de-cpu-e-memoria)
- [Volume EmptyDir no Pod](#volume-emptydir-no-pod)

## O que e um Pod

Pod e a menor unidade de execucao do Kubernetes. Ele agrupa um ou mais containers que compartilham rede, volumes e configuracoes. Containers no mesmo Pod conseguem falar entre si via `localhost`.

## Consultar Pods

- Listar Pods de um namespace especifico:

```bash
kubectl get pods -n <namespace>
```

- Ver detalhes do Pod em YAML:

```bash
kubectl get pod <nome-do-pod> -o yaml
```

- Inspecionar eventos e status do Pod:

```bash
kubectl describe pod <nome-do-pod>
```

## Criar e remover Pods

### Criar um Pod simples

Arquivo: `pod.yaml`

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: giropops
  labels:
    run: giropops
spec:
  containers:
  - name: giropops
    image: nginx
    ports:
    - containerPort: 80
```

Aplicar o manifesto:

```bash
kubectl apply -f pod.yaml
```

### Criar Pod com multiplos containers

Arquivo: `pod-mult-container.yaml`

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: giropops
  labels:
    run: giropops
spec:
  containers:
  - name: girus
    image: nginx
    ports:
    - containerPort: 80
  - name: strigus
    image: alpine
    args:
    - sleep
    - "1800"
```

```bash
kubectl apply -f pod-mult-container.yaml
```

### Remover Pods

- Remover um Pod pelo nome:

```bash
kubectl delete pod <nome-do-pod>
```

- Remover o Pod definido em um arquivo:

```bash
kubectl delete -f pod.yaml
```

## Logs

- Ver logs de um Pod:

```bash
kubectl logs <nome-do-pod>
```

- Acompanhar logs em tempo real:

```bash
kubectl logs -f <nome-do-pod>
```

- Ver logs de um container especifico dentro do Pod:

```bash
kubectl logs <nome-do-pod> -c <container-name>
```

## Acesso ao container

O comando `attach` conecta ao processo principal do container em execucao:

```bash
kubectl attach <pod-name> -c <container-name>
```

O comando `exec` executa comandos dentro do container:

```bash
kubectl exec <pod-name> -c <container-name> -- <comando>
```

- Abrir shell interativo no container:

```bash
kubectl exec -it ubuntu -- bash
```

## Limites de CPU e memoria

Requests definem o minimo garantido de CPU/memoria para o container. Limits definem o maximo que ele pode consumir.

Arquivo: `pod-limits.yaml`

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: giropops
  labels:
    run: giropops
spec:
  containers:
  - name: girus
    image: nginx
    ports:
    - containerPort: 80
    resources:
      limits:
        memory: "128Mi"
        cpu: "0.5"
      requests:
        memory: "64Mi"
        cpu: "0.3"
```

Aplicar o manifesto:

```bash
kubectl apply -f pod-limits.yaml
```

Validar Pods criados:

```bash
kubectl get pods
```

Opcional: testar consumo com `stress` dentro do container:

```bash
apt update
apt install -y stress
```

```bash
stress --vm 1 --vm-bytes 100M
```

## Volume EmptyDir no Pod

EmptyDir e um volume temporario criado quando o Pod inicia e removido quando o Pod e destruido. Ele e util para compartilhamento de dados entre containers no mesmo Pod.

Arquivo: `pod-emptydir.yaml`

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: giropops
spec:
  containers:
  - name: girus
    image: ubuntu
    args:
    - sleep
    - infinity
    volumeMounts:
    - name: primeiro-emptydir
      mountPath: /giropops
  volumes:
  - name: primeiro-emptydir
    emptyDir:
      sizeLimit: 256Mi
```

Criar Pod com volume EmptyDir:

```bash
kubectl apply -f pod-emptydir.yaml
```
