"""Contenido de la exposición de diseños factoriales 3^k, confusión, fracciones 3^{k−p} y niveles mixtos
(Montgomery, cap. 9). Mismos bloques y renderizadores que la exposición de fraccionados 2^{k−p}:
    CONTENIDO=contenido_3k python render_pptx.py salida.pptx   (o ./build.sh 3k)
"""
import os

from bloques import *  # noqa: F401,F403
from doe import basic, effect, f_ppf
from doe3 import (Datos, LIN, QUAD, aliases, basic_design, betas_from_word, blocks, defining, dig,
                  fit_quad, fraction, gen_ints, parse, runs3, word)
import figuras_3k

META = {"titulo": "Diseños factoriales 3^{k} y con niveles mixtos",
        "titulo_html": "Diseños factoriales 3<sup>k</sup> y con niveles mixtos",
        "pie": "Diseños 3^{k} y niveles mixtos",
        "previo": "", "previo_titulo": "", "previo_sub": "", "previo_indice": ""}

FIG = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "exposicion-tema-06", "figuras-3k")


def W(e):
    """Nombre de un componente (vector de exponentes) con superíndices para las diapositivas."""
    return word(e)


# ================================================================ datos y cálculos
# Ejemplo 1: problema 9-6, rendimiento de un proceso químico, 3^2 con n = 2
# A = temperatura (80, 90, 100 °C), B = presión (100, 120, 140 psig)
y96 = {(0, 0): [47.58, 48.77], (0, 1): [64.97, 69.22], (0, 2): [80.92, 72.60],
       (1, 0): [51.86, 82.43], (1, 1): [88.47, 84.23], (1, 2): [93.95, 88.54],
       (2, 0): [71.18, 92.77], (2, 1): [96.57, 88.72], (2, 2): [76.58, 83.04]}
d1 = Datos(2, y96)
an1, sse1, dfe1, mse1 = d1.anova([("A", (0,)), ("B", (1,)), ("AB", (0, 1))])
lq1 = {"A_{L}": d1.ss_contrast({0: LIN}), "A_{Q}": d1.ss_contrast({0: QUAD}),
       "B_{L}": d1.ss_contrast({1: LIN}), "B_{Q}": d1.ss_contrast({1: QUAD}),
       "AB_{L×L}": d1.ss_contrast({0: LIN, 1: LIN}), "AB_{L×Q}": d1.ss_contrast({0: LIN, 1: QUAD}),
       "AB_{Q×L}": d1.ss_contrast({0: QUAD, 1: LIN}), "AB_{Q×Q}": d1.ss_contrast({0: QUAD, 1: QUAD})}
cAB1, tAB1 = d1.ss_component((1, 1))
cAB21, tAB21 = d1.ss_component((1, 2))
_xs, _ys = [], []
for r, v in y96.items():
    for yy in v:
        _xs.append((r[0] - 1, r[1] - 1)); _ys.append(yy)
b1, _, _ = fit_quad(_xs, _ys)
med1 = {r: sum(v) / 2 for r, v in y96.items()}
# punto estacionario: ∂ŷ/∂x = 0 → sistema 2 × 2
_det = 4 * b1[3] * b1[4] - b1[5] ** 2
xs1 = (-2 * b1[4] * b1[1] + b1[5] * b1[2]) / _det
xs2 = (-2 * b1[3] * b1[2] + b1[5] * b1[1]) / _det
ys1 = b1[0] + b1[1] * xs1 + b1[2] * xs2 + b1[3] * xs1 ** 2 + b1[4] * xs2 ** 2 + b1[5] * xs1 * xs2

# Ejemplo 2: ejemplo 9-1, pérdida de jarabe, 3^3 con n = 2
# A = boquilla (1, 2, 3), B = velocidad (100, 120, 140 rpm), C = presión (10, 15, 20 psi); y = cm³ − 70
_raw = {0: {0: [(-35, -25), (-45, -60), (-40, 15)], 1: [(17, 24), (-65, -58), (20, 4)], 2: [(-39, -35), (-55, -67), (15, -30)]},
        1: {0: [(110, 75), (-10, 30), (80, 54)], 1: [(55, 120), (-55, -44), (110, 44)], 2: [(90, 113), (-28, -26), (110, 135)]},
        2: {0: [(4, 5), (-40, -30), (31, 36)], 1: [(-23, -5), (-64, -62), (-20, -31)], 2: [(-30, -55), (-61, -52), (54, 4)]}}
y91 = {}
for _c, _da in _raw.items():
    for _a, _lst in _da.items():
        for _b, _par in enumerate(_lst):
            y91[(_a, _b, _c)] = list(_par)
d2 = Datos(3, y91)
T2 = [("A", (0,)), ("B", (1,)), ("C", (2,)), ("AB", (0, 1)), ("AC", (0, 2)), ("BC", (1, 2)), ("ABC", (0, 1, 2))]
an2, sse2, dfe2, mse2 = d2.anova(T2)
wxyz = {n: d2.ss_component(e) for n, e in (("W = AB^{2}C^{2}", (1, 2, 2)), ("X = AB^{2}C", (1, 2, 1)),
                                            ("Y = ABC^{2}", (1, 1, 2)), ("Z = ABC", (1, 1, 1)))}
tot2 = {}
for r, v in y91.items():
    tot2[r] = sum(v)
cel = lambda i, j, a, b: sum(t for r, t in tot2.items() if r[i] == a and r[j] == b)      # totales de celda
mod2 = {}
for _a in range(3):
    _xs, _ys = [], []
    for r, v in y91.items():
        if r[0] == _a:
            for yy in v:
                _xs.append((r[1] - 1, r[2] - 1)); _ys.append(yy)
    mod2[_a] = fit_quad(_xs, _ys)[0]
libro2 = {0: (22.1, 3.5, 16.3, 51.7, -71.8, 2.9), 1: (25.6, -22.8, -12.3, 14.1, -56.9, -0.7),
          2: (15.1, 20.3, 5.9, 75.8, -94.9, 10.5)}

# Ejemplo 3: ejemplo 9-2, 3^2 en tres bloques con AB^2 confundida (una réplica)
y92 = {(0, 0): 4, (1, 1): -4, (2, 2): 0, (1, 0): -2, (2, 1): 1, (0, 2): 8, (0, 1): 5, (1, 2): -5, (2, 0): 0}
d3 = Datos(2, {r: [v] for r, v in y92.items()})
bl3 = blocks(2, [(1, 2)])

# Ejemplos 4 y 5: problema 9-3 (réplica I), tiempo de acomodo de botellas, 3^3
# A = tipo de botella (plástico, vidrio 28 mm, vidrio 38 mm), B = aparador (permanente, final del
# pasillo, refrigerador), C = empleado (1, 2, 3). Respuesta: minutos para acomodar diez cajas.
_R1 = {0: [[3.45, 4.14, 5.80], [4.07, 4.38, 5.48], [4.20, 4.26, 5.67]],
       1: [[4.80, 5.22, 6.21], [4.52, 5.15, 6.25], [4.96, 5.17, 6.03]],
       2: [[4.08, 3.94, 5.14], [4.30, 4.53, 4.99], [4.17, 4.86, 4.85]]}
y93 = {(a, b, c): [_R1[c][a][b]] for c in range(3) for a in range(3) for b in range(3)}
d4 = Datos(3, y93)
ssABC4 = d4.ss_effect((0, 1, 2))
an4f, _, _, _ = d4.anova(T2[:6], error=(ssABC4, 8))               # réplica completa, error = ABC
bl4 = blocks(3, [(1, 2, 1)])
ssbl4, tbl4 = d4.ss_component((1, 2, 1))
an4, sse4, dfe4, mse4 = d4.anova(T2[:6], error=(ssABC4 - ssbl4, 6))
I5 = (1, 1, 1)
fr5 = fraction(3, [I5])
d5 = Datos(3, {r: y93[r] for r in fr5})
comp5 = [("A", (1, 0, 0)), ("B", (0, 1, 0)), ("C", (0, 0, 1)), ("AB^{2}", (1, 2, 0))]
ss5 = {n: d5.ss_component(e)[0] for n, e in comp5}
al5 = {n: aliases(e, [I5])[0] for n, e in comp5}
med5 = {}
for i, n in enumerate("ABC"):
    med5[n] = ([sum(d5.obs[r][0] for r in fr5 if r[i] == l) / 3 for l in range(3)],
               [sum(y93[r][0] for r in y93 if r[i] == l) / 9 for l in range(3)])

# Ejemplo 6: didáctico, un factor de dos niveles (A) y uno de tres (X) en un 2^3 de ocho corridas
r6 = basic(3)
y6 = [10, 14, 15, 19, 16, 18, 17, 23]
ef6 = {t: effect(r6, y6, t) for t in ["A", "B", "C", "AB", "AC", "BC", "ABC"]}
X6 = [0, 0, 1, 1, 1, 1, 2, 2]
_obs6 = {}
for r, yy, xl in zip(r6, y6, X6):
    _obs6.setdefault((0 if r["A"] < 0 else 1, xl), []).append(yy)
d6 = Datos(2, _obs6)
ssA6, ssX6 = d6.ss_effect((0,)), d6.ss_effect((1,))
ssAX6 = d6.ss_effect((0, 1))
sse6, dfe6 = d6.sse(), d6.dfe()

# Figuras
FIGS = figuras_3k.generar(FIG, {
    "ej1": (b1, "Temperatura (°C)", "Presión (psig)", ["80", "90", "100"], ["100", "120", "140"],
            "Rendimiento estimado · modelo cuadrático", [50, 60, 70, 80, 85, 90], (xs1, xs2)),
    "boq1": (mod2[0], "Velocidad (rpm)", "Presión (psi)", ["100", "120", "140"], ["10", "15", "20"],
             "Boquilla 1 · pérdida (cm³ − 70)", [-60, -40, -20, 0, 20, 40, 60], None),
    "boq2": (mod2[1], "Velocidad (rpm)", "Presión (psi)", ["100", "120", "140"], ["10", "15", "20"],
             "Boquilla 2", [-60, -40, -20, 0, 20, 40, 60], None),
    "boq3": (mod2[2], "Velocidad (rpm)", "Presión (psi)", ["100", "120", "140"], ["10", "15", "20"],
             "Boquilla 3", [-60, -40, -20, 0, 20, 40, 60, 80], None)})


def anova_rows(an, sse, dfe, mse, total, dft, dec=2):
    rows = [[t, f(ss, dec), str(df), f(ms, dec), f(F), pv(p)] for t, ss, df, ms, F, p in an]
    rows.append(["Error", f(sse, dec), str(dfe), f(mse, dec), "", ""])
    rows.append(["Total", f(total, dec), str(dft), "", "", ""])
    return rows


def modelo(b, x1="x_{1}", x2="x_{2}", dec=2):
    s = f"ŷ = {f(b[0], dec)}"
    for c, t in zip(b[1:], (x1, x2, x1 + "^{2}", x2 + "^{2}", x1 + x2)):
        s += (" + " if c >= 0 else " − ") + f(abs(c), dec) + " " + t
    return s


# ================================================================ diapositivas
SLIDES.append({"kind": "title", "title": "Diseños factoriales 3^{k} y con niveles mixtos",
               "sub": "Tema 6 (segunda parte) · Diseño de Experimentos Avanzados (3008475)",
               "meta": "Juan Esteban Rodríguez Ochoa · Sebastián Zapata Henao\n"
                       "Universidad Nacional de Colombia · 31 de octubre de 2026",
               "sec": "", "explica": ""})

S("Ruta de la clase",
  """La clase sigue el orden del capítulo 9 de Montgomery. Primero el propósito del diseño 3^{k}, su notación y sus grados de libertad. Después los componentes de interacción, que son la idea que organiza todo lo demás: con ellos se construyen los bloques y las fracciones. Luego el análisis completo de los diseños 3^{2} y 3^{3} con dos ejemplos del libro. Siguen la confusión en tres bloques y en nueve o más bloques, la fracción un tercio y la fracción general 3^{k−p}, y por último los diseños con niveles mixtos, que son la recomendación práctica del libro cuando hace falta un factor con tres o cuatro niveles. Cierra con las ideas clave.""",
  body=[cards(("1 · Propósito y vocabulario", "Para qué un tercer nivel, notación 0-1-2 y grados de libertad"),
              ("2 · Componentes de interacción", "AB, AB^{2}, W, X, Y, Z: la herramienta de construcción"),
              ("3 · Los diseños 3^{2} y 3^{3}", "Análisis completo con dos ejemplos del libro"),
              ("4 · Confusión en tres bloques", "Definición de contrastes L mod 3 y dos ejemplos"),
              ("5 · Nueve y 3^{p} bloques", "Interacciones generalizadas PQ y PQ^{2}"),
              ("6 · Fracción un tercio 3^{k−1}", "Relación de definición, alias por I e I^{2}, un ejemplo"),
              ("7 · Fracción general 3^{k−p}", "Construcción, alias y el juicio del libro"),
              ("8 · Niveles mixtos", "Factores de tres y cuatro niveles dentro de un 2^{k}"),
              ("9 · Cierre", "Ideas clave y errores frecuentes"), size=15, cols=5)])

# ---------------------------------------------------------------- 1
section(1, "Propósito y vocabulario", "Para qué sirve un tercer nivel, notación 0-1-2 y grados de libertad")

S("¿Para qué sirve un tercer nivel?",
  """Con dos niveles por factor solo se puede estimar una recta entre el nivel bajo y el alto. Si la respuesta tiene curvatura, por ejemplo un máximo en un valor intermedio, dos niveles no la detectan. El diseño 3^{k} agrega el nivel intermedio y permite ajustar un modelo cuadrático: para dos factores, y = β_{0} + β_{1}x_{1} + β_{2}x_{2} + β_{12}x_{1}x_{2} + β_{11}x_{1}^{2} + β_{22}x_{2}^{2} + ε (ecuación 9-1 del libro).

Hay otro uso, que el libro considera el más razonable: cuando un factor es cualitativo y tiene exactamente tres niveles de interés, como tres tipos de boquilla o tres proveedores. Ahí no hay curvatura que modelar: simplemente existen tres categorías y las tres importan.

Un diseño 3^{k} tiene k factores, cada uno con tres niveles, y 3^{k} combinaciones de tratamientos. El tema sigue el mismo esquema del 2^{k}: notación, análisis, confusión en bloques y fracciones; pero cada paso es más complicado, y por eso el libro termina recomendando usar tres niveles solo cuando hacen falta.""",
  left=[form("y = β_{0} + β_{1}x_{1} + β_{2}x_{2} + β_{12}x_{1}x_{2} + β_{11}x_{1}^{2} + β_{22}x_{2}^{2} + ε", size=17),
        bul("Dos niveles → una **recta**; tres niveles → una **parábola**: se puede modelar la **curvatura**",
            "Factores **cualitativos** con tres categorías de interés: boquillas, proveedores, materiales",
            "**k** factores × **3** niveles = **3^{k}** combinaciones de tratamientos", size=16)],
  right=[cards(("Cuándo sí", "Un factor **cualitativo** con tres niveles que interesan todos (ejemplo 9-1 del libro)"),
               ("Cuándo no", "Factores **cuantitativos** solo para ver curvatura: hay diseños más eficientes (siguiente diapositiva)"),
               size=15, cols=1)],
  ratio=0.55)

