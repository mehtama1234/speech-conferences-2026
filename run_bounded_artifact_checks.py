#!/usr/bin/env python3
"""Run a small, dependency-light artifact check and preserve its boundary."""

from __future__ import annotations

import json
import shutil
import subprocess
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = "https://github.com/idiap/RnV.git"


def main() -> None:
    root = Path(tempfile.mkdtemp(prefix="speech-rnv-check-"))
    result = {
        "artifact": "idiap/RnV",
        "source_url": REPO,
        "checked_at_utc": datetime.now(timezone.utc).isoformat(),
        "execution_scope": "syntax-only compile check; no dependency installation, data download, training, checkpoint loading, or scientific reproduction",
        "status": "not-attempted",
        "command": "python -m compileall -q rnv scripts recipes",
        "returncode": None,
        "stdout": "",
        "stderr": "",
        "boundary": "A successful syntax check establishes only that Python files compile in this checkout; it does not establish runnable dependencies, data availability, model behavior, or the paper's reported result.",
    }
    try:
        clone = root / "RnV"
        cloned = subprocess.run(["git", "clone", "--depth", "1", REPO, str(clone)], capture_output=True, text=True, timeout=60)
        result["clone_returncode"] = cloned.returncode
        result["clone_stderr"] = cloned.stderr[-2000:]
        if cloned.returncode != 0:
            result["status"] = "clone-failed"
        else:
            rev = subprocess.run(["git", "rev-parse", "HEAD"], cwd=clone, capture_output=True, text=True, timeout=10, check=True)
            result["commit"] = rev.stdout.strip()
            checked = subprocess.run([sys.executable, "-m", "compileall", "-q", "rnv", "scripts", "recipes"], cwd=clone, capture_output=True, text=True, timeout=60)
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
    out.write_text(json.dumps({"schema_version": 1, "attempts": [result]}, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({"artifact": result["artifact"], "status": result["status"], "commit": result.get("commit"), "output": str(out)}))


if __name__ == "__main__":
    main()
