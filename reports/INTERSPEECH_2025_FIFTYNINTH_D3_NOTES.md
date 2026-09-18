# INTERSPEECH 2025 fifty-ninth-pass full-paper notes

Nine genuinely uncaptured official-PDF readings extend the lowest-coverage D3 families.

## 1. time-frequency-measurement

**Paper:** [A Data-Driven Diffusion-based Approach for Audio Deepfake Explanations](https://www.isca-archive.org/interspeech_2025/grinberg25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `4c8a385770411bf08598e5c79f6470059fd72fcedf609f88dc9de12ae6950ed6`; full text captured.

- **Ordinary problem:** Audio deepfake explanations should show which changing acoustic evidence led to a detector's decision.
- **Why hard:** A global score hides local spectral events and can appear interpretable without exposing evidence.
- **Naive attempt:** Point to an arbitrary waveform segment or global saliency map and call it an explanation.
- **Central move:** Relate detector decisions to localized time-frequency structure with a data-driven explanation model.
- **Mechanism:** A spectro-temporal explanation connects model output to changing acoustic regions.
- **Mathematical/conceptual structure:** The relevant object is the windowed-spectrum evidence described by the paper's mechanism: A spectro-temporal explanation connects model output to changing acoustic regions.
- **What paper reports:** The paper reports a diffusion approach for explaining neural audio deepfake decisions.
- **Limits:** Deepfake types, explanation faithfulness, model family, and listener interpretation bound transfer.

## 2. noise-enhancement

**Paper:** [Multitalker Babble in English Vowel Perception Training: A Comparison between Humans and Neural Models](https://www.isca-archive.org/interspeech_2025/dong25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `482ed8fc09476a23a711ec5828b2dc4408231182fc17dc6a1c60d9528de3b747`; full text captured.

- **Ordinary problem:** Speech-perception training should expose listeners to realistic multitalker babble with a measurable learning target.
- **Why hard:** Babble masks cues differently from stationary noise, so SNR alone may not represent daily listening.
- **Naive attempt:** Train with clean speech or one stationary noise and assume transfer to conversation.
- **Central move:** Compare human vowel-perception training with multitalker babble against neural-model responses.
- **Mechanism:** Babble context is manipulated and perceptual/model error patterns are compared.
- **Mathematical/conceptual structure:** The relevant object is the speech-prior-denoising evidence described by the paper's mechanism: Babble context is manipulated and perceptual/model error patterns are compared.
- **What paper reports:** The paper reports a comparison of human and neural-model responses in multitalker babble.
- **Limits:** Listeners, babble construction, vowel contrasts, training duration, and model architecture bound transfer.

## 3. source-separation-and-spatial-listening

**Paper:** [Location-Aware Target Speaker Extraction for Hearing Aids](https://www.isca-archive.org/interspeech_2025/alcalapadilla25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `cd6aca2134a1fb17edf1017a420dfbb684a15c5cb9f1d9c3a13550e173159757`; full text captured.

- **Ordinary problem:** A hearing-aid listener should extract a desired talker using where the sound comes from.
- **Why hard:** Target and interferer overlap in frequency and may move while hearing aids provide limited spatial evidence.
- **Naive attempt:** Use a fixed beamformer or spectral mask without conditioning on target location.
- **Central move:** Make target location explicit in a location-aware target-speaker extraction model.
- **Mechanism:** Spatial features condition separation toward the selected direction.
- **Mathematical/conceptual structure:** The relevant object is the spatial-filtering evidence described by the paper's mechanism: Spatial features condition separation toward the selected direction.
- **What paper reports:** The paper reports location-aware target-speaker extraction for hearing-aid scenarios.
- **Limits:** Array geometry, motion, layout, processing, and intelligibility metric bound transfer.

## 4. acoustic-unit-mapping

**Paper:** [Towards a Unified Benchmark for Arabic Pronunciation Assessment: Qur’anic Recitation as Case Study](https://www.isca-archive.org/interspeech_2025/elkheir25b_interspeech.html)
**Evidence:** D3; PDF SHA-256 `6cc0700c7f7f6e7b108901409a751f5ccf2bec7265b3c16294af21b135a8c0bb`; full text captured.

- **Ordinary problem:** Qur'anic-recitation pronunciation assessment needs labels that map acoustic deviations to meaningful learner errors.
- **Why hard:** Specialized phonology and pronunciation norms make generic ASR labels insufficient.
- **Naive attempt:** Apply a general ASR benchmark or one pronunciation distance without task-specific labels.
- **Central move:** Construct a unified Arabic pronunciation-assessment benchmark around Qur'anic recitation.
- **Mechanism:** Audio, pronunciation targets, and assessment labels are aligned for model comparison.
- **Mathematical/conceptual structure:** The relevant object is the acoustic-to-token evidence described by the paper's mechanism: Audio, pronunciation targets, and assessment labels are aligned for model comparison.
- **What paper reports:** The paper presents a benchmark and case study for Arabic pronunciation assessment.
- **Limits:** Recitation tradition, annotation, coverage, and metrics bound transfer; automatic scores are not teacher judgment.

## 5. voice-identity-and-conversion

**Paper:** [Towards Better Disentanglement in Non-Autoregressive Zero-Shot Expressive Voice Conversion](https://www.isca-archive.org/interspeech_2025/akti25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `cf4c5704c02d2541d908600a64375a1a4ae0482b3f2ad27a1944fa462408a9bf`; full text captured.

- **Ordinary problem:** Zero-shot expressive voice conversion should change style while preserving content and identity for unseen voices.
- **Why hard:** Content, identity, and style are entangled, and known-speaker training encourages shortcuts.
- **Naive attempt:** Use one entangled vector or train a separate converter for every target speaker.
- **Central move:** Improve disentanglement in non-autoregressive zero-shot expressive voice conversion.
- **Mechanism:** Content, speaker, and expressive factors are separated in a non-autoregressive generation path.
- **Mathematical/conceptual structure:** The relevant object is the voice-conversion evidence described by the paper's mechanism: Content, speaker, and expressive factors are separated in a non-autoregressive generation path.
- **What paper reports:** The paper reports improved disentanglement for zero-shot expressive conversion.
- **Limits:** Enrollment, labels, languages, metrics, and unseen-speaker protocol bound transfer.

## 6. speaker-characteristics

**Paper:** [EmoSpeechAuth: Emotion-Aware Speaker Verification](https://www.isca-archive.org/interspeech_2025/goebiowska25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `6344a1d3bd890a074a2c76c688a972018ec9410d43027d900ad4b5e43057eeba`; full text captured.

- **Ordinary problem:** Speaker verification should remain reliable when emotional state changes the same person's voice.
- **Why hard:** Emotion changes pitch, timing, energy, and voice quality and can cross identity thresholds.
- **Naive attempt:** Enroll and test only neutral speech or treat emotional recordings as different identities.
- **Central move:** Build emotion-aware speaker verification and test identity evidence across affective states.
- **Mechanism:** The verifier separates speaker-consistent structure from emotion-dependent variation.
- **Mathematical/conceptual structure:** The relevant object is the speaker-verification evidence described by the paper's mechanism: The verifier separates speaker-consistent structure from emotion-dependent variation.
- **What paper reports:** The paper presents EmoSpeechAuth and evaluates emotion-aware speaker verification.
- **Limits:** Emotion labels, speakers, channel, enrollment, thresholds, and demographics bound transfer.

## 7. human-centered-evaluation

**Paper:** [EAA: Emotion-Aware Audio Large Language Models with Dual Cross-Attention and Context-Aware Instruction Tuning](https://www.isca-archive.org/interspeech_2025/du25b_interspeech.html)
**Evidence:** D3; PDF SHA-256 `0ab68c5ba71dec71429f4350f11f91b5ed7cd3992b289439a315e45c7e37eea6`; full text captured.

- **Ordinary problem:** An emotion-aware speech model should combine audio and context without confusing fluent output with reliable affect recognition.
- **Why hard:** Emotion is ambiguous and context-dependent; language models can generate plausible unsupported explanations.
- **Naive attempt:** Use one label stream or infer emotion from transcripts alone.
- **Central move:** Use dual cross-attention and context-aware instruction tuning for emotion-aware audio-language modeling.
- **Mechanism:** Cross-attention aligns acoustic and conversational representations.
- **Mathematical/conceptual structure:** The relevant object is the listener-effort evidence described by the paper's mechanism: Cross-attention aligns acoustic and conversational representations.
- **What paper reports:** The paper reports EAA results for emotion-aware audio large language modeling.
- **Limits:** Labels, prompts, audio quality, model, and human agreement bound transfer.

## 8. accent-and-cultural-boundaries

**Paper:** [Is it all about race?: A Cross-examination of /s/ in a Multilingual (Nigerian) Context](https://www.isca-archive.org/interspeech_2025/amoniyan25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `e61598574d5c543e85b0d130cdac979f57085845ed7f2666d2147aab65535306`; full text captured.

- **Ordinary problem:** Multilingual speech analysis should distinguish pronunciation patterns from racialized assumptions about speakers.
- **Why hard:** The same segment can be interpreted differently across languages and communities.
- **Naive attempt:** Assign one standard target or explain variation through race as a direct cause.
- **Central move:** Cross-examine /s/ production in a multilingual Nigerian context using linguistic and social context.
- **Mechanism:** Acoustic realization is interpreted alongside multilingual context rather than one norm.
- **Mathematical/conceptual structure:** The relevant object is the accent-robustness evidence described by the paper's mechanism: Acoustic realization is interpreted alongside multilingual context rather than one norm.
- **What paper reports:** The paper reports a contextual analysis of /s/ in a multilingual Nigerian setting.
- **Limits:** Community, language, sampling, annotation, and interpretation bound transfer.

## 9. robustness-and-system-boundary

**Paper:** [GTA: Towards Generative Text-To-Audio Retrieval via Multi-Scale Tokenizer](https://www.isca-archive.org/interspeech_2025/fang25c_interspeech.html)
**Evidence:** D3; PDF SHA-256 `1f6c6b8fef11b47082e7e3ae71b96bd280478cb7bac70152483fa138c00c222d`; full text captured.

- **Ordinary problem:** Generative text-to-audio retrieval should preserve multiscale audio structure without excessive cost.
- **Why hard:** Fine representations improve detail but make tokenization and retrieval slow or memory-heavy.
- **Naive attempt:** Use one resolution or maximize fidelity without measuring retrieval cost.
- **Central move:** Use a multi-scale tokenizer and generative retrieval architecture with explicit resource tradeoffs.
- **Mechanism:** Coarse and fine audio tokens represent different temporal resolutions for retrieval.
- **Mathematical/conceptual structure:** The relevant object is the latency-and-resource evidence described by the paper's mechanism: Coarse and fine audio tokens represent different temporal resolutions for retrieval.
- **What paper reports:** The paper reports GTA results for generative text-to-audio retrieval.
- **Limits:** Audio, prompts, token rates, metrics, hardware, and generation budget bound transfer.

