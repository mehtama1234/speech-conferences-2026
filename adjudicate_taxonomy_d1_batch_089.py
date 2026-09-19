#!/usr/bin/env python3
"""Record the next eight title-only D1 taxonomy adjudications."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "das25b_interspeech": ("confirmed-current-boundary", "The title explicitly concerns improving intelligibility of dysarthric speech with conditional flow matching. Title-only evidence supports speech-prior denoising, without establishing intelligibility or reconstruction benefit.", "listening-and-separation", "noise-enhancement", "speech-prior-denoising"),
    "dasilva25_interspeech": ("reassigned-to-neighbor", "The title explicitly concerns neuro-guided speaker extraction using speech envelopes and waveforms. Title-only evidence places it under non-airborne sensing rather than target-conditioned separation.", "sound-and-production", "room-channel-and-sensing", "non-airborne-sensing"),
    "degroot25_interspeech": ("confirmed-current-boundary", "The title explicitly concerns objective and subjective evaluation of diffusion speech enhancement for dysarthric speech. Title-only evidence supports speech-prior denoising, without establishing evaluation results.", "listening-and-separation", "noise-enhancement", "speech-prior-denoising"),
    "deluca25_interspeech": ("reassigned-to-neighbor", "The title explicitly concerns exploration of voice data in an interactive dashboard. Title-only evidence places it under speech data collection rather than microphone and channel coloration.", "languages-accents-and-resources", "data-creation", "speech-data-collection"),
    "deng25_interspeech": ("reassigned-to-neighbor", "The title explicitly concerns prompt-expert speaker adaptation for elderly speech recognition. Title-only evidence places it under speaker adaptation rather than target-conditioned source separation.", "recognition-and-alignment", "context-and-open-vocabulary", "speaker-adaptation"),
    "deng25b_interspeech": ("confirmed-current-boundary", "The title explicitly concerns depression detection from acoustic features in long speech. Title-only evidence supports clinical speech marker membership, without establishing clinical validity.", "people-variation-and-health", "clinical-markers", "clinical-speech-marker"),
    "deoliveira25_interspeech": ("confirmed-current-boundary", "The title explicitly concerns non-intrusive speech-quality assessment. Title-only evidence supports quality and naturalness, without establishing assessment validity.", "evaluation-deployment-and-consequence", "metric-and-human-targets", "quality-and-naturalness"),
    "dewhurst25_interspeech": ("confirmed-current-boundary", "The title explicitly concerns open-source hardware for acoustic nasalance measurement. Title-only evidence supports speech data collection, without establishing measurement accuracy or clinical usefulness.", "languages-accents-and-resources", "data-creation", "speech-data-collection"),
}

def main():
    payload = json.loads(QUEUE.read_text())
    rows = {r["paper_id"]: r for r in payload["rows"]}
    for pid, (decision, note, theme, subtheme, concept) in DECISIONS.items():
        row = rows[pid]
        if row["taxonomy_review_state"] == "taxonomy-adjudicated":
            raise SystemExit(f"already adjudicated: {pid}")
        row.update({"taxonomy_review_state": "taxonomy-adjudicated", "final_decision": decision, "reviewer_note": note, "reviewed_sections": ["title"], "final_theme_id": theme, "final_subtheme_id": subtheme, "final_concept_id": concept})
    payload["adjudicated_count"] = sum(r["taxonomy_review_state"] == "taxonomy-adjudicated" for r in rows.values())
    payload["open_count"] = len(rows) - payload["adjudicated_count"]
    payload["decision_counts"] = {d: sum(r.get("final_decision") == d for r in rows.values() if r["taxonomy_review_state"] == "taxonomy-adjudicated") for d in sorted({r.get("final_decision") for r in rows.values() if r["taxonomy_review_state"] == "taxonomy-adjudicated"})}
    QUEUE.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({"batch": len(DECISIONS), "adjudicated": payload["adjudicated_count"], "open": payload["open_count"]}))

if __name__ == "__main__":
    main()
