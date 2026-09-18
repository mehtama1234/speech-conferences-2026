# INTERSPEECH 2025 eighteenth-pass full-paper notes

Twenty-four additional official-PDF readings deepen the atlas across all 24 conceptual subthemes. Results are author-reported and not independently reproduced.

## 1. source-filter-production

**Paper:** [Hybrid Expert Knowledge and Self-Supervised Learning for Diagnostic Modeling of Adductor Spasmodic and Primary Myotonic Dysphonia](https://www.isca-archive.org/interspeech_2025/du25c_interspeech.html)
**Evidence:** D3; PDF SHA-256 `aee0fb89da91dc7017710a711677aac32c95edaf75ef8566d6e708e0c924f58a`; full text captured.

- **Ordinary problem:** Clinicians must distinguish two voice disorders from patients' speech, but expert listening is scarce and subjective.
- **Why hard:** The disorders can sound similar and their acoustic signs vary across patients.
- **Naive attempt:** Rely only on a clinician's global impression or on generic acoustic features.
- **Central move:** Combine expert-designed voice measures with representations learned directly from the waveform.
- **Mechanism:** A CNN receives handcrafted features and self-supervised waveform representations and predicts ADSD versus pMTD on a newly collected patient dataset.
- **Conceptual structure:** The decision is a two-class prediction; accuracy measures the fraction of correctly classified patients.
- **What paper reports:** The paper reports 83.3% classification accuracy.
- **Limits:** The result is tied to the constructed dataset, its patient mix, and the two diagnoses; clinical deployment, calibration, and external validation remain open.

## 2. time-frequency-measurement

**Paper:** [On Enhancing the Performance of Children's ASR Task in Limited Data Scenario](https://www.isca-archive.org/interspeech_2025/ankita25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `3a75dd67cd146b052fe9f209c110bc9455c392c2da3695072dda9ee3324390e6`; full text captured.

- **Ordinary problem:** A child ASR system must recognize speech when only a small amount of child data is available.
- **Why hard:** Children's voices differ from adults and scarce data makes both acoustic modeling and pronunciation variation difficult.
- **Naive attempt:** Train a standard spectrum-only ASR model and accept its data-scarcity error.
- **Central move:** Augment in-domain data, add glottal-activity information to spectral features, and normalize features with fMLLR.
- **Mechanism:** The study compares a baseline with augmented data, MFCCs plus glottal parameters, and fMLLR-normalized features.
- **Conceptual structure:** Character error rate is the main error measure; relative reduction compares each system with the baseline.
- **What paper reports:** The combined normalized MFCC and glottal features give a reported 40% relative character-error-rate reduction over baseline.
- **Limits:** The evidence is limited to the child's speech data and tested feature pipeline; languages, age ranges, and transfer to new schools or microphones are not established.

## 3. room-channel-and-sensing

**Paper:** [SepVAC: Multitask Learning of Speaker Separation, Speaker Localization, Microphone Array Localization, and Room Acoustic Parameter Estimation in Various Acoustic Conditions](https://www.isca-archive.org/interspeech_2025/hartanto25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `0b2a4b2b5711c8d8d94649653827aa03961210558b5fe49c097429cea7260216`; full text captured.

- **Ordinary problem:** A separator must recover each speaker while also coping with where speakers and microphones sit in a reverberant room.
- **Why hard:** Noise and reverberation can make room effects look like properties of the speech itself.
- **Naive attempt:** Ask one network to separate speech while treating the room and microphone arrangement as irrelevant nuisance.
- **Central move:** Predict speech separation and the physical recording conditions together, then use curriculum learning to stabilize training.
- **Mechanism:** SepVAC jointly estimates separated speech, speaker locations, microphone-array location, and room acoustic parameters on SMS-WSJ-Plus.
- **Conceptual structure:** Word error rate evaluates the usefulness of the separated signal to recognition; the multitask losses constrain both speech and scene estimates.
- **What paper reports:** The paper reports a 0.67-point WER improvement over SpatialNet.
- **Limits:** The result is author-reported on SMS-WSJ-Plus and its simulated acoustic conditions; real rooms, imperfect localization, and independent reproduction remain open.

## 4. source-separation-and-spatial-listening

**Paper:** [NeuroSpex+: Dual-Task Training of Neuro-Guided Speaker Extraction with Speech Envelope and Waveform](https://www.isca-archive.org/interspeech_2025/dasilva25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `5a6d839485f9407147d4fc2316bd2126c4e10a4e6fce1fad03c382e42df23ada`; full text captured.

- **Ordinary problem:** In a group conversation, a listener's brain activity can indicate which talker they are attending to; the system should recover that talker's speech.
- **Why hard:** The neural cue is noisy and the extracted waveform can sound plausible while still losing the speech envelope that carries intelligibility.
- **Naive attempt:** Optimize only waveform reconstruction and hope the attended speaker remains identifiable.
- **Central move:** Train the extractor on two linked targets: the target waveform and its amplitude envelope.
- **Mechanism:** NeuroSpex+ uses EEG-derived reference cues and jointly predicts the target waveform and speech envelope to shape its mask.
- **Conceptual structure:** The two reconstruction objectives constrain both detailed waveform quality and slower envelope structure; signal-quality measures compare with baselines.
- **What paper reports:** The paper reports significant improvement over baseline speaker-extraction systems.
- **Limits:** The evidence is bounded to the recorded EEG/speech setup and tested mixtures; listener attention changes, clinical use, and independent reproduction remain open.

## 5. echo-and-reconstruction

**Paper:** [A Deformable Convolution GAN Approach for Speech Dereverberation in Cochlear Implant Users](https://www.isca-archive.org/interspeech_2025/chiang25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `117a8270ea47e2052ea787a81d2b066eb3d38749963c09894a2fc58579ac21c5`; full text captured.

- **Ordinary problem:** Reverberation smears speech, and cochlear-implant users are especially affected; a useful enhancer must restore intelligibility, not just make the waveform look cleaner.
- **Why hard:** Transient speech cues can be blurred by room reflections and by the implant's representation of sound.
- **Naive attempt:** Use a fixed convolutional receptive field or optimize only for normal-hearing listeners.
- **Central move:** Let deformable convolution move its receptive field to the distortion, and evaluate both signal measures and listeners with cochlear implants.
- **Mechanism:** A deformable-convolution GAN is trained for dereverberation, first tested on REVERB and then assessed in listening tests with normal-hearing and CI users.
- **Conceptual structure:** The learned offsets change which neighboring time-frequency evidence is combined; intelligibility and quality are judged by objective tests and listener responses.
- **What paper reports:** The paper reports markedly improved CI speech intelligibility by preserving envelope and transient structure.
- **Limits:** The claim is bounded to REVERB conditions, the tested listeners, and the GAN configuration; broader hearing profiles, rooms, and independent replication remain open.

## 6. acoustic-unit-mapping

**Paper:** [Mixture of LoRA Experts for Low-Resourced Multi-Accent Automatic Speech Recognition](https://www.isca-archive.org/interspeech_2025/bagat25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `24d67d7a94e85d772f56d24def610a3175a38f8f97b105ca6235630b5705ba2c`; full text captured.

- **Ordinary problem:** An ASR model should recognize non-native speech across several accents even when each accent has little labeled data and the accent is unknown at test time.
- **Why hard:** Accent changes sound patterns in different ways, and adapting to one accent can erase performance on others.
- **Naive attempt:** Fine-tune one shared model or train a separate full model for every accent.
- **Central move:** Keep several small accent-specific adapters and let the system combine them, with or without knowing the accent.
- **Mechanism:** MAS-LoRA attaches low-rank adapters specialized to accents to Whisper and evaluates known- and unknown-accent routing on L2-ARCTIC.
- **Conceptual structure:** Word error rate measures recognition; comparisons include ordinary LoRA, full fine-tuning, and forgetting after adaptation.
- **What paper reports:** The paper reports lower WER than those baselines, stronger gains when the accent is known, and less catastrophic forgetting.
- **Limits:** The result is tied to L2-ARCTIC, its accent set, Whisper, and routing assumptions; spontaneous speech and accents outside the corpus remain open.

## 7. adaptation-and-open-vocabulary

**Paper:** [Learning More with Less: Self-Supervised Approaches forLow-Resource Speech Emotion Recognition](https://www.isca-archive.org/interspeech_2025/gong25b_interspeech.html)
**Evidence:** D3; PDF SHA-256 `bb874107ce314f883fc9369123c6c97780f3616ad1b9cd81380279d3b024e3b1`; full text captured.

- **Ordinary problem:** Emotion recognition should work for languages with few labeled examples, not only for languages with large emotion datasets.
- **Why hard:** Emotion labels are scarce and expressive cues do not transfer unchanged across languages.
- **Naive attempt:** Train a supervised classifier only on the small labeled target-language set.
- **Central move:** Learn a speech representation without labels using contrastive learning or BYOL, then transfer it across languages.
- **Mechanism:** The study compares self-supervised objectives and analyzes their cross-lingual behavior for Urdu, German, and Bangla emotion recognition.
- **Conceptual structure:** F1 measures class decisions; the comparison asks how much it improves over supervised or conventional representation learning under limited labels.
- **What paper reports:** The paper reports F1 improvements of 10.6% in Urdu, 15.2% in German, and 13.9% in Bangla.
- **Limits:** The reported gains depend on the selected languages, labels, augmentations, and emotion definitions; cultural validity and transfer to new languages remain open.

## 8. multilingual-and-crosslingual

**Paper:** [NIRANTAR: Continual Learning with New Languages and Domains on Real-world Speech Data](https://www.isca-archive.org/interspeech_2025/javed25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `0a331acd2bb38f841b409b8da2b9d6f606b26fa9e53906d37779ca46468dfee2`; full text captured.

- **Ordinary problem:** A deployed ASR system must keep learning as new languages and domains arrive in an uneven real-world stream.
- **Why hard:** A model can learn the new episode while forgetting older languages, and simulated episodes hide irregular shifts.
- **Naive attempt:** Shuffle all data together or evaluate continual learning on artificially regular episodes.
- **Central move:** Measure language-incremental, domain-incremental, and joint language-plus-domain learning on naturally arriving speech.
- **Mechanism:** NIRANTAR contains 3,250 hours from 22 languages and 208 Indian districts, with non-uniform episodes and human transcripts; existing continual-learning methods are compared.
- **Conceptual structure:** The central objects are recognition error over time and retention after each episode; the framework separates language and domain changes instead of averaging them away.
- **What paper reports:** The paper finds that no single evaluated method performs consistently across the three scenarios.
- **Limits:** This is a benchmark and comparative study, not proof that one method is universally best; the geography, languages, episode order, and ASR models define the boundary.

## 9. low-resource-and-data-creation

**Paper:** [The NaijaVoices Dataset: Cultivating Large-Scale, High-Quality, Culturally-Rich Speech Data for African Languages](https://www.isca-archive.org/interspeech_2025/emezue25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `0cb38fd800ae74f26db6d052b19963ad15ed7bcf95f987a51c51547297fb3755`; full text captured.

- **Ordinary problem:** People who speak Igbo, Hausa, or Yoruba need speech technology trained on enough varied speech to work beyond a few speakers.
- **Why hard:** African languages are underrepresented, and small or homogeneous datasets cannot expose speaker, accent, and recording variation.
- **Naive attempt:** Reuse large-resource-language data or build a small dataset without measuring its diversity.
- **Central move:** Collect a large, culturally grounded speech-text corpus and test whether it improves several ASR families.
- **Mechanism:** NaijaVoices contains 1,800 hours from more than 5,000 speakers; the paper analyzes acoustic diversity and fine-tunes Whisper, MMS, and XLSR.
- **Conceptual structure:** Word error rate compares models before and after the new data; corpus scale and speaker diversity are part of the intervention.
- **What paper reports:** The paper reports average WER improvements of 75.86% for Whisper, 52.06% for MMS, and 42.33% for XLSR.
- **Limits:** The corpus languages, collection process, transcription policy, and model choices bound the result; coverage of other African languages and deployment conditions remains open.

## 10. boundaries-and-sequence-structure

**Paper:** [StutterCut: Uncertainty-Guided Normalised Cut for Dysfluency Segmentation](https://www.isca-archive.org/interspeech_2025/ghosh25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `6cccda140047cade5dceec0636c8e468b51590d78f5b4489ab76eeac13ff71c8`; full text captured.

- **Ordinary problem:** Therapy and feedback need to know where a dysfluency begins and ends, not only whether an entire utterance contains one.
- **Why hard:** Only weak utterance labels are common, while real dysfluency boundaries are uncertain and synthetic timing is unrealistic.
- **Naive attempt:** Classify each utterance or trust every weak label as if it gave exact frame boundaries.
- **Central move:** Turn overlapping speech windows into a graph, use a weakly trained classifier to refine links, and reduce its influence when it is uncertain.
- **Mechanism:** StutterCut uses uncertainty-guided normalized cuts and adds frame-level boundaries for four dysfluency types to FluencyBank.
- **Conceptual structure:** Graph partitioning separates regions; Monte Carlo dropout estimates uncertainty, and F1 plus onset error measure segmentation quality.
- **What paper reports:** The paper reports higher F1 and more precise stuttering-onset detection on real and synthetic data.
- **Limits:** The evidence is bounded to FluencyBank, four dysfluency types, annotation quality, and the tested uncertainty model; therapy outcomes and new speakers remain open.

## 11. dialogue-and-turn-taking

**Paper:** [Backchannel prediction for natural spoken dialog systems  using general speaker and listener information](https://www.isca-archive.org/interspeech_2025/fukunaga25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `f73517c360845a0f65336d5c2ae09689dd89c7e71924391f77105ae0f16b0e3d`; full text captured.

- **Ordinary problem:** A listener's short responses—such as agreement, continuation, or surprise—help a spoken dialogue feel responsive; a system should choose the right surface form without storing private speaker IDs.
- **Why hard:** Three broad classes are too coarse for generation, while identity embeddings are difficult to deploy and raise privacy concerns.
- **Naive attempt:** Predict a coarse backchannel class from a detailed speaker/listener identity embedding.
- **Central move:** Replace identity-specific inputs with general speaker and listener embeddings and predict eleven surface-form categories as well as three classes.
- **Mechanism:** The model uses speech, text, and general embeddings and compares three- and eleven-category prediction against ID-based systems.
- **Conceptual structure:** Accuracy is reported separately for coarse and fine categories, exposing the cost of richer response choices.
- **What paper reports:** The paper reports 1.3% accuracy improvement for three classes and 0.9% for eleven classes over conventional ID embeddings.
- **Limits:** The result is author-reported for the tested dialogue corpus and categories; natural turn timing, privacy leakage in embeddings, and user experience remain open.

## 12. grounding-and-action

**Paper:** [Vela: Scalable Embeddings with Voice Large Language Models for Multimodal Retrieval](https://www.isca-archive.org/interspeech_2025/hu25b_interspeech.html)
**Evidence:** D3; PDF SHA-256 `f4898c608bf99e2fef3492b20bbd9d63da3d711b4d7d0385799a79b9bc804c3a`; full text captured.

- **Ordinary problem:** A retrieval system should find the right audio for a long, complicated text request, not only match short captions to short clips.
- **Why hard:** Audio and text embeddings are trained in different modalities, and simple CLAP-style matching weakens on long or compositional queries.
- **Naive attempt:** Use a fixed audio-text contrastive model and rely on its pooled embedding for every query.
- **Central move:** Adapt a multimodal language model to produce a universal embedding, using prompts and text-pair training without requiring paired audio in the final training stage.
- **Mechanism:** Vela uses selected prompts and in-context examples, then trains on text pairs; retrieval is tested on ordinary and newly designed long/complex benchmarks.
- **Conceptual structure:** Text-audio retrieval metrics compare the rank of the correct audio; the new tests ask whether the embedding preserves multiple pieces of a query.
- **What paper reports:** The paper reports that Vela outperforms traditional CLAP models and is more robust on long, complex retrieval tasks.
- **Limits:** The abstract says code is forthcoming and the result is tied to the chosen benchmarks and prompts; open-world audio, speech-specific retrieval, and independent reproduction remain open.

## 13. prosody-and-intent

**Paper:** [EmotionRankCLAP: Bridging Natural Language Speaking Styles and Ordinal Speech Emotion via Rank-N-Contrast](https://www.isca-archive.org/interspeech_2025/chandra25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `5a34fd5ea1236f670750d09bca0d36398e06570a95f42bd426f55f07066cc0c3`; full text captured.

- **Ordinary problem:** Emotion is ordered: a voice can be more or less excited or positive, but ordinary audio-text contrastive training treats labels as unrelated names.
- **Why hard:** Ignoring order loses gradual differences and leaves audio and language representations poorly aligned.
- **Naive attempt:** Pull each audio sample toward its text label while treating every other label as equally wrong.
- **Central move:** Use valence-arousal rankings in a Rank-N-Contrast objective so nearby and distant emotional examples exert different forces.
- **Mechanism:** EmotionRankCLAP aligns emotional speech with natural-language speaking-style prompts and contrasts examples according to their position in valence-arousal space.
- **Conceptual structure:** The loss encodes an ordering rather than only class identity; cross-modal retrieval tests whether the learned space preserves emotion relations.
- **What paper reports:** The paper reports better emotion ordinality than existing emotion-CLAP systems on cross-modal retrieval.
- **Limits:** The result depends on rating dimensions, prompt wording, and the tested emotion corpus; listener disagreement and transfer across cultures remain open.

## 14. prosody-and-interactive-control

**Paper:** [LombardTokenizer: Disentanglement and Control of Vocal Effort in a Neural Speech Codec](https://www.isca-archive.org/interspeech_2025/jacquelin25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `61fc6c3b9e690b6d0012a21d81f74bd928e50d8bdb9518ca95a41257ba06343e`; full text captured.

- **Ordinary problem:** A speech codec should preserve what was said while allowing a system to change how forcefully it was spoken, such as neutral versus Lombard speech in noise.
- **Why hard:** Content, speaker identity, and vocal effort are mixed in ordinary representations, so changing effort can damage words or voice quality.
- **Naive attempt:** Use one undifferentiated code and hope a conversion model learns effort implicitly.
- **Central move:** Place vocal effort in a designated codec layer while keeping semantic content in another layer, making effort controllable.
- **Mechanism:** LombardTokenizer conditions the second quantization layer of SpeechTokenizer on vocal-effort encoders and tests neutral/Lombard conversion and synthesis quality.
- **Conceptual structure:** Layer-wise discrete codes represent different information; conversion metrics and quality tests compare effort control, intelligibility, and naturalness.
- **What paper reports:** The paper reports better neutral-to-Lombard and Lombard-to-neutral conversion than existing methods while retaining synthesis quality.
- **Limits:** The result is tied to the AVID/Lombard data, selected effort conditions, and codec; other speaking styles, languages, and independent listening tests remain open.

## 15. voice-identity-and-conversion

**Paper:** [Private kNN-VC: Interpretable Anonymization of Converted Speech](https://www.isca-archive.org/interspeech_2025/franzreb25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `a709e7b81114d1221cb0a2cc2f5c8eaf6460f7ac8d5a48cb7594d21202dd6eb4`; full text captured.

- **Ordinary problem:** An anonymizer must hide who is speaking while keeping the words and useful speech intact; a strong attacker may exploit prosody rather than obvious voice quality.
- **Why hard:** Speaker identity leaks through phone duration and pitch variation even after voice conversion, and a single recognition score does not reveal the leak.
- **Naive attempt:** Convert the voice and assume identity is removed once the main spectral cues change.
- **Central move:** Add interpretable controls that alter phone duration and pitch variation, then test which changes defeat the speaker-recognition attack.
- **Mechanism:** Private kNN-VC extends kNN voice conversion with duration and variation anonymization and compares target-selection strategies under an attack protocol.
- **Conceptual structure:** Privacy is measured through attacker recognition error; the interpretable factors connect a score change to a specific speech property.
- **What paper reports:** The paper reports that anonymizing duration and variation substantially increases privacy and that target selection changes attack outcomes.
- **Limits:** The evidence is bounded to kNN-VC, the attack model, selected prosodic factors, and utility measures; stronger attackers and human judgments remain open.

## 16. text-to-speech-and-content

**Paper:** [Code Mix TTS: An Approach to Infer Human Like Speech for Multi-Lingual Input Texts](https://www.isca-archive.org/interspeech_2025/gourav25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `13396297a5acb2acb644562e7cd94e578ae6bf713859b56644c8d68b6952ac35`; full text captured.

- **Ordinary problem:** A text-to-speech system should sound natural when a speaker mixes languages in one utterance, as people commonly do in multilingual communities.
- **Why hard:** Monolingual training assumptions make language switches, pronunciation, and voice continuity brittle.
- **Naive attempt:** Force the input into one language or fine-tune on a new code-mixed dataset.
- **Central move:** Infer code-mixed speech from multilingual text without requiring additional training data or fine-tuning.
- **Mechanism:** The proposed inference procedure sends multilingual input through an existing TTS system and evaluates generated code-mixed speech with automated MOS-style measures.
- **Conceptual structure:** The central tradeoff is whether language-switch content is retained while synthesized audio remains natural; the paper uses automated quality scoring rather than a new training loss.
- **What paper reports:** The paper reports an approach for code-mix inference without extra data or fine-tuning; the preserved evidence does not establish broad human preference gains.
- **Limits:** The paper's method and evaluation details are bounded by the selected TTS system, languages, and automated metric; human listening, pronunciation accuracy, and unseen language pairs remain open.

## 17. clinical-and-assistive-speech

**Paper:** [Test-Time Training for Speech-based Depression Detection](https://www.isca-archive.org/interspeech_2025/dumpala25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `7cb1cd64f77c89f84b93cef4a369bad6b4f6cf1180b2047abb12f663ccfb58a1`; full text captured.

- **Ordinary problem:** A depression detector trained in one recording setting should remain useful when test speech comes from another environment, demographic mix, or dataset.
- **Why hard:** Noise, gender, age, and collection procedures change the speech distribution without changing the clinical question.
- **Naive attempt:** Train once on a clean source dataset and assume the test distribution is the same.
- **Central move:** Adapt the model at test time using the incoming unlabeled speech so its internal features respond to the new distribution.
- **Mechanism:** The study applies test-time training to a speech-based depression detector and tests shifts from noise, gender, and dataset/curation differences.
- **Conceptual structure:** Performance under each shift is compared before and after adaptation; the important object is the distribution gap, not only the average source score.
- **What paper reports:** The paper reports substantial performance improvement under the tested shifts.
- **Limits:** The task is a clinical screening proxy, not a diagnosis; adaptation stability, labels in deployment, privacy, and external clinical validation remain open.

## 18. human-centered-evaluation

**Paper:** [Crowdsourcing MUSHRA Tests in the Age of Generative Speech Technologies: A Comparative Analysis of Subjective and Objective Testing Methods](https://www.isca-archive.org/interspeech_2025/lechler25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `f93a9f4de93bb1a0701ef3b4871f20cbeacf89f549601d1e91b27b6e45c7710b`; full text captured.

- **Ordinary problem:** Generative speech codecs need listening tests sensitive enough to detect subtle artifacts, but expert MUSHRA studies are expensive and objective metrics can mis-rank new systems.
- **Why hard:** Crowdsourced listeners vary by platform and expertise, while traditional metrics were designed for older signal distortions.
- **Naive attempt:** Use only objective metrics during development or reserve all listening tests for experts at the end.
- **Central move:** Adapt MUSHRA for non-experts online, compare platforms with expert data, and test whether objective metrics agree with people.
- **Mechanism:** The paper compares MTurk, Prolific, and expert ratings, measures test-retest reliability, and evaluates six objective metrics on generative speech codecs.
- **Conceptual structure:** MUSHRA ratings, reliability, platform effects, and metric-to-human alignment are separate quantities; collapsing them into one score hides the evaluation problem.
- **What paper reports:** The paper reports platform-specific bias, reasonable crowdsourced comparisons under its protocol, and that traditional metrics undervalue generative models.
- **Limits:** The result is bounded to the codecs, platforms, listener recruitment, and six metrics tested; other populations and model families remain open.

## 19. privacy-security-and-accountability

**Paper:** [PhonemeFake: Redefining Deepfake Realism with Language-Driven Segmental Manipulation and Adaptive Bilevel Detection](https://www.isca-archive.org/interspeech_2025/baser25b_interspeech.html)
**Evidence:** D3; PDF SHA-256 `94b1fe9ee7e02df9b12a5937e370e632c3d75cafe941405c97b0db7ba3ffdd3e`; full text captured.

- **Ordinary problem:** A deepfake detector should face manipulations that fool people, especially when only a few speech segments are changed to alter meaning.
- **Why hard:** Many benchmark fakes are easier for humans to spot than real attacks, and scanning every frame wastes computation.
- **Naive attempt:** Train on broad synthetic fakes and inspect the whole recording uniformly.
- **Central move:** Use language reasoning to choose critical phoneme segments for manipulation, then detect those regions with an adaptive two-level model.
- **Mechanism:** PhonemeFake creates segmental manipulations, measures human and benchmark deception, and trains a detector that allocates computation to suspicious regions across three datasets.
- **Conceptual structure:** Equal error rate measures detection, localization checks whether manipulated regions are found, and speed measures the cost of adaptive processing.
- **What paper reports:** The paper reports up to 42% lower human perception and 94% lower benchmark accuracy for attacks; its detector reports 91% EER reduction and up to 90% speed-up.
- **Limits:** These are author-reported results tied to attack construction, datasets, detector thresholds, and the chosen language reasoning; unseen generators and adversarial adaptation remain open.

## 20. metrics-and-targets

**Paper:** [Multivariate Probabilistic Assessment of Speech Quality](https://www.isca-archive.org/interspeech_2025/cumlin25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `3c57bbf2a98b5538bd29deac09883d832a0f0341a3aa8a5b8d5fb54627308f03`; full text captured.

- **Ordinary problem:** A speech-quality score should say not only that an utterance is poor but whether noise, coloration, discontinuity, or loudness caused the problem.
- **Why hard:** A single mean-opinion score hides different defects and cannot express uncertainty or relationships among them.
- **Naive attempt:** Predict MOS alone with a point estimator.
- **Central move:** Model MOS and four diagnostic quality dimensions jointly as a multivariate probability distribution.
- **Mechanism:** The model predicts a multivariate Gaussian through Cholesky factors and extends probabilistic affine transformations on NISQA ratings.
- **Conceptual structure:** The mean gives a point estimate, covariance gives uncertainty and correlations, and the NISQA dimensions provide a structured target instead of one scalar.
- **What paper reports:** The paper reports state-of-the-art-level point estimation while uniquely providing uncertainty and cross-dimension correlation estimates.
- **Limits:** The result is bounded to NISQA's labels and distributional assumptions; whether listeners and engineers benefit in new codecs or languages remains open.

## 21. noise-enhancement

**Paper:** [Improved Intelligibility of Dysarthric Speech using Conditional Flow Matching](https://www.isca-archive.org/interspeech_2025/das25b_interspeech.html)
**Evidence:** D3; PDF SHA-256 `7f931e5b2b688255edc162db541c8dc623343c9f9959fdaa86a658a4257f76d6`; full text captured.

- **Ordinary problem:** A person with dysarthria may know what they want to say but be hard to understand; conversion should improve intelligibility without erasing useful content or identity.
- **Why hard:** Dysarthric speech varies by speaker and severity, and mel-spectrogram targets may make generation slow or blur the relevant units.
- **Naive attempt:** Map dysarthric mel features to clean speech with an autoregressive or speaker-specific generator.
- **Central move:** Use discrete self-supervised acoustic units and conditional flow matching with a non-autoregressive Diffusion Transformer to map impaired to clearer speech.
- **Mechanism:** The study compares mel-spectrogram and quantized SSL features, controls the output voice with WavLM-derived information, and evaluates generated speech for dysarthric intelligibility.
- **Conceptual structure:** The learned flow maps a conditioning representation to clean-speech acoustics; intelligibility and convergence compare feature choices and generation paths.
- **What paper reports:** The paper reports that discrete acoustic units improve intelligibility and converge faster than the mel-spectrogram alternative.
- **Limits:** The result is bounded to the speakers, severity range, target voice, and tested listening/evaluation protocol; naturalness, identity preservation, and clinical benefit remain open.

## 22. robustness-and-system-boundary

**Paper:** [Ultra-Low Bit Post-Training Quantization of Large Speech Models via K-Means Clustering and Mixed Precision Allocation](https://www.isca-archive.org/interspeech_2025/gu25b_interspeech.html)
**Evidence:** D3; PDF SHA-256 `d24000ee163144cda02059d20dd2e670a4cd316309f2c920a1999e6aebdd553d`; full text captured.

- **Ordinary problem:** A large speech model must fit on practical hardware without losing recognition quality, especially when storage and memory are tight.
- **Why hard:** Below eight bits, transformer weight outliers make uniform quantization damage a small number of important parameters.
- **Naive attempt:** Round every weight to the same low-precision grid.
- **Central move:** Cluster weights nonlinearly, allocate more bits to columns with many outliers, and retain only critical outliers in sparse FP32 form.
- **Mechanism:** The method quantizes Whisper-Large-V3 after training and compares mixed precision and outlier retention across speech datasets.
- **Conceptual structure:** Bits per parameter expresses storage; WER measures recognition loss, and the columnwise allocation ties precision to the observed weight distribution.
- **What paper reports:** The paper reports 2.12-bit quantization with a 0.17 percentage-point WER increase on LibriSpeech test-clean and under 1% degradation across additional datasets.
- **Limits:** The result is author-reported for Whisper-Large-V3 and tested corpora; latency, energy, hardware kernels, and other model families remain open.

## 23. speaker-characteristics

**Paper:** [Towards Robust Speaker Recognition against Intrinsic Variation with Foundation Model Few-shot Tuning and Effective Speech Synthesis](https://www.isca-archive.org/interspeech_2025/chen25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `4523835b2f19dd904f99cc3d16247bda6bf7d9e275ed819f9e923ccc1d4dcdac`; full text captured.

- **Ordinary problem:** A speaker recognizer should recognize a person years later or in a different emotional state, while rejecting unknown people in an open set.
- **Why hard:** Age and emotion change the same speaker's voice, and limited enrollment data makes it hard to learn every future condition.
- **Naive attempt:** Enroll one fixed embedding and set a threshold that assumes the speaker is stable.
- **Central move:** Use few-shot foundation-model tuning at enrollment and generate style-rich synthetic speech to expose time-varying and emotional conditions, with losses focused on unknown outliers.
- **Mechanism:** The framework selects synthetic speech, tunes the foundation model with few enrollment examples, and evaluates open-set identification across time-varying and emotional benchmarks.
- **Conceptual structure:** Identification accuracy and open-set outlier behavior separate recognizing enrolled speakers from rejecting unknown speakers.
- **What paper reports:** The paper reports stronger generalization to aging and emotional variation while maintaining resistance to unknown outliers.
- **Limits:** The claim is bounded to the synthetic-data choices, foundation model, enrollment protocol, and benchmarks; real aging trajectories, spoofing attacks, and fairness across groups remain open.

## 24. accent-and-cultural-boundaries

**Paper:** [A Multi-Dialectal Dataset for German Dialect ASR and Dialect-to-Standard Speech Translation](https://www.isca-archive.org/interspeech_2025/blaschke25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `7a9f7d63cb5bf7e00bcf7040dac177d37eeaacf39e41a1b99bc91ff4da0749ae`; full text captured.

- **Ordinary problem:** An ASR and speech-translation system should preserve what a dialect speaker said rather than silently rewrite dialect grammar into the standard variety.
- **Why hard:** Dialect differences affect words, grammar, pronunciation, and what counts as a correct transcription; a single standard reference hides these distinctions.
- **Naive attempt:** Evaluate one multilingual ASR model against only a standardized transcript.
- **Central move:** Create paired dialectal and Standard German references across three underrepresented dialect groups and compare model outputs against both.
- **Mechanism:** Betthupferl contains four hours of read speech from Franconian, Bavarian, and Alemannic speakers plus Standard German; multilingual ASR models are evaluated for transcription and translation.
- **Conceptual structure:** Error analysis compares similarity to dialectal versus standardized references and inspects grammatical normalization, not only one aggregate score.
- **What paper reports:** The paper reports model-dependent differences: the best system sometimes normalizes dialect grammar but often stays closer to dialect constructions.
- **Limits:** The dataset is four hours of read speech from Southeast Germany; spontaneous speech, other dialects, conversational translation, and community judgments remain open.

