# Capítulo 9 — Diseños factoriales y factoriales fraccionados con tres niveles y con niveles mixtos

> Montgomery, págs. 363–391

Convenciones de esta ficha: $k$ = número de factores, $n$ = réplicas, niveles codificados 0, 1, 2
(bajo, intermedio, alto), toda la aritmética de exponentes y de definiciones de contrastes es
**módulo 3**. Las anotaciones *(nota propia)* no están en el libro. Las listas de bloques, alias
e interacciones generalizadas fueron verificadas por cálculo.

---

## 9-1 Diseño factorial 3^k

### 9-1.1 Notación y motivación del diseño 3^k

- **Diseño $3^k$**: arreglo factorial de $k$ factores con tres niveles cada uno.
- **Notación digital**: cada combinación de tratamientos son $k$ dígitos; el primero es el nivel
  de $A$, el segundo el de $B$, etc. En un $3^2$: `00` = $A$ y $B$ bajos; `01` = $A$ bajo, $B$
  intermedio. En un $3^4$: `0120` = $A$ y $D$ bajos, $B$ intermedio, $C$ alto.
- En el $2^k$ se prefirió $\pm1$ porque facilita la vista geométrica, la regresión, los bloques y
  las fracciones; la notación 0/1 habría sido equivalente.
- **Factores cuantitativos**: suele codificarse −1, 0, +1, lo que facilita ajustar el modelo de
  regresión de segundo orden. Para $3^2$ (ec. 9-1):

$$y = \beta_0 + \beta_1x_1 + \beta_2x_2 + \beta_{12}x_1x_2 + \beta_{11}x_1^2 + \beta_{22}x_2^2 + \varepsilon \qquad \text{(9-1)}$$

- El tercer nivel permite modelar **curvatura** (relación cuadrática).

**Advertencias del autor** (cuándo NO usar el $3^k$):
1. El $3^k$ **no es la forma más eficiente** de modelar una relación cuadrática; los **diseños de
   superficie de respuesta** (cap. 11) son alternativas superiores.
2. El $2^k$ **con puntos centrales** (cap. 6) da indicación y protección contra la curvatura con un
   diseño pequeño y simple; si la curvatura resulta importante se agregan **corridas axiales**
   para formar un **diseño central compuesto** (fig. 6-36). Esta **estrategia secuencial** es mucho
   más eficiente que correr un $3^k$ con factores cuantitativos.

Uso típico razonable del $3^k$: cuando uno o más factores son **cualitativos** con tres niveles
de interés (ejemplo 9-1).

### 9-1.2 El diseño 3^2

**Grados de libertad**: 9 combinaciones → 8 g.l.; $A$: 2, $B$: 2, $AB$: 4. Con $n$ réplicas:
$n3^2-1$ totales y $3^2(n-1)$ del error.

| Fuente | g.l. |
|---|---|
| $A$ | 2 |
| $B$ | 2 |
| $AB$ | 4 |
| Error | $9(n-1)$ |
| Total | $9n-1$ |

SS de $A$, $B$, $AB$: métodos usuales de factoriales (cap. 5).

**Partición de los efectos principales** (solo con sentido si el factor es **cuantitativo**):
componente **lineal** ($A_L$) y **cuadrático** ($A_Q$), 1 g.l. cada uno (corresponden a
$\beta_1x_1$ y $\beta_{11}x_1^2$ de la ec. 9-1).

**Partición de la interacción $AB$ (4 g.l.) — dos maneras:**

**Método 1: componentes de un solo g.l.** $AB_{L\times L}$, $AB_{L\times Q}$, $AB_{Q\times L}$,
$AB_{Q\times Q}$, obtenidos ajustando los términos $\beta_{12}x_1x_2$, $\beta_{122}x_1x_2^2$,
$\beta_{112}x_1^2x_2$, $\beta_{1122}x_1^2x_2^2$. Con los datos de la vida de la herramienta
(ejemplo 5-5): $SS_{AB_{L\times L}} = 8.00$, $SS_{AB_{L\times Q}} = 42.67$,
$SS_{AB_{Q\times L}} = 2.67$, $SS_{AB_{Q\times Q}} = 8.00$; suma $= SS_{AB} = 61.34$ (partición
ortogonal).

**Método 2: cuadrados latinos ortogonales → componentes $AB$ y $AB^2$ (2 g.l. cada uno).**
Se superponen dos cuadrados latinos ortogonales $3\times3$ sobre la tabla de totales de celda
($A$ = renglones, $B$ = columnas). Las letras ocupan las celdas según:

| | Cuadrado *a* (componente $AB$) | Cuadrado *b* (componente $AB^2$) |
|---|---|---|
| $Q$ | $x_1 + x_2 = 0 \pmod 3$ | $x_1 + 2x_2 = 0 \pmod 3$ |
| $R$ | $x_1 + x_2 = 1 \pmod 3$ | $x_1 + 2x_2 = 2 \pmod 3$ |
| $S$ | $x_1 + x_2 = 2 \pmod 3$ | $x_1 + 2x_2 = 1 \pmod 3$ |

Cálculo: sumar los totales de celda por letra y obtener la SS entre los tres totales de letra:

$$SS_{\text{componente}} = \frac{T_Q^2 + T_R^2 + T_S^2}{3n} - \frac{y_{\cdots}^2}{9n} \qquad (2 \text{ g.l.})$$

