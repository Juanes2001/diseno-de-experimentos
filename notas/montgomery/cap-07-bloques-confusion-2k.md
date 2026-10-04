# Capítulo 7 — Formación de bloques y confusión en el diseño factorial 2^k

> Montgomery, págs. 287–302

Convenciones de esta ficha: $k$ = número de factores, $n$ = número de réplicas, $N = n2^k$,
$p$ = número de efectos independientes confundidos ($2^p$ bloques de tamaño $2^{k-p}$).
Las combinaciones de tratamientos se escriben en notación de letras minúsculas: $(1), a, b, ab,\dots$
Las anotaciones marcadas como *(nota propia)* no están en el texto del libro; son aclaraciones.

---

## 7-1 Introducción

- **Problema**: muchas veces no es posible correr todas las $2^k$ (o $n2^k$) corridas en condiciones
  homogéneas (un lote de materia prima no alcanza, un turno no alcanza, etc.).
- También puede ser deseable **variar deliberadamente** las condiciones (p. ej. varios lotes de
  materia prima) para que las conclusiones sean **robustas** frente a condiciones que se
  encontrarán en la práctica.
- La técnica para ambos casos es la **formación de bloques**. El capítulo cubre:
  1. $2^k$ con réplicas, cada réplica en un bloque (bloques completos) — sec. 7-2.
  2. $2^k$ en bloques incompletos mediante **confusión** (2, 4, …, $2^p$ bloques) — secs. 7-3 a 7-6.
  3. **Confusión parcial** (se confunde un efecto distinto en cada réplica) — sec. 7-7.

---

## 7-2 Formación de bloques de un diseño factorial 2^k con réplicas

### Cuándo se usa
Hay $n$ réplicas del $2^k$ y cada conjunto de condiciones no homogéneas (lote, día, turno) alcanza
para una réplica completa. Cada **réplica = un bloque**. Es el diseño factorial en bloques
completos del cap. 5 (sec. 5-6).

### Procedimiento
1. Asignar cada réplica completa del $2^k$ a un bloque.
2. Dentro de cada bloque, correr las $2^k$ combinaciones en **orden aleatorio** (la
   aleatorización está restringida al interior del bloque).

### Modelo *(nota propia, el libro remite a la sec. 5-6)*
Para $2^2$: $y_{ijl} = \mu + \tau_i + \beta_j + (\tau\beta)_{ij} + \delta_l + \varepsilon_{ijl}$,
con $\delta_l$ = efecto del bloque $l$; se supone que no hay interacción bloque × tratamiento
(esa interacción es el error).

### Análisis
- Las SS de todos los efectos factoriales se calculan **exactamente igual** que en el $2^k$ sin
  bloques: $SS_{\text{efecto}} = (\text{contraste})^2/(n2^k)$.
- Suma de cuadrados de bloques a partir de los totales de bloque $B_i$:

$$SS_{\text{Bloques}} = \sum_{i=1}^{n} \frac{B_i^2}{2^k} - \frac{y_{\cdots}^2}{n2^k} \qquad (n-1 \text{ g.l.})$$

- $SS_E = SS_T - SS_{\text{Bloques}} - \sum SS_{\text{efectos}}$, con $(n-1)(2^k-1)$ g.l.
- Los efectos se prueban con $F_0 = MS_{\text{efecto}}/MS_E$. No se calcula $F$ para bloques.

| Fuente | g.l. |
|---|---|
| Bloques | $n-1$ |
| Cada efecto factorial ($2^k-1$ efectos) | 1 |
| Error | $(n-1)(2^k-1)$ |
| Total | $n2^k-1$ |

### Ejemplo 7-1 (proceso químico de la sec. 6-2, $2^2$, $n=3$, tres lotes = tres bloques)
Factores: $A$ = concentración, $B$ = catalizador. Totales de bloque $B_1=113$, $B_2=106$,
$B_3=111$; $y_{\cdots}=330$.
$SS_{\text{Bloques}} = (113^2+106^2+111^2)/4 - 330^2/12 = 6.50$.

Tabla 7-2 (ANOVA):

