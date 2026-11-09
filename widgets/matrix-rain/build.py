#!/usr/bin/env python3
"""Regenerate matrix-rain.txt (the data: URL OBS actually loads) from matrix-rain.html.

Run this after editing matrix-rain.html, then paste the resulting
matrix-rain.txt into the "Matrix" Browser Source's URL field in OBS
(or embed it directly into the scene collection's JSON).
"""
import pathlib
import urllib.parse

here = pathlib.Path(__file__).parent
html = (here / "matrix-rain.html").read_text(encoding="utf-8")
data_url = "data:text/html;charset=utf-8," + urllib.parse.quote(html)
(here / "matrix-rain.txt").write_text(data_url, encoding="utf-8")
print(f"wrote {len(data_url)} chars to matrix-rain.txt")
