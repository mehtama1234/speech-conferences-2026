#!/usr/bin/env python3
"""Build a concept-level cross-venue family atlas with explicit boundaries."""
from __future__ import annotations
import json
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = HERE / "data"
REPORTS = HERE / "reports"


def reviewed_by_concept(queue: dict) -> dict[str, list[dict]]:
    out = defaultdict(list)
    for row in queue.get("rows", []):
        if row.get("review_state") != "analyst-reviewed":
            continue
        review = row.get("analyst_review") or {}
        concept = review.get("concept_id")
        if concept:
            out[concept].append({
                "paper_id": row.get("paper_id"),
                "title": row.get("title"),
                "evidence_depth": row.get("evidence_depth"),
                "semantic_reasoning": review.get("semantic_reasoning"),
                "evidence_excerpt": review.get("evidence_excerpt"),
            })
    return out


def candidate_by_subtheme(queue: dict) -> dict[str, int]:
    out = defaultdict(int)
    for row in queue.get("rows", []):
        if row.get("review_state") == "analyst-reviewed":
            continue
        seen = set()
        for candidate in row.get("candidate_assignments", []):
            key = candidate.get("subtheme_id")
            if key and key not in seen:
                out[key] += 1
                seen.add(key)
    return out


def main() -> None:
    taxonomy = json.loads((DATA / "speech-first-principles-taxonomy.json").read_text())
    inter = json.loads((DATA / "interspeech-2025-semantic-review-queue.json").read_text())
    icassp = json.loads((DATA / "icassp-2026-semantic-review-queue.json").read_text())
    inter_concepts = reviewed_by_concept(inter)
    icassp_concepts = reviewed_by_concept(icassp)
    inter_candidates = candidate_by_subtheme(inter)
    icassp_candidates = candidate_by_subtheme(icassp)
    records = []
    report = [
        "# Speech concept families across INTERSPEECH and ICASSP",
        "",
        "This is a concept-level family atlas, not a prevalence ranking. A reviewed paper supports the concept only at its recorded D2 or D3 depth. Candidate counts show discovery coverage and are not final membership.",
        "",
        f"Reviewed evidence: {inter.get('reviewed_count', 0)} INTERSPEECH records and {icassp.get('reviewed_count', 0)} ICASSP records.",
        "",
    ]
    for theme in taxonomy["themes"]:
        report += [f"## {theme['name']}", "", f"**Ordinary pressure:** {theme['ordinary_problem']}", ""]
        for subtheme in theme["subthemes"]:
            report += [f"### {subtheme['name']}", "", f"**Question:** {subtheme['question']}", ""]
            for concept in subtheme["concepts"]:
                iid = concept["id"]
                ir = inter_concepts.get(iid, [])
                cr = icassp_concepts.get(iid, [])
                subtheme_id = subtheme["id"]
                ic = inter_candidates.get(subtheme_id, 0)
                cc = icassp_candidates.get(subtheme_id, 0)
                depth_i = {"D2": sum(x["evidence_depth"] == "D2" for x in ir), "D3": sum(x["evidence_depth"] == "D3" for x in ir)}
                depth_c = {"D1": sum(x["evidence_depth"] == "D1" for x in cr), "D2": sum(x["evidence_depth"] == "D2" for x in cr), "D3": sum(x["evidence_depth"] == "D3" for x in cr)}
                record = {
                    "theme_id": theme["id"],
                    "subtheme_id": subtheme_id,
                    "concept_id": iid,
                    "concept_name": concept["name"],
                    "definition": concept["definition"],
                    "boundary": concept["boundary"],
                    "ordinary_pressure": theme["ordinary_problem"],
                    "interspeech_reviewed_count": len(ir),
                    "interspeech_reviewed_by_depth": depth_i,
                    "interspeech_paper_ids": [x["paper_id"] for x in ir],
                    "icassp_reviewed_count": len(cr),
                    "icassp_reviewed_by_depth": depth_c,
                    "icassp_paper_ids": [x["paper_id"] for x in cr],
                    "interspeech_candidate_subtheme_count": ic,
                    "icassp_candidate_subtheme_count": cc,
                    "family_claim": (
                        f"The ordinary pressure is {concept['definition']} "
                        f"The reviewed examples are counted below by venue and depth; they show how this pressure is made operational, "
                        f"while the boundary remains: {concept['boundary']}"
                    ),
                    "cross_venue_reading": f"INTERSPEECH has {len(ir)} reviewed example(s) and ICASSP has {len(cr)} reviewed example(s). The difference cannot be read as research prevalence because the reviewed sets are selected, ICASSP includes {sum(x.get('evidence_depth') == 'D1' for x in cr)} title-only records among these examples, and the remaining candidate coverage is unresolved.",
                    "unresolved_question": f"Which of the {ic + cc} open candidate records actually belongs to this concept after reading the problem and mechanism, and where does the concept boundary fail against neighboring subthemes?",
                    "evidence_boundary": "D2 supports the abstract-stated problem and proposed move; D3 supports the captured paper's mechanism and reported evaluation. No independent reproduction or venue-wide estimate is implied.",
                }
                records.append(record)
                report += [
                    f"#### {concept['name']}",
                    "",
                    f"**Definition:** {concept['definition']}",
                    "",
                    f"**Boundary:** {concept['boundary']}",
                    "",
                    f"**INTERSPEECH reviewed:** {len(ir)} ({depth_i['D3']} D3, {depth_i['D2']} D2); **ICASSP reviewed:** {len(cr)} ({depth_c['D2']} D2, {depth_c['D1']} D1).",
                    "",
                    f"**Candidate coverage, not final assignment:** {ic} INTERSPEECH and {cc} ICASSP records mention the surrounding subtheme in the discovery queue.",
                    "",
                    f"**Family reading:** {record['family_claim']}",
                    "",
                    f"**Cross-venue reading:** {record['cross_venue_reading']}",
                    "",
                    f"**Unresolved:** {record['unresolved_question']}",
                    "",
                    f"**Paper IDs:** INTERSPEECH {', '.join(record['interspeech_paper_ids']) or 'none yet'}; ICASSP {', '.join(record['icassp_paper_ids']) or 'none yet'}.",
                    "",
                ]
    payload = {
        "schema_version": 1,
        "status": "bounded-concept-family-cross-venue-atlas",
        "claim_boundary": "All 72 concepts have a definition, boundary, cross-venue reviewed-paper accounting, discovery coverage, and unresolved question. Reviewed membership is not a prevalence estimate; candidate coverage is not final semantic membership.",
        "concept_count": len(records),
        "concepts_with_interspeech_reviewed": sum(x["interspeech_reviewed_count"] > 0 for x in records),
        "concepts_with_icassp_reviewed": sum(x["icassp_reviewed_count"] > 0 for x in records),
        "records": records,
    }
    (DATA / "speech-concept-family-crosswalk.json").write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
    (REPORTS / "SPEECH_CONCEPT_FAMILY_CROSSWALK.md").write_text("\n".join(report) + "\n")
    print(json.dumps({
        "concepts": len(records),
        "with_interspeech_reviewed": payload["concepts_with_interspeech_reviewed"],
        "with_icassp_reviewed": payload["concepts_with_icassp_reviewed"],
    }))


if __name__ == "__main__":
    main()
