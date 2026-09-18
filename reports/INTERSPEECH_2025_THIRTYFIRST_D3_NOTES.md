# INTERSPEECH 2025 thirty-first-pass full-paper notes

Eight official-PDF readings deepen missing frequency detail, silent-speech sensing, flexible alignment, engaging conversation, domain robustness, low-resource transfer, post-hoc TTS control, and word timing. Results remain author-reported and were not independently reproduced.

## 1. time-frequency-measurement

**Paper:** [Neural Spectral Band Generation for Audio Coding](https://www.isca-archive.org/interspeech_2025/choi25d_interspeech.html)
**Evidence:** D3; PDF SHA-256 `3a85e632e3633a9b0e5d5184f5a2c552edfde62e984c674d21e06880ac9bcace`; full text captured.

- **Ordinary problem:** A low-bitrate codec may preserve the important low frequencies while losing high-frequency detail that makes speech and other sounds clear.
- **Why hard:** High-frequency content is not a fixed copy of the low-frequency band; different signals need different missing detail, and simply replicating a subband can add noise or dullness.
- **Naive attempt:** Copy or repeat the low-frequency spectrum into the missing band with a fixed spectral-band-replication rule.
- **Central move:** Encode compact side information about the missing band and use a learned generator conditioned on that information and the decoded core band.
- **Mechanism:** Neural spectral band generation uses an encoder-decoder to quantize high-frequency side information, reconstructs the band from core audio plus that information, and trains the whole codec with adversarial perceptual criteria.
- **Conceptual structure:** The codec separates what is transmitted from what is generated: the core band carries a base signal while a compact code selects plausible high-frequency detail; rate and perceptual quality expose the tradeoff.
- **What paper reports:** Using AAC as the core codec, the paper reports that n-SBG outperforms conventional SBR at comparable bitrates, especially at low rates, though some codec/rate combinations introduce audible noise.
- **Limits:** The core codec, bitrate, adversarial training, signal types, and perceptual metric bound the claim; plausible high-frequency detail is not guaranteed to be the original detail or to improve every downstream speech task.

## 2. room-channel-and-sensing

**Paper:** [Conformer-based Ultrasound-to-Speech Conversion](https://www.isca-archive.org/interspeech_2025/ibrahimov25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `00d449763fa543742c85bca1dcdd08afdecc7fb028bac8208f8afb5d78c6d738`; full text captured.

- **Ordinary problem:** A person who cannot or does not want to produce audible speech may still move the tongue and vocal tract; a silent-speech interface should turn those movements into understandable audio.
- **Why hard:** Ultrasound observes articulator motion rather than sound, and different speakers produce different motion-to-speech mappings; objective waveform similarity may disagree with what listeners hear.
- **Naive attempt:** Use a fixed image-to-speech mapping or make the model larger without testing whether the extra temporal context helps a speaker.
- **Central move:** Use a Conformer that combines local acoustic-image patterns with longer temporal context, and compare a simpler model with a bi-LSTM extension and a standard CNN.
- **Mechanism:** Two Conformer architectures map ultrasound from four speakers in Ultrasuite-Tal80 to mel spectrograms, then HiFi-GAN produces audio; MSE, mel-cepstral distortion, and a MUSHRA listening test are compared with a 2-D CNN.
- **Conceptual structure:** The input is a time sequence of vocal-tract images and the output is a time sequence of spectral frames; objective distance measures signal similarity, while MUSHRA measures perceived quality, so they test different meanings of 'better.'
- **What paper reports:** The paper reports no statistically significant objective improvement for either Conformer, but better perceptual quality for the bi-LSTM model; the base model matches the CNN while training about three times faster.
- **Limits:** Four speakers, speaker-specific training, ultrasound alignment, vocoder quality, and the listening panel bound the result; perceptual improvement is not evidence of speaker-independent silent speech or clinical usefulness.

## 3. boundaries-and-sequence-structure

**Paper:** [SiamCTC:  Learning Speech Representations through Monotonic Temporal Alignment](https://www.isca-archive.org/interspeech_2025/eom25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `0f06a96c93d3f4f735dd7b1efba279f31dc94e92961b6fca19df2f332a29a2ad`; full text captured.

- **Ordinary problem:** The same words can be spoken slowly, quickly, or with different timing, but a representation learner should recognize their shared content without forcing every frame to line up.
- **Why hard:** Frame-by-frame matching treats timing changes as content changes and breaks when one version stretches or compresses a sound.
- **Naive attempt:** Require every frame in two augmented views to have a fixed partner, or discard timing information entirely.
- **Central move:** Use CTC to align two views monotonically but flexibly, letting the learner compare their shared sequence while allowing insertions, deletions, and different speaking rates.
- **Mechanism:** SiamCTC combines Siamese views of speech with a CTC objective and tests speed perturbations and downstream phoneme/representation tasks against HuBERT and other baselines.
- **Conceptual structure:** CTC sums over possible monotonic alignments rather than choosing one frame correspondence; the representation is rewarded for preserving sequence content while tolerating temporal warping.
- **What paper reports:** The paper reports lower phoneme error under speaking-rate changes, with SiamCTC remaining relatively stable at 1.2x speed where HuBERT degrades more sharply.
- **Limits:** Augmentation choices, temperature, pretraining data, downstream task, and error metric bound the claim; flexible alignment does not guarantee invariance to accent, noise, or changes that alter linguistic content.

## 4. grounding-and-action

**Paper:** [Towards Human-like Multimodal Conversational Agent by Generating Engaging Speech](https://www.isca-archive.org/interspeech_2025/kim25m_interspeech.html)
**Evidence:** D3; PDF SHA-256 `ec031e7957b2dd522e3824d9f4d616b5ccdcce329d265da100adb55cb4b91182`; full text captured.

- **Ordinary problem:** A conversational agent can choose the right words yet sound dull or socially mismatched because real conversation also uses tone, mood, gesture, and response style.
- **Why hard:** These cues are spread across audio and video and are not fully recoverable from the text transcript; an engaging response must coordinate meaning with how it is said.
- **Naive attempt:** Generate a text response from text alone and use a generic TTS voice, or append a fixed emotion label after generation.
- **Central move:** Use audio-visual context to generate both the response text and a description of the voice style, then synthesize speech that carries the selected paralinguistic cues.
- **Mechanism:** The system builds a multi-sensory conversation dataset and uses a multimodal language model to produce text plus voice descriptions, which guide speech generation in dialogue examples.
- **Conceptual structure:** The model separates what to say from how to say it but conditions both on the same conversational state; human judgments of engagement and relevance test whether the separation remains coordinated.
- **What paper reports:** The paper reports more engaging and contextually suitable speech than text-only baselines and shows gains from visual and audio modalities.
- **Limits:** Dataset role-play, judge criteria, synthetic or recorded voices, conversation domain, and lack of exact-speaker replication bound the claim; engagement scores do not establish long-term human trust or natural conversation.

## 5. time-frequency-measurement-2

**Paper:** [Evaluating Deep Speaker Embedding Robustness to Domain, Sampling Rate, and Codec Variations](https://www.isca-archive.org/interspeech_2025/ferrofilho25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `42eeb2d2925cb0b68f3552745644b3d9d17c8ae5c2ac6e61a3c0696b637995aa`; full text captured.

- **Ordinary problem:** A speaker-verification model should recognize a person after the recording device, room, sampling rate, or codec changes, because real deployments rarely match training conditions.
- **Why hard:** Those changes remove or distort high-frequency and channel cues that an embedding may have learned as part of identity, so a strong matched-condition score can hide brittle evidence.
- **Naive attempt:** Train on one clean domain and treat later degradation as unavoidable noise, or compare models only at the training sampling rate and codec.
- **Central move:** Stress several embedding models across far-field, noise, music, sampling-rate, and compression shifts and measure how much verification performance moves.
- **Mechanism:** The study evaluates ECAPA-TDNN, TitaNet, ECAPA2, and ReDimNet on domain, sampling-rate, and codec variations, including far-field speech, noise, and music interference.
- **Conceptual structure:** Verification is a threshold decision on similarity between two embeddings; the experiment changes the recording path while holding the speaker task fixed, revealing which cues are not stable identity evidence.
- **What paper reports:** All models degrade under mismatched domains; ReDimNet degrades least in the tested settings, while downsampling and low-bitrate compression further hurt performance and expose reliance on high-frequency information.
- **Limits:** Datasets, codecs, sampling rates, threshold calibration, and attack/evaluation protocol bound the result; robustness to these shifts does not imply fairness or security against adaptive attacks.

## 6. low-resource-and-data-creation

**Paper:** [Speech LLMs in Low-Resource Scenarios: Data Volume Requirements and the Impact of Pretraining on High-Resource Languages](https://www.isca-archive.org/interspeech_2025/fong25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `fac22cfbeb6d608eb6f1cf8296f731c70208dfd66a26f9e619bb0880769bf091`; full text captured.

- **Ordinary problem:** A speech language model trained mostly on high-resource languages may need to recognize a low-resource language from very little labeled speech.
- **Why hard:** The model must connect acoustic evidence to a language model while learning with too few examples; pretraining can transfer useful structure but can also favor the languages that supplied it.
- **Naive attempt:** Train the entire speech-language system from scratch in the low-resource language, or assume a large multilingual model automatically solves the data shortage.
- **Central move:** Pretrain the small bridge between a speech encoder and language model on high-resource languages, then reuse it and measure how much low-resource data is still needed.
- **Mechanism:** Using SLAM-ASR with Whisper-large-v3-turbo and multilingual or monolingual LLMs, the paper varies training volume and projector pretraining, including Galician benchmarks.
- **Conceptual structure:** The projector is a learned translation between acoustic representations and language-model tokens; data-volume curves distinguish transferred alignment from new language-specific learning, while WER measures recognition.
- **What paper reports:** The paper reports that multilingual projector pretraining reduces the impact of scarce data; for Galician it reports WERs such as 13.3% on Common Voice and 19.4% on FLEURS in one configuration.
- **Limits:** Language choice, data cleanliness, projector, LLM, benchmark split, and WER bound the claim; transfer from high-resource languages does not establish equal performance or cultural adequacy.

## 7. prosody-and-interactive-control

**Paper:** [Counterfactual Activation Editing for Post-hoc Prosody and Mispronunciation Correction in TTS Models](https://www.isca-archive.org/interspeech_2025/lee25f_interspeech.html)
**Evidence:** D3; PDF SHA-256 `3547f7c666950c5a67df89996a79961f834e7219be6c23d29537d80d2ecedf16`; full text captured.

- **Ordinary problem:** A trained TTS system may pronounce a word incorrectly or use the wrong emphasis, and users may want to fix the output after training without rebuilding the model.
- **Why hard:** Prosody and pronunciation are encoded inside many hidden activations, while dictionary-based correction fails for names, new words, and low-resource languages.
- **Naive attempt:** Add a new prosody module, retrain the TTS model, or replace pronunciation with a fixed grapheme-to-phoneme dictionary.
- **Central move:** Find internal activations that causally change the unwanted behavior and edit them counterfactually at inference time, leaving the rest of the pretrained generator intact.
- **Mechanism:** Counterfactual Activation Editing modifies selected internal representations in a model-agnostic TTS system to alter prosodic features and correct mispronunciations; WER/PER, semantic similarity, and CMOS assess the tradeoff.
- **Conceptual structure:** The edit asks what output would result if a hidden feature were moved toward a desired state while other activations stayed fixed; causal intervention, not retraining, is the key object.
- **What paper reports:** The paper reports lower WER and PER, preserved semantic similarity, and a 0.764-point CMOS improvement from correcting prosody and mispronunciation.
- **Limits:** The chosen model, activation locations, correction targets, language, evaluation prompts, and listener panel bound the claim; an observed intervention effect does not prove a unique causal representation.

## 8. boundaries-and-sequence-structure-2

**Paper:** [Word Level Timestamp Generation for Automatic Speech Recognition and Translation](https://www.isca-archive.org/interspeech_2025/hu25e_interspeech.html)
**Evidence:** D3; PDF SHA-256 `d76d5c2a6e71d534e2fa694e5cd9fe27baa383fa1616d7de14ed09276bbacc92`; full text captured.

- **Ordinary problem:** A transcript or translation is more useful when each word has a time span for subtitles, search, and editing, but an end-to-end recognizer does not naturally expose word boundaries.
- **Why hard:** Word boundaries are latent decisions coupled to recognition and translation, and an external forced aligner adds a separate system that may disagree with the recognizer.
- **Naive attempt:** Run a separate aligner after ASR, or infer timestamps from token positions without checking their temporal accuracy.
- **Central move:** Train the recognizer to emit explicit start/end timestamp tokens using alignments generated by a teacher aligner, then predict timing directly with the speech model.
- **Mechanism:** The method adds a timestamp token to Canary, uses NeMo Forced Aligner outputs as teacher labels, and evaluates ASR timestamp precision/recall across four languages plus speech-translation timestamps.
- **Conceptual structure:** The timestamp token turns a continuous boundary estimate into a sequence prediction problem; precision, recall, timing error, WER, BLEU, and COMET show whether timing is gained without losing words or translation quality.
- **What paper reports:** The paper reports 80–90% timestamp precision/recall with 20–120 ms ASR errors; translation timestamps have about 200 ms error with reported BLEU and COMET drops, and it outperforms WhisperTimestamped for ASR timing.
- **Limits:** Teacher-aligner quality, tokenization, language, timing tolerance, translation metric drops, and data splits bound the result; usable timestamps do not prove perfect word boundaries or subtitle quality for every domain.

