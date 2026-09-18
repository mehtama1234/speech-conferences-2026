# INTERSPEECH 2025 fourteenth-pass full-paper notes

Two official-PDF analyses deepen the two remaining thin D3 families: sequence boundaries and spatial source separation. Results remain author-reported and were not independently reproduced.

## 1. recognition-and-alignment/boundaries-and-sequence-structure

**Paper:** [Dynamic Context-Aware Streaming Pretrained Language Model For Inverse Text Normalization](https://www.isca-archive.org/interspeech_2025/ho25_interspeech.html)  
**Evidence:** D3; PDF SHA-256 8c15bc4084b595c726690bcf2a4fe9c0b1c2abaf0f0dafe3ecaf73f720f73fde; 5 pages.

- **Big picture:** Speech arrives incrementally, but written formatting often needs context that has not arrived yet.
- **Why hard:** Streaming ITN must balance incomplete context, accuracy, adaptation, and latency.
- **Naive attempt:** Run a full-context normalizer after the utterance is complete, or use fixed chunks that ignore right context.
- **Central move:** Use a pretrained language model with dynamic chunk sizes and controlled right-context during training and inference.
- **Mechanism:** The model changes its available context as speech arrives, using right-context information without abandoning the streaming budget.
- **Mathematical idea:** Sequence decoding maps spoken-form tokens to written-form tokens; latency and accuracy form the deployment tradeoff.
- **Connections:** Normalization is a boundary between recognition and usable text, not a cosmetic postprocessing detail.
- **What paper reports:** The paper reports accuracy comparable to non-streaming ITN and better than prior streaming models on Vietnamese data while maintaining low latency.
- **Limits:** Vietnamese data, benchmark, and author-reported latency/results limit cross-language and independent deployment claims.

## 2. listening-and-separation/source-separation-and-spatial-listening

**Paper:** [Overlap-Adaptive Hybrid Speaker Diarization and ASR-Aware Observation Addition for MISP 2025 Challenge](https://www.isca-archive.org/interspeech_2025/huang25k_interspeech.html)  
**Evidence:** D3; PDF SHA-256 b3ae7c9f1c41b5d59186880d92a9813d4ee6d022d4ac2baa3eac27b9606fa4e8; 5 pages.

- **Big picture:** Meeting speech contains overlapping speakers, and diarization and recognition must make decisions from the same mixed observations.
- **Why hard:** Overlap changes which speaker evidence is reliable; guided source separation can fail at low signal-to-noise ratio.
- **Naive attempt:** Use one diarization model and assume separated observations are equally useful for ASR.
- **Central move:** Combine overlap-adaptive diarization with ASR-aware observation addition and a cascaded meeting-recognition system.
- **Mechanism:** A hybrid segmentation/clustering diarizer selects its model by overlap, while ASR-aware observations compensate for weak guided separation before recognition.
- **Mathematical idea:** Diarization assigns speaker-time regions; CER and concatenated minimum-permutation CER measure the downstream meeting transcript.
- **Connections:** Separation is not an isolated front end: errors in overlap decisions change recognition evidence and speaker attribution together.
- **What paper reports:** The system reports 9.48% CER and 11.56% cpCER and first place in both MISP tracks.
- **Limits:** Challenge tracks, meeting conditions, and author-reported ranking limit generalization and independent reproduction.

