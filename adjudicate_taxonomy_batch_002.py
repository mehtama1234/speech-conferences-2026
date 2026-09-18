#!/usr/bin/env python3
"""Record the second small, full-paper taxonomy adjudication batch."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "ahn25_interspeech": ("confirmed-current-boundary", "HuBERT-VIC changes noisy speech representations before recognition; the captured method and ablations support learned acoustic units, while the paper does not establish human-like units or real-world noise coverage.", "recognition-and-alignment", "acoustic-unit-learning", "self-supervised-speech-units"),
    "ai25_interspeech": ("reassigned-to-neighbor", "The paper measures how the same person's verification evidence changes with age and time gap. Aging is the object of study, not a system that converts one voice into another.", "people-variation-and-health", "identity-and-life-stage", "age-and-development"),
    "akinrintoyo25_interspeech": ("confirmed-current-boundary", "The explicit filler-word target makes preservation of disfluencies part of the transcription object; the dementia speech setting limits the claim but does not change the mechanism.", "recognition-and-alignment", "boundaries-and-alignment", "disfluency-preservation"),
    "akti25_interspeech": ("confirmed-current-boundary", "The method separates linguistic content from speaker and expressive controls to synthesize a changed voice; this is directly a voice-conversion problem, with intelligibility and cross-lingual limits reported.", "voice-generation-and-control", "identity-and-conversion", "voice-conversion"),
    "alabi25_interspeech": ("reassigned-to-neighbor", "The central contribution is a multilingual self-supervised representation spanning African languages and testing transfer across them. Scarce labels motivate the work, but pseudo-label self-training is not the paper's main boundary.", "languages-accents-and-resources", "crosslingual-structure", "crosslingual-transfer"),
    "alcalapadilla25_interspeech": ("confirmed-current-boundary", "Direction of arrival conditions the learned filter for a hearing-aid array, so spatial evidence is the decisive mechanism; the reported scenario does not establish general clinical benefit.", "listening-and-separation", "spatial-listening", "spatial-filtering"),
    "alderete25_interspeech": ("confirmed-current-boundary", "Annotated spontaneous speech errors create a measured shift for ASR evaluation, and the paper compares error type and position; the result remains bounded by the database, language, and WhisperX setup.", "evaluation-deployment-and-consequence", "robustness-and-shift", "distribution-shift"),
    "alip25_interspeech": ("confirmed-current-boundary", "Although the input is multi-channel, the three-stage method estimates masks and refines the spectrum to enhance speech. Spatial structure is an input to enhancement, not the paper's primary target-selection question.", "listening-and-separation", "noise-enhancement", "spectral-mask"),
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
