# Padrão editorial — Kubernetes Learning Path

[⌂ Início](../README.md) · [📦 Camada 01](../trilhas/01-fundamentos/README.md) · [🧪 Guia dos labs](labs.md)

> **Finalidade:** contrato de autoria e revisão de novas aulas e labs nas quatro camadas. A **Camada 01 é a referência editorial**; a homologação funcional no Kind é uma etapa distinta e depende de evidências. O objetivo é padronizar qualidade, não produzir documentação repetitiva.

**Aplicabilidade às quatro camadas:** o contrato vale para todos os 52 temas. Uma ferramenta que não existe no Kind padrão pode ter lab com CRs reais e instruções de instalação controlada, desde que informe dependência, evidência possível, cleanup e **não alegue homologação funcional sem execução adequada**. Os complementares só aparecem onde agregam análise ou diagnóstico.

## Três tipos de conteúdo, três funções

| Conteúdo | Obrigatório? | O que deve entregar | O que não deve fazer |
| --- | --- | --- | --- |
| **Aula** | Sim, para cada ID curricular | Conceito, problema, funcionamento, exemplo interpretado, observação, revisão específica, links | Substituir roteiro executável ou repetir documentação genérica |
| **Lab** | Quando anunciado como disponível | Aluno escreve/aplica YAML, observa, experimenta, diagnostica, registra evidência e limpa | Aplicar a solução como caminho principal do aluno |
| **Complementar** | Não | Consulta técnica, cenários alternativos, comandos, comparações, anti-padrões e documentação oficial | Repetir a aula ou virar pré-requisito oculto do lab |

## Contrato da aula

- [ ] **ID, conceito e objetivo específico:** frase com uma capacidade demonstrável; evite o objetivo genérico reutilizado entre aulas.
- [ ] **Infográfico** com caminho válido e conteúdo coerente com a explicação.
- [ ] **Problema e mecanismo:** por que o recurso existe, os componentes envolvidos e como o comportamento aparece no cluster.
- [ ] **Exemplo curto e interpretado:** YAML e/ou comandos suficientes para compreender o objeto, sem entregar o lab inteiro.
- [ ] **Operação e limitações:** como observar sinais reais; limites de segurança e de funcionamento pertinentes ao conceito.
- [ ] **Aplicação prática:** link para o lab correspondente ou indicação transparente quando indisponível.
- [ ] **Complementar opcional:** link somente quando existe conteúdo adicional específico, sem duplicação.
- [ ] **Revisão específica:** ao menos três perguntas sobre decisões, efeitos e diagnóstico do próprio conceito.
- [ ] **Referência oficial e navegação:** anterior, camada, próxima e links verificáveis.

A aula não precisa forçar todos os títulos literalmente: o conteúdo deve seguir uma ordem lógica de aprendizado. Exemplos de Secrets nunca devem conter credenciais reais.

## Contrato do lab

O aluno deve conseguir concluir a prática estudando a aula e usando documentação oficial, sem depender de solução pronta nem de complementar opcional.

1. **Objetivo e hipótese:** o que será demonstrado e previsto.
2. **Pré-requisitos:** Kind/contexto esperado, ferramentas e addons necessários, quando houver.
3. **Desafio YAML:** recursos, nomes, campos e critérios observáveis; arquivos de starter são editados pelo aluno.
4. **Preparação e inspeção:** `make lab-prepare LAB=...`, sem aplicar a solução.
5. **Aplicação e observação:** `kubectl apply` pelo aluno, `make lab-observe` e `make lab-test`; não tratar sucesso estático como prova funcional.
6. **Experimento:** provoque mudança ou falha controlada, observe o efeito e registre a hipótese inicial.
7. **Resultado esperado:** evidência identificável de estado, evento, tráfego, persistência ou métrica conforme a aula.
8. **Diagnóstico e reflexão:** perguntas específicas que expliquem causas e resultados.
9. **Critérios e limpeza:** checklist, `make lab-down` no contexto seguro e limites explícitos da limpeza.
10. **Fontes e navegação:** docs oficiais, aula, lab anterior e próximo.

**Cada lab deve detalhar suas evidências específicas** (por exemplo, HTTP para Ingress, métricas e réplicas para HPA, arquivo persistente para Volumes). O texto genérico de evidências permanece neste contrato, sem ser repetido literalmente em todos os laboratórios.

