# ICASSP 2026 / INTERSPEECH 2025 first-principles crosswalk

This comparison uses the new conceptual taxonomy. Its compact counts are analyst-reviewed primary-candidate assignments; they are not venue prevalence claims.

- ICASSP denominator: 3,864; 682 D2 abstracts and 3,182 D1 title-only records.
- INTERSPEECH denominator: 1,179 D2 archive records.
- ICASSP records unsupported for the speech taxonomy remain visible: 3,254.
- Analyst-reviewed semantic records: 3864 ICASSP abstract records versus 1179 INTERSPEECH D2/D3 records.

| First-principles theme | INTERSPEECH supported assignment | INTERSPEECH ambiguous | ICASSP supported assignment | ICASSP ambiguous |
|---|---:|---:|---:|---:|
| Sound, bodies, rooms, and recording | 61 | 0 | 26 | 0 |
| Listening through noise, overlap, and missing sound | 111 | 0 | 104 | 0 |
| From sound to words and structured speech | 176 | 0 | 66 | 0 |
| From spoken form to meaning and coordinated action | 83 | 0 | 46 | 0 |
| Creating speech while keeping the right things fixed | 62 | 0 | 36 | 0 |
| Speakers as changing people, not nuisance variables | 72 | 0 | 24 | 0 |
| Many languages, accents, and unequal evidence | 91 | 0 | 22 | 0 |
| Evidence, practical systems, and consequences | 438 | 0 | 208 | 0 |

## Analyst-reviewed evidence by theme

These are counts of explicit analyst-reviewed assignments, separated by evidence depth. They are a reviewed sample, not venue prevalence.

| First-principles theme | INTERSPEECH D2 | INTERSPEECH D3 | ICASSP D2 | ICASSP D3 |
|---|---:|---:|---:|---:|
| Sound, bodies, rooms, and recording | 92 | 11 | 35 | 0 |
| Listening through noise, overlap, and missing sound | 122 | 18 | 43 | 0 |
| From sound to words and structured speech | 125 | 17 | 35 | 0 |
| From spoken form to meaning and coordinated action | 130 | 13 | 35 | 0 |
| Creating speech while keeping the right things fixed | 81 | 15 | 37 | 0 |
| Speakers as changing people, not nuisance variables | 186 | 16 | 33 | 0 |
| Many languages, accents, and unequal evidence | 133 | 15 | 29 | 0 |
| Evidence, practical systems, and consequences | 138 | 17 | 33 | 0 |

## Named conceptual contrasts

These are deliberately small, paper-grounded comparisons rather than claims about which venue is larger or better.
### Mixtures and competing speakers

**Ordinary problem:** A listener or recognizer must decide which voice belongs to which person when speech overlaps.

**INTERSPEECH assignment:** `alizadeh25_interspeech` — ReSepNet: A Unified-Light Model for Recursive Speech Separation with Unknown Speaker Count (D3) — Recursive separation makes the unknown speaker count part of the separation problem.

**ICASSP assignment:** `6599ad30ece84a9f571a837dbf05989981c9ac5b` — Loose Coupling of Spectral and Spatial Models for Multi-Channel Diarization and Enhancement of Meetings in Dynamic Environments (D2) — Meeting diarization and enhancement must use spectral and spatial evidence together when speakers and room conditions change.

**Denominator:** INTERSPEECH comparison context is the 1,179-record archive corpus; ICASSP comparison context is the 3,864-record captured corpus, with this named contrast using one reviewed paper from each venue.

**Conceptual contrast:** INTERSPEECH makes unknown speaker count the central structural problem and recursively peels voices apart; the reviewed ICASSP paper treats meeting diarization and enhancement as coupled spatial decisions in a changing room.

**Boundary:** INTERSPEECH is D3 full-paper evidence; ICASSP is D2 abstract evidence, so this is a mechanism contrast, not a venue prevalence claim.

### Recognition and usable boundaries

**Ordinary problem:** Recognizing words is not enough if the system cannot decide when a unit is complete or how it becomes usable text.

