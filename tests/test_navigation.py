"""Verifica links, rotulos e sequência didática de navegação da Camada 01."""
from pathlib import Path
import re
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from check_navigation import verify_links

LESSONS = (
    "fundamentos", "pods", "deployments", "controladores", "services",
    "namespaces", "configmaps", "secrets", "requests-limits", "probes",
    "volumes", "estrategias-deployment", "ingress", "hpa"
)
LABS = (
    "fundamentos-cluster", "pods-basico", "deployments-basico", "controladores-basico",
    "services-basico", "namespaces-basico", "configmaps-basico", "secrets-basico",
    "requests-limits-basico", "probes-basico", "volumes-basico",
    "estrategias-deployment-basico", "ingress-basico", "hpa-basico"
)


class NavigationTests(unittest.TestCase):
    def test_all_relative_links_exist(self):
        self.assertEqual(verify_links(ROOT), [])

    def test_link_checker_rejects_nonexistent_file(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / "index.md").write_text("[Lab 01.01](labs/missing/README.md)", encoding="utf-8")
            self.assertEqual(len(verify_links(root)), 1)

    def test_course_index_uses_uniform_lab_labels(self):
        index = (ROOT / "trilhas/01-fundamentos/README.md").read_text(encoding="utf-8")
        guide = (ROOT / "docs/labs.md").read_text(encoding="utf-8")
        for number, slug in enumerate(LABS, 1):
            identifier = f"01.{number:02d}"
            with self.subTest(identifier=identifier):
                self.assertIn(f"[🧪 Lab {identifier}](labs/{slug}/README.md)", index)
                self.assertIn(f"[🧪 Lab {identifier}](../trilhas/01-fundamentos/labs/{slug}/README.md)", guide)
        self.assertNotIn("Lab 01.05 — Services](", index)

    def test_lesson_back_next_and_lab_links(self):
        for i, (lesson, lab) in enumerate(zip(LESSONS, LABS)):
            identifier = f"01.{i + 1:02d}"
            path = ROOT / "trilhas/01-fundamentos" / lesson / "README.md"
            content = path.read_text(encoding="utf-8")
            with self.subTest(identifier=identifier):
                self.assertIn(f"[🧪 Lab {identifier}](../labs/{lab}/README.md)", content)
                self.assertIn("[↑ Camada 01](../README.md)", content)
                if i:
                    self.assertIn(f"[← Aula 01.{i:02d}", content)
                if i < len(LESSONS)-1:
                    self.assertIn(f"[Próxima: Aula 01.{i+2:02d}", content)

    def test_lab_back_next_and_lesson_links(self):
        for i, (lesson, slug) in enumerate(zip(LESSONS, LABS)):
            identifier = f"01.{i+1:02d}"
            path = ROOT / "trilhas/01-fundamentos/labs" / slug / "README.md"
            content = path.read_text(encoding="utf-8")
            with self.subTest(identifier=identifier):
                self.assertTrue(content.startswith(f"# Lab {identifier} — "))
                self.assertIn(f"[← Aula {identifier}](../../{lesson}/README.md)", content)
                self.assertIn("[🧪 Índice dos labs](../../../../docs/labs.md)", content)
                if i:
                    self.assertIn(f"[← Lab 01.{i:02d}](../{LABS[i-1]}/README.md)", content)
                if i < len(LABS)-1:
                    self.assertIn(f"[Próximo: Lab 01.{i+2:02d} →](../{LABS[i+1]}/README.md)", content)


if __name__ == "__main__":
    unittest.main()
