#!/usr/bin/env python3
"""Check whether D3-cited artifact URLs are reachable; do not execute them."""

from __future__ import annotations

import json
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

HERE = Path(__file__).resolve().parent
ledger = json.loads((HERE / "data/interspeech-2025-artifact-ledger.json").read_text())
seen = set()
urls = []
for row in ledger["rows"]:
    if row["url"] not in seen:
        seen.add(row["url"])
        urls.append(row["url"])


def check(url: str) -> dict:
    result = {"url": url, "access_status": "unverified", "http_status": None, "error_class": None}
    try:
        request = Request(url, method="HEAD", headers={"User-Agent": "speech-conferences-2026/1.0"})
        with urlopen(request, timeout=5) as response:
            result["http_status"] = response.status
            result["access_status"] = "reachable"
    except HTTPError as exc:
        result["http_status"] = exc.code
        result["access_status"] = "http-error"
        result["error_class"] = "HTTPError"
    except (URLError, TimeoutError, ValueError) as exc:
        result["access_status"] = "unreachable-or-malformed"
        result["error_class"] = type(exc).__name__
    return result


with ThreadPoolExecutor(max_workers=32) as pool:
    results = list(pool.map(check, urls))

out = HERE / "data/interspeech-2025-artifact-access-audit.json"
out.write_text(json.dumps({
    "audit_type": "reachability-only",
    "audited_at_utc": datetime.now(timezone.utc).isoformat(),
    "execution_status": "not-attempted",
    "boundary": "Reachability does not establish code completeness, data access, license, reproducibility, or scientific validity.",
    "results": results,
}, indent=2, ensure_ascii=False) + "\n")
from collections import Counter
print(json.dumps({"url_count": len(results), "statuses": Counter(x["access_status"] for x in results), "output": str(out)}))
