# INTERSPEECH 2025 forty-eighth-pass full-paper notes

Eight official-PDF readings deepen packet-loss repair, articulatory sensing, speech-model unlearning, paralinguistic privacy, synthetic dysarthric data, dysarthric ASR, and fairness in dysarthric voice cloning.

## 1. echo-and-reconstruction

**Paper:** [Multistage Universal Speech Enhancement System for URGENT Challenge](https://www.isca-archive.org/interspeech_2025/le25b_interspeech.html)
**Evidence:** D3; PDF SHA-256 `a49cb0523d436a8def388ed3813c3900416f2b651e3da7b7f7c63ba3e7ab27f7`; full text captured.

- **Ordinary problem:** A transmitted or recorded speech signal can contain clipped samples, missing packets, noise, reverberation, bandwidth loss, and codec artifacts at once.
- **Why hard:** Each distortion removes or corrupts different evidence, and a single undifferentiated enhancer can repair one defect while amplifying another.
- **Naive attempt:** Apply one generic enhancement network to the waveform and hope it learns every corruption jointly.
- **Central move:** Cascade specialized modules in a deliberate order: declipping, separation, packet-loss compensation, and spectral inpainting, with a detector deciding when the first and third modules are needed.
- **Mechanism:** Model the degraded signal as a composition of distortion operators; use Demucs for declipping, BSRoformer for separation, BS-PLCNet in a PQMF subband domain for packet loss, and a time-frequency recurrent inpainting network for spectral artifacts.
- **Mathematical/conceptual structure:** The key object is a masked signal and a composition of operators. Separating domains and ordering repairs reduces the optimization problem from one tangled inverse map to several bounded inverse problems.
- **What paper reports:** The system reports URGENT challenge results competitive with the compared systems; adding inpainting and self-distillation improves several quality measures, while downstream accuracy and objective metrics do not all move together.
- **Limits:** Challenge datasets, distortion order, detector errors, resampling to 48 kHz for some modules, metric choice, and author-reported rankings bound the claim; plausible filling is not recovery of the original samples.

## 2. echo-and-reconstruction

**Paper:** [Rollback Speech: Smart Feedback Prompts for Lost Utterances in Unstable Online Calls](https://www.isca-archive.org/interspeech_2025/quinterovillalobos25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `d95a727348dd6d3a942095bb1361ac92bffd7eff22e7bd0f74b1265ad2fbacae`; full text captured.

- **Ordinary problem:** In an unstable online call, a speaker may continue talking while the listener never receives part of the utterance.
- **Why hard:** The system must identify what was lost without treating an incomplete remote transcript as complete, then request a short useful repair rather than forcing a full repetition.
- **Naive attempt:** Assume the call is reliable, or ask the speaker to repeat everything after any connection failure.
- **Central move:** Compare local and remote ASR streams, identify unreceived content after reconnection, extract keywords from the missing segment, and prompt the speaker to repeat only the relevant information.
- **Mechanism:** The system is an interaction loop: dual transcripts provide two views of the communication event, discrepancy detection estimates the missing interval, and keyword extraction compresses the repair request into actionable cues.
- **Mathematical/conceptual structure:** This is not waveform packet-loss concealment. It preserves conversational meaning through human-in-the-loop selective repetition when acoustic reconstruction is unsafe or unavailable.
- **What paper reports:** The paper demonstrates a WebRTC/WebSocket prototype using Whisper and NLTK keyword extraction in a simulated brief disconnection; it is a show-and-tell feasibility demonstration rather than a controlled recovery benchmark.
- **Limits:** Two-person demonstration conditions, simulated network failure, ASR errors, keyword quality, privacy/latency trade-offs, and absence of a listening study bound the result.

## 3. source-filter-production

**Paper:** [Articulatory Feature Prediction from Surface EMG during Speech Production](https://www.isca-archive.org/interspeech_2025/lee25d_interspeech.html)
**Evidence:** D3; PDF SHA-256 `9511c728f630a8161b77a465df753e1cf2fafb9bddf679590e8baf7961cc2652`; full text captured.

- **Ordinary problem:** A silent-speech interface needs to infer intended speech from muscle activity when an acoustic waveform is absent or inaccessible.
- **Why hard:** EMG channels reflect overlapping facial and articulatory actions, sensors are sparse, and synchronized EMG plus true articulatory measurements are scarce.
- **Naive attempt:** Map EMG directly to a waveform or text while ignoring the physical intermediate movements.
- **Central move:** Use an EMG encoder with convolutional and Transformer layers to predict EMA positions, pitch, loudness, and auxiliary phonemes, making articulatory structure an intermediate target.
- **Mechanism:** The model minimizes L2 losses for EMA, pitch, and loudness and cross-entropy for phonemes. The predicted EMA coordinates represent tongue, lip, and jaw movement rather than an opaque speech label.
- **Mathematical/conceptual structure:** Articulatory features provide a structured bottleneck: the system keeps coordinated movement and voice-source information separate, then can use those predictions for later speech reconstruction.
- **What paper reports:** On 7,565 utterances from one male American English speaker, the paper reports strong EMA and loudness prediction and evaluates held-out utterances using correlations against acoustic-inversion targets.
- **Limits:** Targets are pseudo-ground truth from acoustic-to-articulatory inversion, the speaker is not diverse, experiments focus on vocalized open-vocabulary speech, and feature prediction is not the same as intelligible silent-speech synthesis.

## 4. human-centered-evaluation

**Paper:** [``Alexa, can you forget me?'' Machine Unlearning Benchmark in Spoken Language Understanding](https://www.isca-archive.org/interspeech_2025/koudounas25c_interspeech.html)
**Evidence:** D3; PDF SHA-256 `b1ec8aa661e9eed6b517836026a92fbf14bcf364f70a5a35a3da838c894cbb26`; full text captured.

- **Ordinary problem:** A speaker may ask a spoken-language-understanding service to forget their training examples without destroying the service for everyone else.
- **Why hard:** Removing files is not enough because model parameters retain influence; forgetting must be measured against efficacy, retained utility, and computation across languages and architectures.
- **Naive attempt:** Delete the records and assume the trained model has forgotten, or retrain from scratch for every request.
- **Central move:** Define forget and retain speaker sets, compare eight machine-unlearning methods against a gold model trained without the forget set, and evaluate both what is forgotten and what remains useful.
- **Mechanism:** The benchmark treats unlearning as producing a model close to the retain-only gold model. Metrics include test and forget-set F1, membership-inference attack behavior, generalization, and speedup, making the trade-off explicit.
- **Mathematical/conceptual structure:** Consent becomes a measurable model-state constraint rather than a checkbox: a deletion request is successful only if identity-linked influence is reduced without unacceptable loss of spoken intent recognition.
- **What paper reports:** The paper benchmarks four datasets in four languages, two speech encoders per dataset, and eight unlearning methods; it shows that no single method dominates all efficacy, utility, and efficiency axes.
- **Limits:** Benchmark identities and intent tasks are proxies for real consent, attack strength and gold-model assumptions matter, and unlearning guarantees do not establish that every downstream copy or generated artifact is withdrawn.

## 5. human-centered-evaluation

**Paper:** [Towards Machine Unlearning for Paralinguistic Speech Processing](https://www.isca-archive.org/interspeech_2025/phukan25g_interspeech.html)
**Evidence:** D3; PDF SHA-256 `9d6381021f6a5650d751387c952b7d6faa45c5b803251da57934e33b0e02ad21`; full text captured.

- **Ordinary problem:** A speech emotion or depression model may need to remove a person's contribution from training without rebuilding a large model from zero.
- **Why hard:** Paralinguistic models encode sensitive attributes, and fast forgetting can damage emotion or depression prediction utility; the best feature representation may change the unlearning trade-off.
- **Naive attempt:** Fine-tune the full model on retained data or average models without structuring which data must be forgotten.
- **Central move:** Extend SISA with weight averaging: shard the training data, retrain only affected slices, and average the surviving submodels; compare pretrained speech representations and downstream networks.
- **Mechanism:** SISA++ turns a global deletion into local retraining plus parameter aggregation. The evaluation separates forgetting performance from retained task performance and measures computational savings.
- **Mathematical/conceptual structure:** The mechanism uses data partitioning as a control boundary: the model remembers where influence entered, so a request can remove a bounded subset of training history.
- **What paper reports:** Experiments use CREMA-D speech emotion recognition and E-DAIC depression detection; the paper reports TRILLsson features with a Transformer as a robust recipe under its tested settings.
- **Limits:** The result depends on shard design, feature extractor, downstream task, attack/evaluation protocol, and access to the original training pipeline; fast unlearning is not proof of legal or social consent compliance.

## 6. clinical-and-assistive-speech

**Paper:** [Synthetic Dysarthric Speech: A Supplement, Not a Substitute for Authentic Data in Dysarthric Speech Recognition](https://www.isca-archive.org/interspeech_2025/li25n_interspeech.html)
**Evidence:** D3; PDF SHA-256 `271a0450f07fc0851b90bbbbc8e71c7afde6df7c1906db9051df9edb76be16e5`; full text captured.

- **Ordinary problem:** Dysarthric speech is scarce and variable, so recognizers need more training examples without pretending that synthetic speech is equivalent to a person's real motor patterns.
- **Why hard:** Synthetic speech can scale text and speaker combinations but may miss irregular timing, articulation, spectral detail, and clinically meaningful variation.
- **Naive attempt:** Replace authentic dysarthric recordings with large quantities of generated speech because more data should always improve recognition.
- **Central move:** Train speaker-specific TTS systems, generate synthetic dysarthric utterances at several scales, combine them with authentic data for dysarthric speech recognition, and compare feature distributions and recognition results.
- **Mechanism:** The study varies whether training uses authentic Set A/Set B data, synthetic data derived from Set A, or much larger synthetic additions. It measures ASR performance and compares acoustic feature distributions between authentic and synthetic samples.
- **Mathematical/conceptual structure:** Synthetic data is a distributional proposal, not a label-preserving copy: the relevant question is whether generated speech spans the motor and acoustic variation needed by the recognizer.
- **What paper reports:** Across the tested Chinese dysarthric speech setup, synthetic speech alone does not replace authentic data and large synthetic additions yield only marginal gains over authentic training.
- **Limits:** The language, seven-speaker usable subset, TTS model, data scale, ASR architecture, and speaker-independent split bound generalization; a synthetic-data result is not clinical validation.

## 7. clinical-and-assistive-speech

**Paper:** [Bridging ASR and LLMs for Dysarthric Speech Recognition: Benchmarking Self-Supervised and Generative Approaches](https://www.isca-archive.org/interspeech_2025/aboeitta25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `e39b8c1a94256ca369c6800d405f322258d34df86c51870aaa1b324d273832fd`; full text captured.

- **Ordinary problem:** Automatic speech recognition must transcribe dysarthric speech whose phonetic timing and articulation violate assumptions learned from typical speech.
- **Why hard:** CTC can misalign distorted phonemes, ordinary end-to-end models can produce grammatical but acoustically unsupported text, and severity and speaker shifts change the error pattern.
- **Naive attempt:** Use a standard ASR model and treat WER as the complete measure of success.
- **Central move:** Benchmark CTC, Whisper, and LLM-enhanced decoders, including bridge networks and a Q-Former that connects Whisper acoustic features to Vicuna for context-aware decoding.
- **Mechanism:** The comparison keeps TORGO and UASpeech speaker-independent splits and evaluates WER by dysarthria severity. The decoder choice changes how much linguistic context can repair uncertain acoustic evidence.
- **Mathematical/conceptual structure:** The paper exposes an evidence trade-off: a stronger language prior can improve semantic reconstruction, but it can also make a plausible transcript less directly grounded in the signal.
- **What paper reports:** Whisper improves over CTC baselines, and Whisper-Vicuna reports the lowest WER in the tested TORGO and UASpeech comparisons; all results remain author-reported.
- **Limits:** Dataset splits, severity labels, model scale, decoding prompts, and WER limit the claim; lower WER does not prove faithful preservation of disfluencies or speaker intent.

## 8. human-centered-evaluation

**Paper:** [Fairness in Dysarthric Speech Synthesis: Understanding Intrinsic Bias in Dysarthric Speech Cloning using F5-TTS](https://www.isca-archive.org/interspeech_2025/m25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `55d6ed6df4a7d6c45ba2b1cd66582af5cd0c1e54e27d8888d1063b72ca522f3c`; full text captured.

- **Ordinary problem:** Voice synthesis for dysarthric speakers should preserve intelligibility, identity, and prosodic character without treating disability severity as noise to erase.
- **Why hard:** A zero-shot synthesizer may copy speaker identity while changing pathological speech patterns unevenly across severity groups, creating a fairness problem hidden by average quality scores.
- **Naive attempt:** Report one average similarity or intelligibility score and assume it applies equally to healthy and dysarthric speakers.
- **Central move:** Generate speech from TORGO prompts with F5-TTS, measure intelligibility, speaker similarity, and prosody similarity, then compare severity groups using parity difference and disparate impact.
- **Mechanism:** The study defines metrics over group means: WER/CER for intelligibility, SIM-o cosine similarity for speaker traits, and AutoPCP for prosody. Fairness is assessed by deviations from healthy-speaker reference behavior.
- **Mathematical/conceptual structure:** The mechanism is an evaluation reframing: voice cloning is not one scalar quality target when a model may preserve identity but unevenly alter disability-linked prosody or intelligibility.
- **What paper reports:** The paper reports severity-dependent differences in the objective measures and uses those differences to characterize intrinsic bias in F5-TTS cloning.
- **Limits:** TORGO, reference-prompt choice, automatic metrics, severity grouping, and zero-shot model behavior bound the result; parity in proxies does not establish respectful control, consent, or listener benefit.

