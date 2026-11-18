"""Cobertura do catalogo de laboratorios da Camada 01."""
from pathlib import Path
import sys
import unittest

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import labctl
from validate_lab_resources import validate

EXPECTED_IDS = [f"01.{i:02d}" for i in range(1, 15)]

class FundamentalLabsTests(unittest.TestCase):
    def test_all_fourteen_labs_registered(self):
        labs = labctl.load_labs()
        self.assertEqual(sorted(x for x in labs if x.startswith("01.")), EXPECTED_IDS)

    def test_each_has_docs_checks_and_manifests(self):
        labs = labctl.load_labs()
        for identifier in EXPECTED_IDS:
            with self.subTest(lab=identifier):
                lab = labs[identifier]
                self.assertTrue((lab.directory / "README.md").is_file())
                self.assertTrue(lab.apply)
                self.assertTrue(lab.checks)
                for item in lab.apply:
                    self.assertTrue(item.is_file())

    def test_all_manifests_parse_and_match_namespaces(self):
        self.assertEqual(validate(), [])

    def test_advanced_labs_explain_addons(self):
        labs = labctl.load_labs()
        for identifier, term in (("01.13", "Traefik"), ("01.14", "Metrics Server")):
            with self.subTest(lab=identifier):
                self.assertIn(term, (labs[identifier].directory / "README.md").read_text(encoding="utf-8"))

    def test_undeclared_kind_is_rejected(self):
        self.assertNotIn("serviceaccount", {
            "daemonset", "statefulset", "ingress", "hpa", "secret", "namespace",
            "configmap", "service", "deployment", "pvc", "pod", "limitRange"
        })

if __name__ == "__main__":
    unittest.main()
