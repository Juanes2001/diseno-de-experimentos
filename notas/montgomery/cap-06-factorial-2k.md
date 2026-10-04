# Capítulo 6 — Diseño factorial 2^k

> Montgomery, págs. 218–286 (texto: 218–276; problemas 6-7: 276–286)

Ficha técnica de consulta. Es la base directa del tema 6 (factoriales fraccionados, cap. 8):
toda la maquinaria de contrastes, tabla de signos, aritmética módulo 2, gráfica normal de
efectos y proyección se reutiliza allí sin cambios.

Convenciones usadas en toda la ficha:

- $k$ = número de factores, $n$ = número de réplicas por combinación, $N = n2^k$ = total de corridas.
- Las letras minúsculas `(1), a, b, ab, …` denotan **a la vez** la combinación de tratamientos
  y el **total** de las $n$ observaciones tomadas en ella.
- Las mayúsculas `A, B, AB, …` denotan el **efecto** (principal o de interacción).

---

## 6-1 Introducción

**Qué es.** Factorial completo con $k$ factores, cada uno a dos niveles ("bajo"/"alto"), que
pueden ser cuantitativos (dos temperaturas) o cualitativos (dos máquinas, presencia/ausencia).
Una réplica completa requiere $2\times2\times\cdots\times2 = 2^k$ observaciones.

**Supuestos de todo el capítulo:**

1. Factores **fijos**.
2. Diseño **completamente aleatorizado**.
3. Supuestos usuales de **normalidad** (errores NID$(0,\sigma^2)$).
4. Respuesta aproximadamente **lineal** en el rango de niveles elegido (solo hay dos niveles
   por factor). La sección 6-6 da una prueba de este supuesto (puntos centrales).

**Cuándo se usa.** Etapas iniciales de la experimentación, cuando hay muchos factores
candidatos: es el factorial completo con el menor número de corridas para $k$ factores, por lo
que es el diseño típico de los **experimentos de tamizado (screening) o selección de factores**.

---

## 6-2 El diseño 2²

### Notación

| Corrida | A | B | Etiqueta | Significado |
|---|---|---|---|---|
| 1 | − | − | `(1)` | A bajo, B bajo |
| 2 | + | − | `a` | A alto, B bajo |
| 3 | − | + | `b` | A bajo, B alto |
| 4 | + | + | `ab` | A alto, B alto |

Regla: el nivel alto de un factor se indica con su letra minúscula; el nivel bajo, con la
ausencia de la letra; `(1)` = todos los factores en nivel bajo. El orden `(1), a, b, ab` es el
**orden estándar** (u **orden de Yates**).

### Efectos (ecs. 6-1 a 6-3)

El efecto promedio de un factor es el cambio en la respuesta al pasar de su nivel bajo al alto,
promediado sobre los niveles del otro factor.

$$A = \frac{1}{2n}\{[ab-b]+[a-(1)]\} = \frac{1}{2n}[ab+a-b-(1)] = \bar y_{A^+}-\bar y_{A^-} \tag{6-1}$$

$$B = \frac{1}{2n}\{[ab-a]+[b-(1)]\} = \frac{1}{2n}[ab+b-a-(1)] = \bar y_{B^+}-\bar y_{B^-} \tag{6-2}$$

$$AB = \frac{1}{2n}\{[ab-b]-[a-(1)]\} = \frac{1}{2n}[ab+(1)-a-b] \tag{6-3}$$

- $AB$ = diferencia promedio entre el efecto de $A$ con $B$ alto y el efecto de $A$ con $B$
  bajo (o, de forma equivalente, intercambiando los papeles de $A$ y $B$).
- Interpretación geométrica (cuadrado de la fig. 6-1): $A$ = promedio del lado derecho menos
  el izquierdo; $B$ = lado superior menos inferior; $AB$ = diagonal `ab,(1)` menos diagonal `a,b`.

### Contrastes y sumas de cuadrados (ecs. 6-4 a 6-10)

La cantidad entre corchetes es un **contraste** de los totales de tratamiento, llamado también
**efecto total**:

$$\text{Contraste}_A = ab + a - b - (1) \tag{6-4}$$

Los tres contrastes ($A$, $B$, $AB$) son **ortogonales**. Por la regla general de la SS de un
contraste (ec. 3-29: contraste² dividido por $n\sum c_i^2$):

$$SS_A=\frac{[ab+a-b-(1)]^2}{4n},\qquad SS_B=\frac{[ab+b-a-(1)]^2}{4n},\qquad SS_{AB}=\frac{[ab+(1)-a-b]^2}{4n} \tag{6-5 a 6-7}$$

$$SS_T=\sum_{i=1}^{2}\sum_{j=1}^{2}\sum_{k=1}^{n}y_{ijk}^2-\frac{y_{...}^2}{4n}\quad(4n-1\ \text{g.l.}) \tag{6-9}$$

$$SS_E = SS_T-SS_A-SS_B-SS_{AB}\quad(4(n-1)\ \text{g.l.}) \tag{6-10}$$

Cada efecto tiene 1 g.l.; $F_0 = MS_{\text{efecto}}/MS_E \sim F_{1,\,4(n-1)}$ bajo $H_0$: efecto = 0.

### Tabla de signos (tabla 6-2)

| Combinación | I | A | B | AB |
|---|---|---|---|---|
| `(1)` | + | − | − | + |
| `a` | + | + | − | − |
| `b` | + | − | + | − |
| `ab` | + | + | + | + |

- Los coeficientes de un contraste son siempre $+1$ o $-1$.
- La columna de una interacción es el **producto renglón a renglón** de las columnas de los
  efectos principales correspondientes.
- $I$ (solo signos +) representa el total o promedio del experimento.
- Para obtener un contraste: multiplicar la columna del efecto por los totales de tratamiento y sumar.

### Ejemplo de la sección (proceso químico, sin número)

2² con $n=3$. $A$ = concentración del reactivo (15 %, 25 %), $B$ = catalizador (1 lb, 2 lb),
respuesta = rendimiento. Totales: `(1)`=80, `a`=100, `b`=60, `ab`=90 (gran total 330).

- Efectos: $A = 8.33$, $B = -5.00$, $AB = 1.67$.
- Contrastes: 50, −30, 10 → $SS_A=208.33$, $SS_B=75.00$, $SS_{AB}=8.33$;
  $SS_T = 9398.00-9075.00=323.00$; $SS_E=31.34$.

Tabla 6-1 (ANOVA):

| Fuente | SS | g.l. | MS | $F_0$ | Valor P |
|---|---|---|---|---|---|
| A | 208.33 | 1 | 208.33 | 53.15 | 0.0001 |
| B | 75.00 | 1 | 75.00 | 19.13 | 0.0024 |
| AB | 8.33 | 1 | 8.33 | 2.13 | 0.1826 |
| Error | 31.34 | 8 | 3.92 | | |
| Total | 323.00 | 11 | | | |

