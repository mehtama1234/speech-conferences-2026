#!/usr/bin/env python3
"""Record a fourth, speech-focused ICASSP abstract-level semantic review batch."""
from __future__ import annotations
import hashlib, json
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = HERE / "data"

ASSIGNMENTS = {
    "b301ede7dc6": ("sound-and-production", "source-filter-production", "vocal-tract-physics", "A vocal-tract model treats speech production as a physical source-filter process, making the articulatory path part of the object being learned."),
    "bff2f73d8ce": ("sound-and-production", "time-frequency-measurement", "adaptive-filterbank", "Time-frequency beamformer combination adapts spectral evidence to an underdetermined mixture instead of assuming one fixed representation is sufficient."),
    "c2c0cdb7d27": ("sound-and-production", "room-channel-and-sensing", "reverberant-mixture", "Late reverberation is used as evidence about source location, showing that the room response is both a distortion and a sensing channel."),
    "e4ec2ef439": ("sound-and-production", "room-channel-and-sensing", "soundfield-reconstruction", "Sparse microphone geometry forces reconstruction of a continuous sound field from incomplete spatial measurements."),
    "b8a5252be9": ("listening-and-separation", "source-separation-and-spatial-listening", "target-conditioned-separation", "Cocktail-party emotion recognition depends on recovering the target speaker before interpreting the affective signal."),
    "ba429f7fc80": ("listening-and-separation", "noise-enhancement", "generative-enhancement", "Universal speech enhancement combines discriminative and generative repairs because observed degradation varies while intelligible speech must remain stable."),
    "c4379d42d86": ("listening-and-separation", "noise-enhancement", "multimodal-enhancement", "Bone conduction supplies a second speech-bearing channel, allowing enhancement to use physiology when the airborne recording is corrupted."),
    "9dda34ca211": ("listening-and-separation", "source-separation-and-spatial-listening", "source-counting", "Online source counting estimates how many competing sources are present before separation can be trusted."),
    "a52a797dcf4": ("recognition-and-alignment", "acoustic-unit-mapping", "acoustic-to-token", "A modality-aware Conformer changes how acoustic evidence is routed into ASR experts, making the acoustic-to-token interface conditional rather than uniform."),
    "a754babfcb3": ("recognition-and-alignment", "acoustic-unit-mapping", "self-supervised-acoustic-unit", "Efficient self-supervised speech encoders ask which temporal mixing structure preserves useful acoustic units without paying for full attention everywhere."),
    "feae3e5e4ab": ("recognition-and-alignment", "boundaries-and-sequence-structure", "streaming-alignment", "Streaming decoder-only ASR must trade future context against latency, so recognition quality is constrained by when a token may be committed."),
    "da98ee6a79a": ("recognition-and-alignment", "adaptation-and-open-vocabulary", "open-vocabulary-boundary", "Keyword spotting fails when a prefix bias suppresses unseen words, exposing the boundary between a closed keyword inventory and open speech."),
    "bad275e401e": ("meaning-and-interaction", "dialogue-and-turn-taking", "dialogue-success", "Conversational success is modeled from acoustic and facial markers, treating interaction quality as something signaled over time rather than inferred from words alone."),
    "d2d66a6da68": ("meaning-and-interaction", "prosody-and-intent", "prosody-and-phonology", "Streaming grapheme-to-phoneme and prosody prediction couples linguistic planning with prosodic realization for unsegmented languages."),
    "f48789d81eb": ("meaning-and-interaction", "dialogue-and-turn-taking", "spoken-dialogue-evaluation", "A human-like dialogue challenge makes turn-taking and response quality measurable targets instead of treating spoken dialogue as text generation alone."),
    "83cc6c7acb9": ("meaning-and-interaction", "prosody-and-intent", "prosody-and-intent", "Personalized keyword spotting combines phonemes and prosody because the same lexical content can be realized with different speaker intent and style."),
    "b32bfec9deba": ("voice-generation-and-control", "text-to-speech-and-content", "phonetic-fidelity", "A phonetic analysis of modern speech generators tests whether fluent output preserves fine segmental distinctions, not just global naturalness."),
    "8e16277adee": ("voice-generation-and-control", "text-to-speech-and-content", "synthetic-audio-provenance", "Neural codecs used in resynthesis affect both generation and the ability to label generated audio, tying synthesis choices to provenance."),
    "88b3595ca99": ("voice-generation-and-control", "prosody-and-interactive-control", "audio-morphing-control", "Sound morphing from noisy mixtures treats transformation as a controllable path between sources rather than a single fixed synthesis target."),
    "e9e185e3bf6": ("voice-generation-and-control", "prosody-and-interactive-control", "preference-controlled-generation", "Preference optimization for video-to-audio generation asks how a system can select audio that is both plausible for the scene and aligned with user judgments."),
    "f98a65513f8": ("people-variation-and-health", "clinical-and-assistive-speech", "dysarthric-speech-cues", "Layer-wise analysis of dysarthric speech descriptors asks where pathology-relevant cues live in a self-supervised representation."),
    "889896508123": ("people-variation-and-health", "clinical-and-assistive-speech", "clinical-speech-boundary", "A clinical segmentation task tests whether semi-supervised models can use speech-adjacent evidence without confusing a medical boundary with an ordinary visual one."),
    "bbe8d31e39b": ("people-variation-and-health", "human-centered-evaluation", "subjective-audio-evaluation", "A song-aesthetics challenge makes human preference the target, exposing where automatic audio scores fail to represent listener judgment."),
    "f0924eacbcf": ("people-variation-and-health", "speaker-characteristics", "speaker-representation", "Compact audio-language models must represent musical and vocal characteristics under limited capacity, making representation choice a human-variation problem."),
    "8690f2f5bc2": ("languages-accents-and-resources", "accent-and-cultural-boundaries", "child-speech-transfer", "Child ASR exposes a shift in vocal tract, pronunciation, and data distribution that adult self-supervised embeddings do not automatically absorb."),
    "cb3409d64ed": ("languages-accents-and-resources", "low-resource-and-data-creation", "low-resource-acoustic-transfer", "Cross-domain bioacoustic learning tests whether speech-derived representations transfer when labels and acoustic conditions are both scarce."),
    "db0ff89b489": ("languages-accents-and-resources", "low-resource-and-data-creation", "speech-data-selection", "Speech-model pretraining data selection treats coverage and quality as a resource-allocation problem rather than assuming more unlabeled audio is always better."),
    "97e0409dd4b": ("languages-accents-and-resources", "multilingual-and-crosslingual", "federated-language-adaptation", "Federated ASR adaptation treats language and privacy as coupled resource constraints: the system must learn from distributed varieties without centralizing speech."),
    "b6b6bce799b": ("evaluation-deployment-and-consequence", "privacy-security-and-accountability", "deepfake-detection", "Frame-level speech deepfake detection tests whether a security decision can localize inconsistent evidence rather than rely on one global artifact."),
    "fc17c3af873": ("evaluation-deployment-and-consequence", "privacy-security-and-accountability", "deepfake-consistency", "Deepfake detection can compare emotion and acoustics across levels, asking whether a generated voice is internally coherent rather than merely realistic in isolation."),
    "fce03ed9e56": ("evaluation-deployment-and-consequence", "metrics-and-targets", "subjective-ceiling", "Correlation ceilings ask how much subjective audio evaluation a metric can possibly explain before metric ranking is overinterpreted."),
    "d4de91d048a": ("evaluation-deployment-and-consequence", "metrics-and-targets", "long-context-benchmark", "A long-speech benchmark tests transcription, translation, and understanding under duration and context conditions that short utterance scores hide."),
}

