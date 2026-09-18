#!/usr/bin/env python3
"""Record an eighth balanced analyst-reviewed INTERSPEECH D2 batch."""
from __future__ import annotations
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = HERE / "data"

A = {
"wu25j_interspeech": ("sound-and-production","source-filter-production","vocal-tract-filter","A moving vocal-tract simulation connects articulator geometry to the changing resonances of diphthongs."),
"xiang25b_interspeech": ("sound-and-production","source-filter-production","vocal-tract-filter","Formant dynamics test how speech style and rate change the filter through which a speaker's source is heard."),
"zhao25_interspeech": ("sound-and-production","source-filter-production","periodic-source","Speech-EGG alignment uses vocal-fold timing to study how a glottal stop can disappear during sound change."),
"zhang25i_interspeech": ("sound-and-production","source-filter-production","articulatory-coordination","MRI and respiration measurements connect visible vocal-tract motion with the bodily timing that produces speech."),
"yang25_interspeech": ("listening-and-separation","source-separation-and-spatial-listening","blind-source-separation","Unknown-speaker-count separation must decide both which voices are present and how to isolate them."),
"yang25c_interspeech": ("listening-and-separation","source-separation-and-spatial-listening","target-conditioned-separation","Enrollment audio supplies the identity target needed to extract one requested sound from a mixture."),
"zhao25e_interspeech": ("listening-and-separation","echo-and-reconstruction","acoustic-echo-cancellation","Echo cancellation must estimate the loudspeaker path and remove it without removing the near-end speaker."),
"yang25o_interspeech": ("listening-and-separation","noise-enhancement","speech-prior-denoising","Generative enhancement reconstructs a plausible clean speech signal when noise has hidden parts of the waveform."),
"xia25_interspeech": ("recognition-and-alignment","boundaries-and-sequence-structure","long-context-decoding","Streaming recognition must use enough future context for accuracy without waiting for the whole utterance."),
"ye25b_interspeech": ("recognition-and-alignment","boundaries-and-sequence-structure","alignment","Dysfluent speech analysis needs word timing that preserves repetitions and repairs rather than deleting them as errors."),
"yong25_interspeech": ("recognition-and-alignment","adaptation-and-open-vocabulary","speaker-adaptation","Accent-robust ASR must adapt to speaker and accent variation without mistaking a small low-resource sample for a universal rule."),
"zhou25_interspeech": ("recognition-and-alignment","boundaries-and-sequence-structure","long-context-decoding","Two-pass streaming decoding trades an early usable transcript against later context that can revise uncertain words."),
"paierl25_interspeech": ("meaning-and-interaction","dialogue-and-turn-taking","turn-boundary","A robot listener must predict when a person will finish so its backchannel arrives at the right moment."),
"slomianka25_interspeech": ("meaning-and-interaction","dialogue-and-turn-taking","turn-boundary","Background noise changes the timing cues people use to coordinate turns in a three-person conversation."),
"sasu25b_interspeech": ("meaning-and-interaction","grounding-and-action","speech-act","A robot must use prosody to disambiguate what a spoken instruction is intended to make it do."),
"zhou25f_interspeech": ("meaning-and-interaction","prosody-and-intent","paralinguistic-state","Emotion-inducing tasks test whether speech affect carries useful depression evidence beyond the literal words."),
"xing25_interspeech": ("voice-generation-and-control","prosody-and-interactive-control","style-and-emotion-control","Emotion-adaptive TTS must change delivery style while preserving the requested linguistic content and target voice."),
"zalkow25_interspeech": ("voice-generation-and-control","voice-identity-and-conversion","zero-shot-voice","Low-resource speakers need robust generated voices even when training and inference conditions differ."),
"zhang25c_interspeech": ("voice-generation-and-control","text-to-speech-and-content","text-to-speech-planning","Monotonic attention keeps generated speech aligned with text so the voice does not skip or repeat content."),
"zhao25d_interspeech": ("voice-generation-and-control","voice-identity-and-conversion","zero-shot-voice","A prosody-adaptable codec uses an in-context voice example to change delivery without retraining the converter."),
"yao25b_interspeech": ("people-variation-and-health","speaker-characteristics","speaker-verification","Speaker verification must keep linguistic content separate from identity when text is not fixed."),
"ys25_interspeech": ("people-variation-and-health","clinical-and-assistive-speech","clinical-speech-marker","Dysarthria severity modeling asks whether acoustic and textual cues reflect clinical change rather than task artifacts."),
"yazawa25_interspeech": ("people-variation-and-health","human-centered-evaluation","listener-effort","Fluency ratings depend on who listens and how familiar that listener is with the speaker's language background."),
"mori25_interspeech": ("people-variation-and-health","human-centered-evaluation","listener-effort","Listening selectively in dialogue asks whether ASR evaluation reflects the speech people actually need to understand amid competing talkers."),
"yan25c_interspeech": ("languages-accents-and-resources","multilingual-and-crosslingual","code-switching","A code-switched corpus supplies examples where the recognizer must change language decisions within one utterance."),
"xue25_interspeech": ("languages-accents-and-resources","multilingual-and-crosslingual","crosslingual-transfer","Selective multilingual ASR spends computation where speech is difficult instead of invoking every language model equally."),
"zhuo25_interspeech": ("languages-accents-and-resources","low-resource-and-data-creation","few-shot-adaptation","Vietnamese ASR tests how far large pretrained speech models can go with only 50 hours of local labels."),
"xiong25b_interspeech": ("languages-accents-and-resources","accent-and-cultural-boundaries","accent-robustness","Talker identification changes when listeners and systems are familiar or unfamiliar with an accent's acoustic cues."),
"dutta25b_interspeech": ("evaluation-deployment-and-consequence","privacy-security-and-accountability","spoofing-and-deepfake","Zero-shot spoof detection asks whether an audio-language model recognizes fakery without seeing the attack during training."),
"xiao25c_interspeech": ("evaluation-deployment-and-consequence","privacy-security-and-accountability","auditability-and-contestability","Deepfake source tracing must learn new attack families without retaining every old example."),
"yoneyama25_interspeech": ("evaluation-deployment-and-consequence","robustness-and-system-boundary","latency-and-resource","Streaming vocoders must trade high fidelity against the response time and memory available on the device."),
"zhang25d_interspeech": ("evaluation-deployment-and-consequence","metrics-and-targets","calibration-and-selective-use","An audio encoder benchmark should reveal which capabilities transfer to tasks rather than collapsing quality into one leaderboard score."),
}

