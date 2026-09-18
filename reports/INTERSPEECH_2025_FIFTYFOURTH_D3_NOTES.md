# INTERSPEECH 2025 fifty-fourth-pass full-paper notes

Eight official-PDF readings deepen voice conversion/identity, sequence boundaries, resource and distribution robustness, and speaker-level evaluation.

## 1. voice-identity-and-conversion

**Paper:** [Unsupervised Rhythm and Voice Conversion to Improve ASR on Dysarthric Speech](https://www.isca-archive.org/interspeech_2025/elhajal25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `cc906672e7e809a762735cca9f17d2802f5651b2d6828e98e38bff1442cd9f3e`; full text captured.

- **Ordinary problem:** ASR should recover dysarthric speech even when slow rhythm and unusual voice quality make the acoustic pattern unlike healthy training speech.
- **Why hard:** Speaker variation and rate changes are entangled, and a conversion that sounds healthier may alter linguistic content or fail for severe dysarthria.
- **Naive attempt:** Apply a generic speed perturbation or train a speaker-specific converter and assume the recognizer will adapt.
- **Central move:** Use unsupervised rhythm and voice conversion with syllable-level rhythm modeling, then measure whether converted speech helps LF-MMI and Whisper ASR.
- **Mechanism:** RnV converts timing and voice characteristics without parallel healthy speech; syllable structure supplies a dysarthria-relevant rhythm representation before ASR scoring.
- **Mathematical/conceptual structure:** Conversion is a task-conditioned invariance: remove cues that obstruct recognition while retaining phonetic content needed by the recognizer.
- **What paper reports:** On Torgo, LF-MMI shows reported WER reductions, especially for severe dysarthria, while Whisper fine-tuning on converted data has minimal effect.
- **Limits:** Torgo speakers, severity, conversion fidelity, ASR backend, and WER protocol bound transfer; improved recognition is not improved naturalness or clinical communication.

## 2. voice-identity-and-conversion

**Paper:** [Vo-Ve: An Explainable Voice-Vector for Speaker Identity Evaluation](https://www.isca-archive.org/interspeech_2025/lee25e_interspeech.html)
**Evidence:** D3; PDF SHA-256 `92a27fe7fdd1c407f717cc174311ef5083a4b71cdb2cd8e75fc84d913129cfa7`; full text captured.

- **Ordinary problem:** A speaker-similarity system should say not only whether two voices match but which voice attributes support that judgment.
- **Why hard:** Ordinary embeddings compress identity into opaque coordinates, making errors and shifts across tasks difficult to interpret.
- **Naive attempt:** Use a black-box speaker embedding and treat its similarity score as a complete explanation.
- **Central move:** Represent identity with an interpretable vector of explicit voice-attribute class probabilities and compare its similarity with conventional embeddings.
- **Mechanism:** Vo-Ve maps speech to attribute probabilities; similarity can then be decomposed into human-readable properties instead of a single latent distance.
- **Mathematical/conceptual structure:** The representation trades some compact opacity for an interpretable coordinate system whose attributes can be inspected when similarity changes.
- **What paper reports:** The paper reports competitive speaker-similarity evaluation and attribute-level explanations in its experiments.
- **Limits:** Attribute inventory, labels, language, channel variation, and metric protocol bound interpretability; explainable similarity is not proof of causal identity factors.

## 3. boundaries-and-sequence-structure

**Paper:** [Bidirectional Spoken-Written Text Conversion with Large Language Models](https://www.isca-archive.org/interspeech_2025/choi25g_interspeech.html)
**Evidence:** D3; PDF SHA-256 `46dd7b70401166c9f07ac62da465afe83ce6da56447d82869ce7282efbbd152f`; full text captured.

- **Ordinary problem:** A recognizer should handle both spoken-form and written-form transcripts without inconsistent normalization of numbers, names, or punctuation.
- **Why hard:** Speech databases often contain one transcription convention while modern models emit another, and manually building paired forms is expensive.
- **Naive attempt:** Train on whichever transcript convention is available or attach a one-way text-normalization postprocessor.
- **Central move:** Use LLM-generated dual transcriptions, iterative supervised/semi-supervised expansion, and a bidirectional text-conversion model supporting both ITN and TN.
- **Mechanism:** The model learns mappings in both directions; generated paired text supplies supervision while iterative learning enlarges the conversion data.
- **Mathematical/conceptual structure:** The central object is a representation boundary between spoken language and written conventions, not a change to the acoustic evidence itself.
- **What paper reports:** The paper reports a 13.4% ERR improvement in the evaluated conversion setting.
- **Limits:** LLM generation quality, language conventions, error metric, transcript domain, and iterative-label bias bound transfer; normalization success is not ASR acoustic accuracy.

## 4. boundaries-and-sequence-structure

**Paper:** [Who knows best? Effects of speech disfluencies on incentivized decision-making](https://www.isca-archive.org/interspeech_2025/kirkland25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `e1bec7608bd14b085b60809e14b8508c4523ffc3f40202a91dcccaf4d4162f09`; full text captured.

- **Ordinary problem:** Listeners may use pauses and disfluencies as evidence when deciding whom or what to believe, so removing them can change behavior rather than merely readability.
- **Why hard:** Prior ratings of competence do not show whether speech cues affect consequential choices, and credibility judgments interact with source conflict and incentives.
- **Naive attempt:** Normalize all disfluent speech before evaluation or infer real-world behavior from Likert ratings alone.
- **Central move:** Use an incentivized web decision task with conflicting information and compare choices as a function of speech fluency.
- **Mechanism:** The experiment treats disfluency as part of the observed communication signal and measures choice behavior rather than only an attitude rating.
- **Mathematical/conceptual structure:** Behavioral choice is a downstream proxy: it tests whether a listener’s interpretation of fluency changes action under incentives.
- **What paper reports:** The study reports that listeners take speech fluency into account when deciding whom or what to believe.
- **Limits:** Task stakes, speakers, disfluency types, online sample, and source-conflict design bound transfer; choice bias is not proof that disfluencies carry truthful information.

## 5. robustness-and-system-boundary

**Paper:** [NanoCodec: Towards High-Quality Ultra Fast Speech LLM Inference](https://www.isca-archive.org/interspeech_2025/casanova25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `94b942d9676fb3e3204821f38649c376f7ab4dee89b49344a970e6ec86f5532d`; full text captured.

- **Ordinary problem:** A speech codec used inside an autoregressive audio model should compress sound with few tokens per second without destroying reconstruction quality.
- **Why hard:** High frame rates make every generated second expensive, while lowering rate or bitrate can erase fine acoustic detail and causality can add delay.
- **Naive attempt:** Choose a low frame rate without measuring the rate/bitrate/causality tradeoff, or optimize only waveform quality at an impractical token rate.
- **Central move:** Ablate frame rate, bitrate, and causality, then design NanoCodec around a low-rate operating point and compare reconstruction quality.
- **Mechanism:** The codec maps audio to discrete tokens and back; token rate controls autoregressive steps while bitrate and causal context control information and latency.
- **Mathematical/conceptual structure:** Compression is a rate-distortion-resource tradeoff: fewer symbols reduce computation but constrain what the decoder can reconstruct.
- **What paper reports:** NanoCodec reports high-quality compression at 12.5 FPS and competitive results across bitrate ranges.
- **Limits:** Audio domain, codec training data, perceptual metric, hardware, and causality setting bound transfer; codec quality is not end-to-end speech generation quality.

## 6. robustness-and-system-boundary

**Paper:** [Improving Generalization of End-to-End ASR through Diversity and Independence Regularization](https://www.isca-archive.org/interspeech_2025/ko25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `8be702dbdb60f1787e3c134afe753492373afe8b19d6f0bf514643c41e204cf5`; full text captured.

- **Ordinary problem:** An ASR model should generalize when test speech differs from training speech instead of memorizing redundant or narrow feature patterns.
- **Why hard:** CTC, AED, and RNN-T models can overfit in different ways, and increasing feature diversity without controlling redundancy may not help.
- **Naive attempt:** Add capacity or regularize all features identically without identifying whether redundancy or lack of diversity causes the error.
- **Central move:** Add diversity loss to separate feature representations and independence loss to reduce covariance, then test across three ASR architectures.
- **Mechanism:** The losses operate on learned feature vectors: one discourages collapse toward similar patterns, the other discourages redundant correlated dimensions.
- **Mathematical/conceptual structure:** The method shapes representation geometry so multiple informative directions survive while redundant variation is suppressed.
- **What paper reports:** The paper reports improved generalization and robustness for CTC, AED, and RNN-T models in the evaluated tasks.
- **Limits:** Training/test shifts, loss weights, architectures, languages, and robustness protocol bound transfer; benchmark generalization is not immunity to arbitrary distribution shift.

## 7. speaker-characteristics

**Paper:** [You Are What You Say: Exploiting Linguistic Content for VoicePrivacy Attacks](https://www.isca-archive.org/interspeech_2025/gaznepoglu25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `b6ff765d96a449ac72d3108d33e0cd3c1ed82075ed24659efe7907a740a1bff6`; full text captured.

- **Ordinary problem:** A voice-privacy attack should not mistake repeated linguistic content for speaker identity when evaluating anonymization.
- **Why hard:** If attacker training and test utterances share semantic or lexical content, text alone can predict the speaker and make privacy scores misleading.
- **Naive attempt:** Use a standard ASV attack and assume its error reflects only acoustic identity leakage.
- **Central move:** Adapt BERT to attack speaker identity from transcript content, inspect explainable keywords, and compare the resulting EER and dataset construction.
- **Mechanism:** The attacker maps linguistic content to speaker labels; semantically similar utterances become a non-acoustic identity channel in the evaluation.
- **Mathematical/conceptual structure:** Privacy evaluation requires separating nuisance correlations from the protected attribute; otherwise the attack measures corpus curation rather than voice leakage.
- **What paper reports:** The paper reports mean EER around 35%, with some speakers as low as 2%, using text alone on VoicePrivacy data.
- **Limits:** Dataset curation, speaker/content overlap, BERT training, split design, and EER interpretation bound the claim; text leakage does not prove an anonymizer fails acoustically.

## 8. speaker-characteristics

**Paper:** [Variability in performance across four generations of automatic speaker recognition systems](https://www.isca-archive.org/interspeech_2025/harrington25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `42d5a5cd0253d4566d598e3b5aedd4d36bd5ad4b3595d6230d2466d346e1a5de`; full text captured.

- **Ordinary problem:** A speaker-recognition benchmark should reveal which people and conditions remain difficult, not only report one aggregate score across model generations.
- **Why hard:** Architectural improvements can hide persistent speaker-level failures, and file-level factors can be confused with stable person-level difficulty.
- **Naive attempt:** Compare only aggregate metrics or assume each new generation improves every speaker equally.
- **Central move:** Evaluate four generations on the same forensic test/calibration data at both system and individual-speaker levels.
- **Mechanism:** Matched evaluation separates model-generation effects from test-set changes and decomposes variation by file and speaker factors.
- **Mathematical/conceptual structure:** The unit of analysis matters: an overall metric averages heterogeneous difficulty, while per-speaker outcomes expose persistent tails.
- **What paper reports:** Performance improves from GMM-UBM through i-vector and x-vector but not ECAPA-TDNN in the reported comparison; some individuals remain difficult across systems.
- **Limits:** Forensic data, calibration, system implementations, speaker sampling, and metric choice bound transfer; persistent difficulty is not automatically a biological property.

