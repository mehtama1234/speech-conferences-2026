#!/usr/bin/env python3
"""Record the next eight evidence-bounded taxonomy adjudications."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "ma25b_interspeech": ("confirmed-current-boundary", "The abstract grades spoken second-language proficiency from speech and evaluates generalization across tasks and parts. The evidence supports accent robustness and linguistic variation, bounded by the L2 datasets and grading targets.", ["title", "abstract"], "languages-accents-and-resources", "accent-dialect-and-cultural-meaning", "accent-robustness"),
    "ma25c_interspeech": ("confirmed-current-boundary", "The abstract enhances an on-screen target speaker using audio-visual representations and suppresses interfering speakers and noise in real time. The evidence supports target-conditioned separation, bounded by the CPU streaming and multi-speaker tests.", ["title", "abstract"], "listening-and-separation", "source-separation", "target-conditioned-separation"),
    "maciejewski25_interspeech": ("confirmed-current-boundary", "The abstract supplies a target-speaker representation to locate that speaker's active time regions and uses an implicit separation front end. The evidence supports target-conditioned separation, bounded by the TS-VAD training domains.", ["title", "abstract"], "listening-and-separation", "source-separation", "target-conditioned-separation"),
    "maeda25_interspeech": ("confirmed-current-boundary", "The abstract jointly detects and recognizes a selected speaker in multi-speaker mixtures and reports both recognition and diarization results. The evidence supports target-conditioned separation, bounded by Libri2Mix and Libri3Mix.", ["title", "abstract"], "listening-and-separation", "source-separation", "target-conditioned-separation"),
    "magoshi25_interspeech": ("confirmed-current-boundary", "The abstract predicts language-independent articulatory features and IPA tokens for multilingual and zero-shot ASR across 22 languages. The evidence supports cross-lingual transfer, bounded by the XLS-R fine-tuning and zero-shot languages.", ["title", "abstract"], "languages-accents-and-resources", "crosslingual-structure", "crosslingual-transfer"),
    "mahapatra25_interspeech": ("confirmed-current-boundary", "The abstract evaluates anti-spoofing under emotional synthetic speech, identifies emotion-dependent failures, and proposes an emotion-aware defense. The evidence supports spoofing and synthetic-voice misuse, bounded by EmoSpoof-TTS and the tested emotions.", ["title", "abstract"], "evaluation-deployment-and-consequence", "privacy-and-security", "spoofing-and-deepfake"),
    "mai25b_interspeech": ("confirmed-current-boundary", "The abstract adds automatically described acoustic properties to a speech language model for emotion recognition and evaluates multiple emotion datasets. The evidence supports paralinguistic state, bounded by IEMOCAP, MELD, and LSSED.", ["title", "abstract"], "meaning-and-interaction", "prosody-and-paralinguistics", "paralinguistic-state"),
    "mai25c_interspeech": ("confirmed-current-boundary", "The abstract transfers fine-grained emotion-related acoustic reasoning into a speech emotion model and evaluates in-domain and out-of-domain recognition. The evidence supports paralinguistic state, bounded by the reported datasets and distillation procedure.", ["title", "abstract"], "meaning-and-interaction", "prosody-and-paralinguistics", "paralinguistic-state"),
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
