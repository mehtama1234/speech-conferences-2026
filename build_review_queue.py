#!/usr/bin/env python3
"""Materialize the remaining D2-to-D3 review queue."""

from __future__ import annotations

import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
papers = json.loads((HERE / "data/interspeech-2025-papers.json").read_text())["papers"]
reviewed = {
    row["paper_id"]
    for row in json.loads((HERE / "data/interspeech-2025-representative-papers.json").read_text())["papers"]
}
reviewed |= {
    row["paper_id"]
    for row in json.loads((HERE / "data/interspeech-2025-second-d3-papers.json").read_text())["papers"]
}
reviewed |= {
    row["paper_id"]
    for row in json.loads((HERE / "data/interspeech-2025-third-d3-papers.json").read_text())["papers"]
}
reviewed |= {
    row["paper_id"]
    for row in json.loads((HERE / "data/interspeech-2025-fourth-d3-papers.json").read_text())["papers"]
}
reviewed |= {
    row["paper_id"]
    for row in json.loads((HERE / "data/interspeech-2025-fifth-d3-papers.json").read_text())["papers"]
}
reviewed |= {
    row["paper_id"]
    for row in json.loads((HERE / "data/interspeech-2025-sixth-d3-papers.json").read_text())["papers"]
    + json.loads((HERE / "data/interspeech-2025-seventh-d3-papers.json").read_text())["papers"]
    + json.loads((HERE / "data/interspeech-2025-eighth-d3-papers.json").read_text())["papers"]
    + json.loads((HERE / "data/interspeech-2025-ninth-d3-papers.json").read_text())["papers"]
    + json.loads((HERE / "data/interspeech-2025-tenth-d3-papers.json").read_text())["papers"]
    + json.loads((HERE / "data/interspeech-2025-eleventh-d3-papers.json").read_text())["papers"]
    + json.loads((HERE / "data/interspeech-2025-twelfth-d3-papers.json").read_text())["papers"]
    + json.loads((HERE / "data/interspeech-2025-thirteenth-d3-papers.json").read_text())["papers"]
    + json.loads((HERE / "data/interspeech-2025-fourteenth-d3-papers.json").read_text())["papers"]
    + json.loads((HERE / "data/interspeech-2025-fifteenth-d3-papers.json").read_text())["papers"]
    + json.loads((HERE / "data/interspeech-2025-sixteenth-d3-papers.json").read_text())["papers"]
    + json.loads((HERE / "data/interspeech-2025-seventeenth-d3-papers.json").read_text())["papers"]
    + json.loads((HERE / "data/interspeech-2025-eighteenth-d3-papers.json").read_text())["papers"]
    + json.loads((HERE / "data/interspeech-2025-nineteenth-d3-papers.json").read_text())["papers"]
    + json.loads((HERE / "data/interspeech-2025-twentieth-d3-papers.json").read_text())["papers"]
    + json.loads((HERE / "data/interspeech-2025-twentyfirst-d3-papers.json").read_text())["papers"]
    + json.loads((HERE / "data/interspeech-2025-twentisecond-d3-papers.json").read_text())["papers"]
    + json.loads((HERE / "data/interspeech-2025-twentythird-d3-papers.json").read_text())["papers"]
    + json.loads((HERE / "data/interspeech-2025-twentyfourth-d3-papers.json").read_text())["papers"]
    + json.loads((HERE / "data/interspeech-2025-twentyfifth-d3-papers.json").read_text())["papers"]
    + json.loads((HERE / "data/interspeech-2025-twentysixth-d3-papers.json").read_text())["papers"]
    + json.loads((HERE / "data/interspeech-2025-twentyseventh-d3-papers.json").read_text())["papers"]
    + json.loads((HERE / "data/interspeech-2025-twentyeighth-d3-papers.json").read_text())["papers"]
    + json.loads((HERE / "data/interspeech-2025-twentyninth-d3-papers.json").read_text())["papers"]
    + json.loads((HERE / "data/interspeech-2025-thirtieth-d3-papers.json").read_text())["papers"]
    + json.loads((HERE / "data/interspeech-2025-thirtyfirst-d3-papers.json").read_text())["papers"]
    + json.loads((HERE / "data/interspeech-2025-thirtysecond-d3-papers.json").read_text())["papers"]
    + json.loads((HERE / "data/interspeech-2025-thirtythird-d3-papers.json").read_text())["papers"]
    + json.loads((HERE / "data/interspeech-2025-thirtyfourth-d3-papers.json").read_text())["papers"]
    + json.loads((HERE / "data/interspeech-2025-thirtyfifth-d3-papers.json").read_text())["papers"]
    + json.loads((HERE / "data/interspeech-2025-thirtysixth-d3-papers.json").read_text())["papers"]
    + json.loads((HERE / "data/interspeech-2025-thirtyseventh-d3-papers.json").read_text())["papers"]
    + json.loads((HERE / "data/interspeech-2025-thirtyeighth-d3-papers.json").read_text())["papers"]
    + json.loads((HERE / "data/interspeech-2025-thirtyninth-d3-papers.json").read_text())["papers"]
    + json.loads((HERE / "data/interspeech-2025-fortieth-d3-papers.json").read_text())["papers"]
    + json.loads((HERE / "data/interspeech-2025-fortyfirst-d3-papers.json").read_text())["papers"]
    + json.loads((HERE / "data/interspeech-2025-fortysecond-d3-papers.json").read_text())["papers"]
    + json.loads((HERE / "data/interspeech-2025-fortythird-d3-papers.json").read_text())["papers"]
    + json.loads((HERE / "data/interspeech-2025-fortyfourth-d3-papers.json").read_text())["papers"]
    + json.loads((HERE / "data/interspeech-2025-fortyfifth-d3-papers.json").read_text())["papers"]
    + json.loads((HERE / "data/interspeech-2025-fortysixth-d3-papers.json").read_text())["papers"]
    + json.loads((HERE / "data/interspeech-2025-fortyseventh-d3-papers.json").read_text())["papers"]
    + json.loads((HERE / "data/interspeech-2025-fortyeighth-d3-papers.json").read_text())["papers"]
    + json.loads((HERE / "data/interspeech-2025-fortyninth-d3-papers.json").read_text())["papers"]
    + json.loads((HERE / "data/interspeech-2025-fiftieth-d3-papers.json").read_text())["papers"]
    + json.loads((HERE / "data/interspeech-2025-fiftyfirst-d3-papers.json").read_text())["papers"]
    + json.loads((HERE / "data/interspeech-2025-fiftysecond-d3-papers.json").read_text())["papers"]
    + json.loads((HERE / "data/interspeech-2025-fiftythird-d3-papers.json").read_text())["papers"]
    + json.loads((HERE / "data/interspeech-2025-fiftyfourth-d3-papers.json").read_text())["papers"]
    + json.loads((HERE / "data/interspeech-2025-fiftyfifth-d3-papers.json").read_text())["papers"]
    + json.loads((HERE / "data/interspeech-2025-fiftysixth-d3-papers.json").read_text())["papers"]
    + json.loads((HERE / "data/interspeech-2025-fiftyseventh-d3-papers.json").read_text())["papers"]
    + json.loads((HERE / "data/interspeech-2025-fiftyeighth-d3-papers.json").read_text())["papers"]
    + json.loads((HERE / "data/interspeech-2025-fiftyninth-d3-papers.json").read_text())["papers"]
    + json.loads((HERE / "data/interspeech-2025-sixtieth-d3-papers.json").read_text())["papers"]
    + json.loads((HERE / "data/interspeech-2025-sixtyfirst-d3-papers.json").read_text())["papers"]
    + json.loads((HERE / "data/interspeech-2025-sixtysecond-d3-papers.json").read_text())["papers"]
    + json.loads((HERE / "data/interspeech-2025-sixtythird-d3-papers.json").read_text())["papers"]
}

queue = []
for paper in papers:
    if paper["paper_id"] in reviewed:
        continue
    themes = paper.get("conceptual_themes", [])
    priority = "high" if len(themes) >= 3 else "medium" if themes else "review-unmatched"
    queue.append({
        "paper_id": paper["paper_id"],
        "title": paper["title"],
        "paper_url": paper["paper_url"],
        "pdf_url": paper["pdf_url"],
        "current_themes": themes,
        "current_evidence_depth": paper["evidence_depth"],
        "review_status": "queued-for-full-paper-review",
        "priority": priority,
        "next_action": "inspect official PDF for mechanism, assumptions, evaluation, limitations, and artifact links",
    })

out = HERE / "data/interspeech-2025-review-queue.json"
out.write_text(json.dumps({
    "venue": "INTERSPEECH 2025",
    "queue_scope": "all papers not in the current D3 review set",
    "queue_count": len(queue),
    "unresolved_count": len(queue),
    "evidence_boundary": "D2 abstract-level records remain unresolved for full-paper mechanism claims",
    "rows": queue,
}, indent=2, ensure_ascii=False) + "\n")
print(f"wrote {out} ({len(queue)} queued papers)")
