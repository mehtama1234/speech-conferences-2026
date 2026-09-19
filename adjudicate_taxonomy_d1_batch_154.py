#!/usr/bin/env python3
"""Record the next eight evidence-bounded taxonomy adjudications."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "pendyala25_interspeech": (
        "confirmed-current-boundary",
        "The abstract distills emotion and facial-expression information from unlabeled audio-visual data into a lightweight speech emotion recognizer. The evidence supports paralinguistic state, bounded by the teacher-student design and RAVDESS/CREMA-D evaluations.",
        ["title", "abstract"], "meaning-and-interaction", "prosody-and-paralinguistics", "paralinguistic-state",
    ),
    "peng25_interspeech": (
        "confirmed-current-boundary",
        "The abstract adapts a pretrained model for speaker verification using instance-aware prompts and parallel adapters while updating fewer than ten percent of parameters. The evidence supports speaker verification, bounded by VoxCeleb evaluation and parameter-efficient tuning.",
        ["title", "abstract"], "people-variation-and-health", "identity-and-life-stage", "speaker-verification",
    ),
    "peng25c_interspeech": (
        "confirmed-current-boundary",
        "The abstract cleans and releases a 166,000-hour, 75-language speech corpus from web data and trains open multilingual speech models on it. The evidence supports speech-data collection, bounded by YODAS cleaning, licensing, release, and multilingual benchmarks.",
        ["title", "abstract"], "languages-accents-and-resources", "data-creation", "speech-data-collection",
    ),
    "pepino25_interspeech": (
        "rejected-out-of-scope",
        "The abstract studies universal audio representation learning across speech, music, and environmental sounds and reports averaged cross-audio tasks, without a speech-specific object or claim. Generic audio representation learning is outside this speech taxonomy.",
        ["title", "abstract", "full_paper_excerpt"], None, None, None,
    ),
    "peters25_interspeech": (
        "confirmed-current-boundary",
        "The abstract uses acoustic, linguistic, and task-specific speech features to detect and subtype primary progressive aphasia and relates them to clinical interpretability. The evidence supports clinical speech markers, bounded by the PPA classes, features, and reported classification results.",
        ["title", "abstract"], "people-variation-and-health", "clinical-markers", "clinical-speech-marker",
    ),
    "peurey25_interspeech": (
        "confirmed-current-boundary",
        "The abstract reviews child-worn long-form speech recordings, their resources, annotation errors, and data-quality controls. The evidence supports speech-data collection, bounded by child language recordings, automated annotation limits, and proposed quality metrics.",
        ["title", "abstract"], "languages-accents-and-resources", "data-creation", "speech-data-collection",
    ),
    "pham25_interspeech": (
        "reassigned-to-neighbor",
        "The abstract reconstructs intelligible and expressive speech from silent talking-face video using acoustic and semantic paths and speech units. The governing boundary is intelligibility and naturalness in generated speech, not text-to-speech planning, because the input is visual rather than text.",
        ["title", "abstract"], "voice-generation-and-control", "waveform-and-codec-generation", "intelligibility-naturalness",
    ),
    "phan25_interspeech": (
        "confirmed-current-boundary",
        "The abstract detects mispronunciations in low-resource Finland Swedish using mostly L1 speech and minimal L2 data, with calibrated multilingual representations. The evidence supports pronunciation variation, bounded by the L1/L2 data, model adaptation, and reported precision/recall tradeoff.",
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