Ejemplo (totales de celda del ej. 5-5, $n=2$; filas $A$=0,1,2; columnas $B$=0,1,2:
$(-3,-3,5)$, $(2,4,10)$, $(-1,11,-1)$; $y_{\cdots}=24$):
- Cuadrado *a*: $Q=18$, $R=-2$, $S=8$ → $[18^2+(-2)^2+8^2]/(3)(2) - 24^2/(9)(2) = 33.34$ → **componente $AB$**.
- Cuadrado *b*: $Q=0$, $R=6$, $S=18$ → $[0^2+6^2+18^2]/(3)(2) - 24^2/(9)(2) = 28.00$ → **componente $AB^2$**.
- $33.34 + 28.00 = 61.34 = SS_{AB}$ (2 + 2 = 4 g.l.).

**Cálculo equivalente por diagonales** de la tabla de totales (con extensión cíclica):
- Diagonales "hacia abajo de izquierda a derecha": totales $0, 6, 18$ → SS = 28.00 ($AB^2$).
- Diagonales "hacia abajo de derecha a izquierda": totales $8, -2, 18$ → SS = 33.34 ($AB$).

**Notación de Yates** — componentes $I$ y $J$ de la interacción:

$$I(AB) = AB^2, \qquad J(AB) = AB$$

**Convención de exponentes** para $A^pB^q$: el **único exponente permitido en la primera letra es
1**. Si no lo es, se eleva toda la expresión al cuadrado y se reducen los exponentes módulo 3:
$A^2B = (A^2B)^2 = A^4B^2 = AB^2$.

**Advertencias**:
- Los componentes $AB$ y $AB^2$ **no tienen significado físico** y normalmente **no se incluyen en
  la tabla ANOVA**; son una partición en gran medida arbitraria, pero **muy útil para construir
  diseños** (confusión y fracciones).
- **No hay relación** entre los componentes $AB$, $AB^2$ y los componentes $L\times L$, $L\times Q$,
  $Q\times L$, $Q\times Q$.

### 9-1.3 El diseño 3^3

**Grados de libertad**: 27 combinaciones → 26 g.l. Con $n$ réplicas: $n3^3-1$ totales,
$3^3(n-1)$ del error.

| Fuente | g.l. |
|---|---|
| $A$, $B$, $C$ | 2 c/u |
| $AB$, $AC$, $BC$ | 4 c/u |
| $ABC$ | 8 |
| Error | $27(n-1)$ |
| Total | $27n-1$ |

Particiones posibles:
- Efectos principales (cuantitativos): lineal y cuadrático, 1 g.l. c/u.
- Interacciones de dos factores: $L\times L$, $L\times Q$, $Q\times L$, $Q\times Q$ (1 g.l. c/u), o
  bien componentes $I$ y $J$: $AB, AB^2, AC, AC^2, BC, BC^2$ (2 g.l. c/u, sin significado físico).
- $ABC$: 8 componentes de 1 g.l. ($L\times L\times L$, $L\times L\times Q$, …; en general de poca
  utilidad), o bien **cuatro componentes ortogonales de 2 g.l.** (componentes $W, X, Y, Z$):

$$W(ABC) = AB^2C^2,\quad X(ABC) = AB^2C,\quad Y(ABC) = ABC^2,\quad Z(ABC) = ABC$$

  (la primera letra siempre con exponente 1). Sin interpretación práctica; útiles para construir
  diseños.

**Cálculo numérico de $W, X, Y, Z$** (procedimiento de Cochran y Cox / Davies, pág. 370):
1. Elegir dos factores (p. ej. $A$, $B$) y calcular los totales $I(AB)$ y $J(AB)$ (tres totales
   cada uno) **en cada nivel de $C$**.
2. Formar una tabla de dos vías $C \times I(AB)$ y otra $C \times J(AB)$ (3×3 cada una) y calcular
   en cada una los totales de las diagonales $I$ y $J$.
3. Esos totales corresponden a: $I[I(AB)\times C] = AB^2C^2 = W$; $J[I(AB)\times C] = AB^2C = X$;
   $I[J(AB)\times C] = ABC^2 = Y$; $J[J(AB)\times C] = ABC = Z$.
4. $SS = \sum(\text{totales})^2/(9n) - y_{\cdots}^2/(27n)$, 2 g.l. cada uno.

### Ejemplo 9-1 (pérdida de jarabe por espumeo, $3^3$, $n=2$)
Contexto: máquina que llena contenedores de 5 galones con jarabe. Factores: $A$ = tipo de
boquilla (1, 2, 3; **cualitativo**), $B$ = velocidad de llenado (100, 120, 140 rpm), $C$ = presión
de operación (10, 15, 20 psi). Respuesta: pérdida de jarabe (cm³ − 70). 54 observaciones.

Tabla 9-2 (ANOVA):

| Fuente | SS | g.l. | MS | $F_0$ | Valor P |
|---|---|---|---|---|---|
| $A$, boquilla | 993.77 | 2 | 496.89 | 1.17 | 0.3256 |
| $B$, velocidad | 61,190.33 | 2 | 30,595.17 | 71.74 | <0.0001 |
| $C$, presión | 69,105.33 | 2 | 34,552.67 | 81.01 | <0.0001 |
| $AB$ | 6,300.90 | 4 | 1,575.22 | 3.69 | 0.0383 |
| $AC$ | 7,513.90 | 4 | 1,878.47 | 4.40 | 0.0222 |
| $BC$ | 12,854.34 | 4 | 3,213.58 | 7.53 | 0.0025 |
| $ABC$ | 4,628.76 | 8 | 578.60 | 1.36 | 0.2737 |
| Error | 11,515.50 | 27 | 426.50 | | |
| Total | 174,102.83 | 53 | | | |

Conclusiones: velocidad y presión significativas; las tres interacciones de dos factores
significativas (fig. 9-4). El nivel intermedio de velocidad (120 rpm) da el mejor desempeño; las
boquillas 2 y 3 y la presión baja (10 psi) o alta (20 psi) reducen la pérdida.

