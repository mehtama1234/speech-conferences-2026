#!/usr/bin/env python3
"""Record the next eight evidence-bounded taxonomy adjudications."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "gong25c_interspeech": ("confirmed-current-boundary", "The title and abstract explicitly evaluate meeting summaries by comparing key facts, completeness, and dialogue content. The evidence supports dialogue state, without establishing that the evaluation preserves every conversational action.", ["title", "abstract"], "meaning-and-interaction", "intent-and-dialogue-state", "dialogue-state"),
    "gorthi25_interspeech": ("confirmed-current-boundary", "The title and abstract explicitly detect anti-spoofing attacks in speech alongside other biometric modalities. The evidence supports spoofing and synthetic-voice misuse, without proving equal robustness across modalities.", ["title", "abstract"], "evaluation-deployment-and-consequence", "privacy-and-security", "spoofing-and-deepfake"),
    "gourav25_interspeech": ("confirmed-current-boundary", "The title and abstract explicitly generate TTS output from multilingual and code-mixed text without additional training data. The evidence supports text-to-speech planning, without proving naturalness for every language mix.", ["title", "abstract"], "voice-generation-and-control", "content-planning", "text-to-speech-planning"),
    "greenberg25_interspeech": ("confirmed-current-boundary", "The title and abstract explicitly evaluate speaker recognition across audio, visual, and audio-visual tracks with variable enrollment, duration, and multi-person conditions. The evidence supports speaker verification, without proving identity certainty.", ["title", "abstract"], "people-variation-and-health", "identity-and-life-stage", "speaker-verification"),
    "grigoryan25_interspeech": ("reassigned-to-neighbor", "The title and abstract explicitly optimize beam-search decoding for transducer ASR to reduce inference cost and improve speed. The central boundary is latency and resource budget, not self-training.", ["title", "abstract"], "evaluation-deployment-and-consequence", "deployment-cost", "latency-and-resource"),
    "grossman25_interspeech": ("reassigned-to-neighbor", "The title and abstract explicitly introduce a large professionally transcribed multi-speaker financial-speech dataset with speaker metadata. The paper's primary contribution is speech data collection, not blind source separation itself.", ["title", "abstract"], "languages-accents-and-resources", "data-creation", "speech-data-collection"),
    "gu25_interspeech": ("rejected-out-of-scope", "The title and abstract concern pitch manipulation for music production and singer identity, not ordinary human speech or spoken-language evidence. It is outside this speech taxonomy.", ["title", "abstract"], None, None, None),
    "gu25b_interspeech": ("confirmed-current-boundary", "The title and abstract explicitly quantize a large speech model and measure memory, bit rate, and WER tradeoffs for deployment. The evidence supports latency and resource budget, without proving all downstream capabilities are preserved.", ["title", "abstract"], "evaluation-deployment-and-consequence", "deployment-cost", "latency-and-resource"),
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
