# Guia de execução dos laboratórios

[← Início](../README.md) · [Roadmap](roadmap.md)

## Modelo de laboratório

Todos os labs da **Camada 01** seguem um percurso completo e repetível, adequado para quem está começando:

1. **Objetivo e conceito:** entender qual comportamento Kubernetes será estudado.
2. **Pré-requisitos:** confirmar o Kind local e addons necessários, quando houver.
3. **Desafio YAML:** receber requisitos claros e preencher os arquivos em `.labs/<ID>/` sem copiar a solução.
4. **Aplicação:** executar `kubectl apply` manualmente e observar os recursos criados.
5. **Experimento:** alterar, excluir ou provocar uma falha controlada.
6. **Resultado esperado:** comparar eventos, status, logs e hipóteses com as evidências previstas.
7. **Diagnóstico:** investigar divergências com `kubectl describe` e eventos.
8. **Critérios de conclusão:** responder às perguntas específicas do conceito.
9. **Limpeza:** remover somente os recursos do lab, preservando o cluster.
10. **Aprofundamento:** acessar a aula teórica e as páginas relevantes da documentação oficial.

As atividades precisam **mostrar o comportamento** do recurso, não apenas sua criação. O resultado esperado descreve o que o aluno deve procurar depois de tentar o desafio; a solução de referência continua separada em `solution/`.

## Pré-requisitos locais

- `docker`, `kind`, `kubectl`, `make`, `python3`.
- Para `make validate`: `python3 -m pip install 'PyYAML>=6,<7'`.
- Um cluster criado por `make up` usará o nome `dev` e contexto `kind-dev` por padrão.

Confira as versões e os requisitos do [guia de instalação existente](../install-kind.md). A configuração principal do cluster continua em [kind-config.yaml](../kind-config.yaml).

## Fluxo do aluno e CI

```bash
make lab-prepare LAB=01.02
# Complete .labs/01.02/resources.yaml (comece pela aula)
kubectl apply -f .labs/01.02/
make lab-observe LAB=01.02
make lab-test LAB=01.02
make lab-down LAB=01.02
```

`make lab-reset LAB=01.02` remove os recursos declarados e restaura o setup, **sem sobrescrever seu YAML local**. `make lab-solution LAB=01.02` mostra os caminhos das soluções de referência. **`make lab-up` é exclusivo de CI** e aplica a solução, portanto não faz parte do exercício do aluno.

## Comandos padronizados

A interface do Makefile usa `LAB=<id>`. O lab padrão é `01.01` (Fundamentos); o laboratório dedicado a Services é `01.05`.

```bash
make doctor
make up
make labs
make lab-prepare LAB=01.05
# Edite .labs/01.05/service.yaml
kubectl apply -f .labs/01.05/
make lab-status LAB=01.05
make lab-test LAB=01.05
make lab-observe LAB=01.05
make lab-down LAB=01.05
# Para estudar RollingUpdate, avance ao Lab 01.12.
```

| Comando | Finalidade |
| --- | --- |
| `make doctor` | Conferir ferramentas e Docker |
| `make labs` | Descobrir os labs cadastrados |
| `make lab-prepare LAB=01.02` | Criar workspace de YAML para aluno, namespace e setup mínimo |
| `make lab-solution LAB=01.02` | Mostrar caminhos da solução sem aplicá-la |
| `make lab-reset LAB=01.02` | Limpar recursos declarados e refazer setup sem apagar arquivos locais |
| `make validate` | Verificar contratos e manifests por inspeção |
| `make lab-up LAB=02.02` | Aplicar o lab RBAC e seus pré-requisitos |
| `make lab-test LAB=02.02` | Conferir permissões permitidas e negadas |
| `make lab-up LAB=02.04` | Aplicar quota, LimitRange e Pod de teste |
| `make lab-test LAB=02.04` | Conferir existência de quota e Pod (rejeição fica para experimento específico) |
| `make lab-observe LAB=01.05` | Mostra condições, eventos e recursos relacionados |
| `make lab-experiment LAB=02.04 EXPERIMENT=reject-pod` | Espera e verifica rejeição intencional por quota |
| `make lab-experiment LAB=01.12 EXPERIMENT=controlled-rollout` | Reinicia o Deployment do lab 01.12 e observa o rollout |
| `make lab-down LAB=02.04` | Remover somente os manifests cadastrados; preservar o namespace |
| `make down` | Excluir o cluster Kind local (ação destrutiva) |

