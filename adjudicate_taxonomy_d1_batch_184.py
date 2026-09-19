#!/usr/bin/env python3
"""Record the next eight evidence-bounded taxonomy adjudications."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "wang25s_interspeech": (
        "confirmed-current-boundary",
        "The abstract reconstructs clean speech from noisy mel spectra with a one-pass flow-matching model and optionally uses transcripts to strengthen alignment and quality. The evidence supports speech-prior-denoising, bounded by FlowSE, mel supervision, text/no-text inference, latency claim, and generative-SE comparisons.",
        ["title", "abstract"], "listening-and-separation", "noise-enhancement", "speech-prior-denoising",
    ),
    "wang25t_interspeech": (
        "confirmed-current-boundary",
        "The abstract separates multiple utterances from a single channel while estimating an unknown number of speakers and their active regions. The evidence supports blind-source-separation, bounded by the attractor module, known/unknown source-count settings, synthesized LibriSpeech/WHAM data, noise/reverberation, and activity/source results.",
        ["title", "abstract"], "listening-and-separation", "source-separation", "blind-source-separation",
    ),
    "wang25u_interspeech": (
        "confirmed-current-boundary",
        "The abstract adapts one Whisper-style model to new speech tasks without full retraining by using a gated feature-fusion layer over a generative task format. The evidence supports few-shot-adaptation, bounded by six speech tasks, task-specific feature selection, the encoder-decoder setup, and reported adaptation gains.",
        ["title", "abstract"], "languages-accents-and-resources", "low-resource-learning", "few-shot-adaptation",
    ),
    "wang25v_interspeech": (
        "confirmed-current-boundary",
        "The abstract creates and validates a Mandarin benchmark for prosodic features and their interactions with syntax, semantics, and pragmatics, then compares speech LLMs with humans. The evidence supports prosodic-meaning, bounded by eight MSPB tasks, expert-validated recordings, six models, and the reported subtle-prosody failures.",
        ["title", "abstract"], "meaning-and-interaction", "prosody-and-paralinguistics", "prosodic-meaning",
    ),
    "wang25w_interspeech": (
        "confirmed-current-boundary",
        "The abstract tests whether audio-visual self-supervised representations encode the timing between visible articulation and voicing by tracking phonetic information over time. The evidence supports self-supervised-speech-units, bounded by AV-HuBERT versus HuBERT, classifier probing, audio-visual lag, and the reported temporal-resolution limitation.",
        ["title", "abstract"], "recognition-and-alignment", "acoustic-unit-learning", "self-supervised-speech-units",
    ),
    "wang25x_interspeech": (
        "confirmed-current-boundary",
        "The abstract generates speech dialogues through metadata, scripts, speaker voices, and paralinguistic TTS tags, then evaluates the synthetic conversations against human judgments. The evidence supports dialogue-state, bounded by the three-stage SpeechDialogueFactory pipeline, privacy/cost motivation, automatic-human correlation, and quality comparison.",
        ["title", "abstract"], "meaning-and-interaction", "intent-and-dialogue-state", "dialogue-state",
    ),
    "wang25y_interspeech": (
        "confirmed-current-boundary",
        "The abstract adapts streaming multi-talker ASR instances to a selected speaker using speaker-wise activity rather than enrollment audio or an explicit query. The evidence supports target-conditioned-separation, bounded by speaker-specific kernels, overlapping speech, offline/streaming settings, and reported performance.",
        ["title", "abstract"], "listening-and-separation", "source-separation", "target-conditioned-separation",
    ),
    "wang25z_interspeech": (
        "confirmed-current-boundary",
        "The abstract adapts multilingual speech foundation models under few-shot conditions with fine-tuning choices, augmentation, and language-identification-aware CTC regularization. The evidence supports crosslingual-transfer, bounded by ML-SUPERB 2.0, LID/ASR tasks, adaptation strategies, challenge ranking, and reported accuracy/CER changes.",
        ["title", "abstract"], "languages-accents-and-resources", "crosslingual-structure", "crosslingual-transfer",
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
