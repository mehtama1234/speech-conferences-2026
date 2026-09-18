#!/usr/bin/env python3
"""Ingest the official ISCA Archive metadata for INTERSPEECH 2025.

The archive exposes one HTML page per paper with citation metadata and an
abstract.  This script deliberately does not download PDFs: the paper page and
PDF URL are preserved as provenance, while the evidence depth of the abstract
is kept distinct from full-paper evidence.
"""

from __future__ import annotations

import html
import hashlib
import json
import re
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urljoin
from urllib.request import Request, urlopen


HERE = Path(__file__).resolve().parent
YEAR = "2025"
BASE = f"https://www.isca-archive.org/interspeech_{YEAR}/"
INDEX_URL = BASE
OUT = HERE / "data" / f"interspeech-{YEAR}-papers.json"


def fetch(url: str) -> bytes:
    last_error = None
    for attempt in range(3):
        try:
            req = Request(url, headers={"User-Agent": "speech-conferences-2026/1.0"})
            with urlopen(req, timeout=45) as response:
                return response.read()
        except Exception as exc:
            last_error = exc
            if attempt < 2:
                time.sleep(1.5 * (attempt + 1))
    raise last_error


def meta(page: str, name: str) -> list[str]:
    pattern = rf'<meta\s+name="{re.escape(name)}"\s+content="(.*?)"\s*/?>'
    return [html.unescape(x).strip() for x in re.findall(pattern, page, re.I | re.S)]


def abstract(page: str) -> str | None:
    match = re.search(r'<div\s+id="abstract"[^>]*>(.*?)</div>', page, re.I | re.S)
    if not match:
        return None
    text = re.sub(r"<[^>]+>", " ", match.group(1))
    text = re.sub(r"\s+", " ", html.unescape(text)).strip()
    return text or None


def paper_links(index: str) -> list[str]:
    links = re.findall(r'href="([^"]+_interspeech\.html)"', index, re.I)
    return sorted({urljoin(BASE, link) for link in links})


def parse(url: str) -> dict:
    try:
        raw_page = fetch(url)
        page = raw_page.decode("utf-8", "replace")
        title = meta(page, "citation_title")
        authors = meta(page, "citation_author")
        pdf = meta(page, "citation_pdf_url")
        doi = meta(page, "citation_doi")
        return {
            "paper_id": url.rsplit("/", 1)[-1].removesuffix(".html"),
            "title": title[0] if title else None,
            "authors": authors,
            "doi": doi[0] if doi else None,
            "abstract": abstract(page),
            "paper_url": url,
            "pdf_url": pdf[0] if pdf else None,
            "source": "official-isca-archive",
            "source_page_sha256": hashlib.sha256(raw_page).hexdigest(),
            "evidence_depth": "D2" if abstract(page) else "D1",
        }
    except Exception as exc:  # preserve source failure instead of silently dropping it
        return {
            "paper_id": url.rsplit("/", 1)[-1].removesuffix(".html"),
            "title": None,
            "authors": [],
            "doi": None,
            "abstract": None,
            "paper_url": url,
            "pdf_url": None,
            "source": "official-isca-archive",
            "source_page_sha256": None,
            "evidence_depth": "unavailable",
            "source_error": f"{type(exc).__name__}: {exc}",
        }


def main() -> int:
    started = time.time()
    raw_index = fetch(INDEX_URL)
    index = raw_index.decode("utf-8", "replace")
    links = paper_links(index)
    if not links:
        raise RuntimeError("official ISCA archive returned no paper links")

    papers: list[dict] = []
    with ThreadPoolExecutor(max_workers=12) as pool:
        futures = [pool.submit(parse, link) for link in links]
        for n, future in enumerate(as_completed(futures), 1):
            papers.append(future.result())
            if n % 100 == 0:
                print(f"  fetched {n}/{len(links)}", file=sys.stderr)

    papers.sort(key=lambda row: row["paper_id"])
    with_abstract = sum(bool(row["abstract"]) for row in papers)
    failed = sum(row["evidence_depth"] == "unavailable" for row in papers)
    payload = {
        "venue": "INTERSPEECH 2025",
        "archive": "ISCA Archive",
        "archive_url": INDEX_URL,
        "source_manifest": {
            "source_type": "official-proceedings-archive",
            "retrieved_at_utc": datetime.now(timezone.utc).isoformat(),
            "index_url": INDEX_URL,
            "index_sha256": hashlib.sha256(raw_index).hexdigest(),
            "paper_page_pattern": f"{BASE}<paper_id>.html",
            "pdfs_downloaded": False,
            "evidence_note": "Paper pages and abstracts are D2 evidence; full-paper mechanisms require PDF inspection.",
        },
        "n_papers": len(papers),
        "with_abstract": with_abstract,
        "without_abstract": len(papers) - with_abstract,
        "source_failures": failed,
        "papers": papers,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
    print(f"wrote {OUT}")
    print(f"papers: {len(papers)}  abstracts: {with_abstract}  failures: {failed}  seconds: {time.time()-started:.1f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
