#!/usr/bin/env python3
"""Record the next eight evidence-bounded taxonomy adjudications."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "silveira25_interspeech": (
        "confirmed-current-boundary",
        "The abstract compares intonation patterns in Alagoas and São Paulo varieties of Brazilian Portuguese using boundary-token and F0 measures. The evidence supports dialect-and-variety, bounded by ten male speakers, the interview corpus, 695 tokens, and the stated terminal and non-terminal boundaries.",
        ["title", "abstract"], "languages-accents-and-resources", "accent-dialect-and-cultural-meaning", "dialect-and-variety",
    ),
    "simko25_interspeech": (
        "confirmed-current-boundary",
        "The abstract models articulatory planning as a controller balancing effort against acoustic recognition of target vowels. The evidence supports articulatory-coordination, bounded by the self-supervised objective, isolated American-English vowels, simulations, and near-optimal parameter estimates.",
        ["title", "abstract"], "sound-and-production", "articulatory-dynamics", "articulatory-coordination",
    ),
    "singh25_interspeech": (
        "confirmed-current-boundary",
        "The abstract assigns speaker labels and counts in multimodal diarization through trainable cross-modal embeddings and data-driven clustering. The evidence supports speaker-verification, bounded by the AVA-AVD corpus, missing-modality masking, diarization error rate, and reported comparisons.",
        ["title", "abstract"], "people-variation-and-health", "identity-and-life-stage", "speaker-verification",
    ),
    "singh25b_interspeech": (
        "confirmed-current-boundary",
        "The abstract recognizes emotion in naturalistic speech by fusing acoustic and text representations and using an LLM to correct conflicting multimodal predictions. The evidence supports paralinguistic-state, bounded by the categorical and dimensional challenge tasks, the listed encoders, and the reported baseline gains.",
        ["title", "abstract"], "meaning-and-interaction", "prosody-and-paralinguistics", "paralinguistic-state",
    ),
    "singh25c_interspeech": (
        "reassigned-to-neighbor",
        "The abstract retrieves spoken query terms from audio using learned sparse representations and hierarchical indexing, addressing scaling rather than merely modeling a generic acoustic unit. The evidence supports open-vocabulary-recognition, bounded by query-by-example search, the TF-IDF/HNSW design, and the reported speed and accuracy comparison.",
        ["title", "abstract"], "recognition-and-alignment", "adaptation-and-open-vocabulary", "open-vocabulary-recognition",
    ),
    "singh25d_interspeech": (
        "confirmed-current-boundary",
        "The abstract learns language-agnostic speech tokens for query-by-example spoken-term retrieval across multilingual, code-switched, and unseen-language settings. The evidence supports self-supervised-speech-units, bounded by the tokenizer, multi-stage retrieval, speaker-invariance tests, and cross-language comparisons.",
        ["title", "abstract"], "recognition-and-alignment", "acoustic-unit-learning", "self-supervised-speech-units",
    ),
    "sinha25_interspeech": (
        "reassigned-to-neighbor",
        "The abstract improves zero-shot child ASR by selecting self-supervised representations that retain speaker-invariant phonetic information, without child-specific training data. The governing boundary is child speech variation, not generic representation learning; the evidence supports age-and-development, bounded by the three SSL models, layer analysis, child ASR data, and WER comparison.",
        ["title", "abstract"], "people-variation-and-health", "identity-and-life-stage", "age-and-development",
    ),
    "sirigiaju25_interspeech": (
        "confirmed-current-boundary",
        "The abstract assesses pronunciation from phoneme-level goodness-of-pronunciation vectors when expert labels and samples are scarce, using speech augmentation and an i-vector representation. The evidence supports pronunciation-variation, bounded by the two datasets, few-shot training, augmentation choices, and supervised/unsupervised comparisons.",
        ["title", "abstract"], "recognition-and-alignment", "pronunciation-and-variation", "pronunciation-variation",
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


if __name__ == "__main__":
    main()
