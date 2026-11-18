"""Testes de scaffold sem modificar o repositório real."""
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from new_lab import scaffold


class NewLabTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)

    def test_creates_unpublished_lab(self):
        lab = scaffold(self.root, "01.10", "configmaps-basico", "ConfigMap básico")
        self.assertTrue((lab / "README.md").exists())
        self.assertTrue((lab / "manifests" / "configmap.yaml").exists())
        self.assertTrue((lab / "lab.yaml.example").exists())
        self.assertFalse((lab / "lab.yaml").exists())

    def test_never_overwrites_existing_lab(self):
        scaffold(self.root, "01.10", "configmaps-basico", "ConfigMap básico")
        with self.assertRaises(FileExistsError):
            scaffold(self.root, "01.10", "configmaps-basico", "Outro")

    def test_rejects_unsafe_slug(self):
        with self.assertRaises(ValueError):
            scaffold(self.root, "01.10", "../../other", "Unsafe")
        self.assertFalse((self.root / "trilhas").exists())

    def test_rejects_invalid_id(self):
        with self.assertRaises(ValueError):
            scaffold(self.root, "99.99", "demo", "No")
        self.assertFalse((self.root / "trilhas").exists())


if __name__ == "__main__":
    unittest.main()
