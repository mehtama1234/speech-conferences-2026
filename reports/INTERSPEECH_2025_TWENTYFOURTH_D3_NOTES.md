# INTERSPEECH 2025 twenty-fourth-pass full-paper notes

Eight official-PDF readings deepen variation, clinical context, representation, interpretability, multimodal resources, and category learning. Results are author-reported and not independently reproduced.

## 1. source-filter-production

**Paper:** [Speaker-specific Patterns of Phonetic Covariation in Korean Word-medial Stops and the Role of Phonological and Morphological Contexts](https://www.isca-archive.org/interspeech_2025/kwon25b_interspeech.html)
**Evidence:** D3; PDF SHA-256 `4586a1bbfc5da33b9f6a674b2ca31c0f6ee3fc3f43a803c4d4362a8404d37cc5`; full text captured.

- **Ordinary problem:** A speaker can pronounce the same category differently across sounds and contexts, yet listeners still need the category to remain recognizable.
- **Why hard:** Variation that looks random in one measurement may be coordinated with variation in another, and context can change both measurements at once.
- **Naive attempt:** Average across speakers and treat the remaining variation as noise.
- **Central move:** Measure several phonetic dimensions jointly within each speaker and test whether their covariation preserves category contrasts across phonological and morphological contexts.
- **Mechanism:** Seoul Korean word-medial stops are analyzed through speaker-specific distributions and covariation patterns across contexts.
- **Conceptual structure:** The object is a structured distribution, not one canonical pronunciation; correlations and category separation test whether variation is organized.
- **What paper reports:** The paper reports systematic speaker-specific covariation that keeps stop categories distinct despite contextual variability, supporting a phonetic-uniformity account.
- **Limits:** The language, stop system, contexts, speaker sample, and chosen phonetic measures bound the result; other languages and interactional settings require separate evidence.

## 2. source-filter-production-2

**Paper:** [Supralaryngeal Kinematics of Implosives in Central Vietnamese: An EMA Study](https://www.isca-archive.org/interspeech_2025/mcguire25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `0328292bb2732ab5a4cf9dbb087172fcce39b156ee19a5115dfeae3123bec4d8`; full text captured.

- **Ordinary problem:** To explain an implosive consonant, a researcher must connect its proposed airflow mechanism to the visible movements of the lips and timing of closure and release.
- **Why hard:** A voiced stop can resemble an implosive in a broad label, so a movement difference may be caused by voicing rather than implosivity.
- **Naive attempt:** Describe both sounds as voiced stops and assume the same articulatory timing.
- **Central move:** Track lip-aperture trajectories with electromagnetic articulography and compare Vietnamese implosives against voiced and voiceless controls in another language.
- **Mechanism:** EMA measures movement amplitude, velocity, and plateau timing during Central Vietnamese bilabial implosives; Taiwanese Southern Min controls the voicing explanation.
- **Conceptual structure:** The signal is a time course of gestures; mixed-effects comparisons separate a property of implosivity from a generic property of voicing.
- **What paper reports:** Implosives show greater peak velocity away from closure, while voiceless plosives have a longer gestural plateau; the voiced-plosive control does not reproduce the rapid movement.
- **Limits:** The languages, speakers, consonant inventory, EMA measures, and statistical model bound the result; laryngeal airflow itself was not directly measured.

## 3. metrics-and-targets-1

**Paper:** [Multimodal and Multitask Learning for Predicting Multiple Scores in L2 English Speech](https://www.isca-archive.org/interspeech_2025/oh25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `6e7efb566846da1e172e14e92b79e181fa40b88bec0b388604ffd7ca26065285`; full text captured.

- **Ordinary problem:** An assessment system should predict several aspects of second-language speaking ability while respecting that speech and words reveal different parts of performance.
- **Why hard:** A single score hides trait differences, while simply concatenating audio and text features can make one modality dominate or ignore relationships among traits.
- **Naive attempt:** Train one unimodal predictor or combine embeddings without modeling how the traits depend on each other.
- **Central move:** Use cross-modal attention to exchange information between speech and text and a joint loss that treats the five proficiency traits as related but distinct targets.
- **Mechanism:** MFCC, wav2vec 2.0, GloVe, and BERT embeddings are compared on five L2 English scores with a trait-aware loss and mean Pearson correlation as the main measure.
- **Conceptual structure:** The prediction target is a vector of human-assigned traits; cross-modal attention and the joint loss encode dependencies that a single aggregate score discards.
- **What paper reports:** The wav2vec 2.0 plus BERT configuration reports the best mean PCC, 0.734 with standard deviation 0.0129 across the five criteria, above unimodal and baseline multimodal systems.
- **Limits:** The learner dataset, rubric, rater scores, split, and correlation metric bound the result; correlation is not agreement or evidence that the model understands proficiency.

## 4. clinical-and-assistive-speech

**Paper:** [Optimizing Pause Context in Fine-Tuning Pre-trained Large Language Models for Dementia Detection](https://www.isca-archive.org/interspeech_2025/ke25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `ce626c00027b720202c96d268e3b2f47e7e8a2f997f9121db0884ef6800c42f6`; full text captured.

- **Ordinary problem:** A clinical speech detector may need to use pauses as signs of cognitive change without assuming that one duration threshold works for every language or recording protocol.
- **Why hard:** Pause meaning depends on where the pause occurs and how its duration is represented to a language model; the same insertion rule can help one task and hurt another.
- **Naive attempt:** Add every pause as a fixed token or use a threshold borrowed from another corpus.
- **Central move:** Insert between-segment pause context into automatic transcripts and tune the pause-duration representation for each classification task.
- **Mechanism:** Cantonese elderly speech from CU-Marvel is transcribed, pause context is fused into transformer input, and binary dementia tasks are compared under alternative pause groupings.
- **Conceptual structure:** The pause is treated as structured context attached to a linguistic boundary; classification accuracy and F1 test whether that context adds clinically useful signal.
- **What paper reports:** The paper reports that optimized between-segment pause patterns improve detection and that different tasks prefer different pause representations.
- **Limits:** The corpus, language, age group, transcription quality, diagnostic labels, and pause definitions bound the result; this is not a validated clinical biomarker or a causal account of dementia.

## 5. acoustic-unit-mapping

**Paper:** [EnCodecMAE: leveraging neural codecs for universal audio representation learning](https://www.isca-archive.org/interspeech_2025/pepino25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `67cdae8bdb5d2e3ec550583599e2729db1c21d2dfab7d1d66855579e7f702db9`; full text captured.

- **Ordinary problem:** One audio representation should support speech, music, and environmental sounds even though the useful information is different in each task.
- **Why hard:** A pretext target can make a representation good at reconstructing one signal while discarding information needed by another task.
- **Naive attempt:** Assume a larger model or a single input representation will be uniformly best everywhere.
- **Central move:** Use discrete targets from a neural codec in a masked autoencoder and test the representation across tasks, model sizes, input forms, self-training, and data mixtures.
- **Mechanism:** EnCodecMAE is pretrained on diverse audio and evaluated on pitch, genre, speech commands, emotion, sound events, and environmental sound tasks.
- **Conceptual structure:** Transfer performance is the test of usefulness; the representation is judged by how task, input, model size, and pretraining diversity change downstream accuracy or error.
- **What paper reports:** The paper reports average gains over prior audio representations and finds that larger models, task-dependent inputs, self-training, and diverse data each matter.
- **Limits:** The task suite, pretraining mixture, labels, model comparisons, and aggregate averages bound the claim; average transfer does not prove universal suitability for speech.

## 6. metrics-and-targets-2

**Paper:** [On the reliability of feature attribution methods for speech classification](https://www.isca-archive.org/interspeech_2025/shen25b_interspeech.html)
**Evidence:** D3; PDF SHA-256 `9d785cdeb27b44e907f9e9b4e81aefa37e3e086288839853c6ee3a02061b118f`; full text captured.

- **Ordinary problem:** An explanation of a speech classifier should identify evidence that genuinely changes the decision, not merely highlight plausible-looking waveform regions.
- **Why hard:** Speech unfolds in time, so the reliability of an attribution depends on the input representation, the size of the perturbed region, and whether the task is word-based or acoustic.
- **Naive attempt:** Apply a standard saliency map and interpret the highlighted frames as causal evidence.
- **Central move:** Vary input type, aggregation, and perturbation timespan, then compare attribution stability, faithfulness, and agreement across speech classification tasks.
- **Mechanism:** Experiments use TIMIT and Common Voice with gradient-based saliency and integrated gradients; word-aligned and fixed-timespan perturbations are compared.
- **Conceptual structure:** Attribution is an intervention-dependent measurement; agreement and error-based scores test whether highlighted regions are reliable under controlled perturbations.
- **What paper reports:** Standard approaches are generally unreliable in speech, except that word-aligned perturbations are more reliable for word-based classification tasks.
- **Limits:** The models, tasks, datasets, attribution methods, and reliability definitions bound the result; no explanation method becomes a causal proof from these tests alone.

## 7. low-resource-and-data-creation

**Paper:** [LiRI Corpus Platform: Demonstration of a Web-Based Infrastructure for Multimodal Corpus Analysis](https://www.isca-archive.org/interspeech_2025/vukovic25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `8f138214b31c0ab0e8ae7475e60931c664154f26806d0a9695ac60aa9b97096b`; full text captured.

- **Ordinary problem:** Researchers need to ask questions that connect speech, text, video, gesture, and annotation layers without rebuilding a separate tool for each corpus.
- **Why hard:** Multimodal data are time-aligned but stored and queried in different systems, so a text-only search can miss the speech or gesture event that gives a segment meaning.
- **Naive attempt:** Keep each modality in a separate application and manually synchronize results.
- **Central move:** Provide one corpus platform with a shared query language, synchronized audiovisual views, and layered annotation that can be queried across modalities.
- **Mechanism:** The LiRI Corpus Platform stores and explores multimodal corpora through DQD queries and time-aligned frontends for text, audio, video, gesture, and spoken transcripts.
- **Conceptual structure:** The central object is a cross-modal query over aligned annotation intervals; the platform is evaluated by the operations it makes expressible rather than by a classifier score.
- **What paper reports:** The paper demonstrates integrated storage, synchronized querying, layered annotation, and modality-specific frontends for multimodal corpus analysis.
- **Limits:** This is an infrastructure demonstration, not evidence that every corpus can be aligned or that research conclusions improve; supported formats, annotations, and user workflows are the boundary.

## 8. accent-and-cultural-boundaries

**Paper:** [The Role of Contextual Variation in Learning Cantonese Tones from Naturalistic Speech](https://www.isca-archive.org/interspeech_2025/zhao25j_interspeech.html)
**Evidence:** D3; PDF SHA-256 `1a5721799baa9c82b057c5f67cdfe3519a81dbd9242209ad3131a5bf5b0487f9`; full text captured.

- **Ordinary problem:** An infant must learn tonal categories even when the acoustic cues change with speaker, syllable, and surrounding context rather than repeating one stable value.
- **Why hard:** Complex tone contrasts may have no single invariant cue, so category learning must use how distributions change across contexts.
- **Naive attempt:** Search for one fixed acoustic threshold for each tone and treat contextual variation as noise.
- **Central move:** Compare the amount of contextual variation in naturalistic Cantonese speech with which tone contrasts are easier or harder to acquire.
- **Mechanism:** Naturalistic Cantonese productions are analyzed across six tonal contrasts and compared with existing acquisition findings under the Distributional Learning Across Contexts proposal.
- **Conceptual structure:** The learning signal is a distribution over contexts, not a single token; variation and acquisition difficulty are related at the contrast level.
- **What paper reports:** The paper reports that contextual variation can predict which Cantonese contrasts are easier or harder to learn when invariant cues are absent.
- **Limits:** The naturalistic corpus, tone system, acquisition comparison, and distributional measures bound the inference; a prediction from correspondence is not a direct infant-learning experiment.