| Fuente | SS | g.l. | MS | $F_0$ | Valor P |
|---|---|---|---|---|---|
| Bloques | 6.50 | 2 | 3.25 | | |
| $A$ (concentración) | 208.33 | 1 | 208.33 | 50.32 | 0.0004 |
| $B$ (catalizador) | 75.00 | 1 | 75.00 | 18.12 | 0.0053 |
| $AB$ | 8.33 | 1 | 8.33 | 2.01 | 0.2060 |
| Error | 24.84 | 6 | 4.14 | | |
| Total | 323.00 | 11 | | | |

Datos (tabla 7-1): bloque 1: (1)=28, a=36, b=18, ab=31; bloque 2: 25, 32, 19, 30; bloque 3: 27,
32, 23, 29. Conclusión: mismas conclusiones que sin bloques (sec. 6-2); el efecto de bloques es
pequeño.

---

## 7-3 Confusión del diseño factorial 2^k

- **Confusión (o mezclado)**: técnica para distribuir un factorial completo en bloques cuyo
  **tamaño es menor que el número de combinaciones de una réplica** (bloques incompletos).
- Consecuencia: la información de ciertos efectos (normalmente **interacciones de orden
  superior**) queda **indistinguible de los bloques** (confundida con los bloques).
- Aunque son diseños de bloques incompletos, la estructura del $2^k$ permite un análisis
  simplificado.
- Se estudia el $2^k$ en $2^p$ bloques incompletos, $p<k$: 2, 4, 8, … bloques.

---

## 7-4 Confusión del diseño factorial 2^k en dos bloques

### Idea básica ($2^2$ en dos bloques, fig. 7-1)
Una réplica, cada lote alcanza para dos corridas. Asignación: bloque 1 = $\{(1), ab\}$, bloque 2 =
$\{a, b\}$ (diagonales opuestas del cuadrado).

- $A = \tfrac12[ab + a - b - (1)]$ y $B = \tfrac12[ab + b - a - (1)]$: en cada contraste hay una
  combinación con signo $+$ y otra con signo $-$ de **cada bloque**, de modo que cualquier
  diferencia entre bloques se cancela → $A$ y $B$ **no** se afectan.
- $AB = \tfrac12[ab + (1) - a - b]$: las dos con signo $+$ están en el bloque 1 y las dos con signo
  $-$ en el bloque 2 → el contraste de $AB$ es idéntico al de bloques: **$AB$ está confundido con
  los bloques**.

### Método 1: tabla de signos
Elegir el efecto a confundir; las combinaciones con signo $+$ en su columna van a un bloque y las
de signo $-$ al otro. Puede confundirse cualquier efecto (p. ej. $(1), b$ | $a, ab$ confunde $A$),
pero **la práctica usual es confundir la interacción de orden más alto**.

Tabla de signos $2^3$ (tabla 7-4):

| Comb. | $I$ | $A$ | $B$ | $AB$ | $C$ | $AC$ | $BC$ | $ABC$ |
|---|---|---|---|---|---|---|---|---|
| (1) | + | − | − | + | − | + | + | − |
| a | + | + | − | − | − | − | + | + |
| b | + | − | + | − | − | + | − | + |
| ab | + | + | + | + | − | − | − | − |
| c | + | − | − | + | + | − | − | + |
| ac | + | + | − | − | + | + | − | − |
| bc | + | − | + | − | + | − | + | − |
| abc | + | + | + | + | + | + | + | + |

$2^3$ con $ABC$ confundido (fig. 7-2): bloque 1 ($ABC$ −) = $\{(1), ab, ac, bc\}$; bloque 2
($ABC$ +) = $\{a, b, c, abc\}$.

### Método 2: combinación lineal / definición de contrastes (ec. 7-1)

$$L = \alpha_1 x_1 + \alpha_2 x_2 + \cdots + \alpha_k x_k \qquad \text{(7-1)}$$

- $x_i$ = nivel del factor $i$ en la combinación de tratamientos: 0 (bajo) o 1 (alto).
- $\alpha_i$ = exponente del factor $i$ en el efecto que se confunde: 0 o 1.
- Regla: las combinaciones con el **mismo valor de $L \pmod 2$** van al mismo bloque. Como
  $L \bmod 2 \in \{0,1\}$, resultan exactamente dos bloques.

