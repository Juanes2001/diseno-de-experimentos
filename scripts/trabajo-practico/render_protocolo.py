#!/usr/bin/env python3
"""Genera el protocolo del experimento de comparación simple (HTML para imprimir en PDF).

Uso: render_protocolo.py salida.html

Versión del 23 oct 2026 en lenguaje simple para la profesora. Las hipótesis quedan pendientes
de la hoja de pruebas del fabricante; el procedimiento, el piloto y el número de réplicas
están fijados. El PDF se imprime con Chrome desde build_protocolo.sh (KaTeX desde el CDN).
"""
import html
import sys

import numpy as np
from scipy import stats

FECHA = "23 de octubre de 2026"

KATEX = (
    '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.16.11/katex.min.css">'
    '<script src="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.16.11/katex.min.js"></script>'
    '<script src="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.16.11/contrib/auto-render.min.js"></script>'
)
KATEX_RUN = (
    "<script>renderMathInElement(document.body,{throwOnError:false,delimiters:["
    '{left:"$$",right:"$$",display:true},{left:"$",right:"$",display:false}]});</script>'
)


def potencia_1m(delta, sigma, n, alpha=0.05, dos_colas=False):
    """Potencia exacta de la prueba t de una muestra (t no central)."""
    df = n - 1
    nc = delta / sigma * np.sqrt(n)
    tc = stats.t.ppf(1 - alpha / 2, df) if dos_colas else stats.t.ppf(1 - alpha, df)
    return 1 - stats.nct.cdf(tc, df, nc)


def delta_detectable_1m(sigma, n, alpha=0.05, potencia=0.90, dos_colas=False):
    """Menor delta (fs) que la prueba t de una muestra detecta con la potencia dada."""
    lo, hi = 0.01, 200.0
    for _ in range(60):
        mid = (lo + hi) / 2
        if potencia_1m(mid, sigma, n, alpha, dos_colas) >= potencia:
            hi = mid
        else:
            lo = mid
    return hi


def n_minimo_1m(delta, sigma, alpha=0.05, potencia=0.90, dos_colas=False):
    for n in range(3, 1000):
        if potencia_1m(delta, sigma, n, alpha, dos_colas) >= potencia:
            return n
    return None

ASESORIA = "sábado 24 de octubre de 2026"

# ----------------------------------------------------------------------------- estilo

CSS = """
@page { size: A4; margin: 20mm 18mm 20mm 18mm;
        @bottom-center { content: counter(page); font: 9pt Calibri, 'Segoe UI', Arial, sans-serif; color: #5b6b73; } }
* { box-sizing: border-box; }
body { font: 11pt/1.5 Calibri, 'Segoe UI', Arial, sans-serif; color: #142b33; margin: 0; }
h1, h2, h3, h4 { font-family: Cambria, Georgia, serif; color: #0f4c5c; line-height: 1.2; }
.portada { height: 250mm; display: flex; flex-direction: column; justify-content: center; page-break-after: always; }
.portada h1 { font-size: 26pt; margin: 0 0 6mm; }
.portada .sub { font-size: 14pt; color: #5b6b73; margin: 0 0 16mm; }
.portada .meta { font-size: 11.5pt; }
.portada .como { margin-top: 14mm; background: #e8f1f3; border-radius: 6px; padding: 5mm 6mm; font-size: 10.5pt; }
h2 { font-size: 18pt; margin: 0 0 2mm; page-break-before: always; }
h2.first { page-break-before: auto; }
h2 .n { display: inline-block; background: #e36414; color: #fff; border-radius: 50%; width: 11mm; height: 11mm;
        line-height: 11mm; text-align: center; font-size: 14pt; margin-right: 3mm; }
.secsub { color: #5b6b73; margin: 0 0 5mm; font-size: 11.5pt; }
h3 { font-size: 13pt; margin: 5mm 0 2mm; break-after: avoid; }
h4 { font-size: 11.5pt; margin: 3mm 0 1.5mm; break-after: avoid; }
p { margin: 0 0 2.4mm; text-align: justify; }
table { border-collapse: collapse; width: 100%; margin: 0 0 3mm; font-size: 9.6pt; break-inside: avoid; }
th { background: #0f4c5c; color: #fff; padding: 1.4mm 2mm; text-align: center; font-weight: 700; }
td { padding: 1.2mm 2mm; border-bottom: 0.3pt solid #d5dee1; text-align: center; vertical-align: middle; }
td.l, th.l { text-align: left; }
tr.hl td { background: #fde8d7; }
ul, ol { margin: 0 0 3mm; padding-left: 6mm; } li { margin: 0 0 1.2mm; text-align: justify; }
ol.pasos > li { margin: 0 0 2.2mm; }
.form { background: #e8f1f3; border-radius: 5px; padding: 2.5mm 4mm; margin: 0 0 3mm; text-align: center;
        font-family: 'Cambria Math', Cambria, serif; color: #0f4c5c; font-size: 12pt; break-inside: avoid; }
.katex-display { margin: 1.5mm 0 2.5mm; } .katex { font-size: 1.02em; }
.eq { background: #e8f1f3; border-radius: 5px; padding: 1.5mm 4mm; margin: 0 0 3mm; break-inside: avoid; }
.eq p { margin: 0 0 1mm; } .eq .ref { color: #5b6b73; font-size: 9.3pt; text-align: right; }
.nota { background: #fde8d7; border-radius: 5px; padding: 2.2mm 4mm; margin: 0 0 3mm; break-inside: avoid; }
.ok { background: #e8f1f3; border-radius: 5px; padding: 2.2mm 4mm; margin: 0 0 3mm; break-inside: avoid; }
.s { color: #5b6b73; font-size: 9.5pt; }
.ruta { margin: 0 0 3mm; } .ruta span { display: inline-block; background: #0f4c5c; color: #fff; font-weight: 700;
        border-radius: 4px; padding: 0.8mm 2.5mm; font-size: 9.5pt; } .ruta span.fin { background: #e36414; }
.ruta i { color: #5b6b73; font-style: normal; margin: 0 1.5mm; }
.hoja td { height: 7.5mm; border: 0.3pt solid #c9d6da; } .hoja th { font-size: 9pt; }
.hoja td.l { text-align: left; }
.hoja.alta td { height: 9mm; }
.pend { display: inline-block; border: 0.6pt dashed #e36414; color: #e36414; border-radius: 3px; padding: 0 2mm;
        font-size: 9.5pt; font-weight: 700; }
.firma { margin-top: 12mm; display: flex; gap: 10mm; } .firma div { flex: 1; border-top: 0.6pt solid #142b33; padding-top: 2mm; font-size: 10pt; }
.ref { font-size: 9.8pt; margin: 0 0 2mm; padding-left: 6mm; text-indent: -6mm; text-align: left; }
"""

