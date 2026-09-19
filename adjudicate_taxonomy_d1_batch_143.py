#!/usr/bin/env python3
"""Record the next eight evidence-bounded taxonomy adjudications."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "mondal25b_interspeech": (
        "confirmed-current-boundary",
        "The abstract proposes controllable word-stress exaggeration in TTS for language-learning feedback. The governing boundary is prosody control, bounded by the annotated Tatoeba subset and automatic/manual assessment.",
        ["title", "abstract"], "voice-generation-and-control", "expression-and-interactive-control", "prosody-control",
    ),
    "moore25_interspeech": (
        "confirmed-current-boundary",
        "The official archive title and D1 record describe speech-based intelligent interaction, but provide no abstract-level mechanism. The current dialogue-state boundary is retained only as a taxonomy-membership assignment; no scientific performance claim is made.",
        ["title", "archive_record"], "meaning-and-interaction", "intent-and-dialogue-state", "dialogue-state",
    ),
    "morais25_interspeech": (
        "confirmed-current-boundary",
        "The abstract evaluates speech emotion recognition with a Conformer encoder and language model and identifies paralinguistic information as the target. The evidence supports paralinguistic state, bounded by the reported ASR, SER, and speech-translation experiments.",
        ["title", "abstract"], "meaning-and-interaction", "prosody-and-paralinguistics", "paralinguistic-state",
    ),
    "mori25_interspeech": (
        "reassigned-to-neighbor",
        "The abstract uses human selective listening to propose an ASR evaluation that distinguishes transcription from information needed to generate a dialogue response. The governing boundary is word-error versus understanding, not accessibility fit, because the paper's primary move is an evaluation target.",
        ["title", "abstract"], "evaluation-deployment-and-consequence", "metric-and-human-targets", "word-error-versus-understanding",
    ),
    "mori25b_interspeech": (
        "reassigned-to-neighbor",
        "The abstract predicts complete user utterances and uses confidence to decide whether a response can be prefetched, with the stated goal of reducing user-perceived latency. The governing boundary is latency and resource budget, not dialogue state alone.",
        ["title", "abstract"], "evaluation-deployment-and-consequence", "deployment-cost", "latency-and-resource",
    ),
    "moriya25_interspeech": (
        "confirmed-current-boundary",
        "The abstract explicitly designs chunk-wise streaming and reports faster decoding in a dual-mode ASR system. The evidence supports latency and resource budget, bounded by the reported LC-BiMamba and Conformer comparison.",
        ["title", "abstract"], "evaluation-deployment-and-consequence", "deployment-cost", "latency-and-resource",
    ),
    "mote25_interspeech": (
        "confirmed-current-boundary",
        "The abstract measures shared phonetic structure across English, Taiwanese Mandarin, and Russian to support cross-lingual emotion recognition. The evidence supports cross-lingual transfer, bounded by the three languages, quantized representations, and distribution-similarity analysis.",
        ["title", "abstract"], "languages-accents-and-resources", "crosslingual-structure", "crosslingual-transfer",
    ),
    "mote25b_interspeech": (
        "confirmed-current-boundary",
        "The abstract transfers labeled information from resource-rich to low-resource languages through a shared quantized feature space for speech emotion recognition. The evidence supports cross-lingual transfer, bounded by the stated adaptation setting and classification evaluation.",
        ["title", "abstract"], "languages-accents-and-resources", "crosslingual-structure", "crosslingual-transfer",
    ),
}


def main():
    payload = json.loads(QUEUE.read_text())
    rows = {r["paper_id"]: r for r in payload["rows"]}
    for pid, (decision, note, sections, theme, subtheme, concept) in DECISIONS.items():
        row = rows[pid]
        if row["taxonomy_review_state"] == "taxonomy-adjudicated":
            raise SystemExit(f"already adjudicated: {pid}")
        row.update({
            "taxonomy_review_state": "taxonomy-adjudicated",
            "final_decision": decision,
            "reviewer_note": note,
            "reviewed_sections": sections,
            "final_theme_id": theme,
            "final_subtheme_id": subtheme,
            "final_concept_id": concept,
        })
    adjudicated = sum(r["taxonomy_review_state"] == "taxonomy-adjudicated" for r in rows.values())
    payload["adjudicated_count"] = adjudicated
    payload["open_count"] = len(rows) - adjudicated
    decisions = sorted({r.get("final_decision") for r in rows.values() if r["taxonomy_review_state"] == "taxonomy-adjudicated"})
    payload["decision_counts"] = {d: sum(r.get("final_decision") == d for r in rows.values() if r["taxonomy_review_state"] == "taxonomy-adjudicated") for d in decisions}
    QUEUE.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({"batch": len(DECISIONS), "adjudicated": adjudicated, "open": payload["open_count"]}))


if __name__ == "__main__":
    main()
