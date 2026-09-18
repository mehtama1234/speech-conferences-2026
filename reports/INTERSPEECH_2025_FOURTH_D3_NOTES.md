# INTERSPEECH 2025 fourth-pass full-paper notes

This batch adds eight D3 notes, one per first-principles theme, selected to fill conceptual gaps in the earlier 24-paper sample. They are based on captured official PDFs and remain paper-reported, not independently reproduced.

## 1. sound-and-production

**Paper:** [Subtyping Speech Errors in Childhood Speech Sound Disorders with Acoustic-to-Articulatory Speech Inversion](https://www.isca-archive.org/interspeech_2025/benway25_interspeech.html)  
**Evidence:** D3; PDF SHA-256 `9b0e95c7f7c42854aa709f68cece092b5c88bb35f048fa63a60c229b7b680878`; 5 pages.

- **Big picture:** Clinicians need to distinguish different childhood speech-sound errors, but an acoustic recording does not directly show which articulator moved incorrectly.
- **Why hard:** Perceptually similar errors can arise from different vocal-tract configurations, and a predicted tract variable is only useful clinically if it separates meaningful error subtypes rather than creating uninterpretable coordinates.
- **Naive attempt:** Measure acoustic differences alone or treat an acoustic-to-articulatory inversion output as a direct clinical diagnosis.
- **Central move:** Use acoustic-to-articulatory inversion to obtain interpretable movement variables, then test subtype differences with a mixed-effects statistical model across children and target sounds.
- **Mechanism:** The study compares inverted articulatory trajectories for correct and erroneous /r/ and /s/ productions in children with speech sound disorders, models repeated observations with linear mixed effects, and asks which tract variables differ between perceptually defined subtypes.
- **Mathematical idea:** The inversion maps acoustics to estimated articulator variables; linear mixed modeling separates subtype effects from repeated-speaker and item variation. Statistical significance is evidence of group differences, not proof that the inversion recovered physical motion exactly.
- **Connections:** Connects production physics to clinical speech analysis and illustrates the boundary between a useful intermediate representation and a diagnosis. It complements articulatory-inversion papers focused on prediction accuracy.
- **What paper reports:** The paper reports statistically significant articulatory differences among several perceptually salient /r/ and /s/ error subtypes and correct targets in American English.
- **Limits:** The study is limited to selected American-English child error types and an inversion model; clinical interpretability is demonstrated for these comparisons, not established for all disorders or speakers. No independent reproduction was performed.

## 2. listening-and-separation

**Paper:** [First Analyze Then Enhance: A Task-Aware System for Speech Separation, Denoising, and Dereverberation](https://www.isca-archive.org/interspeech_2025/dang25_interspeech.html)  
**Evidence:** D3; PDF SHA-256 `ae4baeb356fabf28a030ed529860f03f68e01222f201c8ecc4b9155d320d2e21`; 5 pages.

- **Big picture:** A microphone may contain clean speech, noise, echo, or several speakers at once; running every expensive repair stage on every signal wastes computation and can damage already-clean speech.
- **Why hard:** The same observed waveform can require different operations, and separation, denoising, and dereverberation can interfere when cascaded in the wrong order.
- **Naive attempt:** Send every input through one universal enhancement network or a fixed sequence of all enhancement modules.
- **Central move:** Analyze the degradation first, route the signal only through the needed modules, and train the modules separately before integrating them.
- **Mechanism:** A lightweight analyzer uses frozen Whisper/WavLM features, LSTMs, pooling, and a classifier to choose among clean, mixture, noisy/reverberant, and combined conditions. A separator with an attractor estimates an unknown speaker count; a refiner handles noise and reverberation. NAT pretrains separation under noise and DIT trains separator/refiner paths before joint fine-tuning.
- **Mathematical idea:** The analyzer uses four-class cross-entropy. Refinement uses negative SI-SNR; separation uses permutation-invariant SI-SNR so source order does not matter; the attractor uses binary cross-entropy with a stop symbol.
- **Connections:** This is conditional computation: first infer what evidence is missing, then spend capacity on the corresponding repair. It belongs beside source separation and robustness work, but its routing classifier becomes a new failure point.
- **What paper reports:** On Libri-3Mix-derived data covering eleven clean, noisy, reverberant, mixed, and combined conditions, FATE reports comparable enhancement quality while reducing unnecessary processing and avoiding overprocessing clean inputs.
- **Limits:** The degradations are simulated and drawn from specified mixtures, noises, and rooms; real rooms, analyzer errors, and out-of-distribution combinations are not established. The reported score is author-reported and was not independently reproduced.

## 3. recognition-and-alignment

**Paper:** [CMT-LLM: Contextual Multi-Talker ASR Utilizing Large Language Models](https://www.isca-archive.org/interspeech_2025/he25_interspeech.html)  
**Evidence:** D3; PDF SHA-256 `ad5f1a7a62238c7951c28a472bf61be2c975daa7d28dacdcc8ee7e03549ddb09`; 5 pages.

- **Big picture:** In meetings, a recognizer must decide both who said what when voices overlap and which rare technical words are plausible in the current context.
- **Why hard:** A multi-talker transcript is not a single ordinary sentence, while a huge biasing list can distract decoding; treating overlap and rare-word biasing as separate repairs leaves their interaction unresolved.
- **Naive attempt:** Use serialized output training for overlap and add a generic bias list or shallow fusion after decoding.
- **Central move:** Make multi-talker transcription and contextual biasing one sequence-generation task: represent speakers in first-in-first-out order and filter the biasing list before placing relevant rare words into the language model prompt.
- **Mechanism:** A speech encoder produces frame representations, convolution downsamples them, a projector matches the LLM hidden size, and an LLM emits text separated by speaker-change tokens. A first decoding pass supplies evidence for a two-stage filter that selects rare words from a list of up to 1,000 before a second pass.
- **Mathematical idea:** The system minimizes token cross-entropy on serialized transcripts. WER is computed on LibriMix and AMI single-device microphone data under different bias-list sizes; the central decision is which context terms enter the decoder, not a new acoustic metric.
- **Connections:** Joins two uncertainties: source assignment in the waveform and lexical choice in the transcript. It bridges separation-aware ASR and open-vocabulary contextual biasing.
- **What paper reports:** The paper reports WER of 7.9% on LibriMix and 32.9% on AMI SDM at biasing size 1,000, outperforming compared contextual-biasing approaches in its reported settings.
- **Limits:** FIFO serialization imposes an ordering convention; the bias list and first-pass filter supply information that may not exist in every deployment. WER does not separately reveal speaker attribution, rare-word recall, or hallucination cost, and results were not independently reproduced.

## 4. meaning-and-interaction

**Paper:** [FD-Bench: A Full-Duplex Benchmarking Pipeline Designed for Full Duplex Spoken Dialogue Systems](https://www.isca-archive.org/interspeech_2025/peng25b_interspeech.html)  
**Evidence:** D3; PDF SHA-256 `4af22e7595d4e2e61f49815d1d5c666f2f5e9c9df59d8af371f438650c915158`; 5 pages.

- **Big picture:** A full-duplex spoken agent must keep listening while speaking, handle interruptions, and respond to backchannels without waiting for a neat turn boundary.
- **Why hard:** Traditional dialogue benchmarks assume alternating turns and therefore miss failures caused by latency, interruption timing, overlap, and noisy simultaneous speech.
- **Naive attempt:** Evaluate a duplex agent with ordinary response quality or word-error scores and assume those scores reveal interruption behavior.
- **Central move:** Construct a benchmark that generates controlled full-duplex conversations and measures interruption handling, delay, and robustness with metrics designed for overlapping interaction.
- **Mechanism:** FD-Bench combines generated speech, TTS, ASR, and LLM-based scenario control to create over 40 hours of speech, 293 simulated conversations, and 1,200 interruptions. It runs three open-source full-duplex systems through the same scenarios and records response and interruption outcomes.
- **Mathematical idea:** The benchmark defines event-level metrics over interruption and delay conditions rather than reducing the interaction to one transcript score. Its denominator is the simulated conversation/interruption set, not ordinary ASR utterances.
- **Connections:** Shows evaluation as part of the interaction mechanism: if the benchmark omits overlap, the system can look good while failing the human experience. It links turn-taking, deployment, and human-centered evaluation.
- **What paper reports:** The reported benchmark finds that all three tested systems still struggle with user interruptions, frequent disruptions, and noisy conditions; the paper states that data and code will be released.
- **Limits:** The conversations and interruptions are simulated/generated, and benchmark metrics are proxies for human experience. Release claims are not equivalent to artifact execution here; no independent reproduction or user study was performed.

## 5. voice-generation-and-control

**Paper:** [REWIND: Speech Time Reversal for Enhancing Speaker Representations in Diffusion-based Voice Conversion](https://www.isca-archive.org/interspeech_2025/biyani25_interspeech.html)  
**Evidence:** D3; PDF SHA-256 `9ff3e2a720a31008a1e6a986537e9607a3649ac3e9377ed7b302be8de9441d6c`; 5 pages.

- **Big picture:** A voice-conversion system should preserve who the target speaker sounds like without allowing linguistic content to dominate the speaker representation.
- **Why hard:** Reversing speech destroys intelligible phonemes and syllables but leaves broad tonal and vocal characteristics, exposing a way to train speaker representations with less language information.
- **Naive attempt:** Train speaker representations only on ordinary speech and assume the embedding will learn identity while ignoring linguistic content.
- **Central move:** Use time-reversed speech as an augmentation: it removes much of the linguistic structure while retaining speaker-related cues, then use the resulting representations in diffusion-based voice conversion.
- **Mechanism:** The full waveform is reversed, passed through the speaker-representation pipeline, and used as an additional training view. The conversion model conditions generation on speaker information while its content path carries the linguistic signal; experiments compare diffusion VC systems with and without the reversed-speech augmentation.
- **Mathematical idea:** The paper evaluates speaker similarity and speech quality rather than treating reversal as a new waveform objective. The conceptual operation is an information intervention: destroy temporal phoneme order while retaining slower vocal traits.
- **Connections:** Connects representation disentanglement to a physical transformation of the signal. It belongs beside speaker conversion, privacy, and identity-preserving generation, but “retained speaker information” is established only through the tested similarity measures.
- **What paper reports:** The paper reports significantly improved speaker-similarity scores while maintaining high speech quality in diffusion-based voice-conversion experiments.
- **Limits:** Time reversal may remove more or less information depending on language and model; the experiments do not establish universal speaker/language disentanglement or human identity judgments across populations. No independent reproduction was performed.

## 6. people-variation-and-health

**Paper:** [Evaluating Parameter Sharing for Spoofing-Aware Speaker Verification: A Case Study on the ASVspoof 5 Dataset](https://www.isca-archive.org/interspeech_2025/buker25_interspeech.html)  
**Evidence:** D3; PDF SHA-256 `c10f4ab95a8271f203d31b5d3ab0cc5ec5d55cf2d9f7661167314b7480b84d38`; 5 pages.

- **Big picture:** A speaker-verification system can accept the wrong person when a spoofed recording resembles the claimed speaker, so identity matching and attack detection must work together under changing codecs and attacks.
- **Why hard:** SASV combines two decisions—does the voice match, and is the signal genuine—and joint training can help one while harming the other; attack types and compression conditions change the balance.
- **Naive attempt:** Train an ASV verifier and a countermeasure independently, or share all parameters without testing which sharing pattern fits which attack.
- **Central move:** Systematically compare parameter-sharing strategies for the verifier and spoof countermeasure, treating sharing as an experimental variable rather than an automatic improvement.
- **Mechanism:** On ASVspoof 5, the study varies which modules share parameters and evaluates the resulting SASV systems across attack types and codec conditions, comparing min a-DCF and relative performance changes to an unshared baseline.
- **Mathematical idea:** The main decision metric is minimum tandem detection cost, which combines false acceptance and false rejection costs for speaker and spoof decisions. The method question is whether shared representations improve this joint operating tradeoff.
- **Connections:** Makes security a coupled decision problem rather than a binary “deepfake” label. It links speaker identity, robustness, deployment conditions, and accountable evaluation.
- **What paper reports:** The paper reports min a-DCF improving from 0.329 to 0.233 for the A26 attack with parameter sharing and a 14.09% gain for AMR-compressed signals in the tested setup.
- **Limits:** Benefits are attack- and codec-specific; the ASVspoof 5 protocols do not exhaust future generators or deployment channels. min a-DCF is a system-level proxy, not proof of safe authentication, and no independent reproduction was performed.

## 7. languages-accents-and-resources

**Paper:** [Can we train ASR systems on Code-switch without real code-switch data? Case study for Singapore's languages](https://www.isca-archive.org/interspeech_2025/nguyen25_interspeech.html)  
**Evidence:** D3; PDF SHA-256 `5a13d223637e69fd8b427d504325887c9b35dfb2f851bc3c2e286e3da3f40061`; 5 pages.

- **Big picture:** Code-switched speech is common but expensive to transcribe, especially for under-resourced language pairs, so an ASR system needs useful mixed-language examples without requiring a new labeled corpus.
- **Why hard:** Switches occur at phrase boundaries and differ by language pair; naïvely concatenating monolingual data produces mixtures unlike spontaneous speech and may help one language while hurting another.
- **Naive attempt:** Fine-tune a pretrained ASR model only on monolingual data or create synthetic mixtures by randomly swapping isolated words.
- **Central move:** Generate phrase-level synthetic code-switching data from monolingual augmented speech, then use it to adapt large pretrained ASR models and evaluate several Southeast Asian language pairs.
- **Mechanism:** The paper creates phrase-mixed speech for Malay-English, Mandarin-Malay, and Tamil-English, fine-tunes Whisper, MMS, and SeamlessM4T, and compares monolingual and code-switched test performance against training without real code-switch recordings.
- **Mathematical idea:** The outcome is word error rate on monolingual and code-switched benchmarks, with gains compared across language pairs and pretrained models. The crucial design choice is the data distribution used for fine-tuning.
- **Connections:** Makes data creation a conceptual mechanism: preserve the linguistic boundary structure of switching instead of treating the low-resource problem as merely a smaller model. It links multilingual transfer to unequal evidence and cultural boundaries.
- **What paper reports:** The authors report improved ASR on monolingual and code-switched tests, with the largest gains for BM-EN followed by TA-EN and ZH-BM.
- **Limits:** Synthetic phrase mixing is an approximation to spontaneous switching, and the three language pairs do not represent all multilingual communities. WER does not measure whether switches are socially or linguistically natural, and no independent reproduction was performed.

## 8. evaluation-deployment-and-consequence

**Paper:** [Unmasking real-world audio deepfakes: A data-centric approach](https://www.isca-archive.org/interspeech_2025/combei25_interspeech.html)  
**Evidence:** D3; PDF SHA-256 `7f55bfdbd5a5fe183864ad809405f55cabf4e4dc66426a106ef852a6b332783a`; 5 pages.

- **Big picture:** Deepfake detectors that perform well on specially collected datasets can fail on the messy recordings people encounter in the world, so robustness depends on what examples the dataset contains.
- **Why hard:** Real-world audio varies in recording chain, edits, generators, and social context; increasing model complexity cannot repair a dataset that omits those variations.
- **Naive attempt:** Train a larger detector on a benchmark dataset and interpret a low equal-error rate as deployment readiness.
- **Central move:** Treat curation, pruning, and augmentation of real-world examples as the primary intervention, then test generalization on both an in-the-wild set and a newly collected real-world set.
- **Mechanism:** The study introduces the AI4T real-world deepfake dataset, analyzes data quality and coverage, applies data-centric filtering and augmentation, and evaluates detector systems on five public datasets plus the new set.
- **Mathematical idea:** Equal error rate is the operating point where false acceptance and false rejection meet; relative EER reduction compares the data-centric system with its baseline on each dataset. The denominator is each named test corpus, not all possible real-world audio.
- **Connections:** Reframes robustness as a measurement/data problem rather than only a model architecture problem. It connects security evaluation to provenance, distribution shift, and the danger of benchmark proxies.
- **What paper reports:** The paper reports a 55% relative EER reduction on In-the-Wild to 1.7% absolute EER and a 63% reduction on AI4T after the data-centric interventions.
- **Limits:** The new dataset and curation choices define the tested notion of real-world variation; future generators and channels may differ. EER is not a guarantee of safe moderation or authentication, and no independent reproduction was performed.
