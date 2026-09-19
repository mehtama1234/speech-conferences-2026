#!/usr/bin/env python3
"""Record the twenty-eighth title-only D1 taxonomy adjudication batch."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "b04c9362530edcb037c03480a76189a4fe635815": ("confirmed-current-boundary", "The title explicitly concerns distilling attention knowledge for speaker verification. Title-only evidence supports speaker-verification membership.", "people-variation-and-health", "identity-and-life-stage", "speaker-verification"),
    "b0d7f13393cb3a8ed0e3fd7c9c00da894e0a2754": ("confirmed-current-boundary", "The title explicitly concerns cross-lingual Alzheimer's detection from speech cues. Title-only evidence supports a clinical speech marker, without establishing diagnostic validity.", "people-variation-and-health", "clinical-markers", "clinical-speech-marker"),
    "b0f4b9718fb0b578cc7236c65a2a742e83931dea": ("rejected-out-of-scope", "The title concerns hair-noise analysis in smart-glasses audio captures but does not establish human speech or a spoken-language task. With title-only evidence, changing-noise speech membership is not supported.", None, None, None),
    "b249b7629840361195fcb2c79dc1a8bca3a51add": ("confirmed-current-boundary", "The title explicitly concerns a neural speech codec with a built-in voice changer. Title-only evidence supports voice conversion.", "voice-generation-and-control", "identity-and-conversion", "voice-conversion"),
    "b25744f5c988198e254e671922ca4e1a5941bf52": ("reassigned-to-neighbor", "The title explicitly concerns far-field speech enhancement for speech-to-text. The direct boundary is speech-prior denoising rather than acoustic-to-token mapping.", "listening-and-separation", "noise-enhancement", "speech-prior-denoising"),
    "b27c042af6d047e396936a295e3faf84cb308daf": ("confirmed-current-boundary", "The title explicitly concerns ultra-fast utterance restoration. Title-only evidence supports perceptual enhancement.", "listening-and-separation", "perceptual-recovery", "perceptual-enhancement"),
    "b2988abe0d2256450a910514d500edbb9b99516f": ("confirmed-current-boundary", "The title explicitly concerns automatic stuttering detection. Title-only evidence supports a clinical or atypical-speech marker, without establishing diagnostic validity.", "people-variation-and-health", "clinical-markers", "clinical-speech-marker"),
    "b37f5532e67a880ba83401ac29659de4f4a504e3": ("confirmed-current-boundary", "The title explicitly concerns speech-based Alzheimer's detection. Title-only evidence supports a clinical speech marker, without establishing diagnostic validity.", "people-variation-and-health", "clinical-markers", "clinical-speech-marker"),
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