Conclusión: ambos efectos principales significativos, sin interacción. Subir $A$ aumenta el
rendimiento; subir $B$ lo reduce.

### Modelo de regresión

En un $2^k$ el modelo de regresión es más natural que el modelo de efectos:

$$y=\beta_0+\beta_1x_1+\beta_2x_2+\varepsilon$$

(se añade $\beta_{12}x_1x_2$ si la interacción es relevante). Las $x_j$ son **variables
codificadas** en $\pm1$:

$$x_j=\frac{\text{valor natural}-(\text{bajo}+\text{alto})/2}{(\text{alto}-\text{bajo})/2}$$

En el ejemplo: $x_1=(\text{Conc}-20)/5$, $x_2=(\text{Cat}-1.5)/0.5$.

**Regla clave:**

- $\hat\beta_0$ = gran promedio de todas las observaciones.
- $\hat\beta_j$ = **efecto / 2**. Razón: el coeficiente mide el cambio en $y$ por cambio
  unitario en $x$, mientras que el efecto corresponde a un cambio de 2 unidades (de −1 a +1).
- Estas estimaciones coinciden con las de **mínimos cuadrados**.

Ejemplo: $\hat y = 27.5 + (8.33/2)x_1 + (-5.00/2)x_2$. En variables naturales:
$\hat y = 18.33 + 0.8333\,\text{Concentración} - 5.00\,\text{Catalizador}$.

### Residuales y adecuación del modelo

$e = y - \hat y$, con $\hat y$ obtenido del modelo de regresión ajustado en cada punto del
diseño. En el ejemplo los valores predichos son 25.835 `(1)`, 34.165 `a`, 20.835 `b`,
29.165 `ab`; los 12 residuales van de −2.835 a 2.165. Diagnósticos (fig. 6-2): gráfica de
probabilidad normal de residuales y residuales contra predichos; ambas satisfactorias.

### Superficie de respuesta

El modelo ajustado genera la superficie de respuesta y la gráfica de contorno (fig. 6-3).
Un modelo de **primer orden** (solo efectos principales) da un **plano** y contornos rectos
paralelos. Sirve para encontrar la **dirección de mejoramiento potencial**; el procedimiento
formal (ascenso más pronunciado) está en el cap. 11.

---

## 6-3 El diseño 2³

### Notaciones y matriz del diseño

Ocho corridas, representación geométrica en un cubo (fig. 6-4). Tres notaciones equivalentes:
geométrica ($\pm$), etiquetas en minúsculas y binaria (0/1).

| Corrida | A | B | C | Etiqueta | A B C (0/1) |
|---|---|---|---|---|---|
| 1 | − | − | − | `(1)` | 0 0 0 |
| 2 | + | − | − | `a` | 1 0 0 |
| 3 | − | + | − | `b` | 0 1 0 |
| 4 | + | + | − | `ab` | 1 1 0 |
| 5 | − | − | + | `c` | 0 0 1 |
| 6 | + | − | + | `ac` | 1 0 1 |
| 7 | − | + | + | `bc` | 0 1 1 |
| 8 | + | + | + | `abc` | 1 1 1 |

Orden estándar: `(1), a, b, ab, c, ac, bc, abc`. Hay 7 g.l. entre las 8 combinaciones:
3 para efectos principales, 3 para interacciones dobles y 1 para $ABC$.

### Efectos (ecs. 6-11 a 6-17)

Todos tienen la forma (contraste)$/(4n)$:

$$A=\frac{1}{4n}[a+ab+ac+abc-(1)-b-c-bc]=\bar y_{A^+}-\bar y_{A^-} \tag{6-11}$$

$$B=\frac{1}{4n}[b+ab+bc+abc-(1)-a-c-ac] \tag{6-12}$$

$$C=\frac{1}{4n}[c+ac+bc+abc-(1)-a-b-ab] \tag{6-13}$$

$$AB=\frac{1}{4n}[abc-bc+ab-b-ac+c-a+(1)] \tag{6-14}$$

$$AC=\frac{1}{4n}[(1)-a+b-ab-c+ac-bc+abc] \tag{6-15}$$

$$BC=\frac{1}{4n}[(1)+a-b-ab-c-ac+bc+abc] \tag{6-16}$$

$$ABC=\frac{1}{4n}[abc-bc-ac+c-ab+b+a-(1)] \tag{6-17}$$

Definiciones conceptuales:

- Efecto principal: promedio de las 4 corridas de una cara del cubo menos las 4 de la cara opuesta.
- $AB$: **la mitad** de la diferencia entre los efectos promedio de $A$ en los dos niveles de
  $B$; geométricamente, diferencia de promedios entre dos planos diagonales del cubo.
- $ABC$: diferencia promedio entre la interacción $AB$ en los dos niveles de $C$; las corridas
  + y − forman los vértices de dos tetraedros (fig. 6-5c).

### Tabla de signos (tabla 6-3)

| Combinación | I | A | B | AB | C | AC | BC | ABC |
|---|---|---|---|---|---|---|---|---|
| `(1)` | + | − | − | + | − | + | + | − |
| `a` | + | + | − | − | − | − | + | + |
| `b` | + | − | + | − | − | + | − | + |
| `ab` | + | + | + | + | − | − | − | − |
| `c` | + | − | − | + | + | − | − | + |
| `ac` | + | + | − | − | + | + | − | − |
| `bc` | + | − | + | − | + | − | + | − |
| `abc` | + | + | + | + | + | + | + | + |

**Propiedades (fundamentales para el cap. 8):**

1. Salvo $I$, cada columna tiene igual número de signos + y −.
2. La suma de productos de signos de dos columnas cualesquiera es cero (**ortogonalidad**).
3. $I$ es el **elemento identidad**: $I\times X = X$.
4. El producto de dos columnas cualesquiera es otra columna de la tabla, con exponentes en
   **aritmética módulo 2**: $A\times B = AB$; $AB\times B = AB^2 = A$.

### Suma de cuadrados

$$SS=\frac{(\text{Contraste})^2}{8n} \tag{6-18}$$

cada una con 1 g.l. La **contribución porcentual** $SS_{\text{efecto}}/SS_T\times100$ es una
guía aproximada pero efectiva de la importancia relativa de cada término.

### Ejemplo 6-1 — Altura de llenado (2³, $n=2$)

$A$ = carbonatación (10, 12 %), $B$ = presión (25, 30 psi), $C$ = velocidad de línea
(200, 250 bpm); respuesta = desviación de la altura de llenado. Totales:
`(1)`=−4, `a`=1, `b`=−1, `ab`=5, `c`=−1, `ac`=3, `bc`=2, `abc`=11.

Tabla 6-5:

| Término | Contraste | Efecto | SS | % contribución |
|---|---|---|---|---|
| A | 24 | 3.00 | 36.00 | 46.1538 |
| B | 18 | 2.25 | 20.25 | 25.9615 |
| C | 14 | 1.75 | 12.25 | 15.7051 |
| AB | 6 | 0.75 | 2.25 | 2.88462 |
| AC | 2 | 0.25 | 0.25 | 0.320513 |
| BC | 4 | 0.50 | 1.00 | 1.28205 |
| ABC | 4 | 0.50 | 1.00 | 1.28205 |
| Error puro | | | 5.00 | 6.41026 |
| Total | | | 78.00 | |

