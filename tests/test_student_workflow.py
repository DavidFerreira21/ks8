"""Teste do modelo de aprendizado: aluno cria YAML, preparacao nao aplica solucao."""
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import labctl

class StudentWorkflowTests(unittest.TestCase):
    def test_prepare_creates_workspace_but_does_not_apply_solution(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            starter = root / "starter.yaml"
            solution = root / "solution.yaml"
            starter.write_text("kind: Pod\n# TODO\n", encoding="utf-8")
            solution.write_text("kind: Pod\n", encoding="utf-8")
            lab = labctl.Lab("01.02", "Pods", "lab-01-02", root,
                             (solution,), ({"type": "pod-ready", "name": "pod-demo"},),
                             (), (), (starter,))
            with patch.object(labctl, "ROOT", root), patch.object(labctl, "ensure_namespace", return_value=0), patch.object(labctl, "kubectl") as kubectl:
                self.assertEqual(labctl.prepare_lab(lab), 0)
                workspace_file = root / ".labs/01.02/starter.yaml"
                self.assertEqual(workspace_file.read_text(encoding="utf-8"), starter.read_text(encoding="utf-8"))
                kubectl.assert_not_called()
                workspace_file.write_text("meu trabalho", encoding="utf-8")
                self.assertEqual(labctl.prepare_lab(lab), 0)
                self.assertEqual(workspace_file.read_text(encoding="utf-8"), "meu trabalho")
                kubectl.assert_not_called()

    def test_compare_nested_resource_spec(self):
        actual = {"spec": {"replicas": 2, "selector": {"matchLabels": {"app": "demo"}},
                           "revisionHistoryLimit": 10}}
        expected = {"spec": {"replicas": 3, "selector": {"matchLabels": {"app": "demo"}}}}
        self.assertTrue(any("replicas" in item for item in labctl.expected_subset(actual, expected)))
        actual["spec"]["replicas"] = 3
        self.assertEqual(labctl.expected_subset(actual, expected), [])

    def test_all_fundamentals_have_starter_and_solution(self):
        labs = labctl.load_labs()
        for identifier in (f"01.{i:02d}" for i in range(1, 15)):
            with self.subTest(identifier=identifier):
                lab = labs[identifier]
                self.assertEqual(len(lab.starter), len(lab.apply))
                self.assertTrue(all("starter/" in str(x) for x in lab.starter))
                self.assertTrue(all("solution/" in str(x) for x in lab.apply))

if __name__ == "__main__":
    unittest.main()