**Modelos de regresión cuadráticos por boquilla** (tabla 9-3; $x_1$ = velocidad $S$, $x_2$ = presión
$P$; codificación −1, 0, +1 ↔ 100, 120, 140 rpm y 10, 15, 20 psi):

| Boquilla | Modelo |
|---|---|
| 1 | $\hat y = 22.1 + 3.5x_1 + 16.3x_2 + 51.7x_1^2 - 71.8x_2^2 + 2.9x_1x_2$ |
| 1 | $\hat y = 1217.3 - 31.256S + 86.017P + 0.12917S^2 - 2.8733P^2 + 0.02875SP$ |
| 2 | $\hat y = 25.6 - 22.8x_1 - 12.3x_2 + 14.1x_1^2 - 56.9x_2^2 - 0.7x_1x_2$ |
| 2 | $\hat y = 180.1 - 9.475S + 66.75P + 0.035S^2 - 2.2767P^2 - 0.0075SP$ |
| 3 | $\hat y = 15.1 + 20.3x_1 + 5.9x_2 + 75.8x_1^2 - 94.9x_2^2 + 10.5x_1x_2$ |
| 3 | $\hat y = 1940.1 - 40.058S + 102.48P + 0.18958S^2 - 3.7967P^2 + 0.105SP$ |

Gráficas de contorno (fig. 9-5): se prefiere la **boquilla 3** (únicos contornos de −60), velocidad
cerca de 120 rpm y presión baja o alta. Advertencia: con mezcla de factores cuantitativos y
cualitativos, la forma de la superficie de respuesta puede ser muy distinta en cada nivel del
factor cualitativo (la de la boquilla 2 es más alargada), así que las condiciones óptimas difieren
por nivel.

**Partición de $ABC$ en el ejemplo 9-1** (totales $I$, $J$ de $AB$ por nivel de $C$):

| $C$ | $I(AB)$ (tres totales) | $J(AB)$ (tres totales) |
|---|---|---|
| 10 | −198, −106, −155 | −222, −79, −158 |
| 15 | 331, 255, 377 | 238, 440, 285 |
| 20 | −59, −74, −206 | −144, −40, −155 |

Totales de diagonales: de $C\times I(AB)$: $I$: −149, 212, 102; $J$: 41, 19, 105. De
$C\times J(AB)$: $I$: 63, 62, 40; $J$: 138, 4, 23. Gran total 165.

- $W = AB^2C^2$: $[(-149)^2+212^2+102^2]/18 - 165^2/54 = 3804.11$
- $X = AB^2C$: $[41^2+19^2+105^2]/18 - 165^2/54 = 221.77$
- $Y = ABC^2$: $[63^2+62^2+40^2]/18 - 165^2/54 = 18.77$
- $Z = ABC$: $[138^2+4^2+23^2]/18 - 165^2/54 = 584.11$
- Suma $= 4628.76 = SS_{ABC}$. No se acostumbra presentarla en el ANOVA.

### 9-1.4 El diseño general 3^k

- $3^k$ combinaciones, $3^k-1$ g.l.; con $n$ réplicas: $n3^k-1$ totales y $3^k(n-1)$ del error.
- $k$ efectos principales (2 g.l. c/u); $\binom{k}{2}$ interacciones de dos factores (4 g.l. c/u);
  …; una interacción de $k$ factores con $2^k$ g.l. **Una interacción de $h$ factores tiene $2^h$
  g.l.** y $2^{h-1}$ **componentes ortogonales de 2 g.l.**
- Ejemplo: $ABCD$ tiene $2^{4-1}=8$ componentes: $ABCD^2$, $ABC^2D$, $AB^2CD$, $ABCD$, $ABC^2D^2$,
  $AB^2C^2D$, $AB^2CD^2$, $AB^2C^2D^2$. Misma convención de exponentes:
  $A^2BCD = (A^2BCD)^2 = A^4B^2C^2D^2 = AB^2C^2D^2$.
- SS por los métodos usuales; normalmente no se descomponen las interacciones de tres o más
  factores.
- **Tamaño**: $3^3=27$, $3^4=81$, $3^5=243$ corridas por réplica. Suele correrse **una sola
  réplica** y combinar interacciones de orden superior como error: si las de tres o más factores
  son despreciables, una réplica del $3^3$ da 8 g.l. de error y una del $3^4$ da 48 g.l.
- Aun así son diseños grandes para $k\ge3$ → **escasa utilidad**.

---

## 9-2 Confusión en el diseño factorial 3^k

El $3^k$ puede confundirse en $3^p$ bloques incompletos ($p<k$): 3, 9, 27, … bloques.

### 9-2.1 El diseño factorial 3^k en tres bloques

- 3 bloques → 2 g.l. entre bloques → se confunde **un componente de interacción de 2 g.l.**
  (p. ej. $AB$ o $AB^2$; $ABC$, $ABC^2$, $AB^2C$ o $AB^2C^2$).
- **Definición de contrastes** (ec. 9-2):

$$L = \alpha_1x_1 + \alpha_2x_2 + \cdots + \alpha_kx_k \qquad \text{(9-2)}$$

  con $\alpha_i \in\{0,1,2\}$ = exponente del factor $i$ en el componente a confundir (la primera
  $\alpha_i$ no nula es 1) y $x_i\in\{0,1,2\}$ = nivel del factor $i$.
- Las combinaciones se asignan a bloques según **$L \pmod 3$** = 0, 1, 2 (tres bloques únicos).
- **Bloque principal**: $L = 0 \pmod 3$; siempre contiene a $00\ldots0$.
- **Estructura de grupo**: los elementos del bloque principal forman un grupo respecto a la
  **adición módulo 3** (dígito a dígito). Los otros bloques se generan **sumando** (mod 3) un
  elemento que no esté en el bloque principal a cada elemento del bloque principal.

