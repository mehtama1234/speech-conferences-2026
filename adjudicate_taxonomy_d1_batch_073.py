#!/usr/bin/env python3
"""Record the next eight title-only D1 taxonomy adjudications."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "f36b52dbf53f9d5a57c3c4834150c703d5123be8": ("confirmed-current-boundary", "The title explicitly asks whether speech language models learn crossmodal embedding spaces. Title-only evidence supports referential grounding, without establishing grounding behavior or benchmark performance.", "meaning-and-interaction", "grounding-and-action", "referential-grounding"),
    "f41ec924916b88a1a0215218cfa566185a475a2c": ("confirmed-current-boundary", "The title explicitly concerns a low-bitrate speech codec with inter-band prediction. Title-only evidence supports sampling and quantization, without establishing codec quality or bitrate tradeoffs.", "sound-and-production", "time-frequency-measurement", "sampling-and-quantization"),
    "f4290ddf1ba7726c19fbab4515c22dd49eac9650": ("confirmed-current-boundary", "The title explicitly concerns accent-aware language identification for multilingual speech recognition. Title-only evidence supports language and variety identification, without establishing identification robustness.", "languages-accents-and-resources", "crosslingual-structure", "language-identification"),
    "f45b71835dbeba1ae340561e72cbe6dde771bd02": ("confirmed-current-boundary", "The title explicitly concerns a proactive voice memory assistant operating in real time. Title-only evidence supports dialogue state, without establishing memory accuracy or assistant usefulness.", "meaning-and-interaction", "intent-and-dialogue-state", "dialogue-state"),
    "f471420095c3cabfdeece782cac28d8eecb64fdc": ("confirmed-current-boundary", "The title explicitly concerns multilingual speech enhancement evaluated with listening tests. Title-only evidence supports quality and naturalness, without establishing perceptual results.", "evaluation-deployment-and-consequence", "metric-and-human-targets", "quality-and-naturalness"),
    "f4812e23e13ef4174a9f09890c6c67aabb47c6af": ("confirmed-current-boundary", "The title explicitly concerns efficient fine-tuning for speech tasks with input-adaptive ranks. Title-only evidence supports few-shot adaptation, without establishing adaptation efficiency or task coverage.", "languages-accents-and-resources", "low-resource-learning", "few-shot-adaptation"),
    "f48789d81eb50bf2bf625fe35e4c5b262f5e5c3c": ("confirmed-current-boundary", "The title explicitly concerns benchmarking human-like spoken dialogue systems. Title-only evidence supports dialogue state, without establishing human-likeness or benchmark validity.", "meaning-and-interaction", "intent-and-dialogue-state", "dialogue-state"),
    "f516350d0a48d2df969ceabe40cafea5e090fbc8": ("confirmed-current-boundary", "The title explicitly concerns emotional talking-face synthesis with an emotion prior. Title-only evidence supports style and emotion control, without establishing perceptual quality or emotional consistency.", "voice-generation-and-control", "expression-and-interactive-control", "style-and-emotion-control"),
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
