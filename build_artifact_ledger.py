#!/usr/bin/env python3
"""Extract and classify artifact links cited by the D3 representative papers."""

from __future__ import annotations

import json
import re
from pathlib import Path
from urllib.parse import urlparse

HERE = Path(__file__).resolve().parent
reps = json.loads((HERE / "data/interspeech-2025-representative-papers.json").read_text())["papers"]
reps += json.loads((HERE / "data/interspeech-2025-second-d3-papers.json").read_text())["papers"]
for d3_path in sorted((HERE / "data").glob("interspeech-2025-*-d3-papers.json")):
    reps += json.loads(d3_path.read_text())["papers"]
url_re = re.compile(r"https?://[^\s)\]>}\"]+")

def kind(url: str) -> str:
    host = urlparse(url).netloc.lower()
    if "github.com" in host or "gitlab.com" in host:
        return "code-or-repository"
    if "huggingface.co" in host or "modelscope.cn" in host:
        return "model-or-data-host"
    if "youtube.com" in host or "bilibili.com" in host or "github.io" in host:
        return "demo-or-media"
    if "arxiv.org" in host or "doi.org" in host:
        return "related-publication"
    return "dataset-or-external-resource"

rows = []
for paper in reps:
    text = (HERE / paper["full_text_path"]).read_text()
    seen = []
    for raw in url_re.findall(text):
        url = raw.rstrip(".,;:'")
        if url not in seen:
            seen.append(url)
            rows.append({
                "paper_id": paper["paper_id"],
                "title": paper["title"],
                "url": url,
                "artifact_kind": kind(url),
                "evidence_status": "cited-in-full-paper",
                "execution_status": "not-attempted",
                "boundary": "Link presence does not establish accessibility, completeness, license, or reproducibility.",
            })

out = HERE / "data/interspeech-2025-artifact-ledger.json"
out.write_text(json.dumps({
    "venue": "INTERSPEECH 2025",
    "method": "URLs extracted from captured representative full text; no execution implied",
    "papers_with_links": sorted({row["paper_id"] for row in rows}),
    "rows": rows,
}, indent=2, ensure_ascii=False) + "\n")
print(f"wrote {out} ({len(rows)} links across {len(set(row['paper_id'] for row in rows))} papers)")
