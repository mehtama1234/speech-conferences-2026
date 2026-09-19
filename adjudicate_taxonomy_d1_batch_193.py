#!/usr/bin/env python3
"""Record the next eight evidence-bounded taxonomy adjudications."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "yang25o_interspeech": (
        "confirmed-current-boundary",
        "The abstract reconstructs clean speech from severe noise with a continuous autoregressive generative model and compares discrete, masked, mel, and learned-latent choices. The evidence supports speech-prior-denoising, bounded by the continuous AR enhancement setup, representation choices, and the abstract-level severe-noise results.",
        ["title", "abstract"], "listening-and-separation", "noise-enhancement", "speech-prior-denoising",
    ),
    "yang25p_interspeech": (
        "confirmed-current-boundary",
        "The abstract adapts Whisper to code-switching with soft prompts while keeping most parameters frozen, testing the trade-off between new-language performance, prior-language retention, and training cost. The evidence supports code-switching, bounded by SPT/SPT4ASR, SEAME and ASRU2019, prompt variants, and reported error reductions.",
        ["title", "abstract"], "languages-accents-and-resources", "crosslingual-structure", "code-switching",
    ),
    "yao25_interspeech": (
        "confirmed-current-boundary",
        "The abstract anonymizes speaker identity while retaining linguistic content and emotion by separating those attributes into distinct representations. The evidence supports voice-privacy, bounded by EASY, factorized distillation, VoicePrivacy datasets, leakage protection, and the reported preservation/privacy results.",
        ["title", "abstract"], "evaluation-deployment-and-consequence", "privacy-and-security", "voice-privacy",
    ),
    "yao25b_interspeech": (
        "confirmed-current-boundary",
        "The abstract verifies a speaker from speech whose wording is not fixed, so the model must isolate identity from semantic content. The evidence supports speaker-verification, bounded by SCD-Conformer, dual-branch and frame/utterance disentanglement, text-independent trials, and the reported baseline improvement.",
        ["title", "abstract"], "people-variation-and-health", "identity-and-life-stage", "speaker-verification",
    ),
    "yazawa25_interspeech": (
        "confirmed-current-boundary",
        "The abstract shows that fluency judgments depend on listener language background and on how speech rate, pauses, and repetitions are measured. The evidence supports listener-effort, bounded by Japanese speakers' English, 16 listeners, the J-AESOP corpus, Bayesian modeling, and the native/nonnative rating differences.",
        ["title", "abstract"], "people-variation-and-health", "human-centered-accessibility", "listener-effort",
    ),
    "ye25_interspeech": (
        "confirmed-current-boundary",
        "The abstract tests whether the timing of a visible hand beat shifts perceived lexical stress and spoken-word recognition along a continuum. The evidence supports prosodic-meaning, bounded by Dutch disyllabic words, nine beat timings, 40 participants, audiovisual interaction, and the feedback-resistant gradient result.",
        ["title", "abstract"], "meaning-and-interaction", "prosody-and-paralinguistics", "prosodic-meaning",
    ),
    "ye25b_interspeech": (
        "confirmed-current-boundary",
        "The abstract aligns dysfluent speech with intended text while retaining partial matches, phoneme similarity, and segmentation needed for disorder analysis. The evidence supports alignment, bounded by Neural LCS, simulated and real PPA data, phoneme-level modeling, and the reported alignment/segmentation results.",
        ["title", "abstract"], "recognition-and-alignment", "boundaries-and-alignment", "alignment",
    ),
    "yoneyama25_interspeech": (
        "confirmed-current-boundary",
        "The abstract studies streaming neural vocoders under causal processing, limited parallelism, CPU-only resources, and the need to balance fidelity against latency and memory. The evidence supports latency-and-resource, bounded by MS-Wavehax, chunk-size and throughput analysis, causal/non-causal conditions, subjective quality, and deployment constraints.",
        ["title", "abstract"], "evaluation-deployment-and-consequence", "deployment-cost", "latency-and-resource",
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
