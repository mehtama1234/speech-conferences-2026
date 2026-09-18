#!/usr/bin/env python3
"""Record a third balanced ICASSP abstract-level semantic review batch."""
from __future__ import annotations
import hashlib, json
from pathlib import Path
HERE=Path(__file__).resolve().parent; DATA=HERE/"data"
ASSIGNMENTS={
 "5c6d33c016ff":("sound-and-production","room-channel-and-sensing","microphone-channel","Multi-channel speech enhancement uses the sensor arrangement and spatial evidence to reconstruct speech rather than treating the recording as a single clean stream."),
 "6adaacb3eaa8":("sound-and-production","room-channel-and-sensing","reverberant-mixture","Room-impulse-response denoising models the acoustic path itself, connecting measured sound to the room that produced it."),
 "8fdee400f75a":("sound-and-production","source-filter-production","periodic-source","Phonation-mode classification in singing asks how source vibration and vocal production alter the observed sound."),
 "72193e2de974":("sound-and-production","time-frequency-measurement","multi-resolution-signal","Ultra-low-bitrate speech coding must preserve articulatory information while compressing the changing signal into few tokens."),
 "f0556f0e9a55":("listening-and-separation","source-separation-and-spatial-listening","blind-source-separation","A unified generative system handles enhancement and separation because mixtures contain both unwanted noise and competing speech sources."),
 "fdc47da159b6":("listening-and-separation","noise-enhancement","nonstationary-noise","Real-world speech enhancement changes with device and environment, so lightweight adaptation must follow the observed degradation."),
 "6c78ad33fed0":("listening-and-separation","source-separation-and-spatial-listening","blind-source-separation","Independent vector analysis separates mixed acoustic sources by modeling statistical dependence and updating the demixing online."),
 "cd3019a89f4f":("listening-and-separation","source-separation-and-spatial-listening","target-conditioned-separation","The method extracts a closely moving target speaker, using target evidence to keep one source while other sources move."),
 "29ca7953fa67":("recognition-and-alignment","acoustic-unit-mapping","acoustic-to-token","Learnable projection reduces prompt sensitivity in speech recognition by controlling how acoustic representations enter a language model."),
 "69f7a435ef27":("recognition-and-alignment","acoustic-unit-mapping","acoustic-to-token","Visual features supply missing speech evidence when the acoustic channel is noisy, improving audio-visual ASR mapping."),
 "a865cfc4e91b":("recognition-and-alignment","boundaries-and-sequence-structure","long-context-decoding","Speaker-attributed ASR must align words with speaker identity, not only produce an unlabelled token stream."),
 "eff379d6545c":("recognition-and-alignment","adaptation-and-open-vocabulary","domain-and-context-biasing","Orthographic and language-specific evaluation asks whether recognition errors reflect usable words in Indian-language settings rather than only a generic WER."),
 "7571ad7c1a0a":("meaning-and-interaction","prosody-and-intent","paralinguistic-state","Activation steering changes emotional attributes in generated speech, treating affect as a controllable state rather than a fixed speaker label."),
 "8b6a6f22bc92":("meaning-and-interaction","dialogue-and-turn-taking","dialogue-state","Injected emotional attribution gives a spoken language model an intermediate account of how the speaker’s state should affect an interaction."),
 "a127f6df9b9a":("meaning-and-interaction","dialogue-and-turn-taking","turn-boundary","Empathetic dialogue requires choosing when to validate and respond; timing detection connects paralinguistic cues to an interactional action."),
 "b7efe85da9a2":("meaning-and-interaction","prosody-and-intent","intent-in-context","Human perception of AI-dubbed content depends on how acoustic and visual cues combine, so response quality cannot be reduced to text similarity."),
 "39725966a2b7":("voice-generation-and-control","prosody-and-interactive-control","style-and-emotion-control","Personalized avatars require disentangling speaking style and motion control so identity and expression can be changed deliberately."),
 "83eb5e352285":("voice-generation-and-control","text-to-speech-and-content","text-to-speech-planning","Accented speech synthesis must preserve phonological rules while producing a controllable voice, linking language planning to acoustic output."),
 "d1020efad23d":("voice-generation-and-control","text-to-speech-and-content","interactive-latency","On-phone TTS treats latency, memory, and waveform quality as coupled generation constraints rather than optimizing naturalness alone."),
 "838fc7aa4de":("voice-generation-and-control","text-to-speech-and-content","intelligibility-naturalness","Localizing low-quality TTS artifacts asks which regions of generated speech damage perceived quality and where repair should focus."),
 "70672c82c304":("people-variation-and-health","speaker-characteristics","speaker-verification","Spoofing detection changes when speaker identity is present, so identity is a nuisance and a security signal at once."),
 "2b40f524c897":("people-variation-and-health","human-centered-evaluation","listener-effort","Distinguishing real and synthetic super-resolved audio tests whether embedding decisions correspond to a listener-relevant authenticity boundary."),
 "8c76937b26e8":("people-variation-and-health","speaker-characteristics","style-and-state-variation","Lip-to-speech synthesis must preserve prosody while the visual speaker and acoustic voice vary, exposing how style is tied to identity."),
 "a71a0571289f":("people-variation-and-health","human-centered-evaluation","accessibility-fit","Perceptual quality assessment for singing-face generation asks what human listeners value when speech and visual identity are jointly generated."),
 "783ca1357287":("languages-accents-and-resources","multilingual-and-crosslingual","crosslingual-transfer","Dynamic expert projectors add multilingual speech capacity while routing different language structure to different experts."),
 "e72eae582cd3":("languages-accents-and-resources","multilingual-and-crosslingual","speech-data-collection","A curated multilingual speaker-verification dataset addresses unequal language coverage and the need to compare identity across varieties."),
 "d18fc2002429":("languages-accents-and-resources","low-resource-and-data-creation","self-training-and-pseudo-labels","Teacher updates and ensemble pseudo-labels improve unsupervised ASR adaptation when target-domain transcripts are scarce."),
 "ee679d36127c":("languages-accents-and-resources","accent-and-cultural-boundaries","dialect-and-variety","Multi-dialect Arabic SSL must represent shared speech structure without erasing differences among dialects."),
 "fdfc05a09b7d":("evaluation-deployment-and-consequence","privacy-security-and-accountability","voice-privacy","Content leakage tests whether anonymized speaker representations still expose the words that identify or reconstruct a person’s speech."),
 "b82356b06dc1":("evaluation-deployment-and-consequence","metrics-and-targets","quality-and-naturalness","Ultra-low-bitrate codec evaluation asks whether a compact token stream preserves speech quality rather than only minimizing signal distortion."),
 "51d6cdd34dd2":("evaluation-deployment-and-consequence","privacy-security-and-accountability","spoofing-and-deepfake","Deepfake detection at a short greeting tests whether a security decision survives very little speech evidence and realistic conversational entry points."),
 "bf6c53ec9bca":("evaluation-deployment-and-consequence","metrics-and-targets","calibration-and-selective-use","Text-audio relevance scoring evaluates whether an automatic metric tracks semantic alignment in generated audio instead of merely acoustic similarity."),
}
source=json.loads((DATA/"icassp-2026-papers.json").read_text())["papers"]; by={p["paperId"]:p for p in source}; rows=[]
for prefix,a in ASSIGNMENTS.items():
 p=next(p for pid,p in by.items() if pid.startswith(prefix)); abstract=p.get("abstract") or ""
 rows.append({"paper_id":p["paperId"],"title":p["title"],"decision":"supported","confidence":"analyst-reviewed-D2","theme_id":a[0],"subtheme_id":a[1],"concept_id":a[2],"semantic_reasoning":a[3],"evidence_excerpt":abstract[:1000],"source_location":p.get("url"),"source_sha256":hashlib.sha256(abstract.encode()).hexdigest(),"evidence_depth":"D2","review_state":"analyst-reviewed","claim_boundary":"ICASSP discovery/abstract record only; official proceedings and full-paper mechanism are not established."})
payload={"schema_version":1,"batch_id":"icassp-2026-semantic-batch-003","status":"analyst-reviewed-D2-batch","claim_boundary":"These 32 assignments are analyst-reviewed from preserved ICASSP abstract records. They do not establish full-paper mechanisms or venue-wide prevalence.","reviewed_count":len(rows),"rows":rows}
(DATA/"icassp-2026-semantic-reviewed-batch-003.json").write_text(json.dumps(payload,indent=2,ensure_ascii=False)+"\n")
print(json.dumps({"batch_id":payload["batch_id"],"reviewed_count":len(rows),"D2":sum(r["evidence_depth"]=="D2" for r in rows)}))
