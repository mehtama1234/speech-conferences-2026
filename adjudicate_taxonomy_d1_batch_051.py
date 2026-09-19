#!/usr/bin/env python3
"""Record the next eight title-only D1 taxonomy adjudications."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "783ca1357287e1c19e69bb14c20e4cfad58d7513": ("confirmed-current-boundary", "The title explicitly concerns multilingual speech recognition. Title-only evidence supports cross-lingual transfer, without establishing recognition quality across languages.", "languages-accents-and-resources", "crosslingual-structure", "cross-lingual-transfer"),
    "789a80acdec4a583c16afd2df41b2da969abbfad": ("reassigned-to-neighbor", "The title explicitly concerns ambiguity in speech-emotion annotation and uses audio-language models to augment human labels. Title-only evidence places it under paralinguistic state rather than listener effort.", "meaning-and-interaction", "prosody-and-paralinguistics", "paralinguistic-state"),
    "795b51a1a6ad481b22e277ca6095984a65f66f49": ("confirmed-current-boundary", "The title explicitly concerns speech enhancement using self-supervised speech representations. Title-only evidence supports learned speech units, without establishing representation quality or enhancement gains.", "recognition-and-alignment", "acoustic-unit-learning", "learned-speech-units"),
    "7fa35c3b31455b8d645fb29a9c35d1a71361cdb1": ("rejected-out-of-scope", "The title concerns transfer of audio representations for bioacoustics and does not establish a human-speech or spoken-language task. With title-only evidence, accessibility fit is not supported.", None, None, None),
    "803bf703bd7cfd4f7bb05078e582391d4ded9db1": ("rejected-out-of-scope", "The title concerns universal sound-event extraction and localization, not a human-speech or spoken-language task. With title-only evidence, target-conditioned speech separation membership is not supported.", None, None, None),
    "838fc7aa4deffa24d2a2ad4f46012edeba818640": ("confirmed-current-boundary", "The title explicitly concerns low-quality speech and text-to-speech artifacts evaluated through speech quality. Title-only evidence supports intelligibility versus naturalness, without establishing the reported quality relationship.", "voice-generation-and-control", "waveform-and-codec-generation", "intelligibility-versus-naturalness"),
    "83cc6c7acb98b0327743e95ef2ec8337b29486c6": ("confirmed-current-boundary", "The title explicitly concerns personalized keyword spotting using phonemes and prosody. Title-only evidence supports prosodic meaning, without establishing keyword-spotting accuracy or personalization benefit.", "meaning-and-interaction", "prosody-and-paralinguistics", "prosodic-meaning"),
    "83eb5e352285c2760a730ab63d706f0ab2d76159": ("confirmed-current-boundary", "The title explicitly concerns accented speech synthesis and speaker-embedding interactions with phonological rules. Title-only evidence supports text-to-speech planning, without establishing synthesis quality across accents.", "voice-generation-and-control", "content-planning", "text-to-speech-planning"),
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
