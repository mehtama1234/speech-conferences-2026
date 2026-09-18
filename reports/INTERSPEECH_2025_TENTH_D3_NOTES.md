# INTERSPEECH 2025 tenth-pass full-paper notes

Eight additional official-PDF analyses target the thinnest D3 subthemes and add deployment and metric comparisons. Results remain author-reported and were not independently reproduced.

## 1. sound-and-production/time-frequency-measurement

**Paper:** [Extended High-frequency Cues to Phoneme Recognition: Insights from ASR](https://www.isca-archive.org/interspeech_2025/guo25b_interspeech.html)  
**Evidence:** D3; PDF SHA-256 e1e86ca88d7d94a3128474376cd8c301249a5cc7f2084765f0abaf22671fd3cf; 5 pages.

- **Big picture:** Speech in noise may depend on acoustic information above the frequency range normally used by speech systems.
- **Why hard:** High-frequency cues can be masked, and an ASR result does not automatically explain why a human listener benefits from them.
- **Naive attempt:** Discard everything above 6–8 kHz because it is assumed irrelevant to phonemes.
- **Central move:** Use a phoneme recognizer as a controlled probe of which frequency bands help under masking and spatial separation.
- **Mechanism:** A neural network decodes phonemes from cochleagrams of broadband, 8-kHz-low-pass, and 6-kHz-low-pass speech under quiet and masked conditions.
- **Mathematical idea:** Recognition accuracy and phoneme-omission probabilities are compared across target-to-masker ratios, filtering conditions, and consonant/vowel classes.
- **Connections:** The model is a probe for an acoustic cue, not proof that it hears like a person.
- **What paper reports:** Broadband speech improves phoneme accuracy in masked conditions, especially at lower TMR, while adding no quiet-condition benefit; removing extended high frequencies increases consonant omissions.
- **Limits:** VCTK speech, selected maskers, cochleagram assumptions, and a model-based probe bound the conclusion; audiological benefit and general ASR deployment are not established.

## 2. listening-and-separation/echo-and-reconstruction

**Paper:** [Room Impulse Response as a Prompt for Acoustic Echo Cancellation](https://www.isca-archive.org/interspeech_2025/zhao25b_interspeech.html)  
**Evidence:** D3; PDF SHA-256 facff4f7fe6dc4d1ec26cd48ca70151cb06336430c3832074dbb344c66fb74ed; 5 pages.

- **Big picture:** Echo cancellation must work when the room's echo path differs from anything seen during training.
- **Why hard:** The echo path is hidden, changes with geometry, and can be noisy when measured; double talk makes suppression without near-end damage harder.
- **Naive attempt:** Train on synthetic mixtures and assume the learned filter generalizes to every room.
- **Central move:** Give the model a room impulse response as a prompt so it can condition cancellation on acoustic structure at test time.
- **Mechanism:** ICCRN receives several RIR-prompt fusion variants; tests cover matched and mismatched synthetic RIRs plus recorded real RIRs in double-talk and far-end single-talk conditions.
- **Mathematical idea:** ERLE measures echo suppression, PESQ near-end quality, SDR near-end fidelity, and MACs/parameters expose the prompt cost.
- **Connections:** The room response becomes an explicit conditioning variable instead of an unobserved nuisance.
- **What paper reports:** Fusion method (d) is strongest on mismatched and real-RIR ICCRN tests; the reported real-RIR double-talk values are PESQ 2.19 and ERLE 4.79.
- **Limits:** The selected model, fusion choices, RIRs, and author-reported tables bound the claim; independent reproduction and broad room coverage remain absent.

## 3. recognition-and-alignment/boundaries-and-sequence-structure

**Paper:** [Towards Multi-Level Transcript Segmentation: LoRA Fine-Tuning for Table-of-Contents Generation](https://www.isca-archive.org/interspeech_2025/freisinger25_interspeech.html)  
**Evidence:** D3; PDF SHA-256 9bd21deab64e665950eff969da93cf701f3445a323d0445b98b095fcc38467c8; 5 pages.

- **Big picture:** Long transcripts are easier to use when topics are organized into nested sections rather than one flat stream.
- **Why hard:** Spoken transcripts lack visible chapters, boundaries are ambiguous, and coarse and fine topic changes must be represented across languages and recordings.
- **Naive attempt:** Predict one boundary label at each position and evaluate only whether a nearby cut is correct.
- **Central move:** Generate a hierarchical table of contents and use a metric that respects its levels; add pause duration only when training can use it.
- **Mechanism:** TOC-NEMO uses LoRA fine-tuning and optional pause cues on AMI, VideoAula, and LectureDE; zero-shot prompting and supervised baselines provide comparisons.
- **Mathematical idea:** Linear F1/B and hierarchical B distinguish flat boundary quality from agreement across levels; bootstrap and leave-one-speaker-out averages are reported.
- **Connections:** A boundary's meaning depends on the level of organization it creates, not only its time location.
- **What paper reports:** Fine-tuned TOC-NEMO plus pause cues reports the strongest linear scores, including AMI F1 30.34/B 24.81 and VideoAula F1 67.34/B 55.18.
- **Limits:** Datasets, prompts, annotations, and metric behavior constrain the result; transcript segmentation is not proof of human topic understanding.

## 4. voice-generation-and-control/text-to-speech-and-content

**Paper:** [Efficient Streaming TTS Acoustic Model with Depthwise RVQ Decoding Strategies in a Mamba Framework](https://www.isca-archive.org/interspeech_2025/lee25h_interspeech.html)  
**Evidence:** D3; PDF SHA-256 a0662bcda4333905aa6032b3a56bfcdb8dd9b86a10d509ed44fe2506f7e6481b; 5 pages.

- **Big picture:** A useful device speech generator must be intelligible, natural, fast enough for streaming, and usable across speakers.
- **Why hard:** Codec TTS often predicts several discrete code levels sequentially, making large models slow even when waveform quality is good.
- **Naive attempt:** Use a large autoregressive decoder and accept long latency, or predict code levels independently and lose their dependencies.
- **Central move:** Use a Mamba acoustic model with depthwise residual-codec decoding: masked refinement preserves dependencies, while implicit neural representation predicts levels in parallel.
- **Mechanism:** SMAM is tested with MLM, INR, and no-MLM decoding in a zero-shot speaker-conditioned setup; CER, similarity, quality, real-time factor, latency, and listening scores separate tradeoffs.
- **Mathematical idea:** MLM reports 26M parameters, CER 2.73, RTF 0.701, latency 0.065 s, MOS 4.02, and SMOS 3.36; INR uses 25M parameters and RTF 0.568 with latency 0.061 s.
- **Connections:** This is structured prediction under a time budget: preserving codec dependencies improves quality while parallel prediction improves speed.
- **What paper reports:** The proposed models are smaller and faster than listed non-streaming baselines while remaining competitive; removing MLM degrades quality measures.
- **Limits:** Codec, datasets, hardware, and zero-shot speaker conditions bound the conclusion; other languages and devices are not established.

## 5. people-variation-and-health/human-centered-evaluation

**Paper:** [Can ASR generate valid measures of child reading fluency?](https://www.isca-archive.org/interspeech_2025/harmsen25_interspeech.html)  
**Evidence:** D3; PDF SHA-256 cb6a2a4d5cc531bb69165de6b63c6018a0220f3551e2d1ed6d64fe61ace214fb; 5 pages.

- **Big picture:** Reading fluency assessment should capture accuracy, smoothness, phrasing, and pacing without manually scoring every child.
- **Why hard:** ASR and timing errors can corrupt the educational measure, and agreement with transcript proxies is not the same as instructional validity.
- **Naive attempt:** Use words-correct-per-minute alone or treat an accurate transcript as sufficient evidence that every fluency measure is valid.
- **Central move:** Extract fifteen measures from ASR transcripts and timings, then compare them with the same measures from human transcripts.
- **Mechanism:** The study evaluates 244 recordings from 131 Dutch children aged 6–13, compares four ASR systems, and correlates automatic and human-derived fluency measures.
- **Mathematical idea:** WER, timing F1, and Pearson correlations quantify separate links from audio to educational measure; 12 of 15 measures show strong correlations.
- **Connections:** An automatic metric is useful only if its errors preserve the human construct being measured.
- **What paper reports:** The best reported system has WER 12.3% and timing F1 0.82; twelve measures meet r ≥ 0.7.
- **Limits:** Dutch child reading, fixed texts, age distribution, ASR choice, and transcript comparison limit generalization; intervention or diagnosis validity is not established.

## 6. evaluation-deployment-and-consequence/robustness-and-system-boundary

**Paper:** [PruneSLU: Efficient On-device Spoken Language Understanding through Vocabulary and Structural Pruning](https://www.isca-archive.org/interspeech_2025/do25_interspeech.html)  
**Evidence:** D3; PDF SHA-256 1c859b20b12eb8f022c0ef5d6260f3726017b00d090c741d7be7091cbe4c3f21; 5 pages.

- **Big picture:** Spoken-language understanding must fit on a device with limited memory and power without losing needed intent and slot decisions.
- **Why hard:** Pruning can remove rare but important vocabulary or acoustic layers, while average scores can hide task-specific loss.
- **Naive attempt:** Shrink a model uniformly or remove the smallest weights without asking which tokens and layers support the task.
- **Central move:** Prune task-irrelevant vocabulary first, prune layers structurally, then refine with distillation and contrastive losses.
- **Mechanism:** PruneSLU starts from Whisper-tiny, selects a base vocabulary, chooses layers by loss, and trains with language-model, distillation, and contrastive components on STOP and SLURP.
- **Mathematical idea:** Exact match, EM-Tree, intent accuracy, slot F1, parameter counts, and pruning/loss ablations expose the tradeoff.
- **Connections:** Deployment is constrained optimization: retained representation must preserve task structure, not merely parameter magnitude.
- **What paper reports:** The 15M model retains 98% of original STOP performance, reaches STOP EM 72.31 and SLURP slot F1 71.42, and improves on listed compression baselines.
- **Limits:** STOP/SLURP domains, Whisper initialization, five seeds, and author-reported comparisons bound the result; energy and open-world commands are not tested.

## 7. evaluation-deployment-and-consequence/metrics-and-targets

**Paper:** [AttentiveMOS: A Lightweight Attention-Only Model forSpeech Quality Prediction](https://www.isca-archive.org/interspeech_2025/kibria25_interspeech.html)  
**Evidence:** D3; PDF SHA-256 d1987ba4d40a52b4d88c2833b75a97a9a16e9ccbc06c6642b7827755e9fe33f8; 5 pages.

- **Big picture:** A quality predictor should approximate what listeners hear without requiring a listening test for every utterance.
- **Why hard:** Ratings are noisy, quality depends on local defects and whole-utterance context, and large encoders make prediction impractical.
- **Naive attempt:** Train a large model on MOS labels and treat every listener score as equally reliable.
- **Central move:** Use attention for local and global context in a small model, then sequentially teach it from refined targets to reduce noisy-rating effects.
- **Mechanism:** AttentiveMOS uses Swin and transformer attention with 86K parameters and is evaluated across in-domain, out-of-domain, and cross-domain MOS datasets.
- **Mathematical idea:** MSE measures rating error while Pearson and Spearman measure agreement; SOMOS-clean reports MSE 0.257, PCC 0.449, and SRCC 0.442.
- **Connections:** A metric predictor is itself a deployment model whose compactness and domain shift must be measured alongside correlation.
- **What paper reports:** It beats listed lightweight baselines in the reported SOMOS-clean comparison, but PCC falls to 0.359 on out-of-domain LIVETALK.
- **Limits:** MOS labels, listener composition, dataset domains, and the sharp shift drop limit claims of general quality assessment.

## 8. listening-and-separation/noise-enhancement

**Paper:** [Benchmarking Neural Speech Codec Intelligibility with SITool](https://www.isca-archive.org/interspeech_2025/leschanowsky25_interspeech.html)  
**Evidence:** D3; PDF SHA-256 fb36fc9e25a7c01630b62c6552a8228eb650ee2fe1ed11383f892f930e09d539; 5 pages.

- **Big picture:** A codec can sound pleasant yet make words harder to understand, so intelligibility needs its own evaluation target.
- **Why hard:** Quality scores and WER can miss phoneme-specific distortions and listener-dependent effects, especially for generative codecs.
- **Naive attempt:** Use MOS or WER as a universal proxy for whether listeners identify speech sounds.
- **Central move:** Provide a standardized rhyme-test toolkit and compare its subjective results with objective intelligibility measures.
- **Mechanism:** SITool runs Diagnostic and Modified Rhyme Tests in laboratory or crowdsourcing settings; thirteen codecs are evaluated with phoneme, gender, and wordlist analyses.
- **Mathematical idea:** Subjective scores are compared with STOI, ESTOI, and WER; only STOI and ESTOI significantly correlate in the reported analysis.
- **Connections:** The target determines the metric: intelligibility is not interchangeable with naturalness or transcription accuracy.
- **What paper reports:** Some neural codecs outperform traditional codecs in subjective intelligibility, but objective agreement varies and scores show gender- and wordlist-specific differences.
- **Limits:** The codec set, English tests, listener screening, and objective metrics bound the conclusion; the toolkit does not remove human evaluation.

