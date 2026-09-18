# INTERSPEECH 2025 fortieth-pass full-paper notes

Eight official-PDF readings deepen articulatory feedback, lightweight anti-spoofing, transducer decoding, phonetic-acoustic tokens, dialogue-state context, articulator-space translation, audiovisual grounding, and emphasis-emotion synthesis.

## 1. source-filter-production

**Paper:** [PERCEPT-US: A Multimodal American English Child Speech Corpus Specialized for Articulatory Feedback](https://www.isca-archive.org/interspeech_2025/eads25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `d39a7dfdfb91d7ff5da63f23efef82e847b007fe0f44b266ca08e8eb9455f981`; full text captured.

- **Ordinary problem:** A child learning to change articulation needs feedback that connects what they feel and see with how their speech sounds.
- **Why hard:** Articulation is hidden, children vary in development, and feedback must align audio, visual movement, and a usable teaching target without overwhelming the learner.
- **Naive attempt:** Show a waveform or give a generic pronunciation score and assume it identifies the movement to change.
- **Central move:** Build a multimodal American English child-speech corpus specialized for articulatory feedback, with synchronized speech and articulatory information.
- **Mechanism:** PERCEPT-US provides a multimodal child speech corpus designed for articulatory feedback.
- **Conceptual structure:** The corpus makes a hidden motor target observable: acoustic output can be related to articulator configuration and learner-facing feedback rather than treated as an isolated sound label.
- **What paper reports:** The paper reports corpus resources and articulatory-feedback-oriented evaluation for American English child speech.
- **Limits:** Speakers, ages, tasks, sensor alignment, labels, and corpus size limit generalization; a resource does not itself establish learning or clinical benefit.

## 2. privacy-security-and-accountability

**Paper:** [LitMAS: A Lightweight and Generalized Multi-Modal Anti-Spoofing Framework for Biometric Security](https://www.isca-archive.org/interspeech_2025/gorthi25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `bdebf2a582709e76c75b04735c62e0c719a6378d7a1231e463f204c29f8d5e6b`; full text captured.

- **Ordinary problem:** Biometric anti-spoofing must reject attacks across modalities and conditions while staying light enough for real security systems.
- **Why hard:** Attack traces differ by sensor and generator, and a heavy multimodal model can be accurate but too slow or too specialized to deploy.
- **Naive attempt:** Train a modality-specific detector or use a large model and evaluate only on the attack types seen during training.
- **Central move:** Combine lightweight modality-aware representations with generalized anti-spoofing features and test cross-condition biometric security.
- **Mechanism:** LitMAS is a lightweight generalized multimodal anti-spoofing framework for biometric security.
- **Conceptual structure:** Security is a coverage problem: the model must learn signs of manipulation that survive changes in modality and attack source, while the resource budget constrains the detector itself.
- **What paper reports:** The paper reports generalized multimodal anti-spoofing performance with a lightweight framework.
- **Limits:** Biometric modalities, attacks, datasets, fusion, thresholds, and compute budget bound the result; benchmark generalization is not security certification.

## 3. low-resource-and-data-creation

**Paper:** [Pushing the Limits of Beam Search Decoding  for Transducer-based ASR models](https://www.isca-archive.org/interspeech_2025/grigoryan25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `c258bb48da5a266ef648bca8979f53c611efe9e0fe3bdb6de364ccb56d65fa5e`; full text captured.

- **Ordinary problem:** An ASR decoder must choose a likely word sequence efficiently, but beam search can miss a better path or spend too much computation on unhelpful alternatives.
- **Why hard:** Transducer scores are local while the best sequence is global; beam width, pruning, and length effects interact with streaming constraints.
- **Naive attempt:** Increase the beam indefinitely or use greedy decoding and assume the accuracy/latency tradeoff is universal.
- **Central move:** Analyze and improve beam-search decoding for transducer ASR, testing how search choices affect accuracy and computation.
- **Mechanism:** The paper pushes the limits of beam-search decoding for transducer-based ASR models.
- **Conceptual structure:** Decoding is an inference budget: the beam is a controlled approximation to sequence search, and improvements come from spending computation where competing hypotheses remain plausible.
- **What paper reports:** The paper reports decoding accuracy and efficiency findings for transducer ASR across the tested search settings.
- **Limits:** Model, language, beam policy, pruning, hardware, and streaming setup bound the result; a better beam does not remove acoustic or language-model errors.

## 4. echo-and-reconstruction

**Paper:** [PAST: Phonetic-Acoustic Speech Tokenizer](https://www.isca-archive.org/interspeech_2025/hartuv25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `cab000ab53335789ced2950b728895340a8dc1aaf40ff1ef9f8b1e1bd1dc1f04`; full text captured.

- **Ordinary problem:** A speech tokenizer should turn sound into compact units that preserve the information a downstream speech model actually needs.
- **Why hard:** Acoustic detail, phonetic identity, speaker identity, and temporal precision compete for a limited token budget; reconstruction quality alone may reward irrelevant detail.
- **Naive attempt:** Use waveform compression or text-like units and assume the best reconstruction tokenizer is the best speech representation.
- **Central move:** Build a phonetic-acoustic tokenizer and evaluate whether its tokens capture both speech sound structure and useful phonetic distinctions.
- **Mechanism:** PAST is a phonetic-acoustic speech tokenizer.
- **Conceptual structure:** Tokenization is a choice about what survives discretization: units should preserve acoustically grounded, phonetic information while discarding redundant waveform variation.
- **What paper reports:** The paper reports tokenizer quality and downstream speech-representation results for the proposed phonetic-acoustic units.
- **Limits:** Token rate, codebook, languages, speakers, reconstruction target, and downstream tasks bound the claim; discrete units are not automatically linguistically complete.

## 5. dialogue-and-turn-taking

**Paper:** [Factors affecting the in-context learning abilities of LLMs for dialogue state tracking](https://www.isca-archive.org/interspeech_2025/hegde25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `adbf75997fe61e0dcccb324b8b4a83759abd5e33edf5615fbc9d288512a07dbd`; full text captured.

- **Ordinary problem:** A dialogue-state tracker should use examples in context effectively, but its ability to learn from a few demonstrations may depend on how the dialogue and prompts are arranged.
- **Why hard:** State labels, turn order, domain vocabulary, and example selection can change what the model appears to infer from context.
- **Naive attempt:** Measure one prompt format and attribute the result to general in-context learning ability.
- **Central move:** Systematically vary dialogue-state-tracking factors such as demonstrations, domain, and context to identify which conditions support or break in-context learning.
- **Mechanism:** The paper studies factors affecting the in-context learning abilities of LLMs for dialogue state tracking.
- **Conceptual structure:** In-context learning is an interaction between model prior and task presentation: the examples are part of the effective program and must be analyzed as such.
- **What paper reports:** The paper reports factor-level findings on in-context dialogue-state tracking.
- **Limits:** Model family, prompt, domains, state schema, demonstration order, and context length bound the result; prompt sensitivity is not a stable conversational capability.

## 6. multilingual-and-crosslingual

**Paper:** [ArticulateX: End-to-End Monolingual Speech Translation in Articulator Space](https://www.isca-archive.org/interspeech_2025/kumar25c_interspeech.html)
**Evidence:** D3; PDF SHA-256 `ad88b9e82119373fcc3596ceafb860ddafc50a6342923c50240909bd5911d912`; full text captured.

- **Ordinary problem:** Speech translation can use articulator movement as an intermediate signal, especially when the sound alone is ambiguous or the target language lacks data.
- **Why hard:** Articulator space is not directly observed in ordinary speech, and translation must preserve meaning while passing through a representation with its own measurement errors.
- **Naive attempt:** Translate acoustic features directly or force a text transcript and assume articulation adds nothing.
- **Central move:** Build an end-to-end monolingual speech-translation system that represents speech in articulator space and tests whether the intermediate structure helps.
- **Mechanism:** ArticulateX is an end-to-end monolingual speech translation system operating in articulator space.
- **Conceptual structure:** The proposed bridge changes the unit of translation: vocal-tract movement is treated as a structured intermediate constraint between sound and language.
- **What paper reports:** The paper reports speech-translation results for the articulator-space system in its tested monolingual setting.
- **Limits:** Language, corpus, articulatory estimation, model, references, and evaluation bound generalization; an intermediate representation is not proof of human-like translation.

## 7. grounding-and-action

**Paper:** [Bridging Audio and Vision: Zero-Shot Audiovisual Segmentation by Connecting Pretrained Models](https://www.isca-archive.org/interspeech_2025/lee25b_interspeech.html)
**Evidence:** D3; PDF SHA-256 `a32f88413fcdf3a61edaacf056e4c82e60474bc3d0383c127c212ad02ea35366`; full text captured.

- **Ordinary problem:** An audio-visual system should identify the regions in a video associated with a sound, even for categories or scenes it did not see during training.
- **Why hard:** Audio and vision have different timing and semantics; zero-shot matching can confuse co-occurrence with the object that actually produced the sound.
- **Naive attempt:** Detect objects from vision alone or train a closed-set audiovisual segmenter and reject unseen categories.
- **Central move:** Connect pretrained audio and vision models so shared representations can guide zero-shot audiovisual segmentation.
- **Mechanism:** The paper studies zero-shot audiovisual segmentation by bridging pretrained audio and vision models.
- **Conceptual structure:** Segmentation is grounded association: the system must align a sound event with a spatial region using cross-modal evidence rather than merely classify the clip.
- **What paper reports:** The paper reports zero-shot audiovisual segmentation results for the connected pretrained models.
- **Limits:** Datasets, categories, synchronization, pretrained models, and segmentation labels bound the result; co-occurrence does not establish physical source identity.

## 8. prosody-and-interactive-control

**Paper:** [EME-TTS: Unlocking the Emphasis and Emotion Link in Speech Synthesis](https://www.isca-archive.org/interspeech_2025/li25i_interspeech.html)
**Evidence:** D3; PDF SHA-256 `d858d8e97d8a95711eaed9d2abd394de9fff2311cd3f28728b8bb30c805fbc0f`; full text captured.

- **Ordinary problem:** A TTS system should make emphasis and emotion controllable together, because stressing a word changes how emotion is perceived and emotion changes which emphasis sounds natural.
- **Why hard:** Text, prosody, and affect are entangled; independent controls can conflict or produce an emphasized contour that does not fit the intended emotion.
- **Naive attempt:** Add an emotion label after synthesis or control pitch and energy independently with no relation to the emphasized word.
- **Central move:** Model the link between emphasis and emotion explicitly so text position, prosody, and affect can be jointly controlled.
- **Mechanism:** EME-TTS targets the emphasis-emotion link in speech synthesis.
- **Conceptual structure:** Expressive synthesis is a constrained coordination problem: emphasis is local and linguistic, emotion is broader and affective, and the system must make their interaction coherent.
- **What paper reports:** The paper reports expressive TTS quality and controllability for emphasis and emotion in the tested evaluations.
- **Limits:** Languages, speakers, labels, text prompts, control ranges, and subjective raters bound the claim; controllability does not guarantee natural or culturally appropriate expression.

