"""Contenido único de la exposición del tema 6 (factoriales fraccionados 2^{k−p}).

Los bloques (S, E, tab, bul, …) están en bloques.py; render_pptx.py y render_guia.py
leen SLIDES, PREVIO y META de este módulo (o del que indique la variable CONTENIDO).
"""
import random
from doe import (basic, add_factor, effect, fit, lenth, t_ppf, f_ppf,
                 anderson_darling, normal_scores)

from bloques import *  # noqa: F401,F403

META = {"titulo": "Diseños factoriales fraccionados 2^{k−p}",
        "titulo_html": "Diseños factoriales fraccionados 2<sup>k−p</sup>",
        "pie": "Diseños factoriales fraccionados",
        "previo": "Antes de la presentación va la <b>Parte 0</b>, que no se proyecta: repasa el diseño "
                  "2<sup>k</sup> (notación, tabla de signos, contrastes) del que sale toda la terminología "
                  "de los fraccionados.",
        "previo_titulo": "Antes de empezar: el diseño 2<sup>k</sup>",
        "previo_sub": "Lo que hay que saber del factorial completo para entender los fraccionados. "
                      "Esta parte no se proyecta; es la base para leer el resto de la guía.",
        "previo_indice": "lo que hay que saber para entender la terminología de los fraccionados (no se proyecta)"}


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

S("¿Qué es la resolución de un diseño y qué supuestos exige?",
  """La resolución es una etiqueta que resume qué tan grave es la mezcla de efectos en un diseño fraccionado. Se escribe con número romano como subíndice: 2^{3−1}_{III} se lee «dos a la tres menos uno, resolución tres».

Montgomery la define así: un diseño es de resolución R cuando ningún efecto de p factores es alias de otro efecto que contenga menos de R − p factores. Leída de forma más sencilla: si dos efectos son alias, entre los dos suman al menos R letras.

Con esa lectura se entiende cada caso. En resolución III, un efecto principal (1 letra) no puede ser alias de otro principal (1 + 1 = 2 letras), pero sí de una interacción doble (1 + 2 = 3). En resolución IV, un principal solo puede ser alias de una interacción triple (1 + 3 = 4), y dos interacciones dobles sí pueden ser alias entre sí (2 + 2 = 4). En resolución V, un principal solo se mezcla con interacciones de cuatro factores y una doble con triples (2 + 3 = 5).

La resolución dice también qué hay que suponer despreciable para leer los resultados sin ambigüedad. Con resolución III, para interpretar un efecto principal hay que suponer que las interacciones dobles no existen; sirve para tamizar muchos factores cuando se cree que casi no hay interacciones. Con resolución IV basta suponer nulas las triples: los principales se estiman limpios y las dobles quedan en cadenas entre sí, de modo que se ve que una cadena es grande pero no cuál de sus interacciones la causa. Con resolución V, si las triples son despreciables, todos los principales y todas las dobles se estiman de forma única. Montgomery recomienda usar la resolución más alta que permita el grado de fraccionamiento: entre más alta, menos restrictivos son los supuestos necesarios para una interpretación única.""",
  left=[form("Si dos efectos son alias, entre los dos suman al menos **R** letras", size=19),
        bul("Se escribe como subíndice romano: **2^{3−1}_{III}**",
            "Definición del libro: ningún efecto de **p** factores es alias de otro con menos de **R − p** factores",
            "Cuanto **mayor** R, menos se mezclan los efectos de orden bajo", size=16)],
  right=[tab(["Resolución", "Un principal es alias de…", "Una doble es alias de…", "Para leer los principales se supone nula…"],
             [["III", "dobles (1 + 2 = 3)", "principales u otras dobles", "la interacción **doble**: tamizar sin interacciones esperadas"],
              ["IV", "triples (1 + 3 = 4)", "otras **dobles** (2 + 2 = 4)", "la **triple**: tamizar cuando puede haber interacciones"],
              ["V", "de 4 factores (1 + 4 = 5)", "triples (2 + 3 = 5)", "la de **cuatro** factores: estimar principales y dobles"]],
             size=14, colw=[0.15, 0.23, 0.24, 0.38]),
         note("Ningún principal es alias de **otro principal**. Regla: la **resolución más alta** que permita el "
              "presupuesto de corridas; a más resolución, menos supuestos", size=14)], ratio=0.42)

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

En la fracción alterna (I = −ABC) los alias cambian de signo: se estima A − BC. Si se corren las dos fracciones, la semisuma y la semidiferencia de las dos estimaciones separan A de BC: ½(ℓ_{A} + ℓ′_{A}) = ½(A + BC + A − BC) = A y ½(ℓ_{A} − ℓ′_{A}) = BC.

Las dos mitades del 2^{3} son igual de válidas. La fracción principal, I = +ABC, tiene las corridas a, b, c y abc; la alterna o complementaria, I = −ABC, tiene las otras cuatro: (1), ab, ac y bc. Montgomery señala que en la práctica no importa cuál de las dos se corra; ambas pertenecen a la misma familia. Si después de correr una se corre también la otra, se tienen las ocho corridas del 2^{3} completo, corrido en dos bloques de cuatro con ABC confundida con los bloques.""",
  left=[form("ℓ_{A} = ½ (a − b − c + abc) = ℓ_{BC}", size=20),
        bul("Dentro de la fracción, las columnas de **A** y de **BC** son idénticas",
            "No se estima A, sino **A + BC**",
            "**Regla:** multiplicar el efecto por la relación de definición (letra² = I)"),
        form("A · I = A · ABC = A^{2}BC = BC", size=20)],
  right=[tab(["", "Principal (I = ABC)", "Alterna (I = −ABC)"],
             [["ℓ_{A}", "A + BC", "A − BC"], ["ℓ_{B}", "B + AC", "B − AC"],
              ["ℓ_{C}", "C + AB", "C − AB"]], size=16, colw=[0.16, 0.42, 0.42], first_left=False),
         form("½ (ℓ_{A} + ℓ′_{A}) → A,     ½ (ℓ_{A} − ℓ′_{A}) → BC", size=16),
         note("Principal (a, b, c, abc) y alterna ((1), ab, ac, bc) son la misma **familia** y da igual cuál se corra; "
              "juntas forman el 2^{3} completo en **dos bloques** con ABC confundida", size=14)],
  ratio=0.5)

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
  """Con el enunciado de la diapositiva anterior: el factorial completo exigiría 16 corridas y se corre la fracción un medio con D = ABC, es decir I = ABCD, en 8 corridas.

Es un diseño de resolución IV: cada efecto principal es alias de una interacción triple, y las interacciones dobles son alias por pares (AB = CD, AC = BD, AD = BC). Fuente de los datos: Montgomery, ejemplo 8-1.""",
  left=[bul("Fracción un medio con **D = ABC**  (I = ABCD), 8 corridas",
            "**Resolución IV**: principales libres de interacciones dobles; las dobles, aliadas por pares"),
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
  """Con el enunciado de la diapositiva anterior: el factorial completo tendría 32 corridas y se corre la fracción un medio con E = ABCD (I = ABCDE) en 16 corridas. La tabla de la izquierda da los niveles de cada factor.

Es de resolución V: los efectos principales son alias de interacciones de cuatro factores y las interacciones dobles de interacciones triples. Si las interacciones de tres o más factores son despreciables, todos los efectos principales y todas las interacciones dobles se estiman limpios. Fuente: Montgomery, ejemplo 8-2.""",
  left=[bul("Cinco factores, 16 corridas: **E = ABCD**  (I = ABCDE)",
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

S("¿Qué opciones hay después de la primera fracción?",
  """El uso de fraccionados lleva con frecuencia a una gran economía, sobre todo si las corridas se pueden hacer en etapas. Con cuatro factores, en lugar de correr las 16 corridas del 2^{4}, Montgomery recomienda casi siempre correr primero la fracción 2^{4−1}_{IV} de 8 corridas, analizarla y después decidir. Si quedan ambigüedades, se corre la fracción alterna y se completa el 2^{4}: las dos mitades funcionan como bloques del diseño completo, con la interacción de mayor orden (ABCD) confundida con los bloques, y eso es lo único que se pierde por haber experimentado en dos etapas. Muchas veces la primera fracción basta para pasar a la etapa siguiente sin correr la segunda.

La figura 8-11 del libro, adaptada de Box (Sequential Experimentation and Sequential Assembly of Designs), resume las posibilidades de seguimiento después de un fraccionado inicial. Moverse a una nueva región para explorar una tendencia aparente de la respuesta. Agregar otra fracción para resolver las ambigüedades de la primera. Reescalar algunos factores, porque pudieron haberse variado en rangos inapropiados. Eliminar factores que resultaron insignificantes y agregar otros nuevos. Hacer réplicas para mejorar la precisión de las estimaciones o porque algunas corridas se hicieron mal. Y aumentar el diseño, por ejemplo con puntos centrales y axiales, para modelar una curvatura aparente.

La idea de fondo es que el primer experimento casi nunca es el último: sirve para aprender y orientar el siguiente.""",
  body=[note("Correr primero **una fracción** (con 4 factores, el 2^{4−1} de 8 corridas), analizarla y decidir. Si queda "
             "ambigüedad, la fracción alterna completa el 2^{4} y solo se pierde **ABCD**, confundida con los dos bloques", size=15),
        cards(("a · Moverse", "A una nueva región, para explorar una **tendencia** aparente de la respuesta"),
              ("b · Agregar otra fracción", "Para resolver las **ambigüedades** de la primera"),
              ("c · Reescalar factores", "Si sus niveles se eligieron en **rangos inapropiados**"),
              ("d · Eliminar y agregar factores", "Quitar los que no influyen y **probar otros**"),
              ("e · Hacer réplicas", "Para mejorar las estimaciones o **repetir corridas** mal hechas"),
              ("f · Aumentar el diseño", "Para modelar una **curvatura** aparente (Montgomery, fig. 8-11)"), size=15, cols=3)])

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

S("¿Qué es una fracción un cuarto? El 2^{6−2}_{IV}",
  """Con un número moderadamente grande de factores suelen convenir fracciones más pequeñas. Una fracción un cuarto del 2^{k} tiene 2^{k−2} corridas y necesita dos generadores, P y Q; las igualdades I = P e I = Q se llaman relaciones generadoras. Su producto PQ, la interacción generalizada, también pertenece a la relación de definición: I = P = Q = PQ, y cada efecto tiene tres alias, que se obtienen multiplicándolo por cada una de las tres palabras. Los signos de P y Q determinan cuál de las cuatro fracciones de la familia se obtiene; la que tiene P y Q positivos es la principal. Hay que elegir los generadores de modo que los efectos que pueden ser importantes no queden aliados entre sí.

Ejemplo: 2^{6−2} con E = ABC y F = BCD. Las palabras son ABCE, BCDF y su producto ADEF. La palabra más corta tiene cuatro letras, así que es resolución IV: los efectos principales son alias de interacciones de tres y cinco factores, y las interacciones dobles son alias entre sí y de interacciones de orden superior. Las 15 cadenas son seis de efectos principales, siete de interacciones dobles y dos formadas solo por interacciones triples.

Construcción: se escribe el 2^{4} completo en A, B, C y D (16 corridas) y se agregan las columnas E = ABC y F = BCD.""",
  left=[bul("**2^{k−2}** corridas, la cuarta parte: dos generadores **P** y **Q**; su producto **PQ** también es palabra",
            "Cada efecto tiene **tres alias** (efecto × cada palabra)",
            "Los signos de P y Q dan **4 fracciones**, una **familia**; +P, +Q es la principal", size=15),
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

Eso tiene una consecuencia práctica: las dos corridas de cada par se hicieron en las mismas condiciones de A, B y C, así que su diferencia es error puro. El fraccionado no replicado se convierte en un factorial replicado con 16 − 8 = 8 grados de libertad para el error, y el ANOVA ya no depende de descartar efectos.

Una pregunta frecuente: ¿cómo se sabe qué factores importan antes de correr? No hace falta saberlo. Antes de correr se aceptan dos principios generales, escasez de efectos (pocos factores importan) y jerarquía (las interacciones de tres o más factores casi siempre son despreciables), y con ellos se elige la resolución; si se sospecha que algunos factores importan más, se asignan a columnas que no formen una palabra. Se corre una sola vez la fracción y la gráfica de Daniel dice qué factores son activos. Recién entonces se pregunta qué diseño forman las corridas ya hechas en esos factores: eso es la proyección. Si los activos forman una palabra queda una ambigüedad entre alias, y se resuelve agregando corridas (fracción alterna o doblez) que se suman a las ya hechas; nunca se empieza de cero.""",
  left=[num("Decidir qué factores son **inactivos**",
            "**Borrar** sus columnas de la tabla del diseño",
            "**Contar** cuántas veces aparece cada combinación de signos en las columnas que quedan",
            "Leer el diseño que resulta: ¿están **todas** las combinaciones? ¿cuántas veces?", size=16),
        note("2^{6−2} con solo A, B, C activos: **8 combinaciones × 2 veces** = dos réplicas de un 2^{3}  →  **8 g.l. de error puro**", size=15)],
  right=[tab(["A", "B", "C", "Corridas", "Veces"],
             [[sg(k[0]), sg(k[1]), sg(k[2]), " y ".join(map(str, v)), str(len(v))] for k, v in _pABC],
             size=14, first_left=False, pad=0.08),
         txt("Corridas numeradas como en la tabla del 2^{6−2} (E = ABC, F = BCD)", size=12),
         note("La proyección **no se planea**: la gráfica de Daniel dice qué factores son activos y recién entonces se "
              "mira qué diseño forman las corridas **ya hechas**. Si los activos forman una palabra, se agregan corridas "
              "(alterna o doblez) que **se suman** a las anteriores", size=13)],
  ratio=0.5)

