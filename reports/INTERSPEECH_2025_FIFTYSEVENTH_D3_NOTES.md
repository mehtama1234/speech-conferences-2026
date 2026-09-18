# INTERSPEECH 2025 fifty-seventh-pass full-paper notes

Eight new official-PDF readings extend accessibility evaluation, accent simulation, online enhancement, efficient decoding, target extraction, noise-robust TTS, training-free conversion, and listener-aware fluency measurement.

## 1. human-centered-evaluation

**Paper:** [Feature Importance across Domains for Improving Non-Intrusive Speech Intelligibility Prediction in Hearing Aids](https://www.isca-archive.org/interspeech_2025/zezario25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `44997af50fe10a8e1f66fa80bebcf47313f485c09c9f77cfe258401b248c6c8e`; full text captured.

- **Ordinary problem:** A hearing-aid system needs an intelligibility estimate without asking a listener to score every noisy utterance.
- **Why hard:** Human scores are expensive, while acoustic features, learned representations, and hearing-aid conditions expose different parts of the perceptual problem.
- **Naive attempt:** Feed one feature family into a regressor and treat its error as a complete measure of intelligibility.
- **Central move:** Estimate frame-level importance across spectral, temporal, and Whisper latent features, project each domain through those weights, and fuse them in an assessment model.
- **Mechanism:** FiDo produces domain-specific weighted representations before concatenation and regression; RMSE on intelligibility targets evaluates whether the weighting preserves listener-relevant evidence.
- **Mathematical/conceptual structure:** Feature selection is moved inside the representation: the model learns which moments and domains matter before the final proxy prediction.
- **What paper reports:** The paper reports that FiDo reduces MBI-Net+ RMSE from 26.10 to 24.11 and improves over the best 2023 Clarity Prediction Challenge system.
- **Limits:** Weakly supervised targets, hearing-aid/noise conditions, challenge split, proxy RMSE, and absence of a new listener study bound the claim; prediction is not equivalent to real-world access improvement.

## 2. accent-and-cultural-boundaries

**Paper:** [Prosodically Enhanced Foreign Accent Simulation by Discrete Token-based Resynthesis Only with Native Speech Corpora](https://www.isca-archive.org/interspeech_2025/onda25b_interspeech.html)
**Evidence:** D3; PDF SHA-256 `0f2e603c321ce4ead5e22996886a29435b630a0740dd43ad9d5f35059efab9aa`; full text captured.

- **Ordinary problem:** Training and listening materials should expose learners and recognizers to foreign accents that are scarce in native-speech corpora.
- **Why hard:** Accent changes segmental realization and rhythm; a system that changes only discrete phonetic tokens can miss duration patterns characteristic of the speaker’s first language.
- **Naive attempt:** Use native speech unchanged or resynthesize token content without modeling timing, then call the result an accent simulation.
- **Central move:** Add explicit duration modification to discrete-token resynthesis so native speech can approximate durational foreign-accent cues without accented training data.
- **Mechanism:** Self-supervised discrete units preserve linguistic content, while duration controls alter timing before the units are rendered by a decoder; real L2 speech supplies the comparison target.
- **Mathematical/conceptual structure:** Accent simulation is a structured transformation: content units should stay stable while temporal realization changes in a language-specific way.
- **What paper reports:** The paper reports that the enhanced method reproduces durational accents observed in real L2 speech.
- **Limits:** Accent languages, speakers, duration estimator, perceptual validation, and native-corpus assumptions bound transfer; acoustic similarity is not proof of improved ASR or pedagogy.

## 3. noise-enhancement

**Paper:** [Diffusion Buffer: Online Diffusion-based Speech Enhancement with Sub-Second Latency](https://www.isca-archive.org/interspeech_2025/lay25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `a824112d710784820ae0c7e5496d022f713793c1fd3a9219735b68d7cec43923`; full text captured.

- **Ordinary problem:** Live communication needs speech enhancement while the signal is still arriving, with latency small enough for interaction.
- **Why hard:** Diffusion models can restore complex distributions but normally require many iterative steps and future context, conflicting with streaming constraints.
- **Naive attempt:** Run an offline diffusion enhancer or use a fast deterministic model that sacrifices generative restoration quality.
- **Central move:** Use a sliding buffer whose corruption schedule gives more noise to frames near the present, then denoise older frames with a controlled delay.
- **Mechanism:** The buffer defines a causal-to-delayed window; diffusion steps operate on that window and output frames once their future context is sufficient.
- **Mathematical/conceptual structure:** Latency becomes a tunable information budget: a larger buffer gives the score-based model more context while increasing input-output delay.
- **What paper reports:** The paper reports better results than standard diffusion baselines and GPU input-output latency around 0.3–1 seconds.
- **Limits:** GPU/hardware assumptions, buffer size, noise mixtures, real-time scheduling, and perceptual metrics bound the result; a reported latency range is not a full conversational user study.

## 4. robustness-and-system-boundary

**Paper:** [Simultaneous Masked and Unmasked Decoding with Speculative Decoding Masking for Fast ASR without Accuracy Loss](https://www.isca-archive.org/interspeech_2025/okabe25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `bbd4d7f3fdddc859f36b511b2865446d122f4492d04dd4dcf6249675163b1aa3`; full text captured.

- **Ordinary problem:** An ASR decoder should approach autoregressive accuracy without paying for every sequential token decision.
- **Why hard:** Non-autoregressive guesses are fast but can lose accuracy, while autoregressive search repeatedly computes scores for hypotheses that are already predictable.
- **Naive attempt:** Choose either full autoregressive beam search or a non-autoregressive decoder and accept the speed-accuracy tradeoff.
- **Central move:** Combine simultaneous masked/unmasked decoding with speculative masking so confidently predictable hypotheses skip unnecessary decoder computation.
- **Mechanism:** Preliminary masked decisions identify positions whose score computation can be omitted; the remaining positions retain the autoregressive search path and its result.
- **Mathematical/conceptual structure:** The method exploits conditional redundancy in sequence search: computation is spent where uncertainty remains rather than uniformly at every token.
- **What paper reports:** On TED-LIUM2, the paper reports WER 7.3% for both the proposed and autoregressive systems, with RTF 0.41 versus 0.59.
- **Limits:** One corpus/model, beam and hardware settings, confidence thresholds, and real-time measurement protocol bound transfer; equal WER on one test set does not prove universal speed preservation.

## 5. source-separation-and-spatial-listening

**Paper:** [FlowTSE: Target Speaker Extraction with Flow Matching](https://www.isca-archive.org/interspeech_2025/navon25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `38e9684b3f92cdbd235a5733e2e11a1a7311dd333b32418ef4467ecbe6297310`; full text captured.

- **Ordinary problem:** A listener should extract one enrolled speaker from a mixture even when interference is severe or unseen.
- **Why hard:** Discriminative masks can create artifacts and fail under distribution shift, while generative pipelines often require multiple pretrained components and poor phase reconstruction.
- **Naive attempt:** Map the mixture directly to a mask or waveform with a large pipeline, ignoring the enrolled speaker’s distribution and phase evidence.
- **Central move:** Condition flow matching on enrollment and mixture mel-spectrograms, and condition a vocoder on the mixture’s complex STFT when phase matters.
- **Mechanism:** A learned flow transports a noisy conditional distribution toward target speech; complex-STFT conditioning supplies phase information that mel features discard.
- **Mathematical/conceptual structure:** Target extraction is conditional generation under an identity constraint, with magnitude and phase treated as complementary evidence.
- **What paper reports:** The paper reports that FlowTSE matches or outperforms strong target-speaker-extraction baselines on standard benchmarks.
- **Limits:** Enrollment quality, speaker/noise shift, phase-vocoder design, benchmark mixtures, and signal metrics bound transfer; extraction quality is not automatically improved ASR or hearing-aid benefit.

## 6. text-to-speech-and-content

**Paper:** [Improving Noise Robustness of LLM-based Zero-shot TTS via Discrete Acoustic Token Denoising](https://www.isca-archive.org/interspeech_2025/lu25b_interspeech.html)
**Evidence:** D3; PDF SHA-256 `e57916bc48423e54ff4b5ad9e960bc5877ca74f220bf3670e2b57039a7d7d805`; full text captured.

- **Ordinary problem:** Zero-shot TTS should preserve a speaker’s identity when the few-second audio prompt is noisy.
- **Why hard:** Noise corrupts acoustic tokens and can cause an LLM-based TTS system to copy the environment or plan the wrong voice, while ordinary enhancement may not match token-level prompts.
- **Naive attempt:** Enhance the prompt with a generic speech enhancer or trust the noisy codec tokens as if they represented clean speaker evidence.
- **Central move:** Denoise the first acoustic-token groups with a neural codec token predictor, refine the embedding, and use the cleaned prompt in LauraTTS.
- **Mechanism:** The token denoiser predicts clean coarse tokens; an embedding refiner and codec decoder reconstruct usable acoustic evidence before the zero-shot TTS model conditions generation.
- **Mathematical/conceptual structure:** Denoising at the representation used for prompting aligns the cleanup objective with the generator’s actual conditioning interface.
- **What paper reports:** The paper reports that its codec denoiser outperforms speech-enhancement baselines and that noise-robust LauraTTS improves over adding an external enhancer.
- **Limits:** Noise types, prompt duration, speaker overlap, codec/model version, and zero-shot evaluation bound transfer; clean synthesis from a prompt is not speaker-authenticated identity preservation.

## 7. voice-identity-and-conversion

**Paper:** [Training-Free Voice Conversion with Factorized Optimal Transport](https://www.isca-archive.org/interspeech_2025/lobashev25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `6fd2ba5677f7cded0f454f0ac89c66f92ff85fca5051811ae77a82bf0e414220`; full text captured.

- **Ordinary problem:** Any-to-any voice conversion should change identity from a short reference while preserving the source linguistic content, including across languages.
- **Why hard:** Nearest-neighbor replacement needs long reference recordings and can import language-specific artifacts; training a new converter per speaker defeats the any-to-any goal.
- **Naive attempt:** Replace each source embedding with its closest target embedding and assume five minutes of reference speech is always available.
- **Central move:** Replace nearest-neighbor matching with a factorized optimal-transport map in WavLM embedding subspaces, requiring only a short reference.
- **Mechanism:** Monge–Kantorovich linear transport aligns source and target feature distributions; factorization normalizes unequal variances before the encoder-converter-vocoder reconstructs speech.
- **Mathematical/conceptual structure:** Optimal transport matches distributions rather than individual frames, allowing sparse reference evidence to define a target voice without storing a lookup for every source sound.
- **What paper reports:** MKL-VC reports improved content preservation and short-reference robustness on LibriSpeech and FLEURS, with cross-lingual performance comparable to FACodec.
- **Limits:** Reference duration, WavLM space, languages, vocoder, speaker similarity metric, and implementation choices bound transfer; content preservation does not prove perfect identity conversion.

## 8. human-centered-evaluation

**Paper:** [A Bayesian Approach to L2 Fluency Ratings by Native and Nonnative Listeners](https://www.isca-archive.org/interspeech_2025/yazawa25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `b90a77c89758bc8bc5cdfd3005b0ab226af97f66b363ba303a1d698b662a2c04`; full text captured.

- **Ordinary problem:** Fluency ratings of second-language speech should reflect both the speaker’s temporal behavior and the listener’s linguistic background.
- **Why hard:** Listeners disagree, and native-listener norms may not transfer to nonnative listeners; rate, pauses, and repairs are correlated rather than independent cues.
- **Naive attempt:** Average all ratings or use a single syllable-rate predictor and treat the resulting score as a universal fluency scale.
- **Central move:** Use a Bayesian hierarchical model to separate listener variability from utterance-level fluency cues and compare syllable- versus segment-based articulation rate.
- **Mechanism:** Posterior distributions represent listener-specific leniency and cue weights; speed, breakdown, and repair features explain ratings while uncertainty remains explicit.
- **Mathematical/conceptual structure:** Human evaluation is a multilevel measurement problem: the score is jointly produced by the speech sample and the observer’s perceptual prior.
- **What paper reports:** Using 16 listeners and 180 Japanese speakers in J-AESOP, the paper reports greater leniency among some nonnative listeners and stronger fit for segment-based articulation rate.
- **Limits:** Listener sample, language backgrounds, trained-rating task, corpus, feature definitions, and Bayesian priors bound transfer; fluency ratings are not a complete measure of communicative success.

