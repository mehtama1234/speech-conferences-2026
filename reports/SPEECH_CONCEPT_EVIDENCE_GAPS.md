# Speech concept evidence gaps

These are taxonomy concepts with no analyst-reviewed ICASSP example in the current bounded release. The absence is an evidence gap, not a prevalence claim.

- Gaps: 4
- Source boundary: ICASSP title/abstract metadata; most records are title-only.

## Articulatory coordination (`articulatory-coordination`)

**Ordinary problem:** Speech is a timed coordination of several moving constrictions, not a sequence of isolated sounds; overlap lets one gesture affect its neighbors.

**Boundary:** A label such as a phoneme is not itself a physical movement or a complete account of coarticulation.

**INTERSPEECH reviewed examples:** 29
**ICASSP reviewed examples:** 0

**Nearest unresolved ICASSP candidates:**

- No candidate was found by the current subtheme proposal rules.

**Nearby reviewed records not counted as membership:**

- EMG-to-Speech with Fewer Channels — assigned to `atypical-and-assistive-speech/augmentative-communication`; Lexical or abstract proximity is not membership; the paper remains assigned to its reviewed primary concept.
- IPACue-TTS: Integrating Prosody and Articulatory Cues in Conditional Flow Matching for Multilingual Zero-Shot TTS — assigned to `expression-and-interactive-control/prosody-control`; Lexical or abstract proximity is not membership; the paper remains assigned to its reviewed primary concept.
- Mixtures of Lightweight Articulatory Experts for Multilingual Asr — assigned to `crosslingual-structure/crosslingual-transfer`; Lexical or abstract proximity is not membership; the paper remains assigned to its reviewed primary concept.
- From Hallucination to Articulation: Language Model-Driven Losses for Ultra Low-Bitrate Neural Speech Coding — assigned to `time-frequency-measurement/multi-resolution-signal`; Lexical or abstract proximity is not membership; the paper remains assigned to its reviewed primary concept.

**Next evidence needed:** An analyst must inspect the title/abstract or full paper and show that this concept, rather than a neighboring one, is central to the paper's ordinary speech problem.

## Packet-loss concealment (`packet-loss-concealment`)

**Ordinary problem:** When transmitted audio frames disappear, infer a short continuation from nearby waveform or speech structure so playback does not break.

**Boundary:** Short plausible continuation is not recovery of the original utterance and becomes unsafe over long gaps.

**INTERSPEECH reviewed examples:** 4
**ICASSP reviewed examples:** 0

**Nearest unresolved ICASSP candidates:**

- No candidate was found by the current subtheme proposal rules.

**Nearby reviewed records not counted as membership:**

- Unseen but not Unknown: Using Dataset Concealment to Robustly Evaluate Speech Quality Estimation Models — assigned to `metric-and-human-targets/calibration-and-selective-use`; Lexical or abstract proximity is not membership; the paper remains assigned to its reviewed primary concept.
- Context-Aware Dynamic Graph Learning for Multimodal Emotion Recognition with Missing Modalities — assigned to `prosody-and-paralinguistics/paralinguistic-state`; Lexical or abstract proximity is not membership; the paper remains assigned to its reviewed primary concept.
- Content Leakage in LibriSpeech and Its Impact on the Privacy Evaluation of Speaker Anonymization — assigned to `privacy-and-security/voice-privacy`; Lexical or abstract proximity is not membership; the paper remains assigned to its reviewed primary concept.
- Identity Leakage Through Accent Cues in Voice Anonymisation — assigned to `identity-and-life-stage/style-and-state-variation`; Lexical or abstract proximity is not membership; the paper remains assigned to its reviewed primary concept.

**Next evidence needed:** An analyst must inspect the title/abstract or full paper and show that this concept, rather than a neighboring one, is central to the paper's ordinary speech problem.

## Disfluency and event preservation (`disfluency-preservation`)

**Ordinary problem:** Represent pauses, repetitions, repairs, laughter, and overlap when those events are part of the communication or the clinical signal.

**Boundary:** Removing them may improve readability while destroying evidence needed for conversation analysis or diagnosis.

**INTERSPEECH reviewed examples:** 10
**ICASSP reviewed examples:** 0

**Nearest unresolved ICASSP candidates:**

- No candidate was found by the current subtheme proposal rules.

**Nearby reviewed records not counted as membership:**

