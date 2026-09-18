# INTERSPEECH 2025 second-pass full-paper notes

These eight additional notes extend the D3 sample to two papers per initial theme. They are based on captured official PDFs and remain paper-reported, not independently reproduced.

## 1. signal_and_acoustics

**Paper:** [Analysis of Semantic and Acoustic Token Variability Across Speech, Music, and Audio Domains](https://www.isca-archive.org/interspeech_2025/ashihara25_interspeech.html)  
**Evidence:** D3; PDF SHA-256 `6ddf7d958ffbd346680c98f621eaa0099d8c90928357236537c9cbcf109fa701`; 5 pages.

- **Big picture:** Understand what discrete audio tokens preserve when speech, music, and general audio are represented for language models.
- **Why hard:** Tokens can be statistically predictable while still using different codewords across domains, so one universal token vocabulary may hide domain structure.
- **Naive attempt:** Assume a token representation has the same behavior in speech, music, and sound because the encoding format is shared.
- **Central move:** Compare acoustic codec tokens and semantic speech tokens across domains using rank-frequency distributions, perplexity, and token usage patterns.
- **Mechanism:** The study measures statistical structure and predictability of token sequences, then compares domain-specific codeword usage.
- **Mathematical idea:** Rank-frequency distributions describe how often codes occur; perplexity measures uncertainty of the next token. Similar predictability does not imply identical meaning.
- **Connections:** Connects physical audio representation to audio-language-model design and modality bridging.
- **What paper reports:** The paper reports similar statistical/predictable sequence patterns across domains but domain-dependent token usage.
- **Limits:** The analysis supports representation observations, not a universal optimal token design or downstream task improvement.

## 2. recognition_and_transcription

**Paper:** [Spot and Merge: A Hybrid Context Biasing Approach for Rare Word and Out of Vocabulary Recognition](https://www.isca-archive.org/interspeech_2025/agrawal25b_interspeech.html)  
**Evidence:** D3; PDF SHA-256 `84106aa02c63bb5eb30400ffc26ad417253274408fe172b7d514b45ea2fe40c6`; 5 pages.

- **Big picture:** Recognize rare business words and out-of-vocabulary terms in contact-center ASR.
- **Why hard:** Large biasing lists and unseen token sequences make contextual recognition difficult, especially when full ASR retraining is impractical.
- **Naive attempt:** Use shallow fusion or fully retrain a biasing module, sacrificing either internal context use or deployment flexibility.
- **Central move:** Use LoRA adaptation and a spot-and-merge method that detects bias phrases in cross-attention and merges them with ASR output.
- **Mechanism:** Attention weights identify likely bias phrases; the method combines those candidates with the base transcription and uses an auxiliary attention loss.
- **Mathematical idea:** WER measures word errors; OOV F1 measures detection of unseen terms. LoRA changes a small parameter subset rather than the whole recognizer.
- **Connections:** Shows how deployment vocabulary and domain context alter what ‘recognition accuracy’ means.
- **What paper reports:** The paper reports a 1.0% absolute WER reduction on LibriSpeech and improved OOV recognition on in-house contact-center data.
- **Limits:** The in-house data are not independently available in this atlas, and future multilingual/low-resource extension remains open.

## 3. understanding_and_translation

**Paper:** [Spoken Language Understanding on Unseen Tasks With In-Context Learning](https://www.isca-archive.org/interspeech_2025/agrawal25_interspeech.html)  
**Evidence:** D3; PDF SHA-256 `e1b0ce18d9d00ca22245e6a421a4177d2b9673c34cd8191ebb8ca5280d681eb1`; 5 pages.

- **Big picture:** Make a speech-text LLM perform spoken-language-understanding tasks it did not see during task-specific training.
- **Why hard:** Cascaded ASR plus text understanding compounds errors, while task-specific SLU labels are expensive and unseen label sets break ordinary fine-tuning.
- **Naive attempt:** Fine-tune directly on task labels and assume the same labels will exist at evaluation time.
- **Central move:** Use symbol-based and randomized-label fine-tuning with a SALMONN speech-text model to reduce dependence on task-specific label semantics.
- **Mechanism:** The model maps speech and demonstrations to symbolic targets, then is evaluated in matched and mismatched task settings with zero/few-shot context.
- **Mathematical idea:** The central object is a label permutation: performance tests whether the model learned task structure rather than memorized label names.
- **Connections:** Connects speech semantics, in-context learning, task transfer, and the limits of ‘emergent’ ability claims.
- **What paper reports:** The paper reports improved unseen-task performance over standard approaches in its three-task evaluation.
- **Limits:** Fine-tuning used batch size one and the task/model/data setup is narrower than general spoken reasoning.

## 4. generation_and_voice

**Paper:** [Voice Conversion Improves Cross-Domain Robustness  for Spoken Arabic Dialect Identification](https://www.isca-archive.org/interspeech_2025/abdullah25_interspeech.html)  
**Evidence:** D3; PDF SHA-256 `1a900281aa9a8d251c21d3efbae0d648fecec923df8146287e0bdf38e39174f5`; 5 pages.

- **Big picture:** Improve Arabic dialect identification when test speech comes from a different domain or speaker population.
- **Why hard:** Dialect classifiers can exploit speaker-specific shortcuts instead of dialect evidence, causing cross-domain failure.
- **Naive attempt:** Train a classifier on available dialect data and treat in-domain accuracy as evidence of dialect robustness.
- **Central move:** Use voice conversion as augmentation to reduce speaker bias, then evaluate on a newly collected real-world cross-domain set.
- **Mechanism:** Converted speech changes speaker characteristics while preserving dialect-related content; controlled experiments compare conversion with ordinary augmentation.
- **Mathematical idea:** Cross-domain accuracy measures transfer rather than memorization; the causal explanation about speaker bias is supported by the paper’s controlled analysis but not independently verified here.
- **Connections:** Links generation to inclusive language technology and the danger of social or speaker shortcuts.
- **What paper reports:** The paper reports up to +34.07% cross-domain accuracy improvement and releases a model and evaluation dataset.
- **Limits:** The result is specific to Arabic dialect identification and the released artifacts require separate access and execution checks.

## 5. separation_and_enhancement

**Paper:** [A Three-Stage Beamforming with Harmonic Guidance for Multi-Channel Speech Enhancement](https://www.isca-archive.org/interspeech_2025/alip25_interspeech.html)  
**Evidence:** D3; PDF SHA-256 `ec994a3b983b6cc72158e4653ae409ec1c4a89bd2c8e37fd761e54d6b16d83d1`; 5 pages.

- **Big picture:** Enhance multi-channel speech in low-SNR conditions by learning both spatial and spectral structure.
- **Why hard:** Traditional staged systems can separate spatial filtering from speech spectral structure, losing interactions that matter when noise is strong.
- **Naive attempt:** Estimate masks and beamforming weights in separate stages without explicitly modeling speech structure.
- **Central move:** Use a three-stage framework: acoustic structure extraction, coarse full-band noise reduction, and spectral refinement.
- **Mechanism:** Noisy multi-channel inputs produce speech-structure features that interact with spatial cues before later refinement stages.
- **Mathematical idea:** Beamforming combines channels using spatial information; spectral refinement operates over frequency patterns. The design targets the joint spatial-spectral tradeoff.
- **Connections:** Connects learned enhancement to classical beamforming and low-SNR deployment constraints.
- **What paper reports:** The paper reports improvements over a reference method on LibriSpeech-based datasets.
- **Limits:** The evidence is benchmark-bound and the summary does not establish performance in arbitrary rooms, languages, or devices.

## 6. speaker_and_paralinguistics

**Paper:** [WhisperD: Dementia Speech Recognition and Filler Word Detection with Whisper](https://www.isca-archive.org/interspeech_2025/akinrintoyo25_interspeech.html)  
**Evidence:** D3; PDF SHA-256 `e0408484dc96cb89766940fa37f08781aaacb45af7a2809baa563059091d76b5`; 5 pages.

- **Big picture:** Transcribe dementia speech while retaining filler words that may matter for clinical analysis and supportive interaction.
- **Why hard:** Dementia speech includes pauses, repetitions, fragmented sentences, and unclear words unlike the standard speech used to train Whisper.
- **Naive attempt:** Apply an off-the-shelf ASR model and discard fillers as noise.
- **Central move:** Fine-tune Whisper on DementiaBank and an in-house dataset, explicitly evaluating filler inclusion and F1 as well as WER.
- **Mechanism:** Shorter training clips adapt the model to fragmented speech; transcripts are scored for word errors and filler detection.
- **Mathematical idea:** WER measures transcription errors while FIR/F1 measure whether clinically relevant fillers are retained and detected.
- **Connections:** Shows that paralinguistic/disfluency detail can be part of the target rather than an error to remove.
- **What paper reports:** The paper reports a medium model WER of 0.24 and stronger results than off-the-shelf models in its evaluation.
- **Limits:** The dataset is 11.39 hours, some audio is mumbled or unintelligible, and diagnostic or clinical benefit is not established by ASR scores alone.

## 7. languages_and_people

**Paper:** [Adapting Whisper for low-resource Hindi-English Code-Mix speech with on-the-fly Augmentation & LLM-Synthesised Data](https://www.isca-archive.org/interspeech_2025/biswas25_interspeech.html)  
**Evidence:** D3; PDF SHA-256 `7d78135bd1d5c1ef9773a24d9aa2e0652a44ad4f08c42f02f8787002da57d4a1`; 5 pages.

- **Big picture:** Adapt Whisper to Hindi-English code-mixed speech with limited labeled data.
- **Why hard:** Language switching creates acoustic and language confusion, while low-resource Indic settings lack enough in-domain examples.
- **Naive attempt:** Fine-tune a pretrained recognizer only on scarce original code-mixed data.
- **Central move:** Combine language-specific prompts, on-the-fly code-mixed augmentation, and LLM-generated text followed by audio synthesis.
- **Mechanism:** Synthetic switches and language prompts expose the recognizer to transition patterns; MER and code-switch bigram accuracy evaluate transcription.
- **Mathematical idea:** MER measures mixed-language word errors and CBA focuses on correctly recognized bigrams at switch points.
- **Connections:** Connects multilingual variation, synthetic data, and whether generated examples preserve the hard parts of switching.
- **What paper reports:** The paper reports a 31% relative improvement over pretrained Whisper without real in-domain data for fine-tuning.
- **Limits:** The experiments focus on Hindi-English tutorial speech and Whisper large-v2; transfer to other language pairs is proposed, not established.

## 8. evaluation_and_deployment

**Paper:** [Evaluating Speech Enhancement Performance Across Demographics and Language](https://www.isca-archive.org/interspeech_2025/giraldo25_interspeech.html)  
**Evidence:** D3; PDF SHA-256 `45ffdef7daac6c3edcfb326d0151655642c78d96afe1ef16bc74d8b1c2c414a3`; 5 pages.

- **Big picture:** Test whether speech-enhancement rankings survive demographic, language, and realistic data variation.
- **Why hard:** VoiceBank-DEMAND is small, young, mostly English, and simulated; a model can score well there while damaging speech for other populations.
- **Naive attempt:** Use one simplified benchmark and optimize a signal-quality metric as though it fully represents intelligibility.
- **Central move:** Evaluate enhancement systems on multilingual crowdsourced CommonPhone data with age, gender, language, content-retention, and information-loss analyses.
- **Mechanism:** Quality, intelligibility, word error, and phoneme error measures are compared across demographic and language conditions; samples with high WER are examined for information loss.
- **Mathematical idea:** PESQ-like quality scores and WER can disagree; this exposes the tradeoff between perceptual quality and preserved linguistic content.
- **Connections:** Provides a direct evaluation bridge between robustness, inclusion, and deployment risk.
- **What paper reports:** The paper reports performance variation across demographics/languages and warns that model rankings on VoiceBank-DEMAND do not transfer directly.
- **Limits:** The authors still note benchmark simplification and possible metric overfitting; dataset diversity does not by itself prove universal fairness.

## Cross-paper observation

The second set reinforces that speech systems are evaluated against variation in language, health, identity, domain, and listener-relevant content—not only average benchmark quality. This is a D3 observation over sixteen reviewed papers, not venue-wide prevalence.