Tabla 6-6 (ANOVA):

| Fuente | SS | g.l. | MS | $F_0$ | Valor P |
|---|---|---|---|---|---|
| A | 36.00 | 1 | 36.00 | 57.60 | <0.0001 |
| B | 20.25 | 1 | 20.25 | 32.40 | 0.0005 |
| C | 12.25 | 1 | 12.25 | 19.60 | 0.0022 |
| AB | 2.25 | 1 | 2.25 | 3.60 | 0.0943 |
| AC | 0.25 | 1 | 0.25 | 0.40 | 0.5447 |
| BC | 1.00 | 1 | 1.00 | 1.60 | 0.2415 |
| ABC | 1.00 | 1 | 1.00 | 1.60 | 0.2415 |
| Error | 5.00 | 8 | 0.625 | | |
| Total | 78.00 | 15 | | | |

Conclusión: los tres efectos principales son altamente significativos (explican más del 87 %
de la variabilidad); $AB$ es significativa solo al 10 % aproximadamente. Decisión práctica
(ej. 5-3): presión baja, velocidad alta y mejor control de la carbonatación.

Nota: en la pág. 233 el cálculo de $AC$ aparece impreso como "$\tfrac12[2]=0.25$"; es una
errata, el divisor correcto es 8.

### Modelo de regresión y superficie de respuesta (ej. 6-1)

$$\hat y = 1.00+\left(\tfrac{3.00}{2}\right)x_1+\left(\tfrac{2.25}{2}\right)x_2+\left(\tfrac{1.75}{2}\right)x_3+\left(\tfrac{0.75}{2}\right)x_1x_2$$

Al incluir el término de interacción $x_1x_2$ los contornos son **curvos** (plano "torcido",
fig. 6-7, dibujada con $x_3=+1$).

### Salida de computadora (Design-Expert, tabla 6-7) y estadísticos del modelo

**Prueba global del modelo.** $SS_{\text{Modelo}}$ = suma de las SS de todos los términos
incluidos (73.00 con 7 g.l. en el modelo completo):

$$F_0=\frac{MS_{\text{Modelo}}}{MS_E}=\frac{10.43}{0.63}=16.69\quad(P=0.0003)$$

prueba $H_0:\beta_1=\beta_2=\beta_3=\beta_{12}=\beta_{13}=\beta_{23}=\beta_{123}=0$ contra
$H_1$: al menos una $\beta\neq0$.

**Coeficientes de determinación:**

$$R^2=\frac{SS_{\text{Modelo}}}{SS_{\text{Total}}}=\frac{73.00}{78.00}=0.9359$$

$$R^2_{\text{Ajustada}}=1-\frac{SS_E/df_E}{SS_{\text{Total}}/df_{\text{Total}}}=1-\frac{5.00/8}{78.00/15}=0.8798$$

$$R^2_{\text{Predicción}}=1-\frac{\text{PRESS}}{SS_{\text{Total}}}=1-\frac{20.00}{78.00}=0.7436$$

- $R^2$ siempre crece al añadir términos, aunque no sean significativos.
- $R^2$ ajustada penaliza el tamaño del modelo y puede decrecer al añadir términos inútiles.
- PRESS (*prediction error sum of squares*): suma de cuadrados de los errores al predecir cada
  observación con un modelo ajustado sin ella; valor pequeño indica buen predictor.

**Error estándar e intervalo de confianza de un coeficiente:**

$$se(\hat\beta)=\sqrt{V(\hat\beta)}=\sqrt{\frac{MS_E}{n2^k}}=\sqrt{\frac{0.625}{2(8)}}=0.20$$

$$\hat\beta-t_{0.025,N-p}\,se(\hat\beta)\le\beta\le\hat\beta+t_{0.025,N-p}\,se(\hat\beta)$$

con $N$ = total de corridas (16) y $p$ = número de parámetros del modelo (8).

**Modelo reducido** ($A$, $B$, $C$, $AB$). El residual se parte en **error puro** (de las
réplicas, 8 g.l.) y **falta de ajuste** (SS de los términos eliminados $AC$, $BC$, $ABC$):

| Fuente | SS | g.l. | MS | F | Prob > F |
|---|---|---|---|---|---|
| Modelo | 70.75 | 4 | 17.69 | 26.84 | <0.0001 |
| A | 36.00 | 1 | 36.00 | 54.62 | <0.0001 |
| B | 20.25 | 1 | 20.25 | 30.72 | 0.0002 |
| C | 12.25 | 1 | 12.25 | 18.59 | 0.0012 |
| AB | 2.25 | 1 | 2.25 | 3.41 | 0.0917 |
| Residual | 7.25 | 11 | 0.66 | | |
| Falta de ajuste | 2.25 | 3 | 0.75 | 1.20 | 0.3700 |
| Error puro | 5.00 | 8 | 0.63 | | |
| Total | 78.00 | 15 | | | |

| Estadístico | Modelo completo | Modelo reducido |
|---|---|---|
| Desv. est. | 0.79 | 0.81 |
| $R^2$ | 0.9359 | 0.9071 |
| $R^2$ ajustada | 0.8798 | 0.8733 |
| PRESS | 20.00 | 15.34 |
| $R^2$ predicción | 0.7436 | 0.8033 |
| Adeq. Precision | 13.416 | 15.424 |

Coeficientes (codificados, iguales en ambos modelos por ortogonalidad): intercepto 1.00,
$A$ 1.50, $B$ 1.13, $C$ 0.88, $AB$ 0.38 ($AC$ 0.13, $BC$ 0.25, $ABC$ 0.25 en el completo);
error estándar 0.20 en todos; VIF = 1.00. Modelo reducido en variables naturales:
$\text{Desv} = 9.625-2.625\,\text{Carb}-1.20\,\text{Pres}+0.035\,\text{Vel}+0.15\,\text{Carb}\cdot\text{Pres}$.

Lección: eliminar términos no significativos apenas cambia $R^2$ ajustada, baja PRESS y
sube $R^2$ de predicción; los intervalos de confianza de los coeficientes se acortan un poco.
La salida incluye además diagnósticos por caso: leverage (0.313 en todos los puntos del modelo
reducido), residual studentizado, distancia de Cook y *outlier t*.

### Error estándar de los efectos e intervalos de confianza (ecs. 6-19, 6-20)

Con $n$ réplicas, la varianza de la corrida $i$ es
$S_i^2=\frac{1}{n-1}\sum_{j=1}^{n}(y_{ij}-\bar y_i)^2$ y la estimación combinada

$$S^2=\frac{1}{2^k(n-1)}\sum_{i=1}^{2^k}\sum_{j=1}^{n}(y_{ij}-\bar y_i)^2 = MS_E \tag{6-19}$$

