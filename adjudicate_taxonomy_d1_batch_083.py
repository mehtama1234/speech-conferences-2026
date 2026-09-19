#!/usr/bin/env python3
"""Record the next eight title-only D1 taxonomy adjudications."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "chang25d_interspeech": ("confirmed-current-boundary", "The title explicitly concerns resource barriers in speech-emotion recognition and uses data distillation. Title-only evidence supports latency and resource budget, without establishing the resource tradeoff or recognition quality.", "evaluation-deployment-and-consequence", "deployment-cost", "latency-and-resource"),
    "charuau25_interspeech": ("confirmed-current-boundary", "The title explicitly concerns hand gestures and pauses in multiparty interactions. Title-only evidence supports turn-boundary prediction, without establishing interactional timing performance.", "meaning-and-interaction", "turn-taking-and-repair", "turn-boundary"),
    "chatzichristodoulou25_interspeech": ("reassigned-to-neighbor", "The title explicitly concerns speech-emotion recognition in naturalistic conditions. Title-only evidence places it under paralinguistic state rather than intent in context.", "meaning-and-interaction", "prosody-and-paralinguistics", "paralinguistic-state"),
    "cheema25_interspeech": ("reassigned-to-neighbor", "The title explicitly concerns hearing loss and cochlear neural degeneration in a speech-related auditory model. Title-only evidence places it under accessibility fit rather than pronunciation variation.", "people-variation-and-health", "human-centered-accessibility", "accessibility-fit"),
    "chen25_interspeech": ("confirmed-current-boundary", "The title explicitly concerns speaker recognition under intrinsic variation. Title-only evidence supports within-speaker state variation, without establishing robustness or tuning benefit.", "people-variation-and-health", "identity-and-life-stage", "style-and-state-variation"),
    "chen25c_interspeech": ("reassigned-to-neighbor", "The title explicitly concerns perception of emotional speech by people with borderline personality features. Title-only evidence places it under style and state variation rather than clinical speech marker.", "people-variation-and-health", "identity-and-life-stage", "style-and-state-variation"),
    "chen25d_interspeech": ("rejected-out-of-scope", "The title explicitly concerns singing voice conversion rather than a human-speech or spoken-language task. It is outside this speech taxonomy.", None, None, None),
    "chen25e_interspeech": ("reassigned-to-neighbor", "The title explicitly concerns decoding pitch from EEG during Mandarin speech perception. Title-only evidence places it under non-airborne sensing rather than acoustic-to-token mapping.", "sound-and-production", "room-channel-and-sensing", "non-airborne-sensing"),
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
