# INTERSPEECH 2025 artifact execution audit

This is a static repository/dependency inspection. No paper experiment, model inference, dataset download, or listener study was executed.

| Paper | Artifact | Clone | Observed commit | Dataset/runtime boundary | Execution |
|---|---|---|---|---|---|
| ai25_interspeech | https://github.com/aizhiqi-work/voxaging | succeeded | `84f4dae15e1d` | gated-access-request-required | not-attempted |
| lemaguer25_interspeech | https://github.com/seblemaguer/replikant | succeeded | `81e308a079cb` | paper-specific-recipe-not-present-in-clone | not-attempted |
| ai25_interspeech | https://github.com/modelscope/3D-Speaker | succeeded | `065629c313ea` | external-model-and-dataset-download-required | not-attempted |
| giraldo25_interspeech | https://github.com/langtech-bsc/commonphone-se | succeeded | `2033c235e5c2` | demo-repository-only; CommonPhone data access not established | not-attempted |
| giraldo25_interspeech | https://github.com/espeak-ng/espeak-ng | succeeded | `699e79690f23` | not-applicable-to-paper-model | not-attempted |
| agrawal25b_interspeech | https://github.com/Kyubyong/ | not-found | `not-resolved` | unknown | not-attempted |

## Findings

### ai25_interspeech — https://github.com/aizhiqi-work/voxaging
- README documents 293 speakers and gated Hugging Face dataset access
- README states non-commercial/educational restrictions and no identification use
- Next action: Obtain authorized dataset access and inspect a paper-aligned evaluation path before any run.

### lemaguer25_interspeech — https://github.com/seblemaguer/replikant
- README documents Python 3.11 support
- tool launches a recipe-configured local Flask evaluation server
- repository provides generic recipes rather than the paper's listener study data
- Next action: Identify the paper's exact recipe and install under an isolated environment before smoke testing.

### ai25_interspeech — https://github.com/modelscope/3D-Speaker
- README documents Python >=3.8 and PyTorch >=1.10
- README provides speaker verification and diarization recipes
- pretrained models are hosted through ModelScope and some inference paths require access tokens
- Next action: Pin an environment and select a paper-aligned verification model; do not equate toolkit benchmark tables with reproduction of VoxAging.

### giraldo25_interspeech — https://github.com/langtech-bsc/commonphone-se
- README describes a demo for the speech-enhancement paper
- clone contains LICENSE and README but no evaluation pipeline was run
- Next action: Inspect the linked benchmark/data source and paper-aligned evaluation scripts before claiming reproducibility.

### giraldo25_interspeech — https://github.com/espeak-ng/espeak-ng
- README documents a C-based multilingual formant synthesizer with build documentation
- the repository is a third-party speech tool cited for processing, not the paper's enhancement model
- Next action: Do not treat successful eSpeak installation as reproduction of the enhancement experiments.

### agrawal25b_interspeech — https://github.com/Kyubyong/
- git remote inspection returned repository not found; the PDF URL is an organization/base link rather than a resolvable repository
- Next action: Resolve the exact artifact URL from the paper or author before further audit.

## Bounded local checks

These checks are intentionally separate from the artifact ledger. They establish only the recorded local command outcome at the observed commit; they do not reproduce a paper experiment.

| Artifact | Papers | Commit | Scope | Status |
|---|---|---|---|---|
| idiap/RnV | not mapped | `ad9ce5c42c12` | syntax-only compile check; no dependency installation, data download, training, checkpoint loading, or scientific reproduction | syntax-pass |
| lee-jhwn/IS25-emg-ema | not mapped | `d8bd5cfe1722` | repository clone plus Python syntax compilation; no dependency installation, dataset download, checkpoint loading, training, inference, or scientific reproduction | syntax-pass |
| techsword/reliability-speech-feat-attr | not mapped | `37990e842ae8` | repository clone plus Python syntax compilation; no dependency installation, dataset download, checkpoint loading, training, inference, or scientific reproduction | syntax-pass |
| luferrer/ConfidenceIntervals | dumpala25_interspeech, deng25b_interspeech | `4c320a10686c` | repository clone plus Python syntax compilation; no dependency installation, dataset download, checkpoint loading, training, inference, or scientific reproduction | syntax-pass |
| luferrer/ConfidenceIntervals | dumpala25_interspeech, deng25b_interspeech | `4c320a10686c` | bounded documented toy-data smoke test; no paper data, model, checkpoint, training, or scientific reproduction | check-error |
| luferrer/ConfidenceIntervals | dumpala25_interspeech, deng25b_interspeech | `4c320a10686c` | bounded documented toy-data smoke test; no paper data, model, checkpoint, training, or scientific reproduction | smoke-pass |
| aizhiqi-work/voxaging | not mapped | `84f4dae15e1d` | repository clone plus Python syntax compilation; no dependency installation, dataset download, checkpoint loading, training, inference, or scientific reproduction | syntax-pass |
| modelscope/3D-Speaker | not mapped | `065629c313ea` | repository clone plus Python syntax compilation; no dependency installation, dataset/model download, checkpoint loading, inference, or scientific reproduction | syntax-pass |
| seblemaguer/replikant | not mapped | `81e308a079cb` | repository clone, Python syntax compilation, and dependency-free wheel build; no dependency installation, survey data, listener study, server launch, or scientific reproduction | package-build-pass |
| langtech-bsc/commonphone-se | giraldo25_interspeech | `2033c235e5c2` | repository clone plus Python syntax compilation; no CommonPhone data download, dependency installation, model inference, or scientific reproduction | syntax-pass |

The bounded syntax and toy-smoke results above do not establish dependency resolution, dataset/checkpoint access, inference behavior, metric agreement, or scientific reproduction.
