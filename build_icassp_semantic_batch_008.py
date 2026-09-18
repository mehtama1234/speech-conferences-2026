#!/usr/bin/env python3
"""Record an eighth bounded ICASSP semantic review batch."""
from __future__ import annotations
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = HERE / "data"
A = [
 ("Bridging the Measurement", "sound-and-production", "room-channel-and-sensing", "reverberant-mixture", "Room-acoustics simulation must match the recording path before a speech model can learn from the right distortion."),
 ("LipsAM:", "sound-and-production", "room-channel-and-sensing", "reverberant-mixture", "Dereverberation must change the received amplitude pattern without erasing the speech structure carried by that pattern."),
 ("Gencho:", "sound-and-production", "room-channel-and-sensing", "reverberant-mixture", "A room impulse response is the hidden path that turns clean speech into the reverberant signal a microphone observes."),
 ("Exterior Sound Field Estimation", "sound-and-production", "room-channel-and-sensing", "microphone-channel", "Sound-field estimation asks how to infer locations outside the measured microphones from physically constrained acoustic evidence."),
 ("Distributed Multichannel Active Noise", "listening-and-separation", "noise-enhancement", "nonstationary-noise", "Distributed active-noise control must coordinate microphones and loudspeakers when the interfering field changes over space and time."),
 ("CaSNet:", "listening-and-separation", "noise-enhancement", "spectral-mask", "A distributed enhancement model must compress information between devices while preserving the speech needed after reconstruction."),
 ("Fast-ULCNet:", "listening-and-separation", "noise-enhancement", "speech-prior-denoising", "Single-channel enhancement has to suppress noise within a strict compute budget without turning low complexity into lost intelligibility."),
 ("Frontend Token Enhancement", "listening-and-separation", "noise-enhancement", "speech-prior-denoising", "Token-based recognition needs a front end that repairs noisy acoustic units before the language decoder commits to words."),
 ("In-Sync:", "recognition-and-alignment", "adaptation-and-open-vocabulary", "domain-and-context-biasing", "ASR with timestamps must keep words synchronized with speech while adapting a speech-aware language model to the transcript task."),
 ("Sequence-Level Unsupervised", "recognition-and-alignment", "acoustic-unit-mapping", "self-supervised-speech-units", "Unsupervised ASR must learn useful sequence mappings without being handed the correct transcript for every recording."),
 ("Chunk-wise Attention Transducers", "recognition-and-alignment", "boundaries-and-sequence-structure", "long-context-decoding", "Streaming speech-to-text must decide with limited future context while keeping enough history to avoid boundary errors."),
 ("MATE:", "recognition-and-alignment", "adaptation-and-open-vocabulary", "open-vocabulary-recognition", "Open-vocabulary keyword spotting must match a spoken request to a new text query without retraining a fixed keyword list."),
 ("Improving Audio Question Answering", "meaning-and-interaction", "grounding-and-action", "referential-grounding", "Audio question answering must use the sound as evidence rather than generate a plausible answer from language priors alone."),
 ("Hierarchical Activity Recognition", "meaning-and-interaction", "grounding-and-action", "referential-grounding", "Long-form audio understanding must connect events across time instead of treating each short sound fragment as an isolated label."),
 ("AR&D:", "meaning-and-interaction", "grounding-and-action", "referential-grounding", "An audio-language model needs explanations that point back to the acoustic concepts supporting its answer."),
 ("SmoGVLM:", "meaning-and-interaction", "grounding-and-action", "interactional-feedback", "A small multimodal model must combine visual and audio-language evidence while keeping its reasoning useful under limited compute."),
 ("WavLink:", "voice-generation-and-control", "text-to-speech-and-content", "text-to-speech-planning", "Compact audio-text representations must preserve enough speech content for a model to connect words with how they sound."),
 ("VoxMorph:", "voice-generation-and-control", "voice-identity-and-conversion", "zero-shot-voice", "Voice morphing must change identity in a controllable way without entangling identity with the words being spoken."),
 ("MeanVoiceFlow:", "voice-generation-and-control", "voice-identity-and-conversion", "voice-conversion", "Nonparallel voice conversion must transform a source speaker into a target voice without paired recordings of the same sentence."),
 ("Wave-Trainer-Fit:", "voice-generation-and-control", "text-to-speech-and-content", "neural-vocoder", "A neural vocoder must turn learned speech features into a detailed waveform without making the decoder too costly or unstable."),
 ("Hyperbolic Additive Margin", "people-variation-and-health", "speaker-characteristics", "speaker-verification", "Speaker verification must separate identity from content and channel variation, especially when speakers are not all equally represented."),
 ("EMG-to-Speech", "people-variation-and-health", "clinical-and-assistive-speech", "augmentative-communication", "Muscle signals can provide a speech pathway when the ordinary voice is unavailable, but the mapping must remain intelligible with fewer sensors."),
 ("What You Feel Is Not", "people-variation-and-health", "human-centered-evaluation", "listener-effort", "Emotion systems need evaluation that distinguishes a speaker's own experience from what an observer infers from the voice."),
 ("Attention-weighted Centered", "people-variation-and-health", "human-centered-evaluation", "accessibility-fit", "Speech emotion representations should transfer useful information without assuming that one pretrained feature space fits every listener-facing task."),
 ("The TMU System", "languages-accents-and-resources", "multilingual-and-crosslingual", "crosslingual-transfer", "A multilingual audio-language system must transfer sound concepts across languages when local labels are uneven."),
 ("PROST-LLM:", "languages-accents-and-resources", "multilingual-and-crosslingual", "crosslingual-transfer", "Speech-to-speech translation must carry meaning across languages while preserving the spoken interaction rather than only translating text."),
 ("From Human Speech to Ocean", "languages-accents-and-resources", "multilingual-and-crosslingual", "crosslingual-transfer", "Transferring speech representations to underwater signals tests which learned acoustic structure is general and which depends on human language."),
 ("SpeechMapper:", "languages-accents-and-resources", "multilingual-and-crosslingual", "crosslingual-transfer", "A speech-to-text projector must connect acoustic representations to a language model without assuming the two spaces already share meaning."),
 ("Explainable Deepfake Detection", "evaluation-deployment-and-consequence", "privacy-security-and-accountability", "spoofing-and-deepfake", "A fake-speech detector should expose the evidence behind its decision instead of hiding a generator shortcut behind one score."),
 ("Leveraging large multimodal", "evaluation-deployment-and-consequence", "privacy-security-and-accountability", "spoofing-and-deepfake", "Audio-video deepfake detection must test whether multiple modalities agree when manipulation is coordinated."),
 ("StreamMark:", "evaluation-deployment-and-consequence", "privacy-security-and-accountability", "voice-privacy", "Audio watermarking should make generated speech traceable while keeping the watermark difficult to remove from ordinary use."),
 ("SCENE:", "evaluation-deployment-and-consequence", "metrics-and-targets", "quality-and-naturalness", "Codec enhancement must improve perceived sound without treating semantic similarity or waveform fidelity as the whole listening experience."),
]
papers = json.loads((DATA / "icassp-2026-papers.json").read_text())["papers"]
rows, used = [], set()
for prefix, theme, subtheme, concept, reasoning in A:
    matches = [p for p in papers if p["title"].startswith(prefix)]
    if len(matches) != 1: raise SystemExit(f"title match {prefix!r}: {len(matches)}")
    p = matches[0]
    if p["paperId"] in used: raise SystemExit(f"duplicate in batch: {p['paperId']}")
    used.add(p["paperId"])
    abstract = p.get("abstract") or ""
    if not abstract: raise SystemExit(f"batch 008 requires D2 abstract: {p['title']}")
    rows.append({"paper_id":p["paperId"],"title":p["title"],"decision":"supported","confidence":"analyst-reviewed-D2","theme_id":theme,"subtheme_id":subtheme,"concept_id":concept,"semantic_reasoning":reasoning,"evidence_excerpt":abstract[:1000],"source_location":p.get("url"),"source_sha256":hashlib.sha256(abstract.encode()).hexdigest(),"evidence_depth":"D2","review_state":"analyst-reviewed","claim_boundary":"ICASSP discovery record with abstract support; full-paper mechanisms, ablations, and limitations are not established."})
payload={"schema_version":1,"batch_id":"icassp-2026-semantic-batch-008","status":"analyst-reviewed-D2-batch","claim_boundary":"These assignments are analyst-reviewed from preserved ICASSP title/abstract records. They do not establish full-paper mechanisms or venue-wide prevalence.","reviewed_count":len(rows),"rows":rows}
(DATA / "icassp-2026-semantic-reviewed-batch-008.json").write_text(json.dumps(payload,indent=2,ensure_ascii=False)+"\n")
print(json.dumps({"batch_id":payload["batch_id"],"reviewed_count":len(rows),"D2":len(rows)}))
