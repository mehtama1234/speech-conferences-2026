# Speakers as changing people, not nuisance variables

*Essay 6 of 8 in The Speech Atlas.*

A speaker is a person, not a nuisance variable. Age, identity, health, disability, hearing ability, and interaction needs change both the signal and the cost of failure. This essay treats those differences as part of the problem definition.

## Start with the baseline

Fant's speech-chain account places this theme at the following point in communication: Fant pp. 6-7: physical signal parameters and message-level distinctions are related but not identical; this is the baseline for testing when speaker variation is useful evidence or nuisance.

The ordinary problem is simple to state: Voice depends on anatomy, age, health, emotion, language history, social setting, and equipment; these differences affect both communication and measurement.

A tempting shortcut is to Treating variation as noise makes systems work best for a narrow population and can turn a health or identity signal into an unwanted demographic shortcut. That shortcut fails because it hides the distinction this essay needs to keep visible.

The recurring move across this theme is to Measure which variation is task-relevant, model it explicitly when appropriate, and test performance and meaning across people and conditions. The cost is equally important: A factor that helps prediction may be sensitive, confounded, or harmful to expose; personalization can improve access while increasing privacy risk.

## The boundaries

Each section below uses the same test: what pressure is being handled, what shortcut fails, what move recurs, and where the evidence stops.

## Identity, age, and changing voice

**The question.** What ordinary speech pressure is handled by identity, age, and changing voice, and what evidence distinguishes it from neighboring pressures?

**How this boundary is derived.** Baseline link: Fant pp. 6-7: physical signal parameters and message-level distinctions are related but not identical; this is the baseline for testing when speaker variation is useful evidence or nuisance. Ordinary pressure: Voice depends on anatomy, age, health, emotion, language history, social setting, and equipment; these differences affect both communication and measurement. Failed shortcut: Treating variation as noise makes systems work best for a narrow population and can turn a health or identity signal into an unwanted demographic shortcut. Recurring paper move: Measure which variation is task-relevant, model it explicitly when appropriate, and test performance and meaning across people and conditions. Neighbor test: The evidence concerns who is speaking and how that person's voice changes across time and state.

**What the papers share.** Voice depends on anatomy, age, health, emotion, language history, social setting, and equipment; these differences affect both communication and measurement. The subtheme asks: What ordinary speech pressure is handled by identity, age, and changing voice, and what evidence distinguishes it from neighboring pressures?

**Why the shortcut fails.** A first attempt would answer the question only with speaker verification, but that shortcut misses the boundary: Similarity scores are not identity proof and depend on enrollment quality, population, and decision threshold.

**The recurring move.** Across this subtheme, papers make speaker verification, age and developmental speech, within-speaker state variation explicit rather than treating the speech evidence as one undifferentiated variable. The reviewed full-paper mechanisms instantiate that move in different ways; for example: Initialize an interactive phonetic agent model with real speech from two Southern Italian varieties and simulate metaphony, then compare diphthongization and categorical contrasts.

### Words used in this section

**Speaker verification.** Decide whether two recordings plausibly came from the same person under channel, time, and content variation.
*Boundary:* Similarity scores are not identity proof and depend on enrollment quality, population, and decision threshold.

**Age and developmental speech.** Children and older adults differ in anatomy, articulation, vocabulary, and interaction needs, so adult data is not a neutral reference.
*Boundary:* Age prediction or age normalization can encode stereotypes and may not address the actual recognition failure.

**Within-speaker state variation.** The same person's voice shifts with fatigue, emotion, health, audience, and speaking effort; robust systems must not confuse state with identity.
*Boundary:* There is no universal stable identity vector independent of context.

### What the papers show

