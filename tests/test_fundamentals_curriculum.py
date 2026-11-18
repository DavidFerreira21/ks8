"""Evita inconsistencias entre o catalogo, paginas e labs da camada 01."""
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
LESSONS = (
    ("01.01", "Fundamentos Kubernetes", "fundamentos"),
    ("01.02", "Pods", "pods"),
    ("01.03", "Deployments", "deployments"),
    ("01.04", "ReplicaSet, DaemonSet e StatefulSet", "controladores"),
    ("01.05", "Services", "services"),
    ("01.06", "Namespaces", "namespaces"),
    ("01.07", "ConfigMaps", "configmaps"),
    ("01.08", "Secrets", "secrets"),
    ("01.09", "Requests e Limits", "requests-limits"),
    ("01.10", "Probes — Liveness, Readiness e Startup", "probes"),
    ("01.11", "Volumes", "volumes"),
    ("01.12", "Estratégias avançadas de Deployment", "estrategias-deployment"),
    ("01.13", "Ingress", "ingress"),
    ("01.14", "Horizontal Pod Autoscaler (HPA)", "hpa"),
)

class FundamentalsCurriculumTests(unittest.TestCase):
    def test_catalog_and_layer_have_same_sequence(self):
        catalog = (ROOT / "docs/catalogo.md").read_text(encoding="utf-8")
        layer = (ROOT / "trilhas/01-fundamentos/README.md").read_text(encoding="utf-8")
        catalog_ids = re.findall(r"^\| (01\.\d{2}) \|", catalog, flags=re.M)
        layer_ids = re.findall(r"^\| (01\.\d{2}) \|", layer, flags=re.M)
        expected = [item[0] for item in LESSONS]
        self.assertEqual(catalog_ids, expected)
        self.assertEqual(layer_ids, expected)

    def test_lesson_pages_and_next_navigation(self):
        for i, (identifier, title, slug) in enumerate(LESSONS):
            with self.subTest(identifier=identifier):
                content = (ROOT / "trilhas/01-fundamentos" / slug / "README.md").read_text(encoding="utf-8")
                self.assertTrue(content.startswith(f"# {identifier} · {title}"), slug)
                if i < len(LESSONS) - 1:
                    following = LESSONS[i + 1]
                    self.assertIn(f"[Próxima: {following[1]} →](../{following[2]}/README.md)", content)

    def test_lab_ids_are_aligned(self):
        fundamental = (ROOT / "trilhas/01-fundamentos/labs/fundamentos-cluster/lab.yaml").read_text(encoding="utf-8")
        services = (ROOT / "trilhas/01-fundamentos/labs/services-basico/lab.yaml").read_text(encoding="utf-8")
        self.assertIn('id: "01.01"', fundamental)
        self.assertIn('id: "01.05"', services)
        makefile = (ROOT / "Makefile").read_text(encoding="utf-8")
        self.assertIn("LAB ?= 01.01", makefile)

if __name__ == "__main__":
    unittest.main()
