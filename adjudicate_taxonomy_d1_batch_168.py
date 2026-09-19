#!/usr/bin/env python3
"""Record the next eight evidence-bounded taxonomy adjudications."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "shi25e_interspeech": (
        "confirmed-current-boundary",
        "The abstract recognizes emotion from spontaneous speech by combining speech, context, and corrected text representations. The evidence supports paralinguistic-state, bounded by the stated SCT model, challenge and corpus evaluations, and reported macro-F1 comparisons.",
        ["title", "abstract"], "meaning-and-interaction", "prosody-and-paralinguistics", "paralinguistic-state",
    ),
    "shi25f_interspeech": (
        "confirmed-current-boundary",
        "The abstract builds one speech-assessment model that predicts naturalness, intelligibility, speaker characteristics, prosody, and noise measures across enhancement and synthesis settings. The evidence supports calibration-and-selective-use, bounded by the objective targets, URGENT24 benchmark, and the stated human-perception comparison.",
        ["title", "abstract"], "evaluation-deployment-and-consequence", "metric-and-human-targets", "calibration-and-selective-use",
    ),
    "shi25g_interspeech": (
        "confirmed-current-boundary",
        "The abstract releases standardized articulator contours and phonetic alignments from real-time MRI and tests them in phoneme and contour tasks. The evidence supports articulatory-coordination, bounded by the 75-speaker database, annotation and expert-verification process, and the three benchmark tasks.",
        ["title", "abstract"], "sound-and-production", "articulatory-dynamics", "articulatory-coordination",
    ),
    "shi25h_interspeech": (
        "reassigned-to-neighbor",
        "The abstract studies continuous unsupervised test-time adaptation of ASR models to individual children and reports remaining limits for non-linguistic child speech. The governing boundary is speech variation tied to age and development, not generic adaptation alone; the evidence supports age-and-development, bounded by the child-recognition data, two TTA methods, and the tested baselines.",
        ["title", "abstract"], "people-variation-and-health", "identity-and-life-stage", "age-and-development",
    ),
    "shim25_interspeech": (
        "confirmed-current-boundary",
        "The abstract tests whether open-source TTS systems generate prosodic boundaries that preserve syntactic distinctions, then adds training data to make selected cues more predictable. The evidence supports prosody-control, bounded by the five systems, punctuation contrasts, qualitative assessment, and cases that remained unsolved.",
        ["title", "abstract"], "voice-generation-and-control", "expression-and-interactive-control", "prosody-control",
    ),
    "shiota25_interspeech": (
        "confirmed-current-boundary",
        "The abstract introduces an in-the-wild Japanese database for speaker verification and replay and other physical-access spoofing attacks. The evidence supports spoofing-and-deepfake, bounded by the recorded attack scenarios, Japanese corpus, and the reported verification and detection uses.",
        ["title", "abstract"], "evaluation-deployment-and-consequence", "privacy-and-security", "spoofing-and-deepfake",
    ),
    "si25_interspeech": (
        "confirmed-current-boundary",
        "The abstract addresses class-incremental audio classification when both base and new classes have only a few examples, freezing an embedding extractor and updating a light classifier. The evidence supports few-shot-adaptation, bounded by the three public datasets, incremental protocol, and reported accuracy and complexity comparisons.",
        ["title", "abstract"], "languages-accents-and-resources", "low-resource-learning", "few-shot-adaptation",
    ),
    "siegert25_interspeech": (
        "confirmed-current-boundary",
        "The abstract constructs a German corpus from podcast and YouTube speech by self-identified LGBTQIA+ speakers and describes legal, ethical, and representational constraints. The evidence supports speech-data-collection, bounded by the source media, roughly 335 hours, more than 400 speakers, and the stated age and identity coverage.",
        ["title", "abstract"], "languages-accents-and-resources", "data-creation", "speech-data-collection",
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
