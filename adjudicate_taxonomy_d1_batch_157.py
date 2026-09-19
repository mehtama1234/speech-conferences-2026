#!/usr/bin/env python3
"""Record the next eight evidence-bounded taxonomy adjudications."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "prakash25_interspeech": (
        "confirmed-current-boundary",
        "The abstract reconciles multiple ASR outputs with language-model correction and uses the resulting pseudo-labels for semi-supervised training. The evidence supports self-training and pseudo-label expansion, bounded by the multi-ASR/LLM comparisons and downstream semi-supervised datasets.",
        ["title", "abstract"], "languages-accents-and-resources", "low-resource-learning", "self-training-and-pseudo-labels",
    ),
    "prakrankamanant25_interspeech": (
        "rejected-out-of-scope",
        "The abstract explicitly studies text-based depression detection on Thai and English text datasets and does not establish spoken speech or a speech-derived clinical marker. Text-only depression detection is outside this speech taxonomy.",
        ["title", "abstract"], None, None, None,
    ),
    "pratapsingh25_interspeech": (
        "reassigned-to-neighbor",
        "The abstract explains children’s ASR errors through physiological, cognitive, and extrinsic factors and quantifies their causal effects across systems. The governing boundary is age and development, not auditability, because child speech variation is the object being explained.",
        ["title", "abstract"], "people-variation-and-health", "identity-and-life-stage", "age-and-development",
    ),
    "premananth25_interspeech": (
        "confirmed-current-boundary",
        "The abstract estimates individual schizophrenia symptom severity from speech, video, and text rather than only classifying diagnosis. The evidence supports clinical speech markers, bounded by the multimodal symptom-severity task and stated unimodal/multimodal comparisons.",
        ["title", "abstract"], "people-variation-and-health", "clinical-markers", "clinical-speech-marker",
    ),
    "premananth25b_interspeech": (
        "confirmed-current-boundary",
        "The abstract analyzes non-native accented English through acoustic and articulatory measures and proposes accent-strength quantification without phonetic transcription. The evidence supports accent robustness, bounded by the accented/native comparison and the stated coordination features.",
        ["title", "abstract"], "languages-accents-and-resources", "accent-dialect-and-cultural-meaning", "accent-robustness",
    ),
    "proctor25_interspeech": (
        "confirmed-current-boundary",
        "The abstract uses real-time and volumetric MRI to characterize Australian English rhotic articulation and coordinated tongue/labial gestures across speakers. The evidence supports articulatory coordination, bounded by four speakers, three vowel contexts, and the observed rhotic configurations.",
        ["title", "abstract"], "sound-and-production", "articulatory-dynamics", "articulatory-coordination",
    ),
    "pu25_interspeech": (
        "confirmed-current-boundary",
        "The abstract performs direct speech-to-speech translation across languages and adds a synthetic translation corpus for limited data. The evidence supports cross-lingual transfer, bounded by SLAM-TR, SynStard-1000, and the FLEURS comparison.",
        ["title", "abstract"], "languages-accents-and-resources", "crosslingual-structure", "crosslingual-transfer",
    ),
    "pulikodan25_interspeech": (
        "confirmed-current-boundary",
        "The abstract questions WER as the sole target when ASR feeds LLM applications and proposes a downstream-aware evaluation measure. The evidence supports word-error versus understanding, bounded by ASR error correction and the proposed LLM-application analysis.",
        ["title", "abstract"], "evaluation-deployment-and-consequence", "metric-and-human-targets", "word-error-versus-understanding",
    ),
}


def main():
    payload = json.loads(QUEUE.read_text())
    rows = {r["paper_id"]: r for r in payload["rows"]}
    for pid, (decision, note, sections, theme, subtheme, concept) in DECISIONS.items():
        row = rows[pid]
        if row["taxonomy_review_state"] == "taxonomy-adjudicated":
            raise SystemExit(f"already adjudicated: {pid}")
        row.update({
            "taxonomy_review_state": "taxonomy-adjudicated",
            "final_decision": decision,
            "reviewer_note": note,
            "reviewed_sections": sections,
            "final_theme_id": theme,
            "final_subtheme_id": subtheme,
            "final_concept_id": concept,
        })
    adjudicated = sum(r["taxonomy_review_state"] == "taxonomy-adjudicated" for r in rows.values())
    payload["adjudicated_count"] = adjudicated
    payload["open_count"] = len(rows) - adjudicated
    decisions = sorted({r.get("final_decision") for r in rows.values() if r["taxonomy_review_state"] == "taxonomy-adjudicated"})
    payload["decision_counts"] = {d: sum(r.get("final_decision") == d for r in rows.values() if r["taxonomy_review_state"] == "taxonomy-adjudicated") for d in decisions}
    QUEUE.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({"batch": len(DECISIONS), "adjudicated": adjudicated, "open": payload["open_count"]}))


if __name__ == "__main__": main()
