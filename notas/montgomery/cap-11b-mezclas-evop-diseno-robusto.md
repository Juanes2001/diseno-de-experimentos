# Capítulo 11 (parte B) — Mezclas, operación evolutiva y diseño robusto: secciones 11-5 a 11-8

> Montgomery, págs. 472–510

> Nota de paginación: en este tramo del escaneo la equivalencia real es **página PDF = página del libro + 11**
> (pág. 472 → `p483.png`, pág. 510 → `p521.png`), no +13.

Contenido: 11-5 Experimentos con mezclas · 11-6 Operación evolutiva (EVOP) · 11-7 Diseño robusto
(11-7.1 Antecedentes / Taguchi; 11-7.2 Enfoque de superficie de respuesta) · 11-8 Problemas.

---

## 11-5 Experimentos con mezclas (págs. 472–484)

### Cuándo se usa

En los diseños de superficie de respuesta habituales los niveles de cada factor se eligen con
independencia de los demás. En un **experimento con mezclas** los factores son los componentes
(ingredientes) de una formulación y la respuesta depende de las **proporciones**, no de las
cantidades; por eso los niveles no son independientes. Con $p$ componentes de proporciones
$x_1,\dots,x_p$:

$$0 \le x_i \le 1,\quad i=1,\dots,p \qquad\text{y}\qquad x_1+x_2+\cdots+x_p = 1$$

Consecuencias geométricas (fig. 11-30):

- $p=2$: la región factible es el segmento $x_1+x_2=1$.
- $p=3$: es un triángulo equilátero (símplex) cuyos vértices son las **mezclas puras** (100 % de un
  componente); los lados son mezclas binarias (falta el componente del vértice opuesto).
- En general la región es un símplex regular de $p-1$ dimensiones.

Para $p=3$ se representa en **coordenadas trilineales** (fig. 11-31): cada lado corresponde a
$x_i=0$ para el componente del vértice opuesto y las líneas de graduación paralelas a ese lado
marcan incrementos de 10 % en ese componente.

### Diseños símplex

**Símplex reticular $\{p, m\}$** (*simplex lattice*). Cada componente toma los $m+1$ valores
igualmente espaciados

$$x_i = 0, \frac{1}{m}, \frac{2}{m}, \dots, 1 \qquad i = 1,\dots,p \tag{11-21}$$

y se usan **todas** las combinaciones que cumplen $\sum x_i = 1$. Número de puntos:

$$N = \frac{(p+m-1)!}{m!\,(p-1)!}$$

| Diseño | $N$ | Puntos |
|---|---|---|
| $\{3,2\}$ | 6 | 3 vértices + 3 puntos medios de aristas: $(1,0,0),(0,1,0),(0,0,1),(\tfrac12,\tfrac12,0),(\tfrac12,0,\tfrac12),(0,\tfrac12,\tfrac12)$ |
| $\{3,3\}$ | 10 | 3 vértices + 6 puntos a tercios sobre las aristas (p. ej. $x_1=\tfrac23, x_3=\tfrac13$) + centroide |
| $\{4,2\}$ | 10 | 4 vértices + 6 puntos medios de aristas |
| $\{4,3\}$ | 20 | vértices, tercios de aristas y centroides de caras |

(fig. 11-32). El parámetro $m$ es el grado del polinomio que el retículo puede sostener.

**Símplex con centroide** (*simplex centroid*). Con $p$ componentes tiene $2^p-1$ puntos:

- las $p$ permutaciones de $(1,0,\dots,0)$ (mezclas puras),
- las $\binom{p}{2}$ permutaciones de $(\tfrac12,\tfrac12,0,\dots,0)$ (binarias),
- las $\binom{p}{3}$ permutaciones de $(\tfrac13,\tfrac13,\tfrac13,0,\dots,0)$, …
- y el centroide global $(\tfrac1p,\dots,\tfrac1p)$.

Para $p=3$: 7 puntos; para $p=4$: 15 puntos (fig. 11-33).

**Crítica y aumento del diseño.** Ambos son **diseños de puntos frontera**: casi todas las corridas
tienen a lo sumo $p-1$ componentes presentes. Si interesa predecir mezclas completas, Montgomery
recomienda aumentarlos con puntos interiores: **corridas axiales** y el **centroide global** (si no
está ya).

- **Eje del componente $i$**: recta desde el punto base $x_i=0,\ x_j=1/(p-1)\ (j\neq i)$ —centroide
  de la frontera de $p-2$ dimensiones opuesta al vértice— hasta el vértice $x_i=1$. Su longitud es 1.
- **Puntos axiales**: sobre los ejes, a distancia $\Delta$ del centroide. Máximo
  $\Delta=(p-1)/p$ (el vértice). Recomendación: a mitad de camino entre centroide y vértice,
  $\Delta=(p-1)/(2p)$.
- Se les llama **mezclas de verificación axial**: es práctica común dejarlas fuera del ajuste
  preliminar y usarlas después para comprobar la adecuación del modelo.

Ejemplo (fig. 11-35): el $\{3,2\}$ aumentado tiene **10 puntos**, 4 de ellos interiores: centroide
$(\tfrac13,\tfrac13,\tfrac13)$ y los axiales $(\tfrac23,\tfrac16,\tfrac16)$,
$(\tfrac16,\tfrac23,\tfrac16)$, $(\tfrac16,\tfrac16,\tfrac23)$. Comparado con el $\{3,3\}$ (también
10 puntos):

