#!/usr/bin/env python3
"""Materialize first-principles paper records at the evidence actually available.

D2 records are structured abstract readings: they never invent a full-paper
mechanism or limitation. D3 records inherit the analyst's structured notes and
add the missing evaluation/source fields. This makes the depth boundary
machine-checkable instead of hiding it in prose.
"""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

try:
    import fitz
except ImportError:  # pragma: no cover - the bounded build can retain manifest metadata
    fitz = None

HERE = Path(__file__).resolve().parent
DATA = HERE / "data"
REPORTS = HERE / "reports"


def sentences(text: str) -> list[str]:
    text = re.sub(r"\s+", " ", text or "").strip()
    return [x.strip() for x in re.split(r"(?<=[.!?])\s+", text) if x.strip()]


def pick(ss: list[str], patterns: list[str], default: str) -> str:
    for sentence in ss:
        if any(re.search(pattern, sentence, re.I) for pattern in patterns):
            return sentence
    return default


def source_location(capture: dict, paper_id: str) -> dict:
    pdf_path = HERE / "data" / "interspeech-2025-pdfs" / f"{paper_id}.pdf"
    text_path = HERE / capture.get("full_text_path", f"data/interspeech-2025-text/{paper_id}.txt")
    page_count = capture.get("page_count")
    if page_count is None and fitz is not None and pdf_path.exists():
        try:
            with fitz.open(pdf_path) as document:
                page_count = len(document)
        except Exception:
            page_count = None
    section_index = []
    if text_path.exists():
        try:
            for line_number, raw in enumerate(text_path.read_text(errors="replace").splitlines(), 1):
                line = re.sub(r"\s+", " ", raw).strip()
                if not line or len(line) > 120:
                    continue
                normalized = re.sub(r"^(?:\d+(?:\.\d+)*[.)]?\s+)", "", line).strip().lower()
                is_heading = (
                    bool(re.match(r"^\d+(?:\.\d+)*[.)]?\s+[A-Z]", line))
                    or normalized in {"abstract", "introduction", "related work", "method", "methods", "experiments", "results", "discussion", "conclusion", "limitations", "acknowledgments", "references"}
                    or (line.isupper() and 3 <= len(line.split()) <= 10)
                )
                if is_heading and not any(item["line"] == line_number for item in section_index):
                    section_index.append({"heading": line, "line": line_number})
            section_index = section_index[:40]
        except OSError:
            section_index = []
    return {
        "pdf_path": str(pdf_path.relative_to(HERE)),
        "text_path": str(text_path.relative_to(HERE)),
        "pdf_page_range": f"1-{page_count}" if page_count else "not-established",
        "page_count": page_count,
        "section_index": section_index,
        "claim_location_granularity": "paper-level captured source; claim-specific page/section mapping is not independently established",
    }


