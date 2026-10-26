"""Contenido único de la exposición del tema 6 (factoriales fraccionados).

Cada diapositiva es un dict con título, bloques y un texto explicativo ("explica").
render_pptx.py lo convierte en la presentación y render_guia.py en la guía de estudio.
Marcado en los textos: ^{..} superíndice, _{..} subíndice, **..** negrita.
"""
import random
from doe import (basic, add_factor, effect, fit, lenth, t_ppf, f_ppf,
                 anderson_darling, normal_scores)

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


# ================================================================ cálculos
# Ejemplo 1: 2^(4-1) IV, índice de filtración (Montgomery, ej. 8-1)
r1 = basic(3); add_factor(r1, "D", "ABC")
y1 = [45, 100, 45, 65, 75, 60, 80, 96]
trat1 = ["(1)", "ad", "bd", "ab", "cd", "ac", "bc", "abcd"]
ef1 = {w: effect(r1, y1, w) for w in ["A", "B", "C", "D", "AB", "AC", "AD"]}
alias1 = {"A": "A + BCD", "B": "B + ACD", "C": "C + ABD", "D": "D + ABC",
          "AB": "AB + CD", "AC": "AC + BD", "AD": "AD + BC"}
m1 = fit(r1, y1, ["A", "C", "D", "AC", "AD"])
press1 = sum((e / (1 - 6 / 8)) ** 2 for e in m1["res"])
r2pred1 = 1 - press1 / m1["sst"]
# fracción alterna (ej. 8-3)
r1b = basic(3); add_factor(r1b, "D", "ABC", sign=-1)
y1b = [43, 71, 48, 104, 68, 86, 70, 65]
ef1b = {w: effect(r1b, y1b, w) for w in ["A", "B", "C", "D", "AB", "AC", "AD"]}

# Ejemplo 2: 2^(5-1) V, rendimiento de un circuito integrado (ej. 8-2)
r2 = basic(4); add_factor(r2, "E", "ABCD")
y2 = [8, 9, 34, 52, 16, 22, 45, 60, 6, 10, 30, 50, 15, 21, 44, 63]
w2 = ["A", "B", "C", "D", "E", "AB", "AC", "AD", "AE", "BC", "BD", "BE", "CD", "CE", "DE"]
ef2 = {w: effect(r2, y2, w) for w in w2}
m2 = fit(r2, y2, ["A", "B", "C", "AB"])
pse2 = lenth([ef2[w][1] for w in w2]); me2 = t_ppf(0.05, 15 / 3) * pse2
ad2 = anderson_darling(m2["res"])

# Ejemplo 3: 2^(6-2) IV, contracción en moldeo por inyección (ej. 8-4)
r3 = basic(4); add_factor(r3, "E", "ABC"); add_factor(r3, "F", "BCD")
y3 = [6, 10, 32, 60, 4, 15, 26, 60, 8, 12, 34, 60, 16, 5, 37, 52]
w3 = ["A", "B", "C", "D", "E", "F", "AB", "AC", "AD", "AE", "AF", "BD", "BF", "ABD", "ABF"]
lab3 = {"AB": "AB + CE", "AC": "AC + BE", "AD": "AD + EF", "AE": "AE + BC + DF", "AF": "AF + DE",
        "BD": "BD + CF", "BF": "BF + CD", "ABD": "ABD (+ alias)", "ABF": "ABF (+ alias)"}
ef3 = {w: effect(r3, y3, w) for w in w3}
m3 = fit(r3, y3, ["A", "B", "AB"])
ab3 = {(a, b): sum(v for v, row in zip(y3, r3) if row["A"] == a and row["B"] == b) / 4
       for a in (-1, 1) for b in (-1, 1)}
ad3 = anderson_darling(m3["res"])

# Ejemplo 5: 2^(7-4) III y doblez completo, tiempo de enfoque del ojo (ej. 8-7)
r4 = basic(3)
for n_, w_ in [("D", "AB"), ("E", "AC"), ("F", "BC"), ("G", "ABC")]:
    add_factor(r4, n_, w_)
y4 = [85.5, 75.1, 93.2, 145.4, 83.7, 77.6, 95.0, 141.8]
r4b = [{k: -v for k, v in row.items()} for row in r4]
y4b = [91.3, 136.7, 82.4, 73.4, 94.1, 143.8, 87.3, 71.9]
ef4 = {w: effect(r4, y4, w)[1] for w in "ABCDEFG"}
ef4b = {w: effect(r4b, y4b, w)[1] for w in "ABCDEFG"}
alias4 = {"A": "BD + CE + FG", "B": "AD + CF + EG", "C": "AE + BF + DG", "D": "AB + CG + EF",
          "E": "AC + BG + DF", "F": "BC + AG + DE", "G": "CD + BE + AF"}

random.seed(6)
orden = list(range(1, 9)); random.shuffle(orden)

# ================================================================ diapositivas
SLIDES.append({"kind": "title", "title": "Diseños factoriales fraccionados 2^{k−p}",
               "sub": "Tema 6 · Diseño de Experimentos Avanzados (3008475)",
               "meta": "Juan Esteban Rodríguez Ochoa · Sebastián Zapata Henao\n"
                       "Universidad Nacional de Colombia · 31 de octubre de 2026",
               "sec": "", "explica": ""})

S("Ruta de la clase",
  """La clase sigue el orden del capítulo 8 de Montgomery. Primero el propósito del diseño, su vocabulario y el repaso de la tabla del 2^{k}. Después la resolución, que es la idea que organiza todo lo demás. Luego las fracciones de menor a mayor complejidad: la fracción un medio con sus ejemplos, cómo se encadenan las fracciones en secuencia, la fracción un cuarto y el caso general 2^{k−p} con su análisis, su proyección y su separación en bloques. Al final, los diseños de resolución III con el doblez y los de Plackett-Burman, y los de resolución IV y V. Cierra con las ideas clave.""",
  body=[cards(("1 · Propósito y vocabulario", "Para qué sirven, notación y la tabla del 2^{k}"),
              ("2 · Resolución", "Qué tanto se mezclan los efectos"),
              ("3 · Fracción un medio", "Alias, construcción, proyección y ejemplos"),
              ("4 · Secuencias", "Correr una fracción, analizar y decidir"),
              ("5 · Fracción un cuarto", "Dos generadores, alternas, proyección y ejemplo"),
              ("6 · Caso general 2^{k−p}", "Elección, análisis, supuestos, proyección y bloques"),
              ("7 · Resolución III", "Saturados, doblez y Plackett-Burman"),
              ("8 · Resolución IV y V", "Diseños mínimos, doblez y fracciones irregulares"),
              ("9 · Cierre", "Ideas clave y errores frecuentes"), size=15, cols=5)])

section(1, "Propósito y vocabulario", "Para qué sirven, cómo se nombran y la tabla del 2^{k}")

S("¿Qué problema resuelven los factoriales fraccionados?",
  """En un factorial 2^{k} completo el número de corridas se duplica con cada factor que se agrega: con 7 factores ya son 128 corridas y con 10 son 1024. En las primeras etapas de una investigación suele haber muchos factores candidatos y pocos recursos, de modo que el factorial completo deja de ser viable.

El factorial fraccionado corre solo una parte del factorial completo, elegida de forma que todavía se puedan estimar los efectos principales y las interacciones de orden bajo. El precio que se paga es que algunos efectos quedan mezclados entre sí (alias). Por eso su uso típico es el tamizado (cribado o screening): identificar, entre muchos factores, los pocos que realmente afectan la respuesta.""",
  left=[bul("En un 2^{k} completo las corridas **se duplican** con cada factor nuevo",
            "Con muchos factores el experimento completo es inviable en tiempo y costo",
            "El fraccionado corre **solo una parte** del 2^{k}, elegida con criterio",
            "Uso principal: **tamizado** de factores en etapas tempranas"),
        note("El costo: algunos efectos quedan mezclados entre sí (**alias**)")],
  right=[bars([f"k = {k}" for k in range(3, 11)], [2 ** k for k in range(3, 11)],
              "Corridas del factorial completo", h=4.6, fmt="0")], ratio=0.5)

_rows = []
for k in range(4, 9):
    tot = 2 ** k - 1
    two = k * (k - 1) // 2
    _rows.append([str(k), str(2 ** k), str(k), str(two), str(tot - k - two),
                  f"{100 * (tot - k - two) / tot:.0f} %"])
S("¿En qué se gastan las corridas de un 2^{k} completo?",
  """Un factorial completo con N corridas tiene N − 1 grados de libertad para estimar efectos. La tabla muestra cómo se reparten. En un 2^{6} hay 63 grados de libertad, pero solo 6 corresponden a efectos principales y 15 a interacciones de dos factores; los 42 restantes se gastan en interacciones de tres o más factores, que con frecuencia se pueden suponer despreciables.

Si se acepta que esas interacciones de orden alto son despreciables, la información sobre efectos principales e interacciones dobles se puede obtener con una fracción del experimento.""",
  body=[tab(["Factores k", "Corridas 2^{k}", "Efectos principales", "Interacciones de 2 factores",
             "Interacciones de 3 o más", "% en orden alto"], _rows, size=16, hl=[2], first_left=False),
        note("En un 2^{6}, **42 de 63** grados de libertad estiman interacciones de tres o más factores. "
             "Si se pueden suponer despreciables, esa es la información que el fraccionado sacrifica.")])

S("Tres ideas que justifican correr solo una fracción",
  """Escasez de efectos: cuando hay muchas variables, el sistema suele estar dominado por unos pocos efectos principales e interacciones de orden bajo.

Proyección: si algunos factores resultan inactivos, el fraccionado se convierte en un diseño más fuerte (incluso un factorial completo, a veces con réplicas) en los factores que sí importan.

Experimentación secuencial: no hay que correr todo de una vez. Se corre una fracción, se analiza y, si quedan dudas, se agrega otra fracción; juntas forman un diseño mayor que resuelve las ambigüedades.""",
  body=[cards(("Escasez de efectos",
               "De muchos factores, pocos son activos. Dominan los efectos principales y las interacciones de orden bajo."),
              ("Proyección",
               "Al descartar factores inactivos, la fracción se proyecta en un diseño más fuerte en los que quedan, a menudo un factorial completo."),
              ("Experimentación secuencial",
               "Se corre una fracción, se analiza y se decide. Dos fracciones se combinan para resolver dudas."),
              size=22)])

S("¿Cuándo usar un factorial fraccionado?",
  """Conviene cuando hay muchos factores (Montgomery señala que incluso con cuatro suele preferirse empezar con la fracción 2^{4−1}), cuando cada corrida es costosa o lenta, cuando se está en una etapa exploratoria y cuando es razonable suponer que las interacciones de tres o más factores son despreciables.

No conviene cuando hay pocos factores y el factorial completo es barato, cuando se sabe que hay interacciones importantes entre muchos factores, o cuando se necesita un modelo detallado para optimizar: para eso están los factoriales completos y las superficies de respuesta, normalmente en una etapa posterior. Las conclusiones de un fraccionado son tentativas y deben confirmarse.""",
  left=[txt("**Úselo cuando…**", size=20),
        bul("Hay **muchos factores** candidatos",
            "Cada corrida es **costosa o lenta**",
            "La etapa es **exploratoria**: interesa saber qué factores importan",
            "Es razonable despreciar interacciones de **tres o más** factores")],
  right=[txt("**Tenga cuidado cuando…**", size=20),
         bul("Hay pocos factores y el factorial completo es barato",
             "Se esperan interacciones entre muchos factores",
             "El objetivo es **optimizar**, no tamizar",
             "No habrá recursos para **confirmar** las conclusiones")])

S("¿Qué significa 2^{k−p}?",
  """La notación resume el diseño completo. La base 2 indica que cada factor tiene dos niveles (bajo y alto, codificados −1 y +1). k es el número de factores que se estudian. p es el número de generadores, es decir, cuántas veces se parte el factorial por la mitad. El diseño tiene N = 2^{k−p} corridas y es una fracción 1/2^{p} del factorial completo.

Ejemplo: un 2^{6−2} estudia 6 factores en 16 corridas, que es la cuarta parte de las 64 del factorial completo.""",
  left=[form("2^{k−p}", size=54),
        bul("**2**: niveles de cada factor (−1 y +1)",
            "**k**: número de factores",
            "**p**: número de generadores",
            "**N = 2^{k−p}**: número de corridas",
            "Fracción **1/2^{p}** del factorial completo")],
  right=[tab(["Diseño", "Factores", "Corridas", "Fracción", "Completo"],
             [["2^{3−1}", "3", "4", "1/2", "8"], ["2^{4−1}", "4", "8", "1/2", "16"],
              ["2^{5−1}", "5", "16", "1/2", "32"], ["2^{6−2}", "6", "16", "1/4", "64"],
              ["2^{7−4}", "7", "8", "1/16", "128"]], size=16, first_left=False)], ratio=0.46)

S("Vocabulario propio del diseño",
  """Generador: la interacción que define la fracción; por ejemplo ABCD en I = ABCD, que equivale a definir D = ABC. Palabra: cada interacción que aparece en la relación de definición, sea un generador o un producto de generadores.

Relación de definición: el conjunto de todas las palabras iguales a la identidad I; incluye los generadores y todos sus productos.

Alias: efectos que se estiman con la misma columna de signos (o con la opuesta, en una fracción alterna) y por tanto no se pueden distinguir. Una cadena de alias es el grupo completo de efectos que comparten columna.

Fracción principal: la que se obtiene con todos los generadores en signo positivo. Las demás son fracciones alternas; todas juntas forman la familia.

Diseño básico: el factorial completo en k − p factores sobre el que se construye la fracción. Diseño saturado: el que estudia k = N − 1 factores en N corridas.""",
  body=[tab(["Término", "Significado"],
            [["Generador", "Interacción que define la fracción: ABCD en I = ABCD (equivale a D = ABC)"],
             ["Palabra", "Cada interacción de la relación de definición: generadores y sus productos"],
             ["Relación de definición", "El conjunto de todas las palabras, que son iguales a la identidad I"],
             ["Alias", "Efectos que comparten columna de signos (igual u opuesta) y no se distinguen"],
             ["Fracción principal", "La que usa todos los generadores con signo +"],
             ["Fracción alterna", "Cualquier otra de la misma familia (algún generador con signo −)"],
             ["Diseño básico", "Factorial completo en k − p factores sobre el que se construye"],
             ["Diseño saturado", "Estudia k = N − 1 factores en N corridas"]],
            size=16, colw=[0.26, 0.74])])

_r = basic(3)
_names = ["(1)", "a", "b", "ab", "c", "ac", "bc", "abc"]
_sig = ["ninguno (todos en nivel bajo)", "A", "B", "A y B", "C", "A y C", "B y C", "A, B y C"]
_rows = [[str(i + 1), sg(row["A"]), sg(row["B"]), sg(row["C"]), nm, sig]
         for i, (row, nm, sig) in enumerate(zip(_r, _names, _sig))]
S("¿Cómo se lee la tabla de un factorial 2^{k}?",
  """Antes de fraccionar hay que saber leer la tabla del factorial completo, porque la fracción se recorta de ella. La tabla usa dos alfabetos. Las letras mayúsculas A, B, C encabezan las columnas y nombran los factores (y también sus efectos). Las letras minúsculas identifican las filas, es decir, las combinaciones de tratamientos: una letra presente indica que ese factor está en su nivel alto (+1) y una letra ausente indica que está en su nivel bajo (−1). Así, ac es la corrida con A y C altos y B bajo, y (1) es la corrida con todos los factores en nivel bajo.

Las filas se escriben en el orden estándar o de Yates: se introduce un factor a la vez y se combina con todos los anteriores. Para tres factores: (1), a, b, ab, c, ac, bc, abc. En ese orden la columna A alterna −, +; la de B va de dos en dos y la de C de cuatro en cuatro. Montgomery usa la misma minúscula para nombrar la corrida y para denotar la respuesta (o el total de respuestas) observada en ella; por eso más adelante se escriben contrastes como a − b − c + abc. La letra I se reserva para la columna identidad, de modo que el noveno factor se llama J.""",
  left=[tab(["Corrida", "A", "B", "C", "Etiqueta", "Factores en nivel alto"], _rows, size=15,
            colw=[0.13, 0.09, 0.09, 0.09, 0.15, 0.45], first_left=False)],
  right=[bul("**Columnas, mayúsculas**: los factores A, B, C (y sus efectos)",
             "**Filas, minúsculas**: las combinaciones de tratamientos",
             "Letra **presente** = factor en nivel alto (+); **ausente** = nivel bajo (−)",
             "**(1)** = todos los factores en nivel bajo",
             "**Orden estándar (Yates)**: A alterna de uno en uno, B de dos en dos, C de cuatro en cuatro",
             "La minúscula también denota la **respuesta observada** en esa corrida", size=16),
         note("La letra I se reserva para la identidad; por eso tras H el siguiente factor es J", size=14)],
  ratio=0.56)

_rows = []
for nm, row in zip(_names, _r):
    abc = row["A"] * row["B"] * row["C"]
    _rows.append([nm, "+", sg(row["A"]), sg(row["B"]), sg(row["C"]), sg(row["A"] * row["B"]),
                  sg(row["A"] * row["C"]), sg(row["B"] * row["C"]), sg(abc)])
S("¿Cómo se completa la tabla de signos del 2^{k}?",
  """Las columnas de los factores no bastan: hace falta una columna por cada efecto que el diseño puede estimar, y un 2^{k} estima 2^{k} − 1 efectos. Las columnas de las interacciones se obtienen multiplicando, fila por fila, los signos de los factores que las componen: en la corrida a, A es + y B es −, de modo que AB es −; en la corrida ab, ambos son + y AB es +. La columna ABC es el producto de las tres. Se agrega además la columna I, toda positiva, que corresponde al promedio general.

La tabla completa tiene tres propiedades que se usan en todo el tema. Cada columna de efecto tiene la mitad de signos positivos y la mitad negativos (está balanceada). El producto de dos columnas cualesquiera es otra columna de la tabla, y una letra multiplicada por sí misma da I porque (±1)² = 1: A·AB = A²B = B. Las columnas son ortogonales entre sí, por lo que cada efecto se estima de forma independiente con su propio contraste: la suma de las respuestas multiplicadas por los signos de la columna, dividida entre N/2.

De esta tabla sale la fracción: elegir media fracción es quedarse con las filas en que una columna de interacción tiene el mismo signo.""",
  left=[tab(["Trat.", "I", "A", "B", "C", "AB", "AC", "BC", "ABC"], _rows, size=15),
        note("Las columnas de interacción son **productos de signos**: en la fila a, AB = (+)(−) = −", size=14)],
  right=[bul("**2^{k} − 1 columnas** de efectos: 3 principales, 3 dobles y 1 triple en el 2^{3}",
             "La columna **I** es toda positiva y corresponde al promedio general",
             "Cada columna de efecto tiene **N/2 signos +** y **N/2 signos −**",
             "El producto de dos columnas es otra columna; una letra al cuadrado es I",
             "Columnas **ortogonales**: cada efecto se estima con su propio contraste", size=16),
         form("A · AB = A^{2}B = B", "ℓ_{A} = Σ (signo_{A}) · y / (N/2)", size=18)],
  ratio=0.56)

section(2, "Resolución del diseño", "Qué tanto se mezclan los efectos")

S("¿Qué es la resolución de un diseño?",
  """La resolución es una etiqueta que resume qué tan grave es la mezcla de efectos en un diseño fraccionado. Se escribe con número romano como subíndice: 2^{3−1}_{III} se lee «dos a la tres menos uno, resolución tres».

Montgomery la define así: un diseño es de resolución R cuando ningún efecto de p factores es alias de otro efecto que contenga menos de R − p factores. Leída de forma más sencilla: si dos efectos son alias, entre los dos suman al menos R letras.

Con esa lectura se entiende cada caso. En resolución III, un efecto principal (1 letra) no puede ser alias de otro principal (1 + 1 = 2 letras), pero sí de una interacción doble (1 + 2 = 3). En resolución IV, un principal solo puede ser alias de una interacción triple (1 + 3 = 4), y dos interacciones dobles sí pueden ser alias entre sí (2 + 2 = 4). En resolución V, un principal solo se mezcla con interacciones de cuatro factores y una doble con triples (2 + 3 = 5).""",
  left=[form("Si dos efectos son alias, entre los dos suman al menos **R** letras", size=19),
        bul("Se escribe como subíndice romano: **2^{3−1}_{III}**",
            "Definición del libro: ningún efecto de **p** factores es alias de otro con menos de **R − p** factores",
            "Cuanto **mayor** R, menos se mezclan los efectos de orden bajo", size=16)],
  right=[tab(["Resolución", "Un efecto principal es alias de…", "Una interacción doble es alias de…"],
             [["III", "interacciones de **2** factores (1 + 2 = 3)", "principales u otras dobles"],
              ["IV", "interacciones de **3** factores (1 + 3 = 4)", "otras **dobles** (2 + 2 = 4)"],
              ["V", "interacciones de **4** factores (1 + 4 = 5)", "interacciones de **3** factores (2 + 3 = 5)"]],
             size=15, colw=[0.18, 0.41, 0.41]),
         note("En ninguna de las tres un efecto principal es alias de **otro principal**", size=15)], ratio=0.46)

S("¿Cómo se calcula la resolución?",
  """La regla práctica es directa: la resolución es igual al número de letras de la palabra más corta de la relación de definición. Por eso Montgomery llama a los diseños de resolución III, IV y V diseños «de tres, cuatro y cinco letras».

La razón es la regla de los alias. Si la palabra más corta tiene L letras, al multiplicarla por un efecto principal se obtiene un alias de L − 1 letras, y la suma de los dos es justamente L.

La resolución la decide quien elige los generadores. En una fracción un medio, usar como generador la interacción de mayor orden da la resolución más alta posible, que es R = k. En una fracción un cuarto importa también la interacción generalizada: con E = ABC y F = BCD las tres palabras tienen cuatro letras (resolución IV); con E = ABC y F = ABCD aparece la palabra DEF, de tres letras, y el diseño baja a resolución III con el mismo número de corridas.""",
  body=[form("Resolución = número de letras de la **palabra más corta** de la relación de definición", size=19),
        tab(["Diseño", "Generadores", "Relación de definición", "Palabra más corta", "Resolución"],
            [["2^{3−1}", "C = AB", "I = ABC", "3 letras", "III"],
             ["2^{4−1}", "D = ABC", "I = ABCD", "4 letras", "IV"],
             ["2^{5−1}", "E = ABCD", "I = ABCDE", "5 letras", "V"],
             ["2^{6−2}", "E = ABC,  F = BCD", "I = ABCE = BCDF = ADEF", "4 letras", "IV"],
             ["2^{6−2}", "E = ABC,  F = ABCD", "I = ABCE = ABCDF = DEF", "3 letras", "III"]],
            size=15, colw=[0.12, 0.22, 0.32, 0.18, 0.16], hl=[4], first_left=False),
        note("Mismo número de corridas, distinta resolución: la elección de los generadores **importa**", size=15)])

S("¿Qué supuestos exige cada resolución?",
  """La resolución dice qué hay que suponer despreciable para leer los resultados sin ambigüedad.

Con resolución III, cada efecto principal está mezclado con interacciones dobles: para interpretar un efecto principal hay que suponer que esas interacciones no existen. Sirve para tamizar muchos factores cuando se cree que casi no hay interacciones.

Con resolución IV, los efectos principales solo están mezclados con interacciones triples, que casi siempre son despreciables, así que se estiman limpios. Las interacciones dobles quedan en cadenas entre sí: se ve que una cadena es grande, pero no cuál de sus interacciones la causa sin más información.

Con resolución V, si las interacciones triples son despreciables, todos los efectos principales y todas las interacciones dobles se estiman de forma única.

Montgomery recomienda usar la resolución más alta que permita el grado de fraccionamiento: entre más alta, menos restrictivos son los supuestos necesarios para una interpretación única.""",
  body=[tab(["Resolución", "Para leer los principales hay que suponer despreciables…", "Las interacciones dobles…", "Uso típico"],
            [["III", "las interacciones **dobles**", "no se pueden separar de los principales", "Tamizar muchos factores sin interacciones esperadas"],
             ["IV", "las interacciones **triples**", "quedan en cadenas entre sí", "Tamizar cuando puede haber interacciones"],
             ["V", "las de **cuatro** factores", "se estiman limpias si las triples son despreciables", "Estimar principales e interacciones dobles"]],
            size=15, colw=[0.13, 0.31, 0.29, 0.27]),
        note("Regla: la **resolución más alta** que permita el presupuesto de corridas. A más resolución, menos supuestos")])

section(3, "La fracción un medio 2^{k−1}", "Alias, construcción, proyección y dos ejemplos")

