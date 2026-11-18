# 02.11 · PodDisruptionBudget (PDB)

[⌂ Início](../../../README.md) · [↑ Camada 02](../README.md) · [📚 Catálogo](../../../docs/catalogo.md)

> **Ao concluir esta aula, você será capaz de:** Interpretar orçamento de interrupções voluntárias e demonstrar o efeito de `minAvailable` e `disruptionsAllowed`.

## 🎨 Infográfico

![02.11 — PodDisruptionBudget (PDB)](images/pdb.png)

## 📖 Aula teórica

### O problema que este recurso resolve

A manutenção de nós pode interromper várias réplicas ao mesmo tempo. Um PodDisruptionBudget fornece limites para evictions voluntárias realizadas via Eviction API, preservando um nível definido de disponibilidade.

### Como funciona no Kubernetes

A política seleciona Pods e define `minAvailable` ou `maxUnavailable`. O controller calcula `currentHealthy`, `desiredHealthy` e `disruptionsAllowed`. Exclusão direta de Pods, indisponibilidade involuntária e falhas de nó não são impedidas por PDB.

### Exemplo de inspeção

Os comandos são ilustrativos. Substitua nomes e confirme o contexto do Kind antes de executar.

```bash
kubectl config current-context
kubectl get pdb -n NAMESPACE
kubectl describe pdb disponibilidade -n NAMESPACE
kubectl get pods -n NAMESPACE -o wide
```

**O que observar:** Um PDB sobre três réplicas com `minAvailable: 2` normalmente permite uma eviction quando três estão saudáveis. A condição real depende de readiness e estado do controlador.

### Cuidados e limitações

Nunca presuma que PDB protege contra qualquer interrupção. Ao testar drains, identifique pods do sistema e reversão do nó.

## 🧪 Aplicação prática

**[🧪 Lab 02.11](../labs/pdb-basico/README.md):** escreva o YAML do desafio, compare resultados e investigue as condições de execução. O lab não exige leitura complementar.

## ✅ Revisão do aprendizado

- Por que `kubectl delete pod` não respeita o orçamento como Eviction API?
- Como muda `disruptionsAllowed` quando um Pod deixa de estar pronto?
- Por que um PDB mal dimensionado pode bloquear um drain?

## 🔗 Referências oficiais

- [Documentação Kubernetes](https://kubernetes.io/docs/concepts/workloads/pods/disruptions/)

---

[← Aula 02.10](../qos-eviction/README.md) · [↑ Camada 02](../README.md) · [Próxima: Aula 02.12 →](../node-maintenance/README.md)
