# Lab 04.04 — External Secrets Operator

[← Aula 04.04](../../external-secrets-operator/README.md) · [↑ Camada 04](../../README.md) · [🧪 Índice dos labs](../../../../docs/labs.md)

> **MODO DESAFIO:** `make lab-prepare LAB=04.04` cria o namespace e copia um starter incompleto para `.labs/04.04/resources.yaml`. **Instale previamente o controlador/CRD do produto** de acordo com o procedimento documentado; complete o YAML e execute `kubectl apply -f .labs/04.04/`. O comando `make lab-up` usa a solução e é exclusivo de CI com os addons adequados.

## Objetivo e hipótese

Sincronizar segredo fictício com SecretStore Fake e verificar somente metadados e status do Secret alvo.

**Contexto:** `kind-dev` ou cluster de sandbox explicitamente autorizado, namespace de estudo `lab-04-04`. `make lab-test` verifica objetos, **não prova sozinho a funcionalidade do controller**.

## Pré-requisitos da ferramenta

**Instale External Secrets Operator** compatível com `external-secrets.io/v1` em Kind isolado. O Fake Provider não usa API keys nem serviços externos.

**Segurança:** Não inclua credenciais reais ou valores sensíveis em manifests, logs ou Git; `base64` não é criptografia.

## Desafio — o que você vai construir

Escreva SecretStore `simulado` com provedor Fake, contendo chave `/lab/exemplo` versão `v1` e valor **fictício** `TREINO-SEM-SEGREDO`; escreva ExternalSecret `demo` que produza `Secret` `segredo-didatico`.

Defina sua hipótese antes de consultar `solution/`. Se o tipo não aparecer em `kubectl api-resources`, registre dependência ausente e não tente contornar com recursos fictícios.

## Fase 1 — Preparar e prever

```bash
kubectl config current-context
make lab-prepare LAB=04.04
cat .labs/04.04/resources.yaml
```

Confirme disponibilidade da API específica da ferramenta e o namespace alvo antes de aplicar.

## Fase 2 — Aplicar e observar

Complete os TODOs:

```bash
kubectl apply -f .labs/04.04/
make lab-test LAB=04.04
make lab-observe LAB=04.04
```

Use `kubectl get secretstore,externalsecret -n lab-04-04` e `kubectl get secret segredo-didatico -n lab-04-04 -o jsonpath='{.metadata.name}'` sem exibir `.data`.

## Fase 3 — Experimento controlado

Observe Ready do ExternalSecret e a criação do Secret. Altere temporariamente o `remoteRef.key` para um valor inexistente e compare condições de erro; restaure o manifesto local. Nunca substitua o Fake Provider por credencial real no lab.

## Resultado esperado e evidências

Com ESO saudável, o Secret alvo é materializado com dado **fictício**. Erro de referência impede sincronização conforme condições do controlador.

**Evidências específicas:** registre referências do SecretStore, condição Ready do ExternalSecret, existência do Secret e o resultado após referência inválida sem revelar valores.

## Fase 4 — Diagnosticar

Investigue CRDs, condições dos custom resources, logs do controller instalado e permissões. Diferencie **rejeição de API**, **ausência de controller**, **reconciliação não pronta** e **falta de dependência externa**.

## Fase 5 — Limpar com segurança

```bash
make lab-down LAB=04.04
make lab-status LAB=04.04
```

A limpeza remove os objetos declarados neste contrato, **não desinstala automaticamente o addon**. Revise recursos filhos, credenciais e qualquer custo externo antes de excluir a instalação. Na ausência do addon, não tente remoção indiscriminada.

## Critérios de conclusão

- [ ] Escrevi o manifesto principal sem copiar a solução e validei as APIs necessárias.
- [ ] **Critério exclusivo 04.04:** registre referências do SecretStore, condição Ready do ExternalSecret, existência do Secret e o resultado após referência inválida sem revelar valores.
- [ ] Diferenciei validação declarativa de comportamento funcional realmente observado.
- [ ] Reverti mudanças temporárias e executei a limpeza segura.

## Perguntas de diagnóstico e reflexão

- Por que ExternalSecret não é o mesmo que Secret?
- O que faz o SecretStore e por que seu escopo importa?
- Como diagnosticar falha do provedor sem imprimir o conteúdo do Secret?

## Aprofunde seus conhecimentos

[Documentação oficial](https://external-secrets.io/latest/provider/fake/) · [Aula 04.04](../../external-secrets-operator/README.md)

---

[← Lab 04.03](../kyverno-basico/README.md) · [↑ Aula 04.04](../../external-secrets-operator/README.md) · [↑ Camada 04](../../README.md) · [Próximo: Lab 04.05 →](../karpenter-basico/README.md)
