# Lab 01.05 — Services

[← Aula 01.05](../../services/README.md) · [↑ Camada 01](../../README.md) · [🧪 Índice dos labs](../../../../docs/labs.md)

> **MODO DESAFIO:** execute `make lab-prepare LAB=01.05` para preparar o namespace e os Pods de apoio e criar o arquivo `.labs/01.05/service.yaml`. Complete o YAML com base no objetivo desta aula. Execute `kubectl apply -f .labs/01.05/` e depois `make lab-test LAB=01.05`. **`make lab-up` é exclusivo da CI** e aplica a solução, portanto não é o fluxo do aluno. `make lab-solution LAB=01.05` mostra onde consultar a referência.


## Objetivo e hipótese

Entender por que um **Service** fornece um endereço estável para Pods efêmeros e como seus **selectors** se relacionam com os **EndpointSlices**. O Deployment no manifesto existe **somente como backend de apoio**: o objetivo deste lab **não é** estudar criação de Pods, ReplicaSets nem RollingUpdate (assuntos dos labs 01.02, 01.03 e 01.12).

**Ambiente:** Kind local `dev`, contexto `kind-dev`, namespace exclusivo `lab-01-05`. Não requer Ingress Controller.

**Hipótese:** o Service continuará existindo mesmo que seu selector não encontre nenhum Pod. Mas continuará encaminhando tráfego?

## Desafio — o que você vai construir

O `make lab-prepare` cria o **Deployment de apoio**. Você escreve **somente o Service** `web`, do tipo `ClusterIP`, namespace `lab-01-05`, selecionando `app: services-demo`, expondo a porta 80 e encaminhando à porta 80 do container. Compare selector, labels e EndpointSlices.

**Antes de aplicar:** tente explicar o comportamento esperado sem consultar `solution/`. Se precisar, use `kubectl explain` ou a documentação abaixo. A solução de referência só deve ser consultada depois da tentativa.

## Fase 1 — Inspecionar a intenção

```bash
kubectl config current-context
kubectl get nodes
make lab-prepare LAB=01.05
cat .labs/01.05/service.yaml
```

Identifique `metadata.name`, `spec.type: ClusterIP`, `spec.selector`, `port` e `targetPort`. Compare o selector do Service com a label dos Pods do Deployment de apoio.

## Fase 2 — Criar e observar

```bash
# Você já preparou o ambiente na Fase 1; complete agora o YAML local.
kubectl apply -f .labs/01.05/
make lab-test LAB=01.05
make lab-observe LAB=01.05
kubectl get service web -n lab-01-05 -o wide
kubectl get pods -n lab-01-05 -l app=services-demo -o wide
kubectl get endpointslices -n lab-01-05 -l kubernetes.io/service-name=web -o yaml
```

**Observe:** o Service recebe um `CLUSTER-IP`, e os EndpointSlices representam Pods elegíveis. Compare seus endereços com os IPs dos Pods prontos. Um Service do tipo ClusterIP não expõe automaticamente a aplicação para a internet.

## Fase 3 — Testar acesso ao Service

No terminal A:

```bash
kubectl port-forward -n lab-01-05 service/web 8080:80
```

No terminal B:

```bash
curl -I http://127.0.0.1:8080
```

**Resultado esperado:** resposta HTTP do nginx. Encerre o `port-forward` com Ctrl+C antes de prosseguir.

**Nota:** o `port-forward service/web` escolhe um Pod por trás do Service para estabelecer o túnel; ele **não comprova** o balanceamento nem a travessia do ClusterIP. Para exercitar o DNS/ClusterIP de dentro do cluster, utilize o teste adicional:

```bash
kubectl run cliente-service -n lab-01-05 --image=busybox:1.36 --restart=Never --command -- sh -c 'wget -qO- http://web.lab-01-05.svc.cluster.local'
kubectl wait --for=jsonpath='{.status.phase}'=Succeeded pod/cliente-service -n lab-01-05 --timeout=90s
kubectl logs pod/cliente-service -n lab-01-05
kubectl delete pod cliente-service -n lab-01-05 --ignore-not-found
```

