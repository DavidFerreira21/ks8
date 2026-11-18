# Complementar 01.05 — Tipos de Service e descoberta de backends

[← Aula 01.05](../trilhas/01-fundamentos/services/README.md) · [🧪 Lab 01.05](../trilhas/01-fundamentos/labs/services-basico/README.md) · [↑ Camada 01](../trilhas/01-fundamentos/README.md)

> **Leitura opcional:** catálogo de tipos de Service e ferramentas de diagnóstico. A aula e o lab usam ClusterIP, selectors e descoberta; aqui comparamos alternativas que não precisam ser implantadas no exercício.

## Escolhendo o tipo de Service

| Tipo | O que oferece | Uso comum | Limite |
| --- | --- | --- | --- |
| `ClusterIP` | IP virtual e DNS para acesso dentro do cluster | Comunicação entre aplicações | Não expõe automaticamente acesso externo |
| `NodePort` | Porta nos nós, normalmente no intervalo configurado | Testes e integração de rede | Exposição depende da rede do host/nó |
| `LoadBalancer` | Integração com balanceador externo quando suportado | Exposição por cloud/LB controller | Kind puro não cria um LB externo automaticamente |
| `ExternalName` | Alias DNS do Service para nome DNS externo | Referenciar destino externo | Não cria proxy, ClusterIP nem EndpointSlices de backends |
| Headless (`clusterIP: None`) | DNS apontando para endpoints em vez de ClusterIP | Descoberta direta, StatefulSets | Comportamento depende dos endpoints e do cliente |

`Headless` é uma característica da configuração de Service, não um quinto valor de `spec.type`.

## Exemplos adicionais de configuração

**NodePort** — exemplo para entender o campo, não obrigatório no lab:

```yaml
apiVersion: v1
kind: Service
metadata:
  name: app-nodeport
spec:
  type: NodePort
  selector:
    app: minha-app
  ports:
    - port: 80
      targetPort: 8080
      nodePort: 30080
```

**ExternalName** — não encaminha pacotes nem seleciona Pods:

```yaml
apiVersion: v1
kind: Service
metadata:
  name: db-externo
spec:
  type: ExternalName
  externalName: db.exemplo.com
```

**Headless** — permite descoberta direta de endpoints:

```yaml
apiVersion: v1
kind: Service
metadata:
  name: app-headless
spec:
  clusterIP: None
  selector:
    app: minha-app
  ports:
    - port: 80
      targetPort: 8080
```

Os exemplos usam nomes ilustrativos. Não há Deployment ou Pods implícitos; sem backends compatíveis, o Service não terá endpoints prontos.

## Diagnóstico por camadas

```bash
kubectl get svc -n NAMESPACE
kubectl describe svc NOME -n NAMESPACE
kubectl get endpointslices -n NAMESPACE -l kubernetes.io/service-name=NOME
kubectl get pods -n NAMESPACE --show-labels
```

- **Service sem endpoints:** compare `spec.selector`, labels dos Pods e readiness.
- **DNS não resolve:** confirme namespace, nome e DNS do cluster.
- **DNS resolve, mas conexão falha:** confira `targetPort`, aplicação, políticas de rede e endpoints disponíveis.
- **LoadBalancer sem endereço externo:** confira suporte do provedor/controlador; não assuma provisionamento automático no Kind.

O recurso legado `Endpoints` pode ser consultado em clusters antigos, mas prefira `EndpointSlice` para investigação atual.

## Referências oficiais

- [Service](https://kubernetes.io/docs/concepts/services-networking/service/)
- [Service types](https://kubernetes.io/docs/concepts/services-networking/service/#publishing-services-service-types)
- [EndpointSlices](https://kubernetes.io/docs/concepts/services-networking/endpoint-slices/)