Ejemplo ($2^3$, confundir $ABC$): $L = x_1 + x_2 + x_3$.

| Comb. | $(x_1x_2x_3)$ | $L$ | $L \bmod 2$ | Bloque |
|---|---|---|---|---|
| (1) | 000 | 0 | 0 | 1 |
| a | 100 | 1 | 1 | 2 |
| b | 010 | 1 | 1 | 2 |
| ab | 110 | 2 | 0 | 1 |
| c | 001 | 1 | 1 | 2 |
| ac | 101 | 2 | 0 | 1 |
| bc | 011 | 2 | 0 | 1 |
| abc | 111 | 3 | 1 | 2 |

Mismo diseño que con la tabla de signos.

### Método 3: bloque principal y estructura de grupo
- **Bloque principal**: el bloque que contiene a $(1)$ (el de $L = 0$).
- Sus elementos forman un **grupo respecto a la multiplicación módulo 2** (exponentes mod 2):
  el producto de dos elementos del bloque principal es otro elemento del bloque principal.
  Ej.: $ab\cdot ac = a^2bc = bc$; $ab\cdot bc = ab^2c = ac$; $ac\cdot bc = abc^2 = ab$.
- **Los demás bloques** se obtienen multiplicando (mod 2) un elemento que no esté en el bloque
  principal por cada elemento del bloque principal. Ej.: con $b$:
  $b\cdot(1)=b$, $b\cdot ab = ab^2 = a$, $b\cdot ac = abc$, $b\cdot bc = b^2c = c$ → bloque 2 =
  $\{b, a, abc, c\}$.
- Procedimiento práctico: (i) hallar unos pocos elementos del bloque principal con $L=0$;
  (ii) completar el bloque principal por productos; (iii) generar los otros bloques por
  multiplicación.

### Aleatorización
- Orden de las corridas **dentro** de cada bloque: aleatorio.
- También se decide al azar **cuál bloque se corre primero**.

### Estimación del error
- **$k$ pequeño ($k=2$ o 3)**: normalmente hay que replicar. Si se confunde el mismo efecto en
  todas las réplicas (fig. 7-3: $2^3$, 2 bloques, 4 réplicas, $ABC$ confundido en todas), el ANOVA
  es (tabla 7-5), con 32 observaciones y 8 bloques (7 g.l. entre bloques):

| Fuente | g.l. |
|---|---|
| Réplicas | 3 |
| Bloques ($ABC$) | 1 |
| Error de $ABC$ (réplicas × bloques) | 3 |
| $A$, $B$, $C$, $AB$, $AC$, $BC$ | 1 c/u (6) |
| Error (réplicas × efectos) | 18 |
| Total | 31 |

  - El error (18 g.l.) son las interacciones réplicas × cada uno de los 6 efectos no confundidos;
    se supone que esas interacciones son cero y su MS estima $\sigma^2$.
  - Efectos principales e interacciones de dos factores se prueban contra $MS_E$.
  - Cochran y Cox: el MS de bloques ($ABC$) podría probarse contra el MS del "error de $ABC$"
    (réplicas × bloques), pero con solo 3 g.l. la prueba tiene **muy baja sensibilidad**.
  - Con recursos para replicar, suele ser **mejor confundir un efecto distinto en cada réplica**
    (confusión parcial, sec. 7-7).
- **$k$ moderadamente grande ($k \ge 4$)**: con frecuencia solo hay **una réplica**. Se supone que
  las interacciones de orden superior son despreciables y sus SS se combinan como error; la
  **gráfica de probabilidad normal de los efectos** ayuda a decidir cuáles.

### Análisis (una réplica en dos bloques)
- Estimar todos los efectos y SS como en un $2^k$ sin bloques.
- La estimación del efecto confundido es en realidad **Bloques + efecto**; su SS es
  $SS_{\text{Bloques}}$ (1 g.l.).
- Efecto de bloque directo: $\bar y_{\text{Bloque 1}} - \bar y_{\text{Bloque 2}}$ (el signo depende de
  qué bloque tenga el signo $+$ del efecto confundido).
