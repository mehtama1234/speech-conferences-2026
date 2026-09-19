#!/usr/bin/env python3
"""Record the next eight evidence-bounded taxonomy adjudications."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "li25t_interspeech": ("confirmed-current-boundary", "The abstract separates speaker timbre and expressive style in retrieval-augmented zero-shot TTS and evaluates style expressiveness. The evidence supports style and emotion control, bounded by the reference-speech and tested-speaker conditions.", ["title", "abstract"], "voice-generation-and-control", "expression-and-interactive-control", "style-and-emotion-control"),
    "li25u_interspeech": ("confirmed-current-boundary", "The abstract reduces streaming ASR latency by aligning delayed teacher and student CTC outputs and reports a controlled emission delay. The evidence supports latency and resource budget, bounded by the AISHELL-1 and WenetSpeech experiments.", ["title", "abstract"], "evaluation-deployment-and-consequence", "deployment-cost", "latency-and-resource"),
    "li25v_interspeech": ("confirmed-current-boundary", "The abstract compresses Conformer and speech-foundation models to reduce memory and storage while preserving ASR performance. The evidence supports latency and resource budget, bounded by the reported parameter reductions and model families.", ["title", "abstract"], "evaluation-deployment-and-consequence", "deployment-cost", "latency-and-resource"),
    "li25w_interspeech": ("confirmed-current-boundary", "The abstract studies individual variation in Cantonese tone merging and how lexical context preserves or changes tonal contrasts. The evidence supports dialect and variety, bounded by Cantonese tone pairs and the participant groups.", ["title", "abstract"], "languages-accents-and-resources", "accent-dialect-and-cultural-meaning", "dialect-and-variety"),
    "li25x_interspeech": ("confirmed-current-boundary", "The abstract analyzes how grammatical and lexical contexts alter tone and vowel realization in Tianjin Mandarin weak elements. The evidence supports prosodic meaning, bounded by the six speakers and the studied weak-element categories.", ["title", "abstract"], "meaning-and-interaction", "prosody-and-paralinguistics", "prosodic-meaning"),
    "li25y_interspeech": ("confirmed-current-boundary", "The abstract measures rhythm development in bilingual preschool children and relates later-stage changes to cross-linguistic influence. The evidence supports age and developmental speech, bounded by the age range, learning exposure, and Putonghua task.", ["title", "abstract"], "people-variation-and-health", "identity-and-life-stage", "age-and-development"),
    "li25z_interspeech": ("confirmed-current-boundary", "The abstract disentangles speaker features from spoken content and evaluates the resulting representations for speaker verification on VoxCeleb. The evidence supports speaker verification, bounded by the datasets and latent-diffusion model.", ["title", "abstract"], "people-variation-and-health", "identity-and-life-stage", "speaker-verification"),
    "liang25_interspeech": ("confirmed-current-boundary", "The abstract generates synthetic interview text and speech with depression-related features and evaluates whether the added data improves depression detection. The evidence supports a clinical speech marker, while synthetic-data similarity does not establish clinical diagnosis.", ["title", "abstract"], "people-variation-and-health", "clinical-markers", "clinical-speech-marker"),
}

def main():
    payload = json.loads(QUEUE.read_text())
    rows = {r["paper_id"]: r for r in payload["rows"]}
    for pid, (decision, note, sections, theme, subtheme, concept) in DECISIONS.items():
        row = rows[pid]
        if row["taxonomy_review_state"] == "taxonomy-adjudicated":
            raise SystemExit(f"already adjudicated: {pid}")
        row.update({"taxonomy_review_state": "taxonomy-adjudicated", "final_decision": decision, "reviewer_note": note, "reviewed_sections": sections, "final_theme_id": theme, "final_subtheme_id": subtheme, "final_concept_id": concept})
    payload["adjudicated_count"] = sum(r["taxonomy_review_state"] == "taxonomy-adjudicated" for r in rows.values())
    payload["open_count"] = len(rows) - payload["adjudicated_count"]
    payload["decision_counts"] = {d: sum(r.get("final_decision") == d for r in rows.values() if r["taxonomy_review_state"] == "taxonomy-adjudicated") for d in sorted({r.get("final_decision") for r in rows.values() if r["taxonomy_review_state"] == "taxonomy-adjudicated"})}
    QUEUE.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({"batch": len(DECISIONS), "adjudicated": payload["adjudicated_count"], "open": payload["open_count"]}))

if __name__ == "__main__":
    main()
