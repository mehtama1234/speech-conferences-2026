# INTERSPEECH 2025 thirty-sixth-pass full-paper notes

Eight official-PDF readings deepen enhancement, multilingual prosody, dysarthric adaptation, low-resource benchmarking, watermark robustness, portable translation, turn-taking, and speech-aware instruction following.

## 1. echo-and-reconstruction

**Paper:** [Analysis and Extension of a Near-End Listening Enhancement Method Based on Long-Term Fractile Noise Statistics](https://www.isca-archive.org/interspeech_2025/villani25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `761672709fb3e769d51b811cef6c83cea9a06a62f2799f3e43a68c36ae941fec`; full text captured.

- **Ordinary problem:** A listener in noise may need speech made clearer after capture, but enhancement should not erase speech or make the result sound unnatural.
- **Why hard:** Noise statistics change over time and a useful near-end method has to estimate what belongs to the noise without relying on a clean reference.
- **Naive attempt:** Use one fixed noise estimate or raise all frequencies equally and assume intelligibility will follow.
- **Central move:** Estimate long-term fractile noise statistics and use them to guide near-end listening enhancement, then test the method against speech and noise conditions.
- **Mechanism:** The paper analyzes and extends a near-end listening-enhancement method based on long-term fractile noise statistics.
- **Conceptual structure:** The method treats noise as a distribution over time rather than a single fixed level; enhancement is constrained by the estimated noise floor so speech structure is not indiscriminately removed.
- **What paper reports:** The paper reports listening-enhancement results for the proposed statistical method and its extension.
- **Limits:** Noise type, recordings, listeners, parameter settings, and perceptual tests limit generalization; improved quality is not identical to improved intelligibility.

## 2. prosody-and-intent

**Paper:** [Multimodal Prosody Modeling: A Use Case for Multilingual Sentence Mode Prediction](https://www.isca-archive.org/interspeech_2025/vlasenko25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `f9ccc84daa4febcbab3a5ff92c9afeca2f5a1f0461a56e70f894afa1bcd2cae9`; full text captured.

- **Ordinary problem:** Sentence mode—such as a question or statement—is carried not only by words but also by prosody, and a useful model should work across languages and modalities.
- **Why hard:** Prosody varies with language, speaker, emotion, and recording; text alone misses timing and pitch while audio alone can miss lexical structure.
- **Naive attempt:** Predict sentence mode from text or one acoustic feature and assume the same cue works across languages.
- **Central move:** Combine multimodal prosody representations and evaluate multilingual sentence-mode prediction under the actual interaction between words, voice, and language.
- **Mechanism:** The study presents multimodal prosody modeling for multilingual sentence-mode prediction.
- **Conceptual structure:** Sentence mode is a joint signal: lexical content provides one constraint while pitch, timing, and energy provide another, and disagreement between them is informative rather than noise.
- **What paper reports:** The paper reports multilingual multimodal prosody-modeling results for sentence-mode prediction.
- **Limits:** Languages, labels, speaker balance, modality quality, and task definition bound the claim; sentence mode is not a complete model of intent.

## 3. clinical-and-assistive-speech

**Paper:** [Personalized Fine-Tuning with Controllable Synthetic Speech from LLM-Generated Transcripts for Dysarthric Speech Recognition](https://www.isca-archive.org/interspeech_2025/wagner25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `0f321efea0c245e9c9fad89ac1fdf6135bfbff22c5e586a920c503888842289e`; full text captured.

- **Ordinary problem:** A recognizer for dysarthric speech should adapt to a particular speaker even when only limited recordings are available.
- **Why hard:** Dysarthria changes the relation between intended words and acoustic realization; synthetic data can add coverage but can also repeat the wrong errors or sound unlike the speaker.
- **Naive attempt:** Fine-tune on a small personal set only, or add generic synthetic speech without controlling what variation it contributes.
- **Central move:** Use LLM-generated transcripts to create controllable synthetic speech and personalize fine-tuning for the target speaker, then measure recognition under speaker-specific conditions.
- **Mechanism:** The paper studies personalized fine-tuning with controllable synthetic speech for dysarthric speech recognition.
- **Conceptual structure:** Personalization is a data-design problem: synthetic examples are useful only when their transcript, pronunciation variation, and speaker control support the target speaker rather than dilute them.
- **What paper reports:** The paper reports recognition results for personalized adaptation using controllable synthetic data.
- **Limits:** Speaker cohort, dysarthria type, transcript generation, synthesis quality, and adaptation budget limit generalization or clinical claims.

## 4. low-resource-and-data-creation

**Paper:** [The Faetar Speech Recognition Benchmark](https://www.isca-archive.org/interspeech_2025/ong25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `09a5323c1f73cf0215459bcc86d80b04ed3ec63db55bf4c49e725b649485afcd`; full text captured.

- **Ordinary problem:** A low-resource language needs an honest speech-recognition benchmark before claims about progress can be compared.
- **Why hard:** Small corpora make train/test estimates unstable, spelling and dialect choices affect labels, and a benchmark can expose gaps without solving data scarcity.
- **Naive attempt:** Report one model score on a tiny corpus and treat it as a general language capability estimate.
- **Central move:** Build the Faetar speech-recognition benchmark with documented recordings, splits, transcripts, and evaluation so later systems can be compared on the same problem.
- **Mechanism:** The paper introduces the Faetar Speech Recognition Benchmark.
- **Conceptual structure:** Benchmark construction is part of scientific knowledge: the dataset fixes what counts as an error and makes future improvements distinguishable from changes in collection or split.
- **What paper reports:** The paper reports the benchmark resources and baseline recognition results for Faetar.
- **Limits:** Corpus size, speakers, dialect coverage, transcription conventions, and split design bound conclusions about the wider language community.

## 5. privacy-security-and-accountability

**Paper:** [A Comprehensive Real-World Assessment of Audio Watermarking Algorithms: Will They Survive Neural Codecs?](https://www.isca-archive.org/interspeech_2025/ozer25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `a876829819a916551e8945bcf26b155d54c41be474020b7b1e099334bef4cf14`; full text captured.

- **Ordinary problem:** An audio watermark should survive ordinary processing and neural codecs while remaining detectable, otherwise it cannot support provenance or accountability in real systems.
- **Why hard:** Compression and generative codecs intentionally alter waveform details; a watermark can be detectable in clean audio yet disappear after the transformations people actually use.
- **Naive attempt:** Test only clean files or assume a watermark that survives one codec survives every neural codec.
- **Central move:** Evaluate audio-watermarking algorithms under a broad real-world transformation suite, including neural codecs, and compare detectability and audio quality.
- **Mechanism:** The paper provides a comprehensive real-world assessment of audio watermarking algorithms and asks whether they survive neural codecs.
- **Conceptual structure:** Robustness is a chain of transformations: a watermark claim is meaningful only over an explicit threat/process set, with detectability balanced against audible distortion.
- **What paper reports:** The paper reports comparative survival and failure patterns across watermarking methods and neural codecs.
- **Limits:** Algorithms, codec versions, payloads, thresholds, and attack suite bound the result; survival in tested codecs is not universal tamper resistance.

## 6. multilingual-and-crosslingual

**Paper:** [Simultaneous Speech Translation Integrated Compact Multiple Sound Spot Synthesis System On A Laptop Carried Out With A Backpack](https://www.isca-archive.org/interspeech_2025/okamoto25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `a9663a91960630dcf06cd30e0044d8f153e52f7deaae90b7a4665ae7115ee98c`; full text captured.

- **Ordinary problem:** A compact system should translate simultaneous speech and produce multiple sound spots on a laptop carried in a backpack, without assuming a server or a quiet turn-taking environment.
- **Why hard:** Simultaneous speech translation combines overlap, latency, translation uncertainty, and spatial/audio output under tight compute and mobility constraints.
- **Naive attempt:** Wait for a complete utterance, send it to a large remote system, or treat translation and sound placement as separate problems.
- **Central move:** Integrate simultaneous speech translation with compact multiple-sound-spot synthesis in a portable system and evaluate the complete interaction loop.
- **Mechanism:** The paper presents a simultaneous speech-translation system integrated with compact multiple sound-spot synthesis on a laptop carried in a backpack.
- **Conceptual structure:** The system boundary is the product: recognition, translation, timing, and spatialized output must jointly meet latency and resource constraints rather than optimize isolated modules.
- **What paper reports:** The paper reports an integrated portable-system demonstration and evaluation.
- **Limits:** Language pair, overlap conditions, hardware, latency measurement, and user setting limit generalization to broad simultaneous conversation.

## 7. dialogue-and-turn-taking

**Paper:** [Visual Cues Support Robust Turn-taking Prediction in Noise](https://www.isca-archive.org/interspeech_2025/oconnorrussell25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `f7188f142b508f1d0736014ff2eb2e21a493d32bc8674eb3364c2ca6d584922f`; full text captured.

- **Ordinary problem:** People use gaze and other visible cues to signal that a turn is ending or beginning, especially when noise makes audio timing unreliable.
- **Why hard:** Turn-taking is a coupled prediction-and-action problem: visual cues can arrive before words finish, while noise corrupts the acoustic evidence and social norms vary.
- **Naive attempt:** Predict the next turn from audio alone or treat a detected pause as a universal handoff signal.
- **Central move:** Add visual cues to turn-taking prediction and test whether they make decisions more robust in noise.
- **Mechanism:** The study evaluates visual cues for robust turn-taking prediction in noise.
- **Conceptual structure:** A turn is a coordination event between people, not merely a boundary in a waveform; combining channels lets one cue compensate when another is degraded.
- **What paper reports:** The paper reports that visual cues support more robust turn-taking prediction under noisy conditions.
- **Limits:** Participants, camera viewpoint, interaction task, noise type, timing labels, and model latency bound the claim; a lab cue is not a universal conversational rule.

## 8. grounding-and-action

**Paper:** [Speech-IFEval: Evaluating Instruction-Following and Quantifying Catastrophic Forgetting in Speech-Aware Language Models](https://www.isca-archive.org/interspeech_2025/lu25c_interspeech.html)
**Evidence:** D3; PDF SHA-256 `2ac1c2c1da9febb888cb62b28f31feee0df4798f27e8475d0813205687d08499`; full text captured.

- **Ordinary problem:** A speech-aware language model should follow spoken instructions and retain earlier abilities after learning new ones.
- **Why hard:** Instruction following can improve while unrelated skills are forgotten; speech adds recognition errors and modality-specific variation to the usual language-model tradeoff.
- **Naive attempt:** Measure only new-task accuracy or train on new instruction data and assume old abilities remain intact.
- **Central move:** Use Speech-IFEval to test instruction-following behavior and quantify catastrophic forgetting across speech-aware tasks.
- **Mechanism:** The paper introduces Speech-IFEval and evaluates instruction-following and forgetting in speech-aware language models.
- **Conceptual structure:** Evaluation must pair compliance with retention: a model that follows a new command by losing old behavior has shifted capability rather than simply improved it.
- **What paper reports:** The paper reports benchmark results for spoken instruction following and catastrophic forgetting.
- **Limits:** Task suite, speech recognition quality, prompts, model families, and training order bound the conclusions; benchmark retention is not proof of reliable deployment behavior.

