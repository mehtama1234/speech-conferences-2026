# INTERSPEECH 2025 sixty-second-pass full-paper notes

Eight additional captured-PDF readings extend D3 comparison beyond the original seed.

## 1. speaker-characteristics

**Paper:** [VoxAging: Continuously Tracking Speaker Aging with a Large-Scale Longitudinal Dataset in English and Mandarin](https://www.isca-archive.org/interspeech_2025/ai25_interspeech.html)
**Evidence:** D3; PDF SHA-256 %s; full text captured.

- **Ordinary problem:** A speaker system should recognize that a person's voice changes with age rather than treating time-varying identity as noise.
- **Why hard:** Longitudinal recordings mix biological change, channel variation, language, and recording history.
- **Naive attempt:** Train one speaker model on pooled recordings and assume a speaker embedding remains stationary.
- **Central move:** Build a longitudinal English/Mandarin resource and measure how aging changes verification evidence.
- **Mechanism:** Link recordings across years, then test verification as time gap, age group, and gender change.
- **Mathematical/conceptual structure:** EER and embedding cosine similarity turn identity preservation into separability and distance between same-speaker observations.
- **Evaluation:** VoxAging contains 293 speakers with spans up to about 17 years; verification is evaluated with EER and cosine similarity, comparing ECAPA and ERes2Net systems.
- **What paper reports:** The paper reports declining verification accuracy and embedding similarity as recordings move farther apart in time, with age and gender affecting the rate of change.
- **Limits:** Speaker coverage, language balance, recording channels, gated data, and longitudinal confounding limit causal claims about biological aging.

## 2. clinical-and-assistive-speech

**Paper:** [Patient-Aware Feature Alignment for Robust Lung Sound Classification: Cohesion-Separation and Global Alignment Losses](https://www.isca-archive.org/interspeech_2025/jeong25_interspeech.html)
**Evidence:** D3; PDF SHA-256 %s; full text captured.

- **Ordinary problem:** A clinical audio classifier should distinguish medically meaningful lung-sound patterns without letting patient identity dominate.
- **Why hard:** Patient-specific acoustics and recording conditions can make a classifier memorize who was recorded instead of pathology.
- **Naive attempt:** Optimize ordinary cross-entropy on pooled recordings and trust aggregate accuracy.
- **Central move:** Align patient-aware representations while separating normal and abnormal acoustic evidence.
- **Mechanism:** Combine pretrained audio features with patient-aware alignment, cohesion-separation, and global-alignment losses before classification.
- **Mathematical/conceptual structure:** Similarity and separation losses reshape within-patient and across-class distances; sensitivity, specificity, and ICBHI score expose different errors.
- **Evaluation:** The ICBHI 2017 corpus has 6,898 recordings and an official 60/40 split; five-run comparisons report sensitivity, specificity, and ICBHI score with backbone and loss ablations.
- **What paper reports:** The paper reports improved ICBHI performance and more patient-balanced behavior with the proposed alignment losses.
- **Limits:** Patient/device distribution, benchmark labels, acoustic conditions, and absent clinical deployment evaluation limit medical interpretation.

## 3. metrics-and-targets

**Paper:** [Enabling the replicability of speech synthesis perceptual evaluations](https://www.isca-archive.org/interspeech_2025/lemaguer25_interspeech.html)
**Evidence:** D3; PDF SHA-256 %s; full text captured.

- **Ordinary problem:** A speech-synthesis listening claim should be inspectable and repeatable, not just summarized by one MOS number.
- **Why hard:** Subjective results depend on stimuli, participants, protocol, anchors, randomization, analysis, and reporting choices.
- **Naive attempt:** Report a mean listener score and assume reproducibility because the model and samples are named.
- **Central move:** Decompose evaluation into a structured report and a recipe containing materials and decisions needed to repeat it.
- **Mechanism:** Audit the goal, dataset and bias, participant cohort, protocol, analysis, conclusions, and limitations, then package evaluation assets and procedures.
- **Mathematical/conceptual structure:** The central object is an auditable mapping from hypothesis to stimuli, ratings, uncertainty, and conclusion.
- **Evaluation:** This protocol paper contributes a checklist, evaluation-report structure, and reproducibility recipe rather than a new held-out model benchmark.
- **What paper reports:** The paper reports a structured template intended to make subjective speech-synthesis studies more reproducible and limitations more visible.
- **Limits:** A checklist cannot guarantee participant representativeness, perceptual validity, or exact replication when access differs.

## 4. text-to-speech-and-content

**Paper:** [FoleyMaster: High-Quality Video-to-Audio Synthesis via MLLM-Augmented Prompt Tuning and Joint Semantic-Temporal Adaptation](https://www.isca-archive.org/interspeech_2025/liang25b_interspeech.html)
**Evidence:** D3; PDF SHA-256 %s; full text captured.

- **Ordinary problem:** Video-to-audio generation must produce sound that matches what happens in a video and when it happens.
- **Why hard:** A generated sound can be semantically plausible but mistimed, or aligned but acoustically unrelated.
- **Naive attempt:** Prompt a generic text-to-audio model with a caption and ignore fine-grained event timing.
- **Central move:** Use MLLM-augmented prompting and semantic-temporal adaptation for event identity and onset structure.
- **Mechanism:** Video semantics guide the prompt while probabilistic temporal conditioning aligns generated events with visual onsets.
- **Mathematical/conceptual structure:** CLIP score measures semantic alignment and onset accuracy measures temporal agreement; their separation exposes two failures.
- **Evaluation:** FoleyMaster is evaluated on VGGSound Plus with CLIP Score and onset accuracy, baselines, ablations, and a 20-participant pairwise study.
- **What paper reports:** The paper reports gains across semantic and temporal metrics and user preference, with prompt/time components supported by ablations.
- **Limits:** Automatic proxies, dataset distribution, event taxonomy, and a small listener study limit claims about real-world Foley usefulness.

## 5. grounding-and-action

**Paper:** [CLAP-ART: Automated Audio Captioning with Semantic-rich Audio Representation Tokenizer](https://www.isca-archive.org/interspeech_2025/takeuchi25_interspeech.html)
**Evidence:** D3; PDF SHA-256 %s; full text captured.

- **Ordinary problem:** An audio caption should identify the sound event a listener treats as the referent, not merely match common caption words.
- **Why hard:** Caption metrics reward n-gram overlap while missing semantic adequacy, and discrete representations can discard event details.
- **Naive attempt:** Feed a generic continuous audio embedding to a caption decoder and optimize only caption likelihood.
- **Central move:** Use a semantic-rich audio representation tokenizer with multi-layer codebooks.
- **Mechanism:** CLAP-ART converts audio into discrete representations learned from semantic audio features; a caption model conditions on those tokens.
- **Mathematical/conceptual structure:** CIDEr, SPICE, and SPIDEr compare generated language with references, but each is only a proxy for grounded event meaning.
- **Evaluation:** CLAP-ART is tested on AudioCaps and a second audio-caption benchmark with BLEU, METEOR, ROUGE-L, CIDEr, SPICE, and SPIDEr, including six-run averages and codebook ablations.
- **What paper reports:** The paper reports improved caption scores and a favorable multi-layer codebook tradeoff.
- **Limits:** Reference-caption variability, language bias, metric disagreement, and no independent human grounding study limit claims.

## 6. source-separation-and-spatial-listening

**Paper:** [Direct-path Relative Harmonic Coefficients Detection for Multi-source Direction-of-Arrival Estimation in Reverberant Environments](https://www.isca-archive.org/interspeech_2025/tao25_interspeech.html)
**Evidence:** D3; PDF SHA-256 %s; full text captured.

- **Ordinary problem:** A microphone array should locate several sources even when reverberation hides the direct path.
- **Why hard:** Reflections create false direction evidence and make direct-path bins sparse or unstable.
- **Naive attempt:** Search the whole spatial grid with a conventional beamformer or treat every bin as equally reliable.
- **Central move:** Detect direct-path relative harmonic coefficients and use reliable spatial evidence for 3D localization.
- **Mechanism:** Estimate relative harmonic structure, identify valid direct-path bins, and aggregate their directional evidence.
- **Mathematical/conceptual structure:** Mean absolute angular error measures localization distance; valid-bin proportion measures whether usable spatial observations were found.
- **Evaluation:** Simulated reverberant scenes vary source count and T60, with recorded conditions also tested; MAEE and valid-bin proportion compare four baselines.
- **What paper reports:** The paper reports lower localization error in most tested reverberant scenarios and improved robustness.
- **Limits:** Array geometry, source count, room conditions, harmonic assumptions, and angular-error averaging limit transfer.

## 7. human-centered-evaluation

**Paper:** [Accessible Real-time Eye-gaze Tracking for Neurocognitive Health Assessment: A Multimodal Web-based Approach](https://www.isca-archive.org/interspeech_2025/tisdale25_interspeech.html)
**Evidence:** D3; PDF SHA-256 %s; full text captured.

- **Ordinary problem:** A real-time eye-gaze health tool should be usable by people with different motor and cognitive profiles, not only accurate for an average user.
- **Why hard:** Gaze error, fatigue, engagement, task difficulty, and individual movement interact, so one accuracy score misses usability.
- **Naive attempt:** Train one gaze predictor and evaluate only aggregate spatial error.
- **Central move:** Combine accessible web-based interaction with task-specific metric families, cohort analysis, classification, and usability feedback.
- **Mechanism:** Extract distance, velocity, saccade, and task metrics, compare cohorts, and use selected features in an AdaBoost classifier.
- **Mathematical/conceptual structure:** Feature selection and cross-validation turn gaze traces into a cohort-level decision, while survey ratings expose usability beyond classifier accuracy.
- **Evaluation:** Kruskal-Wallis selection, k-fold validation, accuracy/F1, and survey ratings connect gaze traces to cohort decisions.
- **What paper reports:** The paper reports AdaBoost at 0.89 accuracy and 0.67 F1 against 0.77 baseline, plus a 39-participant usability survey with 82% high engagement.
- **Limits:** Cohort composition, task design, leakage risk, self-report, and absent clinical validation limit health claims.

## 8. grounding-and-action

**Paper:** [Mitigating Audiovisual Mismatch in Visual-Guide Audio Captioning](https://www.isca-archive.org/interspeech_2025/xu25j_interspeech.html)
**Evidence:** D3; PDF SHA-256 %s; full text captured.

- **Ordinary problem:** Visual-guide audio captioning should remain semantically faithful when audio and visual streams do not line up.
- **Why hard:** Audiovisual mismatch can make a model overtrust the wrong modality and describe the wrong event fluently.
- **Naive attempt:** Train on perfectly synchronized pairs and assume test alignment is identical.
- **Central move:** Use systematic audiovisual shuffling and semantic/temporal adaptation to train and test under mismatch.
- **Mechanism:** Vary shuffle probability while semantic and temporal modules preserve event meaning and timing.
- **Mathematical/conceptual structure:** Caption metrics combine n-gram and semantic measures; repeated timed inference exposes accuracy and deployment cost.
- **Evaluation:** The paper evaluates eight caption metrics across shuffle probabilities, ablates semantic/temporal components, varies video length, and averages timed inference.
- **What paper reports:** The paper reports stronger semantic resilience under mismatch, with both modules contributing.
- **Limits:** Synthetic shuffle may not represent real errors; caption variability and proxy metrics limit human-grounding claims.

