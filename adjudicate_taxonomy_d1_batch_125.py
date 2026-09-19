#!/usr/bin/env python3
"""Record the next eight evidence-bounded taxonomy adjudications."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "lee25g_interspeech": ("rejected-out-of-scope", "The abstract concerns open-vocabulary separation of generic audio sources and does not establish a human-speech or spoken-language object. The source-separation method alone is not enough for speech-taxonomy membership.", ["title", "abstract"], None, None, None),
    "lee25i_interspeech": ("confirmed-current-boundary", "The abstract explicitly develops a cascaded flow-matching speech-enhancement system and evaluates its denoising quality and sampling cost. The evidence supports speech-prior denoising, bounded by the reported baselines and function-evaluation comparisons.", ["title", "abstract"], "listening-and-separation", "noise-enhancement", "speech-prior-denoising"),
    "lepage25_interspeech": ("confirmed-current-boundary", "The abstract develops and evaluates speaker verification using same-speaker positives from different recording conditions. The evidence supports speaker verification, bounded by the self-supervised sampling method and VoxCeleb1-O evaluation.", ["title", "abstract"], "people-variation-and-health", "identity-and-life-stage", "speaker-verification"),
    "lepagnol25_interspeech": ("confirmed-current-boundary", "The abstract uses retrieved examples to prompt few-shot spoken-language understanding and evaluates intent-related tasks on SLU benchmarks. The evidence supports intent in context, while the few-shot setting bounds the transfer claim.", ["title", "abstract"], "meaning-and-interaction", "intent-and-dialogue-state", "intent-in-context"),
    "lertpetchpun25_interspeech": ("confirmed-current-boundary", "The abstract evaluates speech emotion recognition under naturalistic conditions and explicitly addresses label disagreement and imbalance. The evidence supports paralinguistic state, bounded by the challenge data and reported ensemble.", ["title", "abstract"], "meaning-and-interaction", "prosody-and-paralinguistics", "paralinguistic-state"),
    "leschly25_interspeech": ("confirmed-current-boundary", "The abstract predicts mild cognitive impairment from spontaneous speech and uses interpretable symptom domains to explain the prediction. The evidence supports a clinical speech marker, without establishing clinical diagnosis from the reported cohort.", ["title", "abstract"], "people-variation-and-health", "clinical-markers", "clinical-speech-marker"),
    "letellier25_interspeech": ("confirmed-current-boundary", "The abstract predicts vocal intensity across calibrated bilingual datasets and tests whether representations generalize across recording datasets. The evidence supports within-speaker state variation, bounded by intensity, languages, and datasets.", ["title", "abstract"], "people-variation-and-health", "identity-and-life-stage", "style-and-state-variation"),
    "levkovitch25_interspeech": ("reassigned-to-neighbor", "The abstract synthesizes binaural speech from monaural speech and source position and evaluates generalization across rooms. The governing boundary is spatial acoustic rendering, closest to spatial listening, rather than interactive generation latency.", ["title", "abstract"], "listening-and-separation", "spatial-listening", "spatial-filtering"),
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