Como Efecto = Contraste$/(n2^{k-1})$ y $V(\text{Contraste})=n2^k\sigma^2$:

$$V(\text{Efecto})=\frac{1}{(n2^{k-1})^2}\,n2^k\sigma^2=\frac{\sigma^2}{n2^{k-2}}$$

$$se(\text{Efecto})=\frac{2S}{\sqrt{n2^k}} \tag{6-20}$$

(En la pág. 241 la última línea del desarrollo de la varianza aparece como
$2\sigma/\sqrt{n2^k}$, que es en realidad la desviación estándar, no la varianza.)

- $se(\text{Efecto}) = 2\,se(\hat\beta)$.
- IC de $100(1-\alpha)$ %: $\text{Efecto}\pm t_{\alpha/2,\,N-p}\;se(\text{Efecto})$, con
  $N-p$ = g.l. del error.
- Ej. 6-1: $se = 2\sqrt{0.625}/\sqrt{2\cdot2^3}=0.40$; $t_{0.025,8}=2.31$; semiamplitud 0.92.
  Solo los intervalos de $A$ ($3.00\pm0.92$), $B$ ($2.25\pm0.92$) y $C$ ($1.75\pm0.92$)
  excluyen el cero.

### Efectos de dispersión (con réplicas)

Pregunta: ¿algún factor afecta la **variabilidad** de la respuesta? Método simple: calcular el
**rango** de las réplicas en cada vértice del cubo y graficarlo (fig. 6-8). En el ej. 6-1 los
rangos son similares (0, 1 o 2) en las ocho corridas, así que no hay evidencia de efectos de
dispersión.

---

## 6-4 El diseño general 2^k

**Modelo completo:** $k$ efectos principales, $\binom{k}{2}$ interacciones dobles,
$\binom{k}{3}$ triples, …, 1 interacción de $k$ factores: en total $2^k-1$ efectos, cada uno
con 1 g.l.

**Orden estándar:** se introduce un factor a la vez y se combina con todos los anteriores.
Para $2^4$: `(1), a, b, ab, c, ac, bc, abc, d, ad, bd, abd, cd, acd, bcd, abcd`.
En un $2^5$, `abd` = $A$, $B$, $D$ altos y $C$, $E$ bajos.

**Procedimiento de análisis (tabla 6-8):**

1. Estimar los efectos de los factores (examinar signos y magnitudes).
2. Formar el modelo inicial (el completo, si hay réplica de al menos un punto; si no, ver 6-5).
3. Realizar las pruebas estadísticas (ANOVA).
4. Refinar el modelo (eliminar términos no significativos).
5. Analizar los residuales (adecuación y supuestos; puede obligar a refinar de nuevo).
6. Interpretar los resultados (gráficas de efectos e interacciones, superficies, contornos).

**ANOVA general (tabla 6-9), $n$ réplicas:**

| Fuente | SS | g.l. |
|---|---|---|
| $k$ efectos principales $A, B, \dots, K$ | $SS_A,\dots,SS_K$ | 1 cada uno |
| $\binom{k}{2}$ interacciones dobles $AB, AC, \dots, JK$ | $SS_{AB},\dots$ | 1 cada una |
| $\binom{k}{3}$ interacciones triples $ABC,\dots,IJK$ | $SS_{ABC},\dots$ | 1 cada una |
| ⋮ | ⋮ | ⋮ |
| 1 interacción de $k$ factores $ABC\cdots K$ | $SS_{ABC\cdots K}$ | 1 |
| Error | $SS_E$ | $2^k(n-1)$ |
| Total | $SS_T$ | $n2^k-1$ |

**Contraste por expansión algebraica (ec. 6-21):**

$$\text{Contraste}_{AB\cdots K}=(a\pm1)(b\pm1)\cdots(k\pm1)$$

Signo **−** en el paréntesis si el factor **está** en el efecto, **+** si no está; se expande
con álgebra ordinaria y al final "1" se sustituye por `(1)`. Ejemplos:

- $2^3$: $\text{Contraste}_{AB}=(a-1)(b-1)(c+1)=abc+ab+c+(1)-ac-bc-a-b$.
- $2^5$: $\text{Contraste}_{ABCD}=(a-1)(b-1)(c-1)(d-1)(e+1)$.

**Estimación y SS a partir del contraste:**

$$AB\cdots K=\frac{2}{n2^k}\,(\text{Contraste}_{AB\cdots K}) \tag{6-22}$$

$$SS_{AB\cdots K}=\frac{1}{n2^k}\,(\text{Contraste}_{AB\cdots K})^2 \tag{6-23}$$

Relaciones útiles derivadas: $SS = n2^{k-2}\,(\text{Efecto})^2$ y $\hat\beta=\text{Efecto}/2$.

**Algoritmo de Yates.** El capítulo solo lo menciona (pág. 244) como método tabular para el
cálculo manual y remite al material suplementario; no lo desarrolla. Como referencia (no es
texto del capítulo): se escriben los totales en orden estándar; cada nueva columna se forma con
las sumas de pares consecutivos en la mitad superior y las diferencias (segundo menos primero)
en la inferior; tras $k$ repeticiones la columna contiene el gran total y los contrastes en
orden estándar; efecto = contraste$/(n2^{k-1})$, SS = contraste²$/(n2^k)$.

---

## 6-5 Una sola réplica del diseño 2^k

### Problema y estrategia

- Con $k$ moderado el número de corridas crece rápido ($2^5=32$, $2^6=64$) y a menudo solo se
  puede correr **una réplica** (**factorial no replicado**).
- Riesgo: ajustar el modelo al **ruido**. Con una sola observación por punto, un efecto real
  puede quedar oculto por la variabilidad (fig. 6-9a).
- Recomendación: **separar agresivamente los niveles** bajo y alto de cada factor
  (fig. 6-9b) para que el efecto destaque sobre el ruido.
- Con $n=1$ **no hay estimación interna del error** (error puro). Opciones:
  1. **Principio de efectos esparcidos (escasez de efectos):** el sistema suele estar dominado
     por algunos efectos principales e interacciones de orden bajo; las interacciones de orden
     alto son despreciables, así que se combinan sus cuadrados medios para estimar el error.
     Falla si alguna interacción de orden alto es real.
  2. **Gráfica de probabilidad normal de los efectos (Daniel):** los efectos despreciables se
     comportan como una muestra normal de media 0 y varianza constante y caen sobre una recta;
     los efectos activos se apartan de ella. El modelo preliminar contiene los efectos
     apartados y el resto se combina como error.

### Ejemplo 6-2 — Índice de filtración (2⁴, $n=1$)

Planta piloto. $A$ = temperatura, $B$ = presión, $C$ = concentración de formaldehído,
$D$ = velocidad de agitación; respuesta = índice de filtración (gal/h), a maximizar. Objetivo
adicional: reducir $C$. Promedio general 70.06.

