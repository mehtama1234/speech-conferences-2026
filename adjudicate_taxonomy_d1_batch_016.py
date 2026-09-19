#!/usr/bin/env python3
"""Record the fifth title-only D1 taxonomy adjudication batch."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "1c7473f66eca9c5ac5bdd076e0ecc814616b10db": ("confirmed-current-boundary", "The title explicitly concerns segment-level speech representations for LLM-based speech recognition. Title-only evidence supports learned-speech-unit membership.", "recognition-and-alignment", "acoustic-unit-learning", "self-supervised-speech-units"),
    "1c9389bc4b2a96946c29c9934b7e134f4ee40928": ("reassigned-to-neighbor", "The title explicitly uses text-to-speech and voice conversion as augmentation for Alzheimer's detection from spontaneous speech. The speech-health task is more direct than voice conversion alone; title-only evidence supports a clinical speech marker.", "people-variation-and-health", "clinical-markers", "clinical-speech-marker"),
    "1d9d53c8debfbf7ed246bd7a53cdd1342998264c": ("confirmed-current-boundary", "The title explicitly concerns text-to-speech planning and text-semantic alignment. Title-only evidence supports text-to-speech planning.", "voice-generation-and-control", "content-planning", "text-to-speech-planning"),
    "1dfb5ec24d6e3005e7784a4ceec3f2a3272bff5e": ("confirmed-current-boundary", "The title explicitly concerns speech quality assessment. Title-only evidence supports quality and naturalness, without establishing listener validity.", "evaluation-deployment-and-consequence", "metric-and-human-targets", "quality-and-naturalness"),
    "1e32aa583285695751b8b722a703e3a2c7cfa116": ("reassigned-to-neighbor", "The title explicitly concerns controlled multi-speaker audio synthesis for evaluating speaker diarization. Title-only evidence supports unseen-speaker synthesis rather than speaker verification.", "voice-generation-and-control", "identity-and-conversion", "unseen-speaker-synthesis"),
    "1e470965d610b962554bd756fa4d5d837be4c0e8": ("confirmed-current-boundary", "The title explicitly concerns authenticity representation and localization of partially deepfake audio. Title-only evidence supports spoofing and synthetic-voice misuse.", "evaluation-deployment-and-consequence", "privacy-and-security", "spoofing-and-deepfake"),
    "1e83e39d30fafa6ef144cacd82f276347615d1d0": ("confirmed-current-boundary", "The title explicitly concerns target-speaker extraction using text cues. Title-only evidence supports target-conditioned separation.", "listening-and-separation", "source-separation", "target-conditioned-separation"),
    "1e96005d1136b5724f4868e4b5d72bf4258600c9": ("reassigned-to-neighbor", "The title explicitly concerns Japanese speech recognition with multi-pass generative error correction. Title-only evidence supports context and decoding control more directly than temporal alignment.", "recognition-and-alignment", "context-and-open-vocabulary", "domain-and-context-biasing"),
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
