# INTERSPEECH 2025 ninth-pass full-paper notes

Eight additional official-PDF analyses deepen recognition, accent, enhancement, room diarization, clinical speech, expressive synthesis, spoof tracing, and bias accountability. Results remain author-reported and were not independently reproduced.

## 1. recognition-and-alignment/acoustic-unit-mapping

**Paper:** [HuBERT-VIC: Improving Noise-Robust Automatic Speech Recognition of Speech Foundation Model via Variance-Invariance-Covariance Regularization](https://www.isca-archive.org/interspeech_2025/ahn25_interspeech.html)  
**Evidence:** D3; PDF SHA-256 9ba4f97e7a950bbbd5ebe5d40c5fc3951f7cc17635594a9c9863ef1d9fc4f80a; 5 pages.

- **Big picture:** A recognizer trained on clean speech should still map noisy speech to words.
- **Why hard:** Noise changes acoustic statistics and can be mistaken for speech units.
- **Naive attempt:** Add noise only during fine-tuning and hope the representation stays stable.
- **Central move:** Add variance, invariance, and covariance constraints during HuBERT pretraining.
- **Mechanism:** HuBERT-VIC applies VICReg terms to noisy representations and compares masked prediction with regularizer ablations on MUSAN-noised LibriSpeech.
- **Mathematical idea:** The reported target is WER; relative gains are 23.3% on test-clean and 13.2% on test-other against the noisy-pretrained baseline.
- **Connections:** Noise robustness is changed at the representation level before recognition, not only by filtering the final waveform.
- **What paper reports:** All three regularizers give the best reported WER and show complementary ablation effects.
- **Limits:** MUSAN, SNR choices, HuBERT, and LibriSpeech bound the result; real conversational noise is not established.

## 2. languages-accents-and-resources/accent-and-cultural-boundaries

**Paper:** [Accent Normalization Using Self-Supervised Discrete Tokens with Non-Parallel Data](https://www.isca-archive.org/interspeech_2025/bai25_interspeech.html)  
**Evidence:** D3; PDF SHA-256 625cfec0c68dfd768d3dd5460fee8d3c6bb494b558a99e6a6ca61a335f658392; 5 pages.

- **Big picture:** Accent normalization should change pronunciation while keeping the same speaker recognizable.
- **Why hard:** Changing accent can also change timbre, duration, intelligibility, or words, and parallel data are scarce.
- **Naive attempt:** Convert frames one by one using paired data and accept timing and identity drift.
- **Central move:** Use self-supervised discrete tokens, nonparallel conversion, flow matching, and explicit duration preservation.
- **Mechanism:** The system extracts source tokens, predicts target-accent tokens, synthesizes waveform output, and evaluates several English accents.
- **Mathematical idea:** NAT, ACT, SIM, WER, SECS, F0 correlation, and feature distance separately measure naturalness, accent, content, identity, and prosody.
- **Connections:** The desired change is pronunciation rather than erasure of the speaker, making accent a boundary between language and identity.
- **What paper reports:** The system beats a frame-to-frame baseline on naturalness, accentedness, and timbre preservation, but post-conversion WER remains high.
- **Limits:** Accent definitions, targets, subjective judgments, and nonparallel training bound the claim; native-like is not universally better.

## 3. listening-and-separation/noise-enhancement

**Paper:** [Structured Codebook Based Hierarchical Framework for DNN for Computationally Efficient Speech Enhancement](https://www.isca-archive.org/interspeech_2025/b25_interspeech.html)  
**Evidence:** D3; PDF SHA-256 c40c1d0b52707b0e81a55bf0e0e47f35f1cc74c4890e8959f67ff33a27e0d338; 5 pages.

- **Big picture:** Speech enhancement should run on a device that cannot afford a large neural network.
- **Why hard:** Small models lose detail while large models exceed latency and memory limits.
- **Naive attempt:** Compress one large network until it runs fast, even if its structure becomes opaque.
- **Central move:** Replace one expensive DNN with simpler hierarchical predictors backed by structured speech-parameter codebooks.
- **Mechanism:** Hierarchically clustered log-power-spectrum vectors drive codebook stages and enhancement predictors evaluated on VoiceBank-DEMAND.
- **Mathematical idea:** The paper compares SSNR and computational cost; codebook classifiers use cross-entropy and the table reports parameter/runtime burden.
- **Connections:** This is compression by exploiting speech structure, linking deployment constraints to representation choice.
- **What paper reports:** The framework reduces computation while retaining comparable or improved enhancement scores over the reference systems.
- **Limits:** One corpus and parameterized spectral targets bound the evidence; downstream ASR and perceptual benefit are not fully established.

## 4. sound-and-production/room-channel-and-sensing

**Paper:** [Spatio-Spectral Diarization of Meetings by Combining TDOA-based Segmentation and Speaker Embedding-based Clustering](https://www.isca-archive.org/interspeech_2025/cordlandwehr25_interspeech.html)  
**Evidence:** D3; PDF SHA-256 fa9bfe875dd7027f5e8de013a9cafda5d3a9b3896cb16a2a81d759ef89729d08; 5 pages.

- **Big picture:** Meeting transcription needs to know who spoke when despite overlap and movement.
- **Why hard:** Position is not permanent identity when people move, while a single microphone loses direction information.
- **Naive attempt:** Use speaker embeddings alone or permanently map one direction to one speaker.
- **Central move:** Segment with time-difference-of-arrival cues, cluster speaker embeddings, and combine spatial and spectral evidence.
- **Mechanism:** TDOA detects regions, embeddings assign speakers, cACGMM optionally refines them, and compact/distributed microphone setups are tested.
- **Mathematical idea:** DER measures segmentation/assignment and cpWER measures transcript performance after diarization.
- **Connections:** Room geometry is evidence, but position is not treated as identity; this is a core room-channel boundary.
- **What paper reports:** The combined pipeline outperforms single-channel pyannote in reported compact and distributed meeting scenarios.
- **Limits:** Layouts, datasets, overlap, and spatial cues bound the result; evaluations are author-reported.

## 5. people-variation-and-health/clinical-and-assistive-speech

**Paper:** [Acoustic and Linguistic Biomarkers for Cognitive Impairment Detection from Speech](https://www.isca-archive.org/interspeech_2025/botelho25_interspeech.html)  
**Evidence:** D3; PDF SHA-256 0e19e2ff17930535386a253bfcc9cae382d027983efd3bc33f331932b39c7bf8; 5 pages.

- **Big picture:** Speech may contain signs of cognitive decline, but health signals must be separated from topic and class imbalance.
- **Why hard:** Clinical labels are scarce, the dementia class is small, and acoustic and linguistic evidence can disagree.
- **Naive attempt:** Choose one embedding or optimize overall accuracy.
- **Central move:** Combine acoustic, linguistic, knowledge-based, and neural representations, selecting complementary class-aware systems.
- **Mechanism:** PROCESS Challenge systems combine acoustic features, text features, LLM descriptors, Longformer, ECAPA-TDNN, and TRILLsson embeddings across three tasks.
- **Mathematical idea:** The study emphasizes UAF1 and class-specific F1 rather than accuracy alone.
- **Connections:** A clinical marker is meaningful only when the evaluation protects the rare class and controls confounds.
- **What paper reports:** Selected ensembles provide the strongest reported balance across train/development data and individual classes.
- **Limits:** Challenge data, demographic overlap, and missing metadata limit the claim; this is not clinical validation.

## 6. voice-generation-and-control/prosody-and-interactive-control

**Paper:** [DiEmo-TTS: Disentangled Emotion Representations via Self-Supervised Distillation for Cross-Speaker Emotion Transfer in Text-to-Speech](https://www.isca-archive.org/interspeech_2025/cho25b_interspeech.html)  
**Evidence:** D3; PDF SHA-256 9e8c77e96d0aa8a71a863a99b654f78b3375a77bc58a1c1a9180287ade069bd6; 5 pages.

- **Big picture:** Emotion transfer should change delivery without replacing the target speaker's identity.
- **Why hard:** Emotion and timbre are entangled, so an emotion embedding can leak the reference speaker.
- **Naive attempt:** Copy speaker and emotion embeddings into TTS without testing information leakage.
- **Central move:** Distill speaker-independent emotion representations with cluster sampling, perturbation, and separate style/identity conditioning.
- **Mechanism:** DiEmo-TTS clusters emotion attributes, matches speaker/emotion examples, distills representations, and uses a dual-conditioning transformer.
- **Mathematical idea:** Naturalness, speaker similarity, emotion similarity, WER/CER, and embedding scores measure different goals; ablations remove distillation components.
- **Connections:** The mechanism is disentanglement: retain vocal identity while moving the emotional control variable.
- **What paper reports:** The reported system improves emotion and speaker-related measures in the chosen experiments.
- **Limits:** Pretrained encoders, datasets, subjective measures, and cross-speaker coverage bound the conclusion.

## 7. evaluation-deployment-and-consequence/privacy-security-and-accountability

**Paper:** [Codec-Based Deepfake Source Tracing via Neural Audio Codec Taxonomy](https://www.isca-archive.org/interspeech_2025/chen25j_interspeech.html)  
**Evidence:** D3; PDF SHA-256 c3099bd9d47415030216e865f1941dbc6322f56de2ff99307f5b688937d14e26; 5 pages.

- **Big picture:** Detecting fake speech says it is synthetic; tracing its source can explain which generator family produced it.
- **Why hard:** Codec generators share stages, so a detector can learn dataset artifacts instead of source evidence.
- **Naive attempt:** Train a binary fake detector and treat attribution as the same task with more labels.
- **Central move:** Organize neural codecs into a taxonomy and use codec-related auxiliary objectives for source tracing.
- **Mechanism:** Multi-task systems on CodecFake+ use codec quantization, auxiliary codec tasks, and balanced source-tracing experiments.
- **Mathematical idea:** F1 is reported for vector-quantization, auxiliary, and decoder/source tasks; the best cited DEC F1 is 46.45%.
- **Connections:** The security move is toward contestable provenance, not merely a fake/real label.
- **What paper reports:** CodecFake+ gives initial evidence that codec taxonomy helps source tracing and that balance affects generalization.
- **Limits:** The dataset and generator coverage bound the result; 46.45% F1 is not reliable attribution.

## 8. meaning-and-interaction/grounding-and-action

**Paper:** [Who Gets the Mic? Investigating Gender Bias in the Speaker Assignment of a Speech-LLM](https://www.isca-archive.org/interspeech_2025/puhach25_interspeech.html)  
**Evidence:** D3; PDF SHA-256 f70875a4d05f6d9cf02ff2c70483f142a534d29918c14e38a843ccf2aa515122; 5 pages.

- **Big picture:** A speech model that chooses a voice can reveal social associations even when text does not request gender.
- **Why hard:** Speech generation makes an implicit association audible through selected speaker identity.
- **Naive attempt:** Evaluate TTS only for naturalness and intelligibility.
- **Central move:** Probe default speaker assignment with controlled profession and gender-colored-word prompts.
- **Mechanism:** Bark is prompted with two constructed datasets and assignments are counted for gender alignment and inclinations.
- **Mathematical idea:** The controlled assignment counts are an association probe, not population prevalence or a human perception study.
- **Connections:** A generated voice is a social action, so voice identity belongs in accountability analysis.
- **What paper reports:** Bark shows gender awareness and some inclinations but no strong systematic bias under the tested prompts.
- **Limits:** Two datasets, one model, prompt wording, and supported voices bound the conclusion; this is not a fairness guarantee.

