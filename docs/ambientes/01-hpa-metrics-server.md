# Preparação do Lab 01.14 — Metrics Server no Kind

[↑ Ambientes](README.md) · [🧪 Lab 01.14](../../trilhas/01-fundamentos/labs/hpa-basico/README.md)

> **Somente Kind descartável.** HPA de CPU depende de `metrics.k8s.io`, de requests de CPU no Deployment e de carga suficiente para superar a meta.

## 1. Selecionar versão e instalar

```bash
[[ "$(kubectl config current-context)" == "kind-dev" ]]
helm repo add metrics-server https://kubernetes-sigs.github.io/metrics-server/
helm repo update
helm search repo metrics-server/metrics-server --versions | head -n 12
# Substitua por versão estável compatível com Kubernetes do seu Kind:
export METRICS_SERVER_CHART_VERSION=VERSAO_ESCOLHIDA
helm upgrade --install metrics-server metrics-server/metrics-server \
  --namespace kube-system --version "$METRICS_SERVER_CHART_VERSION" \
  --set 'args[0]=--kubelet-insecure-tls'
kubectl rollout status deployment/metrics-server -n kube-system --timeout=180s
kubectl get apiservice v1beta1.metrics.k8s.io
kubectl top nodes
```

**Segurança:** `--kubelet-insecure-tls` é uma exceção para certificados de kubelet do **Kind local**, não configuração recomendada para produção. Não confunda essa flag com `apiService.insecureSkipTLSVerify`, que protege outra conexão TLS. Registre versão de chart e a configuração de exceção usada.

## 2. Verificar métrica e escala real

```bash
make lab-prepare LAB=01.14
# Complete seu HPA em .labs/01.14/
make lab-apply LAB=01.14
kubectl describe hpa php-apache -n lab-01-14
kubectl top pods -n lab-01-14
kubectl get hpa -n lab-01-14 -w
```

Gere carga conforme o [roteiro principal](../../trilhas/01-fundamentos/labs/hpa-basico/README.md) em outro terminal; interrompa `-w` com Ctrl+C. Registre CPU atual, meta, `desiredReplicas`, `currentReplicas`, Pods Ready e a redução após remover carga. Se `kubectl top` falhar ou HPA mostrar `<unknown>`, **não declare escala funcional**: investigue APIService, logs do Metrics Server, requests de CPU e readiness do workload.

## 3. Limpar com segurança

```bash
kubectl delete pod carga-hpa -n lab-01-14 --ignore-not-found
make lab-down LAB=01.14
helm uninstall metrics-server -n kube-system
```

Desinstale somente o release instalado para o laboratório. Não execute estas etapas se o cluster oferecer um Metrics Server utilizado por outros workloads.

[Documentação oficial Metrics Server](https://kubernetes-sigs.github.io/metrics-server/) · [Horizontal Pod Autoscaling](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/)
