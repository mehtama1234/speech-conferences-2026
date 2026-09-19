#!/usr/bin/env python3
"""Record the next eight evidence-bounded taxonomy adjudications."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "pan25b_interspeech": (
        "confirmed-current-boundary",
        "The abstract converts voices while controlling emotion from natural-language prompts or reference speech and reports intensity, naturalness, and quality evaluations. The evidence supports style and emotion control, bounded by the ClapFM-EVC components and subjective/objective tests.",
        ["title", "abstract"], "voice-generation-and-control", "expression-and-interactive-control", "style-and-emotion-control",
    ),
    "pan25c_interspeech": (
        "confirmed-current-boundary",
        "The abstract introduces a Chinese heart-failure speech database with paired recordings and tests universal and personalized classification, noting individual differences. The evidence supports clinical speech markers, bounded by the database, hospitalization pairing, and classification analyses.",
        ["title", "abstract"], "people-variation-and-health", "clinical-markers", "clinical-speech-marker",
    ),
    "pan25d_interspeech": (
        "confirmed-current-boundary",
        "The abstract extracts a selected speaker from mixtures using the target face and attention over co-occurring faces, with cross-dataset evaluation. The evidence supports target-conditioned separation, bounded by the audio-visual cue and VoxCeleb2/MISP/LRS evaluations.",
        ["title", "abstract"], "listening-and-separation", "source-separation", "target-conditioned-separation",
    ),
    "panda25_interspeech": (
        "confirmed-current-boundary",
        "The abstract augments internal speech representations during training and measures improved ASR performance on unseen and multilingual data. The evidence supports distribution shift, bounded by LibriSpeech/MUCS21, embedding replacement, and the stated robustness evaluation.",
        ["title", "abstract"], "evaluation-deployment-and-consequence", "robustness-and-shift", "distribution-shift",
    ),
    "papadimitriou25_interspeech": (
        "confirmed-current-boundary",
        "The abstract recognizes cued speech from coordinated hand, lip, appearance, and skeletal streams to support communication without requiring explicit synchronization. The evidence supports augmentative communication, bounded by the three benchmark datasets and multimodal alignment method.",
        ["title", "abstract"], "people-variation-and-health", "atypical-and-assistive-speech", "augmentative-communication",
    ),
    "parcollet25_interspeech": (
        "confirmed-current-boundary",
        "The abstract introduces a curated 25,000-hour, commercially usable English speech collection spanning speakers, accents, and speaking conditions for ASR research. The evidence supports speech-data collection, bounded by the stated licensing, scale, and data diversity.",
        ["title", "abstract"], "languages-accents-and-resources", "data-creation", "speech-data-collection",
    ),
    "parikh25_interspeech": (
        "reassigned-to-neighbor",
        "The abstract evaluates goodness-of-pronunciation scoring for learner speech and restricts possible substitutions using phonological knowledge. The governing boundary is pronunciation variation, not alignment, because the outcome is mispronunciation detection across L2 speakers.",
        ["title", "abstract"], "recognition-and-alignment", "pronunciation-and-variation", "pronunciation-variation",
    ),
    "parikh25b_interspeech": (
        "confirmed-current-boundary",
        "The abstract compares logit- and probability-based GOP scores for detecting L2 mispronunciations and correlates them with human ratings. The evidence supports pronunciation variation, bounded by Dutch and Mandarin learner datasets and the stated scoring comparison.",
        ["title", "abstract"], "recognition-and-alignment", "pronunciation-and-variation", "pronunciation-variation",
    ),
}


def main():
    payload = json.loads(QUEUE.read_text())
    rows = {r["paper_id"]: r for r in payload["rows"]}
    for pid, (decision, note, sections, theme, subtheme, concept) in DECISIONS.items():
        row = rows[pid]
        if row["taxonomy_review_state"] == "taxonomy-adjudicated":
            raise SystemExit(f"already adjudicated: {pid}")
        row.update({
            "taxonomy_review_state": "taxonomy-adjudicated",
            "final_decision": decision,
            "reviewer_note": note,
            "reviewed_sections": sections,
            "final_theme_id": theme,
            "final_subtheme_id": subtheme,
            "final_concept_id": concept,
        })
    adjudicated = sum(r["taxonomy_review_state"] == "taxonomy-adjudicated" for r in rows.values())
    payload["adjudicated_count"] = adjudicated
    payload["open_count"] = len(rows) - adjudicated
    decisions = sorted({r.get("final_decision") for r in rows.values() if r["taxonomy_review_state"] == "taxonomy-adjudicated"})
    payload["decision_counts"] = {d: sum(r.get("final_decision") == d for r in rows.values() if r["taxonomy_review_state"] == "taxonomy-adjudicated") for d in decisions}
    QUEUE.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({"batch": len(DECISIONS), "adjudicated": adjudicated, "open": payload["open_count"]}))


if __name__ == "__main__": main()
