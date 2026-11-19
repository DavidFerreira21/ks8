# Complementar 03.17 — Kustomize versus Helm: critérios de uso

[← Aula 03.17](../README.md) · [🧪 Lab 03.17](../../labs/kustomize-helm-basico/README.md) · [↑ Camada 03](../../README.md)

> **Leitura opcional:** referência de arquitetura, comparação e diagnóstico; não substitui o percurso prático da aula e do lab.

## Quando consultar

Ao decidir como empacotar, promover e revisar configuração entre ambientes.

| Critério | Kustomize | Helm |
| --- | --- | --- |
| Abstração | Bases, overlays e patches | Charts, templates e values |
| Prévia | `kubectl kustomize` | `helm template` |
| Deploy | `kubectl apply -k` | `helm install/upgrade` |
| Estado de release | Não gerencia release Helm | Histórico de releases no cluster |

## Fluxo de revisão

1. Renderize a configuração resultante.
2. Compare manifests entre ambientes.
3. Valide schema/policies quando disponíveis.
4. Execute apply/upgrade no contexto autorizado.
5. Observe o estado em execução, especialmente selectors e readiness.

No Kind, comece pelo `examples/base` e `examples/overlays/staging`. O binário Helm não é obrigatório para o experimento principal; pode ser usado para comparar renderização de charts revisados.

## Referências oficiais

[Kustomize](https://kubernetes.io/docs/tasks/manage-kubernetes-objects/kustomization/) · [Helm](https://helm.sh/docs/)

---

[↑ Aula 03.17](../README.md) · [↑ Camada 03](../../README.md)
