#!/usr/bin/env python3
"""Record the next eight evidence-bounded taxonomy adjudications."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "okabe25_interspeech": (
        "confirmed-current-boundary",
        "The abstract omits decoder-score computations through masked and speculative decoding while preserving WER and reducing real-time factor. The evidence supports latency and resource budget, bounded by TED-LIUM2 and the AR comparison.",
        ["title", "abstract"], "evaluation-deployment-and-consequence", "deployment-cost", "latency-and-resource",
    ),
    "okamoto25_interspeech": (
        "confirmed-current-boundary",
        "The abstract integrates four-language simultaneous speech-to-speech translation with a portable multiple-sound-spot system. The evidence supports cross-lingual transfer, bounded by the four-language on-device demonstration and spatial presentation system.",
        ["title", "abstract"], "languages-accents-and-resources", "crosslingual-structure", "crosslingual-transfer",
    ),
    "onda25_interspeech": (
        "confirmed-current-boundary",
        "The abstract tests discrete-token ASR on non-native speech while varying the language used to learn tokenization, with the goal of accent robustness from native speech data. The evidence supports accent robustness, bounded by the ISIB analysis and tested tokenization languages.",
        ["title", "abstract"], "languages-accents-and-resources", "accent-dialect-and-cultural-meaning", "accent-robustness",
    ),
    "onda25b_interspeech": (
        "reassigned-to-neighbor",
        "The abstract resynthesizes native speech into foreign-accented speech and adds duration modification to preserve accent realization. The governing boundary is voice conversion, not recognition robustness, because the central operation changes the acoustic realization for simulation.",
        ["title", "abstract"], "voice-generation-and-control", "identity-and-conversion", "voice-conversion",
    ),
    "onda25c_interspeech": (
        "confirmed-current-boundary",
        "The abstract jointly optimizes discrete tokenization and ASR through differentiable k-means and reports improved phonetic purity and recognition. The evidence supports self-supervised speech units, bounded by the learned tokenization and ASR/resynthesis experiments.",
        ["title", "abstract"], "recognition-and-alignment", "acoustic-unit-learning", "self-supervised-speech-units",
    ),
    "oneata25_interspeech": (
        "confirmed-current-boundary",
        "The abstract studies how bilingual visually grounded speech models associate novel words with novel objects and explains the resulting confusion through visual embeddings. The evidence supports referential grounding, bounded by English/French/Dutch model combinations and image-paired speech.",
        ["title", "abstract"], "meaning-and-interaction", "grounding-and-action", "referential-grounding",
    ),
    "ong25_interspeech": (
        "confirmed-current-boundary",
        "The abstract introduces a low-resource Faetar ASR benchmark from field recordings, with limited transcriptions and additional unlabeled speech, and reports foundation-model baselines. The evidence supports speech-data collection, bounded by Faetar, the hours and labels described, and the baseline pipeline.",
        ["title", "abstract"], "languages-accents-and-resources", "data-creation", "speech-data-collection",
    ),
    "ormaechea25_interspeech": (
        "confirmed-current-boundary",
        "The abstract generates and externally refines simplified text from French spontaneous-speech transcriptions while measuring simplicity gain and semantic preservation. The evidence supports referential grounding as the closest meaning-preservation boundary, bounded by the speech-simplification task, judges, and SARI/COMET results; it does not establish spoken-audio generation.",
        ["title", "abstract", "full_paper_excerpt"], "meaning-and-interaction", "grounding-and-action", "referential-grounding",
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
