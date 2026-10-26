"""Bloques comunes de las presentaciones del tema 6 (fraccionados 2^{k−p} y diseños 3^k).

Cada diapositiva es un dict con título, bloques y un texto explicativo ("explica").
render_pptx.py lo convierte en la presentación y render_guia.py en la guía de estudio.
Marcado en los textos: ^{..} superíndice, _{..} subíndice, **..** negrita.
"""
M = "−"  # signo menos tipográfico


def sg(v):
    return "+" if v > 0 else M


def f(x, d=2):
    from decimal import Decimal, ROUND_HALF_UP
    s = str(Decimal(repr(round(x, 10))).quantize(Decimal(1).scaleb(-d), rounding=ROUND_HALF_UP))
    if s.startswith("-"):
        s = M + s[1:]
    return s


def pv(p):
    return "<0.0001" if p < 0.0001 else f"{p:.4f}"


# ---------------------------------------------------------------- bloques
def bul(*items, size=18):
    return {"t": "bul", "items": list(items), "size": size}


def num(*items, size=18):
    return {"t": "num", "items": list(items), "size": size}


def tab(head, rows, size=14, colw=None, hl=(), h=None, first_left=True, pad=0.13):
    return {"t": "tab", "head": head, "rows": rows, "size": size, "colw": colw,
            "hl": set(hl), "h": h, "first_left": first_left, "pad": pad}


def form(*lines, size=20):
    return {"t": "form", "lines": list(lines), "size": size}


def note(text, size=16):
    return {"t": "note", "text": text, "size": size}


def txt(text, size=18):
    return {"t": "txt", "text": text, "size": size}


def path(*steps):
    return {"t": "path", "steps": list(steps)}


def mono(text, size=12):
    return {"t": "mono", "text": text, "size": size}


def scatter(points, xlab, ylab, h=3.6, labels=None, line=None, title=None, hi=()):
    return {"t": "chart", "kind": "scatter", "points": points, "xlab": xlab, "ylab": ylab,
            "h": h, "labels": labels or {}, "line": line, "title": title, "hi": set(hi)}


def daniel(points, activos, origen=False):
    """Recta de Daniel: se ajusta solo con los efectos inactivos (efecto = a + σ·z) y se
    prolonga a todo el rango de puntuaciones; los activos son los que se apartan de ella.
    En la gráfica seminormal pasa por el origen."""
    nul = [p for i, p in enumerate(points) if i not in activos]
    zs = [p[1] for p in points]
    if origen:
        a, sg_ = 0.0, sum(x * z for x, z in nul) / sum(z * z for _, z in nul)
        z0 = 0.0
    else:
        mx = sum(x for x, _ in nul) / len(nul)
        mz = sum(z for _, z in nul) / len(nul)
        sg_ = sum((x - mx) * (z - mz) for x, z in nul) / sum((z - mz) ** 2 for _, z in nul)
        a, z0 = mx - sg_ * mz, min(zs)
    return [(a + sg_ * z0, z0), (a + sg_ * max(zs), max(zs))]


def bars(cats, vals, xlab, h=3.6, title=None, fmt="0.00"):
    return {"t": "chart", "kind": "bar", "cats": cats, "vals": vals, "xlab": xlab, "h": h,
            "title": title, "fmt": fmt}


def lines(cats, series, ylab, h=3.6, title=None):
    return {"t": "chart", "kind": "line", "cats": cats, "series": series, "ylab": ylab, "h": h,
            "title": title}


def cube(selected, h=3.4, caption=None):
    return {"t": "cube", "sel": selected, "h": h, "caption": caption}


def cards(*items, size=16, cols=None):
    """items: (encabezado, texto)"""
    return {"t": "cards", "items": list(items), "size": size, "cols": cols}


SLIDES = []
_sec = [""]
_secn = [0]


def section(n, title, sub):
    _sec[0] = title
    _secn[0] = n
    SLIDES.append({"kind": "section", "n": n, "title": title, "sub": sub, "sec": title,
                   "explica": ""})


def S(title, explica, body=None, left=None, right=None, ratio=0.5):
    SLIDES.append({"kind": "content", "title": title, "explica": explica.strip(),
                   "body": body, "left": left, "right": right, "ratio": ratio, "sec": _sec[0],
                   "secn": _secn[0]})


def E(n, nombre, fuente, parrafos, objetivo, pide, size=16):
    """Diapositiva de enunciado: la situación completa del ejemplo antes de resolverlo."""
    S(f"Ejemplo {n} · Enunciado: {nombre}",
      "\n\n".join(parrafos) + "\n\nObjetivo: " + objetivo + "\n\nSe pide: " +
      "; ".join(p[0].lower() + p[1:] for p in pide) + ". Fuente: " + fuente + ".",
      left=[txt(p_, size=size) for p_ in parrafos] + [txt("Fuente: " + fuente, size=12)],
      right=[cards(("Objetivo", objetivo), size=15, cols=1),
             txt("**Se pide**", size=17), num(*pide, size=15)],
      ratio=0.58)


PREVIO = []


def P(title, explica, body=None, left=None, right=None, ratio=0.5):
    PREVIO.append({"kind": "content", "title": title, "explica": explica.strip(),
                   "body": body, "left": left, "right": right, "ratio": ratio, "sec": "previo"})


def img(path, h=3.6, caption=None):
    """Imagen (png) generada por el contenido; se escala al ancho de la columna."""
    return {"t": "img", "path": path, "h": h, "caption": caption}
