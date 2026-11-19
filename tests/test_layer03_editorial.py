"""Contrato editorial da Camada 03: 17 aulas, labs e complementares opcionais."""
from __future__ import annotations

import re
import unittest
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
LAYER = ROOT / "trilhas" / "03-arquitetura"
SLUGS = ["arquitetura-cluster","kube-apiserver","etcd","admission-controllers","kube-controller-manager","crds-custom-resources","custom-controllers-operators","kube-scheduler","cloud-controller-manager","kubelet","container-runtime","cni-comunicacao","kube-proxy-ebpf","coredns","csi-storage","gateway-api","kustomize-helm"]
COMPLEMENT_INDICES = [1,2,5,6,11,12,14,15,16]
LINK_RE = re.compile(r"!?\[[^\]]+\]\(([^)]+)\)")


class Layer03EditorialTests(unittest.TestCase):
    def test_curriculum_and_navigation(self):
        index = (LAYER / "README.md").read_text(encoding="utf-8")
        self.assertEqual(len(re.findall(r"^\| 03\.\d{2} \|", index, re.M)), 17)
        for i, slug in enumerate(SLUGS, 1):
            with self.subTest(lesson=i):
                data = (LAYER / slug / "README.md").read_text(encoding="utf-8")
                self.assertTrue(data.startswith(f"# 03.{i:02d} ·"))
                for item in ("**Ao concluir esta aula, você será capaz de:**",
                             "## 🎨 Infográfico", "## 📖 Aula teórica",
                             "### Exemplo interpretado (trecho)",
                             "## 🧪 Aplicação prática", "## ✅ Revisão do aprendizado",
                             "## 🔗 Referências oficiais"):
                    self.assertIn(item, data)
                review = data.split("## ✅ Revisão do aprendizado", 1)[1].split("## 🔗 Referências oficiais", 1)[0]
                self.assertGreaterEqual(len(re.findall(r"^- .+\?", review, re.M)), 3)
                self.assertNotIn("Em preparação.", data)
                self.assertEqual("complementares/README.md" in data, i-1 in COMPLEMENT_INDICES)
                self.assertIn(f"[🧪 Lab 03.{i:02d}]", data)
                if i < 17:
                    self.assertIn(f"[Próxima: Aula 03.{i+1:02d}", data)
                if i > 1:
                    self.assertIn(f"[← Aula 03.{i-1:02d}", data)

    def test_labs_and_contracts(self):
        for i, slug in enumerate(SLUGS, 1):
            folder = LAYER / "labs" / f"{slug}-basico"
            with self.subTest(lab=i):
                text = (folder / "README.md").read_text(encoding="utf-8")
                self.assertTrue(text.startswith(f"# Lab 03.{i:02d}"))
                for item in ("## Objetivo e hipótese", "## Desafio — o que você vai construir",
                             "## Fase 3 — Experimento controlado",
                             "## Resultado esperado e evidências", "**Evidências específicas:**",
                             f"**Critério exclusivo 03.{i:02d}:**",
                             "## Critérios de conclusão", "## Perguntas de diagnóstico e reflexão",
                             "## Aprofunde seus conhecimentos",
                             f"make lab-prepare LAB=03.{i:02d}",
                             f"make lab-test LAB=03.{i:02d}",
                             f"make lab-down LAB=03.{i:02d}"):
                    self.assertIn(item, text)
                reflection = text.split("## Perguntas de diagnóstico e reflexão", 1)[1].split("## Aprofunde", 1)[0]
                self.assertGreaterEqual(len(re.findall(r"^- .+\?", reflection, re.M)), 3)
                meta = yaml.safe_load((folder / "lab.yaml").read_text(encoding="utf-8"))
                self.assertEqual(meta["id"], f"03.{i:02d}")
                self.assertEqual(meta["starter"], ["starter/resources.yaml"])
                self.assertEqual(meta["apply"], ["solution/resources.yaml"])
                self.assertTrue(meta.get("checks"))
                starter = (folder / meta["starter"][0]).read_text(encoding="utf-8")
                self.assertIn("TODO", starter)
                solution = list(yaml.safe_load_all((folder / meta["apply"][0]).read_text(encoding="utf-8")))
                self.assertTrue(all(isinstance(item, dict) and item.get("apiVersion") and item.get("kind") for item in solution))

    def test_all_relative_links_and_images_exist(self):
        pages = [LAYER / "README.md"]
        pages += [LAYER / slug / "README.md" for slug in SLUGS]
        pages += [LAYER / "labs" / f"{slug}-basico" / "README.md" for slug in SLUGS]
        pages += [LAYER / slug / "complementares" / "README.md"
                  for i, slug in enumerate(SLUGS) if i in COMPLEMENT_INDICES]
        for page in pages:
            data = page.read_text(encoding="utf-8")
            for target in LINK_RE.findall(data):
                if target.startswith(("https:", "http:", "mailto:", "#")):
                    continue
                path = target.split("#", 1)[0]
                if path:
                    with self.subTest(page=str(page.relative_to(ROOT)), target=path):
                        self.assertTrue((page.parent / path).exists(), f"broken link: {path}")


if __name__ == "__main__":
    unittest.main()
