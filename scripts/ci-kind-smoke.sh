#!/usr/bin/env bash
set -euo pipefail

# A CI sempre trabalha com o cluster Kind descartável "dev".
context="$(kubectl config current-context)"
[[ "$context" == "kind-dev" ]] || { echo "Contexto inesperado: $context" >&2; exit 1; }

report_dir="${REPORT_DIR:-/tmp/kvg-lab-reports}"
mkdir -p "$report_dir"

diagnostics() {
  local code="$?"
  if [[ "$code" != "0" ]]; then
    echo "Falha no smoke test; coletando diagnóstico..." >&2
    kubectl get pods -A -o wide > "$report_dir/pods.txt" 2>&1 || true
    kubectl get events -A --sort-by=.lastTimestamp > "$report_dir/events.txt" 2>&1 || true
    kubectl describe pods -A > "$report_dir/describe-pods.txt" 2>&1 || true
    kubectl logs -n lab-01-05 deployment/web --all-containers=true > "$report_dir/web-logs.txt" 2>&1 || true
  fi
  for lab in 02.04 02.02 01.12 01.11 01.10 01.09 01.08 01.07 01.06 01.05 01.04 01.03 01.02 01.01; do
    make lab-down LAB="$lab" || true
  done
  exit "$code"
}
trap diagnostics EXIT

make validate
# Aguarda CNI e workers estarem prontos; o passo de criacao do Kind pode terminar antes.
kubectl wait --for=condition=Ready nodes --all --timeout=180s
# Ingress e HPA (01.13 e 01.14) exigem addons e sao validados estaticamente.
for lab in 01.01 01.02 01.03 01.04 01.05 01.06 01.07 01.08 01.09 01.10 01.11 01.12 02.02 02.04; do
  echo "== Aplicando $lab =="
  make lab-up LAB="$lab"
  make lab-test LAB="$lab"
  make lab-observe LAB="$lab" > "$report_dir/observe-${lab}.txt" 2>&1
done

# Testes intencionais de reconciliação e de negação de admissão.
# Confere que Service possui endpoints prontos, não apenas que existe na API.
kubectl get endpointslices -n lab-01-05 -l kubernetes.io/service-name=web \
  -o jsonpath='{.items[0].endpoints[0].conditions.ready}' | grep -qx true
make lab-experiment LAB=01.12 EXPERIMENT=controlled-rollout
make lab-experiment LAB=02.04 EXPERIMENT=reject-pod

echo "Smoke test de 14 laboratórios concluído com sucesso."
