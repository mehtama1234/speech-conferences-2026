# INTERSPEECH 2025 seventeenth-pass full-paper notes

Four additional official-PDF readings deepen separation, expressive synthesis, cross-modal grounding, and overlapping-speech attribution. Results are author-reported and not independently reproduced.

## 1. source-separation-and-spatial-listening

**Paper:** [Inter-Speaker Relative Cues for Text-Guided Target Speech Extraction](https://www.isca-archive.org/interspeech_2025/dai25b_interspeech.html)
**Evidence:** D3; PDF SHA-256 `d86543541f96330320362c68c9c16a6eceb97ffff506c296819c2261f638a01d`; 5 pages.

- **Ordinary problem:** A separator should isolate the speaker a user describes, even when the enrollment recording or direction cue is unavailable.
- **Why hard:** Fixed categories such as male/female or high/low pitch lose information and do not expand cleanly across languages and rooms.
- **Naive attempt:** Treat every attribute as a fixed class or use only one cue such as gender.
- **Central move:** Describe the target relative to the interfering speaker, then combine relative cues and pretrained speech representations in a text-conditioned extractor.
- **Mechanism:** Two-speaker mixtures are built across five languages with cues for language, gender, emotion, order, age, rate, duration, pitch, loudness, and distance; prompts identify the target by those relations.
- **Conceptual structure:** The central object is not a speaker label but a relation between two signals. Extraction quality is measured after the text selects one member of the mixture.
- **What paper reports:** The paper reports that all relative cues beat random subsets, with gender and temporal order especially robust across languages and reverberation; WavLM/CNN initialization improves the baseline.
- **Limits:** The claim is bounded to the constructed mixtures, cue templates, languages, and author-reported tests; real conversational mixtures and privacy effects remain open.

## 2. prosody-and-interactive-control

**Paper:** [Voice Impression Control in Zero-Shot TTS](https://www.isca-archive.org/interspeech_2025/fujita25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `d8845d3d2166ef9c15ba9a96b16fc43dbe6a90e0ad952b9b3c3456c6886d5471`; 5 pages.

- **Ordinary problem:** Zero-shot TTS can imitate a voice while failing to control the subtle qualities listeners perceive as bright, dark, tense, or warm.
- **Why hard:** Speaker identity and impression are entangled, and a text description alone is too coarse for fine control.
- **Naive attempt:** Add a style token or manually search a latent vector for every speaker.
- **Central move:** Represent impression as a small vector of antonym-pair intensities, remove it from the speaker representation, and reinsert the requested values at synthesis time.
- **Mechanism:** The method trains a control module around FastSpeech2, uses subjective ratings to estimate impression vectors, and uses a language model to turn descriptions into those vectors.
- **Conceptual structure:** A generated utterance is judged on two axes: whether it preserves the reference speaker and whether the requested impression moves in the intended direction. The dimensions are correlated, so independent sliders are an approximation.
- **What paper reports:** Objective and subjective tests report effective single-dimension impression control and language-generated vectors that avoid manual optimization.
- **Limits:** The evidence is limited to the selected impression dimensions, speakers, ratings, and TTS model; listener consistency and cross-language control are not established.

## 3. grounding-and-action

**Paper:** [PAEFF: Precise Alignment and Enhanced Gated Feature Fusion for Face-Voice Association](https://www.isca-archive.org/interspeech_2025/hannan25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `a70bc19c6a9e8ea8beec74e01fb8baaf122cc7855300c55816bfe474047ec88a`; 5 pages.

- **Ordinary problem:** A system should decide whether a face and a voice belong together when the person or video is unfamiliar, without relying on hand-tuned negative examples.
- **Why hard:** Face and voice embeddings live in different spaces; margins and mined negatives can make association depend on arbitrary training choices.
- **Naive attempt:** Use a contrastive or triplet loss with a fixed distance margin and assume the two modalities align after ordinary fusion.
- **Central move:** Align the modalities with orthogonality constraints and gated feature fusion in a joint hyperbolic space, where hierarchy-like distances can represent identity similarity.
- **Mechanism:** The two branches extract pretrained face and voice features, fuse them, and optimize a combination of association, orthogonality, and hyperbolic objectives on VoxCeleb1.
- **Conceptual structure:** Verification asks whether a pair matches, while AUC and EER expose different threshold behavior. Seen-heard and unseen-unheard splits test whether the association survives new videos and people.
- **What paper reports:** On the reported VoxCeleb1 splits, PAEFF improves the best listed baseline on unseen-unheard EER and reaches the highest or near-highest AUC in the table.
- **Limits:** The result is author-reported and tied to VoxCeleb1, its split protocol, pretrained encoders, and hyperparameters; it does not establish robustness to dubbing, adversarial pairing, or other cultures.

## 4. grounding-and-action

**Paper:** [Unified Audio-Visual Modeling for Recognizing Which Face Spoke When and What in Multi-Talker Overlapped Speech and Video](https://www.isca-archive.org/interspeech_2025/makishima25b_interspeech.html)
**Evidence:** D3; PDF SHA-256 `8c739fc23e9c9e45b9a20a9b26c7119d3849582044d1b3639a4b5b6726fad498`; 5 pages.

- **Ordinary problem:** In an overlapping conversation, understanding requires assigning each word and time interval to the correct face, not merely producing a bag of words.
- **Why hard:** A pipeline that separately separates speech, detects active speakers, and recognizes speech accumulates interfaces and errors.
- **Naive attempt:** Run single-talker ASR or chain independent separation, lip-motion detection, and transcription modules.
- **Central move:** Train one encoder-decoder to emit a serialized sequence containing speaker tags, timing structure, and words from overlapped audio plus all visible faces.
- **Mechanism:** The model combines speech and video encoders with Transformer decoding; evaluation compares it with single-talker, multi-talker, and modular audio-visual baselines on LRS3-derived mixtures.
- **Conceptual structure:** WER measures words, TER measures which face spoke when, and VWER charges a word error when the speaker tag is wrong even if another transcript is correct. This makes attribution part of recognition.
- **What paper reports:** The proposed model reports lower or competitive WER/VWER and strong VTER as the number of overlapping speakers rises, with tags placed before or after each transcription tested explicitly.
- **Limits:** The evidence is bounded to constructed LRS3 mixtures, visible faces, tested overlap counts, and author-reported metrics; natural meetings, missed faces, and long-range turn structure remain open.

