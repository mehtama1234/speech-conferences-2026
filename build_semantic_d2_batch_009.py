#!/usr/bin/env python3
"""Record a ninth balanced analyst-reviewed INTERSPEECH D2 batch."""
from __future__ import annotations
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = HERE / "data"

A = {
"gupta25_interspeech": ("sound-and-production","time-frequency-measurement","multi-resolution-signal","Hear-through filtering must preserve speech cues while suppressing environmental sound under the computation and latency limits of an earbud."),
"han25_interspeech": ("sound-and-production","room-channel-and-sensing","microphone-channel","Speaker diarization depends on representations that retain who spoke while compressing the acoustic information used to separate speakers."),
"ibrahimov25_interspeech": ("sound-and-production","room-channel-and-sensing","non-airborne-sensing","Ultrasound-to-speech asks whether articulatory measurements can supply speech information when an ordinary acoustic microphone is unavailable."),
"halpern25_interspeech": ("sound-and-production","time-frequency-measurement","multi-resolution-signal","Speech quality in head-and-neck-cancer patients requires relating measurable acoustic properties to what listeners actually perceive."),
"han25c_interspeech": ("listening-and-separation","noise-enhancement","spectral-mask","A spatially aware enhancement model must suppress interference while preserving the speech cues carried by multiple microphone channels."),
"gao25_interspeech": ("listening-and-separation","noise-enhancement","speech-prior-denoising","A compact enhancement model must infer speech from a noisy mixture while keeping enough detail for intelligibility."),
"gan25_interspeech": ("listening-and-separation","source-separation-and-spatial-listening","target-conditioned-separation","Speaker verification can use relations among informative regions of an utterance to decide whether a target identity is present."),
"grossman25_interspeech": ("listening-and-separation","source-separation-and-spatial-listening","blind-source-separation","A multi-speaker, speaker-tagged corpus turns overlapping or mixed conversation into data for separating and attributing voices."),
"geng25c_interspeech": ("recognition-and-alignment","acoustic-unit-mapping","pronunciation-variation","Low-resource recognition tests whether learned acoustic units map reliably to words in a language with little labeled speech."),
"freisinger25_interspeech": ("recognition-and-alignment","boundaries-and-sequence-structure","alignment","Transcript segmentation is a boundary problem: the system must place structure in a long sequence rather than only predict its words."),
"ghosh25_interspeech": ("recognition-and-alignment","boundaries-and-sequence-structure","disfluency-preservation","Dysfluency segmentation must locate irregular speech events without treating repetitions and disruptions as disposable recognition errors."),
"gao25c_interspeech": ("recognition-and-alignment","acoustic-unit-mapping","pronunciation-variation","Child speech recognition and reading-mistake detection must map variable pronunciations to the intended words and errors."),
"gomezzaragoza25_interspeech": ("meaning-and-interaction","prosody-and-intent","paralinguistic-state","Depression detection asks whether vocal and textual patterns carry a speaker state that is not stated directly in the words."),
"gong25b_interspeech": ("meaning-and-interaction","prosody-and-intent","paralinguistic-state","Low-resource emotion recognition asks how much affective meaning can be learned when examples of the relevant speaking state are scarce."),
"gong25c_interspeech": ("meaning-and-interaction","dialogue-and-turn-taking","dialogue-state","Meeting summarization evaluation must compare system outputs by whether they preserve the important state and events of a conversation."),
"halim25_interspeech": ("meaning-and-interaction","prosody-and-intent","intent-in-context","Ambiguous emotion recognition requires examining token-level evidence instead of assuming that one utterance has a single obvious affective label."),
"hu25i_interspeech": ("voice-generation-and-control","voice-identity-and-conversion","voice-conversion","Zero-shot voice conversion must change the speaker characteristics while restoring content and avoiding unwanted identity leakage."),
"jacquelin25_interspeech": ("voice-generation-and-control","prosody-and-interactive-control","prosody-control","Vocal effort is a controllable dimension of delivery; disentangling it from content and identity makes deliberate style change possible."),
"mayer25_interspeech": ("voice-generation-and-control","prosody-and-interactive-control","style-and-emotion-control","Stochastic prosody modeling treats speaking style as a distribution of possible timing and pitch patterns rather than one fixed trajectory."),
"kaneko25_interspeech": ("voice-generation-and-control","voice-identity-and-conversion","voice-conversion","A distilled one-step voice converter trades iterative refinement for speed while trying to preserve the desired identity transformation."),
"greenberg25_interspeech": ("people-variation-and-health","speaker-characteristics","speaker-verification","A speaker-recognition evaluation asks whether identity decisions remain reliable across changing speakers, channels, and test conditions."),
"harmsen25_interspeech": ("people-variation-and-health","human-centered-evaluation","accessibility-fit","Using ASR to measure child reading fluency is only useful if automatic errors track the human construct that educators intend to measure."),
"hidalgojulia25_interspeech": ("people-variation-and-health","clinical-and-assistive-speech","clinical-speech-marker","Depression biomarkers require separating vocal and facial signals associated with illness from variation caused by remote recording and individual differences."),
"hu25d_interspeech": ("people-variation-and-health","clinical-and-assistive-speech","dysarthria-and-atypical-speech","Dysarthric recognition tests whether a speech foundation model can route each input to a useful adaptation without treating atypical speech as ordinary variation."),
"gao25f_interspeech": ("languages-accents-and-resources","multilingual-and-crosslingual","cultural-meaning","A cross-lingual sarcasm dataset tests whether multimodal cues retain social meaning when the language and cultural context change."),
"klejch25_interspeech": ("languages-accents-and-resources","low-resource-and-data-creation","few-shot-adaptation","A low-resource language case study exposes the data, modeling, and evaluation choices required when standard ASR assumptions do not hold."),
"li25ca_interspeech": ("languages-accents-and-resources","low-resource-and-data-creation","few-shot-adaptation","Endangered-language recognition asks whether a model can learn from context and very limited examples without importing the wrong language structure."),
"maison25_interspeech": ("languages-accents-and-resources","accent-and-cultural-boundaries","accent-robustness","A Quebec French corpus makes accent variation visible as a distribution that recognition systems must model rather than erase."),
"durmus25_interspeech": ("evaluation-deployment-and-consequence","metrics-and-targets","calibration-and-selective-use","A diarization benchmark is useful only if its tasks and metrics reveal the errors that matter for different numbers of speakers and recording conditions."),
"do25_interspeech": ("evaluation-deployment-and-consequence","robustness-and-system-boundary","latency-and-resource","On-device spoken-language understanding exposes the tradeoff between a smaller model, response speed, and the language coverage it can retain."),
"hu25j_interspeech": ("evaluation-deployment-and-consequence","privacy-security-and-accountability","voice-privacy","Private speaker verification must decide identity without exposing a reusable representation of the speaker's voice."),
"rai25_interspeech": ("evaluation-deployment-and-consequence","privacy-security-and-accountability","auditability-and-contestability","An equity benchmark makes subgroup error differences inspectable so that a recognition system can be challenged rather than summarized by one average score."),
}