_pABCE = _proy("ABCE")
S("¿Por qué importa si los factores forman una palabra?",
  """Con cuatro factores activos el resultado depende de cuáles sean. Hay 2^{4} = 16 combinaciones posibles y 16 corridas, así que solo hay dos posibilidades: o aparecen todas una vez (factorial completo) o aparece la mitad dos veces (fracción replicada).

Si los cuatro factores son A, B, C y D, se obtienen las 16 combinaciones, una vez cada una: es el diseño básico. Lo mismo pasa con un subconjunto menos obvio, como A, B, E y F: también aparecen las 16 combinaciones.

Pero si los cuatro factores son A, B, C y E, solo aparecen 8 combinaciones, dos veces cada una. La razón es que ABCE es una palabra de la relación de definición: en todas las corridas el producto de los signos de A, B, C y E vale +1, porque E se construyó como ABC. Conocidos A, B y C, el signo de E queda fijado, y las combinaciones con E distinto de ABC nunca se corren. El resultado son dos réplicas de un 2^{4−1} con I = ABCE, y en él E sigue confundido con ABC.

Regla: un subconjunto de factores se proyecta en un factorial completo si no contiene ninguna palabra de la relación de definición. Por eso, al asignar factores a columnas, conviene que los que se creen más importantes no formen una palabra.

Resumen para el 2^{6−2} con I = ABCE = BCDF = ADEF: hay 15 subconjuntos de cuatro factores; tres son palabras (ABCE, BCDF y ADEF) y en ellos el diseño se pliega en dos réplicas de un 2^{4−1}; en los otros doce, como ABCD o ABCF, se proyecta en una réplica de un 2^{4} completo. En cualquier subconjunto de tres factores se proyecta en dos réplicas de un 2^{3}, porque al ser de resolución IV ninguna palabra tiene tres letras y ningún trío queda amarrado; en cualquier par, en cuatro réplicas de un 2^{2}, que es lo que pasa en el ejemplo 3 con A y B. En general, un 2^{k−2} se pliega en un factorial completo o en un fraccionado en cualquier subconjunto de r ≤ k − 2 factores.""",
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
         note("Factorial completo ⇔ el subconjunto **no contiene una palabra**. En el 2^{6−2}: de 15 subconjuntos de 4 "
              "factores, **12** dan un 2^{4} completo y **3** (las palabras) un 2^{4−1} replicado; cualquier trío, dos "
              "réplicas de un 2^{3}; cualquier par, cuatro réplicas de un 2^{2} (ejemplo 3)", size=13)],
  ratio=0.48)

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

S("¿Cómo se escogen los generadores?",
  """El procedimiento concreto tiene ocho pasos.

1. Fijar cuántos factores hay (k) y cuántas corridas se pueden pagar (N). Como N = 2^{k−p}, el número de generadores es p = k − log₂N. Con 6 factores y 16 corridas, p = 6 − 4 = 2.
2. Decidir la resolución mínima que se necesita, según las interacciones que se está dispuesto a despreciar: III si solo interesan los efectos principales (tamizado), IV si los principales deben quedar libres de interacciones dobles, V si también las interacciones dobles deben quedar libres entre sí.
3. Escribir el diseño básico: el factorial completo en los primeros k − p factores. En el ejemplo, el 2^{4} en A, B, C y D, con sus 16 corridas.
4. A cada factor que sobra se le asigna una columna de interacción del diseño básico: sus signos serán los de esa interacción. Si E = ABC, la columna de E es el producto de las columnas A, B y C, y el generador es I = ABCE (se multiplica E = ABC por E y E² = I). Cada factor nuevo debe usar una columna distinta.
5. Multiplicar los generadores entre sí, de dos en dos, de tres en tres, etc., cancelando las letras repetidas (A² = I). Así se obtiene la relación de definición completa, con 2^{p} − 1 palabras.
6. La resolución es la longitud de la palabra más corta. Si es menor que la requerida en el paso 2, se vuelve al paso 4 con otras columnas.
7. Si hay varios candidatos con la misma resolución, se escoge el de aberración mínima: el que tiene menos palabras de esa longitud mínima (siguiente diapositiva).
8. Con el diseño elegido se escriben los alias de las interacciones que interesan y se asignan los factores reales a las letras, de modo que los que pueden interactuar no queden en la misma cadena.

En el 2^{6−2} de la tabla, el primer candidato (E = ABC, F = BCD) da tres palabras de cuatro letras: resolución IV. El segundo usa F = ABCD; como ABCE y ABCDF comparten las letras A, B y C, su producto es DEF, de solo tres letras, y la resolución baja a III. El tercero repite la columna ABCD para E y para F: el producto es EF y los dos factores quedan aliados entre sí (resolución II), por eso cada factor nuevo debe usar una columna distinta. La regla práctica es elegir generadores largos que compartan pocas letras. Con 16 corridas no existe un 2^{6−2} de resolución V: haría falta asignar a E y a F columnas de cuatro letras distintas, y en el 2^{4} la única es ABCD. Fuente: Montgomery, sección 8-4.""",
  left=[num("Fijar k y las corridas N que se pueden pagar: **p = k − log₂N** generadores",
            "Decidir la **resolución** necesaria: III solo principales; IV principales libres de dobles; "
            "V dobles libres entre sí",
            "Escribir el **diseño básico**: 2^{k−p} completo en los primeros k − p factores (A, B, C, D)",
            "A cada factor sobrante, una **columna de interacción** distinta del básico: "
            "E = ABC ⇒ generador **I = ABCE**",
            "Multiplicar los generadores entre sí, cancelando letras repetidas (A² = I): "
            "**2^{p} − 1 palabras**",
            "**Resolución** = longitud de la palabra más corta; si no alcanza, volver al paso 4 con otras columnas",
            "Si hay empate en resolución: **aberración mínima** (siguiente diapositiva)",
            "Escribir los alias y **asignar** los factores reales a las letras, sin poner en la misma cadena "
            "los que pueden interactuar", size=14)],
  right=[txt("**Ejemplo**: 6 factores, 16 corridas ⇒ p = 2, básico 2^{4} en A, B, C, D", size=15),
         tab(["Generadores", "Palabras", "R"],
             [["E = ABC,  F = BCD", "ABCE, BCDF, ADEF", "IV"],
              ["E = ABC,  F = ABCD", "ABCE, ABCDF, **DEF**", "III"],
              ["E = ABCD,  F = ABCD", "ABCDE, ABCDF, **EF**", "II"]],
             size=14, hl=[0], colw=[0.36, 0.5, 0.14]),
         note("Generadores **largos** que compartan **pocas letras**: ABCE y ABCDF comparten ABC y su producto es DEF", size=14),
         note("Con 16 corridas no hay 2^{6−2}_{V}: solo existe una columna de 4 letras, ABCD", size=14)],
  ratio=0.5)

S("¿Cómo se desempata entre diseños de igual resolución?",
  """Primer criterio: máxima resolución. Segundo criterio, para desempatar entre diseños de igual resolución: aberración mínima, es decir, el menor número de palabras de longitud mínima.

Los pasos para comparar candidatos son: (1) escribir la relación de definición completa de cada uno; (2) anotar la longitud de cada palabra; (3) descartar los de menor resolución; (4) entre los que quedan, contar cuántas palabras tienen la longitud mínima y quedarse con el que tiene menos; (5) comprobarlo contando las cadenas de interacciones dobles aliadas entre sí, que es lo que realmente se pierde.

La tabla compara tres diseños 2^{7−2} de resolución IV. El diseño C tiene una sola palabra de cuatro letras, frente a tres y dos de los diseños A y B; por eso deja menos interacciones dobles confundidas entre sí y es el preferido. En la práctica no hay que buscar los generadores: las tablas de diseños recomendados ya entregan el diseño de máxima resolución y aberración mínima, y el software estadístico trae generadores predeterminados.""",
  body=[tab(["", "Diseño A", "Diseño B", "Diseño C"],
            [["Generadores", "F = ABC,  G = BCD", "F = ABC,  G = ADE", "F = ABCD,  G = ABDE"],
             ["Relación de definición", "I = ABCF = BCDG = ADFG", "I = ABCF = ADEG = BCDEFG",
              "I = ABCDF = ABDEG = CEFG"],
             ["Longitud de las palabras", "4, 4, 4", "4, 4, 6", "4, 5, 5"],
             ["Cadenas de interacciones dobles aliadas", "7", "6", "3"]], size=16,
            colw=[0.25, 0.25, 0.25, 0.25]),
        num("Escribir la **relación de definición** de cada candidato y la longitud de cada palabra",
            "Descartar los de menor **resolución**",
            "Entre los que quedan, contar las palabras de **longitud mínima**: gana el que tiene **menos**",
            "Comprobar: menos **cadenas de interacciones dobles** aliadas entre sí", size=15),
        note("Los tres son IV; el diseño C tiene una sola palabra de 4 letras: es el de **aberración mínima**", size=15)])

E("didáctico", "generadores para un pan", "ejemplo construido para la clase",
  ["Una panadería quiere aumentar el **volumen** de su pan (mL). Se estudian cinco factores a dos niveles: "
   "A levadura (1 o 2 %), B temperatura del horno (180 o 200 °C), C tiempo de horneado (25 o 30 min), "
   "D azúcar (3 o 6 %) y E humedad de la masa (60 o 65 %).",
   "Cada corrida ocupa el horno una tarde. El presupuesto es de **8 corridas**; con esfuerzo se podrían pagar 16. "
   "El panadero está seguro de que hay una **interacción temperatura × tiempo** y quiere que ningún efecto "
   "principal quede mezclado con ella; las interacciones de tres o más factores se consideran despreciables."],
  "Escoger los generadores con el procedimiento de ocho pasos.",
  ["Calcular p con 8 corridas y la resolución que hace falta",
   "Probar generadores y decir si alguno alcanza esa resolución",
   "Decidir qué hacer si no alcanza: pagar más corridas o asignar bien los factores",
   "Escribir los alias del diseño elegido"])

S("Ejemplo didáctico · Pasos 1 a 6: ¿alcanzan 8 corridas?",
  """Paso 1: k = 5 factores y N = 8 corridas, así que p = 5 − log₂8 = 5 − 3 = 2 generadores: es un 2^{5−2}, fracción un cuarto.

Paso 2: el panadero quiere los efectos principales libres de la interacción temperatura × tiempo. Si no se sabe de antemano qué letras tocarán a esos dos factores, la forma segura es pedir resolución IV, en la que ningún efecto principal se mezcla con ninguna interacción doble.

Paso 3: el diseño básico es el 2^{3} completo en A, B y C, con 8 corridas. Sus columnas de interacción disponibles son cuatro: AB, AC, BC y ABC.

Pasos 4 y 5: a D y a E se les asignan dos de esas columnas, distintas, y se multiplican los generadores. Con D = AB y E = AC los generadores son I = ABD e I = ACE, y su producto es BCDE. Con D = ABC y E = AB salen ABCD, ABE y CDE. Con D = ABC y E = BC salen ABCD, BCE y ADE.

Paso 6: la palabra más corta tiene tres letras en los tres candidatos: resolución III. No es mala suerte: hay 12 maneras de asignar dos columnas a D y E y todas dan resolución III con dos palabras de tres letras. La razón es que solo hay una columna de tres letras (ABC); el otro factor recibe una columna de dos letras y su generador tiene tres. Conclusión: con 8 corridas la resolución IV es imposible para cinco factores.""",
  left=[num("k = 5, N = 8  ⇒  **p = 2**: un 2^{5−2}",
            "Efectos principales libres de interacciones dobles  ⇒  hace falta **resolución IV**",
            "Diseño básico: **2^{3}** en A, B, C. Columnas disponibles: **AB, AC, BC, ABC**",
            "Asignar a D y E dos columnas distintas y multiplicar los generadores",
            "Leer la palabra más corta: **3 letras** en todos  ⇒  **resolución III**", size=15)],
  right=[tab(["Generadores", "Palabras", "R"],
             [["D = AB,  E = AC", "ABD, ACE, BCDE", "III"],
              ["D = ABC,  E = AB", "ABCD, ABE, CDE", "III"],
              ["D = ABC,  E = BC", "ABCD, BCE, ADE", "III"]],
             size=14, colw=[0.36, 0.5, 0.14]),
         note("Las **12** asignaciones posibles dan **resolución III**: solo hay una columna de 3 letras, ABC", size=15),
         note("Paso 6: **no alcanza**. Con 8 corridas la resolución IV es imposible para 5 factores", size=15)],
  ratio=0.5)

S("Ejemplo didáctico · Decisión y pasos 7 y 8",
  """Como la resolución IV no se alcanza con 8 corridas, hay dos caminos.

Opción 1, pagar 16 corridas. Ahora p = 5 − 4 = 1. El diseño básico es el 2^{4} en A, B, C y D, y E se asigna a la columna más larga, E = ABCD, con generador I = ABCDE. La única palabra tiene cinco letras: resolución V, más de lo pedido. Cada efecto principal queda aliado con una interacción de cuatro factores y cada interacción doble con una de tres, así que la interacción temperatura × tiempo se estima limpia. El paso 7 no hace falta porque hay un solo candidato de resolución V.

Opción 2, quedarse en 8 corridas y aprovechar el paso 8. Con D = AB y E = AC (I = ABD = ACE = BCDE), las cadenas de alias, despreciando las interacciones de tres o más factores, son: A = BD = CE, B = AD, C = AE, D = AB, E = AC, BC = DE y BE = CD. Las interacciones BC, DE, BE y CD son las únicas que no están aliadas con ningún efecto principal. Por eso conviene dar a la temperatura y al tiempo las letras B y C: su interacción BC queda en la cadena BC = DE, junto a otra interacción doble pero lejos de los efectos principales. La asignación queda A levadura, B temperatura, C tiempo, D azúcar y E humedad, que es la del enunciado.

El costo de la opción 2: la levadura (A) queda aliada con las interacciones temperatura × azúcar (BD) y tiempo × humedad (CE), y cada uno de los otros efectos principales queda aliado con una interacción doble. Si el panadero cree que esas interacciones no existen, las 8 corridas bastan; si duda, la opción 1 es la segura. Es exactamente la lógica del procedimiento: el paso 6 dice que el diseño pequeño no da la resolución pedida y el paso 8 permite proteger la única interacción que se teme.""",
  left=[txt("**Opción 1 · pagar 16 corridas**", size=16),
        bul("p = 1, básico 2^{4} en A, B, C, D", "**E = ABCD**  ⇒  I = ABCDE: **resolución V**",
            "Temperatura × tiempo se estima **limpia**", size=15),
        txt("**Opción 2 · quedarse en 8 corridas**", size=16),
        bul("D = AB, E = AC: I = ABD = ACE = BCDE",
            "Paso 8: temperatura y tiempo en **B y C**, porque BC no está aliada con ningún efecto principal", size=15)],
  right=[tab(["Cadena de alias (2^{5−2}, D = AB, E = AC)", "¿Mezcla un efecto principal?"],
             [["A = BD = CE", "Sí"], ["B = AD", "Sí"], ["C = AE", "Sí"], ["D = AB", "Sí"], ["E = AC", "Sí"],
              ["**BC = DE**  (temperatura × tiempo)", "**No**"], ["BE = CD", "No"]],
             size=14, hl=[5], colw=[0.62, 0.38]),
         note("Opción 2: la interacción temida queda **lejos de los efectos principales**, pero cada principal sigue aliado con una doble", size=14)],
  ratio=0.48)

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

