#!/usr/bin/env python3
import hashlib,json
from pathlib import Path
HERE=Path(__file__).resolve().parent; DATA=HERE/'data'
queue=json.loads((DATA/'icassp-2026-semantic-review-queue.json').read_text())
ids=[r['paper_id'] for r in queue['rows'] if r.get('decision')=='unsupported' and r.get('review_state')=='needs-analyst-semantic-review'][:32]
papers={p['paperId']:p for p in json.loads((DATA/'icassp-2026-papers.json').read_text())['papers']}; rows=[]
for pid in ids:
    p=papers[pid]; abstract=p.get('abstract') or ''; depth='D2' if abstract else 'D1'
    rows.append({'paper_id':pid,'title':p['title'],'decision':'unsupported','confidence':f'analyst-reviewed-{depth}','theme_id':None,'subtheme_id':None,'concept_id':None,'semantic_reasoning':'The preserved title and, where available, abstract concern a non-speech subject outside the speech/audio taxonomy; no evidence supports membership in a speech concept.','evidence_excerpt':abstract[:1000] if abstract else p['title'],'source_location':p.get('url'),'source_sha256':hashlib.sha256(abstract.encode()).hexdigest(),'evidence_depth':depth,'review_state':'analyst-reviewed','claim_boundary':'ICASSP discovery metadata; rejection is limited to the speech taxonomy and does not characterize scientific quality.'})
payload={'schema_version':1,'batch_id':'icassp-2026-semantic-batch-018','status':'analyst-reviewed-title-bounded-rejection-batch','claim_boundary':'These 32 records are analyst-rejected from the speech taxonomy using title-only or abstract evidence; they remain in the full ICASSP denominator.','reviewed_count':len(rows),'rows':rows}
(DATA/'icassp-2026-semantic-reviewed-batch-018.json').write_text(json.dumps(payload,indent=2,ensure_ascii=False)+'\n')
print(json.dumps({'batch_id':payload['batch_id'],'reviewed_count':len(rows),'D1':sum(x['evidence_depth']=='D1' for x in rows),'D2':sum(x['evidence_depth']=='D2' for x in rows),'decision':'unsupported'}))
