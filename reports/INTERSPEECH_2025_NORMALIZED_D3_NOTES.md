# INTERSPEECH 2025 normalized D3 paper notes

This consolidated report uses the authoritative semantic-review path for every captured D3 paper. Results remain author-reported unless a separate bounded execution record says otherwise.

## 1. Hear Me Out: Interactive evaluation and bias discovery platform for speech-to-speech conversational AI

**Paper:** [Hear Me Out: Interactive evaluation and bias discovery platform for speech-to-speech conversational AI](https://www.isca-archive.org/interspeech_2025/bokkahallisatish25_interspeech.html)
**Taxonomy:** `evaluation-deployment-and-consequence / auditability-and-accountability / auditability-and-contestability`
**Evidence:** D3 full-paper capture; PDF SHA-256 `95321e8befa4ed5ca1458df111c3893bce8485004925d6db46e971855cd16c97`; full-text SHA-256 `7a4e6d7767894aecdbefe54bfe8119fea876f86455ab7cc44f82727d8a5b9d34`.

- **Ordinary problem:** A conversational speech model may respond differently to the same words when the speaker’s apparent age, gender, accent, or voice is changed, but ordinary benchmarks hide that counterfactual.
- **Why it is hard:** A response difference can come from speech content, vocal identity, prosody, or model randomness; users need a paired way to change one input factor and inspect what changes downstream.
- **Naive attempt:** Run one benchmark transcript per prompt and summarize average response quality without exposing speaker-dependent behavior.
- **Central move:** Build an interactive platform that converts the same user prompt into alternative voices, shows paired model responses, and combines direct inspection with automated speech, sentiment, quality, pitch, and semantic-consistency measures.
- **Mechanism:** Hear Me Out lets a user choose a speech foundation model, submit an original or voice-converted prompt, view the response pair, and inspect response speech rate, pitch, audio-quality dimensions, sentiment, and semantic similarity. The paired interaction makes possible a counterfactual probe of speaker characteristics.
- **Mathematical idea:** The platform reports syllables per second, mean and standard-deviation F0, model-based sentiment/quality scores, and semantic textual similarity. These are diagnostic projections of behavior, not a single fairness metric or causal estimate.
- **What the paper reports:** The paper demonstrates an accessible interactive evaluation experience for comparing responses to original and transformed voices and argues that it can expose speaker-dependent differences and possible bias.
- **Limits:** The work is a platform/demo, not a powered user study or population-level fairness audit; its automated metrics and selected voice profiles constrain what can be observed. The authors explicitly call for larger studies and additional bias metrics, and no independent reproduction was performed.

## 2. FaiST: A Benchmark Dataset for Fairness in Speech Technology

**Paper:** [FaiST: A Benchmark Dataset for Fairness in Speech Technology](https://www.isca-archive.org/interspeech_2025/jahan25_interspeech.html)
**Taxonomy:** `evaluation-deployment-and-consequence / auditability-and-accountability / auditability-and-contestability`
**Evidence:** D3 full-paper capture; PDF SHA-256 `0583b1c6cd20c19ccbb888f0c8e8b8ecef70c270e3f4d269642568d430eecc55`; full-text SHA-256 `e7c6e77552d2807609196c4c400a28c3686576f9faeb7a330c045d996884c1a6`.

- **Ordinary problem:** Speech technology should not work well only for the majority speakers or accents represented in its training data.
- **Why it is hard:** Fairness depends on which groups, tasks, and error costs are measured; one aggregate accuracy can hide unequal failures.
- **Naive attempt:** Report overall WER or accuracy and call the system fair, or compare groups without a reproducible benchmark.
- **Central move:** Create a benchmark that measures fairness across speech-technology tasks and demographic or linguistic conditions with explicit group-level evidence.
- **Mechanism:** FaiST is a benchmark dataset for fairness in speech technology.
- **Mathematical idea:** Fairness becomes an evaluation object rather than a vague aspiration: group membership, task outcome, and error disparity must be linked while respecting privacy and sampling limits.
- **What the paper reports:** The paper reports benchmark resources and fairness evaluation results for the tested speech technologies.
- **Limits:** Group definitions, labels, sample balance, tasks, metrics, and consent bound the conclusions; benchmark parity is not proof of social fairness.

## 3. A Comprehensive Real-World Assessment of Audio Watermarking Algorithms: Will They Survive Neural Codecs?

**Paper:** [A Comprehensive Real-World Assessment of Audio Watermarking Algorithms: Will They Survive Neural Codecs?](https://www.isca-archive.org/interspeech_2025/ozer25_interspeech.html)
**Taxonomy:** `evaluation-deployment-and-consequence / auditability-and-accountability / auditability-and-contestability`
**Evidence:** D3 full-paper capture; PDF SHA-256 `a876829819a916551e8945bcf26b155d54c41be474020b7b1e099334bef4cf14`; full-text SHA-256 `24d006109bb9d1de8a9f23af6cfef914503c8bbfc1324fabb22a8d108a430e2a`.

- **Ordinary problem:** An audio watermark should survive ordinary processing and neural codecs while remaining detectable, otherwise it cannot support provenance or accountability in real systems.
- **Why it is hard:** Compression and generative codecs intentionally alter waveform details; a watermark can be detectable in clean audio yet disappear after the transformations people actually use.
- **Naive attempt:** Test only clean files or assume a watermark that survives one codec survives every neural codec.
- **Central move:** Evaluate audio-watermarking algorithms under a broad real-world transformation suite, including neural codecs, and compare detectability and audio quality.
- **Mechanism:** The paper provides a comprehensive real-world assessment of audio watermarking algorithms and asks whether they survive neural codecs.
- **Mathematical idea:** Robustness is a chain of transformations: a watermark claim is meaningful only over an explicit threat/process set, with detectability balanced against audible distortion.
- **What the paper reports:** The paper reports comparative survival and failure patterns across watermarking methods and neural codecs.
- **Limits:** Algorithms, codec versions, payloads, thresholds, and attack suite bound the result; survival in tested codecs is not universal tamper resistance.

## 4. NanoCodec: Towards High-Quality Ultra Fast Speech LLM Inference

**Paper:** [NanoCodec: Towards High-Quality Ultra Fast Speech LLM Inference](https://www.isca-archive.org/interspeech_2025/casanova25_interspeech.html)
**Taxonomy:** `evaluation-deployment-and-consequence / deployment-cost / latency-and-resource`
**Evidence:** D3 full-paper capture; PDF SHA-256 `94b942d9676fb3e3204821f38649c376f7ab4dee89b49344a970e6ec86f5532d`; full-text SHA-256 `651dd53005e72975dc80faf2470e22fc185cb88ec1cdff4eeacf2777a226125b`.

- **Ordinary problem:** A speech codec used inside an autoregressive audio model should compress sound with few tokens per second without destroying reconstruction quality.
- **Why it is hard:** High frame rates make every generated second expensive, while lowering rate or bitrate can erase fine acoustic detail and causality can add delay.
- **Naive attempt:** Choose a low frame rate without measuring the rate/bitrate/causality tradeoff, or optimize only waveform quality at an impractical token rate.
- **Central move:** Ablate frame rate, bitrate, and causality, then design NanoCodec around a low-rate operating point and compare reconstruction quality.
- **Mechanism:** The codec maps audio to discrete tokens and back; token rate controls autoregressive steps while bitrate and causal context control information and latency.
- **Mathematical idea:** Compression is a rate-distortion-resource tradeoff: fewer symbols reduce computation but constrain what the decoder can reconstruct.
- **What the paper reports:** NanoCodec reports high-quality compression at 12.5 FPS and competitive results across bitrate ranges.
- **Limits:** Audio domain, codec training data, perceptual metric, hardware, and causality setting bound transfer; codec quality is not end-to-end speech generation quality.

## 5. Breaking Resource Barriers in Speech Emotion Recognition via Data Distillation

**Paper:** [Breaking Resource Barriers in Speech Emotion Recognition via Data Distillation](https://www.isca-archive.org/interspeech_2025/chang25d_interspeech.html)
**Taxonomy:** `evaluation-deployment-and-consequence / deployment-cost / latency-and-resource`
**Evidence:** D3 full-paper capture; PDF SHA-256 `55abbd0e0f3461e8cc355fea9994b9d020eeb26c7ed9f006026d7dbf87aae7b4`; full-text SHA-256 `8f9d64585002182b5ad9bbd1e72ae68cb37692c99447e293f70d390e1bb9f2c7`.

- **Ordinary problem:** An emotion recognizer should fit an IoT device without retaining a large private emotional-speech dataset.
- **Why it is hard:** Memory and compute constrain edge models, while emotional speech can carry sensitive information that should not be distributed unnecessarily.
- **Naive attempt:** Compress the model alone or train on a random small subset and assume it preserves the full-data decision boundary.
- **Central move:** Distill a smaller synthetic dataset that retains training utility under fixed initialization, then train resource-constrained SER models on it.
- **Mechanism:** The distilled set approximates the information needed by the learner; performance on held-out emotion recognition tests measures retained utility.
- **Mathematical idea:** Data distillation shifts compression from parameters to examples, trading dataset fidelity and privacy exposure against model performance.
- **What the paper reports:** The paper reports comparable SER performance between models trained on distilled and original emotional-speech data.
- **Limits:** Synthesis method, emotion labels, initialization, privacy threat model, device profile, and test split bound the result; utility parity is not formal privacy.

## 6. PruneSLU: Efficient On-device Spoken Language Understanding through Vocabulary and Structural Pruning

**Paper:** [PruneSLU: Efficient On-device Spoken Language Understanding through Vocabulary and Structural Pruning](https://www.isca-archive.org/interspeech_2025/do25_interspeech.html)
**Taxonomy:** `evaluation-deployment-and-consequence / deployment-cost / latency-and-resource`
**Evidence:** D3 full-paper capture; PDF SHA-256 `1c859b20b12eb8f022c0ef5d6260f3726017b00d090c741d7be7091cbe4c3f21`; full-text SHA-256 `9649c30fbbea53774275ffd7d1be3df351877fd6620cd0a995776bc84c4b9d5a`.

- **Ordinary problem:** Spoken-language understanding must fit on a device with limited memory and power without losing needed intent and slot decisions.
- **Why it is hard:** Pruning can remove rare but important vocabulary or acoustic layers, while average scores can hide task-specific loss.
- **Naive attempt:** Shrink a model uniformly or remove the smallest weights without asking which tokens and layers support the task.
- **Central move:** Prune task-irrelevant vocabulary first, prune layers structurally, then refine with distillation and contrastive losses.
- **Mechanism:** PruneSLU starts from Whisper-tiny, selects a base vocabulary, chooses layers by loss, and trains with language-model, distillation, and contrastive components on STOP and SLURP.
- **Mathematical idea:** Exact match, EM-Tree, intent accuracy, slot F1, parameter counts, and pruning/loss ablations expose the tradeoff.
- **What the paper reports:** The 15M model retains 98% of original STOP performance, reaches STOP EM 72.31 and SLURP slot F1 71.42, and improves on listed compression baselines.
- **Limits:** STOP/SLURP domains, Whisper initialization, five seeds, and author-reported comparisons bound the result; energy and open-world commands are not tested.

## 7. GTA: Towards Generative Text-To-Audio Retrieval via Multi-Scale Tokenizer

**Paper:** [GTA: Towards Generative Text-To-Audio Retrieval via Multi-Scale Tokenizer](https://www.isca-archive.org/interspeech_2025/fang25c_interspeech.html)
**Taxonomy:** `evaluation-deployment-and-consequence / deployment-cost / latency-and-resource`
**Evidence:** D3 full-paper capture; PDF SHA-256 `1f6c6b8fef11b47082e7e3ae71b96bd280478cb7bac70152483fa138c00c222d`; full-text SHA-256 `e73faeb65af4706e8bd6ab71ec57548024367727ad19dd816a265ae8cc7c2ac4`.

- **Ordinary problem:** Generative text-to-audio retrieval should preserve multiscale audio structure without excessive cost.
- **Why it is hard:** Fine representations improve detail but make tokenization and retrieval slow or memory-heavy.
- **Naive attempt:** Use one resolution or maximize fidelity without measuring retrieval cost.
- **Central move:** Use a multi-scale tokenizer and generative retrieval architecture with explicit resource tradeoffs.
- **Mechanism:** Coarse and fine audio tokens represent different temporal resolutions for retrieval.
- **Mathematical idea:** The relevant object is the latency-and-resource evidence described by the paper's mechanism: Coarse and fine audio tokens represent different temporal resolutions for retrieval.
- **What the paper reports:** The paper reports GTA results for generative text-to-audio retrieval.
- **Limits:** Audio, prompts, token rates, metrics, hardware, and generation budget bound transfer.

## 8. Ultra-Low Bit Post-Training Quantization of Large Speech Models via K-Means Clustering and Mixed Precision Allocation

**Paper:** [Ultra-Low Bit Post-Training Quantization of Large Speech Models via K-Means Clustering and Mixed Precision Allocation](https://www.isca-archive.org/interspeech_2025/gu25b_interspeech.html)
**Taxonomy:** `evaluation-deployment-and-consequence / deployment-cost / latency-and-resource`
**Evidence:** D3 full-paper capture; PDF SHA-256 `d24000ee163144cda02059d20dd2e670a4cd316309f2c920a1999e6aebdd553d`; full-text SHA-256 `3a7795325f3a3cf9e318a69080b1c2e0eae161c0650632eb2ad96363997f0e66`.

- **Ordinary problem:** A large speech model must fit on practical hardware without losing recognition quality, especially when storage and memory are tight.
- **Why it is hard:** Below eight bits, transformer weight outliers make uniform quantization damage a small number of important parameters.
- **Naive attempt:** Round every weight to the same low-precision grid.
- **Central move:** Cluster weights nonlinearly, allocate more bits to columns with many outliers, and retain only critical outliers in sparse FP32 form.
- **Mechanism:** The method quantizes Whisper-Large-V3 after training and compares mixed precision and outlier retention across speech datasets.
- **Mathematical idea:** Bits per parameter expresses storage; WER measures recognition loss, and the columnwise allocation ties precision to the observed weight distribution.
- **What the paper reports:** The paper reports 2.12-bit quantization with a 0.17 percentage-point WER increase on LibriSpeech test-clean and under 1% degradation across additional datasets.
- **Limits:** The result is author-reported for Whisper-Large-V3 and tested corpora; latency, energy, hardware kernels, and other model families remain open.

## 9. Unfolding A Few Structures for The Many: Memory-Efficient Compression of Conformer and Speech Foundation Models

**Paper:** [Unfolding A Few Structures for The Many: Memory-Efficient Compression of Conformer and Speech Foundation Models](https://www.isca-archive.org/interspeech_2025/li25v_interspeech.html)
**Taxonomy:** `evaluation-deployment-and-consequence / deployment-cost / latency-and-resource`
**Evidence:** D3 full-paper capture; PDF SHA-256 `38d94d25adae57015cb261471e8788a565f54069396b0240d086459e5285c446`; full-text SHA-256 `fd843bd179416a196c2821419c71b8c637699701996e05e8d5d3e0ded43962a7`.

- **Ordinary problem:** A speech model should fit memory and storage limits without losing larger-model behavior at different deployment depths.
- **Why it is hard:** Depth-specific models duplicate parameters, while compression can reduce capacity or make one operating point brittle.
- **Naive attempt:** Store a separate full model for each depth, or prune once and accept a fixed quality/resource tradeoff.
- **Central move:** Train a compact seed and unfold it through shared structures, using KL self-distillation between largest and seed paths.
- **Mechanism:** Logical depth changes through repeated blocks sharing a seed; distillation aligns small and large outputs across paths.
- **Mathematical idea:** Unfolding trades parameter storage for repeated computation, while KL divergence keeps paths behaviorally close.
- **What the paper reports:** The models report comparable ASR with 35% Conformer and 30% wav2vec2/HuBERT parameter reductions.
- **Limits:** Hardware latency, unfolding cost, family, task, and benchmark coverage bound transfer; fewer parameters is not automatically less energy.

## 10. Simultaneous Masked and Unmasked Decoding with Speculative Decoding Masking for Fast ASR without Accuracy Loss

**Paper:** [Simultaneous Masked and Unmasked Decoding with Speculative Decoding Masking for Fast ASR without Accuracy Loss](https://www.isca-archive.org/interspeech_2025/okabe25_interspeech.html)
**Taxonomy:** `evaluation-deployment-and-consequence / deployment-cost / latency-and-resource`
**Evidence:** D3 full-paper capture; PDF SHA-256 `bbd4d7f3fdddc859f36b511b2865446d122f4492d04dd4dcf6249675163b1aa3`; full-text SHA-256 `0652d5cdba1205f68b5f2842a6a4d6fee1d526e719b5d9c95fadcd11f781cb06`.

- **Ordinary problem:** An ASR decoder should approach autoregressive accuracy without paying for every sequential token decision.
- **Why it is hard:** Non-autoregressive guesses are fast but can lose accuracy, while autoregressive search repeatedly computes scores for hypotheses that are already predictable.
- **Naive attempt:** Choose either full autoregressive beam search or a non-autoregressive decoder and accept the speed-accuracy tradeoff.
- **Central move:** Combine simultaneous masked/unmasked decoding with speculative masking so confidently predictable hypotheses skip unnecessary decoder computation.
- **Mechanism:** Preliminary masked decisions identify positions whose score computation can be omitted; the remaining positions retain the autoregressive search path and its result.
- **Mathematical idea:** The method exploits conditional redundancy in sequence search: computation is spent where uncertainty remains rather than uniformly at every token.
- **What the paper reports:** On TED-LIUM2, the paper reports WER 7.3% for both the proposed and autoregressive systems, with RTF 0.41 versus 0.59.
- **Limits:** One corpus/model, beam and hardware settings, confidence thresholds, and real-time measurement protocol bound transfer; equal WER on one test set does not prove universal speed preservation.

## 11. SpecTokenizer: A Lightweight Streaming Codec in the Compressed Spectrum Domain

**Paper:** [SpecTokenizer: A Lightweight Streaming Codec in the Compressed Spectrum Domain](https://www.isca-archive.org/interspeech_2025/wan25_interspeech.html)
**Taxonomy:** `evaluation-deployment-and-consequence / deployment-cost / latency-and-resource`
**Evidence:** D3 full-paper capture; PDF SHA-256 `796d66ded7e7560ac4e6a34bd3234e09319288a8e26fadc9c401159c0e1ee435`; full-text SHA-256 `38809760c5af9e4f24ff6fc52d95dfe5e32cd2904df7865b0773bad32d8012ae`.

- **Ordinary problem:** An audio codec for a streaming device must compress speech into a small code while operating with little computation and little delay.
- **Why it is hard:** Heavy neural codecs may compress well but require too many parameters or operations for a real-time device.
- **Naive attempt:** Take a large offline codec and accept its compute cost, or reduce layers without changing the representation domain.
- **Central move:** Operate in a compressed spectral domain and combine lightweight convolutional and recurrent layers at multiple time scales.
- **Mechanism:** SpecTokenizer is a streaming single-codebook codec evaluated at 4 kbps against a lightweight codec under matched computation and storage budgets.
- **Mathematical idea:** The codec trades waveform detail for discrete codes; bitrate, reconstruction quality, computation, and parameter count expose the deployment boundary.
- **What the paper reports:** At 4 kbps it reports comparable or better performance with 20% of the computation and 10% of the parameters of the comparison codec.
- **Limits:** Bitrate, audio material, hardware, streaming definition, and quality measure bound the claim; benchmark efficiency does not prove end-to-end device power or user benefit.

## 12. WIND: Accelerated RNN-T Decoding with Windowed Inference for Non-blank Detection

**Paper:** [WIND: Accelerated RNN-T Decoding with Windowed Inference for Non-blank Detection](https://www.isca-archive.org/interspeech_2025/xu25c_interspeech.html)
**Taxonomy:** `evaluation-deployment-and-consequence / deployment-cost / latency-and-resource`
**Evidence:** D3 full-paper capture; PDF SHA-256 `f6522e777465a4261b00105d672dbbef2e3fc6336bec7bef1e8f6042b2512000`; full-text SHA-256 `12bc0d07a13f0b3e0d0fe30c35bafab5ee8b4816f1737508e17419df7f0fec99`.

- **Ordinary problem:** An RNN-T recognizer must decide quickly when a frame contains a label, but sequentially inspecting every frame wastes time when most frames are blank.
- **Why it is hard:** Parallelizing blindly can change the order-dependent decoder state and harm word accuracy.
- **Naive attempt:** Run the original sequential decoder faster in isolation or process every frame in a large batch without respecting non-blank decisions.
- **Central move:** Inspect a window of frames in parallel to locate non-blank predictions, then retain decoder logic around the informative positions for greedy and beam search.
- **Mechanism:** WIND is evaluated on multiple datasets with greedy, batched greedy, and beam-search RNN-T decoding against sequential baselines.
- **Mathematical idea:** The method exploits sparsity in the label stream; speedup is meaningful only when WER remains unchanged and the decoding mode is specified.
- **What the paper reports:** Greedy modes reach up to 2.4x speedup with identical WER, while the proposed beam search is faster and slightly more accurate than alternatives.
- **Limits:** RNN-T models, datasets, hardware, window size, and decoding modes bound the result; reported speedup is not portable to every implementation or workload.

## 13. Effective and Efficient One-pass Compression of Speech Foundation Models Using Sparsity-aware Self-pinching Gates

**Paper:** [Effective and Efficient One-pass Compression of Speech Foundation Models Using Sparsity-aware Self-pinching Gates](https://www.isca-archive.org/interspeech_2025/xu25e_interspeech.html)
**Taxonomy:** `evaluation-deployment-and-consequence / deployment-cost / latency-and-resource`
**Evidence:** D3 full-paper capture; PDF SHA-256 `a9efd05ab02ed6d19849538cfd73c2d842f53abd9bf78e6b0037d4b399fd067b`; full-text SHA-256 `f251365ff939c449738553c9309fb39136b4faad07b486aa2d8c43ea0dfa3f7d`.

- **Ordinary problem:** A speech foundation model may be accurate but too large to deploy, so its unused capacity must be removed without damaging recognition.
- **Why it is hard:** Pruning after training can be expensive and can remove units that are useful only in combination with others.
- **Naive attempt:** Prune fixed layers with a hand rule or compress the model in a separate stage after all training is finished.
- **Central move:** Learn a small gate for each layer during training and let the gates pinch off underused neurons while model parameters are updated at the same time.
- **Mechanism:** Self-pinching gates are trained with wav2vec2.0-base and HuBERT-large and then drive fine-grained neuron pruning on LibriSpeech-100hr.
- **Mathematical idea:** A gate is a learned resource-allocation decision; parameter count, WER, compression ratio, and compression time measure the accuracy-efficiency frontier.
- **What the paper reports:** The method removes 65% of wav2vec2.0-base and 60% of HuBERT-large parameters without a statistically significant test-clean WER increase, with 7.05% WER at 4.26x compression.
- **Limits:** LibriSpeech, model variants, pruning thresholds, and test-clean evaluation bound the result; no claim follows about noisy conditions, energy, or other languages.

## 14. Dynamic Acoustic Model Architecture Optimization in Training for ASR

**Paper:** [Dynamic Acoustic Model Architecture Optimization in Training for ASR](https://www.isca-archive.org/interspeech_2025/xu25i_interspeech.html)
**Taxonomy:** `evaluation-deployment-and-consequence / deployment-cost / latency-and-resource`
**Evidence:** D3 full-paper capture; PDF SHA-256 `2c502635795e3d85856d7ebf4129960ed0a10bc772ce6407669c3ad0680c2069`; full-text SHA-256 `7f86178b9779d38740c98c3f997368c52064bf083e4b76101ecbb337fb4217ab`.

- **Ordinary problem:** An ASR model has a fixed training budget, but not every part of its architecture uses that budget equally well.
- **Why it is hard:** Hand-designed architectures require expertise, while neural architecture search can spend more computation searching than training the final model.
- **Naive attempt:** Choose one repeated block structure before training or run an expensive search over many complete models.
- **Central move:** Grow useful parts and drop less useful parts during training, reallocating parameters while keeping the total model complexity and training resources fixed.
- **Mechanism:** DMAO is evaluated with CTC on LibriSpeech, TED-LIUM-v2, and Switchboard across architectures and model sizes.
- **Mathematical idea:** The architecture becomes a changing allocation of parameters; relative WER at matched resources tests whether reallocation, rather than extra capacity, creates the gain.
- **What the paper reports:** The paper reports up to roughly 6% relative WER improvement across datasets, architectures, and sizes with negligible added training overhead.
- **Limits:** Datasets, CTC setup, compute budget, search rules, and final architecture bound the result; a benchmark gain does not establish optimality or universal resource allocation.

## 15. Optimizing CLAP Reward with LLM Feedback for Semantically Aligned and Diverse Automated Audio Captioning

**Paper:** [Optimizing CLAP Reward with LLM Feedback for Semantically Aligned and Diverse Automated Audio Captioning](https://www.isca-archive.org/interspeech_2025/ahn25b_interspeech.html)
**Taxonomy:** `evaluation-deployment-and-consequence / metric-and-human-targets / quality-and-naturalness`
**Evidence:** D3 full-paper capture; PDF SHA-256 `689b94f24303b766fee46c074cf3f87f158247679e4b54b4717a146d221f2ca2`; full-text SHA-256 `8f8ed754167119ab873fbb0a4349222259abc361c267558e9722d543405ebeab`.

- **Ordinary problem:** An audio captioner should describe what happened naturally and accurately, not exploit a similarity score with repeated or awkward words.
- **Why it is hard:** CLAP rewards can favor semantically related phrases while ignoring repetition and human naturalness.
- **Naive attempt:** Optimize one embedding similarity metric directly.
- **Central move:** Combine CLAP similarity with repetition penalties, clipping, and LLM feedback during reward optimization.
- **Mechanism:** CRRP trains an automated audio-captioning system with a stabilized CLAP reward and an LLM evaluator; semantic, human, and AI assessments are compared.
- **Mathematical idea:** The reward combines semantic alignment and language naturalness, while multiple evaluations expose metric-specific behavior.
- **What the paper reports:** The paper reports strong semantic and human/AI evaluation results for the proposed reward system.
- **Limits:** The result depends on caption datasets, evaluator prompts, and reward weighting; human agreement and out-of-domain audio remain open.

## 16. SMARTMOS: Modeling Subjective Audio Quality Evaluation for Real-Time Applications

**Paper:** [SMARTMOS: Modeling Subjective Audio Quality Evaluation for Real-Time Applications](https://www.isca-archive.org/interspeech_2025/balasubramanian25_interspeech.html)
**Taxonomy:** `evaluation-deployment-and-consequence / metric-and-human-targets / quality-and-naturalness`
**Evidence:** D3 full-paper capture; PDF SHA-256 `386d3dbf18ab82d61c32dd7601146e16631e22609283721e89df977e270db819`; full-text SHA-256 `eb3a3ff4d24d52580aba9e1d55173d3692ff74aaf3b9ba11a0a783136a2383c1`.

- **Ordinary problem:** Estimate how people judge audio quality quickly enough for a real-time system without running a new listening test every time.
- **Why it is hard:** Subjective listening tests are slow and expensive, while signal-only measures may miss the distortions listeners notice under the actual application conditions.
- **Naive attempt:** Replace human ratings with one fixed signal metric and assume it remains valid across codecs, devices, distortions, and listeners.
- **Central move:** Learn a model of subjective quality from listening-test ratings and design it for fast prediction in the intended real-time setting.
- **Mechanism:** Audio examples and human scores are used to train a predictor; its estimates are compared with held-out subjective ratings across conditions and computational constraints.
- **Mathematical idea:** The model minimizes prediction error against quality ratings; correlation and error against human scores measure agreement, not whether the model captures every user-relevant harm.
- **What the paper reports:** The paper reports a real-time subjective-quality model intended to approximate listening-test judgments more cheaply and quickly.
- **Limits:** Human ratings, test conditions, and audio distortions define the target; a predictor can reproduce annotator bias and fail on unseen codecs or populations. No independent reproduction was performed.

## 17. Intelligibility Prediction for Time-Modified Speech Signals Using Spectro-Temporal Modulation Features

**Paper:** [Intelligibility Prediction for Time-Modified Speech Signals Using Spectro-Temporal Modulation Features](https://www.isca-archive.org/interspeech_2025/bashir25_interspeech.html)
**Taxonomy:** `evaluation-deployment-and-consequence / metric-and-human-targets / word-error-versus-understanding`
**Evidence:** D3 full-paper capture; PDF SHA-256 `d16f9d8366aa1d9bdc42725741998c47f64b5238df20ec369ee7572525fa795d`; full-text SHA-256 `4167da4e009d62677ac6bd40c96f92c0fb50fa2e6db5e37c72edcb96213cba84`.

- **Ordinary problem:** A speech-quality score should remain meaningful when processing changes the timing of the speech, not only its spectrum.
- **Why it is hard:** Reference-based intelligibility predictors compare aligned clean and degraded signals; time modification breaks that alignment.
- **Naive attempt:** Use MFCC-based dynamic time warping or assume time modification is a small nuisance.
- **Central move:** Align clean and time-modified speech with selected spectro-temporal modulation features, then feed the alignment into existing reference-based intelligibility predictors.
- **Mechanism:** The system uses DTW over modulation features and compares two ways of incorporating the alignment into RB-SIPAs across noise and time-modification conditions.
- **Mathematical idea:** The move separates two questions that are often mixed: finding corresponding speech events and predicting whether the resulting signal is intelligible.
- **What the paper reports:** The paper reports better alignment behavior and better correlation with listening scores than MFCC-based alternatives under its tested conditions.
- **Limits:** The listening datasets, degradation types, chosen modulation channels, and reference availability bound the claim; correlation is not a complete model of listener experience.

## 18. Benchmarking and Confidence Evaluation of LALMs For Temporal Reasoning

**Paper:** [Benchmarking and Confidence Evaluation of LALMs For Temporal Reasoning](https://www.isca-archive.org/interspeech_2025/bhattacharya25b_interspeech.html)
**Taxonomy:** `evaluation-deployment-and-consequence / metric-and-human-targets / calibration-and-selective-use`
**Evidence:** D3 full-paper capture; PDF SHA-256 `6752a96fca775cf2a4c7e927a22c683332091f52227799fafc053b035fe7c5a7`; full-text SHA-256 `6acb2b735be08f8752a0a0bc92e5b098f51fe1637991c82554842f46e360b1ed`.

- **Ordinary problem:** An audio language model may answer a temporal question correctly for the wrong reasons or change its answer when the same content is phrased equivalently.
- **Why it is hard:** Accuracy alone cannot show whether a model tracks time relations or knows when its answer is unstable; speech duration and temporal ordering create failures not visible in ordinary classification tests.
- **Naive attempt:** Report one accuracy number on a fixed question set and treat it as reasoning competence and confidence.
- **Central move:** Build the TREA temporal-reasoning dataset, benchmark audio language models against people, and measure uncertainty through invariance to semantically identical perturbations.
- **Mechanism:** The paper introduces Temporal Reasoning Evaluation of Audio and an uncertainty metric for large audio language models.
- **Mathematical idea:** Evaluation must separate getting the answer right from behaving consistently under meaning-preserving changes; these are different properties and can move in opposite directions.
- **What the paper reports:** The paper reports that tested open-source models lagged human performance and that accuracy and perturbation-based uncertainty were not necessarily correlated.
- **Limits:** The dataset, perturbations, models, human comparison, and temporal tasks bound conclusions; invariance is one operational uncertainty test, not a complete account of confidence.

## 19. Benchmarking Time-localized Explanations for Audio Classification Models

**Paper:** [Benchmarking Time-localized Explanations for Audio Classification Models](https://www.isca-archive.org/interspeech_2025/bolanos25_interspeech.html)
**Taxonomy:** `evaluation-deployment-and-consequence / metric-and-human-targets / quality-and-naturalness`
**Evidence:** D3 full-paper capture; PDF SHA-256 `c5cd9eca43512c992793f379177678d8b237be6d64e6c311fb619136d7e72806`; full-text SHA-256 `5db912b9f65ee8811a4c218a94fe66882355b3a115d9300bd2f8da69158ce3cc`.

- **Ordinary problem:** A listener should be able to see which moments of an audio clip drove a classifier, especially when the model may be using a spurious sound.
- **Why it is hard:** There is usually no ground-truth explanation, so explanation methods can look plausible while pointing to the wrong time region.
- **Naive attempt:** Trust a saliency plot or compare explanations by visual appeal.
- **Central move:** Create time annotations for target events as a proxy reference and benchmark model-agnostic post-hoc explanations against them.
- **Mechanism:** The benchmark compares temporal explanation methods for audio classifiers and uses the annotations to expose spurious correlations.
- **Mathematical idea:** Time-localized overlap turns an explanation into a measurable alignment problem; the proxy is useful but is not a causal proof of model reasoning.
- **What the paper reports:** The paper reports near-perfect explanations for some methods and shows their use in finding spurious correlations.
- **Limits:** Event annotations, task type, explanation method, and proxy definition bound the claim; faithfulness under distribution shift remains open.

## 20. Exploring Linear Variant Transformers and k-NN Memory Inference for Long-Form ASR

**Paper:** [Exploring Linear Variant Transformers and k-NN Memory Inference for Long-Form ASR](https://www.isca-archive.org/interspeech_2025/carvalho25_interspeech.html)
**Taxonomy:** `evaluation-deployment-and-consequence / metric-and-human-targets / word-error-versus-understanding`
**Evidence:** D3 full-paper capture; PDF SHA-256 `2f4aa4cc89fdc990e1c46383a4c23cdd228f92f5d5547c3e1263c8acdc99c58b`; full-text SHA-256 `e0c75cb360c98a5728e90d58a81c7a1bd88c5c10f582dfbb84b9165212f1271d`.

- **Ordinary problem:** A recognizer must process long recordings without making attention cost grow too quickly or forgetting what happened earlier.
- **Why it is hard:** Short-form transformer success does not guarantee tractable long-form decoding, and a model with local efficiency may lose useful distant context.
- **Naive attempt:** Apply ordinary quadratic self-attention to the entire recording or split it into chunks and discard cross-chunk memory.
- **Central move:** Compare linear-time sequence architectures and add a non-trained nearest-neighbor memory that retrieves useful earlier representations during inference.
- **Mechanism:** Fastformer, SummaryMixing, BiMamba, and E-Branchformer variants are evaluated on a new LibriHeavy long-form benchmark; KNN-MAN is added to encoder-decoder models.
- **Mathematical idea:** Long-form recognition is a time-scale and memory problem: architecture controls cost while retrieval supplies selected history; WER across duration scales tests the tradeoff.
- **What the paper reports:** The paper reports a reduction from 18.8% to 17.5% WER on its LibriSpeech long-form test-clean example with BiMamba and KNN-MAN.
- **Limits:** Benchmark construction, duration distribution, memory retrieval, architectures, and WER bound the result; a single long-form corpus does not establish general conversation robustness.

## 21. Spectrotemporal Modulation: Efficient and Interpretable Feature Representation for Classifying Speech, Music, and Environmental Sounds

**Paper:** [Spectrotemporal Modulation: Efficient and Interpretable Feature Representation for Classifying Speech, Music, and Environmental Sounds](https://www.isca-archive.org/interspeech_2025/chang25b_interspeech.html)
**Taxonomy:** `evaluation-deployment-and-consequence / metric-and-human-targets / quality-and-naturalness`
**Evidence:** D3 full-paper capture; PDF SHA-256 `6cf894bc764d0acbf209e6d7067231534b44b64b7f607ee9a6198f6c301c1e54`; full-text SHA-256 `2ea227f545470aec787b9cd1aa21a5fbaf2b648eb430360aaa73a94df0ef6ea0`.

- **Ordinary problem:** A machine-listening representation should reveal which changing time-frequency patterns distinguish speech, music, and environmental sound without requiring a huge opaque model.
- **Why it is hard:** Large pretrained networks can classify well while hiding which acoustic structures mattered and consuming substantial computation.
- **Naive attempt:** Use a large pretrained embedding and treat its internal features as the explanation.
- **Central move:** Represent sound with spectrotemporal modulation patterns motivated by auditory processing, then compare a compact unpretrained classifier with pretrained audio networks.
- **Mechanism:** STM features are used for naturalistic speech, music, and environmental sound classification without pretraining.
- **Mathematical idea:** The representation describes joint rates of spectral and temporal change; classification performance and feature interpretability test whether a structured signal account can compete with learned scale.
- **What the paper reports:** The STM-based model reaches performance comparable to pretrained audio DNNs across the tested categories while remaining interpretable and efficient.
- **Limits:** Tasks, datasets, modulation parameters, baselines, and definition of interpretability bound the claim; comparable accuracy does not prove a match to human auditory cortex.

## 22. Towards LLM-Empowered Fine-Grained Speech Descriptors for Explainable Emotion Recognition

**Paper:** [Towards LLM-Empowered Fine-Grained Speech Descriptors for Explainable Emotion Recognition](https://www.isca-archive.org/interspeech_2025/chen25i_interspeech.html)
**Taxonomy:** `evaluation-deployment-and-consequence / metric-and-human-targets / calibration-and-selective-use`
**Evidence:** D3 full-paper capture; PDF SHA-256 `b2a932ff542c69ea79a51f11b23961e4b7329b1fc960a12d0b938598a90adc52`; full-text SHA-256 `1363508bfb3e4934a56ce5ff872481eaee6808c0108919cd6bf7caf74d60c5f7`.

- **Ordinary problem:** An emotion recognizer should say which speech cues led to its decision, not only output an emotion label from an opaque embedding.
- **Why it is hard:** Descriptors such as pitch, tone, and emphasis are fine-grained and entangled with linguistic content; forcing explanations can lower useful information unless the representation is controlled.
- **Naive attempt:** Use a large speech embedding as an emotion classifier and generate an explanation after the fact.
- **Central move:** Disentangle speech-emotion descriptors from HuBERT features with alternating LLM fine-tuning, ASR and descriptor tasks, and an information-bottleneck VAE.
- **Mechanism:** The paper proposes LLM-empowered fine-grained descriptors for explainable speech emotion recognition.
- **Mathematical idea:** Explanation is made an intermediate prediction problem: the system must identify acoustically meaningful factors while retaining enough information for the emotion decision.
- **What the paper reports:** On IEMOCAP and MELD, the paper reports up to 4.0 and 3.7 absolute UAR gains over the relevant baselines and presents descriptors as explanations.
- **Limits:** Datasets, descriptor definitions, LLM/SSL choices, bottleneck size, and benchmark labels bound the interpretation; a predicted descriptor is not automatically a human-valid cause.

## 23. Temp4Cap: Temporally-aligned Automated Audio Captioning

**Paper:** [Temp4Cap: Temporally-aligned Automated Audio Captioning](https://www.isca-archive.org/interspeech_2025/choi25_interspeech.html)
**Taxonomy:** `evaluation-deployment-and-consequence / metric-and-human-targets / word-error-versus-understanding`
**Evidence:** D3 full-paper capture; PDF SHA-256 `f41e758ff7c100ca0353682a2a82c952127cb29695199228fa75b9003c0f3cac`; full-text SHA-256 `76f95ae0717c525ed67d97467935f3efff95f0b6a46e26bbf6148ce8d844f9f3`.

- **Ordinary problem:** A caption for a sound scene should say not only what happened but when events occurred and in what order.
- **Why it is hard:** A bag of detected events can produce a plausible sentence with the wrong temporal relation; negative examples must challenge both event identity and event ordering.
- **Naive attempt:** Generate a caption from pooled audio features or attach an independent event detector after caption generation.
- **Central move:** Train temporal alignment directly with contrastive learning, using language-model temporal captions and event/order shuffling plus substitutions as negatives.
- **Mechanism:** Temp4Cap is a temporally aligned automated audio-captioning framework.
- **Mathematical idea:** Meaning includes relations among events: the system must learn that ‘before,’ overlap, and after are structural constraints, not decorative words added after recognition.
- **What the paper reports:** On Clotho and AudioCaps, the paper reports gains in captioning metrics and temporal metrics over the compared systems.
- **Limits:** Datasets, generated temporal captions, negative-sampling design, caption metrics, and temporal scoring bound the claim; metric gains do not ensure every relation is correctly grounded.

## 24. Enhancing Retrieval-Augmented Audio Captioning with Generation-Assisted Multimodal Querying and Progressive Learning

**Paper:** [Enhancing Retrieval-Augmented Audio Captioning with Generation-Assisted Multimodal Querying and Progressive Learning](https://www.isca-archive.org/interspeech_2025/choi25f_interspeech.html)
**Taxonomy:** `evaluation-deployment-and-consequence / metric-and-human-targets / calibration-and-selective-use`
**Evidence:** D3 full-paper capture; PDF SHA-256 `5768e141e17165509b5feae75a1c6676bb0aeec7547fbbeda4b7f9eebcdb935f`; full-text SHA-256 `744053faf5c93474930a7271c50af382762fed1a832085db00abc95c44b5a2bb`.

- **Ordinary problem:** An audio retrieval system should return evidence that matches what the sound means, not merely a caption that resembles the query in one representation.
- **Why it is hard:** Audio and text similarities can disagree: a caption may share words with the query while the retrieved audio is wrong, or vice versa. A generated textual description can also introduce errors before retrieval.
- **Naive attempt:** Retrieve only by audio embedding similarity or generate a caption and use it as the sole query, without checking whether audio and text evidence point to the same item.
- **Central move:** Generate a caption for the query audio, retrieve with a weighted combination of audio-to-audio and text-to-text similarity, and progressively train the model with interleaved audio-text examples.
- **Mechanism:** MQ-Cap trains a connector and LoRA parameters with a cross-entropy loss over interleaved pairs. It first retrieves 25 candidates by audio similarity, then combines normalized Laion-CLAP audio and text similarities with alpha 0.5. WavCaps, AudioCaps, and Clotho provide training and knowledge-base data.
- **Mathematical idea:** The pair score is S = alpha S_A + (1-alpha) S_T. On AudioCaps, MQ-Cap reports SPIDEr 0.519; on Clotho, 0.319; generation-assisted querying raises cross-modal retrieval R@1 from 44.0 to 45.3 for Laion-CLAP and from 56.0 to 59.1 for OmniBind on AudioCaps. The generated text is an intermediate measurement, not ground truth.
- **What the paper reports:** Progressive learning plus generation-assisted querying improves the reported captioning scores and gives up to 3.1 percentage points of retrieval improvement; the method adds about 1.07 seconds of generation overhead to retrieval.
- **Limits:** The benchmarks are AudioCaps, Clotho, and Auto-ACD with overlapping-source controls and missing test audio; retrieval quality depends on the generated caption and CLAP encoders. Results are author-reported and were not independently reproduced.

## 25. Multivariate Probabilistic Assessment of Speech Quality

**Paper:** [Multivariate Probabilistic Assessment of Speech Quality](https://www.isca-archive.org/interspeech_2025/cumlin25_interspeech.html)
**Taxonomy:** `evaluation-deployment-and-consequence / metric-and-human-targets / quality-and-naturalness`
**Evidence:** D3 full-paper capture; PDF SHA-256 `3c57bbf2a98b5538bd29deac09883d832a0f0341a3aa8a5b8d5fb54627308f03`; full-text SHA-256 `7788af81695b7de4c47036d0c938f870a79dea391ba7f2739cc9361f427905f6`.

- **Ordinary problem:** A speech-quality score should say not only that an utterance is poor but whether noise, coloration, discontinuity, or loudness caused the problem.
- **Why it is hard:** A single mean-opinion score hides different defects and cannot express uncertainty or relationships among them.
- **Naive attempt:** Predict MOS alone with a point estimator.
- **Central move:** Model MOS and four diagnostic quality dimensions jointly as a multivariate probability distribution.
- **Mechanism:** The model predicts a multivariate Gaussian through Cholesky factors and extends probabilistic affine transformations on NISQA ratings.
- **Mathematical idea:** The mean gives a point estimate, covariance gives uncertainty and correlations, and the NISQA dimensions provide a structured target instead of one scalar.
- **What the paper reports:** The paper reports state-of-the-art-level point estimation while uniquely providing uncertainty and cross-dimension correlation estimates.
- **Limits:** The result is bounded to NISQA's labels and distributional assumptions; whether listeners and engineers benefit in new codecs or languages remains open.

## 26. Non-intrusive Speech Quality Assessment with Diffusion Models Trained on Clean Speech

**Paper:** [Non-intrusive Speech Quality Assessment with Diffusion Models Trained on Clean Speech](https://www.isca-archive.org/interspeech_2025/deoliveira25_interspeech.html)
**Taxonomy:** `evaluation-deployment-and-consequence / metric-and-human-targets / quality-and-naturalness`
**Evidence:** D3 full-paper capture; PDF SHA-256 `bf09f7a53de81408d740632db4ecec17e99055e12d07ed00e340b68dab8da589`; full-text SHA-256 `701c69be40d680d81691d4c55fa00fd28f8a40b5c3ab303807bb50c16784add0`.

- **Ordinary problem:** A speech-quality monitor should judge a recording without a clean reference and without requiring labeled examples for every new condition.
- **Why it is hard:** Quality is a distance from acceptable clean speech, but a density model can mistake unusual yet good speech for bad speech and may inherit the biases of its clean training set.
- **Naive attempt:** Use a reference recording, train a supervised quality regressor with labels, or rely on a waveform statistic unrelated to perception.
- **Central move:** Train an unconditional diffusion model only on clean speech and use the likelihood of a deterministically noised input as an unsupervised quality score.
- **Mechanism:** The paper uses diffusion-model density estimation for non-intrusive speech-quality assessment.
- **Mathematical idea:** Quality is framed as compatibility with a learned distribution of clean speech: the score is a prior-based anomaly measure, not a direct measurement of every perceptual defect.
- **What the paper reports:** The proposed log-likelihood correlates with intrusive metrics and showed the strongest correlation with human scores in the reported listening experiment.
- **Limits:** Clean-speech corpus, diffusion schedule, likelihood proxy, reference metrics, listeners, and distortion types bound the claim; low likelihood can mean unfamiliarity rather than poor quality.

## 27. Beyond Similarity Scoring: Detecting Entailment and Contradiction in Multilingual and Multimodal Contexts

**Paper:** [Beyond Similarity Scoring: Detecting Entailment and Contradiction in Multilingual and Multimodal Contexts](https://www.isca-archive.org/interspeech_2025/istaiteh25_interspeech.html)
**Taxonomy:** `evaluation-deployment-and-consequence / metric-and-human-targets / word-error-versus-understanding`
**Evidence:** D3 full-paper capture; PDF SHA-256 `2018859381e94231bbca68b57be09073b7dfee9d176cc3f1c76bdf0640e18ed7`; full-text SHA-256 `192a4167737bc4b53af3c8973e5cfcc24b32a05aa060a0fe995f1ab57670cd0a`.

- **Ordinary problem:** A translation or spoken answer can sound similar to a source while quietly changing or contradicting its meaning.
- **Why it is hard:** Similarity rewards shared words or embeddings but does not distinguish agreement, contradiction, and unrelated content.
- **Naive attempt:** Score overlap and call a high similarity score faithful.
- **Central move:** Classify the logical relation between speech and text or between two speech segments as entailment, contradiction, or neutral across languages and modalities.
- **Mechanism:** Speech-text, text-speech, and speech-speech pairs are added to a multilingual inference framework and compared with similarity-based BLASER evaluation.
- **Mathematical idea:** The target is a three-way relation, not a continuous closeness score; F1 measures whether the evaluator detects meaning-preserving and meaning-changing pairs.
- **What the paper reports:** The paper reports F1 gains of 0.19 for speech-speech and 0.13 for speech-text over BLASER in distinguishing entailment from non-entailment.
- **Limits:** Languages, pair construction, translations, labels, and evaluation sets bound the result; logical classification does not guarantee complete translation assessment or human usefulness.

## 28. AttentiveMOS: A Lightweight Attention-Only Model forSpeech Quality Prediction

**Paper:** [AttentiveMOS: A Lightweight Attention-Only Model forSpeech Quality Prediction](https://www.isca-archive.org/interspeech_2025/kibria25_interspeech.html)
**Taxonomy:** `evaluation-deployment-and-consequence / metric-and-human-targets / quality-and-naturalness`
**Evidence:** D3 full-paper capture; PDF SHA-256 `d1987ba4d40a52b4d88c2833b75a97a9a16e9ccbc06c6642b7827755e9fe33f8`; full-text SHA-256 `7735889fab97ee61530ae0d96e96bcb34d07b95ab7b9befb7a18195069f673a9`.

- **Ordinary problem:** A quality predictor should approximate what listeners hear without requiring a listening test for every utterance.
- **Why it is hard:** Ratings are noisy, quality depends on local defects and whole-utterance context, and large encoders make prediction impractical.
- **Naive attempt:** Train a large model on MOS labels and treat every listener score as equally reliable.
- **Central move:** Use attention for local and global context in a small model, then sequentially teach it from refined targets to reduce noisy-rating effects.
- **Mechanism:** AttentiveMOS uses Swin and transformer attention with 86K parameters and is evaluated across in-domain, out-of-domain, and cross-domain MOS datasets.
- **Mathematical idea:** MSE measures rating error while Pearson and Spearman measure agreement; SOMOS-clean reports MSE 0.257, PCC 0.449, and SRCC 0.442.
- **What the paper reports:** It beats listed lightweight baselines in the reported SOMOS-clean comparison, but PCC falls to 0.359 on out-of-domain LIVETALK.
- **Limits:** MOS labels, listener composition, dataset domains, and the sharp shift drop limit claims of general quality assessment.

## 29. Enabling the replicability of speech synthesis perceptual evaluations

**Paper:** [Enabling the replicability of speech synthesis perceptual evaluations](https://www.isca-archive.org/interspeech_2025/lemaguer25_interspeech.html)
**Taxonomy:** `evaluation-deployment-and-consequence / metric-and-human-targets / quality-and-naturalness`
**Evidence:** D3 full-paper capture; PDF SHA-256 `9fdd05d1afa7c4b2130d4c985f98ef144c586642094bab6342a45db5b835a068`; full-text SHA-256 `bd744a53f4bbb943b1081f9c14e05e6f05bc6b42d724f7376fcd4cb1a0c20af3`.

- **Ordinary problem:** A speech-synthesis listening claim should be inspectable and repeatable, not just summarized by one MOS number.
- **Why it is hard:** Subjective results depend on stimuli, participants, protocol, anchors, randomization, analysis, and reporting choices.
- **Naive attempt:** Report a mean listener score and assume reproducibility because the model and samples are named.
- **Central move:** Decompose evaluation into a structured report and a recipe containing materials and decisions needed to repeat it.
- **Mechanism:** Audit the goal, dataset and bias, participant cohort, protocol, analysis, conclusions, and limitations, then package evaluation assets and procedures.
- **Mathematical idea:** The central object is an auditable mapping from hypothesis to stimuli, ratings, uncertainty, and conclusion.
- **What the paper reports:** The paper reports a structured template intended to make subjective speech-synthesis studies more reproducible and limitations more visible.
- **Limits:** A checklist cannot guarantee participant representativeness, perceptual validity, or exact replication when access differs.

## 30. Voice Quality Dimensions as Interpretable Primitives for Speaking Style for Atypical Speech and Affect

**Paper:** [Voice Quality Dimensions as Interpretable Primitives for Speaking Style for Atypical Speech and Affect](https://www.isca-archive.org/interspeech_2025/narain25_interspeech.html)
**Taxonomy:** `evaluation-deployment-and-consequence / metric-and-human-targets / quality-and-naturalness`
**Evidence:** D3 full-paper capture; PDF SHA-256 `1aff853df83c70d430c29e2a2733921dca23eccc0900436d0d4a6aaa3cb463b7`; full-text SHA-256 `fa80374a2a8715b9f4cc831efc76631a88decb25be87d466dd437a932b22f9e3`.

- **Ordinary problem:** A speech system needs interpretable estimates of atypical voice qualities such as breathiness, monopitch, or imprecise consonants.
- **Why it is hard:** A single embedding score compresses distinct perceptual failures and may not generalize across speakers, elicitation tasks, languages, or disorders.
- **Naive attempt:** Train one opaque quality regressor and call its correlation with a rating a complete account of speech accessibility.
- **Central move:** Train separate probes for seven voice-quality dimensions on frozen speech representations, then test cross-category and zero-shot transfer.
- **Mechanism:** The frozen representation supplies a common acoustic space while lightweight probes map it to interpretable dimensions; held-out speakers and out-of-domain datasets test transfer.
- **Mathematical idea:** Factorizing a human judgment into named dimensions makes the target inspectable, but each probe still inherits annotation and distribution assumptions.
- **What the paper reports:** The paper reports strong probe performance and generalization on SAP categories, with zero-shot tests on additional languages, tasks, and affect data.
- **Limits:** Proxy labels, speaker/sample overlap, limited out-of-domain sets, frozen-encoder choice, and correlation metrics bound transfer; dimensional prediction is not a clinical or listener-outcome validation.

## 31. Multimodal and Multitask Learning for Predicting Multiple Scores in L2 English Speech

**Paper:** [Multimodal and Multitask Learning for Predicting Multiple Scores in L2 English Speech](https://www.isca-archive.org/interspeech_2025/oh25_interspeech.html)
**Taxonomy:** `evaluation-deployment-and-consequence / metric-and-human-targets / calibration-and-selective-use`
**Evidence:** D3 full-paper capture; PDF SHA-256 `6e7efb566846da1e172e14e92b79e181fa40b88bec0b388604ffd7ca26065285`; full-text SHA-256 `81d630f891c459cd987d0b81fb17c412868d4df718c77f17a0ae734ba603e781`.

- **Ordinary problem:** An assessment system should predict several aspects of second-language speaking ability while respecting that speech and words reveal different parts of performance.
- **Why it is hard:** A single score hides trait differences, while simply concatenating audio and text features can make one modality dominate or ignore relationships among traits.
- **Naive attempt:** Train one unimodal predictor or combine embeddings without modeling how the traits depend on each other.
- **Central move:** Use cross-modal attention to exchange information between speech and text and a joint loss that treats the five proficiency traits as related but distinct targets.
- **Mechanism:** MFCC, wav2vec 2.0, GloVe, and BERT embeddings are compared on five L2 English scores with a trait-aware loss and mean Pearson correlation as the main measure.
- **Mathematical idea:** The prediction target is a vector of human-assigned traits; cross-modal attention and the joint loss encode dependencies that a single aggregate score discards.
- **What the paper reports:** The wav2vec 2.0 plus BERT configuration reports the best mean PCC, 0.734 with standard deviation 0.0129 across the five criteria, above unimodal and baseline multimodal systems.
- **Limits:** The learner dataset, rubric, rater scores, split, and correlation metric bound the result; correlation is not agreement or evidence that the model understands proficiency.

## 32. Aligning ASR Evaluation with Human and LLM Judgments: Intelligibility Metrics Using Phonetic, Semantic, and NLI Approaches

**Paper:** [Aligning ASR Evaluation with Human and LLM Judgments: Intelligibility Metrics Using Phonetic, Semantic, and NLI Approaches](https://www.isca-archive.org/interspeech_2025/phukon25_interspeech.html)
**Taxonomy:** `evaluation-deployment-and-consequence / metric-and-human-targets / word-error-versus-understanding`
**Evidence:** D3 full-paper capture; PDF SHA-256 `7b5c6cfb08740ebcd12251672aca9347d6b4d199359b3fe7f37e9f87b5f96f08`; full-text SHA-256 `7b0087ed036d280d3f4c8ddc9ca9798df73d96b9fd1e75a7dedf0a7100959f66`.

- **Ordinary problem:** A transcript can differ from reference words yet remain understandable, especially for disordered speech; evaluation must measure recoverable meaning.
- **Why it is hard:** WER and CER penalize harmless substitutions and can reward exact but unintelligible text.
- **Naive attempt:** Use WER as the universal speech-quality measure because it is easy to compute.
- **Central move:** Fit a metric combining natural-language inference, semantic similarity, and phonetic similarity to human ratings of ASR outputs.
- **Mechanism:** Five-fold regression learns weights from 100 transcript pairs rated by six annotators, then tests the combined score against held-out judgments.
- **Mathematical idea:** The combined metric correlates 0.890 with human judgments; weights are 0.40 NLI, 0.28 semantic, and 0.32 phonetic, with MSE 0.237.
- **What the paper reports:** The integrated measure outperforms individual and traditional error measures in the reported SAP evaluation.
- **Limits:** One dataset, six annotators, regression assumptions, and reported correlation limit other listeners, languages, and clinical decisions.

## 33. On the reliability of feature attribution methods for speech classification

**Paper:** [On the reliability of feature attribution methods for speech classification](https://www.isca-archive.org/interspeech_2025/shen25b_interspeech.html)
**Taxonomy:** `evaluation-deployment-and-consequence / metric-and-human-targets / calibration-and-selective-use`
**Evidence:** D3 full-paper capture; PDF SHA-256 `9d785cdeb27b44e907f9e9b4e81aefa37e3e086288839853c6ee3a02061b118f`; full-text SHA-256 `6483c495278279109c175ddb185260dd4f26cbe66a42b38e748357625825f701`.

- **Ordinary problem:** An explanation of a speech classifier should identify evidence that genuinely changes the decision, not merely highlight plausible-looking waveform regions.
- **Why it is hard:** Speech unfolds in time, so the reliability of an attribution depends on the input representation, the size of the perturbed region, and whether the task is word-based or acoustic.
- **Naive attempt:** Apply a standard saliency map and interpret the highlighted frames as causal evidence.
- **Central move:** Vary input type, aggregation, and perturbation timespan, then compare attribution stability, faithfulness, and agreement across speech classification tasks.
- **Mechanism:** Experiments use TIMIT and Common Voice with gradient-based saliency and integrated gradients; word-aligned and fixed-timespan perturbations are compared.
- **Mathematical idea:** Attribution is an intervention-dependent measurement; agreement and error-based scores test whether highlighted regions are reliable under controlled perturbations.
- **What the paper reports:** Standard approaches are generally unreliable in speech, except that word-aligned perturbations are more reliable for word-based classification tasks.
- **Limits:** The models, tasks, datasets, attribution methods, and reliability definitions bound the result; no explanation method becomes a causal proof from these tests alone.

## 34. Collecting, Curating, and Annotating Good Quality Speech deepfake dataset for Famous Figures: Process and Challenges

**Paper:** [Collecting, Curating, and Annotating Good Quality Speech deepfake dataset for Famous Figures: Process and Challenges](https://www.isca-archive.org/interspeech_2025/ali25_interspeech.html)
**Taxonomy:** `evaluation-deployment-and-consequence / privacy-and-security / spoofing-and-deepfake`
**Evidence:** D3 full-paper capture; PDF SHA-256 `65637a57f2597e766eb0674c6c7154a0484792611b8c2031968cd04a563f1e36`; full-text SHA-256 `7f0179db944b04e9e68681eec80ba417b5aa657003e91a7007e4b1eb8290b330`.

- **Ordinary problem:** A deepfake dataset for public figures should resemble the speech impersonation attacks people actually encounter, not merely contain clean synthetic clips.
- **Why it is hard:** Collection, segmentation, synthesis method, and speaker identity all affect how realistic a fake sounds.
- **Naive attempt:** Collect convenient speech and generate one kind of synthetic audio without checking human confusion.
- **Central move:** Build a documented pipeline for high-quality bona-fide data, transcription-based segmentation, and several synthesis regimes, then measure naturalness and confusion.
- **Mechanism:** The paper creates bona-fide and synthetic speech for ten public figures and reports NISQA-TTS and human misclassification.
- **Mathematical idea:** Dataset composition, automated naturalness, and human confusion measure different parts of realism.
- **What the paper reports:** The dataset reports NISQA-TTS naturalness 3.69 and a highest human misclassification rate of 61.9%.
- **Limits:** The ten figures, synthesis systems, listeners, and dataset protocol bound the result; new generators and adversarially chosen public speech remain open.

## 35. ATMM-SAGA: Alternating Training for Multi-Module with Score-Aware Gated Attention SASV system

**Paper:** [ATMM-SAGA: Alternating Training for Multi-Module with Score-Aware Gated Attention SASV system](https://www.isca-archive.org/interspeech_2025/asali25_interspeech.html)
**Taxonomy:** `evaluation-deployment-and-consequence / privacy-and-security / spoofing-and-deepfake`
**Evidence:** D3 full-paper capture; PDF SHA-256 `138853aa4fedc74ca28eac358602c845b325e7d6de3675b91fb6d6da57473617`; full-text SHA-256 `dfafdfd7675aefc4af6ecce6bbb015fa8762ef38b1fb2d3d2cdf5285f7d61cd2`.

- **Ordinary problem:** Decide whether a claimed speaker is the person in a test utterance while resisting impostors and confusing acoustic conditions.
- **Why it is hard:** Speaker verification must compare identity evidence while separating it from channel, content, and nuisance variation; spoofing makes a high similarity score unsafe by itself.
- **Naive attempt:** Train one speaker embedding and threshold its similarity without modeling spoof evidence or interactions among modules.
- **Central move:** Alternate training of speaker and anti-spoofing modules and use score-aware gated attention to combine their evidence.
- **Mechanism:** Speaker and spoof-related representations are produced separately, gates weight evidence according to scores, and the final decision combines identity and authenticity signals; trials measure both acceptance and rejection errors.
- **Mathematical idea:** Verification uses similarity scores and a decision threshold; gated attention learns weights over module outputs, while SASV metrics summarize target, nontarget, and spoof trial errors.
- **What the paper reports:** The paper reports an alternating multi-module SASV system with score-aware gating and evaluates it on speaker-authentication trials.
- **Limits:** Thresholds and spoof types determine operating behavior; benchmark attacks do not exhaust unseen synthesis or replay conditions. No independent reproduction was performed.

## 36. WavShape: Information-Theoretic Speech Representation Learning for Fair and Privacy-Aware Audio Processing

**Paper:** [WavShape: Information-Theoretic Speech Representation Learning for Fair and Privacy-Aware Audio Processing](https://www.isca-archive.org/interspeech_2025/baser25_interspeech.html)
**Taxonomy:** `evaluation-deployment-and-consequence / privacy-and-security / voice-privacy`
**Evidence:** D3 full-paper capture; PDF SHA-256 `ae50c2718241032f75c69a685dda667b052d47854a3bf4815fd162daf058a705`; full-text SHA-256 `383b9daf7e669fdf8e585e88798e19bb64ffef9d06c18f936beda273856938e5`.

- **Ordinary problem:** A speech embedding is useful only if it keeps information needed for the task while not exposing identity, accent, gender, or other sensitive attributes that downstream users did not authorize.
- **Why it is hard:** Removing sensitive information can also remove information a task needs, and privacy cannot be established by looking at a projection or one downstream accuracy score.
- **Naive attempt:** Compress a pretrained embedding with a generic bottleneck or train a classifier adversarially without measuring how much information about each attribute remains.
- **Central move:** Optimize mutual information in two directions: reduce dependence between the public embedding and sensitive labels while retaining dependence with task labels and the original speech representation.
- **Mechanism:** A frozen speech encoder produces embeddings, a trainable WavShape projection creates public embeddings, and a Donsker–Varadhan mutual-information estimator supplies the training signal. The estimator is removed at inference; downstream classifiers and information estimates test sensitive leakage and task retention across three datasets.
- **Mathematical idea:** The objective is a weighted combination of mutual-information terms. The Donsker–Varadhan estimator uses a log moment-generating expression to lower-bound dependence; the paper reports MI changes plus downstream task performance, so the MI estimate is a proxy for leakage rather than a proof of privacy.
- **What the paper reports:** The paper reports up to an 81% reduction in mutual information with sensitive attributes while retaining up to 97% of task-relevant information in its tested settings; on VCTK, gender-related MI falls from 0.40029 to 0.07493.
- **Limits:** Mutual-information estimation depends on the estimator, labels, datasets, and chosen sensitive attributes; unmeasured attributes or powerful attackers may still recover information. The figures are author-reported, and no independent privacy attack or reproduction was performed.

## 37. PhonemeFake: Redefining Deepfake Realism with Language-Driven Segmental Manipulation and Adaptive Bilevel Detection

**Paper:** [PhonemeFake: Redefining Deepfake Realism with Language-Driven Segmental Manipulation and Adaptive Bilevel Detection](https://www.isca-archive.org/interspeech_2025/baser25b_interspeech.html)
**Taxonomy:** `evaluation-deployment-and-consequence / privacy-and-security / spoofing-and-deepfake`
**Evidence:** D3 full-paper capture; PDF SHA-256 `94b1fe9ee7e02df9b12a5937e370e632c3d75cafe941405c97b0db7ba3ffdd3e`; full-text SHA-256 `1129c94fb0709a49f3cfe2eab3b1fe92209314a8edac89e69e19f57d0f1e498e`.

- **Ordinary problem:** A deepfake detector should face manipulations that fool people, especially when only a few speech segments are changed to alter meaning.
- **Why it is hard:** Many benchmark fakes are easier for humans to spot than real attacks, and scanning every frame wastes computation.
- **Naive attempt:** Train on broad synthetic fakes and inspect the whole recording uniformly.
- **Central move:** Use language reasoning to choose critical phoneme segments for manipulation, then detect those regions with an adaptive two-level model.
- **Mechanism:** PhonemeFake creates segmental manipulations, measures human and benchmark deception, and trains a detector that allocates computation to suspicious regions across three datasets.
- **Mathematical idea:** Equal error rate measures detection, localization checks whether manipulated regions are found, and speed measures the cost of adaptive processing.
- **What the paper reports:** The paper reports up to 42% lower human perception and 94% lower benchmark accuracy for attacks; its detector reports 91% EER reduction and up to 90% speed-up.
- **Limits:** These are author-reported results tied to attack construction, datasets, detector thresholds, and the chosen language reasoning; unseen generators and adversarial adaptation remain open.

## 38. Evaluating Parameter Sharing for Spoofing-Aware Speaker Verification: A Case Study on the ASVspoof 5 Dataset

**Paper:** [Evaluating Parameter Sharing for Spoofing-Aware Speaker Verification: A Case Study on the ASVspoof 5 Dataset](https://www.isca-archive.org/interspeech_2025/buker25_interspeech.html)
**Taxonomy:** `evaluation-deployment-and-consequence / privacy-and-security / spoofing-and-deepfake`
**Evidence:** D3 full-paper capture; PDF SHA-256 `c10f4ab95a8271f203d31b5d3ab0cc5ec5d55cf2d9f7661167314b7480b84d38`; full-text SHA-256 `b0b891cec1f42ead260e3fdf2e1ecf3b6a5ed3fc56407f01776c5d19469bbec9`.

- **Ordinary problem:** A speaker-verification system can accept the wrong person when a spoofed recording resembles the claimed speaker, so identity matching and attack detection must work together under changing codecs and attacks.
- **Why it is hard:** SASV combines two decisions—does the voice match, and is the signal genuine—and joint training can help one while harming the other; attack types and compression conditions change the balance.
- **Naive attempt:** Train an ASV verifier and a countermeasure independently, or share all parameters without testing which sharing pattern fits which attack.
- **Central move:** Systematically compare parameter-sharing strategies for the verifier and spoof countermeasure, treating sharing as an experimental variable rather than an automatic improvement.
- **Mechanism:** On ASVspoof 5, the study varies which modules share parameters and evaluates the resulting SASV systems across attack types and codec conditions, comparing min a-DCF and relative performance changes to an unshared baseline.
- **Mathematical idea:** The main decision metric is minimum tandem detection cost, which combines false acceptance and false rejection costs for speaker and spoof decisions. The method question is whether shared representations improve this joint operating tradeoff.
- **What the paper reports:** The paper reports min a-DCF improving from 0.329 to 0.233 for the A26 attack with parameter sharing and a 14.09% gain for AMR-compressed signals in the tested setup.
- **Limits:** Benefits are attack- and codec-specific; the ASVspoof 5 protocols do not exhaust future generators or deployment channels. min a-DCF is a system-level proxy, not proof of safe authentication, and no independent reproduction was performed.

## 39. Beyond Attacks: Advancing Fake Speech Detection with Attack-Agnostic Methods

**Paper:** [Beyond Attacks: Advancing Fake Speech Detection with Attack-Agnostic Methods](https://www.isca-archive.org/interspeech_2025/chandra25b_interspeech.html)
**Taxonomy:** `evaluation-deployment-and-consequence / privacy-and-security / spoofing-and-deepfake`
**Evidence:** D3 full-paper capture; PDF SHA-256 `0b35bf3ce577a82e019bbfede6746f178ac1232cd759c404812183e30321a276`; full-text SHA-256 `78d1568f75a2aa05119c1e9df4ccf9e69c9b0e67d03a04fe1c7a134edaa72b0d`.

- **Ordinary problem:** A fake-speech detector must recognize manipulation it has not seen, including changed codec, attack, and language.
- **Why it is hard:** A detector can learn a generator or recording fingerprint instead of the genuine/fake property, so in-domain scores collapse under shift.
- **Naive attempt:** Train on known attacks and treat high test accuracy as general spoofing ability.
- **Central move:** Remove attack-specific information with an attack-invariant encoder-decoder and common-subspace decomposition before classification.
- **Mechanism:** A frozen wav2vec2 front-end and AASIST backend produce embeddings; AIED suppresses attack variation and CSD projects into a shared subspace, tested on ASVspoof and IndicTTS.
- **Mathematical idea:** EER changes from 6.14 to 5.84 on LA, 12.33 to 10.90 on DF, and 59.82 to 39.51 on IndicTTS; the large cross-language gap remains.
- **What the paper reports:** The paper reports 4%, 12%, and 34% relative EER improvements on LA, DF, and IndicTTS, with ablations separating AIED and CSD.
- **Limits:** Datasets, attacks, frozen front-end, and language coverage bound the result; IndicTTS EER remains high and no independent adversarial evaluation was performed.

## 40. Codec-Based Deepfake Source Tracing via Neural Audio Codec Taxonomy

**Paper:** [Codec-Based Deepfake Source Tracing via Neural Audio Codec Taxonomy](https://www.isca-archive.org/interspeech_2025/chen25j_interspeech.html)
**Taxonomy:** `evaluation-deployment-and-consequence / privacy-and-security / spoofing-and-deepfake`
**Evidence:** D3 full-paper capture; PDF SHA-256 `c3099bd9d47415030216e865f1941dbc6322f56de2ff99307f5b688937d14e26`; full-text SHA-256 `5dd038220fb0ed16043d61a9e481c85f7f978bab997a8b321e6105a4188881ed`.

- **Ordinary problem:** Detecting fake speech says it is synthetic; tracing its source can explain which generator family produced it.
- **Why it is hard:** Codec generators share stages, so a detector can learn dataset artifacts instead of source evidence.
- **Naive attempt:** Train a binary fake detector and treat attribution as the same task with more labels.
- **Central move:** Organize neural codecs into a taxonomy and use codec-related auxiliary objectives for source tracing.
- **Mechanism:** Multi-task systems on CodecFake+ use codec quantization, auxiliary codec tasks, and balanced source-tracing experiments.
- **Mathematical idea:** F1 is reported for vector-quantization, auxiliary, and decoder/source tasks; the best cited DEC F1 is 46.45%.
- **What the paper reports:** CodecFake+ gives initial evidence that codec taxonomy helps source tracing and that balance affects generalization.
- **Limits:** The dataset and generator coverage bound the result; 46.45% F1 is not reliable attribution.

## 41. Generalizable Audio Spoofing Detection using Non-Semantic Representations

**Paper:** [Generalizable Audio Spoofing Detection using Non-Semantic Representations](https://www.isca-archive.org/interspeech_2025/das25_interspeech.html)
**Taxonomy:** `evaluation-deployment-and-consequence / privacy-and-security / spoofing-and-deepfake`
**Evidence:** D3 full-paper capture; PDF SHA-256 `eaa24777b38b4fb02ac90c59ed8cca27e81bcfc970490057d8f057cfd375e2d0`; full-text SHA-256 `b5071141ecdeecaa7ea6a11b5682fe30919d6fe567ba27632d4a64313fba5dd7`.

- **Ordinary problem:** A spoof detector should recognize synthetic audio from new generators and public-domain conditions, not only the generator seen during training.
- **Why it is hard:** Semantic embeddings can learn the message instead of the traces of synthesis, while in-domain scores can hide failure under distribution shift.
- **Naive attempt:** Optimize only on a matched generator and report one in-domain score.
- **Central move:** Use non-semantic universal audio representations and compare them with handcrafted, semantic, and end-to-end alternatives under out-of-domain tests.
- **Mechanism:** TRILL and TRILLsson representations are evaluated as features for a spoofing classifier across in-domain and public-domain conditions.
- **Mathematical idea:** The method changes what evidence the detector is allowed to use: it seeks production artifacts that survive a change in spoken content and generator.
- **What the paper reports:** The paper reports comparable in-domain performance and stronger out-of-domain results than the tested baselines.
- **Limits:** The generators, corpora, representation models, and author-reported tests define the boundary; future synthesis methods and adversarial adaptation remain open.

## 42. Can Quantized Audio Language Models Perform Zero-Shot Spoofing Detection?

**Paper:** [Can Quantized Audio Language Models Perform Zero-Shot Spoofing Detection?](https://www.isca-archive.org/interspeech_2025/dutta25b_interspeech.html)
**Taxonomy:** `evaluation-deployment-and-consequence / privacy-and-security / spoofing-and-deepfake`
**Evidence:** D3 full-paper capture; PDF SHA-256 `701c8eb0461749aed0076b23f36383c6ffc9ed975b7cc18bfda9aa46270bb0c7`; full-text SHA-256 `83d6b075f210d0334ee54316631154d6fd39df3858cf5435edc9604274c61013`.

- **Ordinary problem:** A compact audio language model should detect spoofed speech without turning every unfamiliar recording into a spoof, even after quantization for deployment.
- **Why it is hard:** Zero-shot models can have strong-looking accuracy while carrying a severe class bias; quantization changes internal precision but may not be the main failure.
- **Naive attempt:** Report aggregate accuracy on clean data and assume FP16 or INT8 preserves the task behavior.
- **Central move:** Evaluate several audio language models across spoof datasets and precisions, inspecting class bias and practical discrimination rather than accuracy alone.
- **Mechanism:** The paper tests quantized audio language models for zero-shot spoofing detection on ASVspoof2019, In-the-Wild, and WaveFake.
- **Mathematical idea:** Deployment compression and task validity are separate questions: a model may retain its behavior after quantization while that behavior is already a biased near-random decision rule.
- **What the paper reports:** The paper reports negligible FP16 degradation but severe spoof-prediction bias that undermines practical detection.
- **Limits:** Models, datasets, thresholds, quantization methods, and zero-shot prompts bound the claim; tested robustness is not security certification.

## 43. Audio Deepfake Source Tracing using Multi-Attribute Open-Set Identification and Verification

**Paper:** [Audio Deepfake Source Tracing using Multi-Attribute Open-Set Identification and Verification](https://www.isca-archive.org/interspeech_2025/falez25_interspeech.html)
**Taxonomy:** `evaluation-deployment-and-consequence / privacy-and-security / spoofing-and-deepfake`
**Evidence:** D3 full-paper capture; PDF SHA-256 `4e392a8ff807c3471467dc810875478aba594ddc69b70e1d674a9331e1f8e7e6`; full-text SHA-256 `8914e2ace1c5cf19d2db99cf073f784531a80a585defe3517489ee1f7f64a342`.

- **Ordinary problem:** A detector should say where a fake voice came from, not only that it sounds fake.
- **Why it is hard:** Open-set generators and new vocoders create sources not seen during training, and a binary label cannot explain origin.
- **Naive attempt:** Train a binary real/fake classifier and treat its confidence as source identity.
- **Central move:** Define few-shot identification and verification protocols that trace a generator or one of its components under open-set conditions.
- **Mechanism:** Models are trained on internal and MLAAD data and evaluated across three ASVspoof sets, MLAAD, and Blizzard23.
- **Mathematical idea:** Identification asks which source class matches a few references; verification asks whether a claimed source is supported, making the decision object explicit.
- **What the paper reports:** The paper reports discrimination of unseen source attributes and argues for a standardized source-tracing ontology.
- **Limits:** Datasets, source taxonomy, reference count, and generator families bound the result; real-world provenance and adversarial adaptation remain open.

## 44. Rehearsal with Auxiliary-Informed Sampling for Audio Deepfake Detection

**Paper:** [Rehearsal with Auxiliary-Informed Sampling for Audio Deepfake Detection](https://www.isca-archive.org/interspeech_2025/febrinanto25_interspeech.html)
**Taxonomy:** `evaluation-deployment-and-consequence / privacy-and-security / spoofing-and-deepfake`
**Evidence:** D3 full-paper capture; PDF SHA-256 `e7c8f80a9dce5915880b52224a96390ec7edfdc489821c7023125208a625d0f3`; full-text SHA-256 `831eb132a8a69f650cc6adbfe5f0dd3f7fbd2937619e652457861eebdc95079a`.

- **Ordinary problem:** A deepfake detector must learn new attack types while remembering older ones, even when its memory buffer can hold only a small sample of past audio.
- **Why it is hard:** Uniform rehearsal misses rare acoustic characteristics and can make the buffer biased toward easy or common examples.
- **Naive attempt:** Store random old clips or retrain from scratch whenever a new attack appears.
- **Central move:** Generate auxiliary labels describing audio characteristics and use them to sample a more diverse rehearsal memory during continual learning.
- **Mechanism:** RAIS uses auxiliary-informed sampling for rehearsal-based continual audio-deepfake detection.
- **Mathematical idea:** The memory is selected for coverage of acoustic factors, not only class labels; retaining varied evidence helps the detector update without collapsing onto the newest attack.
- **What the paper reports:** The paper reports improved continual deepfake detection over rehearsal baselines on new attacks.
- **Limits:** Attack families, auxiliary-label quality, buffer size, stream order, and detector threshold bound the result; no finite memory guarantees future attack coverage.

## 45. STOPA: A Dataset of Systematic VariaTion Of DeePfake Audio for Open-Set Source Tracing and Attribution

**Paper:** [STOPA: A Dataset of Systematic VariaTion Of DeePfake Audio for Open-Set Source Tracing and Attribution](https://www.isca-archive.org/interspeech_2025/firc25_interspeech.html)
**Taxonomy:** `evaluation-deployment-and-consequence / privacy-and-security / spoofing-and-deepfake`
**Evidence:** D3 full-paper capture; PDF SHA-256 `dd58fcc8c8640443823b0117bd40e7fc848574506ec17a2b32842b5f6ce3cd84`; full-text SHA-256 `af2b7fd19361a348e4fb5d9d612b7e4971f0784fc92dc166ea75b7389ec003a3`.

- **Ordinary problem:** A deepfake detector should trace and attribute new attack sources, including attacks not represented in training, rather than only say real or fake.
- **Why it is hard:** Open-set attacks change synthesis methods and acoustic traces; a dataset can accidentally reward memorizing a generator or speaker instead of identifying source behavior.
- **Naive attempt:** Train a closed-set binary classifier and evaluate it only on familiar fake types.
- **Central move:** Build systematic variations of deepfake audio with source labels and evaluate open-set detection, tracing, and attribution separately.
- **Mechanism:** STOPA is a dataset of systematic variation of deepfake audio for open-set source tracing and attribution.
- **Mathematical idea:** The task is a structured forensic inference problem: detection asks whether an item is fake, while tracing asks which generating process explains it under variation.
- **What the paper reports:** The paper reports dataset resources and benchmark behavior for open-set deepfake source tracing and attribution.
- **Limits:** Generator coverage, perturbations, speakers, labels, and open-set split design bound the result; benchmark attribution is not courtroom-grade provenance.

## 46. LitMAS: A Lightweight and Generalized Multi-Modal Anti-Spoofing Framework for Biometric Security

**Paper:** [LitMAS: A Lightweight and Generalized Multi-Modal Anti-Spoofing Framework for Biometric Security](https://www.isca-archive.org/interspeech_2025/gorthi25_interspeech.html)
**Taxonomy:** `evaluation-deployment-and-consequence / privacy-and-security / spoofing-and-deepfake`
**Evidence:** D3 full-paper capture; PDF SHA-256 `bdebf2a582709e76c75b04735c62e0c719a6378d7a1231e463f204c29f8d5e6b`; full-text SHA-256 `71e9caca3aa6c7939da79f3d8dc283d3f941812736f8ee49cd293b38132a85a9`.

- **Ordinary problem:** Biometric anti-spoofing must reject attacks across modalities and conditions while staying light enough for real security systems.
- **Why it is hard:** Attack traces differ by sensor and generator, and a heavy multimodal model can be accurate but too slow or too specialized to deploy.
- **Naive attempt:** Train a modality-specific detector or use a large model and evaluate only on the attack types seen during training.
- **Central move:** Combine lightweight modality-aware representations with generalized anti-spoofing features and test cross-condition biometric security.
- **Mechanism:** LitMAS is a lightweight generalized multimodal anti-spoofing framework for biometric security.
- **Mathematical idea:** Security is a coverage problem: the model must learn signs of manipulation that survive changes in modality and attack source, while the resource budget constrains the detector itself.
- **What the paper reports:** The paper reports generalized multimodal anti-spoofing performance with a lightweight framework.
- **Limits:** Biometric modalities, attacks, datasets, fusion, thresholds, and compute budget bound the result; benchmark generalization is not security certification.

## 47. Privacy-Preserving Speaker Verification via End-to-End Secure Representation Learning

**Paper:** [Privacy-Preserving Speaker Verification via End-to-End Secure Representation Learning](https://www.isca-archive.org/interspeech_2025/hu25j_interspeech.html)
**Taxonomy:** `evaluation-deployment-and-consequence / privacy-and-security / voice-privacy`
**Evidence:** D3 full-paper capture; PDF SHA-256 `b5d720d46424d9e895ad228ff119aa34391dde79eadfbe4a91078927177cd791`; full-text SHA-256 `753cfcc3e6a235e7b8012e9ff7a2559def99287c31ce3f53cbb6c6c9b2a4602e`.

- **Ordinary problem:** Speaker verification should protect voice representations so a system can compare speakers without exposing a reusable identity embedding.
- **Why it is hard:** Verification needs a useful similarity signal, but storing or transmitting speaker information creates privacy and attack risks.
- **Naive attempt:** Encrypt storage around an ordinary embedding or remove speaker information so verification becomes impossible.
- **Central move:** Learn secure representations end to end and test the tradeoff between verification accuracy and privacy exposure.
- **Mechanism:** The paper proposes privacy-preserving speaker verification via end-to-end secure representation learning.
- **Mathematical idea:** Privacy is built into the representation rather than added only at storage: the learned object should support the authorized comparison while limiting what an observer can recover.
- **What the paper reports:** The paper reports privacy and speaker-verification results for the proposed secure representation learning method.
- **Limits:** Threat model, attacker access, datasets, privacy measure, calibration, and deployment protocol bound the claim; benchmark privacy is not a complete security proof.

## 48. CBA: Backdoor Attack on Deep Speech Classification via Audio Compression

**Paper:** [CBA: Backdoor Attack on Deep Speech Classification via Audio Compression](https://www.isca-archive.org/interspeech_2025/huang25b_interspeech.html)
**Taxonomy:** `evaluation-deployment-and-consequence / privacy-and-security / spoofing-and-deepfake`
**Evidence:** D3 full-paper capture; PDF SHA-256 `01ec7cdee9a7d860249fcecd0789a78dff0bf80ed800449cc39941b8416ace08`; full-text SHA-256 `ecdc0e566136380d64b363903a2ffa7f0c311c4c9b3ab7e3ff85fe69e61b1e97`.

- **Ordinary problem:** A speech classifier can be compromised by a hidden trigger in compressed audio, causing a targeted wrong label while ordinary tests still look normal.
- **Why it is hard:** Compression changes the waveform and may hide or reveal trigger patterns; an attacker wants the backdoor to survive the front-end while avoiding detection.
- **Naive attempt:** Test clean accuracy only or assume compression destroys every malicious perturbation.
- **Central move:** Demonstrate and analyze a backdoor attack on deep speech classification through audio compression, including its clean-task and triggered behavior.
- **Mechanism:** CBA studies a backdoor attack on deep speech classification via audio compression.
- **Mathematical idea:** The front-end becomes part of the attack surface: a transformation assumed to be harmless can carry a trigger that changes the classifier's decision.
- **What the paper reports:** The paper reports attack success and clean-task behavior for the tested compression-based backdoor.
- **Limits:** Model, compression, trigger, target class, defenses, and threat model bound the claim; one attack does not establish universal vulnerability.

## 49. From Sharpness to Better Generalization for Speech Deepfake Detection

**Paper:** [From Sharpness to Better Generalization for Speech Deepfake Detection](https://www.isca-archive.org/interspeech_2025/huang25e_interspeech.html)
**Taxonomy:** `evaluation-deployment-and-consequence / privacy-and-security / spoofing-and-deepfake`
**Evidence:** D3 full-paper capture; PDF SHA-256 `1f3bedd0a4a47b9dc759e9a610c67464502349dbf7e4fb107c8d7ce4f90f98c9`; full-text SHA-256 `e33ef70ffc9a10967f0b8c56e544b72c6ab2e17b0e9471f942fa8d5867b39eb9`.

- **Ordinary problem:** A speech deepfake detector should generalize to unseen generators and conditions rather than becoming sharp only on the training attacks.
- **Why it is hard:** Sharp decision boundaries can fit artifacts specific to known generators; improving training fit may reduce performance when the attack distribution changes.
- **Naive attempt:** Optimize closed-set accuracy and assume a sharper classifier is more discriminative under every attack.
- **Central move:** Study how sharpness relates to deepfake-detector generalization and use training changes that improve the boundary's transfer to unseen attacks.
- **Mechanism:** The paper studies moving from sharpness to better generalization for speech deepfake detection.
- **Mathematical idea:** Generalization depends on the geometry of the learned boundary, not just its training margin; the relevant test is behavior on new attack sources.
- **What the paper reports:** The paper reports deepfake-detection generalization results linked to sharpness and the proposed training approach.
- **Limits:** Attack types, datasets, sharpness measure, training recipe, and open-set split bound the claim; no benchmark proves future attack coverage.

## 50. ``Alexa, can you forget me?'' Machine Unlearning Benchmark in Spoken Language Understanding

**Paper:** [``Alexa, can you forget me?'' Machine Unlearning Benchmark in Spoken Language Understanding](https://www.isca-archive.org/interspeech_2025/koudounas25c_interspeech.html)
**Taxonomy:** `evaluation-deployment-and-consequence / privacy-and-security / voice-privacy`
**Evidence:** D3 full-paper capture; PDF SHA-256 `b1ec8aa661e9eed6b517836026a92fbf14bcf364f70a5a35a3da838c894cbb26`; full-text SHA-256 `ac0823d50a22325ba810f0ae845a50473ebe71a35a1a4ab190cb2b6892693396`.

- **Ordinary problem:** A speaker may ask a spoken-language-understanding service to forget their training examples without destroying the service for everyone else.
- **Why it is hard:** Removing files is not enough because model parameters retain influence; forgetting must be measured against efficacy, retained utility, and computation across languages and architectures.
- **Naive attempt:** Delete the records and assume the trained model has forgotten, or retrain from scratch for every request.
- **Central move:** Define forget and retain speaker sets, compare eight machine-unlearning methods against a gold model trained without the forget set, and evaluate both what is forgotten and what remains useful.
- **Mechanism:** The benchmark treats unlearning as producing a model close to the retain-only gold model. Metrics include test and forget-set F1, membership-inference attack behavior, generalization, and speedup, making the trade-off explicit.
- **Mathematical idea:** Consent becomes a measurable model-state constraint rather than a checkbox: a deletion request is successful only if identity-linked influence is reduced without unacceptable loss of spoken intent recognition.
- **What the paper reports:** The paper benchmarks four datasets in four languages, two speech encoders per dataset, and eight unlearning methods; it shows that no single method dominates all efficacy, utility, and efficiency axes.
- **Limits:** Benchmark identities and intent tasks are proxies for real consent, attack strength and gold-model assumptions matter, and unlearning guarantees do not establish that every downstream copy or generated artifact is withdrawn.

## 51. LRBA: Stealthy Backdoor Attacks on Speech Classification via Latent Rearrangement in VITS

**Paper:** [LRBA: Stealthy Backdoor Attacks on Speech Classification via Latent Rearrangement in VITS](https://www.isca-archive.org/interspeech_2025/li25aa_interspeech.html)
**Taxonomy:** `evaluation-deployment-and-consequence / privacy-and-security / spoofing-and-deepfake`
**Evidence:** D3 full-paper capture; PDF SHA-256 `0c7f4c4c5d77abc44a6a7bbc1bf134c56359f8cc26cab75ec975a53189501088`; full-text SHA-256 `e8e7a6681a29e0f46dee2b482ef8f3192bef323e912a262f7af1809b6757a0c1`.

- **Ordinary problem:** A speech classifier can be made to behave normally on ordinary inputs while an attacker causes a chosen label when a hidden manipulation is present.
- **Why it is hard:** A visible poisoned sound is easy to notice, but an attack hidden inside a learned representation can preserve apparent audio quality.
- **Naive attempt:** Assume clean-sounding audio means the classifier is safe, or search only for obvious waveform triggers.
- **Central move:** Rearrange latent representations inside a pretrained speech generator so the attack changes the target label while remaining hard to hear.
- **Mechanism:** LRBA uses the normalizing flow in VITS to create rearranged utterances and poisons a small fraction of training data for speech classification.
- **Mathematical idea:** The attack separates perceptual quality from decision integrity; attack success rate, poisoning rate, and mean-opinion score test the tradeoff.
- **What the paper reports:** The paper reports high attack success at a low poisoning rate while retaining high perceived quality and outperforming prior attacks in stealthiness.
- **Limits:** The VITS model, classifier, target labels, poisoning setup, and listener measure bound the threat; this is an attack demonstration, not evidence that every speech system is vulnerable.

## 52. Towards Machine Unlearning for Paralinguistic Speech Processing

**Paper:** [Towards Machine Unlearning for Paralinguistic Speech Processing](https://www.isca-archive.org/interspeech_2025/phukan25g_interspeech.html)
**Taxonomy:** `evaluation-deployment-and-consequence / privacy-and-security / voice-privacy`
**Evidence:** D3 full-paper capture; PDF SHA-256 `9d6381021f6a5650d751387c952b7d6faa45c5b803251da57934e33b0e02ad21`; full-text SHA-256 `e7e7ace4e12288eb477f14adc3a610fddd52fd53667a1beea8dbe26448e49f14`.

- **Ordinary problem:** A speech emotion or depression model may need to remove a person's contribution from training without rebuilding a large model from zero.
- **Why it is hard:** Paralinguistic models encode sensitive attributes, and fast forgetting can damage emotion or depression prediction utility; the best feature representation may change the unlearning trade-off.
- **Naive attempt:** Fine-tune the full model on retained data or average models without structuring which data must be forgotten.
- **Central move:** Extend SISA with weight averaging: shard the training data, retrain only affected slices, and average the surviving submodels; compare pretrained speech representations and downstream networks.
- **Mechanism:** SISA++ turns a global deletion into local retraining plus parameter aggregation. The evaluation separates forgetting performance from retained task performance and measures computational savings.
- **Mathematical idea:** The mechanism uses data partitioning as a control boundary: the model remembers where influence entered, so a request can remove a bounded subset of training history.
- **What the paper reports:** Experiments use CREMA-D speech emotion recognition and E-DAIC depression detection; the paper reports TRILLsson features with a Transformer as a robust recipe under its tested settings.
- **Limits:** The result depends on shard design, feature extractor, downstream task, attack/evaluation protocol, and access to the original training pipeline; fast unlearning is not proof of legal or social consent compliance.

## 53. Evaluating ASR Robustness to Spontaneous Speech Errors: A Study of WhisperX Using a Speech Error Database

**Paper:** [Evaluating ASR Robustness to Spontaneous Speech Errors: A Study of WhisperX Using a Speech Error Database](https://www.isca-archive.org/interspeech_2025/alderete25_interspeech.html)
**Taxonomy:** `evaluation-deployment-and-consequence / robustness-and-shift / distribution-shift`
**Evidence:** D3 full-paper capture; PDF SHA-256 `c7d3c80f0f2d9ddab4ab238b91e1f90eb1106016f792944bf2ce8f5303c69303`; full-text SHA-256 `172c8eea15de2aab1b27b5c97edcc2608a3400a6775f150a02cf56ed33da3ede`.

- **Ordinary problem:** ASR robustness should be tested on errors people actually produce, not only clean speech or synthetic noise.
- **Why it is hard:** Speech errors differ by type and position; aggregate WER hides which deviation caused failure.
- **Naive attempt:** Report one WER on spontaneous speech and treat all deviations as equivalent noise.
- **Central move:** Use annotated SFUSED speech errors to stratify WhisperX performance by error type and word position.
- **Mechanism:** The study evaluates sound and word errors with controlled classification variables and compares initial, medial, and final positions.
- **Mathematical idea:** Accuracy by error class and position reveals interactions; sound errors are reported as easier than word errors.
- **What the paper reports:** Sound errors have higher transcription accuracy than word errors, with position-dependent differences.
- **Limits:** Database, annotations, WhisperX, language, and task design limit generalization.

## 54. Defending Speech-enabled LLMs Against Adversarial Jailbreak Threats

**Paper:** [Defending Speech-enabled LLMs Against Adversarial Jailbreak Threats](https://www.isca-archive.org/interspeech_2025/alexos25_interspeech.html)
**Taxonomy:** `evaluation-deployment-and-consequence / robustness-and-shift / end-to-end-recovery`
**Evidence:** D3 full-paper capture; PDF SHA-256 `419d1d99bdb3f6c7e3d8c08f51bbe8d820235771da40ddfce7724f8cfa900b69`; full-text SHA-256 `4d6bd10edda137fdb541a297782ec30e25f2871a6bc662a80925a773c6a6a1a3`.

- **Ordinary problem:** A speech-enabled LLM should refuse harmful requests even when an attacker uses the speech channel.
- **Why it is hard:** Speech adds transcription, acoustic, and modality-transfer attack surfaces, while harmful data are scarce.
- **Naive attempt:** Apply text-only safety tuning or assume speech inherits the text safety boundary.
- **Central move:** Adversarially train with synthesized harmful and benign speech, then test strong white-box attacks and data ablations.
- **Mechanism:** Speech-domain harmful examples change the model; training configurations vary and safety is measured under attacks.
- **Mathematical idea:** Robustness is response behavior under a threat model, not ordinary accuracy.
- **What the paper reports:** Four hours of harmful plus 150 hours of benign speech yields reported relative safety gains of 45–300% over baseline.
- **Limits:** Attack family, harm taxonomy, model, synthesis, and rubric bound the claim; refusal is not complete security.

## 55. Pushing the Limits of End-to-End Diarization

**Paper:** [Pushing the Limits of End-to-End Diarization](https://www.isca-archive.org/interspeech_2025/broughton25_interspeech.html)
**Taxonomy:** `evaluation-deployment-and-consequence / robustness-and-shift / end-to-end-recovery`
**Evidence:** D3 full-paper capture; PDF SHA-256 `08a56160e0b6fee8b9f410aeb001c959922061ba7d08caee50d10adae3f33d02`; full-text SHA-256 `6a4c7e12078ad7f12ce66be4a2a458f124f95f4f4bedc1eb9ff9f51b1040f5ff`.

- **Ordinary problem:** A diarization system should assign speech to the right people in meetings with many simultaneous speakers without a separate pipeline for every case.
- **Why it is hard:** Overlap and speaker-count variation make it hard to learn all mixture configurations, while modular systems accumulate errors.
- **Naive attempt:** Train on a few-speaker simulation or chain independent detection and clustering modules.
- **Central move:** Use one end-to-end non-autoregressive model and scale pretraining across systematically represented eight-speaker mixtures.
- **Mechanism:** EEND-TA is evaluated on AliMeeting, AMI, DIHARD III, and MagicData RAMC with speed and diarization error comparisons.
- **Mathematical idea:** Diarization error rate measures missed, false, and wrongly attributed speech; multiple corpora test transfer across meeting conditions.
- **What the paper reports:** The paper reports 14.49% DER on DIHARD III and state-of-the-art results on the listed datasets.
- **Limits:** The simulations, corpora, speaker counts, and model speed define the boundary; spontaneous conditions beyond these meetings remain open.

## 56. Multi-Channel Sequence-to-Sequence Neural Diarization: Experimental Results for The MISP 2025 Challenge

**Paper:** [Multi-Channel Sequence-to-Sequence Neural Diarization: Experimental Results for The MISP 2025 Challenge](https://www.isca-archive.org/interspeech_2025/cheng25b_interspeech.html)
**Taxonomy:** `evaluation-deployment-and-consequence / robustness-and-shift / end-to-end-recovery`
**Evidence:** D3 full-paper capture; PDF SHA-256 `44c2cca063a8807aa6ef62642bafe7d040941d90ce3269b71ed1962a15bd8f2f`; full-text SHA-256 `ca7f15fb7b8895d5111a67bac57e3185e50998d648b2ed05bb4f71bd3308f1e2`.

- **Ordinary problem:** A meeting recording needs a timeline of who spoke when, even when one microphone misses spatial information and several people overlap.
- **Why it is hard:** Diarization must find boundaries and identities jointly; multi-channel cues can repair ambiguous single-channel predictions but are not always available or synchronized.
- **Naive attempt:** Run a single-channel diarizer once and treat each predicted segment as final.
- **Central move:** Generate initial predictions with sequence-to-sequence neural diarization, then refine them with multi-channel audio in MC-S2SND for the MISP challenge.
- **Mechanism:** The paper presents a multi-channel sequence-to-sequence neural diarization system.
- **Mathematical idea:** Who-spoke-when is structured segmentation: the first pass proposes a timeline, while additional channels provide evidence for revising boundaries and speaker assignments.
- **What the paper reports:** The system reports 8.09% diarization error rate on the challenge evaluation set and first place in the MISP 2025 diarization task.
- **Limits:** Challenge data, channel layout, scoring convention, enrollment assumptions, and test conditions bound generalization; rank and DER do not guarantee usable transcripts in every meeting.

## 57. Unmasking real-world audio deepfakes: A data-centric approach

**Paper:** [Unmasking real-world audio deepfakes: A data-centric approach](https://www.isca-archive.org/interspeech_2025/combei25_interspeech.html)
**Taxonomy:** `evaluation-deployment-and-consequence / robustness-and-shift / distribution-shift`
**Evidence:** D3 full-paper capture; PDF SHA-256 `7f55bfdbd5a5fe183864ad809405f55cabf4e4dc66426a106ef852a6b332783a`; full-text SHA-256 `e85d4cc4061a32ccea57b07b938093f1de98822228e4ea0d3d71f54ec04c9247`.

- **Ordinary problem:** Deepfake detectors that perform well on specially collected datasets can fail on the messy recordings people encounter in the world, so robustness depends on what examples the dataset contains.
- **Why it is hard:** Real-world audio varies in recording chain, edits, generators, and social context; increasing model complexity cannot repair a dataset that omits those variations.
- **Naive attempt:** Train a larger detector on a benchmark dataset and interpret a low equal-error rate as deployment readiness.
- **Central move:** Treat curation, pruning, and augmentation of real-world examples as the primary intervention, then test generalization on both an in-the-wild set and a newly collected real-world set.
- **Mechanism:** The study introduces the AI4T real-world deepfake dataset, analyzes data quality and coverage, applies data-centric filtering and augmentation, and evaluates detector systems on five public datasets plus the new set.
- **Mathematical idea:** Equal error rate is the operating point where false acceptance and false rejection meet; relative EER reduction compares the data-centric system with its baseline on each dataset. The denominator is each named test corpus, not all possible real-world audio.
- **What the paper reports:** The paper reports a 55% relative EER reduction on In-the-Wild to 1.7% absolute EER and a 63% reduction on AI4T after the data-centric interventions.
- **Limits:** The new dataset and curation choices define the tested notion of real-world variation; future generators and channels may differ. EER is not a guarantee of safe moderation or authentication, and no independent reproduction was performed.

## 58. Improving Generalization of End-to-End ASR through Diversity and Independence Regularization

**Paper:** [Improving Generalization of End-to-End ASR through Diversity and Independence Regularization](https://www.isca-archive.org/interspeech_2025/ko25_interspeech.html)
**Taxonomy:** `evaluation-deployment-and-consequence / robustness-and-shift / distribution-shift`
**Evidence:** D3 full-paper capture; PDF SHA-256 `8be702dbdb60f1787e3c134afe753492373afe8b19d6f0bf514643c41e204cf5`; full-text SHA-256 `335115ce474322cc930f9e9d8484a8581e8c8478e52ca2a3b15edab8b49c354a`.

- **Ordinary problem:** An ASR model should generalize when test speech differs from training speech instead of memorizing redundant or narrow feature patterns.
- **Why it is hard:** CTC, AED, and RNN-T models can overfit in different ways, and increasing feature diversity without controlling redundancy may not help.
- **Naive attempt:** Add capacity or regularize all features identically without identifying whether redundancy or lack of diversity causes the error.
- **Central move:** Add diversity loss to separate feature representations and independence loss to reduce covariance, then test across three ASR architectures.
- **Mechanism:** The losses operate on learned feature vectors: one discourages collapse toward similar patterns, the other discourages redundant correlated dimensions.
- **Mathematical idea:** The method shapes representation geometry so multiple informative directions survive while redundant variation is suppressed.
- **What the paper reports:** The paper reports improved generalization and robustness for CTC, AED, and RNN-T models in the evaluated tasks.
- **Limits:** Training/test shifts, loss weights, architectures, languages, and robustness protocol bound transfer; benchmark generalization is not immunity to arbitrary distribution shift.

## 59. Calm-Whisper: Reduce Whisper Hallucination On Non-Speech By Calming Crazy Heads Down

**Paper:** [Calm-Whisper: Reduce Whisper Hallucination On Non-Speech By Calming Crazy Heads Down](https://www.isca-archive.org/interspeech_2025/wang25b_interspeech.html)
**Taxonomy:** `evaluation-deployment-and-consequence / robustness-and-shift / end-to-end-recovery`
**Evidence:** D3 full-paper capture; PDF SHA-256 `b9c3951a4a04089876c22d27a359eb959ec094a4ec91a5799397abdc90697a95`; full-text SHA-256 `03c58e0d66d1362c5253fc7fceb2cf932a007884b4fb26d94eca11ab86ecbd43`.

- **Ordinary problem:** An ASR system should remain silent or abstain when the input contains non-speech instead of inventing a transcript.
- **Why it is hard:** A sequence decoder is rewarded for plausible language, and non-speech segments lack lexical evidence while still activating learned decoder patterns.
- **Naive attempt:** Add a VAD or post-filter around the model and assume the decoder itself has no identifiable source of hallucination.
- **Central move:** Diagnose decoder self-attention heads with head-wise masking, identify a small set responsible for most non-speech hallucinations, and fine-tune those heads on non-speech data.
- **Mechanism:** Ablation assigns causal responsibility at the head level; targeted fine-tuning changes the decoder’s response to acoustic absence while monitoring speech WER.
- **Mathematical idea:** The method creates an evidence boundary inside generation: silence should not be converted into a high-probability language continuation.
- **What the paper reports:** The paper reports that three of twenty decoder heads account for most hallucinations on UrbanSound and that targeted training reduces them with limited LibriSpeech WER degradation.
- **Limits:** Non-speech corpus, head attribution, fine-tuning regime, language/model version, and WER tradeoff bound transfer; reduced hallucination is not perfect abstention or factual reliability.

## 60. Is it all about race?: A Cross-examination of /s/ in a Multilingual (Nigerian) Context

**Paper:** [Is it all about race?: A Cross-examination of /s/ in a Multilingual (Nigerian) Context](https://www.isca-archive.org/interspeech_2025/amoniyan25_interspeech.html)
**Taxonomy:** `languages-accents-and-resources / accent-dialect-and-cultural-meaning / dialect-and-variety`
**Evidence:** D3 full-paper capture; PDF SHA-256 `e61598574d5c543e85b0d130cdac979f57085845ed7f2666d2147aab65535306`; full-text SHA-256 `17fa5931c31a00064812b4f5914a20db1b84c79a8aef46be44eabb1268dba204`.

- **Ordinary problem:** Multilingual speech analysis should distinguish pronunciation patterns from racialized assumptions about speakers.
- **Why it is hard:** The same segment can be interpreted differently across languages and communities.
- **Naive attempt:** Assign one standard target or explain variation through race as a direct cause.
- **Central move:** Cross-examine /s/ production in a multilingual Nigerian context using linguistic and social context.
- **Mechanism:** Acoustic realization is interpreted alongside multilingual context rather than one norm.
- **Mathematical idea:** The relevant object is the accent-robustness evidence described by the paper's mechanism: Acoustic realization is interpreted alongside multilingual context rather than one norm.
- **What the paper reports:** The paper reports a contextual analysis of /s/ in a multilingual Nigerian setting.
- **Limits:** Community, language, sampling, annotation, and interpretation bound transfer.

## 61. LID Models are Actually Accent Classifiers: Implications and Solutions for LID on Accented Speech

**Paper:** [LID Models are Actually Accent Classifiers: Implications and Solutions for LID on Accented Speech](https://www.isca-archive.org/interspeech_2025/bafna25_interspeech.html)
**Taxonomy:** `languages-accents-and-resources / accent-dialect-and-cultural-meaning / accent-robustness`
**Evidence:** D3 full-paper capture; PDF SHA-256 `a2edf57b420da23f78432b8256995a186edfc84c27c03668bd854c9a80604466`; full-text SHA-256 `71465d00b6ce721bb4077cf0e14ad8010d228cdadd17d99d7eea568bc87dba1e`.

- **Ordinary problem:** A language-identification system should identify the language, not the speaker's accent or first language.
- **Why it is hard:** Short phonetic patterns associated with a speaker's native language can make a model confuse accent with language; overall accuracy hides minority failure.
- **Naive attempt:** Train a classifier on whole-utterance labels and assume longer audio automatically supplies enough language evidence.
- **Central move:** Add phoneme-sequence or discretized-unit views and test the shortcut by permuting short speech chunks.
- **Mechanism:** The study compares ECAPA-TDNN, MMS, and GEO systems on several corpora, measures accent-language confusion, reverses chunks, and fuses acoustic and sequence representations.
- **Mathematical idea:** ECAPA-TDNN falls from 87.6% to 55.8% on CommonVoice and 73% to 57% on EdAcc for mainstream versus L2 accents; many models remain stable down to roughly 0.25-second chunks.
- **What the paper reports:** Dutch-accented English is called Dutch in 82.6% of errors in one setting; sequence-aware systems reduce this confusion while retaining mainstream performance.
- **Limits:** Datasets, accent categories, chunking, and aggregation define the result; it diagnoses a shortcut but does not prove cultural neutrality or universal transfer.

## 62. Accent Normalization Using Self-Supervised Discrete Tokens with Non-Parallel Data

**Paper:** [Accent Normalization Using Self-Supervised Discrete Tokens with Non-Parallel Data](https://www.isca-archive.org/interspeech_2025/bai25_interspeech.html)
**Taxonomy:** `languages-accents-and-resources / accent-dialect-and-cultural-meaning / accent-robustness`
**Evidence:** D3 full-paper capture; PDF SHA-256 `625cfec0c68dfd768d3dd5460fee8d3c6bb494b558a99e6a6ca61a335f658392`; full-text SHA-256 `65a8ae752632d5e90257f0bc79298420877cb2328df44461663481241e3a6366`.

- **Ordinary problem:** Accent normalization should change pronunciation while keeping the same speaker recognizable.
- **Why it is hard:** Changing accent can also change timbre, duration, intelligibility, or words, and parallel data are scarce.
- **Naive attempt:** Convert frames one by one using paired data and accept timing and identity drift.
- **Central move:** Use self-supervised discrete tokens, nonparallel conversion, flow matching, and explicit duration preservation.
- **Mechanism:** The system extracts source tokens, predicts target-accent tokens, synthesizes waveform output, and evaluates several English accents.
- **Mathematical idea:** NAT, ACT, SIM, WER, SECS, F0 correlation, and feature distance separately measure naturalness, accent, content, identity, and prosody.
- **What the paper reports:** The system beats a frame-to-frame baseline on naturalness, accentedness, and timbre preservation, but post-conversion WER remains high.
- **Limits:** Accent definitions, targets, subjective judgments, and nonparallel training bound the claim; native-like is not universally better.

## 63. A Multi-Dialectal Dataset for German Dialect ASR and Dialect-to-Standard Speech Translation

**Paper:** [A Multi-Dialectal Dataset for German Dialect ASR and Dialect-to-Standard Speech Translation](https://www.isca-archive.org/interspeech_2025/blaschke25_interspeech.html)
**Taxonomy:** `languages-accents-and-resources / accent-dialect-and-cultural-meaning / dialect-and-variety`
**Evidence:** D3 full-paper capture; PDF SHA-256 `7a9f7d63cb5bf7e00bcf7040dac177d37eeaacf39e41a1b99bc91ff4da0749ae`; full-text SHA-256 `059d8c488c374dc20a6c7b0231cbd4938fd3380a98fbf3f716a30ea0b8e7596c`.

- **Ordinary problem:** An ASR and speech-translation system should preserve what a dialect speaker said rather than silently rewrite dialect grammar into the standard variety.
- **Why it is hard:** Dialect differences affect words, grammar, pronunciation, and what counts as a correct transcription; a single standard reference hides these distinctions.
- **Naive attempt:** Evaluate one multilingual ASR model against only a standardized transcript.
- **Central move:** Create paired dialectal and Standard German references across three underrepresented dialect groups and compare model outputs against both.
- **Mechanism:** Betthupferl contains four hours of read speech from Franconian, Bavarian, and Alemannic speakers plus Standard German; multilingual ASR models are evaluated for transcription and translation.
- **Mathematical idea:** Error analysis compares similarity to dialectal versus standardized references and inspects grammatical normalization, not only one aggregate score.
- **What the paper reports:** The paper reports model-dependent differences: the best system sometimes normalizes dialect grammar but often stays closer to dialect constructions.
- **Limits:** The dataset is four hours of read speech from Southeast Germany; spontaneous speech, other dialects, conversational translation, and community judgments remain open.

## 64. The ML-SUPERB 2.0 Challenge: Towards Inclusive ASR Benchmarking for All Language Varieties

**Paper:** [The ML-SUPERB 2.0 Challenge: Towards Inclusive ASR Benchmarking for All Language Varieties](https://www.isca-archive.org/interspeech_2025/chen25h_interspeech.html)
**Taxonomy:** `languages-accents-and-resources / accent-dialect-and-cultural-meaning / accent-robustness`
**Evidence:** D3 full-paper capture; PDF SHA-256 `a7c7038485e71a36cdaf86e753293f96bf99bef574c403807f43e16fbc3b0b26`; full-text SHA-256 `88ce581c9f6e74590b21af41893e2d25bfe55d0f320b54a75811dd573a7b5ac8`.

- **Ordinary problem:** ASR should work across languages, accents, and dialects rather than only on well-resourced standard varieties.
- **Why it is hard:** A single average benchmark can hide failures on communities that have little representation in training or evaluation.
- **Naive attempt:** Report one multilingual score on a narrow, convenient test set.
- **Central move:** Build a broad public test suite and an online evaluation process that makes language-variety performance visible.
- **Mechanism:** ML-SUPERB 2.0 evaluates models on 200+ languages, accents, and dialects through DynaBench and compares five challenge submissions with baselines.
- **Mathematical idea:** Language-identification accuracy and character error rate are reported separately for general, accented, and dialectal speech.
- **What the paper reports:** The best submission reports 23% absolute LID improvement and 18% CER reduction generally, with 30.2% lower CER and 15.7% higher LID accuracy on accented/dialectal data.
- **Limits:** Challenge submissions, test-suite composition, and hidden evaluation define the boundary; the results do not prove equal service quality for every language variety.

## 65. Tonal Variation and Word Meaning in Taiwanese

**Paper:** [Tonal Variation and Word Meaning in Taiwanese](https://www.isca-archive.org/interspeech_2025/chuang25_interspeech.html)
**Taxonomy:** `languages-accents-and-resources / accent-dialect-and-cultural-meaning / cultural-meaning`
**Evidence:** D3 full-paper capture; PDF SHA-256 `7468ca38322ce3014c51ab45cd11c7bfa2344f51238abaf2855fc67e469223dc`; full-text SHA-256 `ba83405f919d5d2005ca6e8df97f741e1f1360fb98f1b47eb79f67badd353280`.

- **Ordinary problem:** Tone realization in Taiwanese should be interpreted with word meaning and sandhi context rather than reduced to citation-tone substitution.
- **Why it is hard:** Tone sandhi changes non-final syllables and spontaneous speech varies; a raw sandhi-versus-citation comparison can mistake lexical meaning for phonological neutralization.
- **Naive attempt:** Assign one canonical tone to each lexical item or compare citation and sandhi forms without semantic context.
- **Central move:** Analyze spontaneous high-falling tone realizations while modeling word meaning and compare residual sandhi/citation differences.
- **Mechanism:** Acoustic tone measurements are grouped by lexical/semantic context, allowing meaning-induced variation to be separated from categorical tone effects.
- **Mathematical idea:** The analysis treats linguistic meaning as a conditioning variable in the acoustic realization, not as nuisance variance to average away.
- **What the paper reports:** Word meaning explains part of tonal variability; after accounting for it, the reported sandhi/citation difference disappears.
- **Limits:** Speaker sample, spontaneous corpus, lexical items, tone context, and statistical model bound transfer; one tone pattern is not the whole Taiwanese system.

## 66. ViToSA: Audio-Based Toxic Spans Detection on Vietnamese Speech Utterances

**Paper:** [ViToSA: Audio-Based Toxic Spans Detection on Vietnamese Speech Utterances](https://www.isca-archive.org/interspeech_2025/do25b_interspeech.html)
**Taxonomy:** `languages-accents-and-resources / accent-dialect-and-cultural-meaning / cultural-meaning`
**Evidence:** D3 full-paper capture; PDF SHA-256 `b8e4cb43582deb8dcd796a7cec38b2bca457903f0ec19cb87835c340bb245919`; full-text SHA-256 `7d0db019515d41fdee73abaaa13fec29c103cbeb57fb85d79b58fade9f97df3e`.

- **Ordinary problem:** A speech system should identify toxic spans in Vietnamese audio without hiding which words triggered the judgment.
- **Why it is hard:** Toxicity depends on language, context, and span boundaries; speech recognition errors can change both the words and the location of the alleged harm.
- **Naive attempt:** Classify the whole utterance or run a text toxicity model on an imperfect transcript and treat its spans as exact.
- **Central move:** Create an audio-based Vietnamese toxic-span task that preserves local evidence and evaluates both detection and boundary selection.
- **Mechanism:** ViToSA builds an audio dataset and task for locating toxic spans in Vietnamese speech utterances.
- **Mathematical idea:** The prediction target is localized: the system must connect acoustic input to a particular interval or word span rather than only assign a sentence label.
- **What the paper reports:** The paper reports benchmark results for Vietnamese audio toxic-span detection.
- **Limits:** Dataset construction, annotation agreement, language, ASR errors, and social context bound the result; a benchmark score is not a complete safety policy.

## 67. Tonal Contrasts in the Malipo Variety of the Mienic Language

**Paper:** [Tonal Contrasts in the Malipo Variety of the Mienic Language](https://www.isca-archive.org/interspeech_2025/du25_interspeech.html)
**Taxonomy:** `languages-accents-and-resources / accent-dialect-and-cultural-meaning / dialect-and-variety`
**Evidence:** D3 full-paper capture; PDF SHA-256 `1d5ffb02b45ae9ecf1f928ea612f3f9b4f0ed1a9f5166327c05545a99a3fbd37`; full-text SHA-256 `ad148a9d20d7d1bc8a4822c3c89eda883691f5d7997ad3bf9674075a008a45e1`.

- **Ordinary problem:** A speech system should describe and recognize a language variety without erasing the contrast that makes the variety meaningful.
- **Why it is hard:** Small phonetic inventories and limited documentation make variation easy to mistake for noise or a universal norm.
- **Naive attempt:** Collapse the variety into a standard-language model and report only pooled accuracy.
- **Central move:** Measure tonal contrasts in the Malipo variety as an object of speech description and evaluation.
- **Mechanism:** Contrastive measurements expose which acoustic distinctions carry linguistic information.
- **Mathematical idea:** The paper treats dialect-and-variety as a structured evidence-to-decision problem: Contrastive measurements expose which acoustic distinctions carry linguistic information.
- **What the paper reports:** The paper reports an empirical study of tonal contrasts in a Mienic variety.
- **Limits:** Speaker sample, elicitation design, tonal context, and language-specific scope bound transfer.

## 68. Speech transcription from South Tyrolean Dialect to Standard German with Whisper

**Paper:** [Speech transcription from South Tyrolean Dialect to Standard German with Whisper](https://www.isca-archive.org/interspeech_2025/ducceschi25_interspeech.html)
**Taxonomy:** `languages-accents-and-resources / accent-dialect-and-cultural-meaning / dialect-and-variety`
**Evidence:** D3 full-paper capture; PDF SHA-256 `c40f366bf4f1446b8639b6f03ade3b384876d4248de44b697bbcb21c726fb18d`; full-text SHA-256 `84374738b42e087179914a67dd152d8a4f69e9014e1d66d5bee4c720ca0bc3fe`.

- **Ordinary problem:** An archive may contain South Tyrolean dialect speech while the useful public output must be Standard German subtitles or translations; a recognizer trained on standard speech may miss the dialect before translation begins.
- **Why it is hard:** Dialect pronunciation, vocabulary, and grammar differ from the data used to train a general ASR system, and a small corpus makes it hard to learn all of those differences.
- **Naive attempt:** Run an off-the-shelf recognizer and translate its errors, or collect only standard-German speech and assume dialect variation is small.
- **Central move:** Build manually annotated and synthetic dialect data, fine-tune Whisper for the dialect-to-standard text mapping, and evaluate the actual archival translation task.
- **Mechanism:** The paper fine-tunes Whisper for South Tyrolean dialect speech to Standard German text, uses a small manually annotated plus synthetic corpus, and optimizes the task for archival audiovisual material.
- **Mathematical idea:** Recognition and translation are coupled in the output contract: the model need not first produce a standard transcript if training directly links dialect audio to standard written text; BLEU and error measures test the product.
- **What the paper reports:** The paper reports a BLEU score of 86.18 and substantial improvement over its baselines, with an existing heritage-archive use case.
- **Limits:** Small corpus, synthetic data, dialect region, reference translations, BLEU, and deployment domain bound the claim; high translation score does not establish coverage of every speaker or dialect context.

## 69. Are You Being Sarcastic? Prosodic Cues to Irony Perception in German

**Paper:** [Are You Being Sarcastic? Prosodic Cues to Irony Perception in German](https://www.isca-archive.org/interspeech_2025/funfgeld25_interspeech.html)
**Taxonomy:** `languages-accents-and-resources / accent-dialect-and-cultural-meaning / cultural-meaning`
**Evidence:** D3 full-paper capture; PDF SHA-256 `bf09f0ab68fe59b4d92de3c8469e4bb02f474a79b0a4d2b0a74e23f8c59b0e59`; full-text SHA-256 `616d3d63fa04999dda83e686300cd7897ee4faf97606c271f6d0c582b5cf26fa`.

- **Ordinary problem:** Listeners must infer whether a speaker means the opposite of the words, even when the words themselves sound positive.
- **Why it is hard:** Irony depends on timing and pitch accents as well as lexical content, and listeners from different varieties may use those cues differently.
- **Naive attempt:** Treat the words or one global pitch statistic as sufficient for sarcasm.
- **Central move:** Vary prenuclear and nuclear accent placement/type and measure regional listeners' sarcasm decisions and response times.
- **Mechanism:** German utterances are presented in seven prosodic conditions to listeners from Freiburg and Trier, who classify them as sarcastic or sincere.
- **Mathematical idea:** The experiment separates cue presence, accent type, region, decision, and reaction time rather than reducing intonation to one pitch average.
- **What the paper reports:** Prenuclear accent presence and especially L*+H nuclear accents drive irony judgments; some conditions also yield faster ironic responses.
- **Limits:** The utterances, regions, prosodic manipulations, and binary judgment task bound the result; other languages and natural conversations remain open.

## 70. A Multimodal Chinese Dataset for Cross-lingual Sarcasm Detection

**Paper:** [A Multimodal Chinese Dataset for Cross-lingual Sarcasm Detection](https://www.isca-archive.org/interspeech_2025/gao25f_interspeech.html)
**Taxonomy:** `languages-accents-and-resources / accent-dialect-and-cultural-meaning / accent-robustness`
**Evidence:** D3 full-paper capture; PDF SHA-256 `de40c16869e79395e128991685d60b68ca8fb8af354941a425179cc9f4a99b48`; full-text SHA-256 `ba2f9825cb5feebc6f8333c6870f9bb7fe907b0d06019185f4d21e6abf94fd6f`.

- **Ordinary problem:** A multilingual ASR system should handle accents and varieties without treating one pronunciation norm as universal.
- **Why it is hard:** Accent variation changes acoustic-to-word evidence and can interact with language and speaker identity.
- **Naive attempt:** Train or evaluate only on standard speech and report one pooled error rate.
- **Central move:** Analyze accent robustness under multilingual conditions and identify where recognition errors reflect a narrow training norm.
- **Mechanism:** Subgroup and accent-conditioned evaluation separates intended-word performance across varieties rather than hiding failures in an aggregate.
- **Mathematical idea:** Robustness is a boundary measurement: the system's norm becomes visible only when varieties are evaluated separately.
- **What the paper reports:** The paper reports a study of multilingual/accent robustness and its implications for ASR evaluation.
- **Limits:** Accent labels, languages, speakers, test design, and subgroup denominators bound transfer.

## 71. Audio-Based Classification and Geographic Regression of Austrian Dialects

**Paper:** [Audio-Based Classification and Geographic Regression of Austrian Dialects](https://www.isca-archive.org/interspeech_2025/gutscher25_interspeech.html)
**Taxonomy:** `languages-accents-and-resources / accent-dialect-and-cultural-meaning / dialect-and-variety`
**Evidence:** D3 full-paper capture; PDF SHA-256 `bff7e58252e99c253d3c29e18585b33c5081ecd0a67b3dd57d0c63b120ccb349`; full-text SHA-256 `13201954572cb212beae6bca1ecb68f5f8a0e5aa71b1be8c9ac9d283c74353c4`.

- **Ordinary problem:** An acoustic model should identify regional dialect variation without simply memorizing the speaker identity or location-specific recording conditions.
- **Why it is hard:** Dialect and speaker cues are entangled, locations are unevenly sampled, and geographic regression requires a continuous notion of error rather than a single class label.
- **Naive attempt:** Train a classifier on pooled speech and interpret speaker memorization as dialect recognition, or predict only coarse dialect groups.
- **Central move:** Use speaker augmentation to reduce speaker-specific bias and jointly examine dialect/location classification with geographic-coordinate regression.
- **Mechanism:** The model learns speech representations for hierarchical classification and a continuous coordinate prediction; held-out speaker and location splits test whether regional structure survives identity variation.
- **Mathematical idea:** Classification partitions a geographic continuum while regression measures distance in kilometers, so the two tasks expose different resolutions and failure modes of dialect modeling.
- **What the paper reports:** The Austrian dataset covers 304 speakers at 108 locations; wav2vec 2.0 reports an average geographic test error of 66.7 km in the paper's evaluation.
- **Limits:** Sampling density, speaker augmentation, Austrian dialect geography, split design, and recording conditions limit transfer; geographic prediction is not a complete sociolinguistic account of dialect.

## 72. Are loan sequences different from foreign sequences? A perception study with Japanese listeners on coronal obstruent – high front vowel sequences

**Paper:** [Are loan sequences different from foreign sequences? A perception study with Japanese listeners on coronal obstruent – high front vowel sequences](https://www.isca-archive.org/interspeech_2025/hamann25_interspeech.html)
**Taxonomy:** `languages-accents-and-resources / accent-dialect-and-cultural-meaning / cultural-meaning`
**Evidence:** D3 full-paper capture; PDF SHA-256 `901660a9116a0da070076ea8a601225e1ccc65f03b1601e22f5869edb1b40a41`; full-text SHA-256 `9f9c8e04df747e2a55471a075161eed91d84dcc434d8f660b847e9d473812deb`.

- **Ordinary problem:** Listeners must discriminate sound sequences that are native, permitted only in loanwords, or absent from the native phonotactics.
- **Why it is hard:** Native-language expectations shape perception, but exposure to foreign languages and lexical status may create graded rather than binary categories.
- **Naive attempt:** Treat every non-native sequence as equally foreign or infer perception directly from phonotactic legality.
- **Central move:** Compare AX discrimination of a loan-permitted sequence with a prohibited sequence and measure whether individual English exposure explains performance.
- **Mechanism:** Japanese listeners discriminate /ti/ and /zi/ contrasts in an online task; sequence status and self-reported English input are tested as competing explanations.
- **Mathematical idea:** Phonotactic knowledge acts as a prior over possible sequences, but the experiment tests whether that prior fully determines auditory discrimination.
- **What the paper reports:** Thirty-nine listeners performed better on the loanword-permitted sequence, though the foreign sequence was also often discriminated; self-reported English input did not explain the result.
- **Limits:** Online testing, sequence choices, speaker exposure, sample size, and self-report limit generalization; discrimination is not equivalent to lexical access or translation competence.

## 73. On the Relationship between Accent Strength and Articulatory Features

**Paper:** [On the Relationship between Accent Strength and Articulatory Features](https://www.isca-archive.org/interspeech_2025/huang25h_interspeech.html)
**Taxonomy:** `languages-accents-and-resources / accent-dialect-and-cultural-meaning / accent-robustness`
**Evidence:** D3 full-paper capture; PDF SHA-256 `8dd1a4840138427b50ba39759bbdd0bef7f7c0dc4226d3759198c2da2231fa5a`; full-text SHA-256 `afd9a13fd44957c4dcf5d8d3cba3594be1015aac4d21ef0462ba709361f2368d`.

- **Ordinary problem:** Accent analysis should relate an observable accent difference to speech production rather than treating a phoneme mismatch as an unexplained label.
- **Why it is hard:** Accent strength is a proxy derived from reference pronunciations, while articulatory inversion is itself uncertain and dialect differences can be localized to particular sounds.
- **Naive attempt:** Count transcription differences and declare them an accent score, or infer articulatory movement without checking whether it tracks the accent proxy.
- **Central move:** Use dictionary-based phonetic differences as an accent-strength index and correlate it with articulatory features inferred from acoustic speech.
- **Mechanism:** Self-supervised articulatory inversion estimates tongue and related articulator features; phoneme-level deviations from dictionary references provide the comparison variable across American and British English.
- **Mathematical idea:** The analysis links two imperfect measurements—phonological deviation and inferred movement—so correlation tests whether an accent proxy has a plausible production-level signature.
- **What the paper reports:** The paper reports dialect differences in tongue positioning, especially for rhotic and low-back vowels, and associations between derived articulatory parameters and indexed accent strength.
- **Limits:** Read speech, two dialect groups, dictionary assumptions, inversion error, and correlation do not establish a universal accent scale or causal articulatory explanation.

## 74. Lexical competition in the process of Cantonese tone merging: Diverse Impact Mechanisms Across Different Individuals and Tone Pairs

**Paper:** [Lexical competition in the process of Cantonese tone merging: Diverse Impact Mechanisms Across Different Individuals and Tone Pairs](https://www.isca-archive.org/interspeech_2025/li25w_interspeech.html)
**Taxonomy:** `languages-accents-and-resources / accent-dialect-and-cultural-meaning / dialect-and-variety`
**Evidence:** D3 full-paper capture; PDF SHA-256 `8864eb4a5a5437ae7a823a5765cc26de015076b80dbfdd1b784d17d6a262e3a4`; full-text SHA-256 `67458cc560575f6f6adbfc942a869ab28e0c2e56f22d6988a67f5beaade5649e`.

- **Ordinary problem:** A tone contrast can merge gradually in a community while individual speakers still preserve or reshape it differently.
- **Why it is hard:** Word competition can push a speaker away from a merger, but its effect may depend on the tone pair and on how far that speaker has already merged.
- **Naive attempt:** Treat tone change as one uniform process with one lexical effect for every speaker.
- **Central move:** Examine lexical competition separately for each speaker and tone pair, then relate production distributions to the speaker's merger pattern.
- **Mechanism:** Cantonese tone production is measured for speakers with no clear merger, one merged pair, or multiple merged pairs; lexical competition is compared across pairs.
- **Mathematical idea:** The relevant object is an individual, context-conditioned distribution rather than a population average; different effects reveal inhibition, promotion, or no change.
- **What the paper reports:** Competition helps maintain contrasts in some speakers, consistently inhibits one pair, has three patterns for another, and has little effect in speakers merging all three tones.
- **Limits:** The Cantonese pairs, speaker groups, lexical measure, and production task bound the result; it is evidence about a change process, not a forecast of every speaker's future pronunciation.

## 75. Prosodically Enhanced Foreign Accent Simulation by Discrete Token-based Resynthesis Only with Native Speech Corpora

**Paper:** [Prosodically Enhanced Foreign Accent Simulation by Discrete Token-based Resynthesis Only with Native Speech Corpora](https://www.isca-archive.org/interspeech_2025/onda25b_interspeech.html)
**Taxonomy:** `languages-accents-and-resources / accent-dialect-and-cultural-meaning / accent-robustness`
**Evidence:** D3 full-paper capture; PDF SHA-256 `0f2e603c321ce4ead5e22996886a29435b630a0740dd43ad9d5f35059efab9aa`; full-text SHA-256 `b316da3a4f0d0cff0e3cb04d646028d5c4434d6ba41f0b36d901d9c39ffdd775`.

- **Ordinary problem:** Training and listening materials should expose learners and recognizers to foreign accents that are scarce in native-speech corpora.
- **Why it is hard:** Accent changes segmental realization and rhythm; a system that changes only discrete phonetic tokens can miss duration patterns characteristic of the speaker’s first language.
- **Naive attempt:** Use native speech unchanged or resynthesize token content without modeling timing, then call the result an accent simulation.
- **Central move:** Add explicit duration modification to discrete-token resynthesis so native speech can approximate durational foreign-accent cues without accented training data.
- **Mechanism:** Self-supervised discrete units preserve linguistic content, while duration controls alter timing before the units are rendered by a decoder; real L2 speech supplies the comparison target.
- **Mathematical idea:** Accent simulation is a structured transformation: content units should stay stable while temporal realization changes in a language-specific way.
- **What the paper reports:** The paper reports that the enhanced method reproduces durational accents observed in real L2 speech.
- **Limits:** Accent languages, speakers, duration estimator, perceptual validation, and native-corpus assumptions bound transfer; acoustic similarity is not proof of improved ASR or pedagogy.

## 76. Open Universal Arabic ASR Leaderboard

**Paper:** [Open Universal Arabic ASR Leaderboard](https://www.isca-archive.org/interspeech_2025/wang25_interspeech.html)
**Taxonomy:** `languages-accents-and-resources / accent-dialect-and-cultural-meaning / dialect-and-variety`
**Evidence:** D3 full-paper capture; PDF SHA-256 `cf5820cc3a819d9fabd524eaf08c2d95e36697199de6e51777c1e269249babfa`; full-text SHA-256 `b328b023e1684dcac7cb55fbc333d7c75fa38c5278c4f0bb7b43d730cab28ba8`.

- **Ordinary problem:** An Arabic ASR system should work across dialects rather than appear strong on one convenient corpus.
- **Why it is hard:** Dialect, recording, vocabulary, and corpus composition vary together, so a single benchmark can hide generalization failures.
- **Naive attempt:** Report one WER on one dialect and treat it as universal Arabic performance.
- **Central move:** Build a public multi-dataset leaderboard that compares models across dialects and also exposes robustness, adaptation, efficiency, and memory dimensions.
- **Mechanism:** The benchmark fixes model/data/evaluation axes across six test corpora and records WER plus resource and adaptation measurements.
- **Mathematical idea:** A leaderboard is a measurement design: the set of dialects and denominators determines which kind of generalization is visible.
- **What the paper reports:** The paper reports broad comparative results and identifies differences in dialect robustness, speaker adaptation, inference efficiency, and memory use.
- **Limits:** Corpus selection, language variety, transcription conventions, model versions, and leaderboard maintenance bound the conclusion; rankings are not a causal explanation of dialect performance.

## 77. Tonal Perception in Changde Mandarin

**Paper:** [Tonal Perception in Changde Mandarin](https://www.isca-archive.org/interspeech_2025/zhang25b_interspeech.html)
**Taxonomy:** `languages-accents-and-resources / accent-dialect-and-cultural-meaning / dialect-and-variety`
**Evidence:** D3 full-paper capture; PDF SHA-256 `d00cbd16906d78dfba67f271337ce40f1d55c44d51d70bb4e7103d1742516540`; full-text SHA-256 `083e16d9ae742bc3d7126fc8a71124ceee45cd03f455ef8a27c28029c526e01b`.

- **Ordinary problem:** Listeners must distinguish lexical tones whose pitch contours overlap and whose categories may not behave like cleanly separated bins.
- **Why it is hard:** Pitch height, movement, duration, and phonation interact, and a continuum between tones may be heard gradually rather than categorically.
- **Naive attempt:** Assign each tone one fixed pitch contour and assume every listener makes an all-or-none category decision.
- **Central move:** Measure perceptual cues for all four Changde Mandarin tones and test whether tone continua meet behavioral standards for categorical perception.
- **Mechanism:** Production and perception data examine T1–T4 contours and T2-T3 and T2-T4 continua using tone identification and cue analyses.
- **Mathematical idea:** The key object is the listener's response curve across an acoustic continuum; categorical perception requires a sharp boundary and reduced cross-category sensitivity, not just different labels.
- **What the paper reports:** T1 is high-level, T2 low-rising, T3 falling rather than level, and the T2-T3 and T2-T4 continua do not meet typical categorical-perception standards.
- **Limits:** The Changde variety, speakers, stimuli, cue manipulation, and category criteria bound the result; it should not be generalized to Standard Mandarin or all tonal perception.

## 78. The Role of Contextual Variation in Learning Cantonese Tones from Naturalistic Speech

**Paper:** [The Role of Contextual Variation in Learning Cantonese Tones from Naturalistic Speech](https://www.isca-archive.org/interspeech_2025/zhao25j_interspeech.html)
**Taxonomy:** `languages-accents-and-resources / accent-dialect-and-cultural-meaning / dialect-and-variety`
**Evidence:** D3 full-paper capture; PDF SHA-256 `1a5721799baa9c82b057c5f67cdfe3519a81dbd9242209ad3131a5bf5b0487f9`; full-text SHA-256 `7f013a4a75924d9166ac91c4c1b24a3f9a65ea53b6cb04742fec7c43d96723cf`.

- **Ordinary problem:** An infant must learn tonal categories even when the acoustic cues change with speaker, syllable, and surrounding context rather than repeating one stable value.
- **Why it is hard:** Complex tone contrasts may have no single invariant cue, so category learning must use how distributions change across contexts.
- **Naive attempt:** Search for one fixed acoustic threshold for each tone and treat contextual variation as noise.
- **Central move:** Compare the amount of contextual variation in naturalistic Cantonese speech with which tone contrasts are easier or harder to acquire.
- **Mechanism:** Naturalistic Cantonese productions are analyzed across six tonal contrasts and compared with existing acquisition findings under the Distributional Learning Across Contexts proposal.
- **Mathematical idea:** The learning signal is a distribution over contexts, not a single token; variation and acquisition difficulty are related at the contrast level.
- **What the paper reports:** The paper reports that contextual variation can predict which Cantonese contrasts are easier or harder to learn when invariant cues are absent.
- **Limits:** The naturalistic corpus, tone system, acquisition comparison, and distributional measures bound the inference; a prediction from correspondence is not a direct infant-learning experiment.

## 79. SpokenNativQA: Multilingual Everyday Spoken Queries for LLMs

**Paper:** [SpokenNativQA: Multilingual Everyday Spoken Queries for LLMs](https://www.isca-archive.org/interspeech_2025/alam25_interspeech.html)
**Taxonomy:** `languages-accents-and-resources / crosslingual-structure / code-switching`
**Evidence:** D3 full-paper capture; PDF SHA-256 `18bd3681a3b64e6b91cddb8134034520ac55fbe72d18aeb0334d5041ba26a11a`; full-text SHA-256 `cfd8504a3a78deb73897955050679d4a275cb2101b06777833e367b79116b978`.

- **Ordinary problem:** A spoken question-answering system must handle natural accents, languages, dialects, and everyday phrasing rather than only clean text typed by benchmark authors.
- **Why it is hard:** Text benchmarks remove pronunciation and interaction variability, while a translated dataset can erase culturally specific ways of asking and answering.
- **Naive attempt:** Transcribe a small set of scripted questions and evaluate a text LLM as if it had heard the original speech.
- **Central move:** Build a culturally aligned multilingual spoken QA dataset and evaluate the ASR-plus-LLM chain on naturally spoken questions and answers.
- **Mechanism:** SpokenNativQA contains about 33,000 spoken questions and answers across multilingual, low-resource, and dialect-rich settings; ASR systems and LLMs are benchmarked on the resulting task.
- **Mathematical idea:** The benchmark keeps acoustic variability in the input and evaluates the chain from speech recognition to answer generation rather than text QA alone.
- **What the paper reports:** The paper introduces the dataset, releases data and scripts, and reports comparative ASR and LLM results for spoken QA.
- **Limits:** Language coverage, annotation, question domains, ASR errors, and answer scoring bound the result; a benchmark does not establish equal usefulness across all represented communities.

## 80. TalTech Systems for the Interspeech 2025 ML-SUPERB 2.0 Challenge

**Paper:** [TalTech Systems for the Interspeech 2025 ML-SUPERB 2.0 Challenge](https://www.isca-archive.org/interspeech_2025/alumae25_interspeech.html)
**Taxonomy:** `languages-accents-and-resources / crosslingual-structure / language-identification`
**Evidence:** D3 full-paper capture; PDF SHA-256 `b56d427c2d320aac37c04c4573fe06968581489a58a01f1632424d919a38194e`; full-text SHA-256 `b132318ea731472b4b64ca888004a9f32bc8513c76b8aef7ce11226d36bdf0f8`.

- **Ordinary problem:** A multilingual recognizer must allocate limited capacity across languages with different data sizes and acoustic demands.
- **Why it is hard:** Average scores hide low-resource failures; language-ID errors and subword choices can contaminate recognition.
- **Naive attempt:** Train one pooled recognizer and optimize aggregate CER, letting high-resource languages dominate.
- **Central move:** Use hybrid language identification, multilingual and language-specific models, and targeted decoding resources.
- **Mechanism:** The system combines language identification with multilingual ASR and customized models, then evaluates language ID and CER.
- **Mathematical idea:** Language-ID accuracy and mean CER expose routing and transcription separately; reported values are 86.8% and 27.4%.
- **What the paper reports:** The system is competitive with challenge baselines and identifies languages needing targeted work.
- **Limits:** Challenge data, language mix, averaging, and tuning limit all-multilingual claims.

## 81. A Study of Speech Embedding Similarities Between Australian Aboriginal and High-Resource Languages

**Paper:** [A Study of Speech Embedding Similarities Between Australian Aboriginal and High-Resource Languages](https://www.isca-archive.org/interspeech_2025/ambikairajah25_interspeech.html)
**Taxonomy:** `languages-accents-and-resources / crosslingual-structure / crosslingual-transfer`
**Evidence:** D3 full-paper capture; PDF SHA-256 `c7658cb9cda0e856016c6815426aeae4084fe77890d127d39858792f11884779`; full-text SHA-256 `386fbde563f58dc4c377d4640871937b82e79eddb0cb19cd62a785b11efbadf7`.

- **Ordinary problem:** Understand whether speech representations preserve useful relationships for Australian Aboriginal languages despite their limited digital data.
- **Why it is hard:** Embedding similarity can reflect shared phonetics, recording conditions, or the model's high-resource bias rather than meaningful language structure.
- **Naive attempt:** Treat closeness in an embedding space as proof that two languages are linguistically or task-wise interchangeable.
- **Central move:** Compare speech embeddings across Aboriginal and high-resource languages and inspect what kinds of similarity and transfer the representation actually supports.
- **Mechanism:** Audio from multiple languages is passed through a speech encoder; distances or similarity distributions are compared across language pairs and conditions, with downstream implications analyzed.
- **Mathematical idea:** Embedding similarity is a geometric comparison in the learned representation space; its interpretation depends on normalization, sampling, language balance, and the task used to validate it.
- **What the paper reports:** The paper reports comparative embedding similarities involving Australian Aboriginal and high-resource languages and discusses implications for underrepresented-language technology.
- **Limits:** Similarity is not a language description or a guarantee of recognition transfer; data quantity, speaker coverage, and community context limit interpretation. No independent reproduction was performed.

## 82. From Context to Code-switching: Examining the Interplay of Language Proficiency and Multilingualism in Speech

**Paper:** [From Context to Code-switching: Examining the Interplay of Language Proficiency and Multilingualism in Speech](https://www.isca-archive.org/interspeech_2025/bhattacharya25_interspeech.html)
**Taxonomy:** `languages-accents-and-resources / crosslingual-structure / code-switching`
**Evidence:** D3 full-paper capture; PDF SHA-256 `adb282c8c89a8773fdd0eed5585b8b91676857806f8fadf93bb8c9c898dfd5ba`; full-text SHA-256 `ee83e93d18f25fc7a48c889cc3ef842daf66a73d1c0cba366b95a5f4c3a6c6f6`.

- **Ordinary problem:** People who use more than one language may switch languages within conversation, and interpreting that behavior requires distinguishing language ability and exposure from the switch itself.
- **Why it is hard:** Code-switching is shaped by language pair, conversation, speaker background, and local discourse; treating it as a single frequency can hide different switching strategies and confounds.
- **Naive attempt:** Count switches and attribute differences directly to a demographic label or assume language proficiency is unrelated to spontaneous switching behavior.
- **Central move:** Model code-switching quantity, dominant language, and switching strategy together with speaker background variables such as parental language, schooling language, and self-reported ability.
- **Mechanism:** The study analyzes spontaneous Spanish-English speech in the Bangor Miami corpus, defines insertional and alternational switching outcomes, compares speaker language profiles, and fits regression models to quantity, language distribution, and strategy. It separates associations that are statistically reliable from those that only approach significance.
- **Mathematical idea:** The paper uses correlations, logistic regression, confidence intervals, and prediction analyses. Its denominators are corpus speakers and code-switched utterances; an association between background and switching is not a causal estimate of proficiency.
- **What the paper reports:** The paper reports that parents’ primary language, secondary-school language, and self-reported higher-ability language are associated with code-switching quantity and dominant-language use, while several direct proficiency relationships are weak or inconclusive.
- **Limits:** The analysis is observational, focused on Spanish-English Bangor Miami speakers and available self-reports; background variables may be correlated and do not establish why a speaker switched. Findings do not generalize automatically to other language pairs, communities, or tasks; no independent reproduction was performed.

## 83. Adapting Whisper for low-resource Hindi-English Code-Mix speech with on-the-fly Augmentation & LLM-Synthesised Data

**Paper:** [Adapting Whisper for low-resource Hindi-English Code-Mix speech with on-the-fly Augmentation & LLM-Synthesised Data](https://www.isca-archive.org/interspeech_2025/biswas25_interspeech.html)
**Taxonomy:** `languages-accents-and-resources / crosslingual-structure / code-switching`
**Evidence:** D3 full-paper capture; PDF SHA-256 `7d78135bd1d5c1ef9773a24d9aa2e0652a44ad4f08c42f02f8787002da57d4a1`; full-text SHA-256 `5ebf19c8a3021624ef68ee18dbc76c93d410fe81b174646a1cac78c89d4db2a3`.

- **Ordinary problem:** Adapt Whisper to Hindi-English code-mixed speech with limited labeled data.
- **Why it is hard:** Language switching creates acoustic and language confusion, while low-resource Indic settings lack enough in-domain examples.
- **Naive attempt:** Fine-tune a pretrained recognizer only on scarce original code-mixed data.
- **Central move:** Combine language-specific prompts, on-the-fly code-mixed augmentation, and LLM-generated text followed by audio synthesis.
- **Mechanism:** Synthetic switches and language prompts expose the recognizer to transition patterns; MER and code-switch bigram accuracy evaluate transcription.
- **Mathematical idea:** MER measures mixed-language word errors and CBA focuses on correctly recognized bigrams at switch points.
- **What the paper reports:** The paper reports a 31% relative improvement over pretrained Whisper without real in-domain data for fine-tuning.
- **Limits:** The experiments focus on Hindi-English tutorial speech and Whisper large-v2; transfer to other language pairs is proposed, not established.

## 84. Teacher-Free Knowledge Distillation for Improving Short-Utterance Spoken Language Identification

**Paper:** [Teacher-Free Knowledge Distillation for Improving Short-Utterance Spoken Language Identification](https://www.isca-archive.org/interspeech_2025/dey25_interspeech.html)
**Taxonomy:** `languages-accents-and-resources / crosslingual-structure / language-identification`
**Evidence:** D3 full-paper capture; PDF SHA-256 `78db88d105829c906b85d927be18e04cfee1df9e5ec2ae017f20f676000e4015`; full-text SHA-256 `a06f40730547bc655e3d20c6ad71a70ec554a80f3ab448bb41e2df032b663e85`.

- **Ordinary problem:** Language identification must work on very short speech, where two seconds may contain fillers, overlap, names, or even no speech.
- **Why it is hard:** A separate teacher model is expensive, and ordinary hard labels do not express uncertainty among languages or the fact that a segment may be out of scope.
- **Naive attempt:** Train on hard language labels only or distill from a large teacher and ignore the particular errors caused by short segments.
- **Central move:** Use online soft labels from correctly classified training segments, with dynamic weighting, conditional updates, and entropy-based uncertainty, without a separate teacher.
- **Mechanism:** The paper proposes teacher-free knowledge distillation for short-utterance spoken language identification.
- **Mathematical idea:** The soft target is an accumulated view of what the model reliably knows; uncertainty and segment quality shape how much each example changes the decision boundary.
- **What the paper reports:** The paper reports consistent Cavg improvements in same-corpus and cross-corpus short-utterance evaluations.
- **Limits:** Languages, out-of-scope composition, duration, label updates, and corpora bound the result; better short-segment ID does not solve open-set detection generally.

## 85. ADI-20: Arabic Dialect Identification dataset and models

**Paper:** [ADI-20: Arabic Dialect Identification dataset and models](https://www.isca-archive.org/interspeech_2025/elleuch25_interspeech.html)
**Taxonomy:** `languages-accents-and-resources / crosslingual-structure / language-identification`
**Evidence:** D3 full-paper capture; PDF SHA-256 `6a9c4b54f8abef4f48b40d4968ff771d2594cd2fb39d7819226ffc168b713442`; full-text SHA-256 `e6032581d3cf9dd659a26ef8f74657ee5f5d340434463435ac2e59909220cda4`.

- **Ordinary problem:** A dialect identifier should distinguish all Arabic varieties without requiring the data and model size of a full-resource system.
- **Why it is hard:** Dialects share language identity while differing in sound and vocabulary, and country coverage is uneven.
- **Naive attempt:** Train on a few prominent dialects or assume a large model automatically solves data imbalance.
- **Central move:** Release broad data and compare pretrained encoders, data-size reduction, and model capacity directly.
- **Mechanism:** ADI-20 contains 3,556 hours across 19 dialects plus MSA; ECAPA-TDNN and Whisper encoder systems are evaluated.
- **Mathematical idea:** F1 measures dialect identification while controlled reductions test the value of data volume and parameters.
- **What the paper reports:** Using 30% of the original data causes only a small F1 decrease in the reported experiments.
- **Limits:** The country/dialect inventory, labels, and data collection define the boundary; conversational code-switching and unrepresented varieties remain open.

## 86. Speech-to-Text Translation with Phoneme-Augmented CoT: Enhancing Cross-Lingual Transfer in Low-Resource Scenarios

**Paper:** [Speech-to-Text Translation with Phoneme-Augmented CoT: Enhancing Cross-Lingual Transfer in Low-Resource Scenarios](https://www.isca-archive.org/interspeech_2025/gallego25_interspeech.html)
**Taxonomy:** `languages-accents-and-resources / crosslingual-structure / crosslingual-transfer`
**Evidence:** D3 full-paper capture; PDF SHA-256 `48ccc4729e0124e631b56d67f5f1ea13a678396ff2c1239565757bc6089ef1a3`; full-text SHA-256 `1cca3fd6a0543118cc359dab8842810b54312f6933864e7c17b4e8b5cdec15df`.

- **Ordinary problem:** A translation system should translate speech into text for languages with little or no labeled speech data.
- **Why it is hard:** Sound-to-meaning transfer crosses languages and modalities, while phonetic evidence is easier to share than complete translated speech examples.
- **Naive attempt:** Train a large speech-to-text translator only on languages with parallel speech and translation labels.
- **Central move:** Insert phoneme recognition and phoneme-aware chain-of-thought steps, then gradually shift training from text support toward speech.
- **Mechanism:** A multilingual LLM processes speech and phonemes under a curriculum; multilingual benchmarks compare low-, zero-, and high-resource settings.
- **Mathematical idea:** Phonemes form an intermediate representation that can transfer sound structure across languages, while translation quality measures the final meaning transfer.
- **What the paper reports:** The paper reports improved low-resource translation and zero-resource operation, with a small high-resource tradeoff.
- **Limits:** Languages, phoneme recognizer, curriculum, and benchmark define the boundary; zero-resource claims depend on what other language information is available.

## 87. Self-Supervised Models of Speech Processing for Haitian Creole

**Paper:** [Self-Supervised Models of Speech Processing for Haitian Creole](https://www.isca-archive.org/interspeech_2025/havard25_interspeech.html)
**Taxonomy:** `languages-accents-and-resources / crosslingual-structure / crosslingual-transfer`
**Evidence:** D3 full-paper capture; PDF SHA-256 `01411ac842a7947006c8437a42cce36fff901d0d86dd4af5cb15d6627e313a0c`; full-text SHA-256 `b9bc4f28477a5f75df6230cd9a78efec146c3a688eaab9055f7dbd36cba9295c`.

- **Ordinary problem:** Haitian Creole needs speech models trained on its own sounds and data, not only a large multilingual model that may underrepresent its structure.
- **Why it is hard:** Large multilingual pretraining can help but may encode data imbalance; training a monolingual model from scratch costs data and compute and must be compared fairly.
- **Naive attempt:** Fine-tune a multilingual checkpoint and assume scale always beats language-specific training.
- **Central move:** Pretrain monolingual self-supervised models for Haitian Creole, compare them with multilingual and French-based models, and fine-tune all for ASR.
- **Mechanism:** The paper develops self-supervised speech-processing models for Haitian Creole and compares monolingual, multilingual, and French-derived initialization.
- **Mathematical idea:** Representation quality depends on language fit as well as parameter count; a smaller language-specific model can win when its pretraining signal matches the target speech.
- **What the paper reports:** The paper reports monolingual models that are competitive with or surpass larger multilingual alternatives on the tested ASR tasks.
- **Limits:** Data volume, speakers, orthography, model size, pretraining compute, and evaluation domain limit generalization to the broader Creole speech community.

## 88. NIRANTAR: Continual Learning with New Languages and Domains on Real-world Speech Data

**Paper:** [NIRANTAR: Continual Learning with New Languages and Domains on Real-world Speech Data](https://www.isca-archive.org/interspeech_2025/javed25_interspeech.html)
**Taxonomy:** `languages-accents-and-resources / crosslingual-structure / crosslingual-transfer`
**Evidence:** D3 full-paper capture; PDF SHA-256 `0a331acd2bb38f841b409b8da2b9d6f606b26fa9e53906d37779ca46468dfee2`; full-text SHA-256 `167e19208cdd1139fe1d15389eb433da8530704a2d04326f7f570e1df307c723`.

- **Ordinary problem:** A deployed ASR system must keep learning as new languages and domains arrive in an uneven real-world stream.
- **Why it is hard:** A model can learn the new episode while forgetting older languages, and simulated episodes hide irregular shifts.
- **Naive attempt:** Shuffle all data together or evaluate continual learning on artificially regular episodes.
- **Central move:** Measure language-incremental, domain-incremental, and joint language-plus-domain learning on naturally arriving speech.
- **Mechanism:** NIRANTAR contains 3,250 hours from 22 languages and 208 Indian districts, with non-uniform episodes and human transcripts; existing continual-learning methods are compared.
- **Mathematical idea:** The central objects are recognition error over time and retention after each episode; the framework separates language and domain changes instead of averaging them away.
- **What the paper reports:** The paper finds that no single evaluated method performs consistently across the three scenarios.
- **Limits:** This is a benchmark and comparative study, not proof that one method is universally best; the geography, languages, episode order, and ASR models define the boundary.

## 89. Extending the Fongbe to French Speech Translation Corpus:  resources, models and benchmark

**Paper:** [Extending the Fongbe to French Speech Translation Corpus:  resources, models and benchmark](https://www.isca-archive.org/interspeech_2025/kponou25_interspeech.html)
**Taxonomy:** `languages-accents-and-resources / crosslingual-structure / crosslingual-transfer`
**Evidence:** D3 full-paper capture; PDF SHA-256 `a36e93b7290c17345c54c825534cd24f8b12c18dca2597716a30348cb92f1da9`; full-text SHA-256 `e52e5cac3fbcddf68159285365f688789d108a64d016bb9fe53f0a442f513862`.

- **Ordinary problem:** Fongbe-to-French speech translation needs a benchmark and models that reflect the language rather than treating the low-resource direction as an afterthought.
- **Why it is hard:** Speech translation compounds transcription and translation errors, while limited speakers, orthography, and parallel data make evaluation noisy.
- **Naive attempt:** Translate a few examples with a multilingual model and compare scores without documenting the corpus or split.
- **Central move:** Extend the Fongbe-French speech-translation corpus, document resources and splits, and establish models and baselines for the direction.
- **Mechanism:** The paper extends the Fongbe-to-French speech translation corpus and presents resources, models, and a benchmark.
- **Mathematical idea:** Resource creation and modeling are one research object: a stable corpus fixes what progress means and reveals where transfer from high-resource languages fails.
- **What the paper reports:** The paper reports corpus additions, baseline models, and benchmark results for Fongbe-to-French speech translation.
- **Limits:** Corpus size, speakers, alignment, transcription, translation references, and split design bound generalization to Fongbe communities and other low-resource pairs.

## 90. ArticulateX: End-to-End Monolingual Speech Translation in Articulator Space

**Paper:** [ArticulateX: End-to-End Monolingual Speech Translation in Articulator Space](https://www.isca-archive.org/interspeech_2025/kumar25c_interspeech.html)
**Taxonomy:** `languages-accents-and-resources / crosslingual-structure / crosslingual-transfer`
**Evidence:** D3 full-paper capture; PDF SHA-256 `ad88b9e82119373fcc3596ceafb860ddafc50a6342923c50240909bd5911d912`; full-text SHA-256 `10f645235f52e75c197a5417c34471be7f8f4bbe5a480734cff5c4ab78204d1c`.

- **Ordinary problem:** Speech translation can use articulator movement as an intermediate signal, especially when the sound alone is ambiguous or the target language lacks data.
- **Why it is hard:** Articulator space is not directly observed in ordinary speech, and translation must preserve meaning while passing through a representation with its own measurement errors.
- **Naive attempt:** Translate acoustic features directly or force a text transcript and assume articulation adds nothing.
- **Central move:** Build an end-to-end monolingual speech-translation system that represents speech in articulator space and tests whether the intermediate structure helps.
- **Mechanism:** ArticulateX is an end-to-end monolingual speech translation system operating in articulator space.
- **Mathematical idea:** The proposed bridge changes the unit of translation: vocal-tract movement is treated as a structured intermediate constraint between sound and language.
- **What the paper reports:** The paper reports speech-translation results for the articulator-space system in its tested monolingual setting.
- **Limits:** Language, corpus, articulatory estimation, model, references, and evaluation bound generalization; an intermediate representation is not proof of human-like translation.

## 91. Novel Parasitic Dual-Scale Modeling for Efficient and Accurate Multilingual Speech Translation

**Paper:** [Novel Parasitic Dual-Scale Modeling for Efficient and Accurate Multilingual Speech Translation](https://www.isca-archive.org/interspeech_2025/le25_interspeech.html)
**Taxonomy:** `languages-accents-and-resources / crosslingual-structure / crosslingual-transfer`
**Evidence:** D3 full-paper capture; PDF SHA-256 `5a2aae41201302d203e55d5b73ee869936000d750b8cf46bd8fbdacf7197131f`; full-text SHA-256 `2d4eb9e8683cc14ce41a07b02282f009200a2bd2d78c064564c6f1c299a9234c`.

- **Ordinary problem:** A multilingual speech-translation system should serve many languages efficiently while preserving accuracy, rather than duplicating a full model for each direction.
- **Why it is hard:** Languages have different amounts of data and structures; sharing too much causes interference while separate modules waste parameters.
- **Naive attempt:** Use one monolithic model with uniform capacity or one model per language pair.
- **Central move:** Use a parasitic dual-scale design that shares efficient global structure while preserving language-specific detail for multilingual speech translation.
- **Mechanism:** The paper proposes novel parasitic dual-scale modeling for efficient and accurate multilingual speech translation.
- **Mathematical idea:** The model divides capacity by scale: shared computation handles reusable patterns, while finer or conditional structure protects language-specific translation behavior.
- **What the paper reports:** The paper reports multilingual translation accuracy and efficiency improvements for the tested language set.
- **Limits:** Languages, directions, data imbalance, parameter budget, decoding, and metrics bound the result; efficiency on a benchmark is not equal quality for every language.

## 92. Efficient Multilingual ASR Finetuning via LoRA Language Experts

**Paper:** [Efficient Multilingual ASR Finetuning via LoRA Language Experts](https://www.isca-archive.org/interspeech_2025/li25p_interspeech.html)
**Taxonomy:** `languages-accents-and-resources / crosslingual-structure / crosslingual-transfer`
**Evidence:** D3 full-paper capture; PDF SHA-256 `4333c2f1751ef8526e0053e1518c2cf22bbb5535470e92e04297e3ff1e974f0a`; full-text SHA-256 `d5f797f5004502f8edd7da954388d0d9f1c7cefc052f9ed361d4620e08a13770`.

- **Ordinary problem:** A multilingual ASR model should adapt efficiently to a language without overwriting what it knows about other languages.
- **Why it is hard:** Languages compete for shared parameters and have uneven data; full fine-tuning is costly and can cause interference or forgetting.
- **Naive attempt:** Fine-tune the entire model for each language or use one shared update for every language.
- **Central move:** Use language-specific LoRA experts so a shared base retains common speech structure while small expert updates handle language-specific differences.
- **Mechanism:** The paper proposes efficient multilingual ASR fine-tuning via LoRA language experts.
- **Mathematical idea:** Parameter-efficient adaptation allocates change selectively: shared parameters carry reusable acoustics while experts absorb language-specific pronunciation and decoding behavior.
- **What the paper reports:** The paper reports multilingual ASR accuracy and efficiency results for LoRA language experts.
- **Limits:** Languages, data balance, rank, routing, base model, and evaluation domains bound the claim; parameter efficiency does not guarantee fairness across languages.

## 93. LIST: Language-Independent Speech Token for Multilingual Speech Synthesis with Language Models

**Paper:** [LIST: Language-Independent Speech Token for Multilingual Speech Synthesis with Language Models](https://www.isca-archive.org/interspeech_2025/liu25o_interspeech.html)
**Taxonomy:** `languages-accents-and-resources / crosslingual-structure / crosslingual-transfer`
**Evidence:** D3 full-paper capture; PDF SHA-256 `4d4bc5177e2a91991c6585fc116e880e146a75587e274658b21f48ee4411092a`; full-text SHA-256 `dd3988d42e02d594082a0595a290cd7e3c3a0c7b0a4c4db8c64be20401f87493`.

- **Ordinary problem:** A multilingual speech synthesizer needs token units that can be shared across languages while still preserving language-specific pronunciation and rhythm.
- **Why it is hard:** Separate vocabularies waste capacity, while a universal token can erase distinctions or make the language model confuse languages.
- **Naive attempt:** Train one token set per language or force all languages into a text-like universal code without testing interference.
- **Central move:** Learn a language-independent speech token and use it with language-model synthesis across multiple languages.
- **Mechanism:** LIST is a language-independent speech token for multilingual speech synthesis with language models.
- **Mathematical idea:** The token is a cross-language interface: shared units carry reusable speech structure, while language conditioning reconstructs the differences needed for intelligible output.
- **What the paper reports:** The paper reports multilingual synthesis quality and cross-language token behavior for LIST.
- **Limits:** Languages, token rate, codebook, speakers, conditioning, and evaluation metrics bound the claim; shared tokens do not guarantee equal quality.

## 94. SawtArabi: A Benchmark Corpus for Arabic TTS.  Standard, Dialectal and Code-Switching

**Paper:** [SawtArabi: A Benchmark Corpus for Arabic TTS.  Standard, Dialectal and Code-Switching](https://www.isca-archive.org/interspeech_2025/lodagala25_interspeech.html)
**Taxonomy:** `languages-accents-and-resources / crosslingual-structure / crosslingual-transfer`
**Evidence:** D3 full-paper capture; PDF SHA-256 `8c7be2d612686223c24173ce133f1a9fb590944987c2a785b4481b837926d5a4`; full-text SHA-256 `5f359d9cae5f2ef0653ebbe614f87d852a6f57345d53a0fc7a461b64895c5cab`.

- **Ordinary problem:** Arabic TTS should handle standard, dialectal, and code-switched speech rather than presenting one standardized variety as all Arabic.
- **Why it is hard:** Pronunciation, vocabulary, rhythm, and switching behavior vary across varieties; data imbalance can make a model sound fluent only in the dominant subset.
- **Naive attempt:** Train on standard Arabic alone or concatenate dialect data without labeling the variety and switching context.
- **Central move:** Build a benchmark corpus covering standard, dialectal, and code-switched Arabic TTS with documented speakers, text, and evaluation.
- **Mechanism:** SawtArabi is a benchmark corpus for Arabic TTS spanning standard, dialectal, and code-switching speech.
- **Mathematical idea:** Corpus design exposes variation as a modeling requirement: the system must preserve identity and naturalness while changing or mixing language variety.
- **What the paper reports:** The paper reports corpus resources and baseline TTS evaluations across the covered Arabic conditions.
- **Limits:** Variety coverage, speaker balance, text design, switching labels, and listening tests bound generalization across Arabic communities.

## 95. Can we train ASR systems on Code-switch without real code-switch data? Case study for Singapore's languages

**Paper:** [Can we train ASR systems on Code-switch without real code-switch data? Case study for Singapore's languages](https://www.isca-archive.org/interspeech_2025/nguyen25_interspeech.html)
**Taxonomy:** `languages-accents-and-resources / crosslingual-structure / code-switching`
**Evidence:** D3 full-paper capture; PDF SHA-256 `5a13d223637e69fd8b427d504325887c9b35dfb2f851bc3c2e286e3da3f40061`; full-text SHA-256 `36c9b62eaa4f33891e59aacb5e93b38f88daaf0a6a5c5fef2881dd1586d45153`.

- **Ordinary problem:** Code-switched speech is common but expensive to transcribe, especially for under-resourced language pairs, so an ASR system needs useful mixed-language examples without requiring a new labeled corpus.
- **Why it is hard:** Switches occur at phrase boundaries and differ by language pair; naïvely concatenating monolingual data produces mixtures unlike spontaneous speech and may help one language while hurting another.
- **Naive attempt:** Fine-tune a pretrained ASR model only on monolingual data or create synthetic mixtures by randomly swapping isolated words.
- **Central move:** Generate phrase-level synthetic code-switching data from monolingual augmented speech, then use it to adapt large pretrained ASR models and evaluate several Southeast Asian language pairs.
- **Mechanism:** The paper creates phrase-mixed speech for Malay-English, Mandarin-Malay, and Tamil-English, fine-tunes Whisper, MMS, and SeamlessM4T, and compares monolingual and code-switched test performance against training without real code-switch recordings.
- **Mathematical idea:** The outcome is word error rate on monolingual and code-switched benchmarks, with gains compared across language pairs and pretrained models. The crucial design choice is the data distribution used for fine-tuning.
- **What the paper reports:** The authors report improved ASR on monolingual and code-switched tests, with the largest gains for BM-EN followed by TA-EN and ZH-BM.
- **Limits:** Synthetic phrase mixing is an approximation to spontaneous switching, and the three language pairs do not represent all multilingual communities. WER does not measure whether switches are socially or linguistically natural, and no independent reproduction was performed.

## 96. Simultaneous Speech Translation Integrated Compact Multiple Sound Spot Synthesis System On A Laptop Carried Out With A Backpack

**Paper:** [Simultaneous Speech Translation Integrated Compact Multiple Sound Spot Synthesis System On A Laptop Carried Out With A Backpack](https://www.isca-archive.org/interspeech_2025/okamoto25_interspeech.html)
**Taxonomy:** `languages-accents-and-resources / crosslingual-structure / crosslingual-transfer`
**Evidence:** D3 full-paper capture; PDF SHA-256 `a9663a91960630dcf06cd30e0044d8f153e52f7deaae90b7a4665ae7115ee98c`; full-text SHA-256 `b746dd1e44d22fff6c2d1c662c7dd84c754c50fcc06ce3cd1aeea0b171edbc43`.

- **Ordinary problem:** A compact system should translate simultaneous speech and produce multiple sound spots on a laptop carried in a backpack, without assuming a server or a quiet turn-taking environment.
- **Why it is hard:** Simultaneous speech translation combines overlap, latency, translation uncertainty, and spatial/audio output under tight compute and mobility constraints.
- **Naive attempt:** Wait for a complete utterance, send it to a large remote system, or treat translation and sound placement as separate problems.
- **Central move:** Integrate simultaneous speech translation with compact multiple-sound-spot synthesis in a portable system and evaluate the complete interaction loop.
- **Mechanism:** The paper presents a simultaneous speech-translation system integrated with compact multiple sound-spot synthesis on a laptop carried in a backpack.
- **Mathematical idea:** The system boundary is the product: recognition, translation, timing, and spatialized output must jointly meet latency and resource constraints rather than optimize isolated modules.
- **What the paper reports:** The paper reports an integrated portable-system demonstration and evaluation.
- **Limits:** Language pair, overlap conditions, hardware, latency measurement, and user setting limit generalization to broad simultaneous conversation.

## 97. CS-FLEURS: A Massively Multilingual and Code-Switched Speech Dataset

**Paper:** [CS-FLEURS: A Massively Multilingual and Code-Switched Speech Dataset](https://www.isca-archive.org/interspeech_2025/yan25c_interspeech.html)
**Taxonomy:** `languages-accents-and-resources / crosslingual-structure / code-switching`
**Evidence:** D3 full-paper capture; PDF SHA-256 `43f28c31052ef359ac60c11f4d703b713efd025eff12b87776c36f6a7b4c5019`; full-text SHA-256 `a0ca42703c091ba4fa6409af08dc79d38ed55069eab58ae86adc45d74d3f8b59`.

- **Ordinary problem:** Code-switched speech alternates languages within an utterance, so recognition must switch language and script expectations without losing context.
- **Why it is hard:** Whisper behavior differs sharply on code-switched speech, especially across scripts; synthetic speech may add artifacts.
- **Naive attempt:** Train on monolingual data and expect multilingual modeling to interpolate automatically.
- **Central move:** Build CS-FLEURS across 52 languages and 113 pairs, compare real and synthetic controls, and add synthetic code-switched training data.
- **Mechanism:** The corpus controls pair and switching conditions; experiments compare CER, direct translation, script pairs, and augmented training.
- **Mathematical idea:** Distinct-script CER is about 3x same-script CER; synthetic training lowers reported seen CER 14.38 to 12.67 and unseen 29.62 to 27.77.
- **What the paper reports:** Code-switched ASR is over twice as errorful as monolingual speech, while synthetic training improves seen and unseen pairs.
- **Limits:** Language pairs, synthetic voices, Whisper, CER, and controlled read speech limit natural-conversation claims.

## 98. Nosey: Open-Source Hardware for Acoustic Nasalance

**Paper:** [Nosey: Open-Source Hardware for Acoustic Nasalance](https://www.isca-archive.org/interspeech_2025/dewhurst25_interspeech.html)
**Taxonomy:** `languages-accents-and-resources / data-creation / speech-data-collection`
**Evidence:** D3 full-paper capture; PDF SHA-256 `539819ea64ce289148e7a69d77df8f9a3c88edec254a65b51fc3a8cf9ea94307`; full-text SHA-256 `c51bb22be12db650acbdecfaeef876ef1af46edc700e974c11eab740873eee3b`.

- **Ordinary problem:** Researchers and clinicians need to measure how much sound escapes through the nose, but commercial nasometers are expensive and hard to customize, limiting data collection across communities.
- **Why it is hard:** Nasalance is a ratio of nasal to total acoustic energy, so microphone placement, cross-signal bleed, baffle shape, and speaker anatomy can change the number even when the speech is comparable.
- **Naive attempt:** Infer nasality from a spectrum alone or treat a cheap two-microphone device as interchangeable with a commercial instrument without calibration.
- **Central move:** Build open hardware whose microphone, baffle, and analog path can be changed, then compare raw scores and phonological contrasts against a commercial device.
- **Mechanism:** Nosey is a 3-D-printable baffle with replaceable dual microphone clips and open files; the study compares it with an icSpeech device for speakers and phonological environments.
- **Mathematical idea:** Nasalance is computed as nasal energy divided by nasal plus oral energy; the important test is whether oral/nasal contrasts and their variation are preserved, not whether raw percentages match exactly.
- **What the paper reports:** Nosey produces consistently higher raw nasalance scores, but preserves comparable phonological-environment contrasts under the tested conditions and offers a lower-cost customizable platform.
- **Limits:** The tested speakers, microphones, baffle geometry, placement, and phonological materials bound the comparison; raw-score offsets and cross-signal bleed prevent treating Nosey and commercial values as directly interchangeable.

## 99. Transcribing Oral History Recordings Using the Transcription Portal

**Paper:** [Transcribing Oral History Recordings Using the Transcription Portal](https://www.isca-archive.org/interspeech_2025/draxler25_interspeech.html)
**Taxonomy:** `languages-accents-and-resources / data-creation / speech-data-collection`
**Evidence:** D3 full-paper capture; PDF SHA-256 `191e49f77c33f35a1dd6ed61d6e82f4a4a6b6064546fabe741942ad0ad0a7eb5`; full-text SHA-256 `96eb644d665d29719055eec6a3d03d45a5d73e319d58035740f77ffad1133c6c`.

- **Ordinary problem:** Archivists and communities need searchable transcripts of long oral-history recordings, but the people doing the work may not be speech engineers and the historical audio may be multilingual or difficult.
- **Why it is hard:** Automatic recognition is fast but imperfect, while manual correction is necessary; a fragmented toolchain makes it hard for a nontechnical user to move from audio to a trustworthy export.
- **Naive attempt:** Run a command-line ASR system and hand files between separate tools, or publish an automatic transcript without a correction path.
- **Central move:** Put recognition, human correction, and export into one preconfigured web workflow designed around the user's task rather than the model's internals.
- **Mechanism:** The Transcription Portal provides a GUI with three steps—ASR, manual correction, and data export—supports several languages, and demonstrates the workflow on historical Italian Ravensbrück interviews.
- **Mathematical idea:** The system treats human correction as part of the measurement pipeline: ASR supplies a draft, the user supplies local knowledge, and the exported transcript records the corrected artifact.
- **What the paper reports:** The paper reports a usable multilingual portal and demonstrates it on oral-history recordings, with summarization and translation identified as future extensions.
- **Limits:** The demonstration corpus, user effort, ASR model, correction time, and export format bound the result; a convenient workflow does not establish transcription accuracy without an error audit or independent user study.

## 100. The NaijaVoices Dataset: Cultivating Large-Scale, High-Quality, Culturally-Rich Speech Data for African Languages

**Paper:** [The NaijaVoices Dataset: Cultivating Large-Scale, High-Quality, Culturally-Rich Speech Data for African Languages](https://www.isca-archive.org/interspeech_2025/emezue25_interspeech.html)
**Taxonomy:** `languages-accents-and-resources / data-creation / speech-data-collection`
**Evidence:** D3 full-paper capture; PDF SHA-256 `0cb38fd800ae74f26db6d052b19963ad15ed7bcf95f987a51c51547297fb3755`; full-text SHA-256 `76bde374e59b83c576c629649e7d26916d3bc44883305e89e244a8091206d515`.

- **Ordinary problem:** People who speak Igbo, Hausa, or Yoruba need speech technology trained on enough varied speech to work beyond a few speakers.
- **Why it is hard:** African languages are underrepresented, and small or homogeneous datasets cannot expose speaker, accent, and recording variation.
- **Naive attempt:** Reuse large-resource-language data or build a small dataset without measuring its diversity.
- **Central move:** Collect a large, culturally grounded speech-text corpus and test whether it improves several ASR families.
- **Mechanism:** NaijaVoices contains 1,800 hours from more than 5,000 speakers; the paper analyzes acoustic diversity and fine-tunes Whisper, MMS, and XLSR.
- **Mathematical idea:** Word error rate compares models before and after the new data; corpus scale and speaker diversity are part of the intervention.
- **What the paper reports:** The paper reports average WER improvements of 75.86% for Whisper, 52.06% for MMS, and 42.33% for XLSR.
- **Limits:** The corpus languages, collection process, transcription policy, and model choices bound the result; coverage of other African languages and deployment conditions remains open.

## 101. Speech LLMs in Low-Resource Scenarios: Data Volume Requirements and the Impact of Pretraining on High-Resource Languages

**Paper:** [Speech LLMs in Low-Resource Scenarios: Data Volume Requirements and the Impact of Pretraining on High-Resource Languages](https://www.isca-archive.org/interspeech_2025/fong25_interspeech.html)
**Taxonomy:** `languages-accents-and-resources / data-creation / speech-data-collection`
**Evidence:** D3 full-paper capture; PDF SHA-256 `fac22cfbeb6d608eb6f1cf8296f731c70208dfd66a26f9e619bb0880769bf091`; full-text SHA-256 `2c80af5c3998bc194ca58a7006ff5d4064f04777c0c987e5e95e4fefd5998305`.

- **Ordinary problem:** A speech language model trained mostly on high-resource languages may need to recognize a low-resource language from very little labeled speech.
- **Why it is hard:** The model must connect acoustic evidence to a language model while learning with too few examples; pretraining can transfer useful structure but can also favor the languages that supplied it.
- **Naive attempt:** Train the entire speech-language system from scratch in the low-resource language, or assume a large multilingual model automatically solves the data shortage.
- **Central move:** Pretrain the small bridge between a speech encoder and language model on high-resource languages, then reuse it and measure how much low-resource data is still needed.
- **Mechanism:** Using SLAM-ASR with Whisper-large-v3-turbo and multilingual or monolingual LLMs, the paper varies training volume and projector pretraining, including Galician benchmarks.
- **Mathematical idea:** The projector is a learned translation between acoustic representations and language-model tokens; data-volume curves distinguish transferred alignment from new language-specific learning, while WER measures recognition.
- **What the paper reports:** The paper reports that multilingual projector pretraining reduces the impact of scarce data; for Galician it reports WERs such as 13.3% on Common Voice and 19.4% on FLEURS in one configuration.
- **Limits:** Language choice, data cleanliness, projector, LLM, benchmark split, and WER bound the claim; transfer from high-resource languages does not establish equal performance or cultural adequacy.

## 102. Automatic Speech Recognition for Low-Resourced Middle Eastern Languages

**Paper:** [Automatic Speech Recognition for Low-Resourced Middle Eastern Languages](https://www.isca-archive.org/interspeech_2025/hameed25_interspeech.html)
**Taxonomy:** `languages-accents-and-resources / data-creation / speech-data-collection`
**Evidence:** D3 full-paper capture; PDF SHA-256 `d86d646bd51794bd20b4b19801617990151586086845a6317898818b1a5e17c8`; full-text SHA-256 `0aa9c97cc5df2e7cbefb01afce7a502edc534d9c5f234837229448eea9d01be5`.

- **Ordinary problem:** Many Middle Eastern languages need speech recognition but have little transcribed data, tools, or standardized evaluation.
- **Why it is hard:** Language variety, script, dialect, speaker access, and scarce labels interact; multilingual transfer may help one variety while obscuring another.
- **Naive attempt:** Fine-tune a high-resource recognizer on a tiny sample and report one score without documenting the language or split.
- **Central move:** Build and evaluate ASR resources for low-resourced Middle Eastern languages, making language-specific data and transfer limits explicit.
- **Mechanism:** The paper studies automatic speech recognition for low-resourced Middle Eastern languages.
- **Mathematical idea:** Low-resource ASR is an infrastructure problem as well as a model problem: a documented corpus and baseline expose which errors come from missing data versus model choice.
- **What the paper reports:** The paper reports resources, baselines, and recognition results for the covered Middle Eastern languages.
- **Limits:** Language selection, dialect, corpus size, transcription, speakers, and evaluation splits limit generalization across the region.

## 103. Hybrid Data Sampling for ASR: Integrating Acoustic Diversity and Transcription Uncertainty

**Paper:** [Hybrid Data Sampling for ASR: Integrating Acoustic Diversity and Transcription Uncertainty](https://www.isca-archive.org/interspeech_2025/hiruta25_interspeech.html)
**Taxonomy:** `languages-accents-and-resources / data-creation / speech-data-collection`
**Evidence:** D3 full-paper capture; PDF SHA-256 `913e88bbe1eb7c06bc13222f3c7d69778a84276fa9cbc8ac75419dffe40f99ab`; full-text SHA-256 `7e989907a7ab9e444acd9b885bb75ad8354587cb138d45962da3198e1bd2f9b4`.

- **Ordinary problem:** An ASR training set should cover acoustic diversity and should spend labeling effort where the transcription is uncertain.
- **Why it is hard:** Random sampling can overrepresent easy or similar speech, while uncertainty-only sampling can repeat rare errors without broad acoustic coverage.
- **Naive attempt:** Sample randomly, or rank clips by model uncertainty alone and call the resulting set diverse.
- **Central move:** Combine acoustic-diversity measures with transcription uncertainty when selecting training data, then test the effect on ASR.
- **Mechanism:** The paper proposes hybrid data sampling for ASR by integrating acoustic diversity and transcription uncertainty.
- **Mathematical idea:** Data selection is a coverage-allocation problem: diversity broadens the conditions seen, while uncertainty targets the model's unresolved boundary.
- **What the paper reports:** The paper reports ASR improvements from hybrid sampling relative to the tested selection strategies.
- **Limits:** Acoustic representation, uncertainty estimator, corpus, budget, language, and split bound the result; a sampling score is not a complete measure of data value.

## 104. An Exploratory Framework for LLM-assisted Human Annotation of Speech Datasets

**Paper:** [An Exploratory Framework for LLM-assisted Human Annotation of Speech Datasets](https://www.isca-archive.org/interspeech_2025/johnson25_interspeech.html)
**Taxonomy:** `languages-accents-and-resources / data-creation / speech-data-collection`
**Evidence:** D3 full-paper capture; PDF SHA-256 `a6c7b02826dce5c09a6bc7116c364e213935cb8a7a01a1dd86bc3e2d2bd3d7e3`; full-text SHA-256 `7212e9b9ee8560f0bcb6f41e3a7acd47209cc3e25e8fbd561d8b7042152a122c`.

- **Ordinary problem:** Annotating speech datasets is expensive, but letting an LLM help humans can introduce confident mistakes or erase disagreements that matter.
- **Why it is hard:** Speech labels depend on audio quality, context, dialect, and task definitions; an assistant can accelerate work only if people can inspect and correct its suggestions.
- **Naive attempt:** Accept LLM labels automatically or use humans without recording where model assistance changed a decision.
- **Central move:** Build an exploratory human-in-the-loop framework for LLM-assisted speech annotation with review, uncertainty, and provenance.
- **Mechanism:** The paper presents an exploratory framework for LLM-assisted human annotation of speech datasets.
- **Mathematical idea:** Annotation is a coordination loop: the model proposes, the human adjudicates, and the system records evidence so speed does not replace accountability.
- **What the paper reports:** The paper reports framework behavior and exploratory annotation findings for the tested speech data tasks.
- **Limits:** Task, annotator expertise, model, prompts, disagreement policy, and audit trail bound the result; assistance is not a substitute for label validity.

## 105. Speech Annotation for A: Accuracy, Access, and Application

**Paper:** [Speech Annotation for A: Accuracy, Access, and Application](https://www.isca-archive.org/interspeech_2025/li25ea_interspeech.html)
**Taxonomy:** `languages-accents-and-resources / data-creation / speech-data-collection`
**Evidence:** D3 full-paper capture; PDF SHA-256 `d2d2abb318b699f3d948b6f6b6cedca25777b35d100371bbc0a6ecdd0165e8a2`; full-text SHA-256 `68d258301ab49bacf66a29cf90bc43ec638ea47bd44f174395993e3e2b653a10`.

- **Ordinary problem:** Clinical speech research needs accurate bilingual, multi-speaker, time-aligned annotations, but clinicians cannot spend unlimited time learning complex tools or correcting opaque automatic transcripts.
- **Why it is hard:** Full automation can silently change words, speakers, languages, and timestamps; fully manual annotation is slow and difficult to scale, especially in code-switched recordings.
- **Naive attempt:** Choose either an automatic transcript with no review or a powerful annotation suite that leaves all alignment and metadata work to a specialist.
- **Central move:** Keep the model-generated draft but make human correction cheap: edit in synchronized chunks, highlight every difference, tag speaker/language explicitly, and export structured research files.
- **Mechanism:** SAFA combines Whisper and diarization drafts with a PyQt6 interface. Chunk navigation follows playback, original and edited text/tags/timestamps are compared in real time, language and speaker labels are selectable, and CSV/SRT/TXT exports preserve the corrected record.
- **Mathematical idea:** The central object is an auditable annotation state rather than a prediction score: every edit is exposed to a human. The paper’s evidence is a workflow/design demonstration, not a controlled accuracy study with a fixed annotation denominator.
- **What the paper reports:** The paper presents an end-to-end bilingual clinical annotation workflow intended to reduce setup and manual effort while retaining human validation and structured metadata for downstream research.
- **Limits:** The paper does not report a controlled user study, annotation-time reduction, inter-annotator agreement, or clinical outcome. Whisper/diarization errors and supported language choices remain boundaries; tool availability is not independent execution.

## 106. The Faetar Speech Recognition Benchmark

**Paper:** [The Faetar Speech Recognition Benchmark](https://www.isca-archive.org/interspeech_2025/ong25_interspeech.html)
**Taxonomy:** `languages-accents-and-resources / data-creation / speech-data-collection`
**Evidence:** D3 full-paper capture; PDF SHA-256 `09a5323c1f73cf0215459bcc86d80b04ed3ec63db55bf4c49e725b649485afcd`; full-text SHA-256 `3da4bc2a1fd88078f6c0e8b23af27bbab8a47be11280e365cc6757d22a559720`.

- **Ordinary problem:** A low-resource language needs an honest speech-recognition benchmark before claims about progress can be compared.
- **Why it is hard:** Small corpora make train/test estimates unstable, spelling and dialect choices affect labels, and a benchmark can expose gaps without solving data scarcity.
- **Naive attempt:** Report one model score on a tiny corpus and treat it as a general language capability estimate.
- **Central move:** Build the Faetar speech-recognition benchmark with documented recordings, splits, transcripts, and evaluation so later systems can be compared on the same problem.
- **Mechanism:** The paper introduces the Faetar Speech Recognition Benchmark.
- **Mathematical idea:** Benchmark construction is part of scientific knowledge: the dataset fixes what counts as an error and makes future improvements distinguishable from changes in collection or split.
- **What the paper reports:** The paper reports the benchmark resources and baseline recognition results for Faetar.
- **Limits:** Corpus size, speakers, dialect coverage, transcription conventions, and split design bound conclusions about the wider language community.

## 107. LiRI Corpus Platform: Demonstration of a Web-Based Infrastructure for Multimodal Corpus Analysis

**Paper:** [LiRI Corpus Platform: Demonstration of a Web-Based Infrastructure for Multimodal Corpus Analysis](https://www.isca-archive.org/interspeech_2025/vukovic25_interspeech.html)
**Taxonomy:** `languages-accents-and-resources / data-creation / speech-data-collection`
**Evidence:** D3 full-paper capture; PDF SHA-256 `8f138214b31c0ab0e8ae7475e60931c664154f26806d0a9695ac60aa9b97096b`; full-text SHA-256 `654e597b08a647c57aad800e0df77b75f1491c733a510c6b59cd91be76abcf53`.

- **Ordinary problem:** Researchers need to ask questions that connect speech, text, video, gesture, and annotation layers without rebuilding a separate tool for each corpus.
- **Why it is hard:** Multimodal data are time-aligned but stored and queried in different systems, so a text-only search can miss the speech or gesture event that gives a segment meaning.
- **Naive attempt:** Keep each modality in a separate application and manually synchronize results.
- **Central move:** Provide one corpus platform with a shared query language, synchronized audiovisual views, and layered annotation that can be queried across modalities.
- **Mechanism:** The LiRI Corpus Platform stores and explores multimodal corpora through DQD queries and time-aligned frontends for text, audio, video, gesture, and spoken transcripts.
- **Mathematical idea:** The central object is a cross-modal query over aligned annotation intervals; the platform is evaluated by the operations it makes expressible rather than by a classifier score.
- **What the paper reports:** The paper demonstrates integrated storage, synchronized querying, layered annotation, and modality-specific frontends for multimodal corpus analysis.
- **Limits:** This is an infrastructure demonstration, not evidence that every corpus can be aligned or that research conclusions improve; supported formats, annotations, and user workflows are the boundary.

## 108. AfriHuBERT: A self-supervised speech representation model for African languages

**Paper:** [AfriHuBERT: A self-supervised speech representation model for African languages](https://www.isca-archive.org/interspeech_2025/alabi25_interspeech.html)
**Taxonomy:** `languages-accents-and-resources / low-resource-learning / self-training-and-pseudo-labels`
**Evidence:** D3 full-paper capture; PDF SHA-256 `67dc81680f8f4ef20486538fcd8595aa8d1558f51c9c26a29f95f6e9e6ee2e53`; full-text SHA-256 `1181bd8abd5964806470f7478c8ee43c55b67b19a48ebb1448bb3874631c458d`.

- **Ordinary problem:** Provide reusable speech knowledge for African languages that have little labeled training data.
- **Why it is hard:** A model trained mostly on well-resourced languages has seen too few sound patterns and recording conditions from many African languages to learn useful units for them.
- **Naive attempt:** Apply a multilingual model unchanged and assume language count alone means coverage.
- **Central move:** Continue pretraining a compact HuBERT-style model on a much wider set of African-language audio, then test whether the shared representation transfers to downstream tasks.
- **Mechanism:** Unlabeled audio is converted into masked prediction targets; the encoder learns from contextual speech patterns across languages and is then adapted for recognition and language-related tasks.
- **Mathematical idea:** The pretraining objective predicts hidden or clustered speech units from surrounding frames; downstream scores measure whether those units support task labels with limited supervision.
- **What the paper reports:** The paper reports a representation model expanded to 1,226 African languages and evaluates its transfer against multilingual baselines.
- **Limits:** Language coverage does not mean equal data quality or equal downstream performance; the languages, hours, speaker balance, and task results determine the practical reach. No independent reproduction was performed.

## 109. Evaluating Large Language Models in Data Generation for Low-Resource Scenarios: A Case Study on Question Answering

**Paper:** [Evaluating Large Language Models in Data Generation for Low-Resource Scenarios: A Case Study on Question Answering](https://www.isca-archive.org/interspeech_2025/arisoy25_interspeech.html)
**Taxonomy:** `languages-accents-and-resources / low-resource-learning / self-training-and-pseudo-labels`
**Evidence:** D3 full-paper capture; PDF SHA-256 `bd94133ab93c4b82d4218f8da7999e2f3f4a68d5f6f980763c8520bb83cb0c5b`; full-text SHA-256 `47fc4b07f32eb2db02a75d7c7070d3a96b767601b672eb8822abc221f3b0179e`.

- **Ordinary problem:** A spoken question-answering system needs training examples even when a language has little labeled data.
- **Why it is hard:** Synthetic text can be plentiful but may not resemble spoken questions; gains can come from artifacts or from better coverage, and the two must be separated.
- **Naive attempt:** Generate arbitrary question-answer pairs or train only on the small human set and assume more text automatically transfers to speech.
- **Central move:** Use large-language-model-generated question-answer data and test its value separately on text QA, spoken QA, and Turkish spoken QA.
- **Mechanism:** The study evaluates LLM-generated data for low-resource spoken QA across SQuAD, Spoken SQuAD, and Turkish spoken QA.
- **Mathematical idea:** Data generation is a controlled source of coverage: the useful question is not whether synthetic examples look plausible, but whether they improve the target speech task under restricted human supervision.
- **What the paper reports:** The paper reports relative F1 gains over restricted human-annotated training in the tested text and spoken QA settings.
- **Limits:** Prompting, filtering, language, synthetic distribution, and evaluation splits limit transfer; synthetic gains do not establish factual or linguistic quality everywhere.

## 110. Better Semi-supervised Learning for Multi-domain ASR Through Incremental Retraining and Data Filtering

**Paper:** [Better Semi-supervised Learning for Multi-domain ASR Through Incremental Retraining and Data Filtering](https://www.isca-archive.org/interspeech_2025/carofilis25_interspeech.html)
**Taxonomy:** `languages-accents-and-resources / low-resource-learning / self-training-and-pseudo-labels`
**Evidence:** D3 full-paper capture; PDF SHA-256 `0b0ae771e24a39cd0c481ffd12f36450ae1ce797c733e66e321461549c6d8f7d`; full-text SHA-256 `e8fb7c2dbe60fa449b64b0860863c52335911454e4038fe8482bb302e75d7950`.

- **Ordinary problem:** A recognizer needs to adapt to a new domain when only a little labeled speech is available but related audio is abundant.
- **Why it is hard:** Unlabeled audio can add coverage but can also inject wrong pseudo-labels and reinforce domain errors.
- **Naive attempt:** Fine-tune once on the small labeled set or choose pseudo-labels randomly.
- **Central move:** Incrementally combine in-domain labels with related-domain data, then filter pseudo-labels using multi-model consensus or named-entity recognition.
- **Mechanism:** The pipeline retrains in stages and uses agreement or entity preservation to decide which generated transcripts enter the next training round.
- **Mathematical idea:** Data selection is treated as part of learning: the value of unlabeled speech depends on which errors are admitted, not only on how much audio is added.
- **What the paper reports:** The paper reports up to 22.3% relative improvement on Wow and 24.8% on Fisher over random selection, with consensus strongest and NER cheaper.
- **Limits:** The gains are bounded to the two English corpora, model ensemble, filtering thresholds, and author-reported WER; other domains and languages remain unresolved.

## 111. MSDA: Combining Pseudo-labeling and Self-Supervision for Unsupervised Domain Adaptation in ASR

**Paper:** [MSDA: Combining Pseudo-labeling and Self-Supervision for Unsupervised Domain Adaptation in ASR](https://www.isca-archive.org/interspeech_2025/damianos25_interspeech.html)
**Taxonomy:** `languages-accents-and-resources / low-resource-learning / self-training-and-pseudo-labels`
**Evidence:** D3 full-paper capture; PDF SHA-256 `233530f3ab0d6ed7c8109727fac796e34a937320113dca8862414ace505d4156`; full-text SHA-256 `d87b3487ab32f087a5f2eed08ac65766ef208f4e4567f9c7ba4548809b7c26b9`.

- **Ordinary problem:** ASR should adapt to a new or low-resource domain when labels are scarce or noisy.
- **Why it is hard:** Pseudo-label errors can reinforce themselves, while self-supervised adaptation alone may not learn the task boundary.
- **Naive attempt:** Fine-tune only on the small labeled target set or apply one adaptation technique in isolation.
- **Central move:** Cascade self-supervised representation adaptation with pseudo-label training so each stage prepares the next.
- **Mechanism:** MSDA evaluates a two-stage Meta PL pipeline for Greek and weakly supervised ASR, with ablations of the cascade.
- **Mathematical idea:** Recognition error and ablations test whether the order of self-supervision and self-training matters.
- **What the paper reports:** The paper reports state-of-the-art results and finds the cascading combination necessary in its experiments.
- **Limits:** The languages, pseudo-label quality, source models, and domain shifts bound the claim; robustness to severely wrong pseudo-labels remains open.

## 112. Speechless: Speech Instruction Training Without Speech for Low Resource Languages

**Paper:** [Speechless: Speech Instruction Training Without Speech for Low Resource Languages](https://www.isca-archive.org/interspeech_2025/dao25_interspeech.html)
**Taxonomy:** `languages-accents-and-resources / low-resource-learning / few-shot-adaptation`
**Evidence:** D3 full-paper capture; PDF SHA-256 `4c081f92f821e684db02d1d96bd2435c1f07cf2fc0418883f6f01669e2343eea`; full-text SHA-256 `101e984abba4fdf913b4cb08063a64260b000c588806ab04846991c39f4dbf19`.

- **Ordinary problem:** A voice assistant needs spoken command examples in a low-resource language, but there may be no good text-to-speech system with which to synthesize them.
- **Why it is hard:** Text instructions and spoken instructions share meaning but not the same signal, so training only on text risks losing the acoustic path needed at inference time.
- **Naive attempt:** Translate text instructions into speech with a weak TTS system, or fine-tune only on written commands and hope the speech encoder bridges the gap.
- **Central move:** Generate synthetic instruction examples only up to a semantic representation, align those representations with a pretrained speech encoder, and train the language model without waveform synthesis.
- **Mechanism:** Speechless uses text-generated instructions, aligns their semantic representations with Whisper encoder representations, and fine-tunes an LLM so it can process spoken commands in low-resource settings.
- **Mathematical idea:** The method removes the unavailable waveform generator from the training loop while retaining a shared semantic space; alignment is the bridge between written supervision and spoken input.
- **What the paper reports:** The paper reports that speech-instruction training without TTS can preserve spoken-instruction understanding and offers a simpler route for low-resource languages.
- **Limits:** The language, synthetic text, Whisper encoder, alignment quality, and downstream command tasks bound the result; semantic alignment is not proof that pronunciation, prosody, or real user speech are fully represented.

## 113. Multi-view Fusion and Parameter Perturbation for Few-Shot Class-Incremental Audio Classification

**Paper:** [Multi-view Fusion and Parameter Perturbation for Few-Shot Class-Incremental Audio Classification](https://www.isca-archive.org/interspeech_2025/fang25d_interspeech.html)
**Taxonomy:** `languages-accents-and-resources / low-resource-learning / few-shot-adaptation`
**Evidence:** D3 full-paper capture; PDF SHA-256 `ae7de64989102b169031e6e41dfaf5444fbb603a12d215d472122244a415cf27`; full-text SHA-256 `e5cd2daf512e31a1eea150814d990eae16304a3adda8902d58cd20c544a71143`.

- **Ordinary problem:** An audio classifier may need to learn new classes one at a time with only a few examples, without forgetting classes it already knows.
- **Why it is hard:** The class vocabulary changes and few examples encourage overfitting; a representation that works for old classes may not expose the right view for new ones.
- **Naive attempt:** Fine-tune on each new class and accept forgetting, or keep fixed prototypes and ignore representation drift.
- **Central move:** Fuse multiple views of the audio and perturb parameters during few-shot class-incremental learning to improve coverage and reduce overfitting.
- **Mechanism:** The paper proposes multi-view fusion and parameter perturbation for few-shot class-incremental audio classification.
- **Mathematical idea:** Adaptation is a balance between plasticity and retention: multiple views supply evidence while controlled perturbation tests whether a decision is stable rather than memorized.
- **What the paper reports:** The paper reports class-incremental classification results against the tested baselines.
- **Limits:** Class order, shots, audio domains, perturbation settings, and memory protocol bound the result; benchmark retention does not establish lifelong robustness.

## 114. Evaluating Wav2Vec2-Bert for Computer-Assisted Pronunciation Training for isiZulu

**Paper:** [Evaluating Wav2Vec2-Bert for Computer-Assisted Pronunciation Training for isiZulu](https://www.isca-archive.org/interspeech_2025/fort25_interspeech.html)
**Taxonomy:** `languages-accents-and-resources / low-resource-learning / few-shot-adaptation`
**Evidence:** D3 full-paper capture; PDF SHA-256 `ada6f98045ba930be437c40618e001ba13a4532c399ef1acee8404c722f33a57`; full-text SHA-256 `86eb30c5166ba3e06cd59bde8f80708fdb8d91a5926fd32b9aa757144915c912`.

- **Ordinary problem:** Pronunciation feedback for isiZulu learners needs a recognizer that understands the language and can identify the learner's phoneme errors despite limited labeled data.
- **Why it is hard:** Native and learner recordings differ in speaking style and domain; isiZulu's agglutinative words make character and word errors behave differently, and the gold labels mark an error without always identifying the produced phone.
- **Naive attempt:** Fine-tune on one corpus and treat its output as a complete diagnostic pronunciation label, or transfer a model trained on careful teacher speech directly to natural learner speech.
- **Central move:** Compare Wav2Vec2-BERT models fine-tuned on native isiZulu, learner speech, and both, then evaluate transcription and phoneme-error detection separately.
- **Mechanism:** The study uses NCHLT native speech, L2 isiZulu learner speech, and teacher recordings. Models are fine-tuned with the same setup; phoneme alignment uses Needleman–Wunsch, and error labels are evaluated with false acceptance, false rejection, and true-negative rates.
- **Mathematical idea:** On the NCHLT test set, the NCHLT-trained model reports WER 0.126 and CER 0.0237, versus WER 0.667 for the L2-only model and 0.141 for the combined model. For phoneme errors, the L2 model has FAR 2.2%, FRR 16.1%, and TNR 65.1%; the model cannot compute a full diagnostic error rate because the gold labels omit the learner's produced phone.
- **What the paper reports:** Native-speech transcription is strongest for the NCHLT-trained model, while the L2-trained model detects the most incorrect phonemes under the available true-negative measure; the authors release code and identify the data sources.
- **Limits:** The results depend on three isiZulu corpora, their recording styles, and incomplete phoneme-error labels. Tone is not evaluated because it is not marked orthographically; findings do not automatically transfer to other languages or pronunciation tasks.

## 115. Few-Shot Speech Deepfake Detection Adaptation with Gaussian Processes

**Paper:** [Few-Shot Speech Deepfake Detection Adaptation with Gaussian Processes](https://www.isca-archive.org/interspeech_2025/glazer25_interspeech.html)
**Taxonomy:** `languages-accents-and-resources / low-resource-learning / few-shot-adaptation`
**Evidence:** D3 full-paper capture; PDF SHA-256 `87036d54708344c13d2df0d861254d434131a0770e5fd25ab25c3d85fd2b7027`; full-text SHA-256 `c30b58acb0875491ad4d9535f36fd8e209dcfd02079cd227cd94ce60f7906f42`.

- **Ordinary problem:** A new speech deepfake attack may appear with only a few labeled examples, so detection must adapt without retraining a large model from scratch.
- **Why it is hard:** Few examples make neural updates unstable, while the new attack may occupy a different part of acoustic space from old attacks.
- **Naive attempt:** Fine-tune all parameters on the few examples or use a fixed detector and accept failure on the new attack.
- **Central move:** Use Gaussian-process adaptation to express uncertainty and update the detector from scarce examples.
- **Mechanism:** The paper studies few-shot adaptation for speech deepfake detection with Gaussian processes.
- **Mathematical idea:** The probabilistic adapter separates learning the new attack boundary from pretending that a few examples define it with certainty; uncertainty can guide conservative decisions.
- **What the paper reports:** The paper reports few-shot detection adaptation results against the tested baselines.
- **Limits:** Attack families, kernel choices, calibration, shots, and base detector limit generalization; uncertainty estimates are not automatically reliable under distribution shift.

## 116. Pushing the Limits of Beam Search Decoding  for Transducer-based ASR models

**Paper:** [Pushing the Limits of Beam Search Decoding  for Transducer-based ASR models](https://www.isca-archive.org/interspeech_2025/grigoryan25_interspeech.html)
**Taxonomy:** `languages-accents-and-resources / low-resource-learning / self-training-and-pseudo-labels`
**Evidence:** D3 full-paper capture; PDF SHA-256 `c258bb48da5a266ef648bca8979f53c611efe9e0fe3bdb6de364ccb56d65fa5e`; full-text SHA-256 `965a0700a3415d496172ccb63133535af0e158273ebca76c4bcdb29226876148`.

- **Ordinary problem:** An ASR decoder must choose a likely word sequence efficiently, but beam search can miss a better path or spend too much computation on unhelpful alternatives.
- **Why it is hard:** Transducer scores are local while the best sequence is global; beam width, pruning, and length effects interact with streaming constraints.
- **Naive attempt:** Increase the beam indefinitely or use greedy decoding and assume the accuracy/latency tradeoff is universal.
- **Central move:** Analyze and improve beam-search decoding for transducer ASR, testing how search choices affect accuracy and computation.
- **Mechanism:** The paper pushes the limits of beam-search decoding for transducer-based ASR models.
- **Mathematical idea:** Decoding is an inference budget: the beam is a controlled approximation to sequence search, and improvements come from spending computation where competing hypotheses remain plausible.
- **What the paper reports:** The paper reports decoding accuracy and efficiency findings for transducer ASR across the tested search settings.
- **Limits:** Model, language, beam policy, pruning, hardware, and streaming setup bound the result; a better beam does not remove acoustic or language-model errors.

## 117. An Effective Training Framework for Light-Weight Automatic Speech Recognition Models

**Paper:** [An Effective Training Framework for Light-Weight Automatic Speech Recognition Models](https://www.isca-archive.org/interspeech_2025/hannan25b_interspeech.html)
**Taxonomy:** `languages-accents-and-resources / low-resource-learning / few-shot-adaptation`
**Evidence:** D3 full-paper capture; PDF SHA-256 `65e7356d7adb8a2bd49304d18bb00d9cb7fa03f23d057d61f907e709db885afe`; full-text SHA-256 `abe41cc4e53b145ce8cc7439b384b6db20f1c0d662f55e2d437bd39456909776`.

- **Ordinary problem:** A speech recognizer for a device with little compute should remain useful without the memory and delay of a large model.
- **Why it is hard:** Accuracy, model size, latency, and energy pull in different directions, especially when training data and target hardware are limited.
- **Naive attempt:** Shrink a large model after training or use a tiny architecture and accept that accuracy is unrelated to the resource budget.
- **Central move:** Design a training framework that improves lightweight ASR while measuring the accuracy-resource tradeoff directly.
- **Mechanism:** The paper proposes an effective training framework for lightweight automatic speech-recognition models.
- **Mathematical idea:** Efficiency is a constraint on the whole training-and-inference pipeline: the model must spend its limited capacity on speech distinctions that matter for the target device.
- **What the paper reports:** The paper reports lightweight ASR accuracy and resource results for the proposed framework.
- **Limits:** Hardware, language, model family, data, latency measurement, and compression settings limit generalization; a benchmark model is not a deployment guarantee.

## 118. Discovering Directions of Uncertainty in Speech Inpainting

**Paper:** [Discovering Directions of Uncertainty in Speech Inpainting](https://www.isca-archive.org/interspeech_2025/cohen25_interspeech.html)
**Taxonomy:** `listening-and-separation / echo-reconstruction / packet-loss-concealment`
**Evidence:** D3 full-paper capture; PDF SHA-256 `f29513688bc8a688433c61314f1132da363c44faac012935d937c1eadb2a6c81`; full-text SHA-256 `393a999a0fd82d9165a43d7faa4c70167eec756ecb6d6109542d41ebb94cb2ee`.

- **Ordinary problem:** When speech is inpainted, several completions may fit the observed context, so uncertainty is part of the missing-sound problem.
- **Why it is hard:** A single plausible waveform hides whether the missing content was determined by the evidence.
- **Naive attempt:** Return one deterministic reconstruction and treat residual error as the only uncertainty signal.
- **Central move:** Use Neural Principal Probability Components to represent the posterior over possible inpaintings and compare it with dropout sampling.
- **Mechanism:** NPPC predicts principal components of the conditional output distribution; traversing components produces alternative spectrograms and transcripts.
- **Mathematical idea:** NPPC is reported as 50x faster than 50-sample MC Dropout with slightly better reconstruction error.
- **What the paper reports:** Principal directions change word identity and pitch; NPPC captures diverse outputs while matching or improving dropout error.
- **Limits:** The data, posterior approximation, audio examples, and benchmark define the result; calibration and user decision rules remain unresolved.

## 119. Extended Loss: Incorporating Long Context into Training Models when using Short Audio Frames

**Paper:** [Extended Loss: Incorporating Long Context into Training Models when using Short Audio Frames](https://www.isca-archive.org/interspeech_2025/dinh25_interspeech.html)
**Taxonomy:** `listening-and-separation / echo-reconstruction / packet-loss-concealment`
**Evidence:** D3 full-paper capture; PDF SHA-256 `c9b4b8d80caa6c5af43e9d12e87173c3dbc5f55c5d7ef28ab9d8e3a45f31bc37`; full-text SHA-256 `9556316ecb5bffd6e63e47d96f76aab7b63d102932336ae7bab7f9a39a7e0f01`.

- **Ordinary problem:** A real-time echo canceller may process only 10-ms frames, but each frame still needs enough surrounding context to avoid audible boundary glitches.
- **Why it is hard:** Long context can improve continuity but usually adds delay; short-frame training exposes boundaries that long offline examples hide.
- **Naive attempt:** Use long frames, add post-processing, or train on isolated short chunks and accept discontinuities.
- **Central move:** Keep long-context information in each training batch while producing short-frame outputs, so the model learns continuity without increasing application delay.
- **Mechanism:** The paper proposes Extended Loss for acoustic echo cancellation with short audio frames and limited latency.
- **Mathematical idea:** The loss supervises the local output using context that spans frame boundaries; training context and inference delay are separated rather than traded as the same quantity.
- **What the paper reports:** The paper reports reduced boundary discontinuities and improved short-frame AEC performance under the tested real-time conditions.
- **Limits:** Echo paths, frame size, batch context, hardware, and evaluation signals bound the claim; continuity on the benchmark is not proof of every room or device.

## 120. Rollback Speech: Smart Feedback Prompts for Lost Utterances in Unstable Online Calls

**Paper:** [Rollback Speech: Smart Feedback Prompts for Lost Utterances in Unstable Online Calls](https://www.isca-archive.org/interspeech_2025/quinterovillalobos25_interspeech.html)
**Taxonomy:** `listening-and-separation / echo-reconstruction / packet-loss-concealment`
**Evidence:** D3 full-paper capture; PDF SHA-256 `d95a727348dd6d3a942095bb1361ac92bffd7eff22e7bd0f74b1265ad2fbacae`; full-text SHA-256 `881cc68f342088010771638ce3b58fef691a1d123d4482137b6b2eef20851199`.

- **Ordinary problem:** In an unstable online call, a speaker may continue talking while the listener never receives part of the utterance.
- **Why it is hard:** The system must identify what was lost without treating an incomplete remote transcript as complete, then request a short useful repair rather than forcing a full repetition.
- **Naive attempt:** Assume the call is reliable, or ask the speaker to repeat everything after any connection failure.
- **Central move:** Compare local and remote ASR streams, identify unreceived content after reconnection, extract keywords from the missing segment, and prompt the speaker to repeat only the relevant information.
- **Mechanism:** The system is an interaction loop: dual transcripts provide two views of the communication event, discrepancy detection estimates the missing interval, and keyword extraction compresses the repair request into actionable cues.
- **Mathematical idea:** This is not waveform packet-loss concealment. It preserves conversational meaning through human-in-the-loop selective repetition when acoustic reconstruction is unsafe or unavailable.
- **What the paper reports:** The paper demonstrates a WebRTC/WebSocket prototype using Whisper and NLTK keyword extraction in a simulated brief disconnection; it is a show-and-tell feasibility demonstration rather than a controlled recovery benchmark.
- **Limits:** Two-person demonstration conditions, simulated network failure, ASR errors, keyword quality, privacy/latency trade-offs, and absence of a listening study bound the result.

## 121. TS-URGENet: A Three-stage Universal Robust and Generalizable Speech Enhancement Network

**Paper:** [TS-URGENet: A Three-stage Universal Robust and Generalizable Speech Enhancement Network](https://www.isca-archive.org/interspeech_2025/rong25_interspeech.html)
**Taxonomy:** `listening-and-separation / echo-reconstruction / packet-loss-concealment`
**Evidence:** D3 full-paper capture; PDF SHA-256 `7bf691074f1cebd8350f4e97d43912eb42e9cc7821e20d4eda2b7454bd7c8161`; full-text SHA-256 `b099afae9b090201731014ddec10b6cf9103da628bf82a243c7745331605d9c3`.

- **Ordinary problem:** Packet loss removes evidence rather than merely adding noise; a universal enhancer must reconstruct missing regions and then handle other distortions.
- **Why it is hard:** Lost segments interact with noise, reverberation, clipping, bandwidth limits, codec damage, and residual loss.
- **Naive attempt:** Use one denoiser and assume missing samples behave like ordinary noise.
- **Central move:** Use a three-stage pipeline: filling, separation, and restoration.
- **Mechanism:** The filling stage predicts lost regions, separation suppresses noise/reverb/clipping, and restoration repairs bandwidth, codec, and remaining loss.
- **Mathematical idea:** Stage-wise spectral or waveform reconstruction is evaluated in the URGENT challenge setting.
- **What the paper reports:** The system ranked second in URGENT Track 1.
- **Limits:** Challenge conditions, author-reported ranking, and no independent run limit the claim.

## 122. Room Impulse Response as a Prompt for Acoustic Echo Cancellation

**Paper:** [Room Impulse Response as a Prompt for Acoustic Echo Cancellation](https://www.isca-archive.org/interspeech_2025/zhao25b_interspeech.html)
**Taxonomy:** `listening-and-separation / echo-reconstruction / acoustic-echo-cancellation`
**Evidence:** D3 full-paper capture; PDF SHA-256 `facff4f7fe6dc4d1ec26cd48ca70151cb06336430c3832074dbb344c66fb74ed`; full-text SHA-256 `c4c11379c1793dd3e0a5485216c4c568dd9d1207d25c3b5efbbbd67e506017d3`.

- **Ordinary problem:** Echo cancellation must work when the room's echo path differs from anything seen during training.
- **Why it is hard:** The echo path is hidden, changes with geometry, and can be noisy when measured; double talk makes suppression without near-end damage harder.
- **Naive attempt:** Train on synthetic mixtures and assume the learned filter generalizes to every room.
- **Central move:** Give the model a room impulse response as a prompt so it can condition cancellation on acoustic structure at test time.
- **Mechanism:** ICCRN receives several RIR-prompt fusion variants; tests cover matched and mismatched synthetic RIRs plus recorded real RIRs in double-talk and far-end single-talk conditions.
- **Mathematical idea:** ERLE measures echo suppression, PESQ near-end quality, SDR near-end fidelity, and MACs/parameters expose the prompt cost.
- **What the paper reports:** Fusion method (d) is strongest on mismatched and real-RIR ICCRN tests; the reported real-RIR double-talk values are PESQ 2.19 and ERLE 4.79.
- **Limits:** The selected model, fusion choices, RIRs, and author-reported tables bound the claim; independent reproduction and broad room coverage remain absent.

## 123. A Three-Stage Beamforming with Harmonic Guidance for Multi-Channel Speech Enhancement

**Paper:** [A Three-Stage Beamforming with Harmonic Guidance for Multi-Channel Speech Enhancement](https://www.isca-archive.org/interspeech_2025/alip25_interspeech.html)
**Taxonomy:** `listening-and-separation / noise-enhancement / spectral-mask`
**Evidence:** D3 full-paper capture; PDF SHA-256 `ec994a3b983b6cc72158e4653ae409ec1c4a89bd2c8e37fd761e54d6b16d83d1`; full-text SHA-256 `ce9352b0fd7521cc702b5beb582f4e39cbc47f012a32658048945811312dbfc2`.

- **Ordinary problem:** Enhance multi-channel speech in low-SNR conditions by learning both spatial and spectral structure.
- **Why it is hard:** Traditional staged systems can separate spatial filtering from speech spectral structure, losing interactions that matter when noise is strong.
- **Naive attempt:** Estimate masks and beamforming weights in separate stages without explicitly modeling speech structure.
- **Central move:** Use a three-stage framework: acoustic structure extraction, coarse full-band noise reduction, and spectral refinement.
- **Mechanism:** Noisy multi-channel inputs produce speech-structure features that interact with spatial cues before later refinement stages.
- **Mathematical idea:** Beamforming combines channels using spatial information; spectral refinement operates over frequency patterns. The design targets the joint spatial-spectral tradeoff.
- **What the paper reports:** The paper reports improvements over a reference method on LibriSpeech-based datasets.
- **Limits:** The evidence is benchmark-bound and the summary does not establish performance in arbitrary rooms, languages, or devices.

## 124. Structured Codebook Based Hierarchical Framework for DNN for Computationally Efficient Speech Enhancement

**Paper:** [Structured Codebook Based Hierarchical Framework for DNN for Computationally Efficient Speech Enhancement](https://www.isca-archive.org/interspeech_2025/b25_interspeech.html)
**Taxonomy:** `listening-and-separation / noise-enhancement / speech-prior-denoising`
**Evidence:** D3 full-paper capture; PDF SHA-256 `c40c1d0b52707b0e81a55bf0e0e47f35f1cc74c4890e8959f67ff33a27e0d338`; full-text SHA-256 `c466c2419d78eb1c3b2c6c5fa5ee8f81581b3b607ba5ae2dc67a0f9f1e79c49f`.

- **Ordinary problem:** Speech enhancement should run on a device that cannot afford a large neural network.
- **Why it is hard:** Small models lose detail while large models exceed latency and memory limits.
- **Naive attempt:** Compress one large network until it runs fast, even if its structure becomes opaque.
- **Central move:** Replace one expensive DNN with simpler hierarchical predictors backed by structured speech-parameter codebooks.
- **Mechanism:** Hierarchically clustered log-power-spectrum vectors drive codebook stages and enhancement predictors evaluated on VoiceBank-DEMAND.
- **Mathematical idea:** The paper compares SSNR and computational cost; codebook classifiers use cross-entropy and the table reports parameter/runtime burden.
- **What the paper reports:** The framework reduces computation while retaining comparable or improved enhancement scores over the reference systems.
- **Limits:** One corpus and parameterized spectral targets bound the evidence; downstream ASR and perceptual benefit are not fully established.

## 125. Test-Time Training for Speech Enhancement

**Paper:** [Test-Time Training for Speech Enhancement](https://www.isca-archive.org/interspeech_2025/behera25_interspeech.html)
**Taxonomy:** `listening-and-separation / noise-enhancement / speech-prior-denoising`
**Evidence:** D3 full-paper capture; PDF SHA-256 `14cefc1a98fba14832deebdd27641461e572c1ab20ca128b54656a17486dc250`; full-text SHA-256 `03dcdd08394b074168ffec99ca346d41b6c360fafff1f047405a03a41ec18f15`.

- **Ordinary problem:** An enhancement model should adapt when the noise at test time differs from training, even without labeled examples from the new environment.
- **Why it is hard:** Noise and recording domains shift at deployment, while collecting clean/noisy pairs for every new domain is expensive.
- **Naive attempt:** Freeze the enhancement model and hope training-domain noise statistics transfer.
- **Central move:** Use a Y-shaped enhancement model with self-supervised reconstruction or masked-spectrogram tasks during test-time adaptation.
- **Mechanism:** The main enhancement task shares representations with an auxiliary task optimized on the current noisy signal, with strategies trading adaptation gain against test-time cost.
- **Mathematical idea:** The method treats deployment as a second learning stage: the signal supplies an unsupervised clue about the new domain while the enhancement objective remains the output target.
- **What the paper reports:** The paper reports consistent speech-quality improvements over its baseline on synthetic and real-world datasets.
- **Limits:** The adaptation steps, compute budget, noise conditions, and author-reported metrics bound the result; listener benefit and long-term stability remain open.

## 126. QUADS: Quantized Distillation Framework for Efficient Speech Language Understanding

**Paper:** [QUADS: Quantized Distillation Framework for Efficient Speech Language Understanding](https://www.isca-archive.org/interspeech_2025/biswas25b_interspeech.html)
**Taxonomy:** `listening-and-separation / noise-enhancement / speech-prior-denoising`
**Evidence:** D3 full-paper capture; PDF SHA-256 `a400df07f4284c07ba0f362cbe5f72c29be15e8b7ed4f0f383082ce6f02198d3`; full-text SHA-256 `384c7e924e31a9c0aeb742746628695a6f6ee31f5b0b14f626c8fb378024d02c`.

- **Ordinary problem:** Spoken-language understanding must fit a constrained device without losing intent and slot decisions.
- **Why it is hard:** Distillation can preserve a teacher's behavior that later quantization cannot represent.
- **Naive attempt:** Compress by distillation and quantize afterward as unrelated steps.
- **Central move:** Train the student with distillation and quantization constraints together through multiple stages.
- **Mechanism:** QUADS jointly optimizes a pretrained SLU model for low-bit regimes and evaluates it on SLURP and FSC.
- **Mathematical idea:** Accuracy measures task retention, while GMACs and model size measure compute and storage cost.
- **What the paper reports:** The paper reports 71.13% SLURP and 99.20% FSC accuracy, 60–73x lower GMACs, and 83–700x smaller models with bounded degradation.
- **Limits:** The result depends on tasks, bit settings, and hardware interpretation of the counts; latency and energy on deployed devices remain open.

## 127. Scaling and Enhancing LLM-based AVSR:  A Sparse Mixture of Projectors Approach

**Paper:** [Scaling and Enhancing LLM-based AVSR:  A Sparse Mixture of Projectors Approach](https://www.isca-archive.org/interspeech_2025/cappellazzo25_interspeech.html)
**Taxonomy:** `listening-and-separation / noise-enhancement / speech-prior-denoising`
**Evidence:** D3 full-paper capture; PDF SHA-256 `89bca7181a867c1e2ea1c260d64bc0557225357dd5ba7719bb8cc62f90de373b`; full-text SHA-256 `91079ebc52a5cc23edd0c24ddae3fb536f254b60cf625d3b4e9243ae5a27d629`.

- **Ordinary problem:** Audio-visual recognition can use the face when noise damages the sound, but a large multimodal language model may be too expensive for a device.
- **Why it is hard:** Adding experts or projectors can increase capacity and memory even when only a small part of the model is useful for each modality.
- **Naive attempt:** Use one dense projector for every modality or deploy a large LLM and accept its inference cost.
- **Central move:** Route audio and visual inputs through sparse modality-specific projectors so capacity grows without activating every expert on every example.
- **Mechanism:** Llama-SMoP uses sparsely gated mixtures of projectors with modality-specific routers and experts and is evaluated on ASR, visual speech recognition, and AVSR under noise.
- **Mathematical idea:** Conditional computation separates representational capacity from per-example computation; ASR/VSR/AVSR performance, activation patterns, and noise robustness test the tradeoff.
- **What the paper reports:** The DEDR configuration reports the strongest results among the tested variants, with ablations supporting expert activation, scalability, and noise robustness.
- **Limits:** Model size, routing policy, datasets, noise, and compute accounting bound the claim; sparse projector success does not automatically transfer to every multimodal LLM.

## 128. Towards Bitrate-Efficient and Noise-Robust Speech Coding with Variable Bitrate RVQ

**Paper:** [Towards Bitrate-Efficient and Noise-Robust Speech Coding with Variable Bitrate RVQ](https://www.isca-archive.org/interspeech_2025/chae25b_interspeech.html)
**Taxonomy:** `listening-and-separation / noise-enhancement / nonstationary-noise`
**Evidence:** D3 full-paper capture; PDF SHA-256 `b95134638794c59bce084a366549d14e0fea7ba45cc616f9081da9b59b9b8ff2`; full-text SHA-256 `54a8ba4334b16f27cce309cfd083204316cee94f551a71dbdf95f72dd8c720a1`.

- **Ordinary problem:** A speech codec should spend bits on speech detail that matters to listeners, not on background noise, especially when the transmission budget changes from moment to moment.
- **Why it is hard:** Noise can consume code capacity while speech components vary in importance; removing noise and preserving speech quality are coupled rate-allocation decisions.
- **Naive attempt:** Use one constant bitrate for every frame or denoise after compression without changing the allocation.
- **Central move:** Use variable-bitrate residual vector quantization to allocate more representation to important speech frames and combine it with a feature denoiser.
- **Mechanism:** The paper proposes Variable Bitrate RVQ for noise-robust speech coding.
- **Mathematical idea:** Compression is selective reconstruction: the codec decides which parts of a noisy frame deserve precision, so rate, distortion, denoising, and perceptual quality must be evaluated together.
- **What the paper reports:** The paper reports improved rate-distortion trade-offs and perceptual quality over constant-bitrate baselines in noisy conditions.
- **Limits:** Noise conditions, bitrates, codec architecture, datasets, perceptual measures, and model sizes bound the result; a cleaner perceptual signal is not necessarily a faithful waveform.

## 129. DiffDSR: Dysarthric Speech Reconstruction Using Latent Diffusion Model

**Paper:** [DiffDSR: Dysarthric Speech Reconstruction Using Latent Diffusion Model](https://www.isca-archive.org/interspeech_2025/chen25m_interspeech.html)
**Taxonomy:** `listening-and-separation / noise-enhancement / speech-prior-denoising`
**Evidence:** D3 full-paper capture; PDF SHA-256 `e016be381b2a8968b994a4c4f117b2917420ebac669567a7035d29ad1fb6e2f6`; full-text SHA-256 `2d3ec6439dafcd488e8477c0c65a29d0d19105f1373feb455aeaaa510a83f90c`.

- **Ordinary problem:** Reconstruct dysarthric speech so it becomes more intelligible while retaining the original speaker identity.
- **Why it is hard:** Dysarthria damages content cues and voice characteristics together; improving intelligibility can erase identity or hallucinate phonemes.
- **Naive attempt:** Enhance the waveform generically or optimize intelligibility while ignoring speaker identity.
- **Central move:** Restore phoneme embeddings with a pretrained speech encoder, preserve speaker information through an identity encoder, and generate speech with latent diffusion.
- **Mechanism:** Separate content and identity conditioning feed a diffusion generator that samples a reconstructed waveform in latent space.
- **Mathematical idea:** The system imposes two invariants on generation: linguistic content must be restored while speaker identity remains in the conditioning path.
- **What the paper reports:** The paper reports improved intelligibility and speaker similarity in its dysarthric speech reconstruction evaluation.
- **Limits:** Speaker, severity, reference data, perceptual metrics, and diffusion sampling bound transfer; reconstructed speech is not clinical treatment evidence.

## 130. Adaptive Knowledge Distillation for Device-Directed Speech Detection

**Paper:** [Adaptive Knowledge Distillation for Device-Directed Speech Detection](https://www.isca-archive.org/interspeech_2025/chi25b_interspeech.html)
**Taxonomy:** `listening-and-separation / noise-enhancement / nonstationary-noise`
**Evidence:** D3 full-paper capture; PDF SHA-256 `e6a9df8f1888df042ebd63db16cacd62630b0003bfcef0b7eb3e723eca483f04`; full-text SHA-256 `eb295872d39fc8b0f85da8330f295d2ce4d8c1044f06c9f58b5ebaf0ed922945`.

- **Ordinary problem:** A voice assistant must tell when someone is addressing it instead of reacting to nearby conversation or background speech.
- **Why it is hard:** The detector must work with keyword and follow-up requests, run efficiently, and use a representation that transfers from broad speech recognition without confusing ordinary speech for a command.
- **Naive attempt:** Run a large acoustic model directly on every device or detect only a fixed wake word.
- **Central move:** Use adaptive knowledge distillation from a frozen ASR acoustic encoder, with task-specific adapters jointly trained with a smaller device-directed-speech student.
- **Mechanism:** The paper proposes adaptive knowledge distillation for device-directed speech detection.
- **Mathematical idea:** The assistant’s first decision is social and acoustic: before understanding words, it must infer whether the words are meant for it; general speech knowledge helps, but the invocation boundary needs task-specific evidence.
- **What the paper reports:** The paper reports EER improvements of 26% for keyword and 19% for keyword-free follow-up invocations, with gains across transformer and conformer students.
- **Limits:** Invocation types, EER, teacher/student architectures, training data, and device conditions bound deployment claims; a benchmark detector cannot infer intent perfectly in every home.

## 131. First Analyze Then Enhance: A Task-Aware System for Speech Separation, Denoising, and Dereverberation

**Paper:** [First Analyze Then Enhance: A Task-Aware System for Speech Separation, Denoising, and Dereverberation](https://www.isca-archive.org/interspeech_2025/dang25_interspeech.html)
**Taxonomy:** `listening-and-separation / noise-enhancement / nonstationary-noise`
**Evidence:** D3 full-paper capture; PDF SHA-256 `ae4baeb356fabf28a030ed529860f03f68e01222f201c8ecc4b9155d320d2e21`; full-text SHA-256 `9eb32d7d2148cc6b1bc4d3c8edc9ef250b3def6ac08b8314c59e64fec62a9e1e`.

- **Ordinary problem:** A microphone may contain clean speech, noise, echo, or several speakers at once; running every expensive repair stage on every signal wastes computation and can damage already-clean speech.
- **Why it is hard:** The same observed waveform can require different operations, and separation, denoising, and dereverberation can interfere when cascaded in the wrong order.
- **Naive attempt:** Send every input through one universal enhancement network or a fixed sequence of all enhancement modules.
- **Central move:** Analyze the degradation first, route the signal only through the needed modules, and train the modules separately before integrating them.
- **Mechanism:** A lightweight analyzer uses frozen Whisper/WavLM features, LSTMs, pooling, and a classifier to choose among clean, mixture, noisy/reverberant, and combined conditions. A separator with an attractor estimates an unknown speaker count; a refiner handles noise and reverberation. NAT pretrains separation under noise and DIT trains separator/refiner paths before joint fine-tuning.
- **Mathematical idea:** The analyzer uses four-class cross-entropy. Refinement uses negative SI-SNR; separation uses permutation-invariant SI-SNR so source order does not matter; the attractor uses binary cross-entropy with a stop symbol.
- **What the paper reports:** On Libri-3Mix-derived data covering eleven clean, noisy, reverberant, mixed, and combined conditions, FATE reports comparable enhancement quality while reducing unnecessary processing and avoiding overprocessing clean inputs.
- **Limits:** The degradations are simulated and drawn from specified mixtures, noises, and rooms; real rooms, analyzer errors, and out-of-distribution combinations are not established. The reported score is author-reported and was not independently reproduced.

## 132. Improved Intelligibility of Dysarthric Speech using Conditional Flow Matching

**Paper:** [Improved Intelligibility of Dysarthric Speech using Conditional Flow Matching](https://www.isca-archive.org/interspeech_2025/das25b_interspeech.html)
**Taxonomy:** `listening-and-separation / noise-enhancement / speech-prior-denoising`
**Evidence:** D3 full-paper capture; PDF SHA-256 `7f931e5b2b688255edc162db541c8dc623343c9f9959fdaa86a658a4257f76d6`; full-text SHA-256 `e63164461cd02694d7abbc76c695ac7a9382780e2526a572c2feb6624ee4f050`.

- **Ordinary problem:** A person with dysarthria may know what they want to say but be hard to understand; conversion should improve intelligibility without erasing useful content or identity.
- **Why it is hard:** Dysarthric speech varies by speaker and severity, and mel-spectrogram targets may make generation slow or blur the relevant units.
- **Naive attempt:** Map dysarthric mel features to clean speech with an autoregressive or speaker-specific generator.
- **Central move:** Use discrete self-supervised acoustic units and conditional flow matching with a non-autoregressive Diffusion Transformer to map impaired to clearer speech.
- **Mechanism:** The study compares mel-spectrogram and quantized SSL features, controls the output voice with WavLM-derived information, and evaluates generated speech for dysarthric intelligibility.
- **Mathematical idea:** The learned flow maps a conditioning representation to clean-speech acoustics; intelligibility and convergence compare feature choices and generation paths.
- **What the paper reports:** The paper reports that discrete acoustic units improve intelligibility and converge faster than the mel-spectrogram alternative.
- **Limits:** The result is bounded to the speakers, severity range, target voice, and tested listening/evaluation protocol; naturalness, identity preservation, and clinical benefit remain open.

## 133. Objective and Subjective Evaluation of Diffusion-Based Speech  Enhancement for Dysarthric Speech

**Paper:** [Objective and Subjective Evaluation of Diffusion-Based Speech  Enhancement for Dysarthric Speech](https://www.isca-archive.org/interspeech_2025/degroot25_interspeech.html)
**Taxonomy:** `listening-and-separation / noise-enhancement / speech-prior-denoising`
**Evidence:** D3 full-paper capture; PDF SHA-256 `9680c57abb0bd1c826d515ec20a9cf25e2940927c4d7c59732427dfbfba95a78`; full-text SHA-256 `d5df893ec96d680c83e7fde56701aa8f59f8f4ac79f8eb87ebe4588769a5169d`.

- **Ordinary problem:** Enhancement should make dysarthric speech easier to understand or recognize without changing the speaker into an artificial typical voice.
- **Why it is hard:** Dysarthric speech varies greatly and enhancement can improve a recognizer while damaging intelligibility or perceived quality.
- **Naive attempt:** Optimize a generic noise-reduction score and assume lower noise means better recognition.
- **Central move:** Compare two diffusion enhancers with a signal-processing baseline on typical and dysarthric speech, then measure ASR, objective quality, and listener judgments.
- **Mechanism:** The systems enhance two English dysarthric corpora; Whisper-Turbo is evaluated before and after enhancement and fine-tuning.
- **Mathematical idea:** The paper treats intelligibility, speech quality, and recognition as separate targets, exposing disagreement between them.
- **What the paper reports:** The study reports a systematic comparison rather than a single score; gains and tradeoffs depend on corpus, enhancer, and evaluation target.
- **Limits:** The corpora, listener tests, Whisper model, and enhancement settings bound the result; a recognition gain is not automatically a clinical benefit.

## 134. Multitalker Babble in English Vowel Perception Training: A Comparison between Humans and Neural Models

**Paper:** [Multitalker Babble in English Vowel Perception Training: A Comparison between Humans and Neural Models](https://www.isca-archive.org/interspeech_2025/dong25_interspeech.html)
**Taxonomy:** `listening-and-separation / noise-enhancement / speech-prior-denoising`
**Evidence:** D3 full-paper capture; PDF SHA-256 `482ed8fc09476a23a711ec5828b2dc4408231182fc17dc6a1c60d9528de3b747`; full-text SHA-256 `7094975f2bbb9dfc809443b128b31493455ad883810f20962ddf47d335df338e`.

- **Ordinary problem:** Speech-perception training should expose listeners to realistic multitalker babble with a measurable learning target.
- **Why it is hard:** Babble masks cues differently from stationary noise, so SNR alone may not represent daily listening.
- **Naive attempt:** Train with clean speech or one stationary noise and assume transfer to conversation.
- **Central move:** Compare human vowel-perception training with multitalker babble against neural-model responses.
- **Mechanism:** Babble context is manipulated and perceptual/model error patterns are compared.
- **Mathematical idea:** The relevant object is the speech-prior-denoising evidence described by the paper's mechanism: Babble context is manipulated and perceptual/model error patterns are compared.
- **What the paper reports:** The paper reports a comparison of human and neural-model responses in multitalker babble.
- **Limits:** Listeners, babble construction, vowel contrasts, training duration, and model architecture bound transfer.

## 135. FUSE: Universal Speech Enhancement using Multi‐Stage Fusion of Sparse Compression and Token Generation Models for the URGENT 2025 Challenge

**Paper:** [FUSE: Universal Speech Enhancement using Multi‐Stage Fusion of Sparse Compression and Token Generation Models for the URGENT 2025 Challenge](https://www.isca-archive.org/interspeech_2025/goswami25_interspeech.html)
**Taxonomy:** `listening-and-separation / noise-enhancement / speech-prior-denoising`
**Evidence:** D3 full-paper capture; PDF SHA-256 `4aaa175e2914f3dff046156d64a6d4b3729dd2f2ebd7a4731f4c9c0684e33c20`; full-text SHA-256 `506e28f96bfcfc9f05dec9f3b81ea3324c53515286f87a190f7421c43890625d`.

- **Ordinary problem:** Enhancement must make damaged speech understandable while avoiding invented detail and preserving the speaker's identity.
- **Why it is hard:** Noise, clipping, bandwidth loss, packet loss, and wind damage remove different evidence. A model optimized for sample-level fidelity can leave speech perceptually poor, while a generative model can sound plausible but change the signal.
- **Naive attempt:** Use one signal-reconstruction network and one loss for every distortion, or judge success with only SDR or another single waveform score.
- **Central move:** Use three stages: a discriminative sparse-compression enhancer, a codec-token generator that reconstructs missing detail, and a fusion network that combines their different strengths; shift averaging and network blending stabilize the outputs.
- **Mechanism:** Stage 1 predicts an enhanced waveform with mel and SI-SDR losses. Stage 2 conditions masked codec-token prediction on noisy and Stage-1 features and decodes the predicted tokens. Stage 3 receives the noisy signal and both estimates, then adds speaker, phoneme, and perceptual losses. The data contain 2.5K hours of speech, 550 hours of noise, 60K room responses, seven distortion types, and blind samples with an unseen language.
- **Mathematical idea:** The system combines mel-spectrogram, SI-SDR, speaker cosine, phoneme-feature, and UTMOS losses. In the non-blind test, Stage 1 reaches SDR 12.62 and Stage 2 raises UTMOS to 2.38 but lowers SDR to 9.03; the fusion stage reaches UTMOS 2.64 and SDR 12.53 before shift averaging.
- **What the paper reports:** On the blind challenge set, the system reports DNSMOS 2.94, NISQA 3.25, UTMOS 2.19, MOS 3.44, and CER 77.09; it ranks behind the top system on several signal-level measures but leads the listed systems on perceptual measures.
- **Limits:** The challenge mixtures, five training languages, unseen Japanese test condition, and 900-sample blind set define the evidence. The sequential three-stage inference and shift operations restrict real-time use; all results are author-reported and no independent reproduction was performed.

## 136. Diffusion Buffer: Online Diffusion-based Speech Enhancement with Sub-Second Latency

**Paper:** [Diffusion Buffer: Online Diffusion-based Speech Enhancement with Sub-Second Latency](https://www.isca-archive.org/interspeech_2025/lay25_interspeech.html)
**Taxonomy:** `listening-and-separation / noise-enhancement / nonstationary-noise`
**Evidence:** D3 full-paper capture; PDF SHA-256 `a824112d710784820ae0c7e5496d022f713793c1fd3a9219735b68d7cec43923`; full-text SHA-256 `541726693fd8c8040e517881f715c6c29a8e542df119d678e32ad70947783e15`.

- **Ordinary problem:** Live communication needs speech enhancement while the signal is still arriving, with latency small enough for interaction.
- **Why it is hard:** Diffusion models can restore complex distributions but normally require many iterative steps and future context, conflicting with streaming constraints.
- **Naive attempt:** Run an offline diffusion enhancer or use a fast deterministic model that sacrifices generative restoration quality.
- **Central move:** Use a sliding buffer whose corruption schedule gives more noise to frames near the present, then denoise older frames with a controlled delay.
- **Mechanism:** The buffer defines a causal-to-delayed window; diffusion steps operate on that window and output frames once their future context is sufficient.
- **Mathematical idea:** Latency becomes a tunable information budget: a larger buffer gives the score-based model more context while increasing input-output delay.
- **What the paper reports:** The paper reports better results than standard diffusion baselines and GPU input-output latency around 0.3–1 seconds.
- **Limits:** GPU/hardware assumptions, buffer size, noise mixtures, real-time scheduling, and perceptual metrics bound the result; a reported latency range is not a full conversational user study.

## 137. Multistage Universal Speech Enhancement System for URGENT Challenge

**Paper:** [Multistage Universal Speech Enhancement System for URGENT Challenge](https://www.isca-archive.org/interspeech_2025/le25b_interspeech.html)
**Taxonomy:** `listening-and-separation / noise-enhancement / speech-prior-denoising`
**Evidence:** D3 full-paper capture; PDF SHA-256 `a49cb0523d436a8def388ed3813c3900416f2b651e3da7b7f7c63ba3e7ab27f7`; full-text SHA-256 `e1847002bdae354c29901dba3809fdce5b20a9539ed1eaf80dd9c3a54a63cdfa`.

- **Ordinary problem:** A transmitted or recorded speech signal can contain clipped samples, missing packets, noise, reverberation, bandwidth loss, and codec artifacts at once.
- **Why it is hard:** Each distortion removes or corrupts different evidence, and a single undifferentiated enhancer can repair one defect while amplifying another.
- **Naive attempt:** Apply one generic enhancement network to the waveform and hope it learns every corruption jointly.
- **Central move:** Cascade specialized modules in a deliberate order: declipping, separation, packet-loss compensation, and spectral inpainting, with a detector deciding when the first and third modules are needed.
- **Mechanism:** Model the degraded signal as a composition of distortion operators; use Demucs for declipping, BSRoformer for separation, BS-PLCNet in a PQMF subband domain for packet loss, and a time-frequency recurrent inpainting network for spectral artifacts.
- **Mathematical idea:** The key object is a masked signal and a composition of operators. Separating domains and ordering repairs reduces the optimization problem from one tangled inverse map to several bounded inverse problems.
- **What the paper reports:** The system reports URGENT challenge results competitive with the compared systems; adding inpainting and self-distillation improves several quality measures, while downstream accuracy and objective metrics do not all move together.
- **Limits:** Challenge datasets, distortion order, detector errors, resampling to 48 kHz for some modules, metric choice, and author-reported rankings bound the claim; plausible filling is not recovery of the original samples.

## 138. Model as Loss: A Self-Consistent Training Paradigm

**Paper:** [Model as Loss: A Self-Consistent Training Paradigm](https://www.isca-archive.org/interspeech_2025/phaye25_interspeech.html)
**Taxonomy:** `listening-and-separation / noise-enhancement / speech-prior-denoising`
**Evidence:** D3 full-paper capture; PDF SHA-256 `94e0c05843fc69c8bf34e867731e6e28b3fd951877ab6636d7a79b8eeba48fa5`; full-text SHA-256 `b6451adf9d31464d09c5e51c7cfaf5eada6b2804467a6902d3ca04140668eb84`.

- **Ordinary problem:** An enhancement system should remove noise while keeping the speech properties that matter to perception and downstream tasks.
- **Why it is hard:** A waveform or spectrum loss treats all deviations similarly, while a generic feature loss may preserve features unrelated to the target task.
- **Naive attempt:** Choose a fixed time-domain or frequency-domain distance and assume its error corresponds to what listeners need.
- **Central move:** Use the same model's encoder as a task-specific loss, forcing enhanced output and clean reference to agree in the model's learned feature space.
- **Mechanism:** A speech-enhancement decoder is trained against features from its own encoder and compared with handcrafted and pretrained deep-feature losses on standard benchmarks.
- **Mathematical idea:** The loss measures consistency in a learned representation rather than raw sample distance; perceptual metrics and out-of-domain tests expose whether that representation transfers.
- **What the paper reports:** The paper reports better perceptual quality than pretrained feature losses and robust generalization in both in-domain and out-of-domain tests.
- **Limits:** The encoder, training data, noise conditions, perceptual metrics, and benchmark protocols bound the result; feature agreement is not identical to intelligibility or listener preference.

## 139. FlowSE: Efficient and High-Quality Speech Enhancement via Flow Matching

**Paper:** [FlowSE: Efficient and High-Quality Speech Enhancement via Flow Matching](https://www.isca-archive.org/interspeech_2025/wang25s_interspeech.html)
**Taxonomy:** `listening-and-separation / noise-enhancement / speech-prior-denoising`
**Evidence:** D3 full-paper capture; PDF SHA-256 `0f9edb5f0123db3e1620458d36e6d85ce35c4ba9f3873a243871b4d6b885e8d9`; full-text SHA-256 `a3f1091ca5c57a9891b787a810abcb8470c7435548a84037fd08dae26082bc61`.

- **Ordinary problem:** Enhancement should remove noise while retaining the speaker and intelligibility without making real-time use impractical.
- **Why it is hard:** Noise removal is a conditional distribution problem: aggressive suppression can erase speech detail, while generative samplers can be slow.
- **Naive attempt:** Use a deterministic mask or a many-step diffusion sampler and accept either artifacts or latency.
- **Central move:** Use flow matching to learn a continuous transport from noisy to clean speech and combine it with efficient architecture and multi-resolution objectives.
- **Mechanism:** A neural velocity field maps a noisy waveform toward the clean distribution; consistency of the trajectory permits few-step integration while spectral and waveform losses preserve detail.
- **Mathematical idea:** Flow matching replaces repeated stochastic denoising with an ODE-like path whose learned vector field can be sampled in fewer evaluations.
- **What the paper reports:** The paper reports improved enhancement quality against generative baselines in both its evaluated scenarios with lower inference cost.
- **Limits:** Training data, noise conditions, step count, real-time hardware, perceptual metrics, and speaker preservation tests bound the claim; enhancement scores do not establish conversational benefit.

## 140. A Novel Deep Learning Framework for Efficient Multichannel Acoustic Feedback Control

**Paper:** [A Novel Deep Learning Framework for Efficient Multichannel Acoustic Feedback Control](https://www.isca-archive.org/interspeech_2025/wu25d_interspeech.html)
**Taxonomy:** `listening-and-separation / noise-enhancement / nonstationary-noise`
**Evidence:** D3 full-paper capture; PDF SHA-256 `02587cce87ef16757b6e57ad50308535c94a0b9dd53d8eba70369863644a3b65`; full-text SHA-256 `481c1b9e8490362f15cd22e7a2d093cc1dc92151192b21d7c90e52cf995afb9f`.

- **Ordinary problem:** In a device with microphones and loudspeakers, the device's own output can return through the room and become a howl that damages speech quality.
- **Why it is hard:** Feedback is correlated with the device output, changes as the acoustic path changes, and can defeat methods that assume independent stationary noise.
- **Naive attempt:** Apply a fixed noise suppressor or wait for a conventional adaptive filter to converge.
- **Central move:** Combine spatial and temporal processing in a recurrent controller and train it in the feedback loop, with teacher forcing and a Wiener-filter hybrid as alternatives.
- **Mechanism:** A convolutional recurrent network controls multichannel acoustic feedback; in-loop, teacher-forced, and hybrid training are compared in complex acoustic environments.
- **Mathematical idea:** The task is closed-loop control: the output changes the next input, so stability and enhancement must be evaluated together rather than on isolated noisy clips.
- **What the paper reports:** The paper reports improved speech enhancement with lower computational demand across the proposed training strategies.
- **Limits:** The device geometry, microphones, loudspeakers, feedback paths, training regime, and metrics bound the result; laboratory suppression does not establish stable operation for every room or device.

## 141. MiSTR: Multi-Modal iEEG-to-Speech Synthesis with Transformer-Based Prosody Prediction and Neural Phase Reconstruction

**Paper:** [MiSTR: Multi-Modal iEEG-to-Speech Synthesis with Transformer-Based Prosody Prediction and Neural Phase Reconstruction](https://www.isca-archive.org/interspeech_2025/alradhi25_interspeech.html)
**Taxonomy:** `listening-and-separation / perceptual-recovery / perceptual-enhancement`
**Evidence:** D3 full-paper capture; PDF SHA-256 `3ee13b318b756079bc0d5e0c82e3bf2d800a61e5035c9a391a26ff271d7dd263`; full-text SHA-256 `cf4f5e0f7e85fbbae0f1e1aa5ff557dd01064da0f7196c9d02fe3376b6dec728`.

- **Ordinary problem:** Brain recordings may contain enough motor or auditory information to reconstruct intelligible speech for people who cannot produce it normally.
- **Why it is hard:** Neural signals are indirect, data are limited, and a reconstruction can be spectrally plausible yet unintelligible or unnatural.
- **Naive attempt:** Map neural features directly to a waveform and let a generic vocoder repair phase and prosody.
- **Central move:** Separate linguistic/prosodic prediction from neural phase reconstruction, then use a neural vocoder and a learned MOSA evaluator.
- **Mechanism:** MiSTR uses a multimodal iEEG encoder, Transformer spectrogram/prosody prediction, and a neural phase vocoder with adaptive spectral correction.
- **Mathematical idea:** Mel-spectrogram correlation, intelligibility, naturalness, and MOSA expose different reconstruction failures; MOSA is reported at 3.38.
- **What the paper reports:** The paper reports higher fidelity and naturalness than listed baselines and MOSA 3.38.
- **Limits:** Dataset, subjects, protocol, learned evaluator, and paper-reported comparisons limit clinical claims.

## 142. Voice-ENHANCE: Speech Restoration using a Diffusion-based Voice Conversion Framework

**Paper:** [Voice-ENHANCE: Speech Restoration using a Diffusion-based Voice Conversion Framework](https://www.isca-archive.org/interspeech_2025/byun25_interspeech.html)
**Taxonomy:** `listening-and-separation / perceptual-recovery / perceptual-enhancement`
**Evidence:** D3 full-paper capture; PDF SHA-256 `4137e2b796cd4a2cde970513fa34019d7933861e9897ce249dd7143c86425c29`; full-text SHA-256 `0dac55d9a07a94a5e09b7ec038585532fd82edf7c6f2fd87a8e99d71ddb6d76c`.

- **Ordinary problem:** A damaged recording may be noisy, reverberant, clipped, bandwidth-limited, packet-dropped, or codec-distorted; repairing it requires inventing plausible speech where the waveform contains no evidence.
- **Why it is hard:** A suppressive mask can remove noise but cannot fill missing frequency or time regions, and voice-conversion models can add identity cues while also failing under noise.
- **Naive attempt:** Apply a denoising mask alone, or use voice conversion directly on a noisy waveform and hope its speaker representation remains stable.
- **Central move:** Stage a speaker-agnostic generative restoration model first, then use a clean target-speaker embedding to refine the restored speech through a voice-conversion-style diffusion decoder.
- **Mechanism:** GSR predicts additive corrections to mel features with a ResU-Net and vocoder, covering noise, reverberation, bandwidth extension, clipping, packet loss, and codec artifacts. The second stage extracts HuBERT discrete content and an ECAPA speaker embedding, predicts a coarse spectrogram, and uses a diffusion U-Net conditioned on content and identity to generate the final waveform.
- **Mathematical idea:** GSR uses GAN, feature-matching, and mel losses; the VC stage combines L1 coarse-spectrogram loss with diffusion noise-prediction loss. NISQA, UTMOS, WV-MOS, and DNSMOS estimate non-intrusive quality on VCTK-DEMAND and UNIVERSE validation sets.
- **What the paper reports:** The paper reports that GSR+VC obtains strong objective quality scores across simulated noise, packet loss, bandwidth, reverberation, and codec conditions and compares favorably with the cited restoration systems.
- **Limits:** Training uses a proprietary restoration corpus and evaluation uses small/simulated validation settings; non-intrusive quality proxies do not establish word correctness or speaker-faithful repair. No independent reproduction was performed.

## 143. A Deformable Convolution GAN Approach for Speech Dereverberation in Cochlear Implant Users

**Paper:** [A Deformable Convolution GAN Approach for Speech Dereverberation in Cochlear Implant Users](https://www.isca-archive.org/interspeech_2025/chiang25_interspeech.html)
**Taxonomy:** `listening-and-separation / perceptual-recovery / perceptual-enhancement`
**Evidence:** D3 full-paper capture; PDF SHA-256 `117a8270ea47e2052ea787a81d2b066eb3d38749963c09894a2fc58579ac21c5`; full-text SHA-256 `3428b191c9288b9bfdfba67ea90fa9defa6e3704f8ce134a438757dec099ac67`.

- **Ordinary problem:** Reverberation smears speech, and cochlear-implant users are especially affected; a useful enhancer must restore intelligibility, not just make the waveform look cleaner.
- **Why it is hard:** Transient speech cues can be blurred by room reflections and by the implant's representation of sound.
- **Naive attempt:** Use a fixed convolutional receptive field or optimize only for normal-hearing listeners.
- **Central move:** Let deformable convolution move its receptive field to the distortion, and evaluate both signal measures and listeners with cochlear implants.
- **Mechanism:** A deformable-convolution GAN is trained for dereverberation, first tested on REVERB and then assessed in listening tests with normal-hearing and CI users.
- **Mathematical idea:** The learned offsets change which neighboring time-frequency evidence is combined; intelligibility and quality are judged by objective tests and listener responses.
- **What the paper reports:** The paper reports markedly improved CI speech intelligibility by preserving envelope and transient structure.
- **Limits:** The claim is bounded to REVERB conditions, the tested listeners, and the GAN configuration; broader hearing profiles, rooms, and independent replication remain open.

## 144. Modality-Agnostic Multimodal Emotion Recognition using a Contrastive Masked Autoencoder

**Paper:** [Modality-Agnostic Multimodal Emotion Recognition using a Contrastive Masked Autoencoder](https://www.isca-archive.org/interspeech_2025/chochlakis25_interspeech.html)
**Taxonomy:** `listening-and-separation / perceptual-recovery / perceptual-enhancement`
**Evidence:** D3 full-paper capture; PDF SHA-256 `0fd014ca8ee889c503cf4d3fc3171f05001ac465e09b261005c8f5d82491a013`; full-text SHA-256 `bf125bcc5c1804fa784220d547398aea86671fac749d5dee8e496ca03d21265d`.

- **Ordinary problem:** Emotion recognition should continue working when a camera, transcript, or other modality is missing rather than failing because the training setup expected every input.
- **Why it is hard:** Modalities are correlated but not interchangeable; reconstruction can fill a missing channel while also inventing information that was never observed.
- **Naive attempt:** Train separate models for every modality combination or drop examples with missing inputs.
- **Central move:** Align modalities contrastively and use masked reconstruction in one modality-agnostic model, then test unimodal, multimodal, and missing-modality cases.
- **Mechanism:** The paper proposes a contrastive masked-autoencoder model for modality-agnostic multimodal emotion recognition on MSP-Podcast.
- **Mathematical idea:** The model learns shared structure while treating missingness as a normal observation condition; reconstruction supplies a bridge, but prediction must still be judged against the available evidence.
- **What the paper reports:** The paper reports improvements over unimodal and multimodal baselines and robustness to missing modalities.
- **Limits:** Corpus, emotion labels, missingness pattern, modality quality, and reconstruction objective bound the claim; emotion inference is not guaranteed to be socially reliable.

## 145. Listen through the Sound: Generative Speech Restoration Leveraging Acoustic Context Representation

**Paper:** [Listen through the Sound: Generative Speech Restoration Leveraging Acoustic Context Representation](https://www.isca-archive.org/interspeech_2025/chung25_interspeech.html)
**Taxonomy:** `listening-and-separation / perceptual-recovery / perceptual-enhancement`
**Evidence:** D3 full-paper capture; PDF SHA-256 `d8adca081f35bca40cff9dc160e77c0ab5d808d8cfc49dd72bd0fe9ba29edf8c`; full-text SHA-256 `6b57f14b9104ca734ca1564c5929b93cc906d3ed045f52d891de256bdab46f52`.

- **Ordinary problem:** Speech restoration should use clues about the recording environment to undo distortion without mistaking the environment for speech content.
- **Why it is hard:** The same linguistic content can be damaged differently by noise, reverberation, or other conditions.
- **Naive attempt:** Condition a generator only on linguistic or speaker representations.
- **Central move:** Add an acoustic-context representation that describes the distortion and its intensity, then condition the restoration model on it.
- **Mechanism:** ACX refines CLAP-derived environmental embeddings and conditions the diffusion restoration model UNIVERSE++ across distortion conditions.
- **Mathematical idea:** Restoration quality and stability across conditions compare context-aware and content-based conditioning; variability itself is an evaluation target.
- **What the paper reports:** The paper reports better restoration and reduced performance variability with acoustic context.
- **Limits:** The result is tied to the distortion set, CLAP features, and diffusion backbone; unseen devices, rooms, and perceptual listeners remain open.

## 146. Linguistic Masking and Its Release in Simulated Electric-acoustic Hearing

**Paper:** [Linguistic Masking and Its Release in Simulated Electric-acoustic Hearing](https://www.isca-archive.org/interspeech_2025/ding25_interspeech.html)
**Taxonomy:** `listening-and-separation / perceptual-recovery / perceptual-enhancement`
**Evidence:** D3 full-paper capture; PDF SHA-256 `32f51469f9b1b9e7d6dc21539f714e516b7c66795109640a8835b22b58d93089`; full-text SHA-256 `1683483bfd1f2de6bdb258b6d29944a01e03ee52938e9ff30b19bf08e89b132c`.

- **Ordinary problem:** A cochlear-implant listener may understand speech in competing talkers differently when the target and masker use different languages.
- **Why it is hard:** The useful target and competing voices overlap, and the listener's hearing device changes which acoustic cues survive.
- **Naive attempt:** Measure speech in quiet or use one same-language masker and assume the result transfers.
- **Central move:** Compare electric-acoustic stimulation with implant-only simulation under Mandarin, Cantonese, and English two-talker maskers.
- **Mechanism:** Mandarin sentences are mixed with language-controlled babble, processed by noise vocoders simulating CI or EAS hearing, and scored through sentence recognition.
- **Mathematical idea:** Release from masking is the difference in recognition between a target with and without a linguistic advantage; comparing those differences separates hearing mode from masker language.
- **What the paper reports:** The study reports a combined-stimulation advantage across all three masker languages and language-specific differences in release from masking.
- **Limits:** Normal-hearing listeners, vocoder simulations, Mandarin targets, and the selected masker languages limit direct claims about real CI users and everyday rooms.

## 147. Efficient Neural and Numerical Methods for High-QualityOnline Speech Spectrogram Inversion via Gradient Theorem

**Paper:** [Efficient Neural and Numerical Methods for High-QualityOnline Speech Spectrogram Inversion via Gradient Theorem](https://www.isca-archive.org/interspeech_2025/fernandez25_interspeech.html)
**Taxonomy:** `listening-and-separation / perceptual-recovery / perceptual-enhancement`
**Evidence:** D3 full-paper capture; PDF SHA-256 `a767c10d45a8f47617a27f4e14e014c4d8a27f3a2c9bf5d2ae1986e7d83cf083`; full-text SHA-256 `e97e3551ba42c7cb15670ff3760aa2b66b3c874b57d7ff4e814bc1dbf87f49b2`.

- **Ordinary problem:** A streaming system must reconstruct an audio waveform from a magnitude spectrogram without paying a large compute or latency cost.
- **Why it is hard:** Magnitude says how much energy is present but not the phase relationships needed to make the waveform line up in time.
- **Naive attempt:** Use a large neural inverse model or solve the reconstruction problem with a generic expensive least-squares routine.
- **Central move:** Predict phase derivatives with a tiny network and exploit the tridiagonal positive-semidefinite structure of the resulting least-squares system.
- **Mechanism:** The online inversion model uses 8k parameters, adds at most one hop of latency, and applies a linear-complexity solver after predicting derivative information.
- **Mathematical idea:** Phase reconstruction becomes a structured inverse problem; the solver uses matrix structure instead of treating every coefficient as unrelated.
- **What the paper reports:** The paper reports a 30x smaller network, a further halving of neural cost with one-hop latency, and orders-of-magnitude solver speedup while retaining quality.
- **Limits:** Spectrogram settings, audio domain, latency definition, and samples bound the claim; listening tests and hardware deployment remain separate checks.

## 148. Vision-Integrated High-Quality Neural Speech Coding

**Paper:** [Vision-Integrated High-Quality Neural Speech Coding](https://www.isca-archive.org/interspeech_2025/guo25c_interspeech.html)
**Taxonomy:** `listening-and-separation / perceptual-recovery / perceptual-enhancement`
**Evidence:** D3 full-paper capture; PDF SHA-256 `a8b98a3cc3f9952d5a12a6994412e43e2b7d02e71553d8e23ddf2aececc5300d`; full-text SHA-256 `3c6f728ef5c91de69b214cc5f3c78f1a42c2b9ed2698bd179d0714457d51f007`.

- **Ordinary problem:** A neural speech codec should preserve high-quality speech while using visual information when available, and it should fail gracefully when that information is absent.
- **Why it is hard:** Video can disambiguate speech and improve reconstruction, but synchronization, bitrate, and privacy make it a conditional source rather than a free improvement.
- **Naive attempt:** Encode only audio at a high bitrate or concatenate video features without modeling their timing and reliability.
- **Central move:** Integrate visual cues into a high-quality neural speech coder and measure quality, rate, and behavior across audio-visual conditions.
- **Mechanism:** The paper presents a vision-integrated high-quality neural speech coding system.
- **Mathematical idea:** Coding becomes cross-modal reconstruction: the decoder uses synchronized visual evidence to fill or protect acoustic detail while the rate constraint limits what can be transmitted.
- **What the paper reports:** The paper reports high-quality neural coding results for the tested audio-visual conditions.
- **Limits:** Video quality, synchronization, speakers, bitrate, decoder, and missing-video behavior bound the claim; visual assistance can introduce privacy and spoofing risks.

## 149. PAST: Phonetic-Acoustic Speech Tokenizer

**Paper:** [PAST: Phonetic-Acoustic Speech Tokenizer](https://www.isca-archive.org/interspeech_2025/hartuv25_interspeech.html)
**Taxonomy:** `listening-and-separation / perceptual-recovery / perceptual-enhancement`
**Evidence:** D3 full-paper capture; PDF SHA-256 `cab000ab53335789ced2950b728895340a8dc1aaf40ff1ef9f8b1e1bd1dc1f04`; full-text SHA-256 `e09d869c973a4236dc598d0da6246412c58520c82d103623b478a2bd5b0e980c`.

- **Ordinary problem:** A speech tokenizer should turn sound into compact units that preserve the information a downstream speech model actually needs.
- **Why it is hard:** Acoustic detail, phonetic identity, speaker identity, and temporal precision compete for a limited token budget; reconstruction quality alone may reward irrelevant detail.
- **Naive attempt:** Use waveform compression or text-like units and assume the best reconstruction tokenizer is the best speech representation.
- **Central move:** Build a phonetic-acoustic tokenizer and evaluate whether its tokens capture both speech sound structure and useful phonetic distinctions.
- **Mechanism:** PAST is a phonetic-acoustic speech tokenizer.
- **Mathematical idea:** Tokenization is a choice about what survives discretization: units should preserve acoustically grounded, phonetic information while discarding redundant waveform variation.
- **What the paper reports:** The paper reports tokenizer quality and downstream speech-representation results for the proposed phonetic-acoustic units.
- **Limits:** Token rate, codebook, languages, speakers, reconstruction target, and downstream tasks bound the claim; discrete units are not automatically linguistically complete.

## 150. VoiceNoNG: Robust High-Quality Speech Editing Model without Hallucinations

**Paper:** [VoiceNoNG: Robust High-Quality Speech Editing Model without Hallucinations](https://www.isca-archive.org/interspeech_2025/huang25c_interspeech.html)
**Taxonomy:** `listening-and-separation / perceptual-recovery / perceptual-enhancement`
**Evidence:** D3 full-paper capture; PDF SHA-256 `4eeb16427268e714fe440e9b49e4e93f97923d44b6ef1d532406f70fab67c7da`; full-text SHA-256 `cd836d597a1fa9f0175a92ef67fef0a462e788ff65854da6c8a13d50bf099cc9`.

- **Ordinary problem:** Editing a speech recording should change the requested words or sounds without inventing unrelated content or damaging the surrounding voice.
- **Why it is hard:** An editor must fill a gap using context, but a powerful generator can hallucinate plausible speech that is inconsistent with the speaker, timing, or meaning.
- **Naive attempt:** Regenerate the whole utterance or mask a span and trust unconstrained continuation.
- **Central move:** Build a robust high-quality speech editor whose context use is constrained and evaluate whether edits remain faithful without hallucinations.
- **Mechanism:** VoiceNoNG is a robust high-quality speech-editing model designed to avoid hallucinations.
- **Mathematical idea:** Editing is constrained completion: the model must change a local region while preserving identity, timing, and untouched context, so faithfulness is a separate target from audio quality.
- **What the paper reports:** The paper reports speech-editing quality and reduced hallucination behavior for the tested edits.
- **Limits:** Edit type, context length, speaker set, alignment, metrics, and human judgments bound the claim; no-hallucination behavior is not guaranteed under arbitrary prompts.

## 151. Benchmarking Neural Speech Codec Intelligibility with SITool

**Paper:** [Benchmarking Neural Speech Codec Intelligibility with SITool](https://www.isca-archive.org/interspeech_2025/leschanowsky25_interspeech.html)
**Taxonomy:** `listening-and-separation / perceptual-recovery / perceptual-enhancement`
**Evidence:** D3 full-paper capture; PDF SHA-256 `fb36fc9e25a7c01630b62c6552a8228eb650ee2fe1ed11383f892f930e09d539`; full-text SHA-256 `ef12a5893381b9a425038eb662fa54f134137e6ce2993d49cc279b9fd38d4282`.

- **Ordinary problem:** A codec can sound pleasant yet make words harder to understand, so intelligibility needs its own evaluation target.
- **Why it is hard:** Quality scores and WER can miss phoneme-specific distortions and listener-dependent effects, especially for generative codecs.
- **Naive attempt:** Use MOS or WER as a universal proxy for whether listeners identify speech sounds.
- **Central move:** Provide a standardized rhyme-test toolkit and compare its subjective results with objective intelligibility measures.
- **Mechanism:** SITool runs Diagnostic and Modified Rhyme Tests in laboratory or crowdsourcing settings; thirteen codecs are evaluated with phoneme, gender, and wordlist analyses.
- **Mathematical idea:** Subjective scores are compared with STOI, ESTOI, and WER; only STOI and ESTOI significantly correlate in the reported analysis.
- **What the paper reports:** Some neural codecs outperform traditional codecs in subjective intelligibility, but objective agreement varies and scores show gender- and wordlist-specific differences.
- **Limits:** The codec set, English tests, listener screening, and objective metrics bound the conclusion; the toolkit does not remove human evaluation.

## 152. SpeechRefiner: Towards Perceptual Quality Refinement for Front-End Algorithms

**Paper:** [SpeechRefiner: Towards Perceptual Quality Refinement for Front-End Algorithms](https://www.isca-archive.org/interspeech_2025/li25s_interspeech.html)
**Taxonomy:** `listening-and-separation / perceptual-recovery / perceptual-enhancement`
**Evidence:** D3 full-paper capture; PDF SHA-256 `8477cbf1fa1fd1f763d76d390021c56761550780900d4ce0a77c8f6884bea674`; full-text SHA-256 `af9fd43dda3224c069124097bd0b3756eaa04a0009de789e7e6ac98d32a4fc8f`.

- **Ordinary problem:** A front-end speech algorithm may improve intelligibility or remove noise but leave artifacts that make the final speech sound unpleasant; a refiner should improve perceived quality without undoing the front-end benefit.
- **Why it is hard:** Perceptual quality is hard to predict from signal metrics, and refinement can hallucinate detail or alter speech content.
- **Naive attempt:** Optimize one waveform metric or apply a generic denoiser after every front-end.
- **Central move:** Use SpeechRefiner to learn perceptual quality refinement for outputs from varied front-end algorithms and evaluate quality and faithfulness.
- **Mechanism:** SpeechRefiner targets perceptual quality refinement for front-end speech algorithms.
- **Mathematical idea:** Refinement is a second-stage correction problem: the input already contains a useful transformation, so the model must remove artifacts while preserving the first stage's content and gains.
- **What the paper reports:** The paper reports perceptual and signal-quality improvements for refined front-end outputs.
- **Limits:** Front-end types, distortion, training targets, listeners, metrics, and content preservation bound the result; quality improvement is not guaranteed for unseen algorithms.

## 153. HWB-Net: A Novel High-Performance and Efficient Hybrid Waveform Bandwidth Extension Method

**Paper:** [HWB-Net: A Novel High-Performance and Efficient Hybrid Waveform Bandwidth Extension Method](https://www.isca-archive.org/interspeech_2025/liu25d_interspeech.html)
**Taxonomy:** `listening-and-separation / perceptual-recovery / perceptual-enhancement`
**Evidence:** D3 full-paper capture; PDF SHA-256 `a40ebc29a71477f91b9f6a946666e24cb3636f16500c89d73bd8fef0339e04c0`; full-text SHA-256 `eb2814866a9ef275ed02aac97276bf962187c067e7d4f41f8bde36df38357f72`.

- **Ordinary problem:** A bandwidth-limited recording can sound muffled; a bandwidth-extension model should restore useful high-frequency detail without inventing harsh or speaker-inconsistent content.
- **Why it is hard:** The missing band is not uniquely determined by the low band, and waveform metrics may reward artifacts that listeners dislike.
- **Naive attempt:** Copy the low-band waveform or add fixed high-frequency noise and assume the result is natural.
- **Central move:** Use a hybrid waveform bandwidth-extension network and evaluate reconstruction quality, speech content, and perceptual naturalness.
- **Mechanism:** HWB-Net is a high-performance efficient hybrid waveform bandwidth-extension method.
- **Mathematical idea:** Bandwidth extension is constrained synthesis: the model predicts plausible missing detail from the observed signal while preserving timing and identity in the known band.
- **What the paper reports:** The paper reports quality and efficiency results for HWB-Net on bandwidth-extension tests.
- **Limits:** Bandwidth limit, speakers, noise, training targets, metrics, and listening protocol bound the result; plausible detail is not recovered ground truth.

## 154. A Neural Codec Approach for Noise-Robust Bandwidth Expansion

**Paper:** [A Neural Codec Approach for Noise-Robust Bandwidth Expansion](https://www.isca-archive.org/interspeech_2025/liu25p_interspeech.html)
**Taxonomy:** `listening-and-separation / perceptual-recovery / perceptual-enhancement`
**Evidence:** D3 full-paper capture; PDF SHA-256 `3ad349fb2196bbc86196cdaf39978ebe6886722e74d2e58ad9212be5afcd4661`; full-text SHA-256 `1f032d473043ba7c9a1e4fce2f28a7b288f6fba66878c6cded603e95e2b11232`.

- **Ordinary problem:** A codec should restore missing high-frequency speech detail even when the input is noisy, without amplifying noise or making the speaker sound artificial.
- **Why it is hard:** The missing band is uncertain and noise can be mistaken for speech detail; a model must separate denoising from bandwidth expansion.
- **Naive attempt:** Copy a clean high band from a fixed template or extend bandwidth without modeling the noise condition.
- **Central move:** Use a neural codec approach that jointly supports noise-robust bandwidth expansion and evaluates speech quality under noisy inputs.
- **Mechanism:** The paper proposes a neural codec approach for noise-robust bandwidth expansion.
- **Mathematical idea:** The codec treats missing frequency content and corruption as coupled inference: it must reconstruct a plausible high band conditioned on what the noisy low band actually supports.
- **What the paper reports:** The paper reports bandwidth-expansion quality and noise robustness for the proposed neural codec.
- **Limits:** Noise types, bandwidth, codec rate, speakers, targets, and perceptual evaluation bound the result; plausible high-frequency detail is not ground truth.

## 155. Analysis and Extension of a Near-End Listening Enhancement Method Based on Long-Term Fractile Noise Statistics

**Paper:** [Analysis and Extension of a Near-End Listening Enhancement Method Based on Long-Term Fractile Noise Statistics](https://www.isca-archive.org/interspeech_2025/villani25_interspeech.html)
**Taxonomy:** `listening-and-separation / perceptual-recovery / perceptual-enhancement`
**Evidence:** D3 full-paper capture; PDF SHA-256 `761672709fb3e769d51b811cef6c83cea9a06a62f2799f3e43a68c36ae941fec`; full-text SHA-256 `dcabcb72cb48821bfc027f63340e9900e44c52799a65cc819708f952a59f3615`.

- **Ordinary problem:** A listener in noise may need speech made clearer after capture, but enhancement should not erase speech or make the result sound unnatural.
- **Why it is hard:** Noise statistics change over time and a useful near-end method has to estimate what belongs to the noise without relying on a clean reference.
- **Naive attempt:** Use one fixed noise estimate or raise all frequencies equally and assume intelligibility will follow.
- **Central move:** Estimate long-term fractile noise statistics and use them to guide near-end listening enhancement, then test the method against speech and noise conditions.
- **Mechanism:** The paper analyzes and extends a near-end listening-enhancement method based on long-term fractile noise statistics.
- **Mathematical idea:** The method treats noise as a distribution over time rather than a single fixed level; enhancement is constrained by the estimated noise floor so speech structure is not indiscriminately removed.
- **What the paper reports:** The paper reports listening-enhancement results for the proposed statistical method and its extension.
- **Limits:** Noise type, recordings, listeners, parameter settings, and perceptual tests limit generalization; improved quality is not identical to improved intelligibility.

## 156. ReSepNet: A Unified-Light Model for Recursive Speech Separation with Unknown Speaker Count

**Paper:** [ReSepNet: A Unified-Light Model for Recursive Speech Separation with Unknown Speaker Count](https://www.isca-archive.org/interspeech_2025/alizadeh25_interspeech.html)
**Taxonomy:** `listening-and-separation / source-separation / blind-source-separation`
**Evidence:** D3 full-paper capture; PDF SHA-256 `1080da98bc7918d0e9cb9d557cb387781595586b3c0b4a77c653fa275cde0339`; full-text SHA-256 `3a723fffa265d98a25ae1701e36011e13b037aaf69e1c342e93bb3ff2dc53acd`.

- **Ordinary problem:** A recording may contain an unknown number of people speaking at once, but a useful separator must decide how many voices to return.
- **Why it is hard:** A fixed two- or three-speaker model fails when more people are present, while a separate model for each count grows expensive.
- **Naive attempt:** Tell the model the speaker count in advance, or select a decoder built for that count.
- **Central move:** Separate one stream at a time and let a lightweight authorization block decide when recursion should stop.
- **Mechanism:** ReSepNet applies a dual-path transformer repeatedly; each iteration estimates one source and cross-correlation decides whether another iteration is needed. It trains on two/three-speaker mixtures and tests on four/five.
- **Mathematical idea:** Permutation-invariant loss ignores output order. SI-SNR improvement is 21.16 dB on WSJ0-2mix, 19.19 on 3mix, 14.91 on 4mix, and 12.03 on 5mix; the 2.8M-parameter model estimates count with 96.6% accuracy.
- **What the paper reports:** The paper reports higher SI-SNR improvement than listed baselines and generalization from two/three-speaker training to four/five-speaker tests.
- **Limits:** The evidence is synthetic WSJ0 mixtures, 8-kHz four-second windows, and a bounded count range; real rooms and end-to-end recognition are not tested. Results are author-reported.

## 157. Deep-Simplex Multichannel Speech Separation

**Paper:** [Deep-Simplex Multichannel Speech Separation](https://www.isca-archive.org/interspeech_2025/avidan25_interspeech.html)
**Taxonomy:** `listening-and-separation / source-separation / blind-source-separation`
**Evidence:** D3 full-paper capture; PDF SHA-256 `6e1f4f21d71a4e5fd84a8bc5cd2cd80d6c84cf0a0f73c0c09b72a57c6ba472ae`; full-text SHA-256 `21a1dc5d4cdc779d52f631cc091f3c61cebb092a0c54db52f9dc994cb86a089c`.

- **Ordinary problem:** Separate simultaneous speakers using multiple microphones without requiring a fixed number of speakers or an impractically large model.
- **Why it is hard:** A microphone mixture hides each speaker, and real recordings vary in speaker count, room geometry, and spatial arrangement.
- **Naive attempt:** Train a separator for a fixed number of sources and assume the deployment mixture matches that training setting.
- **Central move:** Use a deep-simplex formulation that combines multichannel spatial evidence with a representation able to handle recursive or variable separation.
- **Mechanism:** The model consumes multichannel mixtures, estimates source structure and spatial cues, and recursively extracts separated streams; experiments compare source-count and computational behavior.
- **Mathematical idea:** The simplex represents mixture proportions or source assignment under constraints; separation losses compare estimated waveforms or spectra with reference sources and report scale-aware signal metrics.
- **What the paper reports:** The paper reports multichannel separation results with a deep-simplex approach designed for variable source conditions and compares it with established separators.
- **Limits:** Performance depends on microphone geometry, room conditions, source count, and the reference metrics; synthetic mixtures may not represent real overlap. No independent reproduction was performed.

## 158. Relative cue weighting in multilingual stop voicing production

**Paper:** [Relative cue weighting in multilingual stop voicing production](https://www.isca-archive.org/interspeech_2025/chan25_interspeech.html)
**Taxonomy:** `listening-and-separation / source-separation / target-conditioned-separation`
**Evidence:** D3 full-paper capture; PDF SHA-256 `cbf6402eb8136436928eb04ecc51861ff474c7cfa159f62f9a7c96d874147cab`; full-text SHA-256 `d5a13f9e6a9d5d523ed85c84b1cd94ff41138159bac988af828179498b83fe66`.

- **Ordinary problem:** A multilingual speaker must produce a stop contrast in several languages even when those languages use different cues such as closure voicing or aspiration.
- **Why it is hard:** The same person can keep language-specific categories while still showing dominance effects, and different acoustic cues can carry different weight in each language.
- **Naive attempt:** Assume one speaker-wide voicing rule or average all languages into one acoustic category.
- **Central move:** Measure nine acoustic correlates in Malay, English, and Mandarin speech from early multilingual Malaysians and use random forests to compare cue weighting.
- **Mechanism:** The paper studies relative cue weighting in multilingual stop-voicing production.
- **Mathematical idea:** Multilingual pronunciation is coordinated but not collapsed: language-specific cue bundles coexist with influence from which language is dominant for the speaker.
- **What the paper reports:** The paper reports language-specific production for all early multilinguals, dominance-driven variation, and a salient role for closure voicing in Malaysian English.
- **Limits:** The Malaysian speakers, three languages, stop inventory, nine correlates, and random-forest analysis bound generalization to other multilingual populations or contrasts.

## 159. NeuroSpex+: Dual-Task Training of Neuro-Guided Speaker Extraction with Speech Envelope and Waveform

**Paper:** [NeuroSpex+: Dual-Task Training of Neuro-Guided Speaker Extraction with Speech Envelope and Waveform](https://www.isca-archive.org/interspeech_2025/dasilva25_interspeech.html)
**Taxonomy:** `listening-and-separation / source-separation / target-conditioned-separation`
**Evidence:** D3 full-paper capture; PDF SHA-256 `5a6d839485f9407147d4fc2316bd2126c4e10a4e6fce1fad03c382e42df23ada`; full-text SHA-256 `073f8c08e752f036801df52208b241fcb1040646206c1941dc8f2e20355a2061`.

- **Ordinary problem:** In a group conversation, a listener's brain activity can indicate which talker they are attending to; the system should recover that talker's speech.
- **Why it is hard:** The neural cue is noisy and the extracted waveform can sound plausible while still losing the speech envelope that carries intelligibility.
- **Naive attempt:** Optimize only waveform reconstruction and hope the attended speaker remains identifiable.
- **Central move:** Train the extractor on two linked targets: the target waveform and its amplitude envelope.
- **Mechanism:** NeuroSpex+ uses EEG-derived reference cues and jointly predicts the target waveform and speech envelope to shape its mask.
- **Mathematical idea:** The two reconstruction objectives constrain both detailed waveform quality and slower envelope structure; signal-quality measures compare with baselines.
- **What the paper reports:** The paper reports significant improvement over baseline speaker-extraction systems.
- **Limits:** The evidence is bounded to the recorded EEG/speech setup and tested mixtures; listener attention changes, clinical use, and independent reproduction remain open.

## 160. MOPSA: Mixture of Prompt-Experts Based Speaker Adaptation for Elderly Speech Recognition

**Paper:** [MOPSA: Mixture of Prompt-Experts Based Speaker Adaptation for Elderly Speech Recognition](https://www.isca-archive.org/interspeech_2025/deng25_interspeech.html)
**Taxonomy:** `listening-and-separation / source-separation / target-conditioned-separation`
**Evidence:** D3 full-paper capture; PDF SHA-256 `89e2c4e3c8a917b92628e441d6648013c416f755dbf87d0f1c071dda90da3462`; full-text SHA-256 `6df4b97218b6fe03ab5e66119d3a5f490c6f1f11119f813f79add632f86c20df`.

- **Ordinary problem:** An ASR system should adapt online to an elderly speaker it has not seen, without stopping for a large offline retraining job.
- **Why it is hard:** Elderly speakers vary acoustically and linguistically, and one prompt that helps one speaker can hurt another.
- **Naive attempt:** Use one speaker-independent model or fine-tune a separate model per speaker.
- **Central move:** Cluster speaker prompts into experts and let a router mix acoustic and language prompts for the new speaker at run time.
- **Mechanism:** MOPSA uses K-means speaker prompt clusters and a router around Whisper, with separate acoustic and language-level prompts, tested on English and Cantonese elderly speech.
- **Mathematical idea:** The router is a mixture-of-experts choice; WER/CER measure recognition and real-time factor measures adaptation cost.
- **What the paper reports:** The paper reports relative WER/CER reductions of 4.21% and 5.40% and up to 16.12x real-time speedup over offline adaptation.
- **Limits:** Datasets, elderly populations, prompt clusters, and Whisper versions bound the claim; broader disorders, languages, and online failure recovery remain open.

## 161. Synchronous analysis of abnormal acoustic and linguistic production in Parkinson's speech

**Paper:** [Synchronous analysis of abnormal acoustic and linguistic production in Parkinson's speech](https://www.isca-archive.org/interspeech_2025/escobargrisales25_interspeech.html)
**Taxonomy:** `listening-and-separation / source-separation / target-conditioned-separation`
**Evidence:** D3 full-paper capture; PDF SHA-256 `618fa0b09963e911faf32aecbe031f0f370b444d76dc1dc5f4aa8a34b531a9a2`; full-text SHA-256 `5db740a46ae209728cfc4587abe99ee5bba3e8a8474ab73709b045ee6f5e7857`.

- **Ordinary problem:** Parkinson's speech can show changes in both how sounds are produced and how language is organized, so one signal family may give an incomplete picture.
- **Why it is hard:** Acoustic and linguistic symptoms vary across speakers and tasks, and changes can be correlated without one causing the other.
- **Naive attempt:** Use only a speech-rate/acoustic score or only a transcript-based linguistic score as a complete disease marker.
- **Central move:** Measure acoustic and linguistic production synchronously in the same speech material and examine their joint relationship.
- **Mechanism:** The study synchronizes analysis of abnormal acoustic and linguistic production in Parkinson's speech.
- **Mathematical idea:** Synchronous observation aligns two levels of behavior in time, allowing co-occurrence to be studied without pretending that either level alone explains the condition.
- **What the paper reports:** The paper reports coordinated acoustic and linguistic findings in Parkinson's speech.
- **Limits:** Cohort, task, disease stage, annotation, and statistical design limit clinical generalization; association is not diagnosis or causation.

## 162. IDIR: Identifying and Distilling Informative Relations for Speaker Verification

**Paper:** [IDIR: Identifying and Distilling Informative Relations for Speaker Verification](https://www.isca-archive.org/interspeech_2025/gan25_interspeech.html)
**Taxonomy:** `listening-and-separation / source-separation / target-conditioned-separation`
**Evidence:** D3 full-paper capture; PDF SHA-256 `b2e8c43f6e9f6ba654abf838dfaeb05e128c894d0dc997b29d6881b435daec17`; full-text SHA-256 `53dd82511bf2c923c3a9992df816c0ba8be1aaf5e5a20ac0559714ced5e0f7c1`.

- **Ordinary problem:** A compact speaker-verification model should retain who spoke when compressed from a large teacher, but copying each hidden feature can miss the structure of how speakers relate to one another.
- **Why it is hard:** Speaker identity is relational: the distance between two voices matters, and a student with less capacity cannot reproduce every teacher coordinate while preserving all useful pairwise distinctions.
- **Naive attempt:** Match the student's feature vector to the teacher's vector one example at a time or shrink the network and accept a loss of speaker separation.
- **Central move:** Distill informative within-speaker and between-speaker relations, then add a margin that pulls same-speaker pairs together and pushes different-speaker pairs apart.
- **Mechanism:** IDIR identifies informative relations in each mini-batch, distills them from teacher to student, and uses margin-adjusted similarity scores for speaker verification.
- **Mathematical idea:** The object being transferred is a geometry of identities rather than a list of feature values; similarity and verification thresholds test whether that geometry survives compression.
- **What the paper reports:** The paper reports improved speaker-verification performance over feature-matching distillation and stronger separation of same- and different-speaker relations.
- **Limits:** Teacher/student architectures, pair mining, margin, dataset, and verification protocol bound the claim; relational distillation does not ensure robustness to domain, overlap, or fairness shifts.

## 163. CabinSep: IR-Augmented Mask-Based MVDR for Real-Time In-car Speech Separation with Distributed Heterogeneous Arrays

**Paper:** [CabinSep: IR-Augmented Mask-Based MVDR for Real-Time In-car Speech Separation with Distributed Heterogeneous Arrays](https://www.isca-archive.org/interspeech_2025/han25d_interspeech.html)
**Taxonomy:** `listening-and-separation / source-separation / target-conditioned-separation`
**Evidence:** D3 full-paper capture; PDF SHA-256 `357c908853384866636202b9641a32347f56f1bae43aab81658d81daa1f095c8`; full-text SHA-256 `132c6ef94a16d5d3ec2778db70d1fd938bc59b07a73c27c36c79571836ebbaf6`.

- **Ordinary problem:** A vehicle assistant must separate overlapping passengers' speech in a changing cabin without introducing distortion that harms recognition.
- **Why it is hard:** Distributed heterogeneous microphones have different impulse responses, sources cross spatial zones, and a separator can improve isolation while damaging the words an ASR system needs.
- **Naive attempt:** Use a generic monaural mask or optimize separation quality without modeling the cabin or downstream recognition cost.
- **Central move:** Combine channel-aware spatial features with mask-based MVDR, augment training with both simulated and real impulse responses, and evaluate the separated signal through ASR.
- **Mechanism:** The mask estimates speech/noise structure from multichannel features; MVDR uses spatial covariance to preserve the chosen target, while mixed impulse-response augmentation exposes zone-boundary variation.
- **Mathematical idea:** Separation is constrained by two objectives: suppress interference through spatial covariance while retaining a distortionless target direction for the recognizer.
- **What the paper reports:** CabinSep reports a 17.5% relative ASR error reduction over DualSep on real recordings at 0.4 GMACs, with better behavior around speaker-zone boundaries.
- **Limits:** Cabin geometry, array placement, impulse-response coverage, ASR backend, and compute measure constrain generalization; ASR improvement is not proof of perceptual superiority for every listener.

## 164. Overlap-Adaptive Hybrid Speaker Diarization and ASR-Aware Observation Addition for MISP 2025 Challenge

**Paper:** [Overlap-Adaptive Hybrid Speaker Diarization and ASR-Aware Observation Addition for MISP 2025 Challenge](https://www.isca-archive.org/interspeech_2025/huang25k_interspeech.html)
**Taxonomy:** `listening-and-separation / source-separation / blind-source-separation`
**Evidence:** D3 full-paper capture; PDF SHA-256 `b3ae7c9f1c41b5d59186880d92a9813d4ee6d022d4ac2baa3eac27b9606fa4e8`; full-text SHA-256 `884ad10eff2154a5cea67700fc1e84e36d9932e4019216c3c9c68cf95700a1b4`.

- **Ordinary problem:** Meeting speech contains overlapping speakers, and diarization and recognition must make decisions from the same mixed observations.
- **Why it is hard:** Overlap changes which speaker evidence is reliable; guided source separation can fail at low signal-to-noise ratio.
- **Naive attempt:** Use one diarization model and assume separated observations are equally useful for ASR.
- **Central move:** Combine overlap-adaptive diarization with ASR-aware observation addition and a cascaded meeting-recognition system.
- **Mechanism:** A hybrid segmentation/clustering diarizer selects its model by overlap, while ASR-aware observations compensate for weak guided separation before recognition.
- **Mathematical idea:** Diarization assigns speaker-time regions; CER and concatenated minimum-permutation CER measure the downstream meeting transcript.
- **What the paper reports:** The system reports 9.48% CER and 11.56% cpCER and first place in both MISP tracks.
- **Limits:** Challenge tracks, meeting conditions, and author-reported ranking limit generalization and independent reproduction.

## 165. Neural Speech Extraction with Human Feedback

**Paper:** [Neural Speech Extraction with Human Feedback](https://www.isca-archive.org/interspeech_2025/itani25_interspeech.html)
**Taxonomy:** `listening-and-separation / source-separation / target-conditioned-separation`
**Evidence:** D3 full-paper capture; PDF SHA-256 `68f8bb70a3a6d06a4ca2d7ca7e871d42f23f9680b020bdcd2c4f0185d144dd95`; full-text SHA-256 `cf48eabd7e574c6847f95863048d98648d00c0d686441e24c28957817dcfe5d5`.

- **Ordinary problem:** A listener should extract a desired speech source from a mixture when ordinary separation assumptions are insufficient.
- **Why it is hard:** Target identity, mixture variability, and human preference can disagree with signal-level objectives.
- **Naive attempt:** Use an unconditioned separator and assume the loudest or most separable source is the desired one.
- **Central move:** Use human feedback to guide neural speech extraction toward the target source.
- **Mechanism:** Human preference supplies a target-selection signal alongside acoustic separation; the model is evaluated on extraction behavior.
- **Mathematical idea:** Separation is not only signal recovery: the system must specify which source counts as useful to a listener.
- **What the paper reports:** The paper reports neural speech extraction with human feedback.
- **Limits:** Feedback population, mixture construction, target definition, signal metrics, and model scope bound transfer.

## 166. FlowTSE: Target Speaker Extraction with Flow Matching

**Paper:** [FlowTSE: Target Speaker Extraction with Flow Matching](https://www.isca-archive.org/interspeech_2025/navon25_interspeech.html)
**Taxonomy:** `listening-and-separation / source-separation / target-conditioned-separation`
**Evidence:** D3 full-paper capture; PDF SHA-256 `38e9684b3f92cdbd235a5733e2e11a1a7311dd333b32418ef4467ecbe6297310`; full-text SHA-256 `643811cfbfc548a7bd7a5ad7747202a66ce8f3a7a3ec3279c7073f627505c5a5`.

- **Ordinary problem:** A listener should extract one enrolled speaker from a mixture even when interference is severe or unseen.
- **Why it is hard:** Discriminative masks can create artifacts and fail under distribution shift, while generative pipelines often require multiple pretrained components and poor phase reconstruction.
- **Naive attempt:** Map the mixture directly to a mask or waveform with a large pipeline, ignoring the enrolled speaker’s distribution and phase evidence.
- **Central move:** Condition flow matching on enrollment and mixture mel-spectrograms, and condition a vocoder on the mixture’s complex STFT when phase matters.
- **Mechanism:** A learned flow transports a noisy conditional distribution toward target speech; complex-STFT conditioning supplies phase information that mel features discard.
- **Mathematical idea:** Target extraction is conditional generation under an identity constraint, with magnitude and phase treated as complementary evidence.
- **What the paper reports:** The paper reports that FlowTSE matches or outperforms strong target-speaker-extraction baselines on standard benchmarks.
- **Limits:** Enrollment quality, speaker/noise shift, phase-vocoder design, benchmark mixtures, and signal metrics bound transfer; extraction quality is not automatically improved ASR or hearing-aid benefit.

## 167. Online Audio-Visual Autoregressive Speaker Extraction

**Paper:** [Online Audio-Visual Autoregressive Speaker Extraction](https://www.isca-archive.org/interspeech_2025/pan25_interspeech.html)
**Taxonomy:** `listening-and-separation / source-separation / target-conditioned-separation`
**Evidence:** D3 full-paper capture; PDF SHA-256 `4ad75662db5d03e521ac1ea2c74aefe6c8d1d0fe91e8476ed8d14fd9368da36f`; full-text SHA-256 `70928e1f384fef6f47579a9594765aedbf87460a426af06d5a900e3c05cbcd46`.

- **Ordinary problem:** A streaming listener should extract the person being watched even when speakers overlap and attention later switches.
- **Why it is hard:** The visual cue is noisy and delayed, the mixture changes over time, and an offline separator can use future context that a live system lacks.
- **Naive attempt:** Process each frame independently or optimize only the audio branch while ignoring the extracted signal’s history.
- **Central move:** Use a lightweight visual front end and an autoregressive acoustic encoder that feeds past separated speech back into the online model, then test target-switching scenes.
- **Mechanism:** Visual embeddings select the target, while the recurrent acoustic path summarizes prior separated audio; the mask is updated causally under a compute budget.
- **Mathematical idea:** Streaming separation is causal state estimation: the system must preserve target identity while updating its estimate from current visual and acoustic evidence.
- **What the paper reports:** On LRS3, the paper reports competitive separation quality with about 0.1M visual parameters and 2.1 MACs/s, and evaluates switching attention.
- **Limits:** LRS3 faces, switching schedule, audiovisual synchronization, causal latency, and separation metrics bound transfer; benchmark separation is not a full human-attention study.

## 168. Location-Aware Target Speaker Extraction for Hearing Aids

**Paper:** [Location-Aware Target Speaker Extraction for Hearing Aids](https://www.isca-archive.org/interspeech_2025/alcalapadilla25_interspeech.html)
**Taxonomy:** `listening-and-separation / spatial-listening / spatial-filtering`
**Evidence:** D3 full-paper capture; PDF SHA-256 `cd6aca2134a1fb17edf1017a420dfbb684a15c5cb9f1d9c3a13550e173159757`; full-text SHA-256 `6ecc6ea1f914b31d7b0ae25bcf510c3ef938eb2d321b6feb1be17fdac7381740`.

- **Ordinary problem:** A hearing-aid listener should extract a desired talker using where the sound comes from.
- **Why it is hard:** Target and interferer overlap in frequency and may move while hearing aids provide limited spatial evidence.
- **Naive attempt:** Use a fixed beamformer or spectral mask without conditioning on target location.
- **Central move:** Make target location explicit in a location-aware target-speaker extraction model.
- **Mechanism:** Spatial features condition separation toward the selected direction.
- **Mathematical idea:** The relevant object is the spatial-filtering evidence described by the paper's mechanism: Spatial features condition separation toward the selected direction.
- **What the paper reports:** The paper reports location-aware target-speaker extraction for hearing-aid scenarios.
- **Limits:** Array geometry, motion, layout, processing, and intelligibility metric bound transfer.

## 169. A Study of Real-world Audio-Visual Corpus Design and Production: A Perspective from MISP Challenges

**Paper:** [A Study of Real-world Audio-Visual Corpus Design and Production: A Perspective from MISP Challenges](https://www.isca-archive.org/interspeech_2025/chen25k_interspeech.html)
**Taxonomy:** `listening-and-separation / spatial-listening / spatial-filtering`
**Evidence:** D3 full-paper capture; PDF SHA-256 `af4012fb05e9102737e66195b41eb2e5bcbc96da3e220a66ec42d9384146166a`; full-text SHA-256 `a3797a65a5a04c329cbef9d0bbac606d2b3c2e28d649051116d6a685caf2dd00`.

- **Ordinary problem:** Audio-visual speech systems fail in the real world when cameras, microphones, rooms, participants, and manual labels do not match the clean assumptions of a benchmark.
- **Why it is hard:** Corpus choices determine which overlap, distance, visibility, and synchronization problems a model can learn; a large dataset can still hide bias if its recording process is undocumented.
- **Naive attempt:** Collect convenient audio and video separately, align them afterward, and treat the resulting benchmark as a neutral sample of deployment.
- **Central move:** Design the corpus around deployment scenarios, synchronized equipment, annotation and alignment procedures, and explicit task requirements, then inspect how those choices shape downstream results.
- **Mechanism:** The paper analyzes the MISP 2022–2024 corpora for audio-visual wakeup, diarization, enhancement, and recognition, covering scenario selection, recording equipment/processes, manual transcription, and alignment.
- **Mathematical idea:** A corpus is part of the measurement apparatus: room, device, overlap, annotation, and synchronization define the conditional distribution on which a model is judged.
- **What the paper reports:** The paper reports broad adoption of the corpora by over 110 teams and identifies design strengths and limitations that affect audio-visual speech-processing comparisons.
- **Limits:** Challenge construction, participant selection, language, room/device coverage, and annotation policy bound generalization; downloading or winning on a corpus does not prove deployment realism.

## 170. SoundSculpt: Direction and Semantics Driven Ambisonic Target Sound Extraction

**Paper:** [SoundSculpt: Direction and Semantics Driven Ambisonic Target Sound Extraction](https://www.isca-archive.org/interspeech_2025/chen25l_interspeech.html)
**Taxonomy:** `listening-and-separation / spatial-listening / spatial-filtering`
**Evidence:** D3 full-paper capture; PDF SHA-256 `6b6c5209588a31723d6aa6dade6a80ef7bc3005c9ed78bf7daf71a665a7cdfd5`; full-text SHA-256 `8fcb8aa338dfdbe8718f77abb0f3fb2c49c97bd06ec4418b1731357c5756b9f5`.

- **Ordinary problem:** A listener should be able to extract a selected sound from an ambisonic scene using both where it is and what it is.
- **Why it is hard:** The target direction is continuous while semantic cues are uncertain; spatial-only extraction can confuse co-located or reverberant sources and semantic-only cues ignore acoustic geometry.
- **Naive attempt:** Apply one fixed beamformer or condition a monaural extractor on a text label without modeling the multichannel sound field.
- **Central move:** Condition an ambisonic-in/ambisonic-out extractor jointly on target direction and semantic embeddings, and test whether the cues complement one another.
- **Mechanism:** The network maps multichannel ambisonic mixtures to a target sound field; direction and image-derived semantic embeddings guide the mask or representation used for extraction.
- **Mathematical idea:** Spatial filtering and semantic conditioning define complementary constraints: the output must preserve the target's spatial structure while suppressing other sources.
- **What the paper reports:** SoundSculpt outperforms the reported signal-processing baselines on synthetic and real ambisonic mixtures, with joint spatial-semantic conditioning helping in difficult cases.
- **Limits:** Synthetic scene construction, ambisonic order, semantic detector quality, room conditions, and target definition bound transfer; benchmark improvement is not guaranteed perceptual source isolation in arbitrary rooms.

## 171. Spatio-Spectral Diarization of Meetings by Combining TDOA-based Segmentation and Speaker Embedding-based Clustering

**Paper:** [Spatio-Spectral Diarization of Meetings by Combining TDOA-based Segmentation and Speaker Embedding-based Clustering](https://www.isca-archive.org/interspeech_2025/cordlandwehr25_interspeech.html)
**Taxonomy:** `listening-and-separation / spatial-listening / spatial-filtering`
**Evidence:** D3 full-paper capture; PDF SHA-256 `fa9bfe875dd7027f5e8de013a9cafda5d3a9b3896cb16a2a81d759ef89729d08`; full-text SHA-256 `baa9b69f3a0ba4b3d96d0e0130322391b33e818ea9e05a5d61273b76f7b4cf7d`.

- **Ordinary problem:** Meeting transcription needs to know who spoke when despite overlap and movement.
- **Why it is hard:** Position is not permanent identity when people move, while a single microphone loses direction information.
- **Naive attempt:** Use speaker embeddings alone or permanently map one direction to one speaker.
- **Central move:** Segment with time-difference-of-arrival cues, cluster speaker embeddings, and combine spatial and spectral evidence.
- **Mechanism:** TDOA detects regions, embeddings assign speakers, cACGMM optionally refines them, and compact/distributed microphone setups are tested.
- **Mathematical idea:** DER measures segmentation/assignment and cpWER measures transcript performance after diarization.
- **What the paper reports:** The combined pipeline outperforms single-channel pyannote in reported compact and distributed meeting scenarios.
- **Limits:** Layouts, datasets, overlap, and spatial cues bound the result; evaluations are author-reported.

## 172. Deep learning based spatial aliasing reduction in beamforming for audio capture

**Paper:** [Deep learning based spatial aliasing reduction in beamforming for audio capture](https://www.isca-archive.org/interspeech_2025/guzik25_interspeech.html)
**Taxonomy:** `listening-and-separation / spatial-listening / spatial-filtering`
**Evidence:** D3 full-paper capture; PDF SHA-256 `5553e9d850f2027998ceae3c4b1b8adbf3078b2c356f7e39c7bd2a74b91a2478`; full-text SHA-256 `e1d06f5e58bfb7b35e6aff76968b2f64019c519ea79a8d9e3100abce6505ec0f`.

- **Ordinary problem:** A microphone array should capture a desired direction without high-frequency spatial aliasing destroying beamformer accuracy.
- **Why it is hard:** Sparse or widely spaced arrays create directional ambiguity above the aliasing frequency, while an adaptive correction must preserve useful cross-channel phase and remain computationally practical.
- **Naive attempt:** Use a conventional beamformer unchanged, or apply a generic post-filter that ignores the array geometry and signal dependence.
- **Central move:** Predict a signal-dependent de-aliasing filter with a U-Net and apply it to conventional beamforming, comparing independent-channel and cross-channel designs.
- **Mechanism:** The model estimates a filter from multichannel spectro-temporal input; the corrected beamformer output is evaluated in common spatial-capture scenarios against conventional and learned alternatives.
- **Mathematical idea:** The learned filter approximates an inverse of geometry-induced aliasing, but its validity depends on the array and acoustic distribution represented during training.
- **What the paper reports:** The paper reports reduced spatial aliasing and improved spatial/spectral capture measures for the proposed deep-learning correction in the tested scenarios.
- **Limits:** Array geometry, source locations, reverberation, training mixtures, and scenario coverage constrain generalization; simulated or benchmark gains do not establish robustness for every microphone layout.

## 173. End-to-End DOA-Guided Speech Extraction in Noisy Multi-Talker Scenarios

**Paper:** [End-to-End DOA-Guided Speech Extraction in Noisy Multi-Talker Scenarios](https://www.isca-archive.org/interspeech_2025/jing25b_interspeech.html)
**Taxonomy:** `listening-and-separation / spatial-listening / spatial-filtering`
**Evidence:** D3 full-paper capture; PDF SHA-256 `3a8e03eb37aef854c14e14103238fb9ad83abd3c1bb649843711d8d41071b6bf`; full-text SHA-256 `8de214160a293099e87daefe89340a94762871323a5641c15a05ccba9af73eca`.

- **Ordinary problem:** In a noisy multi-talker scene, a listener or recognizer needs the speaker inside a requested spatial region while suppressing nearby voices.
- **Why it is hard:** Direction of arrival alone is ambiguous, beamwidth controls a precision-recall tradeoff, and multiple speakers can occupy overlapping acoustic and spatial regions.
- **Naive attempt:** Apply a fixed beamformer or condition extraction only on a speaker embedding while ignoring where the target is.
- **Central move:** Guide an end-to-end target extractor with DOA and beamwidth embeddings so the requested spatial region becomes an explicit conditioning signal.
- **Mechanism:** The model combines spatial and temporal features, uses the DOA as a center and beamwidth as the permitted region, and generates the target waveform for enhancement and ASR.
- **Mathematical idea:** The beamwidth is a controllable spatial prior: narrowing it suppresses more off-axis energy but risks target loss, while widening it preserves coverage at the cost of interference.
- **What the paper reports:** The paper reports stronger target enhancement, interference suppression, and downstream ASR performance in the evaluated noisy multi-talker scenarios.
- **Limits:** DOA estimation, array geometry, spatial overlap, noise type, beamwidth selection, and benchmark composition bound transfer; reported ASR gains do not establish universal spatial hearing quality.

## 174. Co-Speech Motion for Virtual Agents in Dialogue Using LLM-Driven Primitive Action Selection

**Paper:** [Co-Speech Motion for Virtual Agents in Dialogue Using LLM-Driven Primitive Action Selection](https://www.isca-archive.org/interspeech_2025/baihaqi25b_interspeech.html)
**Taxonomy:** `meaning-and-interaction / grounding-and-action / interactional-feedback`
**Evidence:** D3 full-paper capture; PDF SHA-256 `cfa82ec0ba9faa7f318f26b898e9e88c3b0e1e139ba6aeab5946752ff63d6b0b`; full-text SHA-256 `f39cafb121129259ab85f7df17182f73a1be6204201c49afcff08de6758bf4a9`.

- **Ordinary problem:** A virtual agent should move in ways that fit what it is saying without requiring a hand-written rule for every situation.
- **Why it is hard:** Rules do not generalize, while purely data-driven gesture generation is costly and often tied to one embodiment.
- **Naive attempt:** Choose gestures from fixed rules or train a large motion generator for each agent.
- **Central move:** Use an LLM to plan context and select reusable primitive actions that can be adapted across agents.
- **Mechanism:** The proposed model uses LLM-driven primitive action selection for co-speech motion in virtual agents and robots.
- **Mathematical idea:** The key object is the mapping from dialogue context to a sequence of primitive actions; the paper's abstract does not expose a complete quantitative comparison.
- **What the paper reports:** The paper presents a flexible and scalable approach, but the preserved evidence does not establish a numerical gain.
- **Limits:** Full mechanism, baselines, human judgments, and cross-embodiment transfer require the paper's detailed evaluation; the result is not a claim of human-like motion.

## 175. Fact-Controlled Diagnosis of Hallucinations in Medical Text Summarization

**Paper:** [Fact-Controlled Diagnosis of Hallucinations in Medical Text Summarization](https://www.isca-archive.org/interspeech_2025/bn25_interspeech.html)
**Taxonomy:** `meaning-and-interaction / grounding-and-action / referential-grounding`
**Evidence:** D3 full-paper capture; PDF SHA-256 `a4c0a8b359d71c896758b1380dfed179ed3b2fc39a1a03e1d7e2dea089e5d012`; full-text SHA-256 `5223ec22daca90ce50d950644af9ab54b278fe0851e4efbcf28bed92c453c1c6`.

- **Ordinary problem:** A medical summarizer may invent a fact about a patient-clinician conversation, so a detector needs controlled examples as well as naturally occurring failures.
- **Why it is hard:** Hallucinations are rare and variable; general-domain detectors may confuse missing evidence with a false claim, especially when the source is speech-derived clinical dialogue.
- **Naive attempt:** Evaluate only on generic hallucination data or label summaries without controlling which source fact was removed.
- **Central move:** Construct a fact-controlled leave-one-out dataset and a natural hallucination dataset, then compare detection methods in the clinical setting.
- **Mechanism:** The paper studies fact-controlled diagnosis of hallucinations in medical text summarization from patient-clinician dialogues.
- **Mathematical idea:** A controlled deletion makes the missing fact known, while natural cases test ecological validity; the two together separate detector sensitivity from dataset artifacts.
- **What the paper reports:** The paper reports that general-domain detectors struggle on clinical hallucinations and evaluates specialized diagnostic approaches.
- **Limits:** Synthetic deletion, clinical language, annotation, summarizer, and detector thresholds limit generalization; detection is not prevention or clinical validation.

## 176. From Words to Waves: Analyzing Concept Formation in Speech and Text-Based Foundation Models

**Paper:** [From Words to Waves: Analyzing Concept Formation in Speech and Text-Based Foundation Models](https://www.isca-archive.org/interspeech_2025/ersoy25_interspeech.html)
**Taxonomy:** `meaning-and-interaction / grounding-and-action / referential-grounding`
**Evidence:** D3 full-paper capture; PDF SHA-256 `94dbe85e2eca531544c854db522bc0d7719db94a38cc1d775d68e548153f05f8`; full-text SHA-256 `6e688883b822aea6bae7a32bf41e45fcb43a338d1625a98653089db1125ab892`.

- **Ordinary problem:** Speech models may represent concepts differently from text models, and a joint model may combine or distort those structures rather than simply inheriting text knowledge.
- **Why it is hard:** Latent concepts are not directly labeled; comparing modalities requires a method that exposes structure without pretending an interpretation is a measured neuron-level fact.
- **Naive attempt:** Inspect nearest words or report downstream accuracy and call the result a theory of concept formation.
- **Central move:** Use latent concept analysis to compare speech-only, text-only, and joint foundation models and ask which conceptual structures are shared or modality-specific.
- **Mechanism:** The paper analyzes concept formation in speech and text-based foundation models using an unsupervised latent-concept method.
- **Mathematical idea:** Concept formation is treated as a representation-comparison problem: the analysis proposes interpretable structure, while cross-modal differences reveal what the training signal makes easy or hard to encode.
- **What the paper reports:** The paper reports comparative latent conceptual structures across speech, text, and joint models.
- **Limits:** Model choice, layer, analysis method, prompts, and human interpretation bound the claim; a latent cluster is not automatically a human concept.

## 177. AC/DC: LLM-based Audio Comprehension via Dialogue Continuation

**Paper:** [AC/DC: LLM-based Audio Comprehension via Dialogue Continuation](https://www.isca-archive.org/interspeech_2025/fujita25b_interspeech.html)
**Taxonomy:** `meaning-and-interaction / grounding-and-action / referential-grounding`
**Evidence:** D3 full-paper capture; PDF SHA-256 `44933b5f4e1dbb33239fb8035bb87fd59d0b5eb74c022597b55825040ba7f420`; full-text SHA-256 `c3e3388f015d131fb9af26a5afed95cd8d100a559cfaa3f26e82a260b144e87f`.

- **Ordinary problem:** An audio-language system should answer different questions about the same sound, not memorize one caption wording.
- **Why it is hard:** Several captions can describe one sound, and direct reference-sentence training can reward surface wording rather than scene meaning.
- **Naive attempt:** Train directly to reproduce the dataset caption and assume fluency implies instruction following.
- **Central move:** Train the model to continue a dialogue after an audio-triggered caption, making the target a conversational response.
- **Mechanism:** An audio encoder feeds an adapter and language model; interleaved audio/text examples use token cross-entropy, with LoRA tested on AudioCaps, WavCaps, and Clotho.
- **Mathematical idea:** The loss is token-level cross-entropy. The best reported average AQA accuracy is 47.70%, judged by Llama-3-70B-Instruct; the judge is itself a proxy.
- **What the paper reports:** Dialogue-continuation training enables zero-shot instruction following and improves reported AQA, while AAC gains are mixed.
- **Limits:** Generated captions, benchmarks, and an LLM judge define the evidence; human usefulness for deaf or hard-of-hearing users is not established.

## 178. Vela: Scalable Embeddings with Voice Large Language Models for Multimodal Retrieval

**Paper:** [Vela: Scalable Embeddings with Voice Large Language Models for Multimodal Retrieval](https://www.isca-archive.org/interspeech_2025/hu25b_interspeech.html)
**Taxonomy:** `meaning-and-interaction / grounding-and-action / referential-grounding`
**Evidence:** D3 full-paper capture; PDF SHA-256 `f4898c608bf99e2fef3492b20bbd9d63da3d711b4d7d0385799a79b9bc804c3a`; full-text SHA-256 `4747cb72e81897157748b75fac0efe9e5cc40b5f78ebf6c0d06347b8d729a181`.

- **Ordinary problem:** A retrieval system should find the right audio for a long, complicated text request, not only match short captions to short clips.
- **Why it is hard:** Audio and text embeddings are trained in different modalities, and simple CLAP-style matching weakens on long or compositional queries.
- **Naive attempt:** Use a fixed audio-text contrastive model and rely on its pooled embedding for every query.
- **Central move:** Adapt a multimodal language model to produce a universal embedding, using prompts and text-pair training without requiring paired audio in the final training stage.
- **Mechanism:** Vela uses selected prompts and in-context examples, then trains on text pairs; retrieval is tested on ordinary and newly designed long/complex benchmarks.
- **Mathematical idea:** Text-audio retrieval metrics compare the rank of the correct audio; the new tests ask whether the embedding preserves multiple pieces of a query.
- **What the paper reports:** The paper reports that Vela outperforms traditional CLAP models and is more robust on long, complex retrieval tasks.
- **Limits:** The abstract says code is forthcoming and the result is tied to the chosen benchmarks and prompts; open-world audio, speech-specific retrieval, and independent reproduction remain open.

## 179. Language-Guided Contrastive Audio-Visual Masked Autoencoder with Automatically Generated Audio-Visual-Text Triplets from Videos

**Paper:** [Language-Guided Contrastive Audio-Visual Masked Autoencoder with Automatically Generated Audio-Visual-Text Triplets from Videos](https://www.isca-archive.org/interspeech_2025/ishikawa25_interspeech.html)
**Taxonomy:** `meaning-and-interaction / grounding-and-action / referential-grounding`
**Evidence:** D3 full-paper capture; PDF SHA-256 `caf6e98eef9410d02091cb4b208e6dc501dca412d32e55291e3327d0357385fd`; full-text SHA-256 `2541c74f9b78d1ba3b748d14c1d77e364f2cf49a105baae0aa6ef4deac02c5f0`.

- **Ordinary problem:** An audio-visual model should connect what an event sounds like, what it looks like, and what language describes it without requiring every video to be manually labeled.
- **Why it is hard:** Unlabeled videos contain weak and sometimes misleading cross-modal matches, so training on arbitrary audio-caption pairs can teach the wrong correspondence.
- **Naive attempt:** Use one modality pair or trust automatically generated captions without filtering them.
- **Central move:** Generate frame captions, filter audio-caption pairs with a CLAP similarity check, and train a text-guided contrastive masked autoencoder over audio, video, and text.
- **Mechanism:** A pretrained text encoder guides masked audio-visual reconstruction and contrastive learning; automatically formed triplets are used for retrieval and classification tests.
- **Mathematical idea:** Contrastive loss pulls matching modalities together and separates mismatches; masking forces the remaining views to predict missing information rather than copy it.
- **What the paper reports:** The paper reports up to 5.6% recall@10 improvement for retrieval and 3.2% for classification.
- **Limits:** The video domains, caption generator, CLAP filter, and downstream tasks define the result; spoken conversation and human annotation quality outside those videos remain open.

## 180. Face2VoiceSync: Lightweight Face-Voice Consistency for Text-Driven Talking Face Generation

**Paper:** [Face2VoiceSync: Lightweight Face-Voice Consistency for Text-Driven Talking Face Generation](https://www.isca-archive.org/interspeech_2025/kang25c_interspeech.html)
**Taxonomy:** `meaning-and-interaction / grounding-and-action / referential-grounding`
**Evidence:** D3 full-paper capture; PDF SHA-256 `bef3996fb824e750552a884236f007a9c97a1f51dd62cd0fb0a0d48a295fef5c`; full-text SHA-256 `d6989c5b4fba42f2cd04c58a711eb1a71b62d442962949139a399677d1b190c0`.

- **Ordinary problem:** A talking-face system should make a face and a voice that agree when given a face image and text, rather than forcing the user to supply a matching speech recording.
- **Why it is hard:** Text specifies what is said but not the target voice, while a face image specifies appearance but not timing or vocal identity; independently generating the modalities can create a visible-audible mismatch.
- **Naive attempt:** Drive the face from a fixed speech signal or generate a generic voice and animate the face afterward without checking cross-modal consistency.
- **Central move:** Generate the talking-face motion and speech jointly from face and text, with a consistency constraint linking the visual identity and vocal output.
- **Mechanism:** Face2VoiceSync targets text-driven talking-face generation from a face image and text, producing animation and corresponding speech while evaluating the consistency of face and voice attributes.
- **Mathematical idea:** The desired output is a coupled pair: text constrains linguistic content, face conditions visual identity, and a learned cross-modal relation checks whether the generated voice belongs with the generated face.
- **What the paper reports:** The paper reports improved face-voice consistency and text-driven talking-face generation quality relative to fixed-speech baselines.
- **Limits:** Face identities, text prompts, speech/face datasets, consistency metric, and synchronization quality bound the claim; a consistency score does not prove that a viewer will find the character natural or trustworthy.

## 181. Pick and Summarize: Integrating Extractive and Abstractive Speech Summarization

**Paper:** [Pick and Summarize: Integrating Extractive and Abstractive Speech Summarization](https://www.isca-archive.org/interspeech_2025/kano25_interspeech.html)
**Taxonomy:** `meaning-and-interaction / grounding-and-action / referential-grounding`
**Evidence:** D3 full-paper capture; PDF SHA-256 `997ea5b167f4e13e8fcb709835e7908af2b2e1fddd502c6da93f7c9e990384e3`; full-text SHA-256 `dfef4f07cbe688f35a95c03b95d0223a8d1ccfd1920839910e3f8cdf4f9428ee`.

- **Ordinary problem:** A summary of a long spoken presentation must retain the important points without forcing a model to search the whole sequence and compose everything at once.
- **Why it is hard:** Long speech contains many irrelevant stretches, and an abstractive system can lose key content while generating fluent text.
- **Naive attempt:** Generate the summary directly and assume the generator will discover the important spans.
- **Central move:** First identify useful excerpts from the speech, then use that auxiliary selection signal to guide abstractive summary generation.
- **Mechanism:** An extractive-abstractive model is trained on a web-presentation corpus, with an extractive summary predicted from raw speech alongside the final text summary.
- **Mathematical idea:** Selection narrows the content problem before wording is generated; METEOR compares the final summary with reference summaries while the extractive task supplies structure.
- **What the paper reports:** The method gives consistent gains and up to 1.4 METEOR points over a strong abstractive baseline.
- **Limits:** The corpus, reference summaries, metric, summary length, and presentation style bound the result; lexical overlap does not prove that all important facts were preserved.

## 182. Towards Human-like Multimodal Conversational Agent by Generating Engaging Speech

**Paper:** [Towards Human-like Multimodal Conversational Agent by Generating Engaging Speech](https://www.isca-archive.org/interspeech_2025/kim25m_interspeech.html)
**Taxonomy:** `meaning-and-interaction / grounding-and-action / interactional-feedback`
**Evidence:** D3 full-paper capture; PDF SHA-256 `ec031e7957b2dd522e3824d9f4d616b5ccdcce329d265da100adb55cb4b91182`; full-text SHA-256 `42c9b4ac510771d16ce4bd06e8365ca10ae9f37e2362beead86fd474d643a542`.

- **Ordinary problem:** A conversational agent can choose the right words yet sound dull or socially mismatched because real conversation also uses tone, mood, gesture, and response style.
- **Why it is hard:** These cues are spread across audio and video and are not fully recoverable from the text transcript; an engaging response must coordinate meaning with how it is said.
- **Naive attempt:** Generate a text response from text alone and use a generic TTS voice, or append a fixed emotion label after generation.
- **Central move:** Use audio-visual context to generate both the response text and a description of the voice style, then synthesize speech that carries the selected paralinguistic cues.
- **Mechanism:** The system builds a multi-sensory conversation dataset and uses a multimodal language model to produce text plus voice descriptions, which guide speech generation in dialogue examples.
- **Mathematical idea:** The model separates what to say from how to say it but conditions both on the same conversational state; human judgments of engagement and relevance test whether the separation remains coordinated.
- **What the paper reports:** The paper reports more engaging and contextually suitable speech than text-only baselines and shows gains from visual and audio modalities.
- **Limits:** Dataset role-play, judge criteria, synthetic or recorded voices, conversation domain, and lack of exact-speaker replication bound the claim; engagement scores do not establish long-term human trust or natural conversation.

## 183. Teaching Audio-Aware Large Language Models What Does Not Hear: Mitigating Hallucinations through Synthesized Negative Samples

**Paper:** [Teaching Audio-Aware Large Language Models What Does Not Hear: Mitigating Hallucinations through Synthesized Negative Samples](https://www.isca-archive.org/interspeech_2025/kuan25_interspeech.html)
**Taxonomy:** `meaning-and-interaction / grounding-and-action / referential-grounding`
**Evidence:** D3 full-paper capture; PDF SHA-256 `5a0ba8d790ffdaf6628bafeb0eeb1a0ad8dbb73d8dd1bc07a7be49b94ef20144`; full-text SHA-256 `1e4ec0e764027f5b4086d53397ff16126bcf48fbdcd13755d790c6ce95a908d0`.

- **Ordinary problem:** An audio-aware language model should say when spoken input does not contain enough evidence instead of confidently inventing what it did not hear.
- **Why it is hard:** Hallucinations can arise from the language model's prior or from ambiguous/noisy audio; ordinary positive examples do not teach the model when to abstain.
- **Naive attempt:** Train only on correct audio-text pairs or add generic negative text and assume the model learns auditory limits.
- **Central move:** Synthesize negative samples that explicitly represent what the audio does not contain and train the model to distinguish heard evidence from plausible language completion.
- **Mechanism:** The paper teaches audio-aware large language models what they do not hear through synthesized negative samples.
- **Mathematical idea:** The negative examples define an evidence boundary: language generation is rewarded only when its claim is supported by the acoustic input, not merely likely in context.
- **What the paper reports:** The paper reports reduced hallucination behavior for the tested audio-aware models and synthesized negative-sample strategy.
- **Limits:** Negative-sample construction, audio quality, prompts, model family, and evaluation rubric limit the claim; abstention quality is not the same as factual clinical reliability.

## 184. Bridging Audio and Vision: Zero-Shot Audiovisual Segmentation by Connecting Pretrained Models

**Paper:** [Bridging Audio and Vision: Zero-Shot Audiovisual Segmentation by Connecting Pretrained Models](https://www.isca-archive.org/interspeech_2025/lee25b_interspeech.html)
**Taxonomy:** `meaning-and-interaction / grounding-and-action / referential-grounding`
**Evidence:** D3 full-paper capture; PDF SHA-256 `a32f88413fcdf3a61edaacf056e4c82e60474bc3d0383c127c212ad02ea35366`; full-text SHA-256 `9665a223986e0e9125f07388e353764f5769463dda88020749c0bb45ce20d018`.

- **Ordinary problem:** An audio-visual system should identify the regions in a video associated with a sound, even for categories or scenes it did not see during training.
- **Why it is hard:** Audio and vision have different timing and semantics; zero-shot matching can confuse co-occurrence with the object that actually produced the sound.
- **Naive attempt:** Detect objects from vision alone or train a closed-set audiovisual segmenter and reject unseen categories.
- **Central move:** Connect pretrained audio and vision models so shared representations can guide zero-shot audiovisual segmentation.
- **Mechanism:** The paper studies zero-shot audiovisual segmentation by bridging pretrained audio and vision models.
- **Mathematical idea:** Segmentation is grounded association: the system must align a sound event with a spatial region using cross-modal evidence rather than merely classify the clip.
- **What the paper reports:** The paper reports zero-shot audiovisual segmentation results for the connected pretrained models.
- **Limits:** Datasets, categories, synchronization, pretrained models, and segmentation labels bound the result; co-occurrence does not establish physical source identity.

## 185. Speech-IFEval: Evaluating Instruction-Following and Quantifying Catastrophic Forgetting in Speech-Aware Language Models

**Paper:** [Speech-IFEval: Evaluating Instruction-Following and Quantifying Catastrophic Forgetting in Speech-Aware Language Models](https://www.isca-archive.org/interspeech_2025/lu25c_interspeech.html)
**Taxonomy:** `meaning-and-interaction / grounding-and-action / speech-act`
**Evidence:** D3 full-paper capture; PDF SHA-256 `2ac1c2c1da9febb888cb62b28f31feee0df4798f27e8475d0813205687d08499`; full-text SHA-256 `dbafe698f9abc3538dc242c24393588f5c8a2d28675e414cafec5ffa7945f3b2`.

- **Ordinary problem:** A speech-aware language model should follow spoken instructions and retain earlier abilities after learning new ones.
- **Why it is hard:** Instruction following can improve while unrelated skills are forgotten; speech adds recognition errors and modality-specific variation to the usual language-model tradeoff.
- **Naive attempt:** Measure only new-task accuracy or train on new instruction data and assume old abilities remain intact.
- **Central move:** Use Speech-IFEval to test instruction-following behavior and quantify catastrophic forgetting across speech-aware tasks.
- **Mechanism:** The paper introduces Speech-IFEval and evaluates instruction-following and forgetting in speech-aware language models.
- **Mathematical idea:** Evaluation must pair compliance with retention: a model that follows a new command by losing old behavior has shifted capability rather than simply improved it.
- **What the paper reports:** The paper reports benchmark results for spoken instruction following and catastrophic forgetting.
- **Limits:** Task suite, speech recognition quality, prompts, model families, and training order bound the conclusions; benchmark retention is not proof of reliable deployment behavior.

## 186. Unified Audio-Visual Modeling for Recognizing Which Face Spoke When and What in Multi-Talker Overlapped Speech and Video

**Paper:** [Unified Audio-Visual Modeling for Recognizing Which Face Spoke When and What in Multi-Talker Overlapped Speech and Video](https://www.isca-archive.org/interspeech_2025/makishima25b_interspeech.html)
**Taxonomy:** `meaning-and-interaction / grounding-and-action / referential-grounding`
**Evidence:** D3 full-paper capture; PDF SHA-256 `8c739fc23e9c9e45b9a20a9b26c7119d3849582044d1b3639a4b5b6726fad498`; full-text SHA-256 `3fbcf6da100f3c33c4aee4968cb9a48933858674be531cc6bfa4721f403be0f1`.

- **Ordinary problem:** In an overlapping conversation, understanding requires assigning each word and time interval to the correct face, not merely producing a bag of words.
- **Why it is hard:** A pipeline that separately separates speech, detects active speakers, and recognizes speech accumulates interfaces and errors.
- **Naive attempt:** Run single-talker ASR or chain independent separation, lip-motion detection, and transcription modules.
- **Central move:** Train one encoder-decoder to emit a serialized sequence containing speaker tags, timing structure, and words from overlapped audio plus all visible faces.
- **Mechanism:** The model combines speech and video encoders with Transformer decoding; evaluation compares it with single-talker, multi-talker, and modular audio-visual baselines on LRS3-derived mixtures.
- **Mathematical idea:** WER measures words, TER measures which face spoke when, and VWER charges a word error when the speaker tag is wrong even if another transcript is correct. This makes attribution part of recognition.
- **What the paper reports:** The proposed model reports lower or competitive WER/VWER and strong VTER as the number of overlapping speakers rises, with tags placed before or after each transcription tested explicitly.
- **Limits:** The evidence is bounded to constructed LRS3 mixtures, visible faces, tested overlap counts, and author-reported metrics; natural meetings, missed faces, and long-range turn structure remain open.

## 187. Beat gestures made by human-like avatars affect speech perception

**Paper:** [Beat gestures made by human-like avatars affect speech perception](https://www.isca-archive.org/interspeech_2025/maran25_interspeech.html)
**Taxonomy:** `meaning-and-interaction / grounding-and-action / interactional-feedback`
**Evidence:** D3 full-paper capture; PDF SHA-256 `e1c746cb466631956d675031eeb37141ed4c5dd21a1633d3ffa7709fe14f5432`; full-text SHA-256 `92b7b2552aae5f8e2e6186efbf2965c43719ba40f19dfc7a06f4902ffc857199`.

- **Ordinary problem:** A human-like avatar's beat gesture can change how listeners understand or attend to speech, so gesture is part of the communicative signal rather than decoration.
- **Why it is hard:** Perception combines timing, visual form, speech content, and expectations about an avatar; a gesture can help one phrase and distract in another.
- **Naive attempt:** Add random gestures or assume a visually human avatar automatically improves speech perception.
- **Central move:** Manipulate beat gestures made by human-like avatars and measure their effect on speech perception under controlled conditions.
- **Mechanism:** The paper studies how beat gestures made by human-like avatars affect speech perception.
- **Mathematical idea:** Gesture functions as timed emphasis: its effect depends on alignment with prosodic or semantic structure, so perception experiments are needed instead of a visual-quality proxy.
- **What the paper reports:** The paper reports speech-perception effects of avatar beat gestures in the tested stimuli and listener tasks.
- **Limits:** Avatar design, gesture timing, speech material, participants, and task bound generalization; a laboratory effect is not proof of conversational benefit.

## 188. The mutual exclusivity bias of bilingual visually grounded speech models

**Paper:** [The mutual exclusivity bias of bilingual visually grounded speech models](https://www.isca-archive.org/interspeech_2025/oneata25_interspeech.html)
**Taxonomy:** `meaning-and-interaction / grounding-and-action / referential-grounding`
**Evidence:** D3 full-paper capture; PDF SHA-256 `0036e103e98c54f2172f53a65b42c4684caa8bf70a53c906c3eb1f27f6dfb011`; full-text SHA-256 `cb514f3836991acdecd08150ca03d38d1ecd8875cee6cff77432cee56936bdc0`.

- **Ordinary problem:** A bilingual listener may learn that a spoken word refers to one visible object, but a model trained across languages can develop a different bias about whether labels are shared or exclusive.
- **Why it is hard:** Visual grounding combines language, vision, and bilingual experience; correlations in a dataset can make a model prefer one interpretation without representing the underlying referent.
- **Naive attempt:** Measure only retrieval accuracy or assume a bilingual model follows human word-learning biases automatically.
- **Central move:** Test mutual-exclusivity behavior in bilingual visually grounded speech models using controlled novel-object and label situations.
- **Mechanism:** The paper studies mutual exclusivity bias in bilingual visually grounded speech models.
- **Mathematical idea:** The task probes how a model allocates a new label when familiar labels already exist; its choice reveals an interaction between language-specific priors and visual evidence.
- **What the paper reports:** The paper reports mutual-exclusivity behavior and cross-language differences for the tested bilingual grounded models.
- **Limits:** Languages, training data, object stimuli, model architecture, prompt/task design, and bias measure bound the claim; model behavior is not a direct account of child learning.

## 189. Towards High-Quality LLM-Based Data for French Spontaneous Speech Simplification: an Exo-Refinement Approach

**Paper:** [Towards High-Quality LLM-Based Data for French Spontaneous Speech Simplification: an Exo-Refinement Approach](https://www.isca-archive.org/interspeech_2025/ormaechea25_interspeech.html)
**Taxonomy:** `meaning-and-interaction / grounding-and-action / referential-grounding`
**Evidence:** D3 full-paper capture; PDF SHA-256 `214e4715b137832e91165306f3f34e1797e1fa51ab7489efa6df6d6ced3d18b8`; full-text SHA-256 `7a193bfd6fe93f1bb56f3574030e3ba2729695cfbf5e24d785f664bd121dbc3f`.

- **Ordinary problem:** A reader may need a simpler version of spontaneous speech, but parallel examples are scarce and a fluent rewrite can accidentally change what the speaker meant.
- **Why it is hard:** One model judging its own rewrite can approve its own semantic errors, while simplicity and meaning preservation pull in different directions.
- **Naive attempt:** Ask one generator to refine itself until the wording sounds simpler.
- **Central move:** Use separate external judges for task-specific dimensions and iterate only when their feedback improves simplicity without losing semantic content.
- **Mechanism:** LLM-generated French speech simplifications are refined by distinct evaluator models and compared with expert simplifications using SARI and COMET.
- **Mathematical idea:** The rewrite is constrained by two targets—simpler form and preserved meaning—so separate judges provide an outside check on the tradeoff.
- **What the paper reports:** Mistral-large outperforms tested baselines, Mistral-small becomes competitive after few refinements, SARI improves, and COMET indicates semantic preservation in the reported experiments.
- **Limits:** The languages, prompts, judges, reference simplifications, and automatic metrics bound the result; COMET and SARI are proxies, not a guarantee of accessible or faithful speech.

## 190. GenECA: A General-Purpose Framework for Real-Time Adaptive Multimodal Embodied Conversational Agents

**Paper:** [GenECA: A General-Purpose Framework for Real-Time Adaptive Multimodal Embodied Conversational Agents](https://www.isca-archive.org/interspeech_2025/patapati25_interspeech.html)
**Taxonomy:** `meaning-and-interaction / grounding-and-action / interactional-feedback`
**Evidence:** D3 full-paper capture; PDF SHA-256 `986327dab02e0ee3665356ac5a553c859d5d007ec880b85e91563aad5299e9de`; full-text SHA-256 `39e73a7ee6e39abed82dcba87132c3b43e53e5212bb8f62ec9d5c5f079d44202`.

- **Ordinary problem:** An embodied conversational agent should adapt its spoken response to what a person says, sees, and does while the interaction is happening.
- **Why it is hard:** Multimodal inputs arrive at different times and the agent must keep a coherent conversational state while meeting real-time limits.
- **Naive attempt:** Fuse all sensors once per turn or use a scripted avatar with fixed responses and call it adaptive.
- **Central move:** Build a general-purpose real-time multimodal embodied-agent framework that updates perception, dialogue, action, and speech together.
- **Mechanism:** GenECA is a framework for real-time adaptive multimodal embodied conversational agents.
- **Mathematical idea:** Embodied conversation is a closed loop: perception changes the state, the state selects language and action, and the agent's output changes the next observation.
- **What the paper reports:** The paper reports real-time adaptive-agent behavior across its tested multimodal interaction settings.
- **Limits:** Sensors, embodiment, latency, dialogue tasks, user studies, and policy constraints bound the claim; a framework demonstration is not human-level social understanding.

## 191. SNIFR : Boosting Fine-Grained Child Harmful Content Detection Through Audio-Visual Alignment with Cascaded Cross-Transformer

**Paper:** [SNIFR : Boosting Fine-Grained Child Harmful Content Detection Through Audio-Visual Alignment with Cascaded Cross-Transformer](https://www.isca-archive.org/interspeech_2025/phukan25f_interspeech.html)
**Taxonomy:** `meaning-and-interaction / grounding-and-action / referential-grounding`
**Evidence:** D3 full-paper capture; PDF SHA-256 `6fb92fb1d0324c48ccca29953b73f272f76ef54756d0d88c98a31079d22fbb53`; full-text SHA-256 `3fdbf22daef3949eb797738a802360f84afe83fad1fa234ceb4f015d7a2f1247`.

- **Ordinary problem:** A child-safety system should detect harmful content in audiovisual material at a fine-grained level, using both what is said and what is shown.
- **Why it is hard:** Harm can be conveyed by words, objects, actions, or their combination; audio and vision arrive asynchronously and errors have different safety costs.
- **Naive attempt:** Classify the whole clip from audio or vision alone, or use one coarse harmful/not-harmful label.
- **Central move:** Align audio and visual evidence with cascaded cross-transformers and predict fine-grained child-harm categories in real time.
- **Mechanism:** SNIFR boosts fine-grained child harmful-content detection through audio-visual alignment with cascaded cross-transformers.
- **Mathematical idea:** Safety understanding is multimodal grounding: the system must connect a specific spoken or visible event to a category and preserve timing for intervention.
- **What the paper reports:** The paper reports fine-grained audiovisual detection and real-time behavior for the tested harmful-content data.
- **Limits:** Labels, age policy, modalities, cultures, false-positive costs, and latency bound the result; an automated detector is not a safeguarding decision-maker.

## 192. Who Gets the Mic? Investigating Gender Bias in the Speaker Assignment of a Speech-LLM

**Paper:** [Who Gets the Mic? Investigating Gender Bias in the Speaker Assignment of a Speech-LLM](https://www.isca-archive.org/interspeech_2025/puhach25_interspeech.html)
**Taxonomy:** `meaning-and-interaction / grounding-and-action / interactional-feedback`
**Evidence:** D3 full-paper capture; PDF SHA-256 `f70875a4d05f6d9cf02ff2c70483f142a534d29918c14e38a843ccf2aa515122`; full-text SHA-256 `e00e7884bd6b9d514162ebb04324da0404dba6fc98d77a6b02d6be79d51e8da6`.

- **Ordinary problem:** A speech model that chooses a voice can reveal social associations even when text does not request gender.
- **Why it is hard:** Speech generation makes an implicit association audible through selected speaker identity.
- **Naive attempt:** Evaluate TTS only for naturalness and intelligibility.
- **Central move:** Probe default speaker assignment with controlled profession and gender-colored-word prompts.
- **Mechanism:** Bark is prompted with two constructed datasets and assignments are counted for gender alignment and inclinations.
- **Mathematical idea:** The controlled assignment counts are an association probe, not population prevalence or a human perception study.
- **What the paper reports:** Bark shows gender awareness and some inclinations but no strong systematic bias under the tested prompts.
- **Limits:** Two datasets, one model, prompt wording, and supported voices bound the conclusion; this is not a fairness guarantee.

## 193. Enhancing Speech Instruction Understanding and Disambiguation in Robotics via Speech Prosody

**Paper:** [Enhancing Speech Instruction Understanding and Disambiguation in Robotics via Speech Prosody](https://www.isca-archive.org/interspeech_2025/sasu25b_interspeech.html)
**Taxonomy:** `meaning-and-interaction / grounding-and-action / speech-act`
**Evidence:** D3 full-paper capture; PDF SHA-256 `64216ffe7765b03bd814c0f58520e206b52d0df912e8a3488d2b5e93c880911e`; full-text SHA-256 `3fe354690118b75cd97a34ed76c63516f00380cd3b3edbfbed425c9fe64ef547`.

- **Ordinary problem:** A robot can hear the same words but need different physical plans depending on which object or relation the speaker emphasizes.
- **Why it is hard:** ASR preserves much of the lexical content but discards stress, rhythm, pauses, and intonation that distinguish competing interpretations.
- **Naive attempt:** Transcribe the instruction, parse the text, and let a language model choose a plan from the words alone.
- **Central move:** Predict token-level goal/detail referents from prosody, then inject those intent cues into an LLM that selects the robot task plan.
- **Mechanism:** Prosodic and raw-audio features feed Transformer or BiLSTM sequence models trained with cross-entropy; predicted referents are placed in prompts for GPT-4o, o1-mini, or o3-mini to choose among plans.
- **Mathematical idea:** The sequence model estimates a label distribution for each token; accuracy, precision, recall, and F1 measure referent detection, while plan accuracy measures the final discrete action choice.
- **What the paper reports:** On 1,540 recordings from 22 participants, the best BiLSTM reaches 95.79% overall referent accuracy, and Prosody-Transformer plus GPT-4o reaches 71.96% task-plan accuracy versus 50% for the ASR-only prompt.
- **Limits:** The dataset is small and participants are 18–22; recorded ambiguity and candidate plans are controlled rather than open-world robot interaction. Prosody helps the tested task but does not establish safe execution in physical environments.

## 194. Spoken Question Answering for Visual Queries

**Paper:** [Spoken Question Answering for Visual Queries](https://www.isca-archive.org/interspeech_2025/shabtay25_interspeech.html)
**Taxonomy:** `meaning-and-interaction / grounding-and-action / referential-grounding`
**Evidence:** D3 full-paper capture; PDF SHA-256 `c836bb90b78d83905ab1062c34681d57abb38f2682fa7381a0c6a926cc13186b`; full-text SHA-256 `4a079eb7d4f0fbecc2f758e002c5532f32dd8ffbf955259a75137f4436611898`.

- **Ordinary problem:** A person wants to ask about an image using speech, while the answer must depend on what is visible rather than on the words alone.
- **Why it is hard:** Speech must be mapped to language while the image supplies the referent; an ASR error can change the question before the visual model sees it.
- **Naive attempt:** Transcribe the question first and hand the text to a text-only visual QA system, assuming speech contains no useful information beyond words.
- **Central move:** Align speech and image encoders directly into a VQA language model so spoken queries and visual evidence can jointly condition the answer.
- **Mechanism:** Whisper encodes speech and CLIP encodes images; modality-specific projectors align both representations with LLaVA's language space, with speech-only pretraining followed by joint spoken-VQA fine-tuning.
- **Mathematical idea:** The model predicts an answer from a fused representation. Accuracy, ANLS, and MME scores compare the answer with the task-specific reference; WER separately exposes speech-to-text failure.
- **What the paper reports:** Synthetic speech training approaches the text-trained VQA upper bound on several benchmarks; the paper reports 62% SEED-Bench accuracy for its strongest spoken variants, with TTS choice having a small effect.
- **Limits:** Most training speech is synthesized, the spoken models remain below the text model, prompt format changes performance sharply, and transcription failures can be confused with visual-reasoning failures. No independent reproduction was performed.

## 195. Discrete Audio Representations for Automated Audio Captioning

**Paper:** [Discrete Audio Representations for Automated Audio Captioning](https://www.isca-archive.org/interspeech_2025/tian25_interspeech.html)
**Taxonomy:** `meaning-and-interaction / grounding-and-action / referential-grounding`
**Evidence:** D3 full-paper capture; PDF SHA-256 `f9ad0922ba37c8533490d85982fa17b0062f5bdaa44ef7aecc883ad9191685b9`; full-text SHA-256 `9936b69e217f2130784b029e5dc0bab9b913b7a3f5c8712ccdea415032913f7e`.

- **Ordinary problem:** An audio captioner must preserve sound events in a compact representation while giving a language decoder enough evidence to describe them.
- **Why it is hard:** Audio contains simultaneous events and fine timing, but a caption model must compress it before generating variable-length language.
- **Naive attempt:** Use one continuous embedding or a generic tokenizer and assume reconstruction preserves whatever captioning needs.
- **Central move:** Compare discrete audio representations for caption generation and test whether tokenization retains semantic evidence.
- **Mechanism:** Encode audio into learned discrete tokens, condition a text decoder on those tokens, and compare tokenizers and decoder choices on caption metrics.
- **Mathematical idea:** Quantization creates a finite vocabulary of acoustic units; the central question is whether the units preserve event identity rather than merely waveform detail.
- **What the paper reports:** The paper reports that selected audio tokenizers improve automated captioning quality, showing that representation design affects semantic generation.
- **Limits:** Reference-caption incompleteness, metric proxy limits, dataset scope, and no broad human grounding study limit conclusions about listener usefulness.

## 196. Investigating the Reasoning Abilities of Large Language Models for Understanding Spoken Language in Interpersonal Interactions

**Paper:** [Investigating the Reasoning Abilities of Large Language Models for Understanding Spoken Language in Interpersonal Interactions](https://www.isca-archive.org/interspeech_2025/aggarwal25_interspeech.html)
**Taxonomy:** `meaning-and-interaction / intent-and-dialogue-state / intent-in-context`
**Evidence:** D3 full-paper capture; PDF SHA-256 `379dfe0c14c98a674362c1e38020aa556e52d6d32de7d5d20849c15ad992a6e2`; full-text SHA-256 `109dec4ea31dbf1281a944863b37a9a3e8a81a136425d8107446440e3bc720c5`.

- **Ordinary problem:** An interview coach must judge whether a spoken answer addresses the interpersonal question, not merely whether its words are grammatical.
- **Why it is hard:** Interview answers depend on context, social intent, turn history, and domain knowledge that surface lexical matching misses.
- **Naive attempt:** Ask a general language model to answer from the transcript alone and treat fluent text as understanding.
- **Central move:** Evaluate large language models on spoken-interaction reasoning with explicit contextual knowledge and prompt structure.
- **Mechanism:** Supply interview context and domain knowledge, compare prompting strategies and model scales, and score both answer quality and reasoning behavior.
- **Mathematical idea:** Prompt conditions act as information controls: context and domain knowledge reduce ambiguity, while ablations reveal which information supports the decision.
- **What the paper reports:** The paper reports that contextual and domain-knowledge prompting improves selected spoken-interaction reasoning settings, especially for larger models.
- **Limits:** Interview distribution, transcript quality, subjective scoring, prompt sensitivity, and model-family coverage limit claims about general conversational understanding.

## 197. Spoken Language Understanding on Unseen Tasks With In-Context Learning

**Paper:** [Spoken Language Understanding on Unseen Tasks With In-Context Learning](https://www.isca-archive.org/interspeech_2025/agrawal25_interspeech.html)
**Taxonomy:** `meaning-and-interaction / intent-and-dialogue-state / intent-in-context`
**Evidence:** D3 full-paper capture; PDF SHA-256 `e1b0ce18d9d00ca22245e6a421a4177d2b9673c34cd8191ebb8ca5280d681eb1`; full-text SHA-256 `ceb071c2547b85bb56a567b8ed572728402dd06be51acf889b17961269523526`.

- **Ordinary problem:** Make a speech-text LLM perform spoken-language-understanding tasks it did not see during task-specific training.
- **Why it is hard:** Cascaded ASR plus text understanding compounds errors, while task-specific SLU labels are expensive and unseen label sets break ordinary fine-tuning.
- **Naive attempt:** Fine-tune directly on task labels and assume the same labels will exist at evaluation time.
- **Central move:** Use symbol-based and randomized-label fine-tuning with a SALMONN speech-text model to reduce dependence on task-specific label semantics.
- **Mechanism:** The model maps speech and demonstrations to symbolic targets, then is evaluated in matched and mismatched task settings with zero/few-shot context.
- **Mathematical idea:** The central object is a label permutation: performance tests whether the model learned task structure rather than memorized label names.
- **What the paper reports:** The paper reports improved unseen-task performance over standard approaches in its three-task evaluation.
- **Limits:** Fine-tuning used batch size one and the task/model/data setup is narrower than general spoken reasoning.

## 198. Chain-of-Thought Training for Open E2E Spoken Dialogue Systems

**Paper:** [Chain-of-Thought Training for Open E2E Spoken Dialogue Systems](https://www.isca-archive.org/interspeech_2025/arora25_interspeech.html)
**Taxonomy:** `meaning-and-interaction / intent-and-dialogue-state / dialogue-state`
**Evidence:** D3 full-paper capture; PDF SHA-256 `7493db7039715522ae42bc0ac609ad77d48da10b8c9d936aea89b762afc1cce7`; full-text SHA-256 `a5e7ab222c89f2bacc1951258940136f51374f945e1bc621c0cdd881bbc74a20`.

- **Ordinary problem:** Make a spoken dialogue system choose a useful response when the user's words, intent, and conversational state must be handled together.
- **Why it is hard:** A transcript-to-response model can produce a fluent answer while losing non-phonemic cues, task state, or the intermediate decision needed to act correctly.
- **Naive attempt:** Train only on final responses and judge success from response text without exposing how the system interpreted the turn.
- **Central move:** Train an end-to-end spoken dialogue model with intermediate reasoning or planning traces so acoustic and conversational evidence can influence the response.
- **Mechanism:** Speech is encoded into a shared representation, the model predicts intermediate dialogue reasoning, and a decoder produces the next response; ablations compare direct response training with the added supervision.
- **Mathematical idea:** The training objective sums token-level losses over intermediate and final sequences; task success and response quality test whether extra structure improves the intended action rather than only wording.
- **What the paper reports:** The paper reports improvements for open end-to-end spoken dialogue modeling from chain-of-thought training and evaluates the resulting response behavior.
- **Limits:** Reasoning traces are supervision artifacts and do not prove faithful internal reasoning; task distribution, annotation quality, and evaluation subjectivity constrain the claim. No independent reproduction was performed.

## 199. Analysis of ABC Frontend Audio Systems for the NIST-SRE24

**Paper:** [Analysis of ABC Frontend Audio Systems for the NIST-SRE24](https://www.isca-archive.org/interspeech_2025/barahona25_interspeech.html)
**Taxonomy:** `meaning-and-interaction / intent-and-dialogue-state / dialogue-state`
**Evidence:** D3 full-paper capture; PDF SHA-256 `cf760325e19e2f71107224591b5f91b2602db58ef9c2ed548c860168c374e915`; full-text SHA-256 `d1d99ab6d9923ae85fa24ed3046cd4726f939007674fb8d6245eabdf4cd6fa34`.

- **Ordinary problem:** Speaker embeddings for conversational telephone speech need to work across speakers and languages under a fixed or open training-data rule.
- **Why it is hard:** Frontend architecture, pooling, pretraining, and training data all change the speaker geometry; a benchmark comparison can hide which component caused an improvement.
- **Naive attempt:** Choose one embedding architecture or use a large pretrained model without separating data condition, pooling, and domain effects.
- **Central move:** Analyze several frontend families and pooling choices under the NIST SRE24 fixed and open conditions, including multilingual training data.
- **Mechanism:** The paper analyzes ABC frontend audio systems for the NIST SRE24 audio track.
- **Mathematical idea:** The frontend is a measurement pipeline: representation, temporal pooling, training population, and domain match jointly determine whether identity survives telephone speech.
- **What the paper reports:** The paper reports comparative robustness and performance for the explored architectures and data conditions.
- **Limits:** NIST protocol, telephone channel, language mix, training-data access, and calibration limit claims beyond the benchmark.

## 200. Multimodal Fusion with Semi-Supervised Learning Minimizes Annotation Quantity for Modeling Videoconference Conversation Experience

**Paper:** [Multimodal Fusion with Semi-Supervised Learning Minimizes Annotation Quantity for Modeling Videoconference Conversation Experience](https://www.isca-archive.org/interspeech_2025/chang25c_interspeech.html)
**Taxonomy:** `meaning-and-interaction / intent-and-dialogue-state / dialogue-state`
**Evidence:** D3 full-paper capture; PDF SHA-256 `bb03bf4cb4f308acc50c3ff70f8c08a1c04c806a41e361de55376c8b29433cd2`; full-text SHA-256 `00086779092eb328bdc9bbbf0a075c13c2f5d55f3e1a1d8089baaffc2b07d787`.

- **Ordinary problem:** A videoconference system should detect moments when a group conversation becomes awkward or stops feeling enjoyable.
- **Why it is hard:** The moments are rare and expensive to label, and the signal is distributed across voice, face, and words.
- **Naive attempt:** Train a fully supervised multimodal model and label every clip.
- **Central move:** Use a small labeled set to teach a model from a larger targeted unlabeled set through semi-supervised co-training.
- **Mechanism:** Audio, facial-action, and text features are fused; modality-specific learners exchange pseudo-label information while the model is tested on held-out sessions.
- **Mathematical idea:** Co-training uses agreement between views to expand supervision; ROC-AUC measures ranking of rare events while F1 measures the chosen decision threshold.
- **What the paper reports:** The paper reports ROC-AUC .90 and F1 .60, and says 8% labeled data reaches 96% of the full supervised model's performance.
- **Limits:** The labels, videoconference setting, participant population, and definition of negative experience bound the result; detection is not a causal explanation of why a conversation deteriorated.

## 201. Medusa: A Multimodal Deep Fusion Multi-Stage Training Framework for Speech Emotion Recognition in Naturalistic Conditions

**Paper:** [Medusa: A Multimodal Deep Fusion Multi-Stage Training Framework for Speech Emotion Recognition in Naturalistic Conditions](https://www.isca-archive.org/interspeech_2025/chatzichristodoulou25_interspeech.html)
**Taxonomy:** `meaning-and-interaction / intent-and-dialogue-state / intent-in-context`
**Evidence:** D3 full-paper capture; PDF SHA-256 `e76958593c99a4b21afbb23f9bdad9c93e76ebf46f8b8a66c1c639d0325cd9d2`; full-text SHA-256 `c6d38b2b7213671eb8448b7dfdd58dceba38d6a94abdf54c2d65f7e0ecff3f6e`.

- **Ordinary problem:** Emotion recognition should reflect ambiguous human judgments in natural recordings rather than force every clip into one certain label.
- **Why it is hard:** Emotions are subjective, classes are imbalanced, and speech and language cues interact.
- **Naive attempt:** Train one classifier on hard one-hot labels and sample classes uniformly only after training.
- **Central move:** Use cross-modal representation fusion, soft human annotation targets, balanced sampling, multitask learning, and a meta-classifier in stages.
- **Mechanism:** MEDUSA builds an ensemble from self-supervised acoustic and linguistic representations, uses Manifold MixUp, and combines predictions with a trainable meta-classifier.
- **Mathematical idea:** Soft targets preserve disagreement; balanced sampling changes which examples influence learning; the meta-classifier learns when component predictions should be trusted.
- **What the paper reports:** MEDUSA ranked first in the naturalistic categorical emotion challenge task reported by the paper.
- **Limits:** Challenge splits, annotation distributions, modalities, and ranking define the result; a leaderboard position does not establish emotion truth or cross-cultural validity.

## 202. MMLoRA: Multitask Memory Parameter-Efficient Fine-Tuning for Multimodal SER

**Paper:** [MMLoRA: Multitask Memory Parameter-Efficient Fine-Tuning for Multimodal SER](https://www.isca-archive.org/interspeech_2025/fang25_interspeech.html)
**Taxonomy:** `meaning-and-interaction / intent-and-dialogue-state / dialogue-state`
**Evidence:** D3 full-paper capture; PDF SHA-256 `30cc30ac8f29663f4e76529b9ba2f9d15abaa2c50ba9416bbf7e45c4119a160a`; full-text SHA-256 `04ff228fd0a73b671fbb7c4bdae5690c997343758d521798079d1d337bdfaf66`.

- **Ordinary problem:** Emotion recognition should generalize when people express the same emotion differently, across audio and other modalities and across related tasks.
- **Why it is hard:** Individual expression varies with speaker, gender, context, and modality; a parameter-efficient update can share too little or force unrelated tasks together.
- **Naive attempt:** Use one shared LoRA update or train a separate full model for every emotion task.
- **Central move:** Combine shared LoRA experts, task-specific experts, a memory mechanism, and gender as an auxiliary task to separate common structure from expression-specific variation.
- **Mechanism:** MMLoRA is a multitask memory parameter-efficient method for multimodal speech emotion recognition.
- **Mathematical idea:** The adaptation has two roles: shared parameters carry reusable affective structure, while expert and memory paths preserve task/person-specific differences instead of overwriting them.
- **What the paper reports:** The paper reports improved multimodal SER generalization over the tested parameter-efficient baselines.
- **Limits:** Datasets, gender labels, task mix, memory policy, modalities, and expression cultures bound the result; auxiliary gender is not a complete model of individual variation.

## 203. Comparison-Based Automatic Evaluation for Meeting Summarization

**Paper:** [Comparison-Based Automatic Evaluation for Meeting Summarization](https://www.isca-archive.org/interspeech_2025/gong25c_interspeech.html)
**Taxonomy:** `meaning-and-interaction / intent-and-dialogue-state / dialogue-state`
**Evidence:** D3 full-paper capture; PDF SHA-256 `7564415e510871fda9e1217dc49c8edd4176da76020fb95b2ffde3d57c94cb83`; full-text SHA-256 `0a35e045b71d71fb052e616b3ae884199bf1d35ecd0018dd0fed66bd3d561b4a`.

- **Ordinary problem:** A meeting summarizer should be judged for preserving important facts and staying concise even when no reference summary exists.
- **Why it is hard:** Long meetings contain many valid summaries, and reference overlap rewards wording rather than whether the important decisions survived.
- **Naive attempt:** Compare generated text with one reference using lexical similarity or ask an LLM for one unstructured score.
- **Central move:** Use fact alignment and comparison-based judging, then rank systems with an Elo procedure instead of requiring a reference summary.
- **Mechanism:** CREAM uses reasoning traces and key-fact alignment to compare meeting summaries for completeness and conciseness without references.
- **Mathematical idea:** Fact coverage and brevity become comparison evidence; Elo aggregates pairwise preferences while avoiding a false absolute scale.
- **What the paper reports:** The paper presents a reference-free evaluation framework for meeting summarization and reports its ability to rank systems/prompts.
- **Limits:** Facts, judge prompts, meeting domain, and pairwise comparison protocol bound the result; human validation and adversarial summaries remain open.

## 204. Leveraging LLMs for Written to Spoken Style Data Transformation to Enhance Spoken Dialog State Tracking

**Paper:** [Leveraging LLMs for Written to Spoken Style Data Transformation to Enhance Spoken Dialog State Tracking](https://www.isca-archive.org/interspeech_2025/gulzar25_interspeech.html)
**Taxonomy:** `meaning-and-interaction / intent-and-dialogue-state / dialogue-state`
**Evidence:** D3 full-paper capture; PDF SHA-256 `adc9d9d9de2a318d2ae17ed99841467cfa25210f33b906fadff5b60f82cb023e`; full-text SHA-256 `e07a09000aa68ea8a1634cd27e042725a52835a69e9879d6e6d70efe02e6179b`.

- **Ordinary problem:** Spoken dialogue state tracking needs training data that sounds like spoken interaction, not only written dialogue that has been read aloud.
- **Why it is hard:** Written and spoken styles differ in disfluency, brevity, repair, and turn structure; an LLM rewrite can add plausible language while changing the dialogue-state labels.
- **Naive attempt:** Use written dialogue directly or generate paraphrases without checking whether the state remains unchanged.
- **Central move:** Use an LLM to transform written dialogue into spoken style while preserving state annotations, then test the resulting data for spoken dialogue-state tracking.
- **Mechanism:** The paper leverages LLMs for written-to-spoken style transformation to enhance spoken dialogue-state tracking.
- **Mathematical idea:** The transformation is constrained paraphrasing: surface form changes, but the underlying user goal and slot state must remain invariant for the data to be useful.
- **What the paper reports:** The paper reports spoken dialogue-state-tracking gains from the transformed data.
- **Limits:** LLM prompt, domains, state schema, speech realization, annotation checks, and evaluation distribution limit the result; style conversion can silently change intent.

## 205. Factors affecting the in-context learning abilities of LLMs for dialogue state tracking

**Paper:** [Factors affecting the in-context learning abilities of LLMs for dialogue state tracking](https://www.isca-archive.org/interspeech_2025/hegde25_interspeech.html)
**Taxonomy:** `meaning-and-interaction / intent-and-dialogue-state / dialogue-state`
**Evidence:** D3 full-paper capture; PDF SHA-256 `adbf75997fe61e0dcccb324b8b4a83759abd5e33edf5615fbc9d288512a07dbd`; full-text SHA-256 `760d5cb0e991e36b417c6fdcec2163807d797647023c7ccf10d37a37d565060d`.

- **Ordinary problem:** A dialogue-state tracker should use examples in context effectively, but its ability to learn from a few demonstrations may depend on how the dialogue and prompts are arranged.
- **Why it is hard:** State labels, turn order, domain vocabulary, and example selection can change what the model appears to infer from context.
- **Naive attempt:** Measure one prompt format and attribute the result to general in-context learning ability.
- **Central move:** Systematically vary dialogue-state-tracking factors such as demonstrations, domain, and context to identify which conditions support or break in-context learning.
- **Mechanism:** The paper studies factors affecting the in-context learning abilities of LLMs for dialogue state tracking.
- **Mathematical idea:** In-context learning is an interaction between model prior and task presentation: the examples are part of the effective program and must be analyzed as such.
- **What the paper reports:** The paper reports factor-level findings on in-context dialogue-state tracking.
- **Limits:** Model family, prompt, domains, state schema, demonstration order, and context length bound the result; prompt sensitivity is not a stable conversational capability.

## 206. Modeling Multi-Turn Spoken Language Understanding with Dynamic Graph Convolutional Networks

**Paper:** [Modeling Multi-Turn Spoken Language Understanding with Dynamic Graph Convolutional Networks](https://www.isca-archive.org/interspeech_2025/huang25d_interspeech.html)
**Taxonomy:** `meaning-and-interaction / intent-and-dialogue-state / dialogue-state`
**Evidence:** D3 full-paper capture; PDF SHA-256 `3ef4b80202725edd11373dc60b856aa79e736cca9e8cfb2775007e65c4cf9779`; full-text SHA-256 `3cda2608dd880c99ec793bf53aae385b3e442a6f9a5121ea1fbf84fef4dfecc9`.

- **Ordinary problem:** A spoken dialogue tracker must use information across several turns, including references and corrections, rather than treating each utterance as a fresh request.
- **Why it is hard:** State is distributed over a conversation and graph relations change as entities are introduced, resolved, and revised.
- **Naive attempt:** Classify each turn independently or concatenate all text and hope a generic sequence model preserves the relevant relations.
- **Central move:** Represent multi-turn spoken-language understanding with dynamic graph convolution so entities and dialogue relations update over time.
- **Mechanism:** The paper models multi-turn spoken-language understanding with dynamic graph convolutional networks.
- **Mathematical idea:** Dialogue state is a changing relational structure: the graph makes explicit which words, entities, and turns constrain the current interpretation.
- **What the paper reports:** The paper reports multi-turn spoken-language-understanding results for the dynamic graph model.
- **Limits:** Domains, ASR errors, graph construction, turn length, labels, and evaluation split bound the result; a graph state is not complete conversational memory.

## 207. Dialogue Response Prefetching Based on Semantic Similarity and Prediction Confidence of Language Model

**Paper:** [Dialogue Response Prefetching Based on Semantic Similarity and Prediction Confidence of Language Model](https://www.isca-archive.org/interspeech_2025/mori25b_interspeech.html)
**Taxonomy:** `meaning-and-interaction / intent-and-dialogue-state / dialogue-state`
**Evidence:** D3 full-paper capture; PDF SHA-256 `33706d6c9e52b1da5ade1bedbf2ddc81c95c429bd833abd9f2c5df628d5833df`; full-text SHA-256 `294842f0baa255cf6d70c2d38aca29be382a0732a9633d8354edc4ab2cda98d8`.

- **Ordinary problem:** A spoken dialogue system can prepare a response before the user finishes, but a wrong early prediction can waste computation or create a visibly incorrect reply.
- **Why it is hard:** The partial utterance is incomplete and ambiguous; latency savings matter only when the predicted completion is semantically close enough to the final utterance.
- **Naive attempt:** Always prefetch from the current partial transcript or never prefetch until the user stops speaking.
- **Central move:** Predict the complete utterance early, estimate semantic similarity and confidence between the prediction and eventual utterance, and prefetch only when the confidence threshold makes the latency/rollback trade-off worthwhile.
- **Mechanism:** A prediction-confidence model compares embeddings or semantic representations of the predicted and completed user utterances; response latency and prediction correctness quantify when prefetching is safe.
- **Mathematical idea:** The decision is selective rather than binary: the system estimates expected utility under uncertainty, trading saved user-perceived latency against wrong-response risk.
- **What the paper reports:** The paper reports that semantic-similarity confidence can reduce user-perceived latency while limiting unsafe prefetches in the tested spoken-dialogue setting.
- **Limits:** The language model, dialogue domain, confidence calibration, and endpointing assumptions constrain generalization; lower latency is not the same as better conversation or human trust.

## 208. Assessing the feasibility of Large Language Models for detecting micro-behaviors in team interactions during space missions

**Paper:** [Assessing the feasibility of Large Language Models for detecting micro-behaviors in team interactions during space missions](https://www.isca-archive.org/interspeech_2025/raut25_interspeech.html)
**Taxonomy:** `meaning-and-interaction / intent-and-dialogue-state / dialogue-state`
**Evidence:** D3 full-paper capture; PDF SHA-256 `a3b81ba0f325aa9c338caf18c6c6b58284784008dbd50975513bc23b4947f05b`; full-text SHA-256 `c0789df1352d64004d12ff1114fcfd94bbcf9299b2bfbdd16ef3db8434f37dde`.

- **Ordinary problem:** Team communication contains small conversational behaviors that may signal coordination or trouble, but they are rare and their meaning depends on the turn around them.
- **Why it is hard:** Underrepresented behaviors are easy for a classifier to ignore, and transcripts omit timing, voice quality, and other cues present in audio.
- **Naive attempt:** Fine-tune a text classifier and assume more weighting will recover every rare behavior.
- **Central move:** Compare zero-shot, fine-tuned, paraphrase-augmented, and instruction-following models while keeping the turn as the unit of dialogue-state prediction.
- **Mechanism:** Models classify micro-behaviors in transcripts from simulated space missions, including discouraging speech, under three-way and binary labelings.
- **Mathematical idea:** Macro F1 exposes minority-class failure better than accuracy; the task tests whether language context alone can support interactional labeling.
- **What the paper reports:** Encoder-only models struggle with rare behaviors, while an instruction-tuned Llama model reports 44% macro F1 for three-way and 68% for binary classification.
- **Limits:** Simulated missions, transcript quality, label prevalence, model prompting, and macro-F1 targets bound the finding; detected text patterns are not proof of team state or causality.

## 209. Robot-assisted Recognition of Vocal Emotions in Pseudospeech for Cochlear Implanted Adolescents

**Paper:** [Robot-assisted Recognition of Vocal Emotions in Pseudospeech for Cochlear Implanted Adolescents](https://www.isca-archive.org/interspeech_2025/araizaillan25_interspeech.html)
**Taxonomy:** `meaning-and-interaction / prosody-and-paralinguistics / paralinguistic-state`
**Evidence:** D3 full-paper capture; PDF SHA-256 `cbd8dd677e17cdda5e2d152c1651e137c43e2619e6bd06c08e516646a587e3f1`; full-text SHA-256 `57d15c84aa326a4e1d3899dfcebb8d425bd1a990fde36bcf013038c58a88ced9`.

- **Ordinary problem:** A hearing test for adolescents with cochlear implants should measure vocal-emotion perception in an interface they can tolerate and engage with.
- **Why it is hard:** Pseudospeech removes linguistic emotion clues, while interface burden can affect participation and test time.
- **Naive attempt:** Use a computer-only test and treat usability as separate from measurement validity.
- **Central move:** Compare a robot and computer interface on the same emotion task, including sensitivity, duration, and participant preference.
- **Mechanism:** Adolescents aged 10–17 complete EmoHI pseudospeech emotion tests with a computer and NAO robot; d-prime, duration, and usability are measured.
- **Mathematical idea:** Sensitivity, test duration, and perceived usability/enjoyment expose the tradeoff between measurement equivalence and engagement.
- **What the paper reports:** Sensitivity is similar (.36 versus .37); the robot takes longer, is less usable, but is more enjoyable and engaging.
- **Limits:** The participants, robot, pseudospeech task, and small sample bound the result; long-term adherence and general hearing-device populations remain open.

## 210. Coping with segmental–prosodic incongruity in spoken word recognition in Japanese

**Paper:** [Coping with segmental–prosodic incongruity in spoken word recognition in Japanese](https://www.isca-archive.org/interspeech_2025/ariga25_interspeech.html)
**Taxonomy:** `meaning-and-interaction / prosody-and-paralinguistics / prosodic-meaning`
**Evidence:** D3 full-paper capture; PDF SHA-256 `10247574502e1b6779b7e9a37aaf76aa976fc717897595425bc8cd727a142bcc`; full-text SHA-256 `ceac8193c6a9684928cf1239b7877f05869b73c00ef6cf4e8d6e4e5bd4f98622`.

- **Ordinary problem:** Listeners combine segmental sounds and lexical pitch accent when recognizing Japanese words, even when the cues disagree.
- **Why it is hard:** The cues arrive together, priming can mask later effects, and response time does not by itself identify the updated representation.
- **Naive attempt:** Treat phonemes as the only lexical evidence or assume prosody simply overrides segments.
- **Central move:** Create controlled incongruent words and use repetition priming and response timing to test each cue.
- **Mechanism:** Experiments isolate cue type, delay, and lexical repetition; mixed-effects models compare segmental and prosodic conditions.
- **Mathematical idea:** Response-time models compare conditions; the paper reports prosodic inhibition at a 750 ms interval.
- **What the paper reports:** Results suggest prosodic mispronunciation inhibits recognition at the tested delay.
- **Limits:** Japanese materials, pitch-accent system, participants, and laboratory task limit cross-language generalization.

## 211. Stress in Spoken and Whistled Greek

**Paper:** [Stress in Spoken and Whistled Greek](https://www.isca-archive.org/interspeech_2025/batchelderschwab25_interspeech.html)
**Taxonomy:** `meaning-and-interaction / prosody-and-paralinguistics / prosodic-meaning`
**Evidence:** D3 full-paper capture; PDF SHA-256 `3fee5276099baae69eb179f0e66cd303040d9514ac2d865d1147887ea09efbef`; full-text SHA-256 `03dee47efd812b98602c1a80dcae24d858e5533de28183fd9ffc64e566c3a2fa`.

- **Ordinary problem:** A community can communicate by whistling, so a listener must know how spoken vowel and stress distinctions survive when the sound source changes.
- **Why it is hard:** Whistling removes many speech cues and concentrates information in pitch and intensity, so a spoken-language assumption may misidentify what remains contrastive.
- **Naive attempt:** Assume every spoken vowel and stress cue must have the same acoustic realization in the whistle register.
- **Central move:** Compare matched minimal pairs in spoken and whistled Greek and identify which vowel and stress contrasts are carried by F0, intensity, or neither.
- **Mechanism:** Participants produce five Greek vowel qualities in Sfyria whistling and spoken Greek; acoustic contrasts are compared for stressed and unstressed forms.
- **Mathematical idea:** The representation changes with the communication channel: F0 and intensity are alternative carriers of phonological contrast, and a missing cue is itself evidence.
- **What the paper reports:** All five vowel qualities remain distinct in the whistled register, but a whistled stress correlate is not found for /i/, possibly because front vowels are already highly intense.
- **Limits:** The Sfyria community, participants, register, minimal pairs, and acoustic cues bound the result; a ceiling interpretation and cross-language generalization remain open.

## 212. Heart Rate as a Proxy Measure to Assess Human Confidence in Spoken Speech

**Paper:** [Heart Rate as a Proxy Measure to Assess Human Confidence in Spoken Speech](https://www.isca-archive.org/interspeech_2025/battula25_interspeech.html)
**Taxonomy:** `meaning-and-interaction / prosody-and-paralinguistics / paralinguistic-state`
**Evidence:** D3 full-paper capture; PDF SHA-256 `3bb63c026964e22d9e42ffc309f61e6c0ac8bde4c5ea12e07bfea8b728a5af85`; full-text SHA-256 `c58d6d8a2d91db1a74b2f4c50e3f3203eb3ccbee3a2254e81b93c3dce270ac7d`.

- **Ordinary problem:** A person’s confidence is useful to assess in an interview, but the relevant physiological signal is normally hard to collect without a sensor.
- **Why it is hard:** The proposed chain estimates breathing from speech, extracts heart-rate variation with ICA, and maps that estimate to confidence; each step can add error or reflect demographic and situational differences.
- **Naive attempt:** Treat confidence as a direct acoustic class or require a wearable heart-rate sensor for every interaction.
- **Central move:** Infer heart rate from speech-derived breathing patterns, then examine whether the inferred heart rate separates confident and non-confident speakers.
- **Mechanism:** The paper presents a three-stage speech-to-breathing-to-heart-rate approach for confidence analysis.
- **Mathematical idea:** The key conceptual move is indirect sensing: speech is used as a window onto a bodily rhythm, but the inferred physiology is not the same thing as confidence itself.
- **What the paper reports:** The paper reports that confident speakers had an average heart rate about 10 beats per minute lower in its tested data.
- **Limits:** The datasets, Indian demographic, 41-speaker collection, clinical and wearable references, confidence labels, and unreported general accuracy bound the claim; correlation is not a validated psychological diagnosis.

## 213. Multi-Teacher Language-Aware Knowledge Distillation for Multilingual Speech Emotion Recognition

**Paper:** [Multi-Teacher Language-Aware Knowledge Distillation for Multilingual Speech Emotion Recognition](https://www.isca-archive.org/interspeech_2025/bijoy25_interspeech.html)
**Taxonomy:** `meaning-and-interaction / prosody-and-paralinguistics / paralinguistic-state`
**Evidence:** D3 full-paper capture; PDF SHA-256 `391d0eaa6ca6738c4e242d83c5648787cac1db012609926cdacbc898c263e663`; full-text SHA-256 `10a89fd35c2436c7aae63e0ae7b8b149de84012e8966c54997e1d6075f7f37b5`.

- **Ordinary problem:** One emotion recognizer should serve several languages without letting the largest language erase smaller languages or their emotion patterns.
- **Why it is hard:** Languages differ in acoustic and linguistic cues, and one teacher model may be strong in one language but transfer the wrong priorities to another.
- **Naive attempt:** Train one multilingual model directly or average teacher predictions without identifying which language produced the speech.
- **Central move:** Use separate monolingual teachers and a language-aware distillation process to teach one student while preserving language-specific evidence.
- **Mechanism:** Wav2vec2 teachers for English, Finnish, and French are distilled into one multilingual student and evaluated by emotion recall per language and class.
- **Mathematical idea:** The student is a shared model with language-conditioned supervision; weighted and unweighted recall expose both overall performance and class imbalance.
- **What the paper reports:** The student reports weighted recall 72.9 on English and unweighted recall 63.4 on Finnish, with stronger gains for sad and neutral than anger and happiness.
- **Limits:** Languages, emotion labels, teacher quality, class balance, and recall metrics bound the claim; multilingual transfer does not prove equal performance or culturally valid emotion categories.

## 214. EmoDB 2.0: A Database of Emotional Speech in a World that is not Black or White but Grey

**Paper:** [EmoDB 2.0: A Database of Emotional Speech in a World that is not Black or White but Grey](https://www.isca-archive.org/interspeech_2025/burkhardt25_interspeech.html)
**Taxonomy:** `meaning-and-interaction / prosody-and-paralinguistics / prosodic-meaning`
**Evidence:** D3 full-paper capture; PDF SHA-256 `41aa00e673d7957c865344ff0dcc41a89d1de020b3a234a36d554baa3e6bf825`; full-text SHA-256 `6cfc81d78250fbe4d9671f4083245da7175bc083a8444658ccf37c03b4704293`.

- **Ordinary problem:** An emotion database becomes more useful when it preserves ambiguous judgments and records how natural the acted speech sounds, rather than discarding every item without strong agreement.
- **Why it is hard:** Emotion labels are perceptions with disagreement, and glottal behavior may contain information that ordinary audio features miss; a clean majority label can hide meaningful uncertainty.
- **Naive attempt:** Keep only samples with high rater agreement and treat one categorical emotion label as ground truth.
- **Central move:** Extend Berlin EmoDB with previously omitted ambiguous samples, glottograms, and perceived-naturalness labels, then test their value in preliminary classifiers.
- **Mechanism:** The paper extends the Berlin Database of Emotional Speech with ambiguity, glottograms, and naturalness information.
- **Mathematical idea:** Dataset construction is part of the scientific model: disagreement and phonation measurements expose how an emotion label is produced and where it is uncertain.
- **What the paper reports:** The paper reports an 8.1% UAR improvement for an SVM when glottogram information is incorporated in its preliminary study.
- **Limits:** The acted German corpus, old recording conditions, rater thresholds, classifier, and preliminary evaluation bound the result; improved classification does not establish better emotion understanding.

## 215. EmotionRankCLAP: Bridging Natural Language Speaking Styles and Ordinal Speech Emotion via Rank-N-Contrast

**Paper:** [EmotionRankCLAP: Bridging Natural Language Speaking Styles and Ordinal Speech Emotion via Rank-N-Contrast](https://www.isca-archive.org/interspeech_2025/chandra25_interspeech.html)
**Taxonomy:** `meaning-and-interaction / prosody-and-paralinguistics / prosodic-meaning`
**Evidence:** D3 full-paper capture; PDF SHA-256 `5a34fd5ea1236f670750d09bca0d36398e06570a95f42bd426f55f07066cc0c3`; full-text SHA-256 `3e6dfe40eb339a72a5d1b3d2b548704cbffdd8ab525206d3596945ffff9874b3`.

- **Ordinary problem:** Emotion is ordered: a voice can be more or less excited or positive, but ordinary audio-text contrastive training treats labels as unrelated names.
- **Why it is hard:** Ignoring order loses gradual differences and leaves audio and language representations poorly aligned.
- **Naive attempt:** Pull each audio sample toward its text label while treating every other label as equally wrong.
- **Central move:** Use valence-arousal rankings in a Rank-N-Contrast objective so nearby and distant emotional examples exert different forces.
- **Mechanism:** EmotionRankCLAP aligns emotional speech with natural-language speaking-style prompts and contrasts examples according to their position in valence-arousal space.
- **Mathematical idea:** The loss encodes an ordering rather than only class identity; cross-modal retrieval tests whether the learned space preserves emotion relations.
- **What the paper reports:** The paper reports better emotion ordinality than existing emotion-CLAP systems on cross-modal retrieval.
- **Limits:** The result depends on rating dimensions, prompt wording, and the tested emotion corpus; listener disagreement and transfer across cultures remain open.

## 216. A-SMiLE: Affective Sparse Mixture-of-Experts Adapter with Multi-Task Learning for Spoken Dialogue Models

**Paper:** [A-SMiLE: Affective Sparse Mixture-of-Experts Adapter with Multi-Task Learning for Spoken Dialogue Models](https://www.isca-archive.org/interspeech_2025/chao25_interspeech.html)
**Taxonomy:** `meaning-and-interaction / prosody-and-paralinguistics / prosodic-meaning`
**Evidence:** D3 full-paper capture; PDF SHA-256 `74156ce29c0acada9426beb6e2d31b0f360a4141ed25e8ea705491e0443120bb`; full-text SHA-256 `2c526cec833be016799b921654dcebe2580d37bf8e40ad4a6081a504d9399612`.

- **Ordinary problem:** A spoken dialogue response can be linguistically correct yet emotionally wrong if it misses how the user sounds and what affective state the exchange requires.
- **Why it is hard:** Speech carries valence, arousal, and dominance through fine-grained cues that ordinary text-only dialogue models discard, so a coherent response can still be socially inappropriate.
- **Naive attempt:** Generate dialogue from transcript text alone or add a single emotion label after response generation.
- **Central move:** Attach a sparse affective mixture-of-experts adapter and train emotion prediction jointly with response generation so acoustic affect influences the response decision.
- **Mechanism:** A-SMiLE encodes the input speech, routes it through sparse experts, predicts continuous valence/arousal/dominance values, and conditions response generation on the affective representation. The joint objective combines mean-squared error for emotion prediction with cross-entropy for response generation; evaluation uses DailyTalk and a hard-case emotional set.
- **Mathematical idea:** The model minimizes a weighted sum of emotion MSE and response token cross-entropy. Reported metrics separate VAD prediction from response quality, including automatic response measures and GPT-4o-based evaluation, so no one score is treated as emotion itself.
- **What the paper reports:** The paper reports improvements over text-only and other baselines on VAD prediction and response generation on DailyTalk and its 0.8-hour hard-case emotional benchmark.
- **Limits:** The hard-case data and automatic judge define the tested notion of affective appropriateness; VAD labels simplify lived emotion and GPT-based evaluation is a proxy. The paper does not establish sustained human dialogue benefit or causal understanding of emotion; no independent reproduction was performed.

## 217. The Prosodic Characteristics of Standard Chinese Rhetorical Questions in Naturalistic Settings

**Paper:** [The Prosodic Characteristics of Standard Chinese Rhetorical Questions in Naturalistic Settings](https://www.isca-archive.org/interspeech_2025/chen25g_interspeech.html)
**Taxonomy:** `meaning-and-interaction / prosody-and-paralinguistics / prosodic-meaning`
**Evidence:** D3 full-paper capture; PDF SHA-256 `b0d9482e3785e8a7061d9cf904ed4c83b73e562c23cf07b280bd679ae3137929`; full-text SHA-256 `38166b6468f2a1185a95bc735b1948b25f86c2ba2299d5a97bfcce05ebd8017b`.

- **Ordinary problem:** A rhetorical question can have the same words as an information-seeking question but perform a different action, so listeners need prosody and syntax to distinguish them.
- **Why it is hard:** The difference may disappear in scripted laboratory speech, while a single global pitch measure misses which word carries the intended emphasis.
- **Naive attempt:** Treat identical text as identical meaning or look only at sentence-final intonation.
- **Central move:** Compare matched question types in naturalistic reading and measure where prominence shifts, including the interaction with sentence structure.
- **Mechanism:** One hundred three native Mandarin speakers produced information-seeking and rhetorical questions through an online platform; pitch and duration of prominent verbs and modal verbs are analyzed.
- **Mathematical idea:** Prosody is localized to syntactic positions: prominence placement and its acoustic realization connect the waveform to communicative intention.
- **What the paper reports:** Speakers tend to mark rhetorical meaning by increasing pitch and duration on the verb or modal verb, with other cues depending on sentence structure.
- **Limits:** Standard Chinese, sentence materials, online reading, participant sample, and question interpretation bound the result; rhetorical intent is not reducible to one universal pitch rule.

## 218. MIKU-PAL: An Automated and Standardized Multimodal Method for Speech Paralinguistic and Affect Labeling

**Paper:** [MIKU-PAL: An Automated and Standardized Multimodal Method for Speech Paralinguistic and Affect Labeling](https://www.isca-archive.org/interspeech_2025/cheng25_interspeech.html)
**Taxonomy:** `meaning-and-interaction / prosody-and-paralinguistics / paralinguistic-state`
**Evidence:** D3 full-paper capture; PDF SHA-256 `004fbe29e504e0fb366d200ece28698caa68730dfa1595be21f28cdddb293d2c`; full-text SHA-256 `a60c575c7979c1210bd6da5fe6adb9b20d8d6cf4c186e35500acfa1fc482101f`.

- **Ordinary problem:** Large emotional-speech datasets are expensive to label consistently, but expressive text-to-speech and voice-cloning systems need many fine-grained emotion examples.
- **Why it is hard:** Video contains face, voice, context, and annotation noise; an automated labeler must align modalities and preserve disagreement rather than manufacture false precision.
- **Naive attempt:** Have people label every clip manually or assign one coarse emotion from audio alone.
- **Central move:** Use a multimodal language-model pipeline with face tracking and emotion analysis, then release the resulting fine-grained MIKU-EmoBench corpus for synthesis research.
- **Mechanism:** MIKU-PAL is an automated multimodal method for paralinguistic and affect labeling.
- **Mathematical idea:** Corpus creation is itself multimodal inference: the label is a negotiated interpretation of face, voice, and context, and its consistency must be measured separately from its usefulness to a downstream synthesizer.
- **What the paper reports:** The paper reports 68.5% MELD accuracy, 0.93 Fleiss kappa, 83% human rationality ratings, and a 131.2-hour benchmark with up to 26 emotion types.
- **Limits:** Video sources, model judgments, cultural assumptions, label taxonomy, human validation, and downstream use bound the claim; agreement or rationality is not ground-truth emotion.

## 219. EmoSphere-SER: Enhancing Speech Emotion Recognition Through Spherical Representation with Auxiliary Classification

**Paper:** [EmoSphere-SER: Enhancing Speech Emotion Recognition Through Spherical Representation with Auxiliary Classification](https://www.isca-archive.org/interspeech_2025/cho25_interspeech.html)
**Taxonomy:** `meaning-and-interaction / prosody-and-paralinguistics / paralinguistic-state`
**Evidence:** D3 full-paper capture; PDF SHA-256 `a078450f9f9dc00fb9b4442e3144993b28e6aa061f8fbc517a244131a6797743`; full-text SHA-256 `d1fea48166a639c76582293886d9ffbc4e33538ffc44ef1267c4d3e03e26c76c`.

- **Ordinary problem:** Emotion is not just a class label: a listener may need to distinguish nearby positions in arousal, valence, and dominance without making unstable continuous predictions.
- **Why it is hard:** The three dimensions have geometry and uneven density; ordinary independent regression can ignore local structure and produce inconsistent points.
- **Naive attempt:** Regress each affect dimension independently and treat the output as equally reliable everywhere.
- **Central move:** Convert VAD values to spherical coordinates, classify spherical regions as an auxiliary task, dynamically weight objectives, and pool temporal style information.
- **Mechanism:** EmoSphere-SER uses spherical VAD-region classification to guide emotion regression.
- **Mathematical idea:** The model gives the affect space neighborhoods and a coarse location before asking for a precise coordinate, coupling classification’s stability with regression’s detail.
- **What the paper reports:** The reported experiments show the combined model outperforming the compared baselines and improving prediction consistency.
- **Limits:** Emotion labels, VAD geometry, datasets, region partition, weighting, and metrics bound the result; a better coordinate prediction does not establish a speaker’s actual inner state.

## 220. Developing a Top-tier Framework in Naturalistic Conditions Challenge for Categorized Emotion Prediction: From Speech Foundation Models and Learning Objective to Data Augmentation and Engineering Choices

**Paper:** [Developing a Top-tier Framework in Naturalistic Conditions Challenge for Categorized Emotion Prediction: From Speech Foundation Models and Learning Objective to Data Augmentation and Engineering Choices](https://www.isca-archive.org/interspeech_2025/feng25_interspeech.html)
**Taxonomy:** `meaning-and-interaction / prosody-and-paralinguistics / paralinguistic-state`
**Evidence:** D3 full-paper capture; PDF SHA-256 `dc1ba163f0a003b86e5f01f91988b82705bc788cc74327b0c403c592f80cb4fb`; full-text SHA-256 `f348981f798191b93dd4dbabf464b0a245249deff5777293d886b4a232d1dfb2`.

- **Ordinary problem:** Emotion in natural speech is uncertain and often mixed, so a system should represent what listeners actually agree on rather than force one absolute label.
- **Why it is hard:** The challenge data are imbalanced, roughly 19% of training samples lack annotator agreement, and a majority label throws away legitimate ambiguity and minority emotion evidence.
- **Naive attempt:** Train hard one-hot emotion classes and optimize overall accuracy, allowing the majority emotions to dominate the learning signal.
- **Central move:** Predict an emotion distribution with KL-divergence, train speech and transcript representations together, and use annotation dropout, majority/minority audio mixing, reweighting, and minority average precision to expose the imbalance.
- **Mechanism:** SAILER compares WavLM Large and Whisper Large-V3 speech encoders, combines speech and text embeddings, and predicts primary plus secondary emotion and attribute labels. Annotation dropout removes 20% of majority-class annotations during training; audio mixing combines majority and minority samples with silence or overlap.
- **Mathematical idea:** The target is a soft distribution d rather than a one-hot vector, and KL divergence trains the predicted distribution. The best single system reports macro-F1 0.411 and accuracy 54.53; a three-system ensemble reaches macro-F1 0.431 and accuracy 57.00, while minority mean average precision is tracked separately.
- **What the paper reports:** Whisper representations outperform WavLM in the reported comparisons; audio mixing and annotation dropout improve minority-class average precision more reliably than overall accuracy, and adding secondary emotions improves the main score but can hurt minority classes.
- **Limits:** The evidence comes from the MSP-Podcast IS25-SER challenge and validation-heavy experiments; the hidden test labels limit systematic ablation. Emotion categories and annotator distributions remain task-specific, and no independent reproduction was performed.

## 221. Learning More with Less: Self-Supervised Approaches forLow-Resource Speech Emotion Recognition

**Paper:** [Learning More with Less: Self-Supervised Approaches forLow-Resource Speech Emotion Recognition](https://www.isca-archive.org/interspeech_2025/gong25b_interspeech.html)
**Taxonomy:** `meaning-and-interaction / prosody-and-paralinguistics / paralinguistic-state`
**Evidence:** D3 full-paper capture; PDF SHA-256 `bb874107ce314f883fc9369123c6c97780f3616ad1b9cd81380279d3b024e3b1`; full-text SHA-256 `559d4ba41772d7dc07eb59c8f9b421b793574d49889bf181e46c8ef0be3d4fb6`.

- **Ordinary problem:** Emotion recognition should work for languages with few labeled examples, not only for languages with large emotion datasets.
- **Why it is hard:** Emotion labels are scarce and expressive cues do not transfer unchanged across languages.
- **Naive attempt:** Train a supervised classifier only on the small labeled target-language set.
- **Central move:** Learn a speech representation without labels using contrastive learning or BYOL, then transfer it across languages.
- **Mechanism:** The study compares self-supervised objectives and analyzes their cross-lingual behavior for Urdu, German, and Bangla emotion recognition.
- **Mathematical idea:** F1 measures class decisions; the comparison asks how much it improves over supervised or conventional representation learning under limited labels.
- **What the paper reports:** The paper reports F1 improvements of 10.6% in Urdu, 15.2% in German, and 13.9% in Bangla.
- **Limits:** The reported gains depend on the selected languages, labels, augmentations, and emotion definitions; cultural validity and transfer to new languages remain open.

## 222. Age-related changes in multisensory integration of emotions in an audiovisual face-prosody-semantics Stroop task

**Paper:** [Age-related changes in multisensory integration of emotions in an audiovisual face-prosody-semantics Stroop task](https://www.isca-archive.org/interspeech_2025/lin25e_interspeech.html)
**Taxonomy:** `meaning-and-interaction / prosody-and-paralinguistics / prosodic-meaning`
**Evidence:** D3 full-paper capture; PDF SHA-256 `13748e095cc443fc3e00cf144771a59af6566de812451610f41c11a68d75d9bd`; full-text SHA-256 `ede1324b62d8fbb39064efd98016a47045c32eabb7b497847e5ba2c066351a8b`.

- **Ordinary problem:** Emotion can be expressed simultaneously by words, voice melody, and a face, and a listener must decide what to do when those channels disagree.
- **Why it is hard:** Older and younger listeners may rely on channels differently, so a single average emotion score hides both channel priorities and conflict resolution.
- **Naive attempt:** Combine all channels as if they were equally reliable or measure each channel in isolation.
- **Central move:** Use a cross-channel conflict task that directs attention to one channel while manipulating congruence in the others, then compare age groups and channel effects.
- **Mechanism:** Younger and older adults perform an audiovisual face-prosody-semantics Stroop task with happy and sad cues under congruent and incongruent conditions.
- **Mathematical idea:** Reaction or accuracy differences reveal selective attention and integration costs; congruence tests whether one channel can override another.
- **What the paper reports:** Older adults show reduced emotion integration, especially for prosody and other nonverbal cues, with larger age differences under incongruence.
- **Limits:** The task, emotions, participant groups, language, and interpretation of Stroop costs bound the result; laboratory conflict does not directly predict everyday communication.

## 223. Multimodal Prosody Modeling: A Use Case for Multilingual Sentence Mode Prediction

**Paper:** [Multimodal Prosody Modeling: A Use Case for Multilingual Sentence Mode Prediction](https://www.isca-archive.org/interspeech_2025/vlasenko25_interspeech.html)
**Taxonomy:** `meaning-and-interaction / prosody-and-paralinguistics / prosodic-meaning`
**Evidence:** D3 full-paper capture; PDF SHA-256 `f9ccc84daa4febcbab3a5ff92c9afeca2f5a1f0461a56e70f894afa1bcd2cae9`; full-text SHA-256 `4d0a05d2819de1f69b7ae50df033e31473261b9dccd6de346a59d5ca7b3891da`.

- **Ordinary problem:** Sentence mode—such as a question or statement—is carried not only by words but also by prosody, and a useful model should work across languages and modalities.
- **Why it is hard:** Prosody varies with language, speaker, emotion, and recording; text alone misses timing and pitch while audio alone can miss lexical structure.
- **Naive attempt:** Predict sentence mode from text or one acoustic feature and assume the same cue works across languages.
- **Central move:** Combine multimodal prosody representations and evaluate multilingual sentence-mode prediction under the actual interaction between words, voice, and language.
- **Mechanism:** The study presents multimodal prosody modeling for multilingual sentence-mode prediction.
- **Mathematical idea:** Sentence mode is a joint signal: lexical content provides one constraint while pitch, timing, and energy provide another, and disagreement between them is informative rather than noise.
- **What the paper reports:** The paper reports multilingual multimodal prosody-modeling results for sentence-mode prediction.
- **Limits:** Languages, labels, speaker balance, modality quality, and task definition bound the claim; sentence mode is not a complete model of intent.

## 224. Rapport-Building Dialogue Strategies for Deeper Connection: Integrating Proactive Behavior, Personalization, and Aizuchi Backchannels

**Paper:** [Rapport-Building Dialogue Strategies for Deeper Connection: Integrating Proactive Behavior, Personalization, and Aizuchi Backchannels](https://www.isca-archive.org/interspeech_2025/baihaqi25_interspeech.html)
**Taxonomy:** `meaning-and-interaction / turn-taking-and-repair / turn-boundary`
**Evidence:** D3 full-paper capture; PDF SHA-256 `de62a7e39aabd6b88a87b36d134c9fab6013ff6bd4c6fd64ea63924f5bf2a6d0`; full-text SHA-256 `e74618648a48b741e531df95ea157bfb092348e1af3651051d27b670658fc79f`.

- **Ordinary problem:** A conversational agent should build rapport by responding proactively, personally, and with small listener signals rather than waiting for explicit requests.
- **Why it is hard:** Naturalness depends on timing and interaction, so a response strategy can affect both dialogue flow and a person's willingness to share.
- **Naive attempt:** Optimize a language model for task content while ignoring backchannels and stalls.
- **Central move:** Prompt an LLM with a coordinated strategy for proactive behavior, personalization, and aizuchi backchannels, then measure both conversation and participant outcomes.
- **Mechanism:** CO-STAR and few-shot prompts drive a robot in human-robot interaction; stalls, dialogue similarity, robot backchannels, participant behavior, and questionnaires are evaluated.
- **Mathematical idea:** The paper separates system behavior from participant behavior and subjective reports rather than treating one dialogue score as rapport.
- **What the paper reports:** The integrated strategy is reported to improve behavioral and subjective rapport measures.
- **Limits:** The study is bounded to the robot, prompts, participants, and short interaction protocol; long-term trust, cultural variation, and causal attribution remain open.

## 225. ``Dyadosyncrasy'', Idiosyncrasy and Demographic Factors in Turn-Taking

**Paper:** [``Dyadosyncrasy'', Idiosyncrasy and Demographic Factors in Turn-Taking](https://www.isca-archive.org/interspeech_2025/cavalcanti25_interspeech.html)
**Taxonomy:** `meaning-and-interaction / turn-taking-and-repair / turn-boundary`
**Evidence:** D3 full-paper capture; PDF SHA-256 `7b073cb92d0d3888e37e5ef0a05a015282ae3ef70dda3c8b048536f11f7cb76a`; full-text SHA-256 `30437e8e2ad1af33f2b3edb59eecc24126e743fcad8153673697f85626dfd9a1`.

- **Ordinary problem:** Turn timing is jointly produced by two people; one speaker can wait differently with different partners and topics.
- **Why it is hard:** A model that sees only preceding words misses dyad-specific habits, common ground, and social coordination.
- **Naive attempt:** Predict a boundary from current-speaker features and treat talkers as independent.
- **Central move:** Measure transition-floor offset across dyads and model individual, demographic, topic, and pair-specific effects hierarchically.
- **Mechanism:** Spontaneous English dyads are analyzed by mixed models separating individual idiosyncrasy from dyad-specific interaction.
- **Mathematical idea:** Marginal R2 and random-effects comparisons show dyadic effects dominate the reported variation.
- **What the paper reports:** Sex and age have smaller effects while dyad variation most strongly shapes timing; TFO decreases across sampled lifespan.
- **Limits:** English strangers, sparse older data, topic mix, and TFO limit familiar-relationship and full-dialogue claims.

## 226. Multimodal Dynamics of Hand Gestures and Pauses in Multiparty Interactions

**Paper:** [Multimodal Dynamics of Hand Gestures and Pauses in Multiparty Interactions](https://www.isca-archive.org/interspeech_2025/charuau25_interspeech.html)
**Taxonomy:** `meaning-and-interaction / turn-taking-and-repair / turn-boundary`
**Evidence:** D3 full-paper capture; PDF SHA-256 `3a3443380c1af1e2ab7b900fd8b5fbe1eaa97d04d268bb5746ced9bfcaf77daa`; full-text SHA-256 `cb7b6c7108c63df09824287eeac33de44d4e7209c5eb056c811aab8a387e40f3`.

- **Ordinary problem:** In a multiparty conversation, gestures and pauses should be understood as timed coordination rather than unrelated events.
- **Why it is hard:** A pause can occur within one speaker's turn or between speakers, and gesture timing may reflect planning, turn exchange, or social behavior.
- **Naive attempt:** Count gestures and pauses independently or align every gesture only to the nearest word.
- **Central move:** Measure gesture category, pause type, duration, and onset/offset timing together in annotated audiovisual dialogues.
- **Mechanism:** MULTISIMO recordings provide multiparty dialogue annotations; distributions and temporal relations are compared for within- and between-speaker pauses.
- **Mathematical idea:** The unit of analysis is a timed relation among gesture, pause, and speaker turn; duration and onset timing carry different information.
- **What the paper reports:** Self-adaptors align with longer pauses, utterance-final syntax shortens pauses, and most gestured pauses occur within utterances.
- **Limits:** Corpus annotation, participant population, gesture categories, and observational design bound the result; causal cognitive interpretations remain hypotheses.

## 227. Triadic Multi-party Voice Activity Projection for Turn-taking in Spoken Dialogue Systems

**Paper:** [Triadic Multi-party Voice Activity Projection for Turn-taking in Spoken Dialogue Systems](https://www.isca-archive.org/interspeech_2025/elmers25_interspeech.html)
**Taxonomy:** `meaning-and-interaction / turn-taking-and-repair / turn-boundary`
**Evidence:** D3 full-paper capture; PDF SHA-256 `f2c0736fcd3ab708f2fc0ace3ae870a1ebf3a0ddf51ae7236097e00e9180d9b1`; full-text SHA-256 `62e5d686e93c50cff56ba0ded09ed26c96d854482616b1f461bd6b120c7d854c`.

- **Ordinary problem:** A spoken agent must predict who will speak next in a group, because waiting for a long silence causes delay while speaking too early interrupts someone who has not finished.
- **Why it is hard:** Triadic conversation has more possible combinations of active and silent speakers than dyadic conversation, and topic or interaction style changes overlap patterns.
- **Naive attempt:** Use a fixed silence threshold or reuse a two-person turn-taking model without representing each participant’s future activity separately.
- **Central move:** Project future voice activity jointly for all three speakers using short time bins, then compare models trained on spontaneous and attentive triadic Japanese conversation.
- **Mechanism:** The VAP model encodes acoustic history and predicts binary speaking states for each speaker over future bins. With three speakers and two bins per speaker there are 2^6 possible states; cross-entropy trains the state distribution, and next-speaker accuracy compares predictions with held-out activity.
- **Mathematical idea:** The state space is a six-bit joint voice-activity label; probability mass over states gives the predicted future activity. The evaluation reports test loss and next-speaker accuracy, with separate spontaneous and attentive conversation conditions.
- **What the paper reports:** Triadic VAP trained on triadic conversation outperforms the baseline across tested models, while spontaneous discussions are harder than attentive listening; the paper reports accuracy differences by conversation type.
- **Limits:** The data are Japanese triadic discussions with controlled recording and a limited number of participants; the reduced two-bin horizon does not cover the full dyadic two-second state space. Acoustic-only prediction does not establish successful spoken-agent behavior, and no independent reproduction or user study was performed.

## 228. Backchannel prediction for natural spoken dialog systems  using general speaker and listener information

**Paper:** [Backchannel prediction for natural spoken dialog systems  using general speaker and listener information](https://www.isca-archive.org/interspeech_2025/fukunaga25_interspeech.html)
**Taxonomy:** `meaning-and-interaction / turn-taking-and-repair / turn-boundary`
**Evidence:** D3 full-paper capture; PDF SHA-256 `f73517c360845a0f65336d5c2ae09689dd89c7e71924391f77105ae0f16b0e3d`; full-text SHA-256 `b950502c7d5836b3615171fa28b83af36062ceb7a21a8150883e1de157afcbdb`.

- **Ordinary problem:** A listener's short responses—such as agreement, continuation, or surprise—help a spoken dialogue feel responsive; a system should choose the right surface form without storing private speaker IDs.
- **Why it is hard:** Three broad classes are too coarse for generation, while identity embeddings are difficult to deploy and raise privacy concerns.
- **Naive attempt:** Predict a coarse backchannel class from a detailed speaker/listener identity embedding.
- **Central move:** Replace identity-specific inputs with general speaker and listener embeddings and predict eleven surface-form categories as well as three classes.
- **Mechanism:** The model uses speech, text, and general embeddings and compares three- and eleven-category prediction against ID-based systems.
- **Mathematical idea:** Accuracy is reported separately for coarse and fine categories, exposing the cost of richer response choices.
- **What the paper reports:** The paper reports 1.3% accuracy improvement for three classes and 0.9% for eleven classes over conventional ID embeddings.
- **Limits:** The result is author-reported for the tested dialogue corpus and categories; natural turn timing, privacy leakage in embeddings, and user experience remain open.

## 229. Gaze-Enhanced Multimodal Turn-Taking Prediction in Triadic Conversations

**Paper:** [Gaze-Enhanced Multimodal Turn-Taking Prediction in Triadic Conversations](https://www.isca-archive.org/interspeech_2025/heo25_interspeech.html)
**Taxonomy:** `meaning-and-interaction / turn-taking-and-repair / turn-boundary`
**Evidence:** D3 full-paper capture; PDF SHA-256 `872eb41f1b5a7ce0290da61172ca5dce788ac1a13099f67c625fb4427c640061`; full-text SHA-256 `e225d969de4cc2fd137d32ef49e475ee08df533c40f624a4bd149e536520f23b`.

- **Ordinary problem:** In a triadic conversation, a person may look at one participant before taking a turn, and a turn-taking model should use that gaze rather than treating the group as one audio stream.
- **Why it is hard:** Three-way interaction creates competing addressees and overlapping cues; gaze timing can precede speech while being noisy or socially ambiguous.
- **Naive attempt:** Predict turn transitions from audio only or use one global gaze feature for the whole group.
- **Central move:** Add person-specific gaze cues to multimodal turn-taking prediction and test whether they improve decisions in triadic conversations.
- **Mechanism:** The paper studies gaze-enhanced multimodal turn-taking prediction in triadic conversations.
- **Mathematical idea:** Turn-taking is addressed to someone: person-conditioned visual cues resolve part of the interaction structure that an audio-only boundary cannot represent.
- **What the paper reports:** The paper reports turn-taking prediction results with gaze enhancement in triadic interaction.
- **Limits:** Participants, camera setup, roles, task, gaze annotation, and latency bound generalization; gaze is a cue, not a deterministic intention signal.

## 230. Enhancing Transcripts of Open-Source Automatic Speech Recognition Models Through Fine-Tuning with Laughter and Speech-Laugh

**Paper:** [Enhancing Transcripts of Open-Source Automatic Speech Recognition Models Through Fine-Tuning with Laughter and Speech-Laugh](https://www.isca-archive.org/interspeech_2025/ho25b_interspeech.html)
**Taxonomy:** `meaning-and-interaction / turn-taking-and-repair / repair-and-clarification`
**Evidence:** D3 full-paper capture; PDF SHA-256 `35a207e6910569611bbe9471c29659b127994614e16c23c543eac8a198e82263`; full-text SHA-256 `c51b33ea1a8aa6ecf6bb6c3b368ed048a494ddac4afaa009a763af3fdb0f3f93`.

- **Ordinary problem:** An ASR transcript should preserve laughter and speech-laugh events because they affect meaning, turn timing, and conversational analysis.
- **Why it is hard:** Ordinary ASR training treats non-lexical laughter as noise or deletion, while speech-laugh blends vocalization and words in ways that do not fit a simple token.
- **Naive attempt:** Remove laughter before recognition or fine-tune only on ordinary words and infer laughter from punctuation.
- **Central move:** Fine-tune open-source ASR models with laughter and speech-laugh examples and evaluate how transcript enhancement changes these events.
- **Mechanism:** The paper enhances open-source ASR transcripts through fine-tuning with laughter and speech-laugh.
- **Mathematical idea:** The transcript target expands from words to interactional vocal events; the model must preserve an event boundary and its overlap with lexical speech.
- **What the paper reports:** The paper reports improved handling of laughter and speech-laugh in the tested ASR transcripts.
- **Limits:** Annotation scheme, language, laughter types, model, data mixture, and transcript use case bound the result; event recognition is not a full emotion or intent analysis.

## 231. Efficient and Direct Duplex Modeling for Speech-to-Speech Language Model

**Paper:** [Efficient and Direct Duplex Modeling for Speech-to-Speech Language Model](https://www.isca-archive.org/interspeech_2025/hu25f_interspeech.html)
**Taxonomy:** `meaning-and-interaction / turn-taking-and-repair / turn-boundary`
**Evidence:** D3 full-paper capture; PDF SHA-256 `16f0bf9ad75a7eb22bfd15126642ad0103c3f1b1ca776e2868eabdcf35b404e4`; full-text SHA-256 `6227f4e8d1d2257050c96fa7d41e59331d46e0b156b9c7b58eac8808bf62f029`.

- **Ordinary problem:** A speech-to-speech language model in a duplex conversation must listen and speak at overlapping times without losing the current turn or waiting for a full utterance.
- **Why it is hard:** Duplex interaction couples streaming recognition, generation, interruption, and turn timing; a model optimized for one direction can block or talk over the other.
- **Naive attempt:** Use a turn-taking pipeline that waits for end-of-speech or run separate listen and speak models with no shared state.
- **Central move:** Build an efficient direct duplex model that represents incoming and outgoing speech jointly and evaluates real-time speech-to-speech behavior.
- **Mechanism:** The paper studies efficient and direct duplex modeling for speech-to-speech language models.
- **Mathematical idea:** Duplexity is a control problem over concurrent streams: the model must decide what to retain, when to respond, and when to yield while generating speech.
- **What the paper reports:** The paper reports efficiency and interactive speech-to-speech results for the duplex model.
- **Limits:** Latency, overlap, interruptions, model size, dialogue tasks, and evaluation protocol bound the result; a real-time demo is not robust open-ended conversation.

## 232. Visual Cues Support Robust Turn-taking Prediction in Noise

**Paper:** [Visual Cues Support Robust Turn-taking Prediction in Noise](https://www.isca-archive.org/interspeech_2025/oconnorrussell25_interspeech.html)
**Taxonomy:** `meaning-and-interaction / turn-taking-and-repair / turn-boundary`
**Evidence:** D3 full-paper capture; PDF SHA-256 `f7188f142b508f1d0736014ff2eb2e21a493d32bc8674eb3364c2ca6d584922f`; full-text SHA-256 `957a9477b5bb037ff18f49a7c4be67b843d30b2729736484d901c4148c24d8b4`.

- **Ordinary problem:** People use gaze and other visible cues to signal that a turn is ending or beginning, especially when noise makes audio timing unreliable.
- **Why it is hard:** Turn-taking is a coupled prediction-and-action problem: visual cues can arrive before words finish, while noise corrupts the acoustic evidence and social norms vary.
- **Naive attempt:** Predict the next turn from audio alone or treat a detected pause as a universal handoff signal.
- **Central move:** Add visual cues to turn-taking prediction and test whether they make decisions more robust in noise.
- **Mechanism:** The study evaluates visual cues for robust turn-taking prediction in noise.
- **Mathematical idea:** A turn is a coordination event between people, not merely a boundary in a waveform; combining channels lets one cue compensate when another is degraded.
- **What the paper reports:** The paper reports that visual cues support more robust turn-taking prediction under noisy conditions.
- **Limits:** Participants, camera viewpoint, interaction task, noise type, timing labels, and model latency bound the claim; a lab cue is not a universal conversational rule.

## 233. FD-Bench: A Full-Duplex Benchmarking Pipeline Designed for Full Duplex Spoken Dialogue Systems

**Paper:** [FD-Bench: A Full-Duplex Benchmarking Pipeline Designed for Full Duplex Spoken Dialogue Systems](https://www.isca-archive.org/interspeech_2025/peng25b_interspeech.html)
**Taxonomy:** `meaning-and-interaction / turn-taking-and-repair / turn-boundary`
**Evidence:** D3 full-paper capture; PDF SHA-256 `4af22e7595d4e2e61f49815d1d5c666f2f5e9c9df59d8af371f438650c915158`; full-text SHA-256 `ae3598f0d3287fba533aac99288d3f99b7f25ea5e284ddf0a78f241316cd8a74`.

- **Ordinary problem:** A full-duplex spoken agent must keep listening while speaking, handle interruptions, and respond to backchannels without waiting for a neat turn boundary.
- **Why it is hard:** Traditional dialogue benchmarks assume alternating turns and therefore miss failures caused by latency, interruption timing, overlap, and noisy simultaneous speech.
- **Naive attempt:** Evaluate a duplex agent with ordinary response quality or word-error scores and assume those scores reveal interruption behavior.
- **Central move:** Construct a benchmark that generates controlled full-duplex conversations and measures interruption handling, delay, and robustness with metrics designed for overlapping interaction.
- **Mechanism:** FD-Bench combines generated speech, TTS, ASR, and LLM-based scenario control to create over 40 hours of speech, 293 simulated conversations, and 1,200 interruptions. It runs three open-source full-duplex systems through the same scenarios and records response and interruption outcomes.
- **Mathematical idea:** The benchmark defines event-level metrics over interruption and delay conditions rather than reducing the interaction to one transcript score. Its denominator is the simulated conversation/interruption set, not ordinary ASR utterances.
- **What the paper reports:** The reported benchmark finds that all three tested systems still struggle with user interruptions, frequent disruptions, and noisy conditions; the paper states that data and code will be released.
- **Limits:** The conversations and interruptions are simulated/generated, and benchmark metrics are proxies for human experience. Release claims are not equivalent to artifact execution here; no independent reproduction or user study was performed.

## 234. Pathology-Aware Speech Encoding and Data Augmentation for Dysarthric Speech Recognition

**Paper:** [Pathology-Aware Speech Encoding and Data Augmentation for Dysarthric Speech Recognition](https://www.isca-archive.org/interspeech_2025/baumann25_interspeech.html)
**Taxonomy:** `people-variation-and-health / atypical-and-assistive-speech / dysarthria-and-atypical-speech`
**Evidence:** D3 full-paper capture; PDF SHA-256 `8e2c31689e328ae56f2d71f9ec25781e83ade65db4cc786019dfd64932b0ed04`; full-text SHA-256 `6e8d689f1bc265813ce59f2e33f29c8924527df4eba9ff61c29e8be17a1b1b11`.

- **Ordinary problem:** A recognizer trained on typical speech must understand speech altered by different medical conditions despite scarce labels.
- **Why it is hard:** Articulation, phonation, and prosody change differently by etiology; indiscriminate data may teach the wrong invariances, while synthetic data adds artifacts.
- **Naive attempt:** Fine-tune a general encoder on the small clinical corpus, or add as much unrelated speech as possible.
- **Central move:** Continue self-supervised pre-training on pathological speech, use etiology-specific codebooks, and select external examples by semantic similarity.
- **Mechanism:** A BEST-RQ Conformer is continued on pathological speech; fine-tuning compares synthetic, out-of-domain, and transcript-embedding-selected data, with similarity losses.
- **Mathematical idea:** Overall WER is 19.73 versus 22.73 for the BEST-RQ baseline; 150% OOD augmentation reaches 17.32 and similarity-weighted pairing 17.81, while Down syndrome does not benefit from augmentation.
- **What the paper reports:** The authors report 13.2% relative WER improvement from pathology-aware pre-training, up to 8.7% from synthetic data, 12.2% from OOD data, and 9.7% from semantic selection.
- **Limits:** Etiologies, corpora, similarity model, and ratios bound the claim; improvements differ by condition and synthetic speech may not preserve clinical variation.

## 235. EEG-based Voice Conversion : Hearing the Voice of Your Brain

**Paper:** [EEG-based Voice Conversion : Hearing the Voice of Your Brain](https://www.isca-archive.org/interspeech_2025/geng25b_interspeech.html)
**Taxonomy:** `people-variation-and-health / atypical-and-assistive-speech / augmentative-communication`
**Evidence:** D3 full-paper capture; PDF SHA-256 `f924192893764c3172ebff54cdcadd818d34616ca7c581274b0236b43f577479`; full-text SHA-256 `dfa1eb26f6494a46b4734f5f81226331d5b52ead8cccea1c4d7c7d36346aa061`.

- **Ordinary problem:** A person who cannot speak reliably may need a system that turns brain activity into a chosen voice without collecting data from the target speaker first.
- **Why it is hard:** EEG is noisy and indirect, while voice identity is highly speaker-specific; conversion must align these signals without target examples.
- **Naive attempt:** Train a voice converter only from speech or require target-speaker recordings before conversion.
- **Central move:** Align EEG features with speaker voice features and use a speech-trained zero-shot voice-conversion model.
- **Mechanism:** A three-stage training strategy maps EEG to speaker-specific features and conditions a pretrained speech-only converter; Dutch single-word production tests the system.
- **Mathematical idea:** The alignment is a cross-modal mapping problem; zero-shot evaluation tests whether target identity can be supplied without target speech data.
- **What the paper reports:** The paper reports reliable target-voice conversion on the Single-Word-Production Dutch-iBIDS dataset.
- **Limits:** Single words, EEG setup, target voices, and small dataset define the claim; intelligibility, privacy, consent, and real assistive communication remain open.

## 236. A Silent Speech Decoding System from EEG and EMG with Heterogenous Electrode Configurations

**Paper:** [A Silent Speech Decoding System from EEG and EMG with Heterogenous Electrode Configurations](https://www.isca-archive.org/interspeech_2025/inoue25b_interspeech.html)
**Taxonomy:** `people-variation-and-health / atypical-and-assistive-speech / augmentative-communication`
**Evidence:** D3 full-paper capture; PDF SHA-256 `4699a5e0d7a3500e45a6442a1333eec03eadc79be27d48a3e41191146cd7cda5`; full-text SHA-256 `ef9651bbb6b827338f01adb0d41e20be3beb5e3b98bb3cb3cf32f69b2f34da3d`.

- **Ordinary problem:** Silent-speech decoding could let speech-impaired users communicate without vocalizing, but biosignal recordings vary across people and electrode layouts.
- **Why it is hard:** EEG and EMG configurations are heterogeneous and patient data are scarce, so a single fixed-subject model does not transfer well.
- **Naive attempt:** Train one model per subject with one fixed electrode configuration.
- **Central move:** Handle heterogeneous electrodes and use multitask training for cross-subject and cross-language calibration.
- **Mechanism:** A shared model learns from varying EEG/EMG layouts while multitask objectives stabilize word classification across speakers and languages.
- **Mathematical idea:** Word classification accuracy measures whether neural signals preserve enough information for decoding.
- **What the paper reports:** Accuracy is 95.3% for healthy participants and 54.5% for a patient, versus 70.1% and 13.2% for single-subject baselines.
- **Limits:** Patient count, setup, calibration, and author-reported results limit clinical deployment claims.

## 237. EEG-based Speech Decoding Based on Multi-mode Joint Modeling

**Paper:** [EEG-based Speech Decoding Based on Multi-mode Joint Modeling](https://www.isca-archive.org/interspeech_2025/li25j_interspeech.html)
**Taxonomy:** `people-variation-and-health / atypical-and-assistive-speech / augmentative-communication`
**Evidence:** D3 full-paper capture; PDF SHA-256 `d8f3feb21809dd40c7128323d675b6f4a375a995c1c2be4d904cb198cce27620`; full-text SHA-256 `973141aa5b9b11def3bd4a1112f1045165442920e4af9b4812a1a02a0bec358a`.

- **Ordinary problem:** A person who cannot reliably speak may still communicate through brain signals, but imagined speech produces weaker and less direct evidence than spoken speech.
- **Why it is hard:** EEG is noisy and varies across imagined, intended, and spoken modes; a model trained on one mode may discard useful shared structure or use too many channels.
- **Naive attempt:** Train separate decoders for each mode using every available EEG channel.
- **Central move:** Train one model across modes with dynamic masking, then use its learned channel relevance to make a smaller single-mode decoder.
- **Mechanism:** A joint EEG decoder covers imagined, intended, and spoken speech and is evaluated on four-vowel classification, including a channel-selection transfer step.
- **Mathematical idea:** Shared and mode-specific evidence are balanced by masking; vowel accuracy tests decoding while selected-channel performance tests whether the joint model identifies useful measurements.
- **What the paper reports:** Imagined-speech accuracy rises to 34.95% from a 29.18% baseline, and channel-selected single-mode models outperform models using all channels.
- **Limits:** The four-vowel task, participants, EEG hardware, mode definitions, and accuracy metric bound the result; it does not demonstrate unrestricted communication or clinical readiness.

## 238. Synthetic Dysarthric Speech: A Supplement, Not a Substitute for Authentic Data in Dysarthric Speech Recognition

**Paper:** [Synthetic Dysarthric Speech: A Supplement, Not a Substitute for Authentic Data in Dysarthric Speech Recognition](https://www.isca-archive.org/interspeech_2025/li25n_interspeech.html)
**Taxonomy:** `people-variation-and-health / atypical-and-assistive-speech / dysarthria-and-atypical-speech`
**Evidence:** D3 full-paper capture; PDF SHA-256 `271a0450f07fc0851b90bbbbc8e71c7afde6df7c1906db9051df9edb76be16e5`; full-text SHA-256 `fa106e275c42473eb4cb813dd7f9eda0dabd1f823bc1d2963c38fe1cf21a5805`.

- **Ordinary problem:** Dysarthric speech is scarce and variable, so recognizers need more training examples without pretending that synthetic speech is equivalent to a person's real motor patterns.
- **Why it is hard:** Synthetic speech can scale text and speaker combinations but may miss irregular timing, articulation, spectral detail, and clinically meaningful variation.
- **Naive attempt:** Replace authentic dysarthric recordings with large quantities of generated speech because more data should always improve recognition.
- **Central move:** Train speaker-specific TTS systems, generate synthetic dysarthric utterances at several scales, combine them with authentic data for dysarthric speech recognition, and compare feature distributions and recognition results.
- **Mechanism:** The study varies whether training uses authentic Set A/Set B data, synthetic data derived from Set A, or much larger synthetic additions. It measures ASR performance and compares acoustic feature distributions between authentic and synthetic samples.
- **Mathematical idea:** Synthetic data is a distributional proposal, not a label-preserving copy: the relevant question is whether generated speech spans the motor and acoustic variation needed by the recognizer.
- **What the paper reports:** Across the tested Chinese dysarthric speech setup, synthetic speech alone does not replace authentic data and large synthetic additions yield only marginal gains over authentic training.
- **Limits:** The language, seven-speaker usable subset, TTS model, data scale, ASR architecture, and speaker-independent split bound generalization; a synthetic-data result is not clinical validation.

## 239. Addressing Task Conflicts in Stuttering Detection via MMoE-Based Multi-Task Learning

**Paper:** [Addressing Task Conflicts in Stuttering Detection via MMoE-Based Multi-Task Learning](https://www.isca-archive.org/interspeech_2025/liu25f_interspeech.html)
**Taxonomy:** `people-variation-and-health / atypical-and-assistive-speech / dysarthria-and-atypical-speech`
**Evidence:** D3 full-paper capture; PDF SHA-256 `41ff0eed79d90ac7ccab2da8469d8058a3f7b7af6da6300bb5e4e863d0fd4387`; full-text SHA-256 `efbfbd8db38bc651fdd7c238b47e05bac2165f87edcea141ab82f28620747dd9`.

- **Ordinary problem:** A stuttering detector often needs several related outputs, but a feature useful for one symptom can interfere with another task.
- **Why it is hard:** Shared parameters force tasks with different cues or label frequencies to compete, and a single average loss hides which task is being harmed.
- **Naive attempt:** Train all tasks with one shared representation and one fixed loss weighting.
- **Central move:** Analyze task conflicts explicitly, use rules to separate incompatible signals, and let a mixture of experts route examples to task-relevant submodels.
- **Mechanism:** Rule-based multi-task learning and a multi-mixture-of-experts model are evaluated on stuttering-symptom detection and the 2024 SLT challenge.
- **Mathematical idea:** The model treats task gradients and predictions as competing demands; per-task and average F1 reveal whether collaboration improves the clinical outputs.
- **What the paper reports:** The rule-based strategy reports a 19.9% average-F1 gain over baseline and the MMoE strategy a further 7.55% improvement.
- **Limits:** The challenge data, symptom definitions, labels, class balance, and F1 aggregation bound the claim; benchmark gains do not establish clinical reliability or fairness.

## 240. Fairness in Dysarthric Speech Synthesis: Understanding Intrinsic Bias in Dysarthric Speech Cloning using F5-TTS

**Paper:** [Fairness in Dysarthric Speech Synthesis: Understanding Intrinsic Bias in Dysarthric Speech Cloning using F5-TTS](https://www.isca-archive.org/interspeech_2025/m25_interspeech.html)
**Taxonomy:** `people-variation-and-health / atypical-and-assistive-speech / dysarthria-and-atypical-speech`
**Evidence:** D3 full-paper capture; PDF SHA-256 `55d6ed6df4a7d6c45ba2b1cd66582af5cd0c1e54e27d8888d1063b72ca522f3c`; full-text SHA-256 `063336fccff470c1f312df94cd861a0a28a8d118372c7f12c1c616df5d6e234f`.

- **Ordinary problem:** Voice synthesis for dysarthric speakers should preserve intelligibility, identity, and prosodic character without treating disability severity as noise to erase.
- **Why it is hard:** A zero-shot synthesizer may copy speaker identity while changing pathological speech patterns unevenly across severity groups, creating a fairness problem hidden by average quality scores.
- **Naive attempt:** Report one average similarity or intelligibility score and assume it applies equally to healthy and dysarthric speakers.
- **Central move:** Generate speech from TORGO prompts with F5-TTS, measure intelligibility, speaker similarity, and prosody similarity, then compare severity groups using parity difference and disparate impact.
- **Mechanism:** The study defines metrics over group means: WER/CER for intelligibility, SIM-o cosine similarity for speaker traits, and AutoPCP for prosody. Fairness is assessed by deviations from healthy-speaker reference behavior.
- **Mathematical idea:** The mechanism is an evaluation reframing: voice cloning is not one scalar quality target when a model may preserve identity but unevenly alter disability-linked prosody or intelligibility.
- **What the paper reports:** The paper reports severity-dependent differences in the objective measures and uses those differences to characterize intrinsic bias in F5-TTS cloning.
- **Limits:** TORGO, reference-prompt choice, automatic metrics, severity grouping, and zero-shot model behavior bound the result; parity in proxies does not establish respectful control, consent, or listener benefit.

## 241. Personalized Fine-Tuning with Controllable Synthetic Speech from LLM-Generated Transcripts for Dysarthric Speech Recognition

**Paper:** [Personalized Fine-Tuning with Controllable Synthetic Speech from LLM-Generated Transcripts for Dysarthric Speech Recognition](https://www.isca-archive.org/interspeech_2025/wagner25_interspeech.html)
**Taxonomy:** `people-variation-and-health / atypical-and-assistive-speech / dysarthria-and-atypical-speech`
**Evidence:** D3 full-paper capture; PDF SHA-256 `0f321efea0c245e9c9fad89ac1fdf6135bfbff22c5e586a920c503888842289e`; full-text SHA-256 `0396ab21f47dea5d0edb662c677b0e3cfba0d82c4415422a797af6286ddf8ddf`.

- **Ordinary problem:** A recognizer for dysarthric speech should adapt to a particular speaker even when only limited recordings are available.
- **Why it is hard:** Dysarthria changes the relation between intended words and acoustic realization; synthetic data can add coverage but can also repeat the wrong errors or sound unlike the speaker.
- **Naive attempt:** Fine-tune on a small personal set only, or add generic synthetic speech without controlling what variation it contributes.
- **Central move:** Use LLM-generated transcripts to create controllable synthetic speech and personalize fine-tuning for the target speaker, then measure recognition under speaker-specific conditions.
- **Mechanism:** The paper studies personalized fine-tuning with controllable synthetic speech for dysarthric speech recognition.
- **Mathematical idea:** Personalization is a data-design problem: synthetic examples are useful only when their transcript, pronunciation variation, and speaker control support the target speaker rather than dilute them.
- **What the paper reports:** The paper reports recognition results for personalized adaptation using controllable synthetic data.
- **Limits:** Speaker cohort, dysarthria type, transcript generation, synthesis quality, and adaptation budget limit generalization or clinical claims.

## 242. Semantic Processing During Spoken Word Production by Children with Cochlear Implants

**Paper:** [Semantic Processing During Spoken Word Production by Children with Cochlear Implants](https://www.isca-archive.org/interspeech_2025/wang25l_interspeech.html)
**Taxonomy:** `people-variation-and-health / atypical-and-assistive-speech / augmentative-communication`
**Evidence:** D3 full-paper capture; PDF SHA-256 `26ff05eb02b46e3bf0b2eb19de9be45a9be0b7effea408164a4bcb557f55815c`; full-text SHA-256 `5980093c202cc73ebbdadccbb0f1a2155760e594d15c4bf8cc2df994b6a376d8`.

- **Ordinary problem:** Children with cochlear implants may produce intelligible speech while using different internal routes to select and plan words.
- **Why it is hard:** Sound production measures alone cannot reveal how semantic competition is handled during word production.
- **Naive attempt:** Compare only pronunciation accuracy and infer normal semantic access from normal-sounding speech.
- **Central move:** Use a picture-word interference task to test whether semantically related distractors slow naming differently for children with implants and hearing peers.
- **Mechanism:** Children with cochlear implants and normal-hearing peers name pictured objects while distractor words vary in semantic relatedness.
- **Mathematical idea:** Naming latency or accuracy under interference is an indirect test of semantic activation; the group contrast separates access strategy from surface articulation.
- **What the paper reports:** Normal-hearing children show the typical semantic interference effect, while the implant group does not, consistent with different semantic organization or greater top-down control.
- **Limits:** The group, age, implant history, language, task, and interpretation of interference bound the result; absence of an effect is not a direct measurement of neural organization.

## 243. Subtyping Speech Errors in Childhood Speech Sound Disorders with Acoustic-to-Articulatory Speech Inversion

**Paper:** [Subtyping Speech Errors in Childhood Speech Sound Disorders with Acoustic-to-Articulatory Speech Inversion](https://www.isca-archive.org/interspeech_2025/benway25_interspeech.html)
**Taxonomy:** `people-variation-and-health / clinical-markers / clinical-speech-marker`
**Evidence:** D3 full-paper capture; PDF SHA-256 `9b0e95c7f7c42854aa709f68cece092b5c88bb35f048fa63a60c229b7b680878`; full-text SHA-256 `ecb4efd6bd23b702c24543689a41e87351968c9f72318d88acb08f6f8851c68c`.

- **Ordinary problem:** Clinicians need to distinguish different childhood speech-sound errors, but an acoustic recording does not directly show which articulator moved incorrectly.
- **Why it is hard:** Perceptually similar errors can arise from different vocal-tract configurations, and a predicted tract variable is only useful clinically if it separates meaningful error subtypes rather than creating uninterpretable coordinates.
- **Naive attempt:** Measure acoustic differences alone or treat an acoustic-to-articulatory inversion output as a direct clinical diagnosis.
- **Central move:** Use acoustic-to-articulatory inversion to obtain interpretable movement variables, then test subtype differences with a mixed-effects statistical model across children and target sounds.
- **Mechanism:** The study compares inverted articulatory trajectories for correct and erroneous /r/ and /s/ productions in children with speech sound disorders, models repeated observations with linear mixed effects, and asks which tract variables differ between perceptually defined subtypes.
- **Mathematical idea:** The inversion maps acoustics to estimated articulator variables; linear mixed modeling separates subtype effects from repeated-speaker and item variation. Statistical significance is evidence of group differences, not proof that the inversion recovered physical motion exactly.
- **What the paper reports:** The paper reports statistically significant articulatory differences among several perceptually salient /r/ and /s/ error subtypes and correct targets in American English.
- **Limits:** The study is limited to selected American-English child error types and an inversion model; clinical interpretability is demonstrated for these comparisons, not established for all disorders or speakers. No independent reproduction was performed.

## 244. Acoustic and Linguistic Biomarkers for Cognitive Impairment Detection from Speech

**Paper:** [Acoustic and Linguistic Biomarkers for Cognitive Impairment Detection from Speech](https://www.isca-archive.org/interspeech_2025/botelho25_interspeech.html)
**Taxonomy:** `people-variation-and-health / clinical-markers / clinical-speech-marker`
**Evidence:** D3 full-paper capture; PDF SHA-256 `0e19e2ff17930535386a253bfcc9cae382d027983efd3bc33f331932b39c7bf8`; full-text SHA-256 `068a10edeeff89dbf989fd2c1cab3ab53cdf850f557d374405cfb24c6940fe68`.

- **Ordinary problem:** Speech may contain signs of cognitive decline, but health signals must be separated from topic and class imbalance.
- **Why it is hard:** Clinical labels are scarce, the dementia class is small, and acoustic and linguistic evidence can disagree.
- **Naive attempt:** Choose one embedding or optimize overall accuracy.
- **Central move:** Combine acoustic, linguistic, knowledge-based, and neural representations, selecting complementary class-aware systems.
- **Mechanism:** PROCESS Challenge systems combine acoustic features, text features, LLM descriptors, Longformer, ECAPA-TDNN, and TRILLsson embeddings across three tasks.
- **Mathematical idea:** The study emphasizes UAF1 and class-specific F1 rather than accuracy alone.
- **What the paper reports:** Selected ensembles provide the strongest reported balance across train/development data and individual classes.
- **Limits:** Challenge data, demographic overlap, and missing metadata limit the claim; this is not clinical validation.

## 245. Pitfalls and Limits in Automatic Dementia Assessment

**Paper:** [Pitfalls and Limits in Automatic Dementia Assessment](https://www.isca-archive.org/interspeech_2025/braun25_interspeech.html)
**Taxonomy:** `people-variation-and-health / clinical-markers / clinical-speech-marker`
**Evidence:** D3 full-paper capture; PDF SHA-256 `d25917a052e350b1aff677d162e535728c3eb61781b8b02c284a52fce9616959`; full-text SHA-256 `eb9ec658adda613147087d9e2a2924c7e077071f1a1e850a9b2e7fd170c70366`.

- **Ordinary problem:** A speech-based dementia score can correlate with human scores while still being systematically wrong for some people.
- **Why it is hard:** Word-naming performance and fallback rules can make severe impairment look easier to detect than mild impairment or healthy speech.
- **Naive attempt:** Report one overall correlation and treat it as equally meaningful across severity groups.
- **Central move:** Inspect the automated Syndrom-Kurz-Test pipeline by subgroup, transcription quality, item type, and fallback behavior rather than relying on one aggregate number.
- **Mechanism:** The analysis links scoring artifacts to speech production decline, ASR errors, and fallback handling; apparent agreement can therefore arise from the test design.
- **Mathematical idea:** The paper turns evaluation from a single correlation into a chain of measurement decisions whose errors can favor particular groups.
- **What the paper reports:** The paper reports high overall correlation but weaker behavior for healthy and mildly impaired groups and identifies overoptimistic correlations for severely impaired speakers.
- **Limits:** This is an analysis of one standardized assessment and its data; it warns against clinical claims, not a universal ranking of dementia-screening systems.

## 246. Perception of Emotional Speech by Individuals with High Borderline Personality Features

**Paper:** [Perception of Emotional Speech by Individuals with High Borderline Personality Features](https://www.isca-archive.org/interspeech_2025/chen25c_interspeech.html)
**Taxonomy:** `people-variation-and-health / clinical-markers / clinical-speech-marker`
**Evidence:** D3 full-paper capture; PDF SHA-256 `8c01721907ec20ad98b3e655a5ae25715d9af44b709af4f279d2dfa64512ec3d`; full-text SHA-256 `11c04554aa630ce5a1195a8f7b3b637b34b3f2d1e65764f54f37707098aa5cd7`.

- **Ordinary problem:** Listeners with different emotional sensitivities may not interpret the same emotional speech in the same way, especially when the emotion is weak or neutral.
- **Why it is hard:** Emotion perception depends on both the acoustic signal and the listener; changing fundamental frequency creates controlled intensity, but psychological traits and confidence can affect labels.
- **Naive attempt:** Assume one universal emotion decoder or infer a listener’s clinical state directly from one recognition error.
- **Central move:** Present Mandarin emotional speech at controlled intensities and compare emotion-identification accuracy and confusions for participants with high and low borderline-personality features.
- **Mechanism:** The paper studies emotional-speech perception in listeners with high borderline personality features.
- **Mathematical idea:** The listener is part of the speech-perception system: the same acoustic cue can be weighted differently depending on emotional regulation and the listener’s internal expectations.
- **What the paper reports:** High-feature participants were less accurate for neutral speech and high-intensity happy speech, with distinct confusion patterns and marginally higher confidence for angry speech.
- **Limits:** Mandarin synthetic stimuli, university participants, self-report grouping, F0 manipulation, and perceptual task bound generalization; the findings do not diagnose BPD or explain all underlying causes.

## 247. Predicting Adolescent Suicidal Risk from Multi-task-based Speech: An Ensemble Learning Approach

**Paper:** [Predicting Adolescent Suicidal Risk from Multi-task-based Speech: An Ensemble Learning Approach](https://www.isca-archive.org/interspeech_2025/chen25o_interspeech.html)
**Taxonomy:** `people-variation-and-health / clinical-markers / clinical-speech-marker`
**Evidence:** D3 full-paper capture; PDF SHA-256 `53c22053fff97fe1d09eeeb88d23b71e1d4973794354e1b2ef33dc9e77235262`; full-text SHA-256 `7c1a07316322c705e0910cd3c57a1d7084b343ce37bcee1a3e6febeac4ac0f58`.

- **Ordinary problem:** A screening system should use speech to flag possible adolescent suicide risk when interviews and expert time are limited.
- **Why it is hard:** Risk is continuous and multidimensional, while speech carries both acoustic behavior and what the person says; one feature family can miss the other.
- **Naive attempt:** Train one binary classifier on a single acoustic summary and treat its score as a clinical decision.
- **Central move:** Combine acoustic and semantic features across several task models, then use a nested voting ensemble to stabilize the prediction.
- **Mechanism:** OpenSmile and Emotion2Vec supply acoustic representations, a fine-tuned Chinese BERT supplies semantic features, and XGBoost/SVM-style base models are combined after Bayesian hyperparameter search.
- **Mathematical idea:** An ensemble votes across partially different predictors; recall and F1 expose the cost of missing risk more directly than accuracy alone.
- **What the paper reports:** On 600 Chinese adolescents, the paper reports test accuracy .63, recall .74, and F1 about .67.
- **Limits:** This is a screening model on one challenge dataset, not a diagnosis or safety-tested intervention; age, language, labels, privacy, calibration, and external validation constrain the claim.

## 248. Comparative Evaluation of Acoustic Feature Extraction Tools for Clinical Speech Analysis

**Paper:** [Comparative Evaluation of Acoustic Feature Extraction Tools for Clinical Speech Analysis](https://www.isca-archive.org/interspeech_2025/choi25h_interspeech.html)
**Taxonomy:** `people-variation-and-health / clinical-markers / clinical-speech-marker`
**Evidence:** D3 full-paper capture; PDF SHA-256 `e221953deaf74e1d91ba9746a8eb4c8b93db25ec7b1ced8e933196247d4966ac`; full-text SHA-256 `7d3ef1bf07b8ff6848123c8afc693e577e4fc06fa2201d154b1bd2b2405ed7ec`.

- **Ordinary problem:** Clinical speech studies need acoustic features that mean the same thing when extracted by different tools.
- **Why it is hard:** OpenSMILE, Praat, and Librosa can implement nominally similar features differently, changing a model's clinical conclusion.
- **Naive attempt:** Use one toolkit and treat its feature names as interchangeable with another toolkit's names.
- **Central move:** Standardize extraction settings, compare tools directly, and test whether disagreements change group classification.
- **Mechanism:** Three toolkits are applied to 77 schizophrenia-spectrum and 87 control speakers; correlations and classification performance are compared.
- **Mathematical idea:** Feature correlations, agreement for F0/formants, and AUC reveal whether a feature is reproducible and useful for discrimination.
- **What the paper reports:** F0 percentile agreement is high, but F0 variation and formants can disagree or even correlate negatively; F0 mean, HNR, and MFCC1 exceed AUC .70 in the reported classification.
- **Limits:** The clinical groups, recordings, parameter choices, and tool versions define the boundary; no clinical diagnosis or deployment safety follows from these correlations.

## 249. Test-Time Training for Speech-based Depression Detection

**Paper:** [Test-Time Training for Speech-based Depression Detection](https://www.isca-archive.org/interspeech_2025/dumpala25_interspeech.html)
**Taxonomy:** `people-variation-and-health / clinical-markers / clinical-speech-marker`
**Evidence:** D3 full-paper capture; PDF SHA-256 `7cb1cd64f77c89f84b93cef4a369bad6b4f6cf1180b2047abb12f663ccfb58a1`; full-text SHA-256 `c093369c1d8fdb5da0462b438603764c6b7a97bd066b41a9c327628e37f7c566`.

- **Ordinary problem:** A depression detector trained in one recording setting should remain useful when test speech comes from another environment, demographic mix, or dataset.
- **Why it is hard:** Noise, gender, age, and collection procedures change the speech distribution without changing the clinical question.
- **Naive attempt:** Train once on a clean source dataset and assume the test distribution is the same.
- **Central move:** Adapt the model at test time using the incoming unlabeled speech so its internal features respond to the new distribution.
- **Mechanism:** The study applies test-time training to a speech-based depression detector and tests shifts from noise, gender, and dataset/curation differences.
- **Mathematical idea:** Performance under each shift is compared before and after adaptation; the important object is the distribution gap, not only the average source score.
- **What the paper reports:** The paper reports substantial performance improvement under the tested shifts.
- **Limits:** The task is a clinical screening proxy, not a diagnosis; adaptation stability, labels in deployment, privacy, and external clinical validation remain open.

## 250. ADCeleb: A Longitudinal Speech Dataset from Public Figures for Early Detection of Alzheimer’s Disease

**Paper:** [ADCeleb: A Longitudinal Speech Dataset from Public Figures for Early Detection of Alzheimer’s Disease](https://www.isca-archive.org/interspeech_2025/gao25b_interspeech.html)
**Taxonomy:** `people-variation-and-health / clinical-markers / clinical-speech-marker`
**Evidence:** D3 full-paper capture; PDF SHA-256 `077dbdaa2f209046b6158192cf60ace99b8b32eed3f6f7ebaef89e0433ad3e6b`; full-text SHA-256 `33d6eeba3cebabbb97234c8f8c0bbaf8e1d29007a7037993f76f16d2dc44125d`.

- **Ordinary problem:** Early cognitive decline may alter language and speech before diagnosis, but a model needs longitudinal, naturalistic recordings rather than a single clean clinical utterance.
- **Why it is hard:** Public recordings contain changing topics, speakers, video quality, age, and demographic imbalance; a high-dimensional representation can classify a person while hiding which speech change carries the signal.
- **Naive attempt:** Train on random speech segments and report one accuracy number without keeping speakers separated between training and testing or distinguishing acoustic from linguistic evidence.
- **Central move:** Build a longitudinal celebrity speech corpus, balance AD and control groups across relevant demographics, extract frozen acoustic and linguistic representations, and evaluate them with speaker-disjoint nested cross-validation and fusion.
- **Mechanism:** ADCeleb contains public spontaneous recordings from 40 people with AD and 40 controls, with intervals two and one years before diagnosis. Acoustic embeddings include x-vectors, TRILLsson, Wav2Vec2, HuBERT, and Whisper; linguistic embeddings include multilingual encoders. PCA and PLDA classify speakers, and selected acoustic/linguistic predictions are averaged.
- **Mathematical idea:** The evaluation is speaker-level nested 10-fold cross-validation with accuracy, F1, sensitivity, specificity, and AUC. Wav2Vec2 acoustic accuracy is 0.67 and 0.72 at the two intervals; the best linguistic models reach 0.73 and 0.75; fusion reaches 0.80 at the nearer interval.
- **What the paper reports:** The authors report that linguistic representations are stronger earlier, while acoustic information contributes more near the year of diagnosis; fusion improves the nearer interval to 0.80 accuracy.
- **Limits:** The corpus uses public figures, YouTube recordings, 40 AD and 40 control speakers, and imperfect observational labels. It is a dataset and baseline study, not a clinical diagnostic validation; author-reported results were not independently reproduced.

## 251. Optimizing Pause Context in Fine-Tuning Pre-trained Large Language Models for Dementia Detection

**Paper:** [Optimizing Pause Context in Fine-Tuning Pre-trained Large Language Models for Dementia Detection](https://www.isca-archive.org/interspeech_2025/ke25_interspeech.html)
**Taxonomy:** `people-variation-and-health / clinical-markers / clinical-speech-marker`
**Evidence:** D3 full-paper capture; PDF SHA-256 `ce626c00027b720202c96d268e3b2f47e7e8a2f997f9121db0884ef6800c42f6`; full-text SHA-256 `0022a87c8abd5c4319c3dfdb2d271c4a92398743b1ba1ee3fa855cc7432de491`.

- **Ordinary problem:** A clinical speech detector may need to use pauses as signs of cognitive change without assuming that one duration threshold works for every language or recording protocol.
- **Why it is hard:** Pause meaning depends on where the pause occurs and how its duration is represented to a language model; the same insertion rule can help one task and hurt another.
- **Naive attempt:** Add every pause as a fixed token or use a threshold borrowed from another corpus.
- **Central move:** Insert between-segment pause context into automatic transcripts and tune the pause-duration representation for each classification task.
- **Mechanism:** Cantonese elderly speech from CU-Marvel is transcribed, pause context is fused into transformer input, and binary dementia tasks are compared under alternative pause groupings.
- **Mathematical idea:** The pause is treated as structured context attached to a linguistic boundary; classification accuracy and F1 test whether that context adds clinically useful signal.
- **What the paper reports:** The paper reports that optimized between-segment pause patterns improve detection and that different tasks prefer different pause representations.
- **Limits:** The corpus, language, age group, transcription quality, diagnostic labels, and pause definitions bound the result; this is not a validated clinical biomarker or a causal account of dementia.

## 252. Leveraging Ordinal Information for Speech-based Depression Classification

**Paper:** [Leveraging Ordinal Information for Speech-based Depression Classification](https://www.isca-archive.org/interspeech_2025/zuo25_interspeech.html)
**Taxonomy:** `people-variation-and-health / clinical-markers / clinical-speech-marker`
**Evidence:** D3 full-paper capture; PDF SHA-256 `3410e0cf07603dd689c199aa9c3608bc57a359f959519556f11f76e3d9978cc7`; full-text SHA-256 `3c133c638a665615c41f5e5964508d1240db5b7b37b669913c8b30a73c5e97b2`.

- **Ordinary problem:** Depression severity comes in ordered levels, but a detector often throws away that order by labeling everyone only depressed or not depressed.
- **Why it is hard:** A mild case is closer to a moderate case than to no symptoms, and binary loss cannot express that distance.
- **Naive attempt:** Binarize the score and train an ordinary yes/no classifier.
- **Central move:** Create ordered thresholds so the model learns several nested decisions and a latent representation that respects severity order.
- **Mechanism:** Speech-based depression scores are converted into K threshold tasks; an ordinal loss trains the model across these linked boundaries.
- **Mathematical idea:** The target is an ordered scale, not a collection of unrelated labels; threshold consistency lets errors near a boundary differ from errors across the full range.
- **What the paper reports:** The ordinal method outperforms reported state-of-the-art depression-detection methods in the paper's experiments.
- **Limits:** The clinical scale, speakers, labels, dataset, threshold choices, and evaluation metrics bound the result; better ordinal prediction is not diagnosis or clinical validation.

## 253. A Study on Speech Assessment with Visual Cues

**Paper:** [A Study on Speech Assessment with Visual Cues](https://www.isca-archive.org/interspeech_2025/ahmed25_interspeech.html)
**Taxonomy:** `people-variation-and-health / human-centered-accessibility / listener-effort`
**Evidence:** D3 full-paper capture; PDF SHA-256 `597b0fab2ec507b35047a15116a4ea12244fcfe6953afaa7e879f567c8d8a3f0`; full-text SHA-256 `f6ec3a67222d9a3cc6d5aae25a07b1e931813366f38261d53833c774753d0be7`.

- **Ordinary problem:** Speech quality should be estimated when no clean reference exists, using visual context that may help explain what is audible.
- **Why it is hard:** Audio-only proxies can miss visible articulatory or scene evidence, while PESQ/STOI are imperfect targets rather than human usefulness itself.
- **Naive attempt:** Predict a quality score from a single audio stream and treat the proxy metric as intelligibility.
- **Central move:** Fuse STFT audio features with visual embeddings in a dual-branch CNN-BLSTM attention model and jointly predict PESQ and STOI.
- **Mechanism:** The model aligns spectral and visual information before multi-task regression; LCC compares predicted and reference proxy scores under noise.
- **Mathematical idea:** Multimodal evidence can improve prediction of a proxy while still inheriting the proxy’s limitations and the visual/audio distribution.
- **What the paper reports:** On LRS3-TED with DEMAND noise, the paper reports higher LCC than audio-only baselines for PESQ and STOI under seen noise.
- **Limits:** Seen-noise conditions, proxy targets, visual availability, dataset, and correlation metric limit transfer; proxy prediction is not a listener study.

## 254. Can We Trust Machine Learning? The Reliability of Features from Open-Source Speech Analysis Tools for Speech Modeling

**Paper:** [Can We Trust Machine Learning? The Reliability of Features from Open-Source Speech Analysis Tools for Speech Modeling](https://www.isca-archive.org/interspeech_2025/chowdhury25_interspeech.html)
**Taxonomy:** `people-variation-and-health / human-centered-accessibility / user-control-and-consent`
**Evidence:** D3 full-paper capture; PDF SHA-256 `583697ce22a6c66bcddb986f75cbc3c9538ce206a54892c5834d598228fb23c4`; full-text SHA-256 `e9bf83ba9e40fbde49ed4b66c469aae5b09b9aee7f8da3b839205e87385385d3`.

- **Ordinary problem:** Speech features used in behavioral or clinical models should measure the intended behavior consistently across people and contexts.
- **Why it is hard:** Open-source tools can disagree, and those disagreements can change model performance unevenly across demographic groups.
- **Naive attempt:** Extract features from a familiar toolkit and assume the outputs are reliable.
- **Central move:** Compare tools directly in the target population and test how feature differences alter models and group behavior.
- **Mechanism:** OpenSMILE and Praat features are evaluated on adolescents with autism from audio-visual recordings, with model performance compared across contexts and demographics.
- **Mathematical idea:** Feature agreement and downstream classification are both measured; this connects measurement reliability to fairness rather than stopping at correlation.
- **What the paper reports:** The paper reports considerable tool variation that influences model performance across context and demographic groups.
- **Limits:** The population, features, tools, and behavioral tasks define the boundary; the study does not identify one universally correct toolkit.

## 255. EAA: Emotion-Aware Audio Large Language Models with Dual Cross-Attention and Context-Aware Instruction Tuning

**Paper:** [EAA: Emotion-Aware Audio Large Language Models with Dual Cross-Attention and Context-Aware Instruction Tuning](https://www.isca-archive.org/interspeech_2025/du25b_interspeech.html)
**Taxonomy:** `people-variation-and-health / human-centered-accessibility / listener-effort`
**Evidence:** D3 full-paper capture; PDF SHA-256 `0ab68c5ba71dec71429f4350f11f91b5ed7cd3992b289439a315e45c7e37eea6`; full-text SHA-256 `70271f6b06e6fb8a09efb169cd3a3f09533aa716989634ab4bab4aa31afeb496`.

- **Ordinary problem:** An emotion-aware speech model should combine audio and context without confusing fluent output with reliable affect recognition.
- **Why it is hard:** Emotion is ambiguous and context-dependent; language models can generate plausible unsupported explanations.
- **Naive attempt:** Use one label stream or infer emotion from transcripts alone.
- **Central move:** Use dual cross-attention and context-aware instruction tuning for emotion-aware audio-language modeling.
- **Mechanism:** Cross-attention aligns acoustic and conversational representations.
- **Mathematical idea:** The relevant object is the listener-effort evidence described by the paper's mechanism: Cross-attention aligns acoustic and conversational representations.
- **What the paper reports:** The paper reports EAA results for emotion-aware audio large language modeling.
- **Limits:** Labels, prompts, audio quality, model, and human agreement bound transfer.

## 256. Speech stimulus design to study the neural coding of speech and the impact of cochlear synaptopathy

**Paper:** [Speech stimulus design to study the neural coding of speech and the impact of cochlear synaptopathy](https://www.isca-archive.org/interspeech_2025/gaudrain25_interspeech.html)
**Taxonomy:** `people-variation-and-health / human-centered-accessibility / accessibility-fit`
**Evidence:** D3 full-paper capture; PDF SHA-256 `3792842a00a0568a896bb994698311bd4f38ae14996d120f235de1b786166d46`; full-text SHA-256 `b4ad923ae386b430e4662bf457406c6c708c358c1a2360e463e3bb183cb15b4f`.

- **Ordinary problem:** A hearing study needs speech sounds that behave like natural speech but can still isolate one hypothesized neural coding mechanism.
- **Why it is hard:** Ordinary speech changes many acoustic dimensions at once, while simple tones are easy to control but do not show how the mechanism operates during speech; hearing loss may affect neural coding without appearing on a pure-tone audiogram.
- **Naive attempt:** Use only artificial tones for control or use natural recordings and accept that several acoustic causes change together.
- **Central move:** Analyze and resynthesize speech so temporal fine structure and other dimensions can be parametrically varied while preserving naturalistic speech cues.
- **Mechanism:** The paper designs analysis-resynthesis speech stimuli to test phase-locking/temporal-fine-structure coding and accommodates multi-center studies across species, methods, and languages, including cochlear synaptopathy conditions.
- **Mathematical idea:** The stimulus is an experimental instrument: a waveform is decomposed, controlled dimensions are altered, and the result is resynthesized; psychophysical or neural responses can then be attributed more narrowly than with natural recordings alone.
- **What the paper reports:** The paper reports a design framework for controlled naturalistic stimuli suitable for studying the target coding mechanism and its impairment in cochlear synaptopathy.
- **Limits:** Stimulus fidelity, resynthesis artifacts, listener population, language, and study protocol bound the inference; a designed cue isolates a mechanism only insofar as unedited cues remain controlled.

## 257. Evaluating Speech Enhancement Performance Across Demographics and Language

**Paper:** [Evaluating Speech Enhancement Performance Across Demographics and Language](https://www.isca-archive.org/interspeech_2025/giraldo25_interspeech.html)
**Taxonomy:** `people-variation-and-health / human-centered-accessibility / listener-effort`
**Evidence:** D3 full-paper capture; PDF SHA-256 `45ffdef7daac6c3edcfb326d0151655642c78d96afe1ef16bc74d8b1c2c414a3`; full-text SHA-256 `0c257be381152e674324ebcd539596571a6b17e1ffb2b085f6ef2c53cf603060`.

- **Ordinary problem:** Test whether speech-enhancement rankings survive demographic, language, and realistic data variation.
- **Why it is hard:** VoiceBank-DEMAND is small, young, mostly English, and simulated; a model can score well there while damaging speech for other populations.
- **Naive attempt:** Use one simplified benchmark and optimize a signal-quality metric as though it fully represents intelligibility.
- **Central move:** Evaluate enhancement systems on multilingual crowdsourced CommonPhone data with age, gender, language, content-retention, and information-loss analyses.
- **Mechanism:** Quality, intelligibility, word error, and phoneme error measures are compared across demographic and language conditions; samples with high WER are examined for information loss.
- **Mathematical idea:** PESQ-like quality scores and WER can disagree; this exposes the tradeoff between perceptual quality and preserved linguistic content.
- **What the paper reports:** The paper reports performance variation across demographics/languages and warns that model rankings on VoiceBank-DEMAND do not transfer directly.
- **Limits:** The authors still note benchmark simplification and possible metric overfitting; dataset diversity does not by itself prove universal fairness.

## 258. Towards Inclusive and Fair ASR: Insights from the SAPC Challenge for Optimizing Disordered Speech Recognition

**Paper:** [Towards Inclusive and Fair ASR: Insights from the SAPC Challenge for Optimizing Disordered Speech Recognition](https://www.isca-archive.org/interspeech_2025/gohider25_interspeech.html)
**Taxonomy:** `people-variation-and-health / human-centered-accessibility / accessibility-fit`
**Evidence:** D3 full-paper capture; PDF SHA-256 `4874904394f25eef2e84c59725a7f932da72e561716a5dbdf568e77abedd3652`; full-text SHA-256 `c42ced5dc2eb98cabb8e13664ddcee371d859c5d2d337c1e9fe3376e780a8c52`.

- **Ordinary problem:** ASR should transcribe disordered and dysarthric speech rather than silently serving only speakers whose voices match ordinary training data.
- **Why it is hard:** Impaired speech is variable and scarce, and disfluencies can be mistaken for recognition errors or erased by a system tuned for fluent speech.
- **Naive attempt:** Apply a high-performing typical-speech recognizer and compare only its overall WER.
- **Central move:** Evaluate strong contextual ASR architectures on a dedicated impaired-speech corpus and inspect whether their different context mechanisms help.
- **Mechanism:** ContextNet and Parakeet are tested on Speech Accessibility Project challenge subsets; WER is compared across the challenge conditions.
- **Mathematical idea:** Word error rate counts substitutions, insertions, and deletions; it turns a listener's transcription burden into a measurable but incomplete quantity.
- **What the paper reports:** The paper reports WER 10.06% and 11.8% on the two test subsets, with Parakeet slightly ahead of ContextNet.
- **Limits:** Challenge data, speaker impairment profiles, transcripts, and WER define the boundary; fairness across disorders, user control, and clinical usefulness remain unestablished.

## 259. Can ASR generate valid measures of child reading fluency?

**Paper:** [Can ASR generate valid measures of child reading fluency?](https://www.isca-archive.org/interspeech_2025/harmsen25_interspeech.html)
**Taxonomy:** `people-variation-and-health / human-centered-accessibility / accessibility-fit`
**Evidence:** D3 full-paper capture; PDF SHA-256 `cb6a2a4d5cc531bb69165de6b63c6018a0220f3551e2d1ed6d64fe61ace214fb`; full-text SHA-256 `597a47850783bb5fcd06130300b01876e996000789b8c153bf967186d2d41a92`.

- **Ordinary problem:** Reading fluency assessment should capture accuracy, smoothness, phrasing, and pacing without manually scoring every child.
- **Why it is hard:** ASR and timing errors can corrupt the educational measure, and agreement with transcript proxies is not the same as instructional validity.
- **Naive attempt:** Use words-correct-per-minute alone or treat an accurate transcript as sufficient evidence that every fluency measure is valid.
- **Central move:** Extract fifteen measures from ASR transcripts and timings, then compare them with the same measures from human transcripts.
- **Mechanism:** The study evaluates 244 recordings from 131 Dutch children aged 6–13, compares four ASR systems, and correlates automatic and human-derived fluency measures.
- **Mathematical idea:** WER, timing F1, and Pearson correlations quantify separate links from audio to educational measure; 12 of 15 measures show strong correlations.
- **What the paper reports:** The best reported system has WER 12.3% and timing F1 0.82; twelve measures meet r ≥ 0.7.
- **Limits:** Dutch child reading, fixed texts, age distribution, ASR choice, and transcript comparison limit generalization; intervention or diagnosis validity is not established.

## 260. Hearing deficits of transformer-based ASR for anechoic and spatial signals

**Paper:** [Hearing deficits of transformer-based ASR for anechoic and spatial signals](https://www.isca-archive.org/interspeech_2025/hoffner25_interspeech.html)
**Taxonomy:** `people-variation-and-health / human-centered-accessibility / listener-effort`
**Evidence:** D3 full-paper capture; PDF SHA-256 `50d49d6d27a39f28367dad2a3698cb17cc9bc804f6b6cf8c0ed14fe49b5ec0ab`; full-text SHA-256 `34fe14dbb134be8fc62be5b5637bf545da6a248959511e2ac9b832adb6647f83`.

- **Ordinary problem:** ASR and humans should be compared on the same speech-in-noise task rather than assuming low WER means human-like hearing.
- **Why it is hard:** Human recognition depends on thresholds, spatial cues, rooms, and masking; model size changes errors without modeling those mechanisms.
- **Naive attempt:** Report ASR WER in clean speech as a proxy for hearing performance.
- **Central move:** Estimate speech-reception thresholds from controlled sentences in noise for ASR models and humans.
- **Mechanism:** Whisper models are tested on anechoic and spatial signals; thresholds come from WER curves at 50% error.
- **Mathematical idea:** SRT and psychometric slope make the human-machine gap explicit rather than hiding it in average WER.
- **What the paper reports:** Model size improves ASR thresholds, but the gap changes with language, room, and spatial signals.
- **Limits:** Whisper versions, German/English material, steady noise, and laboratory setup limit claims.

## 261. Unifying Listener Scoring Scales: Comparison Learning Framework for Speech Quality Assessment and Continuous Speech Emotion Recognition

**Paper:** [Unifying Listener Scoring Scales: Comparison Learning Framework for Speech Quality Assessment and Continuous Speech Emotion Recognition](https://www.isca-archive.org/interspeech_2025/hu25l_interspeech.html)
**Taxonomy:** `people-variation-and-health / human-centered-accessibility / listener-effort`
**Evidence:** D3 full-paper capture; PDF SHA-256 `f5d5ac83a5c1b084f927c8cc9000990691f3048a4647542e8e321adbf6aa6536`; full-text SHA-256 `b6cf5dfc65b60690b9eb44a61dc67c55f65ba978a3197c5cbee0cf2b8e32ef9f`.

- **Ordinary problem:** A speech-quality or emotion model should account for the fact that listeners use different personal rating scales.
- **Why it is hard:** Averaging ordinal ratings can invent distances and erase systematic listener differences.
- **Naive attempt:** Average all ratings into one target and train a model to reproduce that mean.
- **Central move:** Learn a unified listener scale from pairwise comparisons so the ordering of utterances is preserved without assuming numeric distances.
- **Mechanism:** The method is evaluated on speech quality assessment and continuous emotion recognition, comparing a unified comparison-based scale with mean-listener and multi-scale approaches.
- **Mathematical idea:** Pairwise comparison models order utterances; the central mathematical choice is to preserve ordinal relationships rather than average incompatible numbers.
- **What the paper reports:** The paper reports improved prediction performance and robustness on both tasks.
- **Limits:** Listener panels, rating prompts, comparison construction, and datasets bound the result; agreement and usefulness for new listener populations remain open.

## 262. Does effortful speech production indicate communication difficulty caused by noise and hearing aid support?

**Paper:** [Does effortful speech production indicate communication difficulty caused by noise and hearing aid support?](https://www.isca-archive.org/interspeech_2025/huttner25_interspeech.html)
**Taxonomy:** `people-variation-and-health / human-centered-accessibility / accessibility-fit`
**Evidence:** D3 full-paper capture; PDF SHA-256 `2b187da4f34acbce51b19459ad28b8304cdfc16e165ab62e180777e42623d22a`; full-text SHA-256 `64e43c5071ad16a195ad1645a40ad9b31dd80bcdd72696c6ec3810a98f5fb55c`.

- **Ordinary problem:** Communication difficulty is a lived interactional problem: noise, hearing loss, hearing aids, and the effort of speaking may change how successfully two people can coordinate.
- **Why it is hard:** A person's vocal level or turn-taking behavior can reflect both the acoustic environment and the person's adaptation, so a single acoustic measure cannot be assumed to equal experienced difficulty.
- **Naive attempt:** Measure hearing thresholds or speech level alone and use them as a proxy for how hard the conversation felt.
- **Central move:** Record paired conversations across quiet/noise and hearing-aid conditions, collect participants' difficulty judgments, and test which speech and interaction measures predict those judgments.
- **Mechanism:** The study pairs 44 normal-hearing and hearing-impaired participants in task-based conversations in quiet and 70 dB noise, with the hearing-impaired group tested with and without hearing aids; F1, vocal level, and turn-taking variability are modeled against questionnaires.
- **Mathematical idea:** The target is a human report conditioned on dyad, noise, device, and turn structure; regression links observable speech behavior to experience while keeping the experience measure distinct from the signal.
- **What the paper reports:** The paper reports that higher vocal level and interaction measures predict communication difficulty for hearing-impaired participants under relevant conditions.
- **Limits:** Small dyadic sample, task design, questionnaire, hearing-aid settings, and acoustic noise bound the result; a predictor of reported difficulty is not a universal clinical measure or causal explanation.

## 263. Crowdsourcing MUSHRA Tests in the Age of Generative Speech Technologies: A Comparative Analysis of Subjective and Objective Testing Methods

**Paper:** [Crowdsourcing MUSHRA Tests in the Age of Generative Speech Technologies: A Comparative Analysis of Subjective and Objective Testing Methods](https://www.isca-archive.org/interspeech_2025/lechler25_interspeech.html)
**Taxonomy:** `people-variation-and-health / human-centered-accessibility / listener-effort`
**Evidence:** D3 full-paper capture; PDF SHA-256 `f93a9f4de93bb1a0701ef3b4871f20cbeacf89f549601d1e91b27b6e45c7710b`; full-text SHA-256 `a66fc92c0bdc379902f51db042753c9d95ad50f4cc752368c7a11a4799fe1398`.

- **Ordinary problem:** Generative speech codecs need listening tests sensitive enough to detect subtle artifacts, but expert MUSHRA studies are expensive and objective metrics can mis-rank new systems.
- **Why it is hard:** Crowdsourced listeners vary by platform and expertise, while traditional metrics were designed for older signal distortions.
- **Naive attempt:** Use only objective metrics during development or reserve all listening tests for experts at the end.
- **Central move:** Adapt MUSHRA for non-experts online, compare platforms with expert data, and test whether objective metrics agree with people.
- **Mechanism:** The paper compares MTurk, Prolific, and expert ratings, measures test-retest reliability, and evaluates six objective metrics on generative speech codecs.
- **Mathematical idea:** MUSHRA ratings, reliability, platform effects, and metric-to-human alignment are separate quantities; collapsing them into one score hides the evaluation problem.
- **What the paper reports:** The paper reports platform-specific bias, reasonable crowdsourced comparisons under its protocol, and that traditional metrics undervalue generative models.
- **Limits:** The result is bounded to the codecs, platforms, listener recruitment, and six metrics tested; other populations and model families remain open.

## 264. Web-Based Application for Real-Time Biofeedback of Vocal Resonance in Gender-Affirming Voice Training: Design and Usability Evaluation

**Paper:** [Web-Based Application for Real-Time Biofeedback of Vocal Resonance in Gender-Affirming Voice Training: Design and Usability Evaluation](https://www.isca-archive.org/interspeech_2025/mcallister25_interspeech.html)
**Taxonomy:** `people-variation-and-health / human-centered-accessibility / user-control-and-consent`
**Evidence:** D3 full-paper capture; PDF SHA-256 `370a0fbf351a6a19a7b25c0a5caed9963baa6b5592deed81325a16de5e769f47`; full-text SHA-256 `91e65cca48cfb371e71df4925739d18b76b7539cbe51a55bc998f471f70868a4`.

- **Ordinary problem:** Voice training is an interactional skill, so a useful tool must show a learner what changed while they speak and remain usable in practice.
- **Why it is hard:** Resonance is felt and heard, but a display can overwhelm a learner or turn a gradual skill into a misleading single score.
- **Naive attempt:** Show raw spectra or prescribe a fixed target value and assume users can interpret it.
- **Central move:** Build a browser tool that gives real-time vocal-resonance biofeedback and evaluate whether intended users can complete tasks and understand the feedback.
- **Mechanism:** The study combines real-time acoustic analysis, visual feedback, and a usability evaluation for gender-affirming voice training.
- **Mathematical idea:** The design treats feedback as part of a human learning loop: measurement matters only if a person can notice it, interpret it, and act on it.
- **What the paper reports:** The paper reports a working web application and usability findings supporting its use as a training aid.
- **Limits:** Small usability sample, task design, browser/audio conditions, and self-report limit claims about long-term learning or clinical outcomes.

## 265. Accessible Delivery of Visual-Acoustic Biofeedback for Speech Sound Disorder

**Paper:** [Accessible Delivery of Visual-Acoustic Biofeedback for Speech Sound Disorder](https://www.isca-archive.org/interspeech_2025/mcallister25b_interspeech.html)
**Taxonomy:** `people-variation-and-health / human-centered-accessibility / accessibility-fit`
**Evidence:** D3 full-paper capture; PDF SHA-256 `389575b43bb2e0d05423a71a1789d3a633f0b03461c728de811d0e2f9f204f7e`; full-text SHA-256 `c0da1bcd374dc74e8fa8079e1ba508570c5d9fa4cc9162228bddc4e32be49fd0`.

- **Ordinary problem:** A child practicing a difficult speech sound needs immediate, interpretable feedback that does not require a specialist or expensive equipment at every trial.
- **Why it is hard:** The learner must connect a changing acoustic spectrum to a vocal-tract target, while remote audio processing can add delay, lose frequency detail, or be distorted by browser processing.
- **Naive attempt:** Show a generic waveform or send audio through a video-call pipeline and expect the child to infer which articulatory change is needed.
- **Central move:** Make the source-filter structure visible: display a real-time LPC spectrum alongside a target resonance, with adaptive practice and clinician-mediated feedback.
- **Mechanism:** JavaScript computes LPC coefficients with Levinson-Durbin recursion, renders the spectral envelope and peaks, and supports randomized word/syllable routines, clinician scoring, gamification, and local-device WebRTC processing.
- **Mathematical idea:** LPC models the signal as X(z)=H(z)E(z), with an all-pole vocal-tract filter H(z)=1/A(z); peak locations approximate formant resonances used as the feedback target.
- **What the paper reports:** The staRt iOS/web system provides real-time visual-acoustic biofeedback for /r/ training and reports broad uptake; local processing avoids telepractice loss of frequency resolution and latency.
- **Limits:** The current target is mainly English /r/, peak-picking and formant tracking are not yet stable enough for automated feedback across vocal-tract sizes, and clinical efficacy is not established by this technical description.

## 266. Concurrent Speech and Auditory Tag Clouds for Non-Visual Web Interaction

**Paper:** [Concurrent Speech and Auditory Tag Clouds for Non-Visual Web Interaction](https://www.isca-archive.org/interspeech_2025/merzougui25_interspeech.html)
**Taxonomy:** `people-variation-and-health / human-centered-accessibility / accessibility-fit`
**Evidence:** D3 full-paper capture; PDF SHA-256 `8cc93a7f3bd56e9d84e198404df0db56e3589bf021f8a17896a0d8de9eda229b`; full-text SHA-256 `72b90c628549d2fb318d34dbae8360b20be8ffc659f6118ed2431795dc50abc3`.

- **Ordinary problem:** A blind or visually impaired reader needs to skim a structured web document without relying on a visual page layout.
- **Why it is hard:** Transposing headings, roles, and relationships into sound can overload serial listening; the interface must preserve structure while allowing rapid selective attention.
- **Naive attempt:** Read the page linearly from top to bottom or emit every element with equal salience.
- **Central move:** Represent document semantics as an interactive auditory tag cloud, using concurrent speech and spatial/continuous auditory guidance to let the listener scan and select structure.
- **Mechanism:** TagThunder extracts morpho-dispositional semantics and maps tags to concurrent speech streams and guiding stimuli; discrete and continuous interaction conditions test structured information scanning.
- **Mathematical idea:** The system treats auditory channels as a limited display: timing, concurrency, and user selection determine which semantic items are attended rather than merely transcribed.
- **What the paper reports:** The paper presents the experimental framework and reports feasibility for non-visual web skimming through auditory tag-cloud interaction.
- **Limits:** The evaluation is interaction-specific, auditory clutter and learning effects matter, and accessibility promise is not equivalent to demonstrated performance across blind users, browsers, languages, or real browsing tasks.

## 267. What Do Humans Hear When Interacting? Experiments on Selective Listening for Evaluating ASR of Spoken Dialogue Systems

**Paper:** [What Do Humans Hear When Interacting? Experiments on Selective Listening for Evaluating ASR of Spoken Dialogue Systems](https://www.isca-archive.org/interspeech_2025/mori25_interspeech.html)
**Taxonomy:** `people-variation-and-health / human-centered-accessibility / listener-effort`
**Evidence:** D3 full-paper capture; PDF SHA-256 `3b3247727d8efb9691672390584fbd69085efe011f5f83b11da771df2a1f488a`; full-text SHA-256 `08ec7bba2d2b8b8688d2c6b7ff94a53a366850219a69c244efa9ece3d4ca3d16`.

- **Ordinary problem:** A dialogue system needs the words that matter for its response, not necessarily a verbatim transcript of every utterance.
- **Why it is hard:** WER weights function words and content words alike, while people selectively attend to content during response generation; a low WER can therefore hide a consequential miss.
- **Naive attempt:** Evaluate the front-end ASR with ordinary WER, treating every token as equally important.
- **Central move:** Observe selective listening in 297 human participants, estimate part-of-speech importance, and use those weights to form Human-WWER/H-WCER for dialogue-oriented ASR evaluation.
- **Mechanism:** Participants generate a response and then recall/transcribe the speech; multiple regression estimates POS weights, which are inserted into the edit-distance costs used by weighted WER.
- **Mathematical idea:** A regression predicts the remembered POS counts from the full transcript; the resulting coefficients weight insertions, deletions, and substitutions in a minimum-edit-distance score. Five-fold validation compares MAE and R².
- **What the paper reports:** Humans attend more to content words than function words; the proposed H-WWER gives lower scores to human than Whisper transcriptions in the reported comparison and is offered as a dialogue-relevant complement to WER.
- **Limits:** Transcription follows response generation rather than occurring simultaneously, and the displayed weight comparison is partly optimized on test data. The metric is a proposal, not validated against downstream response success or diverse dialogue settings.

## 268. Processing of grammatical information in cochlear implant simulated speech by German adult listeners

**Paper:** [Processing of grammatical information in cochlear implant simulated speech by German adult listeners](https://www.isca-archive.org/interspeech_2025/schouwenaars25_interspeech.html)
**Taxonomy:** `people-variation-and-health / human-centered-accessibility / accessibility-fit`
**Evidence:** D3 full-paper capture; PDF SHA-256 `e14d07175bb97a319d103dd6ce886cd8df6ca812d5d511e36120fb2d89419970`; full-text SHA-256 `8935831c095f3f2db0ac0494774fa6272d0e603540e563367ce973db3d6b105a`.

- **Ordinary problem:** A listener using a cochlear implant or a simulated cochlear implant must recover grammatical structure from a spectrally degraded speech signal.
- **Why it is hard:** The signal degradation can remove cues that distinguish subject, object, and passive questions, while working memory and grammatical case interact with what the listener can use.
- **Naive attempt:** Assume that good performance on normal speech transfers unchanged to the simulated implant condition.
- **Central move:** Compare normal and CI-simulated speech with eye-tracking, accuracy, and working-memory measures so evaluation reflects both the answer and the listener's processing path.
- **Mechanism:** German adults answer subject, object, and passive which-questions. Eye movements and response accuracy expose whether case and subject-verb agreement cues survive the simulation; mixed-effects analyses relate performance to working memory.
- **Mathematical idea:** Accuracy and gaze behavior are behavioral proxies for comprehension; the comparison is between normal and CI-simulated acoustic conditions rather than between two recognition models.
- **What the paper reports:** Only object-question accuracy was affected by the simulation, with weaker interpretation preferences in gaze patterns; higher working memory was associated with better accuracy and faster reorientation.
- **Limits:** The simulation is not an actual implant, the German grammatical system and question types are narrow, and listener behavior does not establish clinical device benefit or general speech recognition performance.

## 269. Individualized speech enhancement for hearing-impaired listeners

**Paper:** [Individualized speech enhancement for hearing-impaired listeners](https://www.isca-archive.org/interspeech_2025/wen25b_interspeech.html)
**Taxonomy:** `people-variation-and-health / human-centered-accessibility / accessibility-fit`
**Evidence:** D3 full-paper capture; PDF SHA-256 `b5fba23b94cbcba797f70674b5953d359a04599f1a31ab66413fcac146a1d2f1`; full-text SHA-256 `ba55945a342fc89f97e22ffc7dad9b8bf8bb0501f4ca52c9fac8ff042d26ba4b`.

- **Ordinary problem:** Speech enhancement should improve access for a particular hearing-impaired listener, not merely optimize an average signal metric.
- **Why it is hard:** Hearing loss profiles differ, and a global enhancer can preserve the wrong cues.
- **Naive attempt:** Optimize one pooled enhancement objective and assume its score represents every listener.
- **Central move:** Individualize enhancement around the listener's hearing profile and evaluate the resulting speech access.
- **Mechanism:** Listener-specific constraints become the target of enhancement rather than the average waveform.
- **Mathematical idea:** The paper treats accessibility-fit as a structured evidence-to-decision problem: Listener-specific constraints become the target of enhancement rather than the average waveform.
- **What the paper reports:** The paper reports individualized speech enhancement for hearing-impaired listeners.
- **Limits:** Hearing profiles, listener numbers, fitting procedure, materials, and subjective protocol bound transfer.

## 270. A Bayesian Approach to L2 Fluency Ratings by Native and Nonnative Listeners

**Paper:** [A Bayesian Approach to L2 Fluency Ratings by Native and Nonnative Listeners](https://www.isca-archive.org/interspeech_2025/yazawa25_interspeech.html)
**Taxonomy:** `people-variation-and-health / human-centered-accessibility / listener-effort`
**Evidence:** D3 full-paper capture; PDF SHA-256 `b90a77c89758bc8bc5cdfd3005b0ab226af97f66b363ba303a1d698b662a2c04`; full-text SHA-256 `a351c46a47960132f691217ae128fdc652fbd684551e730135796481d098b4c9`.

- **Ordinary problem:** Fluency ratings of second-language speech should reflect both the speaker’s temporal behavior and the listener’s linguistic background.
- **Why it is hard:** Listeners disagree, and native-listener norms may not transfer to nonnative listeners; rate, pauses, and repairs are correlated rather than independent cues.
- **Naive attempt:** Average all ratings or use a single syllable-rate predictor and treat the resulting score as a universal fluency scale.
- **Central move:** Use a Bayesian hierarchical model to separate listener variability from utterance-level fluency cues and compare syllable- versus segment-based articulation rate.
- **Mechanism:** Posterior distributions represent listener-specific leniency and cue weights; speed, breakdown, and repair features explain ratings while uncertainty remains explicit.
- **Mathematical idea:** Human evaluation is a multilevel measurement problem: the score is jointly produced by the speech sample and the observer’s perceptual prior.
- **What the paper reports:** Using 16 listeners and 180 Japanese speakers in J-AESOP, the paper reports greater leniency among some nonnative listeners and stronger fit for segment-based articulation rate.
- **Limits:** Listener sample, language backgrounds, trained-rating task, corpus, feature definitions, and Bayesian priors bound transfer; fluency ratings are not a complete measure of communicative success.

## 271. Feature Importance across Domains for Improving Non-Intrusive Speech Intelligibility Prediction in Hearing Aids

**Paper:** [Feature Importance across Domains for Improving Non-Intrusive Speech Intelligibility Prediction in Hearing Aids](https://www.isca-archive.org/interspeech_2025/zezario25_interspeech.html)
**Taxonomy:** `people-variation-and-health / human-centered-accessibility / accessibility-fit`
**Evidence:** D3 full-paper capture; PDF SHA-256 `44997af50fe10a8e1f66fa80bebcf47313f485c09c9f77cfe258401b248c6c8e`; full-text SHA-256 `8402afe889be93a8f954d8563d14b910fc00b7dae672d82069e00c331586a4b8`.

- **Ordinary problem:** A hearing-aid system needs an intelligibility estimate without asking a listener to score every noisy utterance.
- **Why it is hard:** Human scores are expensive, while acoustic features, learned representations, and hearing-aid conditions expose different parts of the perceptual problem.
- **Naive attempt:** Feed one feature family into a regressor and treat its error as a complete measure of intelligibility.
- **Central move:** Estimate frame-level importance across spectral, temporal, and Whisper latent features, project each domain through those weights, and fuse them in an assessment model.
- **Mechanism:** FiDo produces domain-specific weighted representations before concatenation and regression; RMSE on intelligibility targets evaluates whether the weighting preserves listener-relevant evidence.
- **Mathematical idea:** Feature selection is moved inside the representation: the model learns which moments and domains matter before the final proxy prediction.
- **What the paper reports:** The paper reports that FiDo reduces MBI-Net+ RMSE from 26.10 to 24.11 and improves over the best 2023 Clarity Prediction Challenge system.
- **Limits:** Weakly supervised targets, hearing-aid/noise conditions, challenge split, proxy RMSE, and absence of a new listener study bound the claim; prediction is not equivalent to real-world access improvement.

## 272. Agent-based modelling, sound change, and metaphony in Southern Italian varieties of Italo-Romance.

**Paper:** [Agent-based modelling, sound change, and metaphony in Southern Italian varieties of Italo-Romance.](https://www.isca-archive.org/interspeech_2025/bressensdorf25_interspeech.html)
**Taxonomy:** `people-variation-and-health / identity-and-life-stage / age-and-development`
**Evidence:** D3 full-paper capture; PDF SHA-256 `a143b5b14c9c14d14b57ab479d19eb511be05f1d0e9b0f1df45f9f7cb8c3960d`; full-text SHA-256 `bf13fe6ecec61926e77ec2a0d2a9859c0410aeca3c878e853b05e5bcaf30e8c1`.

- **Ordinary problem:** When speakers of two dialects meet, a sound change can spread unevenly: a conservative dialect may move toward an innovative one, changing how grammatical information is pronounced.
- **Why it is hard:** The change is both social and physical: speakers remember variable signals, categories can emerge gradually, and inflectional cues can move between suffixes and stem vowels.
- **Naive attempt:** Treat dialect contact as a fixed label difference or assume both communities shift symmetrically toward an average.
- **Central move:** Initialize an interactive phonetic agent model with real speech from two Southern Italian varieties and simulate metaphony, then compare diphthongization and categorical contrasts.
- **Mechanism:** The paper tests an agent-based model of dialect contact and morpho-phonological sound change.
- **Mathematical idea:** A dialect is not a static inventory: production is repeatedly updated through perceptual memory and interaction, allowing social contact to reshape acoustic categories over time.
- **What the paper reports:** The reported results provide support for an asymmetric shift toward the innovative dialect and are consistent with feedback models of sound change.
- **Limits:** The two dialects, 54 speakers collapsed to 13 agents, selected words, F1 trajectory representation, and model assumptions limit generalization to other communities or changes.

## 273. Pitch Target Realization in Putonghua Tone Production of Children from Dialect-Speaking Regions

**Paper:** [Pitch Target Realization in Putonghua Tone Production of Children from Dialect-Speaking Regions](https://www.isca-archive.org/interspeech_2025/cao25_interspeech.html)
**Taxonomy:** `people-variation-and-health / identity-and-life-stage / age-and-development`
**Evidence:** D3 full-paper capture; PDF SHA-256 `ce066f2b348f4053694e9cc048f7d33beaad3f39c500ecc82898d3b6b6fbd7e8`; full-text SHA-256 `a779c572ea9c473723cd601c61851bdffc50bb826c3ae2389cc11e26ebace1bc`.

- **Ordinary problem:** Children learning a second tonal variety must realize pitch targets while their physiology and first dialect continue to shape production.
- **Why it is hard:** Targets overlap in time and similar tones can interfere, so an error is not simply a failure to memorize a contour.
- **Naive attempt:** Treat each tone as an isolated fixed pitch template.
- **Central move:** Analyze on-target and off-target realization as interacting targets shaped by physiology and dialect experience.
- **Mechanism:** Pitch production from 139 Changli-exposed children aged 35–71 months is analyzed in the CL-CHILD corpus.
- **Mathematical idea:** The comparison separates target approximation, physiological constraints, and mutual interference among tonal categories.
- **What the paper reports:** The paper reports universal physiological constraints, persistent dialect interference, and off-target forms arising from phonetic similarity and target interaction.
- **Limits:** The age range, dialect exposure, corpus, and tone inventory bound the developmental claim; longitudinal and other language environments remain open.

## 274. Towards Robust Speaker Recognition against Intrinsic Variation with Foundation Model Few-shot Tuning and Effective Speech Synthesis

**Paper:** [Towards Robust Speaker Recognition against Intrinsic Variation with Foundation Model Few-shot Tuning and Effective Speech Synthesis](https://www.isca-archive.org/interspeech_2025/chen25_interspeech.html)
**Taxonomy:** `people-variation-and-health / identity-and-life-stage / style-and-state-variation`
**Evidence:** D3 full-paper capture; PDF SHA-256 `4523835b2f19dd904f99cc3d16247bda6bf7d9e275ed819f9e923ccc1d4dcdac`; full-text SHA-256 `cc31f796e10d9998ab82bcbd8956930213cb81ac76cb5e876f4dd07807c710a4`.

- **Ordinary problem:** A speaker recognizer should recognize a person years later or in a different emotional state, while rejecting unknown people in an open set.
- **Why it is hard:** Age and emotion change the same speaker's voice, and limited enrollment data makes it hard to learn every future condition.
- **Naive attempt:** Enroll one fixed embedding and set a threshold that assumes the speaker is stable.
- **Central move:** Use few-shot foundation-model tuning at enrollment and generate style-rich synthetic speech to expose time-varying and emotional conditions, with losses focused on unknown outliers.
- **Mechanism:** The framework selects synthetic speech, tunes the foundation model with few enrollment examples, and evaluates open-set identification across time-varying and emotional benchmarks.
- **Mathematical idea:** Identification accuracy and open-set outlier behavior separate recognizing enrolled speakers from rejecting unknown speakers.
- **What the paper reports:** The paper reports stronger generalization to aging and emotional variation while maintaining resistance to unknown outliers.
- **Limits:** The claim is bounded to the synthetic-data choices, foundation model, enrollment protocol, and benchmarks; real aging trajectories, spoofing attacks, and fairness across groups remain open.

## 275. Pushing the Frontiers of Self-Distillation Prototypes Network with Dimension Regularization and Score Normalization

**Paper:** [Pushing the Frontiers of Self-Distillation Prototypes Network with Dimension Regularization and Score Normalization](https://www.isca-archive.org/interspeech_2025/chen25f_interspeech.html)
**Taxonomy:** `people-variation-and-health / identity-and-life-stage / speaker-verification`
**Evidence:** D3 full-paper capture; PDF SHA-256 `fc00b539d3324a6b307e7f3194a556c9139d774cdca45298d6befe5610effcf3`; full-text SHA-256 `2b1310b4bd9972faa4cbeb6edb438234cc8239d8449dade3ead9b19bcc1cb5e3`.

- **Ordinary problem:** Speaker verification should work without speaker labels, yet self-supervised embeddings can collapse or score poorly compared with supervised systems.
- **Why it is hard:** Without identity labels, the representation must discover dimensions that separate speakers while avoiding collapse; score calibration also changes verification decisions across trials.
- **Naive attempt:** Use an unlabeled self-supervised embedding and accept collapsed dimensions or unnormalized similarity scores.
- **Central move:** Add dimension regularization to a self-distillation prototype network and use score normalization to close the gap toward supervised verification.
- **Mechanism:** The paper improves self-supervised speaker verification with dimension regularization and score normalization.
- **Mathematical idea:** Verification has two linked problems: learn a non-collapsed identity space and compare enrollment/test scores on a calibrated scale; solving only one leaves unreliable decisions.
- **What the paper reports:** On VoxCeleb1, the paper reports EERs of 1.29%, 1.60%, and 2.80% on the O/E/H trials and relative improvements over prior self-supervised methods.
- **Limits:** VoxCeleb1, trial conditions, unlabeled-training setup, score normalization, and EER bound the claim; benchmark gains do not establish fairness or robustness in deployment.

## 276. Speech Unlearning

**Paper:** [Speech Unlearning](https://www.isca-archive.org/interspeech_2025/cheng25d_interspeech.html)
**Taxonomy:** `people-variation-and-health / identity-and-life-stage / speaker-verification`
**Evidence:** D3 full-paper capture; PDF SHA-256 `3f7e1bf16ec72d818585d6e04a86a27fadc5a55eed48d0e48bf9ebc8d1c9b9cd`; full-text SHA-256 `dcfbf4f4236c8fd00a80ab9d7f4f98d6260191d18dba7cc4a590b0a45b313be5`.

- **Ordinary problem:** A trained speech model may retain information about a recording that its owner wants removed, without the cost of retraining the entire model.
- **Why it is hard:** Speech is sequential, speaker-dependent, and high-dimensional, so removing one recording or one speaker can damage remaining behavior or leave traces behind.
- **Naive attempt:** Delete the source file and assume the trained model no longer contains its influence, or retrain from scratch every time.
- **Central move:** Define sample-level and class-level unlearning and test whether a model forgets the target while preserving performance on remaining speech.
- **Mechanism:** Keyword-spotting and speaker-identification experiments compare removing one recording with removing an entire speaker category and examine the difficulty relative to image and text unlearning.
- **Mathematical idea:** Unlearning is a constrained before/after problem: target influence should disappear while non-target accuracy remains; forgetting and retention need separate tests.
- **What the paper reports:** The paper reports that speech unlearning is substantially harder than image or text unlearning and identifies structured training, evaluation, feature-level removal, and adversarial robustness as open directions.
- **Limits:** Tasks, speakers, unlearning definitions, attack tests, and evaluation criteria bound the result; a proposed forgetting score is not proof of privacy against every adversary.

## 277. Analysis of the ABC Classification Backends for NIST SRE24

**Paper:** [Analysis of the ABC Classification Backends for NIST SRE24](https://www.isca-archive.org/interspeech_2025/cumani25_interspeech.html)
**Taxonomy:** `people-variation-and-health / identity-and-life-stage / speaker-verification`
**Evidence:** D3 full-paper capture; PDF SHA-256 `e55085c9e467f9d8fd4fa93cd5e1db99319492dd4aca005ee8e08731ed6fe205`; full-text SHA-256 `2e6b7bff7ae5286560e503d3962dc1a147a801a792e23e74362aaf2989b3edd4`.

- **Ordinary problem:** A speaker-recognition backend must decide whether recordings belong to the same person, while evaluation rankings can change with scoring, calibration, and trial composition.
- **Why it is hard:** A benchmark result is not only an embedding result: backend assumptions determine how scores are normalized and how errors are traded off.
- **Naive attempt:** Compare systems using one unexamined score or treat the best embedding as automatically the best verification system.
- **Central move:** Analyze the ABC classification backends used for NIST SRE24 and separate representation quality from backend scoring behavior.
- **Mechanism:** The paper studies backend choices for speaker classification/verification in the NIST SRE24 setting.
- **Mathematical idea:** Verification is a decision pipeline: embeddings, score computation, calibration, and operating point jointly produce the accepted/rejected decision.
- **What the paper reports:** The paper reports how the analyzed backends behave on the NIST SRE24 evaluation conditions.
- **Limits:** Benchmark protocol, language/channel conditions, calibration, and chosen operating points limit claims beyond SRE24.

## 278. A Copula-Based Generative Score-Level Fusion Model for Speaker Verification

**Paper:** [A Copula-Based Generative Score-Level Fusion Model for Speaker Verification](https://www.isca-archive.org/interspeech_2025/cumani25b_interspeech.html)
**Taxonomy:** `people-variation-and-health / identity-and-life-stage / speaker-verification`
**Evidence:** D3 full-paper capture; PDF SHA-256 `8c16fb26acda8cb626c73788551889bd9a9ef57acd05fa974a5ec77da042d910`; full-text SHA-256 `e0677d907b6e37601f0d121715c13756113d2042dd98808dbaf7564edea9aa5c`.

- **Ordinary problem:** A speaker verifier should combine several recognizers while producing scores that mean the same thing across operating thresholds.
- **Why it is hard:** Different recognizers make dependent errors and their scores have different scales, so adding scores can miscalibrate decisions.
- **Naive attempt:** Use a weighted linear score sum and tune it on one development set.
- **Central move:** Model the joint score distribution with flexible marginals and a copula that captures dependency, then fuse and calibrate scores.
- **Mechanism:** Variance-Gamma marginals describe each recognizer's score distribution and a Gaussian copula describes dependence for target and non-target trials.
- **Mathematical idea:** The copula separates marginal shape from dependency; Cllr measures calibration and discrimination of verification scores.
- **What the paper reports:** On NIST SRE 2019 and SITW, the method reports up to 7% relative Cllr reduction versus discriminative linear fusion.
- **Limits:** Datasets, recognizer diversity, score distributions, and calibration protocol bound the result; new speakers, channels, and attacks need separate evaluation.

## 279. Inter-Speaker Relative Cues for Text-Guided Target Speech Extraction

**Paper:** [Inter-Speaker Relative Cues for Text-Guided Target Speech Extraction](https://www.isca-archive.org/interspeech_2025/dai25b_interspeech.html)
**Taxonomy:** `people-variation-and-health / identity-and-life-stage / style-and-state-variation`
**Evidence:** D3 full-paper capture; PDF SHA-256 `d86543541f96330320362c68c9c16a6eceb97ffff506c296819c2261f638a01d`; full-text SHA-256 `46be45aa08df47613d19c199de797e1eaa275db8e16bbba197aefd7da7360b29`.

- **Ordinary problem:** A separator should isolate the speaker a user describes, even when the enrollment recording or direction cue is unavailable.
- **Why it is hard:** Fixed categories such as male/female or high/low pitch lose information and do not expand cleanly across languages and rooms.
- **Naive attempt:** Treat every attribute as a fixed class or use only one cue such as gender.
- **Central move:** Describe the target relative to the interfering speaker, then combine relative cues and pretrained speech representations in a text-conditioned extractor.
- **Mechanism:** Two-speaker mixtures are built across five languages with cues for language, gender, emotion, order, age, rate, duration, pitch, loudness, and distance; prompts identify the target by those relations.
- **Mathematical idea:** The central object is not a speaker label but a relation between two signals. Extraction quality is measured after the text selects one member of the mixture.
- **What the paper reports:** The paper reports that all relative cues beat random subsets, with gender and temporal order especially robust across languages and reverberation; WavLM/CNN initialization improves the baseline.
- **Limits:** The claim is bounded to the constructed mixtures, cue templates, languages, and author-reported tests; real conversational mixtures and privacy effects remain open.

## 280. An Investigative Study on Recent Sharpness- and Flatness-Based Optimizers for Enhanced Self-Supervised Speaker Verification

**Paper:** [An Investigative Study on Recent Sharpness- and Flatness-Based Optimizers for Enhanced Self-Supervised Speaker Verification](https://www.isca-archive.org/interspeech_2025/fathan25_interspeech.html)
**Taxonomy:** `people-variation-and-health / identity-and-life-stage / speaker-verification`
**Evidence:** D3 full-paper capture; PDF SHA-256 `fe5c136e891dc4cb2a3ca7243efc66964d54b4c45c6c6e4e607f9a1fc6c3e763`; full-text SHA-256 `3e77e52c808bf03577dcfa861c666dcbd30fbceb347b0ed3faa16c7643d904b6`.

- **Ordinary problem:** A speaker-verification system should recognize the same person when the recording, wording, or channel changes, rather than memorizing the training speakers' exact conditions.
- **Why it is hard:** The model must keep identity evidence while ignoring content, microphones, noise, and recording differences; the training objective and optimizer can change which evidence is retained.
- **Naive attempt:** Use the most familiar optimizer and report one verification score, assuming the representation will generalize if the training loss decreases.
- **Central move:** Treat the optimization geometry itself as part of the identity-learning problem: compare ordinary, mixture-based, and sharpness-aware optimizers and regularizers instead of changing only the network architecture.
- **Mechanism:** The study trains supervised and self-supervised speaker-verification systems with ADOPT, AdEMAMix, SAM, ASAM, GAM, and GSAM, then tests weight decay, exponential moving averages, and SWITCH EMA. The comparison asks whether flatter or better-conditioned solutions improve verification generalization without adding an inference-time identity module.
- **Mathematical idea:** The verification decision compares an enrollment and test embedding, while the training choices change the parameter update. Sharpness-aware methods add a local worst-case loss perturbation so a solution is rewarded for remaining good in a neighborhood; EER and minDCF summarize threshold errors rather than directly measuring identity invariance.
- **What the paper reports:** The paper reports that optimizer choice materially changes generalization and that the tested sharpness-aware and general-purpose optimizers can reach state-of-the-art self-supervised speaker-verification results in its experiments.
- **Limits:** The conclusions are bounded by the selected speaker-verification corpora, architectures, optimizer settings, and author-reported comparisons; a better optimizer score does not establish robustness to every language, channel, attack, or demographic group. No independent reproduction was performed.

## 281. Egocentric Speaker Classification in Child-Adult Dyadic Interactions: From Sensing to Computational Modeling

**Paper:** [Egocentric Speaker Classification in Child-Adult Dyadic Interactions: From Sensing to Computational Modeling](https://www.isca-archive.org/interspeech_2025/feng25b_interspeech.html)
**Taxonomy:** `people-variation-and-health / identity-and-life-stage / speaker-verification`
**Evidence:** D3 full-paper capture; PDF SHA-256 `6724b49743ddf39de27f90dd8e49978d34d55dbc70e2d6f0bf2c12ea51db9a15`; full-text SHA-256 `736e7be64fdf8854d3fd373b5a1434f2610efd5073b6e5c44c609db6e51b2de0`.

- **Ordinary problem:** In a child–adult interaction, a wearable sensor should identify who spoke and when from the child's own viewpoint, because a distant spectator microphone may miss the interactional reality.
- **Why it is hard:** Wearable audio contains body motion, self-noise, changing distance, and overlapping child/adult speech; speaker identity and social behavior are mixed with the sensing perspective.
- **Naive attempt:** Use a fixed room microphone and assume the same speaker cues are available from every viewpoint.
- **Central move:** Treat the egocentric sensor as part of the task, model the child/adult dyad under that perspective, and evaluate how sensing choices affect automatic speaker classification.
- **Mechanism:** The paper studies wearable sensing in BOSCC child–clinician interactions, uses egocentric speech sampling, and evaluates computational speaker classification for behavioral analysis related to autism treatment.
- **Mathematical idea:** The observation point changes the signal distribution; classification performance is therefore a joint property of speaker cues, body-worn placement, interaction, and activity timing rather than voice alone.
- **What the paper reports:** The paper reports that egocentric sensing provides useful information for child/adult speaker classification and highlights the promise and constraints of wearable speech modeling.
- **Limits:** BOSCC activities, children/clinicians, sensor placement, privacy, and speaker labels bound the result; classification is not a direct measure of social communication or treatment outcome.

## 282. How sibilant spectra shape gender perception in prepubertal children: A voice morphing study

**Paper:** [How sibilant spectra shape gender perception in prepubertal children: A voice morphing study](https://www.isca-archive.org/interspeech_2025/funk25_interspeech.html)
**Taxonomy:** `people-variation-and-health / identity-and-life-stage / age-and-development`
**Evidence:** D3 full-paper capture; PDF SHA-256 `2189cb98638b181c71beaefe046fd7e2c3c0977e82584a6dced67a4df7c41f5e`; full-text SHA-256 `9351bdc31caff8a98ce46e1afc3f6ed0fe7fd95d0240dc3a8929ac3a6f053e78`.

- **Ordinary problem:** Listeners may infer gender from a child's voice, but a small acoustic feature such as a sibilant spectrum should not be mistaken for a complete or natural explanation of that social judgment.
- **Why it is hard:** Natural speech contains many correlated cues, and children learn social categories from context; isolating one spectrum can reveal an association while also creating an artificial listening condition.
- **Naive attempt:** Measure average spectral differences between boys and girls and infer that the difference determines listener gender perception.
- **Central move:** Use natural and voice-morphed stimuli to separate the acoustic contribution of /z/ sibilant spectral shape from the broader voice and social context.
- **Mechanism:** The longitudinal study measures center of gravity and skewness of /z/ in German-speaking children aged 6–9 and runs gender-perception experiments with natural and morphed voices.
- **Mathematical idea:** Morphing is a controlled intervention: it holds much of the voice fixed while changing the sibilant spectrum, allowing perception to be compared with the correlation found in natural speech.
- **What the paper reports:** No overall gender differences in the measured sibilant features were found; sibilants did not affect gender perception in natural stimuli but did affect it in morphed stimuli, suggesting stereotypical associations in isolation.
- **Limits:** Age, language, stimulus construction, listener beliefs, longitudinal sample, and morphing artifacts bound the claim; a perceptual association is not a biological marker or justification for gender classification.

## 283. You Are What You Say: Exploiting Linguistic Content for VoicePrivacy Attacks

**Paper:** [You Are What You Say: Exploiting Linguistic Content for VoicePrivacy Attacks](https://www.isca-archive.org/interspeech_2025/gaznepoglu25_interspeech.html)
**Taxonomy:** `people-variation-and-health / identity-and-life-stage / speaker-verification`
**Evidence:** D3 full-paper capture; PDF SHA-256 `b6ff765d96a449ac72d3108d33e0cd3c1ed82075ed24659efe7907a740a1bff6`; full-text SHA-256 `04aac294a05a6e6b2be111022f2231b5afdb9a8accbbb129e6a07c16818ed4fb`.

- **Ordinary problem:** A voice-privacy attack should not mistake repeated linguistic content for speaker identity when evaluating anonymization.
- **Why it is hard:** If attacker training and test utterances share semantic or lexical content, text alone can predict the speaker and make privacy scores misleading.
- **Naive attempt:** Use a standard ASV attack and assume its error reflects only acoustic identity leakage.
- **Central move:** Adapt BERT to attack speaker identity from transcript content, inspect explainable keywords, and compare the resulting EER and dataset construction.
- **Mechanism:** The attacker maps linguistic content to speaker labels; semantically similar utterances become a non-acoustic identity channel in the evaluation.
- **Mathematical idea:** Privacy evaluation requires separating nuisance correlations from the protected attribute; otherwise the attack measures corpus curation rather than voice leakage.
- **What the paper reports:** The paper reports mean EER around 35%, with some speakers as low as 2%, using text alone on VoicePrivacy data.
- **Limits:** Dataset curation, speaker/content overlap, BERT training, split design, and EER interpretation bound the claim; text leakage does not prove an anonymizer fails acoustically.

## 284. EmoSpeechAuth: Emotion-Aware Speaker Verification

**Paper:** [EmoSpeechAuth: Emotion-Aware Speaker Verification](https://www.isca-archive.org/interspeech_2025/goebiowska25_interspeech.html)
**Taxonomy:** `people-variation-and-health / identity-and-life-stage / speaker-verification`
**Evidence:** D3 full-paper capture; PDF SHA-256 `6344a1d3bd890a074a2c76c688a972018ec9410d43027d900ad4b5e43057eeba`; full-text SHA-256 `8c49bbce803dd4bfb905ebd2c13fa3e1f7c982865e1c3f2917bdc62265f07f89`.

- **Ordinary problem:** Speaker verification should remain reliable when emotional state changes the same person's voice.
- **Why it is hard:** Emotion changes pitch, timing, energy, and voice quality and can cross identity thresholds.
- **Naive attempt:** Enroll and test only neutral speech or treat emotional recordings as different identities.
- **Central move:** Build emotion-aware speaker verification and test identity evidence across affective states.
- **Mechanism:** The verifier separates speaker-consistent structure from emotion-dependent variation.
- **Mathematical idea:** The relevant object is the speaker-verification evidence described by the paper's mechanism: The verifier separates speaker-consistent structure from emotion-dependent variation.
- **What the paper reports:** The paper presents EmoSpeechAuth and evaluates emotion-aware speaker verification.
- **Limits:** Emotion labels, speakers, channel, enrollment, thresholds, and demographics bound transfer.

## 285. Unified Text and Speaker Verification using SSL model for Text-Dependent Speaker Verification

**Paper:** [Unified Text and Speaker Verification using SSL model for Text-Dependent Speaker Verification](https://www.isca-archive.org/interspeech_2025/griot25_interspeech.html)
**Taxonomy:** `people-variation-and-health / identity-and-life-stage / speaker-verification`
**Evidence:** D3 full-paper capture; PDF SHA-256 `cf14770d560718bd18e82b1ecf20d8c24bfae793c216cb4833b2d3282c5a3122`; full-text SHA-256 `a4dfb09c8e65f3b19d65ac8c654fe55ca3bcae52ab6baa596592b4853cbf7ba3`.

- **Ordinary problem:** Speaker verification must decide identity while content may be the same or different, without confusing lexical matching with speaker evidence.
- **Why it is hard:** Text-independent and text-dependent trials expose different shortcuts; a representation helping one can fail when phrase content changes.
- **Naive attempt:** Train separate systems for every language and treat verification as one undifferentiated score.
- **Central move:** Use a unified self-supervised student for text validation and speaker verification, then evaluate tandem decisions across multilingual trials.
- **Mechanism:** The student preserves lexical information for text validation while a speaker backend supplies identity evidence; DeepMine and VoxCeleb1 test both modes.
- **Mathematical idea:** English DeepMine TD-SV tandem EER is 3.46% versus 4.28% baseline; VoxCeleb1 TI-SV is 1.29% versus 0.49%, exposing a tradeoff.
- **What the paper reports:** The student improves reported text-dependent and DeepMine results but degrades VoxCeleb1 text-independent results relative to ReDimNet.
- **Limits:** Datasets, languages, content, thresholds, and reported EERs bound the conclusion; open-set deployment is unestablished.

## 286. PAEFF: Precise Alignment and Enhanced Gated Feature Fusion for Face-Voice Association

**Paper:** [PAEFF: Precise Alignment and Enhanced Gated Feature Fusion for Face-Voice Association](https://www.isca-archive.org/interspeech_2025/hannan25_interspeech.html)
**Taxonomy:** `people-variation-and-health / identity-and-life-stage / speaker-verification`
**Evidence:** D3 full-paper capture; PDF SHA-256 `a70bc19c6a9e8ea8beec74e01fb8baaf122cc7855300c55816bfe474047ec88a`; full-text SHA-256 `95c85980f37b31a7b5614211072995d57fe7ae606979910b90270e0307c895bc`.

- **Ordinary problem:** A system should decide whether a face and a voice belong together when the person or video is unfamiliar, without relying on hand-tuned negative examples.
- **Why it is hard:** Face and voice embeddings live in different spaces; margins and mined negatives can make association depend on arbitrary training choices.
- **Naive attempt:** Use a contrastive or triplet loss with a fixed distance margin and assume the two modalities align after ordinary fusion.
- **Central move:** Align the modalities with orthogonality constraints and gated feature fusion in a joint hyperbolic space, where hierarchy-like distances can represent identity similarity.
- **Mechanism:** The two branches extract pretrained face and voice features, fuse them, and optimize a combination of association, orthogonality, and hyperbolic objectives on VoxCeleb1.
- **Mathematical idea:** Verification asks whether a pair matches, while AUC and EER expose different threshold behavior. Seen-heard and unseen-unheard splits test whether the association survives new videos and people.
- **What the paper reports:** On the reported VoxCeleb1 splits, PAEFF improves the best listed baseline on unseen-unheard EER and reaches the highest or near-highest AUC in the table.
- **Limits:** The result is author-reported and tied to VoxCeleb1, its split protocol, pretrained encoders, and hyperparameters; it does not establish robustness to dubbing, adversarial pairing, or other cultures.

## 287. Variability in performance across four generations of automatic speaker recognition systems

**Paper:** [Variability in performance across four generations of automatic speaker recognition systems](https://www.isca-archive.org/interspeech_2025/harrington25_interspeech.html)
**Taxonomy:** `people-variation-and-health / identity-and-life-stage / speaker-verification`
**Evidence:** D3 full-paper capture; PDF SHA-256 `42d5a5cd0253d4566d598e3b5aedd4d36bd5ad4b3595d6230d2466d346e1a5de`; full-text SHA-256 `77300e9c34d00b2bcf6274e188694de6b938412caa519570759242e3d81b62b1`.

- **Ordinary problem:** A speaker-recognition benchmark should reveal which people and conditions remain difficult, not only report one aggregate score across model generations.
- **Why it is hard:** Architectural improvements can hide persistent speaker-level failures, and file-level factors can be confused with stable person-level difficulty.
- **Naive attempt:** Compare only aggregate metrics or assume each new generation improves every speaker equally.
- **Central move:** Evaluate four generations on the same forensic test/calibration data at both system and individual-speaker levels.
- **Mechanism:** Matched evaluation separates model-generation effects from test-set changes and decomposes variation by file and speaker factors.
- **Mathematical idea:** The unit of analysis matters: an overall metric averages heterogeneous difficulty, while per-speaker outcomes expose persistent tails.
- **What the paper reports:** Performance improves from GMM-UBM through i-vector and x-vector but not ECAPA-TDNN in the reported comparison; some individuals remain difficult across systems.
- **Limits:** Forensic data, calibration, system implementations, speaker sampling, and metric choice bound transfer; persistent difficulty is not automatically a biological property.

## 288. Challenges in Automated Processing of Speech from Child Wearables:  The Case of Voice Type Classifier

**Paper:** [Challenges in Automated Processing of Speech from Child Wearables:  The Case of Voice Type Classifier](https://www.isca-archive.org/interspeech_2025/kunze25_interspeech.html)
**Taxonomy:** `people-variation-and-health / identity-and-life-stage / age-and-development`
**Evidence:** D3 full-paper capture; PDF SHA-256 `32e7a16d5b6b203cd09c96160541cd615eb81d37fa7e0e72331179a9bc74c8ab`; full-text SHA-256 `900b990db2325e2eed51e358fdd1acbe6fe8dd34bad9fc029f5bf878b555086c`.

- **Ordinary problem:** Wearable child recordings produce enormous naturalistic audio, but researchers need reliable labels such as who or what kind of voice appears before studying development.
- **Why it is hard:** In-the-wild recordings are noisy, imbalanced, difficult to share, and unlike curated speech data, so a better model may not solve the real bottleneck.
- **Naive attempt:** Keep changing the architecture and features until the classifier improves, while ignoring the data collection and permission process.
- **Central move:** Treat data relevance, quantity, label quality, and permission to share as first-class parts of the recognition problem.
- **Mechanism:** Three years of voice-type classification experiments on child-worn recordings compare representation features, architectures, and parameter search against data changes.
- **Mathematical idea:** Performance is limited by the relationship between labels and the recording environment; classification scores reveal whether engineering changes matter relative to data coverage.
- **What the paper reports:** Model and tuning improvements produce marginal gains, while more relevant and larger shareable data produce more progress.
- **Limits:** The child-wearable setting, label scheme, permissions, and task definition bound the result; conclusions do not automatically transfer to adult or laboratory speech.

## 289. Examining Test-Time Adaptation for Personalized Child Speech Recognition

**Paper:** [Examining Test-Time Adaptation for Personalized Child Speech Recognition](https://www.isca-archive.org/interspeech_2025/shi25h_interspeech.html)
**Taxonomy:** `people-variation-and-health / identity-and-life-stage / age-and-development`
**Evidence:** D3 full-paper capture; PDF SHA-256 `8ef705b043076cb0bebac2bbe985b5bde02fb6c6cbc746131ff1dcf8f98cd464`; full-text SHA-256 `654ff59e7ebedb7420a746b5271d8a4c21240227d961b2a2462011c860cf6c22`.

- **Ordinary problem:** ASR should adapt to individual child speakers at test time without requiring transcript annotations.
- **Why it is hard:** Children differ acoustically and linguistically from adult pretraining data and from one another, making a single child-domain correction insufficient.
- **Naive attempt:** Fine-tune once on a pooled child corpus or use an unadapted adult model for every child.
- **Central move:** Apply unsupervised SUTA and SGEM test-time adaptation to off-the-shelf and child-fine-tuned ASR models and compare per-child results.
- **Mechanism:** The adaptation updates model behavior from incoming child speech at inference time, without target transcripts, and is evaluated against unadapted baselines.
- **Mathematical idea:** Personalization is an online evidence problem: each child supplies a changing acoustic distribution rather than a fixed domain label.
- **What the paper reports:** The paper reports average and per-child gains for both model types, with remaining limitations on non-linguistic child speech.
- **Limits:** Child corpus, adaptation methods, update stability, model family, and evaluation conditions bound transfer; average WER gains are not proof of safe continual deployment.

## 290. Bridging ASR and LLMs for Dysarthric Speech Recognition: Benchmarking Self-Supervised and Generative Approaches

**Paper:** [Bridging ASR and LLMs for Dysarthric Speech Recognition: Benchmarking Self-Supervised and Generative Approaches](https://www.isca-archive.org/interspeech_2025/aboeitta25_interspeech.html)
**Taxonomy:** `recognition-and-alignment / acoustic-unit-learning / acoustic-to-token`
**Evidence:** D3 full-paper capture; PDF SHA-256 `e39b8c1a94256ca369c6800d405f322258d34df86c51870aaa1b324d273832fd`; full-text SHA-256 `8759e60b9a73ba8530c4ddd74b405ca4004fed547460bf94beaaf00457c32d75`.

- **Ordinary problem:** Automatic speech recognition must transcribe dysarthric speech whose phonetic timing and articulation violate assumptions learned from typical speech.
- **Why it is hard:** CTC can misalign distorted phonemes, ordinary end-to-end models can produce grammatical but acoustically unsupported text, and severity and speaker shifts change the error pattern.
- **Naive attempt:** Use a standard ASR model and treat WER as the complete measure of success.
- **Central move:** Benchmark CTC, Whisper, and LLM-enhanced decoders, including bridge networks and a Q-Former that connects Whisper acoustic features to Vicuna for context-aware decoding.
- **Mechanism:** The comparison keeps TORGO and UASpeech speaker-independent splits and evaluates WER by dysarthria severity. The decoder choice changes how much linguistic context can repair uncertain acoustic evidence.
- **Mathematical idea:** The paper exposes an evidence trade-off: a stronger language prior can improve semantic reconstruction, but it can also make a plausible transcript less directly grounded in the signal.
- **What the paper reports:** Whisper improves over CTC baselines, and Whisper-Vicuna reports the lowest WER in the tested TORGO and UASpeech comparisons; all results remain author-reported.
- **Limits:** Dataset splits, severity labels, model scale, decoding prompts, and WER limit the claim; lower WER does not prove faithful preservation of disfluencies or speaker intent.

## 291. HuBERT-VIC: Improving Noise-Robust Automatic Speech Recognition of Speech Foundation Model via Variance-Invariance-Covariance Regularization

**Paper:** [HuBERT-VIC: Improving Noise-Robust Automatic Speech Recognition of Speech Foundation Model via Variance-Invariance-Covariance Regularization](https://www.isca-archive.org/interspeech_2025/ahn25_interspeech.html)
**Taxonomy:** `recognition-and-alignment / acoustic-unit-learning / self-supervised-speech-units`
**Evidence:** D3 full-paper capture; PDF SHA-256 `9ba4f97e7a950bbbd5ebe5d40c5fc3951f7cc17635594a9c9863ef1d9fc4f80a`; full-text SHA-256 `a920134476a64e4fa049ba0f19493bbeca71e6a63395d55af95cc6b6f415e994`.

- **Ordinary problem:** A recognizer trained on clean speech should still map noisy speech to words.
- **Why it is hard:** Noise changes acoustic statistics and can be mistaken for speech units.
- **Naive attempt:** Add noise only during fine-tuning and hope the representation stays stable.
- **Central move:** Add variance, invariance, and covariance constraints during HuBERT pretraining.
- **Mechanism:** HuBERT-VIC applies VICReg terms to noisy representations and compares masked prediction with regularizer ablations on MUSAN-noised LibriSpeech.
- **Mathematical idea:** The reported target is WER; relative gains are 23.3% on test-clean and 13.2% on test-other against the noisy-pretrained baseline.
- **What the paper reports:** All three regularizers give the best reported WER and show complementary ablation effects.
- **Limits:** MUSAN, SNR choices, HuBERT, and LibriSpeech bound the result; real conversational noise is not established.

## 292. Analysis of Semantic and Acoustic Token Variability Across Speech, Music, and Audio Domains

**Paper:** [Analysis of Semantic and Acoustic Token Variability Across Speech, Music, and Audio Domains](https://www.isca-archive.org/interspeech_2025/ashihara25_interspeech.html)
**Taxonomy:** `recognition-and-alignment / acoustic-unit-learning / self-supervised-speech-units`
**Evidence:** D3 full-paper capture; PDF SHA-256 `6ddf7d958ffbd346680c98f621eaa0099d8c90928357236537c9cbcf109fa701`; full-text SHA-256 `da5b1725dd99cb9675f0e6d7f68f2511cefdb458a9858c9231426b13f30b0716`.

- **Ordinary problem:** Understand what discrete audio tokens preserve when speech, music, and general audio are represented for language models.
- **Why it is hard:** Tokens can be statistically predictable while still using different codewords across domains, so one universal token vocabulary may hide domain structure.
- **Naive attempt:** Assume a token representation has the same behavior in speech, music, and sound because the encoding format is shared.
- **Central move:** Compare acoustic codec tokens and semantic speech tokens across domains using rank-frequency distributions, perplexity, and token usage patterns.
- **Mechanism:** The study measures statistical structure and predictability of token sequences, then compares domain-specific codeword usage.
- **Mathematical idea:** Rank-frequency distributions describe how often codes occur; perplexity measures uncertainty of the next token. Similar predictability does not imply identical meaning.
- **What the paper reports:** The paper reports similar statistical/predictable sequence patterns across domains but domain-dependent token usage.
- **Limits:** The analysis supports representation observations, not a universal optimal token design or downstream task improvement.

## 293. From Weak Labels to Strong Results: Utilizing 5,000 Hours of Noisy Classroom Transcripts with Minimal Accurate Data

**Paper:** [From Weak Labels to Strong Results: Utilizing 5,000 Hours of Noisy Classroom Transcripts with Minimal Accurate Data](https://www.isca-archive.org/interspeech_2025/attia25_interspeech.html)
**Taxonomy:** `recognition-and-alignment / acoustic-unit-learning / acoustic-to-token`
**Evidence:** D3 full-paper capture; PDF SHA-256 `f5add729f4ae9e6e1b5f3bd182a567bd1b20b77cc0c26172659c4245e4b4c190`; full-text SHA-256 `5a2550d29e049d919f38904dcc4de414272db225f74e0c311e7c991cfd08d518`.

- **Ordinary problem:** Classroom speech may have thousands of hours of cheap imperfect transcripts and only a small amount of carefully corrected text.
- **Why it is hard:** Discarding weak transcripts wastes coverage, but trusting them as if every word were correct can teach systematic errors.
- **Naive attempt:** Use only the small gold set or train directly on all weak labels with no later correction.
- **Central move:** Pretrain on weak transcripts, then fine-tune on accurate data so broad coverage supplies structure and gold data corrects its errors.
- **Mechanism:** Weakly Supervised Pretraining uses 5,000 hours of noisy classroom transcripts followed by fine-tuning on a small accurate set; synthetic and real weak transcripts are compared.
- **Mathematical idea:** The two-stage schedule separates learning broad acoustic-to-token regularities from calibrating the final transcript against trusted labels.
- **What the paper reports:** The paper reports that WSP outperforms alternative strategies in synthetic and real weak-label settings for classroom ASR.
- **Limits:** Classroom domain, weak-label generation, gold-data size, transcript quality, and WER protocol bound the result; weak supervision can still reproduce systematic omissions or speaker bias.

## 294. Word stress in self-supervised speech models: A cross-linguistic comparison

**Paper:** [Word stress in self-supervised speech models: A cross-linguistic comparison](https://www.isca-archive.org/interspeech_2025/bentum25_interspeech.html)
**Taxonomy:** `recognition-and-alignment / acoustic-unit-learning / self-supervised-speech-units`
**Evidence:** D3 full-paper capture; PDF SHA-256 `7f0ad81d6a23019b42ab3d580f47fea45874e280d3083cbb814c8fb1c5dbfc7e`; full-text SHA-256 `83af12d19bc40667d476c4b199a5023422f671ae5d767155c11367466d9caebe`.

- **Ordinary problem:** A self-supervised speech representation may contain linguistically meaningful stress information, but it is not obvious which language-specific distinctions it encodes.
- **Why it is hard:** A high-performing downstream classifier can exploit shortcuts and does not by itself show what the representation has learned.
- **Naive attempt:** Treat the representation as an opaque feature vector and infer its linguistic content from end-task accuracy alone.
- **Central move:** Use simple diagnostic classifiers across languages and stress systems, then compare whether the encoded distinction changes with the language's stress structure.
- **Mechanism:** Wav2vec 2.0 embeddings are probed for stressed versus unstressed syllables in Dutch, English, German, Hungarian, and Polish.
- **Mathematical idea:** A diagnostic classifier tests recoverable information while cross-language comparison asks whether the representation reflects variable versus fixed or demarcative stress systems.
- **What the paper reports:** Stress is decoded with high accuracy, and the representations show language-specific differences, with a larger contrast between variable-stress and fixed-stress languages.
- **Limits:** Read-aloud sentences, languages, layer choices, probe capacity, and diagnostic accuracy bound the inference; recoverable information is not proof that the model uses stress causally.

## 295. DC-Spin: A Speaker-invariant Speech Tokenizer for Spoken Language Models

**Paper:** [DC-Spin: A Speaker-invariant Speech Tokenizer for Spoken Language Models](https://www.isca-archive.org/interspeech_2025/chang25_interspeech.html)
**Taxonomy:** `recognition-and-alignment / acoustic-unit-learning / acoustic-to-token`
**Evidence:** D3 full-paper capture; PDF SHA-256 `88aad8e6d427172d5732de884d2c9fd3a400cd91b841c6587beba1d5e2488223`; full-text SHA-256 `255050d3985740f2d5b1922d3b3211d2cd6e02e3374312087f9d179cc96eeca7`.

- **Ordinary problem:** A spoken-language model needs compact speech units that preserve phonetic content while ignoring who spoke and small recording changes.
- **Why it is hard:** Raw waveforms contain speaker, channel, and linguistic variation at the same time; a token that keeps all of it is hard for a language model to reuse.
- **Naive attempt:** Cluster acoustic frames directly and assume the most frequent clusters are good linguistic units.
- **Central move:** Use double-codebook speaker-invariant clustering to retain phonetic structure while suppressing speaker variation, then test whether the resulting tokens are easy to model and resynthesize.
- **Mechanism:** SpinHuBERT supplies the speech representation and DC-Spin separates speaker-invariant and phonetic information into codebooks; the tokens are tested in zero-shot spoken-language tasks and resynthesis.
- **Mathematical idea:** Clustering assigns nearby representation vectors to discrete symbols; speaker-invariance changes the training objective so distance caused by identity matters less than distance caused by phonetic content.
- **What the paper reports:** The paper reports that tokens with phoneme alignment or simple language-model structure are useful downstream and improve the tested zero-shot and resynthesis proxies.
- **Limits:** The tokenizers, languages, proxy tasks, and resynthesis setup bound the result; token usefulness is not the same as complete spoken meaning.

## 296. Decoding Speaker-Normalized Pitch from EEG for Mandarin Perception

**Paper:** [Decoding Speaker-Normalized Pitch from EEG for Mandarin Perception](https://www.isca-archive.org/interspeech_2025/chen25e_interspeech.html)
**Taxonomy:** `recognition-and-alignment / acoustic-unit-learning / acoustic-to-token`
**Evidence:** D3 full-paper capture; PDF SHA-256 `fd71b6f9dc9f781691734e49ead291b57fc9b0b29f4aaf1ae42a72922857791f`; full-text SHA-256 `3132ddf9dc440750b8add052bc9f3cf87a27cc127245458d0649485b173b1921`.

- **Ordinary problem:** Listeners must recognize tone and meaning even though different speakers use very different pitch ranges for the same linguistic content.
- **Why it is hard:** The brain may encode pitch relative to a speaker rather than as an absolute frequency; EEG decoding must separate speaker variation from linguistic tone and session noise.
- **Naive attempt:** Decode raw pitch as if one absolute frequency scale applies to every speaker.
- **Central move:** Record EEG during Mandarin speech perception and compare decoding of raw versus speaker-normalized pitch contours with a model that captures temporal context.
- **Mechanism:** The paper decodes speaker-normalized pitch from EEG during Mandarin perception.
- **Mathematical idea:** Perception can preserve a relational variable: normalization removes the speaker’s baseline while retaining the contour relation that carries linguistic information.
- **What the paper reports:** The proposed CE-ViViT approach achieved modest-error decoding, with speaker-normalized contours decoded more accurately than raw contours in the reported experiments.
- **Limits:** Participants, Mandarin tones, EEG sessions, normalization rule, model, and modest-error metric bound the neural claim; better decoding does not by itself reveal the full perceptual code.

## 297. DiceHuBERT: Distilling HuBERT with a Self-Supervised Learning Objective

**Paper:** [DiceHuBERT: Distilling HuBERT with a Self-Supervised Learning Objective](https://www.isca-archive.org/interspeech_2025/chi25_interspeech.html)
**Taxonomy:** `recognition-and-alignment / acoustic-unit-learning / self-supervised-speech-units`
**Evidence:** D3 full-paper capture; PDF SHA-256 `963cbd3bc74318c044302f225cc30409259cb8c4480940170c7ed15ea9479ca5`; full-text SHA-256 `69ed16e13f5f3b3c784e53bf7e27eea720b3fd309c7efebabf1f813c996d97f2`.

- **Ordinary problem:** A large self-supervised speech model may be useful but too expensive to store or run, so a smaller student must retain the teacher's reusable speech knowledge.
- **Why it is hard:** Layer-by-layer imitation adds alignment machinery and can force the student to copy the teacher's structure rather than its learning objective.
- **Naive attempt:** Compress each teacher layer with a separate matching module or simply shrink the network and accept lost representations.
- **Central move:** Replace the HuBERT teacher with a smaller student trained directly under HuBERT's iterative self-supervised objective.
- **Mechanism:** DiceHuBERT distills HuBERT using the same self-supervised objective and evaluates the compact model on phoneme recognition, ASR, and SUPERB tasks.
- **Mathematical idea:** The student learns the task's predictive structure instead of matching every hidden layer; downstream performance measures retained usefulness across tasks.
- **What the paper reports:** The paper reports over 21% improvement in phoneme recognition and over 14% in ASR relative to existing distillation methods, with competitive multi-task results.
- **Limits:** Teacher/student sizes, SUPERB tasks, training data, and comparison baselines bound the result; benchmark transfer does not establish equal behavior under every deployment constraint.

## 298. On-device Streaming Discrete Speech Units

**Paper:** [On-device Streaming Discrete Speech Units](https://www.isca-archive.org/interspeech_2025/choi25b_interspeech.html)
**Taxonomy:** `recognition-and-alignment / acoustic-unit-learning / self-supervised-speech-units`
**Evidence:** D3 full-paper capture; PDF SHA-256 `8ee6e6ed7092b62a31f86a6344fc77ff855a4e20648b15d5f69537015216ea80`; full-text SHA-256 `4042da76913b28a35121d2aee2fa5904946c626776b71494c2054fc7205908b9`.

- **Ordinary problem:** A speech model on a device must start processing before the whole utterance arrives and must fit limited compute, while retaining useful phonetic information.
- **Why it is hard:** Discrete units derived from large self-supervised models are powerful but normally require long context and expensive feature extraction; reducing them risks recognition errors and lost history.
- **Naive attempt:** Wait for the full recording and run the largest self-supervised encoder on every frame.
- **Central move:** Shrink the attention window and model size for streaming discrete speech units, measuring the compute reduction against recognition error.
- **Mechanism:** The paper develops on-device streaming discrete speech units.
- **Mathematical idea:** Streaming is a causal information constraint: the model must decide from the past available at each moment, so efficiency is not just compression but a change in what evidence can be used.
- **What the paper reports:** On ML-SUPERB 1h, the paper reports a 50% FLOP reduction for a 6.5% relative CER increase.
- **Limits:** Dataset size, causal window, unit clustering, hardware, FLOPs accounting, and CER bound practical generalization; the trade-off may change for other languages or latency targets.

## 299. Exploring auditory feedback mechanisms in speech recognition

**Paper:** [Exploring auditory feedback mechanisms in speech recognition](https://www.isca-archive.org/interspeech_2025/coppietersdegibson25_interspeech.html)
**Taxonomy:** `recognition-and-alignment / acoustic-unit-learning / acoustic-to-token`
**Evidence:** D3 full-paper capture; PDF SHA-256 `d6712056def5b6f5b1ece53b0927b5a67b40851b1988f65d42dba382297558e5`; full-text SHA-256 `102bc2f8bb1a03cdbb344fee3fb7b97d592986664c1bf15966721071d5177ce4`.

- **Ordinary problem:** Automatic speech recognition features should reflect how the ear and cochlea actually transform sound, not only a convenient filter bank.
- **Why it is hard:** The cochlea is nonlinear and includes feedback; adding biologically motivated mechanisms increases computation and may help recognition while also serving as a test of hearing hypotheses.
- **Naive attempt:** Treat the cochlea as a fixed bank of independent filters and ignore feedback loops.
- **Central move:** Add Hopf-oscillator compression and olivocochlear feedback mechanisms to an ASR front end, then compare recognition behavior and biological plausibility.
- **Mechanism:** The paper explores auditory feedback mechanisms in speech recognition.
- **Mathematical idea:** A speech front end can be both an engineering component and a biological experiment: a mechanism is interesting when it changes recognition in the direction predicted by auditory physiology.
- **What the paper reports:** The paper reports that adding the larger feedback loop appears beneficial for ASR, while describing the current implications as modest.
- **Limits:** Approximate oscillator model, compute limits, ASR task, feedback implementation, and modest gains bound interpretation; improved recognition does not validate the whole biological mechanism.

## 300. What do self-supervised speech models know about Dutch?  Analyzing advantages of language-specific pre-training

**Paper:** [What do self-supervised speech models know about Dutch?  Analyzing advantages of language-specific pre-training](https://www.isca-archive.org/interspeech_2025/deheerkloots25_interspeech.html)
**Taxonomy:** `recognition-and-alignment / acoustic-unit-learning / self-supervised-speech-units`
**Evidence:** D3 full-paper capture; PDF SHA-256 `269035621f200fb2c27dd37268ed3a051a9d13e2004e65d6d1003e338b687e36`; full-text SHA-256 `7cef93d062a84f73ddf4fcdf55f6cd334b5600e229274701190267ad50cc91c7`.

- **Ordinary problem:** A speech representation can encode phonetic and word information differently across languages and speaking styles.
- **Why it is hard:** Probe accuracy, downstream ASR, and corpus match can disagree, so one score cannot establish what a representation knows.
- **Naive attempt:** Use a multilingual representation as language-neutral and judge it by one WER.
- **Central move:** Compare English, multilingual, and Dutch self-supervised models with linguistic probes and downstream Dutch ASR across read and conversational speech.
- **Mechanism:** Hidden layers are probed for phonetic and lexical structure, then models are fine-tuned and evaluated on five Dutch test sets.
- **Mathematical idea:** The Dutch model WERs are 10.4 CGN-o, 65.6 IFADV, 15.4 MLS, 21.0 CV, and 25.2 N-Best; English is consistently worse.
- **What the paper reports:** Language-specific pretraining yields lower WER, while probe and fine-tuning rankings need not coincide.
- **Limits:** Models, Dutch corpora, probes, and fine-tuning limit generalization; decodability is not causal proof of ASR behavior.

## 301. Towards a Unified Benchmark for Arabic Pronunciation Assessment: Qur’anic Recitation as Case Study

**Paper:** [Towards a Unified Benchmark for Arabic Pronunciation Assessment: Qur’anic Recitation as Case Study](https://www.isca-archive.org/interspeech_2025/elkheir25b_interspeech.html)
**Taxonomy:** `recognition-and-alignment / acoustic-unit-learning / acoustic-to-token`
**Evidence:** D3 full-paper capture; PDF SHA-256 `6cc0700c7f7f6e7b108901409a751f5ccf2bec7265b3c16294af21b135a8c0bb`; full-text SHA-256 `8779dfd4e8948c29beaebc541b3eafd93f5e6538821bd54936c24faac2f9ff0b`.

- **Ordinary problem:** Qur'anic-recitation pronunciation assessment needs labels that map acoustic deviations to meaningful learner errors.
- **Why it is hard:** Specialized phonology and pronunciation norms make generic ASR labels insufficient.
- **Naive attempt:** Apply a general ASR benchmark or one pronunciation distance without task-specific labels.
- **Central move:** Construct a unified Arabic pronunciation-assessment benchmark around Qur'anic recitation.
- **Mechanism:** Audio, pronunciation targets, and assessment labels are aligned for model comparison.
- **Mathematical idea:** The relevant object is the acoustic-to-token evidence described by the paper's mechanism: Audio, pronunciation targets, and assessment labels are aligned for model comparison.
- **What the paper reports:** The paper presents a benchmark and case study for Arabic pronunciation assessment.
- **Limits:** Recitation tradition, annotation, coverage, and metrics bound transfer; automatic scores are not teacher judgment.

## 302. Improving End-to-end Mixed-case ASR with Knowledge Distillation and Integration of Voice Activity Cues

**Paper:** [Improving End-to-end Mixed-case ASR with Knowledge Distillation and Integration of Voice Activity Cues](https://www.isca-archive.org/interspeech_2025/novitasari25b_interspeech.html)
**Taxonomy:** `recognition-and-alignment / acoustic-unit-learning / acoustic-to-token`
**Evidence:** D3 full-paper capture; PDF SHA-256 `1885aa1452d24d1a1b89860875cbb6882fb5b2a5d677b58ef2258b9085700a80`; full-text SHA-256 `bc570146bf65331edc42813034405f4bf32fa3233ed02893dacd377450a8feef`.

- **Ordinary problem:** Written output from speech must include words, capitalization, and punctuation, but asking one recognizer to learn all three at once can damage the underlying word recognition.
- **Why it is hard:** Formatting decisions occur at different levels from phonetic recognition, and voice activity boundaries provide timing information that text-only decoding lacks.
- **Naive attempt:** Train directly on formatted transcripts and accept errors in both formatting and the words themselves.
- **Central move:** Distill word-recognition knowledge from an unformatted teacher into a formatted student and add voice-activity cues to support boundary and formatting decisions.
- **Mechanism:** A mixed-case end-to-end ASR student receives knowledge from a unicase teacher and voice-activity information; case-sensitive and insensitive outputs are measured.
- **Mathematical idea:** The system separates acoustic-to-word evidence from formatting supervision; word error and case/punctuation errors expose whether formatting harms recognition.
- **What the paper reports:** The method reports up to a 9.2% relative error reduction at comparable decoding cost.
- **Limits:** Training data, formatting conventions, teacher quality, decoding budget, and reported error definitions bound the result; punctuation accuracy is not the same as transcript understanding.

## 303. EnCodecMAE: leveraging neural codecs for universal audio representation learning

**Paper:** [EnCodecMAE: leveraging neural codecs for universal audio representation learning](https://www.isca-archive.org/interspeech_2025/pepino25_interspeech.html)
**Taxonomy:** `recognition-and-alignment / acoustic-unit-learning / self-supervised-speech-units`
**Evidence:** D3 full-paper capture; PDF SHA-256 `67cdae8bdb5d2e3ec550583599e2729db1c21d2dfab7d1d66855579e7f702db9`; full-text SHA-256 `648df1d4dd882aca1f7400301d1a7bd00d93547628f55169893904fd795d6abf`.

- **Ordinary problem:** One audio representation should support speech, music, and environmental sounds even though the useful information is different in each task.
- **Why it is hard:** A pretext target can make a representation good at reconstructing one signal while discarding information needed by another task.
- **Naive attempt:** Assume a larger model or a single input representation will be uniformly best everywhere.
- **Central move:** Use discrete targets from a neural codec in a masked autoencoder and test the representation across tasks, model sizes, input forms, self-training, and data mixtures.
- **Mechanism:** EnCodecMAE is pretrained on diverse audio and evaluated on pitch, genre, speech commands, emotion, sound events, and environmental sound tasks.
- **Mathematical idea:** Transfer performance is the test of usefulness; the representation is judged by how task, input, model size, and pretraining diversity change downstream accuracy or error.
- **What the paper reports:** The paper reports average gains over prior audio representations and finds that larger models, task-dependent inputs, self-training, and diverse data each matter.
- **Limits:** The task suite, pretraining mixture, labels, model comparisons, and aggregate averages bound the claim; average transfer does not prove universal suitability for speech.

## 304. WhisperD: Dementia Speech Recognition and Filler Word Detection with Whisper

**Paper:** [WhisperD: Dementia Speech Recognition and Filler Word Detection with Whisper](https://www.isca-archive.org/interspeech_2025/akinrintoyo25_interspeech.html)
**Taxonomy:** `recognition-and-alignment / boundaries-and-alignment / disfluency-preservation`
**Evidence:** D3 full-paper capture; PDF SHA-256 `e0408484dc96cb89766940fa37f08781aaacb45af7a2809baa563059091d76b5`; full-text SHA-256 `c9e6efa122556ad801300a0c435dae9aaf09a6ebb43d46c27f9cabe7967b4256`.

- **Ordinary problem:** Transcribe dementia speech while retaining filler words that may matter for clinical analysis and supportive interaction.
- **Why it is hard:** Dementia speech includes pauses, repetitions, fragmented sentences, and unclear words unlike the standard speech used to train Whisper.
- **Naive attempt:** Apply an off-the-shelf ASR model and discard fillers as noise.
- **Central move:** Fine-tune Whisper on DementiaBank and an in-house dataset, explicitly evaluating filler inclusion and F1 as well as WER.
- **Mechanism:** Shorter training clips adapt the model to fragmented speech; transcripts are scored for word errors and filler detection.
- **Mathematical idea:** WER measures transcription errors while FIR/F1 measure whether clinically relevant fillers are retained and detected.
- **What the paper reports:** The paper reports a medium model WER of 0.24 and stronger results than off-the-shelf models in its evaluation.
- **Limits:** The dataset is 11.39 hours, some audio is mumbled or unintelligible, and diagnostic or clinical benefit is not established by ASR scores alone.

## 305. ASR-based segmentation for the analysis of larger child-speech datasets: Performance evaluation on vowels from Australian-English speaking children aged 4 to 11 years

**Paper:** [ASR-based segmentation for the analysis of larger child-speech datasets: Performance evaluation on vowels from Australian-English speaking children aged 4 to 11 years](https://www.isca-archive.org/interspeech_2025/cai25_interspeech.html)
**Taxonomy:** `recognition-and-alignment / boundaries-and-alignment / alignment`
**Evidence:** D3 full-paper capture; PDF SHA-256 `1a3627d4390a69a3fd7b6afe68cfab8bf1aab47051a0667c7379724953a43cbc`; full-text SHA-256 `3342c10608c5d9faf8f565909764a7cbdd393a16ad4236ab36be711e4221ca92`.

- **Ordinary problem:** Large child-speech collections need segment boundaries, but an adult-trained aligner may place those boundaries according to a different rule than a human analyst.
- **Why it is hard:** Children's articulation and developmental variation make forced alignment less stable, and disagreement can change measured vowel durations or trajectories.
- **Naive attempt:** Treat an adult forced aligner as interchangeable with manual annotation.
- **Central move:** Compare human-human reliability with manual-versus-Montreal-Forced-Aligner boundaries across child ages and inspect systematic discrepancies.
- **Mechanism:** The study evaluates vowel boundaries in Australian-English child speech and asks how alignment error changes from ages four to eleven.
- **Mathematical idea:** The conceptual issue is not simply alignment accuracy: a boundary is an analytic decision whose meaning must be shared by the tool and the human measurement protocol.
- **What the paper reports:** The paper reports that MFA falls short of human annotation, with smaller discrepancies for older children.
- **Limits:** The evidence is tied to the tested vowels, ages, language variety, and annotators; it supports semi-automatic caution rather than universal aligner failure.

## 306. Song Form-aware Full-Song Text-to-Lyrics Generation with Multi-Level Granularity Syllable Count Control

**Paper:** [Song Form-aware Full-Song Text-to-Lyrics Generation with Multi-Level Granularity Syllable Count Control](https://www.isca-archive.org/interspeech_2025/chae25_interspeech.html)
**Taxonomy:** `recognition-and-alignment / boundaries-and-alignment / alignment`
**Evidence:** D3 full-paper capture; PDF SHA-256 `8d7a8f40fd501d1c207c594ba4f7b056d0c009695222ddc9b7785661692f6410`; full-text SHA-256 `f1c2cdbe47501a0432a5c569d0238a9e49d657892d0a6849e075ff5b7838d902`.

- **Ordinary problem:** Lyrics must say something coherent while fitting a song’s verse, chorus, and line-level syllable pattern; ordinary line-by-line text generation often breaks the musical form.
- **Why it is hard:** Syllables constrain several nested units at once, so satisfying a line can damage a phrase or chorus, and semantic coherence must survive the edits.
- **Naive attempt:** Generate each line independently and count syllables only after generation.
- **Central move:** Generate complete lyrics conditioned on text and song form while controlling syllable counts at word, phrase, line, and paragraph levels.
- **Mechanism:** The paper proposes song-form-aware full-song lyrics generation with multi-level syllable control.
- **Mathematical idea:** The output is a structured object: constraints at smaller units must compose into a song-level form, rather than being repaired after a generic text model has already committed to lines.
- **What the paper reports:** The paper reports controlled lyrics-generation experiments and makes generated samples available for inspection.
- **Limits:** Text prompts, song forms, syllable-count rules, dataset construction, and evaluation criteria bound the claim; syllable fit is not the same as singability, musicality, or authorship.

## 307. A semi-automatic pipeline for transcribing and segmenting child speech

**Paper:** [A semi-automatic pipeline for transcribing and segmenting child speech](https://www.isca-archive.org/interspeech_2025/christodoulidou25_interspeech.html)
**Taxonomy:** `recognition-and-alignment / boundaries-and-alignment / alignment`
**Evidence:** D3 full-paper capture; PDF SHA-256 `b81ad4f3ec8943df20ccde351cc256baf68fdc150dd328cdc28fba1fb424728d`; full-text SHA-256 `05af921b309ca0d30845e4b664a527c9347c2374b9c99a26cdb8b311d1c153e8`.

- **Ordinary problem:** A field study needs reliable vowel measurements from children's dialect speech even when recordings are noisy and automatic transcripts are imperfect.
- **Why it is hard:** Child speech, non-standard dialect, and field conditions shift the acoustic and language distributions assumed by pretrained transcription and alignment models.
- **Naive attempt:** Run an off-the-shelf ASR and forced aligner and treat every predicted boundary as ground truth.
- **Central move:** Correct the transcript before forced alignment and adapt the acoustic model toward child speech, then compare automatic measurements with manual annotations.
- **Mechanism:** WhisperX supplies a transcription, manual correction changes the lexical scaffold, and MFA places segment boundaries; adaptation changes the acoustic model used for alignment.
- **Mathematical idea:** The pipeline separates lexical uncertainty from boundary uncertainty: a better transcript and a better acoustic model affect the measured vowel interval through different paths.
- **What the paper reports:** Manual transcript correction improves acoustic vowel measures, and adaptation of the pretrained MFA model helps, while merely increasing the adaptation sample does not add the same improvement.
- **Limits:** The 275-child Scottish-English field corpus, manual reference quality, recording conditions, and selected vowel measures bound transfer; alignment quality is not a complete child-speech recognizer evaluation.

## 308. SiamCTC:  Learning Speech Representations through Monotonic Temporal Alignment

**Paper:** [SiamCTC:  Learning Speech Representations through Monotonic Temporal Alignment](https://www.isca-archive.org/interspeech_2025/eom25_interspeech.html)
**Taxonomy:** `recognition-and-alignment / boundaries-and-alignment / alignment`
**Evidence:** D3 full-paper capture; PDF SHA-256 `0f06a96c93d3f4f735dd7b1efba279f31dc94e92961b6fca19df2f332a29a2ad`; full-text SHA-256 `dad3132ee8f62a5b49ee06a177dac55d179bbcabd3bf0d832190ccfd4e8ed373`.

- **Ordinary problem:** A speech representation should recognize the same linguistic content when the speaker talks faster or slower.
- **Why it is hard:** Two views can have different frame counts, so frame-to-frame equality treats timing variation as content change.
- **Naive attempt:** Align every augmented frame to its counterpart and penalize harmless shifts.
- **Central move:** Use CTC to learn a flexible monotonic alignment between views inside a Siamese learner.
- **Mechanism:** Two encoders produce sequences and CTC sums over valid monotonic paths while training the representations to agree at content level.
- **Mathematical idea:** A monotonic path preserves temporal order while allowing variable durations; it is a soft alignment over possible boundaries.
- **What the paper reports:** SiamCTC improves representation robustness at diverse speaking rates in the reported experiments.
- **Limits:** Augmentation, language, CTC targets, downstream tasks, and rate range bound transfer; robustness is not universal recognition accuracy.

## 309. Towards Multi-Level Transcript Segmentation: LoRA Fine-Tuning for Table-of-Contents Generation

**Paper:** [Towards Multi-Level Transcript Segmentation: LoRA Fine-Tuning for Table-of-Contents Generation](https://www.isca-archive.org/interspeech_2025/freisinger25_interspeech.html)
**Taxonomy:** `recognition-and-alignment / boundaries-and-alignment / alignment`
**Evidence:** D3 full-paper capture; PDF SHA-256 `9bd21deab64e665950eff969da93cf701f3445a323d0445b98b095fcc38467c8`; full-text SHA-256 `3ace804507e5ad21cb4928a63b80aed82271081c58ca8d321c3853daf203191d`.

- **Ordinary problem:** Long transcripts are easier to use when topics are organized into nested sections rather than one flat stream.
- **Why it is hard:** Spoken transcripts lack visible chapters, boundaries are ambiguous, and coarse and fine topic changes must be represented across languages and recordings.
- **Naive attempt:** Predict one boundary label at each position and evaluate only whether a nearby cut is correct.
- **Central move:** Generate a hierarchical table of contents and use a metric that respects its levels; add pause duration only when training can use it.
- **Mechanism:** TOC-NEMO uses LoRA fine-tuning and optional pause cues on AMI, VideoAula, and LectureDE; zero-shot prompting and supervised baselines provide comparisons.
- **Mathematical idea:** Linear F1/B and hierarchical B distinguish flat boundary quality from agreement across levels; bootstrap and leave-one-speaker-out averages are reported.
- **What the paper reports:** Fine-tuned TOC-NEMO plus pause cues reports the strongest linear scores, including AMI F1 30.34/B 24.81 and VideoAula F1 67.34/B 55.18.
- **Limits:** Datasets, prompts, annotations, and metric behavior constrain the result; transcript segmentation is not proof of human topic understanding.

## 310. The Multimodal Information Based Speech Processing (MISP) 2025 Challenge: Audio-Visual Diarization and Recognition

**Paper:** [The Multimodal Information Based Speech Processing (MISP) 2025 Challenge: Audio-Visual Diarization and Recognition](https://www.isca-archive.org/interspeech_2025/gao25g_interspeech.html)
**Taxonomy:** `recognition-and-alignment / boundaries-and-alignment / alignment`
**Evidence:** D3 full-paper capture; PDF SHA-256 `387be447fcc2bd5585d1f5c40075a75829c62d816cc6641d2fcafa0adc28e599`; full-text SHA-256 `2cdc0cbf3c3d6e1276816acce6e6d60ef818dd22eba1f722ea6181a1fa1ab7c4`.

- **Ordinary problem:** Meeting transcription must determine both what was said and which person said it when cameras, microphones, overlap, and devices disagree.
- **Why it is hard:** Recognition and speaker assignment fail together under overlap, and a separate audio-only pipeline cannot use visible mouth and body evidence.
- **Naive attempt:** Transcribe the mixed audio first and attach speaker labels afterward.
- **Central move:** Fuse audio and video across diarization, recognition, and joint diarization-recognition tasks, then compare systems under a shared challenge protocol.
- **Mechanism:** MISP 2025 defines AVSD, AVSR, and AVDR tasks with multi-device meeting data; systems combine acoustic and visual streams and are scored on speaker attribution and transcription.
- **Mathematical idea:** Diarization error counts missed, false, and incorrectly attributed speech; character error measures transcript edits; concatenated minimum-permutation error resolves arbitrary speaker-label names.
- **What the paper reports:** The challenge reports DER 8.09%, CER 9.48%, and cpCER 11.56% for its top systems, with the largest gain in the joint task.
- **Limits:** Challenge data, camera placement, meeting types, language, and leaderboard protocols define the claim; deployment in unseen rooms or privacy-constrained camera settings remains open.

## 311. StutterCut: Uncertainty-Guided Normalised Cut for Dysfluency Segmentation

**Paper:** [StutterCut: Uncertainty-Guided Normalised Cut for Dysfluency Segmentation](https://www.isca-archive.org/interspeech_2025/ghosh25_interspeech.html)
**Taxonomy:** `recognition-and-alignment / boundaries-and-alignment / disfluency-preservation`
**Evidence:** D3 full-paper capture; PDF SHA-256 `6cccda140047cade5dceec0636c8e468b51590d78f5b4489ab76eeac13ff71c8`; full-text SHA-256 `e30d10d77593a898a8cfe69b9df808f751291793d204225434153e1939e2812c`.

- **Ordinary problem:** Therapy and feedback need to know where a dysfluency begins and ends, not only whether an entire utterance contains one.
- **Why it is hard:** Only weak utterance labels are common, while real dysfluency boundaries are uncertain and synthetic timing is unrealistic.
- **Naive attempt:** Classify each utterance or trust every weak label as if it gave exact frame boundaries.
- **Central move:** Turn overlapping speech windows into a graph, use a weakly trained classifier to refine links, and reduce its influence when it is uncertain.
- **Mechanism:** StutterCut uses uncertainty-guided normalized cuts and adds frame-level boundaries for four dysfluency types to FluencyBank.
- **Mathematical idea:** Graph partitioning separates regions; Monte Carlo dropout estimates uncertainty, and F1 plus onset error measure segmentation quality.
- **What the paper reports:** The paper reports higher F1 and more precise stuttering-onset detection on real and synthetic data.
- **Limits:** The evidence is bounded to FluencyBank, four dysfluency types, annotation quality, and the tested uncertainty model; therapy outcomes and new speakers remain open.

## 312. Transcript-Prompted Whisper with Dictionary-Enhanced Decoding for Japanese Speech Annotation

**Paper:** [Transcript-Prompted Whisper with Dictionary-Enhanced Decoding for Japanese Speech Annotation](https://www.isca-archive.org/interspeech_2025/hu25_interspeech.html)
**Taxonomy:** `recognition-and-alignment / boundaries-and-alignment / alignment`
**Evidence:** D3 full-paper capture; PDF SHA-256 `2bf1d8afae46fbec8812e9c627ec5f7add03fd57ecd9b881b66a7a12c7ae098b`; full-text SHA-256 `0c85c619f48f82f99f63ac2e156e7882e0b49b176dc5ea959216664c75d2bdfc`.

- **Ordinary problem:** A Japanese TTS dataset needs phonemic and prosodic labels aligned to speech, but manually adding those labels is slow and ASR text alone does not say how a phrase was pronounced.
- **Why it is hard:** Pronunciation and prosody are coupled to phrase boundaries and context, and an ASR transcript can contain errors that propagate into annotation.
- **Naive attempt:** Use a dictionary-only grapheme-to-phoneme process or annotate every recording by hand without exploiting the transcript already available.
- **Central move:** Condition a pretrained ASR model on the ground-truth transcript so it emits phrase-level graphemes and labels together, then use dictionary-enhanced decoding to correct phonemic labels.
- **Mechanism:** Transcript-Prompted Whisper fine-tunes a large ASR model for simultaneous phrase and annotation output and applies a dictionary-based correction stage for Japanese speech-data construction.
- **Mathematical idea:** The transcript acts as a constraint on what was said while the audio supplies pronunciation and prosody; joint sequence output makes boundaries and labels part of one decoding problem.
- **What the paper reports:** The paper reports improved phonemic/prosodic annotation behavior and a practical pipeline for constructing Japanese TTS data from audio-transcript pairs.
- **Limits:** Ground-truth transcript quality, dictionary coverage, Japanese phonology, label definitions, and annotation evaluation bound the result; automatic labels still require quality control before becoming training truth.

## 313. Word Level Timestamp Generation for Automatic Speech Recognition and Translation

**Paper:** [Word Level Timestamp Generation for Automatic Speech Recognition and Translation](https://www.isca-archive.org/interspeech_2025/hu25e_interspeech.html)
**Taxonomy:** `recognition-and-alignment / boundaries-and-alignment / alignment`
**Evidence:** D3 full-paper capture; PDF SHA-256 `d76d5c2a6e71d534e2fa694e5cd9fe27baa383fa1616d7de14ed09276bbacc92`; full-text SHA-256 `3f7af66d1de938b2d0c19ec715479ef680bee76f549a9178db751f486be44c84`.

- **Ordinary problem:** Speech recognition and translation systems need word boundaries and timestamps for retrieval, subtitles, and downstream editing without a separate forced-aligner at inference time.
- **Why it is hard:** Timestamp prediction must preserve word order while generating content, and errors in one boundary can shift every later timestamp.
- **Naive attempt:** Attach an external aligner after decoding or force the sequence model to emit timestamps without a training signal for their timing semantics.
- **Central move:** Use a forced aligner as a teacher to create timestamp supervision, add a timestamp token, and train the end-to-end Canary model to emit start and end times with words.
- **Mechanism:** Teacher-generated word intervals become sequence targets; the model's timestamp tokens interleave with recognized or translated content, allowing boundary prediction inside the decoder.
- **Mathematical idea:** Alignment quality is measured against teacher or reference timing and downstream recognition/translation behavior, testing whether an integrated decoder can replace a separate alignment stage.
- **What the paper reports:** The paper reports word-level timestamp generation for Canary with the proposed token and teacher-supervised training in the evaluated ASR/translation settings.
- **Limits:** Teacher timing quality, tokenization, language, speaking rate, and evaluation alignment constrain transfer; timestamp agreement does not by itself prove subtitle readability or translation quality.

## 314. VoiceNet: Multilingual On-Device Phoneme-To-Audio Alignment

**Paper:** [VoiceNet: Multilingual On-Device Phoneme-To-Audio Alignment](https://www.isca-archive.org/interspeech_2025/jin25b_interspeech.html)
**Taxonomy:** `recognition-and-alignment / boundaries-and-alignment / alignment`
**Evidence:** D3 full-paper capture; PDF SHA-256 `5787b4dfc7cb4152ead1dcd02b91ba63f001855de83efd06d3a11a5eb3b5f09c`; full-text SHA-256 `035f3205ed9207fda3ae258f1e30dc9b289329d82ec5201d183825a47569a3cc`.

- **Ordinary problem:** An avatar or speech tool needs phoneme boundaries quickly on-device, sometimes without a transcript and across languages.
- **Why it is hard:** Recognition and alignment must share computation, multilingual phonetics vary, and mobile latency limits model size.
- **Naive attempt:** Run a large offline aligner or require text and a separate recognizer before placing boundaries.
- **Central move:** Train an end-to-end model for phoneme recognition and text-independent forced alignment, with optional text conditioning.
- **Mechanism:** VoiceNet predicts phoneme evidence and timing on-device; text adds a constraint when available, and device tests expose latency.
- **Mathematical idea:** Alignment is ordered interval inference rather than a post-processing attachment to recognition.
- **What the paper reports:** The paper reports competitive multilingual alignment and 6 ms average CPU phoneme inference on Galaxy devices.
- **Limits:** Device, language, phoneme inventory, transcript availability, and splits bound transfer; latency is not alignment quality.

## 315. Who knows best? Effects of speech disfluencies on incentivized decision-making

**Paper:** [Who knows best? Effects of speech disfluencies on incentivized decision-making](https://www.isca-archive.org/interspeech_2025/kirkland25_interspeech.html)
**Taxonomy:** `recognition-and-alignment / boundaries-and-alignment / disfluency-preservation`
**Evidence:** D3 full-paper capture; PDF SHA-256 `e1bec7608bd14b085b60809e14b8508c4523ffc3f40202a91dcccaf4d4162f09`; full-text SHA-256 `c748b4073cd0816aef673c78ed9dd366fe029b0464c049cd05198a9a6153003b`.

- **Ordinary problem:** Listeners may use pauses and disfluencies as evidence when deciding whom or what to believe, so removing them can change behavior rather than merely readability.
- **Why it is hard:** Prior ratings of competence do not show whether speech cues affect consequential choices, and credibility judgments interact with source conflict and incentives.
- **Naive attempt:** Normalize all disfluent speech before evaluation or infer real-world behavior from Likert ratings alone.
- **Central move:** Use an incentivized web decision task with conflicting information and compare choices as a function of speech fluency.
- **Mechanism:** The experiment treats disfluency as part of the observed communication signal and measures choice behavior rather than only an attitude rating.
- **Mathematical idea:** Behavioral choice is a downstream proxy: it tests whether a listener’s interpretation of fluency changes action under incentives.
- **What the paper reports:** The study reports that listeners take speech fluency into account when deciding whom or what to believe.
- **Limits:** Task stakes, speakers, disfluency types, online sample, and source-conflict design bound transfer; choice bias is not proof that disfluencies carry truthful information.

## 316. What the Filler? Both ASR Systems and Humans Struggle More With Other Kinds of Disfluencies Than With Filler Particles

**Paper:** [What the Filler? Both ASR Systems and Humans Struggle More With Other Kinds of Disfluencies Than With Filler Particles](https://www.isca-archive.org/interspeech_2025/wepner25_interspeech.html)
**Taxonomy:** `recognition-and-alignment / boundaries-and-alignment / disfluency-preservation`
**Evidence:** D3 full-paper capture; PDF SHA-256 `971503f9d8ab2eb0d22459b7a4c707db568a2fe51b8f2c3b23cdbcd4b93b0e59`; full-text SHA-256 `a935a798e358ee7e2abc2c5b349e158da78dc906a7ab792ff267bee35a73f462`.

- **Ordinary problem:** Conversational ASR and human transcription should account for syntactic disfluencies and filler particles.
- **Why it is hard:** Pauses, repairs, pronunciation, and articulation rate interact, so a global WER can hide which local structures cause errors.
- **Naive attempt:** Collapse all disfluencies into fluent text or treat filler presence as the sole explanatory variable.
- **Central move:** Present the same disfluent utterances to human listeners and multiple ASR systems, and compare error patterns across structure and acoustic factors.
- **Mechanism:** The matched transcription experiment uses participant recall and ASR WER to compare shared difficulty patterns.
- **Mathematical idea:** Disfluency is sequence evidence: preserving its position and type lets recognition error be related to conversational structure.
- **What the paper reports:** The paper reports similar difficulty characteristics for humans and ASR and no WER effect from filler presence alone.
- **Limits:** 54 listeners, nine systems, utterance design, languages, and WER/recall definitions bound transfer; matched error patterns do not establish cognitive equivalence.

## 317. Domain Adaptation Method and Modality Gap Impact in Audio-Text Models for Prototypical Sound Classification

**Paper:** [Domain Adaptation Method and Modality Gap Impact in Audio-Text Models for Prototypical Sound Classification](https://www.isca-archive.org/interspeech_2025/acevedo25_interspeech.html)
**Taxonomy:** `recognition-and-alignment / context-and-open-vocabulary / domain-and-context-biasing`
**Evidence:** D3 full-paper capture; PDF SHA-256 `228720572e58e79cf52af2b5ad83741a15149b53cf2613fb81f7cf165fdf7d3b`; full-text SHA-256 `78648e6d814f1a23d898773215d62f05e4485c4fe2b8402b7f6d30c9f891d58f`.

- **Ordinary problem:** Audio-text classifiers fail when the acoustic domain changes even if the label vocabulary stays fixed.
- **Why it is hard:** The text embedding can remain stable while the audio embedding moves with background and SNR.
- **Naive attempt:** Tune only text prompts or assume a frozen audio-text embedding is domain invariant.
- **Central move:** Adapt the audio side using representative target-domain sound examples and test transfer across environments.
- **Mechanism:** The method aligns audio representations to the target domain and compares audio-based with text-based adaptation.
- **Mathematical idea:** Top-1 accuracy across environments and SNRs measures whether adaptation closes the modality/domain gap; the zero-shot reference is 32.4%.
- **What the paper reports:** Audio-based adaptation gives the largest reported gains across tested conditions.
- **Limits:** Sound set, target examples, class construction, and reported accuracy limit open-world claims.

## 318. Spot and Merge: A Hybrid Context Biasing Approach for Rare Word and Out of Vocabulary Recognition

**Paper:** [Spot and Merge: A Hybrid Context Biasing Approach for Rare Word and Out of Vocabulary Recognition](https://www.isca-archive.org/interspeech_2025/agrawal25b_interspeech.html)
**Taxonomy:** `recognition-and-alignment / context-and-open-vocabulary / domain-and-context-biasing`
**Evidence:** D3 full-paper capture; PDF SHA-256 `84106aa02c63bb5eb30400ffc26ad417253274408fe172b7d514b45ea2fe40c6`; full-text SHA-256 `cab6ab21bec0f4db5fc6f5b8760bc8ea0ad7d764c9820cbfc3296d35b1d3314c`.

- **Ordinary problem:** Recognize rare business words and out-of-vocabulary terms in contact-center ASR.
- **Why it is hard:** Large biasing lists and unseen token sequences make contextual recognition difficult, especially when full ASR retraining is impractical.
- **Naive attempt:** Use shallow fusion or fully retrain a biasing module, sacrificing either internal context use or deployment flexibility.
- **Central move:** Use LoRA adaptation and a spot-and-merge method that detects bias phrases in cross-attention and merges them with ASR output.
- **Mechanism:** Attention weights identify likely bias phrases; the method combines those candidates with the base transcription and uses an auxiliary attention loss.
- **Mathematical idea:** WER measures word errors; OOV F1 measures detection of unseen terms. LoRA changes a small parameter subset rather than the whole recognizer.
- **What the paper reports:** The paper reports a 1.0% absolute WER reduction on LibriSpeech and improved OOV recognition on in-house contact-center data.
- **Limits:** The in-house data are not independently available in this atlas, and future multilingual/low-resource extension remains open.

## 319. Continuous Learning for Children's ASR: Overcoming Catastrophic Forgetting with Elastic Weight Consolidation and Synaptic Intelligence

**Paper:** [Continuous Learning for Children's ASR: Overcoming Catastrophic Forgetting with Elastic Weight Consolidation and Synaptic Intelligence](https://www.isca-archive.org/interspeech_2025/ahadzi25_interspeech.html)
**Taxonomy:** `recognition-and-alignment / context-and-open-vocabulary / speaker-adaptation`
**Evidence:** D3 full-paper capture; PDF SHA-256 `8abee8957844f00f0860523ba28fbeab11a9fe16d11ec7e8e193020b3e21cff6`; full-text SHA-256 `3b4b12d2222cc3aa0c17a57b3c27e37b4e5998851e51238beb09f224a5d14bc3`.

- **Ordinary problem:** A child-focused ASR service may receive speech over time, but updating it can make it forget earlier speakers and require centralized storage.
- **Why it is hard:** Children's speech changes with development, data are scarce, and sequential speakers create drift; ordinary fine-tuning overwrites useful parameters.
- **Naive attempt:** Fine-tune the latest model on each new batch and keep only the newest checkpoint.
- **Central move:** Protect parameters important for earlier batches with EWC or SI, and compare online checkpoint-selection policies.
- **Mechanism:** Whisper-small trains on ten sequential MyST batches. EWC adds an importance-weighted quadratic penalty; SI accumulates importance from parameter movement and loss reduction; models use no selection, rolling-window, or best-so-far selection.
- **Mathematical idea:** MyST has 145.54 training hours, 23.09 development hours, and 25.05 test hours. EWC and SI report relative WER reductions of 5.21% and 4.36% against sequential fine-tuning; bootstrap intervals quantify uncertainty.
- **What the paper reports:** EWC and SI keep WER more stable across ten batches and improve over ordinary sequential fine-tuning under the protocol.
- **Limits:** The protocol is simulated from MyST, uses English child speech and Whisper-small, and treats parameter importance as a proxy rather than a privacy guarantee.

## 320. NGPU-LM: GPU-Accelerated N-Gram Language Model for Context-Biasing in Greedy ASR Decoding

**Paper:** [NGPU-LM: GPU-Accelerated N-Gram Language Model for Context-Biasing in Greedy ASR Decoding](https://www.isca-archive.org/interspeech_2025/bataev25_interspeech.html)
**Taxonomy:** `recognition-and-alignment / context-and-open-vocabulary / domain-and-context-biasing`
**Evidence:** D3 full-paper capture; PDF SHA-256 `a607c37d61f73800165c1f8932173e76595e9c85181cc2d04d318c639fafeba5`; full-text SHA-256 `1e790a538801b8f51e501aa845ba2fd398192cf1b03d4e58aa5c7dfaad3444e7`.

- **Ordinary problem:** A recognizer must recognize rare or domain-specific words without paying the full cost of beam search on every utterance.
- **Why it is hard:** Greedy decoding is cheap but loses context; beam search recovers some context at a large compute cost.
- **Naive attempt:** Use beam search everywhere, or add a sequential language model whose data structure serializes every transition.
- **Central move:** Represent n-gram transitions for parallel GPU lookup and inject their scores into greedy decoding for CTC, transducer, and attention models.
- **Mechanism:** NGPU-LM uses hash-based transition lookup and customizable greedy decoding so context biasing can recover domain words with less than 7% reported overhead.
- **Mathematical idea:** The conceptual trade is between linguistic context and decoding latency; data structure and hardware choices move that boundary without changing the acoustic model.
- **What the paper reports:** The paper reports recovery of more than half the greedy/beam accuracy gap in out-of-domain tests and up to 10.6% relative WER improvement in its experiments.
- **Limits:** The results depend on tested ASR architectures, domains, GPU implementation, and author-reported measurements; deployment energy and other hardware remain open.

## 321. Bidirectional Spoken-Written Text Conversion with Large Language Models

**Paper:** [Bidirectional Spoken-Written Text Conversion with Large Language Models](https://www.isca-archive.org/interspeech_2025/choi25g_interspeech.html)
**Taxonomy:** `recognition-and-alignment / context-and-open-vocabulary / long-context-decoding`
**Evidence:** D3 full-paper capture; PDF SHA-256 `46dd7b70401166c9f07ac62da465afe83ce6da56447d82869ce7282efbbd152f`; full-text SHA-256 `acf3bbddc7bdec593345d1ba17b290a956997aa2c6189a29ed155b74f8db1371`.

- **Ordinary problem:** A recognizer should handle both spoken-form and written-form transcripts without inconsistent normalization of numbers, names, or punctuation.
- **Why it is hard:** Speech databases often contain one transcription convention while modern models emit another, and manually building paired forms is expensive.
- **Naive attempt:** Train on whichever transcript convention is available or attach a one-way text-normalization postprocessor.
- **Central move:** Use LLM-generated dual transcriptions, iterative supervised/semi-supervised expansion, and a bidirectional text-conversion model supporting both ITN and TN.
- **Mechanism:** The model learns mappings in both directions; generated paired text supplies supervision while iterative learning enlarges the conversion data.
- **Mathematical idea:** The central object is a representation boundary between spoken language and written conventions, not a change to the acoustic evidence itself.
- **What the paper reports:** The paper reports a 13.4% ERR improvement in the evaluated conversion setting.
- **Limits:** LLM generation quality, language conventions, error metric, transcript domain, and iterative-label bias bound transfer; normalization success is not ASR acoustic accuracy.

## 322. Effect of Loudspeaker Emitted Speech on ASR performance

**Paper:** [Effect of Loudspeaker Emitted Speech on ASR performance](https://www.isca-archive.org/interspeech_2025/cm25_interspeech.html)
**Taxonomy:** `recognition-and-alignment / context-and-open-vocabulary / domain-and-context-biasing`
**Evidence:** D3 full-paper capture; PDF SHA-256 `ba177e974c1652435b81689a3b1d2636da6b518d72992c736b12d3e348b0e9fd`; full-text SHA-256 `d5a01fc61c2d634008d1adc59c151a47e2307e7bcd25550bb0a51af6b4ad4fce`.

- **Ordinary problem:** An ASR system should recognize speech played through a loudspeaker, not only clean speech recorded directly by a microphone.
- **Why it is hard:** Loudspeaker playback changes the acoustic path and can add coloration, reverberation, and level differences that the recognizer may mistake for speech variation.
- **Naive attempt:** Train and test on direct recordings, then assume the model will transfer to playback speech.
- **Central move:** Measure the distribution shift caused by loudspeaker emission and evaluate recognition under that realistic channel.
- **Mechanism:** The paper studies ASR performance for loudspeaker-emitted speech and compares recognition across the tested playback conditions.
- **Mathematical idea:** Word error rate exposes the channel penalty; the useful distinction is speech content versus the acoustic path that carries it.
- **What the paper reports:** The paper reports a measurable ASR impact from loudspeaker emission under its experimental conditions.
- **Limits:** The result is bounded to the loudspeaker, room, microphones, and ASR systems tested; other devices and adaptive compensation remain open.

## 323. Exploring SSL Discrete Speech Features for Zipformer-based Contextual ASR

**Paper:** [Exploring SSL Discrete Speech Features for Zipformer-based Contextual ASR](https://www.isca-archive.org/interspeech_2025/cui25_interspeech.html)
**Taxonomy:** `recognition-and-alignment / context-and-open-vocabulary / long-context-decoding`
**Evidence:** D3 full-paper capture; PDF SHA-256 `3f2170f5278bed1b1972570a7f0b1116f2b534c5ed21531693d330b48f96ccf7`; full-text SHA-256 `d76952e38cff16ad17986ac6d3dcc208941789745bbf632bc3791690036c41ce`.

- **Ordinary problem:** A recognizer often needs the previous and next utterances to resolve names, references, or conversational context, but the context representation must be compact enough to train and run efficiently.
- **Why it is hard:** Continuous hidden features carry useful detail but are expensive, while a discrete representation may discard the very context needed for a difficult utterance.
- **Naive attempt:** Ignore cross-utterance context, concatenate every hidden vector, or use a large continuous speech model and accept its training cost.
- **Central move:** Compare discrete speech tokens and continuous features for pooled or concatenated context in a Zipformer-Transducer, measuring both recognition gains and efficiency.
- **Mechanism:** The study evaluates contextual Z-T systems on 1,000-hour GigaSpeech-M and DementiaBank Pitt elderly speech, using SSL discrete tokens, WavLM features, and preceding/current/future context variants.
- **Mathematical idea:** Context is a sequence decision: the representation must preserve the distinctions useful for the next utterance while reducing the number of values passed to the recognizer; WER and training time expose the tradeoff.
- **What the paper reports:** Discrete-token contextual systems reduce WER by 0.39 and 1.41 absolute points on the two tasks and achieve up to 4.36x training speedup over continuous WavLM context systems.
- **Limits:** Corpora, context windows, tokenization, speed hardware, and statistical test bound the result; better contextual WER does not prove robust dialogue understanding or causal use of future context in deployment.

## 324. Robust fine-tuning of speech recognition models via model merging: application to disordered speech

**Paper:** [Robust fine-tuning of speech recognition models via model merging: application to disordered speech](https://www.isca-archive.org/interspeech_2025/ducorroy25_interspeech.html)
**Taxonomy:** `recognition-and-alignment / context-and-open-vocabulary / speaker-adaptation`
**Evidence:** D3 full-paper capture; PDF SHA-256 `b63d8c0107dce983002da74b4858187b571e5050ed88c87f14bd85bdc73b5ae6`; full-text SHA-256 `a8ac83cf184c857a1bebad7213ece458e52413fe9e030df36732e7e06dc839a4`.

- **Ordinary problem:** A recognizer trained mostly on clear speech must map speech affected by motor disorders to words without confusing atypical pronunciation with noise.
- **Why it is hard:** Dysarthric speech varies across speakers and within one speaker, and the available training set is small; ordinary fine-tuning can overfit one trajectory and long utterances are especially difficult.
- **Naive attempt:** Fine-tune one model once and choose its last checkpoint, assuming the single optimization path has found the best adaptation.
- **Central move:** Average weights from multiple checkpoints or fine-tuning trajectories, and add a selective rule that keeps a candidate only when it reduces development-set WER.
- **Mechanism:** The study fine-tunes Whisper on the SAP dysarthric-speech data. MAST averages checkpoints along one trajectory, MAcT averages models from different hyperparameter trajectories, and SMAcT scans candidate models and retains those that improve the merged ensemble. The procedure is also tested with 1-hour, 10-hour, and full training subsets.
- **Mathematical idea:** For corresponding parameters, merging uses an arithmetic mean. SMAcT accepts model Mi when WER(E union Mi) is lower than the current WER. On the full set, fine-tuning gives WER 15.0, MAST 13.4, MAcT 13.9, and SMAcT 13.6; in the 1-hour setting SMAcT reduces WER from 21.2 to 19.0.
- **What the paper reports:** The paper reports gains for long utterances and low-data settings, including a 7.6% relative reduction from 18.5 to 17.1 WER with 10 hours of data; smaller Base and Turbo models improve too, but less consistently than Large.
- **Limits:** The SAP data, Whisper family, selected development subset, and merging order determine the result. The selective procedure uses WER on a development subset and may itself be selection-sensitive; no independent reproduction was performed.

## 325. BR-ASR: Efficient and Scalable Bias Retrieval Framework for Contextual Biasing ASR in Speech LLM

**Paper:** [BR-ASR: Efficient and Scalable Bias Retrieval Framework for Contextual Biasing ASR in Speech LLM](https://www.isca-archive.org/interspeech_2025/gong25_interspeech.html)
**Taxonomy:** `recognition-and-alignment / context-and-open-vocabulary / domain-and-context-biasing`
**Evidence:** D3 full-paper capture; PDF SHA-256 `79f03089472d0477711d847f58b09a3cc9620c562abf2d4b7d8e1639569854be`; full-text SHA-256 `55cdb68200039870711e5c2dc157ff884778210c0108833aa3f307f6cd95cb01`.

- **Ordinary problem:** An ASR system should recognize a rare name or domain word when the user supplies a large list of likely terms.
- **Why it is hard:** A list of 200,000 candidates can help one word but also create homophone confusion and unacceptable search cost.
- **Naive attempt:** Insert the entire bias list into decoding or fine-tune the recognizer for each new list.
- **Central move:** Retrieve a small relevant candidate set from speech and bias text, train against homophone confusion, and inject only the retrieved candidates without retraining the recognizer.
- **Mechanism:** Speech-and-bias contrastive learning ranks relevant entries; a dynamic curriculum trains the system on increasingly difficult homophones; pruning then supplies a compact list to the ASR decoder.
- **Mathematical idea:** Contrastive learning pulls matching speech/list pairs together and pushes distractors apart; retrieval converts a huge candidate set into a small conditional search problem.
- **What the paper reports:** The paper reports 2.8%/7.1% biased WER with 2,000 words, only 0.3/2.9% absolute degradation at 200,000 entries, 99.99% pruning, and 20 ms query latency on the tested split.
- **Limits:** The reported latency, languages, bias lists, and ASR systems define the boundary; rare names outside the retrieval distribution and interactive user correction remain open.

## 326. Theoretical proposal for a unified Bayesian model of adaptation in non-interactive and interactive speech production

**Paper:** [Theoretical proposal for a unified Bayesian model of adaptation in non-interactive and interactive speech production](https://www.isca-archive.org/interspeech_2025/guillaume25_interspeech.html)
**Taxonomy:** `recognition-and-alignment / context-and-open-vocabulary / speaker-adaptation`
**Evidence:** D3 full-paper capture; PDF SHA-256 `1cead1c8bb0b43eac1a1e3fc2bf51107634aa1192251a913e6347dedf8b4608b`; full-text SHA-256 `5bf68b5e119c95e85ea964834a51372c3f2ceb179ebf2f308e5ba0efe017e67c`.

- **Ordinary problem:** A speaker changes production when hearing altered feedback or interacting with another person, and one model should explain both adaptations.
- **Why it is hard:** Non-interactive feedback and interactive accommodation are often modeled separately even though both change the speaker-listener system.
- **Naive attempt:** Use unrelated models for altered-feedback production and conversational accommodation.
- **Central move:** Extend a unified Bayesian perception-production framework so adaptation is an inference problem over intended and heard speech.
- **Mechanism:** COSMO-style latent variables connect production and perception; Bayesian updating changes beliefs about the speech system under feedback or interaction.
- **Mathematical idea:** Adaptation is posterior inference under uncertain sensory evidence, not merely a speaker-specific parameter fine-tune.
- **What the paper reports:** The proposal shows how both experimental paradigms can be described within one Bayesian framework.
- **Limits:** This is a theoretical proposal, not an independent behavioral validation; parameterization, priors, and task fit remain open.

## 327. CMT-LLM: Contextual Multi-Talker ASR Utilizing Large Language Models

**Paper:** [CMT-LLM: Contextual Multi-Talker ASR Utilizing Large Language Models](https://www.isca-archive.org/interspeech_2025/he25_interspeech.html)
**Taxonomy:** `recognition-and-alignment / context-and-open-vocabulary / domain-and-context-biasing`
**Evidence:** D3 full-paper capture; PDF SHA-256 `ad5f1a7a62238c7951c28a472bf61be2c975daa7d28dacdcc8ee7e03549ddb09`; full-text SHA-256 `25390dba47b027ed32e2ed6dd0fe4f6cffde31f3c6f433937174b607e32f88d8`.

- **Ordinary problem:** In meetings, a recognizer must decide both who said what when voices overlap and which rare technical words are plausible in the current context.
- **Why it is hard:** A multi-talker transcript is not a single ordinary sentence, while a huge biasing list can distract decoding; treating overlap and rare-word biasing as separate repairs leaves their interaction unresolved.
- **Naive attempt:** Use serialized output training for overlap and add a generic bias list or shallow fusion after decoding.
- **Central move:** Make multi-talker transcription and contextual biasing one sequence-generation task: represent speakers in first-in-first-out order and filter the biasing list before placing relevant rare words into the language model prompt.
- **Mechanism:** A speech encoder produces frame representations, convolution downsamples them, a projector matches the LLM hidden size, and an LLM emits text separated by speaker-change tokens. A first decoding pass supplies evidence for a two-stage filter that selects rare words from a list of up to 1,000 before a second pass.
- **Mathematical idea:** The system minimizes token cross-entropy on serialized transcripts. WER is computed on LibriMix and AMI single-device microphone data under different bias-list sizes; the central decision is which context terms enter the decoder, not a new acoustic metric.
- **What the paper reports:** The paper reports WER of 7.9% on LibriMix and 32.9% on AMI SDM at biasing size 1,000, outperforming compared contextual-biasing approaches in its reported settings.
- **Limits:** FIFO serialization imposes an ordering convention; the bias list and first-pass filter supply information that may not exist in every deployment. WER does not separately reveal speaker attribution, rare-word recall, or hallucination cost, and results were not independently reproduced.

## 328. Dynamic Context-Aware Streaming Pretrained Language Model For Inverse Text Normalization

**Paper:** [Dynamic Context-Aware Streaming Pretrained Language Model For Inverse Text Normalization](https://www.isca-archive.org/interspeech_2025/ho25_interspeech.html)
**Taxonomy:** `recognition-and-alignment / context-and-open-vocabulary / long-context-decoding`
**Evidence:** D3 full-paper capture; PDF SHA-256 `8c15bc4084b595c726690bcf2a4fe9c0b1c2abaf0f0dafe3ecaf73f720f73fde`; full-text SHA-256 `a209b1c12d049997d53bd451be9f95b2797098b235beb1ea8d20fb12aceb2ac8`.

- **Ordinary problem:** Speech arrives incrementally, but written formatting often needs context that has not arrived yet.
- **Why it is hard:** Streaming ITN must balance incomplete context, accuracy, adaptation, and latency.
- **Naive attempt:** Run a full-context normalizer after the utterance is complete, or use fixed chunks that ignore right context.
- **Central move:** Use a pretrained language model with dynamic chunk sizes and controlled right-context during training and inference.
- **Mechanism:** The model changes its available context as speech arrives, using right-context information without abandoning the streaming budget.
- **Mathematical idea:** Sequence decoding maps spoken-form tokens to written-form tokens; latency and accuracy form the deployment tradeoff.
- **What the paper reports:** The paper reports accuracy comparable to non-streaming ITN and better than prior streaming models on Vietnamese data while maintaining low latency.
- **Limits:** Vietnamese data, benchmark, and author-reported latency/results limit cross-language and independent deployment claims.

## 329. Ranking and Selection of Bias Words for Contextual Bias Speech Recognition

**Paper:** [Ranking and Selection of Bias Words for Contextual Bias Speech Recognition](https://www.isca-archive.org/interspeech_2025/hou25_interspeech.html)
**Taxonomy:** `recognition-and-alignment / context-and-open-vocabulary / domain-and-context-biasing`
**Evidence:** D3 full-paper capture; PDF SHA-256 `01639f2a96ebc2d528d87c274db8f2a381d31a72af55afea82a3cb507371dbb4`; full-text SHA-256 `94394888146e5e8940d4400b038dd92c03fb996b3aa3e2d898bef7ccfa2c460e`.

- **Ordinary problem:** Contextual ASR should recognize a large list of names or domain words without being distracted by irrelevant entries.
- **Why it is hard:** A large bias list creates search competition and homophone errors, so adding every candidate can hurt the very words it is meant to help.
- **Naive attempt:** Pass the full list to decoding or choose entries by frequency alone.
- **Central move:** Train a scorer that ranks and selects bias words from an NER-derived list before contextual Whisper decoding.
- **Mechanism:** A bias-word ranking network selects candidates from the IS21 list and evaluates contextual Whisper on LibriSpeech.
- **Mathematical idea:** Selection turns a huge candidate set into a focused conditional recognition problem; biased WER measures the targeted words while overall WER checks collateral damage.
- **What the paper reports:** The paper reports more than 40% relative reduction in biased WER from ranking and selection.
- **Limits:** NER list, LibriSpeech, Whisper context mechanism, and bias-word definition bound the result; new domains and errors in entity extraction remain open.

## 330. Adversarial Deep Metric Learning for Cross-Modal Audio-Text Alignment in Open-Vocabulary Keyword Spotting

**Paper:** [Adversarial Deep Metric Learning for Cross-Modal Audio-Text Alignment in Open-Vocabulary Keyword Spotting](https://www.isca-archive.org/interspeech_2025/jung25b_interspeech.html)
**Taxonomy:** `recognition-and-alignment / context-and-open-vocabulary / open-vocabulary-recognition`
**Evidence:** D3 full-paper capture; PDF SHA-256 `077989cefc8d919100aaa3e6534b475123c639c9f6647b28f5378f0be5917641`; full-text SHA-256 `d75750b3f6a2c0428066b66fd625cdc9ddd42b704c202778f069f5f8bd58b7df`.

- **Ordinary problem:** Text-enrolled keyword spotting should recognize a word not seen as a fixed acoustic class by aligning an utterance with its text description.
- **Why it is hard:** Audio and text embeddings have different modality statistics; a shared space can match superficial modality cues instead of phonetic or lexical content.
- **Naive attempt:** Compare audio and text embeddings directly with ordinary metric learning and assume the modality gap disappears with more data.
- **Central move:** Adversarially train a modality classifier so audio and text encoders produce modality-invariant embeddings, then optimize deep metric alignment for open-vocabulary KWS.
- **Mechanism:** The encoders map acoustic queries and text enrollments into a shared space; the adversarial classifier penalizes recoverable modality identity while the metric objective pulls matched keyword pairs together.
- **Mathematical idea:** The shared embedding is a constrained retrieval geometry: matched audio/text pairs should be close, while modality identity should be uninformative to the adversary.
- **What the paper reports:** Modality-invariant alignment improves the audio-text retrieval decision used for unseen-keyword spotting in the reported experiments.
- **Limits:** Vocabulary, languages, negative sampling, enrollment text, threshold calibration, and speaker/channel variation bound the claim; open-vocabulary benchmark accuracy is not unrestricted lexical understanding.

## 331. MOVER: Combining Multiple Meeting Recognition Systems

**Paper:** [MOVER: Combining Multiple Meeting Recognition Systems](https://www.isca-archive.org/interspeech_2025/kamo25_interspeech.html)
**Taxonomy:** `recognition-and-alignment / context-and-open-vocabulary / long-context-decoding`
**Evidence:** D3 full-paper capture; PDF SHA-256 `1726cf89cb5d6e04bc26e56cd282452aa72884a1a2be8324b022f9c6ece8d988`; full-text SHA-256 `01beeb5bc32a5e4420d9b66315f504964c9a0d6d25228464af9a0684b3baf496`.

- **Ordinary problem:** A meeting recognizer should combine systems that disagree about speaker segments, timing, and words without throwing away either signal.
- **Why it is hard:** DOVER/ROVER-style systems typically combine one output type, while meeting hypotheses disagree in both diarization and ASR boundaries.
- **Naive attempt:** Vote words independently or concatenate the best diarization and best transcript as if their time intervals matched.
- **Central move:** Use MOVER’s staged alignment, segment grouping, word/timing combination, and speaker reconciliation across complete meeting hypotheses.
- **Mechanism:** The method constructs correspondences between speaker-labeled time intervals before combining words and timings, preserving the meeting structure.
- **Mathematical idea:** Combination is a structured matching problem over intervals, labels, and sequences rather than token-majority voting alone.
- **What the paper reports:** MOVER reports successful combination on CHiME-8 DASR and NOTSOFAR-1 multi-channel tasks.
- **Limits:** Task formats, diarization errors, interval alignment, system diversity, and scoring rules bound transfer; fusion gains do not prove every component is complementary.

## 332. Fully End-to-end Streaming Open-vocabulary Keyword Spotting with W-CTC Forced Alignment

**Paper:** [Fully End-to-end Streaming Open-vocabulary Keyword Spotting with W-CTC Forced Alignment](https://www.isca-archive.org/interspeech_2025/kim25d_interspeech.html)
**Taxonomy:** `recognition-and-alignment / context-and-open-vocabulary / open-vocabulary-recognition`
**Evidence:** D3 full-paper capture; PDF SHA-256 `d066ed299af2a95f276648caafaf13903da3a81a4c8849d6c24f0ae42ae88535`; full-text SHA-256 `6bb66d739549b75bf0ebe223b8ef2af7714f23d80c83b6a711d506382ac3bd57`.

- **Ordinary problem:** Open-vocabulary keyword spotting must find arbitrary words without preparing word-aligned training data for every target.
- **Why it is hard:** Forced alignment is costly, while streaming recognition cannot wait for a separately aligned corpus.
- **Naive attempt:** Build a fixed-vocabulary detector or use an external forced aligner and precomputed word segments.
- **Central move:** Integrate W-CTC forced alignment into a fully end-to-end streaming system.
- **Mechanism:** CTC paths supply word-span alignment while the text encoder and verifier are trained in the same pipeline.
- **Mathematical idea:** CTC alignment links acoustic frames to text; keyword audio-text similarity then scores arbitrary words.
- **What the paper reports:** The paper reports superior performance on the Libriphrase hard set.
- **Limits:** Benchmark, language, and author-reported result limit generalization and independent reproducibility.

## 333. GLCLAP: A Novel Contrastive Learning Pre-trained Model for Contextual Biasing in ASR

**Paper:** [GLCLAP: A Novel Contrastive Learning Pre-trained Model for Contextual Biasing in ASR](https://www.isca-archive.org/interspeech_2025/kong25_interspeech.html)
**Taxonomy:** `recognition-and-alignment / context-and-open-vocabulary / domain-and-context-biasing`
**Evidence:** D3 full-paper capture; PDF SHA-256 `f04f4fdb18d044ac8fcce09d6fc6e94a0a9e926cea8b280a91c16a70914384de`; full-text SHA-256 `e48e3a842ae8a40a18a00129d7bf3b84cf331fb762fc62476bb04f05b65c9a48`.

- **Ordinary problem:** A recognizer may need to favor a user's rare names or entities, but it must retrieve the right items from a list rather than biasing toward every vaguely similar word.
- **Why it is hard:** The prompt list can be long and the audio contains both sentence-level meaning and local word evidence; a sentence-only audio-text match may miss the precise entity.
- **Naive attempt:** Give all listed words a fixed decoding bonus or retrieve candidates using only a global sentence embedding.
- **Central move:** Train a contrastive audio-text retriever at both global sentence and local word scales, then use the retrieved bias words during ASR decoding.
- **Mechanism:** GLCLAP learns global and local audio-text relations for contextual biasing, retrieving matched entities from a user-specified list before the ASR decoder uses them.
- **Mathematical idea:** Contrastive learning makes matched audio/text pairs close and mismatched pairs distant; global context narrows meaning while local segments identify the exact rare word, and retrieval accuracy precedes WER.
- **What the paper reports:** The paper reports a marked improvement in bias-word retrieval accuracy and downstream contextual ASR performance over sentence-level contrastive approaches.
- **Limits:** Entity list, prompt quality, language, negative sampling, retrieval threshold, and ASR decoder bound the result; a better retrieved list cannot correct an incorrect user prompt or guarantee unbiased ordinary decoding.

## 334. Improving Synthetic Data Training for Contextual Biasing Models with a Keyword-Aware Cost Function

**Paper:** [Improving Synthetic Data Training for Contextual Biasing Models with a Keyword-Aware Cost Function](https://www.isca-archive.org/interspeech_2025/kwok25b_interspeech.html)
**Taxonomy:** `recognition-and-alignment / context-and-open-vocabulary / domain-and-context-biasing`
**Evidence:** D3 full-paper capture; PDF SHA-256 `ba6b380f1b48c191973921bf7287c183ca99f2ba0a052d3d0fb4fc6e8e04e34f`; full-text SHA-256 `e9eef15019073a075f34380eeafd9d63d09c1b2970adbfadf684acac8d58a075`.

- **Ordinary problem:** Contextual biasing should help a recognizer spell a user's rare keyword, but it should not turn every acoustically similar word into that keyword.
- **Why it is hard:** Synthetic training examples can be plentiful yet unrealistic; a fixed cost for all keywords ignores how often each keyword is confused and how context changes the error.
- **Naive attempt:** Add a uniform decoding bonus or generate random keyword examples without modeling which confusions matter.
- **Central move:** Use a keyword-aware cost function when training synthetic contextual-biasing data so difficult and useful examples receive the right pressure.
- **Mechanism:** The paper improves synthetic-data training for contextual biasing with a keyword-aware cost function.
- **Mathematical idea:** The training objective changes the data's influence according to the keyword-level error structure; the goal is targeted correction rather than blanket bias.
- **What the paper reports:** The paper reports improved contextual-biasing performance for the proposed synthetic-data objective.
- **Limits:** Keyword lists, synthetic-data quality, language, decoder, and evaluation distribution limit generalization; better keyword recall can still create false activations.

## 335. Efficient Trie-based Biasing using K-step Prediction for Rare Word Recognition

**Paper:** [Efficient Trie-based Biasing using K-step Prediction for Rare Word Recognition](https://www.isca-archive.org/interspeech_2025/kwok25c_interspeech.html)
**Taxonomy:** `recognition-and-alignment / context-and-open-vocabulary / open-vocabulary-recognition`
**Evidence:** D3 full-paper capture; PDF SHA-256 `2f8391afc228366b62b77b34a680974c05a39271013f4b1e93ccb7cfe98a64d7`; full-text SHA-256 `61d119a99aa575b0c9c5faab6aaf00efa2b0049baf36d9d580030d9b903aa876`.

- **Ordinary problem:** Rare names and terms should be recognized when they are not common in the vocabulary.
- **Why it is hard:** Trie biasing rewards a partial word before knowing whether the full word completes, then revokes rewards during beam search.
- **Naive attempt:** Add a fixed bonus to every matching prefix and pay the cost of undoing it when the hypothesis fails.
- **Central move:** Train a K-step predictor to look ahead and estimate whether a rare word will complete, avoiding score revocation.
- **Mechanism:** The decoder predicts future steps from a prefix; synthetic data fine-tunes Whisper so contextual biasing becomes learned look-ahead.
- **Mathematical idea:** The method replaces delayed correction with an approximate future-value estimate, trading learned prediction for simpler decoding.
- **What the paper reports:** On NSC Part 2, reported WER falls from 30.86% to 12.19% after 10 hours of synthetic-data fine-tuning.
- **Limits:** Synthetic realism, rare-word list, decoder, beam settings, and WER denominator bound the claim.

## 336. WCTC-Biasing: Retraining-free Contextual Biasing ASR with Wildcard CTC-based Keyword Spotting and Inter-layer Biasing

**Paper:** [WCTC-Biasing: Retraining-free Contextual Biasing ASR with Wildcard CTC-based Keyword Spotting and Inter-layer Biasing](https://www.isca-archive.org/interspeech_2025/nakagome25_interspeech.html)
**Taxonomy:** `recognition-and-alignment / context-and-open-vocabulary / domain-and-context-biasing`
**Evidence:** D3 full-paper capture; PDF SHA-256 `7a6e4263a62e3c48b1f14b3f722453c1337e39ba2839ab5a56d17e8317b057c3`; full-text SHA-256 `44144178e6b4c0c2bd7afa3dfbeb9e532e93d3e86ec52b4c90c6d3b6ae714983`.

- **Ordinary problem:** ASR should recognize rare contextual keywords without retraining whenever application vocabulary changes.
- **Why it is hard:** A fixed bias list can over-bias decoding, while conventional contextual biasing may miss keywords with variable or wildcard forms.
- **Naive attempt:** Retrain the recognizer for every keyword list or inject a static phrase list and accept false substitutions.
- **Central move:** Use wildcard CTC keyword spotting and inter-layer biasing to add contextual evidence at inference time without retraining.
- **Mechanism:** CTC keyword scores detect flexible keyword evidence; inter-layer bias signals steer decoding while retaining the base acoustic model.
- **Mathematical idea:** Contextual biasing changes the prior over candidate words, so it must raise relevant rare words without overruling acoustic evidence.
- **What the paper reports:** The paper reports retraining-free contextual recognition improvements using WCTC-Biasing.
- **Limits:** Keyword lists, wildcard design, domains, decoder thresholds, and test distributions bound transfer; contextual gains do not guarantee lower errors on arbitrary speech.

## 337. Improving Cross-Attention based on Positional Alignment during Inference for Robust Long-form Speech Recognition

**Paper:** [Improving Cross-Attention based on Positional Alignment during Inference for Robust Long-form Speech Recognition](https://www.isca-archive.org/interspeech_2025/oh25c_interspeech.html)
**Taxonomy:** `recognition-and-alignment / context-and-open-vocabulary / long-context-decoding`
**Evidence:** D3 full-paper capture; PDF SHA-256 `8fd6e5266bcd9f9a54cd22e8b42afdc5202097e4d4638bd194ffe49eeaf8cc98`; full-text SHA-256 `4040afbbf056aca79f2e7716b93cd1f9d344b79b0baa9d509ec3420f9b21066f`.

- **Ordinary problem:** Long-form ASR should use positional context without losing local acoustic alignment.
- **Why it is hard:** Cross-attention can attend to misplaced encoder positions, especially as utterances grow, causing errors that a generic language prior cannot diagnose.
- **Naive attempt:** Use unmodified cross-attention or force a hard monotonic alignment that cannot accommodate timing variation.
- **Central move:** Add positional alignment to cross-attention at inference so attention scores favor acoustically corresponding positions during long-form decoding.
- **Mechanism:** Position-aware attention reshapes the correspondence between decoder states and encoder frames without changing the recognized content target.
- **Mathematical idea:** Long-context decoding is a soft alignment problem: context helps only when its evidence remains tied to the relevant time region.
- **What the paper reports:** The paper reports improved robust long-form recognition from inference-time positional alignment.
- **Limits:** Model, long-form segmentation, positional formulation, decoding settings, and evaluation corpora bound transfer; reported robustness is not universal streaming reliability.

## 338. Multilingual Query-by-Example KWS for Indian Languages using Transliteration

**Paper:** [Multilingual Query-by-Example KWS for Indian Languages using Transliteration](https://www.isca-archive.org/interspeech_2025/r25_interspeech.html)
**Taxonomy:** `recognition-and-alignment / context-and-open-vocabulary / open-vocabulary-recognition`
**Evidence:** D3 full-paper capture; PDF SHA-256 `42b906dca87a28c6a7311206856aec2a22a21bd381c817c85285b3477b2f2a7f`; full-text SHA-256 `b3e9411662061185872e08c44c3be309113d72ad9242375930c0e7111db24c14`.

- **Ordinary problem:** Query-by-example search should find a spoken term across Indian languages without one language-specific phoneme inventory.
- **Why it is hard:** Phoneme symbols and pronunciation conventions differ, while query and target need comparable representations.
- **Naive attempt:** Use one shared phoneme dictionary and assume posteriors mean the same thing across languages.
- **Central move:** Use multilingual ASR character logits in a shared Devanagari transliteration space for query and target audio.
- **Mechanism:** The ASR maps ten languages to transliterated characters; posterior sequences become retrieval features.
- **Mathematical idea:** Transliteration changes the shared unit from language-specific phonemes to a common script-level sequence representation.
- **What the paper reports:** The method raises reported MTWV from 0.015 to 0.504 on IndicSUPERB and exceeds the Marathi baseline.
- **Limits:** Language, script, ASR errors, query duration, and splits constrain transfer; script unification is not translation.

## 339. Effects of Speaker Count, Duration, and Accent Diversity on Zero-Shot Accent Robustness in Low-Resource ASR

**Paper:** [Effects of Speaker Count, Duration, and Accent Diversity on Zero-Shot Accent Robustness in Low-Resource ASR](https://www.isca-archive.org/interspeech_2025/yong25_interspeech.html)
**Taxonomy:** `recognition-and-alignment / context-and-open-vocabulary / speaker-adaptation`
**Evidence:** D3 full-paper capture; PDF SHA-256 `6bbdf407c9f054962be570e20a7ff1c7c7916a082c378962b2dafe1c6c0cf224`; full-text SHA-256 `eacaab344934b78cd2f1efe25e48f1f05222cbba08476dabbff32a69a234412c`.

- **Ordinary problem:** Low-resource ASR should generalize to accents not represented in training data.
- **Why it is hard:** Speaker count, hours per speaker, and accent diversity are confounded when the total training budget is fixed.
- **Naive attempt:** Add hours from a few speakers and assume more accent labels alone will guarantee unseen-accent robustness.
- **Central move:** Factor the training-data budget by speaker count, per-speaker duration, and accent diversity, then test zero-shot accents.
- **Mechanism:** Controlled data-composition experiments compare ASR performance across unseen accents and languages.
- **Mathematical idea:** Generalization is constrained by which speakers and accents supply the training evidence, not only by total audio hours.
- **What the paper reports:** The paper reports that more speakers help more than more hours per speaker, while accent-diversity gains are minimal under controlled speaker count.
- **Limits:** Languages, accent labels, low-resource budgets, model/training choices, and zero-shot evaluation bound transfer; this is not a universal data-collection law.

## 340. Mixture of LoRA Experts for Low-Resourced Multi-Accent Automatic Speech Recognition

**Paper:** [Mixture of LoRA Experts for Low-Resourced Multi-Accent Automatic Speech Recognition](https://www.isca-archive.org/interspeech_2025/bagat25_interspeech.html)
**Taxonomy:** `recognition-and-alignment / pronunciation-and-variation / pronunciation-variation`
**Evidence:** D3 full-paper capture; PDF SHA-256 `24d67d7a94e85d772f56d24def610a3175a38f8f97b105ca6235630b5705ba2c`; full-text SHA-256 `412e8e89fb8daf9fb0243646ee12d2e2d94aaaa2d62a77a33b6a1508c5050248`.

- **Ordinary problem:** An ASR model should recognize non-native speech across several accents even when each accent has little labeled data and the accent is unknown at test time.
- **Why it is hard:** Accent changes sound patterns in different ways, and adapting to one accent can erase performance on others.
- **Naive attempt:** Fine-tune one shared model or train a separate full model for every accent.
- **Central move:** Keep several small accent-specific adapters and let the system combine them, with or without knowing the accent.
- **Mechanism:** MAS-LoRA attaches low-rank adapters specialized to accents to Whisper and evaluates known- and unknown-accent routing on L2-ARCTIC.
- **Mathematical idea:** Word error rate measures recognition; comparisons include ordinary LoRA, full fine-tuning, and forgetting after adaptation.
- **What the paper reports:** The paper reports lower WER than those baselines, stronger gains when the accent is known, and less catastrophic forgetting.
- **Limits:** The result is tied to L2-ARCTIC, its accent set, Whisper, and routing assumptions; spontaneous speech and accents outside the corpus remain open.

## 341. CHSER: A Dataset and Case Study on Generative Speech Error Correction for Child ASR

**Paper:** [CHSER: A Dataset and Case Study on Generative Speech Error Correction for Child ASR](https://www.isca-archive.org/interspeech_2025/balajishankar25_interspeech.html)
**Taxonomy:** `recognition-and-alignment / pronunciation-and-variation / pronunciation-variation`
**Evidence:** D3 full-paper capture; PDF SHA-256 `90415e1d635fa623cb761604c0e889418daf65548791bc62e0c74c79220af0bb`; full-text SHA-256 `ea0ec4df48fae32c35e74c254d41b1b7ee54d911444724b8d0ed6f2d0d73cf42`.

- **Ordinary problem:** Child ASR needs a correction stage that fixes transcription errors without turning child-specific disfluencies into fluent but wrong text.
- **Why it is hard:** Child speech has unusual acoustics and language patterns, and child error-correction data are scarce.
- **Naive attempt:** Apply adult speech error correction directly to child hypotheses.
- **Central move:** Create a large hypothesis-to-reference dataset for children and learn a generative correction model whose errors can be inspected by type.
- **Mechanism:** CHSER contains 200K pairs across ages and speaking styles; fine-tuned generative correction is tested in zero-shot and ASR-fine-tuned settings.
- **Mathematical idea:** Word error rate measures overall correction, while substitution, deletion, insertion, and disfluency analysis show which errors are changed.
- **What the paper reports:** The paper reports up to 28.5% relative WER reduction zero-shot and 13.3% after ASR fine-tuning, but insertions and child disfluencies remain difficult.
- **Limits:** The corpus, languages, ASR hypotheses, and correction model bound the result; preserving clinically meaningful disfluencies outside these settings remains open.

## 342. SardinianVoxes: A Speech Recognition Dataset for the Sardinian Languages

**Paper:** [SardinianVoxes: A Speech Recognition Dataset for the Sardinian Languages](https://www.isca-archive.org/interspeech_2025/carta25_interspeech.html)
**Taxonomy:** `recognition-and-alignment / pronunciation-and-variation / pronunciation-variation`
**Evidence:** D3 full-paper capture; PDF SHA-256 `0075474f4f9fe71d6555318c92939252adab0b87b46b93b1a4f56ccdc1056a2e`; full-text SHA-256 `8f996f4804d76739e3311acf4f93a9672044419b7848bfd3172d9d29506fe7dd`.

- **Ordinary problem:** A speech recognizer should serve Sardinian varieties despite fragmented data and internal linguistic diversity.
- **Why it is hard:** Low-resource languages lack enough transcribed, balanced, and variety-labeled speech for ordinary training recipes.
- **Naive attempt:** Pool whatever recordings exist and report one aggregate score that hides variety differences.
- **Central move:** Build a reproducible audio-text corpus with explicit variety annotation and evaluate both pretrained and fine-tuned recognizers across varieties.
- **Mechanism:** SardinianVoxes contains about 170 hours of transcribed speech, and the paper defines a benchmark for state-of-the-art and fine-tuned speech-to-text models.
- **Mathematical idea:** A corpus is a measurement object: coverage, transcription, variety labels, and split design determine what an error rate means.
- **What the paper reports:** The paper contributes a public resource and evaluation protocol intended to make Sardinian speech technology measurable.
- **Limits:** The reported resource, varieties, transcription quality, and benchmark models bound the claim; future collection and independent use are still needed.

## 343. Using Neurogram Similarity Index Measure (NSIM) to Model Hearing Loss and Cochlear Neural Degeneration

**Paper:** [Using Neurogram Similarity Index Measure (NSIM) to Model Hearing Loss and Cochlear Neural Degeneration](https://www.isca-archive.org/interspeech_2025/cheema25_interspeech.html)
**Taxonomy:** `recognition-and-alignment / pronunciation-and-variation / pronunciation-variation`
**Evidence:** D3 full-paper capture; PDF SHA-256 `0f777d89994a53c729b7e7e79b543bf5daf757ea813869574db55d1f89fa787c`; full-text SHA-256 `635dcaac4b1bfef60856b7154dd32b81f04c108ff28fb3f712887b8ce3c574bb`.

- **Ordinary problem:** People can struggle to understand speech in noise even when a routine hearing test does not fully explain the difficulty.
- **Why it is hard:** Damage to auditory-nerve connections may alter the neural representation of sound without appearing as ordinary threshold loss; a useful marker must connect a simulated neural response to behavior.
- **Naive attempt:** Use only an audiogram or infer all noisy-speech difficulty from the loudness threshold.
- **Central move:** Compare modeled auditory-nerve neurograms with a Neurogram Similarity Index and relate the measure to phoneme recognition and simulated cochlear neural degeneration.
- **Mechanism:** The paper evaluates NSIM as an objective measure of hearing loss and cochlear neural degeneration.
- **Mathematical idea:** Hearing ability is a transformation from sound to neural patterns: comparing those patterns can expose losses that a simple input threshold misses, but the model remains an indirect proxy.
- **What the paper reports:** The paper reports that NSIM maps phoneme-recognition performance and is sensitive to simulated degeneration, suggesting a candidate noninvasive biomarker.
- **Limits:** Auditory-periphery model, task, simulations, participant data, and mapping assumptions bound clinical interpretation; a candidate biomarker is not a validated diagnosis.

## 344. Improving Child Speech Recognition and Reading Mistake Detection by Using Prompts

**Paper:** [Improving Child Speech Recognition and Reading Mistake Detection by Using Prompts](https://www.isca-archive.org/interspeech_2025/gao25c_interspeech.html)
**Taxonomy:** `recognition-and-alignment / pronunciation-and-variation / pronunciation-variation`
**Evidence:** D3 full-paper capture; PDF SHA-256 `0993342227593646355656df40fc35a664daeb184c7daff1bf5929c7c41e76d5`; full-text SHA-256 `58f3cae31fe2355c8d8af873fc71c88d62cbaad910ca82fe7e56004104c6abc0`.

- **Ordinary problem:** Child speech recognition and reading-mistake detection should connect variable child acoustics to intended linguistic units and learning outcomes.
- **Why it is hard:** Children differ in articulation, age, reading skill, and pronunciation, so adult-trained acoustic boundaries are unreliable.
- **Naive attempt:** Apply an adult ASR model and treat every mismatch as an ordinary recognition error.
- **Central move:** Use prompts to condition recognition and mistake detection on the child's intended reading task.
- **Mechanism:** Prompt information narrows the hypothesis space: acoustic evidence is interpreted with task and expected linguistic content.
- **Mathematical idea:** The paper treats pronunciation-variation as a structured evidence-to-decision problem: Prompt information narrows the hypothesis space: acoustic evidence is interpreted with task and expected linguistic content.
- **What the paper reports:** The paper reports improving child speech recognition and reading-mistake detection using prompts.
- **Limits:** Child age, language, prompt design, annotation policy, and error definitions bound transfer.

## 345. Reconstruction of the Complete Vocal Tract Contour Through Acoustic to Articulatory Inversion Using Real-Time MRI Data

**Paper:** [Reconstruction of the Complete Vocal Tract Contour Through Acoustic to Articulatory Inversion Using Real-Time MRI Data](https://www.isca-archive.org/interspeech_2025/azzouz25_interspeech.html)
**Taxonomy:** `sound-and-production / articulatory-dynamics / articulatory-coordination`
**Evidence:** D3 full-paper capture; PDF SHA-256 `a96e9463c75424f8f86fcd9e2fa2b202474fe14000aadc19d11ac7a939a16571`; full-text SHA-256 `1940aa0a587e43348c54748fb6563b9931a6054c6bedfcc05d8577e22ded5602`.

- **Ordinary problem:** We want to infer how the entire vocal tract moves from sound, including hidden parts such as the velum and glottis.
- **Why it is hard:** Acoustics are an indirect and many-to-one view of articulation; different configurations can produce similar sound, and real-time MRI labels are expensive.
- **Naive attempt:** Infer only easily sensed articulators or use a small sensor-based corpus and extrapolate to the full tract.
- **Central move:** Train acoustic-to-articulatory models against complete vocal-tract contours from real-time MRI and compare individual and joint articulator prediction.
- **Mechanism:** The paper reconstructs the complete vocal-tract contour from acoustic input using real-time MRI data and bidirectional recurrent models.
- **Mathematical idea:** The problem is inverse measurement: the model estimates hidden physical configuration from its acoustic consequence, so pixel-scale error and anatomical coverage matter as much as waveform fit.
- **What the paper reports:** The paper reports average contour RMSE near the MRI pixel size on its test set.
- **Limits:** Speakers, MRI protocol, segmentation, speech styles, and model assumptions limit generalization; contour accuracy is not a complete articulatory theory.

## 346. Enhancing Acoustic-to-Articulatory Inversion with Multi-Target Pretraining for Low-Resource Settings

**Paper:** [Enhancing Acoustic-to-Articulatory Inversion with Multi-Target Pretraining for Low-Resource Settings](https://www.isca-archive.org/interspeech_2025/bandekar25_interspeech.html)
**Taxonomy:** `sound-and-production / articulatory-dynamics / articulatory-coordination`
**Evidence:** D3 full-paper capture; PDF SHA-256 `c6b6e7668fdd2240d3906c356a569025a1d0560df9a4171eb942c52e260a578d`; full-text SHA-256 `78fd85f6bcd50e3de4debdf05f504e44eef38a62e314dde4e997656923809f3e`.

- **Ordinary problem:** Acoustic-to-articulatory inversion tries to infer moving vocal-tract positions from sound, which can make speech production measurable for recognition, synthesis, and pronunciation work.
- **Why it is hard:** Articulatory data are scarce, unseen speakers differ, and a large self-supervised feature extractor can improve accuracy while making real-time use expensive.
- **Naive attempt:** Attach a large pretrained feature extractor at inference time or train the inversion model only on the limited paired articulatory data.
- **Central move:** Pretrain the inversion model against three related targets—phoneme labels, articulatory features, and critical articulator labels—so it receives useful structure without carrying the external extractor at deployment.
- **Mechanism:** The model maps acoustic features to articulatory trajectories. During pretraining it predicts phonemic, broad articulatory, and critical-articulator targets; it is then fine-tuned with different amounts of paired data and compared with a baseline and SSL-feature systems on seen and unseen speakers.
- **Mathematical idea:** The main measures are correlation coefficient between predicted and reference trajectories and root-mean-square error. Multi-target pretraining adds supervised prediction tasks; the reported efficiency claim concerns removing the external SSL extractor, not eliminating all computation.
- **What the paper reports:** The paper reports consistent AAI improvement, including low-resource gains; the strongest reported unseen-speaker configuration reaches CC 0.8612 and RMSE 1.1023, while inference avoids the external SSL extractor.
- **Limits:** The articulatory targets, speakers, language, and feature choices define the tested boundary; predicted movement is not equivalent to direct imaging. Reported gains and speed claims are author-reported and were not independently reproduced.

## 347. Articulatory modeling of the S-shaped F2 trajectories observed in Öhman's spectrographic analysis of VCV syllables

**Paper:** [Articulatory modeling of the S-shaped F2 trajectories observed in Öhman's spectrographic analysis of VCV syllables](https://www.isca-archive.org/interspeech_2025/berthommier25_interspeech.html)
**Taxonomy:** `sound-and-production / articulatory-dynamics / articulatory-coordination`
**Evidence:** D3 full-paper capture; PDF SHA-256 `036c4dfde7eb6ac0796fa87e90fbd8153f2d92b6608a48dcb1dbf4f819698db6`; full-text SHA-256 `241caa2168261dc952d22e051f1581e3db9459f33bb366c09d1cf3c062cf761b`.

- **Ordinary problem:** Explain why the second formant bends in an S shape while a speaker moves through vowel-consonant-vowel syllables.
- **Why it is hard:** The acoustic trajectory reflects several moving articulators and planning regimes; a purely acoustic curve does not say which physical movement caused it.
- **Naive attempt:** Fit a curve to the spectrogram and treat the curve as a direct articulatory law.
- **Central move:** Generate the same VCV sequences with an articulatory model, separate vowel transitions from consonant influence, and compare the resulting trajectories and locus equations.
- **Mechanism:** The study uses the Maeda articulatory model to reproduce Öhman's S-shaped F2 trajectories and reassesses conventional locus-equation interpretations.
- **Mathematical idea:** The acoustic pattern is an effect of coordinated movement: a model can test whether the pattern follows from planning constraints rather than treating it as an unexplained spectral shape.
- **What the paper reports:** The paper reports synthetic trajectories resembling the observed sequences and structured effects of articulatory planning.
- **Limits:** Model geometry, trajectory planning, corpus, and synthetic-to-observed comparison limit claims; matching a trajectory does not identify a unique human motor plan.

## 348. Speech Reduction in French: The Relationship Between Vowel Space and Articulation Dynamics

**Paper:** [Speech Reduction in French: The Relationship Between Vowel Space and Articulation Dynamics](https://www.isca-archive.org/interspeech_2025/bodur25_interspeech.html)
**Taxonomy:** `sound-and-production / articulatory-dynamics / articulatory-coordination`
**Evidence:** D3 full-paper capture; PDF SHA-256 `a1acaa7ac82fd11ba2f0fa8e61e5cc297585c16d7d72517f359701d2a4dd62a1`; full-text SHA-256 `bf85c418fab2264cbd77e7eb100890dec6a318edcffa88fe4f14cb57959189c2`.

- **Ordinary problem:** Spontaneous speech becomes shorter and less distinct when people speak quickly, so a system or scientist must connect timing to the shape of the vowel space.
- **Why it is hard:** Reduction is not one event: speakers can centralize vowels, compress time, or do both, and a global measure may hide that interaction.
- **Naive attempt:** Use articulation rate or vowel-space size alone as a complete explanation.
- **Central move:** Model spatial vowel distinctiveness and temporal rate together and test whether their interaction predicts non-lexicalized reductions.
- **Mechanism:** French spontaneous speech is measured with pVSA, VDI, articulation rate, and temporally compressed speech zones.
- **Mathematical idea:** Regression separates spatial predictors, temporal predictors, and their interaction rather than treating one acoustic number as the cause.
- **What the paper reports:** Smaller vowel space predicts more reduction only when articulation rate is included; rate is the strongest predictor and VDI is not significant.
- **Limits:** The French speakers, spontaneous tasks, reduction definition, and acoustic measures bound the result; other languages and conversational settings remain open.

## 349. PERCEPT-US: A Multimodal American English Child Speech Corpus Specialized for Articulatory Feedback

**Paper:** [PERCEPT-US: A Multimodal American English Child Speech Corpus Specialized for Articulatory Feedback](https://www.isca-archive.org/interspeech_2025/eads25_interspeech.html)
**Taxonomy:** `sound-and-production / articulatory-dynamics / articulatory-coordination`
**Evidence:** D3 full-paper capture; PDF SHA-256 `d39a7dfdfb91d7ff5da63f23efef82e847b007fe0f44b266ca08e8eb9455f981`; full-text SHA-256 `f277c908c40ab44758effe4a88f95212f4c450674e2bdb43c86852166bcafc36`.

- **Ordinary problem:** A child learning to change articulation needs feedback that connects what they feel and see with how their speech sounds.
- **Why it is hard:** Articulation is hidden, children vary in development, and feedback must align audio, visual movement, and a usable teaching target without overwhelming the learner.
- **Naive attempt:** Show a waveform or give a generic pronunciation score and assume it identifies the movement to change.
- **Central move:** Build a multimodal American English child-speech corpus specialized for articulatory feedback, with synchronized speech and articulatory information.
- **Mechanism:** PERCEPT-US provides a multimodal child speech corpus designed for articulatory feedback.
- **Mathematical idea:** The corpus makes a hidden motor target observable: acoustic output can be related to articulator configuration and learner-facing feedback rather than treated as an isolated sound label.
- **What the paper reports:** The paper reports corpus resources and articulatory-feedback-oriented evaluation for American English child speech.
- **Limits:** Speakers, ages, tasks, sensor alignment, labels, and corpus size limit generalization; a resource does not itself establish learning or clinical benefit.

## 350. Creaky Voice Facilitates More Efficient Phonological Processing of Mandarin Tone 3

**Paper:** [Creaky Voice Facilitates More Efficient Phonological Processing of Mandarin Tone 3](https://www.isca-archive.org/interspeech_2025/fan25b_interspeech.html)
**Taxonomy:** `sound-and-production / articulatory-dynamics / articulatory-coordination`
**Evidence:** D3 full-paper capture; PDF SHA-256 `66fe70b6b48b5aa26b36ad43d8865b2571130b519a3f357cd3eb61e62260eb6a`; full-text SHA-256 `dc690344cd89e9f54d5e555c59870ad8e1efc245c119a167c7477e7cb1d174ec`.

- **Ordinary problem:** A listener must recognize Mandarin Tone 3 efficiently even when the voice has a creaky quality that changes the acoustic signal.
- **Why it is hard:** Tone, voice quality, and phonological context interact; a cue can make processing easier without being the tone itself.
- **Naive attempt:** Use pitch alone or treat creak as irrelevant speaker variation.
- **Central move:** Test whether creaky voice changes the time and accuracy of Tone 3 processing, separating phonological benefit from general listening difficulty.
- **Mechanism:** The paper studies how creaky voice facilitates more efficient phonological processing of Mandarin Tone 3.
- **Mathematical idea:** The speech cue is useful because it changes the listener's inference about a category boundary; processing efficiency is measured behaviorally rather than assumed from an acoustic correlation.
- **What the paper reports:** The paper reports behavioral evidence that creaky voice can facilitate Tone 3 processing in the tested Mandarin stimuli.
- **Limits:** Listeners, stimuli, tone context, creak manipulation, and task bound the claim; a processing benefit is not a universal production or perception rule.

## 351. Acoustic similarities, articulatory uniqueness: Speech production mechanisms in individuals with congenital lip paralysis

**Paper:** [Acoustic similarities, articulatory uniqueness: Speech production mechanisms in individuals with congenital lip paralysis](https://www.isca-archive.org/interspeech_2025/hermes25_interspeech.html)
**Taxonomy:** `sound-and-production / articulatory-dynamics / articulatory-coordination`
**Evidence:** D3 full-paper capture; PDF SHA-256 `5df16153e8544dafe7d61176e473bb4ecd22e6ca9611f21c9143f3db9e8c400b`; full-text SHA-256 `6f26e69ae41a5f8b9e4fda1237dfa42c6f13a49c72a80c10e89bd3960ee3c387`.

- **Ordinary problem:** People with congenital lip paralysis may produce acoustically similar speech using different articulatory movements, so sound alone can hide physical uniqueness.
- **Why it is hard:** The acoustic-to-articulatory mapping is many-to-one and compensatory; a stable sound does not imply a normal or shared production mechanism.
- **Naive attempt:** Classify the voice from acoustics alone or assume one acoustic pattern corresponds to one articulatory configuration.
- **Central move:** Compare acoustic similarity with articulatory measurements in individuals with congenital lip paralysis to identify compensatory production mechanisms.
- **Mechanism:** The paper studies acoustic similarities and articulatory uniqueness in speech production by individuals with congenital lip paralysis.
- **Mathematical idea:** Speech production is an inverse problem with compensation: the same acoustic target can arise from different physical routes, so articulatory evidence changes the interpretation of similarity.
- **What the paper reports:** The paper reports acoustic and articulatory findings for the affected speakers and comparison conditions.
- **Limits:** Cohort, anatomy, language, tasks, imaging or motion measures, and acoustic metrics limit clinical generalization; similarity is not a diagnosis.

## 352. Articulatory variations in Apical Vowels in Southwestern Mandarin

**Paper:** [Articulatory variations in Apical Vowels in Southwestern Mandarin](https://www.isca-archive.org/interspeech_2025/huang25f_interspeech.html)
**Taxonomy:** `sound-and-production / articulatory-dynamics / articulatory-coordination`
**Evidence:** D3 full-paper capture; PDF SHA-256 `a6f165ba92d34562837de5435a7a3e4309c2d132785ac45bc1eb3a1babc135fd`; full-text SHA-256 `1bc29262c94ccd8d34825914afcaf37ebe47df84dde08cbb4d1f198a9b1e08ad`.

- **Ordinary problem:** Speakers with different articulatory habits can produce similar apical vowels, but the physical movements behind those sounds may differ across Southwestern Mandarin speakers.
- **Why it is hard:** Tongue shape, place, and coarticulation interact, and acoustic similarity hides multiple articulatory solutions.
- **Naive attempt:** Describe the vowel only by formants or assume one acoustic target has one tongue configuration.
- **Central move:** Measure articulatory variation in apical vowels and relate it to acoustic outcomes across Southwestern Mandarin speakers.
- **Mechanism:** The paper analyzes articulatory variations in apical vowels in Southwestern Mandarin.
- **Mathematical idea:** The sound-to-movement mapping is underdetermined: production data reveal which physical differences are tolerated while the acoustic category stays recognizable.
- **What the paper reports:** The paper reports articulatory variation and its acoustic relationships for the studied apical vowels.
- **Limits:** Speakers, dialect region, imaging or measurement method, vowel context, and sample size limit generalization; variation is not pathology.

## 353. Speaker-specific Patterns of Phonetic Covariation in Korean Word-medial Stops and the Role of Phonological and Morphological Contexts

**Paper:** [Speaker-specific Patterns of Phonetic Covariation in Korean Word-medial Stops and the Role of Phonological and Morphological Contexts](https://www.isca-archive.org/interspeech_2025/kwon25b_interspeech.html)
**Taxonomy:** `sound-and-production / articulatory-dynamics / articulatory-coordination`
**Evidence:** D3 full-paper capture; PDF SHA-256 `4586a1bbfc5da33b9f6a674b2ca31c0f6ee3fc3f43a803c4d4362a8404d37cc5`; full-text SHA-256 `6455044bd9541df1ded41f40bdc203b5efd76155337690cd2cdd80545dcd9311`.

- **Ordinary problem:** A speaker can pronounce the same category differently across sounds and contexts, yet listeners still need the category to remain recognizable.
- **Why it is hard:** Variation that looks random in one measurement may be coordinated with variation in another, and context can change both measurements at once.
- **Naive attempt:** Average across speakers and treat the remaining variation as noise.
- **Central move:** Measure several phonetic dimensions jointly within each speaker and test whether their covariation preserves category contrasts across phonological and morphological contexts.
- **Mechanism:** Seoul Korean word-medial stops are analyzed through speaker-specific distributions and covariation patterns across contexts.
- **Mathematical idea:** The object is a structured distribution, not one canonical pronunciation; correlations and category separation test whether variation is organized.
- **What the paper reports:** The paper reports systematic speaker-specific covariation that keeps stop categories distinct despite contextual variability, supporting a phonetic-uniformity account.
- **Limits:** The language, stop system, contexts, speaker sample, and chosen phonetic measures bound the result; other languages and interactional settings require separate evidence.

## 354. Supralaryngeal Kinematics of Implosives in Central Vietnamese: An EMA Study

**Paper:** [Supralaryngeal Kinematics of Implosives in Central Vietnamese: An EMA Study](https://www.isca-archive.org/interspeech_2025/mcguire25_interspeech.html)
**Taxonomy:** `sound-and-production / articulatory-dynamics / articulatory-coordination`
**Evidence:** D3 full-paper capture; PDF SHA-256 `0328292bb2732ab5a4cf9dbb087172fcce39b156ee19a5115dfeae3123bec4d8`; full-text SHA-256 `bd4404db00be676177ade89a14b92ee7f6532ef5d6b6829bbfbe1511c39ccd91`.

- **Ordinary problem:** To explain an implosive consonant, a researcher must connect its proposed airflow mechanism to the visible movements of the lips and timing of closure and release.
- **Why it is hard:** A voiced stop can resemble an implosive in a broad label, so a movement difference may be caused by voicing rather than implosivity.
- **Naive attempt:** Describe both sounds as voiced stops and assume the same articulatory timing.
- **Central move:** Track lip-aperture trajectories with electromagnetic articulography and compare Vietnamese implosives against voiced and voiceless controls in another language.
- **Mechanism:** EMA measures movement amplitude, velocity, and plateau timing during Central Vietnamese bilabial implosives; Taiwanese Southern Min controls the voicing explanation.
- **Mathematical idea:** The signal is a time course of gestures; mixed-effects comparisons separate a property of implosivity from a generic property of voicing.
- **What the paper reports:** Implosives show greater peak velocity away from closure, while voiceless plosives have a longer gestural plateau; the voiced-plosive control does not reproduce the rapid movement.
- **Limits:** The languages, speakers, consonant inventory, EMA measures, and statistical model bound the result; laryngeal airflow itself was not directly measured.

## 355. Temporal organization of prenuclear glides in Hefei Mandarin

**Paper:** [Temporal organization of prenuclear glides in Hefei Mandarin](https://www.isca-archive.org/interspeech_2025/yang25i_interspeech.html)
**Taxonomy:** `sound-and-production / articulatory-dynamics / articulatory-coordination`
**Evidence:** D3 full-paper capture; PDF SHA-256 `ee4f070b66cbac5bcdcf876ab944c98617be3dc6db4525bb82ae0b7c72c34161`; full-text SHA-256 `bd3f97b30afbb510ea081a6efa83ed0289862e6118573b12671655ec5e6b5e80`.

- **Ordinary problem:** A short glide between a consonant and vowel must be assigned to a syllable position, but timing can make it look like an onset, a nucleus, or a separate segment.
- **Why it is hard:** Abstract phonological structure is not directly visible in the waveform, and competing analyses can fit the same sequence of labels.
- **Naive attempt:** Choose an onset or rime analysis from spelling, phonotactics, or a single duration measurement.
- **Central move:** Measure the timing coordination of consonant-glide-vowel sequences and use the relative movement of gestures to infer which part of the syllable the glide behaves like.
- **Mechanism:** Hefei Mandarin CjV and CwV syllables are analyzed acoustically, comparing glide timing with competing onset and rime accounts.
- **Mathematical idea:** The acoustic trajectory is evidence about an abstract structure; temporal coordination links measurable events to a phonological hypothesis without treating labels as observations.
- **What the paper reports:** The paper finds that both glides are more likely part of the rime, agreeing with prior evidence for [j] but differing from earlier results for [w].
- **Limits:** The dialect, speakers, acoustic method, and competing analyses bound the inference; timing alone cannot settle every phonological representation or generalize across Mandarin varieties.

## 356. On the Language and Gender Biases in PSTN, VoIP and Neural Audio Codecs

**Paper:** [On the Language and Gender Biases in PSTN, VoIP and Neural Audio Codecs](https://www.isca-archive.org/interspeech_2025/altwlkany25_interspeech.html)
**Taxonomy:** `sound-and-production / room-channel-and-sensing / microphone-channel`
**Evidence:** D3 full-paper capture; PDF SHA-256 `76ca03f71b1e2a15e7e4286d244f565c3aa65eff9a25a88cf5790da027d410e5`; full-text SHA-256 `d3dfd410f9f67399270db0a28e307af31502dd97b7474c4ec92ff031b926054d`.

- **Ordinary problem:** A speech system should not degrade one language or gender more than another when audio passes through a codec.
- **Why it is hard:** Transcoding changes the signal before recognition or sentiment analysis, and the codec may interact with language and vocal characteristics.
- **Naive attempt:** Treat a codec as a neutral pipe and measure only average speech quality.
- **Central move:** Transcode millions of multilingual files through PSTN, VoIP, and neural codecs, then compare quality by language and gender.
- **Mechanism:** The study measures speech quality after representative codec paths across more than two million multilingual files.
- **Mathematical idea:** The target is a distribution of quality differences, not one overall mean; grouping by language and gender exposes unequal channel loss.
- **What the paper reports:** PSTN codecs show strong gender bias and neural codecs introduce language bias in the reported analysis.
- **Limits:** Codec set, languages, gender labels, quality measure, and files define the boundary; causal mechanisms and mitigation in deployed networks remain open.

## 357. AISHELL-5: The First Open-Source In-Car Multi-Channel Multi-Speaker Speech Dataset for Automatic Speech Diarization and Recognition

**Paper:** [AISHELL-5: The First Open-Source In-Car Multi-Channel Multi-Speaker Speech Dataset for Automatic Speech Diarization and Recognition](https://www.isca-archive.org/interspeech_2025/dai25c_interspeech.html)
**Taxonomy:** `sound-and-production / room-channel-and-sensing / microphone-channel`
**Evidence:** D3 full-paper capture; PDF SHA-256 `ca7ca91e0626a58f54e98815830576bfb668532013f38628bc3cff94108b13ae`; full-text SHA-256 `68d540033d21becbde1301c3a3a77f9bcaaf55bcc9dd3f9f3b551253c812ae4d`.

- **Ordinary problem:** In-car microphones hear several speakers through reflections, wind, road noise, music, and air conditioning, so a recognizer needs a dataset that preserves the path from talker to sensor.
- **Why it is hard:** Clean speech recorded close to the mouth does not reveal far-field channel mixing, changing geometry, or realistic driving noise; simulated mixtures alone miss those correlations.
- **Naive attempt:** Train ASR on clean or artificially mixed speech and treat the vehicle microphone array as a fixed recording channel.
- **Central move:** Release a multi-channel, multi-speaker in-car corpus with near-field references, far-field door microphones, real driving conditions, noise recordings, and a reproducible separation-plus-ASR baseline.
- **Mechanism:** AISHELL-5 records 2–4 Mandarin speakers in a hybrid vehicle across more than 60 scenarios, with four far-field channels and headset reference microphones. The baseline uses acoustic echo cancellation, independent vector analysis or SpatialNet separation, VAD segmentation, and ASR; the paper reports separate evaluation sets for oracle and predicted segmentation.
- **Mathematical idea:** The far-field mixture is modeled as y(t)=As(t)+n(t); IVA seeks a demixing that makes sources statistically independent. Evaluation uses character error rate for Eval1 and concatenated minimum-permutation CER for Eval2, after front-end processing.
- **What the paper reports:** The corpus contains over 100 hours of speech from 260 participants plus about 40 hours of environmental noise; the baseline exposes large differences between near/far-field and processed conditions, with the reported ASR/front-end results establishing the challenge difficulty.
- **Limits:** The corpus is Mandarin and vehicle-specific, with its seating, microphones, and scenario design defining the boundary. The baseline does not establish that one separation method is best in all cars, and dataset availability is not independent reproduction of the reported scores.

## 358. Voxplorer: Voice data exploration and projection in an interactive dashboard

**Paper:** [Voxplorer: Voice data exploration and projection in an interactive dashboard](https://www.isca-archive.org/interspeech_2025/deluca25_interspeech.html)
**Taxonomy:** `sound-and-production / room-channel-and-sensing / microphone-channel`
**Evidence:** D3 full-paper capture; PDF SHA-256 `614c7e5553af8cb57d72db5b05e3cd455e0ef495f22c6fefffc0c789ef37a913`; full-text SHA-256 `e63926a948c3be8828d511ea4b779691fe6a944221e1d914339a09f8f7c29f99`.

- **Ordinary problem:** Researchers need to see many dimensions of voice data together rather than inspect one acoustic measure at a time.
- **Why it is hard:** High-dimensional features are difficult to extract, subset, and interpret without a usable exploratory interface.
- **Naive attempt:** Export one feature table and rely on fixed plots or isolated measures.
- **Central move:** Put feature extraction, dimensionality reduction, filtering, and projection into an interactive dashboard.
- **Mechanism:** Voxplorer exposes precomputed high-dimensional voice data and can extract features from recordings directly for interactive exploration.
- **Mathematical idea:** The object is an exploratory mapping from many acoustic dimensions to a visual projection; it is a research instrument rather than a predictive model.
- **What the paper reports:** The paper presents a reusable dashboard intended to broaden voice-analysis exploration; no scientific performance score is claimed.
- **Limits:** Usability, projection choices, and feature-tool assumptions determine what researchers see; the dashboard does not establish causal voice categories.

## 359. Improving Low-Resource Dialect Classification Using Retrieval-based Voice Conversion

**Paper:** [Improving Low-Resource Dialect Classification Using Retrieval-based Voice Conversion](https://www.isca-archive.org/interspeech_2025/fischbach25_interspeech.html)
**Taxonomy:** `sound-and-production / room-channel-and-sensing / microphone-channel`
**Evidence:** D3 full-paper capture; PDF SHA-256 `3490081268b6779f7981bba1701ad8fa6915333602531d50c5f2107bf38da39d`; full-text SHA-256 `46b3cc56f8f184d4bef61c78360d53adc2aac2b6045f2bb86b66a5a3f73f9550`.

- **Ordinary problem:** A dialect classifier should learn pronunciation and linguistic differences, but a low-resource dialect corpus may contain too few speakers to separate dialect from speaker identity.
- **Why it is hard:** Speaker-specific vocal traits can be easier to learn than dialect cues, so adding more altered copies of the same speakers may increase data without adding the missing variation.
- **Naive attempt:** Train directly on the small corpus or apply generic noise/masking augmentation that changes the signal without targeting the nuisance speaker factor.
- **Central move:** Use retrieval-based voice conversion to put examples into a more uniform target-speaker space, then combine it with ordinary augmentations and test whether dialect classification improves.
- **Mechanism:** RVC converts low-resource German dialect samples toward a uniform target speaker; experiments compare RVC alone and with frequency masking and segment removal for dialect classification.
- **Mathematical idea:** The augmentation changes speaker identity while attempting to preserve phonetic and dialect information; classifier accuracy tests whether the nuisance factor was reduced rather than merely replaced.
- **What the paper reports:** The paper reports improved dialect-classification performance from RVC augmentation, with further gains when combined with frequency masking and segment removal.
- **Limits:** Dialect data, target speaker, conversion fidelity, train/test speaker split, and classifier architecture bound the claim; higher accuracy does not prove that all dialect cues survived conversion.

## 360. Influence of Room Acoustics on Objective Voice Assessment Methods in the Context of Speech and Language Therapy

**Paper:** [Influence of Room Acoustics on Objective Voice Assessment Methods in the Context of Speech and Language Therapy](https://www.isca-archive.org/interspeech_2025/franz25_interspeech.html)
**Taxonomy:** `sound-and-production / room-channel-and-sensing / reverberant-mixture`
**Evidence:** D3 full-paper capture; PDF SHA-256 `a0a4cbcec9fbb43bce4199389d0524ad03a81891697a9e8ff1dad3452b4ad7f8`; full-text SHA-256 `d9cc72c1aa409f8382a1bc38116c5f8c3e36c2146be02bdc472d9fef79100a66`.

- **Ordinary problem:** A clinical voice measure should describe the speaker, but the microphone also hears the room and the distance from the mouth.
- **Why it is hard:** Reverberation and microphone placement change the measured voice differently for different underlying voice qualities, so a correction that works for one speaker or room can fail for another.
- **Naive attempt:** Treat an acoustic voice-quality score as portable across rooms, or record at a convenient distance and assume background noise is the main problem.
- **Central move:** Measure room impulse responses and compare dry and room-affected AVQI and ABI values across 35 speech-therapy rooms, two microphone positions, and 1,644 voice samples.
- **Mechanism:** The study simulates room conditions with measured impulse responses and noise, computes the difference between room and dry measures, and fits mixed-effects models with room as a fixed effect, the dry score and its interaction, and subject as a random effect.
- **Mathematical idea:** The central quantity is delta X = X_room - X_dry. The selected models obtain normalized RMSE 0.636 for AVQI and 0.669 for ABI, with R2 0.596 and 0.553; the model is descriptive of the tested rooms, not a universal correction.
- **What the paper reports:** Across the rooms, voice-quality measures generally deteriorate by 0–2 units; the smartphone is more affected than the lavalier microphone, and room effects are significant for almost all rooms. Only 8 of 35 rooms meet the stricter A4 reverberation recommendation.
- **Limits:** The rooms, simulated signals, microphones, and Saarbrücken database define the tested boundary; the study does not establish a correction for other clinics or devices. Reported model fits and significance tests are author-reported and were not independently reproduced.

## 361. AuralNet: Hierarchical Attention-based 3D Binaural Localization of Overlapping Speakers

**Paper:** [AuralNet: Hierarchical Attention-based 3D Binaural Localization of Overlapping Speakers](https://www.isca-archive.org/interspeech_2025/fu25_interspeech.html)
**Taxonomy:** `sound-and-production / room-channel-and-sensing / microphone-channel`
**Evidence:** D3 full-paper capture; PDF SHA-256 `4bba6f6ecb2ca8edb40cfadab414a4e3b6d0d94f7d0d0c5762ba57d6fef8c64b`; full-text SHA-256 `14be7eaa1e132373b68508fdde68f1dcdafb2dcffbf86d44aa2fa52d3d4a7527`.

- **Ordinary problem:** A listener or robot should locate several overlapping sounds in three dimensions even when noise and reverberation distort the binaural cues.
- **Why it is hard:** Sources can overlap, source count may be unknown, and reflections blur the timing and level differences that encode direction.
- **Naive attempt:** Estimate one direction with a fixed-resolution classifier or assume the number of sources in advance.
- **Central move:** Use a gated coarse-to-fine model that first detects sectors and then regresses azimuth/elevation with a masked multitask loss.
- **Mechanism:** AuralNet processes binaural signals with multi-head attention, jointly detects sources and estimates azimuth/elevation, and is tested in noisy-reverberant conditions.
- **Mathematical idea:** Classification chooses a spatial sector while regression refines its coordinates; masking lets the loss ignore nonexistent sources.
- **What the paper reports:** The paper reports superiority over recent methods in its noisy-reverberant multi-source experiments.
- **Limits:** The room simulation/recordings, binaural setup, sector design, and source overlap define the claim; far-field microphone arrays and speech-specific attribution remain open.

## 362. Sub-band based Adaptive IIR Algorithm with Biquad Filter Stability Constraints for Feedforward Hear-Through Equalization

**Paper:** [Sub-band based Adaptive IIR Algorithm with Biquad Filter Stability Constraints for Feedforward Hear-Through Equalization](https://www.isca-archive.org/interspeech_2025/gupta25b_interspeech.html)
**Taxonomy:** `sound-and-production / room-channel-and-sensing / microphone-channel`
**Evidence:** D3 full-paper capture; PDF SHA-256 `6597c0f8859668a9c2a930b108fdcc3479c1579ac2579fdf175e79ab00ae34aa`; full-text SHA-256 `6711a4648ee590a4d52f392e28bf44a5a155d42a2e810108949989e8a9997466`.

- **Ordinary problem:** Transparent earbuds should reproduce the outside world while keeping processing delay low enough that the user does not hear a mismatch between direct and replayed sound.
- **Why it is hard:** Adaptive filtering must track changing source directions and room paths, but high-order FIR or neural filters cost delay; IIR filters are compact but can become unstable during adaptation.
- **Naive attempt:** Use a fixed filter or a large adaptive FIR and accept poor tracking, computational cost, or latency.
- **Central move:** Adapt a low-order sub-band IIR equalizer and enforce stability with a biquad/all-pass constraint based on the least-mean-square fourth criterion.
- **Mechanism:** The reference microphone signal is split into sub-bands; feedforward FxLMS/F adaptation updates IIR paths, while cascaded biquads compensate phase/group delay and constrain poles during changing indoor/outdoor conditions.
- **Mathematical idea:** The filter minimizes an error criterion in sub-bands; the fourth-order LMS constraint penalizes unstable coefficient behavior. MSE, SNR, convergence, and multiply-accumulate counts expose the accuracy/latency/complexity trade-off.
- **What the paper reports:** The paper reports up to 13 dB improvement over compared adaptive methods in simulated scenarios, with stable behavior and similar complexity in dynamic indoor/outdoor tests.
- **Limits:** The evidence is simulation-based and depends on acoustic paths, filter orders, and stability settings; user perception, individualized ears, and end-to-end hardware latency are not established.

## 363. Fine-tune Before Structured Pruning: Towards Compact and Accurate Self-Supervised Models for Speaker Diarization

**Paper:** [Fine-tune Before Structured Pruning: Towards Compact and Accurate Self-Supervised Models for Speaker Diarization](https://www.isca-archive.org/interspeech_2025/han25_interspeech.html)
**Taxonomy:** `sound-and-production / room-channel-and-sensing / microphone-channel`
**Evidence:** D3 full-paper capture; PDF SHA-256 `f07840e4bddc8d1f261e9f887b9887153d7408cd6a7b3b6393893917e3b62226`; full-text SHA-256 `2edbdcfe2d1371710acad0430429649106c61223498ea4dcea64d2acb373532e`.

- **Ordinary problem:** A diarization system must assign speech segments to speakers in far-field meetings while fitting on hardware with limited memory and compute.
- **Why it is hard:** Self-supervised encoders contain redundant parameters, but pruning too aggressively can destroy the representations needed when speakers overlap, reverberation is present, or microphones differ.
- **Naive attempt:** Prune the pretrained encoder immediately and hope a small model preserves the full model's speaker boundaries.
- **Central move:** Fine-tune the self-supervised WavLM model on diarization before structured pruning, and use knowledge distillation to preserve the task behavior while removing redundant structure.
- **Mechanism:** The teacher supplies representations or logits for the student; structured channel/layer removal creates a compact model, and diarization error rate on far-field meeting corpora measures the retained segmentation and attribution ability.
- **Mathematical idea:** The central object is a constrained compression path: task adaptation changes which parameters matter before pruning, while distillation penalizes deviation from the adapted teacher.
- **What the paper reports:** On AMI, AISHELL-4, and AliMeeting, the paper reports that fine-tuning before pruning improves the accuracy/size trade-off over pruning without that order.
- **Limits:** Dataset microphone layouts, pruning ratios, teacher/student settings, and DER's treatment of overlap bound the claim; compact diarization is not universal robustness or real-device validation.

## 364. L3C-DeepMFC: Low-Latency Low-Complexity Deep Marginal Feedback Cancellation with Closed-Loop Fine Tuning for Hearing Aids

**Paper:** [L3C-DeepMFC: Low-Latency Low-Complexity Deep Marginal Feedback Cancellation with Closed-Loop Fine Tuning for Hearing Aids](https://www.isca-archive.org/interspeech_2025/hao25_interspeech.html)
**Taxonomy:** `sound-and-production / room-channel-and-sensing / microphone-channel`
**Evidence:** D3 full-paper capture; PDF SHA-256 `cbd7d515b58ab585fdc4b304620743324d09c128a8b1a43eda22933d45cd4f3f`; full-text SHA-256 `b1d98e83057ba4116f54d786bda2afd492bfb59d34ee4e2dd59457f0cc5168e3`.

- **Ordinary problem:** A hearing aid must amplify speech without feeding the receiver's sound back into its microphone, and it must do so with little delay and little computation.
- **Why it is hard:** The acoustic coupling changes over time, while suppressing feedback can also suppress speech; full-band neural processing may be too slow or expensive for a wearable device.
- **Naive attempt:** Use a fixed notch filter or a large neural model that estimates the entire waveform with no explicit latency or complexity constraint.
- **Central move:** Estimate the desired speech's complex spectrum in time-frequency bands and adapt the feedback canceller with closed-loop fine tuning while keeping the model small.
- **Mechanism:** L3C-DeepMFC uses complex spectrum mapping, full- and sub-band recurrent components, and closed-loop fine tuning for marginal feedback cancellation; evaluation varies feedback paths and reports latency, complexity, and speech quality.
- **Mathematical idea:** The complex spectrum keeps magnitude and phase, while a closed loop uses the residual error created by the receiver-microphone path to update cancellation; the system is judged on both suppression and preserved speech.
- **What the paper reports:** The paper reports low-latency, low-complexity feedback cancellation with improved speech quality relative to its baselines under tested hearing-aid conditions.
- **Limits:** Feedback paths, delay budget, hardware assumptions, noise, and quality metrics bound the result; lab cancellation performance is not the same as clinical benefit for every listener.

## 365. SepVAC: Multitask Learning of Speaker Separation, Speaker Localization, Microphone Array Localization, and Room Acoustic Parameter Estimation in Various Acoustic Conditions

**Paper:** [SepVAC: Multitask Learning of Speaker Separation, Speaker Localization, Microphone Array Localization, and Room Acoustic Parameter Estimation in Various Acoustic Conditions](https://www.isca-archive.org/interspeech_2025/hartanto25_interspeech.html)
**Taxonomy:** `sound-and-production / room-channel-and-sensing / microphone-channel`
**Evidence:** D3 full-paper capture; PDF SHA-256 `0b2a4b2b5711c8d8d94649653827aa03961210558b5fe49c097429cea7260216`; full-text SHA-256 `47a1475e07cc080a33d1e5d2c88ccd06930d3cd058ff552e65661cd096b20a94`.

- **Ordinary problem:** A separator must recover each speaker while also coping with where speakers and microphones sit in a reverberant room.
- **Why it is hard:** Noise and reverberation can make room effects look like properties of the speech itself.
- **Naive attempt:** Ask one network to separate speech while treating the room and microphone arrangement as irrelevant nuisance.
- **Central move:** Predict speech separation and the physical recording conditions together, then use curriculum learning to stabilize training.
- **Mechanism:** SepVAC jointly estimates separated speech, speaker locations, microphone-array location, and room acoustic parameters on SMS-WSJ-Plus.
- **Mathematical idea:** Word error rate evaluates the usefulness of the separated signal to recognition; the multitask losses constrain both speech and scene estimates.
- **What the paper reports:** The paper reports a 0.67-point WER improvement over SpatialNet.
- **Limits:** The result is author-reported on SMS-WSJ-Plus and its simulated acoustic conditions; real rooms, imperfect localization, and independent reproduction remain open.

## 366. Conformer-based Ultrasound-to-Speech Conversion

**Paper:** [Conformer-based Ultrasound-to-Speech Conversion](https://www.isca-archive.org/interspeech_2025/ibrahimov25_interspeech.html)
**Taxonomy:** `sound-and-production / room-channel-and-sensing / non-airborne-sensing`
**Evidence:** D3 full-paper capture; PDF SHA-256 `00d449763fa543742c85bca1dcdd08afdecc7fb028bac8208f8afb5d78c6d738`; full-text SHA-256 `40cea7ad1216119bfd29dac3afc764935437d2486a7398a9a73282359b1a3eb9`.

- **Ordinary problem:** A person who cannot or does not want to produce audible speech may still move the tongue and vocal tract; a silent-speech interface should turn those movements into understandable audio.
- **Why it is hard:** Ultrasound observes articulator motion rather than sound, and different speakers produce different motion-to-speech mappings; objective waveform similarity may disagree with what listeners hear.
- **Naive attempt:** Use a fixed image-to-speech mapping or make the model larger without testing whether the extra temporal context helps a speaker.
- **Central move:** Use a Conformer that combines local acoustic-image patterns with longer temporal context, and compare a simpler model with a bi-LSTM extension and a standard CNN.
- **Mechanism:** Two Conformer architectures map ultrasound from four speakers in Ultrasuite-Tal80 to mel spectrograms, then HiFi-GAN produces audio; MSE, mel-cepstral distortion, and a MUSHRA listening test are compared with a 2-D CNN.
- **Mathematical idea:** The input is a time sequence of vocal-tract images and the output is a time sequence of spectral frames; objective distance measures signal similarity, while MUSHRA measures perceived quality, so they test different meanings of 'better.'
- **What the paper reports:** The paper reports no statistically significant objective improvement for either Conformer, but better perceptual quality for the bi-LSTM model; the base model matches the CNN while training about three times faster.
- **Limits:** Four speakers, speaker-specific training, ultrasound alignment, vocoder quality, and the listening panel bound the result; perceptual improvement is not evidence of speaker-independent silent speech or clinical usefulness.

## 367. Direction-Aware Neural Acoustic Fields for Few-Shot Interpolation of Ambisonic Impulse Responses

**Paper:** [Direction-Aware Neural Acoustic Fields for Few-Shot Interpolation of Ambisonic Impulse Responses](https://www.isca-archive.org/interspeech_2025/ick25_interspeech.html)
**Taxonomy:** `sound-and-production / room-channel-and-sensing / reverberant-mixture`
**Evidence:** D3 full-paper capture; PDF SHA-256 `b814a35a63dbf079f8f6188dbbca124b5bc838388e77b29b545189cc1298131b`; full-text SHA-256 `5c25847c6dd582a23617d7b425e379d4778667bd0a5724146907c2926b8ce678`.

- **Ordinary problem:** A listener or renderer needs to know how sound changes across positions and directions in a room, but measuring every room impulse response at every point is expensive.
- **Why it is hard:** A room response depends on source position, listener position, and direction, and an omnidirectional or binaural model can miss how a directional microphone or loudspeaker receives the field.
- **Naive attempt:** Interpolate each measured channel independently or assume one direction represents all incoming sound at a point.
- **Central move:** Learn a spatially continuous neural field that takes source/listener geometry and direction as inputs and predicts ambisonic impulse responses between sparse measurements.
- **Mechanism:** Direction-Aware Neural Acoustic Fields model ambisonic room impulse responses with a neural field and add explicit directional information, evaluating few-shot interpolation against prior monaural/binaural fields.
- **Mathematical idea:** The neural field is a function from geometry and direction to a time-domain response; the key test is whether a smooth physical variation can be inferred from sparse samples without inventing inconsistent channels.
- **What the paper reports:** The paper reports improved few-shot interpolation of directional ambisonic responses over prior neural-field formulations in its room measurements.
- **Limits:** Room geometry, microphone/ambisonic order, sampling locations, interpolation range, and waveform metrics bound the claim; interpolation quality does not prove accurate rendering in unseen rooms or perceptual equivalence.

## 368. Selective Auditory Attention Decoding in Naturalistic Conversations Using EEG-Based Speech Envelope Tracking in Multi-Speaker Environments

**Paper:** [Selective Auditory Attention Decoding in Naturalistic Conversations Using EEG-Based Speech Envelope Tracking in Multi-Speaker Environments](https://www.isca-archive.org/interspeech_2025/ivucic25_interspeech.html)
**Taxonomy:** `sound-and-production / room-channel-and-sensing / non-airborne-sensing`
**Evidence:** D3 full-paper capture; PDF SHA-256 `267fd2ee224ce27dcb65638cb5f0c1406650b676dd63942965142cdaae2ca913`; full-text SHA-256 `fd909ca8f72dc2d060fefa51a714a87bb763b367cf4ea05ec0b031aaddb0c86f`.

- **Ordinary problem:** In a real conversation, a listener must switch between speakers while background talkers continue, and a neural interface would need to track the attended stream through those switches.
- **Why it is hard:** EEG responses are weak and delayed relative to acoustic envelopes; multiple speakers and changing attention make a static decoder an unsafe assumption.
- **Naive attempt:** Train one decoder on a fixed attended speaker and assume it remains valid when attention moves.
- **Central move:** Reconstruct each speech envelope from EEG with a time-lagged ridge model and identify the attended speaker by whichever reconstructed envelope correlates best.
- **Mechanism:** A multivariate linear model maps 62 EEG channels over 0–200 ms lags to speech-envelope samples; leave-one-trial-out validation compares Pearson correlations for target and distractor streams before and after exogenous switches.
- **Mathematical idea:** The weights minimize squared reconstruction error plus λ||w||². Target selection is an argmax over envelope correlations; chance is 33% for the three-speaker comparison.
- **What the paper reports:** Across 36 trials, target-speaker decoding averages 76% ± 12%; performance remains above chance as windows shrink from 20 seconds to 2 seconds, and reconstruction briefly rises after attention switches.
- **Limits:** The experiment uses controlled speakers and exogenous switches, short windows still perform poorly, EEG signal-to-noise limits real-time use, and neural decoding is not equivalent to robust everyday source separation.

## 369. French Listening Tests for the Assessment of Intelligibility, Quality, and Identity of Body-Conducted Speech Enhancement

**Paper:** [French Listening Tests for the Assessment of Intelligibility, Quality, and Identity of Body-Conducted Speech Enhancement](https://www.isca-archive.org/interspeech_2025/joubaud25_interspeech.html)
**Taxonomy:** `sound-and-production / room-channel-and-sensing / non-airborne-sensing`
**Evidence:** D3 full-paper capture; PDF SHA-256 `cc4b7fd2b5a1483a2a62be1dad563841ccaa55eef349cdd2d13d96282b236911`; full-text SHA-256 `1efed6e9c0bb01d8615f2b9db00f3fd63ffda29d6828732fcb1559e574f8085b`.

- **Ordinary problem:** Body-conduction sensors survive loud environmental noise but remove or reshape spectral information, so an enhancement system must improve speech without changing who is speaking.
- **Why it is hard:** Intelligibility, perceived quality, and speaker identity are different targets; a bandwidth-extension model can improve one while damaging another, and objective metrics may not predict listeners.
- **Naive attempt:** Trust a single objective enhancement score as evidence that a sensor signal is intelligible, natural, and identity-preserving.
- **Central move:** Evaluate EBEN with separate listening tasks for intelligibility, quality, and identity, then correlate each human measure with candidate objective metrics across sensor types and sex.
- **Mechanism:** Forehead-accelerometer, rigid-in-ear, and throat-microphone signals from Vibravox are enhanced by EBEN; French Modified Rhyme Tests, MUSHRA, and A/B identification are compared with STOI, N-MOS, and ECAPA2 similarity.
- **Mathematical idea:** Pearson correlation links metric values to listener outcomes; the test uses IQR outlier filtering, Shapiro-Wilk normality checks, and 95% significance thresholds.
- **What the paper reports:** EBEN improves reported quality and intelligibility but slightly harms female throat-microphone identity; STOI correlates strongly with MUSHRA quality (ρ=.87) and ECAPA2 with identification (ρ=.90), while no tested metric reliably predicts intelligibility change.
- **Limits:** The study uses quiet recordings, selected sensors and speakers, one enhancement model, and finite listening tests. Correlation with a perceptual proxy does not establish general clinical or operational usefulness.

## 370. Recreating Neural Activity During Speech Production with Language and Speech Model Embeddings

**Paper:** [Recreating Neural Activity During Speech Production with Language and Speech Model Embeddings](https://www.isca-archive.org/interspeech_2025/khanday25_interspeech.html)
**Taxonomy:** `sound-and-production / room-channel-and-sensing / non-airborne-sensing`
**Evidence:** D3 full-paper capture; PDF SHA-256 `d763f07741caadf63a30595145295d4693820fa54d5670bb5c78df70df74d5bc`; full-text SHA-256 `0f7d2efd317a02c45f636cc33616a86f3dd7b2f58081a96f5477bb55f64c1cc0`.

- **Ordinary problem:** Neural recordings during speech production contain information about linguistic and acoustic planning before or alongside the sound that reaches a microphone.
- **Why it is hard:** High-gamma activity is spatially and temporally structured, while model embeddings compress speech and language differently; a useful embedding must preserve the neural dynamics rather than just correlate with a label.
- **Naive attempt:** Predict neural activity from word IDs or a generic acoustic feature and ignore timing, cortical location, and representational level.
- **Central move:** Use pretrained language and speech-model embeddings as regressors for high-gamma activity, then compare how linguistic and acoustic representations reconstruct spatio-temporal neural signals.
- **Mechanism:** Embedding vectors are aligned to neural time windows and mapped to high-gamma responses; reconstruction quality is evaluated across electrodes, time, and representational sources.
- **Mathematical idea:** The paper treats a learned embedding as a hypothesis about what information is available to the brain, and reconstruction error/correlation as a test of that information's neural correspondence.
- **What the paper reports:** Language and speech embeddings reconstruct measurable neural activity characteristics, with differences across model type and brain locations reported as evidence about linguistic versus acoustic information.
- **Limits:** Neural recordings, participant count, electrode coverage, alignment choices, and correlational reconstruction limit causal interpretation; a good reconstruction is not a speech decoder or clinical interface.

## 371. Articulatory Feature Prediction from Surface EMG during Speech Production

**Paper:** [Articulatory Feature Prediction from Surface EMG during Speech Production](https://www.isca-archive.org/interspeech_2025/lee25d_interspeech.html)
**Taxonomy:** `sound-and-production / room-channel-and-sensing / non-airborne-sensing`
**Evidence:** D3 full-paper capture; PDF SHA-256 `9511c728f630a8161b77a465df753e1cf2fafb9bddf679590e8baf7961cc2652`; full-text SHA-256 `77547d441c5369f945805833bc78f08b195c471367784d09de23140bf562178e`.

- **Ordinary problem:** A silent-speech interface needs to infer intended speech from muscle activity when an acoustic waveform is absent or inaccessible.
- **Why it is hard:** EMG channels reflect overlapping facial and articulatory actions, sensors are sparse, and synchronized EMG plus true articulatory measurements are scarce.
- **Naive attempt:** Map EMG directly to a waveform or text while ignoring the physical intermediate movements.
- **Central move:** Use an EMG encoder with convolutional and Transformer layers to predict EMA positions, pitch, loudness, and auxiliary phonemes, making articulatory structure an intermediate target.
- **Mechanism:** The model minimizes L2 losses for EMA, pitch, and loudness and cross-entropy for phonemes. The predicted EMA coordinates represent tongue, lip, and jaw movement rather than an opaque speech label.
- **Mathematical idea:** Articulatory features provide a structured bottleneck: the system keeps coordinated movement and voice-source information separate, then can use those predictions for later speech reconstruction.
- **What the paper reports:** On 7,565 utterances from one male American English speaker, the paper reports strong EMA and loudness prediction and evaluates held-out utterances using correlations against acoustic-inversion targets.
- **Limits:** Targets are pseudo-ground truth from acoustic-to-articulatory inversion, the speaker is not diverse, experiments focus on vocalized open-vocabulary speech, and feature prediction is not the same as intelligible silent-speech synthesis.

## 372. Unified Microphone Conversion: Many-to-Many Device Mapping via Feature-wise Linear Modulation

**Paper:** [Unified Microphone Conversion: Many-to-Many Device Mapping via Feature-wise Linear Modulation](https://www.isca-archive.org/interspeech_2025/ryu25b_interspeech.html)
**Taxonomy:** `sound-and-production / room-channel-and-sensing / microphone-channel`
**Evidence:** D3 full-paper capture; PDF SHA-256 `e27b9ba57c6fbf6030e92b7a778a15ba1ff76dc7f4fc2165625fb12fa98611c9`; full-text SHA-256 `8634841c4c2d03647427e4d8f55a88ef265a42c3c54380f92ba84607ed8f89d6`.

- **Ordinary problem:** A recognizer should tolerate microphone/device changes without collecting paired recordings for every device pair.
- **Why it is hard:** Device responses alter spectral evidence, and many-to-many conversion must preserve speech content while changing channel coloration.
- **Naive attempt:** Duplicate channels, apply generic stereo equalization, or train one converter separately for every source-target pair.
- **Central move:** Learn a unified many-to-many microphone conversion model using feature-wise linear modulation to condition conversion on source and target devices.
- **Mechanism:** FiLM parameters modulate intermediate features according to device identities, allowing one model to represent multiple channel mappings.
- **Mathematical idea:** Device conversion is a conditional channel transformation: content is shared while microphone response is the variable being controlled.
- **What the paper reports:** The paper reports unified microphone conversion results across device mappings without paired examples for every target pair.
- **Limits:** Device inventory, pairing protocol, training coverage, content preservation metrics, and acoustic conditions bound transfer; channel conversion is not the same as recognizer invariance.

## 373. Effect of Noise Floor in Room Impulse Response on Speech Perception Under Spherical Harmonics-based Spatial Sound Reproduction

**Paper:** [Effect of Noise Floor in Room Impulse Response on Speech Perception Under Spherical Harmonics-based Spatial Sound Reproduction](https://www.isca-archive.org/interspeech_2025/zhang25e_interspeech.html)
**Taxonomy:** `sound-and-production / room-channel-and-sensing / reverberant-mixture`
**Evidence:** D3 full-paper capture; PDF SHA-256 `5d9cd458088ec9a3b1432a9261977f3d22139a6b6ce208e68a1ea5425f3d3186`; full-text SHA-256 `d583945483e99c2a5fa0352af1744ef26113d8933492df20a2a6fd94112473e4`.

- **Ordinary problem:** Spatial sound reproduction should reproduce speech perception measured in real rooms.
- **Why it is hard:** Measured room impulse responses contain a noise floor that can create artificial late energy and alter intelligibility in reverberant spaces.
- **Naive attempt:** Use any measured RIR or truncate it mechanically and assume the rendered room remains perceptually faithful.
- **Central move:** Vary RIR noise floor and compare speech-in-noise listening in spherical-harmonic reproduction against the rooms where the RIRs were measured.
- **Mechanism:** The RIR encodes direct and reflected paths; its residual floor changes the rendered reverberant tail, which is tested through intelligibility comparisons.
- **Mathematical idea:** Room reproduction is a channel-matching problem: the measurement’s noise floor is part of the rendered evidence unless controlled.
- **What the paper reports:** The paper reports better reproducibility with low-noise-floor RIRs in highly reverberant rooms and at 5 m, while truncation usually did not help.
- **Limits:** Rooms, source distances, RIR measurement, listening protocol, and speech-in-noise task bound transfer; perceptual reproducibility is not exact physical localization.

## 374. Analysis of Avian Biphonic Vocalization Using Computational Modelling

**Paper:** [Analysis of Avian Biphonic Vocalization Using Computational Modelling](https://www.isca-archive.org/interspeech_2025/a25_interspeech.html)
**Taxonomy:** `sound-and-production / source-generation / vocal-tract-filter`
**Evidence:** D3 full-paper capture; PDF SHA-256 `2875a69d4f661d513c1f0c913fe10261e6fcb12f6f408a44bf88e2618169f433`; full-text SHA-256 `86c609f79f2c4ddbb4e833b16ae31c83ec93ea3d5832d2d0ddfe4977df44b543`.

- **Ordinary problem:** Explain how a bird can produce two simultaneous vocal components from a coupled sound source and vocal tract.
- **Why it is hard:** The observed spectrum mixes two sources with filtering and resonance, so a single-source explanation cannot account for the biphonic signal.
- **Naive attempt:** Model one source and attribute every spectral peak to a single vocal-tract filter.
- **Central move:** Build a finite-element model with dual sources and vary tract geometry to connect physical parameters to observed bandwidth and resonance.
- **Mechanism:** A reconstructed syrinx and upper tract are represented in COMSOL; source placement and geometric parameters are changed, then simulated vocalizations are compared with recordings of real birds.
- **Mathematical idea:** Finite-element equations approximate pressure and displacement over small spatial elements; parameter sweeps test how tracheal length, glottal radius, and beak angle move resonances.
- **What the paper reports:** The paper reports experimentally validated biphonic simulations and systematic effects of tract geometry on resonance modulation and syllable bandwidth.
- **Limits:** The model concerns avian vocalization rather than human speech; micro-CT reconstruction, source assumptions, and validation recordings constrain the result. No independent reproduction was performed.

## 375. Vocal-tract model with two directions: Static design for a dummy head and dynamic design for a speaking machine

**Paper:** [Vocal-tract model with two directions: Static design for a dummy head and dynamic design for a speaking machine](https://www.isca-archive.org/interspeech_2025/arai25_interspeech.html)
**Taxonomy:** `sound-and-production / source-generation / vocal-tract-filter`
**Evidence:** D3 full-paper capture; PDF SHA-256 `d529f0df5e18eca2155c00684009c3a950f1d99452b504957a32fb4962cd99a3`; full-text SHA-256 `522213cc77fae999e65e9509d034eabc0cb5a11315ab6c49fc412efbebdf671d`.

- **Ordinary problem:** A physical vocal-tract model should either hold a known shape still for teaching or change shape over time to demonstrate articulation.
- **Why it is hard:** A static model is repeatable but cannot show movement; a dynamic machine is expressive but harder to build and interpret.
- **Naive attempt:** Use one simplified tube model for every purpose and ignore the missing detail or motion.
- **Central move:** Show the two ends of the design space: a fixed one-vowel dummy head and a cam-driven model whose blocks change shape in real time.
- **Mechanism:** The static model fixes one tract configuration and radiates a repeatable vowel; the dynamic model uses blocks and cams to change simulated articulators and tract shape.
- **Mathematical idea:** The relevant object is tract geometry, which determines resonances and radiation; this demonstration has no common benchmark score.
- **What the paper reports:** The paper demonstrates both models and argues that static and dynamic versions serve different education, phonetics, pathology, and technology purposes.
- **Limits:** This is a two-page demonstration with no shared quantitative evaluation or claim of human-speech equivalence.

## 376. Evaluation of a model for sound radiation from the vocal tract wall

**Paper:** [Evaluation of a model for sound radiation from the vocal tract wall](https://www.isca-archive.org/interspeech_2025/birkholz25_interspeech.html)
**Taxonomy:** `sound-and-production / source-generation / vocal-tract-filter`
**Evidence:** D3 full-paper capture; PDF SHA-256 `485017b94dee041ec09f1944a4ee6834145618b4f2293e3489ced5f1e3eec9d4`; full-text SHA-256 `cbdc43270b4561630cbfe27ab327ca91e6848fa951936e029ddbaf907a6d5511`.

- **Ordinary problem:** An articulatory synthesizer should model not only sound traveling through the vocal tract but also sound radiating through its walls.
- **Why it is hard:** A simple physical model must reproduce speaker-specific radiation without adding an impractical number of parameters.
- **Naive attempt:** Ignore wall radiation or use one fixed radiation response for every speaker.
- **Central move:** Represent each tract section as a damped spring-mass system and fit wall parameters to real speaker voicebars.
- **Mechanism:** The simulated radiation from tube sections is compared with six speakers producing /b,d,g/ in vowel contexts, with parameters optimized to real spectra.
- **Mathematical idea:** Frequency-domain root-mean-square error between simulated and natural voicebar spectra measures how well the physical model explains the radiation.
- **What the paper reports:** The paper reports 2.26–3.82 dB RMSE from 0–800 Hz and concludes the simple model can reproduce the spectra closely.
- **Limits:** The six speakers, selected consonants/vowels, frequency range, and fitted parameters bound the claim; other speech sounds and independent physical validation remain open.

## 377. Influence of wall coverings of 3D-printed vocal tract models on measured transfer functions

**Paper:** [Influence of wall coverings of 3D-printed vocal tract models on measured transfer functions](https://www.isca-archive.org/interspeech_2025/birkholz25b_interspeech.html)
**Taxonomy:** `sound-and-production / source-generation / vocal-tract-filter`
**Evidence:** D3 full-paper capture; PDF SHA-256 `ecb8ea59cb5269cfb4ec3ae01f5b0cfe5a6824d12760d0104a67d84f186d0c20`; full-text SHA-256 `010eccd1c99926018ac344857fa59fbc5486db18566b0da6187553fe1faccd31`.

- **Ordinary problem:** A physical vocal-tract replica should reveal the resonances of a modeled vowel, but the printed walls can vibrate and create false peaks and gaps.
- **Why it is hard:** The measurement apparatus can confuse sound transmitted through the model body with sound traveling through the intended tract cavity.
- **Naive attempt:** Trust the measured transfer function or change only the acoustic excitation while ignoring the replica's structural vibration.
- **Central move:** Dampen or mechanically constrain the replica and test whether the expected resonances become cleaner and more repeatable.
- **Mechanism:** Ten axisymmetric 3D-printed vowel tubes are measured with reciprocity; sound-absorbing fabric and sand embedding are compared as artifact-reduction methods.
- **Mathematical idea:** The transfer function is a physical measurement shaped by both air paths and solid-body vibration; artifact reduction is tested through resonance structure and repeatability.
- **What the paper reports:** Both coverings reduce spurious poles and zeros and improve repeatability of the measured transfer functions.
- **Limits:** Printed geometries, ten vowels, materials, reciprocity setup, and repeatability metric bound the claim; improved measurement does not prove the replica matches a human tract.

## 378. Equivalence and differences: Formant patterns of labialization and pharyngealization in Tashlhiyt

**Paper:** [Equivalence and differences: Formant patterns of labialization and pharyngealization in Tashlhiyt](https://www.isca-archive.org/interspeech_2025/buech25_interspeech.html)
**Taxonomy:** `sound-and-production / source-generation / vocal-tract-filter`
**Evidence:** D3 full-paper capture; PDF SHA-256 `86ee48dd3d0986f191969e463e4cbedcd3b022c82b4423920868cc68020b48b7`; full-text SHA-256 `4302d506b1cbf8d07ff834f1f5d3928dccec9d59957d452d2c429f3305a4a9ff`.

- **Ordinary problem:** Two different tongue and lip gestures may produce similar formant changes, so a listener or analyst cannot infer articulation from one acoustic cue alone.
- **Why it is hard:** Labialization and pharyngealization modify different parts of the tract but can both lower F2, making a shared acoustic effect look like a shared gesture.
- **Naive attempt:** Treat a low F2 as proof of one particular secondary articulation.
- **Central move:** Compare adjacent-vowel formants across both articulations, vowel qualities, and speakers, then identify which formants preserve their difference.
- **Mechanism:** Thirty-five Tashlhiyt speakers produce VCV logatomes with /i, a, u/ and labialized or pharyngealized consonants; F1 and F2 patterns are compared.
- **Mathematical idea:** The mapping is many-to-one: F2 can reveal a broad acoustic effect while F1 and vowel context retain articulatory distinctions.
- **What the paper reports:** Both articulations show similar F2 effects, strongest for /i/ and then /a/, while differences depend on F1 and vowel quality.
- **Limits:** The language, speakers, logatomes, adjacent vowels, and formant measures bound the result; formants alone cannot identify every articulatory gesture.

## 379. Phonetic Posteriorgram-Based Phoneme Selection for Vocal Cord Disorder Classification in Continuous Mandarin Speech

**Paper:** [Phonetic Posteriorgram-Based Phoneme Selection for Vocal Cord Disorder Classification in Continuous Mandarin Speech](https://www.isca-archive.org/interspeech_2025/chen25n_interspeech.html)
**Taxonomy:** `sound-and-production / source-generation / vocal-tract-filter`
**Evidence:** D3 full-paper capture; PDF SHA-256 `728f61c6daf8cfd51d64d5f360e2ddf4c81ce1438f55a39e6d56604314fa4331`; full-text SHA-256 `e8d6e6eeea546e1a4c3c051381de8233b5ef8a44bd78a477cddd350ff83edbe2`.

- **Ordinary problem:** A screening system for vocal-cord disorders should use continuous Mandarin speech, where the diagnostic evidence is spread across many phonemes rather than one carefully chosen sound.
- **Why it is hard:** Some phonemes reveal laryngeal behavior more clearly than others, but selecting them from the speech signal can also make the classifier depend on speaker, text, or recording conditions.
- **Naive attempt:** Average the whole utterance or use a fixed phoneme list and assume every segment contributes equally.
- **Central move:** Use phonetic posteriorgrams to identify informative phoneme segments, then classify vocal-cord disorders from the selected evidence.
- **Mechanism:** The paper proposes phonetic-posteriorgram-based phoneme selection for vocal-cord-disorder classification in continuous Mandarin speech.
- **Mathematical idea:** The recognizer supplies a soft map from sound to phonetic identity; selection makes the diagnostic model focus on the speech units that expose the relevant production difference.
- **What the paper reports:** The paper reports classification results for the selected phonetic evidence on continuous Mandarin speech.
- **Limits:** Cohort, disorder labels, language, transcript quality, phoneme selection, and recording conditions limit clinical generalization; classification is not diagnosis.

## 380. Study of vocal fold vibration using M-mode ultrasound: a proof of concept

**Paper:** [Study of vocal fold vibration using M-mode ultrasound: a proof of concept](https://www.isca-archive.org/interspeech_2025/dindart25_interspeech.html)
**Taxonomy:** `sound-and-production / source-generation / periodic-source`
**Evidence:** D3 full-paper capture; PDF SHA-256 `aed2d0b2379710a350e722ef8c774f2015d3599dd402cc352c436de22b478811`; full-text SHA-256 `64692572cf39ba3afff8e678bd02d87d3aac00707859416692d91dd5ac0f087a`.

- **Ordinary problem:** Vocal-fold vibration is physical motion that a microphone observes indirectly; ultrasound may measure the motion itself.
- **Why it is hard:** Ultrasound has spatial and temporal limits, and frequency estimates can alias when the voice is faster than acquisition.
- **Naive attempt:** Treat waveform pitch as the only description of vocal-fold motion.
- **Central move:** Use M-mode ultrasound along the larynx and compare its fundamental-frequency estimate with simultaneous voice analysis.
- **Mechanism:** Spatio-temporal maps of the fundamental and second harmonic are compared with median f0 from recordings.
- **Mathematical idea:** A linear fit gives f0-US = 0.997 f0-voice + 0.293 with correlation 0.999; differences are below 2 Hz in 92% of recordings.
- **What the paper reports:** The paper reports close agreement and reveals temporal drift; four high-pitched recordings expose aliasing.
- **Limits:** The 500-Hz rate, probe placement, healthy participants, and excluded aliased cases limit clinical and high-pitch claims.

## 381. Hybrid Expert Knowledge and Self-Supervised Learning for Diagnostic Modeling of Adductor Spasmodic and Primary Myotonic Dysphonia

**Paper:** [Hybrid Expert Knowledge and Self-Supervised Learning for Diagnostic Modeling of Adductor Spasmodic and Primary Myotonic Dysphonia](https://www.isca-archive.org/interspeech_2025/du25c_interspeech.html)
**Taxonomy:** `sound-and-production / source-generation / periodic-source`
**Evidence:** D3 full-paper capture; PDF SHA-256 `aee0fb89da91dc7017710a711677aac32c95edaf75ef8566d6e708e0c924f58a`; full-text SHA-256 `e2cdaf4d4b9810bc71588c6408d84952c70872e220329a59719eed60f94610dd`.

- **Ordinary problem:** Clinicians must distinguish two voice disorders from patients' speech, but expert listening is scarce and subjective.
- **Why it is hard:** The disorders can sound similar and their acoustic signs vary across patients.
- **Naive attempt:** Rely only on a clinician's global impression or on generic acoustic features.
- **Central move:** Combine expert-designed voice measures with representations learned directly from the waveform.
- **Mechanism:** A CNN receives handcrafted features and self-supervised waveform representations and predicts ADSD versus pMTD on a newly collected patient dataset.
- **Mathematical idea:** The decision is a two-class prediction; accuracy measures the fraction of correctly classified patients.
- **What the paper reports:** The paper reports 83.3% classification accuracy.
- **Limits:** The result is tied to the constructed dataset, its patient mix, and the two diagnoses; clinical deployment, calibration, and external validation remain open.

## 382. French schwa is not acoustically distinct  from its two lexical neighbors /ø/ and /œ/

**Paper:** [French schwa is not acoustically distinct  from its two lexical neighbors /ø/ and /œ/](https://www.isca-archive.org/interspeech_2025/hutin25_interspeech.html)
**Taxonomy:** `sound-and-production / source-generation / vocal-tract-filter`
**Evidence:** D3 full-paper capture; PDF SHA-256 `5607bc71644177b62bd811027c08eccfcd6ed0be6fb97ae895af2878c37ec140`; full-text SHA-256 `be1b290332ca04cbfbe3233f1f9ed01cc6757e45d158744894935fddf87711f5`.

- **Ordinary problem:** A French schwa may be written as a distinct vowel, but listeners may not hear a stable acoustic difference from neighboring /ø/ and /œ/ in ordinary context.
- **Why it is hard:** Vowel categories are shaped by context, speaker, dialect, and lexical function; absence of an acoustic contrast does not mean absence of a linguistic role.
- **Naive attempt:** Measure average formants in isolated tokens and assume every phonological category has a separate acoustic target.
- **Central move:** Compare schwa and its lexical neighbors in natural contexts while separating acoustic overlap from lexical and phonological distribution.
- **Mechanism:** The paper argues that French schwa is not acoustically distinct from its two lexical neighbors /ø/ and /œ/.
- **Mathematical idea:** The study separates category labels from acoustic contrast: a language can maintain a lexical distinction or alternation without a stable one-to-one formant separation.
- **What the paper reports:** The paper reports acoustic overlap between French schwa and the neighboring vowels in the tested materials.
- **Limits:** Speakers, dialect, context, corpus, measurements, and lexical analysis bound the claim; acoustic overlap is not proof that all grammatical distinctions disappear.

## 383. On Enhancing the Performance of Children's ASR Task in Limited Data Scenario

**Paper:** [On Enhancing the Performance of Children's ASR Task in Limited Data Scenario](https://www.isca-archive.org/interspeech_2025/ankita25_interspeech.html)
**Taxonomy:** `sound-and-production / time-frequency-measurement / multi-resolution-signal`
**Evidence:** D3 full-paper capture; PDF SHA-256 `3a75dd67cd146b052fe9f209c110bc9455c392c2da3695072dda9ee3324390e6`; full-text SHA-256 `3299f5b4c4d07d68c90f206649084ded18c031b6635a0cb426b268a4d6a4114d`.

- **Ordinary problem:** A child ASR system must recognize speech when only a small amount of child data is available.
- **Why it is hard:** Children's voices differ from adults and scarce data makes both acoustic modeling and pronunciation variation difficult.
- **Naive attempt:** Train a standard spectrum-only ASR model and accept its data-scarcity error.
- **Central move:** Augment in-domain data, add glottal-activity information to spectral features, and normalize features with fMLLR.
- **Mechanism:** The study compares a baseline with augmented data, MFCCs plus glottal parameters, and fMLLR-normalized features.
- **Mathematical idea:** Character error rate is the main error measure; relative reduction compares each system with the baseline.
- **What the paper reports:** The combined normalized MFCC and glottal features give a reported 40% relative character-error-rate reduction over baseline.
- **Limits:** The evidence is limited to the child's speech data and tested feature pipeline; languages, age ranges, and transfer to new schools or microphones are not established.

## 384. Influence of Proficiency and L2 Experience on Dynamic Spectral Cue Utilization in L2 Vowel Perception and Production

**Paper:** [Influence of Proficiency and L2 Experience on Dynamic Spectral Cue Utilization in L2 Vowel Perception and Production](https://www.isca-archive.org/interspeech_2025/bakkouche25b_interspeech.html)
**Taxonomy:** `sound-and-production / time-frequency-measurement / windowed-spectrum`
**Evidence:** D3 full-paper capture; PDF SHA-256 `2fe715ce3cb6a5756941f5fbaa1adf3327c7bd596ee88b33f769c6c426283e0d`; full-text SHA-256 `15cc1d3bfaaa64e88a8c5ddbcbff13c2f2a214f068bbe3c3092984de2ccffd71`.

- **Ordinary problem:** A learner must hear and produce an unfamiliar vowel contrast whose important evidence changes over time rather than staying at one frequency point.
- **Why it is hard:** Similar categories overlap, and static formant snapshots miss the movement that distinguishes them.
- **Naive attempt:** Measure one midpoint formant and treat perception and production as separate abilities.
- **Central move:** Track vowel-inherent spectral change across the vowel and compare perception-production alignment with proficiency and immersion experience.
- **Mechanism:** Polish learners produce and perceive English /e-æ/ and /i-I/; dynamic formant movement is measured over vowel duration.
- **Mathematical idea:** Formant trajectories are time-varying objects; accuracy and production consistency test whether the moving cue is learned.
- **What the paper reports:** Advanced learners improve, especially for /i-I/; formant movement increases with proficiency, while length of residence is not significant.
- **Limits:** The learner group, contrasts, language experience, and measurements bound the result; other L1s and natural interaction need separate evidence.

## 385. Frequency-Domain Enhanced Extreme Bandwidth Extension Network with ICCRN for Superior Speech Quality

**Paper:** [Frequency-Domain Enhanced Extreme Bandwidth Extension Network with ICCRN for Superior Speech Quality](https://www.isca-archive.org/interspeech_2025/bao25_interspeech.html)
**Taxonomy:** `sound-and-production / time-frequency-measurement / multi-resolution-signal`
**Evidence:** D3 full-paper capture; PDF SHA-256 `0f92e471abc8a855bbd0ce77b0a2a5de3cc4af28f42042ade74c42afe388b474`; full-text SHA-256 `90d50e3359336a52169c4684a849ab1297fe84aa78c095a60f4dd7da2cc1c30d`.

- **Ordinary problem:** Bandwidth extension must recreate missing high-frequency speech without inventing spectral detail that listeners hear as distortion.
- **Why it is hard:** The missing band is not directly supervised by the degraded input; spectral errors can raise objective quality scores while changing consonant detail.
- **Naive attempt:** Copy low-frequency structure upward with a generic network and judge it by one waveform metric.
- **Central move:** Use frequency-domain enhancement with an ICCRN-style recurrent representation to preserve global spectral structure while reconstructing the absent band.
- **Mechanism:** The model operates on frequency representations, combines local and global context, and is compared against EBEN and other bandwidth-extension baselines.
- **Mathematical idea:** PESQ, SI-SDR, STOI, and MUSHRA separate signal fidelity, intelligibility, and listener preference.
- **What the paper reports:** The tests show gains over the original EBEN, including a 40-person MUSHRA comparison; the authors report clearer high-frequency detail and less distortion.
- **Limits:** French LibriSpeech, sampling setup, listeners, and author-reported metrics bound the result; other languages remain open.

## 386. Introducing EMOPARKNZ: the Emotional Speech Database from New Zealand English Speakers with Parkinson’s Disease

**Paper:** [Introducing EMOPARKNZ: the Emotional Speech Database from New Zealand English Speakers with Parkinson’s Disease](https://www.isca-archive.org/interspeech_2025/bendom25_interspeech.html)
**Taxonomy:** `sound-and-production / time-frequency-measurement / multi-resolution-signal`
**Evidence:** D3 full-paper capture; PDF SHA-256 `d3b4fdc89eb8ad2c62d275f15163b879e1f7153745a6061ab55bd6e844357fc5`; full-text SHA-256 `c76c71c1c3631487aed75873d5be5460137083c74d73018e5408f60fece9c2ef`.

- **Ordinary problem:** Researchers need emotional speech from people with Parkinson's disease to study how disease and emotion interact in voice.
- **Why it is hard:** Small clinical datasets make it hard to separate emotional variation from speaker, disease, and language variation.
- **Naive attempt:** Reuse a generic emotion corpus or collect labels without documenting participant and recording choices.
- **Central move:** Create a dedicated New Zealand English database with multiple emotions, speakers, and acoustic analysis, then test human recognition.
- **Mechanism:** EMOPARKNZ contains 1,950 recordings from 13 speakers across five emotions; acoustic measures and a 22-listener perception test are reported.
- **Mathematical idea:** F0, intensity, rate, and five-way listener accuracy connect measurable speech changes to perceived emotion.
- **What the paper reports:** The paper reports emotion-dependent acoustic differences and 63% listener classification accuracy.
- **Limits:** Thirteen speakers, New Zealand English, Parkinson's disease, and the selected emotions bound the resource; clinical severity and broader populations remain open.

## 387. Universal Speech Enhancement with Regression and Generative Mamba

**Paper:** [Universal Speech Enhancement with Regression and Generative Mamba](https://www.isca-archive.org/interspeech_2025/chao25b_interspeech.html)
**Taxonomy:** `sound-and-production / time-frequency-measurement / multi-resolution-signal`
**Evidence:** D3 full-paper capture; PDF SHA-256 `a31e1221b40d1ecf873e80b9e20282bf693d58c58b6900f6020aa824a9fb8657`; full-text SHA-256 `920d9825787f46900d458ddf5af08f38fa540a87cfff03bbcf9e1261213b6fc1`.

- **Ordinary problem:** Enhancement must handle speech that is noisy, reverberant, clipped, bandwidth-limited, packet-damaged, or recorded at another sampling rate without flattening the changing sound structure.
- **Why it is hard:** A model trained on one distortion and one sampling rate can fail when the missing evidence must be invented rather than merely attenuated; long recordings also make full attention expensive.
- **Naive attempt:** Use one masking network that scales down whatever is present, or train separate systems for each distortion and sampling rate.
- **Central move:** Use a linear-time state-space model that represents time and frequency together, maps rather than only masks the spectrum, and switches to flow-based generation when content is missing.
- **Mechanism:** USEMamba applies time/frequency Mamba blocks to compressed STFT features, uses sampling-frequency-independent windows, and combines time, multi-resolution STFT, and phase losses. A flow variant samples missing spectrogram content; a simple energy rule selects the generative output for bandwidth-extension and packet-loss regions.
- **Mathematical idea:** The regression model minimizes a weighted L1 waveform loss, multi-resolution STFT loss, and phase loss. The flow model learns a conditional velocity field from noise to clean STFT coefficients and integrates it with an Euler solver; evaluation includes PESQ, ESTOI, SDR, spectral distances, quality estimators, speaker similarity, and word accuracy.
- **What the paper reports:** On the URGENT 2025 conditions spanning seven distortions, five languages, and several sampling rates, the combined system achieved second place in the blind Track 1 phase; regression worked best for most conditions while generation helped packet loss and bandwidth extension.
- **Limits:** The regression model was trained only on English, the challenge data and distortions define the tested generality, and the flow output sometimes had residual noise or wrong phonemes for long packet losses. Ranking and objective metrics do not establish human usefulness in every language or device; no independent reproduction was performed.

## 388. Neural Spectral Band Generation for Audio Coding

**Paper:** [Neural Spectral Band Generation for Audio Coding](https://www.isca-archive.org/interspeech_2025/choi25d_interspeech.html)
**Taxonomy:** `sound-and-production / time-frequency-measurement / sampling-and-quantization`
**Evidence:** D3 full-paper capture; PDF SHA-256 `3a85e632e3633a9b0e5d5184f5a2c552edfde62e984c674d21e06880ac9bcace`; full-text SHA-256 `7cbb133afab923f0ba67334750e23824599364d36eb76a64ca33603c028843c6`.

- **Ordinary problem:** A low-bitrate codec may preserve the important low frequencies while losing high-frequency detail that makes speech and other sounds clear.
- **Why it is hard:** High-frequency content is not a fixed copy of the low-frequency band; different signals need different missing detail, and simply replicating a subband can add noise or dullness.
- **Naive attempt:** Copy or repeat the low-frequency spectrum into the missing band with a fixed spectral-band-replication rule.
- **Central move:** Encode compact side information about the missing band and use a learned generator conditioned on that information and the decoded core band.
- **Mechanism:** Neural spectral band generation uses an encoder-decoder to quantize high-frequency side information, reconstructs the band from core audio plus that information, and trains the whole codec with adversarial perceptual criteria.
- **Mathematical idea:** The codec separates what is transmitted from what is generated: the core band carries a base signal while a compact code selects plausible high-frequency detail; rate and perceptual quality expose the tradeoff.
- **What the paper reports:** Using AAC as the core codec, the paper reports that n-SBG outperforms conventional SBR at comparable bitrates, especially at low rates, though some codec/rate combinations introduce audible noise.
- **Limits:** The core codec, bitrate, adversarial training, signal types, and perceptual metric bound the claim; plausible high-frequency detail is not guaranteed to be the original detail or to improve every downstream speech task.

## 389. An interpretable speech foundation model for depression detection by revealing prediction-relevant acoustic features from long speech

**Paper:** [An interpretable speech foundation model for depression detection by revealing prediction-relevant acoustic features from long speech](https://www.isca-archive.org/interspeech_2025/deng25b_interspeech.html)
**Taxonomy:** `sound-and-production / time-frequency-measurement / windowed-spectrum`
**Evidence:** D3 full-paper capture; PDF SHA-256 `205b56374a13e30924af66ef9429852ce62be0da69800e314c28272025dad16c`; full-text SHA-256 `66b9e0df6e243230b8487a706543ba6b0e4a8da14d0653a432a948e804dafa29`.

- **Ordinary problem:** A speech-based depression screening system should use enough of a person's speech to reflect a clinical state rather than treating a long answer as a bag of short unrelated clips.
- **Why it is hard:** Short segments can receive noisy labels because depression is labeled at the recording or person level, and a model may rely on loudness or pitch without showing a clinician what it used.
- **Naive attempt:** Split every recording into short windows, assign the same label to each, and report only a black-box score.
- **Central move:** Model the full speech recording and expose which time-frequency regions and acoustic properties drive the decision.
- **Mechanism:** The paper uses a speech-level Audio Spectrogram Transformer on long-duration speech and introduces an interpretation method that identifies prediction-relevant acoustic features, comparing it with a segment-level AST.
- **Mathematical idea:** Longer context reduces segment-label noise; attention over the spectrogram is converted into an acoustic explanation, so the model's output is treated as evidence to inspect rather than a diagnosis itself.
- **What the paper reports:** The paper reports better depression detection than the segment-level model and identifies reduced loudness and F0 as relevant signals consistent with prior clinical findings.
- **Limits:** Dataset, diagnostic labels, recording protocol, attention interpretation, and screening threshold bound the claim; a predictive acoustic correlate is not a clinical cause or validated diagnosis.

## 390. Adaptive Differential Denoising for Respiratory Sounds Classification

**Paper:** [Adaptive Differential Denoising for Respiratory Sounds Classification](https://www.isca-archive.org/interspeech_2025/dong25e_interspeech.html)
**Taxonomy:** `sound-and-production / time-frequency-measurement / windowed-spectrum`
**Evidence:** D3 full-paper capture; PDF SHA-256 `26de42ef3f23f323ef6538936362cfbfc5bc97c9195f9d88dfede52dd8659523`; full-text SHA-256 `14794ce748217cb568c4fe1768f26f02a73a7fed2dafc4baf1440198f90808f4`.

- **Ordinary problem:** Respiratory sounds are noisy measurements of a changing physical process, and a classifier needs to preserve disease-relevant events while suppressing irrelevant noise.
- **Why it is hard:** Breath sounds overlap in time and vary by microphone, patient, environment, and pathology; fixed denoising can remove the very irregularity being measured.
- **Naive attempt:** Apply one fixed noise filter or classify raw recordings without testing how denoising changes the signal.
- **Central move:** Use an adaptive differential denoising procedure whose behavior changes with the observed respiratory signal, then test classification.
- **Mechanism:** The paper proposes adaptive differential denoising for respiratory-sound classification and compares it with less adaptive processing.
- **Mathematical idea:** Denoising is part of the measurement model: the classifier can only learn a clinical distinction if the preprocessing preserves the relevant temporal-acoustic structure.
- **What the paper reports:** The paper reports improved respiratory-sound classification with the proposed denoising approach.
- **Limits:** Dataset, labels, recording hardware, noise conditions, and evaluation split limit generalization to clinical deployment or diagnosis.

## 391. Functional Connectivity and Hilbert-Based Features for Covert Speech EEG Variability Analysis and Classification

**Paper:** [Functional Connectivity and Hilbert-Based Features for Covert Speech EEG Variability Analysis and Classification](https://www.isca-archive.org/interspeech_2025/duraisamy25_interspeech.html)
**Taxonomy:** `sound-and-production / time-frequency-measurement / multi-resolution-signal`
**Evidence:** D3 full-paper capture; PDF SHA-256 `49e6f75cfe73490b95607f60ada962470a539739585aad48039c1bebf1fd724f`; full-text SHA-256 `e46fb1e6c797200a86625afb3e9f763ef3f2c6971b15a92c4dcb84c56ceca0d6`.

- **Ordinary problem:** A brain-computer interface may need to distinguish imagined or covert speech when no acoustic waveform is available.
- **Why it is hard:** EEG varies across trials, words, affective states, and people; phase and connectivity information can be lost when the signal is reduced to a single amplitude feature.
- **Naive attempt:** Train one subject-specific classifier on raw EEG and assume its spectral pattern transfers to another speaker.
- **Central move:** Represent covert speech with Hilbert envelopes, instantaneous phase, and functional connectivity across frequency bands, then train a subject-independent sequence classifier.
- **Mechanism:** Phase Locking Value and coherence summarize coordination among EEG channels. Band-specific Hilbert features feed a BiLSTM, while inter-trial, inter-class, and inter-subject analyses separate stable structure from variability.
- **Mathematical idea:** The features are functions of analytic-signal phase and amplitude; classification accuracy measures whether the learned representation separates five speech-command categories across subjects.
- **What the paper reports:** The reported subject-independent model reaches 59.14% accuracy across five covert-speech categories and reveals both shared and class-specific connectivity patterns.
- **Limits:** Covert speech EEG is not ordinary spoken audio, sample and subject variability constrain the result, class accuracy is not communicative utility, and no independent execution was performed.

## 392. Band-Split Self-supervised Mamba for Infant-centered Audio Analysis

**Paper:** [Band-Split Self-supervised Mamba for Infant-centered Audio Analysis](https://www.isca-archive.org/interspeech_2025/fan25_interspeech.html)
**Taxonomy:** `sound-and-production / time-frequency-measurement / multi-resolution-signal`
**Evidence:** D3 full-paper capture; PDF SHA-256 `b22901a6c5741f8bfd3a5f5b12e10378a50dcca93b2888867a7b9e7200a43acf`; full-text SHA-256 `78e96185bf8f6f63f6ab87474743567d95863c2a6bcbbecfa8c43f12c7be82f2`.

- **Ordinary problem:** Infant-worn recordings contain long, varied home soundscapes in which infant vocalizations and caregiver interaction must be recognized with little labeled data.
- **Why it is hard:** Events occupy different frequency bands and time scales, recordings are noisy and weakly annotated, and a single full-band representation can waste capacity on irrelevant variation.
- **Naive attempt:** Learn one monolithic audio embedding or train a supervised model only on the small labeled set.
- **Central move:** Split the spectrum into bands, learn band-specific projections, and let a band-agnostic Mamba encoder model temporal relations while self-supervised pretraining uses unlabeled in-domain audio.
- **Mechanism:** Band-specific features preserve local spectral evidence while the state-space sequence model carries information over time; self-supervised and supervised objectives share the representation before downstream classification.
- **Mathematical idea:** The system compares classification and representation-learning performance under limited labels, with band ablations testing whether multi-resolution structure matters.
- **What the paper reports:** BS-SSAMBA improves infant-centered audio analysis in the reported experiments and benefits from combining unlabeled in-domain audio with limited annotations.
- **Limits:** Infant audio is adjacent to, not identical with, human speech; task labels, home environments, class balance, and domain-specific data bound transfer to adult speech systems.

## 393. Evaluating Deep Speaker Embedding Robustness to Domain, Sampling Rate, and Codec Variations

**Paper:** [Evaluating Deep Speaker Embedding Robustness to Domain, Sampling Rate, and Codec Variations](https://www.isca-archive.org/interspeech_2025/ferrofilho25_interspeech.html)
**Taxonomy:** `sound-and-production / time-frequency-measurement / sampling-and-quantization`
**Evidence:** D3 full-paper capture; PDF SHA-256 `42eeb2d2925cb0b68f3552745644b3d9d17c8ae5c2ac6e61a3c0696b637995aa`; full-text SHA-256 `2fa4d3282ea35de4861f03520572fb3022b36da67254812796a1d1caecd176df`.

- **Ordinary problem:** A speaker-verification model should recognize a person after the recording device, room, sampling rate, or codec changes, because real deployments rarely match training conditions.
- **Why it is hard:** Those changes remove or distort high-frequency and channel cues that an embedding may have learned as part of identity, so a strong matched-condition score can hide brittle evidence.
- **Naive attempt:** Train on one clean domain and treat later degradation as unavoidable noise, or compare models only at the training sampling rate and codec.
- **Central move:** Stress several embedding models across far-field, noise, music, sampling-rate, and compression shifts and measure how much verification performance moves.
- **Mechanism:** The study evaluates ECAPA-TDNN, TitaNet, ECAPA2, and ReDimNet on domain, sampling-rate, and codec variations, including far-field speech, noise, and music interference.
- **Mathematical idea:** Verification is a threshold decision on similarity between two embeddings; the experiment changes the recording path while holding the speaker task fixed, revealing which cues are not stable identity evidence.
- **What the paper reports:** All models degrade under mismatched domains; ReDimNet degrades least in the tested settings, while downsampling and low-bitrate compression further hurt performance and expose reliance on high-frequency information.
- **Limits:** Datasets, codecs, sampling rates, threshold calibration, and attack/evaluation protocol bound the result; robustness to these shifts does not imply fairness or security against adaptive attacks.

## 394. Echoes of Phonetics:  Unveiling Relevant Acoustic Cues for ASR via Feature Attribution

**Paper:** [Echoes of Phonetics:  Unveiling Relevant Acoustic Cues for ASR via Feature Attribution](https://www.isca-archive.org/interspeech_2025/fucci25_interspeech.html)
**Taxonomy:** `sound-and-production / time-frequency-measurement / windowed-spectrum`
**Evidence:** D3 full-paper capture; PDF SHA-256 `749d3bc40e5a37911b46cad80e20ff1dd250e2a87523526cedd81b592758f18c`; full-text SHA-256 `fad4256fc895922b8468b1d7fb429b0dcaf5fb0bd4185d1cbec4742c4d416322`.

- **Ordinary problem:** An ASR model can produce a word correctly without revealing which parts of the sound it used, making it difficult to tell whether its evidence resembles human phonetic cues or a shortcut.
- **Why it is hard:** Modern models combine time and frequency evidence across many layers, and attribution methods can be unstable or difficult to interpret without a phonetic reference.
- **Naive attempt:** Report only the word error rate or inspect a few hand-picked phonemes and assume the model uses the same cues as listeners.
- **Central move:** Apply feature attribution across plosives, fricatives, and vowels and compare the highlighted regions with known acoustic events in time and frequency.
- **Mechanism:** The study analyzes a modern Conformer ASR system, identifying attribution patterns for vowels, sibilant/non-sibilant fricatives, and plosives including release bursts and formants.
- **Mathematical idea:** Attribution maps assign output sensitivity to time-frequency regions; comparison with acoustic structure tests whether the model's evidence aligns with a physical explanation rather than merely correlating with the label.
- **What the paper reports:** The paper reports that the model uses full vowel spans and especially the first two formants, captures sibilant spectra more strongly, and emphasizes plosive release/burst cues, with differences by speaker sex.
- **Limits:** Attribution method, baseline model, phoneme set, speaker distribution, and interpretation assumptions bound the result; saliency is evidence of sensitivity, not a causal proof that the model listens as a human does.

## 395. Leveraging AM and FM Rhythm Spectrograms for Dementia Classification and Assessment

**Paper:** [Leveraging AM and FM Rhythm Spectrograms for Dementia Classification and Assessment](https://www.isca-archive.org/interspeech_2025/gogoi25_interspeech.html)
**Taxonomy:** `sound-and-production / time-frequency-measurement / multi-resolution-signal`
**Evidence:** D3 full-paper capture; PDF SHA-256 `1c923b4ab7f5326abb9ce89d4baedc72b6accf41838364c0a8883628155b8b83`; full-text SHA-256 `85669588cd56bea22d8ee8052fa7c390c0354b0711d69a5ec35a360c1b82d1fc`.

- **Ordinary problem:** Dementia-related speech changes can unfold over long time scales in rhythm and coordination, so a short spectral snapshot may miss the signal clinicians or researchers need.
- **Why it is hard:** Long speech mixes linguistic content, speaker differences, pauses, and rhythm; handcrafted acoustic features may miss long modulation patterns while a large multimodal model may be hard to interpret.
- **Naive attempt:** Use standard short-window spectral features or treat every long recording as one undifferentiated waveform.
- **Central move:** Represent amplitude and frequency modulation rhythms as spectrograms, compare interpretable handcrafted summaries with a learned fusion of acoustic and linguistic representations.
- **Mechanism:** The study derives Rhythm Formant Analysis AM/FM spectrograms, tests handcrafted features and a ViT-plus-BERT fusion for dementia classification and regression, and compares against eGeMAPs and Mel spectrograms.
- **Mathematical idea:** The representation changes the time scale of measurement: modulation patterns become visible as structured images, while classification and regression test whether they carry diagnostic information.
- **What the paper reports:** The paper reports a 14.2% relative classification-accuracy improvement over eGeMAPs for handcrafted features and further gains when rhythm spectrograms are fused with linguistic and acoustic models.
- **Limits:** Corpus, labels, recording length, disease definition, model fusion, and accuracy/regression metrics bound the result; an acoustic association is not a clinical diagnosis or causal mechanism.

## 396. A Data-Driven Diffusion-based Approach for Audio Deepfake Explanations

**Paper:** [A Data-Driven Diffusion-based Approach for Audio Deepfake Explanations](https://www.isca-archive.org/interspeech_2025/grinberg25_interspeech.html)
**Taxonomy:** `sound-and-production / time-frequency-measurement / windowed-spectrum`
**Evidence:** D3 full-paper capture; PDF SHA-256 `4c8a385770411bf08598e5c79f6470059fd72fcedf609f88dc9de12ae6950ed6`; full-text SHA-256 `9ba418c39a5e266f97f4dfca2bbac05947e27c85696f82d6463050d85e00343a`.

- **Ordinary problem:** Audio deepfake explanations should show which changing acoustic evidence led to a detector's decision.
- **Why it is hard:** A global score hides local spectral events and can appear interpretable without exposing evidence.
- **Naive attempt:** Point to an arbitrary waveform segment or global saliency map and call it an explanation.
- **Central move:** Relate detector decisions to localized time-frequency structure with a data-driven explanation model.
- **Mechanism:** A spectro-temporal explanation connects model output to changing acoustic regions.
- **Mathematical idea:** The relevant object is the windowed-spectrum evidence described by the paper's mechanism: A spectro-temporal explanation connects model output to changing acoustic regions.
- **What the paper reports:** The paper reports a diffusion approach for explaining neural audio deepfake decisions.
- **Limits:** Deepfake types, explanation faithfulness, model family, and listener interpretation bound transfer.

## 397. Extended High-frequency Cues to Phoneme Recognition: Insights from ASR

**Paper:** [Extended High-frequency Cues to Phoneme Recognition: Insights from ASR](https://www.isca-archive.org/interspeech_2025/guo25b_interspeech.html)
**Taxonomy:** `sound-and-production / time-frequency-measurement / multi-resolution-signal`
**Evidence:** D3 full-paper capture; PDF SHA-256 `e1e86ca88d7d94a3128474376cd8c301249a5cc7f2084765f0abaf22671fd3cf`; full-text SHA-256 `a7ffaa8ba82371e6054a111466293fb49817995d9c512856a863e56c8bae7e5c`.

- **Ordinary problem:** Speech in noise may depend on acoustic information above the frequency range normally used by speech systems.
- **Why it is hard:** High-frequency cues can be masked, and an ASR result does not automatically explain why a human listener benefits from them.
- **Naive attempt:** Discard everything above 6–8 kHz because it is assumed irrelevant to phonemes.
- **Central move:** Use a phoneme recognizer as a controlled probe of which frequency bands help under masking and spatial separation.
- **Mechanism:** A neural network decodes phonemes from cochleagrams of broadband, 8-kHz-low-pass, and 6-kHz-low-pass speech under quiet and masked conditions.
- **Mathematical idea:** Recognition accuracy and phoneme-omission probabilities are compared across target-to-masker ratios, filtering conditions, and consonant/vowel classes.
- **What the paper reports:** Broadband speech improves phoneme accuracy in masked conditions, especially at lower TMR, while adding no quiet-condition benefit; removing extended high frequencies increases consonant omissions.
- **Limits:** VCTK speech, selected maskers, cochleagram assumptions, and a model-based probe bound the conclusion; audiological benefit and general ASR deployment are not established.

## 398. Low Complex IIR Adaptive Hear-Through Ambient Filtering for Overcoming Practical Constraints in Earbuds

**Paper:** [Low Complex IIR Adaptive Hear-Through Ambient Filtering for Overcoming Practical Constraints in Earbuds](https://www.isca-archive.org/interspeech_2025/gupta25_interspeech.html)
**Taxonomy:** `sound-and-production / time-frequency-measurement / multi-resolution-signal`
**Evidence:** D3 full-paper capture; PDF SHA-256 `6c36ac07027d357e63eda74ebda7b1cf108eddfd46f045e7446e2318ebd885a3`; full-text SHA-256 `f7385048f66a09a310f477284fdc0f902150089eadc0bc4c4868357116cc92df`.

- **Ordinary problem:** An earbud should make outside speech, horns, and alarms sound as if the ear were open, despite passive attenuation and changing fit or source direction.
- **Why it is hard:** The filter must compensate a user- and direction-dependent acoustic path with low delay, while adaptive IIR filters can become unstable and FIR filters can be expensive.
- **Naive attempt:** Use one fixed equalizer or a high-order adaptive FIR and accept mismatch, computation, or latency.
- **Central move:** Estimate a virtual sensing path and adapt a low-complexity IIR hear-through filter with stability-aware updates for different earbud fittings and directions.
- **Mechanism:** The virtual sensor models the sound pressure at the eardrum; an adaptive IIR filter updates the feedforward path, while constraints on poles/coefficients prevent unstable compensation. Indoor and outdoor acoustic simulations test convergence and delay.
- **Mathematical idea:** Mean-square error, SNR, filter complexity, and processing delay expose the trade-off between matching the open-ear response and maintaining real-time stability.
- **What the paper reports:** The proposed low-complexity IIR method reports improved hear-through performance under practical constraints and reduced complexity relative to larger adaptive alternatives.
- **Limits:** The evidence is simulation-heavy and depends on acoustic-path and fitting assumptions; user listening, hardware latency, and individualized hearing benefit are not established.

## 399. Relationship between objective and subjective perceptual measures of speech in individuals with head and neck cancer

**Paper:** [Relationship between objective and subjective perceptual measures of speech in individuals with head and neck cancer](https://www.isca-archive.org/interspeech_2025/halpern25_interspeech.html)
**Taxonomy:** `sound-and-production / time-frequency-measurement / multi-resolution-signal`
**Evidence:** D3 full-paper capture; PDF SHA-256 `d669e9c5c2abd6b674c3c898cc8798103f979f59b68063abb4fab78bd47f3e24`; full-text SHA-256 `710914fea6f33f1bffb7aa343334186d8812a6db056da7198110f52fa922536c`.

- **Ordinary problem:** Clinical speech monitoring needs measurements that are repeatable yet still mean what listeners experience as intelligibility, articulation, or voice quality.
- **Why it is hard:** Subjective ratings are expensive and variable, while objective acoustic measures can correlate with a broad severity factor rather than the specific speech dimension they claim to measure.
- **Naive attempt:** Validate one objective metric against one listener rating and treat a high correlation as proof that the metric isolates that percept.
- **Central move:** Measure several perceptual dimensions and objective proxies in longitudinal head-and-neck-cancer speech, then inspect their correlation structure for common-cause confounding.
- **Mechanism:** Trained listeners rate intelligibility, articulation, voice quality, phonation, rate, nasality, and noise; objective measures such as NAD, PCX, PER, SPEED, and SNR are compared using Pearson correlations across 53 Dutch participants.
- **Mathematical idea:** The study treats Pearson r as alignment between a computational proxy and a perceptual target, but interprets correlated targets cautiously because shared treatment severity can induce multiple correlations.
- **What the paper reports:** Subjective intelligibility correlates strongly with articulation (r=.95) and voice quality (r=.92); NAD correlates .90 with intelligibility, while phonation and nasality lack reliable objective counterparts in this cohort.
- **Limits:** The population is Dutch readers with head-and-neck cancer, not general speech; neural features are not fully interpretable, running spontaneous speech is absent, and correlation does not prove clinical decision validity.

## 400. LSPnet: an ultra-low bitrate hybrid neural codec

**Paper:** [LSPnet: an ultra-low bitrate hybrid neural codec](https://www.isca-archive.org/interspeech_2025/zhang25l_interspeech.html)
**Taxonomy:** `sound-and-production / time-frequency-measurement / sampling-and-quantization`
**Evidence:** D3 full-paper capture; PDF SHA-256 `789f0e8890cb4177347bdf62eb0cc9afaba6357923251ce02426f681d60219d4`; full-text SHA-256 `587275d851b7c2599e9bd0ed35f644e72f7424a59a14bdbd9f925c2548d90fbe`.

- **Ordinary problem:** A 1.2 kbps speech codec should preserve intelligibility and quality under resource constraints.
- **Why it is hard:** Very-low-rate coding must preserve spectral envelope and waveform detail while avoiding the complexity of large end-to-end decoders.
- **Naive attempt:** Quantize conventional parameters more aggressively or use a high-quality neural codec whose compute and bitrate exceed the deployment budget.
- **Central move:** Combine LSP-based parametric coding, direct neural sample prediction, and joint STFT/cross-entropy training in a hybrid LPCNet-style codec.
- **Mechanism:** LSPs stabilize spectral-envelope quantization; the neural predictor models sample distributions; time-frequency losses jointly constrain local waveform and spectral behavior.
- **Mathematical idea:** Codec design is a rate-distortion allocation across representations and resolutions, with complexity treated as a deployment constraint.
- **What the paper reports:** The paper reports high speech quality at 1.2 kbps and lower complexity than compared end-to-end codecs.
- **Limits:** Datasets, bitrate, codec baselines, quality metrics, hardware, and real-time implementation bound transfer; reported quality is not proof for every channel or listener.

## 401. Non-Standard Accent TTS Support via Large Multi-Accent Frontend Pronunciation Knowledge Transfer

**Paper:** [Non-Standard Accent TTS Support via Large Multi-Accent Frontend Pronunciation Knowledge Transfer](https://www.isca-archive.org/interspeech_2025/berger25_interspeech.html)
**Taxonomy:** `voice-generation-and-control / content-planning / text-to-speech-planning`
**Evidence:** D3 full-paper capture; PDF SHA-256 `a18532251ba2a28fabd6badc002e3a23d6a5062e85e56a0e194c2098dc002140`; full-text SHA-256 `bf0934d87b002d0bc31bba92f0838d348613cf7b6e1a5dbc2d5bcfd791951056`.

- **Ordinary problem:** A text-to-speech system should pronounce an accent it has barely seen without requiring a large new pronunciation database.
- **Why it is hard:** Pronunciation frontend errors occur before waveform generation and are costly to label for every accent.
- **Naive attempt:** Train a separate full-size pronunciation model for every target accent.
- **Central move:** Transfer pronunciation knowledge from a large multi-accent frontend and measure how much target-accent data is needed as source accents vary in similarity.
- **Mechanism:** The frontend predicts phones, lexical stress, and prosodic boundaries; target accents are trained with reduced data and compared with full-data and single-accent baselines.
- **Mathematical idea:** Accent similarity becomes a data-selection variable: transfer is not merely shared representation, but choosing a source whose pronunciation structure is useful for the target.
- **What the paper reports:** The paper reports up to 95% less pronunciation training data for robust performance and examines 14 English accents using LibriTTS and HiFi-TTS-derived data.
- **Limits:** Accuracy is reported for the studied accents, frontend labels, and datasets; transfer to other languages, voices, and synthesis backends remains unestablished.

## 402. Accelerating Diffusion-based Text-to-Speech Model Trainingwith Dual Modality Alignment

**Paper:** [Accelerating Diffusion-based Text-to-Speech Model Trainingwith Dual Modality Alignment](https://www.isca-archive.org/interspeech_2025/choi25c_interspeech.html)
**Taxonomy:** `voice-generation-and-control / content-planning / text-to-speech-planning`
**Evidence:** D3 full-paper capture; PDF SHA-256 `59011c57b9ace950c1f297f967cde43fb896837b18c6141f6787ba71c0f2a5ab`; full-text SHA-256 `4a155f06d0aaa86e840dc38c1aeb20e1fd6b137e96e6caf559f77ec15bef4c35`.

- **Ordinary problem:** A text-to-speech system should reach good quality without spending excessive computation learning every intermediate diffusion state.
- **Why it is hard:** Diffusion models learn a long sequence of noisy-to-clean transformations, and the text and speech views contain different information about the target.
- **Naive attempt:** Train the diffusion model longer or add more capacity without teaching it what text and speech already agree on.
- **Central move:** Align hidden states using both text-guided and speech-guided objectives so the diffusion process starts with more useful semantic structure.
- **Mechanism:** A-DMA aligns contextual text representations and discriminative speech features during diffusion TTS training, then compares convergence and synthesis quality with baselines.
- **Mathematical idea:** Alignment reduces the mismatch between two representations before the generative process; convergence speed and output quality are separate objectives.
- **What the paper reports:** The paper reports doubled convergence speed with better performance than its baselines.
- **Limits:** The text/speech encoders, datasets, diffusion schedule, and quality measures bound the claim; hardware cost and new languages remain open.

## 403. Scheduled Interleaved Speech-Text Training for Speech-to-Speech Translation with LLMs

**Paper:** [Scheduled Interleaved Speech-Text Training for Speech-to-Speech Translation with LLMs](https://www.isca-archive.org/interspeech_2025/futami25_interspeech.html)
**Taxonomy:** `voice-generation-and-control / content-planning / text-to-speech-planning`
**Evidence:** D3 full-paper capture; PDF SHA-256 `26eb613db71dd3656f2fb2b600aca0598348727e5f8ace5573099a69c1518587`; full-text SHA-256 `af0a636a763455714a3e5d443ff06635eeffaa0e5359b64dc4d210efae4a1e05`.

- **Ordinary problem:** A speech-to-speech translator should inherit text-trained language knowledge without needing a huge paired speech-to-speech corpus.
- **Why it is hard:** Text-only LLMs know language patterns but not how discrete speech units carry them, and limited paired data makes direct adaptation unstable.
- **Naive attempt:** Fine-tune directly on speech units and expect the text model to discover the modality bridge.
- **Central move:** Interleave aligned text and speech units during training, then gradually reduce the text proportion so the model moves toward speech output.
- **Mechanism:** LLaMA3.2-1B is fine-tuned on CVSS with scheduled interleaving and evaluated across translation directions and resource levels.
- **Mathematical idea:** The schedule is a curriculum over modalities: text provides a stable scaffold early, while speech units become responsible later; translation quality measures the endpoint.
- **What the paper reports:** The paper reports consistent translation improvements, especially in limited-data languages.
- **Limits:** CVSS, unitizer, schedule, model size, and languages bound the result; naturalness, speaker identity, and unseen domains need separate tests.

## 404. Code Mix TTS: An Approach to Infer Human Like Speech for Multi-Lingual Input Texts

**Paper:** [Code Mix TTS: An Approach to Infer Human Like Speech for Multi-Lingual Input Texts](https://www.isca-archive.org/interspeech_2025/gourav25_interspeech.html)
**Taxonomy:** `voice-generation-and-control / content-planning / text-to-speech-planning`
**Evidence:** D3 full-paper capture; PDF SHA-256 `13396297a5acb2acb644562e7cd94e578ae6bf713859b56644c8d68b6952ac35`; full-text SHA-256 `d134b8fcd0e84929df98b00dfa2a1fa9ef99f70ec79bb4b8dd0f338aa6bed9eb`.

- **Ordinary problem:** A text-to-speech system should sound natural when a speaker mixes languages in one utterance, as people commonly do in multilingual communities.
- **Why it is hard:** Monolingual training assumptions make language switches, pronunciation, and voice continuity brittle.
- **Naive attempt:** Force the input into one language or fine-tune on a new code-mixed dataset.
- **Central move:** Infer code-mixed speech from multilingual text without requiring additional training data or fine-tuning.
- **Mechanism:** The proposed inference procedure sends multilingual input through an existing TTS system and evaluates generated code-mixed speech with automated MOS-style measures.
- **Mathematical idea:** The central tradeoff is whether language-switch content is retained while synthesized audio remains natural; the paper uses automated quality scoring rather than a new training loss.
- **What the paper reports:** The paper reports an approach for code-mix inference without extra data or fine-tuning; the preserved evidence does not establish broad human preference gains.
- **Limits:** The paper's method and evaluation details are bounded by the selected TTS system, languages, and automated metric; human listening, pronunciation accuracy, and unseen language pairs remain open.

## 405. Analyzing Mitigation Strategies for Catastrophic Forgetting in End-to-End Training of Spoken Language Models

**Paper:** [Analyzing Mitigation Strategies for Catastrophic Forgetting in End-to-End Training of Spoken Language Models](https://www.isca-archive.org/interspeech_2025/hsiao25_interspeech.html)
**Taxonomy:** `voice-generation-and-control / content-planning / text-to-speech-planning`
**Evidence:** D3 full-paper capture; PDF SHA-256 `bd40916921226ab2dc9c802c492c341f48247218b54a991aa7d6004d47f2e43c`; full-text SHA-256 `fe4703ba002861000eea76043cb950ee999f1259f255a85ddd8f47c71fdbb554`.

- **Ordinary problem:** A spoken-language model trained end to end may learn new tasks while forgetting how to perform tasks it already knew.
- **Why it is hard:** Speech, text, vocabulary, and task behavior are updated together; reducing forgetting can also reduce learning of the new objective or distort the shared representation.
- **Naive attempt:** Train only on the new data, freeze everything, or assume a larger model automatically retains old abilities.
- **Central move:** Compare mitigation strategies for catastrophic forgetting during end-to-end spoken-language-model training, including how data and parameter updates are controlled.
- **Mechanism:** The study evaluates forgetting-mitigation strategies for end-to-end training of spoken language models.
- **Mathematical idea:** The core tradeoff is retention versus adaptation: an update is useful only if it improves the new task without erasing previously learned speech-language behavior.
- **What the paper reports:** The paper reports comparative forgetting and adaptation results across the tested strategies.
- **Limits:** Tasks, training order, model size, data mixture, and retention metrics bound the conclusions; results do not establish lifelong learning in open deployment.

## 406. Revival with Voice: Multi-modal Controllable Text-to-Speech Synthesis

**Paper:** [Revival with Voice: Multi-modal Controllable Text-to-Speech Synthesis](https://www.isca-archive.org/interspeech_2025/kim25b_interspeech.html)
**Taxonomy:** `voice-generation-and-control / content-planning / text-to-speech-planning`
**Evidence:** D3 full-paper capture; PDF SHA-256 `994d49fd833d6f6c34ea4ee1fb9ca22be60812df334d63bbd7c636d665c5d432`; full-text SHA-256 `c48150ab1e3f50d7dabc9abd6df30aa3f75bf4f5f4e1922246509ba57cf65b73`.

- **Ordinary problem:** A controllable TTS system should synthesize a plausible voice from a face image and obey natural-language descriptions of speaking style and acoustic conditions.
- **Why it is hard:** Face-driven corpora are limited in audio quality, artistic portraits differ from real faces, and controls such as pace, distance, tone, and noise interact rather than forming independent knobs.
- **Naive attempt:** Train only on paired face-audio data and expose separate hand-tuned controls that do not generalize beyond the training corpus.
- **Central move:** Augment face-driven training with high-quality audio-only speech, stylize face inputs to cover artistic portraits, and condition synthesis on natural-language control descriptions.
- **Mechanism:** The face encoder supplies speaker or voice information, while text conditioning specifies controllable attributes; multi-modal training aligns these conditions with waveform generation.
- **Mathematical idea:** The system treats identity and controllable acoustic attributes as separate but compositional conditioning variables, evaluated through speech quality, similarity, and control-following tests.
- **What the paper reports:** Revival with Voice reports controllable synthesis from real and artistic face inputs and improved use of high-quality audio-only data in the tested settings.
- **Limits:** Face distribution, language, control wording, subjective protocol, and disentanglement assumptions limit the claim; controllability is not proof of identity fidelity or safe use of a person's likeness.

## 407. Long-Context Speech Synthesis with Context-Aware Memory

**Paper:** [Long-Context Speech Synthesis with Context-Aware Memory](https://www.isca-archive.org/interspeech_2025/li25b_interspeech.html)
**Taxonomy:** `voice-generation-and-control / content-planning / text-to-speech-planning`
**Evidence:** D3 full-paper capture; PDF SHA-256 `97438ad5c1a18c56baeda5dc30db4cc893795f61d35e8ba37e6a6ed1a4613469`; full-text SHA-256 `c7472b42f6ee0c6976e9bd834141fc9405e5ec012fdc38514c96d44008cb0cda`.

- **Ordinary problem:** Long-form speech should sound like one coherent reading rather than a row of independently synthesized sentences with changing style and voice.
- **Why it is hard:** Paragraph context affects prosody and discourse emphasis, but autoregressive context is expensive and sentence concatenation loses information across boundaries.
- **Naive attempt:** Synthesize each sentence independently and concatenate the waveforms, or attend to the entire paragraph without controlling the generation cost.
- **Central move:** Maintain long-term and local context in a dynamic memory and use a prefix mask to provide bidirectional context to sentence-level synthesis while keeping generation causal.
- **Mechanism:** The context-aware memory retrieves and updates paragraph information; local details and long-term style guide each sentence, while prefix tokens supply in-context information without unrestricted future leakage.
- **Mathematical idea:** The system separates memory access from waveform generation, trading a bounded context representation for coherence and lower context-inference cost.
- **What the paper reports:** The model outperforms the reported baselines on paragraph-level prosody expressiveness, coherence, and context-inference cost.
- **Limits:** Text genre, speaker/style conditioning, subjective measures, memory capacity, and paragraph length bound transfer; coherence scores do not prove human preference in broad long-form use.

## 408. SpeechSEC: A Unified Multi-Task Framework for Speech Synthesis, Editing, and Continuation

**Paper:** [SpeechSEC: A Unified Multi-Task Framework for Speech Synthesis, Editing, and Continuation](https://www.isca-archive.org/interspeech_2025/liang25e_interspeech.html)
**Taxonomy:** `voice-generation-and-control / content-planning / text-to-speech-planning`
**Evidence:** D3 full-paper capture; PDF SHA-256 `fefa100f9bc6c3c6a5d0926cc4b00338052c41dd852db336cebaecf24de6b849`; full-text SHA-256 `3b459f9bc55445d54d98f081809765c74e2457fd5cec855fa2f3f5b79dbd6c2b`.

- **Ordinary problem:** One speech model should support synthesis, editing, and continuation while preserving voice and acoustic continuity across the operation.
- **Why it is hard:** Separate task-specific models duplicate knowledge, and acoustic tokens contain internal relationships that a simple semantic-to-acoustic mapping can discard.
- **Naive attempt:** Train independent systems for synthesis, editing, and continuation or map semantic tokens to acoustic tokens without modeling acoustic context.
- **Central move:** Use a unified non-autoregressive framework whose input conditions select synthesis, editing, or continuation, while shared training captures common acoustic structure.
- **Mechanism:** The model dynamically changes conditioning for each task and remains compatible with multiple speech discretizers such as HuBERT, DAC, and SpeechTokenizer.
- **Mathematical idea:** A shared representation is treated as a reusable coordinate system for several transformations; voice preservation and audio quality test whether task sharing retains the right invariants.
- **What the paper reports:** SpeechSEC reports MOS-like audio quality of 4.20 versus 4.00 and voice preservation of 0.72 versus 0.58 for synthesis, with usable editing and continuation results.
- **Limits:** Reported scores, codec choice, task mixture, prompts, speakers, and sample protocol bound the comparison; multi-task compatibility is not proof of editing safety or continuity in arbitrary audio.

## 409. Improving Noise Robustness of LLM-based Zero-shot TTS via Discrete Acoustic Token Denoising

**Paper:** [Improving Noise Robustness of LLM-based Zero-shot TTS via Discrete Acoustic Token Denoising](https://www.isca-archive.org/interspeech_2025/lu25b_interspeech.html)
**Taxonomy:** `voice-generation-and-control / content-planning / text-to-speech-planning`
**Evidence:** D3 full-paper capture; PDF SHA-256 `e57916bc48423e54ff4b5ad9e960bc5877ca74f220bf3670e2b57039a7d7d805`; full-text SHA-256 `42f1a2c92b318f182093175b1942feea058ee5699598fe434b9533c24d1cc415`.

- **Ordinary problem:** Zero-shot TTS should preserve a speaker’s identity when the few-second audio prompt is noisy.
- **Why it is hard:** Noise corrupts acoustic tokens and can cause an LLM-based TTS system to copy the environment or plan the wrong voice, while ordinary enhancement may not match token-level prompts.
- **Naive attempt:** Enhance the prompt with a generic speech enhancer or trust the noisy codec tokens as if they represented clean speaker evidence.
- **Central move:** Denoise the first acoustic-token groups with a neural codec token predictor, refine the embedding, and use the cleaned prompt in LauraTTS.
- **Mechanism:** The token denoiser predicts clean coarse tokens; an embedding refiner and codec decoder reconstruct usable acoustic evidence before the zero-shot TTS model conditions generation.
- **Mathematical idea:** Denoising at the representation used for prompting aligns the cleanup objective with the generator’s actual conditioning interface.
- **What the paper reports:** The paper reports that its codec denoiser outperforms speech-enhancement baselines and that noise-robust LauraTTS improves over adding an external enhancer.
- **Limits:** Noise types, prompt duration, speaker overlap, codec/model version, and zero-shot evaluation bound transfer; clean synthesis from a prompt is not speaker-authenticated identity preservation.

## 410. Tungnaá In Live Performance: An Implementation Of Interactive Artistic Text-To-Voice

**Paper:** [Tungnaá In Live Performance: An Implementation Of Interactive Artistic Text-To-Voice](https://www.isca-archive.org/interspeech_2025/shepardson25_interspeech.html)
**Taxonomy:** `voice-generation-and-control / content-planning / text-to-speech-planning`
**Evidence:** D3 full-paper capture; PDF SHA-256 `e627d0172aba23d335caba0da949429fb585d1ea3922b2664f08b4bd66301fc1`; full-text SHA-256 `0ea5e405f36b101bc1303f987e3bce9c1a5e454328a04bfd68b5a9c0be764f8d`.

- **Ordinary problem:** A performer needs text-conditioned voice generation that responds in real time, can be trained from a small bespoke corpus, and remains musically controllable.
- **Why it is hard:** Performance demands low worst-case latency and expressive interaction, while ordinary TTS assumes large data, fixed text, and offline generation.
- **Naive attempt:** Use a conventional TTS stack and optimize average throughput, even if buffering and model assumptions make live interaction brittle.
- **Central move:** Define interactive artistic text-to-voice around a reduced-phonetic-alphabet dataset, streaming vocoder, bounded look-ahead, and a GUI that exposes live controls.
- **Mechanism:** The system separates alignment/generation into streaming components, buffers a small number of frames to trade latency for stability, and keeps the interface in a separate process.
- **Mathematical idea:** Deployment constraints become part of the speech representation and evaluation: latency, controllability, and small-data adaptation matter alongside audio quality.
- **What the paper reports:** The demonstration reports real-time inference with worst-case latency below 100 ms and a bespoke performance dataset/application.
- **Limits:** Demonstration scope, artist-specific data, reduced phonetic alphabet, hardware, subjective quality, and no controlled comparison bound generalization; live usability is not a standard TTS benchmark.

## 411. Finding the Human Voice in AI: Insights on the Perception of AI-Voice Clones from Naturalness and Similarity Ratings

**Paper:** [Finding the Human Voice in AI: Insights on the Perception of AI-Voice Clones from Naturalness and Similarity Ratings](https://www.isca-archive.org/interspeech_2025/bakkouche25_interspeech.html)
**Taxonomy:** `voice-generation-and-control / expression-and-interactive-control / style-and-emotion-control`
**Evidence:** D3 full-paper capture; PDF SHA-256 `d310d8a5207ca7d661401a38f2265a93b1cdd8585901ded03b02974a4c1b3f31`; full-text SHA-256 `7d98a7ca4e81352ec6521fa4f61288e10830fa746cb6e70d3b0943877ad4bd9c`.

- **Ordinary problem:** Determine whether a generated voice sounds like a person and whether listeners experience it as naturally spoken.
- **Why it is hard:** Identity similarity and naturalness can move separately: a clone may resemble the target but sound stiff, or sound natural while losing the target's identity and prosody.
- **Naive attempt:** Use one similarity score or a signal metric as if it represented all aspects of a human voice clone.
- **Central move:** Collect separate listener judgments of naturalness and similarity and examine which prosodic properties, including dynamic pitch variation, explain the gap.
- **Mechanism:** Listeners hear natural and generated samples, rate distinct targets, and the analysis relates ratings to acoustic/prosodic differences rather than collapsing them into one number.
- **Mathematical idea:** Ratings are treated as separate subjective measurements; comparisons of pitch movement and other prosodic features test association, not a causal guarantee that one feature determines perception.
- **What the paper reports:** The paper reports that AI voice clones struggle with dynamic F0 variation and analyzes its relationship to naturalness and similarity ratings.
- **Limits:** Listener population, prompts, voices, and rating protocol limit generalization; perceptual association does not establish that changing F0 alone fixes naturalness. No independent reproduction was performed.

## 412. Fine-Tuning Text-to-Speech Diffusion Models Using Reinforcement Learning with Human Feedback

**Paper:** [Fine-Tuning Text-to-Speech Diffusion Models Using Reinforcement Learning with Human Feedback](https://www.isca-archive.org/interspeech_2025/chen25b_interspeech.html)
**Taxonomy:** `voice-generation-and-control / expression-and-interactive-control / style-and-emotion-control`
**Evidence:** D3 full-paper capture; PDF SHA-256 `32f1a2b6134b046d4cec5e67e60a0b63d8909feea4814af53d4c55930256276b`; full-text SHA-256 `34e8e10a06efb25bcf04214982bf9938b71ac59f12638f3c1e11eb703282968c`.

- **Ordinary problem:** TTS must sound natural and intelligible while responding quickly enough for real use; diffusion refinement makes that balance difficult.
- **Why it is hard:** Maximizing a learned naturalness reward can move the generator away from the distribution learned during diffusion training.
- **Naive attempt:** Maximize perceptual reward alone, or keep the original loss and accept the quality-speed tradeoff.
- **Central move:** Use the diffusion loss as a regularizer inside policy optimization so naturalness improvement remains tied to learned speech structure.
- **Mechanism:** DLPO fine-tunes WaveGrad 2 with a reward combining UTMOS naturalness and the original diffusion loss, comparing DPOK, KLinR, and diffusion-only optimization.
- **Mathematical idea:** DLPO reports UTMOS 3.65, NISQA 4.02, WER 1.0%, and 67% pairwise preference; these are different proxies, not one quality axis.
- **What the paper reports:** The paper reports gains over the baseline and competing reward objectives, with listeners preferring samples 67% of the time.
- **Limits:** The evidence uses WaveGrad 2 and selected reward predictors; predicted metrics and pairwise preference do not establish broad real-time deployment.

## 413. DiEmo-TTS: Disentangled Emotion Representations via Self-Supervised Distillation for Cross-Speaker Emotion Transfer in Text-to-Speech

**Paper:** [DiEmo-TTS: Disentangled Emotion Representations via Self-Supervised Distillation for Cross-Speaker Emotion Transfer in Text-to-Speech](https://www.isca-archive.org/interspeech_2025/cho25b_interspeech.html)
**Taxonomy:** `voice-generation-and-control / expression-and-interactive-control / style-and-emotion-control`
**Evidence:** D3 full-paper capture; PDF SHA-256 `9e8c77e96d0aa8a71a863a99b654f78b3375a77bc58a1c1a9180287ade069bd6`; full-text SHA-256 `4abbd1795d8064c164485b6b398f01ca13650424f6fb679fc50394ee530d253b`.

- **Ordinary problem:** Emotion transfer should change delivery without replacing the target speaker's identity.
- **Why it is hard:** Emotion and timbre are entangled, so an emotion embedding can leak the reference speaker.
- **Naive attempt:** Copy speaker and emotion embeddings into TTS without testing information leakage.
- **Central move:** Distill speaker-independent emotion representations with cluster sampling, perturbation, and separate style/identity conditioning.
- **Mechanism:** DiEmo-TTS clusters emotion attributes, matches speaker/emotion examples, distills representations, and uses a dual-conditioning transformer.
- **Mathematical idea:** Naturalness, speaker similarity, emotion similarity, WER/CER, and embedding scores measure different goals; ablations remove distillation components.
- **What the paper reports:** The reported system improves emotion and speaker-related measures in the chosen experiments.
- **Limits:** Pretrained encoders, datasets, subjective measures, and cross-speaker coverage bound the conclusion.

## 414. VibE-SVC: Vibrato Extraction with High-frequency F0 Contour for Singing Voice Conversion

**Paper:** [VibE-SVC: Vibrato Extraction with High-frequency F0 Contour for Singing Voice Conversion](https://www.isca-archive.org/interspeech_2025/choi25e_interspeech.html)
**Taxonomy:** `voice-generation-and-control / expression-and-interactive-control / prosody-control`
**Evidence:** D3 full-paper capture; PDF SHA-256 `453ae8c915b076539864a14d364b60a6162dc333e728f8de03b3f831dc4e241d`; full-text SHA-256 `a2ffe24fb3a91483170ed6f69a9d60e7545473854fe06f70736b2b977e265bc2`.

- **Ordinary problem:** A singing voice converter should transfer vibrato deliberately because vibrato carries style and emotion, but it must preserve the singer's identity and the song's content.
- **Why it is hard:** Vibrato is a fast variation within the fundamental-frequency contour, so treating it as undifferentiated pitch can make it hard to extract or control.
- **Naive attempt:** Leave vibrato entangled in the pitch representation or control it with a single average F0 value.
- **Central move:** Separate high-frequency F0 variation with a wavelet transform, then explicitly transfer and control the vibrato component during conversion.
- **Mechanism:** VibE-SVC extracts vibrato from the high-frequency F0 contour for controllable singing voice conversion.
- **Mathematical idea:** Style becomes an editable signal component: the system changes a time-varying pitch pattern while preserving the slower melody and speaker identity.
- **What the paper reports:** The paper reports objective and subjective evidence for high-quality conversion, style control, and speaker similarity.
- **Limits:** Singers, songs, vibrato ranges, extraction errors, and evaluation conditions limit generalization; explicit control does not guarantee a preferred artistic result.

## 415. From Static to Dynamic: Enhancing AAC with Generative Imagery and Zero-Shot TTS

**Paper:** [From Static to Dynamic: Enhancing AAC with Generative Imagery and Zero-Shot TTS](https://www.isca-archive.org/interspeech_2025/francis25_interspeech.html)
**Taxonomy:** `voice-generation-and-control / expression-and-interactive-control / interactive-latency`
**Evidence:** D3 full-paper capture; PDF SHA-256 `f19af89193786054bb15742a6e18ebe297048630b1b972d7d1465552a8183ef3`; full-text SHA-256 `a90c8059dc46a3cf804e2f4c1f284e1f8e80e1779e37e2ff9f485457ac374dde`.

- **Ordinary problem:** An augmentative communication system should let a minimally verbal child express personal concepts and a personally meaningful voice.
- **Why it is hard:** Fixed symbols and fixed voices limit relevance, identity, and the range of things a user can communicate.
- **Naive attempt:** Offer a static symbol board and one default synthetic voice.
- **Central move:** Generate visual symbols and use zero-shot TTS so users can personalize both the concept representation and voice.
- **Mechanism:** The proposed AAC system combines text-to-image generation with zero-shot TTS for children with autism.
- **Mathematical idea:** The conceptual objects are symbol coverage, voice personalization, and eventual social validity; the paper's abstract does not report a completed comparative trial.
- **What the paper reports:** The paper presents a broader expressive design but leaves long-term communication outcomes for future study.
- **Limits:** No causal benefit or clinical efficacy should be inferred; user satisfaction, safety, cultural fit, and long-term adaptation remain open.

## 416. Voice Impression Control in Zero-Shot TTS

**Paper:** [Voice Impression Control in Zero-Shot TTS](https://www.isca-archive.org/interspeech_2025/fujita25_interspeech.html)
**Taxonomy:** `voice-generation-and-control / expression-and-interactive-control / style-and-emotion-control`
**Evidence:** D3 full-paper capture; PDF SHA-256 `d8845d3d2166ef9c15ba9a96b16fc43dbe6a90e0ad952b9b3c3456c6886d5471`; full-text SHA-256 `c489e7c2e6a6d200a23e9259e55b8482e2e8c478de1a93ccd5b6089bb1d30749`.

- **Ordinary problem:** Zero-shot TTS can imitate a voice while failing to control the subtle qualities listeners perceive as bright, dark, tense, or warm.
- **Why it is hard:** Speaker identity and impression are entangled, and a text description alone is too coarse for fine control.
- **Naive attempt:** Add a style token or manually search a latent vector for every speaker.
- **Central move:** Represent impression as a small vector of antonym-pair intensities, remove it from the speaker representation, and reinsert the requested values at synthesis time.
- **Mechanism:** The method trains a control module around FastSpeech2, uses subjective ratings to estimate impression vectors, and uses a language model to turn descriptions into those vectors.
- **Mathematical idea:** A generated utterance is judged on two axes: whether it preserves the reference speaker and whether the requested impression moves in the intended direction. The dimensions are correlated, so independent sliders are an approximation.
- **What the paper reports:** Objective and subjective tests report effective single-dimension impression control and language-generated vectors that avoid manual optimization.
- **Limits:** The evidence is limited to the selected impression dimensions, speakers, ratings, and TTS model; listener consistency and cross-language control are not established.

## 417. Differentiable Reward Optimization for LLM based TTS system

**Paper:** [Differentiable Reward Optimization for LLM based TTS system](https://www.isca-archive.org/interspeech_2025/gao25d_interspeech.html)
**Taxonomy:** `voice-generation-and-control / expression-and-interactive-control / style-and-emotion-control`
**Evidence:** D3 full-paper capture; PDF SHA-256 `73869cc8f1893064e786fa76ed8a8c89f7b24246fc5a5cd677315f41aa2ebf00`; full-text SHA-256 `d7c96d22dff5c3e66089d6b22945bc8cb82ec08676ddbb624f68e641366d75df`.

- **Ordinary problem:** A speech generator should obey requests about pronunciation, emotion, age, gender, or quality, but judging every generated waveform during training is expensive and listener preferences are hard to turn into a differentiable signal.
- **Why it is hard:** Codec language models generate discrete tokens that later become audio through a flow model and vocoder, so an audio-level reward creates a costly feedback loop and may not distinguish competing outputs.
- **Naive attempt:** Use ordinary reinforcement learning with rewards computed after full waveform synthesis, or optimize only next-token likelihood.
- **Central move:** Predict several task rewards directly from codec tokens and make the reward path differentiable with Gumbel-Softmax, allowing direct back-propagation into the token language model.
- **Mechanism:** DiffRO predicts rewards for ASR, emotion, speech quality, age, and gender from generated codec tokens; a multi-task reward model supplies the signal and the language model is optimized without the full reinforcement-learning loop.
- **Mathematical idea:** The method replaces a sampled discrete choice with a soft probability over codebook entries during training, so reward gradients can reach token probabilities; the reward is a proxy whose meaning depends on each downstream predictor.
- **What the paper reports:** The paper reports improved pronunciation accuracy and state-of-the-art WER results, with controllability experiments for emotion, MOS, age, and gender; codec-level MOS and re-encoded audio reveal disagreement between proxy and waveform quality.
- **Limits:** Reward-model accuracy, codec reconstruction, vocoder behavior, sampling, and listener perception bound the result; a differentiable proxy is not the same as human preference or end-to-end quality.

## 418. DnR-nonverbal: Cinematic Audio Source Separation DatasetContaining Non-Verbal Sounds

**Paper:** [DnR-nonverbal: Cinematic Audio Source Separation DatasetContaining Non-Verbal Sounds](https://www.isca-archive.org/interspeech_2025/hasumi25_interspeech.html)
**Taxonomy:** `voice-generation-and-control / expression-and-interactive-control / style-and-emotion-control`
**Evidence:** D3 full-paper capture; PDF SHA-256 `2a85e203d77f60fd2faa610729b1647c07ebcdd96bf073be90643533ba17a5b4`; full-text SHA-256 `32ba22eb07a62781aadde67303b66fccb94ab51592cc03bfe8b42a7f2fc1a749`.

- **Ordinary problem:** A cinematic separator should keep laughter and screams with the speech stem, because acted nonverbal voice is part of a scene rather than an ordinary sound effect.
- **Why it is hard:** Existing datasets often contain read speech, so a model can learn the wrong boundary and remove emotionally heightened vocal sounds as noise or effects.
- **Naive attempt:** Train on reading-style stems and assume the separator's speech category matches film dialogue.
- **Central move:** Build a dataset whose speech stem includes nonverbal vocalizations and test whether that changes separation behavior on cinematic mixtures.
- **Mechanism:** DnR-nonverbal is a cinematic audio source-separation dataset containing laughter, screams, and other nonverbal sounds in the speech stem.
- **Mathematical idea:** The dataset changes the category definition presented to the model: the target is a vocal event in context, not a narrow phonetic transcript.
- **What the paper reports:** The paper reports that conventional separators mishandle nonverbal sounds and that the new dataset improves the tested synthetic separation task.
- **Limits:** Synthetic mixtures, labels, scene distribution, separator, and nonverbal taxonomy bound the result; real-film generalization remains open.

## 419. SOVA-Bench: Benchmarking the Speech Conversation Ability for LLM-based Voice Assistant

**Paper:** [SOVA-Bench: Benchmarking the Speech Conversation Ability for LLM-based Voice Assistant](https://www.isca-archive.org/interspeech_2025/hou25b_interspeech.html)
**Taxonomy:** `voice-generation-and-control / expression-and-interactive-control / interactive-latency`
**Evidence:** D3 full-paper capture; PDF SHA-256 `4c27c0d1559ac0e4ea6fb7815f33c7ff95930f3f9b74ea86bf7e8bcb9e4929d7`; full-text SHA-256 `069a7bb01a359165f61dd754c552ebc336cba381d8ba37e2782b6ffa37ebd384`.

- **Ordinary problem:** A voice assistant should be judged not only by whether it understood a request but also by whether its spoken response sounds natural and conversational.
- **Why it is hard:** Semantic accuracy can hide stiff timing, poor prosody, or unpleasant acoustic quality, and existing tests emphasize understanding.
- **Naive attempt:** Score a voice assistant with text-task accuracy alone.
- **Central move:** Build a benchmark that tests general knowledge, speech recognition/understanding, semantic generation, and acoustic generation together.
- **Mechanism:** SOVA-Bench compares speech LLMs across comprehension and generated-speech dimensions, making acoustic quality an explicit evaluation target.
- **Mathematical idea:** The benchmark separates what the assistant knows, what it understood, and how it sounded; no single score can substitute for those dimensions.
- **What the paper reports:** The paper presents a systematic evaluation framework intended to guide speech-LLM voice interaction.
- **Limits:** Benchmark tasks, prompts, listeners, model versions, and acoustic measures define the comparison; long-term interaction quality and user adaptation remain open.

## 420. LombardTokenizer: Disentanglement and Control of Vocal Effort in a Neural Speech Codec

**Paper:** [LombardTokenizer: Disentanglement and Control of Vocal Effort in a Neural Speech Codec](https://www.isca-archive.org/interspeech_2025/jacquelin25_interspeech.html)
**Taxonomy:** `voice-generation-and-control / expression-and-interactive-control / prosody-control`
**Evidence:** D3 full-paper capture; PDF SHA-256 `61fc6c3b9e690b6d0012a21d81f74bd928e50d8bdb9518ca95a41257ba06343e`; full-text SHA-256 `38dcd250d653d4d841cf69feab1c912eb835aa815d9ce21af7a275b774ee3266`.

- **Ordinary problem:** A speech codec should preserve what was said while allowing a system to change how forcefully it was spoken, such as neutral versus Lombard speech in noise.
- **Why it is hard:** Content, speaker identity, and vocal effort are mixed in ordinary representations, so changing effort can damage words or voice quality.
- **Naive attempt:** Use one undifferentiated code and hope a conversion model learns effort implicitly.
- **Central move:** Place vocal effort in a designated codec layer while keeping semantic content in another layer, making effort controllable.
- **Mechanism:** LombardTokenizer conditions the second quantization layer of SpeechTokenizer on vocal-effort encoders and tests neutral/Lombard conversion and synthesis quality.
- **Mathematical idea:** Layer-wise discrete codes represent different information; conversion metrics and quality tests compare effort control, intelligibility, and naturalness.
- **What the paper reports:** The paper reports better neutral-to-Lombard and Lombard-to-neutral conversion than existing methods while retaining synthesis quality.
- **Limits:** The result is tied to the AVID/Lombard data, selected effort conditions, and codec; other speaking styles, languages, and independent listening tests remain open.

## 421. Prediction of listening effort ratings for habitual and clear-Lombard speech presented in noise

**Paper:** [Prediction of listening effort ratings for habitual and clear-Lombard speech presented in noise](https://www.isca-archive.org/interspeech_2025/janse25_interspeech.html)
**Taxonomy:** `voice-generation-and-control / expression-and-interactive-control / style-and-emotion-control`
**Evidence:** D3 full-paper capture; PDF SHA-256 `05c09b7f5900487fb41579462d00bea9c765dfb02fb88fd7ef5b979719178f47`; full-text SHA-256 `506888b0aeaae853a84687771a881472af6ddb69756d9ec914abefed92220a49`.

- **Ordinary problem:** A system should predict how hard it is to listen to speech in noise, not merely whether the speech is technically intelligible.
- **Why it is hard:** Listeners can reconstruct words by effort even when masking leaves only intermittent speech glimpses, and speaking style changes those glimpses.
- **Naive attempt:** Use one global SNR or intelligibility score as a proxy for effort.
- **Central move:** Measure high-energy speech glimpses and add speaking-style cues such as pitch range and articulation rate to predict listener effort.
- **Mechanism:** HEGP is computed for habitual and clear-Lombard speech in noise; listening-effort ratings are modeled with spectral balance, F0, and rate measures.
- **Mathematical idea:** The target is subjective effort, while HEGP is a release-from-masking proxy; regression tests whether style explains residual variance.
- **What the paper reports:** HEGP predicts effort similarly across styles; wider F0 range and slower articulation are associated with lower effort, especially for habitual speech.
- **Limits:** Noise, listener ratings, speech styles, and HEGP definition bound the result; individual strategy and real device conditions remain open.

## 422. In This Environment, As That Speaker: A Text-Driven Framework for Multi-Attribute Speech Conversion

**Paper:** [In This Environment, As That Speaker: A Text-Driven Framework for Multi-Attribute Speech Conversion](https://www.isca-archive.org/interspeech_2025/jin25d_interspeech.html)
**Taxonomy:** `voice-generation-and-control / expression-and-interactive-control / prosody-control`
**Evidence:** D3 full-paper capture; PDF SHA-256 `8544a0f7a03420856b7ab045805f0bfe2917d5651af545911ef1f651e8ce8924`; full-text SHA-256 `a461c1c1ca03449da02741869e2ead16818ea35f3630d9f1e1c5545fe09e113d`.

- **Ordinary problem:** A user may want the same words spoken by a different person in a different environment, such as a voice heard through a hallway or in a car, while keeping the source message unchanged.
- **Why it is hard:** Speaker timbre and environmental acoustics both change the waveform and can interfere with one another, especially when paired examples for every combination do not exist.
- **Naive attempt:** Train one entangled converter and describe the target only with a speaker recording, or apply room filtering after voice conversion as an independent afterthought.
- **Central move:** Represent target speaker and environment as separate text-controlled attributes, then retrieve timbre evidence and generate the combined result with a latent diffusion converter.
- **Mechanism:** TES-VC uses synthetic data with decoupled vocal/environment features, a retrieval-based timbre-control module, and text descriptions for both target timbre and acoustic environment.
- **Mathematical idea:** The desired output is a composition of content, speaker, and room factors; independent controls are tested by changing one description while holding the others fixed and measuring content retention and controllability.
- **What the paper reports:** The paper reports effective text-driven control of timbre and environment with high content retention and results on in-domain and out-of-domain conditions.
- **Limits:** Synthetic training mixtures, text descriptions, diffusion sampling, evaluation speakers and rooms, and the notion of controllability bound the result; independent factors are operational test dimensions, not guaranteed physical causes.

## 423. Spotlight-TTS: Spotlighting the Style via Voiced-Aware Style Extraction and Style Direction Adjustment for Expressive Text-to-Speech

**Paper:** [Spotlight-TTS: Spotlighting the Style via Voiced-Aware Style Extraction and Style Direction Adjustment for Expressive Text-to-Speech](https://www.isca-archive.org/interspeech_2025/kim25t_interspeech.html)
**Taxonomy:** `voice-generation-and-control / expression-and-interactive-control / style-and-emotion-control`
**Evidence:** D3 full-paper capture; PDF SHA-256 `9cead5a38aa2002e9b36e111bac81f19b76da36587cfc3ede972a6db8731ca71`; full-text SHA-256 `b38b8c231381a406f2920ab7f4b4a18c7998cfca7e9dd5319a5f698ce930bef3`.

- **Ordinary problem:** A TTS system may have a style reference, but if it extracts style from unvoiced pauses or irrelevant regions, the generated voice can sound less expressive or lose continuity.
- **Why it is hard:** Style is carried strongly by voiced regions yet transitions across voiced and unvoiced regions must remain smooth; an embedding that captures everything can mix content, speaker, and style.
- **Naive attempt:** Average one style embedding over the whole waveform or add a separate style module without controlling what it attends to.
- **Central move:** Extract style primarily from voiced regions and adjust the direction of the style representation before injecting it into the TTS model.
- **Mechanism:** Spotlight-TTS uses voiced-aware style extraction, continuity across speech regions, and style-direction adjustment, then compares expressive speech quality and transfer against baseline style-embedding systems.
- **Mathematical idea:** The model treats style as a direction in a representation space rather than a fixed label; selecting voiced evidence and adjusting its direction are two separate controls on what gets transferred.
- **What the paper reports:** The paper reports stronger expressiveness, overall speech quality, and style-transfer capability than its baselines in objective and perceptual evaluations.
- **Limits:** Reference speakers, style labels, voiced-region detection, subjective ratings, and TTS architecture bound the result; a style direction is not a complete account of emotion, identity, or conversational appropriateness.

## 424. Counterfactual Activation Editing for Post-hoc Prosody and Mispronunciation Correction in TTS Models

**Paper:** [Counterfactual Activation Editing for Post-hoc Prosody and Mispronunciation Correction in TTS Models](https://www.isca-archive.org/interspeech_2025/lee25f_interspeech.html)
**Taxonomy:** `voice-generation-and-control / expression-and-interactive-control / prosody-control`
**Evidence:** D3 full-paper capture; PDF SHA-256 `3547f7c666950c5a67df89996a79961f834e7219be6c23d29537d80d2ecedf16`; full-text SHA-256 `dcf8027ccc946558f9df771617153c532989e5884ec2bad37e8f3cdf3b2c8672`.

- **Ordinary problem:** A trained TTS system may pronounce a word incorrectly or use the wrong emphasis, and users may want to fix the output after training without rebuilding the model.
- **Why it is hard:** Prosody and pronunciation are encoded inside many hidden activations, while dictionary-based correction fails for names, new words, and low-resource languages.
- **Naive attempt:** Add a new prosody module, retrain the TTS model, or replace pronunciation with a fixed grapheme-to-phoneme dictionary.
- **Central move:** Find internal activations that causally change the unwanted behavior and edit them counterfactually at inference time, leaving the rest of the pretrained generator intact.
- **Mechanism:** Counterfactual Activation Editing modifies selected internal representations in a model-agnostic TTS system to alter prosodic features and correct mispronunciations; WER/PER, semantic similarity, and CMOS assess the tradeoff.
- **Mathematical idea:** The edit asks what output would result if a hidden feature were moved toward a desired state while other activations stayed fixed; causal intervention, not retraining, is the key object.
- **What the paper reports:** The paper reports lower WER and PER, preserved semantic similarity, and a 0.764-point CMOS improvement from correcting prosody and mispronunciation.
- **Limits:** The chosen model, activation locations, correction targets, language, evaluation prompts, and listener panel bound the claim; an observed intervention effect does not prove a unique causal representation.

## 425. Zero-Shot Mono-to-Binaural Speech Synthesis

**Paper:** [Zero-Shot Mono-to-Binaural Speech Synthesis](https://www.isca-archive.org/interspeech_2025/levkovitch25_interspeech.html)
**Taxonomy:** `voice-generation-and-control / expression-and-interactive-control / interactive-latency`
**Evidence:** D3 full-paper capture; PDF SHA-256 `530d6e4c5dd930880030a7cd4ddbfb3581369852356e70f0b5304338c9e7862e`; full-text SHA-256 `779cf34b8a80014ba8ef79a642e59f6be023b07163f1d5c1d4ba9b542489d7b5`.

- **Ordinary problem:** A monaural speech synthesizer should produce a binaural signal with believable spatial cues even when it has never seen a paired example for the target speaker.
- **Why it is hard:** Binaural cues depend on source position, room, head-related filtering, and speaker content; zero-shot synthesis must infer them without memorizing a fixed room or voice.
- **Naive attempt:** Duplicate mono audio into both channels or apply one generic stereo widening effect.
- **Central move:** Condition zero-shot speech synthesis on spatial information and generate the two channels with consistent content and interaural cues.
- **Mechanism:** The paper studies zero-shot mono-to-binaural speech synthesis.
- **Mathematical idea:** Spatialization is a structured transformation: linguistic content should remain common across channels while timing and spectral differences encode position and acoustic scene.
- **What the paper reports:** The paper reports objective and perceptual results for zero-shot mono-to-binaural synthesis.
- **Limits:** Room and position range, speaker diversity, spatial labels, head-related filtering, and listening protocol bound generalization; stereo plausibility is not physical localization accuracy.

## 426. EME-TTS: Unlocking the Emphasis and Emotion Link in Speech Synthesis

**Paper:** [EME-TTS: Unlocking the Emphasis and Emotion Link in Speech Synthesis](https://www.isca-archive.org/interspeech_2025/li25i_interspeech.html)
**Taxonomy:** `voice-generation-and-control / expression-and-interactive-control / style-and-emotion-control`
**Evidence:** D3 full-paper capture; PDF SHA-256 `d858d8e97d8a95711eaed9d2abd394de9fff2311cd3f28728b8bb30c805fbc0f`; full-text SHA-256 `140dd0d1ec2b97e1ed9885f9eab4ef88565e1c5f1742b2032c87c3bb072b1719`.

- **Ordinary problem:** A TTS system should make emphasis and emotion controllable together, because stressing a word changes how emotion is perceived and emotion changes which emphasis sounds natural.
- **Why it is hard:** Text, prosody, and affect are entangled; independent controls can conflict or produce an emphasized contour that does not fit the intended emotion.
- **Naive attempt:** Add an emotion label after synthesis or control pitch and energy independently with no relation to the emphasized word.
- **Central move:** Model the link between emphasis and emotion explicitly so text position, prosody, and affect can be jointly controlled.
- **Mechanism:** EME-TTS targets the emphasis-emotion link in speech synthesis.
- **Mathematical idea:** Expressive synthesis is a constrained coordination problem: emphasis is local and linguistic, emotion is broader and affective, and the system must make their interaction coherent.
- **What the paper reports:** The paper reports expressive TTS quality and controllability for emphasis and emotion in the tested evaluations.
- **Limits:** Languages, speakers, labels, text prompts, control ranges, and subjective raters bound the claim; controllability does not guarantee natural or culturally appropriate expression.

## 427. SA-RAS: Speaker-Aware Style Retrieval Augmented Generation for Expressive Zero-Shot Text-to-Speech Synthesis

**Paper:** [SA-RAS: Speaker-Aware Style Retrieval Augmented Generation for Expressive Zero-Shot Text-to-Speech Synthesis](https://www.isca-archive.org/interspeech_2025/li25t_interspeech.html)
**Taxonomy:** `voice-generation-and-control / expression-and-interactive-control / style-and-emotion-control`
**Evidence:** D3 full-paper capture; PDF SHA-256 `a7d249384eed74433d675c8adadb686df2f7d6b348828de52bb4fc52b5f5c112`; full-text SHA-256 `9c93589172395241d194ab90a9f7970b568836b19cfc6fc3b966c89e4d7c7c3a`.

- **Ordinary problem:** A zero-shot TTS system should imitate a target speaker while retrieving a speaking style that fits the requested expressive context.
- **Why it is hard:** Speaker identity and style are entangled; retrieving a style example can improve expressiveness but can also copy unwanted content or confuse whose voice is being produced.
- **Naive attempt:** Use one global style embedding or concatenate a reference clip without separating speaker and style information.
- **Central move:** Use speaker-aware style retrieval-augmented generation so the system retrieves relevant style evidence while maintaining zero-shot speaker identity.
- **Mechanism:** SA-RAS is a speaker-aware style retrieval-augmented method for expressive zero-shot TTS.
- **Mathematical idea:** Style retrieval is constrained by identity: the reference supplies how to speak, while the target speaker supplies who speaks, and generation must keep those roles distinct.
- **What the paper reports:** The paper reports expressive quality, speaker similarity, and style-control results for zero-shot synthesis.
- **Limits:** Reference selection, speaker set, style labels, prompts, listening tests, and language bound the claim; style similarity is not a complete account of naturalness.

## 428. Accelerating Autoregressive Speech Synthesis Inference With Speech Speculative Decoding

**Paper:** [Accelerating Autoregressive Speech Synthesis Inference With Speech Speculative Decoding](https://www.isca-archive.org/interspeech_2025/lin25h_interspeech.html)
**Taxonomy:** `voice-generation-and-control / expression-and-interactive-control / interactive-latency`
**Evidence:** D3 full-paper capture; PDF SHA-256 `0131b8d15531c11251044af4f417955befd76df7eeee1243e1e91ab07ca6d6b4`; full-text SHA-256 `a13bddbe0d3aff7c238428be48aa78f18f6f7b8e18764ec37a70295e83abbee8`.

- **Ordinary problem:** Autoregressive speech synthesis can sound good but take too long because it generates one token after another; users need faster inference without obvious quality loss.
- **Why it is hard:** Speculative decoding needs a fast proposal and an accurate verifier, and speech tokens have temporal dependencies that make incorrect guesses audible.
- **Naive attempt:** Generate fewer tokens by skipping steps or use a smaller model and accept a quality drop.
- **Central move:** Use a fast speculative speech model to propose multiple tokens, then verify them with the target model and keep only accepted sequences.
- **Mechanism:** The paper accelerates autoregressive speech-synthesis inference with speech speculative decoding.
- **Mathematical idea:** Speed comes from parallel verification rather than changing the target distribution blindly: accepted blocks preserve the large model's decisions while reducing serial work.
- **What the paper reports:** The paper reports inference-speed gains and quality behavior for speculative speech decoding.
- **Limits:** Tokenization, proposal model, acceptance rate, hardware, speaker/style, and latency measurement bound the result; speedups vary with the workload.

## 429. Towards Emotionally Consistent Text-Based Speech Editing: Introducing EmoCorrector and The ECD-TSE Dataset

**Paper:** [Towards Emotionally Consistent Text-Based Speech Editing: Introducing EmoCorrector and The ECD-TSE Dataset](https://www.isca-archive.org/interspeech_2025/liu25c_interspeech.html)
**Taxonomy:** `voice-generation-and-control / expression-and-interactive-control / style-and-emotion-control`
**Evidence:** D3 full-paper capture; PDF SHA-256 `21bc34bb7ab4d79145a6c901857b937ae7b3993bb475fb572a938cdd16a41db0`; full-text SHA-256 `3d8e0f2e52dd916b45550bf445060fd1e29dedbbbd6b3d36cca92a75ca41556c`.

- **Ordinary problem:** When editing text-based speech, changing a word should preserve the intended emotion and keep the new audio emotionally consistent with its context.
- **Why it is hard:** Text edits can alter sentiment, emphasis, and prosody at once; a locally fluent replacement may sound emotionally wrong next to surrounding speech.
- **Naive attempt:** Replace the text and synthesize the whole sentence, or optimize word correctness without an emotion-consistency check.
- **Central move:** Create an emotion-consistent speech-editing task and model that preserves affect across the edited span and its context.
- **Mechanism:** EmoCorrector and the ECD-TSE dataset target emotionally consistent text-based speech editing.
- **Mathematical idea:** Editing has two invariants: linguistic content must change as requested, while speaker identity and emotional trajectory must remain coherent around the change.
- **What the paper reports:** The paper reports dataset and model results for emotionally consistent speech editing.
- **Limits:** Emotion labels, edit types, speakers, context, synthesis model, and perceptual evaluation bound the claim; emotional consistency is listener- and culture-dependent.

## 430. Investigating Stochastic Methods for Prosody Modeling in Speech Synthesis

**Paper:** [Investigating Stochastic Methods for Prosody Modeling in Speech Synthesis](https://www.isca-archive.org/interspeech_2025/mayer25_interspeech.html)
**Taxonomy:** `voice-generation-and-control / expression-and-interactive-control / style-and-emotion-control`
**Evidence:** D3 full-paper capture; PDF SHA-256 `515c5da55b47db83a123b59fe39a4e5390f4c62fdfa4c2430c28abdd2f2d3d51`; full-text SHA-256 `b224150cd6aa49900734e70332fe51c9680e21590051c41988b0d2a8f5b7376b`.

- **Ordinary problem:** A speech synthesizer should vary prosody naturally across repeated generations while still following the intended text and style.
- **Why it is hard:** Prosody is multi-dimensional and uncertain; deterministic prediction can sound repetitive while unconstrained randomness can change emphasis or meaning.
- **Naive attempt:** Use one average prosody contour or inject random noise without controlling what it changes.
- **Central move:** Investigate stochastic prosody-modeling methods and measure diversity together with intelligibility, naturalness, and controllability.
- **Mechanism:** The paper investigates stochastic methods for prosody modeling in speech synthesis.
- **Mathematical idea:** Prosody is a conditional distribution, not one correct curve: a useful model samples plausible timing and pitch while remaining anchored to linguistic content.
- **What the paper reports:** The paper reports stochastic prosody-modeling behavior and synthesis evaluations for the tested methods.
- **Limits:** Text, speakers, sampling temperature, prosody labels, raters, and metrics bound the claim; diversity alone is not expressive control.

## 431. Voice Conversion Improves Cross-Domain Robustness  for Spoken Arabic Dialect Identification

**Paper:** [Voice Conversion Improves Cross-Domain Robustness  for Spoken Arabic Dialect Identification](https://www.isca-archive.org/interspeech_2025/abdullah25_interspeech.html)
**Taxonomy:** `voice-generation-and-control / identity-and-conversion / speaker-identity`
**Evidence:** D3 full-paper capture; PDF SHA-256 `1a900281aa9a8d251c21d3efbae0d648fecec923df8146287e0bdf38e39174f5`; full-text SHA-256 `ba28b4ee1457775a6a26feaa6b8a0a6b451b2d9a86cb8434dec21d8dba3b0711`.

- **Ordinary problem:** Improve Arabic dialect identification when test speech comes from a different domain or speaker population.
- **Why it is hard:** Dialect classifiers can exploit speaker-specific shortcuts instead of dialect evidence, causing cross-domain failure.
- **Naive attempt:** Train a classifier on available dialect data and treat in-domain accuracy as evidence of dialect robustness.
- **Central move:** Use voice conversion as augmentation to reduce speaker bias, then evaluate on a newly collected real-world cross-domain set.
- **Mechanism:** Converted speech changes speaker characteristics while preserving dialect-related content; controlled experiments compare conversion with ordinary augmentation.
- **Mathematical idea:** Cross-domain accuracy measures transfer rather than memorization; the causal explanation about speaker bias is supported by the paper’s controlled analysis but not independently verified here.
- **What the paper reports:** The paper reports up to +34.07% cross-domain accuracy improvement and releases a model and evaluation dataset.
- **Limits:** The result is specific to Arabic dialect identification and the released artifacts require separate access and execution checks.

## 432. VoxAging: Continuously Tracking Speaker Aging with a Large-Scale Longitudinal Dataset in English and Mandarin

**Paper:** [VoxAging: Continuously Tracking Speaker Aging with a Large-Scale Longitudinal Dataset in English and Mandarin](https://www.isca-archive.org/interspeech_2025/ai25_interspeech.html)
**Taxonomy:** `voice-generation-and-control / identity-and-conversion / speaker-identity`
**Evidence:** D3 full-paper capture; PDF SHA-256 `64a58c303df73ff039e35c79f78c5ea6160867b8e699b13989b8aed0791575e5`; full-text SHA-256 `3e038e48bde255b2d86036b780818c60a32419bdbadbce2d4613a4a107b13ed3`.

- **Ordinary problem:** A speaker system should recognize that a person's voice changes with age rather than treating time-varying identity as noise.
- **Why it is hard:** Longitudinal recordings mix biological change, channel variation, language, and recording history.
- **Naive attempt:** Train one speaker model on pooled recordings and assume a speaker embedding remains stationary.
- **Central move:** Build a longitudinal English/Mandarin resource and measure how aging changes verification evidence.
- **Mechanism:** Link recordings across years, then test verification as time gap, age group, and gender change.
- **Mathematical idea:** EER and embedding cosine similarity turn identity preservation into separability and distance between same-speaker observations.
- **What the paper reports:** The paper reports declining verification accuracy and embedding similarity as recordings move farther apart in time, with age and gender affecting the rate of change.
- **Limits:** Speaker coverage, language balance, recording channels, gated data, and longitudinal confounding limit causal claims about biological aging.

## 433. Towards Better Disentanglement in Non-Autoregressive Zero-Shot Expressive Voice Conversion

**Paper:** [Towards Better Disentanglement in Non-Autoregressive Zero-Shot Expressive Voice Conversion](https://www.isca-archive.org/interspeech_2025/akti25_interspeech.html)
**Taxonomy:** `voice-generation-and-control / identity-and-conversion / voice-conversion`
**Evidence:** D3 full-paper capture; PDF SHA-256 `cf4c5704c02d2541d908600a64375a1a4ae0482b3f2ad27a1944fa462408a9bf`; full-text SHA-256 `b7162ba382083d6d70ab7f5295182541e60d83dba2d13f9f5e735ece77aec77d`.

- **Ordinary problem:** Zero-shot expressive voice conversion should change style while preserving content and identity for unseen voices.
- **Why it is hard:** Content, identity, and style are entangled, and known-speaker training encourages shortcuts.
- **Naive attempt:** Use one entangled vector or train a separate converter for every target speaker.
- **Central move:** Improve disentanglement in non-autoregressive zero-shot expressive voice conversion.
- **Mechanism:** Content, speaker, and expressive factors are separated in a non-autoregressive generation path.
- **Mathematical idea:** The relevant object is the voice-conversion evidence described by the paper's mechanism: Content, speaker, and expressive factors are separated in a non-autoregressive generation path.
- **What the paper reports:** The paper reports improved disentanglement for zero-shot expressive conversion.
- **Limits:** Enrollment, labels, languages, metrics, and unseen-speaker protocol bound transfer.

## 434. REWIND: Speech Time Reversal for Enhancing Speaker Representations in Diffusion-based Voice Conversion

**Paper:** [REWIND: Speech Time Reversal for Enhancing Speaker Representations in Diffusion-based Voice Conversion](https://www.isca-archive.org/interspeech_2025/biyani25_interspeech.html)
**Taxonomy:** `voice-generation-and-control / identity-and-conversion / voice-conversion`
**Evidence:** D3 full-paper capture; PDF SHA-256 `9ff3e2a720a31008a1e6a986537e9607a3649ac3e9377ed7b302be8de9441d6c`; full-text SHA-256 `c6866aa50c1b42093b419c57b06945b3ce857e6855a83e056880fe5b7100bc38`.

- **Ordinary problem:** A voice-conversion system should preserve who the target speaker sounds like without allowing linguistic content to dominate the speaker representation.
- **Why it is hard:** Reversing speech destroys intelligible phonemes and syllables but leaves broad tonal and vocal characteristics, exposing a way to train speaker representations with less language information.
- **Naive attempt:** Train speaker representations only on ordinary speech and assume the embedding will learn identity while ignoring linguistic content.
- **Central move:** Use time-reversed speech as an augmentation: it removes much of the linguistic structure while retaining speaker-related cues, then use the resulting representations in diffusion-based voice conversion.
- **Mechanism:** The full waveform is reversed, passed through the speaker-representation pipeline, and used as an additional training view. The conversion model conditions generation on speaker information while its content path carries the linguistic signal; experiments compare diffusion VC systems with and without the reversed-speech augmentation.
- **Mathematical idea:** The paper evaluates speaker similarity and speech quality rather than treating reversal as a new waveform objective. The conceptual operation is an information intervention: destroy temporal phoneme order while retaining slower vocal traits.
- **What the paper reports:** The paper reports significantly improved speaker-similarity scores while maintaining high speech quality in diffusion-based voice-conversion experiments.
- **Limits:** Time reversal may remove more or less information depending on language and model; the experiments do not establish universal speaker/language disentanglement or human identity judgments across populations. No independent reproduction was performed.

## 435. DAFMSVC: One-Shot Singing Voice Conversion with Dual Attention Mechanism and Flow Matching

**Paper:** [DAFMSVC: One-Shot Singing Voice Conversion with Dual Attention Mechanism and Flow Matching](https://www.isca-archive.org/interspeech_2025/chen25d_interspeech.html)
**Taxonomy:** `voice-generation-and-control / identity-and-conversion / voice-conversion`
**Evidence:** D3 full-paper capture; PDF SHA-256 `30e2a00e939c6b4d1508a56b13da8eacf40f5051c4cd972296516b21abb7b141`; full-text SHA-256 `f029ace1fac8b670834994ff2a1f697bd9fc2dfe4898d2e3b3c776abbdf2a4eb`.

- **Ordinary problem:** A one-shot singing voice converter should transfer an unseen singer's timbre while preserving the source melody and lyrics, without leaking the source singer into the output or making the target sound poor.
- **Why it is hard:** Timbre, melody, linguistic content, and source-speaker traces are entangled in the input; unseen targets provide little paired evidence for adapting all of them at once.
- **Naive attempt:** Copy the source SSL features directly, concatenate a target speaker embedding, and hope the converter separates timbre from melody and words.
- **Central move:** Replace source features with similar target-speaker features, fuse speaker/melody/content through dual attention, and use flow matching to generate the waveform.
- **Mechanism:** DAFMSVC uses target-feature retrieval to reduce timbre leakage, dual cross-attention for adaptive fusion, and a flow-matching generator for one-shot singing voice conversion.
- **Mathematical idea:** The system treats conversion as constrained substitution: target timbre evidence replaces identity-bearing content while melody and lyrics remain conditions; timbre similarity, content accuracy, and quality expose leakage and distortion.
- **What the paper reports:** The paper reports improved target-timbre similarity and generated-audio quality over comparison methods in one-shot singing conversion experiments.
- **Limits:** Singer, song, target-reference duration, feature retrieval, evaluation metrics, and dataset splits bound the result; one-shot similarity does not prove perfect disentanglement or generalization to every unseen singer.

## 436. Unleashing   the  Inner Monster: Demonstrating High-Fidelity Human to Non-Human  Voice Conversion

**Paper:** [Unleashing   the  Inner Monster: Demonstrating High-Fidelity Human to Non-Human  Voice Conversion](https://www.isca-archive.org/interspeech_2025/cho25c_interspeech.html)
**Taxonomy:** `voice-generation-and-control / identity-and-conversion / voice-conversion`
**Evidence:** D3 full-paper capture; PDF SHA-256 `a61cec18b7ddede4960e2c0fb9f80823f3141d1058c488d9cabdaab6edc7ce0a`; full-text SHA-256 `81978649b7dde58e618b658c683ee2ae6a3c15621edc90c2cd9dd15211e06b87`.

- **Ordinary problem:** Game creators need convincing creature voices without recording and manually designing every non-human sound, while the result must remain controllable and fast enough for interaction.
- **Why it is hard:** Human speech features and vocal-tract assumptions do not directly describe a monster; conversion must move beyond speaker identity while preserving expressive timing and the target sound character.
- **Naive attempt:** Train ordinary human voice conversion and expect it to produce convincing non-human vocalizations.
- **Central move:** Record human vocalizations and convert them in real time with a human-to-non-human voice-conversion model designed around selected monster sounds.
- **Mechanism:** The paper demonstrates high-fidelity human-to-non-human voice conversion for games.
- **Mathematical idea:** Voice conversion can be reframed as changing the sound-producing agent, not merely swapping one human identity for another; the target is a designed acoustic character.
- **What the paper reports:** The paper reports real-time conversion and high-quality generated monster sounds in its selected game-oriented conditions.
- **Limits:** Target creatures, recordings, real-time hardware, perceptual evaluation, and controllability bound the claim; a convincing effect is not a biological model of animal vocalization.

## 437. ZSDEVC: Zero-Shot Diffusion-based Emotional Voice Conversion with Disentangled Mechanism

**Paper:** [ZSDEVC: Zero-Shot Diffusion-based Emotional Voice Conversion with Disentangled Mechanism](https://www.isca-archive.org/interspeech_2025/chou25_interspeech.html)
**Taxonomy:** `voice-generation-and-control / identity-and-conversion / zero-shot-voice`
**Evidence:** D3 full-paper capture; PDF SHA-256 `daff5f4235242bb742e5e584d3758995f08407838c5bb99014c138b72f03d824`; full-text SHA-256 `b2aee8ddcddddf9bcabbc3eef5d93c1447535959026c6a1434834fa8c207044f`.

- **Ordinary problem:** Convert emotional expression for an unseen speaker while preserving words and recognizable identity.
- **Why it is hard:** Emotion and identity share acoustic cues, so changing one can distort content or impose training-speaker assumptions.
- **Naive attempt:** Train a speaker-specific converter or change prosody heuristically and accept identity leakage.
- **Central move:** Use zero-shot diffusion with disentangled content, identity, and expressive guidance, testing unseen speakers in and out of domain.
- **Mechanism:** Diffusion denoising reconstructs speech from a noisy latent while separate conditions guide emotion and speaker/content.
- **Mathematical idea:** Disentanglement asks emotion to move while content and identity remain stable enough for a listener.
- **What the paper reports:** The paper reports improved emotional accuracy and naturalness for unseen speakers across evaluated datasets.
- **Limits:** Labels, speaker coverage, out-of-domain definition, protocol, and identity metrics bound transfer; conversion does not establish consent.

## 438. Unsupervised Rhythm and Voice Conversion to Improve ASR on Dysarthric Speech

**Paper:** [Unsupervised Rhythm and Voice Conversion to Improve ASR on Dysarthric Speech](https://www.isca-archive.org/interspeech_2025/elhajal25_interspeech.html)
**Taxonomy:** `voice-generation-and-control / identity-and-conversion / voice-conversion`
**Evidence:** D3 full-paper capture; PDF SHA-256 `cc906672e7e809a762735cca9f17d2802f5651b2d6828e98e38bff1442cd9f3e`; full-text SHA-256 `657fea2c682a945e565ec157da9bc2caecb7f5558e95f6b3d2681bafc41f155b`.

- **Ordinary problem:** ASR should recover dysarthric speech even when slow rhythm and unusual voice quality make the acoustic pattern unlike healthy training speech.
- **Why it is hard:** Speaker variation and rate changes are entangled, and a conversion that sounds healthier may alter linguistic content or fail for severe dysarthria.
- **Naive attempt:** Apply a generic speed perturbation or train a speaker-specific converter and assume the recognizer will adapt.
- **Central move:** Use unsupervised rhythm and voice conversion with syllable-level rhythm modeling, then measure whether converted speech helps LF-MMI and Whisper ASR.
- **Mechanism:** RnV converts timing and voice characteristics without parallel healthy speech; syllable structure supplies a dysarthria-relevant rhythm representation before ASR scoring.
- **Mathematical idea:** Conversion is a task-conditioned invariance: remove cues that obstruct recognition while retaining phonetic content needed by the recognizer.
- **What the paper reports:** On Torgo, LF-MMI shows reported WER reductions, especially for severe dysarthria, while Whisper fine-tuning on converted data has minimal effect.
- **Limits:** Torgo speakers, severity, conversion fidelity, ASR backend, and WER protocol bound transfer; improved recognition is not improved naturalness or clinical communication.

## 439. Private kNN-VC: Interpretable Anonymization of Converted Speech

**Paper:** [Private kNN-VC: Interpretable Anonymization of Converted Speech](https://www.isca-archive.org/interspeech_2025/franzreb25_interspeech.html)
**Taxonomy:** `voice-generation-and-control / identity-and-conversion / zero-shot-voice`
**Evidence:** D3 full-paper capture; PDF SHA-256 `a709e7b81114d1221cb0a2cc2f5c8eaf6460f7ac8d5a48cb7594d21202dd6eb4`; full-text SHA-256 `01e19aa7e1bba3b5ffd36e101b4efc43a9ed58f500d9d0dddb37d51157101a04`.

- **Ordinary problem:** An anonymizer must hide who is speaking while keeping the words and useful speech intact; a strong attacker may exploit prosody rather than obvious voice quality.
- **Why it is hard:** Speaker identity leaks through phone duration and pitch variation even after voice conversion, and a single recognition score does not reveal the leak.
- **Naive attempt:** Convert the voice and assume identity is removed once the main spectral cues change.
- **Central move:** Add interpretable controls that alter phone duration and pitch variation, then test which changes defeat the speaker-recognition attack.
- **Mechanism:** Private kNN-VC extends kNN voice conversion with duration and variation anonymization and compares target-selection strategies under an attack protocol.
- **Mathematical idea:** Privacy is measured through attacker recognition error; the interpretable factors connect a score change to a specific speech property.
- **What the paper reports:** The paper reports that anonymizing duration and variation substantially increases privacy and that target selection changes attack outcomes.
- **Limits:** The evidence is bounded to kNN-VC, the attack model, selected prosodic factors, and utility measures; stronger attackers and human judgments remain open.

## 440. Neurodyne: Neural Pitch Manipulation with Representation Learning and Cycle-Consistency GAN

**Paper:** [Neurodyne: Neural Pitch Manipulation with Representation Learning and Cycle-Consistency GAN](https://www.isca-archive.org/interspeech_2025/gu25_interspeech.html)
**Taxonomy:** `voice-generation-and-control / identity-and-conversion / voice-conversion`
**Evidence:** D3 full-paper capture; PDF SHA-256 `6d62e93261c7572c75ec3f1fab2601ab0b3b3de7267c0506694a442e79298f3b`; full-text SHA-256 `dd0ebe1a33a1a7fb3e44aa22900d6108db4397c16bf5f41e9f4ac6780a7c3515`.

- **Ordinary problem:** Pitch manipulation should change intonation or musical key without destroying the underlying voice and content.
- **Why it is hard:** Pitch, source, and filter cues are entangled, and paired in-tune/out-of-tune examples are scarce.
- **Naive attempt:** Use a DSP pitch shifter or a source-filter disentanglement model trained only on paired examples.
- **Central move:** Learn a pitch-independent latent representation adversarially and use cycle consistency to create the missing pairing implicitly.
- **Mechanism:** Neurodyne encodes speech while an adversary discourages pitch information in the latent; cycle-consistency trains conversion in both directions.
- **Mathematical idea:** The representation must preserve identity/content while making pitch a controllable variable, and cycle consistency supplies a constraint when aligned pairs are absent.
- **What the paper reports:** The paper reports improved global-key and template-based pitch manipulation over its compared methods.
- **Limits:** Music data, pitch range, cycle assumptions, perceptual protocol, and content preservation bound transfer to conversational voice conversion.

## 441. LSCodec: Low-Bitrate and Speaker-Decoupled Discrete Speech Codec

**Paper:** [LSCodec: Low-Bitrate and Speaker-Decoupled Discrete Speech Codec](https://www.isca-archive.org/interspeech_2025/guo25_interspeech.html)
**Taxonomy:** `voice-generation-and-control / identity-and-conversion / voice-conversion`
**Evidence:** D3 full-paper capture; PDF SHA-256 `4cf0e9b1465f07ed184d8fcace0ac26a89b95cc293ea824c9496a1ab86cb8079`; full-text SHA-256 `7a5a00c742bba0414e8f9bcb572f69784a39d17fcb91c844a0b9bc280c863f30`.

- **Ordinary problem:** A speech codec should use few bits while preserving speech quality and should let a downstream system change speaker identity without accidentally carrying the original identity through the code.
- **Why it is hard:** Compression and identity are entangled: a code that preserves every detail spends bits, while a code that removes identity may damage linguistic content or naturalness.
- **Naive attempt:** Compress a standard speaker-dependent representation and assume the decoder will separate identity later.
- **Central move:** Learn a low-bitrate discrete code that is decoupled from speaker identity, then condition decoding on the desired speaker.
- **Mechanism:** LSCodec targets low-bitrate, speaker-decoupled discrete speech coding for controllable reconstruction or conversion.
- **Mathematical idea:** The code is a bottleneck with a division of labor: linguistic/acoustic content crosses the bottleneck, while speaker identity is supplied separately at decoding.
- **What the paper reports:** The paper reports low-bitrate codec and speaker-decoupling results on its reconstruction/conversion evaluations.
- **Limits:** Bitrate, speaker set, decoder, datasets, and disentanglement tests bound the claim; identity leakage can remain outside the tested conditions.

## 442. Voices of `cyborg awesomeness': Posthuman embodiment of nonbinary gender expression in AI speech technologies

**Paper:** [Voices of `cyborg awesomeness': Posthuman embodiment of nonbinary gender expression in AI speech technologies](https://www.isca-archive.org/interspeech_2025/hope25_interspeech.html)
**Taxonomy:** `voice-generation-and-control / identity-and-conversion / speaker-identity`
**Evidence:** D3 full-paper capture; PDF SHA-256 `9f973b1c5beb4ab0469298f17c0bb05455d8a3f9106764b2cb9116ef1d200a83`; full-text SHA-256 `f2aa9d4d440149a56236dafe5cef2ca9d084e8183d2eed5cd63d344ba47b8984`.

- **Ordinary problem:** For a person who communicates through a speech-generating device, voice is part of self-expression; a useful synthetic voice must be controllable in ways that match the person's identity rather than a default category.
- **Why it is hard:** A small set of voice controls can encode gendered assumptions, while blending identities or changing vocal-tract and voice-quality features can produce affirming, uncomfortable, or unexpected bodily responses.
- **Naive attempt:** Offer one fixed synthetic voice or map identity to a binary pitch choice, assuming lower or higher pitch alone determines whether the voice fits the user.
- **Central move:** Let users explore breathiness, vocal tension, acoustic vocal-tract length, weighted blends between speaker identities, and a continuous transition between identities, then ask users how the voices feel and whether they affirm their gender.
- **Mechanism:** The study presents generated samples from controllable TTS and modified XTTSv2/MAGES systems to 12 nonbinary adults who use speech-generating devices. It measures F0, HNR, and acoustic vocal-tract length with Praat and combines close-ended responses with open-ended reflections.
- **Mathematical idea:** Acoustic vocal-tract length is estimated from the third formant using aVTL = 34000/(2 times mean F3/2.5). The samples deliberately move controls by large standardized amounts; the survey counts preferences and gender affirmation rather than fitting a predictive model.
- **What the paper reports:** Nine of 12 participants wanted breathiness control, 11 wanted vocal-tension control, all 12 wanted extreme vocal-tract-length control, and all 12 wanted the ability to blend two voices; nine found the MoreSecond blend gender-affirming.
- **Limits:** There are 12 participants, deliberately extreme synthetic settings, and a qualitative/close-ended survey rather than a deployment study. Preferences are not a universal mapping from acoustic features to gender; results and interpretations are author-reported and were not independently reproduced.

## 443. Mitigating Non-Target Speaker Bias in Guided Speaker Embedding

**Paper:** [Mitigating Non-Target Speaker Bias in Guided Speaker Embedding](https://www.isca-archive.org/interspeech_2025/horiguchi25_interspeech.html)
**Taxonomy:** `voice-generation-and-control / identity-and-conversion / speaker-identity`
**Evidence:** D3 full-paper capture; PDF SHA-256 `2dc8c0b47ae70b32e1c0225e638f762ac99e8ff9d432a05ecf6f46845b12223d`; full-text SHA-256 `94067e0af855dfb0e726e0993cb9955467dfaaf1151723075f64304d14dd66a5`.

- **Ordinary problem:** A speaker embedding should represent the target speaker when another person overlaps, but it should not become worse in ordinary low-overlap speech because the system is overreacting to irrelevant intervals.
- **Why it is hard:** Global statistics can include frames in which only the non-target speaker is active; this contaminates the target representation, especially when severe-overlap training conditions are rare in natural conversation.
- **Naive attempt:** Aggregate statistics over the whole recording or optimize only for extreme overlap and ignore the low-overlap degradation.
- **Central move:** Use target-speaker activity clues to compute statistics only where the target is active, preserving the benefit of guided extraction without letting non-target intervals dominate.
- **Mechanism:** The paper diagnoses the failure in guided speaker embeddings and modifies global-statistics modules to condition their pooling on target activity, then evaluates speaker verification in low- and high-overlap conditions.
- **Mathematical idea:** Pooling is a weighted estimate of speaker identity; changing the support of that estimate changes which voice contributes, so overlap robustness and ordinary-case preservation can be measured separately.
- **What the paper reports:** The proposed activity-aware statistics improve speaker verification under severe overlap while reducing the degradation seen in low-overlap cases.
- **Limits:** Activity labels, overlap ratios, pooling design, speaker-verification protocol, and evaluation speakers bound the claim; improvement against this overlap pattern does not prove robustness to every diarization or adversarial error.

## 444. Facilitating Personalized TTS for Dysarthric Speakers Using Knowledge Anchoring and Curriculum Learning

**Paper:** [Facilitating Personalized TTS for Dysarthric Speakers Using Knowledge Anchoring and Curriculum Learning](https://www.isca-archive.org/interspeech_2025/jeon25_interspeech.html)
**Taxonomy:** `voice-generation-and-control / identity-and-conversion / zero-shot-voice`
**Evidence:** D3 full-paper capture; PDF SHA-256 `17543ed8ca27efa940eb68bceb9ddae535aa03490bd476855183466aa8f0661b`; full-text SHA-256 `6d2dab5121701a84a16e8f3bbf4c0a43793ddde44440d1d8427a83ae09b26195`.

- **Ordinary problem:** Personalized TTS for dysarthric speakers must preserve identity while producing intelligible speech from scarce and errorful recordings.
- **Why it is hard:** A model can improve intelligibility by erasing the speaker traits personalization is meant to retain.
- **Naive attempt:** Fine-tune directly on all target audio and accept overfitting or poor pronunciation.
- **Central move:** Anchor the target speaker to a teacher model and use curriculum learning before specializing to dysarthric articulation.
- **Mechanism:** A teacher-student knowledge-anchoring framework is evaluated across speaker groups with shortened audio.
- **Mathematical idea:** PER measures intelligibility and speaker similarity measures identity; reported PER reaches 15.579 and similarity rises from 0.586 to 0.708.
- **What the paper reports:** Curriculum and anchoring lower PER and improve speaker similarity across reported groups.
- **Limits:** Groups, language, recording conditions, and reported metrics limit clinical claims.

## 445. LinearVC: Linear Transformations of Self-Supervised Features Through the Lens of Voice Conversion

**Paper:** [LinearVC: Linear Transformations of Self-Supervised Features Through the Lens of Voice Conversion](https://www.isca-archive.org/interspeech_2025/kamper25_interspeech.html)
**Taxonomy:** `voice-generation-and-control / identity-and-conversion / voice-conversion`
**Evidence:** D3 full-paper capture; PDF SHA-256 `9dc6d73aa40e047fa9874135439bb612a7f90a00340387442d3d93fe8571e2a5`; full-text SHA-256 `c9bba4ed49f3781d5023fc19e994c3a34152835e31653a8dbd02f08bfc26cc5c`.

- **Ordinary problem:** Voice conversion should transform a speaker's voice while preserving linguistic content and remain useful with limited target data.
- **Why it is hard:** Self-supervised features encode both content and identity, so a simple transform can leak source traits or distort words.
- **Naive attempt:** Copy nearest target embeddings or train a separate waveform model per speaker.
- **Central move:** Study linear transformations of self-supervised features as a controlled voice-conversion mechanism.
- **Mechanism:** A learned transformation maps representation distributions toward a target voice while retaining content-related structure.
- **Mathematical idea:** Conversion is a representation-space mapping: content preservation and target identity are competing constraints.
- **What the paper reports:** The paper reports LinearVC results through the lens of self-supervised feature transformations.
- **Limits:** Feature model, languages, target data, similarity/content metrics, and transform assumptions bound transfer.

## 446. Vo-Ve: An Explainable Voice-Vector for Speaker Identity Evaluation

**Paper:** [Vo-Ve: An Explainable Voice-Vector for Speaker Identity Evaluation](https://www.isca-archive.org/interspeech_2025/lee25e_interspeech.html)
**Taxonomy:** `voice-generation-and-control / identity-and-conversion / speaker-identity`
**Evidence:** D3 full-paper capture; PDF SHA-256 `92a27fe7fdd1c407f717cc174311ef5083a4b71cdb2cd8e75fc84d913129cfa7`; full-text SHA-256 `da3fe8d5094c207a3e804a7b4d4a235f075d6c318203510f2187f5230ea9ef14`.

- **Ordinary problem:** A speaker-similarity system should say not only whether two voices match but which voice attributes support that judgment.
- **Why it is hard:** Ordinary embeddings compress identity into opaque coordinates, making errors and shifts across tasks difficult to interpret.
- **Naive attempt:** Use a black-box speaker embedding and treat its similarity score as a complete explanation.
- **Central move:** Represent identity with an interpretable vector of explicit voice-attribute class probabilities and compare its similarity with conventional embeddings.
- **Mechanism:** Vo-Ve maps speech to attribute probabilities; similarity can then be decomposed into human-readable properties instead of a single latent distance.
- **Mathematical idea:** The representation trades some compact opacity for an interpretable coordinate system whose attributes can be inspected when similarity changes.
- **What the paper reports:** The paper reports competitive speaker-similarity evaluation and attribute-level explanations in its experiments.
- **Limits:** Attribute inventory, labels, language, channel variation, and metric protocol bound interpretability; explainable similarity is not proof of causal identity factors.

## 447. Training-Free Voice Conversion with Factorized Optimal Transport

**Paper:** [Training-Free Voice Conversion with Factorized Optimal Transport](https://www.isca-archive.org/interspeech_2025/lobashev25_interspeech.html)
**Taxonomy:** `voice-generation-and-control / identity-and-conversion / voice-conversion`
**Evidence:** D3 full-paper capture; PDF SHA-256 `6fd2ba5677f7cded0f454f0ac89c66f92ff85fca5051811ae77a82bf0e414220`; full-text SHA-256 `9f213cd26eff3973d21b5fde8e8520566381a937777c58da9bcc61e060162730`.

- **Ordinary problem:** Any-to-any voice conversion should change identity from a short reference while preserving the source linguistic content, including across languages.
- **Why it is hard:** Nearest-neighbor replacement needs long reference recordings and can import language-specific artifacts; training a new converter per speaker defeats the any-to-any goal.
- **Naive attempt:** Replace each source embedding with its closest target embedding and assume five minutes of reference speech is always available.
- **Central move:** Replace nearest-neighbor matching with a factorized optimal-transport map in WavLM embedding subspaces, requiring only a short reference.
- **Mechanism:** Monge–Kantorovich linear transport aligns source and target feature distributions; factorization normalizes unequal variances before the encoder-converter-vocoder reconstructs speech.
- **Mathematical idea:** Optimal transport matches distributions rather than individual frames, allowing sparse reference evidence to define a target voice without storing a lookup for every source sound.
- **What the paper reports:** MKL-VC reports improved content preservation and short-reference robustness on LibriSpeech and FLEURS, with cross-lingual performance comparable to FACodec.
- **Limits:** Reference duration, WavLM space, languages, vocoder, speaker similarity metric, and implementation choices bound transfer; content preservation does not prove perfect identity conversion.

## 448. Eigenvoice Synthesis based on Model Editing for Speaker Generation

**Paper:** [Eigenvoice Synthesis based on Model Editing for Speaker Generation](https://www.isca-archive.org/interspeech_2025/murata25b_interspeech.html)
**Taxonomy:** `voice-generation-and-control / identity-and-conversion / zero-shot-voice`
**Evidence:** D3 full-paper capture; PDF SHA-256 `d7327d2c25ece965d748da4831731419a18961b8a0f81f7e8158510c2c63bc54`; full-text SHA-256 `25ffb37b0505f6979c4f52aaa9525af407aa8057529bf5a0c633e45e214aed82`.

- **Ordinary problem:** Generate a plausible unseen speaker voice without requiring a reference utterance from that speaker.
- **Why it is hard:** Speaker identity is high-dimensional and entangled with linguistic content; sampling a voice representation can leave the valid speaker manifold.
- **Naive attempt:** Interpolate stored speaker embeddings or clone a speaker from a reference sample, which cannot create a genuinely unseen identity without reference audio.
- **Central move:** Define an eigenvoice space directly in the parameter space of a DNN TTS model and sample edited model parameters to synthesize new speaker traits.
- **Mechanism:** Model-difference directions act as speaker basis vectors; adding sampled combinations to a base model changes identity while retaining the learned text-to-speech mapping.
- **Mathematical idea:** The speaker manifold can be represented by low-dimensional directions in parameter space rather than only by an input speaker vector.
- **What the paper reports:** The paper reports diverse generated voices and compares parameter-space eigenvoice synthesis with prior speaker-generation approaches.
- **Limits:** Validity of sampled parameters, diversity and naturalness criteria, speaker-identification protocol, base model, and absence of reference audio bound the claim; generated identity is not evidence of a real person.

## 449. DS-Codec: Dual-Stage Training with Mirror-to-NonMirror Architecture Switching for Speech Codec

**Paper:** [DS-Codec: Dual-Stage Training with Mirror-to-NonMirror Architecture Switching for Speech Codec](https://www.isca-archive.org/interspeech_2025/chen25p_interspeech.html)
**Taxonomy:** `voice-generation-and-control / waveform-and-codec-generation / neural-vocoder`
**Evidence:** D3 full-paper capture; PDF SHA-256 `3db722e74038c95e08fd2ad0b29ab832bcf8323822e34078ec593e66105ee712`; full-text SHA-256 `09863c6e96443d2d23e30aaf60c085a7ba1a8ee8e6d0196b74c5a6ede59d0d46`.

- **Ordinary problem:** A speech codec must turn a waveform into a short discrete sequence and reconstruct speech that still sounds and works like the original; using several codebooks adds rate and system complexity.
- **Why it is hard:** A single codebook must carry both coarse linguistic structure and fine acoustic detail, while encoder and decoder capacity can become unbalanced during training.
- **Naive attempt:** Use residual codebooks with more tokens, or train a mirror-shaped encoder and decoder throughout even when the decoder needs greater capacity.
- **Central move:** Train in two stages: first use a mirror architecture to stabilize the codebook, then switch to a stronger non-mirror decoder while preserving the learned quantizer.
- **Mechanism:** DS-Codec uses vector and product quantization with one 8,192-entry codebook, a downsampling encoder, recurrent/transformer decoder components, and time/frequency discriminators; ablations compare mirror and non-mirror stages.
- **Mathematical idea:** Quantization maps a continuous latent vector to a nearby code; the staged architecture changes which parameters are allowed to adapt after the codebook has learned a stable partition, while reconstruction and perceptual metrics test the recovered waveform.
- **What the paper reports:** The paper reports that mirror-stage training outperforms APCodec+ and the non-mirror alternatives on its objective measures, with lower reconstruction error and fewer training epochs/cost.
- **Limits:** The speech data, bitrate/downsampling setting, discriminators, metrics, and baselines bound the result; reconstruction quality does not by itself prove usefulness for every TTS or speech-language-model task.

## 450. AF-Vocoder: Artifact-Free Neural Vocoder with Global Artifact Filter

**Paper:** [AF-Vocoder: Artifact-Free Neural Vocoder with Global Artifact Filter](https://www.isca-archive.org/interspeech_2025/chen25q_interspeech.html)
**Taxonomy:** `voice-generation-and-control / waveform-and-codec-generation / neural-vocoder`
**Evidence:** D3 full-paper capture; PDF SHA-256 `c2be743fa83e3d0071a57ccead4ad2fffb8e3782c5a09566b5d4b035eefd112f`; full-text SHA-256 `07c3fa8aa6c76c35a9d4729370d3b0bcf91e476af441036ab69fca4fb0760466`.

- **Ordinary problem:** A neural vocoder should produce detailed speech quickly without adding aliasing, blur, or other audible artifacts.
- **Why it is hard:** GAN vocoders can be sharp and fast but their frequency behavior can create artifacts that aggregate quality scores miss.
- **Naive attempt:** Use a generic GAN vocoder and rely on its learned filters to suppress artifacts.
- **Central move:** Add a learnable frequency-domain artifact filter that imposes explicit control over which spectral components pass.
- **Mechanism:** AF-Vocoder inserts GAFilter into a GAN vocoder and tests reconstruction quality and artifact suppression across datasets and speakers.
- **Mathematical idea:** The frequency filter is the intervention; reconstruction and artifact measures compare quality in-domain and for out-of-domain speakers.
- **What the paper reports:** The paper reports better reconstruction quality and artifact suppression than other GAN vocoders.
- **Limits:** Datasets, speaker coverage, artifacts, and listening protocol define the claim; real-time hardware cost and unseen languages remain open.

## 451. Vocoder-Projected Feature Discriminator

**Paper:** [Vocoder-Projected Feature Discriminator](https://www.isca-archive.org/interspeech_2025/kaneko25b_interspeech.html)
**Taxonomy:** `voice-generation-and-control / waveform-and-codec-generation / neural-vocoder`
**Evidence:** D3 full-paper capture; PDF SHA-256 `6ef656867ca9b6ed64b2f0b3d136e3cade39a120316b4660c2dda8afde7adb5e`; full-text SHA-256 `b8af0e06ae59e5962db3a2c2d630132056c5aa14fd454ffb436fe4df5e902806`.

- **Ordinary problem:** Waveform-generating models need an adversarial signal that rewards perceptual detail without making training prohibitively expensive.
- **Why it is hard:** Time-domain discrimination after waveform upsampling consumes memory and computation, while compact acoustic features can hide artifacts that appear after vocoding.
- **Naive attempt:** Discriminate only mel or acoustic features, or run a full waveform discriminator at every training step despite the cost.
- **Central move:** Project generated acoustic features through a vocoder and discriminate in a vocoder-feature space, retaining waveform-relevant feedback with lower time-domain overhead.
- **Mechanism:** The vocoder-projected feature discriminator compares feature representations after synthesis; diffusion-based voice-conversion distillation tests whether the adversarial target improves the generated waveform.
- **Mathematical idea:** The discriminator changes the metric space rather than the generator's output target: it seeks features that preserve vocoder-relevant waveform distinctions while avoiding repeated raw-waveform processing.
- **What the paper reports:** The paper reports improved diffusion-based VC distillation quality from the projected-feature discriminator under the evaluated settings.
- **Limits:** Vocoder choice, feature projection, training compute, VC data, and perceptual evaluation determine the result; a reported quality gain does not establish universal TTS or VC superiority.

## 452. BitTTS: Highly Compact Text-to-Speech Using 1.58-bit Quantization and Weight Indexing

**Paper:** [BitTTS: Highly Compact Text-to-Speech Using 1.58-bit Quantization and Weight Indexing](https://www.isca-archive.org/interspeech_2025/kawamura25_interspeech.html)
**Taxonomy:** `voice-generation-and-control / waveform-and-codec-generation / neural-vocoder`
**Evidence:** D3 full-paper capture; PDF SHA-256 `cf0e175f72475c44370046deb3b727b3e238ec08b11674c14558f4ff087dca2f`; full-text SHA-256 `1f3fefc79dcd8a90cfa6e0742d709394ba9c85cf3812607b3f5de4363c7c4066`.

- **Ordinary problem:** A TTS model may sound good but be too large for a phone or embedded device; reducing its storage and arithmetic must not destroy intelligibility and naturalness.
- **Why it is hard:** Weights are normally stored with more numerical precision than an edge device needs, but aggressive quantization can change the generator's behavior and hardware may still store small values inefficiently.
- **Naive attempt:** Shrink the architecture until it fits, or quantize weights after training and accept whatever quality loss results.
- **Central move:** Train with quantization present and pack groups of ternary-like weights into compact integer indices so the model learns to tolerate the reduced precision and storage format.
- **Mechanism:** BitTTS uses quantization-aware training down to 1.58-bit, with most weights represented as -1, 0, or 1, and weight indexing that stores groups as int8 indices for on-device use.
- **Mathematical idea:** Quantization replaces a continuous parameter with a small codebook; training under that constraint lets the model adapt, while model size and synthesis quality measure the deployment tradeoff.
- **What the paper reports:** The paper reports an 83% reduction in model size and better synthesis quality than a similar-size unquantized baseline.
- **Limits:** Hardware, model architecture, bitrate/precision, speech data, and quality metrics bound the result; smaller storage does not automatically mean lower latency or energy on every device.

## 453. Efficient Streaming TTS Acoustic Model with Depthwise RVQ Decoding Strategies in a Mamba Framework

**Paper:** [Efficient Streaming TTS Acoustic Model with Depthwise RVQ Decoding Strategies in a Mamba Framework](https://www.isca-archive.org/interspeech_2025/lee25h_interspeech.html)
**Taxonomy:** `voice-generation-and-control / waveform-and-codec-generation / neural-vocoder`
**Evidence:** D3 full-paper capture; PDF SHA-256 `a0662bcda4333905aa6032b3a56bfcdb8dd9b86a10d509ed44fe2506f7e6481b`; full-text SHA-256 `2d5e70cbea7f4c7295b0d0a974573061057fd765b0684a80c00245590c18b656`.

- **Ordinary problem:** A useful device speech generator must be intelligible, natural, fast enough for streaming, and usable across speakers.
- **Why it is hard:** Codec TTS often predicts several discrete code levels sequentially, making large models slow even when waveform quality is good.
- **Naive attempt:** Use a large autoregressive decoder and accept long latency, or predict code levels independently and lose their dependencies.
- **Central move:** Use a Mamba acoustic model with depthwise residual-codec decoding: masked refinement preserves dependencies, while implicit neural representation predicts levels in parallel.
- **Mechanism:** SMAM is tested with MLM, INR, and no-MLM decoding in a zero-shot speaker-conditioned setup; CER, similarity, quality, real-time factor, latency, and listening scores separate tradeoffs.
- **Mathematical idea:** MLM reports 26M parameters, CER 2.73, RTF 0.701, latency 0.065 s, MOS 4.02, and SMOS 3.36; INR uses 25M parameters and RTF 0.568 with latency 0.061 s.
- **What the paper reports:** The proposed models are smaller and faster than listed non-streaming baselines while remaining competitive; removing MLM degrades quality measures.
- **Limits:** Codec, datasets, hardware, and zero-shot speaker conditions bound the conclusion; other languages and devices are not established.

## 454. RapFlow-TTS: Rapid and High-Fidelity Text-to-Speech with Improved Consistency Flow Matching

**Paper:** [RapFlow-TTS: Rapid and High-Fidelity Text-to-Speech with Improved Consistency Flow Matching](https://www.isca-archive.org/interspeech_2025/park25b_interspeech.html)
**Taxonomy:** `voice-generation-and-control / waveform-and-codec-generation / neural-vocoder`
**Evidence:** D3 full-paper capture; PDF SHA-256 `95eaadb01e4c07c51f4844917758453f42610b6e72b715f20e4fa26db18c45fa`; full-text SHA-256 `998d08320a63c3e0e64ee4ccea32da8c42e7c25a5588f10c4d2fde5d8e93dbdf`.

- **Ordinary problem:** A TTS system should produce natural speech quickly enough for interactive use without quality collapsing when sampling steps are reduced.
- **Why it is hard:** ODE-based flow generation follows a continuous path but normally needs many numerical steps; shortcutting the path can break consistency and introduce artifacts.
- **Naive attempt:** Use a many-step sampler or distill it without constraining the velocity field along the path.
- **Central move:** Train RapFlow-TTS with velocity consistency along a straightened flow-matching trajectory, plus time scheduling and adversarial refinement.
- **Mechanism:** The model learns that velocity predictions at different time points agree along the transport path; consistency allows few-step integration while adversarial and acoustic losses protect waveform quality.
- **Mathematical idea:** Consistency regularization turns a generation trajectory into a reusable shortcut: nearby time intervals should imply compatible updates.
- **What the paper reports:** The paper reports high-fidelity synthesis with fewer generation steps than compared flow/diffusion systems.
- **Limits:** Text/speaker data, subjective protocol, step counts, vocoder and hardware, and adversarial stability bound the speed-quality claim; fewer steps do not guarantee lower end-to-end latency.

## 455. Intelligibility of Text-to-Speech Systems for Mathematical Expressions

**Paper:** [Intelligibility of Text-to-Speech Systems for Mathematical Expressions](https://www.isca-archive.org/interspeech_2025/roychowdhury25_interspeech.html)
**Taxonomy:** `voice-generation-and-control / waveform-and-codec-generation / intelligibility-naturalness`
**Evidence:** D3 full-paper capture; PDF SHA-256 `702c8f68987fbac3505bf3bc88b0cba5e2895697aea30606404df796f57598df`; full-text SHA-256 `30824a9240d34d52f2f12300514776c4767b7297710a288982fa8b4d5869366e`.

- **Ordinary problem:** A TTS system can pronounce ordinary prose acceptably yet make mathematical notation unintelligible because symbols, structure, and relations must be spoken in an exact order.
- **Why it is hard:** LaTeX is not directly readable by TTS, and a fluent-sounding output may still change an equation’s meaning; MOS alone cannot tell whether a listener recovered the expression.
- **Naive attempt:** Convert formulas to text with a generic prompt and judge the audio by naturalness or a single speech-quality metric.
- **Central move:** Evaluate the full chain—LLM pronunciation generation, TTS rendering, listener comprehension, expert comparison, and expression category—using both perceptual and transcription-based measures.
- **Mechanism:** The study samples 120 expressions across eight categories, uses Qwen or GPT-4 to create spoken text, synthesizes audio with five TTS models, and asks 49 technically trained listeners to rate and transcribe it. A second test compares 35 expressions with hidden expert renditions.
- **Mathematical idea:** Evaluation includes MOS, exact count-of-correct, LaTeX character error rate, and TeXBLEU; ANOVA tests TTS model, expression category, and LLM effects. The denominator is the selected expression/listener trials, not general language understanding.
- **What the paper reports:** No TTS model is consistently strong across categories; intelligibility varies by expression type and model, and the outputs are generally worse than expert renditions. Pronunciation correctness is reported at 87.5% overall, with category-dependent listener success.
- **Limits:** The expressions, listeners, languages, LLMs, and five TTS systems define the scope; technical listeners and repeated playback may not represent ordinary users. Transcription and MOS remain proxies for mathematical comprehension, and no independent reproduction was performed.

## 456. Bridging the Training–Inference Gap in TTS: Training Strategies for Robust Generative Postprocessing for Low-Resource Speakers

**Paper:** [Bridging the Training–Inference Gap in TTS: Training Strategies for Robust Generative Postprocessing for Low-Resource Speakers](https://www.isca-archive.org/interspeech_2025/zalkow25_interspeech.html)
**Taxonomy:** `voice-generation-and-control / waveform-and-codec-generation / intelligibility-naturalness`
**Evidence:** D3 full-paper capture; PDF SHA-256 `ef5ef664536b4c7e066ebb62f1d103215033561c799162a46e6c16d39358a09e`; full-text SHA-256 `8349131a8a4852b2e9b0dfd2baf03bcbe8cc0809c6f3b14161c8bf37d8f84488`.

- **Ordinary problem:** Low-resource TTS can have correct content but unnatural acoustic detail, so postprocessing must improve naturalness without changing speech.
- **Why it is hard:** The target has little data, objective distances are listening proxies, and a postprocessor can improve one aspect while harming prosody.
- **Naive attempt:** Train a large TTS model directly on the small speaker set or add noise and assume naturalness follows.
- **Central move:** Generate training examples from high-resource speakers and train GAN or consistency-flow postprocessors selected for low-resource targets.
- **Mechanism:** Forward Tacotron features are refined by GAN and CFM postprocessors, then compared with listening and ranking tests.
- **Mathematical idea:** Proposed CFM reaches objective distance 0.27; listener scores are 79.8 proposed CFM and 74.8 proposed GAN versus reference 98.3.
- **What the paper reports:** Both proposed postprocessors improve reported naturalness; the CFM gain over its standard version is not significant.
- **Limits:** Two speakers, ground-truth prosody in part of evaluation, selected data, and reported tests limit arbitrary-voice claims.

## Boundary

The report contains 456 D3 notes with normalized taxonomy paths. It is a purposive full-paper seed, not a venue-wide prevalence estimate or independent reproduction.
