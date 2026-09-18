#!/usr/bin/env python3
"""Build bounded synthesis records for every first-principles subtheme."""

from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = HERE / "data"
REPORTS = HERE / "reports"


def main() -> None:
    taxonomy = json.loads((DATA / "speech-first-principles-taxonomy.json").read_text())
    queue = json.loads((DATA / "interspeech-2025-semantic-review-queue.json").read_text())
    deep_by_id = {json.loads(line)["paper_id"]: json.loads(line) for line in (DATA / "interspeech-2025-deep-paper-analyses.jsonl").read_text().splitlines() if line.strip()}
    notes = {}
    for filename in ("interspeech-2025-d3-notes.json", "interspeech-2025-second-d3-notes.json", "interspeech-2025-third-d3-notes.json", "interspeech-2025-fourth-d3-notes.json", "interspeech-2025-fifth-d3-notes.json", "interspeech-2025-sixth-d3-notes.json", "interspeech-2025-seventh-d3-notes.json", "interspeech-2025-eighth-d3-notes.json", "interspeech-2025-ninth-d3-notes.json", "interspeech-2025-tenth-d3-notes.json", "interspeech-2025-eleventh-d3-notes.json", "interspeech-2025-twelfth-d3-notes.json", "interspeech-2025-thirteenth-d3-notes.json", "interspeech-2025-fourteenth-d3-notes.json", "interspeech-2025-fifteenth-d3-notes.json", "interspeech-2025-sixteenth-d3-notes.json", "interspeech-2025-seventeenth-d3-notes.json", "interspeech-2025-eighteenth-d3-notes.json", "interspeech-2025-nineteenth-d3-notes.json", "interspeech-2025-twentieth-d3-notes.json", "interspeech-2025-twentyfirst-d3-notes.json", "interspeech-2025-twentisecond-d3-notes.json", "interspeech-2025-twentythird-d3-notes.json", "interspeech-2025-twentyfourth-d3-notes.json", "interspeech-2025-twentyfifth-d3-notes.json", "interspeech-2025-twentysixth-d3-notes.json", "interspeech-2025-twentyseventh-d3-notes.json", "interspeech-2025-twentyeighth-d3-notes.json", "interspeech-2025-twentyninth-d3-notes.json", "interspeech-2025-thirtieth-d3-notes.json", "interspeech-2025-thirtyfirst-d3-notes.json", "interspeech-2025-thirtysecond-d3-notes.json", "interspeech-2025-thirtythird-d3-notes.json", "interspeech-2025-thirtyfourth-d3-notes.json", "interspeech-2025-thirtyfifth-d3-notes.json", "interspeech-2025-thirtysixth-d3-notes.json", "interspeech-2025-thirtyseventh-d3-notes.json", "interspeech-2025-thirtyeighth-d3-notes.json", "interspeech-2025-thirtyninth-d3-notes.json", "interspeech-2025-fortieth-d3-notes.json", "interspeech-2025-fortyfirst-d3-notes.json", "interspeech-2025-fortysecond-d3-notes.json", "interspeech-2025-fortythird-d3-notes.json", "interspeech-2025-fortyfourth-d3-notes.json", "interspeech-2025-fortyfifth-d3-notes.json", "interspeech-2025-fortysixth-d3-notes.json", "interspeech-2025-fortyseventh-d3-notes.json", "interspeech-2025-fortyeighth-d3-notes.json", "interspeech-2025-fortyninth-d3-notes.json", "interspeech-2025-fiftieth-d3-notes.json", "interspeech-2025-fiftyfirst-d3-notes.json", "interspeech-2025-fiftysecond-d3-notes.json", "interspeech-2025-fiftythird-d3-notes.json", "interspeech-2025-fiftyfourth-d3-notes.json", "interspeech-2025-fiftyfifth-d3-notes.json", "interspeech-2025-fiftysixth-d3-notes.json", "interspeech-2025-fiftyseventh-d3-notes.json"):
        for row in json.loads((DATA / filename).read_text())["notes"]:
            notes[row["paper_id"]] = row
    for row in json.loads((DATA / "interspeech-2025-fortysecond-d3-notes.json").read_text())["notes"]:
        notes[row["paper_id"]] = row
    for row in json.loads((DATA / "interspeech-2025-fortythird-d3-notes.json").read_text())["notes"]:
        notes[row["paper_id"]] = row
    for row in json.loads((DATA / "interspeech-2025-fortyfourth-d3-notes.json").read_text())["notes"]:
        notes[row["paper_id"]] = row
    for row in json.loads((DATA / "interspeech-2025-fortyfifth-d3-notes.json").read_text())["notes"]:
        notes[row["paper_id"]] = row
    for row in json.loads((DATA / "interspeech-2025-fortysixth-d3-notes.json").read_text())["notes"]:
        notes[row["paper_id"]] = row
    for row in json.loads((DATA / "interspeech-2025-fiftyeighth-d3-notes.json").read_text())["notes"]:
        notes[row["paper_id"]] = row
    for row in json.loads((DATA / "interspeech-2025-fiftyninth-d3-notes.json").read_text())["notes"]:
        notes[row["paper_id"]] = row
    for row in json.loads((DATA / "interspeech-2025-sixtieth-d3-notes.json").read_text())["notes"]:
        notes[row["paper_id"]] = row
    for row in json.loads((DATA / "interspeech-2025-sixtyfirst-d3-notes.json").read_text())["notes"]:
        notes[row["paper_id"]] = row
    for row in json.loads((DATA / "interspeech-2025-sixtysecond-d3-notes.json").read_text())["notes"]:
        notes[row["paper_id"]] = row
    for row in json.loads((DATA / "interspeech-2025-sixtythird-d3-notes.json").read_text())["notes"]:
        notes[row["paper_id"]] = row
    by_subtheme = defaultdict(list)
    for row in queue["rows"]:
        if row.get("review_state") != "analyst-reviewed":
            continue
        if deep_by_id.get(row["paper_id"], {}).get("depth") == "D3":
            row = dict(row)
            row["evidence_depth"] = "D3"
        review = row["analyst_review"]
        by_subtheme[review["subtheme_id"]].append({"queue": row, "review": review})
    records = []
    report = [
        "# Speech subtheme and paper-family syntheses",
        "",
        f"This report covers all 24 taxonomy subthemes and uses the {queue.get('reviewed_count', 0)} analyst-reviewed INTERSPEECH assignments. D2 and D3 evidence are kept separate; an empty subtheme is an unresolved evidence gap, not a claim that no papers exist.",
        "",
    ]
    for theme in taxonomy["themes"]:
        report += [f"## Theme: {theme['name']}", ""]
        for subtheme in theme["subthemes"]:
            papers = by_subtheme.get(subtheme["id"], [])
            d3_count = sum(item["queue"].get("evidence_depth") == "D3" for item in papers)
            d2_count = sum(item["queue"].get("evidence_depth") == "D2" for item in papers)
            record = {
                "theme_id": theme["id"],
                "subtheme_id": subtheme["id"],
                "subtheme_name": subtheme["name"],
                "question": subtheme["question"],
                "concept_ids": [c["id"] for c in subtheme["concepts"]],
                "reviewed_paper_count": len(papers),
                "d3_paper_count": d3_count,
                "d2_paper_count": d2_count,
                "status": "seed-family-evidence" if papers else "unestablished",
                "paper_ids": [item["queue"]["paper_id"] for item in papers],
            }
            d3_items = [item for item in papers if item["queue"].get("evidence_depth") == "D3" and item["queue"]["paper_id"] in notes]
            d3_titles = [item["queue"]["title"] for item in d3_items]
            d3_moves = [notes[item["queue"]["paper_id"]].get("ap", "") for item in d3_items]
            d3_limits = [notes[item["queue"]["paper_id"]].get("limits", "") for item in d3_items]
            concept_names = ", ".join(c["name"].lower() for c in subtheme["concepts"])
            subtheme_naive = (
                f"A first attempt would answer the question only with {subtheme['concepts'][0]['name'].lower()}, "
                f"but that shortcut misses the boundary: {subtheme['concepts'][0]['boundary']}"
            )
            if d3_moves:
                subtheme_move = (
                    f"Across this subtheme, papers make {concept_names} explicit rather than treating the speech evidence as one undifferentiated variable. "
                    f"The reviewed full-paper mechanisms instantiate that move in different ways; for example: {d3_moves[0]}"
                )
            else:
                subtheme_move = (
                    f"The subtheme requires separating {concept_names} so that the measured or generated object matches the question: {subtheme['question']}"
                )
            # Keep a structured comparison alongside the prose. This forces
            # the family layer to identify what each paper changes, what it
            # measures, and where its evidence stops.
            d3_comparison = []
            for item in d3_items:
                note = notes[item["queue"]["paper_id"]]
                deep = deep_by_id.get(item["queue"]["paper_id"], {})
                d3_comparison.append({
                    "paper_id": item["queue"]["paper_id"],
                    "title": item["queue"]["title"],
                    "concept_id": item["review"].get("concept_id"),
                    "central_move": note.get("ap", ""),
                    "mechanism": note.get("mech", ""),
                    "evaluation_object": deep.get("eval", note.get("eval", note.get("math", ""))),
                    "reported_result": note.get("ww", ""),
                    "reported_payoff": deep.get("po", note.get("po", "")),
                    "evidence_limit": note.get("limits", ""),
                })
            # A useful family synthesis must expose a contrast, not merely
            # concatenate paper summaries. Keep the contrast explicitly
            # bounded to the first two captured full-paper notes.
            contrast_items = d3_items[:2]
            if len(contrast_items) >= 2:
                left, right = contrast_items
                left_note = notes[left["queue"]["paper_id"]]
                right_note = notes[right["queue"]["paper_id"]]
                mechanism_contrast = (
                    f"{left['queue']['title']} addresses the pressure by {left_note.get('mech', left_note.get('ap', 'using its reported method'))}; "
                    f"{right['queue']['title']} addresses it by {right_note.get('mech', right_note.get('ap', 'using its reported method'))}. "
                    "The shared problem is therefore compatible with more than one intervention point."
                )
                evidence_contrast = (
                    f"The first paper reports {left_note.get('ww', 'an evaluation result')}; the second reports {right_note.get('ww', 'an evaluation result')}. "
                    "These outcomes should not be ranked unless their data, listeners, metric, and test condition are comparable."
                )
                failure_contrast = (
                    f"The first paper leaves open: {left_note.get('limits', 'its stated boundary')}; "
                    f"the second leaves open: {right_note.get('limits', 'its stated boundary')}. "
                    "Those are evidence boundaries, not proof that either method fails outside the paper."
                )
                named_contrast = f"{left['queue']['title']} versus {right['queue']['title']}"
            elif contrast_items:
                only = contrast_items[0]
                note = notes[only["queue"]["paper_id"]]
                named_contrast = only["queue"]["title"]
                mechanism_contrast = f"Only one captured D3 note is available: {note.get('mech', note.get('ap', 'the reported method'))}. A mechanism contrast is not yet established."
                evidence_contrast = f"The paper reports: {note.get('ww', 'an evaluation result')}. No second full-paper case is available for a controlled comparison."
                failure_contrast = f"The paper states: {note.get('limits', 'an explicit limitation')}. This is a paper boundary, not a venue-wide conclusion."
            else:
                named_contrast = "No captured D3 contrast"
                mechanism_contrast = "No captured D3 mechanism contrast is available."
                evidence_contrast = "No captured D3 evaluation contrast is available."
                failure_contrast = "No captured D3 failure-boundary contrast is available."
            # This is deliberately a synthesis assembled from explicit fields,
            # not a prevalence claim. It tells the reader what the reviewed
            # papers have in common and where they diverge.
            if papers:
                reviewed_examples = "; ".join(
                    f"{item['queue']['title']}: {item['review'].get('semantic_reasoning', '')}"
                    for item in papers[:4]
                )
                family_synthesis = {
                    "ordinary_pressure": f"{theme['ordinary_problem']} The subtheme asks: {subtheme['question']}",
                    "naive_shortcut": subtheme_naive,
                    "recurring_move": subtheme_move,
                    "subtheme_boundary": [c["boundary"] for c in subtheme["concepts"]],
                    "tradeoff": "The recurring move must preserve the evidence relevant to the named concept without importing a neighboring concept's assumptions; the boundaries below state where that interpretation stops.",
                    "reviewed_variation": reviewed_examples,
                    "d3_mechanism_evidence": d3_moves[:4],
                    "d3_comparison_matrix": d3_comparison,
                    "comparison_conclusion": "The papers share the ordinary pressure but intervene at different points in the chain; their reported outcomes are not directly rankable unless the measured object and test condition match.",
                    "named_contrast": named_contrast,
                    "mechanism_contrast": mechanism_contrast,
                    "evidence_contrast": evidence_contrast,
                    "failure_boundary_contrast": failure_contrast,
                    "transfer_question": f"What would have to remain invariant for this family to work across a new speaker, language, room, device, or task, and which paper evidence here actually tests that transfer?",
                    "evidence_boundary": "The shared story is supported only by the reviewed papers listed here; D2 entries support the problem and stated method, while D3 entries support the reported mechanism and evaluation. It is not a venue-wide prevalence claim.",
                    "unresolved_question": f"What changes when this move is tested outside the speakers, languages, rooms, devices, or benchmark conditions represented by the {d3_count} D3 paper(s)?",
                }
            else:
                family_synthesis = {
                    "ordinary_pressure": f"{theme['ordinary_problem']} The subtheme asks: {subtheme['question']}",
                    "naive_shortcut": subtheme_naive,
                    "recurring_move": subtheme_move,
                    "subtheme_boundary": [c["boundary"] for c in subtheme["concepts"]],
                    "tradeoff": "No reviewed paper establishes how to trade this subtheme's competing pressures; the concept boundaries remain the governing limits.",
                    "reviewed_variation": "",
                    "d3_mechanism_evidence": [],
                    "d3_comparison_matrix": [],
                    "comparison_conclusion": "No captured D3 paper is available for a mechanism comparison.",
                    "named_contrast": "No reviewed paper",
                    "mechanism_contrast": "No mechanism contrast is available.",
                    "evidence_contrast": "No evaluation contrast is available.",
                    "failure_boundary_contrast": "No failure-boundary contrast is available.",
                    "transfer_question": "Which captured papers should be adjudicated here before a family contrast can be made?",
                    "evidence_boundary": "No analyst-reviewed paper currently supports a family story here.",
                    "unresolved_question": "Which captured papers should be semantically adjudicated into this subtheme, and what would distinguish them from neighboring subthemes?",
                }
            concept_families = []
            for concept in subtheme["concepts"]:
                concept_papers = [item for item in papers if item["review"].get("concept_id") == concept["id"]]
                concept_d3 = [item for item in concept_papers if item["queue"].get("evidence_depth") == "D3"]
                concept_examples = [
                    f"{item['queue']['title']}: {item['review'].get('semantic_reasoning', '')}"
                    for item in concept_papers[:3]
                ]
                if concept_examples:
                    family_claim = (
                        f"The ordinary pressure is {concept['definition']} In the reviewed evidence, "
                        f"the family appears as {'; '.join(concept_examples)} "
                        f"It must not be confused with neighboring problems outside this boundary: {concept['boundary']}"
                    )
                else:
                    family_claim = (
                        f"The ordinary pressure is {concept['definition']} No analyst-reviewed paper currently "
                        f"demonstrates the family, and its boundary is {concept['boundary']}"
                    )
                concept_families.append({
                    "concept_id": concept["id"],
                    "concept_name": concept["name"],
                    "definition": concept["definition"],
                    "boundary": concept["boundary"],
                    "reviewed_paper_count": len(concept_papers),
                    "d3_paper_count": len(concept_d3),
                    "paper_ids": [item["queue"]["paper_id"] for item in concept_papers],
                    "d3_paper_ids": [item["queue"]["paper_id"] for item in concept_d3],
                    "family_claim": family_claim,
                    "unresolved": f"Whether this concept remains useful outside the reviewed speakers, languages, devices, rooms, and tasks is unresolved; {len(concept_d3)} D3 paper(s) provide full-paper evidence.",
                })
            record["family_synthesis"] = family_synthesis
            record["concept_families"] = concept_families
            records.append(record)
            report += [f"### {subtheme['name']}", "", f"**Question:** {subtheme['question']}", "", f"**Concepts:** {', '.join(c['name'] for c in subtheme['concepts'])}", ""]
            if not papers:
                report += ["**Evidence status:** No analyst-reviewed paper is assigned here yet. Do not infer prevalence or absence from this gap.", ""]
                continue
            synthesis = record["family_synthesis"]
            report += [f"**Evidence status:** {len(papers)} analyst-reviewed paper(s): {d3_count} D3 and {d2_count} D2.", "", "**Family synthesis for the reviewed evidence:**", "", f"- **Ordinary pressure:** {synthesis['ordinary_pressure']}", f"- **Naive shortcut:** {synthesis['naive_shortcut']}", f"- **Recurring move:** {synthesis['recurring_move']}", f"- **Subtheme tradeoff:** {synthesis['tradeoff']}", f"- **Concept boundaries:** {' '.join(synthesis['subtheme_boundary'])}", f"- **Variation in reviewed papers:** {synthesis['reviewed_variation']}", f"- **D3 mechanism evidence:** {' '.join(synthesis['d3_mechanism_evidence']) or 'No D3 mechanism note is available.'}", f"- **Named contrast:** {synthesis['named_contrast']}", f"- **Mechanism contrast:** {synthesis['mechanism_contrast']}", f"- **Evidence contrast:** {synthesis['evidence_contrast']}", f"- **Failure-boundary contrast:** {synthesis['failure_boundary_contrast']}", f"- **Comparison conclusion:** {synthesis['comparison_conclusion']}", f"- **Transfer question:** {synthesis['transfer_question']}", f"- **Boundary:** {synthesis['evidence_boundary']}", f"- **Unresolved:** {synthesis['unresolved_question']}", "", "**D3 paper-family comparison:**", ""]
            for comparison in synthesis["d3_comparison_matrix"]:
                report += [f"- **{comparison['title']}** (`{comparison['concept_id']}`): move — {comparison['central_move']} mechanism — {comparison['mechanism']} evaluation object — {comparison['evaluation_object']} reported result — {comparison['reported_result']} limit — {comparison['evidence_limit']}", ""]
            report += ["**Concept families:**", ""]
            for concept_family in record["concept_families"]:
                report += [f"- **{concept_family['concept_name']}** — {concept_family['family_claim']}", f"  Reviewed examples: {concept_family['reviewed_paper_count']}; D3: {concept_family['d3_paper_count']}; unresolved: {concept_family['unresolved']}", ""]
            for item in papers:
                paper = item["queue"]
                review = item["review"]
                report += [f"#### {paper['title']} ({paper['evidence_depth']})", "", f"**Assignment:** {review['semantic_reasoning']}", ""]
                if paper["evidence_depth"] == "D3":
                    note = notes[paper["paper_id"]]
                    report += [f"**Mechanism:** {note['mech']}", "", f"**Evaluation/result:** {note['ww']}", "", f"**Limit:** {note['limits']}", ""]
                else:
                    report += [f"**Abstract evidence:** {review['evidence_excerpt']}", "", f"**Boundary:** {review.get('claim_boundary', 'Full-paper mechanism and limitations are not established at D2 depth.')}", ""]
    payload = {
        "schema_version": 1,
        "status": "bounded-subtheme-seed-synthesis",
        "claim_boundary": "Every taxonomy subtheme has a synthesis record. Family evidence currently comes from the analyst-reviewed D2/D3 seed and does not represent the full corpus.",
        "subtheme_count": len(records),
        "subthemes_with_reviewed_evidence": sum(x["reviewed_paper_count"] > 0 for x in records),
        "subthemes_with_d3": sum(x["d3_paper_count"] > 0 for x in records),
        "reviewed_inter_speech_count": queue.get("reviewed_count", 0),
        "records": records,
    }
    (DATA / "speech-subtheme-syntheses.json").write_text(json.dumps(payload, indent=2) + "\n")
    (REPORTS / "SPEECH_SUBTHEME_SYNTHESES.md").write_text("\n".join(report) + "\n")
    print(json.dumps({"subthemes": len(records), "subthemes_with_reviewed_evidence": payload["subthemes_with_reviewed_evidence"], "subthemes_with_d3": payload["subthemes_with_d3"], "reviewed_count": payload["reviewed_inter_speech_count"]}))


if __name__ == "__main__":
    main()
