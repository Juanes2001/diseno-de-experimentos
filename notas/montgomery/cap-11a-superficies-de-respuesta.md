# Capítulo 11 (parte A) — Metodología de superficies de respuesta: secciones 11-1 a 11-4

> Montgomery, págs. 427–473 (secciones 11-1 a 11-4; la 11-5 "Experimentos con mezclas" empieza en la pág. 472 y va en la parte B)

Notación usada en todo el capítulo: $\xi_i$ = variable **natural** (unidades reales), $x_i$ = variable
**codificada** (centro 0, niveles $\pm 1$), $k$ = número de factores, $n_F$ = puntos factoriales,
$n_C$ = puntos centrales, $n_A = 2k$ = puntos axiales, $\alpha$ = distancia axial, $N$ = total de corridas,
$p$ = número de parámetros del modelo. MSR = metodología de superficies de respuesta, DCC = diseño
central compuesto.

---

## 11-1 Introducción a la metodología de superficies de respuesta

**Qué es.** Conjunto de técnicas matemáticas y estadísticas para modelar y analizar problemas en los
que una respuesta $y$ depende de varias variables y el objetivo es **optimizarla**.

$$y = f(x_1, x_2) + \varepsilon, \qquad E(y) = f(x_1,x_2) = \eta$$

La superficie $\eta = f(x_1,x_2)$ es la **superficie de respuesta**; se representa en 3D (fig. 11-1) o
con **gráficas de contorno** (líneas de respuesta constante en el plano $x_1,x_2$, fig. 11-2).

**Modelos de aproximación.** La forma real de $f$ es desconocida; se aproxima con un polinomio de
orden bajo en una región pequeña de las $x$:

- **Primer orden** (ec. 11-1), cuando la respuesta es aproximadamente lineal:

$$y = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + \cdots + \beta_k x_k + \varepsilon$$

- **Segundo orden** (ec. 11-2), cuando hay curvatura:

$$y = \beta_0 + \sum_{i=1}^{k}\beta_i x_i + \sum_{i=1}^{k}\beta_{ii}x_i^2 + \sum\sum_{i<j}\beta_{ij}x_i x_j + \varepsilon$$

Los parámetros se estiman por mínimos cuadrados (cap. 10) y el análisis se hace sobre la superficie
**ajustada**. Un polinomio no vale para todo el espacio de los factores, pero suele funcionar bien en
una región relativamente pequeña. Los diseños pensados para ajustar estos modelos son los **diseños
de superficie de respuesta** (sección 11-4).

**Carácter secuencial (fig. 11-3).**

1. Lejos del óptimo (condiciones de operación actuales) hay poca curvatura → modelo de primer orden.
2. Se avanza de forma rápida y económica por la **trayectoria del mejoramiento** hasta la vecindad
   del óptimo (sección 11-2).
3. En la región del óptimo se ajusta un modelo de segundo orden y se analiza para localizar el
   óptimo (sección 11-3).

Analogía: "ascenso a una colina" (máximo) o "descenso a un valle" (mínimo). Objetivo final: hallar
las condiciones de operación óptimas o una región del espacio de factores donde se cumplan los
requerimientos de operación. Referencias que cita el autor: Myers y Montgomery; Khuri y Cornell;
Box y Draper.

---

## 11-2 Método del ascenso más pronunciado

**Cuándo se usa.** Las condiciones iniciales suelen estar lejos del óptimo; se quiere llegar pronto
a su vecindad con un procedimiento económico. Supuesto: en una región pequeña, un modelo de primer
orden aproxima bien la superficie real. Para minimización se llama **descenso más pronunciado**.

**Modelo ajustado** (ec. 11-3):

$$\hat y = \hat\beta_0 + \sum_{i=1}^{k}\hat\beta_i x_i$$

Sus contornos son rectas paralelas (fig. 11-4). La **dirección del ascenso más pronunciado** es
aquella en la que $\hat y$ crece más rápido: es normal a los contornos. Se toma como **trayectoria**
la recta que pasa por el centro de la región de interés y es normal a la superficie ajustada, de modo
que **los pasos son proporcionales a los coeficientes $\{\hat\beta_i\}$** (en signo y magnitud). El
tamaño real del paso lo fija el experimentador con conocimiento del proceso.

### Procedimiento general

1. Correr un diseño de primer orden (típicamente $2^k$ con puntos centrales) centrado en las
   condiciones actuales y ajustar el modelo de primer orden.
2. Verificar la adecuación del modelo (interacción y curvatura, ver abajo) **antes** de moverse.
3. Hacer corridas a lo largo de la trayectoria hasta que la respuesta deje de aumentar.
4. Alrededor del mejor punto ajustar un nuevo modelo de primer orden, calcular una nueva trayectoria
   y repetir.
5. Cuando el modelo de primer orden presenta **falta de ajuste** (curvatura significativa), se ha
   llegado a la vecindad del óptimo: se pasa a un modelo de segundo orden (sección 11-3).

### Verificación de adecuación con un $2^k$ + puntos centrales

El diseño permite: (1) estimar el error, (2) probar interacciones (productos cruzados), (3) probar
curvatura cuadrática pura.

- **Error puro** con las $n_C$ réplicas del centro: $\hat\sigma^2 = \dfrac{\sum y_{c}^2 - (\sum y_c)^2/n_C}{n_C - 1}$.
- **Interacción**: $\hat\beta_{12}$ = mitad del efecto de interacción del $2^2$;
  $SS_{\text{Interacción}} = (\text{contraste})^2/n_F$ con 1 g.l.; $F = SS_{\text{Interacción}}/\hat\sigma^2$.
- **Curvatura cuadrática pura** (sección 6-6): $\bar y_F - \bar y_C$ estima $\sum \beta_{ii}$
  (para $k=2$, $\beta_{11}+\beta_{22}$). Para $H_0:\ \sum\beta_{ii}=0$, con 1 g.l.:

$$SS_{\text{Cuadrática pura}} = \frac{n_F\, n_C\,(\bar y_F - \bar y_C)^2}{n_F + n_C}, \qquad F = \frac{SS_{\text{Cuadrática pura}}}{\hat\sigma^2}$$

- **Error estándar de los coeficientes** en el $2^2$: $se(\hat\beta_i) = \sqrt{MS_E/n_F} = \sqrt{\hat\sigma^2/4}$.

Estructura de la tabla ANOVA (tabla 11-2): Modelo ($\beta_1,\dots,\beta_k$) con $k$ g.l.; Residual
desglosado en Interacción, Cuadrático puro y Error puro ($n_C-1$ g.l.); Total $N-1$.

