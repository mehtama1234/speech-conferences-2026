#!/usr/bin/env python3
"""Record the next eight evidence-bounded taxonomy adjudications."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "merzougui25_interspeech": ("rejected-out-of-scope", "The abstract builds an auditory tag-cloud interface for non-visual web browsing but does not establish a human-speech or spoken-language object. Auditory accessibility alone is not sufficient for this speech taxonomy.", ["title", "abstract"], None, None, None),
    "meyer25_interspeech": ("confirmed-current-boundary", "The abstract evaluates voice anonymization for multilingual code-switching speech and measures privacy and utility under spontaneous conditions. The evidence supports voice privacy, bounded by the code-switching corpora and anonymization systems.", ["title", "abstract"], "evaluation-deployment-and-consequence", "privacy-and-security", "voice-privacy"),
    "millot25_interspeech": ("reassigned-to-neighbor", "The abstract interprets automatically discovered voice attributes in a speaker-recognition system and evaluates their relation to gender, age, and phonation. The governing task is speaker verification, not only within-speaker state variation.", ["title", "abstract"], "people-variation-and-health", "identity-and-life-stage", "speaker-verification"),
    "mimura25_interspeech": ("confirmed-current-boundary", "The abstract uses language-specific and shared phonetic experts for multilingual streaming ASR and evaluates 22-language behavior. The evidence supports cross-lingual transfer, bounded by CommonVoice and the sparse-expert design.", ["title", "abstract"], "languages-accents-and-resources", "crosslingual-structure", "crosslingual-transfer"),
    "miniconi25_interspeech": ("confirmed-current-boundary", "The abstract selects human annotations actively to adapt automatic MOS predictors across languages and domains. The evidence supports quality and naturalness measurement, bounded by the MOS tasks and active-learning strategies.", ["title", "abstract"], "evaluation-deployment-and-consequence", "metric-and-human-targets", "quality-and-naturalness"),
    "minixhofer25_interspeech": ("confirmed-current-boundary", "The abstract studies synthetic speech as a replacement for real ASR training data and models how data scale and distribution mismatch affect performance. The evidence supports speech-data collection and creation, bounded by the TTS models and scaling experiments.", ["title", "abstract"], "languages-accents-and-resources", "data-creation", "speech-data-collection"),
    "miodonska25_interspeech": ("confirmed-current-boundary", "The abstract detects non-normative sibilant articulation in Polish children and frames the result as an automated pronunciation-assessment and diagnostic tool. The evidence supports atypical articulation and dysarthria as the broader atypical-speech boundary.", ["title", "abstract"], "people-variation-and-health", "atypical-and-assistive-speech", "dysarthria-and-atypical-speech"),
    "mitrofanov25_interspeech": ("rejected-out-of-scope", "The abstract evaluates a general auditory-capable language model across speech and other sounds but does not establish a specific human-speech or spoken-language task. Generic auditory benchmarking is insufficient for membership here.", ["title", "abstract"], None, None, None),
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
