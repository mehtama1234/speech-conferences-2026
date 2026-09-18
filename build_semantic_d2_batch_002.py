#!/usr/bin/env python3
"""Record the second curated INTERSPEECH D2 semantic-adjudication batch."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = HERE / "data"

ASSIGNMENTS = {
    "birkholz25_interspeech": ("sound-and-production", "source-filter-production", "vocal-tract-filter", "The paper evaluates sound radiation from the vocal-tract wall, linking physical tract structure to the acoustic output of an articulatory synthesis model."),
    "buech25_interspeech": ("sound-and-production", "source-filter-production", "vocal-tract-filter", "Formant patterns of labialization and pharyngealization show how articulator configuration changes resonances and therefore the sound heard by a listener."),
    "chao25b_interspeech": ("sound-and-production", "time-frequency-measurement", "multi-resolution-signal", "Universal enhancement must preserve speech across several distortion types, making time-frequency information and its loss the central representation problem."),
    "deng25b_interspeech": ("sound-and-production", "time-frequency-measurement", "windowed-spectrum", "The model exposes prediction-relevant acoustic features in long speech so an analyst can connect a health-related decision back to measurable sound properties."),
    "byun25_interspeech": ("listening-and-separation", "noise-enhancement", "speech-prior-denoising", "Voice restoration combines enhancement with a learned voice prior, reconstructing a cleaner signal while risking plausible detail not present in the recording."),
    "chae25b_interspeech": ("listening-and-separation", "noise-enhancement", "nonstationary-noise", "Speech coding must preserve intelligible structure under noisy conditions and changing bitrate, so compression and noise robustness cannot be treated independently."),
    "chen25m_interspeech": ("listening-and-separation", "noise-enhancement", "speech-prior-denoising", "Dysarthric speech reconstruction uses a generative prior to repair atypical articulation, with intelligibility gains bounded by the danger of changing the speaker's intended content."),
    "cohen25_interspeech": ("listening-and-separation", "echo-and-reconstruction", "perceptual-enhancement", "Speech inpainting fills missing evidence, but the paper's uncertainty directions make clear that several plausible repairs may fit the observed context."),
    "acevedo25_interspeech": ("recognition-and-alignment", "adaptation-and-open-vocabulary", "domain-and-context-biasing", "Audio-text classification drops under background sound; the proposed adaptation changes how context is used without retraining the whole model."),
    "bagat25_interspeech": ("recognition-and-alignment", "acoustic-unit-mapping", "pronunciation-variation", "Multi-accent ASR must share useful structure while retaining pronunciation differences that a single dominant accent would call errors."),
    "balajishankar25_interspeech": ("recognition-and-alignment", "acoustic-unit-mapping", "pronunciation-variation", "Generative speech-error correction for child ASR treats unusual pronunciations as a structured correction problem rather than simply deleting uncertain words."),
    "baser25_interspeech": ("recognition-and-alignment", "acoustic-unit-mapping", "self-supervised-speech-units", "Information-theoretic representation learning asks which speech properties remain available for downstream processing while fairness and privacy constraints remove others."),
    "chao25_interspeech": ("meaning-and-interaction", "prosody-and-intent", "paralinguistic-state", "Affective adapters for spoken dialogue model emotion and paralinguistic state as information that changes how a response should be interpreted."),
    "cheng25_interspeech": ("meaning-and-interaction", "prosody-and-intent", "paralinguistic-state", "Automated multimodal affect labeling addresses the instability of emotion judgments by combining signals and standardizing what the labels mean."),
    "elmers25_interspeech": ("meaning-and-interaction", "dialogue-and-turn-taking", "turn-boundary", "Triadic turn-taking requires predicting when several participants will speak next; a pause cannot be interpreted without the interactional state."),
    "eren25_interspeech": ("meaning-and-interaction", "prosody-and-intent", "prosodic-meaning", "A prosody model conditioned on sound and text separates expressive timing and pitch from the literal linguistic content being spoken."),
    "chen25q_interspeech": ("voice-generation-and-control", "text-to-speech-and-content", "neural-vocoder", "An artifact-free vocoder must reconstruct fine waveform detail without introducing audible periodic or transient artifacts that undermine naturalness."),
    "cho25b_interspeech": ("voice-generation-and-control", "prosody-and-interactive-control", "style-and-emotion-control", "Disentangled emotion representations aim to transfer expressive style to a new speaker while keeping linguistic content and identity from drifting."),
    "choi25e_interspeech": ("voice-generation-and-control", "prosody-and-interactive-control", "prosody-control", "Singing voice conversion extracts high-frequency pitch movement so the target voice can change without losing expressive vibrato."),
    "chou25_interspeech": ("voice-generation-and-control", "voice-identity-and-conversion", "zero-shot-voice", "Zero-shot emotional conversion must infer a target voice and expressive state from little enrollment evidence, making identity/style separation the core problem."),
    "funk25_interspeech": ("people-variation-and-health", "speaker-characteristics", "age-and-development", "A voice-morphing study asks how children perceive gender from sibilant spectra, showing that acoustic cues and social interpretation are related but not identical."),
    "gaznepoglu25_interspeech": ("people-variation-and-health", "speaker-characteristics", "speaker-verification", "Voice-privacy attacks use linguistic content to recover identity, demonstrating that removing or changing words is not enough to protect a speaker."),
    "goebiowska25_interspeech": ("people-variation-and-health", "speaker-characteristics", "speaker-verification", "Emotion-aware speaker verification must preserve identity evidence while not mistaking emotional state for who is speaking."),
    "guo25d_interspeech": ("people-variation-and-health", "clinical-and-assistive-speech", "dysarthria-and-atypical-speech", "Zero-shot dysfluency transcription treats repetitions and disruptions as communication events to detect and preserve, not ordinary recognition noise."),
    "dao25_interspeech": ("languages-accents-and-resources", "low-resource-and-data-creation", "few-shot-adaptation", "Low-resource languages need useful speech instruction without assuming large speech corpora; the method shifts supervision toward language and text resources."),
    "gallego25_interspeech": ("languages-accents-and-resources", "multilingual-and-crosslingual", "crosslingual-transfer", "Phoneme-augmented speech translation makes cross-lingual transfer explicit while preserving sound distinctions important to a low-resource language."),
    "hameed25_interspeech": ("languages-accents-and-resources", "low-resource-and-data-creation", "speech-data-collection", "Recognition for low-resourced Middle Eastern languages is first a data and coverage problem; model results cannot be separated from which speakers and varieties were recorded."),
    "joshi25_interspeech": ("languages-accents-and-resources", "low-resource-and-data-creation", "speech-data-collection", "Inclusive ASR for rural Bhojpuri women tests whether data collection covers people omitted by standard speech benchmarks rather than treating their speech as generic noise."),
    "carvalho25_interspeech": ("evaluation-deployment-and-consequence", "metrics-and-targets", "word-error-versus-understanding", "Long-form ASR evaluation asks whether memory and efficient inference preserve the words that matter over extended speech, not only short-utterance accuracy."),
    "casanova25_interspeech": ("evaluation-deployment-and-consequence", "robustness-and-system-boundary", "latency-and-resource", "Ultra-fast speech language model inference makes latency a first-class system constraint, with quality claims meaningful only alongside the compute and timing budget."),
    "chang25d_interspeech": ("evaluation-deployment-and-consequence", "robustness-and-system-boundary", "latency-and-resource", "Data distillation reduces the resources needed for speech emotion recognition, so the question is whether a smaller system retains the intended performance across conditions."),
    "chen25j_interspeech": ("evaluation-deployment-and-consequence", "privacy-security-and-accountability", "spoofing-and-deepfake", "Codec-based deepfake source tracing treats generated speech provenance as a security decision whose errors have consequences beyond a synthesis benchmark."),
}


def main() -> None:
    papers = {row["paper_id"]: row for row in json.loads((DATA / "interspeech-2025-papers.json").read_text())["papers"]}
    rows = []
    for paper_id, (theme, subtheme, concept, rationale) in ASSIGNMENTS.items():
        paper = papers[paper_id]
        abstract = paper.get("abstract") or ""
        rows.append({"paper_id": paper_id, "title": paper["title"], "decision": "supported", "confidence": "analyst-reviewed-D2", "theme_id": theme, "subtheme_id": subtheme, "concept_id": concept, "semantic_reasoning": rationale, "evidence_excerpt": abstract[:900], "source_location": paper["paper_url"], "source_sha256": hashlib.sha256(abstract.encode()).hexdigest(), "evidence_depth": "D2", "review_state": "analyst-reviewed", "claim_boundary": "Abstract supports the problem and proposed conceptual move; full-paper mechanism, tables, ablations, and limitations remain unreviewed."})
    payload = {"schema_version": 1, "batch_id": "interspeech-2025-semantic-d2-batch-002", "status": "analyst-reviewed-d2-seed-batch", "claim_boundary": "These 32 assignments are analyst-reviewed from official abstracts. They do not establish full-paper mechanism or venue-wide prevalence.", "reviewed_count": len(rows), "rows": rows}
    (DATA / "interspeech-2025-semantic-reviewed-d2-batch-002.json").write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({"batch_id": payload["batch_id"], "reviewed_count": len(rows)}))


if __name__ == "__main__":
    main()
