#!/usr/bin/env python3
"""Record the next eight title-only D1 taxonomy adjudications."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "8f23e5c63ba6928faf75a98f2d4213964f2ccc6f": ("confirmed-current-boundary", "The title explicitly concerns localization of speech deepfakes. Title-only evidence supports spoofing and deepfake detection, without establishing localization accuracy.", "evaluation-deployment-and-consequence", "privacy-and-security", "spoofing-and-deepfake"),
    "8f879a97fe9480dfd7865131eeb0b223162d215b": ("rejected-out-of-scope", "The title concerns a general audio foundation model and does not establish a human-speech or spoken-language task. With title-only evidence, calibration and selective use for speech is not supported.", None, None, None),
    "8fdee400f75abe12a4578b1dea440b4f7d30d498": ("rejected-out-of-scope", "The title concerns phonation-mode classification in singing rather than a human-speech or spoken-language task. With title-only evidence, periodic vocal-fold source membership is not supported for this speech taxonomy.", None, None, None),
    "90613cc6054def6586fb8fc7887f8389ffc620a3": ("rejected-out-of-scope", "The title explicitly transfers speech models to underwater acoustic target recognition; the target is not human speech or spoken language. It is outside this speech taxonomy.", None, None, None),
    "90be2c38a59d31432f9de2e4c948a3901920b49c": ("reassigned-to-neighbor", "The title explicitly concerns speech-to-text embedding projection for language models. Title-only evidence places it under acoustic-to-token mapping rather than cross-lingual transfer.", "recognition-and-alignment", "acoustic-unit-learning", "acoustic-to-token"),
    "91299ef1ffee830ed63f6cecbcde9b12e5a80d08": ("confirmed-current-boundary", "The title explicitly concerns an efficient low-bitrate speech codec. Title-only evidence supports waveform and codec generation, without establishing reconstruction quality or bitrate tradeoffs.", "voice-generation-and-control", "waveform-and-codec-generation", "neural-vocoder"),
    "9212141e66d29e78e0c08d6d524689fd842b6867": ("rejected-out-of-scope", "The title concerns prompt weighting for zero-shot audio-language classification but does not establish a human-speech or spoken-language task. With title-only evidence, intent-in-context membership is not supported.", None, None, None),
    "96c95d11aa84c71461d39332c1b84183cbc85fd9": ("confirmed-current-boundary", "The title explicitly concerns noise-robust audio-visual speech recognition. Title-only evidence supports acoustic-to-token mapping, without establishing the contribution of the cross-modal bottleneck.", "recognition-and-alignment", "acoustic-unit-learning", "acoustic-to-token"),
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
