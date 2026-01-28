# Estudos Kubernetes (ks8)

Repositorio dedicado aos meus estudos do curso **Kubernetes**. Aqui registro resumos das aulas, comandos uteis e ajustes no ambiente para poder revisar tudo de maneira rapida.

## Estrutura do repositorio

- [Guia rapido de instalacao do Kind no WSL](install-kind.md) — passo a passo para preparar o ambiente com Docker Desktop + WSL + Kind.
- [Resumo](resume.md) — resumo geral dos objetos e conceitos vistos nos estudos.
- [Fundamentos](1-fundamentos/README.md) — conceitos centrais e primeiros comandos.
- [Pods](2-pod/README.md) — comandos para criar, inspecionar e diagnosticar Pods.
- [Deployment](3-deployment/README.md) — aplicacao, estrategias e rollout de Deployments.
- [ReplicaSet, DaemonSet e StatefulSet](4-replicaSet-daemonSet-statefulSet/README.md) — casos de uso e manifests.
- [Probes](5-probes/README.md) — liveness, readiness e startup probes.
- [Volumes](6-volumes/README.md) — StorageClass, PV, PVC e uso em Pods.
- [Services](7-services/README.md) — tipos de Service e exposicao de Pods.

## Como utilizar

1. **Configure o ambiente** seguindo o guia do Kind para garantir que o cluster local esta funcionando.
2. **Abra a aula desejada** pelo link no indice acima para revisar conteudos e executar os exercicios.
3. **Execute os comandos** descritos em cada README diretamente no cluster Kind (makefile oferece atalhos como `make up`, `make test`, `make install-nginx` e `make down`).

## Ambiente adotado

- Windows + WSL2 (Ubuntu) com Docker Desktop usando WSL Integration.
- `kind` configurado via `kind-config.yaml` para criar um cluster com um control-plane e dois workers.
- `kubectl` instalado localmente, com contexto `kind-dev` configurado apos `make up`.
