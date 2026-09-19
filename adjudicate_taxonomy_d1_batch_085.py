#!/usr/bin/env python3
"""Record the next eight title-only D1 taxonomy adjudications."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "chen25o_interspeech": ("confirmed-current-boundary", "The title explicitly concerns predicting adolescent suicidal risk from speech. Title-only evidence supports clinical speech marker membership, without establishing clinical validity or prediction utility.", "people-variation-and-health", "clinical-markers", "clinical-speech-marker"),
    "chen25p_interspeech": ("confirmed-current-boundary", "The title explicitly concerns a speech codec with dual-stage training. Title-only evidence supports waveform synthesis, without establishing codec reconstruction quality or bitrate tradeoffs.", "voice-generation-and-control", "waveform-and-codec-generation", "intelligibility-naturalness"),
    "chen25q_interspeech": ("reassigned-to-neighbor", "The title explicitly concerns a neural vocoder for speech. Title-only evidence places it under neural vocoder rather than the broader waveform-synthesis label.", "voice-generation-and-control", "waveform-and-codec-generation", "neural-vocoder"),
    "cheng25_interspeech": ("confirmed-current-boundary", "The title explicitly concerns standardized labeling of speech paralinguistic and affective properties. Title-only evidence supports paralinguistic state, without establishing label validity.", "meaning-and-interaction", "prosody-and-paralinguistics", "paralinguistic-state"),
    "cheng25b_interspeech": ("confirmed-current-boundary", "The title explicitly concerns multichannel sequence-to-sequence neural diarization in a speech challenge. Title-only evidence supports end-to-end recovery, without establishing diarization performance.", "evaluation-deployment-and-consequence", "robustness-and-shift", "end-to-end-recovery"),
    "cheng25d_interspeech": ("reassigned-to-neighbor", "The title explicitly concerns speech unlearning, which is a privacy and identity-control problem rather than speaker verification. Title-only evidence places it under voice privacy.", "evaluation-deployment-and-consequence", "privacy-and-security", "voice-privacy"),
    "chi25_interspeech": ("confirmed-current-boundary", "The title explicitly concerns distilling HuBERT with a self-supervised learning objective. Title-only evidence supports learned speech units, without establishing representation quality or downstream benefit.", "recognition-and-alignment", "acoustic-unit-learning", "self-supervised-speech-units"),
    "chi25b_interspeech": ("rejected-out-of-scope", "The title concerns device-directed speech detection and does not establish a changing-noise or enhancement task. With title-only evidence, changing and adverse noise membership is not supported.", None, None, None),
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
