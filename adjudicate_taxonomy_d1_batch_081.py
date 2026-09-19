#!/usr/bin/env python3
"""Record the next eight title-only D1 taxonomy adjudications."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "bressensdorf25_interspeech": ("rejected-out-of-scope", "The title concerns agent-based modeling and sound change in regional varieties but does not establish a human-speech or spoken-language processing task. With title-only evidence, age and developmental speech membership is not supported.", None, None, None),
    "broughton25_interspeech": ("confirmed-current-boundary", "The title explicitly concerns end-to-end speaker diarization. Title-only evidence supports end-to-end recovery, without establishing diarization accuracy or robustness.", "evaluation-deployment-and-consequence", "robustness-and-shift", "end-to-end-recovery"),
    "buech25_interspeech": ("confirmed-current-boundary", "The title explicitly concerns formant patterns of labialization and pharyngealization in a spoken language. Title-only evidence supports vocal-tract filtering, without establishing the articulatory-acoustic equivalence.", "sound-and-production", "source-generation", "vocal-tract-filter"),
    "burkhardt25_interspeech": ("reassigned-to-neighbor", "The title explicitly concerns a database of emotional speech. Title-only evidence places it under paralinguistic state rather than prosodic meaning.", "meaning-and-interaction", "prosody-and-paralinguistics", "paralinguistic-state"),
    "cao25_interspeech": ("confirmed-current-boundary", "The title explicitly concerns tone production by children from dialect-speaking regions. Title-only evidence supports age and developmental speech, without establishing the production differences.", "people-variation-and-health", "identity-and-life-stage", "age-and-development"),
    "cappellazzo25_interspeech": ("reassigned-to-neighbor", "The title explicitly concerns audio-visual speech recognition and sparse projector mixtures. Title-only evidence places it under acoustic-to-token mapping rather than speech-prior denoising.", "recognition-and-alignment", "acoustic-unit-learning", "acoustic-to-token"),
    "carta25_interspeech": ("reassigned-to-neighbor", "The title explicitly concerns a speech-recognition dataset for Sardinian languages. Title-only evidence places it under speech data collection rather than pronunciation variation.", "languages-accents-and-resources", "data-creation", "speech-data-collection"),
    "carvalho25_interspeech": ("reassigned-to-neighbor", "The title explicitly concerns long-form automatic speech recognition. Title-only evidence places it under long-context decoding rather than word error versus understanding.", "recognition-and-alignment", "context-and-open-vocabulary", "long-context-decoding"),
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
