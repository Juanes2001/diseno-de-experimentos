"""Genera la presentación del protocolo de experimentación del trabajo práctico (25 oct 2026):
diseño de comparación simple, una prueba por corriente, del ancho de pulso del láser frente a la
hoja de pruebas de fábrica. Versión mínima (13 diapositivas): poco texto en pantalla, el detalle
va en las notas del orador.

Uso: .venv/bin/python render_protocolo_pptx.py <salida.pptx> <carpeta_figuras> <analisis_piloto.json>
Reutiliza el estilo y los helpers de render_pptx.py (exposición del 17 oct). Las figuras las hace
figuras_protocolo.py. Cifras del piloto leídas del JSON de analiza_piloto.py.
"""
import json
import os
import sys

from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.dml.color import RGBColor

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import render_pptx as rp  # noqa: E402
from render_pptx import (BODY, GRAY_T, HEAD, INK, LIGHT, MUTED, MX, RED, RED_T, TOP, VIOLET,  # noqa: E402
                         VIOLET_L, VIO_T, WHITE, Deck, arrow, bullets, equation, image, rect, stat, table, text)
from analiza_piloto import potencia  # noqa: E402

rp.FOOT = "Protocolo de experimentación · Diseño de Experimentos Avanzados · UNAL 2026-II"
PALE = RGBColor(0xC9, 0xD1, 0xDE)
GREEN = RGBColor(0x1B, 0x8A, 0x5A)
GREEN_T = RGBColor(0xE6, 0xF4, 0xEC)


def f1(v, nd=1):
    return f"{v:.{nd}f}".replace(".", ",")


def chip(slide, x, y, w, h, title, body, fill=GRAY_T, color=VIOLET, size=13, tsize=14):
    rect(slide, x, y, w, h, fill)
    text(slide, x + 0.2, y + 0.12, w - 0.4, 0.4, title, tsize, color, HEAD)
    text(slide, x + 0.2, y + 0.5, w - 0.4, h - 0.6, body, size, INK)


