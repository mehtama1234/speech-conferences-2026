#!/usr/bin/env python3
"""Record the tenth small, full-paper taxonomy adjudication batch."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "du25b_interspeech": ("reassigned-to-neighbor", "EAA predicts and conditions on affective information from audio and context. Its object is a nonliteral speaker state, not the listener's effort to understand a signal.", "meaning-and-interaction", "prosody-and-paralinguistics", "paralinguistic-state"),
    "ducorroy25_interspeech": ("confirmed-current-boundary", "Model merging adapts Whisper to dysarthric speech, using development evidence to select useful checkpoint combinations in low-data settings. The central move is speaker and atypical-speech adaptation, not a new acoustic unit.", "recognition-and-alignment", "context-and-open-vocabulary", "speaker-adaptation"),
    "elkheir25b_interspeech": ("reassigned-to-neighbor", "The benchmark labels deviations from Qur'anic pronunciation targets and evaluates learner-error assessment. The central boundary is which legitimate or erroneous pronunciation path the recognizer accepts, not generic acoustic-to-token mapping.", "recognition-and-alignment", "pronunciation-and-variation", "pronunciation-variation"),
    "elmers25_interspeech": ("confirmed-current-boundary", "Triadic voice-activity projection predicts future speaking states and next-speaker behavior, with controlled and spontaneous discussion conditions compared. This is directly turn-boundary prediction.", "meaning-and-interaction", "turn-taking-and-repair", "turn-boundary"),
    "fang25c_interspeech": ("rejected-out-of-scope", "The captured paper studies general text-to-audio retrieval and multiscale audio tokenization; it does not establish a speech or spoken-language object for this speech taxonomy.", None, None, None),
    "fathan25_interspeech": ("confirmed-current-boundary", "The paper tests whether optimizer and sharpness choices improve speaker-verification generalization. The object is identity evidence across recordings, while the tested corpora and optimizers bound the claim.", "people-variation-and-health", "identity-and-life-stage", "speaker-verification"),
    "feng25_interspeech": ("confirmed-current-boundary", "The challenge system predicts primary and secondary emotion and improves minority-class scores through annotation dropout and audio mixing. Emotion labels are task-specific, but the central object is paralinguistic state.", "meaning-and-interaction", "prosody-and-paralinguistics", "paralinguistic-state"),
    "fort25_interspeech": ("confirmed-current-boundary", "The study adapts recognition and phoneme-error detection to isiZulu learner speech with limited labeled resources. Corpus and tone omissions bound the result, but few-shot/low-resource adaptation is the central pressure.", "languages-accents-and-resources", "low-resource-learning", "few-shot-adaptation"),
}

def main():
    payload = json.loads(QUEUE.read_text())
    rows = {r["paper_id"]: r for r in payload["rows"]}
    for pid, (decision, note, theme, subtheme, concept) in DECISIONS.items():
        row = rows[pid]
        if row["taxonomy_review_state"] == "taxonomy-adjudicated":
            raise SystemExit(f"already adjudicated: {pid}")
        row.update({"taxonomy_review_state": "taxonomy-adjudicated", "final_decision": decision, "reviewer_note": note, "reviewed_sections": ["title", "abstract", "method", "experiments", "results", "limits"], "final_theme_id": theme, "final_subtheme_id": subtheme, "final_concept_id": concept})
    payload["adjudicated_count"] = sum(r["taxonomy_review_state"] == "taxonomy-adjudicated" for r in rows.values())
    payload["open_count"] = len(rows) - payload["adjudicated_count"]
    payload["decision_counts"] = {d: sum(r.get("final_decision") == d for r in rows.values() if r["taxonomy_review_state"] == "taxonomy-adjudicated") for d in sorted({r.get("final_decision") for r in rows.values() if r["taxonomy_review_state"] == "taxonomy-adjudicated"})}
    QUEUE.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({"batch": len(DECISIONS), "adjudicated": payload["adjudicated_count"], "open": payload["open_count"]}))

if __name__ == "__main__":
    main()
