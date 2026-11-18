#!/usr/bin/env python3
"""Verifica links locais Markdown, imagens e caminhos de navegação do repositório.

URLs externas não são consultadas; âncoras internas são ignoradas na resolução.
"""
from __future__ import annotations

from pathlib import Path
import re
import sys
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
LINK_RE = re.compile(r'!?\[[^\]]*\]\(([^)]+)\)')
FENCE_RE = re.compile(r'^\s*(`{3,}|~{3,})')


def local_targets(content: str):
    fenced = False
    for line_number, line in enumerate(content.splitlines(), start=1):
        if FENCE_RE.match(line):
            fenced = not fenced
            continue
        if fenced:
            continue
        for match in LINK_RE.finditer(line):
            raw = match.group(1).strip()
            if raw.startswith("<") and ">" in raw:
                raw = raw[1:raw.index(">")]
            else:
                raw = raw.split(' "', 1)[0].strip()
            if not raw or raw.startswith(("#", "/", "//")):
                continue
            if re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", raw):
                continue
            local = unquote(raw.split("#", 1)[0].split("?", 1)[0])
            if local:
                yield line_number, raw, local


def verify_links(root: Path = ROOT) -> list[str]:
    errors = []
    ignored_parts = {".git", ".labs", ".venv", "node_modules", "__pycache__"}
    for file in sorted(root.rglob("*.md")):
        if any(part in ignored_parts for part in file.relative_to(root).parts):
            continue
        text = file.read_text(encoding="utf-8")
        for line, raw, local in local_targets(text):
            target = (file.parent / local).resolve()
            if not target.is_relative_to(root.resolve()) or not target.exists():
                errors.append(f"{file.relative_to(root)}:{line}: link local inválido: {raw}")
    return errors


if __name__ == "__main__":
    failures = verify_links()
    if failures:
        print("\n".join(failures), file=sys.stderr)
        sys.exit(1)
    print("PASS: links relativos e imagens Markdown resolvem para arquivos existentes")
