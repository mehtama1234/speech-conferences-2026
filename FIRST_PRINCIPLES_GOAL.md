# Deep First-Principles Analysis Goal

Build the speech site as a deeply explanatory map of the field, not a list of paper titles or topic counts. The current ICASSP 2026 site is title-only, so it must stay honest: titles can support a careful topic map, but they are not enough for detailed per-paper mechanisms. When abstracts or proceedings are available, every paper, theme, subtheme, mathematical concept, and paper family should be rebuilt from first principles in plain everyday language.

The reader is smart and curious, but should not need prior knowledge of math, machine learning jargon, benchmark jargon, speech-processing jargon, signal-processing jargon, acoustics jargon, optimization jargon, or systems jargon. Every technical idea must be explained before it is named.

## What The Analysis Must Teach

For every paper, theme, subtheme, mathematical concept, and paper family, explain:

- the real-world sound or communication problem: a voice being heard, words being recognized, a speaker being identified, a noisy recording being cleaned, a room echo being handled, music being separated, or a device listening under bad conditions
- why the problem exists before any method is introduced
- what a smart beginner would try first
- exactly why that naive attempt fails
- the paper's central move in concrete mechanical terms
- what sound, text, labels, timing, speaker evidence, room evidence, or device signal goes in
- what gets transformed, compared, scored, separated, aligned, compressed, predicted, or generated
- what mathematical principle is underneath the method
- why that principle fits the structure of sound, speech, music, language, rooms, or devices
- how the paper connects to sibling papers, neighboring subthemes, and the broader field
- what assumptions must hold, and what the available evidence does not prove

## Per-Paper Standard

Each paper should read like a small conceptual lesson. It should not simply restate an abstract. The explanation should start from the ordinary object: air pressure changing over time, a mouth producing sounds, a microphone mixing voice with room echo, a listener trying to separate speakers, a model deciding where one word ends and another begins, or a device trying to act on spoken intent.

For each paper, the reader should be able to answer:

- What ordinary listening, speaking, music, or communication problem is this paper trying to handle?
- What would someone naturally try first?
- What exactly breaks in that simple attempt?
- What information does the paper keep, discard, compare, align, separate, smooth, predict, or generate?
- What mathematical idea makes that move possible?
- Why is that math a better language for the problem than a hand-written rule?
- What sibling papers are solving the same deeper problem with different surface vocabulary?
- What must be true about the sound, speaker, room, labels, device, or dataset for the claim to be trustworthy?

The paper-level story should include:

- `bp`: big picture
- `wh`: why it is hard
- `naive`: the naive solution and why it fails
- `ap`: the core idea
- `mech`: how the mechanism runs step by step
- `math`: the mathematical concepts being used
- `dots`: how it connects to themes, subthemes, and paper families
- `ww`: why it works
- `po`: payoff
- `limits`: limits and assumptions

The main anti-shallow fields are `mech`, `math`, `dots`, and `limits`. They must name the moving parts and their relationships, not just say "the model learns better features."

## Theme, Subtheme, And Paper-Family Standard

A theme or family should answer: why do these papers belong together?

For each family, explain the shared problem shape, the repeated failure mode, the recurring mathematical tools, and what changed in 2026. The family explanation should make the reader see that superficially different speech papers are often solving the same deeper problem: separating signal from noise, aligning sound with text, deciding speaker identity, preserving meaning while changing voice, compressing a long waveform, estimating uncertainty, adapting to a new accent or room, or making a small device listen reliably.

Themes and subthemes must not be umbrella labels. They should act like connective tissue across papers:

- Here is the common listening or communication pressure that keeps appearing.
- Here is the naive strategy that many papers are trying to move beyond.
- Here is the recurring mathematical move.
- Here is why that move appears in different-looking papers.
- Here are the representative branches of the same idea.
- Here is what changed this year: noisier settings, weaker labels, multilingual breadth, smaller devices, stronger privacy requirements, better generation control, harder spoofing, or more realistic evaluation.

## Math Standard

Do not say "uses signal processing" and stop. Explain what is mixed in the sound and what must be separated.

Do not say "uses optimization" and stop. Explain what settings are being changed and what counts as a worse transcription, worse separation, worse speaker match, or worse generated sound.

Do not say "uses attention" and stop. Explain what pieces of sound or text are being compared, and why some moments should influence the answer more than others.

Every mathematical concept must answer:

- What problem forced this idea into existence?
- What is the idea in everyday language?
- Why does this idea work for this family of papers?

Also explain the shape of the mathematical object:

- If the paper uses a waveform, explain that it is a changing pressure trace over time and what parts carry useful information.
- If it uses a spectrum, explain that sound can be viewed as a mixture of slow and fast vibrations, and why that view can make speech easier to separate.
- If it aligns audio and text, explain what has to be matched in time and where ambiguity enters.
- If it estimates speaker identity, explain what evidence is stable about a voice and what changes with emotion, microphone, room, or language.
- If it removes noise, explain what counts as unwanted sound and why removing too much can damage speech.
- If it generates speech or music, explain what structure must be preserved so the output sounds intentional rather than merely plausible.
- If it learns from examples, explain what pattern is being reused and why reuse may fail for new speakers, languages, microphones, or rooms.

The important concept behind the math is usually a tradeoff: noise removal versus speech damage, speaker similarity versus privacy, accuracy versus device cost, language coverage versus data quality, naturalness versus control, compression versus intelligibility, and local sound evidence versus long-range meaning.

## Rejection Criteria

Reject and regenerate any output that:

- defines the paper only by a model or dataset name
- says "improves accuracy" without explaining what real listening failure is reduced
- says "uses embeddings", "uses attention", "uses diffusion", "uses optimization", or "uses signal processing" without translating the idea
- lists papers without explaining the shared problem underneath them
- explains a benchmark score without explaining the real-world task the score stands in for
- uses jargon as a shortcut
- gives a payoff without limits or assumptions
- invents paper-level details from a title-only source

## Data Honesty

Until abstracts or proceedings are available, the speech project should remain a title-only theme map. It can describe likely field-level pressures and topic families, but it should not claim detailed per-paper mechanisms. When stronger source data arrives, rerun the deeper pipeline against paper-level evidence.
