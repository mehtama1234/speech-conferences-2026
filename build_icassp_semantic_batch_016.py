#!/usr/bin/env python3
import hashlib,json
from pathlib import Path
HERE=Path(__file__).resolve().parent; DATA=HERE/'data'
RULES={
 'Integrating Speaker Embeddings and LLM-Derived Semantic Representations for Streaming Speaker Diarization':('supported','listening-and-separation','source-separation-and-spatial-listening','blind-source-separation','Streaming diarization must use speaker identity and language context while speech arrives.'),
 'Scale: Semantic Chunking and Label-Delay Engine For Streaming Speech-LLM':('supported','recognition-and-alignment','boundaries-and-sequence-structure','long-context-decoding','Streaming speech models need explicit chunk and label-delay rules to trade context against response time.'),
 'Direct Transfer of Prosody in Speech-to-speech Translation using Disentangled Speech Tokens':('supported','voice-generation-and-control','prosody-and-interactive-control','prosody-control','Speech translation must transfer prosody without copying unrelated source-speaker properties.'),
 'SpeechCT-CLIP: Distilling Text-Image Knowledge to Speech for Voice-Native Multimodal CT Analysis':('supported','people-variation-and-health','clinical-and-assistive-speech','clinical-speech-marker','Speech is used as a voice-native input to a medical multimodal task.'),
 'EnTA-Align: Heterogeneous Model Ensemble with Dual-Path Fusion for Text-Audio Alignment':('supported','meaning-and-interaction','grounding-and-action','referential-grounding','Text-audio alignment tests whether sound and language refer to the same content.'),
 'Acoustic Feedback Cancellation in Hearing Aids Exploiting an Inertial Sensor':('supported','listening-and-separation','echo-and-reconstruction','acoustic-echo-cancellation','A hearing aid must remove its own feedback while preserving the desired sound.'),
 'Snore Sound Classification Based on Physiological Features and Adaptive Loss Function':('unsupported',None,None,None,'Snore classification concerns a physiological sleep sound, not speech or spoken interaction.'),
 'TAG: Structured Temporal Audio Generation via LLM-Guided Manual Scription and Control':('unsupported',None,None,None,'Generic temporal audio generation supplies no speech-specific target in the title evidence.')}
source=json.loads((DATA/'icassp-2026-papers.json').read_text())['papers']; by={p['title']:p for p in source}; rows=[]
for title,rule in RULES.items():
 p=by.get(title)
 if not p: raise SystemExit('missing title: '+title)
 a=p.get('abstract') or ''; depth='D2' if a else 'D1'; decision,theme,subtheme,concept,reason=rule
 rows.append({'paper_id':p['paperId'],'title':title,'decision':decision,'confidence':f'analyst-reviewed-{depth}','theme_id':theme,'subtheme_id':subtheme,'concept_id':concept,'semantic_reasoning':reason,'evidence_excerpt':a[:1000] if a else title,'source_location':p.get('url'),'source_sha256':hashlib.sha256(a.encode()).hexdigest(),'evidence_depth':depth,'review_state':'analyst-reviewed','claim_boundary':'ICASSP title/abstract evidence supports only broad membership or bounded rejection; full-paper mechanism and results are not captured.'})
payload={'schema_version':1,'batch_id':'icassp-2026-semantic-batch-016','status':'analyst-reviewed-title-bounded-mixed-batch','claim_boundary':'Eight records are analyst-reviewed from ICASSP title/abstract evidence; assignments are not full-paper analyses.','reviewed_count':len(rows),'rows':rows}
(DATA/'icassp-2026-semantic-reviewed-batch-016.json').write_text(json.dumps(payload,indent=2,ensure_ascii=False)+'\n'); print(json.dumps({'batch_id':payload['batch_id'],'reviewed_count':len(rows),'supported':sum(x['decision']=='supported' for x in rows),'unsupported':sum(x['decision']=='unsupported' for x in rows)}))
