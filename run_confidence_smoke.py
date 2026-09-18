"""Run the repository's documented toy bootstrap example and append a bounded result."""
import json
import shutil
import subprocess
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
URL = "https://github.com/luferrer/ConfidenceIntervals.git"
command = "PYTHONPATH=. python -c '<documented toy bootstrap with 40 samples, 4 conditions, 100 draws>'"
result = {"artifact": "luferrer/ConfidenceIntervals", "paper_ids": ["dumpala25_interspeech", "deng25b_interspeech"], "source_url": URL, "checked_at_utc": datetime.now(timezone.utc).isoformat(), "execution_scope": "bounded documented toy-data smoke test; no paper data, model, checkpoint, training, or scientific reproduction", "command": command, "status": "not-attempted", "returncode": None, "stdout": "", "stderr": "", "boundary": "The toy example tests the repository utility on synthetic data only; it does not reproduce either cited speech paper or establish the validity of its reported scientific conclusions."}
root = Path(tempfile.mkdtemp(prefix="speech-confidence-smoke-"))
try:
    clone = root / "repo"
    cloned = subprocess.run(["git", "clone", "--depth", "1", URL, str(clone)], capture_output=True, text=True, timeout=60)
    result["clone_returncode"] = cloned.returncode
    result["clone_stderr"] = cloned.stderr[-2000:]
    if cloned.returncode != 0:
        result["status"] = "clone-failed"
    else:
        result["commit"] = subprocess.run(["git", "rev-parse", "HEAD"], cwd=clone, capture_output=True, text=True, timeout=10, check=True).stdout.strip()
        code = "from confidence_intervals import evaluate_with_conf_int; from confidence_intervals.utils import create_data; from sklearn.metrics import accuracy_score; d,l,c=create_data(40,40,4); v,i=evaluate_with_conf_int(d,accuracy_score,l,c,num_bootstraps=100,alpha=5); assert 0<=v<=1 and len(i)==2 and i[0]<=v<=i[1]; print({'metric':float(v),'interval':tuple(float(x) for x in i)})"
        checked = subprocess.run([sys.executable, "-c", code], cwd=clone, env={**__import__("os").environ, "PYTHONPATH": "."}, capture_output=True, text=True, timeout=30)
        result["returncode"] = checked.returncode
        result["stdout"] = checked.stdout[-2000:]
        result["stderr"] = checked.stderr[-2000:]
        result["status"] = "smoke-pass" if checked.returncode == 0 else "smoke-failed"
except Exception as exc:
    result["status"] = "check-error"
    result["error"] = f"{type(exc).__name__}: {exc}"
finally:
    shutil.rmtree(root, ignore_errors=True)
path = HERE / "data/speech-artifact-execution-attempts.json"
data = json.loads(path.read_text())
data.setdefault("attempts", []).append(result)
path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
print(json.dumps({"artifact": result["artifact"], "status": result["status"], "commit": result.get("commit"), "output": str(path)}))
