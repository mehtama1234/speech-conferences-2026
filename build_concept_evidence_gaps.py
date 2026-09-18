#!/usr/bin/env python3
"""Report taxonomy concepts with no analyst-reviewed ICASSP evidence."""

import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = HERE / "data"
REPORTS = HERE / "reports"


def main() -> None:
    taxonomy = json.loads((DATA / "speech-first-principles-taxonomy.json").read_text())
    crosswalk = json.loads((DATA / "speech-concept-family-crosswalk.json").read_text())
    queue = json.loads((DATA / "icassp-2026-semantic-review-queue.json").read_text())
    queue_rows = queue.get("rows", [])
    crosswalk_by_id = {row["concept_id"]: row for row in crosswalk.get("records", [])}
    subthemes = {}
    concepts = {}
    for theme in taxonomy.get("themes", []):
        for subtheme in theme.get("subthemes", []):
            subthemes[subtheme["id"]] = subtheme
            for concept in subtheme.get("concepts", []):
                concepts[concept["id"]] = (theme, subtheme, concept)

    gaps = []
    nearby_terms = {
        "articulatory-coordination": ["articulat", "coarticul", "emg", "vocal tract", "tongue"],
        "packet-loss-concealment": ["packet loss", "conceal", "lost region", "network degradation", "missing"],
        "disfluency-preservation": ["disflu", "stutter", "dysarth", "hesitat", "repetition", "repair"],
        "user-control-and-consent": ["consent", "opt-out", "unlearning", "anonym", "voice cloning", "privacy"],
    }
    for concept_id, (theme, subtheme, concept) in concepts.items():
        row = crosswalk_by_id.get(concept_id, {})
        if row.get("icassp_reviewed_count", 0) != 0:
            continue
        candidates = []
        nearby_reviewed = []
        for paper in queue_rows:
            text = ((paper.get("title") or "") + " " + (paper.get("evidence_excerpt") or "")).lower()
            score = sum(text.count(term) for term in nearby_terms.get(concept_id, []))
            review = paper.get("analyst_review") or {}
            if score and paper.get("decision") == "supported" and review.get("concept_id") != concept_id:
                nearby_reviewed.append({
                    "paper_id": paper.get("paper_id"),
                    "title": paper.get("title"),
                    "score": score,
                    "assigned_concept_id": review.get("concept_id"),
                    "assigned_subtheme_id": review.get("subtheme_id"),
                    "boundary": "Lexical or abstract proximity is not membership; the paper remains assigned to its reviewed primary concept.",
                })
            if paper.get("review_state") != "needs-analyst-semantic-review":
                continue
            if not paper.get("in_speech_audio_scope"):
                continue
            if any(candidate.get("subtheme_id") == subtheme["id"] for candidate in paper.get("candidate_assignments", [])):
                candidates.append({
                    "paper_id": paper.get("paper_id"),
                    "title": paper.get("title"),
                    "decision": paper.get("decision"),
                    "evidence_depth": paper.get("evidence_depth"),
                    "evidence_excerpt": paper.get("evidence_excerpt"),
                })
        gaps.append({
            "theme_id": theme["id"],
            "subtheme_id": subtheme["id"],
            "concept_id": concept_id,
            "concept_name": concept["name"],
            "ordinary_problem": concept["definition"],
            "boundary": concept["boundary"],
            "interspeech_reviewed_count": row.get("interspeech_reviewed_count", 0),
            "icassp_reviewed_count": row.get("icassp_reviewed_count", 0),
            "nearest_unresolved_candidates": candidates[:8],
            "nearby_reviewed_candidates": sorted(nearby_reviewed, key=lambda item: (-item["score"], item["title"] or ""))[:8],
            "next_evidence_needed": "An analyst must inspect the title/abstract or full paper and show that this concept, rather than a neighboring one, is central to the paper's ordinary speech problem.",
        })

    payload = {
        "schema_version": 1,
        "status": "explicit-concept-evidence-gaps",
        "claim_boundary": "A gap means no analyst-reviewed ICASSP record currently supports this concept; it does not mean the conference contains no such work.",
        "gap_count": len(gaps),
        "gaps": gaps,
    }
    (DATA / "speech-concept-evidence-gaps.json").write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
    lines = [
        "# Speech concept evidence gaps",
        "",
        "These are taxonomy concepts with no analyst-reviewed ICASSP example in the current bounded release. The absence is an evidence gap, not a prevalence claim.",
        "",
        f"- Gaps: {len(gaps)}",
        "- Source boundary: ICASSP title/abstract metadata; most records are title-only.",
        "",
    ]
    for gap in gaps:
        lines += [f"## {gap['concept_name']} (`{gap['concept_id']}`)", "", f"**Ordinary problem:** {gap['ordinary_problem']}", "", f"**Boundary:** {gap['boundary']}", "", f"**INTERSPEECH reviewed examples:** {gap['interspeech_reviewed_count']}", f"**ICASSP reviewed examples:** {gap['icassp_reviewed_count']}", "", "**Nearest unresolved ICASSP candidates:**", ""]
        if gap["nearest_unresolved_candidates"]:
            for candidate in gap["nearest_unresolved_candidates"]:
                lines.append(f"- {candidate['title']} ({candidate['evidence_depth']}; {candidate['decision']})")
        else:
            lines.append("- No candidate was found by the current subtheme proposal rules.")
        lines += ["", "**Nearby reviewed records not counted as membership:**", ""]
        if gap["nearby_reviewed_candidates"]:
            for candidate in gap["nearby_reviewed_candidates"]:
                lines.append(f"- {candidate['title']} — assigned to `{candidate['assigned_subtheme_id']}/{candidate['assigned_concept_id']}`; {candidate['boundary']}")
        else:
            lines.append("- No nearby reviewed record was found by the bounded term screen.")
        lines += ["", f"**Next evidence needed:** {gap['next_evidence_needed']}", ""]
    (REPORTS / "SPEECH_CONCEPT_EVIDENCE_GAPS.md").write_text("\n".join(lines) + "\n")
    print(json.dumps({"gap_count": len(gaps), "report": str(REPORTS / 'SPEECH_CONCEPT_EVIDENCE_GAPS.md')}))


if __name__ == "__main__":
    main()
