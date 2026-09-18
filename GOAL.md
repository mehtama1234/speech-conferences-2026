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

- a small number of top-level themes derived from the baseline conceptual account;
- a variable number of subthemes under each theme, determined by real differences
  in the ordinary problem, failure mode, mechanism, or evidence—not by a quota;
- concrete concepts under each subtheme, only when they have a distinct boundary
  and at least one paper family that needs that boundary;
- a plain-language definition for every theme, subtheme, and concept;
- the ordinary problem, naive failure, recurring mechanism, and tradeoff for each;
- positive examples, negative examples, and boundary cases;
- evidence depth and source boundaries for every membership rule.

The starting taxonomy may include sound and articulation; recognition and
transcription; spoken meaning and dialogue; generation and voice; separation and
repair; speaker identity and paralinguistics; languages, accents, health, and
access; evaluation and deployment; and social consequences. These are hypotheses
to be tested against the papers, not final labels to be defended by intuition.

### Organic derivation rule

The taxonomy must be derived in a visible sequence from the baseline
first-principles conceptual account:

1. Name the baseline source or sources and record the exact sections that support
   each physical, human, or communicative starting point.
2. Rewrite each starting point as an ordinary pressure: what is happening in the
   world, what information is missing or mixed together, and what a person needs
   to hear, say, understand, or do.
3. For each pressure, record the tempting simple solution and the concrete reason
   it fails. Do not start with model names, conference labels, or keywords.
4. Read the papers and collect recurring moves: what is measured, preserved,
   discarded, separated, aligned, inferred, generated, or checked.
5. Propose a subtheme only when several papers share the same pressure and move,
   and when separating it from a neighboring subtheme changes the assumptions,
   failure cases, mechanism, or evaluation target.
6. Merge subthemes when their ordinary problem, mechanism, evidence, and limits
   are materially the same. Split them when a reader would learn a different
   causal story by keeping them apart.
7. Let the number of subthemes be the result of those tests. There must be no
   requirement that themes have equal numbers of subthemes or that subthemes have
   equal numbers of concepts.
8. Preserve rejected splits, rejected merges, and unresolved boundaries in the
   taxonomy record so the final structure can be challenged and revised.

The previous fixed three-subthemes-per-theme structure is not evidence of organic
derivation and must not be used as the final taxonomy. A passing validator may
check consistency, but it cannot certify that the conceptual divisions are good.

For every theme, subtheme, and concept, the record must answer in plain language:

- What ordinary situation creates the problem?
- What is mixed together, missing, changing, or misunderstood?
- What simple solution fails, and why?
- What recurring move solves part of the problem?
- Why is this boundary different from its neighbors?
- Which named papers support the boundary, and what evidence depth do they have?
- What paper or evidence would make the boundary split, merge, or disappear?

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

The current files are an audited processing release, not the finished intellectual
work. They contain 1,179 INTERSPEECH records and 3,864 ICASSP records, but that
does not mean every paper has been deeply read. The current D3 set is a selected
full-paper reading set; D2 rows are abstract-bounded; ICASSP rows are largely
title/abstract-bounded. The present taxonomy is an organic proposal, not yet a
fully defended account of the field.

The goal is complete only after the entire active corpus has been examined at the
strongest depth actually available and the final taxonomy has been written as a
clear first-principles explanation of speech research.

### Required end-to-end work

1. Establish the baseline account. Name the baseline paper or papers, record the
   exact passages used, and extract the starting facts about sound, speakers,
   listeners, language, interaction, devices, and consequences. Do not begin from
   conference keywords or the current scaffold.

2. Examine every corpus record. For every paper, attempt the official page, PDF,
   abstract, code, data, model, and presentation links in that order where they
   exist. Record what was read, what was unavailable, and why. Every record must
   end with either a supported assignment or an explicit unsupported, ambiguous,
   or insufficient-evidence decision. No paper may be counted as deeply read when
   only its title or abstract was available.

3. Write every paper analysis at its real evidence depth. A full-paper record must
   explain the actual problem, failed simple approach, central move, step-by-step
   mechanism, mathematical object, evaluation, reported result, assumptions, and
   limits. An abstract-only record must say exactly which of those facts remain
   unknown. No record may be padded with details borrowed from the model name or
   from a different paper.

4. Derive the taxonomy from the baseline and readings. For every proposed theme
   and subtheme, preserve the chain:

   `baseline fact -> ordinary speech pressure -> tempting simple solution ->
   concrete failure -> recurring paper move -> boundary from neighbors -> named
   evidence`

   A subtheme exists only when this chain differs in a way that changes the
   problem, information being handled, mechanism, evaluation target, or evidence
   limit. If two chains are the same, merge them. If one chain contains two
   different problems or mechanisms, split it. Equal counts are neither a goal nor
   evidence.

5. Write the complete theme and subtheme account. Every final theme must have a
   substantial plain-language writeup. Every final subtheme must have its own
   writeup containing all of the following:

   - the ordinary situation before a model is introduced;
   - what is mixed, missing, changing, or hard to observe;
   - the smart beginner's first solution;
   - the precise reason that solution fails;
   - the recurring move shared by the papers;
   - the inputs, outputs, and steps of that move;
   - the relevant mathematical idea explained in ordinary language;
   - at least two named supporting papers when the corpus permits;
   - a positive case, a negative case, and a boundary case;
   - the neighboring subtheme it could be confused with and the reason it is
     separate;
   - what the evidence does and does not establish.

   A paragraph that only says “papers use transformers,” “papers improve
   robustness,” “papers model prosody,” or “papers use embeddings” is not a
   writeup. Those phrases must be unpacked into a concrete speech problem and a
   sequence of operations.

6. Re-adjudicate membership after the taxonomy is written. Do not merely move old
   labels to new parents. Re-read the evidence for each supported membership and
   record why the paper belongs there rather than in its nearest neighbor. Keep
   rejected assignments and unresolved cases visible.

7. Synthesize paper families and venues. Explain what several papers jointly show,
   where they disagree, what changes across speakers, languages, rooms, devices,
   and tasks, and where a metric fails to represent human usefulness. Every broad
   statement must have named evidence and a denominator.

8. Audit the result. Rebuild the full release, verify hashes and provenance, run
   validators, inspect the human-readable reports, and check that the reports say
   “unknown” whenever the evidence is unknown. Separate author-reported results,
   analyst interpretation, artifact inspection, and independent execution.

### Completion gates

The goal is not complete unless all of these are true:

- every active record has a recorded evidence depth and disposition;
- every full-paper claim points to a captured page, section, or text hash;
- every final theme and subtheme has the complete first-principles writeup above;
- every final subtheme has a derivation record and named supporting evidence;
- rejected splits, rejected merges, and unresolved boundaries are preserved;
- no subtheme exists only because of a quota, keyword, venue label, or convenient
  implementation;
- all syntheses use explicit denominators and distinguish D1/D2/D3/D4/D5 evidence;
- the clean rebuild and validators pass, and an independent reader can follow the
  atlas from an ordinary speech problem to a mechanism, evidence, and limit.

The release is therefore not complete merely because files are reproducible or a
validator is green. It is complete only when the writing itself demonstrates that
the themes and subthemes are necessary, understandable, evidence-backed divisions
of speech research.
