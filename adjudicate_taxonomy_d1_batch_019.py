#!/usr/bin/env python3
"""Record the eighth title-only D1 taxonomy adjudication batch."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "2b3bcd44dd8fd6a8819f6743cc2eb66870941ff3": ("confirmed-current-boundary", "The title explicitly concerns ALS dysarthria severity estimation from adapted Whisper speech recognition. Title-only evidence supports a clinical speech marker, without establishing clinical validity.", "people-variation-and-health", "clinical-markers", "clinical-speech-marker"),
    "2bb85a31496b5439a72808963ce78debd108eea4": ("confirmed-current-boundary", "The title explicitly concerns lightweight speaker verification. Title-only evidence supports speaker-verification membership.", "people-variation-and-health", "identity-and-life-stage", "speaker-verification"),
    "2bbdd2e5bc25d7b2c43c7d567990192ac2c453cb": ("reassigned-to-neighbor", "The title explicitly concerns an end-to-end speech codec for compression and enhancement. Title-only evidence supports sampling and quantization more directly than multiple time scales.", "sound-and-production", "time-frequency-measurement", "sampling-and-quantization"),
    "2cf3ff950c47f73a828be8ba72ecded16cbd9a63": ("confirmed-current-boundary", "The title explicitly concerns noise-robust speech emotion recognition. Title-only evidence supports paralinguistic-state membership.", "meaning-and-interaction", "prosody-and-paralinguistics", "paralinguistic-state"),
    "2d0e4481166e55eb34d6efb8a9e079aaae0ae73e": ("confirmed-current-boundary", "The title explicitly concerns a dialogue system for a dialogue challenge. Title-only evidence supports dialogue-state membership, without claims about conversational usefulness.", "meaning-and-interaction", "intent-and-dialogue-state", "dialogue-state"),
    "2d9bf6dc3865fda35c1c7eff2e70a35945fe076b": ("confirmed-current-boundary", "The title explicitly concerns speech enhancement using magnitude and phase band splits. Title-only evidence supports time-frequency masking within noise enhancement.", "listening-and-separation", "noise-enhancement", "spectral-mask"),
    "2e513071d71c24dc3f341dd389762c971f20a43e": ("confirmed-current-boundary", "The title explicitly concerns radar-based speech signals. Title-only evidence supports non-airborne speech sensing, without claims about sensing reliability.", "sound-and-production", "room-channel-and-sensing", "non-airborne-sensing"),
    "2e629793880f57253fa78cb9e58eba5a866b2f06": ("rejected-out-of-scope", "The title concerns multichannel active noise control and does not establish a human-speech or spoken-language task. With title-only evidence, speech membership is not supported.", None, None, None),
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
