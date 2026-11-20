# 01.04 · ReplicaSet, DaemonSet e StatefulSet

[⌂ Início](../../../README.md) · [↑ Camada 01](../README.md) · [📚 Catálogo](../../../docs/catalogo.md)

> **Ao concluir esta aula, você será capaz de:** Distinguir as garantias de ReplicaSet, DaemonSet e StatefulSet e selecionar cada um conforme identidade e distribuição dos Pods.

## 🎨 Infográfico

![01.04 — ReplicaSet, DaemonSet e StatefulSet](../replicaset-daemonset-statefulset/images/replicaset-daemonset-statefulset.png)

## 📖 Aula teórica

## Por que existem controladores diferentes?

Todos reconciliam Pods, mas **a intenção de cada workload é diferente**. Escolher o controlador adequado evita tratar aplicações com estado, agentes por nó e réplicas intercambiáveis como se fossem o mesmo problema.

| Recurso | O que garante | Uso típico |
| --- | --- | --- |
| **ReplicaSet** | Número especificado de Pods que correspondem ao seletor | Quase sempre gerenciado por Deployment |
| **DaemonSet** | Um Pod em cada nó elegível, sujeito a regras de agendamento | Agentes de logging, monitoramento ou rede |
| **StatefulSet** | Identidade estável, ordinal e comportamento ordenado | Serviços stateful e clusters distribuídos |

## ReplicaSet

Um ReplicaSet observa o conjunto de Pods selecionados e cria ou remove instâncias para atender `replicas`. Em aplicações comuns, trabalhe com **Deployment**, que gerencia revisões e ReplicaSets de forma mais conveniente.

## DaemonSet

Um DaemonSet acompanha os nós elegíveis; quando um novo nó compatível aparece, o controller procura executar nele o Pod do agente. Isso não significa obrigatoriamente um Pod em *todos* os nós: taints, selectors, affinity e regras podem limitar o conjunto.

## StatefulSet

Um StatefulSet utiliza nomes estáveis como `db-0`, `db-1` e `db-2` e pode criar PVCs exclusivos com `volumeClaimTemplates`. Ele não transforma automaticamente um banco em altamente disponível nem garante replicação de dados: isso continua sendo responsabilidade da aplicação e de sua arquitetura.

É comum associá-lo a um **Headless Service**, para descoberta DNS por identidade estável. A exclusão do StatefulSet não implica necessariamente a remoção dos PVCs.

## Comparação no cluster

```bash
kubectl get deployments,replicasets,statefulsets,daemonsets -A
kubectl get pods -A -o wide
kubectl get pvc -A
```

Verifique quantos Pods cada controlador deseja, onde executam e quais são suas dependências. **Pergunta:** por que um DaemonSet de agente e um Deployment de aplicação precisam de estratégias de escala diferentes?

## 🧪 Aplicação prática

**🧪 Lab 01.04:** [🧪 Lab 01.04](../labs/controladores-basico/README.md). Execute as etapas no seu Kind, observe os eventos e registre sua hipótese antes do experimento.

**Complementar opcional:** [Consultar material complementar](complementares/README.md). Referência adicional para consulta após a aula e o lab.

## ✅ Revisão do aprendizado

- Por que um DaemonSet pode não executar em todos os nós do cluster?
- O que torna a identidade de um Pod de StatefulSet diferente da identidade de um Pod de Deployment?
- Por que StatefulSet não equivale automaticamente a banco de dados replicado ou backup?

## 🔗 Referências oficiais

[Documentação Kubernetes — ReplicaSet, DaemonSet e StatefulSet](https://kubernetes.io/docs/concepts/workloads/controllers/)

---

[← Aula 01.03 — Deployments](../deployments/README.md) · [↑ Camada 01](../README.md) · [🧪 Lab 01.04](../labs/controladores-basico/README.md) · [Próxima: Aula 01.05 — Services →](../services/README.md)
