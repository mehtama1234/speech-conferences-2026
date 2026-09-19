# Evidence, practical systems, and consequences

*Essay 8 of 8 in The Speech Atlas.*

A score is an observation, not a complete account of usefulness. This essay connects measurements to human goals, changing conditions, hardware limits, privacy, and the ability to inspect and challenge a claim.

## Start with the baseline

Fant's speech-chain account places this theme at the following point in communication: Fant pp. 3-4: a compact description should retain needed message information, but every description is approximate and task-dependent; scores must therefore be tied to the use they stand for.

The ordinary problem is simple to state: Speech systems are used through microphones, networks, interfaces, policies, and people; a benchmark number is only one observation of that whole chain.

One tempting shortcut is: Reporting one average score on one dataset encourages the reader to treat a proxy as universal ability and ignores latency, failure recovery, privacy, and misuse. It fails because it hides the distinction this essay needs to keep visible.

The recurring move across this theme is to align the evaluation with the real target, expose subgroup and condition variation, account for the full system boundary, and preserve an audit trail from evidence to claim. The cost is equally important: Broader evaluation costs time and data, but narrow evidence can create false confidence exactly where speech systems affect access, identity, or safety.

## The boundaries

Each section below uses the same test: what pressure is being handled, what shortcut fails, what move recurs, and where the evidence stops.

## Plain-language dictionary

The papers use specialized names because they measure specialized things. These are the terms that recur in this essay, translated before they do argumentative work:

**Fant's speech chain.** a practical way to follow speech from a speaker's body, through the air and a recording device, to a listener and an interpretation.
**D2.** evidence checked in the official paper abstract; it supports the paper's stated problem and approach, but not details that appear only in the full paper.
**D3.** evidence checked in the official full paper text; it supports what the authors report about their method and tests, but it is still not an independent reproduction.
**ASR.** automatic speech recognition: software that turns speech recordings into written words.
**TTS.** text-to-speech: software that turns written words into a spoken signal.
**speaker embedding.** a compact numerical description intended to preserve characteristics of a voice or speaker.
**self-supervised learning.** training in which the recording supplies part of its own teaching signal, so hand-written labels are needed less often.
**voice activity detection.** a decision about whether a signal segment contains speech.
**word error rate.** the number of word substitutions, insertions, and deletions divided by the reference word count.
**equal error rate.** the point at which two kinds of biometric decision error—false acceptance and false rejection—are equal.
**interaural.** between the two ears; an interaural difference is a difference in timing or level between left and right channels.
**MRI.** magnetic resonance imaging, used here to observe anatomy or movement without cutting into the body.
**EEG.** electroencephalography, a measurement of electrical activity at the scalp.
**MFCC.** a compact description of the broad shape of a sound spectrum, often used as an input feature.
**F0.** the rate of vocal-fold vibration, commonly heard as the main component of pitch.

This is a map of distinctions, not a ranking of methods. A paper can be useful while still answering only one narrow question.

## Connecting scores to human goals

This boundary follows from the baseline account: baseline link: Fant pp. 3-4: a compact description should retain needed message information, but every description is approximate and task-dependent; scores must therefore be tied to the use they stand for. Ordinary pressure: Speech systems are used through microphones, networks, interfaces, policies, and people; a benchmark number is only one observation of that whole chain. Failed shortcut: Reporting one average score on one dataset encourages the reader to treat a proxy as universal ability and ignores latency, failure recovery, privacy, and misuse. Recurring paper move: Align the evaluation with the real target, expose subgroup and condition variation, account for the full system boundary, and preserve an audit trail from evidence to claim. Neighbor test: A metric is a proxy and must be tied to the human or engineering property it represents.

**The question.** What ordinary speech pressure is handled by connecting scores to human goals, and what evidence distinguishes it from neighboring pressures?

**The pressure.** Speech systems are used through microphones, networks, interfaces, policies, and people; a benchmark number is only one observation of that whole chain. The subtheme asks: What ordinary speech pressure is handled by connecting scores to human goals, and what evidence distinguishes it from neighboring pressures?

