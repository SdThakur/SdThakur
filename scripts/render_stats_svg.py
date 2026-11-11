#!/usr/bin/env python3
"""
Render the streak / numbers card from data/contributions.json (written daily by
fetch_contributions.py) as a terminal-window SVG that sits beside satya-ascii.svg.
"""
import datetime
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "..", "data", "contributions.json")
OUT = sys.argv[2] if len(sys.argv) > 2 else os.path.join(HERE, "..", "stats.svg")

BG = "#0d1117"
BG2 = "#111722"
TILE = "#161b22"
FRAME = "#30363d"
MUTED = "#7d8590"
INK = "#e6edf3"
GREEN = "#39d353"
BAR = "#26a641"

W, H = 840, 880                      # == satya-ascii.svg canvas
PAD = 20
TITLEBAR_H = 30
COLS, ROWS = 2, 3
GAP = 16
TILE_W = (W - PAD * 2 - GAP * (COLS - 1)) / COLS
TILE_H = 150
TILES_TOP = TITLEBAR_H + PAD + 4
CHART_TOP = TILES_TOP + ROWS * TILE_H + (ROWS - 1) * GAP + GAP

TILE_STAGGER = 0.15
SLIDE_DUR = 0.45
COUNT_DUR = 1.2
FRAMES = 16
BAR_START = TILE_STAGGER * COLS * ROWS + 0.4
BAR_STAGGER = 0.06
BAR_DUR = 0.6


def short(d):
    if not d:
        return ""
    dt = datetime.date.fromisoformat(d)
    return f"{dt.strftime('%b')} {dt.day}"


def span(s):
    return f'{short(s["start"])} – {short(s["end"])}' if s.get("length") else "—"


def count_frames(val, label, x, y, dur, begin, font_size=40, color=INK, unit=""):
    num_txt = f"{val:,}" if isinstance(val, int) else str(val)
    unit_span = f'<tspan fill="{MUTED}" font-size="{int(font_size * 0.5)}"> {unit}</tspan>' if unit else ""
    return f'<text x="{x}" y="{y}" fill="{color}" font-size="{font_size}" font-weight="600">{num_txt}{unit_span}</text>'


def render():
    with open(SRC) as f:
        data = json.load(f)

    cur_s = data["current_streak"]
    lng_s = data["longest_streak"]
    total = data["total_contributions"]
    active = data["active_days"]
    best = data["best_day"]
    monthly = data["monthly"][-12:]

    tiles_data = [
        ("TOTAL CONTRIBUTIONS", total, "past 12 months", GREEN, ""),
        ("CURRENT STREAK", cur_s["length"], span(cur_s), GREEN, "days"),
        ("LONGEST STREAK", lng_s["length"], span(lng_s), INK, "days"),
        ("ACTIVE DAYS", active, f'{round(active / len(data["days"]) * 100)}% of the year', INK, "days"),
        ("BEST DAY", best["count"], short(best["date"]), GREEN, "commits"),
        ("AVG PER DAY", f'{total / len(data["days"]):.2f}', "all 365 days", INK, ""),
    ]

    parts = []
    parts.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" '
                 f'font-family="ui-monospace, SFMono-Regular, Menlo, Consolas, monospace">')
    parts.append('<defs>'
                 f'<linearGradient id="bg" x1="0" y1="0" x2="0" y2="1">'
                 f'<stop offset="0" stop-color="{BG2}"/><stop offset="1" stop-color="{BG}"/>'
                 f'</linearGradient></defs>')
    parts.append(f'<rect width="{W}" height="{H}" rx="12" fill="url(#bg)"/>')
    parts.append(f'<rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="12" fill="none" stroke="{FRAME}" stroke-width="1"/>')
    parts.append(f'<line x1="0" y1="{TITLEBAR_H}" x2="{W}" y2="{TITLEBAR_H}" stroke="{FRAME}"/>')
    for i, dotcol in enumerate(["#ff5f56", "#ffbd2e", "#27c93f"]):
        parts.append(f'<circle cx="{PAD + i*16}" cy="{TITLEBAR_H/2}" r="5" fill="{dotcol}"/>')
    parts.append(f'<text x="{W/2}" y="{TITLEBAR_H/2 + 4}" fill="{MUTED}" font-size="12" text-anchor="middle">satya@github: ~$ gh streak --stats</text>')

    for idx, (lbl, val, sub, col, unit) in enumerate(tiles_data):
        c = idx % COLS
        r = idx // COLS
        tx = PAD + c * (TILE_W + GAP)
        ty = TILES_TOP + r * (TILE_H + GAP)

        parts.append(f'<g transform="translate({tx},{ty})">')
        parts.append(f'<rect width="{TILE_W}" height="{TILE_H}" rx="8" fill="{TILE}" stroke="{FRAME}" stroke-width="1"/>')
        parts.append(f'<text x="20" y="32" fill="{MUTED}" font-size="12" letter-spacing="1">{lbl}</text>')
        parts.append(count_frames(val, lbl, 20, 85, COUNT_DUR, 0, 36, col, unit))
        parts.append(f'<text x="20" y="122" fill="{MUTED}" font-size="12">{sub}</text>')
        parts.append('</g>')

    parts.append('</svg>')
    out_svg = "".join(parts)
    out_dir = os.path.dirname(OUT)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    with open(OUT, "w") as f:
        f.write(out_svg)
    print(f"wrote {OUT}")


if __name__ == "__main__":
    render()
