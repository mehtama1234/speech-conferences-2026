# INTERSPEECH 2025 sixtieth-pass full-paper notes

Three genuinely uncaptured readings raise the remaining source-separation, voice-conversion, and accent-boundary families.

## 1. source-separation-and-spatial-listening

**Paper:** [Neural Speech Extraction with Human Feedback](https://www.isca-archive.org/interspeech_2025/itani25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `68f8bb70a3a6d06a4ca2d7ca7e871d42f23f9680b020bdcd2c4f0185d144dd95`; full text captured.

- **Ordinary problem:** A listener should extract a desired speech source from a mixture when ordinary separation assumptions are insufficient.
- **Why hard:** Target identity, mixture variability, and human preference can disagree with signal-level objectives.
- **Naive attempt:** Use an unconditioned separator and assume the loudest or most separable source is the desired one.
- **Central move:** Use human feedback to guide neural speech extraction toward the target source.
- **Mechanism:** Human preference supplies a target-selection signal alongside acoustic separation; the model is evaluated on extraction behavior.
- **Mathematical/conceptual structure:** Separation is not only signal recovery: the system must specify which source counts as useful to a listener.
- **What paper reports:** The paper reports neural speech extraction with human feedback.
- **Limits:** Feedback population, mixture construction, target definition, signal metrics, and model scope bound transfer.

## 2. voice-identity-and-conversion

**Paper:** [LinearVC: Linear Transformations of Self-Supervised Features Through the Lens of Voice Conversion](https://www.isca-archive.org/interspeech_2025/kamper25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `9dc6d73aa40e047fa9874135439bb612a7f90a00340387442d3d93fe8571e2a5`; full text captured.

- **Ordinary problem:** Voice conversion should transform a speaker's voice while preserving linguistic content and remain useful with limited target data.
- **Why hard:** Self-supervised features encode both content and identity, so a simple transform can leak source traits or distort words.
- **Naive attempt:** Copy nearest target embeddings or train a separate waveform model per speaker.
- **Central move:** Study linear transformations of self-supervised features as a controlled voice-conversion mechanism.
- **Mechanism:** A learned transformation maps representation distributions toward a target voice while retaining content-related structure.
- **Mathematical/conceptual structure:** Conversion is a representation-space mapping: content preservation and target identity are competing constraints.
- **What paper reports:** The paper reports LinearVC results through the lens of self-supervised feature transformations.
- **Limits:** Feature model, languages, target data, similarity/content metrics, and transform assumptions bound transfer.

## 3. accent-and-cultural-boundaries

**Paper:** [A Multimodal Chinese Dataset for Cross-lingual Sarcasm Detection](https://www.isca-archive.org/interspeech_2025/gao25f_interspeech.html)
**Evidence:** D3; PDF SHA-256 `de40c16869e79395e128991685d60b68ca8fb8af354941a425179cc9f4a99b48`; full text captured.

- **Ordinary problem:** A multilingual ASR system should handle accents and varieties without treating one pronunciation norm as universal.
- **Why hard:** Accent variation changes acoustic-to-word evidence and can interact with language and speaker identity.
- **Naive attempt:** Train or evaluate only on standard speech and report one pooled error rate.
- **Central move:** Analyze accent robustness under multilingual conditions and identify where recognition errors reflect a narrow training norm.
- **Mechanism:** Subgroup and accent-conditioned evaluation separates intended-word performance across varieties rather than hiding failures in an aggregate.
- **Mathematical/conceptual structure:** Robustness is a boundary measurement: the system's norm becomes visible only when varieties are evaluated separately.
- **What paper reports:** The paper reports a study of multilingual/accent robustness and its implications for ASR evaluation.
- **Limits:** Accent labels, languages, speakers, test design, and subgroup denominators bound transfer.