| | $\{3,3\}$ | $\{3,2\}$ aumentado |
|---|---|---|
| Cúbico completo | sí | no |
| Cúbico especial | sí | sí |
| Términos especiales de cuarto orden (p. ej. $\beta_{1233}x_1x_2x_3^2$) añadidos al cuadrático | — | sí |
| Detección de curvatura interior / potencia de la prueba de falta de ajuste | menor | mayor |

El aumentado es preferible cuando no se conoce el modelo y se piensa construirlo **secuencialmente**:
ajustar un polinomio simple (quizá lineal), probar falta de ajuste, añadir términos de orden
superior, volver a probar, etc.

### Modelos canónicos (de Scheffé)

Por la restricción $\sum x_i=1$ los polinomios usuales no son estimables tal cual (el intercepto y
los cuadrados puros son redundantes); se usan las formas canónicas **sin término independiente**:

**Lineal**

$$E(y)=\sum_{i=1}^{p}\beta_i x_i \tag{11-22}$$

**Cuadrático**

$$E(y)=\sum_{i=1}^{p}\beta_i x_i+\sum\sum_{i<j}^{p}\beta_{ij}x_ix_j \tag{11-23}$$

**Cúbico completo**

$$E(y)=\sum_{i=1}^{p}\beta_i x_i+\sum\sum_{i<j}^{p}\beta_{ij}x_ix_j+\sum\sum_{i<j}\delta_{ij}x_ix_j(x_i-x_j)+\sum\sum\sum_{i<j<k}\beta_{ijk}x_ix_jx_k \tag{11-24}$$

**Cúbico especial**

$$E(y)=\sum_{i=1}^{p}\beta_i x_i+\sum\sum_{i<j}^{p}\beta_{ij}x_ix_j+\sum\sum\sum_{i<j<k}\beta_{ijk}x_ix_jx_k \tag{11-25}$$

Número de parámetros (conteo propio, no tabulado en el libro): lineal $p$; cuadrático $p(p+1)/2$;
cúbico especial $p(p+1)/2+\binom{p}{3}$; cúbico completo $p(p+1)/2+\binom p2+\binom p3$. Para
$p=3$: 3, 6, 7 y 10.

**Interpretación de los coeficientes**

- $\beta_i$: respuesta esperada de la **mezcla pura** $i$ ($x_i=1$, $x_j=0$ para $j\ne i$). La parte
  $\sum\beta_ix_i$ es la **porción de mezcla lineal** (lo que daría el simple promedio ponderado de
  los componentes puros).
- $\beta_{ij}$: curvatura por mezclado no lineal del par $(i,j)$. $\beta_{ij}>0$ = mezcla
  **sinérgica** (la binaria rinde más que el promedio de las puras); $\beta_{ij}<0$ = mezcla
  **antagónica**. En la mezcla 50:50 el exceso sobre el promedio de las puras es $\beta_{ij}/4$
  (se deduce de 11-23).
- Los términos de orden superior suelen hacer falta porque (1) los fenómenos son complejos y (2) la
  región experimental suele ser toda la región de operabilidad, grande, y exige un modelo elaborado.
- No se interpreta "el efecto de un factor manteniendo los otros fijos": no se puede cambiar una
  proporción sin cambiar otra.

**Ajuste y pruebas.** Mínimos cuadrados sobre el modelo sin intercepto. En la tabla ANOVA de un
modelo cuadrático para mezclas (salida de Design-Expert, tablas 11-15 y 11-16) las fuentes son:

| Fuente | g.l. (caso $p=3$, $N=14$) |
|---|---|
| Modelo | 5 ($=$ n.º de parámetros $-1$) |
| — Mezcla lineal | 2 ($=p-1$) |
| — $AB$, $AC$, $BC$ | 1 cada uno |
| Residual | 8 |
| — Falta de ajuste | 4 |
| — Error puro | 4 |
| Total corregido | 13 |

La prueba de la porción lineal contrasta $H_0:\beta_1=\dots=\beta_p$ (ninguna dependencia de la
composición); cada término binario se prueba con $F=CM_{\text{término}}/CM_{\text{Residual}}$ y la
falta de ajuste con $F=CM_{\text{FdA}}/CM_{\text{EP}}$.

### Restricciones y pseudocomponentes

**Solo cotas inferiores**, $l_i \le x_i \le 1$: la región factible sigue siendo un símplex, inscrito
en el original. Se trabaja con **pseudocomponentes**

$$x_i'=\frac{x_i-l_i}{1-\sum_{j=1}^{p}l_j},\qquad \sum_{j=1}^{p} l_j<1 \tag{11-26}$$

que cumplen $x_1'+\cdots+x_p'=1$, de modo que se aplica cualquier diseño símplex en las $x'$. Para
correr el experimento se regresa a los componentes reales:

$$x_i = l_i+\Big(1-\sum_{j=1}^{p}l_j\Big)x_i' \tag{11-27}$$

