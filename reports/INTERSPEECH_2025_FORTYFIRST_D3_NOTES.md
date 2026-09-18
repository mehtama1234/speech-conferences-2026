# INTERSPEECH 2025 forty-first-pass full-paper notes

Eight official-PDF readings deepen voice quality and tone processing, low-resource Middle Eastern ASR, triadic gaze, secure speaker verification, hallucination-free editing, multilingual translation, expressive style retrieval, and avatar gestures.

## 1. source-filter-production

**Paper:** [Creaky Voice Facilitates More Efficient Phonological Processing of Mandarin Tone 3](https://www.isca-archive.org/interspeech_2025/fan25b_interspeech.html)
**Evidence:** D3; PDF SHA-256 `66fe70b6b48b5aa26b36ad43d8865b2571130b519a3f357cd3eb61e62260eb6a`; full text captured.

- **Ordinary problem:** A listener must recognize Mandarin Tone 3 efficiently even when the voice has a creaky quality that changes the acoustic signal.
- **Why hard:** Tone, voice quality, and phonological context interact; a cue can make processing easier without being the tone itself.
- **Naive attempt:** Use pitch alone or treat creak as irrelevant speaker variation.
- **Central move:** Test whether creaky voice changes the time and accuracy of Tone 3 processing, separating phonological benefit from general listening difficulty.
- **Mechanism:** The paper studies how creaky voice facilitates more efficient phonological processing of Mandarin Tone 3.
- **Conceptual structure:** The speech cue is useful because it changes the listener's inference about a category boundary; processing efficiency is measured behaviorally rather than assumed from an acoustic correlation.
- **What paper reports:** The paper reports behavioral evidence that creaky voice can facilitate Tone 3 processing in the tested Mandarin stimuli.
- **Limits:** Listeners, stimuli, tone context, creak manipulation, and task bound the claim; a processing benefit is not a universal production or perception rule.

## 2. low-resource-and-data-creation

**Paper:** [Automatic Speech Recognition for Low-Resourced Middle Eastern Languages](https://www.isca-archive.org/interspeech_2025/hameed25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `d86d646bd51794bd20b4b19801617990151586086845a6317898818b1a5e17c8`; full text captured.

- **Ordinary problem:** Many Middle Eastern languages need speech recognition but have little transcribed data, tools, or standardized evaluation.
- **Why hard:** Language variety, script, dialect, speaker access, and scarce labels interact; multilingual transfer may help one variety while obscuring another.
- **Naive attempt:** Fine-tune a high-resource recognizer on a tiny sample and report one score without documenting the language or split.
- **Central move:** Build and evaluate ASR resources for low-resourced Middle Eastern languages, making language-specific data and transfer limits explicit.
- **Mechanism:** The paper studies automatic speech recognition for low-resourced Middle Eastern languages.
- **Conceptual structure:** Low-resource ASR is an infrastructure problem as well as a model problem: a documented corpus and baseline expose which errors come from missing data versus model choice.
- **What paper reports:** The paper reports resources, baselines, and recognition results for the covered Middle Eastern languages.
- **Limits:** Language selection, dialect, corpus size, transcription, speakers, and evaluation splits limit generalization across the region.

## 3. dialogue-and-turn-taking

**Paper:** [Gaze-Enhanced Multimodal Turn-Taking Prediction in Triadic Conversations](https://www.isca-archive.org/interspeech_2025/heo25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `872eb41f1b5a7ce0290da61172ca5dce788ac1a13099f67c625fb4427c640061`; full text captured.

- **Ordinary problem:** In a triadic conversation, a person may look at one participant before taking a turn, and a turn-taking model should use that gaze rather than treating the group as one audio stream.
- **Why hard:** Three-way interaction creates competing addressees and overlapping cues; gaze timing can precede speech while being noisy or socially ambiguous.
- **Naive attempt:** Predict turn transitions from audio only or use one global gaze feature for the whole group.
- **Central move:** Add person-specific gaze cues to multimodal turn-taking prediction and test whether they improve decisions in triadic conversations.
- **Mechanism:** The paper studies gaze-enhanced multimodal turn-taking prediction in triadic conversations.
- **Conceptual structure:** Turn-taking is addressed to someone: person-conditioned visual cues resolve part of the interaction structure that an audio-only boundary cannot represent.
- **What paper reports:** The paper reports turn-taking prediction results with gaze enhancement in triadic interaction.
- **Limits:** Participants, camera setup, roles, task, gaze annotation, and latency bound generalization; gaze is a cue, not a deterministic intention signal.

## 4. privacy-security-and-accountability

**Paper:** [Privacy-Preserving Speaker Verification via End-to-End Secure Representation Learning](https://www.isca-archive.org/interspeech_2025/hu25j_interspeech.html)
**Evidence:** D3; PDF SHA-256 `b5d720d46424d9e895ad228ff119aa34391dde79eadfbe4a91078927177cd791`; full text captured.

- **Ordinary problem:** Speaker verification should protect voice representations so a system can compare speakers without exposing a reusable identity embedding.
- **Why hard:** Verification needs a useful similarity signal, but storing or transmitting speaker information creates privacy and attack risks.
- **Naive attempt:** Encrypt storage around an ordinary embedding or remove speaker information so verification becomes impossible.
- **Central move:** Learn secure representations end to end and test the tradeoff between verification accuracy and privacy exposure.
- **Mechanism:** The paper proposes privacy-preserving speaker verification via end-to-end secure representation learning.
- **Conceptual structure:** Privacy is built into the representation rather than added only at storage: the learned object should support the authorized comparison while limiting what an observer can recover.
- **What paper reports:** The paper reports privacy and speaker-verification results for the proposed secure representation learning method.
- **Limits:** Threat model, attacker access, datasets, privacy measure, calibration, and deployment protocol bound the claim; benchmark privacy is not a complete security proof.

## 5. echo-and-reconstruction

**Paper:** [VoiceNoNG: Robust High-Quality Speech Editing Model without Hallucinations](https://www.isca-archive.org/interspeech_2025/huang25c_interspeech.html)
**Evidence:** D3; PDF SHA-256 `4eeb16427268e714fe440e9b49e4e93f97923d44b6ef1d532406f70fab67c7da`; full text captured.

- **Ordinary problem:** Editing a speech recording should change the requested words or sounds without inventing unrelated content or damaging the surrounding voice.
- **Why hard:** An editor must fill a gap using context, but a powerful generator can hallucinate plausible speech that is inconsistent with the speaker, timing, or meaning.
- **Naive attempt:** Regenerate the whole utterance or mask a span and trust unconstrained continuation.
- **Central move:** Build a robust high-quality speech editor whose context use is constrained and evaluate whether edits remain faithful without hallucinations.
- **Mechanism:** VoiceNoNG is a robust high-quality speech-editing model designed to avoid hallucinations.
- **Conceptual structure:** Editing is constrained completion: the model must change a local region while preserving identity, timing, and untouched context, so faithfulness is a separate target from audio quality.
- **What paper reports:** The paper reports speech-editing quality and reduced hallucination behavior for the tested edits.
- **Limits:** Edit type, context length, speaker set, alignment, metrics, and human judgments bound the claim; no-hallucination behavior is not guaranteed under arbitrary prompts.

## 6. multilingual-and-crosslingual

**Paper:** [Novel Parasitic Dual-Scale Modeling for Efficient and Accurate Multilingual Speech Translation](https://www.isca-archive.org/interspeech_2025/le25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `5a2aae41201302d203e55d5b73ee869936000d750b8cf46bd8fbdacf7197131f`; full text captured.

- **Ordinary problem:** A multilingual speech-translation system should serve many languages efficiently while preserving accuracy, rather than duplicating a full model for each direction.
- **Why hard:** Languages have different amounts of data and structures; sharing too much causes interference while separate modules waste parameters.
- **Naive attempt:** Use one monolithic model with uniform capacity or one model per language pair.
- **Central move:** Use a parasitic dual-scale design that shares efficient global structure while preserving language-specific detail for multilingual speech translation.
- **Mechanism:** The paper proposes novel parasitic dual-scale modeling for efficient and accurate multilingual speech translation.
- **Conceptual structure:** The model divides capacity by scale: shared computation handles reusable patterns, while finer or conditional structure protects language-specific translation behavior.
- **What paper reports:** The paper reports multilingual translation accuracy and efficiency improvements for the tested language set.
- **Limits:** Languages, directions, data imbalance, parameter budget, decoding, and metrics bound the result; efficiency on a benchmark is not equal quality for every language.

## 7. prosody-and-interactive-control

**Paper:** [SA-RAS: Speaker-Aware Style Retrieval Augmented Generation for Expressive Zero-Shot Text-to-Speech Synthesis](https://www.isca-archive.org/interspeech_2025/li25t_interspeech.html)
**Evidence:** D3; PDF SHA-256 `a7d249384eed74433d675c8adadb686df2f7d6b348828de52bb4fc52b5f5c112`; full text captured.

- **Ordinary problem:** A zero-shot TTS system should imitate a target speaker while retrieving a speaking style that fits the requested expressive context.
- **Why hard:** Speaker identity and style are entangled; retrieving a style example can improve expressiveness but can also copy unwanted content or confuse whose voice is being produced.
- **Naive attempt:** Use one global style embedding or concatenate a reference clip without separating speaker and style information.
- **Central move:** Use speaker-aware style retrieval-augmented generation so the system retrieves relevant style evidence while maintaining zero-shot speaker identity.
- **Mechanism:** SA-RAS is a speaker-aware style retrieval-augmented method for expressive zero-shot TTS.
- **Conceptual structure:** Style retrieval is constrained by identity: the reference supplies how to speak, while the target speaker supplies who speaks, and generation must keep those roles distinct.
- **What paper reports:** The paper reports expressive quality, speaker similarity, and style-control results for zero-shot synthesis.
- **Limits:** Reference selection, speaker set, style labels, prompts, listening tests, and language bound the claim; style similarity is not a complete account of naturalness.

## 8. grounding-and-action

**Paper:** [Beat gestures made by human-like avatars affect speech perception](https://www.isca-archive.org/interspeech_2025/maran25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `e1c746cb466631956d675031eeb37141ed4c5dd21a1633d3ffa7709fe14f5432`; full text captured.

- **Ordinary problem:** A human-like avatar's beat gesture can change how listeners understand or attend to speech, so gesture is part of the communicative signal rather than decoration.
- **Why hard:** Perception combines timing, visual form, speech content, and expectations about an avatar; a gesture can help one phrase and distract in another.
- **Naive attempt:** Add random gestures or assume a visually human avatar automatically improves speech perception.
- **Central move:** Manipulate beat gestures made by human-like avatars and measure their effect on speech perception under controlled conditions.
- **Mechanism:** The paper studies how beat gestures made by human-like avatars affect speech perception.
- **Conceptual structure:** Gesture functions as timed emphasis: its effect depends on alignment with prosodic or semantic structure, so perception experiments are needed instead of a visual-quality proxy.
- **What paper reports:** The paper reports speech-perception effects of avatar beat gestures in the tested stimuli and listener tasks.
- **Limits:** Avatar design, gesture timing, speech material, participants, and task bound generalization; a laboratory effect is not proof of conversational benefit.