papers = {p["paper_id"]: p for p in json.loads((DATA / "interspeech-2025-papers.json").read_text())["papers"]}
rows = []
for paper_id, assignment in A.items():
    paper = papers[paper_id]
    abstract = paper.get("abstract") or ""
    if not abstract:
        raise SystemExit(f"D2 batch requires an abstract: {paper_id}")
    rows.append({"paper_id":paper_id,"title":paper["title"],"decision":"supported","confidence":"analyst-reviewed-D2","theme_id":assignment[0],"subtheme_id":assignment[1],"concept_id":assignment[2],"semantic_reasoning":assignment[3],"evidence_fields":["bp","wh","naive","ap","mech","math","eval","ww","limits"],"evidence_excerpt":abstract[:1200],"source_location":paper["paper_url"],"source_sha256":hashlib.sha256(abstract.encode()).hexdigest(),"evidence_depth":"D2","review_state":"analyst-reviewed","claim_boundary":"Abstract supports the problem and proposed conceptual move; full-paper mechanism, tables, ablations, and limitations remain unreviewed."})
payload={"schema_version":1,"batch_id":"interspeech-2025-semantic-d2-batch-009","status":"analyst-reviewed-D2-batch","claim_boundary":"These 32 assignments are analyst readings bounded by official abstracts; they do not establish full-paper mechanisms or results.","reviewed_count":len(rows),"rows":rows}
(DATA / "interspeech-2025-semantic-reviewed-d2-batch-009.json").write_text(json.dumps(payload,indent=2,ensure_ascii=False)+"\n")
print(json.dumps({"batch_id":payload["batch_id"],"reviewed_count":len(rows),"D2":len(rows)}))
