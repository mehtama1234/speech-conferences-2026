"""
Ingest ICASSP 2026 paper list from Semantic Scholar (the only source that has it
right now — DBLP/OpenAlex haven't indexed it; IEEE Xplore gates it).

We get titles + DOIs for all ~3,864 papers, plus whatever abstracts/arXiv/PDF
links S2 happens to have (~18% abstracts). Titles are the reliable field; the
theme mining runs off those. Pages through the bulk endpoint with the
continuation token, sleeping between calls to respect the S2 rate limit (429).
"""
import json, os, time, urllib.request, urllib.parse

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "icassp-2026-papers.json")
BASE = "https://api.semanticscholar.org/graph/v1/paper/search/bulk"
FIELDS = "title,abstract,externalIds,openAccessPdf,url"

def fetch(token=None):
    params = {"venue": "ICASSP", "year": "2026", "fields": FIELDS}
    if token:
        params["token"] = token
    url = BASE + "?" + urllib.parse.urlencode(params)
    for attempt in range(6):
        try:
            with urllib.request.urlopen(url, timeout=60) as r:
                return json.loads(r.read())
        except Exception as e:
            wait = 5 * (attempt + 1)
            print(f"  retry {attempt+1} after {wait}s ({str(e)[:60]})", flush=True)
            time.sleep(wait)
    raise RuntimeError("failed after retries")

papers, token, page = [], None, 0
while True:
    d = fetch(token)
    batch = d.get("data") or []
    for p in batch:
        ext = p.get("externalIds") or {}
        papers.append({
            "paperId": p.get("paperId"),
            "title": (p.get("title") or "").strip(),
            "doi": ext.get("DOI"),
            "arxiv": ext.get("ArXiv"),
            "abstract": p.get("abstract"),
            "pdf": (p.get("openAccessPdf") or {}).get("url") or None,
            "url": p.get("url"),
        })
    page += 1
    print(f"page {page}: +{len(batch)}  (total so far {len(papers)} / {d.get('total')})", flush=True)
    token = d.get("token")
    if not token or not batch:
        break
    time.sleep(3)

# de-dup by title (S2 occasionally repeats)
seen, uniq = set(), []
for p in papers:
    k = p["title"].lower()
    if k and k not in seen:
        seen.add(k); uniq.append(p)

with_abs = sum(1 for p in uniq if p["abstract"])
with_arx = sum(1 for p in uniq if p["arxiv"])
json.dump({"venue": "ICASSP 2026", "location": "Barcelona", "dates": "4-8 May 2026",
           "n_papers": len(uniq), "with_abstract": with_abs, "with_arxiv": with_arx,
           "papers": uniq}, open(OUT, "w"), indent=1)
print(f"\nwrote {len(uniq)} unique papers -> {OUT}")
print(f"  abstracts: {with_abs} ({with_abs*100//max(len(uniq),1)}%)  arxiv: {with_arx} ({with_arx*100//max(len(uniq),1)}%)")