### Algoritmo para las coordenadas de la trayectoria (págs. 435–436)

Base u origen: $x_1 = x_2 = \cdots = x_k = 0$.

1. Elegir el tamaño del paso en una variable, $\Delta x_j$. Normalmente la variable que mejor se
   conoce o la de mayor $|\hat\beta_j|$.
2. El paso en las demás variables es

$$\Delta x_i = \frac{\hat\beta_i}{\hat\beta_j/\Delta x_j}, \qquad i = 1,2,\dots,k;\ i \ne j$$

3. Convertir los $\Delta x_i$ codificados a unidades naturales: si $x_i = (\xi_i - \xi_{i,0})/s_i$,
   entonces $\Delta\xi_i = s_i\,\Delta x_i$.

Las corridas del proceso se hacen siempre en variables naturales, aunque los cálculos se hagan en
codificadas.

### Ejemplo 11-1 (rendimiento de un proceso químico)

- Factores: tiempo de reacción $\xi_1$ (min) y temperatura $\xi_2$ (°F). Operación actual: 35 min,
  155 °F, rendimiento ≈ 40 %.
- **Primer diseño**: región (30, 40) min × (150, 160) °F; $x_1 = (\xi_1-35)/5$, $x_2 = (\xi_2-155)/5$.
  $2^2$ + 5 puntos centrales (tabla 11-1). Respuestas factoriales: 39.3, 40.0, 40.9, 41.5; centros:
  40.3, 40.5, 40.7, 40.2, 40.6.
- Modelo: $\hat y = 40.44 + 0.775x_1 + 0.325x_2$.
- $\hat\sigma^2 = 0.0430$ (4 g.l.). $\hat\beta_{12} = -0.025$, $SS_{\text{Int}} = 0.0025$, $F = 0.058$.
  $\bar y_F = 40.425$, $\bar y_C = 40.46$, $\hat\beta_{11}+\hat\beta_{22} = -0.035$,
  $SS_{\text{Cuad. pura}} = 0.0027$, $F = 0.063$. $se(\hat\beta_i) = 0.10$.

Tabla 11-2 (ANOVA del primer modelo de primer orden):

| Fuente | SS | g.l. | MS | $F_0$ | Valor P |
|---|---|---|---|---|---|
| Modelo ($\beta_1,\beta_2$) | 2.8250 | 2 | 1.4125 | 47.83 | 0.0002 |
| Residual | 0.1772 | 6 | | | |
| (Interacción) | (0.0025) | 1 | 0.0025 | 0.058 | 0.8215 |
| (Cuadrático puro) | (0.0027) | 1 | 0.0027 | 0.063 | 0.8142 |
| (Error puro) | (0.1720) | 4 | 0.0430 | | |
| Total | 3.0022 | 8 | | | |

- Conclusión: modelo de primer orden adecuado. **Trayectoria**: pendiente 0.325/0.775; paso básico
  de 5 min → $\Delta x_1 = 1.0$, $\Delta x_2 = 0.325/0.775 = 0.42$, es decir $\Delta\xi_1 = 5$ min,
  $\Delta\xi_2 = 0.42(5) \approx 2$ °F.
- Tabla 11-3 (pasos desde el origen 35 min, 155 °F): rendimientos 41.0, 42.9, 47.1, 49.7, 53.8,
  59.9, 65.0, 70.4, 77.6, **80.3** (paso 10: 85 min, 175 °F), 76.2, 75.1. La respuesta crece hasta
  el paso 10 y luego baja. (En la tabla impresa los pasos 11 y 12 figuran con 179 y 181 °F; con el
  paso de 2 °F corresponderían 177 y 179 — posible errata del libro, pág. 434.)
- **Segundo diseño** alrededor de (85, 175): región [80, 90] × [170, 180]; $x_1 = (\xi_1-85)/5$,
  $x_2 = (\xi_2-175)/5$; $2^2$ + 5 centros (tabla 11-4). Respuestas factoriales: 76.5, 77.0, 78.0,
  79.5; centros: 79.9, 80.3, 80.0, 79.7, 79.8.
- Modelo: $\hat y = 78.97 + 1.00x_1 + 0.50x_2$.

Tabla 11-5 (ANOVA del segundo modelo de primer orden):

| Fuente | SS | g.l. | MS | $F_0$ | Valor P |
|---|---|---|---|---|---|
| Regresión | 5.00 | 2 | | | |
| Residual | 11.1200 | 6 | | | |
| (Interacción) | (0.2500) | 1 | 0.2500 | 4.72 | 0.0955 |
| (Cuadrático puro) | (10.6580) | 1 | 10.6580 | 201.09 | 0.0001 |
| (Error puro) | (0.2120) | 4 | 0.0530 | | |
| Total | 16.1200 | 8 | | | |

- Conclusión: curvatura fuerte → el modelo de primer orden ya no es adecuado; se está cerca del
  óptimo y hay que ampliar el diseño para un modelo de segundo orden (ejemplo 11-2).

---

## 11-3 Análisis de una superficie de respuesta de segundo orden

Cerca del óptimo se usa el modelo de segundo orden (ec. 11-4, idéntico a la ec. 11-2). Objetivos:
encontrar las condiciones óptimas y **caracterizar** la superficie.

### 11-3.1 Localización del punto estacionario

**Punto estacionario**: niveles $x_{1,s},\dots,x_{k,s}$ donde
$\partial\hat y/\partial x_1 = \cdots = \partial\hat y/\partial x_k = 0$. Puede ser (1) un **máximo**
(fig. 11-6), (2) un **mínimo** (fig. 11-7) o (3) un **punto silla** o minimax (fig. 11-8).

Notación matricial (ec. 11-5):

$$\hat y = \hat\beta_0 + \mathbf{x}'\mathbf{b} + \mathbf{x}'\mathbf{B}\mathbf{x}$$

$$\mathbf{x} = \begin{bmatrix} x_1\\ x_2\\ \vdots\\ x_k\end{bmatrix},\quad
\mathbf{b} = \begin{bmatrix}\hat\beta_1\\ \hat\beta_2\\ \vdots\\ \hat\beta_k\end{bmatrix},\quad
\mathbf{B} = \begin{bmatrix}
\hat\beta_{11} & \hat\beta_{12}/2 & \cdots & \hat\beta_{1k}/2\\
 & \hat\beta_{22} & \cdots & \hat\beta_{2k}/2\\
 & & \ddots & \vdots\\
