"""Caso del tema 6: Cui et al. (2023), motor PMSM, 2^(6-2) de resolución IV (Electronics 12, 5024).

Recalcula los 15 contrastes de la tabla 3 del artículo para las tres respuestas (eficiencia, par medio y
rizado de par) y aplica el método de Lenth (PSE, ME al 5 % y al 10 %). Verifica también que los
generadores son E = ABC y F = BCD, los mismos del ejemplo 3 de la presentación (Montgomery, ej. 8-4).

Uso:  .venv/bin/python -I scripts/tema-06/caso_cui.py
"""
import itertools
import math

# Tabla 3 de Cui et al.: std, run, Ws, Ht, At, Tb, delta, Lef, eficiencia (%), par medio (N m), rizado (%)
TABLA_3 = """1 1 2.5 0.901 15 1.7 0.6 115 92.386 105.310 14.228
15 2 2.5 1.301 25 2.7 0.6 135 92.225 119.530 14.342
3 3 2.5 1.301 15 1.7 0.8 135 93.031 118.130 11.729
13 4 2.5 0.901 25 2.7 0.8 115 92.866 96.734 14.983
8 5 3.3 1.301 25 1.7 0.8 115 93.038 99.128 15.670
10 6 3.3 0.901 15 2.7 0.8 135 93.089 111.610 18.312
7 7 2.5 1.301 25 1.7 0.6 115 92.271 105.230 15.591
12 8 3.3 1.301 15 2.7 0.6 115 92.311 100.790 18.754
9 9 2.5 0.901 15 2.7 0.6 135 92.288 119.540 14.731
16 10 3.3 1.301 25 2.7 0.8 135 93.113 111.440 19.263
4 11 3.3 1.301 15 1.7 0.6 135 92.549 122.670 18.285
2 12 3.3 0.901 15 1.7 0.8 115 93.029 99.201 15.882
11 13 2.5 1.301 15 2.7 0.8 115 92.890 96.686 15.005
5 14 2.5 0.901 25 1.7 0.8 135 93.000 118.160 12.418
14 15 3.3 0.901 25 2.7 0.6 115 92.326 100.760 19.180
6 16 3.3 0.901 25 1.7 0.6 135 92.576 122.640 18.676"""
ALTO = [3.3, 1.301, 25, 2.7, 0.8, 135]
FACTORES = "ABCDEF"
NOMBRES = {"A": "Ws apertura de ranura", "B": "Ht altura del hombro", "C": "At ángulo del hombro",
           "D": "Tb puente externo del imán", "E": "δ entrehierro", "F": "Lef longitud del núcleo"}
# t(0.975, 5) y t(0.95, 5): grados de libertad de Lenth = m/3 = 15/3 = 5
T_05, T_10 = 2.571, 2.015


def cargar():
    datos = []
    for linea in TABLA_3.splitlines():
        v = linea.split()
        x = [1 if float(v[2 + i]) == ALTO[i] else -1 for i in range(6)]
        datos.append((int(v[0]), x, float(v[8]), float(v[9]), float(v[10])))
    return sorted(datos)


def columnas(datos):
    """Las 15 columnas de signos estimables, con todas las palabras que caen en cada una."""
    cols = {}
    for r in range(1, 7):
        for comb in itertools.combinations(range(6), r):
            clave = tuple(math.prod(x[i] for i in comb) for _, x, *_ in datos)
            cols.setdefault(clave, []).append("".join(FACTORES[i] for i in comb))
    return {k: v for k, v in cols.items() if any(s != 1 for s in k)}


def lenth(efectos):
    abs_ = sorted(abs(e) for e in efectos)
    s0 = 1.5 * (abs_[len(abs_) // 2] if len(abs_) % 2 else (abs_[len(abs_) // 2 - 1] + abs_[len(abs_) // 2]) / 2)
    sub = sorted(a for a in abs_ if a < 2.5 * s0)
    med = sub[len(sub) // 2] if len(sub) % 2 else (sub[len(sub) // 2 - 1] + sub[len(sub) // 2]) / 2
    return 1.5 * med


def main():
    datos = cargar()
    for nombre, idx in [("E = ABC", (0, 1, 2, 4)), ("F = BCD", (1, 2, 3, 5))]:
        ok = all(math.prod(x[i] for i in idx) == 1 for _, x, *_ in datos)
        print(f"Generador {nombre}: {'se cumple' if ok else 'NO se cumple'} en las 16 corridas")
    print("Relación de definición: I = ABCE = BCDF = ADEF  (resolución IV)\n")
    cols = columnas(datos)
    for ri, resp in [(2, "Eficiencia η (%)"), (3, "Par medio Tave (N·m)"), (4, "Rizado de par Trip (%)")]:
        efs = []
        for clave, alias in cols.items():
            efecto = sum(s * d[ri] for s, d in zip(clave, datos)) / 8
            cortos = [a for a in alias if len(a) <= 2]
            efs.append((efecto, " = ".join(cortos) if cortos else " + ".join(a for a in alias if len(a) == 3)))
        pse = lenth([e for e, _ in efs])
        print(f"== {resp}: PSE = {pse:.4f}   ME(5 %) = {T_05 * pse:.4f}   ME(10 %) = {T_10 * pse:.4f}")
        print(f"   {'cadena':16s} {'efecto':>9s}  {'SS':>9s}  decisión")
        for e, al in sorted(efs, key=lambda t: -abs(t[0])):
            ss = (e * 8) ** 2 / 16
            dec = "activo (5 %)" if abs(e) > T_05 * pse else ("activo (10 %)" if abs(e) > T_10 * pse else "")
            print(f"   {al:16s} {e:9.4f}  {ss:9.4f}  {dec}")
        print()


if __name__ == "__main__":
    main()
