#!/usr/bin/env python3
"""Record the next eight evidence-bounded taxonomy adjudications."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "li25d_interspeech": ("confirmed-current-boundary", "The abstract develops and evaluates a single- and multi-channel speech-enhancement model and reports a large computation reduction at comparable quality. The evidence supports speech-prior denoising, bounded by the stated enhancement tasks and compute budgets.", ["title", "abstract"], "listening-and-separation", "noise-enhancement", "speech-prior-denoising"),
    "li25da_interspeech": ("confirmed-current-boundary", "The abstract introduces a real conversational dataset specifically for target-speaker extraction and shows degradation from synthetic to real mixtures. The evidence supports target-conditioned separation, bounded by the BASE and PRIMARY subsets.", ["title", "abstract"], "listening-and-separation", "source-separation", "target-conditioned-separation"),
    "li25e_interspeech": ("confirmed-current-boundary", "The abstract develops a low-frame-rate neural codec for speech generation and evaluates the tradeoff between semantic content, waveform quality, and coding efficiency. The evidence supports waveform synthesis and codec generation, bounded by the reported codec and speech-generation tests.", ["title", "abstract"], "voice-generation-and-control", "waveform-and-codec-generation", "waveform-synthesis"),
    "li25f_interspeech": ("confirmed-current-boundary", "The abstract uses voice conversion to synthesize dysarthric-like speech for low-resource multilingual ASR and evaluates recognition and generated-speech quality. The evidence supports atypical articulation and dysarthria, with the converted data serving augmentation rather than replacing clinical speech evidence.", ["title", "abstract"], "people-variation-and-health", "atypical-and-assistive-speech", "dysarthria-and-atypical-speech"),
    "li25g_interspeech": ("reassigned-to-neighbor", "The abstract watermarks zero-shot voice-conversion outputs so unauthorized cloning can be traced or resisted. The governing consequence is synthetic-voice misuse and deepfake provenance, rather than privacy protection alone.", ["title", "abstract"], "evaluation-deployment-and-consequence", "privacy-and-security", "spoofing-and-deepfake"),
    "li25h_interspeech": ("confirmed-current-boundary", "The abstract jointly evaluates speaker verification and anti-spoofing under cross-domain and cross-synthesis conditions and models uncertainty from domain shift. The evidence supports spoofing and synthetic-voice misuse, bounded by the tested ASV and anti-spoofing protocols.", ["title", "abstract"], "evaluation-deployment-and-consequence", "privacy-and-security", "spoofing-and-deepfake"),
    "li25i_interspeech": ("confirmed-current-boundary", "The abstract controls emphasis and emotion jointly in TTS and evaluates whether emphasis remains clear across emotional conditions. The evidence supports style and emotion control, bounded by the pseudo-labels and tested synthesis settings.", ["title", "abstract"], "voice-generation-and-control", "expression-and-interactive-control", "style-and-emotion-control"),
    "li25j_interspeech": ("confirmed-current-boundary", "The abstract decodes imagined, intended, and spoken speech from EEG for a non-invasive communication interface aimed at people with speech impairments. The evidence supports augmentative communication, bounded by the four-vowel and EEG-channel experiments.", ["title", "abstract"], "people-variation-and-health", "atypical-and-assistive-speech", "augmentative-communication"),
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