papers = {p["paper_id"]: p for p in json.loads((DATA / "interspeech-2025-papers.json").read_text())["papers"]}
rows = []
for paper_id, assignment in A.items():
    paper = papers[paper_id]
    abstract = paper.get("abstract") or ""
    if not abstract:
        raise SystemExit(f"D2 batch requires an abstract: {paper_id}")
    rows.append({"paper_id":paper_id,"title":paper["title"],"decision":"supported","confidence":"analyst-reviewed-D2","theme_id":assignment[0],"subtheme_id":assignment[1],"concept_id":assignment[2],"semantic_reasoning":assignment[3],"evidence_fields":["bp","wh","naive","ap","mech","math","eval","ww","limits"],"evidence_excerpt":abstract[:1200],"source_location":paper["paper_url"],"source_sha256":hashlib.sha256(abstract.encode()).hexdigest(),"evidence_depth":"D2","review_state":"analyst-reviewed","claim_boundary":"Abstract supports the problem and proposed conceptual move; full-paper mechanism, tables, ablations, and limitations remain unreviewed."})
payload={"schema_version":1,"batch_id":"interspeech-2025-semantic-d2-batch-008","status":"analyst-reviewed-D2-batch","claim_boundary":"These 32 assignments are analyst readings bounded by official abstracts; they do not establish full-paper mechanisms or results.","reviewed_count":len(rows),"rows":rows}
(DATA / "interspeech-2025-semantic-reviewed-d2-batch-008.json").write_text(json.dumps(payload,indent=2,ensure_ascii=False)+"\n")
print(json.dumps({"batch_id":payload["batch_id"],"reviewed_count":len(rows),"D2":len(rows)}))
