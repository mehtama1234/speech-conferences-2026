#!/usr/bin/env python3
"""Record a sixth bounded ICASSP semantic review batch.

Some ICASSP records are D1 title-only. They receive explicit title-bounded
assignments, not invented abstract claims.
"""
from __future__ import annotations
import hashlib, json
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = HERE / "data"

A = {
    "TLDiffGAN:": ("sound-and-production", "time-frequency-measurement", "windowed-spectrum", "Anomalous-sound detection asks which changing acoustic patterns distinguish an event from ordinary background sound."),
    "Generating Training Targets for Real-World Speech Enhancement": ("sound-and-production", "room-channel-and-sensing", "microphone-channel", "Close-to-distant microphone projection treats microphone distance and the recording path as part of the evidence used to train enhancement."),
    "On the Design of Higher-Order Time-Intensity Microphone Arrays": ("sound-and-production", "room-channel-and-sensing", "microphone-channel", "A panoramic microphone array changes the spatial measurements available for recording and reproduction, so sensor geometry is a first-order part of the signal."),
    "Loose Coupling of Spectral and Spatial Models": ("listening-and-separation", "source-separation-and-spatial-listening", "spatial-filtering", "Meeting diarization and enhancement must use spectral and spatial evidence together when speakers and room conditions change."),
    "Diff-vs:": ("listening-and-separation", "noise-enhancement", "speech-prior-denoising", "Vocal separation uses a diffusion model to reconstruct a target stream from a mixture, trading plausible detail against exact source fidelity."),
    "RelUNet:": ("listening-and-separation", "noise-enhancement", "spectral-mask", "Multichannel enhancement uses relations between microphone channels to suppress interference while preserving speech."),
    "Eigenbeam-Feature-Based": ("listening-and-separation", "source-separation-and-spatial-listening", "spatial-filtering", "Geometry-agnostic enhancement asks whether spatial beam evidence can remain useful when microphone layouts change."),
    "SLM-SS:": ("listening-and-separation", "source-separation-and-spatial-listening", "target-conditioned-separation", "A speech language model for separation uses learned speech structure to decide which stream a mixture can be decomposed into."),
    "Multi Stage Training with Dynamic Data Balancing": ("recognition-and-alignment", "acoustic-unit-mapping", "acoustic-to-token", "Multilingual speech recognition and translation must map varied acoustic units to words across languages with uneven data."),
    "Three Seconds is Sufficient": ("recognition-and-alignment", "adaptation-and-open-vocabulary", "speaker-adaptation", "Speaker adaptation under scarce data asks how much evidence is needed before a recognizer can adjust to a new voice."),
    "Improving Automatic Speech Recognition by Mitigating": ("recognition-and-alignment", "acoustic-unit-mapping", "acoustic-to-token", "ASR under drone noise tests whether enhancement artifacts are being mistaken for speech evidence during recognition."),
    "Leveraging Segment-Level Speech Representations": ("recognition-and-alignment", "acoustic-unit-mapping", "self-supervised-speech-units", "Segment-level representations give a language model larger speech units to use when mapping continuous audio to recognized text."),
    "Still Thinking or Stopped Talking": ("meaning-and-interaction", "dialogue-and-turn-taking", "turn-boundary", "Silence in dialogue can mean thinking or that a turn has ended, so timing alone is not enough without interaction context."),
    "SURE:": ("meaning-and-interaction", "prosody-and-intent", "paralinguistic-state", "Emotion recognition in conversation needs uncertainty-aware reasoning because affect and context are not fixed independent labels."),
    "Multimodal Self-Attention Network": ("meaning-and-interaction", "prosody-and-intent", "prosodic-meaning", "Audio-visual emotion recognition combines voice and visible behavior because affective meaning can be distributed across modalities."),
    "Mixture-of-Experts Based Soft-Label": ("meaning-and-interaction", "prosody-and-intent", "paralinguistic-state", "Soft labels and expert specialization represent several plausible emotional states instead of forcing one class."),
    "F5E-TTS:": ("voice-generation-and-control", "text-to-speech-and-content", "text-to-speech-planning", "Speech synthesis must align semantic text content with the acoustic sequence so fluent wording does not drift from what is spoken."),
    "Leveraging Text-to-Speech and Voice Conversion": ("voice-generation-and-control", "voice-identity-and-conversion", "voice-conversion", "Synthetic speech and voice conversion augment health data by changing the speaker or delivery while trying to preserve the linguistic target."),
    "TriVisionTalk:": ("voice-generation-and-control", "text-to-speech-and-content", "text-to-speech-planning", "Lip-to-speech generation infers vocal content from visual movement when the ordinary microphone signal is absent."),
    "PersonaPlex:": ("voice-generation-and-control", "prosody-and-interactive-control", "interactive-latency", "Full-duplex conversational speech models must control role and voice while responding quickly enough to maintain turn-taking."),
    "SSRFNet:": ("people-variation-and-health", "speaker-characteristics", "speaker-verification", "Speaker verification must decide identity from variable speech while keeping the decision separate from channel and content changes."),
    "TVP-UNet:": ("people-variation-and-health", "clinical-and-assistive-speech", "dysarthria-and-atypical-speech", "Voice activity detection for dysarthric speech tests whether ordinary speech boundaries survive atypical timing and articulation."),
    "Breaking Data Efficiency Dilemma": ("people-variation-and-health", "clinical-and-assistive-speech", "clinical-speech-marker", "Alzheimer detection from speech must learn health-related change with limited labeled speakers rather than treating data scarcity as ordinary noise."),
    "Noise-Robust Contrastive Learning with an MFCC-Conformer": ("people-variation-and-health", "clinical-and-assistive-speech", "clinical-speech-marker", "Coronary-artery disease detection asks whether voice and acoustic features carry a health signal that remains under noise."),
    "Language-Infused Retrieval-Augmented": ("languages-accents-and-resources", "multilingual-and-crosslingual", "code-switching", "Code-switching ASR uses language information to choose between competing lexical paths when one utterance crosses language boundaries."),
    "Exploring SSL Discrete Tokens": ("languages-accents-and-resources", "multilingual-and-crosslingual", "crosslingual-transfer", "Discrete self-supervised units test whether one learned acoustic vocabulary can serve multiple languages."),
    "Low-Resource Speech-Based Early": ("languages-accents-and-resources", "low-resource-and-data-creation", "few-shot-adaptation", "Early Alzheimer detection in a low-resource language asks how far cross-lingual transfer can go when local labeled speech is scarce."),
    "Advanced Modeling of Interlanguage Speech Intelligibility": ("languages-accents-and-resources", "accent-and-cultural-boundaries", "accent-robustness", "Interlanguage intelligibility modeling separates accent-related variation from the speech information a listener can actually understand."),
    "Evaluating Compositional Structure in Audio Representations": ("evaluation-deployment-and-consequence", "metrics-and-targets", "calibration-and-selective-use", "Representation evaluation asks whether a score reflects compositional sound structure rather than memorized labels."),
    "Lingometer:": ("evaluation-deployment-and-consequence", "metrics-and-targets", "word-error-versus-understanding", "On-device word counting must measure the intended spoken events under resource limits, not just produce a fluent transcript."),
    "Vocalnet-M2:": ("evaluation-deployment-and-consequence", "robustness-and-system-boundary", "latency-and-resource", "Low-latency spoken language modeling makes response time and model size part of whether the system is usable."),
    "Audio-Visual Deepfake Generation and Detection": ("evaluation-deployment-and-consequence", "privacy-security-and-accountability", "spoofing-and-deepfake", "Audio-visual deepfake detection asks how to distinguish manipulated voice and face evidence from genuine multimodal speech."),
}