_rows = []
for nm, row in zip(_names, _r):
    abc = row["A"] * row["B"] * row["C"]
    _rows.append([nm, sg(row["A"]), sg(row["B"]), sg(row["C"]), sg(row["A"] * row["B"]),
                  sg(row["A"] * row["C"]), sg(row["B"] * row["C"]), sg(abc)])
S("La fracción un medio: el 2^{3−1} con I = ABC",
  """Se parte de la tabla de signos del 2^{3} completo y se conservan solo las corridas en las que la columna ABC es positiva: a, b, c y abc. ABC es el generador de la fracción y, como en esas corridas la columna ABC coincide con la columna identidad, se escribe I = ABC.

Las otras cuatro corridas, (1), ab, ac y bc, forman la fracción alterna, I = −ABC. En el cubo se ve que cada fracción ocupa cuatro vértices no adyacentes y que, al proyectar sobre cualquier cara, queda un factorial 2^{2} completo.""",
  left=[tab(["Trat.", "A", "B", "C", "AB", "AC", "BC", "ABC"], _rows, size=15,
            hl=[1, 2, 4, 7]),
        note("Fracción principal: corridas con **ABC = +**  →  a, b, c, abc", size=15)],
  right=[cube(["a", "b", "c", "abc"], h=4.4,
              caption="Vértices rellenos: fracción principal (I = ABC)")], ratio=0.56)

S("¿Qué son los alias y cómo se obtienen?",
  """Con cuatro corridas solo hay tres grados de libertad. Al calcular el contraste de A se usa exactamente la misma combinación de corridas que para BC: las dos columnas de signos son idénticas dentro de la fracción. Por eso lo que se estima no es A sino A + BC. Se dice que A y BC son alias.

Regla para obtenerlos: se multiplica el efecto por cada palabra de la relación de definición, recordando que cualquier letra al cuadrado es la identidad. Así A·ABC = A²BC = BC.

En la fracción alterna (I = −ABC) los alias cambian de signo: se estima A − BC. Si se corren las dos fracciones, la semisuma y la semidiferencia de las dos estimaciones separan A de BC.""",
  left=[form("ℓ_{A} = ½ (a − b − c + abc) = ℓ_{BC}", size=20),
        bul("Dentro de la fracción, las columnas de **A** y de **BC** son idénticas",
            "No se estima A, sino **A + BC**",
            "**Regla:** multiplicar el efecto por la relación de definición (letra² = I)"),
        form("A · I = A · ABC = A^{2}BC = BC", size=20)],
  right=[tab(["", "Principal (I = ABC)", "Alterna (I = −ABC)"],
             [["ℓ_{A}", "A + BC", "A − BC"], ["ℓ_{B}", "B + AC", "B − AC"],
              ["ℓ_{C}", "C + AB", "C − AB"]], size=16, colw=[0.16, 0.42, 0.42], first_left=False),
         note("Con las dos fracciones se separan el efecto principal y la interacción")],
  ratio=0.5)

S("Fracción principal, fracción alterna y familia",
  """Las dos mitades del 2^{3} son igual de válidas. La fracción principal, I = +ABC, tiene las corridas a, b, c y abc. La fracción alterna o complementaria, I = −ABC, tiene las otras cuatro: (1), ab, ac y bc. En la alterna los alias cambian de signo: ℓ′_{A} estima A − BC. Montgomery señala que en la práctica no importa cuál de las dos se corra; ambas pertenecen a la misma familia.

Si después de correr una se corre también la otra, se tienen las ocho corridas del 2^{3} completo, corrido en dos bloques de cuatro con ABC confundida con los bloques. Los efectos se separan sumando y restando las estimaciones de las dos fracciones: la semisuma deja el efecto principal y la semidiferencia deja la interacción.""",
  left=[cube(["(1)", "ab", "ac", "bc"], h=3.6, caption="Vértices rellenos: fracción alterna (I = −ABC)"),
        bul("Principal **I = +ABC**: a, b, c, abc",
            "Alterna **I = −ABC**: (1), ab, ac, bc",
            "Las dos juntas forman el **2^{3} completo** en dos bloques", size=15)],
  right=[form("½ (ℓ_{A} + ℓ′_{A}) = ½ (A + BC + A − BC) → A",
              "½ (ℓ_{A} − ℓ′_{A}) = ½ (A + BC − A + BC) → BC", size=16),
         tab(["i", "De ½ (ℓ_{i} + ℓ′_{i})", "De ½ (ℓ_{i} − ℓ′_{i})"],
             [["A", "A", "BC"], ["B", "B", "AC"], ["C", "C", "AB"]], size=16, first_left=False),
         note("En la práctica **no importa** cuál de las dos fracciones se corra", size=15)], ratio=0.44)

_rows = [[str(i + 1), sg(r["A"]), sg(r["B"]), sg(r["C"]), sg(r["D"]), t]
         for i, (r, t) in enumerate(zip(r1, trat1))]
S("¿Cómo construyo una fracción un medio?",
  """Método del diseño básico. Primero se escribe el factorial completo en k − 1 factores: tiene el número correcto de corridas pero le falta una columna. Después se agrega el último factor igualando sus signos a los de la interacción de mayor orden de los demás. Para cuatro factores: se escribe el 2^{3} en A, B y C y se define D = ABC, lo que equivale a I = ABCD.

Usar la interacción de mayor orden garantiza la resolución más alta posible, que en una fracción un medio es igual a k. La fracción alterna se obtiene con D = −ABC. Otra forma de verlo: se divide el 2^{k} en dos bloques confundiendo la interacción de mayor orden, ABC···K; cada bloque es una fracción 2^{k−1} de máxima resolución.""",
  left=[num("Escribir el **diseño básico**: factorial completo en k − 1 factores",
            "Agregar el factor k con los signos de la **interacción de mayor orden**",
            "Para la fracción alterna, usar el signo contrario"),
        form("D = ABC   ⇔   I = ABCD", size=20),
        note("La fracción un medio de mayor resolución tiene **resolución k**")],
  right=[tab(["Corrida", "A", "B", "C", "D = ABC", "Trat."], _rows, size=15)], ratio=0.5)

S("¿En qué se proyecta una fracción un medio?",
  """Proyectar es mirar el diseño solo en algunos de sus factores, como si los demás no existieran. Montgomery enuncia la regla general: un fraccionado de resolución R contiene un factorial completo, posiblemente con réplicas, en cualquier subconjunto de R − 1 factores.

La consecuencia práctica es útil: si se cree que a lo sumo R − 1 factores son importantes, un diseño de resolución R es la elección adecuada, porque si la sospecha es correcta el diseño se convierte en un factorial completo en los factores activos.

Como la fracción un medio de máxima resolución tiene R = k, todo 2^{k−1} se proyecta en un factorial completo en cualesquiera k − 1 de sus factores, en dos réplicas de un completo en cualesquiera k − 2, en cuatro réplicas en cualesquiera k − 3, y así sucesivamente. El 2^{3−1}_{III} se proyecta en un 2^{2} completo en cualquier par de factores: es la figura 8-2 del libro, donde el cubo deja un cuadrado completo en cada una de sus tres caras.""",
  left=[form("Resolución R ⇒ factorial completo en cualquier subconjunto de **R − 1** factores", size=18),
        bul("Fracción un medio de máxima resolución: **R = k**",
            "Si a lo sumo R − 1 factores importan, un diseño de resolución R es **adecuado**",
            "Los factores descartados se convierten en **réplicas**", size=16)],
  right=[tab(["Diseño", "En k − 1 factores", "En k − 2", "En k − 3"],
             [["2^{3−1}_{III}", "2^{2} completo", "—", "—"],
              ["2^{4−1}_{IV}", "2^{3} completo", "2 réplicas de 2^{2}", "—"],
              ["2^{5−1}_{V}", "2^{4} completo", "2 réplicas de 2^{3}", "4 réplicas de 2^{2}"]],
             size=15, colw=[0.22, 0.26, 0.26, 0.26], first_left=False),
         txt("Ejemplo: el 2^{3−1} deja un cuadrado completo en cada cara del cubo (Montgomery, fig. 8-2)", size=14)],
  ratio=0.46)

E(1, "índice de filtración", "Montgomery, ejemplos 6-2 y 8-1",
  ["Un producto químico se fabrica en un recipiente a presión. En la planta piloto se quiere estudiar los factores que se cree influyen en el **índice de filtración** del producto (gal/h): A temperatura, B presión, C concentración de formaldehído y D velocidad de agitación, cada uno a dos niveles.",
   "Con las condiciones actuales la filtración ronda los 75 gal/h y el proceso trabaja con la concentración de formaldehído en el nivel alto. El ingeniero quiere **reducir el formaldehído** tanto como sea posible, pero hasta ahora cada intento ha bajado la filtración.",
   "El factorial completo 2^{4} exige 16 corridas. Para ahorrar, se corre solo **la mitad: 8 corridas**, elegidas con D = ABC (I = ABCD). Cada combinación se corre una vez, en orden aleatorio."],
  "Encontrar las condiciones que **maximizan la filtración** y ver si se puede trabajar con **menos formaldehído** sin perderla",
  ["Construir la fracción y escribir sus alias", "Estimar los efectos e identificar los activos",
   "Interpretar las cadenas de alias grandes", "Proponer el modelo y la mejor condición"])

_rows = [[str(i + 1), sg(r["A"]), sg(r["B"]), sg(r["C"]), sg(r["D"]), t, str(v)]
         for i, (r, t, v) in enumerate(zip(r1, trat1, y1))]
S("Ejemplo 1 · Índice de filtración, 2^{4−1}_{IV}",
  """Un producto químico se fabrica en un recipiente a presión y se quiere aumentar su índice de filtración. Se estudian cuatro factores a dos niveles: A temperatura, B presión, C concentración de formaldehído y D velocidad de agitación. El factorial completo exigiría 16 corridas; se corre la fracción un medio con D = ABC, es decir I = ABCD, en 8 corridas.

Es un diseño de resolución IV: cada efecto principal es alias de una interacción triple, y las interacciones dobles son alias por pares (AB = CD, AC = BD, AD = BC). Fuente de los datos: Montgomery, ejemplo 8-1.""",
  left=[bul("Respuesta: **índice de filtración** (se quiere aumentar)",
            "A: temperatura · B: presión · C: concentración · D: velocidad de agitación",
            "Fracción un medio con **D = ABC**  (I = ABCD), 8 corridas",
            "Resolución IV: principales libres de interacciones dobles"),
        tab(["Alias de los principales", "Alias de las interacciones"],
            [["A = BCD", "AB = CD"], ["B = ACD", "AC = BD"], ["C = ABD", "AD = BC"],
             ["D = ABC", "—"]], size=15, first_left=False)],
  right=[tab(["Corrida", "A", "B", "C", "D", "Trat.", "Filtración"], _rows, size=15, first_left=False)],
  ratio=0.5)

_ord = sorted(ef1, key=lambda w: abs(ef1[w][1]))
_ns = sorted(normal_scores([abs(ef1[w][1]) for w in ef1]))
from statistics import NormalDist as _ND
_hs = [_ND().inv_cdf(0.5 + 0.5 * (i + 0.5) / 7) for i in range(7)]
S("Ejemplo 1 · Efectos estimados y alias",
  """La tabla muestra el efecto estimado con cada columna y la cadena de alias que realmente estima. Tres efectos principales son grandes: A (19.0), C (14.0) y D (16.5). También son grandes las cadenas AC + BD (−18.5) y AD + BC (19.0). B y AB + CD son pequeños.

En la gráfica seminormal la recta de Daniel se traza solo con los efectos pequeños (B y AB + CD) y pasa por el origen: es lo que se esperaría si todos los efectos fueran ruido. Los otros cinco se apartan mucho de ella. Esa es la primera clasificación para el ANOVA: lo que se aleja de la recta entra al modelo (A, C, D, AC + BD y AD + BC) y lo que queda sobre ella (B y AB + CD) pasa al error. Esta gráfica es un cálculo propio: el libro solo presenta la tabla de efectos.

Interpretación de las cadenas: como B no tiene efecto, es más razonable atribuir AC + BD a AC y AD + BC a AD. Montgomery lo justifica con la navaja de Ockham: la explicación más simple suele ser la correcta. El modelo tentativo es A, C, D, AC y AD.""",
  left=[tab(["Columna", "Efecto", "Estima"],
            [[w, f(ef1[w][1]), alias1[w]] for w in ["A", "B", "C", "D", "AB", "AC", "AD"]],
            size=16, hl=[0, 2, 3, 5, 6], first_left=False),
        note("B es pequeño  →  AC + BD se atribuye a **AC** y AD + BC a **AD**", size=15)],
  right=[scatter(_p1 := [(abs(ef1[w][1]), z) for w, z in zip(_ord, _hs)], "|Efecto|", "Puntuación seminormal",
                 h=4.1, labels={i: w for i, w in enumerate(_ord)},
                 line=daniel(_p1, _a1 := {i for i, w in enumerate(_ord) if w not in ("B", "AB")}, origen=True),
                 hi=_a1, title="Gráfica seminormal con recta de Daniel"),
         note("Lejos de la recta → **modelo** (A, C, D, AC, AD).  Sobre la recta → **error** (B, AB)", size=14)],
  ratio=0.46)

_an = [[t if len(t) == 1 else t, f(ss, 1), "1", f(ss, 1), f(F), pv(p)] for t, ss, _, _, F, p in m1["anova"]]
_an += [["Error", f(m1["sse"], 1), str(m1["dfe"]), f(m1["mse"]), "", ""],
        ["Total", f(m1["sst"], 1), "7", "", "", ""]]
S("Ejemplo 1 · ANOVA e interpretación",
  f"""Se ajusta el modelo con A, C, D, AC y AD. Los dos efectos descartados (B y AB) forman el error, con 2 grados de libertad. Los cinco términos son significativos al 5 %: todos tienen F_{{0}} mayor que F_{{0.05, 1, 2}} = {f(f_ppf(0.05, 1, 2))} y valores p menores que 0.01. El modelo explica el {100 * m1['r2']:.2f} % de la variabilidad.

Advertencia: esta tabla ANOVA no aparece en el libro, que en este ejemplo solo estima los efectos y da el modelo; se calculó aquí a partir de los datos. El error tiene solo 2 grados de libertad y se formó con los dos efectos más pequeños, elegidos después de ver los datos, de modo que los valores F y p son optimistas y los supuestos apenas se pueden verificar. La conclusión es tentativa.

Interpretación: la temperatura (A) aumenta la filtración; el efecto de la concentración (C) depende de la temperatura (interacción AC negativa) y el de la agitación (D) también (interacción AD positiva). La presión (B) no influye, de modo que el diseño se proyecta en un 2^{{3}} completo en A, C y D. La mejor condición es A alto, C bajo y D alto. El factorial completo original llegó a las mismas conclusiones con el doble de corridas.""",
  left=[tab(["SV", "SS", "DF", "MS", "F_{0}", "P-Value"], _an, size=15),
        form("ŷ = 70.75 + 9.50 x_{1} + 7.00 x_{3} + 8.25 x_{4} − 9.25 x_{1}x_{3} + 9.50 x_{1}x_{4}", size=15)],
  right=[bul(f"Todos los términos: F_{{0}} > F_{{0.05, 1, 2}} = {f(f_ppf(0.05, 1, 2))}  →  se rechaza H_{{0}}",
             f"R^{{2}} = {100 * m1['r2']:.2f} %;  R^{{2}} ajustado = {100 * m1['r2adj']:.2f} %",
             "B no influye: el diseño se **proyecta** en un 2^{3} completo en A, C, D",
             "Mejor condición: **A alto, C bajo, D alto**", size=17),
         note("ANOVA calculada aquí (no está en el libro). Solo 2 g.l. de error: conclusión **tentativa**", size=15)],
  ratio=0.56)

E(2, "rendimiento de un circuito integrado", "Montgomery, ejemplo 8-2",
  ["En la manufactura de un circuito integrado se quiere **mejorar el rendimiento** del proceso. Se investigan cinco factores a dos niveles: A ajuste de apertura (pequeña, grande), B tiempo de exposición (20 % por debajo y por encima del nominal), C tiempo de desarrollo (30 y 45 s), D tamaño de la máscara (pequeña, grande) y E tiempo de grabado (14.5 y 15.5 min).",
   "El factorial completo 2^{5} exige 32 corridas. Se decide correr **la mitad, 16 corridas**, con E = ABCD (I = ABCDE), una sola réplica de cada combinación y en orden aleatorio.",
   "Sin réplicas no hay una estimación directa del error: la significancia de los efectos se tiene que juzgar con los propios efectos."],
  "Saber qué factores e interacciones **afectan el rendimiento** y en qué niveles conviene operar",
  ["Identificar la resolución y los alias", "Estimar los 15 efectos y decidir cuáles son activos",
   "Ajustar el modelo reducido y validar los supuestos", "Recomendar las condiciones de operación"])

S("Ejemplo 2 · Rendimiento de un circuito integrado",
  """En la fabricación de un circuito integrado se quiere mejorar el rendimiento del proceso. Se estudian cinco factores: A ajuste de apertura, B tiempo de exposición, C tiempo de desarrollo, D tamaño de la máscara y E tiempo de grabado. El factorial completo tendría 32 corridas; se corre la fracción un medio con E = ABCD (I = ABCDE) en 16 corridas.

Es de resolución V: los efectos principales son alias de interacciones de cuatro factores y las interacciones dobles de interacciones triples. Si las interacciones de tres o más factores son despreciables, todos los efectos principales y todas las interacciones dobles se estiman limpios. Fuente: Montgomery, ejemplo 8-2.""",
  left=[bul("Respuesta: **rendimiento** del proceso (se quiere aumentar)",
            "Cinco factores, 16 corridas: **E = ABCD**  (I = ABCDE)",
            "**Resolución V**: principales e interacciones dobles libres entre sí"),
        tab(["Factor", "Nivel (−)", "Nivel (+)"],
            [["A  Apertura", "pequeña", "grande"], ["B  Tiempo de exposición", "−20 %", "+20 %"],
             ["C  Tiempo de desarrollo", "30 s", "45 s"], ["D  Tamaño de máscara", "pequeña", "grande"],
             ["E  Tiempo de grabado", "14.5 min", "15.5 min"]], size=15)],
  right=[tab(["Corrida", "A", "B", "C", "D", "E", "Y"],
             [[str(i + 1), sg(r["A"]), sg(r["B"]), sg(r["C"]), sg(r["D"]), sg(r["E"]), str(v)]
              for i, (r, v) in enumerate(zip(r2, y2))], size=12, first_left=False, pad=0.1)], ratio=0.52)

_vals = [ef2[w][1] for w in w2]
_z = normal_scores(_vals)
_srt = sorted(range(15), key=lambda i: _vals[i])
_top = sorted(w2, key=lambda w: -abs(ef2[w][1]))[:8]
S("Ejemplo 2 · ¿Qué efectos son activos?",
  f"""Con una sola réplica y 15 efectos estimados no hay error, así que se usa la gráfica de probabilidad normal de los efectos. La recta de Daniel se ajusta con los efectos pequeños, que se comportan como ruido normal de media cero. Once efectos caen sobre ella alrededor de cero; cuatro se separan claramente: B (33.88), A (11.13), C (10.88) y AB (6.88).

Esa es la primera clasificación para el ANOVA: los cuatro que se apartan forman el modelo reducido y los once que quedan sobre la recta se combinan como error, con 11 grados de libertad.

El método de Lenth coincide: el pseudo error estándar es PSE = {f(pse2, 4)} y el margen de error es ME = {f(me2)}; solo esos cuatro efectos lo superan.

Como el diseño es de resolución V, AB es alias de CDE, una interacción triple, y se atribuye a AB suponiendo que las interacciones triples son despreciables.

El libro usa solo la gráfica normal en este ejemplo; el cálculo de Lenth y el Pareto se agregaron aquí.""",
  left=[scatter(_p2 := [(_vals[i], _z[i]) for i in _srt], "Efecto", "Puntuación normal", h=4.2,
                labels={k: w2[i] for k, i in enumerate(_srt) if w2[i] in ("A", "B", "C", "AB")},
                line=daniel(_p2, _a2 := {k for k, i in enumerate(_srt) if w2[i] in ("A", "B", "C", "AB")}),
                hi=_a2, title="Gráfica normal con recta de Daniel"),
        note("Fuera de la recta → **modelo** (B, A, C, AB).  Sobre la recta → **error** (11 g.l.)", size=14)],
  right=[bars(_top, [abs(ef2[w][1]) for w in _top], "|Efecto|", h=3.4, title="Pareto de efectos (los 8 mayores)"),
         note(f"Lenth: PSE = {f(pse2, 4)},  ME = {f(me2)}.  Activos: **B, A, C y AB**", size=15)],
  ratio=0.5)

_an = [[t, f(ss, 2), "1", f(ss, 2), f(F), pv(p)] for t, ss, _, _, F, p in m2["anova"]]
_an += [["Error", f(m2["sse"], 2), str(m2["dfe"]), f(m2["mse"], 4), "", ""],
        ["Total", f(m2["sst"], 2), "15", "", "", ""]]
S("Ejemplo 2 · ANOVA y conclusión",
  f"""El modelo reducido incluye A, B, C y AB; los once efectos descartados forman el error con 11 grados de libertad. Los cuatro términos son altamente significativos (F_{{0.05, 1, 11}} = {f(f_ppf(0.05, 1, 11))}) y el modelo explica el {100 * m2['r2']:.2f} % de la variabilidad.

Los tres efectos principales son positivos: el rendimiento aumenta con apertura grande, mayor tiempo de exposición y mayor tiempo de desarrollo. La interacción AB es positiva: el efecto de la apertura es mayor cuando el tiempo de exposición es alto.

Como D y E no influyen, el diseño se proyecta en dos réplicas de un 2^{{3}} en A, B y C. La mejor condición es A, B y C en nivel alto, con rendimiento promedio de 61.5. D y E se pueden fijar donde resulte más económico.""",
  left=[tab(["SV", "SS", "DF", "MS", "F_{0}", "P-Value"], _an, size=15),
        form("ŷ = 30.31 + 5.56 x_{1} + 16.94 x_{2} + 5.44 x_{3} + 3.44 x_{1}x_{2}", size=16)],
  right=[bul(f"F_{{0.05, 1, 11}} = {f(f_ppf(0.05, 1, 11))}: los cuatro términos son significativos",
             f"R^{{2}} = {100 * m2['r2']:.2f} %;  R^{{2}} ajustado = {100 * m2['r2adj']:.2f} %",
             "D y E no influyen: proyección en **dos réplicas de un 2^{3}** en A, B, C",
             "Mejor condición: **A, B y C altos** (promedio 61.5)",
             "D y E se fijan donde sea más económico", size=17)], ratio=0.56)

section(4, "Secuencias de diseños fraccionados", "Correr una fracción, analizar y decidir el paso siguiente")

S("¿Por qué experimentar en secuencia?",
  """El uso de fraccionados lleva con frecuencia a una gran economía, sobre todo si las corridas se pueden hacer en etapas. Con cuatro factores, en lugar de correr las 16 corridas del 2^{4}, Montgomery recomienda casi siempre correr primero la fracción 2^{4−1}_{IV} de 8 corridas, analizarla y después decidir qué hacer.

Si quedan ambigüedades, siempre se puede correr la fracción alterna y completar el 2^{4}. Cuando se completa así, las dos mitades funcionan como bloques del diseño completo, con la interacción de mayor orden (ABCD) confundida con los bloques. Lo único que se pierde por haber experimentado en dos etapas es la información de esa interacción, que de todos modos suele ser despreciable.

La ventaja es que muchas veces la primera fracción da información suficiente para pasar a la etapa siguiente sin correr la segunda: agregar o quitar factores, cambiar la respuesta o mover los niveles a otros rangos.""",
  left=[num("Correr la **primera fracción**: 2^{4−1}_{IV}, 8 corridas",
            "**Analizar**: ¿los resultados son claros?",
            "Si hay ambigüedad, correr la **fracción alterna**: 8 corridas más",
            "Las 16 corridas forman el **2^{4} completo** en dos bloques", size=17)],
  right=[cards(("Lo que se pierde", "Solo la interacción de mayor orden, **ABCD**, que queda confundida con los bloques"),
               ("Lo que se gana", "Muchas veces la primera fracción **basta** para decidir el paso siguiente"),
               size=16, cols=1)], ratio=0.52)

