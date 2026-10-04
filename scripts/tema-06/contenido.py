"""Contenido único de la exposición del tema 6 (factoriales fraccionados).

Cada diapositiva es un dict con título, bloques y un texto explicativo ("explica").
render_pptx.py lo convierte en la presentación y render_guia.py en la guía de estudio.
Marcado en los textos: ^{..} superíndice, _{..} subíndice, **..** negrita.
"""
import random
from doe import (basic, add_factor, effect, fit, lenth, t_ppf, f_ppf,
                 anderson_darling, bartlett, normal_scores)

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


def scatter(points, xlab, ylab, h=3.6, labels=None, line=None, title=None):
    return {"t": "chart", "kind": "scatter", "points": points, "xlab": xlab, "ylab": ylab,
            "h": h, "labels": labels or {}, "line": line, "title": title}


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


def section(n, title, sub):
    _sec[0] = title
    SLIDES.append({"kind": "section", "n": n, "title": title, "sub": sub, "sec": title,
                   "explica": ""})


def S(title, explica, body=None, left=None, right=None, ratio=0.5):
    SLIDES.append({"kind": "content", "title": title, "explica": explica.strip(),
                   "body": body, "left": left, "right": right, "ratio": ratio, "sec": _sec[0]})


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
resCp = [e for e, row in zip(m3["res"], r3) if row["C"] == 1]
resCm = [e for e, row in zip(m3["res"], r3) if row["C"] == -1]
bart3 = bartlett([resCp, resCm])
ab3 = {(a, b): sum(v for v, row in zip(y3, r3) if row["A"] == a and row["B"] == b) / 4
       for a in (-1, 1) for b in (-1, 1)}
ad3 = anderson_darling(m3["res"])

# Ejemplo 4: 2^(7-4) III y doblez completo, tiempo de enfoque del ojo (ej. 8-7)
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
  """La clase sigue el mismo orden que usamos en los temas anteriores: primero para qué sirve el diseño y en qué casos conviene, luego su vocabulario, después cómo se construye y cómo se corre, el modelo y las hipótesis, el análisis estadístico, los ejemplos, la verificación de supuestos, el manejo en Minitab y un cierre con las ideas clave.""",
  body=[cards(("1 · ¿Para qué sirven?", "El problema de las corridas y los casos de uso"),
              ("2 · Nomenclatura", "2^{k−p}, generador, alias, resolución"),
              ("3 · Construcción y protocolo", "Fracciones un medio, un cuarto y general"),
              ("4 · Modelo e hipótesis", "Qué se estima y qué se prueba"),
              ("5 · Análisis estadístico", "Contrastes, efectos, ANOVA, efectos activos"),
              ("6 · Ejemplos", "Resolución IV, V y un cuarto de fracción"),
              ("7 · Resolver ambigüedades", "Fracción alterna, doblez, Plackett-Burman"),
              ("8 · Supuestos", "Residuos, pruebas gráficas y analíticas"),
              ("9 · Minitab", "Crear el diseño, ingresar datos y analizar"),
              ("10 · Cierre", "Ideas clave y errores frecuentes"), size=15)])

# ------------------------------------------------------------------ 1
section(1, "¿Para qué sirven?", "El problema que resuelven y cuándo conviene usarlos")

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
  """Un factorial completo con N corridas tiene N − 1 grados de libertad para estimar efectos. La tabla muestra cómo se reparten. En un 2^{6} hay 63 grados de libertad, pero solo 6 corresponden a efectos principales y 15 a interacciones de dos factores; los 42 restantes se gastan en interacciones de tres o más factores, que casi nunca son importantes.

Si se acepta que esas interacciones de orden alto son despreciables, la información sobre efectos principales e interacciones dobles se puede obtener con una fracción del experimento.""",
  body=[tab(["Factores k", "Corridas 2^{k}", "Efectos principales", "Interacciones de 2 factores",
             "Interacciones de 3 o más", "% en orden alto"], _rows, size=16, hl=[2], first_left=False),
        note("En un 2^{6}, **42 de 63** grados de libertad estiman interacciones de tres o más factores, "
             "que rara vez importan. Esa es la información que el fraccionado sacrifica.")])

S("Tres ideas que justifican correr solo una fracción",
  """Escasez de efectos: cuando hay muchas variables, el sistema suele estar dominado por unos pocos efectos principales e interacciones de orden bajo.

Proyección: si algunos factores resultan inactivos, el fraccionado se convierte en un diseño más fuerte (incluso un factorial completo, a veces con réplicas) en los factores que sí importan.

Experimentación secuencial: no hay que correr todo de una vez. Se corre una fracción, se analiza y, si quedan dudas, se agrega otra fracción; juntas forman un diseño mayor que resuelve las ambigüedades.""",
  body=[cards(("Escasez de efectos",
               "De muchos factores, pocos son activos. Dominan los efectos principales y las interacciones de orden bajo."),
              ("Proyección",
               "Al descartar factores inactivos, la fracción se convierte en un factorial completo en los factores que quedan."),
              ("Experimentación secuencial",
               "Se corre una fracción, se analiza y se decide. Dos fracciones se combinan para resolver dudas."),
              size=22)])

S("¿Cuándo usar un factorial fraccionado?",
  """Conviene cuando hay muchos factores (en la práctica cinco o más), cuando cada corrida es costosa o lenta, cuando se está en una etapa exploratoria y cuando es razonable suponer que las interacciones de tres o más factores son despreciables.

No conviene cuando hay pocos factores y el factorial completo es barato, cuando se sabe que hay interacciones importantes entre muchos factores, o cuando se necesita un modelo detallado para optimizar: para eso están los factoriales completos y las superficies de respuesta, normalmente en una etapa posterior. Las conclusiones de un fraccionado son tentativas y deben confirmarse.""",
  left=[txt("**Úselo cuando…**", size=20),
        bul("Hay **muchos factores** candidatos (k ≥ 5 en la práctica)",
            "Cada corrida es **costosa o lenta**",
            "La etapa es **exploratoria**: interesa saber qué factores importan",
            "Es razonable despreciar interacciones de **tres o más** factores")],
  right=[txt("**Tenga cuidado cuando…**", size=20),
         bul("Hay pocos factores y el factorial completo es barato",
             "Se esperan interacciones entre muchos factores",
             "El objetivo es **optimizar**, no tamizar",
             "No habrá recursos para **confirmar** las conclusiones")])

