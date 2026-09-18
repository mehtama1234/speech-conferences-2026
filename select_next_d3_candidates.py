"""Print uncaptured D2 candidates for the lowest-count subthemes."""
import glob, json
captured = set()
for filename in glob.glob("data/*d3-papers.json"):
    try:
        captured.update(row["paper_id"] for row in json.load(open(filename))["papers"])
    except (OSError, KeyError, json.JSONDecodeError):
        pass
queue = json.load(open("data/interspeech-2025-semantic-review-queue.json"))["rows"]
targets = {"time-frequency-measurement", "noise-enhancement", "source-separation-and-spatial-listening", "acoustic-unit-mapping", "voice-identity-and-conversion", "speaker-characteristics", "human-centered-evaluation", "accent-and-cultural-boundaries", "robustness-and-system-boundary"}
for subtheme in sorted(targets):
    rows = [row for row in queue if row["paper_id"] not in captured and row.get("evidence_depth") == "D2" and row.get("decision") == "supported" and row.get("analyst_review", {}).get("subtheme_id") == subtheme]
    print("##", subtheme)
    for row in rows[:6]:
        print(row["paper_id"], "|", row["title"])
