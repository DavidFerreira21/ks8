"""Garante identidade editorial e pedagógica de todas as quatro camadas."""
from __future__ import annotations

from pathlib import Path
import unittest
import yaml

ROOT = Path(__file__).resolve().parents[1]
LAYERS = {
    "01": [
        "01-fundamentos",
        [
            "fundamentos",
            "pods",
            "deployments",
            "controladores",
            "services",
            "namespaces",
            "configmaps",
            "secrets",
            "requests-limits",
            "probes",
            "volumes",
            "estrategias-deployment",
            "ingress",
            "hpa"
        ],
        [
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
            "hpa-basico"
        ],
        [
            1,
            2,
            3,
            4,
            5,
            10
        ]
    ],
    "02": [
        "02-operacao-seguranca",
        [
            "labels-selectors-annotations",
            "rbac-serviceaccount",
            "securitycontext-pod-security",
            "resourcequota-limitrange",
            "init-sidecars",
            "jobs-cronjobs",
            "taints-tolerations-affinity",
            "topology-spread",
            "priorityclass-preemption",
            "qos-eviction",
            "pdb",
            "node-maintenance",
            "networkpolicy",
            "troubleshooting"
        ],
        [
            "labels-selectors-basico",
            "rbac-minimo",
            "securitycontext-psa-basico",
            "quota-namespace",
            "init-sidecars-basico",
            "jobs-cronjobs-basico",
            "scheduling-basico",
            "topology-spread-basico",
            "priorityclass-basico",
            "qos-eviction-basico",
            "pdb-basico",
            "node-maintenance-basico",
            "networkpolicy-basico",
            "troubleshooting-basico"
        ],
        [
            2,
            3,
            7,
            10,
            13,
            14
        ]
    ],
    "03": [
        "03-arquitetura",
        [
            "arquitetura-cluster",
            "kube-apiserver",
            "etcd",
            "admission-controllers",
            "kube-controller-manager",
            "crds-custom-resources",
            "custom-controllers-operators",
            "kube-scheduler",
            "cloud-controller-manager",
            "kubelet",
            "container-runtime",
            "cni-comunicacao",
            "kube-proxy-ebpf",
            "coredns",
            "csi-storage",
            "gateway-api",
            "kustomize-helm"
        ],
        [
            "arquitetura-cluster-basico",
            "kube-apiserver-basico",
            "etcd-basico",
            "admission-controllers-basico",
            "kube-controller-manager-basico",
            "crds-custom-resources-basico",
            "custom-controllers-operators-basico",
            "kube-scheduler-basico",
            "cloud-controller-manager-basico",
            "kubelet-basico",
            "container-runtime-basico",
            "cni-comunicacao-basico",
            "kube-proxy-ebpf-basico",
            "coredns-basico",
            "csi-storage-basico",
            "gateway-api-basico",
            "kustomize-helm-basico"
        ],
        [
            2,
            3,
            6,
            7,
            12,
            13,
            15,
            16,
            17
        ]
    ],
    "04": [
        "04-platform-engineering",
        [
            "argo-cd",
            "crossplane",
            "kyverno",
            "external-secrets-operator",
            "karpenter",
            "cilium",
            "prometheus-grafana"
        ],
        [
            "argo-cd-basico",
            "crossplane-basico",
            "kyverno-basico",
            "external-secrets-operator-basico",
            "karpenter-basico",
            "cilium-basico",
            "prometheus-grafana-basico"
        ],
        [
            1,
            2,
            3,
            4,
            5,
            6,
            7
        ]
    ]
}