\text{sim.} & & & \hat\beta_{kk}\end{bmatrix}$$

$\mathbf{b}$: coeficientes de primer orden ($k\times1$). $\mathbf{B}$: simétrica $k\times k$, con los
cuadráticos **puros** en la diagonal y **la mitad** de los cuadráticos mixtos (interacciones) fuera de
ella.

$$\frac{\partial \hat y}{\partial \mathbf{x}} = \mathbf{b} + 2\mathbf{B}\mathbf{x} = \mathbf{0}\quad(11\text{-}6)
\qquad\Rightarrow\qquad \mathbf{x}_s = -\tfrac12\,\mathbf{B}^{-1}\mathbf{b}\quad(11\text{-}7)$$

Respuesta predicha en el punto estacionario (ec. 11-8):

$$\hat y_s = \hat\beta_0 + \tfrac12\,\mathbf{x}_s'\mathbf{b}$$

### 11-3.2 Caracterización de la superficie de respuesta

Caracterizar = decidir si $\mathbf{x}_s$ es máximo, mínimo o silla, y estudiar la sensibilidad de la
respuesta a cada variable. Vía directa: gráfica de contorno (fácil con 2–3 variables). Vía formal:
**análisis canónico**.

**Forma canónica** (ec. 11-9): se traslada el origen a $\mathbf{x}_s$ y se rotan los ejes hasta
alinearlos con los ejes principales de la superficie ajustada (fig. 11-9):

$$\hat y = \hat y_s + \lambda_1 w_1^2 + \lambda_2 w_2^2 + \cdots + \lambda_k w_k^2$$

$\{w_i\}$ = variables canónicas; $\{\lambda_i\}$ = **eigenvalores** (raíces características) de
$\mathbf{B}$, soluciones de $|\mathbf{B} - \lambda\mathbf{I}| = 0$.

**Reglas de interpretación** (con $\mathbf{x}_s$ dentro de la región de exploración):

| Signos de $\{\lambda_i\}$ | Naturaleza de $\mathbf{x}_s$ |
|---|---|
| Todos positivos | Mínimo |
| Todos negativos | Máximo |
| Signos mezclados | Punto silla |

La superficie es más inclinada en la dirección $w_i$ con mayor $|\lambda_i|$ (y menos sensible en la
de menor $|\lambda_i|$).

**Relación entre variables canónicas y de diseño** (útil cuando no se puede operar en $\mathbf{x}_s$
y se quiere "retroceder" con poca pérdida por la dirección de menor $|\lambda_i|$):

$$\mathbf{w} = \mathbf{M}'(\mathbf{x} - \mathbf{x}_s)$$

$\mathbf{M}$ es ortogonal $k\times k$; su columna $i$ es el eigenvector normalizado $\mathbf{m}_i$
asociado a $\lambda_i$, solución de (ec. 11-10)

$$(\mathbf{B} - \lambda_i\mathbf{I})\,\mathbf{m}_i = \mathbf{0}, \qquad \sum_{j=1}^{k} m_{ji}^2 = 1$$

Cálculo práctico: el sistema no tiene solución única; se fija arbitrariamente una incógnita (p. ej.
$m^*_{21}=1$), se resuelve y se divide entre $\sqrt{\sum (m^*_{ji})^2}$ para normalizar.

### Ejemplo 11-2 (continuación del 11-1: DCC y modelo cuadrático)

- Al $2^2$ + 5 centros de la tabla 11-4 se le agregan 4 **puntos axiales** en $(0,\pm1.414)$ y
  $(\pm1.414, 0)$ → **DCC** de 13 corridas (tabla 11-6, fig. 11-10). En unidades naturales los
  axiales son 92.07/77.93 min y 182.07/167.93 °F. Rendimientos axiales: 78.4 $(1.414,0)$, 75.6
  $(-1.414,0)$, 78.5 $(0,1.414)$, 77.0 $(0,-1.414)$. Se midieron además viscosidad $y_2$ y peso
  molecular $y_3$.
- Nota al pie: las corridas axiales se hicieron casi en el mismo periodo que las primeras nueve; de
  haber pasado mucho tiempo se habría requerido **bloquear** (sección 11-4.3).
- Salida de Design-Expert (tabla 11-7), respuesta rendimiento:

Sumas de cuadrados secuenciales:

| Fuente | SS | g.l. | MS | F | Prob > F |
|---|---|---|---|---|---|
| Media | 80062.16 | 1 | 80062.16 | | |
| Lineal | 10.04 | 2 | 5.02 | 2.69 | 0.1166 |
| 2FI | 0.25 | 1 | 0.25 | 0.12 | 0.7350 |
| **Cuadrático** | 17.95 | 2 | 8.98 | 126.88 | <0.0001 (sugerido) |
| Cúbico | 2.042E-003 | 2 | 1.021E-003 | 0.010 | 0.9897 (con alias) |
| Residual | 0.49 | 5 | 0.099 | | |
| Total | 80090.90 | 13 | 6160.84 | | |

Pruebas de falta de ajuste (error puro: SS 0.21, 4 g.l., MS 0.053):

| Modelo | SS | g.l. | MS | F | Prob > F |
|---|---|---|---|---|---|
| Lineal | 18.49 | 6 | 3.08 | 58.14 | 0.0008 |
| 2FI | 18.24 | 5 | 3.65 | 68.82 | 0.0006 |
| **Cuadrático** | 0.28 | 3 | 0.094 | 1.78 | 0.2897 |
| Cúbico | 0.28 | 1 | 0.28 | 5.31 | 0.0826 |

Estadísticos de resumen:

| Modelo | Desv. est. | $R^2$ | $R^2$ aj. | $R^2$ pred. | PRESS |
|---|---|---|---|---|---|
| Lineal | 1.37 | 0.3494 | 0.2193 | −0.0435 | 29.99 |
| 2FI | 1.43 | 0.3581 | 0.1441 | −0.2730 | 36.59 |
| **Cuadrático** | 0.27 | 0.9828 | 0.9705 | 0.9184 | 2.35 |
| Cúbico | 0.31 | 0.9828 | 0.9588 | 0.3622 | 18.33 |

Criterios de selección de modelo: polinomio de mayor orden cuyos términos adicionales son
significativos, sin falta de ajuste significativa, y con PRESS mínimo ($R^2$ de predicción máximo).
El DCC no soporta el modelo cúbico completo (advertencia "aliased").

ANOVA del modelo cuadrático (sumas de cuadrados parciales; A = tiempo, B = temperatura):

