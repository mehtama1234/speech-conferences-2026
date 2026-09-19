#!/usr/bin/env python3
"""Record the next eight evidence-bounded taxonomy adjudications."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "santamariajorda25_interspeech": (
        "confirmed-current-boundary",
        "The abstract releases a 235-hour narrow-domain English speech corpus with reliable manual test data, pseudo-labeled training data, and in-domain text for ASR benchmarking. The evidence supports speech-data collection, bounded by LHCP talks, the two test sets, release license, and reported WER.",
        ["title", "abstract"], "languages-accents-and-resources", "data-creation", "speech-data-collection",
    ),
    "sasu25_interspeech": (
        "confirmed-current-boundary",
        "The abstract jointly models pitch accent detection and ASR and reports both improved accent detection and lower WER. The evidence supports prosodic meaning, bounded by the joint model, LibriSpeech fine-tuning, and the reported pitch-accent/ASR results.",
        ["title", "abstract"], "meaning-and-interaction", "prosody-and-paralinguistics", "prosodic-meaning",
    ),
    "sasu25b_interspeech": (
        "confirmed-current-boundary",
        "The abstract uses speech prosody to disambiguate robotic instructions and select task plans, with a dedicated ambiguous-instruction dataset. The evidence supports speech acts, bounded by referent-intent detection, plan selection, and the reported robotics accuracies.",
        ["title", "abstract"], "meaning-and-interaction", "grounding-and-action", "speech-act",
    ),
    "scheck25_interspeech": (
        "confirmed-current-boundary",
        "The abstract converts silent-articulation EMG into selectable-voice speech for voice-prosthesis scenarios and tests speaker-independent targets. The evidence supports augmentative communication, bounded by EMG-VCTK, synthetic/auxiliary training speech, and intelligibility/naturalness results.",
        ["title", "abstract"], "people-variation-and-health", "atypical-and-assistive-speech", "augmentative-communication",
    ),
    "schouwenaars25_interspeech": (
        "confirmed-current-boundary",
        "The abstract measures how cochlear-implant-simulated speech affects grammatical interpretation, gaze, and working-memory-related processing. The evidence supports accessibility fit, bounded by German questions, simulated CI speech, eye tracking, and participant WM groups.",
        ["title", "abstract"], "people-variation-and-health", "human-centered-accessibility", "accessibility-fit",
    ),
    "sedlacek25_interspeech": (
        "confirmed-current-boundary",
        "The abstract aligns speech encoders with language models for spoken dialogue-state tracking and evaluates slot values, history, and post-processing. The evidence supports dialogue state, bounded by SpokenWOZ/Speech-Aware MultiWOZ and the reported JGA results.",
        ["title", "abstract"], "meaning-and-interaction", "intent-and-dialogue-state", "dialogue-state",
    ),
    "seong25_interspeech": (
        "confirmed-current-boundary",
        "The abstract conditions target-speaker ASR on multiple and synthesized speaker embeddings in multi-talker speech and reports WER reductions. The evidence supports target-conditioned separation, bounded by Libri2Mix, target embedding modulation, and virtual-speaker augmentation.",
        ["title", "abstract"], "listening-and-separation", "source-separation", "target-conditioned-separation",
    ),
    "serajian25_interspeech": (
        "reassigned-to-neighbor",
        "The abstract’s main contribution is a balanced, transcribed, parallel Farsi dataset covering phonetic combinations and enabling voice-conversion evaluation. The governing boundary is speech-data collection, not the reported conversion baseline.",
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


if __name__ == "__main__": main()