S("¿Cómo elijo un diseño para siete factores? (pasos 1 y 2)",
  """Ejemplo 8-5 de Montgomery, resuelto con el procedimiento de ocho pasos. Se tienen siete factores, interesa estimar los siete efectos principales y tener una idea de las interacciones dobles, y se está dispuesto a suponer despreciables las interacciones de tres o más factores.

Paso 2 primero, porque es el que fija la exigencia: los efectos principales no deben mezclarse con interacciones dobles, así que se pide resolución IV. No se pide V porque basta con una idea de las interacciones dobles; no hace falta estimarlas por separado.

Paso 1: se recorren los tamaños posibles, de menor a mayor, y se busca el más pequeño que alcance la resolución IV. Con N = 8 corridas, p = 7 − 3 = 4: el diseño básico es el 2^{3} en A, B y C, que solo tiene cuatro columnas de interacción (AB, AC, BC y ABC). Los cuatro factores nuevos las ocupan todas, tres de ellos reciben columnas de dos letras y sus generadores tienen tres letras: el diseño es forzosamente de resolución III (es el diseño saturado 2^{7−4}_{III}). Con N = 16, p = 3: existe el 2^{7−3}_{IV}. Con N = 32, p = 2: el 2^{7−2}_{IV}. Con N = 64, p = 1: el 2^{7−1}_{VII}, con I = ABCDEFG.

Entre los que cumplen se elige el más pequeño. El de 16 corridas deja los siete efectos principales aliados solo con interacciones triples y las interacciones dobles en grupos de tres: cumple el objetivo. El de 32 corridas estimaría además de forma única 15 de las 21 interacciones dobles, más información de la que se pidió, al doble de costo. Se elige el 2^{7−3}_{IV} de 16 corridas.""",
  left=[txt("**Objetivo**: 7 efectos principales y una idea de las interacciones dobles; triples despreciables", size=15),
        num("**Paso 2**: principales libres de dobles  ⇒  **resolución IV**",
            "**Paso 1**: probar N = 8, 16, 32, … y quedarse con el **menor** que da IV", size=15),
        note("Con 8 corridas el básico 2^{3} solo tiene 4 columnas (AB, AC, BC, ABC) para 4 factores nuevos: "
             "tres generadores de 3 letras  ⇒  **III** forzosamente", size=14)],
  right=[tab(["Corridas N", "p", "Mejor diseño", "¿Cumple IV?"],
             [["8", "4", "2^{7−4}_{III}", "No"],
              ["**16**", "**3**", "**2^{7−3}_{IV}**", "**Sí**: dobles en grupos de 3"],
              ["32", "2", "2^{7−2}_{IV}", "Sí: 15 de 21 dobles limpias"],
              ["64", "1", "2^{7−1}_{VII}", "Sí, de sobra"]],
             size=15, hl=[1], colw=[0.2, 0.1, 0.28, 0.42], first_left=False),
         note("Se elige el diseño **más pequeño** que cumple el objetivo: el **2^{7−3}_{IV}** de 16 corridas", size=15)],
  ratio=0.47)

S("¿Cómo elijo un diseño para siete factores? (pasos 3 a 8)",
  """Paso 3: el diseño básico es el 2^{4} completo en A, B, C y D, con 16 corridas.

Paso 4: hay que darle a E, F y G tres columnas de interacción distintas. El 2^{4} tiene once: seis de dos letras (AB, AC, AD, BC, BD, CD), cuatro de tres letras (ABC, ABD, ACD, BCD) y una de cuatro (ABCD). Hay 165 maneras de escoger tres; solo 4 dan resolución IV, y son las que usan tres de las cuatro columnas de tres letras. Una columna de dos letras da un generador de tres letras (resolución III). Usar ABCD también falla: con E = ABC y G = ABCD los generadores ABCE y ABCDG comparten A, B y C, y su producto es DEG, de tres letras. Se toma E = ABC, F = BCD y G = ACD, como en la tabla 8-15.

Paso 5: con tres generadores la relación de definición completa tiene 2^{3} − 1 = 7 palabras: los tres generadores, los tres productos de dos en dos (ABCE·BCDF = ADEF, ABCE·ACDG = BDEG, BCDF·ACDG = ABFG) y el producto de los tres (CEFG).

Paso 6: las siete palabras tienen cuatro letras: resolución IV, la pedida.

Paso 7: las cuatro asignaciones que dan resolución IV tienen el mismo patrón, siete palabras de cuatro letras, así que no hay nada que desempatar.

Paso 8: cada efecto principal queda aliado con cuatro interacciones triples (por ejemplo A = BCE = BFG = CDG = DEF) y las 21 interacciones dobles forman 7 cadenas de tres: AB = CE = FG, AC = BE = DG, AD = CG = EF, AE = BC = DF, AF = BG = DE, AG = BF = CD y BD = CF = EG. Para asignar los factores reales, Montgomery aconseja (molino de bolas) poner en A, B, C y D los factores que se creen importantes y que pueden interactuar, y en E, F y G las variables menores. Si las menores resultan inactivas, el diseño se proyecta en un 2^{4} completo en los factores clave. Fuente: Montgomery, ejemplo 8-5, tabla 8-15 y sección de proyección.""",
  left=[bul("**Paso 3**: básico **2^{4}** en A, B, C, D (16 corridas)",
            "**Paso 4**: E, F, G en **tres de las cuatro columnas de 3 letras**: E = ABC, F = BCD, G = ACD",
            "**Paso 5**: 3 generadores + 3 productos de dos en dos + 1 de los tres = **7 palabras**",
            "**Paso 6**: todas de 4 letras  ⇒  **resolución IV**",
            "**Paso 7**: las 4 opciones válidas tienen el mismo patrón: **sin empate**",
            "**Paso 8**: factores **importantes** en A, B, C, D; **menores** en E, F, G", size=15),
        note("Solo **4 de 165** elecciones dan IV. Con ABCD: ABCE · ABCDG = **DEG**  ⇒  III", size=14)],
  right=[form("I = ABCE = BCDF = ACDG = ADEF", "= BDEG = ABFG = CEFG", size=16),
         tab(["Interacciones dobles aliadas (7 cadenas)"],
             [["AB = CE = FG"], ["AC = BE = DG"], ["AD = CG = EF"], ["AE = BC = DF"],
              ["AF = BG = DE"], ["AG = BF = CD"], ["BD = CF = EG"]],
             size=13, first_left=False, pad=0.06),
         note("Principales: cada uno con **4 triples**, p. ej. A = BCE = BFG = CDG = DEF", size=14)],
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
             "Se prueba la **cadena completa**: A + BCD, no A sola (siguientes diapositivas)",
             "Si BCD es **despreciable**, equivale a  H_{0}: β_{A} = 0",
             "Nivel de significancia habitual: **α = 0.05**"),
         note("H_{0}: el factor no afecta la respuesta.  H_{A}: el factor sí la afecta.")])

_bcd = [[t, sg(r["A"]), sg(r["B"] * r["C"] * r["D"]), str(v)] for r, t, v in zip(r1, trat1, y1)]
_sp = sum(v for r, v in zip(r1, y1) if r["A"] > 0)
_sm = sum(v for r, v in zip(r1, y1) if r["A"] < 0)
S("¿Por qué se prueba la cadena completa?",
  f"""Con el ejemplo 1 (índice de filtración, 2^{{4−1}} con I = ABCD). La relación de definición dice que A = BCD: en las ocho corridas de la fracción, la columna de signos de A y la columna de la interacción BCD (producto de las columnas B, C y D) son idénticas, como muestra la tabla. No es una aproximación: son la misma columna.

El efecto se estima con el contraste de esa columna: ℓ_{{A}} = (suma de las respuestas con signo + menos suma de las respuestas con signo −) / 4 = ({_sp} − {_sm}) / 4 = {f(ef1["A"][1])}. Como la columna es la misma, el número {f(ef1["A"][1])} es a la vez el contraste de A y el de BCD. Lo que mide es la suma de los dos efectos: ℓ_{{A}} estima A + BCD (en coeficientes, β̂_{{A}} estima β_{{A}} + β_{{BCD}}).

Por eso varios «mundos» distintos producen exactamente los mismos datos: que A valga {f(ef1["A"][1])} y BCD cero; que A sea cero y BCD valga {f(ef1["A"][1])}; o que se repartan, por ejemplo 10 y 9. Los datos no pueden distinguirlos. Incluso puede pasar lo contrario: si A valiera 19 y BCD −19, la columna daría cero y A parecería inactivo aunque no lo es (cancelación; es rara, pero posible).

Conclusión: la prueba F de la columna de A no puede referirse a A sola, porque los datos no contienen información sobre A sola. La única hipótesis que los datos pueden juzgar es la de la cadena: H_{{0}}: β_{{A}} + β_{{BCD}} = 0 frente a H_{{A}}: β_{{A}} + β_{{BCD}} ≠ 0.""",
  left=[tab(["Corrida", "A", "BCD = B·C·D", "y"], _bcd, size=14, first_left=False, pad=0.07),
        note("Columnas **idénticas**: el contraste de A es también el de BCD", size=14)],
  right=[form(f"ℓ_{{A}} = ({_sp} − {_sm}) / 4 = {f(ef1['A'][1])}  →  estima A + BCD", size=17),
         tab(["Mundo posible", "A", "BCD", "ℓ_{A} observado"],
             [["Solo A", f(ef1["A"][1]), "0", f(ef1["A"][1])],
              ["Solo BCD", "0", f(ef1["A"][1]), f(ef1["A"][1])],
              ["Se reparten", "10.00", "9.00", f(ef1["A"][1])],
              ["Se cancelan", f(ef1["A"][1]), f(-ef1["A"][1]), "**0.00**"]],
             size=14, hl=[3], first_left=True, colw=[0.34, 0.18, 0.18, 0.3]),
         txt(f"Varios «mundos» distintos producen exactamente los mismos datos: que A valga {f(ef1['A'][1])} y BCD "
             f"cero; que A sea cero y BCD valga {f(ef1['A'][1])}; o que se repartan, por ejemplo 10 y 9. Los datos no "
             "pueden distinguirlos. Incluso puede pasar lo contrario: si A valiera 19 y BCD −19, la columna daría cero "
             "y A parecería inactivo aunque no lo es (cancelación; es rara, pero posible).", size=13),
         note("Los datos solo ven la **suma**: H_{0}: β_{A} + β_{BCD} = 0", size=15)],
  ratio=0.42)

_dec = {t: (F, p) for t, _, _, _, F, p in m1["anova"]}
_atr = [["A + BCD", "A", "Jerarquía: la triple BCD se supone despreciable"],
        ["C + ABD", "C", "Jerarquía"],
        ["D + ABC", "D", "Jerarquía"],
        ["AC + BD", "AC", "Herencia: A y C activos, B inactivo"],
        ["AD + BC", "AD", "Herencia: A y D activos, B inactivo"]]
