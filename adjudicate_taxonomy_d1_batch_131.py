#!/usr/bin/env python3
"""Record the next eight evidence-bounded taxonomy adjudications."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "lin25e_interspeech": ("confirmed-current-boundary", "The abstract studies how age changes the integration of prosodic, semantic, and facial emotion cues and reports channel-specific listener differences. The evidence supports prosodic meaning, bounded by the Stroop task and age groups.", ["title", "abstract"], "meaning-and-interaction", "prosody-and-paralinguistics", "prosodic-meaning"),
    "lin25f_interspeech": ("rejected-out-of-scope", "The abstract identifies people from EEG using a music emotion dataset and does not establish a human-speech or spoken-language signal. EEG person identification without a speech object is outside this taxonomy.", ["title", "abstract"], None, None, None),
    "lin25g_interspeech": ("confirmed-current-boundary", "The abstract predicts and activates complete contextual phrases in ASR decoding and evaluates the effect on rare or biased phrases. The evidence supports domain and context biasing, bounded by the Librispeech and WenetSpeech tests.", ["title", "abstract"], "recognition-and-alignment", "context-and-open-vocabulary", "domain-and-context-biasing"),
    "lin25h_interspeech": ("confirmed-current-boundary", "The abstract accelerates autoregressive speech synthesis with draft-and-verify decoding and measures speed against fidelity and naturalness. The evidence supports interactive generation latency, bounded by the reported 1.4x speedup and model setting.", ["title", "abstract"], "voice-generation-and-control", "expression-and-interactive-control", "interactive-latency"),
    "linke25_interspeech": ("confirmed-current-boundary", "The abstract tests how same-speaker and cross-speaker conversational context affects low-resource ASR and short-turn recognition. The evidence supports long-context decoding, bounded by Austrian German and the seven evaluated systems.", ["title", "abstract"], "recognition-and-alignment", "context-and-open-vocabulary", "long-context-decoding"),
    "liu25_interspeech": ("confirmed-current-boundary", "The abstract develops a speaker-verification model that captures local and global sequence context and evaluates accuracy and efficiency. The evidence supports speaker verification, bounded by the reported model and test conditions.", ["title", "abstract"], "people-variation-and-health", "identity-and-life-stage", "speaker-verification"),
    "liu25b_interspeech": ("confirmed-current-boundary", "The abstract measures memorization in LLM-based ASR and removes personal training data on request while evaluating privacy and utility. The evidence supports voice privacy, bounded by LibriSpeech and the tested unlearning procedures.", ["title", "abstract"], "evaluation-deployment-and-consequence", "privacy-and-security", "voice-privacy"),
    "liu25c_interspeech": ("confirmed-current-boundary", "The abstract edits speech from text while retrieving matching emotional references so the edited segment stays emotionally consistent and preserves speaker identity. The evidence supports style and emotion control, bounded by the ECD-TSE data and subjective/objective tests.", ["title", "abstract"], "voice-generation-and-control", "expression-and-interactive-control", "style-and-emotion-control"),
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
