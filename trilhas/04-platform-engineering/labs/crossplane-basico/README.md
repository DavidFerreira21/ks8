# Lab 04.02 — Crossplane

[← Aula 04.02](../../crossplane/README.md) · [↑ Camada 04](../../README.md) · [🧪 Índice dos labs](../../../../docs/labs.md)

> **MODO DESAFIO:** `make lab-prepare LAB=04.02` cria o namespace e copia um starter incompleto para `.labs/04.02/resources.yaml`. **Instale previamente o controlador/CRD do produto** de acordo com o procedimento documentado; complete o YAML e execute `kubectl apply -f .labs/04.02/` após validar no servidor. O comando `make lab-up` usa a solução e é exclusivo de CI com os addons adequados.

## Objetivo e hipótese

Criar uma XRD v2 e comprovar registro da API sem confundir XR com infraestrutura provisionada.

**Contexto:** `kind-dev` ou cluster de sandbox explicitamente autorizado, namespace de estudo `lab-04-02`. `make lab-test` verifica objetos, **não prova sozinho a funcionalidade do controller**.

## Pré-requisitos da ferramenta

**Guia de instalação, versões e reversão:** [🛠️ Preparar Crossplane](../../../../docs/ambientes/04-crossplane.md). Siga-o antes de aplicar Custom Resources; a CI padrão não instala esse controlador.

**Instale Crossplane v2** em um cluster Kind descartável seguindo o guia oficial; confirme `kubectl api-resources --api-group=apiextensions.crossplane.io`. Não configure Providers cloud nem credenciais. O XRD é de escopo de cluster.

**Segurança:** XRD de escopo cluster, apenas em Kind descartável. `make lab-down` exclui a XRD; remova instâncias antes para evitar exclusão acidental.

## Desafio — o que você vai construir

Escreva uma CompositeResourceDefinition `xenvironments.platform.example.org` com `scope: Namespaced`, grupo e versão `v1alpha1`, tipo `XEnvironment` e schema exigindo `spec.tier` como string enum `sandbox/staging`.

Defina sua hipótese antes de consultar `solution/`. Se o tipo não aparecer em `kubectl api-resources`, registre dependência ausente e não tente contornar com recursos fictícios.

## Fase 1 — Preparar e prever

```bash
kubectl config current-context
make lab-prepare LAB=04.02
cat .labs/04.02/resources.yaml
```

Confirme disponibilidade da API específica da ferramenta e o namespace alvo antes de aplicar.

## Fase 2 — Aplicar e observar

Complete os TODOs:

```bash
kubectl apply --dry-run=server --validate=strict -f .labs/04.02/
kubectl apply -f .labs/04.02/
make lab-test LAB=04.02
make lab-observe LAB=04.02
```

`kubectl get xrd xenvironments.platform.example.org -o yaml`, `kubectl api-resources --api-group=platform.example.org` e `kubectl explain xenvironments.spec` comprovam o tipo registrado.

## Fase 3 — Experimento controlado

Quando o XRD estiver Established, crie **temporariamente** uma XR a partir de `examples/xr.yaml` e observe que ela não produz ConfigMap nem recurso externo sem Composition compatível; remova a XR antes de excluir a XRD. Teste também `spec.tier: 123` por `--dry-run=server` e registre o schema inválido.

## Resultado esperado e evidências

O tipo `XEnvironment` fica disponível na API; a instância pode existir sem estado Ready ou recursos derivados até que uma Composition/Function produza o resultado esperado.

**Evidências específicas:** registre XRD Established, discovery, validação de schema e ausência de composição funcional; não trate instância sem recursos como reconciliação de infraestrutura.

## Fase 4 — Diagnosticar

Investigue CRDs, condições dos custom resources, logs do controller instalado e permissões. Diferencie **rejeição de API**, **ausência de controller**, **reconciliação não pronta** e **falta de dependência externa**.

## Fase 5 — Limpar com segurança

```bash
make lab-down LAB=04.02
make lab-status LAB=04.02
```

**Proteção global:** `make lab-down` recusa excluir a XRD enquanto houver instâncias `XEnvironment` em qualquer namespace. Exclua somente a XR didática que você criou; nunca force a exclusão da XRD de outros consumidores. A limpeza remove os objetos declarados neste contrato, **não desinstala automaticamente o addon**. Revise recursos filhos, credenciais e qualquer custo externo antes de excluir a instalação. Na ausência do addon, não tente remoção indiscriminada.

## Critérios de conclusão

- [ ] Escrevi o manifesto principal sem copiar a solução e validei as APIs necessárias.
- [ ] **Critério exclusivo 04.02:** registre XRD Established, discovery, validação de schema e ausência de composição funcional; não trate instância sem recursos como reconciliação de infraestrutura.
- [ ] Diferenciei validação declarativa de comportamento funcional realmente observado.
- [ ] Reverti mudanças temporárias e executei a limpeza segura.

## Perguntas de diagnóstico e reflexão

- O que a XRD define e o que a Composition implementa?
- Por que uma XR pode existir sem recursos derivados?
- Qual risco há em excluir uma XRD instalada no cluster?

## Aprofunde seus conhecimentos

[Documentação oficial](https://docs.crossplane.io/latest/composition/composite-resource-definitions/) · [Aula 04.02](../../crossplane/README.md)

---

[← Lab 04.01](../argo-cd-basico/README.md) · [↑ Aula 04.02](../../crossplane/README.md) · [↑ Camada 04](../../README.md) · [Próximo: Lab 04.03 →](../kyverno-basico/README.md)
