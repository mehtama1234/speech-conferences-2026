#!/usr/bin/env python3
"""Record the next eight evidence-bounded taxonomy adjudications."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "hoq25_interspeech": ("confirmed-current-boundary", "The title and abstract explicitly predict mean-opinion scores for synthesized speech and quantify uncertainty in that quality estimate. The evidence supports quality and naturalness, without proving human judgment in every setting.", ["title", "abstract"], "evaluation-deployment-and-consequence", "metric-and-human-targets", "quality-and-naturalness"),
    "horiguchi25_interspeech": ("reassigned-to-neighbor", "The title and abstract explicitly improve guided speaker embeddings under overlapping speech and measure speaker-verification performance. The governing task is speaker verification, not voice generation identity control.", ["title", "abstract"], "people-variation-and-health", "identity-and-life-stage", "speaker-verification"),
    "horiguchi25b_interspeech": ("confirmed-current-boundary", "The title and abstract explicitly pretrain multi-speaker identification from fully overlapped mixtures for diarization without a target enrollment condition. The evidence supports blind source separation, without proving unique source recovery in every mixture.", ["title", "abstract"], "listening-and-separation", "source-separation", "blind-source-separation"),
    "horii25_interspeech": ("confirmed-current-boundary", "The title and abstract explicitly analyze child phoneme-recognition errors from kindergarten through grade 10 and how they change with age. The evidence supports age and developmental speech, without proving all child-ASR failure causes.", ["title", "abstract"], "people-variation-and-health", "identity-and-life-stage", "age-and-development"),
    "hou25_interspeech": ("confirmed-current-boundary", "The title and abstract explicitly rank and select named-entity bias words for contextual ASR under large bias lists. The evidence supports domain and context biasing, without proving every vocabulary condition.", ["title", "abstract"], "recognition-and-alignment", "context-and-open-vocabulary", "domain-and-context-biasing"),
    "hou25b_interspeech": ("reassigned-to-neighbor", "The title and abstract explicitly benchmark speech assistants on comprehension, recognition, semantic response, acoustic quality, and conversational ability. The central object is quality and naturalness evaluation, not interaction latency alone.", ["title", "abstract"], "evaluation-deployment-and-consequence", "metric-and-human-targets", "quality-and-naturalness"),
    "hovsepyan25_interspeech": ("confirmed-current-boundary", "The title and abstract explicitly measure speech power-spectrum differences associated with Parkinson's disease and motor or neural mechanisms. The evidence supports a clinical speech marker, without establishing diagnosis or causal neural measurement.", ["title", "abstract"], "people-variation-and-health", "clinical-markers", "clinical-speech-marker"),
    "hrabanek25_interspeech": ("reassigned-to-neighbor", "The title and abstract explicitly test creaky phonation as an acoustic cue to a Korean stop contrast in perception. The speech object is phonation at the vocal source, not prosodic meaning.", ["title", "abstract"], "sound-and-production", "source-generation", "periodic-source"),
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
