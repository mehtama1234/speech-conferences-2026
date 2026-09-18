#!/usr/bin/env python3
"""Build a first-principles cross-venue comparison with honest denominators."""

from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = HERE / "data"


def load(name):
    return json.loads((DATA / name).read_text())


def proposal_counts(queue, level):
    counts = Counter()
    for row in queue["rows"]:
        candidates = row.get("candidate_assignments", [])
        if row.get("decision") == "unsupported" or not candidates:
            continue
        key = candidates[0].get(level)
        if key:
            counts[key, row.get("decision")] += 1
    return counts


taxonomy = load("speech-first-principles-taxonomy.json")
inter = load("interspeech-2025-semantic-review-queue.json")
icassp = load("icassp-2026-semantic-review-queue.json")
icassp_batch = load("icassp-2026-semantic-reviewed-batch-001.json")
inter_theme = proposal_counts(inter, "theme_id")
icassp_theme = proposal_counts(icassp, "theme_id")
inter_subtheme = proposal_counts(inter, "subtheme_id")
icassp_subtheme = proposal_counts(icassp, "subtheme_id")

def reviewed_theme_counts(queue):
    counts = Counter()
    for row in queue["rows"]:
        if row.get("review_state") != "analyst-reviewed":
            continue
        review = row.get("analyst_review", row)
        theme_id = review.get("theme_id")
        if theme_id:
            counts[theme_id, row.get("evidence_depth")] += 1
    return counts

inter_reviewed = reviewed_theme_counts(inter)
icassp_reviewed = reviewed_theme_counts(icassp)

def reviewed_row(queue, paper_id):
    for row in queue["rows"]:
        if row.get("paper_id") == paper_id and row.get("review_state") == "analyst-reviewed":
            review = row.get("analyst_review", row)
            return {"paper_id": paper_id, "title": row.get("title"), "evidence_depth": row.get("evidence_depth"), "decision": row.get("decision"), "semantic_reasoning": review.get("semantic_reasoning", row.get("semantic_reasoning", ""))}
    return None

def contrast(label, ordinary, inter_id, icassp_id, difference, boundary):
    i = reviewed_row(inter, inter_id); c = reviewed_row(icassp, icassp_id)
    if not i or not c:
        return None
    return {
        "label": label,
        "ordinary_problem": ordinary,
        "interspeech": i,
        "icassp": c,
        "assignment_links": {"interspeech_paper_id": inter_id, "icassp_paper_id": icassp_id},
        "denominator_statement": "INTERSPEECH comparison context is the 1,179-record archive corpus; ICASSP comparison context is the 3,864-record captured corpus, with this named contrast using one reviewed paper from each venue.",
        "conceptual_difference": difference,
        "evidence_boundary": boundary,
    }

conceptual_contrasts = [x for x in [
    contrast("Mixtures and competing speakers", "A listener or recognizer must decide which voice belongs to which person when speech overlaps.", "alizadeh25_interspeech", "6599ad30ece84a9f571a837dbf05989981c9ac5b", "INTERSPEECH makes unknown speaker count the central structural problem and recursively peels voices apart; the reviewed ICASSP paper treats meeting diarization and enhancement as coupled spatial decisions in a changing room.", "INTERSPEECH is D3 full-paper evidence; ICASSP is D2 abstract evidence, so this is a mechanism contrast, not a venue prevalence claim."),
    contrast("Recognition and usable boundaries", "Recognizing words is not enough if the system cannot decide when a unit is complete or how it becomes usable text.", "ho25_interspeech", "04bc5dc9cb6f4ffdb8109153c0762ceb4ec93fba", "INTERSPEECH uses dynamic right-context and chunk size for streaming inverse text normalization; the ICASSP title-bounded assignment concerns semantic chunking and label delay inside a speech-language stream.", "The INTERSPEECH mechanism is D3; the ICASSP assignment is D1 title evidence and cannot support outcome or mechanism detail."),
    contrast("Emotion as interactional evidence", "Emotion is not a fixed label in the waveform; it is inferred from changing cues, missing channels, and listener interpretation.", "hu25c_interspeech", "11303a06ceaffe7797c7617cf893255fb38f02d4", "INTERSPEECH uses label semantics as anchors for subtle emotion boundaries; the ICASSP paper frames uncertainty-aware reasoning over multimodal conversation as the way to handle ambiguous evidence.", "Both are abstract-bounded D2 assignments here; neither establishes general emotional understanding or comparable performance across venues."),
    contrast("Creating speech while preserving identity", "A speech generator must change the requested content or style without accidentally changing who is speaking or how understandable the result is.", "zalkow25_interspeech", "1d9d53c8debfbf7ed246bd7a53cdd1342998264c", "INTERSPEECH separates low-resource TTS generation from a naturalness postprocessor and checks listener judgments; the ICASSP abstract assignment focuses on aligning text with rich semantic representations during synthesis.", "The INTERSPEECH result is D3 and author-reported; the ICASSP comparison is D2 abstract evidence, so quality and mechanism are not directly comparable.")
] if x is not None]