**Ejemplo: $3^2$ en 3 bloques con $AB^2$ confundido** ($L = x_1 + 2x_2$, fig. 9-6):

| Comb. | 00 | 01 | 02 | 10 | 11 | 12 | 20 | 21 | 22 |
|---|---|---|---|---|---|---|---|---|---|
| $L \bmod 3$ | 0 | 2 | 1 | 1 | 0 | 2 | 2 | 1 | 0 |

- Bloque 1 (principal, $L=0$): 00, 11, 22. (11 + 11 = 22; 11 + 22 = 00.)
- Bloque 2 ($L=1$): 10, 21, 02 (10 + 00, 10 + 11, 10 + 22).
- Bloque 3 ($L=2$): 01, 12, 20 (01 + 00, 01 + 11, 01 + 22).

**Análisis**: SS de efectos como en un factorial sin bloques;
$SS_{\text{Bloques}} = \sum B_i^2/3^{k-1} - y_{\cdots}^2/3^k$ (por réplica), que coincide exactamente
con la SS del componente confundido.

#### Ejemplo 9-2 ($3^2$, una réplica, 3 bloques, $AB^2$ confundido)
Datos: bloque 1: 00=4, 11=−4, 22=0 (total 0); bloque 2: 10=−2, 21=1, 02=8 (total 7); bloque 3:
01=5, 12=−5, 20=0 (total 0).

- $SS_A = 131.56$, $SS_B = 0.22$.
- $SS_{\text{Bloques}} = (0^2+7^2+0^2)/3 - 7^2/9 = 10.89$, idéntico a $SS_{AB^2}$ calculado con los
  totales de la diagonal izquierda-derecha $(0, 0, 7)$.

Tabla 9-4:

| Fuente | SS | g.l. |
|---|---|---|
| Bloques ($AB^2$) | 10.89 | 2 |
| $A$ | 131.56 | 2 |
| $B$ | 0.22 | 2 |
| $AB$ | 2.89 | 2 |
| Total | 145.56 | 8 |

Con una sola réplica **no hay prueba formal**. **No es buena idea** usar el componente $AB$ como
estimación del error.

**Ejemplo: $3^3$ en 3 bloques de 9 con $AB^2C^2$ confundido** ($L = x_1 + 2x_2 + 2x_3$, fig. 9-7):
- En el bloque principal están 000, 012, 101; el resto se genera por sumas:
  101+101=202, 012+012=021, 101+012=110, 101+021=122, 012+202=211, 021+202=220.

| Bloque | $L$ | Combinaciones |
|---|---|---|
| 1 (principal) | 0 | 000, 012, 101, 202, 021, 110, 122, 211, 220 |
| 2 (sumar 200) | 2 | 200, 212, 001, 102, 221, 010, 022, 111, 120 |
| 3 (sumar 100) | 1 | 100, 112, 201, 002, 121, 210, 222, 011, 020 |

Tabla 9-5 (ANOVA del $3^3$ con $AB^2C^2$ confundido, una réplica):

| Fuente | g.l. |
|---|---|
| Bloques ($AB^2C^2$) | 2 |
| $A$, $B$, $C$ | 2 c/u |
| $AB$, $AC$, $BC$ | 4 c/u |
| Error ($ABC + AB^2C + ABC^2$) | 6 |
| Total | 26 |

- Se conserva la información de todos los efectos principales e interacciones de dos factores.
- Los tres componentes restantes de $ABC$ forman el error; su SS se obtiene **por sustracción**:
  $SS_{ABC}$ (cálculo usual) $- SS_{\text{Bloques}}$.
- **Regla general**: en $3^k$ en tres bloques, confundir siempre un componente de la
  **interacción de orden más alto**.

### 9-2.2 El diseño factorial 3^k en nueve bloques

- 9 bloques → 8 g.l. confundidos → **cuatro componentes** de 2 g.l.
- Se eligen **dos** componentes; automáticamente se confunden otros dos: sus **interacciones
  generalizadas**. En el sistema $3^k$, las interacciones generalizadas de $P$ y $Q$ son
  **$PQ$ y $PQ^2$** (o $P^2Q$).
- Dos definiciones de contrastes (ec. 9-3):

$$L_1 = \alpha_1x_1 + \cdots + \alpha_kx_k = u \pmod 3,\quad u = 0,1,2$$
$$L_2 = \beta_1x_1 + \cdots + \beta_kx_k = h \pmod 3,\quad h = 0,1,2 \qquad \text{(9-3)}$$

  Las combinaciones con el mismo par $(L_1, L_2)$ van al mismo bloque (9 pares). Bloque
  principal: $L_1 = L_2 = 0$; es grupo bajo adición mod 3 y sirve para generar los demás.

**Ejemplo: $3^4$ en 9 bloques de 9 con $ABC$ y $AB^2D^2$** (ec. 9-4):
$L_1 = x_1 + x_2 + x_3$, $L_2 = x_1 + 2x_2 + 2x_4$. Interacciones generalizadas:

- $(ABC)(AB^2D^2) = A^2B^3CD^2 = (A^2CD^2)^2 = AC^2D$
- $(ABC)(AB^2D^2)^2 = A^3B^5CD^4 = B^2CD = (B^2CD)^2 = BC^2D^2$

