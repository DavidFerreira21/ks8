"""Testa as proteções de recursos globais e fluxo seguro do aluno."""
from __future__ import annotations

from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
from types import SimpleNamespace

from scripts import labctl


class CriticalLabSafetyTests(unittest.TestCase):
    def test_student_apply_rejects_global_without_annotation(self):
        base = Path(__file__).resolve().parents[1]
        metadata = base / "trilhas/02-operacao-seguranca/labs/priorityclass-basico"
        lab = labctl.Lab(
            "02.09", "PriorityClass", "lab-02-09", metadata,
            (metadata / "solution/resources.yaml",), (), (), (),
            (metadata / "starter/resources.yaml",),
        )
        with tempfile.TemporaryDirectory() as td:
            local_root = Path(td)
            ws = local_root / ".labs" / "02.09"
            ws.mkdir(parents=True)
            (ws / "resources.yaml").write_text(
                "apiVersion: scheduling.k8s.io/v1\n"
                "kind: PriorityClass\nmetadata:\n  name: lab-02-priority\n"
                "value: 1000\n", encoding="utf-8")
            with patch.object(labctl, "ROOT", local_root), \
                 patch.object(labctl, "kubectl") as kubectl:
                self.assertEqual(labctl.apply_student_lab(lab), 1)
                kubectl.assert_not_called()

    def test_student_apply_requires_explicit_namespace(self):
        base = Path(__file__).resolve().parents[1]
        metadata = base / "trilhas/03-arquitetura/labs/kube-apiserver-basico"
        lab = labctl.Lab("03.02", "API", "lab-03-02", metadata,
                         (metadata / "solution/resources.yaml",), (), (), (),
                         (metadata / "starter/resources.yaml",))
        with tempfile.TemporaryDirectory() as td:
            local_root = Path(td)
            ws = local_root / ".labs" / "03.02"
            ws.mkdir(parents=True)
            (ws / "resources.yaml").write_text(
                "apiVersion: v1\\nkind: ConfigMap\\nmetadata:\\n  name: demo\\n",
                encoding="utf-8")
            with patch.object(labctl, "ROOT", local_root), \
                 patch.object(labctl, "kubectl") as kubectl:
                self.assertEqual(labctl.apply_student_lab(lab), 1)
                kubectl.assert_not_called()

    def test_student_apply_rejects_cross_namespace(self):
        base = Path(__file__).resolve().parents[1]
        metadata = base / "trilhas/03-arquitetura/labs/kube-apiserver-basico"
        lab = labctl.Lab(
            "03.02", "API", "lab-03-02", metadata,
            (metadata / "solution/resources.yaml",), (), (), (),
            (metadata / "starter/resources.yaml",),
        )
        with tempfile.TemporaryDirectory() as td:
            local_root = Path(td)
            ws = local_root / ".labs" / "03.02"
            ws.mkdir(parents=True)
            (ws / "resources.yaml").write_text(
                "apiVersion: v1\nkind: ConfigMap\n"
                "metadata:\n  name: exemplo\n  namespace: default\n",
                encoding="utf-8")
            with patch.object(labctl, "ROOT", local_root), \
                 patch.object(labctl, "kubectl") as kubectl:
                self.assertEqual(labctl.apply_student_lab(lab), 1)
                kubectl.assert_not_called()

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
