#!/usr/bin/env python3
"""Record the second abstract-bounded D2 taxonomy adjudication batch."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "06a45d5a7f24ca8a38dfc43d42033bc77ad32089": ("confirmed-current-boundary", "The abstract explicitly concerns audio-visual speech recognition in noise and an integrated speech-enhancement module. D2 supports speech enhancement membership, but not full-paper mechanism or benchmark generalization.", "listening-and-separation", "noise-enhancement", "speech-prior-denoising"),
    "06d2fdf3eaba73be9127cdc7915148764d059fbc": ("rejected-out-of-scope", "The abstract concerns anomalous sound detection and general audio features, not speech or spoken-language evidence; time-frequency terminology alone does not establish speech membership.", None, None, None),
    "085852d8c01df95279b17e54165cf8bcc327e8ff": ("reassigned-to-neighbor", "The abstract explicitly concerns speech emotion recognition under speaker and corpus shifts. Its object is nonliteral emotional state, not dialogue intent.", "meaning-and-interaction", "prosody-and-paralinguistics", "paralinguistic-state"),
    "08da8f18cb892647b29da770aa64bdc89e28eba1": ("rejected-out-of-scope", "The abstract identifies retrieval-augmented general audio generation and does not establish speech or spoken-language content; audio-language modeling alone is insufficient for this speech taxonomy.", None, None, None),
    "098f4e21120d05b0acb4c15705c1ba37e2a8e467": ("rejected-out-of-scope", "The abstract concerns industrial acoustic anomaly detection and explanation, not speech or spoken-language evidence; acoustic interpretability is not enough for speech membership.", None, None, None),
    "0af01b1801747cbafb93b3dff32bc1ed179c9b8d": ("confirmed-current-boundary", "The abstract explicitly studies spatial features for multi-channel speaker diarization and overlapping meeting speech. D2 supports spatial-listening membership without establishing full method behavior.", "listening-and-separation", "spatial-listening", "spatial-filtering"),
    "0c07fef3b5d669e0212be08d570e2b3c8c3447c7": ("confirmed-current-boundary", "The abstract explicitly concerns speech enhancement and uses internal pruning masks to estimate noise, VAD, and pitch properties under device constraints. D2 supports speech-prior enhancement membership.", "listening-and-separation", "noise-enhancement", "speech-prior-denoising"),
    "0ef0b2693e1aab1f0a7c06fe01b20c1f6a6be9d0": ("rejected-out-of-scope", "The abstract concerns targeted detection of general reference sounds in mixtures, not target speech or spoken-language sources; generic sound separation is outside this speech taxonomy.", None, None, None),
}

def main():
    payload = json.loads(QUEUE.read_text())
    rows = {r["paper_id"]: r for r in payload["rows"]}
    for pid, (decision, note, theme, subtheme, concept) in DECISIONS.items():
        row = rows[pid]
        if row["taxonomy_review_state"] == "taxonomy-adjudicated":
            raise SystemExit(f"already adjudicated: {pid}")
        row.update({"taxonomy_review_state": "taxonomy-adjudicated", "final_decision": decision, "reviewer_note": note, "reviewed_sections": ["title", "abstract"], "final_theme_id": theme, "final_subtheme_id": subtheme, "final_concept_id": concept})
    payload["adjudicated_count"] = sum(r["taxonomy_review_state"] == "taxonomy-adjudicated" for r in rows.values())
    payload["open_count"] = len(rows) - payload["adjudicated_count"]
    payload["decision_counts"] = {d: sum(r.get("final_decision") == d for r in rows.values() if r["taxonomy_review_state"] == "taxonomy-adjudicated") for d in sorted({r.get("final_decision") for r in rows.values() if r["taxonomy_review_state"] == "taxonomy-adjudicated"})}
    QUEUE.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({"batch": len(DECISIONS), "adjudicated": payload["adjudicated_count"], "open": payload["open_count"]}))

if __name__ == "__main__":
    main()
