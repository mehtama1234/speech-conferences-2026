# INTERSPEECH 2025 forty-third-pass full-paper notes

Eight official-PDF readings deepen hybrid ASR sampling, duplex speech-to-speech models, deepfake generalization, articulatory variation, emotion-consistent editing, bandwidth extension, multilingual tokens, and embodied agents.

## 1. low-resource-and-data-creation

**Paper:** [Hybrid Data Sampling for ASR: Integrating Acoustic Diversity and Transcription Uncertainty](https://www.isca-archive.org/interspeech_2025/hiruta25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `913e88bbe1eb7c06bc13222f3c7d69778a84276fa9cbc8ac75419dffe40f99ab`; full text captured.

- **Ordinary problem:** An ASR training set should cover acoustic diversity and should spend labeling effort where the transcription is uncertain.
- **Why hard:** Random sampling can overrepresent easy or similar speech, while uncertainty-only sampling can repeat rare errors without broad acoustic coverage.
- **Naive attempt:** Sample randomly, or rank clips by model uncertainty alone and call the resulting set diverse.
- **Central move:** Combine acoustic-diversity measures with transcription uncertainty when selecting training data, then test the effect on ASR.
- **Mechanism:** The paper proposes hybrid data sampling for ASR by integrating acoustic diversity and transcription uncertainty.
- **Conceptual structure:** Data selection is a coverage-allocation problem: diversity broadens the conditions seen, while uncertainty targets the model's unresolved boundary.
- **What paper reports:** The paper reports ASR improvements from hybrid sampling relative to the tested selection strategies.
- **Limits:** Acoustic representation, uncertainty estimator, corpus, budget, language, and split bound the result; a sampling score is not a complete measure of data value.

## 2. dialogue-and-turn-taking

**Paper:** [Efficient and Direct Duplex Modeling for Speech-to-Speech Language Model](https://www.isca-archive.org/interspeech_2025/hu25f_interspeech.html)
**Evidence:** D3; PDF SHA-256 `16f0bf9ad75a7eb22bfd15126642ad0103c3f1b1ca776e2868eabdcf35b404e4`; full text captured.

- **Ordinary problem:** A speech-to-speech language model in a duplex conversation must listen and speak at overlapping times without losing the current turn or waiting for a full utterance.
- **Why hard:** Duplex interaction couples streaming recognition, generation, interruption, and turn timing; a model optimized for one direction can block or talk over the other.
- **Naive attempt:** Use a turn-taking pipeline that waits for end-of-speech or run separate listen and speak models with no shared state.
- **Central move:** Build an efficient direct duplex model that represents incoming and outgoing speech jointly and evaluates real-time speech-to-speech behavior.
- **Mechanism:** The paper studies efficient and direct duplex modeling for speech-to-speech language models.
- **Conceptual structure:** Duplexity is a control problem over concurrent streams: the model must decide what to retain, when to respond, and when to yield while generating speech.
- **What paper reports:** The paper reports efficiency and interactive speech-to-speech results for the duplex model.
- **Limits:** Latency, overlap, interruptions, model size, dialogue tasks, and evaluation protocol bound the result; a real-time demo is not robust open-ended conversation.

## 3. privacy-security-and-accountability

**Paper:** [From Sharpness to Better Generalization for Speech Deepfake Detection](https://www.isca-archive.org/interspeech_2025/huang25e_interspeech.html)
**Evidence:** D3; PDF SHA-256 `1f3bedd0a4a47b9dc759e9a610c67464502349dbf7e4fb107c8d7ce4f90f98c9`; full text captured.

- **Ordinary problem:** A speech deepfake detector should generalize to unseen generators and conditions rather than becoming sharp only on the training attacks.
- **Why hard:** Sharp decision boundaries can fit artifacts specific to known generators; improving training fit may reduce performance when the attack distribution changes.
- **Naive attempt:** Optimize closed-set accuracy and assume a sharper classifier is more discriminative under every attack.
- **Central move:** Study how sharpness relates to deepfake-detector generalization and use training changes that improve the boundary's transfer to unseen attacks.
- **Mechanism:** The paper studies moving from sharpness to better generalization for speech deepfake detection.
- **Conceptual structure:** Generalization depends on the geometry of the learned boundary, not just its training margin; the relevant test is behavior on new attack sources.
- **What paper reports:** The paper reports deepfake-detection generalization results linked to sharpness and the proposed training approach.
- **Limits:** Attack types, datasets, sharpness measure, training recipe, and open-set split bound the claim; no benchmark proves future attack coverage.

## 4. source-filter-production

**Paper:** [Articulatory variations in Apical Vowels in Southwestern Mandarin](https://www.isca-archive.org/interspeech_2025/huang25f_interspeech.html)
**Evidence:** D3; PDF SHA-256 `a6f165ba92d34562837de5435a7a3e4309c2d132785ac45bc1eb3a1babc135fd`; full text captured.

- **Ordinary problem:** Speakers with different articulatory habits can produce similar apical vowels, but the physical movements behind those sounds may differ across Southwestern Mandarin speakers.
- **Why hard:** Tongue shape, place, and coarticulation interact, and acoustic similarity hides multiple articulatory solutions.
- **Naive attempt:** Describe the vowel only by formants or assume one acoustic target has one tongue configuration.
- **Central move:** Measure articulatory variation in apical vowels and relate it to acoustic outcomes across Southwestern Mandarin speakers.
- **Mechanism:** The paper analyzes articulatory variations in apical vowels in Southwestern Mandarin.
- **Conceptual structure:** The sound-to-movement mapping is underdetermined: production data reveal which physical differences are tolerated while the acoustic category stays recognizable.
- **What paper reports:** The paper reports articulatory variation and its acoustic relationships for the studied apical vowels.
- **Limits:** Speakers, dialect region, imaging or measurement method, vowel context, and sample size limit generalization; variation is not pathology.

## 5. prosody-and-interactive-control

**Paper:** [Towards Emotionally Consistent Text-Based Speech Editing: Introducing EmoCorrector and The ECD-TSE Dataset](https://www.isca-archive.org/interspeech_2025/liu25c_interspeech.html)
**Evidence:** D3; PDF SHA-256 `21bc34bb7ab4d79145a6c901857b937ae7b3993bb475fb572a938cdd16a41db0`; full text captured.

- **Ordinary problem:** When editing text-based speech, changing a word should preserve the intended emotion and keep the new audio emotionally consistent with its context.
- **Why hard:** Text edits can alter sentiment, emphasis, and prosody at once; a locally fluent replacement may sound emotionally wrong next to surrounding speech.
- **Naive attempt:** Replace the text and synthesize the whole sentence, or optimize word correctness without an emotion-consistency check.
- **Central move:** Create an emotion-consistent speech-editing task and model that preserves affect across the edited span and its context.
- **Mechanism:** EmoCorrector and the ECD-TSE dataset target emotionally consistent text-based speech editing.
- **Conceptual structure:** Editing has two invariants: linguistic content must change as requested, while speaker identity and emotional trajectory must remain coherent around the change.
- **What paper reports:** The paper reports dataset and model results for emotionally consistent speech editing.
- **Limits:** Emotion labels, edit types, speakers, context, synthesis model, and perceptual evaluation bound the claim; emotional consistency is listener- and culture-dependent.

## 6. echo-and-reconstruction

**Paper:** [HWB-Net: A Novel High-Performance and Efficient Hybrid Waveform Bandwidth Extension Method](https://www.isca-archive.org/interspeech_2025/liu25d_interspeech.html)
**Evidence:** D3; PDF SHA-256 `a40ebc29a71477f91b9f6a946666e24cb3636f16500c89d73bd8fef0339e04c0`; full text captured.

- **Ordinary problem:** A bandwidth-limited recording can sound muffled; a bandwidth-extension model should restore useful high-frequency detail without inventing harsh or speaker-inconsistent content.
- **Why hard:** The missing band is not uniquely determined by the low band, and waveform metrics may reward artifacts that listeners dislike.
- **Naive attempt:** Copy the low-band waveform or add fixed high-frequency noise and assume the result is natural.
- **Central move:** Use a hybrid waveform bandwidth-extension network and evaluate reconstruction quality, speech content, and perceptual naturalness.
- **Mechanism:** HWB-Net is a high-performance efficient hybrid waveform bandwidth-extension method.
- **Conceptual structure:** Bandwidth extension is constrained synthesis: the model predicts plausible missing detail from the observed signal while preserving timing and identity in the known band.
- **What paper reports:** The paper reports quality and efficiency results for HWB-Net on bandwidth-extension tests.
- **Limits:** Bandwidth limit, speakers, noise, training targets, metrics, and listening protocol bound the result; plausible detail is not recovered ground truth.

## 7. multilingual-and-crosslingual

**Paper:** [LIST: Language-Independent Speech Token for Multilingual Speech Synthesis with Language Models](https://www.isca-archive.org/interspeech_2025/liu25o_interspeech.html)
**Evidence:** D3; PDF SHA-256 `4d4bc5177e2a91991c6585fc116e880e146a75587e274658b21f48ee4411092a`; full text captured.

- **Ordinary problem:** A multilingual speech synthesizer needs token units that can be shared across languages while still preserving language-specific pronunciation and rhythm.
- **Why hard:** Separate vocabularies waste capacity, while a universal token can erase distinctions or make the language model confuse languages.
- **Naive attempt:** Train one token set per language or force all languages into a text-like universal code without testing interference.
- **Central move:** Learn a language-independent speech token and use it with language-model synthesis across multiple languages.
- **Mechanism:** LIST is a language-independent speech token for multilingual speech synthesis with language models.
- **Conceptual structure:** The token is a cross-language interface: shared units carry reusable speech structure, while language conditioning reconstructs the differences needed for intelligible output.
- **What paper reports:** The paper reports multilingual synthesis quality and cross-language token behavior for LIST.
- **Limits:** Languages, token rate, codebook, speakers, conditioning, and evaluation metrics bound the claim; shared tokens do not guarantee equal quality.

## 8. grounding-and-action

**Paper:** [GenECA: A General-Purpose Framework for Real-Time Adaptive Multimodal Embodied Conversational Agents](https://www.isca-archive.org/interspeech_2025/patapati25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `986327dab02e0ee3665356ac5a553c859d5d007ec880b85e91563aad5299e9de`; full text captured.

- **Ordinary problem:** An embodied conversational agent should adapt its spoken response to what a person says, sees, and does while the interaction is happening.
- **Why hard:** Multimodal inputs arrive at different times and the agent must keep a coherent conversational state while meeting real-time limits.
- **Naive attempt:** Fuse all sensors once per turn or use a scripted avatar with fixed responses and call it adaptive.
- **Central move:** Build a general-purpose real-time multimodal embodied-agent framework that updates perception, dialogue, action, and speech together.
- **Mechanism:** GenECA is a framework for real-time adaptive multimodal embodied conversational agents.
- **Conceptual structure:** Embodied conversation is a closed loop: perception changes the state, the state selects language and action, and the agent's output changes the next observation.
- **What paper reports:** The paper reports real-time adaptive-agent behavior across its tested multimodal interaction settings.
- **Limits:** Sensors, embodiment, latency, dialogue tasks, user studies, and policy constraints bound the claim; a framework demonstration is not human-level social understanding.

