# Estudos Kubernetes (ks8)

Repositório dedicado aos meus estudos do curso **Kubernetes**. Aqui registro resumos das aulas, comandos úteis e ajustes no ambiente para poder revisar tudo de maneira rápida.

## Estrutura do repositório

- [Guia rápido de instalação do Kind no WSL](install-kind.md) — passo a passo para preparar o ambiente com Docker Desktop + WSL + Kind.
- [Aula 01 - Fundamentos e primeiros passos](aula-01/README.md) — anotações completas da primeira aula, cobrindo conceitos centrais e primeiros comandos.

Novas pastas serão adicionadas conforme eu avançar nas demais aulas do treinamento.

## Como utilizar

1. **Configure o ambiente** seguindo o guia do Kind para garantir que o cluster local está funcionando.
2. **Abra a aula desejada** pelo link no índice acima para revisar conteúdos e executar os exercícios.
3. **Execute os comandos** descritos em cada README diretamente no cluster Kind (makefile oferece atalhos como `make up`, `make nodes` e `make down`).

## Ambiente adotado

- Windows + WSL2 (Ubuntu) com Docker Desktop usando WSL Integration.
- `kind` configurado via `kind-config.yaml` para criar um cluster com um control-plane e dois workers.
- `kubectl` instalado localmente, com contexto `kind-dev` configurado após `make up`.

## Próximos passos

- Documentar as aulas seguintes do curso e incluir novos exemplos de manifests.
- Adicionar notas de troubleshooting e soluções para erros comuns.
- Registrar exercícios extras envolvendo ingress, serviços e objetos avançados.
