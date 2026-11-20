#!/usr/bin/env python3
"""Generate the 20 Nov 2026 world-news summary image (1024x1024 PNG)."""
from PIL import Image, ImageDraw, ImageFont

W = H = 1024
FD = "/data/data/com.termux/files/usr/share/fonts/TTF"
F_SERIF_B = f"{FD}/DejaVuSerif-Bold.ttf"
F_SANS_B = f"{FD}/DejaVuSans-Bold.ttf"
F_SANS = f"{FD}/DejaVuSans.ttf"

BG = (13, 24, 41)
PANEL = (21, 36, 60)
GOLD = (232, 180, 74)
RED = (224, 82, 76)
WHITE = (240, 244, 250)
MUTED = (158, 172, 192)
LINE = (52, 70, 99)

img = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(img)

def font(path, size):
    return ImageFont.truetype(path, size)

def wrap_px(text, f, max_w):
    words = text.split()
    lines, cur = [], ""
    for w_ in words:
        t = (cur + " " + w_).strip()
        if d.textlength(t, font=f) <= max_w:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w_
    if cur:
        lines.append(cur)
    return lines

def draw_wrapped(x, y, text, f, fill, max_w, lh):
    for ln in wrap_px(text, f, max_w):
        d.text((x, y), ln, font=f, fill=fill)
        y += lh
    return y

stories = [
    ("WORLD", "Trump, Putin & Xi sign joint \u201cpeace declaration\u201d at historic Shenzhen summit",
     "First-ever trilateral meeting of the US, Russian and Chinese leaders reaffirms that nuclear war should never be fought; the Russia\u2013Ukraine war is on the table."),
    ("UKRAINE", "Russia hits three Kyiv bridges, 5 killed in major missile attack",
     "Strikes follow Ukraine's hit on the Crimean Bridge; Putin vows a \u201cfar more painful\u201d response."),
    ("EUROPE", "Europe \u201cunited\u201d at Berlin summit, ready for Russia talks",
     "Allies agree a negotiating position to end the Ukraine war; Zelenskyy demands stronger security guarantees."),
    ("UN COURT", "UN court finds Myanmar guilty of Rohingya genocide",
     "Unprecedented ICJ verdict on the 2017 crackdown \u2014 the first genocide finding against a state."),
    ("MARKETS", "Anthropic lists on stock market in landmark AI debut",
     "First purely AI company to go public; shares close up 17%, among the world's most valuable firms."),
    ("UK\u2013EU", "UK and EU approve youth mobility scheme at summit",
     "New deals on food trade and carbon emissions also agreed at Friday's UK\u2013EU meeting."),
    ("CLIMATE", "COP31 in T\u00fcrkiye: Africa demands more climate cash",
     "\u201cMake Polluters Pay\u201d \u2014 developing nations press rich countries to fund adaptation."),
    ("MIDEAST", "Houthi missile strikes Riyadh's tallest tower",
     "Windows blown out across eight floors of the landmark in a second hit on the financial district this month."),
    ("BUSINESS", "US consortium wins Kenya's $60bn minerals deal",
     "Mrima Hill contract beats Chinese rivals; a Van Gogh sells for a record $190.4m."),
]

# masthead
d.rectangle([0, 0, W, 112], fill=(8, 15, 28))
d.text((40, 18), "THE DAILY WORLD", font=font(F_SERIF_B, 54), fill=WHITE)
d.text((40, 80), "Friday, 20 November 2026  \u00b7  The day's world news in one image", font=font(F_SANS, 21), fill=MUTED)
tag = "TOP STORIES"
tf = font(F_SANS_B, 19)
tw = d.textlength(tag, font=tf)
d.rounded_rectangle([W - tw - 60, 30, W - 22, 66], radius=8, fill=RED)
d.text((W - tw - 41, 38), tag, font=tf, fill=WHITE)
d.line([0, 112, W, 112], fill=GOLD, width=3)

# lead story
y = 128
d.rounded_rectangle([32, y, W - 32, y + 158], radius=14, fill=PANEL, outline=GOLD, width=2)
d.text((56, y + 12), stories[0][0], font=font(F_SANS_B, 19), fill=GOLD)
draw_wrapped(56, y + 40, stories[0][1], font(F_SANS_B, 28), WHITE, 890, 34)
draw_wrapped(56, y + 112, stories[0][2], font(F_SANS, 16), MUTED, 890, 20)

# grid of remaining stories: 2 cols x 4 rows
gx0, gx1 = 32, 528
cw, ch = 464, 148
gy = 300
for i, (cat, head, sub) in enumerate(stories[1:], start=2):
    x = gx0 if (i % 2 == 0) else gx1
    if i % 2 == 0 and i > 2:
        pass
    row = (i - 2) // 2
    col = (i - 2) % 2
    x = gx0 if col == 0 else gx1
    yy = gy + row * (ch + 12)
    d.rounded_rectangle([x, yy, x + cw, yy + ch], radius=10, fill=PANEL, outline=LINE, width=1)
    d.ellipse([x + 14, yy + 14, x + 50, yy + 50], fill=GOLD)
    nf = font(F_SANS_B, 21)
    d.text((x + 32 - d.textlength(str(i), font=nf) / 2, yy + 20), str(i), font=nf, fill=BG)
    d.text((x + 62, yy + 12), cat, font=font(F_SANS_B, 14), fill=RED)
    draw_wrapped(x + 62, yy + 32, head, font(F_SANS_B, 19), WHITE, cw - 80, 23)
    draw_wrapped(x + 16, yy + 92, sub, font(F_SANS, 14), MUTED, cw - 32, 17)

# footer
d.line([0, H - 34, W, H - 34], fill=LINE, width=1)
d.text((40, H - 28), "Sources: BBC, Reuters, AP \u00b7 20 Nov 2026 (UTC)", font=font(F_SANS, 15), fill=MUTED)

img.save("entry.png", optimize=True)
import os
print("entry.png", img.size, os.path.getsize("entry.png"), "bytes")
