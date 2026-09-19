#!/usr/bin/env python3
"""Record the next eight title-only D1 taxonomy adjudications."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "72193e2de974d08717ef4ef9e4033c7db6e68d7d": ("confirmed-current-boundary", "The title explicitly concerns neural speech coding at an ultra-low bitrate. Title-only evidence supports multiple-time-scale analysis of the coding problem, without establishing coding quality or rate performance.", "sound-and-production", "time-frequency-measurement", "multiple-time-scales"),
    "724a162c2cd60edb3d14a1aa575359d6bcecc1ef": ("confirmed-current-boundary", "The title explicitly concerns codec-driven speech separation. Title-only evidence supports target-conditioned separation, without establishing separation quality or conditioning behavior.", "listening-and-separation", "source-separation", "target-conditioned-separation"),
    "7253661de1048019e9ea23e395e6c83b4d52bc79": ("rejected-out-of-scope", "The title concerns general audio captioning and modality-gap bridging but does not establish a human-speech or spoken-language task. With title-only evidence, referential grounding membership is not supported.", None, None, None),
    "72b137d1a17c46f657bf82dbc88703bc4c507dbf": ("rejected-out-of-scope", "The title concerns audio-language-model training for the XACLE challenge but does not establish a human-speech or spoken-language task. With title-only evidence, cross-lingual transfer membership is not supported.", None, None, None),
    "74e68c5d13e9a3baf621a5ebd856a2ef6b3676ca": ("rejected-out-of-scope", "The title explicitly concerns music rather than a human-speech or spoken-language task. It is outside this speech taxonomy.", None, None, None),
    "7571ad7c1a0af585d9ad7d04ea3ef3cfb1e82d5f": ("confirmed-current-boundary", "The title explicitly concerns emotion-aware speech synthesis. Title-only evidence supports paralinguistic state, without establishing emotion-recognition or synthesis quality.", "meaning-and-interaction", "prosody-and-paralinguistics", "paralinguistic-state"),
    "77b077287ef1fad8c8334d9dd24d916ea6eec144": ("reassigned-to-neighbor", "The title explicitly concerns cross-domain speech restoration guided by degradation priors. Title-only evidence places it under speech-prior denoising rather than domain and context biasing.", "listening-and-separation", "noise-enhancement", "speech-prior-denoising"),
    "77ce1ad011b2fc3fade0dd1a7161d198746d7ad6": ("confirmed-current-boundary", "The title explicitly concerns EMG-to-speech for an assistive communication setting. Title-only evidence supports augmentative communication, without establishing intelligibility or user benefit.", "people-variation-and-health", "atypical-and-assistive-speech", "augmentative-communication"),
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
