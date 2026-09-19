#!/usr/bin/env python3
"""Record the next eight evidence-bounded taxonomy adjudications."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "yamamoto25_interspeech": (
        "confirmed-current-boundary",
        "The abstract predicts how intelligible binaural speech will be for hearing-impaired listeners without requiring intrusive signals, while replacing costly attention blocks with Mamba temporal processing. The evidence supports word-error-versus-understanding, bounded by CPC2, binaural input, the Mamba-versus-transformer comparison, parameter size, and reported prediction performance.",
        ["title", "abstract"], "evaluation-deployment-and-consequence", "metric-and-human-targets", "word-error-versus-understanding",
    ),
    "yamashita25_interspeech": (
        "confirmed-current-boundary",
        "The abstract corrects ASR output for rare or domain-specific words by adding synthetic rare-word examples and phonetic context from N-best hypotheses. The evidence supports domain-and-context-biasing, bounded by English and Japanese data, generative error correction, over-correction risk, and reported WER/CER changes.",
        ["title", "abstract"], "recognition-and-alignment", "context-and-open-vocabulary", "domain-and-context-biasing",
    ),
    "yan25_interspeech": (
        "confirmed-current-boundary",
        "The abstract tests whether EEG auditory-attention decoding performance is inflated by blocked experimental design, comparing block and non-block recordings and model families. The evidence supports non-airborne-sensing, bounded by scalp/ear EEG, AAD, temporal-autocorrelation risk, neural phase-locking analysis, and the reported design-dependent accuracy change.",
        ["title", "abstract"], "sound-and-production", "room-channel-and-sensing", "non-airborne-sensing",
    ),
    "yan25b_interspeech": (
        "confirmed-current-boundary",
        "The abstract classifies exacerbated versus stable speech in people with COPD or asthma from fused acoustic features, aiming at non-invasive monitoring. The evidence supports clinical-speech-marker, bounded by the TACTICAS dataset, respiratory conditions, feature fusion, classifier comparison, and the stated monitoring aim.",
        ["title", "abstract"], "people-variation-and-health", "clinical-markers", "clinical-speech-marker",
    ),
    "yang25_interspeech": (
        "confirmed-current-boundary",
        "The abstract separates speakers without knowing the speaker count in advance by iteratively deriving speaker representations and identifying the mixture channel. The evidence supports blind-source-separation, bounded by the encoder-decoder contextual module, similarity-based counting, speaker-separation tests, and the reported counting/separation results.",
        ["title", "abstract"], "listening-and-separation", "source-separation", "blind-source-separation",
    ),
    "yang25b_interspeech": (
        "confirmed-current-boundary",
        "The abstract uses mouse vocalizations to classify autism-spectrum-disorder model mice against wild-type mice, establishing a biomedical vocal-marker task rather than ordinary human speech recognition. The evidence supports clinical-speech-marker, bounded by the MADUV challenge, audible and ultrasound recordings, high-rate sampling, baseline features, and the reported UAR values.",
        ["title", "abstract"], "people-variation-and-health", "clinical-markers", "clinical-speech-marker",
    ),
    "yang25c_interspeech": (
        "confirmed-current-boundary",
        "The abstract uses an enrollment recording as a detailed target description and cross-attends it with a mixture to extract an unseen sound class. The evidence supports target-conditioned-separation, bounded by the shared latent space, time/frequency processing, zero-shot target classes, and the reported extraction results.",
        ["title", "abstract"], "listening-and-separation", "source-separation", "target-conditioned-separation",
    ),
    "yang25d_interspeech": (
        "confirmed-current-boundary",
        "The abstract separates music sources under a real-time constraint with a causal lightweight model, explicitly trading model size and latency against separation quality. The evidence supports blind-source-separation, bounded by Band-SCNet, MUSDB18-HQ, causal processing, the 92 ms latency setting, parameter count, and SDR comparison.",
        ["title", "abstract"], "listening-and-separation", "source-separation", "blind-source-separation",
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