# ------------------------------------------------------------------ 2
section(2, "Nomenclatura", "El vocabulario propio del diseño")

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
  """Generador: la interacción con la que se define un factor adicional (por ejemplo D = ABC). Escrito como I = ABCD se llama palabra.

Relación de definición: el conjunto de todas las palabras iguales a la identidad I; incluye los generadores y todos sus productos.

Alias: efectos que se estiman con la misma columna de signos y por tanto no se pueden distinguir. Una cadena de alias es el grupo completo de efectos que comparten columna.

Fracción principal: la que se obtiene con todos los generadores en signo positivo. Las demás son fracciones alternas; todas juntas forman la familia.

Diseño básico: el factorial completo en k − p factores sobre el que se construye la fracción. Diseño saturado: el que estudia k = N − 1 factores en N corridas.""",
  body=[tab(["Término", "Significado"],
            [["Generador", "Interacción con la que se define un factor adicional: D = ABC"],
             ["Palabra", "El generador escrito contra la identidad: I = ABCD"],
             ["Relación de definición", "Todas las palabras iguales a I (generadores y sus productos)"],
             ["Alias", "Efectos que comparten la misma columna de signos y no se distinguen"],
             ["Fracción principal", "La que usa todos los generadores con signo +"],
             ["Fracción alterna", "Cualquier otra de la misma familia (algún generador con signo −)"],
             ["Diseño básico", "Factorial completo en k − p factores sobre el que se construye"],
             ["Diseño saturado", "Estudia k = N − 1 factores en N corridas"]],
            size=16, colw=[0.26, 0.74])])

S("¿Qué es la resolución de un diseño?",
  """La resolución mide qué tan grave es la mezcla de efectos. Se escribe con número romano como subíndice y es igual al número de letras de la palabra más corta de la relación de definición.

Resolución III: los efectos principales no se confunden entre sí, pero sí con interacciones de dos factores. Resolución IV: los efectos principales quedan libres de interacciones dobles, pero las interacciones dobles se confunden entre sí. Resolución V: efectos principales e interacciones dobles quedan libres unos de otros; solo se confunden con interacciones de tres o más factores.

Regla práctica: usar la resolución más alta que permita el presupuesto de corridas.""",
  body=[tab(["Resolución", "Efectos principales", "Interacciones de 2 factores", "Ejemplo"],
            [["III", "Alias de interacciones de 2 factores", "Algunas son alias entre sí", "2^{3−1}_{III},  I = ABC"],
             ["IV", "Libres de interacciones de 2 factores", "Alias entre sí", "2^{4−1}_{IV},  I = ABCD"],
             ["V", "Libres de interacciones de 2 factores", "Libres entre sí; alias de las de 3 factores",
              "2^{5−1}_{V},  I = ABCDE"]], size=16, colw=[0.13, 0.3, 0.32, 0.25]),
        form("Resolución = número de letras de la palabra más corta de la relación de definición", size=18),
        note("A mayor resolución, menos supuestos hay que hacer sobre qué interacciones son despreciables.")])

# ------------------------------------------------------------------ 3
section(3, "Construcción y protocolo", "Cómo se arma la fracción y cómo se corre el experimento")

_r = basic(3)
_rows = []
_names = ["(1)", "a", "b", "ab", "c", "ac", "bc", "abc"]
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

_rows = [[str(i + 1), sg(r["A"]), sg(r["B"]), sg(r["C"]), sg(r["D"]), t]
         for i, (r, t) in enumerate(zip(r1, trat1))]
S("¿Cómo construyo una fracción un medio?",
  """Método del diseño básico. Primero se escribe el factorial completo en k − 1 factores: tiene el número correcto de corridas pero le falta una columna. Después se agrega el último factor igualando sus signos a los de la interacción de mayor orden de los demás. Para cuatro factores: se escribe el 2^{3} en A, B y C y se define D = ABC, lo que equivale a I = ABCD.

Usar la interacción de mayor orden garantiza la resolución más alta posible, que en una fracción un medio es igual a k. La fracción alterna se obtiene con D = −ABC.""",
  left=[num("Escribir el **diseño básico**: factorial completo en k − 1 factores",
            "Agregar el factor k con los signos de la **interacción de mayor orden**",
            "Para la fracción alterna, usar el signo contrario"),
        form("D = ABC   ⇔   I = ABCD", size=20),
        note("La fracción un medio de mayor resolución tiene **resolución k**")],
  right=[tab(["Corrida", "A", "B", "C", "D = ABC", "Trat."], _rows, size=15)], ratio=0.5)

S("La fracción un cuarto: dos generadores",
  """Para una fracción 1/4 se necesitan dos generadores, P y Q. Su producto PQ, la interacción generalizada, también pertenece a la relación de definición: I = P = Q = PQ. Cada efecto tiene entonces tres alias.

Ejemplo: 2^{6−2} con E = ABC y F = BCD. Las palabras son ABCE, BCDF y su producto ADEF. La palabra más corta tiene cuatro letras, así que es resolución IV: los efectos principales son alias de interacciones triples y las interacciones dobles son alias entre sí.

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
         txt("Alias hasta interacciones de tres factores", size=13)], ratio=0.48)

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

La tabla compara tres diseños 2^{7−2} de resolución IV. El diseño C tiene una sola palabra de cuatro letras, frente a tres y dos de los diseños A y B; por eso deja menos interacciones dobles confundidas entre sí y es el preferido. En la práctica no hay que buscar los generadores: las tablas de diseños recomendados y Minitab ya entregan el diseño de máxima resolución y aberración mínima.""",
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
  """Esta tabla reúne los diseños de máxima resolución y aberración mínima para 3 a 8 factores con un máximo de 32 corridas. Se lee por filas: número de factores, diseño con su resolución, corridas y generadores. Todos los generadores admiten signo positivo o negativo; con todos positivos se obtiene la fracción principal. Son los mismos generadores que Minitab usa por defecto.""",
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

S("¿Cuántos factores caben en N corridas?",
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

S("La propiedad de proyección",
  """Un diseño de resolución R contiene un factorial completo en cualquier subconjunto de R − 1 factores. Si al analizar resulta que solo unos pocos factores son activos, se descartan los demás y el diseño se convierte, sin correr nada más, en un factorial completo (posiblemente con réplicas) en los factores activos.

En general, un 2^{k−p} se proyecta en un factorial completo en cualquier subconjunto de factores que no forme una palabra de la relación de definición. Consecuencia práctica: al asignar los factores a las columnas conviene que los que se creen más importantes no formen juntos una palabra.""",
  left=[bul("Resolución **R** ⇒ factorial completo en cualquier subconjunto de **R − 1** factores",
            "Al descartar factores inactivos se ganan **réplicas** sin correr nada más",
            "Falla solo si los factores activos forman una **palabra** de la relación de definición"),
        note("Asigne los factores que cree importantes de modo que **no formen una palabra**")],
  right=[tab(["Diseño", "Se proyecta en…"],
             [["2^{3−1}_{III}", "2^{2} completo en cualquier par de factores"],
              ["2^{4−1}_{IV}", "2^{3} completo en cualesquiera tres factores"],
              ["2^{5−1}_{V}", "2^{4} completo en cuatro factores; dos réplicas de un 2^{3} en tres"],
              ["2^{6−2}_{IV}", "Dos réplicas de un 2^{3} en cualesquiera tres factores"],
              ["2^{7−4}_{III}", "Dos réplicas de un 2^{2} en cualquier par de factores"]],
             size=15, colw=[0.27, 0.73])], ratio=0.46)

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
        note("¡Forme bloques con lo que pueda y aleatorice lo que no pueda!")],
  right=[tab(["Orden de corrida", "Orden estándar", "A", "B", "C", "D", "Respuesta"], _rows,
             size=15, first_left=False),
         txt("Ejemplo de orden aleatorio para un 2^{4−1} (D = ABC)", size=13)], ratio=0.45)

