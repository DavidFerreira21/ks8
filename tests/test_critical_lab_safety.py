"""Testa as proteções de recursos de cluster e NodePool offline."""
from __future__ import annotations

from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
from types import SimpleNamespace

from scripts.validate_karpenter_lab import validate
from scripts import labctl


VALID = """apiVersion: karpenter.sh/v1
kind: NodePool
metadata:
  name: estudo-sem-provisionar
spec:
  template:
    spec:
      nodeClassRef:
        group: karpenter.k8s.aws
        kind: EC2NodeClass
        name: nao-configurada
      requirements:
        - key: kubernetes.io/arch
          operator: In
          values: [amd64]
        - key: karpenter.sh/capacity-type
          operator: In
          values: [on-demand]
  limits:
    nodes: 0
"""


class CriticalLabSafetyTests(unittest.TestCase):
    def test_existing_unowned_crd_refuses_apply_and_delete(self):
        base = Path(__file__).resolve().parents[1]
        metadata = base / "trilhas/03-arquitetura/labs/crds-custom-resources-basico"
        lab = SimpleNamespace(identifier="03.06",
                              setup=(metadata / "setup/crd.yaml",), apply=())
        unowned = SimpleNamespace(returncode=0,
                                  stdout='{"metadata":{"annotations":{}}}',
                                  stderr="")
        with patch.object(labctl.subprocess, "run", return_value=unowned):
            self.assertEqual(labctl._check_global_resources_ownership(lab), 1)

    def test_owned_crd_can_be_reused(self):
        base = Path(__file__).resolve().parents[1]
        metadata = base / "trilhas/03-arquitetura/labs/crds-custom-resources-basico"
        lab = SimpleNamespace(identifier="03.06",
                              setup=(metadata / "setup/crd.yaml",), apply=())
        owned = SimpleNamespace(
            returncode=0,
            stdout='{"metadata":{"annotations":{"learning-path.example/lab-id":"03.06"}}}',
            stderr="",
        )
        with patch.object(labctl.subprocess, "run", return_value=owned):
            self.assertEqual(labctl._check_global_resources_ownership(lab), 0)

    def test_api_unavailable_fails_closed_for_global_objects(self):
        base = Path(__file__).resolve().parents[1]
        metadata = base / "trilhas/04-platform-engineering/labs/crossplane-basico"
        lab = SimpleNamespace(identifier="04.02", setup=(),
                              apply=(metadata / "solution/resources.yaml",))
        broken = SimpleNamespace(returncode=1, stdout="", stderr="forbidden")
        with patch.object(labctl.subprocess, "run", return_value=broken):
            self.assertEqual(labctl._check_global_resources_ownership(lab), 1)

    def test_karpenter_validates_student_yaml_not_reference(self):
        with tempfile.TemporaryDirectory() as td:
            file = Path(td) / "resources.yaml"
            file.write_text(VALID, encoding="utf-8")
            self.assertEqual(validate(file), [])
            file.write_text(VALID.replace("nodes: 0", "nodes: 1"), encoding="utf-8")
            self.assertTrue(any("SEGURANÇA" in x for x in validate(file)))
            file.write_text(VALID.replace("nao-configurada", "real-provider"), encoding="utf-8")
            self.assertTrue(any("NodeClass" in x for x in validate(file)))

    def test_crd_cleanup_rejects_any_remaining_instances(self):
        base = Path(__file__).resolve().parents[1]
        metadata = base / "trilhas/03-arquitetura/labs/crds-custom-resources-basico"
        lab = SimpleNamespace(setup=(metadata / "setup/crd.yaml",), apply=())
        remaining = SimpleNamespace(returncode=0, stdout='{"items": [{"metadata": {"namespace": "other", "name": "keep"}}]}', stderr="")
        with patch.object(labctl.subprocess, "run", return_value=remaining) as run:
            self.assertEqual(labctl._verify_global_api_deletion_safety(lab), 1)
            self.assertTrue(any("-A" in call.args[0] for call in run.call_args_list))

    def test_crd_cleanup_allows_empty_instance_list(self):
        base = Path(__file__).resolve().parents[1]
        metadata = base / "trilhas/03-arquitetura/labs/crds-custom-resources-basico"
        lab = SimpleNamespace(setup=(metadata / "setup/crd.yaml",), apply=())
        empty = SimpleNamespace(returncode=0, stdout='{"items": []}', stderr="")
        with patch.object(labctl.subprocess, "run", return_value=empty):
            self.assertEqual(labctl._verify_global_api_deletion_safety(lab), 0)

    def test_xrd_cleanup_rejects_remaining_xrs(self):
        base = Path(__file__).resolve().parents[1]
        metadata = base / "trilhas/04-platform-engineering/labs/crossplane-basico"
        lab = SimpleNamespace(setup=(), apply=(metadata / "solution/resources.yaml",))
        remaining = SimpleNamespace(returncode=0, stdout='{"items": [{"metadata": {"namespace": "lab-04-02", "name": "still-here"}}]}', stderr="")
        with patch.object(labctl.subprocess, "run", return_value=remaining):
            self.assertEqual(labctl._verify_global_api_deletion_safety(lab), 1)


if __name__ == "__main__":
    unittest.main()
