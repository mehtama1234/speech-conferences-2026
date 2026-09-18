# INTERSPEECH 2025 thirty-fifth-pass full-paper notes

Eight official-PDF readings deepen usability, toxic-span localization, respiratory measurement, spoken-language retention, speaker backends, codec separation, contextual adaptation, and Parkinson's speech.

## 1. human-centered-evaluation

**Paper:** [Web-Based Application for Real-Time Biofeedback of Vocal Resonance in Gender-Affirming Voice Training: Design and Usability Evaluation](https://www.isca-archive.org/interspeech_2025/mcallister25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `370a0fbf351a6a19a7b25c0a5caed9963baa6b5592deed81325a16de5e769f47`; full text captured.

- **Ordinary problem:** Voice training is an interactional skill, so a useful tool must show a learner what changed while they speak and remain usable in practice.
- **Why hard:** Resonance is felt and heard, but a display can overwhelm a learner or turn a gradual skill into a misleading single score.
- **Naive attempt:** Show raw spectra or prescribe a fixed target value and assume users can interpret it.
- **Central move:** Build a browser tool that gives real-time vocal-resonance biofeedback and evaluate whether intended users can complete tasks and understand the feedback.
- **Mechanism:** The study combines real-time acoustic analysis, visual feedback, and a usability evaluation for gender-affirming voice training.
- **Conceptual structure:** The design treats feedback as part of a human learning loop: measurement matters only if a person can notice it, interpret it, and act on it.
- **What paper reports:** The paper reports a working web application and usability findings supporting its use as a training aid.
- **Limits:** Small usability sample, task design, browser/audio conditions, and self-report limit claims about long-term learning or clinical outcomes.

## 2. accent-and-cultural-boundaries

**Paper:** [ViToSA: Audio-Based Toxic Spans Detection on Vietnamese Speech Utterances](https://www.isca-archive.org/interspeech_2025/do25b_interspeech.html)
**Evidence:** D3; PDF SHA-256 `b8e4cb43582deb8dcd796a7cec38b2bca457903f0ec19cb87835c340bb245919`; full text captured.

- **Ordinary problem:** A speech system should identify toxic spans in Vietnamese audio without hiding which words triggered the judgment.
- **Why hard:** Toxicity depends on language, context, and span boundaries; speech recognition errors can change both the words and the location of the alleged harm.
- **Naive attempt:** Classify the whole utterance or run a text toxicity model on an imperfect transcript and treat its spans as exact.
- **Central move:** Create an audio-based Vietnamese toxic-span task that preserves local evidence and evaluates both detection and boundary selection.
- **Mechanism:** ViToSA builds an audio dataset and task for locating toxic spans in Vietnamese speech utterances.
- **Conceptual structure:** The prediction target is localized: the system must connect acoustic input to a particular interval or word span rather than only assign a sentence label.
- **What paper reports:** The paper reports benchmark results for Vietnamese audio toxic-span detection.
- **Limits:** Dataset construction, annotation agreement, language, ASR errors, and social context bound the result; a benchmark score is not a complete safety policy.

## 3. time-frequency-measurement

**Paper:** [Adaptive Differential Denoising for Respiratory Sounds Classification](https://www.isca-archive.org/interspeech_2025/dong25e_interspeech.html)
**Evidence:** D3; PDF SHA-256 `26de42ef3f23f323ef6538936362cfbfc5bc97c9195f9d88dfede52dd8659523`; full text captured.

- **Ordinary problem:** Respiratory sounds are noisy measurements of a changing physical process, and a classifier needs to preserve disease-relevant events while suppressing irrelevant noise.
- **Why hard:** Breath sounds overlap in time and vary by microphone, patient, environment, and pathology; fixed denoising can remove the very irregularity being measured.
- **Naive attempt:** Apply one fixed noise filter or classify raw recordings without testing how denoising changes the signal.
- **Central move:** Use an adaptive differential denoising procedure whose behavior changes with the observed respiratory signal, then test classification.
- **Mechanism:** The paper proposes adaptive differential denoising for respiratory-sound classification and compares it with less adaptive processing.
- **Conceptual structure:** Denoising is part of the measurement model: the classifier can only learn a clinical distinction if the preprocessing preserves the relevant temporal-acoustic structure.
- **What paper reports:** The paper reports improved respiratory-sound classification with the proposed denoising approach.
- **Limits:** Dataset, labels, recording hardware, noise conditions, and evaluation split limit generalization to clinical deployment or diagnosis.

## 4. text-to-speech-and-content

**Paper:** [Analyzing Mitigation Strategies for Catastrophic Forgetting in End-to-End Training of Spoken Language Models](https://www.isca-archive.org/interspeech_2025/hsiao25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `bd40916921226ab2dc9c802c492c341f48247218b54a991aa7d6004d47f2e43c`; full text captured.

- **Ordinary problem:** A spoken-language model trained end to end may learn new tasks while forgetting how to perform tasks it already knew.
- **Why hard:** Speech, text, vocabulary, and task behavior are updated together; reducing forgetting can also reduce learning of the new objective or distort the shared representation.
- **Naive attempt:** Train only on the new data, freeze everything, or assume a larger model automatically retains old abilities.
- **Central move:** Compare mitigation strategies for catastrophic forgetting during end-to-end spoken-language-model training, including how data and parameter updates are controlled.
- **Mechanism:** The study evaluates forgetting-mitigation strategies for end-to-end training of spoken language models.
- **Conceptual structure:** The core tradeoff is retention versus adaptation: an update is useful only if it improves the new task without erasing previously learned speech-language behavior.
- **What paper reports:** The paper reports comparative forgetting and adaptation results across the tested strategies.
- **Limits:** Tasks, training order, model size, data mixture, and retention metrics bound the conclusions; results do not establish lifelong learning in open deployment.

## 5. speaker-characteristics

**Paper:** [Analysis of the ABC Classification Backends for NIST SRE24](https://www.isca-archive.org/interspeech_2025/cumani25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `e55085c9e467f9d8fd4fa93cd5e1db99319492dd4aca005ee8e08731ed6fe205`; full text captured.

- **Ordinary problem:** A speaker-recognition backend must decide whether recordings belong to the same person, while evaluation rankings can change with scoring, calibration, and trial composition.
- **Why hard:** A benchmark result is not only an embedding result: backend assumptions determine how scores are normalized and how errors are traded off.
- **Naive attempt:** Compare systems using one unexamined score or treat the best embedding as automatically the best verification system.
- **Central move:** Analyze the ABC classification backends used for NIST SRE24 and separate representation quality from backend scoring behavior.
- **Mechanism:** The paper studies backend choices for speaker classification/verification in the NIST SRE24 setting.
- **Conceptual structure:** Verification is a decision pipeline: embeddings, score computation, calibration, and operating point jointly produce the accepted/rejected decision.
- **What paper reports:** The paper reports how the analyzed backends behave on the NIST SRE24 evaluation conditions.
- **Limits:** Benchmark protocol, language/channel conditions, calibration, and chosen operating points limit claims beyond SRE24.

## 6. voice-identity-and-conversion

**Paper:** [LSCodec: Low-Bitrate and Speaker-Decoupled Discrete Speech Codec](https://www.isca-archive.org/interspeech_2025/guo25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `4cf0e9b1465f07ed184d8fcace0ac26a89b95cc293ea824c9496a1ab86cb8079`; full text captured.

- **Ordinary problem:** A speech codec should use few bits while preserving speech quality and should let a downstream system change speaker identity without accidentally carrying the original identity through the code.
- **Why hard:** Compression and identity are entangled: a code that preserves every detail spends bits, while a code that removes identity may damage linguistic content or naturalness.
- **Naive attempt:** Compress a standard speaker-dependent representation and assume the decoder will separate identity later.
- **Central move:** Learn a low-bitrate discrete code that is decoupled from speaker identity, then condition decoding on the desired speaker.
- **Mechanism:** LSCodec targets low-bitrate, speaker-decoupled discrete speech coding for controllable reconstruction or conversion.
- **Conceptual structure:** The code is a bottleneck with a division of labor: linguistic/acoustic content crosses the bottleneck, while speaker identity is supplied separately at decoding.
- **What paper reports:** The paper reports low-bitrate codec and speaker-decoupling results on its reconstruction/conversion evaluations.
- **Limits:** Bitrate, speaker set, decoder, datasets, and disentanglement tests bound the claim; identity leakage can remain outside the tested conditions.

## 7. adaptation-and-open-vocabulary

**Paper:** [Improving Synthetic Data Training for Contextual Biasing Models with a Keyword-Aware Cost Function](https://www.isca-archive.org/interspeech_2025/kwok25b_interspeech.html)
**Evidence:** D3; PDF SHA-256 `ba6b380f1b48c191973921bf7287c183ca99f2ba0a052d3d0fb4fc6e8e04e34f`; full text captured.

- **Ordinary problem:** Contextual biasing should help a recognizer spell a user's rare keyword, but it should not turn every acoustically similar word into that keyword.
- **Why hard:** Synthetic training examples can be plentiful yet unrealistic; a fixed cost for all keywords ignores how often each keyword is confused and how context changes the error.
- **Naive attempt:** Add a uniform decoding bonus or generate random keyword examples without modeling which confusions matter.
- **Central move:** Use a keyword-aware cost function when training synthetic contextual-biasing data so difficult and useful examples receive the right pressure.
- **Mechanism:** The paper improves synthetic-data training for contextual biasing with a keyword-aware cost function.
- **Conceptual structure:** The training objective changes the data's influence according to the keyword-level error structure; the goal is targeted correction rather than blanket bias.
- **What paper reports:** The paper reports improved contextual-biasing performance for the proposed synthetic-data objective.
- **Limits:** Keyword lists, synthetic-data quality, language, decoder, and evaluation distribution limit generalization; better keyword recall can still create false activations.

## 8. source-separation-and-spatial-listening

**Paper:** [Synchronous analysis of abnormal acoustic and linguistic production in Parkinson's speech](https://www.isca-archive.org/interspeech_2025/escobargrisales25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `618fa0b09963e911faf32aecbe031f0f370b444d76dc1dc5f4aa8a34b531a9a2`; full text captured.

- **Ordinary problem:** Parkinson's speech can show changes in both how sounds are produced and how language is organized, so one signal family may give an incomplete picture.
- **Why hard:** Acoustic and linguistic symptoms vary across speakers and tasks, and changes can be correlated without one causing the other.
- **Naive attempt:** Use only a speech-rate/acoustic score or only a transcript-based linguistic score as a complete disease marker.
- **Central move:** Measure acoustic and linguistic production synchronously in the same speech material and examine their joint relationship.
- **Mechanism:** The study synchronizes analysis of abnormal acoustic and linguistic production in Parkinson's speech.
- **Conceptual structure:** Synchronous observation aligns two levels of behavior in time, allowing co-occurrence to be studied without pretending that either level alone explains the condition.
- **What paper reports:** The paper reports coordinated acoustic and linguistic findings in Parkinson's speech.
- **Limits:** Cohort, task, disease stage, annotation, and statistical design limit clinical generalization; association is not diagnosis or causation.