S("Dos advertencias del libro antes de usar un 3^{k}",
  """Montgomery advierte dos cosas antes de presentar el diseño. Primera: el 3^{k} no es la forma más eficiente de modelar una relación cuadrática. Los diseños de superficie de respuesta del capítulo 11 lo hacen con menos corridas.

Segunda: el 2^{k} con puntos centrales, visto en el capítulo 6, da una indicación de la curvatura con un diseño pequeño y simple, y además protege contra ella. Si la curvatura resulta importante, se agregan corridas axiales y se obtiene un diseño central compuesto. Esa estrategia secuencial es, por mucho, más eficiente que correr un 3^{k} con factores cuantitativos.

Dicho de otra forma: un 3^{3} cuesta 27 corridas por réplica; un 2^{3} con cuatro puntos centrales cuesta 12 y ya dice si hay curvatura. Solo si la hay se gastan las 6 corridas axiales, para un total de 18 corridas.""",
  left=[num("El 3^{k} **no es la forma más eficiente** de modelar una relación cuadrática: los diseños de **superficie de respuesta** (cap. 11) son mejores",
            "El **2^{k} con puntos centrales** (cap. 6) detecta la curvatura con pocas corridas; si aparece, se agregan **corridas axiales** → **diseño central compuesto**", size=16),
        note("Estrategia **secuencial**: 2^{k} + centro → ¿hay curvatura? → axiales. Mucho más eficiente que un 3^{k}", size=15)],
  right=[tab(["Diseño", "Corridas", "Detecta curvatura", "Modela curvatura"],
             [["2^{3}", "8", "No", "No"], ["2^{3} + 4 puntos centrales", "12", "Sí", "No"],
              ["Central compuesto (+ 6 axiales)", "18", "Sí", "Sí"], ["3^{3}", "27", "Sí", "Sí"]],
             size=15, colw=[0.42, 0.16, 0.21, 0.21])],
  ratio=0.5)

S("Notación: cada combinación es una cadena de dígitos 0, 1, 2",
  """Los tres niveles se llaman bajo, intermedio y alto y se representan con los dígitos 0, 1 y 2. Una combinación de tratamientos se escribe con k dígitos: el primero es el nivel de A, el segundo el de B, y así sucesivamente. En un 3^{2}, 00 es A y B bajos y 01 es A bajo con B intermedio. En un 3^{4}, 0120 significa A y D bajos, B intermedio y C alto.

Esta notación reemplaza a las letras minúsculas del 2^{k} ((1), a, b, ab), que ya no sirven con tres niveles. En el 2^{k} se prefirió ±1 porque facilita la vista geométrica, la regresión, los bloques y las fracciones; con tres niveles la aritmética de bloques y fracciones se hace módulo 3 y por eso conviene 0, 1, 2.

Cuando los factores son cuantitativos se usa −1, 0, +1 para ajustar el modelo de regresión. Las dos notaciones son equivalentes: 0 ↔ −1, 1 ↔ 0, 2 ↔ +1.""",
  left=[img(FIGS["grid"], h=3.9, caption="Las 9 combinaciones del 3^{2} (fig. 9-1)")],
  right=[tab(["Combinación", "Significado"],
             [["00", "A bajo, B bajo"], ["01", "A bajo, B intermedio"], ["21", "A alto, B intermedio"],
              ["0120 (en un 3^{4})", "A bajo, B intermedio, C alto, D bajo"]], size=15, colw=[0.35, 0.65]),
         tab(["Nivel", "Dígito", "Codificado (cuantitativo)"],
             [["Bajo", "0", "−1"], ["Intermedio", "1", "0"], ["Alto", "2", "+1"]], size=15, first_left=False),
         note("Bloques y fracciones usan la aritmética **módulo 3** sobre los dígitos", size=14)],
  ratio=0.42)

S("El 3^{3}: 27 combinaciones en un cubo",
  """Con tres factores hay 27 combinaciones, que se representan como puntos de un cubo con tres cortes por eje (figura 9-2 del libro). Cada vértice, arista, cara y el centro tienen su combinación: 000 es la esquina de todos bajos, 222 la de todos altos y 111 el centro.

Esta figura reaparece en bloques y fracciones: confundir un componente de ABC con tres bloques reparte los 27 puntos en tres grupos de 9, y una fracción un tercio se queda con uno de esos grupos.""",
  left=[img(FIGS["cubo"], h=4.6, caption="Las 27 combinaciones del 3^{3} (fig. 9-2)")],
  right=[bul("**000**: todos bajos · **222**: todos altos · **111**: el centro",
             "27 combinaciones = 3 × 3 × 3",
             "Tres bloques o una fracción un tercio = **grupos de 9 puntos** de este cubo", size=16)],
  ratio=0.55)

S("Grados de libertad: cada efecto principal tiene 2 y cada interacción de h factores tiene 2^{h}",
  """En un 3^{2} hay 9 combinaciones y 8 grados de libertad entre ellas: 2 para A, 2 para B y 4 para AB. Con n réplicas hay n·3^{2} − 1 grados de libertad totales y 3^{2}(n − 1) del error. En un 3^{3} hay 27 combinaciones y 26 grados de libertad: 2 por cada efecto principal, 4 por cada interacción de dos factores y 8 para ABC.

La regla general: un efecto principal tiene 3 − 1 = 2 grados de libertad, y una interacción de h factores tiene 2^{h}. Por eso en un 3^{k} con n réplicas hay n·3^{k} − 1 grados de libertad totales y 3^{k}(n − 1) del error.

Las sumas de cuadrados se calculan con los métodos usuales de los factoriales del capítulo 5. Lo nuevo del capítulo 9 es cómo se parten esos 2^{h} grados de libertad de las interacciones: en componentes lineales y cuadráticos cuando los factores son cuantitativos, o en componentes de 2 grados de libertad para construir bloques y fracciones.""",
  left=[tab(["Fuente", "3^{2}", "3^{3}", "3^{k}"],
            [["Efecto principal", "2", "2", "2"], ["Interacción de 2 factores", "4", "4", "4"],
             ["Interacción de 3 factores", "—", "8", "8"], ["Interacción de h factores", "—", "—", "2^{h}"],
             ["Error (n réplicas)", "9(n − 1)", "27(n − 1)", "3^{k}(n − 1)"], ["Total", "9n − 1", "27n − 1", "n·3^{k} − 1"]],
            size=15, colw=[0.4, 0.2, 0.2, 0.2])],
  right=[form("g.l. de una interacción de h factores = 2^{h}", size=18),
         bul("Las SS se calculan como en cualquier factorial (cap. 5)",
             "Lo nuevo: **cómo se parten** los 2^{h} g.l. de cada interacción", size=16)],
  ratio=0.55)

S("El tamaño crece muy rápido: 27, 81, 243 corridas",
  """Una réplica de un 3^{3} son 27 corridas; de un 3^{4}, 81; de un 3^{5}, 243. Por eso con frecuencia se corre una sola réplica y las interacciones de orden alto se combinan como estimación del error. Si las interacciones de tres o más factores son insignificantes, una réplica del 3^{3} deja 8 grados de libertad para el error (los de ABC) y una del 3^{4} deja 48 (los de las interacciones de tres y cuatro factores).

Aun así el libro es claro: estos diseños siguen siendo grandes para k ≥ 3 y, por consiguiente, son de escasa utilidad. Esa es la motivación de todo lo que sigue: bloques, para no correr 27 combinaciones en condiciones distintas, y fracciones, para no correr tantas.""",
  left=[tab(["Diseño", "Corridas por réplica", "g.l. de error con una réplica (interacciones de 3+ factores)"],
            [["3^{2}", "9", "0 (hace falta replicar)"], ["3^{3}", "27", "8 (ABC)"],
             ["3^{4}", "81", "48 (ABC, ABD, ACD, BCD, ABCD)"], ["3^{5}", "243", "192"]],
            size=15, colw=[0.15, 0.3, 0.55])],
  right=[note("«Siguen siendo diseños grandes para k ≥ 3 y, por consiguiente, de escasa utilidad» (Montgomery)", size=15),
         bul("Una réplica + interacciones de orden alto como error",
             "**Bloques**: para no correr las 27 en condiciones distintas",
             "**Fracciones**: para no correr tantas", size=16)],
  ratio=0.55)

# ---------------------------------------------------------------- 2
section(2, "Componentes de interacción", "La idea que organiza bloques y fracciones: AB, AB^{2}, W, X, Y, Z")

S("Dos formas de partir una interacción",
  """Una interacción AB de un 3^{2} tiene 4 grados de libertad. Hay dos maneras de partirla, y es importante no confundirlas.

Primera: componentes lineales y cuadráticos. Solo tiene sentido con factores cuantitativos. Cada efecto principal se parte en una parte lineal (A_{L}) y una cuadrática (A_{Q}), de 1 grado de libertad cada una, que corresponden a β_{1}x_{1} y β_{11}x_{1}^{2} del modelo. La interacción se parte en AB_{L×L}, AB_{L×Q}, AB_{Q×L} y AB_{Q×Q}, también de 1 grado de libertad, que corresponden a los términos x_{1}x_{2}, x_{1}x_{2}^{2}, x_{1}^{2}x_{2} y x_{1}^{2}x_{2}^{2}. Estos sí tienen interpretación: dicen qué forma tiene la superficie.

Segunda: los componentes AB y AB^{2}, de 2 grados de libertad cada uno. Se obtienen con dos cuadrados latinos ortogonales y no tienen significado físico; sirven para construir bloques y fracciones. El libro insiste en que no hay ninguna relación entre AB, AB^{2} y los componentes L×L, L×Q, Q×L, Q×Q.""",
  left=[cards(("Lineal y cuadrático", "Solo con factores **cuantitativos**. A_{L}, A_{Q}; AB_{L×L}, AB_{L×Q}, AB_{Q×L}, AB_{Q×Q}, de **1 g.l.** Tienen interpretación: la **forma** de la superficie"),
              ("Componentes AB y AB^{2}", "De **2 g.l.** cada uno. **Sin significado físico**. Sirven para **construir** bloques y fracciones"),
              size=15, cols=1)],
  right=[img(FIGS["lq"], h=2.9, caption="Contrastes lineal y cuadrático sobre los tres niveles"),
         note("No hay relación entre AB, AB^{2} y los componentes L × L, L × Q, Q × L, Q × Q", size=14)],
  ratio=0.48)

S("Componentes lineal y cuadrático con contrastes",
  """Con tres niveles equiespaciados, el contraste lineal usa los coeficientes (−1, 0, +1) y el cuadrático (+1, −2, +1). Son ortogonales entre sí. La suma de cuadrados de un contraste se calcula como siempre: SS = (Σ c_{i} T_{i})^{2} / (n Σ c_{i}^{2}), con T_{i} los totales de cada nivel. SS(A_{L}) + SS(A_{Q}) = SS_{A}.

Para la interacción se multiplican los coeficientes: AB_{L×Q} usa el producto del contraste lineal de A por el cuadrático de B en cada una de las nueve celdas. Las cuatro combinaciones suman SS_{AB}.

En el ejemplo de la vida de la herramienta del capítulo 5 (ejemplo 5-5) el libro obtiene SS(AB_{L×L}) = 8.00, SS(AB_{L×Q}) = 42.67, SS(AB_{Q×L}) = 2.67 y SS(AB_{Q×Q}) = 8.00, que suman SS_{AB} = 61.34. La partición es ortogonal.""",
  left=[tab(["Nivel", "Lineal", "Cuadrático"], [["0 (bajo)", "−1", "+1"], ["1 (intermedio)", "0", "−2"], ["2 (alto)", "+1", "+1"]],
            size=16, first_left=False),
        form("SS_{contraste} = (Σ c_{i} T_{i})^{2} / (n Σ c_{i}^{2})", size=18)],
  right=[tab(["Componente", "SS (ejemplo 5-5)"],
             [["AB_{L×L}", "8.00"], ["AB_{L×Q}", "42.67"], ["AB_{Q×L}", "2.67"], ["AB_{Q×Q}", "8.00"], ["**Suma = SS_{AB}**", "**61.34**"]],
             size=15, first_left=False),
         note("Para AB_{L×Q}: coeficiente de la celda (i, j) = L_{i} · Q_{j}", size=14)],
  ratio=0.5)

_tot55 = [[-3, -3, 5], [2, 4, 10], [-1, 11, -1]]
_la = [["Q", "R", "S"], ["R", "S", "Q"], ["S", "Q", "R"]]
_lb = [["Q", "S", "R"], ["R", "Q", "S"], ["S", "R", "Q"]]
S("Los componentes AB y AB^{2}: dos cuadrados latinos ortogonales",
  """Se toman los totales de las nueve celdas de la tabla A × B (filas A, columnas B) y se les superponen dos cuadrados latinos 3 × 3 ortogonales, con letras Q, R y S. Ortogonales quiere decir que cada letra del primero aparece exactamente una vez con cada letra del segundo.

Para cada cuadrado se suman los totales que llevan la misma letra, y se calcula la suma de cuadrados entre los tres totales de letra: SS = (T_{Q}^{2} + T_{R}^{2} + T_{S}^{2}) / (3n) − y_{…}^{2} / (9n), con 2 grados de libertad. La del cuadrado a se llama componente AB; la del cuadrado b, componente AB^{2}.

Con los totales del ejemplo 5-5 (n = 2): en el cuadrado a, Q = 18, R = −2 y S = 8, de donde SS = 33.34. En el cuadrado b, Q = 0, R = 6 y S = 18, de donde SS = 28.00. Y 33.34 + 28.00 = 61.34 = SS_{AB}, con 2 + 2 = 4 grados de libertad.""",
  left=[txt("**Totales de celda (ej. 5-5) con el cuadrado a**", size=15),
        tab(["A \\ B", "0", "1", "2"], [[str(i)] + [f"{_tot55[i][j]} ({_la[i][j]})" for j in range(3)] for i in range(3)],
            size=15, first_left=False),
        txt("**Con el cuadrado b**", size=15),
        tab(["A \\ B", "0", "1", "2"], [[str(i)] + [f"{_tot55[i][j]} ({_lb[i][j]})" for j in range(3)] for i in range(3)],
            size=15, first_left=False)],
  right=[tab(["", "Cuadrado a → AB", "Cuadrado b → AB^{2}"],
             [["Q", "−3 + 10 + 11 = 18", "−3 + 4 − 1 = 0"], ["R", "−3 + 2 − 1 = −2", "5 + 2 − 1 = 6"],
              ["S", "5 + 4 − 1 = 8", "−3 + 10 + 11 = 18"], ["SS", "(18² + 2² + 8²)/6 − 24²/18 = **33.34**", "(0² + 6² + 18²)/6 − 24²/18 = **28.00**"]],
             size=14, colw=[0.1, 0.45, 0.45], first_left=False),
         note("33.34 + 28.00 = 61.34 = SS_{AB}  (2 + 2 = 4 g.l.)", size=15)],
  ratio=0.46)