Confundidos: $ABC$, $AB^2D^2$, $AC^2D$, $BC^2D^2$ (fig. 9-8).
Bloque principal: 0000, 0122, 0211, 1021, 1110, 1202, 2012, 2101, 2220. Los otros ocho bloques
se obtienen sumando a este bloque, p. ej., 0001, 0002, 0010, 0020, 0100, 0200, 1000, 2000.
(Las etiquetas $(L_1,L_2)$ impresas bajo algunos bloques de la fig. 9-8 no coinciden con las que
resultan de la ec. 9-4 —p. ej. el bloque de 0001 tiene $L_2=2$ pero aparece rotulado (0,1)—; el
contenido de los bloques sí es correcto. Dudoso/errata, pág. 378.)

**Análisis**: los componentes no confundidos de las interacciones afectadas se obtienen
**restando** la SS del componente confundido de la SS de la interacción completa; los componentes
se calculan con el método de la sec. 9-1.3.

### 9-2.3 El diseño factorial 3^k en 3^p bloques

- $3^p$ bloques de $3^{k-p}$ observaciones, $p<k$.
- Elegir **$p$ componentes independientes**; se confunden automáticamente otros

$$\frac{3^p - 2p - 1}{2}$$

  componentes (sus interacciones generalizadas). Total: $(3^p-1)/2$ componentes de 2 g.l.
  $= 3^p-1$ g.l. entre bloques.
- Ejemplo: $3^7$ en 27 bloques ($p=3$) de 81 corridas (2187 observaciones). Generadores
  $ABC^2DG$, $BCE^2F^2G$, $BDEFG$; los otros $[3^3-2(3)-1]/2 = 10$ confundidos:

| Producto | Resultado |
|---|---|
| $(ABC^2DG)(BCE^2F^2G)$ | $AB^2DE^2F^2G^2$ |
| $(ABC^2DG)(BCE^2F^2G)^2$ | $ACDEF$ |
| $(ABC^2DG)(BDEFG)$ | $AB^2C^2D^2EFG^2$ |
| $(ABC^2DG)(BDEFG)^2$ | $AC^2E^2F^2$ |
| $(BCE^2F^2G)(BDEFG)$ | $BC^2D^2G$ |
| $(BCE^2F^2G)(BDEFG)^2$ | $CD^2EF$ |
| $(ABC^2DG)(BCE^2F^2G)(BDEFG)$ | $AD^2$ |
| $(ABC^2DG)^2(BCE^2F^2G)(BDEFG)$ | $AB^2CG^2$ |
| $(ABC^2DG)(BCE^2F^2G)^2(BDEFG)$ | $ABCD^2E^2F^2G$ |
| $(ABC^2DG)(BCE^2F^2G)(BDEFG)^2$ | $ABEFG$ |

---

## 9-3 Réplicas fraccionadas del diseño factorial 3^k

Motivación: una réplica completa del $3^k$ es muy grande incluso para $k$ moderado. Problema: las
estructuras de alias son **complicadas**.

### 9-3.1 La fracción un tercio del diseño factorial 3^k (diseño 3^(k-1))

**Construcción (por bloques)**:
1. Elegir un componente de interacción de 2 g.l. (generalmente de la interacción de orden más
   alto), $AB^{\alpha_2}C^{\alpha_3}\cdots K^{\alpha_k}$.
2. Partir el $3^k$ completo en tres bloques con ese componente; **cada bloque es una fracción
   $3^{k-1}$** y puede usarse cualquiera.
3. **Relación de definición**: $I = AB^{\alpha_2}C^{\alpha_3}\cdots K^{\alpha_k}$.
4. **Alias**: cada efecto principal o componente de interacción tiene **dos alias**, que se
   obtienen multiplicando el efecto por $I$ **y** por $I^2$, módulo 3 (normalizando para que la
   primera letra tenga exponente 1).

**Ejemplo: $3^{3-1}$.** Hay 4 componentes de $ABC$ ($ABC$, $AB^2C$, $ABC^2$, $AB^2C^2$) × 3
valores de $u$ → **12 fracciones un tercio diferentes**, definidas por
$x_1 + \alpha_2x_2 + \alpha_3x_3 = u \pmod 3$, $\alpha\in\{1,2\}$, $u\in\{0,1,2\}$.

Con $I = AB^2C^2$: $x_1 + 2x_2 + 2x_3 = u \pmod 3$ (fig. 9-9):

| $u$ | Combinaciones (9 corridas) |
|---|---|
| 0 | 000, 012, 101, 202, 021, 110, 122, 211, 220 |
| 1 | 100, 112, 201, 002, 121, 210, 222, 011, 020 |
| 2 | 200, 212, 001, 102, 221, 010, 022, 111, 120 |

Estructura de alias ($I = AB^2C^2$):

| Efecto | $\times I$ | $\times I^2$ |
|---|---|---|
| $A$ | $A(AB^2C^2) = A^2B^2C^2 = ABC$ | $A(AB^2C^2)^2 = A^3B^4C^4 = BC$ |
| $B$ | $B(AB^2C^2) = AB^3C^2 = AC^2$ | $B(AB^2C^2)^2 = A^2B^5C^4 = ABC^2$ |
| $C$ | $C(AB^2C^2) = AB^2C^3 = AB^2$ | $C(AB^2C^2)^2 = A^2B^4C^5 = AB^2C$ |
| $AB$ | $AB(AB^2C^2) = A^2B^3C^2 = AC$ | $AB(AB^2C^2)^2 = A^3B^5C^4 = BC^2$ |

Los 8 g.l. estiman realmente: $A + BC + ABC$; $B + AC^2 + ABC^2$; $C + AB^2 + AB^2C$;
$AB + AC + BC^2$.

- Es un diseño de **resolución III** ($3^{3-1}_{III}$): efectos principales alias de componentes
  de interacciones de dos factores.
