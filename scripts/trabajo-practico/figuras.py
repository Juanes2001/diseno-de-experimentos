"""Figuras de la exposición del 17 oct 2026 (fundamentos del autocorrelador de intensidad).

Todas las curvas son simulaciones con las fórmulas que se citan en la presentación;
ninguna es un dato medido. Uso: python figuras.py <carpeta_salida>
"""
import os
import sys

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager
import numpy as np

# ------------------------------------------------------------------ estilo
FONT_FILE = "/mnt/c/Windows/Fonts/bahnschrift.ttf"
if os.path.exists(FONT_FILE):
    font_manager.fontManager.addfont(FONT_FILE)
    FAMILY = font_manager.FontProperties(fname=FONT_FILE).get_name()
else:  # sin la fuente de Windows se usa la de matplotlib
    FAMILY = "DejaVu Sans"

INK = "#0E1726"
MUTED = "#5F6B7A"
GRID = "#E3E7EE"
RED = "#D7263D"      # fundamental (≈800 nm)
VIOLET = "#5B3FD9"   # segundo armónico (≈400 nm)
GRAY = "#8A94A3"

plt.rcParams.update({
    "font.family": [FAMILY, "DejaVu Sans"],  # DejaVu cubre ≈, −, ₀ y ⁻ que no trae Bahnschrift
    "font.size": 13,
    "mathtext.fontset": "stix",
    "axes.edgecolor": GRAY,
    "axes.labelcolor": INK,
    "axes.linewidth": 0.8,
    "xtick.color": MUTED,
    "ytick.color": MUTED,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "axes.grid": True,
    "grid.color": GRID,
    "grid.linewidth": 0.8,
    "legend.frameon": False,
    "savefig.dpi": 200,
    "savefig.bbox": "tight",
    "savefig.pad_inches": 0.08,
})

LAMBDA = 0.8          # µm
C = 0.299792458       # µm/fs
W0 = 2 * np.pi * C / LAMBDA   # rad/fs
SECH_T = 1.7627       # τp = 1,7627 T para sech²


def sech2(t, tp):
    return 1 / np.cosh(t * SECH_T / tp) ** 2


def gauss(t, tp):
    return np.exp(-4 * np.log(2) * t ** 2 / tp ** 2)


def fwhm(x, y):
    y = y / y.max()
    idx = np.where(y >= 0.5)[0]
    return x[idx[-1]] - x[idx[0]]


def autocorr(t, inten):
    a = np.correlate(inten, inten, mode="same")
    return a / a.max()


def save(fig, out, name):
    fig.savefig(os.path.join(out, name + ".png"), transparent=False, facecolor="white")
    plt.close(fig)


# ------------------------------------------------------------------ figuras
def portada(out):
    """Pulso fundamental y su segundo armónico sobre fondo oscuro (decorativa)."""
    t = np.linspace(-120, 120, 6000)
    fig, ax = plt.subplots(figsize=(7.0, 4.2))
    fig.patch.set_alpha(0)
    ax.set_facecolor("none")
    env = np.sqrt(sech2(t, 30))
    for k, alpha in [(1.0, 1.0), (1.6, 0.22), (2.4, 0.08)]:
        ax.plot(t, env * np.cos(W0 * t), color=RED, lw=1.3 * k, alpha=alpha)
    env2 = sech2(t, 30 / np.sqrt(2))
    ax.plot(t, 0.55 * env2 * np.cos(2 * W0 * t) - 1.6, color="#8C79FF", lw=1.1)
    ax.fill_between(t, sech2(t, 30), -0.0, color=RED, alpha=0.10, lw=0)
    ax.axis("off")
    fig.savefig(os.path.join(out, "portada.png"), transparent=True)
    plt.close(fig)


