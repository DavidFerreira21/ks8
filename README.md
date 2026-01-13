# Estudos Kubernetes (ks8)

Repositório dedicado aos meus estudos do curso **Kubernetes**. Aqui registro resumos das aulas, comandos úteis e ajustes no ambiente para poder revisar tudo de maneira rápida.

## Estrutura do repositório

- [Guia rápido de instalação do Kind no WSL](install-kind.md) — passo a passo para preparar o ambiente com Docker Desktop + WSL + Kind.
- [Resumo](resume.md) — resumo geral dos objetos e conceitos vistos nos estudos.
- [Fundamentos](aula-01/README.md) — anotações completas da primeira aula, cobrindo conceitos centrais e primeiros comandos.
- [Pod](2-pod/README.md) — comandos para criar, inspecionar e diagnosticar Pods.
- [Deployment](3-deployment/README.md) — aplicacao, estrategias e rollout de Deployments.
- [ReplicaSet,DaemonSet,Probs](4-replicaSet e daemonSet/README.md) — comandos e casos de uso de ReplicaSet e DaemonSet.


## Como utilizar

1. **Configure o ambiente** seguindo o guia do Kind para garantir que o cluster local está funcionando.
2. **Abra a aula desejada** pelo link no índice acima para revisar conteúdos e executar os exercícios.
3. **Execute os comandos** descritos em cada README diretamente no cluster Kind (makefile oferece atalhos como `make up`, `make test`, `make install-nginx` e `make down`).

## Ambiente adotado

- Windows + WSL2 (Ubuntu) com Docker Desktop usando WSL Integration.
- `kind` configurado via `kind-config.yaml` para criar um cluster com um control-plane e dois workers.
- `kubectl` instalado localmente, com contexto `kind-dev` configurado após `make up`.