# ----------------------------------------------------------------------------- utilidades


def ruta(*pasos):
    out = []
    for i, p in enumerate(pasos):
        cls = ' class="fin"' if i == len(pasos) - 1 else ""
        out.append(f"<span{cls}>{html.escape(p)}</span>")
    return '<p class="ruta">' + "<i>›</i>".join(out) + "</p>"


def tabla(filas, cab=None, izq=(0,), hl=(), cls="", widths=None):
    o = [f'<table class="{cls}">' if cls else "<table>"]
    if widths:
        o.append("<colgroup>" + "".join(f'<col style="width:{w}">' for w in widths) + "</colgroup>")
    if cab:
        o.append("<tr>" + "".join(f'<th{" class=l" if i in izq else ""}>{c}</th>' for i, c in enumerate(cab)) + "</tr>")
    for r, fila in enumerate(filas):
        c2 = ' class="hl"' if r in hl else ""
        o.append(f"<tr{c2}>" + "".join(f'<td{" class=l" if i in izq else ""}>{c}</td>' for i, c in enumerate(fila)) + "</tr>")
    o.append("</table>")
    return "".join(o)


def hoja(cab, n, izq=(0,), alta=False):
    """Tabla en blanco para llenar a mano."""
    filas = [[""] * len(cab) for _ in range(n)]
    return tabla(filas, cab=cab, izq=izq, cls="hoja alta" if alta else "hoja")


def seccion(n, titulo, sub, first=False):
    cls = ' class="first"' if first else ""
    return f'<h2{cls}><span class="n">{n}</span>{titulo}</h2><p class="secsub">{sub}</p>'


PEND = '<span class="pend">por definir</span>'

# ----------------------------------------------------------------------------- contenido


