#!/usr/bin/env python3
"""Record the next eight evidence-bounded taxonomy adjudications."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "slomianka25_interspeech": (
        "confirmed-current-boundary",
        "The abstract measures how babble noise changes turn transfers, overlap, conversation length, and perceived difficulty in three-person conversations. The evidence supports turn-boundary, bounded by ten groups, two noise levels, quiet controls, objective timing measures, and subjective ratings.",
        ["title", "abstract"], "meaning-and-interaction", "turn-taking-and-repair", "turn-boundary",
    ),
    "smith25_interspeech": (
        "confirmed-current-boundary",
        "The abstract uses the target reading text to improve verbatim ASR and detect reading miscues directly, including child and atypical speech cases. The evidence supports disfluency-preservation, bounded by the two case studies, prompted architecture, and reported transcription and miscue comparisons.",
        ["title", "abstract"], "recognition-and-alignment", "boundaries-and-alignment", "disfluency-preservation",
    ),
    "smith25b_interspeech": (
        "confirmed-current-boundary",
        "The abstract uses brainstem fMRI during sustained vowel phonation to examine neural involvement in speech motor control. The evidence supports non-airborne-sensing, bounded by four participants, two vowels, 15-second trials, contrastive activation patterns, and the preliminary nature of the observations.",
        ["title", "abstract"], "sound-and-production", "room-channel-and-sensing", "non-airborne-sensing",
    ),
    "so25_interspeech": (
        "confirmed-current-boundary",
        "The abstract evaluates Cantonese forced alignment against human boundaries and identifies checked syllables and connected speech as failure points. The evidence supports alignment, bounded by spontaneous Hong Kong Cantonese interviews, two tailored models, phone boundaries, and the manual-adjustment comparison.",
        ["title", "abstract"], "recognition-and-alignment", "boundaries-and-alignment", "alignment",
    ),
    "sofer25_interspeech": (
        "confirmed-current-boundary",
        "The abstract measures and reduces separation between audio and text embeddings in CLAP and tests the result on text-audio retrieval. The evidence supports acoustic-to-token, bounded by CLIP/CLAP embedding spaces, the modality classifier and gradient-reversal intervention, and the reported retrieval experiments.",
        ["title", "abstract"], "recognition-and-alignment", "acoustic-unit-learning", "acoustic-to-token",
    ),
    "someki25_interspeech": (
        "confirmed-current-boundary",
        "The abstract prunes speech foundation-model computation dynamically using frame context, speaker, acoustic-event, and language information. The evidence supports latency-and-resource, bounded by OWSM, the 56.7 GFLOP reduction, the BLEU comparison, and inference-time context.",
        ["title", "abstract"], "evaluation-deployment-and-consequence", "deployment-cost", "latency-and-resource",
    ),
    "song25b_interspeech": (
        "confirmed-current-boundary",
        "The abstract replaces part of Transformer self-attention with RWKV-based modules to lower sequence-processing cost while preserving bidirectional context for ASR. The evidence supports latency-and-resource, bounded by REB-former, LibriSpeech 100h, reported WER, speed, and complexity results.",
        ["title", "abstract"], "evaluation-deployment-and-consequence", "deployment-cost", "latency-and-resource",
    ),
    "song25c_interspeech": (
        "confirmed-current-boundary",
        "The abstract adapts a self-supervised neural diarization pipeline, combines clustering outputs, and reports challenge-set diarization error. The evidence supports speaker-verification, bounded by the MISP 2025 AVSD track, WavLM module, clustering and DOVER-Lap fusion, and the evaluation-set result.",
        ["title", "abstract"], "people-variation-and-health", "identity-and-life-stage", "speaker-verification",
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
