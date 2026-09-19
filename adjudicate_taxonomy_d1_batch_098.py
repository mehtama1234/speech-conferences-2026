#!/usr/bin/env python3
"""Record the next eight evidence-bounded taxonomy adjudications."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "glazer25_interspeech": ("reassigned-to-neighbor", "The title and abstract explicitly adapt a detector to unseen voice-cloning attacks and identify audio deepfakes. The governing problem is spoofing and synthetic-voice misuse, not generic few-shot adaptation.", ["title", "abstract"], "evaluation-deployment-and-consequence", "privacy-and-security", "spoofing-and-deepfake"),
    "gogate25_interspeech": ("reassigned-to-neighbor", "The title and abstract explicitly use enrollment audio to preserve a personalized target speaker while suppressing competing noise in audio-visual enhancement. This belongs under target-conditioned separation.", ["title", "abstract"], "listening-and-separation", "source-separation", "target-conditioned-separation"),
    "gogoi25_interspeech": ("reassigned-to-neighbor", "The title and abstract explicitly classify and assess dementia from speech rhythm features. The acoustic representation is the mechanism; the governing task is a clinical speech marker.", ["title", "abstract"], "people-variation-and-health", "clinical-markers", "clinical-speech-marker"),
    "gogoi25b_interspeech": ("confirmed-current-boundary", "The title and abstract explicitly recognize lexical tones in low-resource languages and analyze language-specific pitch representations and dialect variation. The evidence supports prosodic meaning, without proving transfer across all tonal languages.", ["title", "abstract"], "meaning-and-interaction", "prosody-and-paralinguistics", "prosodic-meaning"),
    "gohider25_interspeech": ("reassigned-to-neighbor", "The title and abstract explicitly optimize ASR for disordered speech and analyze disfluencies under a speech-accessibility challenge. The central speech object is atypical speech recognition, not demonstrated user or device fit.", ["title", "abstract"], "people-variation-and-health", "atypical-and-assistive-speech", "dysarthria-and-atypical-speech"),
    "gomezzaragoza25_interspeech": ("reassigned-to-neighbor", "The title and abstract explicitly detect depression from speech and text across languages and report fairness differences. The governing claim is a possible clinical speech marker, not merely a generic paralinguistic state.", ["title", "abstract"], "people-variation-and-health", "clinical-markers", "clinical-speech-marker"),
    "gong25_interspeech": ("confirmed-current-boundary", "The title and abstract explicitly retrieve rare words and named entities for contextual ASR while controlling homophone confusion and list scale. The evidence supports domain and context biasing, without proving all open-vocabulary conditions.", ["title", "abstract"], "recognition-and-alignment", "context-and-open-vocabulary", "domain-and-context-biasing"),
    "gong25b_interspeech": ("reassigned-to-neighbor", "The title and abstract explicitly use self-supervised learning to adapt speech emotion recognition to low-resource languages with scarce annotations. The central pressure is few-shot or scarce-data adaptation, not emotion-state definition alone.", ["title", "abstract"], "languages-accents-and-resources", "low-resource-learning", "few-shot-adaptation"),
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
