#!/usr/bin/env python3
"""Record the next eight title-only D1 taxonomy adjudications."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "cm25_interspeech": ("reassigned-to-neighbor", "The title explicitly concerns emitted speech from a loudspeaker and its effect on automatic speech recognition. Title-only evidence places it under microphone and channel coloration rather than domain and context biasing.", "sound-and-production", "room-channel-and-sensing", "microphone-channel"),
    "coppietersdegibson25_interspeech": ("confirmed-current-boundary", "The title explicitly concerns auditory feedback mechanisms in speech recognition. Title-only evidence supports acoustic-to-token mapping, without establishing the proposed mechanism or recognition effect.", "recognition-and-alignment", "acoustic-unit-learning", "acoustic-to-token"),
    "cui25_interspeech": ("confirmed-current-boundary", "The title explicitly concerns contextual automatic speech recognition using self-supervised discrete speech features. Title-only evidence supports long-context decoding, without establishing context benefit or recognition quality.", "recognition-and-alignment", "context-and-open-vocabulary", "long-context-decoding"),
    "cumani25_interspeech": ("confirmed-current-boundary", "The title explicitly concerns classification backends for the NIST speaker-recognition evaluation. Title-only evidence supports speaker verification, without establishing backend performance.", "people-variation-and-health", "identity-and-life-stage", "speaker-verification"),
    "cumani25b_interspeech": ("confirmed-current-boundary", "The title explicitly concerns score-level fusion for speaker verification. Title-only evidence supports speaker verification, without establishing fusion benefit.", "people-variation-and-health", "identity-and-life-stage", "speaker-verification"),
    "cumlin25_interspeech": ("confirmed-current-boundary", "The title explicitly concerns probabilistic assessment of speech quality. Title-only evidence supports quality and naturalness, without establishing assessment validity.", "evaluation-deployment-and-consequence", "metric-and-human-targets", "quality-and-naturalness"),
    "damianos25_interspeech": ("confirmed-current-boundary", "The title explicitly concerns pseudo-labeling and self-supervision for unsupervised domain adaptation in automatic speech recognition. Title-only evidence supports self-training, without establishing adaptation quality.", "languages-accents-and-resources", "low-resource-learning", "self-training-and-pseudo-labels"),
    "dao25_interspeech": ("confirmed-current-boundary", "The title explicitly concerns instruction training for low-resource languages without speech in the training process. Title-only evidence supports few-shot adaptation, without establishing language coverage or transfer quality.", "languages-accents-and-resources", "low-resource-learning", "few-shot-adaptation"),
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
