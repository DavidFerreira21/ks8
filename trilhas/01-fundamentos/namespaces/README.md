# 01.06 · Namespaces

[⌂ Início](../../../README.md) · [↑ Camada 01](../README.md) · [📚 Catálogo](../../../docs/catalogo.md)

> **Objetivo:** compreender o conceito, interpretar seu comportamento no cluster e conectar a teoria à prática.

## 🎨 Infográfico

![01.06 — Namespaces](images/namespaces.png)

## 📖 Aula teórica

## O problema que Namespaces resolvem

Um cluster pode hospedar diferentes equipes e aplicações. **Namespace** organiza recursos com escopo lógico dentro do cluster, permitindo usar nomes iguais em namespaces distintos e aplicar RBAC, quotas e políticas por escopo.

Isso **não cria clusters separados** nem garante isolamento de rede, recursos ou segurança por si só. Recursos como `Node`, `PersistentVolume`, `Namespace` e `CustomResourceDefinition` não pertencem a namespaces.

## Como funciona o escopo

O nome completo de um Pod depende do namespace: `dev/api` e `prod/api` podem ser objetos diferentes. Com `kubectl -n dev` você altera o escopo da requisição, não o cluster de destino.

| Recurso | Escopo típico |
| --- | --- |
| Pod, Deployment, Service, ConfigMap, Secret | Namespace |
| Role, RoleBinding, ResourceQuota | Namespace |
| Node, Namespace, PersistentVolume, ClusterRole | Cluster |

Um Namespace ajuda a administrar **limites e permissões**, mas essas proteções só existem quando as políticas correspondentes são aplicadas.

## Exemplo explicado

```yaml
apiVersion: v1
kind: Namespace
metadata:
  name: aula-namespaces
  labels:
    area: treinamento
```

Este objeto declara o namespace `aula-namespaces`; a label permite classificação. Para utilizar recursos nele, informe `metadata.namespace` nos manifests ou passe `-n aula-namespaces` aos comandos.

```bash
kubectl get namespaces
kubectl api-resources --namespaced=true
kubectl get pods -A
kubectl get pods -n default
```

**Observe:** `-A` agrega namespaces; `-n` seleciona um. Descubra também quais tipos não suportam `metadata.namespace`.

## Cuidados

Não use namespace como única fronteira de isolamento entre ambientes com exigências rígidas; o mesmo cluster continua compartilhando componentes e capacidade. Não exclua namespaces de trabalho: apagar um namespace dispara a exclusão de seus recursos internos.

## 🧪 Aplicação prática

**🧪 Lab 01.06:** [abrir exercício guiado](../labs/namespaces-basico/README.md). Execute as etapas no seu Kind, observe os eventos e registre sua hipótese antes do experimento.

## ✅ Revisão do aprendizado

- Qual problema este conceito resolve?
- Que campos ou estados da API permitem verificar o comportamento real?
- Que erro ou decisão equivocada você conseguiria diagnosticar após esta aula?

## 🔗 Referência oficial

[Documentação Kubernetes — Namespaces](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/)

---

[← Aula 01.05 — Services](../services/README.md) · [↑ Camada 01](../README.md) · [🧪 Lab 01.06](../labs/namespaces-basico/README.md) · [Próxima: Aula 01.07 — ConfigMaps →](../configmaps/README.md)
