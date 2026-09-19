#!/usr/bin/env python3
"""Record the next eight evidence-bounded taxonomy adjudications."""
import json
from pathlib import Path

QUEUE = Path(__file__).resolve().parent / "data/speech-taxonomy-adjudication-queue.json"
DECISIONS = {
    "xie25_interspeech": (
        "confirmed-current-boundary",
        "The abstract uses microphone-array spatial cues to recognize a selected talker, localize the source, and suppress bystander cross-talk. The evidence supports target-conditioned-separation, bounded by directional-SpeechLlama, smart-glasses arrays, serialized directional output, contrastive direction augmentation, and the reported recognition/localization results.",
        ["title", "abstract"], "listening-and-separation", "source-separation", "target-conditioned-separation",
    ),
    "xie25b_interspeech": (
        "confirmed-current-boundary",
        "The abstract trains a speech-language model from paired speech and transcripts, using multi-task behavior imitation and speech-text interleaving to make speech map to the same response space as text. The evidence supports self-supervised-speech-units, bounded by the MTBI setup, paired-data requirement, prompt/task generalization benchmark, and reported model comparisons.",
        ["title", "abstract"], "recognition-and-alignment", "acoustic-unit-learning", "self-supervised-speech-units",
    ),
    "xing25_interspeech": (
        "confirmed-current-boundary",
        "The abstract transfers emotion from reference speech to new text by separating content, emotion, and other style, then prioritizing emotion during synthesis. The evidence supports style-and-emotion-control, bounded by zero-shot TTS, LibriTTS, the emotion-adaptive converter, and reported expressiveness/adaptation results.",
        ["title", "abstract"], "voice-generation-and-control", "expression-and-interactive-control", "style-and-emotion-control",
    ),
    "xiong25_interspeech": (
        "confirmed-current-boundary",
        "The abstract addresses dysarthric speech detection under small-data overfitting by jointly training a related recognition task and the target task, with gradient projection to manage conflicting updates. The evidence supports dysarthria-and-atypical-speech, bounded by the foundation-model fine-tuning setup, in- and cross-corpus tests, and reported accuracy changes.",
        ["title", "abstract"], "people-variation-and-health", "atypical-and-assistive-speech", "dysarthria-and-atypical-speech",
    ),
    "xiong25b_interspeech": (
        "confirmed-current-boundary",
        "The abstract shows that talker identification changes with language and accent familiarity because listeners use different acoustic cues as they learn the context. The evidence supports accent-robustness, bounded by Mandarin-speaking listeners, Mandarin-accented English and native-language conditions, F0/jitter-style acoustic features, and the training study.",
        ["title", "abstract"], "languages-accents-and-resources", "accent-dialect-and-cultural-meaning", "accent-robustness",
    ),
    "xu25c_interspeech": (
        "confirmed-current-boundary",
        "The paper processes multiple frames in parallel to find non-blank RNN-T predictions sooner while preserving recognition accuracy. The evidence supports latency-and-resource, bounded by the WIND decoding strategies, greedy and beam-search settings, multi-dataset tests, and the reported speed/WER results.",
        ["title", "abstract", "full_paper"], "evaluation-deployment-and-consequence", "deployment-cost", "latency-and-resource",
    ),
    "xu25d_interspeech": (
        "confirmed-current-boundary",
        "The abstract predicts a preliminary clean spectrogram from time, frequency, and noise views, then reconstructs speech with a short diffusion sampling process. The evidence supports multi-resolution-signal, bounded by MDDM, public and real-world datasets, subjective/objective measures, and the reported enhancement comparison.",
        ["title", "abstract"], "sound-and-production", "time-frequency-measurement", "multi-resolution-signal",
    ),
    "xu25e_interspeech": (
        "confirmed-current-boundary",
        "The paper compresses speech foundation models by jointly learning fine-grained pruning gates and parameter updates, reducing model size and compression time while measuring recognition cost. The evidence supports latency-and-resource, bounded by wav2vec 2.0 and HuBERT experiments, LibriSpeech-100hr, pruning ratio, WER, and compression-time comparisons.",
        ["title", "abstract", "full_paper"], "evaluation-deployment-and-consequence", "deployment-cost", "latency-and-resource",
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
