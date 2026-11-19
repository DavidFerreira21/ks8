# Experimento avançado 03.15 — CSI Hostpath real

[← Lab 03.15](../README.md) · [↑ Camada 03](../../../README.md)

> **Opcional e isolado:** usa o driver de exemplo **CSI Hostpath**, não destinado à produção. Crie um cluster Kind descartável e evite reutilizar o volume local do lab básico como prova de CSI.

## Pré-requisito — instalar um driver CSI

Siga as instruções do repositório oficial [kubernetes-csi/csi-driver-host-path](https://github.com/kubernetes-csi/csi-driver-host-path). Escolha release/manifests compatíveis com a versão do Kubernetes do seu Kind (a instalação dos sidecars é sensível à versão).

Antes de aplicar o exemplo:

```bash
kubectl config current-context # kind-dev em cluster descartável
kubectl get csidrivers
kubectl get pods -A | grep -i csi
kubectl get storageclass
```

**Não prossiga** até o driver de exemplo estar Ready. O provisioner do manifesto é `hostpath.csi.k8s.io`; caso o driver instalado registre outro nome, compare e corrija em sua cópia local antes de prosseguir.

## Provar PVC provisionado pelo driver CSI

```bash
kubectl apply -f trilhas/03-arquitetura/labs/csi-storage-basico/experiments/csi-hostpath-storageclass.yaml
kubectl apply -f trilhas/03-arquitetura/labs/csi-storage-basico/experiments/csi-hostpath-pvc-pod.yaml
kubectl wait pvc/dados-csi -n lab-03-15 --for=jsonpath='{.status.phase}=Bound' --timeout=180s
kubectl wait pod/escritor-csi -n lab-03-15 --for=condition=Ready --timeout=180s
kubectl get pvc dados-csi -n lab-03-15 -o wide
kubectl get pv -o wide
kubectl exec -n lab-03-15 escritor-csi -- cat /dados/marcador.txt
```

O PV gerado deve referenciar o driver CSI pelo campo `spec.csi.driver`. **Isso diferencia a prática do provisionador local não-CSI**.

## Persistência e limpeza

```bash
kubectl delete pod escritor-csi -n lab-03-15 --ignore-not-found
kubectl apply -f trilhas/03-arquitetura/labs/csi-storage-basico/experiments/csi-hostpath-pvc-pod.yaml
kubectl wait pod/escritor-csi -n lab-03-15 --for=condition=Ready --timeout=180s
kubectl exec -n lab-03-15 escritor-csi -- cat /dados/marcador.txt
```

O arquivo deve permanecer. Se o volume estiver restrito a um nó, observe constraints de agendamento; não confunda falha de montagem com perda de dados.

Para limpar:

```bash
kubectl delete -f trilhas/03-arquitetura/labs/csi-storage-basico/experiments/csi-hostpath-pvc-pod.yaml --ignore-not-found
kubectl delete -f trilhas/03-arquitetura/labs/csi-storage-basico/experiments/csi-hostpath-storageclass.yaml --ignore-not-found
```

A política `reclaimPolicy: Delete` poderá remover os dados do volume de teste ao excluir a PVC. **Não use dados importantes.** Desinstale o driver apenas depois de verificar que nenhuma outra PVC o utiliza.

[CSI Hostpath sample](https://github.com/kubernetes-csi/csi-driver-host-path) · [CSI](https://kubernetes-csi.github.io/docs/)
