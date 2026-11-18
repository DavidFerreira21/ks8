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

    def test_services_lab_is_independent_and_service_focused(self):
        lab = labctl.load_labs()["01.05"]
        self.assertEqual(lab.namespace, "lab-01-05")
        self.assertEqual(lab.directory.name, "services-basico")
        self.assertEqual(lab.experiments, ())
        manifests = []
        for path in lab.apply:
            manifests.extend(yaml.safe_load_all(path.read_text(encoding="utf-8")))
        self.assertEqual({obj["kind"] for obj in manifests}, {"Deployment", "Service"})
        deployment = next(obj for obj in manifests if obj["kind"] == "Deployment")
        service = next(obj for obj in manifests if obj["kind"] == "Service")
        self.assertEqual(service["spec"]["selector"], deployment["spec"]["template"]["metadata"]["labels"])
        self.assertEqual(service["spec"]["type"], "ClusterIP")
        self.assertIn("EndpointSlices", (lab.directory / "README.md").read_text(encoding="utf-8"))

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
