# INTERSPEECH 2025 twenty-eighth-pass full-paper notes

Eight official-PDF readings deepen human-centered assessment, culturally aligned spoken QA, weak supervision, representation interpretation, multimodal efficiency, acoustic transparency, prosodic intent, and machine unlearning. Results are author-reported and not independently reproduced.

## 1. human-centered-evaluation

**Paper:** [A Study on Speech Assessment with Visual Cues](https://www.isca-archive.org/interspeech_2025/ahmed25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `597b0fab2ec507b35047a15116a4ea12244fcfe6953afaa7e879f567c8d8a3f0`; full text captured.

- **Ordinary problem:** When clean reference audio is unavailable, a system still needs to estimate whether speech is understandable and acceptable.
- **Why hard:** Noise can obscure the signal, and a microphone-only score cannot use visible mouth motion that may remain informative.
- **Naive attempt:** Compare the noisy signal with a clean recording or predict a quality score from audio alone.
- **Central move:** Fuse audio and visual evidence and predict quality and intelligibility as separate but related targets.
- **Mechanism:** STFT audio features and visual embeddings from LRS3-TED are fused by a CNN-BLSTM with attention and multi-task prediction of PESQ and STOI.
- **Conceptual structure:** The system estimates two proxies for different human properties; LCC measures association with each reference score under seen and unseen noise conditions.
- **What paper reports:** Under seen noise, the multimodal model improves LCC from 0.8397 to 0.9205 for PESQ and from 0.7403 to 0.8253 for STOI over audio-only input.
- **Limits:** LRS3-TED, DEMAND noise, visual availability, reference metrics, and seen-noise conditions bound the claim; PESQ/STOI prediction is not a direct listener or deployment test.

## 2. multilingual-and-crosslingual

**Paper:** [SpokenNativQA: Multilingual Everyday Spoken Queries for LLMs](https://www.isca-archive.org/interspeech_2025/alam25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `18bd3681a3b64e6b91cddb8134034520ac55fbe72d18aeb0334d5041ba26a11a`; full text captured.

- **Ordinary problem:** A spoken question-answering system must handle natural accents, languages, dialects, and everyday phrasing rather than only clean text typed by benchmark authors.
- **Why hard:** Text benchmarks remove pronunciation and interaction variability, while a translated dataset can erase culturally specific ways of asking and answering.
- **Naive attempt:** Transcribe a small set of scripted questions and evaluate a text LLM as if it had heard the original speech.
- **Central move:** Build a culturally aligned multilingual spoken QA dataset and evaluate the ASR-plus-LLM chain on naturally spoken questions and answers.
- **Mechanism:** SpokenNativQA contains about 33,000 spoken questions and answers across multilingual, low-resource, and dialect-rich settings; ASR systems and LLMs are benchmarked on the resulting task.
- **Conceptual structure:** The benchmark keeps acoustic variability in the input and evaluates the chain from speech recognition to answer generation rather than text QA alone.
- **What paper reports:** The paper introduces the dataset, releases data and scripts, and reports comparative ASR and LLM results for spoken QA.
- **Limits:** Language coverage, annotation, question domains, ASR errors, and answer scoring bound the result; a benchmark does not establish equal usefulness across all represented communities.

## 3. acoustic-to-token-1

**Paper:** [From Weak Labels to Strong Results: Utilizing 5,000 Hours of Noisy Classroom Transcripts with Minimal Accurate Data](https://www.isca-archive.org/interspeech_2025/attia25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `f5add729f4ae9e6e1b5f3bd182a567bd1b20b77cc0c26172659c4245e4b4c190`; full text captured.

- **Ordinary problem:** Classroom speech may have thousands of hours of cheap imperfect transcripts and only a small amount of carefully corrected text.
- **Why hard:** Discarding weak transcripts wastes coverage, but trusting them as if every word were correct can teach systematic errors.
- **Naive attempt:** Use only the small gold set or train directly on all weak labels with no later correction.
- **Central move:** Pretrain on weak transcripts, then fine-tune on accurate data so broad coverage supplies structure and gold data corrects its errors.
- **Mechanism:** Weakly Supervised Pretraining uses 5,000 hours of noisy classroom transcripts followed by fine-tuning on a small accurate set; synthetic and real weak transcripts are compared.
- **Conceptual structure:** The two-stage schedule separates learning broad acoustic-to-token regularities from calibrating the final transcript against trusted labels.
- **What paper reports:** The paper reports that WSP outperforms alternative strategies in synthetic and real weak-label settings for classroom ASR.
- **Limits:** Classroom domain, weak-label generation, gold-data size, transcript quality, and WER protocol bound the result; weak supervision can still reproduce systematic omissions or speaker bias.

## 4. self-supervised-speech-units

**Paper:** [Word stress in self-supervised speech models: A cross-linguistic comparison](https://www.isca-archive.org/interspeech_2025/bentum25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `7f0ad81d6a23019b42ab3d580f47fea45874e280d3083cbb814c8fb1c5dbfc7e`; full text captured.

- **Ordinary problem:** A self-supervised speech representation may contain linguistically meaningful stress information, but it is not obvious which language-specific distinctions it encodes.
- **Why hard:** A high-performing downstream classifier can exploit shortcuts and does not by itself show what the representation has learned.
- **Naive attempt:** Treat the representation as an opaque feature vector and infer its linguistic content from end-task accuracy alone.
- **Central move:** Use simple diagnostic classifiers across languages and stress systems, then compare whether the encoded distinction changes with the language's stress structure.
- **Mechanism:** Wav2vec 2.0 embeddings are probed for stressed versus unstressed syllables in Dutch, English, German, Hungarian, and Polish.
- **Conceptual structure:** A diagnostic classifier tests recoverable information while cross-language comparison asks whether the representation reflects variable versus fixed or demarcative stress systems.
- **What paper reports:** Stress is decoded with high accuracy, and the representations show language-specific differences, with a larger contrast between variable-stress and fixed-stress languages.
- **Limits:** Read-aloud sentences, languages, layer choices, probe capacity, and diagnostic accuracy bound the inference; recoverable information is not proof that the model uses stress causally.

## 5. noise-enhancement

**Paper:** [Scaling and Enhancing LLM-based AVSR:  A Sparse Mixture of Projectors Approach](https://www.isca-archive.org/interspeech_2025/cappellazzo25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `89bca7181a867c1e2ea1c260d64bc0557225357dd5ba7719bb8cc62f90de373b`; full text captured.

- **Ordinary problem:** Audio-visual recognition can use the face when noise damages the sound, but a large multimodal language model may be too expensive for a device.
- **Why hard:** Adding experts or projectors can increase capacity and memory even when only a small part of the model is useful for each modality.
- **Naive attempt:** Use one dense projector for every modality or deploy a large LLM and accept its inference cost.
- **Central move:** Route audio and visual inputs through sparse modality-specific projectors so capacity grows without activating every expert on every example.
- **Mechanism:** Llama-SMoP uses sparsely gated mixtures of projectors with modality-specific routers and experts and is evaluated on ASR, visual speech recognition, and AVSR under noise.
- **Conceptual structure:** Conditional computation separates representational capacity from per-example computation; ASR/VSR/AVSR performance, activation patterns, and noise robustness test the tradeoff.
- **What paper reports:** The DEDR configuration reports the strongest results among the tested variants, with ablations supporting expert activation, scalability, and noise robustness.
- **Limits:** Model size, routing policy, datasets, noise, and compute accounting bound the claim; sparse projector success does not automatically transfer to every multimodal LLM.

## 6. metrics-and-targets

**Paper:** [Spectrotemporal Modulation: Efficient and Interpretable Feature Representation for Classifying Speech, Music, and Environmental Sounds](https://www.isca-archive.org/interspeech_2025/chang25b_interspeech.html)
**Evidence:** D3; PDF SHA-256 `6cf894bc764d0acbf209e6d7067231534b44b64b7f607ee9a6198f6c301c1e54`; full text captured.

- **Ordinary problem:** A machine-listening representation should reveal which changing time-frequency patterns distinguish speech, music, and environmental sound without requiring a huge opaque model.
- **Why hard:** Large pretrained networks can classify well while hiding which acoustic structures mattered and consuming substantial computation.
- **Naive attempt:** Use a large pretrained embedding and treat its internal features as the explanation.
- **Central move:** Represent sound with spectrotemporal modulation patterns motivated by auditory processing, then compare a compact unpretrained classifier with pretrained audio networks.
- **Mechanism:** STM features are used for naturalistic speech, music, and environmental sound classification without pretraining.
- **Conceptual structure:** The representation describes joint rates of spectral and temporal change; classification performance and feature interpretability test whether a structured signal account can compete with learned scale.
- **What paper reports:** The STM-based model reaches performance comparable to pretrained audio DNNs across the tested categories while remaining interpretable and efficient.
- **Limits:** Tasks, datasets, modulation parameters, baselines, and definition of interpretability bound the claim; comparable accuracy does not prove a match to human auditory cortex.

## 7. prosody-and-intent

**Paper:** [The Prosodic Characteristics of Standard Chinese Rhetorical Questions in Naturalistic Settings](https://www.isca-archive.org/interspeech_2025/chen25g_interspeech.html)
**Evidence:** D3; PDF SHA-256 `b0d9482e3785e8a7061d9cf904ed4c83b73e562c23cf07b280bd679ae3137929`; full text captured.

- **Ordinary problem:** A rhetorical question can have the same words as an information-seeking question but perform a different action, so listeners need prosody and syntax to distinguish them.
- **Why hard:** The difference may disappear in scripted laboratory speech, while a single global pitch measure misses which word carries the intended emphasis.
- **Naive attempt:** Treat identical text as identical meaning or look only at sentence-final intonation.
- **Central move:** Compare matched question types in naturalistic reading and measure where prominence shifts, including the interaction with sentence structure.
- **Mechanism:** One hundred three native Mandarin speakers produced information-seeking and rhetorical questions through an online platform; pitch and duration of prominent verbs and modal verbs are analyzed.
- **Conceptual structure:** Prosody is localized to syntactic positions: prominence placement and its acoustic realization connect the waveform to communicative intention.
- **What paper reports:** Speakers tend to mark rhetorical meaning by increasing pitch and duration on the verb or modal verb, with other cues depending on sentence structure.
- **Limits:** Standard Chinese, sentence materials, online reading, participant sample, and question interpretation bound the result; rhetorical intent is not reducible to one universal pitch rule.

## 8. speaker-characteristics

**Paper:** [Speech Unlearning](https://www.isca-archive.org/interspeech_2025/cheng25d_interspeech.html)
**Evidence:** D3; PDF SHA-256 `3f7e1bf16ec72d818585d6e04a86a27fadc5a55eed48d0e48bf9ebc8d1c9b9cd`; full text captured.

- **Ordinary problem:** A trained speech model may retain information about a recording that its owner wants removed, without the cost of retraining the entire model.
- **Why hard:** Speech is sequential, speaker-dependent, and high-dimensional, so removing one recording or one speaker can damage remaining behavior or leave traces behind.
- **Naive attempt:** Delete the source file and assume the trained model no longer contains its influence, or retrain from scratch every time.
- **Central move:** Define sample-level and class-level unlearning and test whether a model forgets the target while preserving performance on remaining speech.
- **Mechanism:** Keyword-spotting and speaker-identification experiments compare removing one recording with removing an entire speaker category and examine the difficulty relative to image and text unlearning.
- **Conceptual structure:** Unlearning is a constrained before/after problem: target influence should disappear while non-target accuracy remains; forgetting and retention need separate tests.
- **What paper reports:** The paper reports that speech unlearning is substantially harder than image or text unlearning and identifies structured training, evaluation, feature-level removal, and adversarial robustness as open directions.
- **Limits:** Tasks, speakers, unlearning definitions, attack tests, and evaluation criteria bound the result; a proposed forgetting score is not proof of privacy against every adversary.