S("La regla que define cada componente: L = x_{1} + x_{2} y L = x_{1} + 2x_{2} (mod 3)",
  """Los dos cuadrados no son arbitrarios. Si los niveles de A y B son x_{1} y x_{2}, las letras del cuadrado a se asignan según x_{1} + x_{2} (mod 3): Q cuando vale 0, R cuando vale 1 y S cuando vale 2. Las del cuadrado b según x_{1} + 2x_{2} (mod 3). Por ejemplo, la celda central tiene x_{1} = 1 y x_{2} = 1; en el cuadrado b, 1 + 2(1) = 3 = 0 (mod 3), así que le toca Q.

De ahí viene el nombre: el componente AB corresponde a la ecuación x_{1} + x_{2}, con exponentes 1 y 1; el componente AB^{2} a x_{1} + 2x_{2}, con exponentes 1 y 2. Esta correspondencia entre exponentes y coeficientes es la que después construye bloques y fracciones.

Yates llamó a estos componentes I y J: I(AB) = AB^{2} y J(AB) = AB. En las tablas de totales se calculan como diagonales: las diagonales hacia abajo de izquierda a derecha dan AB^{2} (I) y las de derecha a izquierda dan AB (J).""",
  left=[tab(["Cuadrado a → componente AB", "Cuadrado b → componente AB^{2}"],
            [["Q:  x_{1} + x_{2} = 0 (mod 3)", "Q:  x_{1} + 2x_{2} = 0 (mod 3)"],
             ["R:  x_{1} + x_{2} = 1 (mod 3)", "R:  x_{1} + 2x_{2} = 1 (mod 3)"],
             ["S:  x_{1} + x_{2} = 2 (mod 3)", "S:  x_{1} + 2x_{2} = 2 (mod 3)"]], size=15, first_left=False),
        note("Los **exponentes** del componente son los **coeficientes** de la ecuación: AB^{2} ↔ x_{1} + 2x_{2}", size=15)],
  right=[form("I(AB) = AB^{2}", "J(AB) = AB", size=22),
         bul("Diagonales ↘ (de izquierda a derecha): **AB^{2}** (I)",
             "Diagonales ↙ (de derecha a izquierda): **AB** (J)",
             "Celda central (1, 1): 1 + 2·1 = 0 (mod 3) → Q en el cuadrado b", size=15)],
  ratio=0.55)

S("La convención de exponentes: el primero siempre es 1",
  """Al escribir componentes de la forma A^{p}B^{q} se establece que el único exponente permitido en la primera letra es 1. Si no lo es, la expresión completa se eleva al cuadrado y los exponentes se reducen módulo 3. Por ejemplo, A^{2}B es lo mismo que AB^{2}, porque (A^{2}B)^{2} = A^{4}B^{2} = AB^{2}.

La razón es que A^{2}B y AB^{2} definen la misma partición: x_{1} + 2x_{2} y 2x_{1} + x_{2} = 2(x_{1} + 2x_{2}) (mod 3) separan las nueve celdas en los mismos tres grupos, solo con las etiquetas permutadas. Elevar al cuadrado equivale a multiplicar la ecuación por 2.

Esta convención se usa en todo el capítulo: al multiplicar palabras para obtener alias o interacciones generalizadas, el resultado siempre se normaliza para que la primera letra tenga exponente 1.""",
  left=[form("A^{2}B = (A^{2}B)^{2} = A^{4}B^{2} = AB^{2}", size=22),
        num("Multiplicar las letras sumando exponentes", "Reducir cada exponente **módulo 3** (A^{3} = I desaparece)",
            "Si la primera letra queda con exponente 2, **elevar todo al cuadrado** y reducir otra vez", size=16)],
  right=[tab(["Expresión", "Normalizada"],
             [["A^{2}B", "AB^{2}"], ["A^{2}BCD", "AB^{2}C^{2}D^{2}"], ["B^{2}CD (sin A)", "BC^{2}D^{2}"], ["A^{3}B^{2}C", "BC^{2}"]],
             size=15, first_left=False),
         note("Mismo grupo de celdas, etiquetas permutadas: x_{1} + 2x_{2} y 2x_{1} + x_{2} son la **misma partición**", size=14)],
  ratio=0.5)

S("Tres factores: los componentes W, X, Y, Z de ABC",
  """La interacción ABC de un 3^{3} tiene 8 grados de libertad y se parte en cuatro componentes ortogonales de 2 grados de libertad, que el libro llama W, X, Y y Z: W(ABC) = AB^{2}C^{2}, X(ABC) = AB^{2}C, Y(ABC) = ABC^{2} y Z(ABC) = ABC. Ninguna primera letra tiene exponente distinto de 1.

En general, una interacción de h factores tiene 2^{h} grados de libertad y 2^{h−1} componentes de 2 grados de libertad. ABCD tiene 8: ABCD, ABCD^{2}, ABC^{2}D, AB^{2}CD, ABC^{2}D^{2}, AB^{2}C^{2}D, AB^{2}CD^{2} y AB^{2}C^{2}D^{2}. Con la convención de exponentes: A^{2}BCD = (A^{2}BCD)^{2} = AB^{2}C^{2}D^{2}.

Igual que AB y AB^{2}, estos componentes no tienen interpretación práctica. Normalmente no se descomponen las interacciones de tres o más factores en la tabla ANOVA; se calculan solo cuando hace falta construir o analizar un diseño en bloques o una fracción.""",
  left=[form("W(ABC) = AB^{2}C^{2}", "X(ABC) = AB^{2}C", "Y(ABC) = ABC^{2}", "Z(ABC) = ABC", size=19),
        note("Cada componente tiene **2 g.l.**; los cuatro suman los **8 g.l.** de ABC", size=15)],
  right=[tab(["Interacción", "g.l.", "Componentes de 2 g.l."],
             [["AB", "4", "2: AB, AB^{2}"], ["ABC", "8", "4: W, X, Y, Z"], ["ABCD", "16", "8: ABCD, ABCD^{2}, …, AB^{2}C^{2}D^{2}"],
              ["h factores", "2^{h}", "2^{h−1}"]], size=15, colw=[0.25, 0.15, 0.6]),
         note("Sin interpretación práctica; útiles para **construir** diseños", size=14)],
  ratio=0.45)

S("Cómo se calcula un componente: la regla L mod 3 con los totales",
  """La forma más directa de calcular cualquier componente, de dos o más factores, es la misma regla que define a AB y AB^{2}. Para el componente A^{α₁}B^{α₂}C^{α₃} se calcula, en cada corrida, L = α_{1}x_{1} + α_{2}x_{2} + α_{3}x_{3} (mod 3). Las corridas se reparten en tres grupos según L = 0, 1 o 2; se suman los totales de cada grupo (T_{0}, T_{1}, T_{2}) y SS = (T_{0}^{2} + T_{1}^{2} + T_{2}^{2}) / (N/3) − y_{…}^{2}/N, con N el número total de observaciones y 2 grados de libertad.

El libro lo hace de otro modo, por tablas de dos vías (procedimiento de Cochran y Cox y de Davies): primero se calculan los totales I(AB) y J(AB) en cada nivel de C; después se forman las tablas C × I(AB) y C × J(AB) y se toman sus diagonales I y J. Las cuatro diagonales dan W = I[I(AB) × C], X = J[I(AB) × C], Y = I[J(AB) × C] y Z = J[J(AB) × C]. Los dos métodos dan lo mismo; el de L es el que usa el ejemplo 2.""",
  left=[num("Para cada corrida, calcular **L = Σ α_{i} x_{i} (mod 3)** con los exponentes del componente",
            "Agrupar las corridas por L = 0, 1, 2 y sumar: **T_{0}, T_{1}, T_{2}**",
            "**SS = (T_{0}² + T_{1}² + T_{2}²) / (N/3) − y_{…}² / N**, con 2 g.l.", size=16)],
  right=[tab(["Componente", "L (mod 3)"],
             [["AB", "x_{1} + x_{2}"], ["AB^{2}", "x_{1} + 2x_{2}"], ["AB^{2}C^{2} (W)", "x_{1} + 2x_{2} + 2x_{3}"],
              ["AB^{2}C (X)", "x_{1} + 2x_{2} + x_{3}"], ["ABC^{2} (Y)", "x_{1} + x_{2} + 2x_{3}"], ["ABC (Z)", "x_{1} + x_{2} + x_{3}"]],
             size=15, first_left=False),
         note("Método del libro: tablas C × I(AB) y C × J(AB) y sus diagonales. Mismo resultado", size=14)],
  ratio=0.5)

# ---------------------------------------------------------------- 3
section(3, "Los diseños 3^{2} y 3^{3}", "Análisis completo con dos ejemplos del libro")

E(1, "rendimiento de un proceso químico", "Montgomery, problema 9-6",
  ["En un proceso químico se quiere **aumentar el rendimiento** (%). Se sospecha que la temperatura y la presión influyen y que la relación no es lineal: podría haber un valor intermedio que rinda más.",
   "Se estudian los dos factores con tres niveles cada uno: A temperatura (80, 90 y 100 °C) y B presión (100, 120 y 140 psig). Los dos son cuantitativos y equiespaciados.",
   "Se corre un **3^{2} con dos réplicas**: 18 corridas en orden aleatorio."],
  "Saber cómo afectan la temperatura y la presión al rendimiento, si hay **curvatura**, y dónde conviene operar",
  ["Hacer el ANOVA del 3^{2}", "Partir los efectos en componentes lineal y cuadrático",
   "Calcular los componentes AB y AB^{2} y comprobar que suman SS_{AB}", "Ajustar el modelo cuadrático y recomendar las condiciones"])

S("Ejemplo 1 · Datos y ANOVA",
  f"""La tabla muestra las 18 observaciones. Hipótesis para cada fuente: H_{{0}}: el efecto es nulo contra H_{{A}}: no lo es. El ANOVA es el de cualquier factorial de dos factores con réplicas: 2 grados de libertad para A, 2 para B, 4 para AB y 9 para el error (9 celdas × 1).

Resultado: la temperatura es significativa (F_{{0}} = {f(an1[0][4])}, p = {f(an1[0][5], 4)}) y la presión también (F_{{0}} = {f(an1[1][4])}, p = {f(an1[1][5], 4)}); la interacción no (p = {f(an1[2][5], 4)}). Con F_{{0.05, 2, 9}} = {f(f_ppf(0.05, 2, 9))} y F_{{0.05, 4, 9}} = {f(f_ppf(0.05, 4, 9))}.

Las medias por nivel muestran la curvatura: el rendimiento sube de 80 a 90 °C y apenas cambia de 90 a 100; con la presión pasa algo parecido. Eso es lo que la partición siguiente va a cuantificar. Fuente: Montgomery, problema 9-6; el ANOVA se calculó aquí.""",
  left=[tab(["Temperatura", "100 psig", "120 psig", "140 psig"],
            [[t] + [", ".join(f(v, 2) for v in y96[(i, j)]) for j in range(3)] for i, t in enumerate(["80 °C", "90 °C", "100 °C"])],
            size=14, first_left=False),
        tab(["Medias", "A = 80", "A = 90", "A = 100", "B = 100", "B = 120", "B = 140"],
            [["ȳ"] + [f(sum(med1[(i, j)] for j in range(3)) / 3, 1) for i in range(3)] + [f(sum(med1[(i, j)] for i in range(3)) / 3, 1) for j in range(3)]],
            size=13, first_left=False)],
  right=[tab(["SV", "SS", "DF", "MS", "F_{0}", "P-Value"], anova_rows(an1, sse1, dfe1, mse1, d1.sst(), 17), size=15),
         note(f"A y B significativos (F_{{0.05, 2, 9}} = {f(f_ppf(0.05, 2, 9))}); AB no", size=15)],
  ratio=0.5)

S("Ejemplo 1 · Partición lineal y cuadrática",
  f"""Como los dos factores son cuantitativos, cada uno se parte en su componente lineal y cuadrático con los contrastes (−1, 0, +1) y (+1, −2, +1) sobre los totales de nivel. SS(A_{{L}}) = {f(lq1['A_{L}'])} y SS(A_{{Q}}) = {f(lq1['A_{Q}'])}, que suman SS_{{A}} = {f(an1[0][1])}. Para la presión, SS(B_{{L}}) = {f(lq1['B_{L}'])} y SS(B_{{Q}}) = {f(lq1['B_{Q}'])}.

Cada componente tiene 1 grado de libertad y se prueba contra el mismo MS_{{E}} = {f(mse1)}: F_{{0.05, 1, 9}} = {f(f_ppf(0.05, 1, 9))}. Los dos términos lineales son claramente significativos; los cuadráticos quedan en el límite (A_{{Q}}: F_{{0}} = {f(lq1['A_{Q}'] / mse1)}; B_{{Q}}: F_{{0}} = {f(lq1['B_{Q}'] / mse1)}). Hay evidencia de curvatura, más clara en la presión.

La interacción se parte en cuatro componentes de 1 grado de libertad. Solo AB_{{L×L}} = {f(lq1['AB_{L×L}'])} es apreciable (F_{{0}} = {f(lq1['AB_{L×L}'] / mse1)}); los otros tres son pequeños. Esa es la partición que sí se interpreta: dice qué términos del modelo cuadrático hacen falta.""",
  left=[tab(["Componente", "SS", "DF", "F_{0}", "¿Significativo al 5 %?"],
            [[k, f(v), "1", f(v / mse1), "Sí" if v / mse1 > f_ppf(0.05, 1, 9) else "No"] for k, v in lq1.items()],
            size=14, hl=[0, 2, 4], first_left=False)],
  right=[form(f"SS(A_{{L}}) + SS(A_{{Q}}) = {f(lq1['A_{L}'])} + {f(lq1['A_{Q}'])} = {f(an1[0][1])} = SS_{{A}}", size=15),
         form(f"Σ SS(AB_{{·×·}}) = {f(an1[2][1])} = SS_{{AB}}", size=15),
         bul("Términos lineales: claros", "Cuadráticos: en el límite (hay **curvatura**, sobre todo en la presión)",
             "De la interacción solo importa **L × L**", size=15)],
  ratio=0.52)

S("Ejemplo 1 · Los componentes AB y AB^{2} con la regla L",
  f"""Ahora la otra partición, la que no se interpreta pero sirve para bloques y fracciones. Con los totales de las nueve celdas se agrupan las corridas según L = x_{{1}} + x_{{2}} (mod 3) para el componente AB y según L = x_{{1}} + 2x_{{2}} (mod 3) para AB^{{2}}. Cada grupo tiene 6 observaciones.

Para AB los totales de grupo son {', '.join(f(t, 2) for t in tAB1)} y SS_{{AB}} = {f(cAB1)}. Para AB^{{2}}, {', '.join(f(t, 2) for t in tAB21)} y SS_{{AB²}} = {f(cAB21)}. La suma es {f(cAB1 + cAB21)}, que es SS_{{AB}} del ANOVA, con 2 + 2 = 4 grados de libertad.

Observe que estos dos números no coinciden con ninguna combinación de los componentes L × L, L × Q, Q × L y Q × Q: son particiones distintas de la misma suma de cuadrados.""",
  left=[tab(["Celda (A, B)", "Total", "x_{1} + x_{2}", "x_{1} + 2x_{2}"],
            [[f"{a}{b}", f(sum(y96[(a, b)]), 2), str((a + b) % 3), str((a + 2 * b) % 3)] for a in range(3) for b in range(3)],
            size=13, first_left=False, pad=0.06)],
  right=[tab(["Componente", "T_{0}", "T_{1}", "T_{2}", "SS"],
             [["AB  (L = x_{1} + x_{2})"] + [f(t, 2) for t in tAB1] + [f(cAB1)],
              ["AB^{2}  (L = x_{1} + 2x_{2})"] + [f(t, 2) for t in tAB21] + [f(cAB21)]], size=14),
         form(f"SS = (T_{{0}}² + T_{{1}}² + T_{{2}}²) / 6 − y_{{…}}² / 18", size=16),
         note(f"{f(cAB1)} + {f(cAB21)} = {f(cAB1 + cAB21)} = SS_{{AB}}  (2 + 2 = 4 g.l.)", size=15)],
  ratio=0.46)

