# Jobs e CronJobs

[← Camada 02](../README.md) · [Roadmap](../../../docs/roadmap.md)

## O que você vai aprender

Job executa Pods até atingir a conclusão desejada; CronJob cria Jobs seguindo uma expressão cron.

## Como funciona

CronJob → Job → Pod(s); configure concurrencyPolicy, backoffLimit e histórico conforme a necessidade.

## Experimento recomendado

Crie Job simples, observe completions e logs; depois agende CronJob e inspecione os Jobs.

**Status do lab:** roteiro conceitual; manifests e validação prática serão adicionados em uma etapa posterior.

## O que observar

- Resultado e eventos dos recursos envolvidos.
- Diferença entre configuração desejada, decisão do Control Plane e resultado observado.
- Regras, condições e pré-requisitos particulares deste mecanismo.

## Infográfico

O infográfico correspondente foi criado na coleção visual, mas **a imagem PNG ainda não foi enviada ao repositório**. Após revisão técnica será incluída no diretório `images/` deste tópico.

## Referência oficial

- [Documentação Kubernetes — Jobs e CronJobs](https://kubernetes.io/docs/concepts/workloads/controllers/cron-jobs/)

**Próxima etapa:** [índice completo da Camada 02](../README.md).


---

### Navegação

[← Anterior](../rbac-serviceaccount/README.md) · [↑ Voltar à camada](../README.md) · [Próximo →](../networkpolicy/README.md)
