#!/usr/bin/env python3
"""Record the next eight title-only D1 taxonomy adjudications."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "a145addd7b1843272a7bfc65d102190b561f9d09": ("reassigned-to-neighbor", "The title explicitly concerns speech enhancement for cochlear-implant recipients. Title-only evidence places it under accessibility fit rather than atypical articulation and dysarthria.", "people-variation-and-health", "human-centered-accessibility", "accessibility-fit"),
    "a1d1037b6e7b1e0856a34aa5bd9628edc58777ff": ("rejected-out-of-scope", "The title concerns event classification from distributed acoustic sensors with degraded channels but does not establish a human-speech or spoken-language task. With title-only evidence, microphone and channel coloration for speech is not supported.", None, None, None),
    "a3fc7ede7606bcc85119bcd941e2c596004f096f": ("confirmed-current-boundary", "The title explicitly concerns text-to-speech with cross-lingual voice cloning and an unseen-speaker setting. Title-only evidence supports unseen-speaker synthesis, without establishing cloning quality or speaker generalization.", "voice-generation-and-control", "identity-and-conversion", "zero-shot-voice"),
    "a47b1a73d88765889f990bf782d23ccd6df47c33": ("confirmed-current-boundary", "The title explicitly concerns speaker verification and angular-margin scoring. Title-only evidence supports speaker verification, without establishing the proposed margin fix's benefit.", "people-variation-and-health", "identity-and-life-stage", "speaker-verification"),
    "a52a797dcf4739a2b8ce20d26b390753b658e408": ("confirmed-current-boundary", "The title explicitly concerns a conformer architecture for automatic speech recognition. Title-only evidence supports acoustic-to-token mapping, without establishing the modality-aware mixture's effect.", "recognition-and-alignment", "acoustic-unit-learning", "acoustic-to-token"),
    "a71a0571289f6bbf269b58ccbebf64200a5a6014": ("rejected-out-of-scope", "The title concerns perceptual quality assessment for singing-face generation rather than a human-speech or spoken-language task. With title-only evidence, accessibility fit is not supported.", None, None, None),
    "a754babfcb3be7d7b368a9de72a60217d919f900": ("confirmed-current-boundary", "The title explicitly concerns self-supervised speech encoders. Title-only evidence supports learned speech units, without establishing representation quality or downstream transfer.", "recognition-and-alignment", "acoustic-unit-learning", "self-supervised-speech-units"),
    "a865cfc4e91bf5c478e2dc62ae4b33c0d0c480fa": ("reassigned-to-neighbor", "The title explicitly concerns speaker-attributed automatic speech recognition and speech-aware language models. Title-only evidence places it under speaker adaptation rather than long-context decoding.", "recognition-and-alignment", "context-and-open-vocabulary", "speaker-adaptation"),
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
