#!/usr/bin/env python3
import hashlib,json
from pathlib import Path
HERE=Path(__file__).resolve().parent; DATA=HERE/"data"
A={
"xu25d_interspeech":("sound-and-production","time-frequency-measurement","diffusion-spectral-model","Speech enhancement predicts a clean time-frequency structure from noisy speech before waveform reconstruction."),
"tuckute25_interspeech":("sound-and-production","time-frequency-measurement","cochlear-representation","Autoregressive prediction of cochlear tokens tests which sound structure a learned speech representation preserves."),
"luan25_interspeech":("sound-and-production","time-frequency-measurement","spectral-reconstruction","Mel-spectrogram restoration treats an acoustic representation as an image whose missing structure can be recovered."),
"yang25k_interspeech":("sound-and-production","time-frequency-measurement","multichannel-spectral-model","Online multichannel enhancement uses mel-scale spectral structure under changing microphone conditions."),
"wen25b_interspeech":("listening-and-separation","noise-enhancement","individualized-hearing-enhancement","Hearing-impaired listeners need enhancement that joins noise reduction with listener-specific amplification."),
"tao25b_interspeech":("listening-and-separation","source-separation-and-spatial-listening","spherical-array-separation","A spherical microphone array must estimate spatial source statistics before separating overlapping sources."),
"luo25b_interspeech":("listening-and-separation","source-separation-and-spatial-listening","guided-separation","Meeting enhancement combines guided separation with pseudo-labels and signal alignment when clean targets are scarce."),
"wang25t_interspeech":("listening-and-separation","source-separation-and-spatial-listening","unknown-speaker-separation","An attractor-based separator must separate multiple utterances without being told how many speakers are present."),
"sasu25_interspeech":("recognition-and-alignment","acoustic-unit-mapping","prosody-aware-recognition","Pitch-accent information supplies a complementary cue that can improve a pretrained ASR representation."),
"parikh25_interspeech":("recognition-and-alignment","boundaries-and-sequence-structure","phonological-alignment","Mispronunciation scoring must make forced alignment less brittle by adding phonological knowledge."),
"ma25_interspeech":("recognition-and-alignment","acoustic-unit-mapping","phoneme-grapheme-mapping","Phoneme-based recognition must map sound units back to written symbols across languages with limited data."),
"huo25_interspeech":("recognition-and-alignment","acoustic-unit-mapping","representation-probing","Representation differences can be explained by training iteration and what hidden states encode."),
"turavecino25_interspeech":("meaning-and-interaction","prosody-and-intent","privacy-semantic-disentanglement","A private speech representation must retain communicative content while removing identity information."),
"markitantov25_interspeech":("meaning-and-interaction","prosody-and-intent","affective-state-fusion","Affective-state recognition combines modalities whose evidence can agree, conflict, or carry speaker bias."),
"yosha25_interspeech":("meaning-and-interaction","prosody-and-intent","stress-and-meaning","Sentence stress changes which words a listener treats as important, beyond the word sequence."),
"wallbridge25_interspeech":("meaning-and-interaction","prosody-and-intent","prosodic-structure","Self-supervised representations may preserve longer prosodic structure beyond lexical content."),
"li25b_interspeech":("voice-generation-and-control","text-to-speech-and-content","long-context-synthesis","Long-form TTS must carry information across an utterance while keeping local pronunciation and prosody coherent."),
"wang25ba_interspeech":("voice-generation-and-control","prosody-and-interactive-control","disentangled-voice-conversion","Controllable zero-shot voice conversion must change one requested attribute without entangling others."),
"tannander25_interspeech":("voice-generation-and-control","text-to-speech-and-content","accent-control","Swedish TTS must control English insertions instead of applying one fixed accent everywhere."),
"mondal25b_interspeech":("voice-generation-and-control","text-to-speech-and-content","prosodic-teaching-synthesis","Exaggerated word stress can give second-language learners a controllable acoustic teaching signal."),
"sanguedolce25_interspeech":("people-variation-and-health","clinical-and-assistive-speech","physiological-clinical-features","Stroke assessment can use physiologically meaningful glottal and acoustic features."),
"millot25_interspeech":("people-variation-and-health","speaker-characteristics","explainable-speaker-attributes","Speaker recognition needs attributes showing whether identity decisions rely on correlated cues."),
"huang25g_interspeech":("people-variation-and-health","human-centered-evaluation","human-quality-estimation","A human-evaluation toolkit estimates quality across datasets and models, making listener judgments cheaper."),
"zhong25c_interspeech":("people-variation-and-health","human-centered-evaluation","accent-similarity-evaluation","Accent similarity requires listener comparisons that distinguish accent from content and identity."),
"tadevosyan25_interspeech":("languages-accents-and-resources","low-resource-and-data-creation","pseudo-labeling","Semi-supervised ASR uses selected pseudo-labels to turn unlabelled speech into training evidence."),
"yang25p_interspeech":("languages-accents-and-resources","multilingual-and-crosslingual","code-switch-adaptation","Parameter-efficient prompt tuning adapts multilingual ASR to code-switching."),
"karpov25_interspeech":("languages-accents-and-resources","low-resource-and-data-creation","zero-resource-pipeline","A zero-resource ASR pipeline must bootstrap recognition with little or no paired speech-text data."),
"zhang25m_interspeech":("languages-accents-and-resources","low-resource-and-data-creation","child-fluency-resources","Low-resource child-fluency assessment requires both usable speech data and a measure that survives sparse supervision."),
"shi25f_interspeech":("evaluation-deployment-and-consequence","metrics-and-targets","unified-speech-assessment","One speech assessment model should be tested across enhancement, synthesis, and quality-control tasks."),
"srinivasavaradhan25_interspeech":("evaluation-deployment-and-consequence","metrics-and-targets","human-fooling-rate","TTS human-parity claims require deception tests measuring whether listeners distinguish generated speech."),
"song25d_interspeech":("evaluation-deployment-and-consequence","robustness-and-system-boundary","body-conducted-sensing","Skin-attached accelerometers provide a noise-robust signal but must combine with microphones without losing quality."),
"pallala25_interspeech":("evaluation-deployment-and-consequence","robustness-and-system-boundary","target-speaker-extraction","Low-latency target-speaker extraction must preserve the requested voice as competitors and rooms change.")}
papers={p["paper_id"]:p for p in json.loads((DATA/"interspeech-2025-papers.json").read_text())["papers"]}
rows=[]
for pid,a in A.items():
    p=papers[pid]; abstract=p.get("abstract") or ""
    if not abstract: raise SystemExit(f"missing abstract: {pid}")
    rows.append({"paper_id":pid,"title":p["title"],"decision":"supported","confidence":"analyst-reviewed-D2","theme_id":a[0],"subtheme_id":a[1],"concept_id":a[2],"semantic_reasoning":a[3],"evidence_fields":["bp","wh","naive","ap","mech","math","eval","ww","limits"],"evidence_excerpt":abstract[:1400],"source_location":p["paper_url"],"source_sha256":hashlib.sha256(abstract.encode()).hexdigest(),"evidence_depth":"D2","review_state":"analyst-reviewed","claim_boundary":"Abstract supports the problem and proposed move; full-paper mechanism, tables, ablations, and limitations remain unreviewed."})
payload={"schema_version":1,"batch_id":"interspeech-2025-semantic-d2-batch-011","status":"analyst-reviewed-D2-batch","claim_boundary":"These 32 assignments are analyst readings bounded by official abstracts; they do not establish full-paper mechanisms or results.","reviewed_count":len(rows),"rows":rows}
(DATA/"interspeech-2025-semantic-reviewed-d2-batch-011.json").write_text(json.dumps(payload,indent=2,ensure_ascii=False)+"\n")
print(json.dumps({"batch_id":payload["batch_id"],"reviewed_count":len(rows),"D2":len(rows)}))
