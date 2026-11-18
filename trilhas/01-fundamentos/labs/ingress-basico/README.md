# Lab 01.13 — Ingress

[← Aula 01.13](../../ingress/README.md) · [↑ Camada 01](../../README.md) · [🧪 Índice dos labs](../../../../docs/labs.md)

> **MODO DESAFIO:** primeiro configure os addons do roteiro. Depois, `make lab-prepare LAB=01.13` prepara somente o Deployment e Service de apoio e cria `.labs/01.13/web.yaml`. **Escreva o Ingress**, execute `kubectl apply -f .labs/01.13/` e valide com `make lab-test LAB=01.13`. `make lab-up` é reservado à CI, não ao aluno.


## Objetivo e hipótese

Ingress vincula rotas HTTP a Services; um controller precisa reconciliar o objeto para existir roteamento real.

**Ambiente:** Kind `dev`, namespace `lab-01-13`. **Atenção:** este lab exige componentes adicionais no cluster local para a parte funcional; o teste declarativo sozinho não prova tráfego ou escala.

## Desafio — o que você vai construir

Após instalar e confirmar Traefik/IngressClass no Kind, o `lab-prepare` cria **Deployment e Service de apoio**. Você escreve **somente o Ingress** `web`, usando `ingressClassName: traefik`, host `aula.local`, caminho `/`, `pathType: Prefix` e backend Service `web` na porta 80.

**Antes de aplicar:** confirme os pré-requisitos, complete o YAML em `.labs/01.13/` e faça uma hipótese sobre o resultado. Recorra a `kubectl explain` ou às referências abaixo; não copie a solução antes de tentar.

## Fase 1 — Pré-requisitos

Ingress é um recurso de roteamento; **sem controller, não existe dataplane HTTP**. Para um cluster Kind de estudo, instale o Helm e o Traefik no namespace dedicado (execute uma vez, fora do namespace de lab):

```bash
helm repo add traefik https://traefik.github.io/charts
helm repo update
helm upgrade --install traefik traefik/traefik -n traefik --create-namespace --set providers.kubernetesIngress.enabled=true
kubectl rollout status deployment/traefik -n traefik --timeout=180s
kubectl get ingressclass
```

Confirme que existe uma IngressClass `traefik`. Charts e políticas de cluster podem mudar; ajuste a instalação ao ambiente caso seja necessário. Não exponha portas 80/443 no host para executar este lab; use port-forward.

## Fase 2 — Aplicar

```bash
kubectl config current-context
make lab-prepare LAB=01.13
# Complete o arquivo local com a especificacao
kubectl apply -f .labs/01.13/
make lab-test LAB=01.13
make lab-observe LAB=01.13
```

**Observe os objetos:**

```bash
kubectl get ingress,service,pods -n lab-01-13
kubectl describe ingress web -n lab-01-13
kubectl get endpointslices -n lab-01-13 -l kubernetes.io/service-name=web
```

**Experimento — tráfego por host:** em outro terminal rode:

```bash
kubectl port-forward -n traefik service/traefik 8080:80
```

E em um terminal separado:

```bash
curl -i -H 'Host: aula.local' http://127.0.0.1:8080/
```

Espere HTTP 200 e resposta do nginx. Teste sem o cabeçalho `Host` e compare o roteamento. Encerre o port-forward com Ctrl+C. Se a resposta for 404, investigue IngressClass, provider, regras, Service e endpoints; não assuma que um Ingress existente já está atendendo tráfego.

## Resultado esperado e evidências

- `kubectl get ingress` mostra a regra criada; isso, sozinho, **não comprova funcionamento**.
- Com o controller correto e o port-forward ativo, `curl -H 'Host: aula.local' http://127.0.0.1:8080/` retorna normalmente **HTTP 200** do backend nginx.
- Sem o header `Host` correspondente, a regra não casa e o controller pode retornar 404. Se o tráfego falhar, confira IngressClass, controller, Service e EndpointSlices antes de alterar o Ingress.

**Se o resultado divergir:** investigue `describe`, eventos e componentes de suporte. Um check que aprova o manifesto não substitui a observação funcional.

## Fase 3 — Diagnosticar

```bash
kubectl get events -n lab-01-13 --sort-by=.lastTimestamp
kubectl describe deployment -n lab-01-13
```

A ausência de controller/telemetria não é falha do YAML em si. Compare recurso declarado, status e dependências externas.

## Fase 4 — Limpar o exercício

```bash
make lab-down LAB=01.13
make lab-status LAB=01.13
```

O namespace é preservado. Componentes compartilhados instalados nas etapas de pré-requisito **não são removidos** por `lab-down`; revise-os manualmente caso queira desinstalá-los, pois outros labs podem estar utilizando-os.

## Critérios de conclusão

- [ ] Confirmei Traefik e uma IngressClass compatível.
- [ ] Escrevi o Ingress com host, path e backend corretos.
- [ ] Testei HTTP com e sem o Host e expliquei o resultado.
- [ ] Distingui o recurso Ingress do controller e limpei apenas o exercício.

## Aprofunde seus conhecimentos

[Ingress](https://kubernetes.io/docs/concepts/services-networking/ingress/) · [Ingress Controllers](https://kubernetes.io/docs/concepts/services-networking/ingress-controllers/) · [Ingress Classes](https://kubernetes.io/docs/concepts/services-networking/ingress/#ingress-class).

Volte à [aula teórica](../../ingress/README.md) e relacione os mecanismos com os eventos e estados vistos no Kind.

---

[← Lab 01.12](../estrategias-deployment-basico/README.md) · [↑ Aula 01.13](../../ingress/README.md) · [Próximo: Lab 01.14 →](../hpa-basico/README.md)