def build(out):
    o = ['<!doctype html><html lang="es"><head><meta charset="utf-8">',
         "<title>Protocolo · Comparación simple del ancho de pulso</title>", KATEX, f"<style>{CSS}</style></head><body>"]

    # ---------------------------------------------------------------- portada
    o.append(
        '<div class="portada"><h1>Protocolo del experimento: ¿el láser Carmel CFL-05RFFUNC sigue dando el ancho de pulso '
        'que midió el fabricante?</h1>'
        '<p class="sub">Trabajo práctico · Diseño de comparación simple (Montgomery, cap. 2)</p>'
        f'<p class="meta">Diseño de Experimentos Avanzados (3008475)<br>Universidad Nacional de Colombia · 2026-II<br>'
        f'Juan Esteban Rodríguez Ochoa · Sebastián Zapata Henao<br>Versión para la asesoría del {ASESORIA}<br>'
        f'Fecha del documento: {FECHA}</p>'
        '<div class="como"><b>En una frase.</b> Vamos a medir el ancho de pulso del láser con el autocorrelador que '
        'construimos y compararlo con el ancho que el fabricante midió en este mismo láser cuando lo entregó, a tres '
        'corrientes de operación.<br><br>'
        '<b>Dos cosas que hay que saber para leer este documento.</b> (1) El valor de referencia del fabricante está en la '
        'hoja de pruebas que vino con el equipo, que todavía no tenemos en la mano; por eso las hipótesis quedan marcadas '
        f'{PEND} y se escribirán cuando tengamos esos números. (2) El láser va a ser retirado del laboratorio, así que '
        'todos los datos se toman entre el sábado 24 y el miércoles 28 de octubre de 2026. El procedimiento de medición y '
        'el método para fijar el número de réplicas no dependen del valor de referencia, y por eso se pueden aprobar ya.</div></div>')

    # ---------------------------------------------------------------- 0. resumen
    o.append(seccion("0", "¿Qué se propone?", "Resumen en una página", first=True))
    o.append(tabla([
        ["Pregunta", "¿El láser entrega hoy, a cada corriente de operación, pulsos tan cortos como los que midió el "
                     "fabricante cuando lo entregó?"],
        ["Tipo de diseño", "Comparación simple: la media de una muestra frente a un valor conocido (Montgomery, cap. 2, "
                           "sec. 2-4.6). Se hace una comparación por cada corriente."],
        ["Valor de referencia", "El ancho de pulso que el fabricante midió en este láser a cada corriente (hoja de pruebas "
                                "de fábrica). Si la hoja no aparece, se usa el máximo que garantiza el modelo: 90 fs."],
        ["Variable respuesta", "Ancho de pulso τ<sub>p</sub>, en femtosegundos (fs). Se obtiene de la traza del "
                               "autocorrelador con el mismo método que usa el fabricante."],
        ["Factor y niveles", "Corriente del láser, en tres valores de operación: I<sub>1</sub>, I<sub>2</sub> e I<sub>3</sub>, los que "
                             "lista la hoja de pruebas. Cada uno tiene su propio valor de referencia."],
        ["Hipótesis", PEND + ". Se escriben cuando se tengan los valores de referencia (sección 3)."],
        ["Réplica", "Una traza completa del autocorrelador, tomada de forma independiente de las demás (sección 4)."],
        ["Cuántas réplicas", "Todavía no se sabe: se calcula el sábado por la noche. Hoy sábado 24 se hace una prueba piloto "
                             "con <b>solo 5 réplicas por corriente</b> (15 trazas en total), cuyo único fin es estimar la "
                             "variabilidad y, con la curva OC de Montgomery, el número de réplicas n del experimento real. Ese "
                             "n se reparte en partes iguales entre las tres corrientes y los días de medición (sección 4)."],
        ["Orden de medición", "Cada día se sortea el orden de todas las trazas del día. Nunca se miden todas las de una "
                              "corriente seguidas."],
        ["Calendario", "Sáb 24: piloto. Lun 26, mar 27 y mié 28: medición. Jue 29: reserva. Desde el vie 30: desmontaje."],
        ["Supuestos", "Normalidad: gráfica de probabilidad normal y prueba de Anderson-Darling. Independencia: orden "
                      "sorteado y gráfica de los datos contra el orden."],
        ["Software", "Minitab (Estadísticas › Estadísticas básicas; Gráfica › Gráfica de probabilidad)."],
        ["Qué se pide aprobar hoy", "El valor de referencia, la definición de réplica, el piloto, el plan de tres días con "
                                    "orden sorteado y el procedimiento de medición. Las hipótesis se traen después."],
    ], cab=["Elemento", "Decisión"], izq=(0, 1)))

    # ---------------------------------------------------------------- 1. fabricante
    o.append(seccion("1", "¿Qué sabemos del láser y de su fabricante?", "Lo confirmado en el laboratorio y lo que dicen las hojas de datos públicas"))
    o.append(tabla([
        ["Fabricante y modelo", "Calmar Laser, Carmel CFL-05RFFUNC. Es un láser de fibra de femtosegundos de 780 nm y 0,5 W, "
                                "hecho a pedido (el sufijo UNC no aparece en ningún catálogo)."],
        ["Datos confirmados", "780 nm, 50 MHz, salida en espacio libre, número de serie 881139, corriente ajustable de 0 a 7,12 A."],
        ["Edad", "Más de nueve años en el laboratorio (compra alrededor de 2016 o 2017)."],
        ["Ancho de pulso según las hojas públicas", "Menos de 90 fs. Valor típico de la traza de ejemplo: 87 fs."],
        ["Cómo lo mide el fabricante", "Con autocorrelación de segundo armónico, la misma técnica de nuestro montaje. "
                                       "Supone pulso sech² y multiplica el ancho de la traza por 0,65."],
        ["Lo que las hojas públicas no traen", "El ancho de pulso a cada corriente. Ese dato solo está en la hoja de pruebas "
                                               "que vino con el equipo."],
    ], cab=["Dato", "Valor"], izq=(0, 1)))
    o.append("<p>Se revisaron todas las hojas de datos del modelo desde 2012 hasta 2025, el catálogo 2023 y el sitio del "
             "fabricante. En todas el método de medición es el mismo. Lo único que cambió con los años fue el máximo "
             "garantizado: menos de 100 fs en 2012, menos de 90 fs desde 2016.</p>")

    # ---------------------------------------------------------------- 2. datos que faltan
    o.append(seccion("2", "¿Qué datos del fabricante faltan?", "Formularios para llenar con la hoja de pruebas y el manual del equipo"))
    o.append("<p>Dónde buscar: la caja del equipo, la carpeta del laboratorio, la memoria o el PC con el software de Calmar, "
             "la orden de compra. Si no aparece, se escribe a sales@calmarlaser.com con el número de serie 881139 pidiendo "
             "la hoja de pruebas de fábrica con el ancho de pulso por corriente, su tolerancia y el criterio de aceptación.</p>")
    o.append("<h3>Formulario 1 · Identidad del equipo</h3>")
    o.append(tabla([
        ["Modelo completo (etiqueta del controlador)", ""],
        ["Número de serie", "<b>881139</b>"],
        ["Fecha de fabricación o de prueba", ""],
        ["Longitud de onda (nm)", "<b>780</b>"],
        ["Tasa de repetición (MHz)", "<b>50</b>"],
        ["Potencia media nominal (mW)", ""],
        ["Rango de corriente (A)", "0 – 7,12 (confirmar en el manual)"],
        ["Tipo de salida", "<b>Espacio libre</b>"],
        ["Documentos encontrados (nombre, fecha, dónde estaban)", ""],
    ], cab=["Dato", "Valor"], izq=(0, 1), cls="hoja"))
    o.append('<h3 style="page-break-before:always">Formulario 2 · Ancho de pulso por corriente, según la hoja de pruebas (indispensable)</h3>')
    o.append("<p>Una fila por cada corriente que liste la hoja. Copiar los valores tal como aparecen, sin redondear.</p>")
    o.append(hoja(["Corriente (A)", "Potencia (mW)", "Ancho de pulso τ<sub>p</sub> (fs)", "Ancho de la traza (fs)",
                   "Forma y factor", "λ<sub>c</sub> (nm)", "Δλ (nm)", "Tolerancia", "Medido o típico"], 7, izq=(), alta=True))
    o.append("<h4>Cómo midió el fabricante</h4>")
    o.append(tabla([
        ["Instrumento (modelo del autocorrelador)", ""],
        ["Dónde midió (salida del cabezal u otro punto)", ""],
        ["Temperatura y tiempo de calentamiento", ""],
        ["Forma de pulso supuesta y factor usado", ""],
        ["Fecha y firma de la prueba", ""],
    ], cab=["Condición", "Valor"], izq=(0, 1), cls="hoja"))
    o.append("<h4>Datos que fijan la diferencia δ que importa detectar (basta uno; ver la regla en la sección 4)</h4>")
    o.append(tabla([
        ["(a) Tolerancia del ancho medido (τ<sub>0</sub> ± t)", ""],
        ["(b) Máximo garantizado (fs)", "&lt; 90 fs según la hoja pública; confirmar"],
        ["(c) Incertidumbre de la medición del fabricante (± u)", ""],
        ["(d) Criterio de aceptación de la prueba final", ""],
        ["(e) Estabilidad del ancho de pulso declarada (% rms)", ""],
    ], cab=["Dato", "Valor"], izq=(0, 1), cls="hoja"))
    o.append("<h3>Formulario 3 · Datos complementarios</h3>")
    o.append(tabla([
        ["Del manual", "Corriente mínima con pulsos estables; corriente máxima permitida; cómo se ajusta la corriente; "
                       "tiempo de calentamiento recomendado", ""],
        ["Del laboratorio", "Horas de uso; reparaciones; cambios en la salida; mediciones anteriores del ancho de pulso", ""],
    ], cab=["Fuente", "Dato", "Valor"], izq=(0, 1, 2), cls="hoja", widths=("14%", "50%", "36%")))

    # ---------------------------------------------------------------- 3. hipótesis
    o.append(seccion("3", "¿Cuáles son las hipótesis?", "Pendientes hasta tener los valores de referencia"))
    o.append("<p>Las hipótesis comparan la media del ancho de pulso medido a una corriente con el valor τ<sub>0</sub> que el "
             "fabricante midió a esa misma corriente. No se escriben todavía porque faltan los valores τ<sub>0</sub>. Cuando "
             "lleguen, se decide también si la prueba es de una o de dos colas: dos colas si τ<sub>0</sub> es un valor "
             "medido (cualquier cambio importa); una cola si solo se tiene el máximo garantizado (solo importa que el pulso "
             "sea más largo).</p>")
    o.append(tabla([
        ["Corriente I<sub>1</sub> = ____ A", "H<sub>0</sub>: μ<sub>1</sub> = τ<sub>0,1</sub>", "H<sub>A</sub>: " + PEND, PEND],
        ["Corriente I<sub>2</sub> = ____ A", "H<sub>0</sub>: μ<sub>2</sub> = τ<sub>0,2</sub>", "H<sub>A</sub>: " + PEND, PEND],
        ["Corriente I<sub>3</sub> = ____ A", "H<sub>0</sub>: μ<sub>3</sub> = τ<sub>0,3</sub>", "H<sub>A</sub>: " + PEND, PEND],
    ], cab=["Nivel", "Hipótesis nula", "Hipótesis alterna", "Valor de referencia τ<sub>0</sub> (fs)"], izq=(0,), cls="hoja"))
    o.append("<p>Lo que sí está decidido: el estadístico es la t de Student de una muestra con n − 1 grados de libertad, "
             "porque la varianza no se conoce y se estima con las réplicas (fórmulas en el anexo A). Medir antes de escribir "
             "las hipótesis es válido: el valor τ<sub>0</sub> no interviene en la toma de datos, solo en la prueba. Lo que debe "
             "quedar fijo antes de medir es el diseño, y eso es lo que fijan las secciones 4 y 5.</p>")

    # ---------------------------------------------------------------- 4. réplicas
    o.append(seccion("4", "¿Qué es una réplica y cuántas se harán?", "Definiciones del diseño, prueba piloto y número de réplicas"))
    o.append(tabla([
        ["Unidad experimental", "Una traza completa del autocorrelador (un barrido del retardo) a una corriente fija."],
        ["Variable respuesta", "τ<sub>p</sub> en fs: se resta el fondo de la traza, se ajusta la forma sech², se lee el ancho a "
                               "media altura y se multiplica por 0,65 (el factor del fabricante)."],
        ["Réplica", "Una traza nueva e independiente. Entre una réplica y la siguiente se bloquea el haz unos segundos y se "
                    "reinicia el barrido desde otra posición. Dos lecturas del mismo barrido no son dos réplicas."],
        ["Niveles", "Tres corrientes de operación, I<sub>1</sub>, I<sub>2</sub> e I<sub>3</sub>, las que lista la hoja de pruebas. Las tres "
                    "tienen el mismo número de réplicas y en cada una se hace la misma comparación."],
        ["Orden", "Cada día se miden las tres corrientes con el mismo número de réplicas cada una, en un orden sorteado "
                  "de antemano. Cuántas por día lo dice el n calculado el sábado."],
        ["Papel del día", "El día no es un factor. Todas las réplicas de una corriente forman una sola muestra; la variación "
                          "entre días queda dentro de la desviación estándar. Como cada día tiene el mismo número de réplicas "
                          "por corriente, si al final el día resultara importante se puede analizar como bloque sin cambiar "
                          "nada de la toma de datos."],
        ["Error experimental", "Fluctuaciones del láser y ruido del detector. Es lo que miden las réplicas."],
    ], cab=["Elemento", "Definición"], izq=(0, 1)))

    o.append("<h3>Prueba piloto: sábado 24 de octubre</h3>")
    o.append("<p>Para saber cuántas réplicas hacen falta hay que conocer antes la variabilidad del ancho medido. La única "
             "forma de conocerla es medir. El piloto es pequeño: <b>solo 5 réplicas por cada corriente</b>, 15 trazas en "
             "total. No es el experimento; sirve únicamente para estimar el número de réplicas del experimento real. Se "
             "hace el sábado, aparte de los días de medición, así:</p>")
    o.append('<ol class="pasos">'
             "<li>Poner el láser en cada una de las tres corrientes y confirmar con una traza rápida que da pulsos estables.</li>"
             "<li>Tomar <b>5 réplicas por corriente</b> (5 en I<sub>1</sub>, 5 en I<sub>2</sub>, 5 en I<sub>3</sub>; 15 trazas en total), en "
             "orden sorteado y con el procedimiento completo de la sección 5. Estas trazas no entran al análisis final; "
             "sirven para estimar la variabilidad de cada corriente y ensayar el procedimiento.</li>"
             "<li>Cronometrar cada réplica, incluido el cambio de corriente, para saber cuántas trazas caben en un día.</li>"
             "<li>Esa noche: calcular la desviación estándar S de cada corriente y decidir el número de réplicas (abajo).</li></ol>")

    o.append("<h3>Número de réplicas</h3>")
    o.append("<p>Se usa el método de Montgomery (sec. 2-4.2): fijar la diferencia δ que importa detectar, estimar la "
             "desviación estándar σ, fijar los riesgos, y leer el número de réplicas n en la curva OC. En cuatro pasos:</p>")
    o.append('<ol class="pasos">'
             "<li><b>σ.</b> Se toma la mayor de las tres S del piloto y se multiplica por 1,56. Con solo 5 datos, S suele "
             "quedarse corta; 1,56 · S es el límite superior de confianza del 80 % para σ y es la estimación conservadora "
             "que pide Montgomery.</li>"
             "<li><b>δ.</b> Es la diferencia entre el ancho de hoy y el del fabricante que ya importaría. La fija el primer "
             "dato del fabricante que exista, según la tabla siguiente. Si no hay ninguno, δ = 10 fs.</li>"
             "<li><b>Riesgos.</b> α = 0,05 y potencia 0,90.</li>"
             "<li><b>Lectura.</b> Con d = δ/σ se lee n en la curva OC de la prueba t de una muestra (Montgomery, apéndice V), "
             "o se calcula en Minitab (Potencia y tamaño de la muestra › t de 1 muestra). Ese n es el número de réplicas "
             "por corriente del experimento real. Con el cronometraje del piloto se sabe cuántas trazas caben en un día: "
             "si las 3n trazas caben en tres días, el plan es de tres días; si no, se usa también el jueves 29; si aun así "
             "no alcanza, se toman las que caben y se informa la potencia que se logró.</li></ol>")
    o.append("<h4>Regla para fijar δ con los datos del fabricante (se usa el primero que exista)</h4>")
    o.append(tabla([
        ["1", "Tolerancia del valor medido, τ<sub>0</sub> ± t", "δ = t", "Ejemplo: 83 ± 5 fs → δ = 5 fs."],
        ["2", "Valor medido τ<sub>0</sub> y máximo garantizado τ<sub>máx</sub>", "δ = τ<sub>máx</sub> − τ<sub>0</sub>", "Es cuánto puede crecer el pulso antes de salir de especificación. Ejemplo: 83 fs medidos y 90 fs máximo → δ = 7 fs."],
        ["3", "Banda de aceptación de la prueba final", "δ = semiancho de la banda", "Es la δ con la que el fabricante dio por bueno el equipo."],
        ["4", "Estabilidad del ancho declarada, e (% rms)", "δ = 3 · e · τ<sub>0</sub>", "δ debe ser claramente mayor que la variación normal."],
        ["5", "Ninguno de los anteriores", "δ = 10 fs", "Ver justificación abajo."],
    ], cab=["Orden", "Dato disponible", "δ", "Lectura"], izq=(1, 2, 3)))
    o.append("<p>Si el fabricante declara la incertidumbre u de su medición, δ no puede ser menor que 2u: no tiene sentido "
             "buscar diferencias más finas que las que el propio patrón puede ver. Si la regla da valores distintos por "
             "corriente, cada corriente usa el suyo y n se lee con el menor.</p>")
    o.append("<p><b>Por qué 10 fs si no hay datos del fabricante.</b> (1) Es el tamaño del error del propio método: suponer "
             "forma gaussiana en vez de sech² mueve el ancho de 90 a 98 fs. Una diferencia menor que eso no se podría "
             "atribuir al láser. (2) Un pulso 11 % más largo tiene 11 % menos potencia pico, que es lo que importa en los "
             "usos del láser. (3) Es alcanzable: con σ entre 5 y 8 fs bastan 4 a 8 réplicas por corriente; detectar 5 fs "
             "exigiría entre 11 y 24.</p>")
    o.append('<div class="nota"><b>Dos preguntas distintas con la misma curva.</b> La curva OC relaciona α, la potencia, n y '
             'd = δ/σ. Si se fijan δ, σ y los riesgos, la curva da el n necesario: es la pregunta de diseño. Si en cambio se '
             'fija el n que cabe en el plazo, la curva da la menor diferencia que el experimento puede detectar, '
             'δ<sub>det</sub>: es una propiedad del plan. El diseño está bien cuando δ<sub>det</sub> es menor o igual que la δ que '
             'importa. El sábado por la noche se calculan las dos. Si δ<sub>det</sub> sale, por ejemplo, 6 fs, el plan sobra; '
             'si sale 14 fs, se sabe desde antes que una desviación de 10 fs podría no verse, y se declara en el informe.</div>')
    o.append(tabla([
        ["S del piloto en I<sub>1</sub> / I<sub>2</sub> / I<sub>3</sub> (fs)", ""], ["S mayor (fs)", ""], ["σ = 1,56 · S mayor (fs)", ""],
        ["δ (fs) y dato del fabricante que la fijó", ""], ["d = δ/σ", ""], ["n leído (α = 0,05, potencia 0,90)", ""],
        ["Duración de una réplica con cambio de corriente (min)", ""], ["Trazas que caben en un día", ""],
        ["Días de medición (3 o 4)", ""], ["Réplicas por corriente y por día (n / días)", ""],
        ["Si n no cabe: n que sí cabe y su δ<sub>det</sub> (fs)", ""], ["¿δ<sub>det</sub> ≤ δ?", ""],
    ], cab=["Cálculo del sábado por la noche", "Valor"], izq=(0, 1), cls="hoja"))
    o.append("<h4>Réplicas por día (se llena el sábado por la noche)</h4>")
    o.append(tabla([
        ["Corriente I<sub>1</sub> (referencia τ<sub>0,1</sub>)", "", ""],
        ["Corriente I<sub>2</sub> (referencia τ<sub>0,2</sub>)", "", ""],
        ["Corriente I<sub>3</sub> (referencia τ<sub>0,3</sub>)", "", ""],
        ["Total de trazas", "", ""],
    ], cab=["Corriente", "Por día", "Total (n)"], izq=(0,), cls="hoja"))

    o.append("<h3>Orden de medición dentro del día</h3>")
    o.append("<ul><li>Se arma la lista del día con el mismo número de réplicas de cada corriente y se sortea completa antes de "
             "empezar (Minitab: Calc › Datos aleatorios › Muestra de columnas). El orden se anota en la hoja de registro y no "
             "se cambia.</li>"
             "<li><b>No se hace</b> lo más cómodo: medir todas las de una corriente seguidas y luego cambiar. Si el láser deriva "
             "durante la tarde, esa deriva se confundiría con el efecto de la corriente.</li>"
             "<li>Si en el piloto el cambio de corriente resulta muy lento, se admite tomar dos réplicas seguidas por "
             "corriente en cada turno, con los turnos sorteados. Cada corriente sigue apareciendo varias veces repartida en el "
             "día.</li>"
             "<li>Si una corriente no da pulsos estables ese día, se anota la causa y sus réplicas se reponen el jueves.</li></ul>")
    o.append("<p>Si la hoja de pruebas lista más de tres corrientes, se eligen tres repartidas en el rango y se dice cuáles. "
             "Si el sábado aún no hubiera aparecido, se usan la corriente de operación habitual y dos más que den pulsos "
             "estables, anotadas con precisión para emparejarlas después con la hoja.</p>")

    # ---------------------------------------------------------------- 5. ejecución
    o.append(seccion("5", "¿Cómo se mide?", "Procedimiento de cada día y de cada réplica"))
    o.append("<h3>Lo que se mantiene fijo</h3>")
    o.append(tabla([
        ["Forma de pulso y factor", "Los del fabricante: sech² y 0,65", "Cambiar la forma cambia el ancho hasta un 9 %"],
        ["Calentamiento", "Encender el láser 30 min antes de la primera réplica", "El ancho cambia mientras el láser se estabiliza"],
        ["Temperatura y humedad", "<b>No se miden</b>: no hay medidores. Se mantiene el cuarto en las mismas condiciones y se anota la hora de cada réplica. Se declara como limitación", "El ancho varía con la temperatura"],
        ["Barrido", "Mismo recorrido (al menos ±500 fs), mismo paso (5 fs o menos), mismo tiempo de integración", "Un barrido distinto cambia el ajuste"],
        ["Análisis de la traza", "El mismo programa para todas: restar fondo, ajustar sech², leer el ancho, multiplicar por 0,65", "El análisis también es una fuente de variación"],
    ], cab=["Qué", "Cómo", "Por qué"], izq=(0, 1, 2)))
    o.append("<h3>Antes del piloto</h3>")
    o.append('<ol class="pasos">'
             "<li>Dejar fijo el programa de análisis y probarlo con una traza simulada de ancho conocido.</li>"
             "<li>Sortear el orden de las trazas de cada día y escribirlo en las hojas de registro.</li></ol>")
    o.append("<h3>Cada día</h3>")
    o.append('<ol class="pasos">'
             "<li>Anotar fecha, hora de inicio, quién mide y cualquier cambio en el cuarto.</li>"
             "<li>Encender el láser y esperar 30 min. Medir la potencia en cada corriente y anotarla.</li>"
             "<li>Medir las réplicas del día en el orden sorteado. Al cambiar de corriente, esperar 5 min y volver a medir la potencia.</li>"
             "<li>Al terminar, medir la potencia otra vez y anotar la hora. Guardar todos los archivos con nombre único.</li></ol>")
    o.append("<h3>Cada réplica</h3>")
    o.append('<ol class="pasos">'
             "<li>Bloquear el haz unos segundos y desbloquearlo.</li>"
             "<li>Mover el motor a una posición inicial distinta de la réplica anterior.</li>"
             "<li>Tomar la traza con los parámetros fijos y guardar el archivo crudo. No descartar ninguna traza en el momento.</li>"
             "<li>Analizar con el programa fijo y anotar el ancho de la traza y τ<sub>p</sub>.</li>"
             "<li>Si hay espectrómetro, tomar el espectro y anotar λ<sub>c</sub> y Δλ.</li></ol>")
    o.append("<h3>Hoja de registro (una fila por réplica)</h3>")
    o.append(hoja(["Día", "Orden", "Corriente (A)", "P (mW)", "Hora", "Ancho traza (fs)",
                   "τ<sub>p</sub> (fs)", "Δλ (nm)", "Archivo", "Observaciones"], 6, izq=()))
    o.append("<h3>Cuándo se descarta una traza</h3>")
    o.append("<ul><li>Solo por una causa anotada en el momento: el láser perdió los pulsos, la potencia salió del rango, o el "
             "barrido se interrumpió. La traza se guarda igual.</li>"
             "<li>Nunca por dar un valor inesperado. Si un dato parece atípico, se reporta el resultado con él y sin él.</li>"
             "<li>Toda traza descartada se repone con una nueva.</li></ul>")

    # ---------------------------------------------------------------- 6. análisis
    o.append(seccion("6", "¿Cómo se analizan los datos?", "Pasos del análisis; la prueba de hipótesis se aplica cuando haya valores de referencia"))
    o.append('<ol class="pasos">'
             "<li><b>Gráficas.</b> Diagrama de puntos de τ<sub>p</sub> por corriente con el valor del fabricante marcado; "
             "diagrama de caja por día y por corriente; τ<sub>p</sub> contra el orden de medición.</li>"
             "<li><b>Independencia.</b> La protege el orden sorteado. Se revisa que τ<sub>p</sub> contra el orden no muestre tendencia.</li>"
             "<li><b>Normalidad.</b> Gráfica de probabilidad normal y prueba de Anderson-Darling por corriente; se acepta si P &gt; 0,05.</li>"
             "<li><b>Efecto del día.</b> Se comparan las medias por día. Si difieren mucho, se reporta y se considera el análisis por bloques.</li>"
             "<li><b>Prueba t de una muestra</b> por corriente, con la hipótesis de la sección 3. Se reporta la salida completa "
             "de Minitab: n, media, S, error estándar, t, valor P e intervalo de confianza.</li>"
             "<li><b>Potencia lograda</b> para la δ fijada, con el n real y la S observada.</li>"
             "<li><b>Conclusión</b> en cada corriente: si el ancho de hoy es igual al del fabricante o se aleja de él, y cuánto "
             "(intervalo de confianza).</li></ol>")
    o.append(ruta("Gráfica", "Gráfica de probabilidad", "Simple") + ruta("Estadísticas", "Estadísticas básicas", "Prueba de normalidad") +
             ruta("Estadísticas", "Estadísticas básicas", "t de 1 muestra"))

    # ---------------------------------------------------------------- 7. cronograma
    o.append(seccion("7", "¿Por qué ahora y cuál es el calendario?", "El láser será retirado del laboratorio"))
    o.append("<p>El láser va a ser retirado y no habrá otra oportunidad de medir. Por eso toda la parte experimental se "
             "concentra en una semana: piloto el sábado y tres días seguidos de medición. Hay que dejar días libres antes "
             "de la recogida para desmontar el montaje óptico. Con los datos tomados, la exposición y el informe del 12 de "
             "diciembre se preparan sin el láser.</p>")
    o.append(tabla([
        ["Sáb 24 oct", "Asesoría. Luego, en el laboratorio, <b>piloto</b>: 5 réplicas por corriente (15 trazas en total) en orden sorteado, cronometradas. Por la noche: S por "
                       "corriente, n en la curva OC, decisión de 3 o 4 días, sorteo del orden de cada día."],
        ["Dom 25 oct", "Buscar la hoja de pruebas y el manual (sección 2). Preparar las hojas de registro."],
        ["Lun 26 oct", "<b>Día 1</b>: las réplicas del día (n/3 por corriente), en orden sorteado."],
        ["Mar 27 oct", "<b>Día 2</b>: ídem. Revisión rápida de los datos de los días 1 y 2."],
        ["Mié 28 oct", "<b>Día 3</b>: ídem. Se completan las n réplicas por corriente. (Ese día se envía también el paper del caso del tema 6.)"],
        ["Jue 29 oct", "<b>Reserva</b>: solo si la curva OC pidió más réplicas o hay trazas por reponer. Copia de seguridad de todos los archivos en dos sitios."],
        ["Vie 30 oct en adelante", "Desmontaje del montaje óptico."],
        ["Noviembre", "Hipótesis con la hoja de pruebas, análisis completo, borrador del informe."],
        ["Sáb 12 dic", "Exposición e informe final del trabajo práctico."],
    ], cab=["Fecha", "Actividad"], izq=(0, 1)))
    o.append('<div class="nota"><b>Si hay menos tiempo.</b> Con dos días se reparte n entre dos; si no cabe, se toman las '
             'que caben, se mantienen las tres corrientes y se informa la potencia lograda. Si el piloto del sábado no se puede hacer, las primeras 5 '
             'trazas del lunes cumplen su papel y se excluyen del análisis.</div>')

    # ---------------------------------------------------------------- 8. aprobación
    o.append(seccion("8", "¿Qué se pide aprobar hoy?", "Lista para la asesoría"))
    o.append(tabla([
        ["1", "Valor de referencia: el ancho medido por el fabricante en este láser a cada corriente (hoja de pruebas), y no el máximo del modelo.", ""],
        ["2", "Escribir las hipótesis cuando se tengan esos valores, sobre datos ya tomados.", ""],
        ["3", "Definición de réplica y de unidad experimental (sección 4).", ""],
        ["4", "Piloto el sábado 24: solo 5 réplicas por corriente (15 trazas en total), en orden sorteado, para estimar el número de réplicas del experimento real. No entran al análisis.", ""],
        ["5", "Número de réplicas leído en la curva OC con σ = 1,56 · S del piloto, δ por la regla de la sección 4, α = 0,05 y potencia 0,90.", ""],
        ["6", "Tres días de medición con el n calculado el sábado, repartido por igual entre corrientes y días; orden sorteado cada día; el día no es un factor.", ""],
        ["7", "Medir las tres corrientes aunque la hoja de pruebas no haya aparecido.", ""],
        ["8", "Sin medición de temperatura ni humedad; se declara como limitación.", ""],
        ["9", "Procedimiento de medición, hoja de registro y reglas para descartar trazas (sección 5).", ""],
        ["10", "Verificación de supuestos con gráfica de probabilidad normal y Anderson-Darling; reporte literal de Minitab.", ""],
    ], cab=["#", "Decisión", "Aprobado / observación"], izq=(1, 2), cls="hoja"))

    # ---------------------------------------------------------------- anexo A: ecuaciones
    o.append(seccion("A", "Fórmulas que usa el diseño", "Solo las del caso del experimento: una media frente a un valor conocido, varianza desconocida"))

    def eq(latex, ref=""):
        r = f'<p class="ref">{ref}</p>' if ref else ""
        return f'<div class="eq"><p>$${latex}$$</p>{r}</div>'

    o.append("<h3>A.1 De la traza al dato</h3>")
    o.append("<p>El autocorrelador entrega una traza. Su ancho a media altura, $\\mathrm{FWHM}_{AC}$, se multiplica por el "
             "factor de la forma supuesta para obtener el ancho del pulso:</p>")
    o.append(eq(r"\tau_p = 0{,}65 \cdot \mathrm{FWHM}_{AC} \quad \text{(forma sech}^2\text{, la del fabricante)}",
                "Diels y Rudolph (2006), cap. 9; nota 2 de las hojas de datos de Calmar"))
    o.append("<p>El eje de tiempo de la traza sale del desplazamiento $\\Delta x$ del espejo móvil (el haz va y vuelve):</p>")
    o.append(eq(r"\tau = \frac{2\,\Delta x}{c}, \qquad 1\ \mu\text{m} = 6{,}67\ \text{fs}"))

    o.append("<h3>A.2 Media, desviación estándar y error estándar de cada corriente</h3>")
    o.append(eq(r"\bar y = \frac{1}{n}\sum_{i=1}^{n} y_i, \qquad S^2 = \frac{\sum_{i=1}^{n}(y_i - \bar y)^2}{n-1}, \qquad \mathrm{EE}(\bar y) = \frac{S}{\sqrt n}",
                "Montgomery, ecs. 2-7 y 2-8"))

    o.append("<h3>A.3 Estadístico de prueba</h3>")
    o.append("<p>Con las $n$ réplicas de una corriente y el valor $\\tau_0$ del fabricante a esa corriente:</p>")
    o.append(eq(r"t_0 = \frac{\bar y - \tau_0}{S/\sqrt n}, \qquad t_0 \sim t_{n-1} \ \text{si } H_0 \text{ es cierta}",
                "Montgomery, ec. 2-37; Gutiérrez–De la Vara, ec. (2.8)"))
    o.append(eq(r"\text{Dos colas: rechazar } H_0 \text{ si } |t_0| > t_{\alpha/2,\,n-1}. \qquad \text{Una cola: rechazar si } t_0 > t_{\alpha,\,n-1}",
                "Montgomery, tabla 2-4"))
    o.append(eq(r"\text{valor } P = 2\,P(t_{n-1} > |t_0|) \ \text{(dos colas)}, \qquad P = P(t_{n-1} > t_0) \ \text{(una cola)}"))
    o.append("<p>Intervalo de confianza para la media del ancho a esa corriente:</p>")
    o.append(eq(r"\bar y - t_{\alpha/2,\,n-1}\frac{S}{\sqrt n} \;\le\; \mu \;\le\; \bar y + t_{\alpha/2,\,n-1}\frac{S}{\sqrt n}",
                "Montgomery, ec. 2-38"))

    o.append("<h3>A.4 Número de réplicas</h3>")
    o.append("<p>Entradas: la diferencia $\\delta$ que importa, la estimación $\\sigma_{\\text{prev}}$ y los riesgos "
             "$\\alpha$ y $\\beta$. Tres formas de obtener $n$, equivalentes:</p>")
    o.append("<p><b>(a) Curva OC de Montgomery</b> (sec. 2-4.2, apéndice V). Es la que usa este protocolo. Se entra con $d$ y "
             "se lee $n$ en la curva de la potencia deseada:</p>")
    o.append(eq(r"d = \frac{\delta}{\sigma_{\text{prev}}}, \qquad \sigma_{\text{prev}} = 1{,}56 \cdot S_{\text{piloto}}"))
    o.append("<p><b>(b) Aproximación con la normal</b>, para tantear:</p>")
    o.append(eq(r"n \approx \left(\frac{(z_{\alpha} + z_{\beta})\,\sigma}{\delta}\right)^2 \ \text{(una cola)}, \qquad n \approx \left(\frac{(z_{\alpha/2} + z_{\beta})\,\sigma}{\delta}\right)^2 \ \text{(dos colas)}"))
    o.append("<p>Con $\\alpha = 0{,}05$ y potencia $0{,}90$: $z_{0{,}05} = 1{,}645$, $z_{0{,}025} = 1{,}960$, $z_{0{,}10} = 1{,}282$. "
             "Ejemplo a una cola con $\\delta = 10$ fs y $\\sigma = 8$ fs: $n \\approx [(1{,}645 + 1{,}282)\\cdot 8/10]^2 \\approx 6$. "
             "La versión exacta da 8, porque con pocos datos la t exige más que la normal.</p>")
    o.append("<p><b>(c) Exacta</b>, con la distribución t no central. Es lo que calcula Minitab. Se busca el menor $n$ tal que</p>")
    o.append(eq(r"1 - \beta = P\!\left(t'_{n-1}(\lambda) > t_{\alpha,\,n-1}\right) \ge 0{,}90, \qquad \lambda = \frac{\delta\sqrt n}{\sigma}",
                "para dos colas se usa t_{α/2, n−1}"))
    o.append("<p><b>Potencia lograda</b>: la misma ecuación (c), resuelta para $1 - \\beta$ con el $n$ real y la $S$ observada.</p>")

    o.append("<h3>A.5 Tabla de apoyo para la decisión del sábado</h3>")
    o.append("<p>Menor diferencia $\\delta$ (fs) que detecta la prueba con $\\alpha = 0{,}05$ y potencia $0{,}90$, para "
             "varios valores de la desviación estándar y del número de réplicas por corriente. Sirve para leer "
             "$\\delta_{\\text{det}}$ con el $n$ que resulte o con el que quepa en los días disponibles.</p>")
    sig = (3, 5, 8, 12)
    ns = (6, 8, 10, 12, 15, 20)
    filas = []
    for sg in sig:
        filas.append([f"{sg} fs"] + [f"{delta_detectable_1m(sg, k):.1f}" for k in ns] + [f"{delta_detectable_1m(sg, k, dos_colas=True):.1f}" for k in ns])
    o.append(tabla(filas, cab=["σ"] + [f"1 cola, n = {k}" for k in ns] + [f"2 colas, n = {k}" for k in ns], hl=(2,)))
    o.append("<p>Al revés, para detectar 10 fs a una cola hacen falta "
             + ", ".join(f"{n_minimo_1m(10, sg)} réplicas con σ = {sg} fs" for sg in sig) + ".</p>")

    # ---------------------------------------------------------------- referencias
    o.append(seccion("R", "Referencias", "Normas ICONTEC"))
    refs = [
        "MONTGOMERY, Douglas C. <i>Diseño y análisis de experimentos</i>. 2 ed. México: Limusa Wiley, 2004. Capítulo 2, "
        "Experimentos comparativos simples, p. 21–59.",
        "GUTIÉRREZ PULIDO, Humberto y DE LA VARA SALAZAR, Román. <i>Análisis y diseño de experimentos</i>. 2 ed. México: "
        "McGraw-Hill, 2008. Capítulo 2, p. 18–59.",
        "CALMAR LASER. <i>Carmel X-780: 780 nm High Power Fiber Based Femtosecond Laser</i>. Hoja de datos, Rev. E, "
        "1 oct. 2025. 4 p. Disponible en: calmarlaser.com/docs/datasheets/high_power/Carmel.780.pdf",
        "CALMAR LASER. <i>Carmel: Fiber Based Femtosecond Laser, CFL-04RFF / 05RFF / 10RFF</i>. Hoja de datos, Rev. H, "
        "21 jun. 2016 y Rev. I, 3 ene. 2017. 4 p. Copias en web.archive.org.",
        "CALMAR LASER. <i>Carmel CFL-05RFF0: High Power 780 nm Fiber Based Femtosecond Laser</i>. Hoja de datos, Rev. C, "
        "4 dic. 2012. 2 p. Copia en web.archive.org.",
        "CALMAR LASER. <i>Calmar Laser Catalog 2023</i>. Palo Alto (CA), 2023. 71 p. Carmel X-780, p. 8–10.",
        "DIELS, Jean-Claude y RUDOLPH, Wolfgang. <i>Ultrashort Laser Pulse Phenomena</i>. 2 ed. Burlington: Academic "
        "Press, 2006. Capítulo 9, Diagnostic techniques, p. 457–489.",
        "SALA, K. L.; KENNEY-WALLACE, G. A. y HALL, G. E. CW autocorrelation measurements of picosecond laser pulses. En: "
        "<i>IEEE Journal of Quantum Electronics</i>. 1980, vol. 16, no. 9, p. 990–996.",
    ]
    o.append("".join(f'<p class="ref">{r}</p>' for r in refs))
    o.append(KATEX_RUN)
    o.append("</body></html>")
    open(out, "w", encoding="utf-8").write("".join(o))
    print("protocolo:", out)


if __name__ == "__main__":
    build(sys.argv[1])