- $SS_{\text{Bloques}} = \dfrac{B_1^2 + B_2^2}{2^{k-1}} - \dfrac{y_{\cdots}^2}{2^k}$.

### Ejemplo 7-2 (índice de filtración, $2^4$ no replicado en dos bloques)
Contexto: ejemplo 6-2 ($A$ = temperatura, $B$ = presión, $C$ = concentración de formaldehído,
$D$ = velocidad de agitación; respuesta: índice de filtración). Modificaciones: (i) un lote solo
alcanza para 8 corridas → $2^4$ en 2 bloques con $ABCD$ confundido, $L = x_1+x_2+x_3+x_4$;
(ii) se simula un efecto de bloque: en el lote de mala calidad (bloque 1) todas las respuestas
son **20 unidades menores**.

- Bloque 1 ($L=0$; $ABCD$ +): (1)=25, ab=45, ac=40, bc=60, ad=80, bd=25, cd=55, abcd=76 (total 406).
- Bloque 2 ($L=1$; $ABCD$ −): a=71, b=48, c=68, d=43, abc=65, bcd=70, acd=86, abd=104 (total 555).

Tabla 7-6 (estimaciones):

| Término | Coef. regresión | Efecto | SS | % contribución |
|---|---|---|---|---|
| $A$ | 10.81 | 21.625 | 1870.5625 | 26.30 |
| $B$ | 1.56 | 3.125 | 39.0625 | 0.55 |
| $C$ | 4.94 | 9.875 | 390.0625 | 5.49 |
| $D$ | 7.31 | 14.625 | 855.5625 | 12.03 |
| $AB$ | 0.062 | 0.125 | 0.0625 | <0.01 |
| $AC$ | −9.06 | −18.125 | 1314.0625 | 18.48 |
| $AD$ | 8.31 | 16.625 | 1105.5625 | 15.55 |
| $BC$ | 1.19 | 2.375 | 22.5625 | 0.32 |
| $BD$ | −0.19 | −0.375 | 0.5625 | <0.01 |
| $CD$ | −0.56 | −1.125 | 5.0625 | 0.07 |
| $ABC$ | 0.94 | 1.875 | 14.0625 | 0.20 |
| $ABD$ | 2.06 | 4.125 | 68.0625 | 0.96 |
| $ACD$ | −0.81 | −1.625 | 10.5625 | 0.15 |
| $BCD$ | −1.31 | −2.625 | 27.5625 | 0.39 |
| Bloques ($ABCD$) | | −18.625 | 1387.5625 | 19.51 |

- Los 14 efectos no confundidos son **idénticos** a los del ejemplo 6-2 (sin efecto de bloque).
- $ABCD$ estimado $= 1.375$ (interacción original) $+ (-20)$ (bloque) $= -18.625$.
  Directamente: $406/8 - 555/8 = -149/8 = -18.625$.
- $SS_{\text{Bloques}} = (406^2 + 555^2)/8 - 961^2/16 = 1387.5625$.
- Gráfica de probabilidad normal: importantes $A$, $C$, $D$, $AC$, $AD$ (igual que en 6-2).

Tabla 7-7 (ANOVA del modelo reducido):

| Fuente | SS | g.l. | MS | $F_0$ | Valor P |
|---|---|---|---|---|---|
| Bloques ($ABCD$) | 1387.5625 | 1 | | | |
| $A$ | 1870.5625 | 1 | 1870.5625 | 89.76 | <0.0001 |
| $C$ | 390.0625 | 1 | 390.0625 | 18.72 | 0.0019 |
| $D$ | 855.5625 | 1 | 855.5625 | 41.05 | 0.0001 |
| $AC$ | 1314.0625 | 1 | 1314.0625 | 63.05 | <0.0001 |
| $AD$ | 1105.5625 | 1 | 1105.5625 | 53.05 | <0.0001 |
| Error | 187.5625 | 9 | 20.8403 | | |
| Total | 7111.4375 | 15 | | | |

Lección: si no se hubieran formado bloques y el desplazamiento de −20 hubiera afectado 8 corridas
elegidas al azar (orden completamente aleatorio), los resultados podrían haber sido muy distintos.

---

## 7-5 Confusión del diseño factorial 2^k en cuatro bloques

