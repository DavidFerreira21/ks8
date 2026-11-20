"""Regressoes da validacao semantica de manifests."""
from __future__ import annotations
import unittest
from scripts.validate_semantic_manifests import check_solution, validate


class SemanticManifestTests(unittest.TestCase):
    def test_all_fifty_two_contracts(self):
        self.assertEqual(validate(), [])

    def test_nodepool_cannot_provision_nodes(self):
        resource = {
            "apiVersion": "karpenter.sh/v1", "kind": "NodePool",
            "metadata": {"name": "estudo-sem-provisionar"},
            "spec": {"limits": {"nodes": 1}, "template": {"spec": {
                "nodeClassRef": {"kind": "EC2NodeClass", "name": "nao-configurada"}}}},
        }
        self.assertTrue(any("desarmado" in x for x in check_solution([resource], "04.05")))

    def test_servicemonitor_port_must_match_service(self):
        service = {"kind": "Service", "metadata": {"name": "demo", "labels": {"app": "demo"}},
                   "spec": {"selector": {"app": "demo"}, "ports": [{"name": "web", "port": 80}]}}
        monitor = {"kind": "ServiceMonitor", "metadata": {"name": "demo"},
                   "spec": {"selector": {"matchLabels": {"app": "demo"}},
                            "endpoints": [{"port": "metrics"}]}}
        self.assertTrue(any("endpoint.port" in x for x in check_solution([service, monitor], "04.07")))

    def test_controller_selectors(self):
        deploy = {"kind": "Deployment", "metadata": {"name": "x"},
                  "spec": {"selector": {"matchLabels": {"app": "a"}},
                           "template": {"metadata": {"labels": {"app": "b"}},
                                        "spec": {"containers": [{"image": "nginx"}]}}}}
        self.assertTrue(any("divergentes" in x for x in check_solution([deploy], "03.01")))


if __name__ == "__main__":
    unittest.main()
