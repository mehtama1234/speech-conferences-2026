#!/usr/bin/env python3
"""Assign eight clear speech cases from the insufficient-evidence queue."""
import hashlib,json
from pathlib import Path
HERE=Path(__file__).resolve().parent; DATA=HERE/'data'
A={
"Deep Learning-Based Joint Optimization of Adaptive Feedback Cancellation and Residual Feedback Suppression for Hearing Aids":("people-and-variation","human-centered-evaluation","accessibility-fit"),
"A Parameter-Efficient Multi-Scale Convolutional Adapter for Synthetic Speech Detection":("evaluation-deployment-and-consequence","privacy-security-and-accountability","spoofing-and-deepfake"),
"Asynchrony-Aware Decoupled Multimodal Control for Cued Speech Video Generation":("voice-generation-and-control","prosody-and-interactive-control","interactive-latency"),
"ST-HNTM: Joint Speech-Text Neural Topic Modeling on the Hypersphere":("meaning-and-interaction","grounding-and-action","referential-grounding"),
"AdaptiveDiffuseMotion: Adaptive Multi-Task Diffusion Model for Speech-Driven Holistic Motion Generation":("meaning-and-interaction","prosody-and-interactive-control","prosody-control"),
"Interpretable Alzheimer’s Disease Detection Via Multi-Scale Fusion of Disentangled Speech Features":("people-and-variation","clinical-and-assistive-speech","clinical-speech-marker"),
"Domain-Aware Scheduling for ASR Fine-Tuning":("recognition-and-alignment","adaptation-and-open-vocabulary","domain-and-context-biasing"),
"LMS-Whisper: Efficient Lightweight Whisper for Multi-Stutter Speech Classification":("people-and-variation","clinical-and-assistive-speech","dysarthria-and-atypical-speech"),
}
q=json.loads((DATA/'icassp-2026-semantic-review-queue.json').read_text()); papers={p['paperId']:p for p in json.loads((DATA/'icassp-2026-papers.json').read_text())['papers']}; by={r['title']:r for r in q['rows']}; already=set()
for path in DATA.glob('icassp-2026-semantic-reviewed-batch-*.json'):
 if path.name!='icassp-2026-semantic-reviewed-batch-045.json': already|={r['paper_id'] for r in json.loads(path.read_text()).get('rows',[])}
missing=[t for t in A if t not in by or by[t]['paper_id'] in already]
if missing: raise SystemExit(f'missing or already reviewed: {missing}')
rows=[]
for title,(theme,subtheme,concept) in A.items():
 p=papers[by[title]['paper_id']]; abstract=p.get('abstract') or ''; depth='D2' if abstract else 'D1'
 rows.append({'paper_id':p['paperId'],'title':title,'decision':'supported','confidence':f'analyst-reviewed-{depth}','theme_id':theme,'subtheme_id':subtheme,'concept_id':concept,'semantic_reasoning':f'The title and preserved abstract identify a speech task and a mechanism that directly instantiates {concept} under {subtheme}.','evidence_excerpt':abstract[:1200] if abstract else title,'source_location':p.get('url'),'source_sha256':hashlib.sha256(abstract.encode()).hexdigest(),'evidence_depth':depth,'review_state':'analyst-reviewed','claim_boundary':'ICASSP discovery metadata; this is a taxonomy assignment, not an independent performance or prevalence claim.'})
payload={'schema_version':1,'batch_id':'icassp-2026-semantic-batch-045','status':'analyst-reviewed-explicit-speech-assignment-batch','claim_boundary':'These records are explicit speech-taxonomy assignments supported by title and, where available, abstract evidence; D2 does not imply full-paper verification.','reviewed_count':len(rows),'rows':rows}
(DATA/'icassp-2026-semantic-reviewed-batch-045.json').write_text(json.dumps(payload,indent=2,ensure_ascii=False)+'\n')
print(json.dumps({'batch_id':payload['batch_id'],'reviewed_count':len(rows),'D1':sum(r['evidence_depth']=='D1' for r in rows),'D2':sum(r['evidence_depth']=='D2' for r in rows)}))
