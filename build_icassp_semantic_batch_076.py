"""Targeted adjudication of clear speech and adjacent-audio boundary cases."""
import hashlib, json
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = HERE / "data"
OUT = DATA / "icassp-2026-semantic-reviewed-batch-076.json"
if OUT.exists():
    p = json.loads(OUT.read_text())
    print(json.dumps({"batch_id": p["batch_id"], "status": "preserved-input", "reviewed_count": p["reviewed_count"]}))
    raise SystemExit(0)

ASSIGNMENTS = {
    "4d989bc72dbc0c12ff4c28dd4d73d75c69953cb4": ("supported", "evaluation-deployment-and-consequence", "privacy-security-and-accountability", "spoofing-and-deepfake", "The title identifies a speaker anti-spoofing system, a speech-identity security problem.", "speech anti-spoofing"),
    "ea768741d49d91543ade5e922f0ba1ae227d9ad8": ("supported", "evaluation-deployment-and-consequence", "privacy-security-and-accountability", "spoofing-and-deepfake", "The title identifies the SASV anti-spoofing track, which evaluates whether a claimed speaker is genuine rather than synthetic or replayed.", "speech anti-spoofing"),
    "a5cd9da36fe1f22fd0f502fa06d0eca7385b9466": ("supported", "recognition-and-alignment", "adaptation-and-open-vocabulary", "open-vocabulary-recognition", "Keyword spotting is the bounded speech problem of detecting a spoken command in a continuous stream.", "speech keyword spotting"),
    "b2988abe0d2256450a910514d500edbb9b99516f": ("supported", "people-variation-and-health", "clinical-and-assistive-speech", "clinical-speech-marker", "Automatic stuttering detection treats a speech production pattern as a clinical or assistive signal.", "clinical speech"),
    "0716a2bf593e9edfa45289e7701c5a2eb345088c": ("unsupported", None, None, None, "Reverb emulation is an audio effect problem, but the title does not identify speech or a speech-specific task.", "adjacent audio"),
    "7448b8bdc8b7f056bcfb716d187d0facffdbbe29": ("unsupported", None, None, None, "Singing skill evaluation concerns musical singing rather than spoken speech.", "music"),
    "83d821e5b474501646ce2dc019e46b6a70801070": ("unsupported", None, None, None, "Accompaniment generation from solo singing is a music-generation task, not spoken speech.", "music"),
    "b732c543ecd09c4e5a9e44b04a35e30013cd92b6": ("unsupported", None, None, None, "Singing melody extraction targets musical pitch and melody rather than spoken speech.", "music"),
    "976a305140e0b528c5f15b987fc7a89dd225d42d": ("unsupported", None, None, None, "A learned lossless audio codec addresses general audio compression; the title supplies no speech-specific object or test.", "adjacent audio"),
    "a52d9732b2a3dafda9e1ac5dba41680636fc59d4": ("unsupported", None, None, None, "Bandwidth extension for an audio codec is a general audio reconstruction task, not a speech-specific task.", "adjacent audio"),
    "fad76002bf342b3eb0b8d697266406e9b4a76ad3": ("unsupported", None, None, None, "Sound-event detection identifies environmental events; the title does not establish spoken speech.", "sound events"),
    "d87aa887a0bb643a4729e3aec4d8293163021a88": ("unsupported", None, None, None, "Bioacoustic recognition concerns animal or ecological sounds, not spoken human speech.", "bioacoustics"),
    "dcd5ddaeec7b15b44c1b10da7db063232179c933": ("unsupported", None, None, None, "The title explicitly concerns corvid vocal repertoires, outside the spoken-speech taxonomy.", "animal vocalization"),
    "f1531d0344d922d6e9ce494ed477492f4ecb598d": ("unsupported", None, None, None, "Binaural distance estimation in reverberant rooms is an audio spatial-perception task, but no speech object is identified.", "adjacent audio"),
    "80d4551c919fb2d15f32a9a7fe5e03e15a5d5212": ("unsupported", None, None, None, "Audio captioning is a broad audio-to-text description task; the preserved title does not establish spoken speech.", "adjacent audio"),
}
queue = json.loads((DATA / "icassp-2026-semantic-review-queue.json").read_text())
papers = {p["paperId"]: p for p in json.loads((DATA / "icassp-2026-papers.json").read_text())["papers"]}
rows = []
for pid, (decision, theme, subtheme, concept, reasoning, family) in ASSIGNMENTS.items():
    candidate = next(r for r in queue["rows"] if r["paper_id"] == pid)
    if candidate.get("review_state") == "analyst-reviewed":
        raise SystemExit(f"already reviewed: {pid}")
    p = papers[pid]
    abstract = p.get("abstract") or ""
    depth = "D2" if abstract else "D1"
    rows.append({"paper_id": pid, "title": p["title"], "decision": decision, "confidence": f"analyst-reviewed-{depth}", "theme_id": theme, "subtheme_id": subtheme, "concept_id": concept, "semantic_reasoning": reasoning, "evidence_excerpt": abstract[:1200] if abstract else p["title"], "source_location": p.get("url"), "source_sha256": hashlib.sha256(abstract.encode()).hexdigest(), "evidence_depth": depth, "review_state": "analyst-reviewed", "claim_boundary": f"ICASSP discovery metadata; this resolves taxonomy membership as {family} only and does not characterize scientific quality or full-paper mechanism."})
payload = {"schema_version": 1, "batch_id": "icassp-2026-semantic-batch-076", "status": "analyst-reviewed-targeted-speech-adjacent-boundary-batch", "claim_boundary": "These targeted decisions distinguish explicit speech tasks from adjacent audio and music tasks using preserved title/abstract evidence.", "reviewed_count": len(rows), "rows": rows}
OUT.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
print(json.dumps({"batch_id": payload["batch_id"], "reviewed_count": len(rows), "supported": sum(r["decision"] == "supported" for r in rows), "unsupported": sum(r["decision"] == "unsupported" for r in rows)}))