S("¿Qué opciones hay después de la primera fracción?",
  """La figura 8-11 del libro, adaptada de Box, resume las posibilidades de seguimiento después de un fraccionado inicial. Moverse a una nueva región para explorar una tendencia aparente de la respuesta. Agregar otra fracción para resolver las ambigüedades de la primera. Reescalar algunos factores, porque pudieron haberse variado en rangos inapropiados. Eliminar factores que resultaron insignificantes y agregar otros nuevos. Hacer réplicas para mejorar la precisión de las estimaciones o porque algunas corridas se hicieron mal. Y aumentar el diseño, por ejemplo con puntos centrales y axiales, para modelar una curvatura aparente.

La idea de fondo es que el primer experimento casi nunca es el último: sirve para aprender y orientar el siguiente.""",
  body=[cards(("a · Moverse", "A una nueva región, para explorar una **tendencia** aparente de la respuesta"),
              ("b · Agregar otra fracción", "Para resolver las **ambigüedades** de la primera"),
              ("c · Reescalar factores", "Si sus niveles se eligieron en **rangos inapropiados**"),
              ("d · Eliminar y agregar factores", "Quitar los que no influyen y **probar otros**"),
              ("e · Hacer réplicas", "Para mejorar las estimaciones o **repetir corridas** mal hechas"),
              ("f · Aumentar el diseño", "Para modelar una **curvatura** aparente"), size=16, cols=3),
        txt("Fuente: Montgomery, fig. 8-11, adaptada de Box (Sequential Experimentation and Sequential Assembly of Designs)", size=13)])

E(1, "la fracción alterna (continuación)", "Montgomery, ejemplo 8-3",
  ["Con la primera fracción del índice de filtración quedaron dos cadenas grandes: AC + BD = −18.5 y AD + BC = 19.0. Se atribuyeron a AC y AD porque B no parecía influir, pero esa decisión se apoyó en el juicio del analista.",
   "El ingeniero no quiere depender de ese juicio antes de cambiar el proceso. Tiene la posibilidad de volver a la planta piloto y hacer **8 corridas más**.",
   "Decide correr la **fracción alterna**, I = −ABCD (D = −ABC): las ocho combinaciones del 2^{4} que no se corrieron la primera vez."],
  "Separar **AC de BD** y **AD de BC** con datos, sin depender del juicio",
  ["Construir la fracción alterna y escribir sus alias", "Estimar sus efectos",
   "Combinar las dos fracciones y aislar cada efecto", "Decidir qué interacciones son las reales"])

_rows = [[str(i + 1), sg(r["A"]), sg(r["B"]), sg(r["C"]), sg(r["D"]), t, str(v)]
         for i, (r, t, v) in enumerate(zip(r1b, ["d", "a", "b", "abd", "c", "acd", "bcd", "abc"], y1b))]
S("Ejemplo 1 · La fracción alterna I = −ABCD",
  """En el ejemplo 1 quedaron dos cadenas grandes, AC + BD y AD + BC. Atribuirlas a AC y AD fue una decisión razonable, pero se apoyó en el juicio del analista. Para no depender de él se corre la fracción alterna, I = −ABCD, que se construye con el mismo diseño básico pero con D = −ABC.

Sus ocho corridas son las que faltaban del 2^{4}. En esta fracción todas las cadenas de alias cambian de signo: ℓ′_{A} estima A − BCD y ℓ′_{AC} estima AC − BD. Las estimaciones obtenidas son ℓ′_{A} = 24.25, ℓ′_{B} = 4.75, ℓ′_{C} = 5.75, ℓ′_{D} = 12.75, ℓ′_{AB} = 1.25, ℓ′_{AC} = −17.75 y ℓ′_{AD} = 14.25. Fuente: Montgomery, ejemplo 8-3.""",
  left=[tab(["Corrida", "A", "B", "C", "D = −ABC", "Trat.", "Filtración"], _rows, size=15, first_left=False)],
  right=[tab(["Estimación", "Estima"],
             [[f"ℓ′_{{{w}}} = {f(ef1b[w][1])}", alias1[w].replace(" + ", " − ")] for w in ["A", "B", "C", "D", "AB", "AC", "AD"]],
             size=15, first_left=False),
         note("En la fracción alterna los alias aparecen con **signo contrario**", size=15)], ratio=0.52)

_rows = []
for w in ["A", "B", "C", "D", "AB", "AC", "AD"]:
    a, b = ef1[w][1], ef1b[w][1]
    al = alias1[w].split(" + ")
    _rows.append([w, f(a), f(b), f"{al[0]} = {f((a + b) / 2)}", f"{al[1]} = {f((a - b) / 2)}"])
S("Ejemplo 1 · Combinar las dos fracciones",
  """Para no depender del juicio del analista se corre la fracción alterna, con D = −ABC. Sus estimaciones ℓ′ tienen los alias con signo contrario: ℓ′_{A} estima A − BCD.

La semisuma de las dos estimaciones aísla el primer efecto de cada cadena y la semidiferencia el segundo. El resultado confirma la interpretación inicial: AC = −18.13 mientras BD = −0.38, y AD = 16.63 mientras BC = 2.38. Las interacciones reales eran AC y AD.

Las 16 corridas forman el factorial 2^{4} completo, corrido en dos bloques con ABCD confundida con bloques.""",
  body=[tab(["Columna", "ℓ  (I = ABCD)", "ℓ′  (I = −ABCD)", "½ (ℓ + ℓ′)", "½ (ℓ − ℓ′)"], _rows, size=16,
            hl=[5, 6], first_left=False),
        note("Se confirma la interpretación: las interacciones activas son **AC** y **AD**, no BD ni BC")])

S("¿Cómo se confirma una conclusión?",
  """Agregar la fracción alterna es en sí un experimento de confirmación: aporta información que fortalece, o corrige, las conclusiones de la primera fracción.

Montgomery menciona una forma más barata. Se usa el modelo ajustado para predecir la respuesta en un punto de interés dentro de la región explorada, que no sea uno de los puntos ya corridos. Después se corre ese ensayo, de preferencia varias veces, y se compara lo observado con lo predicho. Si coinciden dentro del error, el modelo queda respaldado; si no, falta algo en él.

En el ejemplo 1, el modelo con A, C, D, AC y AD predice 70.75 en el centro de la región, donde todos los factores codificados valen cero. Correr unas cuantas veces en el centro y obtener valores cercanos a 70.75 confirmaría el modelo. Si el promedio en el centro se alejara mucho, indicaría además una curvatura que el diseño de dos niveles no puede ver.""",
  left=[cards(("Fracción alterna", "Confirma y separa alias: duplica las corridas"),
              ("Corrida de confirmación", "Predecir con el modelo en un punto **nuevo**, correrlo varias veces y comparar"),
              size=16, cols=1)],
  right=[form("ŷ = 70.75 + 9.50 x_{1} + 7.00 x_{3} + 8.25 x_{4} − 9.25 x_{1}x_{3} + 9.50 x_{1}x_{4}", size=15),
         tab(["Punto", "x_{1}", "x_{3}", "x_{4}", "ŷ"],
             [["Centro de la región", "0", "0", "0", "70.75"]], size=16, first_left=False),
         note("Si las corridas en el centro se alejan de 70.75, el modelo **no** queda confirmado (o hay curvatura)", size=15)],
  ratio=0.42)

section(5, "La fracción un cuarto 2^{k−2}", "Dos generadores, fracciones alternas, proyección y un ejemplo")

S("¿Qué es una fracción un cuarto?",
  """Con un número moderadamente grande de factores suelen convenir fracciones más pequeñas. Una fracción un cuarto del 2^{k} tiene 2^{k−2} corridas y se llama diseño 2^{k−2}.

Necesita dos generadores, P y Q. Las igualdades I = P e I = Q se llaman relaciones generadoras. Los signos de P y Q determinan cuál de las cuatro fracciones se obtiene; las cuatro forman una familia, y la que tiene P y Q positivos es la fracción principal.

La relación de definición completa contiene todas las columnas iguales a la identidad: P, Q y su producto PQ, que se llama interacción generalizada. Así, I = P = Q = PQ, y cada efecto tiene tres alias: se obtienen multiplicando el efecto por cada una de las tres palabras. Hay que elegir los generadores de modo que los efectos que pueden ser importantes no queden aliados entre sí.""",
  left=[form("I = P = Q = PQ", size=30),
        bul("**2^{k−2}** corridas: la cuarta parte del 2^{k}",
            "Dos generadores **P** y **Q**: relaciones generadoras I = P e I = Q",
            "**PQ**: interacción generalizada (producto, letra² = I)",
            "Cada efecto tiene **tres alias**", size=16)],
  right=[tab(["Signos de los generadores", "Fracción"],
             [["+P,  +Q", "Principal"], ["+P,  −Q", "Alterna"], ["−P,  +Q", "Alterna"], ["−P,  −Q", "Alterna"]],
             size=16, colw=[0.55, 0.45], first_left=False),
         note("Las cuatro fracciones forman una **familia**: juntas son el 2^{k} completo", size=15)], ratio=0.5)

S("El 2^{6−2}_{IV}: relación de definición y alias",
  """Para una fracción 1/4 se necesitan dos generadores, P y Q. Su producto PQ, la interacción generalizada, también pertenece a la relación de definición: I = P = Q = PQ. Cada efecto tiene entonces tres alias.

Ejemplo: 2^{6−2} con E = ABC y F = BCD. Las palabras son ABCE, BCDF y su producto ADEF. La palabra más corta tiene cuatro letras, así que es resolución IV: los efectos principales son alias de interacciones de tres y cinco factores, y las interacciones dobles son alias entre sí y de interacciones de orden superior. Las 15 cadenas son seis de efectos principales, siete de interacciones dobles y dos formadas solo por interacciones triples.

Construcción: se escribe el 2^{4} completo en A, B, C y D (16 corridas) y se agregan las columnas E = ABC y F = BCD.""",
  left=[bul("Dos generadores **P** y **Q**; su producto **PQ** también es palabra",
            "Cada efecto tiene **tres alias**"),
        form("I = P = Q = PQ", "2^{6−2}:  E = ABC,  F = BCD", "I = ABCE = BCDF = ADEF", size=19),
        note("Palabra más corta: 4 letras  →  **resolución IV**")],
  right=[tab(["Efectos principales", "Interacciones de 2 factores"],
             [["A = BCE = DEF", "AB = CE"], ["B = ACE = CDF", "AC = BE"],
              ["C = ABE = BDF", "AD = EF"], ["D = BCF = AEF", "AE = BC = DF"],
              ["E = ABC = ADF", "AF = DE"], ["F = BCD = ADE", "BD = CF"], ["", "BF = CD"]],
             size=15, first_left=False),
         txt("Faltan dos cadenas, solo de interacciones triples: ABD = CDE = ACF = BEF y ACD = BDE = ABF = CEF", size=13)], ratio=0.48)

_rows = [[str(i + 1), sg(r["A"]), sg(r["B"]), sg(r["C"]), sg(r["D"]), sg(r["E"]), sg(r["F"])]
         for i, r in enumerate(r3)]
S("¿Cómo se construye el 2^{6−2}?",
  """Se usa el método del diseño básico. Primero se escribe el factorial completo en k − 2 = 4 factores, A, B, C y D: tiene las 16 corridas necesarias pero solo cuatro columnas. Después se agregan los dos factores restantes asociando sus signos a dos interacciones elegidas de los primeros cuatro: E = ABC y F = BCD. Esto equivale a las relaciones generadoras I = ABCE e I = BCDF.

Montgomery da otra forma de verlo: se divide el 2^{6} en cuatro bloques confundiendo ABCE y BCDF, y se elige el bloque en que las dos son positivas. Ese bloque es la fracción principal.

La tabla es la del libro (tabla 8-9) y es el diseño que se usa en el ejemplo 3.""",
  left=[tab(["Corrida", "A", "B", "C", "D", "E = ABC", "F = BCD"], _rows, size=12, first_left=False, pad=0.08)],
  right=[num("Escribir el **2^{4} completo** en A, B, C, D (diseño básico)",
             "Agregar **E = ABC** y **F = BCD**",
             "Con todos los signos positivos: **fracción principal**", size=16),
         form("I = ABCE,   I = BCDF", size=20),
         note("Alternativa: 4 bloques del 2^{6} con ABCE y BCDF confundidas; se toma el bloque en que ambas son +", size=14)],
  ratio=0.52)

S("¿Cuáles son las fracciones alternas del 2^{6−2}?",
  """Además de la principal hay tres fracciones alternas, una por cada combinación de signos negativos en los generadores. Se construyen con el mismo diseño básico, cambiando el signo de la columna correspondiente. Por ejemplo, para la fracción con I = ABCE e I = −BCDF se usa F = −BCD, y la columna de F queda + + − − − − + + − − + + + + − −.

Al cambiar el signo de un generador cambia también el de la interacción generalizada: la relación de definición de esa fracción es I = ABCE = −BCDF = −ADEF. Los alias se obtienen igual, arrastrando los signos: A = BCE = −DEF = −ABCDF, de modo que ℓ_{A} estima en realidad A + BCE − DEF − ABCDF.""",
  body=[tab(["Generadores", "Cómo se construye", "Relación de definición completa"],
            [["I = ABCE,  I = BCDF", "E = ABC,  F = BCD", "I = ABCE = BCDF = ADEF  (principal)"],
             ["I = ABCE,  I = −BCDF", "E = ABC,  F = −BCD", "I = ABCE = −BCDF = −ADEF"],
             ["I = −ABCE,  I = BCDF", "E = −ABC,  F = BCD", "I = −ABCE = BCDF = −ADEF"],
             ["I = −ABCE,  I = −BCDF", "E = −ABC,  F = −BCD", "I = −ABCE = −BCDF = ADEF"]],
            size=16, colw=[0.3, 0.3, 0.4], hl=[1]),
        form("Con F = −BCD:   A = BCE = −DEF = −ABCDF   ⇒   ℓ_{A} → A + BCE − DEF − ABCDF", size=17),
        note("El signo de la interacción generalizada es el **producto** de los signos de los generadores", size=15)])

S("¿Cómo se sabe qué factores importan antes de correr?",
  """No hace falta saberlo. Antes de experimentar nadie sabe cuáles factores son activos; eso es justamente lo que el experimento va a averiguar. Lo que se decide antes son supuestos generales, y lo que se averigua después sale de la misma fracción.

Antes de correr: se aceptan dos principios. Escasez de efectos: en la mayoría de los procesos solo unos pocos factores importan, aunque no se sepa cuáles. Jerarquía: las interacciones de tres o más factores casi siempre son despreciables. Con eso se elige la resolución; con resolución IV, todo efecto principal sale libre de las interacciones dobles, sea cual sea el factor que resulte activo. Si el ingeniero sospecha que algunos factores importan más, los asigna a columnas que no formen una palabra, por ejemplo a las del diseño básico.

Se corre una sola vez la fracción. No se necesita el factorial completo: con las 16 corridas del 2^{6−2} se calculan 15 contrastes, uno por cadena de alias, y esos 15 efectos van a la gráfica de Daniel.

Después de correr: la gráfica dice qué factores son activos. Recién entonces se pregunta qué diseño forman las corridas ya hechas en esos factores; eso es la proyección. Si los activos no forman una palabra, se tiene un factorial completo en ellos. Si forman una palabra, queda alguna ambigüedad entre alias, y se resuelve agregando corridas (fracción alterna o doblez) que se suman a las ya hechas.""",
  left=[cards(("1 · Antes de correr", "Supuestos: **escasez de efectos** y **jerarquía**  →  se elige la **resolución** y la asignación de columnas"),
              ("2 · Se corre la fracción", "**Una sola vez**: 2^{k−p} corridas, sin el factorial completo"),
              ("3 · Gráfica de Daniel", "Con los efectos de la **propia fracción** se ve qué factores son activos"),
              ("4 · Proyección", "¿Qué diseño forman las corridas **ya hechas** en los factores activos?"),
              size=15, cols=2)],
  right=[tab(["Los activos…", "Resultado"],
             [["**No** forman una palabra", "Factorial **completo** en ellos: listo"],
              ["**Sí** forman una palabra", "Ambigüedad entre alias  →  **doblez** o fracción alterna"]],
             size=15, colw=[0.45, 0.55]),
         note("La proyección **no se planea**: es lo que vale lo ya corrido una vez se sabe qué importa", size=15),
         note("Las corridas nuevas **se suman** a las anteriores: nunca se empieza de cero", size=15)],
  ratio=0.55)

# Ejemplo didáctico: 2^(3-1) con I = ABC, datos sin ruido
def _cafe(m, runs):
    return [m(*r) for r in runs]


_fp = [(1, -1, -1), (-1, 1, -1), (-1, -1, 1), (1, 1, 1)]          # a, b, c, abc  (I = +ABC)
_fa = [(-1, -1, -1), (1, 1, -1), (1, -1, 1), (-1, 1, 1)]          # (1), ab, ac, bc (I = −ABC)
_lp, _la = ["a", "b", "c", "abc"], ["(1)", "ab", "ac", "bc"]
_m1 = lambda A, B, C: 70 + 5 * A + 3 * B
_m2 = lambda A, B, C: 70 + 5 * A + 3 * B + 4 * A * B


_g = lambda v: f(v, 0)


def _ell(runs, ys, j):
    return sum(r[j] * y for r, y in zip(runs, ys)) / 2


_y1, _y2, _y2a = _cafe(_m1, _fp), _cafe(_m2, _fp), _cafe(_m2, _fa)
E("didáctico", "el sabor de un café", "ejemplo construido para la clase, con datos inventados",
  ["Una tienda de café quiere mejorar el **puntaje de sabor** de su bebida (0 a 100, promedio de un panel de catadores). Se sospecha de tres factores, cada uno a dos niveles: A temperatura del agua (88 o 96 °C), B molienda (gruesa o fina) y C tiempo de infusión (3 o 4 min).",
   "Cada preparación consume un lote de café y una sesión del panel, así que solo hay presupuesto para **4 corridas**, la mitad de las 8 del factorial 2^{3}. Se corre la fracción un medio con **C = AB** (I = ABC): las preparaciones a, b, c y abc. Si hace falta, más adelante se pueden pagar 4 corridas más.",
   "Se analizan dos situaciones posibles. **Caso 1**: el tiempo de infusión no influye en el sabor. **Caso 2**: el tiempo de infusión tampoco influye, pero la temperatura y la molienda interactúan. El experimentador no sabe cuál de las dos es la real; solo ve los cuatro puntajes."],
  "Ver, con cuentas a mano, qué se puede concluir con 4 corridas, cuándo la **proyección** basta y cuándo hace falta un **doblez**",
  ["Escribir la fracción, la palabra y los alias", "Caso 1: calcular los contrastes y proyectar en A y B",
   "Caso 2: identificar la ambigüedad entre C y AB", "Caso 2: correr la fracción alterna y separar C de AB"])

S("Ejemplo didáctico · Una fracción pequeña y su notación",
  """Para ver la proyección y el doblez con cuentas a mano se usa la fracción más pequeña posible. Se quiere mejorar el puntaje de sabor de un café (escala 0 a 100) y se estudian tres factores a dos niveles: A temperatura del agua (88 o 96 °C), B molienda (gruesa o fina) y C tiempo de infusión (3 o 4 min). El factorial completo 2^{3} tiene 8 corridas; se corre la mitad, 4 corridas, con C = AB, es decir I = ABC.

Notación. Cada factor se codifica x = −1 en el nivel bajo y x = +1 en el alto. Una corrida se nombra con las letras de los factores que están en nivel alto: a es A alto y B, C bajos; abc es todo alto; (1) es todo bajo. La palabra ABC dice que en todas las corridas x_{A}x_{B}x_{C} = +1. Por eso la columna de A coincide con la de BC, la de B con AC y la de C con AB: son alias.

ℓ_{A} es el contraste de la columna A dividido entre 2, es decir el promedio de las corridas con A alto menos el de las corridas con A bajo. La flecha ℓ_{A} → A + BC se lee «ℓ_{A} estima la suma del efecto de A y el de la interacción BC»: con estos datos no se pueden separar.

Los datos de los dos casos que siguen son inventados y sin error experimental, para que las cuentas den números redondos. Con datos reales habría ruido, y por eso en la práctica se usan fracciones más grandes y la gráfica de Daniel.""",
  left=[tab(["Factor", "Nivel bajo (x = −1)", "Nivel alto (x = +1)"],
            [["A  Temperatura del agua", "88 °C", "96 °C"], ["B  Molienda", "gruesa", "fina"],
             ["C  Tiempo de infusión", "3 min", "4 min"]], size=14, colw=[0.42, 0.29, 0.29]),
        tab(["Corrida", "A", "B", "C = AB"],
            [[l, sg(r[0]), sg(r[1]), sg(r[2])] for l, r in zip(_lp, _fp)], size=15, first_left=False),
        txt("Respuesta: **puntaje de sabor** (0 a 100). Datos ilustrativos, sin error.", size=13)],
  right=[tab(["Símbolo", "Significa"],
             [["x = −1, +1", "Nivel bajo, nivel alto"],
              ["a, abc, (1)", "Letras de los factores en **alto**; (1) = todos bajos"],
              ["I = ABC", "x_{A}x_{B}x_{C} = +1 en **todas** las corridas"],
              ["A = BC", "Columnas idénticas: **alias**"],
              ["ℓ_{A}", "Promedio con A alto − promedio con A bajo"],
              ["ℓ_{A} → A + BC", "ℓ_{A} estima la **suma** de los dos efectos"],
              ["ℓ′_{A}", "Lo mismo, calculado en la **segunda** fracción"]],
             size=14, colw=[0.32, 0.68])],
  ratio=0.48)

S("Caso 1 · C no influye: la proyección",
  f"""Suponga que el sabor responde así (el experimentador no lo sabe): y = 70 + 5x_{{A}} + 3x_{{B}}. Es decir, A sube el puntaje en 10 puntos al pasar de bajo a alto, B lo sube en 6, y C no hace nada. Las cuatro corridas dan a = {_y1[0]}, b = {_y1[1]}, c = {_y1[2]} y abc = {_y1[3]}.

Los contrastes: ℓ_{{A}} = (a + abc − b − c)/2 = ({_y1[0]} + {_y1[3]} − {_y1[1]} − {_y1[2]})/2 = {_g(_ell(_fp, _y1, 0))}, que estima A + BC. ℓ_{{B}} = (b + abc − a − c)/2 = {_g(_ell(_fp, _y1, 1))}, que estima B + AC. ℓ_{{C}} = (c + abc − a − b)/2 = {_g(_ell(_fp, _y1, 2))}, que estima C + AB.

Lectura: ℓ_{{C}} = 0, así que C no influye (y AB tampoco, o tendrían que cancelarse exactamente, lo que es muy improbable). Se borra la columna C. En las columnas A y B quedan las cuatro combinaciones (+, −), (−, +), (−, −) y (+, +), cada una una vez: la fracción se proyectó en un 2^{{2}} completo en A y B. Como A y B no forman una palabra (la única palabra es ABC), el resultado es un factorial completo, y ℓ_{{A}} = 10 y ℓ_{{B}} = 6 se atribuyen a A y B.""",
  left=[form("Verdad oculta:  y = 70 + 5x_{A} + 3x_{B}", size=17),
        tab(["Corrida", "A", "B", "C", "Sabor y"],
            [[l, sg(r[0]), sg(r[1]), sg(r[2]), str(y)] for l, r, y in zip(_lp, _fp, _y1)], size=15, first_left=False),
        tab(["Contraste", "Cuenta", "Valor", "Estima"],
            [["ℓ_{A}", "(a + abc − b − c)/2", f"{_g(_ell(_fp, _y1, 0))}", "A + BC"],
             ["ℓ_{B}", "(b + abc − a − c)/2", f"{_g(_ell(_fp, _y1, 1))}", "B + AC"],
             ["ℓ_{C}", "(c + abc − a − b)/2", f"{_g(_ell(_fp, _y1, 2))}", "C + AB"]], size=14, first_left=False)],
  right=[txt("**Se borra C** y se miran solo A y B", size=17),
         tab(["Corrida", "A", "B"],
             [[l, sg(r[0]), sg(r[1])] for l, r in zip(_lp, _fp)], size=15, first_left=False),
         note("Las 4 combinaciones de A y B, una vez cada una: **2^{2} completo**", size=15),
         note("A y B **no** forman palabra  →  no hay ambigüedad: A = 10, B = 6", size=15)],
  ratio=0.55)

