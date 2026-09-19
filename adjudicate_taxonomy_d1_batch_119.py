#!/usr/bin/env python3
"""Record the next eight evidence-bounded taxonomy adjudications."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "klejch25_interspeech": ("reassigned-to-neighbor", "The abstract studies ASR for a low-resource language and relies on continued self-supervised pretraining plus semi-supervised training to use unlabeled data. The central mechanism is self-training and pseudo-label expansion, not adaptation from a fixed few-shot support set.", ["title", "abstract"], "languages-accents-and-resources", "low-resource-learning", "self-training-and-pseudo-labels"),
    "ko25_interspeech": ("confirmed-current-boundary", "The abstract explicitly addresses ASR overfitting and generalization by regularizing representations and evaluates robustness across several end-to-end architectures. The evidence supports distribution shift and generalization, bounded by the reported experiments.", ["title", "abstract"], "evaluation-deployment-and-consequence", "robustness-and-shift", "distribution-shift"),
    "komatsu25_interspeech": ("rejected-out-of-scope", "The abstract evaluates audio-text retrieval on Clotho and AudioCaps and does not establish a human-speech or spoken-language object. Audio-text alignment alone is insufficient for membership in this speech taxonomy.", ["title", "abstract"], None, None, None),
    "kommagouni25_interspeech": ("reassigned-to-neighbor", "The abstract distinguishes typical disfluencies from stuttering-related atypical disfluencies and evaluates speech-disorder classification. The governing boundary is atypical speech and its variation, not preserving disfluency events in recognition output.", ["title", "abstract"], "people-variation-and-health", "atypical-and-assistive-speech", "dysarthria-and-atypical-speech"),
    "kommineni25_interspeech": ("rejected-out-of-scope", "The abstract studies multimodal analysis of child-focused diagnostic videos and broad activity or atypical-behavior recognition. It does not isolate a speech or spoken-language marker, so assigning it to clinical speech evidence would overstate the abstract support.", ["title", "abstract"], None, None, None),
    "kondo25_interspeech": ("confirmed-current-boundary", "The abstract explicitly constructs and documents a Japanese speech corpus with speaker, style, cultural, and ethical metadata for speech-generation evaluation. The evidence supports speech-data collection, bounded by its idol-speaker population and non-commercial access conditions.", ["title", "abstract"], "languages-accents-and-resources", "data-creation", "speech-data-collection"),
    "kong25_interspeech": ("confirmed-current-boundary", "The abstract retrieves user-relevant words from audio and text to construct prompts for contextual ASR decoding. The evidence directly supports domain and context biasing, without implying general language understanding beyond the prompted entities.", ["title", "abstract"], "recognition-and-alignment", "context-and-open-vocabulary", "domain-and-context-biasing"),
    "kong25b_interspeech": ("reassigned-to-neighbor", "The abstract uses multichannel spatial decomposition and array-geometry handling to make speech recognition robust across microphone layouts. The governing operation is spatial filtering and sound-field handling, not temporal alignment of linguistic units.", ["title", "abstract"], "listening-and-separation", "spatial-listening", "spatial-filtering"),
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
