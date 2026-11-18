#!/usr/bin/env python3
"""Cria um esqueleto pedagógico sem publicar automaticamente um novo lab."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
LAYERS = {"01": "01-fundamentos", "02": "02-operacao-seguranca",
          "03": "03-arquitetura", "04": "04-platform-engineering"}
ID = re.compile(r"^(01|02|03|04)\.\d{2}$")
SLUG = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def scaffold(root: Path, identifier: str, slug: str, title: str) -> Path:
    if not ID.fullmatch(identifier):
        raise ValueError("ID inválido: use 01.15, 02.03 etc.")
    if not SLUG.fullmatch(slug) or len(slug) > 50:
        raise ValueError("Slug inválido: somente minúsculas, números e hífens")
    if not title.strip() or len(title) > 120:
        raise ValueError("Informe um título de 1 a 120 caracteres")
    layer = LAYERS[identifier[:2]]
    ns = "lab-" + identifier.replace(".", "-") + "-" + slug
    if len(ns) > 63:
        raise ValueError("Nome do namespace ficaria grande demais")
    lab_dir = root / "trilhas" / layer / "labs" / slug
    if lab_dir.exists():
        raise FileExistsError(f"Lab já existe: {lab_dir}")
    # Falha de validação deve ocorrer antes de criar qualquer diretório.
    (lab_dir / "manifests").mkdir(parents=True)
    (lab_dir / "tests").mkdir()
    contract = (
        f"id: {json.dumps(identifier)}\n"
        f"title: {json.dumps(title, ensure_ascii=False)}\n"
        f"namespace: {ns}\n"
        "apply:\n  - manifests/configmap.yaml\n"
        "checks:\n  - type: configmap\n    name: exemplo\n"
    )
    (lab_dir / "lab.yaml.example").write_text(contract, encoding="utf-8")
    manifest = (
        "apiVersion: v1\nkind: ConfigMap\nmetadata:\n"
        f"  name: exemplo\n  namespace: {ns}\n"
        "data:\n  objetivo: \"entender o ciclo do lab\"\n"
    )
    (lab_dir / "manifests" / "configmap.yaml").write_text(manifest, encoding="utf-8")
    readme = f"""# {identifier} · {title}

[↑ Índice dos laboratórios](../../../../docs/labs.md)

## Objetivo
Descreva a hipótese e o comportamento de Kubernetes que o aluno observará.

## Pré-requisitos
- Kind `dev`, contexto `kind-dev`.
- Não use clusters compartilhados.

## Etapas
1. **Preparar:** confirme contexto e namespace.
2. **Executar:** aplique o manifesto do lab.
3. **Observar:** verifique objeto, status e eventos.
4. **Experimentar:** proponha uma mudança ou falha controlada.
5. **Diagnosticar:** explique o resultado encontrado.
6. **Limpar:** exclua somente os recursos criados.

## Critérios de sucesso
- [ ] Descrever o comportamento esperado.
- [ ] Comparar estado desejado com estado observado.
- [ ] Identificar comandos de diagnóstico.
- [ ] Limpar os recursos do experimento.

## Publicação do lab
Revise o YAML, manifeste checks reais, valide os exercícios e **renomeie
`lab.yaml.example` para `lab.yaml`** somente quando estiver pronto para
aparecer em `make labs`.
"""
    (lab_dir / "README.md").write_text(readme, encoding="utf-8")
    (lab_dir / "tests" / "README.md").write_text(
        "# Verificações\n\nRegistre resultados esperados, comandos e evidências aqui.\n",
        encoding="utf-8",
    )
    return lab_dir


def main() -> int:
    parser = argparse.ArgumentParser(description="Gerador de esqueleto de laboratório")
    parser.add_argument("--id", required=True, help="Ex.: 01.10")
    parser.add_argument("--slug", required=True, help="Ex.: configmaps-variaveis")
    parser.add_argument("--title", required=True)
    args = parser.parse_args()
    try:
        path = scaffold(ROOT, args.id, args.slug, args.title)
    except (ValueError, FileExistsError) as exc:
        parser.error(str(exc))
    print(f"Lab criado: {path.relative_to(ROOT)}")
    print("Complete o README, revise os manifests e publique renomeando lab.yaml.example.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
