# 03.06 · CRDs e Custom Resources

[⌂ Início](../../../README.md) · [↑ Camada 03](../README.md) · [📚 Catálogo](../../../docs/catalogo.md)

> **Ao concluir esta aula, você será capaz de:** Criar um novo tipo de API e uma instância validada por schema, distinguindo armazenamento de reconciliação.

## 🎨 Infográfico

![03.06 — CRDs e Custom Resources](images/crds-custom-resources.png)

## 📖 Aula teórica

### Contexto e responsabilidade

Uma CustomResourceDefinition registra um grupo, versão, escopo e schema de recursos personalizados. Uma Custom Resource é uma instância desse tipo. O API Server passa a aceitar e armazenar o objeto, mas não cria automaticamente recursos de infraestrutura ou aplicações.

### Como o mecanismo funciona

Em `apiextensions.k8s.io/v1`, uma CRD define `spec.group`, `names`, `scope`, versões `served/storage` e `openAPIV3Schema`. O schema pode exigir campos e restringir tipos. `spec` representa a intenção; `status` somente representa observação real quando um controlador o atualiza. A exclusão da CRD pode remover todas as instâncias vinculadas.

### Exemplo interpretado (trecho)

```yaml
apiVersion: learning.example/v1
kind: AppEnvironment
metadata:
  name: demonstra
spec:
  tier: sandbox
```

A instância é aceita apenas depois de registrar uma CRD compatível. A presença da CR não instala um reconciler nem cria outros recursos. O trecho ilustra campos essenciais; consulte o lab para escrever o manifesto completo.

### Inspeção no Kind

```bash
kubectl config current-context
kubectl get crd appenvironments.learning.example
kubectl api-resources --api-group=learning.example
kubectl get appenvironments -n lab-03-06
kubectl explain appenvironment.spec
```

**Interpretação:** Observe a descoberta de `AppEnvironment` depois de registrar a CRD. Crie um recurso válido e tente um manifesto inválido com `--dry-run=server` para obter erro de schema.

### Limites e segurança

CRDs são cluster-scoped, ainda que as instâncias possam ser namespaced. Nunca reutilize nomes reais de CRDs de uma plataforma; exclua a definição apenas no Kind descartável e registre dependências.

## 🧪 Aplicação prática

[🧪 Lab 03.06 — CRDs e Custom Resources](../labs/crds-custom-resources-basico/README.md): construa o YAML do desafio, compare estado declarado com observado e registre uma evidência do conceito. O lab é o caminho principal, independente do material opcional.

**Complementar opcional:** [Guia de decisões e diagnóstico](complementares/README.md). Útil para aprofundar, não é pré-requisito.

## ✅ Revisão do aprendizado

- Por que uma Custom Resource existente não cria infraestrutura sem um reconciler?
- Que diferença existe entre uma CRD e uma instância da Custom Resource?
- O que acontece com as instâncias ao excluir a CRD e por que isso importa?

## 🔗 Referências oficiais

- [Kubernetes — documentação do componente](https://kubernetes.io/docs/tasks/extend-kubernetes/custom-resources/custom-resource-definitions/)
- [Arquitetura e componentes](https://kubernetes.io/docs/concepts/overview/components/)

---

[← Aula 03.05](../kube-controller-manager/README.md) · [↑ Camada 03](../README.md) · [🧪 Lab 03.06](../labs/crds-custom-resources-basico/README.md) · [Próxima: Aula 03.07 →](../custom-controllers-operators/README.md)
