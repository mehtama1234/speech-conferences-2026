#!/usr/bin/env python3
"""Record the next eight title-only D1 taxonomy adjudications."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "5677bfc89f30ef9e06729ba52f257b7af59a6b8d": ("confirmed-current-boundary", "The title explicitly concerns knowledge distillation for speaker verification. Title-only evidence supports speaker-verification membership, without establishing verification accuracy.", "people-variation-and-health", "identity-and-life-stage", "speaker-verification"),
    "56fb34a88cc772f834eb425f5454776d76080ba3": ("rejected-out-of-scope", "The title concerns audio hallucination in egocentric video understanding but does not establish a human-speech or spoken-language task. With title-only evidence, perceptual enhancement membership is not supported.", None, None, None),
    "586bebb49a0f4a50d2c53c004ee62800fad5a203": ("confirmed-current-boundary", "The title explicitly concerns language-audio pretraining with variable-duration audio and multiple objectives. Title-only evidence supports cross-lingual transfer, without establishing transfer quality for a particular language pair.", "languages-accents-and-resources", "crosslingual-structure", "cross-lingual-transfer"),
    "5996ad2b4891379fb11b0afd2aaad8917fe5c967": ("confirmed-current-boundary", "The title explicitly concerns fast single-channel speech enhancement. Title-only evidence supports speech-prior denoising, without establishing robustness across noise conditions.", "listening-and-separation", "noise-enhancement", "speech-prior-denoising"),
    "5a109e50b405f8765120a5b100864e3edd2fa7fd": ("confirmed-current-boundary", "The title explicitly concerns Arabic dialect identification for streaming applications. Title-only evidence supports dialect and variety membership, without establishing coverage of Arabic varieties.", "languages-accents-and-resources", "accent-dialect-and-cultural-meaning", "dialect-and-variety"),
    "5bca16ffa799b2ac9e52b68737ef9e780915df10": ("confirmed-current-boundary", "The title explicitly concerns a hierarchical-margin method for speaker verification. Title-only evidence supports speaker-verification membership, without establishing the claimed hierarchy's benefit.", "people-variation-and-health", "identity-and-life-stage", "speaker-verification"),
    "5c6d33c016ff873656d61f4c257948fc75ec30b5": ("confirmed-current-boundary", "The title explicitly concerns generative refinement for multichannel speech enhancement. Title-only evidence supports microphone and channel coloration, without establishing real-world enhancement quality.", "sound-and-production", "room-channel-and-sensing", "microphone-and-channel-coloration"),
    "5ec8a32bb2cff662b1eafde87a14775ee696a204": ("rejected-out-of-scope", "The title explicitly concerns AI-generated music detection rather than a human-speech or spoken-language object. It is outside this speech taxonomy.", None, None, None),
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