crosswalk = []
for theme in taxonomy["themes"]:
    tid = theme["id"]
    crosswalk.append({
        "theme_id": tid,
        "theme_name": theme["name"],
        "interspeech_supported_proposals": inter_theme[tid, "supported"],
        "interspeech_ambiguous": inter_theme[tid, "ambiguous"],
        "interspeech_insufficient": inter_theme[tid, "insufficient-evidence"],
        "icassp_supported_proposals": icassp_theme[tid, "supported"],
        "icassp_ambiguous": icassp_theme[tid, "ambiguous"],
        "icassp_insufficient": icassp_theme[tid, "insufficient-evidence"],
    })

payload = {
    "comparison": "First-principles analyst-reviewed assignment crosswalk: ICASSP 2026 and INTERSPEECH 2025",
    "denominators": {
        "icassp_all_records": icassp["paper_count"],
        "icassp_with_abstract": icassp["with_abstract"],
        "interspeech_all_records": inter["paper_count"],
        "interspeech_with_abstract": inter["paper_count"],
        "icassp_unsupported_for_speech_taxonomy": icassp["decision_counts"]["unsupported"],
    },
    "evidence_depth": {
        "icassp": "D1 title-only for records without abstract; D2 abstract-supported for 683 records; discovery metadata rather than official proceedings.",
        "interspeech": f"D2 official archive paper pages and abstracts; D3 full-paper evidence currently covers {sum(row.get('evidence_depth') == 'D3' for row in inter['rows'])} captured papers.",
    },
    "analyst_reviewed_seed": {
        "interspeech": inter.get("reviewed_count", 0),
        "icassp": icassp.get("reviewed_count", 0),
    },
    "analyst_reviewed_by_theme": [
        {
            "theme_id": theme["id"],
            "interspeech_d2": inter_reviewed[theme["id"], "D2"],
            "interspeech_d3": inter_reviewed[theme["id"], "D3"],
            "icassp_d2": icassp_reviewed[theme["id"], "D2"],
            "icassp_d3": icassp_reviewed[theme["id"], "D3"],
        }
        for theme in taxonomy["themes"]
    ],
    "crosswalk": crosswalk,
    "conceptual_contrasts": conceptual_contrasts,
        "subtheme_assignment_counts": {
        "interspeech": {"supported": sum(inter_subtheme.values())},
        "icassp": {"supported": sum(icassp_subtheme.values())},
    },
    "comparability_boundaries": [
        "Counts are analyst-reviewed primary-candidate assignments, not prevalence estimates.",
        "A paper can have multiple candidate subthemes; the table uses only the highest-scoring candidate for a compact comparison.",
        "ICASSP contains a broad non-speech corpus; unsupported rows remain in its denominator rather than being discarded.",
        "ICASSP title-only records cannot support abstract-level mechanism or outcome claims.",
        f"INTERSPEECH abstracts are available for all records, but only {sum(row.get('evidence_depth') == 'D3' for row in inter['rows'])} papers currently have captured full-paper D3 notes.",
    ],
}
(DATA / "icassp-interspeech-crosswalk.json").write_text(json.dumps(payload, indent=2) + "\n")

