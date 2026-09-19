#!/usr/bin/env python3
"""Record the third title-only D1 taxonomy adjudication batch."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "0e52cf0c4e007e1c0447027fbaae848bcd1230ab": ("confirmed-current-boundary", "The title explicitly concerns speaker verification. Title-only evidence supports speaker-verification membership.", "people-variation-and-health", "identity-and-life-stage", "speaker-verification"),
    "117a8b68fd57479a0c241bcafe4f407bca83de11": ("rejected-out-of-scope", "The title concerns acoustic feedback cancellation in hearing aids but does not establish a human-speech or spoken-language task. With title-only evidence, speech membership is not supported.", None, None, None),
    "11b7584c9eb86153649dc9087c684705a7a4b513": ("confirmed-current-boundary", "The title explicitly concerns multi-label speech emotion recognition. Title-only evidence supports paralinguistic-state membership, without claims about emotion-label validity.", "meaning-and-interaction", "prosody-and-paralinguistics", "paralinguistic-state"),
    "11dd56ef7b05565fa42406dd90eded7f33fb8d14": ("rejected-out-of-scope", "The title concerns binaural sound-source localization and does not establish a human-speech or spoken-language task. With title-only evidence, speech membership is not supported.", None, None, None),
    "12846ec5114c69222d0e85aa9eb2ff6915835336": ("reassigned-to-neighbor", "The title explicitly concerns automatic speech recognition under drone noise and distortions from speech enhancement. Title-only evidence supports robustness to distribution shift more directly than acoustic-to-token mapping.", "evaluation-deployment-and-consequence", "robustness-and-shift", "distribution-shift"),
    "12926467a7c78a140099849f25e173349dc9e88f": ("confirmed-current-boundary", "The title explicitly concerns Parkinson's detection from speech descriptors. Title-only evidence supports clinical-speech-marker membership, without establishing medical validity.", "people-variation-and-health", "clinical-markers", "clinical-speech-marker"),
    "13058f7ce84fd16da34a06922ca6ed2152230c12": ("confirmed-current-boundary", "The title explicitly concerns neural speech coding. Title-only evidence supports sampling-and-quantization membership.", "sound-and-production", "time-frequency-measurement", "sampling-and-quantization"),
    "137d39469bbb18ae92c5c08a1029e0f4ea202d5a": ("rejected-out-of-scope", "The title concerns audio-driven facial animation and emotion control but does not establish a human-speech or spoken-language task. With title-only evidence, speech membership is not supported.", None, None, None),
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
