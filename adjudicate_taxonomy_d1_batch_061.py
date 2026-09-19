#!/usr/bin/env python3
"""Record the next eight title-only D1 taxonomy adjudications."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "c17ba845024c6779c20c90ab07312fa23a3b62f2": ("confirmed-current-boundary", "The title explicitly concerns online speech models and the absence of future context. Title-only evidence supports long-context decoding, without establishing streaming recognition quality.", "recognition-and-alignment", "context-and-open-vocabulary", "long-context-decoding"),
    "c249f101eedb0599e84b79c3a828d772c0329975": ("confirmed-current-boundary", "The title explicitly concerns scalable zero-shot voice identity morphing. Title-only evidence supports unseen-speaker synthesis, without establishing identity preservation or synthesis quality.", "voice-generation-and-control", "identity-and-conversion", "zero-shot-voice"),
    "c2c0cdb7d276f6564100d556eef163d0f7d2a2ad": ("rejected-out-of-scope", "The title concerns single-microphone point-source localization from reverberation and does not establish a human-speech or spoken-language task. With title-only evidence, reverberant speech-room membership is not supported.", None, None, None),
    "c3cee23f9184a1952fbacb69b7575bd4dac89e46": ("reassigned-to-neighbor", "The title explicitly concerns personalized multi-speaker automatic speech recognition using contextual acoustic-linguistic modeling. Title-only evidence places it under speaker adaptation rather than blind source separation.", "recognition-and-alignment", "context-and-open-vocabulary", "speaker-adaptation"),
    "c3d264865e4a492f7bae1683da3eaa73a07fa530": ("confirmed-current-boundary", "The title explicitly concerns unsupervised training in speech recognition. Title-only evidence supports learned speech units, without establishing the theoretical result's practical usefulness.", "recognition-and-alignment", "acoustic-unit-learning", "self-supervised-speech-units"),
    "c4379d42d8661bae8f488b9ee1b18cc1da44211b": ("confirmed-current-boundary", "The title explicitly concerns multimodal speech enhancement using bone-conduction guidance. Title-only evidence supports time-frequency masking, without establishing enhancement quality or benefit from the guidance signal.", "listening-and-separation", "noise-enhancement", "spectral-mask"),
    "c58bc96ddde807522805298f0a5887c2c8a5033d": ("rejected-out-of-scope", "The title explicitly concerns multi-stem music generation rather than a human-speech or spoken-language task. It is outside this speech taxonomy.", None, None, None),
    "c5eba686c4f670eb5194c4a9a9b955044130ab88": ("rejected-out-of-scope", "The title concerns a general audio-visual quality-assessment dataset and does not establish a human-speech or spoken-language task. With title-only evidence, listener effort membership is not supported.", None, None, None),
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
