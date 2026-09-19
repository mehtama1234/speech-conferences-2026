#!/usr/bin/env python3
"""Record the seventh title-only D1 taxonomy adjudication batch."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "23a2d1975dc0c7f9c93d8f60b4ea15d8e302d571": ("rejected-out-of-scope", "The title concerns audio-text relevance assessment but does not establish a human-speech or spoken-language task. With title-only evidence, speech membership is not supported.", None, None, None),
    "23ee11c59dbdd9045d08998cadef43ba39251003": ("confirmed-current-boundary", "The title explicitly concerns phonetic subspaces of speech representations. Title-only evidence supports learned speech-unit membership.", "recognition-and-alignment", "acoustic-unit-learning", "self-supervised-speech-units"),
    "23fbd2303bfeea0db8aa5b18b19bc6fdd4e3442e": ("confirmed-current-boundary", "The title explicitly concerns speech emotion recognition under noise. Title-only evidence supports paralinguistic-state membership.", "meaning-and-interaction", "prosody-and-paralinguistics", "paralinguistic-state"),
    "24493088ae4c9fbc1adae4d471dbb3bb8e71f306": ("confirmed-current-boundary", "The title explicitly concerns speech spoofing detection using speech features. Title-only evidence supports spoofing and synthetic-voice misuse.", "evaluation-deployment-and-consequence", "privacy-and-security", "spoofing-and-deepfake"),
    "24c48679e5b5b9c0f7326cb5edb70880365a0f6e": ("rejected-out-of-scope", "The title concerns auditory attention decoding across subjects but does not establish a human-speech or spoken-language task. With title-only evidence, speech interaction membership is not supported.", None, None, None),
    "25890b928d7c3e60a9d4a3235c2a067ed0e74119": ("confirmed-current-boundary", "The title explicitly concerns detecting deepfake speech on a social-media platform. Title-only evidence supports spoofing and synthetic-voice misuse.", "evaluation-deployment-and-consequence", "privacy-and-security", "spoofing-and-deepfake"),
    "28bdc6f9e8de67c3fb8041755e60fa0ba9e9cf71": ("rejected-out-of-scope", "The title concerns microphone-less measurement of a general sound source and impulse response. It does not establish human speech or spoken-language evidence.", None, None, None),
    "295ad8fbdd7766969cdafb59bf1b93d868a3af2f": ("confirmed-current-boundary", "The title explicitly concerns acoustic speech enhancement under low-SNR radar noise. Title-only evidence supports speech-prior denoising.", "listening-and-separation", "noise-enhancement", "speech-prior-denoising"),
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
