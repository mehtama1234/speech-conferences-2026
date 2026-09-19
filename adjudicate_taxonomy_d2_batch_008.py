#!/usr/bin/env python3
"""Record the eighth abstract-bounded D2 taxonomy adjudication batch."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "2fa79695d2ba5fcdaee3664a69a18031748f4242": ("rejected-out-of-scope", "The abstract concerns likelihood evaluation in music language models and corrupted music, not speech or spoken-language evidence.", None, None, None),
    "34256c20127c51b3aed13569485a586d62525c68": ("confirmed-current-boundary", "The abstract explicitly concerns a universal speech-enhancement challenge with speech-quality assessment, diverse distortions, and evaluation protocols. D2 supports metric-and-human-target membership, while individual system mechanisms remain unreviewed.", "evaluation-deployment-and-consequence", "metric-and-human-targets", "quality-and-naturalness"),
    "3437b5e47c7124dc574bf3659df037536f5444d4": ("rejected-out-of-scope", "The abstract concerns general audio question answering and unanswerability, without establishing a speech or spoken-language object.", None, None, None),
    "344fe6791f8fa625dfbeeb8cc65557291e6463c4": ("confirmed-current-boundary", "The abstract explicitly concerns speech-derived acoustic features for coronary-artery-disease detection. D2 supports a clinical speech-marker assignment without establishing medical validity.", "people-variation-and-health", "clinical-markers", "clinical-speech-marker"),
    "353486bfb0c6f393f228880e50e484e9c9b12b45": ("reassigned-to-neighbor", "The abstract detects gradual changes in synthetic speaker identity within an utterance using segment embeddings and human-validated labels. The central object is speaker identity consistency, not generic style variation.", "voice-generation-and-control", "identity-and-conversion", "speaker-identity"),
    "38465bde406fcab2d6f8a90f1ea32803bd3f42cc": ("confirmed-current-boundary", "The abstract explicitly concerns voice conversion for electro-laryngeal speech rehabilitation and evaluates intelligibility and naturalness. The atypical-speech setting is the boundary of the assistive claim.", "people-variation-and-health", "atypical-and-assistive-speech", "dysarthria-and-atypical-speech"),
    "38c8b23652ecba9863ce53147ed6aaa1ec86b668": ("confirmed-current-boundary", "The abstract explicitly concerns association of faces and voices belonging to the same speaker through multimodal identity embeddings. D2 supports speaker-verification membership.", "people-variation-and-health", "identity-and-life-stage", "speaker-verification"),
    "38f6bf21c738d202e87685df5ca9761a7c8b5476": ("reassigned-to-neighbor", "The abstract concerns text-to-speech generation, text-audio alignment, and accelerated denoising inference. The semantic aligner supports generation, but the paper's main object is the TTS waveform/acoustic generator rather than text planning.", "voice-generation-and-control", "waveform-and-codec-generation", "neural-vocoder"),
}

def main():
    payload = json.loads(QUEUE.read_text())
    rows = {r["paper_id"]: r for r in payload["rows"]}
    for pid, (decision, note, theme, subtheme, concept) in DECISIONS.items():
        row = rows[pid]
        if row["taxonomy_review_state"] == "taxonomy-adjudicated":
            raise SystemExit(f"already adjudicated: {pid}")
        row.update({"taxonomy_review_state": "taxonomy-adjudicated", "final_decision": decision, "reviewer_note": note, "reviewed_sections": ["title", "abstract"], "final_theme_id": theme, "final_subtheme_id": subtheme, "final_concept_id": concept})
    payload["adjudicated_count"] = sum(r["taxonomy_review_state"] == "taxonomy-adjudicated" for r in rows.values())
    payload["open_count"] = len(rows) - payload["adjudicated_count"]
    payload["decision_counts"] = {d: sum(r.get("final_decision") == d for r in rows.values() if r["taxonomy_review_state"] == "taxonomy-adjudicated") for d in sorted({r.get("final_decision") for r in rows.values() if r["taxonomy_review_state"] == "taxonomy-adjudicated"})}
    QUEUE.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({"batch": len(DECISIONS), "adjudicated": payload["adjudicated_count"], "open": payload["open_count"]}))

if __name__ == "__main__":
    main()