def abstract_record(paper: dict, depth: str, d3: dict | None, captures: dict | None = None) -> dict:
    abstract = paper.get("abstract") or ""
    ss = sentences(abstract)
    boundary = "Abstract-only boundary: the abstract does not establish the full implementation, assumptions, ablations, failure cases, or independent reproduction."
    bp = ss[0] if ss else "The abstract does not state the ordinary problem clearly enough for a bounded first-principles account."
    wh = pick(ss, [r"however", r"challeng", r"difficult", r"limited", r"remain", r"problem", r"variab", r"lack"], "The abstract does not identify why the problem is difficult beyond naming the task.")
    naive = pick(ss, [r"while", r"existing", r"current", r"although", r"prior", r"conventional"], "The abstract does not state a natural first attempt or its failure; this cannot be inferred safely from the title.")
    ap = pick(ss, [r"we (propose|present|introduce|develop)", r"this (paper|study)", r"our (method|approach|system|model)"], "The abstract does not state a central conceptual move clearly enough for a bounded account.")
    mech = pick(ss, [r"using", r"based on", r"combine", r"consist", r"condition", r"train", r"fine-tun", r"extract", r"predict"], ap)
    math = pick(ss, [r"loss", r"objective", r"metric", r"accuracy", r"error", r"WER", r"F1", r"RMSE", r"SNR", r"probab", r"embedding"], "The abstract does not specify a mathematical object or decision rule.")
    evaluation = pick(ss, [r"evaluat", r"test", r"benchmark", r"dataset", r"corpus", r"accuracy", r"error", r"WER", r"F1", r"RMSE", r"MOS", r"human"], "The abstract does not specify enough evaluation detail to identify the denominator or target.")
    reported = pick(ss, [r"result", r"achiev", r"improv", r"outperform", r"find", r"show", r"yield", r"increase", r"decreas"], "The abstract does not state a paper-reported result clearly enough to summarize.")
    payoff = pick(ss, [r"enable", r"support", r"improv", r"robust", r"useful", r"benefit", r"application", r"contribut"], "The abstract does not establish a practical payoff beyond the reported task result.")
    record = {
        "paper_id": paper["paper_id"],
        "title": paper["title"],
        "paper_url": paper["paper_url"],
        "pdf_url": paper["pdf_url"],
        "source_page_sha256": paper.get("source_page_sha256"),
        "abstract_sha256": hashlib.sha256(abstract.encode()).hexdigest(),
        "depth": depth,
        "evidence_boundary": "D3 full-paper note" if depth == "D3" else boundary,
        "bp": bp,
        "wh": wh,
        "naive": naive,
        "ap": ap,
        "mech": mech,
        "math": math,
        "eval": evaluation,
        "ww": reported,
        "po": payoff,
        "limits": boundary,
        "dots": {"themes": paper.get("conceptual_themes", []), "status": "abstract-linked; conceptual links require semantic review"},
        "source": {"kind": "official-isca-archive-paper-page-and-abstract", "abstract_present": bool(abstract)},
    }
    if d3:
        for field in ("bp", "wh", "naive", "ap", "mech", "math", "dots", "ww", "limits"):
            if field in d3:
                record[field] = d3[field]
        record["eval"] = evaluation
        record["po"] = "The paper reports the following payoff at D3 depth: " + d3.get("ww", "")
        record["evidence_boundary"] = "D3 structured analyst note backed by captured PDF/text; result remains author-reported and was not independently reproduced."
        capture = (captures or {}).get(paper["paper_id"], {})
        record["source"] = {
            "kind": "official-isca-archive-paper-page-plus-captured-pdf-text",
            "pdf_sha256": capture.get("pdf_sha256"),
            "full_text_sha256": capture.get("full_text_sha256"),
            "page_count": capture.get("page_count"),
            "full_text_chars": capture.get("full_text_chars"),
            "pdf_path": f"data/interspeech-2025-pdfs/{paper['paper_id']}.pdf",
            "text_path": capture.get("full_text_path", f"data/interspeech-2025-text/{paper['paper_id']}.txt"),
            "location": source_location(capture, paper["paper_id"]),
        }
        record["full_paper_evidence"] = {
            "pdf_sha256": capture.get("pdf_sha256"),
            "full_text_sha256": capture.get("full_text_sha256"),
            "page_count": capture.get("page_count"),
            "source_note": "Structured D3 fields are analyst notes grounded in the captured PDF/text; results remain author-reported and are not independent reproduction.",
            "source_location": source_location(capture, paper["paper_id"]),
        }
    return record


