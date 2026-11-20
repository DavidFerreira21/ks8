"""Garante que links relativos e imagens de todo o currículo existam.

Inclui README de labs, exemplos avançados e guias de preparação, não somente
as aulas listadas no índice. Links externos são auditados pelo workflow semanal.
"""
from __future__ import annotations

from pathlib import Path
import re
import unittest
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
LINK = re.compile(r"!?(?:\\[[^\\]]*\\])\\(([^)]+)\\)")
FENCE = re.compile(r"^\\s*(?:`{3,}|~{3,})")


def curriculum_pages():
    pages = [ROOT / "README.md"]
    for directory in ("docs", "trilhas"):
        pages += sorted((ROOT / directory).rglob("*.md"))
    return [page for page in pages if page.exists()]


def broken_relative_links() -> list[str]:
    broken = []
    for page in curriculum_pages():
        fenced = False
        for index, line in enumerate(page.read_text(encoding="utf-8").splitlines(), 1):
            if FENCE.match(line):
                fenced = not fenced
                continue
            if fenced:
                continue
            for hit in LINK.finditer(line):
                url = hit.group(1).strip().strip("<>")
                if not url or url.startswith("#") or re.match(
                    r"^[a-z][a-z0-9+.-]*:", url, re.I
                ):
                    continue
                local = unquote(url.split("#", 1)[0].split("?", 1)[0])
                if not local:
                    continue
                path = (page.parent / local).resolve()
                if not path.is_relative_to(ROOT) or not path.exists():
                    broken.append(f"{page.relative_to(ROOT)}:{index} => {url}")
    return broken


class FullCurriculumLinkTests(unittest.TestCase):
    def test_every_relative_link_and_infographic(self):
        problems = broken_relative_links()
        self.assertFalse(problems, "\n".join(problems))


if __name__ == "__main__":
    unittest.main()
