# INTERSPEECH 2025 eleventh-pass full-paper notes

Eight additional official-PDF analyses deepen one first-principles branch in each major theme. Results remain author-reported and were not independently reproduced.

## 1. sound-and-production/time-frequency-measurement

**Paper:** [Frequency-Domain Enhanced Extreme Bandwidth Extension Network with ICCRN for Superior Speech Quality](https://www.isca-archive.org/interspeech_2025/bao25_interspeech.html)  
**Evidence:** D3; PDF SHA-256 0f92e471abc8a855bbd0ce77b0a2a5de3cc4af28f42042ade74c42afe388b474; 5 pages.

- **Big picture:** Bandwidth extension must recreate missing high-frequency speech without inventing spectral detail that listeners hear as distortion.
- **Why hard:** The missing band is not directly supervised by the degraded input; spectral errors can raise objective quality scores while changing consonant detail.
- **Naive attempt:** Copy low-frequency structure upward with a generic network and judge it by one waveform metric.
- **Central move:** Use frequency-domain enhancement with an ICCRN-style recurrent representation to preserve global spectral structure while reconstructing the absent band.
- **Mechanism:** The model operates on frequency representations, combines local and global context, and is compared against EBEN and other bandwidth-extension baselines.
- **Mathematical idea:** PESQ, SI-SDR, STOI, and MUSHRA separate signal fidelity, intelligibility, and listener preference.
- **Connections:** Bandwidth extension is an inverse problem: plausible high frequencies are constrained by the observed band and perceptual targets, not uniquely recovered.
- **What paper reports:** The tests show gains over the original EBEN, including a 40-person MUSHRA comparison; the authors report clearer high-frequency detail and less distortion.
- **Limits:** French LibriSpeech, sampling setup, listeners, and author-reported metrics bound the result; other languages remain open.

## 2. listening-and-separation/echo-and-reconstruction

**Paper:** [MiSTR: Multi-Modal iEEG-to-Speech Synthesis with Transformer-Based Prosody Prediction and Neural Phase Reconstruction](https://www.isca-archive.org/interspeech_2025/alradhi25_interspeech.html)  
**Evidence:** D3; PDF SHA-256 3ee13b318b756079bc0d5e0c82e3bf2d800a61e5035c9a391a26ff271d7dd263; 5 pages.

- **Big picture:** Brain recordings may contain enough motor or auditory information to reconstruct intelligible speech for people who cannot produce it normally.
- **Why hard:** Neural signals are indirect, data are limited, and a reconstruction can be spectrally plausible yet unintelligible or unnatural.
- **Naive attempt:** Map neural features directly to a waveform and let a generic vocoder repair phase and prosody.
- **Central move:** Separate linguistic/prosodic prediction from neural phase reconstruction, then use a neural vocoder and a learned MOSA evaluator.
- **Mechanism:** MiSTR uses a multimodal iEEG encoder, Transformer spectrogram/prosody prediction, and a neural phase vocoder with adaptive spectral correction.
- **Mathematical idea:** Mel-spectrogram correlation, intelligibility, naturalness, and MOSA expose different reconstruction failures; MOSA is reported at 3.38.
- **Connections:** The system is a chain of constrained reconstructions: neural evidence determines content and prosody while the vocoder supplies waveform detail.
- **What paper reports:** The paper reports higher fidelity and naturalness than listed baselines and MOSA 3.38.
- **Limits:** Dataset, subjects, protocol, learned evaluator, and paper-reported comparisons limit clinical claims.

## 3. recognition-and-alignment/adaptation-and-open-vocabulary

**Paper:** [Domain Adaptation Method and Modality Gap Impact in Audio-Text Models for Prototypical Sound Classification](https://www.isca-archive.org/interspeech_2025/acevedo25_interspeech.html)  
**Evidence:** D3; PDF SHA-256 228720572e58e79cf52af2b5ad83741a15149b53cf2613fb81f7cf165fdf7d3b; 5 pages.

- **Big picture:** Audio-text classifiers fail when the acoustic domain changes even if the label vocabulary stays fixed.
- **Why hard:** The text embedding can remain stable while the audio embedding moves with background and SNR.
- **Naive attempt:** Tune only text prompts or assume a frozen audio-text embedding is domain invariant.
- **Central move:** Adapt the audio side using representative target-domain sound examples and test transfer across environments.
- **Mechanism:** The method aligns audio representations to the target domain and compares audio-based with text-based adaptation.
- **Mathematical idea:** Top-1 accuracy across environments and SNRs measures whether adaptation closes the modality/domain gap; the zero-shot reference is 32.4%.
- **Connections:** Domain adaptation changes which acoustic evidence the shared representation treats as invariant while preserving the open label interface.
- **What paper reports:** Audio-based adaptation gives the largest reported gains across tested conditions.
- **Limits:** Sound set, target examples, class construction, and reported accuracy limit open-world claims.

## 4. meaning-and-interaction/prosody-and-intent

**Paper:** [Coping with segmental–prosodic incongruity in spoken word recognition in Japanese](https://www.isca-archive.org/interspeech_2025/ariga25_interspeech.html)  
**Evidence:** D3; PDF SHA-256 10247574502e1b6779b7e9a37aaf76aa976fc717897595425bc8cd727a142bcc; 5 pages.

- **Big picture:** Listeners combine segmental sounds and lexical pitch accent when recognizing Japanese words, even when the cues disagree.
- **Why hard:** The cues arrive together, priming can mask later effects, and response time does not by itself identify the updated representation.
- **Naive attempt:** Treat phonemes as the only lexical evidence or assume prosody simply overrides segments.
- **Central move:** Create controlled incongruent words and use repetition priming and response timing to test each cue.
- **Mechanism:** Experiments isolate cue type, delay, and lexical repetition; mixed-effects models compare segmental and prosodic conditions.
- **Mathematical idea:** Response-time models compare conditions; the paper reports prosodic inhibition at a 750 ms interval.
- **Connections:** Prosody is part of lexical recognition, not only an expression-layer signal.
- **What paper reports:** Results suggest prosodic mispronunciation inhibits recognition at the tested delay.
- **Limits:** Japanese materials, pitch-accent system, participants, and laboratory task limit cross-language generalization.

## 5. voice-generation-and-control/text-to-speech-and-content

**Paper:** [Facilitating Personalized TTS for Dysarthric Speakers Using Knowledge Anchoring and Curriculum Learning](https://www.isca-archive.org/interspeech_2025/jeon25_interspeech.html)  
**Evidence:** D3; PDF SHA-256 17543ed8ca27efa940eb68bceb9ddae535aa03490bd476855183466aa8f0661b; 5 pages.

- **Big picture:** Personalized TTS for dysarthric speakers must preserve identity while producing intelligible speech from scarce and errorful recordings.
- **Why hard:** A model can improve intelligibility by erasing the speaker traits personalization is meant to retain.
- **Naive attempt:** Fine-tune directly on all target audio and accept overfitting or poor pronunciation.
- **Central move:** Anchor the target speaker to a teacher model and use curriculum learning before specializing to dysarthric articulation.
- **Mechanism:** A teacher-student knowledge-anchoring framework is evaluated across speaker groups with shortened audio.
- **Mathematical idea:** PER measures intelligibility and speaker similarity measures identity; reported PER reaches 15.579 and similarity rises from 0.586 to 0.708.
- **Connections:** Personalization is constrained transfer: move toward the target voice without transferring articulation errors as content errors.
- **What paper reports:** Curriculum and anchoring lower PER and improve speaker similarity across reported groups.
- **Limits:** Groups, language, recording conditions, and reported metrics limit clinical claims.

## 6. people-variation-and-health/human-centered-evaluation

**Paper:** [Hearing deficits of transformer-based ASR for anechoic and spatial signals](https://www.isca-archive.org/interspeech_2025/hoffner25_interspeech.html)  
**Evidence:** D3; PDF SHA-256 50d49d6d27a39f28367dad2a3698cb17cc9bc804f6b6cf8c0ed14fe49b5ec0ab; 5 pages.

- **Big picture:** ASR and humans should be compared on the same speech-in-noise task rather than assuming low WER means human-like hearing.
- **Why hard:** Human recognition depends on thresholds, spatial cues, rooms, and masking; model size changes errors without modeling those mechanisms.
- **Naive attempt:** Report ASR WER in clean speech as a proxy for hearing performance.
- **Central move:** Estimate speech-reception thresholds from controlled sentences in noise for ASR models and humans.
- **Mechanism:** Whisper models are tested on anechoic and spatial signals; thresholds come from WER curves at 50% error.
- **Mathematical idea:** SRT and psychometric slope make the human-machine gap explicit rather than hiding it in average WER.
- **Connections:** Hearing is an operating boundary shaped by scene geometry and noise, not one recognition score.
- **What paper reports:** Model size improves ASR thresholds, but the gap changes with language, room, and spatial signals.
- **Limits:** Whisper versions, German/English material, steady noise, and laboratory setup limit claims.

## 7. languages-accents-and-resources/multilingual-and-crosslingual

**Paper:** [TalTech Systems for the Interspeech 2025 ML-SUPERB 2.0 Challenge](https://www.isca-archive.org/interspeech_2025/alumae25_interspeech.html)  
**Evidence:** D3; PDF SHA-256 b56d427c2d320aac37c04c4573fe06968581489a58a01f1632424d919a38194e; 5 pages.

- **Big picture:** A multilingual recognizer must allocate limited capacity across languages with different data sizes and acoustic demands.
- **Why hard:** Average scores hide low-resource failures; language-ID errors and subword choices can contaminate recognition.
- **Naive attempt:** Train one pooled recognizer and optimize aggregate CER, letting high-resource languages dominate.
- **Central move:** Use hybrid language identification, multilingual and language-specific models, and targeted decoding resources.
- **Mechanism:** The system combines language identification with multilingual ASR and customized models, then evaluates language ID and CER.
- **Mathematical idea:** Language-ID accuracy and mean CER expose routing and transcription separately; reported values are 86.8% and 27.4%.
- **Connections:** Multilinguality is resource allocation: the front end decides the linguistic regime before recognition specializes.
- **What paper reports:** The system is competitive with challenge baselines and identifies languages needing targeted work.
- **Limits:** Challenge data, language mix, averaging, and tuning limit all-multilingual claims.

## 8. evaluation-deployment-and-consequence/robustness-and-system-boundary

**Paper:** [Evaluating ASR Robustness to Spontaneous Speech Errors: A Study of WhisperX Using a Speech Error Database](https://www.isca-archive.org/interspeech_2025/alderete25_interspeech.html)  
**Evidence:** D3; PDF SHA-256 c7d3c80f0f2d9ddab4ab238b91e1f90eb1106016f792944bf2ce8f5303c69303; 5 pages.

- **Big picture:** ASR robustness should be tested on errors people actually produce, not only clean speech or synthetic noise.
- **Why hard:** Speech errors differ by type and position; aggregate WER hides which deviation caused failure.
- **Naive attempt:** Report one WER on spontaneous speech and treat all deviations as equivalent noise.
- **Central move:** Use annotated SFUSED speech errors to stratify WhisperX performance by error type and word position.
- **Mechanism:** The study evaluates sound and word errors with controlled classification variables and compares initial, medial, and final positions.
- **Mathematical idea:** Accuracy by error class and position reveals interactions; sound errors are reported as easier than word errors.
- **Connections:** Robustness is a boundary map: which linguistic deviations cross the recognizer's failure boundary, and where.
- **What paper reports:** Sound errors have higher transcription accuracy than word errors, with position-dependent differences.
- **Limits:** Database, annotations, WhisperX, language, and task design limit generalization.

