#!/usr/bin/env python3
"""Record the next eight evidence-bounded taxonomy adjudications."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "parvathala25_interspeech": (
        "confirmed-current-boundary",
        "The abstract replaces a costly enhancement encoder block with bispectral features that capture frequency and phase information and reports lower multiply-accumulate cost. The evidence supports speech-prior denoising, bounded by the CMGAN/MP-SENet integrations and DNS/VoiceBank evaluations.",
        ["title", "abstract"], "listening-and-separation", "noise-enhancement", "speech-prior-denoising",
    ),
    "parvathala25b_interspeech": (
        "confirmed-current-boundary",
        "The abstract builds a multi-sampling-frequency speech-enhancement model that handles resolution changes and extracts compact submodels while retaining performance. The evidence supports speech-prior denoising, bounded by the MSFNet architecture and reported parameter/MAC comparisons.",
        ["title", "abstract"], "listening-and-separation", "noise-enhancement", "speech-prior-denoising",
    ),
    "parvathala25c_interspeech": (
        "reassigned-to-neighbor",
        "The abstract dynamically skips enhancement layers according to signal conditions and reports large MAC reductions, making computation the governing pressure. The evidence supports latency and resource budget, bounded by the gating levels, enhancement task, and reported reductions.",
        ["title", "abstract"], "evaluation-deployment-and-consequence", "deployment-cost", "latency-and-resource",
    ),
    "patapati25_interspeech": (
        "confirmed-current-boundary",
        "The abstract coordinates speech, visual signals, dialogue, gestures, and backchannel animations in a real-time embodied agent. The evidence supports interactional feedback, bounded by the modular GenECA framework and real-time multimodal interaction setting.",
        ["title", "abstract"], "meaning-and-interaction", "grounding-and-action", "interactional-feedback",
    ),
    "pathak25_interspeech": (
        "reassigned-to-neighbor",
        "The abstract uses related languages, shared phone representations, and target-language phonotactics to synthesize speech for resource-poor Indian languages. The governing boundary is cross-lingual transfer, not zero-shot speaker-voice generation, because the transfer is across languages and scripts.",
        ["title", "abstract"], "languages-accents-and-resources", "crosslingual-structure", "crosslingual-transfer",
    ),
    "patman25_interspeech": (
        "confirmed-current-boundary",
        "The abstract measures source-related acoustic parameters in normal and breathy speech and tests their suitability across female and male speakers. The evidence supports periodic source, bounded by the PASR recordings, listed parameters, and mixed-effects analysis.",
        ["title", "abstract"], "sound-and-production", "source-generation", "periodic-source",
    ),
    "pei25_interspeech": (
        "confirmed-current-boundary",
        "The abstract presents online raw-waveform speech enhancement and explicitly compares PESQ, parameters, MACs, latency, and fidelity in constrained conditions. The evidence supports latency and resource budget, bounded by aTENNuate and the VoiceBank/DEMAND and DNS1 tests.",
        ["title", "abstract"], "evaluation-deployment-and-consequence", "deployment-cost", "latency-and-resource",
    ),
    "peirolilja25_interspeech": (
        "confirmed-current-boundary",
        "The abstract builds Catalan spoken-language understanding for voice commands in a video game, combining ASR with intent classification and user feedback. The evidence supports intent in context, bounded by the game domain, synthetic-transcription augmentation, and in-game evaluation.",
        ["title", "abstract"], "meaning-and-interaction", "intent-and-dialogue-state", "intent-in-context",
    ),
}


def main():
    payload = json.loads(QUEUE.read_text())
    rows = {r["paper_id"]: r for r in payload["rows"]}
    for pid, (decision, note, sections, theme, subtheme, concept) in DECISIONS.items():
        row = rows[pid]
        if row["taxonomy_review_state"] == "taxonomy-adjudicated":
            raise SystemExit(f"already adjudicated: {pid}")
        row.update({
            "taxonomy_review_state": "taxonomy-adjudicated",
            "final_decision": decision,
            "reviewer_note": note,
            "reviewed_sections": sections,
            "final_theme_id": theme,
            "final_subtheme_id": subtheme,
            "final_concept_id": concept,
        })
    adjudicated = sum(r["taxonomy_review_state"] == "taxonomy-adjudicated" for r in rows.values())
    payload["adjudicated_count"] = adjudicated
    payload["open_count"] = len(rows) - adjudicated
    decisions = sorted({r.get("final_decision") for r in rows.values() if r["taxonomy_review_state"] == "taxonomy-adjudicated"})
    payload["decision_counts"] = {d: sum(r.get("final_decision") == d for r in rows.values() if r["taxonomy_review_state"] == "taxonomy-adjudicated") for d in decisions}
    QUEUE.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({"batch": len(DECISIONS), "adjudicated": adjudicated, "open": payload["open_count"]}))


if __name__ == "__main__": main()
