#!/usr/bin/env python3
"""Record the next eight evidence-bounded taxonomy adjudications."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "lewis25_interspeech": ("confirmed-current-boundary", "The abstract relates longitudinal speech and cognitive-task measures to depression symptom severity within clinically diagnosed patients. The evidence supports a clinical speech marker, bounded by the observational cohort and associations rather than a diagnostic causal claim.", ["title", "abstract"], "people-variation-and-health", "clinical-markers", "clinical-speech-marker"),
    "leygue25_interspeech": ("confirmed-current-boundary", "The abstract localizes emotion-relevant frames in speech and evaluates the method on a naturalistic emotion-recognition challenge. The evidence supports paralinguistic state, bounded by the challenge data and attention-based interpretation.", ["title", "abstract"], "meaning-and-interaction", "prosody-and-paralinguistics", "paralinguistic-state"),
    "li25_interspeech": ("confirmed-current-boundary", "The abstract compresses Conformer ASR weights to one and two bits and evaluates memory savings and recognition loss under resource constraints. The evidence supports latency and resource budget, bounded by the Switchboard and LibriSpeech experiments.", ["title", "abstract"], "evaluation-deployment-and-consequence", "deployment-cost", "latency-and-resource"),
    "li25aa_interspeech": ("reassigned-to-neighbor", "The abstract demonstrates an imperceptible backdoor attack against speech classification through latent rearrangement. It is a speech-system security threat, closer to resisting spoofing and misuse than ordinary speech classification or robustness, though the tested attack is not a generated-voice detector.", ["title", "abstract"], "evaluation-deployment-and-consequence", "privacy-and-security", "spoofing-and-deepfake"),
    "li25b_interspeech": ("confirmed-current-boundary", "The abstract uses long-term and local context to keep paragraph-level TTS prosody, style, and timbre coherent across sentences. The evidence supports text-to-speech planning, bounded by the long-text and paragraph-level experiments.", ["title", "abstract"], "voice-generation-and-control", "content-planning", "text-to-speech-planning"),
    "li25ba_interspeech": ("reassigned-to-neighbor", "The abstract creates and validates a sarcastic-speech dataset, where tone and context change the intended meaning. The governing boundary is prosodic and pragmatic meaning, rather than a generic paralinguistic state label.", ["title", "abstract"], "meaning-and-interaction", "prosody-and-paralinguistics", "prosodic-meaning"),
    "li25c_interspeech": ("reassigned-to-neighbor", "The abstract detects voice activity and overlapping-speech intervals and explicitly addresses transient and boundary errors. The central object is locating speech events in time, not extracting a target source from a mixture.", ["title", "abstract"], "recognition-and-alignment", "boundaries-and-alignment", "alignment"),
    "li25ca_interspeech": ("confirmed-current-boundary", "The abstract tests in-context learning for ASR in unseen endangered languages and evaluates how relevant text examples affect performance. The evidence supports few-shot adaptation, bounded by the four languages and prompt conditions.", ["title", "abstract"], "languages-accents-and-resources", "low-resource-learning", "few-shot-adaptation"),
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
