# Speech first-principles seed synthesis

This is the first family-synthesis layer, grounded in the 456 analyst-reviewed D3 papers. It is not a venue-wide conclusion: themes without a reviewed paper remain explicitly unestablished, and reported results remain author-reported.

## Sound, bodies, rooms, and recording

**Ordinary pressure:** Speech reaches a microphone as changing air pressure after vocal-fold vibration, mouth shape, room reflections, and electronics have already mixed together.

**Naive strategy that breaks:** Treating the waveform as an unstructured list of samples hides which changes came from the talker, the room, or the recording device.

**Recurring move:** Separate source, filter, geometry, and time scale so a measured signal can be related back to a physical cause.

**Boundary:** A useful physical description can be wrong when bodies, rooms, or microphones violate its assumptions.

**D3 evidence status:** 56 reviewed paper(s); the family claim below is limited to these examples.

**Conceptual family represented:** `articulatory-dynamics/articulatory-coordination`, `source-generation/vocal-tract-filter`, `time-frequency-measurement/multi-resolution-signal`, `room-channel-and-sensing/microphone-channel`, `articulatory-dynamics/articulatory-coordination`, `room-channel-and-sensing/reverberant-mixture`, `source-generation/vocal-tract-filter`, `time-frequency-measurement/multi-resolution-signal`, `time-frequency-measurement/multi-resolution-signal`, `source-generation/periodic-source`, `source-generation/periodic-source`, `time-frequency-measurement/multi-resolution-signal`, `room-channel-and-sensing/microphone-channel`, `room-channel-and-sensing/microphone-channel`, `source-generation/vocal-tract-filter`, `time-frequency-measurement/multi-resolution-signal`, `room-channel-and-sensing/microphone-channel`, `room-channel-and-sensing/microphone-channel`, `articulatory-dynamics/articulatory-coordination`, `time-frequency-measurement/windowed-spectrum`, `articulatory-dynamics/articulatory-coordination`, `articulatory-dynamics/articulatory-coordination`, `articulatory-dynamics/articulatory-coordination`, `source-generation/vocal-tract-filter`, `source-generation/vocal-tract-filter`, `room-channel-and-sensing/microphone-channel`, `time-frequency-measurement/sampling-and-quantization`, `room-channel-and-sensing/non-airborne-sensing`, `time-frequency-measurement/sampling-and-quantization`, `time-frequency-measurement/windowed-spectrum`, `room-channel-and-sensing/reverberant-mixture`, `room-channel-and-sensing/microphone-channel`, `time-frequency-measurement/windowed-spectrum`, `time-frequency-measurement/multi-resolution-signal`, `time-frequency-measurement/windowed-spectrum`, `articulatory-dynamics/articulatory-coordination`, `source-generation/vocal-tract-filter`, `articulatory-dynamics/articulatory-coordination`, `articulatory-dynamics/articulatory-coordination`, `articulatory-dynamics/articulatory-coordination`, `articulatory-dynamics/articulatory-coordination`, `source-generation/vocal-tract-filter`, `room-channel-and-sensing/non-airborne-sensing`, `room-channel-and-sensing/non-airborne-sensing`, `room-channel-and-sensing/non-airborne-sensing`, `room-channel-and-sensing/microphone-channel`, `time-frequency-measurement/multi-resolution-signal`, `time-frequency-measurement/multi-resolution-signal`, `time-frequency-measurement/multi-resolution-signal`, `room-channel-and-sensing/non-airborne-sensing`, `time-frequency-measurement/multi-resolution-signal`, `room-channel-and-sensing/microphone-channel`, `room-channel-and-sensing/reverberant-mixture`, `time-frequency-measurement/sampling-and-quantization`, `room-channel-and-sensing/microphone-channel`, `time-frequency-measurement/windowed-spectrum`.

### What the papers make concrete

#### Reconstruction of the Complete Vocal Tract Contour Through Acoustic to Articulatory Inversion Using Real-Time MRI Data

**Why this belongs:** The paper infers coordinated vocal-tract movement from acoustic evidence; it is about the physical source/filter relationship, not ordinary word recognition.

**Mechanism:** The paper reconstructs the complete vocal-tract contour from acoustic input using real-time MRI data and bidirectional recurrent models.

**Mathematical/evaluation object:** The problem is inverse measurement: the model estimates hidden physical configuration from its acoustic consequence, so pixel-scale error and anatomical coverage matter as much as waveform fit.

**Reported evidence:** The paper reports average contour RMSE near the MRI pixel size on its test set.

**Limit:** Speakers, MRI protocol, segmentation, speech styles, and model assumptions limit generalization; contour accuracy is not a complete articulatory theory.

#### Analysis of Avian Biphonic Vocalization Using Computational Modelling

**Why this belongs:** The paper models a dual avian sound source and upper vocal tract to explain how physical geometry produces biphonic spectral structure.

**Mechanism:** A reconstructed syrinx and upper tract are represented in COMSOL; source placement and geometric parameters are changed, then simulated vocalizations are compared with recordings of real birds.

**Mathematical/evaluation object:** Finite-element equations approximate pressure and displacement over small spatial elements; parameter sweeps test how tracheal length, glottal radius, and beak angle move resonances.

**Reported evidence:** The paper reports experimentally validated biphonic simulations and systematic effects of tract geometry on resonance modulation and syllable bandwidth.

**Limit:** The model concerns avian vocalization rather than human speech; micro-CT reconstruction, source assumptions, and validation recordings constrain the result. No independent reproduction was performed.

#### Universal Speech Enhancement with Regression and Generative Mamba

**Why this belongs:** The paper handles changing time-frequency evidence across distortions, using regression where content is present and generation where it is missing.

**Mechanism:** USEMamba applies time/frequency Mamba blocks to compressed STFT features, uses sampling-frequency-independent windows, and combines time, multi-resolution STFT, and phase losses. A flow variant samples missing spectrogram content; a simple energy rule selects the generative output for bandwidth-extension and packet-loss regions.

**Mathematical/evaluation object:** The regression model minimizes a weighted L1 waveform loss, multi-resolution STFT loss, and phase loss. The flow model learns a conditional velocity field from noise to clean STFT coefficients and integrates it with an Euler solver; evaluation includes PESQ, ESTOI, SDR, spectral distances, quality estimators, speaker similarity, and word accuracy.

**Reported evidence:** On the URGENT 2025 conditions spanning seven distortions, five languages, and several sampling rates, the combined system achieved second place in the blind Track 1 phase; regression worked best for most conditions while generation helped packet loss and bandwidth extension.

**Limit:** The regression model was trained only on English, the challenge data and distortions define the tested generality, and the flow output sometimes had residual noise or wrong phonemes for long packet losses. Ranking and objective metrics do not establish human usefulness in every language or device; no independent reproduction was performed.

#### AISHELL-5: The First Open-Source In-Car Multi-Channel Multi-Speaker Speech Dataset for Automatic Speech Diarization and Recognition

**Why this belongs:** The dataset and baseline preserve the room, vehicle, microphone-array, and multi-speaker path that transforms speech before recognition.

**Mechanism:** AISHELL-5 records 2–4 Mandarin speakers in a hybrid vehicle across more than 60 scenarios, with four far-field channels and headset reference microphones. The baseline uses acoustic echo cancellation, independent vector analysis or SpatialNet separation, VAD segmentation, and ASR; the paper reports separate evaluation sets for oracle and predicted segmentation.

**Mathematical/evaluation object:** The far-field mixture is modeled as y(t)=As(t)+n(t); IVA seeks a demixing that makes sources statistically independent. Evaluation uses character error rate for Eval1 and concatenated minimum-permutation CER for Eval2, after front-end processing.

**Reported evidence:** The corpus contains over 100 hours of speech from 260 participants plus about 40 hours of environmental noise; the baseline exposes large differences between near/far-field and processed conditions, with the reported ASR/front-end results establishing the challenge difficulty.

**Limit:** The corpus is Mandarin and vehicle-specific, with its seating, microphones, and scenario design defining the boundary. The baseline does not establish that one separation method is best in all cars, and dataset availability is not independent reproduction of the reported scores.

#### Enhancing Acoustic-to-Articulatory Inversion with Multi-Target Pretraining for Low-Resource Settings

**Why this belongs:** Multi-target pretraining uses linguistic and articulatory labels to make acoustic-to-articulatory inversion useful under scarce paired data and lower inference cost.

**Mechanism:** The model maps acoustic features to articulatory trajectories. During pretraining it predicts phonemic, broad articulatory, and critical-articulator targets; it is then fine-tuned with different amounts of paired data and compared with a baseline and SSL-feature systems on seen and unseen speakers.

**Mathematical/evaluation object:** The main measures are correlation coefficient between predicted and reference trajectories and root-mean-square error. Multi-target pretraining adds supervised prediction tasks; the reported efficiency claim concerns removing the external SSL extractor, not eliminating all computation.

**Reported evidence:** The paper reports consistent AAI improvement, including low-resource gains; the strongest reported unseen-speaker configuration reaches CC 0.8612 and RMSE 1.1023, while inference avoids the external SSL extractor.

**Limit:** The articulatory targets, speakers, language, and feature choices define the tested boundary; predicted movement is not equivalent to direct imaging. Reported gains and speed claims are author-reported and were not independently reproduced.

#### Influence of Room Acoustics on Objective Voice Assessment Methods in the Context of Speech and Language Therapy

**Why this belongs:** Room acoustics alter clinical voice measures, so the paper tests the boundary between speaker quality and recording-path effects.

**Mechanism:** The study simulates room conditions with measured impulse responses and noise, computes the difference between room and dry measures, and fits mixed-effects models with room as a fixed effect, the dry score and its interaction, and subject as a random effect.

**Mathematical/evaluation object:** The central quantity is delta X = X_room - X_dry. The selected models obtain normalized RMSE 0.636 for AVQI and 0.669 for ABI, with R2 0.596 and 0.553; the model is descriptive of the tested rooms, not a universal correction.

**Reported evidence:** Across the rooms, voice-quality measures generally deteriorate by 0–2 units; the smartphone is more affected than the lavalier microphone, and room effects are significant for almost all rooms. Only 8 of 35 rooms meet the stricter A4 reverberation recommendation.

**Limit:** The rooms, simulated signals, microphones, and Saarbrücken database define the tested boundary; the study does not establish a correction for other clinics or devices. Reported model fits and significance tests are author-reported and were not independently reproduced.

#### Vocal-tract model with two directions: Static design for a dummy head and dynamic design for a speaking machine

**Why this belongs:** Physical static and dynamic vocal-tract models expose how geometry and articulation shape sound.

**Mechanism:** The static model fixes one tract configuration and radiates a repeatable vowel; the dynamic model uses blocks and cams to change simulated articulators and tract shape.

**Mathematical/evaluation object:** The relevant object is tract geometry, which determines resonances and radiation; this demonstration has no common benchmark score.

**Reported evidence:** The paper demonstrates both models and argues that static and dynamic versions serve different education, phonetics, pathology, and technology purposes.

**Limit:** This is a two-page demonstration with no shared quantitative evaluation or claim of human-speech equivalence.

#### Extended High-frequency Cues to Phoneme Recognition: Insights from ASR

**Why this belongs:** Extended high-frequency cues are tested as an acoustic factor in phoneme recognition under masking.

**Mechanism:** A neural network decodes phonemes from cochleagrams of broadband, 8-kHz-low-pass, and 6-kHz-low-pass speech under quiet and masked conditions.

**Mathematical/evaluation object:** Recognition accuracy and phoneme-omission probabilities are compared across target-to-masker ratios, filtering conditions, and consonant/vowel classes.

**Reported evidence:** Broadband speech improves phoneme accuracy in masked conditions, especially at lower TMR, while adding no quiet-condition benefit; removing extended high frequencies increases consonant omissions.

**Limit:** VCTK speech, selected maskers, cochleagram assumptions, and a model-based probe bound the conclusion; audiological benefit and general ASR deployment are not established.

#### Frequency-Domain Enhanced Extreme Bandwidth Extension Network with ICCRN for Superior Speech Quality

**Why this belongs:** Frequency-domain bandwidth extension reconstructs missing high-frequency structure under perceptual and signal constraints.

**Mechanism:** The model operates on frequency representations, combines local and global context, and is compared against EBEN and other bandwidth-extension baselines.

**Mathematical/evaluation object:** PESQ, SI-SDR, STOI, and MUSHRA separate signal fidelity, intelligibility, and listener preference.

**Reported evidence:** The tests show gains over the original EBEN, including a 40-person MUSHRA comparison; the authors report clearer high-frequency detail and less distortion.

**Limit:** French LibriSpeech, sampling setup, listeners, and author-reported metrics bound the result; other languages remain open.

#### Study of vocal fold vibration using M-mode ultrasound: a proof of concept

**Why this belongs:** Ultrasound measures vocal-fold vibration as a physical source rather than inferring it only from the recorded waveform.

**Mechanism:** Spatio-temporal maps of the fundamental and second harmonic are compared with median f0 from recordings.

**Mathematical/evaluation object:** A linear fit gives f0-US = 0.997 f0-voice + 0.293 with correlation 0.999; differences are below 2 Hz in 92% of recordings.

**Reported evidence:** The paper reports close agreement and reveals temporal drift; four high-pitched recordings expose aliasing.

**Limit:** The 500-Hz rate, probe placement, healthy participants, and excluded aliased cases limit clinical and high-pitch claims.

#### Hybrid Expert Knowledge and Self-Supervised Learning for Diagnostic Modeling of Adductor Spasmodic and Primary Myotonic Dysphonia

**Why this belongs:** Adductor spasmodic dysphonia changes the physical source of speech; the paper tests whether learned acoustic patterns can expose that change.

**Mechanism:** A CNN receives handcrafted features and self-supervised waveform representations and predicts ADSD versus pMTD on a newly collected patient dataset.

**Mathematical/evaluation object:** The decision is a two-class prediction; accuracy measures the fraction of correctly classified patients.

**Reported evidence:** The paper reports 83.3% classification accuracy.

**Limit:** The result is tied to the constructed dataset, its patient mix, and the two diagnoses; clinical deployment, calibration, and external validation remain open.

#### On Enhancing the Performance of Children's ASR Task in Limited Data Scenario

**Why this belongs:** The abstract ties children's recognition to limited data and acoustic features; this is a measurement/variation problem, not evidence of a new physical production model.

**Mechanism:** The study compares a baseline with augmented data, MFCCs plus glottal parameters, and fMLLR-normalized features.

**Mathematical/evaluation object:** Character error rate is the main error measure; relative reduction compares each system with the baseline.

**Reported evidence:** The combined normalized MFCC and glottal features give a reported 40% relative character-error-rate reduction over baseline.

**Limit:** The evidence is limited to the child's speech data and tested feature pipeline; languages, age ranges, and transfer to new schools or microphones are not established.

#### SepVAC: Multitask Learning of Speaker Separation, Speaker Localization, Microphone Array Localization, and Room Acoustic Parameter Estimation in Various Acoustic Conditions

**Why this belongs:** A microphone array carries location, separation, and room information together, so the system must learn which spatial measurements serve each task.

**Mechanism:** SepVAC jointly estimates separated speech, speaker locations, microphone-array location, and room acoustic parameters on SMS-WSJ-Plus.

**Mathematical/evaluation object:** Word error rate evaluates the usefulness of the separated signal to recognition; the multitask losses constrain both speech and scene estimates.

**Reported evidence:** The paper reports a 0.67-point WER improvement over SpatialNet.

**Limit:** The result is author-reported on SMS-WSJ-Plus and its simulated acoustic conditions; real rooms, imperfect localization, and independent reproduction remain open.

#### Voxplorer: Voice data exploration and projection in an interactive dashboard

**Why this belongs:** An interactive voice-data dashboard exposes how recording conditions and speaker variables shape the projections used to explore speech.

**Mechanism:** Voxplorer exposes precomputed high-dimensional voice data and can extract features from recordings directly for interactive exploration.

**Mathematical/evaluation object:** The object is an exploratory mapping from many acoustic dimensions to a visual projection; it is a research instrument rather than a predictive model.

**Reported evidence:** The paper presents a reusable dashboard intended to broaden voice-analysis exploration; no scientific performance score is claimed.

**Limit:** Usability, projection choices, and feature-tool assumptions determine what researchers see; the dashboard does not establish causal voice categories.

#### Evaluation of a model for sound radiation from the vocal tract wall

**Why this belongs:** The paper evaluates sound radiation from the vocal-tract wall, linking physical tract structure to the acoustic output of an articulatory synthesis model.

**Mechanism:** The simulated radiation from tube sections is compared with six speakers producing /b,d,g/ in vowel contexts, with parameters optimized to real spectra.

**Mathematical/evaluation object:** Frequency-domain root-mean-square error between simulated and natural voicebar spectra measures how well the physical model explains the radiation.

**Reported evidence:** The paper reports 2.26–3.82 dB RMSE from 0–800 Hz and concludes the simple model can reproduce the spectra closely.

**Limit:** The six speakers, selected consonants/vowels, frequency range, and fitted parameters bound the claim; other speech sounds and independent physical validation remain open.

#### Introducing EMOPARKNZ: the Emotional Speech Database from New Zealand English Speakers with Parkinson’s Disease

**Why this belongs:** An emotional speech database from speakers with Parkinson's disease makes changing voice quality measurable across health and affect.

**Mechanism:** EMOPARKNZ contains 1,950 recordings from 13 speakers across five emotions; acoustic measures and a 22-listener perception test are reported.

**Mathematical/evaluation object:** F0, intensity, rate, and five-way listener accuracy connect measurable speech changes to perceived emotion.

**Reported evidence:** The paper reports emotion-dependent acoustic differences and 63% listener classification accuracy.

**Limit:** Thirteen speakers, New Zealand English, Parkinson's disease, and the selected emotions bound the resource; clinical severity and broader populations remain open.

#### AuralNet: Hierarchical Attention-based 3D Binaural Localization of Overlapping Speakers

**Why this belongs:** The system estimates overlapping sound locations from binaural spatial cues; microphone geometry changes the available evidence.

**Mechanism:** AuralNet processes binaural signals with multi-head attention, jointly detects sources and estimates azimuth/elevation, and is tested in noisy-reverberant conditions.

**Mathematical/evaluation object:** Classification chooses a spatial sector while regression refines its coordinates; masking lets the loss ignore nonexistent sources.

**Reported evidence:** The paper reports superiority over recent methods in its noisy-reverberant multi-source experiments.

**Limit:** The room simulation/recordings, binaural setup, sector design, and source overlap define the claim; far-field microphone arrays and speech-specific attribution remain open.

#### On the Language and Gender Biases in PSTN, VoIP and Neural Audio Codecs

**Why this belongs:** The study examines how codecs and channel changes interact with language and gender patterns, making the recording path part of recognition evidence.

**Mechanism:** The study measures speech quality after representative codec paths across more than two million multilingual files.

**Mathematical/evaluation object:** The target is a distribution of quality differences, not one overall mean; grouping by language and gender exposes unequal channel loss.

**Reported evidence:** PSTN codecs show strong gender bias and neural codecs introduce language bias in the reported analysis.

**Limit:** Codec set, languages, gender labels, quality measure, and files define the boundary; causal mechanisms and mitigation in deployed networks remain open.

#### Speech Reduction in French: The Relationship Between Vowel Space and Articulation Dynamics

**Why this belongs:** French vowel reduction links shorter or weaker vowel targets to changing articulation dynamics, so fluent speech cannot be modeled as isolated canonical vowels.

**Mechanism:** French spontaneous speech is measured with pVSA, VDI, articulation rate, and temporally compressed speech zones.

**Mathematical/evaluation object:** Regression separates spatial predictors, temporal predictors, and their interaction rather than treating one acoustic number as the cause.

**Reported evidence:** Smaller vowel space predicts more reduction only when articulation rate is included; rate is the strongest predictor and VDI is not significant.

**Limit:** The French speakers, spontaneous tasks, reduction definition, and acoustic measures bound the result; other languages and conversational settings remain open.

#### Influence of Proficiency and L2 Experience on Dynamic Spectral Cue Utilization in L2 Vowel Perception and Production

**Why this belongs:** L2 listeners and speakers weight changing spectral cues differently; the paper treats the measured spectrum as evidence whose usefulness depends on experience and task.

**Mechanism:** Polish learners produce and perceive English /e-æ/ and /i-I/; dynamic formant movement is measured over vowel duration.

**Mathematical/evaluation object:** Formant trajectories are time-varying objects; accuracy and production consistency test whether the moving cue is learned.

**Reported evidence:** Advanced learners improve, especially for /i-I/; formant movement increases with proficiency, while length of residence is not significant.

**Limit:** The learner group, contrasts, language experience, and measurements bound the result; other L1s and natural interaction need separate evidence.

#### Speaker-specific Patterns of Phonetic Covariation in Korean Word-medial Stops and the Role of Phonological and Morphological Contexts

**Why this belongs:** The official full paper identifies a human spoken-speech object and a bounded research problem that instantiate articulatory-coordination under source-filter-production; this resolves taxonomy membership, not the paper's scientific validity.

**Mechanism:** Seoul Korean word-medial stops are analyzed through speaker-specific distributions and covariation patterns across contexts.

**Mathematical/evaluation object:** The object is a structured distribution, not one canonical pronunciation; correlations and category separation test whether variation is organized.

**Reported evidence:** The paper reports systematic speaker-specific covariation that keeps stop categories distinct despite contextual variability, supporting a phonetic-uniformity account.

**Limit:** The language, stop system, contexts, speaker sample, and chosen phonetic measures bound the result; other languages and interactional settings require separate evidence.

#### Supralaryngeal Kinematics of Implosives in Central Vietnamese: An EMA Study

**Why this belongs:** The official full paper identifies a human spoken-speech object and a bounded research problem that instantiate articulatory-coordination under source-filter-production; this resolves taxonomy membership, not the paper's scientific validity.

**Mechanism:** EMA measures movement amplitude, velocity, and plateau timing during Central Vietnamese bilabial implosives; Taiwanese Southern Min controls the voicing explanation.

**Mathematical/evaluation object:** The signal is a time course of gestures; mixed-effects comparisons separate a property of implosivity from a generic property of voicing.

**Reported evidence:** Implosives show greater peak velocity away from closure, while voiceless plosives have a longer gestural plateau; the voiced-plosive control does not reproduce the rapid movement.

**Limit:** The languages, speakers, consonant inventory, EMA measures, and statistical model bound the result; laryngeal airflow itself was not directly measured.

#### Temporal organization of prenuclear glides in Hefei Mandarin

**Why this belongs:** The official full paper identifies a human spoken-speech object and a bounded research problem that instantiate articulatory-coordination under source-filter-production; this resolves taxonomy membership, not the paper's scientific validity.

**Mechanism:** Hefei Mandarin CjV and CwV syllables are analyzed acoustically, comparing glide timing with competing onset and rime accounts.

**Mathematical/evaluation object:** The acoustic trajectory is evidence about an abstract structure; temporal coordination links measurable events to a phonological hypothesis without treating labels as observations.

**Reported evidence:** The paper finds that both glides are more likely part of the rime, agreeing with prior evidence for [j] but differing from earlier results for [w].

**Limit:** The dialect, speakers, acoustic method, and competing analyses bound the inference; timing alone cannot settle every phonological representation or generalize across Mandarin varieties.

#### Influence of wall coverings of 3D-printed vocal tract models on measured transfer functions

**Why this belongs:** Wall materials in a physical vocal-tract model alter measured transfer functions, showing that the modeled filter includes radiation and construction choices.

**Mechanism:** Ten axisymmetric 3D-printed vowel tubes are measured with reciprocity; sound-absorbing fabric and sand embedding are compared as artifact-reduction methods.

**Mathematical/evaluation object:** The transfer function is a physical measurement shaped by both air paths and solid-body vibration; artifact reduction is tested through resonance structure and repeatability.

**Reported evidence:** Both coverings reduce spurious poles and zeros and improve repeatability of the measured transfer functions.

**Limit:** Printed geometries, ten vowels, materials, reciprocity setup, and repeatability metric bound the claim; improved measurement does not prove the replica matches a human tract.

#### Equivalence and differences: Formant patterns of labialization and pharyngealization in Tashlhiyt

**Why this belongs:** Formant patterns of labialization and pharyngealization show how articulator configuration changes resonances and therefore the sound heard by a listener.

**Mechanism:** Thirty-five Tashlhiyt speakers produce VCV logatomes with /i, a, u/ and labialized or pharyngealized consonants; F1 and F2 patterns are compared.

**Mathematical/evaluation object:** The mapping is many-to-one: F2 can reveal a broad acoustic effect while F1 and vowel context retain articulatory distinctions.

**Reported evidence:** Both articulations show similar F2 effects, strongest for /i/ and then /a/, while differences depend on F1 and vowel quality.

**Limit:** The language, speakers, logatomes, adjacent vowels, and formant measures bound the result; formants alone cannot identify every articulatory gesture.

#### L3C-DeepMFC: Low-Latency Low-Complexity Deep Marginal Feedback Cancellation with Closed-Loop Fine Tuning for Hearing Aids

**Why this belongs:** A hearing-aid feedback canceller must use the sensed acoustic path while remaining low-latency and low-complexity.

**Mechanism:** L3C-DeepMFC uses complex spectrum mapping, full- and sub-band recurrent components, and closed-loop fine tuning for marginal feedback cancellation; evaluation varies feedback paths and reports latency, complexity, and speech quality.

**Mathematical/evaluation object:** The complex spectrum keeps magnitude and phase, while a closed loop uses the residual error created by the receiver-microphone path to update cancellation; the system is judged on both suppression and preserved speech.

**Reported evidence:** The paper reports low-latency, low-complexity feedback cancellation with improved speech quality relative to its baselines under tested hearing-aid conditions.

**Limit:** Feedback paths, delay budget, hardware assumptions, noise, and quality metrics bound the result; lab cancellation performance is not the same as clinical benefit for every listener.

#### Neural Spectral Band Generation for Audio Coding

**Why this belongs:** Neural spectral-band generation asks which frequency information can be reconstructed after audio coding removes or compresses it.

**Mechanism:** Neural spectral band generation uses an encoder-decoder to quantize high-frequency side information, reconstructs the band from core audio plus that information, and trains the whole codec with adversarial perceptual criteria.

**Mathematical/evaluation object:** The codec separates what is transmitted from what is generated: the core band carries a base signal while a compact code selects plausible high-frequency detail; rate and perceptual quality expose the tradeoff.

**Reported evidence:** Using AAC as the core codec, the paper reports that n-SBG outperforms conventional SBR at comparable bitrates, especially at low rates, though some codec/rate combinations introduce audible noise.

**Limit:** The core codec, bitrate, adversarial training, signal types, and perceptual metric bound the claim; plausible high-frequency detail is not guaranteed to be the original detail or to improve every downstream speech task.

#### Conformer-based Ultrasound-to-Speech Conversion

**Why this belongs:** Ultrasound-to-speech asks whether articulatory measurements can supply speech information when an ordinary acoustic microphone is unavailable.

**Mechanism:** Two Conformer architectures map ultrasound from four speakers in Ultrasuite-Tal80 to mel spectrograms, then HiFi-GAN produces audio; MSE, mel-cepstral distortion, and a MUSHRA listening test are compared with a 2-D CNN.

**Mathematical/evaluation object:** The input is a time sequence of vocal-tract images and the output is a time sequence of spectral frames; objective distance measures signal similarity, while MUSHRA measures perceived quality, so they test different meanings of 'better.'

**Reported evidence:** The paper reports no statistically significant objective improvement for either Conformer, but better perceptual quality for the bi-LSTM model; the base model matches the CNN while training about three times faster.

**Limit:** Four speakers, speaker-specific training, ultrasound alignment, vocoder quality, and the listening panel bound the result; perceptual improvement is not evidence of speaker-independent silent speech or clinical usefulness.

#### Evaluating Deep Speaker Embedding Robustness to Domain, Sampling Rate, and Codec Variations

**Why this belongs:** The paper tests how sampling rate, codecs, and far-field/noisy channels alter speaker embeddings, making the recording representation the boundary.

**Mechanism:** The study evaluates ECAPA-TDNN, TitaNet, ECAPA2, and ReDimNet on domain, sampling-rate, and codec variations, including far-field speech, noise, and music interference.

**Mathematical/evaluation object:** Verification is a threshold decision on similarity between two embeddings; the experiment changes the recording path while holding the speaker task fixed, revealing which cues are not stable identity evidence.

**Reported evidence:** All models degrade under mismatched domains; ReDimNet degrades least in the tested settings, while downsampling and low-bitrate compression further hurt performance and expose reliance on high-frequency information.

**Limit:** Datasets, codecs, sampling rates, threshold calibration, and attack/evaluation protocol bound the result; robustness to these shifts does not imply fairness or security against adaptive attacks.

#### An interpretable speech foundation model for depression detection by revealing prediction-relevant acoustic features from long speech

**Why this belongs:** The model exposes prediction-relevant acoustic features in long speech so an analyst can connect a health-related decision back to measurable sound properties.

**Mechanism:** The paper uses a speech-level Audio Spectrogram Transformer on long-duration speech and introduces an interpretation method that identifies prediction-relevant acoustic features, comparing it with a segment-level AST.

**Mathematical/evaluation object:** Longer context reduces segment-label noise; attention over the spectrogram is converted into an acoustic explanation, so the model's output is treated as evidence to inspect rather than a diagnosis itself.

**Reported evidence:** The paper reports better depression detection than the segment-level model and identifies reduced loudness and F0 as relevant signals consistent with prior clinical findings.

**Limit:** Dataset, diagnostic labels, recording protocol, attention interpretation, and screening threshold bound the claim; a predictive acoustic correlate is not a clinical cause or validated diagnosis.

#### Direction-Aware Neural Acoustic Fields for Few-Shot Interpolation of Ambisonic Impulse Responses

**Why this belongs:** The title and preserved abstract identify a speech object and bounded intervention that instantiate reverberant-mixture under room-channel-and-sensing; this resolves taxonomy membership only.

**Mechanism:** Direction-Aware Neural Acoustic Fields model ambisonic room impulse responses with a neural field and add explicit directional information, evaluating few-shot interpolation against prior monaural/binaural fields.

**Mathematical/evaluation object:** The neural field is a function from geometry and direction to a time-domain response; the key test is whether a smooth physical variation can be inferred from sparse samples without inventing inconsistent channels.

**Reported evidence:** The paper reports improved few-shot interpolation of directional ambisonic responses over prior neural-field formulations in its room measurements.

**Limit:** Room geometry, microphone/ambisonic order, sampling locations, interpolation range, and waveform metrics bound the claim; interpolation quality does not prove accurate rendering in unseen rooms or perceptual equivalence.

#### Improving Low-Resource Dialect Classification Using Retrieval-based Voice Conversion

**Why this belongs:** Voice conversion is used to vary speakers and dialect conditions, testing whether a classifier learns dialect evidence or the recording and speaker mix.

**Mechanism:** RVC converts low-resource German dialect samples toward a uniform target speaker; experiments compare RVC alone and with frequency masking and segment removal for dialect classification.

**Mathematical/evaluation object:** The augmentation changes speaker identity while attempting to preserve phonetic and dialect information; classifier accuracy tests whether the nuisance factor was reduced rather than merely replaced.

**Reported evidence:** The paper reports improved dialect-classification performance from RVC augmentation, with further gains when combined with frequency masking and segment removal.

**Limit:** Dialect data, target speaker, conversion fidelity, train/test speaker split, and classifier architecture bound the claim; higher accuracy does not prove that all dialect cues survived conversion.

#### Echoes of Phonetics:  Unveiling Relevant Acoustic Cues for ASR via Feature Attribution

**Why this belongs:** Feature attribution for ASR asks which acoustic regions actually support a recognized phonetic decision instead of treating every input feature as equally meaningful.

**Mechanism:** The study analyzes a modern Conformer ASR system, identifying attribution patterns for vowels, sibilant/non-sibilant fricatives, and plosives including release bursts and formants.

**Mathematical/evaluation object:** Attribution maps assign output sensitivity to time-frequency regions; comparison with acoustic structure tests whether the model's evidence aligns with a physical explanation rather than merely correlating with the label.

**Reported evidence:** The paper reports that the model uses full vowel spans and especially the first two formants, captures sibilant spectra more strongly, and emphasizes plosive release/burst cues, with differences by speaker sex.

**Limit:** Attribution method, baseline model, phoneme set, speaker distribution, and interpretation assumptions bound the result; saliency is evidence of sensitivity, not a causal proof that the model listens as a human does.

#### Leveraging AM and FM Rhythm Spectrograms for Dementia Classification and Assessment

**Why this belongs:** AM and FM rhythm spectrograms represent slow and fast changes in speech, testing whether dementia-related information lives in the rhythm structure rather than one static spectrum.

**Mechanism:** The study derives Rhythm Formant Analysis AM/FM spectrograms, tests handcrafted features and a ViT-plus-BERT fusion for dementia classification and regression, and compares against eGeMAPs and Mel spectrograms.

**Mathematical/evaluation object:** The representation changes the time scale of measurement: modulation patterns become visible as structured images, while classification and regression test whether they carry diagnostic information.

**Reported evidence:** The paper reports a 14.2% relative classification-accuracy improvement over eGeMAPs for handcrafted features and further gains when rhythm spectrograms are fused with linguistic and acoustic models.

**Limit:** Corpus, labels, recording length, disease definition, model fusion, and accuracy/regression metrics bound the result; an acoustic association is not a clinical diagnosis or causal mechanism.

#### Adaptive Differential Denoising for Respiratory Sounds Classification

**Why this belongs:** Respiratory-sound classification asks which changing frequency patterns carry evidence of a medical condition.

**Mechanism:** The paper proposes adaptive differential denoising for respiratory-sound classification and compares it with less adaptive processing.

**Mathematical/evaluation object:** Denoising is part of the measurement model: the classifier can only learn a clinical distinction if the preprocessing preserves the relevant temporal-acoustic structure.

**Reported evidence:** The paper reports improved respiratory-sound classification with the proposed denoising approach.

**Limit:** Dataset, labels, recording hardware, noise conditions, and evaluation split limit generalization to clinical deployment or diagnosis.

#### Articulatory modeling of the S-shaped F2 trajectories observed in Öhman's spectrographic analysis of VCV syllables

**Why this belongs:** The S-shaped formant trajectory is a physical consequence of coordinated articulator movement, not an arbitrary curve in a feature plot.

**Mechanism:** The study uses the Maeda articulatory model to reproduce Öhman's S-shaped F2 trajectories and reassesses conventional locus-equation interpretations.

**Mathematical/evaluation object:** The acoustic pattern is an effect of coordinated movement: a model can test whether the pattern follows from planning constraints rather than treating it as an unexplained spectral shape.

**Reported evidence:** The paper reports synthetic trajectories resembling the observed sequences and structured effects of articulatory planning.

**Limit:** Model geometry, trajectory planning, corpus, and synthetic-to-observed comparison limit claims; matching a trajectory does not identify a unique human motor plan.

#### Phonetic Posteriorgram-Based Phoneme Selection for Vocal Cord Disorder Classification in Continuous Mandarin Speech

**Why this belongs:** Phonetic posteriorgrams select speech evidence for vocal-cord-disorder classification, linking acoustic patterns to altered production.

**Mechanism:** The paper proposes phonetic-posteriorgram-based phoneme selection for vocal-cord-disorder classification in continuous Mandarin speech.

**Mathematical/evaluation object:** The recognizer supplies a soft map from sound to phonetic identity; selection makes the diagnostic model focus on the speech units that expose the relevant production difference.

**Reported evidence:** The paper reports classification results for the selected phonetic evidence on continuous Mandarin speech.

**Limit:** Cohort, disorder labels, language, transcript quality, phoneme selection, and recording conditions limit clinical generalization; classification is not diagnosis.

#### PERCEPT-US: A Multimodal American English Child Speech Corpus Specialized for Articulatory Feedback

**Why this belongs:** The corpus pairs child speech with ultrasound articulation and is about observing how physical movement produces the acoustic error.

**Mechanism:** PERCEPT-US provides a multimodal child speech corpus designed for articulatory feedback.

**Mathematical/evaluation object:** The corpus makes a hidden motor target observable: acoustic output can be related to articulator configuration and learner-facing feedback rather than treated as an isolated sound label.

**Reported evidence:** The paper reports corpus resources and articulatory-feedback-oriented evaluation for American English child speech.

**Limit:** Speakers, ages, tasks, sensor alignment, labels, and corpus size limit generalization; a resource does not itself establish learning or clinical benefit.

#### Creaky Voice Facilitates More Efficient Phonological Processing of Mandarin Tone 3

**Why this belongs:** Creaky voice changes how Mandarin tone is produced and heard, linking a voice-quality cue to phonological processing.

**Mechanism:** The paper studies how creaky voice facilitates more efficient phonological processing of Mandarin Tone 3.

**Mathematical/evaluation object:** The speech cue is useful because it changes the listener's inference about a category boundary; processing efficiency is measured behaviorally rather than assumed from an acoustic correlation.

**Reported evidence:** The paper reports behavioral evidence that creaky voice can facilitate Tone 3 processing in the tested Mandarin stimuli.

**Limit:** Listeners, stimuli, tone context, creak manipulation, and task bound the claim; a processing benefit is not a universal production or perception rule.

#### Acoustic similarities, articulatory uniqueness: Speech production mechanisms in individuals with congenital lip paralysis

**Why this belongs:** Congenital lip paralysis makes it possible to ask which acoustic properties remain stable when articulatory choices are constrained.

**Mechanism:** The paper studies acoustic similarities and articulatory uniqueness in speech production by individuals with congenital lip paralysis.

**Mathematical/evaluation object:** Speech production is an inverse problem with compensation: the same acoustic target can arise from different physical routes, so articulatory evidence changes the interpretation of similarity.

**Reported evidence:** The paper reports acoustic and articulatory findings for the affected speakers and comparison conditions.

**Limit:** Cohort, anatomy, language, tasks, imaging or motion measures, and acoustic metrics limit clinical generalization; similarity is not a diagnosis.

#### Articulatory variations in Apical Vowels in Southwestern Mandarin

**Why this belongs:** Apical-vowel contrasts link measured tongue configurations to the acoustic categories listeners hear.

**Mechanism:** The paper analyzes articulatory variations in apical vowels in Southwestern Mandarin.

**Mathematical/evaluation object:** The sound-to-movement mapping is underdetermined: production data reveal which physical differences are tolerated while the acoustic category stays recognizable.

**Reported evidence:** The paper reports articulatory variation and its acoustic relationships for the studied apical vowels.

**Limit:** Speakers, dialect region, imaging or measurement method, vowel context, and sample size limit generalization; variation is not pathology.

#### French schwa is not acoustically distinct  from its two lexical neighbors /ø/ and /œ/

**Why this belongs:** French schwa and neighboring vowels are compared through controlled acoustic conditions to separate vowel quality from stress and spelling.

**Mechanism:** The paper argues that French schwa is not acoustically distinct from its two lexical neighbors /ø/ and /œ/.

**Mathematical/evaluation object:** The study separates category labels from acoustic contrast: a language can maintain a lexical distinction or alternation without a stable one-to-one formant separation.

**Reported evidence:** The paper reports acoustic overlap between French schwa and the neighboring vowels in the tested materials.

**Limit:** Speakers, dialect, context, corpus, measurements, and lexical analysis bound the claim; acoustic overlap is not proof that all grammatical distinctions disappear.

#### Articulatory Feature Prediction from Surface EMG during Speech Production

**Why this belongs:** The title and preserved abstract identify a speech problem whose object and intended intervention fit non-airborne-sensing under room-channel-and-sensing; the assignment does not claim performance beyond the available source.

**Mechanism:** The model minimizes L2 losses for EMA, pitch, and loudness and cross-entropy for phonemes. The predicted EMA coordinates represent tongue, lip, and jaw movement rather than an opaque speech label.

**Mathematical/evaluation object:** Articulatory features provide a structured bottleneck: the system keeps coordinated movement and voice-source information separate, then can use those predictions for later speech reconstruction.

**Reported evidence:** On 7,565 utterances from one male American English speaker, the paper reports strong EMA and loudness prediction and evaluates held-out utterances using correlations against acoustic-inversion targets.

**Limit:** Targets are pseudo-ground truth from acoustic-to-articulatory inversion, the speaker is not diverse, experiments focus on vocalized open-vocabulary speech, and feature prediction is not the same as intelligible silent-speech synthesis.

#### Selective Auditory Attention Decoding in Naturalistic Conversations Using EEG-Based Speech Envelope Tracking in Multi-Speaker Environments

**Why this belongs:** The title and preserved abstract identify a speech object and bounded intervention that instantiate non-airborne-sensing under room-channel-and-sensing; this resolves taxonomy membership only.

**Mechanism:** A multivariate linear model maps 62 EEG channels over 0–200 ms lags to speech-envelope samples; leave-one-trial-out validation compares Pearson correlations for target and distractor streams before and after exogenous switches.

**Mathematical/evaluation object:** The weights minimize squared reconstruction error plus λ||w||². Target selection is an argmax over envelope correlations; chance is 33% for the three-speaker comparison.

**Reported evidence:** Across 36 trials, target-speaker decoding averages 76% ± 12%; performance remains above chance as windows shrink from 20 seconds to 2 seconds, and reconstruction briefly rises after attention switches.

**Limit:** The experiment uses controlled speakers and exogenous switches, short windows still perform poorly, EEG signal-to-noise limits real-time use, and neural decoding is not equivalent to robust everyday source separation.

#### French Listening Tests for the Assessment of Intelligibility, Quality, and Identity of Body-Conducted Speech Enhancement

**Why this belongs:** Human tests must separately measure intelligibility, quality, and identity because body-conducted enhancement may improve one while harming another.

**Mechanism:** Forehead-accelerometer, rigid-in-ear, and throat-microphone signals from Vibravox are enhanced by EBEN; French Modified Rhyme Tests, MUSHRA, and A/B identification are compared with STOI, N-MOS, and ECAPA2 similarity.

**Mathematical/evaluation object:** Pearson correlation links metric values to listener outcomes; the test uses IQR outlier filtering, Shapiro-Wilk normality checks, and 95% significance thresholds.

**Reported evidence:** EBEN improves reported quality and intelligibility but slightly harms female throat-microphone identity; STOI correlates strongly with MUSHRA quality (ρ=.87) and ECAPA2 with identification (ρ=.90), while no tested metric reliably predicts intelligibility change.

**Limit:** The study uses quiet recordings, selected sensors and speakers, one enhancement model, and finite listening tests. Correlation with a perceptual proxy does not establish general clinical or operational usefulness.

#### Sub-band based Adaptive IIR Algorithm with Biquad Filter Stability Constraints for Feedforward Hear-Through Equalization

**Why this belongs:** Hear-through equalization must compensate for direction-dependent acoustic transmission while remaining stable and low-latency.

**Mechanism:** The reference microphone signal is split into sub-bands; feedforward FxLMS/F adaptation updates IIR paths, while cascaded biquads compensate phase/group delay and constrain poles during changing indoor/outdoor conditions.

**Mathematical/evaluation object:** The filter minimizes an error criterion in sub-bands; the fourth-order LMS constraint penalizes unstable coefficient behavior. MSE, SNR, convergence, and multiply-accumulate counts expose the accuracy/latency/complexity trade-off.

**Reported evidence:** The paper reports up to 13 dB improvement over compared adaptive methods in simulated scenarios, with stable behavior and similar complexity in dynamic indoor/outdoor tests.

**Limit:** The evidence is simulation-based and depends on acoustic paths, filter orders, and stability settings; user perception, individualized ears, and end-to-end hardware latency are not established.

#### Relationship between objective and subjective perceptual measures of speech in individuals with head and neck cancer

**Why this belongs:** Speech quality in head-and-neck-cancer patients requires relating measurable acoustic properties to what listeners actually perceive.

**Mechanism:** Trained listeners rate intelligibility, articulation, voice quality, phonation, rate, nasality, and noise; objective measures such as NAD, PCX, PER, SPEED, and SNR are compared using Pearson correlations across 53 Dutch participants.

**Mathematical/evaluation object:** The study treats Pearson r as alignment between a computational proxy and a perceptual target, but interprets correlated targets cautiously because shared treatment severity can induce multiple correlations.

**Reported evidence:** Subjective intelligibility correlates strongly with articulation (r=.95) and voice quality (r=.92); NAD correlates .90 with intelligibility, while phonation and nasality lack reliable objective counterparts in this cohort.

**Limit:** The population is Dutch readers with head-and-neck cancer, not general speech; neural features are not fully interpretable, running spontaneous speech is absent, and correlation does not prove clinical decision validity.

#### Functional Connectivity and Hilbert-Based Features for Covert Speech EEG Variability Analysis and Classification

**Why this belongs:** Covert-speech EEG varies over time and across people, so the analysis asks whether hidden articulation leaves a measurable temporal signature.

**Mechanism:** Phase Locking Value and coherence summarize coordination among EEG channels. Band-specific Hilbert features feed a BiLSTM, while inter-trial, inter-class, and inter-subject analyses separate stable structure from variability.

**Mathematical/evaluation object:** The features are functions of analytic-signal phase and amplitude; classification accuracy measures whether the learned representation separates five speech-command categories across subjects.

**Reported evidence:** The reported subject-independent model reaches 59.14% accuracy across five covert-speech categories and reveals both shared and class-specific connectivity patterns.

**Limit:** Covert speech EEG is not ordinary spoken audio, sample and subject variability constrain the result, class accuracy is not communicative utility, and no independent execution was performed.

#### Band-Split Self-supervised Mamba for Infant-centered Audio Analysis

**Why this belongs:** Infant-centered audio contains events at different time scales; a band-split model tests whether separating those scales preserves useful sound evidence.

**Mechanism:** Band-specific features preserve local spectral evidence while the state-space sequence model carries information over time; self-supervised and supervised objectives share the representation before downstream classification.

**Mathematical/evaluation object:** The system compares classification and representation-learning performance under limited labels, with band ablations testing whether multi-resolution structure matters.

**Reported evidence:** BS-SSAMBA improves infant-centered audio analysis in the reported experiments and benefits from combining unlabeled in-domain audio with limited annotations.

**Limit:** Infant audio is adjacent to, not identical with, human speech; task labels, home environments, class balance, and domain-specific data bound transfer to adult speech systems.

#### Recreating Neural Activity During Speech Production with Language and Speech Model Embeddings

**Why this belongs:** The preserved abstract identifies a speech object and bounded intervention that instantiate non-airborne-sensing under room-channel-and-sensing; this upgrades a provisional candidate to analyst-reviewed taxonomy membership only.

**Mechanism:** Embedding vectors are aligned to neural time windows and mapped to high-gamma responses; reconstruction quality is evaluated across electrodes, time, and representational sources.

**Mathematical/evaluation object:** The paper treats a learned embedding as a hypothesis about what information is available to the brain, and reconstruction error/correlation as a test of that information's neural correspondence.

**Reported evidence:** Language and speech embeddings reconstruct measurable neural activity characteristics, with differences across model type and brain locations reported as evidence about linguistic versus acoustic information.

**Limit:** Neural recordings, participant count, electrode coverage, alignment choices, and correlational reconstruction limit causal interpretation; a good reconstruction is not a speech decoder or clinical interface.

#### Low Complex IIR Adaptive Hear-Through Ambient Filtering for Overcoming Practical Constraints in Earbuds

**Why this belongs:** Hear-through filtering must preserve speech cues while suppressing environmental sound under the computation and latency limits of an earbud.

**Mechanism:** The virtual sensor models the sound pressure at the eardrum; an adaptive IIR filter updates the feedforward path, while constraints on poles/coefficients prevent unstable compensation. Indoor and outdoor acoustic simulations test convergence and delay.

**Mathematical/evaluation object:** Mean-square error, SNR, filter complexity, and processing delay expose the trade-off between matching the open-ear response and maintaining real-time stability.

**Reported evidence:** The proposed low-complexity IIR method reports improved hear-through performance under practical constraints and reduced complexity relative to larger adaptive alternatives.

**Limit:** The evidence is simulation-heavy and depends on acoustic-path and fitting assumptions; user listening, hardware latency, and individualized hearing benefit are not established.

#### Fine-tune Before Structured Pruning: Towards Compact and Accurate Self-Supervised Models for Speaker Diarization

**Why this belongs:** Speaker diarization depends on representations that retain who spoke while compressing the acoustic information used to separate speakers.

**Mechanism:** The teacher supplies representations or logits for the student; structured channel/layer removal creates a compact model, and diarization error rate on far-field meeting corpora measures the retained segmentation and attribution ability.

**Mathematical/evaluation object:** The central object is a constrained compression path: task adaptation changes which parameters matter before pruning, while distillation penalizes deviation from the adapted teacher.

**Reported evidence:** On AMI, AISHELL-4, and AliMeeting, the paper reports that fine-tuning before pruning improves the accuracy/size trade-off over pruning without that order.

**Limit:** Dataset microphone layouts, pruning ratios, teacher/student settings, and DER's treatment of overlap bound the claim; compact diarization is not universal robustness or real-device validation.

#### Effect of Noise Floor in Room Impulse Response on Speech Perception Under Spherical Harmonics-based Spatial Sound Reproduction

**Why this belongs:** The title and preserved abstract identify a speech object and bounded intervention that instantiate reverberant-mixture under room-channel-and-sensing; this resolves taxonomy membership only.

**Mechanism:** The RIR encodes direct and reflected paths; its residual floor changes the rendered reverberant tail, which is tested through intelligibility comparisons.

**Mathematical/evaluation object:** Room reproduction is a channel-matching problem: the measurement’s noise floor is part of the rendered evidence unless controlled.

**Reported evidence:** The paper reports better reproducibility with low-noise-floor RIRs in highly reverberant rooms and at 5 m, while truncation usually did not help.

**Limit:** Rooms, source distances, RIR measurement, listening protocol, and speech-in-noise task bound transfer; perceptual reproducibility is not exact physical localization.

#### LSPnet: an ultra-low bitrate hybrid neural codec

**Why this belongs:** An ultra-low-bitrate codec must compress speech while retaining the time-frequency structure needed for intelligibility.

**Mechanism:** LSPs stabilize spectral-envelope quantization; the neural predictor models sample distributions; time-frequency losses jointly constrain local waveform and spectral behavior.

**Mathematical/evaluation object:** Codec design is a rate-distortion allocation across representations and resolutions, with complexity treated as a deployment constraint.

**Reported evidence:** The paper reports high speech quality at 1.2 kbps and lower complexity than compared end-to-end codecs.

**Limit:** Datasets, bitrate, codec baselines, quality metrics, hardware, and real-time implementation bound transfer; reported quality is not proof for every channel or listener.

#### Unified Microphone Conversion: Many-to-Many Device Mapping via Feature-wise Linear Modulation

**Why this belongs:** The title and preserved abstract identify a speech object and bounded intervention that instantiate microphone-channel under room-channel-and-sensing; this resolves taxonomy membership only.

**Mechanism:** FiLM parameters modulate intermediate features according to device identities, allowing one model to represent multiple channel mappings.

**Mathematical/evaluation object:** Device conversion is a conditional channel transformation: content is shared while microphone response is the variable being controlled.

**Reported evidence:** The paper reports unified microphone conversion results across device mappings without paired examples for every target pair.

**Limit:** Device inventory, pairing protocol, training coverage, content preservation metrics, and acoustic conditions bound transfer; channel conversion is not the same as recognizer invariance.

#### A Data-Driven Diffusion-based Approach for Audio Deepfake Explanations

**Why this belongs:** The captured official PDF and abstract identify a speech object and mechanism instantiating windowed-spectrum under time-frequency-measurement; this upgrades evidence depth for the structured note and does not establish independent reproduction.

**Mechanism:** A spectro-temporal explanation connects model output to changing acoustic regions.

**Mathematical/evaluation object:** The relevant object is the windowed-spectrum evidence described by the paper's mechanism: A spectro-temporal explanation connects model output to changing acoustic regions.

**Reported evidence:** The paper reports a diffusion approach for explaining neural audio deepfake decisions.

**Limit:** Deepfake types, explanation faithfulness, model family, and listener interpretation bound transfer.

### Synthesis boundary

These papers share a conceptual pressure, but this seed batch does not justify ranking methods, estimating prevalence, or claiming that the mechanism generalizes across speakers, languages, rooms, or tasks. Those claims require additional assignments and comparable denominators.

## Listening through noise, overlap, and missing sound

**Ordinary pressure:** A listener often hears several talkers, music, echo, and device noise at once, yet needs one person's words or an intelligible mixture.

**Naive strategy that breaks:** Amplifying everything or subtracting an average noise profile also removes quiet consonants and fails when the interferer changes with the speech.

**Recurring move:** Use structure that differs between target and interference—time, frequency, space, source identity, or learned speech regularity—to estimate and reconstruct the target.

**Boundary:** A cleaner waveform may be less faithful, introduce artifacts, or favor the wrong speaker when the mixture is ambiguous.

**D3 evidence status:** 56 reviewed paper(s); the family claim below is limited to these examples.

**Conceptual family represented:** `spatial-listening/spatial-filtering`, `noise-enhancement/spectral-mask`, `source-separation/blind-source-separation`, `noise-enhancement/nonstationary-noise`, `perceptual-recovery/perceptual-enhancement`, `noise-enhancement/speech-prior-denoising`, `source-separation/blind-source-separation`, `noise-enhancement/speech-prior-denoising`, `spatial-listening/spatial-filtering`, `echo-reconstruction/acoustic-echo-cancellation`, `perceptual-recovery/perceptual-enhancement`, `perceptual-recovery/perceptual-enhancement`, `echo-reconstruction/packet-loss-concealment`, `echo-reconstruction/packet-loss-concealment`, `source-separation/blind-source-separation`, `noise-enhancement/speech-prior-denoising`, `source-separation/target-conditioned-separation`, `perceptual-recovery/perceptual-enhancement`, `noise-enhancement/speech-prior-denoising`, `perceptual-recovery/perceptual-enhancement`, `noise-enhancement/speech-prior-denoising`, `spatial-listening/spatial-filtering`, `perceptual-recovery/perceptual-enhancement`, `noise-enhancement/speech-prior-denoising`, `source-separation/target-conditioned-separation`, `perceptual-recovery/perceptual-enhancement`, `noise-enhancement/speech-prior-denoising`, `noise-enhancement/nonstationary-noise`, `noise-enhancement/speech-prior-denoising`, `noise-enhancement/speech-prior-denoising`, `spatial-listening/spatial-filtering`, `source-separation/target-conditioned-separation`, `source-separation/target-conditioned-separation`, `perceptual-recovery/perceptual-enhancement`, `perceptual-recovery/perceptual-enhancement`, `echo-reconstruction/packet-loss-concealment`, `perceptual-recovery/perceptual-enhancement`, `perceptual-recovery/perceptual-enhancement`, `perceptual-recovery/perceptual-enhancement`, `perceptual-recovery/perceptual-enhancement`, `perceptual-recovery/perceptual-enhancement`, `perceptual-recovery/perceptual-enhancement`, `noise-enhancement/nonstationary-noise`, `source-separation/target-conditioned-separation`, `noise-enhancement/nonstationary-noise`, `noise-enhancement/speech-prior-denoising`, `echo-reconstruction/packet-loss-concealment`, `spatial-listening/spatial-filtering`, `source-separation/target-conditioned-separation`, `spatial-listening/spatial-filtering`, `noise-enhancement/speech-prior-denoising`, `source-separation/target-conditioned-separation`, `noise-enhancement/nonstationary-noise`, `source-separation/target-conditioned-separation`, `noise-enhancement/speech-prior-denoising`, `source-separation/target-conditioned-separation`.

### What the papers make concrete

#### Location-Aware Target Speaker Extraction for Hearing Aids

**Why this belongs:** The target is selected using direction of arrival for a hearing-aid microphone array; the decisive cue is spatial structure, not generic denoising.

**Mechanism:** Spatial features condition separation toward the selected direction.

**Mathematical/evaluation object:** The relevant object is the spatial-filtering evidence described by the paper's mechanism: Spatial features condition separation toward the selected direction.

**Reported evidence:** The paper reports location-aware target-speaker extraction for hearing-aid scenarios.

**Limit:** Array geometry, motion, layout, processing, and intelligibility metric bound transfer.

#### alip25_interspeech

**Why this belongs:** The three-stage system estimates acoustic structure, reduces full-band noise, and refines the spectrum; its boundary is enhancement quality versus faithful speech recovery.

**Mechanism:** Noisy multi-channel inputs produce speech-structure features that interact with spatial cues before later refinement stages.

**Mathematical/evaluation object:** Beamforming combines channels using spatial information; spectral refinement operates over frequency patterns. The design targets the joint spatial-spectral tradeoff.

**Reported evidence:** The paper reports improvements over a reference method on LibriSpeech-based datasets.

**Limit:** The evidence is benchmark-bound and the summary does not establish performance in arbitrary rooms, languages, or devices.

#### Deep-Simplex Multichannel Speech Separation

**Why this belongs:** The paper addresses multichannel separation when the number of simultaneous speakers is not fixed, using mixture structure rather than a known source count.

**Mechanism:** The model consumes multichannel mixtures, estimates source structure and spatial cues, and recursively extracts separated streams; experiments compare source-count and computational behavior.

**Mathematical/evaluation object:** The simplex represents mixture proportions or source assignment under constraints; separation losses compare estimated waveforms or spectra with reference sources and report scale-aware signal metrics.

**Reported evidence:** The paper reports multichannel separation results with a deep-simplex approach designed for variable source conditions and compares it with established separators.

**Limit:** Performance depends on microphone geometry, room conditions, source count, and the reference metrics; synthetic mixtures may not represent real overlap. No independent reproduction was performed.

#### First Analyze Then Enhance: A Task-Aware System for Speech Separation, Denoising, and Dereverberation

**Why this belongs:** The central move is to identify the degradation before choosing separation, denoising, or dereverberation, rather than treating all mixtures alike.

**Mechanism:** A lightweight analyzer uses frozen Whisper/WavLM features, LSTMs, pooling, and a classifier to choose among clean, mixture, noisy/reverberant, and combined conditions. A separator with an attractor estimates an unknown speaker count; a refiner handles noise and reverberation. NAT pretrains separation under noise and DIT trains separator/refiner paths before joint fine-tuning.

**Mathematical/evaluation object:** The analyzer uses four-class cross-entropy. Refinement uses negative SI-SNR; separation uses permutation-invariant SI-SNR so source order does not matter; the attractor uses binary cross-entropy with a stop symbol.

**Reported evidence:** On Libri-3Mix-derived data covering eleven clean, noisy, reverberant, mixed, and combined conditions, FATE reports comparable enhancement quality while reducing unnecessary processing and avoiding overprocessing clean inputs.

**Limit:** The degradations are simulated and drawn from specified mixtures, noises, and rooms; real rooms, analyzer errors, and out-of-distribution combinations are not established. The reported score is author-reported and was not independently reproduced.

#### Voice-ENHANCE: Speech Restoration using a Diffusion-based Voice Conversion Framework

**Why this belongs:** The system reconstructs missing or damaged speech with a speaker-agnostic stage followed by identity-guided diffusion restoration.

**Mechanism:** GSR predicts additive corrections to mel features with a ResU-Net and vocoder, covering noise, reverberation, bandwidth extension, clipping, packet loss, and codec artifacts. The second stage extracts HuBERT discrete content and an ECAPA speaker embedding, predicts a coarse spectrogram, and uses a diffusion U-Net conditioned on content and identity to generate the final waveform.

**Mathematical/evaluation object:** GSR uses GAN, feature-matching, and mel losses; the VC stage combines L1 coarse-spectrogram loss with diffusion noise-prediction loss. NISQA, UTMOS, WV-MOS, and DNSMOS estimate non-intrusive quality on VCTK-DEMAND and UNIVERSE validation sets.

**Reported evidence:** The paper reports that GSR+VC obtains strong objective quality scores across simulated noise, packet loss, bandwidth, reverberation, and codec conditions and compares favorably with the cited restoration systems.

**Limit:** Training uses a proprietary restoration corpus and evaluation uses small/simulated validation settings; non-intrusive quality proxies do not establish word correctness or speaker-faithful repair. No independent reproduction was performed.

#### FUSE: Universal Speech Enhancement using Multi‐Stage Fusion of Sparse Compression and Token Generation Models for the URGENT 2025 Challenge

**Why this belongs:** A three-stage enhancer separates signal-level recovery from generative perceptual repair and then fuses their different targets.

**Mechanism:** Stage 1 predicts an enhanced waveform with mel and SI-SDR losses. Stage 2 conditions masked codec-token prediction on noisy and Stage-1 features and decodes the predicted tokens. Stage 3 receives the noisy signal and both estimates, then adds speaker, phoneme, and perceptual losses. The data contain 2.5K hours of speech, 550 hours of noise, 60K room responses, seven distortion types, and blind samples with an unseen language.

**Mathematical/evaluation object:** The system combines mel-spectrogram, SI-SDR, speaker cosine, phoneme-feature, and UTMOS losses. In the non-blind test, Stage 1 reaches SDR 12.62 and Stage 2 raises UTMOS to 2.38 but lowers SDR to 9.03; the fusion stage reaches UTMOS 2.64 and SDR 12.53 before shift averaging.

**Reported evidence:** On the blind challenge set, the system reports DNSMOS 2.94, NISQA 3.25, UTMOS 2.19, MOS 3.44, and CER 77.09; it ranks behind the top system on several signal-level measures but leads the listed systems on perceptual measures.

**Limit:** The challenge mixtures, five training languages, unseen Japanese test condition, and 900-sample blind set define the evidence. The sequential three-stage inference and shift operations restrict real-time use; all results are author-reported and no independent reproduction was performed.

#### ReSepNet: A Unified-Light Model for Recursive Speech Separation with Unknown Speaker Count

**Why this belongs:** Recursive separation makes the unknown speaker count part of the separation problem.

**Mechanism:** ReSepNet applies a dual-path transformer repeatedly; each iteration estimates one source and cross-correlation decides whether another iteration is needed. It trains on two/three-speaker mixtures and tests on four/five.

**Mathematical/evaluation object:** Permutation-invariant loss ignores output order. SI-SNR improvement is 21.16 dB on WSJ0-2mix, 19.19 on 3mix, 14.91 on 4mix, and 12.03 on 5mix; the 2.8M-parameter model estimates count with 96.6% accuracy.

**Reported evidence:** The paper reports higher SI-SNR improvement than listed baselines and generalization from two/three-speaker training to four/five-speaker tests.

**Limit:** The evidence is synthetic WSJ0 mixtures, 8-kHz four-second windows, and a bounded count range; real rooms and end-to-end recognition are not tested. Results are author-reported.

#### Structured Codebook Based Hierarchical Framework for DNN for Computationally Efficient Speech Enhancement

**Why this belongs:** Structured codebooks reduce enhancement cost by exploiting regularities in speech parameters.

**Mechanism:** Hierarchically clustered log-power-spectrum vectors drive codebook stages and enhancement predictors evaluated on VoiceBank-DEMAND.

**Mathematical/evaluation object:** The paper compares SSNR and computational cost; codebook classifiers use cross-entropy and the table reports parameter/runtime burden.

**Reported evidence:** The framework reduces computation while retaining comparable or improved enhancement scores over the reference systems.

**Limit:** One corpus and parameterized spectral targets bound the evidence; downstream ASR and perceptual benefit are not fully established.

#### Spatio-Spectral Diarization of Meetings by Combining TDOA-based Segmentation and Speaker Embedding-based Clustering

**Why this belongs:** TDOA and speaker embeddings combine room geometry with voice identity without equating position to identity.

**Mechanism:** TDOA detects regions, embeddings assign speakers, cACGMM optionally refines them, and compact/distributed microphone setups are tested.

**Mathematical/evaluation object:** DER measures segmentation/assignment and cpWER measures transcript performance after diarization.

**Reported evidence:** The combined pipeline outperforms single-channel pyannote in reported compact and distributed meeting scenarios.

**Limit:** Layouts, datasets, overlap, and spatial cues bound the result; evaluations are author-reported.

#### Room Impulse Response as a Prompt for Acoustic Echo Cancellation

**Why this belongs:** Room impulse response prompts condition echo cancellation on the physical echo path to improve mismatch generalization.

**Mechanism:** ICCRN receives several RIR-prompt fusion variants; tests cover matched and mismatched synthetic RIRs plus recorded real RIRs in double-talk and far-end single-talk conditions.

**Mathematical/evaluation object:** ERLE measures echo suppression, PESQ near-end quality, SDR near-end fidelity, and MACs/parameters expose the prompt cost.

**Reported evidence:** Fusion method (d) is strongest on mismatched and real-RIR ICCRN tests; the reported real-RIR double-talk values are PESQ 2.19 and ERLE 4.79.

**Limit:** The selected model, fusion choices, RIRs, and author-reported tables bound the claim; independent reproduction and broad room coverage remain absent.

#### Benchmarking Neural Speech Codec Intelligibility with SITool

**Why this belongs:** Subjective intelligibility testing separates whether a codec preserves identifiable speech from whether it merely scores well on quality or WER.

**Mechanism:** SITool runs Diagnostic and Modified Rhyme Tests in laboratory or crowdsourcing settings; thirteen codecs are evaluated with phoneme, gender, and wordlist analyses.

**Mathematical/evaluation object:** Subjective scores are compared with STOI, ESTOI, and WER; only STOI and ESTOI significantly correlate in the reported analysis.

**Reported evidence:** Some neural codecs outperform traditional codecs in subjective intelligibility, but objective agreement varies and scores show gender- and wordlist-specific differences.

**Limit:** The codec set, English tests, listener screening, and objective metrics bound the conclusion; the toolkit does not remove human evaluation.

#### MiSTR: Multi-Modal iEEG-to-Speech Synthesis with Transformer-Based Prosody Prediction and Neural Phase Reconstruction

**Why this belongs:** Neural-signal speech reconstruction separates content/prosody prediction from waveform phase reconstruction.

**Mechanism:** MiSTR uses a multimodal iEEG encoder, Transformer spectrogram/prosody prediction, and a neural phase vocoder with adaptive spectral correction.

**Mathematical/evaluation object:** Mel-spectrogram correlation, intelligibility, naturalness, and MOSA expose different reconstruction failures; MOSA is reported at 3.38.

**Reported evidence:** The paper reports higher fidelity and naturalness than listed baselines and MOSA 3.38.

**Limit:** Dataset, subjects, protocol, learned evaluator, and paper-reported comparisons limit clinical claims.

#### Discovering Directions of Uncertainty in Speech Inpainting

**Why this belongs:** Speech inpainting represents multiple plausible repairs so missing evidence is not mistaken for known content.

**Mechanism:** NPPC predicts principal components of the conditional output distribution; traversing components produces alternative spectrograms and transcripts.

**Mathematical/evaluation object:** NPPC is reported as 50x faster than 50-sample MC Dropout with slightly better reconstruction error.

**Reported evidence:** Principal directions change word identity and pitch; NPPC captures diverse outputs while matching or improving dropout error.

**Limit:** The data, posterior approximation, audio examples, and benchmark define the result; calibration and user decision rules remain unresolved.

#### TS-URGENet: A Three-stage Universal Robust and Generalizable Speech Enhancement Network

**Why this belongs:** Packet loss is missing acoustic evidence that requires explicit reconstruction before ordinary enhancement.

**Mechanism:** The filling stage predicts lost regions, separation suppresses noise/reverb/clipping, and restoration repairs bandwidth, codec, and remaining loss.

**Mathematical/evaluation object:** Stage-wise spectral or waveform reconstruction is evaluated in the URGENT challenge setting.

**Reported evidence:** The system ranked second in URGENT Track 1.

**Limit:** Challenge conditions, author-reported ranking, and no independent run limit the claim.

#### Overlap-Adaptive Hybrid Speaker Diarization and ASR-Aware Observation Addition for MISP 2025 Challenge

**Why this belongs:** Meeting recognition combines overlap-aware diarization and ASR-aware observation construction because mixed speakers cannot be separated perfectly first.

**Mechanism:** A hybrid segmentation/clustering diarizer selects its model by overlap, while ASR-aware observations compensate for weak guided separation before recognition.

**Mathematical/evaluation object:** Diarization assigns speaker-time regions; CER and concatenated minimum-permutation CER measure the downstream meeting transcript.

**Reported evidence:** The system reports 9.48% CER and 11.56% cpCER and first place in both MISP tracks.

**Limit:** Challenge tracks, meeting conditions, and author-reported ranking limit generalization and independent reproduction.

#### Test-Time Training for Speech Enhancement

**Why this belongs:** The captured paper's ordinary problem, mechanism, and reported evaluation directly instantiate speech-prior-denoising within noise-enhancement.

**Mechanism:** The main enhancement task shares representations with an auxiliary task optimized on the current noisy signal, with strategies trading adaptation gain against test-time cost.

**Mathematical/evaluation object:** The method treats deployment as a second learning stage: the signal supplies an unsupervised clue about the new domain while the enhancement objective remains the output target.

**Reported evidence:** The paper reports consistent speech-quality improvements over its baseline on synthetic and real-world datasets.

**Limit:** The adaptation steps, compute budget, noise conditions, and author-reported metrics bound the result; listener benefit and long-term stability remain open.

#### NeuroSpex+: Dual-Task Training of Neuro-Guided Speaker Extraction with Speech Envelope and Waveform

**Why this belongs:** Neural and speech-envelope evidence guide extraction of a target speaker when the mixture itself does not identify which voice matters.

**Mechanism:** A shared model predicts the target signal and its envelope; the dual losses constrain both fine waveform detail and slower attended-speech structure.

**Mathematical/evaluation object:** Multi-task objectives shape the latent mask toward a target defined by two related projections of the attended speaker.

**Reported evidence:** NeuroSpex+ reports improved overall signal quality over baselines in the evaluated neuro-guided extraction setting.

**Limit:** EEG alignment, subjects, mixtures, signal metric, and lab conditions bound transfer; signal quality is not a demonstrated BCI communication benefit.

#### A Deformable Convolution GAN Approach for Speech Dereverberation in Cochlear Implant Users

**Why this belongs:** Dereverberation repairs temporal smearing especially harmful to cochlear-implant listeners; the target is intelligible speech, not merely a cleaner spectrum.

**Mechanism:** A deformable-convolution GAN is trained for dereverberation, first tested on REVERB and then assessed in listening tests with normal-hearing and CI users.

**Mathematical/evaluation object:** The learned offsets change which neighboring time-frequency evidence is combined; intelligibility and quality are judged by objective tests and listener responses.

**Reported evidence:** The paper reports markedly improved CI speech intelligibility by preserving envelope and transient structure.

**Limit:** The claim is bounded to REVERB conditions, the tested listeners, and the GAN configuration; broader hearing profiles, rooms, and independent replication remain open.

#### Improved Intelligibility of Dysarthric Speech using Conditional Flow Matching

**Why this belongs:** Dysarthric speech enhancement must improve intelligibility without smoothing away atypical but meaningful speech cues.

**Mechanism:** The study compares mel-spectrogram and quantized SSL features, controls the output voice with WavLM-derived information, and evaluates generated speech for dysarthric intelligibility.

**Mathematical/evaluation object:** The learned flow maps a conditioning representation to clean-speech acoustics; intelligibility and convergence compare feature choices and generation paths.

**Reported evidence:** The paper reports that discrete acoustic units improve intelligibility and converge faster than the mel-spectrogram alternative.

**Limit:** The result is bounded to the speakers, severity range, target voice, and tested listening/evaluation protocol; naturalness, identity preservation, and clinical benefit remain open.

#### Listen through the Sound: Generative Speech Restoration Leveraging Acoustic Context Representation

**Why this belongs:** Speech restoration must infer which distortion is present before repairing it; acoustic context is used to condition the repair.

**Mechanism:** ACX refines CLAP-derived environmental embeddings and conditions the diffusion restoration model UNIVERSE++ across distortion conditions.

**Mathematical/evaluation object:** Restoration quality and stability across conditions compare context-aware and content-based conditioning; variability itself is an evaluation target.

**Reported evidence:** The paper reports better restoration and reduced performance variability with acoustic context.

**Limit:** The result is tied to the distortion set, CLAP features, and diffusion backbone; unseen devices, rooms, and perceptual listeners remain open.

#### QUADS: Quantized Distillation Framework for Efficient Speech Language Understanding

**Why this belongs:** Quantized distillation tests how much speech-understanding quality survives when an audio-language system is made smaller and cheaper.

**Mechanism:** QUADS jointly optimizes a pretrained SLU model for low-bit regimes and evaluates it on SLURP and FSC.

**Mathematical/evaluation object:** Accuracy measures task retention, while GMACs and model size measure compute and storage cost.

**Reported evidence:** The paper reports 71.13% SLURP and 99.20% FSC accuracy, 60–73x lower GMACs, and 83–700x smaller models with bounded degradation.

**Limit:** The result depends on tasks, bit settings, and hardware interpretation of the counts; latency and energy on deployed devices remain open.

#### SoundSculpt: Direction and Semantics Driven Ambisonic Target Sound Extraction

**Why this belongs:** Direction and semantic target cues let an ambisonic system extract one sound from a spatial mixture instead of amplifying the entire scene.

**Mechanism:** The network maps multichannel ambisonic mixtures to a target sound field; direction and image-derived semantic embeddings guide the mask or representation used for extraction.

**Mathematical/evaluation object:** Spatial filtering and semantic conditioning define complementary constraints: the output must preserve the target's spatial structure while suppressing other sources.

**Reported evidence:** SoundSculpt outperforms the reported signal-processing baselines on synthetic and real ambisonic mixtures, with joint spatial-semantic conditioning helping in difficult cases.

**Limit:** Synthetic scene construction, ambisonic order, semantic detector quality, room conditions, and target definition bound transfer; benchmark improvement is not guaranteed perceptual source isolation in arbitrary rooms.

#### Linguistic Masking and Its Release in Simulated Electric-acoustic Hearing

**Why this belongs:** Linguistic masking in simulated electric-acoustic hearing asks which missing or distorted speech cues matter to a listener, not merely which samples differ.

**Mechanism:** Mandarin sentences are mixed with language-controlled babble, processed by noise vocoders simulating CI or EAS hearing, and scored through sentence recognition.

**Mathematical/evaluation object:** Release from masking is the difference in recognition between a target with and without a linguistic advantage; comparing those differences separates hearing mode from masker language.

**Reported evidence:** The study reports a combined-stimulation advantage across all three masker languages and language-specific differences in release from masking.

**Limit:** Normal-hearing listeners, vocoder simulations, Mandarin targets, and the selected masker languages limit direct claims about real CI users and everyday rooms.

#### Objective and Subjective Evaluation of Diffusion-Based Speech  Enhancement for Dysarthric Speech

**Why this belongs:** The paper asks whether diffusion enhancement can make dysarthric speech more intelligible without erasing atypical cues needed by recognition.

**Mechanism:** The systems enhance two English dysarthric corpora; Whisper-Turbo is evaluated before and after enhancement and fine-tuning.

**Mathematical/evaluation object:** The paper treats intelligibility, speech quality, and recognition as separate targets, exposing disagreement between them.

**Reported evidence:** The study reports a systematic comparison rather than a single score; gains and tradeoffs depend on corpus, enhancer, and evaluation target.

**Limit:** The corpora, listener tests, Whisper model, and enhancement settings bound the result; a recognition gain is not automatically a clinical benefit.

#### MOPSA: Mixture of Prompt-Experts Based Speaker Adaptation for Elderly Speech Recognition

**Why this belongs:** Speaker adaptation for elderly speech asks whether target-speaker characteristics can guide recognition when voice and environment differ.

**Mechanism:** MOPSA uses K-means speaker prompt clusters and a router around Whisper, with separate acoustic and language-level prompts, tested on English and Cantonese elderly speech.

**Mathematical/evaluation object:** The router is a mixture-of-experts choice; WER/CER measure recognition and real-time factor measures adaptation cost.

**Reported evidence:** The paper reports relative WER/CER reductions of 4.21% and 5.40% and up to 16.12x real-time speedup over offline adaptation.

**Limit:** Datasets, elderly populations, prompt clusters, and Whisper versions bound the claim; broader disorders, languages, and online failure recovery remain open.

#### Efficient Neural and Numerical Methods for High-QualityOnline Speech Spectrogram Inversion via Gradient Theorem

**Why this belongs:** Spectrogram inversion asks what information is lost when a time-frequency picture is turned back into a waveform, and which numerical or learned assumptions fill the gap.

**Mechanism:** The online inversion model uses 8k parameters, adds at most one hop of latency, and applies a linear-complexity solver after predicting derivative information.

**Mathematical/evaluation object:** Phase reconstruction becomes a structured inverse problem; the solver uses matrix structure instead of treating every coefficient as unrelated.

**Reported evidence:** The paper reports a 30x smaller network, a further halving of neural cost with one-hop latency, and orders-of-magnitude solver speedup while retaining quality.

**Limit:** Spectrogram settings, audio domain, latency definition, and samples bound the claim; listening tests and hardware deployment remain separate checks.

#### Model as Loss: A Self-Consistent Training Paradigm

**Why this belongs:** The official archive evidence identifies a human spoken-speech object and a bounded problem that instantiate speech-prior-denoising under noise-enhancement; this resolves membership only.

**Mechanism:** A speech-enhancement decoder is trained against features from its own encoder and compared with handcrafted and pretrained deep-feature losses on standard benchmarks.

**Mathematical/evaluation object:** The loss measures consistency in a learned representation rather than raw sample distance; perceptual metrics and out-of-domain tests expose whether that representation transfers.

**Reported evidence:** The paper reports better perceptual quality than pretrained feature losses and robust generalization in both in-domain and out-of-domain tests.

**Limit:** The encoder, training data, noise conditions, perceptual metrics, and benchmark protocols bound the result; feature agreement is not identical to intelligibility or listener preference.

#### A Novel Deep Learning Framework for Efficient Multichannel Acoustic Feedback Control

**Why this belongs:** The official archive evidence identifies a human spoken-speech object and a bounded problem that instantiate nonstationary-noise under noise-enhancement; this resolves membership only.

**Mechanism:** A convolutional recurrent network controls multichannel acoustic feedback; in-loop, teacher-forced, and hybrid training are compared in complex acoustic environments.

**Mathematical/evaluation object:** The task is closed-loop control: the output changes the next input, so stability and enhancement must be evaluated together rather than on isolated noisy clips.

**Reported evidence:** The paper reports improved speech enhancement with lower computational demand across the proposed training strategies.

**Limit:** The device geometry, microphones, loudspeakers, feedback paths, training regime, and metrics bound the result; laboratory suppression does not establish stable operation for every room or device.

#### Scaling and Enhancing LLM-based AVSR:  A Sparse Mixture of Projectors Approach

**Why this belongs:** Audio-visual recognition uses visual speech evidence to compensate for acoustic noise, while sparse projectors address multimodal cost.

**Mechanism:** Llama-SMoP uses sparsely gated mixtures of projectors with modality-specific routers and experts and is evaluated on ASR, visual speech recognition, and AVSR under noise.

**Mathematical/evaluation object:** Conditional computation separates representational capacity from per-example computation; ASR/VSR/AVSR performance, activation patterns, and noise robustness test the tradeoff.

**Reported evidence:** The DEDR configuration reports the strongest results among the tested variants, with ablations supporting expert activation, scalability, and noise robustness.

**Limit:** Model size, routing policy, datasets, noise, and compute accounting bound the claim; sparse projector success does not automatically transfer to every multimodal LLM.

#### DiffDSR: Dysarthric Speech Reconstruction Using Latent Diffusion Model

**Why this belongs:** Dysarthric speech reconstruction uses a generative prior to repair atypical articulation, with intelligibility gains bounded by the danger of changing the speaker's intended content.

**Mechanism:** Separate content and identity conditioning feed a diffusion generator that samples a reconstructed waveform in latent space.

**Mathematical/evaluation object:** The system imposes two invariants on generation: linguistic content must be restored while speaker identity remains in the conditioning path.

**Reported evidence:** The paper reports improved intelligibility and speaker similarity in its dysarthric speech reconstruction evaluation.

**Limit:** Speaker, severity, reference data, perceptual metrics, and diffusion sampling bound transfer; reconstructed speech is not clinical treatment evidence.

#### A Study of Real-world Audio-Visual Corpus Design and Production: A Perspective from MISP Challenges

**Why this belongs:** A real-world audio-visual corpus preserves visual and acoustic evidence needed when speech is mixed with competing sources.

**Mechanism:** The paper analyzes the MISP 2022–2024 corpora for audio-visual wakeup, diarization, enhancement, and recognition, covering scenario selection, recording equipment/processes, manual transcription, and alignment.

**Mathematical/evaluation object:** A corpus is part of the measurement apparatus: room, device, overlap, annotation, and synchronization define the conditional distribution on which a model is judged.

**Reported evidence:** The paper reports broad adoption of the corpora by over 110 teams and identifies design strengths and limitations that affect audio-visual speech-processing comparisons.

**Limit:** Challenge construction, participant selection, language, room/device coverage, and annotation policy bound generalization; downloading or winning on a corpus does not prove deployment realism.

#### IDIR: Identifying and Distilling Informative Relations for Speaker Verification

**Why this belongs:** Speaker verification can use relations among informative regions of an utterance to decide whether a target identity is present.

**Mechanism:** IDIR identifies informative relations in each mini-batch, distills them from teacher to student, and uses margin-adjusted similarity scores for speaker verification.

**Mathematical/evaluation object:** The object being transferred is a geometry of identities rather than a list of feature values; similarity and verification thresholds test whether that geometry survives compression.

**Reported evidence:** The paper reports improved speaker-verification performance over feature-matching distillation and stronger separation of same- and different-speaker relations.

**Limit:** Teacher/student architectures, pair mining, margin, dataset, and verification protocol bound the claim; relational distillation does not ensure robustness to domain, overlap, or fairness shifts.

#### Synchronous analysis of abnormal acoustic and linguistic production in Parkinson's speech

**Why this belongs:** Parkinsonian speech contains acoustic and linguistic changes together; synchronized analysis asks which signal belongs to which kind of impairment.

**Mechanism:** The study synchronizes analysis of abnormal acoustic and linguistic production in Parkinson's speech.

**Mathematical/evaluation object:** Synchronous observation aligns two levels of behavior in time, allowing co-occurrence to be studied without pretending that either level alone explains the condition.

**Reported evidence:** The paper reports coordinated acoustic and linguistic findings in Parkinson's speech.

**Limit:** Cohort, task, disease stage, annotation, and statistical design limit clinical generalization; association is not diagnosis or causation.

#### Analysis and Extension of a Near-End Listening Enhancement Method Based on Long-Term Fractile Noise Statistics

**Why this belongs:** The preserved abstract identifies a speech object and bounded intervention that instantiate perceptual-enhancement under echo-and-reconstruction; this upgrades a provisional candidate to analyst-reviewed taxonomy membership only.

**Mechanism:** The paper analyzes and extends a near-end listening-enhancement method based on long-term fractile noise statistics.

**Mathematical/evaluation object:** The method treats noise as a distribution over time rather than a single fixed level; enhancement is constrained by the estimated noise floor so speech structure is not indiscriminately removed.

**Reported evidence:** The paper reports listening-enhancement results for the proposed statistical method and its extension.

**Limit:** Noise type, recordings, listeners, parameter settings, and perceptual tests limit generalization; improved quality is not identical to improved intelligibility.

#### Modality-Agnostic Multimodal Emotion Recognition using a Contrastive Masked Autoencoder

**Why this belongs:** Modality-agnostic emotion recognition must recover useful affective evidence when one audio or visual channel is missing or corrupted.

**Mechanism:** The paper proposes a contrastive masked-autoencoder model for modality-agnostic multimodal emotion recognition on MSP-Podcast.

**Mathematical/evaluation object:** The model learns shared structure while treating missingness as a normal observation condition; reconstruction supplies a bridge, but prediction must still be judged against the available evidence.

**Reported evidence:** The paper reports improvements over unimodal and multimodal baselines and robustness to missing modalities.

**Limit:** Corpus, emotion labels, missingness pattern, modality quality, and reconstruction objective bound the claim; emotion inference is not guaranteed to be socially reliable.

#### Extended Loss: Incorporating Long Context into Training Models when using Short Audio Frames

**Why this belongs:** Short audio windows can hide long-range context; the paper asks whether adding broader context restores information needed for the decision.

**Mechanism:** The paper proposes Extended Loss for acoustic echo cancellation with short audio frames and limited latency.

**Mathematical/evaluation object:** The loss supervises the local output using context that spans frame boundaries; training context and inference delay are separated rather than traded as the same quantity.

**Reported evidence:** The paper reports reduced boundary discontinuities and improved short-frame AEC performance under the tested real-time conditions.

**Limit:** Echo paths, frame size, batch context, hardware, and evaluation signals bound the claim; continuity on the benchmark is not proof of every room or device.

#### Vision-Integrated High-Quality Neural Speech Coding

**Why this belongs:** Speech coding must preserve perceptually important detail when visual information can help distinguish or reconstruct the sound.

**Mechanism:** The paper presents a vision-integrated high-quality neural speech coding system.

**Mathematical/evaluation object:** Coding becomes cross-modal reconstruction: the decoder uses synchronized visual evidence to fill or protect acoustic detail while the rate constraint limits what can be transmitted.

**Reported evidence:** The paper reports high-quality neural coding results for the tested audio-visual conditions.

**Limit:** Video quality, synchronization, speakers, bitrate, decoder, and missing-video behavior bound the claim; visual assistance can introduce privacy and spoofing risks.

#### PAST: Phonetic-Acoustic Speech Tokenizer

**Why this belongs:** A speech tokenizer should retain phonetic information while compressing the signal into reconstructable acoustic units.

**Mechanism:** PAST is a phonetic-acoustic speech tokenizer.

**Mathematical/evaluation object:** Tokenization is a choice about what survives discretization: units should preserve acoustically grounded, phonetic information while discarding redundant waveform variation.

**Reported evidence:** The paper reports tokenizer quality and downstream speech-representation results for the proposed phonetic-acoustic units.

**Limit:** Token rate, codebook, languages, speakers, reconstruction target, and downstream tasks bound the claim; discrete units are not automatically linguistically complete.

#### VoiceNoNG: Robust High-Quality Speech Editing Model without Hallucinations

**Why this belongs:** Speech editing must change a requested region without hallucinating unrelated content or failing under background audio.

**Mechanism:** VoiceNoNG is a robust high-quality speech-editing model designed to avoid hallucinations.

**Mathematical/evaluation object:** Editing is constrained completion: the model must change a local region while preserving identity, timing, and untouched context, so faithfulness is a separate target from audio quality.

**Reported evidence:** The paper reports speech-editing quality and reduced hallucination behavior for the tested edits.

**Limit:** Edit type, context length, speaker set, alignment, metrics, and human judgments bound the claim; no-hallucination behavior is not guaranteed under arbitrary prompts.

#### SpeechRefiner: Towards Perceptual Quality Refinement for Front-End Algorithms

**Why this belongs:** The preserved abstract identifies a speech object and bounded intervention that instantiate perceptual-enhancement under echo-and-reconstruction; this upgrades a provisional candidate to analyst-reviewed taxonomy membership only.

**Mechanism:** SpeechRefiner targets perceptual quality refinement for front-end speech algorithms.

**Mathematical/evaluation object:** Refinement is a second-stage correction problem: the input already contains a useful transformation, so the model must remove artifacts while preserving the first stage's content and gains.

**Reported evidence:** The paper reports perceptual and signal-quality improvements for refined front-end outputs.

**Limit:** Front-end types, distortion, training targets, listeners, metrics, and content preservation bound the result; quality improvement is not guaranteed for unseen algorithms.

#### HWB-Net: A Novel High-Performance and Efficient Hybrid Waveform Bandwidth Extension Method

**Why this belongs:** The title and preserved abstract identify a speech object and bounded intervention that instantiate perceptual-enhancement under echo-and-reconstruction; this resolves taxonomy membership only.

**Mechanism:** HWB-Net is a high-performance efficient hybrid waveform bandwidth-extension method.

**Mathematical/evaluation object:** Bandwidth extension is constrained synthesis: the model predicts plausible missing detail from the observed signal while preserving timing and identity in the known band.

**Reported evidence:** The paper reports quality and efficiency results for HWB-Net on bandwidth-extension tests.

**Limit:** Bandwidth limit, speakers, noise, training targets, metrics, and listening protocol bound the result; plausible detail is not recovered ground truth.

#### A Neural Codec Approach for Noise-Robust Bandwidth Expansion

**Why this belongs:** The title and preserved abstract identify a speech object and bounded intervention that instantiate perceptual-enhancement under echo-and-reconstruction; this resolves taxonomy membership only.

**Mechanism:** The paper proposes a neural codec approach for noise-robust bandwidth expansion.

**Mathematical/evaluation object:** The codec treats missing frequency content and corruption as coupled inference: it must reconstruct a plausible high band conditioned on what the noisy low band actually supports.

**Reported evidence:** The paper reports bandwidth-expansion quality and noise robustness for the proposed neural codec.

**Limit:** Noise types, bandwidth, codec rate, speakers, targets, and perceptual evaluation bound the result; plausible high-frequency detail is not ground truth.

#### Towards Bitrate-Efficient and Noise-Robust Speech Coding with Variable Bitrate RVQ

**Why this belongs:** Speech coding must preserve intelligible structure under noisy conditions and changing bitrate, so compression and noise robustness cannot be treated independently.

**Mechanism:** The paper proposes Variable Bitrate RVQ for noise-robust speech coding.

**Mathematical/evaluation object:** Compression is selective reconstruction: the codec decides which parts of a noisy frame deserve precision, so rate, distortion, denoising, and perceptual quality must be evaluated together.

**Reported evidence:** The paper reports improved rate-distortion trade-offs and perceptual quality over constant-bitrate baselines in noisy conditions.

**Limit:** Noise conditions, bitrates, codec architecture, datasets, perceptual measures, and model sizes bound the result; a cleaner perceptual signal is not necessarily a faithful waveform.

#### Relative cue weighting in multilingual stop voicing production

**Why this belongs:** Multilingual stop voicing provides a controlled case where listeners and speakers must weight competing acoustic timing cues differently.

**Mechanism:** The paper studies relative cue weighting in multilingual stop-voicing production.

**Mathematical/evaluation object:** Multilingual pronunciation is coordinated but not collapsed: language-specific cue bundles coexist with influence from which language is dominant for the speaker.

**Reported evidence:** The paper reports language-specific production for all early multilinguals, dominance-driven variation, and a salient role for closure voicing in Malaysian English.

**Limit:** The Malaysian speakers, three languages, stop inventory, nine correlates, and random-forest analysis bound generalization to other multilingual populations or contrasts.

#### Adaptive Knowledge Distillation for Device-Directed Speech Detection

**Why this belongs:** Device-directed speech detection must distinguish intended speech from changing household or device audio without assuming a fixed noise profile.

**Mechanism:** The paper proposes adaptive knowledge distillation for device-directed speech detection.

**Mathematical/evaluation object:** The assistant’s first decision is social and acoustic: before understanding words, it must infer whether the words are meant for it; general speech knowledge helps, but the invocation boundary needs task-specific evidence.

**Reported evidence:** The paper reports EER improvements of 26% for keyword and 19% for keyword-free follow-up invocations, with gains across transformer and conformer students.

**Limit:** Invocation types, EER, teacher/student architectures, training data, and device conditions bound deployment claims; a benchmark detector cannot infer intent perfectly in every home.

#### Multistage Universal Speech Enhancement System for URGENT Challenge

**Why this belongs:** The preserved abstract identifies a speech object and bounded intervention that instantiate speech-prior-denoising under noise-enhancement; this upgrades a provisional candidate to analyst-reviewed taxonomy membership only.

**Mechanism:** Model the degraded signal as a composition of distortion operators; use Demucs for declipping, BSRoformer for separation, BS-PLCNet in a PQMF subband domain for packet loss, and a time-frequency recurrent inpainting network for spectral artifacts.

**Mathematical/evaluation object:** The key object is a masked signal and a composition of operators. Separating domains and ordering repairs reduces the optimization problem from one tangled inverse map to several bounded inverse problems.

**Reported evidence:** The system reports URGENT challenge results competitive with the compared systems; adding inpainting and self-distillation improves several quality measures, while downstream accuracy and objective metrics do not all move together.

**Limit:** Challenge datasets, distortion order, detector errors, resampling to 48 kHz for some modules, metric choice, and author-reported rankings bound the claim; plausible filling is not recovery of the original samples.

#### Rollback Speech: Smart Feedback Prompts for Lost Utterances in Unstable Online Calls

**Why this belongs:** The preserved abstract identifies a speech object and bounded intervention that instantiate packet-loss-concealment under echo-and-reconstruction; this upgrades a provisional candidate to analyst-reviewed taxonomy membership only.

**Mechanism:** The system is an interaction loop: dual transcripts provide two views of the communication event, discrepancy detection estimates the missing interval, and keyword extraction compresses the repair request into actionable cues.

**Mathematical/evaluation object:** This is not waveform packet-loss concealment. It preserves conversational meaning through human-in-the-loop selective repetition when acoustic reconstruction is unsafe or unavailable.

**Reported evidence:** The paper demonstrates a WebRTC/WebSocket prototype using Whisper and NLTK keyword extraction in a simulated brief disconnection; it is a show-and-tell feasibility demonstration rather than a controlled recovery benchmark.

**Limit:** Two-person demonstration conditions, simulated network failure, ASR errors, keyword quality, privacy/latency trade-offs, and absence of a listening study bound the result.

#### Deep learning based spatial aliasing reduction in beamforming for audio capture

**Why this belongs:** Beamforming in a spatially aliased array asks how to recover a useful direction when microphone spacing makes the spatial measurements ambiguous.

**Mechanism:** The model estimates a filter from multichannel spectro-temporal input; the corrected beamformer output is evaluated in common spatial-capture scenarios against conventional and learned alternatives.

**Mathematical/evaluation object:** The learned filter approximates an inverse of geometry-induced aliasing, but its validity depends on the array and acoustic distribution represented during training.

**Reported evidence:** The paper reports reduced spatial aliasing and improved spatial/spectral capture measures for the proposed deep-learning correction in the tested scenarios.

**Limit:** Array geometry, source locations, reverberation, training mixtures, and scenario coverage constrain generalization; simulated or benchmark gains do not establish robustness for every microphone layout.

#### CabinSep: IR-Augmented Mask-Based MVDR for Real-Time In-car Speech Separation with Distributed Heterogeneous Arrays

**Why this belongs:** In-car separation uses room responses and spatial cues to preserve speech in a moving vehicle while suppressing competing sound.

**Mechanism:** The mask estimates speech/noise structure from multichannel features; MVDR uses spatial covariance to preserve the chosen target, while mixed impulse-response augmentation exposes zone-boundary variation.

**Mathematical/evaluation object:** Separation is constrained by two objectives: suppress interference through spatial covariance while retaining a distortionless target direction for the recognizer.

**Reported evidence:** CabinSep reports a 17.5% relative ASR error reduction over DualSep on real recordings at 0.4 GMACs, with better behavior around speaker-zone boundaries.

**Limit:** Cabin geometry, array placement, impulse-response coverage, ASR backend, and compute measure constrain generalization; ASR improvement is not proof of perceptual superiority for every listener.

#### End-to-End DOA-Guided Speech Extraction in Noisy Multi-Talker Scenarios

**Why this belongs:** The title and preserved abstract identify a speech problem whose object and intended intervention fit spatial-filtering under source-separation-and-spatial-listening; the assignment does not claim performance beyond the available source.

**Mechanism:** The model combines spatial and temporal features, uses the DOA as a center and beamwidth as the permitted region, and generates the target waveform for enhancement and ASR.

**Mathematical/evaluation object:** The beamwidth is a controllable spatial prior: narrowing it suppresses more off-axis energy but risks target loss, while widening it preserves coverage at the cost of interference.

**Reported evidence:** The paper reports stronger target enhancement, interference suppression, and downstream ASR performance in the evaluated noisy multi-talker scenarios.

**Limit:** DOA estimation, array geometry, spatial overlap, noise type, beamwidth selection, and benchmark composition bound transfer; reported ASR gains do not establish universal spatial hearing quality.

#### FlowSE: Efficient and High-Quality Speech Enhancement via Flow Matching

**Why this belongs:** The preserved abstract identifies a speech object and bounded intervention that instantiate speech-prior-denoising under noise-enhancement; this upgrades a provisional candidate to analyst-reviewed taxonomy membership only.

**Mechanism:** A neural velocity field maps a noisy waveform toward the clean distribution; consistency of the trajectory permits few-step integration while spectral and waveform losses preserve detail.

**Mathematical/evaluation object:** Flow matching replaces repeated stochastic denoising with an ODE-like path whose learned vector field can be sampled in fewer evaluations.

**Reported evidence:** The paper reports improved enhancement quality against generative baselines in both its evaluated scenarios with lower inference cost.

**Limit:** Training data, noise conditions, step count, real-time hardware, perceptual metrics, and speaker preservation tests bound the claim; enhancement scores do not establish conversational benefit.

#### Online Audio-Visual Autoregressive Speaker Extraction

**Why this belongs:** The title and preserved abstract identify a speech object and bounded intervention that instantiate target-conditioned-separation under source-separation-and-spatial-listening; this resolves taxonomy membership only.

**Mechanism:** Visual embeddings select the target, while the recurrent acoustic path summarizes prior separated audio; the mask is updated causally under a compute budget.

**Mathematical/evaluation object:** Streaming separation is causal state estimation: the system must preserve target identity while updating its estimate from current visual and acoustic evidence.

**Reported evidence:** On LRS3, the paper reports competitive separation quality with about 0.1M visual parameters and 2.1 MACs/s, and evaluates switching attention.

**Limit:** LRS3 faces, switching schedule, audiovisual synchronization, causal latency, and separation metrics bound transfer; benchmark separation is not a full human-attention study.

#### Diffusion Buffer: Online Diffusion-based Speech Enhancement with Sub-Second Latency

**Why this belongs:** Streaming enhancement must suppress noise within a sub-second budget rather than wait for a complete recording.

**Mechanism:** The buffer defines a causal-to-delayed window; diffusion steps operate on that window and output frames once their future context is sufficient.

**Mathematical/evaluation object:** Latency becomes a tunable information budget: a larger buffer gives the score-based model more context while increasing input-output delay.

**Reported evidence:** The paper reports better results than standard diffusion baselines and GPU input-output latency around 0.3–1 seconds.

**Limit:** GPU/hardware assumptions, buffer size, noise mixtures, real-time scheduling, and perceptual metrics bound the result; a reported latency range is not a full conversational user study.

#### FlowTSE: Target Speaker Extraction with Flow Matching

**Why this belongs:** The title and preserved abstract identify a speech object and bounded intervention that instantiate target-conditioned-separation under source-separation-and-spatial-listening; this resolves taxonomy membership only.

**Mechanism:** A learned flow transports a noisy conditional distribution toward target speech; complex-STFT conditioning supplies phase information that mel features discard.

**Mathematical/evaluation object:** Target extraction is conditional generation under an identity constraint, with magnitude and phase treated as complementary evidence.

**Reported evidence:** The paper reports that FlowTSE matches or outperforms strong target-speaker-extraction baselines on standard benchmarks.

**Limit:** Enrollment quality, speaker/noise shift, phase-vocoder design, benchmark mixtures, and signal metrics bound transfer; extraction quality is not automatically improved ASR or hearing-aid benefit.

#### Multitalker Babble in English Vowel Perception Training: A Comparison between Humans and Neural Models

**Why this belongs:** The captured official PDF and abstract identify a speech object and mechanism instantiating speech-prior-denoising under noise-enhancement; this upgrades evidence depth for the structured note and does not establish independent reproduction.

**Mechanism:** Babble context is manipulated and perceptual/model error patterns are compared.

**Mathematical/evaluation object:** The relevant object is the speech-prior-denoising evidence described by the paper's mechanism: Babble context is manipulated and perceptual/model error patterns are compared.

**Reported evidence:** The paper reports a comparison of human and neural-model responses in multitalker babble.

**Limit:** Listeners, babble construction, vowel contrasts, training duration, and model architecture bound transfer.

#### Neural Speech Extraction with Human Feedback

**Why this belongs:** The captured official PDF and abstract identify a speech object and mechanism instantiating target-conditioned-separation under source-separation-and-spatial-listening; this upgrades evidence depth for the structured note and does not establish independent reproduction.

**Mechanism:** Human preference supplies a target-selection signal alongside acoustic separation; the model is evaluated on extraction behavior.

**Mathematical/evaluation object:** Separation is not only signal recovery: the system must specify which source counts as useful to a listener.

**Reported evidence:** The paper reports neural speech extraction with human feedback.

**Limit:** Feedback population, mixture construction, target definition, signal metrics, and model scope bound transfer.

### Synthesis boundary

These papers share a conceptual pressure, but this seed batch does not justify ranking methods, estimating prevalence, or claiming that the mechanism generalizes across speakers, languages, rooms, or tasks. Those claims require additional assignments and comparable denominators.

## From sound to words and structured speech

**Ordinary pressure:** Speech has no visible spaces between words, and pronunciation, speed, accent, noise, and hesitation vary even when the intended sentence is the same.

**Naive strategy that breaks:** Matching each sound to a fixed dictionary pronunciation or treating the utterance as already segmented fails on coarticulation, new words, and disfluency.

**Recurring move:** Infer a sequence of linguistic units while allowing uncertainty about boundaries, pronunciation, context, and what should be preserved.

**Boundary:** A fluent transcript can be easier to read but less faithful to what was said, including omissions, hesitation, or uncertainty.

**D3 evidence status:** 55 reviewed paper(s); the family claim below is limited to these examples.

**Conceptual family represented:** `acoustic-unit-learning/acoustic-to-token`, `acoustic-unit-learning/self-supervised-speech-units`, `context-and-open-vocabulary/domain-and-context-biasing`, `boundaries-and-alignment/disfluency-preservation`, `context-and-open-vocabulary/domain-and-context-biasing`, `context-and-open-vocabulary/speaker-adaptation`, `context-and-open-vocabulary/speaker-adaptation`, `acoustic-unit-learning/self-supervised-speech-units`, `boundaries-and-alignment/alignment`, `context-and-open-vocabulary/domain-and-context-biasing`, `acoustic-unit-learning/self-supervised-speech-units`, `context-and-open-vocabulary/open-vocabulary-recognition`, `context-and-open-vocabulary/long-context-decoding`, `context-and-open-vocabulary/domain-and-context-biasing`, `boundaries-and-alignment/alignment`, `pronunciation-and-variation/pronunciation-variation`, `boundaries-and-alignment/disfluency-preservation`, `pronunciation-and-variation/pronunciation-variation`, `context-and-open-vocabulary/domain-and-context-biasing`, `boundaries-and-alignment/alignment`, `acoustic-unit-learning/acoustic-to-token`, `context-and-open-vocabulary/domain-and-context-biasing`, `boundaries-and-alignment/alignment`, `pronunciation-and-variation/pronunciation-variation`, `context-and-open-vocabulary/domain-and-context-biasing`, `acoustic-unit-learning/self-supervised-speech-units`, `acoustic-unit-learning/acoustic-to-token`, `acoustic-unit-learning/acoustic-to-token`, `acoustic-unit-learning/self-supervised-speech-units`, `acoustic-unit-learning/self-supervised-speech-units`, `context-and-open-vocabulary/long-context-decoding`, `boundaries-and-alignment/alignment`, `boundaries-and-alignment/alignment`, `context-and-open-vocabulary/long-context-decoding`, `boundaries-and-alignment/alignment`, `context-and-open-vocabulary/open-vocabulary-recognition`, `context-and-open-vocabulary/domain-and-context-biasing`, `context-and-open-vocabulary/domain-and-context-biasing`, `boundaries-and-alignment/alignment`, `pronunciation-and-variation/pronunciation-variation`, `acoustic-unit-learning/acoustic-to-token`, `acoustic-unit-learning/self-supervised-speech-units`, `acoustic-unit-learning/acoustic-to-token`, `context-and-open-vocabulary/open-vocabulary-recognition`, `boundaries-and-alignment/alignment`, `context-and-open-vocabulary/open-vocabulary-recognition`, `boundaries-and-alignment/disfluency-preservation`, `context-and-open-vocabulary/speaker-adaptation`, `context-and-open-vocabulary/long-context-decoding`, `context-and-open-vocabulary/speaker-adaptation`, `boundaries-and-alignment/disfluency-preservation`, `context-and-open-vocabulary/domain-and-context-biasing`, `context-and-open-vocabulary/long-context-decoding`, `acoustic-unit-learning/acoustic-to-token`, `pronunciation-and-variation/pronunciation-variation`.

### What the papers make concrete

#### Bridging ASR and LLMs for Dysarthric Speech Recognition: Benchmarking Self-Supervised and Generative Approaches

**Why this belongs:** The central comparison is how acoustic encoders and language-aware decoders map dysarthric speech to words; the clinical population is an important boundary, not the main mechanism.

**Mechanism:** The comparison keeps TORGO and UASpeech speaker-independent splits and evaluates WER by dysarthria severity. The decoder choice changes how much linguistic context can repair uncertain acoustic evidence.

**Mathematical/evaluation object:** The paper exposes an evidence trade-off: a stronger language prior can improve semantic reconstruction, but it can also make a plausible transcript less directly grounded in the signal.

**Reported evidence:** Whisper improves over CTC baselines, and Whisper-Vicuna reports the lowest WER in the tested TORGO and UASpeech comparisons; all results remain author-reported.

**Limit:** Dataset splits, severity labels, model scale, decoding prompts, and WER limit the claim; lower WER does not prove faithful preservation of disfluencies or speaker intent.

#### ashihara25_interspeech

**Why this belongs:** The paper studies what discrete audio tokens preserve and how token predictability changes across domains; it is a representation question, not a claim of universal semantic units.

**Mechanism:** The study measures statistical structure and predictability of token sequences, then compares domain-specific codeword usage.

**Mathematical/evaluation object:** Rank-frequency distributions describe how often codes occur; perplexity measures uncertainty of the next token. Similar predictability does not imply identical meaning.

**Reported evidence:** The paper reports similar statistical/predictable sequence patterns across domains but domain-dependent token usage.

**Limit:** The analysis supports representation observations, not a universal optimal token design or downstream task improvement.

#### agrawal25b_interspeech

**Why this belongs:** The method finds bias phrases in cross-attention and merges them with ASR output, using task context to resolve otherwise difficult terms.

**Mechanism:** Attention weights identify likely bias phrases; the method combines those candidates with the base transcription and uses an auxiliary attention loss.

**Mathematical/evaluation object:** WER measures word errors; OOV F1 measures detection of unseen terms. LoRA changes a small parameter subset rather than the whole recognizer.

**Reported evidence:** The paper reports a 1.0% absolute WER reduction on LibriSpeech and improved OOV recognition on in-house contact-center data.

**Limit:** The in-house data are not independently available in this atlas, and future multilingual/low-resource extension remains open.

#### akinrintoyo25_interspeech

**Why this belongs:** The explicit filler-inclusion analysis makes preservation of disfluencies part of the target rather than treating them as transcription noise; the dementia population is the evaluation boundary.

**Mechanism:** Shorter training clips adapt the model to fragmented speech; transcripts are scored for word errors and filler detection.

**Mathematical/evaluation object:** WER measures transcription errors while FIR/F1 measure whether clinically relevant fillers are retained and detected.

**Reported evidence:** The paper reports a medium model WER of 0.24 and stronger results than off-the-shelf models in its evaluation.

**Limit:** The dataset is 11.39 hours, some audio is mumbled or unintelligible, and diagnostic or clinical benefit is not established by ASR scores alone.

#### CMT-LLM: Contextual Multi-Talker ASR Utilizing Large Language Models

**Why this belongs:** The paper jointly handles speaker-overlap transcription and rare-word contextual biasing; the relevant concept is resolving acoustic and lexical uncertainty together.

**Mechanism:** A speech encoder produces frame representations, convolution downsamples them, a projector matches the LLM hidden size, and an LLM emits text separated by speaker-change tokens. A first decoding pass supplies evidence for a two-stage filter that selects rare words from a list of up to 1,000 before a second pass.

**Mathematical/evaluation object:** The system minimizes token cross-entropy on serialized transcripts. WER is computed on LibriMix and AMI single-device microphone data under different bias-list sizes; the central decision is which context terms enter the decoder, not a new acoustic metric.

**Reported evidence:** The paper reports WER of 7.9% on LibriMix and 32.9% on AMI SDM at biasing size 1,000, outperforming compared contextual-biasing approaches in its reported settings.

**Limit:** FIFO serialization imposes an ordering convention; the bias list and first-pass filter supply information that may not exist in every deployment. WER does not separately reveal speaker attribution, rare-word recall, or hallucination cost, and results were not independently reproduced.

#### Robust fine-tuning of speech recognition models via model merging: application to disordered speech

**Why this belongs:** Weight merging uses multiple fine-tuning solutions to stabilize recognition of disordered speech under speaker and data variation.

**Mechanism:** The study fine-tunes Whisper on the SAP dysarthric-speech data. MAST averages checkpoints along one trajectory, MAcT averages models from different hyperparameter trajectories, and SMAcT scans candidate models and retains those that improve the merged ensemble. The procedure is also tested with 1-hour, 10-hour, and full training subsets.

**Mathematical/evaluation object:** For corresponding parameters, merging uses an arithmetic mean. SMAcT accepts model Mi when WER(E union Mi) is lower than the current WER. On the full set, fine-tuning gives WER 15.0, MAST 13.4, MAcT 13.9, and SMAcT 13.6; in the 1-hour setting SMAcT reduces WER from 21.2 to 19.0.

**Reported evidence:** The paper reports gains for long utterances and low-data settings, including a 7.6% relative reduction from 18.5 to 17.1 WER with 10 hours of data; smaller Base and Turbo models improve too, but less consistently than Large.

**Limit:** The SAP data, Whisper family, selected development subset, and merging order determine the result. The selective procedure uses WER on a development subset and may itself be selection-sensitive; no independent reproduction was performed.

#### Continuous Learning for Children's ASR: Overcoming Catastrophic Forgetting with Elastic Weight Consolidation and Synaptic Intelligence

**Why this belongs:** Importance-weighted continual learning protects earlier child-speech mappings while adapting to sequential speakers.

**Mechanism:** Whisper-small trains on ten sequential MyST batches. EWC adds an importance-weighted quadratic penalty; SI accumulates importance from parameter movement and loss reduction; models use no selection, rolling-window, or best-so-far selection.

**Mathematical/evaluation object:** MyST has 145.54 training hours, 23.09 development hours, and 25.05 test hours. EWC and SI report relative WER reductions of 5.21% and 4.36% against sequential fine-tuning; bootstrap intervals quantify uncertainty.

**Reported evidence:** EWC and SI keep WER more stable across ten batches and improve over ordinary sequential fine-tuning under the protocol.

**Limit:** The protocol is simulated from MyST, uses English child speech and Whisper-small, and treats parameter importance as a proxy rather than a privacy guarantee.

#### HuBERT-VIC: Improving Noise-Robust Automatic Speech Recognition of Speech Foundation Model via Variance-Invariance-Covariance Regularization

**Why this belongs:** VICReg constraints make noisy speech representations retain useful acoustic units before recognition.

**Mechanism:** HuBERT-VIC applies VICReg terms to noisy representations and compares masked prediction with regularizer ablations on MUSAN-noised LibriSpeech.

**Mathematical/evaluation object:** The reported target is WER; relative gains are 23.3% on test-clean and 13.2% on test-other against the noisy-pretrained baseline.

**Reported evidence:** All three regularizers give the best reported WER and show complementary ablation effects.

**Limit:** MUSAN, SNR choices, HuBERT, and LibriSpeech bound the result; real conversational noise is not established.

#### Towards Multi-Level Transcript Segmentation: LoRA Fine-Tuning for Table-of-Contents Generation

**Why this belongs:** Hierarchical transcript segmentation treats topic boundaries as nested sequence structure rather than flat cuts.

**Mechanism:** TOC-NEMO uses LoRA fine-tuning and optional pause cues on AMI, VideoAula, and LectureDE; zero-shot prompting and supervised baselines provide comparisons.

**Mathematical/evaluation object:** Linear F1/B and hierarchical B distinguish flat boundary quality from agreement across levels; bootstrap and leave-one-speaker-out averages are reported.

**Reported evidence:** Fine-tuned TOC-NEMO plus pause cues reports the strongest linear scores, including AMI F1 30.34/B 24.81 and VideoAula F1 67.34/B 55.18.

**Limit:** Datasets, prompts, annotations, and metric behavior constrain the result; transcript segmentation is not proof of human topic understanding.

#### Domain Adaptation Method and Modality Gap Impact in Audio-Text Models for Prototypical Sound Classification

**Why this belongs:** Audio-side adaptation tests whether an audio-text representation preserves open-vocabulary labels across acoustic domains.

**Mechanism:** The method aligns audio representations to the target domain and compares audio-based with text-based adaptation.

**Mathematical/evaluation object:** Top-1 accuracy across environments and SNRs measures whether adaptation closes the modality/domain gap; the zero-shot reference is 32.4%.

**Reported evidence:** Audio-based adaptation gives the largest reported gains across tested conditions.

**Limit:** Sound set, target examples, class construction, and reported accuracy limit open-world claims.

#### What do self-supervised speech models know about Dutch?  Analyzing advantages of language-specific pre-training

**Why this belongs:** Language-specific self-supervised representations are tested by linguistic probes and downstream recognition across speech styles.

**Mechanism:** Hidden layers are probed for phonetic and lexical structure, then models are fine-tuned and evaluated on five Dutch test sets.

**Mathematical/evaluation object:** The Dutch model WERs are 10.4 CGN-o, 65.6 IFADV, 15.4 MLS, 21.0 CV, and 25.2 N-Best; English is consistently worse.

**Reported evidence:** Language-specific pretraining yields lower WER, while probe and fine-tuning rankings need not coincide.

**Limit:** Models, Dutch corpora, probes, and fine-tuning limit generalization; decodability is not causal proof of ASR behavior.

#### Fully End-to-end Streaming Open-vocabulary Keyword Spotting with W-CTC Forced Alignment

**Why this belongs:** Open-vocabulary spotting integrates word alignment into end-to-end streaming recognition instead of relying on fixed keyword lists.

**Mechanism:** CTC paths supply word-span alignment while the text encoder and verifier are trained in the same pipeline.

**Mathematical/evaluation object:** CTC alignment links acoustic frames to text; keyword audio-text similarity then scores arbitrary words.

**Reported evidence:** The paper reports superior performance on the Libriphrase hard set.

**Limit:** Benchmark, language, and author-reported result limit generalization and independent reproducibility.

#### Dynamic Context-Aware Streaming Pretrained Language Model For Inverse Text Normalization

**Why this belongs:** Streaming inverse text normalization makes the recognition-to-written-text boundary explicit under limited context and latency.

**Mechanism:** The model changes its available context as speech arrives, using right-context information without abandoning the streaming budget.

**Mathematical/evaluation object:** Sequence decoding maps spoken-form tokens to written-form tokens; latency and accuracy form the deployment tradeoff.

**Reported evidence:** The paper reports accuracy comparable to non-streaming ITN and better than prior streaming models on Vietnamese data while maintaining low latency.

**Limit:** Vietnamese data, benchmark, and author-reported latency/results limit cross-language and independent deployment claims.

#### NGPU-LM: GPU-Accelerated N-Gram Language Model for Context-Biasing in Greedy ASR Decoding

**Why this belongs:** The captured paper's ordinary problem, mechanism, and reported evaluation directly instantiate domain-and-context-biasing within adaptation-and-open-vocabulary.

**Mechanism:** NGPU-LM uses hash-based transition lookup and customizable greedy decoding so context biasing can recover domain words with less than 7% reported overhead.

**Mathematical/evaluation object:** The conceptual trade is between linguistic context and decoding latency; data structure and hardware choices move that boundary without changing the acoustic model.

**Reported evidence:** The paper reports recovery of more than half the greedy/beam accuracy gap in out-of-domain tests and up to 10.6% relative WER improvement in its experiments.

**Limit:** The results depend on tested ASR architectures, domains, GPU implementation, and author-reported measurements; deployment energy and other hardware remain open.

#### ASR-based segmentation for the analysis of larger child-speech datasets: Performance evaluation on vowels from Australian-English speaking children aged 4 to 11 years

**Why this belongs:** The captured paper's ordinary problem, mechanism, and reported evaluation directly instantiate alignment within boundaries-and-sequence-structure.

**Mechanism:** The study evaluates vowel boundaries in Australian-English child speech and asks how alignment error changes from ages four to eleven.

**Mathematical/evaluation object:** The conceptual issue is not simply alignment accuracy: a boundary is an analytic decision whose meaning must be shared by the tool and the human measurement protocol.

**Reported evidence:** The paper reports that MFA falls short of human annotation, with smaller discrepancies for older children.

**Limit:** The evidence is tied to the tested vowels, ages, language variety, and annotators; it supports semi-automatic caution rather than universal aligner failure.

#### Mixture of LoRA Experts for Low-Resourced Multi-Accent Automatic Speech Recognition

**Why this belongs:** Multi-accent ASR must share useful structure while retaining pronunciation differences that a single dominant accent would call errors.

**Mechanism:** MAS-LoRA attaches low-rank adapters specialized to accents to Whisper and evaluates known- and unknown-accent routing on L2-ARCTIC.

**Mathematical/evaluation object:** Word error rate measures recognition; comparisons include ordinary LoRA, full fine-tuning, and forgetting after adaptation.

**Reported evidence:** The paper reports lower WER than those baselines, stronger gains when the accent is known, and less catastrophic forgetting.

**Limit:** The result is tied to L2-ARCTIC, its accent set, Whisper, and routing assumptions; spontaneous speech and accents outside the corpus remain open.

#### StutterCut: Uncertainty-Guided Normalised Cut for Dysfluency Segmentation

**Why this belongs:** Dysfluency segmentation must locate irregular speech events without treating repetitions and disruptions as disposable recognition errors.

**Mechanism:** Speech embeddings form graph nodes, similarity edges are adjusted by a classifier, and Monte Carlo dropout controls how strongly uncertain predictions affect the partition.

**Mathematical/evaluation object:** Graph partitioning converts local acoustic similarity into event boundaries, while uncertainty limits the influence of labels least supported by the weak supervision.

**Reported evidence:** StutterCut reports better F1 and more precise stuttering-onset detection on real and synthetic data, and the extended FluencyBank boundaries make the evaluation less dependent on synthetic events.

**Limit:** Dysfluency types, annotation quality, speaker population, synthetic-real mismatch, and feedback protocol constrain the claim; segmentation accuracy is not demonstrated therapy benefit.

#### CHSER: A Dataset and Case Study on Generative Speech Error Correction for Child ASR

**Why this belongs:** Generative speech-error correction for child ASR treats unusual pronunciations as a structured correction problem rather than simply deleting uncertain words.

**Mechanism:** CHSER contains 200K pairs across ages and speaking styles; fine-tuned generative correction is tested in zero-shot and ASR-fine-tuned settings.

**Mathematical/evaluation object:** Word error rate measures overall correction, while substitution, deletion, insertion, and disfluency analysis show which errors are changed.

**Reported evidence:** The paper reports up to 28.5% relative WER reduction zero-shot and 13.3% after ASR fine-tuning, but insertions and child disfluencies remain difficult.

**Limit:** The corpus, languages, ASR hypotheses, and correction model bound the result; preserving clinically meaningful disfluencies outside these settings remains open.

#### Effect of Loudspeaker Emitted Speech on ASR performance

**Why this belongs:** Loudspeaker-emitted speech tests whether ASR mistakes playback and acoustic feedback for a person speaking directly to the system.

**Mechanism:** The paper studies ASR performance for loudspeaker-emitted speech and compares recognition across the tested playback conditions.

**Mathematical/evaluation object:** Word error rate exposes the channel penalty; the useful distinction is speech content versus the acoustic path that carries it.

**Reported evidence:** The paper reports a measurable ASR impact from loudspeaker emission under its experimental conditions.

**Limit:** The result is bounded to the loudspeaker, room, microphones, and ASR systems tested; other devices and adaptive compensation remain open.

#### A semi-automatic pipeline for transcribing and segmenting child speech

**Why this belongs:** Transcribing and segmenting child speech requires interaction-aware boundaries because pauses, turn changes, and immature articulation do not follow adult assumptions.

**Mechanism:** WhisperX supplies a transcription, manual correction changes the lexical scaffold, and MFA places segment boundaries; adaptation changes the acoustic model used for alignment.

**Mathematical/evaluation object:** The pipeline separates lexical uncertainty from boundary uncertainty: a better transcript and a better acoustic model affect the measured vowel interval through different paths.

**Reported evidence:** Manual transcript correction improves acoustic vowel measures, and adaptation of the pretrained MFA model helps, while merely increasing the adaptation sample does not add the same improvement.

**Limit:** The 275-child Scottish-English field corpus, manual reference quality, recording conditions, and selected vowel measures bound transfer; alignment quality is not a complete child-speech recognizer evaluation.

#### DC-Spin: A Speaker-invariant Speech Tokenizer for Spoken Language Models

**Why this belongs:** A speaker-invariant speech tokenizer tries to discard identity variation while retaining units useful to a spoken-language model.

**Mechanism:** SpinHuBERT supplies the speech representation and DC-Spin separates speaker-invariant and phonetic information into codebooks; the tokens are tested in zero-shot spoken-language tasks and resynthesis.

**Mathematical/evaluation object:** Clustering assigns nearby representation vectors to discrete symbols; speaker-invariance changes the training objective so distance caused by identity matters less than distance caused by phonetic content.

**Reported evidence:** The paper reports that tokens with phoneme alignment or simple language-model structure are useful downstream and improve the tested zero-shot and resynthesis proxies.

**Limit:** The tokenizers, languages, proxy tasks, and resynthesis setup bound the result; token usefulness is not the same as complete spoken meaning.

#### BR-ASR: Efficient and Scalable Bias Retrieval Framework for Contextual Biasing ASR in Speech LLM

**Why this belongs:** Contextual biasing supplies rare words to an ASR language model without letting a small requested list overwhelm ordinary recognition.

**Mechanism:** Speech-and-bias contrastive learning ranks relevant entries; a dynamic curriculum trains the system on increasingly difficult homophones; pruning then supplies a compact list to the ASR decoder.

**Mathematical/evaluation object:** Contrastive learning pulls matching speech/list pairs together and pushes distractors apart; retrieval converts a huge candidate set into a small conditional search problem.

**Reported evidence:** The paper reports 2.8%/7.1% biased WER with 2,000 words, only 0.3/2.9% absolute degradation at 200,000 entries, 99.99% pruning, and 20 ms query latency on the tested split.

**Limit:** The reported latency, languages, bias lists, and ASR systems define the boundary; rare names outside the retrieval distribution and interactive user correction remain open.

#### The Multimodal Information Based Speech Processing (MISP) 2025 Challenge: Audio-Visual Diarization and Recognition

**Why this belongs:** Audio-visual diarization and recognition must align who spoke, when they spoke, and what was said in multi-person recordings.

**Mechanism:** MISP 2025 defines AVSD, AVSR, and AVDR tasks with multi-device meeting data; systems combine acoustic and visual streams and are scored on speaker attribution and transcription.

**Mathematical/evaluation object:** Diarization error counts missed, false, and incorrectly attributed speech; character error measures transcript edits; concatenated minimum-permutation error resolves arbitrary speaker-label names.

**Reported evidence:** The challenge reports DER 8.09%, CER 9.48%, and cpCER 11.56% for its top systems, with the largest gain in the joint task.

**Limit:** Challenge data, camera placement, meeting types, language, and leaderboard protocols define the claim; deployment in unseen rooms or privacy-constrained camera settings remains open.

#### SardinianVoxes: A Speech Recognition Dataset for the Sardinian Languages

**Why this belongs:** A Sardinian speech-recognition corpus addresses the mapping problem when language varieties are fragmented and resources scarce.

**Mechanism:** SardinianVoxes contains about 170 hours of transcribed speech, and the paper defines a benchmark for state-of-the-art and fine-tuned speech-to-text models.

**Mathematical/evaluation object:** A corpus is a measurement object: coverage, transcription, variety labels, and split design determine what an error rate means.

**Reported evidence:** The paper contributes a public resource and evaluation protocol intended to make Sardinian speech technology measurable.

**Limit:** The reported resource, varieties, transcription quality, and benchmark models bound the claim; future collection and independent use are still needed.

#### Ranking and Selection of Bias Words for Contextual Bias Speech Recognition

**Why this belongs:** Contextual ASR must rank a large bias list so relevant names and terms do not compete equally for recognition.

**Mechanism:** A bias-word ranking network selects candidates from the IS21 list and evaluates contextual Whisper on LibriSpeech.

**Mathematical/evaluation object:** Selection turns a huge candidate set into a focused conditional recognition problem; biased WER measures the targeted words while overall WER checks collateral damage.

**Reported evidence:** The paper reports more than 40% relative reduction in biased WER from ranking and selection.

**Limit:** NER list, LibriSpeech, Whisper context mechanism, and bias-word definition bound the result; new domains and errors in entity extraction remain open.

#### EnCodecMAE: leveraging neural codecs for universal audio representation learning

**Why this belongs:** The official full paper identifies a human spoken-speech object and a bounded research problem that instantiate self-supervised-speech-units under acoustic-unit-mapping; this resolves taxonomy membership, not the paper's scientific validity.

**Mechanism:** EnCodecMAE is pretrained on diverse audio and evaluated on pitch, genre, speech commands, emotion, sound events, and environmental sound tasks.

**Mathematical/evaluation object:** Transfer performance is the test of usefulness; the representation is judged by how task, input, model size, and pretraining diversity change downstream accuracy or error.

**Reported evidence:** The paper reports average gains over prior audio representations and finds that larger models, task-dependent inputs, self-training, and diverse data each matter.

**Limit:** The task suite, pretraining mixture, labels, model comparisons, and aggregate averages bound the claim; average transfer does not prove universal suitability for speech.

#### Improving End-to-end Mixed-case ASR with Knowledge Distillation and Integration of Voice Activity Cues

**Why this belongs:** The official full paper identifies a human spoken-speech object and a bounded research problem that instantiate acoustic-to-token under acoustic-unit-mapping; this resolves taxonomy membership, not the paper's scientific validity.

**Mechanism:** A mixed-case end-to-end ASR student receives knowledge from a unicase teacher and voice-activity information; case-sensitive and insensitive outputs are measured.

**Mathematical/evaluation object:** The system separates acoustic-to-word evidence from formatting supervision; word error and case/punctuation errors expose whether formatting harms recognition.

**Reported evidence:** The method reports up to a 9.2% relative error reduction at comparable decoding cost.

**Limit:** Training data, formatting conventions, teacher quality, decoding budget, and reported error definitions bound the result; punctuation accuracy is not the same as transcript understanding.

#### From Weak Labels to Strong Results: Utilizing 5,000 Hours of Noisy Classroom Transcripts with Minimal Accurate Data

**Why this belongs:** Noisy classroom transcripts provide weak supervision; the central move is learning word mappings while separating unreliable labels from a small accurate set.

**Mechanism:** Weakly Supervised Pretraining uses 5,000 hours of noisy classroom transcripts followed by fine-tuning on a small accurate set; synthetic and real weak transcripts are compared.

**Mathematical/evaluation object:** The two-stage schedule separates learning broad acoustic-to-token regularities from calibrating the final transcript against trusted labels.

**Reported evidence:** The paper reports that WSP outperforms alternative strategies in synthetic and real weak-label settings for classroom ASR.

**Limit:** Classroom domain, weak-label generation, gold-data size, transcript quality, and WER protocol bound the result; weak supervision can still reproduce systematic omissions or speaker bias.

#### Word stress in self-supervised speech models: A cross-linguistic comparison

**Why this belongs:** Cross-linguistic stress probing tests what a self-supervised representation preserves about prominence rather than assuming learned units have the same linguistic meaning everywhere.

**Mechanism:** Wav2vec 2.0 embeddings are probed for stressed versus unstressed syllables in Dutch, English, German, Hungarian, and Polish.

**Mathematical/evaluation object:** A diagnostic classifier tests recoverable information while cross-language comparison asks whether the representation reflects variable versus fixed or demarcative stress systems.

**Reported evidence:** Stress is decoded with high accuracy, and the representations show language-specific differences, with a larger contrast between variable-stress and fixed-stress languages.

**Limit:** Read-aloud sentences, languages, layer choices, probe capacity, and diagnostic accuracy bound the inference; recoverable information is not proof that the model uses stress causally.

#### DiceHuBERT: Distilling HuBERT with a Self-Supervised Learning Objective

**Why this belongs:** Distilling HuBERT asks which learned speech units can remain useful after a larger self-supervised model is made smaller.

**Mechanism:** DiceHuBERT distills HuBERT using the same self-supervised objective and evaluates the compact model on phoneme recognition, ASR, and SUPERB tasks.

**Mathematical/evaluation object:** The student learns the task's predictive structure instead of matching every hidden layer; downstream performance measures retained usefulness across tasks.

**Reported evidence:** The paper reports over 21% improvement in phoneme recognition and over 14% in ASR relative to existing distillation methods, with competitive multi-task results.

**Limit:** Teacher/student sizes, SUPERB tasks, training data, and comparison baselines bound the result; benchmark transfer does not establish equal behavior under every deployment constraint.

#### Bidirectional Spoken-Written Text Conversion with Large Language Models

**Why this belongs:** Spoken and written forms require a controlled conversion boundary after recognition; the paper addresses that normalization step.

**Mechanism:** The model learns mappings in both directions; generated paired text supplies supervision while iterative learning enlarges the conversion data.

**Mathematical/evaluation object:** The central object is a representation boundary between spoken language and written conventions, not a change to the acoustic evidence itself.

**Reported evidence:** The paper reports a 13.4% ERR improvement in the evaluated conversion setting.

**Limit:** LLM generation quality, language conventions, error metric, transcript domain, and iterative-label bias bound transfer; normalization success is not ASR acoustic accuracy.

#### SiamCTC:  Learning Speech Representations through Monotonic Temporal Alignment

**Why this belongs:** Monotonic alignment tests whether speech representations can preserve the order between an acoustic event and the label or content it expresses.

**Mechanism:** Two encoders produce sequences and CTC sums over valid monotonic paths while training the representations to agree at content level.

**Mathematical/evaluation object:** A monotonic path preserves temporal order while allowing variable durations; it is a soft alignment over possible boundaries.

**Reported evidence:** SiamCTC improves representation robustness at diverse speaking rates in the reported experiments.

**Limit:** Augmentation, language, CTC targets, downstream tasks, and rate range bound transfer; robustness is not universal recognition accuracy.

#### Word Level Timestamp Generation for Automatic Speech Recognition and Translation

**Why this belongs:** Word timestamps make the time boundary of each recognized unit explicit for retrieval and subtitles.

**Mechanism:** Teacher-generated word intervals become sequence targets; the model's timestamp tokens interleave with recognized or translated content, allowing boundary prediction inside the decoder.

**Mathematical/evaluation object:** Alignment quality is measured against teacher or reference timing and downstream recognition/translation behavior, testing whether an integrated decoder can replace a separate alignment stage.

**Reported evidence:** The paper reports word-level timestamp generation for Canary with the proposed token and teacher-supervised training in the evaluated ASR/translation settings.

**Limit:** Teacher timing quality, tokenization, language, speaking rate, and evaluation alignment constrain transfer; timestamp agreement does not by itself prove subtitle readability or translation quality.

#### Exploring SSL Discrete Speech Features for Zipformer-based Contextual ASR

**Why this belongs:** Contextual ASR tests whether preceding, current, and future utterances improve the mapping from sound to words.

**Mechanism:** The study evaluates contextual Z-T systems on 1,000-hour GigaSpeech-M and DementiaBank Pitt elderly speech, using SSL discrete tokens, WavLM features, and preceding/current/future context variants.

**Mathematical/evaluation object:** Context is a sequence decision: the representation must preserve the distinctions useful for the next utterance while reducing the number of values passed to the recognizer; WER and training time expose the tradeoff.

**Reported evidence:** Discrete-token contextual systems reduce WER by 0.39 and 1.41 absolute points on the two tasks and achieve up to 4.36x training speedup over continuous WavLM context systems.

**Limit:** Corpora, context windows, tokenization, speed hardware, and statistical test bound the result; better contextual WER does not prove robust dialogue understanding or causal use of future context in deployment.

#### Transcript-Prompted Whisper with Dictionary-Enhanced Decoding for Japanese Speech Annotation

**Why this belongs:** Transcript prompts and dictionary knowledge align acoustic evidence with phonemic and prosodic annotation.

**Mechanism:** Transcript-Prompted Whisper fine-tunes a large ASR model for simultaneous phrase and annotation output and applies a dictionary-based correction stage for Japanese speech-data construction.

**Mathematical/evaluation object:** The transcript acts as a constraint on what was said while the audio supplies pronunciation and prosody; joint sequence output makes boundaries and labels part of one decoding problem.

**Reported evidence:** The paper reports improved phonemic/prosodic annotation behavior and a practical pipeline for constructing Japanese TTS data from audio-transcript pairs.

**Limit:** Ground-truth transcript quality, dictionary coverage, Japanese phonology, label definitions, and annotation evaluation bound the result; automatic labels still require quality control before becoming training truth.

#### Efficient Trie-based Biasing using K-step Prediction for Rare Word Recognition

**Why this belongs:** The preserved abstract identifies a speech object and bounded intervention that instantiate open-vocabulary-recognition under adaptation-and-open-vocabulary; this upgrades a provisional candidate to analyst-reviewed taxonomy membership only.

**Mechanism:** The decoder predicts future steps from a prefix; synthetic data fine-tunes Whisper so contextual biasing becomes learned look-ahead.

**Mathematical/evaluation object:** The method replaces delayed correction with an approximate future-value estimate, trading learned prediction for simpler decoding.

**Reported evidence:** On NSC Part 2, reported WER falls from 30.86% to 12.19% after 10 hours of synthetic-data fine-tuning.

**Limit:** Synthetic realism, rare-word list, decoder, beam settings, and WER denominator bound the claim.

#### GLCLAP: A Novel Contrastive Learning Pre-trained Model for Contextual Biasing in ASR

**Why this belongs:** The preserved abstract identifies a speech object and bounded intervention that instantiate domain-and-context-biasing under adaptation-and-open-vocabulary; this upgrades a provisional candidate to analyst-reviewed taxonomy membership only.

**Mechanism:** GLCLAP learns global and local audio-text relations for contextual biasing, retrieving matched entities from a user-specified list before the ASR decoder uses them.

**Mathematical/evaluation object:** Contrastive learning makes matched audio/text pairs close and mismatched pairs distant; global context narrows meaning while local segments identify the exact rare word, and retrieval accuracy precedes WER.

**Reported evidence:** The paper reports a marked improvement in bias-word retrieval accuracy and downstream contextual ASR performance over sentence-level contrastive approaches.

**Limit:** Entity list, prompt quality, language, negative sampling, retrieval threshold, and ASR decoder bound the result; a better retrieved list cannot correct an incorrect user prompt or guarantee unbiased ordinary decoding.

#### Improving Synthetic Data Training for Contextual Biasing Models with a Keyword-Aware Cost Function

**Why this belongs:** The preserved abstract identifies a speech object and bounded intervention that instantiate domain-and-context-biasing under adaptation-and-open-vocabulary; this upgrades a provisional candidate to analyst-reviewed taxonomy membership only.

**Mechanism:** The paper improves synthetic-data training for contextual biasing with a keyword-aware cost function.

**Mathematical/evaluation object:** The training objective changes the data's influence according to the keyword-level error structure; the goal is targeted correction rather than blanket bias.

**Reported evidence:** The paper reports improved contextual-biasing performance for the proposed synthetic-data objective.

**Limit:** Keyword lists, synthetic-data quality, language, decoder, and evaluation distribution limit generalization; better keyword recall can still create false activations.

#### Song Form-aware Full-Song Text-to-Lyrics Generation with Multi-Level Granularity Syllable Count Control

**Why this belongs:** Song-form-aware lyrics generation must align syllable count and linguistic content with musical timing across a full song.

**Mechanism:** The paper proposes song-form-aware full-song lyrics generation with multi-level syllable control.

**Mathematical/evaluation object:** The output is a structured object: constraints at smaller units must compose into a song-level form, rather than being repaired after a generic text model has already committed to lines.

**Reported evidence:** The paper reports controlled lyrics-generation experiments and makes generated samples available for inspection.

**Limit:** Text prompts, song forms, syllable-count rules, dataset construction, and evaluation criteria bound the claim; syllable fit is not the same as singability, musicality, or authorship.

#### Using Neurogram Similarity Index Measure (NSIM) to Model Hearing Loss and Cochlear Neural Degeneration

**Why this belongs:** Neurogram similarity models how hearing loss changes the mapping from speech acoustics to neural responses and perceived units.

**Mechanism:** The paper evaluates NSIM as an objective measure of hearing loss and cochlear neural degeneration.

**Mathematical/evaluation object:** Hearing ability is a transformation from sound to neural patterns: comparing those patterns can expose losses that a simple input threshold misses, but the model remains an indirect proxy.

**Reported evidence:** The paper reports that NSIM maps phoneme-recognition performance and is sensitive to simulated degeneration, suggesting a candidate noninvasive biomarker.

**Limit:** Auditory-periphery model, task, simulations, participant data, and mapping assumptions bound clinical interpretation; a candidate biomarker is not a validated diagnosis.

#### Decoding Speaker-Normalized Pitch from EEG for Mandarin Perception

**Why this belongs:** Speaker-normalized pitch decoded from EEG tests whether perceptual speech information can be recovered from a non-acoustic signal.

**Mechanism:** The paper decodes speaker-normalized pitch from EEG during Mandarin perception.

**Mathematical/evaluation object:** Perception can preserve a relational variable: normalization removes the speaker’s baseline while retaining the contour relation that carries linguistic information.

**Reported evidence:** The proposed CE-ViViT approach achieved modest-error decoding, with speaker-normalized contours decoded more accurately than raw contours in the reported experiments.

**Limit:** Participants, Mandarin tones, EEG sessions, normalization rule, model, and modest-error metric bound the neural claim; better decoding does not by itself reveal the full perceptual code.

#### On-device Streaming Discrete Speech Units

**Why this belongs:** The paper makes discrete speech units streamable on-device by reducing full-context and extractor cost while preserving phonetic information.

**Mechanism:** The paper develops on-device streaming discrete speech units.

**Mathematical/evaluation object:** Streaming is a causal information constraint: the model must decide from the past available at each moment, so efficiency is not just compression but a change in what evidence can be used.

**Reported evidence:** On ML-SUPERB 1h, the paper reports a 50% FLOP reduction for a 6.5% relative CER increase.

**Limit:** Dataset size, causal window, unit clustering, hardware, FLOPs accounting, and CER bound practical generalization; the trade-off may change for other languages or latency targets.

#### Exploring auditory feedback mechanisms in speech recognition

**Why this belongs:** Auditory feedback mechanisms ask how a listener's own speech recognition system uses expected sound to interpret the incoming signal.

**Mechanism:** The paper explores auditory feedback mechanisms in speech recognition.

**Mathematical/evaluation object:** A speech front end can be both an engineering component and a biological experiment: a mechanism is interesting when it changes recognition in the direction predicted by auditory physiology.

**Reported evidence:** The paper reports that adding the larger feedback loop appears beneficial for ASR, while describing the current implications as modest.

**Limit:** Approximate oscillator model, compute limits, ASR task, feedback implementation, and modest gains bound interpretation; improved recognition does not validate the whole biological mechanism.

#### Adversarial Deep Metric Learning for Cross-Modal Audio-Text Alignment in Open-Vocabulary Keyword Spotting

**Why this belongs:** The title and preserved abstract identify a speech object and bounded intervention that instantiate open-vocabulary-recognition under adaptation-and-open-vocabulary; this resolves taxonomy membership only.

**Mechanism:** The encoders map acoustic queries and text enrollments into a shared space; the adversarial classifier penalizes recoverable modality identity while the metric objective pulls matched keyword pairs together.

**Mathematical/evaluation object:** The shared embedding is a constrained retrieval geometry: matched audio/text pairs should be close, while modality identity should be uninformative to the adversary.

**Reported evidence:** Modality-invariant alignment improves the audio-text retrieval decision used for unseen-keyword spotting in the reported experiments.

**Limit:** Vocabulary, languages, negative sampling, enrollment text, threshold calibration, and speaker/channel variation bound the claim; open-vocabulary benchmark accuracy is not unrestricted lexical understanding.

#### VoiceNet: Multilingual On-Device Phoneme-To-Audio Alignment

**Why this belongs:** The preserved abstract identifies a speech object and bounded intervention that instantiate alignment under boundaries-and-sequence-structure; this upgrades a provisional candidate to analyst-reviewed taxonomy membership only.

**Mechanism:** VoiceNet predicts phoneme evidence and timing on-device; text adds a constraint when available, and device tests expose latency.

**Mathematical/evaluation object:** Alignment is ordered interval inference rather than a post-processing attachment to recognition.

**Reported evidence:** The paper reports competitive multilingual alignment and 6 ms average CPU phoneme inference on Galaxy devices.

**Limit:** Device, language, phoneme inventory, transcript availability, and splits bound transfer; latency is not alignment quality.

#### Multilingual Query-by-Example KWS for Indian Languages using Transliteration

**Why this belongs:** The title and preserved abstract identify a speech object and bounded intervention that instantiate open-vocabulary-recognition under adaptation-and-open-vocabulary; this resolves taxonomy membership only.

**Mechanism:** The ASR maps ten languages to transliterated characters; posterior sequences become retrieval features.

**Mathematical/evaluation object:** Transliteration changes the shared unit from language-specific phonemes to a common script-level sequence representation.

**Reported evidence:** The method raises reported MTWV from 0.015 to 0.504 on IndicSUPERB and exceeds the Marathi baseline.

**Limit:** Language, script, ASR errors, query duration, and splits constrain transfer; script unification is not translation.

#### Who knows best? Effects of speech disfluencies on incentivized decision-making

**Why this belongs:** The title and preserved abstract identify a speech object and bounded intervention that instantiate disfluency-preservation under boundaries-and-sequence-structure; this resolves taxonomy membership only.

**Mechanism:** The experiment treats disfluency as part of the observed communication signal and measures choice behavior rather than only an attitude rating.

**Mathematical/evaluation object:** Behavioral choice is a downstream proxy: it tests whether a listener’s interpretation of fluency changes action under incentives.

**Reported evidence:** The study reports that listeners take speech fluency into account when deciding whom or what to believe.

**Limit:** Task stakes, speakers, disfluency types, online sample, and source-conflict design bound transfer; choice bias is not proof that disfluencies carry truthful information.

#### Theoretical proposal for a unified Bayesian model of adaptation in non-interactive and interactive speech production

**Why this belongs:** A unified Bayesian account asks how speakers adapt their production to a listener and how that differs between interactive and non-interactive speech.

**Mechanism:** COSMO-style latent variables connect production and perception; Bayesian updating changes beliefs about the speech system under feedback or interaction.

**Mathematical/evaluation object:** Adaptation is posterior inference under uncertain sensory evidence, not merely a speaker-specific parameter fine-tune.

**Reported evidence:** The proposal shows how both experimental paradigms can be described within one Bayesian framework.

**Limit:** This is a theoretical proposal, not an independent behavioral validation; parameterization, priors, and task fit remain open.

#### MOVER: Combining Multiple Meeting Recognition Systems

**Why this belongs:** The preserved abstract identifies a speech object and bounded intervention that instantiate long-context-decoding under boundaries-and-sequence-structure; this upgrades a provisional candidate to analyst-reviewed taxonomy membership only.

**Mechanism:** The method constructs correspondences between speaker-labeled time intervals before combining words and timings, preserving the meeting structure.

**Mathematical/evaluation object:** Combination is a structured matching problem over intervals, labels, and sequences rather than token-majority voting alone.

**Reported evidence:** MOVER reports successful combination on CHiME-8 DASR and NOTSOFAR-1 multi-channel tasks.

**Limit:** Task formats, diarization errors, interval alignment, system diversity, and scoring rules bound transfer; fusion gains do not prove every component is complementary.

#### Effects of Speaker Count, Duration, and Accent Diversity on Zero-Shot Accent Robustness in Low-Resource ASR

**Why this belongs:** Accent-robust ASR must adapt to speaker and accent variation without mistaking a small low-resource sample for a universal rule.

**Mechanism:** Controlled data-composition experiments compare ASR performance across unseen accents and languages.

**Mathematical/evaluation object:** Generalization is constrained by which speakers and accents supply the training evidence, not only by total audio hours.

**Reported evidence:** The paper reports that more speakers help more than more hours per speaker, while accent-diversity gains are minimal under controlled speaker count.

**Limit:** Languages, accent labels, low-resource budgets, model/training choices, and zero-shot evaluation bound transfer; this is not a universal data-collection law.

#### What the Filler? Both ASR Systems and Humans Struggle More With Other Kinds of Disfluencies Than With Filler Particles

**Why this belongs:** The preserved abstract identifies a speech object and bounded intervention that instantiate disfluency-preservation under boundaries-and-sequence-structure; this upgrades a provisional candidate to analyst-reviewed taxonomy membership only.

**Mechanism:** The matched transcription experiment uses participant recall and ASR WER to compare shared difficulty patterns.

**Mathematical/evaluation object:** Disfluency is sequence evidence: preserving its position and type lets recognition error be related to conversational structure.

**Reported evidence:** The paper reports similar difficulty characteristics for humans and ASR and no WER effect from filler presence alone.

**Limit:** 54 listeners, nine systems, utterance design, languages, and WER/recall definitions bound transfer; matched error patterns do not establish cognitive equivalence.

#### WCTC-Biasing: Retraining-free Contextual Biasing ASR with Wildcard CTC-based Keyword Spotting and Inter-layer Biasing

**Why this belongs:** The preserved abstract identifies a speech object and bounded intervention that instantiate domain-and-context-biasing under adaptation-and-open-vocabulary; this upgrades a provisional candidate to analyst-reviewed taxonomy membership only.

**Mechanism:** CTC keyword scores detect flexible keyword evidence; inter-layer bias signals steer decoding while retaining the base acoustic model.

**Mathematical/evaluation object:** Contextual biasing changes the prior over candidate words, so it must raise relevant rare words without overruling acoustic evidence.

**Reported evidence:** The paper reports retraining-free contextual recognition improvements using WCTC-Biasing.

**Limit:** Keyword lists, wildcard design, domains, decoder thresholds, and test distributions bound transfer; contextual gains do not guarantee lower errors on arbitrary speech.

#### Improving Cross-Attention based on Positional Alignment during Inference for Robust Long-form Speech Recognition

**Why this belongs:** The preserved abstract identifies a speech object and bounded intervention that instantiate long-context-decoding under boundaries-and-sequence-structure; this upgrades a provisional candidate to analyst-reviewed taxonomy membership only.

**Mechanism:** Position-aware attention reshapes the correspondence between decoder states and encoder frames without changing the recognized content target.

**Mathematical/evaluation object:** Long-context decoding is a soft alignment problem: context helps only when its evidence remains tied to the relevant time region.

**Reported evidence:** The paper reports improved robust long-form recognition from inference-time positional alignment.

**Limit:** Model, long-form segmentation, positional formulation, decoding settings, and evaluation corpora bound transfer; reported robustness is not universal streaming reliability.

#### Towards a Unified Benchmark for Arabic Pronunciation Assessment: Qur’anic Recitation as Case Study

**Why this belongs:** The captured official PDF and abstract identify a speech object and mechanism instantiating acoustic-to-token under acoustic-unit-mapping; this upgrades evidence depth for the structured note and does not establish independent reproduction.

**Mechanism:** Audio, pronunciation targets, and assessment labels are aligned for model comparison.

**Mathematical/evaluation object:** The relevant object is the acoustic-to-token evidence described by the paper's mechanism: Audio, pronunciation targets, and assessment labels are aligned for model comparison.

**Reported evidence:** The paper presents a benchmark and case study for Arabic pronunciation assessment.

**Limit:** Recitation tradition, annotation, coverage, and metrics bound transfer; automatic scores are not teacher judgment.

#### Improving Child Speech Recognition and Reading Mistake Detection by Using Prompts

**Why this belongs:** The captured official PDF and abstract identify a speech object and mechanism instantiating pronunciation-variation under acoustic-unit-mapping; this upgrades the structured note to D3 without establishing independent reproduction.

**Mechanism:** Prompt information narrows the hypothesis space: acoustic evidence is interpreted with task and expected linguistic content.

**Mathematical/evaluation object:** The paper treats pronunciation-variation as a structured evidence-to-decision problem: Prompt information narrows the hypothesis space: acoustic evidence is interpreted with task and expected linguistic content.

**Reported evidence:** The paper reports improving child speech recognition and reading-mistake detection using prompts.

**Limit:** Child age, language, prompt design, annotation policy, and error definitions bound transfer.

### Synthesis boundary

These papers share a conceptual pressure, but this seed batch does not justify ranking methods, estimating prevalence, or claiming that the mechanism generalizes across speakers, languages, rooms, or tasks. Those claims require additional assignments and comparable denominators.

## From spoken form to meaning and coordinated action

**Ordinary pressure:** The same words can request, question, joke, refuse, or warn depending on prosody, shared history, timing, and the surrounding situation.

**Naive strategy that breaks:** A transcript-only system treats words as the whole message and misses intent, reference, turn structure, and what is appropriate to do next.

**Recurring move:** Combine linguistic content with speaker, discourse history, prosody, visual or environmental context, and an explicit action or response target.

**Boundary:** More context can resolve ambiguity but can also leak private information, over-interpret the speaker, or make a system confidently act on a wrong inference.

**D3 evidence status:** 60 reviewed paper(s); the family claim below is limited to these examples.

**Conceptual family represented:** `intent-and-dialogue-state/intent-in-context`, `intent-and-dialogue-state/intent-in-context`, `intent-and-dialogue-state/dialogue-state`, `turn-taking-and-repair/turn-boundary`, `prosody-and-paralinguistics/prosodic-meaning`, `turn-taking-and-repair/turn-boundary`, `prosody-and-paralinguistics/paralinguistic-state`, `grounding-and-action/referential-grounding`, `grounding-and-action/interactional-feedback`, `prosody-and-paralinguistics/prosodic-meaning`, `turn-taking-and-repair/turn-boundary`, `grounding-and-action/referential-grounding`, `prosody-and-paralinguistics/paralinguistic-state`, `turn-taking-and-repair/turn-boundary`, `grounding-and-action/referential-grounding`, `prosody-and-paralinguistics/prosodic-meaning`, `turn-taking-and-repair/turn-boundary`, `grounding-and-action/interactional-feedback`, `prosody-and-paralinguistics/paralinguistic-state`, `intent-and-dialogue-state/dialogue-state`, `grounding-and-action/referential-grounding`, `intent-and-dialogue-state/intent-in-context`, `turn-taking-and-repair/turn-boundary`, `intent-and-dialogue-state/dialogue-state`, `grounding-and-action/referential-grounding`, `prosody-and-paralinguistics/prosodic-meaning`, `grounding-and-action/referential-grounding`, `intent-and-dialogue-state/dialogue-state`, `prosody-and-paralinguistics/prosodic-meaning`, `prosody-and-paralinguistics/prosodic-meaning`, `prosody-and-paralinguistics/paralinguistic-state`, `grounding-and-action/interactional-feedback`, `grounding-and-action/referential-grounding`, `prosody-and-paralinguistics/prosodic-meaning`, `turn-taking-and-repair/turn-boundary`, `grounding-and-action/speech-act`, `intent-and-dialogue-state/dialogue-state`, `grounding-and-action/referential-grounding`, `grounding-and-action/referential-grounding`, `intent-and-dialogue-state/dialogue-state`, `intent-and-dialogue-state/dialogue-state`, `grounding-and-action/referential-grounding`, `intent-and-dialogue-state/dialogue-state`, `grounding-and-action/referential-grounding`, `turn-taking-and-repair/turn-boundary`, `grounding-and-action/interactional-feedback`, `turn-taking-and-repair/repair-and-clarification`, `grounding-and-action/referential-grounding`, `turn-taking-and-repair/turn-boundary`, `grounding-and-action/interactional-feedback`, `intent-and-dialogue-state/dialogue-state`, `grounding-and-action/referential-grounding`, `prosody-and-paralinguistics/paralinguistic-state`, `prosody-and-paralinguistics/prosodic-meaning`, `prosody-and-paralinguistics/paralinguistic-state`, `prosody-and-paralinguistics/paralinguistic-state`, `grounding-and-action/referential-grounding`, `grounding-and-action/speech-act`, `intent-and-dialogue-state/dialogue-state`, `grounding-and-action/referential-grounding`.

### What the papers make concrete

#### Investigating the Reasoning Abilities of Large Language Models for Understanding Spoken Language in Interpersonal Interactions

**Why this belongs:** The study tests whether language models use context and domain knowledge to interpret spoken questions; it concerns intended meaning rather than waveform recovery.

**Mechanism:** Supply interview context and domain knowledge, compare prompting strategies and model scales, and score both answer quality and reasoning behavior.

**Mathematical/evaluation object:** Prompt conditions act as information controls: context and domain knowledge reduce ambiguity, while ablations reveal which information supports the decision.

**Reported evidence:** The paper reports that contextual and domain-knowledge prompting improves selected spoken-interaction reasoning settings, especially for larger models.

**Limit:** Interview distribution, transcript quality, subjective scoring, prompt sensitivity, and model-family coverage limit claims about general conversational understanding.

#### agrawal25_interspeech

**Why this belongs:** The paper probes whether speech-language models rely on label semantics and context when answering tasks; the conceptual issue is intended task meaning, not only transcription.

**Mechanism:** The model maps speech and demonstrations to symbolic targets, then is evaluated in matched and mismatched task settings with zero/few-shot context.

**Mathematical/evaluation object:** The central object is a label permutation: performance tests whether the model learned task structure rather than memorized label names.

**Reported evidence:** The paper reports improved unseen-task performance over standard approaches in its three-task evaluation.

**Limit:** Fine-tuning used batch size one and the task/model/data setup is narrower than general spoken reasoning.

#### Chain-of-Thought Training for Open E2E Spoken Dialogue Systems

**Why this belongs:** The paper adds intermediate reasoning supervision to an end-to-end spoken dialogue system, making conversational state part of the response decision.

**Mechanism:** Speech is encoded into a shared representation, the model predicts intermediate dialogue reasoning, and a decoder produces the next response; ablations compare direct response training with the added supervision.

**Mathematical/evaluation object:** The training objective sums token-level losses over intermediate and final sequences; task success and response quality test whether extra structure improves the intended action rather than only wording.

**Reported evidence:** The paper reports improvements for open end-to-end spoken dialogue modeling from chain-of-thought training and evaluates the resulting response behavior.

**Limit:** Reasoning traces are supervision artifacts and do not prove faithful internal reasoning; task distribution, annotation quality, and evaluation subjectivity constrain the claim. No independent reproduction was performed.

#### FD-Bench: A Full-Duplex Benchmarking Pipeline Designed for Full Duplex Spoken Dialogue Systems

**Why this belongs:** The paper evaluates interruption and overlap behavior directly because ordinary turn-based benchmarks hide the failures of full-duplex dialogue.

**Mechanism:** FD-Bench combines generated speech, TTS, ASR, and LLM-based scenario control to create over 40 hours of speech, 293 simulated conversations, and 1,200 interruptions. It runs three open-source full-duplex systems through the same scenarios and records response and interruption outcomes.

**Mathematical/evaluation object:** The benchmark defines event-level metrics over interruption and delay conditions rather than reducing the interaction to one transcript score. Its denominator is the simulated conversation/interruption set, not ordinary ASR utterances.

**Reported evidence:** The reported benchmark finds that all three tested systems still struggle with user interruptions, frequent disruptions, and noisy conditions; the paper states that data and code will be released.

**Limit:** The conversations and interruptions are simulated/generated, and benchmark metrics are proxies for human experience. Release claims are not equivalent to artifact execution here; no independent reproduction or user study was performed.

#### A-SMiLE: Affective Sparse Mixture-of-Experts Adapter with Multi-Task Learning for Spoken Dialogue Models

**Why this belongs:** The method makes valence, arousal, and dominance part of response generation so prosodic affect can change the dialogue action.

**Mechanism:** A-SMiLE encodes the input speech, routes it through sparse experts, predicts continuous valence/arousal/dominance values, and conditions response generation on the affective representation. The joint objective combines mean-squared error for emotion prediction with cross-entropy for response generation; evaluation uses DailyTalk and a hard-case emotional set.

**Mathematical/evaluation object:** The model minimizes a weighted sum of emotion MSE and response token cross-entropy. Reported metrics separate VAD prediction from response quality, including automatic response measures and GPT-4o-based evaluation, so no one score is treated as emotion itself.

**Reported evidence:** The paper reports improvements over text-only and other baselines on VAD prediction and response generation on DailyTalk and its 0.8-hour hard-case emotional benchmark.

**Limit:** The hard-case data and automatic judge define the tested notion of affective appropriateness; VAD labels simplify lived emotion and GPT-based evaluation is a proxy. The paper does not establish sustained human dialogue benefit or causal understanding of emotion; no independent reproduction was performed.

#### Triadic Multi-party Voice Activity Projection for Turn-taking in Spoken Dialogue Systems

**Why this belongs:** Triadic voice-activity projection predicts who will speak next from acoustic history, replacing fixed silence thresholds with joint temporal state prediction.

**Mechanism:** The VAP model encodes acoustic history and predicts binary speaking states for each speaker over future bins. With three speakers and two bins per speaker there are 2^6 possible states; cross-entropy trains the state distribution, and next-speaker accuracy compares predictions with held-out activity.

**Mathematical/evaluation object:** The state space is a six-bit joint voice-activity label; probability mass over states gives the predicted future activity. The evaluation reports test loss and next-speaker accuracy, with separate spontaneous and attentive conversation conditions.

**Reported evidence:** Triadic VAP trained on triadic conversation outperforms the baseline across tested models, while spontaneous discussions are harder than attentive listening; the paper reports accuracy differences by conversation type.

**Limit:** The data are Japanese triadic discussions with controlled recording and a limited number of participants; the reduced two-bin horizon does not cover the full dyadic two-second state space. Acoustic-only prediction does not establish successful spoken-agent behavior, and no independent reproduction or user study was performed.

#### Developing a Top-tier Framework in Naturalistic Conditions Challenge for Categorized Emotion Prediction: From Speech Foundation Models and Learning Objective to Data Augmentation and Engineering Choices

**Why this belongs:** Soft emotion distributions and minority-aware training treat affect as uncertain human judgment rather than one unquestionable class.

**Mechanism:** SAILER compares WavLM Large and Whisper Large-V3 speech encoders, combines speech and text embeddings, and predicts primary plus secondary emotion and attribute labels. Annotation dropout removes 20% of majority-class annotations during training; audio mixing combines majority and minority samples with silence or overlap.

**Mathematical/evaluation object:** The target is a soft distribution d rather than a one-hot vector, and KL divergence trains the predicted distribution. The best single system reports macro-F1 0.411 and accuracy 54.53; a three-system ensemble reaches macro-F1 0.431 and accuracy 57.00, while minority mean average precision is tracked separately.

**Reported evidence:** Whisper representations outperform WavLM in the reported comparisons; audio mixing and annotation dropout improve minority-class average precision more reliably than overall accuracy, and adding secondary emotions improves the main score but can hurt minority classes.

**Limit:** The evidence comes from the MSP-Podcast IS25-SER challenge and validation-heavy experiments; the hidden test labels limit systematic ablation. Emotion categories and annotator distributions remain task-specific, and no independent reproduction was performed.

#### AC/DC: LLM-based Audio Comprehension via Dialogue Continuation

**Why this belongs:** Dialogue continuation turns audio descriptions into answers grounded in the sound rather than fixed caption wording.

**Mechanism:** An audio encoder feeds an adapter and language model; interleaved audio/text examples use token cross-entropy, with LoRA tested on AudioCaps, WavCaps, and Clotho.

**Mathematical/evaluation object:** The loss is token-level cross-entropy. The best reported average AQA accuracy is 47.70%, judged by Llama-3-70B-Instruct; the judge is itself a proxy.

**Reported evidence:** Dialogue-continuation training enables zero-shot instruction following and improves reported AQA, while AAC gains are mixed.

**Limit:** Generated captions, benchmarks, and an LLM judge define the evidence; human usefulness for deaf or hard-of-hearing users is not established.

#### Who Gets the Mic? Investigating Gender Bias in the Speaker Assignment of a Speech-LLM

**Why this belongs:** Default speaker assignment makes social associations in speech generation observable as an accountability behavior.

**Mechanism:** Bark is prompted with two constructed datasets and assignments are counted for gender alignment and inclinations.

**Mathematical/evaluation object:** The controlled assignment counts are an association probe, not population prevalence or a human perception study.

**Reported evidence:** Bark shows gender awareness and some inclinations but no strong systematic bias under the tested prompts.

**Limit:** Two datasets, one model, prompt wording, and supported voices bound the conclusion; this is not a fairness guarantee.

#### Coping with segmental–prosodic incongruity in spoken word recognition in Japanese

**Why this belongs:** Controlled incongruity experiments test how lexical pitch accent and segments jointly shape word recognition.

**Mechanism:** Experiments isolate cue type, delay, and lexical repetition; mixed-effects models compare segmental and prosodic conditions.

**Mathematical/evaluation object:** Response-time models compare conditions; the paper reports prosodic inhibition at a 750 ms interval.

**Reported evidence:** Results suggest prosodic mispronunciation inhibits recognition at the tested delay.

**Limit:** Japanese materials, pitch-accent system, participants, and laboratory task limit cross-language generalization.

#### ``Dyadosyncrasy'', Idiosyncrasy and Demographic Factors in Turn-Taking

**Why this belongs:** Turn timing is modeled as a property of a speaking pair, not only an isolated speaker or local acoustic cue.

**Mechanism:** Spontaneous English dyads are analyzed by mixed models separating individual idiosyncrasy from dyad-specific interaction.

**Mathematical/evaluation object:** Marginal R2 and random-effects comparisons show dyadic effects dominate the reported variation.

**Reported evidence:** Sex and age have smaller effects while dyad variation most strongly shapes timing; TFO decreases across sampled lifespan.

**Limit:** English strangers, sparse older data, topic mix, and TFO limit familiar-relationship and full-dialogue claims.

#### Unified Audio-Visual Modeling for Recognizing Which Face Spoke When and What in Multi-Talker Overlapped Speech and Video

**Why this belongs:** The official abstract and captured PDF identify a speech object and mechanism that instantiate referential-grounding under grounding-and-action; the PDF now supports full-paper mechanism/evaluation notes, while this remains taxonomy membership rather than independent reproduction.

**Mechanism:** The model combines speech and video encoders with Transformer decoding; evaluation compares it with single-talker, multi-talker, and modular audio-visual baselines on LRS3-derived mixtures.

**Mathematical/evaluation object:** WER measures words, TER measures which face spoke when, and VWER charges a word error when the speaker tag is wrong even if another transcript is correct. This makes attribution part of recognition.

**Reported evidence:** The proposed model reports lower or competitive WER/VWER and strong VTER as the number of overlapping speakers rises, with tags placed before or after each transcription tested explicitly.

**Limit:** The evidence is bounded to constructed LRS3 mixtures, visible faces, tested overlap counts, and author-reported metrics; natural meetings, missed faces, and long-range turn structure remain open.

#### Learning More with Less: Self-Supervised Approaches forLow-Resource Speech Emotion Recognition

**Why this belongs:** Low-resource emotion recognition asks how much affective meaning can be learned when examples of the relevant speaking state are scarce.

**Mechanism:** The study compares self-supervised objectives and analyzes their cross-lingual behavior for Urdu, German, and Bangla emotion recognition.

**Mathematical/evaluation object:** F1 measures class decisions; the comparison asks how much it improves over supervised or conventional representation learning under limited labels.

**Reported evidence:** The paper reports F1 improvements of 10.6% in Urdu, 15.2% in German, and 13.9% in Bangla.

**Limit:** The reported gains depend on the selected languages, labels, augmentations, and emotion definitions; cultural validity and transfer to new languages remain open.

#### Backchannel prediction for natural spoken dialog systems  using general speaker and listener information

**Why this belongs:** Backchannel prediction models when a listener should respond, treating conversation as coordinated timing rather than a sequence of independent utterances.

**Mechanism:** The model uses speech, text, and general embeddings and compares three- and eleven-category prediction against ID-based systems.

**Mathematical/evaluation object:** Accuracy is reported separately for coarse and fine categories, exposing the cost of richer response choices.

**Reported evidence:** The paper reports 1.3% accuracy improvement for three classes and 0.9% for eleven classes over conventional ID embeddings.

**Limit:** The result is author-reported for the tested dialogue corpus and categories; natural turn timing, privacy leakage in embeddings, and user experience remain open.

#### Vela: Scalable Embeddings with Voice Large Language Models for Multimodal Retrieval

**Why this belongs:** Audio-text retrieval asks whether a voice representation can connect spoken sound to a matching textual or multimodal referent.

**Mechanism:** Vela uses selected prompts and in-context examples, then trains on text pairs; retrieval is tested on ordinary and newly designed long/complex benchmarks.

**Mathematical/evaluation object:** Text-audio retrieval metrics compare the rank of the correct audio; the new tests ask whether the embedding preserves multiple pieces of a query.

**Reported evidence:** The paper reports that Vela outperforms traditional CLAP models and is more robust on long, complex retrieval tasks.

**Limit:** The abstract says code is forthcoming and the result is tied to the chosen benchmarks and prompts; open-world audio, speech-specific retrieval, and independent reproduction remain open.

#### EmotionRankCLAP: Bridging Natural Language Speaking Styles and Ordinal Speech Emotion via Rank-N-Contrast

**Why this belongs:** Ordinal emotion and natural-language speaking style are related but not identical; ranking them exposes degrees of perceived affect instead of forcing one universal label.

**Mechanism:** EmotionRankCLAP aligns emotional speech with natural-language speaking-style prompts and contrasts examples according to their position in valence-arousal space.

**Mathematical/evaluation object:** The loss encodes an ordering rather than only class identity; cross-modal retrieval tests whether the learned space preserves emotion relations.

**Reported evidence:** The paper reports better emotion ordinality than existing emotion-CLAP systems on cross-modal retrieval.

**Limit:** The result depends on rating dimensions, prompt wording, and the tested emotion corpus; listener disagreement and transfer across cultures remain open.

#### Rapport-Building Dialogue Strategies for Deeper Connection: Integrating Proactive Behavior, Personalization, and Aizuchi Backchannels

**Why this belongs:** Proactive behavior, personalization, and backchannels are timing choices that determine whether a dialogue partner yields, continues, or repairs.

**Mechanism:** CO-STAR and few-shot prompts drive a robot in human-robot interaction; stalls, dialogue similarity, robot backchannels, participant behavior, and questionnaires are evaluated.

**Mathematical/evaluation object:** The paper separates system behavior from participant behavior and subjective reports rather than treating one dialogue score as rapport.

**Reported evidence:** The integrated strategy is reported to improve behavioral and subjective rapport measures.

**Limit:** The study is bounded to the robot, prompts, participants, and short interaction protocol; long-term trust, cultural variation, and causal attribution remain open.

#### Co-Speech Motion for Virtual Agents in Dialogue Using LLM-Driven Primitive Action Selection

**Why this belongs:** A virtual agent must turn dialogue context into a timed body action; primitive selection makes the response an explicit interactional choice.

**Mechanism:** The proposed model uses LLM-driven primitive action selection for co-speech motion in virtual agents and robots.

**Mathematical/evaluation object:** The operative object is a mapping from dialogue context to a sequence of reusable primitive actions; the captured paper does not establish a completed quantitative comparison.

**Reported evidence:** The paper presents a flexible and scalable approach, but the preserved evidence does not establish a numerical gain.

**Limit:** Full mechanism, baselines, human judgments, and cross-embodiment transfer require the paper's detailed evaluation; the result is not a claim of human-like motion.

#### Robot-assisted Recognition of Vocal Emotions in Pseudospeech for Cochlear Implanted Adolescents

**Why this belongs:** Emotion recognition for cochlear-implant users asks which vocal cues remain meaningful when the listener's access to acoustic detail is altered.

**Mechanism:** Adolescents aged 10–17 complete EmoHI pseudospeech emotion tests with a computer and NAO robot; d-prime, duration, and usability are measured.

**Mathematical/evaluation object:** Sensitivity, test duration, and perceived usability/enjoyment expose the tradeoff between measurement equivalence and engagement.

**Reported evidence:** Sensitivity is similar (.36 versus .37); the robot takes longer, is less usable, but is more enjoyable and engaging.

**Limit:** The participants, robot, pseudospeech task, and small sample bound the result; long-term adherence and general hearing-device populations remain open.

#### Multimodal Fusion with Semi-Supervised Learning Minimizes Annotation Quantity for Modeling Videoconference Conversation Experience

**Why this belongs:** Videoconference experience depends on multimodal timing and interaction context, not only on the words in a transcript.

**Mechanism:** Audio, facial-action, and text features are fused; modality-specific learners exchange pseudo-label information while the model is tested on held-out sessions.

**Mathematical/evaluation object:** Co-training uses agreement between views to expand supervision; ROC-AUC measures ranking of rare events while F1 measures the chosen decision threshold.

**Reported evidence:** The paper reports ROC-AUC .90 and F1 .60, and says 8% labeled data reaches 96% of the full supervised model's performance.

**Limit:** The labels, videoconference setting, participant population, and definition of negative experience bound the result; detection is not a causal explanation of why a conversation deteriorated.

#### Language-Guided Contrastive Audio-Visual Masked Autoencoder with Automatically Generated Audio-Visual-Text Triplets from Videos

**Why this belongs:** The title and preserved abstract identify a speech object and bounded intervention that instantiate referential-grounding under grounding-and-action; this resolves taxonomy membership only.

**Mechanism:** A pretrained text encoder guides masked audio-visual reconstruction and contrastive learning; automatically formed triplets are used for retrieval and classification tests.

**Mathematical/evaluation object:** Contrastive loss pulls matching modalities together and separates mismatches; masking forces the remaining views to predict missing information rather than copy it.

**Reported evidence:** The paper reports up to 5.6% recall@10 improvement for retrieval and 3.2% for classification.

**Limit:** The video domains, caption generator, CLAP filter, and downstream tasks define the result; spoken conversation and human annotation quality outside those videos remain open.

#### Medusa: A Multimodal Deep Fusion Multi-Stage Training Framework for Speech Emotion Recognition in Naturalistic Conditions

**Why this belongs:** Naturalistic speech emotion recognition combines modalities and training stages because affective meaning is distributed across voice, face, and situation.

**Mechanism:** MEDUSA builds an ensemble from self-supervised acoustic and linguistic representations, uses Manifold MixUp, and combines predictions with a trainable meta-classifier.

**Mathematical/evaluation object:** Soft targets preserve disagreement; balanced sampling changes which examples influence learning; the meta-classifier learns when component predictions should be trusted.

**Reported evidence:** MEDUSA ranked first in the naturalistic categorical emotion challenge task reported by the paper.

**Limit:** Challenge splits, annotation distributions, modalities, and ranking define the result; a leaderboard position does not establish emotion truth or cross-cultural validity.

#### Multimodal Dynamics of Hand Gestures and Pauses in Multiparty Interactions

**Why this belongs:** Hand gestures and pauses provide joint timing evidence for multiparty turns, so a participant's next action cannot be inferred from words alone.

**Mechanism:** MULTISIMO recordings provide multiparty dialogue annotations; distributions and temporal relations are compared for within- and between-speaker pauses.

**Mathematical/evaluation object:** The unit of analysis is a timed relation among gesture, pause, and speaker turn; duration and onset timing carry different information.

**Reported evidence:** Self-adaptors align with longer pauses, utterance-final syntax shortens pauses, and most gestured pauses occur within utterances.

**Limit:** Corpus annotation, participant population, gesture categories, and observational design bound the result; causal cognitive interpretations remain hypotheses.

#### Comparison-Based Automatic Evaluation for Meeting Summarization

**Why this belongs:** Meeting summarization evaluation must compare system outputs by whether they preserve the important state and events of a conversation.

**Mechanism:** CREAM uses reasoning traces and key-fact alignment to compare meeting summaries for completeness and conciseness without references.

**Mathematical/evaluation object:** Fact coverage and brevity become comparison evidence; Elo aggregates pairwise preferences while avoiding a false absolute scale.

**Reported evidence:** The paper presents a reference-free evaluation framework for meeting summarization and reports its ability to rank systems/prompts.

**Limit:** Facts, judge prompts, meeting domain, and pairwise comparison protocol bound the result; human validation and adversarial summaries remain open.

#### Pick and Summarize: Integrating Extractive and Abstractive Speech Summarization

**Why this belongs:** The official full paper identifies a human spoken-speech object and a bounded research problem that instantiate referential-grounding under grounding-and-action; this resolves taxonomy membership, not the paper's scientific validity.

**Mechanism:** An extractive-abstractive model is trained on a web-presentation corpus, with an extractive summary predicted from raw speech alongside the final text summary.

**Mathematical/evaluation object:** Selection narrows the content problem before wording is generated; METEOR compares the final summary with reference summaries while the extractive task supplies structure.

**Reported evidence:** The method gives consistent gains and up to 1.4 METEOR points over a strong abstractive baseline.

**Limit:** The corpus, reference summaries, metric, summary length, and presentation style bound the result; lexical overlap does not prove that all important facts were preserved.

#### Age-related changes in multisensory integration of emotions in an audiovisual face-prosody-semantics Stroop task

**Why this belongs:** The official archive evidence identifies a human spoken-speech object and a bounded problem that instantiate prosodic-meaning under prosody-and-intent; this resolves membership only.

**Mechanism:** Younger and older adults perform an audiovisual face-prosody-semantics Stroop task with happy and sad cues under congruent and incongruent conditions.

**Mathematical/evaluation object:** Reaction or accuracy differences reveal selective attention and integration costs; congruence tests whether one channel can override another.

**Reported evidence:** Older adults show reduced emotion integration, especially for prosody and other nonverbal cues, with larger age differences under incongruence.

**Limit:** The task, emotions, participant groups, language, and interpretation of Stroop costs bound the result; laboratory conflict does not directly predict everyday communication.

#### Towards High-Quality LLM-Based Data for French Spontaneous Speech Simplification: an Exo-Refinement Approach

**Why this belongs:** The official archive evidence identifies a human spoken-speech object and a bounded problem that instantiate referential-grounding under grounding-and-action; this resolves membership only.

**Mechanism:** LLM-generated French speech simplifications are refined by distinct evaluator models and compared with expert simplifications using SARI and COMET.

**Mathematical/evaluation object:** The rewrite is constrained by two targets—simpler form and preserved meaning—so separate judges provide an outside check on the tradeoff.

**Reported evidence:** Mistral-large outperforms tested baselines, Mistral-small becomes competitive after few refinements, SARI improves, and COMET indicates semantic preservation in the reported experiments.

**Limit:** The languages, prompts, judges, reference simplifications, and automatic metrics bound the result; COMET and SARI are proxies, not a guarantee of accessible or faithful speech.

#### Assessing the feasibility of Large Language Models for detecting micro-behaviors in team interactions during space missions

**Why this belongs:** The official archive evidence identifies a human spoken-speech object and a bounded problem that instantiate dialogue-state under dialogue-and-turn-taking; this resolves membership only.

**Mechanism:** Models classify micro-behaviors in transcripts from simulated space missions, including discouraging speech, under three-way and binary labelings.

**Mathematical/evaluation object:** Macro F1 exposes minority-class failure better than accuracy; the task tests whether language context alone can support interactional labeling.

**Reported evidence:** Encoder-only models struggle with rare behaviors, while an instruction-tuned Llama model reports 44% macro F1 for three-way and 68% for binary classification.

**Limit:** Simulated missions, transcript quality, label prevalence, model prompting, and macro-F1 targets bound the finding; detected text patterns are not proof of team state or causality.

#### The Prosodic Characteristics of Standard Chinese Rhetorical Questions in Naturalistic Settings

**Why this belongs:** Prosodic patterns in rhetorical questions add communicative meaning beyond the words, so pitch and timing are evidence about intent.

**Mechanism:** One hundred three native Mandarin speakers produced information-seeking and rhetorical questions through an online platform; pitch and duration of prominent verbs and modal verbs are analyzed.

**Mathematical/evaluation object:** Prosody is localized to syntactic positions: prominence placement and its acoustic realization connect the waveform to communicative intention.

**Reported evidence:** Speakers tend to mark rhetorical meaning by increasing pitch and duration on the verb or modal verb, with other cues depending on sentence structure.

**Limit:** Standard Chinese, sentence materials, online reading, participant sample, and question interpretation bound the result; rhetorical intent is not reducible to one universal pitch rule.

#### Stress in Spoken and Whistled Greek

**Why this belongs:** Whistled and spoken Greek test whether stress and vowel identity survive when the acoustic channel changes.

**Mechanism:** Participants produce five Greek vowel qualities in Sfyria whistling and spoken Greek; acoustic contrasts are compared for stressed and unstressed forms.

**Mathematical/evaluation object:** The representation changes with the communication channel: F0 and intensity are alternative carriers of phonological contrast, and a missing cue is itself evidence.

**Reported evidence:** All five vowel qualities remain distinct in the whistled register, but a whistled stress correlate is not found for /i/, possibly because front vowels are already highly intense.

**Limit:** The Sfyria community, participants, register, minimal pairs, and acoustic cues bound the result; a ceiling interpretation and cross-language generalization remain open.

#### Multi-Teacher Language-Aware Knowledge Distillation for Multilingual Speech Emotion Recognition

**Why this belongs:** Multilingual emotion recognition must preserve affective cues while allowing language-specific evidence to differ across speakers and varieties.

**Mechanism:** Wav2vec2 teachers for English, Finnish, and French are distilled into one multilingual student and evaluated by emotion recall per language and class.

**Mathematical/evaluation object:** The student is a shared model with language-conditioned supervision; weighted and unweighted recall expose both overall performance and class imbalance.

**Reported evidence:** The student reports weighted recall 72.9 on English and unweighted recall 63.4 on Finnish, with stronger gains for sad and neutral than anger and happiness.

**Limit:** Languages, emotion labels, teacher quality, class balance, and recall metrics bound the claim; multilingual transfer does not prove equal performance or culturally valid emotion categories.

#### Towards Human-like Multimodal Conversational Agent by Generating Engaging Speech

**Why this belongs:** The title and preserved abstract identify a speech object and bounded intervention that instantiate interactional-feedback under dialogue-and-turn-taking; this resolves taxonomy membership only.

**Mechanism:** The system builds a multi-sensory conversation dataset and uses a multimodal language model to produce text plus voice descriptions, which guide speech generation in dialogue examples.

**Mathematical/evaluation object:** The model separates what to say from how to say it but conditions both on the same conversational state; human judgments of engagement and relevance test whether the separation remains coordinated.

**Reported evidence:** The paper reports more engaging and contextually suitable speech than text-only baselines and shows gains from visual and audio modalities.

**Limit:** Dataset role-play, judge criteria, synthetic or recorded voices, conversation domain, and lack of exact-speaker replication bound the claim; engagement scores do not establish long-term human trust or natural conversation.

#### Face2VoiceSync: Lightweight Face-Voice Consistency for Text-Driven Talking Face Generation

**Why this belongs:** The preserved abstract identifies a speech object and bounded intervention that instantiate referential-grounding under grounding-and-action; this upgrades a provisional candidate to analyst-reviewed taxonomy membership only.

**Mechanism:** Face2VoiceSync targets text-driven talking-face generation from a face image and text, producing animation and corresponding speech while evaluating the consistency of face and voice attributes.

**Mathematical/evaluation object:** The desired output is a coupled pair: text constrains linguistic content, face conditions visual identity, and a learned cross-modal relation checks whether the generated voice belongs with the generated face.

**Reported evidence:** The paper reports improved face-voice consistency and text-driven talking-face generation quality relative to fixed-speech baselines.

**Limit:** Face identities, text prompts, speech/face datasets, consistency metric, and synchronization quality bound the claim; a consistency score does not prove that a viewer will find the character natural or trustworthy.

#### Multimodal Prosody Modeling: A Use Case for Multilingual Sentence Mode Prediction

**Why this belongs:** The preserved abstract identifies a speech object and bounded intervention that instantiate prosodic-meaning under prosody-and-intent; this upgrades a provisional candidate to analyst-reviewed taxonomy membership only.

**Mechanism:** The study presents multimodal prosody modeling for multilingual sentence-mode prediction.

**Mathematical/evaluation object:** Sentence mode is a joint signal: lexical content provides one constraint while pitch, timing, and energy provide another, and disagreement between them is informative rather than noise.

**Reported evidence:** The paper reports multilingual multimodal prosody-modeling results for sentence-mode prediction.

**Limit:** Languages, labels, speaker balance, modality quality, and task definition bound the claim; sentence mode is not a complete model of intent.

#### Visual Cues Support Robust Turn-taking Prediction in Noise

**Why this belongs:** The title and preserved abstract identify a speech object and bounded intervention that instantiate turn-boundary under dialogue-and-turn-taking; this resolves taxonomy membership only.

**Mechanism:** The study evaluates visual cues for robust turn-taking prediction in noise.

**Mathematical/evaluation object:** A turn is a coordination event between people, not merely a boundary in a waveform; combining channels lets one cue compensate when another is degraded.

**Reported evidence:** The paper reports that visual cues support more robust turn-taking prediction under noisy conditions.

**Limit:** Participants, camera viewpoint, interaction task, noise type, timing labels, and model latency bound the claim; a lab cue is not a universal conversational rule.

#### Speech-IFEval: Evaluating Instruction-Following and Quantifying Catastrophic Forgetting in Speech-Aware Language Models

**Why this belongs:** Instruction-following evaluation asks whether a speech model obeys the requested constraint, not merely whether its transcript is plausible.

**Mechanism:** The paper introduces Speech-IFEval and evaluates instruction-following and forgetting in speech-aware language models.

**Mathematical/evaluation object:** Evaluation must pair compliance with retention: a model that follows a new command by losing old behavior has shifted capability rather than simply improved it.

**Reported evidence:** The paper reports benchmark results for spoken instruction following and catastrophic forgetting.

**Limit:** Task suite, speech recognition quality, prompts, model families, and training order bound the conclusions; benchmark retention is not proof of reliable deployment behavior.

#### Analysis of ABC Frontend Audio Systems for the NIST-SRE24

**Why this belongs:** A speaker-recognition evaluation exposes how front-end choices affect identity judgments before a downstream system ever sees the speech.

**Mechanism:** The paper analyzes ABC frontend audio systems for the NIST SRE24 audio track.

**Mathematical/evaluation object:** The frontend is a measurement pipeline: representation, temporal pooling, training population, and domain match jointly determine whether identity survives telephone speech.

**Reported evidence:** The paper reports comparative robustness and performance for the explored architectures and data conditions.

**Limit:** NIST protocol, telephone channel, language mix, training-data access, and calibration limit claims beyond the benchmark.

#### Fact-Controlled Diagnosis of Hallucinations in Medical Text Summarization

**Why this belongs:** Hallucination diagnosis asks whether a model's answer is supported by the source rather than merely fluent, making evidence and intended meaning the central issue.

**Mechanism:** The paper studies fact-controlled diagnosis of hallucinations in medical text summarization from patient-clinician dialogues.

**Mathematical/evaluation object:** A controlled deletion makes the missing fact known, while natural cases test ecological validity; the two together separate detector sensitivity from dataset artifacts.

**Reported evidence:** The paper reports that general-domain detectors struggle on clinical hallucinations and evaluates specialized diagnostic approaches.

**Limit:** Synthetic deletion, clinical language, annotation, summarizer, and detector thresholds limit generalization; detection is not prevention or clinical validation.

#### From Words to Waves: Analyzing Concept Formation in Speech and Text-Based Foundation Models

**Why this belongs:** Comparing speech and text models asks whether a speech representation carries abstract concepts rather than only acoustic form.

**Mechanism:** The paper analyzes concept formation in speech and text-based foundation models using an unsupervised latent-concept method.

**Mathematical/evaluation object:** Concept formation is treated as a representation-comparison problem: the analysis proposes interpretable structure, while cross-modal differences reveal what the training signal makes easy or hard to encode.

**Reported evidence:** The paper reports comparative latent conceptual structures across speech, text, and joint models.

**Limit:** Model choice, layer, analysis method, prompts, and human interpretation bound the claim; a latent cluster is not automatically a human concept.

#### MMLoRA: Multitask Memory Parameter-Efficient Fine-Tuning for Multimodal SER

**Why this belongs:** Parameter-efficient multimodal tuning asks which shared and task-specific information can be retained when one model must handle several affective judgments.

**Mechanism:** MMLoRA is a multitask memory parameter-efficient method for multimodal speech emotion recognition.

**Mathematical/evaluation object:** The adaptation has two roles: shared parameters carry reusable affective structure, while expert and memory paths preserve task/person-specific differences instead of overwriting them.

**Reported evidence:** The paper reports improved multimodal SER generalization over the tested parameter-efficient baselines.

**Limit:** Datasets, gender labels, task mix, memory policy, modalities, and expression cultures bound the result; auxiliary gender is not a complete model of individual variation.

#### Leveraging LLMs for Written to Spoken Style Data Transformation to Enhance Spoken Dialog State Tracking

**Why this belongs:** Spoken dialogue state tracking must survive disfluencies and recognition errors rather than assume clean written turns.

**Mechanism:** The paper leverages LLMs for written-to-spoken style transformation to enhance spoken dialogue-state tracking.

**Mathematical/evaluation object:** The transformation is constrained paraphrasing: surface form changes, but the underlying user goal and slot state must remain invariant for the data to be useful.

**Reported evidence:** The paper reports spoken dialogue-state-tracking gains from the transformed data.

**Limit:** LLM prompt, domains, state schema, speech realization, annotation checks, and evaluation distribution limit the result; style conversion can silently change intent.

#### Teaching Audio-Aware Large Language Models What Does Not Hear: Mitigating Hallucinations through Synthesized Negative Samples

**Why this belongs:** The title and preserved abstract identify a speech object and bounded intervention that instantiate referential-grounding under grounding-and-action; this resolves taxonomy membership only.

**Mechanism:** The paper teaches audio-aware large language models what they do not hear through synthesized negative samples.

**Mathematical/evaluation object:** The negative examples define an evidence boundary: language generation is rewarded only when its claim is supported by the acoustic input, not merely likely in context.

**Reported evidence:** The paper reports reduced hallucination behavior for the tested audio-aware models and synthesized negative-sample strategy.

**Limit:** Negative-sample construction, audio quality, prompts, model family, and evaluation rubric limit the claim; abstention quality is not the same as factual clinical reliability.

#### Factors affecting the in-context learning abilities of LLMs for dialogue state tracking

**Why this belongs:** Dialogue-state tracking depends on what the conversation has established, so in-context examples can change what a spoken turn means.

**Mechanism:** The paper studies factors affecting the in-context learning abilities of LLMs for dialogue state tracking.

**Mathematical/evaluation object:** In-context learning is an interaction between model prior and task presentation: the examples are part of the effective program and must be analyzed as such.

**Reported evidence:** The paper reports factor-level findings on in-context dialogue-state tracking.

**Limit:** Model family, prompt, domains, state schema, demonstration order, and context length bound the result; prompt sensitivity is not a stable conversational capability.

#### Bridging Audio and Vision: Zero-Shot Audiovisual Segmentation by Connecting Pretrained Models

**Why this belongs:** The title and preserved abstract identify a speech object and bounded intervention that instantiate referential-grounding under grounding-and-action; this resolves taxonomy membership only.

**Mechanism:** The paper studies zero-shot audiovisual segmentation by bridging pretrained audio and vision models.

**Mathematical/evaluation object:** Segmentation is grounded association: the system must align a sound event with a spatial region using cross-modal evidence rather than merely classify the clip.

**Reported evidence:** The paper reports zero-shot audiovisual segmentation results for the connected pretrained models.

**Limit:** Datasets, categories, synchronization, pretrained models, and segmentation labels bound the result; co-occurrence does not establish physical source identity.

#### Gaze-Enhanced Multimodal Turn-Taking Prediction in Triadic Conversations

**Why this belongs:** The model uses gaze and speaker localization to predict who will take the next turn in triadic interaction.

**Mechanism:** The paper studies gaze-enhanced multimodal turn-taking prediction in triadic conversations.

**Mathematical/evaluation object:** Turn-taking is addressed to someone: person-conditioned visual cues resolve part of the interaction structure that an audio-only boundary cannot represent.

**Reported evidence:** The paper reports turn-taking prediction results with gaze enhancement in triadic interaction.

**Limit:** Participants, camera setup, roles, task, gaze annotation, and latency bound generalization; gaze is a cue, not a deterministic intention signal.

#### Beat gestures made by human-like avatars affect speech perception

**Why this belongs:** The title and preserved abstract identify a speech object and bounded intervention that instantiate interactional-feedback under grounding-and-action; this resolves taxonomy membership only.

**Mechanism:** The paper studies how beat gestures made by human-like avatars affect speech perception.

**Mathematical/evaluation object:** Gesture functions as timed emphasis: its effect depends on alignment with prosodic or semantic structure, so perception experiments are needed instead of a visual-quality proxy.

**Reported evidence:** The paper reports speech-perception effects of avatar beat gestures in the tested stimuli and listener tasks.

**Limit:** Avatar design, gesture timing, speech material, participants, and task bound generalization; a laboratory effect is not proof of conversational benefit.

#### Enhancing Transcripts of Open-Source Automatic Speech Recognition Models Through Fine-Tuning with Laughter and Speech-Laugh

**Why this belongs:** Transcript correction must preserve laughter and speech-laugh distinctions because those events affect how a conversation is interpreted.

**Mechanism:** The paper enhances open-source ASR transcripts through fine-tuning with laughter and speech-laugh.

**Mathematical/evaluation object:** The transcript target expands from words to interactional vocal events; the model must preserve an event boundary and its overlap with lexical speech.

**Reported evidence:** The paper reports improved handling of laughter and speech-laugh in the tested ASR transcripts.

**Limit:** Annotation scheme, language, laughter types, model, data mixture, and transcript use case bound the result; event recognition is not a full emotion or intent analysis.

#### The mutual exclusivity bias of bilingual visually grounded speech models

**Why this belongs:** The title and preserved abstract identify a speech object and bounded intervention that instantiate referential-grounding under grounding-and-action; this resolves taxonomy membership only.

**Mechanism:** The paper studies mutual exclusivity bias in bilingual visually grounded speech models.

**Mathematical/evaluation object:** The task probes how a model allocates a new label when familiar labels already exist; its choice reveals an interaction between language-specific priors and visual evidence.

**Reported evidence:** The paper reports mutual-exclusivity behavior and cross-language differences for the tested bilingual grounded models.

**Limit:** Languages, training data, object stimuli, model architecture, prompt/task design, and bias measure bound the claim; model behavior is not a direct account of child learning.

#### Efficient and Direct Duplex Modeling for Speech-to-Speech Language Model

**Why this belongs:** Duplex speech-to-speech interaction must model simultaneous streams, barge-in, and turn exchange rather than wait for isolated turns.

**Mechanism:** The paper studies efficient and direct duplex modeling for speech-to-speech language models.

**Mathematical/evaluation object:** Duplexity is a control problem over concurrent streams: the model must decide what to retain, when to respond, and when to yield while generating speech.

**Reported evidence:** The paper reports efficiency and interactive speech-to-speech results for the duplex model.

**Limit:** Latency, overlap, interruptions, model size, dialogue tasks, and evaluation protocol bound the result; a real-time demo is not robust open-ended conversation.

#### GenECA: A General-Purpose Framework for Real-Time Adaptive Multimodal Embodied Conversational Agents

**Why this belongs:** The title and preserved abstract identify a speech object and bounded intervention that instantiate interactional-feedback under grounding-and-action; this resolves taxonomy membership only.

**Mechanism:** GenECA is a framework for real-time adaptive multimodal embodied conversational agents.

**Mathematical/evaluation object:** Embodied conversation is a closed loop: perception changes the state, the state selects language and action, and the agent's output changes the next observation.

**Reported evidence:** The paper reports real-time adaptive-agent behavior across its tested multimodal interaction settings.

**Limit:** Sensors, embodiment, latency, dialogue tasks, user studies, and policy constraints bound the claim; a framework demonstration is not human-level social understanding.

#### Modeling Multi-Turn Spoken Language Understanding with Dynamic Graph Convolutional Networks

**Why this belongs:** Multi-turn spoken understanding must keep the relevant history while ignoring conversational details that no longer affect intent and slots.

**Mechanism:** The paper models multi-turn spoken-language understanding with dynamic graph convolutional networks.

**Mathematical/evaluation object:** Dialogue state is a changing relational structure: the graph makes explicit which words, entities, and turns constrain the current interpretation.

**Reported evidence:** The paper reports multi-turn spoken-language-understanding results for the dynamic graph model.

**Limit:** Domains, ASR errors, graph construction, turn length, labels, and evaluation split bound the result; a graph state is not complete conversational memory.

#### SNIFR : Boosting Fine-Grained Child Harmful Content Detection Through Audio-Visual Alignment with Cascaded Cross-Transformer

**Why this belongs:** The title and preserved abstract identify a speech object and bounded intervention that instantiate referential-grounding under grounding-and-action; this resolves taxonomy membership only.

**Mechanism:** SNIFR boosts fine-grained child harmful-content detection through audio-visual alignment with cascaded cross-transformers.

**Mathematical/evaluation object:** Safety understanding is multimodal grounding: the system must connect a specific spoken or visible event to a category and preserve timing for intervention.

**Reported evidence:** The paper reports fine-grained audiovisual detection and real-time behavior for the tested harmful-content data.

**Limit:** Labels, age policy, modalities, cultures, false-positive costs, and latency bound the result; an automated detector is not a safeguarding decision-maker.

#### Heart Rate as a Proxy Measure to Assess Human Confidence in Spoken Speech

**Why this belongs:** The proposed speech-derived heart-rate proxy treats confidence as a bodily state inferred from voice-related physiology.

**Mechanism:** The paper presents a three-stage speech-to-breathing-to-heart-rate approach for confidence analysis.

**Mathematical/evaluation object:** The key conceptual move is indirect sensing: speech is used as a window onto a bodily rhythm, but the inferred physiology is not the same thing as confidence itself.

**Reported evidence:** The paper reports that confident speakers had an average heart rate about 10 beats per minute lower in its tested data.

**Limit:** The datasets, Indian demographic, 41-speaker collection, clinical and wearable references, confidence labels, and unreported general accuracy bound the claim; correlation is not a validated psychological diagnosis.

#### EmoDB 2.0: A Database of Emotional Speech in a World that is not Black or White but Grey

**Why this belongs:** A broadened emotional-speech database tests whether emotion categories remain meaningful when speakers and social contexts are not treated as one neutral population.

**Mechanism:** The paper extends the Berlin Database of Emotional Speech with ambiguity, glottograms, and naturalness information.

**Mathematical/evaluation object:** Dataset construction is part of the scientific model: disagreement and phonation measurements expose how an emotion label is produced and where it is uncertain.

**Reported evidence:** The paper reports an 8.1% UAR improvement for an SVM when glottogram information is incorporated in its preliminary study.

**Limit:** The acted German corpus, old recording conditions, rater thresholds, classifier, and preliminary evaluation bound the result; improved classification does not establish better emotion understanding.

#### MIKU-PAL: An Automated and Standardized Multimodal Method for Speech Paralinguistic and Affect Labeling

**Why this belongs:** Automated multimodal affect labeling addresses the instability of emotion judgments by combining signals and standardizing what the labels mean.

**Mechanism:** MIKU-PAL is an automated multimodal method for paralinguistic and affect labeling.

**Mathematical/evaluation object:** Corpus creation is itself multimodal inference: the label is a negotiated interpretation of face, voice, and context, and its consistency must be measured separately from its usefulness to a downstream synthesizer.

**Reported evidence:** The paper reports 68.5% MELD accuracy, 0.93 Fleiss kappa, 83% human rationality ratings, and a 131.2-hour benchmark with up to 26 emotion types.

**Limit:** Video sources, model judgments, cultural assumptions, label taxonomy, human validation, and downstream use bound the claim; agreement or rationality is not ground-truth emotion.

#### EmoSphere-SER: Enhancing Speech Emotion Recognition Through Spherical Representation with Auxiliary Classification

**Why this belongs:** A spherical representation for emotion recognition tests whether affective states are better organized by relative relationships than by independent class boundaries.

**Mechanism:** EmoSphere-SER uses spherical VAD-region classification to guide emotion regression.

**Mathematical/evaluation object:** The model gives the affect space neighborhoods and a coarse location before asking for a precise coordinate, coupling classification’s stability with regression’s detail.

**Reported evidence:** The reported experiments show the combined model outperforming the compared baselines and improving prediction consistency.

**Limit:** Emotion labels, VAD geometry, datasets, region partition, weighting, and metrics bound the result; a better coordinate prediction does not establish a speaker’s actual inner state.

#### Spoken Question Answering for Visual Queries

**Why this belongs:** The title and preserved abstract identify a speech object and bounded intervention that instantiate referential-grounding under grounding-and-action; this resolves taxonomy membership only.

**Mechanism:** Whisper encodes speech and CLIP encodes images; modality-specific projectors align both representations with LLaVA's language space, with speech-only pretraining followed by joint spoken-VQA fine-tuning.

**Mathematical/evaluation object:** The model predicts an answer from a fused representation. Accuracy, ANLS, and MME scores compare the answer with the task-specific reference; WER separately exposes speech-to-text failure.

**Reported evidence:** Synthetic speech training approaches the text-trained VQA upper bound on several benchmarks; the paper reports 62% SEED-Bench accuracy for its strongest spoken variants, with TTS choice having a small effect.

**Limit:** Most training speech is synthesized, the spoken models remain below the text model, prompt format changes performance sharply, and transcription failures can be confused with visual-reasoning failures. No independent reproduction was performed.

#### Enhancing Speech Instruction Understanding and Disambiguation in Robotics via Speech Prosody

**Why this belongs:** A robot must use prosody to disambiguate what a spoken instruction is intended to make it do.

**Mechanism:** Prosodic and raw-audio features feed Transformer or BiLSTM sequence models trained with cross-entropy; predicted referents are placed in prompts for GPT-4o, o1-mini, or o3-mini to choose among plans.

**Mathematical/evaluation object:** The sequence model estimates a label distribution for each token; accuracy, precision, recall, and F1 measure referent detection, while plan accuracy measures the final discrete action choice.

**Reported evidence:** On 1,540 recordings from 22 participants, the best BiLSTM reaches 95.79% overall referent accuracy, and Prosody-Transformer plus GPT-4o reaches 71.96% task-plan accuracy versus 50% for the ASR-only prompt.

**Limit:** The dataset is small and participants are 18–22; recorded ambiguity and candidate plans are controlled rather than open-world robot interaction. Prosody helps the tested task but does not establish safe execution in physical environments.

#### Dialogue Response Prefetching Based on Semantic Similarity and Prediction Confidence of Language Model

**Why this belongs:** The title and preserved abstract identify a speech object and bounded intervention that instantiate dialogue-state under dialogue-and-turn-taking; this resolves taxonomy membership only.

**Mechanism:** A prediction-confidence model compares embeddings or semantic representations of the predicted and completed user utterances; response latency and prediction correctness quantify when prefetching is safe.

**Mathematical/evaluation object:** The decision is selective rather than binary: the system estimates expected utility under uncertainty, trading saved user-perceived latency against wrong-response risk.

**Reported evidence:** The paper reports that semantic-similarity confidence can reduce user-perceived latency while limiting unsafe prefetches in the tested spoken-dialogue setting.

**Limit:** The language model, dialogue domain, confidence calibration, and endpointing assumptions constrain generalization; lower latency is not the same as better conversation or human trust.

#### Discrete Audio Representations for Automated Audio Captioning

**Why this belongs:** Captured full paper supports audio-token-semantics under grounding-and-action; author-reported result and limits are preserved.

**Mechanism:** Encode audio into learned discrete tokens, condition a text decoder on those tokens, and compare tokenizers and decoder choices on caption metrics.

**Mathematical/evaluation object:** Quantization creates a finite vocabulary of acoustic units; the central question is whether the units preserve event identity rather than merely waveform detail.

**Reported evidence:** The paper reports that selected audio tokenizers improve automated captioning quality, showing that representation design affects semantic generation.

**Limit:** Reference-caption incompleteness, metric proxy limits, dataset scope, and no broad human grounding study limit conclusions about listener usefulness.

### Synthesis boundary

These papers share a conceptual pressure, but this seed batch does not justify ranking methods, estimating prevalence, or claiming that the mechanism generalizes across speakers, languages, rooms, or tasks. Those claims require additional assignments and comparable denominators.

## Creating speech while keeping the right things fixed

**Ordinary pressure:** A useful synthetic voice must say the requested content, sound like the intended speaker or style, and remain understandable as it changes over time.

**Naive strategy that breaks:** Copying a recording or predicting samples directly entangles words with identity, pitch, rhythm, and recording conditions, making controlled change difficult.

**Recurring move:** Represent or condition distinct factors, generate a time-consistent waveform or acoustic sequence, and evaluate each requested property separately.

**Boundary:** Factor separation is rarely perfect: changing identity can change content, style controls can sound artificial, and a plausible voice can be misused.

**D3 evidence status:** 55 reviewed paper(s); the family claim below is limited to these examples.

**Conceptual family represented:** `identity-and-conversion/voice-conversion`, `identity-and-conversion/speaker-identity`, `expression-and-interactive-control/style-and-emotion-control`, `identity-and-conversion/voice-conversion`, `waveform-and-codec-generation/intelligibility-naturalness`, `identity-and-conversion/speaker-identity`, `expression-and-interactive-control/style-and-emotion-control`, `expression-and-interactive-control/style-and-emotion-control`, `waveform-and-codec-generation/neural-vocoder`, `identity-and-conversion/zero-shot-voice`, `waveform-and-codec-generation/intelligibility-naturalness`, `content-planning/text-to-speech-planning`, `expression-and-interactive-control/style-and-emotion-control`, `expression-and-interactive-control/prosody-control`, `identity-and-conversion/zero-shot-voice`, `content-planning/text-to-speech-planning`, `expression-and-interactive-control/interactive-latency`, `waveform-and-codec-generation/neural-vocoder`, `identity-and-conversion/zero-shot-voice`, `content-planning/text-to-speech-planning`, `identity-and-conversion/voice-conversion`, `expression-and-interactive-control/interactive-latency`, `content-planning/text-to-speech-planning`, `expression-and-interactive-control/style-and-emotion-control`, `expression-and-interactive-control/style-and-emotion-control`, `expression-and-interactive-control/prosody-control`, `waveform-and-codec-generation/neural-vocoder`, `identity-and-conversion/voice-conversion`, `expression-and-interactive-control/prosody-control`, `expression-and-interactive-control/style-and-emotion-control`, `waveform-and-codec-generation/neural-vocoder`, `identity-and-conversion/speaker-identity`, `content-planning/text-to-speech-planning`, `identity-and-conversion/voice-conversion`, `content-planning/text-to-speech-planning`, `identity-and-conversion/voice-conversion`, `expression-and-interactive-control/prosody-control`, `expression-and-interactive-control/style-and-emotion-control`, `expression-and-interactive-control/interactive-latency`, `expression-and-interactive-control/style-and-emotion-control`, `expression-and-interactive-control/style-and-emotion-control`, `expression-and-interactive-control/interactive-latency`, `expression-and-interactive-control/style-and-emotion-control`, `expression-and-interactive-control/style-and-emotion-control`, `identity-and-conversion/voice-conversion`, `waveform-and-codec-generation/neural-vocoder`, `content-planning/text-to-speech-planning`, `content-planning/text-to-speech-planning`, `identity-and-conversion/speaker-identity`, `waveform-and-codec-generation/neural-vocoder`, `identity-and-conversion/zero-shot-voice`, `content-planning/text-to-speech-planning`, `content-planning/text-to-speech-planning`, `identity-and-conversion/voice-conversion`, `identity-and-conversion/voice-conversion`.

### What the papers make concrete

#### Towards Better Disentanglement in Non-Autoregressive Zero-Shot Expressive Voice Conversion

**Why this belongs:** The model separates multilingual content units from expressive voice controls so a new speaker/style can be produced without changing the requested content.

**Mechanism:** Content, speaker, and expressive factors are separated in a non-autoregressive generation path.

**Mathematical/evaluation object:** The relevant object is the voice-conversion evidence described by the paper's mechanism: Content, speaker, and expressive factors are separated in a non-autoregressive generation path.

**Reported evidence:** The paper reports improved disentanglement for zero-shot expressive conversion.

**Limit:** Enrollment, labels, languages, metrics, and unseen-speaker protocol bound transfer.

#### VoxAging: Continuously Tracking Speaker Aging with a Large-Scale Longitudinal Dataset in English and Mandarin

**Why this belongs:** The longitudinal recordings ask how speaker verification changes as a person ages; time-varying identity is the phenomenon being measured.

**Mechanism:** Link recordings across years, then test verification as time gap, age group, and gender change.

**Mathematical/evaluation object:** EER and embedding cosine similarity turn identity preservation into separability and distance between same-speaker observations.

**Reported evidence:** The paper reports declining verification accuracy and embedding similarity as recordings move farther apart in time, with age and gender affecting the rate of change.

**Limit:** Speaker coverage, language balance, recording channels, gated data, and longitudinal confounding limit causal claims about biological aging.

#### Finding the Human Voice in AI: Insights on the Perception of AI-Voice Clones from Naturalness and Similarity Ratings

**Why this belongs:** The paper separates listener judgments of clone naturalness and target similarity and studies prosodic variation as a reason they diverge.

**Mechanism:** Listeners hear natural and generated samples, rate distinct targets, and the analysis relates ratings to acoustic/prosodic differences rather than collapsing them into one number.

**Mathematical/evaluation object:** Ratings are treated as separate subjective measurements; comparisons of pitch movement and other prosodic features test association, not a causal guarantee that one feature determines perception.

**Reported evidence:** The paper reports that AI voice clones struggle with dynamic F0 variation and analyzes its relationship to naturalness and similarity ratings.

**Limit:** Listener population, prompts, voices, and rating protocol limit generalization; perceptual association does not establish that changing F0 alone fixes naturalness. No independent reproduction was performed.

#### REWIND: Speech Time Reversal for Enhancing Speaker Representations in Diffusion-based Voice Conversion

**Why this belongs:** The method uses time reversal to destroy much linguistic order while retaining speaker-related cues, then uses those representations for voice conversion.

**Mechanism:** The full waveform is reversed, passed through the speaker-representation pipeline, and used as an additional training view. The conversion model conditions generation on speaker information while its content path carries the linguistic signal; experiments compare diffusion VC systems with and without the reversed-speech augmentation.

**Mathematical/evaluation object:** The paper evaluates speaker similarity and speech quality rather than treating reversal as a new waveform objective. The conceptual operation is an information intervention: destroy temporal phoneme order while retaining slower vocal traits.

**Reported evidence:** The paper reports significantly improved speaker-similarity scores while maintaining high speech quality in diffusion-based voice-conversion experiments.

**Limit:** Time reversal may remove more or less information depending on language and model; the experiments do not establish universal speaker/language disentanglement or human identity judgments across populations. No independent reproduction was performed.

#### Intelligibility of Text-to-Speech Systems for Mathematical Expressions

**Why this belongs:** The paper tests whether synthesized mathematical speech preserves relations and symbols for listeners, separating intelligibility from naturalness.

**Mechanism:** The study samples 120 expressions across eight categories, uses Qwen or GPT-4 to create spoken text, synthesizes audio with five TTS models, and asks 49 technically trained listeners to rate and transcribe it. A second test compares 35 expressions with hidden expert renditions.

**Mathematical/evaluation object:** Evaluation includes MOS, exact count-of-correct, LaTeX character error rate, and TeXBLEU; ANOVA tests TTS model, expression category, and LLM effects. The denominator is the selected expression/listener trials, not general language understanding.

**Reported evidence:** No TTS model is consistently strong across categories; intelligibility varies by expression type and model, and the outputs are generally worse than expert renditions. Pronunciation correctness is reported at 87.5% overall, with category-dependent listener success.

**Limit:** The expressions, listeners, languages, LLMs, and five TTS systems define the scope; technical listeners and repeated playback may not represent ordinary users. Transcription and MOS remain proxies for mathematical comprehension, and no independent reproduction was performed.

#### Voices of `cyborg awesomeness': Posthuman embodiment of nonbinary gender expression in AI speech technologies

**Why this belongs:** Controllable synthetic voice features are evaluated as identity and embodiment choices for nonbinary users of speech-generating devices.

**Mechanism:** The study presents generated samples from controllable TTS and modified XTTSv2/MAGES systems to 12 nonbinary adults who use speech-generating devices. It measures F0, HNR, and acoustic vocal-tract length with Praat and combines close-ended responses with open-ended reflections.

**Mathematical/evaluation object:** Acoustic vocal-tract length is estimated from the third formant using aVTL = 34000/(2 times mean F3/2.5). The samples deliberately move controls by large standardized amounts; the survey counts preferences and gender affirmation rather than fitting a predictive model.

**Reported evidence:** Nine of 12 participants wanted breathiness control, 11 wanted vocal-tension control, all 12 wanted extreme vocal-tract-length control, and all 12 wanted the ability to blend two voices; nine found the MoreSecond blend gender-affirming.

**Limit:** There are 12 participants, deliberately extreme synthetic settings, and a qualitative/close-ended survey rather than a deployment study. Preferences are not a universal mapping from acoustic features to gender; results and interpretations are author-reported and were not independently reproduced.

#### Fine-Tuning Text-to-Speech Diffusion Models Using Reinforcement Learning with Human Feedback

**Why this belongs:** Diffusion-loss-regularized reward optimization improves naturalness without letting TTS drift from learned speech structure.

**Mechanism:** DLPO fine-tunes WaveGrad 2 with a reward combining UTMOS naturalness and the original diffusion loss, comparing DPOK, KLinR, and diffusion-only optimization.

**Mathematical/evaluation object:** DLPO reports UTMOS 3.65, NISQA 4.02, WER 1.0%, and 67% pairwise preference; these are different proxies, not one quality axis.

**Reported evidence:** The paper reports gains over the baseline and competing reward objectives, with listeners preferring samples 67% of the time.

**Limit:** The evidence uses WaveGrad 2 and selected reward predictors; predicted metrics and pairwise preference do not establish broad real-time deployment.

#### DiEmo-TTS: Disentangled Emotion Representations via Self-Supervised Distillation for Cross-Speaker Emotion Transfer in Text-to-Speech

**Why this belongs:** Disentangled emotion embeddings change delivery while protecting the target speaker's voice.

**Mechanism:** DiEmo-TTS clusters emotion attributes, matches speaker/emotion examples, distills representations, and uses a dual-conditioning transformer.

**Mathematical/evaluation object:** Naturalness, speaker similarity, emotion similarity, WER/CER, and embedding scores measure different goals; ablations remove distillation components.

**Reported evidence:** The reported system improves emotion and speaker-related measures in the chosen experiments.

**Limit:** Pretrained encoders, datasets, subjective measures, and cross-speaker coverage bound the conclusion.

#### Efficient Streaming TTS Acoustic Model with Depthwise RVQ Decoding Strategies in a Mamba Framework

**Why this belongs:** Depthwise codec decoding trades cross-level synthesis quality against streaming latency and model size.

**Mechanism:** SMAM is tested with MLM, INR, and no-MLM decoding in a zero-shot speaker-conditioned setup; CER, similarity, quality, real-time factor, latency, and listening scores separate tradeoffs.

**Mathematical/evaluation object:** MLM reports 26M parameters, CER 2.73, RTF 0.701, latency 0.065 s, MOS 4.02, and SMOS 3.36; INR uses 25M parameters and RTF 0.568 with latency 0.061 s.

**Reported evidence:** The proposed models are smaller and faster than listed non-streaming baselines while remaining competitive; removing MLM degrades quality measures.

**Limit:** Codec, datasets, hardware, and zero-shot speaker conditions bound the conclusion; other languages and devices are not established.

#### Facilitating Personalized TTS for Dysarthric Speakers Using Knowledge Anchoring and Curriculum Learning

**Why this belongs:** Teacher anchoring and curriculum learning adapt TTS to dysarthric speakers while separating identity retention from intelligibility.

**Mechanism:** A teacher-student knowledge-anchoring framework is evaluated across speaker groups with shortened audio.

**Mathematical/evaluation object:** PER measures intelligibility and speaker similarity measures identity; reported PER reaches 15.579 and similarity rises from 0.586 to 0.708.

**Reported evidence:** Curriculum and anchoring lower PER and improve speaker similarity across reported groups.

**Limit:** Groups, language, recording conditions, and reported metrics limit clinical claims.

#### Bridging the Training–Inference Gap in TTS: Training Strategies for Robust Generative Postprocessing for Low-Resource Speakers

**Why this belongs:** Generative postprocessing improves low-resource TTS naturalness while checking objective proxies against listener judgments.

**Mechanism:** Forward Tacotron features are refined by GAN and CFM postprocessors, then compared with listening and ranking tests.

**Mathematical/evaluation object:** Proposed CFM reaches objective distance 0.27; listener scores are 79.8 proposed CFM and 74.8 proposed GAN versus reference 98.3.

**Reported evidence:** Both proposed postprocessors improve reported naturalness; the CFM gain over its standard version is not significant.

**Limit:** Two speakers, ground-truth prosody in part of evaluation, selected data, and reported tests limit arbitrary-voice claims.

#### Non-Standard Accent TTS Support via Large Multi-Accent Frontend Pronunciation Knowledge Transfer

**Why this belongs:** The captured paper's ordinary problem, mechanism, and reported evaluation directly instantiate text-to-speech-planning within text-to-speech-and-content.

**Mechanism:** The frontend predicts phones, lexical stress, and prosodic boundaries; target accents are trained with reduced data and compared with full-data and single-accent baselines.

**Mathematical/evaluation object:** Accent similarity becomes a data-selection variable: transfer is not merely shared representation, but choosing a source whose pronunciation structure is useful for the target.

**Reported evidence:** The paper reports up to 95% less pronunciation training data for robust performance and examines 14 English accents using LibriTTS and HiFi-TTS-derived data.

**Limit:** Accuracy is reported for the studied accents, frontend labels, and datasets; transfer to other languages, voices, and synthesis backends remains unestablished.

#### Voice Impression Control in Zero-Shot TTS

**Why this belongs:** The official abstract and captured PDF identify a speech object and mechanism that instantiate style-and-emotion-control under prosody-and-interactive-control; the PDF now supports full-paper mechanism/evaluation notes, while this remains taxonomy membership rather than independent reproduction.

**Mechanism:** The method trains a control module around FastSpeech2, uses subjective ratings to estimate impression vectors, and uses a language model to turn descriptions into those vectors.

**Mathematical/evaluation object:** A generated utterance is judged on two axes: whether it preserves the reference speaker and whether the requested impression moves in the intended direction. The dimensions are correlated, so independent sliders are an approximation.

**Reported evidence:** Objective and subjective tests report effective single-dimension impression control and language-generated vectors that avoid manual optimization.

**Limit:** The evidence is limited to the selected impression dimensions, speakers, ratings, and TTS model; listener consistency and cross-language control are not established.

#### LombardTokenizer: Disentanglement and Control of Vocal Effort in a Neural Speech Codec

**Why this belongs:** Vocal effort is a controllable dimension of delivery; disentangling it from content and identity makes deliberate style change possible.

**Mechanism:** LombardTokenizer conditions the second quantization layer of SpeechTokenizer on vocal-effort encoders and tests neutral/Lombard conversion and synthesis quality.

**Mathematical/evaluation object:** Layer-wise discrete codes represent different information; conversion metrics and quality tests compare effort control, intelligibility, and naturalness.

**Reported evidence:** The paper reports better neutral-to-Lombard and Lombard-to-neutral conversion than existing methods while retaining synthesis quality.

**Limit:** The result is tied to the AVID/Lombard data, selected effort conditions, and codec; other speaking styles, languages, and independent listening tests remain open.

#### Private kNN-VC: Interpretable Anonymization of Converted Speech

**Why this belongs:** Private voice conversion tries to change speaker identity without requiring parallel recordings, making privacy and controllable identity part of the conversion problem.

**Mechanism:** The anonymizer changes duration and prosodic variation around phones; a recognition attack tests whether those factors predict identity.

**Mathematical/evaluation object:** Privacy is decomposed into leakage channels instead of one opaque score.

**Reported evidence:** The added components increase privacy in the tested attack, and target selection changes measured privacy.

**Limit:** Attack, target pool, language, utility metric, and prosody definitions bound the result; attack reduction is not anonymity.

#### Code Mix TTS: An Approach to Infer Human Like Speech for Multi-Lingual Input Texts

**Why this belongs:** Code-mixed text-to-speech must generate one coherent voice while switching languages, exposing the tension between linguistic content and stable vocal identity.

**Mechanism:** The proposed inference procedure sends multilingual input through an existing TTS system and evaluates generated code-mixed speech with automated MOS-style measures.

**Mathematical/evaluation object:** The central tradeoff is whether language-switch content is retained while synthesized audio remains natural; the paper uses automated quality scoring rather than a new training loss.

**Reported evidence:** The paper reports an approach for code-mix inference without extra data or fine-tuning; the preserved evidence does not establish broad human preference gains.

**Limit:** The paper's method and evaluation details are bounded by the selected TTS system, languages, and automated metric; human listening, pronunciation accuracy, and unseen language pairs remain open.

#### From Static to Dynamic: Enhancing AAC with Generative Imagery and Zero-Shot TTS

**Why this belongs:** Augmentative communication needs a voice that can be controlled quickly and personally, so generation quality is constrained by interaction time and user agency.

**Mechanism:** The proposed AAC system combines text-to-image generation with zero-shot TTS for children with autism.

**Mathematical/evaluation object:** The operative objects are symbol coverage, voice personalization, and eventual social validity; the captured paper does not report a completed comparative trial.

**Reported evidence:** The paper presents a broader expressive design but leaves long-term communication outcomes for future study.

**Limit:** No causal benefit or clinical efficacy should be inferred; user satisfaction, safety, cultural fit, and long-term adaptation remain open.

#### AF-Vocoder: Artifact-Free Neural Vocoder with Global Artifact Filter

**Why this belongs:** An artifact-free vocoder must reconstruct fine waveform detail without introducing audible periodic or transient artifacts that undermine naturalness.

**Mechanism:** AF-Vocoder inserts GAFilter into a GAN vocoder and tests reconstruction quality and artifact suppression across datasets and speakers.

**Mathematical/evaluation object:** The frequency filter is the intervention; reconstruction and artifact measures compare quality in-domain and for out-of-domain speakers.

**Reported evidence:** The paper reports better reconstruction quality and artifact suppression than other GAN vocoders.

**Limit:** Datasets, speaker coverage, artifacts, and listening protocol define the claim; real-time hardware cost and unseen languages remain open.

#### ZSDEVC: Zero-Shot Diffusion-based Emotional Voice Conversion with Disentangled Mechanism

**Why this belongs:** Zero-shot emotional conversion must infer a target voice and expressive state from little enrollment evidence, making identity/style separation the core problem.

**Mechanism:** Diffusion denoising reconstructs speech from a noisy latent while separate conditions guide emotion and speaker/content.

**Mathematical/evaluation object:** Disentanglement asks emotion to move while content and identity remain stable enough for a listener.

**Reported evidence:** The paper reports improved emotional accuracy and naturalness for unseen speakers across evaluated datasets.

**Limit:** Labels, speaker coverage, out-of-domain definition, protocol, and identity metrics bound transfer; conversion does not establish consent.

#### Accelerating Diffusion-based Text-to-Speech Model Trainingwith Dual Modality Alignment

**Why this belongs:** Dual-modality alignment gives diffusion TTS a shared text-and-speech target so linguistic content can guide waveform generation.

**Mechanism:** A-DMA aligns contextual text representations and discriminative speech features during diffusion TTS training, then compares convergence and synthesis quality with baselines.

**Mathematical/evaluation object:** Alignment reduces the mismatch between two representations before the generative process; convergence speed and output quality are separate objectives.

**Reported evidence:** The paper reports doubled convergence speed with better performance than its baselines.

**Limit:** The text/speech encoders, datasets, diffusion schedule, and quality measures bound the claim; hardware cost and new languages remain open.

#### Unsupervised Rhythm and Voice Conversion to Improve ASR on Dysarthric Speech

**Why this belongs:** Rhythm and voice conversion for dysarthric ASR changes delivery while trying to preserve the speaker's linguistic content.

**Mechanism:** RnV converts timing and voice characteristics without parallel healthy speech; syllable structure supplies a dysarthria-relevant rhythm representation before ASR scoring.

**Mathematical/evaluation object:** Conversion is a task-conditioned invariance: remove cues that obstruct recognition while retaining phonetic content needed by the recognizer.

**Reported evidence:** On Torgo, LF-MMI shows reported WER reductions, especially for severe dysarthria, while Whisper fine-tuning on converted data has minimal effect.

**Limit:** Torgo speakers, severity, conversion fidelity, ASR backend, and WER protocol bound transfer; improved recognition is not improved naturalness or clinical communication.

#### SOVA-Bench: Benchmarking the Speech Conversation Ability for LLM-based Voice Assistant

**Why this belongs:** A voice-assistant benchmark tests conversation ability as an interaction over turns, not just isolated speech recognition or response quality.

**Mechanism:** SOVA-Bench compares speech LLMs across comprehension and generated-speech dimensions, making acoustic quality an explicit evaluation target.

**Mathematical/evaluation object:** The benchmark separates what the assistant knows, what it understood, and how it sounded; no single score can substitute for those dimensions.

**Reported evidence:** The paper presents a systematic evaluation framework intended to guide speech-LLM voice interaction.

**Limit:** Benchmark tasks, prompts, listeners, model versions, and acoustic measures define the comparison; long-term interaction quality and user adaptation remain open.

#### Scheduled Interleaved Speech-Text Training for Speech-to-Speech Translation with LLMs

**Why this belongs:** Interleaving speech and text training for speech-to-speech translation couples linguistic planning with generated vocal output.

**Mechanism:** LLaMA3.2-1B is fine-tuned on CVSS with scheduled interleaving and evaluated across translation directions and resource levels.

**Mathematical/evaluation object:** The schedule is a curriculum over modalities: text provides a stable scaffold early, while speech units become responsible later; translation quality measures the endpoint.

**Reported evidence:** The paper reports consistent translation improvements, especially in limited-data languages.

**Limit:** CVSS, unitizer, schedule, model size, and languages bound the result; naturalness, speaker identity, and unseen domains need separate tests.

#### Prediction of listening effort ratings for habitual and clear-Lombard speech presented in noise

**Why this belongs:** Lombard speaking style changes when a person talks in noise, so generated or evaluated delivery must account for both vocal effort and listener effort.

**Mechanism:** HEGP is computed for habitual and clear-Lombard speech in noise; listening-effort ratings are modeled with spectral balance, F0, and rate measures.

**Mathematical/evaluation object:** The target is subjective effort, while HEGP is a release-from-masking proxy; regression tests whether style explains residual variance.

**Reported evidence:** HEGP predicts effort similarly across styles; wider F0 range and slower articulation are associated with lower effort, especially for habitual speech.

**Limit:** Noise, listener ratings, speech styles, and HEGP definition bound the result; individual strategy and real device conditions remain open.

#### Differentiable Reward Optimization for LLM based TTS system

**Why this belongs:** Reward optimization for TTS treats desired naturalness or style as a preference signal used to steer generated speech.

**Mechanism:** DiffRO predicts rewards for ASR, emotion, speech quality, age, and gender from generated codec tokens; a multi-task reward model supplies the signal and the language model is optimized without the full reinforcement-learning loop.

**Mathematical/evaluation object:** The method replaces a sampled discrete choice with a soft probability over codebook entries during training, so reward gradients can reach token probabilities; the reward is a proxy whose meaning depends on each downstream predictor.

**Reported evidence:** The paper reports improved pronunciation accuracy and state-of-the-art WER results, with controllability experiments for emotion, MOS, age, and gender; codec-level MOS and re-encoded audio reveal disagreement between proxy and waveform quality.

**Limit:** Reward-model accuracy, codec reconstruction, vocoder behavior, sampling, and listener perception bound the result; a differentiable proxy is not the same as human preference or end-to-end quality.

#### In This Environment, As That Speaker: A Text-Driven Framework for Multi-Attribute Speech Conversion

**Why this belongs:** Text prompts can request several speech attributes, but changing one attribute should not unintentionally change the others.

**Mechanism:** TES-VC uses synthetic data with decoupled vocal/environment features, a retrieval-based timbre-control module, and text descriptions for both target timbre and acoustic environment.

**Mathematical/evaluation object:** The desired output is a composition of content, speaker, and room factors; independent controls are tested by changing one description while holding the others fixed and measuring content retention and controllability.

**Reported evidence:** The paper reports effective text-driven control of timbre and environment with high content retention and results on in-domain and out-of-domain conditions.

**Limit:** Synthetic training mixtures, text descriptions, diffusion sampling, evaluation speakers and rooms, and the notion of controllability bound the result; independent factors are operational test dimensions, not guaranteed physical causes.

#### DS-Codec: Dual-Stage Training with Mirror-to-NonMirror Architecture Switching for Speech Codec

**Why this belongs:** A speech codec must compress a waveform into usable tokens and reconstruct it; mirror/non-mirror training targets reconstruction quality for TTS.

**Mechanism:** DS-Codec uses vector and product quantization with one 8,192-entry codebook, a downsampling encoder, recurrent/transformer decoder components, and time/frequency discriminators; ablations compare mirror and non-mirror stages.

**Mathematical/evaluation object:** Quantization maps a continuous latent vector to a nearby code; the staged architecture changes which parameters are allowed to adapt after the codebook has learned a stable partition, while reconstruction and perceptual metrics test the recovered waveform.

**Reported evidence:** The paper reports that mirror-stage training outperforms APCodec+ and the non-mirror alternatives on its objective measures, with lower reconstruction error and fewer training epochs/cost.

**Limit:** The speech data, bitrate/downsampling setting, discriminators, metrics, and baselines bound the result; reconstruction quality does not by itself prove usefulness for every TTS or speech-language-model task.

#### Neurodyne: Neural Pitch Manipulation with Representation Learning and Cycle-Consistency GAN

**Why this belongs:** Pitch manipulation must change the intended musical attribute while preserving the singer identity.

**Mechanism:** Neurodyne encodes speech while an adversary discourages pitch information in the latent; cycle-consistency trains conversion in both directions.

**Mathematical/evaluation object:** The representation must preserve identity/content while making pitch a controllable variable, and cycle consistency supplies a constraint when aligned pairs are absent.

**Reported evidence:** The paper reports improved global-key and template-based pitch manipulation over its compared methods.

**Limit:** Music data, pitch range, cycle assumptions, perceptual protocol, and content preservation bound transfer to conversational voice conversion.

#### Counterfactual Activation Editing for Post-hoc Prosody and Mispronunciation Correction in TTS Models

**Why this belongs:** Editing one prosodic or pronunciation attribute requires changing the relevant internal cause without regenerating unrelated speech properties.

**Mechanism:** Counterfactual Activation Editing modifies selected internal representations in a model-agnostic TTS system to alter prosodic features and correct mispronunciations; WER/PER, semantic similarity, and CMOS assess the tradeoff.

**Mathematical/evaluation object:** The edit asks what output would result if a hidden feature were moved toward a desired state while other activations stayed fixed; causal intervention, not retraining, is the key object.

**Reported evidence:** The paper reports lower WER and PER, preserved semantic similarity, and a 0.764-point CMOS improvement from correcting prosody and mispronunciation.

**Limit:** The chosen model, activation locations, correction targets, language, evaluation prompts, and listener panel bound the claim; an observed intervention effect does not prove a unique causal representation.

#### Spotlight-TTS: Spotlighting the Style via Voiced-Aware Style Extraction and Style Direction Adjustment for Expressive Text-to-Speech

**Why this belongs:** The title and preserved abstract identify a speech problem whose object and intended intervention fit style-and-emotion-control under prosody-and-interactive-control; the assignment does not claim performance beyond the available source.

**Mechanism:** Spotlight-TTS uses voiced-aware style extraction, continuity across speech regions, and style-direction adjustment, then compares expressive speech quality and transfer against baseline style-embedding systems.

**Mathematical/evaluation object:** The model treats style as a direction in a representation space rather than a fixed label; selecting voiced evidence and adjusting its direction are two separate controls on what gets transferred.

**Reported evidence:** The paper reports stronger expressiveness, overall speech quality, and style-transfer capability than its baselines in objective and perceptual evaluations.

**Limit:** Reference speakers, style labels, voiced-region detection, subjective ratings, and TTS architecture bound the result; a style direction is not a complete account of emotion, identity, or conversational appropriateness.

#### BitTTS: Highly Compact Text-to-Speech Using 1.58-bit Quantization and Weight Indexing

**Why this belongs:** The preserved abstract identifies a speech object and bounded intervention that instantiate neural-vocoder under text-to-speech-and-content; this upgrades a provisional candidate to analyst-reviewed taxonomy membership only.

**Mechanism:** BitTTS uses quantization-aware training down to 1.58-bit, with most weights represented as -1, 0, or 1, and weight indexing that stores groups as int8 indices for on-device use.

**Mathematical/evaluation object:** Quantization replaces a continuous parameter with a small codebook; training under that constraint lets the model adapt, while model size and synthesis quality measure the deployment tradeoff.

**Reported evidence:** The paper reports an 83% reduction in model size and better synthesis quality than a similar-size unquantized baseline.

**Limit:** Hardware, model architecture, bitrate/precision, speech data, and quality metrics bound the result; smaller storage does not automatically mean lower latency or energy on every device.

#### Mitigating Non-Target Speaker Bias in Guided Speaker Embedding

**Why this belongs:** Guided speaker embeddings must target the intended voice without letting non-target speakers in the mixture bias the identity representation.

**Mechanism:** The paper diagnoses the failure in guided speaker embeddings and modifies global-statistics modules to condition their pooling on target activity, then evaluates speaker verification in low- and high-overlap conditions.

**Mathematical/evaluation object:** Pooling is a weighted estimate of speaker identity; changing the support of that estimate changes which voice contributes, so overlap robustness and ordinary-case preservation can be measured separately.

**Reported evidence:** The proposed activity-aware statistics improve speaker verification under severe overlap while reducing the degradation seen in low-overlap cases.

**Limit:** Activity labels, overlap ratios, pooling design, speaker-verification protocol, and evaluation speakers bound the claim; improvement against this overlap pattern does not prove robustness to every diarization or adversarial error.

#### Revival with Voice: Multi-modal Controllable Text-to-Speech Synthesis

**Why this belongs:** The system maps face and natural-language controls into speech while addressing low-quality audio-visual training data.

**Mechanism:** The face encoder supplies speaker or voice information, while text conditioning specifies controllable attributes; multi-modal training aligns these conditions with waveform generation.

**Mathematical/evaluation object:** The system treats identity and controllable acoustic attributes as separate but compositional conditioning variables, evaluated through speech quality, similarity, and control-following tests.

**Reported evidence:** Revival with Voice reports controllable synthesis from real and artistic face inputs and improved use of high-quality audio-only data in the tested settings.

**Limit:** Face distribution, language, control wording, subjective protocol, and disentanglement assumptions limit the claim; controllability is not proof of identity fidelity or safe use of a person's likeness.

#### DAFMSVC: One-Shot Singing Voice Conversion with Dual Attention Mechanism and Flow Matching

**Why this belongs:** Singing voice conversion must change timbre while preserving melody and lyrics; dual attention and flow matching target that separation.

**Mechanism:** DAFMSVC uses target-feature retrieval to reduce timbre leakage, dual cross-attention for adaptive fusion, and a flow-matching generator for one-shot singing voice conversion.

**Mathematical/evaluation object:** The system treats conversion as constrained substitution: target timbre evidence replaces identity-bearing content while melody and lyrics remain conditions; timbre similarity, content accuracy, and quality expose leakage and distortion.

**Reported evidence:** The paper reports improved target-timbre similarity and generated-audio quality over comparison methods in one-shot singing conversion experiments.

**Limit:** Singer, song, target-reference duration, feature retrieval, evaluation metrics, and dataset splits bound the result; one-shot similarity does not prove perfect disentanglement or generalization to every unseen singer.

#### Analyzing Mitigation Strategies for Catastrophic Forgetting in End-to-End Training of Spoken Language Models

**Why this belongs:** A spoken-language model must learn new tasks without forgetting earlier speech capabilities when it is trained end to end.

**Mechanism:** The study evaluates forgetting-mitigation strategies for end-to-end training of spoken language models.

**Mathematical/evaluation object:** The core tradeoff is retention versus adaptation: an update is useful only if it improves the new task without erasing previously learned speech-language behavior.

**Reported evidence:** The paper reports comparative forgetting and adaptation results across the tested strategies.

**Limit:** Tasks, training order, model size, data mixture, and retention metrics bound the conclusions; results do not establish lifelong learning in open deployment.

#### LSCodec: Low-Bitrate and Speaker-Decoupled Discrete Speech Codec

**Why this belongs:** A low-bitrate codec tries to keep what was said separate from who said it, so rate reduction does not destroy controllable speaker identity.

**Mechanism:** LSCodec targets low-bitrate, speaker-decoupled discrete speech coding for controllable reconstruction or conversion.

**Mathematical/evaluation object:** The code is a bottleneck with a division of labor: linguistic/acoustic content crosses the bottleneck, while speaker identity is supplied separately at decoding.

**Reported evidence:** The paper reports low-bitrate codec and speaker-decoupling results on its reconstruction/conversion evaluations.

**Limit:** Bitrate, speaker set, decoder, datasets, and disentanglement tests bound the claim; identity leakage can remain outside the tested conditions.

#### VibE-SVC: Vibrato Extraction with High-frequency F0 Contour for Singing Voice Conversion

**Why this belongs:** Singing voice conversion extracts high-frequency pitch movement so the target voice can change without losing expressive vibrato.

**Mechanism:** VibE-SVC extracts vibrato from the high-frequency F0 contour for controllable singing voice conversion.

**Mathematical/evaluation object:** Style becomes an editable signal component: the system changes a time-varying pitch pattern while preserving the slower melody and speaker identity.

**Reported evidence:** The paper reports objective and subjective evidence for high-quality conversion, style control, and speaker similarity.

**Limit:** Singers, songs, vibrato ranges, extraction errors, and evaluation conditions limit generalization; explicit control does not guarantee a preferred artistic result.

#### DnR-nonverbal: Cinematic Audio Source Separation DatasetContaining Non-Verbal Sounds

**Why this belongs:** A cinematic nonverbal-sound corpus broadens generation beyond words and asks what data are needed to model meaningful vocal and environmental events.

**Mechanism:** DnR-nonverbal is a cinematic audio source-separation dataset containing laughter, screams, and other nonverbal sounds in the speech stem.

**Mathematical/evaluation object:** The dataset changes the category definition presented to the model: the target is a vocal event in context, not a narrow phonetic transcript.

**Reported evidence:** The paper reports that conventional separators mishandle nonverbal sounds and that the new dataset improves the tested synthetic separation task.

**Limit:** Synthetic mixtures, labels, scene distribution, separator, and nonverbal taxonomy bound the result; real-film generalization remains open.

#### Zero-Shot Mono-to-Binaural Speech Synthesis

**Why this belongs:** The preserved abstract identifies a speech object and bounded intervention that instantiate interactive-latency under prosody-and-interactive-control; this upgrades a provisional candidate to analyst-reviewed taxonomy membership only.

**Mechanism:** The paper studies zero-shot mono-to-binaural speech synthesis.

**Mathematical/evaluation object:** Spatialization is a structured transformation: linguistic content should remain common across channels while timing and spectral differences encode position and acoustic scene.

**Reported evidence:** The paper reports objective and perceptual results for zero-shot mono-to-binaural synthesis.

**Limit:** Room and position range, speaker diversity, spatial labels, head-related filtering, and listening protocol bound generalization; stereo plausibility is not physical localization accuracy.

#### EME-TTS: Unlocking the Emphasis and Emotion Link in Speech Synthesis

**Why this belongs:** Speech synthesis must coordinate emphasis and emotion because changing one can unintentionally alter the other.

**Mechanism:** EME-TTS targets the emphasis-emotion link in speech synthesis.

**Mathematical/evaluation object:** Expressive synthesis is a constrained coordination problem: emphasis is local and linguistic, emotion is broader and affective, and the system must make their interaction coherent.

**Reported evidence:** The paper reports expressive TTS quality and controllability for emphasis and emotion in the tested evaluations.

**Limit:** Languages, speakers, labels, text prompts, control ranges, and subjective raters bound the claim; controllability does not guarantee natural or culturally appropriate expression.

#### SA-RAS: Speaker-Aware Style Retrieval Augmented Generation for Expressive Zero-Shot Text-to-Speech Synthesis

**Why this belongs:** Expressive zero-shot TTS retrieves speaker and style evidence so an unseen voice can be controlled from references.

**Mechanism:** SA-RAS is a speaker-aware style retrieval-augmented method for expressive zero-shot TTS.

**Mathematical/evaluation object:** Style retrieval is constrained by identity: the reference supplies how to speak, while the target speaker supplies who speaks, and generation must keep those roles distinct.

**Reported evidence:** The paper reports expressive quality, speaker similarity, and style-control results for zero-shot synthesis.

**Limit:** Reference selection, speaker set, style labels, prompts, listening tests, and language bound the claim; style similarity is not a complete account of naturalness.

#### Accelerating Autoregressive Speech Synthesis Inference With Speech Speculative Decoding

**Why this belongs:** The preserved abstract identifies a speech object and bounded intervention that instantiate interactive-latency under prosody-and-interactive-control; this upgrades a provisional candidate to analyst-reviewed taxonomy membership only.

**Mechanism:** The paper accelerates autoregressive speech-synthesis inference with speech speculative decoding.

**Mathematical/evaluation object:** Speed comes from parallel verification rather than changing the target distribution blindly: accepted blocks preserve the large model's decisions while reducing serial work.

**Reported evidence:** The paper reports inference-speed gains and quality behavior for speculative speech decoding.

**Limit:** Tokenization, proposal model, acceptance rate, hardware, speaker/style, and latency measurement bound the result; speedups vary with the workload.

#### Towards Emotionally Consistent Text-Based Speech Editing: Introducing EmoCorrector and The ECD-TSE Dataset

**Why this belongs:** The preserved abstract identifies a speech object and bounded intervention that instantiate style-and-emotion-control under prosody-and-interactive-control; this upgrades a provisional candidate to analyst-reviewed taxonomy membership only.

**Mechanism:** EmoCorrector and the ECD-TSE dataset target emotionally consistent text-based speech editing.

**Mathematical/evaluation object:** Editing has two invariants: linguistic content must change as requested, while speaker identity and emotional trajectory must remain coherent around the change.

**Reported evidence:** The paper reports dataset and model results for emotionally consistent speech editing.

**Limit:** Emotion labels, edit types, speakers, context, synthesis model, and perceptual evaluation bound the claim; emotional consistency is listener- and culture-dependent.

#### Investigating Stochastic Methods for Prosody Modeling in Speech Synthesis

**Why this belongs:** Stochastic prosody modeling treats speaking style as a distribution of possible timing and pitch patterns rather than one fixed trajectory.

**Mechanism:** The paper investigates stochastic methods for prosody modeling in speech synthesis.

**Mathematical/evaluation object:** Prosody is a conditional distribution, not one correct curve: a useful model samples plausible timing and pitch while remaining anchored to linguistic content.

**Reported evidence:** The paper reports stochastic prosody-modeling behavior and synthesis evaluations for the tested methods.

**Limit:** Text, speakers, sampling temperature, prosody labels, raters, and metrics bound the claim; diversity alone is not expressive control.

#### Unleashing   the  Inner Monster: Demonstrating High-Fidelity Human to Non-Human  Voice Conversion

**Why this belongs:** Human-to-non-human voice conversion changes identity and vocal character while attempting to retain a recognizable utterance.

**Mechanism:** The paper demonstrates high-fidelity human-to-non-human voice conversion for games.

**Mathematical/evaluation object:** Voice conversion can be reframed as changing the sound-producing agent, not merely swapping one human identity for another; the target is a designed acoustic character.

**Reported evidence:** The paper reports real-time conversion and high-quality generated monster sounds in its selected game-oriented conditions.

**Limit:** Target creatures, recordings, real-time hardware, perceptual evaluation, and controllability bound the claim; a convincing effect is not a biological model of animal vocalization.

#### Vocoder-Projected Feature Discriminator

**Why this belongs:** A vocoder discriminator should judge the acoustic detail that a TTS or voice-conversion system actually needs to reconstruct.

**Mechanism:** The vocoder-projected feature discriminator compares feature representations after synthesis; diffusion-based voice-conversion distillation tests whether the adversarial target improves the generated waveform.

**Mathematical/evaluation object:** The discriminator changes the metric space rather than the generator's output target: it seeks features that preserve vocoder-relevant waveform distinctions while avoiding repeated raw-waveform processing.

**Reported evidence:** The paper reports improved diffusion-based VC distillation quality from the projected-feature discriminator under the evaluated settings.

**Limit:** Vocoder choice, feature projection, training compute, VC data, and perceptual evaluation determine the result; a reported quality gain does not establish universal TTS or VC superiority.

#### Long-Context Speech Synthesis with Context-Aware Memory

**Why this belongs:** Long-form TTS must carry information across an utterance while keeping local pronunciation and prosody coherent.

**Mechanism:** The context-aware memory retrieves and updates paragraph information; local details and long-term style guide each sentence, while prefix tokens supply in-context information without unrestricted future leakage.

**Mathematical/evaluation object:** The system separates memory access from waveform generation, trading a bounded context representation for coherence and lower context-inference cost.

**Reported evidence:** The model outperforms the reported baselines on paragraph-level prosody expressiveness, coherence, and context-inference cost.

**Limit:** Text genre, speaker/style conditioning, subjective measures, memory capacity, and paragraph length bound transfer; coherence scores do not prove human preference in broad long-form use.

#### SpeechSEC: A Unified Multi-Task Framework for Speech Synthesis, Editing, and Continuation

**Why this belongs:** The title and preserved abstract identify a speech object and bounded intervention that instantiate text-to-speech-planning under text-to-speech-and-content; this resolves taxonomy membership only.

**Mechanism:** The model dynamically changes conditioning for each task and remains compatible with multiple speech discretizers such as HuBERT, DAC, and SpeechTokenizer.

**Mathematical/evaluation object:** A shared representation is treated as a reusable coordinate system for several transformations; voice preservation and audio quality test whether task sharing retains the right invariants.

**Reported evidence:** SpeechSEC reports MOS-like audio quality of 4.20 versus 4.00 and voice preservation of 0.72 versus 0.58 for synthesis, with usable editing and continuation results.

**Limit:** Reported scores, codec choice, task mixture, prompts, speakers, and sample protocol bound the comparison; multi-task compatibility is not proof of editing safety or continuity in arbitrary audio.

#### Vo-Ve: An Explainable Voice-Vector for Speaker Identity Evaluation

**Why this belongs:** The title and preserved abstract identify a speech problem whose object and intended intervention fit speaker-identity under voice-identity-and-conversion; the assignment does not claim performance beyond the available source.

**Mechanism:** Vo-Ve maps speech to attribute probabilities; similarity can then be decomposed into human-readable properties instead of a single latent distance.

**Mathematical/evaluation object:** The representation trades some compact opacity for an interpretable coordinate system whose attributes can be inspected when similarity changes.

**Reported evidence:** The paper reports competitive speaker-similarity evaluation and attribute-level explanations in its experiments.

**Limit:** Attribute inventory, labels, language, channel variation, and metric protocol bound interpretability; explainable similarity is not proof of causal identity factors.

#### RapFlow-TTS: Rapid and High-Fidelity Text-to-Speech with Improved Consistency Flow Matching

**Why this belongs:** Rapid TTS uses a consistency-constrained flow to trade fewer inference steps against acoustic fidelity.

**Mechanism:** The model learns that velocity predictions at different time points agree along the transport path; consistency allows few-step integration while adversarial and acoustic losses protect waveform quality.

**Mathematical/evaluation object:** Consistency regularization turns a generation trajectory into a reusable shortcut: nearby time intervals should imply compatible updates.

**Reported evidence:** The paper reports high-fidelity synthesis with fewer generation steps than compared flow/diffusion systems.

**Limit:** Text/speaker data, subjective protocol, step counts, vocoder and hardware, and adversarial stability bound the speed-quality claim; fewer steps do not guarantee lower end-to-end latency.

#### Eigenvoice Synthesis based on Model Editing for Speaker Generation

**Why this belongs:** The title and preserved abstract identify a speech object and bounded intervention that instantiate zero-shot-voice under voice-identity-and-conversion; this resolves taxonomy membership only.

**Mechanism:** Model-difference directions act as speaker basis vectors; adding sampled combinations to a base model changes identity while retaining the learned text-to-speech mapping.

**Mathematical/evaluation object:** The speaker manifold can be represented by low-dimensional directions in parameter space rather than only by an input speaker vector.

**Reported evidence:** The paper reports diverse generated voices and compares parameter-space eigenvoice synthesis with prior speaker-generation approaches.

**Limit:** Validity of sampled parameters, diversity and naturalness criteria, speaker-identification protocol, base model, and absence of reference audio bound the claim; generated identity is not evidence of a real person.

#### Tungnaá In Live Performance: An Implementation Of Interactive Artistic Text-To-Voice

**Why this belongs:** The title and preserved abstract identify a speech object and bounded intervention that instantiate text-to-speech-planning under text-to-speech-and-content; this resolves taxonomy membership only.

**Mechanism:** The system separates alignment/generation into streaming components, buffers a small number of frames to trade latency for stability, and keeps the interface in a separate process.

**Mathematical/evaluation object:** Deployment constraints become part of the speech representation and evaluation: latency, controllability, and small-data adaptation matter alongside audio quality.

**Reported evidence:** The demonstration reports real-time inference with worst-case latency below 100 ms and a bespoke performance dataset/application.

**Limit:** Demonstration scope, artist-specific data, reduced phonetic alphabet, hardware, subjective quality, and no controlled comparison bound generalization; live usability is not a standard TTS benchmark.

#### Improving Noise Robustness of LLM-based Zero-shot TTS via Discrete Acoustic Token Denoising

**Why this belongs:** The preserved abstract identifies a speech object and bounded intervention that instantiate text-to-speech-planning under text-to-speech-and-content; this upgrades a provisional candidate to analyst-reviewed taxonomy membership only.

**Mechanism:** The token denoiser predicts clean coarse tokens; an embedding refiner and codec decoder reconstruct usable acoustic evidence before the zero-shot TTS model conditions generation.

**Mathematical/evaluation object:** Denoising at the representation used for prompting aligns the cleanup objective with the generator’s actual conditioning interface.

**Reported evidence:** The paper reports that its codec denoiser outperforms speech-enhancement baselines and that noise-robust LauraTTS improves over adding an external enhancer.

**Limit:** Noise types, prompt duration, speaker overlap, codec/model version, and zero-shot evaluation bound transfer; clean synthesis from a prompt is not speaker-authenticated identity preservation.

#### Training-Free Voice Conversion with Factorized Optimal Transport

**Why this belongs:** The title and preserved abstract identify a speech object and bounded intervention that instantiate voice-conversion under voice-identity-and-conversion; this resolves taxonomy membership only.

**Mechanism:** Monge–Kantorovich linear transport aligns source and target feature distributions; factorization normalizes unequal variances before the encoder-converter-vocoder reconstructs speech.

**Mathematical/evaluation object:** Optimal transport matches distributions rather than individual frames, allowing sparse reference evidence to define a target voice without storing a lookup for every source sound.

**Reported evidence:** MKL-VC reports improved content preservation and short-reference robustness on LibriSpeech and FLEURS, with cross-lingual performance comparable to FACodec.

**Limit:** Reference duration, WavLM space, languages, vocoder, speaker similarity metric, and implementation choices bound transfer; content preservation does not prove perfect identity conversion.

#### LinearVC: Linear Transformations of Self-Supervised Features Through the Lens of Voice Conversion

**Why this belongs:** The captured official PDF and abstract identify a speech object and mechanism instantiating voice-conversion under voice-identity-and-conversion; this upgrades evidence depth for the structured note and does not establish independent reproduction.

**Mechanism:** A learned transformation maps representation distributions toward a target voice while retaining content-related structure.

**Mathematical/evaluation object:** Conversion is a representation-space mapping: content preservation and target identity are competing constraints.

**Reported evidence:** The paper reports LinearVC results through the lens of self-supervised feature transformations.

**Limit:** Feature model, languages, target data, similarity/content metrics, and transform assumptions bound transfer.

### Synthesis boundary

These papers share a conceptual pressure, but this seed batch does not justify ranking methods, estimating prevalence, or claiming that the mechanism generalizes across speakers, languages, rooms, or tasks. Those claims require additional assignments and comparable denominators.

## Speakers as changing people, not nuisance variables

**Ordinary pressure:** Voice depends on anatomy, age, health, emotion, language history, social setting, and equipment; these differences affect both communication and measurement.

**Naive strategy that breaks:** Treating variation as noise makes systems work best for a narrow population and can turn a health or identity signal into an unwanted demographic shortcut.

**Recurring move:** Measure which variation is task-relevant, model it explicitly when appropriate, and test performance and meaning across people and conditions.

**Boundary:** A factor that helps prediction may be sensitive, confounded, or harmful to expose; personalization can improve access while increasing privacy risk.

**D3 evidence status:** 56 reviewed paper(s); the family claim below is limited to these examples.

**Conceptual family represented:** `human-centered-accessibility/listener-effort`, `clinical-markers/clinical-speech-marker`, `clinical-markers/clinical-speech-marker`, `atypical-and-assistive-speech/dysarthria-and-atypical-speech`, `clinical-markers/clinical-speech-marker`, `human-centered-accessibility/accessibility-fit`, `human-centered-accessibility/listener-effort`, `identity-and-life-stage/speaker-verification`, `atypical-and-assistive-speech/augmentative-communication`, `clinical-markers/clinical-speech-marker`, `identity-and-life-stage/speaker-verification`, `identity-and-life-stage/style-and-state-variation`, `identity-and-life-stage/speaker-verification`, `clinical-markers/clinical-speech-marker`, `human-centered-accessibility/listener-effort`, `identity-and-life-stage/style-and-state-variation`, `clinical-markers/clinical-speech-marker`, `human-centered-accessibility/user-control-and-consent`, `identity-and-life-stage/age-and-development`, `clinical-markers/clinical-speech-marker`, `human-centered-accessibility/accessibility-fit`, `identity-and-life-stage/speaker-verification`, `atypical-and-assistive-speech/augmentative-communication`, `human-centered-accessibility/listener-effort`, `clinical-markers/clinical-speech-marker`, `identity-and-life-stage/age-and-development`, `atypical-and-assistive-speech/augmentative-communication`, `atypical-and-assistive-speech/dysarthria-and-atypical-speech`, `atypical-and-assistive-speech/augmentative-communication`, `clinical-markers/clinical-speech-marker`, `human-centered-accessibility/listener-effort`, `identity-and-life-stage/speaker-verification`, `human-centered-accessibility/accessibility-fit`, `identity-and-life-stage/speaker-verification`, `human-centered-accessibility/accessibility-fit`, `identity-and-life-stage/age-and-development`, `human-centered-accessibility/user-control-and-consent`, `identity-and-life-stage/speaker-verification`, `atypical-and-assistive-speech/dysarthria-and-atypical-speech`, `identity-and-life-stage/age-and-development`, `clinical-markers/clinical-speech-marker`, `identity-and-life-stage/speaker-verification`, `atypical-and-assistive-speech/dysarthria-and-atypical-speech`, `atypical-and-assistive-speech/dysarthria-and-atypical-speech`, `human-centered-accessibility/listener-effort`, `human-centered-accessibility/accessibility-fit`, `human-centered-accessibility/accessibility-fit`, `human-centered-accessibility/accessibility-fit`, `identity-and-life-stage/speaker-verification`, `identity-and-life-stage/speaker-verification`, `human-centered-accessibility/accessibility-fit`, `human-centered-accessibility/listener-effort`, `identity-and-life-stage/age-and-development`, `identity-and-life-stage/speaker-verification`, `human-centered-accessibility/listener-effort`, `human-centered-accessibility/accessibility-fit`.

### What the papers make concrete

#### giraldo25_interspeech

**Why this belongs:** The paper compares enhancement on multilingual crowdsourced speech and measures content retention and information loss across people; the evaluation target is human-useful recovery, not only a signal score.

**Mechanism:** Quality, intelligibility, word error, and phoneme error measures are compared across demographic and language conditions; samples with high WER are examined for information loss.

**Mathematical/evaluation object:** PESQ-like quality scores and WER can disagree; this exposes the tradeoff between perceptual quality and preserved linguistic content.

**Reported evidence:** The paper reports performance variation across demographics/languages and warns that model rankings on VoiceBank-DEMAND do not transfer directly.

**Limit:** The authors still note benchmark simplification and possible metric overfitting; dataset diversity does not by itself prove universal fairness.

#### Subtyping Speech Errors in Childhood Speech Sound Disorders with Acoustic-to-Articulatory Speech Inversion

**Why this belongs:** The paper uses acoustic-to-articulatory inversion to distinguish clinically meaningful speech-sound error subtypes.

**Mechanism:** The study compares inverted articulatory trajectories for correct and erroneous /r/ and /s/ productions in children with speech sound disorders, models repeated observations with linear mixed effects, and asks which tract variables differ between perceptually defined subtypes.

**Mathematical/evaluation object:** The inversion maps acoustics to estimated articulator variables; linear mixed modeling separates subtype effects from repeated-speaker and item variation. Statistical significance is evidence of group differences, not proof that the inversion recovered physical motion exactly.

**Reported evidence:** The paper reports statistically significant articulatory differences among several perceptually salient /r/ and /s/ error subtypes and correct targets in American English.

**Limit:** The study is limited to selected American-English child error types and an inversion model; clinical interpretability is demonstrated for these comparisons, not established for all disorders or speakers. No independent reproduction was performed.

#### ADCeleb: A Longitudinal Speech Dataset from Public Figures for Early Detection of Alzheimer’s Disease

**Why this belongs:** Longitudinal public speech and speaker-disjoint evaluation test whether acoustic and linguistic changes near diagnosis can be separated from recording and person effects.

**Mechanism:** ADCeleb contains public spontaneous recordings from 40 people with AD and 40 controls, with intervals two and one years before diagnosis. Acoustic embeddings include x-vectors, TRILLsson, Wav2Vec2, HuBERT, and Whisper; linguistic embeddings include multilingual encoders. PCA and PLDA classify speakers, and selected acoustic/linguistic predictions are averaged.

**Mathematical/evaluation object:** The evaluation is speaker-level nested 10-fold cross-validation with accuracy, F1, sensitivity, specificity, and AUC. Wav2Vec2 acoustic accuracy is 0.67 and 0.72 at the two intervals; the best linguistic models reach 0.73 and 0.75; fusion reaches 0.80 at the nearer interval.

**Reported evidence:** The authors report that linguistic representations are stronger earlier, while acoustic information contributes more near the year of diagnosis; fusion improves the nearer interval to 0.80 accuracy.

**Limit:** The corpus uses public figures, YouTube recordings, 40 AD and 40 control speakers, and imperfect observational labels. It is a dataset and baseline study, not a clinical diagnostic validation; author-reported results were not independently reproduced.

#### Pathology-Aware Speech Encoding and Data Augmentation for Dysarthric Speech Recognition

**Why this belongs:** Pathology-aware representations and targeted data address systematic production differences rather than generic noise.

**Mechanism:** A BEST-RQ Conformer is continued on pathological speech; fine-tuning compares synthetic, out-of-domain, and transcript-embedding-selected data, with similarity losses.

**Mathematical/evaluation object:** Overall WER is 19.73 versus 22.73 for the BEST-RQ baseline; 150% OOD augmentation reaches 17.32 and similarity-weighted pairing 17.81, while Down syndrome does not benefit from augmentation.

**Reported evidence:** The authors report 13.2% relative WER improvement from pathology-aware pre-training, up to 8.7% from synthetic data, 12.2% from OOD data, and 9.7% from semantic selection.

**Limit:** Etiologies, corpora, similarity model, and ratios bound the claim; improvements differ by condition and synthetic speech may not preserve clinical variation.

#### Acoustic and Linguistic Biomarkers for Cognitive Impairment Detection from Speech

**Why this belongs:** Class-aware acoustic and linguistic ensembles test cognitive-decline signals while exposing clinical data imbalance.

**Mechanism:** PROCESS Challenge systems combine acoustic features, text features, LLM descriptors, Longformer, ECAPA-TDNN, and TRILLsson embeddings across three tasks.

**Mathematical/evaluation object:** The study emphasizes UAF1 and class-specific F1 rather than accuracy alone.

**Reported evidence:** Selected ensembles provide the strongest reported balance across train/development data and individual classes.

**Limit:** Challenge data, demographic overlap, and missing metadata limit the claim; this is not clinical validation.

#### Can ASR generate valid measures of child reading fluency?

**Why this belongs:** ASR-derived child reading measures are checked against human-transcript measures to test whether automation preserves the educational construct.

**Mechanism:** The study evaluates 244 recordings from 131 Dutch children aged 6–13, compares four ASR systems, and correlates automatic and human-derived fluency measures.

**Mathematical/evaluation object:** WER, timing F1, and Pearson correlations quantify separate links from audio to educational measure; 12 of 15 measures show strong correlations.

**Reported evidence:** The best reported system has WER 12.3% and timing F1 0.82; twelve measures meet r ≥ 0.7.

**Limit:** Dutch child reading, fixed texts, age distribution, ASR choice, and transcript comparison limit generalization; intervention or diagnosis validity is not established.

#### Hearing deficits of transformer-based ASR for anechoic and spatial signals

**Why this belongs:** Speech-reception thresholds compare ASR and human recognition under hearing-relevant noise and spatial conditions.

**Mechanism:** Whisper models are tested on anechoic and spatial signals; thresholds come from WER curves at 50% error.

**Mathematical/evaluation object:** SRT and psychometric slope make the human-machine gap explicit rather than hiding it in average WER.

**Reported evidence:** Model size improves ASR thresholds, but the gap changes with language, room, and spatial signals.

**Limit:** Whisper versions, German/English material, steady noise, and laboratory setup limit claims.

#### Unified Text and Speaker Verification using SSL model for Text-Dependent Speaker Verification

**Why this belongs:** A unified self-supervised representation separates lexical validation from speaker identity across text-dependent and independent trials.

**Mechanism:** The student preserves lexical information for text validation while a speaker backend supplies identity evidence; DeepMine and VoxCeleb1 test both modes.

**Mathematical/evaluation object:** English DeepMine TD-SV tandem EER is 3.46% versus 4.28% baseline; VoxCeleb1 TI-SV is 1.29% versus 0.49%, exposing a tradeoff.

**Reported evidence:** The student improves reported text-dependent and DeepMine results but degrades VoxCeleb1 text-independent results relative to ReDimNet.

**Limit:** Datasets, languages, content, thresholds, and reported EERs bound the conclusion; open-set deployment is unestablished.

#### A Silent Speech Decoding System from EEG and EMG with Heterogenous Electrode Configurations

**Why this belongs:** Silent-speech decoding treats heterogeneous EEG/EMG sensing and patient transfer as central to assistive communication.

**Mechanism:** A shared model learns from varying EEG/EMG layouts while multitask objectives stabilize word classification across speakers and languages.

**Mathematical/evaluation object:** Word classification accuracy measures whether neural signals preserve enough information for decoding.

**Reported evidence:** Accuracy is 95.3% for healthy participants and 54.5% for a patient, versus 70.1% and 13.2% for single-subject baselines.

**Limit:** Patient count, setup, calibration, and author-reported results limit clinical deployment claims.

#### Pitfalls and Limits in Automatic Dementia Assessment

**Why this belongs:** The captured paper's ordinary problem, mechanism, and reported evaluation directly instantiate clinical-speech-marker within clinical-and-assistive-speech.

**Mechanism:** The analysis links scoring artifacts to speech production decline, ASR errors, and fallback handling; apparent agreement can therefore arise from the test design.

**Mathematical/evaluation object:** The paper turns evaluation from a single correlation into a chain of measurement decisions whose errors can favor particular groups.

**Reported evidence:** The paper reports high overall correlation but weaker behavior for healthy and mildly impaired groups and identifies overoptimistic correlations for severely impaired speakers.

**Limit:** This is an analysis of one standardized assessment and its data; it warns against clinical claims, not a universal ranking of dementia-screening systems.

#### An Investigative Study on Recent Sharpness- and Flatness-Based Optimizers for Enhanced Self-Supervised Speaker Verification

**Why this belongs:** The captured paper directly studies how training and optimization affect verification of speaker identity under changed conditions.

**Mechanism:** The study trains supervised and self-supervised speaker-verification systems with ADOPT, AdEMAMix, SAM, ASAM, GAM, and GSAM, then tests weight decay, exponential moving averages, and SWITCH EMA. The comparison asks whether flatter or better-conditioned solutions improve verification generalization without adding an inference-time identity module.

**Mathematical/evaluation object:** The verification decision compares an enrollment and test embedding, while the training choices change the parameter update. Sharpness-aware methods add a local worst-case loss perturbation so a solution is rewarded for remaining good in a neighborhood; EER and minDCF summarize threshold errors rather than directly measuring identity invariance.

**Reported evidence:** The paper reports that optimizer choice materially changes generalization and that the tested sharpness-aware and general-purpose optimizers can reach state-of-the-art self-supervised speaker-verification results in its experiments.

**Limit:** The conclusions are bounded by the selected speaker-verification corpora, architectures, optimizer settings, and author-reported comparisons; a better optimizer score does not establish robustness to every language, channel, attack, or demographic group. No independent reproduction was performed.

#### Inter-Speaker Relative Cues for Text-Guided Target Speech Extraction

**Why this belongs:** The official abstract and captured PDF identify a speech object and mechanism that instantiate style-and-state-variation under speaker-characteristics; the PDF now supports full-paper mechanism/evaluation notes, while this remains taxonomy membership rather than independent reproduction.

**Mechanism:** Two-speaker mixtures are built across five languages with cues for language, gender, emotion, order, age, rate, duration, pitch, loudness, and distance; prompts identify the target by those relations.

**Mathematical/evaluation object:** The central object is not a speaker label but a relation between two signals. Extraction quality is measured after the text selects one member of the mixture.

**Reported evidence:** The paper reports that all relative cues beat random subsets, with gender and temporal order especially robust across languages and reverberation; WavLM/CNN initialization improves the baseline.

**Limit:** The claim is bounded to the constructed mixtures, cue templates, languages, and author-reported tests; real conversational mixtures and privacy effects remain open.

#### PAEFF: Precise Alignment and Enhanced Gated Feature Fusion for Face-Voice Association

**Why this belongs:** The official abstract and captured PDF identify a speech object and mechanism that instantiate speaker-verification under speaker-characteristics; the PDF now supports full-paper mechanism/evaluation notes, while this remains taxonomy membership rather than independent reproduction.

**Mechanism:** The two branches extract pretrained face and voice features, fuse them, and optimize a combination of association, orthogonality, and hyperbolic objectives on VoxCeleb1.

**Mathematical/evaluation object:** Verification asks whether a pair matches, while AUC and EER expose different threshold behavior. Seen-heard and unseen-unheard splits test whether the association survives new videos and people.

**Reported evidence:** On the reported VoxCeleb1 splits, PAEFF improves the best listed baseline on unseen-unheard EER and reaches the highest or near-highest AUC in the table.

**Limit:** The result is author-reported and tied to VoxCeleb1, its split protocol, pretrained encoders, and hyperparameters; it does not establish robustness to dubbing, adversarial pairing, or other cultures.

#### Test-Time Training for Speech-based Depression Detection

**Why this belongs:** Depression detection from speech tests whether a voice pattern correlates with a clinical state, with confounding by speaker and context as a central boundary.

**Mechanism:** The study applies test-time training to a speech-based depression detector and tests shifts from noise, gender, and dataset/curation differences.

**Mathematical/evaluation object:** Performance under each shift is compared before and after adaptation; the important object is the distribution gap, not only the average source score.

**Reported evidence:** The paper reports substantial performance improvement under the tested shifts.

**Limit:** The task is a clinical screening proxy, not a diagnosis; adaptation stability, labels in deployment, privacy, and external clinical validation remain open.

#### Crowdsourcing MUSHRA Tests in the Age of Generative Speech Technologies: A Comparative Analysis of Subjective and Objective Testing Methods

**Why this belongs:** Crowdsourced MUSHRA changes who supplies quality judgments, so listener agreement and objective metrics must be compared explicitly.

**Mechanism:** The paper compares MTurk, Prolific, and expert ratings, measures test-retest reliability, and evaluates six objective metrics on generative speech codecs.

**Mathematical/evaluation object:** MUSHRA ratings, reliability, platform effects, and metric-to-human alignment are separate quantities; collapsing them into one score hides the evaluation problem.

**Reported evidence:** The paper reports platform-specific bias, reasonable crowdsourced comparisons under its protocol, and that traditional metrics undervalue generative models.

**Limit:** The result is bounded to the codecs, platforms, listener recruitment, and six metrics tested; other populations and model families remain open.

#### Towards Robust Speaker Recognition against Intrinsic Variation with Foundation Model Few-shot Tuning and Effective Speech Synthesis

**Why this belongs:** Robust speaker recognition tests whether identity survives intrinsic changes in a person's voice instead of being confused with a fixed acoustic profile.

**Mechanism:** The framework selects synthetic speech, tunes the foundation model with few enrollment examples, and evaluates open-set identification across time-varying and emotional benchmarks.

**Mathematical/evaluation object:** Identification accuracy and open-set outlier behavior separate recognizing enrolled speakers from rejecting unknown speakers.

**Reported evidence:** The paper reports stronger generalization to aging and emotional variation while maintaining resistance to unknown outliers.

**Limit:** The claim is bounded to the synthetic-data choices, foundation model, enrollment protocol, and benchmarks; real aging trajectories, spoofing attacks, and fairness across groups remain open.

#### Comparative Evaluation of Acoustic Feature Extraction Tools for Clinical Speech Analysis

**Why this belongs:** The comparison of acoustic feature tools asks whether a measured speech property is stable enough for clinical analysis, not whether it diagnoses by itself.

**Mechanism:** Three toolkits are applied to 77 schizophrenia-spectrum and 87 control speakers; correlations and classification performance are compared.

**Mathematical/evaluation object:** Feature correlations, agreement for F0/formants, and AUC reveal whether a feature is reproducible and useful for discrimination.

**Reported evidence:** F0 percentile agreement is high, but F0 variation and formants can disagree or even correlate negatively; F0 mean, HNR, and MFCC1 exceed AUC .70 in the reported classification.

**Limit:** The clinical groups, recordings, parameter choices, and tool versions define the boundary; no clinical diagnosis or deployment safety follows from these correlations.

#### Can We Trust Machine Learning? The Reliability of Features from Open-Source Speech Analysis Tools for Speech Modeling

**Why this belongs:** Reliability of open-source speech features matters because downstream users may treat a convenient tool as a trustworthy measurement instrument.

**Mechanism:** OpenSMILE and Praat features are evaluated on adolescents with autism from audio-visual recordings, with model performance compared across contexts and demographics.

**Mathematical/evaluation object:** Feature agreement and downstream classification are both measured; this connects measurement reliability to fairness rather than stopping at correlation.

**Reported evidence:** The paper reports considerable tool variation that influences model performance across context and demographic groups.

**Limit:** The population, features, tools, and behavioral tasks define the boundary; the study does not identify one universally correct toolkit.

#### Pitch Target Realization in Putonghua Tone Production of Children from Dialect-Speaking Regions

**Why this belongs:** Children from dialect-speaking regions realize tone targets through both development and language background, so age cannot be treated as a nuisance independent of variety.

**Mechanism:** Pitch production from 139 Changli-exposed children aged 35–71 months is analyzed in the CL-CHILD corpus.

**Mathematical/evaluation object:** The comparison separates target approximation, physiological constraints, and mutual interference among tonal categories.

**Reported evidence:** The paper reports universal physiological constraints, persistent dialect interference, and off-target forms arising from phonetic similarity and target interaction.

**Limit:** The age range, dialect exposure, corpus, and tone inventory bound the developmental claim; longitudinal and other language environments remain open.

#### Predicting Adolescent Suicidal Risk from Multi-task-based Speech: An Ensemble Learning Approach

**Why this belongs:** Suicidal-risk prediction from speech must separate clinically relevant cues from topic, speaker, and recording correlations.

**Mechanism:** OpenSmile and Emotion2Vec supply acoustic representations, a fine-tuned Chinese BERT supplies semantic features, and XGBoost/SVM-style base models are combined after Bayesian hyperparameter search.

**Mathematical/evaluation object:** An ensemble votes across partially different predictors; recall and F1 expose the cost of missing risk more directly than accuracy alone.

**Reported evidence:** On 600 Chinese adolescents, the paper reports test accuracy .63, recall .74, and F1 about .67.

**Limit:** This is a screening model on one challenge dataset, not a diagnosis or safety-tested intervention; age, language, labels, privacy, calibration, and external validation constrain the claim.

#### Towards Inclusive and Fair ASR: Insights from the SAPC Challenge for Optimizing Disordered Speech Recognition

**Why this belongs:** Inclusive ASR for disordered speech asks whether improvement is shared across speakers instead of optimizing an average that hides people with the greatest impairment.

**Mechanism:** ContextNet and Parakeet are tested on Speech Accessibility Project challenge subsets; WER is compared across the challenge conditions.

**Mathematical/evaluation object:** Word error rate counts substitutions, insertions, and deletions; it turns a listener's transcription burden into a measurable but incomplete quantity.

**Reported evidence:** The paper reports WER 10.06% and 11.8% on the two test subsets, with Parakeet slightly ahead of ContextNet.

**Limit:** Challenge data, speaker impairment profiles, transcripts, and WER define the boundary; fairness across disorders, user control, and clinical usefulness remain unestablished.

#### A Copula-Based Generative Score-Level Fusion Model for Speaker Verification

**Why this belongs:** Score-level fusion for speaker verification asks how multiple uncertain identity measurements should combine before access is granted.

**Mechanism:** Variance-Gamma marginals describe each recognizer's score distribution and a Gaussian copula describes dependence for target and non-target trials.

**Mathematical/evaluation object:** The copula separates marginal shape from dependency; Cllr measures calibration and discrimination of verification scores.

**Reported evidence:** On NIST SRE 2019 and SITW, the method reports up to 7% relative Cllr reduction versus discriminative linear fusion.

**Limit:** Datasets, recognizer diversity, score distributions, and calibration protocol bound the result; new speakers, channels, and attacks need separate evaluation.

#### EEG-based Voice Conversion : Hearing the Voice of Your Brain

**Why this belongs:** EEG-based voice conversion asks whether neural activity can control the identity or content of a generated voice without an ordinary microphone signal.

**Mechanism:** A three-stage training strategy maps EEG to speaker-specific features and conditions a pretrained speech-only converter; Dutch single-word production tests the system.

**Mathematical/evaluation object:** The alignment is a cross-modal mapping problem; zero-shot evaluation tests whether target identity can be supplied without target speech data.

**Reported evidence:** The paper reports reliable target-voice conversion on the Single-Word-Production Dutch-iBIDS dataset.

**Limit:** Single words, EEG setup, target voices, and small dataset define the claim; intelligibility, privacy, consent, and real assistive communication remain open.

#### Unifying Listener Scoring Scales: Comparison Learning Framework for Speech Quality Assessment and Continuous Speech Emotion Recognition

**Why this belongs:** Listener ratings differ by person, so speech quality and emotion models need an ordinal comparison scale that does not erase individual judgment.

**Mechanism:** The method is evaluated on speech quality assessment and continuous emotion recognition, comparing a unified comparison-based scale with mean-listener and multi-scale approaches.

**Mathematical/evaluation object:** Pairwise comparison models order utterances; the central mathematical choice is to preserve ordinal relationships rather than average incompatible numbers.

**Reported evidence:** The paper reports improved prediction performance and robustness on both tasks.

**Limit:** Listener panels, rating prompts, comparison construction, and datasets bound the result; agreement and usefulness for new listener populations remain open.

#### Optimizing Pause Context in Fine-Tuning Pre-trained Large Language Models for Dementia Detection

**Why this belongs:** The official full paper identifies a human spoken-speech object and a bounded research problem that instantiate clinical-speech-marker under clinical-and-assistive-speech; this resolves taxonomy membership, not the paper's scientific validity.

**Mechanism:** Cantonese elderly speech from CU-Marvel is transcribed, pause context is fused into transformer input, and binary dementia tasks are compared under alternative pause groupings.

**Mathematical/evaluation object:** The pause is treated as structured context attached to a linguistic boundary; classification accuracy and F1 test whether that context adds clinically useful signal.

**Reported evidence:** The paper reports that optimized between-segment pause patterns improve detection and that different tasks prefer different pause representations.

**Limit:** The corpus, language, age group, transcription quality, diagnostic labels, and pause definitions bound the result; this is not a validated clinical biomarker or a causal account of dementia.

#### Challenges in Automated Processing of Speech from Child Wearables:  The Case of Voice Type Classifier

**Why this belongs:** The official full paper identifies a human spoken-speech object and a bounded research problem that instantiate age-and-development under speaker-characteristics; this resolves taxonomy membership, not the paper's scientific validity.

**Mechanism:** Three years of voice-type classification experiments on child-worn recordings compare representation features, architectures, and parameter search against data changes.

**Mathematical/evaluation object:** Performance is limited by the relationship between labels and the recording environment; classification scores reveal whether engineering changes matter relative to data coverage.

**Reported evidence:** Model and tuning improvements produce marginal gains, while more relevant and larger shareable data produce more progress.

**Limit:** The child-wearable setting, label scheme, permissions, and task definition bound the result; conclusions do not automatically transfer to adult or laboratory speech.

#### EEG-based Speech Decoding Based on Multi-mode Joint Modeling

**Why this belongs:** The official full paper identifies a human spoken-speech object and a bounded research problem that instantiate augmentative-communication under clinical-and-assistive-speech; this resolves taxonomy membership, not the paper's scientific validity.

**Mechanism:** A joint EEG decoder covers imagined, intended, and spoken speech and is evaluated on four-vowel classification, including a channel-selection transfer step.

**Mathematical/evaluation object:** Shared and mode-specific evidence are balanced by masking; vowel accuracy tests decoding while selected-channel performance tests whether the joint model identifies useful measurements.

**Reported evidence:** Imagined-speech accuracy rises to 34.95% from a 29.18% baseline, and channel-selected single-mode models outperform models using all channels.

**Limit:** The four-vowel task, participants, EEG hardware, mode definitions, and accuracy metric bound the result; it does not demonstrate unrestricted communication or clinical readiness.

#### Addressing Task Conflicts in Stuttering Detection via MMoE-Based Multi-Task Learning

**Why this belongs:** The official full paper identifies a human spoken-speech object and a bounded research problem that instantiate dysarthria-and-atypical-speech under clinical-and-assistive-speech; this resolves taxonomy membership, not the paper's scientific validity.

**Mechanism:** Rule-based multi-task learning and a multi-mixture-of-experts model are evaluated on stuttering-symptom detection and the 2024 SLT challenge.

**Mathematical/evaluation object:** The model treats task gradients and predictions as competing demands; per-task and average F1 reveal whether collaboration improves the clinical outputs.

**Reported evidence:** The rule-based strategy reports a 19.9% average-F1 gain over baseline and the MMoE strategy a further 7.55% improvement.

**Limit:** The challenge data, symptom definitions, labels, class balance, and F1 aggregation bound the claim; benchmark gains do not establish clinical reliability or fairness.

#### Semantic Processing During Spoken Word Production by Children with Cochlear Implants

**Why this belongs:** The official full paper identifies a human spoken-speech object and a bounded research problem that instantiate augmentative-communication under clinical-and-assistive-speech; this resolves taxonomy membership, not the paper's scientific validity.

**Mechanism:** Children with cochlear implants and normal-hearing peers name pictured objects while distractor words vary in semantic relatedness.

**Mathematical/evaluation object:** Naming latency or accuracy under interference is an indirect test of semantic activation; the group contrast separates access strategy from surface articulation.

**Reported evidence:** Normal-hearing children show the typical semantic interference effect, while the implant group does not, consistent with different semantic organization or greater top-down control.

**Limit:** The group, age, implant history, language, task, and interpretation of interference bound the result; absence of an effect is not a direct measurement of neural organization.

#### Leveraging Ordinal Information for Speech-based Depression Classification

**Why this belongs:** The official full paper identifies a human spoken-speech object and a bounded research problem that instantiate clinical-speech-marker under clinical-and-assistive-speech; this resolves taxonomy membership, not the paper's scientific validity.

**Mechanism:** Speech-based depression scores are converted into K threshold tasks; an ordinal loss trains the model across these linked boundaries.

**Mathematical/evaluation object:** The target is an ordered scale, not a collection of unrelated labels; threshold consistency lets errors near a boundary differ from errors across the full range.

**Reported evidence:** The ordinal method outperforms reported state-of-the-art depression-detection methods in the paper's experiments.

**Limit:** The clinical scale, speakers, labels, dataset, threshold choices, and evaluation metrics bound the result; better ordinal prediction is not diagnosis or clinical validation.

#### A Study on Speech Assessment with Visual Cues

**Why this belongs:** Visual cues are added to non-intrusive speech-quality assessment because a no-reference score must predict what listeners understand without a clean signal.

**Mechanism:** The model aligns spectral and visual information before multi-task regression; LCC compares predicted and reference proxy scores under noise.

**Mathematical/evaluation object:** Multimodal evidence can improve prediction of a proxy while still inheriting the proxy’s limitations and the visual/audio distribution.

**Reported evidence:** On LRS3-TED with DEMAND noise, the paper reports higher LCC than audio-only baselines for PESQ and STOI under seen noise.

**Limit:** Seen-noise conditions, proxy targets, visual availability, dataset, and correlation metric limit transfer; proxy prediction is not a listener study.

#### Speech Unlearning

**Why this belongs:** Speech unlearning treats private speaker information as something a trained model may need to remove, evaluated through membership inference.

**Mechanism:** Keyword-spotting and speaker-identification experiments compare removing one recording with removing an entire speaker category and examine the difficulty relative to image and text unlearning.

**Mathematical/evaluation object:** Unlearning is a constrained before/after problem: target influence should disappear while non-target accuracy remains; forgetting and retention need separate tests.

**Reported evidence:** The paper reports that speech unlearning is substantially harder than image or text unlearning and identifies structured training, evaluation, feature-level removal, and adversarial robustness as open directions.

**Limit:** Tasks, speakers, unlearning definitions, attack tests, and evaluation criteria bound the result; a proposed forgetting score is not proof of privacy against every adversary.

#### Speech stimulus design to study the neural coding of speech and the impact of cochlear synaptopathy

**Why this belongs:** Controlled speech stimuli test how hearing-related neural limitations affect access to fine temporal speech information.

**Mechanism:** The paper designs analysis-resynthesis speech stimuli to test phase-locking/temporal-fine-structure coding and accommodates multi-center studies across species, methods, and languages, including cochlear synaptopathy conditions.

**Mathematical/evaluation object:** The stimulus is an experimental instrument: a waveform is decomposed, controlled dimensions are altered, and the result is resynthesized; psychophysical or neural responses can then be attributed more narrowly than with natural recordings alone.

**Reported evidence:** The paper reports a design framework for controlled naturalistic stimuli suitable for studying the target coding mechanism and its impairment in cochlear synaptopathy.

**Limit:** Stimulus fidelity, resynthesis artifacts, listener population, language, and study protocol bound the inference; a designed cue isolates a mechanism only insofar as unedited cues remain controlled.

#### Egocentric Speaker Classification in Child-Adult Dyadic Interactions: From Sensing to Computational Modeling

**Why this belongs:** Egocentric sensing changes the acoustic viewpoint, so speaker classification must separate who is speaking from where the microphone is worn.

**Mechanism:** The paper studies wearable sensing in BOSCC child–clinician interactions, uses egocentric speech sampling, and evaluates computational speaker classification for behavioral analysis related to autism treatment.

**Mathematical/evaluation object:** The observation point changes the signal distribution; classification performance is therefore a joint property of speaker cues, body-worn placement, interaction, and activity timing rather than voice alone.

**Reported evidence:** The paper reports that egocentric sensing provides useful information for child/adult speaker classification and highlights the promise and constraints of wearable speech modeling.

**Limit:** BOSCC activities, children/clinicians, sensor placement, privacy, and speaker labels bound the result; classification is not a direct measure of social communication or treatment outcome.

#### Does effortful speech production indicate communication difficulty caused by noise and hearing aid support?

**Why this belongs:** Communication difficulty is a listener-and-speaker experience that must be related to vocal effort, noise, hearing status, and turn timing.

**Mechanism:** The study pairs 44 normal-hearing and hearing-impaired participants in task-based conversations in quiet and 70 dB noise, with the hearing-impaired group tested with and without hearing aids; F1, vocal level, and turn-taking variability are modeled against questionnaires.

**Mathematical/evaluation object:** The target is a human report conditioned on dyad, noise, device, and turn structure; regression links observable speech behavior to experience while keeping the experience measure distinct from the signal.

**Reported evidence:** The paper reports that higher vocal level and interaction measures predict communication difficulty for hearing-impaired participants under relevant conditions.

**Limit:** Small dyadic sample, task design, questionnaire, hearing-aid settings, and acoustic noise bound the result; a predictor of reported difficulty is not a universal clinical measure or causal explanation.

#### How sibilant spectra shape gender perception in prepubertal children: A voice morphing study

**Why this belongs:** A voice-morphing study asks how children perceive gender from sibilant spectra, showing that acoustic cues and social interpretation are related but not identical.

**Mechanism:** The longitudinal study measures center of gravity and skewness of /z/ in German-speaking children aged 6–9 and runs gender-perception experiments with natural and morphed voices.

**Mathematical/evaluation object:** Morphing is a controlled intervention: it holds much of the voice fixed while changing the sibilant spectrum, allowing perception to be compared with the correlation found in natural speech.

**Reported evidence:** No overall gender differences in the measured sibilant features were found; sibilants did not affect gender perception in natural stimuli but did affect it in morphed stimuli, suggesting stereotypical associations in isolation.

**Limit:** Age, language, stimulus construction, listener beliefs, longitudinal sample, and morphing artifacts bound the claim; a perceptual association is not a biological marker or justification for gender classification.

#### Web-Based Application for Real-Time Biofeedback of Vocal Resonance in Gender-Affirming Voice Training: Design and Usability Evaluation

**Why this belongs:** The title and preserved abstract identify a speech object and bounded intervention that instantiate user-control-and-consent under human-centered-evaluation; this resolves taxonomy membership only.

**Mechanism:** The study combines real-time acoustic analysis, visual feedback, and a usability evaluation for gender-affirming voice training.

**Mathematical/evaluation object:** The design treats feedback as part of a human learning loop: measurement matters only if a person can notice it, interpret it, and act on it.

**Reported evidence:** The paper reports a working web application and usability findings supporting its use as a training aid.

**Limit:** Small usability sample, task design, browser/audio conditions, and self-report limit claims about long-term learning or clinical outcomes.

#### Analysis of the ABC Classification Backends for NIST SRE24

**Why this belongs:** Speaker-recognition backends must separate identity evidence from channel and trial variation in a standardized evaluation.

**Mechanism:** The paper studies backend choices for speaker classification/verification in the NIST SRE24 setting.

**Mathematical/evaluation object:** Verification is a decision pipeline: embeddings, score computation, calibration, and operating point jointly produce the accepted/rejected decision.

**Reported evidence:** The paper reports how the analyzed backends behave on the NIST SRE24 evaluation conditions.

**Limit:** Benchmark protocol, language/channel conditions, calibration, and chosen operating points limit claims beyond SRE24.

#### Personalized Fine-Tuning with Controllable Synthetic Speech from LLM-Generated Transcripts for Dysarthric Speech Recognition

**Why this belongs:** The preserved abstract identifies a speech object and bounded intervention that instantiate dysarthria-and-atypical-speech under clinical-and-assistive-speech; this upgrades a provisional candidate to analyst-reviewed taxonomy membership only.

**Mechanism:** The paper studies personalized fine-tuning with controllable synthetic speech for dysarthric speech recognition.

**Mathematical/evaluation object:** Personalization is a data-design problem: synthetic examples are useful only when their transcript, pronunciation variation, and speaker control support the target speaker rather than dilute them.

**Reported evidence:** The paper reports recognition results for personalized adaptation using controllable synthetic data.

**Limit:** Speaker cohort, dysarthria type, transcript generation, synthesis quality, and adaptation budget limit generalization or clinical claims.

#### Agent-based modelling, sound change, and metaphony in Southern Italian varieties of Italo-Romance.

**Why this belongs:** Agent-based sound-change modeling treats speakers and communities as sources of variation rather than nuisance deviations from one pronunciation.

**Mechanism:** The paper tests an agent-based model of dialect contact and morpho-phonological sound change.

**Mathematical/evaluation object:** A dialect is not a static inventory: production is repeatedly updated through perceptual memory and interaction, allowing social contact to reshape acoustic categories over time.

**Reported evidence:** The reported results provide support for an asymmetric shift toward the innovative dialect and are consistent with feedback models of sound change.

**Limit:** The two dialects, 54 speakers collapsed to 13 agents, selected words, F1 trajectory representation, and model assumptions limit generalization to other communities or changes.

#### Perception of Emotional Speech by Individuals with High Borderline Personality Features

**Why this belongs:** Emotional speech from people with borderline personality features tests how voice quality and listener response interact rather than treating emotion as words alone.

**Mechanism:** The paper studies emotional-speech perception in listeners with high borderline personality features.

**Mathematical/evaluation object:** The listener is part of the speech-perception system: the same acoustic cue can be weighted differently depending on emotional regulation and the listener’s internal expectations.

**Reported evidence:** High-feature participants were less accurate for neutral speech and high-intensity happy speech, with distinct confusion patterns and marginally higher confidence for angry speech.

**Limit:** Mandarin synthetic stimuli, university participants, self-report grouping, F0 manipulation, and perceptual task bound generalization; the findings do not diagnose BPD or explain all underlying causes.

#### Pushing the Frontiers of Self-Distillation Prototypes Network with Dimension Regularization and Score Normalization

**Why this belongs:** The paper addresses collapse and score calibration in speaker representations without speaker labels.

**Mechanism:** The paper improves self-supervised speaker verification with dimension regularization and score normalization.

**Mathematical/evaluation object:** Verification has two linked problems: learn a non-collapsed identity space and compare enrollment/test scores on a calibrated scale; solving only one leaves unreliable decisions.

**Reported evidence:** On VoxCeleb1, the paper reports EERs of 1.29%, 1.60%, and 2.80% on the O/E/H trials and relative improvements over prior self-supervised methods.

**Limit:** VoxCeleb1, trial conditions, unlabeled-training setup, score normalization, and EER bound the claim; benchmark gains do not establish fairness or robustness in deployment.

#### Synthetic Dysarthric Speech: A Supplement, Not a Substitute for Authentic Data in Dysarthric Speech Recognition

**Why this belongs:** The title and preserved abstract identify a speech object and bounded intervention that instantiate dysarthria-and-atypical-speech under clinical-and-assistive-speech; this resolves taxonomy membership only.

**Mechanism:** The study varies whether training uses authentic Set A/Set B data, synthetic data derived from Set A, or much larger synthetic additions. It measures ASR performance and compares acoustic feature distributions between authentic and synthetic samples.

**Mathematical/evaluation object:** Synthetic data is a distributional proposal, not a label-preserving copy: the relevant question is whether generated speech spans the motor and acoustic variation needed by the recognizer.

**Reported evidence:** Across the tested Chinese dysarthric speech setup, synthetic speech alone does not replace authentic data and large synthetic additions yield only marginal gains over authentic training.

**Limit:** The language, seven-speaker usable subset, TTS model, data scale, ASR architecture, and speaker-independent split bound generalization; a synthetic-data result is not clinical validation.

#### Fairness in Dysarthric Speech Synthesis: Understanding Intrinsic Bias in Dysarthric Speech Cloning using F5-TTS

**Why this belongs:** The title and preserved abstract identify a speech object and bounded intervention that instantiate dysarthria-and-atypical-speech under clinical-and-assistive-speech; this resolves taxonomy membership only.

**Mechanism:** The study defines metrics over group means: WER/CER for intelligibility, SIM-o cosine similarity for speaker traits, and AutoPCP for prosody. Fairness is assessed by deviations from healthy-speaker reference behavior.

**Mathematical/evaluation object:** The mechanism is an evaluation reframing: voice cloning is not one scalar quality target when a model may preserve identity but unevenly alter disability-linked prosody or intelligibility.

**Reported evidence:** The paper reports severity-dependent differences in the objective measures and uses those differences to characterize intrinsic bias in F5-TTS cloning.

**Limit:** TORGO, reference-prompt choice, automatic metrics, severity grouping, and zero-shot model behavior bound the result; parity in proxies does not establish respectful control, consent, or listener benefit.

#### What Do Humans Hear When Interacting? Experiments on Selective Listening for Evaluating ASR of Spoken Dialogue Systems

**Why this belongs:** Listening selectively in dialogue asks whether ASR evaluation reflects the speech people actually need to understand amid competing talkers.

**Mechanism:** Participants generate a response and then recall/transcribe the speech; multiple regression estimates POS weights, which are inserted into the edit-distance costs used by weighted WER.

**Mathematical/evaluation object:** A regression predicts the remembered POS counts from the full transcript; the resulting coefficients weight insertions, deletions, and substitutions in a minimum-edit-distance score. Five-fold validation compares MAE and R².

**Reported evidence:** Humans attend more to content words than function words; the proposed H-WWER gives lower scores to human than Whisper transcriptions in the reported comparison and is offered as a dialogue-relevant complement to WER.

**Limit:** Transcription follows response generation rather than occurring simultaneously, and the displayed weight comparison is partly optimized on test data. The metric is a proposal, not validated against downstream response success or diverse dialogue settings.

#### Accessible Delivery of Visual-Acoustic Biofeedback for Speech Sound Disorder

**Why this belongs:** The title and preserved abstract identify a speech object and bounded intervention that instantiate accessibility-fit under human-centered-evaluation; this resolves taxonomy membership only.

**Mechanism:** JavaScript computes LPC coefficients with Levinson-Durbin recursion, renders the spectral envelope and peaks, and supports randomized word/syllable routines, clinician scoring, gamification, and local-device WebRTC processing.

**Mathematical/evaluation object:** LPC models the signal as X(z)=H(z)E(z), with an all-pole vocal-tract filter H(z)=1/A(z); peak locations approximate formant resonances used as the feedback target.

**Reported evidence:** The staRt iOS/web system provides real-time visual-acoustic biofeedback for /r/ training and reports broad uptake; local processing avoids telepractice loss of frequency resolution and latency.

**Limit:** The current target is mainly English /r/, peak-picking and formant tracking are not yet stable enough for automated feedback across vocal-tract sizes, and clinical efficacy is not established by this technical description.

#### Processing of grammatical information in cochlear implant simulated speech by German adult listeners

**Why this belongs:** The title and preserved abstract identify a speech object and bounded intervention that instantiate accessibility-fit under human-centered-evaluation; this resolves taxonomy membership only.

**Mechanism:** German adults answer subject, object, and passive which-questions. Eye movements and response accuracy expose whether case and subject-verb agreement cues survive the simulation; mixed-effects analyses relate performance to working memory.

**Mathematical/evaluation object:** Accuracy and gaze behavior are behavioral proxies for comprehension; the comparison is between normal and CI-simulated acoustic conditions rather than between two recognition models.

**Reported evidence:** Only object-question accuracy was affected by the simulation, with weaker interpretation preferences in gaze patterns; higher working memory was associated with better accuracy and faster reorientation.

**Limit:** The simulation is not an actual implant, the German grammatical system and question types are narrow, and listener behavior does not establish clinical device benefit or general speech recognition performance.

#### Concurrent Speech and Auditory Tag Clouds for Non-Visual Web Interaction

**Why this belongs:** The title and preserved abstract identify a speech object and bounded intervention that instantiate accessibility-fit under human-centered-evaluation; this resolves taxonomy membership only.

**Mechanism:** TagThunder extracts morpho-dispositional semantics and maps tags to concurrent speech streams and guiding stimuli; discrete and continuous interaction conditions test structured information scanning.

**Mathematical/evaluation object:** The system treats auditory channels as a limited display: timing, concurrency, and user selection determine which semantic items are attended rather than merely transcribed.

**Reported evidence:** The paper presents the experimental framework and reports feasibility for non-visual web skimming through auditory tag-cloud interaction.

**Limit:** The evaluation is interaction-specific, auditory clutter and learning effects matter, and accessibility promise is not equivalent to demonstrated performance across blind users, browsers, languages, or real browsing tasks.

#### You Are What You Say: Exploiting Linguistic Content for VoicePrivacy Attacks

**Why this belongs:** Voice-privacy attacks use linguistic content to recover identity, demonstrating that removing or changing words is not enough to protect a speaker.

**Mechanism:** The attacker maps linguistic content to speaker labels; semantically similar utterances become a non-acoustic identity channel in the evaluation.

**Mathematical/evaluation object:** Privacy evaluation requires separating nuisance correlations from the protected attribute; otherwise the attack measures corpus curation rather than voice leakage.

**Reported evidence:** The paper reports mean EER around 35%, with some speakers as low as 2%, using text alone on VoicePrivacy data.

**Limit:** Dataset curation, speaker/content overlap, BERT training, split design, and EER interpretation bound the claim; text leakage does not prove an anonymizer fails acoustically.

#### Variability in performance across four generations of automatic speaker recognition systems

**Why this belongs:** Speaker-recognition averages conceal persistent hard speakers; the paper separates system generation effects from person-level variation.

**Mechanism:** Matched evaluation separates model-generation effects from test-set changes and decomposes variation by file and speaker factors.

**Mathematical/evaluation object:** The unit of analysis matters: an overall metric averages heterogeneous difficulty, while per-speaker outcomes expose persistent tails.

**Reported evidence:** Performance improves from GMM-UBM through i-vector and x-vector but not ECAPA-TDNN in the reported comparison; some individuals remain difficult across systems.

**Limit:** Forensic data, calibration, system implementations, speaker sampling, and metric choice bound transfer; persistent difficulty is not automatically a biological property.

#### Feature Importance across Domains for Improving Non-Intrusive Speech Intelligibility Prediction in Hearing Aids

**Why this belongs:** The title and preserved abstract identify a speech object and bounded intervention that instantiate accessibility-fit under human-centered-evaluation; this resolves taxonomy membership only.

**Mechanism:** FiDo produces domain-specific weighted representations before concatenation and regression; RMSE on intelligibility targets evaluates whether the weighting preserves listener-relevant evidence.

**Mathematical/evaluation object:** Feature selection is moved inside the representation: the model learns which moments and domains matter before the final proxy prediction.

**Reported evidence:** The paper reports that FiDo reduces MBI-Net+ RMSE from 26.10 to 24.11 and improves over the best 2023 Clarity Prediction Challenge system.

**Limit:** Weakly supervised targets, hearing-aid/noise conditions, challenge split, proxy RMSE, and absence of a new listener study bound the claim; prediction is not equivalent to real-world access improvement.

#### A Bayesian Approach to L2 Fluency Ratings by Native and Nonnative Listeners

**Why this belongs:** Fluency ratings depend on who listens and how familiar that listener is with the speaker's language background.

**Mechanism:** Posterior distributions represent listener-specific leniency and cue weights; speed, breakdown, and repair features explain ratings while uncertainty remains explicit.

**Mathematical/evaluation object:** Human evaluation is a multilevel measurement problem: the score is jointly produced by the speech sample and the observer’s perceptual prior.

**Reported evidence:** Using 16 listeners and 180 Japanese speakers in J-AESOP, the paper reports greater leniency among some nonnative listeners and stronger fit for segment-based articulation rate.

**Limit:** Listener sample, language backgrounds, trained-rating task, corpus, feature definitions, and Bayesian priors bound transfer; fluency ratings are not a complete measure of communicative success.

#### Examining Test-Time Adaptation for Personalized Child Speech Recognition

**Why this belongs:** The title and preserved abstract identify a speech object and bounded intervention that instantiate age-and-development under speaker-characteristics; this resolves taxonomy membership only.

**Mechanism:** The adaptation updates model behavior from incoming child speech at inference time, without target transcripts, and is evaluated against unadapted baselines.

**Mathematical/evaluation object:** Personalization is an online evidence problem: each child supplies a changing acoustic distribution rather than a fixed domain label.

**Reported evidence:** The paper reports average and per-child gains for both model types, with remaining limitations on non-linguistic child speech.

**Limit:** Child corpus, adaptation methods, update stability, model family, and evaluation conditions bound transfer; average WER gains are not proof of safe continual deployment.

#### EmoSpeechAuth: Emotion-Aware Speaker Verification

**Why this belongs:** The captured official PDF and abstract identify a speech object and mechanism instantiating speaker-verification under speaker-characteristics; this upgrades evidence depth for the structured note and does not establish independent reproduction.

**Mechanism:** The verifier separates speaker-consistent structure from emotion-dependent variation.

**Mathematical/evaluation object:** The relevant object is the speaker-verification evidence described by the paper's mechanism: The verifier separates speaker-consistent structure from emotion-dependent variation.

**Reported evidence:** The paper presents EmoSpeechAuth and evaluates emotion-aware speaker verification.

**Limit:** Emotion labels, speakers, channel, enrollment, thresholds, and demographics bound transfer.

#### EAA: Emotion-Aware Audio Large Language Models with Dual Cross-Attention and Context-Aware Instruction Tuning

**Why this belongs:** The captured official PDF and abstract identify a speech object and mechanism instantiating listener-effort under human-centered-evaluation; this upgrades evidence depth for the structured note and does not establish independent reproduction.

**Mechanism:** Cross-attention aligns acoustic and conversational representations.

**Mathematical/evaluation object:** The relevant object is the listener-effort evidence described by the paper's mechanism: Cross-attention aligns acoustic and conversational representations.

**Reported evidence:** The paper reports EAA results for emotion-aware audio large language modeling.

**Limit:** Labels, prompts, audio quality, model, and human agreement bound transfer.

#### Individualized speech enhancement for hearing-impaired listeners

**Why this belongs:** The captured official PDF and abstract identify a speech object and mechanism instantiating accessibility-fit under human-centered-evaluation; this upgrades the structured note to D3 without establishing independent reproduction.

**Mechanism:** Listener-specific constraints become the target of enhancement rather than the average waveform.

**Mathematical/evaluation object:** The paper treats accessibility-fit as a structured evidence-to-decision problem: Listener-specific constraints become the target of enhancement rather than the average waveform.

**Reported evidence:** The paper reports individualized speech enhancement for hearing-impaired listeners.

**Limit:** Hearing profiles, listener numbers, fitting procedure, materials, and subjective protocol bound transfer.

### Synthesis boundary

These papers share a conceptual pressure, but this seed batch does not justify ranking methods, estimating prevalence, or claiming that the mechanism generalizes across speakers, languages, rooms, or tasks. Those claims require additional assignments and comparable denominators.

## Many languages, accents, and unequal evidence

**Ordinary pressure:** Languages differ in sounds, writing systems, grammar, prosody, code-switching, and social meaning; data and tools are distributed unevenly.

**Naive strategy that breaks:** Scaling an English-centered recipe or translating labels assumes that all languages expose the same units, data, and errors.

**Recurring move:** Share useful structure across languages while preserving language-specific distinctions, measuring who benefits, and making uncertainty visible where evidence is thin.

**Boundary:** Transfer can import pronunciation or cultural assumptions, and aggregate multilingual scores can hide severe failures in a small language or community.

**D3 evidence status:** 59 reviewed paper(s); the family claim below is limited to these examples.

**Conceptual family represented:** `accent-dialect-and-cultural-meaning/dialect-and-variety`, `accent-dialect-and-cultural-meaning/accent-robustness`, `crosslingual-structure/code-switching`, `low-resource-learning/self-training-and-pseudo-labels`, `crosslingual-structure/crosslingual-transfer`, `crosslingual-structure/code-switching`, `data-creation/speech-data-collection`, `crosslingual-structure/code-switching`, `low-resource-learning/few-shot-adaptation`, `accent-dialect-and-cultural-meaning/accent-robustness`, `accent-dialect-and-cultural-meaning/accent-robustness`, `crosslingual-structure/language-identification`, `crosslingual-structure/code-switching`, `low-resource-learning/self-training-and-pseudo-labels`, `crosslingual-structure/crosslingual-transfer`, `data-creation/speech-data-collection`, `accent-dialect-and-cultural-meaning/dialect-and-variety`, `accent-dialect-and-cultural-meaning/accent-robustness`, `low-resource-learning/self-training-and-pseudo-labels`, `crosslingual-structure/language-identification`, `accent-dialect-and-cultural-meaning/cultural-meaning`, `crosslingual-structure/crosslingual-transfer`, `data-creation/speech-data-collection`, `accent-dialect-and-cultural-meaning/dialect-and-variety`, `accent-dialect-and-cultural-meaning/dialect-and-variety`, `accent-dialect-and-cultural-meaning/dialect-and-variety`, `crosslingual-structure/code-switching`, `low-resource-learning/few-shot-adaptation`, `data-creation/speech-data-collection`, `data-creation/speech-data-collection`, `data-creation/speech-data-collection`, `accent-dialect-and-cultural-meaning/cultural-meaning`, `accent-dialect-and-cultural-meaning/dialect-and-variety`, `accent-dialect-and-cultural-meaning/cultural-meaning`, `data-creation/speech-data-collection`, `crosslingual-structure/crosslingual-transfer`, `low-resource-learning/self-training-and-pseudo-labels`, `crosslingual-structure/language-identification`, `low-resource-learning/few-shot-adaptation`, `crosslingual-structure/crosslingual-transfer`, `low-resource-learning/few-shot-adaptation`, `crosslingual-structure/crosslingual-transfer`, `low-resource-learning/self-training-and-pseudo-labels`, `crosslingual-structure/crosslingual-transfer`, `data-creation/speech-data-collection`, `crosslingual-structure/crosslingual-transfer`, `low-resource-learning/few-shot-adaptation`, `crosslingual-structure/crosslingual-transfer`, `data-creation/speech-data-collection`, `crosslingual-structure/crosslingual-transfer`, `data-creation/speech-data-collection`, `crosslingual-structure/crosslingual-transfer`, `accent-dialect-and-cultural-meaning/dialect-and-variety`, `accent-dialect-and-cultural-meaning/accent-robustness`, `accent-dialect-and-cultural-meaning/cultural-meaning`, `accent-dialect-and-cultural-meaning/dialect-and-variety`, `accent-dialect-and-cultural-meaning/accent-robustness`, `accent-dialect-and-cultural-meaning/accent-robustness`, `accent-dialect-and-cultural-meaning/dialect-and-variety`.

### What the papers make concrete

#### Is it all about race? A Cross-examination of /s/ in a Multilingual Nigerian Context

**Why this belongs:** The paper measures /s/ variation across a multilingual Nigerian population and treats ethnicity, age, gender, and phonological context as boundaries on interpretation.

**Mechanism:** Acoustic realization is interpreted alongside multilingual context rather than one norm.

**Mathematical/evaluation object:** The relevant object is the accent-robustness evidence described by the paper's mechanism: Acoustic realization is interpreted alongside multilingual context rather than one norm.

**Reported evidence:** The paper reports a contextual analysis of /s/ in a multilingual Nigerian setting.

**Limit:** Community, language, sampling, annotation, and interpretation bound transfer.

#### abdullah25_interspeech

**Why this belongs:** Voice conversion is used as augmentation, but the paper's evaluated object is cross-domain dialect identification; the current question is whether dialect evidence survives changes in speaker realization.

**Mechanism:** Converted speech changes speaker characteristics while preserving dialect-related content; controlled experiments compare conversion with ordinary augmentation.

**Mathematical/evaluation object:** Cross-domain accuracy measures transfer rather than memorization; the causal explanation about speaker bias is supported by the paper’s controlled analysis but not independently verified here.

**Reported evidence:** The paper reports up to +34.07% cross-domain accuracy improvement and releases a model and evaluation dataset.

**Limit:** The result is specific to Arabic dialect identification and the released artifacts require separate access and execution checks.

#### biswas25_interspeech

**Why this belongs:** The method combines language prompts and code-mixed augmentation, so the core problem is switching language systems within speech rather than generic multilingual scaling.

**Mechanism:** Synthetic switches and language prompts expose the recognizer to transition patterns; MER and code-switch bigram accuracy evaluate transcription.

**Mathematical/evaluation object:** MER measures mixed-language word errors and CBA focuses on correctly recognized bigrams at switch points.

**Reported evidence:** The paper reports a 31% relative improvement over pretrained Whisper without real in-domain data for fine-tuning.

**Limit:** The experiments focus on Hindi-English tutorial speech and Whisper large-v2; transfer to other language pairs is proposed, not established.

#### AfriHuBERT: A self-supervised speech representation model for African languages

**Why this belongs:** The paper expands self-supervised pretraining across African languages so useful speech units can be learned where labeled data are scarce.

**Mechanism:** Unlabeled audio is converted into masked prediction targets; the encoder learns from contextual speech patterns across languages and is then adapted for recognition and language-related tasks.

**Mathematical/evaluation object:** The pretraining objective predicts hidden or clustered speech units from surrounding frames; downstream scores measure whether those units support task labels with limited supervision.

**Reported evidence:** The paper reports a representation model expanded to 1,226 African languages and evaluates its transfer against multilingual baselines.

**Limit:** Language coverage does not mean equal data quality or equal downstream performance; the languages, hours, speaker balance, and task results determine the practical reach. No independent reproduction was performed.

#### A Study of Speech Embedding Similarities Between Australian Aboriginal and High-Resource Languages

**Why this belongs:** The paper studies whether learned speech geometry relates Australian Aboriginal languages to high-resource languages, while testing the limits of interpreting similarity as transfer.

**Mechanism:** Audio from multiple languages is passed through a speech encoder; distances or similarity distributions are compared across language pairs and conditions, with downstream implications analyzed.

**Mathematical/evaluation object:** Embedding similarity is a geometric comparison in the learned representation space; its interpretation depends on normalization, sampling, language balance, and the task used to validate it.

**Reported evidence:** The paper reports comparative embedding similarities involving Australian Aboriginal and high-resource languages and discusses implications for underrepresented-language technology.

**Limit:** Similarity is not a language description or a guarantee of recognition transfer; data quantity, speaker coverage, and community context limit interpretation. No independent reproduction was performed.

#### Can we train ASR systems on Code-switch without real code-switch data? Case study for Singapore's languages

**Why this belongs:** The paper creates phrase-level mixed-language training examples to reduce the need for costly real code-switching transcripts.

**Mechanism:** The paper creates phrase-mixed speech for Malay-English, Mandarin-Malay, and Tamil-English, fine-tunes Whisper, MMS, and SeamlessM4T, and compares monolingual and code-switched test performance against training without real code-switch recordings.

**Mathematical/evaluation object:** The outcome is word error rate on monolingual and code-switched benchmarks, with gains compared across language pairs and pretrained models. The crucial design choice is the data distribution used for fine-tuning.

**Reported evidence:** The authors report improved ASR on monolingual and code-switched tests, with the largest gains for BM-EN followed by TA-EN and ZH-BM.

**Limit:** Synthetic phrase mixing is an approximation to spontaneous switching, and the three language pairs do not represent all multilingual communities. WER does not measure whether switches are socially or linguistically natural, and no independent reproduction was performed.

#### Speech Annotation for A: Accuracy, Access, and Application

**Why this belongs:** The contribution makes bilingual clinical annotation usable by keeping human correction inside the transcription, speaker, language, and timestamp pipeline.

**Mechanism:** SAFA combines Whisper and diarization drafts with a PyQt6 interface. Chunk navigation follows playback, original and edited text/tags/timestamps are compared in real time, language and speaker labels are selectable, and CSV/SRT/TXT exports preserve the corrected record.

**Mathematical/evaluation object:** The central object is an auditable annotation state rather than a prediction score: every edit is exposed to a human. The paper’s evidence is a workflow/design demonstration, not a controlled accuracy study with a fixed annotation denominator.

**Reported evidence:** The paper presents an end-to-end bilingual clinical annotation workflow intended to reduce setup and manual effort while retaining human validation and structured metadata for downstream research.

**Limit:** The paper does not report a controlled user study, annotation-time reduction, inter-annotator agreement, or clinical outcome. Whisper/diarization errors and supported language choices remain boundaries; tool availability is not independent execution.

#### From Context to Code-switching: Examining the Interplay of Language Proficiency and Multilingualism in Speech

**Why this belongs:** The study connects code-switching behavior to language background and proficiency, showing why multilingual speech cannot be interpreted without speaker and language context.

**Mechanism:** The study analyzes spontaneous Spanish-English speech in the Bangor Miami corpus, defines insertional and alternational switching outcomes, compares speaker language profiles, and fits regression models to quantity, language distribution, and strategy. It separates associations that are statistically reliable from those that only approach significance.

**Mathematical/evaluation object:** The paper uses correlations, logistic regression, confidence intervals, and prediction analyses. Its denominators are corpus speakers and code-switched utterances; an association between background and switching is not a causal estimate of proficiency.

**Reported evidence:** The paper reports that parents’ primary language, secondary-school language, and self-reported higher-ability language are associated with code-switching quantity and dominant-language use, while several direct proficiency relationships are weak or inconclusive.

**Limit:** The analysis is observational, focused on Spanish-English Bangor Miami speakers and available self-reports; background variables may be correlated and do not establish why a speaker switched. Findings do not generalize automatically to other language pairs, communities, or tasks; no independent reproduction was performed.

#### Evaluating Wav2Vec2-Bert for Computer-Assisted Pronunciation Training for isiZulu

**Why this belongs:** IsiZulu pronunciation assessment exposes how language-specific data and incomplete error labels limit the meaning of recognition scores.

**Mechanism:** The study uses NCHLT native speech, L2 isiZulu learner speech, and teacher recordings. Models are fine-tuned with the same setup; phoneme alignment uses Needleman–Wunsch, and error labels are evaluated with false acceptance, false rejection, and true-negative rates.

**Mathematical/evaluation object:** On the NCHLT test set, the NCHLT-trained model reports WER 0.126 and CER 0.0237, versus WER 0.667 for the L2-only model and 0.141 for the combined model. For phoneme errors, the L2 model has FAR 2.2%, FRR 16.1%, and TNR 65.1%; the model cannot compute a full diagnostic error rate because the gold labels omit the learner's produced phone.

**Reported evidence:** Native-speech transcription is strongest for the NCHLT-trained model, while the L2-trained model detects the most incorrect phonemes under the available true-negative measure; the authors release code and identify the data sources.

**Limit:** The results depend on three isiZulu corpora, their recording styles, and incomplete phoneme-error labels. Tone is not evaluated because it is not marked orthographically; findings do not automatically transfer to other languages or pronunciation tasks.

#### LID Models are Actually Accent Classifiers: Implications and Solutions for LID on Accented Speech

**Why this belongs:** Language identification must preserve language evidence while refusing the shortcut that treats accent as language.

**Mechanism:** The study compares ECAPA-TDNN, MMS, and GEO systems on several corpora, measures accent-language confusion, reverses chunks, and fuses acoustic and sequence representations.

**Mathematical/evaluation object:** ECAPA-TDNN falls from 87.6% to 55.8% on CommonVoice and 73% to 57% on EdAcc for mainstream versus L2 accents; many models remain stable down to roughly 0.25-second chunks.

**Reported evidence:** Dutch-accented English is called Dutch in 82.6% of errors in one setting; sequence-aware systems reduce this confusion while retaining mainstream performance.

**Limit:** Datasets, accent categories, chunking, and aggregation define the result; it diagnoses a shortcut but does not prove cultural neutrality or universal transfer.

#### Accent Normalization Using Self-Supervised Discrete Tokens with Non-Parallel Data

**Why this belongs:** Discrete tokens change pronunciation while preserving speaker identity with nonparallel accent data.

**Mechanism:** The system extracts source tokens, predicts target-accent tokens, synthesizes waveform output, and evaluates several English accents.

**Mathematical/evaluation object:** NAT, ACT, SIM, WER, SECS, F0 correlation, and feature distance separately measure naturalness, accent, content, identity, and prosody.

**Reported evidence:** The system beats a frame-to-frame baseline on naturalness, accentedness, and timbre preservation, but post-conversion WER remains high.

**Limit:** Accent definitions, targets, subjective judgments, and nonparallel training bound the claim; native-like is not universally better.

#### TalTech Systems for the Interspeech 2025 ML-SUPERB 2.0 Challenge

**Why this belongs:** Language identification and specialized multilingual decoding allocate recognition capacity across languages.

**Mechanism:** The system combines language identification with multilingual ASR and customized models, then evaluates language ID and CER.

**Mathematical/evaluation object:** Language-ID accuracy and mean CER expose routing and transcription separately; reported values are 86.8% and 27.4%.

**Reported evidence:** The system is competitive with challenge baselines and identifies languages needing targeted work.

**Limit:** Challenge data, language mix, averaging, and tuning limit all-multilingual claims.

#### CS-FLEURS: A Massively Multilingual and Code-Switched Speech Dataset

**Why this belongs:** A controlled 52-language code-switched corpus exposes language-pair and script failures and tests synthetic-data transfer.

**Mechanism:** The corpus controls pair and switching conditions; experiments compare CER, direct translation, script pairs, and augmented training.

**Mathematical/evaluation object:** Distinct-script CER is about 3x same-script CER; synthetic training lowers reported seen CER 14.38 to 12.67 and unseen 29.62 to 27.77.

**Reported evidence:** Code-switched ASR is over twice as errorful as monolingual speech, while synthetic training improves seen and unseen pairs.

**Limit:** Language pairs, synthetic voices, Whisper, CER, and controlled read speech limit natural-conversation claims.

#### Better Semi-supervised Learning for Multi-domain ASR Through Incremental Retraining and Data Filtering

**Why this belongs:** The captured paper's ordinary problem, mechanism, and reported evaluation directly instantiate self-training-and-pseudo-labels within low-resource-and-data-creation.

**Mechanism:** The pipeline retrains in stages and uses agreement or entity preservation to decide which generated transcripts enter the next training round.

**Mathematical/evaluation object:** Data selection is treated as part of learning: the value of unlabeled speech depends on which errors are admitted, not only on how much audio is added.

**Reported evidence:** The paper reports up to 22.3% relative improvement on Wow and 24.8% on Fisher over random selection, with consensus strongest and NER cheaper.

**Limit:** The gains are bounded to the two English corpora, model ensemble, filtering thresholds, and author-reported WER; other domains and languages remain unresolved.

#### NIRANTAR: Continual Learning with New Languages and Domains on Real-world Speech Data

**Why this belongs:** The preserved abstract identifies a speech object and bounded intervention that instantiate crosslingual-transfer under multilingual-and-crosslingual; this upgrades a provisional candidate to analyst-reviewed taxonomy membership only.

**Mechanism:** NIRANTAR contains 3,250 hours from 22 languages and 208 Indian districts, with non-uniform episodes and human transcripts; existing continual-learning methods are compared.

**Mathematical/evaluation object:** The central objects are recognition error over time and retention after each episode; the framework separates language and domain changes instead of averaging them away.

**Reported evidence:** The paper finds that no single evaluated method performs consistently across the three scenarios.

**Limit:** This is a benchmark and comparative study, not proof that one method is universally best; the geography, languages, episode order, and ASR models define the boundary.

#### The NaijaVoices Dataset: Cultivating Large-Scale, High-Quality, Culturally-Rich Speech Data for African Languages

**Why this belongs:** A culturally rich African-language dataset addresses unequal speech resources by changing who and which varieties are represented.

**Mechanism:** NaijaVoices contains 1,800 hours from more than 5,000 speakers; the paper analyzes acoustic diversity and fine-tunes Whisper, MMS, and XLSR.

**Mathematical/evaluation object:** Word error rate compares models before and after the new data; corpus scale and speaker diversity are part of the intervention.

**Reported evidence:** The paper reports average WER improvements of 75.86% for Whisper, 52.06% for MMS, and 42.33% for XLSR.

**Limit:** The corpus languages, collection process, transcription policy, and model choices bound the result; coverage of other African languages and deployment conditions remains open.

#### A Multi-Dialectal Dataset for German Dialect ASR and Dialect-to-Standard Speech Translation

**Why this belongs:** A multi-dialect dataset makes German variety differences part of the recognition and translation target instead of normalizing them away.

**Mechanism:** The dataset crosses three Southeast German dialect groups and Standard German; paired transcription conventions make both recognition fidelity and normalization visible.

**Mathematical/evaluation object:** Dialect identity is a structured source of variation, not merely noise: evaluation can distinguish preserving dialect words from mapping them to a standardized target.

**Reported evidence:** Betthupferl provides four hours of dialect speech plus Standard German and reports model-dependent differences in recognition and translation behavior across dialect groups.

**Limit:** Read speech, regional coverage, speaker sampling, benchmark size, and translation direction constrain the conclusions; dataset inclusion does not guarantee broad fairness or dialect preservation in deployed systems.

#### The ML-SUPERB 2.0 Challenge: Towards Inclusive ASR Benchmarking for All Language Varieties

**Why this belongs:** The benchmark includes 200+ languages, accents, and dialects so multilingual ASR claims are tested across varieties.

**Mechanism:** ML-SUPERB 2.0 evaluates models on 200+ languages, accents, and dialects through DynaBench and compares five challenge submissions with baselines.

**Mathematical/evaluation object:** Language-identification accuracy and character error rate are reported separately for general, accented, and dialectal speech.

**Reported evidence:** The best submission reports 23% absolute LID improvement and 18% CER reduction generally, with 30.2% lower CER and 15.7% higher LID accuracy on accented/dialectal data.

**Limit:** Challenge submissions, test-suite composition, and hidden evaluation define the boundary; the results do not prove equal service quality for every language variety.

#### MSDA: Combining Pseudo-labeling and Self-Supervision for Unsupervised Domain Adaptation in ASR

**Why this belongs:** Unsupervised ASR adaptation uses pseudo-labels and self-supervision when target transcripts are scarce, but must filter errors before they reinforce themselves.

**Mechanism:** MSDA evaluates a two-stage Meta PL pipeline for Greek and weakly supervised ASR, with ablations of the cascade.

**Mathematical/evaluation object:** Recognition error and ablations test whether the order of self-supervision and self-training matters.

**Reported evidence:** The paper reports state-of-the-art results and finds the cascading combination necessary in its experiments.

**Limit:** The languages, pseudo-label quality, source models, and domain shifts bound the claim; robustness to severely wrong pseudo-labels remains open.

#### ADI-20: Arabic Dialect Identification dataset and models

**Why this belongs:** Arabic dialect identification needs data and labels that distinguish closely related varieties rather than treating Arabic as one language.

**Mechanism:** ADI-20 contains 3,556 hours across 19 dialects plus MSA; ECAPA-TDNN and Whisper encoder systems are evaluated.

**Mathematical/evaluation object:** F1 measures dialect identification while controlled reductions test the value of data volume and parameters.

**Reported evidence:** Using 30% of the original data causes only a small F1 decrease in the reported experiments.

**Limit:** The country/dialect inventory, labels, and data collection define the boundary; conversational code-switching and unrepresented varieties remain open.

#### Are You Being Sarcastic? Prosodic Cues to Irony Perception in German

**Why this belongs:** Irony perception depends on prosodic and cultural expectations, so the same words cannot be treated as having one fixed intention across speakers.

**Mechanism:** German utterances are presented in seven prosodic conditions to listeners from Freiburg and Trier, who classify them as sarcastic or sincere.

**Mathematical/evaluation object:** The experiment separates cue presence, accent type, region, decision, and reaction time rather than reducing intonation to one pitch average.

**Reported evidence:** Prenuclear accent presence and especially L*+H nuclear accents drive irony judgments; some conditions also yield faster ironic responses.

**Limit:** The utterances, regions, prosodic manipulations, and binary judgment task bound the result; other languages and natural conversations remain open.

#### Speech-to-Text Translation with Phoneme-Augmented CoT: Enhancing Cross-Lingual Transfer in Low-Resource Scenarios

**Why this belongs:** Phoneme-augmented speech translation makes cross-lingual transfer explicit while preserving sound distinctions important to a low-resource language.

**Mechanism:** A multilingual LLM processes speech and phonemes under a curriculum; multilingual benchmarks compare low-, zero-, and high-resource settings.

**Mathematical/evaluation object:** Phonemes form an intermediate representation that can transfer sound structure across languages, while translation quality measures the final meaning transfer.

**Reported evidence:** The paper reports improved low-resource translation and zero-resource operation, with a small high-resource tradeoff.

**Limit:** Languages, phoneme recognizer, curriculum, and benchmark define the boundary; zero-resource claims depend on what other language information is available.

#### LiRI Corpus Platform: Demonstration of a Web-Based Infrastructure for Multimodal Corpus Analysis

**Why this belongs:** The official full paper identifies a human spoken-speech object and a bounded research problem that instantiate speech-data-collection under low-resource-and-data-creation; this resolves taxonomy membership, not the paper's scientific validity.

**Mechanism:** The LiRI Corpus Platform stores and explores multimodal corpora through DQD queries and time-aligned frontends for text, audio, video, gesture, and spoken transcripts.

**Mathematical/evaluation object:** The central object is a cross-modal query over aligned annotation intervals; the platform is evaluated by the operations it makes expressible rather than by a classifier score.

**Reported evidence:** The paper demonstrates integrated storage, synchronized querying, layered annotation, and modality-specific frontends for multimodal corpus analysis.

**Limit:** This is an infrastructure demonstration, not evidence that every corpus can be aligned or that research conclusions improve; supported formats, annotations, and user workflows are the boundary.

#### The Role of Contextual Variation in Learning Cantonese Tones from Naturalistic Speech

**Why this belongs:** The official full paper identifies a human spoken-speech object and a bounded research problem that instantiate dialect-and-variety under accent-and-cultural-boundaries; this resolves taxonomy membership, not the paper's scientific validity.

**Mechanism:** Naturalistic Cantonese productions are analyzed across six tonal contrasts and compared with existing acquisition findings under the Distributional Learning Across Contexts proposal.

**Mathematical/evaluation object:** The learning signal is a distribution over contexts, not a single token; variation and acquisition difficulty are related at the contrast level.

**Reported evidence:** The paper reports that contextual variation can predict which Cantonese contrasts are easier or harder to learn when invariant cues are absent.

**Limit:** The naturalistic corpus, tone system, acquisition comparison, and distributional measures bound the inference; a prediction from correspondence is not a direct infant-learning experiment.

#### Tonal Perception in Changde Mandarin

**Why this belongs:** The official full paper identifies a human spoken-speech object and a bounded research problem that instantiate dialect-and-variety under accent-and-cultural-boundaries; this resolves taxonomy membership, not the paper's scientific validity.

**Mechanism:** Production and perception data examine T1–T4 contours and T2-T3 and T2-T4 continua using tone identification and cue analyses.

**Mathematical/evaluation object:** The key object is the listener's response curve across an acoustic continuum; categorical perception requires a sharp boundary and reduced cross-category sensitivity, not just different labels.

**Reported evidence:** T1 is high-level, T2 low-rising, T3 falling rather than level, and the T2-T3 and T2-T4 continua do not meet typical categorical-perception standards.

**Limit:** The Changde variety, speakers, stimuli, cue manipulation, and category criteria bound the result; it should not be generalized to Standard Mandarin or all tonal perception.

#### Lexical competition in the process of Cantonese tone merging: Diverse Impact Mechanisms Across Different Individuals and Tone Pairs

**Why this belongs:** The official full paper identifies a human spoken-speech object and a bounded research problem that instantiate dialect-and-variety under accent-and-cultural-boundaries; this resolves taxonomy membership, not the paper's scientific validity.

**Mechanism:** Cantonese tone production is measured for speakers with no clear merger, one merged pair, or multiple merged pairs; lexical competition is compared across pairs.

**Mathematical/evaluation object:** The relevant object is an individual, context-conditioned distribution rather than a population average; different effects reveal inhibition, promotion, or no change.

**Reported evidence:** Competition helps maintain contrasts in some speakers, consistently inhibits one pair, has three patterns for another, and has little effect in speakers merging all three tones.

**Limit:** The Cantonese pairs, speaker groups, lexical measure, and production task bound the result; it is evidence about a change process, not a forecast of every speaker's future pronunciation.

#### SpokenNativQA: Multilingual Everyday Spoken Queries for LLMs

**Why this belongs:** Everyday multilingual spoken queries test whether a language model handles language choice and meaning together instead of translating an artificial sentence list.

**Mechanism:** SpokenNativQA contains about 33,000 spoken questions and answers across multilingual, low-resource, and dialect-rich settings; ASR systems and LLMs are benchmarked on the resulting task.

**Mathematical/evaluation object:** The benchmark keeps acoustic variability in the input and evaluates the chain from speech recognition to answer generation rather than text QA alone.

**Reported evidence:** The paper introduces the dataset, releases data and scripts, and reports comparative ASR and LLM results for spoken QA.

**Limit:** Language coverage, annotation, question domains, ASR errors, and answer scoring bound the result; a benchmark does not establish equal usefulness across all represented communities.

#### Speechless: Speech Instruction Training Without Speech for Low Resource Languages

**Why this belongs:** Low-resource languages need useful speech instruction without assuming large speech corpora; the method shifts supervision toward language and text resources.

**Mechanism:** Speechless uses text-generated instructions, aligns their semantic representations with Whisper encoder representations, and fine-tunes an LLM so it can process spoken commands in low-resource settings.

**Mathematical/evaluation object:** The method removes the unavailable waveform generator from the training loop while retaining a shared semantic space; alignment is the bridge between written supervision and spoken input.

**Reported evidence:** The paper reports that speech-instruction training without TTS can preserve spoken-instruction understanding and offers a simpler route for low-resource languages.

**Limit:** The language, synthetic text, Whisper encoder, alignment quality, and downstream command tasks bound the result; semantic alignment is not proof that pronunciation, prosody, or real user speech are fully represented.

#### Nosey: Open-Source Hardware for Acoustic Nasalance

**Why this belongs:** An open acoustic-nasalance device changes what can be collected about speech, connecting low-cost hardware to new clinical and language resources.

**Mechanism:** Nosey is a 3-D-printable baffle with replaceable dual microphone clips and open files; the study compares it with an icSpeech device for speakers and phonological environments.

**Mathematical/evaluation object:** Nasalance is computed as nasal energy divided by nasal plus oral energy; the important test is whether oral/nasal contrasts and their variation are preserved, not whether raw percentages match exactly.

**Reported evidence:** Nosey produces consistently higher raw nasalance scores, but preserves comparable phonological-environment contrasts under the tested conditions and offers a lower-cost customizable platform.

**Limit:** The tested speakers, microphones, baffle geometry, placement, and phonological materials bound the comparison; raw-score offsets and cross-signal bleed prevent treating Nosey and commercial values as directly interchangeable.

#### Speech LLMs in Low-Resource Scenarios: Data Volume Requirements and the Impact of Pretraining on High-Resource Languages

**Why this belongs:** Low-resource speech language models ask how much data is needed before a model learns a language's structure rather than memorizing a small set of examples.

**Mechanism:** Using SLAM-ASR with Whisper-large-v3-turbo and multilingual or monolingual LLMs, the paper varies training volume and projector pretraining, including Galician benchmarks.

**Mathematical/evaluation object:** The projector is a learned translation between acoustic representations and language-model tokens; data-volume curves distinguish transferred alignment from new language-specific learning, while WER measures recognition.

**Reported evidence:** The paper reports that multilingual projector pretraining reduces the impact of scarce data; for Galician it reports WERs such as 13.3% on Common Voice and 19.4% on FLEURS in one configuration.

**Limit:** Language choice, data cleanliness, projector, LLM, benchmark split, and WER bound the claim; transfer from high-resource languages does not establish equal performance or cultural adequacy.

#### Transcribing Oral History Recordings Using the Transcription Portal

**Why this belongs:** Oral-history transcription must adapt tools and review practices to long, noisy, historically varied recordings.

**Mechanism:** The Transcription Portal provides a GUI with three steps—ASR, manual correction, and data export—supports several languages, and demonstrates the workflow on historical Italian Ravensbrück interviews.

**Mathematical/evaluation object:** The system treats human correction as part of the measurement pipeline: ASR supplies a draft, the user supplies local knowledge, and the exported transcript records the corrected artifact.

**Reported evidence:** The paper reports a usable multilingual portal and demonstrates it on oral-history recordings, with summarization and translation identified as future extensions.

**Limit:** The demonstration corpus, user effort, ASR model, correction time, and export format bound the result; a convenient workflow does not establish transcription accuracy without an error audit or independent user study.

#### Tonal Variation and Word Meaning in Taiwanese

**Why this belongs:** Taiwanese tone realization changes with word meaning, so phonetic variation cannot be interpreted without linguistic context.

**Mechanism:** Acoustic tone measurements are grouped by lexical/semantic context, allowing meaning-induced variation to be separated from categorical tone effects.

**Mathematical/evaluation object:** The analysis treats linguistic meaning as a conditioning variable in the acoustic realization, not as nuisance variance to average away.

**Reported evidence:** Word meaning explains part of tonal variability; after accounting for it, the reported sandhi/citation difference disappears.

**Limit:** Speaker sample, spontaneous corpus, lexical items, tone context, and statistical model bound transfer; one tone pattern is not the whole Taiwanese system.

#### Speech transcription from South Tyrolean Dialect to Standard German with Whisper

**Why this belongs:** Transcribing a South Tyrolean dialect into Standard German requires deciding what variation to preserve and what to normalize.

**Mechanism:** The paper fine-tunes Whisper for South Tyrolean dialect speech to Standard German text, uses a small manually annotated plus synthetic corpus, and optimizes the task for archival audiovisual material.

**Mathematical/evaluation object:** Recognition and translation are coupled in the output contract: the model need not first produce a standard transcript if training directly links dialect audio to standard written text; BLEU and error measures test the product.

**Reported evidence:** The paper reports a BLEU score of 86.18 and substantial improvement over its baselines, with an existing heritage-archive use case.

**Limit:** Small corpus, synthetic data, dialect region, reference translations, BLEU, and deployment domain bound the claim; high translation score does not establish coverage of every speaker or dialect context.

#### ViToSA: Audio-Based Toxic Spans Detection on Vietnamese Speech Utterances

**Why this belongs:** Toxic-span detection in Vietnamese speech must identify harmful meaning in a particular language rather than assume that an English-trained boundary transfers directly.

**Mechanism:** ViToSA builds an audio dataset and task for locating toxic spans in Vietnamese speech utterances.

**Mathematical/evaluation object:** The prediction target is localized: the system must connect acoustic input to a particular interval or word span rather than only assign a sentence label.

**Reported evidence:** The paper reports benchmark results for Vietnamese audio toxic-span detection.

**Limit:** Dataset construction, annotation agreement, language, ASR errors, and social context bound the result; a benchmark score is not a complete safety policy.

#### The Faetar Speech Recognition Benchmark

**Why this belongs:** The preserved abstract identifies a speech object and bounded intervention that instantiate speech-data-collection under low-resource-and-data-creation; this upgrades a provisional candidate to analyst-reviewed taxonomy membership only.

**Mechanism:** The paper introduces the Faetar Speech Recognition Benchmark.

**Mathematical/evaluation object:** Benchmark construction is part of scientific knowledge: the dataset fixes what counts as an error and makes future improvements distinguishable from changes in collection or split.

**Reported evidence:** The paper reports the benchmark resources and baseline recognition results for Faetar.

**Limit:** Corpus size, speakers, dialect coverage, transcription conventions, and split design bound conclusions about the wider language community.

#### Simultaneous Speech Translation Integrated Compact Multiple Sound Spot Synthesis System On A Laptop Carried Out With A Backpack

**Why this belongs:** The title and preserved abstract identify a speech object and bounded intervention that instantiate crosslingual-transfer under multilingual-and-crosslingual; this resolves taxonomy membership only.

**Mechanism:** The paper presents a simultaneous speech-translation system integrated with compact multiple sound-spot synthesis on a laptop carried in a backpack.

**Mathematical/evaluation object:** The system boundary is the product: recognition, translation, timing, and spatialized output must jointly meet latency and resource constraints rather than optimize isolated modules.

**Reported evidence:** The paper reports an integrated portable-system demonstration and evaluation.

**Limit:** Language pair, overlap conditions, hardware, latency measurement, and user setting limit generalization to broad simultaneous conversation.

#### Evaluating Large Language Models in Data Generation for Low-Resource Scenarios: A Case Study on Question Answering

**Why this belongs:** Low-resource speech generation asks whether artificial examples teach a recognizer the missing variation or merely repeat the generator's assumptions.

**Mechanism:** The study evaluates LLM-generated data for low-resource spoken QA across SQuAD, Spoken SQuAD, and Turkish spoken QA.

**Mathematical/evaluation object:** Data generation is a controlled source of coverage: the useful question is not whether synthetic examples look plausible, but whether they improve the target speech task under restricted human supervision.

**Reported evidence:** The paper reports relative F1 gains over restricted human-annotated training in the tested text and spoken QA settings.

**Limit:** Prompting, filtering, language, synthetic distribution, and evaluation splits limit transfer; synthetic gains do not establish factual or linguistic quality everywhere.

#### Teacher-Free Knowledge Distillation for Improving Short-Utterance Spoken Language Identification

**Why this belongs:** Short utterances contain non-speech, names, fillers, and overlaps that make language identification ambiguous; label smoothing targets that uncertainty.

**Mechanism:** The paper proposes teacher-free knowledge distillation for short-utterance spoken language identification.

**Mathematical/evaluation object:** The soft target is an accumulated view of what the model reliably knows; uncertainty and segment quality shape how much each example changes the decision boundary.

**Reported evidence:** The paper reports consistent Cavg improvements in same-corpus and cross-corpus short-utterance evaluations.

**Limit:** Languages, out-of-scope composition, duration, label updates, and corpora bound the result; better short-segment ID does not solve open-set detection generally.

#### Multi-view Fusion and Parameter Perturbation for Few-Shot Class-Incremental Audio Classification

**Why this belongs:** Few-shot class-incremental audio learning must add new categories without erasing the old ones when labeled examples are scarce.

**Mechanism:** The paper proposes multi-view fusion and parameter perturbation for few-shot class-incremental audio classification.

**Mathematical/evaluation object:** Adaptation is a balance between plasticity and retention: multiple views supply evidence while controlled perturbation tests whether a decision is stable rather than memorized.

**Reported evidence:** The paper reports class-incremental classification results against the tested baselines.

**Limit:** Class order, shots, audio domains, perturbation settings, and memory protocol bound the result; benchmark retention does not establish lifelong robustness.

#### Self-Supervised Models of Speech Processing for Haitian Creole

**Why this belongs:** Haitian Creole recognition compares monolingual and multilingual pretraining to test when transfer helps a lower-resource language.

**Mechanism:** The paper develops self-supervised speech-processing models for Haitian Creole and compares monolingual, multilingual, and French-derived initialization.

**Mathematical/evaluation object:** Representation quality depends on language fit as well as parameter count; a smaller language-specific model can win when its pretraining signal matches the target speech.

**Reported evidence:** The paper reports monolingual models that are competitive with or surpass larger multilingual alternatives on the tested ASR tasks.

**Limit:** Data volume, speakers, orthography, model size, pretraining compute, and evaluation domain limit generalization to the broader Creole speech community.

#### Few-Shot Speech Deepfake Detection Adaptation with Gaussian Processes

**Why this belongs:** Few-shot deepfake detection tests whether a detector can adapt to a new attack from very little evidence without mistaking speaker or channel variation for fakery.

**Mechanism:** The paper studies few-shot adaptation for speech deepfake detection with Gaussian processes.

**Mathematical/evaluation object:** The probabilistic adapter separates learning the new attack boundary from pretending that a few examples define it with certainty; uncertainty can guide conservative decisions.

**Reported evidence:** The paper reports few-shot detection adaptation results against the tested baselines.

**Limit:** Attack families, kernel choices, calibration, shots, and base detector limit generalization; uncertainty estimates are not automatically reliable under distribution shift.

#### Extending the Fongbe to French Speech Translation Corpus:  resources, models and benchmark

**Why this belongs:** The preserved abstract identifies a speech object and bounded intervention that instantiate crosslingual-transfer under multilingual-and-crosslingual; this upgrades a provisional candidate to analyst-reviewed taxonomy membership only.

**Mechanism:** The paper extends the Fongbe-to-French speech translation corpus and presents resources, models, and a benchmark.

**Mathematical/evaluation object:** Resource creation and modeling are one research object: a stable corpus fixes what progress means and reveals where transfer from high-resource languages fails.

**Reported evidence:** The paper reports corpus additions, baseline models, and benchmark results for Fongbe-to-French speech translation.

**Limit:** Corpus size, speakers, alignment, transcription, translation references, and split design bound generalization to Fongbe communities and other low-resource pairs.

#### Pushing the Limits of Beam Search Decoding  for Transducer-based ASR models

**Why this belongs:** Beam-search choices determine how a recognizer spends limited modeling capacity when transducer decoding must scale.

**Mechanism:** The paper pushes the limits of beam-search decoding for transducer-based ASR models.

**Mathematical/evaluation object:** Decoding is an inference budget: the beam is a controlled approximation to sequence search, and improvements come from spending computation where competing hypotheses remain plausible.

**Reported evidence:** The paper reports decoding accuracy and efficiency findings for transducer ASR across the tested search settings.

**Limit:** Model, language, beam policy, pruning, hardware, and streaming setup bound the result; a better beam does not remove acoustic or language-model errors.

#### ArticulateX: End-to-End Monolingual Speech Translation in Articulator Space

**Why this belongs:** The preserved abstract identifies a speech object and bounded intervention that instantiate crosslingual-transfer under multilingual-and-crosslingual; this upgrades a provisional candidate to analyst-reviewed taxonomy membership only.

**Mechanism:** ArticulateX is an end-to-end monolingual speech translation system operating in articulator space.

**Mathematical/evaluation object:** The proposed bridge changes the unit of translation: vocal-tract movement is treated as a structured intermediate constraint between sound and language.

**Reported evidence:** The paper reports speech-translation results for the articulator-space system in its tested monolingual setting.

**Limit:** Language, corpus, articulatory estimation, model, references, and evaluation bound generalization; an intermediate representation is not proof of human-like translation.

#### Automatic Speech Recognition for Low-Resourced Middle Eastern Languages

**Why this belongs:** Recognition for low-resourced Middle Eastern languages is first a data and coverage problem; model results cannot be separated from which speakers and varieties were recorded.

**Mechanism:** The paper studies automatic speech recognition for low-resourced Middle Eastern languages.

**Mathematical/evaluation object:** Low-resource ASR is an infrastructure problem as well as a model problem: a documented corpus and baseline expose which errors come from missing data versus model choice.

**Reported evidence:** The paper reports resources, baselines, and recognition results for the covered Middle Eastern languages.

**Limit:** Language selection, dialect, corpus size, transcription, speakers, and evaluation splits limit generalization across the region.

#### Novel Parasitic Dual-Scale Modeling for Efficient and Accurate Multilingual Speech Translation

**Why this belongs:** The title and preserved abstract identify a speech object and bounded intervention that instantiate crosslingual-transfer under multilingual-and-crosslingual; this resolves taxonomy membership only.

**Mechanism:** The paper proposes novel parasitic dual-scale modeling for efficient and accurate multilingual speech translation.

**Mathematical/evaluation object:** The model divides capacity by scale: shared computation handles reusable patterns, while finer or conditional structure protects language-specific translation behavior.

**Reported evidence:** The paper reports multilingual translation accuracy and efficiency improvements for the tested language set.

**Limit:** Languages, directions, data imbalance, parameter budget, decoding, and metrics bound the result; efficiency on a benchmark is not equal quality for every language.

#### An Effective Training Framework for Light-Weight Automatic Speech Recognition Models

**Why this belongs:** A lightweight ASR training framework asks how to retain useful recognition with limited model and data resources.

**Mechanism:** The paper proposes an effective training framework for lightweight automatic speech-recognition models.

**Mathematical/evaluation object:** Efficiency is a constraint on the whole training-and-inference pipeline: the model must spend its limited capacity on speech distinctions that matter for the target device.

**Reported evidence:** The paper reports lightweight ASR accuracy and resource results for the proposed framework.

**Limit:** Hardware, language, model family, data, latency measurement, and compression settings limit generalization; a benchmark model is not a deployment guarantee.

#### Efficient Multilingual ASR Finetuning via LoRA Language Experts

**Why this belongs:** The preserved abstract identifies a speech object and bounded intervention that instantiate crosslingual-transfer under multilingual-and-crosslingual; this upgrades a provisional candidate to analyst-reviewed taxonomy membership only.

**Mechanism:** The paper proposes efficient multilingual ASR fine-tuning via LoRA language experts.

**Mathematical/evaluation object:** Parameter-efficient adaptation allocates change selectively: shared parameters carry reusable acoustics while experts absorb language-specific pronunciation and decoding behavior.

**Reported evidence:** The paper reports multilingual ASR accuracy and efficiency results for LoRA language experts.

**Limit:** Languages, data balance, rank, routing, base model, and evaluation domains bound the claim; parameter efficiency does not guarantee fairness across languages.

#### Hybrid Data Sampling for ASR: Integrating Acoustic Diversity and Transcription Uncertainty

**Why this belongs:** Selecting acoustically diverse and uncertain utterances treats annotation budget as a design problem for speech data.

**Mechanism:** The paper proposes hybrid data sampling for ASR by integrating acoustic diversity and transcription uncertainty.

**Mathematical/evaluation object:** Data selection is a coverage-allocation problem: diversity broadens the conditions seen, while uncertainty targets the model's unresolved boundary.

**Reported evidence:** The paper reports ASR improvements from hybrid sampling relative to the tested selection strategies.

**Limit:** Acoustic representation, uncertainty estimator, corpus, budget, language, and split bound the result; a sampling score is not a complete measure of data value.

#### LIST: Language-Independent Speech Token for Multilingual Speech Synthesis with Language Models

**Why this belongs:** The title and preserved abstract identify a speech object and bounded intervention that instantiate crosslingual-transfer under multilingual-and-crosslingual; this resolves taxonomy membership only.

**Mechanism:** LIST is a language-independent speech token for multilingual speech synthesis with language models.

**Mathematical/evaluation object:** The token is a cross-language interface: shared units carry reusable speech structure, while language conditioning reconstructs the differences needed for intelligible output.

**Reported evidence:** The paper reports multilingual synthesis quality and cross-language token behavior for LIST.

**Limit:** Languages, token rate, codebook, speakers, conditioning, and evaluation metrics bound the claim; shared tokens do not guarantee equal quality.

#### An Exploratory Framework for LLM-assisted Human Annotation of Speech Datasets

**Why this belongs:** The title and preserved abstract identify a speech problem whose object and intended intervention fit speech-data-collection under low-resource-and-data-creation; the assignment does not claim performance beyond the available source.

**Mechanism:** The paper presents an exploratory framework for LLM-assisted human annotation of speech datasets.

**Mathematical/evaluation object:** Annotation is a coordination loop: the model proposes, the human adjudicates, and the system records evidence so speed does not replace accountability.

**Reported evidence:** The paper reports framework behavior and exploratory annotation findings for the tested speech data tasks.

**Limit:** Task, annotator expertise, model, prompts, disagreement policy, and audit trail bound the result; assistance is not a substitute for label validity.

#### SawtArabi: A Benchmark Corpus for Arabic TTS.  Standard, Dialectal and Code-Switching

**Why this belongs:** A TTS benchmark must represent standard Arabic, dialects, and code-switching so one average voice score does not hide language variation.

**Mechanism:** SawtArabi is a benchmark corpus for Arabic TTS spanning standard, dialectal, and code-switching speech.

**Mathematical/evaluation object:** Corpus design exposes variation as a modeling requirement: the system must preserve identity and naturalness while changing or mixing language variety.

**Reported evidence:** The paper reports corpus resources and baseline TTS evaluations across the covered Arabic conditions.

**Limit:** Variety coverage, speaker balance, text design, switching labels, and listening tests bound generalization across Arabic communities.

#### Audio-Based Classification and Geographic Regression of Austrian Dialects

**Why this belongs:** Dialect classification links acoustic variation to geographic regions without assuming that a dialect boundary is a clean speaker boundary.

**Mechanism:** The model learns speech representations for hierarchical classification and a continuous coordinate prediction; held-out speaker and location splits test whether regional structure survives identity variation.

**Mathematical/evaluation object:** Classification partitions a geographic continuum while regression measures distance in kilometers, so the two tasks expose different resolutions and failure modes of dialect modeling.

**Reported evidence:** The Austrian dataset covers 304 speakers at 108 locations; wav2vec 2.0 reports an average geographic test error of 66.7 km in the paper's evaluation.

**Limit:** Sampling density, speaker augmentation, Austrian dialect geography, split design, and recording conditions limit transfer; geographic prediction is not a complete sociolinguistic account of dialect.

#### On the Relationship between Accent Strength and Articulatory Features

**Why this belongs:** Accent strength is related to inferred articulatory differences, making pronunciation variation a physical rather than purely label-based boundary.

**Mechanism:** Self-supervised articulatory inversion estimates tongue and related articulator features; phoneme-level deviations from dictionary references provide the comparison variable across American and British English.

**Mathematical/evaluation object:** The analysis links two imperfect measurements—phonological deviation and inferred movement—so correlation tests whether an accent proxy has a plausible production-level signature.

**Reported evidence:** The paper reports dialect differences in tongue positioning, especially for rhotic and low-back vowels, and associations between derived articulatory parameters and indexed accent strength.

**Limit:** Read speech, two dialect groups, dictionary assumptions, inversion error, and correlation do not establish a universal accent scale or causal articulatory explanation.

#### Are loan sequences different from foreign sequences? A perception study with Japanese listeners on coronal obstruent – high front vowel sequences

**Why this belongs:** Listeners’ native phonotactics and language experience change how unfamiliar speech sequences are discriminated.

**Mechanism:** Japanese listeners discriminate /ti/ and /zi/ contrasts in an online task; sequence status and self-reported English input are tested as competing explanations.

**Mathematical/evaluation object:** Phonotactic knowledge acts as a prior over possible sequences, but the experiment tests whether that prior fully determines auditory discrimination.

**Reported evidence:** Thirty-nine listeners performed better on the loanword-permitted sequence, though the foreign sequence was also often discriminated; self-reported English input did not explain the result.

**Limit:** Online testing, sequence choices, speaker exposure, sample size, and self-report limit generalization; discrimination is not equivalent to lexical access or translation competence.

#### Open Universal Arabic ASR Leaderboard

**Why this belongs:** The preserved abstract identifies a speech object and bounded intervention that instantiate dialect-and-variety under accent-and-cultural-boundaries; this upgrades a provisional candidate to analyst-reviewed taxonomy membership only.

**Mechanism:** The benchmark fixes model/data/evaluation axes across six test corpora and records WER plus resource and adaptation measurements.

**Mathematical/evaluation object:** A leaderboard is a measurement design: the set of dialects and denominators determines which kind of generalization is visible.

**Reported evidence:** The paper reports broad comparative results and identifies differences in dialect robustness, speaker adaptation, inference efficiency, and memory use.

**Limit:** Corpus selection, language variety, transcription conventions, model versions, and leaderboard maintenance bound the conclusion; rankings are not a causal explanation of dialect performance.

#### Prosodically Enhanced Foreign Accent Simulation by Discrete Token-based Resynthesis Only with Native Speech Corpora

**Why this belongs:** The preserved abstract identifies a speech object and bounded intervention that instantiate accent-robustness under accent-and-cultural-boundaries; this upgrades a provisional candidate to analyst-reviewed taxonomy membership only.

**Mechanism:** Self-supervised discrete units preserve linguistic content, while duration controls alter timing before the units are rendered by a decoder; real L2 speech supplies the comparison target.

**Mathematical/evaluation object:** Accent simulation is a structured transformation: content units should stay stable while temporal realization changes in a language-specific way.

**Reported evidence:** The paper reports that the enhanced method reproduces durational accents observed in real L2 speech.

**Limit:** Accent languages, speakers, duration estimator, perceptual validation, and native-corpus assumptions bound transfer; acoustic similarity is not proof of improved ASR or pedagogy.

#### A Multimodal Chinese Dataset for Cross-lingual Sarcasm Detection

**Why this belongs:** The captured official PDF and abstract identify a speech object and mechanism instantiating accent-robustness under accent-and-cultural-boundaries; this upgrades evidence depth for the structured note and does not establish independent reproduction.

**Mechanism:** Subgroup and accent-conditioned evaluation separates intended-word performance across varieties rather than hiding failures in an aggregate.

**Mathematical/evaluation object:** Robustness is a boundary measurement: the system's norm becomes visible only when varieties are evaluated separately.

**Reported evidence:** The paper reports a study of multilingual/accent robustness and its implications for ASR evaluation.

**Limit:** Accent labels, languages, speakers, test design, and subgroup denominators bound transfer.

#### Tonal Contrasts in the Malipo Variety of the Mienic Language

**Why this belongs:** The captured official PDF and abstract identify a speech object and mechanism instantiating dialect-and-variety under accent-and-cultural-boundaries; this upgrades the structured note to D3 without establishing independent reproduction.

**Mechanism:** Contrastive measurements expose which acoustic distinctions carry linguistic information.

**Mathematical/evaluation object:** The paper treats dialect-and-variety as a structured evidence-to-decision problem: Contrastive measurements expose which acoustic distinctions carry linguistic information.

**Reported evidence:** The paper reports an empirical study of tonal contrasts in a Mienic variety.

**Limit:** Speaker sample, elicitation design, tonal context, and language-specific scope bound transfer.

### Synthesis boundary

These papers share a conceptual pressure, but this seed batch does not justify ranking methods, estimating prevalence, or claiming that the mechanism generalizes across speakers, languages, rooms, or tasks. Those claims require additional assignments and comparable denominators.

## Evidence, practical systems, and consequences

**Ordinary pressure:** Speech systems are used through microphones, networks, interfaces, policies, and people; a benchmark number is only one observation of that whole chain.

**Naive strategy that breaks:** Reporting one average score on one dataset encourages the reader to treat a proxy as universal ability and ignores latency, failure recovery, privacy, and misuse.

**Recurring move:** Align the evaluation with the real target, expose subgroup and condition variation, account for the full system boundary, and preserve an audit trail from evidence to claim.

**Boundary:** Broader evaluation costs time and data, but narrow evidence can create false confidence exactly where speech systems affect access, identity, or safety.

**D3 evidence status:** 59 reviewed paper(s); the family claim below is limited to these examples.

**Conceptual family represented:** `metric-and-human-targets/quality-and-naturalness`, `privacy-and-security/spoofing-and-deepfake`, `metric-and-human-targets/quality-and-naturalness`, `privacy-and-security/spoofing-and-deepfake`, `robustness-and-shift/distribution-shift`, `auditability-and-accountability/auditability-and-contestability`, `privacy-and-security/voice-privacy`, `metric-and-human-targets/calibration-and-selective-use`, `privacy-and-security/spoofing-and-deepfake`, `privacy-and-security/spoofing-and-deepfake`, `deployment-cost/latency-and-resource`, `metric-and-human-targets/quality-and-naturalness`, `robustness-and-shift/distribution-shift`, `metric-and-human-targets/word-error-versus-understanding`, `metric-and-human-targets/word-error-versus-understanding`, `privacy-and-security/spoofing-and-deepfake`, `privacy-and-security/spoofing-and-deepfake`, `metric-and-human-targets/quality-and-naturalness`, `deployment-cost/latency-and-resource`, `metric-and-human-targets/quality-and-naturalness`, `privacy-and-security/spoofing-and-deepfake`, `robustness-and-shift/end-to-end-recovery`, `privacy-and-security/spoofing-and-deepfake`, `metric-and-human-targets/quality-and-naturalness`, `metric-and-human-targets/calibration-and-selective-use`, `metric-and-human-targets/calibration-and-selective-use`, `metric-and-human-targets/word-error-versus-understanding`, `privacy-and-security/spoofing-and-deepfake`, `deployment-cost/latency-and-resource`, `deployment-cost/latency-and-resource`, `deployment-cost/latency-and-resource`, `deployment-cost/latency-and-resource`, `deployment-cost/latency-and-resource`, `metric-and-human-targets/quality-and-naturalness`, `metric-and-human-targets/word-error-versus-understanding`, `deployment-cost/latency-and-resource`, `auditability-and-accountability/auditability-and-contestability`, `privacy-and-security/spoofing-and-deepfake`, `privacy-and-security/spoofing-and-deepfake`, `privacy-and-security/spoofing-and-deepfake`, `privacy-and-security/spoofing-and-deepfake`, `privacy-and-security/voice-privacy`, `privacy-and-security/spoofing-and-deepfake`, `privacy-and-security/spoofing-and-deepfake`, `auditability-and-accountability/auditability-and-contestability`, `robustness-and-shift/end-to-end-recovery`, `metric-and-human-targets/calibration-and-selective-use`, `deployment-cost/latency-and-resource`, `metric-and-human-targets/calibration-and-selective-use`, `robustness-and-shift/end-to-end-recovery`, `metric-and-human-targets/word-error-versus-understanding`, `metric-and-human-targets/quality-and-naturalness`, `privacy-and-security/voice-privacy`, `privacy-and-security/voice-privacy`, `robustness-and-shift/distribution-shift`, `metric-and-human-targets/quality-and-naturalness`, `robustness-and-shift/end-to-end-recovery`, `deployment-cost/latency-and-resource`, `deployment-cost/latency-and-resource`.

### What the papers make concrete

#### Enabling the replicability of speech synthesis perceptual evaluations

**Why this belongs:** The contribution is a reproducible perceptual-evaluation procedure; it belongs to the problem of what a listener score establishes and how to report it.

**Mechanism:** Audit the goal, dataset and bias, participant cohort, protocol, analysis, conclusions, and limitations, then package evaluation assets and procedures.

**Mathematical/evaluation object:** The central object is an auditable mapping from hypothesis to stimuli, ratings, uncertainty, and conclusion.

**Reported evidence:** The paper reports a structured template intended to make subjective speech-synthesis studies more reproducible and limitations more visible.

**Limit:** A checklist cannot guarantee participant representativeness, perceptual validity, or exact replication when access differs.

#### ATMM-SAGA: Alternating Training for Multi-Module with Score-Aware Gated Attention SASV system

**Why this belongs:** The SASV system combines claimed-speaker evidence with anti-spoofing evidence because a voice match alone does not establish an authentic speaker.

**Mechanism:** Speaker and spoof-related representations are produced separately, gates weight evidence according to scores, and the final decision combines identity and authenticity signals; trials measure both acceptance and rejection errors.

**Mathematical/evaluation object:** Verification uses similarity scores and a decision threshold; gated attention learns weights over module outputs, while SASV metrics summarize target, nontarget, and spoof trial errors.

**Reported evidence:** The paper reports an alternating multi-module SASV system with score-aware gating and evaluates it on speaker-authentication trials.

**Limit:** Thresholds and spoof types determine operating behavior; benchmark attacks do not exhaust unseen synthesis or replay conditions. No independent reproduction was performed.

#### SMARTMOS: Modeling Subjective Audio Quality Evaluation for Real-Time Applications

**Why this belongs:** The paper predicts subjective audio-quality judgments for real-time use, directly addressing the gap between a cheap proxy and what listeners actually report.

**Mechanism:** Audio examples and human scores are used to train a predictor; its estimates are compared with held-out subjective ratings across conditions and computational constraints.

**Mathematical/evaluation object:** The model minimizes prediction error against quality ratings; correlation and error against human scores measure agreement, not whether the model captures every user-relevant harm.

**Reported evidence:** The paper reports a real-time subjective-quality model intended to approximate listening-test judgments more cheaply and quickly.

**Limit:** Human ratings, test conditions, and audio distortions define the target; a predictor can reproduce annotator bias and fail on unseen codecs or populations. No independent reproduction was performed.

#### Evaluating Parameter Sharing for Spoofing-Aware Speaker Verification: A Case Study on the ASVspoof 5 Dataset

**Why this belongs:** The study treats speaker verification and spoof detection as coupled identity decisions whose shared parameters must be tested across attacks and codecs.

**Mechanism:** On ASVspoof 5, the study varies which modules share parameters and evaluates the resulting SASV systems across attack types and codec conditions, comparing min a-DCF and relative performance changes to an unshared baseline.

**Mathematical/evaluation object:** The main decision metric is minimum tandem detection cost, which combines false acceptance and false rejection costs for speaker and spoof decisions. The method question is whether shared representations improve this joint operating tradeoff.

**Reported evidence:** The paper reports min a-DCF improving from 0.329 to 0.233 for the A26 attack with parameter sharing and a 14.09% gain for AMR-compressed signals in the tested setup.

**Limit:** Benefits are attack- and codec-specific; the ASVspoof 5 protocols do not exhaust future generators or deployment channels. min a-DCF is a system-level proxy, not proof of safe authentication, and no independent reproduction was performed.

#### Unmasking real-world audio deepfakes: A data-centric approach

**Why this belongs:** The paper treats real-world data coverage and curation as the intervention needed to test whether deepfake detection survives distribution shift.

**Mechanism:** The study introduces the AI4T real-world deepfake dataset, analyzes data quality and coverage, applies data-centric filtering and augmentation, and evaluates detector systems on five public datasets plus the new set.

**Mathematical/evaluation object:** Equal error rate is the operating point where false acceptance and false rejection meet; relative EER reduction compares the data-centric system with its baseline on each dataset. The denominator is each named test corpus, not all possible real-world audio.

**Reported evidence:** The paper reports a 55% relative EER reduction on In-the-Wild to 1.7% absolute EER and a 63% reduction on AI4T after the data-centric interventions.

**Limit:** The new dataset and curation choices define the tested notion of real-world variation; future generators and channels may differ. EER is not a guarantee of safe moderation or authentication, and no independent reproduction was performed.

#### Hear Me Out: Interactive evaluation and bias discovery platform for speech-to-speech conversational AI

**Why this belongs:** The platform changes perceived speaker characteristics while holding the prompt fixed, making speaker-dependent model behavior inspectable.

**Mechanism:** Hear Me Out lets a user choose a speech foundation model, submit an original or voice-converted prompt, view the response pair, and inspect response speech rate, pitch, audio-quality dimensions, sentiment, and semantic similarity. The paired interaction makes possible a counterfactual probe of speaker characteristics.

**Mathematical/evaluation object:** The platform reports syllables per second, mean and standard-deviation F0, model-based sentiment/quality scores, and semantic textual similarity. These are diagnostic projections of behavior, not a single fairness metric or causal estimate.

**Reported evidence:** The paper demonstrates an accessible interactive evaluation experience for comparing responses to original and transformed voices and argues that it can expose speaker-dependent differences and possible bias.

**Limit:** The work is a platform/demo, not a powered user study or population-level fairness audit; its automated metrics and selected voice profiles constrain what can be observed. The authors explicitly call for larger studies and additional bias metrics, and no independent reproduction was performed.

#### WavShape: Information-Theoretic Speech Representation Learning for Fair and Privacy-Aware Audio Processing

**Why this belongs:** WavShape treats a speech embedding as an information budget: reduce dependence on sensitive attributes while retaining task-relevant speech information.

**Mechanism:** A frozen speech encoder produces embeddings, a trainable WavShape projection creates public embeddings, and a Donsker–Varadhan mutual-information estimator supplies the training signal. The estimator is removed at inference; downstream classifiers and information estimates test sensitive leakage and task retention across three datasets.

**Mathematical/evaluation object:** The objective is a weighted combination of mutual-information terms. The Donsker–Varadhan estimator uses a log moment-generating expression to lower-bound dependence; the paper reports MI changes plus downstream task performance, so the MI estimate is a proxy for leakage rather than a proof of privacy.

**Reported evidence:** The paper reports up to an 81% reduction in mutual information with sensitive attributes while retaining up to 97% of task-relevant information in its tested settings; on VCTK, gender-related MI falls from 0.40029 to 0.07493.

**Limit:** Mutual-information estimation depends on the estimator, labels, datasets, and chosen sensitive attributes; unmeasured attributes or powerful attackers may still recover information. The figures are author-reported, and no independent privacy attack or reproduction was performed.

#### Enhancing Retrieval-Augmented Audio Captioning with Generation-Assisted Multimodal Querying and Progressive Learning

**Why this belongs:** Generation-assisted multimodal retrieval tests whether audio and text evidence agree on what should be retrieved, rather than rewarding fluent captions alone.

**Mechanism:** MQ-Cap trains a connector and LoRA parameters with a cross-entropy loss over interleaved pairs. It first retrieves 25 candidates by audio similarity, then combines normalized Laion-CLAP audio and text similarities with alpha 0.5. WavCaps, AudioCaps, and Clotho provide training and knowledge-base data.

**Mathematical/evaluation object:** The pair score is S = alpha S_A + (1-alpha) S_T. On AudioCaps, MQ-Cap reports SPIDEr 0.519; on Clotho, 0.319; generation-assisted querying raises cross-modal retrieval R@1 from 44.0 to 45.3 for Laion-CLAP and from 56.0 to 59.1 for OmniBind on AudioCaps. The generated text is an intermediate measurement, not ground truth.

**Reported evidence:** Progressive learning plus generation-assisted querying improves the reported captioning scores and gives up to 3.1 percentage points of retrieval improvement; the method adds about 1.07 seconds of generation overhead to retrieval.

**Limit:** The benchmarks are AudioCaps, Clotho, and Auto-ACD with overlapping-source controls and missing test audio; retrieval quality depends on the generated caption and CLAP encoders. Results are author-reported and were not independently reproduced.

#### Beyond Attacks: Advancing Fake Speech Detection with Attack-Agnostic Methods

**Why this belongs:** Attack-invariant representations test whether fake-speech detection survives changes in attack, codec, and language.

**Mechanism:** A frozen wav2vec2 front-end and AASIST backend produce embeddings; AIED suppresses attack variation and CSD projects into a shared subspace, tested on ASVspoof and IndicTTS.

**Mathematical/evaluation object:** EER changes from 6.14 to 5.84 on LA, 12.33 to 10.90 on DF, and 59.82 to 39.51 on IndicTTS; the large cross-language gap remains.

**Reported evidence:** The paper reports 4%, 12%, and 34% relative EER improvements on LA, DF, and IndicTTS, with ablations separating AIED and CSD.

**Limit:** Datasets, attacks, frozen front-end, and language coverage bound the result; IndicTTS EER remains high and no independent adversarial evaluation was performed.

#### Codec-Based Deepfake Source Tracing via Neural Audio Codec Taxonomy

**Why this belongs:** Codec taxonomy makes fake-speech source tracing a provenance problem rather than only binary detection.

**Mechanism:** Multi-task systems on CodecFake+ use codec quantization, auxiliary codec tasks, and balanced source-tracing experiments.

**Mathematical/evaluation object:** F1 is reported for vector-quantization, auxiliary, and decoder/source tasks; the best cited DEC F1 is 46.45%.

**Reported evidence:** CodecFake+ gives initial evidence that codec taxonomy helps source tracing and that balance affects generalization.

**Limit:** The dataset and generator coverage bound the result; 46.45% F1 is not reliable attribution.

#### PruneSLU: Efficient On-device Spoken Language Understanding through Vocabulary and Structural Pruning

**Why this belongs:** Vocabulary-first and structural pruning preserve spoken-language-understanding task structure under device resource limits.

**Mechanism:** PruneSLU starts from Whisper-tiny, selects a base vocabulary, chooses layers by loss, and trains with language-model, distillation, and contrastive components on STOP and SLURP.

**Mathematical/evaluation object:** Exact match, EM-Tree, intent accuracy, slot F1, parameter counts, and pruning/loss ablations expose the tradeoff.

**Reported evidence:** The 15M model retains 98% of original STOP performance, reaches STOP EM 72.31 and SLURP slot F1 71.42, and improves on listed compression baselines.

**Limit:** STOP/SLURP domains, Whisper initialization, five seeds, and author-reported comparisons bound the result; energy and open-world commands are not tested.

#### AttentiveMOS: A Lightweight Attention-Only Model forSpeech Quality Prediction

**Why this belongs:** A small attention model predicts listener quality while exposing how MOS prediction fails under domain shift.

**Mechanism:** AttentiveMOS uses Swin and transformer attention with 86K parameters and is evaluated across in-domain, out-of-domain, and cross-domain MOS datasets.

**Mathematical/evaluation object:** MSE measures rating error while Pearson and Spearman measure agreement; SOMOS-clean reports MSE 0.257, PCC 0.449, and SRCC 0.442.

**Reported evidence:** It beats listed lightweight baselines in the reported SOMOS-clean comparison, but PCC falls to 0.359 on out-of-domain LIVETALK.

**Limit:** MOS labels, listener composition, dataset domains, and the sharp shift drop limit claims of general quality assessment.

#### Evaluating ASR Robustness to Spontaneous Speech Errors: A Study of WhisperX Using a Speech Error Database

**Why this belongs:** Annotated spontaneous speech errors map where ASR crosses failure boundaries by error type and position.

**Mechanism:** The study evaluates sound and word errors with controlled classification variables and compares initial, medial, and final positions.

**Mathematical/evaluation object:** Accuracy by error class and position reveals interactions; sound errors are reported as easier than word errors.

**Reported evidence:** Sound errors have higher transcription accuracy than word errors, with position-dependent differences.

**Limit:** Database, annotations, WhisperX, language, and task design limit generalization.

#### Aligning ASR Evaluation with Human and LLM Judgments: Intelligibility Metrics Using Phonetic, Semantic, and NLI Approaches

**Why this belongs:** An intelligibility metric combines semantic, logical, and phonetic similarity because exact word error is not the human target.

**Mechanism:** Five-fold regression learns weights from 100 transcript pairs rated by six annotators, then tests the combined score against held-out judgments.

**Mathematical/evaluation object:** The combined metric correlates 0.890 with human judgments; weights are 0.40 NLI, 0.28 semantic, and 0.32 phonetic, with MSE 0.237.

**Reported evidence:** The integrated measure outperforms individual and traditional error measures in the reported SAP evaluation.

**Limit:** One dataset, six annotators, regression assumptions, and reported correlation limit other listeners, languages, and clinical decisions.

#### Intelligibility Prediction for Time-Modified Speech Signals Using Spectro-Temporal Modulation Features

**Why this belongs:** The captured paper's ordinary problem, mechanism, and reported evaluation directly instantiate word-error-versus-understanding within metrics-and-targets.

**Mechanism:** The system uses DTW over modulation features and compares two ways of incorporating the alignment into RB-SIPAs across noise and time-modification conditions.

**Mathematical/evaluation object:** The move separates two questions that are often mixed: finding corresponding speech events and predicting whether the resulting signal is intelligible.

**Reported evidence:** The paper reports better alignment behavior and better correlation with listening scores than MFCC-based alternatives under its tested conditions.

**Limit:** The listening datasets, degradation types, chosen modulation channels, and reference availability bound the claim; correlation is not a complete model of listener experience.

#### Generalizable Audio Spoofing Detection using Non-Semantic Representations

**Why this belongs:** The captured paper's ordinary problem, mechanism, and reported evaluation directly instantiate spoofing-and-deepfake within privacy-security-and-accountability.

**Mechanism:** TRILL and TRILLsson representations are evaluated as features for a spoofing classifier across in-domain and public-domain conditions.

**Mathematical/evaluation object:** The method changes what evidence the detector is allowed to use: it seeks production artifacts that survive a change in spoken content and generator.

**Reported evidence:** The paper reports comparable in-domain performance and stronger out-of-domain results than the tested baselines.

**Limit:** The generators, corpora, representation models, and author-reported tests define the boundary; future synthesis methods and adversarial adaptation remain open.

#### PhonemeFake: Redefining Deepfake Realism with Language-Driven Segmental Manipulation and Adaptive Bilevel Detection

**Why this belongs:** Segment-level manipulation tests whether deepfake realism is judged from linguistic content and phonetic detail rather than one global acoustic score.

**Mechanism:** PhonemeFake creates segmental manipulations, measures human and benchmark deception, and trains a detector that allocates computation to suspicious regions across three datasets.

**Mathematical/evaluation object:** Equal error rate measures detection, localization checks whether manipulated regions are found, and speed measures the cost of adaptive processing.

**Reported evidence:** The paper reports up to 42% lower human perception and 94% lower benchmark accuracy for attacks; its detector reports 91% EER reduction and up to 90% speed-up.

**Limit:** These are author-reported results tied to attack construction, datasets, detector thresholds, and the chosen language reasoning; unseen generators and adversarial adaptation remain open.

#### Multivariate Probabilistic Assessment of Speech Quality

**Why this belongs:** Speech quality assessment combines several uncertain measures, asking how to represent perceived quality without pretending one score is the whole listening experience.

**Mechanism:** The model predicts a multivariate Gaussian through Cholesky factors and extends probabilistic affine transformations on NISQA ratings.

**Mathematical/evaluation object:** The mean gives a point estimate, covariance gives uncertainty and correlations, and the NISQA dimensions provide a structured target instead of one scalar.

**Reported evidence:** The paper reports state-of-the-art-level point estimation while uniquely providing uncertainty and cross-dimension correlation estimates.

**Limit:** The result is bounded to NISQA's labels and distributional assumptions; whether listeners and engineers benefit in new codecs or languages remains open.

#### Ultra-Low Bit Post-Training Quantization of Large Speech Models via K-Means Clustering and Mixed Precision Allocation

**Why this belongs:** Quantizing a large speech model changes its memory and computation boundary, so deployment requires measuring the accuracy-cost tradeoff.

**Mechanism:** The method quantizes Whisper-Large-V3 after training and compares mixed precision and outlier retention across speech datasets.

**Mathematical/evaluation object:** Bits per parameter expresses storage; WER measures recognition loss, and the columnwise allocation ties precision to the observed weight distribution.

**Reported evidence:** The paper reports 2.12-bit quantization with a 0.17 percentage-point WER increase on LibriSpeech test-clean and under 1% degradation across additional datasets.

**Limit:** The result is author-reported for Whisper-Large-V3 and tested corpora; latency, energy, hardware kernels, and other model families remain open.

#### Optimizing CLAP Reward with LLM Feedback for Semantically Aligned and Diverse Automated Audio Captioning

**Why this belongs:** Optimizing an automated audio-captioning reward raises the question of whether a metric rewards semantic coverage or merely reference style.

**Mechanism:** CRRP trains an automated audio-captioning system with a stabilized CLAP reward and an LLM evaluator; semantic, human, and AI assessments are compared.

**Mathematical/evaluation object:** The reward combines semantic alignment and language naturalness, while multiple evaluations expose metric-specific behavior.

**Reported evidence:** The paper reports strong semantic and human/AI evaluation results for the proposed reward system.

**Limit:** The result depends on caption datasets, evaluator prompts, and reward weighting; human agreement and out-of-domain audio remain open.

#### Collecting, Curating, and Annotating Good Quality Speech deepfake dataset for Famous Figures: Process and Challenges

**Why this belongs:** A curated public-figure deepfake dataset treats voice identity as a security and consent problem, not simply a synthesis-quality benchmark.

**Mechanism:** The paper creates bona-fide and synthetic speech for ten public figures and reports NISQA-TTS and human misclassification.

**Mathematical/evaluation object:** Dataset composition, automated naturalness, and human confusion measure different parts of realism.

**Reported evidence:** The dataset reports NISQA-TTS naturalness 3.69 and a highest human misclassification rate of 61.9%.

**Limit:** The ten figures, synthesis systems, listeners, and dataset protocol bound the result; new generators and adversarially chosen public speech remain open.

#### Pushing the Limits of End-to-End Diarization

**Why this belongs:** End-to-end diarization removes hand-built intermediate labels, making the evaluation sensitive to how speaker boundaries and identities fail together.

**Mechanism:** EEND-TA is evaluated on AliMeeting, AMI, DIHARD III, and MagicData RAMC with speed and diarization error comparisons.

**Mathematical/evaluation object:** Diarization error rate measures missed, false, and wrongly attributed speech; multiple corpora test transfer across meeting conditions.

**Reported evidence:** The paper reports 14.49% DER on DIHARD III and state-of-the-art results on the listed datasets.

**Limit:** The simulations, corpora, speaker counts, and model speed define the boundary; spontaneous conditions beyond these meetings remain open.

#### Audio Deepfake Source Tracing using Multi-Attribute Open-Set Identification and Verification

**Why this belongs:** Open-set deepfake tracing asks whether a system can identify an unfamiliar generating source rather than only recognize examples seen during training.

**Mechanism:** Models are trained on internal and MLAAD data and evaluated across three ASVspoof sets, MLAAD, and Blizzard23.

**Mathematical/evaluation object:** Identification asks which source class matches a few references; verification asks whether a claimed source is supported, making the decision object explicit.

**Reported evidence:** The paper reports discrimination of unseen source attributes and argues for a standardized source-tracing ontology.

**Limit:** Datasets, source taxonomy, reference count, and generator families bound the result; real-world provenance and adversarial adaptation remain open.

#### Benchmarking Time-localized Explanations for Audio Classification Models

**Why this belongs:** Time-localized explanations are evaluated as evidence about why an audio classifier decided, so explanation quality must be measured separately from classification accuracy.

**Mechanism:** The benchmark compares temporal explanation methods for audio classifiers and uses the annotations to expose spurious correlations.

**Mathematical/evaluation object:** Time-localized overlap turns an explanation into a measurable alignment problem; the proxy is useful but is not a causal proof of model reasoning.

**Reported evidence:** The paper reports near-perfect explanations for some methods and shows their use in finding spurious correlations.

**Limit:** Event annotations, task type, explanation method, and proxy definition bound the claim; faithfulness under distribution shift remains open.

#### Multimodal and Multitask Learning for Predicting Multiple Scores in L2 English Speech

**Why this belongs:** The official full paper identifies a human spoken-speech object and a bounded research problem that instantiate calibration-and-selective-use under metrics-and-targets; this resolves taxonomy membership, not the paper's scientific validity.

**Mechanism:** MFCC, wav2vec 2.0, GloVe, and BERT embeddings are compared on five L2 English scores with a trait-aware loss and mean Pearson correlation as the main measure.

**Mathematical/evaluation object:** The prediction target is a vector of human-assigned traits; cross-modal attention and the joint loss encode dependencies that a single aggregate score discards.

**Reported evidence:** The wav2vec 2.0 plus BERT configuration reports the best mean PCC, 0.734 with standard deviation 0.0129 across the five criteria, above unimodal and baseline multimodal systems.

**Limit:** The learner dataset, rubric, rater scores, split, and correlation metric bound the result; correlation is not agreement or evidence that the model understands proficiency.

#### On the reliability of feature attribution methods for speech classification

**Why this belongs:** The official full paper identifies a human spoken-speech object and a bounded research problem that instantiate calibration-and-selective-use under metrics-and-targets; this resolves taxonomy membership, not the paper's scientific validity.

**Mechanism:** Experiments use TIMIT and Common Voice with gradient-based saliency and integrated gradients; word-aligned and fixed-timespan perturbations are compared.

**Mathematical/evaluation object:** Attribution is an intervention-dependent measurement; agreement and error-based scores test whether highlighted regions are reliable under controlled perturbations.

**Reported evidence:** Standard approaches are generally unreliable in speech, except that word-aligned perturbations are more reliable for word-based classification tasks.

**Limit:** The models, tasks, datasets, attribution methods, and reliability definitions bound the result; no explanation method becomes a causal proof from these tests alone.

#### Beyond Similarity Scoring: Detecting Entailment and Contradiction in Multilingual and Multimodal Contexts

**Why this belongs:** The official archive evidence identifies a human spoken-speech object and a bounded problem that instantiate word-error-versus-understanding under metrics-and-targets; this resolves membership only.

**Mechanism:** Speech-text, text-speech, and speech-speech pairs are added to a multilingual inference framework and compared with similarity-based BLASER evaluation.

**Mathematical/evaluation object:** The target is a three-way relation, not a continuous closeness score; F1 measures whether the evaluator detects meaning-preserving and meaning-changing pairs.

**Reported evidence:** The paper reports F1 gains of 0.19 for speech-speech and 0.13 for speech-text over BLASER in distinguishing entailment from non-entailment.

**Limit:** Languages, pair construction, translations, labels, and evaluation sets bound the result; logical classification does not guarantee complete translation assessment or human usefulness.

#### LRBA: Stealthy Backdoor Attacks on Speech Classification via Latent Rearrangement in VITS

**Why this belongs:** The official full paper identifies a human spoken-speech object and a bounded research problem that instantiate spoofing-and-deepfake under privacy-security-and-accountability; this resolves taxonomy membership, not the paper's scientific validity.

**Mechanism:** LRBA uses the normalizing flow in VITS to create rearranged utterances and poisons a small fraction of training data for speech classification.

**Mathematical/evaluation object:** The attack separates perceptual quality from decision integrity; attack success rate, poisoning rate, and mean-opinion score test the tradeoff.

**Reported evidence:** The paper reports high attack success at a low poisoning rate while retaining high perceived quality and outperforming prior attacks in stealthiness.

**Limit:** The VITS model, classifier, target labels, poisoning setup, and listener measure bound the threat; this is an attack demonstration, not evidence that every speech system is vulnerable.

#### Unfolding A Few Structures for The Many: Memory-Efficient Compression of Conformer and Speech Foundation Models

**Why this belongs:** The official full paper identifies a human spoken-speech object and a bounded research problem that instantiate latency-and-resource under robustness-and-system-boundary; this resolves taxonomy membership, not the paper's scientific validity.

**Mechanism:** Logical depth changes through repeated blocks sharing a seed; distillation aligns small and large outputs across paths.

**Mathematical/evaluation object:** Unfolding trades parameter storage for repeated computation, while KL divergence keeps paths behaviorally close.

**Reported evidence:** The models report comparable ASR with 35% Conformer and 30% wav2vec2/HuBERT parameter reductions.

**Limit:** Hardware latency, unfolding cost, family, task, and benchmark coverage bound transfer; fewer parameters is not automatically less energy.

#### SpecTokenizer: A Lightweight Streaming Codec in the Compressed Spectrum Domain

**Why this belongs:** The official full paper identifies a human spoken-speech object and a bounded research problem that instantiate latency-and-resource under robustness-and-system-boundary; this resolves taxonomy membership, not the paper's scientific validity.

**Mechanism:** SpecTokenizer is a streaming single-codebook codec evaluated at 4 kbps against a lightweight codec under matched computation and storage budgets.

**Mathematical/evaluation object:** The codec trades waveform detail for discrete codes; bitrate, reconstruction quality, computation, and parameter count expose the deployment boundary.

**Reported evidence:** At 4 kbps it reports comparable or better performance with 20% of the computation and 10% of the parameters of the comparison codec.

**Limit:** Bitrate, audio material, hardware, streaming definition, and quality measure bound the claim; benchmark efficiency does not prove end-to-end device power or user benefit.

#### WIND: Accelerated RNN-T Decoding with Windowed Inference for Non-blank Detection

**Why this belongs:** The official full paper identifies a human spoken-speech object and a bounded research problem that instantiate latency-and-resource under robustness-and-system-boundary; this resolves taxonomy membership, not the paper's scientific validity.

**Mechanism:** WIND is evaluated on multiple datasets with greedy, batched greedy, and beam-search RNN-T decoding against sequential baselines.

**Mathematical/evaluation object:** The method exploits sparsity in the label stream; speedup is meaningful only when WER remains unchanged and the decoding mode is specified.

**Reported evidence:** Greedy modes reach up to 2.4x speedup with identical WER, while the proposed beam search is faster and slightly more accurate than alternatives.

**Limit:** RNN-T models, datasets, hardware, window size, and decoding modes bound the result; reported speedup is not portable to every implementation or workload.

#### Effective and Efficient One-pass Compression of Speech Foundation Models Using Sparsity-aware Self-pinching Gates

**Why this belongs:** The official full paper identifies a human spoken-speech object and a bounded research problem that instantiate latency-and-resource under robustness-and-system-boundary; this resolves taxonomy membership, not the paper's scientific validity.

**Mechanism:** Self-pinching gates are trained with wav2vec2.0-base and HuBERT-large and then drive fine-grained neuron pruning on LibriSpeech-100hr.

**Mathematical/evaluation object:** A gate is a learned resource-allocation decision; parameter count, WER, compression ratio, and compression time measure the accuracy-efficiency frontier.

**Reported evidence:** The method removes 65% of wav2vec2.0-base and 60% of HuBERT-large parameters without a statistically significant test-clean WER increase, with 7.05% WER at 4.26x compression.

**Limit:** LibriSpeech, model variants, pruning thresholds, and test-clean evaluation bound the result; no claim follows about noisy conditions, energy, or other languages.

#### Dynamic Acoustic Model Architecture Optimization in Training for ASR

**Why this belongs:** The official full paper identifies a human spoken-speech object and a bounded research problem that instantiate latency-and-resource under robustness-and-system-boundary; this resolves taxonomy membership, not the paper's scientific validity.

**Mechanism:** DMAO is evaluated with CTC on LibriSpeech, TED-LIUM-v2, and Switchboard across architectures and model sizes.

**Mathematical/evaluation object:** The architecture becomes a changing allocation of parameters; relative WER at matched resources tests whether reallocation, rather than extra capacity, creates the gain.

**Reported evidence:** The paper reports up to roughly 6% relative WER improvement across datasets, architectures, and sizes with negligible added training overhead.

**Limit:** Datasets, CTC setup, compute budget, search rules, and final architecture bound the result; a benchmark gain does not establish optimality or universal resource allocation.

#### Spectrotemporal Modulation: Efficient and Interpretable Feature Representation for Classifying Speech, Music, and Environmental Sounds

**Why this belongs:** Spectrotemporal modulation features are evaluated for interpretable classification across speech, music, and environmental sounds, exposing task and domain boundaries.

**Mechanism:** STM features are used for naturalistic speech, music, and environmental sound classification without pretraining.

**Mathematical/evaluation object:** The representation describes joint rates of spectral and temporal change; classification performance and feature interpretability test whether a structured signal account can compete with learned scale.

**Reported evidence:** The STM-based model reaches performance comparable to pretrained audio DNNs across the tested categories while remaining interpretable and efficient.

**Limit:** Tasks, datasets, modulation parameters, baselines, and definition of interpretability bound the claim; comparable accuracy does not prove a match to human auditory cortex.

#### Exploring Linear Variant Transformers and k-NN Memory Inference for Long-Form ASR

**Why this belongs:** Long-form ASR evaluation asks whether memory and efficient inference preserve the words that matter over extended speech, not only short-utterance accuracy.

**Mechanism:** Fastformer, SummaryMixing, BiMamba, and E-Branchformer variants are evaluated on a new LibriHeavy long-form benchmark; KNN-MAN is added to encoder-decoder models.

**Mathematical/evaluation object:** Long-form recognition is a time-scale and memory problem: architecture controls cost while retrieval supplies selected history; WER across duration scales tests the tradeoff.

**Reported evidence:** The paper reports a reduction from 18.8% to 17.5% WER on its LibriSpeech long-form test-clean example with BiMamba and KNN-MAN.

**Limit:** Benchmark construction, duration distribution, memory retrieval, architectures, and WER bound the result; a single long-form corpus does not establish general conversation robustness.

#### NanoCodec: Towards High-Quality Ultra Fast Speech LLM Inference

**Why this belongs:** Ultra-fast speech language model inference makes latency a first-class system constraint, with quality claims meaningful only alongside the compute and timing budget.

**Mechanism:** The codec maps audio to discrete tokens and back; token rate controls autoregressive steps while bitrate and causal context control information and latency.

**Mathematical/evaluation object:** Compression is a rate-distortion-resource tradeoff: fewer symbols reduce computation but constrain what the decoder can reconstruct.

**Reported evidence:** NanoCodec reports high-quality compression at 12.5 FPS and competitive results across bitrate ranges.

**Limit:** Audio domain, codec training data, perceptual metric, hardware, and causality setting bound transfer; codec quality is not end-to-end speech generation quality.

#### A Comprehensive Real-World Assessment of Audio Watermarking Algorithms: Will They Survive Neural Codecs?

**Why this belongs:** The preserved abstract identifies a speech object and bounded intervention that instantiate auditability-and-contestability under privacy-security-and-accountability; this upgrades a provisional candidate to analyst-reviewed taxonomy membership only.

**Mechanism:** The paper provides a comprehensive real-world assessment of audio watermarking algorithms and asks whether they survive neural codecs.

**Mathematical/evaluation object:** Robustness is a chain of transformations: a watermark claim is meaningful only over an explicit threat/process set, with detectability balanced against audible distortion.

**Reported evidence:** The paper reports comparative survival and failure patterns across watermarking methods and neural codecs.

**Limit:** Algorithms, codec versions, payloads, thresholds, and attack suite bound the result; survival in tested codecs is not universal tamper resistance.

#### Can Quantized Audio Language Models Perform Zero-Shot Spoofing Detection?

**Why this belongs:** Zero-shot spoof detection asks whether an audio-language model recognizes fakery without seeing the attack during training.

**Mechanism:** The paper tests quantized audio language models for zero-shot spoofing detection on ASVspoof2019, In-the-Wild, and WaveFake.

**Mathematical/evaluation object:** Deployment compression and task validity are separate questions: a model may retain its behavior after quantization while that behavior is already a biased near-random decision rule.

**Reported evidence:** The paper reports negligible FP16 degradation but severe spoof-prediction bias that undermines practical detection.

**Limit:** Models, datasets, thresholds, quantization methods, and zero-shot prompts bound the claim; tested robustness is not security certification.

#### Rehearsal with Auxiliary-Informed Sampling for Audio Deepfake Detection

**Why this belongs:** Deepfake detection must remain useful when new attacks arrive, so rehearsal should preserve old attack evidence while learning new ones.

**Mechanism:** RAIS uses auxiliary-informed sampling for rehearsal-based continual audio-deepfake detection.

**Mathematical/evaluation object:** The memory is selected for coverage of acoustic factors, not only class labels; retaining varied evidence helps the detector update without collapsing onto the newest attack.

**Reported evidence:** The paper reports improved continual deepfake detection over rehearsal baselines on new attacks.

**Limit:** Attack families, auxiliary-label quality, buffer size, stream order, and detector threshold bound the result; no finite memory guarantees future attack coverage.

#### STOPA: A Dataset of Systematic VariaTion Of DeePfake Audio for Open-Set Source Tracing and Attribution

**Why this belongs:** A systematic deepfake corpus varies how synthetic speech is made, making it possible to separate generator-specific artifacts from general evidence of manipulation.

**Mechanism:** STOPA is a dataset of systematic variation of deepfake audio for open-set source tracing and attribution.

**Mathematical/evaluation object:** The task is a structured forensic inference problem: detection asks whether an item is fake, while tracing asks which generating process explains it under variation.

**Reported evidence:** The paper reports dataset resources and benchmark behavior for open-set deepfake source tracing and attribution.

**Limit:** Generator coverage, perturbations, speakers, labels, and open-set split design bound the result; benchmark attribution is not courtroom-grade provenance.

#### LitMAS: A Lightweight and Generalized Multi-Modal Anti-Spoofing Framework for Biometric Security

**Why this belongs:** Anti-spoofing must combine modalities and remain reliable when an attacker changes the attack type rather than repeat a familiar artifact.

**Mechanism:** LitMAS is a lightweight generalized multimodal anti-spoofing framework for biometric security.

**Mathematical/evaluation object:** Security is a coverage problem: the model must learn signs of manipulation that survive changes in modality and attack source, while the resource budget constrains the detector itself.

**Reported evidence:** The paper reports generalized multimodal anti-spoofing performance with a lightweight framework.

**Limit:** Biometric modalities, attacks, datasets, fusion, thresholds, and compute budget bound the result; benchmark generalization is not security certification.

#### Privacy-Preserving Speaker Verification via End-to-End Secure Representation Learning

**Why this belongs:** Private speaker verification must decide identity without exposing a reusable representation of the speaker's voice.

**Mechanism:** The paper proposes privacy-preserving speaker verification via end-to-end secure representation learning.

**Mathematical/evaluation object:** Privacy is built into the representation rather than added only at storage: the learned object should support the authorized comparison while limiting what an observer can recover.

**Reported evidence:** The paper reports privacy and speaker-verification results for the proposed secure representation learning method.

**Limit:** Threat model, attacker access, datasets, privacy measure, calibration, and deployment protocol bound the claim; benchmark privacy is not a complete security proof.

#### CBA: Backdoor Attack on Deep Speech Classification via Audio Compression

**Why this belongs:** A speech classifier must remain trustworthy when an attacker hides a sample-specific trigger inside compressed audio.

**Mechanism:** CBA studies a backdoor attack on deep speech classification via audio compression.

**Mathematical/evaluation object:** The front-end becomes part of the attack surface: a transformation assumed to be harmless can carry a trigger that changes the classifier's decision.

**Reported evidence:** The paper reports attack success and clean-task behavior for the tested compression-based backdoor.

**Limit:** Model, compression, trigger, target class, defenses, and threat model bound the claim; one attack does not establish universal vulnerability.

#### From Sharpness to Better Generalization for Speech Deepfake Detection

**Why this belongs:** Deepfake detection needs a generalization explanation because unseen domains expose whether the detector learned artifacts or forgery evidence.

**Mechanism:** The paper studies moving from sharpness to better generalization for speech deepfake detection.

**Mathematical/evaluation object:** Generalization depends on the geometry of the learned boundary, not just its training margin; the relevant test is behavior on new attack sources.

**Reported evidence:** The paper reports deepfake-detection generalization results linked to sharpness and the proposed training approach.

**Limit:** Attack types, datasets, sharpness measure, training recipe, and open-set split bound the claim; no benchmark proves future attack coverage.

#### FaiST: A Benchmark Dataset for Fairness in Speech Technology

**Why this belongs:** The preserved abstract identifies a speech object and bounded intervention that instantiate auditability-and-contestability under privacy-security-and-accountability; this upgrades a provisional candidate to analyst-reviewed taxonomy membership only.

**Mechanism:** FaiST is a benchmark dataset for fairness in speech technology.

**Mathematical/evaluation object:** Fairness becomes an evaluation object rather than a vague aspiration: group membership, task outcome, and error disparity must be linked while respecting privacy and sampling limits.

**Reported evidence:** The paper reports benchmark resources and fairness evaluation results for the tested speech technologies.

**Limit:** Group definitions, labels, sample balance, tasks, metrics, and consent bound the conclusions; benchmark parity is not proof of social fairness.

#### Defending Speech-enabled LLMs Against Adversarial Jailbreak Threats

**Why this belongs:** Speech-enabled language systems must be evaluated as an end-to-end interaction because an acoustic request can become a harmful action through later reasoning and tool use.

**Mechanism:** Speech-domain harmful examples change the model; training configurations vary and safety is measured under attacks.

**Mathematical/evaluation object:** Robustness is response behavior under a threat model, not ordinary accuracy.

**Reported evidence:** Four hours of harmful plus 150 hours of benign speech yields reported relative safety gains of 45–300% over baseline.

**Limit:** Attack family, harm taxonomy, model, synthesis, and rubric bound the claim; refusal is not complete security.

#### Benchmarking and Confidence Evaluation of LALMs For Temporal Reasoning

**Why this belongs:** Confidence evaluation tests whether a spoken temporal-reasoning system knows when its answer is uncertain, not only whether its average score is high.

**Mechanism:** The paper introduces Temporal Reasoning Evaluation of Audio and an uncertainty metric for large audio language models.

**Mathematical/evaluation object:** Evaluation must separate getting the answer right from behaving consistently under meaning-preserving changes; these are different properties and can move in opposite directions.

**Reported evidence:** The paper reports that tested open-source models lagged human performance and that accuracy and perturbation-based uncertainty were not necessarily correlated.

**Limit:** The dataset, perturbations, models, human comparison, and temporal tasks bound conclusions; invariance is one operational uncertainty test, not a complete account of confidence.

#### Breaking Resource Barriers in Speech Emotion Recognition via Data Distillation

**Why this belongs:** Data distillation reduces the resources needed for speech emotion recognition, so the question is whether a smaller system retains the intended performance across conditions.

**Mechanism:** The distilled set approximates the information needed by the learner; performance on held-out emotion recognition tests measures retained utility.

**Mathematical/evaluation object:** Data distillation shifts compression from parameters to examples, trading dataset fidelity and privacy exposure against model performance.

**Reported evidence:** The paper reports comparable SER performance between models trained on distilled and original emotional-speech data.

**Limit:** Synthesis method, emotion labels, initialization, privacy threat model, device profile, and test split bound the result; utility parity is not formal privacy.

#### Towards LLM-Empowered Fine-Grained Speech Descriptors for Explainable Emotion Recognition

**Why this belongs:** Fine-grained speech descriptors make an emotion claim inspectable, testing whether explanations correspond to meaningful acoustic evidence.

**Mechanism:** The paper proposes LLM-empowered fine-grained descriptors for explainable speech emotion recognition.

**Mathematical/evaluation object:** Explanation is made an intermediate prediction problem: the system must identify acoustically meaningful factors while retaining enough information for the emotion decision.

**Reported evidence:** On IEMOCAP and MELD, the paper reports up to 4.0 and 3.7 absolute UAR gains over the relevant baselines and presents descriptors as explanations.

**Limit:** Datasets, descriptor definitions, LLM/SSL choices, bottleneck size, and benchmark labels bound the interpretation; a predicted descriptor is not automatically a human-valid cause.

#### Multi-Channel Sequence-to-Sequence Neural Diarization: Experimental Results for The MISP 2025 Challenge

**Why this belongs:** Multi-channel diarization evaluation must reveal coupled failures in segmentation, speaker identity, and overlap rather than one isolated score.

**Mechanism:** The paper presents a multi-channel sequence-to-sequence neural diarization system.

**Mathematical/evaluation object:** Who-spoke-when is structured segmentation: the first pass proposes a timeline, while additional channels provide evidence for revising boundaries and speaker assignments.

**Reported evidence:** The system reports 8.09% diarization error rate on the challenge evaluation set and first place in the MISP 2025 diarization task.

**Limit:** Challenge data, channel layout, scoring convention, enrollment assumptions, and test conditions bound generalization; rank and DER do not guarantee usable transcripts in every meeting.

#### Temp4Cap: Temporally-aligned Automated Audio Captioning

**Why this belongs:** Temporally aligned audio captioning needs evaluation of whether captions identify the right events at the right time, not only fluent text.

**Mechanism:** Temp4Cap is a temporally aligned automated audio-captioning framework.

**Mathematical/evaluation object:** Meaning includes relations among events: the system must learn that ‘before,’ overlap, and after are structural constraints, not decorative words added after recognition.

**Reported evidence:** On Clotho and AudioCaps, the paper reports gains in captioning metrics and temporal metrics over the compared systems.

**Limit:** Datasets, generated temporal captions, negative-sampling design, caption metrics, and temporal scoring bound the claim; metric gains do not ensure every relation is correctly grounded.

#### Non-intrusive Speech Quality Assessment with Diffusion Models Trained on Clean Speech

**Why this belongs:** Non-intrusive quality assessment predicts degradation from the received signal alone, so the central question is whether a quality judgment can be made without the clean reference.

**Mechanism:** The paper uses diffusion-model density estimation for non-intrusive speech-quality assessment.

**Mathematical/evaluation object:** Quality is framed as compatibility with a learned distribution of clean speech: the score is a prior-based anomaly measure, not a direct measurement of every perceptual defect.

**Reported evidence:** The proposed log-likelihood correlates with intrusive metrics and showed the strongest correlation with human scores in the reported listening experiment.

**Limit:** Clean-speech corpus, diffusion schedule, likelihood proxy, reference metrics, listeners, and distortion types bound the claim; low likelihood can mean unfamiliarity rather than poor quality.

#### ``Alexa, can you forget me?'' Machine Unlearning Benchmark in Spoken Language Understanding

**Why this belongs:** A spoken-language system should forget a requested capability or data trace without damaging unrelated language understanding.

**Mechanism:** The benchmark treats unlearning as producing a model close to the retain-only gold model. Metrics include test and forget-set F1, membership-inference attack behavior, generalization, and speedup, making the trade-off explicit.

**Mathematical/evaluation object:** Consent becomes a measurable model-state constraint rather than a checkbox: a deletion request is successful only if identity-linked influence is reduced without unacceptable loss of spoken intent recognition.

**Reported evidence:** The paper benchmarks four datasets in four languages, two speech encoders per dataset, and eight unlearning methods; it shows that no single method dominates all efficacy, utility, and efficiency axes.

**Limit:** Benchmark identities and intent tasks are proxies for real consent, attack strength and gold-model assumptions matter, and unlearning guarantees do not establish that every downstream copy or generated artifact is withdrawn.

#### Towards Machine Unlearning for Paralinguistic Speech Processing

**Why this belongs:** The preserved abstract identifies a speech object and bounded intervention that instantiate voice-privacy under privacy-security-and-accountability; this upgrades a provisional candidate to analyst-reviewed taxonomy membership only.

**Mechanism:** SISA++ turns a global deletion into local retraining plus parameter aggregation. The evaluation separates forgetting performance from retained task performance and measures computational savings.

**Mathematical/evaluation object:** The mechanism uses data partitioning as a control boundary: the model remembers where influence entered, so a request can remove a bounded subset of training history.

**Reported evidence:** Experiments use CREMA-D speech emotion recognition and E-DAIC depression detection; the paper reports TRILLsson features with a Transformer as a robust recipe under its tested settings.

**Limit:** The result depends on shard design, feature extractor, downstream task, attack/evaluation protocol, and access to the original training pipeline; fast unlearning is not proof of legal or social consent compliance.

#### Improving Generalization of End-to-End ASR through Diversity and Independence Regularization

**Why this belongs:** The preserved abstract identifies a speech object and bounded intervention that instantiate distribution-shift under robustness-and-system-boundary; this upgrades a provisional candidate to analyst-reviewed taxonomy membership only.

**Mechanism:** The losses operate on learned feature vectors: one discourages collapse toward similar patterns, the other discourages redundant correlated dimensions.

**Mathematical/evaluation object:** The method shapes representation geometry so multiple informative directions survive while redundant variation is suppressed.

**Reported evidence:** The paper reports improved generalization and robustness for CTC, AED, and RNN-T models in the evaluated tasks.

**Limit:** Training/test shifts, loss weights, architectures, languages, and robustness protocol bound transfer; benchmark generalization is not immunity to arbitrary distribution shift.

#### Voice Quality Dimensions as Interpretable Primitives for Speaking Style for Atypical Speech and Affect

**Why this belongs:** Interpretable voice-quality dimensions can describe speaking style across atypical speech and affect without hiding the explanation in one label.

**Mechanism:** The frozen representation supplies a common acoustic space while lightweight probes map it to interpretable dimensions; held-out speakers and out-of-domain datasets test transfer.

**Mathematical/evaluation object:** Factorizing a human judgment into named dimensions makes the target inspectable, but each probe still inherits annotation and distribution assumptions.

**Reported evidence:** The paper reports strong probe performance and generalization on SAP categories, with zero-shot tests on additional languages, tasks, and affect data.

**Limit:** Proxy labels, speaker/sample overlap, limited out-of-domain sets, frozen-encoder choice, and correlation metrics bound transfer; dimensional prediction is not a clinical or listener-outcome validation.

#### Calm-Whisper: Reduce Whisper Hallucination On Non-Speech By Calming Crazy Heads Down

**Why this belongs:** The preserved abstract identifies a speech object and bounded intervention that instantiate end-to-end-recovery under robustness-and-system-boundary; this upgrades a provisional candidate to analyst-reviewed taxonomy membership only.

**Mechanism:** Ablation assigns causal responsibility at the head level; targeted fine-tuning changes the decoder’s response to acoustic absence while monitoring speech WER.

**Mathematical/evaluation object:** The method creates an evidence boundary inside generation: silence should not be converted into a high-probability language continuation.

**Reported evidence:** The paper reports that three of twenty decoder heads account for most hallucinations on UrbanSound and that targeted training reduces them with limited LibriSpeech WER degradation.

**Limit:** Non-speech corpus, head attribution, fine-tuning regime, language/model version, and WER tradeoff bound transfer; reduced hallucination is not perfect abstention or factual reliability.

#### Simultaneous Masked and Unmasked Decoding with Speculative Decoding Masking for Fast ASR without Accuracy Loss

**Why this belongs:** The preserved abstract identifies a speech object and bounded intervention that instantiate latency-and-resource under robustness-and-system-boundary; this upgrades a provisional candidate to analyst-reviewed taxonomy membership only.

**Mechanism:** Preliminary masked decisions identify positions whose score computation can be omitted; the remaining positions retain the autoregressive search path and its result.

**Mathematical/evaluation object:** The method exploits conditional redundancy in sequence search: computation is spent where uncertainty remains rather than uniformly at every token.

**Reported evidence:** On TED-LIUM2, the paper reports WER 7.3% for both the proposed and autoregressive systems, with RTF 0.41 versus 0.59.

**Limit:** One corpus/model, beam and hardware settings, confidence thresholds, and real-time measurement protocol bound transfer; equal WER on one test set does not prove universal speed preservation.

#### GTA: Towards Generative Text-To-Audio Retrieval via Multi-Scale Tokenizer

**Why this belongs:** The captured official PDF and abstract identify a speech object and mechanism instantiating latency-and-resource under robustness-and-system-boundary; this upgrades evidence depth for the structured note and does not establish independent reproduction.

**Mechanism:** Coarse and fine audio tokens represent different temporal resolutions for retrieval.

**Mathematical/evaluation object:** The relevant object is the latency-and-resource evidence described by the paper's mechanism: Coarse and fine audio tokens represent different temporal resolutions for retrieval.

**Reported evidence:** The paper reports GTA results for generative text-to-audio retrieval.

**Limit:** Audio, prompts, token rates, metrics, hardware, and generation budget bound transfer.

### Synthesis boundary

These papers share a conceptual pressure, but this seed batch does not justify ranking methods, estimating prevalence, or claiming that the mechanism generalizes across speakers, languages, rooms, or tasks. Those claims require additional assignments and comparable denominators.

