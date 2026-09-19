#!/usr/bin/env python3
"""Record the next eight title-only D1 taxonomy adjudications."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "50e14b9ac570189aebe20561ad4144aad4e1614f": ("rejected-out-of-scope", "The title concerns novel-view acoustic synthesis and 3D acoustic environments but does not establish a human-speech or spoken-language task. With title-only evidence, reverberant speech-room membership is not supported.", None, None, None),
    "519c2042045bbe187163b1f7db0a55a86d5ab5b5": ("confirmed-current-boundary", "The title explicitly concerns speaker unlearning for zero-shot text-to-speech. Title-only evidence supports speaker identity representation, without establishing the effectiveness of voice removal.", "voice-generation-and-control", "identity-and-conversion", "speaker-identity-representation"),
    "51d6cdd34dd2c20106c9fb38fac53700e9978612": ("confirmed-current-boundary", "The title explicitly concerns audio deepfake detection and a synthetic-voice threat scenario. Title-only evidence supports spoofing and synthetic voice misuse, without establishing detection reliability.", "evaluation-deployment-and-consequence", "privacy-and-security", "spoofing-and-synthetic-voice-misuse"),
    "53e7ac04cd272b699aa4db921bea836d76f62fec": ("confirmed-current-boundary", "The title explicitly concerns robust accent identification through voice conversion and non-timbral features. Title-only evidence supports accent robustness, without establishing performance across a defined accent inventory.", "languages-accents-and-resources", "accent-dialect-and-cultural-meaning", "accent-robustness"),
    "54b731b40cbb3b27f39773696230bfca7c539426": ("confirmed-current-boundary", "The title explicitly concerns real-world speech enhancement and projection between close and distant microphones. Title-only evidence supports microphone and channel coloration, without establishing enhancement quality in deployment.", "sound-and-production", "room-channel-and-sensing", "microphone-and-channel-coloration"),
    "54c3c5ac59c612e4e4f0abc055888c8370208316": ("rejected-out-of-scope", "The title names compact audio-text embeddings and a Whisper token but does not establish a text-to-speech or spoken-language generation task. With title-only evidence, text-to-speech planning membership is not supported.", None, None, None),
    "55c342722bc5357808194912973e1c500348a201": ("rejected-out-of-scope", "The title concerns topic segmentation from audio features but does not establish a speech, dialogue, or spoken-language task. With title-only evidence, dialogue-state membership is not supported.", None, None, None),
    "55fe457194f7dc62b01ebc0abf1612e1a8112ad0": ("rejected-out-of-scope", "The title explicitly concerns a music source-restoration challenge rather than a human-speech or spoken-language object. It is outside this speech taxonomy.", None, None, None),
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
