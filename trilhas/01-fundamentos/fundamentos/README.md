# 01.01 · Fundamentos Kubernetes

[⌂ Início](../../../README.md) · [↑ Camada 01](../README.md) · [📚 Catálogo](../../../docs/catalogo.md)

> **Ao concluir esta aula, você será capaz de:** Explicar a diferença entre estado desejado e observado e identificar o papel de API Server, etcd, scheduler, controllers e kubelet.

## 🎨 Infográfico

![01.01 — Fundamentos Kubernetes](../fundamentos-kubernetes/images/fundamentos-kubernetes.png)

## 📖 Aula teórica

## Por que Kubernetes existe?

Um container empacota a aplicação e suas dependências, mas, sozinho, não resolve descoberta de serviços, distribuição de carga, recuperação de falhas ou atualizações de múltiplas réplicas. O **Kubernetes** é um orquestrador: você declara o estado desejado de uma aplicação e seus controladores trabalham continuamente para aproximar a execução desse estado.

**Container image** é o artefato imutável de distribuição; **container runtime** executa os containers no nó; **Pod** é a unidade de execução gerenciada pelo Kubernetes. O Kubernetes utiliza runtimes compatíveis com a **Container Runtime Interface (CRI)**, como containerd e CRI-O. Docker pode ser usado para construir imagens e para executar os nós do Kind, mas não precisa atuar como runtime CRI do cluster.

## Componentes e responsabilidades

| Componente | Responsabilidade |
| --- | --- |
| **API Server** | Recebe e valida requisições; é a interface central do cluster |
| **etcd** | Persiste os dados de configuração e estado do cluster |
| **Scheduler** | Escolhe o nó para um Pod ainda sem agendamento |
| **Controllers** | Comparam estado desejado e observado e reconciliam divergências |
| **kubelet** | Garante que os containers dos Pods atribuídos ao nó sejam executados |
| **Rede e DNS** | Permitem conectividade e descoberta entre workloads |

O **Control Plane** coordena a plataforma; os **Worker Nodes** executam os workloads. Em serviços gerenciados como EKS, parte da operação do Control Plane é responsabilidade do provedor, mas os conceitos permanecem.

## O que acontece quando você aplica um YAML?

1. O cliente `kubectl` envia uma requisição à API.
2. A API autentica, autoriza e valida o objeto antes de persistir o estado desejado.
3. Controladores observam a mudança e criam ou ajustam recursos dependentes.
4. O scheduler decide onde executar Pods pendentes.
5. O kubelet instrui o runtime e reporta o estado observado.

Esse ciclo não é uma pipeline única; é um conjunto de **loops de reconciliação assíncronos**. Por isso, `kubectl apply` aceitar o objeto não significa que a aplicação já esteja saudável.

## Objetos, spec e status

Em recursos declarativos, `metadata` identifica o objeto, `spec` descreve a intenção e `status`, quando presente, expressa observações do controlador. Nem todos os objetos têm os mesmos campos.

```bash
kubectl config current-context
kubectl cluster-info
kubectl get nodes -o wide
kubectl get pods -A
kubectl api-resources
```

**Leitura esperada:** identifique quantos nós existem, qual é o contexto selecionado e quais recursos o API Server conhece. Os comandos acima são de inspeção.

## Modelo mental

**Você declara; o Kubernetes reconcilia; você observa.** Quando houver diferença entre `spec` e `status`, investigue eventos, condições, controladores e dependências.

## 🧪 Aplicação prática

**Atividade prática:** [🧪 Lab 01.01](../labs/fundamentos-cluster/README.md). Exercício guiado com ConfigMap, comparação entre manifesto e objeto no cluster e limpeza segura.

**Complementar opcional:** [Consultar material complementar](../../../1-fundamentos/README.md). Referência adicional para consulta após a aula e o lab.

## ✅ Revisão do aprendizado

- O que acontece entre um `kubectl apply` aceito e um Pod efetivamente pronto?
- Qual componente escolhe o nó de execução de um Pod e qual mantém os containers em funcionamento?
- Como distinguir `spec` e `status` ao investigar uma divergência no cluster?

## 🔗 Referências oficiais

[Documentação Kubernetes — Fundamentos Kubernetes](https://kubernetes.io/docs/concepts/overview/)

---

[↑ Camada 01](../README.md) · [🧪 Lab 01.01](../labs/fundamentos-cluster/README.md) · [Próxima: Aula 01.02 — Pods →](../pods/README.md)
