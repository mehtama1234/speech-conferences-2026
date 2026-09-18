"""Normalize reviewed assignments written against retired taxonomy labels.

The atlas has one canonical 72-concept taxonomy. Earlier review batches were
written while the taxonomy was being refined, so this module preserves their
evidence but translates their labels at the semantic boundary. The mapping is
deliberately explicit and context-aware where an old label was reused.
"""

from __future__ import annotations


# Old concept id -> (canonical theme, canonical subtheme, canonical concept).
# These are semantic translations, not string substitutions.
LEGACY = {
    "spectral-reconstruction": ("sound-and-production", "time-frequency-measurement", "multi-resolution-signal"),
    "domain-adaptation": ("recognition-and-alignment", "adaptation-and-open-vocabulary", "domain-and-context-biasing"),
    "speech-error-robustness": ("evaluation-deployment-and-consequence", "robustness-and-system-boundary", "distribution-shift"),
    "neural-reconstruction": ("listening-and-separation", "echo-and-reconstruction", "perceptual-enhancement"),
    "channel-microphone": ("sound-and-production", "room-channel-and-sensing", "microphone-channel"),
    "language-routing": ("languages-accents-and-resources", "multilingual-and-crosslingual", "language-identification"),
    "prosodic-recognition": ("meaning-and-interaction", "prosody-and-intent", "prosodic-meaning"),
    "synthetic-data": ("languages-accents-and-resources", "low-resource-and-data-creation", "self-training-and-pseudo-labels"),
    "speaker-role": ("meaning-and-interaction", "dialogue-and-turn-taking", "dialogue-state"),
    "clinical-articulation": ("people-and-variation", "clinical-and-assistive-speech", "clinical-speech-marker"),
    "efficient-enhancement": ("listening-and-separation", "noise-enhancement", "speech-prior-denoising"),
    "claim-grounding": ("meaning-and-interaction", "grounding-and-action", "referential-grounding"),
    "counterfactual-voice-evaluation": ("evaluation-deployment-and-consequence", "privacy-security-and-accountability", "auditability-and-contestability"),
    "spoof-aware-identity": ("evaluation-deployment-and-consequence", "privacy-security-and-accountability", "spoofing-and-deepfake"),
    "generative-restoration": ("listening-and-separation", "echo-and-reconstruction", "perceptual-enhancement"),
    "turn-boundary-prediction": ("meaning-and-interaction", "dialogue-and-turn-taking", "turn-boundary"),
    "cue-weighting": ("listening-and-separation", "source-separation-and-spatial-listening", "target-conditioned-separation"),
    "affective-intent": ("meaning-and-interaction", "prosody-and-intent", "prosodic-meaning"),
    "speaker-variation": ("people-and-variation", "speaker-characteristics", "style-and-state-variation"),
    "voice-quality": ("people-and-variation", "clinical-and-assistive-speech", "clinical-speech-marker"),
    "emotion-representation": ("meaning-and-interaction", "prosody-and-intent", "paralinguistic-state"),
    "child-speech-segmentation": ("recognition-and-alignment", "boundaries-and-sequence-structure", "alignment"),
    "uncertainty-aware-inpainting": ("listening-and-separation", "echo-and-reconstruction", "packet-loss-concealment"),
    "real-world-deepfake-shift": ("evaluation-deployment-and-consequence", "robustness-and-system-boundary", "distribution-shift"),
    "degradation-aware-routing": ("listening-and-separation", "noise-enhancement", "nonstationary-noise"),
    "periodic-vocal-source": ("sound-and-production", "source-filter-production", "periodic-source"),
    "long-context-recovery": ("listening-and-separation", "echo-and-reconstruction", "packet-loss-concealment"),
    "spectral-shape": ("sound-and-production", "time-frequency-measurement", "windowed-spectrum"),
    "source-dynamics": ("sound-and-production", "source-filter-production", "periodic-source"),
    "temporal-dynamics": ("sound-and-production", "time-frequency-measurement", "multi-resolution-signal"),
    "naturalistic-emotion": ("meaning-and-interaction", "prosody-and-intent", "paralinguistic-state"),
    "spectro-temporal-separation": ("listening-and-separation", "source-separation-and-spatial-listening", "blind-source-separation"),
    "temporal-alignment": ("recognition-and-alignment", "boundaries-and-sequence-structure", "alignment"),
    "clinical-signal-separation": ("listening-and-separation", "source-separation-and-spatial-listening", "target-conditioned-separation"),
    "articulatory-inference": ("sound-and-production", "source-filter-production", "articulatory-coordination"),
    "deepfake-provenance": ("evaluation-deployment-and-consequence", "privacy-security-and-accountability", "spoofing-and-deepfake"),
    "prosodic-production": ("sound-and-production", "source-filter-production", "articulatory-coordination"),
    "multitask-memory": ("meaning-and-interaction", "dialogue-and-turn-taking", "dialogue-state"),
    "label-noise": ("listening-and-separation", "noise-enhancement", "nonstationary-noise"),
    "spectrogram-inversion": ("listening-and-separation", "echo-and-reconstruction", "perceptual-enhancement"),
    "deepfake-variation": ("evaluation-deployment-and-consequence", "privacy-security-and-accountability", "spoofing-and-deepfake"),
    "channel-variation": ("sound-and-production", "room-channel-and-sensing", "microphone-channel"),
    "brain-to-voice": ("people-and-variation", "clinical-and-assistive-speech", "augmentative-communication"),
    "personalized-enhancement": ("listening-and-separation", "noise-enhancement", "speech-prior-denoising"),
    "multimodal-anti-spoofing": ("evaluation-deployment-and-consequence", "privacy-security-and-accountability", "spoofing-and-deepfake"),
    "multilingual-generation": ("voice-generation-and-control", "text-to-speech-and-content", "text-to-speech-planning"),
    "nonverbal-generation": ("voice-generation-and-control", "prosody-and-interactive-control", "style-and-emotion-control"),
    "multi-talker-contextual-asr": ("recognition-and-alignment", "adaptation-and-open-vocabulary", "domain-and-context-biasing"),
    "human-machine-gap": ("people-and-variation", "human-centered-evaluation", "listener-effort"),
    "child-speech-recognition": ("people-and-variation", "speaker-characteristics", "age-and-development"),
    "human-quality-estimation": ("evaluation-deployment-and-consequence", "metrics-and-targets", "quality-and-naturalness"),
    "representation-probing": ("recognition-and-alignment", "acoustic-unit-mapping", "self-supervised-speech-units"),
    "target-speaker-separation": ("listening-and-separation", "source-separation-and-spatial-listening", "target-conditioned-separation"),
    "personalized-synthesis": ("voice-generation-and-control", "voice-identity-and-conversion", "zero-shot-voice"),
    "directional-separation": ("listening-and-separation", "source-separation-and-spatial-listening", "spatial-filtering"),
    "body-conducted-listening": ("sound-and-production", "room-channel-and-sensing", "non-airborne-sensing"),
    "vocoder-discrimination": ("voice-generation-and-control", "text-to-speech-and-content", "neural-vocoder"),
    "zero-resource-pipeline": ("languages-accents-and-resources", "low-resource-and-data-creation", "few-shot-adaptation"),
    "spoken-unlearning": ("evaluation-deployment-and-consequence", "privacy-security-and-accountability", "voice-privacy"),
    "audio-deepfake-forensics": ("evaluation-deployment-and-consequence", "privacy-security-and-accountability", "spoofing-and-deepfake"),
    "dialect-aware-recognition": ("languages-accents-and-resources", "accent-and-cultural-boundaries", "dialect-and-variety"),
    "affect-data-selection": ("meaning-and-interaction", "prosody-and-intent", "paralinguistic-state"),
    "online-enhancement": ("listening-and-separation", "noise-enhancement", "nonstationary-noise"),
    "crowdsourced-listening": ("people-and-variation", "human-centered-evaluation", "listener-effort"),
    "counterfactual-prosody-editing": ("voice-generation-and-control", "prosody-and-interactive-control", "prosody-control"),
    "long-context-synthesis": ("voice-generation-and-control", "text-to-speech-and-content", "text-to-speech-planning"),
    "human-in-the-loop-annotation": ("languages-accents-and-resources", "low-resource-and-data-creation", "speech-data-collection"),
    "emphasis-emotion-control": ("voice-generation-and-control", "prosody-and-interactive-control", "style-and-emotion-control"),
    "style-retrieval": ("voice-generation-and-control", "prosody-and-interactive-control", "style-and-emotion-control"),
    "arabic-tts-resources": ("languages-accents-and-resources", "multilingual-and-crosslingual", "crosslingual-transfer"),
    "speech-instruction-following": ("meaning-and-interaction", "grounding-and-action", "speech-act"),
    "guided-separation": ("listening-and-separation", "source-separation-and-spatial-listening", "target-conditioned-separation"),
    "phoneme-grapheme-mapping": ("recognition-and-alignment", "acoustic-unit-mapping", "acoustic-to-token"),
    "speech-guided-pronunciation": ("recognition-and-alignment", "acoustic-unit-mapping", "pronunciation-variation"),
    "affective-state-fusion": ("meaning-and-interaction", "prosody-and-intent", "paralinguistic-state"),
    "explainable-speaker-attributes": ("people-and-variation", "speaker-characteristics", "style-and-state-variation"),
    "prosodic-teaching-synthesis": ("voice-generation-and-control", "prosody-and-interactive-control", "prosody-control"),
    "voice-quality-primitives": ("evaluation-deployment-and-consequence", "metrics-and-targets", "quality-and-naturalness"),
    "script-and-language-resources": ("languages-accents-and-resources", "low-resource-and-data-creation", "speech-data-collection"),
    "synthetic-code-switching": ("languages-accents-and-resources", "multilingual-and-crosslingual", "code-switching"),
    "auditory-representation": ("recognition-and-alignment", "acoustic-unit-mapping", "self-supervised-speech-units"),
    "full-duplex-dialogue": ("meaning-and-interaction", "dialogue-and-turn-taking", "turn-boundary"),
    "target-speaker-extraction": ("listening-and-separation", "source-separation-and-spatial-listening", "target-conditioned-separation"),
    "phonological-alignment": ("recognition-and-alignment", "boundaries-and-sequence-structure", "alignment"),
    "flow-synthesis": ("voice-generation-and-control", "text-to-speech-and-content", "neural-vocoder"),
    "full-duplex-interruption": ("meaning-and-interaction", "dialogue-and-turn-taking", "turn-boundary"),
    "content-intelligibility": ("voice-generation-and-control", "text-to-speech-and-content", "intelligibility-naturalness"),
    "physiological-clinical-features": ("people-and-variation", "clinical-and-assistive-speech", "clinical-speech-marker"),
    "accented-tts-resources": ("languages-accents-and-resources", "accent-and-cultural-boundaries", "accent-robustness"),
    "prosody-aware-recognition": ("meaning-and-interaction", "prosody-and-intent", "prosodic-meaning"),
    "regional-asr-corpus": ("languages-accents-and-resources", "low-resource-and-data-creation", "speech-data-collection"),
    "unified-speech-assessment": ("evaluation-deployment-and-consequence", "metrics-and-targets", "calibration-and-selective-use"),
    "body-conducted-sensing": ("sound-and-production", "room-channel-and-sensing", "non-airborne-sensing"),
    "human-fooling-rate": ("evaluation-deployment-and-consequence", "privacy-security-and-accountability", "spoofing-and-deepfake"),
    "pseudo-labeling": ("languages-accents-and-resources", "low-resource-and-data-creation", "self-training-and-pseudo-labels"),
    "accent-control": ("languages-accents-and-resources", "accent-and-cultural-boundaries", "accent-robustness"),
    "spherical-array-separation": ("listening-and-separation", "source-separation-and-spatial-listening", "spatial-filtering"),
    "cochlear-representation": ("sound-and-production", "time-frequency-measurement", "windowed-spectrum"),
    "privacy-semantic-disentanglement": ("evaluation-deployment-and-consequence", "privacy-security-and-accountability", "voice-privacy"),
    "prosodic-structure": ("meaning-and-interaction", "prosody-and-intent", "prosodic-meaning"),
    "disentangled-voice-conversion": ("voice-generation-and-control", "voice-identity-and-conversion", "voice-conversion"),
    "unknown-speaker-separation": ("listening-and-separation", "source-separation-and-spatial-listening", "blind-source-separation"),
    "dialogue-data-generation": ("meaning-and-interaction", "dialogue-and-turn-taking", "dialogue-state"),
    "individualized-hearing-enhancement": ("people-and-variation", "human-centered-evaluation", "accessibility-fit"),
    "speech-wellness": ("people-and-variation", "clinical-and-assistive-speech", "clinical-speech-marker"),
    "sound-localization": ("listening-and-separation", "source-separation-and-spatial-listening", "spatial-filtering"),
    "diffusion-spectral-model": ("sound-and-production", "time-frequency-measurement", "multi-resolution-signal"),
    "multichannel-spectral-model": ("listening-and-separation", "source-separation-and-spatial-listening", "spatial-filtering"),
    "code-switch-adaptation": ("languages-accents-and-resources", "multilingual-and-crosslingual", "code-switching"),
    "stress-and-meaning": ("meaning-and-interaction", "prosody-and-intent", "prosodic-meaning"),
    "gradient-audio-recovery": ("listening-and-separation", "echo-and-reconstruction", "perceptual-enhancement"),
    "neural-codec": ("sound-and-production", "time-frequency-measurement", "sampling-and-quantization"),
    "child-fluency-resources": ("people-and-variation", "speaker-characteristics", "age-and-development"),
    "accent-similarity-evaluation": ("languages-accents-and-resources", "accent-and-cultural-boundaries", "accent-robustness"),
    "speaker-identity": ("people-variation-and-health", "speaker-characteristics", "speaker-verification"),
    "conversational-grounding": ("meaning-and-interaction", "dialogue-and-turn-taking", "dialogue-state"),
    "audio-token-semantics": ("meaning-and-interaction", "grounding-and-action", "referential-grounding"),
    # ICASSP-era labels
    "dysarthria-assessment": ("people-and-variation", "clinical-and-assistive-speech", "clinical-speech-marker"),
    "flow-tts": ("voice-generation-and-control", "text-to-speech-and-content", "neural-vocoder"),
    "audio-language-adaptation": ("recognition-and-alignment", "adaptation-and-open-vocabulary", "domain-and-context-biasing"),
    "speech-watermarking": ("evaluation-deployment-and-consequence", "privacy-security-and-accountability", "voice-privacy"),
    "asr-error-estimation": ("evaluation-deployment-and-consequence", "metrics-and-targets", "calibration-and-selective-use"),
    "dysarthric-recognition": ("people-and-variation", "clinical-and-assistive-speech", "dysarthria-and-atypical-speech"),
    "continual-audio-separation": ("listening-and-separation", "source-separation-and-spatial-listening", "blind-source-separation"),
    "codec-tts": ("voice-generation-and-control", "text-to-speech-and-content", "neural-vocoder"),
    "privacy-preserving-conversion": ("evaluation-deployment-and-consequence", "privacy-security-and-accountability", "voice-privacy"),
    "audio-visual-separation": ("listening-and-separation", "source-separation-and-spatial-listening", "target-conditioned-separation"),
    "multichannel-asr": ("recognition-and-alignment", "boundaries-and-sequence-structure", "alignment"),
    "dysarthric-corpus": ("languages-accents-and-resources", "low-resource-and-data-creation", "speech-data-collection"),
    "speech-driven-motion": ("voice-generation-and-control", "prosody-and-interactive-control", "prosody-control"),
    "audio-visual-enhancement": ("listening-and-separation", "noise-enhancement", "spectral-mask"),
    "prosody-and-intent": ("meaning-and-interaction", "prosody-and-intent", "prosodic-meaning"),
    "child-speech-transfer": ("people-and-variation", "speaker-characteristics", "age-and-development"),
    "clinical-speech-boundary": ("people-and-variation", "clinical-and-assistive-speech", "clinical-speech-marker"),
    "audio-morphing-control": ("voice-generation-and-control", "voice-identity-and-conversion", "voice-conversion"),
    "synthetic-audio-provenance": ("evaluation-deployment-and-consequence", "privacy-security-and-accountability", "spoofing-and-deepfake"),
    "prompted-separation": ("listening-and-separation", "source-separation-and-spatial-listening", "target-conditioned-separation"),
    "federated-language-adaptation": ("languages-accents-and-resources", "multilingual-and-crosslingual", "crosslingual-transfer"),
    "synthetic-data-selection": ("languages-accents-and-resources", "low-resource-and-data-creation", "self-training-and-pseudo-labels"),
    "source-counting": ("listening-and-separation", "source-separation-and-spatial-listening", "blind-source-separation"),
    "speech-privacy": ("evaluation-deployment-and-consequence", "privacy-security-and-accountability", "voice-privacy"),
    "self-supervised-acoustic-unit": ("recognition-and-alignment", "acoustic-unit-mapping", "self-supervised-speech-units"),
    "speech-domain-adaptation": ("recognition-and-alignment", "adaptation-and-open-vocabulary", "domain-and-context-biasing"),
    "vocal-tract-physics": ("sound-and-production", "source-filter-production", "vocal-tract-filter"),
    "phonetic-fidelity": ("voice-generation-and-control", "text-to-speech-and-content", "intelligibility-naturalness"),
    "low-resource-representation": ("languages-accents-and-resources", "low-resource-and-data-creation", "few-shot-adaptation"),
    "deepfake-detection": ("evaluation-deployment-and-consequence", "privacy-security-and-accountability", "spoofing-and-deepfake"),
    "generative-enhancement": ("listening-and-separation", "noise-enhancement", "speech-prior-denoising"),
    "dialogue-success": ("meaning-and-interaction", "dialogue-and-turn-taking", "dialogue-state"),
    "subjective-audio-evaluation": ("people-and-variation", "human-centered-evaluation", "listener-effort"),
    "adaptive-filterbank": ("sound-and-production", "time-frequency-measurement", "multi-resolution-signal"),
    "multimodal-enhancement": ("listening-and-separation", "noise-enhancement", "spectral-mask"),
    "low-resource-acoustic-transfer": ("languages-accents-and-resources", "low-resource-and-data-creation", "few-shot-adaptation"),
    "prosody-and-phonology": ("meaning-and-interaction", "prosody-and-intent", "prosodic-meaning"),
    "long-context-benchmark": ("recognition-and-alignment", "boundaries-and-sequence-structure", "long-context-decoding"),
    "inference-time-separation": ("listening-and-separation", "source-separation-and-spatial-listening", "target-conditioned-separation"),
    "open-vocabulary-boundary": ("recognition-and-alignment", "adaptation-and-open-vocabulary", "open-vocabulary-recognition"),
    "speech-data-selection": ("languages-accents-and-resources", "low-resource-and-data-creation", "speech-data-collection"),
    "synthetic-mixture-design": ("listening-and-separation", "source-separation-and-spatial-listening", "blind-source-separation"),
    "soundfield-reconstruction": ("sound-and-production", "room-channel-and-sensing", "reverberant-mixture"),
    "preference-controlled-generation": ("voice-generation-and-control", "prosody-and-interactive-control", "style-and-emotion-control"),
    "asr-distillation": ("recognition-and-alignment", "acoustic-unit-mapping", "acoustic-to-token"),
    "speaker-representation": ("people-and-variation", "speaker-characteristics", "speaker-verification"),
    "speaker-domain-adaptation": ("people-and-variation", "speaker-characteristics", "speaker-verification"),
    "text-normalization": ("voice-generation-and-control", "text-to-speech-and-content", "text-to-speech-planning"),
    "spoken-dialogue-evaluation": ("meaning-and-interaction", "dialogue-and-turn-taking", "dialogue-state"),
    "dysarthric-speech-cues": ("people-and-variation", "clinical-and-assistive-speech", "dysarthria-and-atypical-speech"),
    "efficient-speech-representation": ("recognition-and-alignment", "acoustic-unit-mapping", "self-supervised-speech-units"),
    "deepfake-consistency": ("evaluation-deployment-and-consequence", "privacy-security-and-accountability", "spoofing-and-deepfake"),
    "subjective-ceiling": ("evaluation-deployment-and-consequence", "metrics-and-targets", "quality-and-naturalness"),
    "emotional-voice-conversion": ("voice-generation-and-control", "prosody-and-interactive-control", "style-and-emotion-control"),
    "streaming-alignment": ("recognition-and-alignment", "boundaries-and-sequence-structure", "alignment"),
}


