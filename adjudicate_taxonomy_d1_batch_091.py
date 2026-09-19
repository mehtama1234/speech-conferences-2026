#!/usr/bin/env python3
"""Record the next eight evidence-bounded taxonomy adjudications."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "draxler25_interspeech": ("confirmed-current-boundary", "The title and abstract explicitly describe a multilingual oral-history transcription portal whose workflow collects speech, runs recognition, and supports manual correction. The evidence supports speech data collection; it does not establish universal transcription quality.", ["title", "abstract"], "languages-accents-and-resources", "data-creation", "speech-data-collection"),
    "du25c_interspeech": ("reassigned-to-neighbor", "The title and abstract explicitly diagnose adductor spasmodic and muscle-tension dysphonia from patient speech. The speech signal is being used as a clinical marker, not studied primarily as a periodic source.", ["title", "abstract"], "people-variation-and-health", "clinical-markers", "clinical-speech-marker"),
    "ducceschi25_interspeech": ("confirmed-current-boundary", "The title and abstract explicitly transcribe South Tyrolean dialect into Standard German and discuss dialectal variation and low-resource data. The evidence supports dialect and variety; it does not establish transfer to all dialects.", ["title", "abstract"], "languages-accents-and-resources", "accent-dialect-and-cultural-meaning", "dialect-and-variety"),
    "dumpala25_interspeech": ("confirmed-current-boundary", "The title and abstract explicitly detect depression from speech and test robustness under recording and demographic shifts. The evidence supports a clinical speech marker, without establishing diagnosis or clinical validity.", ["title", "abstract"], "people-variation-and-health", "clinical-markers", "clinical-speech-marker"),
    "duraisamy25_interspeech": ("rejected-out-of-scope", "The title and abstract concern EEG classification of imagined or covert speech rather than an acoustic spoken-language signal. It is outside this speech-signal taxonomy.", ["title", "abstract"], None, None, None),
    "durmus25_interspeech": ("confirmed-current-boundary", "The title and abstract explicitly provide a reproducible benchmark with defined datasets, splits, metrics, and efficiency analysis for speaker diarization. The evidence supports calibration and selective use, without proving deployment reliability everywhere.", ["title", "abstract"], "evaluation-deployment-and-consequence", "metric-and-human-targets", "calibration-and-selective-use"),
    "dutta25_interspeech": ("confirmed-current-boundary", "The title and abstract explicitly address emotion recognition in naturalistic speech with variable context, speakers, recording conditions, and class balance. The evidence supports paralinguistic state, without making emotion recognition universal.", ["title", "abstract"], "meaning-and-interaction", "prosody-and-paralinguistics", "paralinguistic-state"),
    "dutta25b_interspeech": ("confirmed-current-boundary", "The title and abstract explicitly test zero-shot spoofing detection and quantify bias and precision effects under quantization. The evidence supports spoofing and synthetic-voice misuse, without establishing safe deployment.", ["title", "abstract"], "evaluation-deployment-and-consequence", "privacy-and-security", "spoofing-and-deepfake"),
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
