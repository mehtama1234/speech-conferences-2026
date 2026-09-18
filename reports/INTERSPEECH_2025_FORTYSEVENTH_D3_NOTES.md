# INTERSPEECH 2025 forty-seventh-pass full-paper notes

Eight official-PDF readings deepen device-directed boundaries, black-box confidence, affect geometry, non-human voice conversion, temporal captioning, streaming units, auditory feedback, and reference-free quality assessment.

## 1. boundaries-and-sequence-structure

**Paper:** [Adaptive Knowledge Distillation for Device-Directed Speech Detection](https://www.isca-archive.org/interspeech_2025/chi25b_interspeech.html)
**Evidence:** D3; PDF SHA-256 `e6a9df8f1888df042ebd63db16cacd62630b0003bfcef0b7eb3e723eca483f04`; full text captured.

- **Ordinary problem:** A voice assistant must tell when someone is addressing it instead of reacting to nearby conversation or background speech.
- **Why hard:** The detector must work with keyword and follow-up requests, run efficiently, and use a representation that transfers from broad speech recognition without confusing ordinary speech for a command.
- **Naive attempt:** Run a large acoustic model directly on every device or detect only a fixed wake word.
- **Central move:** Use adaptive knowledge distillation from a frozen ASR acoustic encoder, with task-specific adapters jointly trained with a smaller device-directed-speech student.
- **Mechanism:** The paper proposes adaptive knowledge distillation for device-directed speech detection.
- **Conceptual structure:** The assistant’s first decision is social and acoustic: before understanding words, it must infer whether the words are meant for it; general speech knowledge helps, but the invocation boundary needs task-specific evidence.
- **What paper reports:** The paper reports EER improvements of 26% for keyword and 19% for keyword-free follow-up invocations, with gains across transformer and conformer students.
- **Limits:** Invocation types, EER, teacher/student architectures, training data, and device conditions bound deployment claims; a benchmark detector cannot infer intent perfectly in every home.

## 2. metrics-and-targets

**Paper:** [CAPR: Confidence-Aware Prompt Refinement in Large Language Models](https://www.isca-archive.org/interspeech_2025/chien25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `e822c794e91273b4b3e44055c336883730eda95446e14673e8a1d322d5ec73fb`; full text captured.

- **Ordinary problem:** A language model should indicate when a long answer may be wrong, even when its internal probabilities are unavailable because it is a black-box service.
- **Why hard:** Confidence must track correctness rather than fluent style, and long-form answers contain many opportunities for one unsupported sentence to hide inside an apparently confident response.
- **Naive attempt:** Ask the black-box model for a confidence number or use a short-answer calibration method unchanged.
- **Central move:** Train a confidence-aware prompt refiner with external knowledge and rewards tied to answer confidence and accuracy, then use the refined prompt to elicit calibrated scores.
- **Mechanism:** CAPR is a confidence-aware prompt-refinement method for black-box long-form generation.
- **Conceptual structure:** Confidence is treated as an interaction design problem: a prompt can change the model’s observable behavior, but the resulting score is still an externally elicited proxy rather than direct access to belief.
- **What paper reports:** The paper reports more reliable confidence elicitation and calibrated responses in its long-form experiments.
- **Limits:** Question domains, external knowledge, black-box model, reward, calibration measure, and answer segmentation bound the claim; prompt-based confidence is not a guarantee of factuality.

## 3. prosody-and-intent

**Paper:** [EmoSphere-SER: Enhancing Speech Emotion Recognition Through Spherical Representation with Auxiliary Classification](https://www.isca-archive.org/interspeech_2025/cho25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `a078450f9f9dc00fb9b4442e3144993b28e6aa061f8fbc517a244131a6797743`; full text captured.

- **Ordinary problem:** Emotion is not just a class label: a listener may need to distinguish nearby positions in arousal, valence, and dominance without making unstable continuous predictions.
- **Why hard:** The three dimensions have geometry and uneven density; ordinary independent regression can ignore local structure and produce inconsistent points.
- **Naive attempt:** Regress each affect dimension independently and treat the output as equally reliable everywhere.
- **Central move:** Convert VAD values to spherical coordinates, classify spherical regions as an auxiliary task, dynamically weight objectives, and pool temporal style information.
- **Mechanism:** EmoSphere-SER uses spherical VAD-region classification to guide emotion regression.
- **Conceptual structure:** The model gives the affect space neighborhoods and a coarse location before asking for a precise coordinate, coupling classification’s stability with regression’s detail.
- **What paper reports:** The reported experiments show the combined model outperforming the compared baselines and improving prediction consistency.
- **Limits:** Emotion labels, VAD geometry, datasets, region partition, weighting, and metrics bound the result; a better coordinate prediction does not establish a speaker’s actual inner state.

## 4. voice-identity-and-conversion

**Paper:** [Unleashing   the  Inner Monster: Demonstrating High-Fidelity Human to Non-Human  Voice Conversion](https://www.isca-archive.org/interspeech_2025/cho25c_interspeech.html)
**Evidence:** D3; PDF SHA-256 `a61cec18b7ddede4960e2c0fb9f80823f3141d1058c488d9cabdaab6edc7ce0a`; full text captured.

- **Ordinary problem:** Game creators need convincing creature voices without recording and manually designing every non-human sound, while the result must remain controllable and fast enough for interaction.
- **Why hard:** Human speech features and vocal-tract assumptions do not directly describe a monster; conversion must move beyond speaker identity while preserving expressive timing and the target sound character.
- **Naive attempt:** Train ordinary human voice conversion and expect it to produce convincing non-human vocalizations.
- **Central move:** Record human vocalizations and convert them in real time with a human-to-non-human voice-conversion model designed around selected monster sounds.
- **Mechanism:** The paper demonstrates high-fidelity human-to-non-human voice conversion for games.
- **Conceptual structure:** Voice conversion can be reframed as changing the sound-producing agent, not merely swapping one human identity for another; the target is a designed acoustic character.
- **What paper reports:** The paper reports real-time conversion and high-quality generated monster sounds in its selected game-oriented conditions.
- **Limits:** Target creatures, recordings, real-time hardware, perceptual evaluation, and controllability bound the claim; a convincing effect is not a biological model of animal vocalization.

## 5. grounding-and-action

**Paper:** [Temp4Cap: Temporally-aligned Automated Audio Captioning](https://www.isca-archive.org/interspeech_2025/choi25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `f41e758ff7c100ca0353682a2a82c952127cb29695199228fa75b9003c0f3cac`; full text captured.

- **Ordinary problem:** A caption for a sound scene should say not only what happened but when events occurred and in what order.
- **Why hard:** A bag of detected events can produce a plausible sentence with the wrong temporal relation; negative examples must challenge both event identity and event ordering.
- **Naive attempt:** Generate a caption from pooled audio features or attach an independent event detector after caption generation.
- **Central move:** Train temporal alignment directly with contrastive learning, using language-model temporal captions and event/order shuffling plus substitutions as negatives.
- **Mechanism:** Temp4Cap is a temporally aligned automated audio-captioning framework.
- **Conceptual structure:** Meaning includes relations among events: the system must learn that ‘before,’ overlap, and after are structural constraints, not decorative words added after recognition.
- **What paper reports:** On Clotho and AudioCaps, the paper reports gains in captioning metrics and temporal metrics over the compared systems.
- **Limits:** Datasets, generated temporal captions, negative-sampling design, caption metrics, and temporal scoring bound the claim; metric gains do not ensure every relation is correctly grounded.

## 6. adaptation-and-open-vocabulary

**Paper:** [On-device Streaming Discrete Speech Units](https://www.isca-archive.org/interspeech_2025/choi25b_interspeech.html)
**Evidence:** D3; PDF SHA-256 `8ee6e6ed7092b62a31f86a6344fc77ff855a4e20648b15d5f69537015216ea80`; full text captured.

- **Ordinary problem:** A speech model on a device must start processing before the whole utterance arrives and must fit limited compute, while retaining useful phonetic information.
- **Why hard:** Discrete units derived from large self-supervised models are powerful but normally require long context and expensive feature extraction; reducing them risks recognition errors and lost history.
- **Naive attempt:** Wait for the full recording and run the largest self-supervised encoder on every frame.
- **Central move:** Shrink the attention window and model size for streaming discrete speech units, measuring the compute reduction against recognition error.
- **Mechanism:** The paper develops on-device streaming discrete speech units.
- **Conceptual structure:** Streaming is a causal information constraint: the model must decide from the past available at each moment, so efficiency is not just compression but a change in what evidence can be used.
- **What paper reports:** On ML-SUPERB 1h, the paper reports a 50% FLOP reduction for a 6.5% relative CER increase.
- **Limits:** Dataset size, causal window, unit clustering, hardware, FLOPs accounting, and CER bound practical generalization; the trade-off may change for other languages or latency targets.

## 7. room-channel-and-sensing

**Paper:** [Exploring auditory feedback mechanisms in speech recognition](https://www.isca-archive.org/interspeech_2025/coppietersdegibson25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `d6712056def5b6f5b1ece53b0927b5a67b40851b1988f65d42dba382297558e5`; full text captured.

- **Ordinary problem:** Automatic speech recognition features should reflect how the ear and cochlea actually transform sound, not only a convenient filter bank.
- **Why hard:** The cochlea is nonlinear and includes feedback; adding biologically motivated mechanisms increases computation and may help recognition while also serving as a test of hearing hypotheses.
- **Naive attempt:** Treat the cochlea as a fixed bank of independent filters and ignore feedback loops.
- **Central move:** Add Hopf-oscillator compression and olivocochlear feedback mechanisms to an ASR front end, then compare recognition behavior and biological plausibility.
- **Mechanism:** The paper explores auditory feedback mechanisms in speech recognition.
- **Conceptual structure:** A speech front end can be both an engineering component and a biological experiment: a mechanism is interesting when it changes recognition in the direction predicted by auditory physiology.
- **What paper reports:** The paper reports that adding the larger feedback loop appears beneficial for ASR, while describing the current implications as modest.
- **Limits:** Approximate oscillator model, compute limits, ASR task, feedback implementation, and modest gains bound interpretation; improved recognition does not validate the whole biological mechanism.

## 8. metrics-and-targets

**Paper:** [Non-intrusive Speech Quality Assessment with Diffusion Models Trained on Clean Speech](https://www.isca-archive.org/interspeech_2025/deoliveira25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `bf09f7a53de81408d740632db4ecec17e99055e12d07ed00e340b68dab8da589`; full text captured.

- **Ordinary problem:** A speech-quality monitor should judge a recording without a clean reference and without requiring labeled examples for every new condition.
- **Why hard:** Quality is a distance from acceptable clean speech, but a density model can mistake unusual yet good speech for bad speech and may inherit the biases of its clean training set.
- **Naive attempt:** Use a reference recording, train a supervised quality regressor with labels, or rely on a waveform statistic unrelated to perception.
- **Central move:** Train an unconditional diffusion model only on clean speech and use the likelihood of a deterministically noised input as an unsupervised quality score.
- **Mechanism:** The paper uses diffusion-model density estimation for non-intrusive speech-quality assessment.
- **Conceptual structure:** Quality is framed as compatibility with a learned distribution of clean speech: the score is a prior-based anomaly measure, not a direct measurement of every perceptual defect.
- **What paper reports:** The proposed log-likelihood correlates with intrusive metrics and showed the strongest correlation with human scores in the reported listening experiment.
- **Limits:** Clean-speech corpus, diffusion schedule, likelihood proxy, reference metrics, listeners, and distortion types bound the claim; low likelihood can mean unfamiliarity rather than poor quality.

