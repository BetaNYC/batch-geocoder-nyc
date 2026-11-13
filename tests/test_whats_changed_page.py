#!/usr/bin/env python3
"""Checks for the "What's changed" page and the links to it. Standard library only.

The page is public/whats-changed.html, built from WHATS-CHANGED.md by
scripts/whats_changed.py (a copy of BetaNYC's shared renderer; never edit it
here). Vite copies public/ into the site as is. This catches the page losing
its accessible structure and a page losing its footer link.

Run: python3 tests/test_whats_changed_page.py   (exit 0 passes, 1 fails)
"""
from __future__ import annotations

import json
import subprocess
import sys
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PAGE = ROOT / "public" / "whats-changed.html"
# Every page of the site: the app (its footer component) and the street view page.
LINKERS = [ROOT / "src" / "components" / "Footer.svelte", ROOT / "public" / "streetview.html"]


class Outline(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.tags: dict[str, int] = {}
        self.h1_text: list[str] = []
        self.in_h1 = False
        self.in_legend = False
        self.legend = ""
        self.attrs_seen: list[tuple[str, dict[str, str | None]]] = []

    def handle_starttag(self, tag, attrs):
        self.tags[tag] = self.tags.get(tag, 0) + 1
        self.attrs_seen.append((tag, dict(attrs)))
        self.in_h1 = tag == "h1" or self.in_h1
        self.in_legend = tag == "legend" or self.in_legend

    def handle_endtag(self, tag):
        if tag == "h1":
            self.in_h1 = False
        if tag == "legend":
            self.in_legend = False

    def handle_data(self, data):
        if self.in_h1:
            self.h1_text.append(data)
        if self.in_legend:
            self.legend += data


def main() -> int:
    failures: list[str] = []
    o = Outline()
    o.feed(PAGE.read_text(encoding="utf-8"))

    def need(ok: bool, what: str) -> None:
        if not ok:
            failures.append(what)

    need(o.tags.get("h1") == 1, "exactly one <h1>")
    need("".join(o.h1_text).strip() == "What's changed", "the <h1> reads What's changed")
    for tag in ("header", "nav", "main", "footer", "fieldset"):
        need(o.tags.get(tag, 0) >= 1, f"a <{tag}>")
    # Counts come from the parsed file, so Update lines and an `Unreleased:` entry
    # (no date yet) are handled.
    parsed = json.loads(subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "whats_changed.py"), "json", str(ROOT / "WHATS-CHANGED.md")],
        check=True, capture_output=True, text=True).stdout)
    entries = [e for e in parsed["entries"] if e["valid"]]
    articles = o.tags.get("article", 0)
    need(articles == len(entries), f"one <article> per entry ({len(entries)})")
    ids = {a.get("id") for t, a in o.attrs_seen if t == "article"}
    dates = {a.get("datetime") for t, a in o.attrs_seen if t == "time"}
    for e in entries:
        need(e["anchor"] in ids, f"an <article> for {e['anchor']}")
        if not e["unreleased"]:
            need(e["date"] in dates, f"a <time datetime> for {e['anchor']}")
    has_correction = any("Correction" in e["tags"] for e in entries)
    need(("Corrections only" in PAGE.read_text(encoding="utf-8")) == has_correction,
         "the Corrections only box exactly when there is a correction")
    need(o.legend.strip() == "Show changes to", "the filter legend")
    need(
        any(a.get("role") == "status" and a.get("aria-live") == "polite" for _, a in o.attrs_seen),
        "a polite live region",
    )
    need(any(t == "a" and a.get("href") == "#main" for t, a in o.attrs_seen), "a skip link")
    # Relative, so it works at www.geocoder.nyc/ and under any base path.
    need(any(t == "a" and a.get("href") == "./" for t, a in o.attrs_seen), "a relative home link")
    for f in LINKERS:
        need('href="whats-changed.html"' in f.read_text(encoding="utf-8"), f"footer link in {f.name}")

    for f in failures:
        print(f"FAIL: missing {f}")
    print(f"whats-changed page: {len(failures)} failure(s), {articles} entries")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
