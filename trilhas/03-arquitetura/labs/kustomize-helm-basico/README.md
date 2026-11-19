# Lab 03.17 — Kustomize e Helm

[← Aula 03.17](../../kustomize-helm/README.md) · [↑ Camada 03](../../README.md) · [🧪 Índice dos labs](../../../../docs/labs.md)

> **MODO DESAFIO:** `make lab-prepare LAB=03.17` prepara namespace e starter incompleto. Complete `.labs/03.17/resources.yaml`, aplique com `kubectl apply -f .labs/03.17/`, observe e valide. `make lab-up` usa a solução e é exclusivo da CI.

## Objetivo e hipótese

Renderizar e comparar base/overlay com Kustomize e distinguir esse processo do empacotamento Helm.

**Pré-requisitos:** `kind-dev`, `kubectl`, `make`, namespace `lab-03-17`. 

## Desafio — o que você vai construir

Crie ConfigMap `config-renderizada` com `data.ambiente: base`. Depois estude o exemplo base/overlay separado que altera a configuração sem editar a base.

Preveja o resultado antes de consultar `solution/`. A documentação oficial é a referência para esclarecer recursos e campos.

## Fase 1 — Preparar e prever

```bash
kubectl config current-context
make lab-prepare LAB=03.17
cat .labs/03.17/resources.yaml
```

## Fase 2 — Aplicar e observar

Complete os TODOs e execute:

```bash
kubectl apply -f .labs/03.17/
make lab-test LAB=03.17
make lab-observe LAB=03.17
```

Execute `kubectl kustomize trilhas/03-arquitetura/labs/kustomize-helm-basico/examples/base` e compare com `.../examples/overlays/staging`. Observe os campos após renderização.

## Fase 3 — Experimento controlado

Altere somente o overlay `examples/overlays/staging/kustomization.yaml` em uma cópia local e compare a saída `kubectl kustomize`; não aplique saída imprevista automaticamente. Se Helm estiver instalado, use `helm template` apenas sobre chart que você mesmo criou/inspecionou.

## Resultado esperado e evidências

A base produz valor `base`; o overlay produz `staging`. Kustomize transforma YAML; Helm, quando disponível, renderiza templates e gerencia releases — capacidades relacionadas, não idênticas.

**Evidências específicas:** registre diferença base/overlay, o arquivo responsável pelo patch e indique qual comando renderiza manifests sem instalar release.

## Fase 4 — Diagnosticar

Investigue `kubectl describe`, eventos, status, selectors e dependências do ambiente. Identifique o primeiro sinal causal; não confunda ausência de um addon com erro do YAML principal.

## Fase 5 — Limpar com segurança

```bash
make lab-down LAB=03.17
make lab-status LAB=03.17
```

O namespace permanece preservado. Reverta recursos temporários não declarados no contrato; não execute `make down`.

## Critérios de conclusão

- [ ] Escrevi o YAML sem copiar a solução.
- [ ] **Critério exclusivo 03.17:** registre diferença base/overlay, o arquivo responsável pelo patch e indique qual comando renderiza manifests sem instalar release.
- [ ] Expliquei a diferença entre estado declarado e comportamento comprovado.
- [ ] Reverti experimentos e limpei o laboratório.

## Perguntas de diagnóstico e reflexão

- Por que overlays não precisam editar bases?
- Qual diferença entre `kubectl kustomize` e `helm template`?
- Por que manifest renderizado ainda precisa de revisão antes de aplicar?

## Aprofunde seus conhecimentos

[Documentação Kubernetes](https://kubernetes.io/docs/tasks/manage-kubernetes-objects/kustomization/) · [Aula 03.17](../../kustomize-helm/README.md)

---

[← Lab 03.16](../gateway-api-basico/README.md) · [↑ Aula 03.17](../../kustomize-helm/README.md) · [↑ Camada 03](../../README.md) · [Próxima: Camada 04 →](../../../04-platform-engineering/README.md)
