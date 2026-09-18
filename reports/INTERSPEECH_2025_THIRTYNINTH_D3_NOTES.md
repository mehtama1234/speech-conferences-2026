# INTERSPEECH 2025 thirty-ninth-pass full-paper notes

Eight official-PDF readings deepen clinical phonetic selection, open-set deepfake attribution, few-shot forensic adaptation, spoken dialogue data, visual neural coding, Fongbe translation, audio-model abstention, and mono-to-binaural synthesis.

## 1. source-filter-production

**Paper:** [Phonetic Posteriorgram-Based Phoneme Selection for Vocal Cord Disorder Classification in Continuous Mandarin Speech](https://www.isca-archive.org/interspeech_2025/chen25n_interspeech.html)
**Evidence:** D3; PDF SHA-256 `728f61c6daf8cfd51d64d5f360e2ddf4c81ce1438f55a39e6d56604314fa4331`; full text captured.

- **Ordinary problem:** A screening system for vocal-cord disorders should use continuous Mandarin speech, where the diagnostic evidence is spread across many phonemes rather than one carefully chosen sound.
- **Why hard:** Some phonemes reveal laryngeal behavior more clearly than others, but selecting them from the speech signal can also make the classifier depend on speaker, text, or recording conditions.
- **Naive attempt:** Average the whole utterance or use a fixed phoneme list and assume every segment contributes equally.
- **Central move:** Use phonetic posteriorgrams to identify informative phoneme segments, then classify vocal-cord disorders from the selected evidence.
- **Mechanism:** The paper proposes phonetic-posteriorgram-based phoneme selection for vocal-cord-disorder classification in continuous Mandarin speech.
- **Conceptual structure:** The recognizer supplies a soft map from sound to phonetic identity; selection makes the diagnostic model focus on the speech units that expose the relevant production difference.
- **What paper reports:** The paper reports classification results for the selected phonetic evidence on continuous Mandarin speech.
- **Limits:** Cohort, disorder labels, language, transcript quality, phoneme selection, and recording conditions limit clinical generalization; classification is not diagnosis.

## 2. privacy-security-and-accountability

**Paper:** [STOPA: A Dataset of Systematic VariaTion Of DeePfake Audio for Open-Set Source Tracing and Attribution](https://www.isca-archive.org/interspeech_2025/firc25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `dd58fcc8c8640443823b0117bd40e7fc848574506ec17a2b32842b5f6ce3cd84`; full text captured.

- **Ordinary problem:** A deepfake detector should trace and attribute new attack sources, including attacks not represented in training, rather than only say real or fake.
- **Why hard:** Open-set attacks change synthesis methods and acoustic traces; a dataset can accidentally reward memorizing a generator or speaker instead of identifying source behavior.
- **Naive attempt:** Train a closed-set binary classifier and evaluate it only on familiar fake types.
- **Central move:** Build systematic variations of deepfake audio with source labels and evaluate open-set detection, tracing, and attribution separately.
- **Mechanism:** STOPA is a dataset of systematic variation of deepfake audio for open-set source tracing and attribution.
- **Conceptual structure:** The task is a structured forensic inference problem: detection asks whether an item is fake, while tracing asks which generating process explains it under variation.
- **What paper reports:** The paper reports dataset resources and benchmark behavior for open-set deepfake source tracing and attribution.
- **Limits:** Generator coverage, perturbations, speakers, labels, and open-set split design bound the result; benchmark attribution is not courtroom-grade provenance.

## 3. low-resource-and-data-creation

**Paper:** [Few-Shot Speech Deepfake Detection Adaptation with Gaussian Processes](https://www.isca-archive.org/interspeech_2025/glazer25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `87036d54708344c13d2df0d861254d434131a0770e5fd25ab25c3d85fd2b7027`; full text captured.

- **Ordinary problem:** A new speech deepfake attack may appear with only a few labeled examples, so detection must adapt without retraining a large model from scratch.
- **Why hard:** Few examples make neural updates unstable, while the new attack may occupy a different part of acoustic space from old attacks.
- **Naive attempt:** Fine-tune all parameters on the few examples or use a fixed detector and accept failure on the new attack.
- **Central move:** Use Gaussian-process adaptation to express uncertainty and update the detector from scarce examples.
- **Mechanism:** The paper studies few-shot adaptation for speech deepfake detection with Gaussian processes.
- **Conceptual structure:** The probabilistic adapter separates learning the new attack boundary from pretending that a few examples define it with certainty; uncertainty can guide conservative decisions.
- **What paper reports:** The paper reports few-shot detection adaptation results against the tested baselines.
- **Limits:** Attack families, kernel choices, calibration, shots, and base detector limit generalization; uncertainty estimates are not automatically reliable under distribution shift.

## 4. dialogue-and-turn-taking

**Paper:** [Leveraging LLMs for Written to Spoken Style Data Transformation to Enhance Spoken Dialog State Tracking](https://www.isca-archive.org/interspeech_2025/gulzar25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `adc9d9d9de2a318d2ae17ed99841467cfa25210f33b906fadff5b60f82cb023e`; full text captured.

- **Ordinary problem:** Spoken dialogue state tracking needs training data that sounds like spoken interaction, not only written dialogue that has been read aloud.
- **Why hard:** Written and spoken styles differ in disfluency, brevity, repair, and turn structure; an LLM rewrite can add plausible language while changing the dialogue-state labels.
- **Naive attempt:** Use written dialogue directly or generate paraphrases without checking whether the state remains unchanged.
- **Central move:** Use an LLM to transform written dialogue into spoken style while preserving state annotations, then test the resulting data for spoken dialogue-state tracking.
- **Mechanism:** The paper leverages LLMs for written-to-spoken style transformation to enhance spoken dialogue-state tracking.
- **Conceptual structure:** The transformation is constrained paraphrasing: surface form changes, but the underlying user goal and slot state must remain invariant for the data to be useful.
- **What paper reports:** The paper reports spoken dialogue-state-tracking gains from the transformed data.
- **Limits:** LLM prompt, domains, state schema, speech realization, annotation checks, and evaluation distribution limit the result; style conversion can silently change intent.

## 5. echo-and-reconstruction

**Paper:** [Vision-Integrated High-Quality Neural Speech Coding](https://www.isca-archive.org/interspeech_2025/guo25c_interspeech.html)
**Evidence:** D3; PDF SHA-256 `a8b98a3cc3f9952d5a12a6994412e43e2b7d02e71553d8e23ddf2aececc5300d`; full text captured.

- **Ordinary problem:** A neural speech codec should preserve high-quality speech while using visual information when available, and it should fail gracefully when that information is absent.
- **Why hard:** Video can disambiguate speech and improve reconstruction, but synchronization, bitrate, and privacy make it a conditional source rather than a free improvement.
- **Naive attempt:** Encode only audio at a high bitrate or concatenate video features without modeling their timing and reliability.
- **Central move:** Integrate visual cues into a high-quality neural speech coder and measure quality, rate, and behavior across audio-visual conditions.
- **Mechanism:** The paper presents a vision-integrated high-quality neural speech coding system.
- **Conceptual structure:** Coding becomes cross-modal reconstruction: the decoder uses synchronized visual evidence to fill or protect acoustic detail while the rate constraint limits what can be transmitted.
- **What paper reports:** The paper reports high-quality neural coding results for the tested audio-visual conditions.
- **Limits:** Video quality, synchronization, speakers, bitrate, decoder, and missing-video behavior bound the claim; visual assistance can introduce privacy and spoofing risks.

## 6. multilingual-and-crosslingual

**Paper:** [Extending the Fongbe to French Speech Translation Corpus:  resources, models and benchmark](https://www.isca-archive.org/interspeech_2025/kponou25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `a36e93b7290c17345c54c825534cd24f8b12c18dca2597716a30348cb92f1da9`; full text captured.

- **Ordinary problem:** Fongbe-to-French speech translation needs a benchmark and models that reflect the language rather than treating the low-resource direction as an afterthought.
- **Why hard:** Speech translation compounds transcription and translation errors, while limited speakers, orthography, and parallel data make evaluation noisy.
- **Naive attempt:** Translate a few examples with a multilingual model and compare scores without documenting the corpus or split.
- **Central move:** Extend the Fongbe-French speech-translation corpus, document resources and splits, and establish models and baselines for the direction.
- **Mechanism:** The paper extends the Fongbe-to-French speech translation corpus and presents resources, models, and a benchmark.
- **Conceptual structure:** Resource creation and modeling are one research object: a stable corpus fixes what progress means and reveals where transfer from high-resource languages fails.
- **What paper reports:** The paper reports corpus additions, baseline models, and benchmark results for Fongbe-to-French speech translation.
- **Limits:** Corpus size, speakers, alignment, transcription, translation references, and split design bound generalization to Fongbe communities and other low-resource pairs.

## 7. grounding-and-action

**Paper:** [Teaching Audio-Aware Large Language Models What Does Not Hear: Mitigating Hallucinations through Synthesized Negative Samples](https://www.isca-archive.org/interspeech_2025/kuan25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `5a0ba8d790ffdaf6628bafeb0eeb1a0ad8dbb73d8dd1bc07a7be49b94ef20144`; full text captured.

- **Ordinary problem:** An audio-aware language model should say when spoken input does not contain enough evidence instead of confidently inventing what it did not hear.
- **Why hard:** Hallucinations can arise from the language model's prior or from ambiguous/noisy audio; ordinary positive examples do not teach the model when to abstain.
- **Naive attempt:** Train only on correct audio-text pairs or add generic negative text and assume the model learns auditory limits.
- **Central move:** Synthesize negative samples that explicitly represent what the audio does not contain and train the model to distinguish heard evidence from plausible language completion.
- **Mechanism:** The paper teaches audio-aware large language models what they do not hear through synthesized negative samples.
- **Conceptual structure:** The negative examples define an evidence boundary: language generation is rewarded only when its claim is supported by the acoustic input, not merely likely in context.
- **What paper reports:** The paper reports reduced hallucination behavior for the tested audio-aware models and synthesized negative-sample strategy.
- **Limits:** Negative-sample construction, audio quality, prompts, model family, and evaluation rubric limit the claim; abstention quality is not the same as factual clinical reliability.

## 8. prosody-and-interactive-control

**Paper:** [Zero-Shot Mono-to-Binaural Speech Synthesis](https://www.isca-archive.org/interspeech_2025/levkovitch25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `530d6e4c5dd930880030a7cd4ddbfb3581369852356e70f0b5304338c9e7862e`; full text captured.

- **Ordinary problem:** A monaural speech synthesizer should produce a binaural signal with believable spatial cues even when it has never seen a paired example for the target speaker.
- **Why hard:** Binaural cues depend on source position, room, head-related filtering, and speaker content; zero-shot synthesis must infer them without memorizing a fixed room or voice.
- **Naive attempt:** Duplicate mono audio into both channels or apply one generic stereo widening effect.
- **Central move:** Condition zero-shot speech synthesis on spatial information and generate the two channels with consistent content and interaural cues.
- **Mechanism:** The paper studies zero-shot mono-to-binaural speech synthesis.
- **Conceptual structure:** Spatialization is a structured transformation: linguistic content should remain common across channels while timing and spectral differences encode position and acoustic scene.
- **What paper reports:** The paper reports objective and perceptual results for zero-shot mono-to-binaural synthesis.
- **Limits:** Room and position range, speaker diversity, spatial labels, head-related filtering, and listening protocol bound generalization; stereo plausibility is not physical localization accuracy.