def escala(out):
    fig, ax = plt.subplots(figsize=(11.6, 2.9))
    ax.set_xscale("log")
    ax.set_xlim(1, 1e6)
    ax.set_ylim(0, 4)
    ax.grid(False)
    ax.spines["left"].set_visible(False)
    ax.set_yticks([])
    ticks = [1, 10, 100, 1e3, 1e4, 1e5, 1e6]
    ax.set_xticks(ticks)
    ax.set_xticklabels(["1 fs", "10 fs", "100 fs", "1 ps", "10 ps", "100 ps", "1 ns"])
    bands = [
        (10, 100, 3.0, RED, "Pulso de un láser de femtosegundos\n(≈ 10–100 fs)"),
        (5e3, 5e4, 1.9, GRAY, "Osciloscopio rápido\n(≈ 5–50 ps)"),
        (1e4, 1e5, 0.8, INK, "Fotodiodo rápido\n(≈ 10–100 ps)"),
    ]
    for a, b, y, col, lab in bands:
        ax.barh(y, b - a, left=a, height=0.55, color=col, alpha=0.9)
        ax.text(b * 1.4, y, lab, va="center", ha="left", color=INK, fontsize=12.5)
    ax.axvline(2.67, color=VIOLET, lw=1.2, ls="--")
    ax.text(2.67 * 1.15, 3.75, "Periodo óptico a 800 nm: 2,7 fs", color=VIOLET, fontsize=11.5,
            va="center")
    ax.set_xlabel("Tiempo (escala logarítmica)")
    save(fig, out, "escala")


def pulso(out):
    t = np.linspace(-70, 70, 4000)
    tp = 30
    env = np.sqrt(gauss(t, tp))
    fig, ax = plt.subplots(figsize=(6.4, 4.2))
    ax.fill_between(t, gauss(t, tp), color=RED, alpha=0.12, lw=0)
    ax.plot(t, gauss(t, tp), color=RED, lw=2.2, label="Intensidad I(t)")
    ax.plot(t, env * np.cos(W0 * t), color=GRAY, lw=0.9, alpha=0.7, label="Campo E(t)")
    ax.plot(t, env, color=INK, lw=1.4, ls="--", label="Envolvente A(t)")
    ax.annotate("", xy=(tp / 2, 0.5), xytext=(-tp / 2, 0.5),
                arrowprops=dict(arrowstyle="<->", color=INK, lw=1.4))
    ax.text(0, 0.58, r"$\tau_p$ (FWHM)", ha="center", color=INK, fontsize=13,
            bbox=dict(boxstyle="round,pad=0.2", fc="white", ec="none"))
    ax.set_xlabel("Tiempo t (fs)")
    ax.set_ylabel("Amplitud normalizada")
    ax.set_ylim(-1.1, 1.25)
    ax.legend(loc="upper right", fontsize=11)
    save(fig, out, "pulso")


def fourier(out):
    t = np.linspace(-400, 400, 2 ** 14)
    dt = t[1] - t[0]
    nu = np.fft.fftshift(np.fft.fftfreq(t.size, dt)) * 1e3  # THz
    fig, axs = plt.subplots(2, 2, figsize=(7.2, 4.6), gridspec_kw=dict(hspace=0.55, wspace=0.3))
    for row, tp in enumerate([20, 100]):
        it = gauss(t, tp)
        spec = np.abs(np.fft.fftshift(np.fft.fft(np.sqrt(it)))) ** 2
        spec /= spec.max()
        axs[row, 0].plot(t, it, color=RED, lw=2)
        axs[row, 0].fill_between(t, it, color=RED, alpha=0.12, lw=0)
        axs[row, 0].set_xlim(-150, 150)
        axs[row, 0].set_title(f"Pulso de {tp} fs", fontsize=12.5, color=INK, loc="left")
        axs[row, 1].plot(nu, spec, color=VIOLET, lw=2)
        axs[row, 1].fill_between(nu, spec, color=VIOLET, alpha=0.12, lw=0)
        axs[row, 1].set_xlim(-60, 60)
        dnu = fwhm(nu, spec)
        axs[row, 1].set_title(f"Espectro: Δν ≈ {dnu:.0f} THz".replace(".", ","), fontsize=12.5,
                              color=INK, loc="left")
        for ax in axs[row]:
            ax.set_yticks([])
    axs[1, 0].set_xlabel("Tiempo (fs)")
    axs[1, 1].set_xlabel("Frecuencia − ν₀ (THz)")
    save(fig, out, "fourier")


