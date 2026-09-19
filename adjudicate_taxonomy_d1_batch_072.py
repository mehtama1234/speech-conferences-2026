#!/usr/bin/env python3
"""Record the next eight title-only D1 taxonomy adjudications."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "f0924eacbcf0288735d4a8e3e83caa8b6255e1ad": ("rejected-out-of-scope", "The title concerns a compact audio-language model for music understanding rather than a human-speech or spoken-language task. It is outside this speech taxonomy.", None, None, None),
    "f13d00332d028e499f5fce9073ee2936aa373ef3": ("confirmed-current-boundary", "The title explicitly concerns domain-adapted speaker verification. Title-only evidence supports speaker verification, without establishing verification performance or domain robustness.", "people-variation-and-health", "identity-and-life-stage", "speaker-verification"),
    "f1ad862c634587bcf8357c1e958d1b58764a9919": ("confirmed-current-boundary", "The title explicitly concerns text normalization for non-standard words in text-to-speech synthesis. Title-only evidence supports text-to-speech planning, without establishing normalization or synthesis quality.", "voice-generation-and-control", "content-planning", "text-to-speech-planning"),
    "f1f4448e5a0d6b9e4039e06fcef44ed63fb19342": ("rejected-out-of-scope", "The title concerns virtual microphone estimation for general spatial audio and does not establish a human-speech or spoken-language task. With title-only evidence, microphone and channel coloration for speech is not supported.", None, None, None),
    "f2376a106e7f304eb0c4ea1d4ca05b43850653f4": ("rejected-out-of-scope", "The title concerns observer-label emotion prediction but does not establish a human-speech or spoken-language task. With title-only evidence, listener effort membership is not supported.", None, None, None),
    "f2abc333ac4fd78e1783e0a3d0cd0a7afa852630": ("confirmed-current-boundary", "The title explicitly concerns multimodal emotion recognition in conversations. Title-only evidence supports paralinguistic state, without establishing emotion-recognition reliability.", "meaning-and-interaction", "prosody-and-paralinguistics", "paralinguistic-state"),
    "f2e289a5e1a0f1aac8a9f50a14d4ca85a8c90c1c": ("rejected-out-of-scope", "The title concerns lyric-to-melody generation and musical constraints rather than a human-speech or spoken-language task. It is outside this speech taxonomy.", None, None, None),
    "f30f800954d57e1fcda2b7724ac89df1ff830d14": ("confirmed-current-boundary", "The title explicitly concerns explainable speech deepfake detection. Title-only evidence supports spoofing and deepfake detection, without establishing detection reliability or explanation quality.", "evaluation-deployment-and-consequence", "privacy-and-security", "spoofing-and-deepfake"),
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
