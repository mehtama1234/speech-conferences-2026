# INTERSPEECH 2025 twenty-seventh-pass full-paper notes

Six official-PDF readings form a deployment family around shared parameters, streaming, decoding sparsity, pruning, dynamic architecture, and one acoustic-to-phonological inference. Results are author-reported and not independently reproduced.

## 1. robustness-and-system-boundary-1

**Paper:** [Unfolding A Few Structures for The Many: Memory-Efficient Compression of Conformer and Speech Foundation Models](https://www.isca-archive.org/interspeech_2025/li25v_interspeech.html)
**Evidence:** D3; PDF SHA-256 `38d94d25adae57015cb261471e8788a565f54069396b0240d086459e5285c446`; full text captured.

- **Ordinary problem:** A speech recognizer must fit on a device with limited memory while retaining the behavior of a much larger model.
- **Why hard:** A separately compressed model can lose accuracy, while storing many depth variants defeats the memory goal.
- **Naive attempt:** Train one large model and prune or distill it after the fact into one fixed size.
- **Central move:** Train a small seed network and unfold it along multiple logical depths, using self-distillation to keep the paths consistent.
- **Mechanism:** A compact Conformer or Transformer seed is repeatedly unfolded during joint training and compared with larger Conformer and wav2vec2/HuBERT systems.
- **Conceptual structure:** Depth becomes a reusable path through shared parameters; KL divergence constrains the smallest and largest paths so compression is measured against performance, storage, and model depth.
- **What paper reports:** The foldable model reduces Conformer parameters by 35% and speech-foundation parameters by 30% without reported performance loss across depth configurations.
- **Limits:** The architectures, training data, depth choices, and compression comparisons bound the claim; parameter reduction is not the same as lower device latency or energy.

## 2. robustness-and-system-boundary-2

**Paper:** [SpecTokenizer: A Lightweight Streaming Codec in the Compressed Spectrum Domain](https://www.isca-archive.org/interspeech_2025/wan25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `796d66ded7e7560ac4e6a34bd3234e09319288a8e26fadc9c401159c0e1ee435`; full text captured.

- **Ordinary problem:** An audio codec for a streaming device must compress speech into a small code while operating with little computation and little delay.
- **Why hard:** Heavy neural codecs may compress well but require too many parameters or operations for a real-time device.
- **Naive attempt:** Take a large offline codec and accept its compute cost, or reduce layers without changing the representation domain.
- **Central move:** Operate in a compressed spectral domain and combine lightweight convolutional and recurrent layers at multiple time scales.
- **Mechanism:** SpecTokenizer is a streaming single-codebook codec evaluated at 4 kbps against a lightweight codec under matched computation and storage budgets.
- **Conceptual structure:** The codec trades waveform detail for discrete codes; bitrate, reconstruction quality, computation, and parameter count expose the deployment boundary.
- **What paper reports:** At 4 kbps it reports comparable or better performance with 20% of the computation and 10% of the parameters of the comparison codec.
- **Limits:** Bitrate, audio material, hardware, streaming definition, and quality measure bound the claim; benchmark efficiency does not prove end-to-end device power or user benefit.

## 3. robustness-and-system-boundary-3

**Paper:** [WIND: Accelerated RNN-T Decoding with Windowed Inference for Non-blank Detection](https://www.isca-archive.org/interspeech_2025/xu25c_interspeech.html)
**Evidence:** D3; PDF SHA-256 `f6522e777465a4261b00105d672dbbef2e3fc6336bec7bef1e8f6042b2512000`; full text captured.

- **Ordinary problem:** An RNN-T recognizer must decide quickly when a frame contains a label, but sequentially inspecting every frame wastes time when most frames are blank.
- **Why hard:** Parallelizing blindly can change the order-dependent decoder state and harm word accuracy.
- **Naive attempt:** Run the original sequential decoder faster in isolation or process every frame in a large batch without respecting non-blank decisions.
- **Central move:** Inspect a window of frames in parallel to locate non-blank predictions, then retain decoder logic around the informative positions for greedy and beam search.
- **Mechanism:** WIND is evaluated on multiple datasets with greedy, batched greedy, and beam-search RNN-T decoding against sequential baselines.
- **Conceptual structure:** The method exploits sparsity in the label stream; speedup is meaningful only when WER remains unchanged and the decoding mode is specified.
- **What paper reports:** Greedy modes reach up to 2.4x speedup with identical WER, while the proposed beam search is faster and slightly more accurate than alternatives.
- **Limits:** RNN-T models, datasets, hardware, window size, and decoding modes bound the result; reported speedup is not portable to every implementation or workload.

## 4. robustness-and-system-boundary-4

**Paper:** [Effective and Efficient One-pass Compression of Speech Foundation Models Using Sparsity-aware Self-pinching Gates](https://www.isca-archive.org/interspeech_2025/xu25e_interspeech.html)
**Evidence:** D3; PDF SHA-256 `a9efd05ab02ed6d19849538cfd73c2d842f53abd9bf78e6b0037d4b399fd067b`; full text captured.

- **Ordinary problem:** A speech foundation model may be accurate but too large to deploy, so its unused capacity must be removed without damaging recognition.
- **Why hard:** Pruning after training can be expensive and can remove units that are useful only in combination with others.
- **Naive attempt:** Prune fixed layers with a hand rule or compress the model in a separate stage after all training is finished.
- **Central move:** Learn a small gate for each layer during training and let the gates pinch off underused neurons while model parameters are updated at the same time.
- **Mechanism:** Self-pinching gates are trained with wav2vec2.0-base and HuBERT-large and then drive fine-grained neuron pruning on LibriSpeech-100hr.
- **Conceptual structure:** A gate is a learned resource-allocation decision; parameter count, WER, compression ratio, and compression time measure the accuracy-efficiency frontier.
- **What paper reports:** The method removes 65% of wav2vec2.0-base and 60% of HuBERT-large parameters without a statistically significant test-clean WER increase, with 7.05% WER at 4.26x compression.
- **Limits:** LibriSpeech, model variants, pruning thresholds, and test-clean evaluation bound the result; no claim follows about noisy conditions, energy, or other languages.

## 5. robustness-and-system-boundary-5

**Paper:** [Dynamic Acoustic Model Architecture Optimization in Training for ASR](https://www.isca-archive.org/interspeech_2025/xu25i_interspeech.html)
**Evidence:** D3; PDF SHA-256 `2c502635795e3d85856d7ebf4129960ed0a10bc772ce6407669c3ad0680c2069`; full text captured.

- **Ordinary problem:** An ASR model has a fixed training budget, but not every part of its architecture uses that budget equally well.
- **Why hard:** Hand-designed architectures require expertise, while neural architecture search can spend more computation searching than training the final model.
- **Naive attempt:** Choose one repeated block structure before training or run an expensive search over many complete models.
- **Central move:** Grow useful parts and drop less useful parts during training, reallocating parameters while keeping the total model complexity and training resources fixed.
- **Mechanism:** DMAO is evaluated with CTC on LibriSpeech, TED-LIUM-v2, and Switchboard across architectures and model sizes.
- **Conceptual structure:** The architecture becomes a changing allocation of parameters; relative WER at matched resources tests whether reallocation, rather than extra capacity, creates the gain.
- **What paper reports:** The paper reports up to roughly 6% relative WER improvement across datasets, architectures, and sizes with negligible added training overhead.
- **Limits:** Datasets, CTC setup, compute budget, search rules, and final architecture bound the result; a benchmark gain does not establish optimality or universal resource allocation.

## 6. source-filter-production

**Paper:** [Temporal organization of prenuclear glides in Hefei Mandarin](https://www.isca-archive.org/interspeech_2025/yang25i_interspeech.html)
**Evidence:** D3; PDF SHA-256 `ee4f070b66cbac5bcdcf876ab944c98617be3dc6db4525bb82ae0b7c72c34161`; full text captured.

- **Ordinary problem:** A short glide between a consonant and vowel must be assigned to a syllable position, but timing can make it look like an onset, a nucleus, or a separate segment.
- **Why hard:** Abstract phonological structure is not directly visible in the waveform, and competing analyses can fit the same sequence of labels.
- **Naive attempt:** Choose an onset or rime analysis from spelling, phonotactics, or a single duration measurement.
- **Central move:** Measure the timing coordination of consonant-glide-vowel sequences and use the relative movement of gestures to infer which part of the syllable the glide behaves like.
- **Mechanism:** Hefei Mandarin CjV and CwV syllables are analyzed acoustically, comparing glide timing with competing onset and rime accounts.
- **Conceptual structure:** The acoustic trajectory is evidence about an abstract structure; temporal coordination links measurable events to a phonological hypothesis without treating labels as observations.
- **What paper reports:** The paper finds that both glides are more likely part of the rime, agreeing with prior evidence for [j] but differing from earlier results for [w].
- **Limits:** The dialect, speakers, acoustic method, and competing analyses bound the inference; timing alone cannot settle every phonological representation or generalize across Mandarin varieties.

