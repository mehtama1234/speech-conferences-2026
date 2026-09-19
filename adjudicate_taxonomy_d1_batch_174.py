#!/usr/bin/env python3
"""Record the next eight evidence-bounded taxonomy adjudications."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "sun25h_interspeech": (
        "confirmed-current-boundary",
        "The abstract explains shorter Mandarin syllabic fricative nuclei through constriction, pressure release, voicing, and context, using forced alignment over spontaneous and read speech. The evidence supports articulatory-coordination, bounded by the corpus, apical versus regular vowels, duration analysis, and the stated fricative interpretation.",
        ["title", "abstract"], "sound-and-production", "articulatory-dynamics", "articulatory-coordination",
    ),
    "sun25i_interspeech": (
        "confirmed-current-boundary",
        "The abstract detects time regions containing overlapping speakers and adds speaker information to a progressive VAD/overlap model. The evidence supports target-conditioned-separation, bounded by WavLM and wav2vec comparisons, speaker attention, the AMI test set, and the reported F1 score.",
        ["title", "abstract"], "listening-and-separation", "source-separation", "target-conditioned-separation",
    ),
    "sung25_interspeech": (
        "confirmed-current-boundary",
        "The abstract jointly transcribes children with speech sound disorders and detects mispronunciations, using fused attention to emphasize relevant acoustic features. The evidence supports dysarthria-and-atypical-speech, bounded by the Korean children dataset, multitask objectives, CER/UAR measures, and baseline comparison.",
        ["title", "abstract"], "people-variation-and-health", "atypical-and-assistive-speech", "dysarthria-and-atypical-speech",
    ),
    "szalay25_interspeech": (
        "confirmed-current-boundary",
        "The abstract reduces annotation work for a child-and-accent-specific corpus through recording design, segmentation cues, out-of-domain diarization, and ASR followed by correction. The evidence supports speech-data-collection, bounded by AusKidTalk, the two WER settings, manual correction workflow, and the stated portability of the process.",
        ["title", "abstract"], "languages-accents-and-resources", "data-creation", "speech-data-collection",
    ),
    "szalay25b_interspeech": (
        "confirmed-current-boundary",
        "The abstract uses real-time and volumetric MRI to measure bilateral lateral channels, oral occlusion, timing, and acoustic intensity in Australian English /l/. The evidence supports articulatory-coordination, bounded by three speakers, three vowel contexts, MRI measurements, and the observed speaker/context variation.",
        ["title", "abstract"], "sound-and-production", "articulatory-dynamics", "articulatory-coordination",
    ),
    "szekely25_interspeech": (
        "confirmed-current-boundary",
        "The abstract reconstructs a personalised voice for augmentative communication across different amounts of available speech and adds user-guided prosody adaptation from dysarthric speech. The evidence supports augmentative-communication, bounded by the stroke-survivor case, zero-shot and fine-tuned TTS, data-availability scenarios, and the described prompt interaction.",
        ["title", "abstract"], "people-variation-and-health", "atypical-and-assistive-speech", "augmentative-communication",
    ),
    "tabatabaee25_interspeech": (
        "confirmed-current-boundary",
        "The abstract adapts speaker-verification models to noisy classrooms with augmented children’s speech and reports lower equal-error rates. The evidence supports speaker-verification, bounded by the x-vector and ECAPA-TDNN models, classroom datasets, babble noise, augmentation, and reported EER changes.",
        ["title", "abstract"], "people-variation-and-health", "identity-and-life-stage", "speaker-verification",
    ),
    "tabatabaee25b_interspeech": (
        "confirmed-current-boundary",
        "The abstract recovers oral and velum movement from acoustics by adding nasalance and source information to acoustic-to-articulatory inversion. The evidence supports articulatory-coordination, bounded by American English speakers, nasometry/nasopharyngoscopy comparison, two inversion models, and the reported oral-TV and nasalance gains.",
        ["title", "abstract"], "sound-and-production", "articulatory-dynamics", "articulatory-coordination",
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
