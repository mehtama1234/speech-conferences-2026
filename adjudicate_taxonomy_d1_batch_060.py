#!/usr/bin/env python3
"""Record the next eight title-only D1 taxonomy adjudications."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "bcb97164784540986701bd9ed5ff048012da1bea": ("confirmed-current-boundary", "The title explicitly concerns vocal-effort classification in naturalistic speech recordings. Title-only evidence supports within-speaker state variation, without establishing effort-classification accuracy.", "people-variation-and-health", "identity-and-life-stage", "style-and-state-variation"),
    "bd2bacf64a664b31d493bd21ad3563b32fd89be6": ("confirmed-current-boundary", "The title explicitly concerns pitch estimation and temporal alignment. Title-only evidence supports the periodic vocal-fold source, without establishing pitch-estimation accuracy.", "sound-and-production", "source-generation", "periodic-source"),
    "bd6d4e8e756650f5ef36e5b73e91ca1c5ca1ceae": ("confirmed-current-boundary", "The title explicitly concerns Fréchet speech distance for synthetic-speech quality evaluation. Title-only evidence supports quality and naturalness, without establishing metric validity.", "evaluation-deployment-and-consequence", "metric-and-human-targets", "quality-and-naturalness"),
    "be2217792263f6dc8cf26815c828b6e7ce0c1133": ("confirmed-current-boundary", "The title explicitly concerns nonparallel voice conversion. Title-only evidence supports voice conversion, without establishing conversion quality or speaker preservation.", "voice-generation-and-control", "identity-and-conversion", "voice-conversion"),
    "be2261eafa31bece124a3279984e93640376f60d": ("reassigned-to-neighbor", "The title explicitly concerns a neural vocoder for high-quality speech generation. Title-only evidence places it under neural vocoder rather than the broader waveform-synthesis label.", "voice-generation-and-control", "waveform-and-codec-generation", "neural-vocoder"),
    "be3257200948d26ec885299c4174474ffd8a6d86": ("rejected-out-of-scope", "The title concerns general audio-video correspondence pretraining and does not establish a human-speech or spoken-language task. With title-only evidence, cross-lingual transfer membership is not supported.", None, None, None),
    "bf6c53ec9bca47fd8f79b7d4b3e3f4b0ce9aeb3f": ("rejected-out-of-scope", "The title concerns text-audio relevance for a general text-to-audio system and does not establish a human-speech or spoken-language task. With title-only evidence, speech calibration membership is not supported.", None, None, None),
    "bff2f73d8ce84e17eb7b7ee9f6cebdd6a8d89b68": ("rejected-out-of-scope", "The title concerns beamformer combinations for generic target-source extraction and does not establish a human-speech or spoken-language task. With title-only evidence, speech source-separation membership is not supported.", None, None, None),
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
