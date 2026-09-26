"""Build the public site and the friends' Claude copy from the app source.

Source:  ../bramble-camp-log.html (your private Claude version)
Outputs: index.html (GitHub Pages) and ../bramble-camp-log-friends.html (shareable Claude copy;
         republish it to https://claude.ai/artifact/Towu58453iQk6pDE18U6Qk after changes)

Usage:  python build.py
"""
import shutil
from pathlib import Path

here = Path(__file__).parent
src_path = here.parent / "bramble-camp-log.html"
src = src_path.read_text(encoding="utf-8")
shutil.copyfile(src_path, here.parent / "bramble-camp-log-friends.html")
i = src.index('<div class="scene-wrap"')
head, body = src[:i].rstrip(), src[i:].rstrip()
page = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="description" content="Bramble Camp Log: rate the campsites you've visited, note amenities and gear, and keep a watch list of hard-to-get sites.">
<meta name="theme-color" content="#2E5B39">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-title" content="Bramble">
<meta name="apple-mobile-web-app-status-bar-style" content="default">
<meta property="og:title" content="Bramble Camp Log">
<meta property="og:description" content="Track and rate your campsites with Bramble the bear.">
<meta property="og:image" content="icon-512.png">
<link rel="manifest" href="manifest.json">
<link rel="icon" type="image/png" sizes="32x32" href="favicon-32.png">
<link rel="apple-touch-icon" href="apple-touch-icon.png">
<style>
:root{{color-scheme:light;padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}}
body{{margin:0}}
img{{max-width:100%}}
</style>
{head}
</head>
<body>
{body}
</body>
</html>
'''
(here / "index.html").write_text(page, encoding="utf-8", newline="\n")
print("index.html built,", len(page), "bytes")
