#!/usr/bin/env python3
"""Record the twenty-seventh title-only D1 taxonomy adjudication batch."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "ac4bc340ad2965e56c69ff538b36db1136b7bd53": ("confirmed-current-boundary", "The title explicitly concerns fatigue detection using speech and personal assessments. Title-only evidence supports paralinguistic-state membership, without establishing a clinical or psychological diagnosis.", "meaning-and-interaction", "prosody-and-paralinguistics", "paralinguistic-state"),
    "ae0b1f3f46c4244609dc7deb1b925ca5eb495982": ("confirmed-current-boundary", "The title explicitly concerns audio-visual speech separation. Title-only evidence supports time-frequency masking within speech enhancement.", "listening-and-separation", "noise-enhancement", "spectral-mask"),
    "ae15b281fb4457fc9393442487657e832af7ee37": ("confirmed-current-boundary", "The title explicitly concerns speaker anonymization that preserves emotion. Title-only evidence supports voice privacy, without establishing an anonymization guarantee.", "evaluation-deployment-and-consequence", "privacy-and-security", "voice-privacy"),
    "aea25182c5962be7d867b5ba34348fb01c98be9c": ("confirmed-current-boundary", "The title explicitly concerns speech translation with speech-entity prompts. Title-only evidence supports cross-lingual transfer.", "languages-accents-and-resources", "crosslingual-structure", "crosslingual-transfer"),
    "aeaafa08c713bfc127c269676c49038df07119f3": ("confirmed-current-boundary", "The title explicitly concerns content-preserving speech representations with segment-level alignment. Title-only evidence supports learned speech-unit membership.", "recognition-and-alignment", "acoustic-unit-learning", "self-supervised-speech-units"),
    "aef8e955a158867909b3dc5c22b529f24384c1e0": ("rejected-out-of-scope", "The title concerns general audio deepfake detection but does not establish synthetic speech or spoken-language evidence. With title-only evidence, speech spoofing membership is not supported.", None, None, None),
    "af1a8da1fee78af9c88e4366740c01e1c757d395": ("confirmed-current-boundary", "The title explicitly concerns classification of multi-stutter speech. Title-only evidence supports atypical-articulation and dysarthria membership.", "people-variation-and-health", "atypical-and-assistive-speech", "dysarthria-and-atypical-speech"),
    "af4113105be30b5accdadcf03ce0f2eb3313688e": ("rejected-out-of-scope", "The title concerns perceptual defect assessment for general audio and does not establish a human-speech or spoken-language task. With title-only evidence, speech quality membership is not supported.", None, None, None),
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
