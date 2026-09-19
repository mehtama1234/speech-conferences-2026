#!/usr/bin/env python3
"""Record the tenth title-only D1 taxonomy adjudication batch."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "39856bd3d175d634475ff210326624df514c14c7": ("confirmed-current-boundary", "The title explicitly concerns multilingual automatic speech recognition using discrete tokens. Title-only evidence supports cross-lingual transfer.", "languages-accents-and-resources", "crosslingual-structure", "crosslingual-transfer"),
    "399e06ca9091a5fe36fdc3814cc6793a73014260": ("rejected-out-of-scope", "The title concerns automotive sound-field reproduction and does not establish a human-speech or spoken-language task. With title-only evidence, speech membership is not supported.", None, None, None),
    "39e9e6f5b005b274a971b07373a1ef0939a58b1f": ("confirmed-current-boundary", "The title explicitly concerns multilingual speaker verification. Title-only evidence supports speaker-verification membership.", "people-variation-and-health", "identity-and-life-stage", "speaker-verification"),
    "3a176b4c85bc9328e2657e7026ee503719c455d1": ("confirmed-current-boundary", "The title explicitly concerns speech discretization for discrete-token automatic speech recognition. Title-only evidence supports learned speech-unit membership.", "recognition-and-alignment", "acoustic-unit-learning", "self-supervised-speech-units"),
    "3a2f40f5fb10bbb29f77af4b4b9f9861e6846a39": ("rejected-out-of-scope", "The title concerns a general deep-audio watermark and does not establish speech or spoken-language evidence. With title-only evidence, speech accountability membership is not supported.", None, None, None),
    "3b9a2c34cd9e9dfe79350f9685af96c60fc5fe4c": ("reassigned-to-neighbor", "The title explicitly concerns Mandarin lip-to-speech synthesis, but not text-to-speech planning. Title-only evidence supports waveform synthesis more directly.", "voice-generation-and-control", "waveform-and-codec-generation", "waveform-synthesis"),
    "3c4b3a29df5e8841a5f1b92d67b6a3c285c355cd": ("confirmed-current-boundary", "The title explicitly concerns audio-visual target-speaker extraction for real-time processing. Title-only evidence supports target-conditioned separation.", "listening-and-separation", "source-separation", "target-conditioned-separation"),
    "3d75bc25e57a63180e334eaa6c8a9ba193f1d16f": ("confirmed-current-boundary", "The title explicitly concerns sEEG-driven speech synthesis. Title-only evidence supports non-airborne speech sensing, without claims about assistive communication or neural decoding quality.", "sound-and-production", "room-channel-and-sensing", "non-airborne-sensing"),
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
