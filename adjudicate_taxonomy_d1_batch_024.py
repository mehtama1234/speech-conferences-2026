#!/usr/bin/env python3
"""Record the thirteenth title-only D1 taxonomy adjudication batch."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "49e79c7f999ab06a3e7d5cc9b19319ee93b8ef05": ("confirmed-current-boundary", "The title explicitly concerns large speech-language models evaluating expressive speech. Title-only evidence supports quality and naturalness, without establishing agreement with human listeners.", "evaluation-deployment-and-consequence", "metric-and-human-targets", "quality-and-naturalness"),
    "4b580de823ac5593b4bedaecb0e2fd33fba3b352": ("reassigned-to-neighbor", "The title explicitly concerns fine-grained estimation of automatic speech recognition errors. The direct boundary is word-error measurement rather than calibration and selective use.", "evaluation-deployment-and-consequence", "metric-and-human-targets", "word-error-versus-understanding"),
    "4be134ffad97a3a473833d3aba007c6b59054fc3": ("confirmed-current-boundary", "The title explicitly concerns prompt tuning for speech-language models. Title-only evidence supports domain and context biasing.", "recognition-and-alignment", "context-and-open-vocabulary", "domain-and-context-biasing"),
    "4d989bc72dbc0c12ff4c28dd4d73d75c69953cb4": ("confirmed-current-boundary", "The title explicitly concerns a real-world spoofing-aware speaker-verification system. Title-only evidence supports spoofing and synthetic-voice misuse.", "evaluation-deployment-and-consequence", "privacy-and-security", "spoofing-and-deepfake"),
    "502aba0d0be1f72c5bd3b0f976e19899597dc5d7": ("rejected-out-of-scope", "The title concerns source-free domain adaptation for video and a video-language model but does not establish a human-speech or spoken-language task. With title-only evidence, speech robustness membership is not supported.", None, None, None),
    "509738b8db425d90e83d79476bae8d1cf265142b": ("confirmed-current-boundary", "The title explicitly concerns multimodal control for cued-speech video generation and names asynchronous behavior. Title-only evidence supports interactive generation latency.", "voice-generation-and-control", "expression-and-interactive-control", "interactive-latency"),
    "52756cff017ebb99ec3d75a4560d7fc4b9668806": ("confirmed-current-boundary", "The title explicitly concerns dysarthric speech recognition. Title-only evidence supports atypical-articulation and dysarthria membership.", "people-variation-and-health", "atypical-and-assistive-speech", "dysarthria-and-atypical-speech"),
    "5286e4c6b44b4986da4a0a790af3bf8ac5893e00": ("rejected-out-of-scope", "The title concerns general audio anti-spoofing but does not establish synthetic speech or spoken-language evidence. With title-only evidence, speech spoofing membership is not supported.", None, None, None),
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
