#!/usr/bin/env bash
set -euo pipefail

[[ "$(kubectl config current-context)" == "kind-dev" ]] || { echo "Esperado kind-dev" >&2; exit 1; }
report_dir="${REPORT_DIR:-/tmp/kvg-lab-reports}"
mkdir -p "$report_dir"
cleanup_layer03() {
  code=$?
  if [[ $code -ne 0 ]]; then
    kubectl get pods -A -o wide > "$report_dir/layer03-pods.txt" 2>&1 || true
    kubectl get events -A --sort-by=.lastTimestamp > "$report_dir/layer03-events.txt" 2>&1 || true
  fi
  for n in $(seq 17 -1 1); do
    printf -v lab "03.%02d" "$n"
    make lab-down LAB="$lab" || true
  done
  exit "$code"
}
trap cleanup_layer03 EXIT

for n in $(seq 1 17); do
  printf -v lab "03.%02d" "$n"
  echo "== Camada 03: $lab =="
  if [[ "$lab" == "03.06" ]]; then
    make lab-prepare LAB="$lab"
    kubectl wait --for=condition=Established crd/appenvironments.learning.example --timeout=120s
  fi
  make lab-up LAB="$lab"
  make lab-test LAB="$lab"
  make lab-observe LAB="$lab" > "$report_dir/observe-${lab}.txt" 2>&1
done

kubectl rollout status deployment/percurso -n lab-03-01 --timeout=180s
kubectl get cm api-demo -n lab-03-02 -o jsonpath='{.data.revisao}' | grep -qx v1
kubectl get cm registro -n lab-03-03 -o jsonpath='{.data.revisao}' | grep -qx primeira
kubectl get quota limites -n lab-03-04 -o yaml > "$report_dir/layer03-quota.yaml"
kubectl rollout status deployment/controlador -n lab-03-05 --timeout=180s
kubectl get appenvironments.learning.example demonstra -n lab-03-06
kubectl rollout status deployment/operator-demo -n lab-03-07 --timeout=180s

# O Pod do scheduler é propositalmente Pending; não esperar Ready.
kubectl get pod sem-no -n lab-03-08 -o jsonpath='{.status.phase}' | grep -qx Pending
test -z "$(kubectl get pod sem-no -n lab-03-08 -o jsonpath='{.spec.nodeName}')"

# Kind sem cloud-controller: LoadBalancer não cria infraestrutura externa.
kubectl rollout status deployment/web -n lab-03-09 --timeout=180s
test -z "$(kubectl get svc exposicao -n lab-03-09 -o jsonpath='{.status.loadBalancer.ingress[*].ip}')"
kubectl wait --for=condition=Ready pod/agente-demo -n lab-03-10 --timeout=180s
kubectl wait --for=condition=Ready pod/runtime-demo -n lab-03-11 --timeout=180s
kubectl rollout status deployment/web -n lab-03-12 --timeout=180s
kubectl wait --for=condition=Ready pod/cliente -n lab-03-12 --timeout=180s
web_ip="$(kubectl get pod -n lab-03-12 -l app=web -o jsonpath='{.items[0].status.podIP}')"
kubectl exec -n lab-03-12 cliente -- wget -qO- "http://$web_ip" > "$report_dir/layer03-pod-ip-http.txt"

kubectl rollout status deployment/web -n lab-03-13 --timeout=180s
kubectl get endpointslices -n lab-03-13 -l kubernetes.io/service-name=web -o yaml > "$report_dir/layer03-endpoints.yaml"
kubectl rollout status deployment/web -n lab-03-14 --timeout=180s
kubectl exec -n lab-03-14 cliente -- nslookup web.lab-03-14.svc.cluster.local > "$report_dir/layer03-dns.txt"
kubectl exec -n lab-03-14 cliente -- wget -qO- http://web > "$report_dir/layer03-dns-http.txt"
kubectl get pvc dados -n lab-03-15 -o jsonpath='{.status.phase}' | grep -qx Bound
kubectl exec -n lab-03-15 escritor -- cat /dados/marcador.txt | grep -qx criado
kubectl rollout status deployment/web -n lab-03-16 --timeout=180s
kubectl get svc web -n lab-03-16
kubectl get cm config-renderizada -n lab-03-17 -o jsonpath='{.data.ambiente}' | grep -qx base
kubectl kustomize trilhas/03-arquitetura/labs/kustomize-helm-basico/examples/overlays/staging > "$report_dir/layer03-kustomize.yaml"
grep -q 'ambiente: staging' "$report_dir/layer03-kustomize.yaml"

echo "PASS: 17 labs da Camada 03 executados na suíte Kind (limites de addon documentados)."