# ------------------------------------------------------------------ 4
section(4, "Modelo e hipótesis", "Qué se estima y qué se prueba")

S("¿Cuál es el modelo matemático del diseño?",
  """El modelo es el mismo del factorial 2^{k}: un modelo de regresión en variables codificadas, donde cada x vale −1 o +1. β_{0} es la media general, cada β_{j} es la mitad del efecto principal del factor j y cada β_{ij} es la mitad del efecto de la interacción. El error ε se supone normal, independiente, con media cero y varianza constante σ².

La diferencia con el factorial completo es que no todos los términos se pueden estimar por separado. Cada columna del diseño estima una cadena de alias completa: el efecto que nos interesa más todos sus alias. El modelo final incluye un solo término por cadena, el que se juzga más razonable.""",
  body=[form("Y = β_{0} + Σ β_{j} x_{j} + ΣΣ β_{ij} x_{i} x_{j} + ε", "ε ~ NID(0, σ^{2})", size=24),
        bul("**x_{j}** = −1 (nivel bajo) o +1 (nivel alto) del factor j",
            "**β_{0}**: media general;  **β_{j}** = efecto / 2;  **β_{ij}** = efecto de interacción / 2",
            "En la fracción cada columna estima una **cadena de alias**:  ℓ_{A} → A + BCD",
            "El modelo final lleva **un término por cadena**: el más razonable"),
        note("Se supone que las interacciones de orden alto de cada cadena son despreciables")])

S("¿Cuál es la hipótesis del diseño?",
  """Se plantea una hipótesis por cada cadena de alias que se quiere probar. La hipótesis nula dice que el efecto es cero y la alterna que es distinto de cero; se puede escribir en términos del coeficiente o del efecto, que son equivalentes.

Lo que realmente se prueba es la cadena completa: rechazar H_{0} para la columna de A significa que A + BCD es distinto de cero. Atribuirlo a A es una decisión del analista, apoyada en el supuesto de que BCD es despreciable.

Regla de decisión: se rechaza H_{0} si F_{0} supera el valor crítico F_{α, 1, gl del error}, o de forma equivalente si el valor p es menor que α = 0.05.""",
  left=[form("H_{0}: β_{j} = 0", "H_{A}: β_{j} ≠ 0", size=26),
        txt("Una hipótesis por cada cadena de alias que entra al modelo", size=16),
        form("Se rechaza H_{0} si  F_{0} > F_{α, 1, gl del error}", "o si  valor p < α", size=20)],
  right=[bul("Equivale a probar que el **efecto** es cero",
             "Se prueba la **cadena completa**: A + BCD, no A sola",
             "Asignarlo a A exige suponer que BCD es **despreciable**",
             "Nivel de significancia habitual: **α = 0.05**"),
         note("H_{0}: el factor no afecta la respuesta.  H_{A}: el factor sí la afecta.")])

# ------------------------------------------------------------------ 5
section(5, "Análisis estadístico", "De los datos a los efectos activos")

S("¿Cómo debo analizar los datos recolectados?",
  """La ruta de análisis tiene siete pasos. Se calculan los contrastes y los efectos de todas las cadenas de alias. Se identifican los efectos activos: si no hay réplicas, con la gráfica de probabilidad normal o seminormal y el diagrama de Pareto. Se interpreta cada cadena activa para decidir a qué efecto se atribuye. Se ajusta el modelo reducido y se construye la tabla ANOVA, usando los efectos descartados como error. Se verifican los supuestos con los residuos. Se interpretan los efectos con gráficas de efectos principales, de interacción y de cubo. Por último se informa la conclusión en términos del problema del investigador y se confirma.""",
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
             ["Coeficiente", "β_{i} = ℓ_{i} / 2", "Cambio en Y por unidad codificada", f"19.00 / 2 = {f(_e / 2)}"],
             ["Suma de cuadrados", "SS_{i} = (Contraste_{i})^{2} / N", "Variabilidad explicada (1 g.l.)",
              f"76^{{2}} / 8 = {f(_s, 1)}"]], size=16, colw=[0.16, 0.26, 0.27, 0.31]),
        note("Con una sola réplica, N = 2^{k−p}. El intercepto es el promedio general:  β_{0} = ȳ")])

S("Tabla ANOVA del factorial fraccionado",
  """Cada efecto que entra al modelo aporta una fila con un grado de libertad; su cuadrado medio es igual a su suma de cuadrados. El error se obtiene por sustracción: la suma de cuadrados total menos las de los m efectos del modelo, con N − 1 − m grados de libertad. Ese error está formado por los efectos que se juzgaron inactivos.

El estadístico de prueba de cada efecto es F_{0} = MS del efecto / MS del error, que se compara con F de 1 y N − 1 − m grados de libertad.

Si el diseño tiene n réplicas, N = n·2^{k−p} y el error incluye además el error puro, con 2^{k−p}(n − 1) grados de libertad.""",
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

El método de Lenth, que usa Minitab para trazar la línea de referencia del diagrama de Pareto: estima un pseudo error estándar (PSE) a partir de la mediana de los efectos y declara activo todo efecto cuyo valor absoluto supere el margen de error.

Y los principios de interpretación de cadenas: escasez de efectos, jerarquía (los efectos de orden bajo son más probables) y herencia (una interacción es más creíble si sus factores tienen efecto principal).""",
  left=[bul("**Gráfica normal o seminormal de efectos**: los inactivos caen sobre una recta",
            "**Pareto con método de Lenth**: activo si |efecto| > margen de error",
            "Los efectos descartados pasan a formar el **error** del ANOVA"),
        form("s_{0} = 1.5 · mediana |ℓ_{i}|", "PSE = 1.5 · mediana { |ℓ_{i}| : |ℓ_{i}| < 2.5 s_{0} }",
             "ME = t_{0.025, m/3} · PSE", size=17)],
  right=[txt("**Para interpretar una cadena de alias**", size=18),
         cards(("Escasez", "Pocos efectos son realmente activos"),
               ("Jerarquía", "Los efectos de orden bajo son más probables que los de orden alto"),
               ("Herencia", "Una interacción es más creíble si sus factores tienen efecto principal"),
               size=15, cols=1)], ratio=0.54)

# ------------------------------------------------------------------ 6
section(6, "Ejemplos", "Media fracción de resolución IV y V, y un cuarto de fracción")

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

En la gráfica seminormal, los dos efectos pequeños quedan cerca del origen y los otros cinco se separan con claridad.

Interpretación de las cadenas: como B no tiene efecto, es más razonable atribuir AC + BD a AC y AD + BC a AD (principio de herencia). El modelo tentativo es A, C, D, AC y AD.""",
  left=[tab(["Columna", "Efecto", "Estima"],
            [[w, f(ef1[w][1]), alias1[w]] for w in ["A", "B", "C", "D", "AB", "AC", "AD"]],
            size=16, hl=[0, 2, 3, 5, 6], first_left=False),
        note("B es pequeño  →  AC + BD se atribuye a **AC** y AD + BC a **AD**", size=15)],
  right=[scatter([(abs(ef1[w][1]), z) for w, z in zip(_ord, _hs)], "|Efecto|", "Puntuación seminormal",
                 h=4.5, labels={i: w for i, w in enumerate(_ord)},
                 title="Gráfica seminormal de efectos")], ratio=0.46)

