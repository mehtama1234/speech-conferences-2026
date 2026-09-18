# Speech first-principles conceptual taxonomy

Themes and variable subthemes are derived from the baseline first-principles account and explicit paper-family boundary tests; this is not an official conference classification or prevalence estimate.

This organically derived proposal has 8 themes, 34 variable subthemes, and 72 concepts. Counts are not equalized.

## Sound, bodies, rooms, and recording

**Ordinary problem:** Speech reaches a microphone as changing air pressure after vocal-fold vibration, mouth shape, room reflections, and electronics have already mixed together.

**Why the naive approach fails:** Treating the waveform as an unstructured list of samples hides which changes came from the talker, the room, or the recording device.

**Recurring conceptual move:** Separate source, filter, geometry, and time scale so a measured signal can be related back to a physical cause.

**Tradeoff/boundary:** A useful physical description can be wrong when bodies, rooms, or microphones violate its assumptions.

### Making a physical sound

**Question:** What ordinary speech pressure is handled by making a physical sound, and what evidence distinguishes it from neighboring pressures?
**Why this boundary exists:** The source and tract shape the pressure wave before a device records it.
**Derivation rule:** Split or retained because the ordinary pressure, failure mode, mechanism, or evaluation target differs from neighboring groups.

#### Periodic vocal-fold source

A speaker can repeatedly open and close the vocal folds; the repetition supplies pitch and harmonic energy while its exact timing varies.

**Positive membership example:** A study measures vocal-fold pulse timing or harmonic structure in voiced vowels.

**Negative/boundary example:** A study models only a microphone's frequency response with no source or phonation question.

**Boundary:** Not every speech segment is periodic: frication, stops, breath, and irregular phonation cannot be reduced to one stable pitch.

**Evidence rule:** D2 abstract evidence must name the spoken-speech object and conceptual pressure; D3 full-paper evidence must additionally support the mechanism and evaluation object.

#### Vocal-tract filtering

The tongue, lips, jaw, and throat reshape source energy so some frequency regions are strengthened and others weakened; those regions carry much of vowel identity.

**Positive membership example:** A study links tongue or lip geometry to vowel resonances or spectral peaks.

**Negative/boundary example:** A study predicts words from text without modeling how the tract shapes sound.

**Boundary:** A filter-only explanation misses changes caused directly by source irregularity, radiation, or recording conditions.

**Evidence rule:** D2 abstract evidence must name the spoken-speech object and conceptual pressure; D3 full-paper evidence must additionally support the mechanism and evaluation object.

### Coordinating moving speech parts

**Question:** What ordinary speech pressure is handled by coordinating moving speech parts, and what evidence distinguishes it from neighboring pressures?
**Why this boundary exists:** Gesture overlap and timing are the object; a static source/filter description is not enough.
**Derivation rule:** Split or retained because the ordinary pressure, failure mode, mechanism, or evaluation target differs from neighboring groups.

#### Articulatory coordination

Speech is a timed coordination of several moving constrictions, not a sequence of isolated sounds; overlap lets one gesture affect its neighbors.

**Positive membership example:** A study measures overlapping lip, tongue, jaw, or laryngeal gestures over time.

**Negative/boundary example:** A study treats each phoneme as an isolated label with no timing or movement evidence.

**Boundary:** A label such as a phoneme is not itself a physical movement or a complete account of coarticulation.

**Evidence rule:** D2 abstract evidence must name the spoken-speech object and conceptual pressure; D3 full-paper evidence must additionally support the mechanism and evaluation object.

### Representing a changing signal

**Question:** What ordinary speech pressure is handled by representing a changing signal, and what evidence distinguishes it from neighboring pressures?
**Why this boundary exists:** The question is what a digital representation keeps or loses across time, frequency, and precision.
**Derivation rule:** Split or retained because the ordinary pressure, failure mode, mechanism, or evaluation target differs from neighboring groups.

#### Local frequency content

Short windows expose which frequencies are present near each moment, making pitch, resonances, and noise easier to compare than raw samples alone.

**Positive membership example:** A spectrogram or short-time Fourier representation tracks local frequency content.

**Negative/boundary example:** A long-term average spectrum with no time-local measurement is not a windowed account.

**Boundary:** A window discards some exact timing and long-range phase; two signals with similar spectra may still sound different.

**Evidence rule:** D2 abstract evidence must name the spoken-speech object and conceptual pressure; D3 full-paper evidence must additionally support the mechanism and evaluation object.

#### Multiple time scales

Fast events such as consonant closures and slow changes such as intonation require measurements at different temporal resolutions.

**Positive membership example:** A method combines short windows for closures with longer windows for intonation or rhythm.

**Negative/boundary example:** Adding multiple neural layers without showing distinct time scales is not itself multi-resolution analysis.

**Boundary:** Adding resolutions is not automatically informative; it can increase computation or preserve nuisance variation.

**Evidence rule:** D2 abstract evidence must name the spoken-speech object and conceptual pressure; D3 full-paper evidence must additionally support the mechanism and evaluation object.

#### Sampling and quantization

A digital recording keeps a finite set of amplitude measurements, so the sampling rate and numeric precision set what can still be recovered.

**Positive membership example:** A study analyzes sample rate, bit depth, clipping, or quantization noise as information limits.

**Negative/boundary example:** A model that merely uses digital audio but never examines discretization does not instantiate this concept.

**Boundary:** A high sample rate cannot restore information lost through clipping, poor microphones, or an absent frequency range.

**Evidence rule:** D2 abstract evidence must name the spoken-speech object and conceptual pressure; D3 full-paper evidence must additionally support the mechanism and evaluation object.

### Changing the path from source to sensor

**Question:** What ordinary speech pressure is handled by changing the path from source to sensor, and what evidence distinguishes it from neighboring pressures?
**Why this boundary exists:** Room reflections, device coloration, and alternate sensors change the evidence before recognition.
**Derivation rule:** Split or retained because the ordinary pressure, failure mode, mechanism, or evaluation target differs from neighboring groups.

#### Reverberant room mixture

The microphone hears direct sound plus delayed reflections, so a word can overlap its own earlier energy and blur boundaries.

**Positive membership example:** A method separates direct speech from delayed room reflections or models room impulse responses.

**Negative/boundary example:** Stationary additive microphone hiss with no room-delay structure is not reverberant mixing.

**Boundary:** Reverberation is not just additive stationary noise; its delay pattern depends on room geometry and position.

**Evidence rule:** D2 abstract evidence must name the spoken-speech object and conceptual pressure; D3 full-paper evidence must additionally support the mechanism and evaluation object.

#### Microphone and channel coloration

A device emphasizes some frequencies, clips loud peaks, or transmits only a narrow band, changing the evidence available to a recognizer.

**Positive membership example:** A system corrects frequency coloration, clipping, bandwidth, or device-specific transmission effects.

**Negative/boundary example:** A speaker adaptation method that never observes a recording channel is not channel modeling.

**Boundary:** Channel normalization can remove useful speaker or environment information along with nuisance coloration.

**Evidence rule:** D2 abstract evidence must name the spoken-speech object and conceptual pressure; D3 full-paper evidence must additionally support the mechanism and evaluation object.

#### Non-airborne speech sensing

Neck vibration, ultrasound, radar, or muscle signals can observe speech when airborne audio is missing, but they observe a different projection of the act.

**Positive membership example:** Speech is inferred from neck vibration, ultrasound, radar, or another non-airborne sensor.

**Negative/boundary example:** Ordinary far-field microphone speech, even if noisy, is not non-airborne sensing.