**Cotas inferiores y superiores a la vez**: la región deja de ser un símplex y pasa a ser un
**politopo irregular**. Sin forma estándar, lo indicado son los **diseños generados por computadora**
(D-óptimos, sección 11-4.3), tomando como puntos candidatos vértices, centros de aristas, centroide
global y puntos de verificación axial (a medio camino entre centroide y vértices).

### Ejemplo 11-3 — Mezcla de tres componentes (elongación de hilo; Cornell)

- Componentes: polietileno ($x_1$), poliestireno ($x_2$), polipropileno ($x_3$). Respuesta:
  elongación del hilo (kg de fuerza).
- Diseño: símplex reticular $\{3,2\}$ (tabla 11-13), 2 réplicas en las mezclas puras y 3 en las
  binarias (15 observaciones). Promedios: $(1,0,0)$ 11.7; $(\tfrac12,\tfrac12,0)$ 15.3; $(0,1,0)$
  9.4; $(0,\tfrac12,\tfrac12)$ 10.5; $(0,0,1)$ 16.4; $(\tfrac12,0,\tfrac12)$ 16.9.
- $\hat\sigma = 0.85$ (de las réplicas).
- Modelo cuadrático ajustado:

$$\hat y = 11.7x_1+9.4x_2+16.4x_3+19.0x_1x_2+11.4x_1x_3-9.6x_2x_3$$

  (Comprobación propia: con un $\{p,2\}$ saturado, $\hat\beta_i=\bar y_i$ y
  $\hat\beta_{ij}=4\bar y_{ij}-2(\bar y_i+\bar y_j)$; p. ej. $4(15.3)-2(11.7+9.4)=19.0$.)
- Interpretación: $\hat\beta_3>\hat\beta_1>\hat\beta_2$ → el polipropileno puro da la mayor
  elongación; $\hat\beta_{12},\hat\beta_{13}>0$ → mezclado sinérgico en los pares 1–2 y 1–3;
  $\hat\beta_{23}<0$ → antagónico en 2–3.
- Óptimo (contornos, fig. 11-34): máxima elongación sobre la arista 1–3, con ≈ 80 % del componente 3
  y ≈ 20 % del componente 1.

### Ejemplo 11-4 — Formulación de una pintura (región restringida, D-óptimo, dos respuestas)

- Recubrimiento automotriz: monómero ($x_1$), entrelazador ($x_2$), resina ($x_3$), en porcentaje.
  Requisitos: dureza Knoop $y_1 > 25$ y porcentaje de sólidos $y_2 < 30$.
- Restricciones: $x_1+x_2+x_3=100$; $5\le x_1\le 25$; $25\le x_2\le 40$; $50\le x_3\le 70$ (fig.
  11-36). Región no símplex → diseño **D-óptimo** para modelo cuadrático de mezcla (Design-Expert).
- Diseño de **14 corridas** (tabla 11-14): 6 para el modelo cuadrático + 4 puntos distintos
  adicionales para falta de ajuste + 4 réplicas para error puro.