- A Hierarchical Coarse-to-Fine Whisper Adaptation Framework for ALS Dysarthria Severity Estimation — assigned to `clinical-markers/clinical-speech-marker`; Lexical or abstract proximity is not membership; the paper remains assigned to its reviewed primary concept.
- LMS-Whisper: Efficient Lightweight Whisper for Multi-Stutter Speech Classification — assigned to `atypical-and-assistive-speech/dysarthria-and-atypical-speech`; Lexical or abstract proximity is not membership; the paper remains assigned to its reviewed primary concept.
- Multi-View Hierarchical Hypergraph Neural Network for Automatic Stuttering Detection — assigned to `clinical-markers/clinical-speech-marker`; Lexical or abstract proximity is not membership; the paper remains assigned to its reviewed primary concept.
- PhoenixDSR: Phoneme-Guided and LLM-Enhanced Dysarthric Speech Recognition — assigned to `atypical-and-assistive-speech/dysarthria-and-atypical-speech`; Lexical or abstract proximity is not membership; the paper remains assigned to its reviewed primary concept.
- SS-JDSC: Single-Speaker Japanese Dysarthric Speech Corpus — assigned to `data-creation/speech-data-collection`; Lexical or abstract proximity is not membership; the paper remains assigned to its reviewed primary concept.
- Syllable-Level Acoustic Modeling with a Stage-Aware Transformer for ALS Dysarthria Severity Estimation - ICASSP-2026 Sand Challenge — assigned to `clinical-markers/clinical-speech-marker`; Lexical or abstract proximity is not membership; the paper remains assigned to its reviewed primary concept.
- TVP-UNet: Threshold Variance Penalty U-Net for Voice Activity Detection in Dysarthric Speech — assigned to `atypical-and-assistive-speech/dysarthria-and-atypical-speech`; Lexical or abstract proximity is not membership; the paper remains assigned to its reviewed primary concept.
- Time vs. Layer: Locating Predictive Cues for Dysarthric Speech Descriptors in wav2vec 2.0 — assigned to `atypical-and-assistive-speech/dysarthria-and-atypical-speech`; Lexical or abstract proximity is not membership; the paper remains assigned to its reviewed primary concept.

**Next evidence needed:** An analyst must inspect the title/abstract or full paper and show that this concept, rather than a neighboring one, is central to the paper's ordinary speech problem.

## User control and consent (`user-control-and-consent`)

**Ordinary problem:** Let speakers decide how their voice is recorded, adapted, generated, shared, or corrected, especially when identity is involved.

**Boundary:** A consent checkbox does not solve power imbalance, downstream copying, or inability to withdraw a trained model.

**INTERSPEECH reviewed examples:** 2
**ICASSP reviewed examples:** 0

**Nearest unresolved ICASSP candidates:**

- No candidate was found by the current subtheme proposal rules.

**Nearby reviewed records not counted as membership:**

- Content Leakage in LibriSpeech and Its Impact on the Privacy Evaluation of Speaker Anonymization — assigned to `privacy-and-security/voice-privacy`; Lexical or abstract proximity is not membership; the paper remains assigned to its reviewed primary concept.
- Identity Leakage Through Accent Cues in Voice Anonymisation — assigned to `identity-and-life-stage/style-and-state-variation`; Lexical or abstract proximity is not membership; the paper remains assigned to its reviewed primary concept.
- PFluxTTS: Hybrid Flow-Matching TTS with Robust Cross-Lingual Voice Cloning and Inference-Time Model Fusion — assigned to `identity-and-conversion/zero-shot-voice`; Lexical or abstract proximity is not membership; the paper remains assigned to its reviewed primary concept.
- Stream-Voice-Anon: Enhancing Utility of Real-Time Speaker Anonymization via Neural Audio Codec and Language Models — assigned to `identity-and-conversion/zero-shot-voice`; Lexical or abstract proximity is not membership; the paper remains assigned to its reviewed primary concept.
- ECSA: Dual-Branch Emotion Compensation for Emotion-Consistent Speaker Anonymization — assigned to `privacy-and-security/voice-privacy`; Lexical or abstract proximity is not membership; the paper remains assigned to its reviewed primary concept.
- Erasing Your Voice Before It's Heard: Training-free Speaker Unlearning for Zero-shot Text-to-Speech — assigned to `identity-and-conversion/speaker-identity`; Lexical or abstract proximity is not membership; the paper remains assigned to its reviewed primary concept.
- Listen, But Don't Leak: Sensitive Data Protection for Privacy Aware Automatic Speech Recognition with Acoustic Triggers — assigned to `privacy-and-security/voice-privacy`; Lexical or abstract proximity is not membership; the paper remains assigned to its reviewed primary concept.
- Marco-Voice: A Unified Framework for Expressive Speech Synthesis with Voice Cloning — assigned to `identity-and-conversion/voice-conversion`; Lexical or abstract proximity is not membership; the paper remains assigned to its reviewed primary concept.

**Next evidence needed:** An analyst must inspect the title/abstract or full paper and show that this concept, rather than a neighboring one, is central to the paper's ordinary speech problem.

