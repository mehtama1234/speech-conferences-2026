# INTERSPEECH 2025 twenty-ninth-pass full-paper notes

Eight official-PDF readings deepen channel-dependent prosody, multilingual emotion, physical vocal-tract measurement, long-form recognition, codec efficiency, dysarthric reconstruction, and foundation-model compression. Results are author-reported and not independently reproduced.

## 1. prosody-and-intent-1

**Paper:** [Stress in Spoken and Whistled Greek](https://www.isca-archive.org/interspeech_2025/batchelderschwab25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `3fee5276099baae69eb179f0e66cd303040d9514ac2d865d1147887ea09efbef`; full text captured.

- **Ordinary problem:** A community can communicate by whistling, so a listener must know how spoken vowel and stress distinctions survive when the sound source changes.
- **Why hard:** Whistling removes many speech cues and concentrates information in pitch and intensity, so a spoken-language assumption may misidentify what remains contrastive.
- **Naive attempt:** Assume every spoken vowel and stress cue must have the same acoustic realization in the whistle register.
- **Central move:** Compare matched minimal pairs in spoken and whistled Greek and identify which vowel and stress contrasts are carried by F0, intensity, or neither.
- **Mechanism:** Participants produce five Greek vowel qualities in Sfyria whistling and spoken Greek; acoustic contrasts are compared for stressed and unstressed forms.
- **Conceptual structure:** The representation changes with the communication channel: F0 and intensity are alternative carriers of phonological contrast, and a missing cue is itself evidence.
- **What paper reports:** All five vowel qualities remain distinct in the whistled register, but a whistled stress correlate is not found for /i/, possibly because front vowels are already highly intense.
- **Limits:** The Sfyria community, participants, register, minimal pairs, and acoustic cues bound the result; a ceiling interpretation and cross-language generalization remain open.

## 2. prosody-and-intent-2

**Paper:** [Multi-Teacher Language-Aware Knowledge Distillation for Multilingual Speech Emotion Recognition](https://www.isca-archive.org/interspeech_2025/bijoy25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `391d0eaa6ca6738c4e242d83c5648787cac1db012609926cdacbc898c263e663`; full text captured.

- **Ordinary problem:** One emotion recognizer should serve several languages without letting the largest language erase smaller languages or their emotion patterns.
- **Why hard:** Languages differ in acoustic and linguistic cues, and one teacher model may be strong in one language but transfer the wrong priorities to another.
- **Naive attempt:** Train one multilingual model directly or average teacher predictions without identifying which language produced the speech.
- **Central move:** Use separate monolingual teachers and a language-aware distillation process to teach one student while preserving language-specific evidence.
- **Mechanism:** Wav2vec2 teachers for English, Finnish, and French are distilled into one multilingual student and evaluated by emotion recall per language and class.
- **Conceptual structure:** The student is a shared model with language-conditioned supervision; weighted and unweighted recall expose both overall performance and class imbalance.
- **What paper reports:** The student reports weighted recall 72.9 on English and unweighted recall 63.4 on Finnish, with stronger gains for sad and neutral than anger and happiness.
- **Limits:** Languages, emotion labels, teacher quality, class balance, and recall metrics bound the claim; multilingual transfer does not prove equal performance or culturally valid emotion categories.

## 3. source-filter-production-1

**Paper:** [Influence of wall coverings of 3D-printed vocal tract models on measured transfer functions](https://www.isca-archive.org/interspeech_2025/birkholz25b_interspeech.html)
**Evidence:** D3; PDF SHA-256 `ecb8ea59cb5269cfb4ec3ae01f5b0cfe5a6824d12760d0104a67d84f186d0c20`; full text captured.

- **Ordinary problem:** A physical vocal-tract replica should reveal the resonances of a modeled vowel, but the printed walls can vibrate and create false peaks and gaps.
- **Why hard:** The measurement apparatus can confuse sound transmitted through the model body with sound traveling through the intended tract cavity.
- **Naive attempt:** Trust the measured transfer function or change only the acoustic excitation while ignoring the replica's structural vibration.
- **Central move:** Dampen or mechanically constrain the replica and test whether the expected resonances become cleaner and more repeatable.
- **Mechanism:** Ten axisymmetric 3D-printed vowel tubes are measured with reciprocity; sound-absorbing fabric and sand embedding are compared as artifact-reduction methods.
- **Conceptual structure:** The transfer function is a physical measurement shaped by both air paths and solid-body vibration; artifact reduction is tested through resonance structure and repeatability.
- **What paper reports:** Both coverings reduce spurious poles and zeros and improve repeatability of the measured transfer functions.
- **Limits:** Printed geometries, ten vowels, materials, reciprocity setup, and repeatability metric bound the claim; improved measurement does not prove the replica matches a human tract.

## 4. source-filter-production-2

**Paper:** [Equivalence and differences: Formant patterns of labialization and pharyngealization in Tashlhiyt](https://www.isca-archive.org/interspeech_2025/buech25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `86ee48dd3d0986f191969e463e4cbedcd3b022c82b4423920868cc68020b48b7`; full text captured.

- **Ordinary problem:** Two different tongue and lip gestures may produce similar formant changes, so a listener or analyst cannot infer articulation from one acoustic cue alone.
- **Why hard:** Labialization and pharyngealization modify different parts of the tract but can both lower F2, making a shared acoustic effect look like a shared gesture.
- **Naive attempt:** Treat a low F2 as proof of one particular secondary articulation.
- **Central move:** Compare adjacent-vowel formants across both articulations, vowel qualities, and speakers, then identify which formants preserve their difference.
- **Mechanism:** Thirty-five Tashlhiyt speakers produce VCV logatomes with /i, a, u/ and labialized or pharyngealized consonants; F1 and F2 patterns are compared.
- **Conceptual structure:** The mapping is many-to-one: F2 can reveal a broad acoustic effect while F1 and vowel context retain articulatory distinctions.
- **What paper reports:** Both articulations show similar F2 effects, strongest for /i/ and then /a/, while differences depend on F1 and vowel quality.
- **Limits:** The language, speakers, logatomes, adjacent vowels, and formant measures bound the result; formants alone cannot identify every articulatory gesture.

## 5. metrics-and-targets

**Paper:** [Exploring Linear Variant Transformers and k-NN Memory Inference for Long-Form ASR](https://www.isca-archive.org/interspeech_2025/carvalho25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `2f4aa4cc89fdc990e1c46383a4c23cdd228f92f5d5547c3e1263c8acdc99c58b`; full text captured.

- **Ordinary problem:** A recognizer must process long recordings without making attention cost grow too quickly or forgetting what happened earlier.
- **Why hard:** Short-form transformer success does not guarantee tractable long-form decoding, and a model with local efficiency may lose useful distant context.
- **Naive attempt:** Apply ordinary quadratic self-attention to the entire recording or split it into chunks and discard cross-chunk memory.
- **Central move:** Compare linear-time sequence architectures and add a non-trained nearest-neighbor memory that retrieves useful earlier representations during inference.
- **Mechanism:** Fastformer, SummaryMixing, BiMamba, and E-Branchformer variants are evaluated on a new LibriHeavy long-form benchmark; KNN-MAN is added to encoder-decoder models.
- **Conceptual structure:** Long-form recognition is a time-scale and memory problem: architecture controls cost while retrieval supplies selected history; WER across duration scales tests the tradeoff.
- **What paper reports:** The paper reports a reduction from 18.8% to 17.5% WER on its LibriSpeech long-form test-clean example with BiMamba and KNN-MAN.
- **Limits:** Benchmark construction, duration distribution, memory retrieval, architectures, and WER bound the result; a single long-form corpus does not establish general conversation robustness.

## 6. robustness-and-system-boundary

**Paper:** [NanoCodec: Towards High-Quality Ultra Fast Speech LLM Inference](https://www.isca-archive.org/interspeech_2025/casanova25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `94b942d9676fb3e3204821f38649c376f7ab4dee89b49344a970e6ec86f5532d`; full text captured.

- **Ordinary problem:** A speech language model should generate high-quality audio quickly, but autoregressive generation must produce many codec tokens for each second of speech.
- **Why hard:** A high-rate codec can preserve detail while making training and inference slow; lowering the rate can destroy quality or causal timing.
- **Naive attempt:** Use a high-frame-rate codec and accept the step count, or reduce frames without testing which bitrate and causality choices caused the quality loss.
- **Central move:** Measure the separate effects of frame rate, bitrate, and causality, then design a codec with a low frame rate that still reconstructs speech well.
- **Mechanism:** NanoCodec is evaluated through codec ablations and compared across bitrate ranges, targeting 12.5 frames per second for speech LLM training and inference.
- **Conceptual structure:** The codec converts a continuous waveform into fewer discrete generation steps; reconstruction quality and rate expose the speed-quality boundary.
- **What paper reports:** The paper reports high-quality compression at 12.5 FPS and competitive performance across tested bitrates.
- **Limits:** Codec architecture, audio data, bitrate, causality, quality metric, and hardware bound the result; low frame rate alone does not prove low end-to-end latency.

## 7. noise-enhancement

**Paper:** [DiffDSR: Dysarthric Speech Reconstruction Using Latent Diffusion Model](https://www.isca-archive.org/interspeech_2025/chen25m_interspeech.html)
**Evidence:** D3; PDF SHA-256 `e016be381b2a8968b994a4c4f117b2917420ebac669567a7035d29ad1fb6e2f6`; full text captured.

- **Ordinary problem:** A person with dysarthria may know the intended words but produce speech that listeners cannot understand; reconstruction should improve clarity without replacing the person's voice.
- **Why hard:** Content is hard to recover from atypical acoustics, while a system that focuses only on clarity can erase speaker identity.
- **Naive attempt:** Train a generic speech enhancer or normalize the voice toward an average speaker.
- **Central move:** Separate content recovery from identity preservation and generate a clearer signal in a latent space conditioned on both.
- **Mechanism:** DiffDSR uses a self-supervised speech content encoder, an in-context speaker identity encoder, and a latent diffusion generator on UASpeech.
- **Conceptual structure:** The system has two constraints—recover phoneme content and retain speaker identity—so intelligibility and speaker similarity must be evaluated separately.
- **What paper reports:** The paper reports improved speech intelligibility and speaker similarity over prior dysarthric speech reconstruction methods on UASpeech.
- **Limits:** UASpeech, speaker identities, dysarthria types, reconstruction target, and metrics bound the claim; improved similarity and intelligibility are not clinical validation or authorship proof.

## 8. acoustic-unit-mapping

**Paper:** [DiceHuBERT: Distilling HuBERT with a Self-Supervised Learning Objective](https://www.isca-archive.org/interspeech_2025/chi25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `963cbd3bc74318c044302f225cc30409259cb8c4480940170c7ed15ea9479ca5`; full text captured.

- **Ordinary problem:** A large self-supervised speech model may be useful but too expensive to store or run, so a smaller student must retain the teacher's reusable speech knowledge.
- **Why hard:** Layer-by-layer imitation adds alignment machinery and can force the student to copy the teacher's structure rather than its learning objective.
- **Naive attempt:** Compress each teacher layer with a separate matching module or simply shrink the network and accept lost representations.
- **Central move:** Replace the HuBERT teacher with a smaller student trained directly under HuBERT's iterative self-supervised objective.
- **Mechanism:** DiceHuBERT distills HuBERT using the same self-supervised objective and evaluates the compact model on phoneme recognition, ASR, and SUPERB tasks.
- **Conceptual structure:** The student learns the task's predictive structure instead of matching every hidden layer; downstream performance measures retained usefulness across tasks.
- **What paper reports:** The paper reports over 21% improvement in phoneme recognition and over 14% in ASR relative to existing distillation methods, with competitive multi-task results.
- **Limits:** Teacher/student sizes, SUPERB tasks, training data, and comparison baselines bound the result; benchmark transfer does not establish equal behavior under every deployment constraint.

