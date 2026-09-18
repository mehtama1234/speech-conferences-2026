#!/usr/bin/env python3
"""Materialize the evidence-backed variable taxonomy proposal.

The analyst-authored baseline supplies concept definitions.  This step changes
only the grouping boundary, using the organic proposal's explicit derivation
records; it never invents paper membership from keywords.
"""
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parent; DATA=ROOT/"data"; REPORTS=ROOT/"reports"

def main():
    base=json.loads((DATA/"speech-first-principles-taxonomy.json").read_text())
    proposal=json.loads((DATA/"speech-organic-taxonomy-proposal.json").read_text())
    baseline=json.loads((DATA/"speech-baseline-source.json").read_text())
    old_themes={t["id"]:t for t in base["themes"]}
    old_concepts={c["id"]:c for t in base["themes"] for s in t["subthemes"] for c in s["concepts"]}
    themes=[]; seen=[]
    for ptheme in proposal["records"]:
        old=old_themes[ptheme["theme_id"]]
        subs=[]
        for ps in ptheme["subthemes"]:
            concepts=[old_concepts[cid] for cid in ps["supporting_current_concepts"]]
            subs.append({
                "id":ps["id"],
                "name":ps["name"],
                "question":f"What ordinary speech pressure is handled by {ps['name'].lower()}, and what evidence distinguishes it from neighboring pressures?",
                "derivation_boundary":ps["boundary"],
                "derivation_evidence":ps["derivation"],
                "concepts":concepts,
            })
            seen.extend(c["id"] for c in concepts)
        themes.append({k:old[k] for k in ("id","name","question","ordinary_problem","naive_failure","recurring_move","tradeoff")} | {"subthemes":subs})
    if sorted(seen)!=sorted(old_concepts):
        raise SystemExit("organic taxonomy does not partition the baseline concepts exactly")
    out={"schema_version":2,"taxonomy_status":"analyst-authored-organically-derived-proposal","claim_boundary":"Themes and variable subthemes are derived from the named baseline paper and explicit paper-family boundary tests; this is not an official conference classification or prevalence estimate.","baseline_source":baseline,"source_boundary":"Concept definitions begin from the baseline account. Subtheme boundaries are proposed from recurring ordinary pressures, failures, mechanisms, and evidence counts; paper membership is adjudicated separately.","membership_evidence_rule":base["membership_evidence_rule"],"derivation_source":"data/speech-organic-taxonomy-proposal.json","theme_count":len(themes),"subtheme_count":sum(len(t["subthemes"]) for t in themes),"concept_count":len(seen),"themes":themes}
    (DATA/"speech-first-principles-taxonomy.json").write_text(json.dumps(out,indent=2,ensure_ascii=False)+"\n")
    lines=["# Speech first-principles conceptual taxonomy","",out["claim_boundary"],"",f"**Baseline:** {baseline['citation']} — {baseline['source_url']}","",f"This organically derived proposal has {out['theme_count']} themes, {out['subtheme_count']} variable subthemes, and {out['concept_count']} concepts. Counts are not equalized.",""]
    for t in themes:
        lines += [f"## {t['name']}","",f"**Ordinary problem:** {t['ordinary_problem']}","",f"**Why the naive approach fails:** {t['naive_failure']}","",f"**Recurring conceptual move:** {t['recurring_move']}", "", f"**Tradeoff/boundary:** {t['tradeoff']}", ""]
        for s in t["subthemes"]:
            lines += [f"### {s['name']}","",f"**Question:** {s['question']}",f"**Why this boundary exists:** {s['derivation_boundary']}",f"**Derivation rule:** {s['derivation_evidence']}",""]
            for c in s["concepts"]:
                lines += [f"#### {c['name']}","",c["definition"],"",f"**Positive membership example:** {c.get('positive_example','')}","",f"**Negative/boundary example:** {c.get('negative_example','')}","",f"**Boundary:** {c['boundary']}","",f"**Evidence rule:** {c.get('membership_evidence_rule','')}",""]
    (REPORTS/"SPEECH_FIRST_PRINCIPLES_TAXONOMY.md").write_text("\n".join(lines).rstrip()+"\n")
    print(json.dumps({"themes":out["theme_count"],"subthemes":out["subtheme_count"],"concepts":out["concept_count"]}))
if __name__=="__main__": main()
