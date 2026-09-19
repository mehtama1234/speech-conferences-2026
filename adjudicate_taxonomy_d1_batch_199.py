#!/usr/bin/env python3
"""Record the next eight evidence-bounded taxonomy adjudications."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "zhao25e_interspeech": (
        "confirmed-current-boundary",
        "The abstract cancels loudspeaker echo from a multichannel microphone signal by first estimating source directions and then using those cues in the near-end estimator. The evidence supports acoustic-echo-cancellation, bounded by the two-stage DOA/AEC design, multichannel and far-end inputs, varied acoustic environments, and baseline comparisons.",
        ["title", "abstract"], "listening-and-separation", "echo-reconstruction", "acoustic-echo-cancellation",
    ),
    "zhao25f_interspeech": (
        "confirmed-current-boundary",
        "The abstract presents an open toolkit that turns enhancement, separation, super-resolution, and target extraction models into usable workflows with optimization, audio-format support, and evaluation tools. The evidence supports latency-and-resource, bounded by ClearerVoice-Studio, pretrained models, deployment tooling, SpeechScore, benchmark/community claims, and the abstract-level adoption report.",
        ["title", "abstract"], "evaluation-deployment-and-consequence", "deployment-cost", "latency-and-resource",
    ),
    "zhao25g_interspeech": (
        "confirmed-current-boundary",
        "The abstract generates stereo singing voice whose spatial character and reverberation match a scene image, using visual features in text conditioning and a one-step decoder. The evidence supports prosody-control, bounded by VS-Singer, visual/acoustic matching, stereo output, scene perspective, and the reported single-step synthesis results.",
        ["title", "abstract"], "voice-generation-and-control", "expression-and-interactive-control", "prosody-control",
    ),
    "zhao25h_interspeech": (
        "confirmed-current-boundary",
        "The abstract reduces the cost of a noisy-speech enhancement front end by resampling frames and pruning less informative frequency bands while preserving ASR performance. The evidence supports speech-prior-denoising, bounded by layer-wise resampling, sub-band pruning, synthetic/real noisy data, BSRNN comparison, and the reported overhead reduction.",
        ["title", "abstract"], "listening-and-separation", "noise-enhancement", "speech-prior-denoising",
    ),
    "zhao25i_interspeech": (
        "confirmed-current-boundary",
        "The abstract synthesizes room impulse responses from source/receiver positions and reverberant speech by encoding room geometry and acoustic propagation without a detailed 3D model. The evidence supports reverberant-mixture, bounded by TA-RIR, topology-aware embeddings, propagation-informed decoding, reverberation time, and complexity comparison.",
        ["title", "abstract"], "sound-and-production", "room-channel-and-sensing", "reverberant-mixture",
    ),
    "zhao25j_interspeech": (
        "confirmed-current-boundary",
        "The paper asks whether infants can learn Cantonese tone categories from natural speech by using variation across contexts when no cue is invariant. The evidence supports dialect-and-variety, bounded by six Cantonese tones, naturalistic speech, distributional learning across contexts, acquisition comparisons, and the proposed ease-of-learning relation.",
        ["title", "abstract", "full_paper"], "languages-accents-and-resources", "accent-dialect-and-cultural-meaning", "dialect-and-variety",
    ),
    "zhao25k_interspeech": (
        "confirmed-current-boundary",
        "The abstract trains a zero-shot TTS codec to reject watermarked prompts so copyrighted speaker identity cannot be cloned, while leaving unwatermarked speech usable. The evidence supports voice-privacy, bounded by watermark-aware codec muting, zero-shot TTS, attack robustness, prompt conditions, and speech-quality preservation.",
        ["title", "abstract"], "evaluation-deployment-and-consequence", "privacy-and-security", "voice-privacy",
    ),
    "zhao25l_interspeech": (
        "confirmed-current-boundary",
        "The abstract first suppresses noise and then uses estimated F0 to restore harmonic components that masking removed, targeting speech structure and perceived quality together. The evidence supports speech-prior-denoising, bounded by DMHRN, NRM/HR stages, DNS3, P.835/P.808 measures, and the reported quality/noise-suppression results.",
        ["title", "abstract"], "listening-and-separation", "noise-enhancement", "speech-prior-denoising",
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
