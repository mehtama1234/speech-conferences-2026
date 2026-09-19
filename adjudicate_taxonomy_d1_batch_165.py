#!/usr/bin/env python3
"""Record the next eight evidence-bounded taxonomy adjudications."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "serbest25_interspeech": (
        "confirmed-current-boundary",
        "The abstract combines predictive and generative speech enhancement in a low-latency stochastic-regeneration system and measures perceptual quality. The evidence supports speech-prior denoising, bounded by 3.58M parameters, streaming latency, NISQA-MOS, and URGENT participation.",
        ["title", "abstract"], "listening-and-separation", "noise-enhancement", "speech-prior-denoising",
    ),
    "serditova25_interspeech": (
        "confirmed-current-boundary",
        "The abstract analyzes phonological, lexical, and morphosyntactic ASR errors in Newcastle English and ties them to regional dialect features. The evidence supports accent robustness, bounded by 160 speakers, the two pronouns, and the manual/case-study analyses.",
        ["title", "abstract"], "languages-accents-and-resources", "accent-dialect-and-cultural-meaning", "accent-robustness",
    ),
    "serrand25_interspeech": (
        "confirmed-current-boundary",
        "The abstract releases more than 1,000 hours of spontaneous Québec French speech with normalized, aligned transcripts for ASR training and evaluation. The evidence supports speech-data collection, bounded by the public-inquiry recordings, alignment/filtering process, and ASR results.",
        ["title", "abstract"], "languages-accents-and-resources", "data-creation", "speech-data-collection",
    ),
    "serre25_interspeech": (
        "confirmed-current-boundary",
        "The abstract extracts multiple enrolled target speakers from mixtures using multiple speaker embeddings and evaluates meeting-type speech. The evidence supports target-conditioned separation, bounded by MTSE, curriculum learning, and the multi-target/single-target experiments.",
        ["title", "abstract"], "listening-and-separation", "source-separation", "target-conditioned-separation",
    ),
    "setoguchi25_interspeech": (
        "confirmed-current-boundary",
        "The abstract synthesizes speech-laugh and controls the onset of laughter while testing naturalness, laughter-likeness, and intelligibility. The evidence supports style and emotion control, bounded by the speech-laugh training conditions and listening/dictation tests.",
        ["title", "abstract"], "voice-generation-and-control", "expression-and-interactive-control", "style-and-emotion-control",
    ),
    "shabtay25_interspeech": (
        "confirmed-current-boundary",
        "The abstract answers spoken questions about images by fusing speech, text, and visual inputs and creates the missing tri-modal data with TTS. The evidence supports referential grounding, bounded by spoken VQA, synthesized speech, and the textual upper-bound comparison.",
        ["title", "abstract"], "meaning-and-interaction", "grounding-and-action", "referential-grounding",
    ),
    "shah25_interspeech": (
        "confirmed-current-boundary",
        "The abstract converts non-audible murmurs into speech for silent communication using multi-speaker, synthetic, and multitask training. The evidence supports augmentative communication, bounded by the two public datasets, alignment-free autoregression, and zero-shot/WER results.",
        ["title", "abstract"], "people-variation-and-health", "atypical-and-assistive-speech", "augmentative-communication",
    ),
    "shahidi25_interspeech": (
        "reassigned-to-neighbor",
        "The abstract uses cloned voices as controlled stimuli for audiological speech-perception assessment and measures intelligibility, quality, and speaker discrimination with listeners. The governing boundary is accessibility fit, not a clinical speech marker, bounded by the UK test, 73-person online study, and psychometric functions.",
        ["title", "abstract"], "people-variation-and-health", "human-centered-accessibility", "accessibility-fit",
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


if __name__ == "__main__": main()
