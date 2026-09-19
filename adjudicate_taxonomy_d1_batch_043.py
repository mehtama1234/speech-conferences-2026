#!/usr/bin/env python3
"""Record the thirty-second title-only D1 taxonomy adjudication batch."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "c5e89fc972f6c7225c521e05372ec72da9e0a140": ("rejected-out-of-scope", "The title concerns multimodal poetry generation and prosody-guided text refinement but does not establish spoken speech or a speech signal. With title-only evidence, speech prosody membership is not supported.", None, None, None),
    "c60bfabacd080644748ad81aab75ed31f5536eb9": ("confirmed-current-boundary", "The title explicitly concerns source-speaker tracing with contrastive learning and threshold calibration. Title-only evidence supports speaker-verification membership.", "people-variation-and-health", "identity-and-life-stage", "speaker-verification"),
    "c6ac1e268099a6ba5b76a565a024867b319b07dd": ("confirmed-current-boundary", "The title explicitly concerns universal speech enhancement and speech restoration. Title-only evidence supports speech-prior denoising.", "listening-and-separation", "noise-enhancement", "speech-prior-denoising"),
    "c6cf0ea9ddc329952b67a5114d8386ca9ef9b5ce": ("confirmed-current-boundary", "The title explicitly concerns speech analysis for neurodegenerative diseases. Title-only evidence supports a clinical speech marker, without establishing clinical validity.", "people-variation-and-health", "clinical-markers", "clinical-speech-marker"),
    "c79f8eb4f85bdd4881a6cb4f4191bebafc118bfe": ("confirmed-current-boundary", "The title explicitly concerns recognition of disordered speech. Title-only evidence supports atypical-articulation and dysarthria membership.", "people-variation-and-health", "atypical-and-assistive-speech", "dysarthria-and-atypical-speech"),
    "c89067b31a2e42cffabf0f03fb510b84bd50cb9b": ("confirmed-current-boundary", "The title explicitly concerns a high-fidelity neural vocoder. Title-only evidence supports waveform synthesis.", "voice-generation-and-control", "waveform-and-codec-generation", "waveform-synthesis"),
    "c8b22be558c208683b1e247876248b897fa9e655": ("confirmed-current-boundary", "The title explicitly concerns hierarchical acoustic-semantic annotation for scripted speech data. Title-only evidence supports speech data collection.", "languages-accents-and-resources", "data-creation", "speech-data-collection"),
    "c8fd5fb10541e194e69117fb8b95ec4f55302a6e": ("confirmed-current-boundary", "The title explicitly concerns acoustic-semantic speech quality assessment. Title-only evidence supports quality and naturalness, without establishing human-listener agreement.", "evaluation-deployment-and-consequence", "metric-and-human-targets", "quality-and-naturalness"),
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
