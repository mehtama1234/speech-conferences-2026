#!/usr/bin/env python3
"""Record the next eight evidence-bounded taxonomy adjudications."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "ick25_interspeech": ("rejected-out-of-scope", "The title and abstract concern direction-aware acoustic fields and Ambisonic room impulse responses for general sound fields, without establishing a human-speech or spoken-language object. It is outside this speech taxonomy.", ["title", "abstract"], None, None, None),
    "inoue25_interspeech": ("confirmed-current-boundary", "The title and abstract explicitly infer personality traits from acoustic, textual, and behavioral cues in fully duplex speech dialogues and compare them with human judgments. The evidence supports paralinguistic state, without proving stable personality inference.", ["title", "abstract"], "meaning-and-interaction", "prosody-and-paralinguistics", "paralinguistic-state"),
    "ishikawa25_interspeech": ("rejected-out-of-scope", "The title and abstract concern general audio-visual-text representation learning and retrieval from videos, without establishing a human-speech or spoken-language object. It is outside this speech taxonomy.", ["title", "abstract"], None, None, None),
    "istaiteh25_interspeech": ("confirmed-current-boundary", "The title and abstract explicitly evaluate speech translation and speech-text or speech-speech entailment and contradiction rather than similarity alone. The evidence supports word error versus understanding, without proving complete semantic evaluation.", ["title", "abstract"], "evaluation-deployment-and-consequence", "metric-and-human-targets", "word-error-versus-understanding"),
    "ivucic25_interspeech": ("confirmed-current-boundary", "The title and abstract explicitly decode attended speakers from EEG speech-envelope tracking in multi-speaker listening and test attention switching. The evidence supports non-airborne speech sensing, without proving a practical hearing device.", ["title", "abstract"], "sound-and-production", "room-channel-and-sensing", "non-airborne-sensing"),
    "jacquelin25_interspeech": ("confirmed-current-boundary", "The title and abstract explicitly disentangle and control vocal effort in a neural speech codec and evaluate neutral-to-Lombard conversion. The evidence supports prosody control, without proving every effort or speaker condition.", ["title", "abstract"], "voice-generation-and-control", "expression-and-interactive-control", "prosody-control"),
    "jahan25_interspeech": ("confirmed-current-boundary", "The title and abstract explicitly create a speech fairness dataset with demographic and conversational annotations and test racial bias across ASR systems. The evidence supports auditability and contestability, without covering every group or task.", ["title", "abstract"], "evaluation-deployment-and-consequence", "auditability-and-accountability", "auditability-and-contestability"),
    "jalal25_interspeech": ("confirmed-current-boundary", "The title and abstract explicitly train target-speaker diarization and separation with robust speaker embeddings under overlap and noise. The evidence supports target-conditioned separation, without proving enrollment-free robustness everywhere.", ["title", "abstract"], "listening-and-separation", "source-separation", "target-conditioned-separation"),
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
