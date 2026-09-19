#!/usr/bin/env python3
"""Record the next eight title-only D1 taxonomy adjudications."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "chen25f_interspeech": ("confirmed-current-boundary", "The title concerns self-distillation, prototype learning, dimension regularization, and score normalization in a speaker-recognition setting. Title-only evidence supports speaker verification, without establishing verification performance.", "people-variation-and-health", "identity-and-life-stage", "speaker-verification"),
    "chen25g_interspeech": ("confirmed-current-boundary", "The title explicitly concerns prosodic characteristics of Chinese rhetorical questions in naturalistic speech. Title-only evidence supports prosodic meaning, without establishing the rhetorical or acoustic interpretation.", "meaning-and-interaction", "prosody-and-paralinguistics", "prosodic-meaning"),
    "chen25h_interspeech": ("confirmed-current-boundary", "The title explicitly concerns inclusive automatic speech recognition across language varieties. Title-only evidence supports accent robustness, without establishing benchmark coverage or robustness.", "languages-accents-and-resources", "accent-dialect-and-cultural-meaning", "accent-robustness"),
    "chen25i_interspeech": ("reassigned-to-neighbor", "The title explicitly concerns fine-grained speech descriptors for explainable emotion recognition. Title-only evidence places it under paralinguistic state rather than calibration and selective use.", "meaning-and-interaction", "prosody-and-paralinguistics", "paralinguistic-state"),
    "chen25k_interspeech": ("rejected-out-of-scope", "The title concerns audio-visual corpus design for challenge production but does not establish a human-speech or spoken-language object strongly enough to support spatial filtering from title-only evidence.", None, None, None),
    "chen25l_interspeech": ("rejected-out-of-scope", "The title concerns ambisonic target-sound extraction and does not establish a human-speech or spoken-language task. With title-only evidence, spatial filtering for speech is not supported.", None, None, None),
    "chen25m_interspeech": ("confirmed-current-boundary", "The title explicitly concerns reconstruction of dysarthric speech using a latent diffusion model. Title-only evidence supports atypical articulation and dysarthria, without establishing reconstruction quality or user benefit.", "people-variation-and-health", "atypical-and-assistive-speech", "dysarthria-and-atypical-speech"),
    "chen25n_interspeech": ("reassigned-to-neighbor", "The title explicitly concerns vocal-cord-disorder classification in continuous Mandarin speech. Title-only evidence places it under clinical speech marker rather than vocal-tract filtering.", "people-variation-and-health", "clinical-markers", "clinical-speech-marker"),
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