S("Caso 2 · ¿Es C o es AB? Una ambigüedad",
  f"""Ahora suponga que la verdad oculta es y = 70 + 5x_{{A}} + 3x_{{B}} + 4x_{{A}}x_{{B}}: C sigue sin hacer nada, pero A y B interactúan (la molienda fina rinde más cuando el agua está caliente). Las mismas cuatro corridas dan a = {_y2[0]}, b = {_y2[1]}, c = {_y2[2]} y abc = {_y2[3]}.

Los contrastes son ℓ_{{A}} = {_g(_ell(_fp, _y2, 0))}, ℓ_{{B}} = {_g(_ell(_fp, _y2, 1))} y ℓ_{{C}} = {_g(_ell(_fp, _y2, 2))}. Los tres son grandes, y aquí aparece el problema: ℓ_{{C}} = 8 estima C + AB. Hay dos explicaciones igual de lógicas: o el tiempo de infusión C sube el sabor en 8 puntos, o C no hace nada y lo que se ve es la interacción AB. Con estas cuatro corridas no hay forma de distinguirlas.

La razón es que los tres factores aparentemente activos, A, B y C, forman la palabra ABC. Si se intenta proyectar en A, B y C, solo están 4 de las 8 combinaciones del 2^{{3}}: las que cumplen x_{{A}}x_{{B}}x_{{C}} = +1. No hay proyección en un factorial completo, y la duda solo se resuelve corriendo las combinaciones que faltan.""",
  left=[form("Verdad oculta:  y = 70 + 5x_{A} + 3x_{B} + 4x_{A}x_{B}", size=16),
        tab(["Corrida", "A", "B", "C", "Sabor y"],
            [[l, sg(r[0]), sg(r[1]), sg(r[2]), str(y)] for l, r, y in zip(_lp, _fp, _y2)], size=15, first_left=False),
        tab(["Contraste", "Valor", "Estima"],
            [["ℓ_{A}", f"{_g(_ell(_fp, _y2, 0))}", "A + BC"], ["ℓ_{B}", f"{_g(_ell(_fp, _y2, 1))}", "B + AC"],
             ["ℓ_{C}", f"{_g(_ell(_fp, _y2, 2))}", "**C + AB**"]], size=15, hl=[2], first_left=False)],
  right=[cards(("Explicación 1", "**C** (tiempo de infusión) sube el sabor 8 puntos"),
               ("Explicación 2", "C no hace nada; es la interacción **AB** (temperatura × molienda)"),
               size=15, cols=1),
         note("A, B y C forman la palabra **ABC**: solo se corrieron 4 de las 8 combinaciones  →  no se pueden separar", size=15)],
  ratio=0.52)

_rows = []
for j, (w, al) in enumerate([("A", "BC"), ("B", "AC"), ("C", "AB")]):
    lp, la = _ell(_fp, _y2, j), _ell(_fa, _y2a, j)
    _rows.append([w, f"{_g(lp)}", f"{_g(la)}", f"{w} = {_g((lp + la) / 2)}", f"{al} = {_g((lp - la) / 2)}"])
S("Caso 2 · El doblez resuelve la duda",
  f"""Se corren las cuatro combinaciones que faltaban: (1), ab, ac y bc. Es la fracción alterna, I = −ABC (C = −AB). En una fracción 2^{{3−1}} coincide con el doblez completo: se obtiene invirtiendo todos los signos de la primera (a = (+, −, −) pasa a ser (−, +, +) = bc). Los resultados son (1) = {_y2a[0]}, ab = {_y2a[1]}, ac = {_y2a[2]} y bc = {_y2a[3]}.

En la segunda fracción los alias cambian de signo, porque ahora x_{{A}}x_{{B}}x_{{C}} = −1: ℓ′_{{C}} estima C − AB, ℓ′_{{A}} estima A − BC y ℓ′_{{B}} estima B − AC. Se obtiene ℓ′_{{C}} = {_g(_ell(_fa, _y2a, 2))}.

Combinando: ½(ℓ_{{C}} + ℓ′_{{C}}) = ½(8 − 8) = 0 es el efecto de C, y ½(ℓ_{{C}} − ℓ′_{{C}}) = ½(8 + 8) = 8 es la interacción AB. La duda queda resuelta: C no influye y lo que se veía era la interacción entre temperatura y molienda. De paso, A = 10 y B = 6, con BC = AC = 0.

Las 8 corridas juntas forman el 2^{{3}} completo. Las primeras cuatro no se desperdiciaron: se usaron en la combinación. Así funciona la experimentación secuencial.""",
  left=[tab(["Corrida", "A", "B", "C = −AB", "Sabor y"],
            [[l, sg(r[0]), sg(r[1]), sg(r[2]), str(y)] for l, r, y in zip(_la, _fa, _y2a)], size=15, first_left=False),
        form("½ (ℓ + ℓ′) → el efecto principal", "½ (ℓ − ℓ′) → su alias", size=17)],
  right=[tab(["Columna", "ℓ  (I = ABC)", "ℓ′  (I = −ABC)", "½ (ℓ + ℓ′)", "½ (ℓ − ℓ′)"], _rows, size=15,
             hl=[2], first_left=False),
         form("ℓ′_{C} → C − AB  (en la segunda fracción x_{A}x_{B}x_{C} = −1)", size=15),
         note("C = 0 y **AB = 8**: era la interacción, no el tiempo de infusión", size=15),
         note("4 + 4 corridas = **2^{3} completo**; nada se desperdició", size=15)],
  ratio=0.44)

def _proy(sub):
    """Combinaciones distintas de signos de las columnas `sub` del 2^{6−2} y las corridas en que aparecen."""
    d = {}
    for i, r in enumerate(r3):
        d.setdefault(tuple(r[x] for x in sub), []).append(i + 1)
    return sorted(d.items(), key=lambda kv: kv[1][0])


_pABC = _proy("ABC")
S("¿Qué significa proyectar un fraccionado?",
  """Proyectar es lo que pasa con el diseño cuando, después del análisis, algunos factores resultan inactivos. Si un factor no influye en la respuesta, su columna ya no sirve para explicar nada y se puede borrar. Lo que queda son las columnas de los factores activos, y la pregunta es qué diseño forman esas columnas por sí solas.

Para saberlo basta contar: se miran las 16 corridas solo en las columnas que quedan y se anota cuántas veces aparece cada combinación de signos.

Ejemplo con el 2^{6−2} (E = ABC, F = BCD). Suponga que solo A, B y C importan. Se borran D, E y F. En las columnas A, B y C aparecen las ocho combinaciones del 2^{3}, y cada una exactamente dos veces: la corrida 1 y la 9 son (−, −, −), la 2 y la 10 son (+, −, −), y así sucesivamente. Las 16 corridas son entonces dos réplicas completas de un 2^{3}.

Eso tiene una consecuencia práctica: las dos corridas de cada par se hicieron en las mismas condiciones de A, B y C, así que su diferencia es error puro. El fraccionado no replicado se convierte en un factorial replicado con 16 − 8 = 8 grados de libertad para el error, y el ANOVA ya no depende de descartar efectos.""",
  left=[num("Decidir qué factores son **inactivos**",
            "**Borrar** sus columnas de la tabla del diseño",
            "**Contar** cuántas veces aparece cada combinación de signos en las columnas que quedan",
            "Leer el diseño que resulta: ¿están **todas** las combinaciones? ¿cuántas veces?", size=16),
        note("2^{6−2} con solo A, B, C activos: **8 combinaciones × 2 veces** = dos réplicas de un 2^{3}  →  **8 g.l. de error puro**", size=15)],
  right=[tab(["A", "B", "C", "Corridas", "Veces"],
             [[sg(k[0]), sg(k[1]), sg(k[2]), " y ".join(map(str, v)), str(len(v))] for k, v in _pABC],
             size=15, first_left=False),
         txt("Corridas numeradas como en la tabla del 2^{6−2} (E = ABC, F = BCD)", size=12)],
  ratio=0.5)

_pABCE = _proy("ABCE")
S("¿Por qué importa si los factores forman una palabra?",
  """Con cuatro factores activos el resultado depende de cuáles sean. Hay 2^{4} = 16 combinaciones posibles y 16 corridas, así que solo hay dos posibilidades: o aparecen todas una vez (factorial completo) o aparece la mitad dos veces (fracción replicada).

Si los cuatro factores son A, B, C y D, se obtienen las 16 combinaciones, una vez cada una: es el diseño básico. Lo mismo pasa con un subconjunto menos obvio, como A, B, E y F: también aparecen las 16 combinaciones.

Pero si los cuatro factores son A, B, C y E, solo aparecen 8 combinaciones, dos veces cada una. La razón es que ABCE es una palabra de la relación de definición: en todas las corridas el producto de los signos de A, B, C y E vale +1, porque E se construyó como ABC. Conocidos A, B y C, el signo de E queda fijado, y las combinaciones con E distinto de ABC nunca se corren. El resultado son dos réplicas de un 2^{4−1} con I = ABCE, y en él E sigue confundido con ABC.

Regla: un subconjunto de factores se proyecta en un factorial completo si no contiene ninguna palabra de la relación de definición. Por eso, al asignar factores a columnas, conviene que los que se creen más importantes no formen una palabra.""",
  left=[tab(["A", "B", "C", "E", "Corridas", "Veces"],
            [[sg(k[0]), sg(k[1]), sg(k[2]), sg(k[3]), " y ".join(map(str, v)), str(len(v))] for k, v in _pABCE],
            size=14, first_left=False),
        note("En todas las filas **E = A·B·C**: falta la mitad de las combinaciones", size=14)],
  right=[tab(["Factores activos", "¿Es palabra?", "Comb. × veces", "Diseño"],
             [["A, B, C, D", "No", "16 × 1", "**2^{4}** completo"],
              ["A, B, E, F", "No", "16 × 1", "**2^{4}** completo"],
              ["A, B, C, E", "Sí (ABCE)", "8 × 2", "2 réplicas de **2^{4−1}**"]],
             size=14, colw=[0.25, 0.2, 0.22, 0.33], hl=[2]),
         form("ABCE palabra  ⇒  x_{A}x_{B}x_{C}x_{E} = +1 siempre", "⇒  E queda fijado por A, B y C", size=16),
         note("Factorial completo ⇔ el subconjunto **no contiene una palabra**", size=15)],
  ratio=0.48)

S("Resumen: ¿en qué se proyecta el 2^{6−2}?",
  """Esta tabla resume lo que se obtiene al contar combinaciones en cada tamaño de subconjunto, como en las dos diapositivas anteriores. Un 2^{k−2} se pliega en un factorial completo o en un fraccionado en cualquier subconjunto de r ≤ k − 2 factores. La diferencia la marca la relación de definición: los subconjuntos que forman factoriales completos son los que no son palabras de ella.

Para el 2^{6−2} con I = ABCE = BCDF = ADEF hay 15 subconjuntos de cuatro factores. Tres son palabras (ABCE, BCDF y ADEF), y en ellos el diseño se pliega en dos réplicas de un 2^{4−1}. En los otros doce, como ABCD o ABCF, se proyecta en una réplica de un 2^{4} completo.

En cualquier subconjunto de tres factores se proyecta en dos réplicas de un 2^{3}: como el diseño es de resolución IV, ninguna palabra tiene tres letras, así que ningún trío queda amarrado. En cualquier par de factores se proyecta en cuatro réplicas de un 2^{2}.""",
  left=[tab(["Subconjunto de factores", "Se proyecta en…"],
             [["4 factores que **no** son palabra (12, p. ej. ABCD)", "Una réplica de un **2^{4} completo**"],
              ["4 factores que **sí** son palabra (ABCE, BCDF, ADEF)", "Dos réplicas de un **2^{4−1}**"],
              ["Cualesquiera 3 factores", "Dos réplicas de un **2^{3}**"],
              ["Cualesquiera 2 factores", "Cuatro réplicas de un **2^{2}**"]],
             size=15, colw=[0.55, 0.45])],
  right=[form("Subconjunto que **no** es palabra ⇒ factorial completo", size=18),
         bul("En general: completo o fraccionado en cualquier subconjunto de **r ≤ k − 2** factores",
             "Por eso conviene que los factores que se creen importantes **no formen una palabra**", size=16),
         note("De los 15 subconjuntos de 4 factores: **12** dan un 2^{4} completo y **3** (las palabras) dan un 2^{4−1} replicado", size=15),
         note("En el ejemplo 3 solo A y B resultan activos: el 2^{6−2} queda en **cuatro réplicas de un 2^{2}**", size=15)],
  ratio=0.56)

E(3, "contracción en moldeo por inyección", "Montgomery, ejemplo 8-4",
  ["Las piezas fabricadas en un proceso de moldeo por inyección presentan una **contracción excesiva**, y eso causa problemas en las operaciones de ensamble posteriores.",
   "Un equipo de mejora de la calidad decide estudiar el proceso con un experimento diseñado. Investiga seis factores a dos niveles: A temperatura del molde, B velocidad del tornillo, C tiempo de retención, D duración del ciclo, E tamaño de la compuerta (vaciadero) y F presión de retención. La respuesta es la contracción (× 10).",
   "El factorial completo serían 64 corridas. El equipo usa un **2^{6−2} de 16 corridas**, con E = ABC y F = BCD, corridas en orden aleatorio."],
  "Aprender cómo afecta cada factor la contracción, **algo de cómo interactúan** y cómo **reducirla**",
  ["Escribir la relación de definición y la resolución", "Identificar los efectos activos y sus alias",
   "Ajustar el modelo y hacer el ANOVA", "Proyectar en los factores activos e interpretar la interacción"])

_v3 = [ef3[w][1] for w in w3]
_z3 = normal_scores(_v3)
_s3 = sorted(range(15), key=lambda i: _v3[i])
_p3 = [(_v3[i], _z3[i]) for i in _s3]
_act3 = {k for k, i in enumerate(_s3) if w3[i] in ("A", "B", "AB")}
_lab3 = {k: (w3[i] if w3[i] == "ABF" else lab3.get(w3[i], w3[i])) for k, i in enumerate(_s3) if w3[i] in ("A", "B", "AB", "AD", "ABF")}
pse3 = lenth(_v3); me3 = t_ppf(0.05, 15 / 3) * pse3; sme3 = t_ppf(1 - 0.95 ** (1 / 15), 15 / 3) * pse3
_top3 = sorted(w3, key=lambda w: -abs(ef3[w][1]))[:8]
S("Ejemplo 3 · ¿Qué efectos son activos?",
  f"""El diseño tiene 16 corridas y una sola réplica, así que no hay error puro: los 15 grados de libertad se gastan en 15 contrastes, uno por cadena de alias. Para decidir cuáles son reales, Montgomery usa la gráfica de probabilidad normal de los efectos (fig. 8-12). Aquí se le agrega la recta de Daniel, ajustada con los efectos pequeños, y el diagrama de Pareto.

Cómo se lee. Los efectos nulos son solo ruido y caen sobre la recta, alrededor de cero; un efecto real se aparta de ella. Tres se apartan con claridad: B, velocidad del tornillo (35.63); A, temperatura del molde (13.88); y la cadena AB + CE (11.88). Todos son positivos: suben la contracción.

¿Por qué AB y no CE? C y E no tienen efecto principal (−0.88 y 0.38). Por el principio de herencia, una interacción suele ser activa solo si alguno de sus factores lo es; A y B lo son, C y E no. Se atribuye la cadena a AB.

Dos efectos quedan en una zona gris: AD + EF (−5.38) y ABF (−4.88). Son mucho menores que los tres anteriores. El método de Lenth da PSE = {f(pse3, 4)}, ME = {f(me3)} y SME = {f(sme3)}: los dos superan el ME, y AD + EF apenas supera el SME. Montgomery los deja fuera del modelo. En AD + EF, de los cuatro factores solo A es activo; D, E y F no tienen efecto principal (1.38, 0.38 y 0.38). ABF es una cadena de interacciones triples, que por jerarquía se suponen despreciables. Además, su tamaño no cambia las conclusiones. Quedan en el error.

Primera clasificación para el ANOVA: al modelo A, B y AB; al error, los otros doce.""",
  left=[scatter(_p3, "Efecto", "Puntuación normal", h=4.2, labels=_lab3, line=daniel(_p3, _act3), hi=_act3,
                title="Gráfica normal con recta de Daniel (fig. 8-12)"),
        note("Al **modelo**: A, B y AB.  Al **error**: los otros 12 efectos", size=15)],
  right=[num("**Sobre la recta** = ruido: 10 efectos cerca de cero",
             "**Se apartan con claridad**: B = 35.63, A = 13.88 y AB + CE = 11.88",
             "**AB + CE se atribuye a AB**: A y B son activos; C (−0.88) y E (0.38) no",
             f"**Zona gris**: AD + EF = −5.38 y ABF = −4.88. Lenth: ME = {f(me3)}, SME = {f(sme3)}; mucho menores que los tres grandes, quedan en el error",
             size=14),
         bars([lab3.get(w, w).replace(" (+ alias)", "") for w in _top3], [abs(ef3[w][1]) for w in _top3], "|Efecto|", h=2.6, title="Pareto (los 8 mayores)")],
  ratio=0.5)

_rows = [[lab3.get(w, w), f(ef3[w][1], 3), f(ef3[w][2], 2)] for w in w3]          # las 15 cadenas, orden de la tabla 8-11
_an3 = [[t, f(ss, 2), "1", f(ss, 2), f(F), pv(p)] for t, ss, _, _, F, p in m3["anova"]]
_an3 += [["Error", f(m3["sse"], 2), str(m3["dfe"]), f(m3["mse"], 2), "", ""],
         ["Total", f(m3["sst"], 2), "15", "", "", ""]]
S("Ejemplo 3 · Modelo y ANOVA",
  f"""Con la clasificación anterior se ajusta el modelo con A, B y AB. La tabla de la izquierda muestra las 15 cadenas, como la tabla 8-11 del libro, con su efecto y su suma de cuadrados; las tres que entran al modelo están resaltadas. Los doce efectos descartados forman el error, con 12 grados de libertad: su SS suma 248.75.

El factor C también está en la tabla: su efecto es −0.875 y su SS 3.06, de modo que no cambia la contracción promedio y va al error.

Hipótesis para cada término: H_{{0}}: el efecto es cero; H_{{A}}: no lo es. Los tres términos tienen F_{{0}} muy por encima de F_{{0.05, 1, 12}} = {f(f_ppf(0.05, 1, 12))} y valores p menores que 0.001: se rechaza H_{{0}} en los tres. El modelo explica el {100 * m3['r2']:.2f} % de la variabilidad de la contracción.

Lectura de los coeficientes: cada coeficiente es la mitad del efecto. La contracción promedio es 27.31; subir la velocidad del tornillo (B) la aumenta 17.81 por encima del promedio, subir la temperatura (A) la aumenta 6.94, y cuando las dos están altas se suma otro 5.94. Para reducir la contracción conviene A y B en nivel bajo.

El libro no presenta esta tabla ANOVA; se calculó aquí a partir de los datos de la tabla 8-10. Fuente: Montgomery, ejemplo 8-4.""",
  left=[tab(["Cadena (tabla 8-11)", "Efecto", "SS"], _rows, size=12, hl=[0, 1, 6], first_left=False, pad=0.05),
        note("A, B y AB explican **6411 de 6659** de la SS total. C (−0.875) es ruido", size=13)],
  right=[tab(["SV", "SS", "DF", "MS", "F_{0}", "P-Value"], _an3, size=15),
         form("ŷ = 27.31 + 6.94 x_{1} + 17.81 x_{2} + 5.94 x_{1}x_{2}", size=16),
         bul(f"F_{{0}} > F_{{0.05, 1, 12}} = {f(f_ppf(0.05, 1, 12))} en los tres: **se rechaza H_{{0}}**",
             f"R^{{2}} = {100 * m3['r2']:.2f} %",
             "Coeficiente = efecto / 2. Para **reducir** la contracción: **A y B bajos**", size=15)],
  ratio=0.42)

_cel3 = []
for _b in (-1, 1):
    for _a in (-1, 1):
        _v = [yy for yy, rr in zip(y3, r3) if rr["A"] == _a and rr["B"] == _b]
        _cel3.append([sg(_a), sg(_b), ",  ".join(map(str, _v)), f(sum(_v) / 4, 2)])
S("Ejemplo 3 · Proyección en A y B e interacción",
  f"""Solo A y B resultaron activos, así que C, D, E y F se pueden borrar del diseño. Al contar combinaciones en las columnas de A y B, cada una de las cuatro aparece cuatro veces: el 2^{{6−2}} se proyecta en cuatro réplicas de un 2^{{2}}, como dice la regla para cualquier par de factores de un diseño de resolución IV. La tabla muestra las cuatro contracciones de cada combinación y su promedio.

Esa proyección explica el ANOVA anterior: con cuatro réplicas por combinación hay 4 × 3 = 12 grados de libertad de error puro, los mismos 12 del ANOVA del modelo A, B y AB.

La gráfica de interacción se construye con los cuatro promedios. Con la velocidad del tornillo baja (B −) la contracción es pequeña y casi no depende de la temperatura: {f(ab3[(-1, -1)], 2)} y {f(ab3[(1, -1)], 2)}. Con B alta es grande y muy sensible a la temperatura: {f(ab3[(-1, 1)], 2)} y {f(ab3[(1, 1)], 2)}. Las rectas no son paralelas: eso es la interacción AB. La recomendación para reducir la contracción es trabajar con A y B en nivel bajo. Fuente: Montgomery, ejemplo 8-4 (fig. 8-13).""",
  left=[tab(["A", "B", "Las 4 corridas (contracción)", "Promedio"], _cel3, size=15, hl=[0], first_left=False,
            colw=[0.12, 0.12, 0.5, 0.26]),
        note("Cada combinación de A y B aparece **4 veces**: cuatro réplicas de un **2^{2}**  →  **12 g.l.** de error puro", size=15),
        note("Así se obtienen los 12 g.l. del error del ANOVA", size=14)],
  right=[lines(["A bajo (−)", "A alto (+)"],
               [("B bajo (−)", [ab3[(-1, -1)], ab3[(1, -1)]]), ("B alto (+)", [ab3[(-1, 1)], ab3[(1, 1)]])],
               "Contracción promedio", h=3.9, title="Interacción AB (fig. 8-13)"),
         note("Con **B bajo** la contracción es pequeña a cualquier temperatura. Recomendación: **A y B bajos**", size=15)],
  ratio=0.5)

section(6, "El diseño 2^{k−p} general", "Elección, protocolo, análisis, supuestos, proyección y bloques")

S("El caso general 2^{k−p}",
  """Las reglas se generalizan. Con p generadores independientes, la relación de definición completa tiene 2^{p} − 1 palabras: los p generadores más todos sus productos. Cada efecto tiene 2^{p} − 1 alias. El diseño solo permite estimar 2^{k−p} − 1 cadenas de alias, una por cada grado de libertad.

La resolución es la longitud de la palabra más corta. Para construirlo se escribe el factorial completo en k − p factores y se agregan p columnas definidas por los generadores.""",
  body=[tab(["Concepto", "Regla"],
            [["Corridas", "N = 2^{k−p}"],
             ["Generadores independientes", "p"],
             ["Palabras de la relación de definición", "2^{p} − 1  (generadores y todos sus productos)"],
             ["Alias de cada efecto", "2^{p} − 1  (efecto × cada palabra)"],
             ["Cadenas de alias estimables", "2^{k−p} − 1  (una por grado de libertad)"],
             ["Resolución", "Longitud de la palabra más corta"],
             ["Construcción", "Factorial completo en k − p factores + p columnas generadas"]],
            size=17, colw=[0.4, 0.6])])

S("¿Qué generadores elijo?",
  """Primer criterio: máxima resolución. Segundo criterio, para desempatar entre diseños de igual resolución: aberración mínima, es decir, el menor número de palabras de longitud mínima.

La tabla compara tres diseños 2^{7−2} de resolución IV. El diseño C tiene una sola palabra de cuatro letras, frente a tres y dos de los diseños A y B; por eso deja menos interacciones dobles confundidas entre sí y es el preferido. En la práctica no hay que buscar los generadores: las tablas de diseños recomendados ya entregan el diseño de máxima resolución y aberración mínima, y el software estadístico trae generadores predeterminados.""",
  body=[tab(["", "Diseño A", "Diseño B", "Diseño C"],
            [["Generadores", "F = ABC,  G = BCD", "F = ABC,  G = ADE", "F = ABCD,  G = ABDE"],
             ["Relación de definición", "I = ABCF = BCDG = ADFG", "I = ABCF = ADEG = BCDEFG",
              "I = ABCDF = ABDEG = CEFG"],
             ["Longitud de las palabras", "4, 4, 4", "4, 4, 6", "4, 5, 5"],
             ["Cadenas de interacciones dobles aliadas", "7", "6", "3"]], size=16,
            colw=[0.25, 0.25, 0.25, 0.25]),
        num("**Máxima resolución**: la palabra más corta, lo más larga posible",
            "**Aberración mínima**: el menor número de palabras de longitud mínima", size=17),
        note("El diseño C tiene una sola palabra de 4 letras: es el de **aberración mínima**")])

