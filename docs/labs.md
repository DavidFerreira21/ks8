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

A partir da raiz do repositório:

| Comando | Comportamento |
| --- | --- |
| `make help` | Exibe os alvos disponíveis |
| `make up` | Cria o cluster Kind somente se não existir |
| `make nodes` | Inspeciona os Nodes do contexto esperado |
| `make status` | Exibe recursos do namespace de laboratório |
| `make validate` | Confere sintaxe e invariantes básicas de quatro manifests |
| `make lab-up` | Cria namespace, Deployment e Service do lab integrado |
| `make lab-test` | Aguarda rollout e inspeciona Service/EndpointSlices |
| `make lab-down` | Exclui apenas Deployment e Service do lab |
| `make down` | Exclui o cluster Kind local `dev` (ação destrutiva) |

`make lab-up` **não** executa a etapa manual de Pod individual do lab integrado, para preservar a sequência didática. Execute essa etapa a partir do [README do laboratório](../trilhas/01-fundamentos/labs/primeira-aplicacao/README.md).

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