| Fuente | SS | g.l. | MS | F | Prob > F |
|---|---|---|---|---|---|
| Modelo | 28.25 | 5 | 5.65 | 79.85 | <0.0001 |
| A | 7.92 | 1 | 7.92 | 111.93 | <0.0001 |
| B | 2.12 | 1 | 2.12 | 30.01 | 0.0009 |
| A² | 13.18 | 1 | 13.18 | 186.22 | <0.0001 |
| B² | 6.97 | 1 | 6.97 | 98.56 | <0.0001 |
| AB | 0.25 | 1 | 0.25 | 3.53 | 0.1022 |
| Residual | 0.50 | 7 | 0.071 | | |
| Falta de ajuste | 0.28 | 3 | 0.094 | 1.78 | 0.2897 |
| Error puro | 0.21 | 4 | 0.053 | | |
| Total corr. | 28.74 | 12 | | | |

Desv. est. 0.27; media 78.48; C.V. 0.34; PRESS 2.35; $R^2$ = 0.9828; $R^2_{aj}$ = 0.9705;
$R^2_{pred}$ = 0.9184; Adeq Precision 23.018.

Coeficientes (codificados):

| Término | Estimación | Error est. | IC 95 % inf. | IC 95 % sup. | VIF |
|---|---|---|---|---|---|
| Intercepto | 79.94 | 0.12 | 79.66 | 80.22 | |
| A (tiempo) | 0.99 | 0.094 | 0.77 | 1.22 | 1.00 |
| B (temp.) | 0.52 | 0.094 | 0.29 | 0.74 | 1.00 |
| A² | −1.38 | 0.10 | −1.61 | −1.14 | 1.02 |
| B² | −1.00 | 0.10 | −1.24 | −0.76 | 1.02 |
| AB | 0.25 | 0.13 | −0.064 | 0.56 | 1.00 |

- Modelo codificado: $\hat y_1 = 79.94 + 0.99x_1 + 0.52x_2 - 1.38x_1^2 - 1.00x_2^2 + 0.25x_1x_2$.
- Modelo en unidades naturales: $\hat y_1 = -1430.52285 + 7.80749\,t + 13.27053\,T - 0.055050\,t^2 - 0.040050\,T^2 + 0.010000\,tT$.
- Diagnósticos por corrida: leverage 0.625 en los 8 puntos factoriales/axiales y 0.200 en los
  centros; residuales estudentizados entre −1.283 y 1.513; distancia de Cook máxima 0.457;
  $t$ de outlier máximo 1.708 (sin puntos anómalos).
- **Punto estacionario**:

$$\mathbf{b} = \begin{bmatrix}0.995\\0.515\end{bmatrix},\quad
\mathbf{B} = \begin{bmatrix}-1.376 & 0.1250\\ 0.1250 & -1.001\end{bmatrix},\quad
\mathbf{x}_s = -\tfrac12\begin{bmatrix}-0.7345 & -0.0917\\ -0.0917 & -1.0096\end{bmatrix}\begin{bmatrix}0.995\\0.515\end{bmatrix} = \begin{bmatrix}0.389\\0.306\end{bmatrix}$$

  En unidades naturales: $\xi_1 = 86.95 \approx 87$ min, $\xi_2 = 176.53 \approx 176.5$ °F;
  $\hat y_s = 80.21$. La gráfica de contorno (fig. 11-11) muestra un máximo cerca de 85 min y 175 °F
  y un proceso algo más sensible al tiempo que a la temperatura.
- **Análisis canónico**: $|\mathbf{B}-\lambda\mathbf{I}| = 0 \Rightarrow \lambda^2 + 2.3788\lambda + 1.3639 = 0$;
  $\lambda_1 = -0.9641$, $\lambda_2 = -1.4147$.

$$\hat y = 80.21 - 0.9641\,w_1^2 - 1.4147\,w_2^2$$

  Ambos negativos y $\mathbf{x}_s$ dentro de la región → **máximo**. La superficie es menos sensible
  en la dirección $w_1$.
- **Eigenvectores**: para $\lambda_1$: $-0.4129m_{11} + 0.1250m_{21} = 0$; con $m^*_{21}=1$,
  $m^*_{11}=0.3027$, norma 1.0448 → $m_{11}=0.2897$, $m_{21}=0.9571$. Para $\lambda_2$:
  $m_{12}=-0.9574$, $m_{22}=0.2888$.

$$\mathbf{M} = \begin{bmatrix}0.2897 & -0.9574\\ 0.9571 & 0.2888\end{bmatrix}$$

$$w_1 = 0.2897(x_1-0.389) + 0.9571(x_2-0.306),\qquad w_2 = -0.9574(x_1-0.389) + 0.2888(x_2-0.306)$$

### 11-3.3 Sistemas de cordilleras

Parten de la forma canónica (ec. 11-9) cuando uno o más $\lambda_i \approx 0$: la respuesta es casi
insensible a las $w_i$ correspondientes.

| Situación | Nombre | Consecuencia |
|---|---|---|
| $\mathbf{x}_s$ **dentro** de la región experimental y algún $\lambda_i \approx 0$ | **Cordillera estacionaria** (fig. 11-12; con $k=2$, $\hat y = \hat y_s + \lambda_2 w_2^2$, $\lambda_2<0$) | Hay una línea (o plano) de óptimos: el óptimo puede tomarse en cualquier punto a lo largo de $w_1$, lo que da flexibilidad para elegir condiciones de operación. |
| $\mathbf{x}_s$ **muy lejos** de la región y algún $\lambda_i \approx 0$ | **Cordillera creciente** (fig. 11-13, $\lambda_2<0$); si $\lambda_2>0$, **cordillera descendente** | No se pueden hacer inferencias sobre la superficie verdadera ni sobre $\mathbf{x}_s$ (está fuera de donde se ajustó el modelo); conviene seguir explorando en la dirección $w_1$. |

En la práctica $\lambda_i$ no será exactamente cero, solo cercano.

### 11-3.4 Respuestas múltiples

Procedimiento general: (1) ajustar un modelo de superficie de respuesta adecuado para **cada**
respuesta; (2) buscar condiciones de operación que optimicen todas en algún sentido o al menos las
mantengan en los rangos deseados.

Modelos de las otras respuestas del ejemplo 11-2:

