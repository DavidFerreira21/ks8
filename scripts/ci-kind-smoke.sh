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
  for lab in 02.11 02.10 02.08 02.07 02.06 02.05 02.04 02.03 02.02 02.01 01.12 01.11 01.10 01.09 01.08 01.07 01.06 01.05 01.04 01.03 01.02 01.01; do
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

# Cobertura incremental da Camada 02: cenários determinísticos sem mutação de nós,
# preempção nem promessas de NetworkPolicy funcional sem CNI compatível.
for lab in 02.01 02.03 02.05 02.06 02.07 02.08 02.10 02.11; do
  echo "== Camada 02: $lab =="
  make lab-up LAB="$lab"
  make lab-test LAB="$lab"
  make lab-observe LAB="$lab" > "$report_dir/observe-${lab}.txt" 2>&1
done

kubectl wait --for=condition=Ready pod/rotulado -n lab-02-01 --timeout=180s
kubectl wait --for=condition=Ready pod/seguro -n lab-02-03 --timeout=180s
kubectl wait --for=condition=Ready pod/auxiliares -n lab-02-05 --timeout=180s
kubectl wait --for=condition=complete job/tarefa -n lab-02-06 --timeout=180s
kubectl wait --for=condition=Ready pod/afinidade -n lab-02-07 --timeout=180s
test "$(kubectl get pod afinidade -n lab-02-07 -o jsonpath='{.spec.nodeName}')" = "dev-worker"
kubectl rollout status deployment/distribuida -n lab-02-08 --timeout=180s
for entry in 'sem-recursos:BestEffort' 'variavel:Burstable' 'garantido:Guaranteed'; do
  pod="${entry%%:*}"
  expected="${entry##*:}"
  test "$(kubectl get pod "$pod" -n lab-02-10 -o jsonpath='{.status.qosClass}')" = "$expected"
done
kubectl rollout status deployment/replicas -n lab-02-11 --timeout=180s
kubectl get pdb disponibilidade -n lab-02-11 -o yaml > "$report_dir/pdb-02.11.yaml"

# Testes intencionais de reconciliação e de negação de admissão.
# Confere que Service possui endpoints prontos, não apenas que existe na API.
kubectl get endpointslices -n lab-01-05 -l kubernetes.io/service-name=web \
  -o jsonpath='{.items[0].endpoints[0].conditions.ready}' | grep -qx true
make lab-experiment LAB=01.12 EXPERIMENT=controlled-rollout
make lab-experiment LAB=02.04 EXPERIMENT=reject-pod

echo "Smoke test de 22 laboratórios concluído (14 originais + 8 novos da Camada 02)."