S("Diseños recomendados hasta 32 corridas",
  """Esta tabla reúne los diseños de máxima resolución y aberración mínima para 3 a 8 factores con un máximo de 32 corridas. Se lee por filas: número de factores, diseño con su resolución, corridas y generadores. Todos los generadores admiten signo positivo o negativo; con todos positivos se obtiene la fracción principal.

Nota para quien coteje con el libro: la tabla 8-14 de Montgomery imprime el 2^{7−3} con resolución III. Es una errata: todas las palabras de su relación de definición tienen cuatro letras y el propio texto lo trata como resolución IV.""",
  body=[tab(["Factores", "Diseño", "Corridas", "Generadores"],
            [["3", "2^{3−1}_{III}", "4", "C = AB"],
             ["4", "2^{4−1}_{IV}", "8", "D = ABC"],
             ["5", "2^{5−1}_{V}", "16", "E = ABCD"],
             ["5", "2^{5−2}_{III}", "8", "D = AB,  E = AC"],
             ["6", "2^{6−1}_{VI}", "32", "F = ABCDE"],
             ["6", "2^{6−2}_{IV}", "16", "E = ABC,  F = BCD"],
             ["6", "2^{6−3}_{III}", "8", "D = AB,  E = AC,  F = BC"],
             ["7", "2^{7−2}_{IV}", "32", "F = ABCD,  G = ABDE"],
             ["7", "2^{7−3}_{IV}", "16", "E = ABC,  F = BCD,  G = ACD"],
             ["7", "2^{7−4}_{III}", "8", "D = AB,  E = AC,  F = BC,  G = ABC"],
             ["8", "2^{8−3}_{IV}", "32", "F = ABC,  G = ABD,  H = BCDE"],
             ["8", "2^{8−4}_{IV}", "16", "E = BCD,  F = ACD,  G = ABC,  H = ABD"]],
            size=14, colw=[0.13, 0.17, 0.13, 0.57], first_left=False)])

S("¿Cómo elijo un diseño para siete factores?",
  """Ejemplo 8-5 de Montgomery. Se tienen siete factores, interesa estimar los siete efectos principales y tener una idea de las interacciones dobles, y se está dispuesto a suponer despreciables las interacciones de tres o más factores. Eso pide resolución IV.

La tabla de diseños recomendados ofrece dos de resolución IV: el 2^{7−2} de 32 corridas y el 2^{7−3} de 16. En el de 16 corridas los siete efectos principales son alias de interacciones triples y las interacciones dobles quedan aliadas en grupos de tres: cumple el objetivo. El de 32 corridas permitiría además estimar de forma única 15 de las 21 interacciones dobles, más información de la que se necesita. Se elige el 2^{7−3}.

Se construye con el 2^{4} en A, B, C y D y las columnas E = ABC, F = BCD y G = ACD. La relación de definición completa tiene siete palabras, todas de cuatro letras.""",
  left=[tab(["", "2^{7−3}_{IV}", "2^{7−2}_{IV}"],
            [["Corridas", "16", "32"], ["Efectos principales", "Alias de triples", "Alias de triples o limpios"],
             ["Interacciones dobles", "En grupos de tres", "15 de 21 limpias"], ["¿Cumple el objetivo?", "Sí", "Sí, con información de sobra"]],
            size=15, colw=[0.36, 0.32, 0.32], hl=[0])],
  right=[form("E = ABC,  F = BCD,  G = ACD", size=19),
         form("I = ABCE = BCDF = ADEF = ACDG", "= BDEG = CEFG = ABFG", size=17),
         note("Se elige el diseño **más pequeño** que cumple el objetivo: el 2^{7−3} de 16 corridas", size=15)],
  ratio=0.5)

S("¿Cómo debo recolectar los datos?",
  """El protocolo experimental tiene ocho pasos. Se define la respuesta y los factores con sus dos niveles. Se decide qué interacciones se está dispuesto a despreciar, y de ahí sale la resolución necesaria. Se elige el diseño de la tabla y se revisa su estructura de alias antes de correr. Se asignan los factores reales a las letras cuidando que los más importantes no queden aliados entre sí. Se construye la matriz de diseño. Se aleatoriza el orden de las corridas. Se ejecuta registrando el orden real, y se planea desde el principio una corrida de confirmación o una segunda fracción.""",
  body=[num("Definir la **respuesta**, los **factores** y sus dos **niveles**",
            "Decidir qué interacciones se pueden despreciar  →  **resolución** requerida",
            "Elegir el diseño 2^{k−p} y **revisar sus alias** antes de correr",
            "**Asignar** los factores reales a las letras (los importantes, sin aliarse entre sí)",
            "Construir la **matriz de diseño**: diseño básico + columnas generadas",
            "**Aleatorizar** el orden de las corridas (dentro de bloques, si los hay)",
            "Ejecutar y **registrar el orden real** de corrida",
            "Planear la **confirmación**: corrida de verificación o segunda fracción", size=20)])

_rows = sorted([[str(o), str(i + 1), sg(r["A"]), sg(r["B"]), sg(r["C"]), sg(r["D"]), ""]
                for i, (r, o) in enumerate(zip(r1, orden))], key=lambda z: int(z[0]))
S("¿Cómo debo aleatorizar el diseño?",
  """Se sortea el orden en que se ejecutan las corridas, de modo que los efectos de variables no controladas (tiempo, desgaste, lote, operario) se repartan al azar y no se confundan con los factores. La tabla muestra un 2^{4−1} ya aleatorizado: la primera corrida que se ejecuta es la que el sorteo dejó en primer lugar, no la primera del orden estándar.

En cada corrida se reajustan todos los niveles, aunque coincidan con los de la corrida anterior. Se conserva el orden de corrida porque se necesita para verificar el supuesto de independencia. Si no es posible hacer todas las corridas en condiciones homogéneas, se forman bloques confundiendo con ellos una cadena de alias de orden alto.""",
  left=[bul("El orden de ejecución se **sortea**; no se corre en orden estándar",
            "En cada corrida se **reajustan** todos los niveles",
            "Se guarda el **orden de corrida**: se usa para verificar independencia",
            "Sin condiciones homogéneas: **bloques**, confundiendo una cadena de orden alto"),
        note("«Forme bloques con lo que pueda y aleatorice lo que no pueda» (Box, Hunter y Hunter)")],
  right=[tab(["Orden de corrida", "Orden estándar", "A", "B", "C", "D", "Respuesta"], _rows,
             size=15, first_left=False),
         txt("Ejemplo de orden aleatorio para un 2^{4−1} (D = ABC)", size=13)], ratio=0.45)

S("¿Cuál es el modelo matemático del diseño?",
  """El modelo es el mismo del factorial 2^{k}: un modelo de regresión en variables codificadas, donde cada x vale −1 o +1. β_{0} es la media general, y cada coeficiente se estima con la mitad del efecto correspondiente: β_{j} con la mitad del efecto principal del factor j y β_{ij} con la mitad del efecto de la interacción. El error ε se supone normal, independiente, con media cero y varianza constante σ².

La diferencia con el factorial completo es que no todos los términos se pueden estimar por separado. Cada columna del diseño estima una cadena de alias completa: el efecto que nos interesa más todos sus alias. El modelo final incluye un solo término por cada cadena que resulte activa, el que se juzga más razonable; las cadenas inactivas quedan fuera.""",
  body=[form("Y = β_{0} + Σ β_{j} x_{j} + ΣΣ β_{ij} x_{i} x_{j} + ε", "ε ~ NID(0, σ^{2})", size=24),
        bul("**x_{j}** = −1 (nivel bajo) o +1 (nivel alto) del factor j",
            "Se estiman así:  **β_{0}** con el promedio general;  **β_{j}** con efecto / 2;  **β_{ij}** con efecto de interacción / 2",
            "En la fracción cada columna estima una **cadena de alias**:  ℓ_{A} → A + BCD",
            "El modelo final lleva **un término por cada cadena activa**: el más razonable"),
        note("Se supone que las interacciones de orden alto de cada cadena son despreciables")])

S("¿Cuál es la hipótesis del diseño?",
  """Se plantea una hipótesis por cada cadena de alias que se quiere probar. La hipótesis nula dice que el efecto de la cadena es cero y la alterna que es distinto de cero.

Montgomery no plantea hipótesis en el capítulo de fraccionados; en el del 2^{k} plantea la hipótesis global de que todos los coeficientes son cero y luego prueba cada efecto con F. La formulación por cadena es la adaptación de esa idea al fraccionado.

Lo que realmente se prueba es la cadena completa: rechazar H_{0} para la columna de A significa que A + BCD es distinto de cero. Atribuirlo a A es una decisión del analista, apoyada en el supuesto de que BCD es despreciable.

Regla de decisión: se rechaza H_{0} si F_{0} supera el valor crítico F_{α, 1, gl del error}, o de forma equivalente si el valor p es menor que α = 0.05.""",
  left=[form("H_{0}: efecto de la cadena = 0", "H_{A}: efecto de la cadena ≠ 0", size=24),
        txt("Ejemplo, columna A del 2^{4−1}:   H_{0}: β_{A} + β_{BCD} = 0", size=16),
        form("Se rechaza H_{0} si  F_{0} > F_{α, 1, gl del error}", "o si  valor p < α", size=20)],
  right=[bul("Una hipótesis por cada **cadena de alias** que entra al modelo",
             "Se prueba la **cadena completa**: A + BCD, no A sola",
             "Si BCD es **despreciable**, equivale a  H_{0}: β_{A} = 0",
             "Nivel de significancia habitual: **α = 0.05**"),
         note("H_{0}: el factor no afecta la respuesta.  H_{A}: el factor sí la afecta.")])

S("¿Cómo debo analizar los datos recolectados?",
  """La ruta de análisis tiene siete pasos. Se calculan los contrastes y los efectos de todas las cadenas de alias. Se identifican los efectos activos: si no hay réplicas, con la gráfica de probabilidad normal o seminormal y el diagrama de Pareto. Se interpreta cada cadena activa para decidir a qué efecto se atribuye. Se ajusta el modelo reducido y se construye la tabla ANOVA, usando los efectos descartados como error. Se verifican los supuestos con los residuos. Se interpretan los efectos con gráficas de efectos principales, de interacción y de cubo. Por último se informa la conclusión en términos del problema del investigador y se confirma.

Es una adaptación del procedimiento de seis pasos que Montgomery da para el 2^{k}: estimar efectos, formar el modelo inicial, hacer las pruebas, refinar el modelo, analizar residuales e interpretar.""",
  body=[num("Calcular **contrastes y efectos** de todas las cadenas de alias",
            "Identificar los **efectos activos**: gráfica normal o seminormal y Pareto",
            "**Interpretar las cadenas** activas: ¿a qué efecto se atribuye cada una?",
            "Ajustar el **modelo reducido** y construir la **tabla ANOVA**",
            "**Verificar los supuestos** con los residuos",
            "Interpretar con gráficas de efectos principales, interacción y cubo",
            "Concluir **en términos del problema** y confirmar con nuevas corridas", size=20)])

_c, _e, _s = ef1["A"]
S("¿Qué estadísticos debo calcular?",
  """Para cada columna de signos se calculan cuatro cantidades. El contraste es la suma de las respuestas multiplicadas por los signos de la columna. El efecto es el contraste dividido entre N/2: la diferencia entre el promedio de la respuesta en el nivel alto y en el nivel bajo. El coeficiente de regresión es la mitad del efecto. La suma de cuadrados, con un grado de libertad, es el contraste al cuadrado dividido entre N.

La última columna muestra el cálculo para el factor A del ejemplo 1 (N = 8): contraste 76, efecto 19.00, coeficiente 9.50 y suma de cuadrados 722.""",
  body=[tab(["Estadístico", "Fórmula", "Qué mide", "Ejemplo 1, factor A (N = 8)"],
            [["Contraste", "Contraste_{i} = Σ (signo_{i}) · y", "Suma con signos de la columna i",
              "−45 + 100 − 45 + 65 − 75 + 60 − 80 + 96 = 76"],
             ["Efecto", "ℓ_{i} = Contraste_{i} / (N/2)", "Promedio en (+) menos promedio en (−)",
              f"76 / 4 = {f(_e)}"],
             ["Coeficiente", "β_{i} estimado = ℓ_{i} / 2", "Cambio en Y por unidad codificada", f"19.00 / 2 = {f(_e / 2)}"],
             ["Suma de cuadrados", "SS_{i} = (Contraste_{i})^{2} / N", "Variabilidad explicada (1 g.l.)",
              f"76^{{2}} / 8 = {f(_s, 1)}"]], size=16, colw=[0.16, 0.26, 0.27, 0.31]),
        note("Con una sola réplica, N = 2^{k−p}. El intercepto es el promedio general:  β_{0} = ȳ")])

S("Tabla ANOVA del factorial fraccionado",
  """Cada efecto que entra al modelo aporta una fila con un grado de libertad; su cuadrado medio es igual a su suma de cuadrados. El error se obtiene por sustracción: la suma de cuadrados total menos las de los m efectos del modelo, con N − 1 − m grados de libertad. Ese error está formado por los efectos que se juzgaron inactivos.

El estadístico de prueba de cada efecto es F_{0} = MS del efecto / MS del error, que se compara con F de 1 y N − 1 − m grados de libertad.

Si el diseño tiene n réplicas, N = n·2^{k−p} y el error incluye además el error puro, con 2^{k−p}(n − 1) grados de libertad.

Montgomery presenta esta tabla para el 2^{k} con réplicas; la versión para el fraccionado es la misma con N = 2^{k−p} y coincide con las ANOVA de sus ejemplos.""",
  body=[tab(["SV", "SS", "DF", "MS", "F_{0}"],
            [["Efecto i (cadena de alias)", "SS_{i} = (Contraste_{i})^{2} / N", "1", "MS_{i} = SS_{i}",
              "MS_{i} / MS_{E}"],
             ["Error", "SS_{E} = SS_{T} − Σ SS_{i}  (por sustracción)", "N − 1 − m", "SS_{E} / (N − 1 − m)", ""],
             ["Total", "SS_{T} = Σ y^{2} − (Σ y)^{2} / N", "N − 1", "", ""]],
            size=17, colw=[0.25, 0.33, 0.13, 0.17, 0.12]),
        bul("**m**: número de efectos incluidos en el modelo; **N**: total de corridas",
            "Se rechaza H_{0} si  **F_{0} > F_{α, 1, N−1−m}**  o si el valor p < α",
            "Con **n réplicas**:  N = n · 2^{k−p}  y hay error puro con 2^{k−p}(n − 1) g.l.", size=17)])

S("Sin réplicas no hay error: ¿cómo decido?",
  """Con una sola réplica, el modelo completo consume todos los grados de libertad y no queda error para hacer pruebas F. Hay tres herramientas.

La gráfica de probabilidad normal (o seminormal) de los efectos: los efectos inactivos se comportan como ruido normal de media cero y caen sobre una recta; los activos se alejan de ella.

El método de Lenth, que traza la línea de referencia del diagrama de Pareto: estima un pseudo error estándar (PSE) a partir de la mediana de los efectos y declara activo todo efecto cuyo valor absoluto supere el margen de error.

Montgomery advierte que el método de Lenth solo es razonable cuando hay pocos efectos activos y recomienda usarlo como complemento de la gráfica normal. En el ejemplo 1, donde cinco de siete efectos son grandes, Lenth no detecta ninguno (PSE = 24.75).

Y los principios de interpretación de cadenas: escasez de efectos (Montgomery lo nombra en la introducción del capítulo), jerarquía (los efectos de orden bajo son más probables; Montgomery lo invoca en el ejemplo 8-6, pág. 335, para conservar el factor D en el modelo junto con la interacción AD) y herencia (una interacción es más creíble si sus factores tienen efecto principal; este nombre es usual en otros textos, como Wu y Hamada).""",
  left=[bul("**Gráfica normal o seminormal de efectos**: los inactivos caen sobre una recta",
            "**Pareto con método de Lenth**: activo si |efecto| > margen de error; complementa la gráfica normal, no la sustituye",
            "Los efectos descartados pasan a formar el **error** del ANOVA"),
        form("s_{0} = 1.5 · mediana |ℓ_{i}|", "PSE = 1.5 · mediana { |ℓ_{i}| : |ℓ_{i}| < 2.5 s_{0} }",
             "ME = t_{0.025, m/3} · PSE", size=17)],
  right=[txt("**Para interpretar una cadena de alias**", size=18),
         cards(("Escasez", "Pocos efectos son realmente activos"),
               ("Jerarquía", "Los efectos de orden bajo son más probables que los de orden alto"),
               ("Herencia", "Una interacción es más creíble si sus factores tienen efecto principal"),
               size=15, cols=1)], ratio=0.54)

S("¿Qué debemos verificar sobre el modelo?",
  """Las pruebas F del ANOVA son válidas si los errores son normales, tienen varianza constante y son independientes. Los errores no se observan, así que se trabaja con los residuos: la diferencia entre cada respuesta observada y el valor que predice el modelo ajustado.

Montgomery verifica los supuestos con gráficas de residuales y solo da pruebas formales para la igualdad de varianzas (Bartlett y Levene modificada). Siguiendo la estructura de la clase, aquí se propone además una prueba analítica para cada supuesto; Anderson-Darling, Shapiro-Wilk y Durbin-Watson no provienen del libro. Normalidad: gráfica de probabilidad normal de los residuos y prueba de Anderson-Darling o Shapiro-Wilk. Varianza constante: gráfica de residuos contra valores ajustados y contra cada factor, y prueba de Bartlett o de Levene modificada; Bartlett es muy sensible a la falta de normalidad y no debe usarse si esta está en duda. Independencia: gráfica de residuos contra el orden de corrida y prueba de Durbin-Watson.

En un fraccionado sin réplicas los residuos provienen de los efectos descartados; si el modelo deja pocos grados de libertad para el error, la verificación tiene poca potencia.""",
  left=[form("e = y − ŷ", size=26),
        txt("Residuo: respuesta observada menos valor ajustado por el modelo", size=16),
        note("Con pocos g.l. en el error, la verificación tiene **poca potencia**")],
  right=[tab(["Supuesto", "Prueba gráfica", "Prueba analítica"],
             [["Normalidad", "Probabilidad normal de residuos", "Anderson-Darling, Shapiro-Wilk"],
              ["Varianza constante", "Residuos contra ajustados y contra cada factor", "Bartlett, Levene modificada"],
              ["Independencia", "Residuos contra orden de corrida", "Durbin-Watson"]],
             size=16, colw=[0.26, 0.4, 0.34])], ratio=0.36)

_res2 = m2["res"]
_zr = normal_scores(_res2)
_sr = sorted(range(16), key=lambda i: _res2[i])
S("Ejemplo 2 · Normalidad de los residuos",
  f"""Hipótesis: H_{{0}}: los residuos siguen una distribución normal; H_{{A}}: no la siguen.

Prueba gráfica: en la gráfica de probabilidad normal los 16 residuos se alinean razonablemente sobre una recta, sin puntos alejados.

Prueba analítica: el estadístico de Anderson-Darling es A² = {f(ad2[0], 3)}, con valor p = {f(ad2[2], 3)}. Como el valor p es mayor que 0.05, no se rechaza H_{{0}}: los residuos son normales.""",
  left=[scatter([(_res2[i], _zr[i]) for i in _sr], "Residuo", "Puntuación normal", h=4.6,
                line="fit", title="Probabilidad normal de los residuos")],
  right=[form("H_{0}: los residuos son normales", "H_{A}: los residuos no son normales", size=18),
         tab(["Anderson-Darling", "Valor"], [["A^{2}", f(ad2[0], 3)], ["Valor p", f(ad2[2], 3)]], size=17),
         note("Valor p > 0.05: **no se rechaza H_{0}**, los residuos son normales")], ratio=0.54)

S("Ejemplo 2 · Varianza constante e independencia",
  """Varianza constante: en la gráfica de residuos contra valores ajustados los puntos forman una banda horizontal, sin forma de embudo; la dispersión es similar para rendimientos bajos y altos. No hay evidencia contra el supuesto.

Independencia: se verifica graficando los residuos contra el orden real de corrida y con la prueba de Durbin-Watson. Requiere haber registrado el orden de corrida durante el experimento; el ejemplo del libro no lo reporta, así que aquí no se puede calcular. Por eso el protocolo insiste en aleatorizar y guardar ese orden.""",
  left=[scatter(list(zip(m2["fitted"], _res2)), "Valor ajustado", "Residuo", h=4.6,
                title="Residuos contra valores ajustados")],
  right=[bul("**Varianza constante:** banda horizontal, sin forma de embudo  →  se cumple",
             "**Independencia:** residuos contra **orden de corrida**; sin tendencias ni rachas",
             "Prueba analítica: **Durbin-Watson**", size=17),
         form("d = Σ (e_{t} − e_{t−1})^{2} / Σ e_{t}^{2}", size=18),
         note("Sin el orden de corrida registrado, la independencia **no se puede verificar**", size=15)],
  ratio=0.54)

S("¿Qué hago si se viola un supuesto?",
  """Si falla la normalidad: revisar datos atípicos y errores de registro, y considerar una transformación de la respuesta; el ANOVA es robusto a desviaciones moderadas.

Si la varianza no es constante: transformar la respuesta (logaritmo, raíz cuadrada, recíproco; la elección puede guiarse por la relación entre la desviación estándar y la media, o por el método de Box-Cox).

Si falla la independencia: es un problema potencialmente serio y difícil de corregir; la aleatorización es la principal forma de prevenirlo. Si existe una fuente identificable (tiempo, lote), debe controlarse en experimentos futuros o incluirse en el análisis como bloque o covariable.

Si el modelo deja residuos con patrón: probablemente falta un término; hay que revisar las cadenas de alias y, si es necesario, agregar corridas.""",
  body=[tab(["Problema", "Síntoma", "Qué hacer"],
            [["No normalidad", "Curvatura o puntos alejados en la gráfica normal",
              "Revisar atípicos; transformar la respuesta"],
             ["Varianza no constante", "Embudo en residuos contra ajustados",
              "Transformar la respuesta (logaritmo, raíz, Box-Cox)"],
             ["Dependencia", "Tendencia o rachas contra el orden de corrida",
              "Difícil de corregir: prevenir aleatorizando; incluir la fuente como bloque o covariable"],
             ["Modelo incompleto", "Patrón en los residuos",
              "Revisar cadenas de alias; agregar términos o corridas"]],
            size=16, colw=[0.2, 0.36, 0.44])])

S("¿Qué es la proyección en el caso general?",
  """Un diseño de resolución R contiene un factorial completo en cualquier subconjunto de R − 1 factores. Si al analizar resulta que solo unos pocos factores son activos, se descartan los demás y el diseño se convierte, sin correr nada más, en un factorial completo (posiblemente con réplicas) en los factores activos.

En general, un 2^{k−p} se proyecta en un factorial completo en cualquier subconjunto de r ≤ k − p factores que no contenga una palabra de la relación de definición; si la contiene, lo que queda es un factorial fraccionado con réplicas. Consecuencia práctica: al asignar los factores a las columnas conviene que los que se creen más importantes no formen juntos una palabra.""",
  left=[bul("Resolución **R** ⇒ factorial completo en cualquier subconjunto de **R − 1** factores",
            "Al descartar factores inactivos se ganan **réplicas** sin correr nada más",
            "Si los factores activos contienen una **palabra**, queda un fraccionado con réplicas, no un completo"),
        note("Asigne los factores que cree importantes de modo que **no formen una palabra**")],
  right=[tab(["Diseño", "Se proyecta en…"],
             [["2^{3−1}_{III}", "2^{2} completo en cualquier par de factores"],
              ["2^{4−1}_{IV}", "2^{3} completo en cualesquiera tres factores"],
              ["2^{5−1}_{V}", "2^{4} completo en cuatro factores; dos réplicas de un 2^{3} en tres"],
              ["2^{6−2}_{IV}", "Dos réplicas de un 2^{3} en cualesquiera tres factores"],
              ["2^{7−4}_{III}", "Dos réplicas de un 2^{2} en cualquier par de factores"]],
             size=15, colw=[0.27, 0.73])], ratio=0.46)

S("¿Cómo asigno los factores a las columnas?",
  """La proyección permite asignar los factores con estrategia. En el 2^{7−3}_{IV} de 16 corridas hay 35 subconjuntos de cuatro factores; siete son palabras de la relación de definición y los otros 28 forman un 2^{4} completo. Uno de ellos, el más obvio, es el de las columnas del diseño básico: A, B, C y D.

Montgomery lo ilustra con un molino de bolas con siete factores. Se tiene bastante certeza de que la velocidad del motor, el modo de alimentación, el tamaño de la alimentación y el tipo de material afectan la eficiencia y pueden interactuar; se sabe menos de la muesca, el ángulo de la criba y el nivel de vibración, que probablemente son insignificantes. La estrategia es asignar los cuatro primeros a las columnas A, B, C y D y las «variables menores» a E, F y G. Si se está en lo correcto y estas resultan despreciables, queda un 2^{4} completo en las variables clave.

Las conclusiones obtenidas así deben considerarse tentativas: suele haber explicaciones alternativas basadas en interacciones de orden superior.""",
  left=[tab(["Columna", "Factor del molino de bolas"],
            [["A", "Velocidad del motor"], ["B", "Modo de alimentación"], ["C", "Tamaño de la alimentación"],
             ["D", "Tipo de material"], ["E = ABC", "Muesca"], ["F = BCD", "Ángulo de la criba"],
             ["G = ACD", "Nivel de vibración de la criba"]], size=15, colw=[0.3, 0.7], hl=[0, 1, 2, 3])],
  right=[bul("Factores **importantes** y que pueden interactuar: columnas del **diseño básico**",
             "Factores **menores**: columnas generadas",
             "Si los menores no influyen, queda un **2^{4} completo** en los importantes",
             "De 35 subconjuntos de 4 factores, **28** dan un 2^{4} completo", size=16),
         note("Las conclusiones son **tentativas**: puede haber explicaciones con interacciones de orden alto", size=15)],
  ratio=0.48)

