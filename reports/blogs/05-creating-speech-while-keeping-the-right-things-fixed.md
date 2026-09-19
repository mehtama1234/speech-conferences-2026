# Creating speech while keeping the right things fixed

*Essay 5 of 8 in The Speech Atlas.*

Making speech is not one decision. A system must decide what to say, when to say it, whose voice to use, and how the delivery should sound. This essay separates those controls so a gain in one does not hide a loss in another.

## Start with the baseline

Fant's speech-chain account places this theme at the following point in communication: Fant pp. 2-3: production passes through message, sentence form, motor activity, and acoustic processes; a generator must keep these layers aligned.

The ordinary problem is simple to state: A useful synthetic voice must say the requested content, sound like the intended speaker or style, and remain understandable as it changes over time.

A tempting shortcut is to Copying a recording or predicting samples directly entangles words with identity, pitch, rhythm, and recording conditions, making controlled change difficult. That shortcut fails because it hides the distinction this essay needs to keep visible.

The recurring move across this theme is to Represent or condition distinct factors, generate a time-consistent waveform or acoustic sequence, and evaluate each requested property separately. The cost is equally important: Factor separation is rarely perfect: changing identity can change content, style controls can sound artificial, and a plausible voice can be misused.

## The boundaries

Each section below uses the same test: what pressure is being handled, what shortcut fails, what move recurs, and where the evidence stops.

## Turning language into a timed speech plan

**The question.** What ordinary speech pressure is handled by turning language into a timed speech plan, and what evidence distinguishes it from neighboring pressures?

**How this boundary is derived.** Baseline link: Fant pp. 2-3: production passes through message, sentence form, motor activity, and acoustic processes; a generator must keep these layers aligned. Ordinary pressure: A useful synthetic voice must say the requested content, sound like the intended speaker or style, and remain understandable as it changes over time. Failed shortcut: Copying a recording or predicting samples directly entangles words with identity, pitch, rhythm, and recording conditions, making controlled change difficult. Recurring paper move: Represent or condition distinct factors, generate a time-consistent waveform or acoustic sequence, and evaluate each requested property separately. Neighbor test: This boundary covers the step from intended text or meaning to pronunciation, duration, pitch targets, and sequence; it is separate from waveform generation, which realizes an already chosen plan as samples.

**What the papers share.** A useful synthetic voice must say the requested content, sound like the intended speaker or style, and remain understandable as it changes over time. The subtheme asks: What ordinary speech pressure is handled by turning language into a timed speech plan, and what evidence distinguishes it from neighboring pressures?

**Why the shortcut fails.** A first attempt would answer the question only with text-to-speech planning, but that shortcut misses the boundary: Text does not specify one correct prosody, and a fluent output can still mispronounce names or sound unnatural.

**The recurring move.** Across this subtheme, papers make text-to-speech planning explicit rather than treating the speech evidence as one undifferentiated variable. The reviewed full-paper mechanisms instantiate that move in different ways; for example: Transfer pronunciation knowledge from a large multi-accent frontend and measure how much target-accent data is needed as source accents vary in similarity.

### Words used in this section

**Text-to-speech planning.** Choose pronunciation, durations, pitch targets, and acoustic details before or while producing the waveform so written content becomes speakable.
*Boundary:* Text does not specify one correct prosody, and a fluent output can still mispronounce names or sound unnatural.

### What the papers show

