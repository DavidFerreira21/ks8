"""Validação editorial da Camada 04: APIs reais, addons, YAML e navegação."""
from __future__ import annotations
import re
import unittest
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[1]
LAYER = ROOT / "trilhas" / "04-platform-engineering"
SLUGS = ["argo-cd","crossplane","kyverno","external-secrets-operator","karpenter","cilium","prometheus-grafana"]
LINK_RE = re.compile(r"!?\[[^\]]+\]\(([^)]+)\)")


class Layer04EditorialTests(unittest.TestCase):
    def test_seven_lessons_and_labs(self):
        catalog = (LAYER / "README.md").read_text(encoding="utf-8")
        curriculum = catalog.split("## 📚 Catálogo oficial da Camada 04", 1)[1].split("## 🧪 Como estudar", 1)[0]
        self.assertEqual(len(re.findall(r"^\| 04\.\d{2} \|", curriculum, re.M)), 7)
        for i, slug in enumerate(SLUGS, 1):
            with self.subTest(i=i):
                lesson = (LAYER / slug / "README.md").read_text(encoding="utf-8")
                self.assertTrue(lesson.startswith(f"# 04.{i:02d} ·"))
                for heading in ("**Ao concluir esta aula, você será capaz de:**",
                                "## 🎨 Infográfico", "## 📖 Aula teórica",
                                "### Exemplo interpretado (trecho)",
                                "## 🧪 Aplicação prática", "## ✅ Revisão do aprendizado",
                                "## 🔗 Referências oficiais"):
                    self.assertIn(heading, lesson)
                questions = lesson.split("## ✅ Revisão do aprendizado", 1)[1].split("## 🔗 Referências oficiais", 1)[0]
                self.assertGreaterEqual(len(re.findall(r"^- .+\?", questions, re.M)), 3)
                self.assertIn("complementares/README.md", lesson)
                self.assertNotIn("Em preparação.", lesson)
                labdir = LAYER / "labs" / f"{slug}-basico"
                lab = (labdir / "README.md").read_text(encoding="utf-8")
                for section in ("## Objetivo e hipótese", "## Desafio — o que você vai construir",
                                "## Fase 3 — Experimento controlado",
                                "## Resultado esperado e evidências", "**Evidências específicas:**",
                                f"**Critério exclusivo 04.{i:02d}:**",
                                "## Critérios de conclusão", "## Perguntas de diagnóstico e reflexão",
                                "## Aprofunde seus conhecimentos"):
                    self.assertIn(section, lab)
                meta = yaml.safe_load((labdir / "lab.yaml").read_text(encoding="utf-8"))
                self.assertEqual(meta["id"], f"04.{i:02d}")
                self.assertEqual(meta["apply"], ["solution/resources.yaml"])
                self.assertEqual(meta["starter"], ["starter/resources.yaml"])
                self.assertTrue(meta.get("checks"))
                starter = (labdir / "starter/resources.yaml").read_text(encoding="utf-8")
                self.assertIn("TODO", starter)
                solution = list(yaml.safe_load_all((labdir / "solution/resources.yaml").read_text(encoding="utf-8")))
                self.assertTrue(all(isinstance(x, dict) and x.get("kind") and x.get("apiVersion") for x in solution))
                comp = (LAYER / slug / "complementares" / "README.md").read_text(encoding="utf-8")
                self.assertIn("Leitura opcional", comp)

    def test_specific_api_contracts(self):
        def documents(slug):
            path = LAYER / "labs" / f"{slug}-basico" / "solution/resources.yaml"
            return list(yaml.safe_load_all(path.read_text(encoding="utf-8")))
        self.assertEqual(documents("argo-cd")[0]["kind"], "Application")
        self.assertEqual(documents("crossplane")[0]["apiVersion"], "apiextensions.crossplane.io/v2")
        self.assertEqual(documents("kyverno")[0]["kind"], "NamespacedValidatingPolicy")
        self.assertEqual(documents("external-secrets-operator")[0]["spec"]["provider"].keys(), {"fake"})
        self.assertEqual(documents("karpenter")[0]["spec"]["limits"]["nodes"], 0)
        self.assertEqual(documents("cilium")[-1]["kind"], "CiliumNetworkPolicy")
        self.assertEqual(documents("prometheus-grafana")[-1]["kind"], "ServiceMonitor")
        self.assertEqual(documents("prometheus-grafana")[-1]["spec"]["endpoints"][0]["port"], "metrics")

    def test_links_exist(self):
        pages = [LAYER / "README.md"]
        pages += [LAYER / slug / "README.md" for slug in SLUGS]
        pages += [LAYER / "labs" / f"{slug}-basico" / "README.md" for slug in SLUGS]
        pages += [LAYER / slug / "complementares" / "README.md" for slug in SLUGS]
        for page in pages:
            body = page.read_text(encoding="utf-8")
            for link in LINK_RE.findall(body):
                if link.startswith(("http:", "https:", "#", "mailto:")):
                    continue
                target = link.split("#", 1)[0]
                if target:
                    with self.subTest(page=str(page.relative_to(ROOT)), target=target):
                        self.assertTrue((page.parent / target).exists(), f"broken link: {target}")


if __name__ == "__main__":
    unittest.main()
