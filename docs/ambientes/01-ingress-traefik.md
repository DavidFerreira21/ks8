# Preparação do Lab 01.13 — Traefik no Kind

[↑ Ambientes](README.md) · [🧪 Lab 01.13](../../trilhas/01-fundamentos/labs/ingress-basico/README.md)

> **Somente Kind descartável.** O Ingress é um objeto declarativo; a prova funcional depende de um Ingress Controller saudável. Não reutilize instalação de produção nem exponha portas públicas para este estudo.

## 1. Selecionar versão e instalar

```bash
[[ "$(kubectl config current-context)" == "kind-dev" ]]
helm repo add traefik https://traefik.github.io/charts
helm repo update
helm search repo traefik/traefik --versions | head -n 12
# Substitua por uma versão estável do chart compatível com seu Kubernetes:
export TRAEFIK_CHART_VERSION=VERSAO_ESCOLHIDA
helm upgrade --install traefik traefik/traefik \
  --namespace traefik --create-namespace \
  --version "$TRAEFIK_CHART_VERSION" \
  --set providers.kubernetesIngress.enabled=true \
  --set service.type=ClusterIP
kubectl rollout status deployment/traefik -n traefik --timeout=180s
kubectl get ingressclass
```

**Revisão de versão:** anote a versão real selecionada e o `helm status traefik -n traefik`. Não use literalmente `VERSAO_ESCOLHIDA`. Confirme a IngressClass chamada `traefik`; se não existir, consulte valores e eventos do chart em vez de declarar sucesso.

## 2. Provar tráfego por Host

```bash
make lab-prepare LAB=01.13
# Complete seu Ingress em .labs/01.13/
make lab-apply LAB=01.13
kubectl get ingress,svc,endpointslices -n lab-01-13
```

Em outro terminal: `kubectl -n traefik port-forward svc/traefik 8080:80`. Em terminal separado: `curl -i -H 'Host: aula.local' http://127.0.0.1:8080/`. Registre status e corpo HTTP. Repita sem header Host para observar diferença. Se houver 404/503, compare IngressClass, selector, backend Service, EndpointSlices e logs do Traefik.

## 3. Limpar com segurança

```bash
make lab-down LAB=01.13
helm uninstall traefik -n traefik
```

**Só desinstale se o release tiver sido criado exclusivamente para este Kind de estudo**. Não exclua CRDs/IngressClass globais pertencentes a outros controllers. Faça inventário de Ingresses e dependências antes.

[Documentação oficial Traefik](https://doc.traefik.io/traefik/setup/kubernetes/) · [Ingress Kubernetes](https://kubernetes.io/docs/concepts/services-networking/ingress/)
