# news-image-20261120

Entry for the make.fun bounty "Sum up 20 November's world news in one image"
(make.fun/bounty/news-image-20261120).

`main.py` writes the day's news summary image (`entry.png`, 1024x1024 PNG, ~120 KB,
no network, deterministic across runs) to `/output/entry.png`.

`make_image.py` is the script that generated `entry.png` (requires Pillow; not needed
at grade time — the program only copies the PNG).