**Boundary:** A sensor that works in quiet laboratory placement is not automatically a replacement for ordinary audio in daily use.

**Evidence rule:** D2 abstract evidence must name the spoken-speech object and conceptual pressure; D3 full-paper evidence must additionally support the mechanism and evaluation object.

## Listening through noise, overlap, and missing sound

**Ordinary problem:** A listener often hears several talkers, music, echo, and device noise at once, yet needs one person's words or an intelligible mixture.

**Why the naive approach fails:** Amplifying everything or subtracting an average noise profile also removes quiet consonants and fails when the interferer changes with the speech.

**Recurring conceptual move:** Use structure that differs between target and interference—time, frequency, space, source identity, or learned speech regularity—to estimate and reconstruct the target.

**Tradeoff/boundary:** A cleaner waveform may be less faithful, introduce artifacts, or favor the wrong speaker when the mixture is ambiguous.

### Suppressing changing interference

**Question:** What ordinary speech pressure is handled by suppressing changing interference, and what evidence distinguishes it from neighboring pressures?
**Why this boundary exists:** The target is one speech stream and the failure is removing speech along with noise.
**Derivation rule:** Split or retained because the ordinary pressure, failure mode, mechanism, or evaluation target differs from neighboring groups.

#### Time-frequency masking

Estimate how much each local frequency region belongs to speech, then attenuate regions dominated by noise.

**Positive membership example:** A system estimates a time-frequency mask and attenuates bins assigned to noise.

**Negative/boundary example:** A waveform denoiser with no time-frequency assignment is not necessarily masking.

**Boundary:** A binary or soft mask can create musical noise and cannot reliably separate sources that occupy the same region.

**Evidence rule:** D2 abstract evidence must name the spoken-speech object and conceptual pressure; D3 full-paper evidence must additionally support the mechanism and evaluation object.

#### Speech-prior denoising

A model learned from clean speech can fill in a plausible speech pattern where the recording is noisy, trading exact fidelity for intelligibility.

**Positive membership example:** A learned clean-speech prior reconstructs plausible speech where noise obscures the waveform.

**Negative/boundary example:** A fixed notch filter that uses no speech structure is not a speech prior.

**Boundary:** A plausible completion can hallucinate phonetic detail the microphone never captured.

**Evidence rule:** D2 abstract evidence must name the spoken-speech object and conceptual pressure; D3 full-paper evidence must additionally support the mechanism and evaluation object.

#### Changing and adverse noise

The useful distinction is whether noise changes faster than the system can track, as with competing speech, vehicles, or sudden events.

**Positive membership example:** The interference changes rapidly or contains competing speech, feedback, or transient events.

**Negative/boundary example:** A single fixed broadband noise condition does not establish nonstationary-noise handling.

**Boundary:** A result on fixed background noise does not establish performance under changing or speech-like interference.

**Evidence rule:** D2 abstract evidence must name the spoken-speech object and conceptual pressure; D3 full-paper evidence must additionally support the mechanism and evaluation object.

### Recovering several hidden sources

**Question:** What ordinary speech pressure is handled by recovering several hidden sources, and what evidence distinguishes it from neighboring pressures?
**Why this boundary exists:** The mixture contains multiple sources and the system must infer source identity or count.
**Derivation rule:** Split or retained because the ordinary pressure, failure mode, mechanism, or evaluation target differs from neighboring groups.

#### Blind source separation

Infer several hidden signals from their mixture using differences in statistics, timing, or spectral structure without receiving isolated sources at test time.

**Positive membership example:** Several hidden signals are inferred from their mixture without isolated target audio at test time.

**Negative/boundary example:** A target voice embedding supplied at test time makes the task target-conditioned rather than blind.

**Boundary:** The mixture may not contain enough information to identify sources uniquely; permutation and source-count assumptions matter.

**Evidence rule:** D2 abstract evidence must name the spoken-speech object and conceptual pressure; D3 full-paper evidence must additionally support the mechanism and evaluation object.

#### Target-conditioned separation

A voice example, enrollment identity, or visual cue tells the separator which source to preserve rather than asking it to output every source.

**Positive membership example:** An enrollment voice, visual cue, or target example selects which speaker to retain.

**Negative/boundary example:** Separating every source without a target condition is not target-conditioned separation.

**Boundary:** Conditioning can lock onto the wrong talker or encode identity without guaranteeing intelligible content.

**Evidence rule:** D2 abstract evidence must name the spoken-speech object and conceptual pressure; D3 full-paper evidence must additionally support the mechanism and evaluation object.

### Using location to select sound

**Question:** What ordinary speech pressure is handled by using location to select sound, and what evidence distinguishes it from neighboring pressures?
**Why this boundary exists:** Microphone geometry and direction are the evidence; a single-channel separator has a different limit.
**Derivation rule:** Split or retained because the ordinary pressure, failure mode, mechanism, or evaluation target differs from neighboring groups.

#### Spatial filtering

Several microphones provide direction-dependent differences, allowing a filter to reinforce one location and reject others.

**Positive membership example:** Microphone-array direction or spatial covariance is used to reinforce one location.

**Negative/boundary example:** A single-channel spectral model with no spatial input is not spatial filtering.

**Boundary:** A single microphone or moving speaker removes the spatial cue the method depends on.

**Evidence rule:** D2 abstract evidence must name the spoken-speech object and conceptual pressure; D3 full-paper evidence must additionally support the mechanism and evaluation object.

### Canceling copies and filling gaps

**Question:** What ordinary speech pressure is handled by canceling copies and filling gaps, and what evidence distinguishes it from neighboring pressures?
**Why this boundary exists:** The unwanted signal is a known delayed copy or missing frame, not an arbitrary background.
**Derivation rule:** Split or retained because the ordinary pressure, failure mode, mechanism, or evaluation target differs from neighboring groups.

#### Acoustic echo cancellation

Use the known far-end playback signal to predict the speaker signal that returns through the room, then subtract that predicted copy.

**Positive membership example:** Known loudspeaker playback is used to estimate and subtract its reflected copy from microphone input.

**Negative/boundary example:** Removing unrelated background noise without a playback reference is not echo cancellation.

**Boundary:** The loudspeaker path changes with movement and delay; an imperfect estimate can cancel near-end speech.

**Evidence rule:** D2 abstract evidence must name the spoken-speech object and conceptual pressure; D3 full-paper evidence must additionally support the mechanism and evaluation object.

#### Packet-loss concealment

When transmitted audio frames disappear, infer a short continuation from nearby waveform or speech structure so playback does not break.

**Positive membership example:** Missing transmitted frames are filled using neighboring waveform or speech continuity.

**Negative/boundary example:** Denoising a complete recording is not packet-loss concealment.

**Boundary:** Short plausible continuation is not recovery of the original utterance and becomes unsafe over long gaps.

**Evidence rule:** D2 abstract evidence must name the spoken-speech object and conceptual pressure; D3 full-paper evidence must additionally support the mechanism and evaluation object.

### Optimizing what a listener can use

**Question:** What ordinary speech pressure is handled by optimizing what a listener can use, and what evidence distinguishes it from neighboring pressures?
**Why this boundary exists:** This boundary is for methods whose target is what a listener can understand or tolerate; it is separate from noise removal, separation, and packet repair, which target a signal or source before the listener judges it.
**Derivation rule:** Split or retained because the ordinary pressure, failure mode, mechanism, or evaluation target differs from neighboring groups.

#### Perceptual enhancement

