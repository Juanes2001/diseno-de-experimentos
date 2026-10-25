"""Informe del piloto del 24 oct 2026: resultados por traza, revisión del libro y número de réplicas.

Uso: .venv/bin/python render_informe_piloto.py <analisis.json> <salida.html>
(El PDF se imprime con Chrome; ver build_informe_piloto.sh.)
"""
import base64
import io
import json
import sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

sys.path.insert(0, __file__.rsplit("/", 1)[0])
from analiza_piloto import CONV, F_GAUSS, F_SECH, TAU0, g_gauss, g_sech2, potencia  # noqa: E402

AZUL, NARANJA, AQUA = "#2a78d6", "#eb6834", "#1baf7a"
TINTA, TINTA2, GRIS, REJILLA = "#0b0b0b", "#52514e", "#8a8984", "#e1e0d9"
CUR = {"I1": "5 A", "I2": "6 A", "I3": "7 A"}
FECHA = "24 de octubre de 2026"

CSS = """
@page { size: A4; margin: 18mm 16mm; }
body { font-family: Arial, Helvetica, sans-serif; font-size: 10.5pt; color: #0b0b0b; line-height: 1.38; }
h1 { font-size: 20pt; color: #1F3864; margin: 0 0 4px; line-height: 1.2; }
h2 { font-size: 14pt; color: #1F3864; border-bottom: 2px solid #1F3864; padding-bottom: 2px; margin: 22px 0 8px; page-break-after: avoid; }
h3 { font-size: 11.5pt; color: #1F3864; margin: 14px 0 4px; page-break-after: avoid; }
p { margin: 5px 0; }
.meta { color: #52514e; font-size: 9.5pt; }
.frase { background: #eef3fb; border-left: 4px solid #1F3864; padding: 8px 12px; margin: 14px 0; }
.ojo { background: #fff4e5; border-left: 4px solid #eb6834; padding: 8px 12px; margin: 10px 0; }
.ok { background: #e8f6ef; border-left: 4px solid #1baf7a; padding: 8px 12px; margin: 10px 0; }
table { border-collapse: collapse; width: 100%; margin: 6px 0 10px; font-size: 9.5pt; page-break-inside: avoid; }
th { background: #1F3864; color: #fff; padding: 4px 6px; text-align: center; font-weight: bold; }
td { border: 1px solid #c9c8c0; padding: 3px 6px; text-align: right; }
td.l, th.l { text-align: left; }
td.c { text-align: center; }
tr.tot td { font-weight: bold; background: #f3f3f0; }
.fig { text-align: center; margin: 8px 0 4px; page-break-inside: avoid; }
.fig img { max-width: 100%; }
.pie { font-size: 9pt; color: #52514e; text-align: left; margin: 2px 0 10px; }
.nota { font-size: 9pt; color: #52514e; }
.salto { page-break-before: always; }
ol, ul { margin: 4px 0 6px 18px; padding: 0; }
li { margin: 2px 0; }
.kv td:first-child { text-align: left; width: 38%; }
"""


