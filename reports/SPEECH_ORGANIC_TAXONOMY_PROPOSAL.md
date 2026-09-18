# Organic taxonomy proposal

This is a derivation proposal, not yet the canonical taxonomy. It records why each proposed boundary exists and which reviewed concept families motivate it.

Proposed subthemes: **34**; current fixed subthemes: **24**.

## Sound, bodies, rooms, and recording — 4 proposed subthemes

The corpus separates the act of making sound from the act of measuring a changing signal and from the channel that carries it.

### Making a physical sound

- Supported-paper evidence inherited from current concepts: **15**
- Current concepts: `periodic-source`, `vocal-tract-filter`
- Boundary: The source and tract shape the pressure wave before a device records it.

### Coordinating moving speech parts

- Supported-paper evidence inherited from current concepts: **29**
- Current concepts: `articulatory-coordination`
- Boundary: Gesture overlap and timing are the object; a static source/filter description is not enough.

### Representing a changing signal

- Supported-paper evidence inherited from current concepts: **27**
- Current concepts: `windowed-spectrum`, `multi-resolution-signal`, `sampling-and-quantization`
- Boundary: The question is what a digital representation keeps or loses across time, frequency, and precision.

### Changing the path from source to sensor

- Supported-paper evidence inherited from current concepts: **32**
- Current concepts: `reverberant-mixture`, `microphone-channel`, `non-airborne-sensing`
- Boundary: Room reflections, device coloration, and alternate sensors change the evidence before recognition.

## Listening through noise, overlap, and missing sound — 5 proposed subthemes

The papers distinguish suppressing nuisance, recovering a chosen source, using space to choose it, and repairing information that is absent or perceptually damaged.

### Suppressing changing interference

- Supported-paper evidence inherited from current concepts: **52**
- Current concepts: `spectral-mask`, `speech-prior-denoising`, `nonstationary-noise`
- Boundary: The target is one speech stream and the failure is removing speech along with noise.

### Recovering several hidden sources

- Supported-paper evidence inherited from current concepts: **49**
- Current concepts: `blind-source-separation`, `target-conditioned-separation`
- Boundary: The mixture contains multiple sources and the system must infer source identity or count.

### Using location to select sound

- Supported-paper evidence inherited from current concepts: **14**
- Current concepts: `spatial-filtering`
- Boundary: Microphone geometry and direction are the evidence; a single-channel separator has a different limit.

### Canceling copies and filling gaps

- Supported-paper evidence inherited from current concepts: **8**
- Current concepts: `acoustic-echo-cancellation`, `packet-loss-concealment`
- Boundary: The unwanted signal is a known delayed copy or missing frame, not an arbitrary background.

### Optimizing what a listener can use

- Supported-paper evidence inherited from current concepts: **17**
- Current concepts: `perceptual-enhancement`
- Boundary: The target is intelligibility or acceptability rather than exact waveform recovery.

## From sound to words and structured speech — 4 proposed subthemes

Recognition papers separate learning sound units, handling pronunciation variation, locating sequence boundaries, and using context to resolve open vocabulary.

### Learning reusable sound units

- Supported-paper evidence inherited from current concepts: **46**
- Current concepts: `acoustic-to-token`, `self-supervised-speech-units`
- Boundary: The system first decides what reusable evidence can be extracted from continuous sound.

### Allowing different realizations of words

- Supported-paper evidence inherited from current concepts: **16**
- Current concepts: `pronunciation-variation`
- Boundary: The same intended unit has multiple acoustic paths; this is distinct from learning a unit representation.

### Locating units in time

- Supported-paper evidence inherited from current concepts: **37**
- Current concepts: `alignment`, `disfluency-preservation`
- Boundary: The output must preserve or locate timing, hesitation, repair, or sequence boundaries.

### Using context without inventing words

- Supported-paper evidence inherited from current concepts: **43**
- Current concepts: `long-context-decoding`, `domain-and-context-biasing`, `speaker-adaptation`, `open-vocabulary-recognition`
- Boundary: Context, speaker evidence, and new words resolve ambiguity but can override what was actually said.

## From spoken form to meaning and coordinated action — 4 proposed subthemes

The corpus distinguishes information carried by voice, state carried across turns, timing of participation, and grounding language in people or actions.

### Meaning carried by how speech sounds

- Supported-paper evidence inherited from current concepts: **85**
- Current concepts: `prosodic-meaning`, `paralinguistic-state`
- Boundary: Pitch, timing, voice quality, and effort add information beyond words.

### Inferring what a speaker is trying to do

- Supported-paper evidence inherited from current concepts: **22**
- Current concepts: `intent-in-context`, `dialogue-state`
- Boundary: The system tracks goals, commitments, and situation rather than only classifying acoustic style.

### Coordinating participation under uncertainty

- Supported-paper evidence inherited from current concepts: **13**
- Current concepts: `turn-boundary`, `repair-and-clarification`
- Boundary: The problem is when to speak, yield, interrupt, or ask for clarification.

### Connecting language to a shared world

