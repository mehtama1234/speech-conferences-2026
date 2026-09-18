# INTERSPEECH 2025 fifty-eighth-pass full-paper notes

Eight official-PDF readings deepen five previously lowest-coverage subthemes: adaptation, sequence boundaries, room/channel evidence, speaker variation, and time-frequency coding.

## 1. adaptation-and-open-vocabulary

**Paper:** [Effects of Speaker Count, Duration, and Accent Diversity on Zero-Shot Accent Robustness in Low-Resource ASR](https://www.isca-archive.org/interspeech_2025/yong25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `6bbdf407c9f054962be570e20a7ff1c7c7916a082c378962b2dafe1c6c0cf224`; full text captured.

- **Ordinary problem:** Low-resource ASR should generalize to accents not represented in training data.
- **Why hard:** Speaker count, hours per speaker, and accent diversity are confounded when the total training budget is fixed.
- **Naive attempt:** Add hours from a few speakers and assume more accent labels alone will guarantee unseen-accent robustness.
- **Central move:** Factor the training-data budget by speaker count, per-speaker duration, and accent diversity, then test zero-shot accents.
- **Mechanism:** Controlled data-composition experiments compare ASR performance across unseen accents and languages.
- **Mathematical/conceptual structure:** Generalization is constrained by which speakers and accents supply the training evidence, not only by total audio hours.
- **What paper reports:** The paper reports that more speakers help more than more hours per speaker, while accent-diversity gains are minimal under controlled speaker count.
- **Limits:** Languages, accent labels, low-resource budgets, model/training choices, and zero-shot evaluation bound transfer; this is not a universal data-collection law.

## 2. boundaries-and-sequence-structure

**Paper:** [What the Filler? Both ASR Systems and Humans Struggle More With Other Kinds of Disfluencies Than With Filler Particles](https://www.isca-archive.org/interspeech_2025/wepner25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `971503f9d8ab2eb0d22459b7a4c707db568a2fe51b8f2c3b23cdbcd4b93b0e59`; full text captured.

- **Ordinary problem:** Conversational ASR and human transcription should account for syntactic disfluencies and filler particles.
- **Why hard:** Pauses, repairs, pronunciation, and articulation rate interact, so a global WER can hide which local structures cause errors.
- **Naive attempt:** Collapse all disfluencies into fluent text or treat filler presence as the sole explanatory variable.
- **Central move:** Present the same disfluent utterances to human listeners and multiple ASR systems, and compare error patterns across structure and acoustic factors.
- **Mechanism:** The matched transcription experiment uses participant recall and ASR WER to compare shared difficulty patterns.
- **Mathematical/conceptual structure:** Disfluency is sequence evidence: preserving its position and type lets recognition error be related to conversational structure.
- **What paper reports:** The paper reports similar difficulty characteristics for humans and ASR and no WER effect from filler presence alone.
- **Limits:** 54 listeners, nine systems, utterance design, languages, and WER/recall definitions bound transfer; matched error patterns do not establish cognitive equivalence.

## 3. room-channel-and-sensing

**Paper:** [Effect of Noise Floor in Room Impulse Response on Speech Perception Under Spherical Harmonics-based Spatial Sound Reproduction](https://www.isca-archive.org/interspeech_2025/zhang25e_interspeech.html)
**Evidence:** D3; PDF SHA-256 `5d9cd458088ec9a3b1432a9261977f3d22139a6b6ce208e68a1ea5425f3d3186`; full text captured.

- **Ordinary problem:** Spatial sound reproduction should reproduce speech perception measured in real rooms.
- **Why hard:** Measured room impulse responses contain a noise floor that can create artificial late energy and alter intelligibility in reverberant spaces.
- **Naive attempt:** Use any measured RIR or truncate it mechanically and assume the rendered room remains perceptually faithful.
- **Central move:** Vary RIR noise floor and compare speech-in-noise listening in spherical-harmonic reproduction against the rooms where the RIRs were measured.
- **Mechanism:** The RIR encodes direct and reflected paths; its residual floor changes the rendered reverberant tail, which is tested through intelligibility comparisons.
- **Mathematical/conceptual structure:** Room reproduction is a channel-matching problem: the measurement’s noise floor is part of the rendered evidence unless controlled.
- **What paper reports:** The paper reports better reproducibility with low-noise-floor RIRs in highly reverberant rooms and at 5 m, while truncation usually did not help.
- **Limits:** Rooms, source distances, RIR measurement, listening protocol, and speech-in-noise task bound transfer; perceptual reproducibility is not exact physical localization.

## 4. speaker-characteristics

**Paper:** [Examining Test-Time Adaptation for Personalized Child Speech Recognition](https://www.isca-archive.org/interspeech_2025/shi25h_interspeech.html)
**Evidence:** D3; PDF SHA-256 `8ef705b043076cb0bebac2bbe985b5bde02fb6c6cbc746131ff1dcf8f98cd464`; full text captured.

- **Ordinary problem:** ASR should adapt to individual child speakers at test time without requiring transcript annotations.
- **Why hard:** Children differ acoustically and linguistically from adult pretraining data and from one another, making a single child-domain correction insufficient.
- **Naive attempt:** Fine-tune once on a pooled child corpus or use an unadapted adult model for every child.
- **Central move:** Apply unsupervised SUTA and SGEM test-time adaptation to off-the-shelf and child-fine-tuned ASR models and compare per-child results.
- **Mechanism:** The adaptation updates model behavior from incoming child speech at inference time, without target transcripts, and is evaluated against unadapted baselines.
- **Mathematical/conceptual structure:** Personalization is an online evidence problem: each child supplies a changing acoustic distribution rather than a fixed domain label.
- **What paper reports:** The paper reports average and per-child gains for both model types, with remaining limitations on non-linguistic child speech.
- **Limits:** Child corpus, adaptation methods, update stability, model family, and evaluation conditions bound transfer; average WER gains are not proof of safe continual deployment.

## 5. time-frequency-measurement

**Paper:** [LSPnet: an ultra-low bitrate hybrid neural codec](https://www.isca-archive.org/interspeech_2025/zhang25l_interspeech.html)
**Evidence:** D3; PDF SHA-256 `789f0e8890cb4177347bdf62eb0cc9afaba6357923251ce02426f681d60219d4`; full text captured.

- **Ordinary problem:** A 1.2 kbps speech codec should preserve intelligibility and quality under resource constraints.
- **Why hard:** Very-low-rate coding must preserve spectral envelope and waveform detail while avoiding the complexity of large end-to-end decoders.
- **Naive attempt:** Quantize conventional parameters more aggressively or use a high-quality neural codec whose compute and bitrate exceed the deployment budget.
- **Central move:** Combine LSP-based parametric coding, direct neural sample prediction, and joint STFT/cross-entropy training in a hybrid LPCNet-style codec.
- **Mechanism:** LSPs stabilize spectral-envelope quantization; the neural predictor models sample distributions; time-frequency losses jointly constrain local waveform and spectral behavior.
- **Mathematical/conceptual structure:** Codec design is a rate-distortion allocation across representations and resolutions, with complexity treated as a deployment constraint.
- **What paper reports:** The paper reports high speech quality at 1.2 kbps and lower complexity than compared end-to-end codecs.
- **Limits:** Datasets, bitrate, codec baselines, quality metrics, hardware, and real-time implementation bound transfer; reported quality is not proof for every channel or listener.

## 6. adaptation-and-open-vocabulary

**Paper:** [WCTC-Biasing: Retraining-free Contextual Biasing ASR with Wildcard CTC-based Keyword Spotting and Inter-layer Biasing](https://www.isca-archive.org/interspeech_2025/nakagome25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `7a6e4263a62e3c48b1f14b3f722453c1337e39ba2839ab5a56d17e8317b057c3`; full text captured.

- **Ordinary problem:** ASR should recognize rare contextual keywords without retraining whenever application vocabulary changes.
- **Why hard:** A fixed bias list can over-bias decoding, while conventional contextual biasing may miss keywords with variable or wildcard forms.
- **Naive attempt:** Retrain the recognizer for every keyword list or inject a static phrase list and accept false substitutions.
- **Central move:** Use wildcard CTC keyword spotting and inter-layer biasing to add contextual evidence at inference time without retraining.
- **Mechanism:** CTC keyword scores detect flexible keyword evidence; inter-layer bias signals steer decoding while retaining the base acoustic model.
- **Mathematical/conceptual structure:** Contextual biasing changes the prior over candidate words, so it must raise relevant rare words without overruling acoustic evidence.
- **What paper reports:** The paper reports retraining-free contextual recognition improvements using WCTC-Biasing.
- **Limits:** Keyword lists, wildcard design, domains, decoder thresholds, and test distributions bound transfer; contextual gains do not guarantee lower errors on arbitrary speech.

## 7. boundaries-and-sequence-structure

**Paper:** [Improving Cross-Attention based on Positional Alignment during Inference for Robust Long-form Speech Recognition](https://www.isca-archive.org/interspeech_2025/oh25c_interspeech.html)
**Evidence:** D3; PDF SHA-256 `8fd6e5266bcd9f9a54cd22e8b42afdc5202097e4d4638bd194ffe49eeaf8cc98`; full text captured.

- **Ordinary problem:** Long-form ASR should use positional context without losing local acoustic alignment.
- **Why hard:** Cross-attention can attend to misplaced encoder positions, especially as utterances grow, causing errors that a generic language prior cannot diagnose.
- **Naive attempt:** Use unmodified cross-attention or force a hard monotonic alignment that cannot accommodate timing variation.
- **Central move:** Add positional alignment to cross-attention at inference so attention scores favor acoustically corresponding positions during long-form decoding.
- **Mechanism:** Position-aware attention reshapes the correspondence between decoder states and encoder frames without changing the recognized content target.
- **Mathematical/conceptual structure:** Long-context decoding is a soft alignment problem: context helps only when its evidence remains tied to the relevant time region.
- **What paper reports:** The paper reports improved robust long-form recognition from inference-time positional alignment.
- **Limits:** Model, long-form segmentation, positional formulation, decoding settings, and evaluation corpora bound transfer; reported robustness is not universal streaming reliability.

## 8. room-channel-and-sensing

**Paper:** [Unified Microphone Conversion: Many-to-Many Device Mapping via Feature-wise Linear Modulation](https://www.isca-archive.org/interspeech_2025/ryu25b_interspeech.html)
**Evidence:** D3; PDF SHA-256 `e27b9ba57c6fbf6030e92b7a778a15ba1ff76dc7f4fc2165625fb12fa98611c9`; full text captured.

- **Ordinary problem:** A recognizer should tolerate microphone/device changes without collecting paired recordings for every device pair.
- **Why hard:** Device responses alter spectral evidence, and many-to-many conversion must preserve speech content while changing channel coloration.
- **Naive attempt:** Duplicate channels, apply generic stereo equalization, or train one converter separately for every source-target pair.
- **Central move:** Learn a unified many-to-many microphone conversion model using feature-wise linear modulation to condition conversion on source and target devices.
- **Mechanism:** FiLM parameters modulate intermediate features according to device identities, allowing one model to represent multiple channel mappings.
- **Mathematical/conceptual structure:** Device conversion is a conditional channel transformation: content is shared while microphone response is the variable being controlled.
- **What paper reports:** The paper reports unified microphone conversion results across device mappings without paired examples for every target pair.
- **Limits:** Device inventory, pairing protocol, training coverage, content preservation metrics, and acoustic conditions bound transfer; channel conversion is not the same as recognizer invariance.

