#!/usr/bin/env python3
"""Align D3 note and claim taxonomy IDs with authoritative semantic assignments."""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = HERE / "data"
deep = {
    json.loads(line)["paper_id"]: json.loads(line)
    for line in (DATA / "interspeech-2025-deep-paper-analyses.jsonl").read_text().splitlines()
    if line.strip()
}
changed_notes = changed_claims = 0
for path in sorted(DATA.glob("interspeech-2025-*-d3-notes.json")):
    payload = json.loads(path.read_text())
    changed = False
    for note in payload.get("notes", []):
        row = deep.get(note.get("paper_id"), {})
        assignment = row.get("semantic_review", {})
        if row.get("depth") != "D3" or not assignment.get("theme_id"):
            continue
        for key in ("theme_id", "subtheme_id", "concept_id"):
            if note.get(key) != assignment.get(key):
                note[key] = assignment.get(key)
                changed = True
                changed_notes += 1
    if changed:
        path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")

for path in sorted(DATA.glob("interspeech-2025-*-claim-ledger.json")):
    payload = json.loads(path.read_text())
    changed = False
    for claim in payload.get("claims", []):
        assignment = deep.get(claim.get("paper_id"), {}).get("semantic_review", {})
        if assignment.get("subtheme_id") and claim.get("subtheme") != assignment["subtheme_id"]:
            claim["subtheme"] = assignment["subtheme_id"]
            changed = True
            changed_claims += 1
    if changed:
        path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
print(json.dumps({"changed_note_fields": changed_notes, "changed_claims": changed_claims}))
