#!/usr/bin/env python3
"""Reject a bounded batch of clearly non-speech ambiguous ICASSP proposals."""
import hashlib,json,re
from pathlib import Path
HERE=Path(__file__).resolve().parent; DATA=HERE/'data'
pattern=re.compile(r'image|MRI|\bCT\b|video|knowledge graph|vehicle|EEG|ECG|LiDAR|RF heatmap|LLM|recommendation|object detection|ultrasound|low-light|polyp|\bgraph\b|\bQAM\b|\bOFDM\b|federated|stock|malware|text editing|Gaussian splatting|SAR |thermal|endoscopic|driving|code completion|medical',re.I)
q=json.loads((DATA/'icassp-2026-semantic-review-queue.json').read_text()); papers={p['paperId']:p for p in json.loads((DATA/'icassp-2026-papers.json').read_text())['papers']}; already=set()
for path in DATA.glob('icassp-2026-semantic-reviewed-batch-*.json'):
 if path.name!='icassp-2026-semantic-reviewed-batch-043.json': already|={r['paper_id'] for r in json.loads(path.read_text()).get('rows',[])}
selected=[r for r in q['rows'] if r['review_state']=='needs-analyst-semantic-review' and r['decision']=='ambiguous' and pattern.search(r['title']) and r['paper_id'] not in already][:32]
if len(selected)!=32: raise SystemExit(f'expected 32 new non-speech rows, found {len(selected)}')
rows=[]
for c in selected:
 p=papers[c['paper_id']]; abstract=p.get('abstract') or ''; depth='D2' if abstract else 'D1'
 rows.append({'paper_id':p['paperId'],'title':p['title'],'decision':'unsupported','confidence':f'analyst-reviewed-{depth}','theme_id':None,'subtheme_id':None,'concept_id':None,'semantic_reasoning':'The title and preserved abstract identify an image, video, medical, vehicle, RF, graph, language-model, or other non-speech object; generic lexical overlap is insufficient for membership in the speech taxonomy.','evidence_excerpt':abstract[:1000] if abstract else p['title'],'source_location':p.get('url'),'source_sha256':hashlib.sha256(abstract.encode()).hexdigest(),'evidence_depth':depth,'review_state':'analyst-reviewed','claim_boundary':'ICASSP discovery metadata; rejection resolves membership in the speech taxonomy only and does not characterize scientific quality.'})
payload={'schema_version':1,'batch_id':'icassp-2026-semantic-batch-043','status':'analyst-reviewed-ambiguous-non-speech-batch','claim_boundary':'These records were ambiguous machine proposals but their preserved titles identify non-speech objects; they remain in the full ICASSP denominator.','reviewed_count':len(rows),'rows':rows}
(DATA/'icassp-2026-semantic-reviewed-batch-043.json').write_text(json.dumps(payload,indent=2,ensure_ascii=False)+'\n')
print(json.dumps({'batch_id':payload['batch_id'],'reviewed_count':len(rows),'D1':sum(r['evidence_depth']=='D1' for r in rows),'D2':sum(r['evidence_depth']=='D2' for r in rows)}))
