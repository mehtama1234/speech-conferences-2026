#!/usr/bin/env python3
"""Record the next eight title-only D1 taxonomy adjudications."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "f98a65513f89f2ba1ebf6e1b28274bd339b96d1e": ("confirmed-current-boundary", "The title explicitly concerns predictive cues for dysarthric speech descriptors. Title-only evidence supports atypical articulation and dysarthria, without establishing descriptor reliability or clinical value.", "people-variation-and-health", "atypical-and-assistive-speech", "dysarthria-and-atypical-speech"),
    "f9b9441f4c573b538dced6abc5d338b5f575a271": ("confirmed-current-boundary", "The title explicitly concerns efficient self-supervised speech recognition models. Title-only evidence supports learned speech units, without establishing the pruning tradeoff or recognition quality.", "recognition-and-alignment", "acoustic-unit-learning", "self-supervised-speech-units"),
    "fa541c58c89c154e01ea14f29f5c2259a774f792": ("confirmed-current-boundary", "The title explicitly concerns generative speech enhancement. Title-only evidence supports speech-prior denoising, without establishing enhancement quality or acceleration benefit.", "listening-and-separation", "noise-enhancement", "speech-prior-denoising"),
    "fa75aa083824b68bd7f3fef81f952d81aa59bb54": ("reassigned-to-neighbor", "The title explicitly concerns speech-intelligibility prediction for hearing aids. Title-only evidence places it under listener effort rather than word error versus understanding.", "people-variation-and-health", "human-centered-accessibility", "listener-effort"),
    "fadd84b448ddaa2a37c87dd1c89414301012a31b": ("confirmed-current-boundary", "The title explicitly concerns speech translation and adaptive token mixing. Title-only evidence supports cross-lingual transfer, without establishing translation quality or language coverage.", "languages-accents-and-resources", "crosslingual-structure", "crosslingual-transfer"),
    "faeec59c814a27f42e0869a5dd0781556a62105c": ("confirmed-current-boundary", "The title explicitly concerns audio-text retrieval and temporal grounding. Title-only evidence supports referential grounding, without establishing retrieval or grounding accuracy.", "meaning-and-interaction", "grounding-and-action", "referential-grounding"),
    "fb88cd068e0a2b62372a4fced53c6b4dd86d433f": ("confirmed-current-boundary", "The title explicitly concerns adversarial defense for a speech system using generative enhancement. Title-only evidence supports distribution shift and robustness, without establishing defense effectiveness.", "evaluation-deployment-and-consequence", "robustness-and-shift", "distribution-shift"),
    "fc17c3af8734c19c6e030d992dedc6d87cf5409e": ("confirmed-current-boundary", "The title explicitly concerns audio deepfake detection using acoustic inconsistency analysis. Title-only evidence supports spoofing and deepfake detection, without establishing detection reliability.", "evaluation-deployment-and-consequence", "privacy-and-security", "spoofing-and-deepfake"),
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
