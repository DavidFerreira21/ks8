# Exercício avançado 04.02 — XRD, Composition, Function e XR reais

[← Lab 04.02](../../README.md) · [↑ Preparação do Crossplane](../../../../../../docs/ambientes/04-crossplane.md)

> **Opcional e funcional:** requer Crossplane **v2 compatível** instalado no Kind descartável, Function pronta e a XRD do lab principal registrada. **Não utiliza Provider cloud ou credenciais AWS**. Não faz parte da CI Kind padrão.

## Hipótese

Uma XRD apenas registra o contrato `XEnvironment`. Uma Composition selecionada por `spec.crossplane.compositionRef` e executada pela Function Go Templating deve materializar um ConfigMap no namespace da XR e atualizá-lo quando `spec.tier` mudar.

## Fase A — Verificar pré-requisitos

```bash
kubectl config current-context         # kind-dev
kubectl get xrd xenvironments.platform.example.org
kubectl wait --for=condition=Established xrd/xenvironments.platform.example.org --timeout=120s
kubectl get pods -n crossplane-system
```

Se faltar XRD, execute o [lab básico 04.02](../../README.md) e crie a definição antes da Composition.

## Fase B — Instalar Function e Composition didáticas

```bash
kubectl apply -f trilhas/04-platform-engineering/labs/crossplane-basico/examples/composition-avancada/function.yaml
kubectl wait --for=condition=Healthy function/crossplane-contrib-function-go-templating --timeout=180s
kubectl apply -f trilhas/04-platform-engineering/labs/crossplane-basico/examples/composition-avancada/composition.yaml
kubectl get composition xenvironment-configmap-lab
```

A Function utiliza um pacote oficial fixado no exemplo. Confirme compatibilidade com sua versão do Crossplane antes da instalação.

## Fase C — Criar XR e observar reconciliação

```bash
kubectl apply -f trilhas/04-platform-engineering/labs/crossplane-basico/examples/composition-avancada/xr.yaml
kubectl get xenvironments.platform.example.org -n lab-04-02 -o wide
kubectl get configmap env-ambiente-didatico -n lab-04-02 -o yaml
kubectl get configmap env-ambiente-didatico -n lab-04-02 -o jsonpath='{.data.tier}'
```

**Esperado:** `sandbox`. Se o ConfigMap não aparecer, examine condições/eventos da XR, Revision da Composition, Function Healthy e RBAC do Crossplane; apenas a presença da XR não comprova composição.

## Fase D — Provocar drift de intenção e observar nova reconciliação

```bash
kubectl patch xenvironments.platform.example.org ambiente-didatico -n lab-04-02 --type merge -p '{"spec":{"tier":"staging"}}'
kubectl get configmap env-ambiente-didatico -n lab-04-02 -o jsonpath='{.data.tier}'
```

**Esperado:** `staging`, após reconciliação. Aguarde e repita a consulta; não presuma atualização síncrona. Registre valor anterior/posterior, status da XR, Function e nome da Composition selecionada.

## Fase E — Reversão e segurança

```bash
kubectl delete -f trilhas/04-platform-engineering/labs/crossplane-basico/examples/composition-avancada/xr.yaml --ignore-not-found
kubectl get cm env-ambiente-didatico -n lab-04-02 --ignore-not-found
kubectl delete -f trilhas/04-platform-engineering/labs/crossplane-basico/examples/composition-avancada/composition.yaml --ignore-not-found
```

**Function é global:** exclua-a **somente se foi instalada exclusivamente para este exercício** e nenhum outro Composition a utiliza. A XRD também é global; não exclua antes de inventariar XRs em todos os namespaces. O `make lab-down LAB=04.02` tem proteção adicional contra exclusão de XRD usada por outras instâncias.

## Checklist de evidências

- [ ] XRD `Established` e Function `Healthy`.
- [ ] XR contém `spec.crossplane.compositionRef` para a Composition didática.
- [ ] ConfigMap real foi criado pela Composition com `data.tier=sandbox`.
- [ ] Alterar a XR para staging atualizou o mesmo ConfigMap sem aplicação manual do YAML dele.
- [ ] Recursos de teste foram removidos sem apagar definições globais compartilhadas.

[Documentação oficial — primeiro Composition](https://docs.crossplane.io/latest/get-started/get-started-with-composition/) · [Seleção da Composition](https://docs.crossplane.io/latest/composition/composite-resources/)
