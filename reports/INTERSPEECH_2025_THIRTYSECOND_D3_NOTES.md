# INTERSPEECH 2025 thirty-second-pass full-paper notes

Eight official-PDF readings deepen long-speech clinical evidence, directional room fields, contextual ASR, multimodal conversation, expressive style, dialect augmentation, phonetic annotation, and oral-history transcription. Results remain author-reported and were not independently reproduced.

## 1. time-frequency-measurement

**Paper:** [An interpretable speech foundation model for depression detection by revealing prediction-relevant acoustic features from long speech](https://www.isca-archive.org/interspeech_2025/deng25b_interspeech.html)
**Evidence:** D3; PDF SHA-256 `205b56374a13e30924af66ef9429852ce62be0da69800e314c28272025dad16c`; full text captured.

- **Ordinary problem:** A speech-based depression screening system should use enough of a person's speech to reflect a clinical state rather than treating a long answer as a bag of short unrelated clips.
- **Why hard:** Short segments can receive noisy labels because depression is labeled at the recording or person level, and a model may rely on loudness or pitch without showing a clinician what it used.
- **Naive attempt:** Split every recording into short windows, assign the same label to each, and report only a black-box score.
- **Central move:** Model the full speech recording and expose which time-frequency regions and acoustic properties drive the decision.
- **Mechanism:** The paper uses a speech-level Audio Spectrogram Transformer on long-duration speech and introduces an interpretation method that identifies prediction-relevant acoustic features, comparing it with a segment-level AST.
- **Conceptual structure:** Longer context reduces segment-label noise; attention over the spectrogram is converted into an acoustic explanation, so the model's output is treated as evidence to inspect rather than a diagnosis itself.
- **What paper reports:** The paper reports better depression detection than the segment-level model and identifies reduced loudness and F0 as relevant signals consistent with prior clinical findings.
- **Limits:** Dataset, diagnostic labels, recording protocol, attention interpretation, and screening threshold bound the claim; a predictive acoustic correlate is not a clinical cause or validated diagnosis.

## 2. room-channel-and-sensing

**Paper:** [Direction-Aware Neural Acoustic Fields for Few-Shot Interpolation of Ambisonic Impulse Responses](https://www.isca-archive.org/interspeech_2025/ick25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `b814a35a63dbf079f8f6188dbbca124b5bc838388e77b29b545189cc1298131b`; full text captured.

- **Ordinary problem:** A listener or renderer needs to know how sound changes across positions and directions in a room, but measuring every room impulse response at every point is expensive.
- **Why hard:** A room response depends on source position, listener position, and direction, and an omnidirectional or binaural model can miss how a directional microphone or loudspeaker receives the field.
- **Naive attempt:** Interpolate each measured channel independently or assume one direction represents all incoming sound at a point.
- **Central move:** Learn a spatially continuous neural field that takes source/listener geometry and direction as inputs and predicts ambisonic impulse responses between sparse measurements.
- **Mechanism:** Direction-Aware Neural Acoustic Fields model ambisonic room impulse responses with a neural field and add explicit directional information, evaluating few-shot interpolation against prior monaural/binaural fields.
- **Conceptual structure:** The neural field is a function from geometry and direction to a time-domain response; the key test is whether a smooth physical variation can be inferred from sparse samples without inventing inconsistent channels.
- **What paper reports:** The paper reports improved few-shot interpolation of directional ambisonic responses over prior neural-field formulations in its room measurements.
- **Limits:** Room geometry, microphone/ambisonic order, sampling locations, interpolation range, and waveform metrics bound the claim; interpolation quality does not prove accurate rendering in unseen rooms or perceptual equivalence.

## 3. boundaries-and-sequence-structure

**Paper:** [Exploring SSL Discrete Speech Features for Zipformer-based Contextual ASR](https://www.isca-archive.org/interspeech_2025/cui25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `3f2170f5278bed1b1972570a7f0b1116f2b534c5ed21531693d330b48f96ccf7`; full text captured.

- **Ordinary problem:** A recognizer often needs the previous and next utterances to resolve names, references, or conversational context, but the context representation must be compact enough to train and run efficiently.
- **Why hard:** Continuous hidden features carry useful detail but are expensive, while a discrete representation may discard the very context needed for a difficult utterance.
- **Naive attempt:** Ignore cross-utterance context, concatenate every hidden vector, or use a large continuous speech model and accept its training cost.
- **Central move:** Compare discrete speech tokens and continuous features for pooled or concatenated context in a Zipformer-Transducer, measuring both recognition gains and efficiency.
- **Mechanism:** The study evaluates contextual Z-T systems on 1,000-hour GigaSpeech-M and DementiaBank Pitt elderly speech, using SSL discrete tokens, WavLM features, and preceding/current/future context variants.
- **Conceptual structure:** Context is a sequence decision: the representation must preserve the distinctions useful for the next utterance while reducing the number of values passed to the recognizer; WER and training time expose the tradeoff.
- **What paper reports:** Discrete-token contextual systems reduce WER by 0.39 and 1.41 absolute points on the two tasks and achieve up to 4.36x training speedup over continuous WavLM context systems.
- **Limits:** Corpora, context windows, tokenization, speed hardware, and statistical test bound the result; better contextual WER does not prove robust dialogue understanding or causal use of future context in deployment.

## 4. grounding-and-action

**Paper:** [Face2VoiceSync: Lightweight Face-Voice Consistency for Text-Driven Talking Face Generation](https://www.isca-archive.org/interspeech_2025/kang25c_interspeech.html)
**Evidence:** D3; PDF SHA-256 `bef3996fb824e750552a884236f007a9c97a1f51dd62cd0fb0a0d48a295fef5c`; full text captured.

- **Ordinary problem:** A talking-face system should make a face and a voice that agree when given a face image and text, rather than forcing the user to supply a matching speech recording.
- **Why hard:** Text specifies what is said but not the target voice, while a face image specifies appearance but not timing or vocal identity; independently generating the modalities can create a visible-audible mismatch.
- **Naive attempt:** Drive the face from a fixed speech signal or generate a generic voice and animate the face afterward without checking cross-modal consistency.
- **Central move:** Generate the talking-face motion and speech jointly from face and text, with a consistency constraint linking the visual identity and vocal output.
- **Mechanism:** Face2VoiceSync targets text-driven talking-face generation from a face image and text, producing animation and corresponding speech while evaluating the consistency of face and voice attributes.
- **Conceptual structure:** The desired output is a coupled pair: text constrains linguistic content, face conditions visual identity, and a learned cross-modal relation checks whether the generated voice belongs with the generated face.
- **What paper reports:** The paper reports improved face-voice consistency and text-driven talking-face generation quality relative to fixed-speech baselines.
- **Limits:** Face identities, text prompts, speech/face datasets, consistency metric, and synchronization quality bound the claim; a consistency score does not prove that a viewer will find the character natural or trustworthy.

## 5. prosody-and-interactive-control

**Paper:** [Spotlight-TTS: Spotlighting the Style via Voiced-Aware Style Extraction and Style Direction Adjustment for Expressive Text-to-Speech](https://www.isca-archive.org/interspeech_2025/kim25t_interspeech.html)
**Evidence:** D3; PDF SHA-256 `9cead5a38aa2002e9b36e111bac81f19b76da36587cfc3ede972a6db8731ca71`; full text captured.

- **Ordinary problem:** A TTS system may have a style reference, but if it extracts style from unvoiced pauses or irrelevant regions, the generated voice can sound less expressive or lose continuity.
- **Why hard:** Style is carried strongly by voiced regions yet transitions across voiced and unvoiced regions must remain smooth; an embedding that captures everything can mix content, speaker, and style.
- **Naive attempt:** Average one style embedding over the whole waveform or add a separate style module without controlling what it attends to.
- **Central move:** Extract style primarily from voiced regions and adjust the direction of the style representation before injecting it into the TTS model.
- **Mechanism:** Spotlight-TTS uses voiced-aware style extraction, continuity across speech regions, and style-direction adjustment, then compares expressive speech quality and transfer against baseline style-embedding systems.
- **Conceptual structure:** The model treats style as a direction in a representation space rather than a fixed label; selecting voiced evidence and adjusting its direction are two separate controls on what gets transferred.
- **What paper reports:** The paper reports stronger expressiveness, overall speech quality, and style-transfer capability than its baselines in objective and perceptual evaluations.
- **Limits:** Reference speakers, style labels, voiced-region detection, subjective ratings, and TTS architecture bound the result; a style direction is not a complete account of emotion, identity, or conversational appropriateness.

## 6. low-resource-and-data-creation

**Paper:** [Improving Low-Resource Dialect Classification Using Retrieval-based Voice Conversion](https://www.isca-archive.org/interspeech_2025/fischbach25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `3490081268b6779f7981bba1701ad8fa6915333602531d50c5f2107bf38da39d`; full text captured.

- **Ordinary problem:** A dialect classifier should learn pronunciation and linguistic differences, but a low-resource dialect corpus may contain too few speakers to separate dialect from speaker identity.
- **Why hard:** Speaker-specific vocal traits can be easier to learn than dialect cues, so adding more altered copies of the same speakers may increase data without adding the missing variation.
- **Naive attempt:** Train directly on the small corpus or apply generic noise/masking augmentation that changes the signal without targeting the nuisance speaker factor.
- **Central move:** Use retrieval-based voice conversion to put examples into a more uniform target-speaker space, then combine it with ordinary augmentations and test whether dialect classification improves.
- **Mechanism:** RVC converts low-resource German dialect samples toward a uniform target speaker; experiments compare RVC alone and with frequency masking and segment removal for dialect classification.
- **Conceptual structure:** The augmentation changes speaker identity while attempting to preserve phonetic and dialect information; classifier accuracy tests whether the nuisance factor was reduced rather than merely replaced.
- **What paper reports:** The paper reports improved dialect-classification performance from RVC augmentation, with further gains when combined with frequency masking and segment removal.
- **Limits:** Dialect data, target speaker, conversion fidelity, train/test speaker split, and classifier architecture bound the claim; higher accuracy does not prove that all dialect cues survived conversion.

## 7. boundaries-and-sequence-structure-2

**Paper:** [Transcript-Prompted Whisper with Dictionary-Enhanced Decoding for Japanese Speech Annotation](https://www.isca-archive.org/interspeech_2025/hu25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `2bf1d8afae46fbec8812e9c627ec5f7add03fd57ecd9b881b66a7a12c7ae098b`; full text captured.

- **Ordinary problem:** A Japanese TTS dataset needs phonemic and prosodic labels aligned to speech, but manually adding those labels is slow and ASR text alone does not say how a phrase was pronounced.
- **Why hard:** Pronunciation and prosody are coupled to phrase boundaries and context, and an ASR transcript can contain errors that propagate into annotation.
- **Naive attempt:** Use a dictionary-only grapheme-to-phoneme process or annotate every recording by hand without exploiting the transcript already available.
- **Central move:** Condition a pretrained ASR model on the ground-truth transcript so it emits phrase-level graphemes and labels together, then use dictionary-enhanced decoding to correct phonemic labels.
- **Mechanism:** Transcript-Prompted Whisper fine-tunes a large ASR model for simultaneous phrase and annotation output and applies a dictionary-based correction stage for Japanese speech-data construction.
- **Conceptual structure:** The transcript acts as a constraint on what was said while the audio supplies pronunciation and prosody; joint sequence output makes boundaries and labels part of one decoding problem.
- **What paper reports:** The paper reports improved phonemic/prosodic annotation behavior and a practical pipeline for constructing Japanese TTS data from audio-transcript pairs.
- **Limits:** Ground-truth transcript quality, dictionary coverage, Japanese phonology, label definitions, and annotation evaluation bound the result; automatic labels still require quality control before becoming training truth.

## 8. low-resource-and-data-creation-2

**Paper:** [Transcribing Oral History Recordings Using the Transcription Portal](https://www.isca-archive.org/interspeech_2025/draxler25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `191e49f77c33f35a1dd6ed61d6e82f4a4a6b6064546fabe741942ad0ad0a7eb5`; full text captured.

- **Ordinary problem:** Archivists and communities need searchable transcripts of long oral-history recordings, but the people doing the work may not be speech engineers and the historical audio may be multilingual or difficult.
- **Why hard:** Automatic recognition is fast but imperfect, while manual correction is necessary; a fragmented toolchain makes it hard for a nontechnical user to move from audio to a trustworthy export.
- **Naive attempt:** Run a command-line ASR system and hand files between separate tools, or publish an automatic transcript without a correction path.
- **Central move:** Put recognition, human correction, and export into one preconfigured web workflow designed around the user's task rather than the model's internals.
- **Mechanism:** The Transcription Portal provides a GUI with three steps—ASR, manual correction, and data export—supports several languages, and demonstrates the workflow on historical Italian Ravensbrück interviews.
- **Conceptual structure:** The system treats human correction as part of the measurement pipeline: ASR supplies a draft, the user supplies local knowledge, and the exported transcript records the corrected artifact.
- **What paper reports:** The paper reports a usable multilingual portal and demonstrates it on oral-history recordings, with summarization and translation identified as future extensions.
- **Limits:** The demonstration corpus, user effort, ASR model, correction time, and export format bound the result; a convenient workflow does not establish transcription accuracy without an error audit or independent user study.

