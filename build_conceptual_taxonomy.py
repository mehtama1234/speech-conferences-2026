#!/usr/bin/env python3
"""Build the analyst-authored first-principles speech taxonomy.

This is deliberately separate from the old abstract keyword map.  The latter
finds candidates; this artifact states the concepts and their boundaries that
later semantic review must test against the papers.
"""

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data"
REPORTS = ROOT / "reports"


def concept(cid, name, definition, boundary):
    return {
        "id": cid,
        "name": name,
        "definition": definition,
        "boundary": boundary,
    }


def subtheme(sid, name, question, concepts):
    return {"id": sid, "name": name, "question": question, "concepts": concepts}


def theme(tid, name, question, ordinary_problem, naive_failure, recurring_move,
         tradeoff, subthemes):
    return {
        "id": tid,
        "name": name,
        "question": question,
        "ordinary_problem": ordinary_problem,
        "naive_failure": naive_failure,
        "recurring_move": recurring_move,
        "tradeoff": tradeoff,
        "subthemes": subthemes,
    }


TAXONOMY = [
    theme(
        "sound-and-production", "Sound, bodies, rooms, and recording",
        "How does a human or other source turn a physical event into the signal a machine receives?",
        "Speech reaches a microphone as changing air pressure after vocal-fold vibration, mouth shape, room reflections, and electronics have already mixed together.",
        "Treating the waveform as an unstructured list of samples hides which changes came from the talker, the room, or the recording device.",
        "Separate source, filter, geometry, and time scale so a measured signal can be related back to a physical cause.",
        "A useful physical description can be wrong when bodies, rooms, or microphones violate its assumptions.",
        [
            subtheme("source-filter-production", "How bodies make voiced and unvoiced sound", "Which parts of the signal come from the source and which from the moving vocal tract?", [
                concept("periodic-source", "Periodic vocal-fold source", "A speaker can repeatedly open and close the vocal folds; the repetition supplies pitch and harmonic energy while its exact timing varies.", "Not every speech segment is periodic: frication, stops, breath, and irregular phonation cannot be reduced to one stable pitch."),
                concept("vocal-tract-filter", "Vocal-tract filtering", "The tongue, lips, jaw, and throat reshape source energy so some frequency regions are strengthened and others weakened; those regions carry much of vowel identity.", "A filter-only explanation misses changes caused directly by source irregularity, radiation, or recording conditions."),
                concept("articulatory-coordination", "Articulatory coordination", "Speech is a timed coordination of several moving constrictions, not a sequence of isolated sounds; overlap lets one gesture affect its neighbors.", "A label such as a phoneme is not itself a physical movement or a complete account of coarticulation."),
            ]),
            subtheme("time-frequency-measurement", "Representing a changing sound", "What must be preserved when a continuous signal is made into manageable measurements?", [
                concept("windowed-spectrum", "Local frequency content", "Short windows expose which frequencies are present near each moment, making pitch, resonances, and noise easier to compare than raw samples alone.", "A window discards some exact timing and long-range phase; two signals with similar spectra may still sound different."),
                concept("multi-resolution-signal", "Multiple time scales", "Fast events such as consonant closures and slow changes such as intonation require measurements at different temporal resolutions.", "Adding resolutions is not automatically informative; it can increase computation or preserve nuisance variation."),
                concept("sampling-and-quantization", "Sampling and quantization", "A digital recording keeps a finite set of amplitude measurements, so the sampling rate and numeric precision set what can still be recovered.", "A high sample rate cannot restore information lost through clipping, poor microphones, or an absent frequency range."),
            ]),
            subtheme("room-channel-and-sensing", "Rooms, devices, and unusual sensors", "How does the path from talker to sensor alter the speech evidence?", [
                concept("reverberant-mixture", "Reverberant room mixture", "The microphone hears direct sound plus delayed reflections, so a word can overlap its own earlier energy and blur boundaries.", "Reverberation is not just additive stationary noise; its delay pattern depends on room geometry and position."),
                concept("microphone-channel", "Microphone and channel coloration", "A device emphasizes some frequencies, clips loud peaks, or transmits only a narrow band, changing the evidence available to a recognizer.", "Channel normalization can remove useful speaker or environment information along with nuisance coloration."),
                concept("non-airborne-sensing", "Non-airborne speech sensing", "Neck vibration, ultrasound, radar, or muscle signals can observe speech when airborne audio is missing, but they observe a different projection of the act.", "A sensor that works in quiet laboratory placement is not automatically a replacement for ordinary audio in daily use."),
            ]),
        ],
    ),
    theme(
        "listening-and-separation", "Listening through noise, overlap, and missing sound",
        "How can a system recover one useful speech stream from several competing or damaged signals?",
        "A listener often hears several talkers, music, echo, and device noise at once, yet needs one person's words or an intelligible mixture.",
        "Amplifying everything or subtracting an average noise profile also removes quiet consonants and fails when the interferer changes with the speech.",
        "Use structure that differs between target and interference—time, frequency, space, source identity, or learned speech regularity—to estimate and reconstruct the target.",
        "A cleaner waveform may be less faithful, introduce artifacts, or favor the wrong speaker when the mixture is ambiguous.",
        [
            subtheme("noise-enhancement", "Suppressing background noise without erasing speech", "Which variation is nuisance and which is the quiet speech cue needed for intelligibility?", [
                concept("spectral-mask", "Time-frequency masking", "Estimate how much each local frequency region belongs to speech, then attenuate regions dominated by noise.", "A binary or soft mask can create musical noise and cannot reliably separate sources that occupy the same region."),
                concept("speech-prior-denoising", "Speech-prior denoising", "A model learned from clean speech can fill in a plausible speech pattern where the recording is noisy, trading exact fidelity for intelligibility.", "A plausible completion can hallucinate phonetic detail the microphone never captured."),
                concept("nonstationary-noise", "Changing and adverse noise", "The useful distinction is whether noise changes faster than the system can track, as with competing speech, vehicles, or sudden events.", "A result on fixed background noise does not establish performance under changing or speech-like interference."),
            ]),
            subtheme("source-separation-and-spatial-listening", "Choosing one source from a mixture", "How can a system decide which part of a mixture belongs to the target talker?", [
                concept("blind-source-separation", "Blind source separation", "Infer several hidden signals from their mixture using differences in statistics, timing, or spectral structure without receiving isolated sources at test time.", "The mixture may not contain enough information to identify sources uniquely; permutation and source-count assumptions matter."),
                concept("spatial-filtering", "Spatial filtering", "Several microphones provide direction-dependent differences, allowing a filter to reinforce one location and reject others.", "A single microphone or moving speaker removes the spatial cue the method depends on."),
                concept("target-conditioned-separation", "Target-conditioned separation", "A voice example, enrollment identity, or visual cue tells the separator which source to preserve rather than asking it to output every source.", "Conditioning can lock onto the wrong talker or encode identity without guaranteeing intelligible content."),
            ]),
            subtheme("echo-and-reconstruction", "Removing echo and repairing missing evidence", "When should the system cancel an unwanted copy and when must it reconstruct what is no longer observed?", [
                concept("acoustic-echo-cancellation", "Acoustic echo cancellation", "Use the known far-end playback signal to predict the speaker signal that returns through the room, then subtract that predicted copy.", "The loudspeaker path changes with movement and delay; an imperfect estimate can cancel near-end speech."),
                concept("packet-loss-concealment", "Packet-loss concealment", "When transmitted audio frames disappear, infer a short continuation from nearby waveform or speech structure so playback does not break.", "Short plausible continuation is not recovery of the original utterance and becomes unsafe over long gaps."),
                concept("perceptual-enhancement", "Perceptual enhancement", "Optimize what a listener can understand or tolerate rather than preserving every sample, using intelligibility or quality as the target.", "A perceptual score can hide distortions important for recognition, speaker identity, or forensic use."),
            ]),
        ],
    ),
    theme(
        "recognition-and-alignment", "From sound to words and structured speech",
        "How does a system turn a continuous acoustic stream into the words, boundaries, and disfluencies a user meant?",
        "Speech has no visible spaces between words, and pronunciation, speed, accent, noise, and hesitation vary even when the intended sentence is the same.",
        "Matching each sound to a fixed dictionary pronunciation or treating the utterance as already segmented fails on coarticulation, new words, and disfluency.",
        "Infer a sequence of linguistic units while allowing uncertainty about boundaries, pronunciation, context, and what should be preserved.",
        "A fluent transcript can be easier to read but less faithful to what was said, including omissions, hesitation, or uncertainty.",
        [
            subtheme("acoustic-unit-mapping", "Mapping continuous acoustics to linguistic units", "How can changing sound be assigned to phones, words, or tokens without visible boundaries?", [
                concept("acoustic-to-token", "Acoustic-to-token mapping", "The system scores candidate symbol sequences against the observed sound and chooses or represents alternatives rather than reading words directly from samples.", "The highest-scoring sequence may exploit dataset regularities instead of matching the actual speech."),
                concept("self-supervised-speech-units", "Learned speech units", "Predicting or grouping parts of unlabeled audio can provide reusable units before a task-specific word recognizer is trained.", "A useful pretraining prediction need not produce units aligned with words, phonemes, or human categories."),
                concept("pronunciation-variation", "Pronunciation variation", "The same word can have reductions, substitutions, or accent-specific realizations, so recognition must allow more than one acoustic path.", "Adding variants without evidence can increase confusions and may encode an accent as an error."),
            ]),
            subtheme("boundaries-and-sequence-structure", "Boundaries, timing, and sequence constraints", "How does the system decide where units begin, end, and depend on one another?", [
                concept("alignment", "Temporal alignment", "Align an audio timeline with words, phones, or labels so duration and position can be measured rather than treating the utterance as an unordered bag.", "Forced alignment assumes the transcript is correct and can conceal recognition errors."),
                concept("long-context-decoding", "Long-context decoding", "Use words and turns before and after a sound to resolve locally ambiguous acoustics, such as homophones or clipped endings.", "Context can override a rare but correct word, especially when the language model has a strong prior."),
                concept("disfluency-preservation", "Disfluency and event preservation", "Represent pauses, repetitions, repairs, laughter, and overlap when those events are part of the communication or the clinical signal.", "Removing them may improve readability while destroying evidence needed for conversation analysis or diagnosis."),
            ]),
            subtheme("adaptation-and-open-vocabulary", "Recognizing new speakers, domains, and words", "How can recognition remain useful when the test speech differs from training speech?", [
                concept("speaker-adaptation", "Speaker adaptation", "Adjust the acoustic or decoding assumptions to a talker's voice, speaking rate, or pronunciation using a small amount of evidence.", "Adaptation can overfit a short sample and degrade when the talker changes state or the enrollment is wrong."),
                concept("domain-and-context-biasing", "Domain and context biasing", "Use the meeting topic, contact list, or application vocabulary to raise plausible rare words without changing the audio itself.", "A biased vocabulary can turn uncertainty into confident but context-shaped substitutions."),
                concept("open-vocabulary-recognition", "Open-vocabulary recognition", "Handle names, code-switching, jargon, and newly encountered words without requiring a fixed closed list.", "Open vocabulary expands recall but makes spelling, segmentation, and evaluation less settled."),
            ]),
        ],
    ),
    theme(
        "meaning-and-interaction", "From spoken form to meaning and coordinated action",
        "What does an utterance mean here, and what should another participant do with it?",
        "The same words can request, question, joke, refuse, or warn depending on prosody, shared history, timing, and the surrounding situation.",
        "A transcript-only system treats words as the whole message and misses intent, reference, turn structure, and what is appropriate to do next.",
        "Combine linguistic content with speaker, discourse history, prosody, visual or environmental context, and an explicit action or response target.",
        "More context can resolve ambiguity but can also leak private information, over-interpret the speaker, or make a system confidently act on a wrong inference.",
        [
            subtheme("prosody-and-intent", "Prosody, emotion, and communicative intent", "What does timing, pitch, loudness, and voice quality add beyond the words?", [
                concept("prosodic-meaning", "Prosodic meaning", "Pitch movement, timing, stress, and pauses can mark questions, contrast, turn completion, urgency, or attitude.", "Prosody is language- and speaker-dependent; a pitch pattern is not a universal emotion label."),
                concept("paralinguistic-state", "Paralinguistic state", "Voice properties can provide clues about emotion, fatigue, engagement, or health that are not the literal linguistic content.", "A correlational acoustic cue is not proof of an internal state or a reliable diagnosis."),
                concept("intent-in-context", "Intent in context", "Infer what the speaker is trying to accomplish from words plus the situation and prior turns, then keep uncertainty when several intents fit.", "Intent labels often reflect annotator interpretation and may erase ambiguity or culturally different readings."),
            ]),
            subtheme("dialogue-and-turn-taking", "Conversation as joint timing", "How do participants know when to listen, speak, yield, repair, or overlap?", [
                concept("turn-boundary", "Turn-boundary prediction", "Predict whether a speaker is continuing, yielding, or likely to stop so a system can respond without cutting them off.", "A pause is not always a turn end; cultures, speakers, and task types change timing conventions."),
                concept("dialogue-state", "Dialogue state", "Track unresolved questions, commitments, entities, and prior actions so a response is connected to the conversation rather than only the last sentence.", "A stored state can be stale, incorrectly inferred, or sensitive, and the system may not know when to discard it."),
                concept("repair-and-clarification", "Repair and clarification", "When recognition or understanding is uncertain, ask a targeted question or offer alternatives instead of silently continuing.", "A clarification costs time and can burden users if uncertainty estimates are poorly calibrated."),
            ]),
            subtheme("grounding-and-action", "Connecting speech to people, objects, and actions", "How does a spoken description become a shared reference or an authorized action?", [
                concept("referential-grounding", "Referential grounding", "Use the scene, shared task, or prior mention to determine which object, person, or event a phrase denotes.", "Words alone may underdetermine the referent; a model can infer a plausible object without actually observing it."),
                concept("speech-act", "Speech act", "Distinguish information from a request, command, permission, or commitment because the same proposition can require different responses.", "Classifying an act does not grant authority to execute it."),
                concept("interactional-feedback", "Interactional feedback", "Let user corrections, confirmations, and response outcomes update the system's interpretation during the interaction.", "Feedback can be sparse, ambiguous, or shaped by users adapting to the system's mistakes."),
            ]),
        ],
    ),
    theme(
        "voice-generation-and-control", "Creating speech while keeping the right things fixed",
        "How can a system produce intelligible speech while controlling content, identity, timing, style, and naturalness separately?",
        "A useful synthetic voice must say the requested content, sound like the intended speaker or style, and remain understandable as it changes over time.",
        "Copying a recording or predicting samples directly entangles words with identity, pitch, rhythm, and recording conditions, making controlled change difficult.",
        "Represent or condition distinct factors, generate a time-consistent waveform or acoustic sequence, and evaluate each requested property separately.",
        "Factor separation is rarely perfect: changing identity can change content, style controls can sound artificial, and a plausible voice can be misused.",
        [
            subtheme("text-to-speech-and-content", "Turning language plans into audible speech", "How does a text or linguistic plan become a timed, pronounceable signal?", [
                concept("text-to-speech-planning", "Text-to-speech planning", "Choose pronunciation, durations, pitch targets, and acoustic details before or while producing the waveform so written content becomes speakable.", "Text does not specify one correct prosody, and a fluent output can still mispronounce names or sound unnatural."),
                concept("neural-vocoder", "Waveform synthesis", "Generate fine-grained samples conditioned on a coarser acoustic plan, reconstructing the periodic and noisy detail listeners hear as voice.", "Sample-level realism does not guarantee correct words, stable identity, or natural long-range timing."),
                concept("intelligibility-naturalness", "Intelligibility versus naturalness", "Treat ease of understanding and human-likeness as related but distinct targets that need separate tests.", "A single listener score can conflate content accuracy, recording quality, and preference."),
            ]),
            subtheme("voice-identity-and-conversion", "Changing who sounds like they are speaking", "How can voice identity change while the spoken message remains the same?", [
                concept("speaker-identity", "Speaker identity representation", "Capture stable voice traits that let a system preserve or imitate who is speaking across different words and sessions.", "A short recording can encode noise, emotion, or demographic stereotypes rather than stable identity."),
                concept("voice-conversion", "Voice conversion", "Transform the acoustic realization toward a target voice while trying to preserve linguistic timing and content.", "Conversion may leak source identity, distort pronunciation, or require target-speaker data unavailable in practice."),
                concept("zero-shot-voice", "Unseen-speaker synthesis", "Use a voice description or brief enrollment to synthesize a speaker not represented by a dedicated model.", "Similarity on a benchmark does not establish consent, identity security, or robustness to unusual voices."),
            ]),
            subtheme("prosody-and-interactive-control", "Controlling timing, style, and expression", "Which expressive choices should the user specify, and which should the system infer?", [
                concept("prosody-control", "Prosody control", "Set or predict pitch, duration, energy, and pauses so the same words can sound questioning, emphatic, calm, or urgent.", "Independent controls can conflict; expressive variation may change perceived meaning or naturalness."),
                concept("style-and-emotion-control", "Style and emotion control", "Condition generation on a speaking style or affective target while preserving the requested content.", "Emotion categories are culturally and contextually unstable, and a label may not describe what listeners perceive."),
                concept("interactive-latency", "Interactive generation latency", "Produce speech quickly enough for a conversation while preserving continuity and allowing interruption or correction.", "Low latency can require shorter context, lower quality, or speculative output that must later be repaired."),
            ]),
        ],
    ),
    theme(
        "people-variation-and-health", "Speakers as changing people, not nuisance variables",
        "How should speech systems represent differences between people and changes within one person?",
        "Voice depends on anatomy, age, health, emotion, language history, social setting, and equipment; these differences affect both communication and measurement.",
        "Treating variation as noise makes systems work best for a narrow population and can turn a health or identity signal into an unwanted demographic shortcut.",
        "Measure which variation is task-relevant, model it explicitly when appropriate, and test performance and meaning across people and conditions.",
        "A factor that helps prediction may be sensitive, confounded, or harmful to expose; personalization can improve access while increasing privacy risk.",
        [
            subtheme("speaker-characteristics", "Identity, age, gender, and speaking style", "Which voice differences should be preserved, normalized, or treated as evidence?", [
                concept("speaker-verification", "Speaker verification", "Decide whether two recordings plausibly came from the same person under channel, time, and content variation.", "Similarity scores are not identity proof and depend on enrollment quality, population, and decision threshold."),
                concept("age-and-development", "Age and developmental speech", "Children and older adults differ in anatomy, articulation, vocabulary, and interaction needs, so adult data is not a neutral reference.", "Age prediction or age normalization can encode stereotypes and may not address the actual recognition failure."),
                concept("style-and-state-variation", "Within-speaker state variation", "The same person's voice shifts with fatigue, emotion, health, audience, and speaking effort; robust systems must not confuse state with identity.", "There is no universal stable identity vector independent of context."),
            ]),
            subtheme("clinical-and-assistive-speech", "Speech as a health or access signal", "How can speech technology help when speaking or hearing itself is impaired or changing?", [
                concept("clinical-speech-marker", "Clinical speech marker", "Measure a reproducible speech property associated with a clinical condition or progression, while separating it from age, device, and language effects.", "Association with a diagnosis is not clinical validity, causation, or permission to make a medical decision."),
                concept("dysarthria-and-atypical-speech", "Atypical articulation and dysarthria", "Recognize or synthesize speech whose timing, precision, or coordination differs from training norms instead of treating it as mere noise.", "Small datasets and speaker-specific patterns make broad claims especially fragile."),
                concept("augmentative-communication", "Augmentative communication", "Use residual vocal, muscular, visual, or typed signals to help a person express intended language or control a device.", "A system should preserve the person's authorship and offer correction, not silently decide what they meant."),
            ]),
            subtheme("human-centered-evaluation", "Whether the system helps a real person", "What does success mean for the person using or affected by the speech system?", [
                concept("listener-effort", "Listener effort", "Measure how much concentration, repetition, or repair a listener needs, not just whether a word error count changed.", "Effort measures depend on task, listener experience, and presentation conditions."),
                concept("user-control-and-consent", "User control and consent", "Let speakers decide how their voice is recorded, adapted, generated, shared, or corrected, especially when identity is involved.", "A consent checkbox does not solve power imbalance, downstream copying, or inability to withdraw a trained model."),
                concept("accessibility-fit", "Accessibility fit", "Judge whether a system works within a person's actual device, environment, communication practice, and time constraints.", "A lab improvement can be irrelevant or harmful if setup, latency, or interaction burden is omitted."),
            ]),
        ],
    ),
    theme(
        "languages-accents-and-resources", "Many languages, accents, and unequal evidence",
        "How can speech technology serve people whose language or variety has little labeled data or little institutional support?",
        "Languages differ in sounds, writing systems, grammar, prosody, code-switching, and social meaning; data and tools are distributed unevenly.",
        "Scaling an English-centered recipe or translating labels assumes that all languages expose the same units, data, and errors.",
        "Share useful structure across languages while preserving language-specific distinctions, measuring who benefits, and making uncertainty visible where evidence is thin.",
        "Transfer can import pronunciation or cultural assumptions, and aggregate multilingual scores can hide severe failures in a small language or community.",
        [
            subtheme("multilingual-and-crosslingual", "Sharing structure across languages", "What can be shared, and what must remain language-specific?", [
                concept("crosslingual-transfer", "Cross-lingual transfer", "Reuse representations or training signals from one language to improve another when their speech structure overlaps.", "Transfer may favor high-resource languages and erase distinctions absent from the source language."),
                concept("language-identification", "Language and variety identification", "Determine which language or variety is being spoken so the appropriate recognizer or interaction policy can be selected.", "Closely related varieties and code-switching make a single label inadequate or politically loaded."),
                concept("code-switching", "Code-switching", "Handle a speaker moving between languages within an utterance, including pronunciation, grammar, and word-boundary changes.", "A monolingual metric can count appropriate switching as error and fail to define the intended transcript."),
            ]),
            subtheme("low-resource-and-data-creation", "Learning when labels and recordings are scarce", "How can a system improve without assuming a large clean labeled corpus?", [
                concept("self-training-and-pseudo-labels", "Self-training", "Use a model's predictions on unlabeled speech as additional training signals, ideally filtering or weighting uncertain labels.", "Errors can reinforce themselves and create a false appearance of data scale."),
                concept("speech-data-collection", "Speech data collection", "Design recording prompts, speakers, transcription, and consent so newly collected data covers the intended community and task.", "More hours do not fix biased sampling, poor transcripts, or a task definition that excludes natural speech."),
                concept("few-shot-adaptation", "Few-shot adaptation", "Adjust a model to a language, speaker, or domain from a small number of examples rather than retraining from scratch.", "Few examples may cover only one speaker or style and make variance look like progress."),
            ]),
            subtheme("accent-and-cultural-boundaries", "Accent, dialect, and cultural interpretation", "When is a difference a recognition problem, and when is it the system's narrow norm?", [
                concept("accent-robustness", "Accent robustness", "Maintain intended-word accuracy across pronunciation patterns that differ from the training majority.", "A single pooled error rate cannot show which accents fail or whether adaptation changes identity representation."),
                concept("dialect-and-variety", "Dialect and variety", "Treat grammar, vocabulary, pronunciation, and discourse conventions of a variety as part of the language, not merely deviations from a standard.", "Dialect labels can be contested and may conflate region, ethnicity, class, and speaker identity."),
                concept("cultural-meaning", "Cultural meaning", "Interpret politeness, indirectness, emotion, and conversational norms within the community that uses them.", "A label imported from another culture may be statistically convenient but semantically wrong."),
            ]),
        ],
    ),
    theme(
        "evaluation-deployment-and-consequence", "Evidence, practical systems, and consequences",
        "What does a result establish, under what conditions, and who is affected when the system leaves the paper?",
        "Speech systems are used through microphones, networks, interfaces, policies, and people; a benchmark number is only one observation of that whole chain.",
        "Reporting one average score on one dataset encourages the reader to treat a proxy as universal ability and ignores latency, failure recovery, privacy, and misuse.",
        "Align the evaluation with the real target, expose subgroup and condition variation, account for the full system boundary, and preserve an audit trail from evidence to claim.",
        "Broader evaluation costs time and data, but narrow evidence can create false confidence exactly where speech systems affect access, identity, or safety.",
        [
            subtheme("metrics-and-targets", "What a metric actually measures", "Which human or engineering property is the score standing in for?", [
                concept("word-error-versus-understanding", "Word error versus understanding", "A transcript edit distance counts substitutions, insertions, and deletions, but a small count is not automatically successful task understanding.", "A word metric can miss critical entity errors and can penalize harmless orthographic or dialect differences."),
                concept("quality-and-naturalness", "Quality and naturalness", "Listening ratings, preference tests, and signal measures estimate different aspects of whether generated or enhanced speech is acceptable.", "A score without listeners, conditions, and target definition cannot support a general quality claim."),
                concept("calibration-and-selective-use", "Calibration and selective use", "A system should know when its uncertainty is high enough to defer, ask, or show alternatives rather than making every output look certain.", "Calibration on a held-out sample does not guarantee safety under a new population or distribution."),
            ]),
            subtheme("robustness-and-system-boundary", "From model score to deployed behavior", "What changes when the model is placed in a real device and interaction loop?", [
                concept("distribution-shift", "Distribution shift", "Performance changes when speakers, microphones, rooms, languages, topics, or noise differ from training and test conditions.", "A named shift is not evidence of coverage; the shift must be measured and tied to the failure."),
                concept("latency-and-resource", "Latency and resource budget", "A system must meet timing, memory, energy, bandwidth, and hardware limits while preserving the property users need.", "A faster model may emit less context, reduce quality, or move cost into an unreported service."),
                concept("end-to-end-recovery", "End-to-end recovery", "Handle uncertainty through confirmation, correction, fallback, and logging so one recognition error does not become an irreversible action.", "A robust component is not an end-to-end safe system if downstream policy ignores its uncertainty."),
            ]),
            subtheme("privacy-security-and-accountability", "Voice data, identity, and social risk", "What can be inferred or done with speech beyond the immediate task?", [
                concept("voice-privacy", "Voice privacy", "Speech recordings reveal content and may reveal identity, health, location, emotion, or group membership, so collection and storage are part of the technical problem.", "Removing words does not necessarily remove speaker identity or sensitive acoustic information."),
                concept("spoofing-and-deepfake", "Spoofing and synthetic voice misuse", "A system must distinguish authorized speech from replayed or generated audio when identity or access depends on it.", "A detector trained on known generators can fail on unseen synthesis, replay channels, or an attacker who changes the interaction."),
                concept("auditability-and-contestability", "Auditability and contestability", "Keep enough provenance, uncertainty, and correction path for a person to understand and challenge a consequential speech-derived decision.", "A stored confidence number is not an explanation of what evidence drove the decision."),
            ]),
        ],
    ),
]

