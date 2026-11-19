# Complementar 03.15 — Storage: PV, PVC e provisionamento

[← Aula 03.15](../README.md) · [🧪 Lab 03.15](../../labs/csi-storage-basico/README.md) · [↑ Camada 03](../../README.md)

> **Leitura opcional:** referência de arquitetura, comparação e diagnóstico; não substitui o percurso prático da aula e do lab.

## Quando consultar

Ao tratar Pending de PVC, perda aparente de dados ou diferenças entre armazenamento local e cloud.

| Recurso | Responsabilidade | Evidência |
| --- | --- | --- |
| StorageClass | Política de provisionamento | Provisioner, reclaimPolicy |
| PVC | Pedido de volume por namespace | `Bound`, requested storage |
| PV | Volume do cluster vinculado | ClaimRef e volumeHandle |
| CSI driver | Integração real com storage backend | Node/controller plugin, quando instalado |

## Diagnóstico

```bash
kubectl get sc
kubectl describe pvc dados -n lab-03-15
kubectl get pv -o wide
kubectl get csidrivers
```

O Kind pode ter StorageClass funcional sem driver CSI. **Bound não prova preservação de arquivo**; o experimento exige recriar apenas o Pod e ler o mesmo marcador.

Antes de excluir PVC, consulte `persistentVolumeReclaimPolicy` e avalie dados compartilhados.

## Referências oficiais

[Volumes](https://kubernetes.io/docs/concepts/storage/volumes/) · [CSI](https://kubernetes.io/docs/concepts/storage/volumes/#csi)

---

[↑ Aula 03.15](../README.md) · [↑ Camada 03](../../README.md)