def build(out, figdir, analisis):
    A = json.load(open(analisis))
    R = A["resumen"]["fit_sech|sin_R01"]
    rp.icono(os.path.join(figdir, "icono.png"))
    d = Deck(figdir)
    F = d.fig
    n_oc, n_plan, sigma = R["n"], 9, R["sigma"]
    pot9 = potencia(n_plan, R["d"])

    # 1 · Portada ---------------------------------------------------------------------------------
    s = d.dark("Vamos a medir el ancho de pulso del láser a tres corrientes y comparar cada una con el valor que el "
               "fabricante midió en este mismo equipo. Diseño de comparación simple: una media frente a un valor "
               "conocido, repetido en cada corriente.")
    image(s, F("traza"), 7.0, 1.1, w=5.9)
    text(s, MX, 0.9, 7.0, 0.4, "DISEÑO DE EXPERIMENTOS AVANZADOS · TRABAJO PRÁCTICO", 13, VIOLET_L, HEAD)
    text(s, MX, 1.4, 6.3, 1.7, "Protocolo de experimentación", 44, WHITE, HEAD, line_spacing=0.95)
    text(s, MX, 3.3, 6.3, 1.5, "Ancho de pulso del láser Carmel CFL-05RFFUNC frente a su hoja de fábrica, a 5, 6 y 7 A. "
         "Comparación simple: una prueba por corriente.", 18, PALE, LIGHT)
    text(s, MX, 5.45, 7.0, 0.9, ["Juan Esteban Rodríguez Ochoa · Sebastián Zapata Henao",
                                 "Profesora: Faviana Gutiérrez Rôa"], 15, WHITE, BODY, space=4)
    text(s, MX, 6.45, 8.0, 0.4, "Universidad Nacional de Colombia · Sede Medellín · 25 de octubre de 2026", 13,
         RGBColor(0x9A, 0xA4, 0xB5), BODY)

    # 2 · Pregunta --------------------------------------------------------------------------------
    s = d.content("1 · Pregunta", "¿Qué pregunta responde el experimento?",
                  "El fabricante midió este láser al entregarlo (hoja de pruebas, tabla 5): ancho de pulso a cada "
                  "corriente de bombeo. La pregunta es si hoy, nueve años después, sigue dando esos anchos. Es una "
                  "pregunta por corriente: cada una tiene su valor de referencia y su propia prueba. Se eligieron 5, 6 "
                  "y 7 A porque son las corrientes altas, con más señal de segundo armónico; 7,23 A supera el máximo "
                  "del controlador (7,12 A). A 7 A la hoja da 70 fs en la tabla 4 y 54 fs en la tabla 5; se usa la "
                  "tabla 5 porque mide las tres corrientes con el mismo método, y se declara. El patrón no trae "
                  "tolerancia ni incertidumbre. Diseño de comparación simple, Montgomery sec. 2-4.6: la media de una "
                  "muestra frente a un valor conocido, una comparación por corriente.",
                  "Hoja de pruebas de fábrica del equipo, serie 881139, tabla 5")
    rect(s, MX, TOP, 12.13, 1.4, RED_T)
    text(s, MX + 0.4, TOP, 11.3, 1.4, "¿El láser entrega hoy, **a cada corriente**, pulsos tan cortos como los que el "
         "fabricante midió en este mismo equipo al entregarlo?", 24, INK, anchor=MSO_ANCHOR.MIDDLE)
    table(s, MX, TOP + 1.75, 5.6, [["Nivel", "Corriente", "τ₀ de fábrica"], ["I₁", "5 A", "107 fs"],
                                   ["I₂", "6 A", "76 fs"], ["I₃", "7 A", "54 fs"]], [1.4, 2.0, 2.2], 17, row_h=0.55)
    chips = [("Patrón", "Hoja de pruebas de fábrica del equipo (serie 881139), tabla 5."),
             ("Mismo método", "Autocorrelación de segundo armónico, sech², factor 0,65."),
             ("Una prueba por corriente", "Comparación simple: una media frente a un valor conocido.")]
    for i, (t_, b_) in enumerate(chips):
        chip(s, 6.6, TOP + 1.75 + i * 1.1, 6.13, 1.0, t_, b_, VIO_T if i < 2 else RED_T, VIOLET if i < 2 else RED)

    # 3 · Modelo, hipótesis y caso ----------------------------------------------------------------
    s = d.content("2 · Modelo e hipótesis", "¿Cuál es el modelo, la hipótesis y el caso?",
                  "Tres muestras independientes, una por corriente; cada observación es la media de su corriente más "
                  "un error normal; el parámetro de interés es μk − τ0,k. Hipótesis de dos colas porque τ0 es un "
                  "valor medido de este láser, no un máximo: un pulso más corto también diría que algo cambió. De los "
                  "nueve casos de la comparación simple es el caso 2: se compara una media, una población frente a un "
                  "patrón fijo (τ0 no tiene varianza) y σ desconocida, estimada con S. No es el caso 6 (pareadas) "
                  "porque el patrón no es una segunda medición; ni el 4 o 5 porque no hay dos muestras. Cada H0 se "
                  "decide con su muestra, su S y su t0.",
                  "Montgomery (2004), secs. 2-2 y 2-4.6, ec. 2-37; teoría del 23 oct 2026, parte III")
    equation(s, MX, TOP, 5.9, 1.3, ["y_{kj} = μ_{k} + ε_{kj}", "ε_{kj} ~ NID(0, σ_{k}²) · k = 1, 2, 3 · j = 1, …, n"], 22)
    table(s, MX, TOP + 1.55, 5.9, [["Corriente", "H₀", "H_{A}"], ["5 A", "μ₁ = 107 fs", "μ₁ ≠ 107 fs"],
                                   ["6 A", "μ₂ = 76 fs", "μ₂ ≠ 76 fs"], ["7 A", "μ₃ = 54 fs", "μ₃ ≠ 54 fs"]],
          [1.5, 2.2, 2.2], 16, row_h=0.52)
    text(s, MX, TOP + 3.75, 5.9, 0.9, "Dos colas: τ₀ es un valor **medido** de este láser, no un máximo.", 14.5, MUTED)
    ruta = ["Una media", "Una población frente a un patrón", "σ desconocida"]
    for i, r_ in enumerate(ruta):
        rect(s, 6.9 + i * 1.98, TOP, 1.85, 0.7, VIO_T)
        text(s, 6.9 + i * 1.98, TOP, 1.85, 0.7, r_, 12, VIOLET, HEAD, PP_ALIGN.CENTER, MSO_ANCHOR.MIDDLE)
        if i < 2:
            arrow(s, 8.76 + i * 1.98, TOP + 0.35, 8.87 + i * 1.98, TOP + 0.35, MUTED, 1.5)
    equation(s, 6.9, TOP + 0.9, 5.83, 1.45, ["Caso 2 · t de una muestra", "t₀ = (ȳ_{k} − τ_{0,k}) / (S_{k}/√n) · t_{n−1}"],
             20, RED_T, caption="se rechaza H₀ si |t₀| > t_{0,025; n−1} = 2,306 (n = 9)")
    casos = ["1 · media, σ conocida · Z", "2 · media, σ desconocida · t", "3 · dos medias, σ conocidas · Z",
             "4 · dos medias, σ iguales · t", "5 · dos medias, σ distintas · t", "6 · pareadas · t",
             "7 · una varianza · χ²", "8 · dos varianzas · F", "9 · proporciones · z"]
    text(s, 6.9, TOP + 2.5, 5.83, 0.3, "LOS NUEVE CASOS DE LA COMPARACIÓN SIMPLE", 10.5, MUTED, HEAD)
    for i, c_ in enumerate(casos):
        x = 6.9 + (i % 3) * 1.98
        y = TOP + 2.85 + (i // 3) * 0.7
        ours = i == 1
        rect(s, x, y, 1.85, 0.6, RED_T if ours else GRAY_T, RED if ours else None)
        text(s, x + 0.08, y, 1.7, 0.6, c_, 10.5, RED if ours else INK, HEAD if ours else BODY, PP_ALIGN.CENTER,
             MSO_ANCHOR.MIDDLE)

    # 4 · Qué se mide -----------------------------------------------------------------------------
    s = d.content("3 · Qué se mide", "¿Qué se mide y qué es una réplica?",
                  "La respuesta es el ancho de pulso τp, en fs, obtenido de la traza con el método del fabricante: "
                  "sech² y factor 0,65 sobre el ancho a media altura. El eje de retardo sale del micrómetro con "
                  "τ = 2Δx/c (6,67 fs por µm, brazo con retrorreflector). El cero de retardo es el pico de la "
                  "autocorrelación: el centro ajustado; el ancho no depende de dónde se ponga el cero. Con paso de "
                  "10 µm (66,7 fs) el máximo leído puede caer hasta 33 fs lejos del pico: por eso el estimador "
                  "principal es el ajuste por mínimos cuadrados de toda la traza y el FWHM interpolado es la "
                  "comprobación. Unidad experimental: una traza completa a corriente fija. Réplica: una traza nueva e "
                  "independiente: corriente fijada de nuevo y barrido nuevo desde el extremo, con lecturas nuevas. Dos "
                  "lecturas del mismo barrido no son réplicas. No se apaga el láser entre réplicas: la variación del "
                  "encendido entra a nivel de día.",
                  "Diels y Rudolph (2006), cap. 9; nota 2 de las hojas de datos de Calmar")
    image(s, F("traza"), MX, TOP - 0.05, w=6.5)
    equation(s, 7.4, TOP, 5.33, 1.4, ["τ_{p} = 0,65 · Δτ_{AC}", "τ = 2Δx / c = 6,67 fs por µm"], 22)
    bullets(s, 7.4, TOP + 1.65, 5.33, 2.0, [
        "**Cero de retardo = pico** de la autocorrelación. El ancho no depende del cero.",
        "**Estimador:** ajuste sech² de toda la traza; FWHM × 0,65 como comprobación.",
    ], 14.5, space=7)
    chip(s, 7.4, TOP + 3.55, 5.33, 1.4, "Réplica", "Una traza **nueva e independiente**: corriente fijada de nuevo y "
         "barrido nuevo desde el extremo.", RED_T, RED, size=13.5, tsize=15)

    # 5 · Piloto ----------------------------------------------------------------------------------
    s = d.content("4 · Cuántas réplicas", "¿Qué dijo el piloto del 24 de octubre?",
                  "Quince trazas en orden sorteado, ocho válidas (R08 a R15). La dispersión entre trazas es pequeña, "
                  "S de 2 a 5 fs (CV ≈ 2 %), y eso es lo que fija el número de réplicas. Las medias están 1,9 a 2,8 "
                  "veces por encima de la hoja de fábrica y la razón crece con la corriente: no cambia n, pero es la "
                  "pregunta abierta del informe (dispersión en el vidrio del montaje: un pulso de 54 fs se ensancha más "
                  "que uno de 107 fs). Entre inicios de trazas válidas pasaron 6,1 min: caben 48 trazas en 5 h.",
                  "Informe del piloto, 24 oct 2026, secciones 4 a 6")
    image(s, F("piloto"), MX, TOP - 0.05, w=6.6)
    stat(s, 7.6, TOP - 0.1, 5.1, "S = 2 a 5 fs", "dispersión entre trazas de una misma corriente: es lo que fija n", GREEN, 30)
    stat(s, 7.6, TOP + 1.55, 5.1, "2 a 3 × τ₀", "medias sobre la hoja de fábrica; no cambia n, es la pregunta del informe", RED, 30)
    stat(s, 7.6, TOP + 3.2, 5.1, "6,1 min por traza", "48 trazas caben en un día de 5 h", INK, 30)

    # 6 · Réplicas, delta y potencia --------------------------------------------------------------
    s = d.content("4 · Cuántas réplicas", "¿Cuántas réplicas, y por qué δ = 10 fs?",
                  "Método de Montgomery, sec. 2-4.2, curva OC de la t de una muestra. σ conservadora: la mayor S del "
                  "piloto (4,58 fs, 5 A, n = 5) por 1,558, límite superior de confianza del 80 %. δ = 10 fs tiene "
                  "tres bases: (1) el margen del propio fabricante, tabla 4 a 7 A: límite < 80 fs y resultado 70 fs, "
                  "regla 2 del protocolo δ = τmáx − τ0; (2) el error del método: cambiar la forma supuesta de sech² a "
                  "gaussiana mueve τp un 8,8 %, 9,4 fs a 107 fs, menos que eso no se puede atribuir al láser; (3) está "
                  "por encima del ruido (S de 2 a 5 fs). α = 0,05 es el nivel convencional; β = 0,10 es más exigente "
                  "que el 0,20 habitual porque el error tipo II, no ver 10 fs de más, es el que más pesa en una "
                  "verificación: seguir usando un láser con pulsos más largos sin saberlo. Con d = 1,40 sale n = 8; "
                  "el plan toma 9 por corriente, con potencia 0,96 para 10 fs y ≈ 1 para 15 fs. Límites: β nunca es "
                  "cero con n finito (β = 0,001 pediría 16; 0,00001, 22); β depende de δ (con n = 9 es 0,54 para 5 fs); "
                  "y más réplicas no quitan el sesgo del montaje. Con α = 0,01 harían falta 12 para mantener 0,90.",
                  "Montgomery (2004), sec. 2-4.2 y apéndice V; hoja de pruebas, tabla 4; Diels y Rudolph (2006), cap. 9")
    image(s, F("delta"), MX, TOP - 0.05, w=6.4)
    stat(s, 7.3, TOP - 0.1, 2.6, f"σ = {f1(sigma, 2)} fs", "1,558 × S mayor del piloto", VIOLET, 24)
    stat(s, 10.1, TOP - 0.1, 2.63, "δ = 10 fs", "margen del fabricante: 80 − 70 fs a 7 A; error de la forma 8,8 %", RED, 24)
    stat(s, 7.3, TOP + 1.65, 2.6, f"n = {n_oc}", "α = 0,05 · potencia 0,90 · dos colas", INK, 24)
    stat(s, 10.1, TOP + 1.65, 2.63, f"9 → {f1(pot9, 2)}", "potencia real del plan para 10 fs; ≈ 1 para 15 fs", GREEN, 24)
    chip(s, 7.3, TOP + 3.45, 5.43, 1.5, "β pesa más que α", "No ver 10 fs de más es seguir usando un láser fuera de "
         "especificación. Más réplicas bajan β, no el sesgo del montaje.", RED_T, RED, size=13, tsize=14)

    # 7 · Orden sorteado --------------------------------------------------------------------------
    s = d.content("5 · Cómo se mide", "¿Por qué se sortea el orden dentro del día?",
                  "Notación: ȳₖ es la media de las réplicas de la corriente k (k = 1, 2, 3 para 5, 6 y 7 A) y Sₖ su "
                  "desviación estándar. Deriva: un cambio lento del montaje a lo largo de la tarde (alineación, "
                  "temperatura del cuarto, detector que se calienta) que no depende de la corriente. Cada traza mide "
                  "τ real de su corriente + deriva del momento en que se tomó + ruido. Ejemplo: 9 trazas en una tarde y "
                  "una deriva de +2 fs por traza (0, 2, …, 16 fs). Agrupadas por corriente, I₁ recibe 0, 2 y 4 fs (sesgo "
                  "+2 fs), I₂ 6, 8 y 10 (+8 fs) e I₃ 12, 14 y 16 (+14 fs): a 7 A se mediría 14 fs de más solo por ir al "
                  "final, más que δ = 10 fs. Además las tres réplicas de cada corriente se tomaron seguidas y se parecen "
                  "demasiado: Sₖ queda subestimada y t0 = (ȳₖ − τ0)/(Sₖ/√n) se infla en numerador y denominador. Con "
                  "el orden sorteado cada corriente cae en momentos repartidos de la tarde: ninguna se lleva la parte "
                  "alta de la deriva, la deriva pasa a la variación entre réplicas (Sₖ la incluye) y el error de cada "
                  "traza se comporta como aleatorio e independiente, que es lo que supone la prueba t (Montgomery, "
                  "sec. 1-3). Matiz: el sorteo reparte la deriva pero no borra su nivel promedio; si en toda la tarde "
                  "el montaje mide en promedio 8 fs de más, eso le pasa a las tres corrientes por igual y es un error "
                  "sistemático del instrumento frente a τ0, que se controla con el calentamiento de 30 min, el montaje "
                  "fijo y se discute en el informe. Lo que el sorteo garantiza es que la deriva no favorezca a una "
                  "corriente y que Sₖ sea realista. Las corrientes no interfieren: cada traza es una realización "
                  "separada y el láser no guarda memoria de la corriente anterior tras 5 min.",
                  "Montgomery (2004), secs. 1-3 y 2-4.1")
    col = {"I₁": VIOLET, "I₂": RED, "I₃": INK}
    text(s, MX + 1.9, TOP - 0.1, 9.0, 0.35, "deriva del montaje: +2 fs por traza a lo largo de la tarde →", 13, MUTED,
         align=PP_ALIGN.CENTER)
    arrow(s, MX + 1.9, TOP + 0.28, MX + 10.9, TOP + 0.28, MUTED, 1.5)
    filas = [("Agrupado", ["I₁"] * 3 + ["I₂"] * 3 + ["I₃"] * 3,
              "sesgo de ȳ₁, ȳ₂, ȳ₃: +2, +8 y +14 fs; réplicas seguidas → Sₖ chica", RED),
             ("Sorteado", ["I₂", "I₁", "I₂", "I₃", "I₁", "I₁", "I₃", "I₃", "I₂"],
              "la deriva se reparte por igual entre corrientes y entra en Sₖ", GREEN)]
    for r_, (nom, orden, expl, c_) in enumerate(filas):
        y = TOP + 0.45 + r_ * 1.25
        text(s, MX, y, 1.8, 0.55, nom, 15, c_, HEAD, anchor=MSO_ANCHOR.MIDDLE)
        for j, lv in enumerate(orden):
            x = MX + 1.9 + j * 1.0
            rect(s, x, y, 0.9, 0.55, col[lv])
            text(s, x, y, 0.9, 0.55, lv, 15, WHITE, HEAD, PP_ALIGN.CENTER, MSO_ANCHOR.MIDDLE)
        text(s, MX + 1.9, y + 0.6, 9.3, 0.45, expl, 13.5, c_)
    chips = [("ȳₖ y Sₖ", "Media y desviación estándar de las réplicas de la corriente k (5, 6 o 7 A).", VIO_T, VIOLET),
             ("Qué protege el sorteo", "Que la deriva no favorezca a una corriente y que Sₖ sea realista: el tiempo "
              "pasa al error, como supone la prueba t.", RED_T, RED),
             ("Qué no protege", "El nivel promedio de la deriva, igual en las tres: se controla con calentamiento y "
              "montaje fijo, y se discute.", GRAY_T, INK)]
    for i, (t_, b_, f_, c_) in enumerate(chips):
        chip(s, MX + i * 4.1, TOP + 3.25, 3.93, 1.7, t_, b_, f_, c_, size=13, tsize=14)

    # 7b · Una corriente por día -------------------------------------------------------------------
    s = d.content("5 · Cómo se mide", "¿Por qué no medir una corriente por día?",
                  "Alternativa tentadora: lunes 9 trazas de I₁, martes 9 de I₂, miércoles 9 de I₃. Falla por la misma "
                  "razón que el orden agrupado, pero a escala de días: cada día trae su propio nivel (realineación, "
                  "temperatura, humedad, estado del láser al arrancar). Ejemplo: lunes 0, martes +6 fs, miércoles −4 fs. "
                  "Con una corriente por día el sesgo de ȳ₁, ȳ₂ y ȳ₃ es 0, +6 y −4 fs: el día y la corriente quedan "
                  "confundidos y no se sabe si lo observado es el láser o el martes. Con 3 réplicas de cada corriente "
                  "por día, el nivel de cada día se reparte por igual: (0 + 6 − 4)/3 = +0,67 fs en las tres. Dos "
                  "problemas más: (1) Sₖ sale de una sola sesión y no ve la variación de un día a otro, así que se "
                  "subestima y t0 se infla; en el plan balanceado las réplicas de cada corriente vienen de tres días; "
                  "(2) un mal día cuesta una corriente entera, mientras que en el plan balanceado cuesta 3 réplicas de "
                  "cada corriente y quedan 6. Además, la pregunta es si el láser da el ancho de fábrica, no si lo dio "
                  "el martes: cada media debe representar varias condiciones de medición. Lo único a favor de una "
                  "corriente por día es ahorrar cambios de corriente (5 min de estabilización cada uno), pero en el "
                  "piloto una traza con cambio tomó unos 6 min y caben 48 trazas al día; solo se necesitan 9. Y si el "
                  "efecto del día fuera cero, con ese diseño no se podría comprobar; con el plan balanceado el día queda "
                  "como bloque y se puede analizar sin cambiar la toma de datos. Conclusión: 3 días × 3 réplicas por "
                  "corriente con orden sorteado protegen de la hora (sorteo) y del día (balance).",
                  "Montgomery (2004), secs. 1-3 y 4-1")
    table(s, MX, TOP - 0.05, 7.4,
          [["Plan", "Sesgo de ȳ₁ (5 A)", "ȳ₂ (6 A)", "ȳ₃ (7 A)"],
           ["Una corriente por día", "0", "+6 fs", "−4 fs"],
           ["3 de cada corriente por día", "+0,67 fs", "+0,67 fs", "+0,67 fs"]],
          [2.8, 1.6, 1.5, 1.5], size=14)
    text(s, MX, TOP + 1.45, 7.4, 0.4, "Ejemplo: nivel del lunes 0, del martes +6 fs, del miércoles −4 fs", 12.5, MUTED)
    chips = [("Día y corriente confundidos", "El +6 del martes entra entero en ȳ₂: ¿es el láser o es el martes?",
              RED_T, RED),
             ("Sₖ chica", "Una sola sesión no ve la variación entre días: t0 se infla.", RED_T, RED),
             ("Un mal día", "Cuesta una corriente entera; balanceado, solo 3 réplicas de cada una.", RED_T, RED)]
    for i, (t_, b_, f_, c_) in enumerate(chips):
        chip(s, MX + 7.75, TOP - 0.05 + i * 1.2, 4.55, 1.1, t_, b_, f_, c_, size=12.5, tsize=14)
    chip(s, MX, TOP + 2.05, 7.4, 1.25, "¿Y lo que ahorra?", "Cambios de corriente de 5 min. El piloto: 6 min por traza "
         "con cambio, caben 48 al día y se necesitan 9.", GRAY_T, INK, size=13, tsize=14)
    chip(s, MX, TOP + 3.6, 12.3, 1.2, "Plan: 3 días × 3 réplicas por corriente, orden sorteado cada día",
         "El sorteo protege de la hora; el balance protege del día, que queda como bloque y se puede analizar.",
         GREEN_T, GREEN, size=13.5, tsize=15)

    # 8 · Cada réplica ----------------------------------------------------------------------------
    s = d.content("5 · Cómo se mide", "¿Cómo se toma cada réplica?",
                  "Procedimiento fijo. Fijar la corriente del turno, llevar el micrómetro más allá del extremo "
                  "del barrido y avanzar siempre en el mismo sentido para que el juego del micrómetro no cambie la "
                  "posición. El recorrido llega a 2 o 3 anchos de la autocorrelación a cada lado; con el paso de "
                  "10 µm (resolución del micrómetro, confirmada) son de 15 a 29 lecturas y 4 o 5 dentro del ancho; "
                  "por eso el ajuste de toda la traza es el estimador principal. Se fija lo demás: forma y factor del "
                  "fabricante, 30 min de calentamiento, mismo programa de análisis; temperatura y humedad no se miden, "
                  "se anota la hora y se declara. Registro: una fila por réplica (día, turno, corriente, potencia, "
                  "horas, hoja, Δτ_AC, τp, válida, observaciones). Se descarta solo por causa anotada en el momento; "
                  "nunca por el valor que dio; toda traza descartada se repone el jueves.",
                  "Protocolo, sección 5; informe del piloto, conclusión 4")
    pasos = ["Fijar la corriente; esperar 5 min si cambió; anotar la potencia.",
             "Llevar el micrómetro más allá del extremo del barrido.",
             "Avanzar **siempre en el mismo sentido**, paso 10 µm.",
             "Anotar posición y potencia óptica en cada lectura, hasta las alas.",
             "Guardar la hoja Rk. **No descartar nada en el momento.**",
             "Analizar con el programa fijo: Δτ_{AC}, τ_{p}, estado."]
    for i, p_ in enumerate(pasos):
        y = TOP + i * 0.72
        rect(s, MX, y + 0.08, 0.5, 0.5, VIOLET if i < 5 else RED, shape=MSO_SHAPE.OVAL)
        text(s, MX, y + 0.08, 0.5, 0.5, str(i + 1), 15, WHITE, HEAD, PP_ALIGN.CENTER, MSO_ANCHOR.MIDDLE)
        text(s, MX + 0.7, y, 5.6, 0.66, p_, 14.5, INK, anchor=MSO_ANCHOR.MIDDLE)
    table(s, 7.2, TOP, 5.53, [["Corriente", "Δτ_{AC} medido", "Barrido", "Lecturas"],
                             ["5 A", "≈ 310 fs = 46 µm", "±90 a ±140 µm", "19 a 29"],
                             ["6 A", "≈ 238 fs = 36 µm", "±70 a ±105 µm", "15 a 22"],
                             ["7 A", "≈ 238 fs = 36 µm", "±70 a ±105 µm", "15 a 22"]], [1.1, 1.85, 1.63, 0.95], 13, row_h=0.46)
    chip(s, 7.2, TOP + 2.15, 5.53, 1.3, "Fijo", "sech² y 0,65 · 30 min de calentamiento · paso 10 µm · mismo programa · "
         "temperatura y humedad: limitación declarada", GRAY_T, INK, size=13, tsize=14)
    chip(s, 7.2, TOP + 3.6, 5.53, 1.35, "Registro y descarte", "Una fila por réplica. Se descarta **solo por causa anotada "
         "en el momento**, nunca por el valor; se repone.", RED_T, RED, size=13, tsize=14)

    # 9 · Análisis y decisión ---------------------------------------------------------------------
    s = d.content("6 · Análisis y decisión", "¿Cómo se analiza y cómo se decide en cada corriente?",
                  "Todo por corriente. Gráficas: diagrama de puntos con τ0 marcado y τp contra el orden. Supuestos de "
                  "la t: normalidad con gráfica de probabilidad y Anderson-Darling (con n = 9 manda la gráfica), "
                  "independencia con τp contra el orden de medición, atípicos con residuos estandarizados y la causa "
                  "anotada; si falla la normalidad se reporta igual la t y se añade la prueba de signos o Wilcoxon. "
                  "Prueba t de una muestra con la salida literal de Minitab: n, media, S, error estándar, IC, t, P. "
                  "La prueba dice si hay diferencia; la verificación pregunta cuánto, por eso se lee el IC del 95 % "
                  "de μk − τ0,k frente a la banda de ±10 fs: dentro, conforme; fuera, desviación; cruza, no "
                  "concluyente. No rechazar H0 no prueba conformidad; se puede leer así porque n se fijó con potencia "
                  "0,90 para 10 fs. Se reporta también la potencia lograda con el n y la S reales. Tabla de ejemplos con "
                  "n = 9 y S = 5 fs (semiancho 0,77·S = 3,8 fs): con 9 fs de diferencia la t rechaza H0 porque el IC "
                  "excluye el cero, pero el IC va de 5 a 13 fs y no se puede afirmar que supere 10 fs: no concluyente. "
                  "Con 6 fs la diferencia es significativa pero pequeña frente a lo que importa: conforme. La prueba "
                  "dice si hay diferencia; el intervalo dice si es grande.",
                  "Montgomery (2004), secs. 2-4.1, 2-4.2 y 2-4.6, ec. 2-38")
    pasos = [("Gráficas", "τ_{p} por corriente con τ₀ marcado; τ_{p} contra el orden."),
             ("Supuestos", "Normalidad: gráfica de probabilidad y Anderson-Darling. Independencia: orden. Atípicos: causa."),
             ("Prueba t", "n, ȳ, S, EE, t₀, valor P e IC. Salida literal de Minitab."),
             ("Decisión", "IC del 95 % de μ_{k} − τ_{0,k} frente a ±10 fs.")]
    for i, (t_, b_) in enumerate(pasos):
        y = TOP + i * 1.22
        rect(s, MX, y + 0.05, 0.5, 0.5, VIOLET if i < 3 else RED, shape=MSO_SHAPE.OVAL)
        text(s, MX, y + 0.05, 0.5, 0.5, str(i + 1), 15, WHITE, HEAD, PP_ALIGN.CENTER, MSO_ANCHOR.MIDDLE)
        text(s, MX + 0.7, y, 5.2, 0.45, t_, 16, VIOLET if i < 3 else RED, HEAD)
        text(s, MX + 0.7, y + 0.45, 5.2, 0.7, b_, 13.5, INK)
    equation(s, 7.0, TOP, 5.73, 1.15, ["t₀ = (ȳ_{k} − τ_{0,k}) / (S_{k}/√n)", "IC: (ȳ_{k} − τ_{0,k}) ± 2,306 · S_{k}/√n"], 18)
    res = [("Conforme", "IC dentro de ±10 fs", GREEN_T, GREEN),
           ("Desviación", "IC fuera de ±10 fs", RED_T, RED),
           ("No concluyente", "IC contiene el límite de 10 fs", GRAY_T, INK)]
    for i, (t_, b_, f_, c_) in enumerate(res):
        x = 7.0 + i * 1.94
        rect(s, x, TOP + 1.3, 1.85, 0.95, f_)
        text(s, x + 0.12, TOP + 1.36, 1.65, 0.4, t_, 13, c_, HEAD)
        text(s, x + 0.12, TOP + 1.74, 1.65, 0.5, b_, 11.5, INK)
    table(s, 7.0, TOP + 2.45, 5.73, [["ȳ − τ₀", "IC del 95 %", "¿Rechaza H₀?", "Decisión"],
                                    ["20 fs", "16,2 a 23,8", "Sí", "Desviación"],
                                    ["9 fs", "5,2 a 12,8", "Sí", "No concluyente"],
                                    ["6 fs", "2,2 a 9,8", "Sí", "Conforme"],
                                    ["3 fs", "−0,8 a 6,8", "No", "Conforme"]], [1.0, 1.55, 1.4, 1.78], 12.5, row_h=0.38)
    text(s, 7.0, TOP + 4.45, 5.73, 0.6, "Ejemplos con n = 9 y S = 5 fs (semiancho ±3,8 fs). Rechazar H₀ dice que hay "
         "diferencia; el IC dice si supera 10 fs.", 11.5, MUTED)

    # 10 · Minitab y calendario -------------------------------------------------------------------
    s = d.content("7 · Minitab y calendario", "¿Con qué se calcula y cuándo se mide?",
                  "Rutas de Minitab en español: n en Potencia y tamaño de la muestra (diferencia 10, σ 7,13, potencia "
                  "0,90) da 8; sorteo con Muestra de columnas; normalidad con la gráfica de probabilidad y "
                  "Anderson-Darling; prueba con t de 1 muestra, media hipotética τ0,k, dos colas, 95 %. Calendario: el "
                  "láser será retirado, así que se mide lunes, martes y miércoles, con el jueves de reserva para "
                  "reponer trazas y comprobar el montaje; desde el viernes se desmonta; en noviembre análisis e "
                  "informe; entrega el 12 de diciembre. Si hay menos tiempo: dos días con 4 + 5 por corriente, o lo que "
                  "quepa, y se informa la potencia lograda.", "Documentación de Minitab en español; protocolo, sección 7")
    table(s, MX, TOP, 6.2, [["Para qué", "Minitab"],
                            ["Réplicas", "Estadísticas › Potencia y tamaño de la muestra › t de 1 muestra"],
                            ["Sorteo", "Calc › Datos aleatorios › Muestra de columnas"],
                            ["Normalidad", "Gráfica › Gráfica de probabilidad · Prueba de normalidad"],
                            ["Prueba", "Estadísticas › Estadísticas básicas › t de 1 muestra"]], [1.4, 4.8], 13, row_h=0.6)
    text(s, MX, TOP + 3.25, 6.2, 1.2, "Salida literal por corriente: **N, Media, Desv.Est., EE, IC 95 %, T, P**, más la "
         "potencia lograda y las gráficas de supuestos.", 14, MUTED)
    hitos = [("Lun 26 – Mié 28", "Días 1, 2 y 3: 9 trazas al día, 3 por corriente, orden sorteado", VIOLET),
             ("Jue 29", "Reserva: reponer trazas, comprobar el montaje, copia de seguridad", RED),
             ("Vie 30 →", "Desmontaje", INK),
             ("Nov · 12 dic", "Análisis, informe ICONTEC y exposición", INK)]
    for i, (f_, b_, c_) in enumerate(hitos):
        y = TOP + i * 1.22
        rect(s, 7.3, y + 0.1, 0.45, 0.45, c_, shape=MSO_SHAPE.OVAL)
        text(s, 7.95, y, 4.8, 0.45, f_, 16, c_, HEAD)
        text(s, 7.95, y + 0.45, 4.8, 0.7, b_, 13.5, INK)

    # 11 · Cierre ---------------------------------------------------------------------------------
    s = d.dark("Cerrar con las cuatro decisiones del protocolo.")
    text(s, MX, 0.9, 10, 0.4, "EN UNA PANTALLA", 13, VIOLET_L, HEAD)
    text(s, MX, 1.3, 11.5, 0.9, "¿Qué queda decidido?", 40, WHITE, HEAD)
    dec = [("1", "Una prueba por corriente", "H₀: μ_{k} = τ_{0,k} · dos colas · t de una muestra"),
           ("2", "9 réplicas por corriente", "σ = 7,13 fs · δ = 10 fs · α = 0,05 · potencia 0,96"),
           ("3", "Orden sorteado", "3 días × (3 + 3 + 3) · traza completa por réplica · descarte solo con causa"),
           ("4", "Decisión con el IC", "IC de μ_{k} − τ_{0,k} frente a ±10 fs: conforme, desviación o no concluyente")]
    for i, (n_, t_, b_) in enumerate(dec):
        x = MX + i * 3.07
        rect(s, x, 2.6, 2.9, 3.1, RGBColor(0x16, 0x1D, 0x33))
        text(s, x + 0.25, 2.8, 2.4, 0.7, n_, 34, RED if i < 2 else VIOLET_L, HEAD)
        text(s, x + 0.25, 3.5, 2.4, 0.9, t_, 18, WHITE, HEAD)
        text(s, x + 0.25, 4.45, 2.4, 1.2, b_, 13.5, PALE)
    text(s, MX, 6.1, 12.1, 0.6, "Pendiente: confirmar el brazo de 2 pasos y declarar la discrepancia de la hoja a 7 A.",
         15, PALE, LIGHT, italic=True)

    # 12 · Referencias ----------------------------------------------------------------------------
    s = d.content("Referencias", "Referencias", "Referencias en Normas ICONTEC.")
    refs = [
        "MONTGOMERY, Douglas C. Diseño y análisis de experimentos. 2 ed. México: Limusa Wiley, 2004. Capítulo 2, "
        "Experimentos comparativos simples, p. 21-59.",
        "GUTIÉRREZ PULIDO, Humberto y DE LA VARA SALAZAR, Román. Análisis y diseño de experimentos. 2 ed. México: "
        "McGraw-Hill, 2008. Capítulo 2, p. 18-59.",
        "CALMAR LASER. Carmel CFL-05RFFUNC, serie 881139: hoja de pruebas de fábrica, sección 4, tablas 4 y 5. "
        "Documento técnico del equipo.",
        "CALMAR LASER. Carmel X-780: 780 nm High Power Fiber Based Femtosecond Laser. Hoja de datos, Rev. E, 2025.",
        "DIELS, Jean-Claude y RUDOLPH, Wolfgang. Ultrashort laser pulse phenomena. 2 ed. Burlington: Academic Press, "
        "2006. Capítulo 9, p. 457-489.",
        "RODRÍGUEZ OCHOA, Juan Esteban y ZAPATA HENAO, Sebastián. Piloto del 24 de octubre: resultados, revisión del "
        "libro de cálculo y número de réplicas. Informe interno, 24 oct. 2026.",
    ]
    text(s, MX, TOP, 12.13, 5.0, refs, 14, INK, space=10)

    d.prs.save(out)
    print("pptx:", out, "·", d.n, "diapositivas")


if __name__ == "__main__":
    build(sys.argv[1], sys.argv[2], sys.argv[3])
