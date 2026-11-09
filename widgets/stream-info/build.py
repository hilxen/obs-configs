#!/usr/bin/env python3
"""Regenerate stream-info.txt (the data: URL OBS actually loads) from stream-info.html.

Run this after editing stream-info.html. Then paste the resulting
stream-info.txt into the "Stream Info" Browser Source's URL field in OBS
(or embed it directly into the scene collection's JSON).
"""
import pathlib
import urllib.parse

here = pathlib.Path(__file__).parent
html = (here / "stream-info.html").read_text(encoding="utf-8")
data_url = "data:text/html;charset=utf-8," + urllib.parse.quote(html)
(here / "stream-info.txt").write_text(data_url, encoding="utf-8")
print(f"wrote {len(data_url)} chars to stream-info.txt")
