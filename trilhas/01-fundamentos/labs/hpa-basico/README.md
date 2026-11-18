# Lab 01.14 — HPA

[← Aula 01.14](../../hpa/README.md) · [↑ Camada 01](../../README.md) · [🧪 Índice dos labs](../../../../docs/labs.md)

> **MODO DESAFIO:** primeiro configure os addons do roteiro. Depois, `make lab-prepare LAB=01.14` prepara somente o Deployment e Service de apoio e cria `.labs/01.14/php-apache.yaml`. **Escreva o HPA**, execute `kubectl apply -f .labs/01.14/` e valide com `make lab-test LAB=01.14`. `make lab-up` é reservado à CI, não ao aluno.


## Objetivo e hipótese

O HPA compara métricas observadas com a meta de utilização e ajusta replicas do Deployment; sem Metrics Server a escala por CPU não funciona.

**Ambiente:** Kind `dev`, namespace `lab-01-14`. **Atenção:** este lab exige componentes adicionais no cluster local para a parte funcional; o teste declarativo sozinho não prova tráfego ou escala.

## Desafio — o que você vai construir

Com Metrics Server funcional, o `lab-prepare` cria Deployment e Service `php-apache` como apoio. Você escreve o **HorizontalPodAutoscaler** `php-apache` em `autoscaling/v2`, apontando para esse Deployment, com mínimo **1** e máximo **4** réplicas, meta de utilização média de CPU **50%**.

**Antes de aplicar:** confirme os pré-requisitos, complete o YAML em `.labs/01.14/` e faça uma hipótese sobre o resultado. Recorra a `kubectl explain` ou às referências abaixo; não copie a solução antes de tentar.

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
make lab-prepare LAB=01.14
# Complete o arquivo local com a especificacao
kubectl apply -f .labs/01.14/
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

## Resultado esperado e evidências

- `kubectl get hpa` mostra o recurso e, após coleta de métricas, a utilização de CPU deixa de aparecer como `<unknown>`.
- Sob carga suficiente, as réplicas podem subir **gradualmente**, até o limite de 4; a decisão depende de métricas, requests CPU, disponibilidade do cluster e janelas do controlador.
- Após excluir o Pod gerador de carga, as réplicas tendem a cair com atraso devido à estabilização. Um HPA existente **sem métricas funcionais não prova escalabilidade**.

**Se o resultado divergir:** investigue `describe`, eventos e componentes de suporte. Um check que aprova o manifesto não substitui a observação funcional.

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

## Critérios de conclusão

- [ ] Verifiquei Metrics Server e `kubectl top nodes` antes do teste.
- [ ] Escrevi o HPA com alvo, mínimo, máximo e CPU 50%.
- [ ] Gerei carga e observei métricas e réplicas, ou diagnostiquei por que não escalaram.
- [ ] Removi o Pod gerador de carga e limpei o HPA e o backend de apoio.

## Aprofunde seus conhecimentos

[HPA](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/) · [Algoritmo do HPA](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/#algorithm-details) · [Metrics Server](https://github.com/kubernetes-sigs/metrics-server).

Volte à [aula teórica](../../hpa/README.md) e relacione os mecanismos com os eventos e estados vistos no Kind.

---

[← Lab 01.13](../ingress-basico/README.md) · [↑ Aula 01.14](../../hpa/README.md) · [Próxima camada: Operação e Segurança →](../../../02-operacao-seguranca/README.md)
