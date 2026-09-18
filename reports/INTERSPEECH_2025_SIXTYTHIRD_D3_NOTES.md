# INTERSPEECH 2025 sixty-third-pass full-paper notes

Eight additional captured-PDF readings extend D3 comparison beyond the prior seed.

## 1. dialogue-and-social-speech

**Paper:** [Investigating the Reasoning Abilities of Large Language Models for Understanding Spoken Language in Interpersonal Interactions](https://www.isca-archive.org/interspeech_2025/aggarwal25_interspeech.html)
**Evidence:** D3; PDF SHA-256 379dfe0c14c98a674362c1e38020aa556e52d6d32de7d5d20849c15ad992a6e2; full text captured.

- **Ordinary problem:** An interview coach must judge whether a spoken answer addresses the interpersonal question, not merely whether its words are grammatical.
- **Why hard:** Interview answers depend on context, social intent, turn history, and domain knowledge that surface lexical matching misses.
- **Naive attempt:** Ask a general language model to answer from the transcript alone and treat fluent text as understanding.
- **Central move:** Evaluate large language models on spoken-interaction reasoning with explicit contextual knowledge and prompt structure.
- **Mechanism:** Supply interview context and domain knowledge, compare prompting strategies and model scales, and score both answer quality and reasoning behavior.
- **Mathematical/conceptual structure:** Prompt conditions act as information controls: context and domain knowledge reduce ambiguity, while ablations reveal which information supports the decision.
- **Evaluation:** VetTrain interview data are used with quantitative and qualitative evaluation, model-size comparisons, and prompt ablations involving domain knowledge and interaction context.
- **What paper reports:** The paper reports that contextual and domain-knowledge prompting improves selected spoken-interaction reasoning settings, especially for larger models.
- **Limits:** Interview distribution, transcript quality, subjective scoring, prompt sensitivity, and model-family coverage limit claims about general conversational understanding.

## 2. voice-conversion-and-identity

**Paper:** [When Humans Growl and Birds Speak: High-Fidelity Voice Conversion from Human to Animal and Designed Sounds](https://www.isca-archive.org/interspeech_2025/kang25b_interspeech.html)
**Evidence:** D3; PDF SHA-256 f7fead0497c8eb4611b3d8727f790aa5b2104f3dfba26e8d9e29fa4243db0988; full text captured.

- **Ordinary problem:** A voice converter should carry identity and expressive qualities across human, animal, or designed sound domains without collapsing the target sound.
- **Why hard:** Source and target domains differ in pitch structure, timbre, articulation, and available parallel data.
- **Naive attempt:** Copy a human speaker embedding into the target domain or train paired conversion on a narrow set of source and target voices.
- **Central move:** Learn high-fidelity cross-domain conversion that preserves controllable identity cues while generating a plausible target-domain signal.
- **Mechanism:** Separate content-like and identity-like evidence, condition generation on the desired target sound, and evaluate both acoustic fidelity and perceptual identity.
- **Mathematical/conceptual structure:** The conversion mapping must preserve information useful for the target domain while discarding source-domain artifacts; perceptual judgments test whether this tradeoff is believable.
- **Evaluation:** The paper evaluates human-to-animal and designed-sound conversion with objective audio comparisons and listener judgments against conversion baselines.
- **What paper reports:** The authors report improved fidelity and plausibility for cross-domain conversion, while the unusual targets expose failures hidden by ordinary human voice-conversion benchmarks.
- **Limits:** Sparse target data, subjective evaluation, target-domain definitions, and unclear physical correspondence limit claims of general voice conversion.

## 3. fairness-and-social-risk

**Paper:** [Investigating Gender Bias in Text-to-Audio Generation Models](https://www.isca-archive.org/interspeech_2025/mohsin25_interspeech.html)
**Evidence:** D3; PDF SHA-256 474edc54c8280107180a51ad817640ffc1b522b2da1359cc26e4511f50b888bc; full text captured.

- **Ordinary problem:** A text-to-audio generator should not turn neutral prompts into systematically gendered sound or reproduce stereotypes as if they were acoustic facts.
- **Why hard:** Training captions and web audio encode social stereotypes, and a plausible sample can conceal unequal behavior across prompt groups.
- **Naive attempt:** Report aggregate generation quality and assume that a named model is neutral unless an obvious failure is heard.
- **Central move:** Define a measurable gender-bias audit for text-to-audio outputs and compare model behavior across controlled prompts.
- **Mechanism:** Generate matched prompt sets, classify or rate gendered attributes, and aggregate the results into a bias score that makes asymmetry visible.
- **Mathematical/conceptual structure:** The audit compares conditional output distributions rather than a single sample; the metric converts a social-risk question into a reproducible disparity measurement.
- **Evaluation:** Multiple text-to-audio systems and controlled prompt sets are evaluated with the proposed gender-bias metric and qualitative inspection.
- **What paper reports:** The paper reports frequent gender bias that reflects training-data stereotypes and argues for explicit bias evaluation in text-to-audio systems.
- **Limits:** Gender labels, annotator assumptions, prompt coverage, model versions, and the proposed metric's validity limit causal or cultural conclusions.

## 4. grounding-and-action

**Paper:** [Discrete Audio Representations for Automated Audio Captioning](https://www.isca-archive.org/interspeech_2025/tian25_interspeech.html)
**Evidence:** D3; PDF SHA-256 f9ad0922ba37c8533490d85982fa17b0062f5bdaa44ef7aecc883ad9191685b9; full text captured.

- **Ordinary problem:** An audio captioner must preserve sound events in a compact representation while giving a language decoder enough evidence to describe them.
- **Why hard:** Audio contains simultaneous events and fine timing, but a caption model must compress it before generating variable-length language.
- **Naive attempt:** Use one continuous embedding or a generic tokenizer and assume reconstruction preserves whatever captioning needs.
- **Central move:** Compare discrete audio representations for caption generation and test whether tokenization retains semantic evidence.
- **Mechanism:** Encode audio into learned discrete tokens, condition a text decoder on those tokens, and compare tokenizers and decoder choices on caption metrics.
- **Mathematical/conceptual structure:** Quantization creates a finite vocabulary of acoustic units; the central question is whether the units preserve event identity rather than merely waveform detail.
- **Evaluation:** Experiments on Clotho compare discrete tokenization methods and captioning systems with standard automatic caption metrics and representation ablations.
- **What paper reports:** The paper reports that selected audio tokenizers improve automated captioning quality, showing that representation design affects semantic generation.
- **Limits:** Reference-caption incompleteness, metric proxy limits, dataset scope, and no broad human grounding study limit conclusions about listener usefulness.

## 5. grounding-and-action

**Paper:** [Towards Diverse and Efficient Audio Captioning via Diffusion Models](https://www.isca-archive.org/interspeech_2025/xu25_interspeech.html)
**Evidence:** D3; PDF SHA-256 0d822af0fcafe171fce50808f7eecd05cbb2badc3c06aa84db62e3f2d7a3a72c; full text captured.

- **Ordinary problem:** An audio captioner should describe the same sound accurately in several natural ways instead of producing one brittle sentence or repeating training phrasing.
- **Why hard:** Sound events are ambiguous and captions are one-to-many: several descriptions can be correct while lexical metrics prefer one wording.
- **Naive attempt:** Use a deterministic autoregressive decoder and optimize likelihood toward a single reference style.
- **Central move:** Use diffusion-based caption generation to model multiple plausible descriptions while retaining event fidelity.
- **Mechanism:** Condition iterative denoising on audio representations, sample candidate text representations, and decode captions whose diversity can be measured alongside quality.
- **Mathematical/conceptual structure:** Diffusion represents a distribution over possible captions; sampling exposes the tradeoff between semantic accuracy, diversity, and computation.
- **Evaluation:** DAC is evaluated on audio-captioning benchmarks with caption-quality and diversity metrics, efficiency comparisons, and ablations of the diffusion design.
- **What paper reports:** The paper reports stronger caption quality and diversity than comparison systems, with the stochastic decoder offering broader descriptions.
- **Limits:** Automatic diversity can reward irrelevant variation, sampling cost matters, references are incomplete, and benchmark audio limits transfer.

## 6. source-separation-and-spatial-listening

**Paper:** [Position also matters! Separating Same Instruments in String Quartet using Timbral and Positional Cues](https://www.isca-archive.org/interspeech_2025/xu25b_interspeech.html)
**Evidence:** D3; PDF SHA-256 2d18c220e4f553706e041039928607c3aab3ade61583f5db874d9a067fae38e4; full text captured.

- **Ordinary problem:** A listener should be able to separate same-instrument parts in a quartet when timbre alone is insufficient and room position carries the distinction.
- **Why hard:** Same instruments have similar spectra, while reverberation and changing seating alter the spatial cues needed to assign each source.
- **Naive attempt:** Train a separator on isolated modern music or rely only on instrument timbre, ignoring position and room response.
- **Central move:** Use timbral and positional cues and evaluate generalization to a seating arrangement not used for training.
- **Mechanism:** Represent spectral identity together with spatial or positional evidence, then estimate each instrument while preserving the quartet mixture's structure.
- **Mathematical/conceptual structure:** Separation is an inverse mixture problem: the model uses complementary cues to resolve sources whose timbral likelihoods overlap.
- **Evaluation:** A new reverberant string-quartet dataset tests the proposed separator across seating arrangements against state-of-the-art separation methods.
- **What paper reports:** The authors report competitive or improved separation and transfer to a new arrangement, indicating that positional cues complement timbre.
- **Limits:** One quartet domain, limited seating and recording conditions, dataset scale, and source-isolation metrics limit claims about music separation broadly.

## 7. text-to-audio-and-content

**Paper:** [Audiobox TTA-RAG: Improving Zero-Shot and Few-Shot Text-To-Audio with Retrieval-Augmented Generation](https://www.isca-archive.org/interspeech_2025/yang25h_interspeech.html)
**Evidence:** D3; PDF SHA-256 f4aa338bf983b8e77e44f28c61798e4d308b9234452119db3176e54d135c9478; full text captured.

- **Ordinary problem:** A text-to-audio system should retrieve acoustically relevant examples when a prompt describes a rare event, without requiring retraining for every new sound.
- **Why hard:** Zero-shot prompts may be underspecified and generative models inherit gaps and stereotypes from training data.
- **Naive attempt:** Generate directly from text with a fixed model and assume its parametric memory covers rare or compositional events.
- **Central move:** Add retrieval-augmented conditioning so generated audio can use examples selected from an external datastore.
- **Mechanism:** Retrieve top-k semantically related audio or captions, inject them into the conditioning context, and compare retrieval strategies without changing the generator's core weights.
- **Mathematical/conceptual structure:** Retrieval changes the evidence available at generation time; matched comparisons test whether external examples improve conditional likelihood and perceptual relevance.
- **Evaluation:** Audiobox TTA-RAG evaluates retrieval variants and zero-/few-shot text-to-audio generation on multiple metrics and curated evaluation sets.
- **What paper reports:** The paper reports improved generation metrics while preserving few-shot and zero-shot operation, with retrieval choice affecting the result.
- **Limits:** Datastore curation, retrieval leakage, metric validity, prompt coverage, and compute/memory cost limit claims about open-world generation.

## 8. source-separation-and-spatial-listening

**Paper:** [Efficient and Microphone-Fault-Tolerant 3D Sound Source Localization](https://www.isca-archive.org/interspeech_2025/yang25q_interspeech.html)
**Evidence:** D3; PDF SHA-256 9baafb3fd7829b204652a6bc6324d2dcb334961cf9b231337d42029dc16dc478; full text captured.

- **Ordinary problem:** A 3D sound-localization system should continue locating sources when microphones are few, fail, or provide unreliable measurements.
- **Why hard:** Localization depends on spatial geometry and synchronized channels, so a bad microphone can create confident but incorrect direction evidence.
- **Naive attempt:** Use every microphone equally and add hardware redundancy whenever a channel fails.
- **Central move:** Learn efficient 3D localization with explicit microphone-fault tolerance and fewer input channels.
- **Mechanism:** Fuse spatial cues with a fault-aware weighting or inference rule, detect unreliable channels, and estimate direction without assuming all sensors are healthy.
- **Mathematical/conceptual structure:** The system treats sensor selection as part of localization: reducing the active array saves computation while robustness prevents one channel from dominating the spatial estimate.
- **Evaluation:** Simulated and measured microphone faults are evaluated for 3D localization accuracy, computational efficiency, and performance as the number of input microphones changes.
- **What paper reports:** The paper reports competitive localization with fewer microphones and improved tolerance to unreliable or unknown faults.
- **Limits:** Array geometry, fault simulation, room conditions, source count, and calibration assumptions limit deployment claims.