S("Ejemplo 1 · Modelo cuadrático y condiciones recomendadas",
  f"""Con x_{{1}} = (temperatura − 90)/10 y x_{{2}} = (presión − 120)/20, el ajuste por mínimos cuadrados del modelo de la ecuación 9-1 da {modelo(b1)}. El libro reporta el mismo modelo (inciso c del problema; el coeficiente de x_{{2}}^{{2}} aparece como −7.86).

Los coeficientes cuadráticos negativos dicen que la superficie es un máximo: el rendimiento sube con cada factor hasta cierto punto y luego baja. El término x_{{1}}x_{{2}} negativo dice que el aumento por temperatura es menor cuando la presión es alta.

Igualando a cero las derivadas parciales se obtiene el punto estacionario: x_{{1}} = {f(xs1)} y x_{{2}} = {f(xs2)}, es decir temperatura {f(90 + 10 * xs1, 0)} °C y presión {f(120 + 20 * xs2, 0)} psig, con rendimiento estimado {f(ys1, 1)} %. Esa sería la condición recomendada, que conviene confirmar con corridas adicionales. Un diseño central compuesto habría llegado a lo mismo con menos corridas.""",
  left=[form(modelo(b1), size=16),
        form("x_{1} = (T − 90)/10,   x_{2} = (P − 120)/20", size=15),
        bul("β_{11}, β_{22} < 0 → la superficie tiene un **máximo**",
            "β_{12} < 0 → menos ganancia por temperatura cuando la presión es alta",
            f"Punto estacionario: **T ≈ {f(90 + 10 * xs1, 0)} °C, P ≈ {f(120 + 20 * xs2, 0)} psig**, ŷ ≈ {f(ys1, 1)} %", size=15)],
  right=[img(FIGS["ej1"], h=4.4, caption="Contornos del rendimiento estimado (cálculo propio)")],
  ratio=0.52)

E(2, "pérdida de jarabe por espumeo", "Montgomery, ejemplo 9-1",
  ["Una máquina llena contenedores metálicos de 5 galones con jarabe para una bebida gaseosa. Al llenar, el jarabe **hace espuma y se pierde** parte del producto. Se quiere reducir esa pérdida.",
   "Se piensa que influyen tres factores: A el **diseño de la boquilla** (tres tipos: 1, 2 y 3, un factor **cualitativo**), B la **velocidad de llenado** (100, 120 y 140 rpm) y C la **presión de operación** (10, 15 y 20 psi).",
   "Se corre un **3^{3} con dos réplicas**, 54 observaciones. La respuesta se codifica como centímetros cúbicos perdidos menos 70."],
  "Encontrar la boquilla, la velocidad y la presión que **minimizan la pérdida** de jarabe",
  ["Hacer el ANOVA del 3^{3}", "Interpretar las interacciones de dos factores",
   "Ajustar un modelo cuadrático por boquilla y leer los contornos", "Partir ABC en sus componentes W, X, Y, Z con la regla L"])

_vel = ["100", "120", "140"]
S("Ejemplo 2 · Datos (tabla 9-1)",
  """Las 54 observaciones, en cm³ − 70. Las filas son la presión C, las columnas la boquilla A y dentro de cada boquilla la velocidad B; cada celda tiene dos réplicas. Este ejemplo es el caso típico en que el libro considera razonable un 3^{k}: hay un factor cualitativo con tres niveles de interés (la boquilla) y los otros dos son cuantitativos.""",
  body=[tab(["Presión C", "Boq. 1 · 100", "Boq. 1 · 120", "Boq. 1 · 140", "Boq. 2 · 100", "Boq. 2 · 120", "Boq. 2 · 140", "Boq. 3 · 100", "Boq. 3 · 120", "Boq. 3 · 140"],
            [[p] + [f"{y91[(a, b, c)][0]}, {y91[(a, b, c)][1]}" for a in range(3) for b in range(3)] for c, p in enumerate(["10 psi", "15 psi", "20 psi"])],
            size=14, first_left=False),
        note("Respuesta = cm³ de jarabe perdido − 70. Dos réplicas por celda (n = 2), 54 observaciones", size=15)])

S("Ejemplo 2 · ANOVA (tabla 9-2)",
  f"""Hipótesis para cada fuente: H_{{0}}: el efecto es nulo. Las sumas de cuadrados se calculan con los métodos usuales. Con 27 celdas y dos réplicas el error tiene 27 grados de libertad.

Resultado: la velocidad de llenado (B) y la presión (C) son muy significativas; la boquilla (A) no lo es como efecto principal (p = {f(an2[0][5], 4)}). Las tres interacciones de dos factores sí son significativas: AB (p = {f(an2[3][5], 4)}), AC (p = {f(an2[4][5], 4)}) y BC (p = {f(an2[5][5], 4)}). ABC no (p = {f(an2[6][5], 4)}).

Que la boquilla no sea significativa como efecto principal pero sí en sus interacciones significa que el efecto de la boquilla depende de la velocidad y de la presión: hay que mirar las gráficas de interacción. Nota para quien coteje: las SS y los F_{{0}} coinciden con la tabla 9-2; los valores p de AB, AC y BC que imprime el libro (0.0383, 0.0222 y 0.0025) no corresponden a esos F con 4 y 27 grados de libertad; los correctos son {f(an2[3][5], 4)}, {f(an2[4][5], 4)} y {f(an2[5][5], 4)}.""",
  left=[tab(["SV", "SS", "DF", "MS", "F_{0}", "P-Value"],
            anova_rows([(("A, boquilla", "B, velocidad", "C, presión", "AB", "AC", "BC", "ABC")[i],) + tuple(r[1:]) for i, r in enumerate(an2)],
                       sse2, dfe2, mse2, d2.sst(), 53), size=14, hl=[1, 2, 3, 4, 5])],
  right=[bul("**B y C** muy significativos", "**A** no como efecto principal…", "…pero **AB, AC y BC** sí: el efecto de la boquilla **depende** de velocidad y presión",
             "ABC no significativa", size=16),
         note("Los valores p de AB, AC y BC impresos en la tabla 9-2 no corresponden a sus F_{0}; aquí se recalcularon", size=13)],
  ratio=0.6)

S("Ejemplo 2 · Las interacciones de dos factores (fig. 9-4)",
  """Las gráficas usan los totales de celda, como en la figura 9-4 del libro. A × B: con velocidad 120 rpm la pérdida es mucho menor para cualquier boquilla; con 100 o 140 rpm es mayor y la boquilla 2 se comporta distinto. A × C: la presión intermedia (15 psi) da pérdidas altas con las tres boquillas; 10 y 20 psi dan pérdidas bajas. B × C: con cualquier presión, 120 rpm es lo mejor, pero el salto es enorme con 15 psi.

Conclusión del libro: el nivel intermedio de la velocidad produce el mejor desempeño, mientras que las boquillas 2 y 3 y la presión baja (10 psi) o alta (20 psi) parecen ser las más efectivas para reducir la pérdida.""",
  left=[lines(["Boquilla 1", "Boquilla 2", "Boquilla 3"],
              [(f"B = {v} rpm", [cel(0, 1, a, b) for a in range(3)]) for b, v in enumerate(_vel)],
              "Total de celda A × B", h=2.55, title="A × B"),
        lines(["Boquilla 1", "Boquilla 2", "Boquilla 3"],
              [(f"C = {p} psi", [cel(0, 2, a, c) for a in range(3)]) for c, p in enumerate(["10", "15", "20"])],
              "Total de celda A × C", h=2.55, title="A × C")],
  right=[lines(["100 rpm", "120 rpm", "140 rpm"],
               [(f"C = {p} psi", [cel(1, 2, b, c) for b in range(3)]) for c, p in enumerate(["10", "15", "20"])],
               "Total de celda B × C", h=3.6, title="B × C"),
         note("Mejor: **120 rpm**, boquillas **2 o 3**, presión **10 o 20 psi**", size=15)],
  ratio=0.5)

S("Ejemplo 2 · Un modelo cuadrático por boquilla (tabla 9-3)",
  f"""Como la boquilla es cualitativa, no entra en un modelo de regresión. Lo que hace el libro es ajustar, para cada boquilla, un modelo cuadrático en los dos factores cuantitativos, velocidad (x_{{1}}) y presión (x_{{2}}), codificados −1, 0, +1. Los modelos de la tabla 9-3 se reproducen aquí por mínimos cuadrados.

Las gráficas de contorno muestran que las superficies son muy distintas de una boquilla a otra: la de la boquilla 2 es más alargada. El libro advierte que, cuando se mezclan factores cualitativos y cuantitativos, las condiciones óptimas de los cuantitativos pueden ser muy diferentes en cada nivel del cualitativo.

Como el objetivo es minimizar la pérdida, se prefiere la boquilla 3: es la única cuyos contornos llegan a −60. Con ella debe usarse la velocidad cerca de 120 rpm y la presión baja o alta.

Nota para quien coteje: los modelos de las boquillas 1 y 3 coinciden con la tabla 9-3. El de la boquilla 2 no: el libro imprime ŷ = 25.6 − 22.8x_{{1}} − 12.3x_{{2}} + 14.1x_{{1}}^{{2}} − 56.9x_{{2}}^{{2}} − 0.7x_{{1}}x_{{2}}, que no reproduce los datos de la tabla 9-1 (la celda central de la boquilla 2 promedia −49.5 y el modelo del libro da 25.6 en el centro). El modelo de esta diapositiva se ajustó a los datos impresos.""",
  left=[tab(["Boquilla", "Modelo en unidades codificadas (x_{1} = velocidad, x_{2} = presión)"],
            [[str(a + 1), modelo(mod2[a], dec=1)] for a in range(3)], size=13, colw=[0.14, 0.86]),
        note("Se prefiere la **boquilla 3**: la única con contornos de **−60**. Velocidad ≈ 120 rpm; presión baja o alta", size=14),
        txt("Boquillas 1 y 3: iguales a la tabla 9-3. Boquilla 2: el modelo impreso en el libro no reproduce los datos de la tabla 9-1; aquí se reajustó.", size=12)],
  right=[img(FIGS["boq3"], h=4.3, caption="Contornos de la boquilla 3 (cálculo propio, como la fig. 9-5c)")],
  ratio=0.55)

S("Ejemplo 2 · Contornos de las tres boquillas (fig. 9-5)",
  """Las tres superficies lado a lado. Las boquillas 1 y 3 tienen forma de silla, con el mínimo en la banda de 120 rpm y en las presiones extremas; la boquilla 2 tiene una superficie alargada y nunca baja de −20. Cuando hay un factor cualitativo, la forma de la superficie cambia con él, y por eso se ajusta un modelo por nivel.""",
  left=[img(FIGS["boq1"], h=4.4, caption="Boquilla 1 (como la fig. 9-5a)")],
  right=[img(FIGS["boq2"], h=4.4, caption="Boquilla 2 (como la fig. 9-5b)")])

S("Ejemplo 2 · Partición de ABC en W, X, Y y Z",
  f"""Para ilustrar la regla L con tres factores se parte SS_{{ABC}} = {f(an2[6][1])} en sus cuatro componentes. Con los 27 totales de celda se calcula, para cada componente, L (mod 3) y se agrupan los totales en T_{{0}}, T_{{1}} y T_{{2}}; cada grupo tiene 18 observaciones, así que SS = (T_{{0}}² + T_{{1}}² + T_{{2}}²)/18 − 165²/54, donde 165 es el gran total.

Resultado: W = AB^{{2}}C^{{2}} = {f(wxyz['W = AB^{2}C^{2}'][0])}, X = AB^{{2}}C = {f(wxyz['X = AB^{2}C'][0])}, Y = ABC^{{2}} = {f(wxyz['Y = ABC^{2}'][0])} y Z = ABC = {f(wxyz['Z = ABC'][0])}, que suman {f(sum(v[0] for v in wxyz.values()))} = SS_{{ABC}}. El libro obtiene los mismos cuatro números (3804.11, 221.77, 18.77 y 584.11) por el método de las tablas C × I(AB) y C × J(AB).

Nota para quien coteje: en el libro los nombres de Y y Z aparecen intercambiados (ABC^{{2}} = 18.77 y ABC = 584.11), porque ordena los totales J de 2 a 0 en lugar de 0 a 2; con la definición L = x_{{1}} + x_{{2}} + 2x_{{3}} el componente ABC^{{2}} da {f(wxyz['Y = ABC^{2}'][0])}. Como estos componentes no tienen interpretación, no se presentan en el ANOVA.""",
  left=[tab(["Componente", "L (mod 3)", "T_{0}", "T_{1}", "T_{2}", "SS"],
            [[n, l] + [str(t) for t in v[1]] + [f(v[0])] for (n, v), l in
             zip(wxyz.items(), ["x_{1} + 2x_{2} + 2x_{3}", "x_{1} + 2x_{2} + x_{3}", "x_{1} + x_{2} + 2x_{3}", "x_{1} + x_{2} + x_{3}"])],
            size=14, colw=[0.22, 0.3, 0.12, 0.12, 0.12, 0.12])],
  right=[form("SS = (T_{0}² + T_{1}² + T_{2}²) / 18 − 165² / 54", size=16),
         note(f"Suma = {f(sum(v[0] for v in wxyz.values()))} = SS_{{ABC}}  (4 × 2 = 8 g.l.)", size=15),
         txt("El libro imprime los nombres de Y y Z intercambiados; los cuatro valores y la suma coinciden.", size=13)],
  ratio=0.6)

# ---------------------------------------------------------------- 4
section(4, "Confusión en tres bloques", "Definición de contrastes L mod 3, bloque principal y dos ejemplos")

S("¿Por qué confundir un 3^{k} en bloques?",
  """Incluso una sola réplica de un 3^{3} son 27 corridas, y es improbable que puedan hacerse todas en condiciones uniformes: un mismo día, un mismo lote de materia prima, un mismo operario. La solución es la misma del capítulo 7: repartir las corridas en bloques incompletos, aceptando que algún efecto quede confundido con las diferencias entre bloques.

El 3^{k} se puede confundir en 3^{p} bloques incompletos, con p < k: tres bloques, nueve bloques, veintisiete, etcétera. Con tres bloques hay 2 grados de libertad entre bloques, así que lo que se confunde es exactamente un componente de interacción de 2 grados de libertad: AB o AB^{2} en un 3^{2}; ABC, ABC^{2}, AB^{2}C o AB^{2}C^{2} en un 3^{3}. Aquí es donde los componentes de la sección 2 muestran su utilidad.""",
  left=[bul("27 corridas difícilmente se hacen en **condiciones uniformes**",
            "Bloques incompletos: 3^{p} bloques de 3^{k−p} corridas",
            "3 bloques → **2 g.l.** entre bloques → se confunde **un componente de 2 g.l.**", size=16)],
  right=[tab(["Diseño", "Bloques", "Se confunde"],
             [["3^{2}", "3", "AB o AB^{2}"], ["3^{3}", "3", "ABC, ABC^{2}, AB^{2}C o AB^{2}C^{2}"],
              ["3^{k}", "3", "un componente de la interacción de orden más alto"]], size=15, colw=[0.15, 0.17, 0.68]),
         note("Regla: confundir siempre un componente de la **interacción de orden más alto**", size=15)],
  ratio=0.45)

