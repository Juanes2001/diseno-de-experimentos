"""Genera los libros de Excel de la medición definitiva del autocorrelador (una corriente por libro).

Cada libro recibe 9 réplicas de una sola corriente: por traza, solo la potencia óptica (W); las
posiciones del micrómetro quedan fijas con el muestreo del piloto (22 lecturas, 0 a 210 µm cada
10 µm). Con fórmulas calcula el retardo, la traza normalizada, el ancho a media altura y τp
(FWHM × factor sech²), el registro de tiempos por corrida y la prueba t de una muestra contra τ0.

Uso:
    .venv/bin/python scripts/trabajo-practico/build_medicion_xlsx.py           # los tres libros
    .venv/bin/python scripts/trabajo-practico/build_medicion_xlsx.py --prueba  # con datos sintéticos
"""
import argparse
from pathlib import Path

import numpy as np
import xlsxwriter
from xlsxwriter.utility import xl_rowcol_to_cell as rc

RAIZ = Path(__file__).resolve().parents[2]
CARPETA = RAIZ / "trabajo-practico" / "medicion"
FONT = "Arial"

N_REP = 9                                  # réplicas del plan (informe del piloto)
N_REPO = 3                                 # hojas de reposición por si se descarta una traza
POSICIONES = [10.0 * k for k in range(22)]  # µm, muestreo del piloto (R12–R15)
FS_POR_UM = 2 * 1e-6 / 299792458.0 * 1e15

# corriente (A), clave, τ0 de fábrica (fs), potencia de fábrica (mW), fecha prevista
CORRIENTES = [
    (5.0, "I1", 107, 218, "martes 27 oct 2026"),
    (6.0, "I2", 76, 378, "miércoles 28 oct 2026"),
    (7.0, "I3", 54, 579, "sábado 31 oct 2026"),
]


def g_sech2(tau, tau_p):
    u = np.where(np.abs(tau) < 1e-6, 1.0, tau / (tau_p / 1.7627))
    return np.where(np.abs(tau) < 1e-6, 1.0, 3 * (u / np.tanh(u) - 1) / np.sinh(u) ** 2)


def traza_sintetica(tau_p, semilla, centro_um=105.0):
    """Solo para --prueba: potencia (W) en las posiciones fijas para un pulso sech² de ancho tau_p."""
    rng = np.random.default_rng(semilla)
    x = np.array(POSICIONES) - centro_um - rng.uniform(-5, 5)
    y = 2.4e-5 * g_sech2(x * FS_POR_UM, tau_p) * (1 + 0.02 * rng.standard_normal(x.size))
    return [float(v) for v in np.round(y + 1e-8 * rng.standard_normal(x.size), 10)]


