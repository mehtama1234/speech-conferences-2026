#!/usr/bin/env python3
"""Record the next eight evidence-bounded taxonomy adjudications."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "karpov25_interspeech": ("reassigned-to-neighbor", "The abstract describes building labeled data and then using pseudo-labeling for a zero-resource Armenian ASR system. The central low-resource mechanism is self-training and pseudo-label expansion, not few-shot adaptation from a small fixed support set.", ["title", "abstract"], "languages-accents-and-resources", "low-resource-learning", "self-training-and-pseudo-labels"),
    "kawamura25_interspeech": ("confirmed-current-boundary", "The title and abstract explicitly study compact text-to-speech waveform generation through 1.58-bit quantization and weight indexing. The evidence supports neural-vocoder and waveform-generation membership, bounded by the reported model-size and quality experiments.", ["title", "abstract"], "voice-generation-and-control", "waveform-and-codec-generation", "neural-vocoder"),
    "kawanishi25_interspeech": ("confirmed-current-boundary", "The title and abstract explicitly adapt both linguistic and paralinguistic response expression as a dialogue relationship develops. The speech-specific control object is paralinguistic state, without establishing general human-like relationship understanding.", ["title", "abstract"], "meaning-and-interaction", "prosody-and-paralinguistics", "paralinguistic-state"),
    "kc25_interspeech": ("confirmed-current-boundary", "The abstract evaluates voice mimicry by comparing spectral and prosodic speaker embeddings with human judgments of which artist is most proficient. The central evidence concerns speaker identity similarity, not general voice conversion generation.", ["title", "abstract"], "people-variation-and-health", "identity-and-life-stage", "speaker-verification"),
    "ke25_interspeech": ("confirmed-current-boundary", "The abstract uses pause duration and pause context as speech biomarkers for dementia detection. The evidence supports a clinical speech marker, while the corpus and classification results do not establish clinical diagnosis or deployment.", ["title", "abstract"], "people-variation-and-health", "clinical-markers", "clinical-speech-marker"),
    "khanday25_interspeech": ("confirmed-current-boundary", "The abstract reconstructs high-gamma neural activity during speech production from language and speech-model embeddings. This is an alternate sensing path for a speech-production process, so non-airborne speech sensing is the closest boundary; reconstruction correlation is not evidence of a usable communication device.", ["title", "abstract"], "sound-and-production", "room-channel-and-sensing", "non-airborne-sensing"),
    "khurana25_interspeech": ("confirmed-current-boundary", "The abstract explicitly factorizes a neural speech codec into acoustic, phonetic, and lexical token sets and evaluates their linguistic information and reconstruction. The evidence supports learned speech units, without proving that the factors are uniquely or universally linguistic.", ["title", "abstract"], "recognition-and-alignment", "acoustic-unit-learning", "self-supervised-speech-units"),
    "kienegger25_interspeech": ("confirmed-current-boundary", "The abstract extracts a moving target speaker from a mixture using only the target's initial position plus learned tracking. The central pressure is target-conditioned separation under changing spatial cues, not generic spatial filtering alone.", ["title", "abstract"], "listening-and-separation", "source-separation", "target-conditioned-separation"),
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
