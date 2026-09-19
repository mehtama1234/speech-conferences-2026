#!/usr/bin/env python3
"""Record the next eight evidence-bounded taxonomy adjudications."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "maison25_interspeech": ("reassigned-to-neighbor", "The abstract's main deliverable is a 600-hour Quebec French accented-speech corpus with cleaned transcripts and aligned audio; the ASR experiments demonstrate its use. The closer boundary is speech-data collection rather than accent robustness alone.", ["title", "abstract"], "languages-accents-and-resources", "data-creation", "speech-data-collection"),
    "maji25_interspeech": ("confirmed-current-boundary", "The abstract detects depression from spoken language using speech foundation models and tests English and Bengali data under transcription variation. The evidence supports a clinical speech marker, bounded by the two datasets and foundation-model settings.", ["title", "abstract"], "people-variation-and-health", "clinical-markers", "clinical-speech-marker"),
    "mak25_interspeech": ("confirmed-current-boundary", "The abstract resolves multiple Cantonese character pronunciations for text-to-speech using speech-guided grapheme-to-phoneme conversion and evaluates unseen speech. The evidence supports pronunciation variation, bounded by Cantonese jyutping and the synthetic-data training procedure.", ["title", "abstract"], "recognition-and-alignment", "pronunciation-and-variation", "pronunciation-variation"),
    "makishima25_interspeech": ("reassigned-to-neighbor", "The abstract jointly recognizes and diarizes several fully overlapping speakers and learns speaker embeddings without a selected enrollment target. The governing boundary is assigning hidden concurrent sources, so blind source separation is closer than target-conditioned separation.", ["title", "abstract"], "listening-and-separation", "source-separation", "blind-source-separation"),
    "male25_interspeech": ("confirmed-current-boundary", "The abstract learns one speech representation that serves both streaming and offline ASR and analyzes acoustic versus semantic information across layers. The evidence supports acoustic-to-token mapping, bounded by the multilingual ASR and downstream evaluations.", ["title", "abstract"], "recognition-and-alignment", "acoustic-unit-learning", "acoustic-to-token"),
    "malisz25_interspeech": ("confirmed-current-boundary", "The abstract relates contextual predictability and discourse to acoustic distinctiveness, duration, vowel space, and stress in Polish speech. The evidence supports prosodic meaning, bounded by the PRODIS read-speech corpus and language model.", ["title", "abstract"], "meaning-and-interaction", "prosody-and-paralinguistics", "prosodic-meaning"),
    "mallela25_interspeech": ("confirmed-current-boundary", "The abstract detects word prominence from syllable-level acoustic and linguistic context and links prominence to interpreting speaker intent. The evidence supports prosodic meaning, bounded by the labeled data and non-native speech conditions.", ["title", "abstract"], "meaning-and-interaction", "prosody-and-paralinguistics", "prosodic-meaning"),
    "malykh25_interspeech": ("confirmed-current-boundary", "The abstract develops and evaluates speaker-recognition systems combining diarization, embeddings, and adaptive scoring across difficult recording conditions. The evidence supports speaker verification, bounded by NIST SRE24 scenarios and leaderboard evaluation.", ["title", "abstract"], "people-variation-and-health", "identity-and-life-stage", "speaker-verification"),
}

def main():
    payload = json.loads(QUEUE.read_text())
    rows = {r["paper_id"]: r for r in payload["rows"]}
    for pid, (decision, note, sections, theme, subtheme, concept) in DECISIONS.items():
        row = rows[pid]
        if row["taxonomy_review_state"] == "taxonomy-adjudicated":
            raise SystemExit(f"already adjudicated: {pid}")
        row.update({"taxonomy_review_state": "taxonomy-adjudicated", "final_decision": decision, "reviewer_note": note, "reviewed_sections": sections, "final_theme_id": theme, "final_subtheme_id": subtheme, "final_concept_id": concept})
    payload["adjudicated_count"] = sum(r["taxonomy_review_state"] == "taxonomy-adjudicated" for r in rows.values())
    payload["open_count"] = len(rows) - payload["adjudicated_count"]
    payload["decision_counts"] = {d: sum(r.get("final_decision") == d for r in rows.values() if r["taxonomy_review_state"] == "taxonomy-adjudicated") for d in sorted({r.get("final_decision") for r in rows.values() if r["taxonomy_review_state"] == "taxonomy-adjudicated"})}
    QUEUE.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({"batch": len(DECISIONS), "adjudicated": payload["adjudicated_count"], "open": payload["open_count"]}))

if __name__ == "__main__":
    main()
