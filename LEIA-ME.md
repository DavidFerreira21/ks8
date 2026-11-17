# Pacote de infográficos — Kubernetes Visual Guide (ks8)

Estrutura preparada para extrair **na raiz do repositório `ks8`**.

- **52 aulas** no catálogo oficial (14 + 14 + 17 + 7).
- **46 infográficos** correspondentes a aulas, em `trilhas/<camada>/<topico>/images/<topico>.png`.
- **18 arquivos PNG alternativos** em `imagens-alternativas/`, mantidos sem sobrescrever as imagens selecionadas. Algumas são versões anteriores ou composições de mais de um conceito.
- **6 aulas sem uma imagem específica localizada** (lista abaixo). Não foram usados arquivos de assunto diferente para preencher essas lacunas.

## Importante sobre integração com o GitHub

Este ZIP **não altera ou cria READMEs de aulas** nem manifests; apenas organiza as imagens e disponibiliza inventários CSV. Há diretórios com o nome semântico da aula, e nem todos têm README ainda. Os índices e a navegação devem continuar no PR #8 ou no commit que você fizer.

No diretório raiz do repositório:

```bash
unzip -o ks8-infograficos-52.zip
git status --short
git add trilhas/
git commit -m "docs(images): adicionar infograficos ao catalogo Kubernetes"
```

A pasta `imagens-alternativas/` é opcional para commit; se quiser manter o repositório enxuto, **não a adicione**.

## Aulas sem PNG específico

- 01.02 — Namespaces (`trilhas/01-fundamentos/namespaces/images/namespaces.png`)
- 01.06 — Deployments (`trilhas/01-fundamentos/deployments/images/deployments.png`)
- 01.10 — ConfigMaps (`trilhas/01-fundamentos/configmaps/images/configmaps.png`)
- 01.14 — Horizontal Pod Autoscaler (`trilhas/01-fundamentos/hpa/images/hpa.png`)
- 02.02 — RBAC e ServiceAccount (`trilhas/02-operacao-seguranca/rbac-serviceaccount/images/rbac-serviceaccount.png`)
- 02.13 — NetworkPolicy (`trilhas/02-operacao-seguranca/networkpolicy/images/networkpolicy.png`)

## Observações editoriais

Os 46 PNGs são as imagens disponíveis e associáveis aos temas; não foram auditados exaustivamente quanto à precisão técnica do texto dentro de cada ilustração. O material de `CRDs e Custom Resources` contém uma imagem intitulada sobre CRDs/Controllers; o tema `Custom Controllers e Operators` tem outra imagem específica de Operators. Revise esses títulos antes da publicação final.

Arquivo `inventario-52-aulas.csv`: mapeamento de código, título, imagem escolhida, origem e SHA-256.

Arquivo `imagens-alternativas.csv`: relação das variantes não selecionadas.
