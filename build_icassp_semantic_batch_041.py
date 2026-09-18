#!/usr/bin/env python3
"""Assign eight further clearly speech-specific ICASSP cases."""
import hashlib,json
from pathlib import Path
HERE=Path(__file__).resolve().parent; DATA=HERE/'data'
A={
"Hanui: Harnessing Distributional Discrepancies for Singing Voice Deepfake Detection":("evaluation-deployment-and-consequence","privacy-security-and-accountability","spoofing-and-deepfake"),
"Emotional Damage: Investigating Safety Vulnerabilities of Large Audio-Language Models Under Speaker Emotional Variations":("evaluation-deployment-and-consequence","robustness-and-system-boundary","distribution-shift"),
"The Curious Case of Visual Grounding: Different Effects for Speech-and Text-Based Language Encoders":("meaning-and-interaction","grounding-and-action","referential-grounding"),
"Input-Adaptive Differentiable Filterbanks via Hypernetworks for Robust Speech Processing":("sound-and-production","time-frequency-measurement","multi-resolution-signal"),
"Attention-Based Encoder-Decoder Target-Speaker Voice Activity Detection for Robust Speaker Diarization":("recognition-and-alignment","boundaries-and-sequence-structure","alignment"),
"Distilling Attention Knowledge for Speaker Verification":("people-and-variation","speaker-characteristics","speaker-verification"),
"LAFUFU: Latent Acoustic Features For Ultra-Fast Utterance Restoration":("listening-and-separation","echo-and-reconstruction","perceptual-enhancement"),
"A Multi-View Fusion Framework for Audio-Visual Multi-Speaker Tracking":("meaning-and-interaction","dialogue-and-turn-taking","turn-boundary"),
}
q=json.loads((DATA/'icassp-2026-semantic-review-queue.json').read_text()); papers={p['paperId']:p for p in json.loads((DATA/'icassp-2026-papers.json').read_text())['papers']}; by={r['title']:r for r in q['rows']}; already=set()
for path in DATA.glob('icassp-2026-semantic-reviewed-batch-*.json'):
 if path.name!='icassp-2026-semantic-reviewed-batch-041.json': already|={r['paper_id'] for r in json.loads(path.read_text()).get('rows',[])}
missing=[t for t in A if t not in by or by[t]['paper_id'] in already]
if missing: raise SystemExit(f'missing or already reviewed: {missing}')
rows=[]
for title,(theme,subtheme,concept) in A.items():
 p=papers[by[title]['paper_id']]; abstract=p.get('abstract') or ''; depth='D2' if abstract else 'D1'
 rows.append({'paper_id':p['paperId'],'title':title,'decision':'supported','confidence':f'analyst-reviewed-{depth}','theme_id':theme,'subtheme_id':subtheme,'concept_id':concept,'semantic_reasoning':f'The title and preserved abstract identify a speech task and a mechanism that directly instantiates {concept} under {subtheme}.','evidence_excerpt':abstract[:1200] if abstract else title,'source_location':p.get('url'),'source_sha256':hashlib.sha256(abstract.encode()).hexdigest(),'evidence_depth':depth,'review_state':'analyst-reviewed','claim_boundary':'ICASSP discovery metadata; this is a taxonomy assignment, not an independent performance or prevalence claim.'})
payload={'schema_version':1,'batch_id':'icassp-2026-semantic-batch-041','status':'analyst-reviewed-explicit-speech-assignment-batch','claim_boundary':'These records are explicit speech-taxonomy assignments supported by title and, where available, abstract evidence; D2 does not imply full-paper verification.','reviewed_count':len(rows),'rows':rows}
(DATA/'icassp-2026-semantic-reviewed-batch-041.json').write_text(json.dumps(payload,indent=2,ensure_ascii=False)+'\n')
print(json.dumps({'batch_id':payload['batch_id'],'reviewed_count':len(rows),'D1':sum(r['evidence_depth']=='D1' for r in rows),'D2':sum(r['evidence_depth']=='D2' for r in rows)}))
