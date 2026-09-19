# From sound to words and structured speech

*Essay 3 of 8 in The Speech Atlas.*

Speech does not arrive as ready-made words with neat boundaries. This essay follows the work of turning changing sound into reusable units, pronunciations, timed alignments, and context-sensitive words without letting context invent what was not heard.

## Start with the baseline

Fant's speech-chain account places this theme at the following point in communication: Fant pp. 6-7, 11-12: message units and signal segments do not line up one-to-one, so perception uses context, memory, comparison, and prediction.

The ordinary problem is simple to state: Speech has no visible spaces between words, and pronunciation, speed, accent, noise, and hesitation vary even when the intended sentence is the same.

A tempting shortcut is to Matching each sound to a fixed dictionary pronunciation or treating the utterance as already segmented fails on coarticulation, new words, and disfluency. That shortcut fails because it hides the distinction this essay needs to keep visible.

The recurring move across this theme is to Infer a sequence of linguistic units while allowing uncertainty about boundaries, pronunciation, context, and what should be preserved. The cost is equally important: A fluent transcript can be easier to read but less faithful to what was said, including omissions, hesitation, or uncertainty.

## The boundaries

Each section below uses the same test: what pressure is being handled, what shortcut fails, what move recurs, and where the evidence stops.

## Learning reusable sound units

**The question.** What ordinary speech pressure is handled by learning reusable sound units, and what evidence distinguishes it from neighboring pressures?

**How this boundary is derived.** Baseline link: Fant pp. 6-7, 11-12: message units and signal segments do not line up one-to-one, so perception uses context, memory, comparison, and prediction. Ordinary pressure: Speech has no visible spaces between words, and pronunciation, speed, accent, noise, and hesitation vary even when the intended sentence is the same. Failed shortcut: Matching each sound to a fixed dictionary pronunciation or treating the utterance as already segmented fails on coarticulation, new words, and disfluency. Recurring paper move: Infer a sequence of linguistic units while allowing uncertainty about boundaries, pronunciation, context, and what should be preserved. Neighbor test: The system first decides what reusable evidence can be extracted from continuous sound.

**What the papers share.** Speech has no visible spaces between words, and pronunciation, speed, accent, noise, and hesitation vary even when the intended sentence is the same. The subtheme asks: What ordinary speech pressure is handled by learning reusable sound units, and what evidence distinguishes it from neighboring pressures?

**Why the shortcut fails.** A first attempt would answer the question only with acoustic-to-token mapping, but that shortcut misses the boundary: The highest-scoring sequence may exploit dataset regularities instead of matching the actual speech.

**The recurring move.** Across this subtheme, papers make acoustic-to-token mapping, learned speech units explicit rather than treating the speech evidence as one undifferentiated variable. The reviewed full-paper mechanisms instantiate that move in different ways; for example: Benchmark CTC, Whisper, and LLM-enhanced decoders, including bridge networks and a Q-Former that connects Whisper acoustic features to Vicuna for context-aware decoding.

### Words used in this section

**Acoustic-to-token mapping.** The system scores candidate symbol sequences against the observed sound and chooses or represents alternatives rather than reading words directly from samples.
*Boundary:* The highest-scoring sequence may exploit dataset regularities instead of matching the actual speech.

**Learned speech units.** Predicting or grouping parts of unlabeled audio can provide reusable units before a task-specific word recognizer is trained.
*Boundary:* A useful pretraining prediction need not produce units aligned with words, phonemes, or human categories.

### What the papers show