### Cuándo se usa
$k$ moderadamente grande ($k \ge 4$) y bloques pequeños: 4 bloques de $2^{k-2}$ corridas.

### Construcción
1. Elegir **dos** efectos a confundir (generadores), con sus definiciones de contrastes $L_1$ y $L_2$.
2. Cada combinación produce un par $(L_1, L_2) \pmod 2 \in \{(0,0),(1,0),(0,1),(1,1)\}$; las
   combinaciones con el mismo par van al mismo bloque.
3. Entre 4 bloques hay 3 g.l. → se confunde automáticamente un **tercer efecto**: la
   **interacción generalizada** de los dos elegidos = su producto módulo 2.

### Ejemplo en el texto: $2^5$ en 4 bloques de 8 con $ADE$ y $BCE$
$L_1 = x_1 + x_4 + x_5$, $L_2 = x_2 + x_3 + x_5$. Interacción generalizada:
$(ADE)(BCE) = ABCDE^2 = ABCD$ (también confundida).

| Bloque | $(L_1,L_2)$ | Combinaciones (fig. 7-5) | Signo $ADE$ | Signo $BCE$ | Signo $ABCD$ |
|---|---|---|---|---|---|
| 1 (principal) | (0,0) | (1), ad, bc, abcd, abe, ace, cde, bde | − | − | + |
| 2 | (1,0) | a, d, abc, bcd, be, abde, ce, acde | + | − | − |
| 3 | (0,1) | b, abd, c, acd, ae, de, abce, bcde | − | + | − |
| 4 | (1,1) | e, ade, bce, abcde, ab, bd, ac, cd | + | + | + |

- En cada bloque el producto de los signos de dos de los efectos confundidos da el signo del
  tercero.
- Siguen valiendo las propiedades de grupo del bloque principal: $ad\cdot bc = abcd$;
  $abe\cdot bde = ab^2de^2 = ad$. Otro bloque: multiplicar por un elemento externo, p. ej. $b$:
  $b\cdot(1)=b$, $b\cdot ad = abd$, $b\cdot bc = c$, $b\cdot abcd = acd$, … (bloque 3).

### Regla para elegir los generadores
Cuidar que la interacción generalizada no sea un efecto de interés. Contraejemplo: en $2^5$,
confundir $ABCDE$ y $ABD$ confunde automáticamente $CE$ (dos factores). Mejor $ADE$ y $BCE$
→ $ABCD$: se sacrifican dos interacciones de tres factores y una de cuatro, no una de dos.

---

## 7-6 Confusión del diseño factorial 2^k en 2^p bloques

### Construcción general
- $2^k$ en $2^p$ bloques ($p<k$), cada uno con $2^{k-p}$ corridas.
- Elegir **$p$ efectos independientes** (ninguno es interacción generalizada de los otros) con
  definiciones de contrastes $L_1, \dots, L_p$; los bloques son las clases de
  $(L_1,\dots,L_p) \pmod 2$.
- Quedan confundidos además otros $2^p - p - 1$ efectos: todas las interacciones generalizadas
  de los $p$ elegidos. Total confundido: $2^p - 1$ efectos (= g.l. entre bloques).
- La elección de los $p$ generadores es crítica: determina toda la estructura de confusión.

### Análisis
1. Calcular las SS de todos los efectos como si no hubiera bloques.
2. $SS_{\text{Bloques}}$ = suma de las SS de todos los efectos confundidos con los bloques
   ($2^p-1$ g.l.) [equivalentemente, a partir de los totales de bloque].
3. Error: réplicas, o interacciones de orden alto no confundidas supuestas despreciables.

### Ejemplo en el texto: $2^6$ en 8 bloques de 8
Generadores (tabla 7-8): $ABEF$, $ABCD$, $ACE$. Interacciones generalizadas ($2^3-3-1=4$):

- $(ABEF)(ABCD) = A^2B^2CDEF = CDEF$
- $(ABEF)(ACE) = A^2BCE^2F = BCF$
- $(ABCD)(ACE) = A^2BC^2ED = BDE$
- $(ABEF)(ABCD)(ACE) = A^3B^2C^2DE^2F = ADF$

