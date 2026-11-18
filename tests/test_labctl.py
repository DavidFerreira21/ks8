"""Testes locais sem Kind para o contrato e descoberta de labs."""
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import labctl


class LabRegistryTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.dir = self.root / "01-fundamentos" / "labs" / "demo"
        self.dir.mkdir(parents=True)
        (self.dir / "deployment.yaml").write_text("apiVersion: v1\nkind: ConfigMap\n", encoding="utf-8")
        self.metadata = self.dir / "lab.yaml"
        self.valid = (
            'id: "01.06"\n'
            'title: "Aula demo"\n'
            'namespace: aula-demo\n'
            'apply:\n  - deployment.yaml\n'
            'checks:\n  - type: service\n    name: web\n'
        )
        self.metadata.write_text(self.valid, encoding="utf-8")

    def load(self):
        with patch.object(labctl, "TRILHAS", self.root):
            return labctl.load_labs()

    def test_discovers_registered_lab(self):
        labs = self.load()
        self.assertEqual(list(labs), ["01.06"])
        self.assertEqual(labs["01.06"].namespace, "aula-demo")

    def test_rejects_path_traversal(self):
        self.metadata.write_text(self.valid.replace("deployment.yaml", "../other.yaml"), encoding="utf-8")
        with self.assertRaises(ValueError):
            self.load()

    def test_rejects_unknown_check(self):
        self.metadata.write_text(self.valid.replace("type: service", "type: arbitrary-shell"), encoding="utf-8")
        with self.assertRaises(ValueError):
            self.load()

    def test_rejects_duplicate_ids(self):
        other = self.root / "02-operacao-seguranca" / "labs" / "other"
        other.mkdir(parents=True)
        (other / "deployment.yaml").write_text("apiVersion: v1\nkind: ConfigMap\n", encoding="utf-8")
        (other / "lab.yaml").write_text(self.valid, encoding="utf-8")
        with self.assertRaises(ValueError):
            self.load()


if __name__ == "__main__":
    unittest.main()
