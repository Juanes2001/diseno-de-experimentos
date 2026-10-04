"""Genera la guía de estudio (HTML listo para imprimir a PDF) a partir de contenido.SLIDES."""
import html
import sys

from contenido import SLIDES, M
from render_pptx import parse, plain, CUBE

CSS = """
@page { size: A4; margin: 20mm 18mm 20mm 18mm;
        @bottom-center { content: counter(page); font: 9pt Calibri, 'Segoe UI', Arial, sans-serif; color: #5b6b73; } }
* { box-sizing: border-box; }
body { font: 11pt/1.5 Calibri, 'Segoe UI', Arial, sans-serif; color: #142b33; margin: 0; }
h1, h2, h3 { font-family: Cambria, Georgia, serif; color: #0f4c5c; line-height: 1.2; }
.portada { height: 250mm; display: flex; flex-direction: column; justify-content: center; page-break-after: always; }
.portada h1 { font-size: 30pt; margin: 0 0 6mm; }
.portada .sub { font-size: 14pt; color: #5b6b73; margin: 0 0 16mm; }
.portada .meta { font-size: 11.5pt; }
.portada .como { margin-top: 14mm; background: #e8f1f3; border-radius: 6px; padding: 5mm 6mm; font-size: 10.5pt; }
.indice { page-break-after: always; }
.indice ol { columns: 1; padding-left: 6mm; }
.indice li { margin: 1.2mm 0; }
h2 { font-size: 19pt; margin: 0 0 2mm; page-break-before: always; }
h2 .n { display: inline-block; background: #e36414; color: #fff; border-radius: 50%; width: 11mm; height: 11mm;
        line-height: 11mm; text-align: center; font-size: 14pt; margin-right: 3mm; }
.secsub { color: #5b6b73; margin: 0 0 6mm; font-size: 11.5pt; }
section.d { margin: 0 0 8mm; break-inside: avoid; }
h3 { font-size: 13.5pt; margin: 0 0 2mm; break-after: avoid; }
p { margin: 0 0 2.4mm; text-align: justify; }
.bloques { margin-top: 3mm; }
.cols { display: flex; gap: 5mm; align-items: flex-start; }
.cols > div { min-width: 0; }
table { border-collapse: collapse; width: 100%; margin: 0 0 3mm; font-size: 9.6pt; break-inside: avoid; }
th { background: #0f4c5c; color: #fff; padding: 1.4mm 2mm; text-align: center; font-weight: 700; }
td { padding: 1.2mm 2mm; border-bottom: 0.3pt solid #d5dee1; text-align: center; vertical-align: middle; }
td.l, th.l { text-align: left; }
tr.hl td { background: #fde8d7; }
td.pos { color: #0f4c5c; font-weight: 700; } td.neg { color: #e36414; font-weight: 700; }
ul, ol.pasos { margin: 0 0 3mm; padding-left: 6mm; } li { margin: 0 0 1mm; }
.form { background: #e8f1f3; border-radius: 5px; padding: 2.5mm 4mm; margin: 0 0 3mm; text-align: center;
        font-family: 'Cambria Math', Cambria, serif; color: #0f4c5c; font-size: 12pt; break-inside: avoid; }
.form.big { font-size: 26pt; }
.nota { background: #fde8d7; border-radius: 5px; padding: 2.2mm 4mm; margin: 0 0 3mm; break-inside: avoid; }
.txt { margin: 0 0 2mm; } .txt.s { color: #5b6b73; font-size: 9.5pt; }
.ruta { margin: 0 0 3mm; } .ruta span { display: inline-block; background: #0f4c5c; color: #fff; font-weight: 700;
        border-radius: 4px; padding: 0.8mm 2.5mm; } .ruta span.fin { background: #e36414; } .ruta i { color: #5b6b73; font-style: normal; margin: 0 1.5mm; }
pre { background: #f4f8f9; border: 0.5pt solid #c9d6da; padding: 3mm; font: 8.6pt/1.3 'Courier New', monospace;
      margin: 0 0 3mm; break-inside: avoid; white-space: pre; overflow: hidden; }
.cards { display: grid; gap: 3mm; margin: 0 0 3mm; } .card { background: #e8f1f3; border-radius: 5px; padding: 2.5mm 3.5mm; break-inside: avoid; }
.card b.h { display: block; font-family: Cambria, serif; color: #0f4c5c; font-size: 11.5pt; margin-bottom: 1mm; }
figure { margin: 0 0 3mm; break-inside: avoid; text-align: center; }
figcaption { font-size: 9.5pt; color: #0f4c5c; font-weight: 700; margin-bottom: 1mm; }
svg text { font-family: Calibri, 'Segoe UI', Arial, sans-serif; }
"""