### Tabla 7-8 — Disposiciones de bloques sugeridas para el $2^k$

(Los conjuntos de efectos confundidos fueron verificados calculando las interacciones
generalizadas de los generadores; la tabla del libro está impresa girada.)

| $k$ | N.º de bloques $2^p$ | Tamaño de bloque $2^{k-p}$ | Efectos elegidos para generar los bloques | Interacciones confundidas con los bloques |
|---|---|---|---|---|
| 3 | 2 | 4 | $ABC$ | $ABC$ |
| 3 | 4 | 2 | $AB, AC$ | $AB, AC, BC$ |
| 4 | 2 | 8 | $ABCD$ | $ABCD$ |
| 4 | 4 | 4 | $ABC, ACD$ | $ABC, ACD, BD$ |
| 4 | 8 | 2 | $AB, BC, CD$ | $AB, BC, CD, AC, BD, AD, ABCD$ |
| 5 | 2 | 16 | $ABCDE$ | $ABCDE$ |
| 5 | 4 | 8 | $ABC, CDE$ | $ABC, CDE, ABDE$ |
| 5 | 8 | 4 | $ABE, BCE, CDE$ | $ABE, BCE, CDE, AC, ABCD, BD, ADE$ |
| 5 | 16 | 2 | $AB, AC, CD, DE$ | Todas las interacciones de dos y de cuatro factores (15 efectos) |
| 6 | 2 | 32 | $ABCDEF$ | $ABCDEF$ |
| 6 | 4 | 16 | $ABCF, CDEF$ | $ABCF, CDEF, ABDE$ |
| 6 | 8 | 8 | $ABEF, ABCD, ACE$ | $ABEF, ABCD, ACE, BCF, BDE, CDEF, ADF$ |
| 6 | 16 | 4 | $ABF, ACF, BDF, DEF$ | $ABF, ACF, BDF, DEF, BC, ABCD, ABDE, AD, ACDE, CE, CDF, BCDEF, ABCEF, AEF, BE$ |
| 6 | 32 | 2 | $AB, BC, CD, DE, EF$ | Todas las interacciones de dos, cuatro y seis factores (31 efectos) |
| 7 | 2 | 64 | $ABCDEFG$ | $ABCDEFG$ |
| 7 | 4 | 32 | $ABCFG, CDEFG$ | $ABCFG, CDEFG, ABDE$ |
| 7 | 8 | 16 | $ABC, DEF, AFG$ | $ABC, DEF, AFG, ABCDEF, BCFG, ADEG, BCDEG$ |
| 7 | 16 | 8 | $ABCD, EFG, CDE, ADG$ | $ABCD, EFG, CDE, ADG, ABCDEFG, ABE, BCG, CDFG, ADEF, ACEG, ABFG, BCEF, BDEG, ACF, BDF$ |
| 7 | 32 | 4 | $ABG, BCG, CDG, DEG, EFG$ | $ABG, BCG, CDG, DEG, EFG, AC, BD, CE, DF, AE, BF, ABCD, ABDE, ABEF, BCDE, BCEF, CDEF, ABCDEFG, ADG, ACDEG, ACEFG, ABDFG, ABCEG, BEG, BDEFG, CFG, ADEF, ACDF, ABCF, AFG, BCDFG$ |
| 7 | 64 | 2 | $AB, BC, CD, DE, EF, FG$ | Todas las interacciones de dos, cuatro y seis factores (63 efectos) |

Notas de lectura de la tabla 7-8:
- Fila $k=6$, 16 bloques: en la imagen el undécimo efecto parece leerse "BDF" repetido; por
  cálculo debe ser $CDF$ (dudoso en la impresión, pág. 298).
- Fila $k=7$, 32 bloques: en la imagen se leen 30 efectos; el conjunto completo calculado tiene
  31 (el que no se alcanzó a leer es $BCDFG$) (dudoso, pág. 298).

---

## 7-7 Confusión parcial

### Motivación
- Sin estimación previa del error ni disposición a despreciar interacciones, hay que replicar.
- **Confusión completa**: el mismo efecto se confunde en todas las réplicas (fig. 7-3, tabla 7-5)
  → **no hay información alguna** sobre ese efecto.
