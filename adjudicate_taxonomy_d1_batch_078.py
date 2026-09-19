#!/usr/bin/env python3
"""Record the next eight title-only D1 taxonomy adjudications."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "araizaillan25_interspeech": ("confirmed-current-boundary", "The title explicitly concerns recognition of vocal emotions in pseudospeech from cochlear-implanted adolescents. Title-only evidence supports paralinguistic state, without establishing emotion-recognition reliability or clinical benefit.", "meaning-and-interaction", "prosody-and-paralinguistics", "paralinguistic-state"),
    "arisoy25_interspeech": ("rejected-out-of-scope", "The title concerns language-model data generation for general question answering and does not establish a human-speech or spoken-language task. With title-only evidence, speech self-training membership is not supported.", None, None, None),
    "attia25_interspeech": ("reassigned-to-neighbor", "The title explicitly concerns noisy classroom speech transcripts and the value of accurate speech data. Title-only evidence places it under speech data collection rather than acoustic-to-token mapping.", "languages-accents-and-resources", "data-creation", "speech-data-collection"),
    "bagat25_interspeech": ("confirmed-current-boundary", "The title explicitly concerns multi-accent automatic speech recognition. Title-only evidence supports pronunciation variation, without establishing accent coverage or recognition robustness.", "recognition-and-alignment", "pronunciation-and-variation", "pronunciation-variation"),
    "baihaqi25_interspeech": ("reassigned-to-neighbor", "The title explicitly concerns rapport-building dialogue strategies, proactive behavior, and backchannels. Title-only evidence places it under interactional feedback rather than turn-boundary prediction.", "meaning-and-interaction", "grounding-and-action", "interactional-feedback"),
    "baihaqi25b_interspeech": ("confirmed-current-boundary", "The title explicitly concerns co-speech motion for virtual-agent dialogue. Title-only evidence supports interactional feedback, without establishing agent quality or user benefit.", "meaning-and-interaction", "grounding-and-action", "interactional-feedback"),
    "bakkouche25b_interspeech": ("confirmed-current-boundary", "The title explicitly concerns dynamic spectral cues in second-language vowel perception and production. Title-only evidence supports pronunciation variation, without establishing proficiency effects.", "recognition-and-alignment", "pronunciation-and-variation", "pronunciation-variation"),
    "balajishankar25_interspeech": ("reassigned-to-neighbor", "The title explicitly concerns child automatic speech recognition and speech-error correction. Title-only evidence places it under age and developmental speech rather than pronunciation variation.", "people-variation-and-health", "identity-and-life-stage", "age-and-development"),
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
