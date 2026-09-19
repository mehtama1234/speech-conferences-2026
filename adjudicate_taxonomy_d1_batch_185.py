#!/usr/bin/env python3
"""Record the next eight evidence-bounded taxonomy adjudications."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "wardah25_interspeech": (
        "confirmed-current-boundary",
        "The abstract predicts overall speech quality and separate perceptual dimensions from degraded audio alone, using a large multi-database training set. The evidence supports quality-and-naturalness, bounded by SQ-AST, four-to-twelve-second clips, 106 databases, 165,791 samples, and stated external evaluations.",
        ["title", "abstract"], "evaluation-deployment-and-consequence", "metric-and-human-targets", "quality-and-naturalness",
    ),
    "watkins25_interspeech": (
        "confirmed-current-boundary",
        "The abstract tests F0-ratio jumps as a measure of creaky/modal voice and phonological contrast in Seoul Korean and Danish. The evidence supports periodic-source, bounded by the two languages, fortis/stød contrasts, gender effect, categorization results, and the unresolved Danish interpretation.",
        ["title", "abstract"], "sound-and-production", "source-generation", "periodic-source",
    ),
    "wei25_interspeech": (
        "confirmed-current-boundary",
        "The abstract separates disease-related from device, demographic, and environment-related information in respiratory-sound representations to reduce domain mismatch. The evidence supports clinical-speech-marker, bounded by DDE-MAE, the ICBHI dataset, dual encoders, and the stated classification result.",
        ["title", "abstract"], "people-variation-and-health", "clinical-markers", "clinical-speech-marker",
    ),
    "weilinghoff25_interspeech": (
        "confirmed-current-boundary",
        "The abstract evaluates Whisper across sociolinguistic corpora of Nigerian and Scottish English and measures effects of model size and file conditions. The evidence supports accent-robustness, bounded by ICE Nigeria/Scotland, WER and mixed-effects analysis, model-size comparison, and remaining diarization/hallucination problems.",
        ["title", "abstract"], "languages-accents-and-resources", "accent-dialect-and-cultural-meaning", "accent-robustness",
    ),
    "weirich25_interspeech": (
        "confirmed-current-boundary",
        "The abstract measures female fundamental frequency across hormone levels, cycle phases, ages, and speakers and finds an age effect but no cycle-phase effect. The evidence supports style-and-state-variation, bounded by 62 German participants, measured hormones, age/height/material covariates, and mean-F0 outcomes.",
        ["title", "abstract"], "people-variation-and-health", "identity-and-life-stage", "style-and-state-variation",
    ),
    "weizman25_interspeech": (
        "confirmed-current-boundary",
        "The abstract compares ASVspoof2019 and ASVspoof5 under changed bona-fide and spoofed-speech distributions and measures the resulting difficulty. The evidence supports spoofing-and-deepfake, bounded by the two challenge databases, genuine/spoof mismatch conditions, qualitative/quantitative comparisons, and the observed shift.",
        ["title", "abstract"], "evaluation-deployment-and-consequence", "privacy-and-security", "spoofing-and-deepfake",
    ),
    "wen25_interspeech": (
        "confirmed-current-boundary",
        "The abstract splits low- and high-frequency latent representations and predicts one from the other before residual-vector quantization, reducing redundancy in a neural speech codec. The evidence supports sampling-and-quantization, bounded by SPCODEC, the convolutional codec, group RVQ, tested bitrates, and MOS-POLQA results.",
        ["title", "abstract"], "sound-and-production", "time-frequency-measurement", "sampling-and-quantization",
    ),
    "wepner25_interspeech": (
        "confirmed-current-boundary",
        "The abstract compares human and ASR transcription of disfluent conversational speech and tests syntactic disfluencies, filler particles, pronunciation variation, and rate. The evidence supports disfluency-preservation, bounded by 54 listeners, nine ASR systems, WER/semantic measures, and the filler-particle finding.",
        ["title", "abstract"], "recognition-and-alignment", "boundaries-and-alignment", "disfluency-preservation",
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