Tabla 6-12:

| Término | Efecto | SS | % contribución |
|---|---|---|---|
| A | 21.625 | 1870.56 | 32.6397 |
| B | 3.125 | 39.0625 | 0.681608 |
| C | 9.875 | 390.062 | 6.80626 |
| D | 14.625 | 855.563 | 14.9288 |
| AB | 0.125 | 0.0625 | 0.00109057 |
| AC | −18.125 | 1314.06 | 22.9293 |
| AD | 16.625 | 1105.56 | 19.2911 |
| BC | 2.375 | 22.5625 | 0.393696 |
| BD | −0.375 | 0.5625 | 0.00981515 |
| CD | −1.125 | 5.0625 | 0.0883363 |
| ABC | 1.875 | 14.0625 | 0.245379 |
| ABD | 4.125 | 68.0625 | 1.18763 |
| ACD | −1.625 | 10.5625 | 0.184307 |
| BCD | −2.625 | 27.5625 | 0.480942 |
| ABCD | 1.375 | 7.5625 | 0.131959 |

- Gráfica normal (fig. 6-11): se apartan $A$, $C$, $D$, $AC$ y $AD$.
- Interacción $AC$: el efecto de la temperatura es muy pequeño con $C$ alto y muy grande con
  $C$ bajo. Interacción $AD$: $D$ casi no influye con temperatura baja y tiene efecto positivo
  grande con temperatura alta.
- Recomendación: $A$ y $D$ altos, $C$ bajo (cumple además el objetivo de reducir formaldehído).
- Advertencia del autor: los efectos principales tienen poco significado cuando participan en
  interacciones significativas; siempre examinar las interacciones.

### Proyección del diseño

Como $B$ y todas sus interacciones son despreciables, se descarta $B$ y el $2^4$ no replicado
se **proyecta** en un $2^3$ en $A$, $C$, $D$ con **2 réplicas** (**réplica oculta**), lo que da
error con 8 g.l. Tabla 6-13:

| Fuente | SS | g.l. | MS | $F_0$ | Valor P |
|---|---|---|---|---|---|
| A | 1870.56 | 1 | 1870.56 | 83.36 | <0.0001 |
| C | 390.06 | 1 | 390.06 | 17.38 | <0.0001 |
| D | 855.56 | 1 | 855.56 | 38.13 | <0.0001 |
| AC | 1314.06 | 1 | 1314.06 | 58.56 | <0.0001 |
| AD | 1105.56 | 1 | 1105.56 | 49.27 | <0.0001 |
| CD | 5.06 | 1 | 5.06 | <1 | |
| ACD | 10.56 | 1 | 10.56 | <1 | |
| Error | 179.52 | 8 | 22.44 | | |
| Total | 5730.94 | 15 | | | |

**Regla general de proyección:** en una réplica única de un $2^k$, si $h$ ($h<k$) factores son
despreciables y se descartan, los datos corresponden a un factorial completo $2^{k-h}$ con
$2^h$ réplicas.

### Verificación de diagnóstico (ej. 6-2)

$$\hat y=70.06+\left(\tfrac{21.625}{2}\right)x_1+\left(\tfrac{9.875}{2}\right)x_3+\left(\tfrac{14.625}{2}\right)x_4-\left(\tfrac{18.125}{2}\right)x_1x_3+\left(\tfrac{16.625}{2}\right)x_1x_4$$

Ejemplo: en `(1)`, $\hat y=46.22$ y $e=45-46.22=-1.22$. Predichos por grupo: 46.22
(`(1)`, `b`), 69.39 (`a`, `ab`), 74.23 (`c`, `bc`), 61.14 (`ac`, `abc`), 44.22 (`d`, `bd`),
100.65 (`ad`, `abd`), 72.23 (`cd`, `bcd`), 92.40 (`acd`, `abcd`). Los residuales van de −6.40
a 5.77; su gráfica normal (fig. 6-13) es satisfactoria.

Superficie de respuesta (fig. 6-14):

- Con $x_4=1$: $\hat y=77.3725+(38.25/2)x_1+(9.875/2)x_3-(18.125/2)x_1x_3$ (contornos curvos).
- Con $x_1=1$: $\hat y=80.8725-(8.25/2)x_3+(31.25/2)x_4$ (contornos rectos paralelos).
- Conclusión: $A$ y $D$ altos; el proceso es relativamente robusto a $C$.

### Mitad de gráfica normal (seminormal, *half-normal*)

Se grafica el **valor absoluto** de los efectos contra su probabilidad normal acumulada
(fig. 6-15). La recta pasa siempre por el origen y cerca del percentil 50 de los datos. Muchos
analistas la encuentran más fácil de interpretar, sobre todo con pocos efectos (p. ej. diseños
de 8 corridas).

### Método de Lenth

Procedimiento formal para reducir la subjetividad de la gráfica normal; según Hamada y
Balakrishnan tiene buena potencia y es fácil de implementar. Sean $c_1,\dots,c_m$ los
contrastes (estimaciones de efectos), $m=2^k-1$ en un $2^k$ no replicado.

$$s_0=1.5\times\text{mediana}(|c_j|)$$

$$PSE=1.5\times\text{mediana}(|c_j| : |c_j|<2.5\,s_0)$$

- $PSE$ = **pseudo error estándar**: estimador razonable del error estándar de un contraste
  cuando hay pocos efectos activos.
- **Margen de error** (un contraste individual): $ME=t_{0.025,d}\times PSE$, con $d=m/3$.
- **Margen de error simultáneo** (grupo de contrastes): $SME=t_{\gamma,d}\times PSE$, con
  $\gamma=1-(1+0.95^{1/m})/2$.
- Regla: $|c_j|>SME$ es significativo; entre $ME$ y $SME$ es dudoso.

Ej. 6-2 ($m=15$, $d=5$): $s_0=1.5\times|-2.625|=3.9375$; $2.5\,s_0=9.84375$;
$PSE=1.5\times|1.75|=2.625$; $ME=2.571\times2.625=6.75$; $SME=5.219\times2.625=13.70$.
Los cuatro efectos mayores ($A$, $AC$, $AD$, $D$) superan $SME$; $C$ (9.875) supera $ME$ pero
no $SME$, aunque se incluye porque $AC$ es importante. Mismo resultado que la gráfica normal.

(El "1.75" impreso como mediana restringida no coincide con ningún efecto de la tabla 6-12;
la mediana de los 10 efectos menores que 9.84 queda entre 1.625 y 1.875, cuyo promedio es 1.75.)

**Limitación:** no controla bien el error tipo I. Multiplicadores ajustados por simulación
(Larntz y Whitcomb):

| Número de contrastes | 7 | 15 | 31 |
|---|---|---|---|
| ME original | 3.764 | 2.571 | 2.218 |
| ME ajustado | 2.295 | 2.140 | 2.082 |
| SME original | 9.008 | 5.219 | 4.218 |
| SME ajustado | 4.891 | 4.163 | 4.030 |

