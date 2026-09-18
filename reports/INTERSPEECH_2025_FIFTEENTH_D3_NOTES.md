# INTERSPEECH 2025 fifteenth-pass full-paper notes

Eight official-PDF analyses deepen clinical speech, accent boundaries, recognition, enhancement, separation, and voice conversion. Results remain author-reported and were not independently reproduced.

## 1. listening-and-separation/noise-enhancement

**Paper:** [Test-Time Training for Speech Enhancement](https://www.isca-archive.org/interspeech_2025/behera25_interspeech.html)
**Evidence:** D3; PDF SHA-256 14cefc1a98fba14832deebdd27641461e572c1ab20ca128b54656a17486dc250; 5 pages.

- **Big picture:** An enhancement model should adapt when the noise at test time differs from training, even without labeled examples from the new environment.
- **Why hard:** Noise and recording domains shift at deployment, while collecting clean/noisy pairs for every new domain is expensive.
- **Naive attempt:** Freeze the enhancement model and hope training-domain noise statistics transfer.
- **Central move:** Use a Y-shaped enhancement model with self-supervised reconstruction or masked-spectrogram tasks during test-time adaptation.
- **Mechanism:** The main enhancement task shares representations with an auxiliary task optimized on the current noisy signal, with strategies trading adaptation gain against test-time cost.
- **Conceptual structure:** The method treats deployment as a second learning stage: the signal supplies an unsupervised clue about the new domain while the enhancement objective remains the output target.
- **What paper reports:** The paper reports consistent speech-quality improvements over its baseline on synthetic and real-world datasets.
- **Limits:** The adaptation steps, compute budget, noise conditions, and author-reported metrics bound the result; listener benefit and long-term stability remain open.

## 2. people-and-variation/clinical-and-assistive-speech

**Paper:** [Pitfalls and Limits in Automatic Dementia Assessment](https://www.isca-archive.org/interspeech_2025/braun25_interspeech.html)
**Evidence:** D3; PDF SHA-256 d25917a052e350b1aff677d162e535728c3eb61781b8b02c284a52fce9616959; 5 pages.

- **Big picture:** A speech-based dementia score can correlate with human scores while still being systematically wrong for some people.
- **Why hard:** Word-naming performance and fallback rules can make severe impairment look easier to detect than mild impairment or healthy speech.
- **Naive attempt:** Report one overall correlation and treat it as equally meaningful across severity groups.
- **Central move:** Inspect the automated Syndrom-Kurz-Test pipeline by subgroup, transcription quality, item type, and fallback behavior rather than relying on one aggregate number.
- **Mechanism:** The analysis links scoring artifacts to speech production decline, ASR errors, and fallback handling; apparent agreement can therefore arise from the test design.
- **Conceptual structure:** The paper turns evaluation from a single correlation into a chain of measurement decisions whose errors can favor particular groups.
- **What paper reports:** The paper reports high overall correlation but weaker behavior for healthy and mildly impaired groups and identifies overoptimistic correlations for severely impaired speakers.
- **Limits:** This is an analysis of one standardized assessment and its data; it warns against clinical claims, not a universal ranking of dementia-screening systems.

## 3. voice-generation-and-control/text-to-speech-and-content

**Paper:** [Non-Standard Accent TTS Support via Large Multi-Accent Frontend Pronunciation Knowledge Transfer](https://www.isca-archive.org/interspeech_2025/berger25_interspeech.html)
**Evidence:** D3; PDF SHA-256 a18532251ba2a28fabd6badc002e3a23d6a5062e85e56a0e194c2098dc002140; 5 pages.

- **Big picture:** A text-to-speech system should pronounce an accent it has barely seen without requiring a large new pronunciation database.
- **Why hard:** Pronunciation frontend errors occur before waveform generation and are costly to label for every accent.
- **Naive attempt:** Train a separate full-size pronunciation model for every target accent.
- **Central move:** Transfer pronunciation knowledge from a large multi-accent frontend and measure how much target-accent data is needed as source accents vary in similarity.
- **Mechanism:** The frontend predicts phones, lexical stress, and prosodic boundaries; target accents are trained with reduced data and compared with full-data and single-accent baselines.
- **Conceptual structure:** Accent similarity becomes a data-selection variable: transfer is not merely shared representation, but choosing a source whose pronunciation structure is useful for the target.
- **What paper reports:** The paper reports up to 95% less pronunciation training data for robust performance and examines 14 English accents using LibriTTS and HiFi-TTS-derived data.
- **Limits:** Accuracy is reported for the studied accents, frontend labels, and datasets; transfer to other languages, voices, and synthesis backends remains unestablished.

## 4. recognition-and-alignment/adaptation-and-open-vocabulary

**Paper:** [NGPU-LM: GPU-Accelerated N-Gram Language Model for Context-Biasing in Greedy ASR Decoding](https://www.isca-archive.org/interspeech_2025/bataev25_interspeech.html)
**Evidence:** D3; PDF SHA-256 a607c37d61f73800165c1f8932173e76595e9c85181cc2d04d318c639fafeba5; 5 pages.

- **Big picture:** A recognizer must recognize rare or domain-specific words without paying the full cost of beam search on every utterance.
- **Why hard:** Greedy decoding is cheap but loses context; beam search recovers some context at a large compute cost.
- **Naive attempt:** Use beam search everywhere, or add a sequential language model whose data structure serializes every transition.
- **Central move:** Represent n-gram transitions for parallel GPU lookup and inject their scores into greedy decoding for CTC, transducer, and attention models.
- **Mechanism:** NGPU-LM uses hash-based transition lookup and customizable greedy decoding so context biasing can recover domain words with less than 7% reported overhead.
- **Conceptual structure:** The conceptual trade is between linguistic context and decoding latency; data structure and hardware choices move that boundary without changing the acoustic model.
- **What paper reports:** The paper reports recovery of more than half the greedy/beam accuracy gap in out-of-domain tests and up to 10.6% relative WER improvement in its experiments.
- **Limits:** The results depend on tested ASR architectures, domains, GPU implementation, and author-reported measurements; deployment energy and other hardware remain open.

## 5. evaluation-deployment-and-consequence/metrics-and-targets

**Paper:** [Intelligibility Prediction for Time-Modified Speech Signals Using Spectro-Temporal Modulation Features](https://www.isca-archive.org/interspeech_2025/bashir25_interspeech.html)
**Evidence:** D3; PDF SHA-256 d16f9d8366aa1d9bdc42725741998c47f64b5238df20ec369ee7572525fa795d; 5 pages.

- **Big picture:** A speech-quality score should remain meaningful when processing changes the timing of the speech, not only its spectrum.
- **Why hard:** Reference-based intelligibility predictors compare aligned clean and degraded signals; time modification breaks that alignment.
- **Naive attempt:** Use MFCC-based dynamic time warping or assume time modification is a small nuisance.
- **Central move:** Align clean and time-modified speech with selected spectro-temporal modulation features, then feed the alignment into existing reference-based intelligibility predictors.
- **Mechanism:** The system uses DTW over modulation features and compares two ways of incorporating the alignment into RB-SIPAs across noise and time-modification conditions.
- **Conceptual structure:** The move separates two questions that are often mixed: finding corresponding speech events and predicting whether the resulting signal is intelligible.
- **What paper reports:** The paper reports better alignment behavior and better correlation with listening scores than MFCC-based alternatives under its tested conditions.
- **Limits:** The listening datasets, degradation types, chosen modulation channels, and reference availability bound the claim; correlation is not a complete model of listener experience.

## 6. languages-accents-and-resources/low-resource-and-data-creation

**Paper:** [Better Semi-supervised Learning for Multi-domain ASR Through Incremental Retraining and Data Filtering](https://www.isca-archive.org/interspeech_2025/carofilis25_interspeech.html)
**Evidence:** D3; PDF SHA-256 0b0ae771e24a39cd0c481ffd12f36450ae1ce797c733e66e321461549c6d8f7d; 5 pages.

- **Big picture:** A recognizer needs to adapt to a new domain when only a little labeled speech is available but related audio is abundant.
- **Why hard:** Unlabeled audio can add coverage but can also inject wrong pseudo-labels and reinforce domain errors.
- **Naive attempt:** Fine-tune once on the small labeled set or choose pseudo-labels randomly.
- **Central move:** Incrementally combine in-domain labels with related-domain data, then filter pseudo-labels using multi-model consensus or named-entity recognition.
- **Mechanism:** The pipeline retrains in stages and uses agreement or entity preservation to decide which generated transcripts enter the next training round.
- **Conceptual structure:** Data selection is treated as part of learning: the value of unlabeled speech depends on which errors are admitted, not only on how much audio is added.
- **What paper reports:** The paper reports up to 22.3% relative improvement on Wow and 24.8% on Fisher over random selection, with consensus strongest and NER cheaper.
- **Limits:** The gains are bounded to the two English corpora, model ensemble, filtering thresholds, and author-reported WER; other domains and languages remain unresolved.

## 7. recognition-and-alignment/boundaries-and-sequence-structure

**Paper:** [ASR-based segmentation for the analysis of larger child-speech datasets: Performance evaluation on vowels from Australian-English speaking children aged 4 to 11 years](https://www.isca-archive.org/interspeech_2025/cai25_interspeech.html)
**Evidence:** D3; PDF SHA-256 1a3627d4390a69a3fd7b6afe68cfab8bf1aab47051a0667c7379724953a43cbc; 5 pages.

- **Big picture:** Large child-speech collections need segment boundaries, but an adult-trained aligner may place those boundaries according to a different rule than a human analyst.
- **Why hard:** Children's articulation and developmental variation make forced alignment less stable, and disagreement can change measured vowel durations or trajectories.
- **Naive attempt:** Treat an adult forced aligner as interchangeable with manual annotation.
- **Central move:** Compare human-human reliability with manual-versus-Montreal-Forced-Aligner boundaries across child ages and inspect systematic discrepancies.
- **Mechanism:** The study evaluates vowel boundaries in Australian-English child speech and asks how alignment error changes from ages four to eleven.
- **Conceptual structure:** The conceptual issue is not simply alignment accuracy: a boundary is an analytic decision whose meaning must be shared by the tool and the human measurement protocol.
- **What paper reports:** The paper reports that MFA falls short of human annotation, with smaller discrepancies for older children.
- **Limits:** The evidence is tied to the tested vowels, ages, language variety, and annotators; it supports semi-automatic caution rather than universal aligner failure.

## 8. evaluation-deployment-and-consequence/privacy-security-and-accountability

**Paper:** [Generalizable Audio Spoofing Detection using Non-Semantic Representations](https://www.isca-archive.org/interspeech_2025/das25_interspeech.html)
**Evidence:** D3; PDF SHA-256 eaa24777b38b4fb02ac90c59ed8cca27e81bcfc970490057d8f057cfd375e2d0; 5 pages.

- **Big picture:** A spoof detector should recognize synthetic audio from new generators and public-domain conditions, not only the generator seen during training.
- **Why hard:** Semantic embeddings can learn the message instead of the traces of synthesis, while in-domain scores can hide failure under distribution shift.
- **Naive attempt:** Optimize only on a matched generator and report one in-domain score.
- **Central move:** Use non-semantic universal audio representations and compare them with handcrafted, semantic, and end-to-end alternatives under out-of-domain tests.
- **Mechanism:** TRILL and TRILLsson representations are evaluated as features for a spoofing classifier across in-domain and public-domain conditions.
- **Conceptual structure:** The method changes what evidence the detector is allowed to use: it seeks production artifacts that survive a change in spoken content and generator.
- **What paper reports:** The paper reports comparable in-domain performance and stronger out-of-domain results than the tested baselines.
- **Limits:** The generators, corpora, representation models, and author-reported tests define the boundary; future synthesis methods and adversarial adaptation remain open.