S("¿Cómo se separa un fraccionado en bloques?",
  """A veces un fraccionado tiene tantas corridas que no se pueden hacer todas en condiciones homogéneas. Entonces se confunde con bloques, igual que un 2^{k}. La tabla XII del apéndice de Montgomery da los arreglos recomendados; en ellos el bloque más pequeño tiene ocho corridas.

El procedimiento: se elige para confundir con los bloques una cadena de alias formada solo por interacciones de orden alto, para no perder efectos de interés. En el 2^{6−2} con I = ABCE = BCDF = ADEF hay dos cadenas formadas solo por interacciones triples; la tabla sugiere ABD (con sus alias CDE, ACF y BEF).

Las corridas se reparten según el signo de ABD. El bloque principal contiene las combinaciones de tratamientos con un número par de letras en común con ABD, es decir, las que cumplen L = x_{1} + x_{2} + x_{4} = 0 (mod 2), donde x vale 1 si la letra está presente y 0 si no.""",
  left=[tab(["Bloque 1 (principal)", "Bloque 2"],
            [["(1)", "ae"], ["abf", "acf"], ["cef", "bef"], ["abce", "bc"], ["adef", "df"], ["bde", "abd"],
             ["acd", "cde"], ["bcdf", "abcdef"]], size=15, first_left=False),
        txt("Montgomery, fig. 8-18. La figura imprime «abef» en el bloque 1; para pertenecer a la fracción debe ser adef", size=12)],
  right=[num("Elegir una cadena de alias con **solo interacciones de orden alto**",
             "Confundirla con los bloques: aquí **ABD = CDE = ACF = BEF**",
             "Repartir las corridas según el signo de ABD", size=16),
         form("Bloque principal:  L = x_{1} + x_{2} + x_{4} = 0  (mod 2)", size=17),
         note("Bloque principal: número **par** de letras en común con ABD", size=15)], ratio=0.4)

E(4, "máquina CNC", "Montgomery, ejemplo 8-6",
  ["Una máquina CNC de cinco ejes produce el impulsor de un motor de turbina. Una característica de calidad clave es el **perfil de los álabes**: interesa su desviación respecto al perfil especificado en el plano, medida como la desviación estándar de la diferencia entre ambos.",
   "Se quiere saber **qué parámetros de la máquina** afectan esa desviación. Se eligen ocho factores a dos niveles: desviaciones de los ejes x, y, z y a, fabricante de la herramienta, velocidad del husillo, altura de la plantilla sujetadora y velocidad de alimentación.",
   "La máquina tiene **cuatro husillos** (la traducción del libro los llama areómetros) que pueden diferir entre sí; deben tratarse como **bloques**. Los ingenieros creen que las interacciones de tres o más factores son despreciables, pero no quieren ignorar las de dos."],
  "Identificar los parámetros de la máquina que **más afectan la desviación del perfil**, controlando la diferencia entre husillos",
  ["Elegir entre 16 y 32 corridas y justificarlo", "Repartir el diseño en cuatro bloques y ver qué se confunde",
   "Estimar los efectos y ajustar el modelo", "Interpretar los alias que queden ambiguos"])

S("Ejemplo 4 · Máquina CNC: 2^{8−3}_{IV} en cuatro bloques",
  """Una máquina CNC de cinco ejes maquina un propulsor para un motor de turbina. La respuesta es la desviación del perfil de los álabes respecto al plano: la desviación estándar de la diferencia entre el perfil real y el especificado. Se estudian ocho factores. La máquina tiene cuatro areómetros que pueden diferir, así que se tratan como bloques. Fuente: Montgomery, ejemplo 8-6.

Los ingenieros confían en que las interacciones de tres o más factores no importan, pero no quieren ignorar las dobles. La tabla de diseños ofrece dos de resolución IV: el 2^{8−4} de 16 corridas y el 2^{8−3} de 32. El de 16 tiene muchas interacciones dobles aliadas entre sí y no se puede correr en cuatro bloques sin confundir cuatro interacciones dobles con ellos. Se elige el 2^{8−3} en cuatro bloques, con F = ABC, G = ABD y H = BCDE. Quedan confundidas con los bloques una cadena de interacciones triples y la interacción EH, entre la desviación del eje a y la velocidad de alimentación, que los ingenieros consideran muy improbable.

Como la respuesta es una desviación estándar, se analiza su logaritmo.""",
  left=[tab(["Factor", "Bajo (−)", "Alto (+)"],
            [["A  Desviación eje x (0.001 pulg)", "0", "15"], ["B  Desviación eje y (0.001 pulg)", "0", "15"],
             ["C  Desviación eje z (0.001 pulg)", "0", "15"], ["D  Fabricante de la herramienta", "1", "2"],
             ["E  Desviación eje a (0.001 grados)", "0", "30"], ["F  Velocidad del areómetro (%)", "90", "110"],
             ["G  Altura de la plantilla (0.001 pulg)", "0", "15"], ["H  Velocidad de alimentación (%)", "90", "110"]],
            size=13, colw=[0.6, 0.2, 0.2])],
  right=[bul("Respuesta: **ln(desviación estándar × 10^{3})**",
             "Cuatro **areómetros** como bloques",
             "**2^{8−3}_{IV}** en 4 bloques: 32 corridas", size=16),
         form("F = ABC,  G = ABD,  H = BCDE", size=17),
         note("Con bloques se confunden una cadena triple y **EH**, que se considera muy improbable", size=14)],
  ratio=0.55)

S("Ejemplo 4 · Efectos, ANOVA y conclusión",
  """En la gráfica normal de los efectos solo sobresalen A (desviación del eje x), B (desviación del eje y) y la cadena AD + BG. AD es la interacción del eje x con el fabricante de la herramienta y BG la del eje y con la altura de la plantilla. Como las dos incluyen un efecto principal grande, no hay una simplificación lógica obvia: hace falta conocimiento del proceso o más corridas para separarlas.

Suponiendo, por conocimiento del proceso, que la interacción es AD, el modelo lleva A, B, D y AD. D entra aunque su efecto sea pequeño para respetar el principio de jerarquía. El efecto de los bloques es pequeño: los areómetros no difieren mucho. La gráfica normal de residuales sugiere colas algo más gruesas que las normales.

Interpretación: con el fabricante 1 la respuesta crece mucho al pasar A de bajo a alto; con el fabricante 2 casi no cambia. La mejor combinación es A en nivel bajo, B en nivel alto y la herramienta del fabricante 1. La tabla ANOVA es la del libro (tabla 8-18).""",
  left=[tab(["SV", "SS", "DF", "MS", "F_{0}", "P-Value"],
            [["A", "0.6740", "1", "0.6740", "39.42", "<0.0001"], ["B", "0.3217", "1", "0.3217", "18.81", "0.0002"],
             ["D", "0.0935", "1", "0.0935", "5.47", "0.0280"], ["AD", "1.1197", "1", "1.1197", "65.48", "<0.0001"],
             ["Bloques", "0.0201", "3", "0.0067", "", ""], ["Error", "0.4099", "24", "0.0171", "", ""],
             ["Total", "2.6389", "31", "", "", ""]], size=15)],
  right=[bul("Activos: **A**, **B** y la cadena **AD + BG**",
             "Las dos interacciones tienen un efecto principal grande: se requiere **conocimiento del proceso**",
             "D entra por **jerarquía** (acompaña a AD)",
             "Bloques pequeños: los areómetros **no difieren** mucho",
             "Mejor condición: **A bajo, B alto, fabricante 1**", size=15)],
  ratio=0.5)

section(7, "Diseños de resolución III", "Saturados, doblez y diseños de Plackett-Burman")

_rows = [[str(i + 1)] + [sg(r[c]) for c in "ABCDEFG"] for i, r in enumerate(r4)]
S("¿Qué es un diseño saturado? El 2^{7−4}_{III}",
  """Los diseños de resolución III permiten estudiar hasta k = N − 1 factores en N corridas, con N múltiplo de 4. El 2^{7−4} estudia siete factores en solo ocho corridas: se escribe el 2^{3} completo en A, B y C y se definen D = AB, E = AC, F = BC y G = ABC. Se dice que el diseño está saturado porque usa todos los grados de libertad para efectos principales.

El costo es alto: cada efecto principal es alias de tres interacciones dobles. Solo sirve si se puede suponer que las interacciones son despreciables o si se planea un doblez posterior.""",
  left=[tab(["Corrida", "A", "B", "C", "D = AB", "E = AC", "F = BC", "G = ABC"], _rows, size=14,
            first_left=False),
        note("**Saturado**: 7 factores en 8 corridas (k = N − 1)", size=15)],
  right=[tab(["Columna", "Estima"], [[w, f"{w} + {alias4[w]}"] for w in "ABCDEFG"], size=15,
             first_left=False),
         txt("Alias despreciando interacciones de tres o más factores", size=13)], ratio=0.56)

S("¿Cuál es la relación de definición del 2^{7−4}?",
  """El 2^{7−4} tiene cuatro generadores: I = ABD, I = ACE, I = BCF e I = ABCG. Su relación de definición completa se obtiene multiplicando los generadores de dos en dos, de tres en tres y los cuatro a la vez: tiene 2^{4} − 1 = 15 palabras. La más corta tiene tres letras, así que es de resolución III.

Cada efecto tiene 15 alias. Si se suponen despreciables las interacciones de tres o más factores, cada estimación es la suma del efecto principal y de tres interacciones dobles; son las cadenas de la tabla de la diapositiva anterior (ecuación 8-1 del libro).

Es una fracción un dieciseisavo del 2^{7}. Hay 16 diseños en la familia, uno por cada combinación de signos de los cuatro generadores; con todos positivos se tiene la fracción principal.""",
  body=[form("I = ABD = ACE = BCF = ABCG = BCDE = ACDF = CDG", "= ABEF = BEG = AFG = DEF = ADEG = CEFG = BDFG = ABCDEFG", size=17),
        form("B = AD = CF = EG = ACG = CDE = AEF = DFG = ABCE = ABFG = BCDG = BDEF = ABCDF = ABDEG = BCEFG = ACDEFG", size=14),
        cards(("15 palabras", "Generadores y todos sus productos; la más corta tiene **3 letras**: resolución III"),
              ("15 alias por efecto", "Despreciando triples: principal + **tres interacciones dobles**"),
              ("16 fracciones", "Una por cada combinación de signos de los **cuatro generadores**"), size=15)])

S("¿Cómo obtengo diseños para menos factores?",
  """Del 2^{7−4} saturado se obtienen diseños de resolución III para menos de siete factores en ocho corridas: basta eliminar columnas. Si se elimina G queda un 2^{6−3}_{III}, con D = AB, E = AC y F = BC.

Regla: al eliminar d factores, la nueva relación de definición está formada por las palabras de la original que no contienen ninguna de las letras eliminadas. Para el 2^{6−3} quedan siete palabras: I = ABD = ACE = BCF = BCDE = ACDF = ABEF = DEF.

Hay que elegir bien qué columnas se eliminan. Si se eliminan B, D, F y G quedan tres factores en ocho corridas, pero el diseño resulta ser dos réplicas de un 2^{3−1}, cuando con las mismas ocho corridas se podría tener un 2^{3} completo en A, C y E.

La misma idea da diseños saturados mayores: con el 2^{4} en A, B, C y D y once factores nuevos igualados a todas sus interacciones se obtiene el 2^{15−11}_{III}, que estudia 15 factores en 16 corridas, cada uno alias de siete interacciones dobles. Del mismo modo, el 2^{31−26}_{III} estudia 31 factores en 32 corridas.""",
  left=[form("Nueva relación = palabras que **no contienen** las letras eliminadas", size=17),
        tab(["Se elimina", "Queda", "Relación de definición"],
            [["G", "2^{6−3}_{III}", "I = ABD = ACE = BCF = BCDE = ACDF = ABEF = DEF"],
             ["B, D, F, G", "3 factores", "Dos réplicas de un 2^{3−1} (mala elección)"]],
            size=14, colw=[0.2, 0.2, 0.6], first_left=False)],
  right=[tab(["Diseño saturado", "Factores", "Corridas"],
             [["2^{3−1}_{III}", "3", "4"], ["2^{7−4}_{III}", "7", "8"], ["2^{15−11}_{III}", "15", "16"],
              ["2^{31−26}_{III}", "31", "32"]], size=15, first_left=False),
         note("Para 3 factores en 8 corridas es mejor un **2^{3} completo** en A, C y E", size=15)], ratio=0.58)

S("¿Qué es el doblez?",
  """En un diseño de resolución III cada efecto principal está mezclado con interacciones dobles. Para separarlos se usa el ensamblaje secuencial: se corre una segunda fracción en la que se han invertido los signos de algunos factores y se combinan las dos. A esta técnica se le llama doblez o plegado (fold over).

La estructura de alias de la segunda fracción no hay que calcularla de cero: se obtiene cambiando el signo de los factores invertidos en la estructura de alias de la fracción original. Después, como con la fracción alterna, la semisuma y la semidiferencia de las estimaciones de las dos fracciones separan los efectos.

Hay dos variantes. El doblez de un solo factor invierte los signos de un factor. El doblez completo, o reflexión, invierte los signos de todos.""",
  left=[bul("Correr una **segunda fracción** con signos invertidos y combinarla con la primera",
            "Alias de la segunda fracción: **cambiar el signo** de los factores invertidos",
            "Separar con **½ (ℓ + ℓ′)** y **½ (ℓ − ℓ′)**", size=17)],
  right=[cards(("Doblez de un solo factor", "Se invierten los signos de **un** factor"),
               ("Doblez completo (reflexión)", "Se invierten los signos de **todos** los factores"),
               size=17, cols=1)], ratio=0.55)

_rows = [["A", "A + BD + CE + FG", "A − BD + CE + FG", "A + CE + FG", "BD"],
         ["B", "B + AD + CF + EG", "B − AD + CF + EG", "B + CF + EG", "AD"],
         ["C", "C + AE + BF + DG", "C + AE + BF − DG", "C + AE + BF", "DG"],
         ["D", "D + AB + CG + EF", "D − AB − CG − EF", "D", "AB + CG + EF"],
         ["E", "E + AC + BG + DF", "E + AC + BG − DF", "E + AC + BG", "DF"],
         ["F", "F + BC + AG + DE", "F + BC + AG − DE", "F + BC + AG", "DE"],
         ["G", "G + CD + BE + AF", "G − CD + BE + AF", "G + BE + AF", "CD"]]
S("Doblez de un solo factor",
  """Junto a la fracción principal del 2^{7−4} se corre una segunda fracción con los signos de solo la columna D invertidos. Los alias de la segunda fracción se obtienen reemplazando D por −D en la estructura original: ℓ′_{A} estima A − BD + CE + FG, y como −D = AB + CG + EF, ℓ′_{D} estima D − AB − CG − EF (ecuación 8-2).

Al combinar las dos fracciones, D queda limpio y cada una de sus interacciones dobles, BD, AD, DG, DF, DE y CD, queda aislada en una semidiferencia.

Regla general de Montgomery: si a un fraccionado de resolución III o mayor se le agrega una fracción con los signos de un solo factor invertidos, el diseño combinado estima ese efecto principal y todas sus interacciones dobles. Se supone que las interacciones de tres o más factores son despreciables.""",
  body=[tab(["i", "ℓ_{i}  (1.ª fracción)", "ℓ′_{i}  (D invertido)", "½ (ℓ_{i} + ℓ′_{i})", "½ (ℓ_{i} − ℓ′_{i})"], _rows, size=14,
            hl=[3], colw=[0.06, 0.24, 0.24, 0.22, 0.24], first_left=False),
        note("Regla: invertir **un** factor deja limpios ese factor y **todas sus interacciones dobles**")])

S("Doblez completo",
  """En el doblez completo, o reflexión, se agrega una segunda fracción con los signos de todos los factores invertidos. La columna de cada factor cambia de signo, pero la de cada interacción doble no, porque es producto de dos signos invertidos: (−)(−) = +. Por eso, en la segunda fracción cada efecto principal queda aliado con sus interacciones dobles con signo contrario: ℓ′_{A} estima A − BD − CE − FG. La semisuma deja los efectos principales limpios y la semidiferencia deja las cadenas de interacciones dobles.

Montgomery lo resume así: el doblez completo rompe los vínculos de alias entre los efectos principales y las interacciones dobles, y el diseño combinado estima todos los efectos principales libres de interacciones dobles.

Un detalle útil para construirlo: invertir todos los signos equivale a cambiar el signo de los generadores con número impar de letras. En el 2^{7−4}, ABD, ACE y BCF cambian de signo y ABCG no.""",
  left=[form("Columna de A: se invierte  ·  Columna de BD: (−)(−) = +, no se invierte", "⇒  ℓ′_{A} → A − BD − CE − FG", size=16),
        form("½ (ℓ_{i} + ℓ′_{i}) → efecto principal", "½ (ℓ_{i} − ℓ′_{i}) → cadena de interacciones dobles", size=18)],
  right=[bul("Se invierten los signos de **todos** los factores",
             "Rompe los alias entre **principales** e **interacciones dobles**",
             "Equivale a cambiar el signo de los generadores con **número impar** de letras",
             "En el 2^{7−4}: ABD, ACE y BCF cambian; **ABCG** no", size=16)], ratio=0.5)

E(5, "tiempo de enfoque del ojo", "Montgomery, ejemplo 8-7",
  ["Un experimentador estudia el **tiempo de enfoque del ojo** (ms) y construyó un aparato en el que puede controlar varios factores durante la prueba. Considera importantes siete, cada uno a dos niveles: A agudeza visual, B distancia del objetivo al ojo, C forma del objetivo, D nivel de iluminación, E tamaño del objetivo, F densidad del objetivo y G sujeto.",
   "Sospecha que **solo unos pocos** de los siete factores son importantes y que las interacciones de orden alto se pueden despreciar.",
   "Decide hacer primero un **experimento de tamizado** con un 2^{7−4}_{III} de 8 corridas, en orden aleatorio, para identificar los factores importantes y concentrar en ellos el estudio posterior."],
  "**Tamizar**: encontrar los pocos factores que de verdad afectan el tiempo de enfoque",
  ["Estimar los efectos de la primera fracción", "Listar las explicaciones compatibles con los alias",
   "Elegir y correr una segunda fracción que las separe", "Decidir qué efectos son los reales"])

_o4 = sorted("ABCDEFG", key=lambda w: abs(ef4[w]))
S("Ejemplo 5 · Una primera fracción ambigua",
  """Experimento sobre el tiempo de enfoque del ojo con siete factores: A agudeza visual, B distancia al objetivo, C forma del objetivo, D nivel de iluminación, E tamaño del objetivo, F densidad y G sujeto. Se corre el 2^{7−4} de ocho corridas. Fuente: Montgomery, ejemplo 8-7.

Tres estimaciones son grandes: ℓ_{B} = 38.38, ℓ_{D} = 28.88 y ℓ_{A} = 20.63. La lectura más simple es que A, B y D son activos. Pero como D = AB, hay otras tres explicaciones igual de lógicas: A, B y la interacción AB; A, D y la interacción AD; o B, D y la interacción BD. La fracción sola no permite distinguirlas.""",
  left=[bars(_o4, [ef4[w] for w in _o4], "Efecto estimado (ms)", h=3.9,
             title="Primera fracción: efectos estimados"),
        note("Grandes: ℓ_{B} = 38.38,  ℓ_{D} = 28.88,  ℓ_{A} = 20.63", size=15)],
  right=[txt("**Cuatro explicaciones posibles**", size=18),
         tab(["Explicación", "Efectos activos"],
             [["1", "A, B y D"], ["2", "A, B y la interacción AB"], ["3", "A, D y la interacción AD"],
              ["4", "B, D y la interacción BD"]], size=16, first_left=False),
         note("Como **D = AB**, la fracción no distingue entre ellas", size=15)], ratio=0.5)

_rows = []
for w in "ABCDEFG":
    a, b = ef4[w], ef4b[w]
    _rows.append([w, f(a), f(b), f"{w} = {f((a + b) / 2)}", f"{alias4[w]} = {f((a - b) / 2)}"])
S("Ejemplo 5 · Qué aclara el doblez completo",
  """Se corre una segunda fracción de ocho corridas con los signos de todos los factores invertidos. En ella cada efecto principal aparece con sus interacciones dobles con signo negativo, de modo que la semisuma aísla el efecto principal y la semidiferencia aísla el grupo de interacciones.

Resultado: los efectos principales grandes son B = 38.05 y D = 29.38. El efecto de A es solo 1.48; lo que parecía el efecto de A era en realidad la cadena BD + CE + FG = 19.15, que es razonable atribuir a BD porque B y D son activos. BD sigue aliada con CE y FG; en el estudio se confirmó con experimentos posteriores. La explicación más plausible era la cuarta.

Las 16 corridas forman un 2^{7−3} de resolución IV: el doblez completo de un diseño de resolución III siempre produce uno de resolución IV.

Nota para quien coteje con el libro: en la fila F, Montgomery imprime −1.53; con sus propios datos el valor es −1.13.""",
  body=[tab(["Columna", "ℓ  (1.ª fracción)", "ℓ′  (doblez)", "½ (ℓ + ℓ′)", "½ (ℓ − ℓ′)"], _rows, size=15,
            hl=[0, 1, 3], colw=[0.12, 0.17, 0.17, 0.2, 0.34], first_left=False),
        note("Activos: **B**, **D** y la cadena **BD + CE + FG**, que es razonable atribuir a BD. "
             "Diseño combinado: 2^{7−3} de resolución **IV**")])

S("¿Cuál es la relación de definición del diseño combinado?",
  """Montgomery da una regla sencilla. Cada fracción por separado tiene L + U generadores: L palabras con el mismo signo en las dos fracciones y U palabras con signo distinto. El diseño combinado tiene L + U − 1 generadores: las L palabras de igual signo y U − 1 palabras formadas por productos pares independientes de las palabras de signo distinto. Productos pares son las palabras tomadas de dos en dos, de cuatro en cuatro, etc.

En el ejemplo 5, la primera fracción tiene I = ABD, ACE, BCF y ABCG; el doblez tiene I = −ABD, −ACE, −BCF y ABCG. Así, L = 1 (ABCG) y U = 3. El combinado usa ABCG y dos productos pares, por ejemplo (ABD)(ACE) = BCDE y (ABD)(BCF) = ACDF.

La relación completa del diseño combinado tiene siete palabras, todas de cuatro letras: es un 2^{7−3}_{IV}. El doblez completo de un diseño de resolución III da un diseño de resolución IV.""",
  left=[tab(["", "1.ª fracción", "Doblez", "Signo"],
            [["ABD", "+", "−", "distinto"], ["ACE", "+", "−", "distinto"], ["BCF", "+", "−", "distinto"],
             ["ABCG", "+", "+", "igual"]], size=15, first_left=False),
        form("L = 1,  U = 3  ⇒  L + U − 1 = 3 generadores", size=17)],
  right=[form("ABCG,   (ABD)(ACE) = BCDE,   (ABD)(BCF) = ACDF", size=16),
         form("I = ABCG = BCDE = ACDF = ADEG", "= BDFG = ABEF = CEFG", size=18),
         note("Siete palabras de 4 letras: **2^{7−3}_{IV}**", size=16)], ratio=0.45)

