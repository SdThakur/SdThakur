#!/usr/bin/env python3
"""Generate an animated GitHub-streak SVG (squares light up one by one).
Works standalone; designed to run in a GitHub Action daily to stay live.
Usage: python generate_streak_svg.py [username] [output.svg]
"""
import sys, json, os, datetime, urllib.request

USER = sys.argv[1] if len(sys.argv) > 1 else "SdThakur"
OUT  = sys.argv[2] if len(sys.argv) > 2 else "contrib-heatmap.svg"

def get_data(user):
    snap = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data", "contributions.json")
    if os.path.exists(snap):
        d = json.load(open(snap))
        if d.get("username", "").lower() == user.lower() and all("level" in x for x in d["days"]):
            return {"contributions": d["days"], "total": {"lastYear": d["total_contributions"]}}
    url = f"https://github-contributions-api.jogruber.de/v4/{user}?y=last"
    try:
        with urllib.request.urlopen(url, timeout=25) as r:
            return json.loads(r.read().decode())
    except Exception as e:
        print("API failed (%s)" % e)
        raise

data = get_data(USER)
contribs = data["contributions"]
total = data["total"]["lastYear"]

# ---- layout ----
CELL, GAP, RAD, LEFT, TOP = 13, 3, 2.5, 34, 24
COLORS = ["#161b22", "#0e4429", "#006d32", "#26a641", "#39d353"]
FLASH = "#b4ffaa"
GRAY = "#7d8590"
MONTHS = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]

n = len(contribs)
NW = (n + 6) // 7
W = LEFT + NW*(CELL+GAP) + 6
H = TOP + 7*(CELL+GAP) + 22

# timing (seconds)
REVEAL, DUR = 3.6, 0.55
maxorder = (NW-1) + 6*0.55

rects, labels = [], []
sd = datetime.date.fromisoformat(contribs[0]["date"])
last_m = None
for wk in range(NW):
    d = sd + datetime.timedelta(days=wk*7)
    if d.month != last_m:
        last_m = d.month
        labels.append(f'<text class="lbl" x="{LEFT+wk*(CELL+GAP)}" y="{TOP-8}">{MONTHS[d.month-1]}</text>')
for name, r in [("Mon",1),("Wed",3),("Fri",5)]:
    labels.append(f'<text class="lbl" x="2" y="{TOP+r*(CELL+GAP)+CELL-2}">{name}</text>')

for i, day in enumerate(contribs):
    wk = i // 7
    dow = i % 7
    x = LEFT + wk*(CELL+GAP)
    y = TOP + dow*(CELL+GAP)
    lvl = day.get("level", 0)
    col = COLORS[lvl]
    cnt = day.get("count", 0)
    tip = f"{day['date']}: {cnt} contribution{'s' if cnt!=1 else ''}"

    order = wk + dow*0.55
    delay = (order / maxorder) * REVEAL
    rects.append(
        f'<rect class="c" style="animation-delay:{delay:.2f}s" '
        f'x="{x}" y="{y}" width="{CELL}" height="{CELL}" rx="{RAD}" '
        f'data-fill="{col}"><title>{tip}</title></rect>'
    )

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
<style>
  svg {{ background: #0d1117; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif; }}
  .lbl {{ fill: {GRAY}; font-size: 10px; }}
  .c {{
    fill: {COLORS[0]};
    animation: pop {DUR}s cubic-bezier(0.34, 1.56, 0.64, 1) forwards;
    transform-origin: center;
  }}
  @keyframes pop {{
    0%   {{ fill: {COLORS[0]}; }}
    40%  {{ fill: {FLASH}; }}
    100% {{ fill: var(--final); }}
  }}
</style>
<script>
  // fallback for static viewers
</script>
<g id="labels">{''.join(labels)}</g>
<g id="cells">{''.join(rects)}</g>
</svg>'''

svg = svg.replace('data-fill="', 'style="--final:')
svg = svg.replace('" data-fill="', '; --final:')
out_dir = os.path.dirname(OUT)
if out_dir:
    os.makedirs(out_dir, exist_ok=True)
with open(OUT, "w") as f:
    f.write(svg)
print(f"wrote {OUT} ({W}x{H}, {total} contributions)")
