#!/usr/bin/env python3
"""Record a ninth bounded ICASSP semantic review batch."""
from __future__ import annotations
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = HERE / "data"
A = [
 ("Shared Representation Learning", "listening-and-separation", "source-separation-and-spatial-listening", "target-conditioned-separation", "A reference sound supplies the target identity needed to extract one sound from a mixture."),
 ("A Noval Monte Carlo", "listening-and-separation", "noise-enhancement", "nonstationary-noise", "Active noise control must update its estimate while the interfering field changes rather than assuming stationary noise."),
 ("CoVA:", "meaning-and-interaction", "grounding-and-action", "referential-grounding", "Audio-visual retrieval must connect a language query to the sound and visual event it actually refers to."),
 ("ToS:", "listening-and-separation", "source-separation-and-spatial-listening", "spatial-filtering", "Sound-event localization uses spatial evidence to estimate both what happened and where it happened."),
 ("Break-the-Beat!", "voice-generation-and-control", "prosody-and-interactive-control", "style-and-emotion-control", "Controllable audio generation changes rhythmic delivery while preserving the intended musical structure."),
 ("Class-Aware Permutation-Invariant", "listening-and-separation", "source-separation-and-spatial-listening", "blind-source-separation", "A separation score must not punish a system for swapping sources when several sources share the same class."),
 ("Analytic Incremental Learning", "listening-and-separation", "source-separation-and-spatial-listening", "spatial-filtering", "Sound-source localization must learn new acoustic scenes without forgetting locations learned earlier."),
 ("LuSeeL:", "listening-and-separation", "source-separation-and-spatial-listening", "target-conditioned-separation", "A language query can specify which sound should be extracted from a binaural scene."),
 ("Poly-SVC:", "voice-generation-and-control", "voice-identity-and-conversion", "voice-conversion", "Singing voice conversion must change a singer while preserving multiple simultaneous musical voices."),
 ("Beyond Lips:", "listening-and-separation", "source-separation-and-spatial-listening", "target-conditioned-separation", "Visual gestures and lip motion provide a target cue for extracting one speaker from overlapping audio."),
 ("Sounding Highlights:", "meaning-and-interaction", "grounding-and-action", "referential-grounding", "Audio-visual highlight detection must connect a salient sound event to the relevant moment in a video."),
 ("Audio-to-Score Jazz", "recognition-and-alignment", "acoustic-unit-mapping", "acoustic-to-token", "Music transcription maps a continuous acoustic performance to discrete symbolic notes and timing."),
 ("FOCA: Frequency-Oriented", "evaluation-deployment-and-consequence", "privacy-security-and-accountability", "spoofing-and-deepfake", "Forgery detection should identify where and why an audio-visual signal is manipulated rather than return only a binary label."),
 ("B-GRPO:", "meaning-and-interaction", "prosody-and-intent", "paralinguistic-state", "Speech emotion recognition must learn affective states when labels are absent or uneven rather than relying on a fully labeled class set."),
 ("SwitchCodec:", "voice-generation-and-control", "text-to-speech-and-content", "neural-vocoder", "A neural codec must spend bits on acoustic detail that preserves usable sound while adapting its representation to the signal."),
 ("DECAF:", "people-variation-and-health", "clinical-and-assistive-speech", "augmentative-communication", "Speech-envelope reconstruction from EEG asks whether neural signals can provide a communication channel when acoustic speech is unavailable."),
 ("AmbER2:", "meaning-and-interaction", "prosody-and-intent", "paralinguistic-state", "Emotion recognition should retain ambiguity between speech and text cues instead of forcing one confident label."),
 ("Stemphonic:", "voice-generation-and-control", "text-to-speech-and-content", "neural-vocoder", "Flexible music generation must produce multiple sound stems that remain separately usable after synthesis."),
 ("Audiocards:", "meaning-and-interaction", "grounding-and-action", "referential-grounding", "Structured audio metadata gives a sound-language model explicit entities and attributes to ground its descriptions."),
 ("Multi-Stage Music Source", "listening-and-separation", "source-separation-and-spatial-listening", "blind-source-separation", "Music restoration separates and reconstructs overlapping sources when the original stems are unavailable."),
 ("ACAVCaps:", "meaning-and-interaction", "grounding-and-action", "referential-grounding", "Audio captioning needs diverse paired examples so a model links varied language to the same sound events."),
 ("FlowSE-GRPO:", "listening-and-separation", "noise-enhancement", "speech-prior-denoising", "Speech enhancement can optimize perceptual recovery online, but it must preserve speech rather than merely maximize a learned reward."),
 ("Residual Tokens Enhance", "recognition-and-alignment", "acoustic-unit-mapping", "self-supervised-speech-units", "Speech modeling uses residual acoustic tokens to retain detail that a coarse representation discards."),
 ("Prosody-Guided Harmonic", "voice-generation-and-control", "text-to-speech-and-content", "neural-vocoder", "A vocoder must use prosody to reconstruct phase-coherent harmonics rather than treat each spectral frame independently."),
 ("A Stabilized Hybrid Active", "listening-and-separation", "noise-enhancement", "nonstationary-noise", "Active noise control must remain stable while its online clustering changes the noise model."),
 ("S-SONDO:", "evaluation-deployment-and-consequence", "metrics-and-targets", "calibration-and-selective-use", "A general audio foundation model should be evaluated by transfer across sound tasks, not by one pretraining score."),
 ("Event Classification by Physics", "sound-and-production", "room-channel-and-sensing", "microphone-channel", "Acoustic event classification must recover a label when part of the sensor network is degraded, using the physical structure of the field."),
 ("Phonological Tokenizer:", "recognition-and-alignment", "acoustic-unit-mapping", "self-supervised-speech-units", "A phonetic tokenizer should preserve prosodic information while converting continuous speech into reusable discrete units."),
 ("PC-MCL:", "people-variation-and-health", "clinical-and-assistive-speech", "clinical-speech-marker", "Respiratory sound classification must separate patient-specific variation from the clinical condition being detected."),
 ("Taming Audio VAEs", "voice-generation-and-control", "text-to-speech-and-content", "neural-vocoder", "An audio latent model must keep its compressed representation useful for reconstruction without collapsing or wasting capacity."),
 ("Uncertainty-Aware 3D", "voice-generation-and-control", "prosody-and-interactive-control", "style-and-emotion-control", "A talking-face generator must express emotion while representing uncertainty about how visible behavior maps to vocal delivery."),
 ("Audio Effect Estimation", "sound-and-production", "time-frequency-measurement", "multi-resolution-signal", "Audio-effect estimation compares altered and unaltered signal structure across time and frequency to choose a usable transformation."),
]
papers = json.loads((DATA / "icassp-2026-papers.json").read_text())["papers"]
rows, used = [], set()
for prefix, theme, subtheme, concept, reasoning in A:
    matches = [p for p in papers if p["title"].startswith(prefix)]
    if len(matches) != 1: raise SystemExit(f"title match {prefix!r}: {len(matches)}")
    p = matches[0]
    if p["paperId"] in used: raise SystemExit(f"duplicate in batch: {p['paperId']}")
    used.add(p["paperId"])
    abstract = p.get("abstract") or ""
    if not abstract: raise SystemExit(f"batch 009 requires D2 abstract: {p['title']}")
    rows.append({"paper_id":p["paperId"],"title":p["title"],"decision":"supported","confidence":"analyst-reviewed-D2","theme_id":theme,"subtheme_id":subtheme,"concept_id":concept,"semantic_reasoning":reasoning,"evidence_excerpt":abstract[:1000],"source_location":p.get("url"),"source_sha256":hashlib.sha256(abstract.encode()).hexdigest(),"evidence_depth":"D2","review_state":"analyst-reviewed","claim_boundary":"ICASSP discovery record with abstract support; full-paper mechanisms, ablations, and limitations are not established."})
payload={"schema_version":1,"batch_id":"icassp-2026-semantic-batch-009","status":"analyst-reviewed-D2-batch","claim_boundary":"These assignments are analyst-reviewed from preserved ICASSP title/abstract records. They do not establish full-paper mechanisms or venue-wide prevalence.","reviewed_count":len(rows),"rows":rows}
(DATA / "icassp-2026-semantic-reviewed-batch-009.json").write_text(json.dumps(payload,indent=2,ensure_ascii=False)+"\n")
print(json.dumps({"batch_id":payload["batch_id"],"reviewed_count":len(rows),"D2":len(rows)}))