**INTERSPEECH assignment:** `ho25_interspeech` — Dynamic Context-Aware Streaming Pretrained Language Model For Inverse Text Normalization (D3) — Streaming inverse text normalization makes the recognition-to-written-text boundary explicit under limited context and latency.

**ICASSP assignment:** `04bc5dc9cb6f4ffdb8109153c0762ceb4ec93fba` — Scale: Semantic Chunking and Label-Delay Engine For Streaming Speech-LLM (D1) — Streaming speech models need explicit chunk and label-delay rules to trade context against response time.

**Denominator:** INTERSPEECH comparison context is the 1,179-record archive corpus; ICASSP comparison context is the 3,864-record captured corpus, with this named contrast using one reviewed paper from each venue.

**Conceptual contrast:** INTERSPEECH uses dynamic right-context and chunk size for streaming inverse text normalization; the ICASSP title-bounded assignment concerns semantic chunking and label delay inside a speech-language stream.

**Boundary:** The INTERSPEECH mechanism is D3; the ICASSP assignment is D1 title evidence and cannot support outcome or mechanism detail.

### Emotion as interactional evidence

**Ordinary problem:** Emotion is not a fixed label in the waveform; it is inferred from changing cues, missing channels, and listener interpretation.

**INTERSPEECH assignment:** `hu25c_interspeech` — Label Semantic-Driven Contrastive Learning for Speech Emotion Recognition (D2) — Emotion labels are not equally separated in speech; label semantics are used as anchors for subtle affective distinctions.

**ICASSP assignment:** `11303a06ceaffe7797c7617cf893255fb38f02d4` — SURE: Synergistic Uncertainty-aware Reasoning for Multimodal Emotion Recognition in Conversations (D2) — Emotion recognition in conversation needs uncertainty-aware reasoning because affect and context are not fixed independent labels.

**Denominator:** INTERSPEECH comparison context is the 1,179-record archive corpus; ICASSP comparison context is the 3,864-record captured corpus, with this named contrast using one reviewed paper from each venue.

**Conceptual contrast:** INTERSPEECH uses label semantics as anchors for subtle emotion boundaries; the ICASSP paper frames uncertainty-aware reasoning over multimodal conversation as the way to handle ambiguous evidence.

**Boundary:** Both are abstract-bounded D2 assignments here; neither establishes general emotional understanding or comparable performance across venues.

### Creating speech while preserving identity

**Ordinary problem:** A speech generator must change the requested content or style without accidentally changing who is speaking or how understandable the result is.

**INTERSPEECH assignment:** `zalkow25_interspeech` — Bridging the Training–Inference Gap in TTS: Training Strategies for Robust Generative Postprocessing for Low-Resource Speakers (D3) — Generative postprocessing improves low-resource TTS naturalness while checking objective proxies against listener judgments.

**ICASSP assignment:** `1d9d53c8debfbf7ed246bd7a53cdd1342998264c` — F5E-TTS: Enhancing Speech Synthesis by Aligning Text with Rich Semantic Representations (D1) — Speech synthesis must align semantic text content with the acoustic sequence so fluent wording does not drift from what is spoken.

**Denominator:** INTERSPEECH comparison context is the 1,179-record archive corpus; ICASSP comparison context is the 3,864-record captured corpus, with this named contrast using one reviewed paper from each venue.

**Conceptual contrast:** INTERSPEECH separates low-resource TTS generation from a naturalness postprocessor and checks listener judgments; the ICASSP abstract assignment focuses on aligning text with rich semantic representations during synthesis.

**Boundary:** The INTERSPEECH result is D3 and author-reported; the ICASSP comparison is D2 abstract evidence, so quality and mechanism are not directly comparable.

## What can be said now

The two corpora can now be compared using the same conceptual questions, but not yet as settled research emphasis. INTERSPEECH has complete abstract evidence and a speech-focused denominator. ICASSP has a much broader denominator and mostly title-only evidence, so its proposed assignments are both less certain and more affected by scope filtering.

The reviewed table is evidence about the explicit corpus assignments, not a random sample and not a prevalence estimate. The remaining comparison gate is comparable D3 review in both venues. Until then, differences in the assignment table may reflect source access, title vocabulary, and the 3,182 ICASSP records without abstracts rather than differences in research activity.
