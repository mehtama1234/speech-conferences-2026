# INTERSPEECH 2025 thirteenth-pass full-paper notes

Three official-PDF analyses close the remaining reviewed-evidence gaps for packet-loss concealment, open-vocabulary recognition, and augmentative communication. Results remain author-reported and were not independently reproduced.

## 1. listening-and-separation/echo-and-reconstruction

**Paper:** [TS-URGENet: A Three-stage Universal Robust and Generalizable Speech Enhancement Network](https://www.isca-archive.org/interspeech_2025/rong25_interspeech.html)  
**Evidence:** D3; PDF SHA-256 7bf691074f1cebd8350f4e97d43912eb42e9cc7821e20d4eda2b7454bd7c8161; 5 pages.

- **Big picture:** Packet loss removes evidence rather than merely adding noise; a universal enhancer must reconstruct missing regions and then handle other distortions.
- **Why hard:** Lost segments interact with noise, reverberation, clipping, bandwidth limits, codec damage, and residual loss.
- **Naive attempt:** Use one denoiser and assume missing samples behave like ordinary noise.
- **Central move:** Use a three-stage pipeline: filling, separation, and restoration.
- **Mechanism:** The filling stage predicts lost regions, separation suppresses noise/reverb/clipping, and restoration repairs bandwidth, codec, and remaining loss.
- **Mathematical idea:** Stage-wise spectral or waveform reconstruction is evaluated in the URGENT challenge setting.
- **Connections:** Packet loss is a missing-evidence problem and should not be collapsed into generic denoising.
- **What paper reports:** The system ranked second in URGENT Track 1.
- **Limits:** Challenge conditions, author-reported ranking, and no independent run limit the claim.

## 2. recognition-and-alignment/adaptation-and-open-vocabulary

**Paper:** [Fully End-to-end Streaming Open-vocabulary Keyword Spotting with W-CTC Forced Alignment](https://www.isca-archive.org/interspeech_2025/kim25d_interspeech.html)  
**Evidence:** D3; PDF SHA-256 d066ed299af2a95f276648caafaf13903da3a81a4c8849d6c24f0ae42ae88535; 5 pages.

- **Big picture:** Open-vocabulary keyword spotting must find arbitrary words without preparing word-aligned training data for every target.
- **Why hard:** Forced alignment is costly, while streaming recognition cannot wait for a separately aligned corpus.
- **Naive attempt:** Build a fixed-vocabulary detector or use an external forced aligner and precomputed word segments.
- **Central move:** Integrate W-CTC forced alignment into a fully end-to-end streaming system.
- **Mechanism:** CTC paths supply word-span alignment while the text encoder and verifier are trained in the same pipeline.
- **Mathematical idea:** CTC alignment links acoustic frames to text; keyword audio-text similarity then scores arbitrary words.
- **Connections:** Open vocabulary is a training and alignment problem, not only a larger keyword list.
- **What paper reports:** The paper reports superior performance on the Libriphrase hard set.
- **Limits:** Benchmark, language, and author-reported result limit generalization and independent reproducibility.

## 3. people-variation-and-health/clinical-and-assistive-speech

**Paper:** [A Silent Speech Decoding System from EEG and EMG with Heterogenous Electrode Configurations](https://www.isca-archive.org/interspeech_2025/inoue25b_interspeech.html)  
**Evidence:** D3; PDF SHA-256 4699a5e0d7a3500e45a6442a1333eec03eadc79be27d48a3e41191146cd7cda5; 5 pages.

- **Big picture:** Silent-speech decoding could let speech-impaired users communicate without vocalizing, but biosignal recordings vary across people and electrode layouts.
- **Why hard:** EEG and EMG configurations are heterogeneous and patient data are scarce, so a single fixed-subject model does not transfer well.
- **Naive attempt:** Train one model per subject with one fixed electrode configuration.
- **Central move:** Handle heterogeneous electrodes and use multitask training for cross-subject and cross-language calibration.
- **Mechanism:** A shared model learns from varying EEG/EMG layouts while multitask objectives stabilize word classification across speakers and languages.
- **Mathematical idea:** Word classification accuracy measures whether neural signals preserve enough information for decoding.
- **Connections:** Assistive speech is constrained by sensing hardware and patient variation as much as by the decoder.
- **What paper reports:** Accuracy is 95.3% for healthy participants and 54.5% for a patient, versus 70.1% and 13.2% for single-subject baselines.
- **Limits:** Patient count, setup, calibration, and author-reported results limit clinical deployment claims.