def build(salida, amp, clave, tau0, pfab, fecha, datos=None):
    wb = xlsxwriter.Workbook(str(salida), {"use_future_functions": True})
    wb.set_calc_mode("auto")
    wb.set_properties({"title": f"Medición del autocorrelador · {amp:g} A",
                       "author": "Juan Esteban Rodríguez Ochoa · Sebastián Zapata Henao"})
    base = {"font_name": FONT, "font_size": 10, "valign": "vcenter"}

    def F(**kw):
        d = dict(base)
        d.update(kw)
        return wb.add_format(d)

    f_tit = F(bold=True, font_size=14, font_color="#1F3864")
    f_sub = F(italic=True, font_color="#595959")
    f_h = F(bold=True, bg_color="#1F3864", font_color="white", border=1, text_wrap=True, align="center")
    f_lab = F(border=1, text_wrap=True)
    f_labb = F(border=1, bold=True, text_wrap=True)
    f_in = F(border=1, bg_color="#FFF2CC", font_color="#0000FF", locked=False)
    f_in_w = F(border=1, bg_color="#FFF2CC", font_color="#0000FF", num_format="0.000E+00", locked=False)
    f_in_num = F(border=1, bg_color="#FFF2CC", font_color="#0000FF", num_format="General", locked=False)
    f_in_t = F(border=1, bg_color="#FFF2CC", font_color="#0000FF", num_format="hh:mm", locked=False, align="center")
    f_in_txt = F(border=1, bg_color="#FFF2CC", font_color="#0000FF", text_wrap=True, locked=False)
    f_fijo = F(border=1, bg_color="#D9D9D9", bold=True, num_format="0", align="center")
    f_calc = F(border=1, num_format="0.00")
    f_calc3 = F(border=1, num_format="0.000")
    f_calc4 = F(border=1, num_format="0.0000")
    f_sci = F(border=1, num_format="0.00E+00")
    f_int = F(border=1, num_format="0", align="center")
    f_link = F(border=1, font_color="#008000", num_format="0.00")
    f_linkt = F(border=1, font_color="#008000")
    f_key = F(border=2, bold=True, bg_color="#E2EFDA", num_format="0.00", font_size=12)
    f_keyt = F(border=2, bold=True, bg_color="#E2EFDA", text_wrap=True)
    f_gray = F(font_color="#808080", num_format="0.00")
    f_gray3 = F(font_color="#808080", num_format="0.0000")
    f_gsci = F(font_color="#808080", num_format="0.000E+00")
    f_note = F(italic=True, font_color="#595959", text_wrap=True, valign="top")
    f_txt = F(text_wrap=True, valign="top")
    f_ok = F(bg_color="#C6EFCE", font_color="#006100", border=1)
    f_warn = F(bg_color="#FFEB9C", font_color="#9C5700", border=1)
    f_bad = F(bg_color="#FFC7CE", font_color="#9C0006", border=1)

    NP = len(POSICIONES)
    L = NP + 1                                            # última fila Excel con datos
    q = lambda s: f"'{s}'"
    S_CFG, S_REG, S_RES = "Configuración", "Registro", "Resumen"
    trazas = [f"R{k:02d}" for k in range(1, N_REP + N_REPO + 1)]

    ws_ins = wb.add_worksheet("Instrucciones")
    ws_cfg = wb.add_worksheet(S_CFG)
    ws_reg = wb.add_worksheet(S_REG)
    ws_res = wb.add_worksheet(S_RES)
    ws_tr = [wb.add_worksheet(n) for n in trazas]
    for w in ws_tr[N_REP:]:
        w.set_tab_color("#A6A6A6")

    # ============================================================ Instrucciones
    w = ws_ins
    w.set_column("A:A", 110)
    w.write("A1", f"Medición definitiva del autocorrelador · corriente {amp:g} A ({clave})", f_tit)
    w.write("A2", f"Fecha prevista: {fecha}. Nueve réplicas de la misma corriente, una tras otra.", f_sub)
    pasos = [
        "1. Encender el láser y dejarlo calentar como en el piloto. Fijar la corriente de bombeo en "
        f"{amp:g} A y anotar en Registro la fecha, la hora de encendido y la potencia media del láser.",
        "2. Las posiciones del micrómetro están fijas en todas las hojas R01–R09 (columna A, gris): 22 lecturas, "
        "de 0 a 210 µm cada 10 µm, contadas desde el punto de partida del barrido. Escoger el punto de partida "
        "de modo que el pico caiga en la mitad del recorrido (≈ 100–110 µm). A 5 A la traza es ancha: si el pico "
        "queda en 120 µm o más, el barrido no alcanza el ala derecha (el Estado lo avisa).",
        "3. Girar el micrómetro siempre en el mismo sentido. En cada posición escribir la potencia óptica en W "
        "(columna B, amarilla), tal como la da el medidor: por ejemplo 2.35E-05.",
        "4. En Registro, escribir la hora de inicio y la hora de fin de cada corrida (hh:mm). La duración y el "
        "tiempo entre inicios se calculan solos.",
        "5. Revisar el «Estado de la traza» (columna L del Registro, o la celda M20 de la hoja). Si dice OK o "
        "Aviso, seguir. Si dice Revisar, comprobar los datos escritos antes de seguir.",
        "6. Una traza solo se marca «No» en ¿Válida? por una causa anotada en el momento (el láser perdió los "
        "pulsos, la potencia salió de rango, el barrido se interrumpió). Nunca por dar un valor inesperado. "
        "Toda traza descartada se repone en la siguiente hoja de reposición (R10, R11, R12).",
        "7. La hoja Resumen da n, la media, S, el intervalo de confianza del 95 % y la prueba t de una muestra "
        "contra τ0 del fabricante. El análisis definitivo (ajuste sech² de toda la traza) se hace después con "
        "scripts/trabajo-practico/analiza_piloto.py; aquí se usa el ancho a media altura × 0,65.",
        "Colores: amarillo con letra azul = se llena; gris = fijo; lo demás son fórmulas. Las hojas de traza "
        "están protegidas (sin contraseña) para no borrar las posiciones ni las fórmulas.",
    ]
    for i, p in enumerate(pasos):
        w.write(3 + i, 0, p, f_txt)
        w.set_row(3 + i, 42)

    # ============================================================ Configuración
    w = ws_cfg
    w.set_column("A:A", 50)
    w.set_column("B:B", 16)
    w.set_column("C:C", 70)
    w.write("A1", "Configuración", f_tit)
    w.write("A2", "Valores fijos del protocolo. No cambiarlos durante la medición.", f_sub)
    w.write_row("A4", ["Parámetro", "Valor", "Nota"], f_h)
    r = 4

    def cfg(nombre, etiqueta, valor, nota, fmt, formula=False):
        nonlocal r
        w.write(r, 0, etiqueta, f_lab)
        (w.write_formula if formula else w.write)(r, 1, valor, fmt)
        w.write(r, 2, nota, f_note)
        wb.define_name(nombre, f"={q(S_CFG)}!$B${r + 1}")
        r += 1

    cfg("corriente", "Corriente de bombeo (A)", amp, f"{clave} del protocolo; hoja de pruebas de fábrica, tabla 5.", f_calc)
    cfg("tau0", "τ0: ancho de pulso del fabricante (fs)", tau0, "Tabla 5 de la hoja de pruebas de fábrica.", f_calc)
    cfg("pfab", "Potencia media de fábrica (mW)", pfab, "Referencia para comparar con la potencia medida.", f_calc)
    cfg("paso", "Paso del micrómetro (µm)", 10, "Fijo, como en el piloto.", f_calc)
    cfg("pasos", "Veces que el haz recorre el desplazamiento", 2, "Retrorreflector: τ = 2Δx/c.", f_calc)
    cfg("c_luz", "Velocidad de la luz c (m/s)", 299792458, "Valor exacto (SI).", F(border=1, num_format="0"))
    cfg("conv", "Retardo por µm del micrómetro (fs)", "=pasos*10^-6/c_luz*10^15", "6,6713 fs por µm.",
        f_calc4, formula=True)
    cfg("factor_forma", "Factor de forma sech²: τp = factor × Δτ_AC", 0.65, "El que usa Calmar (teórico 0,648).", f_calc)
    cfg("n_fondo", "Lecturas por ala para el fondo", 2, "Promedio de las 2 primeras y las 2 últimas lecturas.", f_int)
    cfg("semi", "Semiventana de suavizado", 0, "0 = sin suavizar (programa de análisis fijo).", f_int)
    cfg("pts_min", "Lecturas mínimas dentro del ancho a media altura", 4,
        "Con paso de 10 µm el piloto tuvo 4–5 lecturas dentro del FWHM.", f_int)
    cfg("rec_min", "Recorrido mínimo a cada lado del centro (múltiplos de Δτ_AC)", 2,
        "Si no se alcanza, el fondo sale alto y el ancho corto.", f_calc)
    cfg("alfa", "α de la prueba t (dos colas)", 0.05, "Protocolo.", f_calc)

    # ============================================================ hojas de traza
    def hoja_traza(w, nombre, num, datos=None):
        w.set_column("A:A", 14)
        w.set_column("B:B", 15)
        w.set_column("C:E", 12)
        w.set_column("F:H", 9)
        w.set_column("I:J", 11)
        w.set_column("K:K", 7)
        w.set_column("L:L", 42)
        w.set_column("M:M", 14)
        w.freeze_panes(1, 0)
        w.write_row(0, 0, ["Posición del micrómetro (µm) · fija", "Potencia óptica (W)", "Retardo τ (fs)",
                           "Señal suavizada", "Señal normalizada", "Cruce izq. (fila)", "Cruce der. (fila)",
                           "τ de cruce (fs)", "Retardo centrado (fs) · gráfica", "Normalizada · gráfica", "Sentido"], f_h)
        w.set_row(0, 42)
        rngA, rngB = f"$A$2:$A${L}", f"$B$2:$B${L}"
        rngC, rngD, rngE = f"$C$2:$C${L}", f"$D$2:$D${L}", f"$E$2:$E${L}"
        P = {}
        panel = [
            ("npts", "Posiciones de la traza", f"=COUNT({rngA})", f_int),
            ("npts_b", "Lecturas de potencia escritas", f"=COUNT({rngB})", f_int),
            ("fondo", "Fondo (promedio de las alas, W)",
             f"=IF($M$3<$M$2,\"\",(AVERAGE(INDEX({rngB},1):INDEX({rngB},n_fondo))"
             f"+AVERAGE(INDEX({rngB},$M$3-n_fondo+1):INDEX({rngB},$M$3)))/2)", f_sci),
            ("maxd", "Máximo de la señal (W)", f"=IF($M$3<$M$2,\"\",MAX({rngD}))", f_sci),
            ("filapico", "Fila del máximo", f"=IFERROR(MATCH($M$5,{rngD},0)+1,\"\")", f_int),
            ("taupico", "Retardo del máximo (fs)", f"=IFERROR(INDEX($C$1:$C${L},$M$6),\"\")", f_calc),
            ("filaizq", "Fila del cruce izquierdo a media altura", f"=MAX($F$2:$F${L})", f_int),
            ("filader", "Fila del cruce derecho a media altura", f"=MIN($G$2:$G${L})", f_int),
            ("tauizq", "τ del cruce izquierdo (fs)", f"=IF($M$8>0,INDEX($H$1:$H${L},$M$8),\"\")", f_calc),
            ("tauder", "τ del cruce derecho (fs)", f"=IF($M$9>0,INDEX($H$1:$H${L},$M$9),\"\")", f_calc),
            ("fwhm", "Ancho de la traza a media altura Δτ_AC (fs)",
             "=IF(AND($M$8>0,$M$9>0),ABS($M$11-$M$10),\"\")", f_key),
            ("taup", "Ancho de pulso τp = factor × Δτ_AC (fs)", "=IF(ISNUMBER($M$12),factor_forma*$M$12,\"\")", f_key),
            ("taug", "Referencia: τp si fuera gaussiano (fs)", "=IF(ISNUMBER($M$12),0.7071*$M$12,\"\")", f_calc),
            ("centro", "Centro de la traza (fs)", "=IF(ISNUMBER($M$12),($M$10+$M$11)/2,$M$7)", f_calc),
            ("ptsfw", "Lecturas dentro del ancho a media altura", f"=COUNTIF({rngE},\">=0.5\")", f_int),
            ("rizq", "Recorrido a la izquierda del centro (fs)", f"=IFERROR($M$15-MIN({rngC}),\"\")", f_calc),
            ("rder", "Recorrido a la derecha del centro (fs)", f"=IFERROR(MAX({rngC})-$M$15,\"\")", f_calc),
            ("pico_pos", "Posición del pico (µm)", f"=IF($M$3<$M$2,\"\",IFERROR(INDEX($A$1:$A${L},$M$6),\"\"))", f_int),
            ("estado", "Estado de la traza",
             "=IF($M$3=0,\"Sin datos\",IF($M$3<$M$2,\"Incompleta: faltan lecturas de potencia\","
             "IF(OR($M$8=0,$M$9=0),\"Revisar: no se hallaron los dos cruces de media altura\","
             "IF($M$16<pts_min,\"Aviso: pocas lecturas dentro del ancho a media altura\","
             "IF(MIN($M$17,$M$18)<rec_min*$M$12,\"Aviso: el pico está corrido; el barrido no llega a una de las alas\","
             "\"OK\")))))", f_keyt),
        ]
        for i, (k, et, fo, fm) in enumerate(panel):
            P[k] = i + 1
            w.write(i + 1, 11, et, f_lab)
            w.write_formula(i + 1, 12, fo, fm)
        w.write(0, 11, f"Traza {nombre}" + (" · reposición" if num > N_REP else ""), f_h)
        w.write(0, 12, f"{amp:g} A", f_h)
        est = rc(P["estado"], 12)
        w.conditional_format(est, {"type": "cell", "criteria": "==", "value": '"OK"', "format": f_ok})
        w.conditional_format(est, {"type": "text", "criteria": "begins with", "value": "Aviso", "format": f_warn})
        w.conditional_format(est, {"type": "text", "criteria": "begins with", "value": "Revisar", "format": f_bad})
        fl = len(panel) + 2
        w.write(fl, 11, "Línea de media altura (gráfica)", f_sub)
        for j, cel in ((1, "$M$10"), (2, "$M$11")):
            w.write_formula(fl + j, 11, f"=IF(ISNUMBER($M$12),{cel}-$M$15,NA())", f_gray)
            w.write_formula(fl + j, 12, "=IF(ISNUMBER($M$12),0.5,NA())", f_gray)
        w.write(fl + 4, 11, "Solo se llena la columna B (potencia en W), en el orden de las posiciones.", f_note)

        for i in range(NP):
            R = i + 2
            w.write_number(i + 1, 0, POSICIONES[i], f_fijo)
            if datos is not None:
                w.write_number(i + 1, 1, datos[i], f_in_w)
            else:
                w.write_blank(i + 1, 1, None, f_in_w)
            nxt = f"E{R + 1}"
            w.write_formula(i + 1, 2, f"=IF(ISNUMBER(A{R}),A{R}*conv,\"\")", f_gray)
            w.write_formula(i + 1, 3, f"=IF(ISNUMBER(B{R}),AVERAGE(INDEX({rngB},MAX(1,{i + 1}-semi)):"
                                      f"INDEX({rngB},MIN($M$3,{i + 1}+semi))),\"\")", f_gsci)
            w.write_formula(i + 1, 4, f"=IF(AND(ISNUMBER(D{R}),ISNUMBER($M$4)),(D{R}-$M$4)/($M$5-$M$4),\"\")", f_gray3)
            w.write_formula(i + 1, 5, f"=IF(AND(ISNUMBER(E{R}),ISNUMBER({nxt}),ISNUMBER($M$6)),"
                                      f"IF(AND({R}<$M$6,E{R}<0.5,{nxt}>=0.5),{R},\"\"),\"\")", f_gray)
            w.write_formula(i + 1, 6, f"=IF(AND(ISNUMBER(E{R}),ISNUMBER({nxt}),ISNUMBER($M$6)),"
                                      f"IF(AND({R}>=$M$6,E{R}>=0.5,{nxt}<0.5),{R},\"\"),\"\")", f_gray)
            w.write_formula(i + 1, 7, f"=IF(OR(ISNUMBER(F{R}),ISNUMBER(G{R})),"
                                      f"C{R}+(0.5-E{R})*(C{R + 1}-C{R})/({nxt}-E{R}),\"\")", f_gray)
            w.write_formula(i + 1, 8, f"=IF(AND(ISNUMBER(E{R}),ISNUMBER($M$15)),C{R}-$M$15,NA())", f_gray)
            w.write_formula(i + 1, 9, f"=IF(ISNUMBER(E{R}),E{R},NA())", f_gray3)
            w.write_formula(i + 1, 10, f"=IF(AND(ISNUMBER(C{R}),ISNUMBER(C{R + 1})),SIGN(C{R + 1}-C{R}),\"\")", f_gray)
        w.conditional_format(1, 8, NP, 9, {"type": "errors", "format": F(font_color="#D9D9D9")})
        w.conditional_format(fl + 1, 11, fl + 2, 12, {"type": "errors", "format": F(font_color="#D9D9D9")})
        w.data_validation(1, 1, NP, 1, {"validate": "decimal", "criteria": "between", "minimum": -1, "maximum": 1,
                                        "error_title": "Potencia en W",
                                        "error_message": "Escribir la potencia en W, p. ej. 2.35E-05 (no en µW)."})

        ch1 = wb.add_chart({"type": "scatter", "subtype": "straight_with_markers"})
        ch1.add_series({"name": "Datos crudos", "categories": [w.name, 1, 0, NP, 0], "values": [w.name, 1, 1, NP, 1],
                        "marker": {"type": "circle", "size": 5, "fill": {"color": "#7F7F7F"}, "border": {"color": "#7F7F7F"}},
                        "line": {"color": "#BFBFBF", "width": 0.75}})
        ch1.set_title({"name": "Traza cruda: potencia óptica contra posición", "name_font": {"size": 11}})
        ch1.set_x_axis({"name": "Posición del micrómetro (µm)", "min": 0, "max": POSICIONES[-1],
                        "major_gridlines": {"visible": False}})
        ch1.set_y_axis({"name": "Potencia óptica (W)", "num_format": "0.0E+00",
                        "major_gridlines": {"visible": True, "line": {"color": "#EEEEEE"}}})
        ch1.set_legend({"none": True})
        ch1.show_blanks_as("gap")
        ch1.set_size({"width": 620, "height": 300})
        w.insert_chart(fl + 6, 11, ch1)
        ch2 = wb.add_chart({"type": "scatter", "subtype": "straight_with_markers"})
        ch2.add_series({"name": "Traza normalizada", "categories": [w.name, 1, 8, NP, 8], "values": [w.name, 1, 9, NP, 9],
                        "marker": {"type": "circle", "size": 5, "fill": {"color": "#1F3864"}, "border": {"color": "#1F3864"}},
                        "line": {"color": "#8EA9DB", "width": 0.75}})
        ch2.add_series({"name": "Ancho a media altura", "categories": [w.name, fl + 1, 11, fl + 2, 11],
                        "values": [w.name, fl + 1, 12, fl + 2, 12],
                        "marker": {"type": "diamond", "size": 7, "fill": {"color": "#C00000"}, "border": {"color": "#C00000"}},
                        "line": {"color": "#C00000", "width": 2}})
        ch2.set_title({"name": "Autocorrelación normalizada contra retardo", "name_font": {"size": 11}})
        ch2.set_x_axis({"name": "Retardo respecto al centro (fs)", "major_gridlines": {"visible": False}})
        ch2.set_y_axis({"name": "Señal normalizada", "min": -0.1, "max": 1.1,
                        "major_gridlines": {"visible": True, "line": {"color": "#EEEEEE"}}})
        ch2.set_legend({"position": "bottom"})
        ch2.show_na_as_empty_cell()
        ch2.set_size({"width": 620, "height": 320})
        w.insert_chart(fl + 22, 11, ch2)
        w.protect("", {"format_columns": True, "format_rows": True, "select_locked_cells": True,
                       "select_unlocked_cells": True})
        return P

    P = None
    for k, (w, n) in enumerate(zip(ws_tr, trazas)):
        d = datos[k] if datos and k < len(datos) else None
        P = hoja_traza(w, n, k + 1, d)
    cel = lambda clave_: f"$M${P[clave_] + 1}"

    # ============================================================ Registro
    w = ws_reg
    anchos = {"A": 5, "B": 8, "C": 16, "D": 11, "E": 11, "F": 11, "G": 12, "H": 13, "I": 9, "J": 36,
              "K": 12, "L": 12, "M": 36, "N": 12}
    for col, a in anchos.items():
        w.set_column(f"{col}:{col}", a)
    w.write("A1", f"Registro de la medición · {amp:g} A ({clave})", f_tit)
    w.write("A2", "Amarillo = llenar. Nueve réplicas seguidas a la misma corriente; R10–R12 solo si hay que reponer "
            "una traza descartada.", f_sub)
    w.write("A4", "Fecha", f_labb)
    w.merge_range("B4:C4", fecha, f_in)
    w.write("D4", "Encendido del láser", f_labb)
    w.write("E4", "", f_in_t)
    w.write("F4", "Corriente (A)", f_labb)
    w.write_formula("G4", "=corriente", f_link)
    w.write("H4", "Temperatura del laboratorio (°C)", f_labb)
    w.write("I4", "", f_in_num)
    w.write("J4", "Responsables:", f_labb)
    w.merge_range("K4:M4", "", f_in)
    w.set_row(3, 30)
    H0 = 5                                          # fila (base 0) del encabezado
    w.write_row(H0, 0, ["N°", "Hoja", "Hora inicio", "Hora fin", "Duración (min)", "Δ inicio a la siguiente (min)",
                        "Potencia media del láser (mW)", "Posición del pico (µm)", "¿Válida?",
                        "Observaciones (causa si no es válida)", "Δτ_AC (fs)", "τp (fs)", "Estado de la traza",
                        "τp usable (fs)"], f_h)
    w.set_row(H0, 42)
    r1 = H0 + 2                                     # primera fila Excel de datos
    nt = len(trazas)
    r2 = r1 + nt - 1
    for k in range(nt):
        R = H0 + 1 + k
        E = R + 1
        w.write_number(R, 0, k + 1, f_int)
        w.write_url(R, 1, f"internal:'{trazas[k]}'!A1", string=trazas[k], cell_format=f_linkt)
        w.write_blank(R, 2, None, f_in_t)
        w.write_blank(R, 3, None, f_in_t)
        w.write_formula(R, 4, f"=IF(AND(ISNUMBER(C{E}),ISNUMBER(D{E})),(D{E}-C{E})*1440,\"\")", f_calc)
        if k < nt - 1:
            w.write_formula(R, 5, f"=IF(AND(ISNUMBER(C{E}),ISNUMBER(C{E + 1})),(C{E + 1}-C{E})*1440,\"\")", f_calc)
        else:
            w.write_blank(R, 5, None, f_calc)
        w.write_blank(R, 6, None, f_in_num)
        w.write_formula(R, 7, f"=IFERROR({q(trazas[k])}!{cel('pico_pos')}+0,\"\")", F(border=1, font_color="#008000", num_format="0"))
        w.write(R, 8, "Sí" if k < N_REP else "", f_in)
        w.write(R, 9, "" if k < N_REP else "Reposición: anotar qué traza reemplaza", f_in_txt)
        w.write_formula(R, 10, f"=IFERROR({q(trazas[k])}!{cel('fwhm')}+0,\"\")", f_link)
        w.write_formula(R, 11, f"=IFERROR({q(trazas[k])}!{cel('taup')}+0,\"\")", f_link)
        w.write_formula(R, 12, f"={q(trazas[k])}!{cel('estado')}", f_linkt)
        w.write_formula(R, 13, f"=IF(AND(ISNUMBER(L{E}),I{E}<>\"No\"),L{E},\"\")", f_calc)
    w.data_validation(f"I{r1}:I{r2}", {"validate": "list", "source": ["Sí", "No"]})
    w.data_validation(f"C{r1}:D{r2}", {"validate": "time", "criteria": "between", "minimum": 0, "maximum": 0.99999,
                                       "error_message": "Escribir la hora como hh:mm, p. ej. 14:35"})
    rng_est = f"M{r1}:M{r2}"
    w.conditional_format(rng_est, {"type": "cell", "criteria": "==", "value": '"OK"', "format": f_ok})
    w.conditional_format(rng_est, {"type": "text", "criteria": "begins with", "value": "Aviso", "format": f_warn})
    w.conditional_format(rng_est, {"type": "text", "criteria": "begins with", "value": "Revisar", "format": f_bad})
    w.conditional_format(f"A{r1 + N_REP}:M{r2}", {"type": "no_errors", "format": F(bg_color="#F2F2F2")})
    rr = r2
    w.write(rr + 1, 3, "Media", f_labb)
    w.write_formula(rr + 1, 4, f"=IF(COUNT(E{r1}:E{r2})=0,\"\",AVERAGE(E{r1}:E{r2}))", f_calc)
    w.write_formula(rr + 1, 5, f"=IF(COUNT(F{r1}:F{r2})=0,\"\",AVERAGE(F{r1}:F{r2}))", f_calc)
    w.write(rr + 2, 3, "Total (h)", f_labb)
    w.write_formula(rr + 2, 4, f"=IF(COUNT(C{r1}:D{r2})<2,\"\",(MAX(D{r1}:D{r2})-MIN(C{r1}:C{r2}))*24)", f_calc)
    w.write(rr + 2, 5, "del primer inicio al último fin", f_note)
    w.merge_range(rr + 4, 0, rr + 4, 12, "Reglas del protocolo (sección 5): una traza solo se marca «No» por una causa "
                  "anotada en el momento (el láser perdió los pulsos, la potencia salió de rango, el barrido se "
                  "interrumpió). Nunca por dar un valor inesperado. La traza que la reemplaza va en la siguiente hoja "
                  "de reposición (R10, R11, R12), y se anota en Observaciones a cuál reemplaza.", f_note)
    w.set_row(rr + 4, 40)
    w.freeze_panes(H0 + 1, 0)

    # ============================================================ Resumen
    w = ws_res
    w.set_column("A:A", 52)
    w.set_column("B:B", 16)
    w.set_column("C:C", 60)
    w.write("A1", f"Resumen y prueba t de una muestra · {amp:g} A", f_tit)
    w.write("A2", "Cuentan las trazas con τp calculado y no marcadas «No» en el Registro (incluidas las de reposición).",
            f_sub)
    reg = q(S_REG)
    tp = f"{reg}!$N${r1}:$N${r2}"
    w.write_row(3, 0, ["Cálculo", "Valor", "Nota"], f_h)
    filas = [
        ("n", "Réplicas válidas n", f"=COUNT({tp})", f_int, f"Meta: {N_REP}."),
        ("media", "Media de τp, ȳ (fs)", f"=IF(B5=0,\"\",AVERAGE({tp}))",
         f_key, "Estimador: ancho a media altura × factor sech²."),
        ("S", "Desviación estándar S (fs)",
         f"=IF(B5<2,\"\",STDEV.S({tp}))", f_key, ""),
        ("cv", "Coeficiente de variación (%)", "=IF(ISNUMBER(B7),100*B7/B6,\"\")", f_calc, ""),
        ("tau0r", "τ0 del fabricante (fs)", "=tau0", f_link, "Tabla 5 de la hoja de pruebas."),
        ("dif", "ȳ − τ0 (fs)", "=IF(ISNUMBER(B6),B6-B9,\"\")", f_calc, ""),
        ("t0", "Estadístico t0 = (ȳ − τ0) / (S/√n)", "=IF(ISNUMBER(B7),B10/(B7/SQRT(B5)),\"\")", f_calc3,
         "H0: μ = τ0   frente a   H1: μ ≠ τ0."),
        ("gl", "Grados de libertad n − 1", "=IF(B5>1,B5-1,\"\")", f_int, ""),
        ("tcrit", "t crítico t(α/2, n − 1)", "=IF(ISNUMBER(B12),T.INV.2T(alfa,B12),\"\")", f_calc3, ""),
        ("p", "Valor P (dos colas)", "=IF(ISNUMBER(B11),T.DIST.2T(ABS(B11),B12),\"\")", f_calc4, ""),
        ("li", "Límite inferior del IC 95 % de μ (fs)", "=IF(ISNUMBER(B13),B6-B13*B7/SQRT(B5),\"\")", f_calc, ""),
        ("ls", "Límite superior del IC 95 % de μ (fs)", "=IF(ISNUMBER(B13),B6+B13*B7/SQRT(B5),\"\")", f_calc, ""),
        ("dec", "Decisión",
         "=IF(ISNUMBER(B14),IF(B14<alfa,\"Se rechaza H0: el ancho medido difiere de τ0\","
         "\"No se rechaza H0: no hay evidencia de diferencia con τ0\"),\"\")", f_keyt, ""),
        ("dur", "Duración media por corrida (min)", f"={reg}!E{rr + 2}", f_link, "Desde el Registro."),
    ]
    for i, (_, et, fo, fm, nota) in enumerate(filas):
        w.write(4 + i, 0, et, f_lab)
        w.write_formula(4 + i, 1, fo, fm)
        w.write(4 + i, 2, nota, f_note)
    w.set_row(4 + 12, 30)
    w.write(4 + len(filas) + 1, 0, "Prueba preliminar con el estimador de la hoja (FWHM × 0,65). El informe usa el "
            "ajuste sech² de toda la traza (analiza_piloto.py) y valida los supuestos (normalidad, sin tendencia en "
            "el orden de medición).", f_note)
    ch = wb.add_chart({"type": "scatter"})
    ch.add_series({"name": "τp por réplica", "categories": [S_REG, H0 + 1, 0, H0 + nt, 0],
                   "values": [S_REG, H0 + 1, 13, H0 + nt, 13],
                   "marker": {"type": "circle", "size": 7, "fill": {"color": "#1F3864"}, "border": {"color": "#1F3864"}}})
    ch.set_title({"name": "τp en el orden de medición (¿hay deriva?)", "name_font": {"size": 11}})
    ch.set_x_axis({"name": "N° de corrida", "min": 0, "max": nt + 1, "major_unit": 1,
                   "major_gridlines": {"visible": False}})
    ch.set_y_axis({"name": "τp (fs)", "major_gridlines": {"visible": True, "line": {"color": "#EEEEEE"}}})
    ch.set_legend({"none": True})
    ch.set_size({"width": 560, "height": 300})
    w.insert_chart("E4", ch)
    wb.close()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--prueba", action="store_true", help="llena las trazas con datos sintéticos (en el scratchpad)")
    ap.add_argument("--carpeta", type=Path, default=CARPETA)
    args = ap.parse_args()
    args.carpeta.mkdir(parents=True, exist_ok=True)
    medidos = {"I1": 200.0, "I2": 145.0, "I3": 148.0}           # τp del piloto, solo para --prueba
    for amp, clave, tau0, pfab, fecha in CORRIENTES:
        nombre = f"Medicion_{amp:g}A_Autocorrelador.xlsx"
        datos = None
        if args.prueba:
            rng = np.random.default_rng(int(amp))
            datos = [traza_sintetica(medidos[clave] + 4 * rng.standard_normal(), int(amp) * 100 + k)
                     for k in range(N_REP)]
        build(args.carpeta / nombre, amp, clave, tau0, pfab, fecha, datos)
        print(args.carpeta / nombre)


if __name__ == "__main__":
    main()
