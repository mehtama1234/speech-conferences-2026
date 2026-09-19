#!/usr/bin/env python3
"""Record the next eight title-only D1 taxonomy adjudications."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "ff6e1f8a6a937aa540f1130796f05fca9a4f7f98": ("confirmed-current-boundary", "The title explicitly concerns low-resource neural speech coding and enhancement. Title-only evidence supports perceptual enhancement, without establishing enhancement or coding quality.", "listening-and-separation", "perceptual-recovery", "perceptual-enhancement"),
    "ahmed25_interspeech": ("confirmed-current-boundary", "The title explicitly concerns speech assessment using visual cues. Title-only evidence supports listener effort, without establishing the assessment's perceptual validity.", "people-variation-and-health", "human-centered-accessibility", "listener-effort"),
    "ahn25b_interspeech": ("rejected-out-of-scope", "The title concerns semantic alignment and captioning for general automated audio captions, not a human-speech or spoken-language task. With title-only evidence, speech quality and naturalness membership is not supported.", None, None, None),
    "alam25_interspeech": ("reassigned-to-neighbor", "The title explicitly concerns multilingual everyday spoken queries. Title-only evidence places it under cross-lingual transfer rather than code-switching, because code mixing is not named.", "languages-accents-and-resources", "crosslingual-structure", "crosslingual-transfer"),
    "alexos25_interspeech": ("reassigned-to-neighbor", "The title explicitly concerns adversarial jailbreak threats against speech-enabled language models. Title-only evidence places it under distribution shift and robustness rather than end-to-end recovery.", "evaluation-deployment-and-consequence", "robustness-and-shift", "distribution-shift"),
    "ali25_interspeech": ("confirmed-current-boundary", "The title explicitly concerns collecting and annotating a speech deepfake dataset. Title-only evidence supports spoofing and deepfake detection, without establishing dataset quality or detection performance.", "evaluation-deployment-and-consequence", "privacy-and-security", "spoofing-and-deepfake"),
    "altwlkany25_interspeech": ("confirmed-current-boundary", "The title explicitly concerns speech carried through PSTN, VoIP, and neural audio codecs, with language and gender effects. Title-only evidence supports microphone and channel coloration, without establishing channel robustness.", "sound-and-production", "room-channel-and-sensing", "microphone-channel"),
    "ankita25_interspeech": ("reassigned-to-neighbor", "The title explicitly concerns children's automatic speech recognition under limited data. Title-only evidence places it under age and developmental speech rather than multiple-time-scale measurement.", "people-variation-and-health", "identity-and-life-stage", "age-and-development"),
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
