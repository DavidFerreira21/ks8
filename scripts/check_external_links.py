#!/usr/bin/env python3
"""Revisão periódica de links externos, separada do check local do PR.

Somente HTTP 404/410 confirmados via GET reprovam o job. 401/403/429/5xx,
timeouts e bloqueios antibot são sinalizados para revisão, não inventados
como links quebrados. Não captura ou envia dados de usuários.
"""
from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
import re
import sys
from urllib.error import HTTPError, URLError
from urllib.parse import urldefrag
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
LINK = re.compile(r"!?(?:\[[^\]]*\])\((https?://[^\s)]+)\)")
FENCE = re.compile(r"^\s*(?:`{3,}|~{3,})")
HEADERS = {"User-Agent": "Kubernetes-Learning-Path-LinkCheck/1.0 (+GitHub Actions)"}


def collect(root: Path = ROOT) -> dict[str, list[str]]:
    found: dict[str, list[str]] = {}
    ignored = {".git", ".labs", ".venv", "node_modules", "__pycache__"}
    for file in sorted(root.rglob("*.md")):
        if any(part in ignored for part in file.relative_to(root).parts):
            continue
        fence = False
        for n, line in enumerate(file.read_text(encoding="utf-8").splitlines(), 1):
            if FENCE.match(line):
                fence = not fence
                continue
            if fence:
                continue
            for match in LINK.finditer(line):
                # Preserva URL completa salvo fragmentos, sem remover caminhos
                # usados em documentações oficiais.
                url, _ = urldefrag(match.group(1).strip("<>"))
                found.setdefault(url, []).append(f"{file.relative_to(root)}:{n}")
    return found


def probe(url: str, timeout: float = 10.0) -> tuple[str, str]:
    # HEAD é menos custoso, mas alguns servidores não aceitam. HTTP 404/410
    # é confirmado via GET; HTTP 403/429 pode ser bloqueio/rate-limit.
    def request(method: str) -> int:
        req = Request(url, method=method, headers=HEADERS)
        with urlopen(req, timeout=timeout) as response:
            return response.status

    try:
        status = request("HEAD")
        if 200 <= status < 400:
            return "ok", str(status)
    except HTTPError as exc:
        status = exc.code
        if status not in {404, 405, 410, 403, 429}:
            return "review", f"HTTP {status}"
    except (URLError, TimeoutError, OSError) as exc:
        return "review", type(exc).__name__
    try:
        status = request("GET")
        if status in {404, 410}:
            return "broken", f"HTTP {status}"
        return ("ok" if 200 <= status < 400 else "review"), f"HTTP {status}"
    except HTTPError as exc:
        if exc.code in {404, 410}:
            return "broken", f"HTTP {exc.code}"
        return "review", f"HTTP {exc.code}"
    except (URLError, TimeoutError, OSError) as exc:
        return "review", type(exc).__name__


def main() -> int:
    parser = argparse.ArgumentParser(description="Verificador periódico de links externos")
    parser.add_argument("--timeout", type=float, default=10.0)
    parser.add_argument("--workers", type=int, default=4)
    parser.add_argument("--strict", action="store_true", help="falha somente para 404/410 confirmados")
    parser.add_argument("--report", type=Path, default=Path("external-links-report.txt"))
    args = parser.parse_args()
    urls = collect()
    results = []
    with ThreadPoolExecutor(max_workers=max(1, min(8, args.workers))) as pool:
        futures = {pool.submit(probe, url, args.timeout): url for url in urls}
        for future in as_completed(futures):
            url = futures[future]
            status, detail = future.result()
            results.append((status, detail, url, urls[url]))
    results.sort(key=lambda x: ({"broken": 0, "review": 1, "ok": 2}[x[0]], x[2]))
    lines = [f"URLs únicas: {len(urls)}", "404/410 = quebrado; 403/429/5xx/timeout = revisar (não confirmado).", ""]
    for status, detail, url, places in results:
        lines.append(f"[{status.upper()}] {detail} {url}  ({'; '.join(places[:4])})")
    args.report.write_text("\n".join(lines) + "\n", encoding="utf-8")
    broken = sum(status == "broken" for status, _, _, _ in results)
    review = sum(status == "review" for status, _, _, _ in results)
    print(f"Links externos: {len(urls)} verificados, {broken} 404/410 confirmados, {review} para revisão.")
    print(f"Relatório: {args.report}")
    return 1 if args.strict and broken else 0


if __name__ == "__main__":
    sys.exit(main())