**Segurança:** as operações conferem se o contexto é `kind-<CLUSTER_NAME>` e se o cluster Kind existe. Nenhuma operação do lab deve mirar um contexto diferente do esperado. `lab-down` preserva namespaces por padrão; não pressupõe que estejam vazios.

**Sequência didática:** no lab `01.05`, um Deployment simples fornece dois backends, mas a prática investiga apenas Services, selectors, EndpointSlices e acesso via DNS/ClusterIP. O experimento de rollout pertence ao lab 01.12.


## Camada 01 — Fundamentos

- [🧪 Lab 01.01](../trilhas/01-fundamentos/labs/fundamentos-cluster/README.md): explorar o cluster, criar ConfigMap e comparar o estado no arquivo e na API.
- [🧪 Lab 01.05](../trilhas/01-fundamentos/labs/services-basico/README.md): ClusterIP, selector, EndpointSlices e DNS.

A criação de namespaces ausentes não imprime mais um erro esperado de `NotFound`; falhas reais na consulta ao API Server continuam visíveis.

**Pré-requisitos adicionais:** o Lab 01.11 requer StorageClass funcional; o 01.13 requer um Ingress Controller (Traefik) e Helm; o 01.14 requer Metrics Server funcional. O `make lab-test` desses labs verifica seus objetos, mas **não** substitui o experimento de tráfego ou escalabilidade descrito no README.

| ID | Aula | Laboratório |
| --- | --- | --- |
| 01.01 | Fundamentos | [🧪 Lab 01.01](../trilhas/01-fundamentos/labs/fundamentos-cluster/README.md) |
| 01.02 | Pods | [🧪 Lab 01.02](../trilhas/01-fundamentos/labs/pods-basico/README.md) |
| 01.03 | Deployments | [🧪 Lab 01.03](../trilhas/01-fundamentos/labs/deployments-basico/README.md) |
| 01.04 | Controladores | [🧪 Lab 01.04](../trilhas/01-fundamentos/labs/controladores-basico/README.md) |
| 01.05 | Services | [🧪 Lab 01.05](../trilhas/01-fundamentos/labs/services-basico/README.md) |
| 01.06 | Namespaces | [🧪 Lab 01.06](../trilhas/01-fundamentos/labs/namespaces-basico/README.md) |
| 01.07 | ConfigMaps | [🧪 Lab 01.07](../trilhas/01-fundamentos/labs/configmaps-basico/README.md) |
| 01.08 | Secrets | [🧪 Lab 01.08](../trilhas/01-fundamentos/labs/secrets-basico/README.md) |
| 01.09 | Requests/Limits | [🧪 Lab 01.09](../trilhas/01-fundamentos/labs/requests-limits-basico/README.md) |
| 01.10 | Probes | [🧪 Lab 01.10](../trilhas/01-fundamentos/labs/probes-basico/README.md) |
| 01.11 | Volumes | [🧪 Lab 01.11](../trilhas/01-fundamentos/labs/volumes-basico/README.md) |
| 01.12 | Estratégias | [🧪 Lab 01.12](../trilhas/01-fundamentos/labs/estrategias-deployment-basico/README.md) |
| 01.13 | Ingress | [🧪 Lab 01.13](../trilhas/01-fundamentos/labs/ingress-basico/README.md) |
| 01.14 | HPA | [🧪 Lab 01.14](../trilhas/01-fundamentos/labs/hpa-basico/README.md) |

## Camada 02 — Operação e Segurança

- [🧪 Lab 02.02](../trilhas/02-operacao-seguranca/labs/rbac-minimo/README.md): exercício de menor privilégio com autorização permitida/negada.
- [🧪 Lab 02.04](../trilhas/02-operacao-seguranca/labs/quota-namespace/README.md): defaults de recursos e rejeição intencional por quota.

Ambos podem ser preparados e verificados usando `LAB=02.02` ou `LAB=02.04`. O experimento `reject-pod` faz uma tentativa controlada de admissão e **só considera sucesso se identificar rejeição por quota**, nunca qualquer erro genérico.

