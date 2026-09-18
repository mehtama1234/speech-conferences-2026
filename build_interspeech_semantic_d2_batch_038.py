#!/usr/bin/env python3
"""Record the last full-paper semantic pass over the 26 unresolved rows."""

import hashlib
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = HERE / "data"

ASSIGNMENTS = {
    "kano25_interspeech": ("meaning-and-interaction", "grounding-and-action", "referential-grounding"),
    "ke25_interspeech": ("people-variation-and-health", "clinical-and-assistive-speech", "clinical-speech-marker"),
    "kunze25_interspeech": ("people-variation-and-health", "speaker-characteristics", "age-and-development"),
    "kwon25b_interspeech": ("sound-and-production", "source-filter-production", "articulatory-coordination"),
    "li25aa_interspeech": ("evaluation-deployment-and-consequence", "privacy-security-and-accountability", "spoofing-and-deepfake"),
    "li25j_interspeech": ("people-variation-and-health", "clinical-and-assistive-speech", "augmentative-communication"),
    "li25v_interspeech": ("evaluation-deployment-and-consequence", "robustness-and-system-boundary", "latency-and-resource"),
    "li25w_interspeech": ("languages-accents-and-resources", "accent-and-cultural-boundaries", "dialect-and-variety"),
    "liu25f_interspeech": ("people-variation-and-health", "clinical-and-assistive-speech", "dysarthria-and-atypical-speech"),
    "mcguire25_interspeech": ("sound-and-production", "source-filter-production", "articulatory-coordination"),
    "novitasari25b_interspeech": ("recognition-and-alignment", "acoustic-unit-mapping", "acoustic-to-token"),
    "oh25_interspeech": ("evaluation-deployment-and-consequence", "metrics-and-targets", "calibration-and-selective-use"),
    "pepino25_interspeech": ("recognition-and-alignment", "acoustic-unit-mapping", "self-supervised-speech-units"),
    "shen25b_interspeech": ("evaluation-deployment-and-consequence", "metrics-and-targets", "calibration-and-selective-use"),
    "vukovic25_interspeech": ("languages-accents-and-resources", "low-resource-and-data-creation", "speech-data-collection"),
    "wan25_interspeech": ("evaluation-deployment-and-consequence", "robustness-and-system-boundary", "latency-and-resource"),
    "wang25l_interspeech": ("people-variation-and-health", "clinical-and-assistive-speech", "augmentative-communication"),
    "xu25c_interspeech": ("evaluation-deployment-and-consequence", "robustness-and-system-boundary", "latency-and-resource"),
    "xu25e_interspeech": ("evaluation-deployment-and-consequence", "robustness-and-system-boundary", "latency-and-resource"),
    "xu25i_interspeech": ("evaluation-deployment-and-consequence", "robustness-and-system-boundary", "latency-and-resource"),
    "yang25i_interspeech": ("sound-and-production", "source-filter-production", "articulatory-coordination"),
    "zhang25b_interspeech": ("languages-accents-and-resources", "accent-and-cultural-boundaries", "dialect-and-variety"),
    "zhao25j_interspeech": ("languages-accents-and-resources", "accent-and-cultural-boundaries", "dialect-and-variety"),
    "zuo25_interspeech": ("people-variation-and-health", "clinical-and-assistive-speech", "clinical-speech-marker"),
}

UNSUPPORTED = {
    "tian25_interspeech": "The full paper evaluates automated captioning on the Clotho environmental-audio benchmark; it does not study a spoken-speech object, so it is outside this atlas.",
    "wang25n_interspeech": "The full paper studies anomalous sound detection on DCASE industrial/consumer audio, not human spoken speech; it is outside this atlas.",
}


def abstract(text: str) -> str:
    text = re.sub(r"\s+", " ", text)
    match = re.search(r"Abstract\s+(.*?)(?:\s+1\.?\s+Introduction|\s+1\s+Introduction)", text, re.I)
    return (match.group(1) if match else text[:1800]).strip()[:1800]


def main() -> None:
    queue = json.loads((DATA / "interspeech-2025-semantic-review-queue.json").read_text())
    by_id = {row["paper_id"]: row for row in queue["rows"]}
    rows = []
    for paper_id, assignment in ASSIGNMENTS.items():
        paper = by_id[paper_id]
        pdf = DATA / "interspeech-2025-pdfs" / f"{paper_id}.pdf"
        text_path = DATA / "interspeech-2025-text" / f"{paper_id}.txt"
        excerpt = abstract(text_path.read_text())
        theme, subtheme, concept = assignment
        rows.append({
            "paper_id": paper_id,
            "title": paper["title"],
            "decision": "supported",
            "confidence": "analyst-reviewed-D2",
            "theme_id": theme,
            "subtheme_id": subtheme,
            "concept_id": concept,
            "semantic_reasoning": f"The official full paper identifies a human spoken-speech object and a bounded research problem that instantiate {concept} under {subtheme}; this resolves taxonomy membership, not the paper's scientific validity.",
            "evidence_excerpt": excerpt,
            "source_location": paper["paper_url"],
            "source_sha256": hashlib.sha256(pdf.read_bytes()).hexdigest(),
            "evidence_depth": "D2",
            "review_state": "analyst-reviewed",
            "claim_boundary": "Official full-paper evidence supports taxonomy membership; this pass does not claim independent reproduction or establish every empirical result.",
        })
    for paper_id, reasoning in UNSUPPORTED.items():
        paper = by_id[paper_id]
        pdf = DATA / "interspeech-2025-pdfs" / f"{paper_id}.pdf"
        text_path = DATA / "interspeech-2025-text" / f"{paper_id}.txt"
        rows.append({
            "paper_id": paper_id,
            "title": paper["title"],
            "decision": "unsupported",
            "confidence": "analyst-reviewed-D2",
            "theme_id": None, "subtheme_id": None, "concept_id": None,
            "semantic_reasoning": reasoning,
            "evidence_excerpt": abstract(text_path.read_text()),
            "source_location": paper["paper_url"],
            "source_sha256": hashlib.sha256(pdf.read_bytes()).hexdigest(),
            "evidence_depth": "D2",
            "review_state": "analyst-reviewed",
            "claim_boundary": "Official full-paper evidence resolves scope membership only; the paper is not included in the spoken-speech taxonomy.",
        })
    payload = {
        "schema_version": 1,
        "batch_id": "interspeech-2025-semantic-reviewed-d2-batch-038",
        "reviewed_count": len(rows),
        "review_method": "Official ISCA full-paper PDF read with abstract and scope evidence preserved; unsupported rows are retained explicitly.",
        "rows": sorted(rows, key=lambda row: row["paper_id"]),
    }
    (DATA / "interspeech-2025-semantic-reviewed-d2-batch-038.json").write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({"batch": payload["batch_id"], "rows": len(rows), "supported": sum(r["decision"] == "supported" for r in rows), "unsupported": sum(r["decision"] == "unsupported" for r in rows)}))


if __name__ == "__main__":
    main()
