#!/usr/bin/env python3
"""Record the next eight evidence-bounded taxonomy adjudications."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "wu25g_interspeech": (
        "confirmed-current-boundary",
        "The abstract generates unseen-speaker speech with emotion controlled from text, image, or speech prompts while separating content, timbre, emotion, and prosody. The evidence supports style-and-emotion-control, bounded by MPE-TTS, multimodal prompt encoding, prosody prediction, diffusion synthesis, and objective/subjective tests.",
        ["title", "abstract"], "voice-generation-and-control", "expression-and-interactive-control", "style-and-emotion-control",
    ),
    "wu25h_interspeech": (
        "confirmed-current-boundary",
        "The abstract extracts a selected speaker from an audio-visual mixture using language-model constraints as additional supervision, including multilingual and missing-visual conditions. The evidence supports target-conditioned-separation, bounded by AV-TSE, visual cues, PSLM/PLM supervision, no added inference cost, and robustness tests.",
        ["title", "abstract"], "listening-and-separation", "source-separation", "target-conditioned-separation",
    ),
    "wu25i_interspeech": (
        "confirmed-current-boundary",
        "The abstract compares watermark-based proactive defenses with passive deepfake detectors under common data, metrics, and adversarial distortions. The evidence supports spoofing-and-deepfake, bounded by the unified evaluation framework, shared training/testing protocol, attack types, vulnerabilities, and released code.",
        ["title", "abstract"], "evaluation-deployment-and-consequence", "privacy-and-security", "spoofing-and-deepfake",
    ),
    "wu25j_interspeech": (
        "confirmed-current-boundary",
        "The abstract simulates moving vocal-tract boundaries during diphthongs with a fixed-grid immersed-boundary wave model and compares formant trajectories with other models and recordings. The evidence supports vocal-tract-filter, bounded by the 2D Eulerian/Lagrangian method, three diphthongs, F1/F2 comparisons, and reported correlations.",
        ["title", "abstract"], "sound-and-production", "source-generation", "vocal-tract-filter",
    ),
    "wu25k_interspeech": (
        "confirmed-current-boundary",
        "The abstract adds a statistical watermark to autoregressive speech generation so outputs remain traceable and tests detectability after re-encoding. The evidence supports auditability-and-contestability, bounded by watermark detection, audio quality, re-encoded mismatch, and the reported experiments.",
        ["title", "abstract"], "evaluation-deployment-and-consequence", "auditability-and-accountability", "auditability-and-contestability",
    ),
    "wu25l_interspeech": (
        "confirmed-current-boundary",
        "The abstract automates phone mappings for cross-language alignment so low-resource languages can use existing aligners without expert-built mappings. The evidence supports pronunciation-variation, bounded by CrossPhon, 14 languages in seven families, expert agreement rates, and cross-language alignment tests.",
        ["title", "abstract"], "recognition-and-alignment", "pronunciation-and-variation", "pronunciation-variation",
    ),
    "wu25m_interspeech": (
        "confirmed-current-boundary",
        "The abstract evaluates Mandarin-English child speech assessment in telehealth, including multiple speakers, languages, and code-switching, and measures preprocessing/diarization effects on ASR. The evidence supports age-and-development, bounded by 53 sessions, child and code-switching WER, Whisper, speaker diarization, and the clinical-service setting.",
        ["title", "abstract"], "people-variation-and-health", "identity-and-life-stage", "age-and-development",
    ),
    "xia25_interspeech": (
        "confirmed-current-boundary",
        "The abstract adapts Whisper for streaming recognition by combining quasi-monotonic alignment, infinite left context, finite right look-ahead, and wait-k decoding. The evidence supports long-context-decoding, bounded by MFLA, CIF training, latency/quality tradeoff, streaming applications, and the stated theoretical/experimental results.",
        ["title", "abstract"], "recognition-and-alignment", "context-and-open-vocabulary", "long-context-decoding",
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
