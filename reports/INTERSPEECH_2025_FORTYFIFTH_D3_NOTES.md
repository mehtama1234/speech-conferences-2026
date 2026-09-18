# INTERSPEECH 2025 forty-fifth-pass full-paper notes

Eight official-PDF readings deepen speech-model security, physiological inference, temporal evaluation, dialect change, emotion-data design, lyric structure, noisy coding, and multilingual cue weighting.

## 1. privacy-security-and-accountability

**Paper:** [Defending Speech-enabled LLMs Against Adversarial Jailbreak Threats](https://www.isca-archive.org/interspeech_2025/alexos25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `419d1d99bdb3f6c7e3d8c08f51bbe8d820235771da40ddfce7724f8cfa900b69`; full text captured.

- **Ordinary problem:** A speech-enabled language model can be tricked into producing a harmful answer even when its text safety training appears strong.
- **Why hard:** Speech adds an attack surface: an adversarial spoken query must survive speech recognition and still steer the language model, while defenses need scarce harmful speech examples.
- **Naive attempt:** Apply ordinary text safety tuning and assume the speech front end does not change the jailbreak problem.
- **Central move:** Train with synthesized harmful and benign speech queries and test against strong white-box attacks across two model sizes and data configurations.
- **Mechanism:** The paper develops adversarial-training methods tailored to speech-enabled language models.
- **Conceptual structure:** Safety is a path property: the audio, recognition, and language-model stages jointly determine whether a harmful request is blocked, so safety examples must cover the spoken route.
- **What paper reports:** The paper reports relative safety gains of 45%–300% in its tested settings using four hours of harmful speech with 150 hours of benign speech.
- **Limits:** The two models, synthesized data, attack family, safety measure, and training recipe bound the result; robustness to unseen speakers, attacks, languages, and real-world misuse remains open.

## 2. clinical-and-assistive-speech

**Paper:** [Heart Rate as a Proxy Measure to Assess Human Confidence in Spoken Speech](https://www.isca-archive.org/interspeech_2025/battula25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `3bb63c026964e22d9e42ffc309f61e6c0ac8bde4c5ea12e07bfea8b728a5af85`; full text captured.

- **Ordinary problem:** A person’s confidence is useful to assess in an interview, but the relevant physiological signal is normally hard to collect without a sensor.
- **Why hard:** The proposed chain estimates breathing from speech, extracts heart-rate variation with ICA, and maps that estimate to confidence; each step can add error or reflect demographic and situational differences.
- **Naive attempt:** Treat confidence as a direct acoustic class or require a wearable heart-rate sensor for every interaction.
- **Central move:** Infer heart rate from speech-derived breathing patterns, then examine whether the inferred heart rate separates confident and non-confident speakers.
- **Mechanism:** The paper presents a three-stage speech-to-breathing-to-heart-rate approach for confidence analysis.
- **Conceptual structure:** The key conceptual move is indirect sensing: speech is used as a window onto a bodily rhythm, but the inferred physiology is not the same thing as confidence itself.
- **What paper reports:** The paper reports that confident speakers had an average heart rate about 10 beats per minute lower in its tested data.
- **Limits:** The datasets, Indian demographic, 41-speaker collection, clinical and wearable references, confidence labels, and unreported general accuracy bound the claim; correlation is not a validated psychological diagnosis.

## 3. metrics-and-targets

**Paper:** [Benchmarking and Confidence Evaluation of LALMs For Temporal Reasoning](https://www.isca-archive.org/interspeech_2025/bhattacharya25b_interspeech.html)
**Evidence:** D3; PDF SHA-256 `6752a96fca775cf2a4c7e927a22c683332091f52227799fafc053b035fe7c5a7`; full text captured.

- **Ordinary problem:** An audio language model may answer a temporal question correctly for the wrong reasons or change its answer when the same content is phrased equivalently.
- **Why hard:** Accuracy alone cannot show whether a model tracks time relations or knows when its answer is unstable; speech duration and temporal ordering create failures not visible in ordinary classification tests.
- **Naive attempt:** Report one accuracy number on a fixed question set and treat it as reasoning competence and confidence.
- **Central move:** Build the TREA temporal-reasoning dataset, benchmark audio language models against people, and measure uncertainty through invariance to semantically identical perturbations.
- **Mechanism:** The paper introduces Temporal Reasoning Evaluation of Audio and an uncertainty metric for large audio language models.
- **Conceptual structure:** Evaluation must separate getting the answer right from behaving consistently under meaning-preserving changes; these are different properties and can move in opposite directions.
- **What paper reports:** The paper reports that tested open-source models lagged human performance and that accuracy and perturbation-based uncertainty were not necessarily correlated.
- **Limits:** The dataset, perturbations, models, human comparison, and temporal tasks bound conclusions; invariance is one operational uncertainty test, not a complete account of confidence.

## 4. accent-and-cultural-boundaries

**Paper:** [Agent-based modelling, sound change, and metaphony in Southern Italian varieties of Italo-Romance.](https://www.isca-archive.org/interspeech_2025/bressensdorf25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `a143b5b14c9c14d14b57ab479d19eb511be05f1d0e9b0f1df45f9f7cb8c3960d`; full text captured.

- **Ordinary problem:** When speakers of two dialects meet, a sound change can spread unevenly: a conservative dialect may move toward an innovative one, changing how grammatical information is pronounced.
- **Why hard:** The change is both social and physical: speakers remember variable signals, categories can emerge gradually, and inflectional cues can move between suffixes and stem vowels.
- **Naive attempt:** Treat dialect contact as a fixed label difference or assume both communities shift symmetrically toward an average.
- **Central move:** Initialize an interactive phonetic agent model with real speech from two Southern Italian varieties and simulate metaphony, then compare diphthongization and categorical contrasts.
- **Mechanism:** The paper tests an agent-based model of dialect contact and morpho-phonological sound change.
- **Conceptual structure:** A dialect is not a static inventory: production is repeatedly updated through perceptual memory and interaction, allowing social contact to reshape acoustic categories over time.
- **What paper reports:** The reported results provide support for an asymmetric shift toward the innovative dialect and are consistent with feedback models of sound change.
- **Limits:** The two dialects, 54 speakers collapsed to 13 agents, selected words, F1 trajectory representation, and model assumptions limit generalization to other communities or changes.

## 5. low-resource-and-data-creation

**Paper:** [EmoDB 2.0: A Database of Emotional Speech in a World that is not Black or White but Grey](https://www.isca-archive.org/interspeech_2025/burkhardt25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `41aa00e673d7957c865344ff0dcc41a89d1de020b3a234a36d554baa3e6bf825`; full text captured.

- **Ordinary problem:** An emotion database becomes more useful when it preserves ambiguous judgments and records how natural the acted speech sounds, rather than discarding every item without strong agreement.
- **Why hard:** Emotion labels are perceptions with disagreement, and glottal behavior may contain information that ordinary audio features miss; a clean majority label can hide meaningful uncertainty.
- **Naive attempt:** Keep only samples with high rater agreement and treat one categorical emotion label as ground truth.
- **Central move:** Extend Berlin EmoDB with previously omitted ambiguous samples, glottograms, and perceived-naturalness labels, then test their value in preliminary classifiers.
- **Mechanism:** The paper extends the Berlin Database of Emotional Speech with ambiguity, glottograms, and naturalness information.
- **Conceptual structure:** Dataset construction is part of the scientific model: disagreement and phonation measurements expose how an emotion label is produced and where it is uncertain.
- **What paper reports:** The paper reports an 8.1% UAR improvement for an SVM when glottogram information is incorporated in its preliminary study.
- **Limits:** The acted German corpus, old recording conditions, rater thresholds, classifier, and preliminary evaluation bound the result; improved classification does not establish better emotion understanding.

## 6. text-to-speech-and-content

**Paper:** [Song Form-aware Full-Song Text-to-Lyrics Generation with Multi-Level Granularity Syllable Count Control](https://www.isca-archive.org/interspeech_2025/chae25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `8d7a8f40fd501d1c207c594ba4f7b056d0c009695222ddc9b7785661692f6410`; full text captured.

- **Ordinary problem:** Lyrics must say something coherent while fitting a song’s verse, chorus, and line-level syllable pattern; ordinary line-by-line text generation often breaks the musical form.
- **Why hard:** Syllables constrain several nested units at once, so satisfying a line can damage a phrase or chorus, and semantic coherence must survive the edits.
- **Naive attempt:** Generate each line independently and count syllables only after generation.
- **Central move:** Generate complete lyrics conditioned on text and song form while controlling syllable counts at word, phrase, line, and paragraph levels.
- **Mechanism:** The paper proposes song-form-aware full-song lyrics generation with multi-level syllable control.
- **Conceptual structure:** The output is a structured object: constraints at smaller units must compose into a song-level form, rather than being repaired after a generic text model has already committed to lines.
- **What paper reports:** The paper reports controlled lyrics-generation experiments and makes generated samples available for inspection.
- **Limits:** Text prompts, song forms, syllable-count rules, dataset construction, and evaluation criteria bound the claim; syllable fit is not the same as singability, musicality, or authorship.

## 7. echo-and-reconstruction

**Paper:** [Towards Bitrate-Efficient and Noise-Robust Speech Coding with Variable Bitrate RVQ](https://www.isca-archive.org/interspeech_2025/chae25b_interspeech.html)
**Evidence:** D3; PDF SHA-256 `b95134638794c59bce084a366549d14e0fea7ba45cc616f9081da9b59b9b8ff2`; full text captured.

- **Ordinary problem:** A speech codec should spend bits on speech detail that matters to listeners, not on background noise, especially when the transmission budget changes from moment to moment.
- **Why hard:** Noise can consume code capacity while speech components vary in importance; removing noise and preserving speech quality are coupled rate-allocation decisions.
- **Naive attempt:** Use one constant bitrate for every frame or denoise after compression without changing the allocation.
- **Central move:** Use variable-bitrate residual vector quantization to allocate more representation to important speech frames and combine it with a feature denoiser.
- **Mechanism:** The paper proposes Variable Bitrate RVQ for noise-robust speech coding.
- **Conceptual structure:** Compression is selective reconstruction: the codec decides which parts of a noisy frame deserve precision, so rate, distortion, denoising, and perceptual quality must be evaluated together.
- **What paper reports:** The paper reports improved rate-distortion trade-offs and perceptual quality over constant-bitrate baselines in noisy conditions.
- **Limits:** Noise conditions, bitrates, codec architecture, datasets, perceptual measures, and model sizes bound the result; a cleaner perceptual signal is not necessarily a faithful waveform.

## 8. multilingual-and-crosslingual

**Paper:** [Relative cue weighting in multilingual stop voicing production](https://www.isca-archive.org/interspeech_2025/chan25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `cbf6402eb8136436928eb04ecc51861ff474c7cfa159f62f9a7c96d874147cab`; full text captured.

- **Ordinary problem:** A multilingual speaker must produce a stop contrast in several languages even when those languages use different cues such as closure voicing or aspiration.
- **Why hard:** The same person can keep language-specific categories while still showing dominance effects, and different acoustic cues can carry different weight in each language.
- **Naive attempt:** Assume one speaker-wide voicing rule or average all languages into one acoustic category.
- **Central move:** Measure nine acoustic correlates in Malay, English, and Mandarin speech from early multilingual Malaysians and use random forests to compare cue weighting.
- **Mechanism:** The paper studies relative cue weighting in multilingual stop-voicing production.
- **Conceptual structure:** Multilingual pronunciation is coordinated but not collapsed: language-specific cue bundles coexist with influence from which language is dominant for the speaker.
- **What paper reports:** The paper reports language-specific production for all early multilinguals, dominance-driven variation, and a salient role for closure voicing in Malaysian English.
- **Limits:** The Malaysian speakers, three languages, stop inventory, nine correlates, and random-forest analysis bound generalization to other multilingual populations or contrasts.

