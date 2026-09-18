#!/usr/bin/env python3
"""Record a second balanced ICASSP abstract-level semantic review batch."""
from __future__ import annotations
import hashlib, json
from pathlib import Path
HERE=Path(__file__).resolve().parent; DATA=HERE/"data"
ASSIGNMENTS={
 "26776d22965e":("sound-and-production","room-channel-and-sensing","microphone-channel","Vision and spatial information are used to reconstruct binaural audio, so the sensor/channel path is part of the sound evidence."),
 "27bac793b206":("sound-and-production","room-channel-and-sensing","reverberant-mixture","The enhancement problem includes reverberation and speech mixtures; the observed channel must be related to the clean source before generation."),
 "2cd5b5a38e31":("sound-and-production","time-frequency-measurement","multi-resolution-signal","The method combines discrete and continuous speech representations to preserve changing acoustic structure during enhancement."),
 "2e136c64ecad":("sound-and-production","time-frequency-measurement","sampling-and-quantization","Multi-rate speech quality prediction tests how spectral representation changes when sampling conditions change."),
 "0af01b180174":("listening-and-separation","source-separation-and-spatial-listening","spatial-filtering","The paper asks which spatial cues help diarization under overlap, separating voices by location before assigning identity."),
 "0c07fef3b5d6":("listening-and-separation","noise-enhancement","speech-prior-denoising","Dynamic pruning estimates what auxiliary signal information is useful so enhancement can spend computation where noise repair needs it."),
 "2aa7d97b928fe":("listening-and-separation","source-separation-and-spatial-listening","target-conditioned-separation","Target-speaker extraction uses training dynamics and multiple factors to select one voice from a mixture."),
 "3b9021143ff7":("listening-and-separation","noise-enhancement","nonstationary-noise","Contextual specialization in enhancement asks whether different acoustic contexts require different restoration behavior rather than one universal filter."),
 "0f4083d8f544":("recognition-and-alignment","acoustic-unit-mapping","acoustic-to-token","The paper changes the attention representation in ASR to reduce memory while retaining the mapping from speech frames to tokens."),
 "15d8dcdc31eb":("recognition-and-alignment","boundaries-and-sequence-structure","long-context-decoding","Streaming ASR must decide how much future context is worth the latency; the paper tests whether full self-attention is necessary."),
 "1b7e4d682dce":("recognition-and-alignment","adaptation-and-open-vocabulary","domain-and-context-biasing","A medical knowledge graph supplies domain terms for correcting ASR errors in spoken medical questions rather than treating every word equally."),
 "14649513fd57":("recognition-and-alignment","boundaries-and-sequence-structure","alignment","Weakly supervised audio-visual segmentation asks where an event begins and ends when frame-level boundaries are not fully labeled."),
 "1c6d9829cb49":("meaning-and-interaction","prosody-and-intent","paralinguistic-state","Soft audio-language targets model affect as graded rather than forcing one hard emotion label onto ambiguous speech."),
 "50bb514fcea9":("meaning-and-interaction","dialogue-and-turn-taking","turn-boundary","Prosodic and lexical cues predict turn transitions, making timing and conversational control the target rather than transcription alone."),
 "26ad929e3cfd":("meaning-and-interaction","prosody-and-intent","paralinguistic-state","The paper recovers emotion information from discrete speech tokens, testing which compressed cues still carry paralinguistic state."),
 "0fd6674c828f":("meaning-and-interaction","grounding-and-action","intent-in-context","Multimodal sentiment decisions depend on when spatial and temporal signals are integrated before an affective label is chosen."),
 "38f6bf21c738":("voice-generation-and-control","text-to-speech-and-content","text-to-speech-planning","ARCHI-TTS aligns self-supervised semantic information with flow-matching generation so text plans become intelligible speech efficiently."),
 "519c2042045b":("voice-generation-and-control","voice-identity-and-conversion","speaker-identity","Speaker unlearning in zero-shot TTS asks whether a generated voice can avoid retaining a person’s identity while still speaking."),
 "a3fc7ede7606":("voice-generation-and-control","text-to-speech-and-content","zero-shot-voice","Cross-lingual voice cloning must preserve linguistic content while transferring a speaker identity across languages."),
 "63b0b73e17e4":("voice-generation-and-control","voice-identity-and-conversion","speaker-identity","Short-enrollment speaker embeddings determine whether a personal voice activity detector can distinguish the intended speaker."),
 "38465bde406f":("people-variation-and-health","clinical-and-assistive-speech","dysarthria-and-atypical-speech","Electro-laryngeal speech has atypical source characteristics, so perceptually guided conversion targets access and intelligibility for a clinical population."),
 "bcb971647845":("people-variation-and-health","speaker-characteristics","style-and-state-variation","Vocal effort varies with speaking conditions; the paper tests whether speaker representations can classify it in naturalistic, uncalibrated speech."),
 "a47b1a73d887":("people-variation-and-health","speaker-characteristics","speaker-verification","The paper studies how angular-margin decisions fail in speaker verification and changes score geometry to preserve identity evidence."),
 "789a80acdec4":("people-variation-and-health","human-centered-evaluation","listener-effort","Emotion annotations vary across humans; augmenting annotation with audio-language models addresses the cost and disagreement of listener judgments."),
 "2e870d5a3ceb":("languages-accents-and-resources","accent-and-cultural-boundaries","accent-robustness","Parameter-efficient adaptation tests how to preserve recognition when accent-related acoustic patterns differ from training speech."),
 "3c121afc5b61":("languages-accents-and-resources","multilingual-and-crosslingual","crosslingual-transfer","OCR supplies visual context to a multilingual ASR system, combining language and non-speech evidence when audio alone is ambiguous."),
 "4fcfd39662d5":("languages-accents-and-resources","multilingual-and-crosslingual","crosslingual-transfer","Continual multilingual self-supervised expansion must add languages without forgetting earlier speech structure."),
 "6071d47e9f39":("languages-accents-and-resources","accent-and-cultural-boundaries","dialect-and-variety","Dialectal ASR requires adaptation that preserves distinctions among varieties instead of treating one standard accent as the target."),
 "34256c20127c":("evaluation-deployment-and-consequence","metrics-and-targets","word-error-versus-understanding","A challenge benchmark tests enhancement across conditions and makes the denominator and metric explicit before ranking systems."),
 "85e15a20e929":("evaluation-deployment-and-consequence","metrics-and-targets","word-error-versus-understanding","Post-ASR correction for dysarthric speech asks what errors WER misses and whether a language-aware correction better reflects usable meaning."),
 "bd6d4e8e756650":("evaluation-deployment-and-consequence","metrics-and-targets","quality-and-naturalness","Frechet Speech Distance evaluates synthetic speech distributions, raising the question of whether a learned proxy tracks listener quality."),
 "8f23e5c63ba6":("evaluation-deployment-and-consequence","privacy-security-and-accountability","spoofing-and-deepfake","Segment-aware deepfake localization tests whether a detector can identify where manipulation occurs, not merely label an entire clip fake."),
}
source=json.loads((DATA/"icassp-2026-papers.json").read_text())["papers"]; by={p["paperId"]:p for p in source}; rows=[]
for prefix,a in ASSIGNMENTS.items():
 p=next(p for pid,p in by.items() if pid.startswith(prefix)); abstract=p.get("abstract") or ""
 rows.append({"paper_id":p["paperId"],"title":p["title"],"decision":"supported","confidence":"analyst-reviewed-D2","theme_id":a[0],"subtheme_id":a[1],"concept_id":a[2],"semantic_reasoning":a[3],"evidence_excerpt":abstract[:1000],"source_location":p.get("url"),"source_sha256":hashlib.sha256(abstract.encode()).hexdigest(),"evidence_depth":"D2","review_state":"analyst-reviewed","claim_boundary":"ICASSP discovery/abstract record only; official proceedings and full-paper mechanism are not established."})
payload={"schema_version":1,"batch_id":"icassp-2026-semantic-batch-002","status":"analyst-reviewed-D2-batch","claim_boundary":"These 32 assignments are analyst-reviewed from preserved ICASSP abstract records. They do not establish full-paper mechanisms or venue-wide prevalence.","reviewed_count":len(rows),"rows":rows}
(DATA/"icassp-2026-semantic-reviewed-batch-002.json").write_text(json.dumps(payload,indent=2,ensure_ascii=False)+"\n")
print(json.dumps({"batch_id":payload["batch_id"],"reviewed_count":len(rows),"D2":sum(r["evidence_depth"]=="D2" for r in rows)}))