S("¿Qué son los diseños de Plackett-Burman?",
  """Son diseños de resolución III para estudiar k = N − 1 factores en N corridas, donde N es múltiplo de 4 y no solo potencia de 2: 12, 20, 24, 28, 36. Dan tamaños intermedios entre los de los diseños 2^{k−p} (8, 16, 32 corridas).

Se construyen a partir de un renglón generador que se desplaza cíclicamente una posición cada vez; al final se agrega un renglón con todos los signos negativos. Para N = 28 la construcción es distinta, con tres bloques de signos.

Advertencia: su estructura de alias es muy compleja. En el diseño de 12 corridas cada efecto principal es alias parcial de todas las interacciones dobles en las que no participa. Si hay interacciones importantes, pueden aparecer como falsos efectos principales. Montgomery recomienda usarlos con mucho cuidado. A su favor: se proyectan en un factorial completo en cualesquiera tres factores, y bajo ciertas condiciones sus alias se pueden desenredar con técnicas de regresión.""",
  left=[bul("Resolución III para **k = N − 1** factores en N corridas",
            "N **múltiplo de 4**: 12, 20, 24, 28, 36",
            "Para N = 12, 20, 24 y 36 se construye **desplazando cíclicamente** un renglón generador y agregando un renglón de signos −"),
        tab(["N", "Renglón generador"], [["12", "+ + − + + + − − − + −"],
             ["20", "+ + − − + + + + − + − + − − − − + + −"],
             ["24", "+ + + + + − + − + + − − + + − − + − + − − − −"]], size=14, colw=[0.1, 0.9], first_left=False)],
  right=[note("**Cuidado:** cada efecto principal es **alias parcial** de muchas interacciones dobles. "
              "Una interacción real puede aparecer como varios falsos efectos principales.", size=17),
         bul("Úselos **con mucho cuidado**, para tamizado, cuando no se esperan interacciones importantes",
             "Un **2^{k−p}** de tamaño parecido puede ser mejor elección", size=17)], ratio=0.52)

_pb_gen = [1, 1, -1, 1, 1, 1, -1, -1, -1, 1, -1]
_pbL = "ABCDEFGHJKL"
r_pb = []
for _i in range(11):
    _s = _pb_gen[-_i:] + _pb_gen[:-_i] if _i else _pb_gen
    r_pb.append(dict(zip(_pbL, _s)))
r_pb.append({l: -1 for l in _pbL})
y_pb = [231, 207, 230, 217, 175, 176, 183, 185, 181, 220, 229, 168]
ef_pb = {l: effect(r_pb, y_pb, l)[1] for l in _pbL}
_rows = [[str(i + 1)] + [sg(r[l]) for l in _pbL] for i, r in enumerate(r_pb)]
S("¿Cómo se construye un Plackett-Burman de 12 corridas?",
  """Para N = 12, 20, 24 y 36 el diseño se arma con el renglón de signos de la tabla 8-23 del libro. Se escribe ese renglón como primera fila (o primera columna). La segunda fila se obtiene desplazando la primera una posición hacia la derecha y pasando el último elemento al principio. Se repite el desplazamiento hasta tener k = N − 1 filas, y al final se agrega una fila con todos los signos negativos.

La tabla es el diseño de 12 corridas para 11 factores construido de esa forma, el mismo del ejemplo 6. La letra I no se usa como factor porque está reservada para la identidad. Para N = 28 la construcción es distinta: tres bloques de signos X, Y y Z de 9 × 9 se disponen en forma cíclica y se agrega la fila de signos negativos.""",
  left=[tab(["Corrida"] + list(_pbL), _rows, size=12, first_left=False, pad=0.06)],
  right=[num("Escribir el **renglón generador** como fila 1",
             "Desplazar **una posición** a la derecha para cada fila nueva",
             "Repetir hasta **N − 1** filas",
             "Agregar una fila de **signos −**", size=15),
         form("N = 12:  + + − + + + − − − + −", size=15)], ratio=0.66)

S("Alias parciales y proyectividad",
  """Los diseños de Plackett-Burman no geométricos tienen estructuras de alias muy intrincadas. En el diseño de 12 corridas, cada efecto principal es alias parcial de todas las interacciones dobles en las que no interviene. Por ejemplo, la interacción AB es alias parcial de los nueve efectos principales C, D, …, K, y cada efecto principal es alias parcial de 45 interacciones dobles. «Parcial» quiere decir que la interacción no se suma completa a la estimación, sino con un peso fraccionario. En diseños mayores la situación es aún más compleja; Montgomery recomienda usarlos con mucho cuidado.

Su ventaja está en la proyección. El de 12 corridas se proyecta en tres réplicas de un 2^{2} completo en cualquier par de factores, y en cualquier trío de factores en un 2^{3} completo más una fracción 2^{3−1}. Por eso se dice que tiene proyectividad 3, mientras que un 2^{k−p}_{III} solo tiene proyectividad 2. Las proyecciones en tres y cuatro factores no son balanceadas.""",
  left=[cards(("Alias parciales", "Cada principal es alias **parcial** de 45 interacciones dobles; AB se reparte entre los 9 principales C, …, K"),
              ("Consecuencia", "Una interacción real puede aparecer como **varios** falsos efectos principales"), size=15, cols=1)],
  right=[tab(["Proyección del PB de 12 corridas", "Resultado"],
             [["En 2 factores", "Tres réplicas de un 2^{2}"], ["En 3 factores", "Un 2^{3} completo + un 2^{3−1}"],
              ["Proyectividad", "**3** (un 2^{k−p}_{III} tiene 2)"]], size=15, colw=[0.5, 0.5]),
         note("Las proyecciones en 3 y 4 factores **no son balanceadas**", size=15)], ratio=0.5)

E(6, "Plackett-Burman con datos simulados", "Montgomery, ejemplo 8-8",
  ["Se quiere tamizar **11 factores** (A a L, sin I) con el mínimo de corridas. Un Plackett-Burman de **12 corridas** lo permite: es de resolución III y cada interacción doble queda repartida parcialmente sobre varios efectos principales.",
   "Para ver qué pasa cuando hay interacciones, Montgomery **simula** los datos con un modelo conocido: tres efectos principales activos (A, B y D), dos interacciones (AB y AD) y un error normal de varianza 9. Los demás factores no tienen ningún efecto.",
   "El analista no conoce ese modelo: solo ve las 12 respuestas y analiza el diseño como se haría en la práctica."],
  "Comprobar si el análisis del Plackett-Burman **recupera el modelo verdadero**",
  ["Estimar los 11 efectos principales", "Compararlos con el modelo que generó los datos",
   "Explicar de dónde salen los efectos falsos", "Decidir qué diseño habría sido mejor"])

_srt_pb = sorted(_pbL, key=lambda l: -abs(ef_pb[l]))
S("Ejemplo 6 · Plackett-Burman con datos simulados",
  """Montgomery simula datos para mostrar la dificultad (ejemplo 8-8). El modelo verdadero tiene tres efectos principales, A, B y D, y dos interacciones, AB y AD, más un error normal con varianza 9. Se corre el Plackett-Burman de 12 corridas para 11 factores.

Al estimar los efectos aparecen siete grandes: A, B, C, D, E, J y K. Solo tres son reales; los demás son interacciones que se repartieron como alias parciales sobre otros efectos principales. Con estos datos no es evidente cuáles de esos efectos son en realidad interacciones. Un doblez del diseño resolvería en general los efectos principales, pero suele dejar incertidumbre sobre las interacciones.

Recomendación del libro: si la elección es entre un 2^{11−7}_{III} geométrico de 16 corridas y un Plackett-Burman de 12 que quizá haya que doblar (24 corridas), el geométrico puede ser mejor elección. Nota para quien coteje: la tabla 8-26 imprime 12.667 para el efecto de C; con los datos es 13.667, que es lo que da su propio coeficiente.""",
  left=[form("y = 200 + 8x_{1} + 10x_{2} + 12x_{4} − 12x_{1}x_{2} + 9x_{1}x_{4} + ε", size=16),
        bars(_srt_pb, [abs(ef_pb[l]) for l in _srt_pb], "|Efecto|", h=3.5, title="Efectos estimados (valor absoluto)")],
  right=[cards(("Lo que es real", "**A, B, D**, AB y AD"),
               ("Lo que aparece", "**Siete** efectos grandes: A, B, C, D, E, J y K"),
               ("Recomendación", "Preferir un **2^{11−7}_{III}** de 16 corridas a un PB de 12 que haya que doblar"),
               size=15, cols=1)], ratio=0.55)

S("¿Cómo se resuelven las dudas que dejan los alias?",
  """Las conclusiones de un fraccionado son tentativas porque siempre existe una explicación alternativa basada en los alias. Hay cuatro formas de resolver la duda.

Corrida de confirmación: predecir con el modelo la respuesta en una condición nueva y comprobarla. Fracción alterna: en una fracción un medio, correr la otra mitad completa el factorial. Doblez completo: correr una segunda fracción con los signos de todos los factores invertidos; separa los efectos principales de las interacciones dobles y convierte un diseño de resolución III en uno de resolución IV. Doblez de un factor: invertir los signos de un solo factor; en un diseño de resolución III o mayor, y despreciando interacciones de tres o más factores, deja limpio ese factor y todas sus interacciones dobles. Cuesta las mismas corridas que el doblez completo.

Cuando se agrega una segunda fracción, las dos se combinan con la semisuma y la semidiferencia de las estimaciones.""",
  left=[tab(["Estrategia", "Qué se corre", "Qué se gana"],
            [["Confirmación", "Una o pocas corridas nuevas", "Verifica la predicción del modelo"],
             ["Fracción alterna", "La otra mitad del 2^{k−1}", "Completa el factorial"],
             ["Doblez completo", "Todos los signos invertidos", "Principales libres de interacciones dobles (III → IV)"],
             ["Doblez de un factor", "Signos de un factor invertidos", "Ese factor y sus interacciones dobles, limpios"]],
            size=15, colw=[0.24, 0.34, 0.42])],
  right=[form("½ (ℓ_{i} + ℓ′_{i})", "½ (ℓ_{i} − ℓ′_{i})", size=24),
         txt("Semisuma y semidiferencia de las estimaciones de las dos fracciones: cada una aísla una parte de la cadena",
             size=16),
         note("Las dos fracciones funcionan como **bloques**")], ratio=0.62)

section(8, "Diseños de resolución IV y V", "Diseños mínimos, doblez y fracciones irregulares")

S("¿Qué es un diseño de resolución IV?",
  """Un 2^{k−p} es de resolución IV si los efectos principales están separados de las interacciones dobles y algunas interacciones dobles son alias entre sí. Si se suprimen las interacciones de tres o más factores, los efectos principales se estiman directamente. Ya se vieron dos: el 2^{6−2}_{IV} del ejemplo 3 y el 2^{7−3}_{IV} que resultó de combinar las dos fracciones del ejemplo 5.

Hay un límite inferior de tamaño: todo diseño 2^{k−p}_{IV} debe tener al menos 2k corridas. Los diseños de resolución IV con exactamente 2k corridas se llaman diseños mínimos. Por ejemplo, el 2^{4−1}_{IV} tiene 8 = 2·4 corridas y el 2^{8−4}_{IV} tiene 16 = 2·8.""",
  left=[bul("Principales **separados** de las interacciones dobles",
            "Algunas interacciones dobles son **alias entre sí**",
            "Suprimiendo triples, los principales se estiman **directamente**", size=17),
        form("Resolución IV ⇒ N ≥ 2k corridas", size=20)],
  right=[tab(["Diseño mínimo", "Factores", "Corridas = 2k"],
             [["2^{4−1}_{IV}", "4", "8"], ["2^{8−4}_{IV}", "8", "16"], ["2^{16−11}_{IV}", "16", "32"]],
             size=16, first_left=False),
         note("Diseño **mínimo**: resolución IV con exactamente **2k** corridas", size=15)], ratio=0.52)

_rows = [["+", "−", "−", "+"], ["+", "+", "−", "−"], ["+", "−", "+", "−"], ["+", "+", "+", "+"],
         ["−", "+", "+", "−"], ["−", "−", "+", "+"], ["−", "+", "−", "+"], ["−", "−", "−", "−"]]
S("¿Cómo se obtiene un resolución IV a partir de un resolución III?",
  """Los diseños de resolución IV se pueden obtener doblando un diseño de resolución III. Se toma el 2^{k−p}_{III}, se le agrega la segunda fracción con todos los signos invertidos, y se aprovecha la columna identidad: en la primera fracción es toda +, y en la segunda se cambia a toda −. Esa columna se asigna al factor k + 1. El resultado es un 2^{k+1−p}_{IV}.

La tabla es la del libro (tabla 8-27): del 2^{3−1}_{III} con I = ABC se obtiene un 2^{4−1}_{IV}, y es fácil verificar que su relación de definición es I = ABCD. Con cuatro corridas más se gana un factor y se sube de resolución III a IV.""",
  left=[tab(["D (columna I)", "A", "B", "C"], _rows, size=15, hl=[0, 1, 2, 3], first_left=False),
        txt("Arriba: 2^{3−1}_{III} original (I = ABC). Abajo: segunda fracción con los signos invertidos", size=13)],
  right=[num("Tomar el **2^{k−p}_{III}**",
             "Agregar la fracción con **todos los signos invertidos**",
             "La columna **I** pasa de + a −: se asigna al factor **k + 1**", size=16),
         form("2^{3−1}_{III}  →  2^{4−1}_{IV},   I = ABCD", size=18),
         note("Un factor más y resolución IV con solo **doblar**", size=15)], ratio=0.42)

S("¿Cómo se dobla un diseño de resolución IV?",
  """También se doblan diseños de resolución IV, para separar interacciones dobles que son alias entre sí. Montgomery y Runger señalan tres objetivos posibles: romper tantas cadenas de interacciones dobles como sea posible, romper las de una cadena específica, o romper las que incluyen un factor específico.

Una forma de hacerlo es correr una segunda fracción en la que se invierte el signo de todos los generadores con número impar de letras. En el 2^{6−2} del ejemplo 3, con I = ABCE e I = BCDF, la segunda fracción usa I = −ABCE e I = −BCDF, y el diseño combinado tiene un solo generador, I = ADEF. Sigue siendo de resolución IV, pero las únicas interacciones dobles que quedan con alias son AD = EF, AE = DF y AF = DE. En el 2^{8−3}_{IV}, con I = ABCF, ABDG y BCDEH, el combinado queda con I = CDFG = BCDEH = BEFGH y solo CD = FG, CF = DG y CG = DF siguen aliadas.

Advertencia: el doblez de un resolución III garantiza un combinado de resolución IV, pero el doblez de un resolución IV no necesariamente separa todas las interacciones dobles. Si la fracción original tiene una cadena con más de dos interacciones dobles, el doblez no las separa por completo.""",
  body=[tab(["Diseño original", "Segunda fracción", "Diseño combinado", "Interacciones dobles que siguen aliadas"],
            [["2^{6−2}_{IV}:  I = ABCE,  I = BCDF", "I = −ABCE,  I = −BCDF", "I = ADEF", "AD = EF,  AE = DF,  AF = DE"],
             ["2^{8−3}_{IV}:  I = ABCF, ABDG, BCDEH", "I = −ABCF, −ABDG, BCDEH", "I = CDFG = BCDEH = BEFGH", "CD = FG,  CF = DG,  CG = DF"]],
            size=14, colw=[0.27, 0.24, 0.23, 0.26]),
        cards(("Objetivos", "Romper muchas cadenas, una cadena específica, o las de un factor específico"),
              ("Procedimiento", "Invertir los generadores con **número impar** de letras"),
              ("Advertencia", "Con cadenas de **más de dos** interacciones dobles, no se separan todas"), size=14)])

S("¿Qué es un diseño de resolución V?",
  """En un diseño de resolución V los efectos principales y las interacciones dobles no tienen como alias otros principales ni otras interacciones dobles. Son diseños muy poderosos: si las interacciones de tres o más factores son despreciables, estiman de forma única todos los efectos principales y todas las interacciones dobles. La palabra más corta de su relación de definición debe tener cinco letras. Ejemplos: el 2^{5−1} con I = ABCDE y el 2^{8−2} con I = ABCDG = ABEFH.

Su problema es el tamaño: los diseños estándar de resolución V son grandes cuando el número de factores es moderado. Por eso interesan las fracciones irregulares de resolución V, disponibles para 4 a 9 factores: 12 corridas para 4 factores, 24 para 5 (tabla 8-28 del libro, tres cuartas partes del 2^{5}), 48 para 6, 7 u 8, y 96 para 9.

Por último, Montgomery señala que el doblez completo de un diseño de resolución IV o V suele ser innecesario: en general solo hay una o dos interacciones aliadas de interés, y sus alias se pueden separar agregando unas pocas corridas a la fracción original. Esa técnica se llama doblez parcial (ver ejemplo 10-5 del libro).""",
  left=[bul("Principales e interacciones dobles **sin alias entre sí**",
            "Palabra más corta de **5 letras**",
            "Ejemplos: **2^{5−1}**, I = ABCDE;  **2^{8−2}**, I = ABCDG = ABEFH", size=16),
        note("**Doblez parcial**: separar una o dos interacciones agregando **pocas corridas**", size=15)],
  right=[tab(["Factores", "Fracción irregular de resolución V"],
             [["4", "12 corridas"], ["5", "24 corridas (3/4 del 2^{5})"], ["6, 7 u 8", "48 corridas"], ["9", "96 corridas"]],
             size=16, colw=[0.3, 0.7], first_left=False),
         txt("Fuente: Montgomery, sec. 8-6 y tabla 8-28", size=13)], ratio=0.52)

S("Resumen · ¿Cuántos factores caben en N corridas?",
  """La tabla se lee por columnas. Con 16 corridas se puede hacer un factorial completo de 4 factores, una fracción un medio de 5, una fracción de resolución IV para 6 a 8 factores, o una de resolución III para 9 a 15.

Dos límites útiles: un diseño de resolución III admite como máximo k = N − 1 factores (diseño saturado), y un diseño de resolución IV necesita al menos N = 2k corridas.""",
  body=[tab(["Tipo de diseño", "4 corridas", "8 corridas", "16 corridas", "32 corridas"],
            [["Factorial completo", "2", "3", "4", "5"],
             ["Fracción un medio", "3", "4", "5", "6"],
             ["Fracción de resolución IV", "—", "4", "6 a 8", "7 a 16"],
             ["Fracción de resolución III", "3", "5 a 7", "9 a 15", "17 a 31"]], size=18,
            colw=[0.36, 0.16, 0.16, 0.16, 0.16]),
        txt("Las celdas indican el **número de factores** que se pueden estudiar", size=15),
        cards(("Resolución III", "Máximo **k = N − 1** factores (diseño saturado)"),
              ("Resolución IV", "Mínimo **N = 2k** corridas"), size=17)])

# ------------------------------------------------------------------ 9
section(9, "Cierre", "Lo que hay que recordar")

S("Lo que hay que recordar",
  """Un factorial fraccionado estudia muchos factores en pocas corridas a cambio de mezclar efectos. La notación 2^{k−p} dice cuántos factores, cuántos generadores y cuántas corridas. La relación de definición determina los alias y la resolución dice qué tan grave es la mezcla. El análisis es el del 2^{k}: contrastes, efectos, gráfica normal de efectos, ANOVA del modelo reducido y residuos. Las conclusiones son tentativas y se confirman con una fracción alterna, un doblez o una corrida de verificación.

Errores frecuentes: interpretar un efecto sin mirar sus alias; usar una resolución III sin prever un doblez cuando puede haber interacciones; no aleatorizar o no guardar el orden de corrida; no cuidar la asignación de los factores a las columnas cuando se tiene idea de cuáles importan; y dar por definitivas las conclusiones sin confirmar.""",
  left=[txt("**Ideas clave**", size=20),
        bul("Muchos factores en pocas corridas, **a cambio de alias**",
            "La **relación de definición** determina los alias",
            "La **resolución** dice qué tan grave es la mezcla",
            "Análisis: efectos → gráfica normal → ANOVA reducido → residuos",
            "Las conclusiones son **tentativas**: hay que confirmar", size=17)],
  right=[txt("**Errores frecuentes**", size=20),
         bul("Interpretar un efecto **sin revisar sus alias**",
             "Usar resolución III **sin prever un doblez** cuando puede haber interacciones",
             "No aleatorizar o no guardar el **orden de corrida**",
             "No cuidar la **asignación** de factores a columnas (alias y proyección)",
             "Dar por definitivo lo que no se ha confirmado", size=17)])

S("Referencias",
  """Los ejemplos numéricos y la teoría provienen de Montgomery (capítulos 6, 7 y 8); todos los cálculos (efectos, sumas de cuadrados, ANOVA, pruebas de supuestos) se rehicieron a partir de los datos. Los demás títulos son la bibliografía del curso recomendada para este tema, para quien quiera profundizar.""",
  left=[txt("**Fuente de la teoría y de los ejemplos**", size=20),
        bul("Montgomery, D. C. (2004). Diseño y análisis de experimentos, 2.ª ed. Limusa-Wiley. "
            "Capítulos 6, 7 y 8 (ejemplos 8-1 a 8-8)", size=17),
        note("Todos los cálculos se rehicieron a partir de los datos", size=15)],
  right=[txt("**Bibliografía del curso para profundizar**", size=20),
         bul("Gutiérrez Pulido, H. y De la Vara Salazar, R. (2008). Análisis y diseño de experimentos. McGraw-Hill",
             "Box, G. E. P., Hunter, J. S. y Hunter, W. G. (2005). Statistics for Experimenters. John Wiley & Sons",
             size=17)])

SLIDES.append({"kind": "closing", "title": "¿Preguntas?",
               "sub": "Diseños factoriales fraccionados 2^{k−p}", "sec": "", "explica": ""})


# ================================================================ parte 0 (solo guía)
# Repaso del 2^k que la exposición da por conocido. No genera diapositivas: render_guia.py
# lo imprime antes de la presentación. Fuente: Montgomery, cap. 6 (ficha en notas/montgomery).
PREVIO = []


def P(title, explica, body=None, left=None, right=None, ratio=0.5):
    PREVIO.append({"kind": "content", "title": title, "explica": explica.strip(),
                   "body": body, "left": left, "right": right, "ratio": ratio, "sec": "previo"})


# 2^2 del proceso químico (Montgomery, sec. 6-2): totales con n = 3
q = {"(1)": 80, "a": 100, "b": 60, "ab": 90}
qA = (q["ab"] + q["a"] - q["b"] - q["(1)"]) / 6
qB = (q["ab"] + q["b"] - q["a"] - q["(1)"]) / 6
qAB = (q["ab"] + q["(1)"] - q["a"] - q["b"]) / 6
# Ejemplo 6-1, altura de llenado: 2^3 con n = 2, totales en orden estándar
r61 = basic(3)
t61 = [-4, 1, -1, 5, -1, 3, 2, 11]
w61 = ["A", "B", "C", "AB", "AC", "BC", "ABC"]
c61 = {w: effect(r61, t61, w)[0] for w in w61}
# Ejemplo 6-2, índice de filtración: 2^4 no replicado
r62 = basic(4)
y62 = [45, 71, 48, 65, 68, 60, 80, 65, 43, 100, 45, 104, 75, 86, 70, 96]
w62 = ["A", "B", "C", "D", "AB", "AC", "AD", "BC", "BD", "CD", "ABC", "ABD", "ACD", "BCD", "ABCD"]
e62 = {w: effect(r62, y62, w)[1] for w in w62}
pse62 = lenth(list(e62.values())); me62 = t_ppf(0.05, 15 / 3) * pse62

_n3 = ["(1)", "a", "b", "ab", "c", "ac", "bc", "abc"]

P("¿Qué es un diseño 2^{k} y por qué hay que dominarlo primero?",
  """Un diseño factorial 2^{k} estudia k factores, cada uno en solo dos niveles, que se llaman «bajo» y «alto». Los factores pueden ser cuantitativos (dos temperaturas) o cualitativos (dos máquinas, presencia o ausencia de un aditivo). Una réplica completa corre todas las combinaciones posibles: 2 × 2 × ⋯ × 2 = 2^{k} corridas. Con n réplicas el total es N = n·2^{k}.

Se supone que los factores son fijos, que las corridas se hacen en orden aleatorio, que los errores son normales e independientes con varianza constante y que, como solo hay dos niveles, la respuesta es aproximadamente lineal en el rango estudiado.

Un factorial fraccionado 2^{k−p} no es un diseño nuevo: es un subconjunto de las filas de un 2^{k}. Todo lo que se dice en el tema 6 (generador, relación de definición, alias, resolución, proyección) está escrito en el lenguaje del 2^{k}: tabla de signos, producto de columnas y contrastes. Si ese lenguaje está claro, el tema 6 se reduce a una sola idea nueva: qué pasa cuando no se corren todas las filas.""",
  left=[bul("**k** factores, **dos niveles** cada uno",
            "Una réplica = **2^{k}** corridas; con n réplicas, **N = n·2^{k}**",
            "Factores fijos, orden aleatorio, errores NID(0, σ^{2})",
            "Respuesta aproximadamente **lineal** entre los dos niveles",
            "Uso típico: **tamizado** de factores en etapas tempranas", size=16)],
  right=[note("Un 2^{k−p} es un **pedazo** de la tabla del 2^{k}. Por eso esta parte va primero.", size=15),
         txt("Fuente: Montgomery, cap. 6, sec. 6-1.", size=12)], ratio=0.58)