# These examples make membership testable during review.  A positive example
# names the observable object or research move that belongs; a negative example
# names a tempting neighboring case that does not.  They are conceptual rules,
# not claims that the corpus contains each example.
CONCEPT_EXAMPLES = {
    "periodic-source": ("A study measures vocal-fold pulse timing or harmonic structure in voiced vowels.", "A study models only a microphone's frequency response with no source or phonation question."),
    "vocal-tract-filter": ("A study links tongue or lip geometry to vowel resonances or spectral peaks.", "A study predicts words from text without modeling how the tract shapes sound."),
    "articulatory-coordination": ("A study measures overlapping lip, tongue, jaw, or laryngeal gestures over time.", "A study treats each phoneme as an isolated label with no timing or movement evidence."),
    "windowed-spectrum": ("A spectrogram or short-time Fourier representation tracks local frequency content.", "A long-term average spectrum with no time-local measurement is not a windowed account."),
    "multi-resolution-signal": ("A method combines short windows for closures with longer windows for intonation or rhythm.", "Adding multiple neural layers without showing distinct time scales is not itself multi-resolution analysis."),
    "sampling-and-quantization": ("A study analyzes sample rate, bit depth, clipping, or quantization noise as information limits.", "A model that merely uses digital audio but never examines discretization does not instantiate this concept."),
    "reverberant-mixture": ("A method separates direct speech from delayed room reflections or models room impulse responses.", "Stationary additive microphone hiss with no room-delay structure is not reverberant mixing."),
    "microphone-channel": ("A system corrects frequency coloration, clipping, bandwidth, or device-specific transmission effects.", "A speaker adaptation method that never observes a recording channel is not channel modeling."),
    "non-airborne-sensing": ("Speech is inferred from neck vibration, ultrasound, radar, or another non-airborne sensor.", "Ordinary far-field microphone speech, even if noisy, is not non-airborne sensing."),
    "spectral-mask": ("A system estimates a time-frequency mask and attenuates bins assigned to noise.", "A waveform denoiser with no time-frequency assignment is not necessarily masking."),
    "speech-prior-denoising": ("A learned clean-speech prior reconstructs plausible speech where noise obscures the waveform.", "A fixed notch filter that uses no speech structure is not a speech prior."),
    "nonstationary-noise": ("The interference changes rapidly or contains competing speech, feedback, or transient events.", "A single fixed broadband noise condition does not establish nonstationary-noise handling."),
    "blind-source-separation": ("Several hidden signals are inferred from their mixture without isolated target audio at test time.", "A target voice embedding supplied at test time makes the task target-conditioned rather than blind."),
    "spatial-filtering": ("Microphone-array direction or spatial covariance is used to reinforce one location.", "A single-channel spectral model with no spatial input is not spatial filtering."),
    "target-conditioned-separation": ("An enrollment voice, visual cue, or target example selects which speaker to retain.", "Separating every source without a target condition is not target-conditioned separation."),
    "acoustic-echo-cancellation": ("Known loudspeaker playback is used to estimate and subtract its reflected copy from microphone input.", "Removing unrelated background noise without a playback reference is not echo cancellation."),
    "packet-loss-concealment": ("Missing transmitted frames are filled using neighboring waveform or speech continuity.", "Denoising a complete recording is not packet-loss concealment."),
    "perceptual-enhancement": ("Enhancement is optimized or judged by intelligibility, listener quality, or perceptual acceptability.", "A lower sample MSE alone is not perceptual enhancement evidence."),
    "acoustic-to-token": ("A continuous acoustic sequence is scored against phones, words, or discrete recognition tokens.", "Text-only language modeling with no acoustic input is not acoustic-to-token mapping."),
    "self-supervised-speech-units": ("Unlabeled speech predicts masked or neighboring content to create reusable acoustic representations.", "A supervised classifier trained only on labeled words is not self-supervised unit learning."),
    "pronunciation-variation": ("Recognition explicitly permits reductions, substitutions, accents, or multiple pronunciations of a word.", "Adding a new vocabulary item without pronunciation variation is not this concept."),
    "alignment": ("Words, phones, or labels are assigned positions and durations on an audio timeline.", "An utterance-level class with no temporal correspondence is not alignment."),
    "long-context-decoding": ("Earlier or later words and turns resolve an acoustically ambiguous local segment.", "A frame-local classifier that never uses surrounding context is not long-context decoding."),
    "disfluency-preservation": ("Pauses, repetitions, repairs, laughter, or overlap are retained as output events.", "Cleaning a transcript by deleting all disfluencies is the neighboring failure, not preservation."),
    "speaker-adaptation": ("A small enrollment sample changes acoustic or decoding assumptions for a particular talker.", "A single population-wide model with no speaker evidence is not adaptation."),
    "domain-and-context-biasing": ("A meeting topic, contact list, or application vocabulary changes rare-word decoding.", "A generic language model with no task context is not contextual biasing."),
    "open-vocabulary-recognition": ("The recognizer handles names, jargon, code-switching, or newly encountered words outside a fixed list.", "A closed command grammar with a fixed word list is not open-vocabulary recognition."),
    "prosodic-meaning": ("Pitch, stress, rhythm, or pauses change whether an utterance sounds like a question, contrast, or turn completion.", "A lexical-only text classifier with no prosodic evidence is not prosodic meaning analysis."),
    "paralinguistic-state": ("Acoustic voice changes are used as clues about emotion, fatigue, engagement, or health.", "A diagnosis asserted from a transcript alone is not acoustic paralinguistic-state evidence."),
    "intent-in-context": ("Words, prosody, and discourse situation jointly determine whether a speaker requests, warns, jokes, or refuses.", "Assigning intent from isolated keywords alone is not context-sensitive intent inference."),
    "turn-boundary": ("The system predicts whether a speaker will continue, yield, or stop before responding.", "Detecting sentence punctuation after the turn is complete is not turn-boundary prediction."),
    "dialogue-state": ("The system tracks unresolved questions, commitments, entities, and prior actions across turns.", "A response based only on the last utterance is not dialogue-state tracking."),
    "repair-and-clarification": ("Uncertainty triggers a targeted question, confirmation, or alternative instead of silent continuation.", "Returning a confident guess without a correction path is not repair."),
    "referential-grounding": ("A phrase such as 'that cup' is linked to an object in the shared scene or prior discourse.", "Choosing a likely object without scene or discourse evidence is not grounding."),
    "speech-act": ("The system distinguishes an assertion from a request, command, permission, or commitment.", "Topic classification without an action or authority interpretation is not speech-act analysis."),
    "interactional-feedback": ("User correction or response outcome updates what the system believes the user meant.", "Logging a prediction without using subsequent interaction is not feedback."),
    "text-to-speech-planning": ("Text is converted into pronunciation, duration, pitch, and acoustic plans before waveform generation.", "A waveform vocoder receiving a complete acoustic plan is not itself text-to-speech planning."),
    "neural-vocoder": ("A model generates fine waveform samples conditioned on a lower-rate acoustic representation.", "A text-to-text model with no waveform synthesis is not a neural vocoder."),
    "intelligibility-naturalness": ("Separate tests ask whether words are understood and whether the voice sounds human-like.", "One unqualified quality score cannot establish both intelligibility and naturalness."),
    "speaker-identity": ("A representation preserves or imitates a person's stable vocal characteristics across words.", "A recording-specific noise signature mistaken for identity is not a valid identity representation."),
    "voice-conversion": ("The acoustic realization moves toward a target speaker while the source linguistic content remains.", "Changing text content without preserving the source message is not voice conversion."),
    "zero-shot-voice": ("A brief enrollment or description synthesizes a speaker without a dedicated per-speaker model.", "A model trained and tested only on speakers seen during training is not zero-shot voice."),
    "prosody-control": ("A user or model sets pitch, timing, energy, or pauses while keeping words fixed.", "Changing speaker identity without an explicit timing or melody control is not prosody control."),
    "style-and-emotion-control": ("A generation system is conditioned on a style or affect target while preserving content.", "A classifier that only labels emotion but generates nothing is not style control."),
    "interactive-latency": ("A voice system speaks quickly, permits interruption, and responds within conversational timing.", "Offline synthesis with no response-time or interruption constraint is not interactive latency work."),
    "speaker-verification": ("Two recordings are compared to decide whether they came from the same person.", "Predicting age or emotion without comparing identity is not speaker verification."),
    "age-and-development": ("A system models children or older adults whose anatomy, language, or interaction differs from adults.", "A generic adult corpus with age omitted is not age/development analysis."),
    "style-and-state-variation": ("The same speaker is measured across fatigue, emotion, effort, audience, or health states.", "Differences only between unrelated speakers are not within-speaker state variation."),
    "clinical-speech-marker": ("A reproducible pause, articulation, or voice measure is tested against a clinical condition or severity scale.", "A speech feature correlated with a generic class but never tied to a clinical target is not a clinical marker."),
    "dysarthria-and-atypical-speech": ("Recognition or synthesis explicitly handles atypical timing, precision, or coordination.", "Treating all low-confidence speech as atypical without a speaker or disorder target is not this concept."),
    "augmentative-communication": ("Residual vocal, muscular, visual, or typed signals are turned into a person's intended communication.", "A general speech recognizer for fluent speakers is not augmentative communication."),
    "listener-effort": ("Listeners' concentration, repetition, or effort is measured under a speech condition.", "WER alone, with no listener task or report, is not listener-effort evidence."),
    "user-control-and-consent": ("A system gives people control over recording, adaptation, generation, sharing, or correction of their voice.", "A privacy statement with no user choice or withdrawal path is not demonstrated control."),
    "accessibility-fit": ("Evaluation includes the person's actual device, environment, communication practice, setup burden, or timing needs.", "A clean laboratory score with no user or deployment constraint is not accessibility fit."),
    "crosslingual-transfer": ("Training signals or representations from one language improve another language while measuring what is lost.", "Translating an English label without cross-language speech evidence is not cross-lingual transfer."),
    "language-identification": ("The system selects a language or variety from spoken input before choosing a downstream policy.", "Classifying topics or speakers without language choice is not language identification."),
    "code-switching": ("A single utterance changes language and the recognizer preserves its words, boundaries, and pronunciation shifts.", "Separate monolingual recordings are not code-switching."),
    "self-training-and-pseudo-labels": ("A model labels unlabeled speech and filtered predictions become new training examples.", "Adding more human-transcribed data is not self-training."),
    "speech-data-collection": ("A study designs prompts, speakers, transcripts, permissions, and sampling for a new speech corpus.", "Using an existing benchmark without examining its collection is not data-collection analysis."),
    "few-shot-adaptation": ("A model changes to a new language, speaker, or domain from only a small number of examples.", "A full retraining run on a large new corpus is not few-shot adaptation."),
    "accent-robustness": ("Intended-word accuracy is measured across pronunciation patterns outside the training majority.", "A pooled score with no accent or variety breakdown is not evidence of accent robustness."),
    "dialect-and-variety": ("A study treats a community's pronunciation, grammar, vocabulary, or discourse as a language variety.", "Calling every deviation from a standard an error is the boundary failure, not dialect analysis."),
    "cultural-meaning": ("Interpretation is evaluated against community-specific politeness, indirectness, emotion, or conversational norms.", "Importing a label from another culture without local interpretation is not cultural-meaning analysis."),
    "word-error-versus-understanding": ("A paper compares transcript edit distance with whether a person can complete the intended task or recover critical entities.", "Reporting WER and calling it understanding without a task measure is not this concept."),
    "quality-and-naturalness": ("Listeners or a defined signal target judge acceptability, preference, naturalness, or intelligibility under stated conditions.", "An unexplained aggregate score with no target or listening condition is not quality evidence."),
    "calibration-and-selective-use": ("A system defers, asks, or shows alternatives when confidence does not match observed correctness.", "A softmax score reported without reliability or selective behavior is not calibration."),
    "distribution-shift": ("The same system is tested across new speakers, rooms, microphones, languages, topics, or noise conditions.", "Calling a dataset diverse without measuring a train-test change is not distribution-shift evidence."),
    "latency-and-resource": ("A paper measures response time, memory, energy, bandwidth, or compute under a deployment constraint.", "A smaller parameter count with no resource or timing measurement is not a deployment-budget result."),
    "end-to-end-recovery": ("A recognition error leads to confirmation, correction, fallback, or logging instead of irreversible action.", "Improving one model component without testing downstream recovery is not end-to-end recovery."),
    "voice-privacy": ("A system limits or audits what identity, health, location, or content can be inferred from recorded speech.", "Deleting the transcript while retaining identifiable acoustic recordings is not voice privacy."),
    "spoofing-and-deepfake": ("A detector tests replayed or generated speech against an identity or access decision, including unseen attacks.", "A normal speech classifier with no adversarial or synthetic-audio threat model is not spoofing analysis."),
    "auditability-and-contestability": ("A consequential speech-derived decision preserves provenance, uncertainty, and a way for a person to challenge it.", "A confidence number without evidence trace or appeal path is not auditability."),
}

