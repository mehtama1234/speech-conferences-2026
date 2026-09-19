#!/usr/bin/env python3
"""Record the eleventh small, full-paper taxonomy adjudication batch."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "franz25_interspeech": ("confirmed-current-boundary", "Room impulse responses and microphone placement change objective clinical voice measures before interpretation. The study directly addresses reverberant mixture and channel dependence, bounded by its rooms and devices.", "sound-and-production", "room-channel-and-sensing", "reverberant-mixture"),
    "freisinger25_interspeech": ("confirmed-current-boundary", "The work segments long spoken transcripts into nested topical sections and measures boundary quality. It concerns sequence boundaries in recognized speech, not proof of human topic understanding.", "recognition-and-alignment", "boundaries-and-alignment", "alignment"),
    "fujita25_interspeech": ("confirmed-current-boundary", "The zero-shot TTS system turns listener-described qualities such as bright or warm into controllable impression vectors. This is expressive control, bounded by selected dimensions, speakers, and ratings.", "voice-generation-and-control", "expression-and-interactive-control", "style-and-emotion-control"),
    "fujita25b_interspeech": ("rejected-out-of-scope", "The captured paper evaluates general audio question answering and captioning on AudioCaps, WavCaps, and Clotho; it does not establish a speech or spoken-language object for this speech taxonomy.", None, None, None),
    "gao25b_interspeech": ("confirmed-current-boundary", "ADCeleb uses longitudinal public recordings and acoustic/linguistic representations to study signals near Alzheimer diagnosis. It is a clinical speech-marker dataset and baseline, not diagnostic validation.", "people-variation-and-health", "clinical-markers", "clinical-speech-marker"),
    "gao25c_interspeech": ("confirmed-current-boundary", "Prompt information helps interpret variable child speech against intended linguistic content and reading errors. The central issue is permitted pronunciation variation, bounded by age, prompts, and labels.", "recognition-and-alignment", "pronunciation-and-variation", "pronunciation-variation"),
    "gao25f_interspeech": ("confirmed-current-boundary", "The paper evaluates multilingual accent robustness by subgroup rather than treating one pronunciation norm as universal. Accent labels, languages, and denominators bound the comparison.", "languages-accents-and-resources", "accent-dialect-and-cultural-meaning", "accent-robustness"),
    "giraldo25_interspeech": ("reassigned-to-neighbor", "The paper asks whether enhancement rankings survive demographic and language changes and warns that benchmark performance transfers poorly. It diagnoses distribution shift; it does not measure listener concentration, repetition, or repair directly.", "evaluation-deployment-and-consequence", "robustness-and-shift", "distribution-shift"),
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