S("La definición de contrastes: L = α_{1}x_{1} + α_{2}x_{2} + ··· + α_{k}x_{k} (mod 3)",
  """El procedimiento es construir la definición de contrastes de la ecuación 9-2: L = α_{1}x_{1} + α_{2}x_{2} + ··· + α_{k}x_{k}, donde α_{i} es el exponente del factor i en el componente que se va a confundir (0, 1 o 2, con el primer α distinto de cero igual a 1) y x_{i} es el nivel del factor i en la combinación (0, 1 o 2). Las combinaciones se asignan a los bloques según el valor de L (mod 3): como solo puede valer 0, 1 o 2, quedan tres bloques definidos de manera única.

El bloque con L = 0 (mod 3) se llama bloque principal y siempre contiene a la combinación 00…0.

Ejemplo: un 3^{2} en tres bloques confundiendo AB^{2}. Los exponentes son 1 y 2, así que L = x_{1} + 2x_{2}. Para 01: L = 1(0) + 2(1) = 2. Para 11: 1 + 2 = 3 = 0 (mod 3). Para 22: 2 + 4 = 6 = 0 (mod 3). Así se reparten las nueve combinaciones (figura 9-6).""",
  left=[form("L = α_{1}x_{1} + α_{2}x_{2} + ··· + α_{k}x_{k}  (mod 3)", size=18),
        bul("α_{i} = exponente del factor i en el componente confundido", "x_{i} = nivel del factor i (0, 1, 2)",
            "Bloque = valor de L (mod 3); **bloque principal**: L = 0, contiene a 00…0", size=15),
        tab(["Combinación", "00", "01", "02", "10", "11", "12", "20", "21", "22"],
            [["L = x_{1} + 2x_{2} (mod 3)"] + [str((a + 2 * b) % 3) for a in range(3) for b in range(3)]], size=13)],
  right=[img(FIGS["bloques"], h=4.2, caption="El 3^{2} en tres bloques con AB^{2} confundida (fig. 9-6)")],
  ratio=0.55)

S("El bloque principal es un grupo: los otros bloques se generan sumando",
  """Los elementos del bloque principal forman un grupo con respecto a la adición módulo 3, dígito a dígito. En el 3^{2} con AB^{2} confundida, el bloque principal es {00, 11, 22}: 11 + 11 = 22 y 11 + 22 = 33 = 00. Cualquier suma de dos elementos del bloque principal cae en el bloque principal.

Esa propiedad permite construir los demás bloques sin calcular L para cada combinación: se toma cualquier combinación que no esté en el bloque principal y se suma (mod 3) a cada elemento del bloque principal. Con 10: 10 + 00 = 10, 10 + 11 = 21, 10 + 22 = 02, que es el bloque 2. Con 01: 01 + 00 = 01, 01 + 11 = 12, 01 + 22 = 20, que es el bloque 3.

Con tres factores el método es el mismo, y es la forma práctica de construir los bloques de 9 corridas del 3^{3}.""",
  left=[tab(["Bloque", "L", "Combinaciones", "Cómo se obtiene"],
            [["1 (principal)", "0", "00, 11, 22", "L = 0; es un grupo: 11 + 11 = 22, 11 + 22 = 00"],
             ["2", "1", "10, 21, 02", "10 + {00, 11, 22}"], ["3", "2", "01, 12, 20", "01 + {00, 11, 22}"]],
            size=15, colw=[0.18, 0.08, 0.26, 0.48])],
  right=[form("Bloque nuevo = (una combinación fuera del principal) + (bloque principal), mod 3", size=16),
         note("Suma dígito a dígito: 10 + 22 = 32 → 02 (mod 3)", size=15)],
  ratio=0.6)

E(3, "un 3^{2} en tres bloques", "Montgomery, ejemplo 9-2",
  ["Se corre **una sola réplica de un 3^{2}** cuyas nueve combinaciones no caben en condiciones homogéneas: hay que repartirlas en **tres bloques de tres corridas**, por ejemplo tres lotes de material o tres turnos.",
   "Se decide confundir el componente **AB^{2}** con los bloques, con la definición de contrastes L = x_{1} + 2x_{2} de la figura 9-6.",
   "Los datos (una observación por combinación) son: bloque 1: 00 = 4, 11 = −4, 22 = 0; bloque 2: 10 = −2, 21 = 1, 02 = 8; bloque 3: 01 = 5, 12 = −5, 20 = 0."],
  "Ver cómo se **analiza** un 3^{k} confundido en bloques y comprobar que SS_{Bloques} es exactamente el componente confundido",
  ["Calcular SS_{A} y SS_{B} como en un factorial sin bloques", "Calcular SS_{Bloques} con los totales de bloque",
   "Calcular el componente AB^{2} por diagonales y compararlo", "Armar la tabla ANOVA y decir qué se puede probar"])

_tab92 = [[str(a)] + [str(y92[(a, b)]) for b in range(3)] for a in range(3)]
S("Ejemplo 3 · SS_{Bloques} es exactamente SS_{AB²} (tabla 9-4)",
  f"""Al aplicar los métodos convencionales se encuentra SS_{{A}} = {f(d3.ss_effect((0,)))} y SS_{{B}} = {f(d3.ss_effect((1,)))}. Los totales de bloque son {', '.join(str(sum(y92[r] for r in v)) for _, v in sorted(bl3.items()))}, así que SS_{{Bloques}} = (0² + 7² + 0²)/3 − 7²/9 = {f(d3.ss_component((1, 2))[0])}.

Ese número es exactamente el componente AB^{{2}}. Para verlo, se escriben las observaciones en la tabla A × B y se calcula la suma de cuadrados entre los totales de las diagonales de izquierda a derecha, que son 0, 0 y 7: SS_{{AB²}} = (0² + 0² + 7²)/3 − 7²/9 = {f(d3.ss_component((1, 2))[0])}. Confundir AB^{{2}} con los bloques significa literalmente que su suma de cuadrados es la de los bloques. El otro componente, AB = {f(d3.ss_component((1, 1))[0])}, sí se estima.

Como hay una sola réplica, no puede hacerse una prueba formal: no hay grados de libertad para el error. El libro advierte que no es buena idea usar el componente AB como estimación del error.""",
  left=[tab(["A \\ B", "0", "1", "2"], _tab92, size=16, first_left=False),
        note("Diagonales ↘: 4 − 4 + 0 = **0**;  5 − 5 + 0 = **0**;  8 − 2 + 1 = **7**  →  SS_{AB²} = 10.89", size=14)],
  right=[tab(["SV", "SS", "DF"],
             [["Bloques (AB^{2})", f(d3.ss_component((1, 2))[0]), "2"], ["A", f(d3.ss_effect((0,))), "2"], ["B", f(d3.ss_effect((1,))), "2"],
              ["AB", f(d3.ss_component((1, 1))[0]), "2"], ["Total", f(d3.sst()), "8"]], size=15, hl=[0]),
         note("Una sola réplica: **no hay prueba formal**. No usar AB como error", size=15)],
  ratio=0.46)

_b33 = blocks(3, [(1, 2, 2)])
S("El 3^{3} en tres bloques de 9: AB^{2}C^{2} confundida",
  """Un diseño un poco más complicado: el 3^{3} en tres bloques de nueve corridas, confundiendo el componente AB^{2}C^{2}. La definición de contrastes es L = x_{1} + 2x_{2} + 2x_{3}. Es fácil verificar que 000, 012 y 101 están en el bloque principal (L = 0); las demás corridas del bloque principal se generan por sumas: 101 + 101 = 202, 012 + 012 = 021, 101 + 012 = 110, 101 + 021 = 122, 012 + 202 = 211, 021 + 202 = 220.

Para el bloque 2 se toma una combinación que no está en el principal, por ejemplo 200, y se suma a cada elemento: 200, 212, 001, 102, 221, 010, 022, 111, 120; todas cumplen L = 2. Para el bloque 3 se usa 100, que no está en los dos primeros: 100, 112, 201, 002, 121, 210, 222, 011, 020, con L = 1. Es la figura 9-7 del libro.

El ANOVA (tabla 9-5) conserva información de todos los efectos principales y de las interacciones de dos factores. Los otros tres componentes de ABC (ABC, AB^{2}C y ABC^{2}) se combinan como error, con 6 grados de libertad; su suma de cuadrados se obtiene por sustracción: SS_{ABC} calculada de la forma usual menos SS_{Bloques}.""",
  left=[tab(["Bloque", "L", "Corridas"],
            [[str(i + 1), str(k[0]), ", ".join(dig(r) for r in _b33[k])] for i, k in enumerate(((0,), (2,), (1,)))],
            size=14, colw=[0.12, 0.08, 0.8]),
        img(FIGS["cubo_bloq"], h=3.4)],
  right=[tab(["SV", "DF"], [["Bloques (AB^{2}C^{2})", "2"], ["A, B, C", "2 cada uno"], ["AB, AC, BC", "4 cada uno"],
                             ["Error (ABC + AB^{2}C + ABC^{2})", "6"], ["Total", "26"]], size=15, colw=[0.7, 0.3]),
         note("SS_{Error} = SS_{ABC} (usual) − SS_{Bloques}: los componentes **no confundidos** de ABC", size=14)],
  ratio=0.55)

E(4, "acomodar botellas en tres días", "Montgomery, problemas 9-3 y 9-9 (réplica I)",
  ["Una embotelladora quiere saber cuánto tarda un empleado en acomodar diez cajas de doce botellas en los aparadores de venta, y qué lo afecta. Se estudian tres factores con tres niveles: A el **tipo de botella** (plástico, vidrio de 28 mm, vidrio de 38 mm), B el **tipo de aparador** (anaquel permanente liso, aparador al final del pasillo, refrigerador para refrescos) y C el **empleado** (tres personas).",
   "El experimento completo es un 3^{3} (27 corridas por réplica). El problema 9-9 agrega una restricción: **no es posible hacer las 27 observaciones el mismo día**; se hacen en tres días, nueve cada día.",
   "Se usan los datos de la primera réplica del problema 9-3 (tiempo en minutos) y se confunde el componente **AB^{2}C** con los días."],
  "Repartir las 27 corridas en **tres días** sin perder los efectos principales ni las interacciones de dos factores, y analizar",
  ["Construir los tres bloques con L = x_{1} + 2x_{2} + x_{3}", "Calcular SS_{Bloques} y comprobar que es SS_{AB²C}",
   "Armar el ANOVA con el error formado por los otros componentes de ABC", "Concluir qué afecta el tiempo"])

S("Ejemplo 4 · Los tres días",
  f"""Con AB^{{2}}C los exponentes son 1, 2 y 1: L = x_{{1}} + 2x_{{2}} + x_{{3}} (mod 3). El bloque principal (L = 0) contiene a 000; se generan los nueve elementos por sumas y los otros dos bloques sumando 100 y 200. Cada día recibe nueve combinaciones, con los tres tipos de botella, los tres aparadores y los tres empleados representados tres veces cada uno: los bloques están balanceados en cada factor.

Los totales de los tres días son {', '.join(f(t, 2) for t in tbl4)} minutos, muy parecidos, y SS_{{Bloques}} = {f(ssbl4, 4)}. Si se calcula el componente AB^{{2}}C con la regla L sobre las 27 observaciones se obtiene exactamente el mismo valor: eso es lo que significa que esté confundido.""",
  body=[tab(["Día (bloque)", "L", "Combinaciones (A botella, B aparador, C empleado)", "Total (min)"],
            [[f"Día {i + 1}", str(k[0]), ", ".join(dig(r) for r in bl4[k]), f(sum(y93[r][0] for r in bl4[k]), 2)] for i, k in enumerate(((0,), (1,), (2,)))],
            size=14, colw=[0.14, 0.06, 0.64, 0.16]),
        note(f"SS_{{Bloques}} = Σ T_{{i}}²/9 − y_{{…}}²/27 = {f(ssbl4, 4)} = SS_{{AB²C}}. Cada día tiene cada nivel de cada factor **tres veces**", size=15)])

S("Ejemplo 4 · ANOVA con los días como bloques",
  f"""El ANOVA sigue la tabla 9-5: bloques (AB^{{2}}C) con 2 grados de libertad, los tres efectos principales con 2, las tres interacciones de dos factores con 4 y el error formado por los otros tres componentes de ABC, con 6 grados de libertad: SS_{{Error}} = SS_{{ABC}} − SS_{{Bloques}} = {f(ssABC4, 4)} − {f(ssbl4, 4)} = {f(ssABC4 - ssbl4, 4)}.

Resultado: el aparador (B) y el empleado (C) afectan mucho el tiempo (F_{{0}} = {f(an4[1][4])} y {f(an4[2][4])}, con F_{{0.05, 2, 6}} = {f(f_ppf(0.05, 2, 6))}); el tipo de botella no (p = {f(an4[0][5], 3)}). De las interacciones, BC está cerca del límite (p = {f(an4[5][5], 3)}): el efecto del aparador podría depender del empleado. Con las dos réplicas del problema 9-3, BC sí resulta significativa.

El precio de los bloques fue pequeño: solo se perdió un componente sin interpretación de ABC, y el error quedó con 6 grados de libertad en vez de 8.""",
  left=[tab(["SV", "SS", "DF", "MS", "F_{0}", "P-Value"],
            [["Bloques (AB^{2}C)", f(ssbl4, 4), "2", f(ssbl4 / 2, 4), "", ""]] +
            [[t, f(ss, 4), str(df), f(ms, 4), f(F), pv(p)] for t, ss, df, ms, F, p in an4] +
            [["Error (resto de ABC)", f(sse4, 4), "6", f(mse4, 4), "", ""], ["Total", f(d4.sst(), 4), "26", "", "", ""]],
            size=14, hl=[2, 3])],
  right=[bul("**Aparador** y **empleado**: muy significativos", "Tipo de botella: no", "BC en el límite: con dos réplicas sí es significativa",
             "Costo de los bloques: **un componente de ABC** y 2 g.l. de error", size=16),
         note(f"Medias por aparador: {', '.join(f(sum(y93[r][0] for r in y93 if r[1] == l) / 9, 2) for l in range(3))} min (permanente, pasillo, refrigerador)", size=14)],
  ratio=0.58)

# ---------------------------------------------------------------- 5
section(5, "Confusión en nueve y en 3^{p} bloques", "Interacciones generalizadas PQ y PQ^{2}")

S("Nueve bloques: se eligen dos componentes y se confunden cuatro",
  """Con nueve bloques hay 8 grados de libertad entre bloques, es decir cuatro componentes de 2 grados de libertad. Se eligen dos componentes de interacción, P y Q, y como resultado se confunden automáticamente otros dos: sus interacciones generalizadas. En el sistema 3^{k} las interacciones generalizadas de P y Q son PQ y PQ^{2} (o P^{2}Q, que es lo mismo normalizado).

Los dos componentes elegidos producen dos definiciones de contrastes (ecuación 9-3): L_{1} = α_{1}x_{1} + ··· + α_{k}x_{k} = u (mod 3) y L_{2} = β_{1}x_{1} + ··· + β_{k}x_{k} = h (mod 3), con u y h en {0, 1, 2}. Las combinaciones con el mismo par (L_{1}, L_{2}) van al mismo bloque; hay nueve pares posibles y por eso nueve bloques. El bloque principal es el de L_{1} = L_{2} = 0 y, como antes, es un grupo bajo la adición módulo 3 que sirve para generar los demás.""",
  left=[form("L_{1} = α_{1}x_{1} + ··· + α_{k}x_{k} = u (mod 3)", "L_{2} = β_{1}x_{1} + ··· + β_{k}x_{k} = h (mod 3)", size=17),
        bul("9 bloques → **8 g.l.** → **cuatro** componentes confundidos",
            "Se eligen **P y Q**; se confunden también **PQ y PQ^{2}**",
            "Bloque = par (L_{1}, L_{2}); principal = (0, 0)", size=16)],
  right=[note("En el 2^{k} la interacción generalizada de P y Q era solo PQ. En el 3^{k} son **dos**: PQ y PQ^{2}", size=15),
         tab(["Se eligen", "Se confunden además"], [["P, Q", "PQ, PQ^{2}"]], size=16, first_left=False)],
  ratio=0.55)