for _theme in TAXONOMY:
    for _subtheme in _theme["subthemes"]:
        for _concept in _subtheme["concepts"]:
            positive, negative = CONCEPT_EXAMPLES[_concept["id"]]
            _concept["positive_example"] = positive
            _concept["negative_example"] = negative
            _concept["membership_evidence_rule"] = "D2 abstract evidence must name the spoken-speech object and conceptual pressure; D3 full-paper evidence must additionally support the mechanism and evaluation object."


def flatten(taxonomy):
    rows = []
    for t in taxonomy:
        for s in t["subthemes"]:
            for c in s["concepts"]:
                rows.append({
                    "theme_id": t["id"],
                    "theme_name": t["name"],
                    "subtheme_id": s["id"],
                    "subtheme_name": s["name"],
                    **c,
                })
    return rows


def main():
    DATA.mkdir(exist_ok=True)
    REPORTS.mkdir(exist_ok=True)
    concepts = flatten(TAXONOMY)
    document = {
        "schema_version": 1,
        "taxonomy_status": "analyst-authored-first-principles-framework",
        "claim_boundary": "This taxonomy is a conceptual scaffold for semantic review, not an official conference classification or a prevalence estimate.",
        "source_boundary": "Theme and concept definitions are analyst-authored. Paper membership must be established separately from title/abstract/full-paper evidence.",
        "membership_evidence_rule": "D1 title-only records may propose candidates but cannot establish conceptual membership; D2 abstract evidence can establish a bounded speech object and problem; D3 full-paper evidence is required for mechanism and evaluation claims.",
        "theme_count": len(TAXONOMY),
        "subtheme_count": sum(len(t["subthemes"]) for t in TAXONOMY),
        "concept_count": len(concepts),
        "themes": TAXONOMY,
    }
    (DATA / "speech-first-principles-taxonomy.json").write_text(json.dumps(document, indent=2, ensure_ascii=False) + "\n")

    out = ["# Speech first-principles conceptual taxonomy", "", document["claim_boundary"], "", "This is the semantic contract for the deep atlas. The old keyword map only discovers candidates.", ""]
    for t in TAXONOMY:
        out += [f"## {t['name']}", "", f"**Question:** {t['question']}", "", f"**Ordinary problem:** {t['ordinary_problem']}", "", f"**Why the naive approach fails:** {t['naive_failure']}", "", f"**Recurring conceptual move:** {t['recurring_move']}", "", f"**Tradeoff/boundary:** {t['tradeoff']}", ""]
        for s in t["subthemes"]:
            out += [f"### {s['name']}", "", f"**Question:** {s['question']}", ""]
            for c in s["concepts"]:
                out += [f"#### {c['name']}", "", c["definition"], "", f"**Positive membership example:** {c['positive_example']}", "", f"**Negative/boundary example:** {c['negative_example']}", "", f"**Boundary:** {c['boundary']}", "", f"**Evidence rule:** {c['membership_evidence_rule']}", ""]
    (REPORTS / "SPEECH_FIRST_PRINCIPLES_TAXONOMY.md").write_text("\n".join(out))
    print(f"themes={document['theme_count']} subthemes={document['subtheme_count']} concepts={document['concept_count']}")


if __name__ == "__main__":
    main()
