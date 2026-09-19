#!/usr/bin/env python3
"""Record the next eight evidence-bounded taxonomy adjudications."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "vukovic25_interspeech": (
        "confirmed-current-boundary",
        "The full paper presents a platform for storing, querying, and aligning multimodal corpora with synchronized audio, video, text, gesture, and annotation layers. The evidence supports speech-data-collection, bounded by LCP, DQD, audiovisual corpus workflows, and the demonstrated interfaces.",
        ["title", "abstract", "full_paper"], "languages-accents-and-resources", "data-creation", "speech-data-collection",
    ),
    "vurma25_interspeech": (
        "confirmed-current-boundary",
        "The abstract tests how voiced-consonant duration affects recognition of sung and spoken CV/VC segments across pitch, reverberation, accompaniment, and noise. The evidence supports articulatory-coordination, bounded by 42 listeners, four consonants, two singers, duration manipulation, and recognition results.",
        ["title", "abstract"], "sound-and-production", "articulatory-dynamics", "articulatory-coordination",
    ),
    "wagner25_interspeech": (
        "confirmed-current-boundary",
        "The abstract personalizes dysarthric ASR with speaker codes, parameter-efficient adaptation, synthetic dysarthric speech, and LLM-generated transcript prompts. The evidence supports dysarthria-and-atypical-speech, bounded by Parler-TTS, x-vectors, AdaLoRA comparisons, wav2vec features, and reported WER changes.",
        ["title", "abstract"], "people-variation-and-health", "atypical-and-assistive-speech", "dysarthria-and-atypical-speech",
    ),
    "waibel25_interspeech": (
        "confirmed-current-boundary",
        "The abstract traces speech technology from recognition through translation, dialogue, multimodal systems, and dubbing as tools for reducing language barriers. The evidence supports accessibility-fit, bounded by the invited overview's historical examples and its claim about speech science, learned representations, and global communication.",
        ["title", "abstract"], "people-variation-and-health", "human-centered-accessibility", "accessibility-fit",
    ),
    "wakayama25_interspeech": (
        "confirmed-current-boundary",
        "The abstract demonstrates real-time target sound extraction from live mixtures using a causal, knowledge-distilled SoundBeam model. The evidence supports target-conditioned-separation, bounded by selected sound-event classes, laptop real-time operation, causal/non-causal teacher setup, and Waveformer comparison.",
        ["title", "abstract"], "listening-and-separation", "source-separation", "target-conditioned-separation",
    ),
    "wallbridge25_interspeech": (
        "confirmed-current-boundary",
        "The abstract tests whether self-supervised acoustic representations preserve prosodic structure beyond lexical content and across different time scales. The evidence supports prosodic-meaning, bounded by the Masked Prosody Model, word-boundary and emotion labels, pitch/energy/voice-activity baselines, and probing gains.",
        ["title", "abstract"], "meaning-and-interaction", "prosody-and-paralinguistics", "prosodic-meaning",
    ),
    "wan25_interspeech": (
        "confirmed-current-boundary",
        "The full paper proposes a streaming neural codec in the compressed spectral domain using compact CNN/RNN layers and measures computation, parameters, bitrate, and representation quality. The evidence supports latency-and-resource, bounded by SpecTokenizer, 4 kbps operation, the lightweight comparison, and stated efficiency ratios.",
        ["title", "abstract", "full_paper"], "evaluation-deployment-and-consequence", "deployment-cost", "latency-and-resource",
    ),
    "wang25_interspeech": (
        "confirmed-current-boundary",
        "The abstract creates a continuous benchmark for open Arabic ASR across multiple dialects and compares generalization, speaker adaptation, efficiency, and memory. The evidence supports dialect-and-variety, bounded by the multi-dialect datasets, open-source models, leaderboard design, and listed evaluation dimensions.",
        ["title", "abstract"], "languages-accents-and-resources", "accent-dialect-and-cultural-meaning", "dialect-and-variety",
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
