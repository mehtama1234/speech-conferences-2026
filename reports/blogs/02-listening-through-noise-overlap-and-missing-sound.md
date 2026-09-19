# Listening through noise, overlap, and missing sound

*Essay 2 of 8 in The Speech Atlas.*

A recording can contain the requested voice, other voices, music, echo, and device noise at the same time. This essay asks how a system can recover useful speech without pretending that missing evidence was cleanly observed.

## Start with the baseline

Fant's speech-chain account places this theme at the following point in communication: Fant pp. 2-4: the technical medium carries the speech wave, and a useful description should preserve task-relevant message information without treating every signal detail as equally necessary.

The ordinary problem is simple to state: A listener often hears several talkers, music, echo, and device noise at once, yet needs one person's words or an intelligible mixture.

One tempting shortcut is: Amplifying everything or subtracting an average noise profile also removes quiet consonants and fails when the interferer changes with the speech. It fails because it hides the distinction this essay needs to keep visible.

The recurring move across this theme is to use structure that differs between target and interference—time, frequency, space, source identity, or learned speech regularity—to estimate and reconstruct the target. The cost is equally important: A cleaner waveform may be less faithful, introduce artifacts, or favor the wrong speaker when the mixture is ambiguous.

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

## Suppressing changing interference

This boundary follows from the baseline account: baseline link: Fant pp. 2-4: the technical medium carries the speech wave, and a useful description should preserve task-relevant message information without treating every signal detail as equally necessary. Ordinary pressure: A listener often hears several talkers, music, echo, and device noise at once, yet needs one person's words or an intelligible mixture. Failed shortcut: Amplifying everything or subtracting an average noise profile also removes quiet consonants and fails when the interferer changes with the speech. Recurring paper move: Use structure that differs between target and interference—time, frequency, space, source identity, or learned speech regularity—to estimate and reconstruct the target. Neighbor test: The target is one speech stream and the failure is removing speech along with noise.

**The question.** What ordinary speech pressure is handled by suppressing changing interference, and what evidence distinguishes it from neighboring pressures?

**The pressure.** A listener often hears several talkers, music, echo, and device noise at once, yet needs one person's words or an intelligible mixture. The subtheme asks: What ordinary speech pressure is handled by suppressing changing interference, and what evidence distinguishes it from neighboring pressures?

**Why the easy answer breaks.** A first attempt would answer the question only with time-frequency masking, but that shortcut misses the boundary: A binary or soft mask can create musical noise and cannot reliably separate sources that occupy the same region.

**The move that recurs.** Across this subtheme, papers make time-frequency masking, speech-prior denoising, changing and adverse noise explicit rather than treating the speech evidence as one undifferentiated variable. The reviewed full-paper mechanisms instantiate that move in different ways; for example: Use a three-stage framework: acoustic structure extraction, coarse full-band noise reduction, and spectral refinement.

### Words used in this section

**Time-frequency masking.** Estimate how much each local frequency region belongs to speech, then attenuate regions dominated by noise.
*Boundary:* A binary or soft mask can create musical noise and cannot reliably separate sources that occupy the same region.

**Speech-prior denoising.** A model learned from clean speech can fill in a plausible speech pattern where the recording is noisy, trading exact fidelity for intelligibility.
*Boundary:* A plausible completion can hallucinate phonetic detail the microphone never captured.

**Changing and adverse noise.** The useful distinction is whether noise changes faster than the system can track, as with competing speech, vehicles, or sudden events.
*Boundary:* A result on fixed background noise does not establish performance under changing or speech-like interference.

### What the evidence shows