def rich(text):
    out = []
    for t, b, mode in parse(text):
        t = html.escape(t)
        if mode == "sup":
            t = f"<sup>{t}</sup>"
        elif mode == "sub":
            t = f"<sub>{t}</sub>"
        if b:
            t = f"<b>{t}</b>"
        out.append(t)
    return "".join(out)


# ------------------------------------------------------------------ gráficas SVG
def ticks(lo, hi, n=5):
    import math
    span = hi - lo or 1
    step = 10 ** math.floor(math.log10(span / n))
    for m in (1, 2, 2.5, 5, 10):
        if span / (step * m) <= n:
            step *= m
            break
    t = math.ceil(lo / step) * step
    out = []
    while t <= hi + 1e-9:
        out.append(round(t, 10))
        t += step
    return out


def fmt(v):
    s = f"{v:.2f}".rstrip("0").rstrip(".")
    return s.replace("-", M) if s not in ("-0", "") else "0"


def svg_scatter(b, W=420, H=300):
    pts = b["points"]
    xs, ys = [p[0] for p in pts], [p[1] for p in pts]
    px0, px1, py0, py1 = 52, W - 28, 16, H - 44
    xlo, xhi = min(xs), max(xs)
    ylo, yhi = min(ys), max(ys)
    if set(xs) <= {-1, 1}:
        xlo, xhi = -2, 2
    dx, dy = (xhi - xlo) * 0.08 or 1, (yhi - ylo) * 0.08 or 1
    xlo, xhi, ylo, yhi = xlo - dx, xhi + dx, ylo - dy, yhi + dy
    X = lambda v: px0 + (v - xlo) / (xhi - xlo) * (px1 - px0)
    Y = lambda v: py1 - (v - ylo) / (yhi - ylo) * (py1 - py0)
    o = [f'<svg viewBox="0 0 {W} {H}" width="100%" xmlns="http://www.w3.org/2000/svg">']
    for t in ticks(ylo, yhi):
        o.append(f'<line x1="{px0}" x2="{px1}" y1="{Y(t):.1f}" y2="{Y(t):.1f}" stroke="#dde5e8" stroke-width="0.6"/>')
        o.append(f'<text x="{px0 - 6}" y="{Y(t) + 3.5:.1f}" font-size="10" text-anchor="end" fill="#5b6b73">{fmt(t)}</text>')
    xt = [-1, 1] if set(xs) <= {-1, 1} else ticks(xlo, xhi)
    for t in xt:
        o.append(f'<text x="{X(t):.1f}" y="{py1 + 14}" font-size="10" text-anchor="middle" fill="#5b6b73">{fmt(t)}</text>')
    o.append(f'<rect x="{px0}" y="{py0}" width="{px1 - px0}" height="{py1 - py0}" fill="none" stroke="#9aa8ae" stroke-width="0.8"/>')
    if b.get("line") == "fit":
        n = len(xs)
        mx, my = sum(xs) / n, sum(ys) / n
        sl = sum((a - mx) * (c - my) for a, c in zip(xs, ys)) / sum((a - mx) ** 2 for a in xs)
        a0, a1 = min(xs), max(xs)
        o.append(f'<line x1="{X(a0):.1f}" y1="{Y(my + sl * (a0 - mx)):.1f}" x2="{X(a1):.1f}" y2="{Y(my + sl * (a1 - mx)):.1f}" stroke="#e36414" stroke-width="1.4"/>')
    for i, (x, y) in enumerate(pts):
        o.append(f'<circle cx="{X(x):.1f}" cy="{Y(y):.1f}" r="4" fill="#0f4c5c" stroke="#fff" stroke-width="0.8"/>')
        if i in b["labels"]:
            right = X(x) < px1 - 40
            o.append(f'<text x="{X(x) + (7 if right else -7):.1f}" y="{Y(y) + 4:.1f}" font-size="11" font-weight="700" '
                     f'text-anchor="{"start" if right else "end"}" fill="#e36414">{html.escape(b["labels"][i])}</text>')
    o.append(f'<text x="{(px0 + px1) / 2}" y="{H - 8}" font-size="10.5" text-anchor="middle" fill="#5b6b73">{html.escape(b["xlab"])}</text>')
    o.append(f'<text transform="translate(13 {(py0 + py1) / 2}) rotate(-90)" font-size="10.5" text-anchor="middle" fill="#5b6b73">{html.escape(b["ylab"])}</text>')
    o.append("</svg>")
    return "".join(o)


