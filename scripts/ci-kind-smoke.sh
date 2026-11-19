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
  # Reversão dos experimentos fora do contrato, também em falhas da CI.
  kubectl label namespace lab-02-03 pod-security.kubernetes.io/warn- pod-security.kubernetes.io/enforce- >/dev/null 2>&1 || true
  kubectl delete -f trilhas/02-operacao-seguranca/labs/topology-spread-basico/experiments/spread-impossivel.yaml --ignore-not-found >/dev/null 2>&1 || true
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

# PSA: contraste real entre warn e enforce sem criar Pod privilegiado.
psa_manifest="trilhas/02-operacao-seguranca/labs/securitycontext-psa-basico/experiments/psa-incompativel.yaml"
kubectl label namespace lab-02-03 pod-security.kubernetes.io/warn=restricted --overwrite
kubectl apply --dry-run=server -f "$psa_manifest" > "$report_dir/psa-warn.txt" 2>&1
grep -Eiq 'warning|would violate podsecurity' "$report_dir/psa-warn.txt"
kubectl label namespace lab-02-03 pod-security.kubernetes.io/enforce=restricted --overwrite
if kubectl apply --dry-run=server -f "$psa_manifest" > "$report_dir/psa-enforce.txt" 2>&1; then
  echo "FAIL: PSA enforce aceitou manifesto privilegiado" >&2
  exit 1
fi
grep -Eiq 'violates podsecurity|forbidden' "$report_dir/psa-enforce.txt"
test -z "$(kubectl get pod psa-incompativel -n lab-02-03 --ignore-not-found -o name)"
kubectl label namespace lab-02-03 pod-security.kubernetes.io/warn- pod-security.kubernetes.io/enforce-

# Topology Spread: 3 réplicas, minDomains 3 e apenas 2 workers elegíveis.
spread_manifest="trilhas/02-operacao-seguranca/labs/topology-spread-basico/experiments/spread-impossivel.yaml"
kubectl apply -f "$spread_manifest"
spread_ok=false
for attempt in $(seq 1 40); do
  # Evita depender de field selectors e torna qualquer falha na consulta explícita.
  if ! kubectl get deployment spread-impossivel -n lab-02-08 -o json > "$report_dir/spread-deployment.json" 2>"$report_dir/spread-query-error.txt"; then
    echo "Falha consultando o Deployment (tentativa $attempt); confira spread-query-error.txt" >&2
    sleep 3
    continue
  fi
  if ! kubectl get pods -n lab-02-08 -l app=spread-impossivel -o json > "$report_dir/spread-pods.json" 2>"$report_dir/spread-query-error.txt"; then
    echo "Falha consultando Pods (tentativa $attempt); confira spread-query-error.txt" >&2
    sleep 3
    continue
  fi
  snapshot="$(python3 - "$report_dir/spread-deployment.json" "$report_dir/spread-pods.json" <<'PY'
import json
import sys
deployment = json.load(open(sys.argv[1], encoding="utf-8"))
pods = json.load(open(sys.argv[2], encoding="utf-8")).get("items", [])
ready = deployment.get("status", {}).get("readyReplicas", 0)
pending = sum(p.get("status", {}).get("phase") == "Pending" for p in pods)
print(f"{ready} {pending} {len(pods)}")
PY
)"
  read -r ready pending total <<< "$snapshot"
  echo "Topology Spread: tentativa=$attempt ready=$ready pending=$pending pods=$total"
  if [[ "$ready" == "2" && "$pending" -ge 1 && "$total" -eq 3 ]]; then
    spread_ok=true
    break
  fi
  sleep 3
done
kubectl get pods -n lab-02-08 -l app=spread-impossivel -o wide > "$report_dir/spread-pods.txt"
kubectl describe pods -n lab-02-08 -l app=spread-impossivel > "$report_dir/spread-describe.txt"
if [[ "$spread_ok" != true ]]; then
  echo "FAIL: Topology Spread não comprovou 2 Ready + 1 Pending; veja spread-pods.txt e spread-describe.txt" >&2
  exit 1
fi
if ! grep -q 'FailedScheduling' "$report_dir/spread-describe.txt"; then
  echo "FAIL: não há evento FailedScheduling documentado no experimento de Topology Spread" >&2
  exit 1
fi
kubectl delete -f "$spread_manifest"

# Testes intencionais de reconciliação e de negação de admissão.
# Confere que Service possui endpoints prontos, não apenas que existe na API.
kubectl get endpointslices -n lab-01-05 -l kubernetes.io/service-name=web \
  -o jsonpath='{.items[0].endpoints[0].conditions.ready}' | grep -qx true
make lab-experiment LAB=01.12 EXPERIMENT=controlled-rollout
make lab-experiment LAB=02.04 EXPERIMENT=reject-pod

echo "Smoke test de 22 laboratórios e experimentos de PSA/Topology Spread concluído."