- [Bridging ASR and LLMs for Dysarthric Speech Recognition: Benchmarking Self-Supervised and Generative Approaches](https://www.isca-archive.org/interspeech_2025/aboeitta25_interspeech.html) (D3): Benchmark CTC, Whisper, and LLM-enhanced decoders, including bridge networks and a Q-Former that connects Whisper acoustic features to Vicuna for context-aware decoding. **Measured or tested:** This study systematically benchmarks these models with different decoding strategies, including CTC, seq2seq, and LLM-enhanced decoding (BART, GPT-2, Vicuna). **Limit:** Dataset splits, severity labels, model scale, decoding prompts, and WER limit the claim; lower WER does not prove faithful preservation of disfluencies or speaker intent.
- [HuBERT-VIC: Improving Noise-Robust Automatic Speech Recognition of Speech Foundation Model via Variance-Invariance-Covariance Regularization](https://www.isca-archive.org/interspeech_2025/ahn25_interspeech.html) (D3): Add variance, invariance, and covariance constraints during HuBERT pretraining. **Measured or tested:** Noise robustness in speech foundation models (SFMs) has been a critical challenge, as most models are primarily trained on clean data and experience performance degradation when the models are exposed to noisy speech. **Limit:** MUSAN, SNR choices, HuBERT, and LibriSpeech bound the result; real conversational noise is not established.
- [Analysis of Semantic and Acoustic Token Variability Across Speech, Music, and Audio Domains](https://www.isca-archive.org/interspeech_2025/ashihara25_interspeech.html) (D3): Compare acoustic codec tokens and semantic speech tokens across domains using rank-frequency distributions, perplexity, and token usage patterns. **Measured or tested:** Using up to 1,000 held-out samples per speech, music, and sound domain, the study compares semantic and acoustic token distributions from HuBERT, EnCodec, and DAC. It evaluates rank-frequency/power-law behavior, N-gram language-model perplexity, normalized cross-entropy predictability, and… **Limit:** The analysis supports representation observations, not a universal optimal token design or downstream task improvement.
- [From Weak Labels to Strong Results: Utilizing 5,000 Hours of Noisy Classroom Transcripts with Minimal Accurate Data](https://www.isca-archive.org/interspeech_2025/attia25_interspeech.html) (D3): Pretrain on weak transcripts, then fine-tune on accurate data so broad coverage supplies structure and gold data corrects its errors. **Measured or tested:** Synthetic corruption experiments fine-tune Robust-wav2vec2 with deletion, misspelling, sound-alike, repetition, and timestamp corruption at 25/50/75/100% mixed with clean transcripts, then fine-tune with 10 minutes of precise data. A real-world NCTE classroom case uses 5,235 hours, 17 gold… **Limit:** Classroom domain, weak-label generation, gold-data size, transcript quality, and WER protocol bound the result; weak supervision can still reproduce systematic omissions or speaker bias.

**Where this boundary stops.** The highest-scoring sequence may exploit dataset regularities instead of matching the actual speech.; A useful pretraining prediction need not produce units aligned with words, phonemes, or human categories.

**What this evidence does not establish.** The shared story is supported only by the reviewed papers listed here; D2 entries support the problem and stated method, while D3 entries support the reported mechanism and evaluation. It is not a venue-wide prevalence claim.

**Question left open.** What changes when this move is tested outside the speakers, languages, rooms, devices, or benchmark conditions represented by the 14 D3 paper(s)?

## Allowing different realizations of words

**The question.** What ordinary speech pressure is handled by allowing different realizations of words, and what evidence distinguishes it from neighboring pressures?

**How this boundary is derived.** Baseline link: Fant pp. 6-7, 11-12: message units and signal segments do not line up one-to-one, so perception uses context, memory, comparison, and prediction. Ordinary pressure: Speech has no visible spaces between words, and pronunciation, speed, accent, noise, and hesitation vary even when the intended sentence is the same. Failed shortcut: Matching each sound to a fixed dictionary pronunciation or treating the utterance as already segmented fails on coarticulation, new words, and disfluency. Recurring paper move: Infer a sequence of linguistic units while allowing uncertainty about boundaries, pronunciation, context, and what should be preserved. Neighbor test: The same intended unit has multiple acoustic paths; this is distinct from learning a unit representation.

**What the papers share.** Speech has no visible spaces between words, and pronunciation, speed, accent, noise, and hesitation vary even when the intended sentence is the same. The subtheme asks: What ordinary speech pressure is handled by allowing different realizations of words, and what evidence distinguishes it from neighboring pressures?

**Why the shortcut fails.** A first attempt would answer the question only with pronunciation variation, but that shortcut misses the boundary: Adding variants without evidence can increase confusions and may encode an accent as an error.

**The recurring move.** Across this subtheme, papers make pronunciation variation explicit rather than treating the speech evidence as one undifferentiated variable. The reviewed full-paper mechanisms instantiate that move in different ways; for example: Keep several small accent-specific adapters and let the system combine them, with or without knowing the accent.

### Words used in this section

**Pronunciation variation.** The same word can have reductions, substitutions, or accent-specific realizations, so recognition must allow more than one acoustic path.
*Boundary:* Adding variants without evidence can increase confusions and may encode an accent as an error.

### What the papers show

- [Mixture of LoRA Experts for Low-Resourced Multi-Accent Automatic Speech Recognition](https://www.isca-archive.org/interspeech_2025/bagat25_interspeech.html) (D3): Keep several small accent-specific adapters and let the system combine them, with or without knowing the accent. **Measured or tested:** Our experiments, conducted using Whisper on the L2-ARCTIC corpus, demonstrate significant improvements in Word Error Rate compared to regular LoRA and full fine-tuning when the accent is unknown. **Limit:** The result is tied to L2-ARCTIC, its accent set, Whisper, and routing assumptions; spontaneous speech and accents outside the corpus remain open.
- [CHSER: A Dataset and Case Study on Generative Speech Error Correction for Child ASR](https://www.isca-archive.org/interspeech_2025/balajishankar25_interspeech.html) (D3): Create a large hypothesis-to-reference dataset for children and learn a generative correction model whose errors can be inspected by type. **Measured or tested:** Automatic Speech Recognition (ASR) systems struggle with child speech due to its distinct acoustic and linguistic variability and limited availability of child speech datasets, leading to high transcription error rates. **Limit:** The corpus, languages, ASR hypotheses, and correction model bound the result; preserving clinically meaningful disfluencies outside these settings remains open.
- [SardinianVoxes: A Speech Recognition Dataset for the Sardinian Languages](https://www.isca-archive.org/interspeech_2025/carta25_interspeech.html) (D3): Build a reproducible audio-text corpus with explicit variety annotation and evaluate both pretrained and fine-tuned recognizers across varieties. **Measured or tested:** First, we present the design and implementation of a reproducible pipeline that led to the preparation of SardinianVoxes, an audio-text dataset comprising approximately 170 hours of transcribed speech, carefully annotated to reflect the internal linguistic diversity of Sardinian. **Limit:** The reported resource, varieties, transcription quality, and benchmark models bound the claim; future collection and independent use are still needed.
- [Using Neurogram Similarity Index Measure (NSIM) to Model Hearing Loss and Cochlear Neural Degeneration](https://www.isca-archive.org/interspeech_2025/cheema25_interspeech.html) (D3): Compare modeled auditory-nerve neurograms with a Neurogram Similarity Index and relate the measure to phoneme recognition and simulated cochlear neural degeneration. **Measured or tested:** Specifically study 1, shows that NSIM can be used to map performance of individuals with hearing loss on phoneme recognition task with reasonable accuracy. **Limit:** Auditory-periphery model, task, simulations, participant data, and mapping assumptions bound clinical interpretation; a candidate biomarker is not a validated diagnosis.

**Where this boundary stops.** Adding variants without evidence can increase confusions and may encode an accent as an error.

**What this evidence does not establish.** The shared story is supported only by the reviewed papers listed here; D2 entries support the problem and stated method, while D3 entries support the reported mechanism and evaluation. It is not a venue-wide prevalence claim.

**Question left open.** What changes when this move is tested outside the speakers, languages, rooms, devices, or benchmark conditions represented by the 5 D3 paper(s)?

## Locating units in time

**The question.** What ordinary speech pressure is handled by locating units in time, and what evidence distinguishes it from neighboring pressures?

**How this boundary is derived.** Baseline link: Fant pp. 6-7, 11-12: message units and signal segments do not line up one-to-one, so perception uses context, memory, comparison, and prediction. Ordinary pressure: Speech has no visible spaces between words, and pronunciation, speed, accent, noise, and hesitation vary even when the intended sentence is the same. Failed shortcut: Matching each sound to a fixed dictionary pronunciation or treating the utterance as already segmented fails on coarticulation, new words, and disfluency. Recurring paper move: Infer a sequence of linguistic units while allowing uncertainty about boundaries, pronunciation, context, and what should be preserved. Neighbor test: The output must preserve or locate timing, hesitation, repair, or sequence boundaries.

**What the papers share.** Speech has no visible spaces between words, and pronunciation, speed, accent, noise, and hesitation vary even when the intended sentence is the same. The subtheme asks: What ordinary speech pressure is handled by locating units in time, and what evidence distinguishes it from neighboring pressures?

**Why the shortcut fails.** A first attempt would answer the question only with temporal alignment, but that shortcut misses the boundary: Forced alignment assumes the transcript is correct and can conceal recognition errors.

**The recurring move.** Across this subtheme, papers make temporal alignment, disfluency and event preservation explicit rather than treating the speech evidence as one undifferentiated variable. The reviewed full-paper mechanisms instantiate that move in different ways; for example: Fine-tune Whisper on DementiaBank and an in-house dataset, explicitly evaluating filler inclusion and F1 as well as WER.

### Words used in this section

**Temporal alignment.** Align an audio timeline with words, phones, or labels so duration and position can be measured rather than treating the utterance as an unordered bag.
*Boundary:* Forced alignment assumes the transcript is correct and can conceal recognition errors.

**Disfluency and event preservation.** Represent pauses, repetitions, repairs, laughter, and overlap when those events are part of the communication or the clinical signal.
*Boundary:* Removing them may improve readability while destroying evidence needed for conversation analysis or diagnosis.

### What the papers show

- [WhisperD: Dementia Speech Recognition and Filler Word Detection with Whisper](https://www.isca-archive.org/interspeech_2025/akinrintoyo25_interspeech.html) (D3): Fine-tune Whisper on DementiaBank and an in-house dataset, explicitly evaluating filler inclusion and F1 as well as WER. **Measured or tested:** In this work, we fine-tune Whisper with the open-source dementia speech dataset (DementiaBank) and our in-house dataset to improve its word error rate (WER). **Limit:** The dataset is 11.39 hours, some audio is mumbled or unintelligible, and diagnostic or clinical benefit is not established by ASR scores alone.
- [ASR-based segmentation for the analysis of larger child-speech datasets: Performance evaluation on vowels from Australian-English speaking children aged 4 to 11 years](https://www.isca-archive.org/interspeech_2025/cai25_interspeech.html) (D3): Compare human-human reliability with manual-versus-Montreal-Forced-Aligner boundaries across child ages and inspect systematic discrepancies. **Measured or tested:** Annotation of segment boundaries in child speech presents a persistent challenge, particularly with large-scale datasets. **Limit:** The evidence is tied to the tested vowels, ages, language variety, and annotators; it supports semi-automatic caution rather than universal aligner failure.
- [Song Form-aware Full-Song Text-to-Lyrics Generation with Multi-Level Granularity Syllable Count Control](https://www.isca-archive.org/interspeech_2025/chae25_interspeech.html) (D3): Generate complete lyrics conditioned on text and song form while controlling syllable counts at word, phrase, line, and paragraph levels. **Measured or tested:** Song-form-aware lyric generation is evaluated on approximately 340K training, 18K validation, and 10K evaluation samples from Genius Song Lyrics after toxicity filtering. Perplexity, syllable-count deviation, syllable-count error rate, and BERT-S similarity are compared across full, paragraph,… **Limit:** Text prompts, song forms, syllable-count rules, dataset construction, and evaluation criteria bound the claim; syllable fit is not the same as singability, musicality, or authorship.
- [A semi-automatic pipeline for transcribing and segmenting child speech](https://www.isca-archive.org/interspeech_2025/christodoulidou25_interspeech.html) (D3): Correct the transcript before forced alignment and adapt the acoustic model toward child speech, then compare automatic measurements with manual annotations. **Measured or tested:** This study evaluates both automated transcription (WhisperX) and forced alignment (MFA) in developing a semi-automated pipeline for obtaining acoustic vowel measures from field recordings from 275 children speaking a non-standard, English dialect, Scottish English. **Limit:** The 275-child Scottish-English field corpus, manual reference quality, recording conditions, and selected vowel measures bound transfer; alignment quality is not a complete child-speech recognizer evaluation.

**Where this boundary stops.** Forced alignment assumes the transcript is correct and can conceal recognition errors.; Removing them may improve readability while destroying evidence needed for conversation analysis or diagnosis.

**What this evidence does not establish.** The shared story is supported only by the reviewed papers listed here; D2 entries support the problem and stated method, while D3 entries support the reported mechanism and evaluation. It is not a venue-wide prevalence claim.

**Question left open.** What changes when this move is tested outside the speakers, languages, rooms, devices, or benchmark conditions represented by the 13 D3 paper(s)?

## Using context without inventing words

**The question.** What ordinary speech pressure is handled by using context without inventing words, and what evidence distinguishes it from neighboring pressures?

**How this boundary is derived.** Baseline link: Fant pp. 6-7, 11-12: message units and signal segments do not line up one-to-one, so perception uses context, memory, comparison, and prediction. Ordinary pressure: Speech has no visible spaces between words, and pronunciation, speed, accent, noise, and hesitation vary even when the intended sentence is the same. Failed shortcut: Matching each sound to a fixed dictionary pronunciation or treating the utterance as already segmented fails on coarticulation, new words, and disfluency. Recurring paper move: Infer a sequence of linguistic units while allowing uncertainty about boundaries, pronunciation, context, and what should be preserved. Neighbor test: Context, speaker evidence, and new words resolve ambiguity but can override what was actually said.

**What the papers share.** Speech has no visible spaces between words, and pronunciation, speed, accent, noise, and hesitation vary even when the intended sentence is the same. The subtheme asks: What ordinary speech pressure is handled by using context without inventing words, and what evidence distinguishes it from neighboring pressures?

**Why the shortcut fails.** A first attempt would answer the question only with long-context decoding, but that shortcut misses the boundary: Context can override a rare but correct word, especially when the language model has a strong prior.

**The recurring move.** Across this subtheme, papers make long-context decoding, domain and context biasing, speaker adaptation, open-vocabulary recognition explicit rather than treating the speech evidence as one undifferentiated variable. The reviewed full-paper mechanisms instantiate that move in different ways; for example: Adapt the audio side using representative target-domain sound examples and test transfer across environments.

### Words used in this section

**Long-context decoding.** Use words and turns before and after a sound to resolve locally ambiguous acoustics, such as homophones or clipped endings.
*Boundary:* Context can override a rare but correct word, especially when the language model has a strong prior.

**Domain and context biasing.** Use the meeting topic, contact list, or application vocabulary to raise plausible rare words without changing the audio itself.
*Boundary:* A biased vocabulary can turn uncertainty into confident but context-shaped substitutions.

**Speaker adaptation.** Adjust the acoustic or decoding assumptions to a talker's voice, speaking rate, or pronunciation using a small amount of evidence.
*Boundary:* Adaptation can overfit a short sample and degrade when the talker changes state or the enrollment is wrong.

**Open-vocabulary recognition.** Handle names, code-switching, jargon, and newly encountered words without requiring a fixed closed list.
*Boundary:* Open vocabulary expands recall but makes spelling, segmentation, and evaluation less settled.

### What the papers show

- [Domain Adaptation Method and Modality Gap Impact in Audio-Text Models for Prototypical Sound Classification](https://www.isca-archive.org/interspeech_2025/acevedo25_interspeech.html) (D3): Adapt the audio side using representative target-domain sound examples and test transfer across environments. **Measured or tested:** Our domain adaptation technique enhances accuracy across various backgrounds and SNR conditions. **Limit:** Sound set, target examples, class construction, and reported accuracy limit open-world claims.
- [Spot and Merge: A Hybrid Context Biasing Approach for Rare Word and Out of Vocabulary Recognition](https://www.isca-archive.org/interspeech_2025/agrawal25b_interspeech.html) (D3): Use LoRA adaptation and a spot-and-merge method that detects bias phrases in cross-attention and merges them with ASR output. **Measured or tested:** Unlike existing methods, our approach maintains strong performance even with larger biasing lists, achieving a 1.0% absolute word error rate (WER) reduction on LibriSpeech. **Limit:** The in-house data are not independently available in this atlas, and future multilingual/low-resource extension remains open.
- [Continuous Learning for Children's ASR: Overcoming Catastrophic Forgetting with Elastic Weight Consolidation and Synaptic Intelligence](https://www.isca-archive.org/interspeech_2025/ahadzi25_interspeech.html) (D3): Protect parameters important for earlier batches with EWC or SI, and compare online checkpoint-selection policies. **Measured or tested:** Using a custom protocol on the MyST corpus, tailored to the online learning setting, we achieve relative word error rate (WER) reductions of 5.21 % with EWC and 4.36 % with SI, compared to the fine-tuning baseline. **Limit:** The protocol is simulated from MyST, uses English child speech and Whisper-small, and treats parameter importance as a proxy rather than a privacy guarantee.
- [NGPU-LM: GPU-Accelerated N-Gram Language Model for Context-Biasing in Greedy ASR Decoding](https://www.isca-archive.org/interspeech_2025/bataev25_interspeech.html) (D3): Represent n-gram transitions for parallel GPU lookup and inject their scores into greedy decoding for CTC, transducer, and attention models. **Measured or tested:** The proposed approach can eliminate more than 50% of the accuracy gap between greedy and beam search for out-of-domain scenarios while avoiding significant slowdown caused by beam search. **Limit:** The results depend on tested ASR architectures, domains, GPU implementation, and author-reported measurements; deployment energy and other hardware remain open.

**Where this boundary stops.** Context can override a rare but correct word, especially when the language model has a strong prior.; A biased vocabulary can turn uncertainty into confident but context-shaped substitutions.; Adaptation can overfit a short sample and degrade when the talker changes state or the enrollment is wrong.; Open vocabulary expands recall but makes spelling, segmentation, and evaluation less settled.

**What this evidence does not establish.** The shared story is supported only by the reviewed papers listed here; D2 entries support the problem and stated method, while D3 entries support the reported mechanism and evaluation. It is not a venue-wide prevalence claim.

**Question left open.** What changes when this move is tested outside the speakers, languages, rooms, devices, or benchmark conditions represented by the 23 D3 paper(s)?

## Closing note

This essay is a map of recurring problems and research moves, not a leaderboard or a claim that these categories cover every speech study. The paper links and depth labels show what was actually checked; they do not turn reported results into independent facts.