Optimize what a listener can understand or tolerate rather than preserving every sample, using intelligibility or quality as the target.

**Positive membership example:** Enhancement is optimized or judged by intelligibility, listener quality, or perceptual acceptability.

**Negative/boundary example:** A lower sample MSE alone is not perceptual enhancement evidence.

**Boundary:** A perceptual score can hide distortions important for recognition, speaker identity, or forensic use.

**Evidence rule:** D2 abstract evidence must name the spoken-speech object and conceptual pressure; D3 full-paper evidence must additionally support the mechanism and evaluation object.

## From sound to words and structured speech

**Ordinary problem:** Speech has no visible spaces between words, and pronunciation, speed, accent, noise, and hesitation vary even when the intended sentence is the same.

**Why the naive approach fails:** Matching each sound to a fixed dictionary pronunciation or treating the utterance as already segmented fails on coarticulation, new words, and disfluency.

**Recurring conceptual move:** Infer a sequence of linguistic units while allowing uncertainty about boundaries, pronunciation, context, and what should be preserved.

**Tradeoff/boundary:** A fluent transcript can be easier to read but less faithful to what was said, including omissions, hesitation, or uncertainty.

### Learning reusable sound units

**Question:** What ordinary speech pressure is handled by learning reusable sound units, and what evidence distinguishes it from neighboring pressures?
**Why this boundary exists:** The system first decides what reusable evidence can be extracted from continuous sound.
**Derivation rule:** Split or retained because the ordinary pressure, failure mode, mechanism, or evaluation target differs from neighboring groups.

#### Acoustic-to-token mapping

The system scores candidate symbol sequences against the observed sound and chooses or represents alternatives rather than reading words directly from samples.

**Positive membership example:** A continuous acoustic sequence is scored against phones, words, or discrete recognition tokens.

**Negative/boundary example:** Text-only language modeling with no acoustic input is not acoustic-to-token mapping.

**Boundary:** The highest-scoring sequence may exploit dataset regularities instead of matching the actual speech.

**Evidence rule:** D2 abstract evidence must name the spoken-speech object and conceptual pressure; D3 full-paper evidence must additionally support the mechanism and evaluation object.

#### Learned speech units

Predicting or grouping parts of unlabeled audio can provide reusable units before a task-specific word recognizer is trained.

**Positive membership example:** Unlabeled speech predicts masked or neighboring content to create reusable acoustic representations.

**Negative/boundary example:** A supervised classifier trained only on labeled words is not self-supervised unit learning.

**Boundary:** A useful pretraining prediction need not produce units aligned with words, phonemes, or human categories.

**Evidence rule:** D2 abstract evidence must name the spoken-speech object and conceptual pressure; D3 full-paper evidence must additionally support the mechanism and evaluation object.

### Allowing different realizations of words

**Question:** What ordinary speech pressure is handled by allowing different realizations of words, and what evidence distinguishes it from neighboring pressures?
**Why this boundary exists:** The same intended unit has multiple acoustic paths; this is distinct from learning a unit representation.
**Derivation rule:** Split or retained because the ordinary pressure, failure mode, mechanism, or evaluation target differs from neighboring groups.

#### Pronunciation variation

The same word can have reductions, substitutions, or accent-specific realizations, so recognition must allow more than one acoustic path.

**Positive membership example:** Recognition explicitly permits reductions, substitutions, accents, or multiple pronunciations of a word.

**Negative/boundary example:** Adding a new vocabulary item without pronunciation variation is not this concept.

**Boundary:** Adding variants without evidence can increase confusions and may encode an accent as an error.

**Evidence rule:** D2 abstract evidence must name the spoken-speech object and conceptual pressure; D3 full-paper evidence must additionally support the mechanism and evaluation object.

### Locating units in time

**Question:** What ordinary speech pressure is handled by locating units in time, and what evidence distinguishes it from neighboring pressures?
**Why this boundary exists:** The output must preserve or locate timing, hesitation, repair, or sequence boundaries.
**Derivation rule:** Split or retained because the ordinary pressure, failure mode, mechanism, or evaluation target differs from neighboring groups.

#### Temporal alignment

Align an audio timeline with words, phones, or labels so duration and position can be measured rather than treating the utterance as an unordered bag.

**Positive membership example:** Words, phones, or labels are assigned positions and durations on an audio timeline.

**Negative/boundary example:** An utterance-level class with no temporal correspondence is not alignment.

**Boundary:** Forced alignment assumes the transcript is correct and can conceal recognition errors.

**Evidence rule:** D2 abstract evidence must name the spoken-speech object and conceptual pressure; D3 full-paper evidence must additionally support the mechanism and evaluation object.

#### Disfluency and event preservation

Represent pauses, repetitions, repairs, laughter, and overlap when those events are part of the communication or the clinical signal.

**Positive membership example:** Pauses, repetitions, repairs, laughter, or overlap are retained as output events.

**Negative/boundary example:** Cleaning a transcript by deleting all disfluencies is the neighboring failure, not preservation.

**Boundary:** Removing them may improve readability while destroying evidence needed for conversation analysis or diagnosis.

**Evidence rule:** D2 abstract evidence must name the spoken-speech object and conceptual pressure; D3 full-paper evidence must additionally support the mechanism and evaluation object.

### Using context without inventing words

**Question:** What ordinary speech pressure is handled by using context without inventing words, and what evidence distinguishes it from neighboring pressures?
**Why this boundary exists:** Context, speaker evidence, and new words resolve ambiguity but can override what was actually said.
**Derivation rule:** Split or retained because the ordinary pressure, failure mode, mechanism, or evaluation target differs from neighboring groups.

#### Long-context decoding

Use words and turns before and after a sound to resolve locally ambiguous acoustics, such as homophones or clipped endings.

**Positive membership example:** Earlier or later words and turns resolve an acoustically ambiguous local segment.

**Negative/boundary example:** A frame-local classifier that never uses surrounding context is not long-context decoding.

**Boundary:** Context can override a rare but correct word, especially when the language model has a strong prior.

**Evidence rule:** D2 abstract evidence must name the spoken-speech object and conceptual pressure; D3 full-paper evidence must additionally support the mechanism and evaluation object.

#### Domain and context biasing

Use the meeting topic, contact list, or application vocabulary to raise plausible rare words without changing the audio itself.

**Positive membership example:** A meeting topic, contact list, or application vocabulary changes rare-word decoding.

**Negative/boundary example:** A generic language model with no task context is not contextual biasing.

**Boundary:** A biased vocabulary can turn uncertainty into confident but context-shaped substitutions.

**Evidence rule:** D2 abstract evidence must name the spoken-speech object and conceptual pressure; D3 full-paper evidence must additionally support the mechanism and evaluation object.

#### Speaker adaptation

Adjust the acoustic or decoding assumptions to a talker's voice, speaking rate, or pronunciation using a small amount of evidence.

**Positive membership example:** A small enrollment sample changes acoustic or decoding assumptions for a particular talker.

**Negative/boundary example:** A single population-wide model with no speaker evidence is not adaptation.

**Boundary:** Adaptation can overfit a short sample and degrade when the talker changes state or the enrollment is wrong.

**Evidence rule:** D2 abstract evidence must name the spoken-speech object and conceptual pressure; D3 full-paper evidence must additionally support the mechanism and evaluation object.

#### Open-vocabulary recognition

Handle names, code-switching, jargon, and newly encountered words without requiring a fixed closed list.

**Positive membership example:** The recognizer handles names, jargon, code-switching, or newly encountered words outside a fixed list.

