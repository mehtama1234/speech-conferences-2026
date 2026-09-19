#!/usr/bin/env python3
"""Record the next eight title-only D1 taxonomy adjudications."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "97e0409dd4be705832052492e33fea915455ceb9": ("confirmed-current-boundary", "The title explicitly concerns federated optimization for hybrid automatic speech recognition across heterogeneous languages. Title-only evidence supports cross-lingual transfer, without establishing transfer quality or privacy behavior.", "languages-accents-and-resources", "crosslingual-structure", "crosslingual-transfer"),
    "98a622eab408c535d14cdf5aa96f0823383a017e": ("confirmed-current-boundary", "The title explicitly concerns multilingual large-model automatic speech recognition. Title-only evidence supports cross-lingual transfer, without establishing language coverage or recognition quality.", "languages-accents-and-resources", "crosslingual-structure", "crosslingual-transfer"),
    "9d426105ae5466196e126aa5e50efec0ba3ec410": ("confirmed-current-boundary", "The title explicitly concerns token enhancement for token-based speech recognition. Title-only evidence supports speech-prior denoising, without establishing recognition or enhancement gains.", "listening-and-separation", "noise-enhancement", "speech-prior-denoising"),
    "9dda34ca21164e123f236c272b9a967c61cbca16": ("rejected-out-of-scope", "The title concerns online source counting from spatial coherence and does not establish a human-speech or spoken-language task. With title-only evidence, blind speech source separation membership is not supported.", None, None, None),
    "9e693df27c03306e87a93d85a202387c01e66a03": ("rejected-out-of-scope", "The title concerns jazz solo transcription and music scores rather than a human-speech or spoken-language task. With title-only evidence, acoustic-to-token speech mapping is not supported.", None, None, None),
    "9f6c870ee35050d73c2a2ec1eceb4b64bf87686a": ("rejected-out-of-scope", "The title concerns multimodal forgery detection but does not establish a human-speech, spoken-language, or synthetic-voice task. With title-only evidence, synthetic voice misuse membership is not supported.", None, None, None),
    "a01e28cf84390d2b299b8599e75f6795367e83b9": ("confirmed-current-boundary", "The title explicitly concerns interlanguage speech intelligibility and accent-robust automatic speech recognition. Title-only evidence supports accent robustness, without establishing intelligibility benefit across language backgrounds.", "languages-accents-and-resources", "accent-dialect-and-cultural-meaning", "accent-robustness"),
    "a127f6df9b9af46e20a51a0124222d07c2849ec2": ("reassigned-to-neighbor", "The title explicitly concerns emotion-aware validation timing in empathetic spoken dialogue. Title-only evidence places it under interactional feedback rather than turn-boundary prediction.", "meaning-and-interaction", "grounding-and-action", "interactional-feedback"),
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
