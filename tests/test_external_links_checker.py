"""Testes de classificação do verificador de URLs sem acessar a rede."""
from __future__ import annotations
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
from urllib.error import HTTPError
from scripts.check_external_links import collect, probe


class LinkCheckerTests(unittest.TestCase):
    def test_deduplicates_and_ignores_fenced_links(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "README.md"
            path.write_text("""[a](https://docs.example.org/a#one)
[b](https://docs.example.org/a#two)
```markdown
[c](https://docs.example.org/fake)
```
""", encoding="utf-8")
            found = collect(Path(tmp))
            self.assertEqual(list(found), ["https://docs.example.org/a"])
            self.assertEqual(len(found["https://docs.example.org/a"]), 2)

    def test_404_confirmed_by_get(self):
        errors = [
            HTTPError("https://example.org/no", 404, "Not found", {}, None),
            HTTPError("https://example.org/no", 404, "Not found", {}, None),
        ]
        with patch("scripts.check_external_links.urlopen", side_effect=errors) as call:
            self.assertEqual(probe("https://example.org/no")[0], "broken")
            self.assertEqual(call.call_count, 2)

    def test_429_is_warning_not_broken(self):
        errors = [
            HTTPError("https://example.org", 429, "Rate limited", {}, None),
            HTTPError("https://example.org", 429, "Rate limited", {}, None),
        ]
        with patch("scripts.check_external_links.urlopen", side_effect=errors):
            self.assertEqual(probe("https://example.org")[0], "review")


if __name__ == "__main__":
    unittest.main()