**Negative/boundary example:** A closed command grammar with a fixed word list is not open-vocabulary recognition.

**Boundary:** Open vocabulary expands recall but makes spelling, segmentation, and evaluation less settled.

**Evidence rule:** D2 abstract evidence must name the spoken-speech object and conceptual pressure; D3 full-paper evidence must additionally support the mechanism and evaluation object.

## From spoken form to meaning and coordinated action

**Ordinary problem:** The same words can request, question, joke, refuse, or warn depending on prosody, shared history, timing, and the surrounding situation.

**Why the naive approach fails:** A transcript-only system treats words as the whole message and misses intent, reference, turn structure, and what is appropriate to do next.

**Recurring conceptual move:** Combine linguistic content with speaker, discourse history, prosody, visual or environmental context, and an explicit action or response target.

**Tradeoff/boundary:** More context can resolve ambiguity but can also leak private information, over-interpret the speaker, or make a system confidently act on a wrong inference.

### Meaning carried by how speech sounds

**Question:** What ordinary speech pressure is handled by meaning carried by how speech sounds, and what evidence distinguishes it from neighboring pressures?
**Why this boundary exists:** This boundary covers information carried by pitch, timing, loudness, voice quality, or effort beyond the words; it is separate from dialogue action because the cue is in how an utterance sounds, not in the conversational state alone.
**Derivation rule:** Split or retained because the ordinary pressure, failure mode, mechanism, or evaluation target differs from neighboring groups.

#### Prosodic meaning

Pitch movement, timing, stress, and pauses can mark questions, contrast, turn completion, urgency, or attitude.

**Positive membership example:** Pitch, stress, rhythm, or pauses change whether an utterance sounds like a question, contrast, or turn completion.

**Negative/boundary example:** A lexical-only text classifier with no prosodic evidence is not prosodic meaning analysis.

**Boundary:** Prosody is language- and speaker-dependent; a pitch pattern is not a universal emotion label.

**Evidence rule:** D2 abstract evidence must name the spoken-speech object and conceptual pressure; D3 full-paper evidence must additionally support the mechanism and evaluation object.

#### Paralinguistic state

Voice properties can provide clues about emotion, fatigue, engagement, or health that are not the literal linguistic content.

**Positive membership example:** Acoustic voice changes are used as clues about emotion, fatigue, engagement, or health.

**Negative/boundary example:** A diagnosis asserted from a transcript alone is not acoustic paralinguistic-state evidence.

**Boundary:** A correlational acoustic cue is not proof of an internal state or a reliable diagnosis.

**Evidence rule:** D2 abstract evidence must name the spoken-speech object and conceptual pressure; D3 full-paper evidence must additionally support the mechanism and evaluation object.

### Inferring what a speaker is trying to do

**Question:** What ordinary speech pressure is handled by inferring what a speaker is trying to do, and what evidence distinguishes it from neighboring pressures?
**Why this boundary exists:** The system tracks goals, commitments, and situation rather than only classifying acoustic style.
**Derivation rule:** Split or retained because the ordinary pressure, failure mode, mechanism, or evaluation target differs from neighboring groups.

#### Intent in context

Infer what the speaker is trying to accomplish from words plus the situation and prior turns, then keep uncertainty when several intents fit.

**Positive membership example:** Words, prosody, and discourse situation jointly determine whether a speaker requests, warns, jokes, or refuses.

**Negative/boundary example:** Assigning intent from isolated keywords alone is not context-sensitive intent inference.

**Boundary:** Intent labels often reflect annotator interpretation and may erase ambiguity or culturally different readings.

**Evidence rule:** D2 abstract evidence must name the spoken-speech object and conceptual pressure; D3 full-paper evidence must additionally support the mechanism and evaluation object.

#### Dialogue state

Track unresolved questions, commitments, entities, and prior actions so a response is connected to the conversation rather than only the last sentence.

**Positive membership example:** The system tracks unresolved questions, commitments, entities, and prior actions across turns.

**Negative/boundary example:** A response based only on the last utterance is not dialogue-state tracking.

**Boundary:** A stored state can be stale, incorrectly inferred, or sensitive, and the system may not know when to discard it.

**Evidence rule:** D2 abstract evidence must name the spoken-speech object and conceptual pressure; D3 full-paper evidence must additionally support the mechanism and evaluation object.

### Coordinating participation under uncertainty

**Question:** What ordinary speech pressure is handled by coordinating participation under uncertainty, and what evidence distinguishes it from neighboring pressures?
**Why this boundary exists:** The problem is when to speak, yield, interrupt, or ask for clarification.
**Derivation rule:** Split or retained because the ordinary pressure, failure mode, mechanism, or evaluation target differs from neighboring groups.

#### Turn-boundary prediction

Predict whether a speaker is continuing, yielding, or likely to stop so a system can respond without cutting them off.

**Positive membership example:** The system predicts whether a speaker will continue, yield, or stop before responding.

**Negative/boundary example:** Detecting sentence punctuation after the turn is complete is not turn-boundary prediction.

**Boundary:** A pause is not always a turn end; cultures, speakers, and task types change timing conventions.

**Evidence rule:** D2 abstract evidence must name the spoken-speech object and conceptual pressure; D3 full-paper evidence must additionally support the mechanism and evaluation object.

#### Repair and clarification

When recognition or understanding is uncertain, ask a targeted question or offer alternatives instead of silently continuing.

**Positive membership example:** Uncertainty triggers a targeted question, confirmation, or alternative instead of silent continuation.

**Negative/boundary example:** Returning a confident guess without a correction path is not repair.

**Boundary:** A clarification costs time and can burden users if uncertainty estimates are poorly calibrated.

**Evidence rule:** D2 abstract evidence must name the spoken-speech object and conceptual pressure; D3 full-paper evidence must additionally support the mechanism and evaluation object.

### Connecting language to a shared world

**Question:** What ordinary speech pressure is handled by connecting language to a shared world, and what evidence distinguishes it from neighboring pressures?
**Why this boundary exists:** A phrase must identify a referent or authorized action and remain corrigible through feedback.
**Derivation rule:** Split or retained because the ordinary pressure, failure mode, mechanism, or evaluation target differs from neighboring groups.

#### Referential grounding

Use the scene, shared task, or prior mention to determine which object, person, or event a phrase denotes.

**Positive membership example:** A phrase such as 'that cup' is linked to an object in the shared scene or prior discourse.

**Negative/boundary example:** Choosing a likely object without scene or discourse evidence is not grounding.

**Boundary:** Words alone may underdetermine the referent; a model can infer a plausible object without actually observing it.

**Evidence rule:** D2 abstract evidence must name the spoken-speech object and conceptual pressure; D3 full-paper evidence must additionally support the mechanism and evaluation object.

#### Speech act

Distinguish information from a request, command, permission, or commitment because the same proposition can require different responses.

**Positive membership example:** The system distinguishes an assertion from a request, command, permission, or commitment.

**Negative/boundary example:** Topic classification without an action or authority interpretation is not speech-act analysis.

**Boundary:** Classifying an act does not grant authority to execute it.

**Evidence rule:** D2 abstract evidence must name the spoken-speech object and conceptual pressure; D3 full-paper evidence must additionally support the mechanism and evaluation object.

#### Interactional feedback

Let user corrections, confirmations, and response outcomes update the system's interpretation during the interaction.

**Positive membership example:** User correction or response outcome updates what the system believes the user meant.

**Negative/boundary example:** Logging a prediction without using subsequent interaction is not feedback.

**Boundary:** Feedback can be sparse, ambiguous, or shaped by users adapting to the system's mistakes.