_dt = [[c, f(_dec[k][0]), pv(_dec[k][1]), "Sí", a, w] for (c, a, w), k in zip(_atr, ["A", "C", "D", "AC", "AD"])]
S("¿Cómo se lee la decisión de cada cadena y a qué término se atribuye?",
  f"""La prueba se hace en dos momentos que conviene no mezclar.

Primero la decisión estadística, que es sobre la cadena. Si F_{{0}} supera el valor crítico (o el valor p es menor que α), se rechaza H_{{0}} y se concluye que la cadena está activa: al menos uno de sus efectos es distinto de cero. Si no se rechaza, se concluye que la cadena no muestra efecto; lo usual es que todos sus términos sean nulos, aunque no se puede descartar una cancelación.

Después viene la atribución, que no es estadística: decidir a qué término de la cadena se le adjudica el efecto. Se hace con supuestos y conocimiento del proceso, y hay que decirlo en el informe. Hay dos herramientas. La jerarquía (escasez de efectos): las interacciones de orden alto son raras, así que en A + BCD el efecto se atribuye a A. La herencia: una interacción suele ser importante cuando sus factores también lo son. En una cadena de dos interacciones dobles, como AC + BD, la jerarquía no decide (ambas son dobles); como A y C resultaron activos y B no, se atribuye a AC.

En el ejemplo 1 el ANOVA del modelo reducido rechaza H_{{0}} en las cinco cadenas que entraron: A + BCD (F_{{0}} = {f(_dec["A"][0])}, p = {pv(_dec["A"][1])}), C + ABD (F_{{0}} = {f(_dec["C"][0])}), D + ABC (F_{{0}} = {f(_dec["D"][0])}), AC + BD (F_{{0}} = {f(_dec["AC"][0])}) y AD + BC (F_{{0}} = {f(_dec["AD"][0])}), con 1 y {m1["dfe"]} grados de libertad. Las tres primeras se atribuyen a los efectos principales por jerarquía y las dos últimas a AC y AD por herencia.

¿Cómo se sabe entonces qué término de la cadena produce el efecto? Ninguna herramienta estadística del fraccionado ve factores: la gráfica normal de Daniel, el diagrama de Pareto y el ANOVA usan el mismo contraste de cada columna, y en el 2^{{4−1}} con I = ABCD la columna de A es la columna de BCD; el punto de la gráfica normal es el de «A + BCD», no el de A. La pregunta se resuelve en tres capas. Antes de correr, con la resolución: en resolución III un principal queda aliado con dobles y la duda es real; en IV solo con triples, de modo que atribuirle el efecto al principal es un riesgo pequeño y conocido, y las dobles quedan aliadas entre sí; en V los principales quedan con cuádruples y las dobles con triples. Después de correr, con la atribución razonada de arriba (jerarquía, herencia, conocimiento del proceso), que es razonamiento, no prueba, y se declara en el informe. Y para saberlo con datos, más corridas: la fracción alterna o el doblez cambian el signo de los alias, y al combinar las dos fracciones los términos se separan. En el ejemplo 1, con la fracción alterna del ejemplo 8-3: A = ({f(ef1["A"][1])} + {f(ef1b["A"][1])}) / 2 = {f((ef1["A"][1] + ef1b["A"][1]) / 2)} y BCD = {f((ef1["A"][1] - ef1b["A"][1]) / 2)}; AC = {f((ef1["AC"][1] + ef1b["AC"][1]) / 2)} y BD = {f((ef1["AC"][1] - ef1b["AC"][1]) / 2)}; AD = {f((ef1["AD"][1] + ef1b["AD"][1]) / 2)} y BC = {f((ef1["AD"][1] - ef1b["AD"][1]) / 2)}. La jerarquía y la herencia habían acertado. Otras salidas: el doblez de un solo factor separa ese factor y todas sus interacciones dobles, y una corrida de confirmación verifica que la respuesta predicha con el modelo atribuido coincide con la observada. En resumen: la prueba responde si la cadena pesa; qué término pesa lo acota la resolución, lo razonan la jerarquía y la herencia, y lo confirman las corridas adicionales. Por eso las conclusiones de un fraccionado son tentativas hasta confirmarlas.""",
  left=[cards(("1 · Decisión estadística", "Sobre la **cadena**: se rechaza H_{0} ⇒ **la cadena está activa**. "
                                         "Daniel, Pareto y ANOVA ven **cadenas**, no factores"),
              ("2 · Atribución razonada", "Sobre el **término**: **jerarquía** (A + BCD → A), **herencia** "
                                          "(AC + BD → AC: A y C activos, B no), conocimiento del proceso. "
                                          "No es estadística; se declara"),
              ("3 · Para saberlo: más corridas", f"La **fracción alterna** o el **doblez** separan la cadena. Ejemplo 1: "
                                                  f"A = {f((ef1['A'][1] + ef1b['A'][1]) / 2)} y BCD = {f((ef1['A'][1] - ef1b['A'][1]) / 2)}; "
                                                  f"AC = {f((ef1['AC'][1] + ef1b['AC'][1]) / 2)} y BD = {f((ef1['AC'][1] - ef1b['AC'][1]) / 2)}"),
              size=13, cols=1)],
  right=[tab(["Cadena", "F_{0}", "Valor p", "¿Rechaza H_{0}?", "Se atribuye a", "Por qué"], _dt,
             size=12, first_left=True, colw=[0.15, 0.12, 0.12, 0.13, 0.13, 0.35]),
         txt(f"Ejemplo 1 (2^{{4−1}}, I = ABCD), modelo reducido, gl del error = {m1['dfe']}", size=12),
         note("Rechazar H_{0} en AC + BD dice que **la cadena** pesa; que sea **AC** lo dice la herencia y lo "
              "**confirman** las corridas adicionales", size=14)],
  ratio=0.42)

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
  body=[bul("**Gráfica normal o seminormal de efectos**: los inactivos caen sobre una recta",
            "**Pareto con método de Lenth**: activo si |efecto| > margen de error; complementa la gráfica normal, no la sustituye",
            "Los efectos descartados pasan a formar el **error** del ANOVA"),
        form("s_{0} = 1.5 · mediana |ℓ_{i}|", "PSE = 1.5 · mediana { |ℓ_{i}| : |ℓ_{i}| < 2.5 s_{0} }",
             "ME = t_{0.025, m/3} · PSE", size=17),
        note("Lenth solo es razonable con **pocos efectos activos**: en el ejemplo 1, con cinco de siete efectos grandes, "
             "no detecta ninguno (PSE = 24.75). Las cadenas activas se atribuyen con escasez, jerarquía y herencia", size=15)])

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

S("¿Cómo aprovecho la proyección al asignar los factores a las columnas?",
  """Un diseño de resolución R contiene un factorial completo en cualquier subconjunto de R − 1 factores, y en general un 2^{k−p} se proyecta en un factorial completo en cualquier subconjunto de factores que no contenga una palabra de la relación de definición; si la contiene, queda un fraccionado con réplicas. Si al analizar solo unos pocos factores resultan activos, el diseño se convierte, sin correr nada más, en un factorial completo (posiblemente con réplicas) en ellos. La proyección permite entonces asignar los factores con estrategia. En el 2^{7−3}_{IV} de 16 corridas hay 35 subconjuntos de cuatro factores; siete son palabras de la relación de definición y los otros 28 forman un 2^{4} completo. Uno de ellos, el más obvio, es el de las columnas del diseño básico: A, B, C y D.

Montgomery lo ilustra con un molino de bolas con siete factores. Se tiene bastante certeza de que la velocidad del motor, el modo de alimentación, el tamaño de la alimentación y el tipo de material afectan la eficiencia y pueden interactuar; se sabe menos de la muesca, el ángulo de la criba y el nivel de vibración, que probablemente son insignificantes. La estrategia es asignar los cuatro primeros a las columnas A, B, C y D y las «variables menores» a E, F y G. Si se está en lo correcto y estas resultan despreciables, queda un 2^{4} completo en las variables clave.

Las conclusiones obtenidas así deben considerarse tentativas: suele haber explicaciones alternativas basadas en interacciones de orden superior.""",
  left=[tab(["Columna", "Factor del molino de bolas"],
            [["A", "Velocidad del motor"], ["B", "Modo de alimentación"], ["C", "Tamaño de la alimentación"],
             ["D", "Tipo de material"], ["E = ABC", "Muesca"], ["F = BCD", "Ángulo de la criba"],
             ["G = ACD", "Nivel de vibración de la criba"]], size=15, colw=[0.3, 0.7], hl=[0, 1, 2, 3])],
  right=[bul("Resolución **R** ⇒ factorial completo en cualquier subconjunto de **R − 1** factores; en general, en todo "
             "subconjunto que **no contenga una palabra**",
             "Factores **importantes** y que pueden interactuar: columnas del **diseño básico**",
             "Factores **menores**: columnas generadas",
             "Si los menores no influyen, queda un **2^{4} completo** en los importantes",
             "De 35 subconjuntos de 4 factores, **28** dan un 2^{4} completo", size=16),
         note("Las conclusiones son **tentativas**: puede haber explicaciones con interacciones de orden alto", size=15)],
  ratio=0.48)

def _nom(r):
    return "".join(k.lower() for k in "ABCDEF" if r[k] > 0) or "(1)"


_t1 = [[str(i + 1), _nom(r), sg(r["D"])] for i, r in enumerate(r3[:8])]
_t2 = [[str(i + 9), _nom(r), sg(r["D"])] for i, r in enumerate(r3[8:])]
_tt = [a_ + b_ for a_, b_ in zip(_t1, _t2)]
S("¿Qué es un bloque? Un caso concreto",
  """Se toma el ejemplo 3, el moldeo por inyección: un 2^{6−2}_{IV} de 16 corridas con I = ABCE = BCDF = ADEF. Supóngase que la inyectora solo permite hacer 8 corridas por turno, así que el experimento se corre en dos partes: 8 corridas en la mañana y 8 en la tarde. Por la tarde la máquina está más caliente y las piezas se contraen un poco más, digamos 5 unidades más en todas las corridas de la tarde, sin importar los factores.

Cada uno de esos grupos de corridas hechas en las mismas condiciones (el mismo turno) es un bloque. El turno no es un factor que interese estudiar: es una fuente de variación molesta que no se puede eliminar. Formar bloques significa decidir de antemano qué corridas van en cada parte, de modo que esa diferencia no estropee los efectos que sí interesan. Es exactamente lo que se pregunta: tomar una fracción, aquí un 2^{6−2}, y correrla por secciones.

La pregunta concreta es qué 8 corridas se hacen en la mañana. La forma ingenua es hacer las 8 primeras del orden estándar en la mañana y las 8 últimas en la tarde. La tabla muestra el problema: en el orden estándar del diseño básico, D es la columna que cambia más despacio, así que las corridas 1 a 8 tienen todas D en nivel bajo y las corridas 9 a 16 tienen todas D en nivel alto. El turno y el factor D quedan perfectamente mezclados: cualquier diferencia entre mañana y tarde se va a leer como efecto de D.""",
  left=[txt("**Ejemplo 3, moldeo**: 2^{6−2}_{IV}, 16 corridas. La inyectora solo permite **8 corridas por turno**: "
            "mañana y tarde. En la tarde la máquina está más caliente: **+5** de contracción en todas sus corridas", size=15),
        cards(("Bloque", "Cada grupo de corridas hechas en las **mismas condiciones** (aquí, el mismo turno). El turno "
                         "no se estudia: es variación **molesta** que no se puede quitar"),
              ("La decisión", "¿Qué 8 corridas van en la mañana y cuáles en la tarde?"), size=14, cols=1)],
  right=[txt("**Reparto ingenuo**: las 8 primeras del orden estándar en la mañana", size=15),
         tab(["Corrida", "Mañana", "D", "Corrida", "Tarde", "D"], _tt, size=13, first_left=False, pad=0.05),
         note("Toda la mañana tiene **D −** y toda la tarde **D +**: el turno queda **mezclado con D**", size=14)],
  ratio=0.44)

def _efm(y, t):
    sgn = [1] * len(r3)
    for k in t:
        sgn = [a_ * r[k] for a_, r in zip(sgn, r3)]
    return sum(v for v, x in zip(y, sgn) if x > 0) / 8 - sum(v for v, x in zip(y, sgn) if x < 0) / 8


_yn = [v + 5 * (i >= 8) for i, v in enumerate(y3)]
_yb = [v + 5 * (r["A"] * r["B"] * r["D"] > 0) for v, r in zip(y3, r3)]
_ce = [[t if t != "ABD" else "ABD (+ ACF + BEF + CDE)", f(_efm(y3, t)), f(_efm(_yn, t)), f(_efm(_yb, t))]
       for t in ("A", "B", "D", "AB", "AD", "ABD")]
S("¿Qué pasa con los efectos según cómo se reparta?",
  f"""Para ver el daño se toman los datos reales del ejemplo 3 y se les suma 5 a las corridas de la tarde, como si el turno tuviera ese efecto. Después se recalculan los efectos con dos repartos distintos.

Con el reparto ingenuo (las 8 primeras corridas en la mañana) la tarde coincide con D alto, y el efecto de D pasa de {f(_efm(y3, "D"))} a {f(_efm(_yn, "D"))}. D era inactivo y ahora parecería activo: se concluiría que D importa cuando lo que importa es el turno. Los demás efectos no cambian, porque sus columnas tienen cuatro signos + y cuatro − en cada turno.

Con el reparto por el signo de ABD (las corridas con ABD negativo en la mañana y las de ABD positivo en la tarde) el único efecto que cambia es el de la cadena ABD = ACF = BEF = CDE, que pasa de {f(_efm(y3, "ABD"))} a {f(_efm(_yb, "ABD"))}. Todos los efectos principales y todas las interacciones dobles quedan exactamente igual que sin turnos.

Esa es toda la idea de los bloques. La diferencia entre bloques siempre se va a pegar a alguna columna: a la columna con la que se hizo el reparto. Lo que se decide al formar bloques es cuál columna se sacrifica. Se elige una cadena formada solo por interacciones de orden alto, que de todos modos se suponían despreciables. La diapositiva siguiente da el procedimiento general.""",
  left=[tab(["Efecto", "Sin turnos", "Reparto ingenuo (por D)", "Reparto por ABD"], _ce,
            size=14, hl=[2, 5], colw=[0.34, 0.18, 0.26, 0.22]),
        txt("Datos del ejemplo 3; a la tarde se le suman 5 unidades", size=12)],
  right=[bul("**Ingenuo**: D pasa de " + f(_efm(y3, "D")) + " a **" + f(_efm(_yn, "D")) + "**: parece activo y no lo es",
             "**Por ABD**: solo cambia la cadena ABD, de " + f(_efm(y3, "ABD")) + " a **" + f(_efm(_yb, "ABD")) + "**",
             "Principales y dobles: **iguales** que sin turnos", size=15),
         note("La diferencia entre bloques **siempre** cae en una columna: se escoge **cuál se sacrifica**, "
              "una de orden alto", size=15)],
  ratio=0.55)

