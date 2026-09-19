#!/usr/bin/env python3
"""Record the thirty-third title-only D1 taxonomy adjudication batch."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "c9e75e339f308ed3e99f3188bdab14f1167fc720": ("confirmed-current-boundary", "The title explicitly names a real-time MRI speech dataset and benchmark. Title-only evidence supports non-airborne speech sensing, without establishing dataset coverage.", "sound-and-production", "room-channel-and-sensing", "non-airborne-sensing"),
    "ca269cec0bc11edd9172e2157043e25a02a83ade": ("confirmed-current-boundary", "The title explicitly concerns end-to-end speaker verification with uncertainty-aware scoring. Title-only evidence supports speaker-verification membership.", "people-variation-and-health", "identity-and-life-stage", "speaker-verification"),
    "cb8d54e55a8487dff13603d05c5c62a43333ba7b": ("confirmed-current-boundary", "The title explicitly concerns hearing-aid speech intelligibility prediction. Title-only evidence supports listener effort, without establishing hearing-aid benefit.", "people-variation-and-health", "human-centered-accessibility", "listener-effort"),
    "cbdd77e4248c739d0308028a136b48dfdeb3ccfe": ("confirmed-current-boundary", "The title explicitly concerns sEEG-based speech decoding with test-time adaptation. Title-only evidence supports non-airborne speech sensing, without claims about neural communication benefit.", "sound-and-production", "room-channel-and-sensing", "non-airborne-sensing"),
    "cbefe484c49db0a71a5adb3b7cd52816fec72c01": ("confirmed-current-boundary", "The title explicitly concerns fast inference for masked-transformer text-to-speech. Title-only evidence supports interactive generation latency.", "voice-generation-and-control", "expression-and-interactive-control", "interactive-latency"),
    "cd1e64eda4d040b38742ad61f24392dff7615ea8": ("rejected-out-of-scope", "The title concerns general audio class-incremental classification and does not establish a human-speech or spoken-language task. With title-only evidence, open-vocabulary speech recognition membership is not supported.", None, None, None),
    "ce33cd9174c587d6063fc257e9d8f0a2440f3c0e": ("confirmed-current-boundary", "The title explicitly concerns semantic coherence failures in speech-language-model outputs. Title-only evidence supports referential grounding, without establishing a specific grounding benchmark.", "meaning-and-interaction", "grounding-and-action", "referential-grounding"),
    "cead5caf2ea8d799566a8c0b1c77e9213bf0ecce": ("rejected-out-of-scope", "The title concerns microphone-array geometry and beamforming for general sound but does not establish a human-speech or spoken-language task. With title-only evidence, speech microphone membership is not supported.", None, None, None),
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
