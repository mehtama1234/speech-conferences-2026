#!/usr/bin/env python3
"""Record the next eight evidence-bounded taxonomy adjudications."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "kunze25_interspeech": ("confirmed-current-boundary", "The abstract studies voice-type classification in naturalistic child-wearable recordings and explicitly identifies child data quantity, relevance, and permissions as limiting factors. The evidence supports age and developmental speech, without claiming a universal child voice classifier.", ["title", "abstract"], "people-variation-and-health", "identity-and-life-stage", "age-and-development"),
    "kuparinen25_interspeech": ("confirmed-current-boundary", "The abstract defines automatic dialectal transcription and evaluates Finnish and Norwegian variation at two transcription precisions. The evidence supports dialect and variety, bounded by the languages, dialects, and transcription conventions tested.", ["title", "abstract"], "languages-accents-and-resources", "accent-dialect-and-cultural-meaning", "dialect-and-variety"),
    "kutsakov25_interspeech": ("confirmed-current-boundary", "The abstract trains and releases a self-supervised speech representation and evaluates its transfer to Russian speech recognition under full-context and streaming conditions. The evidence supports self-supervised speech units, without making the reported model universal.", ["title", "abstract"], "recognition-and-alignment", "acoustic-unit-learning", "self-supervised-speech-units"),
    "kwok25_interspeech": ("confirmed-current-boundary", "The abstract evaluates audio deepfake detectors across many synthesizers and diverse bona fide speech conditions and proposes a more balanced testing protocol. The evidence supports spoofing and synthetic-voice misuse, with the benchmark design defining the claim boundary.", ["title", "abstract"], "evaluation-deployment-and-consequence", "privacy-and-security", "spoofing-and-deepfake"),
    "kwok25b_interspeech": ("confirmed-current-boundary", "The abstract trains contextual-biasing modules to recognize rare words in synthetic speech and uses a keyword-aware loss to improve decoding. The evidence supports domain and context biasing, bounded by the synthetic-data and NSC evaluation conditions.", ["title", "abstract"], "recognition-and-alignment", "context-and-open-vocabulary", "domain-and-context-biasing"),
    "kwok25c_interspeech": ("reassigned-to-neighbor", "The abstract uses trie look-ahead specifically to bias ASR toward rare words during contextual decoding. The governing operation is domain and context biasing, rather than open-vocabulary recognition without a supplied keyword context.", ["title", "abstract"], "recognition-and-alignment", "context-and-open-vocabulary", "domain-and-context-biasing"),
    "kwon25_interspeech": ("confirmed-current-boundary", "The abstract adapts text-to-speech to a new language with a single-speaker dataset and parameter-efficient adapters under explicit compute constraints. The evidence supports few-shot adaptation, bounded by the language and speaker settings tested.", ["title", "abstract"], "languages-accents-and-resources", "low-resource-learning", "few-shot-adaptation"),
    "kwon25b_interspeech": ("reassigned-to-neighbor", "The abstract studies structured speaker differences in phonetic realizations across Korean phonological and morphological contexts. The central evidence is systematic speaker variation, not a model of articulatory movement or gesture timing.", ["title", "abstract"], "people-variation-and-health", "identity-and-life-stage", "style-and-state-variation"),
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
