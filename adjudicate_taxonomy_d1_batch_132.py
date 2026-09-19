#!/usr/bin/env python3
"""Record the next eight evidence-bounded taxonomy adjudications."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "liu25d_interspeech": ("confirmed-current-boundary", "The abstract reconstructs missing high-frequency speech components and evaluates subjective and objective quality while reducing computation. The evidence supports perceptual enhancement, bounded by the bandwidth-extension and real-time communication tests.", ["title", "abstract"], "listening-and-separation", "perceptual-recovery", "perceptual-enhancement"),
    "liu25e_interspeech": ("confirmed-current-boundary", "The abstract creates a generated Mandarin-Cantonese parallel speech database with retrieval-based text generation, TTS, and quality filtering. The evidence supports speech-data collection, bounded by the synthetic corpus and its fine-tuning evaluation.", ["title", "abstract"], "languages-accents-and-resources", "data-creation", "speech-data-collection"),
    "liu25f_interspeech": ("confirmed-current-boundary", "The abstract detects stuttering and addresses conflicting detection tasks with rule-based and mixture-of-experts multi-task learning. The evidence supports atypical articulation and dysarthria as the broader atypical-speech boundary, without equating stuttering with dysarthria.", ["title", "abstract"], "people-variation-and-health", "atypical-and-assistive-speech", "dysarthria-and-atypical-speech"),
    "liu25g_interspeech": ("reassigned-to-neighbor", "The abstract evaluates continuous visual speech recognition from lip and face information and expands its visual-speech data. The alternate visual sensing path is the governing boundary, not acoustic-to-token mapping alone.", ["title", "abstract"], "sound-and-production", "room-channel-and-sensing", "non-airborne-sensing"),
    "liu25j_interspeech": ("confirmed-current-boundary", "The abstract converts speech timbre while preserving semantically relevant background sound and evaluates both objectives and listener judgments. The evidence supports voice conversion, bounded by background-preservation conditions.", ["title", "abstract"], "voice-generation-and-control", "identity-and-conversion", "voice-conversion"),
    "liu25k_interspeech": ("confirmed-current-boundary", "The abstract analyzes spontaneous speech for dementia and cognitive-score prediction, including pause and disfluency information. The evidence supports a clinical speech marker, without establishing diagnosis beyond the PROCESS challenge data.", ["title", "abstract"], "people-variation-and-health", "clinical-markers", "clinical-speech-marker"),
    "liu25l_interspeech": ("confirmed-current-boundary", "The abstract tests Alzheimer detection using ASR transcripts and examines whether recognition errors carry useful disease-related cues. The evidence supports a clinical speech marker, bounded by ADReSS and the evaluated ASR systems.", ["title", "abstract"], "people-variation-and-health", "clinical-markers", "clinical-speech-marker"),
    "liu25m_interspeech": ("confirmed-current-boundary", "The abstract predicts dimensional emotional attributes from multiple pretrained speech representations and evaluates the method in a naturalistic challenge. The evidence supports paralinguistic state, bounded by the official test set and reported challenge metric.", ["title", "abstract"], "meaning-and-interaction", "prosody-and-paralinguistics", "paralinguistic-state"),
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
