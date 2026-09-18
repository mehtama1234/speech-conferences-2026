#!/usr/bin/env python3
"""Run a bounded syntax check for the linked 3D-Speaker toolkit."""
import json, subprocess, sys, tempfile
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = "https://github.com/modelscope/3D-Speaker.git"
record = {
    "artifact": "modelscope/3D-Speaker",
    "paper_id": "ai25_interspeech",
    "source_url": REPO,
    "checked_at_utc": datetime.now(timezone.utc).isoformat(),
    "execution_scope": "repository clone plus Python syntax compilation; no dependency installation, dataset/model download, checkpoint loading, inference, or scientific reproduction",
    "status": "not-attempted",
    "command": "python -m compileall -q <repository>",
    "returncode": None,
    "boundary": "A syntax pass establishes only that the captured toolkit compiles under the local interpreter; the paper-aligned path still requires external models, datasets, dependencies, and a defined evaluation protocol.",
}
with tempfile.TemporaryDirectory(prefix="speech-3dspeaker-check-") as root:
    clone = Path(root) / "repo"
    cloned = subprocess.run(["git", "clone", "--depth", "1", REPO, str(clone)], capture_output=True, text=True, timeout=120)
    record["clone_returncode"] = cloned.returncode
    record["clone_stderr"] = cloned.stderr[-2000:]
    if cloned.returncode != 0:
        record["status"] = "clone-failed"
    else:
        record["commit"] = subprocess.run(["git", "rev-parse", "HEAD"], cwd=clone, capture_output=True, text=True, timeout=10, check=True).stdout.strip()
        checked = subprocess.run([sys.executable, "-m", "compileall", "-q", str(clone)], capture_output=True, text=True, timeout=120)
        record["returncode"] = checked.returncode
        record["stdout"] = checked.stdout[-2000:]
        record["stderr"] = checked.stderr[-2000:]
        record["status"] = "syntax-pass" if checked.returncode == 0 else "syntax-failed"
out = HERE / "data/speech-artifact-execution-attempts.json"
payload = json.loads(out.read_text()) if out.exists() else {"schema_version": 1, "attempts": []}
payload.setdefault("attempts", [])
payload["attempts"] = [row for row in payload["attempts"] if row.get("artifact") != record["artifact"]] + [record]
out.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
print(json.dumps({"artifact": record["artifact"], "status": record["status"], "commit": record.get("commit"), "output": str(out)}))