- Los modelos se reportan en pseudocomponentes (A, B, C). (Con $\sum l_j = 80$ sobre 100, la
  ec. 11-26 da $x_i'=(x_i-l_i)/20$; deducción propia.)

**Dureza** (tabla 11-15):

| Fuente | SC | g.l. | CM | $F$ | $p$ |
|---|---|---|---|---|---|
| Modelo | 279.73 | 5 | 55.95 | 2.37 | 0.1329 |
| Mezcla lineal | 29.13 | 2 | 14.56 | 0.62 | 0.5630 |
| AB | 72.61 | 1 | 72.61 | 3.08 | 0.1174 |
| AC | 179.67 | 1 | 179.67 | 7.62 | 0.0247 |
| BC | 8.26 | 1 | 8.26 | 0.35 | 0.5703 |
| Residual | 188.63 | 8 | 23.58 | | |
| Falta de ajuste | 63.63 | 4 | 15.91 | 0.51 | 0.7354 |
| Error puro | 125.00 | 4 | 31.25 | | |
| Total corr. | 468.36 | 13 | | | |

$s=4.86$, media 24.79, CV 19.59, PRESS 638.60, $R^2=0.5973$, $R^2_{aj}=0.3455$,
$R^2_{pred}=-0.3635$, precisión adecuada 4.975.

$$\widehat{\text{dureza}} = 23.81A+16.40B+29.45C+44.42AB-44.01AC+13.80BC$$

Errores estándar: 3.36, 7.68, 3.36, 25.31, 15.94, 23.32.

**Sólidos** (tabla 11-16):

| Fuente | SC | g.l. | CM | $F$ | $p$ |
|---|---|---|---|---|---|
| Modelo | 4297.94 | 5 | 859.59 | 25.78 | <0.0001 |
| Mezcla lineal | 2931.09 | 2 | 1465.66 | 43.95 | <0.0001 |
| AB | 211.20 | 1 | 211.20 | 6.33 | 0.0360 |
| AC | 285.67 | 1 | 285.67 | 8.57 | 0.0191 |
| BC | 1036.72 | 1 | 1036.72 | 31.09 | 0.0005 |
| Residual | 266.79 | 8 | 33.35 | | |
| Falta de ajuste | 139.92 | 4 | 34.98 | 1.10 | 0.4633 |
| Error puro | 126.86 | 4 | 31.72 | | |
| Total corr. | 4564.73 | 13 | | | |

$s=5.77$, media 33.01, CV 17.49, PRESS 991.86, $R^2=0.9416$, $R^2_{aj}=0.9050$,
$R^2_{pred}=0.7827$, precisión adecuada 15.075.

$$\widehat{\text{sólidos}} = 26.53A+46.60B+73.23C-75.76AB-55.50AC-154.61BC$$

Errores estándar: 3.99, 9.14, 3.99, 30.11, 18.96, 27.73.

- Conclusión: se superponen los contornos dureza = 25 y sólidos = 30 (fig. 11-39); la región
  factible queda cerca del centro de la región restringida y admite varias formulaciones.
- Advertencia propia al validar: el texto afirma que ambos modelos cuadráticos "se ajustan muy
  bien", pero la tabla 11-15 muestra que el de dureza **no** es globalmente significativo
  ($p=0.1329$, $R^2_{pred}<0$); solo AC es significativo. El de sólidos sí es bueno.

---

## 11-6 Operación evolutiva — EVOP (págs. 484–488)

### Qué problema resuelve

La MSR se aplica normalmente en planta piloto y una sola vez. Al escalar a producción el óptimo se
distorsiona, y aunque se arranque en el óptimo el proceso **deriva** con el tiempo (materias primas,
ambiente, personal). **EVOP** (Box) es un método de **monitoreo y mejora continua del proceso a
escala completa**, ejecutado por el personal de manufactura como rutina, que:

- introduce de manera sistemática **cambios pequeños** en las variables de operación, lo bastante
  pequeños para no perturbar seriamente rendimiento, calidad o cantidad, pero lo bastante grandes
  para que, acumulando ciclos, se detecten mejoras;
- no exige cambios grandes ni bruscos que interrumpan la producción.

### Diseño y terminología

- Diseño: un $2^k$ **más un punto central** situado en las mejores condiciones de operación
  actuales. En la práctica $k=2$ o $3$.
- **Ciclo**: una observación en cada punto del diseño. Tras cada ciclo se actualizan promedios,
  efectos e interacciones.
- **Fase**: conjunto de ciclos alrededor de un mismo centro; termina cuando un efecto resulta
  significativo y se decide mover las condiciones de operación. La siguiente fase se centra en las
  nuevas condiciones.
- **Cambio en la media (CIM)**: comparación del centro con los $2^k$ puntos periféricos; mide
  curvatura. Si el proceso está centrado en un máximo, la respuesta del centro supera
  significativamente a la periferia.

Numeración de puntos para $2^2$ (fig. 11-40): (1) centro; (2) $(-,-)$; (3) $(+,+)$; (4) $(+,-)$;
(5) $(-,+)$. Cada ciclo se corre en orden 1, 2, 3, 4, 5.

### Hoja de cálculo EVOP ($k=2$), ciclo $n$

Para cada condición $i=1,\dots,5$:

| Renglón | Cálculo |
|---|---|
| (i) | Suma del ciclo anterior |
| (ii) | Promedio del ciclo anterior, $\bar y_i(n-1)$ |
| (iii) | Nuevas observaciones, $y_i(n)$ |
| (iv) | Diferencias (ii) − (iii) |
| (v) | Nuevas sumas (i) + (iii) |
| (vi) | Nuevos promedios $\bar y_i = (\text{v})/n$ |

**Efectos** (con los promedios vigentes):

$$\text{Efecto de } x_1=\tfrac12(\bar y_3+\bar y_4-\bar y_2-\bar y_5)$$

$$\text{Efecto de } x_2=\tfrac12(\bar y_3+\bar y_5-\bar y_2-\bar y_4)$$

$$\text{Interacción } x_1x_2=\tfrac12(\bar y_2+\bar y_3-\bar y_4-\bar y_5)$$

$$\text{CIM}=\tfrac15(\bar y_2+\bar y_3+\bar y_4+\bar y_5-4\bar y_1)$$

**Desviación estándar** (método del rango; disponible desde el ciclo 2):

1. Rango de (iv): $R_D=\max-\min$ de las diferencias.
2. Nueva $S = R_D \times f_{k,n}$.
3. Nueva suma de $S$ = suma anterior de $S$ + nueva $S$.
4. Nuevo promedio de $S$ = (nueva suma de $S$)$/(n-1)$. Este promedio es el $S$ que entra en los
   límites.

**Límites de error (≈ 95 %, dos desviaciones estándar)**:

| Para | Límite |
|---|---|
| Nuevos promedios | $\pm\dfrac{2}{\sqrt n}S$ |
| Nuevos efectos | $\pm\dfrac{2}{\sqrt n}S$ |
| Cambio en la media | $\pm\dfrac{1.78}{\sqrt n}S$ |

**Regla de decisión**: si un efecto excede su límite de error se considera real y se justifica
cambiar las condiciones de operación (nueva fase); si ninguno lo excede se sigue con otro ciclo.

### Justificación de las fórmulas

- Varianza de un efecto del $2^2$ sobre promedios de $n$ ciclos: $\sigma^2/n$ → límites
  $\pm 2\sigma/\sqrt n$.
- $V(\text{CIM})=\dfrac{1}{25}\left(4\sigma^2_{\bar y}+16\sigma^2_{\bar y}\right)=\dfrac{20}{25}\dfrac{\sigma^2}{n}$
  → límites $\pm 2\sqrt{20/25}\,\sigma/\sqrt n=\pm1.78\,\sigma/\sqrt n$. (En el libro aparece impreso
  "$5\sigma^2_{\bar y}+16\sigma^2_{\bar y}$"; para que el total sea $20/25$ debe ser $4+16$.)
- Las diferencias del renglón (iv) son $y_i(n)-\bar y_i(n-1)$, con

$$V[y_i(n)-\bar y_i(n-1)]\equiv\sigma_D^2=\sigma^2\left[1+\frac{1}{n-1}\right]=\sigma^2\frac{n}{n-1}$$

- Con $\hat\sigma_D=R_D/d_2$ ($d_2$ depende del número $k$ de diferencias):

$$\hat\sigma=\sqrt{\frac{n-1}{n}}\,\frac{R_D}{d_2}=f_{k,n}R_D\equiv S$$

  donde $k$ = número de puntos del diseño ($k=5$ para $2^2$ + centro; $k=9$ para $2^3$ + centro).

**Tabla 11-21 — valores de $f_{k,n}$**

| $n$ | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|
| $k=5$ | 0.30 | 0.35 | 0.37 | 0.38 | 0.39 | 0.40 | 0.40 | 0.40 | 0.41 |
| $k=9$ | 0.24 | 0.27 | 0.29 | 0.30 | 0.31 | 0.31 | 0.31 | 0.32 | 0.32 |
| $k=10$ | 0.23 | 0.26 | 0.28 | 0.29 | 0.30 | 0.30 | 0.30 | 0.31 | 0.31 |

### Recomendaciones

- La retroalimentación a operadores y supervisores es parte esencial: se mantiene a la vista un
  **tablero de información EVOP** (tabla 11-20) con los promedios vigentes en cada punto, los
  efectos con sus límites del 95 % y la desviación estándar.
- Para $k=3$ ver Box y Draper (formas y hojas de trabajo); Myers y Montgomery tratan la
  implementación en computadora.

### Ejemplo 11-5 — EVOP con temperatura y presión

Proceso químico; respuesta: rendimiento (maximizar). Centro actual $x_1=250$ °F, $x_2=145$ psi;
diseño $2^2$ con temperatura 245/255 y presión 140/150 más centro.

| Ciclo | Obs. (1) | (2) | (3) | (4) | (5) |
|---|---|---|---|---|---|
| 1 | 84.5 | 84.2 | 84.9 | 84.5 | 84.3 |
| 2 | 84.9 | 84.6 | 85.9 | 83.5 | 84.0 |
| 3 | 85.0 | 84.0 | 86.6 | 84.9 | 85.2 |

| Ciclo $n$ | Promedios (1)…(5) | Temp. | Presión | $T\times P$ | CIM | $R_D$ | $S$ | Límite efectos | Límite CIM |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 84.5, 84.2, 84.9, 84.5, 84.3 | 0.45 | 0.25 | 0.15 | 0.02 | — | — | — | — |
| 2 | 84.70, 84.40, 85.40, 84.00, 84.15 | 0.43 | 0.58 | 0.83 | −0.17 | 2.0 | 0.60 | ±0.85 | ±0.76 |
| 3 | 84.80, 84.27, 85.80, 84.30, 84.50 | 0.67 | 0.87 | 0.64 | −0.07 (*) | 1.60 | 0.58 | ±0.67 | ±0.60 |

(*) En la hoja de cálculo (tabla 11-19) el CIM del ciclo 3 es −0.07, valor que se reproduce con los
promedios impresos; el tablero (tabla 11-20) lo muestra como 0.07, sin signo (pág. 487).

- Ciclo 1: no hay estimación de $\sigma$.
- Ciclo 2: diferencias (iv) = −0.4, −0.4, −1.0, +1.0, 0.3; $R_D=2.0$; $S=2.0(0.30)=0.60$. Ningún
  efecto excede su límite → no se cambia nada.
- Ciclo 3: diferencias −0.30, +0.40, −1.20, −0.90, −1.05; $R_D=1.60$; nueva $S=1.60(0.35)=0.56$;
  suma 1.16; promedio $S=0.58$. La presión (0.87) excede ±0.67 y la temperatura (0.67) iguala el
  límite → se justifica cambiar las condiciones.
- Decisión: iniciar la fase 2 centrada en el punto (3), es decir 255 °F y 150 psi. (El libro
  imprime "$x_1=225$ °F"; por la fig. 11-40 el punto (3) es 255 °F — errata aparente, pág. 486.)

---

## 11-7 Diseño robusto (págs. 488–500)

### 11-7.1 Antecedentes y enfoque de Taguchi

**Objetivos del diseño robusto** (cualquiera de estos):

1. Sistemas (productos o procesos) insensibles a factores ambientales que afectan el desempeño en
   campo (p. ej. pintura de exteriores frente al clima).
2. Productos insensibles a la variabilidad transmitida por sus componentes (p. ej. amplificador
   frente a tolerancias de resistores y transistores).
3. Procesos cuyo producto quede lo más cerca posible del nominal aunque algunas variables del
   proceso o de las materias primas no puedan controlarse con precisión.
4. Condiciones de operación que centren las características críticas en el objetivo **y** minimicen
   la variabilidad alrededor de él (p. ej. espesor de óxido en obleas: media en el objetivo y
   uniformidad).

**Problema del diseño paramétrico robusto (RPD)**, Taguchi, inicios de los 80. Se clasifican las
variables en:

- **Variables de control** (controlables), $x$.
- **Variables de ruido** (no controlables en operación normal), $z$. Supuesto clave: aunque no se
  controlen a escala completa, **sí pueden controlarse para los fines del experimento**.

Meta: hallar los niveles de las variables de control que minimizan la variabilidad transmitida por
las de ruido, con la media en el objetivo.

**Estrategia experimental de Taguchi: arreglo cruzado**

- **Arreglo interior**: diseño ortogonal para los factores de control.
- **Arreglo exterior**: diseño ortogonal separado para los factores de ruido.
- **Arreglo cruzado**: cada corrida del interior se ejecuta en todas las combinaciones del exterior.

Ejemplo de Byrne y Taguchi (tabla 11-22), conector elastomérico en tubo de nylon, respuesta = fuerza
de separación:

| | Factores | Diseño |
|---|---|---|
| Control (3 niveles) | $A$ interferencia, $B$ espesor de pared del conector, $C$ profundidad de inserción, $D$ porcentaje de adhesivo | $3^{4-2}$ (9 corridas, el $L_9$) |
| Ruido (2 niveles) | $E$ tiempo, $F$ temperatura y $G$ humedad relativa de acondicionamiento | $2^3$ (8 corridas) |

Total $9\times 8=72$ observaciones.

**Análisis de Taguchi**: para cada corrida del arreglo interior se resumen las observaciones del
exterior con (1) el **promedio** y (2) una **relación señal a ruido** (SN) que pretende combinar
media y varianza y que se define de modo que su **maximización** minimice la variabilidad
transmitida. Luego se buscan los niveles de control que dan media ≈ objetivo y SN máxima.

> El texto del capítulo **no da las fórmulas** de las relaciones SN (remite al material
> suplementario). Complemento externo al capítulo, para referencia: las tres formas usuales son
> nominal-es-mejor $SN_T=10\log_{10}(\bar y^2/s^2)$, mayor-es-mejor
> $SN_L=-10\log_{10}\big(\tfrac1n\sum 1/y_i^2\big)$ y menor-es-mejor
> $SN_S=-10\log_{10}\big(\tfrac1n\sum y_i^2\big)$.

**Críticas de Montgomery**

1. **Tamaño del experimento**: el cruce de arreglos produce diseños muy grandes (7 factores → 72
   corridas en el ejemplo).
2. **Arreglo interior de resolución III**: pese a las 72 corridas, el $3^{4-2}$ no da **ninguna**
   información sobre interacciones entre factores de control, y los efectos principales quedan
   fuertemente aliados con interacciones de dos factores.
3. **Relaciones SN problemáticas**: maximizarlas no garantiza minimizar la variabilidad (confunden
   efectos de localización y dispersión).
4. Históricamente, la metodología se difundió en Occidente sin revisión estadística adecuada; la
   conclusión de finales de los 80 es que la **filosofía de ingeniería y el objetivo del RPD son
   sólidos**, pero la estrategia experimental y el análisis de datos tienen fallas de fondo
   (referencias: Box; Box, Bisgaard y Fung; Hunter; Myers y Montgomery; Pignatiello y Ramberg; panel
   de Nair et al. en *Technometrics*).

**Lo que sí aporta el arreglo cruzado**: información sobre las **interacciones control × ruido**,
que son la clave del RPD (fig. 11-41):

- Sin interacción $x\times z$: las rectas de $y$ contra $z$ son paralelas para los niveles de $x$;
  la variabilidad transmitida por $z$ es la misma con cualquier $x$ → no hay nada que robustecer.
- Con interacción $x\times z$ fuerte: en un nivel de $x$ la pendiente respecto de $z$ es casi nula y
  la variabilidad transmitida se reduce mucho.

**Regla**: sin al menos una interacción control × ruido **no existe problema de diseño robusto**.

### 11-7.2 Enfoque de la superficie de respuesta

**Idea**: ajustar un único **modelo de respuesta** (o de reacción) que incluya factores de control,
factores de ruido y sus interacciones, y derivar de él un modelo para la media y otro para la
varianza.

**Modelo ilustrativo** (dos controlables, un ruido; variables codificadas, centradas en 0 con
límites $\pm a$):

$$y=\beta_0+\beta_1x_1+\beta_2x_2+\beta_{12}x_1x_2+\gamma_1z_1+\delta_{11}x_1z_1+\delta_{21}x_2z_1+\varepsilon \tag{11-28}$$

- $\gamma_1$: efecto principal del ruido; $\delta_{11},\delta_{21}$: interacciones control × ruido.
- Si $\delta_{11}=\delta_{21}=0$ no hay problema de diseño robusto.

**Diseño de arreglo combinado**: controlables y ruido van en **un solo diseño** (factorial,
fraccionado, DCC…), evitando la estructura interior/exterior. Ventaja: menos corridas y posibilidad
de estimar interacciones control × control.

**Supuestos sobre el ruido**: las $z$ son variables aleatorias (aunque se fijen durante el
experimento), codificadas con $E(z)=0$, $V(z)=\sigma_z^2$, covarianzas nulas entre ellas y con
$\varepsilon$.

**Modelo de la media** (esperanza respecto de $z_1$ y $\varepsilon$):

$$E_z(y)=\beta_0+\beta_1x_1+\beta_2x_2+\beta_{12}x_1x_2$$

**Modelo de la varianza por transmisión (propagación) del error**: expansión de Taylor de primer
orden alrededor de $z_1=0$,

$$y\cong\beta_0+\beta_1x_1+\beta_2x_2+\beta_{12}x_1x_2+(\gamma_1+\delta_{11}x_1+\delta_{21}x_2)z_1+R+\varepsilon$$

despreciando el residuo $R$ y aplicando el operador varianza:

$$V_z(y)=\sigma_z^2(\gamma_1+\delta_{11}x_1+\delta_{21}x_2)^2+\sigma^2$$

Observaciones:

1. Ambos modelos contienen **únicamente variables controlables** → se puede fijar $x$ para llevar la
   media al objetivo y minimizar la variabilidad transmitida.
2. El modelo de varianza incluye los **coeficientes de interacción control × ruido**: por ahí
   influye el ruido.
3. El modelo de la varianza es **cuadrático** en las controlables.
4. Salvo $\sigma^2$, es el **cuadrado de la pendiente** del modelo de respuesta en la dirección del
   ruido.

**Procedimiento operativo**

1. Correr el experimento (arreglo combinado) y ajustar un modelo de respuesta como 11-28.
2. Sustituir los coeficientes por sus estimaciones de mínimos cuadrados y $\sigma^2$ por el
   **cuadrado medio de los residuales** del ajuste. $\sigma_z^2$ debe conocerse o suponerse (si los
   niveles ±1 del ruido se fijaron a ±1 desviación estándar, $\sigma_z^2=1$).
3. Optimizar simultáneamente media y varianza con los métodos de respuestas múltiples de 11-3.4
   (superposición de contornos, optimización restringida, deseabilidad).

**Generalización** ($k$ controlables, $r$ de ruido):

$$y(\mathbf x,\mathbf z)=f(\mathbf x)+h(\mathbf x,\mathbf z)+\varepsilon \tag{11-29}$$

$$h(\mathbf x,\mathbf z)=\sum_{i=1}^{r}\gamma_iz_i+\sum_{i=1}^{k}\sum_{j=1}^{r}\delta_{ij}x_iz_j$$

- $f(\mathbf x)$: solo controlables; opciones lógicas: primer orden con interacción o segundo orden.
- Con ruido de media 0, varianza $\sigma_z^2$ y covarianzas nulas:

$$E_z[y(\mathbf x,\mathbf z)]=f(\mathbf x) \tag{11-30}$$

$$V_z[y(\mathbf x,\mathbf z)]=\sigma_z^2\sum_{i=1}^{r}\left[\frac{\partial y(\mathbf x,\mathbf z)}{\partial z_i}\right]^2+\sigma^2 \tag{11-31}$$

  (Myers y Montgomery dan una forma más general con el operador de varianza condicional.)

**POE** (*propagation of error*): Design-Expert grafica la **raíz cuadrada** del modelo de
varianza, es decir, la desviación estándar transmitida a la respuesta como función de las
controlables.

### Ejemplo 11-6 — Rapidez de filtración (ejemplo 6-2 reinterpretado)

- Diseño $2^4$ no replicado en planta piloto. Se supone que la temperatura ($A$) es difícil de
  controlar a escala completa → **ruido** $z_1$; presión ($B$) $=x_1$, concentración ($C$) $=x_2$,
  velocidad de agitación ($D$) $=x_3$ son controlables. Es un **arreglo combinado**.
- Modelo de respuesta (coeficiente = efecto/2; efectos $A=21.625$, $C=9.875$, $D=14.625$,
  $AC=-18.125$, $AD=16.625$):

$$\hat y(\mathbf x,z_1)=70.06+10.81z_1+4.94x_2+7.31x_3-9.06x_2z_1+8.31x_3z_1$$

- Modelo de la media: $E_z[y]=70.06+4.94x_2+7.31x_3$.
- Modelo de la varianza:

$$V_z[y]=\sigma_z^2(10.81-9.06x_2+8.31x_3)^2+\sigma^2$$

  Con $\sigma_z^2=1$ (niveles del ruido a ±1 desviación estándar) y $\hat\sigma^2=19.51$ (CM
  residual):

$$V_z[y]=136.42-195.88x_2+179.66x_3-150.58x_2x_3+82.08x_2^2+69.06x_3^2$$

- Resultados (figs. 11-42 a 11-44; temperatura = 0, presión = 0): la media crece con concentración y
  agitación; la POE va de ≈ 4.4 a ≈ 28.5 y es menor con concentración alta y agitación baja.
  Objetivo: media ≈ 75 con variabilidad mínima → **concentración en el nivel alto y velocidad de
  agitación cerca del nivel intermedio** (región con $\hat y\ge 75$ y POE ≤ 5.5).
- Nota: en las figuras de Design-Expert los ejes están rotulados "$x_3$ = concentración" y "$x_4$ =
  velocidad de agitación" (numeración original de los factores), distinta de la del texto.

### Ejemplo 11-7 — Semiconductores: modelo de segundo orden con tres ruidos

- Dos controlables ($x_1,x_2$) y tres de ruido ($z_1,z_2,z_3$). Arreglo combinado de **23 corridas**
  (tabla 11-23): variante de un DCC de 5 factores con porción cúbica $2^{5-1}$ (16 corridas), puntos
  axiales **solo** en las controlables ($\pm2$; 4 corridas; se eliminan los axiales de las variables
  de ruido) y 3 puntos centrales.
- Soporta: segundo orden en las controlables + efectos principales de ruido + interacciones control
  × ruido.

$$\hat y=30.37-2.92x_1-4.13x_2+2.60x_1^2+2.18x_2^2+2.87x_1x_2+2.73z_1-2.33z_2+2.33z_3-0.27x_1z_1+0.89x_1z_2+2.58x_1z_3+2.01x_2z_1-1.43x_2z_2+1.56x_2z_3$$

- Modelo de la media: $E_z[y]=30.37-2.92x_1-4.13x_2+2.60x_1^2+2.18x_2^2+2.87x_1x_2$.
- Modelo de la varianza según el libro ($\sigma_z^2=1$):

$$V_z[y]=19.26+3.20x_1+12.45x_2+7.52x_1^2+8.52x_2^2+2.21x_1x_2$$

- Objetivo: media ≤ 30 y desviación estándar ≤ 5. Superponiendo contornos de media y POE (fig.
  11-47) queda una región factible estrecha cerca del centro (aprox. $x_1$ entre −0.3 y 1 y $x_2$
  entre −0.3 y 0.3, leído de la figura).
- **Duda de exactitud**: al aplicar la ec. 11-31 a los coeficientes impresos, con pendientes
  $(2.73-0.27x_1+2.01x_2)$, $(-2.33+0.89x_1-1.43x_2)$ y $(2.33+2.58x_1+1.56x_2)$, los términos
  cuadráticos puros coinciden (7.52 y 8.52), pero los términos lineales y el cruzado salen al
  **doble** de lo impreso: $6.40x_1$, $24.91x_2$ y $4.42x_1x_2$. El modelo de varianza impreso
  parece omitir el factor 2 de los dobles productos (pág. 497). Al validar con software, esperar los
  valores duplicados. La constante 19.26 implica $\hat\sigma^2\approx0.95$ (suma de cuadrados de
  $\gamma$ = 18.31).

### Reglas prácticas del 11-7

- Identificar y modelar las interacciones control × ruido es la clave; sin ellas no hay RPD.
- Preferir arreglos combinados a los cruzados: menos corridas y permiten estimar interacciones entre
  factores de control.
- El análisis descansa en un buen modelo de respuesta: verificar su adecuación antes de derivar
  media y varianza.
- Alternativa cuando hay réplicas o mediciones repetidas (problemas 11-14, 11-33, 11-34): modelar
  directamente $\bar y$ y $s^2$ (o $\ln s^2$, o $s$) como dos respuestas y optimizar ambas.

---

## 11-8 Problemas (págs. 500–510)

Solo ubicación temática (no se resumen):

| Problemas | Tema |
|---|---|
| 11-1 a 11-7 | Ascenso/descenso más pronunciado (parte A) |
| 11-8 a 11-12 | Modelos de segundo orden, análisis canónico, DCC, hexagonal, Box-Behnken, dos respuestas |
| 11-13 | Región factible con dos respuestas lineales |
| 11-14 | DCC con media y varianza por corrida; modelar $\bar y$, $s^2$ y $\ln(s^2)$ |
| 11-15 a 11-20 | Ortogonalidad, rotabilidad ($\alpha=n_F^{1/4}$), bloques ortogonales en DCC |
| 11-21 | **EVOP**: 4 ciclos, concentración 30/31/32 y temperatura 140/142/144 °F |
| 11-22 | Matriz alias $\mathbf A=(\mathbf X_1'\mathbf X_1)^{-1}\mathbf X_1'\mathbf X_2$ |
| 11-23 | Hunter: $3^2$ frente a $3^{4-2}$ ($L_9$) con los mismos datos; alias de efectos principales con interacciones |
| 11-24 a 11-28 | Criterios D, A, G, V; diseños en regiones restringidas |
| 11-29 | **Mezcla** restringida de 3 componentes, diseño D-óptimo con $n=14$ y $n=12$ |
| 11-30 | **Mezcla** de gasolina, 3 componentes, 10 puntos (símplex reticular aumentado con axiales y centroide) |
| 11-31, 11-32 | **Diseño robusto**: modelo de respuesta, media, varianza/POE con un factor de ruido |
| 11-33 | $3^3$ con media y desviación estándar como respuestas |
| 11-34 | Variación del ejemplo 6-2: $C$, $D$ controlables y $A$ ruido; modelar $\bar y$ y $\ln(s^2)$ y comparar con el ejemplo 11-6 |
