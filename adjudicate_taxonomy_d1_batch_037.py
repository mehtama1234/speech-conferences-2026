#!/usr/bin/env python3
"""Record the twenty-sixth title-only D1 taxonomy adjudication batch."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "a5cd9da36fe1f22fd0f502fa06d0eca7385b9466": ("confirmed-current-boundary", "The title explicitly concerns keyword spotting implemented in FPGA hardware. Title-only evidence supports open-vocabulary recognition, without claims about vocabulary coverage.", "recognition-and-alignment", "context-and-open-vocabulary", "open-vocabulary-recognition"),
    "a5dfd6f9c261b41e8029f39fc35d4911ef8ffba7": ("confirmed-current-boundary", "The title explicitly concerns directional speech understanding in a large language model. Title-only evidence supports referential grounding.", "meaning-and-interaction", "grounding-and-action", "referential-grounding"),
    "a68f6358f5e03df7c2c79c7efca1ec5de8829220": ("confirmed-current-boundary", "The title explicitly concerns protecting sensitive data in automatic speech recognition. Title-only evidence supports voice privacy, without establishing a security guarantee.", "evaluation-deployment-and-consequence", "privacy-and-security", "voice-privacy"),
    "a72f084a74b385cb895854bee7fbfedb556e5ab5": ("confirmed-current-boundary", "The title explicitly concerns target-speaker voice activity detection for speaker diarization. Title-only evidence supports temporal alignment and boundary modeling.", "recognition-and-alignment", "boundaries-and-alignment", "alignment"),
    "a761c70798d74d17ce14ad9cc4334f7bcb869b62": ("reassigned-to-neighbor", "The title explicitly concerns autoregressive speech synthesis but does not mention text planning. Title-only evidence supports waveform synthesis more directly than text-to-speech planning.", "voice-generation-and-control", "waveform-and-codec-generation", "waveform-synthesis"),
    "a90b2cf4bc51065b9cd7ece3552bfa0821b1597b": ("reassigned-to-neighbor", "The title explicitly concerns source-free unsupervised domain adaptation in speech recognition. Distribution shift is the direct boundary, rather than domain-context biasing.", "evaluation-deployment-and-consequence", "robustness-and-shift", "distribution-shift"),
    "aae3d291d8018c414104c4e4c4917e65bdaf0f92": ("rejected-out-of-scope", "The title concerns virtual sound sources in personalized sound zones and does not establish a human-speech or spoken-language task. With title-only evidence, reverberant speech membership is not supported.", None, None, None),
    "abc1e2002aeac2134f1db8f1465af77b8cd0d764": ("confirmed-current-boundary", "The title explicitly concerns linguistic knowledge transfer and alignment for automatic speech recognition. Title-only evidence supports acoustic-to-token mapping.", "recognition-and-alignment", "acoustic-unit-learning", "acoustic-to-token"),
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