- Solo tiene valor práctico si **todas las interacciones son pequeñas**. Si p. ej. $BC$ es grande,
  distorsiona la estimación de $A$ y hace muy difícil interpretar $AB + AC + BC^2$.
- **Relación con el cuadrado latino**: la fracción $u=0$, con $A$ = renglón y $B$ = columna y el
  nivel de $C$ como "letra", es un cuadrado latino $3\times3$:

  | | $B=0$ | $B=1$ | $B=2$ |
  |---|---|---|---|
  | $A=0$ | 000 | 012 | 021 |
  | $A=1$ | 101 | 110 | 122 |
  | $A=2$ | 202 | 211 | 220 |

  El supuesto de interacciones despreciables es el mismo del cuadrado latino. Hay exactamente 12
  cuadrados latinos $3\times3$ (tabla 4-13), uno por cada una de las 12 fracciones $3^{3-1}$. (Los
  dos diseños surgen por motivos distintos: fracción vs. restricción en la aleatorización.)

**Construcción alternativa (diseño básico + generador)**, análoga a la del $2^{k-p}$:
1. Escribir el factorial completo $3^{k-1}$ en $k-1$ factores (**diseño básico**).
2. Introducir el factor $k$-ésimo igualando sus niveles al componente apropiado de la interacción
   de orden más alto de los primeros $k-1$ factores (ec. 9-5):

$$x_k = \beta_1x_1 + \beta_2x_2 + \cdots + \beta_{k-1}x_{k-1} \pmod 3, \qquad \beta_i = (3-\alpha_k)\,\alpha_i \pmod 3 \qquad \text{(9-5)}$$

   Se obtiene el diseño de **resolución más alta posible**.

**Ejemplo: $3^{4-1}_{IV}$ con $I = AB^2CD$** ($\alpha_1=\alpha_3=\alpha_4=1$, $\alpha_2=2$):
$\beta_1 = (3-1)(1) = 2$, $\beta_2 = (3-1)(2) = 4 = 1$, $\beta_3 = 2$ →

$$x_4 = 2x_1 + x_2 + 2x_3 \pmod 3 \qquad \text{(9-6)}$$

Tabla 9-6 (27 corridas; los tres primeros dígitos son el $3^3$ completo):

| | | |
|---|---|---|
| 0000 | 0012 | 2221 |
| 0101 | 0110 | 0021 |
| 1100 | 0211 | 0122 |
| 1002 | 1011 | 0220 |
| 0202 | 1112 | 1020 |
| 1201 | 1210 | 1121 |
| 2001 | 2010 | 1222 |
| 2102 | 2111 | 2022 |
| 2200 | 2212 | 2120 |

- 26 g.l. → SS de 13 efectos principales y componentes de interacción (con sus alias).
- Alias de $A$: $A(AB^2CD) = ABC^2D^2$ y $A(AB^2CD)^2 = BC^2D^2$.
- Los 4 efectos principales quedan libres de componentes de interacciones de dos factores, pero
  **algunos componentes de interacciones de dos factores son alias entre sí** (resolución IV).
  Si una interacción de dos factores es grande, será muy difícil aislarla.

**Análisis de un $3^{k-1}$**: ANOVA usual de factoriales; SS de componentes de interacción como en
la sec. 9-1. Recordar que los componentes **no tienen interpretación práctica**.

### 9-3.2 Otros diseños factoriales fraccionados 3^(k-p)

- Fracción $(1/3)^p$ del $3^k$ con $3^{k-p}$ corridas, $p<k$: $3^{k-2}$ = un noveno, $3^{k-3}$ = un
  veintisieteavo, etc.
- **Construcción por bloques**: elegir $p$ componentes de interacción, partir el $3^k$ en $3^p$
  bloques; cada bloque es una fracción $3^{k-p}$.
- **Relación de definición**: los $p$ efectos elegidos más sus $(3^p - 2p - 1)/2$ interacciones
  generalizadas.
- **Alias**: multiplicar el efecto por cada palabra de $I$ y por su cuadrado ($I$ e $I^2$),
  módulo 3.
- **Construcción alternativa**: escribir un $3^{k-p}$ completo e introducir los $p$ factores
  adicionales igualándolos a componentes de interacción (como en 9-3.1).

**Ejemplo: $3^{4-2}_{III}$ con $AB^2C$ y $BCD$.** Interacciones generalizadas:
$(AB^2C)(BCD) = AC^2D$ y $(AB^2C)(BCD)^2 = ABD^2$.

$$I = AB^2C = BCD = AC^2D = ABD^2$$

Diseño: $3^2$ completo en $A$, $B$ y

$$x_3 = 2x_1 + x_2, \qquad x_4 = 2x_2 + 2x_3 \pmod 3$$

Tabla 9-7 (9 corridas): 0000, 1021, 2012, 0111, 1102, 2120, 0222, 1210, 2201.
(Equivale a partir el $3^4$ en 9 bloques con $AB^2C$ y $BCD$ y tomar uno.)

Tabla 9-8 (estructura de alias completa; 8 g.l. = 4 efectos principales y sus alias):

| Efecto | Alias por $I$ | Alias por $I^2$ |
|---|---|---|
| $A$ | $ABC^2$, $ABCD$, $ACD^2$, $AB^2D$ | $BC^2$, $AB^2C^2D^2$, $CD^2$, $BD^2$ |
| $B$ | $AC$, $BC^2D^2$, $ABC^2D$, $AB^2D^2$ | $ABC$, $CD$, $AB^2C^2D$, $AD^2$ |
| $C$ | $AB^2C^2$, $BC^2D$, $AD$, $ABCD^2$ | $AB^2$, $BD$, $ACD$, $ABC^2D^2$ |
| $D$ | $AB^2CD$, $BCD^2$, $AC^2D^2$, $AB$ | $AB^2CD^2$, $BC$, $AC^2$, $ABD$ |

