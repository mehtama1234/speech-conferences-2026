#!/usr/bin/env python3
"""Record the next eight title-only D1 taxonomy adjudications."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "bijoy25_interspeech": ("confirmed-current-boundary", "The title explicitly concerns multilingual speech-emotion recognition. Title-only evidence supports paralinguistic state, without establishing emotion-recognition reliability or the distillation benefit.", "meaning-and-interaction", "prosody-and-paralinguistics", "paralinguistic-state"),
    "birkholz25_interspeech": ("confirmed-current-boundary", "The title explicitly concerns sound radiation from the vocal-tract wall. Title-only evidence supports vocal-tract filtering, without establishing model accuracy.", "sound-and-production", "source-generation", "vocal-tract-filter"),
    "birkholz25b_interspeech": ("confirmed-current-boundary", "The title explicitly concerns transfer functions measured from physical vocal-tract models. Title-only evidence supports vocal-tract filtering, without establishing how wall coverings affect acoustic fidelity.", "sound-and-production", "source-generation", "vocal-tract-filter"),
    "biswas25b_interspeech": ("rejected-out-of-scope", "The title concerns efficient speech-language understanding but does not establish a denoising or enhancement task. With title-only evidence, speech-prior denoising membership is not supported.", None, None, None),
    "blaschke25_interspeech": ("confirmed-current-boundary", "The title explicitly concerns German dialect ASR and dialect-to-standard speech translation. Title-only evidence supports dialect and variety, without establishing dialect coverage or translation quality.", "languages-accents-and-resources", "accent-dialect-and-cultural-meaning", "dialect-and-variety"),
    "bn25_interspeech": ("rejected-out-of-scope", "The title concerns hallucinations in medical text summarization and does not establish a human-speech or spoken-language task. With title-only evidence, referential grounding membership is not supported.", None, None, None),
    "bodur25_interspeech": ("confirmed-current-boundary", "The title explicitly concerns speech reduction, vowel space, and articulation dynamics in French. Title-only evidence supports articulatory coordination, without establishing the articulatory relationship.", "sound-and-production", "articulatory-dynamics", "articulatory-coordination"),
    "bolanos25_interspeech": ("rejected-out-of-scope", "The title concerns explanations for general audio classification models and does not establish a human-speech or spoken-language task. With title-only evidence, speech quality and naturalness membership is not supported.", None, None, None),
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
