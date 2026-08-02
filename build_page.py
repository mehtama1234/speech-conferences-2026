import json, os, html
HERE = os.path.dirname(os.path.abspath(__file__))
T = json.load(open(os.path.join(HERE, "data", "icassp-2026-themes.json")))
def esc(s): return html.escape(str(s))

def bars(items, key, nkey, color, maxn=None):
    mx = maxn or max(i["n"] for i in items)
    out = ""
    for i in items:
        pct = i["n"]/mx*100
        out += (f"<div class='bar'><span class='bl'>{esc(i[key])}</span>"
                f"<span class='bt'><span class='bf' style='width:{pct:.1f}%;background:{color}'></span></span>"
                f"<span class='bv'>{i['n']}<span class='bp'> · {i['pct']}%</span></span></div>")
    return out

def domaincards():
    out = ""
    for d in T["domains"]:
        speech = d["domain"].startswith("Speech") or d["domain"].startswith("Audio")
        ex = "".join(f"<li>{esc(t)}</li>" for t in d["examples"][:4])
        out += (f"<div class='dcard{' hot' if speech else ''}'>"
                f"<div class='dh'><span class='dn'>{esc(d['domain'])}</span>"
                f"<span class='dc'>{d['n']} <span class='dp'>{d['pct']}%</span></span></div>"
                f"<ul class='dex'>{ex}</ul></div>")
    return out

def subtheme_examples():
    out = ""
    for s in T["speech_subthemes"]:
        ex = "".join(f"<li>{esc(t)}</li>" for t in s["examples"][:3])
        out += (f"<div class='scard'><div class='sh'><span class='sn'>{esc(s['theme'])}</span>"
                f"<span class='sc'>{s['n']}</span></div><ul class='sex'>{ex}</ul></div>")
    return out

