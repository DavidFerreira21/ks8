"""Testa as proteções na exclusão de recursos globais do cluster."""
from __future__ import annotations

from pathlib import Path
import unittest
from unittest.mock import patch
from types import SimpleNamespace

from scripts import labctl



class CriticalLabSafetyTests(unittest.TestCase):
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


if __name__ == "__main__":
    unittest.main()
