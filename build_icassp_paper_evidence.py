#!/usr/bin/env python3
"""Materialize honest first-principles records for every ICASSP record."""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = HERE / "data"
REPORTS = HERE / "reports"


def sentences(text: str) -> list[str]:
    return [x.strip() for x in re.split(r"(?<=[.!?])\s+", re.sub(r"\s+", " ", text or "").strip()) if x.strip()]


def pick(ss: list[str], patterns: list[str], default: str) -> str:
    for sentence in ss:
        if any(re.search(pattern, sentence, re.I) for pattern in patterns):
            return sentence
    return default


def main() -> None:
    source = json.loads((DATA / "icassp-2026-papers.json").read_text())
    queue = json.loads((DATA / "icassp-2026-semantic-review-queue.json").read_text())
    queue_by_id = {row["paper_id"]: row for row in queue["rows"]}
    rows = []
    for paper in source["papers"]:
        paper_id = paper["paperId"]
        abstract = paper.get("abstract") or ""
        depth = "D2" if abstract else "D1"
        ss = sentences(abstract)
        if depth == "D1":
            boundary = "D1 title-only boundary: the record does not establish the ordinary problem, mechanism, evaluation, limitations, or official proceedings details."
            bp = f"The title concerns: {paper['title']}. The underlying ordinary problem cannot be established from title-only evidence."
            unknown = "Title-only record; not established from available evidence."
            source_kind = "preserved Semantic Scholar discovery metadata"
        else:
            boundary = "D2 abstract boundary: the abstract does not establish full implementation, assumptions, ablations, failure cases, or independent reproduction."
            bp = ss[0] if ss else unknown
            unknown = "The abstract does not establish this detail."
            source_kind = "preserved Semantic Scholar discovery metadata with abstract"
        row = {
            "paper_id": paper_id,
            "title": paper["title"],
            "doi": paper.get("doi"),
            "paper_url": paper.get("url"),
            "source": source_kind,
            "depth": depth,
            "abstract_sha256": hashlib.sha256(abstract.encode()).hexdigest(),
            "evidence_boundary": boundary,
            "bp": bp,
            "wh": pick(ss, [r"however", r"challeng", r"difficult", r"limited", r"problem", r"lack"], unknown),
            "naive": pick(ss, [r"while", r"existing", r"current", r"although", r"prior", r"conventional"], unknown),
            "ap": pick(ss, [r"we (propose|present|introduce|develop)", r"this (paper|work)", r"our (method|approach|model)"], unknown),
            "mech": pick(ss, [r"using", r"based on", r"combine", r"condition", r"train", r"extract", r"predict"], unknown),
            "math": pick(ss, [r"loss", r"objective", r"metric", r"accuracy", r"error", r"embedding", r"frequency"], unknown),
            "eval": pick(ss, [r"evaluat", r"test", r"benchmark", r"dataset", r"accuracy", r"error", r"human"], unknown),
            "ww": pick(ss, [r"result", r"achiev", r"improv", r"outperform", r"find", r"show", r"yield"], unknown),
            "po": pick(ss, [r"enable", r"support", r"improv", r"robust", r"useful", r"application"], unknown),
            "limits": boundary,
        }
        qrow = queue_by_id.get(paper_id, {})
        row["dots"] = {
            "candidate_assignments": qrow.get("candidate_assignments", []),
            "review_state": qrow.get("review_state"),
            "decision": qrow.get("decision"),
        }
        rows.append(row)
    out = DATA / "icassp-2026-paper-evidence.jsonl"
    with out.open("w") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False) + "\n")
    report = REPORTS / "ICASSP_2026_PAPER_EVIDENCE.md"
    report.write_text("\n".join([
        "# ICASSP 2026 paper evidence",
        "",
        "Every captured ICASSP record now has a first-principles evidence record. D1 title-only and D2 abstract-backed evidence remain separate because the preserved source is discovery metadata, not official proceedings access.",
        "",
        f"- Records: {len(rows)}",
        f"- D1 title-only: {sum(x['depth'] == 'D1' for x in rows)}",
        f"- D2 abstract-backed: {sum(x['depth'] == 'D2' for x in rows)}",
        "",
        "Fields are intentionally conservative: missing problem, mechanism, evaluation, and limitation details are recorded as not established rather than inferred from model names or conference context.",
        "",
    ]) + "\n")
    print(json.dumps({"records": len(rows), "D1": sum(x["depth"] == "D1" for x in rows), "D2": sum(x["depth"] == "D2" for x in rows)}))


if __name__ == "__main__":
    main()