- **Confusión parcial**: en cada réplica se confunde un efecto **diferente**; cada efecto
  confundido se estima con las réplicas en las que **no** está confundido.

### Ejemplo de esquema (fig. 7-6): $2^3$, 4 réplicas, 2 bloques por réplica

| Réplica | Confundido | Bloque 1 | Bloque 2 |
|---|---|---|---|
| I | $ABC$ | (1), ab, ac, bc | a, b, c, abc |
| II | $AB$ | (1), c, ab, abc | a, b, ac, bc |
| III | $BC$ | (1), a, bc, abc | b, c, ab, ac |
| IV | $AC$ | (1), b, ac, abc | a, c, ab, bc |

- $ABC$ se estima con las réplicas II, III, IV; $AB$ con I, III, IV; $AC$ con I, II, III; $BC$ con
  I, II, IV.
- **Información relativa de los efectos confundidos** (Yates): fracción de réplicas donde el
  efecto no está confundido; aquí **3/4** para cada interacción. Los efectos principales tienen
  información completa.

### Análisis (tabla 7-9)

| Fuente | g.l. |
|---|---|
| Réplicas | 3 |
| Bloques dentro de réplicas [$ABC$ (rép. I) + $AB$ (rép. II) + $BC$ (rép. III) + $AC$ (rép. IV)] | 4 |
| $A$ | 1 |
| $B$ | 1 |
| $C$ | 1 |
| $AB$ (de las réplicas I, III y IV) | 1 |
| $AC$ (de las réplicas I, II y III) | 1 |
| $BC$ (de las réplicas I, II y IV) | 1 |
| $ABC$ (de las réplicas II, III y IV) | 1 |
| Error | 17 |
| Total | 31 |

(En la tabla 7-9 impresa la fila de $ABC$ dice "réplicas I, III y IV"; por el texto de la
pág. 299 y la fig. 7-6 debe ser II, III y IV — errata aparente, pág. 300.)

Reglas de cálculo:
- **Efectos nunca confundidos**: SS usual con todas las observaciones,
  $SS = (\text{contraste})^2/(n2^k)$.
