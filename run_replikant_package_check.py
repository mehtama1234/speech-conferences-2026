"""Run a bounded packaging and syntax check for the Replikant artifact."""
import json, shutil, subprocess, sys, tempfile
from datetime import datetime, timezone
from pathlib import Path
HERE=Path(__file__).resolve().parent
URL="https://github.com/seblemaguer/replikant.git"
result={"artifact":"seblemaguer/replikant","paper_id":"lemaguer25_interspeech","source_url":URL,"checked_at_utc":datetime.now(timezone.utc).isoformat(),"execution_scope":"repository clone, Python syntax compilation, and dependency-free wheel build; no dependency installation, survey data, listener study, server launch, or scientific reproduction","command":"python -m compileall -q src && python -m pip wheel --no-deps --no-build-isolation . -w /tmp/replikant-wheel","status":"not-attempted","returncode":None,"stdout":"","stderr":"","boundary":"The syntax and package-build checks establish only that the captured source compiles and can be packaged without resolving runtime dependencies; they do not execute a subjective evaluation, launch the web application, access recipes/data, or reproduce the paper's findings."}
root=Path(tempfile.mkdtemp(prefix="speech-replikant-package-"))
try:
 clone=root/"repo"; c=subprocess.run(["git","clone","--depth","1",URL,str(clone)],capture_output=True,text=True,timeout=60); result["clone_returncode"]=c.returncode; result["clone_stderr"]=c.stderr[-2000:]
 if c.returncode:
  result["status"]="clone-failed"
 else:
  result["commit"]=subprocess.run(["git","rev-parse","HEAD"],cwd=clone,capture_output=True,text=True,check=True,timeout=10).stdout.strip()
  syntax=subprocess.run([sys.executable,"-m","compileall","-q","src"],cwd=clone,capture_output=True,text=True,timeout=60)
  build=subprocess.run([sys.executable,"-m","pip","wheel","--no-deps","--no-build-isolation",".","-w",str(root/"wheel")],cwd=clone,capture_output=True,text=True,timeout=90)
  result["returncode"]=build.returncode; result["stdout"]=(syntax.stdout+build.stdout)[-3000:]; result["stderr"]=(syntax.stderr+build.stderr)[-3000:]; result["status"]="package-build-pass" if syntax.returncode==0 and build.returncode==0 else "package-build-failed"; result["syntax_returncode"]=syntax.returncode
except Exception as exc:
 result["status"]="check-error"; result["error"]=f"{type(exc).__name__}: {exc}"
finally: shutil.rmtree(root,ignore_errors=True)
path=HERE/"data/speech-artifact-execution-attempts.json"; data=json.loads(path.read_text()); data.setdefault("attempts",[]).append(result); path.write_text(json.dumps(data,indent=2,ensure_ascii=False)+"\n"); print(json.dumps({"artifact":result["artifact"],"status":result["status"],"commit":result.get("commit"),"output":str(path)}))
