#!/usr/bin/env python3
"""Record a title-bounded ICASSP semantic review batch."""
from __future__ import annotations
import hashlib, json
from pathlib import Path
HERE = Path(__file__).resolve().parent
DATA = HERE / "data"
A = [
 ("038b5e264b9c82c821a7a5a950349d6c7af968bd","sound-and-production","time-frequency-measurement","multi-resolution-signal","Speech super-resolution reconstructs missing bandwidth, making the frequency limit of the recording part of the speech problem."),
 ("11dd56ef7b05565fa42406dd90eded7f33fb8d14","sound-and-production","room-channel-and-sensing","microphone-channel","Binaural speech enhancement must preserve interaural timing cues as well as the speech waveform."),
 ("13058f7ce84fd16da34a06922ca6ed2152230c12","sound-and-production","time-frequency-measurement","sampling-and-quantization","A lightweight neural speech codec allocates a limited bitrate between acoustic detail and usable reconstruction."),
 ("2bbdd2e5bc25d7b2c43c7d567990192ac2c453cb","sound-and-production","time-frequency-measurement","multi-resolution-signal","Joint speech compression and enhancement treats coding distortion and noise removal as one signal-representation problem."),
 ("08ad5f25492709dddba346ca401f29fac4fa380d","listening-and-separation","source-separation-and-spatial-listening","blind-source-separation","Music source separation must isolate several sounds when only their mixture is available."),
("1842b07d6356febdfc7a2dd0d960fe3593bd4d2d","listening-and-separation","noise-enhancement","speech-prior-denoising","Cochlear-implant speech denoising must remove interference while retaining cues that an impaired listener can use."),
 ("2d9bf6dc3865fda35c1c7eff2e70a35945fe076b","listening-and-separation","noise-enhancement","spectral-mask","Speech enhancement must coordinate magnitude and phase rather than suppress noise in only one representation."),
 ("d18190bbefd1c4b3729d5ac36ee6aafefcad56d9","listening-and-separation","source-separation-and-spatial-listening","target-conditioned-separation","A streamable diffusion separator reconstructs a target speech source while meeting an online latency constraint."),
 ("1e96005d1136b5724f4868e4b5d72bf4258600c9","recognition-and-alignment","boundaries-and-sequence-structure","alignment","Multi-pass error correction changes an ASR transcript after decoding, making recognition a sequence-repair problem."),
("23ee11c59dbdd9045d08998cadef43ba39251003","recognition-and-alignment","acoustic-unit-mapping","self-supervised-speech-units","A phonetic subspace asks which dimensions of a speech representation carry the sound distinctions needed for recognition."),
 ("3a176b4c85bc9328e2657e7026ee503719c455d1","recognition-and-alignment","acoustic-unit-mapping","self-supervised-speech-units","Speech discretization converts continuous signals into units that a discrete-token recognizer can reuse."),
 ("da02d9998c528c02e8189fc418f45beee9e5c4c1","recognition-and-alignment","boundaries-and-sequence-structure","long-context-decoding","Consistency regularization stabilizes transducer decisions across the sequence of an automatic speech recognizer."),
 ("2d0e4481166e55eb34d6efb8a9e079aaae0ae73e","meaning-and-interaction","dialogue-and-turn-taking","dialogue-state","A dialogue system must use conversational context to improve the cognitive support it provides over multiple turns."),
 ("30a6b7b3036cf9c279f9b26bd5d535cd7e9a81b0","meaning-and-interaction","dialogue-and-turn-taking","dialogue-state","Generated spoken dialogues can supply varied conversational context for training speech interaction systems."),
 ("cfb40c957353851cdccc0497f9e6c1696f0f020e","meaning-and-interaction","prosody-and-intent","paralinguistic-state","Speech and non-verbal vocal sounds jointly carry emotion, so recognition must not discard the non-verbal channel."),
("d9f764f6cc990b6044c7907ef50ad2799613cb94","meaning-and-interaction","grounding-and-action","intent-in-context","Audio-based toxic-span detection asks a system to connect spoken content and harmful meaning to the relevant span."),
("137d39469bbb18ae92c5c08a1029e0f4ea202d5a","voice-generation-and-control","prosody-and-interactive-control","style-and-emotion-control","Emotion-controlled audio-driven facial animation must coordinate visible movement with the intended vocal affect."),
 ("1f8a801c970c93b61ebe34702e2f3164d8b0a956","voice-generation-and-control","text-to-speech-and-content","text-to-speech-planning","Few-step speech generation trades iterative refinement against the speed needed to synthesize usable voice."),
 ("d7cc01eb6aad28ecca46d33e099a310e44bae6e7","voice-generation-and-control","voice-identity-and-conversion","voice-conversion","Voice cloning attempts to reproduce a speaker's identity from a learned voice representation."),
("d9324538740727199cda494aa4d1a1c7c2f48ae3","voice-generation-and-control","prosody-and-interactive-control","prosody-control","Multilingual zero-shot TTS must use prosody and articulatory cues to control delivery across languages and speakers."),
 ("12926467a7c78a140099849f25e173349dc9e88f","people-variation-and-health","clinical-and-assistive-speech","clinical-speech-marker","Speech annotation for Parkinson's detection asks which acoustic descriptors reflect a clinical condition rather than recording context."),
 ("39e9e6f5b005b274a971b07373a1ef0939a58b1f","people-variation-and-health","speaker-characteristics","speaker-verification","Multilingual speaker verification must keep identity evidence stable when the language changes."),
("dab4d746066207fd1627bdaf5be41ce61e0c8468","people-variation-and-health","clinical-and-assistive-speech","clinical-speech-marker","Audio-based depression detection asks whether learned acoustic patterns carry a health signal across recordings."),
 ("f5e4f41e1b459fd296cd5a45e80375a4a50aeab2","people-variation-and-health","speaker-characteristics","speaker-verification","Distilling a speaker-verification model must retain identity discrimination while reducing its representation and compute."),
 ("1671667347ae459d1e7fc2aaff651009f6814a9e","languages-accents-and-resources","multilingual-and-crosslingual","crosslingual-transfer","Spoken-to-sign generation transfers linguistic content between spoken language and a visual sign sequence."),
 ("f4290ddf1ba7726c19fbab4515c22dd49eac9650","languages-accents-and-resources","multilingual-and-crosslingual","language-identification","Accent-aware language identification must separate language evidence from pronunciation variation."),
 ("f76b8e5bf1828e1a59fd362967dff8ccfb4b5521","languages-accents-and-resources","low-resource-and-data-creation","few-shot-adaptation","Multilingual low-resource recognition must allocate adaptation capacity where labeled speech is scarce."),
 ("fadd84b448ddaa2a37c87dd1c89414301012a31b","languages-accents-and-resources","multilingual-and-crosslingual","crosslingual-transfer","Speech translation must map between languages while preserving the intended content rather than only acoustic similarity."),
 ("1e470965d610b962554bd756fa4d5d837be4c0e8","evaluation-deployment-and-consequence","privacy-security-and-accountability","spoofing-and-deepfake","Deepfake audio localization must identify manipulated regions rather than output only a whole-recording fake label."),
 ("2299f07e80e65dda8f3b3218b4ae3cf660f0a029","evaluation-deployment-and-consequence","privacy-security-and-accountability","voice-privacy","A defense against voice-cloning attacks treats a person's voice as an identity signal that can be misused."),
 ("f471420095c3cabfdeece782cac28d8eecb64fdc","evaluation-deployment-and-consequence","metrics-and-targets","quality-and-naturalness","Listening-test results for multilingual enhancement ask whether a metric tracks what people actually hear across languages."),
 ("fa75aa083824b68bd7f3fef81f952d81aa59bb54","evaluation-deployment-and-consequence","metrics-and-targets","word-error-versus-understanding","Hearing-aid intelligibility prediction must target listener understanding rather than assume waveform similarity or word error is sufficient."),
]
papers={p["paperId"]:p for p in json.loads((DATA/"icassp-2026-papers.json").read_text())["papers"]}
rows=[]; used=set()
for pid,theme,subtheme,concept,reasoning in A:
    if pid.endswith("?"): raise SystemExit(f"unresolved paper id: {pid}")
    if pid in used: raise SystemExit(f"duplicate in batch: {pid}")
    used.add(pid); p=papers[pid]; abstract=p.get("abstract") or ""; depth="D2" if abstract else "D1"
    rows.append({"paper_id":pid,"title":p["title"],"decision":"supported","confidence":f"analyst-reviewed-{depth}","theme_id":theme,"subtheme_id":subtheme,"concept_id":concept,"semantic_reasoning":reasoning,"evidence_excerpt":abstract[:1000] if abstract else p["title"],"source_location":p.get("url"),"source_sha256":hashlib.sha256(abstract.encode()).hexdigest(),"evidence_depth":depth,"review_state":"analyst-reviewed","claim_boundary":"ICASSP discovery record only; title-only rows support only the named topic, while abstract-backed rows support the stated problem and proposed move. Official proceedings and full-paper mechanism are not established."})
payload={"schema_version":1,"batch_id":"icassp-2026-semantic-batch-011","status":"analyst-reviewed-title-and-abstract-batch","claim_boundary":"These assignments are analyst-reviewed from preserved ICASSP title/abstract records. D1 rows are title-bounded; D2 rows are abstract-bounded. They do not establish full-paper mechanisms or venue-wide prevalence.","reviewed_count":len(rows),"rows":rows}
(DATA/"icassp-2026-semantic-reviewed-batch-011.json").write_text(json.dumps(payload,indent=2,ensure_ascii=False)+"\n")
print(json.dumps({"batch_id":payload["batch_id"],"reviewed_count":len(rows),"D2":sum(x["evidence_depth"]=="D2" for x in rows),"D1":sum(x["evidence_depth"]=="D1" for x in rows)}))
