# Many languages, accents, and unequal evidence

*Essay 7 of 8 in The Speech Atlas.*

Speech technology is trained from uneven evidence. Languages, accents, dialects, speakers, and recording conditions do not receive equal data or equal evaluation. This essay follows what can be shared, what must remain local, and how missing evidence is made.

## Start with the baseline

Fant's speech-chain account places this theme at the following point in communication: Fant pp. 5-7: physical cues vary with context and production, and a single message distinction may have different signal realizations; language-specific evidence must therefore be tested rather than assumed.

The ordinary problem is simple to state: Languages differ in sounds, writing systems, grammar, prosody, code-switching, and social meaning; data and tools are distributed unevenly.

One tempting shortcut is: Scaling an English-centered recipe or translating labels assumes that all languages expose the same units, data, and errors. It fails because it hides the distinction this essay needs to keep visible.

The recurring move across this theme is to share useful structure across languages while preserving language-specific distinctions, measuring who benefits, and making uncertainty visible where evidence is thin. The cost is equally important: Transfer can import pronunciation or cultural assumptions, and aggregate multilingual scores can hide severe failures in a small language or community.

## The boundaries

Each section below uses the same test: what pressure is being handled, what shortcut fails, what move recurs, and where the evidence stops.

## Plain-language dictionary

The papers use specialized names because they measure specialized things. These are the terms that recur in this essay, translated before they do argumentative work:

**Fant's speech chain.** a practical way to follow speech from a speaker's body, through the air and a recording device, to a listener and an interpretation.
**D2.** evidence checked in the official paper abstract; it supports the paper's stated problem and approach, but not details that appear only in the full paper.
**D3.** evidence checked in the official full paper text; it supports what the authors report about their method and tests, but it is still not an independent reproduction.
**ASR.** automatic speech recognition: software that turns speech recordings into written words.
**TTS.** text-to-speech: software that turns written words into a spoken signal.
**speaker embedding.** a compact numerical description intended to preserve characteristics of a voice or speaker.
**self-supervised learning.** training in which the recording supplies part of its own teaching signal, so hand-written labels are needed less often.
**voice activity detection.** a decision about whether a signal segment contains speech.
**word error rate.** the number of word substitutions, insertions, and deletions divided by the reference word count.
**equal error rate.** the point at which two kinds of biometric decision error—false acceptance and false rejection—are equal.
**interaural.** between the two ears; an interaural difference is a difference in timing or level between left and right channels.
**MRI.** magnetic resonance imaging, used here to observe anatomy or movement without cutting into the body.
**EEG.** electroencephalography, a measurement of electrical activity at the scalp.
**MFCC.** a compact description of the broad shape of a sound spectrum, often used as an input feature.
**F0.** the rate of vocal-fold vibration, commonly heard as the main component of pitch.

This is a map of distinctions, not a ranking of methods. A paper can be useful while still answering only one narrow question.

## Sharing structure across languages

This boundary follows from the baseline account: baseline link: Fant pp. 5-7: physical cues vary with context and production, and a single message distinction may have different signal realizations; language-specific evidence must therefore be tested rather than assumed. Ordinary pressure: Languages differ in sounds, writing systems, grammar, prosody, code-switching, and social meaning; data and tools are distributed unevenly. Failed shortcut: Scaling an English-centered recipe or translating labels assumes that all languages expose the same units, data, and errors. Recurring paper move: Share useful structure across languages while preserving language-specific distinctions, measuring who benefits, and making uncertainty visible where evidence is thin. Neighbor test: The central question is what can be shared while retaining language-specific distinctions.

**The question.** What ordinary speech pressure is handled by sharing structure across languages, and what evidence distinguishes it from neighboring pressures?

**The pressure.** Languages differ in sounds, writing systems, grammar, prosody, code-switching, and social meaning; data and tools are distributed unevenly. The subtheme asks: What ordinary speech pressure is handled by sharing structure across languages, and what evidence distinguishes it from neighboring pressures?

