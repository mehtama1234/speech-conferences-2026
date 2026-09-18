#!/usr/bin/env python3
"""Record a bounded ICASSP semantic review batch."""
from __future__ import annotations
import hashlib, json
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = HERE / "data"

A = {
    "GAP-URGENet:": ("sound-and-production", "time-frequency-measurement", "multi-resolution-signal", "Speech enhancement must represent slow room/noise changes and fast consonant detail at the same time."),
    "BioSEN:": ("sound-and-production", "source-filter-production", "periodic-source", "Vocalization is a produced signal whose useful source patterns can be obscured by surrounding acoustic conditions."),
    "Dissecting Performance Degradation in Audio Source Separation": ("sound-and-production", "time-frequency-measurement", "sampling-and-quantization", "A sampling-rate mismatch changes which acoustic detail exists in the input, so separation failure is partly a measurement problem."),
    "Phase-Retrieval-Based Physics-Informed": ("sound-and-production", "room-channel-and-sensing", "reverberant-mixture", "Reconstructing an acoustic field from incomplete magnitude measurements asks how propagation creates the observed mixture."),
    "CodeSep:": ("listening-and-separation", "source-separation-and-spatial-listening", "target-conditioned-separation", "A mixture can contain several voices, so the system needs a principled way to preserve the requested stream while discarding the others."),
    "SE-DiCoW:": ("listening-and-separation", "source-separation-and-spatial-listening", "target-conditioned-separation", "Diarization-conditioned recognition uses speaker identity to separate whose words should be decoded in overlapping speech."),
    "CALM:": ("listening-and-separation", "source-separation-and-spatial-listening", "blind-source-separation", "Multi-speaker recognition must infer both linguistic content and which acoustic stream belongs to the intended speaker."),
    "Towards noise-robust speech inversion": ("listening-and-separation", "noise-enhancement", "speech-prior-denoising", "Speech inversion should recover a stable linguistic or articulatory signal even when noise changes the observed waveform."),
    "UNMIXX:": ("listening-and-separation", "source-separation-and-spatial-listening", "blind-source-separation", "Highly similar voices are difficult to unmix because the available acoustic differences are small and overlapping."),
    "DisSR:": ("recognition-and-alignment", "adaptation-and-open-vocabulary", "domain-and-context-biasing", "Speech restoration must distinguish a degraded recording from the speaker and words that should remain unchanged."),
    "Position-invariant Fine-tuning": ("recognition-and-alignment", "acoustic-unit-mapping", "self-supervised-speech-units", "A recognizer should preserve useful speech representations when recording position changes the acoustic evidence."),
    "Inverse-Hessian Regularization": ("recognition-and-alignment", "adaptation-and-open-vocabulary", "domain-and-context-biasing", "Continual ASR must learn a new domain without erasing mappings that still matter for earlier speech."),
    "Tagarela - A Portuguese speech dataset": ("recognition-and-alignment", "acoustic-unit-mapping", "pronunciation-variation", "A speech dataset creates examples needed to map a language's real pronunciation variation to words."),
    "RLBR:": ("recognition-and-alignment", "adaptation-and-open-vocabulary", "domain-and-context-biasing", "Contextual recognition should use likely words without forcing the decoder to invent context that was not spoken."),
    "Encoding Emotion Through Self-Supervised Eye Movement": ("meaning-and-interaction", "prosody-and-intent", "paralinguistic-state", "Emotion is not only lexical content; it can be inferred from coordinated vocal and behavioral state cues."),
    "SPAM:": ("voice-generation-and-control", "prosody-and-interactive-control", "style-and-emotion-control", "Prompt-based TTS needs a measurement of whether generated delivery follows the requested speaking style."),
    "S\n 2\n Voice:": ("voice-generation-and-control", "voice-identity-and-conversion", "voice-conversion", "Singing-style conversion changes how a voice performs while trying to preserve musical and linguistic content."),
    "VoCodec:": ("voice-generation-and-control", "text-to-speech-and-content", "neural-vocoder", "A speech codec must preserve intelligible voice while using few bits to describe the waveform."),
    "Zero-Shot TTS with Enhanced Audio Prompts": ("voice-generation-and-control", "voice-identity-and-conversion", "zero-shot-voice", "Zero-shot synthesis asks whether a short voice prompt is enough to control who speaks without retraining."),
    "Face-Voice Association": ("people-variation-and-health", "speaker-characteristics", "speaker-verification", "Voice identity can be checked against a face, while avoiding confusion between shared content and the person who produced it."),
    "Identity Leakage Through Accent Cues": ("people-variation-and-health", "speaker-characteristics", "style-and-state-variation", "Accent can reveal identity after anonymization, so speaker protection must account for stable variation in how people speak."),
    "SpeakerRPL V2:": ("people-variation-and-health", "speaker-characteristics", "speaker-verification", "Open-set verification must decide whether an unfamiliar voice matches a claimed speaker."),
    "Windowed SummaryMixing:": ("recognition-and-alignment", "acoustic-unit-mapping", "self-supervised-speech-units", "Low-resource recognition asks how to adapt learned speech units without requiring a large new labeled corpus."),
    "Cross-Modal Bottleneck Fusion": ("recognition-and-alignment", "acoustic-unit-mapping", "acoustic-to-token", "Audio-visual recognition should let visual evidence repair noisy speech without allowing the visual stream to overwrite what was said."),
    "A Dataset of Robot-Patient": ("languages-accents-and-resources", "low-resource-and-data-creation", "speech-data-collection", "A spoken-dialogue dataset creates the situated examples needed to study medical language between different participants."),
    "CosyAccent:": ("languages-accents-and-resources", "accent-and-cultural-boundaries", "accent-robustness", "Accent normalization should change intelligibility-related pronunciation while preserving the speaker's intended words and identity."),
    "Confidence-based Filtering for Speech Dataset": ("evaluation-deployment-and-consequence", "metrics-and-targets", "calibration-and-selective-use", "Dataset curation needs confidence estimates that identify which automatically generated speech labels are safe to keep."),
    "Test-Time Adaptation for Speech Enhancement": ("evaluation-deployment-and-consequence", "robustness-and-system-boundary", "distribution-shift", "Enhancement deployed in a new acoustic environment must adapt to changed noise without clean targets."),
    "MSCT:": ("evaluation-deployment-and-consequence", "privacy-security-and-accountability", "spoofing-and-deepfake", "A multimodal detector must test whether voice and face evidence agree because coordinated manipulation can defeat a single-modality check."),
}

