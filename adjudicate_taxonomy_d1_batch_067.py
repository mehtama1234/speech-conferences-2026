#!/usr/bin/env python3
"""Record the next eight title-only D1 taxonomy adjudications."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "dcf1cfac25f51e1490915903a948998d3be86a38": ("rejected-out-of-scope", "The title concerns environment-sound deepfake detection and does not establish a human-speech or spoken-language task. With title-only evidence, synthetic voice misuse membership is not supported.", None, None, None),
    "ddd7e538b79b4a0847744a3cac05196060c8d39a": ("confirmed-current-boundary", "The title explicitly concerns speech recognition and translation. Title-only evidence supports acoustic-to-token mapping, without establishing recognition or translation quality.", "recognition-and-alignment", "acoustic-unit-learning", "acoustic-to-token"),
    "deab2a991a985b09dcbdc9baf60ee3b0d5379004": ("rejected-out-of-scope", "The title concerns audio-visual multi-speaker tracking but does not establish a human-speech or spoken-language task. With title-only evidence, turn-boundary prediction is not supported.", None, None, None),
    "deef773b3c27f7fd5de51ea7329364cf23586315": ("rejected-out-of-scope", "The title concerns universal sound separation and synthetic audio mixtures but does not establish a human-speech or spoken-language task. With title-only evidence, blind speech source separation membership is not supported.", None, None, None),
    "df0a895267ef8c1a0d57f87e55f8836d0c329722": ("reassigned-to-neighbor", "The title explicitly concerns target-speaker automatic speech recognition with a speaker-aware encoder. Title-only evidence places it under speaker adaptation rather than source separation.", "recognition-and-alignment", "context-and-open-vocabulary", "speaker-adaptation"),
    "df86196063981e670870ba8b6c8e60e7de661262": ("rejected-out-of-scope", "The title concerns membership inference against music diffusion models rather than a human-speech or spoken-language task. It is outside this speech taxonomy.", None, None, None),
    "dfd27df13f693bd9b9ab366e67fedd919132edfc": ("rejected-out-of-scope", "The title concerns general audio-video deepfake detection but does not establish a human-speech, spoken-language, or synthetic-voice task. With title-only evidence, synthetic voice misuse membership is not supported.", None, None, None),
    "e0dcf21c3bf580ce939cae4796e53f0d7a6e6eda": ("confirmed-current-boundary", "The title explicitly concerns controllable accent normalization using source-synthesis data. Title-only evidence supports accent robustness, without establishing normalization quality or accent coverage.", "languages-accents-and-resources", "accent-dialect-and-cultural-meaning", "accent-robustness"),
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
