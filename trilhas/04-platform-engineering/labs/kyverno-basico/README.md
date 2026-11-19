# Lab 04.03 — Kyverno

[← Aula 04.03](../../kyverno/README.md) · [↑ Camada 04](../../README.md) · [🧪 Índice dos labs](../../../../docs/labs.md)

> **MODO DESAFIO:** `make lab-prepare LAB=04.03` cria o namespace e copia um starter incompleto para `.labs/04.03/resources.yaml`. **Instale previamente o controlador/CRD do produto** de acordo com o procedimento documentado; complete o YAML e execute `kubectl apply --dry-run=server --validate=strict -f .labs/04.03/
kubectl apply -f .labs/04.03/`. O comando `make lab-up` usa a solução e é exclusivo de CI com os addons adequados.

## Objetivo e hipótese

Aplicar política namespaced CEL de validação e comprovar rejeição de um ConfigMap sem label obrigatória.

**Contexto:** `kind-dev` ou cluster de sandbox explicitamente autorizado, namespace de estudo `lab-04-03`. `make lab-test` verifica objetos, **não prova sozinho a funcionalidade do controller**.

## Pré-requisitos da ferramenta

**Guia de instalação, versões e reversão:** [🛠️ Preparar Kyverno](../../../../docs/ambientes/04-kyverno.md). Siga-o antes de aplicar Custom Resources; a CI padrão não instala esse controlador.

**Instale Kyverno v1.17 ou superior** com `policies.kyverno.io/v1` disponível e aguarde os controladores de admissão. Este lab usa API CEL, não ClusterPolicy legada.

**Segurança:** Requer CRD/controller Kyverno e seus webhooks. O default Kind não executa policy sem instalação específica.

## Desafio — o que você vai construir

Escreva `NamespacedValidatingPolicy` `requer-equipe` com ação Deny para CREATE/UPDATE de ConfigMaps que não tenham label `equipe`.

Defina sua hipótese antes de consultar `solution/`. Se o tipo não aparecer em `kubectl api-resources`, registre dependência ausente e não tente contornar com recursos fictícios.

## Fase 1 — Preparar e prever

```bash
kubectl config current-context
make lab-prepare LAB=04.03
cat .labs/04.03/resources.yaml
```

Confirme disponibilidade da API específica da ferramenta e o namespace alvo antes de aplicar.

## Fase 2 — Aplicar e observar

Complete os TODOs:

```bash
kubectl apply -f .labs/04.03/
make lab-test LAB=04.03
make lab-observe LAB=04.03
```

Verifique `kubectl get namespacedvalidatingpolicy requer-equipe -n lab-04-03 -o yaml`. Compare com os testes em `examples/` por dry-run de servidor.

## Fase 3 — Experimento controlado

Execute `kubectl apply --dry-run=server -f trilhas/04-platform-engineering/labs/kyverno-basico/examples/sem-label.yaml` e registre rejeição. Depois teste `examples/com-label.yaml`, que deve ser aceito no dry-run. Não afete namespaces alheios.

## Resultado esperado e evidências

Com controlador ativo, ConfigMap sem `equipe` recebe negação na admissão e o com label passa. A presença do objeto policy não garante que webhooks estejam saudáveis.

**Evidências específicas:** registre policy, versão do Kyverno, retorno da API para os dois exemplos e motivo da rejeição; caso nenhum seja barrado, investigue controller e admission.

## Fase 4 — Diagnosticar

Investigue CRDs, condições dos custom resources, logs do controller instalado e permissões. Diferencie **rejeição de API**, **ausência de controller**, **reconciliação não pronta** e **falta de dependência externa**.

## Fase 5 — Limpar com segurança

```bash
make lab-down LAB=04.03
make lab-status LAB=04.03
```

A limpeza remove os objetos declarados neste contrato, **não desinstala automaticamente o addon**. Revise recursos filhos, credenciais e qualquer custo externo antes de excluir a instalação. Na ausência do addon, não tente remoção indiscriminada.

## Critérios de conclusão

- [ ] Escrevi o manifesto principal sem copiar a solução e validei as APIs necessárias.
- [ ] **Critério exclusivo 04.03:** registre policy, versão do Kyverno, retorno da API para os dois exemplos e motivo da rejeição; caso nenhum seja barrado, investigue controller e admission.
- [ ] Diferenciei validação declarativa de comportamento funcional realmente observado.
- [ ] Reverti mudanças temporárias e executei a limpeza segura.

## Perguntas de diagnóstico e reflexão

- Qual diferença entre ação Deny e Audit?
- Como comprovar que a negação ocorreu antes da criação?
- Por que este exemplo não deve ser instalado em namespace compartilhado?

## Aprofunde seus conhecimentos

[Documentação oficial](https://kyverno.io/docs/policy-types/validating-policy/) · [Aula 04.03](../../kyverno/README.md)

---

[← Lab 04.02](../crossplane-basico/README.md) · [↑ Aula 04.03](../../kyverno/README.md) · [↑ Camada 04](../../README.md) · [Próximo: Lab 04.04 →](../external-secrets-operator-basico/README.md)
