"""Figuras de la presentación de diseños 3^k (se generan al construir el contenido).

Uso desde contenido_3k.py: figuras_3k.generar(carpeta) → dict nombre → ruta png.
"""
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

PRIM, ACC, INK, MUTED = "#0F4C5C", "#E36414", "#142B33", "#5B6B73"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11})


def _limpio(ax):
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    ax.tick_params(colors=MUTED, labelsize=10)


def fig_3x3(out):
    """Las 9 combinaciones del 3^2 con su notación digital (fig. 9-1)."""
    fig, ax = plt.subplots(figsize=(4.2, 3.9))
    for a in range(3):
        for b in range(3):
            ax.plot(a, b, "o", ms=11, color=PRIM, mec="white", mew=1.2, zorder=3)
            ax.text(a + 0.12, b + 0.1, f"{a}{b}", fontsize=12, color=INK)
    for v in range(3):
        ax.plot([0, 2], [v, v], color="#C9D6DA", lw=1.2, zorder=1)
        ax.plot([v, v], [0, 2], color="#C9D6DA", lw=1.2, zorder=1)
    ax.set_xticks([0, 1, 2]); ax.set_yticks([0, 1, 2])
    ax.set_xlabel("Factor A", color=MUTED); ax.set_ylabel("Factor B", color=MUTED)
    ax.set_xlim(-0.4, 2.6); ax.set_ylim(-0.4, 2.6)
    _limpio(ax)
    fig.tight_layout(); fig.savefig(out, dpi=200); plt.close(fig)


def fig_cubo(out, marcar=None, titulo=None):
    """Las 27 combinaciones del 3^3 en proyección oblicua (fig. 9-2); marcar: set de dígitos en naranja."""
    marcar = marcar or set()
    fig, ax = plt.subplots(figsize=(5.2, 4.6))
    dx, dy = 0.42, 0.3
    P = lambda a, b, c: (a + dx * b, c + dy * b)
    for b in range(3):
        for v in range(3):
            ax.plot([P(0, b, v)[0], P(2, b, v)[0]], [P(0, b, v)[1], P(2, b, v)[1]], color="#C9D6DA", lw=0.9, zorder=1)
            ax.plot([P(v, b, 0)[0], P(v, b, 2)[0]], [P(v, b, 0)[1], P(v, b, 2)[1]], color="#C9D6DA", lw=0.9, zorder=1)
    for a in range(3):
        for c in range(3):
            ax.plot([P(a, 0, c)[0], P(a, 2, c)[0]], [P(a, 0, c)[1], P(a, 2, c)[1]], color="#C9D6DA", lw=0.9, zorder=1)
    for a in range(3):
        for b in range(3):
            for c in range(3):
                x, y = P(a, b, c)
                d = f"{a}{b}{c}"
                sel = d in marcar
                ax.plot(x, y, "o", ms=9 if sel else 6, color=ACC if sel else PRIM, mec="white", mew=1, zorder=3 + sel)
                ax.text(x + 0.05, y + 0.06, d, fontsize=8.5, color=ACC if sel else MUTED, zorder=5)
    ax.text(2.35, -0.25, "A", color=MUTED); ax.text(-0.05, 2.35, "C", color=MUTED); ax.text(2.95, 0.85, "B", color=MUTED)
    ax.set_axis_off()
    if titulo:
        ax.set_title(titulo, loc="left", fontsize=11, color=INK)
    ax.set_xlim(-0.3, 3.3); ax.set_ylim(-0.4, 2.9)
    fig.tight_layout(); fig.savefig(out, dpi=200); plt.close(fig)


def fig_contorno(out, b, xlab, ylab, xt, yt, titulo, niveles=None, marca=None):
    """Contornos de ŷ = b0 + b1 x1 + b2 x2 + b11 x1² + b22 x2² + b12 x1 x2 en el cuadrado [−1, 1]²."""
    x = np.linspace(-1, 1, 121)
    X1, X2 = np.meshgrid(x, x)
    Y = b[0] + b[1] * X1 + b[2] * X2 + b[3] * X1 ** 2 + b[4] * X2 ** 2 + b[5] * X1 * X2
    fig, ax = plt.subplots(figsize=(4.6, 4.0))
    cs = ax.contour(X1, X2, Y, levels=niveles or 10, colors=PRIM, linewidths=1.2)
    ax.clabel(cs, fontsize=8, fmt="%.0f", colors=INK)
    if marca:
        ax.plot(*marca, "o", color=ACC, ms=9, zorder=5)
    ax.set_xticks([-1, 0, 1]); ax.set_xticklabels(xt)
    ax.set_yticks([-1, 0, 1]); ax.set_yticklabels(yt)
    ax.set_xlabel(xlab, color=MUTED); ax.set_ylabel(ylab, color=MUTED)
    ax.set_title(titulo, loc="left", fontsize=11, color=INK)
    _limpio(ax)
    fig.tight_layout(); fig.savefig(out, dpi=200); plt.close(fig)