_P, _Q = (1, 1, 1, 0), (1, 2, 0, 2)
_gi = gen_ints(_P, _Q)
_b94 = blocks(4, [_P, _Q])
S("Ejemplo: el 3^{4} en nueve bloques con ABC y AB^{2}D^{2} (fig. 9-8)",
  f"""Se confunden ABC y AB^{{2}}D^{{2}}. Sus interacciones generalizadas son (ABC)(AB^{{2}}D^{{2}}) = A^{{2}}B^{{3}}CD^{{2}} = (A^{{2}}CD^{{2}})^{{2}} = AC^{{2}}D y (ABC)(AB^{{2}}D^{{2}})^{{2}} = A^{{3}}B^{{5}}CD^{{4}} = B^{{2}}CD = (B^{{2}}CD)^{{2}} = BC^{{2}}D^{{2}}. Quedan confundidos los cuatro: ABC, AB^{{2}}D^{{2}}, AC^{{2}}D y BC^{{2}}D^{{2}}.

Las definiciones de contrastes (ecuación 9-4) son L_{{1}} = x_{{1}} + x_{{2}} + x_{{3}} y L_{{2}} = x_{{1}} + 2x_{{2}} + 2x_{{4}}. El bloque principal tiene las nueve combinaciones con L_{{1}} = L_{{2}} = 0; los otros ocho se generan sumándole combinaciones que no estén en él.

Para analizar, los componentes no confundidos de ABC, ABD, ACD y BCD se obtienen restando la SS del componente confundido de la SS de la interacción completa. Nota para quien coteje: en la figura 9-8 algunas etiquetas (L_{{1}}, L_{{2}}) impresas bajo los bloques no coinciden con las que da la ecuación 9-4, aunque el contenido de los bloques es correcto.""",
  left=[form("(ABC)(AB^{2}D^{2}) = A^{2}B^{3}CD^{2} → AC^{2}D", "(ABC)(AB^{2}D^{2})^{2} = A^{3}B^{5}CD^{4} → BC^{2}D^{2}", size=16),
        form("L_{1} = x_{1} + x_{2} + x_{3},   L_{2} = x_{1} + 2x_{2} + 2x_{4}", size=16),
        note("Confundidos: **ABC, AB^{2}D^{2}, AC^{2}D, BC^{2}D^{2}** (4 × 2 = 8 g.l.)", size=15)],
  right=[tab(["(L_{1}, L_{2})", "Bloque"],
             [[f"({k[0]}, {k[1]})", ", ".join(dig(r) for r in _b94[k])] for k in sorted(_b94)], size=12, colw=[0.16, 0.84], pad=0.05)],
  ratio=0.42)

_g7 = [parse("ABC2DG", 7), parse("BCE2F2G", 7), parse("BDEFG", 7)]
_d7 = [W(x) for x in defining(_g7)]
S("El caso general: 3^{k} en 3^{p} bloques",
  f"""El 3^{{k}} se puede confundir en 3^{{p}} bloques de 3^{{k−p}} corridas, con p < k. Se seleccionan p componentes independientes y, como resultado, se confunden automáticamente otros (3^{{p}} − 2p − 1)/2: todas sus interacciones generalizadas. En total quedan confundidos (3^{{p}} − 1)/2 componentes, que son los 3^{{p}} − 1 grados de libertad entre bloques.

Con p = 2 la fórmula da (9 − 4 − 1)/2 = 2 adicionales, los PQ y PQ^{{2}} de la diapositiva anterior. Con p = 3 da (27 − 6 − 1)/2 = 10 adicionales. El libro ilustra con un 3^{{7}} en 27 bloques de 81 corridas (2187 observaciones), eligiendo ABC^{{2}}DG, BCE^{{2}}F^{{2}}G y BDEFG; los otros diez salen de los productos de dos y de tres generadores con exponentes 1 y 2. Es un diseño enorme, que el libro muestra solo para ilustrar el método.""",
  left=[form("Adicionales = (3^{p} − 2p − 1) / 2", "Total confundidos = (3^{p} − 1) / 2", size=19),
        tab(["p", "Bloques", "Se eligen", "Adicionales", "Total"],
            [["1", "3", "1", "0", "1"], ["2", "9", "2", "2", "4"], ["3", "27", "3", "10", "13"]], size=15, first_left=False)],
  right=[txt("**3^{7} en 27 bloques** con ABC^{2}DG, BCE^{2}F^{2}G y BDEFG; los 13 componentes confundidos:", size=14),
         txt(",  ".join(_d7), size=13),
         note("Productos de dos generadores (6) y de tres con exponentes 1 y 2 (4) = 10 adicionales", size=14)],
  ratio=0.45)

# ---------------------------------------------------------------- 6
section(6, "La fracción un tercio 3^{k−1}", "Relación de definición, alias por I e I^{2}, cuadrado latino y un ejemplo")

S("De los bloques a la fracción: cada bloque es un 3^{k−1}",
  """Una réplica completa del 3^{k} puede requerir demasiadas corridas incluso para k moderado, así que interesan las réplicas fraccionadas. La fracción más grande es la un tercio, con 3^{k−1} corridas: el diseño 3^{k−1}.

Para construirlo se elige un componente de interacción de 2 grados de libertad, generalmente de la interacción de orden más alto, y se parte el 3^{k} completo en tres bloques con él. Cada uno de los tres bloques es una fracción 3^{k−1} y puede usarse cualquiera. Si AB^{α₂}C^{α₃}···K^{αₖ} es el componente usado, I = AB^{α₂}C^{α₃}···K^{αₖ} es la relación de definición de la fracción.

La diferencia con el 2^{k−p} está en los alias: cada efecto principal o componente de interacción tiene dos alias, que se obtienen multiplicando el efecto tanto por I como por I^{2}, módulo 3, y normalizando.""",
  left=[num("Elegir un componente de la interacción de **orden más alto**",
            "Partir el 3^{k} en **tres bloques** con L = u (mod 3), u = 0, 1, 2",
            "Quedarse con **uno** de los bloques: es la fracción 3^{k−1}", size=16),
        form("I = AB^{α₂}C^{α₃} ··· K^{αₖ}", size=20)],
  right=[cards(("Alias", "Cada efecto tiene **dos**: efecto × I y efecto × I^{2}, módulo 3 y normalizado"),
               ("Diferencia con el 2^{k−1}", "Allí un alias por palabra; aquí **dos** por palabra, porque I² ≠ I"),
               size=15, cols=1)],
  ratio=0.5)

S("El 3^{3−1}: hay 12 fracciones un tercio distintas",
  """Para una fracción un tercio del 3^{3} se puede usar cualquiera de los cuatro componentes de ABC: ABC, AB^{2}C, ABC^{2} o AB^{2}C^{2}. Cada uno parte el diseño en tres bloques (u = 0, 1, 2), así que hay 4 × 3 = 12 fracciones diferentes, definidas por x_{1} + α_{2}x_{2} + α_{3}x_{3} = u (mod 3), con α = 1 o 2 y u = 0, 1 o 2.

Con I = AB^{2}C^{2}, cada fracción contiene las 9 combinaciones que satisfacen x_{1} + 2x_{2} + 2x_{3} = u (mod 3). Son los tres bloques de la figura 9-7, ahora leídos como tres fracciones (figura 9-9). La de u = 0 es la fracción principal.""",
  left=[tab(["u", "Fracción (9 corridas) con I = AB^{2}C^{2}"],
            [[str(u), ", ".join(dig(r) for r in fraction(3, [(1, 2, 2)], (u,)))] for u in range(3)], size=14, colw=[0.08, 0.92]),
        note("4 componentes × 3 valores de u = **12 fracciones** 3^{3−1} distintas", size=15)],
  right=[img(FIGS["cubo_frac"], h=4.3)],
  ratio=0.55)

_I = (1, 2, 2)
_al33 = [(W(e), aliases(e, [_I])[0]) for e in ((1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 1, 0))]
S("Alias del 3^{3−1} con I = AB^{2}C^{2}: resolución III",
  """Para el efecto A: A·(AB^{2}C^{2}) = A^{2}B^{2}C^{2}, que normalizado es ABC; y A·(AB^{2}C^{2})^{2} = A^{3}B^{4}C^{4} = BC. Así que A es alias de BC y de ABC. Igual para B: B·I = AB^{3}C^{2} = AC^{2} y B·I^{2} = A^{2}B^{5}C^{4} = ABC^{2}. Para C: AB^{2} y AB^{2}C. Y para el componente AB: AC y BC^{2}.

Los cuatro efectos que de verdad se estiman con los 8 grados de libertad son A + BC + ABC, B + AC^{2} + ABC^{2}, C + AB^{2} + AB^{2}C y AB + AC + BC^{2}. Como cada efecto principal es alias de un componente de una interacción de dos factores, es un diseño de resolución III.

El libro es tajante: este diseño solo tendría valor práctico si todas las interacciones fueran pequeñas frente a los efectos principales. Si BC es grande, distorsiona la estimación de A, y la interpretación de AB + AC + BC^{2} se vuelve muy complicada. Es muy difícil ver cómo podría ser útil, a menos que se suponga que todas las interacciones son insignificantes.""",
  left=[tab(["Efecto", "× I", "× I^{2}", "Lo que estima"],
            [[n, W(a[0]), W(a[1]), f"{n} + {W(a[0])} + {W(a[1])}"] for n, a in _al33], size=15, first_left=False),
        form("A · AB^{2}C^{2} = A^{2}B^{2}C^{2} → (·)^{2} = A^{4}B^{4}C^{4} = ABC", "A · (AB^{2}C^{2})^{2} = A^{3}B^{4}C^{4} = BC", size=14)],
  right=[note("Efectos principales alias de **componentes de interacciones de dos factores** → **resolución III**", size=15),
         bul("Solo sirve si **todas** las interacciones son pequeñas", "Si BC es grande, distorsiona a A",
             "AB + AC + BC^{2} es casi imposible de interpretar", size=16)],
  ratio=0.55)

_fr0 = fraction(3, [(1, 2, 2)])
S("El 3^{3−1} es un cuadrado latino 3 × 3",
  """Si en la fracción u = 0 se pone A como renglón y B como columna, y se escribe en cada celda el nivel de C, resulta un cuadrado latino 3 × 3: cada nivel de C aparece exactamente una vez en cada fila y en cada columna. El supuesto de interacciones insignificantes que necesita el 3^{3−1}_{III} es el mismo que necesita el cuadrado latino del capítulo 4.

Los dos diseños surgen por motivos distintos: uno como consecuencia de la réplica fraccionada y el otro de las restricciones sobre la aleatorización (dos variables de bloque). Pero son el mismo arreglo: por la tabla 4-13 solo hay 12 cuadrados latinos 3 × 3, y cada uno corresponde a una de las 12 fracciones 3^{3−1}.""",
  left=[tab(["A \\ B", "B = 0", "B = 1", "B = 2"],
            [[f"A = {a}"] + [next(f"{dig(r)}  (C = {r[2]})" for r in _fr0 if r[0] == a and r[1] == b) for b in range(3)] for a in range(3)],
            size=15, first_left=False),
        note("Cada nivel de C aparece **una vez** por fila y por columna: un cuadrado latino", size=15)],
  right=[bul("Mismo supuesto: **sin interacciones**", "Motivos distintos: **fracción** frente a **restricción de la aleatorización**",
             "12 cuadrados latinos 3 × 3 ↔ 12 fracciones 3^{3−1}", size=16)],
  ratio=0.55)

_e41 = (1, 2, 1, 1)
_bt = betas_from_word(_e41)
_t96 = basic_design(4, 1, [_bt])
S("Construcción por diseño básico: x_{k} = Σ β_{i}x_{i} (ecuación 9-5)",
  f"""Como en el 2^{{k−p}}, la fracción se puede construir sin pasar por los bloques. Se escriben las 3^{{k−1}} corridas del factorial completo en k − 1 factores (el diseño básico) y se introduce el factor k-ésimo igualando sus niveles con el componente apropiado de la interacción de orden más alto: x_{{k}} = β_{{1}}x_{{1}} + β_{{2}}x_{{2}} + ··· + β_{{k−1}}x_{{k−1}} (mod 3), con β_{{i}} = (3 − α_{{k}})α_{{i}} (mod 3). Así se obtiene el diseño de resolución más alta posible.

Ilustración: el 3^{{4−1}}_{{IV}} con I = AB^{{2}}CD. Los exponentes son α_{{1}} = α_{{3}} = α_{{4}} = 1 y α_{{2}} = 2, así que β_{{1}} = (3 − 1)(1) = 2, β_{{2}} = (3 − 1)(2) = 4 = 1 y β_{{3}} = (3 − 1)(1) = 2: x_{{4}} = 2x_{{1}} + x_{{2}} + 2x_{{3}} (mod 3), la ecuación 9-6. Para 000: 0; para 010: 1; para 110: 2 + 1 = 3 = 0. Las 27 corridas son la tabla 9-6.

Los alias de A son A(AB^{{2}}CD) = ABC^{{2}}D^{{2}} y A(AB^{{2}}CD)^{{2}} = BC^{{2}}D^{{2}}. Los cuatro efectos principales quedan separados de los componentes de interacciones de dos factores (resolución IV), pero algunos componentes de interacciones de dos factores son alias entre sí; si una es grande, será muy difícil aislarla.""",
  left=[form("x_{k} = β_{1}x_{1} + ··· + β_{k−1}x_{k−1} (mod 3)", "β_{i} = (3 − α_{k}) α_{i} (mod 3)", size=17),
        form("I = AB^{2}CD:  x_{4} = 2x_{1} + x_{2} + 2x_{3}", size=17),
        tab(["Efecto", "× I", "× I^{2}"], [["A", "ABC^{2}D^{2}", "BC^{2}D^{2}"], ["B", W(aliases((0, 1, 0, 0), [_e41])[0][0]), W(aliases((0, 1, 0, 0), [_e41])[0][1])]],
            size=14, first_left=False)],
  right=[tab(["Tabla 9-6 · 3^{4−1}_{IV}", "", ""],
             [[dig(_t96[i]), dig(_t96[i + 9]), dig(_t96[i + 18])] for i in range(9)], size=13, first_left=False, pad=0.05),
         note("Resolución **IV**: principales libres de interacciones dobles; algunas dobles alias entre sí", size=14)],
  ratio=0.58)

E(5, "un tercio del experimento de las botellas", "Montgomery, problema 9-12 (réplica I del 9-3)",
  ["Vuelve el experimento de acomodar botellas: A tipo de botella, B aparador, C empleado, respuesta el tiempo en minutos. Suponga que **solo hay presupuesto para 9 corridas** en lugar de las 27 de una réplica completa.",
   "Se decide correr una **fracción un tercio 3^{3−1} con I = ABC**: la fracción principal, las nueve combinaciones con x_{1} + x_{2} + x_{3} = 0 (mod 3).",
   "Como se tienen los datos de la réplica I completa, se puede comparar lo que concluye la fracción con lo que concluye el experimento completo, y ver qué pasa cuando una interacción no es despreciable."],
  "Construir la fracción, escribir sus alias, analizarla y **ver qué se pierde** frente a la réplica completa",
  ["Escribir las 9 corridas y comprobar que forman un cuadrado latino", "Obtener los dos alias de cada efecto",
   "Calcular las SS de las cuatro cadenas con la regla L", "Comparar con el ANOVA de la réplica completa"])

