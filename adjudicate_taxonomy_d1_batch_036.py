#!/usr/bin/env python3
"""Record the twenty-fifth title-only D1 taxonomy adjudication batch."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "9df0b5000a1dedc69a16a7d3cd12448a0f671fb5": ("confirmed-current-boundary", "The title explicitly concerns child speech recognition and developmental speech under label noise. Title-only evidence supports age and developmental speech.", "people-variation-and-health", "identity-and-life-stage", "age-and-development"),
    "9ebadcacaec354b601e244bb3c4e2f8fce18fb81": ("rejected-out-of-scope", "The title concerns general audio deepfake detection but does not establish synthetic speech or spoken-language evidence. With title-only evidence, speech spoofing membership is not supported.", None, None, None),
    "9ec1f211dc888682c1e78fed3de940cb022571b9": ("confirmed-current-boundary", "The title explicitly concerns segment- and time-aware decoding attention for models listening to speech. Title-only evidence supports long-context decoding.", "recognition-and-alignment", "context-and-open-vocabulary", "long-context-decoding"),
    "9f333419971c9db1df8c114ddde6a48da53caa87": ("rejected-out-of-scope", "The title concerns differential microphone-array design and spatial operators but does not establish a human-speech or spoken-language task. With title-only evidence, speech microphone membership is not supported.", None, None, None),
    "a05d08ade35fb3811e01e9d0cc75c0397eb98d2f": ("confirmed-current-boundary", "The title explicitly concerns speaker verification using WavLM representations and spectro-temporal modulation. Title-only evidence supports speaker-verification membership.", "people-variation-and-health", "identity-and-life-stage", "speaker-verification"),
    "a27f4499d459f32a571078f6b19651b2e776ffe9": ("confirmed-current-boundary", "The title explicitly concerns a speech-based screener for developmental language disorder. Title-only evidence supports a clinical speech marker, without establishing screening validity.", "people-variation-and-health", "clinical-markers", "clinical-speech-marker"),
    "a2e740f186e36314f5b460f579490cac44a30e7b": ("confirmed-current-boundary", "The title explicitly concerns adaptive filterbanks for robust speech processing. Title-only evidence supports multiple time scales in speech signal processing.", "sound-and-production", "time-frequency-measurement", "multi-resolution-signal"),
    "a3a2d0a03aaf90b18c3ea8db0a951bb3a2bed73a": ("confirmed-current-boundary", "The title explicitly concerns short-to-long speech transfer for a long-speech summarization framework. Title-only evidence supports long-context decoding.", "recognition-and-alignment", "context-and-open-vocabulary", "long-context-decoding"),
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
