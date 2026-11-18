"""Contrato pedagógico de todos os laboratórios de Fundamentos (Camada 01).

O aluno prepara o namespace, escreve YAML, executa kubectl, observa, testa,
experimenta, diagnostica, limpa e pode aprofundar pela documentação oficial.
"""
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
LABS = (
    "fundamentos-cluster",
    "pods-basico",
    "deployments-basico",
    "controladores-basico",
    "services-basico",
    "namespaces-basico",
    "configmaps-basico",
    "secrets-basico",
    "requests-limits-basico",
    "probes-basico",
    "volumes-basico",
    "estrategias-deployment-basico",
    "ingress-basico",
    "hpa-basico",
)


class LabPedagogyTests(unittest.TestCase):
    def test_fourteen_labs_have_start_middle_end_and_further_reading(self):
        for index, slug in enumerate(LABS, 1):
            identifier = f"01.{index:02d}"
            path = ROOT / "trilhas/01-fundamentos/labs" / slug / "README.md"
            text = path.read_text(encoding="utf-8")
            with self.subTest(identifier=identifier):
                self.assertTrue(text.startswith(f"# Lab {identifier} — "))
                self.assertRegex(text, r"(?m)^## (Objetivo|Hipótese)")
                for section in (
                    "## Desafio — o que você vai construir",
                    "## Fase 1",
                    "## Resultado esperado e evidências",
                    "## Critérios de conclusão",
                    "## Aprofunde seus conhecimentos",
                ):
                    self.assertIn(section, text)
                self.assertIn("https://kubernetes.io/docs/", text)
                self.assertIn(f"make lab-test LAB={identifier}", text)
                self.assertIn(f"make lab-down LAB={identifier}", text)
                self.assertIn("kubectl", text)
                checklist = re.search(
                    r"## Critérios de conclusão\n\n((?:- \[ \].*\n)+)", text
                )
                self.assertIsNotNone(checklist)
                self.assertGreaterEqual(checklist.group(1).count("- [ ]"), 3)
                self.assertIn("README.md", text)

    def test_prepare_once_then_student_apply_and_validate(self):
        for index, slug in enumerate(LABS, 1):
            identifier = f"01.{index:02d}"
            text = (ROOT / "trilhas/01-fundamentos/labs" / slug / "README.md").read_text(encoding="utf-8")
            bash = "\n".join(re.findall(r"(?ms)^\\`\\`\\`bash\n(.*?)^\\`\\`\\`$", text))
            with self.subTest(identifier=identifier):
                prepare = f"make lab-prepare LAB={identifier}"
                self.assertEqual(bash.count(prepare), 1, "Preparar o lab deve acontecer somente uma vez")
                self.assertIn("kubectl apply -f .labs/", bash)
                self.assertIn(f"make lab-test LAB={identifier}", bash)
                self.assertLess(bash.index(prepare), bash.index("kubectl apply -f .labs/"))
                self.assertLess(bash.index("kubectl apply -f .labs/"), bash.index(f"make lab-test LAB={identifier}"))


if __name__ == "__main__":
    unittest.main()
