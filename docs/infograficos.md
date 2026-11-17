# Convenção de infográficos — Kubernetes Visual Guide

[← Início](../README.md) · [Roadmap](roadmap.md)

A coleção visual terá **44 infográficos**, distribuídos nas quatro camadas da trilha. A criação dos PNGs ocorreu fora do repositório; **este PR não faz upload das imagens**.

## Identidade visual

- Fundo branco e faixa superior azul com título do conceito.
- Destaques amarelos, painéis em cores pastel e diagramas com traços ilustrados.
- Português brasileiro, preservando nomes de recursos Kubernetes em inglês.
- Uma imagem por conceito (ou conjunto estreitamente relacionado), com explicações breves e takeaway.

## Estrutura e nomes

Quando os PNGs estiverem revisados, salvar em um diretório `images/` ao lado do README de cada tema, com nomes previsíveis em letras minúsculas e hífens:

```text
trilhas/02-operacao-seguranca/rbac-serviceaccount/
├── README.md
└── images/
    └── rbac-serviceaccount.png
```

A mesma convenção se aplica às demais camadas. Não criar diretórios vazios: o Git não versiona pastas sem arquivos.

## Revisão antes de publicar

1. Conferir terminologia, acentos, diagramas, textos e exemplos técnicos.
2. Evitar representar como garantidas características dependentes de CNI/CSI ou provider.
3. Preferir resolução adequada à leitura em celular e imagem com tamanho otimizado.
4. Vincular o PNG no README do conceito usando caminho relativo.
5. Registrar a referência oficial junto ao material e revisar diferenças entre versões de Kubernetes.

**Status:** esquema definido, arquivos pendentes de upload e revisão.
