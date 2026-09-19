#!/usr/bin/env python3
"""Record the next eight evidence-bounded taxonomy adjudications."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "wang25aa_interspeech": (
        "confirmed-current-boundary",
        "The abstract turns picture-description behavior and speech organization into interpretable features for Alzheimer’s detection. The evidence supports clinical-speech-marker, bounded by visual attention, description quality, repetition, the no-special-equipment setting, and the reported accuracy.",
        ["title", "abstract"], "people-variation-and-health", "clinical-markers", "clinical-speech-marker",
    ),
    "wang25b_interspeech": (
        "confirmed-current-boundary",
        "The abstract reduces Whisper hallucinations on non-speech by identifying a small set of decoder heads and fine-tuning them with non-speech data. The evidence supports end-to-end-recovery, bounded by Whisper-large-v3, UrbanSound, three heads, LibriSpeech WER, and the reported hallucination reduction.",
        ["title", "abstract"], "evaluation-deployment-and-consequence", "robustness-and-shift", "end-to-end-recovery",
    ),
    "wang25ba_interspeech": (
        "confirmed-current-boundary",
        "The abstract converts between unseen speakers while separating content and prosody and using prompts to control the target speaking style. The evidence supports voice-conversion, bounded by Discl-VC, discrete prosody tokens, in-context flow matching, zero-shot speakers, and reported prosody-control results.",
        ["title", "abstract"], "voice-generation-and-control", "identity-and-conversion", "voice-conversion",
    ),
    "wang25c_interspeech": (
        "confirmed-current-boundary",
        "The abstract combines acoustic analysis and ultrasound tongue imaging to distinguish apical vowels from high front vowels in Eastern Zhenjiang Mandarin. The evidence supports articulatory-coordination, bounded by the two apical vowels, contrasting contexts, spectral measures, and anterior/posterior tongue observations.",
        ["title", "abstract"], "sound-and-production", "articulatory-dynamics", "articulatory-coordination",
    ),
    "wang25d_interspeech": (
        "confirmed-current-boundary",
        "The abstract jointly cancels acoustic echo and suppresses noise with a compact gated recurrent model whose cross-attention aligns delayed signals. The evidence supports acoustic-echo-cancellation, bounded by CAGCRN, AEC/NS joint operation, delay alignment, 0.07M parameters, and reported task performance.",
        ["title", "abstract"], "listening-and-separation", "echo-reconstruction", "acoustic-echo-cancellation",
    ),
    "wang25e_interspeech": (
        "confirmed-current-boundary",
        "The abstract creates multimodal speech-LLM training data by condensing paralinguistic labels and generating contextual spoken question-answer pairs, then compares model behavior with human data. The evidence supports paralinguistic-state, bounded by in-the-wild speech, CPQA generation, Qwen2-Audio evaluation, empathy reasoning, and reported correlation.",
        ["title", "abstract"], "meaning-and-interaction", "prosody-and-paralinguistics", "paralinguistic-state",
    ),
    "wang25f_interspeech": (
        "confirmed-current-boundary",
        "The abstract changes self-supervised spectrogram attention so irrelevant regions receive less weight, then evaluates learned representations on classification, keyword spotting, and environmental sound tasks. The evidence supports self-supervised-speech-units, bounded by ASDA, dual softmax/differential coefficients, the listed benchmarks, and reported scores.",
        ["title", "abstract"], "recognition-and-alignment", "acoustic-unit-learning", "self-supervised-speech-units",
    ),
    "wang25g_interspeech": (
        "confirmed-current-boundary",
        "The abstract uses self-training to enlarge data and handle incomplete segments for long dysarthric speech, addressing the limits of short command-style corpora. The evidence supports dysarthria-and-atypical-speech, bounded by the SAP dataset/challenge, Whisper adaptation, long-speech setting, and reported WER/Semantic Score ranking.",
        ["title", "abstract"], "people-variation-and-health", "atypical-and-assistive-speech", "dysarthria-and-atypical-speech",
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
