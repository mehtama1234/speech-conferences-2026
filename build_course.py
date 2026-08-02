#!/usr/bin/env python3
import html
from pathlib import Path

from course_spine import COURSE_SUBTITLE, COURSE_TITLE, INTRO, READING_PATH, SECTIONS

ROOT = Path(__file__).resolve().parent
SITE = ROOT / "site"


def esc(value):
    return html.escape(str(value or ""), quote=True)


def render_intro():
    return "".join(f"<p>{esc(p)}</p>" for p in INTRO)


def render_path():
    return "".join(f'<a href="{esc(href)}">{esc(label)}</a>' for href, label in READING_PATH)


def render_nav():
    return "".join(
        f'<a href="#s{idx}">{idx}. {esc(section["kicker"])}</a>'
        for idx, section in enumerate(SECTIONS, 1)
    )


def render_sections():
    parts = []
    for idx, section in enumerate(SECTIONS, 1):
        body = "".join(f"<p>{esc(p)}</p>" for p in section["body"])
        apps = "".join(f"<li>{esc(app)}</li>" for app in section["applications"])
        parts.append(
            f"""
<section id="s{idx}" class="part">
  <div class="kicker">{esc(section["kicker"])}</div>
  <h2>{idx}. {esc(section["title"])}</h2>
  <p class="summary">{esc(section["summary"])}</p>
  <div class="essay">{body}</div>
  <div class="uses"><h3>Where this shows up</h3><ul>{apps}</ul></div>
</section>"""
        )
    return "\n".join(parts)


PAGE = """<meta charset="utf-8">
<title>__TITLE__</title>
<style>
:root{--bg:#0E1420;--bg2:#141D2C;--panel:#18212F;--ink:#EAEEF4;--soft:#B4BFD0;--dim:#8493A8;--faint:#5A6577;--line:rgba(150,170,205,.14);--accent:#4FA8B8;--amber:#E3A63A;--serif:"Iowan Old Style",Palatino,Georgia,serif;--sans:-apple-system,system-ui,"Segoe UI",Roboto,Arial,sans-serif;--mono:ui-monospace,"SF Mono",Menlo,Consolas,monospace}
*{box-sizing:border-box}html{scroll-behavior:smooth}body{margin:0;background:var(--bg);color:var(--ink);font-family:var(--sans);line-height:1.7;font-size:17px}.wrap{max-width:900px;margin:0 auto;padding:0 24px}p{color:var(--soft);margin:0 0 16px}a{color:var(--accent);text-decoration:none;border-bottom:1px solid rgba(79,168,184,.5)}a:hover{border-color:var(--amber)}.kick,.kicker{font-family:var(--mono);font-size:11.5px;letter-spacing:.22em;text-transform:uppercase;color:var(--accent)}h1{font-family:var(--serif);font-size:clamp(34px,6vw,58px);line-height:1.05;margin:14px 0 0;color:#fff;letter-spacing:-.02em}h2{font-family:var(--serif);font-size:clamp(27px,4vw,38px);line-height:1.12;margin:7px 0 8px;color:#fff}.dek{font-size:19px;color:var(--soft);margin-top:18px;max-width:68ch}
nav{position:sticky;top:0;z-index:2;background:rgba(14,20,32,.96);border-bottom:1px solid var(--line)}.navwrap{display:flex;gap:8px;overflow:auto;padding-top:10px;padding-bottom:10px}nav a{white-space:nowrap;background:var(--bg2);border:1px solid var(--line);border-radius:999px;padding:5px 9px;font-family:var(--mono);font-size:11px}
.intro,.path,.part{background:var(--bg2);border:1px solid var(--line);border-radius:12px}.intro{border-left:3px solid var(--amber);padding:18px 20px;margin:26px 0 18px}.intro p:last-child{margin-bottom:0}.path{padding:15px 18px;margin:18px 0 24px}.path b{display:block;font-family:var(--mono);font-size:11px;letter-spacing:.15em;text-transform:uppercase;color:var(--dim);margin-bottom:8px}.path a{display:inline-block;margin:4px 12px 4px 0}.part{border-left:3px solid var(--accent);padding:23px 24px;margin:18px 0}.summary{color:var(--dim);font-size:18px;margin-bottom:16px}.essay p{margin-bottom:13px}.uses{border-top:1px solid var(--line);padding-top:13px;margin-top:15px}.uses h3{font-family:var(--mono);font-size:11px;letter-spacing:.12em;text-transform:uppercase;color:var(--dim);margin:0 0 8px}.uses ul{margin:0;padding-left:20px}.uses li{color:var(--soft);margin:5px 0}footer{font-family:var(--mono);font-size:12px;color:var(--faint);padding:30px 0 64px;border-top:1px solid var(--line);margin-top:30px}@media(max-width:640px){.wrap{padding:0 18px}.part{padding:20px}}
</style>
<header class="wrap" style="padding:60px 24px 8px">
  <div class="kick">Speech course spine</div>
  <h1>__TITLE__</h1>
  <p class="dek">__SUBTITLE__</p>
</header>
<nav><div class="wrap navwrap">__NAV__</div></nav>
<main class="wrap">
  <div class="intro">__INTRO__</div>
  <div class="path"><b>Read next</b>__PATH__</div>
  __SECTIONS__
  <footer>Part of the speech conferences 2026 title map. Continue to <a href="index.html">ICASSP title map</a>.</footer>
</main>
"""


def main():
    page = (
        PAGE.replace("__TITLE__", esc(COURSE_TITLE))
        .replace("__SUBTITLE__", esc(COURSE_SUBTITLE))
        .replace("__NAV__", render_nav())
        .replace("__INTRO__", render_intro())
        .replace("__PATH__", render_path())
        .replace("__SECTIONS__", render_sections())
    )
    SITE.mkdir(exist_ok=True)
    (SITE / "course.html").write_text(page, encoding="utf-8")
    (ROOT / "course.html").write_text(page, encoding="utf-8")
    print(f"wrote course.html + site/course.html ({len(page) // 1024} KB, {len(SECTIONS)} sections)")


if __name__ == "__main__":
    main()