source = json.loads((DATA / "icassp-2026-papers.json").read_text())["papers"]
rows = []
for prefix, assignment in ASSIGNMENTS.items():
    matches = [p for p in source if p["paperId"].startswith(prefix)]
    if len(matches) != 1:
        raise SystemExit(f"expected one paper for prefix {prefix}, found {len(matches)}")
    p = matches[0]
    abstract = p.get("abstract") or ""
    rows.append({
        "paper_id": p["paperId"], "title": p["title"], "decision": "supported",
        "confidence": "analyst-reviewed-D2", "theme_id": assignment[0],
        "subtheme_id": assignment[1], "concept_id": assignment[2],
        "semantic_reasoning": assignment[3], "evidence_excerpt": abstract[:1000],
        "source_location": p.get("url"),
        "source_sha256": hashlib.sha256(abstract.encode()).hexdigest(),
        "evidence_depth": "D2", "review_state": "analyst-reviewed",
        "claim_boundary": "ICASSP discovery/abstract record only; official proceedings and full-paper mechanism are not established.",
    })
payload = {"schema_version": 1, "batch_id": "icassp-2026-semantic-batch-004",
           "status": "analyst-reviewed-D2-batch",
           "claim_boundary": "These assignments are analyst-reviewed from preserved ICASSP abstract records. They do not establish full-paper mechanisms or venue-wide prevalence.",
           "reviewed_count": len(rows), "rows": rows}
(DATA / "icassp-2026-semantic-reviewed-batch-004.json").write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
print(json.dumps({"batch_id": payload["batch_id"], "reviewed_count": len(rows), "D2": len(rows)}))