**Why the easy answer breaks.** A first attempt would answer the question only with word error versus understanding, but that shortcut misses the boundary: A word metric can miss critical entity errors and can penalize harmless orthographic or dialect differences.

**The move that recurs.** Across this subtheme, papers make word error versus understanding, quality and naturalness, calibration and selective use explicit rather than treating the speech evidence as one undifferentiated variable. The reviewed full-paper mechanisms instantiate that move in different ways; for example: Combine CLAP similarity with repetition penalties, clipping, and LLM feedback during reward optimization.

### Words used in this section

**Word error versus understanding.** A transcript edit distance counts substitutions, insertions, and deletions, but a small count is not automatically successful task understanding.
*Boundary:* A word metric can miss critical entity errors and can penalize harmless orthographic or dialect differences.

**Quality and naturalness.** Listening ratings, preference tests, and signal measures estimate different aspects of whether generated or enhanced speech is acceptable.
*Boundary:* A score without listeners, conditions, and target definition cannot support a general quality claim.

**Calibration and selective use.** A system should know when its uncertainty is high enough to defer, ask, or show alternatives rather than making every output look certain.
*Boundary:* Calibration on a held-out sample does not guarantee safety under a new population or distribution.

### What the evidence shows

- [Optimizing CLAP Reward with LLM Feedback for Semantically Aligned and Diverse Automated Audio Captioning](https://www.isca-archive.org/interspeech_2025/ahn25b_interspeech.html) (D3): Combine CLAP similarity with repetition penalties, clipping, and LLM feedback during reward optimization. **Measured or tested:** To address this, reinforcement learning (RL) techniques have been adopted to directly optimize evaluation metrics, but these methods often suffer from word repetition and contextual distortion. **Limit:** The result depends on caption datasets, evaluator prompts, and reward weighting; human agreement and out-of-domain audio remain open.
- [SMARTMOS: Modeling Subjective Audio Quality Evaluation for Real-Time Applications](https://www.isca-archive.org/interspeech_2025/balasubramanian25_interspeech.html) (D3): Learn a model of subjective quality from listening-test ratings and design it for fast prediction in the intended real-time setting. **Measured or tested:** Evaluating audio quality is a crucial task, with subjective listening tests being the gold standard. **Limit:** Human ratings, test conditions, and audio distortions define the target; a predictor can reproduce annotator bias and fail on unseen codecs or populations. No independent reproduction was performed.
- [Intelligibility Prediction for Time-Modified Speech Signals Using Spectro-Temporal Modulation Features](https://www.isca-archive.org/interspeech_2025/bashir25_interspeech.html) (D3): Align clean and time-modified speech with selected spectro-temporal modulation features, then feed the alignment into existing reference-based intelligibility predictors. **Measured or tested:** Using these methods, we compare the output scores of the RB-SIPA with listening test scores and show better correlation results using the STM features as compared to MFCCs. **Limit:** The listening datasets, degradation types, chosen modulation channels, and reference availability bound the claim; correlation is not a complete model of listener experience.
- [Benchmarking and Confidence Evaluation of LALMs For Temporal Reasoning](https://www.isca-archive.org/interspeech_2025/bhattacharya25b_interspeech.html) (D3): Build the TREA temporal-reasoning dataset, benchmark audio language models against people, and measure uncertainty through invariance to semantically identical perturbations. **Measured or tested:** In this quest, large audio language models (LALMs) have to be evaluated on reasoning related tasks which are different from traditional classification or generation tasks. **Limit:** The dataset, perturbations, models, human comparison, and temporal tasks bound conclusions; invariance is one operational uncertainty test, not a complete account of confidence.

**Where this boundary stops.** A word metric can miss critical entity errors and can penalize harmless orthographic or dialect differences.; A score without listeners, conditions, and target definition cannot support a general quality claim.; Calibration on a held-out sample does not guarantee safety under a new population or distribution.

**What this evidence does not establish.** The shared story is supported only by the reviewed papers listed here; D2 entries support the problem and stated method, while D3 entries support the reported mechanism and evaluation. It is not a venue-wide prevalence claim.

**Question left open.** What changes when this move is tested outside the speakers, languages, rooms, devices, or benchmark conditions represented by the 19 D3 paper(s)?

## Changing speakers, rooms, and conditions

This boundary follows from the baseline account: baseline link: Fant pp. 3-4: a compact description should retain needed message information, but every description is approximate and task-dependent; scores must therefore be tied to the use they stand for. Ordinary pressure: Speech systems are used through microphones, networks, interfaces, policies, and people; a benchmark number is only one observation of that whole chain. Failed shortcut: Reporting one average score on one dataset encourages the reader to treat a proxy as universal ability and ignores latency, failure recovery, privacy, and misuse. Recurring paper move: Align the evaluation with the real target, expose subgroup and condition variation, account for the full system boundary, and preserve an audit trail from evidence to claim. Neighbor test: The question is whether failures are detected and recovered when conditions differ from training.

**The question.** What ordinary speech pressure is handled by changing speakers, rooms, and conditions, and what evidence distinguishes it from neighboring pressures?

**The pressure.** Speech systems are used through microphones, networks, interfaces, policies, and people; a benchmark number is only one observation of that whole chain. The subtheme asks: What ordinary speech pressure is handled by changing speakers, rooms, and conditions, and what evidence distinguishes it from neighboring pressures?

**Why the easy answer breaks.** A first attempt would answer the question only with distribution shift, but that shortcut misses the boundary: A named shift is not evidence of coverage; the shift must be measured and tied to the failure.

**The move that recurs.** Across this subtheme, papers make distribution shift, end-to-end recovery explicit rather than treating the speech evidence as one undifferentiated variable. The reviewed full-paper mechanisms instantiate that move in different ways; for example: Use annotated SFUSED speech errors to stratify WhisperX performance by error type and word position.

### Words used in this section

**Distribution shift.** Performance changes when speakers, microphones, rooms, languages, topics, or noise differ from training and test conditions.
*Boundary:* A named shift is not evidence of coverage; the shift must be measured and tied to the failure.

**End-to-end recovery.** Handle uncertainty through confirmation, correction, fallback, and logging so one recognition error does not become an irreversible action.
*Boundary:* A robust component is not an end-to-end safe system if downstream policy ignores its uncertainty.

### What the evidence shows

- [Evaluating ASR Robustness to Spontaneous Speech Errors: A Study of WhisperX Using a Speech Error Database](https://www.isca-archive.org/interspeech_2025/alderete25_interspeech.html) (D3): Use annotated SFUSED speech errors to stratify WhisperX performance by error type and word position. **Measured or tested:** The Simon Fraser University Speech Error Database (SFUSED) is a public data collection developed for linguistic and psycholinguistic research. **Limit:** Database, annotations, WhisperX, language, and task design limit generalization.
- [Defending Speech-enabled LLMs Against Adversarial Jailbreak Threats](https://www.isca-archive.org/interspeech_2025/alexos25_interspeech.html) (D3): Train with synthesized harmful and benign speech queries and test against strong white-box attacks across two model sizes and data configurations. **Measured or tested:** We experiment with different training data configurations, and evaluate the methods on strong white-box adversarial attacks. **Limit:** The two models, synthesized data, attack family, safety measure, and training recipe bound the result; robustness to unseen speakers, attacks, languages, and real-world misuse remains open.
- [Pushing the Limits of End-to-End Diarization](https://www.isca-archive.org/interspeech_2025/broughton25_interspeech.html) (D3): Use one end-to-end non-autoregressive model and scale pretraining across systematically represented eight-speaker mixtures. **Measured or tested:** In this paper, we present state-of-the-art diarization error rates (DERs) on multiple publicly available datasets, including AliMeeting-far, AliMeeting-near, AMI-Mix, AMI-SDM, DIHARD III, and MagicData RAMC. **Limit:** The simulations, corpora, speaker counts, and model speed define the boundary; spontaneous conditions beyond these meetings remain open.
- [Multi-Channel Sequence-to-Sequence Neural Diarization: Experimental Results for The MISP 2025 Challenge](https://www.isca-archive.org/interspeech_2025/cheng25b_interspeech.html) (D3): Generate initial predictions with sequence-to-sequence neural diarization, then refine them with multi-channel audio in MC-S2SND for the MISP challenge. **Measured or tested:** The final system achieves a diarization error rate (DER) of 8.09% on the evaluation set of the competition database, ranking first place in the speaker diarization task of the MISP 2025 Challenge. **Limit:** Challenge data, channel layout, scoring convention, enrollment assumptions, and test conditions bound generalization; rank and DER do not guarantee usable transcripts in every meeting.

**Where this boundary stops.** A named shift is not evidence of coverage; the shift must be measured and tied to the failure.; A robust component is not an end-to-end safe system if downstream policy ignores its uncertainty.

**What this evidence does not establish.** The shared story is supported only by the reviewed papers listed here; D2 entries support the problem and stated method, while D3 entries support the reported mechanism and evaluation. It is not a venue-wide prevalence claim.

**Question left open.** What changes when this move is tested outside the speakers, languages, rooms, devices, or benchmark conditions represented by the 7 D3 paper(s)?

## Meeting time, memory, and hardware limits

This boundary follows from the baseline account: baseline link: Fant pp. 3-4: a compact description should retain needed message information, but every description is approximate and task-dependent; scores must therefore be tied to the use they stand for. Ordinary pressure: Speech systems are used through microphones, networks, interfaces, policies, and people; a benchmark number is only one observation of that whole chain. Failed shortcut: Reporting one average score on one dataset encourages the reader to treat a proxy as universal ability and ignores latency, failure recovery, privacy, and misuse. Recurring paper move: Align the evaluation with the real target, expose subgroup and condition variation, account for the full system boundary, and preserve an audit trail from evidence to claim. Neighbor test: The system must operate within a device or interaction budget without hiding cost elsewhere.

**The question.** What ordinary speech pressure is handled by meeting time, memory, and hardware limits, and what evidence distinguishes it from neighboring pressures?

**The pressure.** Speech systems are used through microphones, networks, interfaces, policies, and people; a benchmark number is only one observation of that whole chain. The subtheme asks: What ordinary speech pressure is handled by meeting time, memory, and hardware limits, and what evidence distinguishes it from neighboring pressures?

**Why the easy answer breaks.** A first attempt would answer the question only with latency and resource budget, but that shortcut misses the boundary: A faster model may emit less context, reduce quality, or move cost into an unreported service.

**The move that recurs.** Across this subtheme, papers make latency and resource budget explicit rather than treating the speech evidence as one undifferentiated variable. The reviewed full-paper mechanisms instantiate that move in different ways; for example: Ablate frame rate, bitrate, and causality, then design NanoCodec around a low-rate operating point and compare reconstruction quality.

### Words used in this section

**Latency and resource budget.** A system must meet timing, memory, energy, bandwidth, and hardware limits while preserving the property users need.
*Boundary:* A faster model may emit less context, reduce quality, or move cost into an unreported service.

### What the evidence shows

- [NanoCodec: Towards High-Quality Ultra Fast Speech LLM Inference](https://www.isca-archive.org/interspeech_2025/casanova25_interspeech.html) (D3): Ablate frame rate, bitrate, and causality, then design NanoCodec around a low-rate operating point and compare reconstruction quality. **Measured or tested:** NanoCodec outperforms related works across various bitrate ranges, establishing a new benchmark for low-latency and efficient Speech LLM training and inference. **Limit:** Audio domain, codec training data, perceptual metric, hardware, and causality setting bound transfer; codec quality is not end-to-end speech generation quality.
- [Breaking Resource Barriers in Speech Emotion Recognition via Data Distillation](https://www.isca-archive.org/interspeech_2025/chang25d_interspeech.html) (D3): Distill the original emotional speech into a smaller synthesized dataset and test whether models trained on it retain emotion-recognition performance. **Measured or tested:** Speech emotion recognition (SER) plays a crucial role in human-computer interaction. **Limit:** The distillation procedure, emotion labels, source corpora, privacy threat model, model initialization, and UAR evaluation bound the claim; smaller data is not automatically private or representative.
- [PruneSLU: Efficient On-device Spoken Language Understanding through Vocabulary and Structural Pruning](https://www.isca-archive.org/interspeech_2025/do25_interspeech.html) (D3): Prune task-irrelevant vocabulary first, prune layers structurally, then refine with distillation and contrastive losses. **Measured or tested:** Experiments on the STOP and SLURP datasets demonstrate that PruneSLU compresses a 39M model to 15M while retaining 98\% of its original performance, outperforming previous compression techniques. **Limit:** STOP/SLURP domains, Whisper initialization, five seeds, and author-reported comparisons bound the result; energy and open-world commands are not tested.
- [GTA: Towards Generative Text-To-Audio Retrieval via Multi-Scale Tokenizer](https://www.isca-archive.org/interspeech_2025/fang25c_interspeech.html) (D3): Use a multi-scale tokenizer and generative retrieval architecture with explicit resource tradeoffs. **Measured or tested:** Currently, mainstream approaches primarily employ a dual-tower architecture, independently encoding text and audio while performing similarity score matching. **Limit:** Audio, prompts, token rates, metrics, hardware, and generation budget bound transfer.

**Where this boundary stops.** A faster model may emit less context, reduce quality, or move cost into an unreported service.

**What this evidence does not establish.** The shared story is supported only by the reviewed papers listed here; D2 entries support the problem and stated method, while D3 entries support the reported mechanism and evaluation. It is not a venue-wide prevalence claim.

**Question left open.** What changes when this move is tested outside the speakers, languages, rooms, devices, or benchmark conditions represented by the 11 D3 paper(s)?

## Protecting voice and resisting misuse

This boundary follows from the baseline account: baseline link: Fant pp. 3-4: a compact description should retain needed message information, but every description is approximate and task-dependent; scores must therefore be tied to the use they stand for. Ordinary pressure: Speech systems are used through microphones, networks, interfaces, policies, and people; a benchmark number is only one observation of that whole chain. Failed shortcut: Reporting one average score on one dataset encourages the reader to treat a proxy as universal ability and ignores latency, failure recovery, privacy, and misuse. Recurring paper move: Align the evaluation with the real target, expose subgroup and condition variation, account for the full system boundary, and preserve an audit trail from evidence to claim. Neighbor test: This boundary covers harm from exposing voice identity or accepting imitation, replay, or generated speech as genuine; it is separate from ordinary robustness because the failure is unauthorized inference or deception, not merely a lower score in a changed condition.

**The question.** What ordinary speech pressure is handled by protecting voice and resisting misuse, and what evidence distinguishes it from neighboring pressures?

**The pressure.** Speech systems are used through microphones, networks, interfaces, policies, and people; a benchmark number is only one observation of that whole chain. The subtheme asks: What ordinary speech pressure is handled by protecting voice and resisting misuse, and what evidence distinguishes it from neighboring pressures?

**Why the easy answer breaks.** A first attempt would answer the question only with voice privacy, but that shortcut misses the boundary: Removing words does not necessarily remove speaker identity or sensitive acoustic information.

**The move that recurs.** Across this subtheme, papers make voice privacy, spoofing and synthetic voice misuse explicit rather than treating the speech evidence as one undifferentiated variable. The reviewed full-paper mechanisms instantiate that move in different ways; for example: Build a documented pipeline for high-quality bona-fide data, transcription-based segmentation, and several synthesis regimes, then measure naturalness and confusion.

### Words used in this section

**Voice privacy.** Speech recordings reveal content and may reveal identity, health, location, emotion, or group membership, so collection and storage are part of the technical problem.
*Boundary:* Removing words does not necessarily remove speaker identity or sensitive acoustic information.

**Spoofing and synthetic voice misuse.** A system must distinguish authorized speech from replayed or generated audio when identity or access depends on it.
*Boundary:* A detector trained on known generators can fail on unseen synthesis, replay channels, or an attacker who changes the interaction.

### What the evidence shows

- [Collecting, Curating, and Annotating Good Quality Speech deepfake dataset for Famous Figures: Process and Challenges](https://www.isca-archive.org/interspeech_2025/ali25_interspeech.html) (D3): Build a documented pipeline for high-quality bona-fide data, transcription-based segmentation, and several synthesis regimes, then measure naturalness and confusion. **Measured or tested:** The resulting dataset comprises bonafide and synthetic speech samples from ten public figures, demonstrating superior quality with a NISQA-TTS naturalness score of 3.69 and the highest human misclassification rate of 61.9%. **Limit:** The ten figures, synthesis systems, listeners, and dataset protocol bound the result; new generators and adversarially chosen public speech remain open.
- [ATMM-SAGA: Alternating Training for Multi-Module with Score-Aware Gated Attention SASV system](https://www.isca-archive.org/interspeech_2025/asali25_interspeech.html) (D3): Alternate training of speaker and anti-spoofing modules and use score-aware gated attention to combine their evidence. **Measured or tested:** The objective of automatic speaker verification (ASV) systems is to determine whether a given test speech utterance corresponds to a claimed enrolled speaker. **Limit:** Thresholds and spoof types determine operating behavior; benchmark attacks do not exhaust unseen synthesis or replay conditions. No independent reproduction was performed.
- [WavShape: Information-Theoretic Speech Representation Learning for Fair and Privacy-Aware Audio Processing](https://www.isca-archive.org/interspeech_2025/baser25_interspeech.html) (D3): Optimize mutual information in two directions: reduce dependence between the public embedding and sensitive labels while retaining dependence with task labels and the original speech representation. **Measured or tested:** Experimental results on three known datasets show that WavShape reduces MI between embeddings and sensitive attributes by up to 81% while retaining 97% of task-relevant information. **Limit:** Mutual-information estimation depends on the estimator, labels, datasets, and chosen sensitive attributes; unmeasured attributes or powerful attackers may still recover information. The figures are author-reported, and no independent privacy attack or reproduction was performed.
- [PhonemeFake: Redefining Deepfake Realism with Language-Driven Segmental Manipulation and Adaptive Bilevel Detection](https://www.isca-archive.org/interspeech_2025/baser25b_interspeech.html) (D3): Use language reasoning to choose critical phoneme segments for manipulation, then detect those regions with an adaptive two-level model. **Measured or tested:** However, our study reveals that existing DF datasets fail to deceive human perception, unlike real DF attacks that influence public discourse. **Limit:** These are author-reported results tied to attack construction, datasets, detector thresholds, and the chosen language reasoning; unseen generators and adversarial adaptation remain open.

**Where this boundary stops.** Removing words does not necessarily remove speaker identity or sensitive acoustic information.; A detector trained on known generators can fail on unseen synthesis, replay channels, or an attacker who changes the interaction.

**What this evidence does not establish.** The shared story is supported only by the reviewed papers listed here; D2 entries support the problem and stated method, while D3 entries support the reported mechanism and evaluation. It is not a venue-wide prevalence claim.

**Question left open.** What changes when this move is tested outside the speakers, languages, rooms, devices, or benchmark conditions represented by the 19 D3 paper(s)?

## Keeping claims inspectable and contestable

This boundary follows from the baseline account: baseline link: Fant pp. 3-4: a compact description should retain needed message information, but every description is approximate and task-dependent; scores must therefore be tied to the use they stand for. Ordinary pressure: Speech systems are used through microphones, networks, interfaces, policies, and people; a benchmark number is only one observation of that whole chain. Failed shortcut: Reporting one average score on one dataset encourages the reader to treat a proxy as universal ability and ignores latency, failure recovery, privacy, and misuse. Recurring paper move: Align the evaluation with the real target, expose subgroup and condition variation, account for the full system boundary, and preserve an audit trail from evidence to claim. Neighbor test: A person must be able to trace evidence, uncertainty, and correction when a speech system matters.

**The question.** What ordinary speech pressure is handled by keeping claims inspectable and contestable, and what evidence distinguishes it from neighboring pressures?

**The pressure.** Speech systems are used through microphones, networks, interfaces, policies, and people; a benchmark number is only one observation of that whole chain. The subtheme asks: What ordinary speech pressure is handled by keeping claims inspectable and contestable, and what evidence distinguishes it from neighboring pressures?

**Why the easy answer breaks.** A first attempt would answer the question only with auditability and contestability, but that shortcut misses the boundary: A stored confidence number is not an explanation of what evidence drove the decision.

**The move that recurs.** Across this subtheme, papers make auditability and contestability explicit rather than treating the speech evidence as one undifferentiated variable. The reviewed full-paper mechanisms instantiate that move in different ways; for example: Build an interactive platform that converts the same user prompt into alternative voices, shows paired model responses, and combines direct inspection with automated speech, sentiment, quality, pitch, and semantic-consistency measures.

### Words used in this section

**Auditability and contestability.** Keep enough provenance, uncertainty, and correction path for a person to understand and challenge a consequential speech-derived decision.
*Boundary:* A stored confidence number is not an explanation of what evidence drove the decision.

### What the evidence shows

- [Hear Me Out: Interactive evaluation and bias discovery platform for speech-to-speech conversational AI](https://www.isca-archive.org/interspeech_2025/bokkahallisatish25_interspeech.html) (D3): Build an interactive platform that converts the same user prompt into alternative voices, shows paired model responses, and combines direct inspection with automated speech, sentiment, quality, pitch, and semantic-consistency measures. **Measured or tested:** ‘Hear Me Out’ evaluates their ability to preserve crucial vocal cues, enabling users to explore how variations in speaker characteristics and paralinguistic features influence AI responses. **Limit:** The work is a platform/demo, not a powered user study or population-level fairness audit; its automated metrics and selected voice profiles constrain what can be observed. The authors explicitly call for larger studies and additional bias metrics, and no independent reproduction was performed.
- [FaiST: A Benchmark Dataset for Fairness in Speech Technology](https://www.isca-archive.org/interspeech_2025/jahan25_interspeech.html) (D3): Create a benchmark that measures fairness across speech-technology tasks and demographic or linguistic conditions with explicit group-level evidence. **Measured or tested:** To help combat this problem, we are introducing FaiST (Fairness in Speech Technology), a novel speech dataset from American English speakers of various racial, ethnic, and national origin groups. **Limit:** Group definitions, labels, sample balance, tasks, metrics, and consent bound the conclusions; benchmark parity is not proof of social fairness.
- [A Comprehensive Real-World Assessment of Audio Watermarking Algorithms: Will They Survive Neural Codecs?](https://www.isca-archive.org/interspeech_2025/ozer25_interspeech.html) (D3): Evaluate audio-watermarking algorithms under a broad real-world transformation suite, including neural codecs, and compare detectability and audio quality. **Measured or tested:** We present the Robust Audio Watermarking Benchmark (RAW-Bench) to foster the evaluation of deep learning-based audio watermarking algorithms, establishing a standardized benchmark and allowing systematic comparisons. **Limit:** Algorithms, codec versions, payloads, thresholds, and attack suite bound the result; survival in tested codecs is not universal tamper resistance.

**Where this boundary stops.** A stored confidence number is not an explanation of what evidence drove the decision.

**What this evidence does not establish.** The shared story is supported only by the reviewed papers listed here; D2 entries support the problem and stated method, while D3 entries support the reported mechanism and evaluation. It is not a venue-wide prevalence claim.

**Question left open.** What changes when this move is tested outside the speakers, languages, rooms, devices, or benchmark conditions represented by the 3 D3 paper(s)?

## Closing note

This essay is a map of recurring problems and research moves, not a leaderboard or a claim that these categories cover every speech study. The paper links and depth labels show what was actually checked; they do not turn reported results into independent facts.
