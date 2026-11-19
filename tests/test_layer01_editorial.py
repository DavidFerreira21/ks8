"""Verificações editoriais para a camada-base de Kubernetes."""
from __future__ import annotations

import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LAYER = ROOT / "trilhas" / "01-fundamentos"

LESSONS = [
    "fundamentos", "pods", "deployments", "controladores", "services",
    "namespaces", "configmaps", "secrets", "requests-limits", "probes",
    "volumes", "estrategias-deployment", "ingress", "hpa",
]
LABS = [
    "fundamentos-cluster", "pods-basico", "deployments-basico",
    "controladores-basico", "services-basico", "namespaces-basico",
    "configmaps-basico", "secrets-basico", "requests-limits-basico",
    "probes-basico", "volumes-basico", "estrategias-deployment-basico",
    "ingress-basico", "hpa-basico",
]
LINK_RE = re.compile(r"!?(?:\[[^\]]+\])\(([^)]+)\)")


class Layer01EditorialTests(unittest.TestCase):
    def test_lesson_objectives_and_reviews(self):
        for index, slug in enumerate(LESSONS, start=1):
            path = LAYER / slug / "README.md"
            with self.subTest(lesson=slug):
                body = path.read_text(encoding="utf-8")
                self.assertTrue(body.startswith(f"# 01.{index:02d} ·"))
                self.assertIn("**Ao concluir esta aula, você será capaz de:**", body)
                self.assertIn("## 🎨 Infográfico", body)
                self.assertIn("## 🧪 Aplicação prática", body)
                self.assertIn("## ✅ Revisão do aprendizado", body)
                self.assertIn("## 🔗 Referências oficiais", body)
                review = body.split("## ✅ Revisão do aprendizado", 1)[1].split(
                    "## 🔗 Referências oficiais", 1
                )[0]
                self.assertGreaterEqual(len(re.findall(r"(?m)^- .+\?", review)), 3)
                self.assertNotIn("Qual problema este conceito resolve?", review)

    def test_lab_evidence_and_navigation(self):
        for index, slug in enumerate(LABS, start=1):
            path = LAYER / "labs" / slug / "README.md"
            with self.subTest(lab=slug):
                body = path.read_text(encoding="utf-8")
                self.assertTrue(body.startswith(f"# Lab 01.{index:02d}"))
                for required in (
                    "## Desafio — o que você vai construir",
                    "## Resultado esperado e evidências",
                    "## Critérios de conclusão",
                    "## Perguntas de diagnóstico e reflexão",
                    "**Evidências específicas:**",
                    "## Aprofunde seus conhecimentos",
                    "make lab-test LAB=01.",
                    "make lab-down LAB=01.",
                ):
                    self.assertIn(required, body)
                self.assertNotIn("**Evidências mínimas:**", body)
                section = body.split("**Evidências específicas:**", 1)[1].splitlines()[0]
                self.assertGreaterEqual(len(section.strip()), 75)

    def test_relative_links_in_layer_content(self):
        pages = [LAYER / "README.md", ROOT / "docs" / "padrao-editorial.md"]
        pages += [LAYER / slug / "README.md" for slug in LESSONS]
        pages += [LAYER / "labs" / slug / "README.md" for slug in LABS]
        for path in pages:
            body = path.read_text(encoding="utf-8")
            for target in LINK_RE.findall(body):
                if target.startswith(("http:", "https:", "mailto:", "#")):
                    continue
                target = target.split("#", 1)[0]
                if not target:
                    continue
                with self.subTest(path=str(path.relative_to(ROOT)), target=target):
                    self.assertTrue((path.parent / target).exists(), f"Link quebrado: {target}")

    def test_complementaries_are_actual_optional_material(self):
        body = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("## 📚 Materiais complementares", body)
        extras = body.split("## 📚 Materiais complementares", 1)[1].split(
            "## 🗺️ Como usar este repositório", 1
        )[0]
        self.assertNotIn("[Volumes — aula]", extras)
        self.assertNotIn("sem complementar específico", extras)
        self.assertNotIn("Anotações", extras)
        self.assertIn("complementares são opcionais", extras)

    def test_layer_index_has_distinct_columns(self):
        body = (LAYER / "README.md").read_text(encoding="utf-8")
        self.assertIn("| Aula | Conceito | Aula | Lab | Complementares |", body)
        self.assertEqual(len(re.findall(r"(?m)^\| 01\.\d{2} \|", body)), 14)
        self.assertNotIn("[Anotações]", body)


if __name__ == "__main__":
    unittest.main()
