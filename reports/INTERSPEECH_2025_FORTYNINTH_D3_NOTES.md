# INTERSPEECH 2025 forty-ninth-pass full-paper notes

Eight official-PDF readings deepen grounding/action, human-centered evaluation, room/channel sensing, time-frequency measurement, and metric-target alignment.

## 1. grounding-and-action

**Paper:** [Spoken Question Answering for Visual Queries](https://www.isca-archive.org/interspeech_2025/shabtay25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `c836bb90b78d83905ab1062c34681d57abb38f2682fa7381a0c6a926cc13186b`; full text captured.

- **Ordinary problem:** A person wants to ask about an image using speech, while the answer must depend on what is visible rather than on the words alone.
- **Why hard:** Speech must be mapped to language while the image supplies the referent; an ASR error can change the question before the visual model sees it.
- **Naive attempt:** Transcribe the question first and hand the text to a text-only visual QA system, assuming speech contains no useful information beyond words.
- **Central move:** Align speech and image encoders directly into a VQA language model so spoken queries and visual evidence can jointly condition the answer.
- **Mechanism:** Whisper encodes speech and CLIP encodes images; modality-specific projectors align both representations with LLaVA's language space, with speech-only pretraining followed by joint spoken-VQA fine-tuning.
- **Mathematical/conceptual structure:** The model predicts an answer from a fused representation. Accuracy, ANLS, and MME scores compare the answer with the task-specific reference; WER separately exposes speech-to-text failure.
- **What paper reports:** Synthetic speech training approaches the text-trained VQA upper bound on several benchmarks; the paper reports 62% SEED-Bench accuracy for its strongest spoken variants, with TTS choice having a small effect.
- **Limits:** Most training speech is synthesized, the spoken models remain below the text model, prompt format changes performance sharply, and transcription failures can be confused with visual-reasoning failures. No independent reproduction was performed.

## 2. grounding-and-action

**Paper:** [Enhancing Speech Instruction Understanding and Disambiguation in Robotics via Speech Prosody](https://www.isca-archive.org/interspeech_2025/sasu25b_interspeech.html)
**Evidence:** D3; PDF SHA-256 `64216ffe7765b03bd814c0f58520e206b52d0df912e8a3488d2b5e93c880911e`; full text captured.

- **Ordinary problem:** A robot can hear the same words but need different physical plans depending on which object or relation the speaker emphasizes.
- **Why hard:** ASR preserves much of the lexical content but discards stress, rhythm, pauses, and intonation that distinguish competing interpretations.
- **Naive attempt:** Transcribe the instruction, parse the text, and let a language model choose a plan from the words alone.
- **Central move:** Predict token-level goal/detail referents from prosody, then inject those intent cues into an LLM that selects the robot task plan.
- **Mechanism:** Prosodic and raw-audio features feed Transformer or BiLSTM sequence models trained with cross-entropy; predicted referents are placed in prompts for GPT-4o, o1-mini, or o3-mini to choose among plans.
- **Mathematical/conceptual structure:** The sequence model estimates a label distribution for each token; accuracy, precision, recall, and F1 measure referent detection, while plan accuracy measures the final discrete action choice.
- **What paper reports:** On 1,540 recordings from 22 participants, the best BiLSTM reaches 95.79% overall referent accuracy, and Prosody-Transformer plus GPT-4o reaches 71.96% task-plan accuracy versus 50% for the ASR-only prompt.
- **Limits:** The dataset is small and participants are 18–22; recorded ambiguity and candidate plans are controlled rather than open-world robot interaction. Prosody helps the tested task but does not establish safe execution in physical environments.

## 3. human-centered-evaluation

**Paper:** [What Do Humans Hear When Interacting? Experiments on Selective Listening for Evaluating ASR of Spoken Dialogue Systems](https://www.isca-archive.org/interspeech_2025/mori25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `3b3247727d8efb9691672390584fbd69085efe011f5f83b11da771df2a1f488a`; full text captured.

- **Ordinary problem:** A dialogue system needs the words that matter for its response, not necessarily a verbatim transcript of every utterance.
- **Why hard:** WER weights function words and content words alike, while people selectively attend to content during response generation; a low WER can therefore hide a consequential miss.
- **Naive attempt:** Evaluate the front-end ASR with ordinary WER, treating every token as equally important.
- **Central move:** Observe selective listening in 297 human participants, estimate part-of-speech importance, and use those weights to form Human-WWER/H-WCER for dialogue-oriented ASR evaluation.
- **Mechanism:** Participants generate a response and then recall/transcribe the speech; multiple regression estimates POS weights, which are inserted into the edit-distance costs used by weighted WER.
- **Mathematical/conceptual structure:** A regression predicts the remembered POS counts from the full transcript; the resulting coefficients weight insertions, deletions, and substitutions in a minimum-edit-distance score. Five-fold validation compares MAE and R².
- **What paper reports:** Humans attend more to content words than function words; the proposed H-WWER gives lower scores to human than Whisper transcriptions in the reported comparison and is offered as a dialogue-relevant complement to WER.
- **Limits:** Transcription follows response generation rather than occurring simultaneously, and the displayed weight comparison is partly optimized on test data. The metric is a proposal, not validated against downstream response success or diverse dialogue settings.

## 4. human-centered-evaluation

**Paper:** [Accessible Delivery of Visual-Acoustic Biofeedback for Speech Sound Disorder](https://www.isca-archive.org/interspeech_2025/mcallister25b_interspeech.html)
**Evidence:** D3; PDF SHA-256 `389575b43bb2e0d05423a71a1789d3a633f0b03461c728de811d0e2f9f204f7e`; full text captured.

- **Ordinary problem:** A child practicing a difficult speech sound needs immediate, interpretable feedback that does not require a specialist or expensive equipment at every trial.
- **Why hard:** The learner must connect a changing acoustic spectrum to a vocal-tract target, while remote audio processing can add delay, lose frequency detail, or be distorted by browser processing.
- **Naive attempt:** Show a generic waveform or send audio through a video-call pipeline and expect the child to infer which articulatory change is needed.
- **Central move:** Make the source-filter structure visible: display a real-time LPC spectrum alongside a target resonance, with adaptive practice and clinician-mediated feedback.
- **Mechanism:** JavaScript computes LPC coefficients with Levinson-Durbin recursion, renders the spectral envelope and peaks, and supports randomized word/syllable routines, clinician scoring, gamification, and local-device WebRTC processing.
- **Mathematical/conceptual structure:** LPC models the signal as X(z)=H(z)E(z), with an all-pole vocal-tract filter H(z)=1/A(z); peak locations approximate formant resonances used as the feedback target.
- **What paper reports:** The staRt iOS/web system provides real-time visual-acoustic biofeedback for /r/ training and reports broad uptake; local processing avoids telepractice loss of frequency resolution and latency.
- **Limits:** The current target is mainly English /r/, peak-picking and formant tracking are not yet stable enough for automated feedback across vocal-tract sizes, and clinical efficacy is not established by this technical description.

## 5. room-channel-and-sensing

**Paper:** [Selective Auditory Attention Decoding in Naturalistic Conversations Using EEG-Based Speech Envelope Tracking in Multi-Speaker Environments](https://www.isca-archive.org/interspeech_2025/ivucic25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `267fd2ee224ce27dcb65638cb5f0c1406650b676dd63942965142cdaae2ca913`; full text captured.

- **Ordinary problem:** In a real conversation, a listener must switch between speakers while background talkers continue, and a neural interface would need to track the attended stream through those switches.
- **Why hard:** EEG responses are weak and delayed relative to acoustic envelopes; multiple speakers and changing attention make a static decoder an unsafe assumption.
- **Naive attempt:** Train one decoder on a fixed attended speaker and assume it remains valid when attention moves.
- **Central move:** Reconstruct each speech envelope from EEG with a time-lagged ridge model and identify the attended speaker by whichever reconstructed envelope correlates best.
- **Mechanism:** A multivariate linear model maps 62 EEG channels over 0–200 ms lags to speech-envelope samples; leave-one-trial-out validation compares Pearson correlations for target and distractor streams before and after exogenous switches.
- **Mathematical/conceptual structure:** The weights minimize squared reconstruction error plus λ||w||². Target selection is an argmax over envelope correlations; chance is 33% for the three-speaker comparison.
- **What paper reports:** Across 36 trials, target-speaker decoding averages 76% ± 12%; performance remains above chance as windows shrink from 20 seconds to 2 seconds, and reconstruction briefly rises after attention switches.
- **Limits:** The experiment uses controlled speakers and exogenous switches, short windows still perform poorly, EEG signal-to-noise limits real-time use, and neural decoding is not equivalent to robust everyday source separation.

## 6. room-channel-and-sensing

**Paper:** [French Listening Tests for the Assessment of Intelligibility, Quality, and Identity of Body-Conducted Speech Enhancement](https://www.isca-archive.org/interspeech_2025/joubaud25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `cc4b7fd2b5a1483a2a62be1dad563841ccaa55eef349cdd2d13d96282b236911`; full text captured.

- **Ordinary problem:** Body-conduction sensors survive loud environmental noise but remove or reshape spectral information, so an enhancement system must improve speech without changing who is speaking.
- **Why hard:** Intelligibility, perceived quality, and speaker identity are different targets; a bandwidth-extension model can improve one while damaging another, and objective metrics may not predict listeners.
- **Naive attempt:** Trust a single objective enhancement score as evidence that a sensor signal is intelligible, natural, and identity-preserving.
- **Central move:** Evaluate EBEN with separate listening tasks for intelligibility, quality, and identity, then correlate each human measure with candidate objective metrics across sensor types and sex.
- **Mechanism:** Forehead-accelerometer, rigid-in-ear, and throat-microphone signals from Vibravox are enhanced by EBEN; French Modified Rhyme Tests, MUSHRA, and A/B identification are compared with STOI, N-MOS, and ECAPA2 similarity.
- **Mathematical/conceptual structure:** Pearson correlation links metric values to listener outcomes; the test uses IQR outlier filtering, Shapiro-Wilk normality checks, and 95% significance thresholds.
- **What paper reports:** EBEN improves reported quality and intelligibility but slightly harms female throat-microphone identity; STOI correlates strongly with MUSHRA quality (ρ=.87) and ECAPA2 with identification (ρ=.90), while no tested metric reliably predicts intelligibility change.
- **Limits:** The study uses quiet recordings, selected sensors and speakers, one enhancement model, and finite listening tests. Correlation with a perceptual proxy does not establish general clinical or operational usefulness.

## 7. time-frequency-measurement

**Paper:** [Sub-band based Adaptive IIR Algorithm with Biquad Filter Stability Constraints for Feedforward Hear-Through Equalization](https://www.isca-archive.org/interspeech_2025/gupta25b_interspeech.html)
**Evidence:** D3; PDF SHA-256 `6597c0f8859668a9c2a930b108fdcc3479c1579ac2579fdf175e79ab00ae34aa`; full text captured.

- **Ordinary problem:** Transparent earbuds should reproduce the outside world while keeping processing delay low enough that the user does not hear a mismatch between direct and replayed sound.
- **Why hard:** Adaptive filtering must track changing source directions and room paths, but high-order FIR or neural filters cost delay; IIR filters are compact but can become unstable during adaptation.
- **Naive attempt:** Use a fixed filter or a large adaptive FIR and accept poor tracking, computational cost, or latency.
- **Central move:** Adapt a low-order sub-band IIR equalizer and enforce stability with a biquad/all-pass constraint based on the least-mean-square fourth criterion.
- **Mechanism:** The reference microphone signal is split into sub-bands; feedforward FxLMS/F adaptation updates IIR paths, while cascaded biquads compensate phase/group delay and constrain poles during changing indoor/outdoor conditions.
- **Mathematical/conceptual structure:** The filter minimizes an error criterion in sub-bands; the fourth-order LMS constraint penalizes unstable coefficient behavior. MSE, SNR, convergence, and multiply-accumulate counts expose the accuracy/latency/complexity trade-off.
- **What paper reports:** The paper reports up to 13 dB improvement over compared adaptive methods in simulated scenarios, with stable behavior and similar complexity in dynamic indoor/outdoor tests.
- **Limits:** The evidence is simulation-based and depends on acoustic paths, filter orders, and stability settings; user perception, individualized ears, and end-to-end hardware latency are not established.

## 8. metrics-and-targets

**Paper:** [Relationship between objective and subjective perceptual measures of speech in individuals with head and neck cancer](https://www.isca-archive.org/interspeech_2025/halpern25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `d669e9c5c2abd6b674c3c898cc8798103f979f59b68063abb4fab78bd47f3e24`; full text captured.

- **Ordinary problem:** Clinical speech monitoring needs measurements that are repeatable yet still mean what listeners experience as intelligibility, articulation, or voice quality.
- **Why hard:** Subjective ratings are expensive and variable, while objective acoustic measures can correlate with a broad severity factor rather than the specific speech dimension they claim to measure.
- **Naive attempt:** Validate one objective metric against one listener rating and treat a high correlation as proof that the metric isolates that percept.
- **Central move:** Measure several perceptual dimensions and objective proxies in longitudinal head-and-neck-cancer speech, then inspect their correlation structure for common-cause confounding.
- **Mechanism:** Trained listeners rate intelligibility, articulation, voice quality, phonation, rate, nasality, and noise; objective measures such as NAD, PCX, PER, SPEED, and SNR are compared using Pearson correlations across 53 Dutch participants.
- **Mathematical/conceptual structure:** The study treats Pearson r as alignment between a computational proxy and a perceptual target, but interprets correlated targets cautiously because shared treatment severity can induce multiple correlations.
- **What paper reports:** Subjective intelligibility correlates strongly with articulation (r=.95) and voice quality (r=.92); NAD correlates .90 with intelligibility, while phonation and nasality lack reliable objective counterparts in this cohort.
- **Limits:** The population is Dutch readers with head-and-neck cancer, not general speech; neural features are not fully interpretable, running spontaneous speech is absent, and correlation does not prove clinical decision validity.

