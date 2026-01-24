# Volumes

## Indice

- [O que sao volumes](#o-que-sao-volumes)
- [StorageClass](#storageclass)
- [PersistentVolume (PV)](#persistentvolume-pv)
- [PersistentVolumeClaim (PVC)](#persistentvolumeclaim-pvc)
- [Access modes e reclaim policy](#access-modes-e-reclaim-policy)
- [Exemplo de Pod usando PVC](#exemplo-de-pod-usando-pvc)
- [Comandos rapidos](#comandos-rapidos)

## O que sao volumes

Volumes permitem persistir dados alem do ciclo de vida dos Pods. Eles podem ser temporarios (ex: EmptyDir) ou persistentes com PV/PVC.

## StorageClass

A StorageClass define classes de armazenamento e como os PVs sao provisionados. Quando usa `no-provisioner`, os PVs precisam ser criados manualmente.

Exemplo (arquivo `storageclass.yaml`):

```yaml
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: giropops
provisioner: kubernetes.io/no-provisioner
reclaimPolicy: Retain
volumeBindingMode: WaitForFirstConsumer
```

## PersistentVolume (PV)

O PV representa um volume real no cluster, com capacidade e modo de acesso. Pode ser baseado em `hostPath`, NFS, EBS, etc.

Exemplo (arquivo `nfs.yaml`):

```yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  name: meu-pv
  labels:
    storage: local
spec:
  capacity:
    storage: 1Gi
  accessModes:
    - ReadWriteOnce
  persistentVolumeReclaimPolicy: Retain
  hostPath:
    path: "/mnt/data"
  storageClassName: giropops
```

## PersistentVolumeClaim (PVC)

O PVC e o pedido de armazenamento feito por um Pod. Ele seleciona um PV que atenda aos requisitos de capacidade, access mode e StorageClass.

Exemplo (arquivo `pvc.yaml`):

```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: meu-pvc
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 1Gi
  storageClassName: nfs
  selector:
    matchLabels:
      storage: nfs
```

Ajuste `storageClassName` e `labels` para casar com o PV/StorageClass do seu ambiente.

## Access modes e reclaim policy

- `ReadWriteOnce` (RWO): um no monta leitura/escrita.
- `ReadOnlyMany` (ROX): varios nos montam leitura.
- `ReadWriteMany` (RWX): varios nos montam leitura/escrita.
- `Retain`: PV nao e apagado ao deletar o PVC.
- `Delete`: PV e removido junto com o PVC (em provisionamento dinamico).

## Exemplo de Pod usando PVC

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx-pod
spec:
  containers:
  - name: nginx
    image: nginx:latest
    ports:
    - containerPort: 80
    volumeMounts:
    - name: meu-pvc
      mountPath: /usr/share/nginx/html
  volumes:
  - name: meu-pvc
    persistentVolumeClaim:
      claimName: meu-pvc
```

## Comandos rapidos

- Aplicar StorageClass, PV e PVC

```bash
kubectl apply -f storageclass.yaml
kubectl apply -f nfs.yaml
kubectl apply -f pvc.yaml
```

- Verificar PVs e PVCs

```bash
kubectl get pv
kubectl get pvc
```

- Descrever recursos

```bash
kubectl describe pv <nome-do-pv>
kubectl describe pvc <nome-do-pvc>
```
