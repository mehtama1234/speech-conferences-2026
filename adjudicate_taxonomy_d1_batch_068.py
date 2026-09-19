#!/usr/bin/env python3
"""Record the next eight title-only D1 taxonomy adjudications."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "e1ef6d4639a2979b1b7d400a374a0ea53a6528c9": ("reassigned-to-neighbor", "The title explicitly concerns EEG-based decoding of auditory attention during mixed speech. Title-only evidence places it under non-airborne speech sensing rather than interactional feedback.", "sound-and-production", "room-channel-and-sensing", "non-airborne-sensing"),
    "e264f8b04b889d8e4ce74234d789a34688303bbc": ("reassigned-to-neighbor", "The title explicitly concerns audio watermarking for proactive deepfake detection. Title-only evidence places it under spoofing and deepfake detection rather than voice privacy.", "evaluation-deployment-and-consequence", "privacy-and-security", "spoofing-and-deepfake"),
    "e45510076a027f702edb742c8752c28cb223dc6b": ("confirmed-current-boundary", "The title explicitly concerns emotion recognition in conversations. Title-only evidence supports paralinguistic state, without establishing emotion-recognition reliability.", "meaning-and-interaction", "prosody-and-paralinguistics", "paralinguistic-state"),
    "e4ec2ef439d4bf9ae68b325afc9de1ecde1ec502": ("rejected-out-of-scope", "The title concerns sparse sound-field reconstruction with microphone arrays and does not establish a human-speech or spoken-language task. With title-only evidence, reverberant speech-room membership is not supported.", None, None, None),
    "e5cfa34259fb4eed3c2d7c3aacde858b19d0cc43": ("confirmed-current-boundary", "The title explicitly concerns conversational emotion recognition. Title-only evidence supports paralinguistic state, without establishing robustness or emotion-recognition reliability.", "meaning-and-interaction", "prosody-and-paralinguistics", "paralinguistic-state"),
    "e5ddce2b50a7696faf858e68acbb161109f3952c": ("confirmed-current-boundary", "The title explicitly concerns deepfake audio detection. Title-only evidence supports spoofing and deepfake detection, without establishing detection reliability.", "evaluation-deployment-and-consequence", "privacy-and-security", "spoofing-and-deepfake"),
    "e5e9bdfab1dee9b3d504c5fd0d01a28a225c30eb": ("confirmed-current-boundary", "The title explicitly concerns cued speech recognition for barrier-free communication. Title-only evidence supports augmentative communication, without establishing accessibility or user benefit.", "people-variation-and-health", "atypical-and-assistive-speech", "augmentative-communication"),
    "e656dcb00437d4750583756f5fedc88935f99fa9": ("confirmed-current-boundary", "The title explicitly concerns open-vocabulary keyword spotting. Title-only evidence supports open-vocabulary recognition, without establishing vocabulary coverage or false-alarm behavior.", "recognition-and-alignment", "context-and-open-vocabulary", "open-vocabulary-recognition"),
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
