#!/usr/bin/env python3
"""Record the tenth abstract-bounded D2 taxonomy adjudication batch."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "3ec73fac05e9ba3126f22c06398cbda8c5a63958": ("confirmed-current-boundary", "The abstract explicitly studies few-shot open-set speaker identification and verification-style error rates. D2 supports speaker-verification membership.", "people-variation-and-health", "identity-and-life-stage", "speaker-verification"),
    "3fb899f3708fb35f2de35edc4e670e3d18a05581": ("rejected-out-of-scope", "The abstract concerns extension and morphing of general stationary sounds with a generative audio model, not human speech or spoken-language evidence.", None, None, None),
    "410eca01a4f0a09f9220ebcd502ad2431b1abe01": ("rejected-out-of-scope", "The abstract concerns semantic enhancement for compressed video and visual perceptual quality, not speech evidence or a spoken-language task.", None, None, None),
    "412b2762028b666985f4832aea40a2848b01547b": ("confirmed-current-boundary", "The abstract explicitly targets attended-speaker selection in multi-talker speech enhancement using gaze and facial evidence. D2 supports target-conditioned separation membership.", "listening-and-separation", "source-separation", "target-conditioned-separation"),
    "43737c2851b028c44c9d08aee1d52c5000014a7d": ("confirmed-current-boundary", "The abstract explicitly studies test-time adaptation of speech enhancement under unseen environmental domain shifts. D2 supports distribution-shift membership.", "evaluation-deployment-and-consequence", "robustness-and-shift", "distribution-shift"),
    "454db90b70ea3dd1da6a572e15cadd201a6e82e4": ("reassigned-to-neighbor", "The abstract explicitly addresses streaming speaker anonymization and protection of speaker identity. The speech-specific privacy boundary is voice privacy rather than unseen-speaker synthesis.", "evaluation-deployment-and-consequence", "privacy-and-security", "voice-privacy"),
    "45f5c2a0fc3b163760566e98edb3aa88706077c2": ("rejected-out-of-scope", "The abstract concerns general audio question answering and multimodal model calibration; it does not establish a human-speech or spoken-language task.", None, None, None),
    "4811d23ab656972dc064f2e83a627f857d72aa63": ("confirmed-current-boundary", "The abstract explicitly targets attended-speaker separation for cochlear-implant processing using EEG attention cues. D2 supports target-conditioned separation membership.", "listening-and-separation", "source-separation", "target-conditioned-separation"),
}

def main():
    payload = json.loads(QUEUE.read_text())
    rows = {r["paper_id"]: r for r in payload["rows"]}
    for pid, (decision, note, theme, subtheme, concept) in DECISIONS.items():
        row = rows[pid]
        if row["taxonomy_review_state"] == "taxonomy-adjudicated":
            raise SystemExit(f"already adjudicated: {pid}")
        row.update({"taxonomy_review_state": "taxonomy-adjudicated", "final_decision": decision, "reviewer_note": note, "reviewed_sections": ["title", "abstract"], "final_theme_id": theme, "final_subtheme_id": subtheme, "final_concept_id": concept})
    payload["adjudicated_count"] = sum(r["taxonomy_review_state"] == "taxonomy-adjudicated" for r in rows.values())
    payload["open_count"] = len(rows) - payload["adjudicated_count"]
    payload["decision_counts"] = {d: sum(r.get("final_decision") == d for r in rows.values() if r["taxonomy_review_state"] == "taxonomy-adjudicated") for d in sorted({r.get("final_decision") for r in rows.values() if r["taxonomy_review_state"] == "taxonomy-adjudicated"})}
    QUEUE.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({"batch": len(DECISIONS), "adjudicated": payload["adjudicated_count"], "open": payload["open_count"]}))

if __name__ == "__main__":
    main()
