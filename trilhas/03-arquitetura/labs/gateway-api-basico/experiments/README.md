# Experimento avançado 03.16 — HTTPRoute real via Envoy Gateway

[← Lab 03.16](../README.md) · [↑ Camada 03](../../../README.md)

> **Opcional e funcional:** Gateway API depende de CRDs e controlador. O exemplo usa **Envoy Gateway** em Kind descartável e um serviço nginx do lab principal.

## Preparação e versões

Consulte [instalação oficial do Envoy Gateway com Helm](https://gateway.envoyproxy.io/latest/install/install-helm/) e escolha uma versão estável compatível. A instalação de chart normalmente inclui as CRDs necessárias.

```bash
kubectl config current-context # kind-dev, cluster descartável
export ENVOY_GATEWAY_VERSION=VERSAO_ESTAVEL_ESCOLHIDA
: "${ENVOY_GATEWAY_VERSION:?Escolha uma versão estável revisada}"
helm install eg oci://docker.io/envoyproxy/gateway-helm \
  --version "$ENVOY_GATEWAY_VERSION" \
  --namespace envoy-gateway-system --create-namespace
kubectl get pods -n envoy-gateway-system
kubectl api-resources --api-group=gateway.networking.k8s.io
kubectl get gatewayclass
```

**Importante:** algumas instalações gerenciam uma única GatewayClass por controller. Não crie outra se uma classe funcional gerenciada por Envoy Gateway já existir; nesse caso use a classe existente em uma cópia local do manifesto.

## Criar backend e rota

```bash
make lab-prepare LAB=03.16
kubectl apply -f .labs/03.16/
kubectl rollout status deployment/web -n lab-03-16 --timeout=180s
kubectl apply -f trilhas/03-arquitetura/labs/gateway-api-basico/experiments/gatewayclass.yaml
kubectl apply -f trilhas/03-arquitetura/labs/gateway-api-basico/experiments/gateway-route.yaml
kubectl get gatewayclass eg-lab-03-16
kubectl get gateway,httproute -n lab-03-16 -o yaml
```

Observe condições **Accepted**, **Programmed** e **ResolvedRefs**. Recurso aceito sem Programmed não prova tráfego.

## Comprovar HTTP no dataplane

Identifique o Service do Envoy Proxy criado pelo controlador com `kubectl get svc -A`. No segundo terminal faça port-forward ao Service real correspondente ao Gateway:

```bash
kubectl -n NAMESPACE_DO_PROXY port-forward svc/NOME_DO_PROXY 18080:80
```

No primeiro terminal:

```bash
curl --fail --show-error http://127.0.0.1:18080/
```

O retorno HTTP do nginx é a evidência funcional. Em Kind puro, a ausência de `EXTERNAL-IP` em LoadBalancer é normal; **port-forward** evita confundir isso com falha de Gateway API.

## Reversão

```bash
kubectl delete -f trilhas/03-arquitetura/labs/gateway-api-basico/experiments/gateway-route.yaml --ignore-not-found
kubectl delete -f trilhas/03-arquitetura/labs/gateway-api-basico/experiments/gatewayclass.yaml --ignore-not-found
make lab-down LAB=03.16
```

Exclua a GatewayClass apenas se foi criada **exclusivamente** para este teste e nenhuma outra Gateway a utiliza. Só então avalie `helm uninstall eg -n envoy-gateway-system` no Kind descartável.

[Gateway API](https://gateway-api.sigs.k8s.io/) · [Envoy Gateway HTTP Routing](https://gateway.envoyproxy.io/docs/tasks/traffic/http-routing/)
