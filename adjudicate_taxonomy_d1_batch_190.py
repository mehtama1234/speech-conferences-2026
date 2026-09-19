#!/usr/bin/env python3
"""Record the next eight evidence-bounded taxonomy adjudications."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "xu25f_interspeech": (
        "confirmed-current-boundary",
        "The abstract embeds keyed watermarks in generated audio and recovers them under repeated insertion and variable length, with the key controlling who can decode. The evidence supports auditability-and-contestability, bounded by the WAKE watermarking framework, unauthorized-access/copyright setting, audio-quality and detection comparisons, and the abstract-level security claims.",
        ["title", "abstract"], "evaluation-deployment-and-consequence", "auditability-and-accountability", "auditability-and-contestability",
    ),
    "xu25g_interspeech": (
        "confirmed-current-boundary",
        "The abstract uses language models to correct ASR errors in conversational child speech, and shows that the benefit depends on the upstream recognizer and use of context. The evidence supports age-and-development, bounded by two child-conversation datasets, zero-shot and fine-tuned ASR outputs, and the reported successes and failures of correction.",
        ["title", "abstract"], "people-variation-and-health", "identity-and-life-stage", "age-and-development",
    ),
    "xu25h_interspeech": (
        "confirmed-current-boundary",
        "The abstract tests how contrastive focus changes prosodic grouping and syllable duration in Mandarin complex nominals, with tones and syntax affecting the result. The evidence supports prosodic-meaning, bounded by the mini-dialogue production design, numeral-classifier-noun phrases, focus spans, and the two experiments.",
        ["title", "abstract"], "meaning-and-interaction", "prosody-and-paralinguistics", "prosodic-meaning",
    ),
    "xu25i_interspeech": (
        "confirmed-current-boundary",
        "The paper reallocates model parameters during training, moving capacity from less-used regions to more useful ones without increasing the stated training budget. The evidence supports latency-and-resource, bounded by DMAO, CTC ASR, the LibriSpeech/TED-LIUM/Switchboard tests, architecture and model-size comparisons, and reported WER changes.",
        ["title", "abstract", "full_paper"], "evaluation-deployment-and-consequence", "deployment-cost", "latency-and-resource",
    ),
    "xu25k_interspeech": (
        "confirmed-current-boundary",
        "The abstract studies ASR for Chinese dialects and accented speech where data are scarce, using large unlabeled pretraining followed by supervised alignment and comparing projectors and language models. The evidence supports dialect-and-variety, bounded by the Data2vec2/LLM setup, the stated corpus sizes, dialect datasets, and reported recognition results.",
        ["title", "abstract"], "languages-accents-and-resources", "accent-dialect-and-cultural-meaning", "dialect-and-variety",
    ),
    "xue25_interspeech": (
        "confirmed-current-boundary",
        "The abstract routes easy multilingual speech to a direct transcription path and invokes a stronger ASR system only when difficulty warrants it. The evidence supports crosslingual-transfer, bounded by SIMA, the multilingual imbalance and language-identification comparison, three datasets, WER, and invocation-cost results.",
        ["title", "abstract"], "languages-accents-and-resources", "crosslingual-structure", "crosslingual-transfer",
    ),
    "xue25b_interspeech": (
        "confirmed-current-boundary",
        "The abstract measures how predictable words change comprehension of Dutch speech by listeners whose first languages differ, and tests whether written context helps. The evidence supports crosslingual-transfer, bounded by German and English listeners, Dutch sentential material, predictability conditions, translation responses, and the language-specific context effect.",
        ["title", "abstract"], "languages-accents-and-resources", "crosslingual-structure", "crosslingual-transfer",
    ),
    "yadav25_interspeech": (
        "confirmed-current-boundary",
        "The abstract learns general audio representations by predicting masked spectrogram patches with an xLSTM architecture and evaluates them on ten downstream tasks. The evidence supports self-supervised-speech-units, bounded by AxLSTM, AudioSet pretraining, the masked-patch objective, SSAST comparisons, and the reported performance/parameter counts.",
        ["title", "abstract"], "recognition-and-alignment", "acoustic-unit-learning", "self-supervised-speech-units",
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
