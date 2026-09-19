#!/usr/bin/env python3
"""Record the thirty-first title-only D1 taxonomy adjudication batch."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "bccd76bb5f248e0565b9b76458ea2fdde31dabee": ("confirmed-current-boundary", "The title explicitly concerns fine-grained conversational emotion recognition. Title-only evidence supports paralinguistic-state membership.", "meaning-and-interaction", "prosody-and-paralinguistics", "paralinguistic-state"),
    "bd4a0b8c6b271049041fb09bbc3aaf0be0296d7f": ("rejected-out-of-scope", "The title concerns a general neural audio codec and does not establish a human-speech or spoken-language task. With title-only evidence, speech latency membership is not supported.", None, None, None),
    "bddadbef17ae03f31601ff615fd701fc95322f56": ("confirmed-current-boundary", "The title explicitly concerns spoken-language-based dementia detection. Title-only evidence supports a clinical speech marker, without establishing diagnostic validity.", "people-variation-and-health", "clinical-markers", "clinical-speech-marker"),
    "c02be3a349febc43a47dab6b5a5d0e6cd47ca704": ("reassigned-to-neighbor", "The title explicitly concerns zero-shot cross-lingual voice conversion. The direct speech operation is voice conversion rather than transfer alone.", "voice-generation-and-control", "identity-and-conversion", "voice-conversion"),
    "c190b7b4ce26a6046fa2680549d7ecb545f4d0a5": ("confirmed-current-boundary", "The title explicitly concerns Alzheimer's disease progression classification using audio. Title-only evidence supports a clinical speech marker, without establishing diagnostic validity.", "people-variation-and-health", "clinical-markers", "clinical-speech-marker"),
    "c1bee1bb8b1d5f37356bb868ad79b565d129817d": ("confirmed-current-boundary", "The title explicitly concerns target-speaker voice activity detection with chunk-level queries. Title-only evidence supports temporal alignment and boundary modeling.", "recognition-and-alignment", "boundaries-and-alignment", "alignment"),
    "c1feec40a8ba8e39029b44d47770b453a5464e08": ("rejected-out-of-scope", "The title concerns general inhomogeneous sound-field estimation and does not establish a human-speech or spoken-language task. With title-only evidence, reverberant speech membership is not supported.", None, None, None),
    "c4ef85911ee7d188b0d62636f76ffba73dee0d8f": ("rejected-out-of-scope", "The title concerns audio deepfake detection on AI-processed data but does not establish synthetic speech or spoken-language evidence. With title-only evidence, speech spoofing membership is not supported.", None, None, None),
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
