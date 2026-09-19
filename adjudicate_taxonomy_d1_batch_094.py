#!/usr/bin/env python3
"""Record the next eight evidence-bounded taxonomy adjudications."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "fathan25b_interspeech": ("reassigned-to-neighbor", "The title and abstract explicitly improve self-supervised speaker verification by correcting noisy speaker labels. The speech task is speaker verification, not acoustic noise enhancement.", ["title", "abstract"], "people-variation-and-health", "identity-and-life-stage", "speaker-verification"),
    "febrinanto25_interspeech": ("confirmed-current-boundary", "The title and abstract explicitly detect audio deepfakes under continual arrival of new attacks and evaluate forgetting. The evidence supports spoofing and synthetic-voice misuse, without proving future-attack coverage.", ["title", "abstract"], "evaluation-deployment-and-consequence", "privacy-and-security", "spoofing-and-deepfake"),
    "feng25b_interspeech": ("confirmed-current-boundary", "The title and abstract explicitly classify who is speaking in child-adult dyadic speech using egocentric wearable sensing. The evidence supports speaker verification as an identity task, without establishing general wearable performance.", ["title", "abstract"], "people-variation-and-health", "identity-and-life-stage", "speaker-verification"),
    "fernandez25_interspeech": ("confirmed-current-boundary", "The title and abstract explicitly reconstruct online speech waveforms from spectrogram magnitudes and estimated phase. The evidence supports perceptual recovery, without proving preservation of every original signal detail.", ["title", "abstract"], "listening-and-separation", "perceptual-recovery", "perceptual-enhancement"),
    "ferrofilho25_interspeech": ("reassigned-to-neighbor", "The title and abstract explicitly evaluate speaker embeddings under domain, sampling-rate, codec, far-field, and noise changes. The central boundary is distribution shift, not sampling and quantization as a signal operation.", ["title", "abstract"], "evaluation-deployment-and-consequence", "robustness-and-shift", "distribution-shift"),
    "firc25_interspeech": ("confirmed-current-boundary", "The title and abstract explicitly introduce a systematically varied dataset for deepfake speech source tracing and attribution. The evidence supports spoofing and synthetic-voice misuse, without proving forensic reliability.", ["title", "abstract"], "evaluation-deployment-and-consequence", "privacy-and-security", "spoofing-and-deepfake"),
    "fischbach25_interspeech": ("reassigned-to-neighbor", "The title and abstract explicitly use voice conversion to augment low-resource German dialect classification and isolate dialect evidence. This belongs under dialect and variety, not microphone or channel coloration.", ["title", "abstract"], "languages-accents-and-resources", "accent-dialect-and-cultural-meaning", "dialect-and-variety"),
    "fong25_interspeech": ("reassigned-to-neighbor", "The title and abstract explicitly study low-resource ASR adaptation as data volume and high-resource pretraining change. This is few-shot or scarce-data adaptation, not speech data collection itself.", ["title", "abstract"], "languages-accents-and-resources", "low-resource-learning", "few-shot-adaptation"),
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
