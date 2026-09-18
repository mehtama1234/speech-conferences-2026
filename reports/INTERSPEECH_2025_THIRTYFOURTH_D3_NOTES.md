# INTERSPEECH 2025 thirty-fourth-pass full-paper notes

Eight official-PDF readings deepen experienced communication difficulty, relational speaker verification, dialect translation, rhythm-based clinical acoustics, face/text-controlled TTS, social voice perception, one-shot singing conversion, and contextual rare-word retrieval. Results remain author-reported and were not independently reproduced.

## 1. human-centered-evaluation

**Paper:** [Does effortful speech production indicate communication difficulty caused by noise and hearing aid support?](https://www.isca-archive.org/interspeech_2025/huttner25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `2b187da4f34acbce51b19459ad28b8304cdfc16e165ab62e180777e42623d22a`; full text captured.

- **Ordinary problem:** Communication difficulty is a lived interactional problem: noise, hearing loss, hearing aids, and the effort of speaking may change how successfully two people can coordinate.
- **Why hard:** A person's vocal level or turn-taking behavior can reflect both the acoustic environment and the person's adaptation, so a single acoustic measure cannot be assumed to equal experienced difficulty.
- **Naive attempt:** Measure hearing thresholds or speech level alone and use them as a proxy for how hard the conversation felt.
- **Central move:** Record paired conversations across quiet/noise and hearing-aid conditions, collect participants' difficulty judgments, and test which speech and interaction measures predict those judgments.
- **Mechanism:** The study pairs 44 normal-hearing and hearing-impaired participants in task-based conversations in quiet and 70 dB noise, with the hearing-impaired group tested with and without hearing aids; F1, vocal level, and turn-taking variability are modeled against questionnaires.
- **Conceptual structure:** The target is a human report conditioned on dyad, noise, device, and turn structure; regression links observable speech behavior to experience while keeping the experience measure distinct from the signal.
- **What paper reports:** The paper reports that higher vocal level and interaction measures predict communication difficulty for hearing-impaired participants under relevant conditions.
- **Limits:** Small dyadic sample, task design, questionnaire, hearing-aid settings, and acoustic noise bound the result; a predictor of reported difficulty is not a universal clinical measure or causal explanation.

## 2. source-separation-and-spatial-listening

**Paper:** [IDIR: Identifying and Distilling Informative Relations for Speaker Verification](https://www.isca-archive.org/interspeech_2025/gan25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `b2e8c43f6e9f6ba654abf838dfaeb05e128c894d0dc997b29d6881b435daec17`; full text captured.

- **Ordinary problem:** A compact speaker-verification model should retain who spoke when compressed from a large teacher, but copying each hidden feature can miss the structure of how speakers relate to one another.
- **Why hard:** Speaker identity is relational: the distance between two voices matters, and a student with less capacity cannot reproduce every teacher coordinate while preserving all useful pairwise distinctions.
- **Naive attempt:** Match the student's feature vector to the teacher's vector one example at a time or shrink the network and accept a loss of speaker separation.
- **Central move:** Distill informative within-speaker and between-speaker relations, then add a margin that pulls same-speaker pairs together and pushes different-speaker pairs apart.
- **Mechanism:** IDIR identifies informative relations in each mini-batch, distills them from teacher to student, and uses margin-adjusted similarity scores for speaker verification.
- **Conceptual structure:** The object being transferred is a geometry of identities rather than a list of feature values; similarity and verification thresholds test whether that geometry survives compression.
- **What paper reports:** The paper reports improved speaker-verification performance over feature-matching distillation and stronger separation of same- and different-speaker relations.
- **Limits:** Teacher/student architectures, pair mining, margin, dataset, and verification protocol bound the claim; relational distillation does not ensure robustness to domain, overlap, or fairness shifts.

## 3. accent-and-cultural-boundaries

**Paper:** [Speech transcription from South Tyrolean Dialect to Standard German with Whisper](https://www.isca-archive.org/interspeech_2025/ducceschi25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `c40f366bf4f1446b8639b6f03ade3b384876d4248de44b697bbcb21c726fb18d`; full text captured.

- **Ordinary problem:** An archive may contain South Tyrolean dialect speech while the useful public output must be Standard German subtitles or translations; a recognizer trained on standard speech may miss the dialect before translation begins.
- **Why hard:** Dialect pronunciation, vocabulary, and grammar differ from the data used to train a general ASR system, and a small corpus makes it hard to learn all of those differences.
- **Naive attempt:** Run an off-the-shelf recognizer and translate its errors, or collect only standard-German speech and assume dialect variation is small.
- **Central move:** Build manually annotated and synthetic dialect data, fine-tune Whisper for the dialect-to-standard text mapping, and evaluate the actual archival translation task.
- **Mechanism:** The paper fine-tunes Whisper for South Tyrolean dialect speech to Standard German text, uses a small manually annotated plus synthetic corpus, and optimizes the task for archival audiovisual material.
- **Conceptual structure:** Recognition and translation are coupled in the output contract: the model need not first produce a standard transcript if training directly links dialect audio to standard written text; BLEU and error measures test the product.
- **What paper reports:** The paper reports a BLEU score of 86.18 and substantial improvement over its baselines, with an existing heritage-archive use case.
- **Limits:** Small corpus, synthetic data, dialect region, reference translations, BLEU, and deployment domain bound the claim; high translation score does not establish coverage of every speaker or dialect context.

## 4. time-frequency-measurement

**Paper:** [Leveraging AM and FM Rhythm Spectrograms for Dementia Classification and Assessment](https://www.isca-archive.org/interspeech_2025/gogoi25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `1c923b4ab7f5326abb9ce89d4baedc72b6accf41838364c0a8883628155b8b83`; full text captured.

- **Ordinary problem:** Dementia-related speech changes can unfold over long time scales in rhythm and coordination, so a short spectral snapshot may miss the signal clinicians or researchers need.
- **Why hard:** Long speech mixes linguistic content, speaker differences, pauses, and rhythm; handcrafted acoustic features may miss long modulation patterns while a large multimodal model may be hard to interpret.
- **Naive attempt:** Use standard short-window spectral features or treat every long recording as one undifferentiated waveform.
- **Central move:** Represent amplitude and frequency modulation rhythms as spectrograms, compare interpretable handcrafted summaries with a learned fusion of acoustic and linguistic representations.
- **Mechanism:** The study derives Rhythm Formant Analysis AM/FM spectrograms, tests handcrafted features and a ViT-plus-BERT fusion for dementia classification and regression, and compares against eGeMAPs and Mel spectrograms.
- **Conceptual structure:** The representation changes the time scale of measurement: modulation patterns become visible as structured images, while classification and regression test whether they carry diagnostic information.
- **What paper reports:** The paper reports a 14.2% relative classification-accuracy improvement over eGeMAPs for handcrafted features and further gains when rhythm spectrograms are fused with linguistic and acoustic models.
- **Limits:** Corpus, labels, recording length, disease definition, model fusion, and accuracy/regression metrics bound the result; an acoustic association is not a clinical diagnosis or causal mechanism.

## 5. text-to-speech-and-content

**Paper:** [Revival with Voice: Multi-modal Controllable Text-to-Speech Synthesis](https://www.isca-archive.org/interspeech_2025/kim25b_interspeech.html)
**Evidence:** D3; PDF SHA-256 `994d49fd833d6f6c34ea4ee1fb9ca22be60812df334d63bbd7c636d665c5d432`; full text captured.

- **Ordinary problem:** A user may want a voice that matches a face and also specify pace, distance, noise, tone, or place in ordinary language; a system must honor all of these constraints without making the output inconsistent.
- **Why hard:** A face does not uniquely determine a voice, artistic portraits differ from photographs, and audio-visual corpora may have low-quality audio; one-to-many mappings create ambiguity rather than a single correct answer.
- **Naive attempt:** Map each face to one fixed voice, generate speech only from a face-conditioned audio-visual corpus, or apply text controls after synthesis.
- **Central move:** Combine high-quality audio-only training, stylized-face augmentation, sampled face-to-voice decoding, and natural-language control of acoustic attributes.
- **Mechanism:** Revival with Voice generates speech from face images and text descriptions of pace, noise, distance, tone, and place; sampling handles multiple plausible voices while consistency mechanisms keep repeated generation coherent.
- **Conceptual structure:** The output is a constrained sample from a one-to-many mapping: face conditions identity, text conditions content and environment, and sampling expresses uncertainty without losing control.
- **What paper reports:** The paper reports improved face-driven TTS quality and controllability while extending the system to artistic portraits and natural-language acoustic descriptions.
- **Limits:** Training corpora, face style, prompt interpretation, sampling variability, and subjective quality measures bound the claim; consistent face-voice generation is not proof of real identity or social appropriateness.

## 6. speaker-characteristics

**Paper:** [How sibilant spectra shape gender perception in prepubertal children: A voice morphing study](https://www.isca-archive.org/interspeech_2025/funk25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `2189cb98638b181c71beaefe046fd7e2c3c0977e82584a6dced67a4df7c41f5e`; full text captured.

- **Ordinary problem:** Listeners may infer gender from a child's voice, but a small acoustic feature such as a sibilant spectrum should not be mistaken for a complete or natural explanation of that social judgment.
- **Why hard:** Natural speech contains many correlated cues, and children learn social categories from context; isolating one spectrum can reveal an association while also creating an artificial listening condition.
- **Naive attempt:** Measure average spectral differences between boys and girls and infer that the difference determines listener gender perception.
- **Central move:** Use natural and voice-morphed stimuli to separate the acoustic contribution of /z/ sibilant spectral shape from the broader voice and social context.
- **Mechanism:** The longitudinal study measures center of gravity and skewness of /z/ in German-speaking children aged 6–9 and runs gender-perception experiments with natural and morphed voices.
- **Conceptual structure:** Morphing is a controlled intervention: it holds much of the voice fixed while changing the sibilant spectrum, allowing perception to be compared with the correlation found in natural speech.
- **What paper reports:** No overall gender differences in the measured sibilant features were found; sibilants did not affect gender perception in natural stimuli but did affect it in morphed stimuli, suggesting stereotypical associations in isolation.
- **Limits:** Age, language, stimulus construction, listener beliefs, longitudinal sample, and morphing artifacts bound the claim; a perceptual association is not a biological marker or justification for gender classification.

## 7. voice-identity-and-conversion

**Paper:** [DAFMSVC: One-Shot Singing Voice Conversion with Dual Attention Mechanism and Flow Matching](https://www.isca-archive.org/interspeech_2025/chen25d_interspeech.html)
**Evidence:** D3; PDF SHA-256 `30e2a00e939c6b4d1508a56b13da8eacf40f5051c4cd972296516b21abb7b141`; full text captured.

- **Ordinary problem:** A one-shot singing voice converter should transfer an unseen singer's timbre while preserving the source melody and lyrics, without leaking the source singer into the output or making the target sound poor.
- **Why hard:** Timbre, melody, linguistic content, and source-speaker traces are entangled in the input; unseen targets provide little paired evidence for adapting all of them at once.
- **Naive attempt:** Copy the source SSL features directly, concatenate a target speaker embedding, and hope the converter separates timbre from melody and words.
- **Central move:** Replace source features with similar target-speaker features, fuse speaker/melody/content through dual attention, and use flow matching to generate the waveform.
- **Mechanism:** DAFMSVC uses target-feature retrieval to reduce timbre leakage, dual cross-attention for adaptive fusion, and a flow-matching generator for one-shot singing voice conversion.
- **Conceptual structure:** The system treats conversion as constrained substitution: target timbre evidence replaces identity-bearing content while melody and lyrics remain conditions; timbre similarity, content accuracy, and quality expose leakage and distortion.
- **What paper reports:** The paper reports improved target-timbre similarity and generated-audio quality over comparison methods in one-shot singing conversion experiments.
- **Limits:** Singer, song, target-reference duration, feature retrieval, evaluation metrics, and dataset splits bound the result; one-shot similarity does not prove perfect disentanglement or generalization to every unseen singer.

## 8. adaptation-and-open-vocabulary

**Paper:** [GLCLAP: A Novel Contrastive Learning Pre-trained Model for Contextual Biasing in ASR](https://www.isca-archive.org/interspeech_2025/kong25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `f04f4fdb18d044ac8fcce09d6fc6e94a0a9e926cea8b280a91c16a70914384de`; full text captured.

- **Ordinary problem:** A recognizer may need to favor a user's rare names or entities, but it must retrieve the right items from a list rather than biasing toward every vaguely similar word.
- **Why hard:** The prompt list can be long and the audio contains both sentence-level meaning and local word evidence; a sentence-only audio-text match may miss the precise entity.
- **Naive attempt:** Give all listed words a fixed decoding bonus or retrieve candidates using only a global sentence embedding.
- **Central move:** Train a contrastive audio-text retriever at both global sentence and local word scales, then use the retrieved bias words during ASR decoding.
- **Mechanism:** GLCLAP learns global and local audio-text relations for contextual biasing, retrieving matched entities from a user-specified list before the ASR decoder uses them.
- **Conceptual structure:** Contrastive learning makes matched audio/text pairs close and mismatched pairs distant; global context narrows meaning while local segments identify the exact rare word, and retrieval accuracy precedes WER.
- **What paper reports:** The paper reports a marked improvement in bias-word retrieval accuracy and downstream contextual ASR performance over sentence-level contrastive approaches.
- **Limits:** Entity list, prompt quality, language, negative sampling, retrieval threshold, and ASR decoder bound the result; a better retrieved list cannot correct an incorrect user prompt or guarantee unbiased ordinary decoding.