def fig_bloques3x3(out, L, titulo):
    """El 3^2 en tres bloques (fig. 9-6): cada combinación coloreada por el valor de L mod 3."""
    cols = [PRIM, ACC, "#8FB3BC"]
    fig, ax = plt.subplots(figsize=(4.8, 4.1))
    for a in range(3):
        for b in range(3):
            l = L(a, b)
            ax.plot(a, b, "o", ms=14, color=cols[l], mec="white", mew=1.2, zorder=3)
            ax.text(a + 0.13, b + 0.11, f"{a}{b}", fontsize=12, color=INK)
    for v in range(3):
        ax.plot([0, 2], [v, v], color="#C9D6DA", lw=1.2, zorder=1)
        ax.plot([v, v], [0, 2], color="#C9D6DA", lw=1.2, zorder=1)
    for l, c in enumerate(cols):
        ax.plot([], [], "o", color=c, ms=10, label=f"Bloque {l + 1}  (L = {l})")
    ax.legend(loc="upper center", bbox_to_anchor=(0.45, -0.16), ncol=3, frameon=False, fontsize=8, handletextpad=0.3, columnspacing=0.8)
    ax.set_xticks([0, 1, 2]); ax.set_yticks([0, 1, 2])
    ax.set_xlabel("Factor A", color=MUTED); ax.set_ylabel("Factor B", color=MUTED)
    ax.set_xlim(-0.4, 2.6); ax.set_ylim(-0.4, 2.6)
    ax.set_title(titulo, loc="left", fontsize=11, color=INK)
    _limpio(ax)
    fig.tight_layout(); fig.savefig(out, dpi=200); plt.close(fig)


def fig_lq(out):
    """Los contrastes lineal (−1, 0, 1) y cuadrático (1, −2, 1) sobre tres niveles."""
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(6.4, 2.9))
    for ax, c, t in ((a1, (-1, 0, 1), "Lineal:  (−1, 0, +1)"), (a2, (1, -2, 1), "Cuadrático:  (+1, −2, +1)")):
        ax.bar([0, 1, 2], c, color=[PRIM if v >= 0 else ACC for v in c], width=0.5)
        ax.axhline(0, color=MUTED, lw=0.8)
        ax.set_xticks([0, 1, 2]); ax.set_xticklabels(["bajo (0)", "medio (1)", "alto (2)"])
        ax.set_title(t, loc="left", fontsize=11, color=INK)
        ax.set_ylim(-2.4, 1.6)
        _limpio(ax)
    fig.tight_layout(); fig.savefig(out, dpi=200); plt.close(fig)


def generar(carpeta, modelos):
    """modelos: dict nombre → (coeficientes b, etiquetas…) para los contornos."""
    os.makedirs(carpeta, exist_ok=True)
    F = {}
    F["grid"] = os.path.join(carpeta, "3x3.png"); fig_3x3(F["grid"])
    F["cubo"] = os.path.join(carpeta, "cubo.png"); fig_cubo(F["cubo"])
    F["lq"] = os.path.join(carpeta, "lq.png"); fig_lq(F["lq"])
    F["bloques"] = os.path.join(carpeta, "bloques3x3.png")
    fig_bloques3x3(F["bloques"], lambda a, b: (a + 2 * b) % 3, "L = x₁ + 2x₂ (mod 3): AB² confundida")
    F["cubo_frac"] = os.path.join(carpeta, "cubo_fraccion.png")
    fig_cubo(F["cubo_frac"], marcar={"000", "110", "220", "101", "211", "021", "202", "012", "122"},
             titulo="Fracción u = 0 de I = AB²C² (9 de 27 corridas)")
    F["cubo_bloq"] = os.path.join(carpeta, "cubo_bloques.png")
    fig_cubo(F["cubo_bloq"], marcar={"000", "110", "220", "101", "211", "021", "202", "012", "122"},
             titulo="Bloque principal de AB²C² (L = 0)")
    for nombre, (b, xlab, ylab, xt, yt, tit, niv, marca) in modelos.items():
        F[nombre] = os.path.join(carpeta, f"contorno_{nombre}.png")
        fig_contorno(F[nombre], b, xlab, ylab, xt, yt, tit, niv, marca)
    return F
