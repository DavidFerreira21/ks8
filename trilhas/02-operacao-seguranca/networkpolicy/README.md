# 02.13 · NetworkPolicy

[⌂ Início](../../../README.md) · [↑ Camada 02](../README.md) · [📚 Catálogo](../../../docs/catalogo.md)

> **Ao concluir esta aula, você será capaz de:** Explicar isolamento de tráfego com NetworkPolicy e comprovar a dependência de um CNI que implemente enforcement.

## 🎨 Infográfico

![02.13 — NetworkPolicy](images/networkpolicy.png)

## 📖 Aula teórica

### O problema que este recurso resolve

Namespaces e Services não isolam conexões por padrão. NetworkPolicy seleciona Pods e declara quais origens/destinos e portas são permitidos por direção. Sem plugin que implemente NetworkPolicy, aceitar o YAML não significa bloquear tráfego.

### Como funciona no Kubernetes

O efeito é aditivo: várias policies selecionando o mesmo Pod somam o tráfego permitido. A seleção por `podSelector` é por namespace; `namespaceSelector` permite cruzar namespaces. Políticas de ingress/egress são independentes conforme `policyTypes`.

### Exemplo interpretado (trecho)

Uma NetworkPolicy com ingress vazio isola tráfego de entrada de Pods selecionados somente quando o CNI implementa a política.

```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: deny-ingress
spec:
  podSelector: {}
  policyTypes: [Ingress]
  ingress: []
```

Este é um **trecho ilustrativo**, não um manifesto para aplicar isoladamente. A implementação completa será escrita pelo aluno no laboratório.

### Exemplo de inspeção

Os comandos são ilustrativos. Substitua nomes e confirme o contexto do Kind antes de executar.

```bash
kubectl config current-context
kubectl get networkpolicy -n NAMESPACE
kubectl describe networkpolicy isolada -n NAMESPACE
kubectl get pods -n NAMESPACE --show-labels
```

**O que observar:** Confira o objeto na API e os selectors. O teste funcional exige CNI compatível, como Cilium ou Calico configurado corretamente; não presuma isolamento no Kind padrão.

### Cuidados e limitações

Um default-deny de egress pode bloquear DNS. Mudanças de rede podem interromper workloads; teste apenas em namespace isolado.

## 🧪 Aplicação prática

**[🧪 Lab 02.13](../labs/networkpolicy-basico/README.md):** escreva o YAML do desafio, compare resultados e investigue as condições de execução. O lab não exige leitura complementar.

**Complementar opcional:** [Consultar aprofundamento 02.13](complementares/README.md). Referência adicional; não é necessária para executar o lab.

## ✅ Revisão do aprendizado

- Por que NetworkPolicy criada não prova enforcement?
- Como políticas múltiplas combinam permissões?
- Por que uma regra de egress precisa considerar DNS?

## 🔗 Referências oficiais

- [Documentação oficial do conceito](https://kubernetes.io/docs/concepts/services-networking/network-policies/)

---

[← Aula 02.12 — Node Maintenance](../node-maintenance/README.md) · [↑ Camada 02](../README.md) · [🧪 Lab 02.13](../labs/networkpolicy-basico/README.md) · [Próxima: Aula 02.14 — Kubernetes Troubleshooting →](../troubleshooting/README.md)
