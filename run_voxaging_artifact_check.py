#!/usr/bin/env python3
"""Run a bounded syntax check for the VoxAging repository and append its record."""
import json, shutil, subprocess, sys, tempfile
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = "https://github.com/aizhiqi-work/voxaging.git"
root = Path(tempfile.mkdtemp(prefix="speech-voxaging-check-"))
result = {
    "artifact": "aizhiqi-work/voxaging",
    "paper_id": "ai25_interspeech",
    "source_url": REPO,
    "checked_at_utc": datetime.now(timezone.utc).isoformat(),
    "execution_scope": "repository clone plus Python syntax compilation; no dependency installation, dataset download, checkpoint loading, training, inference, or scientific reproduction",
    "status": "not-attempted", "command": "python -m compileall -q <repository>",
    "returncode": None, "stdout": "", "stderr": "",
    "boundary": "A syntax pass establishes only that the captured checkout compiles under the local interpreter; it does not establish runnable dependencies, dataset/model access, inference behavior, or the paper's reported result.",
}
try:
    clone = root / "repo"
    fetched = subprocess.run(["git", "clone", "--depth", "1", REPO, str(clone)], capture_output=True, text=True, timeout=90)
    result["clone_returncode"] = fetched.returncode
    result["clone_stderr"] = fetched.stderr[-2000:]
    if fetched.returncode:
        result["status"] = "clone-failed"
    else:
        rev = subprocess.run(["git", "rev-parse", "HEAD"], cwd=clone, capture_output=True, text=True, timeout=10, check=True)
        result["commit"] = rev.stdout.strip()
        checked = subprocess.run([sys.executable, "-m", "compileall", "-q", "."], cwd=clone, capture_output=True, text=True, timeout=90)
        result["returncode"] = checked.returncode
        result["stdout"] = checked.stdout[-2000:]
        result["stderr"] = checked.stderr[-2000:]
        result["status"] = "syntax-pass" if checked.returncode == 0 else "syntax-failed"
except Exception as exc:
    result["status"] = "check-error"
    result["error"] = f"{type(exc).__name__}: {exc}"
finally:
    shutil.rmtree(root, ignore_errors=True)

out = HERE / "data/speech-artifact-execution-attempts.json"
payload = json.loads(out.read_text()) if out.exists() else {"schema_version": 1, "attempts": []}
payload.setdefault("attempts", []).append(result)
out.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
print(json.dumps({"artifact": result["artifact"], "status": result["status"], "commit": result.get("commit"), "output": str(out)}))
