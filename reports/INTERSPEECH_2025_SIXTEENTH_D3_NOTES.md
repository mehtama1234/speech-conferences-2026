# INTERSPEECH 2025 sixteenth-pass full-paper note

## An Investigative Study on Recent Sharpness- and Flatness-Based Optimizers for Enhanced Self-Supervised Speaker Verification

**Evidence:** D3; PDF SHA-256 `fe5c136e891dc4cb2a3ca7243efc66964d54b4c45c6c6e4e607f9a1fc6c3e763`; 5 pages.

**Ordinary problem:** A speaker-verification system should recognize the same person when the recording, wording, or channel changes, rather than memorizing the training speakers' exact conditions.

**Why hard:** The model must keep identity evidence while ignoring content, microphones, noise, and recording differences; the training objective and optimizer can change which evidence is retained.

**Naive attempt:** Use the most familiar optimizer and report one verification score, assuming the representation will generalize if the training loss decreases.

**Conceptual move:** Treat the optimization geometry itself as part of the identity-learning problem: compare ordinary, mixture-based, and sharpness-aware optimizers and regularizers instead of changing only the network architecture.

**Mechanism:** The study trains supervised and self-supervised speaker-verification systems with ADOPT, AdEMAMix, SAM, ASAM, GAM, and GSAM, then tests weight decay, exponential moving averages, and SWITCH EMA. The comparison asks whether flatter or better-conditioned solutions improve verification generalization without adding an inference-time identity module.

**Mathematical/evaluation object:** The verification decision compares an enrollment and test embedding, while the training choices change the parameter update. Sharpness-aware methods add a local worst-case loss perturbation so a solution is rewarded for remaining good in a neighborhood; EER and minDCF summarize threshold errors rather than directly measuring identity invariance.

**What it reports:** The paper reports that optimizer choice materially changes generalization and that the tested sharpness-aware and general-purpose optimizers can reach state-of-the-art self-supervised speaker-verification results in its experiments.

**Limit:** The conclusions are bounded by the selected speaker-verification corpora, architectures, optimizer settings, and author-reported comparisons; a better optimizer score does not establish robustness to every language, channel, attack, or demographic group. No independent reproduction was performed.

