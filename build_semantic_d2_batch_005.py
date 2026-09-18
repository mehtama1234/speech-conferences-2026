#!/usr/bin/env python3
"""Record a fifth balanced analyst-reviewed INTERSPEECH D2 batch."""
from __future__ import annotations
import hashlib,json
from pathlib import Path
HERE=Path(__file__).resolve().parent; DATA=HERE/"data"
A={
"bendom25_interspeech":("sound-and-production","time-frequency-measurement","multi-resolution-signal","An emotional speech database from speakers with Parkinson's disease makes changing voice quality measurable across health and affect."),
"chen25n_interspeech":("sound-and-production","source-filter-production","vocal-tract-filter","Phonetic posteriorgrams select speech evidence for vocal-cord-disorder classification, linking acoustic patterns to altered production."),
"choi25d_interspeech":("sound-and-production","time-frequency-measurement","sampling-and-quantization","Neural spectral-band generation asks which frequency information can be reconstructed after audio coding removes or compresses it."),
"deluca25_interspeech":("sound-and-production","room-channel-and-sensing","microphone-channel","An interactive voice-data dashboard exposes how recording conditions and speaker variables shape the projections used to explore speech."),
"chen25k_interspeech":("listening-and-separation","source-separation-and-spatial-listening","spatial-filtering","A real-world audio-visual corpus preserves visual and acoustic evidence needed when speech is mixed with competing sources."),
"chi25b_interspeech":("listening-and-separation","noise-enhancement","nonstationary-noise","Device-directed speech detection must distinguish intended speech from changing household or device audio without assuming a fixed noise profile."),
"deng25_interspeech":("listening-and-separation","source-separation-and-spatial-listening","target-conditioned-separation","Speaker adaptation for elderly speech asks whether target-speaker characteristics can guide recognition when voice and environment differ."),
"chochlakis25_interspeech":("listening-and-separation","echo-and-reconstruction","perceptual-enhancement","Modality-agnostic emotion recognition must recover useful affective evidence when one audio or visual channel is missing or corrupted."),
"cheema25_interspeech":("recognition-and-alignment","acoustic-unit-mapping","pronunciation-variation","Neurogram similarity models how hearing loss changes the mapping from speech acoustics to neural responses and perceived units."),
"chen25e_interspeech":("recognition-and-alignment","acoustic-unit-mapping","acoustic-to-token","Speaker-normalized pitch decoded from EEG tests whether perceptual speech information can be recovered from a non-acoustic signal."),
"chi25_interspeech":("recognition-and-alignment","acoustic-unit-mapping","self-supervised-speech-units","Distilling HuBERT asks which learned speech units can remain useful after a larger self-supervised model is made smaller."),
"chae25_interspeech":("recognition-and-alignment","boundaries-and-sequence-structure","alignment","Song-form-aware lyrics generation must align syllable count and linguistic content with musical timing across a full song."),
"bijoy25_interspeech":("meaning-and-interaction","prosody-and-intent","paralinguistic-state","Multilingual emotion recognition must preserve affective cues while allowing language-specific evidence to differ across speakers and varieties."),
"burkhardt25_interspeech":("meaning-and-interaction","prosody-and-intent","prosodic-meaning","A broadened emotional-speech database tests whether emotion categories remain meaningful when speakers and social contexts are not treated as one neutral population."),
"chang25c_interspeech":("meaning-and-interaction","dialogue-and-turn-taking","dialogue-state","Videoconference experience depends on multimodal timing and interaction context, not only on the words in a transcript."),
"chatzichristodoulou25_interspeech":("meaning-and-interaction","prosody-and-intent","intent-in-context","Naturalistic speech emotion recognition combines modalities and training stages because affective meaning is distributed across voice, face, and situation."),
"doan25_interspeech":("voice-generation-and-control","text-to-speech-and-content","neural-vocoder","Real pre-emphasis audio deepfake tracing tests whether generated speech leaves source evidence after waveform processing and resynthesis."),
"elhajal25_interspeech":("voice-generation-and-control","voice-identity-and-conversion","voice-conversion","Rhythm and voice conversion for dysarthric ASR changes delivery while trying to preserve the speaker's linguistic content."),
"futami25_interspeech":("voice-generation-and-control","text-to-speech-and-content","text-to-speech-planning","Interleaving speech and text training for speech-to-speech translation couples linguistic planning with generated vocal output."),
"gao25d_interspeech":("voice-generation-and-control","prosody-and-interactive-control","style-and-emotion-control","Reward optimization for TTS treats desired naturalness or style as a preference signal used to steer generated speech."),
"chen25o_interspeech":("people-variation-and-health","clinical-and-assistive-speech","clinical-speech-marker","Suicidal-risk prediction from speech must separate clinically relevant cues from topic, speaker, and recording correlations."),
"du25b_interspeech":("people-variation-and-health","human-centered-evaluation","accessibility-fit","Emotion-aware audio-language models are evaluated against human-relevant affective distinctions rather than generic audio similarity."),
"bressensdorf25_interspeech":("people-variation-and-health","speaker-characteristics","age-and-development","Agent-based sound-change modeling treats speakers and communities as sources of variation rather than nuisance deviations from one pronunciation."),
"cumani25b_interspeech":("people-variation-and-health","speaker-characteristics","speaker-verification","Score-level fusion for speaker verification asks how multiple uncertain identity measurements should combine before access is granted."),
"ducceschi25_interspeech":("languages-accents-and-resources","accent-and-cultural-boundaries","dialect-and-variety","Transcribing a South Tyrolean dialect into Standard German requires deciding what variation to preserve and what to normalize."),
"elleuch25_interspeech":("languages-accents-and-resources","multilingual-and-crosslingual","language-identification","Arabic dialect identification needs data and labels that distinguish closely related varieties rather than treating Arabic as one language."),
"emezue25_interspeech":("languages-accents-and-resources","low-resource-and-data-creation","speech-data-collection","A culturally rich African-language dataset addresses unequal speech resources by changing who and which varieties are represented."),
"draxler25_interspeech":("languages-accents-and-resources","low-resource-and-data-creation","speech-data-collection","Oral-history transcription must adapt tools and review practices to long, noisy, historically varied recordings."),
"cheng25b_interspeech":("evaluation-deployment-and-consequence","robustness-and-system-boundary","end-to-end-recovery","Multi-channel diarization evaluation must reveal coupled failures in segmentation, speaker identity, and overlap rather than one isolated score."),
"chen25i_interspeech":("evaluation-deployment-and-consequence","metrics-and-targets","calibration-and-selective-use","Fine-grained speech descriptors make an emotion claim inspectable, testing whether explanations correspond to meaningful acoustic evidence."),
"choi25_interspeech":("evaluation-deployment-and-consequence","metrics-and-targets","word-error-versus-understanding","Temporally aligned audio captioning needs evaluation of whether captions identify the right events at the right time, not only fluent text."),
"chang25b_interspeech":("evaluation-deployment-and-consequence","metrics-and-targets","quality-and-naturalness","Spectrotemporal modulation features are evaluated for interpretable classification across speech, music, and environmental sounds, exposing task and domain boundaries."),
}
source=json.loads((DATA/"interspeech-2025-papers.json").read_text())["papers"]; by={p["paper_id"]:p for p in source}; rows=[]
for pid,a in A.items():
 p=by[pid]; abstract=p.get("abstract","")
 rows.append({"paper_id":pid,"title":p["title"],"decision":"supported","confidence":"analyst-reviewed-D2","theme_id":a[0],"subtheme_id":a[1],"concept_id":a[2],"semantic_reasoning":a[3],"evidence_fields":["bp","wh","naive","ap","mech","math","eval","ww","limits"],"evidence_excerpt":abstract[:1200],"source_location":p["paper_url"],"source_sha256":hashlib.sha256(abstract.encode()).hexdigest(),"evidence_depth":"D2","review_state":"analyst-reviewed","claim_boundary":"Abstract supports the problem and proposed conceptual move; full-paper mechanism, tables, ablations, and limitations remain unreviewed."})
payload={"schema_version":1,"batch_id":"interspeech-2025-semantic-d2-batch-005","status":"analyst-reviewed-D2-batch","claim_boundary":"These 32 assignments are analyst readings bounded by official abstracts; they do not establish full-paper mechanisms or results.","reviewed_count":len(rows),"rows":rows}
(DATA/"interspeech-2025-semantic-reviewed-d2-batch-005.json").write_text(json.dumps(payload,indent=2,ensure_ascii=False)+"\n")
print(json.dumps({"batch_id":payload["batch_id"],"reviewed_count":len(rows),"D2":len(rows)}))

