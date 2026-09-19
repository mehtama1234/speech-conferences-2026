#!/usr/bin/env python3
"""Record the twelfth small, full-paper taxonomy adjudication batch."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "goebiowska25_interspeech": ("confirmed-current-boundary", "EmoSpeechAuth asks whether identity evidence survives emotion-dependent voice changes. The emotion labels, enrollment conditions, and thresholds limit the speaker-verification claim.", "people-variation-and-health", "identity-and-life-stage", "speaker-verification"),
    "goswami25_interspeech": ("confirmed-current-boundary", "FUSE combines waveform, codec-token, speaker, phoneme, and perceptual losses to restore damaged speech across several distortions. Its blind challenge scores and unseen-language setting bound the result.", "listening-and-separation", "noise-enhancement", "speech-prior-denoising"),
    "grinberg25_interspeech": ("reassigned-to-neighbor", "The diffusion model is trained to expose artifact regions that explain why vocoded speech is judged fake. Its central object is evidence of synthetic voice misuse, while time-frequency differences are the explanatory mechanism.", "evaluation-deployment-and-consequence", "privacy-and-security", "spoofing-and-deepfake"),
    "griot25_interspeech": ("confirmed-current-boundary", "The system separates lexical validation from speaker evidence and tests identity under text-dependent and text-independent conditions. Dataset content and thresholds bound the verification claim.", "people-variation-and-health", "identity-and-life-stage", "speaker-verification"),
    "guo25b_interspeech": ("confirmed-current-boundary", "Broadband high-frequency cues improve phoneme recognition under masking, especially at low target-to-masker ratios. The cochleagram probe and selected maskers bound the conclusion.", "sound-and-production", "time-frequency-measurement", "multi-resolution-signal"),
    "hannan25_interspeech": ("confirmed-current-boundary", "PAEFF tests whether a face and voice belong together by aligning and fusing their identity embeddings. It is identity verification across modalities, bounded by VoxCeleb and its split protocol.", "people-variation-and-health", "identity-and-life-stage", "speaker-verification"),
    "harmsen25_interspeech": ("confirmed-current-boundary", "Automatic measures of child reading fluency are compared with human-derived accuracy, pacing, and phrasing measures. The work concerns whether the tool fits the accessibility task, not diagnosis or intervention benefit.", "people-variation-and-health", "human-centered-accessibility", "accessibility-fit"),
    "he25_interspeech": ("confirmed-current-boundary", "Contextual multi-talker ASR uses speaker-change tokens and a filtered rare-word list to resolve meeting speech. The bias list and serialization assumptions bound the context-biasing result.", "recognition-and-alignment", "context-and-open-vocabulary", "domain-and-context-biasing"),
}

def main():
    payload = json.loads(QUEUE.read_text())
    rows = {r["paper_id"]: r for r in payload["rows"]}
    for pid, (decision, note, theme, subtheme, concept) in DECISIONS.items():
        row = rows[pid]
        if row["taxonomy_review_state"] == "taxonomy-adjudicated":
            raise SystemExit(f"already adjudicated: {pid}")
        row.update({"taxonomy_review_state": "taxonomy-adjudicated", "final_decision": decision, "reviewer_note": note, "reviewed_sections": ["title", "abstract", "method", "experiments", "results", "limits"], "final_theme_id": theme, "final_subtheme_id": subtheme, "final_concept_id": concept})
    payload["adjudicated_count"] = sum(r["taxonomy_review_state"] == "taxonomy-adjudicated" for r in rows.values())
    payload["open_count"] = len(rows) - payload["adjudicated_count"]
    payload["decision_counts"] = {d: sum(r.get("final_decision") == d for r in rows.values() if r["taxonomy_review_state"] == "taxonomy-adjudicated") for d in sorted({r.get("final_decision") for r in rows.values() if r["taxonomy_review_state"] == "taxonomy-adjudicated"})}
    QUEUE.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({"batch": len(DECISIONS), "adjudicated": payload["adjudicated_count"], "open": payload["open_count"]}))

if __name__ == "__main__":
    main()
