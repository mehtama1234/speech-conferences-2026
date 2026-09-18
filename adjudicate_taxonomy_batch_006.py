#!/usr/bin/env python3
"""Record the sixth small, full-paper taxonomy adjudication batch."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "benway25_interspeech": ("confirmed-current-boundary", "The paper uses inverted articulatory trajectories to distinguish childhood speech-sound error subtypes. It connects measurable speech to a clinical marker, while the selected English errors and inversion model limit clinical reach.", "people-variation-and-health", "clinical-markers", "clinical-speech-marker"),
    "berger25_interspeech": ("confirmed-current-boundary", "The contribution is a text-to-speech frontend that predicts pronunciation and prosodic labels for underrepresented accents with less labeled data. The mechanism is planning the spoken form before waveform generation.", "voice-generation-and-control", "content-planning", "text-to-speech-planning"),
    "bhattacharya25_interspeech": ("confirmed-current-boundary", "The observational study measures when Spanish-English speakers switch and relates it to language background and ability. It distinguishes switching behavior from general multilingual competence, without claiming causal explanations.", "languages-accents-and-resources", "crosslingual-structure", "code-switching"),
    "biswas25_interspeech": ("confirmed-current-boundary", "Synthetic language switches and prompts adapt Whisper to Hindi-English code-mixed speech, with transcription and switch accuracy evaluated. The language pair and tutorial domain bound the transfer claim.", "languages-accents-and-resources", "crosslingual-structure", "code-switching"),
    "biyani25_interspeech": ("confirmed-current-boundary", "Time-reversed speech supplies an additional speaker-representation view for diffusion voice conversion while the content path carries language. The paper directly tests identity preservation versus content leakage.", "voice-generation-and-control", "identity-and-conversion", "voice-conversion"),
    "bokkahallisatish25_interspeech": ("confirmed-current-boundary", "The interactive paired-voice platform makes counterfactual differences in speech-to-speech responses inspectable. It is an auditability tool, not evidence of a population-level fairness effect.", "evaluation-deployment-and-consequence", "auditability-and-accountability", "auditability-and-contestability"),
    "botelho25_interspeech": ("confirmed-current-boundary", "The challenge systems combine acoustic, linguistic, and learned representations to identify cognitive-decline signals. Class imbalance, missing metadata, and challenge data prevent treating the scores as clinical validation.", "people-variation-and-health", "clinical-markers", "clinical-speech-marker"),
    "braun25_interspeech": ("confirmed-current-boundary", "The paper shows how a dementia assessment can correlate with human scores while behaving differently across severity groups because of production, ASR, and fallback effects. It is a clinical-marker validity analysis, not a new recognizer.", "people-variation-and-health", "clinical-markers", "clinical-speech-marker"),
}

def main():
    payload = json.loads(QUEUE.read_text())
    rows = {r["paper_id"]: r for r in payload["rows"]}
    for pid, (decision, note, theme, subtheme, concept) in DECISIONS.items():
        row = rows[pid]
        if row["taxonomy_review_state"] == "taxonomy-adjudicated":
            raise SystemExit(f"already adjudicated: {pid}")
        row.update({"taxonomy_review_state": "taxonomy-adjudicated", "final_decision": decision, "reviewer_note": note, "reviewed_sections": ["title", "abstract", "method", "experiments", "results", "limits"], "final_theme_id": theme, "final_subtheme_id": subtheme, "final_concept_id": concept})
    payload["adjudicated_count"] = sum(r["taxonomy_review_state"] == "taxonomy-adjudicated" for r in rows.values())
    payload["open_count"] = len(rows) - payload["adjudicated_count"]
    payload["decision_counts"] = {d: sum(r.get("final_decision") == d for r in rows.values() if r["taxonomy_review_state"] == "taxonomy-adjudicated") for d in sorted({r.get("final_decision") for r in rows.values() if r["taxonomy_review_state"] == "taxonomy-adjudicated"})}
    QUEUE.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({"batch": len(DECISIONS), "adjudicated": payload["adjudicated_count"], "open": payload["open_count"]}))

if __name__ == "__main__":
    main()
