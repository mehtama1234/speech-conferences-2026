"""Resolve ambiguity cases whose object is demonstrably outside speech/audio."""
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = HERE / "data"
OUT = DATA / "icassp-2026-semantic-reviewed-batch-061.json"

if OUT.exists():
    payload = json.loads(OUT.read_text())
    print(json.dumps({"batch_id": payload["batch_id"], "status": "preserved-input", "reviewed_count": payload["reviewed_count"]}))
    raise SystemExit(0)

titles = {
    "232ad35f8e0c0f4824e3fb6ad467fae61c101719": "The object is social-media popularity prediction; multimodal retrieval is not evidence that the task is speech or audio.",
    "3c8d8e19244b7bc9df26ebb6bf3bbe256b7acb6b": "The object is electromagnetic interference in OPM-MEG biosignals, not a speech or audio recording.",
    "3cacac9acfa2acce23930c2e8564bf69d5e17ad5": "The object is a spiked-matrix estimation problem with rotationally invariant mathematical noise, not speech or audio.",
    "4a7fa1ca25a87ff62dc52066262280ff0b2d043a": "The object is class-incremental continual learning; noise perturbations are a training device, not an audio signal.",
    "70f27f782cd16116b06953a8924fdcd00df80e78": "CFAR detection in colored Gaussian noise is a generic detection problem; the title gives no speech or audio object.",
    "780da3d2977505744d08aaf4609b7049f0c0d46c": "The object is Bayesian calibration for retrieval-augmented text generation, not speech or audio.",
    "86d9ee619a351f061fe1cc5c5b1a452912f28c1f": "The object is reconstruction of brain activation, not a speech or audio signal.",
    "8aa7a225e9158cda3535ec8f3c9d4b3faf5ce772": "The object is attributed text generation; signal-to-noise is a metaphor for contextual information.",
    "a374184314bc38d5a22b4e7c9e388ca4f298392c": "The object is biosignal classification; no speech or audio object is identified.",
    "b75e000c9ef276237fd161ae9397e6bf37410e4e": "The object is dataset pruning for generic noisy labels, not speech or audio.",
    "b9d1213442a0f977476d7c5274ab6c28cd85bdb6": "The object is detection of unknown LFM signals below a noise floor; the preserved record does not identify speech or an audio source.",
    "bab9bf6e1f09c7b77571d95bf29804073da6591b": "The object is measurement-noise estimation for Kalman filters, not speech or audio.",
    "c9886e6988e1fcbe77f9d593aee7ab4aa770c355": "The object is a generic Bayesian last-layer model under heavy-tailed noise, not speech or audio.",
    "ce8e159a43b0b31cadcf4436a2d360d57b17052d": "The object is cross-modal hashing under noisy data, not a speech or audio task.",
    "df6bf29a93493315b887e10d163580f46f5d14af": "The object is direction-of-arrival estimation for generic sub-arrays; the preserved record does not identify speech or an audio source.",
    "ffd328d7a10eedef07ae882ef510d48a112a06b6": "The object is image-editing watermark robustness, not speech or audio.",
}
queue = json.loads((DATA / "icassp-2026-semantic-review-queue.json").read_text())
papers = {p["paperId"]: p for p in json.loads((DATA / "icassp-2026-papers.json").read_text())["papers"]}
current = {r["paper_id"]: r for r in queue["rows"]}
if any(pid not in current or current[pid].get("decision") != "ambiguous" or current[pid].get("review_state") == "analyst-reviewed" for pid in titles):
    raise SystemExit("batch 061 selection is no longer an unresolved ambiguity set")
rows = []
for pid, reasoning in titles.items():
    paper = papers[pid]
    abstract = paper.get("abstract") or ""
    rows.append({
        "paper_id": pid,
        "title": paper["title"],
        "decision": "unsupported",
        "confidence": "analyst-reviewed-D2" if abstract else "analyst-reviewed-D1",
        "theme_id": None,
        "subtheme_id": None,
        "concept_id": None,
        "semantic_reasoning": reasoning,
        "evidence_excerpt": abstract[:1200] if abstract else paper["title"],
        "source_location": paper.get("url"),
        "source_sha256": hashlib.sha256(abstract.encode()).hexdigest(),
        "evidence_depth": "D2" if abstract else "D1",
        "review_state": "analyst-reviewed",
        "claim_boundary": "ICASSP discovery metadata; rejection resolves speech-taxonomy membership only and does not characterize scientific quality.",
    })
payload = {"schema_version": 1, "batch_id": "icassp-2026-semantic-batch-061", "status": "analyst-reviewed-non-speech-boundary-batch", "claim_boundary": "These records are explicit unsupported decisions based on preserved title/abstract evidence; they remain in the full ICASSP denominator.", "reviewed_count": len(rows), "rows": rows}
OUT.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
print(json.dumps({"batch_id": payload["batch_id"], "reviewed_count": len(rows), "D1": sum(r["evidence_depth"] == "D1" for r in rows), "D2": sum(r["evidence_depth"] == "D2" for r in rows)}))
