#!/usr/bin/env python3
"""Adjudicate the remaining provisional INTERSPEECH scope proposals."""

import hashlib
import json
import re
import urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = HERE / "data"

SUPPORTED = {
    "istaiteh25_interspeech": ("evaluation-deployment-and-consequence", "metrics-and-targets", "word-error-versus-understanding", "D2"),
    "lin25e_interspeech": ("meaning-and-interaction", "prosody-and-intent", "prosodic-meaning", "D2"),
    "moore25_interspeech": ("meaning-and-interaction", "dialogue-and-turn-taking", "dialogue-state", "D1"),
    "ormaechea25_interspeech": ("meaning-and-interaction", "grounding-and-action", "referential-grounding", "D2"),
    "phaye25_interspeech": ("listening-and-separation", "noise-enhancement", "speech-prior-denoising", "D2"),
    "raut25_interspeech": ("meaning-and-interaction", "dialogue-and-turn-taking", "dialogue-state", "D2"),
    "wu25d_interspeech": ("listening-and-separation", "noise-enhancement", "nonstationary-noise", "D2"),
}

REJECT_REASONS = {
    "jeong25_interspeech": "The full paper classifies lung sounds, not human spoken speech; it is a biomedical audio paper outside this atlas.",
    "jiang25b_interspeech": "The full paper studies anomalous industrial sound detection on DCASE data, not human spoken speech.",
    "jiang25c_interspeech": "The full paper studies anomalous machine-sound detection, not human spoken speech.",
    "kang25b_interspeech": "The full paper converts human voice into animal and designed non-speech sounds; the target object is outside a spoken-speech atlas.",
    "liang25b_interspeech": "The full paper generates sound effects from video; it does not model human spoken speech.",
    "liu25h_interspeech": "The full paper studies singing voice conversion rather than spoken-speech voice conversion; singing is outside this scope.",
    "mohsin25_interspeech": "The full paper audits gender bias in general text-to-audio generation, without a human spoken-speech object.",
    "rasendiranr25_interspeech": "The full paper classifies bird songs, not human spoken speech.",
    "schuster25_interspeech": "The full paper detects anomalies in Kubernetes multivariate time series, not speech or audio.",
    "song25_interspeech": "The full paper classifies ultrasonic vocalizations from mice, not human spoken speech.",
    "szmajdzinski25_interspeech": "The full paper classifies mouse ultrasonic vocalizations, not human spoken speech.",
    "takeuchi25_interspeech": "The full paper performs general audio captioning on acoustic events and scenes, not spoken speech.",
    "tao25_interspeech": "The full paper estimates direction of arrival for general acoustic sources and does not establish a speech object.",
    "tisdale25_interspeech": "The full paper studies eye-gaze tracking for health assessment; its multimodal dialogue interface does not make spoken speech the research object.",
    "wu25b_interspeech": "The full paper detects anomalous machine sounds under domain shift, not human spoken speech.",
    "wu25c_interspeech": "The full paper detects autism-related mouse ultrasonic vocalizations, not human spoken speech.",
    "xu25_interspeech": "The full paper performs general audio captioning, not spoken-speech recognition or interaction.",
    "xu25b_interspeech": "The full paper separates string-quartet instruments; music source separation is outside this spoken-speech atlas.",
    "xu25j_interspeech": "The full paper captions general audio from visual guides on AudioCaps, not human spoken speech.",
    "yang25h_interspeech": "The full paper generates general audio events from text; it does not establish a spoken-speech target.",
    "yang25q_interspeech": "The full paper localizes general sound sources and does not establish a spoken-speech object.",
    "zhang25f_interspeech": "The full paper detects face liveness from ultrasound; this is a sensing/security task, not spoken speech.",
    "zhou25c_interspeech": "The full paper classifies infant cries, not human spoken speech; cries are outside the atlas scope.",
    "zhou25d_interspeech": "The full paper detects abnormal UAV sounds, not human spoken speech.",
}


def abstract(text: str) -> str:
    text = re.sub(r"\s+", " ", text)
    match = re.search(r"Abstract\s+(.*?)(?:\s+1\.?\s+Introduction|\s+1\s+Introduction)", text, re.I)
    return (match.group(1) if match else text[:1800]).strip()[:1800]


def main() -> None:
    queue = json.loads((DATA / "interspeech-2025-semantic-review-queue.json").read_text())
    by_id = {row["paper_id"]: row for row in queue["rows"]}
    rows = []
    for paper_id, (theme, subtheme, concept, depth) in SUPPORTED.items():
        paper = by_id[paper_id]
        if depth == "D2":
            source_file = DATA / "interspeech-2025-pdfs" / f"{paper_id}.pdf"
            text = (DATA / "interspeech-2025-text" / f"{paper_id}.txt").read_text()
            sha = hashlib.sha256(source_file.read_bytes()).hexdigest()
        else:
            source_file = None
            text = urllib.request.urlopen(paper["paper_url"], timeout=10).read().decode("utf-8", errors="ignore")
            sha = hashlib.sha256(text.encode("utf-8")).hexdigest()
        rows.append({
            "paper_id": paper_id, "title": paper["title"], "decision": "supported",
            "confidence": f"analyst-reviewed-{depth}", "theme_id": theme,
            "subtheme_id": subtheme, "concept_id": concept,
            "semantic_reasoning": f"The official archive evidence identifies a human spoken-speech object and a bounded problem that instantiate {concept} under {subtheme}; this resolves membership only.",
            "evidence_excerpt": abstract(text), "source_location": paper["paper_url"],
            "source_sha256": sha, "evidence_depth": depth,
            "review_state": "analyst-reviewed",
            "claim_boundary": "Official archive evidence supports taxonomy membership; this pass does not claim independent reproduction or scientific validity.",
        })
    for paper_id, reason in REJECT_REASONS.items():
        paper = by_id[paper_id]
        source_file = DATA / "interspeech-2025-pdfs" / f"{paper_id}.pdf"
        text = (DATA / "interspeech-2025-text" / f"{paper_id}.txt").read_text()
        rows.append({
            "paper_id": paper_id, "title": paper["title"], "decision": "unsupported",
            "confidence": "analyst-reviewed-D2", "theme_id": None, "subtheme_id": None,
            "concept_id": None, "semantic_reasoning": reason,
            "evidence_excerpt": abstract(text), "source_location": paper["paper_url"],
            "source_sha256": hashlib.sha256(source_file.read_bytes()).hexdigest(),
            "evidence_depth": "D2", "review_state": "analyst-reviewed",
            "claim_boundary": "Official full-paper evidence resolves scope membership only; the paper is excluded from the spoken-speech taxonomy.",
        })
    payload = {"schema_version": 1, "batch_id": "interspeech-2025-semantic-batch-026", "reviewed_count": len(rows), "review_method": "Official ISCA archive evidence reviewed against the first-principles speech scope; supported and out-of-scope decisions are preserved separately.", "rows": sorted(rows, key=lambda row: row["paper_id"])}
    (DATA / "interspeech-2025-semantic-reviewed-batch-026.json").write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({"rows": len(rows), "supported": len(SUPPORTED), "unsupported": len(REJECT_REASONS)}))


if __name__ == "__main__":
    main()
