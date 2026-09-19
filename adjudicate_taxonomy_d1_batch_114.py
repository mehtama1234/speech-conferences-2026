#!/usr/bin/env python3
"""Record the next eight evidence-bounded taxonomy adjudications."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "kando25_interspeech": ("confirmed-current-boundary", "The title and abstract explicitly study segmentation width and cluster size in discrete speech tokenization and relate them to spoken-language understanding. The evidence supports learned speech units, without proving one tokenization scheme universally.", ["title", "abstract"], "recognition-and-alignment", "acoustic-unit-learning", "self-supervised-speech-units"),
    "kaneko25_interspeech": ("confirmed-current-boundary", "The title and abstract explicitly distill iterative diffusion voice conversion into a one-step model and report speed and similarity. The evidence supports voice conversion, without proving equal quality for every speaker.", ["title", "abstract"], "voice-generation-and-control", "identity-and-conversion", "voice-conversion"),
    "kaneko25b_interspeech": ("confirmed-current-boundary", "The title and abstract explicitly use vocoder-projected features to discriminate waveform detail in TTS and voice conversion while reducing training cost. The evidence supports waveform synthesis, without proving all acoustic detail is preserved.", ["title", "abstract"], "voice-generation-and-control", "waveform-and-codec-generation", "neural-vocoder"),
    "kang25_interspeech": ("confirmed-current-boundary", "The title and abstract explicitly make a frozen language model respond to expressive speech by transmitting linguistic and paralinguistic information from an encoder. The evidence supports paralinguistic state, without proving general empathetic understanding.", ["title", "abstract"], "meaning-and-interaction", "prosody-and-paralinguistics", "paralinguistic-state"),
    "kang25c_interspeech": ("reassigned-to-neighbor", "The title and abstract explicitly generate a voice matched to a face and control paralinguistic features in text-driven talking-face generation. The governing speech concept is prosody control, not referential grounding.", ["title", "abstract"], "voice-generation-and-control", "expression-and-interactive-control", "prosody-control"),
    "kang25d_interspeech": ("confirmed-current-boundary", "The title and abstract explicitly address within-class heterogeneity and cognitive-score variation in Alzheimer's speech detection. The evidence supports a clinical speech marker, without establishing diagnosis or clinical deployment.", ["title", "abstract"], "people-variation-and-health", "clinical-markers", "clinical-speech-marker"),
    "kano25_interspeech": ("confirmed-current-boundary", "The title and abstract explicitly summarize long spoken input by selecting important content before generating an abstract summary. The evidence supports referential grounding of speech content, without proving preservation of every conversational implication.", ["title", "abstract"], "meaning-and-interaction", "grounding-and-action", "referential-grounding"),
    "karimov25_interspeech": ("confirmed-current-boundary", "The title and abstract explicitly obfuscate speaker identity with universal adversarial patches while measuring audio quality, recognition quality, and transfer across biometric models. The evidence supports voice privacy, without proving protection against all attackers.", ["title", "abstract"], "evaluation-deployment-and-consequence", "privacy-and-security", "voice-privacy"),
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