_an = [[t if len(t) == 1 else t, f(ss, 1), "1", f(ss, 1), f(F), pv(p)] for t, ss, _, _, F, p in m1["anova"]]
_an += [["Error", f(m1["sse"], 1), str(m1["dfe"]), f(m1["mse"]), "", ""],
        ["Total", f(m1["sst"], 1), "7", "", "", ""]]
S("Ejemplo 1 · ANOVA e interpretación",
  f"""Se ajusta el modelo con A, C, D, AC y AD. Los dos efectos descartados (B y AB) forman el error, con 2 grados de libertad. Los cinco términos son significativos al 5 %: todos tienen F_{{0}} mayor que F_{{0.05, 1, 2}} = {f(f_ppf(0.05, 1, 2))} y valores p menores que 0.01. El modelo explica el {100 * m1['r2']:.2f} % de la variabilidad.

Advertencia: con solo 2 grados de libertad en el error la prueba es poco potente y los supuestos apenas se pueden verificar; la conclusión es tentativa.

Interpretación: la temperatura (A) aumenta la filtración; el efecto de la concentración (C) depende de la temperatura (interacción AC negativa) y el de la agitación (D) también (interacción AD positiva). La presión (B) no influye, de modo que el diseño se proyecta en un 2^{{3}} completo en A, C y D. La mejor condición es A alto, C bajo y D alto. El factorial completo original llegó a las mismas conclusiones con el doble de corridas.""",
  left=[tab(["SV", "SS", "DF", "MS", "F_{0}", "P-Value"], _an, size=15),
        form("ŷ = 70.75 + 9.50 x_{1} + 7.00 x_{3} + 8.25 x_{4} − 9.25 x_{1}x_{3} + 9.50 x_{1}x_{4}", size=15)],
  right=[bul(f"Todos los términos: F_{{0}} > F_{{0.05, 1, 2}} = {f(f_ppf(0.05, 1, 2))}  →  se rechaza H_{{0}}",
             f"R^{{2}} = {100 * m1['r2']:.2f} %;  R^{{2}} ajustado = {100 * m1['r2adj']:.2f} %",
             "B no influye: el diseño se **proyecta** en un 2^{3} completo en A, C, D",
             "Mejor condición: **A alto, C bajo, D alto**", size=17),
         note("Solo 2 g.l. en el error: conclusión **tentativa**, hay que confirmar", size=15)],
  ratio=0.56)

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
  f"""Con una sola réplica y 15 efectos estimados no hay error, así que se usa la gráfica de probabilidad normal de los efectos. Once efectos caen sobre una recta alrededor de cero; cuatro se separan claramente: B (33.88), A (11.13), C (10.88) y AB (6.88).

El método de Lenth coincide: el pseudo error estándar es PSE = {f(pse2, 4)} y el margen de error es ME = {f(me2)}; solo esos cuatro efectos lo superan.

Como el diseño es de resolución V, AB es alias de CDE, una interacción triple, y se atribuye sin ambigüedad a AB.""",
  left=[scatter([(_vals[i], _z[i]) for i in _srt], "Efecto", "Puntuación normal", h=4.6,
                labels={k: w2[i] for k, i in enumerate(_srt) if w2[i] in ("A", "B", "C", "AB")},
                title="Gráfica normal de efectos")],
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

_rows = [[w if w not in lab3 else lab3[w], f(ef3[w][1], 3), f(ef3[w][2], 2)]
         for w in sorted(w3, key=lambda w: -abs(ef3[w][1]))[:8]]
_an3 = [[t, f(ss, 2), "1", f(ss, 2), f(F), pv(p)] for t, ss, _, _, F, p in m3["anova"]]
_an3 += [["Error", f(m3["sse"], 2), str(m3["dfe"]), f(m3["mse"], 2), "", ""],
         ["Total", f(m3["sst"], 2), "15", "", "", ""]]
S("Ejemplo 3 · Contracción en moldeo por inyección",
  f"""En un proceso de moldeo por inyección las piezas se contraen demasiado. Se estudian seis factores: A temperatura del molde, B velocidad del tornillo, C tiempo de retención, D duración del ciclo, E tamaño del vaciadero y F presión de retención. Se corre un 2^{{6−2}} de resolución IV con E = ABC y F = BCD: 16 corridas en lugar de 64.

La tabla muestra los ocho efectos de mayor magnitud. Sobresalen B (35.63), A (13.88) y la cadena AB + CE (11.88). Como A y B son activos y C y E no, la cadena se atribuye a AB.

El ANOVA del modelo A, B, AB confirma que los tres términos son significativos (F_{{0.05, 1, 12}} = {f(f_ppf(0.05, 1, 12))}), con R² = {100 * m3['r2']:.2f} %. Fuente: Montgomery, ejemplo 8-4.""",
  left=[bul("Respuesta: **contracción** de la pieza (se quiere reducir)",
            "Seis factores en 16 corridas: **E = ABC, F = BCD**",
            "Resolución IV: I = ABCE = BCDF = ADEF", size=17),
        tab(["Cadena", "Efecto", "SS"], _rows, size=14, hl=[0, 1, 2], first_left=False)],
  right=[tab(["SV", "SS", "DF", "MS", "F_{0}", "P-Value"], _an3, size=15),
         form("ŷ = 27.31 + 6.94 x_{1} + 17.81 x_{2} + 5.94 x_{1}x_{2}", size=16),
         note("AB + CE se atribuye a **AB**: A y B son activos, C y E no", size=15)], ratio=0.46)

S("Ejemplo 3 · Interacción AB y dispersión",
  """Gráfica de interacción: con la velocidad del tornillo baja (B −), la contracción es pequeña y casi no depende de la temperatura; con B alta, la contracción es grande y muy sensible a la temperatura. La recomendación para reducir la contracción media es trabajar con B en nivel bajo.

Los residuos contra el tiempo de retención (C) muestran algo más: con C bajo los residuos están muy concentrados y con C alto están mucho más dispersos. C no afecta la media de la contracción, pero sí su variabilidad: es un efecto de dispersión. Conclusión: B bajo para reducir la contracción media y C bajo para reducir la variabilidad entre piezas.""",
  left=[lines(["A bajo (−)", "A alto (+)"],
              [("B bajo (−)", [ab3[(-1, -1)], ab3[(1, -1)]]), ("B alto (+)", [ab3[(-1, 1)], ab3[(1, 1)]])],
              "Contracción promedio", h=4.3, title="Interacción AB"),
        note("Con **B bajo** la contracción es pequeña a cualquier temperatura", size=15)],
  right=[scatter([(row["C"], e) for row, e in zip(r3, m3["res"])], "Nivel de C (tiempo de retención)",
                 "Residuo", h=4.3, title="Residuos contra el factor C"),
         note("Con **C alto** los residuos se dispersan mucho más", size=15)], ratio=0.5)

