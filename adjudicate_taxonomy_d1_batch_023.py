#!/usr/bin/env python3
"""Record the twelfth title-only D1 taxonomy adjudication batch."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "4404349e76404b052df0fead73af1bf2f711b8be": ("confirmed-current-boundary", "The title explicitly concerns generative speech enhancement. Title-only evidence supports speech-prior denoising.", "listening-and-separation", "noise-enhancement", "speech-prior-denoising"),
    "4405eb6f1007c723ebbcbc0f56f6f0062f298afa": ("confirmed-current-boundary", "The title explicitly concerns sequential modeling for speaker embeddings and speaker verification. Title-only evidence supports speaker-verification membership.", "people-variation-and-health", "identity-and-life-stage", "speaker-verification"),
    "441388b56ae6e0904f2efb5711fae7c4feced9e5": ("rejected-out-of-scope", "The title concerns a real-time codec for general audio transmission but does not establish human speech or spoken-language evidence. With title-only evidence, speech deployment membership is not supported.", None, None, None),
    "44add82e8532ca50ed5d5e2904abaa5e2e757016": ("confirmed-current-boundary", "The title explicitly concerns speech emotion recognition and speaker/listener personality interactions. Title-only evidence supports paralinguistic-state membership.", "meaning-and-interaction", "prosody-and-paralinguistics", "paralinguistic-state"),
    "4503994cf38fd02246697453c852a414fa53ffaf": ("confirmed-current-boundary", "The title explicitly concerns medical automatic speech recognition with domain-specific adaptation. Title-only evidence supports domain and context biasing.", "recognition-and-alignment", "context-and-open-vocabulary", "domain-and-context-biasing"),
    "467e67ae21f49486c193e2e6302bc3550ff35186": ("reassigned-to-neighbor", "The title explicitly concerns early Alzheimer's detection from speech, using cross-lingual and few-shot transfer. The clinical speech task is more direct than few-shot adaptation alone; title-only evidence supports a clinical speech marker.", "people-variation-and-health", "clinical-markers", "clinical-speech-marker"),
    "470de39094a921d74e222c0561ee33d97f2186c6": ("reassigned-to-neighbor", "The title explicitly concerns stress prediction in clinical patient-physician conversations. Stress is a paralinguistic state; title-only evidence supports paralinguistic-state more directly than a clinical marker.", "meaning-and-interaction", "prosody-and-paralinguistics", "paralinguistic-state"),
    "47d2baf4376dc54a7adb8073904be2d7fe75d3c6": ("rejected-out-of-scope", "The title concerns auditory cognition in general audio-language models but does not establish a human-speech or spoken-language task. With title-only evidence, referential grounding membership is not supported.", None, None, None),
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