- Viscosidad: $\hat y_2 = 70.00 - 0.16x_1 - 0.95x_2 - 0.69x_1^2 - 6.69x_2^2 - 1.25x_1x_2$
  (natural: $\hat y_2 = -9030.74 + 13.393\xi_1 + 97.708\xi_2 - 2.75\times10^{-2}\xi_1^2 - 0.26757\xi_2^2 - 5\times10^{-2}\xi_1\xi_2$).
- Peso molecular: $\hat y_3 = 3386.2 + 205.1x_1 + 17.4x_2$
  (natural: $\hat y_3 = -6308.8 + 41.025\xi_1 + 35.473\xi_2$).

**a) Superposición de gráficas de contorno.** Funciona bien con pocas variables. Se superponen los
contornos límite de cada respuesta y se examina visualmente la región factible. Ejemplo (fig. 11-16):
$y_1 \ge 78.5$, $62 \le y_2 \le 68$, $y_3 \le 3400$ → quedan dos regiones factibles (una mayor que la
otra). Limitación: con más de tres variables hay que fijar $k-2$ de ellas para cada gráfica y se
requiere mucho ensayo y error.

**b) Optimización restringida** (programación no lineal). Ejemplo:

$$\max\ y_1 \quad \text{sujeto a}\quad 62 \le y_2 \le 68,\quad y_3 \le 3400$$

Design-Expert (búsqueda directa) da dos soluciones: (tiempo 83.5, temp. 177.1, $\hat y_1 = 79.5$) en
la región factible superior (la pequeña) y (tiempo 86.6, temp. 172.25, $\hat y_1 = 79.5$) en la región
grande. Ambas quedan muy cerca de los límites de las restricciones.

**c) Funciones de deseabilidad ("condición de deseable", Derringer y Suich).** Cada respuesta $y_i$
se convierte en una deseabilidad individual $0 \le d_i \le 1$ ($d_i = 1$ si está en su objetivo,
$d_i = 0$ si está fuera de la región aceptable). Se eligen las variables de diseño que maximizan la
deseabilidad global de las $m$ respuestas:

$$D = (d_1\cdot d_2\cdots d_m)^{1/m}$$

Con objetivo $T$, límite inferior $L$, límite superior $U$ y ponderaciones $r$ (fig. 11-17):

- Objetivo = **máximo** (ec. 11-11):

$$d = \begin{cases} 0 & y < L\\[4pt] \left(\dfrac{y-L}{T-L}\right)^{r} & L \le y \le T\\[8pt] 1 & y > T\end{cases}$$

- Objetivo = **mínimo** (ec. 11-12):

$$d = \begin{cases} 1 & y < T\\[4pt] \left(\dfrac{U-y}{U-T}\right)^{r} & T \le y \le U\\[8pt] 0 & y > U\end{cases}$$

- Objetivo = **valor nominal** entre $L$ y $U$, dos colas (ec. 11-13):

$$d = \begin{cases} 0 & y < L\\[4pt] \left(\dfrac{y-L}{T-L}\right)^{r_1} & L \le y \le T\\[8pt] \left(\dfrac{U-y}{U-T}\right)^{r_2} & T \le y \le U\\[8pt] 0 & y > U\end{cases}$$

Ponderación: $r = 1$ → función lineal; $r > 1$ → se da más importancia a estar cerca del objetivo;
$0 < r < 1$ → menos importancia.

Aplicación al ejemplo 11-2: rendimiento con $T = 80$ y límite 70, $r = 1$ (el libro escribe
"$U = 70$"; por ser un objetivo de máximo corresponde al límite inferior $L$ — posible errata,
pág. 452); viscosidad con $T = 65$, $L = 62$, $U = 68$, $r_1 = r_2 = 1$; peso molecular aceptable por
debajo de 3400. Soluciones:

| | Tiempo | Temperatura | $D$ | $\hat y_1$ | $\hat y_2$ | $\hat y_3$ |
|---|---|---|---|---|---|---|
| Solución 1 | 86.5 | 170.5 | 0.822 | 78.8 | 65 | 3287 |
| Solución 2 | 82 | 178.8 | 0.792 | 78.5 | 65 | 3400 |

La solución 1 (mayor $D$) cae en la región factible grande de la fig. 11-16; la 2, en la pequeña.
La fig. 11-18 muestra la superficie de $D$.

---

## 11-4 Diseños experimentales para ajustar superficies de respuesta

**Características deseables de un diseño de superficie de respuesta** (pág. 455):

1. Distribución razonable de puntos (información) en toda la región de interés.
2. Permite investigar la adecuación del modelo, incluida la falta de ajuste.
3. Permite experimentar en bloques.
4. Permite construir secuencialmente diseños de orden superior.
5. Da una estimación interna del error.
6. Da estimaciones precisas de los coeficientes.
7. Buen perfil de la varianza de predicción en toda la región.
8. Robustez razonable ante puntos atípicos o valores faltantes.
9. No requiere muchas corridas.
10. No requiere demasiados niveles de las variables.
11. Cálculo sencillo de los parámetros.

Estas propiedades entran en conflicto entre sí; elegir un diseño exige criterio.

### 11-4.1 Diseños para ajustar el modelo de primer orden

Modelo (ec. 11-14): $y = \beta_0 + \sum_{i=1}^{k}\beta_i x_i + \varepsilon$.

- **Diseños de primer orden ortogonales**: única clase que minimiza la varianza de los
  $\{\hat\beta_i\}$. Un diseño es ortogonal si los elementos fuera de la diagonal de
  $\mathbf{X}'\mathbf{X}$ son cero (los productos cruzados de las columnas de $\mathbf{X}$ suman cero).
- Incluye los factoriales $2^k$ y las fracciones $2^{k-p}$ en las que los efectos principales no son
  alias entre sí, con niveles codificados $\pm1$.
- El $2^k$ sin réplicas no estima el error. Remedio habitual: **puntos centrales**
  ($x_i = 0$ para todo $i$). No cambian los $\hat\beta_i$ ($i\ge1$); $\hat\beta_0$ pasa a ser el gran
  promedio de todas las observaciones; no alteran la ortogonalidad.
- **Diseño símplex**: otro diseño ortogonal de primer orden; figura regular con $k+1$ vértices en
  $k$ dimensiones (triángulo equilátero para $k=2$, tetraedro regular para $k=3$; fig. 11-19).
- Todo diseño de primer orden ortogonal es rotable (pág. 457).

### 11-4.2 Diseños para ajustar el modelo de segundo orden

#### Diseño central compuesto (DCC)

La clase más usada. Componentes (fig. 11-20):

