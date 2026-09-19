#!/usr/bin/env python3
"""Record the next eight title-only D1 taxonomy adjudications."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "fce03ed9e56cba18f08a9d155b826dcd6ab37963": ("confirmed-current-boundary", "The title explicitly concerns correlation ceilings for subjective evaluation datasets. Title-only evidence supports quality and naturalness, without establishing the ceiling estimate or dataset validity.", "evaluation-deployment-and-consequence", "metric-and-human-targets", "quality-and-naturalness"),
    "fdc47da159b6fc57b213faabd437e1cf3ba456b7": ("confirmed-current-boundary", "The title explicitly concerns speech-enhancement adaptation in real-world environments. Title-only evidence supports changing and adverse noise, without establishing adaptation robustness.", "listening-and-separation", "noise-enhancement", "nonstationary-noise"),
    "fdcb2a96a83e0b410af16d270de3604188a0f634": ("confirmed-current-boundary", "The title explicitly concerns expressive voice conversion with controllable emotional intensity. Title-only evidence supports style and emotion control, without establishing emotional controllability or conversion quality.", "voice-generation-and-control", "expression-and-interactive-control", "style-and-emotion-control"),
    "fde621abd515c9d0ec593beb4c863ff16bf82ce7": ("rejected-out-of-scope", "The title concerns room impulse-response measurement and reflection suppression but does not establish a human-speech or spoken-language task. With title-only evidence, reverberant speech-room membership is not supported.", None, None, None),
    "fdfc05a09b7de29e3808fa964efac09882dd17a0": ("confirmed-current-boundary", "The title explicitly concerns content leakage in LibriSpeech and privacy evaluation of speaker anonymization. Title-only evidence supports voice privacy, without establishing leakage or anonymization protection.", "evaluation-deployment-and-consequence", "privacy-and-security", "voice-privacy"),
    "fe57ef4a3f50dd43df25151ffedf6bb5ad4e0c89": ("confirmed-current-boundary", "The title explicitly concerns zero-shot text-to-speech with enhanced prompts. Title-only evidence supports unseen-speaker synthesis, without establishing synthesis quality or speaker generalization.", "voice-generation-and-control", "identity-and-conversion", "zero-shot-voice"),
    "feae3e5e4abfb50309eb769b65ccc629651c8dca": ("reassigned-to-neighbor", "The title explicitly concerns streaming speech recognition and latency optimization. Title-only evidence places it under latency and resource budget rather than temporal alignment.", "evaluation-deployment-and-consequence", "deployment-cost", "latency-and-resource"),
    "fef784e8377f62db477265919d25298185f259c2": ("confirmed-current-boundary", "The title explicitly concerns beamforming and WPE for speech dereverberation. Title-only evidence supports spatial filtering, without establishing dereverberation quality.", "listening-and-separation", "spatial-listening", "spatial-filtering"),
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