_b1 = [r for r in r3 if r["A"] * r["B"] * r["D"] < 0]
_b2 = [r for r in r3 if r["A"] * r["B"] * r["D"] > 0]
_com = lambda r: str(sum(1 for k in "ABD" if r[k] > 0))
_bl = [[_nom(a), _com(a), _nom(b), _com(b)] for a, b in zip(_b1, _b2)]
S("¿Cómo se separa un fraccionado en bloques?",
  """Un bloque es un grupo de corridas hechas en condiciones parecidas: el mismo día, el mismo lote de material, la misma máquina. Se forman bloques cuando no se pueden hacer todas las corridas en condiciones homogéneas, y se hace igual que en un 2^{k}: se escoge una columna del diseño y se usa su signo para repartir las corridas. Todas las corridas con signo − van a un bloque y todas las de signo + al otro. Esa columna queda confundida con los bloques: su contraste mide a la vez su efecto y la diferencia entre bloques.

El procedimiento tiene cinco pasos. (1) Decidir cuántos bloques hacen falta: dos bloques confunden una columna; cuatro bloques confunden dos columnas y su producto (tres en total). (2) Escribir las cadenas de alias del fraccionado. (3) Escoger para los bloques una cadena formada solo por interacciones de orden alto, porque se va a perder. Nunca una que contenga efectos principales o interacciones dobles de interés. En el 2^{6−2} con I = ABCE = BCDF = ADEF hay quince cadenas; solo dos están formadas únicamente por interacciones triples: ABD = ACF = BEF = CDE y ABF = ACD = BDE = CEF. La tabla XII de Montgomery sugiere ABD. (4) Calcular el signo de ABD en cada corrida, que es el producto de los signos de A, B y D. (5) Repartir: las ocho corridas con ABD = − forman el bloque 1 y las ocho con ABD = + el bloque 2.

Atajo para el paso 4 sin calcular signos: contar cuántas letras tiene en común cada combinación de tratamientos con ABD. Si el número es par (0 o 2), ABD vale − y la corrida va al bloque 1, que es el bloque principal porque contiene a (1). Si es impar (1 o 3), ABD vale + y va al bloque 2. Ejemplos: abf tiene en común a y b, dos letras, par: bloque 1 (A +, B +, D −, producto −). ae tiene en común solo a, una letra, impar: bloque 2 (A +, B −, D −, producto +). En la notación de Montgomery es la regla L = x_{1} + x_{2} + x_{4} = 0 (mod 2) para el bloque principal, donde x vale 1 si la letra está y 0 si no. Fuente: Montgomery, sección 8-4 y fig. 8-18; la figura imprime «abef» en el bloque 1 y debe ser adef, la que pertenece a la fracción.

Qué se pierde y qué se conserva. Supóngase que la tarde da respuestas sistemáticamente más altas que la mañana. La columna de ABD vale − en toda la mañana y + en toda la tarde, así que su contraste es exactamente la diferencia entre turnos: el efecto estimado de la cadena ABD = ACF = BEF = CDE ya no se puede separar del efecto de los bloques. Por eso se escogió una cadena de triples: se pierde algo que de todos modos se suponía despreciable. En el ANOVA esa columna aparece como la fila de bloques, con 1 grado de libertad y la misma suma de cuadrados. Todas las demás columnas están balanceadas dentro de cada bloque, con cuatro signos + y cuatro signos − en cada turno: al calcular el contraste de A, el corrimiento de la tarde aparece cuatro veces sumando y cuatro veces restando, y se cancela. Lo mismo pasa con las otras trece cadenas, que incluyen todos los efectos principales y todas las interacciones dobles. Es la ortogonalidad de la tabla de signos: la columna de bloques (ABD) es ortogonal a todas las demás.""",
  left=[tab(["Mañana · ABD −", "Letras en común", "Tarde · ABD +", "Letras en común"], _bl,
            size=13, first_left=False, colw=[0.29, 0.21, 0.29, 0.21], pad=0.06),
        txt("Montgomery, fig. 8-18 (la figura imprime «abef»; debe ser adef)", size=11)],
  right=[num("Decidir cuántos bloques: **2** bloques confunden **1** columna; **4** confunden **2** y su producto",
             "Escribir las **cadenas de alias** del fraccionado",
             "Escoger una cadena con **solo interacciones de orden alto**: aquí ABD = ACF = BEF = CDE",
             "Calcular el **signo de ABD** en cada corrida: signo de A × signo de B × signo de D",
             "Repartir: **ABD = −** a la mañana (bloque 1), **ABD = +** a la tarde (bloque 2); ABD queda "
             "**confundida** con el turno", size=13),
         note("**Atajo**: letras en común con ABD. **Par** (0 o 2) → mañana; **impar** (1 o 3) → tarde. "
              "abf: a, b = 2 → mañana.  ae: a = 1 → tarde", size=13),
         note("**Se pierde** la cadena ABD = ACF = BEF = CDE: su contraste es la diferencia entre turnos (fila de "
              "**bloques** del ANOVA, 1 g.l.). **Se conserva** el resto: las otras 13 cadenas tienen 4 + y 4 − en "
              "cada turno y la diferencia se cancela en sus contrastes", size=13)], ratio=0.44)

E(4, "máquina CNC", "Montgomery, ejemplo 8-6",
  ["Una máquina CNC de cinco ejes produce el impulsor de un motor de turbina. Una característica de calidad clave es el **perfil de los álabes**: interesa su desviación respecto al perfil especificado en el plano, medida como la desviación estándar de la diferencia entre ambos.",
   "Se quiere saber **qué parámetros de la máquina** afectan esa desviación. Se eligen ocho factores a dos niveles: desviaciones de los ejes x, y, z y a, fabricante de la herramienta, velocidad del husillo, altura de la plantilla sujetadora y velocidad de alimentación.",
   "La máquina tiene **cuatro husillos** (la traducción del libro los llama areómetros) que pueden diferir entre sí; deben tratarse como **bloques**. Los ingenieros creen que las interacciones de tres o más factores son despreciables, pero no quieren ignorar las de dos."],
  "Identificar los parámetros de la máquina que **más afectan la desviación del perfil**, controlando la diferencia entre husillos",
  ["Elegir entre 16 y 32 corridas y justificarlo", "Repartir el diseño en cuatro bloques y ver qué se confunde",
   "Estimar los efectos y ajustar el modelo", "Interpretar los alias que queden ambiguos"])

# Ejemplo 4 (Montgomery, ej. 8-6): efectos de la tabla 8-17 sobre ln(desv. estándar × 10^3).
# Los 32 datos crudos (tabla 8-16) no están transcritos; el análisis se rehace desde los efectos.
ef8 = {"A": (0.29026, 0.674020), "B": (-0.20054, 0.321729), "C": (-0.02576, 0.005310), "D": (0.10813, 0.093540),
       "E": (-0.0005063, 0.00000205), "F": (-0.03871, 0.011988), "G": (0.11608, 0.107799), "H": (0.01417, 0.001606),
       "AB + CF + DG": (-0.00588, 0.0002767), "AC + BF": (-0.06206, 0.030815), "AD + BG": (-0.37412, 1.119705),
       "AE": (0.00804, 0.000517), "AF + BC": (-0.04502, 0.016214), "AG + BD": (0.05288, 0.022370),
       "AH": (-0.05042, 0.020339), "BE": (0.09851, 0.077627), "BH": (0.01309, 0.001371), "CD + FG": (0.03452, 0.009535),
       "CE": (0.03982, 0.012685), "CG + DF": (-0.01467, 0.001721), "CH": (0.06080, 0.029568), "DE": (0.01708, 0.002334),
       "DH": (0.01569, 0.001969), "EF": (-0.01808, 0.002616), "EG": (-0.05371, 0.023078), "EH": (-0.03534, 0.009993),
       "FH": (-0.02808, 0.006308), "GH": (0.00489, 0.0001914), "ABE": (0.03331, 0.008874), "ABH": (-0.01261, 0.001273),
       "ACD": (-0.05433, 0.023617)}
_blq8 = ("ABE", "ABH", "EH")
_w8 = [w for w in ef8 if w not in _blq8]
_v8 = [ef8[w][0] for w in _w8]
_z8 = normal_scores(_v8)
_s8 = sorted(range(len(_w8)), key=lambda i: _v8[i])
_p8 = [(_v8[i], _z8[i]) for i in _s8]
_act8 = {k for k, i in enumerate(_s8) if _w8[i] in ("A", "B", "AD + BG")}
_lab8 = {k: _w8[i] for k, i in enumerate(_s8) if _w8[i] in ("A", "B", "AD + BG", "G")}
pse8 = lenth(_v8); me8 = t_ppf(0.05, len(_v8) / 3) * pse8
sme8 = t_ppf(1 - 0.95 ** (1 / len(_v8)), len(_v8) / 3) * pse8
ssb8 = sum(ef8[w][1] for w in _blq8)
_cubo8 = {(0, 0, 1): 0.9595, (15, 0, 1): 1.745, (0, 15, 1): 0.8280, (15, 15, 1): 1.370,
          (0, 0, 2): 1.504, (15, 0, 2): 1.310, (0, 15, 2): 1.247, (15, 15, 2): 1.273}
_ad8 = {(a, d): (_cubo8[(a, 0, d)] + _cubo8[(a, 15, d)]) / 2 for a in (0, 15) for d in (1, 2)}

r8 = basic(5); add_factor(r8, "F", "ABC"); add_factor(r8, "G", "ABD"); add_factor(r8, "H", "BCDE")


def _nom8(r):
    return "".join(k.lower() for k in "ABCDEFGH" if r[k] > 0) or "(1)"


def _sg8(r, t):
    v = 1
    for k in t:
        v *= r[k]
    return v


_hus = {}
for _r in r8:
    _hus.setdefault((_sg8(_r, "ABE"), _sg8(_r, "ABH")), []).append(_nom8(_r))
_orden_h = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
_tab_h = [[f"Husillo {i + 1}", sg(k[0]), sg(k[1]), sg(k[0] * k[1]), ", ".join(_hus[k])] for i, k in enumerate(_orden_h)]

S("Ejemplo 4 · Pasos 1 y 2: respuesta, factores y resolución",
  """Paso 1, planteamiento. La respuesta es la desviación del perfil de los álabes respecto al plano, medida como la desviación estándar de la diferencia entre el perfil real y el especificado (en milésimas de pulgada). Como es una desviación estándar, se analiza su logaritmo, ln(desviación estándar × 10^{3}): las desviaciones estándar suelen tener varianza que crece con su media, y el logaritmo la estabiliza. Hay ocho factores a dos niveles, los de la tabla.

Paso 2, supuestos y resolución. Los ingenieros creen que las interacciones de tres o más factores son despreciables, pero no quieren ignorar las de dos. De ahí sale la resolución mínima. Resolución III no sirve: mezclaría efectos principales con interacciones dobles, que no se quieren ignorar. Resolución IV basta: los efectos principales quedan aliados solo con triples, que se suponen nulas, y las dobles quedan aliadas entre sí, lo que se acepta porque se pueden interpretar con conocimiento del proceso. Resolución V separaría también las dobles, pero para ocho factores exige 64 corridas (2^{8−2}_{V}), demasiadas.

Hay un requisito más, que pesa en el paso 3: la máquina tiene cuatro husillos (la traducción del libro los llama areómetros) que pueden diferir entre sí. Las corridas se van a repartir en los cuatro husillos, así que el diseño se corre en cuatro bloques.""",
  left=[tab(["Factor", "Bajo (−)", "Alto (+)"],
            [["A  Desviación eje x (0.001 pulg)", "0", "15"], ["B  Desviación eje y (0.001 pulg)", "0", "15"],
             ["C  Desviación eje z (0.001 pulg)", "0", "15"], ["D  Fabricante de la herramienta", "1", "2"],
             ["E  Desviación eje a (0.001 grados)", "0", "30"], ["F  Velocidad del husillo (%)", "90", "110"],
             ["G  Altura de la plantilla (0.001 pulg)", "0", "15"], ["H  Velocidad de alimentación (%)", "90", "110"]],
            size=13, colw=[0.6, 0.2, 0.2])],
  right=[num("**Respuesta**: ln(desviación estándar × 10^{3}); el logaritmo estabiliza la varianza",
             "**Supuestos**: triples despreciables; dobles **no** se ignoran",
             "**III** no sirve (principales + dobles); **IV** basta; **V** pide 64 corridas",
             "**Restricción**: 4 husillos que pueden diferir  ⇒  el diseño va en **4 bloques**", size=15),
         note("Resolución requerida: **IV**, corrida en **cuatro bloques**", size=15)],
  ratio=0.5)

S("Ejemplo 4 · Paso 3: ¿16 o 32 corridas? Qué significa «confundir con bloques»",
  """La tabla de diseños recomendados ofrece dos diseños de resolución IV para ocho factores: el 2^{8−4}_{IV} de 16 corridas y el 2^{8−3}_{IV} de 32. Sin bloques, el de 16 bastaría. Los bloques cambian la decisión. Montgomery lo dice así: el de 16 «no puede correrse en cuatro bloques sin confundir cuatro interacciones de dos factores con los bloques». Para entender la frase hay que tener claro qué es confundir.

Dos efectos están confundidos cuando los datos no permiten distinguirlos. Ocurre cuando la columna de signos con la que se estima uno es idéntica a la columna con la que se estima el otro: el contraste calcula entonces la suma de ambos y no hay manera de repartirla. Cuando los dos efectos son de factores, Montgomery lo llama alias; cuando uno de ellos es la diferencia entre bloques (husillos, turnos, días), lo llama confundido con bloques. Es el mismo fenómeno con dos nombres. Ya se vio con el moldeo en dos turnos: la columna ABD valía − en toda la mañana y + en toda la tarde, así que su contraste medía a la vez la interacción ABD y la diferencia entre turnos, y nunca se sabría cuál de las dos se está viendo. En cambio A seguía limpio, porque cada turno tenía cuatro corridas con A alto y cuatro con A bajo y la diferencia se cancelaba.

Por eso cuatro bloques cuestan tres columnas. Para repartir las corridas en cuatro husillos se usan dos columnas P y Q: cada husillo recibe las corridas con una combinación de signos (−,−), (−,+), (+,−) o (+,+). Dentro de cada husillo P es constante, Q es constante y, por tanto, también su producto PQ. Las tres columnas valen lo mismo en todas las corridas de un husillo, así que las tres quedan confundidas con los husillos: son 3 grados de libertad perdidos. Y en un fraccionado cada columna no es un solo efecto sino una cadena de alias completa: lo que se pierde es la cadena entera.

En el 2^{8−4}_{IV} las 15 columnas son 8 efectos principales y 7 cadenas de cuatro interacciones dobles cada una (por ejemplo AB = CG = DH = EF). No hay ninguna columna formada solo por interacciones triples, es decir, ninguna columna «barata». Cualquier columna que se use para bloques cuesta cuatro interacciones dobles de un golpe, que es la frase del libro, y con cuatro bloques hacen falta tres columnas: se perderían 12 de las 28 interacciones dobles, justo lo que los ingenieros no quieren ignorar.

En el 2^{8−3}_{IV} hay 31 columnas. Varias cadenas están formadas solo por interacciones triples y pueden ir a los bloques sin costo; muchas interacciones dobles quedan solas en su cadena. Por eso se elige el 2^{8−3}_{IV} en cuatro bloques de ocho corridas: los bloques obligan a duplicar el tamaño del experimento para no perder las interacciones dobles. Fuente: Montgomery, ejemplo 8-6.""",
  left=[cards(("¿Qué es confundir?", "Dos efectos están **confundidos** cuando se estiman con la **misma columna de "
                                     "signos**: el contraste mide su **suma** y los datos no los separan. Entre efectos "
                                     "de factores se llama **alias**; cuando uno de los dos es la diferencia entre "
                                     "bloques, **confundido con bloques**. Moldeo: ABD era − en la mañana y + en la "
                                     "tarde, su contraste medía ABD **más** el turno"),
              ("¿Por qué 4 bloques cuestan 3 columnas?", "Dos columnas **P** y **Q** reparten las corridas por sus 4 "
                                                          "combinaciones de signos. Dentro de cada bloque P, Q y su "
                                                          "producto **PQ** son constantes: las tres quedan confundidas "
                                                          "(**3 g.l.**), y cada columna arrastra su **cadena de alias "
                                                          "completa**"),
              size=13, cols=1)],
  right=[tab(["", "2^{8−4}_{IV}", "2^{8−3}_{IV}"],
             [["Corridas", "16", "32"],
              ["Columnas (grados de libertad)", "15", "31"],
              ["Cadenas solo de triples", "**ninguna**", "varias"],
              ["Cadenas de dobles", "7, de **4 dobles** cada una", "7 con alias; el resto, dobles solas"],
              ["Con 4 bloques se pierden", "**3 cadenas de dobles** (12 dobles)", "2 cadenas triples y **EH**"]],
             size=13, colw=[0.36, 0.32, 0.32], hl=[4]),
         note("Montgomery: el de 16 «no puede correrse en cuatro bloques sin **confundir cuatro interacciones de dos "
              "factores** con los bloques»: toda columna de bloques sería una cadena de 4 dobles", size=13),
         cards(("Decisión", "Se elige el **2^{8−3}_{IV}** en **4 bloques de 8**: los bloques obligan a duplicar el "
                            "experimento para no perder interacciones dobles"), size=13, cols=1)],
  ratio=0.45)