| Parte | Corridas | Función |
|---|---|---|
| Factorial $2^k$ (o fraccionado de **resolución V**) | $n_F$ | Efectos lineales e interacciones |
| Axiales o estrella, a distancia $\pm\alpha$ sobre cada eje | $2k$ | Términos cuadráticos puros |
| Centrales | $n_C$ | Error puro y estabilidad de la varianza de predicción |

Se presta a la **experimentación secuencial**: $2^k$ + centros para el modelo de primer orden →
falta de ajuste → se agregan los axiales. Parámetros por especificar: $\alpha$ y $n_C$.

**Rotabilidad.** Varianza de la respuesta predicha en un punto $\mathbf{x}$ (ec. 10-40):

$$V[\hat y(\mathbf{x})] = \sigma^2\,\mathbf{x}'(\mathbf{X}'\mathbf{X})^{-1}\mathbf{x}$$

Un diseño es **rotable** (Box y Hunter) si $V[\hat y(\mathbf{x})]$ es igual en todos los puntos a la
misma distancia del centro (constante sobre esferas; contornos de $\sqrt{V[\hat y(\mathbf{x})]}$
circulares, fig. 11-21). Justificación: antes de experimentar no se sabe dónde está el óptimo, así
que conviene igual precisión en todas las direcciones. El DCC es rotable con

$$\alpha = (n_F)^{1/4}$$

(p. ej. $k=2$: $\alpha = 1.414$; $k=3$: $1.682$; $k=4$: $2.000$).

**DCC esférico.** La rotabilidad es una propiedad esférica y no hace falta que sea exacta. Para una
región de interés esférica, la mejor elección desde el punto de vista de la varianza de predicción es

$$\alpha = \sqrt{k}$$

que coloca todos los puntos factoriales y axiales sobre una esfera de radio $\sqrt{k}$.

**Corridas centrales.** Con región esférica el diseño necesita puntos centrales para que la varianza
de predicción sea razonablemente estable: se recomiendan **de 3 a 5**.

**DCC con centros en las caras (cubo con centros en las caras), $\alpha = 1$.** Para región de interés
**cuboidal** (fig. 11-23). Ventaja: solo 3 niveles por factor (útil cuando es difícil cambiar
niveles). **No es rotable.** Necesita menos centros que el esférico: $n_C = 2$ o $3$ basta para una
buena varianza de predicción (se usan más si se quiere una estimación razonable del error). Fig.
11-24 ($k=3$, $n_C=3$, $x_3=0$): $\sqrt{V[\hat y(\mathbf{x})]}$ bastante uniforme en buena parte del
espacio de diseño.

#### Diseño de Box-Behnken

- Diseños de **tres niveles** formados combinando factoriales $2^k$ con diseños de bloques
  incompletos. Eficientes en número de corridas; rotables o casi rotables.
- $k=3$ (tabla 11-8, fig. 11-22), 15 corridas: 12 puntos en los puntos medios de las aristas del
  cubo + 3 centros.

| Corridas | $x_1$ | $x_2$ | $x_3$ |
|---|---|---|---|
| 1–4 | $\pm1$ | $\pm1$ | 0 |
| 5–8 | $\pm1$ | 0 | $\pm1$ |
| 9–12 | 0 | $\pm1$ | $\pm1$ |
| 13–15 | 0 | 0 | 0 |

- Es un diseño **esférico**: todos los puntos (salvo el centro) sobre una esfera de radio $\sqrt2$.
- **No tiene puntos en los vértices** del cubo: ventaja cuando las combinaciones extremas son
  costosas o físicamente imposibles.

#### Otros diseños

- **Equirradiales** ($k=2$): puntos igualmente espaciados sobre un círculo (polígonos regulares) más
  centro. Un diseño equirradial rotable se obtiene con $n_2 \ge 5$ puntos equiespaciados en el
  círculo y $n_1 \ge 1$ puntos en el centro. Útiles: **pentágono** y **hexágono** (fig. 11-25).
- **Diseño compuesto pequeño**: fracción en el cubo de **resolución III\*** (efectos principales
  alias de interacciones de dos factores, pero ninguna interacción de dos factores alias de otra) +
  axiales + centros. Para $k=3$ (tabla 11-9): fracción un medio del $2^3$ (4 corridas:
  $(1,1,-1)$, $(1,-1,1)$, $(-1,1,1)$, $(-1,-1,-1)$) + 6 axiales con $\alpha = 1.73$ + 4 centros = 14
  corridas. Mínimo $N = 11$ (con un solo centro) para $p = 10$ parámetros. No puede hacerse rotable;
  por eso se eligió $\alpha = 1.73 = \sqrt3$ (esférico).
- **Diseños híbridos**: muy pequeños y con excelente varianza de predicción, pero con niveles
  irregulares (limitante práctica). Ejemplo $k=3$, 11 corridas (tabla 11-10):

| Corrida | $x_1$ | $x_2$ | $x_3$ |
|---|---|---|---|
| 1 | 0 | 0 | 1.41 |
| 2 | 0 | 0 | −1.41 |
| 3–6 | $\pm1$ | $\pm1$ | 0.71 |
| 7, 8 | $\pm1.41$ | 0 | −0.71 |
| 9, 10 | 0 | $\pm1.41$ | −0.71 |
| 11 | 0 | 0 | 0 |

### 11-4.3 Formación de bloques en los diseños de superficie de respuesta

**Cuándo.** Sobre todo cuando un diseño de segundo orden se arma secuencialmente a partir de uno de
primer orden y entre ambas etapas pasa suficiente tiempo para que cambien las condiciones.

**Bloques ortogonales**: el diseño se divide en bloques de modo que los efectos de bloque no afectan
las estimaciones de los parámetros del modelo.

- Diseños de primer orden $2^k$ o $2^{k-p}$: usar los métodos del cap. 7 para formar $2^r$ bloques;
  los puntos centrales se reparten **por igual** entre los bloques.
- Diseños de segundo orden: con $n_b$ observaciones en el bloque $b$, deben cumplirse dos condiciones:

1. Cada bloque es un diseño ortogonal de primer orden:

$$\sum_{u=1}^{n_b} x_{iu}x_{ju} = 0,\qquad i \ne j = 0,1,\dots,k,\ \text{para todo } b \quad (x_{0u}=1)$$

2. La fracción de la suma de cuadrados total de cada variable aportada por cada bloque es igual a la
   fracción de observaciones que contiene el bloque:

$$\frac{\sum_{u=1}^{n_b} x_{iu}^2}{\sum_{u=1}^{N} x_{iu}^2} = \frac{n_b}{N},\qquad i = 1,2,\dots,k,\ \text{para todo } b$$

