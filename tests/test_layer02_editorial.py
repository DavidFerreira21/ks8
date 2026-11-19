"""Regras editoriais da Camada 02: aulas, labs, complementares e links."""
from __future__ import annotations

import re
import unittest
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
LAYER = ROOT / "trilhas" / "02-operacao-seguranca"
LESSONS = [
    "labels-selectors-annotations", "rbac-serviceaccount",
    "securitycontext-pod-security", "resourcequota-limitrange",
    "init-sidecars", "jobs-cronjobs", "taints-tolerations-affinity",
    "topology-spread", "priorityclass-preemption", "qos-eviction",
    "pdb", "node-maintenance", "networkpolicy", "troubleshooting",
]
LABS = [
    "labels-selectors-basico", "rbac-minimo", "securitycontext-psa-basico",
    "quota-namespace", "init-sidecars-basico", "jobs-cronjobs-basico",
    "scheduling-basico", "topology-spread-basico", "priorityclass-basico",
    "qos-eviction-basico", "pdb-basico", "node-maintenance-basico",
    "networkpolicy-basico", "troubleshooting-basico",
]
COMPLEMENTS = (1, 2, 6, 9, 12, 13)  # índices zero-based
LINK_RE = re.compile(r"!?\[[^\]]+\]\(([^)]+)\)")


class Layer02EditorialTests(unittest.TestCase):
    def test_all_fourteen_lessons(self):
        for n, slug in enumerate(LESSONS, 1):
            page = LAYER / slug / "README.md"
            with self.subTest(id=n):
                data = page.read_text(encoding="utf-8")
                self.assertTrue(data.startswith(f"# 02.{n:02d} ·"))
                for required in (
                    "**Ao concluir esta aula, você será capaz de:**",
                    "## 🎨 Infográfico", "## 📖 Aula teórica",
                    "### Exemplo interpretado (trecho)",
                    "## 🧪 Aplicação prática", "## ✅ Revisão do aprendizado",
                    "## 🔗 Referências oficiais",
                ):
                    self.assertIn(required, data)
                review = data.split("## ✅ Revisão do aprendizado", 1)[1].split(
                    "## 🔗 Referências oficiais", 1
                )[0]
                self.assertGreaterEqual(len(re.findall(r"^- .+\?", review, re.M)), 3)
                self.assertNotIn("Em preparação.", data)
                self.assertNotIn("Qual problema este conceito resolve?", review)
                self.assertEqual("complementares/README.md" in data, n - 1 in COMPLEMENTS)

    def test_all_fourteen_student_labs(self):
        for n, slug in enumerate(LABS, 1):
            folder = LAYER / "labs" / slug
            with self.subTest(id=n):
                page = (folder / "README.md").read_text(encoding="utf-8")
                self.assertTrue(page.startswith(f"# Lab 02.{n:02d}"))
                for required in (
                    "## Objetivo e hipótese", "## Desafio — o que você vai construir",
                    "## Resultado esperado e evidências", "**Evidências específicas:**",
                    "## Critérios de conclusão", "## Perguntas de diagnóstico e reflexão",
                    "make lab-prepare LAB=02.", "make lab-test LAB=02.",
                    "make lab-down LAB=02.", "## Aprofunde seus conhecimentos",
                ):
                    self.assertIn(required, page)
                self.assertNotIn("**Evidências mínimas:**", page)
                self.assertIn(f"**Evidência funcional do Lab 02.{n:02d}:**", page)
                reflection = page.split("## Perguntas de diagnóstico e reflexão", 1)[1].split("## Aprofunde seus conhecimentos", 1)[0]
                self.assertGreaterEqual(len(re.findall(r"^- .+\\?", reflection, re.M)), 3)
                self.assertIn(f"[↑ Aula 02.{n:02d}]", page)
                meta = yaml.safe_load((folder / "lab.yaml").read_text(encoding="utf-8"))
                self.assertEqual(meta["id"], f"02.{n:02d}")
                self.assertEqual(meta["apply"], ["solution/resources.yaml"])
                self.assertEqual(meta["starter"], ["starter/resources.yaml"])
                self.assertTrue(meta.get("checks"), f"Lab 02.{n:02d} sem checks executáveis")
                starter = (folder / meta["starter"][0]).read_text(encoding="utf-8")
                self.assertIn("TODO", starter)
                solution = list(yaml.safe_load_all(
                    (folder / meta["apply"][0]).read_text(encoding="utf-8")
                ))
                self.assertTrue(solution)
                self.assertTrue(all(isinstance(x, dict) and x.get("kind") for x in solution))

    def test_experiment_manifests(self):
        cases = {
            "securitycontext-psa-basico": ("psa-incompativel.yaml", "Pod", "lab-02-03"),
            "topology-spread-basico": ("spread-impossivel.yaml", "Deployment", "lab-02-08"),
            "qos-eviction-basico": ("qos-parcial.yaml", "Pod", "lab-02-10"),
            "node-maintenance-basico": ("novo-pod.yaml", "Pod", "lab-02-12"),
        }
        for slug, (filename, kind, namespace) in cases.items():
            with self.subTest(lab=slug):
                path = LAYER / "labs" / slug / "experiments" / filename
                self.assertTrue(path.exists())
                data = yaml.safe_load(path.read_text(encoding="utf-8"))
                self.assertEqual(data["kind"], kind)
                self.assertEqual(data["metadata"]["namespace"], namespace)
        spread = yaml.safe_load(
            (LAYER / "labs" / "topology-spread-basico" / "experiments" / "spread-impossivel.yaml")
            .read_text(encoding="utf-8")
        )
        constraint = spread["spec"]["template"]["spec"]["topologySpreadConstraints"][0]
        self.assertEqual(constraint["minDomains"], 3)
        self.assertEqual(constraint["maxSkew"], 1)
        self.assertEqual(constraint["whenUnsatisfiable"], "DoNotSchedule")

    def test_lesson_navigation_and_lab_links(self):
        for i, (slug, lab) in enumerate(zip(LESSONS, LABS), start=1):
            page = (LAYER / slug / "README.md").read_text(encoding="utf-8")
            with self.subTest(lesson=i):
                self.assertIn(f"[🧪 Lab 02.{i:02d}](../labs/{lab}/README.md)", page)
                self.assertIn("[↑ Camada 02](../README.md)", page)
                if i < 14:
                    self.assertIn(f"[Próxima: Aula 02.{i+1:02d}", page)
                if i > 1:
                    self.assertIn(f"[← Aula 02.{i-1:02d}", page)

    def test_links_and_catalog(self):
        index = (LAYER / "README.md").read_text(encoding="utf-8")
        self.assertIn("| Aula | Conceito | Aula | Lab | Complementares |", index)
        self.assertEqual(len(re.findall(r"^\| 02\.\d{2} \|", index, re.M)), 14)
        pages = [LAYER / "README.md"]
        pages += [LAYER / s / "README.md" for s in LESSONS]
        pages += [LAYER / s / "complementares" / "README.md" for i, s in enumerate(LESSONS) if i in COMPLEMENTS]
        pages += [LAYER / "labs" / s / "README.md" for s in LABS]
        for page in pages:
            text = page.read_text(encoding="utf-8")
            for target in LINK_RE.findall(text):
                if target.startswith(("https:", "http:", "mailto:", "#")):
                    continue
                target = target.split("#", 1)[0]
                if target:
                    with self.subTest(page=str(page.relative_to(ROOT)), target=target):
                        self.assertTrue((page.parent / target).exists(), f"Broken link: {target}")


if __name__ == "__main__":
    unittest.main()