P("Variables codificadas: por qué todo se escribe con −1 y +1",
  """En lugar de trabajar con las unidades de cada factor (°C, psi, minutos) se usa una variable codificada x que vale −1 en el nivel bajo y +1 en el nivel alto. La transformación es lineal: se resta el punto medio y se divide entre la mitad del rango. Por ejemplo, si la concentración va de 15 % a 25 %, x = (Conc − 20)/5.

La codificación tiene tres ventajas. Pone todos los factores en la misma escala, así que los efectos se pueden comparar directamente. Convierte la tabla del diseño en una tabla de signos, donde «−» significa −1 y «+» significa +1. Y hace que las columnas sean ortogonales, propiedad de la que depende todo el análisis.

Geométricamente, un 2^{2} es un cuadrado y un 2^{3} es un cubo: cada corrida es un vértice. El nivel alto de A es la cara derecha del cubo; el nivel bajo, la cara izquierda.""",
  left=[form("x = (valor − centro) / semirrango", "centro = (bajo + alto)/2", "semirrango = (alto − bajo)/2", size=16),
        bul("Nivel bajo → **x = −1**  (se escribe «−»)",
            "Nivel alto → **x = +1**  (se escribe «+»)",
            "Todos los factores quedan en la **misma escala**",
            "El 2^{3} es un **cubo**; cada corrida es un **vértice**", size=16)],
  right=[cube(["a", "ab", "ac", "abc"], caption="Vértices rellenos: la cara A = + (A en nivel alto)"),
         txt("Fuente: Montgomery, sec. 6-2 (modelo de regresión) y fig. 6-4.", size=12)], ratio=0.55)

_sig = ["ninguno", "A", "B", "A y B", "C", "A y C", "B y C", "A, B y C"]
_rows = [[str(i + 1), sg(r["A"]), sg(r["B"]), sg(r["C"]), nm,
          f"{(r['A'] + 1) // 2} {(r['B'] + 1) // 2} {(r['C'] + 1) // 2}", s_]
         for i, (r, nm, s_) in enumerate(zip(r61, _n3, _sig))]
P("La notación: mayúsculas, minúsculas y orden estándar",
  """La tabla de un 2^{k} usa dos alfabetos y conviene no confundirlos.

Las letras mayúsculas (A, B, C, AB, ABC…) nombran factores y efectos. Encabezan columnas.

Las letras minúsculas nombran corridas, es decir, combinaciones de tratamientos. Encabezan filas. La regla es: la letra aparece si el factor está en su nivel alto y no aparece si está en su nivel bajo. Así, ac es la corrida con A y C en alto y B en bajo; (1) es la corrida con todo en bajo. En un 2^{5}, abd significa A, B y D altos y C, E bajos. Montgomery usa además la misma minúscula para el total de las n respuestas observadas en esa corrida, de modo que una expresión como ab + a − b − (1) es una cuenta con datos.

Las filas se escriben en orden estándar (u orden de Yates): se introduce un factor a la vez y se combina con todo lo anterior. Se parte de (1); se agrega a; se agrega b y se multiplica por lo que había: b, ab; se agrega c: c, ac, bc, abc; y así sucesivamente. En ese orden la columna A alterna de uno en uno, la B de dos en dos, la C de cuatro en cuatro y, en general, el factor j-ésimo cambia cada 2^{j−1} filas.

Hay tres notaciones equivalentes para la misma corrida: signos (+ − +), letras (ac) y binaria (1 0 1). La I queda reservada para la identidad; por eso, después de H, el siguiente factor se llama J.""",
  body=[tab(["Corrida", "A", "B", "C", "Etiqueta", "Binaria", "Factores en nivel alto"], _rows, size=14,
            colw=[0.11, 0.08, 0.08, 0.08, 0.13, 0.14, 0.38], first_left=False),
        form("2^{4}:  (1), a, b, ab, c, ac, bc, abc, d, ad, bd, abd, cd, acd, bcd, abcd", size=16),
        txt("Fuente: Montgomery, secs. 6-2 a 6-4 (tablas de notación y orden estándar).", size=12)])

P("¿Qué es un efecto principal?",
  f"""El efecto principal de un factor es el cambio promedio en la respuesta al pasar ese factor de su nivel bajo a su nivel alto. Se calcula como el promedio de las corridas con el factor en «+» menos el promedio de las corridas con el factor en «−». En el cubo es la cara derecha menos la cara izquierda.

Ejemplo del proceso químico de Montgomery (sec. 6-2): un 2^{{2}} con n = 3, A = concentración del reactivo (15 % y 25 %), B = cantidad de catalizador (1 y 2 lb), respuesta = rendimiento. Los totales de las tres réplicas son (1) = 80, a = 100, b = 60 y ab = 90.

El efecto de A combina dos comparaciones: con B bajo, a − (1); con B alto, ab − b. Se suman y se dividen entre 2n porque cada total tiene n observaciones y hay dos comparaciones: A = [ab + a − b − (1)]/(2n) = (90 + 100 − 60 − 80)/6 = {f(qA)}. Del mismo modo B = [ab + b − a − (1)]/(2n) = {f(qB)}. Subir la concentración aumenta el rendimiento en unos 8.3 puntos; subir el catalizador lo reduce en 5.

La expresión entre corchetes, ab + a − b − (1), se llama contraste. Sus coeficientes son siempre +1 o −1, y son justamente los signos de la columna A de la tabla.""",
  left=[form("Efecto de A = ȳ_{A+} − ȳ_{A−}", "A = [ab + a − b − (1)] / (2n)", size=18),
        tab(["Corrida", "A", "B", "Total (n = 3)"],
            [["(1)", M, M, "80"], ["a", "+", M, "100"], ["b", M, "+", "60"], ["ab", "+", "+", "90"]],
            size=15, first_left=False)],
  right=[tab(["Efecto", "Contraste", "Valor"],
             [["A", "ab + a − b − (1) = 50", f(qA)], ["B", "ab + b − a − (1) = −30", f(qB)],
              ["AB", "ab + (1) − a − b = 10", f(qAB)]], size=15, first_left=False),
         note("El contraste de A usa los **signos de la columna A**: + en a y ab, − en (1) y b", size=14),
         txt("Fuente: Montgomery, sec. 6-2, ecs. 6-1 a 6-4.", size=12)], ratio=0.5)

P("¿Qué es una interacción?",
  f"""Hay interacción entre A y B cuando el efecto de A depende del nivel de B. En el ejemplo, con B bajo el efecto de A es [a − (1)]/n = (100 − 80)/3 = 6.67, y con B alto es (ab − b)/n = (90 − 60)/3 = 10. El efecto de interacción AB es la mitad de esa diferencia: AB = (10 − 6.67)/2 = {f(qAB)}.

Al desarrollar la cuenta queda AB = [ab + (1) − a − b]/(2n). Los signos +, −, −, + de ese contraste son los de una columna nueva que no se fijó al diseñar el experimento: resulta de multiplicar, fila por fila, los signos de A y de B. Esta es la idea que se repite en todo el tema 6: la columna de una interacción es el producto de las columnas de sus factores.

En la gráfica de interacción las líneas casi paralelas indican poca interacción; si se cruzan o se separan mucho, la interacción es fuerte. Cuando una interacción es importante, el efecto principal de sus factores pierde sentido por sí solo y hay que interpretar los dos factores juntos.""",
  left=[form("AB = ½ [ A_{con B alto} − A_{con B bajo} ]",
             "AB = [ab + (1) − a − b] / (2n)", size=16),
        note("Columna AB = **(signo de A) × (signo de B)**, fila por fila", size=15)],
  right=[lines(["A bajo (15 %)", "A alto (25 %)"],
               [("B bajo (1 lb)", [80 / 3, 100 / 3]), ("B alto (2 lb)", [60 / 3, 90 / 3])],
               "Rendimiento promedio", title="Gráfica de interacción A × B"),
         txt("Fuente: Montgomery, sec. 6-2, ec. 6-3.", size=12)], ratio=0.5)

_rows = []
for nm, r in zip(_n3, r61):
    _rows.append([nm, "+", sg(r["A"]), sg(r["B"]), sg(r["A"] * r["B"]), sg(r["C"]),
                  sg(r["A"] * r["C"]), sg(r["B"] * r["C"]), sg(r["A"] * r["B"] * r["C"])])
P("¿Cómo se construye la tabla de signos?",
  """La tabla de signos tiene una fila por corrida y una columna por cada efecto que el diseño puede estimar. Se arma en cuatro pasos:

1) Escribir las corridas en orden estándar. 2) Llenar las columnas de los factores: + si la letra minúscula de ese factor está en la etiqueta, − si no está. 3) Llenar cada columna de interacción multiplicando, fila por fila, los signos de las columnas de los factores que la forman. En la fila ac: A = +, B = −, C = +; entonces AB = (+)(−) = −, AC = (+)(+) = +, BC = (−)(+) = − y ABC = (+)(−)(+) = −. 4) Agregar la columna I, toda de signos +, que corresponde al promedio general.

Un 2^{3} tiene 8 filas y 8 columnas: I más 7 efectos (A, B, C, AB, AC, BC, ABC). En general, un 2^{k} tiene 2^{k} − 1 columnas de efectos, una por cada grado de libertad entre las 2^{k} corridas.

Esta tabla es la que se recorta en el tema 6. La fracción un medio del 2^{3} con I = ABC son las cuatro filas en que la columna ABC tiene signo +: a, b, c y abc.""",
  left=[tab(["Trat.", "I", "A", "B", "AB", "C", "AC", "BC", "ABC"], _rows, size=14, hl=[1, 2, 4, 7])],
  right=[num("Corridas en **orden estándar**",
             "Columnas de factores: **+ si la letra está**, − si no",
             "Columnas de interacción: **producto de signos**",
             "Columna **I**: todo +", size=15),
         note("Filas resaltadas: **ABC = +**. Son la fracción un medio con I = ABC del tema 6", size=14),
         txt("Fuente: Montgomery, sec. 6-3, tabla 6-3.", size=12)], ratio=0.58)

P("Las cuatro propiedades de la tabla de signos",
  """De la construcción salen cuatro propiedades. Son la base algebraica de todo el tema 6.

1) Balance: salvo I, cada columna tiene tantos signos + como −. Cada efecto compara la mitad de las corridas contra la otra mitad.

2) Ortogonalidad: si se multiplican dos columnas distintas fila por fila y se suman los productos, el resultado es cero. Por ejemplo, A·B en el 2^{3} da (+)+(−)+(−)+(+)+(+)+(−)+(−)+(+) = 0. Por eso cada efecto se estima con su propio contraste, sin que los demás lo contaminen.

3) Identidad: I × X = X para cualquier columna X, porque multiplicar por una columna de puros + no cambia nada.

4) Cerradura con aritmética módulo 2: el producto de dos columnas es otra columna de la tabla. Como cada signo es ±1, su cuadrado es +1; por lo tanto, cualquier letra al cuadrado es I y desaparece. En la práctica, para multiplicar dos palabras se juntan las letras y se tachan las que aparecen dos veces: AB × BC = AB^{2}C = AC.

La propiedad 4 es la regla que el tema 6 usa para obtener alias: A × ABC = A^{2}BC = BC. La diferencia es que en el 2^{k} completo dos columnas distintas nunca coinciden; en una fracción sí pueden coincidir, y eso es un alias.""",
  left=[cards(("1 · Balance", "Cada columna de efecto tiene N/2 signos + y N/2 signos −"),
              ("2 · Ortogonalidad", "Σ (columna X × columna Y) = 0 si X ≠ Y"),
              ("3 · Identidad", "I × X = X"),
              ("4 · Cerradura (módulo 2)", "X × Y es otra columna; X × X = I"), size=14, cols=1)],
  right=[tab(["Producto", "Cuenta", "Resultado"],
             [["A × B", "—", "AB"], ["A × AB", "A^{2}B", "B"], ["AB × BC", "AB^{2}C", "AC"],
              ["AB × AB", "A^{2}B^{2}", "I"], ["A × ABC", "A^{2}BC", "BC"],
              ["ABCD × AB", "A^{2}B^{2}CD", "CD"]], size=15, first_left=False),
         note("Regla práctica: juntar letras y **tachar las repetidas**", size=14),
         txt("Fuente: Montgomery, sec. 6-3, propiedades de la tabla 6-3.", size=12)], ratio=0.5)

_rows = [[w, f"{c61[w]:d}".replace("-", M), f(c61[w] / 8), f(c61[w] ** 2 / 16),
          f(100 * c61[w] ** 2 / 16 / 78, 2) + " %"] for w in w61]
P("Del contraste al efecto, a la suma de cuadrados y al coeficiente",
  """Una vez armada la tabla, todos los cálculos de un 2^{k} salen de los contrastes:

Contraste de X = Σ (signo de la columna X) × (total de la corrida).
Efecto de X = Contraste / (n·2^{k−1}).
SS_{X} = Contraste^{2} / (n·2^{k}), con 1 grado de libertad.
Coeficiente de regresión β̂_{X} = Efecto / 2; el intercepto β̂_{0} es el promedio general.

El coeficiente es la mitad del efecto porque el efecto mide el cambio al pasar de x = −1 a x = +1 (dos unidades), y el coeficiente mide el cambio por unidad de x.

Ejemplo 6-1 de Montgomery (altura de llenado, 2^{3} con n = 2). Los totales en orden estándar son (1) = −4, a = 1, b = −1, ab = 5, c = −1, ac = 3, bc = 2 y abc = 11. Con los signos de la columna A: −(−4) + 1 − (−1) + 5 − (−1) + 3 − 2 + 11 = 24. Entonces A = 24/8 = 3.00 y SS_{A} = 24^{2}/16 = 36.00. La SS total es 78, así que A explica el 46 % de la variabilidad.

Atajo para escribir cualquier contraste sin la tabla: (a ± 1)(b ± 1)(c ± 1), con signo − en el paréntesis si el factor está en el efecto y + si no está. Por ejemplo, AB = (a − 1)(b − 1)(c + 1) = abc + ab + c + (1) − ac − bc − a − b.""",
  left=[form("Efecto = Contraste / (n·2^{k−1})", "SS = Contraste^{2} / (n·2^{k})",
             "β̂ = Efecto / 2,   β̂_{0} = ȳ", size=17),
        form("Contraste_{AB} = (a − 1)(b − 1)(c + 1)", size=16)],
  right=[tab(["Término", "Contraste", "Efecto", "SS", "% de SS_{T}"], _rows, size=14, first_left=False),
         txt("SS_{T} = 78.00; error puro = 5.00 con 8 g.l. Fuente: Montgomery, ej. 6-1, tabla 6-5, ecs. 6-18, 6-21 a 6-23.", size=12)],
  ratio=0.46)

_rows = []
for k in range(2, 8):
    from math import comb
    _rows.append([str(k), str(2 ** k), str(2 ** k - 1), str(k), str(comb(k, 2)), str(comb(k, 3)),
                  str(2 ** k - 1 - k - comb(k, 2) - comb(k, 3))])
P("¿Cuántos efectos estima un 2^{k} y cuáles importan?",
  """Un 2^{k} tiene 2^{k} − 1 grados de libertad entre sus corridas y estima exactamente 2^{k} − 1 efectos, cada uno con 1 grado de libertad: k efectos principales, C(k, 2) interacciones de dos factores, C(k, 3) de tres factores, y así hasta una interacción de los k factores.

La tabla muestra que el número de interacciones de orden alto crece mucho más rápido que el de efectos principales. Dos principios empíricos permiten no preocuparse por ellas:

Escasez (o esparcimiento) de efectos: un sistema suele estar dominado por unos pocos efectos principales e interacciones de orden bajo; las interacciones de tres o más factores casi siempre son despreciables.

Jerarquía: si una interacción entra al modelo, se incluyen también sus efectos principales, aunque no sean significativos.

El tema 6 se apoya justamente en la escasez de efectos: si casi todos los grados de libertad se gastan en interacciones que son prácticamente cero, se puede correr una fracción del diseño y aceptar que esas interacciones queden mezcladas (aliadas) con los efectos que sí interesan.""",
  body=[tab(["k", "Corridas 2^{k}", "Efectos 2^{k} − 1", "Principales", "Dobles", "Triples", "4 o más"],
            _rows, size=15, first_left=False),
        note("En un 2^{7} solo **28 de los 127 efectos** son principales o dobles: los otros 99 suelen ser ruido", size=15),
        txt("Fuente: Montgomery, sec. 6-4 (tabla 6-9) y sec. 6-5 (principio de efectos esparcidos); jerarquía en «Reglas y advertencias», cap. 6.", size=12)])

_v = [e62[w] for w in w62]
_z = normal_scores(_v)
_srt = sorted(range(15), key=lambda i: _v[i])
P("Una sola réplica: la gráfica normal de efectos",
  f"""Con k moderado muchas veces solo se puede correr una réplica (n = 1). Entonces no hay error puro: cada uno de los 2^{{k}} − 1 grados de libertad se gasta en un efecto y no sobra ninguno para estimar σ^{{2}}. Esta es exactamente la situación de casi todos los factoriales fraccionados.

La salida es la gráfica de probabilidad normal de los efectos (Daniel). Si un efecto es nulo, su estimación es solo ruido: una variable normal de media cero. Los efectos nulos caen entonces sobre una recta que pasa cerca del cero, y los efectos activos se apartan de ella. La recta se traza solo con los efectos pequeños, no con todos: si se ajustara con todos, los activos la inclinarían y parecerían menos alejados. Los efectos que se apartan forman el modelo; el resto se combina como estimación del error. Es la primera clasificación de los términos para el ANOVA.

En el ejemplo 6-2 de Montgomery (índice de filtración, 2^{{4}} no replicado) se apartan A = {f(e62['A'], 3)}, AC = {f(e62['AC'], 3)}, AD = {f(e62['AD'], 3)}, D = {f(e62['D'], 3)} y C = {f(e62['C'], 3)}. El método de Lenth hace lo mismo de forma numérica: estima un pseudo error estándar PSE con la mediana de los efectos pequeños y declara activos los que superan el margen de error ME = t·PSE. Aquí PSE = {f(pse62, 3)} y ME = {f(me62)}.

La gráfica normal, Lenth y la gráfica seminormal (valores absolutos) se usan sin cambios en el tema 6.""",
  left=[scatter(_p62 := [(_v[i], _z[i]) for i in _srt], "Efecto", "Puntuación normal",
                labels={k: w62[i] for k, i in enumerate(_srt) if w62[i] in ("A", "C", "D", "AC", "AD")},
                line=daniel(_p62, _a62 := {k for k, i in enumerate(_srt) if w62[i] in ("A", "C", "D", "AC", "AD")}),
                hi=_a62, title="Gráfica normal con recta de Daniel · ejemplo 6-2")],
  right=[bul("n = 1 → **no hay error puro**",
             "Efectos nulos ≈ normal(0, σ^{2}) → caen **sobre una recta**",
             "Efectos activos → **se apartan** de la recta: van al **modelo**; los demás, al **error**",
             f"Lenth: PSE = {f(pse62, 3)}, ME = {f(me62)}", size=15),
         txt("Fuente: Montgomery, sec. 6-5, ej. 6-2, tabla 6-12 y fig. 6-11; Lenth en la misma sección.", size=12)],
  ratio=0.52)

P("Proyección: quitar un factor duplica las réplicas",
  """Si en un 2^{k} con una réplica un factor y todas sus interacciones resultan despreciables, ese factor se puede eliminar del análisis. Lo que queda es un factorial completo en los k − 1 factores restantes, con dos réplicas. En general, quitar h factores convierte un 2^{k} no replicado en un 2^{k−h} completo con 2^{h} réplicas.

En el ejemplo 6-2, B y todas sus interacciones son pequeñas. Al eliminar B, el 2^{4} se proyecta en un 2^{3} en A, C y D con dos réplicas (las corridas que solo difieren en b, como (1) y b, pasan a ser réplicas). Ahora sí hay error con 8 grados de libertad y se puede hacer un ANOVA formal.

En el tema 6 la proyección reaparece con más fuerza: una fracción de resolución R se proyecta en un factorial completo en cualquier subconjunto de R − 1 factores. Por eso un diseño de tamizado no se desperdicia aunque solo unos pocos factores resulten activos.""",
  left=[form("2^{k} con n = 1, sin h factores", "→  2^{k−h} con 2^{h} réplicas", size=17),
        tab(["Fuente", "SS", "g.l.", "MS", "F_{0}"],
            [["A", "1870.56", "1", "1870.56", "83.36"], ["C", "390.06", "1", "390.06", "17.38"],
             ["D", "855.56", "1", "855.56", "38.13"], ["AC", "1314.06", "1", "1314.06", "58.56"],
             ["AD", "1105.56", "1", "1105.56", "49.27"], ["CD", "5.06", "1", "5.06", "< 1"],
             ["ACD", "10.56", "1", "10.56", "< 1"], ["Error", "179.52", "8", "22.44", ""],
             ["Total", "5730.94", "15", "", ""]], size=13, first_left=True)],
  right=[note("Al quitar B, el 2^{4} se vuelve un **2^{3} en A, C, D con 2 réplicas**", size=15),
         tab(["Corrida del 2^{3} (A, C, D)", "Corridas del 2^{4} que reúne"],
             [["(1)", "(1), b"], ["a", "a, ab"], ["c", "c, bc"], ["ac", "ac, abc"],
              ["d", "d, bd"], ["ad", "ad, abd"], ["cd", "cd, bcd"], ["acd", "acd, abcd"]],
             size=13, first_left=False),
         txt("Fuente: Montgomery, sec. 6-5, ej. 6-2, tabla 6-13.", size=12)], ratio=0.55)

P("Puente: del 2^{k} al 2^{k−p}",
  """Esta tabla traduce cada idea del 2^{k} a la forma en que aparece en el tema 6. Conviene tenerla a mano durante toda la exposición.""",
  body=[tab(["En el 2^{k} completo", "En el factorial fraccionado 2^{k−p}"],
            [["Tabla de signos con 2^{k} filas", "Se corre solo una parte: 2^{k−p} filas"],
             ["Columna de interacción = producto de columnas", "**Generador**: un factor nuevo se define con la columna de una interacción (D = ABC)"],
             ["Columna I, todo +", "**Relación de definición**: las palabras cuya columna es toda + en la fracción (I = ABCD)"],
             ["Letra^{2} = I (módulo 2)", "**Alias**: efecto × palabra (A × ABCD = BCD)"],
             ["Columnas distintas son ortogonales", "Dentro de la fracción, dos columnas pueden ser **idénticas**: son alias"],
             ["Contraste → efecto", "El contraste estima la **suma** de los efectos aliados (ℓ_{A} → A + BCD)"],
             ["2^{k} − 1 efectos, 1 g.l. cada uno", "2^{k−p} − 1 **cadenas de alias**, 1 g.l. cada una"],
             ["Escasez de efectos", "Justifica suponer nulas las interacciones de orden alto aliadas"],
             ["Una réplica: gráfica normal y Lenth", "Mismo análisis: casi todas las fracciones son no replicadas"],
             ["Proyección: quitar factores da réplicas", "Una fracción de resolución R es un factorial completo en R − 1 factores"]],
            size=14, colw=[0.4, 0.6])])

P("Autoevaluación antes de pasar al tema 6",
  """Si estas preguntas salen sin dudar, la notación del tema 6 no va a ser un obstáculo. Conviene responderlas antes de leer las respuestas.""",
  body=[num("En un 2^{4}, ¿qué factores están en nivel alto en la corrida bd?",
            "¿Qué lugar ocupa abc en el orden estándar del 2^{4}?",
            "En la fila ab de un 2^{3}, ¿cuál es el signo de la columna ABC?",
            "Simplifique ABD × BCD.",
            "¿Cuántas interacciones de dos factores tiene un 2^{6}?",
            "En un 2^{3} con n = 2 el contraste de un efecto vale 14. ¿Cuánto valen el efecto, su suma de cuadrados y su coeficiente de regresión?",
            "¿Por qué en la fracción un medio con I = ABC no se puede distinguir A de BC?", size=15),
        note("**Respuestas.** 1) B y D (A y C en bajo). 2) Es la octava corrida. 3) A = +, B = +, C = −, "
             "así que ABC = −. 4) ABD × BCD = AB^{2}CD^{2} = AC. 5) C(6, 2) = 15. 6) Efecto = 14/(2·4) = 1.75; "
             "SS = 14^{2}/16 = 12.25; β̂ = 0.875 (es el factor C del ejemplo 6-1). 7) Porque en las cuatro "
             "corridas con ABC = + las columnas A y BC son idénticas (A × ABC = BC): su contraste estima A + BC.", size=14)])
