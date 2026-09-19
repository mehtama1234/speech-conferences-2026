#!/usr/bin/env python3
"""Record the next eight title-only D1 taxonomy adjudications."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "casanova25_interspeech": ("confirmed-current-boundary", "The title explicitly concerns ultra-fast speech language model inference. Title-only evidence supports latency and resource budget, without establishing inference speed or quality tradeoffs.", "evaluation-deployment-and-consequence", "deployment-cost", "latency-and-resource"),
    "chae25_interspeech": ("rejected-out-of-scope", "The title concerns full-song lyrics generation and musical structure rather than a human-speech or spoken-language task. With title-only evidence, temporal alignment for speech is not supported.", None, None, None),
    "chae25b_interspeech": ("confirmed-current-boundary", "The title explicitly concerns noise-robust speech coding with variable bitrate. Title-only evidence supports changing and adverse noise, without establishing coding robustness or bitrate quality.", "listening-and-separation", "noise-enhancement", "nonstationary-noise"),
    "chan25_interspeech": ("reassigned-to-neighbor", "The title explicitly concerns multilingual stop voicing production and relative acoustic cues. Title-only evidence places it under pronunciation variation rather than target-conditioned separation.", "recognition-and-alignment", "pronunciation-and-variation", "pronunciation-variation"),
    "chandra25_interspeech": ("reassigned-to-neighbor", "The title explicitly concerns speaking styles and speech emotion. Title-only evidence places it under paralinguistic state rather than prosodic meaning.", "meaning-and-interaction", "prosody-and-paralinguistics", "paralinguistic-state"),
    "chang25_interspeech": ("confirmed-current-boundary", "The title explicitly concerns a speaker-invariant speech tokenizer for spoken language models. Title-only evidence supports acoustic-to-token mapping, without establishing token quality or speaker invariance.", "recognition-and-alignment", "acoustic-unit-learning", "acoustic-to-token"),
    "chang25b_interspeech": ("rejected-out-of-scope", "The title concerns a feature representation for classifying speech, music, and environmental sounds, not a bounded speech research object. With title-only evidence, quality and naturalness membership is not supported.", None, None, None),
    "chang25c_interspeech": ("confirmed-current-boundary", "The title explicitly concerns modeling videoconference conversation experience with multimodal data. Title-only evidence supports dialogue state, without establishing experience-modeling validity.", "meaning-and-interaction", "intent-and-dialogue-state", "dialogue-state"),
}

def main():
    payload = json.loads(QUEUE.read_text())
    rows = {r["paper_id"]: r for r in payload["rows"]}
    for pid, (decision, note, theme, subtheme, concept) in DECISIONS.items():
        row = rows[pid]
        if row["taxonomy_review_state"] == "taxonomy-adjudicated":
            raise SystemExit(f"already adjudicated: {pid}")
        row.update({"taxonomy_review_state": "taxonomy-adjudicated", "final_decision": decision, "reviewer_note": note, "reviewed_sections": ["title"], "final_theme_id": theme, "final_subtheme_id": subtheme, "final_concept_id": concept})
    payload["adjudicated_count"] = sum(r["taxonomy_review_state"] == "taxonomy-adjudicated" for r in rows.values())
    payload["open_count"] = len(rows) - payload["adjudicated_count"]
    payload["decision_counts"] = {d: sum(r.get("final_decision") == d for r in rows.values() if r["taxonomy_review_state"] == "taxonomy-adjudicated") for d in sorted({r.get("final_decision") for r in rows.values() if r["taxonomy_review_state"] == "taxonomy-adjudicated"})}
    QUEUE.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({"batch": len(DECISIONS), "adjudicated": payload["adjudicated_count"], "open": payload["open_count"]}))

if __name__ == "__main__":
    main()