## Fase 4 — Experimento: quebrar o selector

Antes de alterar, mantenha um terminal observando os EndpointSlices:

```bash
kubectl get endpointslices -n lab-01-05 -l kubernetes.io/service-name=web -w
```

Em outro terminal, faça uma alteração controlada, **somente no Service**:

```bash
kubectl patch service web -n lab-01-05 --type merge -p '{"spec":{"selector":{"app":"nao-existe"}}}'
kubectl describe service web -n lab-01-05
kubectl get endpointslices -n lab-01-05 -l kubernetes.io/service-name=web -o yaml
```

**Resultado esperado:** o Service continua com o mesmo ClusterIP, porém sem endpoints de Pods correspondentes. O Service isoladamente não cria Pods nem corrige o selector.

Restaure o selector e confirme o retorno dos backends:

```bash
kubectl patch service web -n lab-01-05 --type merge -p '{"spec":{"selector":{"app":"services-demo"}}}'
kubectl get endpointslices -n lab-01-05 -l kubernetes.io/service-name=web -o yaml
make lab-test LAB=01.05
```

Finalize o watch com Ctrl+C. Explique a diferença entre Service existente, endpoint disponível e tráfego realmente funcionando.

## Resultado esperado e evidências

- O Deployment de apoio fica disponível; seu Service recebe um ClusterIP e EndpointSlices com endereços dos Pods `Ready`.
- O `port-forward` permite HTTP local, enquanto o Pod temporário testa DNS e ClusterIP **de dentro do cluster**.
- Com o selector `app: nao-existe`, o Service **continua existindo**, mas os endpoints disponíveis desaparecem. Após restaurar `app: services-demo`, eles reaparecem.

**Se o resultado divergir:** consulte `kubectl describe`, `kubectl get events` e os logs quando existirem Pods. Diferencie erro de YAML, problema no cluster e comportamento intencional do experimento.

## Fase 5 — Diagnóstico

```bash
kubectl describe service web -n lab-01-05
kubectl get pods -n lab-01-05 --show-labels
kubectl get events -n lab-01-05 --sort-by=.lastTimestamp
```

Quando um Service não responde, compare **selector → labels → readiness → EndpointSlices → DNS → porta de destino**, nessa ordem. Um selector inválido pode resultar em Service saudável do ponto de vista da API, mas sem backends.

## Fase 6 — Limpeza

Se executou os experimentos, confirme que removeu o Pod temporário `cliente-service`. Depois:

```bash
kubectl delete pod cliente-service -n lab-01-05 --ignore-not-found
make lab-down LAB=01.05
make lab-status LAB=01.05
```

O namespace é preservado; `lab-down` remove os recursos declarados no contrato. Não use `make down` para limpar este exercício.

## Critérios de conclusão

- [ ] Criei somente o Service; o backend veio do `lab-prepare`.
- [ ] Distingui ClusterIP, porta do Service e `targetPort`.
- [ ] Conferi Pod labels, selector e EndpointSlices antes e depois do erro.
- [ ] Testei DNS interno, restaurei o selector e limpei o Pod cliente.

## Aprofunde seus conhecimentos

[Services](https://kubernetes.io/docs/concepts/services-networking/service/) · [EndpointSlices](https://kubernetes.io/docs/concepts/services-networking/endpoint-slices/) · [DNS de Services e Pods](https://kubernetes.io/docs/concepts/services-networking/dns-pod-service/).

Use essas referências para entender **por que** o Kubernetes se comportou assim; depois compare com a [aula teórica](../../services/README.md).

---

[← Lab 01.04](../controladores-basico/README.md) · [↑ Aula 01.05](../../services/README.md) · [Próximo: Lab 01.06 →](../namespaces-basico/README.md)
