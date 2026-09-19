#!/usr/bin/env python3
"""Record the next eight evidence-bounded taxonomy adjudications."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "hu25e_interspeech": ("confirmed-current-boundary", "The title and abstract explicitly predict word-level start and end timestamps for ASR and speech translation output. The evidence supports temporal alignment, without proving perfect timing across languages.", ["title", "abstract"], "recognition-and-alignment", "boundaries-and-alignment", "alignment"),
    "hu25f_interspeech": ("confirmed-current-boundary", "The title and abstract explicitly model simultaneous user and agent speech, barge-in, and turn-taking in a duplex speech-to-speech system. The evidence supports turn-boundary prediction, without proving all real-time interaction conditions.", ["title", "abstract"], "meaning-and-interaction", "turn-taking-and-repair", "turn-boundary"),
    "hu25g_interspeech": ("reassigned-to-neighbor", "The title and abstract explicitly allocate sensor rate and selection under wireless energy and performance constraints for speech enhancement. The governing boundary is bandwidth and resource budget, not adverse noise alone.", ["title", "abstract"], "evaluation-deployment-and-consequence", "deployment-cost", "latency-and-resource"),
    "hu25i_interspeech": ("confirmed-current-boundary", "The title and abstract explicitly disentangle source content and target speaker identity for zero-shot voice conversion and evaluate unseen speakers. The evidence supports voice conversion, without proving identity preservation for all targets.", ["title", "abstract"], "voice-generation-and-control", "identity-and-conversion", "voice-conversion"),
    "hu25j_interspeech": ("confirmed-current-boundary", "The title and abstract explicitly encrypt speaker templates while retaining speaker-verification accuracy and resisting voice exposure. The evidence supports voice privacy, without proving protection against every attack.", ["title", "abstract"], "evaluation-deployment-and-consequence", "privacy-and-security", "voice-privacy"),
    "hu25l_interspeech": ("reassigned-to-neighbor", "The title and abstract explicitly unify listener scoring scales for speech quality assessment and continuous emotion recognition. The central evaluation target is quality and naturalness, not listener effort as a user burden.", ["title", "abstract"], "evaluation-deployment-and-consequence", "metric-and-human-targets", "quality-and-naturalness"),
    "hu25m_interspeech": ("rejected-out-of-scope", "The title and abstract concern multichannel active noise control and microphone/filter selection without establishing a human-speech or spoken-language object. It is outside this speech taxonomy.", ["title", "abstract"], None, None, None),
    "huang25_interspeech": ("rejected-out-of-scope", "The title and abstract concern lyrics transcription in singing and music mixtures rather than ordinary human speech or spoken-language evidence. It is outside this speech taxonomy.", ["title", "abstract"], None, None, None),
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