def png(fig):
    buf = io.BytesIO()
    fig.savefig(buf, format="png", dpi=170, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    return "data:image/png;base64," + base64.b64encode(buf.getvalue()).decode()


def estilo(ax):
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    for s in ("left", "bottom"):
        ax.spines[s].set_color("#c3c2b7")
    ax.tick_params(colors=TINTA2, labelsize=8)
    ax.grid(axis="y", color=REJILLA, linewidth=0.6)
    ax.set_axisbelow(True)


def fig_trazas(trazas, validas):
    fig, axs = plt.subplots(4, 2, figsize=(9.0, 9.4))
    for ax, hoja in zip(axs.flat, validas):
        t = trazas[hoja]
        x, y = np.array(t["x"]), np.array(t["y"])
        tau = x * CONV
        esc = 10 ** np.floor(np.log10(max(y.max(), 1e-12)))
        ax.plot(tau, y / esc, "o", ms=4, color=TINTA2, mfc="white", mew=1.1, label="Lecturas", zorder=3)
        tt = np.linspace(tau.min(), tau.max(), 400)
        for clave, g, col, nombre in (("fit_sech", g_sech2, AZUL, "Ajuste sech²"), ("fit_gauss", g_gauss, NARANJA, "Ajuste gaussiano")):
            f = t[clave]
            ax.plot(tt, (f["B"] + f["A"] * g(tt - f["centro"], f["tau_p"])) / esc, color=col, lw=1.8, label=nombre)
        ax.set_title(f"{hoja} · {t['corriente']} ({CUR[t['corriente']]}) · τ₀ = {TAU0[t['corriente']]:.0f} fs\n"
                     f"τp sech² {t['fit_sech']['tau_p']:.0f} fs · gauss {t['fit_gauss']['tau_p']:.0f} fs · R² {t['fit_sech']['r2']:.3f} / {t['fit_gauss']['r2']:.3f}",
                     fontsize=8, color=TINTA, loc="left")
        ax.set_xlabel("Retardo τ (fs)", fontsize=8, color=TINTA2)
        ax.set_ylabel(f"Potencia (×{esc:.0e} W)", fontsize=7.5, color=TINTA2)
        estilo(ax)
    h, l = axs.flat[0].get_legend_handles_labels()
    fig.legend(h, l, loc="lower center", ncol=3, frameon=False, fontsize=9, bbox_to_anchor=(0.5, -0.01))
    fig.tight_layout(rect=(0, 0.03, 1, 1))
    return png(fig)


def fig_corrientes(trazas, validas):
    fig, ax = plt.subplots(figsize=(7.2, 3.9))
    xs = {"I1": 5, "I2": 6, "I3": 7}
    for clave, col, nombre, dx in (("fit_sech", AZUL, "Ajuste sech² (cada traza)", -0.08), ("fit_gauss", NARANJA, "Ajuste gaussiano (cada traza)", 0.08)):
        for hoja in validas:
            t = trazas[hoja]
            ax.plot(xs[t["corriente"]] + dx, t[clave]["tau_p"], "o", ms=6, color=col, mec="white", mew=1, zorder=3,
                    label=nombre if hoja == validas[0] else None)
    ax.plot([5, 6, 7], [107, 76, 54], "_", ms=22, mew=3, color=TINTA, label="Hoja de pruebas de fábrica (τ₀)", zorder=4)
    for c, v in zip((5, 6, 7), (107, 76, 54)):
        ax.text(c + 0.2, v, f"τ₀ = {v} fs", fontsize=8, color=TINTA2, va="center")
    ax.set_xticks([5, 6, 7])
    ax.set_xticklabels(["I1 · 5 A", "I2 · 6 A", "I3 · 7 A"])
    ax.set_xlim(4.5, 7.7)
    ax.set_ylim(0, 240)
    ax.set_ylabel("Ancho de pulso τp (fs)", fontsize=9, color=TINTA2)
    estilo(ax)
    ax.legend(loc="upper right", frameon=False, fontsize=8)
    fig.tight_layout()
    return png(fig)


def f1(v, nd=1):
    return "—" if v is None else f"{v:.{nd}f}".replace(".", ",")


def build(analisis, salida):
    A = json.load(open(analisis))
    T, R, TI = A["trazas"], A["resumen"], A["tiempos"]
    validas = [h for h in T if h != "R01"]       # R08–R15; R01 excluida (sin señal de autocorrelación)
    reales = validas
    rs = R["fit_sech|sin_R01"]
    rg = R["fit_gauss|sin_R01"]
    rfs = R["fwhm_sech|sin_R01"]
    rfg = R["fwhm_gauss|sin_R01"]
    min_traza = TI["entre_inicios_media"]
    cabe_dia = int(5 * 60 / min_traza)
    n = rs["n"]
    rpd3, rpd4 = -(-n // 3), -(-n // 4)
    o = [f"<!doctype html><html lang='es'><head><meta charset='utf-8'><title>Informe del piloto · réplicas</title><style>{CSS}</style></head><body>"]
    w = o.append

    # ---------------------------------------------------------------- portada
    w("<h1>Piloto del 24 de octubre: resultados, revisión del libro de cálculo y número de réplicas para la semana</h1>")
    w(f"<p class='meta'>Trabajo práctico · Diseño de Experimentos Avanzados (3008475) · Universidad Nacional de Colombia · 2026-II<br>"
      f"Juan Esteban Rodríguez Ochoa · Sebastián Zapata Henao · {FECHA}</p>")
    w(f"<div class='frase'><b>En una frase.</b> Con las {len(reales)} trazas válidas del piloto (R08–R15), la desviación estándar del ancho "
      f"de pulso es de 2 a 5 fs; para detectar una diferencia de 10 fs con α = 0,05 y potencia 0,90 hacen falta "
      f"<b>{n} réplicas por corriente</b> (ajuste sech² o gaussiano; {rfs['n']} si se usa el ancho a media altura). A {f1(min_traza)} min por "
      f"traza caben {cabe_dia} trazas en un día de 5 h, así que el plan de tres días (lunes a miércoles) con <b>{rpd3} réplicas por corriente y por "
      f"día</b> ({3 * rpd3 * 3} trazas en la semana, unos {f1(3 * rpd3 * min_traza, 0)} min de medición al día) sobra. "
      f"Las medias medidas (≈ {rs['por_corriente']['I1']['media']:.0f}, {rs['por_corriente']['I2']['media']:.0f} y {rs['por_corriente']['I3']['media']:.0f} fs) "
      f"están muy por encima de la hoja de fábrica (107, 76 y 54 fs); eso no cambia el n, pero sí lo que hay que revisar antes del lunes.</div>")

    # ---------------------------------------------------------------- 1 resumen
    w("<h2>1. Resumen</h2>")
    w("<table class='kv'>")
    for k, v in [
        ("Trazas tomadas / usadas", f"15 / {len(reales)} (R08–R15). R01–R07 excluidas: R02–R07 por error de medición; R01 porque no registró señal de autocorrelación (potencia diez veces menor y sin pico)."),
        ("Muestreo real", "Paso de 10 µm = 66,7 fs; 17–22 lecturas por traza; 4–5 lecturas dentro del ancho a media altura."),
        ("Estimadores de τp", "Ancho a media altura (FWHM) × 0,65 (sech²) o × 0,7071 (gaussiano); y ajuste por mínimos cuadrados de la autocorrelación completa, sech² y gaussiana."),
        ("Medias por corriente, ajuste sech² (gaussiano)", " · ".join(f"{c} {CUR[c]}: {rs['por_corriente'][c]['media']:.0f} ({rg['por_corriente'][c]['media']:.0f}) fs, n = {rs['por_corriente'][c]['n']}" for c in ("I1", "I2", "I3"))),
        ("Hoja de fábrica τ₀", "5 A: 107 fs · 6 A: 76 fs · 7 A: 54 fs"),
        ("σ para el diseño", f"{f1(rs['sigma'], 2)} fs = 1,558 × S mayor ({f1(rs['S_max'], 2)} fs, {rs['corriente_S_max']}, n = {rs['n_S_max']}); ajuste sech². Gaussiano: {f1(rg['sigma'], 2)} fs."),
        ("δ · α · potencia · colas", "10 fs · 0,05 · 0,90 · 2 (protocolo, sección 4)"),
        ("n por corriente", f"<b>{n}</b> (ajuste sech²; gaussiano {rg['n']}; FWHM {rfs['n']}–{rfg['n']})"),
        ("Tiempo por traza", f"{f1(min_traza)} min entre inicios de trazas válidas consecutivas (R08–R15); {cabe_dia} trazas por día de 5 h"),
        ("Plan recomendado", f"3 días (lun 26 – mié 28): {rpd3} réplicas por corriente y por día, {3 * rpd3} trazas/día en orden sorteado, n = {3 * rpd3} por corriente, δ detectable {f1(rs['delta_det'][str(3 * rpd3)])} fs"),
    ]:
        w(f"<tr><td>{k}</td><td class='l'>{v}</td></tr>")
    w("</table>")

    # ---------------------------------------------------------------- 2 qué se midió
    w("<h2>2. Qué se midió</h2>")
    w("<p>Se tomaron las 15 trazas del piloto en el orden sorteado, a mano con el micrómetro: posición en µm y potencia óptica en W leída en el "
      "medidor. El paso fue de 10 µm (66,7 fs de retardo) en todas: la resolución del micrómetro no permitió el paso fino de la guía "
      "(2 a 4 µm). Por eso cada traza tiene solo 4 o 5 lecturas dentro del ancho a media altura y el libro marcó el aviso «pocas lecturas». "
      "Con ese muestreo, el ancho a media altura se lee interpolando entre lecturas separadas 67 fs; el ajuste por mínimos cuadrados usa todos los "
      "puntos de la traza y es la lectura más estable con pasos gruesos. Se reportan los dos.</p>")
    w("<table><tr><th>Traza</th><th>Corriente</th><th>Inicio</th><th>Fin</th><th>Lecturas</th><th>Estado</th></tr>")
    for h, t in A["registro"].items():
        est = "descartada por el equipo" if h in ("R02", "R03", "R04", "R05", "R06", "R07") else ("excluida: sin señal de autocorrelación" if h == "R01" else "usada")
        pts = T[h]["puntos"] if h in T else "—"
        w(f"<tr><td class='c'>{h}</td><td class='c'>{t['corriente']} ({CUR[t['corriente']]})</td><td class='c'>{(t['inicio'] or '')[:5]}</td>"
          f"<td class='c'>{(t['fin'] or '')[:5]}</td><td>{pts}</td><td class='l'>{est}</td></tr>")
    w("</table>")

    # ---------------------------------------------------------------- 3 R01 y revisión del libro
    w("<h2>3. Revisión del libro de cálculo</h2>")
    w("<p>Se comparó el libro usado, celda por celda, con uno recién generado por el mismo programa. Las únicas entradas del equipo son los "
      "datos de las columnas A y B de cada traza, las horas del Registro y la nota «R02 a R07 Descartar». Hallazgos en las celdas con fórmula:</p>")
    w("<table><tr><th>#</th><th class='l'>Hallazgo</th><th class='l'>Efecto</th><th class='l'>Corrección en la copia</th></tr>")
    for i, (a, b, c) in enumerate([
        ("R02–R07 seguían marcadas «Sí» en la columna ¿Válida? del Registro (la nota las descartaba, pero la fórmula lee la columna, no la nota).",
         "El Resumen y Réplicas las incluían: I2 con n = 4 y S = 46 fs → σ = 79 fs → «n > 100».", "Marcadas «No» con la causa en Observaciones."),
        ("La duración media por traza se calculaba con las 15 trazas (de la primera a la última hora de inicio).",
         "7,5 min por traza, contaminado por las descartadas.", "Nueva columna M «Δ inicio a la siguiente»: solo pares de trazas válidas consecutivas. Da 6,1 min."),
        ("El fondo de cada traza usaba el conteo de la columna A para ubicar las últimas lecturas de la columna B.",
         "En R07 (17 posiciones y 13 potencias) daba #DIV/0! en toda la hoja.", "El fondo usa el conteo de la columna B; R07 queda en «Revisar: columnas con distinto número de datos»."),
        ("R14!D5 tenía ISNUMBER(B3) en vez de ISNUMBER(B5) (edición accidental).", "Ninguno: B3 también tiene dato.", "Fórmula restaurada."),
        ("Las celdas «Fondo» y «Máximo» mostraban 0,000 porque el formato era de tres decimales y las potencias leídas son del orden de 10⁻⁵.",
         "Solo de presentación: la normalización no depende de la unidad.", "Formato científico y etiqueta en W (el medidor se leyó en W, no en µW); el cálculo no cambia."),
        ("El n de Réplicas no tenía forma de usar otro estimador que el ancho a media altura × 0,65.", "No se podía comparar sech² con gaussiano ni FWHM con ajuste.",
         "Hoja nueva «Ajustes» con los cuatro estimadores por traza y un selector en Configuración («Estimador de τp»); el Resumen, Réplicas y Plan semana siguen al elegido."),
    ], 1):
        w(f"<tr><td class='c'>{i}</td><td class='l'>{a}</td><td class='l'>{b}</td><td class='l'>{c}</td></tr>")
    w("</table>")
    # ---------------------------------------------------------------- 4 por traza
    w("<h2>4. Resultados por traza</h2>")
    w("<p>Para cada traza: Δτ<sub>AC</sub> es el ancho a media altura de la autocorrelación leído por el libro (fondo de 2 lecturas por ala, "
      "cruces a 0,5 interpolados). El ajuste busca por mínimos cuadrados los cuatro parámetros de B + A·g(τ − τ<sub>c</sub>; τ<sub>p</sub>), con g la "
      "autocorrelación de intensidad de un pulso sech² o de un pulso gaussiano; ± SE es el error estándar del ajuste y R² su bondad.</p>")
    w("<table><tr><th>Traza</th><th>Corriente</th><th>Lecturas</th><th>En el FWHM</th><th>Δτ<sub>AC</sub> (fs)</th><th>τp FWHM sech² (fs)</th><th>τp FWHM gauss (fs)</th>"
      "<th>τp ajuste sech² (fs)</th><th>± SE</th><th>R²</th><th>τp ajuste gauss (fs)</th><th>± SE</th><th>R²</th></tr>")
    for h in validas:
        t = T[h]
        w(f"<tr><td class='c'>{h}</td><td class='c'>{t['corriente']} ({CUR[t['corriente']]})</td><td>{t['puntos']}</td><td>{t['lect_fwhm']}</td><td>{f1(t['fwhm_py'])}</td>"
          f"<td>{f1(t['taup_fwhm_sech'])}</td><td>{f1(t['taup_fwhm_gauss'])}</td><td><b>{f1(t['fit_sech']['tau_p'])}</b></td><td>{f1(t['fit_sech']['se_tau_p'])}</td>"
          f"<td>{f1(t['fit_sech']['r2'], 3)}</td><td><b>{f1(t['fit_gauss']['tau_p'])}</b></td><td>{f1(t['fit_gauss']['se_tau_p'])}</td><td>{f1(t['fit_gauss']['r2'], 3)}</td></tr>")
    w("</table>")
    w(f"<div class='fig'><img src='{fig_trazas(T, validas)}'><p class='pie'><b>Figura 1.</b> Las ocho trazas válidas con los dos ajustes. "
      "Potencia en W, como la da el medidor (escala en cada eje).</p></div>")

    # ---------------------------------------------------------------- 5 por corriente
    w("<h2>5. Resultado por corriente frente a la hoja de fábrica</h2>")
    w("<table><tr><th>Corriente</th><th>τ₀ fábrica (fs)</th><th>n</th><th>FWHM sech²: media (S)</th><th>Ajuste sech²: media (S)</th><th>FWHM gauss: media (S)</th><th>Ajuste gauss: media (S)</th><th>Ajuste sech² − τ₀ (fs)</th><th>Razón</th></tr>")
    for c in ("I1", "I2", "I3"):
        p = [r["por_corriente"][c] for r in (rfs, rs, rfg, rg)]
        cel = lambda q: f"{f1(q['media'])} ({f1(q['S'], 2)})" if q['S'] is not None else f"{f1(q['media'])} (—)"
        w(f"<tr><td class='c'>{c} · {CUR[c]}</td><td>{TAU0[c]:.0f}</td><td>{p[1]['n']}</td><td>{cel(p[0])}</td><td><b>{cel(p[1])}</b></td><td>{cel(p[2])}</td><td><b>{cel(p[3])}</b></td>"
          f"<td>{f1(p[1]['dif'])}</td><td>{f1(p[1]['media'] / TAU0[c], 2)}</td></tr>")
    w("</table>")
    w(f"<div class='fig'><img src='{fig_corrientes(T, reales)}'><p class='pie'><b>Figura 2.</b> τp de cada traza válida con los dos ajustes y el valor de la hoja de fábrica.</p></div>")
    w("<p>Dos cosas se ven de inmediato. (1) <b>La dispersión entre trazas es pequeña</b>: en I1, con cinco trazas, S = 3 a 5 fs según el estimador "
      "(CV ≈ 2 %); en I3, con dos, 2 a 3 fs. Esa es la variabilidad que fija el número de réplicas y es buena noticia. (2) <b>Las medias están 1,9 a 2,8 veces por encima "
      "de la hoja de fábrica</b>, y la razón crece hacia las corrientes altas (pulsos más cortos). Con S de pocos fs, cualquier prueba t rechazará "
      "H<sub>0</sub>: μ = τ₀ con valores P minúsculos, sea cual sea el n. La pregunta que vale es si esa diferencia es del láser o del montaje: un pulso de 54 fs se "
      "ensancha mucho más que uno de 107 fs al atravesar vidrio (divisor, lente, cristal, ventanas), y ese patrón —más ensanchamiento cuanto más corto el "
      "pulso— es justo el que se observa. También conviene confirmar el factor 2 de la conversión posición → retardo (τ = 2Δx/c): si el brazo móvil "
      "tuviera un recorrido óptico distinto, todos los anchos cambiarían en la misma proporción, lo que no explica por sí solo que la razón cambie con la corriente.</p>")
    w("<p>Nada de esto altera el cálculo de réplicas, que depende solo de S. Sí conviene dejarlo escrito desde ya como pregunta abierta del informe final.</p>")

    # ---------------------------------------------------------------- 6 réplicas
    w("<h2 class='salto'>6. Número de réplicas para la semana</h2>")
    w("<p>Método del protocolo (sección 4; Montgomery, sec. 2-4.2): σ conservadora = límite superior de confianza del 80 % de la S mayor del piloto; "
      "δ = 10 fs (regla 5: la hoja de fábrica no trae tolerancia ni incertidumbre del ancho; en 7 A la regla 2 daría 26 fs, pero manda la menor); "
      "α = 0,05, potencia 0,90, dos colas (τ₀ es un valor medido). n se lee en la curva OC de la prueba t de una muestra; aquí se calculó con la "
      "distribución t no central exacta y se comprobó que el libro (aproximación normal) da el mismo n.</p>")
    w("<table><tr><th class='l'>Estimador</th><th>S por corriente I1 / I2 / I3 (fs)</th><th>S mayor (corriente, n)</th><th>Factor</th><th>σ (fs)</th><th>d = δ/σ</th><th>n por corriente</th><th>Potencia con ese n</th></tr>")
    for nombre, r in (("FWHM × 0,65 (sech²)", rfs), ("FWHM × 0,7071 (gaussiano)", rfg), ("Ajuste sech²", rs), ("Ajuste gaussiano", rg)):
        ss = " / ".join(f1(r["por_corriente"][c]["S"], 2) for c in ("I1", "I2", "I3"))
        w(f"<tr><td class='l'>{nombre}</td><td class='c'>{ss}</td><td class='c'>{f1(r['S_max'], 2)} ({r['corriente_S_max']}, {r['n_S_max']})</td><td>{f1(r['factor'], 3)}</td>"
          f"<td>{f1(r['sigma'], 2)}</td><td>{f1(r['d'], 2)}</td><td><b>{r['n']}</b></td><td>{f1(r['potencia_n'], 3)}</td></tr>")
    w("</table>")
    w("<h3>Qué diferencia detecta cada n</h3>")
    w("<p>La misma curva, leída al revés: con un n fijo, la menor diferencia que se detecta con α = 0,05 y potencia 0,90 (σ del ajuste sech²; entre paréntesis, gaussiano).</p>")
    ks = [str(k) for k in (4, 5, 6, 8, 9, 10, 12, 15, 20)]
    w("<table><tr><th class='l'>n por corriente</th>" + "".join(f"<th>{k}</th>" for k in ks) + "</tr>")
    w("<tr><td class='l'>δ detectable (fs)</td>" + "".join(f"<td>{f1(rs['delta_det'][k])} ({f1(rg['delta_det'][k])})</td>" for k in ks) + "</tr></table>")
    w("<h3>Tiempo y reparto en la semana</h3>")
    w(f"<p>Entre el inicio de una traza válida y el de la siguiente (R08 a R15, incluye cambio de corriente y anotación) pasaron "
      f"{', '.join(str(x) for x in TI['entre_inicios_R08_R15'])} min: <b>{f1(min_traza)} min por traza</b>. Con 5 h útiles al día caben {cabe_dia} trazas. "
      f"Las {3 * n} trazas de n = {n} se tomarían en un solo día; el protocolo reparte n por igual entre tres días para que el día quede balanceado "
      f"(y se pueda bloquear si hiciera falta), así que:</p>")
    w("<table><tr><th class='l'>Plan</th><th>Réplicas por corriente y por día</th><th>Trazas por día</th><th>Minutos de medición al día</th><th>n por corriente</th><th>Trazas en la semana</th><th>δ detectable (fs)</th></tr>")
    for dias, rpd in ((3, rpd3), (4, rpd4)):
        nn = rpd * dias
        w(f"<tr{' class=tot' if dias == 3 else ''}><td class='l'>{dias} días ({'lun 26 – mié 28' if dias == 3 else 'lun 26 – jue 29'})</td><td>{rpd}</td><td>{3 * rpd}</td>"
          f"<td>{f1(3 * rpd * min_traza, 0)}</td><td>{nn}</td><td>{3 * nn}</td><td>{f1(rs['delta_det'].get(str(nn)))}</td></tr>")
    w("</table>")
    w(f"<div class='ok'><b>Recomendación.</b> Tres días, {rpd3} réplicas por corriente y por día ({3 * rpd3} trazas/día, ≈ {f1(3 * rpd3 * min_traza, 0)} min), orden "
      f"completamente sorteado cada día (hoja Plan semana de la copia). Se alcanza n = {3 * rpd3} ≥ {n} y la diferencia detectable baja a "
      f"{f1(rs['delta_det'].get(str(3 * rpd3)))} fs. Como sobra tiempo, el jueves 29 queda de reserva para reponer trazas que fallen o, mejor, para las "
      "comprobaciones de la sección 7.</div>")

    # ---------------------------------------------------------------- 7 conclusiones
    w("<h2>7. Conclusiones y recomendaciones</h2>")
    w("<ol>"
      f"<li><b>Réplicas:</b> {n} por corriente bastan para δ = 10 fs (α = 0,05, potencia 0,90). Plan: {rpd3} por corriente y por día durante tres días (n = {3 * rpd3}, {9 * rpd3} trazas, "
      f"≈ 1 h de medición al día).</li>"
      "<li><b>Forma del pulso:</b> el ajuste sech² y el gaussiano dan la misma S (misma n) y medias que difieren un 10–11 % de forma sistemática (gauss > sech²). "
      "Para la comparación con la hoja de fábrica se usa sech² × 0,65, que es lo que usó Calmar; el gaussiano se reporta al lado como sensibilidad a la forma.</li>"
      "<li><b>Estimador:</b> con paso de 67 fs y 4–5 lecturas en el ancho, usar el ajuste por mínimos cuadrados (todos los puntos) como análisis principal y el FWHM "
      "como comprobación. Ambos están en la hoja Ajustes; el selector de Configuración cambia cuál alimenta el Resumen.</li>"
      "<li><b>Muestreo de la semana:</b> mantener el paso de 10 µm (no se puede afinar), pero llevar el barrido hasta ±2–3 Δτ<sub>AC</sub> del pico para que las "
      "lecturas del fondo queden fuera de la señal: en I1 el ancho medido es ≈ 300 fs = 45 µm, así que el barrido debe cubrir ±90 a ±135 µm (19 a 28 lecturas); "
      "en I2 e I3 (≈ 230 fs = 35 µm), ±70 a ±105 µm (15 a 22 lecturas). Hoy varias trazas de I1 no llegaron a las alas.</li>"
      "<li><b>Trazas fallidas:</b> antes de cada traza confirmar que hay señal de solapamiento (el pico debe ser ≥ 10 veces el fondo); hoy una traza (R01) se tomó sin pico y hubo que excluirla. Anotar la causa y reponerla.</li>"
      "<li><b>Diferencia con fábrica:</b> las medias duplican τ₀ y la razón crece con la corriente. Revisar el jueves, con el mismo montaje: (a) el factor de conversión posición → retardo "
      "(mover el micrómetro una distancia conocida y comparar con el retardo esperado), (b) cuánto vidrio atraviesa el haz antes del cristal y su ensanchamiento esperado por dispersión, "
      "(c) si el láser tiene compensación de chirp activa. Son preguntas del informe final, no del número de réplicas.</li>"
      "<li><b>Unidades:</b> las potencias se leyeron en W (≈ 10⁻⁵ W). No afecta ningún resultado: la traza se normaliza y el ajuste tiene amplitud y fondo libres. El libro y las gráficas quedan etiquetados en W.</li>"
      "</ol>")
    w("<h3>Anexo. Fórmulas</h3>")
    w("<p class='nota'>Retardo: τ = 2·Δx/c = 6,6713 fs por µm. Autocorrelación de intensidad: sech²: g(τ) = 3·[u·coth(u) − 1]/sinh²(u), u = τ/t₀, τp = 1,7627·t₀, Δτ<sub>AC</sub> = τp/0,6482; "
      "gaussiana: g(τ) = exp(−4 ln2 · τ²/Δτ<sub>AC</sub>²), τp = 0,7071·Δτ<sub>AC</sub>. Modelo ajustado: y = B + A·g(τ − τ<sub>c</sub>), con A, B, τ<sub>c</sub>, τp libres (scipy.optimize.curve_fit). "
      "σ conservadora: S·√[(n−1)/χ²<sub>0,20; n−1</sub>] (n = 5: factor 1,558). Potencia de la t de una muestra: 1 − β = P(|T′| > t<sub>0,025; n−1</sub>) con T′ ~ t no central, λ = d·√n, d = δ/σ. "
      "Archivos: trabajo-practico/piloto/Piloto_Replicas_Autocorrelador_analisis.xlsx (copia revisada), scripts/trabajo-practico/analiza_piloto.py (ajustes y n), "
      "build_piloto_xlsx.py (libro), render_informe_piloto.py (este informe).</p>")
    w("</body></html>")
    open(salida, "w").write("\n".join(o))


if __name__ == "__main__":
    build(sys.argv[1], sys.argv[2])
