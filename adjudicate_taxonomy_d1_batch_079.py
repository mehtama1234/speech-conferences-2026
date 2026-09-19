#!/usr/bin/env python3
"""Record the next eight title-only D1 taxonomy adjudications."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "barahona25_interspeech": ("reassigned-to-neighbor", "The title identifies the NIST speaker-recognition evaluation and concerns audio-system recognition. Title-only evidence places it under speaker verification rather than dialogue state.", "people-variation-and-health", "identity-and-life-stage", "speaker-verification"),
    "baser25b_interspeech": ("confirmed-current-boundary", "The title explicitly concerns language-driven speech deepfake manipulation and detection. Title-only evidence supports spoofing and deepfake detection, without establishing realism or detector performance.", "evaluation-deployment-and-consequence", "privacy-and-security", "spoofing-and-deepfake"),
    "batchelderschwab25_interspeech": ("confirmed-current-boundary", "The title explicitly concerns stress in spoken Greek, with a comparison to whistled Greek. Title-only evidence supports prosodic meaning, without establishing the linguistic or acoustic interpretation of stress.", "meaning-and-interaction", "prosody-and-paralinguistics", "prosodic-meaning"),
    "battula25_interspeech": ("confirmed-current-boundary", "The title explicitly concerns a physiological proxy for confidence in spoken speech. Title-only evidence supports paralinguistic state, without establishing proxy validity or confidence measurement quality.", "meaning-and-interaction", "prosody-and-paralinguistics", "paralinguistic-state"),
    "bendom25_interspeech": ("reassigned-to-neighbor", "The title explicitly concerns an emotional speech database from speakers with Parkinson's disease. Title-only evidence places it under clinical speech markers rather than multiple-time-scale measurement.", "people-variation-and-health", "clinical-markers", "clinical-speech-marker"),
    "bentum25_interspeech": ("confirmed-current-boundary", "The title explicitly concerns word stress in self-supervised speech models across languages. Title-only evidence supports learned speech units, without establishing model or cross-linguistic performance.", "recognition-and-alignment", "acoustic-unit-learning", "self-supervised-speech-units"),
    "berthommier25_interspeech": ("confirmed-current-boundary", "The title explicitly concerns articulatory modeling of formant trajectories in VCV syllables. Title-only evidence supports articulatory coordination, without establishing the model's articulatory accuracy.", "sound-and-production", "articulatory-dynamics", "articulatory-coordination"),
    "bhattacharya25b_interspeech": ("rejected-out-of-scope", "The title concerns temporal reasoning in general language-audio models and does not establish a human-speech or spoken-language task. With title-only evidence, calibration and selective use for speech is not supported.", None, None, None),
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
