"""The countdown, animated: a terminal where you negotiate and mom counts.

Renders media/countdown.gif — HTML frames shot with headless Chrome,
stitched with ffmpeg. Pure stdlib.

    python3 render_gif.py
"""
import pathlib
import subprocess
import tempfile

HERE = pathlib.Path(__file__).resolve().parent
W, H = 800, 450

USER = "#7ee787"   # terminal green
MOM = "#ff7b72"    # mom red
DIM = "#8b949e"

CSS = f"""
*{{box-sizing:border-box;margin:0}}
body{{width:{W}px;height:{H}px;background:#010409;display:flex;
  align-items:center;justify-content:center;
  font-family:ui-monospace,'JetBrains Mono',Menlo,Consolas,monospace}}
.term{{width:720px;height:380px;background:#0d1117;border:1px solid #30363d;
  border-radius:12px;overflow:hidden;box-shadow:0 20px 60px rgba(0,0,0,.6)}}
.bar{{height:34px;background:#161b22;border-bottom:1px solid #30363d;
  display:flex;align-items:center;gap:7px;padding:0 14px}}
.dot{{width:11px;height:11px;border-radius:50%}}
.title{{margin-left:10px;color:{DIM};font-size:12px}}
.body{{padding:20px 24px;font-size:16px;line-height:2.1}}
.u{{color:{USER}}}
.m{{color:{MOM};font-weight:700}}
.cur{{display:inline-block;width:9px;height:18px;background:{USER};
  vertical-align:-3px}}
.big{{font-size:34px;font-weight:800;color:{MOM};margin-top:14px}}
.card{{text-align:center;color:#e6edf3}}
.card h1{{font-size:30px;margin-bottom:10px}}
.card p{{color:{DIM};font-size:15px}}
"""


def term(lines, cursor=True):
    rows = ""
    for who, txt in lines:
        rows += f'<div class="{who}">{txt}</div>'
    if cursor:
        rows += '<span class="cur"></span>'
    return (f'<!doctype html><meta charset=utf-8><style>{CSS}</style><body>'
            f'<div class="term"><div class="bar">'
            f'<span class="dot" style="background:#ff5f57"></span>'
            f'<span class="dot" style="background:#febc2e"></span>'
            f'<span class="dot" style="background:#28c840"></span>'
            f'<span class="title">claude — 00:13</span></div>'
            f'<div class="body">{rows}</div></div></body>')


def card():
    return (f'<!doctype html><meta charset=utf-8><style>{CSS}</style><body>'
            f'<div class="card"><h1>🛏️ go-to-damn-bed</h1>'
            f'<p>a Claude Code skill · it never says what happens at three</p>'
            f'</div></body>')


U1 = "> just one more experiment"
M1 = "The GPU isn't going anywhere. You are."
U2 = "> ok ok, last one, I promise"
U3 = "> ..."

FRAMES = [
    (term([("u", U1[:12])]), 0.5),
    (term([("u", U1)]), 0.9),
    (term([("u", U1), ("m", M1)]), 1.6),
    (term([("u", U1), ("m", M1), ("m", "One.")]), 1.4),
    (term([("u", U1), ("m", M1), ("m", "One."), ("u", U2[:14])]), 0.5),
    (term([("u", U1), ("m", M1), ("m", "One."), ("u", U2)]), 0.9),
    (term([("u", U1), ("m", M1), ("m", "One."), ("u", U2),
           ("m", "Two.")]), 1.5),
    (term([("u", U1), ("m", M1), ("m", "One."), ("u", U2),
           ("m", "Two."), ("u", U3)]), 1.2),
    (term([("u", U1), ("m", M1), ("m", "One."), ("u", U2),
           ("m", "Two."), ("u", U3),
           ("m", '<div class="big">🛏️ Go. Now.</div>')], cursor=False), 2.2),
    (card(), 2.0),
]


def main():
    build = pathlib.Path(tempfile.mkdtemp(prefix="bedgif_"))
    lines = []
    for i, (doc, hold) in enumerate(FRAMES):
        src = build / f"f{i:02d}.html"
        src.write_text(doc)
        subprocess.run(["google-chrome", "--headless=new",
                        f"--window-size={W},{H + 120}",
                        f"--screenshot={build / f'f{i:02d}.png'}",
                        "--hide-scrollbars", "--force-device-scale-factor=1",
                        str(src)], check=True, capture_output=True)
        lines += [f"file 'f{i:02d}.png'", f"duration {hold}"]
    lines.append(f"file 'f{len(FRAMES)-1:02d}.png'")
    (build / "c.txt").write_text("\n".join(lines) + "\n")
    out = HERE / "media"
    out.mkdir(exist_ok=True)
    subprocess.run(["ffmpeg", "-y", "-f", "concat", "-i", str(build / "c.txt"),
                    "-vf", f"crop={W}:{H}:0:0,fps=10,"
                           "scale=680:-1:flags=lanczos,split[a][b];"
                           "[a]palettegen=max_colors=64[p];"
                           "[b][p]paletteuse=dither=bayer:bayer_scale=3",
                    "-loop", "0", str(out / "countdown.gif")],
                   check=True, capture_output=True, cwd=build)
    print("->", out / "countdown.gif")


main()
