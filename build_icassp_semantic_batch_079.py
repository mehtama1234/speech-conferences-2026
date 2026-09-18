"""Targeted adjudication of clear non-speech audio-boundary cases."""
import hashlib, json
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = HERE / "data"
OUT = DATA / "icassp-2026-semantic-reviewed-batch-079.json"
if OUT.exists():
    p = json.loads(OUT.read_text())
    print(json.dumps({"batch_id": p["batch_id"], "status": "preserved-input", "reviewed_count": p["reviewed_count"]}))
    raise SystemExit(0)

IDS = {
    "4df1d9009b5ecfb874087881f554e07f6822649e": "Novel-view audio synthesis from visual-acoustic representations is a general audiovisual generation task; the title does not identify spoken speech.",
    "651244b67d331bf43c9dbcf6acf00baf481864be": "Anomalous sound detection concerns unusual environmental or machine sounds, not spoken speech.",
    "879a37d5d77193818a4f02a99d004cce472c903f": "Sensor-array and camera fusion for 3D source localization is spatial sensing, not a speech task.",
    "90ffd47c2ab04e09f930f1e632846ae7e39d852f": "Source localization and acoustic inversion estimate physical sound-scene properties without identifying spoken speech.",
    "9886c6d519b49561981fec4667232a51e4945e3e": "An audio-visual object dataset is a general audiovisual perception resource; the title does not establish a spoken-speech task.",
    "9b56cc7688900de3c09c515e8fcfe99bd6686cb1": "Sensitive audio-visual content detection is a broad content-moderation task, not a speech-specific task.",
    "afed95ad7a7709e929063f8f8f0269ef1a0b5435": "RIR tracking and sound-field control are room-acoustic control problems, not spoken-speech processing.",
    "b3eb41c12bab26203b9bfb1fa46b9e6fe3e8b50d": "Acoustic-parameter estimation with smart glasses measures the sound field; it does not identify a spoken-speech task.",
    "b3eb5962a0cf829aec20cb89cc30710ac049930a": "Sagittal-plane sound localization estimates where sound comes from, not what spoken speech means or how it is produced.",
    "bd340b20debd34e3874a424ea829d9ce9e314cf7": "Heart-sound synthesis is a cardiac auscultation task, distinct from spoken speech.",
    "c5f1a0aa5bd35f8085688ebdf0c710bb2b4113ca": "Audio-visual match-cut retrieval supports video editing and does not identify spoken speech as the task object.",
    "d2b6797137c88a48d3570b86982ef95d2d71ab46": "Industrial and surveillance sound-event selection concerns environmental events, not spoken speech.",
    "d654cb0abdd16bf6de181f83087a8a00ac6c65bd": "Video-to-music generation is a musical generation task, not spoken-speech generation.",
    "da0da647400cdae68b9edf7f7b0f7b34abdbfd5a": "Music classification concerns musical content rather than spoken speech.",
    "dda90516b5640ae43bce33e037b4137fb5d0b2a2": "Interference reduction for musical recordings is music production, not speech enhancement.",
    "e36afd25155bebedcf6877af73ee0401b0195328": "Neural coding during music imagery and perception studies musical cognition, not spoken speech.",
    "ec2bd3551d710f533e23cf1fbea53672d6f26304": "Audio-visual video-moment retrieval is a general video-search task and does not establish spoken speech.",
    "f5d3286735987a8ec26fa3e73f42f673f9eaf5a2": "Face-phone interaction detection is visual behavior understanding, not speech.",
    "fe64d60df25fce4975c21104d684b8912d7e10d2": "Audio-driven 3D mesh generation uses sound to shape geometry; it is not a spoken-speech task.",
}
queue = json.loads((DATA / "icassp-2026-semantic-review-queue.json").read_text())
papers = {p["paperId"]: p for p in json.loads((DATA / "icassp-2026-papers.json").read_text())["papers"]}
rows = []
for pid, reasoning in IDS.items():
    candidate = next(r for r in queue["rows"] if r["paper_id"] == pid)
    if candidate.get("review_state") == "analyst-reviewed":
        raise SystemExit(f"already reviewed: {pid}")
    p = papers[pid]
    abstract = p.get("abstract") or ""
    depth = "D2" if abstract else "D1"
    rows.append({"paper_id": pid, "title": p["title"], "decision": "unsupported", "confidence": f"analyst-reviewed-{depth}", "theme_id": None, "subtheme_id": None, "concept_id": None, "semantic_reasoning": reasoning, "evidence_excerpt": abstract[:1200] if abstract else p["title"], "source_location": p.get("url"), "source_sha256": hashlib.sha256(abstract.encode()).hexdigest(), "evidence_depth": depth, "review_state": "analyst-reviewed", "claim_boundary": "ICASSP discovery metadata; this resolves taxonomy membership only and does not characterize scientific quality or full-paper mechanism."})
payload = {"schema_version": 1, "batch_id": "icassp-2026-semantic-batch-079", "status": "analyst-reviewed-targeted-non-speech-audio-boundary-batch", "claim_boundary": "These decisions exclude explicit sound-event, room-acoustic, localization, music, audiovisual-retrieval, and geometry-generation tasks from the spoken-speech taxonomy using preserved title/abstract evidence. Generic audio-language cases remain unresolved.", "reviewed_count": len(rows), "rows": rows}
OUT.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
print(json.dumps({"batch_id": payload["batch_id"], "reviewed_count": len(rows), "unsupported": len(rows)}))