# Context-specific overrides for labels reused under different old parents.
CONTEXT = {
    ("voice-generation-and-control", "voice-identity-and-conversion", "speaker-content-disentanglement"): ("voice-generation-and-control", "voice-identity-and-conversion", "voice-conversion"),
    ("voice-generation-and-control", "text-to-speech-and-content", "speaker-content-disentanglement"): ("voice-generation-and-control", "voice-identity-and-conversion", "voice-conversion"),
    ("voice-generation-and-control", "text-to-speech-and-content", "personalized-synthesis"): ("voice-generation-and-control", "voice-identity-and-conversion", "zero-shot-voice"),
    ("voice-generation-and-control", "voice-identity-and-conversion", "deepfake-provenance"): ("evaluation-deployment-and-consequence", "privacy-security-and-accountability", "spoofing-and-deepfake"),
    ("listening-and-separation", "echo-and-reconstruction", "synthetic-data"): ("languages-accents-and-resources", "low-resource-and-data-creation", "self-training-and-pseudo-labels"),
    ("meaning-and-interaction", "dialogue-and-turn-taking", "speaker-variation"): ("people-and-variation", "speaker-characteristics", "style-and-state-variation"),
    ("sound-and-production", "echo-and-reconstruction", "spectrogram-inversion"): ("listening-and-separation", "echo-and-reconstruction", "perceptual-enhancement"),
}


