#!/usr/bin/env python3
"""Record the next eight evidence-bounded taxonomy adjudications."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "janse25_interspeech": ("reassigned-to-neighbor", "The title and abstract explicitly predict listener-effort ratings in noise and compare habitual with clear-Lombard speech. The direct target is listener effort, not control of speaking style.", ["title", "abstract"], "people-variation-and-health", "human-centered-accessibility", "listener-effort"),
    "javed25_interspeech": ("reassigned-to-neighbor", "The title and abstract explicitly benchmark continual ASR learning as new languages and domains arrive in real speech data. The governing pressure is adaptation to changing languages and domains, not cross-lingual transfer alone.", ["title", "abstract"], "languages-accents-and-resources", "low-resource-learning", "few-shot-adaptation"),
    "ji25_interspeech": ("confirmed-current-boundary", "The title and abstract explicitly analyze Mandarin lexical-tone production by native and L2 speakers under noise, including F0, duration, and intensity changes. The evidence supports prosodic meaning, without proving all learner or noise conditions.", ["title", "abstract"], "meaning-and-interaction", "prosody-and-paralinguistics", "prosodic-meaning"),
    "jia25_interspeech": ("confirmed-current-boundary", "The title and abstract explicitly detect Alzheimer's disease from multilingual spontaneous speech and test low-resource improvements. The evidence supports a clinical speech marker, without establishing diagnosis or clinical validity.", ["title", "abstract"], "people-variation-and-health", "clinical-markers", "clinical-speech-marker"),
    "jiang25_interspeech": ("confirmed-current-boundary", "The title and abstract explicitly separate regional speech using microphone-array direction, distance, and reverberation cues. The evidence supports spatial filtering, without proving all regions or room conditions.", ["title", "abstract"], "listening-and-separation", "spatial-listening", "spatial-filtering"),
    "jin25_interspeech": ("confirmed-current-boundary", "The title and abstract explicitly route a mixed-bandwidth speech-to-text model across ASR and speech-translation tasks using supervised experts. The evidence supports acoustic-to-token mapping, without proving task routing eliminates all interference.", ["title", "abstract"], "recognition-and-alignment", "acoustic-unit-learning", "acoustic-to-token"),
    "jin25b_interspeech": ("confirmed-current-boundary", "The title and abstract explicitly align multilingual phonemes to audio on devices and report forced-alignment latency and accuracy. The evidence supports temporal alignment, without proving all languages and hardware.", ["title", "abstract"], "recognition-and-alignment", "boundaries-and-alignment", "alignment"),
    "jin25c_interspeech": ("confirmed-current-boundary", "The title and abstract explicitly detect and diagnose syllable- and phoneme-level mispronunciations for speech audiometry and hearing assessment. The evidence supports a clinical speech marker, without replacing audiological diagnosis.", ["title", "abstract"], "people-variation-and-health", "clinical-markers", "clinical-speech-marker"),
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