def main() -> None:
    source = json.loads((DATA / "interspeech-2025-papers.json").read_text())
    taxonomy = json.loads((DATA / "speech-first-principles-taxonomy.json").read_text())
    themes = {theme["id"]: theme for theme in taxonomy.get("themes", [])}
    semantic_queue = json.loads((DATA / "interspeech-2025-semantic-review-queue.json").read_text())
    semantic_by_id = {row["paper_id"]: row for row in semantic_queue.get("rows", [])}
    evaluation_enrichments = {row["paper_id"]: row for row in json.loads((DATA / "interspeech-2025-d3-evaluation-enrichments.json").read_text()).get("records", [])}
    notes = {}
    captures = {}
    for filename in ("interspeech-2025-representative-papers.json", "interspeech-2025-second-d3-papers.json", "interspeech-2025-third-d3-papers.json", "interspeech-2025-fourth-d3-papers.json", "interspeech-2025-fifth-d3-papers.json", "interspeech-2025-sixth-d3-papers.json", "interspeech-2025-seventh-d3-papers.json", "interspeech-2025-eighth-d3-papers.json", "interspeech-2025-ninth-d3-papers.json", "interspeech-2025-tenth-d3-papers.json", "interspeech-2025-eleventh-d3-papers.json", "interspeech-2025-twelfth-d3-papers.json", "interspeech-2025-thirteenth-d3-papers.json", "interspeech-2025-fourteenth-d3-papers.json", "interspeech-2025-fifteenth-d3-papers.json", "interspeech-2025-sixteenth-d3-papers.json", "interspeech-2025-seventeenth-d3-papers.json", "interspeech-2025-eighteenth-d3-papers.json", "interspeech-2025-nineteenth-d3-papers.json", "interspeech-2025-twentieth-d3-papers.json", "interspeech-2025-twentyfirst-d3-papers.json", "interspeech-2025-twentisecond-d3-papers.json", "interspeech-2025-twentythird-d3-papers.json", "interspeech-2025-twentyfourth-d3-papers.json", "interspeech-2025-twentyfifth-d3-papers.json", "interspeech-2025-twentysixth-d3-papers.json", "interspeech-2025-twentyseventh-d3-papers.json", "interspeech-2025-twentyeighth-d3-papers.json", "interspeech-2025-twentyninth-d3-papers.json", "interspeech-2025-thirtieth-d3-papers.json", "interspeech-2025-thirtyfirst-d3-papers.json", "interspeech-2025-thirtysecond-d3-papers.json", "interspeech-2025-thirtythird-d3-papers.json", "interspeech-2025-thirtyfourth-d3-papers.json", "interspeech-2025-thirtyfifth-d3-papers.json", "interspeech-2025-thirtysixth-d3-papers.json", "interspeech-2025-thirtyseventh-d3-papers.json", "interspeech-2025-thirtyeighth-d3-papers.json", "interspeech-2025-thirtyninth-d3-papers.json", "interspeech-2025-fortieth-d3-papers.json", "interspeech-2025-fortyfirst-d3-papers.json", "interspeech-2025-fortysecond-d3-papers.json", "interspeech-2025-fortythird-d3-papers.json", "interspeech-2025-fortyfourth-d3-papers.json", "interspeech-2025-fortyfifth-d3-papers.json", "interspeech-2025-fortysixth-d3-papers.json", "interspeech-2025-fortyseventh-d3-papers.json", "interspeech-2025-fortyeighth-d3-papers.json", "interspeech-2025-fortyninth-d3-papers.json", "interspeech-2025-fiftieth-d3-papers.json", "interspeech-2025-fiftyfirst-d3-papers.json", "interspeech-2025-fiftysecond-d3-papers.json", "interspeech-2025-fiftythird-d3-papers.json", "interspeech-2025-fiftyfourth-d3-papers.json", "interspeech-2025-fiftyfifth-d3-papers.json", "interspeech-2025-fiftysixth-d3-papers.json", "interspeech-2025-fiftyseventh-d3-papers.json", "interspeech-2025-sixtysecond-d3-papers.json", "interspeech-2025-sixtythird-d3-papers.json"):
        for row in json.loads((DATA / filename).read_text())["papers"]:
            captures[row["paper_id"]] = row
    for filename in ("interspeech-2025-d3-notes.json", "interspeech-2025-second-d3-notes.json", "interspeech-2025-third-d3-notes.json", "interspeech-2025-fourth-d3-notes.json", "interspeech-2025-fifth-d3-notes.json", "interspeech-2025-sixth-d3-notes.json", "interspeech-2025-seventh-d3-notes.json", "interspeech-2025-eighth-d3-notes.json", "interspeech-2025-ninth-d3-notes.json", "interspeech-2025-tenth-d3-notes.json", "interspeech-2025-eleventh-d3-notes.json", "interspeech-2025-twelfth-d3-notes.json", "interspeech-2025-thirteenth-d3-notes.json", "interspeech-2025-fourteenth-d3-notes.json", "interspeech-2025-fifteenth-d3-notes.json", "interspeech-2025-sixteenth-d3-notes.json", "interspeech-2025-seventeenth-d3-notes.json", "interspeech-2025-eighteenth-d3-notes.json", "interspeech-2025-nineteenth-d3-notes.json", "interspeech-2025-twentieth-d3-notes.json", "interspeech-2025-twentyfirst-d3-notes.json", "interspeech-2025-twentisecond-d3-notes.json", "interspeech-2025-twentythird-d3-notes.json", "interspeech-2025-twentyfourth-d3-notes.json", "interspeech-2025-twentyfifth-d3-notes.json", "interspeech-2025-twentysixth-d3-notes.json", "interspeech-2025-twentyseventh-d3-notes.json", "interspeech-2025-twentyeighth-d3-notes.json", "interspeech-2025-twentyninth-d3-notes.json", "interspeech-2025-thirtieth-d3-notes.json", "interspeech-2025-thirtyfirst-d3-notes.json", "interspeech-2025-thirtysecond-d3-notes.json", "interspeech-2025-thirtythird-d3-notes.json", "interspeech-2025-thirtyfourth-d3-notes.json", "interspeech-2025-thirtyfifth-d3-notes.json", "interspeech-2025-thirtysixth-d3-notes.json", "interspeech-2025-thirtyseventh-d3-notes.json", "interspeech-2025-thirtyeighth-d3-notes.json", "interspeech-2025-thirtyninth-d3-notes.json", "interspeech-2025-fortieth-d3-notes.json", "interspeech-2025-fortyfirst-d3-notes.json", "interspeech-2025-fortysecond-d3-notes.json", "interspeech-2025-fortythird-d3-notes.json", "interspeech-2025-fortyfourth-d3-notes.json", "interspeech-2025-fortyfifth-d3-notes.json", "interspeech-2025-fortysixth-d3-notes.json", "interspeech-2025-fortyseventh-d3-notes.json", "interspeech-2025-fortyeighth-d3-notes.json", "interspeech-2025-fortyninth-d3-notes.json", "interspeech-2025-fiftieth-d3-notes.json"):
        for row in json.loads((DATA / filename).read_text())["notes"]:
            notes[row["paper_id"]] = row
    for row in json.loads((DATA / "interspeech-2025-fortysecond-d3-papers.json").read_text())["papers"]:
        captures[row["paper_id"]] = row
    for row in json.loads((DATA / "interspeech-2025-fortysecond-d3-notes.json").read_text())["notes"]:
        notes[row["paper_id"]] = row
    for row in json.loads((DATA / "interspeech-2025-fortythird-d3-papers.json").read_text())["papers"]:
        captures[row["paper_id"]] = row
    for row in json.loads((DATA / "interspeech-2025-fortythird-d3-notes.json").read_text())["notes"]:
        notes[row["paper_id"]] = row
    for row in json.loads((DATA / "interspeech-2025-fortyfourth-d3-papers.json").read_text())["papers"]:
        captures[row["paper_id"]] = row
    for row in json.loads((DATA / "interspeech-2025-fortyfourth-d3-notes.json").read_text())["notes"]:
        notes[row["paper_id"]] = row
    for row in json.loads((DATA / "interspeech-2025-fortyfifth-d3-papers.json").read_text())["papers"]:
        captures[row["paper_id"]] = row
    for row in json.loads((DATA / "interspeech-2025-fortyfifth-d3-notes.json").read_text())["notes"]:
        notes[row["paper_id"]] = row
    for row in json.loads((DATA / "interspeech-2025-fortysixth-d3-papers.json").read_text())["papers"]:
        captures[row["paper_id"]] = row
    for row in json.loads((DATA / "interspeech-2025-fortysixth-d3-notes.json").read_text())["notes"]:
        notes[row["paper_id"]] = row
    for row in json.loads((DATA / "interspeech-2025-fiftieth-d3-papers.json").read_text())["papers"]:
        captures[row["paper_id"]] = row
    for row in json.loads((DATA / "interspeech-2025-fiftieth-d3-notes.json").read_text())["notes"]:
        notes[row["paper_id"]] = row
    for row in json.loads((DATA / "interspeech-2025-fiftyfirst-d3-papers.json").read_text())["papers"]:
        captures[row["paper_id"]] = row
    for row in json.loads((DATA / "interspeech-2025-fiftyfirst-d3-notes.json").read_text())["notes"]:
        notes[row["paper_id"]] = row
    for row in json.loads((DATA / "interspeech-2025-fiftysecond-d3-papers.json").read_text())["papers"]:
        captures[row["paper_id"]] = row
    for row in json.loads((DATA / "interspeech-2025-fiftysecond-d3-notes.json").read_text())["notes"]:
        notes[row["paper_id"]] = row
    for row in json.loads((DATA / "interspeech-2025-fiftythird-d3-papers.json").read_text())["papers"]:
        captures[row["paper_id"]] = row
    for row in json.loads((DATA / "interspeech-2025-fiftythird-d3-notes.json").read_text())["notes"]:
        notes[row["paper_id"]] = row
    for row in json.loads((DATA / "interspeech-2025-fiftyfourth-d3-papers.json").read_text())["papers"]:
        captures[row["paper_id"]] = row
    for row in json.loads((DATA / "interspeech-2025-fiftyfourth-d3-notes.json").read_text())["notes"]:
        notes[row["paper_id"]] = row
    for row in json.loads((DATA / "interspeech-2025-fiftyfifth-d3-papers.json").read_text())["papers"]:
        captures[row["paper_id"]] = row
    for row in json.loads((DATA / "interspeech-2025-fiftyfifth-d3-notes.json").read_text())["notes"]:
        notes[row["paper_id"]] = row
    for row in json.loads((DATA / "interspeech-2025-fiftysixth-d3-papers.json").read_text())["papers"]:
        captures[row["paper_id"]] = row
    for row in json.loads((DATA / "interspeech-2025-fiftysixth-d3-notes.json").read_text())["notes"]:
        notes[row["paper_id"]] = row
    for row in json.loads((DATA / "interspeech-2025-fiftyseventh-d3-papers.json").read_text())["papers"]:
        captures[row["paper_id"]] = row
    for row in json.loads((DATA / "interspeech-2025-fiftyseventh-d3-notes.json").read_text())["notes"]:
        notes[row["paper_id"]] = row
    for row in json.loads((DATA / "interspeech-2025-fiftyeighth-d3-papers.json").read_text())["papers"]:
        captures[row["paper_id"]] = row
    for row in json.loads((DATA / "interspeech-2025-fiftyeighth-d3-notes.json").read_text())["notes"]:
        notes[row["paper_id"]] = row
    for row in json.loads((DATA / "interspeech-2025-fiftyninth-d3-papers.json").read_text())["papers"]:
        captures[row["paper_id"]] = row
    for row in json.loads((DATA / "interspeech-2025-fiftyninth-d3-notes.json").read_text())["notes"]:
        notes[row["paper_id"]] = row
    for row in json.loads((DATA / "interspeech-2025-sixtieth-d3-papers.json").read_text())["papers"]:
        captures[row["paper_id"]] = row
    for row in json.loads((DATA / "interspeech-2025-sixtieth-d3-notes.json").read_text())["notes"]:
        notes[row["paper_id"]] = row
    for row in json.loads((DATA / "interspeech-2025-sixtyfirst-d3-papers.json").read_text())["papers"]:
        captures[row["paper_id"]] = row
    for row in json.loads((DATA / "interspeech-2025-sixtyfirst-d3-notes.json").read_text())["notes"]:
        notes[row["paper_id"]] = row
    for row in json.loads((DATA / "interspeech-2025-sixtysecond-d3-papers.json").read_text())["papers"]:
        captures[row["paper_id"]] = row
    for row in json.loads((DATA / "interspeech-2025-sixtysecond-d3-notes.json").read_text())["notes"]:
        notes[row["paper_id"]] = row
    for row in json.loads((DATA / "interspeech-2025-sixtythird-d3-papers.json").read_text())["papers"]:
        captures[row["paper_id"]] = row
    for row in json.loads((DATA / "interspeech-2025-sixtythird-d3-notes.json").read_text())["notes"]:
        notes[row["paper_id"]] = row
    rows = []
    for paper in source["papers"]:
        d3 = notes.get(paper["paper_id"])
        record = abstract_record(paper, "D3" if d3 else "D2", d3, captures)
        if record.get("depth") == "D3" and paper["paper_id"] in evaluation_enrichments:
            enrichment = evaluation_enrichments[paper["paper_id"]]
            record["eval"] = enrichment["eval"]
            record.setdefault("full_paper_evidence", {})["evaluation_source"] = enrichment["evaluation_source"]
        semantic = semantic_by_id.get(paper["paper_id"], {})
        reviewed = semantic.get("analyst_review") or {}
        assignment = reviewed if semantic.get("review_state") == "analyst-reviewed" else (semantic.get("candidate_assignments") or [{}])[0]
        record["semantic_review"] = {
            "decision": semantic.get("decision"),
            "review_state": semantic.get("review_state"),
            "evidence_depth": semantic.get("evidence_depth"),
            "confidence": semantic.get("confidence"),
            "theme_id": assignment.get("theme_id"),
            "subtheme_id": assignment.get("subtheme_id"),
            "concept_id": assignment.get("concept_id"),
            "semantic_reasoning": reviewed.get("semantic_reasoning") if reviewed else None,
            "alternative_assignment": semantic.get("alternative_assignment"),
            "evidence_excerpt": (reviewed.get("evidence_excerpt") if reviewed else semantic.get("evidence_excerpt")),
            "claim_boundary": reviewed.get("claim_boundary") if reviewed else semantic.get("review_rule"),
        }
        if reviewed:
            theme = themes.get(reviewed.get("theme_id"), {})
            scaffolded = []
            if record["depth"] == "D2":
                if "does not identify" in record["wh"].lower() or "does not specify" in record["wh"].lower():
                    record["wh"] = f"The ordinary difficulty is: {theme.get('ordinary_problem', 'the abstract does not expose the full real-world difficulty')}. The abstract does not establish which of these difficulties dominates this paper's setting."
                    scaffolded.append("wh")
                if "does not state a natural first attempt" in record["naive"].lower() or "cannot be inferred" in record["naive"].lower():
                    record["naive"] = f"A natural first attempt would be: {theme.get('naive_failure', 'apply a simple task-specific baseline')}. The abstract does not establish the paper's complete baseline comparison."
                    scaffolded.append("naive")
                if "does not state a central conceptual move" in record["ap"].lower():
                    record["ap"] = reviewed.get("semantic_reasoning") or record["ap"]
                    scaffolded.append("ap")
                if "does not specify a mathematical object" in record["math"].lower():
                    record["math"] = "The abstract does not expose the full loss, representation, or decision rule. Its mathematical/evaluation details remain a D3 reading task rather than a safe inference from the title."
                    scaffolded.append("math")
                if "does not establish a practical payoff" in record["po"].lower():
                    record["po"] = "The bounded intended payoff is the paper's reviewed conceptual move: " + (reviewed.get("semantic_reasoning") or "the abstract-stated task result") + " Exact practical benefit remains abstract-bounded."
                    scaffolded.append("po")
            record["quality_flags"] = {"d2_scaffolded_fields": scaffolded, "boundary": "Scaffolding supplies a plain-language question or taxonomy anchor; it is not additional paper evidence."}
            record["dots"] = {
                "theme_id": reviewed.get("theme_id"),
                "subtheme_id": reviewed.get("subtheme_id"),
                "concept_id": reviewed.get("concept_id"),
                "semantic_reasoning": reviewed.get("semantic_reasoning"),
                "status": "analyst-reviewed semantic link",
            }
        rows.append(record)
    out = DATA / "interspeech-2025-deep-paper-analyses.jsonl"
    with out.open("w") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False) + "\n")
    report = REPORTS / "INTERSPEECH_2025_DEEP_PAPER_ANALYSES.md"
    scaffolded_count = sum(bool(row.get("quality_flags", {}).get("d2_scaffolded_fields")) for row in rows)
    report.write_text("\n".join([
        "# INTERSPEECH 2025 deep paper analyses",
        "",
        "Every captured paper has a depth-labeled first-principles record in `data/interspeech-2025-deep-paper-analyses.jsonl`.",
        "",
        f"- Papers: {len(rows)}",
        f"- D3 full-paper records: {sum(x['depth'] == 'D3' for x in rows)}",
        f"- D2 abstract-bounded records: {sum(x['depth'] == 'D2' for x in rows)}",
        "",
        "D2 records provide an evidence-bounded reading of the ordinary problem, stated difficulty, proposed move, reported evaluation, and explicit unknowns. They do not claim full-paper mechanisms or limitations. D3 records inherit the existing structured notes and remain author-reported unless an independent execution record says otherwise.",
        "",
        f"For {scaffolded_count} D2 records with analyst-reviewed semantic assignments, plain-language taxonomy scaffolds fill otherwise missing beginner-facing fields; each is marked in `quality_flags` and is not treated as additional paper evidence.",
        "",
        "The required fields are `bp`, `wh`, `naive`, `ap`, `mech`, `math`, `dots`, `eval`, `ww`, `po`, `limits`, `source`, and `depth`.",
        "",
    ]) + "\n")
    print(json.dumps({"papers": len(rows), "D3": sum(x["depth"] == "D3" for x in rows), "D2": sum(x["depth"] == "D2" for x in rows)}))


if __name__ == "__main__":
    main()
