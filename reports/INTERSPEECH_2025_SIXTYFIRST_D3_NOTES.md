# INTERSPEECH 2025 sixty-first-pass full-paper notes

Three additional readings extend comparison across dialect description, individualized accessibility, and child-speech recognition.

## 1. accent-and-cultural-boundaries

**Paper:** [Tonal Contrasts in the Malipo Variety of the Mienic Language](https://www.isca-archive.org/interspeech_2025/du25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `1d5ffb02b45ae9ecf1f928ea612f3f9b4f0ed1a9f5166327c05545a99a3fbd37`; full text captured.

- **Ordinary problem:** A speech system should describe and recognize a language variety without erasing the contrast that makes the variety meaningful.
- **Why hard:** Small phonetic inventories and limited documentation make variation easy to mistake for noise or a universal norm.
- **Naive attempt:** Collapse the variety into a standard-language model and report only pooled accuracy.
- **Central move:** Measure tonal contrasts in the Malipo variety as an object of speech description and evaluation.
- **Mechanism:** Contrastive measurements expose which acoustic distinctions carry linguistic information.
- **Mathematical/conceptual structure:** The paper treats dialect-and-variety as a structured evidence-to-decision problem: Contrastive measurements expose which acoustic distinctions carry linguistic information.
- **What paper reports:** The paper reports an empirical study of tonal contrasts in a Mienic variety.
- **Limits:** Speaker sample, elicitation design, tonal context, and language-specific scope bound transfer.

## 2. human-centered-evaluation

**Paper:** [Individualized speech enhancement for hearing-impaired listeners](https://www.isca-archive.org/interspeech_2025/wen25b_interspeech.html)
**Evidence:** D3; PDF SHA-256 `b5fba23b94cbcba797f70674b5953d359a04599f1a31ab66413fcac146a1d2f1`; full text captured.

- **Ordinary problem:** Speech enhancement should improve access for a particular hearing-impaired listener, not merely optimize an average signal metric.
- **Why hard:** Hearing loss profiles differ, and a global enhancer can preserve the wrong cues.
- **Naive attempt:** Optimize one pooled enhancement objective and assume its score represents every listener.
- **Central move:** Individualize enhancement around the listener's hearing profile and evaluate the resulting speech access.
- **Mechanism:** Listener-specific constraints become the target of enhancement rather than the average waveform.
- **Mathematical/conceptual structure:** The paper treats accessibility-fit as a structured evidence-to-decision problem: Listener-specific constraints become the target of enhancement rather than the average waveform.
- **What paper reports:** The paper reports individualized speech enhancement for hearing-impaired listeners.
- **Limits:** Hearing profiles, listener numbers, fitting procedure, materials, and subjective protocol bound transfer.

## 3. acoustic-unit-mapping

**Paper:** [Improving Child Speech Recognition and Reading Mistake Detection by Using Prompts](https://www.isca-archive.org/interspeech_2025/gao25c_interspeech.html)
**Evidence:** D3; PDF SHA-256 `0993342227593646355656df40fc35a664daeb184c7daff1bf5929c7c41e76d5`; full text captured.

- **Ordinary problem:** Child speech recognition and reading-mistake detection should connect variable child acoustics to intended linguistic units and learning outcomes.
- **Why hard:** Children differ in articulation, age, reading skill, and pronunciation, so adult-trained acoustic boundaries are unreliable.
- **Naive attempt:** Apply an adult ASR model and treat every mismatch as an ordinary recognition error.
- **Central move:** Use prompts to condition recognition and mistake detection on the child's intended reading task.
- **Mechanism:** Prompt information narrows the hypothesis space: acoustic evidence is interpreted with task and expected linguistic content.
- **Mathematical/conceptual structure:** The paper treats pronunciation-variation as a structured evidence-to-decision problem: Prompt information narrows the hypothesis space: acoustic evidence is interpreted with task and expected linguistic content.
- **What paper reports:** The paper reports improving child speech recognition and reading-mistake detection using prompts.
- **Limits:** Child age, language, prompt design, annotation policy, and error definitions bound transfer.

