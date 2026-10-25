"""Figuras de la presentación del protocolo (verificación por nivel del ancho de pulso).

Uso: .venv/bin/python figuras_protocolo.py <analisis_piloto.json> <carpeta_salida>
Genera: traza.png (una traza del piloto con su ajuste y el centro), piloto.png (τp por traza frente
a la hoja de fábrica), oc.png (potencia de la t de una muestra contra n y δ detectable).
"""
import json
import os
import sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from analiza_piloto import CONV, TAU0, g_sech2, potencia  # noqa: E402

RED, VIOLET, INK, MUTED, LINE = "#D7263D", "#5B3FD9", "#0E1726", "#5F6B7A", "#D5DAE2"
CUR = {"I1": "5 A", "I2": "6 A", "I3": "7 A"}
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11})


def estilo(ax):
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    for s in ("left", "bottom"):
        ax.spines[s].set_color(LINE)
    ax.tick_params(colors=MUTED, labelsize=10)
    ax.grid(axis="y", color="#EEF1F5", linewidth=0.8)
    ax.set_axisbelow(True)


def fig_traza(T, out):
    t = T["R12"]
    x, y = np.array(t["x"]), np.array(t["y"])
    f = t["fit_sech"]
    tau = x * CONV - f["centro"]                       # el cero de retardo es el centro ajustado (pico)
    yn = (y - f["B"]) / f["A"]
    tt = np.linspace(tau.min(), tau.max(), 500)
    fig, ax = plt.subplots(figsize=(6.4, 3.9))
    ax.plot(tt, g_sech2(tt, f["tau_p"]), color=VIOLET, lw=2.2, label="Ajuste sech² (A, B, τc, τp libres)")
    ax.plot(tau, yn, "o", ms=6, color=INK, mfc="white", mew=1.4, label="Lecturas (paso 10 µm = 66,7 fs)", zorder=3)
    d_ac = f["tau_p"] / 0.6482
    ax.hlines(0.5, -d_ac / 2, d_ac / 2, color=RED, lw=2, zorder=4)
    ax.text(-d_ac / 2 - 25, 0.5, f"Δτ_AC = {d_ac:.0f} fs", ha="right", va="center", color=RED, fontsize=10.5)
    ax.axvline(0, color=MUTED, lw=1, ls="--")
    ax.text(15, 0.12, "τ = 0 en el pico", color=MUTED, fontsize=9.5, ha="left", va="bottom")
    ax.text(0.98, 0.42, f"τp = 0,65 · Δτ_AC = {f['tau_p']:.0f} fs", transform=ax.transAxes, ha="right", fontsize=11, color=INK,
            bbox=dict(boxstyle="round,pad=0.35", fc="#EFECFF", ec="none"))
    ax.set_xlabel("Retardo τ respecto al centro (fs)", color=MUTED)
    ax.set_ylabel("Autocorrelación normalizada", color=MUTED)
    ax.set_ylim(-0.08, 1.1)
    ax.set_title(("Traza R12 del piloto · 5 A · R² = %.3f" % f["r2"]).replace(".", ","), loc="left", fontsize=11, color=INK)
    estilo(ax)
    ax.legend(loc="upper left", frameon=False, fontsize=9.5)
    fig.tight_layout()
    fig.savefig(out, dpi=220)
    plt.close(fig)


def fig_piloto(T, out):
    fig, ax = plt.subplots(figsize=(6.4, 3.9))
    xs = {"I1": 5, "I2": 6, "I3": 7}
    for h, t in T.items():
        if h == "R01":
            continue
        ax.plot(xs[t["corriente"]], t["fit_sech"]["tau_p"], "o", ms=8, color=VIOLET, mec="white", mew=1.2, zorder=3)
    ax.plot([5, 6, 7], [107, 76, 54], "_", ms=26, mew=3.5, color=RED, zorder=4)
    for c, v in zip((5, 6, 7), (107, 76, 54)):
        ax.text(c + 0.17, v, f"τ₀ = {v} fs", fontsize=10, color=RED, va="center")
    for c, k in zip((5, 6, 7), ("I1", "I2", "I3")):
        vals = [t["fit_sech"]["tau_p"] for h, t in T.items() if t["corriente"] == k and h != "R01"]
        ax.text(c + 0.17, np.mean(vals), f"media {np.mean(vals):.0f} fs\nn = {len(vals)}", fontsize=10, color=VIOLET, va="center")
    ax.plot([], [], "o", color=VIOLET, label="τp de cada traza (ajuste sech²)")
    ax.plot([], [], "_", ms=20, mew=3, color=RED, label="Hoja de pruebas de fábrica τ₀")
    ax.set_xticks([5, 6, 7])
    ax.set_xticklabels(["I₁ · 5 A", "I₂ · 6 A", "I₃ · 7 A"])
    ax.set_xlim(4.6, 7.9)
    ax.set_ylim(0, 240)
    ax.set_ylabel("Ancho de pulso τp (fs)", color=MUTED)
    ax.set_title("Piloto del 24 oct · 8 trazas válidas", loc="left", fontsize=11, color=INK)
    estilo(ax)
    ax.legend(loc="lower left", frameon=False, fontsize=9.5)
    fig.tight_layout()
    fig.savefig(out, dpi=220)
    plt.close(fig)