def svg_bar(b, W=420, H=300):
    cats, vals = [plain(c) for c in b["cats"]], b["vals"]
    vertical = all(c.startswith("k = ") for c in cats)
    dec = 0 if b["fmt"] == "0" else 2
    o = [f'<svg viewBox="0 0 {W} {H}" width="100%" xmlns="http://www.w3.org/2000/svg">']
    if vertical:
        px0, px1, py0, py1 = 40, W - 10, 18, H - 44
        vmax = max(vals) * 1.1
        bw = (px1 - px0) / len(cats)
        for i, (c, v) in enumerate(zip(cats, vals)):
            hh = v / vmax * (py1 - py0)
            x = px0 + i * bw + bw * 0.18
            o.append(f'<rect x="{x:.1f}" y="{py1 - hh:.1f}" width="{bw * 0.64:.1f}" height="{hh:.1f}" fill="#0f4c5c"/>')
            o.append(f'<text x="{x + bw * 0.32:.1f}" y="{py1 - hh - 4:.1f}" font-size="10" text-anchor="middle">{v:.{dec}f}</text>')
            o.append(f'<text x="{x + bw * 0.32:.1f}" y="{py1 + 14}" font-size="10" text-anchor="middle" fill="#5b6b73">{html.escape(c)}</text>')
        o.append(f'<line x1="{px0}" x2="{px1}" y1="{py1}" y2="{py1}" stroke="#9aa8ae"/>')
        o.append(f'<text x="{(px0 + px1) / 2}" y="{H - 8}" font-size="10.5" text-anchor="middle" fill="#5b6b73">{html.escape(b["xlab"])}</text>')
    else:
        px0, px1, py0, py1 = 46, W - 46, 8, H - 34
        lo, hi = min(0, min(vals)), max(0, max(vals))
        span = (hi - lo) * 1.12
        X = lambda v: px0 + (v - lo) / span * (px1 - px0)
        bh = (py1 - py0) / len(cats)
        for i, (c, v) in enumerate(zip(cats, vals)):
            y = py0 + i * bh + bh * 0.2
            x0, x1 = sorted((X(0), X(v)))
            o.append(f'<rect x="{x0:.1f}" y="{y:.1f}" width="{max(x1 - x0, 0.5):.1f}" height="{bh * 0.6:.1f}" fill="#0f4c5c"/>')
            lab = f"{v:.{dec}f}".replace("-", M)
            if v >= 0:
                o.append(f'<text x="{x1 + 4:.1f}" y="{y + bh * 0.42:.1f}" font-size="10">{lab}</text>')
            else:
                o.append(f'<text x="{x1 + 4:.1f}" y="{y + bh * 0.42:.1f}" font-size="10">{lab}</text>')
            o.append(f'<text x="{px0 - 6}" y="{y + bh * 0.42:.1f}" font-size="10.5" text-anchor="end" fill="#142b33">{html.escape(c)}</text>')
        o.append(f'<line x1="{X(0):.1f}" x2="{X(0):.1f}" y1="{py0}" y2="{py1}" stroke="#9aa8ae"/>')
        o.append(f'<text x="{(px0 + px1) / 2}" y="{H - 10}" font-size="10.5" text-anchor="middle" fill="#5b6b73">{html.escape(b["xlab"])}</text>')
    o.append("</svg>")
    return "".join(o)