def modos(out):
    t = np.linspace(0, 3, 3000)  # en periodos de ida y vuelta
    n = np.arange(-7, 8)
    rng = np.random.default_rng(4)
    fig, axs = plt.subplots(2, 1, figsize=(6.6, 4.4), sharex=True,
                            gridspec_kw=dict(hspace=0.45))
    for ax, phases, title, col in [
        (axs[0], np.zeros(n.size), "15 modos con la misma fase: tren de pulsos", RED),
        (axs[1], rng.uniform(0, 2 * np.pi, n.size), "15 modos con fases al azar: ruido", GRAY),
    ]:
        field = np.exp(1j * (2 * np.pi * np.outer(t, n) + phases)).sum(axis=1)
        inten = np.abs(field) ** 2 / n.size ** 2
        ax.plot(t, inten, color=col, lw=1.6)
        ax.fill_between(t, inten, color=col, alpha=0.12, lw=0)
        ax.set_title(title, fontsize=12.5, color=INK, loc="left")
        ax.set_ylim(0, 1.05)
        ax.set_yticks([0, 1])
    axs[1].set_xlabel("Tiempo (en unidades del tiempo de ida y vuelta 2nL/c)")
    axs[0].annotate("", xy=(2, 1.0), xytext=(1, 1.0),
                    arrowprops=dict(arrowstyle="<->", color=INK, lw=1.2))
    axs[0].text(1.5, 0.82, "T = 2nL/c", ha="center", color=INK, fontsize=12)
    save(fig, out, "modos")


def gdd(out):
    g = np.linspace(0, 2000, 400)
    fig, ax = plt.subplots(figsize=(6.6, 4.3))
    for tp, col, dy in [(20, RED, 0), (30, VIOLET, 0), (50, INK, 8), (100, GRAY, -8)]:
        tout = tp * np.sqrt(1 + (4 * np.log(2) * g / tp ** 2) ** 2)
        ax.plot(g, tout, color=col, lw=2.2)
        ax.text(2030, tout[-1] + dy, f"{tp} fs", color=col, fontsize=12.5, va="center")
    ax.axvline(450, color=MUTED, lw=1.2, ls="--")
    ax.text(470, 270, "1 cm de BK7\n(≈ 450 fs²)", color=MUTED, fontsize=11.5, va="top")
    ax.set_xlim(0, 2200)
    ax.set_ylim(0, 300)
    ax.set_xlabel("Dispersión acumulada GDD (fs²)")
    ax.set_ylabel(r"Ancho de salida $\tau_{sal}$ (fs)")
    ax.set_title("Ancho de entrada (pulso gaussiano sin chirp)", fontsize=12, color=MUTED, loc="left")
    save(fig, out, "gdd")


def sinc(out):
    dk = np.linspace(-80, 80, 4000)  # mm⁻¹
    fig, ax = plt.subplots(figsize=(6.0, 3.6))
    for L, col, lab in [(0.1, VIOLET, "L = 0,1 mm"), (1.0, RED, "L = 1 mm")]:
        y = np.sinc(dk * L / 2 / np.pi) ** 2
        ax.plot(dk, y, color=col, lw=2.2)
        ax.fill_between(dk, y, color=col, alpha=0.10, lw=0)
    ax.text(-80, 1.42, "L = 0,1 mm: acepta más ancho de banda", color=VIOLET, fontsize=12,
            va="top")
    ax.text(-80, 1.26, "L = 1 mm: banda angosta, pero señal $\\propto$ L² (100 veces más)",
            color=RED, fontsize=12, va="top")
    ax.set_xlabel("Desajuste de fase Δk (mm⁻¹)")
    ax.set_ylabel(r"sinc$^2(\Delta k L/2)$")
    ax.set_ylim(0, 1.45)
    ax.set_yticks([0, 0.5, 1])
    save(fig, out, "sinc")