lines = [
    "# ICASSP 2026 / INTERSPEECH 2025 first-principles crosswalk",
    "",
    "This comparison uses the new conceptual taxonomy. Its compact counts are analyst-reviewed primary-candidate assignments; they are not venue prevalence claims.",
    "",
    f"- ICASSP denominator: {icassp['paper_count']:,}; {icassp['with_abstract']:,} D2 abstracts and {icassp['paper_count'] - icassp['with_abstract']:,} D1 title-only records.",
    f"- INTERSPEECH denominator: {inter['paper_count']:,} D2 archive records.",
    f"- ICASSP records unsupported for the speech taxonomy remain visible: {icassp['decision_counts']['unsupported']:,}.",
    f"- Analyst-reviewed semantic records: {icassp.get('reviewed_count', 0)} ICASSP abstract records versus {inter.get('reviewed_count', 0)} INTERSPEECH D2/D3 records.",
    "",
    "| First-principles theme | INTERSPEECH supported assignment | INTERSPEECH ambiguous | ICASSP supported assignment | ICASSP ambiguous |",
    "|---|---:|---:|---:|---:|",
]
for row in crosswalk:
    lines.append(f"| {row['theme_name']} | {row['interspeech_supported_proposals']:,} | {row['interspeech_ambiguous']:,} | {row['icassp_supported_proposals']:,} | {row['icassp_ambiguous']:,} |")
lines += [
    "",
    "## Analyst-reviewed evidence by theme",
    "",
    "These are counts of explicit analyst-reviewed assignments, separated by evidence depth. They are a reviewed sample, not venue prevalence.",
    "",
    "| First-principles theme | INTERSPEECH D2 | INTERSPEECH D3 | ICASSP D2 | ICASSP D3 |",
    "|---|---:|---:|---:|---:|",
]
for theme in taxonomy["themes"]:
    tid = theme["id"]
    lines.append(f"| {theme['name']} | {inter_reviewed[tid, 'D2']} | {inter_reviewed[tid, 'D3']} | {icassp_reviewed[tid, 'D2']} | {icassp_reviewed[tid, 'D3']} |")
lines += [
    "",
    "## Named conceptual contrasts",
    "",
    "These are deliberately small, paper-grounded comparisons rather than claims about which venue is larger or better.",
]
for item in conceptual_contrasts:
    lines += [f"### {item['label']}", "", f"**Ordinary problem:** {item['ordinary_problem']}", "", f"**INTERSPEECH assignment:** `{item['assignment_links']['interspeech_paper_id']}` — {item['interspeech']['title']} ({item['interspeech']['evidence_depth']}) — {item['interspeech']['semantic_reasoning']}", "", f"**ICASSP assignment:** `{item['assignment_links']['icassp_paper_id']}` — {item['icassp']['title']} ({item['icassp']['evidence_depth']}) — {item['icassp']['semantic_reasoning']}", "", f"**Denominator:** {item['denominator_statement']}", "", f"**Conceptual contrast:** {item['conceptual_difference']}", "", f"**Boundary:** {item['evidence_boundary']}", ""]
lines += [
    "## What can be said now",
    "",
    "The two corpora can now be compared using the same conceptual questions, but not yet as settled research emphasis. INTERSPEECH has complete abstract evidence and a speech-focused denominator. ICASSP has a much broader denominator and mostly title-only evidence, so its proposed assignments are both less certain and more affected by scope filtering.",
    "",
    "The reviewed table is evidence about the explicit corpus assignments, not a random sample and not a prevalence estimate. The remaining comparison gate is comparable D3 review in both venues. Until then, differences in the assignment table may reflect source access, title vocabulary, and the 3,182 ICASSP records without abstracts rather than differences in research activity.",
]
(HERE / "reports/ICASSP_2026_INTERSPEECH_2025_CROSSWALK.md").write_text("\n".join(lines) + "\n")
print(f"wrote {HERE / 'reports/ICASSP_2026_INTERSPEECH_2025_CROSSWALK.md'}")
