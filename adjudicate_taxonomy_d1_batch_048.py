#!/usr/bin/env python3
"""Record the next eight title-only D1 taxonomy adjudications."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "653efeb59c5b066720dc0c457bd2189a063fab37": ("rejected-out-of-scope", "The title concerns cross-modal deepfake detection but does not establish a human-speech, spoken-language, or synthetic-voice task. With title-only evidence, synthetic voice misuse membership is not supported.", None, None, None),
    "6599ad30ece84a9f571a837dbf05989981c9ac5b": ("confirmed-current-boundary", "The title explicitly concerns diarization and enhancement of meetings with multichannel spatial processing. Title-only evidence supports spatial filtering, without establishing meeting robustness.", "listening-and-separation", "spatial-listening", "spatial-filtering"),
    "681dfa90368a1b9545ee50a497eb8d71f2df77b6": ("confirmed-current-boundary", "The title explicitly concerns distributed-microphone speech enhancement. Title-only evidence supports time-frequency masking, without establishing enhancement quality across devices.", "listening-and-separation", "noise-enhancement", "time-frequency-masking"),
    "688146d07467757d9ff7aa3ccbfbdd338e639819": ("confirmed-current-boundary", "The title explicitly concerns dynamic speech networks and layer dropping. Title-only evidence supports latency and resource budget, without establishing the deployment tradeoff.", "evaluation-deployment-and-consequence", "deployment-cost", "latency-and-resource-budget"),
    "69f7a435ef273037fe9be59b226d0def924601b8": ("confirmed-current-boundary", "The title explicitly concerns noise-robust audiovisual automatic speech recognition. Title-only evidence supports acoustic-to-token mapping, without establishing the contribution of either modality.", "recognition-and-alignment", "acoustic-unit-learning", "acoustic-to-token-mapping"),
    "6adaacb3eaa8df84d8df088b8f48d59e9f658ef2": ("rejected-out-of-scope", "The title concerns denoising room impulse responses and does not establish a human-speech or spoken-language task. With title-only evidence, reverberant speech-room membership is not supported.", None, None, None),
    "6c213dec41c76bee60f40b339aa508476ef41d67": ("rejected-out-of-scope", "The title concerns a general neural audio autoencoder and does not establish a human-speech or spoken-language task. With title-only evidence, multiple-time-scale speech membership is not supported.", None, None, None),
    "6c78ad33fed0c4e824d0a8824fd810aa708948f6": ("rejected-out-of-scope", "The title concerns general independent-vector-analysis source separation and does not establish a human-speech or spoken-language task. With title-only evidence, blind speech source separation membership is not supported.", None, None, None),
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