source = json.loads((DATA / "icassp-2026-papers.json").read_text())["papers"]
rows = []
used = set()
for title_prefix, assignment in A.items():
    matches = [p for p in source if p["title"].startswith(title_prefix)]
    if len(matches) != 1:
        raise SystemExit(f"expected one title match for {title_prefix!r}, found {len(matches)}")
    paper = matches[0]
    if paper["paperId"] in used:
        raise SystemExit(f"duplicate selected paper {paper['paperId']}")
    used.add(paper["paperId"])
    abstract = paper.get("abstract") or ""
    depth = "D2" if abstract else "D1"
    rows.append({
        "paper_id": paper["paperId"], "title": paper["title"], "decision": "supported",
        "confidence": f"analyst-reviewed-{depth}", "theme_id": assignment[0],
        "subtheme_id": assignment[1], "concept_id": assignment[2],
        "semantic_reasoning": assignment[3],
        "evidence_excerpt": abstract[:1000] if abstract else paper["title"],
        "source_location": paper.get("url"),
        "source_sha256": hashlib.sha256(abstract.encode()).hexdigest(),
        "evidence_depth": depth, "review_state": "analyst-reviewed",
        "claim_boundary": "ICASSP discovery record only; title-only rows support only the named topic, while abstract-backed rows support the stated problem and proposed move. Official proceedings and full-paper mechanism are not established.",
    })

payload = {
    "schema_version": 1, "batch_id": "icassp-2026-semantic-batch-006",
    "status": "analyst-reviewed-mixed-depth-batch",
    "claim_boundary": "These assignments are analyst-reviewed from preserved ICASSP title/abstract records. D1 rows are title-bounded; D2 rows are abstract-bounded. They do not establish full-paper mechanisms or venue-wide prevalence.",
    "reviewed_count": len(rows), "rows": rows,
}
(DATA / "icassp-2026-semantic-reviewed-batch-006.json").write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
print(json.dumps({"batch_id": payload["batch_id"], "reviewed_count": len(rows), "D2": sum(x["evidence_depth"] == "D2" for x in rows), "D1": sum(x["evidence_depth"] == "D1" for x in rows)}))

