#!/usr/bin/env python3
"""Record the next eight evidence-bounded taxonomy adjudications."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "eads25_interspeech": ("confirmed-current-boundary", "The title and abstract explicitly present a child speech corpus pairing audio with ultrasound articulation for speech-sound feedback. The evidence supports articulatory coordination; it does not establish therapy effectiveness.", ["title", "abstract"], "sound-and-production", "articulatory-dynamics", "articulatory-coordination"),
    "elhajal25_interspeech": ("confirmed-current-boundary", "The title and abstract explicitly perform dysarthric-to-healthy rhythm and voice conversion while measuring downstream ASR. The evidence supports voice conversion, without establishing preservation of every speaker property.", ["title", "abstract"], "voice-generation-and-control", "identity-and-conversion", "voice-conversion"),
    "elkheir25_interspeech": ("reassigned-to-neighbor", "The title and abstract explicitly detect synthetic or deepfake speech using spectro-temporal evidence. This is spoofing and synthetic-voice security, not separation of simultaneous sources.", ["title", "abstract"], "evaluation-deployment-and-consequence", "privacy-and-security", "spoofing-and-deepfake"),
    "elleuch25_interspeech": ("confirmed-current-boundary", "The title and abstract explicitly build and evaluate an Arabic dialect identification dataset covering many varieties. The evidence supports language and variety identification, without establishing coverage of all Arabic use.", ["title", "abstract"], "languages-accents-and-resources", "crosslingual-structure", "language-identification"),
    "emezue25_interspeech": ("confirmed-current-boundary", "The title and abstract explicitly collect a large, culturally diverse speech-text dataset for under-represented African languages. The evidence supports speech data collection, without proving equal performance for every community.", ["title", "abstract"], "languages-accents-and-resources", "data-creation", "speech-data-collection"),
    "eom25_interspeech": ("confirmed-current-boundary", "The title and abstract explicitly learn flexible monotonic temporal alignments for speech representations under speaking-rate changes. The evidence supports temporal alignment, without proving robustness beyond the reported tasks.", ["title", "abstract"], "recognition-and-alignment", "boundaries-and-alignment", "alignment"),
    "eren25_interspeech": ("reassigned-to-neighbor", "The title and abstract explicitly predict prosodic features from acoustic and textual inputs for downstream speech synthesis. This is prosody control in voice generation, not interpretation of prosodic meaning.", ["title", "abstract"], "voice-generation-and-control", "expression-and-interactive-control", "prosody-control"),
    "ersoy25_interspeech": ("confirmed-current-boundary", "The title and abstract explicitly analyze whether speech and text models form abstract semantic concepts and compare their latent structures. The evidence supports referential grounding, without proving human-like understanding.", ["title", "abstract"], "meaning-and-interaction", "grounding-and-action", "referential-grounding"),
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
