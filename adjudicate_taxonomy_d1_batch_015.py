#!/usr/bin/env python3
"""Record the fourth title-only D1 taxonomy adjudication batch."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "1525608fc7436162fdac0ba8e89a238b6de566f1": ("rejected-out-of-scope", "The title concerns text-audio alignment but does not establish human speech or spoken-language evidence. With title-only evidence, speech membership is not supported.", None, None, None),
    "156cfdc110a9f73b7e8c5893b569d98e361ae573": ("confirmed-current-boundary", "The title explicitly concerns dynamic target-speaker extraction driven by EEG and eye tracking. Title-only evidence supports target-conditioned separation for speech processing.", "listening-and-separation", "source-separation", "target-conditioned-separation"),
    "165b642e85eb1e87fdce906317e81b03606e362a": ("confirmed-current-boundary", "The title explicitly concerns multimodal emotion recognition. Title-only evidence supports paralinguistic-state membership, without claims about emotion-label validity.", "meaning-and-interaction", "prosody-and-paralinguistics", "paralinguistic-state"),
    "1671667347ae459d1e7fc2aaff651009f6814a9e": ("confirmed-current-boundary", "The title explicitly concerns spoken-to-sign language generation. Title-only evidence supports cross-lingual or cross-modal language transfer, without claims about sign-language quality.", "languages-accents-and-resources", "crosslingual-structure", "crosslingual-transfer"),
    "1832417f4de28e9ee83e27322d7b791efea2f43a": ("confirmed-current-boundary", "The title explicitly concerns a personal speech word-counting system. Title-only evidence supports the boundary between word-error measurement and the user-level understanding target.", "evaluation-deployment-and-consequence", "metric-and-human-targets", "word-error-versus-understanding"),
    "1842b07d6356febdfc7a2dd0d960fe3593bd4d2d": ("confirmed-current-boundary", "The title explicitly concerns cochlear-implant speech denoising. Title-only evidence supports speech-prior denoising.", "listening-and-separation", "noise-enhancement", "speech-prior-denoising"),
    "191294c576ca75d76f70cb728d2290d6417f3749": ("rejected-out-of-scope", "The title concerns audio-visual deepfake generation and detection but does not establish synthetic speech or spoken-language evidence. With title-only evidence, speech privacy membership is not supported.", None, None, None),
    "1b3a97557f11e537bee409963df14cf43451e8b0": ("confirmed-current-boundary", "The title explicitly concerns low-latency spoken-language modeling. Title-only evidence supports latency and resource budget.", "evaluation-deployment-and-consequence", "deployment-cost", "latency-and-resource"),
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