S("Ejemplo 4 · Paso 4: generadores, relación de definición y alias",
  """El diseño básico es el 2^{5} completo en A, B, C, D y E (32 corridas). Los tres factores restantes se generan con F = ABC, G = ABD y H = BCDE (tabla 8-14). Los generadores son I = ABCF, I = ABDG e I = BCDEH; sus productos completan la relación de definición, con 2^{3} − 1 = 7 palabras: ABCF, ABDG, CDFG, BCDEH, ADEFH, ACEGH y BEFGH. La más corta tiene cuatro letras: resolución IV.

Despreciando las interacciones de tres o más factores, los ocho efectos principales quedan limpios. Las interacciones dobles se reparten así: siete cadenas tienen más de una doble (las de la tabla) y las otras trece dobles quedan solas en su cadena: AE, AH, BE, BH, CE, CH, DE, DH, EF, EG, EH, FH y GH. La cadena que más va a importar es AD = BG: la interacción del eje x con el fabricante de la herramienta está aliada con la del eje y con la altura de la plantilla.""",
  left=[form("F = ABC,   G = ABD,   H = BCDE", size=18),
        form("I = ABCF = ABDG = CDFG = BCDEH", "= ADEFH = ACEGH = BEFGH", size=16),
        note("Palabra más corta: **4 letras**  ⇒  **resolución IV**", size=15)],
  right=[tab(["Cadenas con más de una interacción doble"],
             [["AB = CF = DG"], ["AC = BF"], ["**AD = BG**"], ["AF = BC"], ["AG = BD"], ["CD = FG"], ["CG = DF"]],
             size=14, first_left=False, hl=[2], pad=0.06),
         txt("Los 8 principales, limpios; las otras 13 dobles, **solas** en su cadena", size=14)],
  ratio=0.5)

S("Ejemplo 4 · Paso 5: ¿cómo se reparten en los 4 husillos?",
  f"""Este es el paso de los bloques. Hay cuatro husillos y cada uno va a recibir 8 corridas. Si hubiera una diferencia entre husillos (uno corta un poco peor que otro), esa diferencia se suma a todas sus corridas; el reparto debe hacer que caiga en columnas que no importen.

Se escogen dos columnas P y Q formadas solo por interacciones de orden alto: P = ABE (cadena ABE = CEF = DEG) y Q = ABH (cadena ABH = CFH = DGH). Las dos son cadenas de triples, que se suponen despreciables. Cada corrida tiene un signo de ABE y uno de ABH, y la combinación de los dos signos dice a qué husillo va: (−, −) al husillo 1, (−, +) al 2, (+, −) al 3 y (+, +) al 4. La tabla muestra las 8 corridas de cada husillo.

El precio inevitable es el producto: PQ = ABE · ABH = EH (A y B se cancelan). La columna de EH vale + en los husillos 1 y 4 y − en los husillos 2 y 3, así que también queda confundida con los husillos. EH es la interacción entre la desviación del eje a y la velocidad de alimentación, que los ingenieros consideran muy improbable; por eso se acepta perderla. Su cadena completa es EH = ACG = ADF = BCD = BFG.

Todas las demás columnas, los ocho efectos principales y las demás interacciones dobles, tienen cuatro signos + y cuatro − dentro de cada husillo: la diferencia entre husillos se cancela en sus contrastes. Dentro de cada husillo se sortea el orden de las 8 corridas; no se sortea entre husillos, porque el husillo de cada corrida ya está fijado por el diseño.""",
  left=[tab(["Husillo", "ABE", "ABH", "EH", "Sus 8 corridas"], _tab_h, size=12, first_left=False,
            colw=[0.14, 0.08, 0.08, 0.08, 0.62], pad=0.06),
        txt("Las 32 corridas del 2^{8−3}_{IV} repartidas por los signos de ABE y ABH", size=12),
        num("Escoger **P = ABE** y **Q = ABH**: cadenas **solo de triples**",
            "Cada combinación de signos (P, Q) es un **husillo**",
            "**PQ = ABE · ABH = EH** queda confundida también: es el precio", size=14)],
  right=[cards(("Se pierde", "ABE, ABH y **EH** (eje a × velocidad de alimentación, considerada muy improbable)"),
               ("Se conserva", "Los 8 principales y las demás dobles: **4 + y 4 −** en cada husillo"),
               ("Aleatorización", "El orden se sortea **dentro** de cada husillo"), size=13, cols=1)],
  ratio=0.56)

S("Ejemplo 4 · Paso 6: ¿qué efectos son activos?",
  f"""Con una sola réplica no hay error puro, así que los efectos activos se identifican con la gráfica de probabilidad normal (fig. 8-19 del libro). De las 31 columnas se grafican 28: las tres confundidas con los husillos (ABE, ABH y EH) no son efectos de factores sino diferencias entre husillos, y se dejan fuera. Los valores son los efectos de la tabla 8-17 sobre ln(desviación estándar × 10^{{3}}).

Tres puntos se apartan con claridad de la recta de Daniel: la cadena AD + BG ({f(ef8["AD + BG"][0], 3)}), A ({f(ef8["A"][0], 3)}) y B ({f(ef8["B"][0], 3)}). Les siguen G ({f(ef8["G"][0], 3)}), D ({f(ef8["D"][0], 3)}) y BE ({f(ef8["BE"][0], 3)}), mucho menores. El método de Lenth con los 28 efectos da PSE = {f(pse8, 4)}, ME = {f(me8, 3)} y SME = {f(sme8, 3)}. AD + BG y A superan el SME. B supera el ME pero queda un poco por debajo del SME; se incluye porque se aparta con claridad de la recta y es el tercer efecto en tamaño, casi el doble del siguiente. G queda justo en el límite del ME ({f(ef8["G"][0], 4)} frente a {f(me8, 4)}), y D y BE por debajo: se dejan en el error, como hace Montgomery.

Primera clasificación: al modelo, A, B y la cadena AD + BG; el resto, al error. Falta decidir a qué interacción se atribuye la cadena, que es el paso siguiente.""",
  left=[scatter(_p8, "Efecto", "Puntuación normal", h=4.2, labels=_lab8, line=daniel(_p8, _act8), hi=_act8,
                title="Gráfica normal de los 28 efectos (fig. 8-19)"),
        txt("Sin ABE, ABH y EH, confundidas con los husillos", size=12)],
  right=[num(f"**Se apartan**: AD + BG = {f(ef8['AD + BG'][0], 3)}, A = {f(ef8['A'][0], 3)}, B = {f(ef8['B'][0], 3)}",
             f"**Menores**: G = {f(ef8['G'][0], 3)}, D = {f(ef8['D'][0], 3)}, BE = {f(ef8['BE'][0], 3)}",
             f"**Lenth**: ME = {f(me8, 3)}, SME = {f(sme8, 3)}. AD + BG y A > SME; B > ME; G en el límite; D y BE < ME",
             "Al **modelo**: A, B y la cadena AD + BG", size=15),
         note("Las 3 columnas de los husillos **no se grafican**: no son efectos de factores", size=14)],
  ratio=0.52)

S("Ejemplo 4 · Paso 7: ¿la cadena es AD o BG?",
  f"""La cadena AD + BG es la más grande de todas ({f(ef8["AD + BG"][0], 3)}), pero los datos no pueden separar sus dos términos: AD es la interacción del eje x con el fabricante de la herramienta y BG la del eje y con la altura de la plantilla.

Las herramientas de atribución no deciden aquí. La jerarquía no ayuda, porque las dos son interacciones dobles. La herencia tampoco: cada una contiene un efecto principal grande (A en AD, B en BG) y uno pequeño de tamaño parecido (D = {f(ef8["D"][0], 3)} en AD, G = {f(ef8["G"][0], 3)} en BG). Montgomery lo dice así: no hay una simplificación lógica obvia.

Quedan dos salidas. La primera, conocimiento del proceso: los ingenieros consideran que la interacción real es AD, entre el eje x y el fabricante de la herramienta. La segunda, más corridas: un doblez del factor A o del factor D separaría la cadena. Montgomery sigue la primera y advierte que la conclusión es tentativa. Por jerarquía del modelo, al incluir AD también entra D, aunque su efecto sea pequeño.""",
  body=[tab(["", "AD (eje x × fabricante)", "BG (eje y × altura de plantilla)"],
            [["Jerarquía", "Interacción doble", "Interacción doble"],
             ["Herencia: principal grande", f"A = {f(ef8['A'][0], 3)}", f"B = {f(ef8['B'][0], 3)}"],
             ["Herencia: principal pequeño", f"D = {f(ef8['D'][0], 3)}", f"G = {f(ef8['G'][0], 3)}"],
             ["Conclusión", "**Empate**: los datos no deciden", "**Empate**: los datos no deciden"]],
            size=15, colw=[0.3, 0.35, 0.35]),
        cards(("Conocimiento del proceso", "Los ingenieros juzgan que la interacción real es **AD**"),
              ("Más corridas", "Un **doblez** de A o de D separaría AD de BG"),
              ("Modelo", "**A, B, D y AD**; D entra por **jerarquía**"), size=14)])

S("Ejemplo 4 · Paso 8: hipótesis, modelo y ANOVA con bloques",
  f"""Hipótesis: una por cada cadena que entra al modelo. Para la cadena AD + BG, H_{{0}}: β_{{AD}} + β_{{BG}} = 0 frente a H_{{A}}: β_{{AD}} + β_{{BG}} ≠ 0; igual para A, B y D. Se rechaza H_{{0}} si F_{{0}} > F_{{0.05, 1, 24}} = {f(f_ppf(0.05, 1, 24))} o si el valor p es menor que 0.05.

Modelo: ŷ = β_{{0}} + β_{{A}} x_{{A}} + β_{{B}} x_{{B}} + β_{{D}} x_{{D}} + β_{{AD}} x_{{A}} x_{{D}} + (efecto del husillo) + ε. La tabla ANOVA es la del libro (tabla 8-18). Se rechaza H_{{0}} para A, B, D y AD.

La fila de bloques merece atención. Su suma de cuadrados, 0.0201 con 3 grados de libertad, es exactamente la suma de las tres columnas confundidas con los husillos: SS(ABE) + SS(ABH) + SS(EH) = {f(ef8["ABE"][1], 6)} + {f(ef8["ABH"][1], 6)} + {f(ef8["EH"][1], 6)} = {f(ssb8, 4)}. Se separa del error para que la diferencia entre husillos no infle el error y no le reste potencia a las pruebas. No lleva F_{{0}}: los husillos no se asignaron al azar a las corridas, así que la prueba de bloques no tiene la misma validez que las de los factores. Su cuadrado medio, 0.0067, es menor que el del error (0.0171): los husillos casi no difieren.

El error, 0.4099 con 24 grados de libertad, reúne las 24 columnas que no entraron al modelo ni a los bloques: 31 − 4 − 3 = 24.""",
  left=[tab(["SV", "SS", "DF", "MS", "F_{0}", "P-Value"],
            [["A", "0.6740", "1", "0.6740", "39.42", "<0.0001"], ["B", "0.3217", "1", "0.3217", "18.81", "0.0002"],
             ["D", "0.0935", "1", "0.0935", "5.47", "0.0280"], ["AD", "1.1197", "1", "1.1197", "65.48", "<0.0001"],
             ["**Bloques**", "**0.0201**", "**3**", "**0.0067**", "", ""], ["Error", "0.4099", "24", "0.0171", "", ""],
             ["Total", "2.6389", "31", "", "", ""]], size=14, hl=[4]),
        form(f"H_{{0}}: β_{{AD}} + β_{{BG}} = 0,   F_{{0.05, 1, 24}} = {f(f_ppf(0.05, 1, 24))}", size=15)],
  right=[cards(("Bloques = las 3 columnas de los husillos",
                f"SS(ABE) + SS(ABH) + SS(EH) = **{f(ssb8, 4)}** con **3 g.l.**"),
               ("¿Por qué separarlos?", "Para que la diferencia entre husillos **no infle el error**"),
               ("¿Por qué sin F_{0}?", "Los husillos no se asignaron al azar; MS = 0.0067 < 0.0171: **casi no difieren**"),
               size=13, cols=1),
         note("Error: 31 − 4 (modelo) − 3 (bloques) = **24 g.l.**", size=14)],
  ratio=0.52)

S("Ejemplo 4 · Pasos 9 y 10: supuestos e interpretación",
  f"""Supuestos. Montgomery muestra la gráfica de probabilidad normal de los residuales (fig. 8-20): sugiere colas algo más gruesas que las de la normal, por lo que podría considerarse otra transformación además del logaritmo. Los datos crudos de la tabla 8-16 no se transcribieron aquí, así que esa verificación se cita del libro.

Interpretación. Como el modelo solo tiene A, B y D, el diseño se proyecta en cuatro réplicas de un 2^{{3}} en esos factores (fig. 8-22). Los promedios de ln(desviación) en los ocho vértices dan la interacción AD: con el fabricante 1, la desviación crece mucho al pasar el eje x de 0 a 15 ({f(_ad8[(0, 1)], 3)} a {f(_ad8[(15, 1)], 3)}, promediando sobre B); con el fabricante 2 casi no cambia ({f(_ad8[(0, 2)], 3)} a {f(_ad8[(15, 2)], 3)}). B tiene efecto negativo: la desviación baja cuando el eje y está en su nivel alto.

Conclusión: la desviación del perfil es mínima con A en nivel bajo (eje x en 0), B en nivel alto (eje y en 15) y la herramienta del fabricante 1, vértice con promedio {f(_cubo8[(0, 15, 1)], 3)}. Los husillos casi no difieren. La atribución de la cadena a AD es tentativa y conviene confirmarla con un doblez o una corrida de verificación.""",
  left=[lines(["A bajo (0)", "A alto (15)"],
              [("Fabricante 1 (D −)", [_ad8[(0, 1)], _ad8[(15, 1)]]), ("Fabricante 2 (D +)", [_ad8[(0, 2)], _ad8[(15, 2)]])],
              "ln(desviación) promedio", h=3.6, title="Interacción AD (promedio sobre B)"),
        txt("Promedios del cubo A, B, D de la fig. 8-22", size=12)],
  right=[bul("**Residuales** (fig. 8-20): colas algo gruesas; se podría probar otra transformación",
             "Proyección: **4 réplicas de un 2^{3}** en A, B, D",
             "Con el **fabricante 1**, A sube mucho la desviación; con el **2**, casi nada",
             "B **alto** baja la desviación", size=15),
         note(f"Mejor condición: **A bajo, B alto, fabricante 1** (promedio {f(_cubo8[(0, 15, 1)], 3)}). "
              "Husillos casi iguales. Confirmar AD", size=14)],
  ratio=0.5)