class GlobalEditorialQualityTests(unittest.TestCase):
    def test_fifty_two_lessons_labs_and_twenty_eight_optional_references(self):
        lessons = labs = refs = 0
        for layer_id, (folder, lesson_slugs, lab_slugs, complement_indices) in LAYERS.items():
            root = ROOT / "trilhas" / folder
            self.assertEqual(len(lesson_slugs), len(lab_slugs))
            index = (root / "README.md").read_text(encoding="utf-8")
            for i, (slug, labslug) in enumerate(zip(lesson_slugs, lab_slugs), start=1):
                cid = f"{layer_id}.{i:02d}"
                with self.subTest(id=cid):
                    page = (root / slug / "README.md").read_text(encoding="utf-8")
                    lab = (root / "labs" / labslug / "README.md").read_text(encoding="utf-8")
                    self.assertTrue(page.startswith(f"# {cid} ·"))
                    self.assertTrue(lab.startswith(f"# Lab {cid}"))
                    self.assertIn("**Ao concluir esta aula, você será capaz de:**", page)
                    self.assertIn("## 📖 Aula teórica", page)
                    self.assertIn("## ✅ Revisão do aprendizado", page)
                    self.assertIn("## 🔗 Referências oficiais", page)
                    self.assertIn("## 🧪 Aplicação prática", page)
                    self.assertIn(f"[🧪 Lab {cid}]", page)
                    self.assertIn(f"Lab {cid}", index)
                    lesson_q = page.split("## ✅ Revisão do aprendizado", 1)[1].split("## 🔗 Referências oficiais", 1)[0]
                    self.assertGreaterEqual(sum(line.strip().startswith("- ") and "?" in line for line in lesson_q.splitlines()), 3)
                    self.assertIn("**Evidências específicas:**", lab)
                    self.assertIn("## Perguntas de diagnóstico e reflexão", lab)
                    lab_q = lab.split("## Perguntas de diagnóstico e reflexão", 1)[1].split("## Aprofunde seus conhecimentos", 1)[0]
                    self.assertGreaterEqual(sum(line.strip().startswith("- ") and "?" in line for line in lab_q.splitlines()), 3)
                    meta = yaml.safe_load((root / "labs" / labslug / "lab.yaml").read_text(encoding="utf-8"))
                    self.assertEqual(meta["id"], cid)
                    self.assertTrue(meta.get("checks"))
                    lessons += 1
                    labs += 1
                    comp = root / slug / "complementares" / "README.md"
                    self.assertEqual(comp.exists(), i in complement_indices)
                    self.assertEqual("complementares/README.md" in page, i in complement_indices)
                    if comp.exists():
                        self.assertIn("Leitura opcional", comp.read_text(encoding="utf-8"))
                        refs += 1
        self.assertEqual((lessons, labs, refs), (52, 52, 28))

    def test_legacy_complementaries_preserved(self):
        for folder in ("1-fundamentos", "2-pod", "3-deployment",
                       "4-replicaSet-daemonSet-statefulSet", "7-services", "5-probes"):
            self.assertTrue((ROOT / folder / "README.md").exists())

    def test_coverage_matrix_has_exactly_52_curricular_rows(self):
        matrix = (ROOT / "docs/matriz-homologacao.md").read_text(encoding="utf-8")
        rows = [line for line in matrix.splitlines() if line.startswith("| [0")]
        self.assertEqual(len(rows), 52)
        self.assertIn("39 labs", matrix)
        self.assertIn("13 cenários", matrix)

    def test_advanced_resources_have_coherent_dependencies(self):
        p = ROOT / "trilhas/04-platform-engineering/labs/crossplane-basico/examples/composition-avancada"
        composition = yaml.safe_load((p / "composition.yaml").read_text(encoding="utf-8"))
        xr = yaml.safe_load((p / "xr.yaml").read_text(encoding="utf-8"))
        function = yaml.safe_load((p / "function.yaml").read_text(encoding="utf-8"))
        self.assertEqual(composition["kind"], "Composition")
        self.assertEqual(composition["spec"]["mode"], "Pipeline")
        self.assertEqual(xr["spec"]["crossplane"]["compositionRef"]["name"],
                         composition["metadata"]["name"])
        self.assertEqual(composition["spec"]["pipeline"][0]["functionRef"]["name"],
                         function["metadata"]["name"])
        c = ROOT / "trilhas/03-arquitetura/labs/custom-controllers-operators-basico/examples/reconciler-real"
        compile((c / "controller.py").read_text(encoding="utf-8"), str(c / "controller.py"), "exec")
        storage = ROOT / "trilhas/03-arquitetura/labs/csi-storage-basico/experiments"
        sc = yaml.safe_load((storage / "csi-hostpath-storageclass.yaml").read_text(encoding="utf-8"))
        pvc = list(yaml.safe_load_all((storage / "csi-hostpath-pvc-pod.yaml").read_text(encoding="utf-8")))[0]
        self.assertEqual(sc["provisioner"], "hostpath.csi.k8s.io")
        self.assertEqual(pvc["spec"]["storageClassName"], sc["metadata"]["name"])
        cilium = yaml.safe_load((ROOT / "docs/ambientes/kind-cilium-config.yaml").read_text(encoding="utf-8"))
        self.assertTrue(cilium["networking"]["disableDefaultCNI"])


if __name__ == "__main__":
    unittest.main()
