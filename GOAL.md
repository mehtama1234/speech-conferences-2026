# Meaty end-to-end goal: first-principles speech research analysis

## The actual objective

Build the speech equivalent of the ICML/ICLR deep research atlas: begin with a
first-principles conceptual account of speech, derive themes, subthemes, and
reusable concepts from that account, assign the entire captured corpus through a
semantic review process, and write paper analyses that explain what each paper is
actually trying to make possible.

The output must be a teaching-quality research analysis, not a title map, keyword
cloud, vague topic summary, or infrastructure-only release.

The reader should be able to move through the atlas like this:

`ordinary speech problem -> first-principles concept -> theme -> subtheme -> paper family -> paper mechanism -> evidence -> limitation`

The current ICASSP title map and INTERSPEECH abstract corpus are inputs to this
work. They are not the finished analysis.

## What “deep” means here

Every important concept must start with the ordinary physical or human problem
that forced it into existence:

- air pressure changes over time and a microphone records a mixture;
- a vocal tract turns intention into sound through moving articulators;
- a listener must separate words from noise, accent, overlap, and room echo;
- a recognizer must decide where sounds become phonemes, words, and meaning;
- a generated voice must preserve linguistic content while changing identity,
  timing, emotion, or prosody;
- a speaker's voice changes with age, health, emotion, language, and context;
- a benchmark score is only a proxy for intelligibility, naturalness, identity,
  access, or human usefulness.

For each idea, explain in plain language:

1. What real-world problem exists before the model is introduced?
2. What would a smart beginner try first?
3. Why does that simple approach fail?
4. What information is kept, discarded, compared, aligned, separated, compressed,
   predicted, or generated?
5. What is the mechanism, step by step?
6. What mathematical object or principle makes the mechanism possible?
7. Why does that principle fit sound, speech, language, people, rooms, or devices?
8. What sibling papers make the same deeper move with different vocabulary?
9. What does the paper actually show, and what does it not show?

No jargon may substitute for these explanations. “Uses embeddings,” “uses
attention,” “uses diffusion,” “uses a foundation model,” “uses signal
processing,” and “improves robustness” are not explanations until the moving
parts and the real failure being reduced are named.

## Analytical layers to build

### Layer 1: first-principles conceptual taxonomy

Create a machine-readable and human-readable taxonomy with:

- 8–12 top-level speech themes;
- 3–6 subthemes under each theme;
- 3–5 concrete concepts under each subtheme;
- a plain-language definition for every theme, subtheme, and concept;
- the ordinary problem, naive failure, recurring mechanism, and tradeoff for each;
- positive examples, negative examples, and boundary cases;
- evidence depth and source boundaries for every membership rule.

The starting taxonomy may include sound and articulation; recognition and
transcription; spoken meaning and dialogue; generation and voice; separation and
repair; speaker identity and paralinguistics; languages, accents, health, and
access; evaluation and deployment; and social consequences. These are hypotheses
to be tested against the papers, not final labels to be defended by intuition.

The taxonomy must become more precise than those umbrella labels. For example,
“recognition” should separate acoustic-to-text mapping, alignment and boundary
decisions, rare-word/context biasing, disfluency preservation, multilingual
switching, and clinical speech—not count them as one topic.

### Layer 2: whole-corpus semantic assignment

Build a deterministic review queue over all ICASSP speech/audio and INTERSPEECH
records. Keyword matches may discover candidates, but they may not be the final
semantic judgment.

For every candidate assignment, record:

- paper identity and source URL;
- theme, subtheme, and concept proposed;
- decision: `supported`, `unsupported`, `ambiguous`, or `insufficient-evidence`;
- evidence depth: title, abstract, full paper, artifact, or execution;
- exact title/abstract/full-paper excerpt or section supporting the decision;
- reviewer rule and confidence;
- alternative plausible assignment;
- whether the decision changes a theme count or synthesis claim.

The queue must be closed for the active taxonomy: every candidate row receives a
decision, and unmatched or insufficient rows remain visible. Do not quietly
convert lexical presence into semantic membership.

Maintain separate denominators for all conference records, ICASSP speech/audio
records, INTERSPEECH records, candidate assignments, supported assignments,
ambiguous/insufficient assignments, papers with abstracts, papers with full text,
and papers with code or executable artifacts.

### Layer 3: per-paper first-principles analyses

Every paper receives a structured record. At D2 abstract depth, the record must
remain explicitly bounded; at D3 full-paper depth, it should be a real conceptual
lesson.

Required fields:

- `bp`: ordinary problem and why anyone cares;
- `wh`: why the problem is difficult;
- `naive`: natural first attempt and its failure;
- `ap`: central conceptual move;
- `mech`: step-by-step mechanism and moving parts;
- `math`: mathematical objects, losses, signals, or decision rules in plain language;
- `dots`: links to themes, subthemes, concepts, and sibling paper families;
- `eval`: task, baseline, metric, denominator, and what the metric stands for;
- `ww`: what the paper reports;
- `po`: practical or scientific payoff claimed by the paper;
- `limits`: assumptions, failure cases, missing controls, and evidence boundary;
- `source`: exact paper/abstract/PDF location and content hash;
- `depth`: D1, D2, D3, D4, or D5.