section(7, "Diseños de resolución III", "Saturados, doblez y diseños de Plackett-Burman")

_sat = [["2^{3−1}_{III}", "3", "4", "C = AB"], ["2^{7−4}_{III}", "7", "8", "D = AB, E = AC, F = BC, G = ABC"],
        ["2^{15−11}_{III}", "15", "16", "las 11 interacciones del 2^{4}"], ["2^{31−26}_{III}", "31", "32", "las 26 interacciones del 2^{5}"]]
S("¿Qué son los diseños de resolución III y los diseños saturados?",
  """Un diseño de resolución III es un fraccionado cuya relación de definición tiene como palabra más corta una de tres letras. La consecuencia práctica es que ningún efecto principal está aliado con otro efecto principal, pero cada efecto principal sí está aliado con interacciones de dos factores. Por eso solo se interpretan bien si se puede suponer que esas interacciones son despreciables.

Un diseño saturado es un diseño de resolución III que estudia el máximo número posible de factores con sus corridas: k = N − 1. La razón es una cuenta de grados de libertad. Con N corridas se pueden estimar N − 1 efectos (el grado de libertad restante se usa en la media general). Si hay N − 1 factores, cada uno de esos grados de libertad se gasta en un efecto principal y el diseño queda lleno: no sobra ninguna columna para estimar interacciones ni para el error. Con ocho corridas, siete factores saturan el diseño; con seis factores sobra una columna, con cinco sobran dos, y así sucesivamente.

Estos diseños se usan para tamizado (screening): al comienzo de una investigación, cuando hay muchos factores candidatos y se espera que solo unos pocos importen.

Los saturados que existen se construyen todos igual: se escribe el factorial completo en los primeros factores y a cada interacción de sus columnas se le asigna un factor nuevo. Con el 2^{2} se obtiene el 2^{3−1}_{III} (3 factores en 4 corridas); con el 2^{3}, el 2^{7−4}_{III} (7 en 8), que es el que se desarrolla a continuación; con el 2^{4} en A, B, C y D y once factores igualados a todas sus interacciones, el 2^{15−11}_{III}, que estudia 15 factores en 16 corridas, cada uno alias de siete interacciones dobles; con el 2^{5}, el 2^{31−26}_{III} (31 en 32). Para otro número de factores se eliminan columnas, como se ve más adelante, y cuando N no es potencia de 2 están los diseños de Plackett-Burman.""",
  left=[txt("**Diseño de resolución III**: fraccionado cuya palabra más corta en la relación de definición tiene "
            "**tres letras**. Ningún efecto principal está aliado con otro principal, pero **cada principal sí está "
            "aliado con interacciones dobles**. Solo se interpreta bien si esas interacciones son despreciables.", size=15),
        txt("**Diseño saturado**: diseño de resolución III que estudia el **máximo número de factores** posible, "
            "**k = N − 1**. Con N corridas se estiman N − 1 efectos (un grado de libertad es para la media). Si hay "
            "N − 1 factores, todos los grados de libertad se gastan en efectos principales: el diseño queda **lleno** y "
            "no sobra ninguna columna para interacciones ni para el error.", size=15),
        txt("**Para qué se usan**: tamizado (screening), cuando hay muchos factores candidatos y se espera que "
            "solo unos pocos importen.", size=15)],
  right=[txt("**Los diseños saturados que existen**", size=15),
         tab(["Diseño", "Factores", "Corridas", "Factores nuevos ="], _sat, size=14, first_left=False,
             colw=[0.22, 0.17, 0.17, 0.44]),
         note("Saturado: **N corridas, N − 1 factores**. Para menos factores se **eliminan columnas** con cuidado "
              "(se ve más adelante); para N que no es potencia de 2, **Plackett-Burman**", size=14)],
  ratio=0.55)

_rows = [[str(i + 1)] + [sg(r[c]) for c in "ABCDEFG"] for i, r in enumerate(r4)]
S("El diseño saturado 2^{7−4}_{III}: construcción y alias",
  """Los diseños de resolución III permiten estudiar hasta k = N − 1 factores en N corridas, con N múltiplo de 4. El 2^{7−4} estudia siete factores en solo ocho corridas: se escribe el 2^{3} completo en A, B y C y se definen D = AB, E = AC, F = BC y G = ABC. Se dice que el diseño está saturado porque usa todos los grados de libertad para efectos principales.

El costo es alto: cada efecto principal es alias de tres interacciones dobles. Solo sirve si se puede suponer que las interacciones son despreciables o si se planea un doblez posterior.""",
  left=[tab(["Corrida", "A", "B", "C", "D = AB", "E = AC", "F = BC", "G = ABC"], _rows, size=14,
            first_left=False),
        txt("**Cómo se construye**: (1) se escribe el 2^{3} completo en A, B y C; (2) a cada una de sus cuatro "
            "interacciones (AB, AC, BC, ABC) se le asigna un factor nuevo. Son 3 + 4 = **7 columnas = N − 1**: saturado.",
            size=14)],
  right=[tab(["Columna", "Estima"], [[w, f"{w} + {alias4[w]}"] for w in "ABCDEFG"], size=15,
             first_left=False),
         txt("Alias despreciando interacciones de tres o más factores", size=13)], ratio=0.56)

S("¿Cuál es la relación de definición del 2^{7−4}?",
  """El 2^{7−4} tiene cuatro generadores: I = ABD, I = ACE, I = BCF e I = ABCG. Su relación de definición completa se obtiene multiplicando los generadores de dos en dos, de tres en tres y los cuatro a la vez: tiene 2^{4} − 1 = 15 palabras. La más corta tiene tres letras, así que es de resolución III.

Cada efecto tiene 15 alias. Si se suponen despreciables las interacciones de tres o más factores, cada estimación es la suma del efecto principal y de tres interacciones dobles; son las cadenas de la tabla de la diapositiva anterior (ecuación 8-1 del libro).

Es una fracción un dieciseisavo del 2^{7}. Hay 16 diseños en la familia, uno por cada combinación de signos de los cuatro generadores; con todos positivos se tiene la fracción principal.

Esta lista de 15 palabras es la herramienta para el resto del subtema: al eliminar un factor se tachan las palabras que contienen su letra, y lo que queda es la relación de definición del diseño más pequeño.""",
  body=[form("I = ABD = ACE = BCF = ABCG = BCDE = ACDF = CDG", "= ABEF = BEG = AFG = DEF = ADEG = CEFG = BDFG = ABCDEFG", size=17),
        txt("**Palabra**: producto de letras cuya columna de signos es toda +, es decir, igual a I. **Cómo se obtienen**: "
            "cada generador se convierte en palabra multiplicando por la letra nueva, D = AB ⇒ D·D = ABD ⇒ **I = ABD** "
            "(porque D·D = I). Después se multiplican las palabras entre sí y toda letra repetida se cancela: "
            "ABD · ACE = A^{2}BCDE = **BCDE**. Cuatro generadores dan 2^{4} − 1 = **15 palabras**.", size=15),
        txt("**Alias de B**: se multiplica B por cada palabra (B · ABD = AD, B · BCF = CF, B · BEG = EG, …):", size=14),
        form("B = AD = CF = EG = ACG = CDE = AEF = DFG = ABCE = ABFG = BCDG = BDEF = ABCDF = ABDEG = BCEFG = ACDEFG", size=14),
        cards(("Resolución III", "La palabra más corta tiene **3 letras** (ABD, ACE, …): un principal se alía con dobles"),
              ("15 alias por efecto", "Despreciando triples: principal + **tres interacciones dobles**"),
              ("Para eliminar factores", "Al quitar un factor se **tachan las palabras con su letra**; las que quedan son la nueva relación"),
              size=14)])

S("¿Qué significa eliminar un factor y cuál es el procedimiento?",
  """Los diseños saturados existen solo para k = 3, 7, 15, 31 factores. Cuando el problema tiene otro número de factores, por ejemplo seis, no se construye un diseño nuevo desde cero: se toma el saturado inmediatamente mayor como plantilla y se dejan sin usar las columnas que sobran. A eso se le llama eliminar factores (o eliminar columnas).

Eliminar una columna no cambia las corridas. La columna sigue existiendo en la matriz, porque sus signos son el producto de otras columnas, pero no se le asigna ningún factor real: nadie fija esa variable en el laboratorio. Por eso las palabras que contienen su letra desaparecen de la relación de definición. Una palabra como ABCG dice que la columna de G es igual al producto de A, B y C; si G ya no es un factor, esa igualdad ya no liga a factores entre sí. Y las columnas que quedan libres no se pierden: cada una estima una cadena de interacciones.

Procedimiento paso a paso:
1. Contar los factores k y escoger el saturado más pequeño con N − 1 ≥ k (N = 4, 8, 16, 32).
2. Calcular cuántas columnas sobran: N − 1 − k.
3. Elegir cuáles eliminar. Se prefieren columnas generadas, se revisa que las que quedan no formen una palabra corta entre sí y, si es posible, que solo sobrevivan palabras de cuatro o más letras, porque así el diseño gana resolución.
4. Borrar esas columnas de la tabla. Las N corridas quedan iguales.
5. Escribir la nueva relación de definición: se tacha toda palabra que contenga alguna letra eliminada. La palabra más corta que quede da la resolución.
6. Escribir los nuevos alias: en cada cadena se tachan los términos que contienen letras eliminadas.
7. Interpretar las columnas libres: cada una estima una cadena de interacciones; si se suponen nulas, dan grados de libertad para estimar el error.""",
  left=[txt("**Eliminar un factor** = usar el saturado como **plantilla** para menos factores, dejando **sin asignar** "
            "las columnas que sobran. Se hace porque los saturados solo existen para k = 3, 7, 15, 31.", size=15),
        cards(("Las corridas no cambian", "La columna sigue en la matriz (sus signos son producto de otras), pero "
                                          "**nadie fija esa variable** en el laboratorio"),
              ("Por qué se tachan palabras", "ABCG dice «la columna G = A·B·C». Si G no es un factor, esa igualdad "
                                             "**ya no liga factores**: la palabra sale de la relación"),
              size=14, cols=1)],
  right=[txt("**Paso a paso**", size=16),
         num("**Contar k** y escoger el saturado más pequeño con **N − 1 ≥ k** (N = 4, 8, 16, 32)",
             "**Cuántas sobran**: N − 1 − k columnas",
             "**Cuáles eliminar**: que lo que queda **no forme palabras cortas**; si se puede, que solo "
             "sobrevivan palabras de **4 o más letras** (se gana resolución)",
             "**Borrar** esas columnas: las N corridas quedan iguales",
             "**Nueva relación**: tachar toda palabra con una letra eliminada; la más corta que quede da la **resolución**",
             "**Nuevos alias**: tachar en cada cadena los términos con letras eliminadas",
             "**Columnas libres**: estiman cadenas de interacciones o dan grados de libertad al error", size=13)],
  ratio=0.45)

_rows98 = [[str(i + 1)] + [sg(r[c]) for c in "ABCDEF"] + ["(" + sg(r["G"]) + ")"] for i, r in enumerate(r4)]
S("Ejemplo: ¿cómo se pasa del 2^{7−4} a seis factores?",
  """Se aplican los siete pasos a un caso concreto: hay seis factores y solo se pueden hacer ocho corridas.

Paso 1: con k = 6 el saturado más pequeño que alcanza es el de N = 8, el 2^{7−4}_{III}: el 2^{3} en A, B y C con D = AB, E = AC, F = BC y G = ABC (la tabla).

Paso 2: sobran N − 1 − k = 8 − 1 − 6 = 1 columna.

Paso 3: se elige cuál. Con seis factores en ocho corridas el diseño es necesariamente de resolución III, y quitar D, E, F o G da lo mismo en resolución: siempre quedan siete palabras y la más corta es de tres letras. Se elige G.

Paso 4: se borra la columna de G. Las ocho corridas quedan iguales; solo que nadie fija esa columna. El diseño que queda es un 2^{6−3}_{III}, con D = AB, E = AC y F = BC.

Paso 5: nueva relación de definición. De las 15 palabras del 2^{7−4} (I = ABD = ACE = BCF = ABCG = BCDE = ACDF = CDG = ABEF = BEG = AFG = DEF = ADEG = BDFG = CEFG = ABCDEFG) se tachan las ocho que tienen G y quedan siete: I = ABD = ACE = BCF = BCDE = ACDF = ABEF = DEF. La más corta tiene tres letras: resolución III.

Paso 6: los alias se aligeran. En el 2^{7−4}, A = BD = CE = FG; al quitar G desaparece FG y queda A = BD = CE. Cada efecto principal pasa de tres interacciones dobles aliadas a dos.

Paso 7: la columna liberada no se tira. La columna ABC, que era la de G, ahora estima la cadena de interacciones AF + BE + CD. Sirve para ver si hay interacciones o, si se suponen nulas, como un grado de libertad para el error.""",
  left=[tab(["Corrida", "A", "B", "C", "D = AB", "E = AC", "F = BC", "G = ABC (se borra)"], _rows98, size=13,
            first_left=False, pad=0.06),
        note("Las **8 corridas no cambian**: solo la columna de G deja de ser un factor", size=14)],
  right=[num("k = 6  ⇒  N − 1 ≥ 6  ⇒  **N = 8**: el **2^{7−4}_{III}**",
             "Sobran 8 − 1 − 6 = **1 columna**",
             "Quitar D, E, F o G da igual (siempre III): se elige **G**",
             "Se **borra** G  ⇒  **2^{6−3}_{III}** con D = AB, E = AC, F = BC",
             "Se tachan las 8 palabras con G; quedan **7**, la más corta de 3 letras: **III**",
             "En A = BD = CE = FG sale FG  →  **A = BD = CE**",
             "La columna ABC (la de G) estima **AF + BE + CD**", size=13),
         form("I = ABD = ACE = BCF = BCDE", "= ACDF = ABEF = DEF", size=15)],
  ratio=0.53)