**Evidence rule:** D2 abstract evidence must name the spoken-speech object and conceptual pressure; D3 full-paper evidence must additionally support the mechanism and evaluation object.

## Creating speech while keeping the right things fixed

**Ordinary problem:** A useful synthetic voice must say the requested content, sound like the intended speaker or style, and remain understandable as it changes over time.

**Why the naive approach fails:** Copying a recording or predicting samples directly entangles words with identity, pitch, rhythm, and recording conditions, making controlled change difficult.

**Recurring conceptual move:** Represent or condition distinct factors, generate a time-consistent waveform or acoustic sequence, and evaluate each requested property separately.

**Tradeoff/boundary:** Factor separation is rarely perfect: changing identity can change content, style controls can sound artificial, and a plausible voice can be misused.

### Turning language into a timed speech plan

**Question:** What ordinary speech pressure is handled by turning language into a timed speech plan, and what evidence distinguishes it from neighboring pressures?
**Why this boundary exists:** This boundary covers the step from intended text or meaning to pronunciation, duration, pitch targets, and sequence; it is separate from waveform generation, which realizes an already chosen plan as samples.
**Derivation rule:** Split or retained because the ordinary pressure, failure mode, mechanism, or evaluation target differs from neighboring groups.

#### Text-to-speech planning

Choose pronunciation, durations, pitch targets, and acoustic details before or while producing the waveform so written content becomes speakable.

**Positive membership example:** Text is converted into pronunciation, duration, pitch, and acoustic plans before waveform generation.

**Negative/boundary example:** A waveform vocoder receiving a complete acoustic plan is not itself text-to-speech planning.

**Boundary:** Text does not specify one correct prosody, and a fluent output can still mispronounce names or sound unnatural.

**Evidence rule:** D2 abstract evidence must name the spoken-speech object and conceptual pressure; D3 full-paper evidence must additionally support the mechanism and evaluation object.

### Producing or compressing audible detail

**Question:** What ordinary speech pressure is handled by producing or compressing audible detail, and what evidence distinguishes it from neighboring pressures?
**Why this boundary exists:** The issue is sample-level detail and the tradeoff between faithful content and natural sound.
**Derivation rule:** Split or retained because the ordinary pressure, failure mode, mechanism, or evaluation target differs from neighboring groups.

#### Waveform synthesis

Generate fine-grained samples conditioned on a coarser acoustic plan, reconstructing the periodic and noisy detail listeners hear as voice.

**Positive membership example:** A model generates fine waveform samples conditioned on a lower-rate acoustic representation.

**Negative/boundary example:** A text-to-text model with no waveform synthesis is not a neural vocoder.

**Boundary:** Sample-level realism does not guarantee correct words, stable identity, or natural long-range timing.

**Evidence rule:** D2 abstract evidence must name the spoken-speech object and conceptual pressure; D3 full-paper evidence must additionally support the mechanism and evaluation object.

#### Intelligibility versus naturalness

Treat ease of understanding and human-likeness as related but distinct targets that need separate tests.

**Positive membership example:** Separate tests ask whether words are understood and whether the voice sounds human-like.

**Negative/boundary example:** One unqualified quality score cannot establish both intelligibility and naturalness.

**Boundary:** A single listener score can conflate content accuracy, recording quality, and preference.

**Evidence rule:** D2 abstract evidence must name the spoken-speech object and conceptual pressure; D3 full-paper evidence must additionally support the mechanism and evaluation object.

### Changing who sounds like the speaker

**Question:** What ordinary speech pressure is handled by changing who sounds like the speaker, and what evidence distinguishes it from neighboring pressures?
**Why this boundary exists:** This boundary covers changing or measuring who the voice sounds like while keeping the message stable; it is separate from expression control, which changes emotion or style, and from content planning, which changes the speech plan.
**Derivation rule:** Split or retained because the ordinary pressure, failure mode, mechanism, or evaluation target differs from neighboring groups.

#### Speaker identity representation

Capture stable voice traits that let a system preserve or imitate who is speaking across different words and sessions.

**Positive membership example:** A representation preserves or imitates a person's stable vocal characteristics across words.

**Negative/boundary example:** A recording-specific noise signature mistaken for identity is not a valid identity representation.

**Boundary:** A short recording can encode noise, emotion, or demographic stereotypes rather than stable identity.

**Evidence rule:** D2 abstract evidence must name the spoken-speech object and conceptual pressure; D3 full-paper evidence must additionally support the mechanism and evaluation object.

#### Voice conversion

Transform the acoustic realization toward a target voice while trying to preserve linguistic timing and content.

**Positive membership example:** The acoustic realization moves toward a target speaker while the source linguistic content remains.

**Negative/boundary example:** Changing text content without preserving the source message is not voice conversion.

**Boundary:** Conversion may leak source identity, distort pronunciation, or require target-speaker data unavailable in practice.

**Evidence rule:** D2 abstract evidence must name the spoken-speech object and conceptual pressure; D3 full-paper evidence must additionally support the mechanism and evaluation object.

#### Unseen-speaker synthesis

Use a voice description or brief enrollment to synthesize a speaker not represented by a dedicated model.

**Positive membership example:** A brief enrollment or description synthesizes a speaker without a dedicated per-speaker model.

**Negative/boundary example:** A model trained and tested only on speakers seen during training is not zero-shot voice.

**Boundary:** Similarity on a benchmark does not establish consent, identity security, or robustness to unusual voices.

**Evidence rule:** D2 abstract evidence must name the spoken-speech object and conceptual pressure; D3 full-paper evidence must additionally support the mechanism and evaluation object.

### Changing style, timing, and response behavior

**Question:** What ordinary speech pressure is handled by changing style, timing, and response behavior, and what evidence distinguishes it from neighboring pressures?
**Why this boundary exists:** The system must obey expressive controls quickly without breaking continuity or meaning.
**Derivation rule:** Split or retained because the ordinary pressure, failure mode, mechanism, or evaluation target differs from neighboring groups.

#### Prosody control

Set or predict pitch, duration, energy, and pauses so the same words can sound questioning, emphatic, calm, or urgent.

**Positive membership example:** A user or model sets pitch, timing, energy, or pauses while keeping words fixed.

**Negative/boundary example:** Changing speaker identity without an explicit timing or melody control is not prosody control.

**Boundary:** Independent controls can conflict; expressive variation may change perceived meaning or naturalness.

**Evidence rule:** D2 abstract evidence must name the spoken-speech object and conceptual pressure; D3 full-paper evidence must additionally support the mechanism and evaluation object.

#### Style and emotion control

Condition generation on a speaking style or affective target while preserving the requested content.

**Positive membership example:** A generation system is conditioned on a style or affect target while preserving content.

**Negative/boundary example:** A classifier that only labels emotion but generates nothing is not style control.

**Boundary:** Emotion categories are culturally and contextually unstable, and a label may not describe what listeners perceive.

**Evidence rule:** D2 abstract evidence must name the spoken-speech object and conceptual pressure; D3 full-paper evidence must additionally support the mechanism and evaluation object.

#### Interactive generation latency

Produce speech quickly enough for a conversation while preserving continuity and allowing interruption or correction.

**Positive membership example:** A voice system speaks quickly, permits interruption, and responds within conversational timing.

**Negative/boundary example:** Offline synthesis with no response-time or interruption constraint is not interactive latency work.

**Boundary:** Low latency can require shorter context, lower quality, or speculative output that must later be repaired.

