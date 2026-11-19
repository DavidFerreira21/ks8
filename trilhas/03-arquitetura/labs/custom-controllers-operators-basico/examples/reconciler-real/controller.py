#!/usr/bin/env python3
"""Reconciler didático: AppEnvironment -> ConfigMap namespaced.

Sem framework externo: usa a API Kubernetes com ServiceAccount limitada.
Não utilizar em produção. Loop de polling para demonstrar idempotência.
"""
import json
import os
import ssl
import sys
import time
import urllib.error
import urllib.request

NAMESPACE = os.environ.get("LAB_NAMESPACE", "lab-03-07")
BASE = "https://kubernetes.default.svc"
SERVICE = "/var/run/secrets/kubernetes.io/serviceaccount"
TOKEN = open(SERVICE + "/token", encoding="utf-8").read().strip()
SSL = ssl.create_default_context(cafile=SERVICE + "/ca.crt")


def request(method, path, payload=None):
    body = None if payload is None else json.dumps(payload).encode("utf-8")
    headers = {"Authorization": "Bearer " + TOKEN}
    if payload is not None:
        headers["Content-Type"] = "application/apply-patch+yaml"
    req = urllib.request.Request(BASE + path, data=body, method=method, headers=headers)
    with urllib.request.urlopen(req, context=SSL, timeout=10) as response:
        return json.loads(response.read() or b"{}")


def reconcile():
    resources = request(
        "GET", "/apis/learning.example/v1/namespaces/" + NAMESPACE + "/appenvironments"
    ).get("items", [])
    for cr in resources:
        name = cr["metadata"]["name"]
        tier = cr.get("spec", {}).get("tier")
        if tier not in {"sandbox", "staging", "production"}:
            continue
        cm_name = "environment-" + name
        desired = {
            "apiVersion": "v1",
            "kind": "ConfigMap",
            "metadata": {
                "name": cm_name,
                "namespace": NAMESPACE,
                "labels": {"learning.example/owner": name},
                "ownerReferences": [{
                    "apiVersion": "learning.example/v1",
                    "kind": "AppEnvironment",
                    "name": name,
                    "uid": cr["metadata"]["uid"],
                }],
            },
            "data": {"tier": tier},
        }
        request(
            "PATCH",
            "/api/v1/namespaces/" + NAMESPACE + "/configmaps/" + cm_name
            + "?fieldManager=lab-03-07-reconciler&force=true",
            desired,
        )
        print(f"Reconciliado {name}: tier={tier}", flush=True)


def main():
    while True:
        try:
            reconcile()
        except (urllib.error.URLError, ValueError, KeyError, OSError) as exc:
            print(f"Reconcile failed: {exc}", file=sys.stderr, flush=True)
        time.sleep(5)


if __name__ == "__main__":
    main()
