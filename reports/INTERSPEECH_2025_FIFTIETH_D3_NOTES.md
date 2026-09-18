# INTERSPEECH 2025 fiftieth-pass full-paper notes

Eight official-PDF readings deepen human-centered evaluation, time-frequency measurement, room/channel sensing, source separation, and dialogue latency.

## 1. human-centered-evaluation

**Paper:** [Processing of grammatical information in cochlear implant simulated speech by German adult listeners](https://www.isca-archive.org/interspeech_2025/schouwenaars25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `e14d07175bb97a319d103dd6ce886cd8df6ca812d5d511e36120fb2d89419970`; full text captured.

- **Ordinary problem:** A listener using a cochlear implant or a simulated cochlear implant must recover grammatical structure from a spectrally degraded speech signal.
- **Why hard:** The signal degradation can remove cues that distinguish subject, object, and passive questions, while working memory and grammatical case interact with what the listener can use.
- **Naive attempt:** Assume that good performance on normal speech transfers unchanged to the simulated implant condition.
- **Central move:** Compare normal and CI-simulated speech with eye-tracking, accuracy, and working-memory measures so evaluation reflects both the answer and the listener's processing path.
- **Mechanism:** German adults answer subject, object, and passive which-questions. Eye movements and response accuracy expose whether case and subject-verb agreement cues survive the simulation; mixed-effects analyses relate performance to working memory.
- **Mathematical/conceptual structure:** Accuracy and gaze behavior are behavioral proxies for comprehension; the comparison is between normal and CI-simulated acoustic conditions rather than between two recognition models.
- **What paper reports:** Only object-question accuracy was affected by the simulation, with weaker interpretation preferences in gaze patterns; higher working memory was associated with better accuracy and faster reorientation.
- **Limits:** The simulation is not an actual implant, the German grammatical system and question types are narrow, and listener behavior does not establish clinical device benefit or general speech recognition performance.

## 2. human-centered-evaluation

**Paper:** [Concurrent Speech and Auditory Tag Clouds for Non-Visual Web Interaction](https://www.isca-archive.org/interspeech_2025/merzougui25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `8cc93a7f3bd56e9d84e198404df0db56e3589bf021f8a17896a0d8de9eda229b`; full text captured.

- **Ordinary problem:** A blind or visually impaired reader needs to skim a structured web document without relying on a visual page layout.
- **Why hard:** Transposing headings, roles, and relationships into sound can overload serial listening; the interface must preserve structure while allowing rapid selective attention.
- **Naive attempt:** Read the page linearly from top to bottom or emit every element with equal salience.
- **Central move:** Represent document semantics as an interactive auditory tag cloud, using concurrent speech and spatial/continuous auditory guidance to let the listener scan and select structure.
- **Mechanism:** TagThunder extracts morpho-dispositional semantics and maps tags to concurrent speech streams and guiding stimuli; discrete and continuous interaction conditions test structured information scanning.
- **Mathematical/conceptual structure:** The system treats auditory channels as a limited display: timing, concurrency, and user selection determine which semantic items are attended rather than merely transcribed.
- **What paper reports:** The paper presents the experimental framework and reports feasibility for non-visual web skimming through auditory tag-cloud interaction.
- **Limits:** The evaluation is interaction-specific, auditory clutter and learning effects matter, and accessibility promise is not equivalent to demonstrated performance across blind users, browsers, languages, or real browsing tasks.

## 3. time-frequency-measurement

**Paper:** [Functional Connectivity and Hilbert-Based Features for Covert Speech EEG Variability Analysis and Classification](https://www.isca-archive.org/interspeech_2025/duraisamy25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `49e6f75cfe73490b95607f60ada962470a539739585aad48039c1bebf1fd724f`; full text captured.

- **Ordinary problem:** A brain-computer interface may need to distinguish imagined or covert speech when no acoustic waveform is available.
- **Why hard:** EEG varies across trials, words, affective states, and people; phase and connectivity information can be lost when the signal is reduced to a single amplitude feature.
- **Naive attempt:** Train one subject-specific classifier on raw EEG and assume its spectral pattern transfers to another speaker.
- **Central move:** Represent covert speech with Hilbert envelopes, instantaneous phase, and functional connectivity across frequency bands, then train a subject-independent sequence classifier.
- **Mechanism:** Phase Locking Value and coherence summarize coordination among EEG channels. Band-specific Hilbert features feed a BiLSTM, while inter-trial, inter-class, and inter-subject analyses separate stable structure from variability.
- **Mathematical/conceptual structure:** The features are functions of analytic-signal phase and amplitude; classification accuracy measures whether the learned representation separates five speech-command categories across subjects.
- **What paper reports:** The reported subject-independent model reaches 59.14% accuracy across five covert-speech categories and reveals both shared and class-specific connectivity patterns.
- **Limits:** Covert speech EEG is not ordinary spoken audio, sample and subject variability constrain the result, class accuracy is not communicative utility, and no independent execution was performed.

## 4. time-frequency-measurement

**Paper:** [Band-Split Self-supervised Mamba for Infant-centered Audio Analysis](https://www.isca-archive.org/interspeech_2025/fan25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `b22901a6c5741f8bfd3a5f5b12e10378a50dcca93b2888867a7b9e7200a43acf`; full text captured.

- **Ordinary problem:** Infant-worn recordings contain long, varied home soundscapes in which infant vocalizations and caregiver interaction must be recognized with little labeled data.
- **Why hard:** Events occupy different frequency bands and time scales, recordings are noisy and weakly annotated, and a single full-band representation can waste capacity on irrelevant variation.
- **Naive attempt:** Learn one monolithic audio embedding or train a supervised model only on the small labeled set.
- **Central move:** Split the spectrum into bands, learn band-specific projections, and let a band-agnostic Mamba encoder model temporal relations while self-supervised pretraining uses unlabeled in-domain audio.
- **Mechanism:** Band-specific features preserve local spectral evidence while the state-space sequence model carries information over time; self-supervised and supervised objectives share the representation before downstream classification.
- **Mathematical/conceptual structure:** The system compares classification and representation-learning performance under limited labels, with band ablations testing whether multi-resolution structure matters.
- **What paper reports:** BS-SSAMBA improves infant-centered audio analysis in the reported experiments and benefits from combining unlabeled in-domain audio with limited annotations.
- **Limits:** Infant audio is adjacent to, not identical with, human speech; task labels, home environments, class balance, and domain-specific data bound transfer to adult speech systems.

## 5. room-channel-and-sensing

**Paper:** [Recreating Neural Activity During Speech Production with Language and Speech Model Embeddings](https://www.isca-archive.org/interspeech_2025/khanday25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `d763f07741caadf63a30595145295d4693820fa54d5670bb5c78df70df74d5bc`; full text captured.

- **Ordinary problem:** Neural recordings during speech production contain information about linguistic and acoustic planning before or alongside the sound that reaches a microphone.
- **Why hard:** High-gamma activity is spatially and temporally structured, while model embeddings compress speech and language differently; a useful embedding must preserve the neural dynamics rather than just correlate with a label.
- **Naive attempt:** Predict neural activity from word IDs or a generic acoustic feature and ignore timing, cortical location, and representational level.
- **Central move:** Use pretrained language and speech-model embeddings as regressors for high-gamma activity, then compare how linguistic and acoustic representations reconstruct spatio-temporal neural signals.
- **Mechanism:** Embedding vectors are aligned to neural time windows and mapped to high-gamma responses; reconstruction quality is evaluated across electrodes, time, and representational sources.
- **Mathematical/conceptual structure:** The paper treats a learned embedding as a hypothesis about what information is available to the brain, and reconstruction error/correlation as a test of that information's neural correspondence.
- **What paper reports:** Language and speech embeddings reconstruct measurable neural activity characteristics, with differences across model type and brain locations reported as evidence about linguistic versus acoustic information.
- **Limits:** Neural recordings, participant count, electrode coverage, alignment choices, and correlational reconstruction limit causal interpretation; a good reconstruction is not a speech decoder or clinical interface.

## 6. room-channel-and-sensing

**Paper:** [Low Complex IIR Adaptive Hear-Through Ambient Filtering for Overcoming Practical Constraints in Earbuds](https://www.isca-archive.org/interspeech_2025/gupta25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `6c36ac07027d357e63eda74ebda7b1cf108eddfd46f045e7446e2318ebd885a3`; full text captured.

- **Ordinary problem:** An earbud should make outside speech, horns, and alarms sound as if the ear were open, despite passive attenuation and changing fit or source direction.
- **Why hard:** The filter must compensate a user- and direction-dependent acoustic path with low delay, while adaptive IIR filters can become unstable and FIR filters can be expensive.
- **Naive attempt:** Use one fixed equalizer or a high-order adaptive FIR and accept mismatch, computation, or latency.
- **Central move:** Estimate a virtual sensing path and adapt a low-complexity IIR hear-through filter with stability-aware updates for different earbud fittings and directions.
- **Mechanism:** The virtual sensor models the sound pressure at the eardrum; an adaptive IIR filter updates the feedforward path, while constraints on poles/coefficients prevent unstable compensation. Indoor and outdoor acoustic simulations test convergence and delay.
- **Mathematical/conceptual structure:** Mean-square error, SNR, filter complexity, and processing delay expose the trade-off between matching the open-ear response and maintaining real-time stability.
- **What paper reports:** The proposed low-complexity IIR method reports improved hear-through performance under practical constraints and reduced complexity relative to larger adaptive alternatives.
- **Limits:** The evidence is simulation-heavy and depends on acoustic-path and fitting assumptions; user listening, hardware latency, and individualized hearing benefit are not established.

## 7. source-separation-and-spatial-listening

**Paper:** [Fine-tune Before Structured Pruning: Towards Compact and Accurate Self-Supervised Models for Speaker Diarization](https://www.isca-archive.org/interspeech_2025/han25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `f07840e4bddc8d1f261e9f887b9887153d7408cd6a7b3b6393893917e3b62226`; full text captured.

- **Ordinary problem:** A diarization system must assign speech segments to speakers in far-field meetings while fitting on hardware with limited memory and compute.
- **Why hard:** Self-supervised encoders contain redundant parameters, but pruning too aggressively can destroy the representations needed when speakers overlap, reverberation is present, or microphones differ.
- **Naive attempt:** Prune the pretrained encoder immediately and hope a small model preserves the full model's speaker boundaries.
- **Central move:** Fine-tune the self-supervised WavLM model on diarization before structured pruning, and use knowledge distillation to preserve the task behavior while removing redundant structure.
- **Mechanism:** The teacher supplies representations or logits for the student; structured channel/layer removal creates a compact model, and diarization error rate on far-field meeting corpora measures the retained segmentation and attribution ability.
- **Mathematical/conceptual structure:** The central object is a constrained compression path: task adaptation changes which parameters matter before pruning, while distillation penalizes deviation from the adapted teacher.
- **What paper reports:** On AMI, AISHELL-4, and AliMeeting, the paper reports that fine-tuning before pruning improves the accuracy/size trade-off over pruning without that order.
- **Limits:** Dataset microphone layouts, pruning ratios, teacher/student settings, and DER's treatment of overlap bound the claim; compact diarization is not universal robustness or real-device validation.

## 8. dialogue-and-turn-taking

**Paper:** [Dialogue Response Prefetching Based on Semantic Similarity and Prediction Confidence of Language Model](https://www.isca-archive.org/interspeech_2025/mori25b_interspeech.html)
**Evidence:** D3; PDF SHA-256 `33706d6c9e52b1da5ade1bedbf2ddc81c95c429bd833abd9f2c5df628d5833df`; full text captured.

- **Ordinary problem:** A spoken dialogue system can prepare a response before the user finishes, but a wrong early prediction can waste computation or create a visibly incorrect reply.
- **Why hard:** The partial utterance is incomplete and ambiguous; latency savings matter only when the predicted completion is semantically close enough to the final utterance.
- **Naive attempt:** Always prefetch from the current partial transcript or never prefetch until the user stops speaking.
- **Central move:** Predict the complete utterance early, estimate semantic similarity and confidence between the prediction and eventual utterance, and prefetch only when the confidence threshold makes the latency/rollback trade-off worthwhile.
- **Mechanism:** A prediction-confidence model compares embeddings or semantic representations of the predicted and completed user utterances; response latency and prediction correctness quantify when prefetching is safe.
- **Mathematical/conceptual structure:** The decision is selective rather than binary: the system estimates expected utility under uncertainty, trading saved user-perceived latency against wrong-response risk.
- **What paper reports:** The paper reports that semantic-similarity confidence can reduce user-perceived latency while limiting unsafe prefetches in the tested spoken-dialogue setting.
- **Limits:** The language model, dialogue domain, confidence calibration, and endpointing assumptions constrain generalization; lower latency is not the same as better conversation or human trust.

