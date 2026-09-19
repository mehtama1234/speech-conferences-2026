#!/usr/bin/env python3
"""Record the first title-only D1 taxonomy adjudication batch."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "02243661b4fee8c9a88d369aa883fa870956ec84": ("rejected-out-of-scope", "The title names a large audio-language model but does not establish a human-speech or spoken-language task. With title-only evidence, speech membership is not supported.", None, None, None),
    "038b5e264b9c82c821a7a5a950349d6c7af968bd": ("confirmed-current-boundary", "The title explicitly concerns speech super-resolution in low-bandwidth conditions. Title-only evidence supports the signal-resolution and multiple-time-scale boundary, but not detailed mechanism or performance claims.", "sound-and-production", "time-frequency-measurement", "multi-resolution-signal"),
    "0431020f65a8b81c27946dd682982ee4610aca37": ("reassigned-to-neighbor", "The title explicitly concerns dialogue silence intention classification. Title-only evidence places it under dialogue state rather than turn-boundary timing.", "meaning-and-interaction", "intent-and-dialogue-state", "dialogue-state"),
    "0474ae80a5a5bfc4371b4cdeb8bab58c6333d9b1": ("confirmed-current-boundary", "The title explicitly concerns streaming speaker diarization and speaker embeddings. Title-only evidence supports blind/source separation membership, without claims about diarization quality or streaming behavior.", "listening-and-separation", "source-separation", "blind-source-separation"),
    "04bc5dc9cb6f4ffdb8109153c0762ceb4ec93fba": ("confirmed-current-boundary", "The title explicitly concerns streaming speech-LLM semantic chunking and label delay. Title-only evidence supports long-context decoding within speech recognition and interaction.", "recognition-and-alignment", "context-and-open-vocabulary", "long-context-decoding"),
    "0510abedf28ab2ff580cde1a691e1189cc53fe73": ("confirmed-current-boundary", "The title explicitly concerns multimodal emotion recognition from speech-related inputs. Title-only evidence supports paralinguistic-state membership, without establishing clinical or psychological validity.", "meaning-and-interaction", "prosody-and-paralinguistics", "paralinguistic-state"),
    "064179583b8ff35904bee372f1aa7729625802d3": ("confirmed-current-boundary", "The title explicitly links speech to voice-native clinical CT analysis. Title-only evidence supports a clinical speech-marker boundary, without establishing diagnostic validity.", "people-variation-and-health", "clinical-markers", "clinical-speech-marker"),
    "06582771395aa0de89d76be0f5adf6519d9e99dc": ("reassigned-to-neighbor", "The title explicitly concerns multilingual speech recognition and translation. Title-only evidence supports cross-lingual transfer more directly than acoustic-to-token mapping.", "languages-accents-and-resources", "crosslingual-structure", "crosslingual-transfer"),
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
