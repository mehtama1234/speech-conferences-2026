#!/usr/bin/env python3
import hashlib,json
from pathlib import Path
HERE=Path(__file__).resolve().parent; DATA=HERE/"data"
A=[
("02243661b4fee8c9a88d369aa883fa870956ec84","recognition-and-alignment","adaptation-and-open-vocabulary","audio-language-adaptation","Audio-language domain adaptation must align labels when the audio distribution changes but the label space is closed."),
("3c4b3a29df5e8841a5f1b92d67b6a3c285c355cd","listening-and-separation","source-separation-and-spatial-listening","target-speaker-separation","Edge target-speaker extraction must use visual and acoustic evidence while meeting a real-time budget."),
("4b580de823ac5593b4bedaecb0e2fd33fba3b352","recognition-and-alignment","acoustic-unit-mapping","asr-error-estimation","Predicting edit operations makes ASR quality finer than one aggregate word-error number."),
("52756cff017ebb99ec3d75a4560d7fc4b9668806","people-variation-and-health","clinical-and-assistive-speech","dysarthric-recognition","Phoneme guidance and language knowledge can help recognition when dysarthric articulation breaks ordinary acoustic-to-text mappings."),
("5331fe1016a8ff681a7dc5873b28d4ee98a107b8","listening-and-separation","source-separation-and-spatial-listening","continual-audio-separation","Continual audio-visual separation must learn new mixtures without forgetting earlier source distinctions."),
("60d255bd00b63837339b03c74ab44e4a7691653f","listening-and-separation","source-separation-and-spatial-listening","audio-visual-separation","A speaker-image separator uses who is visible to decide which acoustic stream to retain."),
("7ffe20657d03f2e520c2368b5d262a64a59ca3ee","voice-generation-and-control","prosody-and-interactive-control","speech-driven-motion","Speech-driven body motion must preserve speaker identity while generating controllable movement."),
("8c34befb5bf60724639cf82f2b05b5a52242a7d2","voice-generation-and-control","text-to-speech-and-content","flow-tts","Rapid speech synthesis trades fewer flow-matching steps against waveform quality and intelligibility."),
("912db650c4cc9a3db2cf2c003c7a1b797ca7009e","listening-and-separation","source-separation-and-spatial-listening","prompted-separation","A smart-glasses separator uses a text prompt to identify the requested source in a multichannel mixture."),
("9862889a562e2a2896cfca777aad486f876a6221","languages-accents-and-resources","low-resource-and-data-creation","synthetic-data-selection","Low-resource Māori ASR needs a rule for selecting useful synthetic speech rather than trusting all generated examples."),
("a68f6358f5e03df7c2c79c7efca1ec5de8829220","evaluation-deployment-and-consequence","privacy-security-and-accountability","speech-privacy","Privacy-aware ASR must block sensitive acoustic triggers while preserving ordinary recognition."),
("ae0b1f3f46c4244609dc7deb1b925ca5eb495982","listening-and-separation","source-separation-and-spatial-listening","audio-visual-enhancement","Visual speech evidence can guide separation when acoustic sources overlap."),
("d9b1ef17ca01a3e13e6b0fdd761a079b2585e1a0","listening-and-separation","source-separation-and-spatial-listening","inference-time-separation","Source separation can spend extra inference computation at test time when the mixture is unusually difficult."),
("deef773b3c27f7fd5de51ea7329364cf23586315","listening-and-separation","source-separation-and-spatial-listening","synthetic-mixture-design","Universal separation depends on synthetic mixtures whose distance and room cues resemble the mixtures encountered later."),
("eeb002d55758577c6fea97304ea9d8db8d3e0b55","recognition-and-alignment","acoustic-unit-mapping","asr-distillation","Generative reconstruction pathways transfer useful speech structure into a smaller end-to-end recognizer."),
("f0855377153ed857c099d62cf84a0bdedeb3db2d","voice-generation-and-control","text-to-speech-and-content","flow-tts","Neighborhood consistency in flow matching stabilizes rapid text-to-speech synthesis."),
("f13d00332d028e499f5fce9073ee2936aa373ef3","people-variation-and-health","speaker-characteristics","speaker-domain-adaptation","Speaker verification must adapt to a new domain without losing the identity evidence learned before adaptation."),
("f1ad862c634587bcf8357c1e958d1b58764a9919","voice-generation-and-control","text-to-speech-and-content","text-normalization","TTS must normalize non-standard written forms into pronunciable language before acoustic generation."),
("f9b9441f4c573b538dced6abc5d338b5f575a271","recognition-and-alignment","acoustic-unit-mapping","efficient-speech-representation","Head pruning tests which parts of a self-supervised speech recognizer are necessary for recognition."),
("fdcb2a96a83e0b410af16d270de3604188a0f634","voice-generation-and-control","prosody-and-interactive-control","emotional-voice-conversion","Emotional voice conversion must change intensity while retaining the target speaker's identity."),
("2b3bcd44dd8fd6a8819f6743cc2eb66870941ff3","people-variation-and-health","clinical-and-assistive-speech","dysarthria-assessment","ASR adaptation can estimate dysarthria severity only if recognition errors are separated from clinical evidence."),
("352089123e1bd0373c317ff162afe29946d15b9d","evaluation-deployment-and-consequence","privacy-security-and-accountability","speech-watermarking","Speech authentication must detect whether a recording carries a trustworthy provenance signal."),
("537488e9a529c552272d9361c2349f9e5274bc53","voice-generation-and-control","text-to-speech-and-content","codec-tts","Codec-based TTS predicts several discrete acoustic codebooks while controlling generation cost."),
("5f993544b3607f0c819297f710985bf7bf671b93","voice-generation-and-control","voice-identity-and-conversion","privacy-preserving-conversion","Voice conversion must alter identity while preserving the speaker's mental-health-relevant vocal content."),
("6cfea1f4e985754dc1fa8ec28e7482aa89308291","recognition-and-alignment","boundaries-and-sequence-structure","multichannel-asr","Multi-channel multi-speaker ASR must organize streams and sentence order before transcription becomes usable."),
("73d69ca576dc8e65e0f4826f6f6c3db3d0e8a2f2","people-variation-and-health","clinical-and-assistive-speech","dysarthric-corpus","A dysarthric speech corpus makes speaker and condition variation available for models that otherwise confuse pathology with identity."),
("76027423d418665db7a133787c6b817143a9112f","evaluation-deployment-and-consequence","privacy-security-and-accountability","spoofing-and-deepfake","Speaker verification must face speech-generation attacks recorded in the wild rather than only laboratory spoofs."),
("834c6c9aa5de738060ebf7e41deb082e5c23e7ae","listening-and-separation","noise-enhancement","audio-visual-enhancement","Audiovisual enhancement combines visual speech and recognition features to preserve words under acoustic interference."),
("8bb0a3187e680dd770ec55c68546d74ef05e8216","people-variation-and-health","clinical-and-assistive-speech","dysarthria-assessment","Syllable-level acoustic modeling tests whether timing and pronunciation patterns reveal ALS severity."),
("9df0b5000a1dedc69a16a7d3cd12448a0f671fb5","people-variation-and-health","clinical-and-assistive-speech","child-speech-recognition","Child ASR must learn through label-noise-aware temporal decisions when pronunciation differs from adult speech."),
("a90b2cf4bc51065b9cd7ece3552bfa0821b1597b","recognition-and-alignment","adaptation-and-open-vocabulary","speech-domain-adaptation","Cross-modal self-training adapts speech recognition without requiring a fully labeled target domain."),
("b3fb63852e7054a894168d220324bd4148249207","languages-accents-and-resources","low-resource-and-data-creation","low-resource-representation","Low-resource speech recognition needs representations that imitate useful features without large paired corpora."),
]
papers={p["paperId"]:p for p in json.loads((DATA/"icassp-2026-papers.json").read_text())["papers"]}
rows=[]; used=set()
for pid,theme,subtheme,concept,reasoning in A:
 if pid in used: raise SystemExit(f"duplicate {pid}")
 if pid not in papers: raise SystemExit(f"missing {pid}")
 used.add(pid); p=papers[pid]; abstract=p.get("abstract") or ""; depth="D2" if abstract else "D1"
 rows.append({"paper_id":pid,"title":p["title"],"decision":"supported","confidence":f"analyst-reviewed-{depth}","theme_id":theme,"subtheme_id":subtheme,"concept_id":concept,"semantic_reasoning":reasoning,"evidence_excerpt":abstract[:1000] if abstract else p["title"],"source_location":p.get("url"),"source_sha256":hashlib.sha256(abstract.encode()).hexdigest(),"evidence_depth":depth,"review_state":"analyst-reviewed","claim_boundary":"ICASSP discovery record only; title-only rows support only the named topic, while abstract-backed rows support the stated problem and proposed move. Full-paper mechanism is not established."})
payload={"schema_version":1,"batch_id":"icassp-2026-semantic-batch-012","status":"analyst-reviewed-title-and-abstract-batch","claim_boundary":"These 32 assignments are analyst-reviewed from preserved ICASSP title/abstract records. D1 rows are title-bounded; D2 rows are abstract-bounded. They do not establish full-paper mechanisms or venue-wide prevalence.","reviewed_count":len(rows),"rows":rows}
(DATA/"icassp-2026-semantic-reviewed-batch-012.json").write_text(json.dumps(payload,indent=2,ensure_ascii=False)+"\n")
print(json.dumps({"batch_id":payload["batch_id"],"reviewed_count":len(rows),"D2":sum(x["evidence_depth"]=="D2" for x in rows),"D1":sum(x["evidence_depth"]=="D1" for x in rows)}))