**Ejemplo de verificación**: DCC rotable con $k=2$, $N=12$. Bloque 1 = 4 puntos factoriales + 2
centros; bloque 2 = 4 axiales ($\alpha=1.414$) + 2 centros. En cada bloque $\sum x_{iu}^2 = 4$, total
8, $n_b = 6$: $4/8 = 6/12$ → se cumple en ambos; el diseño está en bloques ortogonales.

**DCC en dos bloques, caso general.** Bloque 1: $n_F$ factoriales + $n_{CF}$ centros; bloque 2:
$n_A = 2k$ axiales + $n_{CA}$ centros. La condición 1 se cumple siempre, sea cual sea $\alpha$. La
condición 2 exige (ec. 11-15)

$$\frac{\sum_{u}^{n_2} x_{iu}^2}{\sum_{u}^{n_1} x_{iu}^2} = \frac{n_A + n_{CA}}{n_F + n_{CF}}$$

cuyo miembro izquierdo vale $2\alpha^2/n_F$; por tanto (ec. 11-16)

$$\alpha = \left[\frac{n_F\,(n_A + n_{CA})}{2\,(n_F + n_{CF})}\right]^{1/2}$$

Este $\alpha$ en general no da rotabilidad ni esfericidad. Para tener además rotabilidad
($\alpha = n_F^{1/4}$) se necesita (ec. 11-17)

$$(n_F)^{1/2} = \frac{n_F\,(n_A + n_{CA})}{2\,(n_F + n_{CF})}$$

que no siempre tiene solución exacta. Ejemplo $k=3$ ($n_F=8$, $n_A=6$):
$2.83 = (48 + 8n_{CA})/(16 + 2n_{CF})$ no tiene solución entera, pero con $n_{CF}=3$, $n_{CA}=2$ el
segundo miembro vale 2.91 → bloques **casi ortogonales**. En la práctica se puede relajar un poco la
rotabilidad o la ortogonalidad de bloques sin pérdida importante de información.

Si $k$ es grande, la porción factorial puede dividirse en dos o más bloques (número de bloques
factoriales = potencia de 2) y la porción axial forma un solo bloque.

Tabla 11-11 — DCC rotables y casi rotables que se separan en bloques ortogonales:

| $k$ | 2 | 3 | 4 | 5 | 5 (½ rép.) | 6 | 6 (½ rép.) | 7 | 7 (½ rép.) |
|---|---|---|---|---|---|---|---|---|---|
| **Bloques factoriales** | | | | | | | | | |
| $n_F$ | 4 | 8 | 16 | 32 | 16 | 64 | 32 | 128 | 64 |
| Número de bloques | 1 | 2 | 2 | 4 | 1 | 8 | 2 | 16 | 8 |
| Puntos factoriales por bloque | 4 | 4 | 8 | 8 | 16 | 8 | 16 | 8 | 8 |
| Puntos centrales por bloque | 3 | 2 | 2 | 2 | 6 | 1 | 4 | 1 | 1 |
| Total de puntos por bloque | 7 | 6 | 10 | 10 | 22 | 9 | 20 | 9 | 9 |
| **Bloque axial** | | | | | | | | | |
| $n_A$ | 4 | 6 | 8 | 10 | 10 | 12 | 12 | 14 | 14 |
| $n_{CA}$ | 3 | 2 | 2 | 4 | 1 | 6 | 2 | 11 | 4 |
| Total de puntos del bloque axial | 7 | 8 | 10 | 14 | 11 | 18 | 14 | 25 | 18 |
| **Total $N$ del diseño** | 14 | 20 | 30 | 54 | 33 | 90 | 54 | 169 | 80 |
| $\alpha$ para bloques ortogonales | 1.4142 | 1.6330 | 2.0000 | 2.3664 | 2.0000 | 2.8284 | 2.3664 | 3.3636 | 2.8284 |
| $\alpha$ para rotabilidad | 1.4142 | 1.6818 | 2.0000 | 2.3784 | 2.0000 | 2.8284 | 2.3784 | 3.3333 | 2.8284 |

(Los valores 3.3636 y 3.3333 de $k=7$ se transcriben tal como aparecen impresos, pág. 465; nótese
que $128^{1/4} = 3.3636$, por lo que las dos cifras podrían estar intercambiadas en el libro.)

**ANOVA cuando se corre en bloques**:

- **Error puro**: solo los puntos centrales corridos en el **mismo bloque** son réplicas; el error
  puro se calcula dentro de cada bloque y se agrupa entre bloques si la variabilidad es consistente.
- **Suma de cuadrados de bloques** con $m$ bloques ortogonales (ec. 11-18):

$$SS_{\text{Bloques}} = \sum_{b=1}^{m}\frac{B_b^2}{n_b} - \frac{G^2}{N}$$

  $B_b$ = total de las $n_b$ observaciones del bloque $b$; $G$ = gran total; $m-1$ g.l.
- Si los bloques no son exactamente ortogonales, usar la prueba general de significación de la
  regresión (método de la "suma de cuadrados extra", cap. 10).

### 11-4.4 Diseños (óptimos) generados por computadora

Los diseños estándar (DCC, Box-Behnken, cubo con centros en las caras) sirven cuando la región es un
cubo o una esfera. Los diseños generados por computadora son alternativa en tres situaciones:

