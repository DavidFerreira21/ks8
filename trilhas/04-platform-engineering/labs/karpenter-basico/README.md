# Lab 04.05 — Karpenter

[← Aula 04.05](../../karpenter/README.md) · [↑ Camada 04](../../README.md) · [🧪 Índice dos labs](../../../../docs/labs.md)

> **MODO DESAFIO — cloud opcional:** use `make lab-prepare LAB=04.05` **somente no Kind local** para obter o starter. Complete o NodePool e valide o desenho por inspeção estática. O motor de labs é bloqueado para qualquer contexto que não seja Kind; **não use `make lab-up`, `make lab-test` ou `make lab-down` contra EKS**. A aplicação real é uma etapa separada e só deve ocorrer em cluster AWS de sandbox autorizado, com contextos explícitos.

## Objetivo e hipótese

Escrever NodePool com NodeClass explícita e limites que impedem provisionamento, distinguindo configuração de capacidade real.

**Contexto:** use `kind-dev` para preparar/validar arquivos localmente. Para API Karpenter real, utilize apenas EKS de sandbox **explicitamente autorizado**, com `kubectl --context` apontando para esse ambiente. A ferramenta `labctl` não suporta operar no EKS.

## Pré-requisitos da ferramenta

**Guia de instalação, versões e reversão:** [🛠️ Preparar Karpenter](../../../../docs/ambientes/04-karpenter.md). Siga-o antes de aplicar Custom Resources; a CI padrão não instala esse controlador.

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

Complete os TODOs, depois execute **somente validação estática local**:

```bash
python3 scripts/validate_karpenter_lab.py .labs/04.05/resources.yaml
kubectl config current-context
```

**Execução AWS opcional, somente após autorização:** confirme um contexto EKS de sandbox, leia os manifests com atenção e aplique explicitamente usando `kubectl --context CONTEXTO-EKS-SANDBOX apply -f .labs/04.05/resources.yaml`. Não faça isso em contexto de produção. O NodePool está limitado a **zero nós** e aponta para NodeClass inexistente justamente para evitar provisionamento. Sem EKS autorizado, registre **dependência funcional não atendida**.

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
# Na sessão Kind local, apenas confira arquivos e namespace.
make lab-status LAB=04.05
```

**Se a aplicação opcional ocorreu no EKS autorizado**, elimine o NodePool com `kubectl --context CONTEXTO-EKS-SANDBOX delete -f .labs/04.05/resources.yaml --ignore-not-found` e confira que nenhum NodeClaim/nó foi provisionado. `make lab-down` não atua sobre o contexto EKS.

A validação offline lê **o arquivo realmente escrito pelo aluno**, sem chamar o API Server e sem criar NodePool. `make validate` sozinho valida os manifests de referência do repositório, não substitui essa conferência. Qualquer limpeza de recurso AWS aplicada manualmente deve usar o **mesmo contexto EKS aprovado**, com conferência de NodeClaims e custos. Nunca altere o contexto do laboratório automaticamente.

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
