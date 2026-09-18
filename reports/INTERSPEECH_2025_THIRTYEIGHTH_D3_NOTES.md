# INTERSPEECH 2025 thirty-eighth-pass full-paper notes

Eight official-PDF readings deepen articulatory planning, low-latency echo cancellation, latent concept formation, emotion adaptation, class-incremental learning, continual deepfake detection, nonverbal separation, and Haitian Creole modeling.

## 1. source-filter-production

**Paper:** [Articulatory modeling of the S-shaped F2 trajectories observed in Öhman's spectrographic analysis of VCV syllables](https://www.isca-archive.org/interspeech_2025/berthommier25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `036c4dfde7eb6ac0796fa87e90fbd8153f2d92b6608a48dcb1dbf4f819698db6`; full text captured.

- **Ordinary problem:** Explain why the second formant bends in an S shape while a speaker moves through vowel-consonant-vowel syllables.
- **Why hard:** The acoustic trajectory reflects several moving articulators and planning regimes; a purely acoustic curve does not say which physical movement caused it.
- **Naive attempt:** Fit a curve to the spectrogram and treat the curve as a direct articulatory law.
- **Central move:** Generate the same VCV sequences with an articulatory model, separate vowel transitions from consonant influence, and compare the resulting trajectories and locus equations.
- **Mechanism:** The study uses the Maeda articulatory model to reproduce Öhman's S-shaped F2 trajectories and reassesses conventional locus-equation interpretations.
- **Conceptual structure:** The acoustic pattern is an effect of coordinated movement: a model can test whether the pattern follows from planning constraints rather than treating it as an unexplained spectral shape.
- **What paper reports:** The paper reports synthetic trajectories resembling the observed sequences and structured effects of articulatory planning.
- **Limits:** Model geometry, trajectory planning, corpus, and synthetic-to-observed comparison limit claims; matching a trajectory does not identify a unique human motor plan.

## 2. echo-and-reconstruction

**Paper:** [Extended Loss: Incorporating Long Context into Training Models when using Short Audio Frames](https://www.isca-archive.org/interspeech_2025/dinh25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `c9b4b8d80caa6c5af43e9d12e87173c3dbc5f55c5d7ef28ab9d8e3a45f31bc37`; full text captured.

- **Ordinary problem:** A real-time echo canceller may process only 10-ms frames, but each frame still needs enough surrounding context to avoid audible boundary glitches.
- **Why hard:** Long context can improve continuity but usually adds delay; short-frame training exposes boundaries that long offline examples hide.
- **Naive attempt:** Use long frames, add post-processing, or train on isolated short chunks and accept discontinuities.
- **Central move:** Keep long-context information in each training batch while producing short-frame outputs, so the model learns continuity without increasing application delay.
- **Mechanism:** The paper proposes Extended Loss for acoustic echo cancellation with short audio frames and limited latency.
- **Conceptual structure:** The loss supervises the local output using context that spans frame boundaries; training context and inference delay are separated rather than traded as the same quantity.
- **What paper reports:** The paper reports reduced boundary discontinuities and improved short-frame AEC performance under the tested real-time conditions.
- **Limits:** Echo paths, frame size, batch context, hardware, and evaluation signals bound the claim; continuity on the benchmark is not proof of every room or device.

## 3. grounding-and-action

**Paper:** [From Words to Waves: Analyzing Concept Formation in Speech and Text-Based Foundation Models](https://www.isca-archive.org/interspeech_2025/ersoy25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `94dbe85e2eca531544c854db522bc0d7719db94a38cc1d775d68e548153f05f8`; full text captured.

- **Ordinary problem:** Speech models may represent concepts differently from text models, and a joint model may combine or distort those structures rather than simply inheriting text knowledge.
- **Why hard:** Latent concepts are not directly labeled; comparing modalities requires a method that exposes structure without pretending an interpretation is a measured neuron-level fact.
- **Naive attempt:** Inspect nearest words or report downstream accuracy and call the result a theory of concept formation.
- **Central move:** Use latent concept analysis to compare speech-only, text-only, and joint foundation models and ask which conceptual structures are shared or modality-specific.
- **Mechanism:** The paper analyzes concept formation in speech and text-based foundation models using an unsupervised latent-concept method.
- **Conceptual structure:** Concept formation is treated as a representation-comparison problem: the analysis proposes interpretable structure, while cross-modal differences reveal what the training signal makes easy or hard to encode.
- **What paper reports:** The paper reports comparative latent conceptual structures across speech, text, and joint models.
- **Limits:** Model choice, layer, analysis method, prompts, and human interpretation bound the claim; a latent cluster is not automatically a human concept.

## 4. dialogue-and-turn-taking

**Paper:** [MMLoRA: Multitask Memory Parameter-Efficient Fine-Tuning for Multimodal SER](https://www.isca-archive.org/interspeech_2025/fang25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `30cc30ac8f29663f4e76529b9ba2f9d15abaa2c50ba9416bbf7e45c4119a160a`; full text captured.

- **Ordinary problem:** Emotion recognition should generalize when people express the same emotion differently, across audio and other modalities and across related tasks.
- **Why hard:** Individual expression varies with speaker, gender, context, and modality; a parameter-efficient update can share too little or force unrelated tasks together.
- **Naive attempt:** Use one shared LoRA update or train a separate full model for every emotion task.
- **Central move:** Combine shared LoRA experts, task-specific experts, a memory mechanism, and gender as an auxiliary task to separate common structure from expression-specific variation.
- **Mechanism:** MMLoRA is a multitask memory parameter-efficient method for multimodal speech emotion recognition.
- **Conceptual structure:** The adaptation has two roles: shared parameters carry reusable affective structure, while expert and memory paths preserve task/person-specific differences instead of overwriting them.
- **What paper reports:** The paper reports improved multimodal SER generalization over the tested parameter-efficient baselines.
- **Limits:** Datasets, gender labels, task mix, memory policy, modalities, and expression cultures bound the result; auxiliary gender is not a complete model of individual variation.

## 5. low-resource-and-data-creation

**Paper:** [Multi-view Fusion and Parameter Perturbation for Few-Shot Class-Incremental Audio Classification](https://www.isca-archive.org/interspeech_2025/fang25d_interspeech.html)
**Evidence:** D3; PDF SHA-256 `ae7de64989102b169031e6e41dfaf5444fbb603a12d215d472122244a415cf27`; full text captured.

- **Ordinary problem:** An audio classifier may need to learn new classes one at a time with only a few examples, without forgetting classes it already knows.
- **Why hard:** The class vocabulary changes and few examples encourage overfitting; a representation that works for old classes may not expose the right view for new ones.
- **Naive attempt:** Fine-tune on each new class and accept forgetting, or keep fixed prototypes and ignore representation drift.
- **Central move:** Fuse multiple views of the audio and perturb parameters during few-shot class-incremental learning to improve coverage and reduce overfitting.
- **Mechanism:** The paper proposes multi-view fusion and parameter perturbation for few-shot class-incremental audio classification.
- **Conceptual structure:** Adaptation is a balance between plasticity and retention: multiple views supply evidence while controlled perturbation tests whether a decision is stable rather than memorized.
- **What paper reports:** The paper reports class-incremental classification results against the tested baselines.
- **Limits:** Class order, shots, audio domains, perturbation settings, and memory protocol bound the result; benchmark retention does not establish lifelong robustness.

## 6. privacy-security-and-accountability

**Paper:** [Rehearsal with Auxiliary-Informed Sampling for Audio Deepfake Detection](https://www.isca-archive.org/interspeech_2025/febrinanto25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `e7c8f80a9dce5915880b52224a96390ec7edfdc489821c7023125208a625d0f3`; full text captured.

- **Ordinary problem:** A deepfake detector must learn new attack types while remembering older ones, even when its memory buffer can hold only a small sample of past audio.
- **Why hard:** Uniform rehearsal misses rare acoustic characteristics and can make the buffer biased toward easy or common examples.
- **Naive attempt:** Store random old clips or retrain from scratch whenever a new attack appears.
- **Central move:** Generate auxiliary labels describing audio characteristics and use them to sample a more diverse rehearsal memory during continual learning.
- **Mechanism:** RAIS uses auxiliary-informed sampling for rehearsal-based continual audio-deepfake detection.
- **Conceptual structure:** The memory is selected for coverage of acoustic factors, not only class labels; retaining varied evidence helps the detector update without collapsing onto the newest attack.
- **What paper reports:** The paper reports improved continual deepfake detection over rehearsal baselines on new attacks.
- **Limits:** Attack families, auxiliary-label quality, buffer size, stream order, and detector threshold bound the result; no finite memory guarantees future attack coverage.

## 7. prosody-and-interactive-control

**Paper:** [DnR-nonverbal: Cinematic Audio Source Separation DatasetContaining Non-Verbal Sounds](https://www.isca-archive.org/interspeech_2025/hasumi25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `2a85e203d77f60fd2faa610729b1647c07ebcdd96bf073be90643533ba17a5b4`; full text captured.

- **Ordinary problem:** A cinematic separator should keep laughter and screams with the speech stem, because acted nonverbal voice is part of a scene rather than an ordinary sound effect.
- **Why hard:** Existing datasets often contain read speech, so a model can learn the wrong boundary and remove emotionally heightened vocal sounds as noise or effects.
- **Naive attempt:** Train on reading-style stems and assume the separator's speech category matches film dialogue.
- **Central move:** Build a dataset whose speech stem includes nonverbal vocalizations and test whether that changes separation behavior on cinematic mixtures.
- **Mechanism:** DnR-nonverbal is a cinematic audio source-separation dataset containing laughter, screams, and other nonverbal sounds in the speech stem.
- **Conceptual structure:** The dataset changes the category definition presented to the model: the target is a vocal event in context, not a narrow phonetic transcript.
- **What paper reports:** The paper reports that conventional separators mishandle nonverbal sounds and that the new dataset improves the tested synthetic separation task.
- **Limits:** Synthetic mixtures, labels, scene distribution, separator, and nonverbal taxonomy bound the result; real-film generalization remains open.

## 8. multilingual-and-crosslingual

**Paper:** [Self-Supervised Models of Speech Processing for Haitian Creole](https://www.isca-archive.org/interspeech_2025/havard25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `01411ac842a7947006c8437a42cce36fff901d0d86dd4af5cb15d6627e313a0c`; full text captured.

- **Ordinary problem:** Haitian Creole needs speech models trained on its own sounds and data, not only a large multilingual model that may underrepresent its structure.
- **Why hard:** Large multilingual pretraining can help but may encode data imbalance; training a monolingual model from scratch costs data and compute and must be compared fairly.
- **Naive attempt:** Fine-tune a multilingual checkpoint and assume scale always beats language-specific training.
- **Central move:** Pretrain monolingual self-supervised models for Haitian Creole, compare them with multilingual and French-based models, and fine-tune all for ASR.
- **Mechanism:** The paper develops self-supervised speech-processing models for Haitian Creole and compares monolingual, multilingual, and French-derived initialization.
- **Conceptual structure:** Representation quality depends on language fit as well as parameter count; a smaller language-specific model can win when its pretraining signal matches the target speech.
- **What paper reports:** The paper reports monolingual models that are competitive with or surpass larger multilingual alternatives on the tested ASR tasks.
- **Limits:** Data volume, speakers, orthography, model size, pretraining compute, and evaluation domain limit generalization to the broader Creole speech community.

