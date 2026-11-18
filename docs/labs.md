# Guia de execução dos laboratórios

[← Início](../README.md) · [Roadmap](roadmap.md)

## Modelo de laboratório

Cada lab deve documentar: objetivo, pré-requisitos, manifests, sequência de comandos, resultado esperado, investigação de falhas, limpeza e referências oficiais. As atividades novas devem demonstrar o comportamento de um recurso, não somente sua criação.

## Pré-requisitos locais

- `docker`, `kind`, `kubectl`, `make`, `python3`.
- Para `make validate`: `python3 -m pip install 'PyYAML>=6,<7'`.
- Um cluster criado por `make up` usará o nome `dev` e contexto `kind-dev` por padrão.

Confira as versões e os requisitos do [guia de instalação existente](../install-kind.md). A configuração principal do cluster continua em [kind-config.yaml](../kind-config.yaml).

## Comandos padronizados

A interface do Makefile usa `LAB=<id>`. O lab padrão é `01.06` (primeira aplicação).

```bash
make doctor
make up
make labs
make lab-up LAB=01.06
make lab-status LAB=01.06
make lab-test LAB=01.06
make lab-observe LAB=01.06
make lab-experiment LAB=01.06 EXPERIMENT=controlled-rollout
make lab-down LAB=01.06
```

| Comando | Finalidade |
| --- | --- |
| `make doctor` | Conferir ferramentas e Docker |
| `make labs` | Descobrir os labs cadastrados |
| `make validate` | Verificar contratos e manifests por inspeção |
| `make lab-up LAB=02.02` | Aplicar o lab RBAC e seus pré-requisitos |
| `make lab-test LAB=02.02` | Conferir permissões permitidas e negadas |
| `make lab-up LAB=02.04` | Aplicar quota, LimitRange e Pod de teste |
| `make lab-test LAB=02.04` | Conferir existência de quota e Pod (rejeição fica para experimento específico) |
| `make lab-observe LAB=01.06` | Mostra condições, eventos e recursos relacionados |
| `make lab-experiment LAB=02.04 EXPERIMENT=reject-pod` | Espera e verifica rejeição intencional por quota |
| `make lab-experiment LAB=01.06 EXPERIMENT=controlled-rollout` | Reinicia o Deployment do lab e observa a reconciliação |
| `make lab-down LAB=02.04` | Remover somente os manifests cadastrados; preservar o namespace |
| `make down` | Excluir o cluster Kind local (ação destrutiva) |

**Segurança:** as operações conferem se o contexto é `kind-<CLUSTER_NAME>` e se o cluster Kind existe. Nenhuma operação do lab deve mirar um contexto diferente do esperado. `lab-down` preserva namespaces por padrão; não pressupõe que estejam vazios.

**Sequência didática:** no lab `01.06` o Pod individual continua sendo criado manualmente conforme o README; o comando automatizado aplica apenas Deployment e Service para não ocultar a primeira etapa.


## Camada 02 — Operação e Segurança

- [RBAC e ServiceAccount](../trilhas/02-operacao-seguranca/labs/rbac-minimo/README.md): exercício de menor privilégio com autorização permitida/negada.
- [ResourceQuota e LimitRange](../trilhas/02-operacao-seguranca/labs/quota-namespace/README.md): defaults de recursos e rejeição intencional por quota.

Ambos podem ser preparados e verificados usando `LAB=02.02` ou `LAB=02.04`. O experimento `reject-pod` faz uma tentativa controlada de admissão e **só considera sucesso se identificar rejeição por quota**, nunca qualquer erro genérico.

## Aprendizado orientado por observação

O fluxo recomendado é **aplicar → observar → experimentar → testar → limpar**. O comando `lab-observe` mostra recursos do namespace e eventos recentes, além de destacar Deployments, quotas e EndpointSlices quando relevantes.

Os experimentos têm **IDs pré-definidos** em `lab.yaml`, não aceitam comandos arbitrários e exigem confirmação explícita via `--confirm` no CLI (o alvo `make lab-experiment` confirma a ação por ser um comando dedicado). O rollout controlado exige que o Deployment já exista; o teste de quota depende do Pod inicial estar presente.

**Importante:** não execute os experimentos em clusters compartilhados. No experimento de quota, se a segunda criação for admitida inesperadamente, o comando falha e o Pod inesperado precisa ser removido após inspeção; o sistema não tenta apagar recursos às cegas.

## Diagnóstico

```bash
bash scripts/lab-diagnostics.sh
```

O script verifica o contexto antes de consultar recursos e não modifica o cluster. Também é possível definir `EXPECTED_CONTEXT` e `NAMESPACE` para ambientes locais diferentes.

## Segurança e limitações

- Os alvos `lab-up`, `lab-test` e `lab-down` falham se o contexto não for o Kind esperado.
- `make down` remove o cluster Kind indicado por `CLUSTER_NAME`. Verifique esse valor antes da execução.
- `make lab-down` **preserva o namespace** para evitar excluir recursos não relacionados.
- `make validate` realiza parse YAML e alguns checks didáticos, **não é um validador completo do schema Kubernetes**.
- A pipeline do GitHub executa verificações estáticas, mas **não cria um cluster Kind**.
- Nenhum lab foi executado em um cluster durante a elaboração deste PR.

## Referências oficiais

- [Kind Quick Start](https://kind.sigs.k8s.io/docs/user/quick-start/)
- [kubectl](https://kubernetes.io/docs/reference/kubectl/)
- [Debug Applications](https://kubernetes.io/docs/tasks/debug/debug-application/)