S("¿Qué diseño queda según cuántos factores se eliminen?",
  """La tabla aplica el mismo procedimiento quitando cada vez más columnas del 2^{7−4}. En cada fila, la relación de definición son las palabras de la original que solo usan las letras que quedan.

Con seis factores (se quita G) queda el 2^{6−3}_{III} de la diapositiva anterior. Con cinco (se quitan F y G) queda el 2^{5−2}_{III}, con D = AB y E = AC e I = ABD = ACE = BCDE; los alias de A son BD y CE, y las dos columnas libres estiman BC + DE y BE + CD.

Con cuatro factores aparece la lección importante: importa cuáles se quitan. Si se quitan E, F y G queda D = AB, con I = ABD: resolución III, y A, B y D siguen aliados con interacciones dobles. Si en cambio se quitan D, E y F y se conserva G = ABC, la única palabra es ABCG, de cuatro letras: resolución IV, y los cuatro efectos principales quedan libres de interacciones dobles. Con el mismo número de corridas se gana una resolución. Es el 2^{4−1}_{IV} de la tabla de diseños recomendados (allí la cuarta letra se llama D, con D = ABC). Las tres columnas libres estiman AB + CG, AC + BG y AG + BC.

Con tres factores lo correcto es quedarse con A, B y C, las columnas del diseño básico: no queda ninguna palabra y el diseño es el 2^{3} completo. La diapositiva siguiente muestra qué pasa si se eligen mal.""",
  body=[txt("Cada fila repite los siete pasos sobre el 2^{7−4}, quitando cada vez más columnas. La **relación de definición** "
            "de cada fila son las palabras de la original que **solo usan las letras que quedan**, y la **resolución** es la "
            "longitud de la más corta. Al quitar columnas los alias se aligeran y las columnas libres pasan a estimar interacciones.",
            size=15),
        tab(["Factores", "Se eliminan", "Diseño que queda", "Relación de definición", "Alias de A (dobles)", "Columnas libres estiman"],
            [["6", "G", "2^{6−3}_{III}", "ABD, ACE, BCF, BCDE, ACDF, ABEF, DEF", "BD, CE", "AF + BE + CD"],
             ["5", "F, G", "2^{5−2}_{III}", "ABD, ACE, BCDE", "BD, CE", "BC + DE;  BE + CD"],
             ["4", "E, F, G", "2^{4−1}_{III}", "ABD", "BD", "AC;  BC;  CD"],
             ["**4**", "**D, E, F**", "**2^{4−1}_{IV}**", "**ABCG**", "**ninguno**", "AB + CG;  AC + BG;  AG + BC"],
             ["3", "D, E, F, G", "**2^{3} completo**", "ninguna", "ninguno", "AB, AC, BC, ABC"]],
            size=13, hl=[3], first_left=False, colw=[0.09, 0.12, 0.14, 0.27, 0.14, 0.24]),
        cards(("Con 4 factores importa cuáles se quitan", "Si se conserva **G = ABC**, la única palabra que sobrevive es "
                                                       "**ABCG** (4 letras): **resolución IV**, principales libres de dobles. "
                                                       "Si se conserva D = AB sobrevive ABD (3 letras): solo III"),
              ("Con 3 factores", "Quedarse con **A, B y C**: no sobrevive ninguna palabra y se obtiene el **2^{3} completo**. "
                                 "Otra elección puede repetir corridas (diapositiva siguiente)"),
              size=13)])

_dup3 = {0: 3, 2: 1, 1: 4, 3: 2, 4: 7, 6: 5, 5: 8, 7: 6}
_rows3 = [[str(i + 1), sg(r["A"]), sg(r["C"]), sg(r["E"]), f"= corrida {_dup3[i]}", sg(r["A"]), sg(r["B"]), sg(r["C"])]
          for i, r in enumerate(r4)]
S("¿Qué pasa si se eliminan mal las columnas?",
  """Supóngase que hay tres factores y se toman del 2^{7−4} las columnas A, C y E, eliminando B, D, F y G. Parece razonable, pero E = AC: la palabra ACE sigue en la relación de definición. El diseño en A, C y E es entonces una fracción 2^{3−1} con I = ACE.

La tabla lo hace visible. En la columna de la izquierda solo aparecen cuatro combinaciones distintas de A, C y E: (−, −, +), (+, −, −), (−, +, −) y (+, +, +), cada una dos veces. Las ocho corridas son dos réplicas de un 2^{3−1}: cada efecto principal sigue aliado con una interacción doble (A = CE, C = AE, E = AC) y la mitad de las combinaciones de tratamientos nunca se prueba.

Con las mismas ocho corridas se puede tener algo mucho mejor: quedarse con A, B y C, las columnas del diseño básico. Entre ellas no hay ninguna palabra, así que las ocho corridas son las ocho combinaciones distintas del 2^{3} completo, sin ningún alias.

La regla práctica: al eliminar columnas, revisar que el subconjunto que queda no forme una palabra de la relación de definición. Si la forma, el diseño se repite en lugar de completarse.""",
  left=[tab(["N°", "Mala: A", "C", "E = AC", "Se repite", "Buena: A", "B", "C"], _rows3, size=12,
            first_left=False, pad=0.06, colw=[0.08, 0.13, 0.08, 0.12, 0.21, 0.14, 0.08, 0.08]),
        txt("Mala elección: A, C, E (cada combinación aparece dos veces). Buena: A, B, C (8 combinaciones distintas)", size=12)],
  right=[cards(("Quedarse con A, C, E", "ACE es una palabra: **2^{3−1} repetido dos veces**. Solo 4 combinaciones "
                                         "distintas; A = CE, C = AE, E = AC"),
               ("Quedarse con A, B, C", "Ninguna palabra: **2^{3} completo**, 8 combinaciones distintas, sin alias"),
               ("Regla", "El subconjunto que queda **no debe formar una palabra** de la relación de definición"),
               size=14, cols=1)],
  ratio=0.56)

S("¿Qué es el doblez y qué otras salidas hay para los alias?",
  """En un diseño de resolución III cada efecto principal está mezclado con interacciones dobles. Para separarlos se usa el ensamblaje secuencial: se corre una segunda fracción en la que se han invertido los signos de algunos factores y se combinan las dos. A esta técnica se le llama doblez o plegado (fold over). Hay dos variantes: el doblez de un solo factor invierte los signos de un factor; el doblez completo, o reflexión, invierte los signos de todos.

La estructura de alias de la segunda fracción no hay que calcularla de cero: se obtiene cambiando el signo de los factores invertidos en la estructura de alias de la fracción original. Después, como con la fracción alterna, la semisuma y la semidiferencia de las estimaciones de las dos fracciones separan los efectos; las dos fracciones funcionan como bloques.

Las conclusiones de un fraccionado son tentativas porque siempre existe una explicación alternativa basada en los alias, y la tabla reúne las cuatro formas de resolver la duda. Corrida de confirmación: predecir con el modelo la respuesta en una condición nueva y comprobarla. Fracción alterna: en una fracción un medio, correr la otra mitad completa el factorial. Doblez completo: separa los efectos principales de las interacciones dobles y convierte un diseño de resolución III en uno de resolución IV. Doblez de un factor: en un diseño de resolución III o mayor, y despreciando interacciones de tres o más factores, deja limpio ese factor y todas sus interacciones dobles; cuesta las mismas corridas que el doblez completo.""",
  left=[bul("Correr una **segunda fracción** con signos invertidos y combinarla con la primera",
            "Alias de la segunda fracción: **cambiar el signo** de los factores invertidos",
            "Separar con **½ (ℓ + ℓ′)** y **½ (ℓ − ℓ′)**: cada una aísla una parte de la cadena", size=16),
        note("Las dos fracciones funcionan como **bloques**", size=15)],
  right=[tab(["Estrategia", "Qué se corre", "Qué se gana"],
             [["Confirmación", "Una o pocas corridas nuevas", "Verifica la predicción del modelo"],
              ["Fracción alterna", "La otra mitad del 2^{k−1}", "Completa el factorial"],
              ["Doblez completo", "Todos los signos invertidos", "Principales libres de dobles (III → IV)"],
              ["Doblez de un factor", "Signos de **un** factor invertidos", "Ese factor y sus dobles, limpios"]],
             size=14, colw=[0.26, 0.36, 0.38])], ratio=0.42)

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
  """Se corre el 2^{7−4}_{III} de ocho corridas del enunciado anterior (Montgomery, ejemplo 8-7).

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

Advertencia: su estructura de alias es muy compleja. En el diseño de 12 corridas cada efecto principal es alias parcial de todas las interacciones dobles en las que no interviene: por ejemplo, la interacción AB es alias parcial de los nueve efectos principales C, D, …, K, y cada efecto principal es alias parcial de 45 interacciones dobles. «Parcial» quiere decir que la interacción no se suma completa a la estimación, sino con un peso fraccionario. Si hay interacciones importantes, pueden aparecer como varios falsos efectos principales. En diseños mayores la situación es aún más compleja; Montgomery recomienda usarlos con mucho cuidado, y bajo ciertas condiciones sus alias se pueden desenredar con técnicas de regresión.

Su ventaja está en la proyección. El de 12 corridas se proyecta en tres réplicas de un 2^{2} completo en cualquier par de factores, y en cualquier trío de factores en un 2^{3} completo más una fracción 2^{3−1}. Por eso se dice que tiene proyectividad 3, mientras que un 2^{k−p}_{III} solo tiene proyectividad 2. Las proyecciones en tres y cuatro factores no son balanceadas.""",
  left=[bul("Resolución III para **k = N − 1** factores en N corridas",
            "N **múltiplo de 4**: 12, 20, 24, 28, 36",
            "Para N = 12, 20, 24 y 36 se construye **desplazando cíclicamente** un renglón generador y agregando un renglón de signos −"),
        tab(["N", "Renglón generador"], [["12", "+ + − + + + − − − + −"],
             ["20", "+ + − − + + + + − + − + − − − − + + −"],
             ["24", "+ + + + + − + − + + − − + + − − + − + − − − −"]], size=14, colw=[0.1, 0.9], first_left=False)],
  right=[cards(("Alias parciales", "En el de 12 corridas cada principal es alias **parcial** (con peso fraccionario) de 45 "
                                   "interacciones dobles; una interacción real puede aparecer como **varios** falsos principales"),
               ("Proyectividad 3", "En cualquier par: 3 réplicas de un 2^{2}; en cualquier trío: un 2^{3} completo + un "
                                   "2^{3−1} (no balanceado). Un 2^{k−p}_{III} solo tiene proyectividad 2"),
               size=14, cols=1),
         bul("Úselos **con mucho cuidado**, para tamizado sin interacciones esperadas; un **2^{k−p}** de tamaño "
             "parecido puede ser mejor elección", size=15)], ratio=0.52)

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

section(8, "Diseños de resolución IV y V", "Diseños mínimos, doblez y fracciones irregulares")

_rows = [["+", "−", "−", "+"], ["+", "+", "−", "−"], ["+", "−", "+", "−"], ["+", "+", "+", "+"],
         ["−", "+", "+", "−"], ["−", "−", "+", "+"], ["−", "+", "−", "+"], ["−", "−", "−", "−"]]
S("¿Qué es un diseño de resolución IV y cómo se obtiene de uno de resolución III?",
  """Un 2^{k−p} es de resolución IV si los efectos principales están separados de las interacciones dobles y algunas interacciones dobles son alias entre sí. Si se suprimen las interacciones de tres o más factores, los efectos principales se estiman directamente. Ya se vieron dos: el 2^{6−2}_{IV} del ejemplo 3 y el 2^{7−3}_{IV} que resultó de combinar las dos fracciones del ejemplo 5.

Hay un límite inferior de tamaño: todo diseño 2^{k−p}_{IV} debe tener al menos 2k corridas. Los diseños de resolución IV con exactamente 2k corridas se llaman diseños mínimos. Por ejemplo, el 2^{4−1}_{IV} tiene 8 = 2·4 corridas y el 2^{8−4}_{IV} tiene 16 = 2·8.

Los diseños de resolución IV se pueden obtener doblando un diseño de resolución III. Se toma el 2^{k−p}_{III}, se le agrega la segunda fracción con todos los signos invertidos, y se aprovecha la columna identidad: en la primera fracción es toda +, y en la segunda se cambia a toda −. Esa columna se asigna al factor k + 1. El resultado es un 2^{k+1−p}_{IV}. La tabla es la del libro (tabla 8-27): del 2^{3−1}_{III} con I = ABC se obtiene un 2^{4−1}_{IV}, y es fácil verificar que su relación de definición es I = ABCD. Con cuatro corridas más se gana un factor y se sube de resolución III a IV.""",
  left=[bul("Principales **separados** de las interacciones dobles; algunas dobles son **alias entre sí**",
            "Suprimiendo triples, los principales se estiman **directamente**",
            "Tamaño mínimo **N ≥ 2k**; con exactamente 2k corridas se llama diseño **mínimo**", size=15),
        tab(["Diseño mínimo", "Factores", "Corridas = 2k"],
            [["2^{4−1}_{IV}", "4", "8"], ["2^{8−4}_{IV}", "8", "16"], ["2^{16−11}_{IV}", "16", "32"]],
            size=14, first_left=False)],
  right=[tab(["D (columna I)", "A", "B", "C"], _rows, size=13, hl=[0, 1, 2, 3], first_left=False, pad=0.07),
         num("Tomar el **2^{k−p}_{III}** y agregar la fracción con **todos los signos invertidos**",
             "La columna **I** pasa de + a −: se asigna al factor **k + 1**  ⇒  2^{3−1}_{III} → 2^{4−1}_{IV}, I = ABCD",
             size=14),
         txt("Tabla 8-27 del libro: arriba la fracción original (I = ABC), abajo la invertida", size=12)], ratio=0.48)

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
