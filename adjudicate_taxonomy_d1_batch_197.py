#!/usr/bin/env python3
"""Record the next eight evidence-bounded taxonomy adjudications."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "zhang25h_interspeech": (
        "confirmed-current-boundary",
        "The abstract generates keyword examples near the decision boundary by making grapheme insertions, deletions, and substitutions, targeting the rare hard negatives that ordinary data miss. The evidence supports open-vocabulary-recognition, bounded by GraphemeAug, synthetic hard negatives, held-out evaluation, AUC, and positive/ambient-audio quality checks.",
        ["title", "abstract"], "recognition-and-alignment", "context-and-open-vocabulary", "open-vocabulary-recognition",
    ),
    "zhang25i_interspeech": (
        "confirmed-current-boundary",
        "The abstract co-registers vocal-tract MRI and respiratory plethysmography so articulatory motion and breathing can be measured on the same timeline during speech. The evidence supports articulatory-coordination, bounded by the acquisition/analysis protocol, two production experiments, linguistic focus, and preliminary timing results.",
        ["title", "abstract"], "sound-and-production", "articulatory-dynamics", "articulatory-coordination",
    ),
    "zhang25j_interspeech": (
        "confirmed-current-boundary",
        "The abstract analyzes a speech-enhancement challenge to show that bandwidth mismatch, label noise, hard acoustic conditions, and single metrics distort system conclusions. The evidence supports quality-and-naturalness, bounded by URGENT 2024, multi-domain data, cleaning/evaluation analysis, human-correlated metrics, and the challenge scope.",
        ["title", "abstract"], "evaluation-deployment-and-consequence", "metric-and-human-targets", "quality-and-naturalness",
    ),
    "zhang25k_interspeech": (
        "confirmed-current-boundary",
        "The abstract makes a neural speech codec vary its frame rate with local temporal information density, trading token rate against reconstruction quality and real-time efficiency. The evidence supports sampling-and-quantization, bounded by TFC/VFR, entropy-based allocation, lower frame rates, reconstruction quality, and downstream-efficiency aim.",
        ["title", "abstract"], "sound-and-production", "time-frequency-measurement", "sampling-and-quantization",
    ),
    "zhang25l_interspeech": (
        "confirmed-current-boundary",
        "The abstract compresses speech to 1.2 kbps while preserving its time-frequency structure through LSP quantization and joint STFT/cross-entropy training. The evidence supports sampling-and-quantization, bounded by LSPnet/LPCNet, the hybrid loss, resource-constrained real-time use, bitrate, quality, and compute comparisons.",
        ["title", "abstract"], "sound-and-production", "time-frequency-measurement", "sampling-and-quantization",
    ),
    "zhang25m_interspeech": (
        "confirmed-current-boundary",
        "The abstract assesses children's fluency in Tamil and Malay by combining multilingual ASR, timing/error measures, and a small-ground-truth GPT classifier. The evidence supports age-and-development, bounded by the two low-resource languages, child speech, human fluency examples, objective metrics, baselines, and reported accuracy.",
        ["title", "abstract"], "people-variation-and-health", "identity-and-life-stage", "age-and-development",
    ),
    "zhang25n_interspeech": (
        "confirmed-current-boundary",
        "The abstract transfers information from a large RNN-T into a pruned small model by sharing pruning structure and combining distillation losses, targeting useful recognition under limited computation. The evidence supports latency-and-resource, bounded by pruned RNN-Ts, Aishell-1, same-size training comparison, multi-loss distillation, and CER reduction.",
        ["title", "abstract"], "evaluation-deployment-and-consequence", "deployment-cost", "latency-and-resource",
    ),
    "zhang25o_interspeech": (
        "confirmed-current-boundary",
        "The abstract tests whether speaker anonymization preserves intelligibility when the content encoder was trained in another language, then adapts English-only and multilingual self-supervised encoders with Japanese speech. The evidence supports voice-privacy, bounded by Japanese/Mandarin evaluation, language mismatch, identity protection, intelligibility, and multilingual adaptation.",
        ["title", "abstract"], "evaluation-deployment-and-consequence", "privacy-and-security", "voice-privacy",
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
