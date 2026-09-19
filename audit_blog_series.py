#!/usr/bin/env python3
"""Audit the standalone blog series for coverage, links, and cliché leakage."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data"
REPORTS = ROOT / "reports"
BLOGS = REPORTS / "blogs"

BANNED_CLICHES = [
    "in today's rapidly changing world",
    "at the forefront",
    "cutting-edge",
    "game-changing",
    "paradigm shift",
    "unlock the potential",
    "revolutionize",
    "seamlessly",
]


def main():
    manifest = json.loads((DATA / "speech-blog-series-manifest.json").read_text())
    taxonomy = json.loads((DATA / "speech-first-principles-taxonomy.json").read_text())
    failures = []
    warnings = []
    records = []
    expected_subthemes = []
    for theme in taxonomy.get("themes", []):
        expected_subthemes.extend(s["name"] for s in theme.get("subthemes", []))
    if manifest.get("theme_count") != 8 or manifest.get("subtheme_count") != 34:
        failures.append("manifest does not cover 8 themes and 34 subthemes")
    for essay in manifest.get("essays", []):
        path = ROOT / essay["path"]
        if not path.exists():
            failures.append(f"missing essay: {essay['path']}")
            continue
        text = path.read_text()
        missing = []
        for marker in ("## Start with the baseline", "## The boundaries", "## Plain-language dictionary", "## Closing note", "**The pressure.**", "**Why the easy answer breaks.**", "**The move that recurs.**", "**What this evidence does not establish.**", "**Where this boundary stops.**", "### Words used in this section", "### What the evidence shows"):
            if marker not in text:
                missing.append(marker)
        subtheme_count = sum(1 for name in expected_subthemes if f"## {name}\n" in text)
        if subtheme_count != essay["subtheme_count"]:
            failures.append(f"{essay['theme_id']}: expected {essay['subtheme_count']} subthemes, found {subtheme_count}")
        lower = text.lower()
        found_cliches = [phrase for phrase in BANNED_CLICHES if phrase in lower]
        if found_cliches:
            warnings.append({"essay": essay["theme_id"], "cliches": found_cliches})
        links = re.findall(r"\[[^\]]+\]\((https?://[^)]+)\)", text)
        if not links:
            failures.append(f"{essay['theme_id']}: no paper links")
        if "D2 means" not in text and "**D2.**" not in text:
            failures.append(f"{essay['theme_id']}: D2 is not defined in plain language")
        if "D3 means" not in text and "**D3.**" not in text:
            failures.append(f"{essay['theme_id']}: D3 is not defined in plain language")
        if missing:
            failures.append(f"{essay['theme_id']}: missing {', '.join(missing)}")
        records.append({"theme_id": essay["theme_id"], "word_count": len(text.split()), "subtheme_count": subtheme_count, "paper_link_count": len(links), "missing": missing, "cliche_warnings": found_cliches})
    payload = {"status": "pass" if not failures else "incomplete", "claim_boundary": "Coverage and language audit only; it does not prove that every conceptual sentence is correct or that every paper result is independently reproduced.", "essay_count": len(records), "subtheme_count": sum(r["subtheme_count"] for r in records), "failures": failures, "warnings": warnings, "records": records}
    (DATA / "speech-blog-series-audit.json").write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
    lines = ["# Blog series audit", "", f"**Status:** `{payload['status']}`", "", payload["claim_boundary"], "", f"Essays: **{payload['essay_count']}**; subtheme sections: **{payload['subtheme_count']}**; failures: **{len(failures)}**.", "", "| Essay | Words | Subthemes | Paper links | Cliché warnings |", "|---|---:|---:|---:|---|"]
    for row in records:
        lines.append(f"| {row['theme_id']} | {row['word_count']} | {row['subtheme_count']} | {row['paper_link_count']} | {', '.join(row['cliche_warnings']) or '—'} |")
    if failures:
        lines += ["", "## Failures", ""] + [f"- {f}" for f in failures]
    (REPORTS / "SPEECH_BLOG_SERIES_AUDIT.md").write_text("\n".join(lines) + "\n")
    print(json.dumps({"status": payload["status"], "essays": payload["essay_count"], "subthemes": payload["subtheme_count"], "failures": len(failures), "warnings": len(warnings)}))


if __name__ == "__main__":
    main()