**Evidências mínimas de conclusão:** (a) manifesto/recurso criado pelo aluno; (b) comportamento real observado; (c) explicação do motivo e, se falhou, diagnóstico. O laboratório pode ter mais de quatro fases quando o experimento justificar (Services, por exemplo). Não renumerar fases sem necessidade.

**Segurança de APIs globais:** CRDs/XRDs podem atender instâncias de múltiplos namespaces. Antes de excluir a definição, inventarie recursos dependentes; recuse a operação se houver instâncias não removidas. Não use um cleanup automático cego em objetos de escopo do cluster.

**Evidência pedagógica:** além dos critérios genéricos, todo lab deve possuir ao menos um critério de aprovação exclusivo, verificável por observação. Para testes que alteram políticas, nós ou recursos temporários, inclua reversão explícita mesmo em caso de falha. Separe validação declarativa, comportamento real e diagnóstico.

**Dependências especiais da Camada 01:** PVC requer StorageClass/provisionador funcional (01.11); Ingress exige controller e teste de tráfego (01.13); HPA exige Metrics Server, CPU requests e teste de carga (01.14). Sem esses componentes, marque a validação funcional como **pendente**.

## Contrato do complementar

Se houver valor adicional, use apenas as seções necessárias: **quando consultar**, **comparações ou alternativas**, **exemplos adicionais**, **referência de comandos**, **diagnóstico**, **limitações/boas práticas** e **referências oficiais**. Declare logo no início que é leitura opcional e inclua links de retorno à aula, lab e camada.

Não criar uma página vazia só para preencher a coluna `Complementares`.

## Regras de navegação e linguagem

- O índice da camada usa **Aula | Conceito | Aula | Lab | Complementares**.
- Links de lab usam `🧪 Lab NN.NN` e apontam para o README correspondente.
- Evitar a nomenclatura antiga **Anotações** no percurso atual; a palavra pode existir apenas em documentos históricos.
- Manter IDs curriculares estáveis e indicar claramente recursos planejados versus executáveis.
- Os caminhos históricos existentes podem permanecer até migração planejada; não mover arquivos sem atualizar todos os links.
- Comandos de alteração de estado devem destacar impacto, namespace/contexto e limpeza segura.
- Preferir documentação oficial estável e revisitar exemplos conforme novas versões do Kubernetes.

**Checklist transversal da trilha:** todos os 52 temas precisam de objetivo e três perguntas específicas por aula, três questões de diagnóstico por lab, material complementar **somente quando houver ganho real** e links de retorno. A coluna Complementares deve usar a página curricular canônica e conservar o acesso ao histórico. Subtítulos internos podem variar quando isso melhora a didática, mas a seção final `## 🔗 Referências oficiais` é estável em todas as aulas.

**Links e atualizações:** os links relativos/imagens são testados em todo PR; a [auditoria semanal de URLs externas](../.github/workflows/external-links.yml) confirma 404/410 e publica relatório, sem confundir rate-limit ou bloqueio antibot com link definitivamente quebrado.

## Qualidade e validação

| Nível | Critério | O que comprova |
| --- | --- | --- |
| 1 — Editorial | Objetivo, revisão específica, estrutura e links | Revisão humana + verificações estáticas |
| 2 — Contratos | Manifestos, starters, definições `lab.yaml` e checks | `make validate` e testes Python |
| 3 — Integração | Aplicação/validação dos labs cobertos pela CI | Workflow Kind no GitHub Actions |
| 4 — Funcional completa | Experimentos com PVC, controller HTTP e métricas | Execução documentada no Kind e observação de resultados |

**Declaração de status:** "Camada 01 como padrão editorial" significa contrato e conteúdo de referência consolidados; **não significa** que todos os 14 labs foram homologados funcionalmente. Para declarar a camada *completamente validada*, registre resultados dos 14 labs, addons, data/versões, falhas e evidências.

## Checklist de PR para novas camadas

- [ ] Aulas e labs usam IDs corretos e índice atualizado.
- [ ] Objetivos e perguntas não são genéricos ou repetidos sem motivo.
- [ ] Os exemplos respeitam escopo pedagógico e evitam credenciais reais.
- [ ] Complementares são opcionais e não duplicam aulas.
- [ ] Links relativos e infográficos existem.
- [ ] O lab começa sem solução aplicada pelo motor.
- [ ] O experimento possui evidências e diagnóstico.
- [ ] CI e limites de validação estão explicitamente documentados.
