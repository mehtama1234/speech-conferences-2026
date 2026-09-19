#!/usr/bin/env python3
"""Record the next eight evidence-bounded taxonomy adjudications."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "wang25h_interspeech": (
        "confirmed-current-boundary",
        "The abstract combines independent vector analysis with a compact dual-channel recurrent model to enhance speech under low SNR while limiting computation. The evidence supports nonstationary-noise, bounded by IVA/GTCRN cooperation, dual-channel inputs, low-SNR conditions, and reported efficiency claims.",
        ["title", "abstract"], "listening-and-separation", "noise-enhancement", "nonstationary-noise",
    ),
    "wang25i_interspeech": (
        "confirmed-current-boundary",
        "The abstract evaluates pseudo-labels from an audio LLM's own decoding and uses them for reinforcement-learning domain adaptation without labeled target data. The evidence supports self-training-and-pseudo-labels, bounded by SI-SDA, ASR/SQA/S2TT tasks, public datasets, WER/BLEU, and the data-efficiency claim.",
        ["title", "abstract"], "languages-accents-and-resources", "low-resource-learning", "self-training-and-pseudo-labels",
    ),
    "wang25j_interspeech": (
        "confirmed-current-boundary",
        "The abstract reduces the cost of long-context speech separation by replacing quadratic attention with focused linear attention and gated processing. The evidence supports blind-source-separation, bounded by FLASepformer variants, multiple datasets, speed, memory, and state-of-the-art comparisons.",
        ["title", "abstract"], "listening-and-separation", "source-separation", "blind-source-separation",
    ),
    "wang25k_interspeech": (
        "confirmed-current-boundary",
        "The abstract recognizes emotion while jointly learning gender, speaker, and ASR tasks, using co-attention and a weighted contrastive loss to combine features and handle imbalance. The evidence supports paralinguistic-state, bounded by the naturalistic SER challenge, four tasks, SWFC, and reported performance gains.",
        ["title", "abstract"], "meaning-and-interaction", "prosody-and-paralinguistics", "paralinguistic-state",
    ),
    "wang25l_interspeech": (
        "confirmed-current-boundary",
        "The full paper compares semantic processing during spoken-word production in children with cochlear implants and normal-hearing peers using picture-word interference. The evidence supports augmentative-communication, bounded by the CI/NH groups, semantic relatedness manipulation, spoken production task, and observed interference difference.",
        ["title", "abstract", "full_paper"], "people-variation-and-health", "atypical-and-assistive-speech", "augmentative-communication",
    ),
    "wang25m_interspeech": (
        "confirmed-current-boundary",
        "The abstract unifies speech, general audio, and music understanding by routing specialized encoder outputs into an LLM and training a semantic-aware contrastive alignment objective. The evidence supports self-supervised-speech-units, bounded by U-SAM, MoE routing, cross-modal alignment, multiple benchmarks, and unseen-task results.",
        ["title", "abstract"], "recognition-and-alignment", "acoustic-unit-learning", "self-supervised-speech-units",
    ),
    "wang25o_interspeech": (
        "confirmed-current-boundary",
        "The abstract uses known loudspeaker/microphone geometry as an echo-path prior and adapts a stereo echo canceller according to tracked mismatch. The evidence supports acoustic-echo-cancellation, bounded by MCSSFDAF, process-noise adjustment, simulated and real recordings, reconvergence, and misalignment measures.",
        ["title", "abstract"], "listening-and-separation", "echo-reconstruction", "acoustic-echo-cancellation",
    ),
    "wang25q_interspeech": (
        "confirmed-current-boundary",
        "The abstract releases a multimodal deepfake dataset with synthesized environmental audio and video and evaluates separate audio-only and visual-only detection tasks. The evidence supports spoofing-and-deepfake, bounded by VCapAV, its text-to-audio/video generation pipeline, two baseline tasks, comparisons, and released code/data.",
        ["title", "abstract"], "evaluation-deployment-and-consequence", "privacy-and-security", "spoofing-and-deepfake",
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
