# INTERSPEECH 2025 nineteenth-pass full-paper notes

Twenty-three additional official-PDF readings add mechanism contrasts across the subthemes; one selected PDF remained text-extraction-limited and is recorded in the capture manifest. Results are author-reported and not independently reproduced.

## 1. accent-and-cultural-boundaries

**Paper:** [The ML-SUPERB 2.0 Challenge: Towards Inclusive ASR Benchmarking for All Language Varieties](https://www.isca-archive.org/interspeech_2025/chen25h_interspeech.html)
**Evidence:** D3; PDF SHA-256 `a7c7038485e71a36cdaf86e753293f96bf99bef574c403807f43e16fbc3b0b26`; full text captured.

- **Ordinary problem:** ASR should work across languages, accents, and dialects rather than only on well-resourced standard varieties.
- **Why hard:** A single average benchmark can hide failures on communities that have little representation in training or evaluation.
- **Naive attempt:** Report one multilingual score on a narrow, convenient test set.
- **Central move:** Build a broad public test suite and an online evaluation process that makes language-variety performance visible.
- **Mechanism:** ML-SUPERB 2.0 evaluates models on 200+ languages, accents, and dialects through DynaBench and compares five challenge submissions with baselines.
- **Conceptual structure:** Language-identification accuracy and character error rate are reported separately for general, accented, and dialectal speech.
- **What paper reports:** The best submission reports 23% absolute LID improvement and 18% CER reduction generally, with 30.2% lower CER and 15.7% higher LID accuracy on accented/dialectal data.
- **Limits:** Challenge submissions, test-suite composition, and hidden evaluation define the boundary; the results do not prove equal service quality for every language variety.

## 2. acoustic-unit-mapping

**Paper:** [CHSER: A Dataset and Case Study on Generative Speech Error Correction for Child ASR](https://www.isca-archive.org/interspeech_2025/balajishankar25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `90415e1d635fa623cb761604c0e889418daf65548791bc62e0c74c79220af0bb`; full text captured.

- **Ordinary problem:** Child ASR needs a correction stage that fixes transcription errors without turning child-specific disfluencies into fluent but wrong text.
- **Why hard:** Child speech has unusual acoustics and language patterns, and child error-correction data are scarce.
- **Naive attempt:** Apply adult speech error correction directly to child hypotheses.
- **Central move:** Create a large hypothesis-to-reference dataset for children and learn a generative correction model whose errors can be inspected by type.
- **Mechanism:** CHSER contains 200K pairs across ages and speaking styles; fine-tuned generative correction is tested in zero-shot and ASR-fine-tuned settings.
- **Conceptual structure:** Word error rate measures overall correction, while substitution, deletion, insertion, and disfluency analysis show which errors are changed.
- **What paper reports:** The paper reports up to 28.5% relative WER reduction zero-shot and 13.3% after ASR fine-tuning, but insertions and child disfluencies remain difficult.
- **Limits:** The corpus, languages, ASR hypotheses, and correction model bound the result; preserving clinically meaningful disfluencies outside these settings remains open.

## 3. adaptation-and-open-vocabulary

**Paper:** [Effect of Loudspeaker Emitted Speech on ASR performance](https://www.isca-archive.org/interspeech_2025/cm25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `ba177e974c1652435b81689a3b1d2636da6b518d72992c736b12d3e348b0e9fd`; full text captured.

- **Ordinary problem:** An ASR system should recognize speech played through a loudspeaker, not only clean speech recorded directly by a microphone.
- **Why hard:** Loudspeaker playback changes the acoustic path and can add coloration, reverberation, and level differences that the recognizer may mistake for speech variation.
- **Naive attempt:** Train and test on direct recordings, then assume the model will transfer to playback speech.
- **Central move:** Measure the distribution shift caused by loudspeaker emission and evaluate recognition under that realistic channel.
- **Mechanism:** The paper studies ASR performance for loudspeaker-emitted speech and compares recognition across the tested playback conditions.
- **Conceptual structure:** Word error rate exposes the channel penalty; the useful distinction is speech content versus the acoustic path that carries it.
- **What paper reports:** The paper reports a measurable ASR impact from loudspeaker emission under its experimental conditions.
- **Limits:** The result is bounded to the loudspeaker, room, microphones, and ASR systems tested; other devices and adaptive compensation remain open.

## 4. boundaries-and-sequence-structure

**Paper:** [A semi-automatic pipeline for transcribing and segmenting child speech](https://www.isca-archive.org/interspeech_2025/christodoulidou25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `b81ad4f3ec8943df20ccde351cc256baf68fdc150dd328cdc28fba1fb424728d`; full text captured.

- **Ordinary problem:** Researchers need vowel measurements from child field recordings without manually transcribing and aligning every sample.
- **Why hard:** Child speech, dialect, recording conditions, and imperfect boundaries make automatic alignment unreliable.
- **Naive attempt:** Trust an automatic transcript and forced alignment without checking its acoustic measurements.
- **Central move:** Use a semi-automatic pipeline, manually correct transcripts, and adapt the alignment model toward the child dialect.
- **Mechanism:** WhisperX transcription and MFA alignment are evaluated on 275 Scottish-English children; acoustic vowel measures are compared with manual annotation.
- **Conceptual structure:** Agreement of vowel measures with manual data is the target; transcript correction and acoustic-model adaptation are separate interventions.
- **What paper reports:** Manual correction improves measures, adaptation helps, and more training data does not automatically add improvement.
- **Limits:** The result is tied to Scottish English, field recordings, and vowel measurements; other ages, dialects, and measures need separate validation.

## 5. clinical-and-assistive-speech

**Paper:** [Comparative Evaluation of Acoustic Feature Extraction Tools for Clinical Speech Analysis](https://www.isca-archive.org/interspeech_2025/choi25h_interspeech.html)
**Evidence:** D3; PDF SHA-256 `e221953deaf74e1d91ba9746a8eb4c8b93db25ec7b1ced8e933196247d4966ac`; full text captured.

- **Ordinary problem:** Clinical speech studies need acoustic features that mean the same thing when extracted by different tools.
- **Why hard:** OpenSMILE, Praat, and Librosa can implement nominally similar features differently, changing a model's clinical conclusion.
- **Naive attempt:** Use one toolkit and treat its feature names as interchangeable with another toolkit's names.
- **Central move:** Standardize extraction settings, compare tools directly, and test whether disagreements change group classification.
- **Mechanism:** Three toolkits are applied to 77 schizophrenia-spectrum and 87 control speakers; correlations and classification performance are compared.
- **Conceptual structure:** Feature correlations, agreement for F0/formants, and AUC reveal whether a feature is reproducible and useful for discrimination.
- **What paper reports:** F0 percentile agreement is high, but F0 variation and formants can disagree or even correlate negatively; F0 mean, HNR, and MFCC1 exceed AUC .70 in the reported classification.
- **Limits:** The clinical groups, recordings, parameter choices, and tool versions define the boundary; no clinical diagnosis or deployment safety follows from these correlations.

## 6. dialogue-and-turn-taking

**Paper:** [Rapport-Building Dialogue Strategies for Deeper Connection: Integrating Proactive Behavior, Personalization, and Aizuchi Backchannels](https://www.isca-archive.org/interspeech_2025/baihaqi25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `de62a7e39aabd6b88a87b36d134c9fab6013ff6bd4c6fd64ea63924f5bf2a6d0`; full text captured.

- **Ordinary problem:** A conversational agent should build rapport by responding proactively, personally, and with small listener signals rather than waiting for explicit requests.
- **Why hard:** Naturalness depends on timing and interaction, so a response strategy can affect both dialogue flow and a person's willingness to share.
- **Naive attempt:** Optimize a language model for task content while ignoring backchannels and stalls.
- **Central move:** Prompt an LLM with a coordinated strategy for proactive behavior, personalization, and aizuchi backchannels, then measure both conversation and participant outcomes.
- **Mechanism:** CO-STAR and few-shot prompts drive a robot in human-robot interaction; stalls, dialogue similarity, robot backchannels, participant behavior, and questionnaires are evaluated.
- **Conceptual structure:** The paper separates system behavior from participant behavior and subjective reports rather than treating one dialogue score as rapport.
- **What paper reports:** The integrated strategy is reported to improve behavioral and subjective rapport measures.
- **Limits:** The study is bounded to the robot, prompts, participants, and short interaction protocol; long-term trust, cultural variation, and causal attribution remain open.

## 7. echo-and-reconstruction

**Paper:** [Listen through the Sound: Generative Speech Restoration Leveraging Acoustic Context Representation](https://www.isca-archive.org/interspeech_2025/chung25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `d8adca081f35bca40cff9dc160e77c0ab5d808d8cfc49dd72bd0fe9ba29edf8c`; full text captured.

- **Ordinary problem:** Speech restoration should use clues about the recording environment to undo distortion without mistaking the environment for speech content.
- **Why hard:** The same linguistic content can be damaged differently by noise, reverberation, or other conditions.
- **Naive attempt:** Condition a generator only on linguistic or speaker representations.
- **Central move:** Add an acoustic-context representation that describes the distortion and its intensity, then condition the restoration model on it.
- **Mechanism:** ACX refines CLAP-derived environmental embeddings and conditions the diffusion restoration model UNIVERSE++ across distortion conditions.
- **Conceptual structure:** Restoration quality and stability across conditions compare context-aware and content-based conditioning; variability itself is an evaluation target.
- **What paper reports:** The paper reports better restoration and reduced performance variability with acoustic context.
- **Limits:** The result is tied to the distortion set, CLAP features, and diffusion backbone; unseen devices, rooms, and perceptual listeners remain open.

## 8. grounding-and-action

**Paper:** [Co-Speech Motion for Virtual Agents in Dialogue Using LLM-Driven Primitive Action Selection](https://www.isca-archive.org/interspeech_2025/baihaqi25b_interspeech.html)
**Evidence:** D3; PDF SHA-256 `cfa82ec0ba9faa7f318f26b898e9e88c3b0e1e139ba6aeab5946752ff63d6b0b`; full text captured.

- **Ordinary problem:** A virtual agent should move in ways that fit what it is saying without requiring a hand-written rule for every situation.
- **Why hard:** Rules do not generalize, while purely data-driven gesture generation is costly and often tied to one embodiment.
- **Naive attempt:** Choose gestures from fixed rules or train a large motion generator for each agent.
- **Central move:** Use an LLM to plan context and select reusable primitive actions that can be adapted across agents.
- **Mechanism:** The proposed model uses LLM-driven primitive action selection for co-speech motion in virtual agents and robots.
- **Conceptual structure:** The operative object is a mapping from dialogue context to a sequence of reusable primitive actions; the captured paper does not establish a completed quantitative comparison.
- **What paper reports:** The paper presents a flexible and scalable approach, but the preserved evidence does not establish a numerical gain.
- **Limits:** Full mechanism, baselines, human judgments, and cross-embodiment transfer require the paper's detailed evaluation; the result is not a claim of human-like motion.

## 9. human-centered-evaluation

**Paper:** [Can We Trust Machine Learning? The Reliability of Features from Open-Source Speech Analysis Tools for Speech Modeling](https://www.isca-archive.org/interspeech_2025/chowdhury25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `583697ce22a6c66bcddb986f75cbc3c9538ce206a54892c5834d598228fb23c4`; full text captured.

- **Ordinary problem:** Speech features used in behavioral or clinical models should measure the intended behavior consistently across people and contexts.
- **Why hard:** Open-source tools can disagree, and those disagreements can change model performance unevenly across demographic groups.
- **Naive attempt:** Extract features from a familiar toolkit and assume the outputs are reliable.
- **Central move:** Compare tools directly in the target population and test how feature differences alter models and group behavior.
- **Mechanism:** OpenSMILE and Praat features are evaluated on adolescents with autism from audio-visual recordings, with model performance compared across contexts and demographics.
- **Conceptual structure:** Feature agreement and downstream classification are both measured; this connects measurement reliability to fairness rather than stopping at correlation.
- **What paper reports:** The paper reports considerable tool variation that influences model performance across context and demographic groups.
- **Limits:** The population, features, tools, and behavioral tasks define the boundary; the study does not identify one universally correct toolkit.

## 10. low-resource-and-data-creation

**Paper:** [MSDA: Combining Pseudo-labeling and Self-Supervision for Unsupervised Domain Adaptation in ASR](https://www.isca-archive.org/interspeech_2025/damianos25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `233530f3ab0d6ed7c8109727fac796e34a937320113dca8862414ace505d4156`; full text captured.

- **Ordinary problem:** ASR should adapt to a new or low-resource domain when labels are scarce or noisy.
- **Why hard:** Pseudo-label errors can reinforce themselves, while self-supervised adaptation alone may not learn the task boundary.
- **Naive attempt:** Fine-tune only on the small labeled target set or apply one adaptation technique in isolation.
- **Central move:** Cascade self-supervised representation adaptation with pseudo-label training so each stage prepares the next.
- **Mechanism:** MSDA evaluates a two-stage Meta PL pipeline for Greek and weakly supervised ASR, with ablations of the cascade.
- **Conceptual structure:** Recognition error and ablations test whether the order of self-supervision and self-training matters.
- **What paper reports:** The paper reports state-of-the-art results and finds the cascading combination necessary in its experiments.
- **Limits:** The languages, pseudo-label quality, source models, and domain shifts bound the claim; robustness to severely wrong pseudo-labels remains open.

## 11. metrics-and-targets

**Paper:** [Optimizing CLAP Reward with LLM Feedback for Semantically Aligned and Diverse Automated Audio Captioning](https://www.isca-archive.org/interspeech_2025/ahn25b_interspeech.html)
**Evidence:** D3; PDF SHA-256 `689b94f24303b766fee46c074cf3f87f158247679e4b54b4717a146d221f2ca2`; full text captured.

- **Ordinary problem:** An audio captioner should describe what happened naturally and accurately, not exploit a similarity score with repeated or awkward words.
- **Why hard:** CLAP rewards can favor semantically related phrases while ignoring repetition and human naturalness.
- **Naive attempt:** Optimize one embedding similarity metric directly.
- **Central move:** Combine CLAP similarity with repetition penalties, clipping, and LLM feedback during reward optimization.
- **Mechanism:** CRRP trains an automated audio-captioning system with a stabilized CLAP reward and an LLM evaluator; semantic, human, and AI assessments are compared.
- **Conceptual structure:** The reward combines semantic alignment and language naturalness, while multiple evaluations expose metric-specific behavior.
- **What paper reports:** The paper reports strong semantic and human/AI evaluation results for the proposed reward system.
- **Limits:** The result depends on caption datasets, evaluator prompts, and reward weighting; human agreement and out-of-domain audio remain open.

## 12. multilingual-and-crosslingual

**Paper:** [ADI-20: Arabic Dialect Identification dataset and models](https://www.isca-archive.org/interspeech_2025/elleuch25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `6a9c4b54f8abef4f48b40d4968ff771d2594cd2fb39d7819226ffc168b713442`; full text captured.

- **Ordinary problem:** A dialect identifier should distinguish all Arabic varieties without requiring the data and model size of a full-resource system.
- **Why hard:** Dialects share language identity while differing in sound and vocabulary, and country coverage is uneven.
- **Naive attempt:** Train on a few prominent dialects or assume a large model automatically solves data imbalance.
- **Central move:** Release broad data and compare pretrained encoders, data-size reduction, and model capacity directly.
- **Mechanism:** ADI-20 contains 3,556 hours across 19 dialects plus MSA; ECAPA-TDNN and Whisper encoder systems are evaluated.
- **Conceptual structure:** F1 measures dialect identification while controlled reductions test the value of data volume and parameters.
- **What paper reports:** Using 30% of the original data causes only a small F1 decrease in the reported experiments.
- **Limits:** The country/dialect inventory, labels, and data collection define the boundary; conversational code-switching and unrepresented varieties remain open.

## 13. noise-enhancement

**Paper:** [QUADS: Quantized Distillation Framework for Efficient Speech Language Understanding](https://www.isca-archive.org/interspeech_2025/biswas25b_interspeech.html)
**Evidence:** D3; PDF SHA-256 `a400df07f4284c07ba0f362cbe5f72c29be15e8b7ed4f0f383082ce6f02198d3`; full text captured.

- **Ordinary problem:** Spoken-language understanding must fit a constrained device without losing intent and slot decisions.
- **Why hard:** Distillation can preserve a teacher's behavior that later quantization cannot represent.
- **Naive attempt:** Compress by distillation and quantize afterward as unrelated steps.
- **Central move:** Train the student with distillation and quantization constraints together through multiple stages.
- **Mechanism:** QUADS jointly optimizes a pretrained SLU model for low-bit regimes and evaluates it on SLURP and FSC.
- **Conceptual structure:** Accuracy measures task retention, while GMACs and model size measure compute and storage cost.
- **What paper reports:** The paper reports 71.13% SLURP and 99.20% FSC accuracy, 60–73x lower GMACs, and 83–700x smaller models with bounded degradation.
- **Limits:** The result depends on tasks, bit settings, and hardware interpretation of the counts; latency and energy on deployed devices remain open.

## 14. privacy-security-and-accountability

**Paper:** [Collecting, Curating, and Annotating Good Quality Speech deepfake dataset for Famous Figures: Process and Challenges](https://www.isca-archive.org/interspeech_2025/ali25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `65637a57f2597e766eb0674c6c7154a0484792611b8c2031968cd04a563f1e36`; full text captured.

- **Ordinary problem:** A deepfake dataset for public figures should resemble the speech impersonation attacks people actually encounter, not merely contain clean synthetic clips.
- **Why hard:** Collection, segmentation, synthesis method, and speaker identity all affect how realistic a fake sounds.
- **Naive attempt:** Collect convenient speech and generate one kind of synthetic audio without checking human confusion.
- **Central move:** Build a documented pipeline for high-quality bona-fide data, transcription-based segmentation, and several synthesis regimes, then measure naturalness and confusion.
- **Mechanism:** The paper creates bona-fide and synthetic speech for ten public figures and reports NISQA-TTS and human misclassification.
- **Conceptual structure:** Dataset composition, automated naturalness, and human confusion measure different parts of realism.
- **What paper reports:** The dataset reports NISQA-TTS naturalness 3.69 and a highest human misclassification rate of 61.9%.
- **Limits:** The ten figures, synthesis systems, listeners, and dataset protocol bound the result; new generators and adversarially chosen public speech remain open.

## 15. prosody-and-intent

**Paper:** [Robot-assisted Recognition of Vocal Emotions in Pseudospeech for Cochlear Implanted Adolescents](https://www.isca-archive.org/interspeech_2025/araizaillan25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `cbd8dd677e17cdda5e2d152c1651e137c43e2619e6bd06c08e516646a587e3f1`; full text captured.

- **Ordinary problem:** A hearing test for adolescents with cochlear implants should measure vocal-emotion perception in an interface they can tolerate and engage with.
- **Why hard:** Pseudospeech removes linguistic emotion clues, while interface burden can affect participation and test time.
- **Naive attempt:** Use a computer-only test and treat usability as separate from measurement validity.
- **Central move:** Compare a robot and computer interface on the same emotion task, including sensitivity, duration, and participant preference.
- **Mechanism:** Adolescents aged 10–17 complete EmoHI pseudospeech emotion tests with a computer and NAO robot; d-prime, duration, and usability are measured.
- **Conceptual structure:** Sensitivity, test duration, and perceived usability/enjoyment expose the tradeoff between measurement equivalence and engagement.
- **What paper reports:** Sensitivity is similar (.36 versus .37); the robot takes longer, is less usable, but is more enjoyable and engaging.
- **Limits:** The participants, robot, pseudospeech task, and small sample bound the result; long-term adherence and general hearing-device populations remain open.

## 16. prosody-and-interactive-control

**Paper:** [From Static to Dynamic: Enhancing AAC with Generative Imagery and Zero-Shot TTS](https://www.isca-archive.org/interspeech_2025/francis25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `f19af89193786054bb15742a6e18ebe297048630b1b972d7d1465552a8183ef3`; full text captured.

- **Ordinary problem:** An augmentative communication system should let a minimally verbal child express personal concepts and a personally meaningful voice.
- **Why hard:** Fixed symbols and fixed voices limit relevance, identity, and the range of things a user can communicate.
- **Naive attempt:** Offer a static symbol board and one default synthetic voice.
- **Central move:** Generate visual symbols and use zero-shot TTS so users can personalize both the concept representation and voice.
- **Mechanism:** The proposed AAC system combines text-to-image generation with zero-shot TTS for children with autism.
- **Conceptual structure:** The operative objects are symbol coverage, voice personalization, and eventual social validity; the captured paper does not report a completed comparative trial.
- **What paper reports:** The paper presents a broader expressive design but leaves long-term communication outcomes for future study.
- **Limits:** No causal benefit or clinical efficacy should be inferred; user satisfaction, safety, cultural fit, and long-term adaptation remain open.

## 17. robustness-and-system-boundary

**Paper:** [Pushing the Limits of End-to-End Diarization](https://www.isca-archive.org/interspeech_2025/broughton25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `08a56160e0b6fee8b9f410aeb001c959922061ba7d08caee50d10adae3f33d02`; full text captured.

- **Ordinary problem:** A diarization system should assign speech to the right people in meetings with many simultaneous speakers without a separate pipeline for every case.
- **Why hard:** Overlap and speaker-count variation make it hard to learn all mixture configurations, while modular systems accumulate errors.
- **Naive attempt:** Train on a few-speaker simulation or chain independent detection and clustering modules.
- **Central move:** Use one end-to-end non-autoregressive model and scale pretraining across systematically represented eight-speaker mixtures.
- **Mechanism:** EEND-TA is evaluated on AliMeeting, AMI, DIHARD III, and MagicData RAMC with speed and diarization error comparisons.
- **Conceptual structure:** Diarization error rate measures missed, false, and wrongly attributed speech; multiple corpora test transfer across meeting conditions.
- **What paper reports:** The paper reports 14.49% DER on DIHARD III and state-of-the-art results on the listed datasets.
- **Limits:** The simulations, corpora, speaker counts, and model speed define the boundary; spontaneous conditions beyond these meetings remain open.

## 18. room-channel-and-sensing

**Paper:** [Voxplorer: Voice data exploration and projection in an interactive dashboard](https://www.isca-archive.org/interspeech_2025/deluca25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `614c7e5553af8cb57d72db5b05e3cd455e0ef495f22c6fefffc0c789ef37a913`; full text captured.

- **Ordinary problem:** Researchers need to see many dimensions of voice data together rather than inspect one acoustic measure at a time.
- **Why hard:** High-dimensional features are difficult to extract, subset, and interpret without a usable exploratory interface.
- **Naive attempt:** Export one feature table and rely on fixed plots or isolated measures.
- **Central move:** Put feature extraction, dimensionality reduction, filtering, and projection into an interactive dashboard.
- **Mechanism:** Voxplorer exposes precomputed high-dimensional voice data and can extract features from recordings directly for interactive exploration.
- **Conceptual structure:** The object is an exploratory mapping from many acoustic dimensions to a visual projection; it is a research instrument rather than a predictive model.
- **What paper reports:** The paper presents a reusable dashboard intended to broaden voice-analysis exploration; no scientific performance score is claimed.
- **Limits:** Usability, projection choices, and feature-tool assumptions determine what researchers see; the dashboard does not establish causal voice categories.

## 19. source-filter-production

**Paper:** [Evaluation of a model for sound radiation from the vocal tract wall](https://www.isca-archive.org/interspeech_2025/birkholz25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `485017b94dee041ec09f1944a4ee6834145618b4f2293e3489ced5f1e3eec9d4`; full text captured.

- **Ordinary problem:** An articulatory synthesizer should model not only sound traveling through the vocal tract but also sound radiating through its walls.
- **Why hard:** A simple physical model must reproduce speaker-specific radiation without adding an impractical number of parameters.
- **Naive attempt:** Ignore wall radiation or use one fixed radiation response for every speaker.
- **Central move:** Represent each tract section as a damped spring-mass system and fit wall parameters to real speaker voicebars.
- **Mechanism:** The simulated radiation from tube sections is compared with six speakers producing /b,d,g/ in vowel contexts, with parameters optimized to real spectra.
- **Conceptual structure:** Frequency-domain root-mean-square error between simulated and natural voicebar spectra measures how well the physical model explains the radiation.
- **What paper reports:** The paper reports 2.26–3.82 dB RMSE from 0–800 Hz and concludes the simple model can reproduce the spectra closely.
- **Limits:** The six speakers, selected consonants/vowels, frequency range, and fitted parameters bound the claim; other speech sounds and independent physical validation remain open.

## 20. source-separation-and-spatial-listening

**Paper:** [SoundSculpt: Direction and Semantics Driven Ambisonic Target Sound Extraction](https://www.isca-archive.org/interspeech_2025/chen25l_interspeech.html)
**Evidence:** D3; PDF SHA-256 `6b6c5209588a31723d6aa6dade6a80ef7bc3005c9ed78bf7daf71a665a7cdfd5`; full text captured.

- **Ordinary problem:** A listener may want one sound from a spatial mixture, and the system should use both where it is and what it is.
- **Why hard:** Nearby sources can overlap spatially, so direction alone may not distinguish the target.
- **Naive attempt:** Apply a spatial beamformer using only a target direction.
- **Central move:** Condition an ambisonic-to-ambisonic separator on direction plus semantic information about the target sound.
- **Mechanism:** SoundSculpt is trained on synthetic and real ambisonic mixtures, with direction from pointing and semantic embeddings from visual/audio description.
- **Conceptual structure:** Separation quality compares spatial-only and spatial-plus-semantic conditioning, especially for nearby secondary sources.
- **What paper reports:** The paper reports that semantic conditioning helps when sources are spatially close and outperforms signal-processing baselines.
- **Limits:** Synthetic/real mixtures, semantic encoders, and target descriptions define the boundary; spoken conversation and pointing errors remain open.

## 21. speaker-characteristics

**Paper:** [Pitch Target Realization in Putonghua Tone Production of Children from Dialect-Speaking Regions](https://www.isca-archive.org/interspeech_2025/cao25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `ce066f2b348f4053694e9cc048f7d33beaad3f39c500ecc82898d3b6b6fbd7e8`; full text captured.

- **Ordinary problem:** Children learning a second tonal variety must realize pitch targets while their physiology and first dialect continue to shape production.
- **Why hard:** Targets overlap in time and similar tones can interfere, so an error is not simply a failure to memorize a contour.
- **Naive attempt:** Treat each tone as an isolated fixed pitch template.
- **Central move:** Analyze on-target and off-target realization as interacting targets shaped by physiology and dialect experience.
- **Mechanism:** Pitch production from 139 Changli-exposed children aged 35–71 months is analyzed in the CL-CHILD corpus.
- **Conceptual structure:** The comparison separates target approximation, physiological constraints, and mutual interference among tonal categories.
- **What paper reports:** The paper reports universal physiological constraints, persistent dialect interference, and off-target forms arising from phonetic similarity and target interaction.
- **Limits:** The age range, dialect exposure, corpus, and tone inventory bound the developmental claim; longitudinal and other language environments remain open.

## 22. text-to-speech-and-content

**Paper:** [AF-Vocoder: Artifact-Free Neural Vocoder with Global Artifact Filter](https://www.isca-archive.org/interspeech_2025/chen25q_interspeech.html)
**Evidence:** D3; PDF SHA-256 `c2be743fa83e3d0071a57ccead4ad2fffb8e3782c5a09566b5d4b035eefd112f`; full text captured.

- **Ordinary problem:** A neural vocoder should produce detailed speech quickly without adding aliasing, blur, or other audible artifacts.
- **Why hard:** GAN vocoders can be sharp and fast but their frequency behavior can create artifacts that aggregate quality scores miss.
- **Naive attempt:** Use a generic GAN vocoder and rely on its learned filters to suppress artifacts.
- **Central move:** Add a learnable frequency-domain artifact filter that imposes explicit control over which spectral components pass.
- **Mechanism:** AF-Vocoder inserts GAFilter into a GAN vocoder and tests reconstruction quality and artifact suppression across datasets and speakers.
- **Conceptual structure:** The frequency filter is the intervention; reconstruction and artifact measures compare quality in-domain and for out-of-domain speakers.
- **What paper reports:** The paper reports better reconstruction quality and artifact suppression than other GAN vocoders.
- **Limits:** Datasets, speaker coverage, artifacts, and listening protocol define the claim; real-time hardware cost and unseen languages remain open.

## 23. time-frequency-measurement

**Paper:** [Introducing EMOPARKNZ: the Emotional Speech Database from New Zealand English Speakers with Parkinson’s Disease](https://www.isca-archive.org/interspeech_2025/bendom25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `d3b4fdc89eb8ad2c62d275f15163b879e1f7153745a6061ab55bd6e844357fc5`; full text captured.

- **Ordinary problem:** Researchers need emotional speech from people with Parkinson's disease to study how disease and emotion interact in voice.
- **Why hard:** Small clinical datasets make it hard to separate emotional variation from speaker, disease, and language variation.
- **Naive attempt:** Reuse a generic emotion corpus or collect labels without documenting participant and recording choices.
- **Central move:** Create a dedicated New Zealand English database with multiple emotions, speakers, and acoustic analysis, then test human recognition.
- **Mechanism:** EMOPARKNZ contains 1,950 recordings from 13 speakers across five emotions; acoustic measures and a 22-listener perception test are reported.
- **Conceptual structure:** F0, intensity, rate, and five-way listener accuracy connect measurable speech changes to perceived emotion.
- **What paper reports:** The paper reports emotion-dependent acoustic differences and 63% listener classification accuracy.
- **Limits:** Thirteen speakers, New Zealand English, Parkinson's disease, and the selected emotions bound the resource; clinical severity and broader populations remain open.

## 24. voice-identity-and-conversion

**Paper:** [ZSDEVC: Zero-Shot Diffusion-based Emotional Voice Conversion with Disentangled Mechanism](https://www.isca-archive.org/interspeech_2025/chou25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `daff5f4235242bb742e5e584d3758995f08407838c5bb99014c138b72f03d824`; full text captured.

- **Ordinary problem:** A voice-conversion system should change emotional expression for a speaker it has never seen while preserving the words and identity.
- **Why hard:** Emotion and identity are entangled, and changing one can distort the other; unseen speakers remove the shortcut of memorized target voices.
- **Naive attempt:** Train a separate converter for each target speaker or treat all speech variation as one undifferentiated style code.
- **Central move:** Use diffusion with disentangled content, speaker, and emotion mechanisms plus expressive guidance for zero-shot conversion.
- **Mechanism:** The model is trained on a large emotional-speech corpus and evaluated on unseen speakers in in-domain and out-of-domain data.
- **Conceptual structure:** Emotion accuracy, naturalness, and speech quality are separate targets; zero-shot splits test whether the conversion survives a new speaker.
- **What paper reports:** The paper reports expressive converted speech with high emotional accuracy, naturalness, and quality on its reported tests.
- **Limits:** The result is bounded to the training corpus, emotion set, diffusion design, and unseen-speaker protocol; identity verification, languages, and independent listening remain open.