def trazas(out):
    tp = 20.0
    t = np.linspace(-250, 250, 2 ** 13)
    dt = t[1] - t[0]
    a = np.sqrt(sech2(t, tp)).astype(complex)
    taus = np.linspace(-60, 60, 1201)
    shift = lambda tau: np.interp(t - tau, t, a.real)  # envolvente real (pulso sin chirp)
    i4 = (np.abs(a) ** 4).sum() * dt
    bgfree, inten, interf = [], [], []
    for tau in taus:
        b = shift(tau)
        ac = (np.abs(a) ** 2 * b ** 2).sum() * dt / i4
        bgfree.append(ac)
        inten.append(1 + 2 * ac)
        e = a + b * np.exp(-1j * W0 * tau)
        interf.append((np.abs(e) ** 4).sum() * dt / (2 * i4))
    fig, axs = plt.subplots(1, 3, figsize=(12.4, 3.5), sharex=True,
                            gridspec_kw=dict(wspace=0.28))
    data = [
        (bgfree, "No colineal: sin fondo", (0, 1.15), VIOLET, None),
        (inten, "Colineal promediada: 3:1", (0, 3.4), VIOLET, 3),
        (interf, "Interferométrica: 8:1", (0, 8.8), VIOLET, 8),
    ]
    for ax, (y, title, ylim, col, peak) in zip(axs, data):
        ax.plot(taus, y, color=col, lw=1.0 if peak == 8 else 2.2)
        ax.set_ylim(*ylim)
        ax.set_title(title, fontsize=13, color=INK, loc="left")
        ax.set_xlabel("Retardo τ (fs)")
        if peak:
            ax.axhline(1, color=MUTED, lw=1, ls="--")
            ax.text(-58, 1.25 if peak == 3 else 0.35, "fondo = 1", color=MUTED, fontsize=11)
    axs[0].set_ylabel("Señal normalizada")
    save(fig, out, "trazas")


def deconv(out):
    tac = 100.0
    t = np.linspace(-160, 160, 3000)
    ac = sech2(t, tac / 1.543)  # no exacto: solo ilustración de la forma
    # traza de autocorrelación exacta de un sech² con τ_AC = 100 fs
    tp_s = tac / 1.543
    x = t * SECH_T / tp_s
    with np.errstate(invalid="ignore", divide="ignore"):
        acs = 3 * (x * np.cosh(x) - np.sinh(x)) / np.sinh(x) ** 3
    acs[np.isnan(acs)] = 1.0
    fig, ax = plt.subplots(figsize=(6.2, 4.0))
    ax.fill_between(t, acs, color=GRAY, alpha=0.18, lw=0)
    ax.plot(t, acs, color=GRAY, lw=2.2)
    ax.plot(t, gauss(t, tac / 1.414), color=INK, lw=2, ls="--")
    ax.plot(t, sech2(t, tp_s), color=RED, lw=2.2)
    ax.text(62, 0.62, "Traza medida\nτ_AC = 100 fs", color=MUTED, fontsize=12)
    ax.text(-160, 0.95, "Gaussiano:\nτp = 70,7 fs", color=INK, fontsize=12, va="top")
    ax.text(-160, 0.68, "sech²:\nτp = 64,8 fs", color=RED, fontsize=12, va="top")
    ax.set_xlabel("Tiempo o retardo (fs)")
    ax.set_yticks([0, 0.5, 1])
    ax.set_ylim(0, 1.05)
    save(fig, out, "deconv")
    del ac