- Supported-paper evidence inherited from current concepts: **24**
- Current concepts: `referential-grounding`, `speech-act`, `interactional-feedback`
- Boundary: A phrase must identify a referent or authorized action and remain corrigible through feedback.

## Creating speech while keeping the right things fixed — 4 proposed subthemes

Generation papers separate planning content, producing fine waveform detail, changing identity, and controlling expression or interaction.

### Turning language into a timed speech plan

- Supported-paper evidence inherited from current concepts: **15**
- Current concepts: `text-to-speech-planning`
- Boundary: Text must become pronunciation, duration, pitch targets, and an audible sequence.

### Producing or compressing audible detail

- Supported-paper evidence inherited from current concepts: **14**
- Current concepts: `neural-vocoder`, `intelligibility-naturalness`
- Boundary: The issue is sample-level detail and the tradeoff between faithful content and natural sound.

### Changing who sounds like the speaker

- Supported-paper evidence inherited from current concepts: **31**
- Current concepts: `speaker-identity`, `voice-conversion`, `zero-shot-voice`
- Boundary: Identity changes while linguistic content is meant to remain stable.

### Changing style, timing, and response behavior

- Supported-paper evidence inherited from current concepts: **36**
- Current concepts: `prosody-control`, `style-and-emotion-control`, `interactive-latency`
- Boundary: The system must obey expressive controls quickly without breaking continuity or meaning.

## Speakers as changing people, not nuisance variables — 4 proposed subthemes

The papers separate identity and within-person change, clinical measurement, atypical/assistive communication, and whether a system fits a person's real life.

### Identity, age, and changing voice

- Supported-paper evidence inherited from current concepts: **64**
- Current concepts: `speaker-verification`, `age-and-development`, `style-and-state-variation`
- Boundary: The evidence concerns who is speaking and how that person's voice changes across time and state.

### Speech measurements associated with health

- Supported-paper evidence inherited from current concepts: **74**
- Current concepts: `clinical-speech-marker`
- Boundary: A measurable speech property is evaluated as a possible health signal, with clinical limits kept explicit.

### Communicating with atypical or impaired speech

- Supported-paper evidence inherited from current concepts: **41**
- Current concepts: `dysarthria-and-atypical-speech`, `augmentative-communication`
- Boundary: The goal is recognition or expression for people whose speech does not match majority training data.

### Whether the system actually helps a person

- Supported-paper evidence inherited from current concepts: **23**
- Current concepts: `listener-effort`, `user-control-and-consent`, `accessibility-fit`
- Boundary: The target is effort, control, access, and fit in a real activity rather than model accuracy alone.

## Many languages, accents, and unequal evidence — 4 proposed subthemes

The papers distinguish sharing structure across languages, learning with little data, creating missing evidence, and interpreting varieties without treating them as errors.

### Sharing structure across languages

- Supported-paper evidence inherited from current concepts: **34**
- Current concepts: `crosslingual-transfer`, `language-identification`, `code-switching`
- Boundary: The central question is what can be shared while retaining language-specific distinctions.

### Learning from sparse labels

- Supported-paper evidence inherited from current concepts: **28**
- Current concepts: `self-training-and-pseudo-labels`, `few-shot-adaptation`
- Boundary: The method changes how a model learns when labeled examples are scarce.

### Making missing speech evidence

- Supported-paper evidence inherited from current concepts: **40**
- Current concepts: `speech-data-collection`
- Boundary: The work creates speakers, prompts, labels, or recordings needed by a community or task.

### Respecting variation and local meaning

- Supported-paper evidence inherited from current concepts: **46**
- Current concepts: `accent-robustness`, `dialect-and-variety`, `cultural-meaning`
- Boundary: The boundary is social and linguistic interpretation, not only transfer accuracy.

## Evidence, practical systems, and consequences — 5 proposed subthemes

The corpus separates what a score stands for, what changes outside the test set, what a device can afford, and what voice technology can expose or harm.

### Connecting scores to human goals

- Supported-paper evidence inherited from current concepts: **40**
- Current concepts: `word-error-versus-understanding`, `quality-and-naturalness`, `calibration-and-selective-use`
- Boundary: A metric is a proxy and must be tied to the human or engineering property it represents.

### Changing speakers, rooms, and conditions

- Supported-paper evidence inherited from current concepts: **15**
- Current concepts: `distribution-shift`, `end-to-end-recovery`
- Boundary: The question is whether failures are detected and recovered when conditions differ from training.

### Meeting time, memory, and hardware limits

- Supported-paper evidence inherited from current concepts: **29**
- Current concepts: `latency-and-resource`
- Boundary: The system must operate within a device or interaction budget without hiding cost elsewhere.

### Protecting voice and resisting misuse

- Supported-paper evidence inherited from current concepts: **60**
- Current concepts: `voice-privacy`, `spoofing-and-deepfake`
- Boundary: The risk concerns sensitive voice evidence, impersonation, replay, and generated speech.

### Keeping claims inspectable and contestable

- Supported-paper evidence inherited from current concepts: **11**
- Current concepts: `auditability-and-contestability`
- Boundary: A person must be able to trace evidence, uncertainty, and correction when a speech system matters.