**Why the easy answer breaks.** A first attempt would answer the question only with cross-lingual transfer, but that shortcut misses the boundary: Transfer may favor high-resource languages and erase distinctions absent from the source language.

**The move that recurs.** Across this subtheme, papers make cross-lingual transfer, language and variety identification, code-switching explicit rather than treating the speech evidence as one undifferentiated variable. The reviewed full-paper mechanisms instantiate that move in different ways; for example: Build a culturally aligned multilingual spoken QA dataset and evaluate the ASR-plus-LLM chain on naturally spoken questions and answers.

### Words used in this section

**Cross-lingual transfer.** Reuse representations or training signals from one language to improve another when their speech structure overlaps.
*Boundary:* Transfer may favor high-resource languages and erase distinctions absent from the source language.

**Language and variety identification.** Determine which language or variety is being spoken so the appropriate recognizer or interaction policy can be selected.
*Boundary:* Closely related varieties and code-switching make a single label inadequate or politically loaded.

**Code-switching.** Handle a speaker moving between languages within an utterance, including pronunciation, grammar, and word-boundary changes.
*Boundary:* A monolingual metric can count appropriate switching as error and fail to define the intended transcript.

### What the evidence shows

- [SpokenNativQA: Multilingual Everyday Spoken Queries for LLMs](https://www.isca-archive.org/interspeech_2025/alam25_interspeech.html) (D3): Build a culturally aligned multilingual spoken QA dataset and evaluate the ASR-plus-LLM chain on naturally spoken questions and answers. **Measured or tested:** However, benchmarking their capabilities with multilingual spoken queries remains largely unexplored. **Limit:** Language coverage, annotation, question domains, ASR errors, and answer scoring bound the result; a benchmark does not establish equal usefulness across all represented communities.
- [TalTech Systems for the Interspeech 2025 ML-SUPERB 2.0 Challenge](https://www.isca-archive.org/interspeech_2025/alumae25_interspeech.html) (D3): Use hybrid language identification, multilingual and language-specific models, and targeted decoding resources. **Measured or tested:** The ML-SUPERB 2.0 development and dialect-development sets evaluate language-identification accuracy and character error rate across the challenge languages, dialects, and accents. Uniform interpolation of the embedding and generative LID models is compared with each component; the reported… **Limit:** Challenge data, language mix, averaging, and tuning limit all-multilingual claims.
- [A Study of Speech Embedding Similarities Between Australian Aboriginal and High-Resource Languages](https://www.isca-archive.org/interspeech_2025/ambikairajah25_interspeech.html) (D3): Compare speech embeddings across Aboriginal and high-resource languages and inspect what kinds of similarity and transfer the representation actually supports. **Measured or tested:** Our results reveal that aboriginal languages are most frequently identified as Māori, suggesting phonetic or structural similarities, while showing significant differences from globally dominant languages. **Limit:** Similarity is not a language description or a guarantee of recognition transfer; data quantity, speaker coverage, and community context limit interpretation. No independent reproduction was performed.
- [From Context to Code-switching: Examining the Interplay of Language Proficiency and Multilingualism in Speech](https://www.isca-archive.org/interspeech_2025/bhattacharya25_interspeech.html) (D3): Model code-switching quantity, dominant language, and switching strategy together with speaker background variables such as parental language, schooling language, and self-reported ability. **Measured or tested:** To answer this question, we examine the Bangor Miami corpus of spontaneous Spanish-English speech and analyze the linguistic and demographic profiles of its speakers alongside features of their conversational language production. **Limit:** The analysis is observational, focused on Spanish-English Bangor Miami speakers and available self-reports; background variables may be correlated and do not establish why a speaker switched. Findings do not generalize automatically to other language pairs, communities, or tasks; no independent…

**Where this boundary stops.** Transfer may favor high-resource languages and erase distinctions absent from the source language.; Closely related varieties and code-switching make a single label inadequate or politically loaded.; A monolingual metric can count appropriate switching as error and fail to define the intended transcript.

**What this evidence does not establish.** The shared story is supported only by the reviewed papers listed here; D2 entries support the problem and stated method, while D3 entries support the reported mechanism and evaluation. It is not a venue-wide prevalence claim.

**Question left open.** What changes when this move is tested outside the speakers, languages, rooms, devices, or benchmark conditions represented by the 19 D3 paper(s)?

## Learning from sparse labels

This boundary follows from the baseline account: baseline link: Fant pp. 5-7: physical cues vary with context and production, and a single message distinction may have different signal realizations; language-specific evidence must therefore be tested rather than assumed. Ordinary pressure: Languages differ in sounds, writing systems, grammar, prosody, code-switching, and social meaning; data and tools are distributed unevenly. Failed shortcut: Scaling an English-centered recipe or translating labels assumes that all languages expose the same units, data, and errors. Recurring paper move: Share useful structure across languages while preserving language-specific distinctions, measuring who benefits, and making uncertainty visible where evidence is thin. Neighbor test: The method changes how a model learns when labeled examples are scarce.

**The question.** What ordinary speech pressure is handled by learning from sparse labels, and what evidence distinguishes it from neighboring pressures?

**The pressure.** Languages differ in sounds, writing systems, grammar, prosody, code-switching, and social meaning; data and tools are distributed unevenly. The subtheme asks: What ordinary speech pressure is handled by learning from sparse labels, and what evidence distinguishes it from neighboring pressures?

**Why the easy answer breaks.** A first attempt would answer the question only with self-training, but that shortcut misses the boundary: Errors can reinforce themselves and create a false appearance of data scale.

**The move that recurs.** Across this subtheme, papers make self-training, few-shot adaptation explicit rather than treating the speech evidence as one undifferentiated variable. The reviewed full-paper mechanisms instantiate that move in different ways; for example: Continue pretraining a compact HuBERT-style model on a much wider set of African-language audio, then test whether the shared representation transfers to downstream tasks.

### Words used in this section

**Self-training.** Use a model's predictions on unlabeled speech as additional training signals, ideally filtering or weighting uncertain labels.
*Boundary:* Errors can reinforce themselves and create a false appearance of data scale.

**Few-shot adaptation.** Adjust a model to a language, speaker, or domain from a small number of examples rather than retraining from scratch.
*Boundary:* Few examples may cover only one speaker or style and make variance look like progress.

### What the evidence shows

- [AfriHuBERT: A self-supervised speech representation model for African languages](https://www.isca-archive.org/interspeech_2025/alabi25_interspeech.html) (D3): Continue pretraining a compact HuBERT-style model on a much wider set of African-language audio, then test whether the shared representation transfers to downstream tasks. **Measured or tested:** We evaluate AfriHuBERT on two key speech tasks, Spoken Language Identification (SLID) and Automatic Speech Recognition (ASR), using the FLEURS benchmark. **Limit:** Language coverage does not mean equal data quality or equal downstream performance; the languages, hours, speaker balance, and task results determine the practical reach. No independent reproduction was performed.
- [Evaluating Large Language Models in Data Generation for Low-Resource Scenarios: A Case Study on Question Answering](https://www.isca-archive.org/interspeech_2025/arisoy25_interspeech.html) (D3): Use large-language-model-generated question-answer data and test its value separately on text QA, spoken QA, and Turkish spoken QA. **Measured or tested:** Large Language Models (LLMs) are powerful tools for generating synthetic data, offering a promising solution to data scarcity in low-resource scenarios. **Limit:** Prompting, filtering, language, synthetic distribution, and evaluation splits limit transfer; synthetic gains do not establish factual or linguistic quality everywhere.
- [Better Semi-supervised Learning for Multi-domain ASR Through Incremental Retraining and Data Filtering](https://www.isca-archive.org/interspeech_2025/carofilis25_interspeech.html) (D3): Incrementally combine in-domain labels with related-domain data, then filter pseudo-labels using multi-model consensus or named-entity recognition. **Measured or tested:** We propose an incremental semi-supervised learning pipeline that first integrates a small in-domain labeled set and an auxiliary dataset from a closely related domain, achieving a relative improvement of 4% over no auxiliary data. **Limit:** The gains are bounded to the two English corpora, model ensemble, filtering thresholds, and author-reported WER; other domains and languages remain unresolved.
- [MSDA: Combining Pseudo-labeling and Self-Supervision for Unsupervised Domain Adaptation in ASR](https://www.isca-archive.org/interspeech_2025/damianos25_interspeech.html) (D3): Cascade self-supervised representation adaptation with pseudo-label training so each stage prepares the next. **Measured or tested:** MSDA is evaluated for six source-to-target Greek domain transfers using target-domain WER, comparing supervised source fine-tuning, continual pretraining, M2DS2, Meta pseudo-labeling, CASTLE, and MSDA. The corpora include 72-hour Logotypografia, 12-hour Common Voice, 99-hour HParl, and weakly… **Limit:** The languages, pseudo-label quality, source models, and domain shifts bound the claim; robustness to severely wrong pseudo-labels remains open.

**Where this boundary stops.** Errors can reinforce themselves and create a false appearance of data scale.; Few examples may cover only one speaker or style and make variance look like progress.

**What this evidence does not establish.** The shared story is supported only by the reviewed papers listed here; D2 entries support the problem and stated method, while D3 entries support the reported mechanism and evaluation. It is not a venue-wide prevalence claim.

**Question left open.** What changes when this move is tested outside the speakers, languages, rooms, devices, or benchmark conditions represented by the 10 D3 paper(s)?

## Making missing speech evidence

This boundary follows from the baseline account: baseline link: Fant pp. 5-7: physical cues vary with context and production, and a single message distinction may have different signal realizations; language-specific evidence must therefore be tested rather than assumed. Ordinary pressure: Languages differ in sounds, writing systems, grammar, prosody, code-switching, and social meaning; data and tools are distributed unevenly. Failed shortcut: Scaling an English-centered recipe or translating labels assumes that all languages expose the same units, data, and errors. Recurring paper move: Share useful structure across languages while preserving language-specific distinctions, measuring who benefits, and making uncertainty visible where evidence is thin. Neighbor test: The work creates speakers, prompts, labels, or recordings needed by a community or task.

**The question.** What ordinary speech pressure is handled by making missing speech evidence, and what evidence distinguishes it from neighboring pressures?

**The pressure.** Languages differ in sounds, writing systems, grammar, prosody, code-switching, and social meaning; data and tools are distributed unevenly. The subtheme asks: What ordinary speech pressure is handled by making missing speech evidence, and what evidence distinguishes it from neighboring pressures?

**Why the easy answer breaks.** A first attempt would answer the question only with speech data collection, but that shortcut misses the boundary: More hours do not fix biased sampling, poor transcripts, or a task definition that excludes natural speech.

**The move that recurs.** Across this subtheme, papers make speech data collection explicit rather than treating the speech evidence as one undifferentiated variable. The reviewed full-paper mechanisms instantiate that move in different ways; for example: Build open hardware whose microphone, baffle, and analog path can be changed, then compare raw scores and phonological contrasts against a commercial device.

### Words used in this section

**Speech data collection.** Design recording prompts, speakers, transcription, and consent so newly collected data covers the intended community and task.
*Boundary:* More hours do not fix biased sampling, poor transcripts, or a task definition that excludes natural speech.

### What the evidence shows

- [Nosey: Open-Source Hardware for Acoustic Nasalance](https://www.isca-archive.org/interspeech_2025/dewhurst25_interspeech.html) (D3): Build open hardware whose microphone, baffle, and analog path can be changed, then compare raw scores and phonological contrasts against a commercial device. **Measured or tested:** We also review ways of customizing the hardware to facilitate testing, such as comparison of microphones and different construction materials. **Limit:** The tested speakers, microphones, baffle geometry, placement, and phonological materials bound the comparison; raw-score offsets and cross-signal bleed prevent treating Nosey and commercial values as directly interchangeable.
- [Transcribing Oral History Recordings Using the Transcription Portal](https://www.isca-archive.org/interspeech_2025/draxler25_interspeech.html) (D3): Put recognition, human correction, and export into one preconfigured web workflow designed around the user's task rather than the model's internals. **Measured or tested:** The Transcription Portal workflow is demonstrated on four 1976 Italian oral-history interviews with five Ravensbrück survivors and approximately 18 hours of speech digitized at 96 kHz/24-bit. Evaluation is a bounded transcription-workflow demonstration comparing ASR-generated SRT material with… **Limit:** The demonstration corpus, user effort, ASR model, correction time, and export format bound the result; a convenient workflow does not establish transcription accuracy without an error audit or independent user study.
- [The NaijaVoices Dataset: Cultivating Large-Scale, High-Quality, Culturally-Rich Speech Data for African Languages](https://www.isca-archive.org/interspeech_2025/emezue25_interspeech.html) (D3): Collect a large, culturally grounded speech-text corpus and test whether it improves several ASR families. **Measured or tested:** The development of high-performing, robust, and reliable speech technologies depends on large, high-quality datasets. **Limit:** The corpus languages, collection process, transcription policy, and model choices bound the result; coverage of other African languages and deployment conditions remains open.
- [Speech LLMs in Low-Resource Scenarios: Data Volume Requirements and the Impact of Pretraining on High-Resource Languages](https://www.isca-archive.org/interspeech_2025/fong25_interspeech.html) (D3): Pretrain the small bridge between a speech encoder and language model on high-resource languages, then reuse it and measure how much low-resource data is still needed. **Measured or tested:** Using multilingual LLMs (EuroLLM, Salamandra) with whisper-large-v3-turbo, we evaluate performance on several public benchmarks, providing insights for future research on optimizing Speech LLMs for low-resource languages and multilinguality. **Limit:** Language choice, data cleanliness, projector, LLM, benchmark split, and WER bound the claim; transfer from high-resource languages does not establish equal performance or cultural adequacy.

**Where this boundary stops.** More hours do not fix biased sampling, poor transcripts, or a task definition that excludes natural speech.

**What this evidence does not establish.** The shared story is supported only by the reviewed papers listed here; D2 entries support the problem and stated method, while D3 entries support the reported mechanism and evaluation. It is not a venue-wide prevalence claim.

**Question left open.** What changes when this move is tested outside the speakers, languages, rooms, devices, or benchmark conditions represented by the 10 D3 paper(s)?

## Respecting variation and local meaning

This boundary follows from the baseline account: baseline link: Fant pp. 5-7: physical cues vary with context and production, and a single message distinction may have different signal realizations; language-specific evidence must therefore be tested rather than assumed. Ordinary pressure: Languages differ in sounds, writing systems, grammar, prosody, code-switching, and social meaning; data and tools are distributed unevenly. Failed shortcut: Scaling an English-centered recipe or translating labels assumes that all languages expose the same units, data, and errors. Recurring paper move: Share useful structure across languages while preserving language-specific distinctions, measuring who benefits, and making uncertainty visible where evidence is thin. Neighbor test: This boundary covers differences in pronunciation, variety, and local meaning that affect who is understood and how speech is interpreted; it is separate from generic low-resource learning because more data alone cannot decide whether a social or cultural distinction was represented correctly.

**The question.** What ordinary speech pressure is handled by respecting variation and local meaning, and what evidence distinguishes it from neighboring pressures?

**The pressure.** Languages differ in sounds, writing systems, grammar, prosody, code-switching, and social meaning; data and tools are distributed unevenly. The subtheme asks: What ordinary speech pressure is handled by respecting variation and local meaning, and what evidence distinguishes it from neighboring pressures?

**Why the easy answer breaks.** A first attempt would answer the question only with accent robustness, but that shortcut misses the boundary: A single pooled error rate cannot show which accents fail or whether adaptation changes identity representation.

**The move that recurs.** Across this subtheme, papers make accent robustness, dialect and variety, cultural meaning explicit rather than treating the speech evidence as one undifferentiated variable. The reviewed full-paper mechanisms instantiate that move in different ways; for example: Use voice conversion as augmentation to reduce speaker bias, then evaluate on a newly collected real-world cross-domain set.

### Words used in this section

**Accent robustness.** Maintain intended-word accuracy across pronunciation patterns that differ from the training majority.
*Boundary:* A single pooled error rate cannot show which accents fail or whether adaptation changes identity representation.

**Dialect and variety.** Treat grammar, vocabulary, pronunciation, and discourse conventions of a variety as part of the language, not merely deviations from a standard.
*Boundary:* Dialect labels can be contested and may conflate region, ethnicity, class, and speaker identity.

**Cultural meaning.** Interpret politeness, indirectness, emotion, and conversational norms within the community that uses them.
*Boundary:* A label imported from another culture may be statistically convenient but semantically wrong.

### What the evidence shows

- [Voice Conversion Improves Cross-Domain Robustness  for Spoken Arabic Dialect Identification](https://www.isca-archive.org/interspeech_2025/abdullah25_interspeech.html) (D3): Use voice conversion as augmentation to reduce speaker bias, then evaluate on a newly collected real-world cross-domain set. **Measured or tested:** Evaluated on a newly collected real-world test set spanning four different domains, our approach yields consistent improvements of up to +34.1% in accuracy across domains. **Limit:** The result is specific to Arabic dialect identification and the released artifacts require separate access and execution checks.
- [Is it all about race?: A Cross-examination of /s/ in a Multilingual (Nigerian) Context](https://www.isca-archive.org/interspeech_2025/amoniyan25_interspeech.html) (D3): Cross-examine /s/ production in a multilingual Nigerian context using linguistic and social context. **Measured or tested:** The analysis uses 4,056 /s/ tokens from 42 Nigerian English speakers across Hausa, Igbo, and Yoruba groups. CoG, duration, skewness, and zero-crossing measures are analyzed with mixed-effects regressions using gender, birth year, segment duration, speaker, and phonological environment; reported… **Limit:** Community, language, sampling, annotation, and interpretation bound transfer.
- [LID Models are Actually Accent Classifiers: Implications and Solutions for LID on Accented Speech](https://www.isca-archive.org/interspeech_2025/bafna25_interspeech.html) (D3): Add phoneme-sequence or discretized-unit views and test the shortcut by permuting short speech chunks. **Measured or tested:** Prior research indicates that LID model performance significantly declines on accented speech; however, the specific causes, extent, and characterization of these errors remain under-explored. **Limit:** Datasets, accent categories, chunking, and aggregation define the result; it diagnoses a shortcut but does not prove cultural neutrality or universal transfer.
- [Accent Normalization Using Self-Supervised Discrete Tokens with Non-Parallel Data](https://www.isca-archive.org/interspeech_2025/bai25_interspeech.html) (D3): Use self-supervised discrete tokens, nonparallel conversion, flow matching, and explicit duration preservation. **Measured or tested:** Accent normalization is evaluated on seven accents from L2-ARCTIC/ARCTIC, with four speakers per accent, 50 validation and 80 held-out test sentences, and one unseen speaker per accent. WER, speaker-embedding cosine similarity, MUSHRA naturalness/accentedness, and best-worst speaker similarity are… **Limit:** Accent definitions, targets, subjective judgments, and nonparallel training bound the claim; native-like is not universally better.

**Where this boundary stops.** A single pooled error rate cannot show which accents fail or whether adaptation changes identity representation.; Dialect labels can be contested and may conflate region, ethnicity, class, and speaker identity.; A label imported from another culture may be statistically convenient but semantically wrong.

**What this evidence does not establish.** The shared story is supported only by the reviewed papers listed here; D2 entries support the problem and stated method, while D3 entries support the reported mechanism and evaluation. It is not a venue-wide prevalence claim.

**Question left open.** What changes when this move is tested outside the speakers, languages, rooms, devices, or benchmark conditions represented by the 20 D3 paper(s)?

## Closing note

This essay is a map of recurring problems and research moves, not a leaderboard or a claim that these categories cover every speech study. The paper links and depth labels show what was actually checked; they do not turn reported results into independent facts.