Recomendación del autor: usar Lenth como **complemento** de la gráfica normal, no como sustituto.

### Carta de inferencia condicional (Bisgaard)

Se basa en que el error estándar de un efecto en un diseño de dos niveles con $N$ corridas es
$2\sigma/\sqrt N$, de modo que $\pm2$ errores estándar es $\pm4\sigma/\sqrt N$. Se grafican los
efectos en el eje vertical contra $\sigma$ en el horizontal, con las rectas
$y=\pm4\sigma/\sqrt N$ (fig. 6-16). Para cada valor supuesto de $\sigma$, la banda entre las
rectas es un IC aproximado del 95 % para efectos nulos. Ej. 6-2 ($N=16$, rectas $y=\pm\sigma$):
si $\sigma$ está entre 4 y 8, $A$, $C$, $D$, $AC$, $AD$ son significativos; si $\sigma$ pudiera
llegar a 10, $C$ quedaría en duda. También sirve en sentido inverso (¿es razonable un $\sigma$
tan grande?).

### Ejemplo 6-3 — Transformación de datos (2⁴, $n=1$)

Daniel: rapidez de avance de una perforadora. $A$ = carga, $B$ = rapidez de flujo,
$C$ = velocidad de rotación, $D$ = tipo de lodo.

- Escala original: la gráfica normal sugiere $B$, $C$, $D$, $BC$ y $BD$ (fig. 6-18). Los
  residuales muestran no normalidad y varianza creciente con el valor predicho (embudo,
  figs. 6-19 y 6-20).
- Como la respuesta es una razón de cambio se usa $y^*=\ln y$. Tras transformar, solo $B$,
  $C$ y $D$ están activos (fig. 6-21); las interacciones desaparecen y los residuales son
  satisfactorios (figs. 6-22 y 6-23).

Tabla 6-14 (ANOVA en escala logarítmica):

| Fuente | SS | g.l. | MS | $F_0$ | Valor P |
|---|---|---|---|---|---|
| B (flujo) | 5.345 | 1 | 5.345 | 381.79 | <0.0001 |
| C (velocidad) | 1.339 | 1 | 1.339 | 95.64 | <0.0001 |
| D (lodo) | 0.431 | 1 | 0.431 | 30.79 | <0.0001 |
| Error | 0.173 | 12 | 0.014 | | |
| Total | 7.288 | 15 | | | |

$SS_{\text{Modelo}}=7.115$, $R^2=7.115/7.288=0.98$. Lección: expresar los datos en la métrica
correcta puede simplificar el modelo y eliminar interacciones aparentes.

### Ejemplo 6-4 — Efectos de localización y de dispersión (2⁴, $n=1$)

Paneles de avión prensados; respuesta = defectos por panel (promedio actual 5.5).
$A$ = temperatura (295, 325 °F), $B$ = tiempo de sujeción (7, 9 min), $C$ = flujo de resina
(10, 20), $D$ = tiempo de cierre (15, 30 s).

- **Localización:** $A=5.75$ y $C=-4.25$ son los únicos efectos grandes y explican cerca del
  77 % de la variabilidad. Conviene temperatura baja y flujo de resina alto.
- **Dispersión:** la gráfica normal de residuales es normal, pero residuales contra $B$
  (fig. 6-26) muestra mucha menos dispersión con $B$ bajo. $B$ no afecta la media pero sí la
  variabilidad. En la gráfica de cubo (fig. 6-27) el rango promedio es
  $\bar R_{B^+}=4.75$ y $\bar R_{B^-}=1.25$.

**Estadístico de dispersión (Box y Meyer), ecs. 6-24 y 6-25.** Para cada columna $i$ de la
tabla de signos se calcula la desviación estándar de los residuales con signo +, $S(i^+)$, y
con signo −, $S(i^-)$:

$$F_i^*=\ln\frac{S^2(i^+)}{S^2(i^-)},\qquad i=1,2,\dots,15$$

Si las dos varianzas son iguales, $F_i^*$ es aproximadamente normal, por lo que los $F_i^*$ se
llevan a una gráfica de probabilidad normal (fig. 6-28). Tabla 6-15:

| Columna | $S(i^+)$ | $S(i^-)$ | $F_i^*$ |
|---|---|---|---|
| A | 2.25 | 1.85 | 0.39 |
| B | 2.72 | 0.83 | **2.37** |
| AB | 2.21 | 1.86 | 0.34 |
| C | 1.91 | 2.20 | −0.28 |
| AC | 1.81 | 2.24 | −0.43 |
| BC | 1.80 | 2.26 | −0.46 |
| ABC | 1.80 | 2.24 | −0.44 |
| D | 2.24 | 1.55 | 0.74 |
| AD | 2.05 | 1.93 | 0.12 |
| BD | 2.28 | 1.61 | 0.70 |
| ABD | 1.97 | 2.11 | −0.14 |
| CD | 1.93 | 1.58 | 0.40 |
| ACD | 1.52 | 2.16 | −0.70 |
| BCD | 2.09 | 1.89 | 0.28 (dudoso, pág. 263; con esas desviaciones daría 0.20) |
| ABCD | 1.61 | 2.33 | −0.74 |

Residuales en orden estándar (modelo con $A$ y $C$): −0.94, −0.69, −2.44, −2.69, −1.19, 0.56,
−0.19, 2.06, 0.06, 0.81, 2.06, 3.81, −0.69, −1.44, 3.31, −2.44.

Solo $B$ se aparta de la recta. Decisión: temperatura baja, flujo de resina alto, tiempo de
sujeción bajo (menos variabilidad) y tiempo de cierre bajo ($D$ sin efecto de localización ni
dispersión). Resultado: menos de un defecto por panel.

**Advertencia:** para que los residuales informen bien sobre la dispersión, el **modelo de
localización** debe estar correctamente especificado.

### Ejemplo 6-5 — Mediciones duplicadas frente a réplicas reales (2⁴)

Horno de oxidación vertical; cada corrida procesa **4 obleas juntas** y se mide el espesor de
óxido de cada una. $A$ = temperatura, $B$ = tiempo, $C$ = presión, $D$ = flujo de gas.

**Punto clave.** Las cuatro obleas recibieron los tratamientos simultáneamente, así que son
**mediciones duplicadas**, no réplicas. Su variabilidad (dentro de la corrida) es mucho menor
que la variabilidad entre corridas. La respuesta correcta es el **promedio** $\bar y$ por
corrida, analizado como $2^4$ no replicado.

Análisis correcto (tabla 6-17, respuesta $\bar y$):