def fig_oc(R, out):
    d = R["d"]
    ns = np.arange(2, 21)
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(9.2, 3.6))
    pot = [potencia(int(n), d) for n in ns]
    a1.plot(ns, pot, "o-", color=VIOLET, ms=5)
    a1.axhline(0.90, color=RED, lw=1.2, ls="--")
    a1.axvline(R["n"], color=MUTED, lw=1, ls=":")
    a1.text(R["n"] + 0.3, 0.3, f"n = {R['n']}\npotencia {R['potencia_n']:.2f}".replace(".", ","), fontsize=10, color=INK)
    a1.text(2.2, 0.92, "potencia 0,90", color=RED, fontsize=9.5)
    a1.set_xlabel("Réplicas n por corriente", color=MUTED)
    a1.set_ylabel("Potencia 1 − β", color=MUTED)
    a1.set_title(f"d = δ/σ = 10 / {R['sigma']:.2f} = {d:.2f} · α = 0,05 · dos colas".replace(".", ","), loc="left", fontsize=10.5, color=INK)
    a1.set_ylim(0, 1.02)
    a1.set_xticks(range(2, 21, 2))
    estilo(a1)
    dd = [R["delta_det"][str(int(n))] for n in ns]
    a2.plot(ns, dd, "o-", color=VIOLET, ms=5)
    a2.axhline(10, color=RED, lw=1.2, ls="--")
    a2.text(13, 11, "δ que importa = 10 fs", color=RED, fontsize=9.5)
    for n_, yy in ((8, 26), (9, 20)):
        a2.annotate(f"n = {n_}: {R['delta_det'][str(n_)]:.1f} fs".replace(".", ","), (n_, R["delta_det"][str(n_)]),
                    xytext=(n_ + 2.5, yy), fontsize=9.5, color=INK,
                    arrowprops=dict(arrowstyle="-", color=MUTED, lw=0.8))
    a2.set_xlabel("Réplicas n por corriente", color=MUTED)
    a2.set_ylabel("Menor δ detectable (fs)", color=MUTED)
    a2.set_title("La misma curva leída al revés (potencia 0,90)", loc="left", fontsize=10.5, color=INK)
    a2.set_ylim(0, 45)
    a2.set_xticks(range(2, 21, 2))
    estilo(a2)
    fig.tight_layout()
    fig.savefig(out, dpi=220)
    plt.close(fig)


def fig_delta(R, out):
    sigma = R["sigma"]
    dd = np.linspace(2, 20, 73)
    fig, ax = plt.subplots(figsize=(6.4, 3.9))
    for n_, col, ls, lab in ((9, VIOLET, "-", "n = 9 (plan)"), (8, VIOLET, "--", "n = 8 (curva OC)"), (5, MUTED, ":", "n = 5 (piloto)")):
        ax.plot(dd, [potencia(n_, x / sigma) for x in dd], color=col, ls=ls, lw=2, label=lab)
    ax.axhline(0.90, color=RED, lw=1.2, ls="--")
    ax.axvline(10, color=RED, lw=1.2, ls="--")
    ax.text(2.3, 0.915, "potencia 0,90", color=RED, fontsize=9.5)
    ax.text(10.3, 0.16, "δ = 10 fs", color=RED, fontsize=9.5)
    p9 = potencia(9, 10 / sigma)
    ax.plot([10], [p9], "o", color=RED, ms=7, zorder=5)
    ax.annotate(f"{p9:.2f}".replace(".", ","), (10, p9), xytext=(12.5, 0.72), fontsize=10, color=INK,
                arrowprops=dict(arrowstyle="-", color=MUTED, lw=0.8))
    for t0 in (107, 76, 54):
        e = 0.0884 * t0
        ax.plot([e], [0.015], "^", color=INK, ms=7, zorder=5)
        ax.text(e, 0.06, f"{e:.1f}".replace(".", ","), ha="center", fontsize=8.5, color=INK)
    ax.plot([], [], "^", color=INK, ms=7, ls="none", label="error de la forma (8,8 %)")
    ax.set_xlabel("Diferencia δ frente a la hoja de fábrica (fs)", color=MUTED)
    ax.set_ylabel("Potencia 1 − β", color=MUTED)
    ax.set_title(f"Potencia de la t de una muestra contra δ · σ = {sigma:.2f} fs · α = 0,05 · dos colas".replace(".", ","), loc="left", fontsize=10.5, color=INK)
    ax.set_ylim(0, 1.02)
    ax.set_xlim(2, 20)
    estilo(ax)
    ax.legend(loc="lower right", frameon=False, fontsize=9)
    fig.tight_layout()
    fig.savefig(out, dpi=220)
    plt.close(fig)


if __name__ == "__main__":
    A = json.load(open(sys.argv[1]))
    os.makedirs(sys.argv[2], exist_ok=True)
    fig_traza(A["trazas"], os.path.join(sys.argv[2], "traza.png"))
    fig_piloto(A["trazas"], os.path.join(sys.argv[2], "piloto.png"))
    fig_oc(A["resumen"]["fit_sech|sin_R01"], os.path.join(sys.argv[2], "oc.png"))
    fig_delta(A["resumen"]["fit_sech|sin_R01"], os.path.join(sys.argv[2], "delta.png"))
    print("figuras en", sys.argv[2])
