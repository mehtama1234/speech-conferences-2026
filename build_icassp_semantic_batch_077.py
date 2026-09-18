"""Targeted adjudication of clear non-speech boundary cases."""
import hashlib, json
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = HERE / "data"
OUT = DATA / "icassp-2026-semantic-reviewed-batch-077.json"
if OUT.exists():
    p = json.loads(OUT.read_text())
    print(json.dumps({"batch_id": p["batch_id"], "status": "preserved-input", "reviewed_count": p["reviewed_count"]}))
    raise SystemExit(0)

IDS = {
    "049ff810bb300dcfba5035adb98077bbfd71519b": "Environmental sound deepfake detection evaluates synthetic environmental audio, not spoken speech.",
    "4540bba9a09c37e860f898cc4bdff4dd2a02cf90": "The ESDD task is environmental sound deepfake detection; the title does not identify spoken speech.",
    "36994b46f0cb07823396c0865a571dffabd38daf": "EEG auditory-attention decoding studies neural attention signals rather than a speech-processing task.",
    "88ff1b2786b0a850fc9cb60304ed5abe2fadee2c": "The task decodes auditory attention from EEG; speech is not the object of recognition or generation.",
    "a9d246ebcbd255ab85380382e349a3834af2ab59": "EEG-based auditory attention is a neural decoding problem, not a spoken-speech task.",
    "dbd2cb763a178284a158fe7d641739b24640ff9d": "EEG auditory attention decoding is outside the speech taxonomy because the measured object is neural attention.",
    "edd19dc637d1ca376b93fe6739ed7f766c987171": "The task is auditory-attention decoding from brain signals, not analysis of spoken speech.",
    "f2d0d421d6c205921a6af720c7ac6f94589dcae6": "Neural decoding of auditory attention does not establish a spoken-speech research problem.",
    "68d9605c75c90e3f84aee0c673804722cd1041d6": "Room-acoustic characterization is an acoustics problem; the title does not identify speech as the task object.",
    "7af55d4eda499f32949e852ea97ca835dac05794": "Ultrasonic or room-acoustic sensing is adjacent audio research, not a spoken-speech task.",
    "c6bd1b6d6dae47eb16d4ff94fffd36c4d81db778": "The paper studies room acoustics or ultrasonic sensing without a speech-specific recognition, production, or health task.",
    "02f118077baae91a89239c62f0c353bf0823630e": "Sign-language recognition uses visual manual language rather than spoken speech.",
    "44e2bb3e3fcdbcad8165a08820c97837bf80819e": "The task is visual sign-language understanding, not spoken-language processing.",
    "5f0b592deb269f3b54baa0488dac3c83a8bda984": "Sign-language video translation is a visual language task and does not belong in a spoken-speech taxonomy.",
    "707d046e8cd00a5887a6e513a25b439c6ce88349": "The title identifies sign-language recognition, whose input and output are visual/manual rather than spoken.",
    "928a30192cb47fb96453a5d1ded5e9951106e255": "Visual sign-language processing is outside the spoken-speech corpus boundary.",
    "b15ad29a89182126b25d19cfcacf8574ea876afa": "The paper concerns sign language rather than spoken speech; no speech task is established.",
    "cc0216913168a73e899dbbf946148b414548f0d7": "Sign-language understanding is a visual/manual-language problem, not a spoken-speech problem.",
    "eec3206aa259cb5c66598c06f27492a2db8af772": "The task is sign-language video or gesture understanding, outside the spoken-speech scope.",
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
payload = {"schema_version": 1, "batch_id": "icassp-2026-semantic-batch-077", "status": "analyst-reviewed-targeted-non-speech-boundary-batch", "claim_boundary": "These targeted decisions exclude explicit environmental-audio, neural-auditory, acoustics, and visual sign-language tasks from the spoken-speech taxonomy using preserved title/abstract evidence.", "reviewed_count": len(rows), "rows": rows}
OUT.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
print(json.dumps({"batch_id": payload["batch_id"], "reviewed_count": len(rows), "unsupported": len(rows)}))