Reject or regenerate a record that only names a model, dataset, benchmark, or
paper title; says “better performance” without identifying the real failure; gives
a mechanism with no inputs/outputs; gives a payoff without limitations; or fills
full-paper details from an abstract-only source.

### Layer 4: paper families and subtheme synthesis

For every active subtheme and important paper family, write the deeper shared
story:

- the recurring listening, speaking, or communication pressure;
- the naive strategy many papers outgrow;
- the recurring mathematical or engineering move;
- how the move appears in different papers;
- what changes across languages, speakers, rooms, devices, or tasks;
- representative positive cases;
- negative and boundary cases;
- what evidence supports the family claim;
- what remains unresolved.

The synthesis must connect the papers conceptually. It must not be a list of
paper titles followed by a generic sentence about “future work.”

### Layer 5: cross-venue and cross-conference comparison

Compare ICASSP 2026 and INTERSPEECH 2025/2026 only after the semantic layers
exist. Ask which deeper speech problems recur in both venues; which subthemes are
emphasized by signal-processing versus speech-communication communities; which
differences are real research emphasis versus source/access differences; which
concepts are uniquely visible; how papers evaluate intelligibility, naturalness,
identity, meaning, fairness, robustness, privacy, and human usefulness; and where
claims exceed evaluation evidence.

Every comparison paragraph must link to paper assignments and state its denominator.
No venue-wide prevalence, causal ranking, or “community believes” claim may be
made from lexical counts or a purposive D3 sample.

## Evidence and reproducibility boundaries

Use the following evidence ladder:

- D0 metadata only;
- D1 title/keyword interpretation;
- D2 abstract-supported problem, method family, and stated result;
- D3 full-paper mechanism, assumptions, evaluation, and limitations;
- D4 code/data/model/presentation inspection;
- D5 bounded independent execution with environment, inputs, outputs, and deviations.

The atlas must keep author-reported results, analyst interpretation, artifact
inspection, and local execution separate. Repository presence is not reproduction.
Reachability is not runnable code. A local smoke test is not validation of a paper's
scientific conclusion.

For code, data, checkpoints, demos, and presentations, record repository/ref,
critical files, dependencies, hardware, access gates, commands, logs, hashes,
missing pieces, and the exact reason execution was completed, partial, or not
attempted.

## Required output structure

The release must include:

- official/discovery source manifests and denominator report;
- extracted paper text and provenance hashes;
- conceptual taxonomy: themes, subthemes, concepts, rules, examples, boundaries;
- closed semantic review queue with every decision preserved;
- per-paper evidence records for the full captured corpus;
- D3 deep notes for the papers carrying major theme and synthesis claims;
- paper-family and cross-venue syntheses;
- claim ledger linking each headline claim to paper evidence;
- code/data/presentation/reproducibility audit;
- human-readable reports and reader navigation;
- deterministic rebuild script, release manifest, and validators;
- completion audit that distinguishes verified analysis from unresolved science.

## Definition of done

## Current completion state

The bounded end-to-end goal is complete. The atlas contains 1,179 INTERSPEECH and
3,864 ICASSP records with closed semantic dispositions, 8 themes, 24 subthemes, and
72 concepts. It contains 469 D3 and 710 D2 INTERSPEECH evidence records; every
subtheme has 18–22 D3 papers, with captured-PDF/text hashes, family comparisons,
cross-venue denominators, artifact audits, reader navigation, release manifests,
and a clean deterministic rebuild. The final validator passes with zero errors.

The completion audit remains explicit about boundaries: additional D3 readings are
optional expansion; data-dependent training and independent scientific reproduction
are not established; and 125 ICASSP discovery records remain unmatched to the
official supplement. These are not silently upgraded into evidence.

The goal is complete only when:

1. The conceptual taxonomy has precise first-principles themes, subthemes, and
   concepts with plain-language explanations, rules, examples, and boundaries.
2. The whole active corpus has semantic assignments or explicit unsupported,
   ambiguous, or insufficient-evidence decisions; no active queue is silently
   left unreviewed.
3. Every paper has a depth-labeled evidence record, and the major papers in each
   theme/family have full first-principles notes rather than vague summaries.
4. Every theme, subtheme, concept, and paper family has a connected synthesis
   grounded in named papers and explicit denominators.
5. ICASSP and INTERSPEECH comparisons separate research differences from source,
   access, and taxonomy differences.
6. Code, data, presentation, and execution evidence are audited without claiming
   reproduction where none occurred.
7. The final reader path is explanatory: it teaches the field from ordinary
   speech problems through mechanisms, mathematics, evidence, and limits.
8. A clean rebuild reproduces the semantic layers, reports, manifests, and release
   artifacts; focused tests and validators pass with zero errors.

The bounded release is not complete merely because its files are reproducible.
It is complete when the reproducible files contain the deep conceptual and
paper-grounded analysis that makes the atlas useful.