def svg_line(b, W=420, H=300):
    px0, px1, py0, py1 = 52, W - 28, 16, H - 62
    allv = [v for _, vs in b["series"] for v in vs]
    lo, hi = 0, max(allv) * 1.12
    Y = lambda v: py1 - (v - lo) / (hi - lo) * (py1 - py0)
    xs = [px0 + (px1 - px0) * 0.2, px0 + (px1 - px0) * 0.8]
    o = [f'<svg viewBox="0 0 {W} {H}" width="100%" xmlns="http://www.w3.org/2000/svg">']
    for t in ticks(lo, hi):
        o.append(f'<line x1="{px0}" x2="{px1}" y1="{Y(t):.1f}" y2="{Y(t):.1f}" stroke="#dde5e8" stroke-width="0.6"/>')
        o.append(f'<text x="{px0 - 6}" y="{Y(t) + 3.5:.1f}" font-size="10" text-anchor="end" fill="#5b6b73">{fmt(t)}</text>')
    for x, c in zip(xs, b["cats"]):
        o.append(f'<text x="{x:.1f}" y="{py1 + 14}" font-size="10.5" text-anchor="middle" fill="#5b6b73">{html.escape(c)}</text>')
    for k, ((name, vs), col) in enumerate(zip(b["series"], ("#0f4c5c", "#e36414"))):
        o.append(f'<line x1="{xs[0]:.1f}" y1="{Y(vs[0]):.1f}" x2="{xs[1]:.1f}" y2="{Y(vs[1]):.1f}" stroke="{col}" stroke-width="2.2"/>')
        for x, v in zip(xs, vs):
            o.append(f'<circle cx="{x:.1f}" cy="{Y(v):.1f}" r="4" fill="{col}"/>')
            o.append(f'<text x="{x + 8:.1f}" y="{Y(v) - 6:.1f}" font-size="10">{fmt(v)}</text>')
        lx = px0 + 40 + k * 150
        o.append(f'<line x1="{lx}" x2="{lx + 22}" y1="{H - 22}" y2="{H - 22}" stroke="{col}" stroke-width="2.2"/>')
        o.append(f'<text x="{lx + 28}" y="{H - 18}" font-size="10.5">{html.escape(name)}</text>')
    o.append(f'<line x1="{px0}" x2="{px1}" y1="{py1}" y2="{py1}" stroke="#9aa8ae"/>')
    o.append(f'<text transform="translate(13 {(py0 + py1) / 2}) rotate(-90)" font-size="10.5" text-anchor="middle" fill="#5b6b73">{html.escape(b["ylab"])}</text>')
    o.append("</svg>")
    return "".join(o)


def svg_cube(b, W=320, H=260):
    side, dx, dy = 130, 68, 50
    ox, oy = 60, 70
    P = {k: (ox + a * side + bb * dx, oy + (1 - c) * side - bb * dy) for k, (a, bb, c) in CUBE.items()}
    o = [f'<svg viewBox="0 0 {W} {H}" width="78%" xmlns="http://www.w3.org/2000/svg">']
    names = list(CUBE)
    for i, p in enumerate(names):
        for q in names[i + 1:]:
            if sum(abs(u - v) for u, v in zip(CUBE[p], CUBE[q])) == 1:
                o.append(f'<line x1="{P[p][0]}" y1="{P[p][1]}" x2="{P[q][0]}" y2="{P[q][1]}" stroke="#9aa8ae" stroke-width="1.2"/>')
    for k, (x, y) in P.items():
        sel = k in b["sel"]
        o.append(f'<circle cx="{x}" cy="{y}" r="8" fill="{"#e36414" if sel else "#fff"}" stroke="{"#e36414" if sel else "#9aa8ae"}" stroke-width="1.5"/>')
        right = CUBE[k][0] == 1
        o.append(f'<text x="{x + (13 if right else -13)}" y="{y - 9}" font-size="14" font-weight="{700 if sel else 400}" '
                 f'text-anchor="{"start" if right else "end"}" fill="{"#e36414" if sel else "#5b6b73"}">{html.escape(k)}</text>')
    o.append("</svg>")
    return "".join(o)


