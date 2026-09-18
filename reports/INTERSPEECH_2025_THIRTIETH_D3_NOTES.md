# INTERSPEECH 2025 thirtieth-pass full-paper notes

Eight official-PDF readings deepen low-resource data creation, controllable generation, vocal effort, spatial listening, multimodal meeting recognition, codecs, privacy, and open measurement. Results remain author-reported and were not independently reproduced.

## 1. low-resource-and-data-creation

**Paper:** [Speechless: Speech Instruction Training Without Speech for Low Resource Languages](https://www.isca-archive.org/interspeech_2025/dao25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `4c081f92f821e684db02d1d96bd2435c1f07cf2fc0418883f6f01669e2343eea`; full text captured.

- **Ordinary problem:** A voice assistant needs spoken command examples in a low-resource language, but there may be no good text-to-speech system with which to synthesize them.
- **Why hard:** Text instructions and spoken instructions share meaning but not the same signal, so training only on text risks losing the acoustic path needed at inference time.
- **Naive attempt:** Translate text instructions into speech with a weak TTS system, or fine-tune only on written commands and hope the speech encoder bridges the gap.
- **Central move:** Generate synthetic instruction examples only up to a semantic representation, align those representations with a pretrained speech encoder, and train the language model without waveform synthesis.
- **Mechanism:** Speechless uses text-generated instructions, aligns their semantic representations with Whisper encoder representations, and fine-tunes an LLM so it can process spoken commands in low-resource settings.
- **Conceptual structure:** The method removes the unavailable waveform generator from the training loop while retaining a shared semantic space; alignment is the bridge between written supervision and spoken input.
- **What paper reports:** The paper reports that speech-instruction training without TTS can preserve spoken-instruction understanding and offers a simpler route for low-resource languages.
- **Limits:** The language, synthetic text, Whisper encoder, alignment quality, and downstream command tasks bound the result; semantic alignment is not proof that pronunciation, prosody, or real user speech are fully represented.

## 2. prosody-and-interactive-control

**Paper:** [Differentiable Reward Optimization for LLM based TTS system](https://www.isca-archive.org/interspeech_2025/gao25d_interspeech.html)
**Evidence:** D3; PDF SHA-256 `73869cc8f1893064e786fa76ed8a8c89f7b24246fc5a5cd677315f41aa2ebf00`; full text captured.

- **Ordinary problem:** A speech generator should obey requests about pronunciation, emotion, age, gender, or quality, but judging every generated waveform during training is expensive and listener preferences are hard to turn into a differentiable signal.
- **Why hard:** Codec language models generate discrete tokens that later become audio through a flow model and vocoder, so an audio-level reward creates a costly feedback loop and may not distinguish competing outputs.
- **Naive attempt:** Use ordinary reinforcement learning with rewards computed after full waveform synthesis, or optimize only next-token likelihood.
- **Central move:** Predict several task rewards directly from codec tokens and make the reward path differentiable with Gumbel-Softmax, allowing direct back-propagation into the token language model.
- **Mechanism:** DiffRO predicts rewards for ASR, emotion, speech quality, age, and gender from generated codec tokens; a multi-task reward model supplies the signal and the language model is optimized without the full reinforcement-learning loop.
- **Conceptual structure:** The method replaces a sampled discrete choice with a soft probability over codebook entries during training, so reward gradients can reach token probabilities; the reward is a proxy whose meaning depends on each downstream predictor.
- **What paper reports:** The paper reports improved pronunciation accuracy and state-of-the-art WER results, with controllability experiments for emotion, MOS, age, and gender; codec-level MOS and re-encoded audio reveal disagreement between proxy and waveform quality.
- **Limits:** Reward-model accuracy, codec reconstruction, vocoder behavior, sampling, and listener perception bound the result; a differentiable proxy is not the same as human preference or end-to-end quality.

## 3. prosody-and-interactive-control-2

**Paper:** [In This Environment, As That Speaker: A Text-Driven Framework for Multi-Attribute Speech Conversion](https://www.isca-archive.org/interspeech_2025/jin25d_interspeech.html)
**Evidence:** D3; PDF SHA-256 `8544a0f7a03420856b7ab045805f0bfe2917d5651af545911ef1f651e8ce8924`; full text captured.

- **Ordinary problem:** A user may want the same words spoken by a different person in a different environment, such as a voice heard through a hallway or in a car, while keeping the source message unchanged.
- **Why hard:** Speaker timbre and environmental acoustics both change the waveform and can interfere with one another, especially when paired examples for every combination do not exist.
- **Naive attempt:** Train one entangled converter and describe the target only with a speaker recording, or apply room filtering after voice conversion as an independent afterthought.
- **Central move:** Represent target speaker and environment as separate text-controlled attributes, then retrieve timbre evidence and generate the combined result with a latent diffusion converter.
- **Mechanism:** TES-VC uses synthetic data with decoupled vocal/environment features, a retrieval-based timbre-control module, and text descriptions for both target timbre and acoustic environment.
- **Conceptual structure:** The desired output is a composition of content, speaker, and room factors; independent controls are tested by changing one description while holding the others fixed and measuring content retention and controllability.
- **What paper reports:** The paper reports effective text-driven control of timbre and environment with high content retention and results on in-domain and out-of-domain conditions.
- **Limits:** Synthetic training mixtures, text descriptions, diffusion sampling, evaluation speakers and rooms, and the notion of controllability bound the result; independent factors are operational test dimensions, not guaranteed physical causes.

## 4. room-channel-and-sensing

**Paper:** [L3C-DeepMFC: Low-Latency Low-Complexity Deep Marginal Feedback Cancellation with Closed-Loop Fine Tuning for Hearing Aids](https://www.isca-archive.org/interspeech_2025/hao25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `cbd7d515b58ab585fdc4b304620743324d09c128a8b1a43eda22933d45cd4f3f`; full text captured.

- **Ordinary problem:** A hearing aid must amplify speech without feeding the receiver's sound back into its microphone, and it must do so with little delay and little computation.
- **Why hard:** The acoustic coupling changes over time, while suppressing feedback can also suppress speech; full-band neural processing may be too slow or expensive for a wearable device.
- **Naive attempt:** Use a fixed notch filter or a large neural model that estimates the entire waveform with no explicit latency or complexity constraint.
- **Central move:** Estimate the desired speech's complex spectrum in time-frequency bands and adapt the feedback canceller with closed-loop fine tuning while keeping the model small.
- **Mechanism:** L3C-DeepMFC uses complex spectrum mapping, full- and sub-band recurrent components, and closed-loop fine tuning for marginal feedback cancellation; evaluation varies feedback paths and reports latency, complexity, and speech quality.
- **Conceptual structure:** The complex spectrum keeps magnitude and phase, while a closed loop uses the residual error created by the receiver-microphone path to update cancellation; the system is judged on both suppression and preserved speech.
- **What paper reports:** The paper reports low-latency, low-complexity feedback cancellation with improved speech quality relative to its baselines under tested hearing-aid conditions.
- **Limits:** Feedback paths, delay budget, hardware assumptions, noise, and quality metrics bound the result; lab cancellation performance is not the same as clinical benefit for every listener.

## 5. boundaries-and-sequence-structure

**Paper:** [Bidirectional Spoken-Written Text Conversion with Large Language Models](https://www.isca-archive.org/interspeech_2025/choi25g_interspeech.html)
**Evidence:** D3; PDF SHA-256 `46dd7b70401166c9f07ac62da465afe83ce6da56447d82869ce7282efbbd152f`; full text captured.

- **Ordinary problem:** Speech recognition may correctly hear a sentence but write it in a form different from what a downstream application expects: numbers, punctuation, abbreviations, and spoken forms can all encode the same meaning.
- **Why hard:** Most speech databases provide only one transcription convention, so a recognizer cannot learn when to preserve spoken wording and when to normalize into written wording without expensive paired labels.
- **Naive attempt:** Normalize every transcript with hand-written rules, or train a recognizer on whichever form appears most often and treat the other form as an error.
- **Central move:** Create paired spoken/written text with an LLM, expand it through iterative supervised and semi-supervised learning, and use one bidirectional model for both text-normalization directions.
- **Mechanism:** The BTC model maps spoken to written form and written to spoken form; generated dual transcripts supply training pairs and the model is evaluated on text-conversion quality alongside recognition behavior.
- **Conceptual structure:** The central object is not a new sound representation but a boundary convention: the same recognized content is rewritten under a task-specific output contract, so conversion errors are distinct from acoustic errors.
- **What paper reports:** The paper reports improved bidirectional text conversion and shows that automatically generated dual transcription data can reduce the cost of constructing paired resources.
- **Limits:** LLM-generated text quality, language conventions, iterative filtering, and conversion metrics bound the claim; written-form accuracy does not establish that the underlying ASR heard the speech correctly.

## 6. text-to-speech-and-content

**Paper:** [DS-Codec: Dual-Stage Training with Mirror-to-NonMirror Architecture Switching for Speech Codec](https://www.isca-archive.org/interspeech_2025/chen25p_interspeech.html)
**Evidence:** D3; PDF SHA-256 `3db722e74038c95e08fd2ad0b29ab832bcf8323822e34078ec593e66105ee712`; full text captured.

- **Ordinary problem:** A speech codec must turn a waveform into a short discrete sequence and reconstruct speech that still sounds and works like the original; using several codebooks adds rate and system complexity.
- **Why hard:** A single codebook must carry both coarse linguistic structure and fine acoustic detail, while encoder and decoder capacity can become unbalanced during training.
- **Naive attempt:** Use residual codebooks with more tokens, or train a mirror-shaped encoder and decoder throughout even when the decoder needs greater capacity.
- **Central move:** Train in two stages: first use a mirror architecture to stabilize the codebook, then switch to a stronger non-mirror decoder while preserving the learned quantizer.
- **Mechanism:** DS-Codec uses vector and product quantization with one 8,192-entry codebook, a downsampling encoder, recurrent/transformer decoder components, and time/frequency discriminators; ablations compare mirror and non-mirror stages.
- **Conceptual structure:** Quantization maps a continuous latent vector to a nearby code; the staged architecture changes which parameters are allowed to adapt after the codebook has learned a stable partition, while reconstruction and perceptual metrics test the recovered waveform.
- **What paper reports:** The paper reports that mirror-stage training outperforms APCodec+ and the non-mirror alternatives on its objective measures, with lower reconstruction error and fewer training epochs/cost.
- **Limits:** The speech data, bitrate/downsampling setting, discriminators, metrics, and baselines bound the result; reconstruction quality does not by itself prove usefulness for every TTS or speech-language-model task.

## 7. voice-identity-and-conversion

**Paper:** [Neurodyne: Neural Pitch Manipulation with Representation Learning and Cycle-Consistency GAN](https://www.isca-archive.org/interspeech_2025/gu25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `6d62e93261c7572c75ec3f1fab2601ab0b3b3de7267c0506694a442e79298f3b`; full text captured.

- **Ordinary problem:** A singer or speaker may need the same recorded phrase moved to a new pitch while retaining its timing, timbre, and natural vocal quality.
- **Why hard:** Pitch, vocal-tract resonances, and source characteristics are entangled in the waveform, and paired examples at every original and target pitch are scarce.
- **Naive attempt:** Shift the waveform with a fixed signal-processing rule or train a supervised mapper that requires matched in-tune and out-of-tune examples.
- **Central move:** Learn a pitch representation and use cycle consistency so a converter can move pitch and return it without losing the source information, even without paired training examples.
- **Mechanism:** Neurodyne uses representation learning and a cycle-consistency GAN to manipulate pitch; pitch and non-pitch features are separated through learned representations and evaluated on singing-voice conversion behavior.
- **Conceptual structure:** Cycle consistency supplies a testable conservation rule: converting to a target pitch and back should recover the original, while the pitch representation controls the intended change.
- **What paper reports:** The paper reports improved pitch manipulation and synthesis quality over classical and neural comparisons under its singing-voice experiments.
- **Limits:** Training voices, pitch range, unpaired-data assumptions, cycle losses, and musical evaluation bound the claim; a successful pitch change does not establish general speaker/style disentanglement.

## 8. low-resource-and-data-creation-2

**Paper:** [Nosey: Open-Source Hardware for Acoustic Nasalance](https://www.isca-archive.org/interspeech_2025/dewhurst25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `539819ea64ce289148e7a69d77df8f9a3c88edec254a65b51fc3a8cf9ea94307`; full text captured.

- **Ordinary problem:** Researchers and clinicians need to measure how much sound escapes through the nose, but commercial nasometers are expensive and hard to customize, limiting data collection across communities.
- **Why hard:** Nasalance is a ratio of nasal to total acoustic energy, so microphone placement, cross-signal bleed, baffle shape, and speaker anatomy can change the number even when the speech is comparable.
- **Naive attempt:** Infer nasality from a spectrum alone or treat a cheap two-microphone device as interchangeable with a commercial instrument without calibration.
- **Central move:** Build open hardware whose microphone, baffle, and analog path can be changed, then compare raw scores and phonological contrasts against a commercial device.
- **Mechanism:** Nosey is a 3-D-printable baffle with replaceable dual microphone clips and open files; the study compares it with an icSpeech device for speakers and phonological environments.
- **Conceptual structure:** Nasalance is computed as nasal energy divided by nasal plus oral energy; the important test is whether oral/nasal contrasts and their variation are preserved, not whether raw percentages match exactly.
- **What paper reports:** Nosey produces consistently higher raw nasalance scores, but preserves comparable phonological-environment contrasts under the tested conditions and offers a lower-cost customizable platform.
- **Limits:** The tested speakers, microphones, baffle geometry, placement, and phonological materials bound the comparison; raw-score offsets and cross-signal bleed prevent treating Nosey and commercial values as directly interchangeable.

