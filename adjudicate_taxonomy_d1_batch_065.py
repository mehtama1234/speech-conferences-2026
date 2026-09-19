#!/usr/bin/env python3
"""Record the next eight title-only D1 taxonomy adjudications."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "d7cc01eb6aad28ecca46d33e099a310e44bae6e7": ("reassigned-to-neighbor", "The title explicitly concerns expressive speech synthesis with voice cloning. Title-only evidence places it under style and emotion control rather than generic voice conversion.", "voice-generation-and-control", "expression-and-interactive-control", "style-and-emotion-control"),
    "d7de85d1a50b28c6be89c52bf4f280b4040c8814": ("confirmed-current-boundary", "The title explicitly concerns low-resource speech recognition with progressive training. Title-only evidence supports few-shot adaptation, without establishing the amount or value of adaptation data.", "languages-accents-and-resources", "low-resource-learning", "few-shot-adaptation"),
    "d90d42d847c14e006b4f0a368833df6d5453fbed": ("rejected-out-of-scope", "The title concerns respiratory sound classification and does not establish a human-speech or spoken-language task. With title-only evidence, clinical speech marker membership is not supported.", None, None, None),
    "d9324538740727199cda494aa4d1a1c7c2f48ae3": ("confirmed-current-boundary", "The title explicitly concerns prosody and articulatory cues in multilingual zero-shot text-to-speech. Title-only evidence supports prosody control, without establishing synthesis quality or zero-shot coverage.", "voice-generation-and-control", "expression-and-interactive-control", "prosody-control"),
    "d97853b4f6e73fd9e73f988d0902a4f08e7964ba": ("confirmed-current-boundary", "The title explicitly concerns flow-matching speech enhancement. Title-only evidence supports speech-prior denoising, without establishing enhancement quality or the effect of online reinforcement learning.", "listening-and-separation", "noise-enhancement", "speech-prior-denoising"),
    "d9adafcf5122950f31099fd630aa14a2cdc5a1fa": ("confirmed-current-boundary", "The title explicitly concerns speaker verification and anti-spoofing under domain variation. Title-only evidence supports spoofing and deepfake detection, without establishing generalization.", "evaluation-deployment-and-consequence", "privacy-and-security", "spoofing-and-deepfake"),
    "d9b1ef17ca01a3e13e6b0fdd761a079b2585e1a0": ("rejected-out-of-scope", "The title concerns generic audio source separation and does not establish a human-speech or spoken-language task. With title-only evidence, target-conditioned speech separation membership is not supported.", None, None, None),
    "d9f764f6cc990b6044c7907ef50ad2799613cb94": ("rejected-out-of-scope", "The title concerns audio-based toxic-span detection but does not establish a speech or spoken-language object strongly enough to support intent-in-context membership from title-only evidence.", None, None, None),
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
