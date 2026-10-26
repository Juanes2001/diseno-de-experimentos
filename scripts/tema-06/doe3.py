"""Cálculos para diseños 3^k: componentes de interacción, bloques, fracciones y ANOVA (Montgomery, cap. 9).

Niveles 0, 1, 2. Una corrida es una tupla de k dígitos (nivel de A, de B, …). Un componente de
interacción se representa por su vector de exponentes (α_1, …, α_k) con α_i ∈ {0, 1, 2}, normalizado
para que el primer exponente distinto de cero sea 1. Toda la aritmética es módulo 3.
"""
import itertools
import math

from doe import f_sf

LETRAS = "ABCDEFGHJK"


# ---------------------------------------------------------------- corridas y palabras
def runs3(k):
    """Las 3^k combinaciones en orden estándar: el primer factor cambia más rápido."""
    return [tuple(reversed(r)) for r in itertools.product((0, 1, 2), repeat=k)]


def dig(run):
    return "".join(str(x) for x in run)


def normalize(e):
    """Primer exponente no nulo igual a 1 (si es 2, se eleva al cuadrado: ×2 mod 3)."""
    e = tuple(x % 3 for x in e)
    for x in e:
        if x:
            return e if x == 1 else tuple((2 * v) % 3 for v in e)
    return e


def word(e, letras=LETRAS, sup=True):
    """Nombre del componente: (1,2,0) → AB^{2}; (0,...,0) → I."""
    out = []
    for a, L in zip(e, letras):
        if a == 1:
            out.append(L)
        elif a == 2:
            out.append(L + ("^{2}" if sup else "²"))
    return "".join(out) or "I"


def parse(w, k, letras=LETRAS):
    """'AB2C' o 'AB^{2}C' → vector de exponentes."""
    w = w.replace("^{", "").replace("}", "").replace("²", "2")
    e = [0] * k
    i = 0
    while i < len(w):
        j = letras.index(w[i])
        if i + 1 < len(w) and w[i + 1] == "2":
            e[j] = 2
            i += 2
        else:
            e[j] = 1
            i += 1
    return tuple(e)


def mult(e1, e2, p=1):
    """Producto e1 · e2^p (p = 1 o 2) normalizado."""
    return normalize(tuple(a + p * b for a, b in zip(e1, e2)))


def L_val(run, e):
    return sum(a * x for a, x in zip(e, run)) % 3


def gen_ints(P, Q):
    """Interacciones generalizadas de dos componentes: PQ y PQ^2."""
    return mult(P, Q, 1), mult(P, Q, 2)


def defining(gens):
    """Relación de definición completa: todos los productos ∏ g_i^{c_i} con c ∈ {0,1,2}^p, salvo I."""
    k = len(gens[0])
    words = set()
    for cs in itertools.product((0, 1, 2), repeat=len(gens)):
        if not any(cs):
            continue
        e = tuple(sum(c * g[i] for c, g in zip(cs, gens)) % 3 for i in range(k))
        words.add(normalize(e))
    return sorted(words, key=lambda e: (sum(1 for a in e if a), e))


def aliases(e, words):
    """Alias de un efecto: e·W y e·W^2 para cada palabra W de la relación de definición."""
    out = []
    for w in words:
        out.append((mult(e, w, 1), mult(e, w, 2)))
    return out


def components(factors, k):
    """Los 2^{h−1} componentes de la interacción de los factores dados (índices)."""
    h = len(factors)
    out = set()
    for exps in itertools.product((1, 2), repeat=h):
        e = [0] * k
        for i, a in zip(factors, exps):
            e[i] = a
        out.add(normalize(e))
    return sorted(out)


def blocks(k, gens):
    """Bloques del 3^k confundiendo los generadores: dict (L_1, …, L_p) → corridas."""
    out = {}
    for r in runs3(k):
        key = tuple(L_val(r, g) for g in gens)
        out.setdefault(key, []).append(r)
    return out


def fraction(k, gens, us=None):
    """Fracción 3^{k−p}: corridas con L_i = u_i (por defecto todas cero, la fracción principal)."""
    us = us or tuple(0 for _ in gens)
    return [r for r in runs3(k) if tuple(L_val(r, g) for g in gens) == tuple(us)]


def basic_design(k, p, rels):
    """Diseño básico 3^{k−p} y factores adicionales x_j = Σ β_i x_i (mod 3). rels: lista de tuplas β."""
    out = []
    for b in runs3(k - p):
        extra = tuple(sum(c * x for c, x in zip(bet, b)) % 3 for bet in rels)
        out.append(tuple(b) + extra)
    return out


