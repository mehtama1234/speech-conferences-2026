#!/usr/bin/env python3
"""Record the next eight evidence-bounded taxonomy adjudications."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "huang25j_interspeech": ("confirmed-current-boundary", "The title and abstract explicitly compare word-level errors in ASR and brain-to-text systems and measure semantic costs of rare-word mistakes. The evidence supports word error versus understanding, without reducing usability to one metric.", ["title", "abstract"], "evaluation-deployment-and-consequence", "metric-and-human-targets", "word-error-versus-understanding"),
    "hui25_interspeech": ("reassigned-to-neighbor", "The title and abstract explicitly test perception of a language-specific long-short vowel contrast across Māori listeners, learners, and room conditions. This belongs under dialect and variety structure, not cultural meaning.", ["title", "abstract"], "languages-accents-and-resources", "accent-dialect-and-cultural-meaning", "dialect-and-variety"),
    "huo25_interspeech": ("confirmed-current-boundary", "The title and abstract explicitly compare self-supervised speech representations and show how iterative refinement encodes word, phoneme, and speaker information. The evidence supports learned speech units, without proving one training cause universally.", ["title", "abstract"], "recognition-and-alignment", "acoustic-unit-learning", "self-supervised-speech-units"),
    "hussein25_interspeech": ("confirmed-current-boundary", "The title and abstract explicitly disentangle discrete semantic and acoustic speech tokens while preserving recognition and reconstruction. The evidence supports learned speech units, without proving complete semantic-acoustic separation.", ["title", "abstract"], "recognition-and-alignment", "acoustic-unit-learning", "self-supervised-speech-units"),
    "hutin25_interspeech": ("confirmed-current-boundary", "The title and abstract explicitly compare formants and duration of French schwa and neighboring vowels under controlled stress and orthography. The evidence supports vocal-tract filtering, without resolving all French schwa variation.", ["title", "abstract"], "sound-and-production", "source-generation", "vocal-tract-filter"),
    "huttner25_interspeech": ("reassigned-to-neighbor", "The title and abstract explicitly measure participants' reported communication difficulty and relate it to vocal effort, hearing status, noise, hearing aids, and turn timing. The direct human target is listener effort, not device or environment fit alone.", ["title", "abstract"], "people-variation-and-health", "human-centered-accessibility", "listener-effort"),
    "hwang25_interspeech": ("confirmed-current-boundary", "The title and abstract explicitly use voice and speech representations to detect dysphagia under scarce medical data and report diagnostic metrics. The evidence supports a clinical speech marker, without establishing safe clinical diagnosis.", ["title", "abstract"], "people-variation-and-health", "clinical-markers", "clinical-speech-marker"),
    "ibrahimov25_interspeech": ("confirmed-current-boundary", "The title and abstract explicitly convert ultrasound articulatory measurements into speech for a silent-speech interface and compare perceptual quality. The evidence supports non-airborne speech sensing, without proving microphone-free communication generally.", ["title", "abstract"], "sound-and-production", "room-channel-and-sensing", "non-airborne-sensing"),
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
