# INTERSPEECH 2025 thirty-seventh-pass full-paper notes

Eight official-PDF readings deepen low-resource data generation, articulatory inversion, missing-modality emotion recognition, singing vibrato control, short-utterance language ID, spoofing, speaker frontends, and clinical hallucination diagnosis.

## 1. low-resource-and-data-creation

**Paper:** [Evaluating Large Language Models in Data Generation for Low-Resource Scenarios: A Case Study on Question Answering](https://www.isca-archive.org/interspeech_2025/arisoy25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `bd94133ab93c4b82d4218f8da7999e2f3f4a68d5f6f980763c8520bb83cb0c5b`; full text captured.

- **Ordinary problem:** A spoken question-answering system needs training examples even when a language has little labeled data.
- **Why hard:** Synthetic text can be plentiful but may not resemble spoken questions; gains can come from artifacts or from better coverage, and the two must be separated.
- **Naive attempt:** Generate arbitrary question-answer pairs or train only on the small human set and assume more text automatically transfers to speech.
- **Central move:** Use large-language-model-generated question-answer data and test its value separately on text QA, spoken QA, and Turkish spoken QA.
- **Mechanism:** The study evaluates LLM-generated data for low-resource spoken QA across SQuAD, Spoken SQuAD, and Turkish spoken QA.
- **Conceptual structure:** Data generation is a controlled source of coverage: the useful question is not whether synthetic examples look plausible, but whether they improve the target speech task under restricted human supervision.
- **What paper reports:** The paper reports relative F1 gains over restricted human-annotated training in the tested text and spoken QA settings.
- **Limits:** Prompting, filtering, language, synthetic distribution, and evaluation splits limit transfer; synthetic gains do not establish factual or linguistic quality everywhere.

## 2. source-filter-production

**Paper:** [Reconstruction of the Complete Vocal Tract Contour Through Acoustic to Articulatory Inversion Using Real-Time MRI Data](https://www.isca-archive.org/interspeech_2025/azzouz25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `a96e9463c75424f8f86fcd9e2fa2b202474fe14000aadc19d11ac7a939a16571`; full text captured.

- **Ordinary problem:** We want to infer how the entire vocal tract moves from sound, including hidden parts such as the velum and glottis.
- **Why hard:** Acoustics are an indirect and many-to-one view of articulation; different configurations can produce similar sound, and real-time MRI labels are expensive.
- **Naive attempt:** Infer only easily sensed articulators or use a small sensor-based corpus and extrapolate to the full tract.
- **Central move:** Train acoustic-to-articulatory models against complete vocal-tract contours from real-time MRI and compare individual and joint articulator prediction.
- **Mechanism:** The paper reconstructs the complete vocal-tract contour from acoustic input using real-time MRI data and bidirectional recurrent models.
- **Conceptual structure:** The problem is inverse measurement: the model estimates hidden physical configuration from its acoustic consequence, so pixel-scale error and anatomical coverage matter as much as waveform fit.
- **What paper reports:** The paper reports average contour RMSE near the MRI pixel size on its test set.
- **Limits:** Speakers, MRI protocol, segmentation, speech styles, and model assumptions limit generalization; contour accuracy is not a complete articulatory theory.

## 3. echo-and-reconstruction

**Paper:** [Modality-Agnostic Multimodal Emotion Recognition using a Contrastive Masked Autoencoder](https://www.isca-archive.org/interspeech_2025/chochlakis25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `0fd014ca8ee889c503cf4d3fc3171f05001ac465e09b261005c8f5d82491a013`; full text captured.

- **Ordinary problem:** Emotion recognition should continue working when a camera, transcript, or other modality is missing rather than failing because the training setup expected every input.
- **Why hard:** Modalities are correlated but not interchangeable; reconstruction can fill a missing channel while also inventing information that was never observed.
- **Naive attempt:** Train separate models for every modality combination or drop examples with missing inputs.
- **Central move:** Align modalities contrastively and use masked reconstruction in one modality-agnostic model, then test unimodal, multimodal, and missing-modality cases.
- **Mechanism:** The paper proposes a contrastive masked-autoencoder model for modality-agnostic multimodal emotion recognition on MSP-Podcast.
- **Conceptual structure:** The model learns shared structure while treating missingness as a normal observation condition; reconstruction supplies a bridge, but prediction must still be judged against the available evidence.
- **What paper reports:** The paper reports improvements over unimodal and multimodal baselines and robustness to missing modalities.
- **Limits:** Corpus, emotion labels, missingness pattern, modality quality, and reconstruction objective bound the claim; emotion inference is not guaranteed to be socially reliable.

## 4. prosody-and-interactive-control

**Paper:** [VibE-SVC: Vibrato Extraction with High-frequency F0 Contour for Singing Voice Conversion](https://www.isca-archive.org/interspeech_2025/choi25e_interspeech.html)
**Evidence:** D3; PDF SHA-256 `453ae8c915b076539864a14d364b60a6162dc333e728f8de03b3f831dc4e241d`; full text captured.

- **Ordinary problem:** A singing voice converter should transfer vibrato deliberately because vibrato carries style and emotion, but it must preserve the singer's identity and the song's content.
- **Why hard:** Vibrato is a fast variation within the fundamental-frequency contour, so treating it as undifferentiated pitch can make it hard to extract or control.
- **Naive attempt:** Leave vibrato entangled in the pitch representation or control it with a single average F0 value.
- **Central move:** Separate high-frequency F0 variation with a wavelet transform, then explicitly transfer and control the vibrato component during conversion.
- **Mechanism:** VibE-SVC extracts vibrato from the high-frequency F0 contour for controllable singing voice conversion.
- **Conceptual structure:** Style becomes an editable signal component: the system changes a time-varying pitch pattern while preserving the slower melody and speaker identity.
- **What paper reports:** The paper reports objective and subjective evidence for high-quality conversion, style control, and speaker similarity.
- **Limits:** Singers, songs, vibrato ranges, extraction errors, and evaluation conditions limit generalization; explicit control does not guarantee a preferred artistic result.

## 5. multilingual-and-crosslingual

**Paper:** [Teacher-Free Knowledge Distillation for Improving Short-Utterance Spoken Language Identification](https://www.isca-archive.org/interspeech_2025/dey25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `78db88d105829c906b85d927be18e04cfee1df9e5ec2ae017f20f676000e4015`; full text captured.

- **Ordinary problem:** Language identification must work on very short speech, where two seconds may contain fillers, overlap, names, or even no speech.
- **Why hard:** A separate teacher model is expensive, and ordinary hard labels do not express uncertainty among languages or the fact that a segment may be out of scope.
- **Naive attempt:** Train on hard language labels only or distill from a large teacher and ignore the particular errors caused by short segments.
- **Central move:** Use online soft labels from correctly classified training segments, with dynamic weighting, conditional updates, and entropy-based uncertainty, without a separate teacher.
- **Mechanism:** The paper proposes teacher-free knowledge distillation for short-utterance spoken language identification.
- **Conceptual structure:** The soft target is an accumulated view of what the model reliably knows; uncertainty and segment quality shape how much each example changes the decision boundary.
- **What paper reports:** The paper reports consistent Cavg improvements in same-corpus and cross-corpus short-utterance evaluations.
- **Limits:** Languages, out-of-scope composition, duration, label updates, and corpora bound the result; better short-segment ID does not solve open-set detection generally.

## 6. privacy-security-and-accountability

**Paper:** [Can Quantized Audio Language Models Perform Zero-Shot Spoofing Detection?](https://www.isca-archive.org/interspeech_2025/dutta25b_interspeech.html)
**Evidence:** D3; PDF SHA-256 `701c8eb0461749aed0076b23f36383c6ffc9ed975b7cc18bfda9aa46270bb0c7`; full text captured.

- **Ordinary problem:** A compact audio language model should detect spoofed speech without turning every unfamiliar recording into a spoof, even after quantization for deployment.
- **Why hard:** Zero-shot models can have strong-looking accuracy while carrying a severe class bias; quantization changes internal precision but may not be the main failure.
- **Naive attempt:** Report aggregate accuracy on clean data and assume FP16 or INT8 preserves the task behavior.
- **Central move:** Evaluate several audio language models across spoof datasets and precisions, inspecting class bias and practical discrimination rather than accuracy alone.
- **Mechanism:** The paper tests quantized audio language models for zero-shot spoofing detection on ASVspoof2019, In-the-Wild, and WaveFake.
- **Conceptual structure:** Deployment compression and task validity are separate questions: a model may retain its behavior after quantization while that behavior is already a biased near-random decision rule.
- **What paper reports:** The paper reports negligible FP16 degradation but severe spoof-prediction bias that undermines practical detection.
- **Limits:** Models, datasets, thresholds, quantization methods, and zero-shot prompts bound the claim; tested robustness is not security certification.

## 7. speaker-characteristics

**Paper:** [Analysis of ABC Frontend Audio Systems for the NIST-SRE24](https://www.isca-archive.org/interspeech_2025/barahona25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `cf760325e19e2f71107224591b5f91b2602db58ef9c2ed548c860168c374e915`; full text captured.

- **Ordinary problem:** Speaker embeddings for conversational telephone speech need to work across speakers and languages under a fixed or open training-data rule.
- **Why hard:** Frontend architecture, pooling, pretraining, and training data all change the speaker geometry; a benchmark comparison can hide which component caused an improvement.
- **Naive attempt:** Choose one embedding architecture or use a large pretrained model without separating data condition, pooling, and domain effects.
- **Central move:** Analyze several frontend families and pooling choices under the NIST SRE24 fixed and open conditions, including multilingual training data.
- **Mechanism:** The paper analyzes ABC frontend audio systems for the NIST SRE24 audio track.
- **Conceptual structure:** The frontend is a measurement pipeline: representation, temporal pooling, training population, and domain match jointly determine whether identity survives telephone speech.
- **What paper reports:** The paper reports comparative robustness and performance for the explored architectures and data conditions.
- **Limits:** NIST protocol, telephone channel, language mix, training-data access, and calibration limit claims beyond the benchmark.

## 8. grounding-and-action

**Paper:** [Fact-Controlled Diagnosis of Hallucinations in Medical Text Summarization](https://www.isca-archive.org/interspeech_2025/bn25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `a4c0a8b359d71c896758b1380dfed179ed3b2fc39a1a03e1d7e2dea089e5d012`; full text captured.

- **Ordinary problem:** A medical summarizer may invent a fact about a patient-clinician conversation, so a detector needs controlled examples as well as naturally occurring failures.
- **Why hard:** Hallucinations are rare and variable; general-domain detectors may confuse missing evidence with a false claim, especially when the source is speech-derived clinical dialogue.
- **Naive attempt:** Evaluate only on generic hallucination data or label summaries without controlling which source fact was removed.
- **Central move:** Construct a fact-controlled leave-one-out dataset and a natural hallucination dataset, then compare detection methods in the clinical setting.
- **Mechanism:** The paper studies fact-controlled diagnosis of hallucinations in medical text summarization from patient-clinician dialogues.
- **Conceptual structure:** A controlled deletion makes the missing fact known, while natural cases test ecological validity; the two together separate detector sensitivity from dataset artifacts.
- **What paper reports:** The paper reports that general-domain detectors struggle on clinical hallucinations and evaluates specialized diagnostic approaches.
- **Limits:** Synthetic deletion, clinical language, annotation, summarizer, and detector thresholds limit generalization; detection is not prevention or clinical validation.