def betas_from_word(e):
    """Ec. 9-5: para I = AB^{α_2}…K^{α_k}, x_k = Σ β_i x_i con β_i = (3 − α_k) α_i mod 3."""
    ak = e[-1]
    return tuple(((3 - ak) * a) % 3 for a in e[:-1])


# ---------------------------------------------------------------- sumas de cuadrados
class Datos:
    """Observaciones de un 3^k (posiblemente parcial): dict corrida → lista de réplicas."""

    def __init__(self, k, obs):
        self.k = k
        self.obs = {tuple(r): list(v) for r, v in obs.items()}
        self.N = sum(len(v) for v in self.obs.values())
        self.total = sum(sum(v) for v in self.obs.values())
        self.cf = self.total ** 2 / self.N
        self.ybar = self.total / self.N

    def sst(self):
        return sum(y * y for v in self.obs.values() for y in v) - self.cf

    def ss_cells(self, factors):
        """SS entre las celdas definidas por un subconjunto de factores (sin restar subconjuntos)."""
        tot, cnt = {}, {}
        for r, v in self.obs.items():
            key = tuple(r[i] for i in factors)
            tot[key] = tot.get(key, 0) + sum(v)
            cnt[key] = cnt.get(key, 0) + len(v)
        return sum(t * t / cnt[key] for key, t in tot.items()) - self.cf

    def ss_effect(self, factors):
        """SS de un efecto principal (|factors| = 1) o de una interacción, por diferencias."""
        factors = tuple(factors)
        ss = self.ss_cells(factors)
        for h in range(1, len(factors)):
            for sub in itertools.combinations(factors, h):
                ss -= self.ss_effect(sub)
        return ss

    def ss_component(self, e):
        """SS (2 g.l.) del componente con exponentes e: tres totales según L mod 3."""
        tot, cnt = [0, 0, 0], [0, 0, 0]
        for r, v in self.obs.items():
            l = L_val(r, e)
            tot[l] += sum(v)
            cnt[l] += len(v)
        return sum(t * t / c for t, c in zip(tot, cnt)) - self.cf, tot

    def ss_contrast(self, coefs):
        """SS (1 g.l.) de un contraste polinómico: coefs = dict factor → (c0, c1, c2) o None."""
        num, den = 0.0, 0.0
        for r, v in self.obs.items():
            c = 1.0
            for i, cc in coefs.items():
                c *= cc[r[i]]
            num += c * sum(v)
            den += c * c * len(v)
        return num * num / den

    def sse(self):
        """Error puro: variación dentro de cada celda."""
        return sum(sum((y - sum(v) / len(v)) ** 2 for y in v) for v in self.obs.values())

    def dfe(self):
        return sum(len(v) - 1 for v in self.obs.values())

    def anova(self, terms, error=None):
        """terms: lista de (nombre, tupla de factores). error = (SS, g.l.) o None → error puro."""
        rows = []
        if error is None:
            sse, dfe = self.sse(), self.dfe()
        else:
            sse, dfe = error
        mse = sse / dfe if dfe else float("nan")
        for name, fs in terms:
            ss = self.ss_effect(fs)
            df = 2 ** len(fs)
            F = (ss / df) / mse if dfe else float("nan")
            rows.append((name, ss, df, ss / df, F, f_sf(F, df, dfe) if dfe else float("nan")))
        return rows, sse, dfe, mse


LIN, QUAD = (-1, 0, 1), (1, -2, 1)


def lstsq(X, y):
    """Mínimos cuadrados sin numpy: resuelve (X'X) b = X'y por eliminación gaussiana."""
    n, p = len(X), len(X[0])
    A = [[sum(X[r][i] * X[r][j] for r in range(n)) for j in range(p)] + [sum(X[r][i] * y[r] for r in range(n))]
         for i in range(p)]
    for i in range(p):
        piv = max(range(i, p), key=lambda r: abs(A[r][i]))
        A[i], A[piv] = A[piv], A[i]
        for r in range(p):
            if r != i:
                f = A[r][i] / A[i][i]
                A[r] = [a - f * b for a, b in zip(A[r], A[i])]
    return [A[i][p] / A[i][i] for i in range(p)]


def fit_quad(xs, ys):
    """Modelo cuadrático completo en dos variables codificadas: b0, b1, b2, b11, b22, b12."""
    X = [[1, x1, x2, x1 * x1, x2 * x2, x1 * x2] for x1, x2 in xs]
    b = lstsq(X, ys)
    fitted = [sum(c * v for c, v in zip(b, row)) for row in X]
    res = [y - f for y, f in zip(ys, fitted)]
    return b, fitted, res