1. **Región experimental irregular.** Ejemplo del adhesivo ($x_1$ = cantidad de adhesivo, $x_2$ =
   temperatura de curado, ambos en $[-1, 1]$) con restricciones $-1.5 \le x_1 + x_2$ y
   $x_1 + x_2 \le 1$, que recortan dos vértices del cuadrado (fig. 11-26; regiones tipo "lata
   abollada"). Ningún diseño estándar se ajusta exactamente.
2. **Modelo no estándar.** Conocimiento del proceso que sugiere términos especiales, p. ej.

$$y = \beta_0 + \beta_1x_1 + \beta_2x_2 + \beta_{12}x_1x_2 + \beta_{11}x_1^2 + \beta_{22}x_2^2 + \beta_{112}x_1^2x_2 + \beta_{1112}x_1^3x_2 + \varepsilon$$

   o factores **categóricos** entre las variables del diseño.
3. **Requerimientos inusuales de tamaño de muestra.** P. ej. segundo orden en 4 variables: el DCC
   pide 28–30 corridas para un modelo de 15 términos. Advertencia del autor: para reducir corridas
   suele haber opciones mejores que el diseño por computadora (compuesto pequeño de 20 corridas con 4
   centros, o híbrido de 16 corridas).

**Procedimiento** (teoría de diseños optimales de Kiefer y Kiefer–Wolfowitz): especificar el modelo
→ definir la región de interés → fijar el número de corridas → elegir el criterio de optimalidad →
seleccionar los puntos de un conjunto de **puntos candidatos** (normalmente una rejilla sobre la
región factible).

**Criterios de optimalidad alfabética**:

| Criterio | Definición | Qué optimiza |
|---|---|---|
| **D** | Minimiza $\lvert(\mathbf{X}'\mathbf{X})^{-1}\rvert$ | Volumen de la región de confianza conjunta de los coeficientes de regresión. El más usado. |
| **A** | Minimiza $\mathrm{tr}\,(\mathbf{X}'\mathbf{X})^{-1}$ | Suma de las varianzas de los coeficientes de regresión. |
| **G** | Minimiza el máximo en la región de $N\,V[\hat y(\mathbf{x})]/\sigma^2$ | Peor varianza de predicción escalada. |
| **V** | Minimiza la varianza de predicción **promedio** sobre un conjunto de $m$ puntos de interés $\mathbf{x}_1,\dots,\mathbf{x}_m$ (los candidatos u otros puntos relevantes) | Varianza de predicción media. |

D y A atienden a la estimación de parámetros; G y V son **criterios de la varianza de predicción**
(de interés cuando el fin es predecir la respuesta). El libro no usa el nombre "I-optimalidad"; el
criterio V es el de varianza de predicción promedio.

Eficiencias:

$$D_e = \left(\frac{\lvert(\mathbf{X}_2'\mathbf{X}_2)^{-1}\rvert}{\lvert(\mathbf{X}_1'\mathbf{X}_1)^{-1}\rvert}\right)^{1/p}\quad(11\text{-}19)
\qquad\qquad
G_e = \frac{p}{\max\ \dfrac{N\,V[\hat y(\mathbf{x})]}{\sigma^2}}\quad(11\text{-}20)$$

($D_e$: eficiencia relativa del diseño 1 respecto del diseño 2; $p$ = número de parámetros.
$1/D_e$ = número de réplicas del diseño 1 necesarias para igualar la precisión del diseño 2.)

**Casos con solución analítica**: el $2^k$ es optimal D, A, G y V para el modelo de primer orden en
$k$ variables y para el de primer orden con interacción.

**Algoritmo de intercambio**: se parte de una matriz de candidatos y un diseño inicial (quizá al
azar); el algoritmo intercambia puntos del diseño con candidatos que no están en él para mejorar el
criterio. No evalúa todos los diseños posibles → no garantiza el óptimo, pero suele quedar cerca;
algunas implementaciones repiten el proceso desde varios diseños iniciales.

**Ilustración (adhesivo, modelo de segundo orden, $p = 6$, 12 corridas)**:

| Diseño | $\lvert(\mathbf{X}'\mathbf{X})^{-1}\rvert$ | $\mathrm{tr}\,(\mathbf{X}'\mathbf{X})^{-1}$ | $D_e$ respecto al optimal D |
|---|---|---|---|
| DCC inscrito en la región, 4 centros (fig. 11-27); no rotable | 1.852E-2 | 6.375 | $(0.0002153/0.01852)^{1/6} = 0.476$ |
| Optimal D de Design-Expert (tabla 11-12, fig. 11-28) | 2.153E-4 | 2.516 | 1 |
| Optimal D modificado (fig. 11-29) | 3.71E-4 | 2.448 | $(0.0002153/0.000371)^{1/6} = 0.91$ |

- El DCC inscrito tiene eficiencia 47.6 %: harían falta $1/0.476 = 2.1$ réplicas para igualar al
  optimal D. Su desviación estándar de predicción es peor sobre todo cerca de los límites de la
  región, donde no tiene puntos.
- Puntos del optimal D (tabla 11-12): $(-0.50,-1)$, $(1,0)$ ×2, $(-0.08,-0.08)$ ×2, $(-1,1)$,
  $(1,-1)$, $(0,1)$ ×2, $(-1,0.25)$, $(0.25,-1)$, $(-1,-0.50)$.
- El **modificado** traslada al centro las dos réplicas de los vértices, porque en el optimal D la
  desviación estándar de predicción sube ligeramente cerca del centro. Queda casi tan eficiente
  (91 %) y con contornos de predicción al menos tan buenos, sobre todo en el centro. (El libro dice
  que su traza, 2.448, es "ligeramente mayor" que la del optimal D, 2.516; las cifras impresas
  indican lo contrario — dudoso, pág. 472.)

**Advertencias del autor**: los diseños alfabéticamente optimales son útiles cuando la región no es
esférica ni cuboidal, pero **no sustituyen** a los diseños estándar en la mayoría de los problemas.
Se generan atendiendo a un único criterio, mientras que la lista de propiedades deseables de la
sección 11-4 incluye varios criterios, algunos cualitativos; en problemas reales hay que evaluar
muchos a la vez (Myers y Montgomery, cap. 8).

---

## Resumen operativo (secciones 11-1 a 11-4)

1. Codificar los factores; correr $2^k$ (o $2^{k-p}$) + centros alrededor de las condiciones actuales.
2. Ajustar el modelo de primer orden; probar interacción y curvatura con el error puro de los centros.
3. Sin curvatura: avanzar por la trayectoria de ascenso/descenso más pronunciado
   ($\Delta x_i = \hat\beta_i/(\hat\beta_j/\Delta x_j)$) hasta que la respuesta deje de mejorar; repetir.
4. Con curvatura: aumentar a DCC (axiales con $\alpha = n_F^{1/4}$, $\sqrt k$ o 1 según la región;
   3–5 centros en región esférica, 2–3 en cuboidal) o usar Box-Behnken; bloquear ortogonalmente si las
   etapas se corren en momentos distintos.
5. Ajustar el modelo de segundo orden; verificar falta de ajuste, PRESS y diagnósticos.
6. Hallar $\mathbf{x}_s = -\tfrac12\mathbf{B}^{-1}\mathbf{b}$ y $\hat y_s = \hat\beta_0 + \tfrac12\mathbf{x}_s'\mathbf{b}$;
   caracterizar con los eigenvalores de $\mathbf{B}$ (máximo, mínimo, silla, cordillera).
7. Con varias respuestas: superponer contornos, optimizar con restricciones o maximizar la
   deseabilidad global $D$.
