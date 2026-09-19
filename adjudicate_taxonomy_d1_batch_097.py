#!/usr/bin/env python3
"""Record the next eight evidence-bounded taxonomy adjudications."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "gaznepoglu25_interspeech": ("reassigned-to-neighbor", "The title and abstract explicitly attack voice-privacy systems using linguistic content to recover speaker identity. This is voice privacy and security evaluation, not ordinary speaker verification enrollment.", ["title", "abstract"], "evaluation-deployment-and-consequence", "privacy-and-security", "voice-privacy"),
    "gebauer25_interspeech": ("confirmed-current-boundary", "The title and abstract explicitly detect grammatical errors in children's spontaneous speech as a possible indicator of developmental language disorder. The evidence supports a clinical speech marker, without establishing diagnosis.", ["title", "abstract"], "people-variation-and-health", "clinical-markers", "clinical-speech-marker"),
    "geng25_interspeech": ("reassigned-to-neighbor", "The title and abstract explicitly build a perception-based L2 intelligibility indicator and compare it with ASR measures and native listener judgments. This is word error versus understanding, not speech denoising.", ["title", "abstract"], "evaluation-deployment-and-consequence", "metric-and-human-targets", "word-error-versus-understanding"),
    "geng25b_interspeech": ("reassigned-to-neighbor", "The title and abstract explicitly present EEG-based voice conversion to a target speaker and identify assistive communication as an application. The central speech operation is voice conversion, not general augmentative communication.", ["title", "abstract"], "voice-generation-and-control", "identity-and-conversion", "voice-conversion"),
    "geng25c_interspeech": ("reassigned-to-neighbor", "The title and abstract explicitly evaluate speech foundation models for ASR in a low-resource Indigenous language and test synthesized data and cross-lingual transfer. This is scarce-data adaptation, not pronunciation variation alone.", ["title", "abstract"], "languages-accents-and-resources", "low-resource-learning", "few-shot-adaptation"),
    "getman25_interspeech": ("confirmed-current-boundary", "The title and abstract explicitly train and interpret a large self-supervised speech foundation model and assess learned representations for downstream ASR. The evidence supports learned speech units, without proving language-independent representations.", ["title", "abstract"], "recognition-and-alignment", "acoustic-unit-learning", "self-supervised-speech-units"),
    "ghosh25_interspeech": ("confirmed-current-boundary", "The title and abstract explicitly segment dysfluency events and preserve frame-level onset boundaries for stuttering analysis. The evidence supports disfluency and event preservation, without proving therapy benefit.", ["title", "abstract"], "recognition-and-alignment", "boundaries-and-alignment", "disfluency-preservation"),
    "gimenogomez25_interspeech": ("confirmed-current-boundary", "The title and abstract explicitly use speech to identify Parkinson's medication states and compare clinical assessment tasks. The evidence supports a clinical speech marker, without establishing clinical deployment validity.", ["title", "abstract"], "people-variation-and-health", "clinical-markers", "clinical-speech-marker"),
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
