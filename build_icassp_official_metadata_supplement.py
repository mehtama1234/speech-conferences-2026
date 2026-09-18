"""Capture the official ICASSP accepted-paper title and paper-number manifest."""
import hashlib
import html
import json
import re
import unicodedata
import urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = HERE / "data"
URL = "https://cmsworkshops.com/ICASSP2026/papers/accepted_papers.php"

def norm(value):
    return re.sub(r"[^a-z0-9]+", "", unicodedata.normalize("NFKC", value).lower())

raw = urllib.request.urlopen(URL, timeout=60).read()
text = raw.decode("utf-8", "replace")
official = [
    (number, html.unescape(re.sub(r"<[^>]+>", "", title)).strip())
    for number, title in re.findall(r"<tr><td>(\d+)</td><td>(.*?)</td></tr>", text, re.S)
]
official_by_title = {norm(title): (number, title) for number, title in official}
discovery = json.loads((DATA / "icassp-2026-papers.json").read_text())["papers"]
records = []
unmatched = []
for paper in discovery:
    match = official_by_title.get(norm(paper["title"]))
    if match:
        number, title = match
        records.append({
            "paper_id": paper["paperId"],
            "title": paper["title"],
            "official_title": title,
            "official_paper_number": number,
            "doi": paper.get("doi"),
            "official_source_url": URL,
            "metadata_evidence_depth": "D1",
            "match_rule": "normalized title exact match",
        })
    else:
        unmatched.append({
            "paper_id": paper["paperId"],
            "title": paper["title"],
            "reason": "not found by normalized title in official accepted-paper manifest",
        })
payload = {
    "schema_version": 2,
    "venue": "ICASSP 2026",
    "source": "official ICASSP accepted-paper page",
    "source_url": URL,
    "captured_bytes": len(raw),
    "source_sha256": hashlib.sha256(raw).hexdigest(),
    "official_row_count": len(official),
    "discovery_record_count": len(discovery),
    "matched_record_count": len(records),
    "unmatched_record_count": len(unmatched),
    "coverage_boundary": "Official title/paper-number metadata is matched for the records listed below; the supplement does not provide abstracts, full proceedings text, or scientific evidence, and unmatched discovery records remain visibly unresolved.",
    "records": records,
    "unmatched": unmatched,
}
(DATA / "icassp-2026-official-metadata-supplement.json").write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
print(json.dumps({"official_rows": len(official), "discovery_records": len(discovery), "matched": len(records), "unmatched": len(unmatched), "source_sha256": payload["source_sha256"]}))