| Término | Efecto | SS | % contribución |
|---|---|---|---|
| A | 43.125 | 7439.06 | 67.9339 |
| B | 18.125 | 1314.06 | 12.0001 |
| C | −10.375 | 430.562 | 3.93192 |
| D | −1.625 | 10.5625 | 0.0964573 |
| AB | 16.875 | 1139.06 | 10.402 |
| AC | −10.625 | 451.563 | 4.12369 |
| AD | 1.125 | 5.0625 | 0.046231 |
| BC | 3.875 | 60.0625 | 0.548494 |
| BD | −3.875 | 60.0625 | 0.548494 |
| CD | 1.125 | 5.0625 | 0.046231 |
| ABC | −0.375 | 0.5625 | 0.00513678 |
| ABD | 2.875 | 33.0625 | 0.301929 |
| ACD | −0.125 | 0.0625 | 0.000570753 |
| BCD | −0.625 | 1.5625 | 0.0142688 |
| ABCD | 0.125 | 0.0625 | 0.000570753 |

Activos según la gráfica normal (fig. 6-29): $A$, $B$, $C$, $AB$, $AC$. ANOVA (tabla 6-18):

| Fuente | SS | g.l. | MS | F | Prob > F |
|---|---|---|---|---|---|
| Modelo | 10774.31 | 5 | 2154.86 | 122.35 | <0.000 |
| A | 7439.06 | 1 | 7439.06 | 422.37 | <0.000 |
| B | 1314.06 | 1 | 1314.06 | 74.61 | <0.000 |
| C | 430.56 | 1 | 430.56 | 24.45 | 0.0006 |
| AB | 1139.06 | 1 | 1139.06 | 64.67 | <0.000 |
| AC | 451.56 | 1 | 451.56 | 25.64 | 0.0005 |
| Residual | 176.12 | 10 | 17.61 | | |
| Total | 10950.44 | 15 | | | |

$R^2=0.9839$, $R^2$ ajustada 0.9759, $R^2$ predicción 0.9588, PRESS 450.88, desv. est. 4.20,
error estándar de los coeficientes 1.05.

$$\hat y=399.19+21.56x_1+9.06x_2-5.19x_3+8.44x_1x_2-5.31x_1x_3$$

Objetivo: espesor medio de 400 Å (especificación 390–410 Å). Hay muchas combinaciones de $A$ y
$B$ aceptables; con presión baja la ventana se desplaza hacia tiempos de ciclo más cortos
(fig. 6-30).

Análisis **incorrecto** (tabla 6-19: las 64 mediciones tratadas como 4 réplicas): error puro
294.00 con 48 g.l., $\hat\sigma^2=6.12$ frente a $17.61$ del análisis correcto. Con ese error
subestimado resultan "significativos" además $D$ ($P=0.0115$), $BC$, $BD$ y $ABD$ (todos
<0.0001); el modelo sale mucho más complejo de lo real. Daño: manipular factores que no importan
desperdicia recursos y puede añadir variabilidad a otras respuestas.

**Uso de las duplicadas para modelar la variabilidad.** Las duplicadas informan sobre la
variabilidad dentro de la corrida (o sobre el instrumento, o la uniformidad, según cómo se
tomen). Se analiza $\ln(s^2)$ como respuesta (el logaritmo es la transformación habitual para
varianzas). No hay efectos fuertes; los mayores son $A$ y $BD$. Modelo jerárquico:

$$\widehat{\ln(s^2)}=1.08+0.41x_1-0.40x_2+0.20x_4-0.56x_2x_4$$

Explica algo menos de la mitad de la variabilidad de $\ln(s^2)$. Superponiendo los contornos de
espesor medio (390–410 Å) y de varianza ($s^2\le2$), con presión baja y flujo de gas alto, se
obtiene una región factible en tiempo y temperatura (fig. 6-33). Es un ejemplo simple de
optimización simultánea de dos respuestas (cap. 11).

Nota de exactitud: el texto define $A$ = temperatura y $B$ = tiempo, pero la salida de la
tabla 6-18 rotula "A-Time, B-Temp" y los contornos ponen Tiempo en el eje horizontal. La
inconsistencia está en el libro.

---

## 6-6 Adición de puntos centrales en el diseño 2^k

### Motivación y modelos

El $2^k$ supone linealidad. El modelo de primer orden con interacciones

$$y=\beta_0+\sum_{j=1}^{k}\beta_jx_j+\sum_{i<j}\sum\beta_{ij}x_ix_j+\varepsilon \tag{6-26}$$

admite cierta curvatura (torsión del plano), pero no la **curvatura cuadrática pura** del
modelo de superficie de respuesta de segundo orden:

$$y=\beta_0+\sum_{j=1}^{k}\beta_jx_j+\sum_{i<j}\sum\beta_{ij}x_ix_j+\sum_{j=1}^{k}\beta_{jj}x_j^2+\varepsilon \tag{6-27}$$

### Método

Agregar $n_C$ réplicas en el **punto central** $x_i=0$ ($i=1,\dots,k$). Ventajas:

- Protege contra la curvatura (permite probarla).
- Da una estimación **independiente del error** (error puro) con $n_C-1$ g.l., aunque los
  puntos factoriales no tengan réplicas.
- **No altera** las estimaciones usuales de los efectos del $2^k$.
- Requiere que los $k$ factores sean **cuantitativos** (ver punto 5 de las recomendaciones).

### Prueba de curvatura

Sean $\bar y_F$ el promedio de las $n_F$ corridas factoriales y $\bar y_C$ el promedio de las
$n_C$ corridas centrales. Si $\bar y_F-\bar y_C$ es pequeña, el centro cae sobre el plano de
los puntos factoriales y no hay curvatura.

$$SS_{\text{Cuadrática pura}}=\frac{n_Fn_C(\bar y_F-\bar y_C)^2}{n_F+n_C}\quad(1\ \text{g.l.}) \tag{6-28}$$

$$MS_E=\frac{SS_E}{n_C-1}=\frac{\sum_{\text{puntos centrales}}(y_i-\bar y_C)^2}{n_C-1} \tag{6-29}$$

$$F_0=\frac{SS_{\text{Cuadrática pura}}}{MS_E}\sim F_{1,\,n_C-1}$$

Hipótesis: $H_0:\sum_{j=1}^{k}\beta_{jj}=0$ contra $H_1:\sum_{j=1}^{k}\beta_{jj}\neq0$.
Se prueba la **suma** de los coeficientes cuadráticos, no cada uno: no se puede saber qué
factor causa la curvatura, y curvaturas de signo opuesto podrían cancelarse.

### Ejemplo 6-6 — Rendimiento de un proceso químico (2² + 5 puntos centrales)

$A$ = tiempo de reacción (30, 40 min; centro 35), $B$ = temperatura (150, 160 °C; centro 155).
Datos (fig. 6-35): `(1)`=39.3, `a`=40.9, `b`=40.0, `ab`=41.5; centro: 40.3, 40.5, 40.7, 40.2, 40.6.

- $\bar y_F=40.425$, $\bar y_C=40.46$, diferencia $=-0.035$.
- $SS_{\text{Cuadrática pura}}=(4)(5)(-0.035)^2/(4+5)=0.0027$.
- $MS_E=0.1720/4=0.0430$.
- Efectos (calculados aquí a partir de los datos, no impresos en el libro): $A=1.55$,
  $B=0.65$, $AB=-0.05$.