- Solo útil **en ausencia de interacciones**.
- Con $A$ = renglones y $B$ = columnas, este $3^{4-2}_{III}$ es un **cuadrado grecolatino**.
- Catálogo: Connor y Zelen (National Bureau of Standards) tabulan diseños $3^{k-p}$ para
  $4\le k\le10$.

**Juicio del autor sobre los $3^{k-p}$** (pág. 383):
- Para $k \ge 4$ o 5 se termina en fracciones pequeñas con **alias parciales** de componentes de
  interacción de 2 g.l.; la interpretación es difícil o imposible si las interacciones no son
  despreciables.
- **No existen esquemas simples de aumento** (como el doblez del $2^{k-p}$) para combinar
  fracciones y aislar interacciones.
- Para curvatura hay alternativas más eficientes (cap. 11).
- Conclusión: los $3^{k-p}$ "son soluciones que causan problemas; no son, en general, buenos
  diseños".

---

## 9-4 Diseños factoriales con niveles mixtos

- Postura del autor: los factoriales y fraccionados de **dos niveles** deben ser la piedra angular
  de la experimentación industrial; el sistema de tres niveles es mucho menos útil (diseños
  grandes, alias complejos).
- Sin embargo, a veces hay que incluir factores con más de dos niveles, típicamente cuando hay un
  factor **cualitativo** con (p. ej.) tres niveles junto a factores cuantitativos.
- Si **todos** los factores son cuantitativos: usar dos niveles **con puntos centrales**.
- Esta sección: cómo incorporar factores de **tres** y **cuatro** niveles en un $2^k$.

### 9-4.1 Factores con dos y tres niveles

**Idea (reemplazo/colapso)**: dos columnas de dos niveles ($B$, $C$) de la tabla de signos del
$2^k$ se combinan para formar un factor $X$ de tres niveles, **repitiendo el nivel intermedio**
(tabla 9-9):

| $B$ | $C$ | $X$ |
|---|---|---|
| − | − | $x_1$ (bajo) |
| + | − | $x_2$ (intermedio) |
| − | + | $x_2$ (intermedio) |
| + | + | $x_3$ (alto) |

**Ejemplo: $A$ de dos niveles y $X$ de tres niveles en un $2^3$ de 8 corridas** (tabla 9-10; la
fila superior indica el efecto real que estima cada columna):

| Corrida | $A$ [$A$] | $B$ [$X_L$] | $C$ [$X_L$] | $AB$ [$A\times X_L$] | $AC$ [$A\times X_L$] | $BC$ [$X_Q$] | $ABC$ [$A\times X_Q$] | $A$ real | $X$ real |
|---|---|---|---|---|---|---|---|---|---|
| 1 | − | − | − | + | + | + | − | Bajo | Bajo |
| 2 | + | − | − | − | − | + | + | Alto | Bajo |
| 3 | − | + | − | − | + | − | + | Bajo | Intermedio |
| 4 | + | + | − | + | − | − | − | Alto | Intermedio |
| 5 | − | − | + | + | − | − | + | Bajo | Intermedio |
| 6 | + | − | + | − | + | − | − | Alto | Intermedio |
| 7 | − | + | + | − | − | + | − | Bajo | Alto |
| 8 | + | + | + | + | + | + | + | Alto | Alto |

Interpretación:
- $X$ tiene 2 g.l.; si es cuantitativo se parte en $X_L$ (lineal) y $X_Q$ (cuadrático), 1 g.l. c/u.
- $X_L$ = **suma** de las estimaciones de los efectos de las columnas $B$ y $C$; solo usa las
  corridas con $X$ bajo o alto (1, 2, 7, 8).
- $A\times X_L$ = suma de los efectos de las columnas $AB$ y $AC$.
- $X_Q$ = columna $BC$; $A\times X_Q$ = columna $ABC$.
- **Error puro**: las corridas 3 y 5 son réplicas ($A$ bajo, $X$ intermedio) → 1 g.l.; las corridas
  4 y 6 también ($A$ alto, $X$ intermedio) → 1 g.l. El promedio de las dos varianzas es $MS_E$
  con 2 g.l.

Tabla 9-11 (ANOVA):

| Fuente | SS | g.l. | MS |
|---|---|---|---|
| $A$ | $SS_A$ | 1 | $MS_A$ |
| $X$ ($X_L + X_Q$) | $SS_X$ | 2 | $MS_X$ |
| $AX$ ($A\times X_L + A\times X_Q$) | $SS_{AX}$ | 2 | $MS_{AX}$ |
| Error (corridas 3 y 5, y corridas 4 y 6) | $SS_E$ | 2 | $MS_E$ |
| Total | $SS_T$ | 7 | |

(En la tabla impresa el cuadrado medio de $X$ aparece como "$MS_B$"; es $MS_X$ — errata aparente,
pág. 385.)

**Extensiones**:
- Si se suponen despreciables las interacciones de dos o más factores, el diseño de la tabla 9-10
  se convierte en una fracción de **resolución III** con hasta **cuatro factores de dos niveles y
  uno de tres niveles**: los de dos niveles se asocian a las columnas $A$, $AB$, $AC$, $ABC$. La
  columna **$BC$ no puede usarse** (contiene el efecto cuadrático $X_Q$).
- Mismo procedimiento en $2^k$ de 16, 32 y 64 corridas. Con **16 corridas**:
  - resolución V con **2 factores de dos niveles y 2 o 3 factores de tres niveles**;
  - resolución V con **3 factores de dos niveles y 1 de tres niveles**;
  - con **4 factores de dos niveles y 1 de tres niveles** → resolución III.
