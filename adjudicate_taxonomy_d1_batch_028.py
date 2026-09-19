#!/usr/bin/env python3
"""Record the seventeenth title-only D1 taxonomy adjudication batch."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "64bf350e3e39c298180a4880f33b136f214998d9": ("confirmed-current-boundary", "The title explicitly concerns ALS detection from phonation audio. Title-only evidence supports a clinical speech marker, without establishing diagnostic validity.", "people-variation-and-health", "clinical-markers", "clinical-speech-marker"),
    "660f35b8352b53a899ba4c4c25fcacabd473e27a": ("confirmed-current-boundary", "The title explicitly concerns estimating speaker-diarization error from audio quality and speaker discriminability. Title-only evidence supports calibrated/selective evaluation use.", "evaluation-deployment-and-consequence", "metric-and-human-targets", "calibration-and-selective-use"),
    "676675c7bb94470d53620f8a14da4535906bc471": ("rejected-out-of-scope", "The title concerns cross-modal semantic alignment for a general audio-text challenge but does not establish human speech or spoken-language evidence. With title-only evidence, speech grounding membership is not supported.", None, None, None),
    "68aad77e17f25b06e9fe42fd85415056ffb0fb5b": ("rejected-out-of-scope", "The title concerns language-queried audio source separation but does not establish human speech or spoken-language evidence. With title-only evidence, speech target separation membership is not supported.", None, None, None),
    "68cf1cdf5126273eaae63cf77c10e296ebb2c853": ("confirmed-current-boundary", "The title explicitly concerns radar acoustic speech enhancement. Title-only evidence supports speech-prior denoising.", "listening-and-separation", "noise-enhancement", "speech-prior-denoising"),
    "68edcdb1a7eeeb95d1b3cef31da62bd72ac5bad7": ("confirmed-current-boundary", "The title explicitly concerns open-vocabulary multimodal emotion recognition. Title-only evidence supports paralinguistic-state membership.", "meaning-and-interaction", "prosody-and-paralinguistics", "paralinguistic-state"),
    "6966194d76db19ba5c79b3ed4644d7c3db68ccee": ("confirmed-current-boundary", "The title explicitly concerns real-time acoustic echo cancellation. Title-only evidence supports acoustic-echo cancellation.", "listening-and-separation", "echo-reconstruction", "acoustic-echo-cancellation"),
    "69f1a8fdb2a671f427eeea461d86c2202365c441": ("rejected-out-of-scope", "The title concerns lyric intelligibility and ASR embeddings, which points to singing or music content rather than ordinary human speech. With title-only evidence, speech word-error membership is not supported.", None, None, None),
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