# ------------------------------------------------------------------ 7
section(7, "Resolver ambigüedades", "Fracción alterna, doblez y diseños de Plackett-Burman")

S("¿Qué hago si los alias me dejan dudas?",
  """Las conclusiones de un fraccionado son tentativas porque siempre existe una explicación alternativa basada en los alias. Hay cuatro formas de resolver la duda, de menor a mayor costo.

Corrida de confirmación: predecir con el modelo la respuesta en una condición nueva y comprobarla. Fracción alterna: en una fracción un medio, correr la otra mitad completa el factorial. Doblez completo: correr una segunda fracción con los signos de todos los factores invertidos; separa los efectos principales de las interacciones dobles y convierte un diseño de resolución III en uno de resolución IV. Doblez de un factor: invertir los signos de un solo factor; deja limpio ese factor y todas sus interacciones dobles.

En todos los casos las dos fracciones se combinan con la semisuma y la semidiferencia de las estimaciones.""",
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

_rows = []
for w in ["A", "B", "C", "D", "AB", "AC", "AD"]:
    a, b = ef1[w][1], ef1b[w][1]
    al = alias1[w].split(" + ")
    _rows.append([w, f(a), f(b), f"{al[0]} = {f((a + b) / 2)}", f"{al[1]} = {f((a - b) / 2)}"])
S("Ejemplo 1 · Agregar la fracción alterna",
  """Para no depender del juicio del analista se corre la fracción alterna, con D = −ABC. Sus estimaciones ℓ′ tienen los alias con signo contrario: ℓ′_{A} estima A − BCD.

La semisuma de las dos estimaciones aísla el primer efecto de cada cadena y la semidiferencia el segundo. El resultado confirma la interpretación inicial: AC = −18.13 mientras BD = −0.38, y AD = 16.63 mientras BC = 2.38. Las interacciones reales eran AC y AD.

Las 16 corridas forman el factorial 2^{4} completo, corrido en dos bloques con ABCD confundida con bloques.""",
  body=[tab(["Columna", "ℓ  (I = ABCD)", "ℓ′  (I = −ABCD)", "½ (ℓ + ℓ′)", "½ (ℓ − ℓ′)"], _rows, size=16,
            hl=[5, 6], first_left=False),
        note("Se confirma la interpretación: las interacciones activas son **AC** y **AD**, no BD ni BC")])

_rows = [[str(i + 1)] + [sg(r[c]) for c in "ABCDEFG"] for i, r in enumerate(r4)]
S("Resolución III saturada: el 2^{7−4}",
  """Los diseños de resolución III permiten estudiar hasta k = N − 1 factores en N corridas. El 2^{7−4} estudia siete factores en solo ocho corridas: se escribe el 2^{3} completo en A, B y C y se definen D = AB, E = AC, F = BC y G = ABC. Se dice que el diseño está saturado porque usa todos los grados de libertad para efectos principales.

El costo es alto: cada efecto principal es alias de tres interacciones dobles. Solo sirve si se puede suponer que las interacciones son despreciables o si se planea un doblez posterior.""",
  left=[tab(["Corrida", "A", "B", "C", "D = AB", "E = AC", "F = BC", "G = ABC"], _rows, size=14,
            first_left=False),
        note("**Saturado**: 7 factores en 8 corridas (k = N − 1)", size=15)],
  right=[tab(["Columna", "Estima"], [[w, f"{w} + {alias4[w]}"] for w in "ABCDEFG"], size=15,
             first_left=False),
         txt("Alias despreciando interacciones de tres o más factores", size=13)], ratio=0.56)

_o4 = sorted("ABCDEFG", key=lambda w: abs(ef4[w]))
S("Ejemplo 4 · Una primera fracción ambigua",
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
S("Ejemplo 4 · El doblez completo resuelve la duda",
  """Se corre una segunda fracción de ocho corridas con los signos de todos los factores invertidos. En ella cada efecto principal aparece con sus interacciones dobles con signo negativo, de modo que la semisuma aísla el efecto principal y la semidiferencia aísla el grupo de interacciones.

Resultado: los efectos principales grandes son B = 38.05 y D = 29.38. El efecto de A es solo 1.48; lo que parecía el efecto de A era en realidad la cadena BD + CE + FG = 19.15, que se atribuye a BD porque B y D son activos. La explicación correcta era la cuarta.

Las 16 corridas forman un 2^{7−3} de resolución IV: el doblez completo de un diseño de resolución III siempre produce uno de resolución IV.""",
  body=[tab(["Columna", "ℓ  (1.ª fracción)", "ℓ′  (doblez)", "½ (ℓ + ℓ′)", "½ (ℓ − ℓ′)"], _rows, size=15,
            hl=[0, 1, 3], colw=[0.12, 0.17, 0.17, 0.2, 0.34], first_left=False),
        note("Activos: **B**, **D** y la interacción **BD**. El aparente efecto de A era BD. "
             "Diseño combinado: 2^{7−3} de resolución **IV**")])

S("Diseños de Plackett-Burman",
  """Son diseños de resolución III para estudiar k = N − 1 factores en N corridas, donde N es múltiplo de 4 y no solo potencia de 2: 12, 20, 24, 28, 36. Cubren los huecos entre 8, 16 y 32 corridas.

Se construyen a partir de un renglón generador que se desplaza cíclicamente una posición cada vez; al final se agrega un renglón con todos los signos negativos.

Advertencia: su estructura de alias es muy compleja. En el diseño de 12 corridas cada efecto principal es alias parcial de todas las interacciones dobles en las que no participa. Si hay interacciones importantes, pueden aparecer como falsos efectos principales. Úselos solo para tamizado cuando sea razonable suponer que no hay interacciones, y con mucho cuidado.""",
  left=[bul("Resolución III para **k = N − 1** factores en N corridas",
            "N **múltiplo de 4**: 12, 20, 24, 28, 36",
            "Se construye **desplazando cíclicamente** un renglón generador y agregando un renglón de signos −"),
        tab(["N", "Renglón generador"], [["12", "+ + − + + + − − − + −"],
             ["20", "+ + − − + + + + − + − + − − − − + + −"],
             ["24", "+ + + + + − + − + + − − + + − − + − + − − − −"]], size=14, colw=[0.1, 0.9], first_left=False)],
  right=[note("**Cuidado:** cada efecto principal es **alias parcial** de muchas interacciones dobles. "
              "Una interacción real puede aparecer como varios falsos efectos principales.", size=17),
         bul("Úselos solo para **tamizado**, suponiendo que no hay interacciones",
             "Si la diferencia de corridas es pequeña, prefiera un **2^{k−p}**", size=17)], ratio=0.52)

# ------------------------------------------------------------------ 8
section(8, "Supuestos", "Qué debemos verificar sobre el modelo")

S("¿Qué debemos verificar sobre el modelo?",
  """Las pruebas F del ANOVA son válidas si los errores son normales, tienen varianza constante y son independientes. Los errores no se observan, así que se trabaja con los residuos: la diferencia entre cada respuesta observada y el valor que predice el modelo ajustado.

Cada supuesto tiene una prueba gráfica y una analítica. Normalidad: gráfica de probabilidad normal de los residuos y prueba de Anderson-Darling (la que Minitab usa por defecto) o Shapiro-Wilk. Varianza constante: gráfica de residuos contra valores ajustados y contra cada factor, y prueba de Bartlett o de Levene. Independencia: gráfica de residuos contra el orden de corrida y prueba de Durbin-Watson.

En un fraccionado sin réplicas los residuos provienen de los efectos descartados; si el modelo deja pocos grados de libertad para el error, la verificación tiene poca potencia.""",
  left=[form("e = y − ŷ", size=26),
        txt("Residuo: respuesta observada menos valor ajustado por el modelo", size=16),
        note("Con pocos g.l. en el error, la verificación tiene **poca potencia**")],
  right=[tab(["Supuesto", "Prueba gráfica", "Prueba analítica"],
             [["Normalidad", "Probabilidad normal de residuos", "Anderson-Darling, Shapiro-Wilk"],
              ["Varianza constante", "Residuos contra ajustados y contra cada factor", "Bartlett, Levene"],
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

S("Ejemplo 3 · Cuando la varianza no es constante",
  f"""En el ejemplo 3 la gráfica de residuos contra el factor C mostró más dispersión con C alto. La prueba de Bartlett lo confirma. Hipótesis: H_{{0}}: las varianzas de los residuos son iguales en los dos niveles de C; H_{{A}}: son distintas.

La desviación estándar de los residuos es {f(bart3[3][0] ** 0.5)} con C alto y {f(bart3[3][1] ** 0.5)} con C bajo. El estadístico de Bartlett es {f(bart3[0])} con 1 grado de libertad y valor p = {f(bart3[2], 4)}: se rechaza H_{{0}}.

Aquí la violación del supuesto es en sí misma un hallazgo: el tiempo de retención no cambia la contracción media, pero sí su variabilidad. Para detectar este tipo de efecto en todas las columnas se usa el estadístico F* = ln[S²(+)/S²(−)]; los valores que se alejan de cero señalan efectos de dispersión.""",
  left=[form("H_{0}: σ^{2}(C+) = σ^{2}(C−)", "H_{A}: σ^{2}(C+) ≠ σ^{2}(C−)", size=20),
        tab(["Nivel de C", "Desv. estándar de residuos", "n"],
            [["C alto (+)", f(bart3[3][0] ** 0.5), "8"], ["C bajo (−)", f(bart3[3][1] ** 0.5), "8"]], size=16),
        tab(["Bartlett", "Valor"], [["Estadístico χ^{2}", f(bart3[0])], ["g.l.", "1"],
                                    ["Valor p", f(bart3[2], 4)]], size=16)],
  right=[note("Valor p < 0.05: **se rechaza H_{0}**. La varianza depende de C", size=17),
         bul("C no cambia la media, pero sí la **variabilidad**: efecto de dispersión",
             "Decisión: **C bajo** reduce la variabilidad entre piezas", size=17),
         form("F*_{i} = ln [ S^{2}(i+) / S^{2}(i−) ]", size=19),
         txt("Se calcula para cada columna; los valores lejos de cero señalan efectos de dispersión", size=15)],
  ratio=0.5)

S("¿Qué hago si se viola un supuesto?",
  """Si falla la normalidad: revisar datos atípicos y errores de registro, y considerar una transformación de la respuesta; el ANOVA es robusto a desviaciones moderadas.

Si la varianza no es constante: transformar la respuesta (logaritmo, raíz cuadrada, o Box-Cox para elegir la transformación) o, si la varianza depende de un factor, tratarlo como efecto de dispersión y aprovecharlo.

Si falla la independencia: es el problema más grave y no se corrige con el análisis. Suele deberse a no haber aleatorizado. Si existe una fuente identificable (tiempo, lote), puede incorporarse como bloque o covariable.

Si el modelo deja residuos con patrón: probablemente falta un término; hay que revisar las cadenas de alias y, si es necesario, agregar corridas.""",
  body=[tab(["Problema", "Síntoma", "Qué hacer"],
            [["No normalidad", "Curvatura o puntos alejados en la gráfica normal",
              "Revisar atípicos; transformar la respuesta"],
             ["Varianza no constante", "Embudo en residuos contra ajustados",
              "Transformar (logaritmo, raíz, Box-Cox) o tratar como efecto de dispersión"],
             ["Dependencia", "Tendencia o rachas contra el orden de corrida",
              "No se corrige en el análisis: aleatorizar; agregar bloque o covariable"],
             ["Modelo incompleto", "Patrón en los residuos",
              "Revisar cadenas de alias; agregar términos o corridas"]],
            size=16, colw=[0.2, 0.36, 0.44])])

# ------------------------------------------------------------------ 9
section(9, "Minitab", "Cómo crear el diseño, ingresar los datos y analizarlos")

S("Minitab en cinco pasos",
  """El trabajo en Minitab sigue cinco pasos. Crear el diseño: Minitab genera la matriz y el orden aleatorio. Ingresar la respuesta en la hoja de trabajo. Analizar el diseño: efectos, alias, ANOVA y gráficas de efectos. Verificar supuestos con las gráficas de residuos y las pruebas analíticas. Interpretar con gráficas factoriales y, si hace falta, agregar un doblez.

Los nombres de los menús corresponden a Minitab en español; pueden variar ligeramente entre versiones.""",
  body=[cards(("1 · Crear el diseño", "Estadísticas > DOE > Factorial > Crear diseño factorial"),
              ("2 · Ingresar la respuesta", "Una columna nueva en la hoja de trabajo"),
              ("3 · Analizar", "Estadísticas > DOE > Factorial > Analizar diseño factorial"),
              ("4 · Verificar supuestos", "Gráficas de residuos y prueba de normalidad"),
              ("5 · Interpretar y ampliar", "Gráficas factoriales; Modificar diseño > Doblar"),
              size=18, cols=3),
        txt("Los nombres de menú corresponden a Minitab en español y pueden variar entre versiones", size=13)])

S("Paso 1 · Crear el diseño",
  """Ruta: Estadísticas > DOE > Factorial > Crear diseño factorial. En tipo de diseño se deja «Factorial de 2 niveles (generadores predeterminados)» y se indica el número de factores.

En «Diseños» se elige la fracción: Minitab lista las opciones con sus corridas y su resolución; ahí mismo se definen réplicas, puntos centrales y bloques. En «Factores» se escribe el nombre real de cada factor y sus niveles bajo y alto. En «Opciones» se deja marcada la casilla de aleatorizar corridas y se elige la fracción (principal u otra) o el doblez. En «Resultados» se pide la estructura de alias.

Si se necesitan generadores propios, se usa el tipo «Factorial de 2 niveles (especificar generadores)».""",
  body=[path("Estadísticas", "DOE", "Factorial", "Crear diseño factorial…"),
        tab(["En el cuadro de diálogo", "Qué elegir"],
            [["Tipo de diseño", "Factorial de 2 niveles (generadores predeterminados)"],
             ["Número de factores", "El número k de factores del experimento"],
             ["Botón Diseños…", "La fracción (1/2, 1/4…): muestra corridas y resolución. Réplicas, puntos centrales, bloques"],
             ["Botón Factores…", "Nombre, tipo y niveles bajo y alto de cada factor"],
             ["Botón Opciones…", "Aleatorizar corridas; fracción principal u otra; doblar diseño"],
             ["Botón Resultados…", "Tabla de resumen y estructura de alias"]],
            size=16, colw=[0.27, 0.73])])

S("Paso 1 · ¿Qué fracciones ofrece Minitab?",
  """El botón «Mostrar diseños disponibles» abre una tabla que cruza el número de corridas con el número de factores e indica la resolución de cada combinación. Es la misma información de la tabla de diseños recomendados.

Se lee así: con 5 factores y 16 corridas el diseño es de resolución V; con 7 factores y 8 corridas es de resolución III. Minitab colorea las celdas: rojo para resolución III, amarillo para IV y verde para V o superior.""",
  body=[tab(["Corridas", "3 factores", "4 factores", "5 factores", "6 factores", "7 factores", "8 factores"],
            [["4", "III", "", "", "", "", ""],
             ["8", "Completo", "IV", "III", "III", "III", ""],
             ["16", "", "Completo", "V", "IV", "IV", "IV"],
             ["32", "", "", "Completo", "VI", "IV", "IV"]], size=18, first_left=False),
        note("Botón **Mostrar diseños disponibles…**: resolución de cada combinación de factores y corridas. "
             "Minitab colorea: rojo = III, amarillo = IV, verde = V o más"),
        bul("Elija la celda con la **mayor resolución** que permita su presupuesto de corridas", size=17)])

_ws = sorted([[str(i + 1), str(o), "1", "1", sg(r["A"]) + "1", sg(r["B"]) + "1", sg(r["C"]) + "1",
               sg(r["D"]) + "1", str(v)] for i, (r, o, v) in enumerate(zip(r1, orden, y1))],
             key=lambda z: int(z[1]))
S("Paso 2 · Hoja de trabajo e ingreso de datos",
  """Al aceptar, Minitab escribe el diseño en la hoja de trabajo. Las cuatro primeras columnas son de control: OrdenEst (orden estándar), OrdenCorrida (el orden aleatorio en que se debe ejecutar), PtCentral y Bloques. Luego viene una columna por factor.

La respuesta se digita en la primera columna libre, con un nombre descriptivo, en la fila de la corrida correspondiente. No se deben borrar ni reordenar a mano las columnas de control.

Si los datos ya existen en una hoja (por ejemplo, de un experimento corrido antes), no hace falta crear el diseño: se usa Estadísticas > DOE > Factorial > Definir diseño factorial personalizado, indicando qué columnas son los factores.""",
  left=[tab(["OrdenEst", "OrdenCorrida", "PtCentral", "Bloques", "A", "B", "C", "D", "Filtración"], _ws,
            size=14, first_left=False, colw=[0.13, 0.18, 0.14, 0.12, 0.06, 0.06, 0.06, 0.06, 0.19]),
        txt("Ejemplo 1 en la hoja de trabajo, ordenado por OrdenCorrida", size=13)],
  right=[bul("Columnas de control: **OrdenEst, OrdenCorrida, PtCentral, Bloques**",
             "Una columna por **factor**",
             "La **respuesta** se digita en la primera columna libre",
             "No reordenar ni borrar las columnas de control", size=16),
         note("Datos ya existentes: **Definir diseño factorial personalizado**", size=15)], ratio=0.67)

S("Paso 3 · Analizar el diseño",
  """Ruta: Estadísticas > DOE > Factorial > Analizar diseño factorial. En «Respuestas» se selecciona la columna de la respuesta.

En «Términos» se decide qué entra al modelo. En el primer análisis se incluyen todos los términos disponibles para ver todos los efectos; después se regresa y se dejan solo los activos, con lo cual los descartados pasan al error.

En «Gráficas» se marcan las gráficas de efectos (Pareto, normal y seminormal) y las gráficas de residuos «Cuatro en uno». En «Almacenamiento» se piden los ajustes y los residuos para las pruebas analíticas.""",
  body=[path("Estadísticas", "DOE", "Factorial", "Analizar diseño factorial…"),
        tab(["En el cuadro de diálogo", "Qué elegir"],
            [["Respuestas", "La columna con la respuesta"],
             ["Botón Términos…", "1.ª pasada: todos los términos.  2.ª pasada: solo los efectos activos"],
             ["Botón Gráficas…", "Gráficas de efectos: Pareto, Normal, Seminormal.  Residuos: Cuatro en uno"],
             ["Botón Almacenamiento…", "Ajustes y Residuos (para las pruebas de supuestos)"]],
            size=16, colw=[0.27, 0.73]),
        note("Sin réplicas, la primera pasada no da valores p: se decide con la gráfica normal y el Pareto")])

_lin = m1["ss"]["A"] + m1["ss"]["C"] + m1["ss"]["D"]
_int = m1["ss"]["AC"] + m1["ss"]["AD"]
from doe import f_sf as _fsf
def _p3(p):
    return f"{p:.3f}"


def _row(name, gl, ss, F=None, p=None):
    base = f"{name:<24}{gl:>4}{ss:>12.2f}{ss / gl:>11.2f}"
    return base + (f"{F:>9.2f}{_p3(p):>9}" if F is not None else "")


_mse = m1["mse"]
_L = ["Estructura de alias", "I + ABCD", "A + BCD        AB + CD", "B + ACD        AC + BD",
      "C + ABD        AD + BC", "D + ABC", "", "Análisis de Varianza",
      f"{'Fuente':<24}{'GL':>4}{'SC Ajust.':>12}{'MC Ajust.':>11}{'Valor F':>9}{'Valor p':>9}",
      _row("Modelo", 5, m1["ssm"], m1["Fm"], m1["pm"]),
      _row("  Lineal", 3, _lin, _lin / 3 / _mse, _fsf(_lin / 3 / _mse, 3, 2))]
for _t in ["A", "C", "D"]:
    _L.append(_row("    " + _t, 1, m1["ss"][_t], m1["ss"][_t] / _mse, _fsf(m1["ss"][_t] / _mse, 1, 2)))
_L.append(_row("  Interacciones de 2 t.", 2, _int, _int / 2 / _mse, _fsf(_int / 2 / _mse, 2, 2)))
for _t in ["AC", "AD"]:
    _L.append(_row("    " + _t[0] + "*" + _t[1], 1, m1["ss"][_t], m1["ss"][_t] / _mse,
                   _fsf(m1["ss"][_t] / _mse, 1, 2)))
_L += [_row("Error", 2, m1["sse"]), f"{'Total':<24}{7:>4}{m1['sst']:>12.2f}", "", "Resumen del modelo",
       f"{'S':>7}{'R-cuad.':>10}{'R-cuad.(ajustado)':>20}{'R-cuad.(pred)':>16}",
       f"{m1['S']:>7.5f}{100 * m1['r2']:>9.2f}%{100 * m1['r2adj']:>19.2f}%{100 * r2pred1:>15.2f}%"]
_out = "\n".join(_L)
S("Paso 4 · Leer la salida",
  """La salida tiene tres partes que hay que leer en orden. Primero la estructura de alias: confirma qué efectos están mezclados; hay que revisarla antes de interpretar cualquier efecto. Segundo, el análisis de varianza: cada término con sus grados de libertad, suma de cuadrados, F y valor p; se rechaza H_{0} para los términos con valor p menor que 0.05. Tercero, el resumen del modelo: S es la raíz del cuadrado medio del error y R-cuad el porcentaje de variabilidad explicada.

La salida mostrada es la que corresponde al modelo reducido del ejemplo 1; los valores se calcularon a partir de los datos y deben coincidir con los que entregue Minitab.""",
  left=[mono(_out, size=12)],
  right=[num("**Estructura de alias**: qué está mezclado con qué",
             "**Análisis de varianza**: valor p < 0.05  →  término significativo",
             "**Resumen del modelo**: S = raíz de MS_{E};  R-cuad = % explicado", size=16),
         note("Valores calculados a partir de los datos del ejemplo 1; verifíquelos en Minitab", size=14)],
  ratio=0.64)

S("Paso 5 · Gráficas, supuestos y doblez",
  """Para interpretar: las gráficas factoriales muestran los efectos principales y las interacciones; la gráfica de cubos muestra la respuesta media en cada vértice de los factores activos.

Para los supuestos: las gráficas de residuos «Cuatro en uno» se piden dentro del análisis; la prueba de normalidad se aplica a la columna de residuos almacenada, y la prueba de igualdad de varianzas compara la dispersión de los residuos entre niveles de un factor.

Para ampliar el experimento: Modificar diseño permite doblar el diseño (en todos los factores o en uno solo); Minitab agrega las corridas nuevas a la hoja. Los diseños de Plackett-Burman se crean desde el mismo cuadro de Crear diseño factorial, eligiendo ese tipo de diseño.""",
  body=[tab(["Para…", "Ruta en Minitab"],
            [["Efectos principales e interacciones", "Estadísticas > DOE > Factorial > Gráficas factoriales…"],
             ["Respuesta en cada vértice", "Estadísticas > DOE > Factorial > Gráfica de cubos…"],
             ["Residuos (normalidad, ajustes, orden)", "Analizar diseño factorial > Gráficas… > Cuatro en uno"],
             ["Prueba de normalidad", "Estadísticas > Estadísticas básicas > Prueba de normalidad…"],
             ["Igualdad de varianzas", "Estadísticas > ANOVA > Prueba de igualdad de varianzas…"],
             ["Doblez completo o de un factor", "Estadísticas > DOE > Modificar diseño… > Doblar diseño"],
             ["Plackett-Burman", "Crear diseño factorial… > Diseño de Plackett-Burman"]],
            size=16, colw=[0.36, 0.64])])

# ------------------------------------------------------------------ 10
section(10, "Cierre", "Lo que hay que recordar")

S("Lo que hay que recordar",
  """Un factorial fraccionado estudia muchos factores en pocas corridas a cambio de mezclar efectos. La notación 2^{k−p} dice cuántos factores, cuántos generadores y cuántas corridas. La relación de definición determina los alias y la resolución dice qué tan grave es la mezcla. El análisis es el del 2^{k}: contrastes, efectos, gráfica normal de efectos, ANOVA del modelo reducido y residuos. Las conclusiones son tentativas y se confirman con una fracción alterna, un doblez o una corrida de verificación.

Errores frecuentes: interpretar un efecto sin mirar sus alias; elegir una resolución III cuando se esperan interacciones; no aleatorizar o no guardar el orden de corrida; asignar los factores importantes a letras que forman una palabra; y dar por definitivas las conclusiones sin confirmar.""",
  left=[txt("**Ideas clave**", size=20),
        bul("Muchos factores en pocas corridas, **a cambio de alias**",
            "La **relación de definición** determina los alias",
            "La **resolución** dice qué tan grave es la mezcla",
            "Análisis: efectos → gráfica normal → ANOVA reducido → residuos",
            "Las conclusiones son **tentativas**: hay que confirmar", size=17)],
  right=[txt("**Errores frecuentes**", size=20),
         bul("Interpretar un efecto **sin revisar sus alias**",
             "Usar resolución III cuando se esperan interacciones",
             "No aleatorizar o no guardar el **orden de corrida**",
             "Asignar los factores importantes a letras que forman una **palabra**",
             "Dar por definitivo lo que no se ha confirmado", size=17)])

S("Referencias",
  """Los ejemplos numéricos y la teoría provienen de Montgomery (capítulos 6, 7 y 8); todos los cálculos (efectos, sumas de cuadrados, ANOVA, pruebas de supuestos) se rehicieron a partir de los datos. Los demás títulos son la bibliografía del curso recomendada para este tema, para quien quiera profundizar.""",
  left=[txt("**Fuente de la teoría y de los ejemplos**", size=20),
        bul("Montgomery, D. C. (2004). Diseño y análisis de experimentos, 2.ª ed. Limusa-Wiley. "
            "Capítulos 6, 7 y 8 (ejemplos 8-1, 8-2, 8-3, 8-4 y 8-7)", size=17),
        note("Todos los cálculos se rehicieron a partir de los datos", size=15)],
  right=[txt("**Bibliografía del curso para profundizar**", size=20),
         bul("Gutiérrez Pulido, H. y De la Vara Salazar, R. (2008). Análisis y diseño de experimentos. McGraw-Hill",
             "Box, G. E. P., Hunter, J. S. y Hunter, W. G. (2005). Statistics for Experimenters. John Wiley & Sons",
             "Grima, P., Marco, L. y Tort-Martorell, X. (2004). Estadística práctica con Minitab. Pearson",
             size=17)])

SLIDES.append({"kind": "closing", "title": "¿Preguntas?",
               "sub": "Diseños factoriales fraccionados 2^{k−p}", "sec": "", "explica": ""})
