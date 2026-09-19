#!/usr/bin/env python3
"""Record the fifteenth title-only D1 taxonomy adjudication batch."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "590b4443111d0b760b47b74f729c0a71fbc832ec": ("confirmed-current-boundary", "The title explicitly concerns multichannel speech enhancement under low-SNR conditions. Title-only evidence supports speech-prior denoising.", "listening-and-separation", "noise-enhancement", "speech-prior-denoising"),
    "59678d7c13e23f643251fdb4594067d07a3080ed": ("rejected-out-of-scope", "The title concerns a general audio watermarking algorithm and does not establish speech or spoken-language evidence. With title-only evidence, speech accountability membership is not supported.", None, None, None),
    "5b41e3c200362ac9e517bd4e74e895d503ca09f2": ("confirmed-current-boundary", "The title explicitly concerns depression detection from speech. Title-only evidence supports a clinical speech marker, without establishing diagnostic validity.", "people-variation-and-health", "clinical-markers", "clinical-speech-marker"),
    "5ca505f745b70f6d9a849aeb917685c67d1847fd": ("rejected-out-of-scope", "The title concerns audio-text apparent-personality analysis but does not establish human speech or a spoken-language task. With title-only evidence, paralinguistic membership is not supported.", None, None, None),
    "5d33f0b903d577c6144ed4ad9fd2b2cc64b44075": ("confirmed-current-boundary", "The title explicitly concerns speech emotion recognition. Title-only evidence supports paralinguistic-state membership.", "meaning-and-interaction", "prosody-and-paralinguistics", "paralinguistic-state"),
    "5d56f20a7561ff30d93ea82f974d742e784bc77b": ("confirmed-current-boundary", "The title explicitly concerns multichannel speech enhancement. Title-only evidence supports time-frequency masking within noise enhancement.", "listening-and-separation", "noise-enhancement", "spectral-mask"),
    "5dcb315487049d194ce0336e8a536496085c4bd4": ("confirmed-current-boundary", "The title explicitly concerns speech and speaker-attribute recognition using Whisper. Title-only evidence supports within-speaker state and attribute variation.", "people-variation-and-health", "identity-and-life-stage", "style-and-state-variation"),
    "5dd522f2b7bd4e4bd512d307db75d988fe9e2cb5": ("rejected-out-of-scope", "The title concerns natural-language control of spatial-audio rendering for creative authoring but does not establish a human-speech or spoken-language task. With title-only evidence, speech-act membership is not supported.", None, None, None),
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