- **Efecto parcialmente confundido**: SS (y estimación) usando **solo las réplicas donde no está
  confundido**: $SS = (\text{contraste en esas réplicas})^2/(n'2^k)$, $n'$ = número de esas réplicas.
- **Réplicas**: $SS_{\text{Rep}} = \sum_{h=1}^{n} \dfrac{R_h^2}{2^k} - \dfrac{y_{\cdots}^2}{N}$, con
  $R_h$ = total de la réplica $h$; $n-1$ g.l.
- **Bloques dentro de réplicas**: suma, sobre las réplicas, de la SS del efecto confundido en
  cada réplica calculada con los datos de esa réplica (1 g.l. por réplica cuando hay 2 bloques por
  réplica). Los $(\text{n.º bloques}-1)$ g.l. entre bloques se parten en réplicas + bloques dentro
  de réplicas (7 = 3 + 4 en el ejemplo).
- **Error**: réplicas × efectos principales, más réplicas × interacción solo sobre las réplicas en
  que esa interacción no está confundida (p. ej. réplicas × $ABC$ en II, III, IV). En la práctica
  por diferencia.

### Ejemplo 7-3 (un $2^3$ con confusión parcial)
Contexto: ejemplo 6-1 (bebida carbonatada; $A$ = % carbonatación, $B$ = presión de operación,
$C$ = velocidad de línea; respuesta = desviación de altura de llenado). Cada lote de jarabe
alcanza para 4 corridas → 2 bloques por réplica; 2 réplicas: **$ABC$ confundido en la réplica I,
$AB$ en la réplica II**.

Datos:
- Réplica I: bloque 1: (1)=−3, ab=2, ac=2, bc=1; bloque 2: a=0, b=−1, c=−1, abc=6. ($R_1=6$)
- Réplica II: bloque 1: (1)=−1, c=0, ab=3, abc=5; bloque 2: a=1, b=0, ac=1, bc=1. ($R_2=10$)

Cálculos:
- $SS_A$, $SS_B$, $SS_C$, $SS_{AC}$, $SS_{BC}$: forma usual con las 16 observaciones.
- $SS_{ABC}$ solo con la réplica II:
  $[a+b+c+abc-ab-ac-bc-(1)]^2/(1\cdot 8) = [1+0+0+5-3-1-1-(-1)]^2/8 = 0.50$.
- $SS_{AB}$ solo con la réplica I:
  $[(1)+abc-ac+c-a-b+ab-bc]^2/(1\cdot 8) = [-3+6-2+(-1)-0-(-1)+2-1]^2/8 = 0.50$.
- $SS_{\text{Rep}} = (6^2+10^2)/8 - 16^2/16 = 1.00$.
- $SS_{\text{Bloques(réplicas)}} = SS_{ABC}(\text{rép. I}) + SS_{AB}(\text{rép. II}) = 2.50$.

Tabla 7-10 (ANOVA):

| Fuente | SS | g.l. | MS | $F_0$ | Valor P |
|---|---|---|---|---|---|
| Réplicas | 1.00 | 1 | 1.00 | — | |
| Bloques dentro de réplicas | 2.50 | 2 | 1.25 | — | |
| $A$ | 36.00 | 1 | 36.00 | 48.00 | 0.0001 |
| $B$ | 20.25 | 1 | 20.25 | 27.00 | 0.0035 |
| $C$ | 12.25 | 1 | 12.25 | 16.33 | 0.0099 |
| $AB$ (solo réplica I) | 0.50 | 1 | 0.50 | 0.67 | 0.4503 |
| $AC$ | 0.25 | 1 | 0.25 | 0.33 | 0.5905 |
| $BC$ | 1.00 | 1 | 1.00 | 1.33 | 0.3009 |
| $ABC$ (solo réplica II) | 0.50 | 1 | 0.50 | 0.67 | 0.4503 |
| Error | 3.75 | 5 | 0.75 | — | |
| Total | 78.00 | 15 | | | |

Conclusión: los tres efectos principales son significativos; ninguna interacción lo es.

---

## Resumen operativo (reglas y advertencias del capítulo)

1. **Réplicas completas caben en un bloque** → cada réplica es un bloque; ANOVA usual más una
   fila de bloques ($n-1$ g.l.).
2. **La réplica no cabe en un bloque** → confusión en $2^p$ bloques: elegir $p$ efectos
   independientes, asignar por $(L_1,\dots,L_p) \bmod 2$; se confunden $2^p-1$ efectos (los $p$
   más sus interacciones generalizadas).
3. Confundir siempre **interacciones del orden más alto posible** y revisar las **interacciones
   generalizadas** para no perder efectos principales ni interacciones de dos factores de interés.
   Usar la tabla 7-8.
4. El bloque principal ($L_i=0$ para todo $i$, contiene a $(1)$) es un **grupo** bajo
   multiplicación mod 2; los demás bloques son sus "clases laterales" (multiplicar por un elemento
   externo).
5. Aleatorizar el orden de corridas dentro de cada bloque y el orden de los bloques.
6. Efectos no confundidos: estimaciones y SS **idénticas** a las del diseño sin bloques; el efecto
   de bloques no los contamina (ejemplo 7-2).
7. El efecto confundido estima **efecto + bloques**; no se puede separar ni probar (salvo la
   prueba de baja sensibilidad contra réplicas × bloques cuando hay réplicas).
8. Una sola réplica: error a partir de interacciones de orden alto no confundidas + gráfica de
   probabilidad normal de los efectos.
9. Con réplicas: preferir **confusión parcial**; cada efecto confundido se analiza solo con las
   réplicas donde está libre, con información relativa = (réplicas libres)/(réplicas totales).

## 7-8 Problemas
Problemas 7-1 a 7-17 (págs. 301–302): reanálisis de experimentos del cap. 6 en bloques por
réplica (7-1 a 7-3), construcción y análisis de $2^3$, $2^4$, $2^5$, $2^6$ confundidos en 2, 4 y 8
bloques (7-4 a 7-11), demostración de $SS_{AB}=SS_{\text{Bloques}}$ en el $2^2$ (7-12), variaciones
del ejemplo 7-2 (7-13) y confusión parcial/completa (7-14 a 7-17).
