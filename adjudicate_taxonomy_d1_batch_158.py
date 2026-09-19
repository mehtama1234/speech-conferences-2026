#!/usr/bin/env python3
"""Record the next eight evidence-bounded taxonomy adjudications."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "qi25_interspeech": (
        "confirmed-current-boundary",
        "The abstract converts voices with natural-language control over emotion, intensity, mixed emotions, prosody, and speaker identity. The evidence supports style and emotion control, bounded by PromptEVC, its prompt/reference inputs, and stated conversion evaluations.",
        ["title", "abstract"], "voice-generation-and-control", "expression-and-interactive-control", "style-and-emotion-control",
    ),
    "qian25_interspeech": (
        "reassigned-to-neighbor",
        "The abstract expands spoken grammatical-error-correction training from 77 to about 2,500 hours using pseudo-labels, then studies prompts and model size. The governing boundary is self-training and pseudo-label expansion, not alignment alone.",
        ["title", "abstract"], "languages-accents-and-resources", "low-resource-learning", "self-training-and-pseudo-labels",
    ),
    "qian25b_interspeech": (
        "confirmed-current-boundary",
        "The abstract measures perceived prosodic similarity of lexical feedback forms and compares representations with human judgments. The evidence supports prosodic meaning, bounded by the triadic comparison, feedback datasets, and representation analysis.",
        ["title", "abstract"], "meaning-and-interaction", "prosody-and-paralinguistics", "prosodic-meaning",
    ),
    "qin25_interspeech": (
        "confirmed-current-boundary",
        "The abstract enhances reverberant speech with dual-path multi-channel prediction and beamforming while preserving target directions. The evidence supports speech-prior denoising, bounded by microphone-array enhancement and high-reverberation evaluations.",
        ["title", "abstract"], "listening-and-separation", "noise-enhancement", "speech-prior-denoising",
    ),
    "que25_interspeech": (
        "confirmed-current-boundary",
        "The abstract uses visual context alongside text to predict varied TTS prosody and reports more expressive synthesis. The evidence supports prosody control, bounded by VisualSpeech and its visual/text prosody modeling comparison.",
        ["title", "abstract"], "voice-generation-and-control", "expression-and-interactive-control", "prosody-control",
    ),
    "quinterovillalobos25_interspeech": (
        "confirmed-current-boundary",
        "The abstract detects utterances lost during network failures and supplies targeted keyword prompts for repetition after reconnection. The evidence supports packet-loss concealment, bounded by dual ASR discrepancy detection, simulated degradation, and keyword recovery.",
        ["title", "abstract"], "listening-and-separation", "echo-reconstruction", "packet-loss-concealment",
    ),
    "r25_interspeech": (
        "confirmed-current-boundary",
        "The abstract detects multilingual query audio by mapping ten Indian languages to a shared transliterated representation for open-vocabulary keyword spotting. The evidence supports open-vocabulary recognition, bounded by transliterated logits, Kathbath, and IndicSUPERB evaluation.",
        ["title", "abstract"], "recognition-and-alignment", "context-and-open-vocabulary", "open-vocabulary-recognition",
    ),
    "rachman25_interspeech": (
        "reassigned-to-neighbor",
        "The abstract measures how adult age changes sensitivity to F0/VTL cues and vocal emotion recognition, connecting sensory and higher-level effects. The governing boundary is age and development, not paralinguistic state alone.",
        ["title", "abstract"], "people-variation-and-health", "identity-and-life-stage", "age-and-development",
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
