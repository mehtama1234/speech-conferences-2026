#!/usr/bin/env python3
"""Record the next eight evidence-bounded taxonomy adjudications."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "kothare25_interspeech": ("confirmed-current-boundary", "The abstract extracts multimodal measures from standard speaking exercises and models individual ALS progression. The evidence supports a clinical speech marker, while the cohort and disease-specific assessment limit clinical generalization.", ["title", "abstract"], "people-variation-and-health", "clinical-markers", "clinical-speech-marker"),
    "koudounas25_interspeech": ("confirmed-current-boundary", "The title and abstract explicitly evaluate spoken-language-understanding tasks from speech and compare how models attend to waveform regions. The evidence supports intent in context, bounded by the five datasets and tested architectures.", ["title", "abstract"], "meaning-and-interaction", "intent-and-dialogue-state", "intent-in-context"),
    "koudounas25b_interspeech": ("confirmed-current-boundary", "The abstract detects voice pathology from sustained vowels and read sentences across three languages and recording sources. The evidence supports a clinical speech marker, without establishing diagnosis outside the evaluated sources.", ["title", "abstract"], "people-variation-and-health", "clinical-markers", "clinical-speech-marker"),
    "koudounas25c_interspeech": ("confirmed-current-boundary", "The abstract benchmarks removing speaker-specific information from spoken-language-understanding models in response to right-to-be-forgotten requests. The evidence supports voice privacy, bounded by the four datasets and unlearning measures.", ["title", "abstract"], "evaluation-deployment-and-consequence", "privacy-and-security", "voice-privacy"),
    "koutsianos25_interspeech": ("confirmed-current-boundary", "The abstract traces which generative system produced manipulated speech and evaluates synthetic-speech source tracing. The evidence supports spoofing and synthetic-voice misuse, without proving attribution for every unseen generator.", ["title", "abstract"], "evaluation-deployment-and-consequence", "privacy-and-security", "spoofing-and-deepfake"),
    "kponou25_interspeech": ("reassigned-to-neighbor", "The abstract's main contribution is an expanded transcribed Fongbe-to-French speech corpus and its resource/benchmark construction; the translation models use that resource. The closer boundary is speech-data collection rather than transfer alone.", ["title", "abstract"], "languages-accents-and-resources", "data-creation", "speech-data-collection"),
    "krzywdziak25_interspeech": ("confirmed-current-boundary", "The abstract tests audio, linguistic, and combined speech features for suicide-risk classification and explicitly treats speech as a mental-health indicator. The evidence supports a clinical speech marker, without establishing clinical diagnosis or safety.", ["title", "abstract"], "people-variation-and-health", "clinical-markers", "clinical-speech-marker"),
    "kuan25_interspeech": ("confirmed-current-boundary", "The abstract trains an audio-aware model to distinguish sound events supported by the input from plausible but absent events. The evidence supports referential grounding of audio claims, bounded by the synthesized negatives and tested benchmarks.", ["title", "abstract"], "meaning-and-interaction", "grounding-and-action", "referential-grounding"),
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