P = f"""<meta charset="utf-8">
<title>ICASSP 2026 · the speech landscape</title>
<style>
:root{{--bg:#0E1420;--bg2:#141D2C;--panel:#18212F;--ink:#EAEEF4;--soft:#B4BFD0;--dim:#8493A8;--faint:#5A6577;
--line:rgba(150,170,205,.14);--accent:#4FA8B8;--amber:#E3A63A;--rose:#E0748A;--viol:#9B8CE0;--serif:"Iowan Old Style",Palatino,Georgia,serif;
--sans:-apple-system,system-ui,"Segoe UI",Roboto,Arial,sans-serif;--mono:ui-monospace,"SF Mono",Menlo,Consolas,monospace;}}
*{{box-sizing:border-box}}body{{margin:0;background:var(--bg);color:var(--ink);font-family:var(--sans);line-height:1.7;font-size:17px}}
.wrap{{max-width:900px;margin:0 auto;padding:0 24px}}
p{{color:var(--soft);margin:0 0 16px}}b{{color:var(--ink)}}em{{color:#fff;font-style:italic}}
.mono{{font-family:var(--mono)}}
.kick{{font-family:var(--mono);font-size:11.5px;letter-spacing:.22em;text-transform:uppercase;color:var(--accent)}}
h1{{font-family:var(--serif);font-size:clamp(32px,6vw,52px);line-height:1.05;margin:14px 0 0;color:#fff;letter-spacing:-.02em}}
h2{{font-family:var(--serif);font-size:27px;margin:0 0 6px;color:#fff}}
.dek{{font-size:19px;color:var(--soft);margin-top:18px;max-width:64ch}}
section{{padding:42px 0;border-top:1px solid var(--line)}}
.eye{{font-family:var(--mono);font-size:11px;letter-spacing:.16em;text-transform:uppercase;color:var(--dim);margin-bottom:12px}}
.stat{{display:flex;gap:26px;flex-wrap:wrap;margin:22px 0 6px}}
.stat .sn{{font-family:var(--serif);font-size:34px;color:#fff;line-height:1}}.stat .sl{{font-family:var(--mono);font-size:11px;color:var(--dim);margin-top:6px}}
.note{{background:var(--bg2);border:1px solid var(--line);border-left:3px solid var(--amber);border-radius:12px;padding:14px 18px;margin:18px 0}}
.note .nt{{font-family:var(--mono);font-size:11px;letter-spacing:.1em;text-transform:uppercase;color:var(--amber);margin-bottom:6px}}.note p{{margin:0;font-size:14.5px;color:var(--soft)}}
.why{{background:var(--bg2);border:1px solid var(--line);border-left:3px solid var(--accent);border-radius:12px;padding:16px 20px;margin:18px 0}}
.why h3{{margin:0 0 6px;font-size:12.5px;font-family:var(--mono);letter-spacing:.05em;text-transform:uppercase;color:var(--accent)}}.why p{{margin:0;font-size:15px;color:var(--soft)}}
.bar{{display:flex;align-items:center;gap:12px;margin:7px 0;font-family:var(--mono);font-size:12.5px}}
.bar .bl{{width:210px;color:var(--soft);text-align:right;flex:0 0 auto}}
.bar .bt{{flex:1;height:18px;background:rgba(150,170,205,.06);border-radius:5px;overflow:hidden}}
.bar .bf{{display:block;height:100%}}
.bar .bv{{width:78px;color:var(--ink)}}.bar .bp{{color:var(--faint)}}
@media(max-width:640px){{.bar .bl{{width:120px;font-size:11px}}}}
.dcard{{background:var(--bg2);border:1px solid var(--line);border-radius:12px;padding:14px 16px}}
.dcard.hot{{border-color:rgba(79,168,184,.4);background:rgba(79,168,184,.06)}}
.dgrid{{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-top:14px}}
@media(max-width:640px){{.dgrid{{grid-template-columns:1fr}}}}
.dh{{display:flex;justify-content:space-between;align-items:baseline;margin-bottom:6px}}
.dn{{font-family:var(--serif);font-size:17px;color:#fff}}.dc{{font-family:var(--mono);font-size:13px;color:var(--accent)}}.dp{{color:var(--faint);font-size:11px}}
.dex,.sex{{margin:0;padding-left:16px;list-style:none}}
.dex li,.sex li{{font-size:12.5px;color:var(--dim);margin:3px 0;padding-left:10px;text-indent:-10px;line-height:1.4}}
.dex li:before,.sex li:before{{content:'· ';color:var(--faint)}}
.scard{{background:var(--bg2);border:1px solid var(--line);border-radius:11px;padding:12px 14px}}
.sgrid{{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-top:14px}}
@media(max-width:640px){{.sgrid{{grid-template-columns:1fr}}}}
.sh{{display:flex;justify-content:space-between;align-items:baseline;margin-bottom:5px}}
.sn{{font-family:var(--mono);font-size:13px;font-weight:600;color:#fff}}.sc{{font-family:var(--mono);font-size:13px;color:var(--accent)}}
.aha{{font-family:var(--serif);font-size:21px;line-height:1.4;color:#fff;border-left:3px solid var(--accent);padding-left:18px;margin:8px 0}}
.src{{font-family:var(--mono);font-size:12px;color:var(--faint);margin-top:28px;padding-top:16px;border-top:1px solid var(--line)}}.src a{{color:var(--accent);text-decoration:none}}
</style>
<div class="wrap">
<header style="padding:60px 0 8px">
  <div class="kick">Speech conferences 2026 · a work in progress</div>
  <h1>ICASSP 2026, from the titles up.</h1>
  <p class="dek">A first map of <b>{T['n_papers']:,} papers</b> from ICASSP 2026 ({esc(T['location'])}, {esc(T['dates'])}) — the flagship signal-processing conference. Built from titles alone, because that is what's public right now, and honest about what that can and can't tell us.</p>
  <div class="stat">
    <div><div class="sn">{T['n_papers']:,}</div><div class="sl">papers</div></div>
    <div><div class="sn">{T['n_speech_audio']:,}</div><div class="sl">speech &amp; audio (~{T['n_speech_audio']*100//T['n_papers']}%)</div></div>
    <div><div class="sn">{len(T['domains'])}</div><div class="sl">primary domains</div></div>
    <div><div class="sn">{len(T['speech_subthemes'])}</div><div class="sl">speech sub-themes</div></div>
  </div>
  <div class="note"><div class="nt">read this first — what this is and isn't</div>
  <p>ICASSP's full name is "Acoustics, <b>Speech</b>, and Signal Processing" — it is a <em>broad</em> conference, and speech is one slice of it. Right now only titles + DOIs are public for all papers (abstracts exist for just {T['with_abstract']*100//T['n_papers']}% via Semantic Scholar; IEEE gates the rest). So this is a <b>titles-only theme map</b> — a reliable read of <em>what topics are present and how much</em>, but not the per-paper problem/approach/contribution analysis that needs abstracts. That deeper pass waits for open indexing. Interspeech 2026 (Sydney, Sept 28–Oct 1) isn't published yet and joins later.</p></div>
  <div class="why"><h3>Plain course spine</h3><p>Read <a href="course.html">Speech And Signal Processing From First Principles</a> for the everyday-word version of the big ideas: signals, speech, time, topology, learned representations, trust, evaluation, and why this matters outside speech.</p></div>
</header>

<section>
  <div class="eye">The whole conference · one paper, one primary domain</div>
  <h2>Speech is ~{T['n_speech_audio']*100//T['n_papers']}% of a much bigger signal-processing world</h2>
  <p>Each paper is placed in its single best-matching domain by keyword. The surprise for anyone who thinks of ICASSP as a speech venue: <b>image &amp; video is larger than speech</b>, and both sit inside a vast general signal-processing tail. Speech and audio together are the highlighted slices:</p>
  <div class="dgrid">{domaincards()}</div>
  <div class="why"><h3>Why "Other" is so large, honestly</h3><p>The single biggest bucket is a catch-all — ICASSP has a long tail of signal-processing subfields (estimation, optimization, arrays, statistical SP, specialized applications) that no small keyword set cleanly names from a title. That's a real property of the venue, not a bug in the map; a deeper pass with abstracts would split it further.</p></div>
</section>

<section>
  <div class="eye">Zoom in · the speech &amp; audio papers</div>
  <h2>What's hot in speech at ICASSP 2026</h2>
  <p>Within the {T['n_speech_audio']} speech &amp; audio papers, the research sub-themes — a title can carry more than one:</p>
  <div style="margin-top:12px">{bars(T['speech_subthemes'], 'theme', 'n', '#4FA8B8')}</div>
  <p style="margin-top:22px"><b>A few real titles per theme</b>, so you can see what each bucket actually contains:</p>
  <div class="sgrid">{subtheme_examples()}</div>
</section>

<section>
  <div class="eye">Cutting across · the methods in fashion</div>
  <h2>How the speech work is being done</h2>
  <p>Independent of topic, these method-signatures show up across the speech papers — the current toolkit:</p>
  <div style="margin-top:12px">{bars(T['speech_methods'], 'method', 'n', '#9B8CE0', maxn=max(m['n'] for m in T['speech_methods']))}</div>
  <p class="mini" style="font-family:var(--mono);font-size:12px;color:var(--faint);margin-top:12px">Counts are of the {T['n_speech_audio']} speech/audio papers whose title carries each signature. Efficiency/on-device and adversarial/robustness lead — the field is optimizing and hardening, alongside the newer diffusion- and LLM-based waves.</p>
</section>

<section>
  <div class="eye">The one-line read</div>
  <p class="aha">ICASSP 2026 is first a signal-processing conference and only second a speech one — but within its speech slice, the story is recognition and enhancement as the steady core, with self-supervised foundations, anti-spoofing, and a fresh diffusion/LLM wave rising on top.</p>
  <p class="src">Data: Semantic Scholar (the only source with ICASSP 2026 right now; DBLP/OpenAlex not yet indexed, IEEE Xplore gated). Themes assigned by a transparent, deterministic keyword taxonomy over titles — code in <span class="mono">ingest_icassp.py</span> + <span class="mono">mine_themes.py</span>. Titles-only pilot; a full per-paper analysis + Interspeech 2026 follow when open proceedings publish.</p>
</section>
</div>
"""
open(os.path.join(HERE, "site", "index.html"), "w", encoding="utf-8").write(P)
open(os.path.join(HERE, "index.html"), "w", encoding="utf-8").write(P)
print("wrote index.html + site/index.html ·", len(P)//1024, "KB · FFFD:", P.count("�"))
