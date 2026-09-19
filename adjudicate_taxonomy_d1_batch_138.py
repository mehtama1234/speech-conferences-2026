#!/usr/bin/env python3
"""Record the next eight evidence-bounded taxonomy adjudications."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "manakul25_interspeech": ("confirmed-current-boundary", "The abstract evaluates audio language models on Thai and English and studies how data mixtures affect low-resource instruction following and speech understanding. The evidence supports cross-lingual transfer, bounded by Thai, English, and the tested model adaptations.", ["title", "abstract"], "languages-accents-and-resources", "crosslingual-structure", "crosslingual-transfer"),
    "mansi25_interspeech": ("confirmed-current-boundary", "The abstract uses dementia-related speech, generated images, and alignment explanations to test a disease-detection signal. The evidence supports a clinical speech marker, bounded by ADReSS and the unusual image-mediated representation.", ["title", "abstract"], "people-variation-and-health", "clinical-markers", "clinical-speech-marker"),
    "maran25_interspeech": ("reassigned-to-neighbor", "The abstract tests whether timed avatar gestures alter listeners' perception of word stress in speech. The governing boundary is prosodic meaning and multimodal interpretation, not interactional feedback from a user response.", ["title", "abstract"], "meaning-and-interaction", "prosody-and-paralinguistics", "prosodic-meaning"),
    "marchini25_interspeech": ("confirmed-current-boundary", "The abstract models pitch contours and focus-related prosody across two Mexican Spanish ethnolects and emphasizes phonetic variation. The evidence supports prosodic meaning, bounded by the dialects, focus conditions, and modeling choices.", ["title", "abstract"], "meaning-and-interaction", "prosody-and-paralinguistics", "prosodic-meaning"),
    "marcinek25_interspeech": ("confirmed-current-boundary", "The abstract varies vocal effort and environmental noise in synthesized speech and measures intelligibility through recognition error. The evidence supports intelligibility and naturalness tradeoffs, bounded by the simulated conditions and ASR-based measure.", ["title", "abstract"], "voice-generation-and-control", "waveform-and-codec-generation", "intelligibility-naturalness"),
    "markitantov25_interspeech": ("confirmed-current-boundary", "The abstract recognizes emotion and sentiment from audio, video, and text with a multimodal multi-task model and evaluates several corpora. The evidence supports paralinguistic state, bounded by the affective labels and datasets.", ["title", "abstract"], "meaning-and-interaction", "prosody-and-paralinguistics", "paralinguistic-state"),
    "marmor25_interspeech": ("confirmed-current-boundary", "The abstract creates a crowdsourced Hebrew speech corpus and evaluation set and trains an open ASR model for a resource-limited language. The evidence supports speech-data collection, bounded by Hebrew, the crowdsourcing process, and released evaluation data.", ["title", "abstract"], "languages-accents-and-resources", "data-creation", "speech-data-collection"),
    "martin25_interspeech": ("confirmed-current-boundary", "The abstract analyzes acoustic characteristics in reading and spontaneous speech for suicide-risk detection and compares network methods with a baseline. The evidence supports a clinical speech marker, bounded by the SpeechWellness challenge and its speech tasks.", ["title", "abstract"], "people-variation-and-health", "clinical-markers", "clinical-speech-marker"),
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
