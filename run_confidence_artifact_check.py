"""Run a bounded syntax check for the ConfidenceIntervals artifact and append the result."""
import json
import shutil
import subprocess
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
URL = "https://github.com/luferrer/ConfidenceIntervals.git"
result = {"artifact": "luferrer/ConfidenceIntervals", "paper_ids": ["dumpala25_interspeech", "deng25b_interspeech"], "source_url": URL, "checked_at_utc": datetime.now(timezone.utc).isoformat(), "execution_scope": "repository clone plus Python syntax compilation; no dependency installation, dataset download, checkpoint loading, training, inference, or scientific reproduction", "status": "not-attempted", "command": "python -m compileall -q <repository>", "returncode": None, "stdout": "", "stderr": "", "boundary": "A syntax pass establishes only that the captured checkout compiles under the local interpreter; it does not establish the paper's data path, statistical experiment, model behavior, or reported result."}
root = Path(tempfile.mkdtemp(prefix="speech-confidence-check-"))
try:
    clone = root / "repo"
    cloned = subprocess.run(["git", "clone", "--depth", "1", URL, str(clone)], capture_output=True, text=True, timeout=60)
    result["clone_returncode"] = cloned.returncode
    result["clone_stderr"] = cloned.stderr[-2000:]
    if cloned.returncode != 0:
        result["status"] = "clone-failed"
    else:
        rev = subprocess.run(["git", "rev-parse", "HEAD"], cwd=clone, capture_output=True, text=True, timeout=10, check=True)
        result["commit"] = rev.stdout.strip()
        checked = subprocess.run([sys.executable, "-m", "compileall", "-q", "."], cwd=clone, capture_output=True, text=True, timeout=60)
        result["returncode"] = checked.returncode
        result["stdout"] = checked.stdout[-2000:]
        result["stderr"] = checked.stderr[-2000:]
        result["status"] = "syntax-pass" if checked.returncode == 0 else "syntax-failed"
except Exception as exc:
    result["status"] = "check-error"
    result["error"] = f"{type(exc).__name__}: {exc}"
finally:
    shutil.rmtree(root, ignore_errors=True)
path = HERE / "data/speech-artifact-execution-attempts.json"
data = json.loads(path.read_text()) if path.exists() else {"schema_version": 1, "attempts": []}
data.setdefault("attempts", []).append(result)
path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
print(json.dumps({"artifact": result["artifact"], "status": result["status"], "commit": result.get("commit"), "output": str(path)}))
