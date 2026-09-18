#!/usr/bin/env python3
"""Record a fifth speech-focused ICASSP abstract review batch."""
from __future__ import annotations
import hashlib, json
from pathlib import Path
HERE = Path(__file__).resolve().parent
DATA = HERE / "data"
A = {
"148e6a28a06":("sound-and-production","room-channel-and-sensing","microphone-channel","Echo cancellation models the path from loudspeaker back to microphone so the returned copy can be removed without erasing near-end speech."),
"1cbb191e933":("sound-and-production","time-frequency-measurement","windowed-spectrum","Cross-cultural Mel-scale analysis tests whether a convenient frequency representation encodes assumptions about which spectral differences matter."),
"2cdabc58f85":("sound-and-production","room-channel-and-sensing","microphone-channel","Neural ambisonics reconstructs sound for arbitrary microphone directivity, treating sensor geometry as part of the signal."),
"50e14b9ac57":("sound-and-production","room-channel-and-sensing","reverberant-mixture","Acoustic synthesis from reverberant speech and text tries to infer a room response from incomplete evidence and generate a controllable environment."),
"2e70c2af8e1":("listening-and-separation","noise-enhancement","speech-prior-denoising","Phonetic mutual information gives enhancement a target beyond waveform cleanliness: preserve cues a recognizer needs while suppressing degradation."),
"03131c31bab":("listening-and-separation","echo-and-reconstruction","perceptual-enhancement","Audio coding compresses a changing waveform while trying to preserve what listeners and downstream speech systems can use."),
"412b276202":("listening-and-separation","noise-enhancement","target-conditioned-separation","Gaze and visual attention identify which speech source matters, allowing enhancement to follow the listener's target."),
"4811d23ab65":("listening-and-separation","source-separation-and-spatial-listening","target-conditioned-separation","Brain-informed separation uses listener neural responses as evidence about the speech being followed in a mixture."),
"221e2ec185":("recognition-and-alignment","acoustic-unit-mapping","open-vocabulary-recognition","Zero-shot keyword spotting must detect unseen terms while suppressing false alarms, exposing the boundary of a fixed keyword list."),
"223a9bfefef":("recognition-and-alignment","adaptation-and-open-vocabulary","domain-and-context-biasing","Courtside context can guide ASR toward rare names and terms, but context must not override what audio says."),
"225b064777":("recognition-and-alignment","acoustic-unit-mapping","pronunciation-variation","Synthetic text and phonetic respelling create target-domain pronunciations when labeled speech is scarce."),
"616a1e4bc31":("recognition-and-alignment","adaptation-and-open-vocabulary","domain-and-context-biasing","Contextual biasing changes lexical decisions using common-word cues and predicted bias-word positions."),
"036b21f2e70":("meaning-and-interaction","dialogue-and-turn-taking","dialogue-state","Dialogue satisfaction, emotion, and state change cannot be reduced to transcription correctness alone."),
"050635ffb58":("meaning-and-interaction","prosody-and-intent","paralinguistic-state","Generative speech-emotion recognition treats affect as a structured state rather than a fixed utterance label."),
"085852d8c01":("meaning-and-interaction","prosody-and-intent","intent-in-context","Test-time emotion adaptation asks whether affective cues change across speakers and domains without target labels."),
"3437b5e47c7":("meaning-and-interaction","grounding-and-action","referential-grounding","Audio question answering must know when an answer is absent instead of forcing a confident response."),
"240230b87b7":("voice-generation-and-control","prosody-and-interactive-control","style-and-emotion-control","Low-resource audio diffusion must follow a requested style when examples are limited."),
"3fb899f3708":("voice-generation-and-control","prosody-and-interactive-control","prosody-control","Audio extension and morphing changes a sound along a controlled path while preserving identity."),
"454db90b70e":("voice-generation-and-control","voice-identity-and-conversion","zero-shot-voice","Real-time voice anonymization must hide identity while retaining content and acceptable live latency."),
"c92d0c92d4c":("voice-generation-and-control","text-to-speech-and-content","text-to-speech-planning","Open-vocabulary instruction TTS turns an instruction into content and controllable vocal realization."),
"03e18de3236":("people-variation-and-health","speaker-characteristics","speaker-verification","Duration-robust verification asks whether identity evidence survives very short utterances."),
"21fff85b5e9":("people-variation-and-health","clinical-and-assistive-speech","clinical-speech-marker","Cognitive-status classification must distinguish health evidence from topic, speaker, and recording confounds."),
"1e5c84848c9":("people-variation-and-health","speaker-characteristics","style-and-state-variation","Deepfake attribution tests whether a representation identifies a generator across changing content and speakers."),
"a145addd7b1":("people-variation-and-health","clinical-and-assistive-speech","dysarthria-and-atypical-speech","Enhancement for cochlear-implant recipients must preserve cues accessible to altered hearing, not just ordinary-listener scores."),
"53e7ac04cd2":("languages-accents-and-resources","accent-and-cultural-boundaries","accent-robustness","Accent identification via voice conversion tests whether accent can be separated from timbre."),
"5a109e50b40":("languages-accents-and-resources","accent-and-cultural-boundaries","dialect-and-variety","Streaming Arabic dialect identification must decide a variety before the utterance ends."),
"890364175bb":("languages-accents-and-resources","multilingual-and-crosslingual","crosslingual-transfer","A byte-level multilingual tokenizer changes the symbol inventory so writing-system differences do not force incompatible vocabularies."),
"98a622eab40":("languages-accents-and-resources","multilingual-and-crosslingual","crosslingual-transfer","Mixture-of-experts and dynamic downsampling adapt ASR to languages with different acoustic and temporal structure."),
"11f0ad96bd0":("evaluation-deployment-and-consequence","metrics-and-targets","word-error-versus-understanding","Diarization must expose speaker and boundary errors rather than hide them in one global score."),
"f029a2feba6":("evaluation-deployment-and-consequence","metrics-and-targets","calibration-and-selective-use","Speech-quality estimation should be tested on concealed datasets so familiar conditions cannot make a model appear calibrated."),
"f30f800954d":("evaluation-deployment-and-consequence","privacy-security-and-accountability","spoofing-and-deepfake","Explainable deepfake detection links a security decision to formant evidence instead of only emitting a label."),
"bc910f279b7":("evaluation-deployment-and-consequence","metrics-and-targets","calibration-and-selective-use","Few-shot and pseudo-label quality evaluation tests whether metrics remain reliable when human labels are scarce."),
}
source = json.loads((DATA/"icassp-2026-papers.json").read_text())["papers"]
rows=[]
for prefix,a in A.items():
    matches=[p for p in source if p["paperId"].startswith(prefix)]
    if len(matches)!=1: raise SystemExit(f"expected one paper for {prefix}, found {len(matches)}")
    p=matches[0]; abstract=p.get("abstract") or ""
    rows.append({"paper_id":p["paperId"],"title":p["title"],"decision":"supported","confidence":"analyst-reviewed-D2","theme_id":a[0],"subtheme_id":a[1],"concept_id":a[2],"semantic_reasoning":a[3],"evidence_excerpt":abstract[:1000],"source_location":p.get("url"),"source_sha256":hashlib.sha256(abstract.encode()).hexdigest(),"evidence_depth":"D2","review_state":"analyst-reviewed","claim_boundary":"ICASSP discovery/abstract record only; official proceedings and full-paper mechanism are not established."})
payload={"schema_version":1,"batch_id":"icassp-2026-semantic-batch-005","status":"analyst-reviewed-D2-batch","claim_boundary":"These 32 assignments are analyst-reviewed from preserved ICASSP abstract records. They do not establish full-paper mechanisms or venue-wide prevalence.","reviewed_count":len(rows),"rows":rows}
(DATA/"icassp-2026-semantic-reviewed-batch-005.json").write_text(json.dumps(payload,indent=2,ensure_ascii=False)+"\n")
print(json.dumps({"batch_id":payload["batch_id"],"reviewed_count":len(rows),"D2":len(rows)}))

