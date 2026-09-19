#!/usr/bin/env python3
"""Record the twentieth title-only D1 taxonomy adjudication batch."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "7719a913ac5a504fef4a6d06263c7bff8cb8aff4": ("confirmed-current-boundary", "The title explicitly concerns brain-assisted speech enhancement in multi-speaker conditions. Title-only evidence supports speech-prior denoising.", "listening-and-separation", "noise-enhancement", "speech-prior-denoising"),
    "77c4d4bf79700812d57e4f020e01f17c997d0414": ("confirmed-current-boundary", "The title explicitly concerns acoustic echo cancellation. Title-only evidence supports acoustic-echo cancellation.", "listening-and-separation", "echo-reconstruction", "acoustic-echo-cancellation"),
    "782606c69daf2ddd2a3657d0861af3f7517dc192": ("confirmed-current-boundary", "The title explicitly concerns speech emotion recognition. Title-only evidence supports paralinguistic-state membership.", "meaning-and-interaction", "prosody-and-paralinguistics", "paralinguistic-state"),
    "78329b6217b8a008c04b46108b02f51dc6f09463": ("rejected-out-of-scope", "The title concerns 3D sound-source mapping with camera-microphone geometry but does not establish a human-speech or spoken-language task. With title-only evidence, speech microphone membership is not supported.", None, None, None),
    "78d3f7d76084a19f984595afa028650e19bb24c8": ("confirmed-current-boundary", "The title explicitly concerns speech enhancement in reverberant multi-source environments using spatial covariance. Title-only evidence supports spatial filtering.", "listening-and-separation", "spatial-listening", "spatial-filtering"),
    "7920a44df49aad7f0dc970d6d296c88a31369af5": ("reassigned-to-neighbor", "The title explicitly concerns separating similar speakers, which is a source-separation task rather than speaker verification. Title-only evidence supports target-conditioned separation.", "listening-and-separation", "source-separation", "target-conditioned-separation"),
    "7a23faa2eea5435d7829709e849c526da9c4223a": ("confirmed-current-boundary", "The title explicitly compares visual grounding effects for speech- and text-based language encoders. Title-only evidence supports referential grounding.", "meaning-and-interaction", "grounding-and-action", "referential-grounding"),
    "7b3746f1a67c4f24e95c987ff84a012e5eb49df4": ("rejected-out-of-scope", "The title concerns audio-language-model behavior in clinical decision-making but does not establish a clinical speech marker or human-speech task. With title-only evidence, speech membership is not supported.", None, None, None),
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
