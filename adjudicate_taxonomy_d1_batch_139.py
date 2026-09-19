#!/usr/bin/env python3
"""Record the next eight evidence-bounded taxonomy adjudications."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "martinek25_interspeech": ("reassigned-to-neighbor", "The abstract directly evaluates speaker-verification systems under read-versus-spontaneous speech and synthetic impostor conditions. The governing object is identity verification, not merely within-speaker state variation.", ["title", "abstract"], "people-variation-and-health", "identity-and-life-stage", "speaker-verification"),
    "marx25_interspeech": ("confirmed-current-boundary", "The abstract detects speech sound disorders in German-speaking children and tests whether typical and pathological speech augmentation improves recognition and disorder classification. The evidence supports atypical articulation and dysarthria as the broader atypical-speech boundary.", ["title", "abstract"], "people-variation-and-health", "atypical-and-assistive-speech", "dysarthria-and-atypical-speech"),
    "masson25_interspeech": ("confirmed-current-boundary", "The abstract uses ASR transcription errors to identify pronunciation profiles associated with head-and-neck cancer and Parkinson's speech disorders and tests synthesized variants. The evidence supports atypical articulation and dysarthria, bounded by the disorders, ASR systems, and synthesized profiles.", ["title", "abstract"], "people-variation-and-health", "atypical-and-assistive-speech", "dysarthria-and-atypical-speech"),
    "masztalski25_interspeech": ("confirmed-current-boundary", "The abstract develops hard-negative sampling for supervised contrastive speaker verification and evaluates verification error on VoxCeleb. The evidence supports speaker verification, bounded by the clustering strategy and benchmark.", ["title", "abstract"], "people-variation-and-health", "identity-and-life-stage", "speaker-verification"),
    "mayer25_interspeech": ("reassigned-to-neighbor", "The abstract models variable pitch, energy, and duration in expressive TTS and evaluates stochastic control of prosody. The governing operation is prosody control, rather than style or emotion labels alone.", ["title", "abstract"], "voice-generation-and-control", "expression-and-interactive-control", "prosody-control"),
    "mcallister25_interspeech": ("reassigned-to-neighbor", "The abstract develops and usability-tests real-time resonance biofeedback for gender-affirming voice training. The central consequence is whether the tool fits users' access and training needs, rather than consent or data control.", ["title", "abstract"], "people-variation-and-health", "human-centered-accessibility", "accessibility-fit"),
    "mcallister25b_interspeech": ("confirmed-current-boundary", "The abstract presents a visual-acoustic biofeedback application for children with speech sound disorder and describes its adjustable target and delivery platforms. The evidence supports accessibility fit, bounded by the current /r/ exercises and stated adaptation potential.", ["title", "abstract"], "people-variation-and-health", "human-centered-accessibility", "accessibility-fit"),
    "mcgahay25_interspeech": ("reassigned-to-neighbor", "The abstract models how vowel categories and sound-change pressures emerge from listener-speaker confusion and predicts typological variation. The closest speech boundary is pronunciation variation, not articulatory coordination of physical gestures.", ["title", "abstract"], "recognition-and-alignment", "pronunciation-and-variation", "pronunciation-variation"),
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
