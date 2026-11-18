# Complementar 02.13 — NetworkPolicy: isolamento e DNS

[← Aula 02.13](../README.md) · [🧪 Lab 02.13](../../labs/networkpolicy-basico/README.md) · [↑ Camada 02](../../README.md)

> **Leitura opcional.** Referência para consulta após a aula e o lab; não é pré-requisito e não repete o desafio YAML.

## Quando consultar

Ao planejar default-deny e investigar por que a comunicação entre Pods parou após uma policy.

As políticas de **egress da origem** e **ingress do destino** são avaliadas separadamente quando os Pods estão isolados nessas direções. Regras permissivas são aditivas; não existe regra explícita de deny com precedência sobre allow.

### Exemplo alternativo: default-deny egress

```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: deny-egress
spec:
  podSelector: {}
  policyTypes: [Egress]
  egress: []
```

Aplique apenas em namespace de estudo. Bloquear egress pode impedir resolução DNS até que regras adicionais permitam o tráfego correto.

```bash
kubectl get networkpolicy -n NAMESPACE -o yaml
kubectl get pods -n NAMESPACE --show-labels
```

**A existência da policy não prova enforcement:** confira CNI compatível e conectividade antes/depois.

## Referências oficiais

[NetworkPolicies](https://kubernetes.io/docs/concepts/services-networking/network-policies/)

---

[↑ Aula 02.13](../README.md) · [↑ Camada 02](../../README.md)
