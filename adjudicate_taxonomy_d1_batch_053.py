#!/usr/bin/env python3
"""Record the next eight title-only D1 taxonomy adjudications."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "890364175bb710ac2ff70fcb093352b95a0cd4fd": ("confirmed-current-boundary", "The title explicitly concerns improved multilingual speech recognition using a byte-level encoding. Title-only evidence supports cross-lingual transfer, without establishing recognition quality across languages.", "languages-accents-and-resources", "crosslingual-structure", "crosslingual-transfer"),
    "893ce28f671feec9882616854700af85b48a6510": ("confirmed-current-boundary", "The title explicitly concerns confidence-based filtering for speech dataset curation. Title-only evidence supports calibration and selective use, without establishing the reliability of the confidence scores.", "evaluation-deployment-and-consequence", "metric-and-human-targets", "calibration-and-selective-use"),
    "8acbc8ec45ece03f9c9eff5f15d136e382a3b101": ("confirmed-current-boundary", "The title explicitly concerns a full-duplex spoken dialogue system and its turn structure. Title-only evidence supports turn-boundary prediction, without establishing interruption or latency performance.", "meaning-and-interaction", "turn-taking-and-repair", "turn-boundary"),
    "8b6a6f22bc92ddc6c3ed33ba2eb5654b71361439": ("confirmed-current-boundary", "The title explicitly concerns a unified spoken language model for human-like interaction with emotional attribution. Title-only evidence supports dialogue state, without establishing interaction quality or emotional understanding.", "meaning-and-interaction", "intent-and-dialogue-state", "dialogue-state"),
    "8bf98d256760575121a176bcc064871a3ea80cf0": ("rejected-out-of-scope", "The title concerns audio-visual video-highlight detection but does not establish a human-speech or spoken-language task. With title-only evidence, referential grounding membership is not supported.", None, None, None),
    "8c76937b26e8aab0c19592f81f654e006f463e1b": ("reassigned-to-neighbor", "The title explicitly concerns lip-to-speech synthesis and prosody consistency. Title-only evidence places it under prosody control rather than within-speaker state variation.", "voice-generation-and-control", "expression-and-interactive-control", "prosody-control"),
    "8e16277adee97a48218203a0fd59570ebb560967": ("confirmed-current-boundary", "The title explicitly concerns resynthesized audio, neural codecs, and audio deepfake detection. Title-only evidence supports spoofing and deepfake detection, without establishing detection reliability.", "evaluation-deployment-and-consequence", "privacy-and-security", "spoofing-and-deepfake"),
    "8e5830626e2fc4f09d4e157ff865fee93752c9de": ("rejected-out-of-scope", "The title concerns active noise control for general acoustic signals and does not establish a human-speech or spoken-language task. With title-only evidence, changing and adverse speech noise membership is not supported.", None, None, None),
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
