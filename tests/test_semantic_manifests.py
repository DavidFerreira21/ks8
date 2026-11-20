"""Regressoes da validacao semantica de manifests."""
from __future__ import annotations
import unittest
from scripts.validate_semantic_manifests import check_solution, validate


class SemanticManifestTests(unittest.TestCase):
    def test_all_forty_nine_contracts(self):
        self.assertEqual(validate(), [])

    def test_servicemonitor_port_must_match_service(self):
        service = {"kind": "Service", "metadata": {"name": "demo", "labels": {"app": "demo"}},
                   "spec": {"selector": {"app": "demo"}, "ports": [{"name": "web", "port": 80}]}}
        monitor = {"kind": "ServiceMonitor", "metadata": {"name": "demo"},
                   "spec": {"selector": {"matchLabels": {"app": "demo"}},
                            "endpoints": [{"port": "metrics"}]}}
        self.assertTrue(any("endpoint.port" in x for x in check_solution([service, monitor], "04.04")))

    def test_controller_selectors(self):
        deploy = {"kind": "Deployment", "metadata": {"name": "x"},
                  "spec": {"selector": {"matchLabels": {"app": "a"}},
                           "template": {"metadata": {"labels": {"app": "b"}},
                                        "spec": {"containers": [{"image": "nginx"}]}}}}
        self.assertTrue(any("divergentes" in x for x in check_solution([deploy], "03.01")))


if __name__ == "__main__":
    unittest.main()