- Referencia para más diseños: Addelman.

### 9-4.2 Factores con dos y cuatro niveles

**Idea**: un factor de **cuatro niveles** se representa con **dos columnas de dos niveles** ($P$,
$Q$) de la tabla de signos (tabla 9-12):

| Corrida | $P$ | $Q$ | Factor $A$ (4 niveles) |
|---|---|---|---|
| 1 | − | − | $a_1$ |
| 2 | + | − | $a_2$ |
| 3 | − | + | $a_3$ |
| 4 | + | + | $a_4$ |

Las columnas $P$, $Q$ y $PQ$ son mutuamente ortogonales y juntas son el efecto del factor de
cuatro niveles (**3 g.l.**).

**Ejemplo: diseño $4\times2^2$ en 16 corridas** (tabla 9-13). Se parte de la tabla de signos del
$2^4$ ($A$, $B$, $C$, $D$); las columnas $A$ y $B$ forman el factor $X$ de cuatro niveles:
$(A,B) = (-,-)\to x_1$, $(+,-)\to x_2$, $(-,+)\to x_3$, $(+,+)\to x_4$. Se calculan las SS de las
15 columnas $A, B, \dots, ABCD$ como en un $2^4$ usual y se agrupan:

| Efecto real | Composición | g.l. |
|---|---|---|
| $SS_X$ | $SS_A + SS_B + SS_{AB}$ | 3 |
| $SS_C$ | $SS_C$ | 1 |
| $SS_D$ | $SS_D$ | 1 |
| $SS_{CD}$ | $SS_{CD}$ | 1 |
| $SS_{XC}$ | $SS_{AC} + SS_{BC} + SS_{ABC}$ | 3 |
| $SS_{XD}$ | $SS_{AD} + SS_{BD} + SS_{ABD}$ | 3 |
| $SS_{XCD}$ | $SS_{ACD} + SS_{BCD} + SS_{ABCD}$ | 3 |

- Con una réplica (16 corridas) permite estimar todos los efectos principales e interacciones de
  $X$, $C$, $D$ (15 g.l.; el error requiere réplicas o despreciar interacciones de orden alto —
  *nota propia*).
- Si se ignoran las interacciones de dos factores, pueden asociarse **hasta nueve factores
  adicionales de dos niveles** a las columnas de interacción de dos factores (**excepto $AB$**),
  de tres factores y de cuatro factores. *(Nota propia: quitando $A$, $B$, $AB$, $C$ y $D$ quedan
  10 columnas; el libro dice "nueve", pág. 387.)*

---

## Resumen operativo (reglas y advertencias del capítulo)

1. **Notación**: niveles 0, 1, 2; combinación = cadena de $k$ dígitos; efectos principales 2 g.l.;
   interacción de $h$ factores $2^h$ g.l. = $2^{h-1}$ componentes ortogonales de 2 g.l.
2. **Componentes**: $AB = J(AB)$ ↔ $x_1 + x_2$; $AB^2 = I(AB)$ ↔ $x_1 + 2x_2$; para tres factores
   $W=AB^2C^2$, $X=AB^2C$, $Y=ABC^2$, $Z=ABC$. Primera letra siempre con exponente 1 (si no, elevar
   al cuadrado y reducir mod 3). Sin significado físico; son herramientas de construcción.
3. **Confusión en $3^p$ bloques**: $p$ definiciones de contrastes mod 3; bloque principal
   ($L_i=0$) es grupo bajo suma mod 3; se confunden $(3^p-1)/2$ componentes (los $p$ elegidos +
   $(3^p-2p-1)/2$ interacciones generalizadas $PQ$, $PQ^2$).
4. **Análisis con confusión**: SS de efectos como siempre; $SS_{\text{Bloques}}$ = suma de las SS de
   los componentes confundidos; componentes no confundidos de una interacción = SS de la
   interacción completa − SS confundida.
5. **Fracción $3^{k-p}$**: un bloque del esquema de confusión; $I$ = generadores + interacciones
   generalizadas; cada efecto tiene alias al multiplicar por cada palabra de $I$ y de $I^2$
   (dos alias por palabra). $3^{3-1}$ = cuadrado latino; $3^{4-2}$ = cuadrado grecolatino.
6. **Generador de máxima resolución para $3^{k-1}$**: $x_k = \sum\beta_ix_i$ con
   $\beta_i = (3-\alpha_k)\alpha_i \bmod 3$.
7. **Recomendación global**: evitar $3^k$ y $3^{k-p}$ para factores cuantitativos; preferir $2^k$
   con puntos centrales → diseño central compuesto, o diseños de superficie de respuesta
   (cap. 11). Reservar tres niveles para factores cualitativos, y entonces considerar niveles
   mixtos construidos sobre un $2^k$ (secs. 9-4.1 y 9-4.2).

## 9-5 Problemas
Problemas 9-1 a 9-23 (págs. 387–391): análisis de $3^2$ y $3^3$ con réplicas (9-1 a 9-6, incluye
componentes $I$ y $J$ y ajuste de modelo de segundo orden en 9-6), confusión de $3^3$ y $3^4$ en 3
y 9 bloques (9-7 a 9-11), fracciones $3^{3-1}$, $3^{4-1}_{IV}$, $3^{5-2}$, $3^{9-6}$ (9-12 a 9-17),
niveles mixtos $4\times2^3$, $2^23^2$ y factores de tres niveles en un $2^4$ de 16 corridas (9-18
a 9-21), experimento Pinot Noir 1987 con un factor de cuatro niveles en una fracción de 16
corridas (9-22) y experimento de Baten de barras de acero $3\times2\times4$ (9-23).
