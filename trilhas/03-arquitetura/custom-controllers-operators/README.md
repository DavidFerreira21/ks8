# 🧩 03.07 · Custom Controllers e Operators

[⌂ Início](../../../README.md) · [↑ Camada 03](../README.md) · [🗺️ Roadmap](../../../docs/roadmap.md)

> **Objetivo:** entender o padrão de reconciliação e como controladores personalizados e Operators automatizam a operação de recursos no Kubernetes.

## 🎨 Infográfico

![03.07 — Custom Controllers e Operators](images/custom-controllers-operators.png)

> Imagem disponível no repositório; confira detalhes técnicos na documentação da aula.


## 📖 Conceito

Um **Controller** observa o estado atual de recursos e toma medidas para aproximá-lo do estado desejado. Um **Custom Controller** aplica esse princípio a uma necessidade específica — frequentemente a tipos registrados por CRDs.

O padrão **Operator** combina recursos personalizados com lógica de controle para codificar conhecimento operacional de um sistema. Nem todo controlador precisa ser um Operator; também é possível construir controladores para recursos Kubernetes existentes.

| Conceito | Responsabilidade |
| --- | --- |
| **Watch / Informer** | Detectar alterações relevantes nos recursos |
| **Reconcile loop** | Comparar estado desejado e observado e aplicar ajustes |
| **Idempotência** | Repetir uma reconciliação sem provocar efeitos indesejados |
| **Status / Conditions** | Publicar progresso, estado observado e problemas |
| **Finalizers** | Coordenar limpeza de dependências antes da exclusão |

## 🧪 Laboratório proposto — AppEnvironment

1. Partir da CRD `AppEnvironment` apresentada na aula anterior.
2. Implementar um controlador simples que observa seus objetos.
3. Fazer o controlador criar ou atualizar um **ConfigMap** derivado da `spec`.
4. Alterar a `spec` e observar a reconciliação do ConfigMap.
5. Simular drift alterando o ConfigMap manualmente e verificar seu retorno ao estado esperado.
6. Explorar a atualização de `status` e a limpeza segura dos recursos.

**Status:** roteiro de lab; não há código de controlador, manifests prontos ou execução validada neste PR.

## 🎯 Você deverá conseguir

- [ ] Explicar o loop de reconciliação e a diferença entre estado desejado e observado.
- [ ] Distinguir CRD, Custom Controller e Operator.
- [ ] Relacionar idempotência, condições de status e finalizers à operação.
- [ ] Reconhecer como projetos como Crossplane estendem o padrão declarativo.

## 🔗 Referências

[Kubernetes · Controllers](https://kubernetes.io/docs/concepts/architecture/controller/) · [Kubernetes · Operator Pattern](https://kubernetes.io/docs/concepts/extend-kubernetes/operator/) · [Kubernetes · Custom Resources](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/)

---

[← CRDs e Custom Resources](../crds-custom-resources/README.md) · [↑ Camada 03](../README.md) · [Próxima: kube-scheduler no índice →](../README.md)
