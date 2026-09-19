#!/usr/bin/env python3
"""Record the sixth title-only D1 taxonomy adjudication batch."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "1f25976b7708c5e4ee5e02c02a8d36ef46748662": ("rejected-out-of-scope", "The title concerns panoramic audio recording and microphone arrays but does not establish a human-speech or spoken-language task. With title-only evidence, speech membership is not supported.", None, None, None),
    "1f8a801c970c93b61ebe34702e2f3164d8b0a956": ("reassigned-to-neighbor", "The title explicitly concerns few-step speech generation but does not mention text planning. Title-only evidence supports waveform synthesis more directly than text-to-speech planning.", "voice-generation-and-control", "waveform-and-codec-generation", "waveform-synthesis"),
    "206fced6cf644b81963ed305bbdd3eff408c9ddc": ("confirmed-current-boundary", "The title explicitly concerns audio deepfake detection under dynamic noise. Title-only evidence supports spoofing and synthetic-voice misuse.", "evaluation-deployment-and-consequence", "privacy-and-security", "spoofing-and-deepfake"),
    "2199f02febe4070c615460719d1061134b4a09ee": ("rejected-out-of-scope", "The title concerns feedback cancellation in hearing aids but does not establish a human-speech or spoken-language task. With title-only evidence, speech membership is not supported.", None, None, None),
    "21f61c426a74f6519f57e0819309129fba61b735": ("rejected-out-of-scope", "The title concerns audio-driven 3D talking-head synthesis but does not establish a speech signal or spoken-language task. With title-only evidence, speech membership is not supported.", None, None, None),
    "227e23e92c2501f987da091972ab773a198850f9": ("confirmed-current-boundary", "The title explicitly combines acoustic feedback cancellation with speaker extraction. Title-only evidence supports acoustic-echo cancellation within speech listening and separation.", "listening-and-separation", "echo-reconstruction", "acoustic-echo-cancellation"),
    "2299f07e80e65dda8f3b3218b4ae3cf660f0a029": ("confirmed-current-boundary", "The title explicitly concerns defense against voice-cloning attacks. Title-only evidence supports voice privacy and misuse protection.", "evaluation-deployment-and-consequence", "privacy-and-security", "voice-privacy"),
    "22dc19dcc4dc31a240c8e6523017075154159a8e": ("confirmed-current-boundary", "The title explicitly names acted voices and a dataset aligned to manga images. Title-only evidence supports speech data collection, without establishing dataset quality or coverage.", "languages-accents-and-resources", "data-creation", "speech-data-collection"),
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
