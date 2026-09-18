#!/usr/bin/env python3
"""Assign eight clearly speech-specific ICASSP ambiguity cases."""
import hashlib, json
from pathlib import Path
HERE=Path(__file__).resolve().parent; DATA=HERE/'data'
assignments={
"MSANET: Multi-Scale Semantic Aggregation Network for Brain-Assisted Speech Enhancement in Multi-Speaker Conditions":("listening-and-separation","noise-enhancement","speech-prior-denoising"),
"Spatial Covariance Matrix Reconstruction for Speech Enhancement in Reverberant Multi-Source Environments":("listening-and-separation","source-separation-and-spatial-listening","spatial-filtering"),
"Tri-Attention Fusion: Joint Temporal-Spectral and Bidirectional Modeling for Speech Spoofing Detection":("evaluation-deployment-and-consequence","privacy-security-and-accountability","spoofing-and-deepfake"),
"Sampling-Rate-Agnostic Speech Super-Resolution Based on Gaussian Process Dynamical Systems with Deep Kernel Learning":("listening-and-separation","echo-and-reconstruction","perceptual-enhancement"),
"Radar Acoustic Speech Enhancement Using Bilinear Decoding":("listening-and-separation","noise-enhancement","speech-prior-denoising"),
"Lightweight Phoneme-Conditioned Bandwidth Extension for Body-Conducted Speech":("listening-and-separation","echo-and-reconstruction","perceptual-enhancement"),
"Connecting Layer-Wise Representation of Wavlm with Spectro-Temporal Modulation on Speaker Verification":("people-and-variation","speaker-characteristics","speaker-verification"),
"Content-Preserving Speech Representation Learning Via Adaptive Segment-Level Alignment":("recognition-and-alignment","acoustic-unit-mapping","self-supervised-speech-units"),
}
q=json.loads((DATA/'icassp-2026-semantic-review-queue.json').read_text()); papers={p['paperId']:p for p in json.loads((DATA/'icassp-2026-papers.json').read_text())['papers']}; by_title={r['title']:r for r in q['rows']}
already=set()
for path in DATA.glob('icassp-2026-semantic-reviewed-batch-*.json'):
 if path.name!='icassp-2026-semantic-reviewed-batch-038.json': already|={r['paper_id'] for r in json.loads(path.read_text()).get('rows',[])}
missing=[t for t in assignments if t not in by_title or by_title[t]['paper_id'] in already]
if missing: raise SystemExit(f'missing or already reviewed: {missing}')
rows=[]
for title,(theme,subtheme,concept) in assignments.items():
 p=papers[by_title[title]['paper_id']]; abstract=p.get('abstract') or ''; depth='D2' if abstract else 'D1'
 rows.append({'paper_id':p['paperId'],'title':title,'decision':'supported','confidence':f'analyst-reviewed-{depth}','theme_id':theme,'subtheme_id':subtheme,'concept_id':concept,'semantic_reasoning':f'The title and preserved abstract identify a speech task and a mechanism that directly instantiates {concept} under {subtheme}.','evidence_excerpt':abstract[:1200] if abstract else title,'source_location':p.get('url'),'source_sha256':hashlib.sha256(abstract.encode()).hexdigest(),'evidence_depth':depth,'review_state':'analyst-reviewed','claim_boundary':'ICASSP discovery metadata; this is a taxonomy assignment, not an independent performance or prevalence claim.'})
payload={'schema_version':1,'batch_id':'icassp-2026-semantic-batch-038','status':'analyst-reviewed-explicit-speech-assignment-batch','claim_boundary':'These eight records are explicit speech-taxonomy assignments supported by title and, where available, abstract evidence; D2 does not imply full-paper verification.','reviewed_count':len(rows),'rows':rows}
(DATA/'icassp-2026-semantic-reviewed-batch-038.json').write_text(json.dumps(payload,indent=2,ensure_ascii=False)+'\n')
print(json.dumps({'batch_id':payload['batch_id'],'reviewed_count':len(rows),'D1':sum(r['evidence_depth']=='D1' for r in rows),'D2':sum(r['evidence_depth']=='D2' for r in rows)}))
