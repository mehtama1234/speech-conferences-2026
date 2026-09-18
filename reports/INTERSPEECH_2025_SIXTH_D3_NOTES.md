# INTERSPEECH 2025 sixth-pass full-paper notes

These four notes use already-captured official PDFs and extend D3 coverage across articulatory inversion, privacy-aware representations, code-switching, and triadic turn-taking. Results remain paper-reported, not independently reproduced.

## 1. sound-and-production/source-filter-production

**Paper:** [Enhancing Acoustic-to-Articulatory Inversion with Multi-Target Pretraining for Low-Resource Settings](https://www.isca-archive.org/interspeech_2025/bandekar25_interspeech.html)  
**Evidence:** D3; PDF SHA-256 `c6b6e7668fdd2240d3906c356a569025a1d0560df9a4171eb942c52e260a578d`; 5 pages.

- **Big picture:** Acoustic-to-articulatory inversion tries to infer moving vocal-tract positions from sound, which can make speech production measurable for recognition, synthesis, and pronunciation work.
- **Why hard:** Articulatory data are scarce, unseen speakers differ, and a large self-supervised feature extractor can improve accuracy while making real-time use expensive.
- **Naive attempt:** Attach a large pretrained feature extractor at inference time or train the inversion model only on the limited paired articulatory data.
- **Central move:** Pretrain the inversion model against three related targets—phoneme labels, articulatory features, and critical articulator labels—so it receives useful structure without carrying the external extractor at deployment.
- **Mechanism:** The model maps acoustic features to articulatory trajectories. During pretraining it predicts phonemic, broad articulatory, and critical-articulator targets; it is then fine-tuned with different amounts of paired data and compared with a baseline and SSL-feature systems on seen and unseen speakers.
- **Mathematical idea:** The main measures are correlation coefficient between predicted and reference trajectories and root-mean-square error. Multi-target pretraining adds supervised prediction tasks; the reported efficiency claim concerns removing the external SSL extractor, not eliminating all computation.
- **Connections:** Connects physical production to representation learning: linguistic labels are used as scaffolding for predicting continuous movement. It complements MRI-based inversion while exposing the tradeoff between a useful intermediate representation and direct physical measurement.
- **What paper reports:** The paper reports consistent AAI improvement, including low-resource gains; the strongest reported unseen-speaker configuration reaches CC 0.8612 and RMSE 1.1023, while inference avoids the external SSL extractor.
- **Limits:** The articulatory targets, speakers, language, and feature choices define the tested boundary; predicted movement is not equivalent to direct imaging. Reported gains and speed claims are author-reported and were not independently reproduced.

## 2. evaluation-deployment-and-consequence/privacy-security-and-accountability

**Paper:** [WavShape: Information-Theoretic Speech Representation Learning for Fair and Privacy-Aware Audio Processing](https://www.isca-archive.org/interspeech_2025/baser25_interspeech.html)  
**Evidence:** D3; PDF SHA-256 `ae50c2718241032f75c69a685dda667b052d47854a3bf4815fd162daf058a705`; 5 pages.

- **Big picture:** A speech embedding is useful only if it keeps information needed for the task while not exposing identity, accent, gender, or other sensitive attributes that downstream users did not authorize.
- **Why hard:** Removing sensitive information can also remove information a task needs, and privacy cannot be established by looking at a projection or one downstream accuracy score.
- **Naive attempt:** Compress a pretrained embedding with a generic bottleneck or train a classifier adversarially without measuring how much information about each attribute remains.
- **Central move:** Optimize mutual information in two directions: reduce dependence between the public embedding and sensitive labels while retaining dependence with task labels and the original speech representation.
- **Mechanism:** A frozen speech encoder produces embeddings, a trainable WavShape projection creates public embeddings, and a Donsker–Varadhan mutual-information estimator supplies the training signal. The estimator is removed at inference; downstream classifiers and information estimates test sensitive leakage and task retention across three datasets.
- **Mathematical idea:** The objective is a weighted combination of mutual-information terms. The Donsker–Varadhan estimator uses a log moment-generating expression to lower-bound dependence; the paper reports MI changes plus downstream task performance, so the MI estimate is a proxy for leakage rather than a proof of privacy.
- **Connections:** Makes representation design a constrained information-allocation problem. It joins speaker characteristics, fairness, privacy, compression, and evaluation: discarding a signal is only useful if the discarded signal is actually the unwanted one.
- **What paper reports:** The paper reports up to an 81% reduction in mutual information with sensitive attributes while retaining up to 97% of task-relevant information in its tested settings; on VCTK, gender-related MI falls from 0.40029 to 0.07493.
- **Limits:** Mutual-information estimation depends on the estimator, labels, datasets, and chosen sensitive attributes; unmeasured attributes or powerful attackers may still recover information. The figures are author-reported, and no independent privacy attack or reproduction was performed.

## 3. languages-accents-and-resources/multilingual-and-crosslingual

**Paper:** [From Context to Code-switching: Examining the Interplay of Language Proficiency and Multilingualism in Speech](https://www.isca-archive.org/interspeech_2025/bhattacharya25_interspeech.html)  
**Evidence:** D3; PDF SHA-256 `adb282c8c89a8773fdd0eed5585b8b91676857806f8fadf93bb8c9c898dfd5ba`; 5 pages.

- **Big picture:** People who use more than one language may switch languages within conversation, and interpreting that behavior requires distinguishing language ability and exposure from the switch itself.
- **Why hard:** Code-switching is shaped by language pair, conversation, speaker background, and local discourse; treating it as a single frequency can hide different switching strategies and confounds.
- **Naive attempt:** Count switches and attribute differences directly to a demographic label or assume language proficiency is unrelated to spontaneous switching behavior.
- **Central move:** Model code-switching quantity, dominant language, and switching strategy together with speaker background variables such as parental language, schooling language, and self-reported ability.
- **Mechanism:** The study analyzes spontaneous Spanish-English speech in the Bangor Miami corpus, defines insertional and alternational switching outcomes, compares speaker language profiles, and fits regression models to quantity, language distribution, and strategy. It separates associations that are statistically reliable from those that only approach significance.
- **Mathematical idea:** The paper uses correlations, logistic regression, confidence intervals, and prediction analyses. Its denominators are corpus speakers and code-switched utterances; an association between background and switching is not a causal estimate of proficiency.
- **Connections:** Treats language variety as part of the speech-generating person rather than noise around a universal model. It connects code-switching to data collection, accent/cultural boundaries, and the risk of interpreting a behavioral label without its linguistic context.
- **What paper reports:** The paper reports that parents’ primary language, secondary-school language, and self-reported higher-ability language are associated with code-switching quantity and dominant-language use, while several direct proficiency relationships are weak or inconclusive.
- **Limits:** The analysis is observational, focused on Spanish-English Bangor Miami speakers and available self-reports; background variables may be correlated and do not establish why a speaker switched. Findings do not generalize automatically to other language pairs, communities, or tasks; no independent reproduction was performed.

## 4. meaning-and-interaction/dialogue-and-turn-taking

**Paper:** [Triadic Multi-party Voice Activity Projection for Turn-taking in Spoken Dialogue Systems](https://www.isca-archive.org/interspeech_2025/elmers25_interspeech.html)  
**Evidence:** D3; PDF SHA-256 `f2c0736fcd3ab708f2fc0ace3ae870a1ebf3a0ddf51ae7236097e00e9180d9b1`; 5 pages.

- **Big picture:** A spoken agent must predict who will speak next in a group, because waiting for a long silence causes delay while speaking too early interrupts someone who has not finished.
- **Why hard:** Triadic conversation has more possible combinations of active and silent speakers than dyadic conversation, and topic or interaction style changes overlap patterns.
- **Naive attempt:** Use a fixed silence threshold or reuse a two-person turn-taking model without representing each participant’s future activity separately.
- **Central move:** Project future voice activity jointly for all three speakers using short time bins, then compare models trained on spontaneous and attentive triadic Japanese conversation.
- **Mechanism:** The VAP model encodes acoustic history and predicts binary speaking states for each speaker over future bins. With three speakers and two bins per speaker there are 2^6 possible states; cross-entropy trains the state distribution, and next-speaker accuracy compares predictions with held-out activity.
- **Mathematical idea:** The state space is a six-bit joint voice-activity label; probability mass over states gives the predicted future activity. The evaluation reports test loss and next-speaker accuracy, with separate spontaneous and attentive conversation conditions.
- **Connections:** Shows that turn-taking is a temporal prediction problem before it is a language-generation problem. It connects dialogue state, overlap, latency, and evaluation: a transcript score cannot reveal whether a system entered the turn at the right time.
- **What paper reports:** Triadic VAP trained on triadic conversation outperforms the baseline across tested models, while spontaneous discussions are harder than attentive listening; the paper reports accuracy differences by conversation type.
- **Limits:** The data are Japanese triadic discussions with controlled recording and a limited number of participants; the reduced two-bin horizon does not cover the full dyadic two-second state space. Acoustic-only prediction does not establish successful spoken-agent behavior, and no independent reproduction or user study was performed.