**Evidence rule:** D2 abstract evidence must name the spoken-speech object and conceptual pressure; D3 full-paper evidence must additionally support the mechanism and evaluation object.

## Speakers as changing people, not nuisance variables

**Ordinary problem:** Voice depends on anatomy, age, health, emotion, language history, social setting, and equipment; these differences affect both communication and measurement.

**Why the naive approach fails:** Treating variation as noise makes systems work best for a narrow population and can turn a health or identity signal into an unwanted demographic shortcut.

**Recurring conceptual move:** Measure which variation is task-relevant, model it explicitly when appropriate, and test performance and meaning across people and conditions.

**Tradeoff/boundary:** A factor that helps prediction may be sensitive, confounded, or harmful to expose; personalization can improve access while increasing privacy risk.

### Identity, age, and changing voice

**Question:** What ordinary speech pressure is handled by identity, age, and changing voice, and what evidence distinguishes it from neighboring pressures?
**Why this boundary exists:** The evidence concerns who is speaking and how that person's voice changes across time and state.
**Derivation rule:** Split or retained because the ordinary pressure, failure mode, mechanism, or evaluation target differs from neighboring groups.

#### Speaker verification

Decide whether two recordings plausibly came from the same person under channel, time, and content variation.

**Positive membership example:** Two recordings are compared to decide whether they came from the same person.

**Negative/boundary example:** Predicting age or emotion without comparing identity is not speaker verification.

**Boundary:** Similarity scores are not identity proof and depend on enrollment quality, population, and decision threshold.

**Evidence rule:** D2 abstract evidence must name the spoken-speech object and conceptual pressure; D3 full-paper evidence must additionally support the mechanism and evaluation object.

#### Age and developmental speech

Children and older adults differ in anatomy, articulation, vocabulary, and interaction needs, so adult data is not a neutral reference.

**Positive membership example:** A system models children or older adults whose anatomy, language, or interaction differs from adults.

**Negative/boundary example:** A generic adult corpus with age omitted is not age/development analysis.

**Boundary:** Age prediction or age normalization can encode stereotypes and may not address the actual recognition failure.

**Evidence rule:** D2 abstract evidence must name the spoken-speech object and conceptual pressure; D3 full-paper evidence must additionally support the mechanism and evaluation object.

#### Within-speaker state variation

The same person's voice shifts with fatigue, emotion, health, audience, and speaking effort; robust systems must not confuse state with identity.

**Positive membership example:** The same speaker is measured across fatigue, emotion, effort, audience, or health states.

**Negative/boundary example:** Differences only between unrelated speakers are not within-speaker state variation.

**Boundary:** There is no universal stable identity vector independent of context.

**Evidence rule:** D2 abstract evidence must name the spoken-speech object and conceptual pressure; D3 full-paper evidence must additionally support the mechanism and evaluation object.

### Speech measurements associated with health

**Question:** What ordinary speech pressure is handled by speech measurements associated with health, and what evidence distinguishes it from neighboring pressures?
**Why this boundary exists:** A measurable speech property is evaluated as a possible health signal, with clinical limits kept explicit.
**Derivation rule:** Split or retained because the ordinary pressure, failure mode, mechanism, or evaluation target differs from neighboring groups.

#### Clinical speech marker

Measure a reproducible speech property associated with a clinical condition or progression, while separating it from age, device, and language effects.

**Positive membership example:** A reproducible pause, articulation, or voice measure is tested against a clinical condition or severity scale.

**Negative/boundary example:** A speech feature correlated with a generic class but never tied to a clinical target is not a clinical marker.

**Boundary:** Association with a diagnosis is not clinical validity, causation, or permission to make a medical decision.

**Evidence rule:** D2 abstract evidence must name the spoken-speech object and conceptual pressure; D3 full-paper evidence must additionally support the mechanism and evaluation object.

### Communicating with atypical or impaired speech

**Question:** What ordinary speech pressure is handled by communicating with atypical or impaired speech, and what evidence distinguishes it from neighboring pressures?
**Why this boundary exists:** The goal is recognition or expression for people whose speech does not match majority training data.
**Derivation rule:** Split or retained because the ordinary pressure, failure mode, mechanism, or evaluation target differs from neighboring groups.

#### Atypical articulation and dysarthria

Recognize or synthesize speech whose timing, precision, or coordination differs from training norms instead of treating it as mere noise.

**Positive membership example:** Recognition or synthesis explicitly handles atypical timing, precision, or coordination.

**Negative/boundary example:** Treating all low-confidence speech as atypical without a speaker or disorder target is not this concept.

**Boundary:** Small datasets and speaker-specific patterns make broad claims especially fragile.

**Evidence rule:** D2 abstract evidence must name the spoken-speech object and conceptual pressure; D3 full-paper evidence must additionally support the mechanism and evaluation object.

#### Augmentative communication

Use residual vocal, muscular, visual, or typed signals to help a person express intended language or control a device.

**Positive membership example:** Residual vocal, muscular, visual, or typed signals are turned into a person's intended communication.

**Negative/boundary example:** A general speech recognizer for fluent speakers is not augmentative communication.

**Boundary:** A system should preserve the person's authorship and offer correction, not silently decide what they meant.

**Evidence rule:** D2 abstract evidence must name the spoken-speech object and conceptual pressure; D3 full-paper evidence must additionally support the mechanism and evaluation object.

### Whether the system actually helps a person

**Question:** What ordinary speech pressure is handled by whether the system actually helps a person, and what evidence distinguishes it from neighboring pressures?
**Why this boundary exists:** The target is effort, control, access, and fit in a real activity rather than model accuracy alone.
**Derivation rule:** Split or retained because the ordinary pressure, failure mode, mechanism, or evaluation target differs from neighboring groups.

#### Listener effort

Measure how much concentration, repetition, or repair a listener needs, not just whether a word error count changed.

**Positive membership example:** Listeners' concentration, repetition, or effort is measured under a speech condition.

**Negative/boundary example:** WER alone, with no listener task or report, is not listener-effort evidence.

**Boundary:** Effort measures depend on task, listener experience, and presentation conditions.

**Evidence rule:** D2 abstract evidence must name the spoken-speech object and conceptual pressure; D3 full-paper evidence must additionally support the mechanism and evaluation object.

#### User control and consent

Let speakers decide how their voice is recorded, adapted, generated, shared, or corrected, especially when identity is involved.

**Positive membership example:** A system gives people control over recording, adaptation, generation, sharing, or correction of their voice.

**Negative/boundary example:** A privacy statement with no user choice or withdrawal path is not demonstrated control.

**Boundary:** A consent checkbox does not solve power imbalance, downstream copying, or inability to withdraw a trained model.

**Evidence rule:** D2 abstract evidence must name the spoken-speech object and conceptual pressure; D3 full-paper evidence must additionally support the mechanism and evaluation object.

#### Accessibility fit

Judge whether a system works within a person's actual device, environment, communication practice, and time constraints.

**Positive membership example:** Evaluation includes the person's actual device, environment, communication practice, setup burden, or timing needs.

**Negative/boundary example:** A clean laboratory score with no user or deployment constraint is not accessibility fit.

**Boundary:** A lab improvement can be irrelevant or harmful if setup, latency, or interaction burden is omitted.

**Evidence rule:** D2 abstract evidence must name the spoken-speech object and conceptual pressure; D3 full-paper evidence must additionally support the mechanism and evaluation object.

## Many languages, accents, and unequal evidence

**Ordinary problem:** Languages differ in sounds, writing systems, grammar, prosody, code-switching, and social meaning; data and tools are distributed unevenly.