source = json.loads((DATA / "icassp-2026-papers.json").read_text())["papers"]
rows, used = [], set()
for prefix, assignment in A.items():
    matches = [p for p in source if p["title"].startswith(prefix)]
    if len(matches) != 1:
        raise SystemExit(f"expected one title match for {prefix!r}, found {len(matches)}")
    paper = matches[0]
    if paper["paperId"] in used:
        raise SystemExit(f"duplicate selected paper {paper['paperId']}")
    used.add(paper["paperId"])
    abstract = paper.get("abstract") or ""
    depth = "D2" if abstract else "D1"
    rows.append({"paper_id": paper["paperId"], "title": paper["title"], "decision": "supported", "confidence": f"analyst-reviewed-{depth}", "theme_id": assignment[0], "subtheme_id": assignment[1], "concept_id": assignment[2], "semantic_reasoning": assignment[3], "evidence_excerpt": abstract[:1000] if abstract else paper["title"], "source_location": paper.get("url"), "source_sha256": hashlib.sha256(abstract.encode()).hexdigest(), "evidence_depth": depth, "review_state": "analyst-reviewed", "claim_boundary": "ICASSP discovery record only; D1 rows are title-bounded and D2 rows are abstract-bounded. Full-paper mechanisms and venue-wide prevalence are not established."})

payload = {"schema_version": 1, "batch_id": "icassp-2026-semantic-batch-007", "status": "analyst-reviewed-mixed-depth-batch", "claim_boundary": "These assignments are analyst-reviewed from preserved ICASSP title/abstract records. They do not establish full-paper mechanisms or venue-wide prevalence.", "reviewed_count": len(rows), "rows": rows}
(DATA / "icassp-2026-semantic-reviewed-batch-007.json").write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
print(json.dumps({"batch_id": payload["batch_id"], "reviewed_count": len(rows), "D2": sum(x["evidence_depth"] == "D2" for x in rows), "D1": sum(x["evidence_depth"] == "D1" for x in rows)}))