S("Ejemplo 5 · La fracción y sus alias",
  f"""Con I = ABC la definición es L = x_{{1}} + x_{{2}} + x_{{3}} = 0 (mod 3). Las nueve corridas son {', '.join(dig(r) for r in fr5)}. Puestas con A en filas y B en columnas, el nivel de C forma un cuadrado latino.

Alias: A·ABC = A^{{2}}BC → (·)^{{2}} = AB^{{2}}C^{{2}}, y A·(ABC)^{{2}} = A^{{3}}B^{{2}}C^{{2}} = B^{{2}}C^{{2}} → BC. Así, la cadena de A es A + BC + AB^{{2}}C^{{2}}. Del mismo modo B + AC + AB^{{2}}C, C + AB + ABC^{{2}} y AB^{{2}} + AC^{{2}} + BC^{{2}}. Cada efecto principal está mezclado con un componente de una interacción de dos factores: resolución III.""",
  left=[tab(["A \\ B", "B = 0", "B = 1", "B = 2"],
            [[f"A = {a}"] + [next(f"{dig(r)}  (C = {r[2]})" for r in fr5 if r[0] == a and r[1] == b) for b in range(3)] for a in range(3)],
            size=15, first_left=False),
        tab(["Corrida", "Botella", "Aparador", "Empleado", "Minutos"],
            [[dig(r), ["plástico", "vidrio 28", "vidrio 38"][r[0]], ["permanente", "pasillo", "refrigerador"][r[1]], str(r[2] + 1), f(y93[r][0], 2)] for r in fr5],
            size=12, first_left=False, pad=0.05)],
  right=[tab(["Efecto", "× I", "× I^{2}", "Cadena"],
             [[n, W(al5[n][0]), W(al5[n][1]), f"{n} + {W(al5[n][1])} + {W(al5[n][0])}"] for n, _ in comp5], size=14, first_left=False),
         note("I = ABC → **resolución III**: cada principal lleva un componente de interacción doble", size=14)],
  ratio=0.5)

S("Ejemplo 5 · Análisis de la fracción y comparación con la réplica completa",
  f"""Con nueve corridas hay 8 grados de libertad: cuatro cadenas de 2 grados de libertad, sin error. Las sumas de cuadrados se calculan con la regla L: para la cadena de A se agrupan las nueve corridas según x_{{1}} (que en esta fracción es lo mismo que agrupar por BC). Resultan SS = {f(ss5['A'], 3)} para A + BC + AB^{{2}}C^{{2}}, {f(ss5['B'], 3)} para B + AC + AB^{{2}}C, {f(ss5['C'], 3)} para C + AB + ABC^{{2}} y {f(ss5['AB^{2}'], 3)} para la cadena de interacciones. La lectura ingenua es: el aparador y el empleado importan, la botella no, igual que en el experimento completo.

Pero mire las medias. En la fracción, el tiempo medio por tipo de botella es {', '.join(f(v, 2) for v in med5['A'][0])}; en la réplica completa es {', '.join(f(v, 2) for v in med5['A'][1])}. La fracción exagera la diferencia entre botellas: SS = {f(ss5['A'], 3)} frente a {f(an4f[0][1], 3)} en el experimento completo. La razón es la interacción BC (aparador × empleado), que en la réplica completa tiene SS = {f(an4f[5][1], 3)} y con las dos réplicas del problema resulta significativa: en la fracción, BC está aliada con A y se cuela en su estimación.

Esa es la advertencia del libro en la práctica: la fracción un tercio solo es confiable si no hay interacciones. Aquí la conclusión cualitativa se salvó, pero la magnitud del efecto de la botella quedó contaminada, y no hay forma de saberlo con las nueve corridas solas.""",
  left=[tab(["Cadena (fracción, 9 corridas)", "SS", "DF"],
            [[f"A + BC + AB^{{2}}C^{{2}}", f(ss5['A'], 3), "2"], ["B + AC + AB^{2}C", f(ss5['B'], 3), "2"],
             ["C + AB + ABC^{2}", f(ss5['C'], 3), "2"], ["AB^{2} + AC^{2} + BC^{2}", f(ss5['AB^{2}'], 3), "2"], ["Total", f(d5.sst(), 3), "8"]],
            size=14, hl=[1, 2]),
        tab(["Réplica completa (27)", "SS", "DF", "P-Value"],
            [[t, f(ss, 3), str(df), pv(p)] for t, ss, df, ms, F, p in an4f] + [["ABC (error)", f(ssABC4, 3), "8", ""]], size=13, hl=[1, 2, 5])],
  right=[tab(["Media por botella", "plástico", "vidrio 28", "vidrio 38"],
             [["Fracción (n = 3)"] + [f(v, 2) for v in med5["A"][0]], ["Completa (n = 9)"] + [f(v, 2) for v in med5["A"][1]]],
             size=14, first_left=True),
         note("BC no es despreciable y está **aliada con A**: la fracción **exagera** el efecto de la botella", size=15),
         note("Sin error ni réplica completa, con las 9 corridas solas no se puede detectar", size=14)],
  ratio=0.55)

# ---------------------------------------------------------------- 7
section(7, "La fracción general 3^{k−p}", "Construcción, alias y el juicio del libro")

S("Fracciones (1/3)^{p}: un noveno, un veintisieteavo…",
  """Para moderar valores grandes de k conviene un fraccionamiento mayor: una fracción (1/3)^{p} del 3^{k}, con 3^{k−p} corridas. Un 3^{k−2} es un noveno, un 3^{k−3} un veintisieteavo.

Construcción: se seleccionan p componentes de interacción y se usan para partir las 3^{k} combinaciones en 3^{p} bloques; cada bloque es una fracción 3^{k−p}. La relación de definición I consta de los p componentes elegidos y de sus (3^{p} − 2p − 1)/2 interacciones generalizadas, la misma cuenta de la sección 5. El alias de cualquier efecto se obtiene multiplicándolo, módulo 3, por cada palabra de I y por su cuadrado: dos alias por palabra.

También se pueden generar las corridas escribiendo primero un 3^{k−p} completo y agregando los p factores adicionales como componentes de interacción de los primeros, igual que en la sección 6.""",
  left=[num("Elegir **p** componentes de interacción", "Partir el 3^{k} en **3^{p} bloques**; un bloque es la fracción",
            "I = los p elegidos + sus **(3^{p} − 2p − 1)/2** interacciones generalizadas",
            "Alias: efecto × cada palabra de I y × su cuadrado", size=16)],
  right=[tab(["Fracción", "Corridas", "Palabras de I", "Alias por efecto"],
             [["3^{k−1}", "3^{k−1}", "1", "2"], ["3^{k−2}", "3^{k−2}", "4", "8"], ["3^{k−3}", "3^{k−3}", "13", "26"]],
             size=15, first_left=False),
         note("Alias por efecto = 2 × número de palabras: la estructura se complica muy rápido", size=14)],
  ratio=0.5)

_g42 = [parse("AB2C", 4), parse("BCD", 4)]
_d42 = defining(_g42)
_t97 = []
for _a, _b in runs3(2):
    _c = (2 * _a + _b) % 3
    _t97.append((_a, _b, _c, (2 * _b + 2 * _c) % 3))
S("Ejemplo: el 3^{4−2}_{III} con AB^{2}C y BCD (tablas 9-7 y 9-8)",
  f"""Una fracción un noveno del 3^{{4}}: nueve corridas para cuatro factores. Se eligen AB^{{2}}C y BCD. Sus interacciones generalizadas son (AB^{{2}}C)(BCD) = AB^{{3}}C^{{2}}D = AC^{{2}}D y (AB^{{2}}C)(BCD)^{{2}} = AB^{{4}}C^{{3}}D^{{2}} = ABD^{{2}}. La relación de definición completa es I = AB^{{2}}C = BCD = AC^{{2}}D = ABD^{{2}}, y el diseño es de resolución III.

Las nueve corridas se obtienen con un 3^{{2}} completo en A y B y los factores adicionales x_{{3}} = 2x_{{1}} + x_{{2}} y x_{{4}} = 2x_{{2}} + 2x_{{3}} (mod 3): es la tabla 9-7. Equivale a partir el 3^{{4}} en nueve bloques con AB^{{2}}C y BCD y tomar el bloque principal.

Con 8 grados de libertad solo se estiman los cuatro efectos principales, cada uno con ocho alias (tabla 9-8): cuatro por las palabras de I y cuatro por sus cuadrados. Por ejemplo, A es alias de ABC^{{2}}, ABCD, ACD^{{2}}, AB^{{2}}D, BC^{{2}}, AB^{{2}}C^{{2}}D^{{2}}, CD^{{2}} y BD^{{2}}. El diseño solo es útil en ausencia de interacciones. Con A en renglones y B en columnas, la tabla 9-7 es además un cuadrado grecolatino.""",
  left=[form("I = AB^{2}C = BCD = AC^{2}D = ABD^{2}", size=18),
        form("x_{3} = 2x_{1} + x_{2},   x_{4} = 2x_{2} + 2x_{3}  (mod 3)", size=16),
        tab(["Tabla 9-7", "", ""], [[dig(_t97[i]), dig(_t97[i + 3]), dig(_t97[i + 6])] for i in range(3)], size=14, first_left=False)],
  right=[tab(["Efecto", "Alias por I (× cada palabra)", "Alias por I^{2}"],
             [[W(e), ", ".join(W(a[0]) for a in aliases(e, _d42)), ", ".join(W(a[1]) for a in aliases(e, _d42))]
              for e in ((1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1))], size=12, colw=[0.1, 0.45, 0.45], pad=0.06),
         note("Resolución III, 8 alias por efecto. Es también un **cuadrado grecolatino**", size=14)],
  ratio=0.42)

S("El juicio del libro sobre los 3^{k−p}: «soluciones que causan problemas»",
  """Montgomery cierra la sección con una valoración poco favorable. Si k es moderadamente grande, por ejemplo 4 o 5, el tamaño del 3^{k} lleva a considerar fracciones bastante pequeñas, y esas fracciones tienen relaciones de alias que incluyen alias parciales de componentes de interacción con dos grados de libertad. La interpretación resulta difícil, si no imposible, a menos que las interacciones sean insignificantes.

Además, no hay esquemas de aumento simples, como el doblez del 2^{k−p}, que permitan combinar dos o más fracciones para aislar las interacciones significativas. Y cuando lo que se busca es curvatura, hay alternativas más eficientes en el capítulo 11.

Conclusión textual: los diseños factoriales fraccionados 3^{k−p} son soluciones que causan problemas; no son, en general, buenos diseños. Para diseños concretos con 4 ≤ k ≤ 10 el libro remite al catálogo de Connor y Zelen (National Bureau of Standards).""",
  left=[cards(("Alias parciales", "Componentes de 2 g.l. mezclados entre sí; interpretación **difícil o imposible** si hay interacciones"),
              ("Sin doblez", "No existe un esquema simple para **combinar fracciones** y aislar interacciones, como en el 2^{k−p}"),
              ("Hay mejores opciones", "Para curvatura: **superficie de respuesta** (cap. 11); para factores cualitativos: **niveles mixtos** (sección 8)"),
              size=14, cols=1)],
  right=[note("«Los diseños 3^{k−p} son soluciones que causan problemas; no son, en general, buenos diseños» (Montgomery, pág. 383)", size=16),
         tab(["", "2^{k−p}", "3^{k−p}"],
             [["Alias por palabra", "1", "2"], ["Resolución", "Clara y tabulada", "Difícil de aprovechar"],
              ["Aumentar el diseño", "Doblez, fracción alterna", "No hay esquema simple"], ["Catálogo", "Tabla XII", "Connor y Zelen"]],
             size=14, colw=[0.34, 0.33, 0.33])],
  ratio=0.5)

# ---------------------------------------------------------------- 8
section(8, "Niveles mixtos", "Factores de tres y cuatro niveles dentro de un 2^{k}")

S("La postura del libro: dos niveles como piedra angular",
  """El sistema de dos niveles de los capítulos 6, 7 y 8 es de particular utilidad; el de tres niveles es de utilidad mucho menor, porque los diseños son grandes incluso con pocos factores y la mayoría de las fracciones pequeñas tienen alias complejos. Montgomery lo dice sin rodeos: los factoriales y fraccionados de dos niveles deben ser la piedra angular de la experimentación industrial.

Sin embargo hay situaciones en que es necesario incluir un factor con más de dos niveles. Suele ocurrir cuando se mezclan factores cuantitativos y cualitativos y el cualitativo tiene, por ejemplo, tres niveles. Si todos los factores son cuantitativos, lo indicado es un diseño de dos niveles con puntos centrales.

La sección 9-4 muestra cómo incorporar factores de tres y de cuatro niveles dentro de un 2^{k}: se aprovecha la tabla de signos del 2^{k}, que ya se sabe analizar, y se sacrifican algunas columnas.""",
  left=[bul("Dos niveles: **piedra angular** de la experimentación industrial",
            "Tres niveles: diseños grandes y alias complejos",
            "Todos cuantitativos → **2^{k} con puntos centrales**",
            "Un factor **cualitativo** con 3 o 4 niveles → **niveles mixtos** sobre la tabla del 2^{k}", size=16)],
  right=[cards(("Dos y tres niveles (9-4.1)", "Dos columnas del 2^{k} **se colapsan** en un factor de tres niveles, repitiendo el nivel intermedio"),
               ("Dos y cuatro niveles (9-4.2)", "Dos columnas del 2^{k} **representan** un factor de cuatro niveles: sus 4 combinaciones de signos son los 4 niveles"),
               size=15, cols=1)],
  ratio=0.5)

S("Factores con dos y tres niveles: colapsar dos columnas en una (tabla 9-9)",
  """La idea es tomar dos columnas de dos niveles, B y C, de la tabla de signos del 2^{k} y combinarlas para formar un factor X de tres niveles: (−, −) es el nivel bajo x_{1}, (+, −) y (−, +) son los dos el nivel intermedio x_{2}, y (+, +) es el nivel alto x_{3}. El nivel intermedio queda repetido.

Ejemplo del libro: A con dos niveles y X con tres en un 2^{3} de ocho corridas (tabla 9-10). La fila superior de la tabla indica el efecto real que estima cada columna. X tiene 2 grados de libertad; si es cuantitativo se parte en X_{L} y X_{Q}.

X_{L} es la suma de las estimaciones de las columnas B y C, y solo usa las corridas con X bajo o alto (1, 2, 7 y 8). A × X_{L} es la suma de las columnas AB y AC. X_{Q} es la columna BC y A × X_{Q} la columna ABC. La columna BC no puede usarse para otro factor porque contiene el efecto cuadrático de X.""",
  left=[tab(["B", "C", "X"], [["−", "−", "x_{1} (bajo)"], ["+", "−", "x_{2} (intermedio)"], ["−", "+", "x_{2} (intermedio)"], ["+", "+", "x_{3} (alto)"]],
            size=16, first_left=False),
        note("El nivel intermedio queda **repetido**: de ahí salen réplicas para el error", size=15)],
  right=[tab(["Corrida", "A [A]", "B [X_{L}]", "C [X_{L}]", "AB [A×X_{L}]", "AC [A×X_{L}]", "BC [X_{Q}]", "ABC [A×X_{Q}]", "A real", "X real"],
             [[str(i + 1), sg(r["A"]), sg(r["B"]), sg(r["C"]), sg(r["A"] * r["B"]), sg(r["A"] * r["C"]), sg(r["B"] * r["C"]), sg(r["A"] * r["B"] * r["C"]),
               "Alto" if r["A"] > 0 else "Bajo", ["Bajo", "Intermedio", "Alto"][X6[i]]] for i, r in enumerate(r6)],
             size=12, first_left=False, pad=0.05),
         txt("Tabla 9-10: entre corchetes, el efecto real que estima cada columna", size=12)],
  ratio=0.36)

