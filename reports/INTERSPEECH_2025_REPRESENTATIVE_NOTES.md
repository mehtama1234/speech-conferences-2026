# INTERSPEECH 2025 representative full-paper notes

These eight notes are the first D3 pass: one representative paper per initial conceptual theme. They are based on the official ISCA PDFs captured in `data/interspeech-2025-representative-papers.json`; they summarize paper evidence and do not independently reproduce experiments.

## 1. signal_and_acoustics

**Paper:** [Reconstruction of the Complete Vocal Tract Contour Through Acoustic to Articulatory Inversion Using Real-Time MRI Data](https://www.isca-archive.org/interspeech_2025/azzouz25_interspeech.html)  
**Evidence:** D3 full-text capture; PDF SHA-256 `a96e9463c75424f8f86fcd9e2fa2b202474fe14000aadc19d11ac7a939a16571`; 5 pages.

- **Big picture:** Infer the shape of the whole vocal tract from the sound a speaker produces.
- **Why it is hard:** Speech acoustics are an indirect result of many moving articulators; EMA sees only selected points while MRI is broader but lower-resolution and temporally blurred.
- **Naive attempt:** Predict each contour point without accounting for articulator compensation or target-tracking error.
- **Central move:** Train bidirectional LSTM models on denoised speech and real-time MRI contours, either articulator-by-articulator or all together.
- **Mechanism:** The acoustic sequence is mapped to contour coordinates; phonetic segmentation is tested as an auxiliary signal and RMSE/median geometric error measure reconstruction.
- **Mathematical idea:** RMSE is average squared contour distance in millimetres; temporal sequence models use surrounding speech context.
- **Connections:** Connects physical speech production to recognition and future articulatory simulation.
- **What the paper reports:** The paper reports 1.65 mm ABA and 1.69 mm AAT mean RMSE, compared with a 1.62 mm MRI pixel size.
- **Limits:** The data are 2D MRI with 1.62 mm pixels and 8 mm slice thickness; acquisition and contour tracking introduce error. No independent reproduction was performed.

## 2. recognition_and_transcription

**Paper:** [Bridging ASR and LLMs for Dysarthric Speech Recognition: Benchmarking Self-Supervised and Generative Approaches](https://www.isca-archive.org/interspeech_2025/aboeitta25_interspeech.html)  
**Evidence:** D3 full-text capture; PDF SHA-256 `e39b8c1a94256ca369c6800d405f322258d34df86c51870aaa1b324d273832fd`; 5 pages.

- **Big picture:** Make transcription usable for dysarthric speech whose motor impairments distort phonemes, timing, and clarity.
- **Why it is hard:** Ordinary-speech recognizers fail when acoustic evidence is variable; CTC can misalign distorted phonemes and end-to-end systems can produce incoherent text.
- **Naive attempt:** Improve only the acoustic encoder and leave decoding without stronger linguistic constraints.
- **Central move:** Benchmark Wav2Vec, HuBERT, and Whisper with CTC/sequence decoding and add BART, GPT-2, or Vicuna as language-aware decoders.
- **Mechanism:** Acoustic representations produce candidates and an LLM uses context to select or repair sequences; WER is compared across TORGO and UASpeech.
- **Mathematical idea:** WER counts substitutions, deletions, and insertions; the key tradeoff is acoustic fidelity versus linguistic plausibility.
- **Connections:** Bridges speech perception, language modeling, and accessibility rather than treating ASR as a generic benchmark.
- **What the paper reports:** The paper reports better Whisper results than CTC baselines and lower WER for LLM-assisted decoding in its experiments.
- **Limits:** Cross-dataset generalization is poor, dysarthric data are limited, and not all encoder-decoder combinations were evaluated.

## 3. understanding_and_translation

**Paper:** [Investigating the Reasoning Abilities of Large Language Models for Understanding Spoken Language in Interpersonal Interactions](https://www.isca-archive.org/interspeech_2025/aggarwal25_interspeech.html)  
**Evidence:** D3 full-text capture; PDF SHA-256 `379dfe0c14c98a674362c1e38020aa556e52d6d32de7d5d20849c15ad992a6e2`; 5 pages.

- **Big picture:** Classify whether a job-interview answer is under-explained, succinct, comprehensive, or over-explained.
- **Why it is hard:** Spoken interaction requires judging an utterance relative to the question, prior context, and social task.
- **Naive attempt:** Use zero-shot prompting without examples, domain knowledge, or conversational context.
- **Central move:** Compare few-shot examples, domain knowledge, and prior context across Gemini-1.5-pro, GPT-3.5-turbo, and GPT-4o.
- **Mechanism:** Prompt factors condition a four-class decision; macro-F1 compares performance across classes.
- **Mathematical idea:** Macro-F1 averages per-class F1; context changes the evidence available for interpreting the same utterance.
- **Connections:** Treats spoken-language understanding as social interpretation, not merely transcription or intent labels.
- **What the paper reports:** The paper reports selected macro-F1 results near 0.50 and 0.55 for its two tasks, with context and combined prompt factors sometimes helping.
- **Limits:** The dataset focuses on military veterans and interview contexts; generalization across occupations, cultures, languages, and interaction styles is unresolved.

## 4. generation_and_voice

**Paper:** [Towards Better Disentanglement in Non-Autoregressive Zero-Shot Expressive Voice Conversion](https://www.isca-archive.org/interspeech_2025/akti25_interspeech.html)  
**Evidence:** D3 full-text capture; PDF SHA-256 `cf4c5704c02d2541d908600a64375a1a4ae0482b3f2ad27a1944fa462408a9bf`; 5 pages.

- **Big picture:** Transfer a target speaker's voice and expression while preserving source linguistic content and reducing source-style leakage.
- **Why it is hard:** Speaker identity, words, emotion, pitch, and energy are mixed in speech, and parallel expressive data are scarce.
- **Naive attempt:** Use one style embedding, which can carry source timbre or content into the converted speech.
- **Central move:** Combine multilingual discrete mHuBERT units, a conditional VAE, perturbation similarity loss, Mix-LN, pitch/energy features, and local-F0 cross-attention.
- **Mechanism:** Content units encode linguistic material, style encoders represent speaker/emotion, and cross-attention injects local pitch into generated regions.
- **Mathematical idea:** Disentanglement allocates content and style to separable representations; cross-attention makes local target-pitch evidence influential where needed.
- **Connections:** Connects generation to identity, expression, agency, and voice-conversion safety.
- **What the paper reports:** The paper reports improved emotion and speaker similarity and reduced source-style leakage versus its baselines.
- **Limits:** The authors identify remaining intelligibility and cross-lingual challenges; this atlas did not run the model or inspect its demo independently.

## 5. separation_and_enhancement

**Paper:** [Location-Aware Target Speaker Extraction for Hearing Aids](https://www.isca-archive.org/interspeech_2025/alcalapadilla25_interspeech.html)  
**Evidence:** D3 full-text capture; PDF SHA-256 `cd6aca2134a1fb17edf1017a420dfbb684a15c5cb9f1d9c3a13550e173159757`; 5 pages.

- **Big picture:** Help a listener follow one person amid competing speakers, noise, and reverberation.
- **Why it is hard:** Microphones record mixtures and hearing aids impose strict latency and model-size limits; the target may move away from a fixed direction.
- **Naive attempt:** Use a fixed-direction separator or a one-hot direction code that cannot flexibly steer a small device.
- **Central move:** Extend GCBFSnet with target direction of arrival, comparing one-hot and complex-exponential encodings and integration methods.
- **Mechanism:** Binaural time-frequency features are conditioned on direction so learned filtering emphasizes the target; SI-SDR and intelligibility measures are evaluated.
- **Mathematical idea:** Complex exponentials encode direction through phase relationships; SI-SDR, HASPI, and MBSTOI represent signal and intelligibility outcomes.
- **Connections:** Combines source separation, spatial acoustics, assistive technology, and on-device deployment.
- **What the paper reports:** The paper reports about +9.93 dB SI-SDR and +0.208 absolute HASPI for FILM-exp in its stated 1,000-utterance setup.
- **Limits:** The evaluation is scenario-specific; future work includes direction estimation and scenes with more than two speakers. Objective scores are not clinical outcomes.

## 6. speaker_and_paralinguistics

**Paper:** [VoxAging: Continuously Tracking Speaker Aging with a Large-Scale Longitudinal Dataset in English and Mandarin](https://www.isca-archive.org/interspeech_2025/ai25_interspeech.html)  
**Evidence:** D3 full-text capture; PDF SHA-256 `64a58c303df73ff039e35c79f78c5ea6160867b8e699b13989b8aed0791575e5`; 5 pages.

- **Big picture:** Measure how a voice changes over years and how that changes speaker-verification decisions.
- **Why it is hard:** Voice identity is not static; aging changes the vocal tract, while longitudinal data are difficult to collect.
- **Naive attempt:** Treat a speaker embedding or stored voiceprint as a permanent identity representation.
- **Central move:** Introduce a longitudinal dataset of 293 speakers, weekly recordings, 7,522 hours, and a longest span of 17 years, then test verification over time.
- **Mechanism:** Repeated observations allow verification scores and equal-error rates to be compared as the time gap grows, with age and gender analyses.
- **Mathematical idea:** Equal-error rate is where false-accept and false-reject rates meet; longitudinal evaluation makes identity time-dependent.
- **Connections:** Connects representation learning to biometrics, dataset design, privacy, and the meaning of same speaker across a lifetime.
- **What the paper reports:** The paper reports declining verification performance and speaker similarity with increasing time span, with differences across age and gender groups.
- **Limits:** The demographic and language composition is not universal; collection, labeling, and model execution were not independently audited here.

## 7. languages_and_people

**Paper:** [Is it all about race? A Cross-examination of /s/ in a Multilingual Nigerian Context](https://www.isca-archive.org/interspeech_2025/amoniyan25_interspeech.html)  
**Evidence:** D3 full-text capture; PDF SHA-256 `e61598574d5c543e85b0d130cdac979f57085845ed7f2666d2147aab65535306`; 5 pages.

- **Big picture:** Identify which social and linguistic factors shape /s/ pronunciation in Nigerian English.
- **Why it is hard:** Acoustic realization depends on neighboring segments, language ecology, age, ethnicity, and social context; imported categories can mislead.
- **Naive attempt:** Explain /s/ variation mainly through gender or race based on studies from other linguistic settings.
- **Central move:** Analyze 4,056 /s/ tokens from ICE-NigE using center of gravity, zero crossings, duration, and skewness across ethnicity, age, gender, and phonological context.
- **Mechanism:** Acoustic measurements operationalize frontness/backness and duration; statistical comparisons associate variation with linguistic and sociolinguistic factors.
- **Mathematical idea:** Spectral center of gravity, zero crossings, and skewness summarize signal distribution as proxies for articulation and social patterning.
- **Connections:** Shows why accents and social variation should be modeled as meaningful local structure rather than generic nuisance variation.
- **What the paper reports:** The paper reports age and ethnicity effects among Igbo, Yoruba, and Hausa Nigerian English speakers, with limited gender differences in this analysis.
- **Limits:** The result concerns this corpus and phoneme; acoustic measures should not be treated as direct proof of identity categories.

## 8. evaluation_and_deployment

**Paper:** [Enabling the replicability of speech synthesis perceptual evaluations](https://www.isca-archive.org/interspeech_2025/lemaguer25_interspeech.html)  
**Evidence:** D3 full-text capture; PDF SHA-256 `9fdd05d1afa7c4b2130d4c985f98ef144c586642094bab6342a45db5b835a068`; 5 pages.

- **Big picture:** Make subjective speech-synthesis evaluations sufficiently specified for meaningful repetition and comparison.
- **Why it is hard:** Listener ratings depend on questions, framing, participants, stimuli, and protocol, while headline MOS-style scores hide those choices.
- **Naive attempt:** Report a perceptual score without the question asked or the evaluation recipe.
- **Central move:** Propose a standardized report, shareable evaluation recipe, open-source platform, and reporting guidelines.
- **Mechanism:** Separate the readable report from supplementary procedural data; distinguish reproducibility with the same inputs from replicability across new participants and data.
- **Mathematical idea:** A subjective score is an observation produced by a protocol, not a property of a waveform independent of listeners; omitted protocol variables become unmeasured variance.
- **Connections:** Provides a methodological backbone for judging speech claims throughout the atlas.
- **What the paper reports:** The contribution is a proposed platform and reporting structure intended to make evaluation choices inspectable.
- **Limits:** Human subjective evaluations cannot simply be rerun with identical participants; adoption and future standards remain open, and the platform was not executed here.

## Cross-paper observation

These papers show a speech-specific pattern: the central object is rarely just the model. It is a relationship between a signal and a human or physical condition—articulation, impairment, direction, aging, identity, social context, or listener judgment. The notes support this interpretation at D3 depth for this small review set; they do not establish venue-wide prevalence.
