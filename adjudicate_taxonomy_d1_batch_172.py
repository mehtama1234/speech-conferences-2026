#!/usr/bin/env python3
"""Record the next eight evidence-bounded taxonomy adjudications."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "su25_interspeech": (
        "confirmed-current-boundary",
        "The abstract enhances esophageal speech for people after laryngectomy using mask, ratio-mask, and voice-conversion methods trained with ASR loss. The evidence supports dysarthria-and-atypical-speech, bounded by Mandarin esophageal speech, the three enhancement methods, ASR and human evaluations, naturalness ratings, and voicing measures.",
        ["title", "abstract"], "people-variation-and-health", "atypical-and-assistive-speech", "dysarthria-and-atypical-speech",
    ),
    "su25b_interspeech": (
        "confirmed-current-boundary",
        "The abstract aligns audio embeddings with text for LLM-based ASR using unpaired audio-text data, then evaluates the aligned encoder in recognition. The evidence supports acoustic-to-token, bounded by the cross-modality pretraining method, unpaired-data setting, and reported comparison with audio-only pretraining.",
        ["title", "abstract"], "recognition-and-alignment", "acoustic-unit-learning", "acoustic-to-token",
    ),
    "su25c_interspeech": (
        "confirmed-current-boundary",
        "The abstract converts voices between speakers while controlling emotion, separating utterance-level and frame-level emotion cues from speaker and content. The evidence supports style-and-emotion-control, bounded by the any-to-any diffusion model, disentanglement losses, UTMOS result, and emotion-recognition test.",
        ["title", "abstract"], "voice-generation-and-control", "expression-and-interactive-control", "style-and-emotion-control",
    ),
    "subramanian25_interspeech": (
        "confirmed-current-boundary",
        "The abstract translates speech for dubbing while choosing output lengths that keep target audio synchronized with source video and speech. The evidence supports crosslingual-transfer, bounded by the phoneme-based LSST model, length tags, one-pass beam search, Spanish and Korean tests, and BLEU/MOS results.",
        ["title", "abstract"], "languages-accents-and-resources", "crosslingual-structure", "crosslingual-transfer",
    ),
    "subramanian25b_interspeech": (
        "confirmed-current-boundary",
        "The abstract recognizes several overlapping speakers by combining continuous separation with serialized output training and choosing streaming or offline architectures. The evidence supports target-conditioned-separation, bounded by the multi-talker ASR setting, CSS front end, SOT variants, latency/accuracy tradeoff, and stated captioning uses.",
        ["title", "abstract"], "listening-and-separation", "source-separation", "target-conditioned-separation",
    ),
    "suda25_interspeech": (
        "confirmed-current-boundary",
        "The abstract converts speech to control perceived likability while preserving speaker identity and linguistic content, using an automatically rated synthesis corpus. The evidence supports style-and-emotion-control, bounded by the likability predictor, human-rating correlation, voice-conversion method, and subjective/objective tests.",
        ["title", "abstract"], "voice-generation-and-control", "expression-and-interactive-control", "style-and-emotion-control",
    ),
    "sudo25_interspeech": (
        "confirmed-current-boundary",
        "The abstract biases ASR toward rare or unseen phrases with dynamic vocabulary while retaining non-autoregressive speed. The evidence supports domain-and-context-biasing, bounded by DYNAC's self-conditioned CTC design, dynamic tokens, LibriSpeech test, RTF change, and WER tradeoff.",
        ["title", "abstract"], "recognition-and-alignment", "context-and-open-vocabulary", "domain-and-context-biasing",
    ),
    "sudo25b_interspeech": (
        "confirmed-current-boundary",
        "The abstract adds contextual biasing for rare and unseen words to a frozen Open Whisper-style model, using a small dataset while measuring recognition and speed. The evidence supports domain-and-context-biasing, bounded by OWSM v3.1, dynamic vocabulary, LibriSpeech 100 test-clean, B-WER/WER, and real-time factor results.",
        ["title", "abstract"], "recognition-and-alignment", "context-and-open-vocabulary", "domain-and-context-biasing",
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