- [A Three-Stage Beamforming with Harmonic Guidance for Multi-Channel Speech Enhancement](https://www.isca-archive.org/interspeech_2025/alip25_interspeech.html) (D3): Use a three-stage framework: acoustic structure extraction, coarse full-band noise reduction, and spectral refinement. **Measured or tested:** Experiments on LibriSpeech-based datasets demonstrate that the proposed method significantly outperforms the reference method. **Limit:** The evidence is benchmark-bound and the summary does not establish performance in arbitrary rooms, languages, or devices.
- [Structured Codebook Based Hierarchical Framework for DNN for Computationally Efficient Speech Enhancement](https://www.isca-archive.org/interspeech_2025/b25_interspeech.html) (D3): Replace one expensive DNN with simpler hierarchical predictors backed by structured speech-parameter codebooks. **Measured or tested:** This is achieved by using structured codebooks of speech parameters, like log power spectra, that are generated by exploiting hierarchical relation between the speech training data. **Limit:** One corpus and parameterized spectral targets bound the evidence; downstream ASR and perceptual benefit are not fully established.
- [Test-Time Training for Speech Enhancement](https://www.isca-archive.org/interspeech_2025/behera25_interspeech.html) (D3): Use a Y-shaped enhancement model with self-supervised reconstruction or masked-spectrogram tasks during test-time adaptation. **Measured or tested:** This paper introduces a novel application of Test-Time Training (TTT) for Speech Enhancement, addressing the challenges posed by unpredictable noise conditions and domain shifts. **Limit:** The adaptation steps, compute budget, noise conditions, and author-reported metrics bound the result; listener benefit and long-term stability remain open.
- [QUADS: Quantized Distillation Framework for Efficient Speech Language Understanding](https://www.isca-archive.org/interspeech_2025/biswas25b_interspeech.html) (D3): Train the student with distillation and quantization constraints together through multiple stages. **Measured or tested:** We propose QUADS, a unified framework that optimizes both through multi-stage training with a pre-trained model, enhancing adaptability to low-bit regimes while maintaining accuracy. **Limit:** The result depends on tasks, bit settings, and hardware interpretation of the counts; latency and energy on deployed devices remain open.

**Where this boundary stops.** A binary or soft mask can create musical noise and cannot reliably separate sources that occupy the same region.; A plausible completion can hallucinate phonetic detail the microphone never captured.; A result on fixed background noise does not establish performance under changing or speech-like interference.

**What this evidence does not establish.** The shared story is supported only by the reviewed papers listed here; D2 entries support the problem and stated method, while D3 entries support the reported mechanism and evaluation. It is not a venue-wide prevalence claim.

**Question left open.** What changes when this move is tested outside the speakers, languages, rooms, devices, or benchmark conditions represented by the 18 D3 paper(s)?

## Recovering several hidden sources

This boundary follows from the baseline account: baseline link: Fant pp. 2-4: the technical medium carries the speech wave, and a useful description should preserve task-relevant message information without treating every signal detail as equally necessary. Ordinary pressure: A listener often hears several talkers, music, echo, and device noise at once, yet needs one person's words or an intelligible mixture. Failed shortcut: Amplifying everything or subtracting an average noise profile also removes quiet consonants and fails when the interferer changes with the speech. Recurring paper move: Use structure that differs between target and interference—time, frequency, space, source identity, or learned speech regularity—to estimate and reconstruct the target. Neighbor test: The mixture contains multiple sources and the system must infer source identity or count.

**The question.** What ordinary speech pressure is handled by recovering several hidden sources, and what evidence distinguishes it from neighboring pressures?

**The pressure.** A listener often hears several talkers, music, echo, and device noise at once, yet needs one person's words or an intelligible mixture. The subtheme asks: What ordinary speech pressure is handled by recovering several hidden sources, and what evidence distinguishes it from neighboring pressures?

**Why the easy answer breaks.** A first attempt would answer the question only with blind source separation, but that shortcut misses the boundary: The mixture may not contain enough information to identify sources uniquely; permutation and source-count assumptions matter.

**The move that recurs.** Across this subtheme, papers make blind source separation, target-conditioned separation explicit rather than treating the speech evidence as one undifferentiated variable. The reviewed full-paper mechanisms instantiate that move in different ways; for example: Separate one stream at a time and let a lightweight authorization block decide when recursion should stop.

### Words used in this section

**Blind source separation.** Infer several hidden signals from their mixture using differences in statistics, timing, or spectral structure without receiving isolated sources at test time.
*Boundary:* The mixture may not contain enough information to identify sources uniquely; permutation and source-count assumptions matter.

**Target-conditioned separation.** A voice example, enrollment identity, or visual cue tells the separator which source to preserve rather than asking it to output every source.
*Boundary:* Conditioning can lock onto the wrong talker or encode identity without guaranteeing intelligible content.

### What the evidence shows

- [ReSepNet: A Unified-Light Model for Recursive Speech Separation with Unknown Speaker Count](https://www.isca-archive.org/interspeech_2025/alizadeh25_interspeech.html) (D3): Separate one stream at a time and let a lightweight authorization block decide when recursion should stop. **Measured or tested:** We demonstrate the effectiveness of ReSepNet on the WSJ0 datasets, achieving state-of-the-art separation performance and accurate speaker count estimation. **Limit:** The evidence is synthetic WSJ0 mixtures, 8-kHz four-second windows, and a bounded count range; real rooms and end-to-end recognition are not tested. Results are author-reported.
- [Deep-Simplex Multichannel Speech Separation](https://www.isca-archive.org/interspeech_2025/avidan25_interspeech.html) (D3): Use a deep-simplex formulation that combines multichannel spatial evidence with a representation able to handle recursive or variable separation. **Measured or tested:** While deep-learning-based models often outperform conventional methods, they require large training datasets and struggle to generalize to new settings. **Limit:** Performance depends on microphone geometry, room conditions, source count, and the reference metrics; synthetic mixtures may not represent real overlap. No independent reproduction was performed.
- [Relative cue weighting in multilingual stop voicing production](https://www.isca-archive.org/interspeech_2025/chan25_interspeech.html) (D3): Measure nine acoustic correlates in Malay, English, and Mandarin speech from early multilingual Malaysians and use random forests to compare cue weighting. **Measured or tested:** The analysis uses 7,504 annotated stop tokens from Malaysian speakers across Malay, English, and Mandarin, with four dominance/repertoire groups. Closure voicing, VOT, burst intensity, vowel duration, and onset f0/F1 slopes are normalized by language and speaker and modeled with random-forest… **Limit:** The Malaysian speakers, three languages, stop inventory, nine correlates, and random-forest analysis bound generalization to other multilingual populations or contrasts.
- [NeuroSpex+: Dual-Task Training of Neuro-Guided Speaker Extraction with Speech Envelope and Waveform](https://www.isca-archive.org/interspeech_2025/dasilva25_interspeech.html) (D3): Train jointly to reconstruct both target waveform and target speech envelope, reinforcing the extraction mask. **Measured or tested:** NeuroSpex+ uses 128 KULeuven speech-EEG trials from 16 subjects in subject-independent 16-fold cross-validation, with 4-second windows yielding 39,984 training and 2,856 validation/test segments per fold. Speaker extraction is evaluated with SDRi, SI-SDRi, PESQ, and STOI; envelope reconstruction… **Limit:** EEG alignment, subjects, mixtures, signal metric, and lab conditions bound transfer; signal quality is not a demonstrated BCI communication benefit.

**Where this boundary stops.** The mixture may not contain enough information to identify sources uniquely; permutation and source-count assumptions matter.; Conditioning can lock onto the wrong talker or encode identity without guaranteeing intelligible content.

**What this evidence does not establish.** The shared story is supported only by the reviewed papers listed here; D2 entries support the problem and stated method, while D3 entries support the reported mechanism and evaluation. It is not a venue-wide prevalence claim.

**Question left open.** What changes when this move is tested outside the speakers, languages, rooms, devices, or benchmark conditions represented by the 12 D3 paper(s)?

## Using location to select sound

This boundary follows from the baseline account: baseline link: Fant pp. 2-4: the technical medium carries the speech wave, and a useful description should preserve task-relevant message information without treating every signal detail as equally necessary. Ordinary pressure: A listener often hears several talkers, music, echo, and device noise at once, yet needs one person's words or an intelligible mixture. Failed shortcut: Amplifying everything or subtracting an average noise profile also removes quiet consonants and fails when the interferer changes with the speech. Recurring paper move: Use structure that differs between target and interference—time, frequency, space, source identity, or learned speech regularity—to estimate and reconstruct the target. Neighbor test: Microphone geometry and direction are the evidence; a single-channel separator has a different limit.

**The question.** What ordinary speech pressure is handled by using location to select sound, and what evidence distinguishes it from neighboring pressures?

**The pressure.** A listener often hears several talkers, music, echo, and device noise at once, yet needs one person's words or an intelligible mixture. The subtheme asks: What ordinary speech pressure is handled by using location to select sound, and what evidence distinguishes it from neighboring pressures?

**Why the easy answer breaks.** A first attempt would answer the question only with spatial filtering, but that shortcut misses the boundary: A single microphone or moving speaker removes the spatial cue the method depends on.

**The move that recurs.** Across this subtheme, papers make spatial filtering explicit rather than treating the speech evidence as one undifferentiated variable. The reviewed full-paper mechanisms instantiate that move in different ways; for example: Make target location explicit in a location-aware target-speaker extraction model.

### Words used in this section

**Spatial filtering.** Several microphones provide direction-dependent differences, allowing a filter to reinforce one location and reject others.
*Boundary:* A single microphone or moving speaker removes the spatial cue the method depends on.

### What the evidence shows

- [Location-Aware Target Speaker Extraction for Hearing Aids](https://www.isca-archive.org/interspeech_2025/alcalapadilla25_interspeech.html) (D3): Make target location explicit in a location-aware target-speaker extraction model. **Measured or tested:** The evaluation using objective measures demonstrates that our extended model outperforms the baseline system with our novel encoding method achieving superior performance in 16 out of 21 cases. **Limit:** Array geometry, motion, layout, processing, and intelligibility metric bound transfer.
- [A Study of Real-world Audio-Visual Corpus Design and Production: A Perspective from MISP Challenges](https://www.isca-archive.org/interspeech_2025/chen25k_interspeech.html) (D3): Design the corpus around deployment scenarios, synchronized equipment, annotation and alignment procedures, and explicit task requirements, then inspect how those choices shape downstream results. **Measured or tested:** In this context, the MISP challenges were organized at ICASSP 2022, 2023, and 2024, respectively. **Limit:** Challenge construction, participant selection, language, room/device coverage, and annotation policy bound generalization; downloading or winning on a corpus does not prove deployment realism.
- [SoundSculpt: Direction and Semantics Driven Ambisonic Target Sound Extraction](https://www.isca-archive.org/interspeech_2025/chen25l_interspeech.html) (D3): Condition an ambisonic-in/ambisonic-out extractor jointly on target direction and semantic embeddings, and test whether the cues complement one another. **Measured or tested:** Trained and evaluated on synthetic and real ambisonic mixtures, SoundSculpt demonstrates superior performance compared to various signal processing baselines. **Limit:** Synthetic scene construction, ambisonic order, semantic detector quality, room conditions, and target definition bound transfer; benchmark improvement is not guaranteed perceptual source isolation in arbitrary rooms.
- [Spatio-Spectral Diarization of Meetings by Combining TDOA-based Segmentation and Speaker Embedding-based Clustering](https://www.isca-archive.org/interspeech_2025/cordlandwehr25_interspeech.html) (D3): Segment with time-difference-of-arrival cues, cluster speaker embeddings, and combine spatial and spectral evidence. **Measured or tested:** The spatio-spectral diarization pipeline is evaluated on 10-minute LibriCSS eight-speaker meetings with 0–40% overlap and LibriW ASN re-recordings in two rooms with T60 values of 200/800 ms. Four microphones are used for diarization and DER is reported without a forgiveness collar; downstream… **Limit:** Layouts, datasets, overlap, and spatial cues bound the result; evaluations are author-reported.

**Where this boundary stops.** A single microphone or moving speaker removes the spatial cue the method depends on.

**What this evidence does not establish.** The shared story is supported only by the reviewed papers listed here; D2 entries support the problem and stated method, while D3 entries support the reported mechanism and evaluation. It is not a venue-wide prevalence claim.

**Question left open.** What changes when this move is tested outside the speakers, languages, rooms, devices, or benchmark conditions represented by the 6 D3 paper(s)?

## Canceling copies and filling gaps

This boundary follows from the baseline account: baseline link: Fant pp. 2-4: the technical medium carries the speech wave, and a useful description should preserve task-relevant message information without treating every signal detail as equally necessary. Ordinary pressure: A listener often hears several talkers, music, echo, and device noise at once, yet needs one person's words or an intelligible mixture. Failed shortcut: Amplifying everything or subtracting an average noise profile also removes quiet consonants and fails when the interferer changes with the speech. Recurring paper move: Use structure that differs between target and interference—time, frequency, space, source identity, or learned speech regularity—to estimate and reconstruct the target. Neighbor test: The unwanted signal is a known delayed copy or missing frame, not an arbitrary background.

**The question.** What ordinary speech pressure is handled by canceling copies and filling gaps, and what evidence distinguishes it from neighboring pressures?

**The pressure.** A listener often hears several talkers, music, echo, and device noise at once, yet needs one person's words or an intelligible mixture. The subtheme asks: What ordinary speech pressure is handled by canceling copies and filling gaps, and what evidence distinguishes it from neighboring pressures?

**Why the easy answer breaks.** A first attempt would answer the question only with acoustic echo cancellation, but that shortcut misses the boundary: The loudspeaker path changes with movement and delay; an imperfect estimate can cancel near-end speech.

**The move that recurs.** Across this subtheme, papers make acoustic echo cancellation, packet-loss concealment explicit rather than treating the speech evidence as one undifferentiated variable. The reviewed full-paper mechanisms instantiate that move in different ways; for example: Use Neural Principal Probability Components to represent the posterior over possible inpaintings and compare it with dropout sampling.

### Words used in this section

**Acoustic echo cancellation.** Use the known far-end playback signal to predict the speaker signal that returns through the room, then subtract that predicted copy.
*Boundary:* The loudspeaker path changes with movement and delay; an imperfect estimate can cancel near-end speech.

**Packet-loss concealment.** When transmitted audio frames disappear, infer a short continuation from nearby waveform or speech structure so playback does not break.
*Boundary:* Short plausible continuation is not recovery of the original utterance and becomes unsafe over long gaps.

### What the evidence shows

- [Discovering Directions of Uncertainty in Speech Inpainting](https://www.isca-archive.org/interspeech_2025/cohen25_interspeech.html) (D3): Use Neural Principal Probability Components to represent the posterior over possible inpaintings and compare it with dropout sampling. **Measured or tested:** Our empirical results demonstrate that these directions capture diverse and meaningful variations in both speech content and style, while more precisely capturing the predictive error compared to a more costly Bayesian deep learning approach. **Limit:** The data, posterior approximation, audio examples, and benchmark define the result; calibration and user decision rules remain unresolved.
- [Extended Loss: Incorporating Long Context into Training Models when using Short Audio Frames](https://www.isca-archive.org/interspeech_2025/dinh25_interspeech.html) (D3): Keep long-context information in each training batch while producing short-frame outputs, so the model learns continuity without increasing application delay. **Measured or tested:** Most existing works focus on architecture design and ignore practical issues such as the effect of frame length on the performance of end-to-end AEC models. **Limit:** Echo paths, frame size, batch context, hardware, and evaluation signals bound the claim; continuity on the benchmark is not proof of every room or device.
- [Rollback Speech: Smart Feedback Prompts for Lost Utterances in Unstable Online Calls](https://www.isca-archive.org/interspeech_2025/quinterovillalobos25_interspeech.html) (D3): Compare local and remote ASR streams, identify unreceived content after reconnection, extract keywords from the missing segment, and prompt the speaker to repeat only the relevant information. **Measured or tested:** When connection issues cause parts of a speaker’s audio to be lost, the system uses dual automatic speech recognition (ASR) outputs—one local and one remote—to detect which utterances were not received. **Limit:** Two-person demonstration conditions, simulated network failure, ASR errors, keyword quality, privacy/latency trade-offs, and absence of a listening study bound the result.
- [TS-URGENet: A Three-stage Universal Robust and Generalizable Speech Enhancement Network](https://www.isca-archive.org/interspeech_2025/rong25_interspeech.html) (D3): Use a three-stage pipeline: filling, separation, and restoration. **Measured or tested:** TS-URGENet is evaluated on an official validation set and an official blind test set using DNSMOS, NISQA, UTMOS, PESQ/POLQA, ESTOI, SDR, MCD, LSD, SpeechBERTScore, phonetic similarity, speaker similarity, content accuracy, and MOS. Ablations add metric-aware fine-tuning terms and joint-stage… **Limit:** Challenge conditions, author-reported ranking, and no independent run limit the claim.

**Where this boundary stops.** The loudspeaker path changes with movement and delay; an imperfect estimate can cancel near-end speech.; Short plausible continuation is not recovery of the original utterance and becomes unsafe over long gaps.

**What this evidence does not establish.** The shared story is supported only by the reviewed papers listed here; D2 entries support the problem and stated method, while D3 entries support the reported mechanism and evaluation. It is not a venue-wide prevalence claim.

**Question left open.** What changes when this move is tested outside the speakers, languages, rooms, devices, or benchmark conditions represented by the 5 D3 paper(s)?

## Optimizing what a listener can use

This boundary follows from the baseline account: baseline link: Fant pp. 2-4: the technical medium carries the speech wave, and a useful description should preserve task-relevant message information without treating every signal detail as equally necessary. Ordinary pressure: A listener often hears several talkers, music, echo, and device noise at once, yet needs one person's words or an intelligible mixture. Failed shortcut: Amplifying everything or subtracting an average noise profile also removes quiet consonants and fails when the interferer changes with the speech. Recurring paper move: Use structure that differs between target and interference—time, frequency, space, source identity, or learned speech regularity—to estimate and reconstruct the target. Neighbor test: This boundary is for methods whose target is what a listener can understand or tolerate; it is separate from noise removal, separation, and packet repair, which target a signal or source before the listener judges it.

**The question.** What ordinary speech pressure is handled by optimizing what a listener can use, and what evidence distinguishes it from neighboring pressures?

**The pressure.** A listener often hears several talkers, music, echo, and device noise at once, yet needs one person's words or an intelligible mixture. The subtheme asks: What ordinary speech pressure is handled by optimizing what a listener can use, and what evidence distinguishes it from neighboring pressures?

**Why the easy answer breaks.** A first attempt would answer the question only with perceptual enhancement, but that shortcut misses the boundary: A perceptual score can hide distortions important for recognition, speaker identity, or forensic use.

**The move that recurs.** Across this subtheme, papers make perceptual enhancement explicit rather than treating the speech evidence as one undifferentiated variable. The reviewed full-paper mechanisms instantiate that move in different ways; for example: Separate linguistic/prosodic prediction from neural phase reconstruction, then use a neural vocoder and a learned MOSA evaluator.

### Words used in this section

**Perceptual enhancement.** Optimize what a listener can understand or tolerate rather than preserving every sample, using intelligibility or quality as the target.
*Boundary:* A perceptual score can hide distortions important for recognition, speaker identity, or forensic use.

### What the evidence shows

- [MiSTR: Multi-Modal iEEG-to-Speech Synthesis with Transformer-Based Prosody Prediction and Neural Phase Reconstruction](https://www.isca-archive.org/interspeech_2025/alradhi25_interspeech.html) (D3): Separate linguistic/prosodic prediction from neural phase reconstruction, then use a neural vocoder and a learned MOSA evaluator. **Measured or tested:** Evaluated on a public iEEG dataset, MiSTR achieves state-of-the-art speech intelligibility, with a mean Pearson correlation of 0.91 between reconstructed and original Mel spectrograms, improving over existing neural speech synthesis baselines. **Limit:** Dataset, subjects, protocol, learned evaluator, and paper-reported comparisons limit clinical claims.
- [Voice-ENHANCE: Speech Restoration using a Diffusion-based Voice Conversion Framework](https://www.isca-archive.org/interspeech_2025/byun25_interspeech.html) (D3): Stage a speaker-agnostic generative restoration model first, then use a clean target-speaker embedding to refine the restored speech through a voice-conversion-style diffusion decoder. **Measured or tested:** By employing this two-stage approach, we have achieved speech quality objective metric scores comparable to state-of-the-art (SOTA) methods across multiple datasets. **Limit:** Training uses a proprietary restoration corpus and evaluation uses small/simulated validation settings; non-intrusive quality proxies do not establish word correctness or speaker-faithful repair. No independent reproduction was performed.
- [A Deformable Convolution GAN Approach for Speech Dereverberation in Cochlear Implant Users](https://www.isca-archive.org/interspeech_2025/chiang25_interspeech.html) (D3): Let deformable convolution move its receptive field to the distortion, and evaluate both signal measures and listeners with cochlear implants. **Measured or tested:** We first evaluate the effectiveness of the proposed method on REVERB challenge dataset. **Limit:** The claim is bounded to REVERB conditions, the tested listeners, and the GAN configuration; broader hearing profiles, rooms, and independent replication remain open.
- [Modality-Agnostic Multimodal Emotion Recognition using a Contrastive Masked Autoencoder](https://www.isca-archive.org/interspeech_2025/chochlakis25_interspeech.html) (D3): Align modalities contrastively and use masked reconstruction in one modality-agnostic model, then test unimodal, multimodal, and missing-modality cases. **Measured or tested:** Experimental results on the MSP-Podcast corpus show that our unified model achieves state-of-the-art performance, and improves both unimodal and multimodal baselines by 1-5% relative in respective evaluation metrics with the capability to handle missing modalities for two emotion recognition tasks… **Limit:** Corpus, emotion labels, missingness pattern, modality quality, and reconstruction objective bound the claim; emotion inference is not guaranteed to be socially reliable.

**Where this boundary stops.** A perceptual score can hide distortions important for recognition, speaker identity, or forensic use.

**What this evidence does not establish.** The shared story is supported only by the reviewed papers listed here; D2 entries support the problem and stated method, while D3 entries support the reported mechanism and evaluation. It is not a venue-wide prevalence claim.

**Question left open.** What changes when this move is tested outside the speakers, languages, rooms, devices, or benchmark conditions represented by the 15 D3 paper(s)?

## Closing note

This essay is a map of recurring problems and research moves, not a leaderboard or a claim that these categories cover every speech study. The paper links and depth labels show what was actually checked; they do not turn reported results into independent facts.
