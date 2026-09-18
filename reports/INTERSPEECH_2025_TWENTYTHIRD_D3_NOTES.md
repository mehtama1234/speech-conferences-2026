# INTERSPEECH 2025 twenty-third-pass full-paper notes

Eight official-PDF readings deepen physical measurement, interaction, evaluation, and contextual recognition. Results are author-reported and not independently reproduced.

## 1. source-filter-production

**Paper:** [Speech Reduction in French: The Relationship Between Vowel Space and Articulation Dynamics](https://www.isca-archive.org/interspeech_2025/bodur25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `a1acaa7ac82fd11ba2f0fa8e61e5cc297585c16d7d72517f359701d2a4dd62a1`; full text captured.

- **Ordinary problem:** Spontaneous speech becomes shorter and less distinct when people speak quickly, so a system or scientist must connect timing to the shape of the vowel space.
- **Why hard:** Reduction is not one event: speakers can centralize vowels, compress time, or do both, and a global measure may hide that interaction.
- **Naive attempt:** Use articulation rate or vowel-space size alone as a complete explanation.
- **Central move:** Model spatial vowel distinctiveness and temporal rate together and test whether their interaction predicts non-lexicalized reductions.
- **Mechanism:** French spontaneous speech is measured with pVSA, VDI, articulation rate, and temporally compressed speech zones.
- **Conceptual structure:** Regression separates spatial predictors, temporal predictors, and their interaction rather than treating one acoustic number as the cause.
- **What paper reports:** Smaller vowel space predicts more reduction only when articulation rate is included; rate is the strongest predictor and VDI is not significant.
- **Limits:** The French speakers, spontaneous tasks, reduction definition, and acoustic measures bound the result; other languages and conversational settings remain open.

## 2. time-frequency-measurement

**Paper:** [Influence of Proficiency and L2 Experience on Dynamic Spectral Cue Utilization in L2 Vowel Perception and Production](https://www.isca-archive.org/interspeech_2025/bakkouche25b_interspeech.html)
**Evidence:** D3; PDF SHA-256 `2fe715ce3cb6a5756941f5fbaa1adf3327c7bd596ee88b33f769c6c426283e0d`; full text captured.

- **Ordinary problem:** A learner must hear and produce an unfamiliar vowel contrast whose important evidence changes over time rather than staying at one frequency point.
- **Why hard:** Similar categories overlap, and static formant snapshots miss the movement that distinguishes them.
- **Naive attempt:** Measure one midpoint formant and treat perception and production as separate abilities.
- **Central move:** Track vowel-inherent spectral change across the vowel and compare perception-production alignment with proficiency and immersion experience.
- **Mechanism:** Polish learners produce and perceive English /e-æ/ and /i-I/; dynamic formant movement is measured over vowel duration.
- **Conceptual structure:** Formant trajectories are time-varying objects; accuracy and production consistency test whether the moving cue is learned.
- **What paper reports:** Advanced learners improve, especially for /i-I/; formant movement increases with proficiency, while length of residence is not significant.
- **Limits:** The learner group, contrasts, language experience, and measurements bound the result; other L1s and natural interaction need separate evidence.

## 3. echo-and-reconstruction

**Paper:** [Efficient Neural and Numerical Methods for High-QualityOnline Speech Spectrogram Inversion via Gradient Theorem](https://www.isca-archive.org/interspeech_2025/fernandez25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `a767c10d45a8f47617a27f4e14e014c4d8a27f3a2c9bf5d2ae1986e7d83cf083`; full text captured.

- **Ordinary problem:** A streaming system must reconstruct an audio waveform from a magnitude spectrogram without paying a large compute or latency cost.
- **Why hard:** Magnitude says how much energy is present but not the phase relationships needed to make the waveform line up in time.
- **Naive attempt:** Use a large neural inverse model or solve the reconstruction problem with a generic expensive least-squares routine.
- **Central move:** Predict phase derivatives with a tiny network and exploit the tridiagonal positive-semidefinite structure of the resulting least-squares system.
- **Mechanism:** The online inversion model uses 8k parameters, adds at most one hop of latency, and applies a linear-complexity solver after predicting derivative information.
- **Conceptual structure:** Phase reconstruction becomes a structured inverse problem; the solver uses matrix structure instead of treating every coefficient as unrelated.
- **What paper reports:** The paper reports a 30x smaller network, a further halving of neural cost with one-hop latency, and orders-of-magnitude solver speedup while retaining quality.
- **Limits:** Spectrogram settings, audio domain, latency definition, and samples bound the claim; listening tests and hardware deployment remain separate checks.

## 4. dialogue-and-turn-taking

**Paper:** [Multimodal Dynamics of Hand Gestures and Pauses in Multiparty Interactions](https://www.isca-archive.org/interspeech_2025/charuau25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `3a3443380c1af1e2ab7b900fd8b5fbe1eaa97d04d268bb5746ced9bfcaf77daa`; full text captured.

- **Ordinary problem:** In a multiparty conversation, gestures and pauses should be understood as timed coordination rather than unrelated events.
- **Why hard:** A pause can occur within one speaker's turn or between speakers, and gesture timing may reflect planning, turn exchange, or social behavior.
- **Naive attempt:** Count gestures and pauses independently or align every gesture only to the nearest word.
- **Central move:** Measure gesture category, pause type, duration, and onset/offset timing together in annotated audiovisual dialogues.
- **Mechanism:** MULTISIMO recordings provide multiparty dialogue annotations; distributions and temporal relations are compared for within- and between-speaker pauses.
- **Conceptual structure:** The unit of analysis is a timed relation among gesture, pause, and speaker turn; duration and onset timing carry different information.
- **What paper reports:** Self-adaptors align with longer pauses, utterance-final syntax shortens pauses, and most gestured pauses occur within utterances.
- **Limits:** Corpus annotation, participant population, gesture categories, and observational design bound the result; causal cognitive interpretations remain hypotheses.

## 5. metrics-and-targets

**Paper:** [Comparison-Based Automatic Evaluation for Meeting Summarization](https://www.isca-archive.org/interspeech_2025/gong25c_interspeech.html)
**Evidence:** D3; PDF SHA-256 `7564415e510871fda9e1217dc49c8edd4176da76020fb95b2ffde3d57c94cb83`; full text captured.

- **Ordinary problem:** A meeting summarizer should be judged for preserving important facts and staying concise even when no reference summary exists.
- **Why hard:** Long meetings contain many valid summaries, and reference overlap rewards wording rather than whether the important decisions survived.
- **Naive attempt:** Compare generated text with one reference using lexical similarity or ask an LLM for one unstructured score.
- **Central move:** Use fact alignment and comparison-based judging, then rank systems with an Elo procedure instead of requiring a reference summary.
- **Mechanism:** CREAM uses reasoning traces and key-fact alignment to compare meeting summaries for completeness and conciseness without references.
- **Conceptual structure:** Fact coverage and brevity become comparison evidence; Elo aggregates pairwise preferences while avoiding a false absolute scale.
- **What paper reports:** The paper presents a reference-free evaluation framework for meeting summarization and reports its ability to rank systems/prompts.
- **Limits:** Facts, judge prompts, meeting domain, and pairwise comparison protocol bound the result; human validation and adversarial summaries remain open.

## 6. human-centered-evaluation

**Paper:** [Unifying Listener Scoring Scales: Comparison Learning Framework for Speech Quality Assessment and Continuous Speech Emotion Recognition](https://www.isca-archive.org/interspeech_2025/hu25l_interspeech.html)
**Evidence:** D3; PDF SHA-256 `f5d5ac83a5c1b084f927c8cc9000990691f3048a4647542e8e321adbf6aa6536`; full text captured.

- **Ordinary problem:** A speech-quality or emotion model should account for the fact that listeners use different personal rating scales.
- **Why hard:** Averaging ordinal ratings can invent distances and erase systematic listener differences.
- **Naive attempt:** Average all ratings into one target and train a model to reproduce that mean.
- **Central move:** Learn a unified listener scale from pairwise comparisons so the ordering of utterances is preserved without assuming numeric distances.
- **Mechanism:** The method is evaluated on speech quality assessment and continuous emotion recognition, comparing a unified comparison-based scale with mean-listener and multi-scale approaches.
- **Conceptual structure:** Pairwise comparison models order utterances; the central mathematical choice is to preserve ordinal relationships rather than average incompatible numbers.
- **What paper reports:** The paper reports improved prediction performance and robustness on both tasks.
- **Limits:** Listener panels, rating prompts, comparison construction, and datasets bound the result; agreement and usefulness for new listener populations remain open.

## 7. prosody-and-interactive-control

**Paper:** [Prediction of listening effort ratings for habitual and clear-Lombard speech presented in noise](https://www.isca-archive.org/interspeech_2025/janse25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `05c09b7f5900487fb41579462d00bea9c765dfb02fb88fd7ef5b979719178f47`; full text captured.

- **Ordinary problem:** A system should predict how hard it is to listen to speech in noise, not merely whether the speech is technically intelligible.
- **Why hard:** Listeners can reconstruct words by effort even when masking leaves only intermittent speech glimpses, and speaking style changes those glimpses.
- **Naive attempt:** Use one global SNR or intelligibility score as a proxy for effort.
- **Central move:** Measure high-energy speech glimpses and add speaking-style cues such as pitch range and articulation rate to predict listener effort.
- **Mechanism:** HEGP is computed for habitual and clear-Lombard speech in noise; listening-effort ratings are modeled with spectral balance, F0, and rate measures.
- **Conceptual structure:** The target is subjective effort, while HEGP is a release-from-masking proxy; regression tests whether style explains residual variance.
- **What paper reports:** HEGP predicts effort similarly across styles; wider F0 range and slower articulation are associated with lower effort, especially for habitual speech.
- **Limits:** Noise, listener ratings, speech styles, and HEGP definition bound the result; individual strategy and real device conditions remain open.

## 8. adaptation-and-open-vocabulary

**Paper:** [Ranking and Selection of Bias Words for Contextual Bias Speech Recognition](https://www.isca-archive.org/interspeech_2025/hou25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `01639f2a96ebc2d528d87c274db8f2a381d31a72af55afea82a3cb507371dbb4`; full text captured.

- **Ordinary problem:** Contextual ASR should recognize a large list of names or domain words without being distracted by irrelevant entries.
- **Why hard:** A large bias list creates search competition and homophone errors, so adding every candidate can hurt the very words it is meant to help.
- **Naive attempt:** Pass the full list to decoding or choose entries by frequency alone.
- **Central move:** Train a scorer that ranks and selects bias words from an NER-derived list before contextual Whisper decoding.
- **Mechanism:** A bias-word ranking network selects candidates from the IS21 list and evaluates contextual Whisper on LibriSpeech.
- **Conceptual structure:** Selection turns a huge candidate set into a focused conditional recognition problem; biased WER measures the targeted words while overall WER checks collateral damage.
- **What paper reports:** The paper reports more than 40% relative reduction in biased WER from ranking and selection.
- **Limits:** NER list, LibriSpeech, Whisper context mechanism, and bias-word definition bound the result; new domains and errors in entity extraction remain open.