- [Agent-based modelling, sound change, and metaphony in Southern Italian varieties of Italo-Romance.](https://www.isca-archive.org/interspeech_2025/bressensdorf25_interspeech.html) (D3): Initialize an interactive phonetic agent model with real speech from two Southern Italian varieties and simulate metaphony, then compare diphthongization and categorical contrasts. **Measured or tested:** The study uses an agent-based computational model to test the hypothesis that contact between two dialects that are conservative and innovative as far as a sound change is concerned produces an asymmetric shift of the conservative speakers towards the innovative ones. **Limit:** The two dialects, 54 speakers collapsed to 13 agents, selected words, F1 trajectory representation, and model assumptions limit generalization to other communities or changes.
- [Pitch Target Realization in Putonghua Tone Production of Children from Dialect-Speaking Regions](https://www.isca-archive.org/interspeech_2025/cao25_interspeech.html) (D3): Analyze on-target and off-target realization as interacting targets shaped by physiology and dialect experience. **Measured or tested:** This study examines the production of Putonghua tones from both on- and off-target perspectives, using data from 139 children (aged 35–71 months) with Changli dialect exposure, drawn from the CL-CHILD corpus. **Limit:** The age range, dialect exposure, corpus, and tone inventory bound the developmental claim; longitudinal and other language environments remain open.
- [Towards Robust Speaker Recognition against Intrinsic Variation with Foundation Model Few-shot Tuning and Effective Speech Synthesis](https://www.isca-archive.org/interspeech_2025/chen25_interspeech.html) (D3): Use few-shot foundation-model tuning at enrollment and generate style-rich synthetic speech to expose time-varying and emotional conditions, with losses focused on unknown outliers. **Measured or tested:** Experiments demonstrate strong generalization across multiple time-varying and emotionally rich benchmarks. **Limit:** The claim is bounded to the synthetic-data choices, foundation model, enrollment protocol, and benchmarks; real aging trajectories, spoofing attacks, and fairness across groups remain open.
- [Pushing the Frontiers of Self-Distillation Prototypes Network with Dimension Regularization and Score Normalization](https://www.isca-archive.org/interspeech_2025/chen25f_interspeech.html) (D3): Add dimension regularization to a self-distillation prototype network and use score normalization to close the gap toward supervised verification. **Measured or tested:** SDPN with dimension regularization and score normalization sets a new state-of-the-art on the VoxCeleb1 speaker verification evaluation benchmark, achieving Equal Error Rate 1.29%, 1.60%, and 2.80% for trial VoxCeleb1-{O,E,H} respectively. **Limit:** VoxCeleb1, trial conditions, unlabeled-training setup, score normalization, and EER bound the claim; benchmark gains do not establish fairness or robustness in deployment.

**Where this boundary stops.** Similarity scores are not identity proof and depend on enrollment quality, population, and decision threshold.; Age prediction or age normalization can encode stereotypes and may not address the actual recognition failure.; There is no universal stable identity vector independent of context.

**What this evidence does not establish.** The shared story is supported only by the reviewed papers listed here; D2 entries support the problem and stated method, while D3 entries support the reported mechanism and evaluation. It is not a venue-wide prevalence claim.

**Question left open.** What changes when this move is tested outside the speakers, languages, rooms, devices, or benchmark conditions represented by the 18 D3 paper(s)?

## Speech measurements associated with health

**The question.** What ordinary speech pressure is handled by speech measurements associated with health, and what evidence distinguishes it from neighboring pressures?

**How this boundary is derived.** Baseline link: Fant pp. 6-7: physical signal parameters and message-level distinctions are related but not identical; this is the baseline for testing when speaker variation is useful evidence or nuisance. Ordinary pressure: Voice depends on anatomy, age, health, emotion, language history, social setting, and equipment; these differences affect both communication and measurement. Failed shortcut: Treating variation as noise makes systems work best for a narrow population and can turn a health or identity signal into an unwanted demographic shortcut. Recurring paper move: Measure which variation is task-relevant, model it explicitly when appropriate, and test performance and meaning across people and conditions. Neighbor test: A measurable speech property is evaluated as a possible health signal, with clinical limits kept explicit.

**What the papers share.** Voice depends on anatomy, age, health, emotion, language history, social setting, and equipment; these differences affect both communication and measurement. The subtheme asks: What ordinary speech pressure is handled by speech measurements associated with health, and what evidence distinguishes it from neighboring pressures?

**Why the shortcut fails.** A first attempt would answer the question only with clinical speech marker, but that shortcut misses the boundary: Association with a diagnosis is not clinical validity, causation, or permission to make a medical decision.

**The recurring move.** Across this subtheme, papers make clinical speech marker explicit rather than treating the speech evidence as one undifferentiated variable. The reviewed full-paper mechanisms instantiate that move in different ways; for example: Use acoustic-to-articulatory inversion to obtain interpretable movement variables, then test subtype differences with a mixed-effects statistical model across children and target sounds.

### Words used in this section

**Clinical speech marker.** Measure a reproducible speech property associated with a clinical condition or progression, while separating it from age, device, and language effects.
*Boundary:* Association with a diagnosis is not clinical validity, causation, or permission to make a medical decision.

### What the papers show

- [Subtyping Speech Errors in Childhood Speech Sound Disorders with Acoustic-to-Articulatory Speech Inversion](https://www.isca-archive.org/interspeech_2025/benway25_interspeech.html) (D3): Use acoustic-to-articulatory inversion to obtain interpretable movement variables, then test subtype differences with a mixed-effects statistical model across children and target sounds. **Measured or tested:** Speech inversion holds much potential to describe speech errors in childhood speech sound disorders. **Limit:** The study is limited to selected American-English child error types and an inversion model; clinical interpretability is demonstrated for these comparisons, not established for all disorders or speakers. No independent reproduction was performed.
- [Acoustic and Linguistic Biomarkers for Cognitive Impairment Detection from Speech](https://www.isca-archive.org/interspeech_2025/botelho25_interspeech.html) (D3): Combine acoustic, linguistic, knowledge-based, and neural representations, selecting complementary class-aware systems. **Measured or tested:** Based on our previous experience on the use of speech and text-derived biomarkers for disease detection, we evaluate here the use of knowledge-based acoustic and text-based feature sets, as well as LLM-based macro-descriptors, and multiple neural representations (e.g., Longformer, ECAPA-TDNN, and… **Limit:** Challenge data, demographic overlap, and missing metadata limit the claim; this is not clinical validation.
- [Pitfalls and Limits in Automatic Dementia Assessment](https://www.isca-archive.org/interspeech_2025/braun25_interspeech.html) (D3): Inspect the automated Syndrom-Kurz-Test pipeline by subgroup, transcription quality, item type, and fallback behavior rather than relying on one aggregate number. **Measured or tested:** Current work on speech-based dementia assessment focuses on either feature extraction to predict assessment scales, or on the automation of existing test procedures. **Limit:** This is an analysis of one standardized assessment and its data; it warns against clinical claims, not a universal ranking of dementia-screening systems.
- [Perception of Emotional Speech by Individuals with High Borderline Personality Features](https://www.isca-archive.org/interspeech_2025/chen25c_interspeech.html) (D3): Present Mandarin emotional speech at controlled intensities and compare emotion-identification accuracy and confusions for participants with high and low borderline-personality features. **Measured or tested:** High-BPF participants showed lower accuracy in identifying neutral speech, more frequently misidentifying it as other emotions, and were less accurate in identifying high-intensity happy speech, tending to misclassify it as neutral. **Limit:** Mandarin synthetic stimuli, university participants, self-report grouping, F0 manipulation, and perceptual task bound generalization; the findings do not diagnose BPD or explain all underlying causes.

**Where this boundary stops.** Association with a diagnosis is not clinical validity, causation, or permission to make a medical decision.

**What this evidence does not establish.** The shared story is supported only by the reviewed papers listed here; D2 entries support the problem and stated method, while D3 entries support the reported mechanism and evaluation. It is not a venue-wide prevalence claim.

**Question left open.** What changes when this move is tested outside the speakers, languages, rooms, devices, or benchmark conditions represented by the 10 D3 paper(s)?

## Communicating with atypical or impaired speech

**The question.** What ordinary speech pressure is handled by communicating with atypical or impaired speech, and what evidence distinguishes it from neighboring pressures?

**How this boundary is derived.** Baseline link: Fant pp. 6-7: physical signal parameters and message-level distinctions are related but not identical; this is the baseline for testing when speaker variation is useful evidence or nuisance. Ordinary pressure: Voice depends on anatomy, age, health, emotion, language history, social setting, and equipment; these differences affect both communication and measurement. Failed shortcut: Treating variation as noise makes systems work best for a narrow population and can turn a health or identity signal into an unwanted demographic shortcut. Recurring paper move: Measure which variation is task-relevant, model it explicitly when appropriate, and test performance and meaning across people and conditions. Neighbor test: The goal is recognition or expression for people whose speech does not match majority training data.

**What the papers share.** Voice depends on anatomy, age, health, emotion, language history, social setting, and equipment; these differences affect both communication and measurement. The subtheme asks: What ordinary speech pressure is handled by communicating with atypical or impaired speech, and what evidence distinguishes it from neighboring pressures?

**Why the shortcut fails.** A first attempt would answer the question only with atypical articulation and dysarthria, but that shortcut misses the boundary: Small datasets and speaker-specific patterns make broad claims especially fragile.

**The recurring move.** Across this subtheme, papers make atypical articulation and dysarthria, augmentative communication explicit rather than treating the speech evidence as one undifferentiated variable. The reviewed full-paper mechanisms instantiate that move in different ways; for example: Continue self-supervised pre-training on pathological speech, use etiology-specific codebooks, and select external examples by semantic similarity.

### Words used in this section

**Atypical articulation and dysarthria.** Recognize or synthesize speech whose timing, precision, or coordination differs from training norms instead of treating it as mere noise.
*Boundary:* Small datasets and speaker-specific patterns make broad claims especially fragile.

**Augmentative communication.** Use residual vocal, muscular, visual, or typed signals to help a person express intended language or control a device.
*Boundary:* A system should preserve the person's authorship and offer correction, not silently decide what they meant.

### What the papers show

- [Pathology-Aware Speech Encoding and Data Augmentation for Dysarthric Speech Recognition](https://www.isca-archive.org/interspeech_2025/baumann25_interspeech.html) (D3): Continue self-supervised pre-training on pathological speech, use etiology-specific codebooks, and select external examples by semantic similarity. **Measured or tested:** We achieve a 13.2% relative word error rate (WER) improvement using the pathology-aware speech encoder with etiology-specific continued pre-training. **Limit:** Etiologies, corpora, similarity model, and ratios bound the claim; improvements differ by condition and synthetic speech may not preserve clinical variation.
- [EEG-based Voice Conversion : Hearing the Voice of Your Brain](https://www.isca-archive.org/interspeech_2025/geng25b_interspeech.html) (D3): Align EEG features with speaker voice features and use a speech-trained zero-shot voice-conversion model. **Measured or tested:** The connection between Electroencephalography (EEG) signals and human voice has gained significant attention, with studies demonstrating the feasibility of speech synthesis from EEG data. **Limit:** Single words, EEG setup, target voices, and small dataset define the claim; intelligibility, privacy, consent, and real assistive communication remain open.
- [A Silent Speech Decoding System from EEG and EMG with Heterogenous Electrode Configurations](https://www.isca-archive.org/interspeech_2025/inoue25b_interspeech.html) (D3): Handle heterogeneous electrodes and use multitask training for cross-subject and cross-language calibration. **Measured or tested:** Silent speech decoding, which performs unvocalized human speech recognition from electroencephalography/electromyography (EEG/EMG), increases accessibility for speech-impaired humans. **Limit:** Patient count, setup, calibration, and author-reported results limit clinical deployment claims.
- [EEG-based Speech Decoding Based on Multi-mode Joint Modeling](https://www.isca-archive.org/interspeech_2025/li25j_interspeech.html) (D3): Train one model across modes with dynamic masking, then use its learned channel relevance to make a smaller single-mode decoder. **Measured or tested:** The accuracy improvements and channel selection capability demonstrate the effectiveness of the proposed joint modeling framework. **Limit:** The four-vowel task, participants, EEG hardware, mode definitions, and accuracy metric bound the result; it does not demonstrate unrestricted communication or clinical readiness.

**Where this boundary stops.** Small datasets and speaker-specific patterns make broad claims especially fragile.; A system should preserve the person's authorship and offer correction, not silently decide what they meant.

**What this evidence does not establish.** The shared story is supported only by the reviewed papers listed here; D2 entries support the problem and stated method, while D3 entries support the reported mechanism and evaluation. It is not a venue-wide prevalence claim.

**Question left open.** What changes when this move is tested outside the speakers, languages, rooms, devices, or benchmark conditions represented by the 9 D3 paper(s)?

## Whether the system actually helps a person

**The question.** What ordinary speech pressure is handled by whether the system actually helps a person, and what evidence distinguishes it from neighboring pressures?

**How this boundary is derived.** Baseline link: Fant pp. 6-7: physical signal parameters and message-level distinctions are related but not identical; this is the baseline for testing when speaker variation is useful evidence or nuisance. Ordinary pressure: Voice depends on anatomy, age, health, emotion, language history, social setting, and equipment; these differences affect both communication and measurement. Failed shortcut: Treating variation as noise makes systems work best for a narrow population and can turn a health or identity signal into an unwanted demographic shortcut. Recurring paper move: Measure which variation is task-relevant, model it explicitly when appropriate, and test performance and meaning across people and conditions. Neighbor test: The target is effort, control, access, and fit in a real activity rather than model accuracy alone.

**What the papers share.** Voice depends on anatomy, age, health, emotion, language history, social setting, and equipment; these differences affect both communication and measurement. The subtheme asks: What ordinary speech pressure is handled by whether the system actually helps a person, and what evidence distinguishes it from neighboring pressures?

**Why the shortcut fails.** A first attempt would answer the question only with listener effort, but that shortcut misses the boundary: Effort measures depend on task, listener experience, and presentation conditions.

**The recurring move.** Across this subtheme, papers make listener effort, user control and consent, accessibility fit explicit rather than treating the speech evidence as one undifferentiated variable. The reviewed full-paper mechanisms instantiate that move in different ways; for example: Fuse STFT audio features with visual embeddings in a dual-branch CNN-BLSTM attention model and jointly predict PESQ and STOI.

### Words used in this section

**Listener effort.** Measure how much concentration, repetition, or repair a listener needs, not just whether a word error count changed.
*Boundary:* Effort measures depend on task, listener experience, and presentation conditions.

**User control and consent.** Let speakers decide how their voice is recorded, adapted, generated, shared, or corrected, especially when identity is involved.
*Boundary:* A consent checkbox does not solve power imbalance, downstream copying, or inability to withdraw a trained model.

**Accessibility fit.** Judge whether a system works within a person's actual device, environment, communication practice, and time constraints.
*Boundary:* A lab improvement can be irrelevant or harmful if setup, latency, or interaction burden is omitted.

### What the papers show

- [A Study on Speech Assessment with Visual Cues](https://www.isca-archive.org/interspeech_2025/ahmed25_interspeech.html) (D3): Fuse STFT audio features with visual embeddings in a dual-branch CNN-BLSTM attention model and jointly predict PESQ and STOI. **Measured or tested:** Evaluations on the LRS3-TED dataset, augmented with noise from the DEMAND corpus, show that our model outperforms the audio-only baseline. **Limit:** Seen-noise conditions, proxy targets, visual availability, dataset, and correlation metric limit transfer; proxy prediction is not a listener study.
- [Can We Trust Machine Learning? The Reliability of Features from Open-Source Speech Analysis Tools for Speech Modeling](https://www.isca-archive.org/interspeech_2025/chowdhury25_interspeech.html) (D3): Compare tools directly in the target population and test how feature differences alter models and group behavior. **Measured or tested:** We evaluate speech features extracted from two widely used speech analysis tools, OpenSMILE and Praat, to assess their reliability when considering adolescents with autism. **Limit:** The population, features, tools, and behavioral tasks define the boundary; the study does not identify one universally correct toolkit.
- [EAA: Emotion-Aware Audio Large Language Models with Dual Cross-Attention and Context-Aware Instruction Tuning](https://www.isca-archive.org/interspeech_2025/du25b_interspeech.html) (D3): Use dual cross-attention and context-aware instruction tuning for emotion-aware audio-language modeling. **Measured or tested:** Understanding speech emotion through artificial intelligence (AI) is crucial for human-computer interaction and mental health monitoring. **Limit:** Labels, prompts, audio quality, model, and human agreement bound transfer.
- [Speech stimulus design to study the neural coding of speech and the impact of cochlear synaptopathy](https://www.isca-archive.org/interspeech_2025/gaudrain25_interspeech.html) (D3): Analyze and resynthesize speech so temporal fine structure and other dimensions can be parametrically varied while preserving naturalistic speech cues. **Measured or tested:** Here, speech stimuli were designed to assess the involvement of a specific coding mechanism: the coding of temporal fine structure through phase-locking. **Limit:** Stimulus fidelity, resynthesis artifacts, listener population, language, and study protocol bound the inference; a designed cue isolates a mechanism only insofar as unedited cues remain controlled.

**Where this boundary stops.** Effort measures depend on task, listener experience, and presentation conditions.; A consent checkbox does not solve power imbalance, downstream copying, or inability to withdraw a trained model.; A lab improvement can be irrelevant or harmful if setup, latency, or interaction burden is omitted.

**What this evidence does not establish.** The shared story is supported only by the reviewed papers listed here; D2 entries support the problem and stated method, while D3 entries support the reported mechanism and evaluation. It is not a venue-wide prevalence claim.

**Question left open.** What changes when this move is tested outside the speakers, languages, rooms, devices, or benchmark conditions represented by the 19 D3 paper(s)?

## Closing note

This essay is a map of recurring problems and research moves, not a leaderboard or a claim that these categories cover every speech study. The paper links and depth labels show what was actually checked; they do not turn reported results into independent facts.
