#!/usr/bin/env python3
"""Materialize one honest evidence record for every INTERSPEECH paper."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
source = json.loads((HERE / "data/interspeech-2025-papers.json").read_text())
reviewed = {
    row["paper_id"] for row in json.loads((HERE / "data/interspeech-2025-representative-papers.json").read_text())["papers"]
}
reviewed.update(x["paper_id"] for x in json.loads((HERE / "data/interspeech-2025-fourth-d3-papers.json").read_text())["papers"])
reviewed.update(x["paper_id"] for x in json.loads((HERE / "data/interspeech-2025-fifth-d3-papers.json").read_text())["papers"])
reviewed.update(x["paper_id"] for x in json.loads((HERE / "data/interspeech-2025-sixth-d3-papers.json").read_text())["papers"])
reviewed.update(x["paper_id"] for x in json.loads((HERE / "data/interspeech-2025-seventh-d3-papers.json").read_text())["papers"])
reviewed.update(x["paper_id"] for x in json.loads((HERE / "data/interspeech-2025-eighth-d3-papers.json").read_text())["papers"])
reviewed.update(x["paper_id"] for x in json.loads((HERE / "data/interspeech-2025-ninth-d3-papers.json").read_text())["papers"])
reviewed.update(x["paper_id"] for x in json.loads((HERE / "data/interspeech-2025-tenth-d3-papers.json").read_text())["papers"])
reviewed.update(x["paper_id"] for x in json.loads((HERE / "data/interspeech-2025-eleventh-d3-papers.json").read_text())["papers"])
reviewed.update(x["paper_id"] for x in json.loads((HERE / "data/interspeech-2025-twelfth-d3-papers.json").read_text())["papers"])
reviewed.update(x["paper_id"] for x in json.loads((HERE / "data/interspeech-2025-thirteenth-d3-papers.json").read_text())["papers"])
reviewed.update(x["paper_id"] for x in json.loads((HERE / "data/interspeech-2025-fourteenth-d3-papers.json").read_text())["papers"])
reviewed.update(x["paper_id"] for x in json.loads((HERE / "data/interspeech-2025-fifteenth-d3-papers.json").read_text())["papers"])
reviewed.update(x["paper_id"] for x in json.loads((HERE / "data/interspeech-2025-sixteenth-d3-papers.json").read_text())["papers"])
reviewed.update(x["paper_id"] for x in json.loads((HERE / "data/interspeech-2025-seventeenth-d3-papers.json").read_text())["papers"])
reviewed.update(x["paper_id"] for x in json.loads((HERE / "data/interspeech-2025-eighteenth-d3-papers.json").read_text())["papers"])
reviewed.update(x["paper_id"] for x in json.loads((HERE / "data/interspeech-2025-nineteenth-d3-papers.json").read_text())["papers"])
reviewed.update(x["paper_id"] for x in json.loads((HERE / "data/interspeech-2025-twentieth-d3-papers.json").read_text())["papers"])
reviewed.update(x["paper_id"] for x in json.loads((HERE / "data/interspeech-2025-twentyfirst-d3-papers.json").read_text())["papers"])
reviewed.update(x["paper_id"] for x in json.loads((HERE / "data/interspeech-2025-twentisecond-d3-papers.json").read_text())["papers"])
reviewed.update(x["paper_id"] for x in json.loads((HERE / "data/interspeech-2025-twentythird-d3-papers.json").read_text())["papers"])
reviewed.update(x["paper_id"] for x in json.loads((HERE / "data/interspeech-2025-twentyfourth-d3-papers.json").read_text())["papers"])
reviewed.update(x["paper_id"] for x in json.loads((HERE / "data/interspeech-2025-twentyfifth-d3-papers.json").read_text())["papers"])
reviewed.update(x["paper_id"] for x in json.loads((HERE / "data/interspeech-2025-twentysixth-d3-papers.json").read_text())["papers"])
reviewed.update(x["paper_id"] for x in json.loads((HERE / "data/interspeech-2025-twentyseventh-d3-papers.json").read_text())["papers"])
reviewed.update(x["paper_id"] for x in json.loads((HERE / "data/interspeech-2025-twentyeighth-d3-papers.json").read_text())["papers"])
reviewed.update(x["paper_id"] for x in json.loads((HERE / "data/interspeech-2025-twentyninth-d3-papers.json").read_text())["papers"])
reviewed.update(x["paper_id"] for x in json.loads((HERE / "data/interspeech-2025-thirtieth-d3-papers.json").read_text())["papers"])
reviewed.update(x["paper_id"] for x in json.loads((HERE / "data/interspeech-2025-thirtyfirst-d3-papers.json").read_text())["papers"])
reviewed.update(x["paper_id"] for x in json.loads((HERE / "data/interspeech-2025-thirtysecond-d3-papers.json").read_text())["papers"])
reviewed.update(x["paper_id"] for x in json.loads((HERE / "data/interspeech-2025-thirtythird-d3-papers.json").read_text())["papers"])
reviewed.update(x["paper_id"] for x in json.loads((HERE / "data/interspeech-2025-thirtyfourth-d3-papers.json").read_text())["papers"])
reviewed.update(x["paper_id"] for x in json.loads((HERE / "data/interspeech-2025-thirtyfifth-d3-papers.json").read_text())["papers"])
reviewed.update(x["paper_id"] for x in json.loads((HERE / "data/interspeech-2025-thirtysixth-d3-papers.json").read_text())["papers"])
reviewed.update(x["paper_id"] for x in json.loads((HERE / "data/interspeech-2025-thirtyseventh-d3-papers.json").read_text())["papers"])
reviewed.update(x["paper_id"] for x in json.loads((HERE / "data/interspeech-2025-thirtyeighth-d3-papers.json").read_text())["papers"])
reviewed.update(x["paper_id"] for x in json.loads((HERE / "data/interspeech-2025-thirtyninth-d3-papers.json").read_text())["papers"])
reviewed.update(x["paper_id"] for x in json.loads((HERE / "data/interspeech-2025-fortieth-d3-papers.json").read_text())["papers"])
reviewed.update(x["paper_id"] for x in json.loads((HERE / "data/interspeech-2025-fortyfirst-d3-papers.json").read_text())["papers"])
reviewed.update(x["paper_id"] for x in json.loads((HERE / "data/interspeech-2025-fortysecond-d3-papers.json").read_text())["papers"])
reviewed.update(x["paper_id"] for x in json.loads((HERE / "data/interspeech-2025-fortythird-d3-papers.json").read_text())["papers"])
reviewed.update(x["paper_id"] for x in json.loads((HERE / "data/interspeech-2025-fortyfourth-d3-papers.json").read_text())["papers"])
reviewed.update(x["paper_id"] for x in json.loads((HERE / "data/interspeech-2025-fortyfifth-d3-papers.json").read_text())["papers"])
reviewed.update(x["paper_id"] for x in json.loads((HERE / "data/interspeech-2025-fortysixth-d3-papers.json").read_text())["papers"])
reviewed.update(x["paper_id"] for x in json.loads((HERE / "data/interspeech-2025-fortyseventh-d3-papers.json").read_text())["papers"])
reviewed.update(x["paper_id"] for x in json.loads((HERE / "data/interspeech-2025-fortyeighth-d3-papers.json").read_text())["papers"])
reviewed.update(x["paper_id"] for x in json.loads((HERE / "data/interspeech-2025-fortyninth-d3-papers.json").read_text())["papers"])
reviewed.update(x["paper_id"] for x in json.loads((HERE / "data/interspeech-2025-fiftieth-d3-papers.json").read_text())["papers"])
reviewed.update(x["paper_id"] for x in json.loads((HERE / "data/interspeech-2025-fiftyfirst-d3-papers.json").read_text())["papers"])
reviewed.update(x["paper_id"] for x in json.loads((HERE / "data/interspeech-2025-fiftysecond-d3-papers.json").read_text())["papers"])
reviewed.update(x["paper_id"] for x in json.loads((HERE / "data/interspeech-2025-fiftythird-d3-papers.json").read_text())["papers"])
reviewed.update(x["paper_id"] for x in json.loads((HERE / "data/interspeech-2025-fiftyfourth-d3-papers.json").read_text())["papers"])
reviewed.update(x["paper_id"] for x in json.loads((HERE / "data/interspeech-2025-fiftyfifth-d3-papers.json").read_text())["papers"])
reviewed.update(x["paper_id"] for x in json.loads((HERE / "data/interspeech-2025-fiftysixth-d3-papers.json").read_text())["papers"])
reviewed.update(x["paper_id"] for x in json.loads((HERE / "data/interspeech-2025-fiftyseventh-d3-papers.json").read_text())["papers"])
reviewed.update(x["paper_id"] for x in json.loads((HERE / "data/interspeech-2025-fiftyeighth-d3-papers.json").read_text())["papers"])
reviewed.update(x["paper_id"] for x in json.loads((HERE / "data/interspeech-2025-fiftyninth-d3-papers.json").read_text())["papers"])
reviewed.update(x["paper_id"] for x in json.loads((HERE / "data/interspeech-2025-sixtieth-d3-papers.json").read_text())["papers"])
reviewed.update(x["paper_id"] for x in json.loads((HERE / "data/interspeech-2025-sixtyfirst-d3-papers.json").read_text())["papers"])
reviewed.update(x["paper_id"] for x in json.loads((HERE / "data/interspeech-2025-sixtysecond-d3-papers.json").read_text())["papers"])
reviewed.update(x["paper_id"] for x in json.loads((HERE / "data/interspeech-2025-sixtythird-d3-papers.json").read_text())["papers"])
reviewed |= {
    row["paper_id"] for row in json.loads((HERE / "data/interspeech-2025-second-d3-papers.json").read_text())["papers"]
}
reviewed |= {
    row["paper_id"] for row in json.loads((HERE / "data/interspeech-2025-third-d3-papers.json").read_text())["papers"]
}
deep_rows = {
    row["paper_id"]: row
    for row in (
        json.loads(line)
        for line in (HERE / "data/interspeech-2025-deep-paper-analyses.jsonl").read_text().splitlines()
        if line.strip()
    )
}
evaluation_rows = {
    row["paper_id"]: row
    for row in (
        json.loads(line)
        for line in (HERE / "data/interspeech-2025-evaluation-audit.jsonl").read_text().splitlines()
        if line.strip()
    )
}

out = HERE / "data/interspeech-2025-paper-evidence.jsonl"
with out.open("w") as handle:
    for paper in source["papers"]:
        abstract = paper.get("abstract") or ""
        depth = "D3" if paper["paper_id"] in reviewed else "D2"
        record = {
            "paper_id": paper["paper_id"],
            "title": paper["title"],
            "authors": paper["authors"],
            "paper_url": paper["paper_url"],
            "pdf_url": paper["pdf_url"],
            "source": paper["source"],
            "source_page_sha256": paper.get("source_page_sha256"),
            "evidence_depth": depth,
            "abstract": abstract,
            "abstract_sha256": hashlib.sha256(abstract.encode()).hexdigest(),
            "conceptual_themes": paper.get("conceptual_themes", []),
            "full_paper_status": "reviewed-representative-set" if depth == "D3" else "queued-for-full-paper-review",
            "mechanism_claim_status": "captured-in-D3-notes" if depth == "D3" else "not-established-from-abstract",
            "artifact_execution_status": "not-attempted",
            "next_action": "use official PDF to extract mechanism, assumptions, evaluation, limitations, and artifact links" if depth == "D2" else "link structured D3 notes and inspect artifacts",
        }
        analysis = deep_rows[paper["paper_id"]]
        for field in ("bp", "wh", "naive", "ap", "mech", "math", "dots", "eval", "ww", "po", "limits", "source", "depth", "evidence_boundary"):
            record[field] = analysis[field]
        record["evaluation_audit"] = evaluation_rows[paper["paper_id"]]
        handle.write(json.dumps(record, ensure_ascii=False) + "\n")
print(f"wrote {out} ({len(source['papers'])} records)")