# ------------------------------------------------------------------ bloques HTML
def block(b):
    t = b["t"]
    if t == "bul":
        return "<ul>" + "".join(f"<li>{rich(i)}</li>" for i in b["items"]) + "</ul>"
    if t == "num":
        return '<ol class="pasos">' + "".join(f"<li>{rich(i)}</li>" for i in b["items"]) + "</ol>"
    if t == "txt":
        return f'<div class="txt{" s" if b["size"] < 15 else ""}">{rich(b["text"])}</div>'
    if t == "note":
        return f'<div class="nota">{rich(b["text"])}</div>'
    if t == "form":
        cls = "form big" if b["size"] >= 40 else "form"
        return f'<div class="{cls}">' + "<br>".join(rich(l) for l in b["lines"]) + "</div>"
    if t == "path":
        parts = []
        for k, s in enumerate(b["steps"]):
            parts.append(f'<span class="{"fin" if k == len(b["steps"]) - 1 else ""}">{html.escape(s)}</span>')
        return '<div class="ruta">' + "<i>›</i>".join(parts) + "</div>"
    if t == "mono":
        return f"<pre>{html.escape(b['text'])}</pre>"
    if t == "cards":
        n = len(b["items"])
        cols = 1 if b.get("cols") == 1 else (2 if n in (2, 4, 8, 10) else (3 if n in (3, 5, 6) else 2))
        cells = "".join(f'<div class="card"><b class="h">{rich(h_)}</b>{rich(tx)}</div>' for h_, tx in b["items"])
        return f'<div class="cards" style="grid-template-columns: repeat({cols}, 1fr)">{cells}</div>'
    if t == "tab":
        cg = ""
        if b["colw"]:
            cg = "<colgroup>" + "".join(f'<col style="width:{100 * c:.1f}%">' for c in b["colw"]) + "</colgroup>"
        left = lambda j, c: (b["first_left"] and (j == 0 or any(len(plain(rr[j])) > 30 for rr in b["rows"])))
        th = "".join(f'<th class="{"l" if (b["first_left"] and j == 0) else ""}">{rich(c)}</th>' for j, c in enumerate(b["head"]))
        rows = []
        for i, r in enumerate(b["rows"]):
            tds = []
            for j, c in enumerate(r):
                cls = "pos" if c == "+" else ("neg" if c == M else ("l" if left(j, c) else ""))
                tds.append(f'<td class="{cls}">{rich(c)}</td>')
            rows.append(f'<tr class="{"hl" if i in b["hl"] else ""}">' + "".join(tds) + "</tr>")
        return f"<table>{cg}<thead><tr>{th}</tr></thead><tbody>{''.join(rows)}</tbody></table>"
    if t == "chart":
        fn = {"scatter": svg_scatter, "bar": svg_bar, "line": svg_line}[b["kind"]]
        cap = f"<figcaption>{html.escape(b['title'])}</figcaption>" if b.get("title") else ""
        return f"<figure>{cap}{fn(b)}</figure>"
    if t == "cube":
        cap = f'<div class="txt s">{html.escape(b["caption"])}</div>' if b.get("caption") else ""
        return f"<figure>{svg_cube(b)}{cap}</figure>"
    raise ValueError(t)


def build(out):
    o = ['<!doctype html><html lang="es"><head><meta charset="utf-8">',
         "<title>Guía de estudio · Diseños factoriales fraccionados</title>", f"<style>{CSS}</style></head><body>"]
    o.append('<div class="portada"><h1>Diseños factoriales fraccionados 2<sup>k−p</sup></h1>'
             '<p class="sub">Guía de estudio para los expositores · Tema 6</p>'
             '<p class="meta">Diseño de Experimentos Avanzados (3008475)<br>Universidad Nacional de Colombia · 2026-II<br>'
             'Juan Esteban Rodríguez Ochoa · Sebastián Zapata Henao<br>Exposición: 31 de octubre de 2026</p>'
             '<div class="como"><b>Cómo usar esta guía.</b> Sigue el mismo orden de la presentación. Cada apartado '
             'corresponde a una diapositiva: primero la explicación que el expositor debe dominar y después el '
             'contenido que aparece proyectado (tablas, fórmulas y gráficas).</div></div>')
    secs = [s for s in SLIDES if s["kind"] == "section"]
    o.append('<div class="indice"><h2 style="page-break-before:auto">Contenido</h2><ol>')
    for s in secs:
        o.append(f'<li><b>{html.escape(s["title"])}</b> — {html.escape(s["sub"])}</li>')
    o.append("</ol></div>")
    first = True
    n = 0
    for s in SLIDES:
        n += 1
        if s["kind"] in ("title", "closing"):
            continue
        if s["kind"] == "section":
            o.append(f'<h2><span class="n">{s["n"]}</span>{rich(s["title"])}</h2><p class="secsub">{html.escape(s["sub"])}</p>')
            first = False
            continue
        if first:
            o.append('<h2 style="page-break-before:auto">Presentación</h2>')
            first = False
        o.append(f'<section class="d"><h3>{rich(s["title"])} <span style="font:9pt Calibri;color:#5b6b73">· diapositiva {n}</span></h3>')
        for par in s["explica"].split("\n\n"):
            o.append(f"<p>{rich(par.strip())}</p>")
        o.append('<div class="bloques">')
        if s.get("body"):
            o.append("".join(block(b) for b in s["body"]))
        else:
            r = s["ratio"]
            o.append(f'<div class="cols"><div style="flex:{r}">{"".join(block(b) for b in s["left"])}</div>'
                     f'<div style="flex:{1 - r}">{"".join(block(b) for b in s["right"])}</div></div>')
        o.append("</div></section>")
    o.append("</body></html>")
    open(out, "w", encoding="utf-8").write("".join(o))
    print("guía:", out)


if __name__ == "__main__":
    build(sys.argv[1])
