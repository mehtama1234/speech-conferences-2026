#!/usr/bin/env python3
"""Record the next eight title-only D1 taxonomy adjudications."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "6c79a29332af1653da5ef579148e0a736bc7ae3f": ("confirmed-current-boundary", "The title explicitly concerns a speech language model for generative speech separation. Title-only evidence supports target-conditioned separation, without establishing separation quality or conditioning behavior.", "listening-and-separation", "source-separation", "target-conditioned-separation"),
    "6eb99e4599f047f16712fb8f4225b55340d91b63": ("rejected-out-of-scope", "The title concerns sound-scene segmentation with same-class sources but does not establish a human-speech or spoken-language task. With title-only evidence, blind speech source separation membership is not supported.", None, None, None),
    "6ef606385df2873c8570937816958ffcb0e24480": ("rejected-out-of-scope", "The title concerns mixtures of singing voices rather than a human-speech or spoken-language task. With title-only evidence, blind speech source separation membership is not supported.", None, None, None),
    "6fd6e2e8ea62c3b9a66d02b0ee7526ddab6e0a74": ("confirmed-current-boundary", "The title explicitly concerns neural vocoders for generative waveform models. Title-only evidence supports waveform synthesis, without establishing audio fidelity or speed in deployment.", "voice-generation-and-control", "waveform-and-codec-generation", "waveform-synthesis"),
    "70672c82c3044944c88a807ed172d3bae1726224": ("reassigned-to-neighbor", "The title explicitly concerns speech spoofing detection and the role of speaker identity. Title-only evidence places it under spoofing and synthetic voice misuse rather than speaker verification.", "evaluation-deployment-and-consequence", "privacy-and-security", "spoofing-and-synthetic-voice-misuse"),
    "706f9d8fd024f6ca3ec3c6883db04b44cca003ab": ("rejected-out-of-scope", "The title concerns language-audio pretraining for animal species recognition and trait inference, not a human-speech or spoken-language task. It is outside this speech taxonomy.", None, None, None),
    "711d83af8c72e162159e84b6373017612be73a5b": ("rejected-out-of-scope", "The title concerns token pruning for a general audio-visual large language model and does not establish a human-speech or spoken-language task. With title-only evidence, acoustic-to-token mapping membership is not supported.", None, None, None),
    "72156810522bbfe62a02bb99c66e22f9697a5155": ("rejected-out-of-scope", "The title concerns sound-source localization and does not establish a human-speech or spoken-language task. With title-only evidence, spatial filtering membership is not supported.", None, None, None),
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
