# Lab 04.05 — Karpenter

[← Aula 04.05](../../karpenter/README.md) · [↑ Camada 04](../../README.md) · [🧪 Índice dos labs](../../../../docs/labs.md)

> **MODO DESAFIO:** `make lab-prepare LAB=04.05` cria o namespace e copia um starter incompleto para `.labs/04.05/resources.yaml`. **Instale previamente o controlador/CRD do produto** de acordo com o procedimento documentado; complete o YAML e execute `kubectl apply -f .labs/04.05/`. O comando `make lab-up` usa a solução e é exclusivo de CI com os addons adequados.

## Objetivo e hipótese

Escrever NodePool com NodeClass explícita e limites que impedem provisionamento, distinguindo configuração de capacidade real.

**Contexto:** `kind-dev` ou cluster de sandbox explicitamente autorizado, namespace de estudo `lab-04-05`. `make lab-test` verifica objetos, **não prova sozinho a funcionalidade do controller**.

## Pré-requisitos da ferramenta

**Este lab exige cluster EKS de sandbox com Karpenter AWS provider instalado e autorização explícita.** Não execute no Kind padrão; um node pool com NodeClass não configurada e limits.nodes 0 é didático e não deve provisionar nós.

**Segurança:** **Cloud-only e dependente de autorização.** O manifesto foi intencionalmente desarmado para não criar infraestrutura; não é homologação funcional de escala.

## Desafio — o que você vai construir

Produza um NodePool AWS `estudo-sem-provisionar`, referenciando `EC2NodeClass` `nao-configurada`, requirements amd64/on-demand e **limits.nodes: 0** para impedir consumo cloud no exemplo.

Defina sua hipótese antes de consultar `solution/`. Se o tipo não aparecer em `kubectl api-resources`, registre dependência ausente e não tente contornar com recursos fictícios.

## Fase 1 — Preparar e prever

```bash
kubectl config current-context
make lab-prepare LAB=04.05
cat .labs/04.05/resources.yaml
```

Confirme disponibilidade da API específica da ferramenta e o namespace alvo antes de aplicar.

## Fase 2 — Aplicar e observar

Complete os TODOs:

```bash
kubectl apply -f .labs/04.05/
make lab-test LAB=04.05
make lab-observe LAB=04.05
```

Use `kubectl get nodepool estudo-sem-provisionar -o yaml`, `kubectl get nodeclaims` e `kubectl describe nodepool estudo-sem-provisionar`. Confirme NodeClass ausente/NotReady e zero NodeClaims do lab.

## Fase 3 — Experimento controlado

Compare os campos de `nodeClassRef`, requirements e limits com NodePool existente autorizado. Explique o que precisaria mudar **em um exercício separado e aprovado** para permitir capacidade real; não altere limits para valor positivo neste lab.

## Resultado esperado e evidências

NodePool pode ser registrado, mas não está apto a provisionar capacidade: NodeClass não configurada e limite zero. Nenhum gasto AWS é esperado por este exercício.

**Evidências específicas:** registre NodePool spec, readiness/conditions e ausência de NodeClaims criados; não afirme teste de autoscaling de nós.

## Fase 4 — Diagnosticar

Investigue CRDs, condições dos custom resources, logs do controller instalado e permissões. Diferencie **rejeição de API**, **ausência de controller**, **reconciliação não pronta** e **falta de dependência externa**.

## Fase 5 — Limpar com segurança

```bash
make lab-down LAB=04.05
make lab-status LAB=04.05
```

A limpeza remove os objetos declarados neste contrato, **não desinstala automaticamente o addon**. Revise recursos filhos, credenciais e qualquer custo externo antes de excluir a instalação. Na ausência do addon, não tente remoção indiscriminada.

## Critérios de conclusão

- [ ] Escrevi o manifesto principal sem copiar a solução e validei as APIs necessárias.
- [ ] **Critério exclusivo 04.05:** registre NodePool spec, readiness/conditions e ausência de NodeClaims criados; não afirme teste de autoscaling de nós.
- [ ] Diferenciei validação declarativa de comportamento funcional realmente observado.
- [ ] Reverti mudanças temporárias e executei a limpeza segura.

## Perguntas de diagnóstico e reflexão

- Por que NodePool sem NodeClass pronta não provisiona?
- Como Karpenter e HPA se complementam?
- Qual diferença entre EC2NodeClass do Karpenter AWS e NodeClass do EKS Auto Mode?

## Aprofunde seus conhecimentos

[Documentação oficial](https://karpenter.sh/docs/concepts/nodepools/) · [Aula 04.05](../../karpenter/README.md)

---

[← Lab 04.04](../external-secrets-operator-basico/README.md) · [↑ Aula 04.05](../../karpenter/README.md) · [↑ Camada 04](../../README.md) · [Próximo: Lab 04.06 →](../cilium-basico/README.md)
