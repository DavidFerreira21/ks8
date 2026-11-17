# 01.14 · Horizontal Pod Autoscaler (HPA)

[↑ Camada 01](../README.md) · [📚 Catálogo](../../../docs/catalogo.md)

## 🎨 Infográfico

![01.14 — Horizontal Pod Autoscaler (HPA)](images/hpa.png)

## 📖 Aula teórica

**Em preparação.** O HPA ajusta o número de réplicas de workloads compatíveis conforme métricas e limites configurados. O funcionamento com métricas de CPU e memória normalmente depende da Metrics API, como a fornecida pelo metrics-server.

[Referência oficial — HPA](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/)

## 🧪 Prática e observação

Roteiro conceitual (ainda não validado em Kind):

```bash
kubectl get hpa -A
kubectl top pods -A
kubectl describe hpa <nome> -n <namespace>
```

> Os comandos de métricas dependem de um coletor compatível instalado. Os nomes entre `<...>` são exemplos a substituir; não há manifesto executável nesta aula ainda.

## 🔎 Diagnóstico e conclusão

Observe condições, métricas disponíveis e os limites mínimo/máximo de réplicas. O laboratório de geração de carga será criado posteriormente.

---

[← Ingress](../ingress/README.md) · [↑ Camada 01](../README.md) · [📚 Catálogo](../../../docs/catalogo.md)
