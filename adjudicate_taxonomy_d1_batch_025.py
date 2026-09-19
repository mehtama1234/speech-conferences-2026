#!/usr/bin/env python3
"""Record the fourteenth title-only D1 taxonomy adjudication batch."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "5331fe1016a8ff681a7dc5873b28d4ee98a107b8": ("rejected-out-of-scope", "The title concerns continual audio-visual sound separation but does not establish human speech or spoken-language evidence. With title-only evidence, speech source-separation membership is not supported.", None, None, None),
    "5333a836a46f3b563dcdc5e9dedd98af93698b59": ("confirmed-current-boundary", "The title explicitly concerns multimodal emotion recognition in conversations. Title-only evidence supports paralinguistic-state membership.", "meaning-and-interaction", "prosody-and-paralinguistics", "paralinguistic-state"),
    "537488e9a529c552272d9361c2349f9e5274bc53": ("confirmed-current-boundary", "The title explicitly concerns codec-based text-to-speech. Title-only evidence supports waveform synthesis.", "voice-generation-and-control", "waveform-and-codec-generation", "waveform-synthesis"),
    "554cd489c5895dd613b0de284120b1099330f1f4": ("confirmed-current-boundary", "The title explicitly concerns detecting and attributing synthetic Spanish speech. Title-only evidence supports spoofing and synthetic-voice misuse.", "evaluation-deployment-and-consequence", "privacy-and-security", "spoofing-and-deepfake"),
    "56774f3ae80d0bb4f025443614ff7ea7f36d9c9a": ("rejected-out-of-scope", "The title concerns multimodal deepfake detection but does not establish synthetic speech or spoken-language evidence. With title-only evidence, speech privacy membership is not supported.", None, None, None),
    "56cb603449bbe6be83622a36796e2f09da065785": ("confirmed-current-boundary", "The title explicitly concerns hybrid speech enhancement for the URGENT challenge. Title-only evidence supports speech-prior denoising.", "listening-and-separation", "noise-enhancement", "speech-prior-denoising"),
    "58309794fbce780b33ddfc233c5acca528510343": ("confirmed-current-boundary", "The title explicitly concerns compression of a neural speech codec through dynamic frame rates. Title-only evidence supports latency and resource budget.", "evaluation-deployment-and-consequence", "deployment-cost", "latency-and-resource"),
    "589cefbc1642bea16a5e231cddf377194e498c9e": ("rejected-out-of-scope", "The title concerns inverse filtering for a rigid spherical microphone array but does not establish a human-speech or spoken-language task. With title-only evidence, speech microphone membership is not supported.", None, None, None),
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