def artefacto(out):
    """Tren de pulsos inestables: cada pulso es una ráfaga de ruido de ≈150 fs con
    subestructura de ≈15 fs que cambia de un pulso al siguiente (Ratner et al. 2012)."""
    t = np.linspace(-500, 500, 4001)
    dt = t[1] - t[0]
    rng = np.random.default_rng(7)
    kern = np.exp(-4 * np.log(2) * (np.arange(-60, 61) * dt) ** 2 / 15 ** 2)
    acc = np.zeros_like(t)
    for _ in range(300):
        noise = rng.normal(size=t.size) + 1j * rng.normal(size=t.size)
        e = np.sqrt(gauss(t, 150)) * np.convolve(noise, kern, mode="same")
        i = np.abs(e) ** 2
        acc += np.correlate(i, i, mode="same")
    acc /= acc.max()
    fig, ax = plt.subplots(figsize=(6.2, 3.9))
    ax.fill_between(t, acc, color=VIOLET, alpha=0.14, lw=0)
    ax.plot(t, acc, color=VIOLET, lw=2.2)
    ax.set_xlim(-400, 400)
    ax.set_ylim(0, 1.08)
    ax.annotate("Pico angosto (artefacto coherente):\nsolo la subestructura, ≈ 15 fs", xy=(8, 0.9),
                xytext=(60, 0.88), color=INK, fontsize=12,
                arrowprops=dict(arrowstyle="-", color=INK, lw=1))
    ax.annotate("Pedestal ancho: la duración\nreal del pulso, ≈ 150 fs", xy=(165, 0.12),
                xytext=(170, 0.62), color=VIOLET, fontsize=12,
                arrowprops=dict(arrowstyle="-", color=VIOLET, lw=1))
    ax.set_xlabel("Retardo τ (fs)")
    ax.set_ylabel("Señal promediada")
    save(fig, out, "artefacto")


def ishikawa(out):
    fig, ax = plt.subplots(figsize=(12.4, 5.0))
    ax.set_xlim(0, 12.4)
    ax.set_ylim(0, 5.0)
    ax.axis("off")
    ax.annotate("", xy=(9.75, 2.5), xytext=(0.3, 2.5),
                arrowprops=dict(arrowstyle="-|>", color=INK, lw=2.2, mutation_scale=22))
    ax.text(9.85, 2.5, "Ancho de pulso\nmedido τp", fontsize=15, color="white", va="center",
            ha="left", fontweight="bold",
            bbox=dict(boxstyle="round,pad=0.5", fc=RED, ec="none"))
    bones = [
        (1.6, "Fuente", ["Bombeo", "Alineación", "Calentamiento"], 1),
        (4.3, "Propagación", ["Vidrio (GDD)", "Compresor", "Automodulación (SPM)"], 1),
        (7.0, "Proceso no lineal", ["Espesor del cristal", "Ángulo de fase", "Potencia"], 1),
        (1.6, "Geometría y retardo", ["Calibración", "Ángulo de cruce", "Superposición"], -1),
        (4.3, "Detección", ["Saturación", "Ruido", "Pulsos promediados"], -1),
        (7.0, "Interpretación", ["Forma supuesta", "Método de ajuste", "Nivel del fondo"], -1),
    ]
    for x, name, causes, side in bones:
        y0, y1 = 2.5, 2.5 + side * 2.0
        ax.plot([x + 1.3, x], [y0, y1], color=GRAY, lw=1.6)
        ax.text(x - 0.05, y1 + side * 0.22, name, fontsize=14, color=VIOLET, ha="left",
                va="center", fontweight="bold")
        for k, c in enumerate(causes):
            frac = (k + 1) / (len(causes) + 1)
            yy = y1 + (y0 - y1) * frac
            xx = x + 1.3 * frac
            ax.plot([xx - 0.35, xx], [yy, yy], color=GRAY, lw=1.0)
            ax.text(xx - 0.4, yy, c, fontsize=11.5, color=INK, ha="right", va="center")
    save(fig, out, "ishikawa")


FIGURAS = [portada, escala, pulso, fourier, modos, gdd, sinc, trazas, deconv, artefacto, ishikawa]

if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else "figuras"
    os.makedirs(out, exist_ok=True)
    for f in FIGURAS:
        f(out)
        print("figura:", f.__name__)
