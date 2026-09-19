#!/usr/bin/env python3
"""Record the second title-only D1 taxonomy adjudication batch."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "069e6db011dcf996ba8b2bb540a3b5d8d3edebb6": ("confirmed-current-boundary", "The title explicitly concerns prosody transfer in speech-to-speech translation using speech tokens. Title-only evidence supports prosody-control membership.", "voice-generation-and-control", "expression-and-interactive-control", "prosody-control"),
    "06a2330b327e7f133776f8145b955405caed8904": ("confirmed-current-boundary", "The title explicitly concerns multichannel speech enhancement and relative channel fusion. Title-only evidence supports time-frequency masking within speech enhancement.", "listening-and-separation", "noise-enhancement", "spectral-mask"),
    "06a9e45523b1b67eda62ac12b6db46c06167f30e": ("confirmed-current-boundary", "The title explicitly concerns anti-spoofing models for speech or voice authentication. Title-only evidence supports spoofing and synthetic-voice misuse.", "evaluation-deployment-and-consequence", "privacy-and-security", "spoofing-and-deepfake"),
    "075e67a89d63d18e2bc50fc08d56c1a64930499c": ("rejected-out-of-scope", "The title concerns personal sound zones and acoustic control but does not establish a human-speech or spoken-language task. With title-only evidence, speech membership is not supported.", None, None, None),
    "07bf93966087f1a0a3ee5f7735fa4d6aed40a53d": ("confirmed-current-boundary", "The title explicitly concerns geometry-agnostic speech enhancement. Title-only evidence supports spatial filtering within speech enhancement.", "listening-and-separation", "spatial-listening", "spatial-filtering"),
    "08ad5f25492709dddba346ca401f29fac4fa380d": ("rejected-out-of-scope", "The title explicitly concerns music source separation, not human speech or spoken-language evidence.", None, None, None),
    "09213e8ddcf4f227af2c7b167e960c420d62e3f4": ("confirmed-current-boundary", "The title explicitly concerns speaker adaptation in automatic speech recognition. Title-only evidence supports speaker-adaptation membership.", "recognition-and-alignment", "context-and-open-vocabulary", "speaker-adaptation"),
    "0b2e98d178862a3c87fda6e70159c2324e9d2446": ("confirmed-current-boundary", "The title explicitly concerns multimodal emotion recognition in conversations. Title-only evidence supports paralinguistic-state membership, without claims about emotional validity.", "meaning-and-interaction", "prosody-and-paralinguistics", "paralinguistic-state"),
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
