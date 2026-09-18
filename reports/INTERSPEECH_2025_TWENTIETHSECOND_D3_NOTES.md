# INTERSPEECH 2025 twenty-second-pass full-paper notes

Eight official-PDF readings deepen deployment, adaptation, evaluation, and assistive branches. Results are author-reported and not independently reproduced.

## 1. room-channel-and-sensing

**Paper:** [On the Language and Gender Biases in PSTN, VoIP and Neural Audio Codecs](https://www.isca-archive.org/interspeech_2025/altwlkany25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `76ca03f71b1e2a15e7e4286d244f565c3aa65eff9a25a88cf5790da027d410e5`; full text captured.

- **Ordinary problem:** A speech system should not degrade one language or gender more than another when audio passes through a codec.
- **Why hard:** Transcoding changes the signal before recognition or sentiment analysis, and the codec may interact with language and vocal characteristics.
- **Naive attempt:** Treat a codec as a neutral pipe and measure only average speech quality.
- **Central move:** Transcode millions of multilingual files through PSTN, VoIP, and neural codecs, then compare quality by language and gender.
- **Mechanism:** The study measures speech quality after representative codec paths across more than two million multilingual files.
- **Conceptual structure:** The target is a distribution of quality differences, not one overall mean; grouping by language and gender exposes unequal channel loss.
- **What paper reports:** PSTN codecs show strong gender bias and neural codecs introduce language bias in the reported analysis.
- **Limits:** Codec set, languages, gender labels, quality measure, and files define the boundary; causal mechanisms and mitigation in deployed networks remain open.

## 2. source-separation-and-spatial-listening

**Paper:** [MOPSA: Mixture of Prompt-Experts Based Speaker Adaptation for Elderly Speech Recognition](https://www.isca-archive.org/interspeech_2025/deng25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `89e2c4e3c8a917b92628e441d6648013c416f755dbf87d0f1c071dda90da3462`; full text captured.

- **Ordinary problem:** An ASR system should adapt online to an elderly speaker it has not seen, without stopping for a large offline retraining job.
- **Why hard:** Elderly speakers vary acoustically and linguistically, and one prompt that helps one speaker can hurt another.
- **Naive attempt:** Use one speaker-independent model or fine-tune a separate model per speaker.
- **Central move:** Cluster speaker prompts into experts and let a router mix acoustic and language prompts for the new speaker at run time.
- **Mechanism:** MOPSA uses K-means speaker prompt clusters and a router around Whisper, with separate acoustic and language-level prompts, tested on English and Cantonese elderly speech.
- **Conceptual structure:** The router is a mixture-of-experts choice; WER/CER measure recognition and real-time factor measures adaptation cost.
- **What paper reports:** The paper reports relative WER/CER reductions of 4.21% and 5.40% and up to 16.12x real-time speedup over offline adaptation.
- **Limits:** Datasets, elderly populations, prompt clusters, and Whisper versions bound the claim; broader disorders, languages, and online failure recovery remain open.

## 3. speaker-characteristics

**Paper:** [A Copula-Based Generative Score-Level Fusion Model for Speaker Verification](https://www.isca-archive.org/interspeech_2025/cumani25b_interspeech.html)
**Evidence:** D3; PDF SHA-256 `8c16fb26acda8cb626c73788551889bd9a9ef57acd05fa974a5ec77da042d910`; full text captured.

- **Ordinary problem:** A speaker verifier should combine several recognizers while producing scores that mean the same thing across operating thresholds.
- **Why hard:** Different recognizers make dependent errors and their scores have different scales, so adding scores can miscalibrate decisions.
- **Naive attempt:** Use a weighted linear score sum and tune it on one development set.
- **Central move:** Model the joint score distribution with flexible marginals and a copula that captures dependency, then fuse and calibrate scores.
- **Mechanism:** Variance-Gamma marginals describe each recognizer's score distribution and a Gaussian copula describes dependence for target and non-target trials.
- **Conceptual structure:** The copula separates marginal shape from dependency; Cllr measures calibration and discrimination of verification scores.
- **What paper reports:** On NIST SRE 2019 and SITW, the method reports up to 7% relative Cllr reduction versus discriminative linear fusion.
- **Limits:** Datasets, recognizer diversity, score distributions, and calibration protocol bound the result; new speakers, channels, and attacks need separate evaluation.

## 4. metrics-and-targets

**Paper:** [Benchmarking Time-localized Explanations for Audio Classification Models](https://www.isca-archive.org/interspeech_2025/bolanos25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `c5cd9eca43512c992793f379177678d8b237be6d64e6c311fb619136d7e72806`; full text captured.

- **Ordinary problem:** A listener should be able to see which moments of an audio clip drove a classifier, especially when the model may be using a spurious sound.
- **Why hard:** There is usually no ground-truth explanation, so explanation methods can look plausible while pointing to the wrong time region.
- **Naive attempt:** Trust a saliency plot or compare explanations by visual appeal.
- **Central move:** Create time annotations for target events as a proxy reference and benchmark model-agnostic post-hoc explanations against them.
- **Mechanism:** The benchmark compares temporal explanation methods for audio classifiers and uses the annotations to expose spurious correlations.
- **Conceptual structure:** Time-localized overlap turns an explanation into a measurable alignment problem; the proxy is useful but is not a causal proof of model reasoning.
- **What paper reports:** The paper reports near-perfect explanations for some methods and shows their use in finding spurious correlations.
- **Limits:** Event annotations, task type, explanation method, and proxy definition bound the claim; faithfulness under distribution shift remains open.

## 5. multilingual-and-crosslingual

**Paper:** [Speech-to-Text Translation with Phoneme-Augmented CoT: Enhancing Cross-Lingual Transfer in Low-Resource Scenarios](https://www.isca-archive.org/interspeech_2025/gallego25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `48ccc4729e0124e631b56d67f5f1ea13a678396ff2c1239565757bc6089ef1a3`; full text captured.

- **Ordinary problem:** A translation system should translate speech into text for languages with little or no labeled speech data.
- **Why hard:** Sound-to-meaning transfer crosses languages and modalities, while phonetic evidence is easier to share than complete translated speech examples.
- **Naive attempt:** Train a large speech-to-text translator only on languages with parallel speech and translation labels.
- **Central move:** Insert phoneme recognition and phoneme-aware chain-of-thought steps, then gradually shift training from text support toward speech.
- **Mechanism:** A multilingual LLM processes speech and phonemes under a curriculum; multilingual benchmarks compare low-, zero-, and high-resource settings.
- **Conceptual structure:** Phonemes form an intermediate representation that can transfer sound structure across languages, while translation quality measures the final meaning transfer.
- **What paper reports:** The paper reports improved low-resource translation and zero-resource operation, with a small high-resource tradeoff.
- **Limits:** Languages, phoneme recognizer, curriculum, and benchmark define the boundary; zero-resource claims depend on what other language information is available.

## 6. clinical-and-assistive-speech

**Paper:** [EEG-based Voice Conversion : Hearing the Voice of Your Brain](https://www.isca-archive.org/interspeech_2025/geng25b_interspeech.html)
**Evidence:** D3; PDF SHA-256 `f924192893764c3172ebff54cdcadd818d34616ca7c581274b0236b43f577479`; full text captured.

- **Ordinary problem:** A person who cannot speak reliably may need a system that turns brain activity into a chosen voice without collecting data from the target speaker first.
- **Why hard:** EEG is noisy and indirect, while voice identity is highly speaker-specific; conversion must align these signals without target examples.
- **Naive attempt:** Train a voice converter only from speech or require target-speaker recordings before conversion.
- **Central move:** Align EEG features with speaker voice features and use a speech-trained zero-shot voice-conversion model.
- **Mechanism:** A three-stage training strategy maps EEG to speaker-specific features and conditions a pretrained speech-only converter; Dutch single-word production tests the system.
- **Conceptual structure:** The alignment is a cross-modal mapping problem; zero-shot evaluation tests whether target identity can be supplied without target speech data.
- **What paper reports:** The paper reports reliable target-voice conversion on the Single-Word-Production Dutch-iBIDS dataset.
- **Limits:** Single words, EEG setup, target voices, and small dataset define the claim; intelligibility, privacy, consent, and real assistive communication remain open.

## 7. prosody-and-interactive-control

**Paper:** [SOVA-Bench: Benchmarking the Speech Conversation Ability for LLM-based Voice Assistant](https://www.isca-archive.org/interspeech_2025/hou25b_interspeech.html)
**Evidence:** D3; PDF SHA-256 `4c27c0d1559ac0e4ea6fb7815f33c7ff95930f3f9b74ea86bf7e8bcb9e4929d7`; full text captured.

- **Ordinary problem:** A voice assistant should be judged not only by whether it understood a request but also by whether its spoken response sounds natural and conversational.
- **Why hard:** Semantic accuracy can hide stiff timing, poor prosody, or unpleasant acoustic quality, and existing tests emphasize understanding.
- **Naive attempt:** Score a voice assistant with text-task accuracy alone.
- **Central move:** Build a benchmark that tests general knowledge, speech recognition/understanding, semantic generation, and acoustic generation together.
- **Mechanism:** SOVA-Bench compares speech LLMs across comprehension and generated-speech dimensions, making acoustic quality an explicit evaluation target.
- **Conceptual structure:** The benchmark separates what the assistant knows, what it understood, and how it sounded; no single score can substitute for those dimensions.
- **What paper reports:** The paper presents a systematic evaluation framework intended to guide speech-LLM voice interaction.
- **Limits:** Benchmark tasks, prompts, listeners, model versions, and acoustic measures define the comparison; long-term interaction quality and user adaptation remain open.

## 8. text-to-speech-and-content

**Paper:** [Scheduled Interleaved Speech-Text Training for Speech-to-Speech Translation with LLMs](https://www.isca-archive.org/interspeech_2025/futami25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `26eb613db71dd3656f2fb2b600aca0598348727e5f8ace5573099a69c1518587`; full text captured.

- **Ordinary problem:** A speech-to-speech translator should inherit text-trained language knowledge without needing a huge paired speech-to-speech corpus.
- **Why hard:** Text-only LLMs know language patterns but not how discrete speech units carry them, and limited paired data makes direct adaptation unstable.
- **Naive attempt:** Fine-tune directly on speech units and expect the text model to discover the modality bridge.
- **Central move:** Interleave aligned text and speech units during training, then gradually reduce the text proportion so the model moves toward speech output.
- **Mechanism:** LLaMA3.2-1B is fine-tuned on CVSS with scheduled interleaving and evaluated across translation directions and resource levels.
- **Conceptual structure:** The schedule is a curriculum over modalities: text provides a stable scaffold early, while speech units become responsible later; translation quality measures the endpoint.
- **What paper reports:** The paper reports consistent translation improvements, especially in limited-data languages.
- **Limits:** CVSS, unitizer, schedule, model size, and languages bound the result; naturalness, speaker identity, and unseen domains need separate tests.

