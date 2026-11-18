# Lab 01.14 — HPA: escalabilidade orientada por CPU

[← Camada 01](../../README.md) · [Guia de labs](../../../../docs/labs.md)

## Objetivo e hipótese

O HPA compara métricas observadas com a meta de utilização e ajusta replicas do Deployment; sem Metrics Server a escala por CPU não funciona.

**Ambiente:** Kind `dev`, namespace `lab-01-14`. **Atenção:** este lab exige componentes adicionais no cluster local para a parte funcional; o teste declarativo sozinho não prova tráfego ou escala.

## Fase 1 — Pré-requisitos

Para o HPA de CPU funcionar, o API Server precisa disponibilizar `metrics.k8s.io` via Metrics Server. Confira:

```bash
kubectl get apiservice v1beta1.metrics.k8s.io
kubectl top nodes
```

Se não existir Metrics Server, instale-o conforme [instruções oficiais](https://github.com/kubernetes-sigs/metrics-server). No Kind, certificados self-signed dos kubelets podem exigir `--kubelet-insecure-tls` **somente neste ambiente local**. Confirme que `kubectl top nodes` funciona antes de esperar escala; nunca copie a flag insegura para produção.

## Fase 2 — Aplicar

```bash
kubectl config current-context
make lab-up LAB=01.14
make lab-test LAB=01.14
make lab-observe LAB=01.14
```

**Observe o controlador HPA:**

```bash
kubectl get hpa -n lab-01-14 -w
kubectl describe hpa php-apache -n lab-01-14
```

**Experimento — gerar carga:** em outro terminal:

```bash
kubectl run carga-hpa -n lab-01-14 --image=busybox:1.36 --restart=Never -- /bin/sh -c 'while true; do wget -q -O- http://php-apache >/dev/null; done'
```

Observe novamente `kubectl get hpa -n lab-01-14`, `kubectl get deployment -n lab-01-14` e `kubectl top pods -n lab-01-14`. A escala pode levar minutos e depende de métricas, request CPU e carga efetiva. Remova o gerador de carga antes da limpeza:

```bash
kubectl delete pod carga-hpa -n lab-01-14 --ignore-not-found
```

Aguarde as réplicas reduzirem. Um HPA criado sem métricas pode existir no cluster sem conseguir escalar — não confunda existência do recurso com sucesso do experimento.

## Fase 3 — Diagnosticar

```bash
kubectl get events -n lab-01-14 --sort-by=.lastTimestamp
kubectl describe deployment -n lab-01-14
```

A ausência de controller/telemetria não é falha do YAML em si. Compare recurso declarado, status e dependências externas.

## Fase 4 — Limpar o exercício

```bash
make lab-down LAB=01.14
make lab-status LAB=01.14
```

O namespace é preservado. Componentes compartilhados instalados nas etapas de pré-requisito **não são removidos** por `lab-down`; revise-os manualmente caso queira desinstalá-los, pois outros labs podem estar utilizando-os.

## Checklist

- [ ] Instalei ou verifiquei a dependência adicional.
- [ ] Apliquei os recursos e observei o controlador.
- [ ] Provei o comportamento com tráfego ou carga.
- [ ] Limpei recursos temporários e diagnostiquei o resultado.