- [Non-Standard Accent TTS Support via Large Multi-Accent Frontend Pronunciation Knowledge Transfer](https://www.isca-archive.org/interspeech_2025/berger25_interspeech.html) (D3): Transfer pronunciation knowledge from a large multi-accent frontend and measure how much target-accent data is needed as source accents vary in similarity. **Measured or tested:** The multi-accent pronunciation frontend is tested on EDI and LDS1 accents against uni-accent baselines using word-boundary, prosodic-boundary, and word accuracy for seen and unseen tokens. The paper reports multi-accent accuracy near the uni-accent baseline, with seen-word scores above 99% and… **Limit:** Accuracy is reported for the studied accents, frontend labels, and datasets; transfer to other languages, voices, and synthesis backends remains unestablished.
- [Accelerating Diffusion-based Text-to-Speech Model Trainingwith Dual Modality Alignment](https://www.isca-archive.org/interspeech_2025/choi25c_interspeech.html) (D3): Align hidden states using both text-guided and speech-guided objectives so the diffusion process starts with more useful semantic structure. **Measured or tested:** The diffusion TTS model is trained on approximately 585 hours of multi-speaker LibriTTS and evaluated on the 2.2-hour LibriSpeech-PC test-clean set. WER measures intelligibility and speaker similarity is measured against the F5-TTS Small baseline; the paper reports comparisons for the… **Limit:** The text/speech encoders, datasets, diffusion schedule, and quality measures bound the claim; hardware cost and new languages remain open.
- [Scheduled Interleaved Speech-Text Training for Speech-to-Speech Translation with LLMs](https://www.isca-archive.org/interspeech_2025/futami25_interspeech.html) (D3): Interleave aligned text and speech units during training, then gradually reduce the text proportion so the model moves toward speech output. **Measured or tested:** We conduct experimental evaluations by fine-tuning LLaMA3.2-1B for S2ST on the CVSS dataset. **Limit:** CVSS, unitizer, schedule, model size, and languages bound the result; naturalness, speaker identity, and unseen domains need separate tests.
- [Code Mix TTS: An Approach to Infer Human Like Speech for Multi-Lingual Input Texts](https://www.isca-archive.org/interspeech_2025/gourav25_interspeech.html) (D3): Infer code-mixed speech from multilingual text without requiring additional training data or fine-tuning. **Measured or tested:** We have come a far way in terms of producing high quality, human like audios for given input texts using TTS or Text to Speech Systems. **Limit:** The paper's method and evaluation details are bounded by the selected TTS system, languages, and automated metric; human listening, pronunciation accuracy, and unseen language pairs remain open.

**Where this boundary stops.** Text does not specify one correct prosody, and a fluent output can still mispronounce names or sound unnatural.

**What this evidence does not establish.** The shared story is supported only by the reviewed papers listed here; D2 entries support the problem and stated method, while D3 entries support the reported mechanism and evaluation. It is not a venue-wide prevalence claim.

**Question left open.** What changes when this move is tested outside the speakers, languages, rooms, devices, or benchmark conditions represented by the 10 D3 paper(s)?

## Producing or compressing audible detail

**The question.** What ordinary speech pressure is handled by producing or compressing audible detail, and what evidence distinguishes it from neighboring pressures?

**How this boundary is derived.** Baseline link: Fant pp. 2-3: production passes through message, sentence form, motor activity, and acoustic processes; a generator must keep these layers aligned. Ordinary pressure: A useful synthetic voice must say the requested content, sound like the intended speaker or style, and remain understandable as it changes over time. Failed shortcut: Copying a recording or predicting samples directly entangles words with identity, pitch, rhythm, and recording conditions, making controlled change difficult. Recurring paper move: Represent or condition distinct factors, generate a time-consistent waveform or acoustic sequence, and evaluate each requested property separately. Neighbor test: The issue is sample-level detail and the tradeoff between faithful content and natural sound.

**What the papers share.** A useful synthetic voice must say the requested content, sound like the intended speaker or style, and remain understandable as it changes over time. The subtheme asks: What ordinary speech pressure is handled by producing or compressing audible detail, and what evidence distinguishes it from neighboring pressures?

**Why the shortcut fails.** A first attempt would answer the question only with waveform synthesis, but that shortcut misses the boundary: Sample-level realism does not guarantee correct words, stable identity, or natural long-range timing.

**The recurring move.** Across this subtheme, papers make waveform synthesis, intelligibility versus naturalness explicit rather than treating the speech evidence as one undifferentiated variable. The reviewed full-paper mechanisms instantiate that move in different ways; for example: Train in two stages: first use a mirror architecture to stabilize the codebook, then switch to a stronger non-mirror decoder while preserving the learned quantizer.

### Words used in this section

**Waveform synthesis.** Generate fine-grained samples conditioned on a coarser acoustic plan, reconstructing the periodic and noisy detail listeners hear as voice.
*Boundary:* Sample-level realism does not guarantee correct words, stable identity, or natural long-range timing.

**Intelligibility versus naturalness.** Treat ease of understanding and human-likeness as related but distinct targets that need separate tests.
*Boundary:* A single listener score can conflate content accuracy, recording quality, and preference.

### What the papers show

- [DS-Codec: Dual-Stage Training with Mirror-to-NonMirror Architecture Switching for Speech Codec](https://www.isca-archive.org/interspeech_2025/chen25p_interspeech.html) (D3): Train in two stages: first use a mirror architecture to stabilize the codebook, then switch to a stronger non-mirror decoder while preserving the learned quantizer. **Measured or tested:** We conduct extensive experiments and ablation studies to evaluate the effectiveness of our training strategy and compare the performance of the two architectures. **Limit:** The speech data, bitrate/downsampling setting, discriminators, metrics, and baselines bound the result; reconstruction quality does not by itself prove usefulness for every TTS or speech-language-model task.
- [AF-Vocoder: Artifact-Free Neural Vocoder with Global Artifact Filter](https://www.isca-archive.org/interspeech_2025/chen25q_interspeech.html) (D3): Add a learnable frequency-domain artifact filter that imposes explicit control over which spectral components pass. **Measured or tested:** In this paper, we propose AF-Vocoder, a novel GAN-based vocoder that can synthesize high-fidelity speech with fewer artifacts. **Limit:** Datasets, speaker coverage, artifacts, and listening protocol define the claim; real-time hardware cost and unseen languages remain open.
- [Vocoder-Projected Feature Discriminator](https://www.isca-archive.org/interspeech_2025/kaneko25b_interspeech.html) (D3): Project generated acoustic features through a vocoder and discriminate in a vocoder-feature space, retaining waveform-relevant feedback with lower time-domain overhead. **Measured or tested:** Vocoder-Projected Feature Discriminator is evaluated on VCTK and LibriTTS using UTMOS, DNSMOS, Whisper-large-v3 CER, Resemblyzer SECS, training time, and peak memory. Ablations vary discriminator upsampling depth, pretraining/freezing, and alternative acceleration strategies; the main subjective… **Limit:** Vocoder choice, feature projection, training compute, VC data, and perceptual evaluation determine the result; a reported quality gain does not establish universal TTS or VC superiority.
- [BitTTS: Highly Compact Text-to-Speech Using 1.58-bit Quantization and Weight Indexing](https://www.isca-archive.org/interspeech_2025/kawamura25_interspeech.html) (D3): Train with quantization present and pack groups of ternary-like weights into compact integer indices so the model learns to tolerate the reduced precision and storage format. **Measured or tested:** In this case, most of 32-bit model parameters are quantized to ternary values {-1, 0, 1}. **Limit:** Hardware, model architecture, bitrate/precision, speech data, and quality metrics bound the result; smaller storage does not automatically mean lower latency or energy on every device.

**Where this boundary stops.** Sample-level realism does not guarantee correct words, stable identity, or natural long-range timing.; A single listener score can conflate content accuracy, recording quality, and preference.

**What this evidence does not establish.** The shared story is supported only by the reviewed papers listed here; D2 entries support the problem and stated method, while D3 entries support the reported mechanism and evaluation. It is not a venue-wide prevalence claim.

**Question left open.** What changes when this move is tested outside the speakers, languages, rooms, devices, or benchmark conditions represented by the 8 D3 paper(s)?

## Changing who sounds like the speaker

**The question.** What ordinary speech pressure is handled by changing who sounds like the speaker, and what evidence distinguishes it from neighboring pressures?

**How this boundary is derived.** Baseline link: Fant pp. 2-3: production passes through message, sentence form, motor activity, and acoustic processes; a generator must keep these layers aligned. Ordinary pressure: A useful synthetic voice must say the requested content, sound like the intended speaker or style, and remain understandable as it changes over time. Failed shortcut: Copying a recording or predicting samples directly entangles words with identity, pitch, rhythm, and recording conditions, making controlled change difficult. Recurring paper move: Represent or condition distinct factors, generate a time-consistent waveform or acoustic sequence, and evaluate each requested property separately. Neighbor test: This boundary covers changing or measuring who the voice sounds like while keeping the message stable; it is separate from expression control, which changes emotion or style, and from content planning, which changes the speech plan.

**What the papers share.** A useful synthetic voice must say the requested content, sound like the intended speaker or style, and remain understandable as it changes over time. The subtheme asks: What ordinary speech pressure is handled by changing who sounds like the speaker, and what evidence distinguishes it from neighboring pressures?

**Why the shortcut fails.** A first attempt would answer the question only with speaker identity representation, but that shortcut misses the boundary: A short recording can encode noise, emotion, or demographic stereotypes rather than stable identity.

**The recurring move.** Across this subtheme, papers make speaker identity representation, voice conversion, unseen-speaker synthesis explicit rather than treating the speech evidence as one undifferentiated variable. The reviewed full-paper mechanisms instantiate that move in different ways; for example: Build a longitudinal English/Mandarin resource and measure how aging changes verification evidence.

### Words used in this section

**Speaker identity representation.** Capture stable voice traits that let a system preserve or imitate who is speaking across different words and sessions.
*Boundary:* A short recording can encode noise, emotion, or demographic stereotypes rather than stable identity.

**Voice conversion.** Transform the acoustic realization toward a target voice while trying to preserve linguistic timing and content.
*Boundary:* Conversion may leak source identity, distort pronunciation, or require target-speaker data unavailable in practice.

**Unseen-speaker synthesis.** Use a voice description or brief enrollment to synthesize a speaker not represented by a dedicated model.
*Boundary:* Similarity on a benchmark does not establish consent, identity security, or robustness to unusual voices.

### What the papers show

- [VoxAging: Continuously Tracking Speaker Aging with a Large-Scale Longitudinal Dataset in English and Mandarin](https://www.isca-archive.org/interspeech_2025/ai25_interspeech.html) (D3): Build a longitudinal English/Mandarin resource and measure how aging changes verification evidence. **Measured or tested:** VoxAging contains 293 speakers with longitudinal English/Mandarin recordings spanning up to about 17 years. Speaker-aging experiments compare ECAPA and ERes2Net verification systems using EER on held-out speaker-recognition conditions and embedding cosine similarity across recordings, with… **Limit:** Speaker coverage, language balance, recording channels, gated data, and longitudinal confounding limit causal claims about biological aging.
- [Towards Better Disentanglement in Non-Autoregressive Zero-Shot Expressive Voice Conversion](https://www.isca-archive.org/interspeech_2025/akti25_interspeech.html) (D3): Improve disentanglement in non-autoregressive zero-shot expressive voice conversion. **Measured or tested:** Evaluation uses ESD, Expresso, and LibriTTS test sets. Objective measures are Whisper-Large-3 WER, Resemblyzer speaker-embedding cosine similarity, Emotion2Vec+ emotion similarity and classification accuracy, and speaker-verification EER; subjective measures are 1–5 naturalness,… **Limit:** Enrollment, labels, languages, metrics, and unseen-speaker protocol bound transfer.
- [REWIND: Speech Time Reversal for Enhancing Speaker Representations in Diffusion-based Voice Conversion](https://www.isca-archive.org/interspeech_2025/biyani25_interspeech.html) (D3): Use time-reversed speech as an augmentation: it removes much of the linguistic structure while retaining speaker-related cues, then use the resulting representations in diffusion-based voice conversion. **Measured or tested:** The effectiveness of the proposed approach is evaluated in the context of state-of-the-art diffusion-based VC models. **Limit:** Time reversal may remove more or less information depending on language and model; the experiments do not establish universal speaker/language disentanglement or human identity judgments across populations. No independent reproduction was performed.
- [DAFMSVC: One-Shot Singing Voice Conversion with Dual Attention Mechanism and Flow Matching](https://www.isca-archive.org/interspeech_2025/chen25d_interspeech.html) (D3): Replace source features with similar target-speaker features, fuse speaker/melody/content through dual attention, and use flow matching to generate the waveform. **Measured or tested:** To address these challenges, we propose DAFMSVC, where the self-supervised learning (SSL) features from the source audio are replaced with the most similar SSL features from the target audio to prevent timbre leakage. **Limit:** Singer, song, target-reference duration, feature retrieval, evaluation metrics, and dataset splits bound the result; one-shot similarity does not prove perfect disentanglement or generalization to every unseen singer.

**Where this boundary stops.** A short recording can encode noise, emotion, or demographic stereotypes rather than stable identity.; Conversion may leak source identity, distort pronunciation, or require target-speaker data unavailable in practice.; Similarity on a benchmark does not establish consent, identity security, or robustness to unusual voices.

**What this evidence does not establish.** The shared story is supported only by the reviewed papers listed here; D2 entries support the problem and stated method, while D3 entries support the reported mechanism and evaluation. It is not a venue-wide prevalence claim.

**Question left open.** What changes when this move is tested outside the speakers, languages, rooms, devices, or benchmark conditions represented by the 17 D3 paper(s)?

## Changing style, timing, and response behavior

**The question.** What ordinary speech pressure is handled by changing style, timing, and response behavior, and what evidence distinguishes it from neighboring pressures?

**How this boundary is derived.** Baseline link: Fant pp. 2-3: production passes through message, sentence form, motor activity, and acoustic processes; a generator must keep these layers aligned. Ordinary pressure: A useful synthetic voice must say the requested content, sound like the intended speaker or style, and remain understandable as it changes over time. Failed shortcut: Copying a recording or predicting samples directly entangles words with identity, pitch, rhythm, and recording conditions, making controlled change difficult. Recurring paper move: Represent or condition distinct factors, generate a time-consistent waveform or acoustic sequence, and evaluate each requested property separately. Neighbor test: The system must obey expressive controls quickly without breaking continuity or meaning.

**What the papers share.** A useful synthetic voice must say the requested content, sound like the intended speaker or style, and remain understandable as it changes over time. The subtheme asks: What ordinary speech pressure is handled by changing style, timing, and response behavior, and what evidence distinguishes it from neighboring pressures?

**Why the shortcut fails.** A first attempt would answer the question only with prosody control, but that shortcut misses the boundary: Independent controls can conflict; expressive variation may change perceived meaning or naturalness.

**The recurring move.** Across this subtheme, papers make prosody control, style and emotion control, interactive generation latency explicit rather than treating the speech evidence as one undifferentiated variable. The reviewed full-paper mechanisms instantiate that move in different ways; for example: Collect separate listener judgments of naturalness and similarity and examine which prosodic properties, including dynamic pitch variation, explain the gap.

### Words used in this section

**Prosody control.** Set or predict pitch, duration, energy, and pauses so the same words can sound questioning, emphatic, calm, or urgent.
*Boundary:* Independent controls can conflict; expressive variation may change perceived meaning or naturalness.

**Style and emotion control.** Condition generation on a speaking style or affective target while preserving the requested content.
*Boundary:* Emotion categories are culturally and contextually unstable, and a label may not describe what listeners perceive.

**Interactive generation latency.** Produce speech quickly enough for a conversation while preserving continuity and allowing interruption or correction.
*Boundary:* Low latency can require shorter context, lower quality, or speculative output that must later be repaired.

### What the papers show

- [Finding the Human Voice in AI: Insights on the Perception of AI-Voice Clones from Naturalness and Similarity Ratings](https://www.isca-archive.org/interspeech_2025/bakkouche25_interspeech.html) (D3): Collect separate listener judgments of naturalness and similarity and examine which prosodic properties, including dynamic pitch variation, explain the gap. **Measured or tested:** To address this, we conducted two behavioural tasks, evaluating listeners’ ratings of naturalness and similarity for human speech, three AI voice clones (ElevenLabs, StyleTTS-2, XTTS-v2), and a 30% F0 variation condition. **Limit:** Listener population, prompts, voices, and rating protocol limit generalization; perceptual association does not establish that changing F0 alone fixes naturalness. No independent reproduction was performed.
- [Fine-Tuning Text-to-Speech Diffusion Models Using Reinforcement Learning with Human Feedback](https://www.isca-archive.org/interspeech_2025/chen25b_interspeech.html) (D3): Use the diffusion loss as a regularizer inside policy optimization so naturalness improvement remains tied to learned speech structure. **Measured or tested:** We evaluate DLPO on WaveGrad 2, a non-autoregressive diffusion-based TTS model. **Limit:** The evidence uses WaveGrad 2 and selected reward predictors; predicted metrics and pairwise preference do not establish broad real-time deployment.
- [DiEmo-TTS: Disentangled Emotion Representations via Self-Supervised Distillation for Cross-Speaker Emotion Transfer in Text-to-Speech](https://www.isca-archive.org/interspeech_2025/cho25b_interspeech.html) (D3): Distill speaker-independent emotion representations with cluster sampling, perturbation, and separate style/identity conditioning. **Measured or tested:** Cross-speaker emotion transfer is evaluated with five-point naturalness, speaker-similarity, and emotion-similarity MOS, Whisper-Large WER/CER, WavLM speaker cosine similarity, and Emotion2Vec emotion similarity. Twenty participants rate two random samples per emotion for each evaluation speaker;… **Limit:** Pretrained encoders, datasets, subjective measures, and cross-speaker coverage bound the conclusion.
- [VibE-SVC: Vibrato Extraction with High-frequency F0 Contour for Singing Voice Conversion](https://www.isca-archive.org/interspeech_2025/choi25e_interspeech.html) (D3): Separate high-frequency F0 variation with a wavelet transform, then explicitly transfer and control the vibrato component during conversion. **Measured or tested:** Both subjective and objective evaluations confirm high-quality conversion. **Limit:** Singers, songs, vibrato ranges, extraction errors, and evaluation conditions limit generalization; explicit control does not guarantee a preferred artistic result.

**Where this boundary stops.** Independent controls can conflict; expressive variation may change perceived meaning or naturalness.; Emotion categories are culturally and contextually unstable, and a label may not describe what listeners perceive.; Low latency can require shorter context, lower quality, or speculative output that must later be repaired.

**What this evidence does not establish.** The shared story is supported only by the reviewed papers listed here; D2 entries support the problem and stated method, while D3 entries support the reported mechanism and evaluation. It is not a venue-wide prevalence claim.

**Question left open.** What changes when this move is tested outside the speakers, languages, rooms, devices, or benchmark conditions represented by the 20 D3 paper(s)?

## Closing note

This essay is a map of recurring problems and research moves, not a leaderboard or a claim that these categories cover every speech study. The paper links and depth labels show what was actually checked; they do not turn reported results into independent facts.
