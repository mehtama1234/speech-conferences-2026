#!/usr/bin/env python3
"""Record the next eight evidence-bounded taxonomy adjudications."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "zheng25_interspeech": (
        "confirmed-current-boundary",
        "The challenge evaluates ASR for people with speech disabilities using a large shared corpus and both transcription error and semantic preservation measures. The evidence supports accessibility-fit, bounded by 400+ hours, 500+ participants, 22 teams, remote evaluation, WER/SemScore, and the reported baseline comparisons.",
        ["title", "abstract"], "people-variation-and-health", "human-centered-accessibility", "accessibility-fit",
    ),
    "zheng25b_interspeech": (
        "confirmed-current-boundary",
        "The abstract separates speech properties into dedicated frame-level codes and reconstructs them with fewer tokens, targeting efficient quantization without losing speech structure. The evidence supports sampling-and-quantization, bounded by FreeCodec, disentangled encoders/decoders, 57 tokens, reconstruction/disentanglement tests, and subjective/objective comparisons.",
        ["title", "abstract"], "sound-and-production", "time-frequency-measurement", "sampling-and-quantization",
    ),
    "zheng25c_interspeech": (
        "confirmed-current-boundary",
        "The abstract uses video and language-model analysis to decide dubbing type, speaker attributes, emotion, and synchronization before generating the dubbed speech. The evidence supports text-to-speech-planning, bounded by MM-MovieDubber, multimodal inputs, dialogue/narration/monologue, age/gender/emotion, dataset construction, and reported quality measures.",
        ["title", "abstract"], "voice-generation-and-control", "content-planning", "text-to-speech-planning",
    ),
    "zheng25d_interspeech": (
        "confirmed-current-boundary",
        "The abstract removes redundant flow-matching sampling steps from TTS without retraining the model, reducing generation time while retaining comparable output quality. The evidence supports interactive-latency, bounded by EPSS/Fast F5-TTS, seven-step generation, RTF, RTX 3090 evaluation, F5-TTS/E2-TTS transfer, and reported speed/quality results.",
        ["title", "abstract"], "voice-generation-and-control", "expression-and-interactive-control", "interactive-latency",
    ),
    "zhengjie25_interspeech": (
        "confirmed-current-boundary",
        "The abstract makes Chinese ASR predict Pinyin alongside characters so phonetic relations and homophones can be corrected before the language model refines the transcript. The evidence supports pronunciation-variation, bounded by PYG-ASR, acoustic-to-Pinyin/text mapping, AISHELL-1, context biasing, and CER reductions.",
        ["title", "abstract"], "recognition-and-alignment", "pronunciation-and-variation", "pronunciation-variation",
    ),
    "zhong25_interspeech": (
        "confirmed-current-boundary",
        "The abstract applies regularized federated learning to dysarthric and elderly speech so data remain distributed while speaker heterogeneity, scarcity, and imbalance are addressed. The evidence supports dysarthria-and-atypical-speech, bounded by UASpeech and DementiaBank Pitt, three regularization levels, FedAvg comparison, communication frequency, and WER results.",
        ["title", "abstract"], "people-variation-and-health", "atypical-and-assistive-speech", "dysarthria-and-atypical-speech",
    ),
    "zhong25b_interspeech": (
        "confirmed-current-boundary",
        "The abstract tests whether turn-taking speech collected for non-diagnostic purposes can support Parkinson's classification and checks how dataset composition changes generalization. The evidence supports clinical-speech-marker, bounded by TT and PC-GITA, cross-dataset evaluation, gender/status balance, concatenation, and fold/speaker variability.",
        ["title", "abstract"], "people-variation-and-health", "clinical-markers", "clinical-speech-marker",
    ),
    "zhong25c_interspeech": (
        "confirmed-current-boundary",
        "The abstract builds a pairwise listener test and pronunciation-based objective measures for judging whether synthesized speech carries the intended accent, while warning that WER can miss underrepresented accents. The evidence supports accent-robustness, bounded by XAB evaluation, listener transcription/highlighting, formants/phonetic posteriors, reliability screening, and metric limitations.",
        ["title", "abstract"], "languages-accents-and-resources", "accent-dialect-and-cultural-meaning", "accent-robustness",
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


if __name__ == "__main__":
    main()