S("El análisis: X_{L}, X_{Q} y el error puro de las corridas repetidas (tabla 9-11)",
  """Las corridas 3 y 5 son réplicas: las dos tienen A bajo y X intermedio. Con ellas se estima el error con 1 grado de libertad. Las corridas 4 y 6 también son réplicas (A alto, X intermedio) y dan otro grado de libertad. El promedio de las dos varianzas es el cuadrado medio del error con 2 grados de libertad.

La tabla ANOVA completa tiene A con 1 grado de libertad, X con 2 (X_{L} + X_{Q}), AX con 2 (A × X_{L} + A × X_{Q}) y error con 2; total 7. Nota para quien coteje: en la tabla 9-11 el cuadrado medio de X aparece impreso como MS_{B}; es MS_{X}.

Si se está dispuesto a suponer que las interacciones son insignificantes, este diseño se convierte en una fracción de resolución III con hasta cuatro factores de dos niveles y uno de tres: los de dos niveles se asocian a las columnas A, AB, AC y ABC. El mismo procedimiento sirve en diseños de 16, 32 y 64 corridas: con 16 corridas hay fracciones de resolución V con 2 factores de dos niveles y 2 o 3 de tres niveles, o con 3 de dos niveles y 1 de tres; con 4 de dos niveles y 1 de tres el diseño baja a resolución III.""",
  left=[tab(["SV", "SS", "DF", "MS"],
            [["A", "SS_{A}", "1", "MS_{A}"], ["X (X_{L} + X_{Q})", "SS_{X}", "2", "MS_{X}"], ["AX (A×X_{L} + A×X_{Q})", "SS_{AX}", "2", "MS_{AX}"],
             ["Error (corridas 3 y 5; 4 y 6)", "SS_{E}", "2", "MS_{E}"], ["Total", "SS_{T}", "7", ""]], size=15, colw=[0.45, 0.2, 0.12, 0.23])],
  right=[cards(("Error puro", "Pares (3, 5) y (4, 6): dos varianzas con 1 g.l. cada una → MS_{E} con **2 g.l.**"),
               ("Más factores de dos niveles", "Si no hay interacciones: columnas A, AB, AC, ABC → hasta **4 de dos niveles + 1 de tres**, resolución III. **BC no**: lleva X_{Q}"),
               ("16 corridas", "Resolución V con 2 de dos niveles y 2 o 3 de tres; o 3 de dos y 1 de tres"),
               size=14, cols=1)],
  ratio=0.5)

E(6, "un factor de dos niveles y uno de tres en 8 corridas", "ejemplo construido para la clase, con datos inventados",
  ["Se quiere medir la **adherencia** (N) de un recubrimiento. Influyen el **tipo de imprimante** (A, dos tipos: factor cualitativo de dos niveles) y la **temperatura de curado** (X, tres niveles: 60, 80 y 100 °C, cuantitativo).",
   "Solo se pueden hacer **8 corridas**. Un 2 × 3 completo tiene 6 combinaciones; con 8 corridas se usa la tabla 9-10: las columnas B y C de un 2^{3} se colapsan en X y el nivel intermedio queda repetido.",
   "Los datos son inventados para que las cuentas sean cortas: corridas 1 a 8 con adherencia 10, 14, 15, 19, 16, 18, 17 y 23."],
  "Ver cómo las columnas del 2^{3} se **reagrupan** en los efectos reales A, X_{L}, X_{Q} y sus interacciones, y de dónde sale el error",
  ["Calcular los efectos de las siete columnas del 2^{3}", "Reagruparlos: X_{L} = B + C, X_{Q} = BC, etc.",
   "Obtener el error puro con las corridas repetidas", "Armar la tabla ANOVA de la tabla 9-11"])

_ssc = {t: ef6[t][2] for t in ef6}
S("Ejemplo 6 · De las siete columnas a los cuatro efectos reales",
  f"""Primero se calculan los efectos de las siete columnas del 2^{{3}} como si fuera un factorial de dos niveles. Después se reagrupan según la fila superior de la tabla 9-10.

X_{{L}}: las columnas B y C estiman cada una el efecto lineal de X, y su suma, {f(ef6['B'][1])} + {f(ef6['C'][1])} = {f(ef6['B'][1] + ef6['C'][1])}, es la diferencia entre la adherencia media con X alto (corridas 7 y 8: {f((y6[6] + y6[7]) / 2, 1)}) y con X bajo (corridas 1 y 2: {f((y6[0] + y6[1]) / 2, 1)}). Su suma de cuadrados es SS_{{B}} + SS_{{C}} = {f(_ssc['B'])} + {f(_ssc['C'])} = {f(_ssc['B'] + _ssc['C'])}. X_{{Q}} es la columna BC: efecto {f(ef6['BC'][1])}, SS = {f(_ssc['BC'])}; compara el nivel intermedio con el promedio de los extremos. SS_{{X}} = {f(_ssc['B'] + _ssc['C'] + _ssc['BC'])}, con 2 grados de libertad, es lo mismo que se obtiene calculando directamente la SS entre los tres niveles de X.

A × X_{{L}} es la suma de AB y AC (SS = {f(_ssc['AB'] + _ssc['AC'])}) y A × X_{{Q}} es ABC (SS = {f(_ssc['ABC'])}); juntas, SS_{{AX}} = {f(ssAX6)}. El error puro sale de los pares repetidos: (15, 16) y (19, 18) dan SS_{{E}} = 0.5 + 0.5 = {f(sse6, 1)} con 2 grados de libertad. Todo cuadra: {f(ssA6)} + {f(ssX6)} + {f(ssAX6)} + {f(sse6, 1)} = {f(d6.sst())} = SS_{{T}}.""",
  left=[tab(["Columna", "Efecto", "SS", "Estima"],
            [[t, f(ef6[t][1]), f(_ssc[t]), lab] for t, lab in (("A", "A"), ("B", "X_{L}"), ("C", "X_{L}"), ("AB", "A × X_{L}"), ("AC", "A × X_{L}"), ("BC", "X_{Q}"), ("ABC", "A × X_{Q}"))],
            size=14, first_left=False),
        note(f"X_{{L}} = B + C = {f(ef6['B'][1] + ef6['C'][1])}: media con X alto ({f((y6[6] + y6[7]) / 2, 1)}) − media con X bajo ({f((y6[0] + y6[1]) / 2, 1)})", size=14)],
  right=[tab(["SV", "SS", "DF", "MS", "F_{0}"],
             [["A", f(ssA6), "1", f(ssA6), f(ssA6 / (sse6 / dfe6))], [f"X  (X_{{L}} = {f(_ssc['B'] + _ssc['C'])} + X_{{Q}} = {f(_ssc['BC'])})", f(ssX6), "2", f(ssX6 / 2), f(ssX6 / 2 / (sse6 / dfe6))],
              [f"AX  ({f(_ssc['AB'] + _ssc['AC'])} + {f(_ssc['ABC'])})", f(ssAX6), "2", f(ssAX6 / 2), f(ssAX6 / 2 / (sse6 / dfe6))],
              ["Error (3 y 5; 4 y 6)", f(sse6, 1), "2", f(sse6 / dfe6, 2), ""], ["Total", f(d6.sst()), "7", "", ""]], size=14),
         note(f"F_{{0.05, 1, 2}} = {f(f_ppf(0.05, 1, 2))}, F_{{0.05, 2, 2}} = {f(f_ppf(0.05, 2, 2))}: con 2 g.l. de error la prueba es muy poco potente; el diseño es ilustrativo", size=13)],
  ratio=0.5)

S("Factores con dos y cuatro niveles: dos columnas representan los cuatro niveles (tabla 9-12)",
  """Incorporar un factor con cuatro niveles en un 2^{k} es muy sencillo. Se toman dos columnas de la tabla de signos, P y Q, y sus cuatro combinaciones de signos se hacen corresponder con los cuatro niveles del factor A: (−, −) → a_{1}, (+, −) → a_{2}, (−, +) → a_{3}, (+, +) → a_{4}. Las columnas P, Q y PQ son mutuamente ortogonales y, juntas, representan el efecto de A con 3 grados de libertad.

Ejemplo del libro: un factor X de cuatro niveles y dos factores C y D de dos niveles en 16 corridas (tabla 9-13). Se parte de la tabla de signos del 2^{4} y las columnas A y B forman X. Las sumas de cuadrados de las 15 columnas se calculan exactamente igual que en un 2^{4}, y después se agrupan: SS_{X} = SS_{A} + SS_{B} + SS_{AB} con 3 grados de libertad; SS_{XC} = SS_{AC} + SS_{BC} + SS_{ABC}; SS_{XD} = SS_{AD} + SS_{BD} + SS_{ABD}; SS_{XCD} = SS_{ACD} + SS_{BCD} + SS_{ABCD}; y SS_{C}, SS_{D} y SS_{CD} quedan como están. A este diseño se le llama 4 × 2^{2}.

Si se ignoran las interacciones de dos factores, pueden asociarse factores adicionales de dos niveles a las columnas de interacción de dos, tres y cuatro factores, excepto AB, que lleva parte del efecto de X. El libro dice «hasta nueve»; descontando A, B, AB, C y D de las 15 columnas quedan diez disponibles.""",
  left=[tab(["P", "Q", "Factor de 4 niveles"], [["−", "−", "a_{1}"], ["+", "−", "a_{2}"], ["−", "+", "a_{3}"], ["+", "+", "a_{4}"]], size=16, first_left=False),
        note("P, Q y PQ: tres columnas ortogonales = **3 g.l.** del factor de cuatro niveles", size=15)],
  right=[tab(["Efecto real (4 × 2^{2}, 16 corridas)", "Columnas del 2^{4} que se suman", "DF"],
             [["X", "A + B + AB", "3"], ["C", "C", "1"], ["D", "D", "1"], ["CD", "CD", "1"], ["XC", "AC + BC + ABC", "3"],
              ["XD", "AD + BD + ABD", "3"], ["XCD", "ACD + BCD + ABCD", "3"], ["Total", "15 columnas", "15"]], size=14, colw=[0.38, 0.47, 0.15]),
         note("Sin interacciones dobles: las columnas libres (**excepto AB**) admiten más factores de dos niveles", size=14)],
  ratio=0.4)

# ---------------------------------------------------------------- 9
section(9, "Cierre", "Lo que hay que recordar")

S("Lo que hay que recordar",
  """Siete ideas resumen el capítulo. El 3^{k} agrega el nivel intermedio y permite modelar curvatura, pero crece muy rápido y el libro lo reserva para factores cualitativos con tres niveles. Cada efecto principal tiene 2 grados de libertad y una interacción de h factores tiene 2^{h}, que se parten en 2^{h−1} componentes de 2 grados de libertad. Esos componentes (AB, AB^{2}, W, X, Y, Z) no se interpretan, pero son la herramienta con que se construyen bloques y fracciones, mediante la regla L = Σ α_{i}x_{i} (mod 3). Con factores cuantitativos la partición que sí se interpreta es la lineal y cuadrática. Confundir en 3^{p} bloques cuesta (3^{p} − 1)/2 componentes; una fracción 3^{k−p} es un bloque de ese esquema y cada efecto tiene dos alias por palabra. Y la recomendación final: preferir dos niveles con puntos centrales, y cuando haga falta un factor de tres o cuatro niveles, incorporarlo dentro de un 2^{k}.""",
  body=[tab(["Idea", "En una frase"],
            [["Tercer nivel", "Permite modelar **curvatura**; crece como 27, 81, 243. Reservarlo para factores **cualitativos** con tres niveles"],
             ["Grados de libertad", "Efecto principal 2; interacción de h factores **2^{h}** = 2^{h−1} componentes de 2 g.l."],
             ["Componentes", "AB, AB^{2}, W, X, Y, Z: **sin significado físico**; la regla **L = Σ α_{i}x_{i} (mod 3)** los calcula y los confunde"],
             ["Lineal y cuadrático", "La partición que **sí se interpreta**, solo con factores cuantitativos: (−1, 0, 1) y (1, −2, 1)"],
             ["Bloques", "3^{p} bloques cuestan **(3^{p} − 1)/2** componentes: los elegidos y sus interacciones generalizadas PQ, PQ^{2}"],
             ["Fracciones", "Un bloque del esquema de confusión; **dos alias por palabra** (× I y × I^{2}); sin doblez: «causan problemas»"],
             ["Niveles mixtos", "Colapsar dos columnas del 2^{k} (tres niveles) o usar dos columnas como cuatro niveles; se analiza con la tabla del 2^{k}"]],
            size=14, colw=[0.2, 0.8])])

S("Errores frecuentes",
  """Los errores más comunes al trabajar con 3^{k}: usarlo para factores cuantitativos solo por ver curvatura, cuando un 2^{k} con puntos centrales lo detecta con menos corridas; interpretar los componentes AB y AB^{2} o W, X, Y, Z como si tuvieran significado físico, o confundirlos con los componentes lineal y cuadrático; olvidar normalizar los exponentes (A^{2}B no es una palabra válida: es AB^{2}); olvidar el segundo alias (× I^{2}) en las fracciones; confundir con los bloques un componente de un efecto principal o de una interacción de dos factores, cuando hay disponibles los de la interacción de orden más alto; y usar un 3^{k−1} de resolución III cuando se sospecha de interacciones, porque no hay doblez que lo rescate.""",
  body=[cards(("Curvatura", "Usar un 3^{k} con factores cuantitativos en vez de **2^{k} + puntos centrales → central compuesto**"),
              ("Componentes", "Darles **significado físico** a AB, AB^{2}, W, X, Y, Z, o mezclarlos con L × L, L × Q…"),
              ("Exponentes", "No normalizar: A^{2}B debe escribirse **AB^{2}**; la primera letra siempre con exponente 1"),
              ("Alias", "Olvidar el alias por **I^{2}**: en el 3^{k−p} cada palabra da **dos** alias"),
              ("Bloques", "Confundir un componente de un efecto principal o de una doble, pudiendo usar la interacción de **orden más alto**"),
              ("Fracciones III", "Usar un 3^{k−1}_{III} sospechando interacciones: **no hay doblez** que lo arregle"),
              size=14, cols=3)])

S("Referencias",
  """Capítulo 9 de Montgomery, en la segunda edición en español: diseños 3^{k} (9-1), confusión (9-2), fracciones 3^{k−p} (9-3) y niveles mixtos (9-4), páginas 363 a 391. Los ejemplos numéricos son el 9-1 (jarabe), el 9-2 (3^{2} en bloques) y los problemas 9-3, 9-6, 9-9 y 9-12; el ejemplo 6 es propio. Para los componentes de la interacción y la tabla de cuadrados latinos se citan además los capítulos 4 y 5, y para el diseño central compuesto el capítulo 6 y el 11.""",
  body=[bul("Montgomery, D. C. *Diseño y análisis de experimentos*, 2.ª ed. en español, Limusa-Wiley. Capítulo 9, págs. 363–391; cap. 4 (cuadrados latinos, tabla 4-13), cap. 5 (ejemplo 5-5), cap. 6 (puntos centrales), cap. 11 (superficies de respuesta).",
            "Cochran, W. G. y Cox, G. M. *Experimental Designs*. Procedimiento para los componentes W, X, Y, Z.",
            "Connor, W. S. y Zelen, M. *Fractional Factorial Experiment Designs for Factors at Three Levels*, National Bureau of Standards. Catálogo de diseños 3^{k−p}, 4 ≤ k ≤ 10.",
            "Addelman, S. Diseños con niveles mixtos a partir de 2^{k} (citado en la sección 9-4).",
            "Datos: ejemplo 9-1 (tabla 9-1), ejemplo 9-2, problemas 9-3 (réplica I), 9-6, 9-9 y 9-12. Ejemplo 6: datos inventados para la clase.", size=15)])

SLIDES.append({"kind": "closing", "title": "¿Preguntas?",
               "sub": "Diseños factoriales 3^{k} y con niveles mixtos · Tema 6, segunda parte",
               "meta": "Juan Esteban Rodríguez Ochoa · Sebastián Zapata Henao", "sec": "", "explica": ""})
