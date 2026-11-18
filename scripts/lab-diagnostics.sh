#!/usr/bin/env bash
set -euo pipefail

EXPECTED_CONTEXT="${EXPECTED_CONTEXT:-kind-dev}"
NAMESPACE="${NAMESPACE:-k8s-lab}"

actual="$(kubectl config current-context 2>/dev/null || true)"
if [[ "$actual" != "$EXPECTED_CONTEXT" ]]; then
  echo "Contexto incorreto: '${actual}'. Esperado: '${EXPECTED_CONTEXT}'." >&2
  exit 1
fi

printf '\n== Nós ==\n'
kubectl get nodes -o wide
printf '\n== Recursos do laboratório ==\n'
kubectl get pods,deployments,services -n "$NAMESPACE" --ignore-not-found
printf '\n== EndpointSlices ==\n'
kubectl get endpointslices -n "$NAMESPACE" --ignore-not-found
printf '\n== Eventos recentes ==\n'
kubectl get events -n "$NAMESPACE" --sort-by=.lastTimestamp || true
printf '\n== Diagnóstico de Deployment (se existir) ==\n'
if kubectl get deployment web -n "$NAMESPACE" >/dev/null 2>&1; then
  kubectl describe deployment web -n "$NAMESPACE"
fi