**Why the naive approach fails:** Scaling an English-centered recipe or translating labels assumes that all languages expose the same units, data, and errors.

**Recurring conceptual move:** Share useful structure across languages while preserving language-specific distinctions, measuring who benefits, and making uncertainty visible where evidence is thin.

**Tradeoff/boundary:** Transfer can import pronunciation or cultural assumptions, and aggregate multilingual scores can hide severe failures in a small language or community.

### Sharing structure across languages

**Question:** What ordinary speech pressure is handled by sharing structure across languages, and what evidence distinguishes it from neighboring pressures?
**Why this boundary exists:** The central question is what can be shared while retaining language-specific distinctions.
**Derivation rule:** Split or retained because the ordinary pressure, failure mode, mechanism, or evaluation target differs from neighboring groups.

#### Cross-lingual transfer

Reuse representations or training signals from one language to improve another when their speech structure overlaps.

**Positive membership example:** Training signals or representations from one language improve another language while measuring what is lost.

**Negative/boundary example:** Translating an English label without cross-language speech evidence is not cross-lingual transfer.

**Boundary:** Transfer may favor high-resource languages and erase distinctions absent from the source language.

**Evidence rule:** D2 abstract evidence must name the spoken-speech object and conceptual pressure; D3 full-paper evidence must additionally support the mechanism and evaluation object.

#### Language and variety identification

Determine which language or variety is being spoken so the appropriate recognizer or interaction policy can be selected.

**Positive membership example:** The system selects a language or variety from spoken input before choosing a downstream policy.

**Negative/boundary example:** Classifying topics or speakers without language choice is not language identification.

**Boundary:** Closely related varieties and code-switching make a single label inadequate or politically loaded.

**Evidence rule:** D2 abstract evidence must name the spoken-speech object and conceptual pressure; D3 full-paper evidence must additionally support the mechanism and evaluation object.

#### Code-switching

Handle a speaker moving between languages within an utterance, including pronunciation, grammar, and word-boundary changes.

**Positive membership example:** A single utterance changes language and the recognizer preserves its words, boundaries, and pronunciation shifts.

**Negative/boundary example:** Separate monolingual recordings are not code-switching.

**Boundary:** A monolingual metric can count appropriate switching as error and fail to define the intended transcript.

**Evidence rule:** D2 abstract evidence must name the spoken-speech object and conceptual pressure; D3 full-paper evidence must additionally support the mechanism and evaluation object.

### Learning from sparse labels

**Question:** What ordinary speech pressure is handled by learning from sparse labels, and what evidence distinguishes it from neighboring pressures?
**Why this boundary exists:** The method changes how a model learns when labeled examples are scarce.
**Derivation rule:** Split or retained because the ordinary pressure, failure mode, mechanism, or evaluation target differs from neighboring groups.

#### Self-training

Use a model's predictions on unlabeled speech as additional training signals, ideally filtering or weighting uncertain labels.

**Positive membership example:** A model labels unlabeled speech and filtered predictions become new training examples.

**Negative/boundary example:** Adding more human-transcribed data is not self-training.

**Boundary:** Errors can reinforce themselves and create a false appearance of data scale.

**Evidence rule:** D2 abstract evidence must name the spoken-speech object and conceptual pressure; D3 full-paper evidence must additionally support the mechanism and evaluation object.

#### Few-shot adaptation

Adjust a model to a language, speaker, or domain from a small number of examples rather than retraining from scratch.

**Positive membership example:** A model changes to a new language, speaker, or domain from only a small number of examples.

**Negative/boundary example:** A full retraining run on a large new corpus is not few-shot adaptation.

**Boundary:** Few examples may cover only one speaker or style and make variance look like progress.

**Evidence rule:** D2 abstract evidence must name the spoken-speech object and conceptual pressure; D3 full-paper evidence must additionally support the mechanism and evaluation object.

### Making missing speech evidence

**Question:** What ordinary speech pressure is handled by making missing speech evidence, and what evidence distinguishes it from neighboring pressures?
**Why this boundary exists:** The work creates speakers, prompts, labels, or recordings needed by a community or task.
**Derivation rule:** Split or retained because the ordinary pressure, failure mode, mechanism, or evaluation target differs from neighboring groups.

#### Speech data collection

Design recording prompts, speakers, transcription, and consent so newly collected data covers the intended community and task.

**Positive membership example:** A study designs prompts, speakers, transcripts, permissions, and sampling for a new speech corpus.

**Negative/boundary example:** Using an existing benchmark without examining its collection is not data-collection analysis.

**Boundary:** More hours do not fix biased sampling, poor transcripts, or a task definition that excludes natural speech.

**Evidence rule:** D2 abstract evidence must name the spoken-speech object and conceptual pressure; D3 full-paper evidence must additionally support the mechanism and evaluation object.

### Respecting variation and local meaning

**Question:** What ordinary speech pressure is handled by respecting variation and local meaning, and what evidence distinguishes it from neighboring pressures?
**Why this boundary exists:** This boundary covers differences in pronunciation, variety, and local meaning that affect who is understood and how speech is interpreted; it is separate from generic low-resource learning because more data alone cannot decide whether a social or cultural distinction was represented correctly.
**Derivation rule:** Split or retained because the ordinary pressure, failure mode, mechanism, or evaluation target differs from neighboring groups.

#### Accent robustness

Maintain intended-word accuracy across pronunciation patterns that differ from the training majority.

**Positive membership example:** Intended-word accuracy is measured across pronunciation patterns outside the training majority.

**Negative/boundary example:** A pooled score with no accent or variety breakdown is not evidence of accent robustness.

**Boundary:** A single pooled error rate cannot show which accents fail or whether adaptation changes identity representation.

**Evidence rule:** D2 abstract evidence must name the spoken-speech object and conceptual pressure; D3 full-paper evidence must additionally support the mechanism and evaluation object.

#### Dialect and variety

Treat grammar, vocabulary, pronunciation, and discourse conventions of a variety as part of the language, not merely deviations from a standard.

**Positive membership example:** A study treats a community's pronunciation, grammar, vocabulary, or discourse as a language variety.

**Negative/boundary example:** Calling every deviation from a standard an error is the boundary failure, not dialect analysis.

**Boundary:** Dialect labels can be contested and may conflate region, ethnicity, class, and speaker identity.

**Evidence rule:** D2 abstract evidence must name the spoken-speech object and conceptual pressure; D3 full-paper evidence must additionally support the mechanism and evaluation object.

#### Cultural meaning

Interpret politeness, indirectness, emotion, and conversational norms within the community that uses them.

**Positive membership example:** Interpretation is evaluated against community-specific politeness, indirectness, emotion, or conversational norms.

**Negative/boundary example:** Importing a label from another culture without local interpretation is not cultural-meaning analysis.

**Boundary:** A label imported from another culture may be statistically convenient but semantically wrong.

**Evidence rule:** D2 abstract evidence must name the spoken-speech object and conceptual pressure; D3 full-paper evidence must additionally support the mechanism and evaluation object.

## Evidence, practical systems, and consequences

**Ordinary problem:** Speech systems are used through microphones, networks, interfaces, policies, and people; a benchmark number is only one observation of that whole chain.

**Why the naive approach fails:** Reporting one average score on one dataset encourages the reader to treat a proxy as universal ability and ignores latency, failure recovery, privacy, and misuse.

**Recurring conceptual move:** Align the evaluation with the real target, expose subgroup and condition variation, account for the full system boundary, and preserve an audit trail from evidence to claim.