def normalize_review_row(
    row: dict,
    valid_concepts: set[str] | None = None,
    canonical_triples: set[tuple[str, str, str]] | None = None,
) -> dict:
    """Return a copied row whose reviewed assignment uses canonical IDs."""
    out = dict(row)
    if out.get("decision") == "unsupported":
        return out
    old_theme, old_subtheme, old_concept = out.get("theme_id"), out.get("subtheme_id"), out.get("concept_id")
    if valid_concepts and old_concept in valid_concepts:
        if canonical_triples:
            parent = next((triple for triple in canonical_triples if triple[2] == old_concept), None)
            if parent:
                out["theme_id"], out["subtheme_id"], out["concept_id"] = parent
        return out
    target = CONTEXT.get((old_theme, old_subtheme, old_concept)) or LEGACY.get(old_concept)
    if target:
        # Legacy entries often already name the surviving concept but retain
        # the subtheme that existed before the organic regrouping.  Resolve
        # the concept against the live taxonomy one more time so every
        # reviewed row follows the current concept parent.
        if canonical_triples and target[2] in valid_concepts:
            parent = next((triple for triple in canonical_triples if triple[2] == target[2]), None)
            if parent:
                out["theme_id"], out["subtheme_id"], out["concept_id"] = parent
                return out
        if target[0] == "people-and-variation":
            target = ("people-variation-and-health", target[1], target[2])
        out["theme_id"], out["subtheme_id"], out["concept_id"] = target
    return out
