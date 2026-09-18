# INTERSPEECH 2025 fifth-pass full-paper notes

This batch targets the seven taxonomy subthemes that previously had no D3 paper: time-frequency measurement, room/channel sensing, echo/reconstruction, prosody/intent, TTS content, clinical/assistive speech, and human-centered evaluation. Notes are based on captured official PDFs and remain paper-reported, not independently reproduced.

## 1. sound-and-production/time-frequency-measurement

**Paper:** [Universal Speech Enhancement with Regression and Generative Mamba](https://www.isca-archive.org/interspeech_2025/chao25b_interspeech.html)  
**Evidence:** D3; PDF SHA-256 `a31e1221b40d1ecf873e80b9e20282bf693d58c58b6900f6020aa824a9fb8657`; 5 pages.

- **Big picture:** Enhancement must handle speech that is noisy, reverberant, clipped, bandwidth-limited, packet-damaged, or recorded at another sampling rate without flattening the changing sound structure.
- **Why hard:** A model trained on one distortion and one sampling rate can fail when the missing evidence must be invented rather than merely attenuated; long recordings also make full attention expensive.
- **Naive attempt:** Use one masking network that scales down whatever is present, or train separate systems for each distortion and sampling rate.
- **Central move:** Use a linear-time state-space model that represents time and frequency together, maps rather than only masks the spectrum, and switches to flow-based generation when content is missing.
- **Mechanism:** USEMamba applies time/frequency Mamba blocks to compressed STFT features, uses sampling-frequency-independent windows, and combines time, multi-resolution STFT, and phase losses. A flow variant samples missing spectrogram content; a simple energy rule selects the generative output for bandwidth-extension and packet-loss regions.
- **Mathematical idea:** The regression model minimizes a weighted L1 waveform loss, multi-resolution STFT loss, and phase loss. The flow model learns a conditional velocity field from noise to clean STFT coefficients and integrates it with an Euler solver; evaluation includes PESQ, ESTOI, SDR, spectral distances, quality estimators, speaker similarity, and word accuracy.
- **Connections:** Shows why time-frequency representation is a conceptual choice, not a preprocessing detail: masking fits attenuation but cannot restore absent content. It connects efficient long-context modeling to generative repair and evaluation tradeoffs.
- **What paper reports:** On the URGENT 2025 conditions spanning seven distortions, five languages, and several sampling rates, the combined system achieved second place in the blind Track 1 phase; regression worked best for most conditions while generation helped packet loss and bandwidth extension.
- **Limits:** The regression model was trained only on English, the challenge data and distortions define the tested generality, and the flow output sometimes had residual noise or wrong phonemes for long packet losses. Ranking and objective metrics do not establish human usefulness in every language or device; no independent reproduction was performed.

## 2. sound-and-production/room-channel-and-sensing

**Paper:** [AISHELL-5: The First Open-Source In-Car Multi-Channel Multi-Speaker Speech Dataset for Automatic Speech Diarization and Recognition](https://www.isca-archive.org/interspeech_2025/dai25c_interspeech.html)  
**Evidence:** D3; PDF SHA-256 `ca7ca91e0626a58f54e98815830576bfb668532013f38628bc3cff94108b13ae`; 5 pages.

- **Big picture:** In-car microphones hear several speakers through reflections, wind, road noise, music, and air conditioning, so a recognizer needs a dataset that preserves the path from talker to sensor.
- **Why hard:** Clean speech recorded close to the mouth does not reveal far-field channel mixing, changing geometry, or realistic driving noise; simulated mixtures alone miss those correlations.
- **Naive attempt:** Train ASR on clean or artificially mixed speech and treat the vehicle microphone array as a fixed recording channel.
- **Central move:** Release a multi-channel, multi-speaker in-car corpus with near-field references, far-field door microphones, real driving conditions, noise recordings, and a reproducible separation-plus-ASR baseline.
- **Mechanism:** AISHELL-5 records 2–4 Mandarin speakers in a hybrid vehicle across more than 60 scenarios, with four far-field channels and headset reference microphones. The baseline uses acoustic echo cancellation, independent vector analysis or SpatialNet separation, VAD segmentation, and ASR; the paper reports separate evaluation sets for oracle and predicted segmentation.
- **Mathematical idea:** The far-field mixture is modeled as y(t)=As(t)+n(t); IVA seeks a demixing that makes sources statistically independent. Evaluation uses character error rate for Eval1 and concatenated minimum-permutation CER for Eval2, after front-end processing.
- **Connections:** Makes room, device, and source separation inseparable from recognition. It is a resource contribution whose deeper point is that a benchmark can encode the physical nuisance structure that a model must learn.
- **What paper reports:** The corpus contains over 100 hours of speech from 260 participants plus about 40 hours of environmental noise; the baseline exposes large differences between near/far-field and processed conditions, with the reported ASR/front-end results establishing the challenge difficulty.
- **Limits:** The corpus is Mandarin and vehicle-specific, with its seating, microphones, and scenario design defining the boundary. The baseline does not establish that one separation method is best in all cars, and dataset availability is not independent reproduction of the reported scores.

## 3. listening-and-separation/echo-and-reconstruction

**Paper:** [Voice-ENHANCE: Speech Restoration using a Diffusion-based Voice Conversion Framework](https://www.isca-archive.org/interspeech_2025/byun25_interspeech.html)  
**Evidence:** D3; PDF SHA-256 `4137e2b796cd4a2cde970513fa34019d7933861e9897ce249dd7143c86425c29`; 5 pages.

- **Big picture:** A damaged recording may be noisy, reverberant, clipped, bandwidth-limited, packet-dropped, or codec-distorted; repairing it requires inventing plausible speech where the waveform contains no evidence.
- **Why hard:** A suppressive mask can remove noise but cannot fill missing frequency or time regions, and voice-conversion models can add identity cues while also failing under noise.
- **Naive attempt:** Apply a denoising mask alone, or use voice conversion directly on a noisy waveform and hope its speaker representation remains stable.
- **Central move:** Stage a speaker-agnostic generative restoration model first, then use a clean target-speaker embedding to refine the restored speech through a voice-conversion-style diffusion decoder.
- **Mechanism:** GSR predicts additive corrections to mel features with a ResU-Net and vocoder, covering noise, reverberation, bandwidth extension, clipping, packet loss, and codec artifacts. The second stage extracts HuBERT discrete content and an ECAPA speaker embedding, predicts a coarse spectrogram, and uses a diffusion U-Net conditioned on content and identity to generate the final waveform.
- **Mathematical idea:** GSR uses GAN, feature-matching, and mel losses; the VC stage combines L1 coarse-spectrogram loss with diffusion noise-prediction loss. NISQA, UTMOS, WV-MOS, and DNSMOS estimate non-intrusive quality on VCTK-DEMAND and UNIVERSE validation sets.
- **Connections:** Separates “repair the evidence” from “restore the intended voice.” It connects echo/reconstruction to generation and identity control, while making clear that plausible speech can be wrong speech.
- **What paper reports:** The paper reports that GSR+VC obtains strong objective quality scores across simulated noise, packet loss, bandwidth, reverberation, and codec conditions and compares favorably with the cited restoration systems.
- **Limits:** Training uses a proprietary restoration corpus and evaluation uses small/simulated validation settings; non-intrusive quality proxies do not establish word correctness or speaker-faithful repair. No independent reproduction was performed.

## 4. meaning-and-interaction/prosody-and-intent

**Paper:** [A-SMiLE: Affective Sparse Mixture-of-Experts Adapter with Multi-Task Learning for Spoken Dialogue Models](https://www.isca-archive.org/interspeech_2025/chao25_interspeech.html)  
**Evidence:** D3; PDF SHA-256 `74156ce29c0acada9426beb6e2d31b0f360a4141ed25e8ea705491e0443120bb`; 5 pages.

- **Big picture:** A spoken dialogue response can be linguistically correct yet emotionally wrong if it misses how the user sounds and what affective state the exchange requires.
- **Why hard:** Speech carries valence, arousal, and dominance through fine-grained cues that ordinary text-only dialogue models discard, so a coherent response can still be socially inappropriate.
- **Naive attempt:** Generate dialogue from transcript text alone or add a single emotion label after response generation.
- **Central move:** Attach a sparse affective mixture-of-experts adapter and train emotion prediction jointly with response generation so acoustic affect influences the response decision.
- **Mechanism:** A-SMiLE encodes the input speech, routes it through sparse experts, predicts continuous valence/arousal/dominance values, and conditions response generation on the affective representation. The joint objective combines mean-squared error for emotion prediction with cross-entropy for response generation; evaluation uses DailyTalk and a hard-case emotional set.
- **Mathematical idea:** The model minimizes a weighted sum of emotion MSE and response token cross-entropy. Reported metrics separate VAD prediction from response quality, including automatic response measures and GPT-4o-based evaluation, so no one score is treated as emotion itself.
- **Connections:** Treats prosody as information needed for action, not decoration added to synthesized words. It connects affective speech understanding to dialogue grounding and exposes the gap between automatic response scores and human emotional appropriateness.
- **What paper reports:** The paper reports improvements over text-only and other baselines on VAD prediction and response generation on DailyTalk and its 0.8-hour hard-case emotional benchmark.
- **Limits:** The hard-case data and automatic judge define the tested notion of affective appropriateness; VAD labels simplify lived emotion and GPT-based evaluation is a proxy. The paper does not establish sustained human dialogue benefit or causal understanding of emotion; no independent reproduction was performed.

## 5. voice-generation-and-control/text-to-speech-and-content

**Paper:** [Intelligibility of Text-to-Speech Systems for Mathematical Expressions](https://www.isca-archive.org/interspeech_2025/roychowdhury25_interspeech.html)  
**Evidence:** D3; PDF SHA-256 `702c8f68987fbac3505bf3bc88b0cba5e2895697aea30606404df796f57598df`; 5 pages.

- **Big picture:** A TTS system can pronounce ordinary prose acceptably yet make mathematical notation unintelligible because symbols, structure, and relations must be spoken in an exact order.
- **Why hard:** LaTeX is not directly readable by TTS, and a fluent-sounding output may still change an equation’s meaning; MOS alone cannot tell whether a listener recovered the expression.
- **Naive attempt:** Convert formulas to text with a generic prompt and judge the audio by naturalness or a single speech-quality metric.
- **Central move:** Evaluate the full chain—LLM pronunciation generation, TTS rendering, listener comprehension, expert comparison, and expression category—using both perceptual and transcription-based measures.
- **Mechanism:** The study samples 120 expressions across eight categories, uses Qwen or GPT-4 to create spoken text, synthesizes audio with five TTS models, and asks 49 technically trained listeners to rate and transcribe it. A second test compares 35 expressions with hidden expert renditions.
- **Mathematical idea:** Evaluation includes MOS, exact count-of-correct, LaTeX character error rate, and TeXBLEU; ANOVA tests TTS model, expression category, and LLM effects. The denominator is the selected expression/listener trials, not general language understanding.
- **Connections:** Shows that content preservation is a separate generation constraint from naturalness. It links TTS to human-centered evaluation and demonstrates why a benchmark must measure the intended object—in this case mathematical meaning.
- **What paper reports:** No TTS model is consistently strong across categories; intelligibility varies by expression type and model, and the outputs are generally worse than expert renditions. Pronunciation correctness is reported at 87.5% overall, with category-dependent listener success.
- **Limits:** The expressions, listeners, languages, LLMs, and five TTS systems define the scope; technical listeners and repeated playback may not represent ordinary users. Transcription and MOS remain proxies for mathematical comprehension, and no independent reproduction was performed.

## 6. people-variation-and-health/clinical-and-assistive-speech

**Paper:** [Speech Annotation for A: Accuracy, Access, and Application](https://www.isca-archive.org/interspeech_2025/li25ea_interspeech.html)  
**Evidence:** D3; PDF SHA-256 `d2d2abb318b699f3d948b6f6b6cedca25777b35d100371bbc0a6ecdd0165e8a2`; 2 pages.

- **Big picture:** Clinical speech research needs accurate bilingual, multi-speaker, time-aligned annotations, but clinicians cannot spend unlimited time learning complex tools or correcting opaque automatic transcripts.
- **Why hard:** Full automation can silently change words, speakers, languages, and timestamps; fully manual annotation is slow and difficult to scale, especially in code-switched recordings.
- **Naive attempt:** Choose either an automatic transcript with no review or a powerful annotation suite that leaves all alignment and metadata work to a specialist.
- **Central move:** Keep the model-generated draft but make human correction cheap: edit in synchronized chunks, highlight every difference, tag speaker/language explicitly, and export structured research files.
- **Mechanism:** SAFA combines Whisper and diarization drafts with a PyQt6 interface. Chunk navigation follows playback, original and edited text/tags/timestamps are compared in real time, language and speaker labels are selectable, and CSV/SRT/TXT exports preserve the corrected record.
- **Mathematical idea:** The central object is an auditable annotation state rather than a prediction score: every edit is exposed to a human. The paper’s evidence is a workflow/design demonstration, not a controlled accuracy study with a fixed annotation denominator.
- **Connections:** Makes the human reviewer part of the system mechanism. It connects clinical speech, multilingual resources, evaluation, and access: the useful model is the one that lets domain experts correct its uncertain parts.
- **What paper reports:** The paper presents an end-to-end bilingual clinical annotation workflow intended to reduce setup and manual effort while retaining human validation and structured metadata for downstream research.
- **Limits:** The paper does not report a controlled user study, annotation-time reduction, inter-annotator agreement, or clinical outcome. Whisper/diarization errors and supported language choices remain boundaries; tool availability is not independent execution.

## 7. people-variation-and-health/human-centered-evaluation

**Paper:** [Hear Me Out: Interactive evaluation and bias discovery platform for speech-to-speech conversational AI](https://www.isca-archive.org/interspeech_2025/bokkahallisatish25_interspeech.html)  
**Evidence:** D3; PDF SHA-256 `95321e8befa4ed5ca1458df111c3893bce8485004925d6db46e971855cd16c97`; 2 pages.

- **Big picture:** A conversational speech model may respond differently to the same words when the speaker’s apparent age, gender, accent, or voice is changed, but ordinary benchmarks hide that counterfactual.
- **Why hard:** A response difference can come from speech content, vocal identity, prosody, or model randomness; users need a paired way to change one input factor and inspect what changes downstream.
- **Naive attempt:** Run one benchmark transcript per prompt and summarize average response quality without exposing speaker-dependent behavior.
- **Central move:** Build an interactive platform that converts the same user prompt into alternative voices, shows paired model responses, and combines direct inspection with automated speech, sentiment, quality, pitch, and semantic-consistency measures.
- **Mechanism:** Hear Me Out lets a user choose a speech foundation model, submit an original or voice-converted prompt, view the response pair, and inspect response speech rate, pitch, audio-quality dimensions, sentiment, and semantic similarity. The paired interaction makes possible a counterfactual probe of speaker characteristics.
- **Mathematical idea:** The platform reports syllables per second, mean and standard-deviation F0, model-based sentiment/quality scores, and semantic textual similarity. These are diagnostic projections of behavior, not a single fairness metric or causal estimate.
- **Connections:** Treats evaluation as an experience that can reveal hidden behavior rather than only a leaderboard. It connects human-centered testing to voice conversion, bias discovery, and accountable deployment.
- **What paper reports:** The paper demonstrates an accessible interactive evaluation experience for comparing responses to original and transformed voices and argues that it can expose speaker-dependent differences and possible bias.
- **Limits:** The work is a platform/demo, not a powered user study or population-level fairness audit; its automated metrics and selected voice profiles constrain what can be observed. The authors explicitly call for larger studies and additional bias metrics, and no independent reproduction was performed.