## Aprendizado orientado por observação

O fluxo recomendado é **escrever YAML → aplicar com kubectl → observar → experimentar → testar → limpar**. `make lab-prepare` cria apenas o namespace, os recursos de apoio explicitamente declarados e uma cópia local do starter em `.labs/<ID>/`, preservando suas alterações existentes. A solução não é aplicada neste comando. O comando `lab-observe` mostra recursos do namespace e eventos recentes, além de destacar Deployments, quotas e EndpointSlices quando relevantes.

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
- `make validate` analisa todos os manifests declarados nos contratos e executa checks didáticos, **não substituindo a validação completa do schema Kubernetes**.
- A pipeline do GitHub mantém verificações estáticas e agora possui um **job de integração com Kind descartável**, que executa 14 labs básicos, checks e experimentos. A existência do workflow não prova sucesso: consulte o status das execuções no GitHub Actions.
- Os novos labs não foram executados manualmente durante a elaboração deste PR. A CI os valida conforme a cobertura descrita; os labs 01.13 e 01.14 exigem teste funcional em Kind com addons.


**Modelo didático da camada:** inspecionar → aplicar → observar → experimentar → diagnosticar → limpar. As fases constam no README; o motor atual executa o `apply` declarado no contrato, e não interpreta `PHASE=`. Alterações experimentais manuais precisam ser conferidas antes da limpeza.

## Criar novos laboratórios sem copiar pastas

```bash
make new-lab LAB_ID=01.07 LAB_SLUG=configmaps-basico LAB_TITLE="ConfigMaps: variáveis"
```

Isso gera `trilhas/01-fundamentos/labs/configmaps-basico/` com:

```text
configmaps-basico/
├── README.md
├── lab.yaml.example
├── manifests/
│   └── configmap.yaml
└── tests/
    └── README.md
```

O gerador **não registra automaticamente o lab**: `lab.yaml.example` é um rascunho. Reescreva o README com objetivo, pré-requisitos, etapas, observação, diagnóstico, experimentos, limpeza e critérios de sucesso. Revise os manifests e os checks (`deployment`, `service`, `configmap`, `rbac`, `rbac-deny`, `quota`, `resource`, `pod-ready`, `pvc-bound`). Somente quando o exercício estiver pronto, renomeie para `lab.yaml`, execute `make validate` e `make labs`.

**Regras de organização:** mantenha infográfico e teoria no diretório do conceito; coloque os labs em `trilhas/<camada>/labs/<slug>`; deixe `scripts/labctl.py` como motor compartilhado; não introduza comandos shell arbitrários no contrato. IDs seguem o catálogo oficial, e cada lab publicado deve usar um ID único.

**Limitação atual:** o identificador de lab é único. Caso uma aula precise de múltiplos labs independentes, será necessário ampliar o contrato para IDs com sufixo, em uma evolução posterior.

## Referências oficiais

- [Kind Quick Start](https://kind.sigs.k8s.io/docs/user/quick-start/)
- [kubectl](https://kubernetes.io/docs/reference/kubectl/)
- [Debug Applications](https://kubernetes.io/docs/tasks/debug/debug-application/)

## CI: Kind descartável

O workflow `.github/workflows/kind-integration.yml` cria um Kind chamado `dev` e executa `scripts/ci-kind-smoke.sh`. O teste percorre 14 laboratórios sem addons (01.01–01.12, 02.02 e 02.04), valida os checks, experimenta rollout no lab 01.12 e rejeição por quota, e **remove os recursos declarados** ao terminar. Os namespaces são preservados até o runner descartável ser destruído.

Na falha, o script grava Pods, eventos, describes e logs em `/tmp/kvg-lab-reports`; o workflow publica o artefato `kind-lab-diagnostics`. Esse teste exige Docker, pull de imagens e rede disponível no GitHub runner.

Testes unitários do motor:
```bash
python3 -m unittest discover -s tests -p 'test_*.py' -v
```

A CI de Kind não substitui validação de labs de CNI, ingress controller, cloud providers ou storage que precisem de plugins e infraestrutura adicionais.
