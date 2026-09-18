# INTERSPEECH 2025 seventh-pass full-paper notes

These eight notes use captured official PDFs and extend D3 evidence across eight first-principles areas. Results remain paper-reported, not independently reproduced.

## 1. sound-and-production/room-channel-and-sensing

**Paper:** [Influence of Room Acoustics on Objective Voice Assessment Methods in the Context of Speech and Language Therapy](https://www.isca-archive.org/interspeech_2025/franz25_interspeech.html)  
**Evidence:** D3; PDF SHA-256 a0a4cbcec9fbb43bce4199389d0524ad03a81891697a9e8ff1dad3452b4ad7f8; 5 pages.

- **Big picture:** A clinical voice measure should describe the speaker, but the microphone also hears the room and the distance from the mouth.
- **Why hard:** Reverberation and microphone placement change the measured voice differently for different underlying voice qualities, so a correction that works for one speaker or room can fail for another.
- **Naive attempt:** Treat an acoustic voice-quality score as portable across rooms, or record at a convenient distance and assume background noise is the main problem.
- **Central move:** Measure room impulse responses and compare dry and room-affected AVQI and ABI values across 35 speech-therapy rooms, two microphone positions, and 1,644 voice samples.
- **Mechanism:** The study simulates room conditions with measured impulse responses and noise, computes the difference between room and dry measures, and fits mixed-effects models with room as a fixed effect, the dry score and its interaction, and subject as a random effect.
- **Mathematical idea:** The central quantity is delta X = X_room - X_dry. The selected models obtain normalized RMSE 0.636 for AVQI and 0.669 for ABI, with R2 0.596 and 0.553; the model is descriptive of the tested rooms, not a universal correction.
- **Connections:** This is a direct example of separating the talker from the recording path. It connects physical acoustics to clinical measurement and shows why a benchmark score can partly measure the room.
- **What paper reports:** Across the rooms, voice-quality measures generally deteriorate by 0–2 units; the smartphone is more affected than the lavalier microphone, and room effects are significant for almost all rooms. Only 8 of 35 rooms meet the stricter A4 reverberation recommendation.
- **Limits:** The rooms, simulated signals, microphones, and Saarbrücken database define the tested boundary; the study does not establish a correction for other clinics or devices. Reported model fits and significance tests are author-reported and were not independently reproduced.

## 2. listening-and-separation/noise-enhancement

**Paper:** [FUSE: Universal Speech Enhancement using Multi‐Stage Fusion of Sparse Compression and Token Generation Models for the URGENT 2025 Challenge](https://www.isca-archive.org/interspeech_2025/goswami25_interspeech.html)  
**Evidence:** D3; PDF SHA-256 4aaa175e2914f3dff046156d64a6d4b3729dd2f2ebd7a4731f4c9c0684e33c20; 5 pages.

- **Big picture:** Enhancement must make damaged speech understandable while avoiding invented detail and preserving the speaker's identity.
- **Why hard:** Noise, clipping, bandwidth loss, packet loss, and wind damage remove different evidence. A model optimized for sample-level fidelity can leave speech perceptually poor, while a generative model can sound plausible but change the signal.
- **Naive attempt:** Use one signal-reconstruction network and one loss for every distortion, or judge success with only SDR or another single waveform score.
- **Central move:** Use three stages: a discriminative sparse-compression enhancer, a codec-token generator that reconstructs missing detail, and a fusion network that combines their different strengths; shift averaging and network blending stabilize the outputs.
- **Mechanism:** Stage 1 predicts an enhanced waveform with mel and SI-SDR losses. Stage 2 conditions masked codec-token prediction on noisy and Stage-1 features and decodes the predicted tokens. Stage 3 receives the noisy signal and both estimates, then adds speaker, phoneme, and perceptual losses. The data contain 2.5K hours of speech, 550 hours of noise, 60K room responses, seven distortion types, and blind samples with an unseen language.
- **Mathematical idea:** The system combines mel-spectrogram, SI-SDR, speaker cosine, phoneme-feature, and UTMOS losses. In the non-blind test, Stage 1 reaches SDR 12.62 and Stage 2 raises UTMOS to 2.38 but lowers SDR to 9.03; the fusion stage reaches UTMOS 2.64 and SDR 12.53 before shift averaging.
- **Connections:** The paper makes the fidelity-versus-plausibility tradeoff concrete. The generative stage is not simply a better denoiser: it fills missing evidence, so perceptual improvement can coexist with lower waveform agreement.
- **What paper reports:** On the blind challenge set, the system reports DNSMOS 2.94, NISQA 3.25, UTMOS 2.19, MOS 3.44, and CER 77.09; it ranks behind the top system on several signal-level measures but leads the listed systems on perceptual measures.
- **Limits:** The challenge mixtures, five training languages, unseen Japanese test condition, and 900-sample blind set define the evidence. The sequential three-stage inference and shift operations restrict real-time use; all results are author-reported and no independent reproduction was performed.

## 3. recognition-and-alignment/adaptation-and-open-vocabulary

**Paper:** [Robust fine-tuning of speech recognition models via model merging: application to disordered speech](https://www.isca-archive.org/interspeech_2025/ducorroy25_interspeech.html)  
**Evidence:** D3; PDF SHA-256 b63d8c0107dce983002da74b4858187b571e5050ed88c87f14bd85bdc73b5ae6; 5 pages.

- **Big picture:** A recognizer trained mostly on clear speech must map speech affected by motor disorders to words without confusing atypical pronunciation with noise.
- **Why hard:** Dysarthric speech varies across speakers and within one speaker, and the available training set is small; ordinary fine-tuning can overfit one trajectory and long utterances are especially difficult.
- **Naive attempt:** Fine-tune one model once and choose its last checkpoint, assuming the single optimization path has found the best adaptation.
- **Central move:** Average weights from multiple checkpoints or fine-tuning trajectories, and add a selective rule that keeps a candidate only when it reduces development-set WER.
- **Mechanism:** The study fine-tunes Whisper on the SAP dysarthric-speech data. MAST averages checkpoints along one trajectory, MAcT averages models from different hyperparameter trajectories, and SMAcT scans candidate models and retains those that improve the merged ensemble. The procedure is also tested with 1-hour, 10-hour, and full training subsets.
- **Mathematical idea:** For corresponding parameters, merging uses an arithmetic mean. SMAcT accepts model Mi when WER(E union Mi) is lower than the current WER. On the full set, fine-tuning gives WER 15.0, MAST 13.4, MAcT 13.9, and SMAcT 13.6; in the 1-hour setting SMAcT reduces WER from 21.2 to 19.0.
- **Connections:** The conceptual move is stability across solutions, not a new acoustic feature. It treats model variation as useful evidence about what transfers to impaired speech, while keeping the inference model the same size.
- **What paper reports:** The paper reports gains for long utterances and low-data settings, including a 7.6% relative reduction from 18.5 to 17.1 WER with 10 hours of data; smaller Base and Turbo models improve too, but less consistently than Large.
- **Limits:** The SAP data, Whisper family, selected development subset, and merging order determine the result. The selective procedure uses WER on a development subset and may itself be selection-sensitive; no independent reproduction was performed.

## 4. meaning-and-interaction/prosody-and-intent

**Paper:** [Developing a Top-tier Framework in Naturalistic Conditions Challenge for Categorized Emotion Prediction: From Speech Foundation Models and Learning Objective to Data Augmentation and Engineering Choices](https://www.isca-archive.org/interspeech_2025/feng25_interspeech.html)  
**Evidence:** D3; PDF SHA-256 dc1ba163f0a003b86e5f01f91988b82705bc788cc74327b0c403c592f80cb4fb; 5 pages.

- **Big picture:** Emotion in natural speech is uncertain and often mixed, so a system should represent what listeners actually agree on rather than force one absolute label.
- **Why hard:** The challenge data are imbalanced, roughly 19% of training samples lack annotator agreement, and a majority label throws away legitimate ambiguity and minority emotion evidence.
- **Naive attempt:** Train hard one-hot emotion classes and optimize overall accuracy, allowing the majority emotions to dominate the learning signal.
- **Central move:** Predict an emotion distribution with KL-divergence, train speech and transcript representations together, and use annotation dropout, majority/minority audio mixing, reweighting, and minority average precision to expose the imbalance.
- **Mechanism:** SAILER compares WavLM Large and Whisper Large-V3 speech encoders, combines speech and text embeddings, and predicts primary plus secondary emotion and attribute labels. Annotation dropout removes 20% of majority-class annotations during training; audio mixing combines majority and minority samples with silence or overlap.
- **Mathematical idea:** The target is a soft distribution d rather than a one-hot vector, and KL divergence trains the predicted distribution. The best single system reports macro-F1 0.411 and accuracy 54.53; a three-system ensemble reaches macro-F1 0.431 and accuracy 57.00, while minority mean average precision is tracked separately.
- **Connections:** This paper connects meaning to measurement: the label is not the emotion itself, but an imperfect distribution of human judgments. It shows why a higher overall score can coexist with worse minority performance.
- **What paper reports:** Whisper representations outperform WavLM in the reported comparisons; audio mixing and annotation dropout improve minority-class average precision more reliably than overall accuracy, and adding secondary emotions improves the main score but can hurt minority classes.
- **Limits:** The evidence comes from the MSP-Podcast IS25-SER challenge and validation-heavy experiments; the hidden test labels limit systematic ablation. Emotion categories and annotator distributions remain task-specific, and no independent reproduction was performed.

## 5. voice-generation-and-control/voice-identity-and-conversion

**Paper:** [Voices of `cyborg awesomeness': Posthuman embodiment of nonbinary gender expression in AI speech technologies](https://www.isca-archive.org/interspeech_2025/hope25_interspeech.html)  
**Evidence:** D3; PDF SHA-256 9f973b1c5beb4ab0469298f17c0bb05455d8a3f9106764b2cb9116ef1d200a83; 5 pages.

- **Big picture:** For a person who communicates through a speech-generating device, voice is part of self-expression; a useful synthetic voice must be controllable in ways that match the person's identity rather than a default category.
- **Why hard:** A small set of voice controls can encode gendered assumptions, while blending identities or changing vocal-tract and voice-quality features can produce affirming, uncomfortable, or unexpected bodily responses.
- **Naive attempt:** Offer one fixed synthetic voice or map identity to a binary pitch choice, assuming lower or higher pitch alone determines whether the voice fits the user.
- **Central move:** Let users explore breathiness, vocal tension, acoustic vocal-tract length, weighted blends between speaker identities, and a continuous transition between identities, then ask users how the voices feel and whether they affirm their gender.
- **Mechanism:** The study presents generated samples from controllable TTS and modified XTTSv2/MAGES systems to 12 nonbinary adults who use speech-generating devices. It measures F0, HNR, and acoustic vocal-tract length with Praat and combines close-ended responses with open-ended reflections.
- **Mathematical idea:** Acoustic vocal-tract length is estimated from the third formant using aVTL = 34000/(2 times mean F3/2.5). The samples deliberately move controls by large standardized amounts; the survey counts preferences and gender affirmation rather than fitting a predictive model.
- **Connections:** This expands voice identity beyond speaker recognition. The relevant target is user control and embodiment, so a voice that sounds less conventionally human can be more appropriate for a particular person.
- **What paper reports:** Nine of 12 participants wanted breathiness control, 11 wanted vocal-tension control, all 12 wanted extreme vocal-tract-length control, and all 12 wanted the ability to blend two voices; nine found the MoreSecond blend gender-affirming.
- **Limits:** There are 12 participants, deliberately extreme synthetic settings, and a qualitative/close-ended survey rather than a deployment study. Preferences are not a universal mapping from acoustic features to gender; results and interpretations are author-reported and were not independently reproduced.

## 6. people-variation-and-health/clinical-and-assistive-speech

**Paper:** [ADCeleb: A Longitudinal Speech Dataset from Public Figures for Early Detection of Alzheimer’s Disease](https://www.isca-archive.org/interspeech_2025/gao25b_interspeech.html)  
**Evidence:** D3; PDF SHA-256 077dbdaa2f209046b6158192cf60ace99b8b32eed3f6f7ebaef89e0433ad3e6b; 5 pages.

- **Big picture:** Early cognitive decline may alter language and speech before diagnosis, but a model needs longitudinal, naturalistic recordings rather than a single clean clinical utterance.
- **Why hard:** Public recordings contain changing topics, speakers, video quality, age, and demographic imbalance; a high-dimensional representation can classify a person while hiding which speech change carries the signal.
- **Naive attempt:** Train on random speech segments and report one accuracy number without keeping speakers separated between training and testing or distinguishing acoustic from linguistic evidence.
- **Central move:** Build a longitudinal celebrity speech corpus, balance AD and control groups across relevant demographics, extract frozen acoustic and linguistic representations, and evaluate them with speaker-disjoint nested cross-validation and fusion.
- **Mechanism:** ADCeleb contains public spontaneous recordings from 40 people with AD and 40 controls, with intervals two and one years before diagnosis. Acoustic embeddings include x-vectors, TRILLsson, Wav2Vec2, HuBERT, and Whisper; linguistic embeddings include multilingual encoders. PCA and PLDA classify speakers, and selected acoustic/linguistic predictions are averaged.
- **Mathematical idea:** The evaluation is speaker-level nested 10-fold cross-validation with accuracy, F1, sensitivity, specificity, and AUC. Wav2Vec2 acoustic accuracy is 0.67 and 0.72 at the two intervals; the best linguistic models reach 0.73 and 0.75; fusion reaches 0.80 at the nearer interval.
- **Connections:** The paper makes health inference a problem of separating a changing clinical signal from person, topic, and recording context. It also shows why a larger accuracy number does not by itself identify a clinical marker.
- **What paper reports:** The authors report that linguistic representations are stronger earlier, while acoustic information contributes more near the year of diagnosis; fusion improves the nearer interval to 0.80 accuracy.
- **Limits:** The corpus uses public figures, YouTube recordings, 40 AD and 40 control speakers, and imperfect observational labels. It is a dataset and baseline study, not a clinical diagnostic validation; author-reported results were not independently reproduced.

## 7. languages-accents-and-resources/low-resource-and-data-creation

**Paper:** [Evaluating Wav2Vec2-Bert for Computer-Assisted Pronunciation Training for isiZulu](https://www.isca-archive.org/interspeech_2025/fort25_interspeech.html)  
**Evidence:** D3; PDF SHA-256 ada6f98045ba930be437c40618e001ba13a4532c399ef1acee8404c722f33a57; 5 pages.

- **Big picture:** Pronunciation feedback for isiZulu learners needs a recognizer that understands the language and can identify the learner's phoneme errors despite limited labeled data.
- **Why hard:** Native and learner recordings differ in speaking style and domain; isiZulu's agglutinative words make character and word errors behave differently, and the gold labels mark an error without always identifying the produced phone.
- **Naive attempt:** Fine-tune on one corpus and treat its output as a complete diagnostic pronunciation label, or transfer a model trained on careful teacher speech directly to natural learner speech.
- **Central move:** Compare Wav2Vec2-BERT models fine-tuned on native isiZulu, learner speech, and both, then evaluate transcription and phoneme-error detection separately.
- **Mechanism:** The study uses NCHLT native speech, L2 isiZulu learner speech, and teacher recordings. Models are fine-tuned with the same setup; phoneme alignment uses Needleman–Wunsch, and error labels are evaluated with false acceptance, false rejection, and true-negative rates.
- **Mathematical idea:** On the NCHLT test set, the NCHLT-trained model reports WER 0.126 and CER 0.0237, versus WER 0.667 for the L2-only model and 0.141 for the combined model. For phoneme errors, the L2 model has FAR 2.2%, FRR 16.1%, and TNR 65.1%; the model cannot compute a full diagnostic error rate because the gold labels omit the learner's produced phone.
- **Connections:** This is a resource problem and a target-definition problem at once: better recognition is not the same as better feedback. It exposes how language-specific data and annotation choices determine what a system can claim.
- **What paper reports:** Native-speech transcription is strongest for the NCHLT-trained model, while the L2-trained model detects the most incorrect phonemes under the available true-negative measure; the authors release code and identify the data sources.
- **Limits:** The results depend on three isiZulu corpora, their recording styles, and incomplete phoneme-error labels. Tone is not evaluated because it is not marked orthographically; findings do not automatically transfer to other languages or pronunciation tasks.

## 8. evaluation-deployment-and-consequence/metrics-and-targets

**Paper:** [Enhancing Retrieval-Augmented Audio Captioning with Generation-Assisted Multimodal Querying and Progressive Learning](https://www.isca-archive.org/interspeech_2025/choi25f_interspeech.html)  
**Evidence:** D3; PDF SHA-256 5768e141e17165509b5feae75a1c6676bb0aeec7547fbbeda4b7f9eebcdb935f; 5 pages.

- **Big picture:** An audio retrieval system should return evidence that matches what the sound means, not merely a caption that resembles the query in one representation.
- **Why hard:** Audio and text similarities can disagree: a caption may share words with the query while the retrieved audio is wrong, or vice versa. A generated textual description can also introduce errors before retrieval.
- **Naive attempt:** Retrieve only by audio embedding similarity or generate a caption and use it as the sole query, without checking whether audio and text evidence point to the same item.
- **Central move:** Generate a caption for the query audio, retrieve with a weighted combination of audio-to-audio and text-to-text similarity, and progressively train the model with interleaved audio-text examples.
- **Mechanism:** MQ-Cap trains a connector and LoRA parameters with a cross-entropy loss over interleaved pairs. It first retrieves 25 candidates by audio similarity, then combines normalized Laion-CLAP audio and text similarities with alpha 0.5. WavCaps, AudioCaps, and Clotho provide training and knowledge-base data.
- **Mathematical idea:** The pair score is S = alpha S_A + (1-alpha) S_T. On AudioCaps, MQ-Cap reports SPIDEr 0.519; on Clotho, 0.319; generation-assisted querying raises cross-modal retrieval R@1 from 44.0 to 45.3 for Laion-CLAP and from 56.0 to 59.1 for OmniBind on AudioCaps. The generated text is an intermediate measurement, not ground truth.
- **Connections:** This paper turns evaluation into a question about what counts as matching: waveform similarity, words, or the event described. It connects retrieval, captioning, and selective use because a fluent caption can still retrieve the wrong evidence.
- **What paper reports:** Progressive learning plus generation-assisted querying improves the reported captioning scores and gives up to 3.1 percentage points of retrieval improvement; the method adds about 1.07 seconds of generation overhead to retrieval.
- **Limits:** The benchmarks are AudioCaps, Clotho, and Auto-ACD with overlapping-source controls and missing test audio; retrieval quality depends on the generated caption and CLAP encoders. Results are author-reported and were not independently reproduced.

