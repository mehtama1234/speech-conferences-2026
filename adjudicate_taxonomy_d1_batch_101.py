#!/usr/bin/env python3
"""Record the next eight evidence-bounded taxonomy adjudications."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "gutscher25_interspeech": ("confirmed-current-boundary", "The title and abstract explicitly classify Austrian dialects and regress geographic location from speech across many locations. The evidence supports dialect and variety, without establishing clean geographic boundaries.", ["title", "abstract"], "languages-accents-and-resources", "accent-dialect-and-cultural-meaning", "dialect-and-variety"),
    "guzik25_interspeech": ("confirmed-current-boundary", "The title and abstract explicitly reduce spatial aliasing in microphone-array beamforming and evaluate spatial capture. The evidence supports spatial filtering, without proving all array geometries.", ["title", "abstract"], "listening-and-separation", "spatial-listening", "spatial-filtering"),
    "halim25_interspeech": ("reassigned-to-neighbor", "The title and abstract explicitly recognize ambiguous emotional states from speech foundation models and inspect token-level evidence. This is paralinguistic state, not dialogue intent.", ["title", "abstract"], "meaning-and-interaction", "prosody-and-paralinguistics", "paralinguistic-state"),
    "halpern25_interspeech": ("reassigned-to-neighbor", "The title and abstract explicitly relate acoustic and listener-rated speech measures in people with head and neck cancer for clinical monitoring. The governing object is a clinical speech marker, not time-scale analysis.", ["title", "abstract"], "people-variation-and-health", "clinical-markers", "clinical-speech-marker"),
    "hamann25_interspeech": ("reassigned-to-neighbor", "The title and abstract explicitly test how Japanese phonotactics and language experience affect perception of loan and foreign sequences. This belongs under dialect and variety structure, not cultural meaning as a social interpretation.", ["title", "abstract"], "languages-accents-and-resources", "accent-dialect-and-cultural-meaning", "dialect-and-variety"),
    "hameed25_interspeech": ("confirmed-current-boundary", "The title and abstract explicitly collect community speech recordings for six under-resourced Middle Eastern languages and test their effect on speech technology. The evidence supports speech data collection, without proving equal coverage.", ["title", "abstract"], "languages-accents-and-resources", "data-creation", "speech-data-collection"),
    "han25_interspeech": ("reassigned-to-neighbor", "The title and abstract explicitly prune self-supervised diarization models to reduce size and accelerate inference under resource constraints. The governing boundary is latency and resource budget, not microphone coloration.", ["title", "abstract"], "evaluation-deployment-and-consequence", "deployment-cost", "latency-and-resource"),
    "han25b_interspeech": ("confirmed-current-boundary", "The title and abstract explicitly generate clean speech from noisy and reverberant evidence while reducing sampling steps. The evidence supports speech-prior denoising, without proving fidelity in all noise conditions.", ["title", "abstract"], "listening-and-separation", "noise-enhancement", "speech-prior-denoising"),
}

def main():
    payload = json.loads(QUEUE.read_text())
    rows = {r["paper_id"]: r for r in payload["rows"]}
    for pid, (decision, note, sections, theme, subtheme, concept) in DECISIONS.items():
        row = rows[pid]
        if row["taxonomy_review_state"] == "taxonomy-adjudicated":
            raise SystemExit(f"already adjudicated: {pid}")
        row.update({"taxonomy_review_state": "taxonomy-adjudicated", "final_decision": decision, "reviewer_note": note, "reviewed_sections": sections, "final_theme_id": theme, "final_subtheme_id": subtheme, "final_concept_id": concept})
    payload["adjudicated_count"] = sum(r["taxonomy_review_state"] == "taxonomy-adjudicated" for r in rows.values())
    payload["open_count"] = len(rows) - payload["adjudicated_count"]
    payload["decision_counts"] = {d: sum(r.get("final_decision") == d for r in rows.values() if r["taxonomy_review_state"] == "taxonomy-adjudicated") for d in sorted({r.get("final_decision") for r in rows.values() if r["taxonomy_review_state"] == "taxonomy-adjudicated"})}
    QUEUE.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({"batch": len(DECISIONS), "adjudicated": payload["adjudicated_count"], "open": payload["open_count"]}))

if __name__ == "__main__":
    main()