Tabla 6-20:

| Fuente | SS | g.l. | MS | $F_0$ | Valor P |
|---|---|---|---|---|---|
| A (tiempo) | 2.4025 | 1 | 2.4025 | 55.87 | 0.0017 |
| B (temperatura) | 0.4225 | 1 | 0.4225 | 9.83 | 0.0350 |
| AB | 0.0025 | 1 | 0.0025 | 0.06 | 0.8185 |
| Cuadrática pura | 0.0027 | 1 | 0.0027 | 0.06 | 0.8185 |
| Error | 0.1720 | 4 | 0.0430 | | |
| Total | 3.0022 | 8 | | | |

Conclusión: ambos efectos principales significativos, sin interacción ni curvatura; no se
rechaza $H_0:\beta_{11}+\beta_{22}=0$. Basta el modelo de primer orden.

### Si hay curvatura: diseño central compuesto

El $2^2$ con centro solo tiene 5 corridas independientes y el modelo de segundo orden en dos
factores tiene 6 parámetros, por lo que no se puede estimar. Solución: agregar **corridas
axiales** para formar un **diseño central compuesto** (fig. 6-36). Para $k=3$ tiene
$14+n_C$ corridas (típicamente $3\le n_C\le5$) y ajusta los 10 parámetros del modelo de
segundo orden. Se detalla en el cap. 11.

### Recomendaciones prácticas sobre puntos centrales

1. En un proceso en marcha, usar las **condiciones de operación actuales** como punto central:
   garantiza al personal que parte de las corridas se hacen en condiciones familiares.
2. Si el centro coincide con la operación actual, comparar sus respuestas con el histórico
   (p. ej. en la carta de control) para detectar si algo inusual ocurrió durante el experimento.
3. Correr los puntos centrales en **orden no aleatorio**: uno o dos al principio, uno o dos a
   la mitad y uno o dos al final. Sirven para verificar la estabilidad del proceso y detectar
   tendencias en el tiempo.
4. Si no hay información previa sobre la variabilidad, correr 2 o 3 puntos centrales como
   **primeras corridas** para obtener una estimación preliminar; si es mayor de lo razonable,
   detenerse e investigar antes de continuar.
5. Con factores **cualitativos** mezclados con cuantitativos, los puntos centrales se colocan
   en el centro de los cuantitativos **para cada nivel** de los cualitativos (fig. 6-37:
   tiempo y temperatura cuantitativos, tipo de catalizador cualitativo; un centro en cada
   cara opuesta del cubo).

---

## Resumen de fórmulas (diseño 2^k con n réplicas)

| Cantidad | Fórmula |
|---|---|
| Contraste de $AB\cdots K$ | $(a\pm1)(b\pm1)\cdots(k\pm1)$; signo − si el factor está en el efecto |
| Efecto | $\text{Contraste}/(n2^{k-1})$ |
| Suma de cuadrados (1 g.l.) | $\text{Contraste}^2/(n2^k)=n2^{k-2}\,\text{Efecto}^2$ |
| Coeficiente de regresión | $\hat\beta=\text{Efecto}/2$; $\hat\beta_0=\bar y$ |
| Varianza de un efecto | $\sigma^2/(n2^{k-2})$ |
| Error estándar de un efecto | $2S/\sqrt{n2^k}$, con $S^2=MS_E$ |
| Error estándar de un coeficiente | $\sqrt{MS_E/(n2^k)}$ |
| IC de un efecto | $\text{Efecto}\pm t_{\alpha/2,\,N-p}\,se(\text{Efecto})$ |
| g.l. del error (modelo completo) | $2^k(n-1)$ |
| g.l. totales | $n2^k-1$ |
| Proyección | descartar $h$ factores da un $2^{k-h}$ con $2^h$ réplicas |
| Lenth | $s_0=1.5\,\text{med}\lvert c_j\rvert$; $PSE=1.5\,\text{med}(\lvert c_j\rvert:\lvert c_j\rvert<2.5s_0)$; $ME=t_{0.025,m/3}\,PSE$ |
| Dispersión | $F_i^*=\ln[S^2(i^+)/S^2(i^-)]$ |
| Curvatura | $SS=n_Fn_C(\bar y_F-\bar y_C)^2/(n_F+n_C)$; error puro con $n_C-1$ g.l. |

## Reglas y advertencias del autor

- Mirar siempre **magnitud y dirección** de los efectos antes del ANOVA; el ANOVA confirma.
- Un efecto principal carece de interpretación aislada si participa en una interacción significativa.
- En diseños no replicados, separar agresivamente los niveles de los factores.
- No agrupar a ciegas las interacciones de orden alto como error (problema 6-20): usar primero
  la gráfica normal o seminormal de efectos.
- Principio de **jerarquía**: si una interacción entra al modelo, se incluyen sus efectos
  principales aunque no sean significativos (p. ej. modelo de $\ln s^2$ del ej. 6-5). No es un
  principio absoluto (problema 6-34).
- Revisar siempre los residuales: contra predichos, en papel normal y **contra cada factor**
  (así se descubren efectos de dispersión, ej. 6-4).
- Si los residuales muestran embudo o no normalidad, probar una transformación (logaritmo para
  tasas y varianzas) antes de aceptar un modelo con interacciones.
- Distinguir **réplicas reales** (corridas independientes, con su propio ajuste de factores) de
  **mediciones duplicadas** (varias lecturas o unidades dentro de una misma corrida): con
  duplicadas se analiza el promedio y, aparte, $\ln(s^2)$.
- Añadir puntos centrales cuando los factores son cuantitativos: curvatura y error puro sin
  alterar los efectos.

## 6-7 Problemas (solo referencia)

Problemas 6-1 a 6-34 (págs. 276–286). De interés para validar software o como práctica:

- 6-1 a 6-4: 2³ con $n=3$, vida de herramienta; 6-6 añade 4 puntos centrales.
- 6-5, 6-8 a 6-12: diseños 2² replicados.
- 6-7, 6-15: 2⁴ con $n=2$.
- 6-17, 6-18, 6-23, 6-30, 6-31: 2⁴ no replicados (gráfica normal, proyección, transformaciones
  $1/y$ y $\ln y$).
- 6-21, 6-22: 2⁵ no replicado, con puntos centrales en 6-22.
- 6-25: mediciones duplicadas frente a réplicas (brownies).
- 6-26, 6-32: 2⁴ con 4 puntos centrales.
- 6-28: curvatura en el ej. 6-2 con 5 puntos centrales (73, 75, 71, 69, 76).
- 6-29: valor faltante en un $2^k$ no replicado; se estima con el valor que anula el contraste
  de la interacción de mayor orden.
- 6-33: varianza de $\hat y$ e intervalo de confianza para la respuesta media, usando
  $V(\hat\beta)=\sigma^2/(n2^k)$ y covarianzas nulas.
- 6-34: modelos jerárquicos frente a no jerárquicos.
