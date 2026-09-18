#!/usr/bin/env python3
"""Record a tenth balanced analyst-reviewed INTERSPEECH D2 batch."""
from __future__ import annotations
import hashlib, json
from pathlib import Path
HERE = Path(__file__).resolve().parent
DATA = HERE / "data"
A = {
"hao25_interspeech": ("sound-and-production","room-channel-and-sensing","microphone-channel","A hearing-aid feedback canceller must use the sensed acoustic path while remaining low-latency and low-complexity."),
"hartanto25_interspeech": ("sound-and-production","room-channel-and-sensing","microphone-channel","A microphone array carries location, separation, and room information together, so the system must learn which spatial measurements serve each task."),
"havras25_interspeech": ("sound-and-production","time-frequency-measurement","multi-resolution-signal","Filled pauses are measurable acoustic events whose timing and phonetic form can vary across speakers and languages."),
"hermes25_interspeech": ("sound-and-production","source-filter-production","articulatory-coordination","Congenital lip paralysis makes it possible to ask which acoustic properties remain stable when articulatory choices are constrained."),
"guo25c_interspeech": ("listening-and-separation","noise-enhancement","perceptual-enhancement","Speech coding must preserve perceptually important detail when visual information can help distinguish or reconstruct the sound."),
"geng25_interspeech": ("listening-and-separation","noise-enhancement","speech-prior-denoising","An intelligibility indicator should model what a listener can recover from speech rather than assume waveform quality is enough."),
"he25b_interspeech": ("listening-and-separation","source-separation-and-spatial-listening","spatial-filtering","Generating several sources in binaural space requires controlling both source identity and the spatial cues that place them around a listener."),
"hartuv25_interspeech": ("listening-and-separation","echo-and-reconstruction","perceptual-enhancement","A speech tokenizer should retain phonetic information while compressing the signal into reconstructable acoustic units."),
"gong25_interspeech": ("recognition-and-alignment","adaptation-and-open-vocabulary","domain-and-context-biasing","Contextual biasing supplies rare words to an ASR language model without letting a small requested list overwhelm ordinary recognition."),
"getman25_interspeech": ("recognition-and-alignment","acoustic-unit-mapping","self-supervised-speech-units","Scaling a monolingual speech foundation model raises the question of whether larger representations actually map more reliably to speech units."),
"guillaume25_interspeech": ("recognition-and-alignment","adaptation-and-open-vocabulary","speaker-adaptation","A unified Bayesian account asks how speakers adapt their production to a listener and how that differs between interactive and non-interactive speech."),
"gao25g_interspeech": ("recognition-and-alignment","boundaries-and-sequence-structure","alignment","Audio-visual diarization and recognition must align who spoke, when they spoke, and what was said in multi-person recordings."),
"he25c_interspeech": ("meaning-and-interaction","prosody-and-intent","paralinguistic-state","Emotion recognition combines modalities while trying to keep the affective state stable when one modality contains speaker-specific nuisance information."),
"hegde25_interspeech": ("meaning-and-interaction","dialogue-and-turn-taking","dialogue-state","Dialogue-state tracking depends on what the conversation has established, so in-context examples can change what a spoken turn means."),
"ho25b_interspeech": ("meaning-and-interaction","dialogue-and-turn-taking","repair-and-clarification","Transcript correction must preserve laughter and speech-laugh distinctions because those events affect how a conversation is interpreted."),
"hsu25_interspeech": ("meaning-and-interaction","prosody-and-intent","prosodic-meaning","Rapid acoustic changes can mark syllable progression, linking fine time structure to the listener's segmentation of spoken units."),
"hsiao25_interspeech": ("voice-generation-and-control","text-to-speech-and-content","text-to-speech-planning","A spoken-language model must learn new tasks without forgetting earlier speech capabilities when it is trained end to end."),
"jeon25_interspeech": ("voice-generation-and-control","text-to-speech-and-content","intelligibility-naturalness","Personalized TTS for dysarthric speakers must improve intelligibility while retaining the person's own voice and speaking style."),
"jin25d_interspeech": ("voice-generation-and-control","prosody-and-interactive-control","prosody-control","Text prompts can request several speech attributes, but changing one attribute should not unintentionally change the others."),
"janse25_interspeech": ("voice-generation-and-control","prosody-and-interactive-control","style-and-emotion-control","Lombard speaking style changes when a person talks in noise, so generated or evaluated delivery must account for both vocal effort and listener effort."),
"cumani25_interspeech": ("people-variation-and-health","speaker-characteristics","speaker-verification","Speaker-recognition backends must separate identity evidence from channel and trial variation in a standardized evaluation."),
"griot25_interspeech": ("people-variation-and-health","speaker-characteristics","speaker-verification","Text-dependent verification asks whether identity can be checked while the spoken phrase is fixed and the content cue is controlled."),
"gu25c_interspeech": ("people-variation-and-health","speaker-characteristics","speaker-verification","Domain-robust speaker verification needs representations whose identity structure survives a change in recording domain."),
"hoffner25_interspeech": ("people-variation-and-health","human-centered-evaluation","accessibility-fit","ASR errors in anechoic and spatial signals can reveal hearing-relevant failures that average clean-speech accuracy hides."),
"fang25d_interspeech": ("languages-accents-and-resources","low-resource-and-data-creation","few-shot-adaptation","Few-shot class-incremental audio learning must add new categories without erasing the old ones when labeled examples are scarce."),
"gutscher25_interspeech": ("languages-accents-and-resources","accent-and-cultural-boundaries","dialect-and-variety","Dialect classification links acoustic variation to geographic regions without assuming that a dialect boundary is a clean speaker boundary."),
"grigoryan25_interspeech": ("languages-accents-and-resources","low-resource-and-data-creation","self-training-and-pseudo-labels","Beam-search choices determine how a recognizer spends limited modeling capacity when transducer decoding must scale."),
"hannan25b_interspeech": ("languages-accents-and-resources","low-resource-and-data-creation","few-shot-adaptation","A lightweight ASR training framework asks how to retain useful recognition with limited model and data resources."),
"dong25d_interspeech": ("evaluation-deployment-and-consequence","metrics-and-targets","word-error-versus-understanding","Tone variation tests whether a recognition or phonetic analysis captures the contrast listeners use for lexical meaning."),
"febrinanto25_interspeech": ("evaluation-deployment-and-consequence","privacy-security-and-accountability","spoofing-and-deepfake","Deepfake detection must remain useful when new attacks arrive, so rehearsal should preserve old attack evidence while learning new ones."),
"gan25b_interspeech": ("evaluation-deployment-and-consequence","robustness-and-system-boundary","latency-and-resource","Speech compression trades bitrate against preserved meaning, so semantic equivalence is a deployment target beyond waveform fidelity."),
"fang25c_interspeech": ("evaluation-deployment-and-consequence","robustness-and-system-boundary","distribution-shift","Text-to-audio retrieval must connect language queries to acoustic events across token scales and unseen audio conditions."),
}
papers = {p["paper_id"]: p for p in json.loads((DATA / "interspeech-2025-papers.json").read_text())["papers"]}
rows = []
for pid, assignment in A.items():
    paper = papers[pid]
    abstract = paper.get("abstract") or ""
    if not abstract:
        raise SystemExit(f"D2 batch requires an abstract: {pid}")
    rows.append({"paper_id":pid,"title":paper["title"],"decision":"supported","confidence":"analyst-reviewed-D2","theme_id":assignment[0],"subtheme_id":assignment[1],"concept_id":assignment[2],"semantic_reasoning":assignment[3],"evidence_fields":["bp","wh","naive","ap","mech","math","eval","ww","limits"],"evidence_excerpt":abstract[:1200],"source_location":paper["paper_url"],"source_sha256":hashlib.sha256(abstract.encode()).hexdigest(),"evidence_depth":"D2","review_state":"analyst-reviewed","claim_boundary":"Abstract supports the problem and proposed conceptual move; full-paper mechanism, tables, ablations, and limitations remain unreviewed."})
payload={"schema_version":1,"batch_id":"interspeech-2025-semantic-d2-batch-010","status":"analyst-reviewed-D2-batch","claim_boundary":"These 32 assignments are analyst readings bounded by official abstracts; they do not establish full-paper mechanisms or results.","reviewed_count":len(rows),"rows":rows}
(DATA / "interspeech-2025-semantic-reviewed-d2-batch-010.json").write_text(json.dumps(payload,indent=2,ensure_ascii=False)+"\n")
print(json.dumps({"batch_id":payload["batch_id"],"reviewed_count":len(rows),"D2":len(rows)}))
