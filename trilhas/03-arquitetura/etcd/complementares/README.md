# Complementar 03.03 — Persistência, consistência e recuperação

[← Aula 03.03](../README.md) · [🧪 Lab 03.03](../../labs/etcd-basico/README.md) · [↑ Camada 03](../../README.md)

> **Leitura opcional:** referência de arquitetura, comparação e diagnóstico; não substitui o percurso prático da aula e do lab.

## Quando consultar

Ao investigar inconsistências aparentes entre recursos declarados, cache de clientes e o estado recuperado após reinicialização.

| Sinal | Significado | Cuidado |
| --- | --- | --- |
| `metadata.resourceVersion` | Versão usada em observação e controle de concorrência | Não é relógio nem contador global |
| `metadata.uid` | Identidade de objeto | Recriar objeto com mesmo nome gera novo UID |
| `metadata.generation` | Alterações relevantes na especificação | Nem todo update incrementa geração |
| `status.observedGeneration` | Última geração reconciliada por controlador | Pode estar atrasada |

## Recuperação de etcd

Snapshots devem ter controle de acesso, compatibilidade de versões e plano de restore. Restaurar um estado antigo pode causar perda de alterações recentes e afetar objetos críticos. **Este lab não pede snapshot real nem leitura direta das chaves do cluster**.

```bash
kubectl get cm registro -n lab-03-03 -o yaml
kubectl get cm registro -n lab-03-03 -o jsonpath='{.metadata.resourceVersion}'
```

## Referências oficiais

[Operating etcd](https://kubernetes.io/docs/tasks/administer-cluster/configure-upgrade-etcd/)

---

[↑ Aula 03.03](../README.md) · [↑ Camada 03](../../README.md)
