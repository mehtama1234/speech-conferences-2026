#!/usr/bin/env python3
"""Record the next eight evidence-bounded taxonomy adjudications."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "gallego25_interspeech": ("confirmed-current-boundary", "The title and abstract explicitly use phoneme representations to improve speech-to-text translation across low-resource and zero-resource languages. The evidence supports cross-lingual transfer, without proving universal transfer.", ["title", "abstract"], "languages-accents-and-resources", "crosslingual-structure", "crosslingual-transfer"),
    "gan25_interspeech": ("reassigned-to-neighbor", "The title and abstract explicitly distill relations for speaker verification and compare speaker embeddings. This is identity verification, not target-conditioned separation of sound sources.", ["title", "abstract"], "people-variation-and-health", "identity-and-life-stage", "speaker-verification"),
    "gan25b_interspeech": ("confirmed-current-boundary", "The title and abstract explicitly compress speech by exploiting synonymous representations while measuring rate and perceptual quality. The evidence supports a deployment resource budget, without proving preservation of every linguistic distinction.", ["title", "abstract"], "evaluation-deployment-and-consequence", "deployment-cost", "latency-and-resource"),
    "gao25_interspeech": ("confirmed-current-boundary", "The title and abstract explicitly present a low-complexity speech enhancement system that denoises speech under computational limits. The evidence supports speech-prior denoising, without establishing all-device generalization.", ["title", "abstract"], "listening-and-separation", "noise-enhancement", "speech-prior-denoising"),
    "gao25d_interspeech": ("confirmed-current-boundary", "The title and abstract explicitly optimize an LLM-based TTS system with rewards for pronunciation, emotion, and quality control. The evidence supports style and emotion control, without proving reliable zero-shot control in every voice.", ["title", "abstract"], "voice-generation-and-control", "expression-and-interactive-control", "style-and-emotion-control"),
    "gao25e_interspeech": ("confirmed-current-boundary", "The title and abstract explicitly use spontaneous speech to assess suicide risk in adolescents. The evidence supports a clinical speech marker, without establishing clinical validity or safe intervention.", ["title", "abstract"], "people-variation-and-health", "clinical-markers", "clinical-speech-marker"),
    "gao25g_interspeech": ("confirmed-current-boundary", "The title and abstract explicitly align audio-visual speaker diarization with speech recognition in meetings and report diarization and recognition tasks. The evidence supports temporal alignment, without proving robustness beyond the challenge setting.", ["title", "abstract"], "recognition-and-alignment", "boundaries-and-alignment", "alignment"),
    "gaudrain25_interspeech": ("confirmed-current-boundary", "The title and abstract explicitly design controlled naturalistic speech stimuli for studying hearing-related neural coding across study constraints. The evidence supports accessibility fit, without establishing a clinical hearing test.", ["title", "abstract"], "people-variation-and-health", "human-centered-accessibility", "accessibility-fit"),
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
