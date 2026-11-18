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
    kubectl logs -n k8s-lab deployment/web --all-containers=true > "$report_dir/web-logs.txt" 2>&1 || true
  fi
  for lab in 02.04 02.02 01.06; do
    make lab-down LAB="$lab" || true
  done
  exit "$code"
}
trap diagnostics EXIT

make validate
for lab in 01.06 02.02 02.04; do
  echo "== Aplicando $lab =="
  make lab-up LAB="$lab"
  make lab-test LAB="$lab"
  make lab-observe LAB="$lab" > "$report_dir/observe-${lab}.txt" 2>&1
done

# Testes intencionais de reconciliação e de negação de admissão.
make lab-experiment LAB=01.06 EXPERIMENT=controlled-rollout
make lab-experiment LAB=02.04 EXPERIMENT=reject-pod

echo "Smoke test de 3 laboratórios concluído com sucesso."
