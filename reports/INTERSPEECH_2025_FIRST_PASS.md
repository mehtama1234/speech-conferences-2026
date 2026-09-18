# INTERSPEECH 2025 first-pass speech atlas

## What this establishes

This report is a deterministic abstract-aware map of the official ISCA Archive
for INTERSPEECH 2025. The archive contains **1,179 papers**;
**1,179** have abstracts in the captured corpus, and there
were **0** source-page failures.

The assignment method matches transparent patterns against each official title
and abstract. It is useful for discovering field structure, but it is not a
full-paper semantic judgment. Every assignment is therefore marked D2 (abstract
evidence), and the report must not be read as evidence that the paper's detailed
mechanism or result has been independently checked.

Source: [https://www.isca-archive.org/interspeech_2025/](https://www.isca-archive.org/interspeech_2025/)

## First-principles themes

| Theme | Papers | Share of corpus | Why this pressure exists |
|---|---:|---:|---|
| Sound, acoustics, and speech production | 495 | 42.0% | Speech begins as changing air pressure shaped by bodies, rooms, microphones, and channels. |
| Recognizing and transcribing speech | 384 | 32.6% | A system must turn a continuous, variable sound stream into words, boundaries, and aligned text. |
| Understanding, translating, and dialoguing | 113 | 9.6% | Recognized words are not yet an interpretation of intent, context, or a response in another language. |
| Generating, converting, and controlling voice | 178 | 15.1% | A generated voice must preserve linguistic content while controlling identity, timing, expressiveness, and naturalness. |
| Separating and repairing sound | 153 | 13.0% | A microphone records mixtures, echoes, and noise; useful speech must be preserved while unwanted sound is removed. |
| Speaker identity and beyond-the-words information | 354 | 30.0% | Voice carries information about who is speaking and how they are speaking, but that evidence changes with context. |
| Languages, accents, people, and access | 286 | 24.3% | Speech systems meet variation in language, dialect, age, disability, health, culture, and available data. |
| Evaluation, robustness, privacy, and deployment | 765 | 64.9% | A benchmark score is only useful if it stands for a real listening failure and survives new speakers, rooms, languages, and devices. |

Membership is overlapping: a paper can address more than one pressure. The map
therefore measures theme mentions/assignments, not a partition of the conference.
54 papers received no current conceptual
assignment and remain an explicit review queue rather than being forced into a
theme.

## Evidence boundaries

- D0/D1 metadata and title evidence are not used to claim a mechanism.
- D2 abstracts support the broad problem, method family, and stated result only
  when the abstract says them explicitly.
- D3 full-paper analysis, D4 artifact inspection, and D5 independent execution
  have not yet been completed by this first pass.
- Theme counts are corpus-local and should not be interpreted as prevalence in
  speech research as a whole.
- Abstract claims remain author-reported claims until full-paper and artifact
  corroboration are performed.

## Next depth pass

1. Resolve the 54 unmatched records and review ambiguous multi-theme assignments.
2. Add paper-level `bp`, `wh`, `naive`, `ap`, `mech`, `math`, `dots`, `ww`,
   `po`, and `limits` records for the highest-yield themes.
3. Inspect official PDFs for mechanism, assumptions, baselines, denominators,
   and limitations.
4. Audit linked code, data, checkpoints, and run instructions.
5. Compare the resulting speech taxonomy with the existing ICASSP 2026 map.
