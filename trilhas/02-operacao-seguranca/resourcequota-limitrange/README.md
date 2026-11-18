# 02.04 · ResourceQuota e LimitRange

[⌂ Início](../../../README.md) · [↑ Camada 02](../README.md) · [📚 Catálogo](../../../docs/catalogo.md)

> **Ao concluir esta aula, você será capaz de:** Interpretar defaults por container e comprovar que uma ResourceQuota restringe o consumo agregado do namespace.

## 🎨 Infográfico

![02.04 — ResourceQuota e LimitRange](images/resourcequota-limitrange.png)

## 📖 Aula teórica

### O problema que este recurso resolve

LimitRange define restrições e valores padrão para requests e limits de containers ou Pods. ResourceQuota limita agregados do namespace, como Pods, requests CPU/memória ou objetos. São políticas diferentes, aplicadas na admissão.

### Como funciona no Kubernetes

O admission controller pode completar requests/limits ausentes a partir do LimitRange. O ResourceQuota compara a demanda resultante com o limite do namespace. Uma falha por quota é rejeição na API, não um Pod `Pending`.

### Exemplo de inspeção

Os comandos abaixo são exemplos para um cluster de estudo. Substitua os nomes ilustrativos e confirme o contexto antes de executar.

```bash
kubectl config current-context
kubectl get limitrange,resourcequota -n lab-ops-quota
kubectl describe resourcequota pod-count -n lab-ops-quota
kubectl get pod demo-1 -n lab-ops-quota -o yaml
```

**O que observar:** Compare `spec.containers[].resources` admitidos com o manifesto enviado. Quando a quota de Pods é atingida, o próximo manifesto deve falhar com mensagem de quota excedida.

### Cuidados e limitações

Quota de requests pode causar rejeição mesmo quando há CPU livre nos nós. Não confunda quotas com limits por container.

## 🧪 Aplicação prática

**[🧪 Lab 02.04](../labs/quota-namespace/README.md):** escreva o YAML do exercício, execute no Kind, registre evidências e explique as divergências. O complementar não é pré-requisito.

## ✅ Revisão do aprendizado

- Qual recurso fornece defaults para containers que não especificam requests?
- Por que uma criação rejeitada por quota não aparece como Pod Pending?
- Como distinguir `hard` e `used` ao interpretar uma ResourceQuota?

## 🔗 Referências oficiais

- [Documentação Kubernetes](https://kubernetes.io/docs/concepts/policy/resource-quotas/)
- [Documentação Kubernetes](https://kubernetes.io/docs/concepts/policy/limit-range/)

---

[↑ Camada 02](../README.md) · [🧪 Lab 02.04](../labs/quota-namespace/README.md) · [← Aula 02.03](../securitycontext-pod-security/README.md) · [Próxima: 02.05 →](../init-sidecars/README.md)
