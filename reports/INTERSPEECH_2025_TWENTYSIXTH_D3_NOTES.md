# INTERSPEECH 2025 twenty-sixth-pass full-paper notes

Eight official-PDF readings deepen dialect change, task conflict, semantic refinement, speech enhancement, interaction analysis, assistive speech, feedback control, and ordered clinical prediction. Results are author-reported and not independently reproduced.

## 1. accent-and-cultural-boundaries

**Paper:** [Lexical competition in the process of Cantonese tone merging: Diverse Impact Mechanisms Across Different Individuals and Tone Pairs](https://www.isca-archive.org/interspeech_2025/li25w_interspeech.html)
**Evidence:** D3; PDF SHA-256 `8864eb4a5a5437ae7a823a5765cc26de015076b80dbfdd1b784d17d6a262e3a4`; full text captured.

- **Ordinary problem:** A tone contrast can merge gradually in a community while individual speakers still preserve or reshape it differently.
- **Why hard:** Word competition can push a speaker away from a merger, but its effect may depend on the tone pair and on how far that speaker has already merged.
- **Naive attempt:** Treat tone change as one uniform process with one lexical effect for every speaker.
- **Central move:** Examine lexical competition separately for each speaker and tone pair, then relate production distributions to the speaker's merger pattern.
- **Mechanism:** Cantonese tone production is measured for speakers with no clear merger, one merged pair, or multiple merged pairs; lexical competition is compared across pairs.
- **Conceptual structure:** The relevant object is an individual, context-conditioned distribution rather than a population average; different effects reveal inhibition, promotion, or no change.
- **What paper reports:** Competition helps maintain contrasts in some speakers, consistently inhibits one pair, has three patterns for another, and has little effect in speakers merging all three tones.
- **Limits:** The Cantonese pairs, speaker groups, lexical measure, and production task bound the result; it is evidence about a change process, not a forecast of every speaker's future pronunciation.

## 2. clinical-and-assistive-speech-1

**Paper:** [Addressing Task Conflicts in Stuttering Detection via MMoE-Based Multi-Task Learning](https://www.isca-archive.org/interspeech_2025/liu25f_interspeech.html)
**Evidence:** D3; PDF SHA-256 `41ff0eed79d90ac7ccab2da8469d8058a3f7b7af6da6300bb5e4e863d0fd4387`; full text captured.

- **Ordinary problem:** A stuttering detector often needs several related outputs, but a feature useful for one symptom can interfere with another task.
- **Why hard:** Shared parameters force tasks with different cues or label frequencies to compete, and a single average loss hides which task is being harmed.
- **Naive attempt:** Train all tasks with one shared representation and one fixed loss weighting.
- **Central move:** Analyze task conflicts explicitly, use rules to separate incompatible signals, and let a mixture of experts route examples to task-relevant submodels.
- **Mechanism:** Rule-based multi-task learning and a multi-mixture-of-experts model are evaluated on stuttering-symptom detection and the 2024 SLT challenge.
- **Conceptual structure:** The model treats task gradients and predictions as competing demands; per-task and average F1 reveal whether collaboration improves the clinical outputs.
- **What paper reports:** The rule-based strategy reports a 19.9% average-F1 gain over baseline and the MMoE strategy a further 7.55% improvement.
- **Limits:** The challenge data, symptom definitions, labels, class balance, and F1 aggregation bound the claim; benchmark gains do not establish clinical reliability or fairness.

## 3. grounding-and-action

**Paper:** [Towards High-Quality LLM-Based Data for French Spontaneous Speech Simplification: an Exo-Refinement Approach](https://www.isca-archive.org/interspeech_2025/ormaechea25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `214e4715b137832e91165306f3f34e1797e1fa51ab7489efa6df6d6ced3d18b8`; full text captured.

- **Ordinary problem:** A reader may need a simpler version of spontaneous speech, but parallel examples are scarce and a fluent rewrite can accidentally change what the speaker meant.
- **Why hard:** One model judging its own rewrite can approve its own semantic errors, while simplicity and meaning preservation pull in different directions.
- **Naive attempt:** Ask one generator to refine itself until the wording sounds simpler.
- **Central move:** Use separate external judges for task-specific dimensions and iterate only when their feedback improves simplicity without losing semantic content.
- **Mechanism:** LLM-generated French speech simplifications are refined by distinct evaluator models and compared with expert simplifications using SARI and COMET.
- **Conceptual structure:** The rewrite is constrained by two targets—simpler form and preserved meaning—so separate judges provide an outside check on the tradeoff.
- **What paper reports:** Mistral-large outperforms tested baselines, Mistral-small becomes competitive after few refinements, SARI improves, and COMET indicates semantic preservation in the reported experiments.
- **Limits:** The languages, prompts, judges, reference simplifications, and automatic metrics bound the result; COMET and SARI are proxies, not a guarantee of accessible or faithful speech.

## 4. noise-enhancement-1

**Paper:** [Model as Loss: A Self-Consistent Training Paradigm](https://www.isca-archive.org/interspeech_2025/phaye25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `94e0c05843fc69c8bf34e867731e6e28b3fd951877ab6636d7a79b8eeba48fa5`; full text captured.

- **Ordinary problem:** An enhancement system should remove noise while keeping the speech properties that matter to perception and downstream tasks.
- **Why hard:** A waveform or spectrum loss treats all deviations similarly, while a generic feature loss may preserve features unrelated to the target task.
- **Naive attempt:** Choose a fixed time-domain or frequency-domain distance and assume its error corresponds to what listeners need.
- **Central move:** Use the same model's encoder as a task-specific loss, forcing enhanced output and clean reference to agree in the model's learned feature space.
- **Mechanism:** A speech-enhancement decoder is trained against features from its own encoder and compared with handcrafted and pretrained deep-feature losses on standard benchmarks.
- **Conceptual structure:** The loss measures consistency in a learned representation rather than raw sample distance; perceptual metrics and out-of-domain tests expose whether that representation transfers.
- **What paper reports:** The paper reports better perceptual quality than pretrained feature losses and robust generalization in both in-domain and out-of-domain tests.
- **Limits:** The encoder, training data, noise conditions, perceptual metrics, and benchmark protocols bound the result; feature agreement is not identical to intelligibility or listener preference.

## 5. dialogue-and-turn-taking

**Paper:** [Assessing the feasibility of Large Language Models for detecting micro-behaviors in team interactions during space missions](https://www.isca-archive.org/interspeech_2025/raut25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `a3b81ba0f325aa9c338caf18c6c6b58284784008dbd50975513bc23b4947f05b`; full text captured.

- **Ordinary problem:** Team communication contains small conversational behaviors that may signal coordination or trouble, but they are rare and their meaning depends on the turn around them.
- **Why hard:** Underrepresented behaviors are easy for a classifier to ignore, and transcripts omit timing, voice quality, and other cues present in audio.
- **Naive attempt:** Fine-tune a text classifier and assume more weighting will recover every rare behavior.
- **Central move:** Compare zero-shot, fine-tuned, paraphrase-augmented, and instruction-following models while keeping the turn as the unit of dialogue-state prediction.
- **Mechanism:** Models classify micro-behaviors in transcripts from simulated space missions, including discouraging speech, under three-way and binary labelings.
- **Conceptual structure:** Macro F1 exposes minority-class failure better than accuracy; the task tests whether language context alone can support interactional labeling.
- **What paper reports:** Encoder-only models struggle with rare behaviors, while an instruction-tuned Llama model reports 44% macro F1 for three-way and 68% for binary classification.
- **Limits:** Simulated missions, transcript quality, label prevalence, model prompting, and macro-F1 targets bound the finding; detected text patterns are not proof of team state or causality.

## 6. clinical-and-assistive-speech-2

**Paper:** [Semantic Processing During Spoken Word Production by Children with Cochlear Implants](https://www.isca-archive.org/interspeech_2025/wang25l_interspeech.html)
**Evidence:** D3; PDF SHA-256 `26ff05eb02b46e3bf0b2eb19de9be45a9be0b7effea408164a4bcb557f55815c`; full text captured.

- **Ordinary problem:** Children with cochlear implants may produce intelligible speech while using different internal routes to select and plan words.
- **Why hard:** Sound production measures alone cannot reveal how semantic competition is handled during word production.
- **Naive attempt:** Compare only pronunciation accuracy and infer normal semantic access from normal-sounding speech.
- **Central move:** Use a picture-word interference task to test whether semantically related distractors slow naming differently for children with implants and hearing peers.
- **Mechanism:** Children with cochlear implants and normal-hearing peers name pictured objects while distractor words vary in semantic relatedness.
- **Conceptual structure:** Naming latency or accuracy under interference is an indirect test of semantic activation; the group contrast separates access strategy from surface articulation.
- **What paper reports:** Normal-hearing children show the typical semantic interference effect, while the implant group does not, consistent with different semantic organization or greater top-down control.
- **Limits:** The group, age, implant history, language, task, and interpretation of interference bound the result; absence of an effect is not a direct measurement of neural organization.

## 7. noise-enhancement-2

**Paper:** [A Novel Deep Learning Framework for Efficient Multichannel Acoustic Feedback Control](https://www.isca-archive.org/interspeech_2025/wu25d_interspeech.html)
**Evidence:** D3; PDF SHA-256 `02587cce87ef16757b6e57ad50308535c94a0b9dd53d8eba70369863644a3b65`; full text captured.

- **Ordinary problem:** In a device with microphones and loudspeakers, the device's own output can return through the room and become a howl that damages speech quality.
- **Why hard:** Feedback is correlated with the device output, changes as the acoustic path changes, and can defeat methods that assume independent stationary noise.
- **Naive attempt:** Apply a fixed noise suppressor or wait for a conventional adaptive filter to converge.
- **Central move:** Combine spatial and temporal processing in a recurrent controller and train it in the feedback loop, with teacher forcing and a Wiener-filter hybrid as alternatives.
- **Mechanism:** A convolutional recurrent network controls multichannel acoustic feedback; in-loop, teacher-forced, and hybrid training are compared in complex acoustic environments.
- **Conceptual structure:** The task is closed-loop control: the output changes the next input, so stability and enhancement must be evaluated together rather than on isolated noisy clips.
- **What paper reports:** The paper reports improved speech enhancement with lower computational demand across the proposed training strategies.
- **Limits:** The device geometry, microphones, loudspeakers, feedback paths, training regime, and metrics bound the result; laboratory suppression does not establish stable operation for every room or device.

## 8. clinical-and-assistive-speech-3

**Paper:** [Leveraging Ordinal Information for Speech-based Depression Classification](https://www.isca-archive.org/interspeech_2025/zuo25_interspeech.html)
**Evidence:** D3; PDF SHA-256 `3410e0cf07603dd689c199aa9c3608bc57a359f959519556f11f76e3d9978cc7`; full text captured.

- **Ordinary problem:** Depression severity comes in ordered levels, but a detector often throws away that order by labeling everyone only depressed or not depressed.
- **Why hard:** A mild case is closer to a moderate case than to no symptoms, and binary loss cannot express that distance.
- **Naive attempt:** Binarize the score and train an ordinary yes/no classifier.
- **Central move:** Create ordered thresholds so the model learns several nested decisions and a latent representation that respects severity order.
- **Mechanism:** Speech-based depression scores are converted into K threshold tasks; an ordinal loss trains the model across these linked boundaries.
- **Conceptual structure:** The target is an ordered scale, not a collection of unrelated labels; threshold consistency lets errors near a boundary differ from errors across the full range.
- **What paper reports:** The ordinal method outperforms reported state-of-the-art depression-detection methods in the paper's experiments.
- **Limits:** The clinical scale, speakers, labels, dataset, threshold choices, and evaluation metrics bound the result; better ordinal prediction is not diagnosis or clinical validation.