**Tradeoff/boundary:** Broader evaluation costs time and data, but narrow evidence can create false confidence exactly where speech systems affect access, identity, or safety.

### Connecting scores to human goals

**Question:** What ordinary speech pressure is handled by connecting scores to human goals, and what evidence distinguishes it from neighboring pressures?
**Why this boundary exists:** A metric is a proxy and must be tied to the human or engineering property it represents.
**Derivation rule:** Split or retained because the ordinary pressure, failure mode, mechanism, or evaluation target differs from neighboring groups.

#### Word error versus understanding

A transcript edit distance counts substitutions, insertions, and deletions, but a small count is not automatically successful task understanding.

**Positive membership example:** A paper compares transcript edit distance with whether a person can complete the intended task or recover critical entities.

**Negative/boundary example:** Reporting WER and calling it understanding without a task measure is not this concept.

**Boundary:** A word metric can miss critical entity errors and can penalize harmless orthographic or dialect differences.

**Evidence rule:** D2 abstract evidence must name the spoken-speech object and conceptual pressure; D3 full-paper evidence must additionally support the mechanism and evaluation object.

#### Quality and naturalness

Listening ratings, preference tests, and signal measures estimate different aspects of whether generated or enhanced speech is acceptable.

**Positive membership example:** Listeners or a defined signal target judge acceptability, preference, naturalness, or intelligibility under stated conditions.

**Negative/boundary example:** An unexplained aggregate score with no target or listening condition is not quality evidence.

**Boundary:** A score without listeners, conditions, and target definition cannot support a general quality claim.

**Evidence rule:** D2 abstract evidence must name the spoken-speech object and conceptual pressure; D3 full-paper evidence must additionally support the mechanism and evaluation object.

#### Calibration and selective use

A system should know when its uncertainty is high enough to defer, ask, or show alternatives rather than making every output look certain.

**Positive membership example:** A system defers, asks, or shows alternatives when confidence does not match observed correctness.

**Negative/boundary example:** A softmax score reported without reliability or selective behavior is not calibration.

**Boundary:** Calibration on a held-out sample does not guarantee safety under a new population or distribution.

**Evidence rule:** D2 abstract evidence must name the spoken-speech object and conceptual pressure; D3 full-paper evidence must additionally support the mechanism and evaluation object.

### Changing speakers, rooms, and conditions

**Question:** What ordinary speech pressure is handled by changing speakers, rooms, and conditions, and what evidence distinguishes it from neighboring pressures?
**Why this boundary exists:** The question is whether failures are detected and recovered when conditions differ from training.
**Derivation rule:** Split or retained because the ordinary pressure, failure mode, mechanism, or evaluation target differs from neighboring groups.

#### Distribution shift

Performance changes when speakers, microphones, rooms, languages, topics, or noise differ from training and test conditions.

**Positive membership example:** The same system is tested across new speakers, rooms, microphones, languages, topics, or noise conditions.

**Negative/boundary example:** Calling a dataset diverse without measuring a train-test change is not distribution-shift evidence.

**Boundary:** A named shift is not evidence of coverage; the shift must be measured and tied to the failure.

**Evidence rule:** D2 abstract evidence must name the spoken-speech object and conceptual pressure; D3 full-paper evidence must additionally support the mechanism and evaluation object.

#### End-to-end recovery

Handle uncertainty through confirmation, correction, fallback, and logging so one recognition error does not become an irreversible action.

**Positive membership example:** A recognition error leads to confirmation, correction, fallback, or logging instead of irreversible action.

**Negative/boundary example:** Improving one model component without testing downstream recovery is not end-to-end recovery.

**Boundary:** A robust component is not an end-to-end safe system if downstream policy ignores its uncertainty.

**Evidence rule:** D2 abstract evidence must name the spoken-speech object and conceptual pressure; D3 full-paper evidence must additionally support the mechanism and evaluation object.

### Meeting time, memory, and hardware limits

**Question:** What ordinary speech pressure is handled by meeting time, memory, and hardware limits, and what evidence distinguishes it from neighboring pressures?
**Why this boundary exists:** The system must operate within a device or interaction budget without hiding cost elsewhere.
**Derivation rule:** Split or retained because the ordinary pressure, failure mode, mechanism, or evaluation target differs from neighboring groups.

#### Latency and resource budget

A system must meet timing, memory, energy, bandwidth, and hardware limits while preserving the property users need.

**Positive membership example:** A paper measures response time, memory, energy, bandwidth, or compute under a deployment constraint.

**Negative/boundary example:** A smaller parameter count with no resource or timing measurement is not a deployment-budget result.

**Boundary:** A faster model may emit less context, reduce quality, or move cost into an unreported service.

**Evidence rule:** D2 abstract evidence must name the spoken-speech object and conceptual pressure; D3 full-paper evidence must additionally support the mechanism and evaluation object.

### Protecting voice and resisting misuse

**Question:** What ordinary speech pressure is handled by protecting voice and resisting misuse, and what evidence distinguishes it from neighboring pressures?
**Why this boundary exists:** This boundary covers harm from exposing voice identity or accepting imitation, replay, or generated speech as genuine; it is separate from ordinary robustness because the failure is unauthorized inference or deception, not merely a lower score in a changed condition.
**Derivation rule:** Split or retained because the ordinary pressure, failure mode, mechanism, or evaluation target differs from neighboring groups.

#### Voice privacy

Speech recordings reveal content and may reveal identity, health, location, emotion, or group membership, so collection and storage are part of the technical problem.

**Positive membership example:** A system limits or audits what identity, health, location, or content can be inferred from recorded speech.

**Negative/boundary example:** Deleting the transcript while retaining identifiable acoustic recordings is not voice privacy.

**Boundary:** Removing words does not necessarily remove speaker identity or sensitive acoustic information.

**Evidence rule:** D2 abstract evidence must name the spoken-speech object and conceptual pressure; D3 full-paper evidence must additionally support the mechanism and evaluation object.

#### Spoofing and synthetic voice misuse

A system must distinguish authorized speech from replayed or generated audio when identity or access depends on it.

**Positive membership example:** A detector tests replayed or generated speech against an identity or access decision, including unseen attacks.

**Negative/boundary example:** A normal speech classifier with no adversarial or synthetic-audio threat model is not spoofing analysis.

**Boundary:** A detector trained on known generators can fail on unseen synthesis, replay channels, or an attacker who changes the interaction.

**Evidence rule:** D2 abstract evidence must name the spoken-speech object and conceptual pressure; D3 full-paper evidence must additionally support the mechanism and evaluation object.

### Keeping claims inspectable and contestable

**Question:** What ordinary speech pressure is handled by keeping claims inspectable and contestable, and what evidence distinguishes it from neighboring pressures?
**Why this boundary exists:** A person must be able to trace evidence, uncertainty, and correction when a speech system matters.
**Derivation rule:** Split or retained because the ordinary pressure, failure mode, mechanism, or evaluation target differs from neighboring groups.

#### Auditability and contestability

Keep enough provenance, uncertainty, and correction path for a person to understand and challenge a consequential speech-derived decision.

**Positive membership example:** A consequential speech-derived decision preserves provenance, uncertainty, and a way for a person to challenge it.

**Negative/boundary example:** A confidence number without evidence trace or appeal path is not auditability.

**Boundary:** A stored confidence number is not an explanation of what evidence drove the decision.

**Evidence rule:** D2 abstract evidence must name the spoken-speech object and conceptual pressure; D3 full-paper evidence must additionally support the mechanism and evaluation object.
