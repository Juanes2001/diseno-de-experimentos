# Capítulo 10 — Ajuste de modelos de regresión

> Montgomery, págs. 392–426

> **Nota sobre el escaneo:** las págs. 400–401 del libro **no están en el PDF** (se salta de la
> 399 a la 402). Contenían el final del ejemplo 10-1 (modelo ajustado y figuras 10-1 a 10-4, que
> por contexto son las gráficas de residuales). Lo que falta se marca abajo como tal.

## Índice rápido

| Sección | Tema | Ecuaciones |
|---|---|---|
| 10-1 | Introducción | — |
| 10-2 | Modelos de regresión lineal | 10-1 a 10-6 |
| 10-3 | Estimación por mínimos cuadrados; regresión en experimentos diseñados | 10-7 a 10-19 |
| 10-4 | Pruebas de hipótesis (significación, $R^2$, $t$, suma de cuadrados extra) | 10-20 a 10-36 |
| 10-5 | Intervalos de confianza (coeficientes, respuesta media) | 10-37 a 10-41 |
| 10-6 | Predicción de nuevas observaciones | 10-42 |
| 10-7 | Diagnósticos (residuales escalados, PRESS, R-student, leverage, Cook) | 10-43 a 10-55 |
| 10-8 | Prueba de falta de ajuste | 10-56 a 10-62 |
| 10-9 | Problemas | — |

---

## 10-1 Introducción

- Se tiene una respuesta $y$ que depende de $k$ regresores $x_1,\dots,x_k$. La relación verdadera
  $y=\phi(x_1,\dots,x_k)$ casi nunca se conoce; se aproxima con un **modelo empírico**,
  normalmente un polinomio de orden bajo.
- Relación diseño ↔ regresión: el modelo de regresión es la forma cuantitativa de expresar los
  resultados de un experimento (es lo que se ha hecho en los caps. 6–8 con los $2^k$ y $2^{k-p}$).
- Usos de la regresión que destaca el autor:
  1. Datos de **experimentos no planeados** (registros históricos, fenómenos no controlados).
  2. Experimentos diseñados en los que **"algo salió mal"** (corrida faltante, niveles que no se
     alcanzaron, necesidad de separar alias con pocas corridas). Es el hilo conductor del capítulo.
- Referencias para profundizar: Montgomery y Peck [82], Myers [84].

## 10-2 Modelos de regresión lineal

Modelo de regresión lineal múltiple con $k$ regresores (ec. 10-2):

$$y=\beta_0+\beta_1x_1+\beta_2x_2+\cdots+\beta_kx_k+\varepsilon$$

- $\beta_j$ = **coeficiente de regresión parcial**: cambio esperado en $y$ por cambio unitario de
  $x_j$ con los demás regresores constantes. $\beta_0$ = ordenada al origen.
- "Lineal" se refiere a linealidad **en los parámetros**, no a la forma de la superficie.
  Cualquier modelo lineal en las $\beta$ es un modelo de regresión lineal:
  - Interacción (ec. 10-3): $y=\beta_0+\beta_1x_1+\beta_2x_2+\beta_{12}x_1x_2+\varepsilon$; con
    $x_3=x_1x_2$, $\beta_3=\beta_{12}$ queda en la forma estándar (ec. 10-4).
  - Superficie de respuesta de segundo orden (ec. 10-5):
    $y=\beta_0+\beta_1x_1+\beta_2x_2+\beta_{11}x_1^2+\beta_{22}x_2^2+\beta_{12}x_1x_2+\varepsilon$;
    con $x_3=x_1^2$, $x_4=x_2^2$, $x_5=x_1x_2$ es lineal con 5 regresores (ec. 10-6).
- **Ajuste del modelo** = estimación de los parámetros.

## 10-3 Estimación de los parámetros en modelos de regresión lineal

### Planteamiento y supuestos

- Datos: $n>k$ observaciones $(y_i, x_{i1},\dots,x_{ik})$ (tabla 10-1).
- Supuestos para la estimación: $E(\varepsilon)=0$, $V(\varepsilon)=\sigma^2$, errores **no
  correlacionados**. (La normalidad solo se exige para pruebas e intervalos, secc. 10-4 y 10-5.)
- Modelo por observación (ec. 10-7):
  $y_i=\beta_0+\sum_{j=1}^{k}\beta_jx_{ij}+\varepsilon_i,\quad i=1,\dots,n$.

### Mínimos cuadrados, forma escalar

Función a minimizar (ec. 10-8):

$$L=\sum_{i=1}^{n}\varepsilon_i^2=\sum_{i=1}^{n}\Big(y_i-\beta_0-\sum_{j=1}^{k}\beta_jx_{ij}\Big)^2$$

Derivando respecto de $\beta_0$ y de cada $\beta_j$ e igualando a cero (ecs. 10-9a, 10-9b) se
obtienen las $p=k+1$ **ecuaciones normales** (ec. 10-10):

$$
\begin{aligned}
n\hat\beta_0+\hat\beta_1\sum x_{i1}+\cdots+\hat\beta_k\sum x_{ik}&=\sum y_i\\
\hat\beta_0\sum x_{i1}+\hat\beta_1\sum x_{i1}^2+\cdots+\hat\beta_k\sum x_{i1}x_{ik}&=\sum x_{i1}y_i\\
&\;\;\vdots\\
\hat\beta_0\sum x_{ik}+\hat\beta_1\sum x_{ik}x_{i1}+\cdots+\hat\beta_k\sum x_{ik}^2&=\sum x_{ik}y_i
\end{aligned}
$$

### Mínimos cuadrados, forma matricial

$$\mathbf y=\mathbf X\boldsymbol\beta+\boldsymbol\varepsilon$$

| Objeto | Dimensión | Contenido |
|---|---|---|
| $\mathbf y$ | $n\times1$ | observaciones |
| $\mathbf X$ | $n\times p$ | columna de unos + niveles de los regresores |
| $\boldsymbol\beta$ | $p\times1$ | coeficientes ($p=k+1$) |
| $\boldsymbol\varepsilon$ | $n\times1$ | errores aleatorios |

$$L=\boldsymbol\varepsilon'\boldsymbol\varepsilon=(\mathbf y-\mathbf X\boldsymbol\beta)'(\mathbf y-\mathbf X\boldsymbol\beta)
=\mathbf y'\mathbf y-2\boldsymbol\beta'\mathbf X'\mathbf y+\boldsymbol\beta'\mathbf X'\mathbf X\boldsymbol\beta\qquad\text{(ec. 10-11)}$$

$$\frac{\partial L}{\partial\boldsymbol\beta}\Big|_{\hat{\boldsymbol\beta}}=-2\mathbf X'\mathbf y+2\mathbf X'\mathbf X\hat{\boldsymbol\beta}=\mathbf 0
\;\Rightarrow\;\mathbf X'\mathbf X\hat{\boldsymbol\beta}=\mathbf X'\mathbf y\qquad\text{(ec. 10-12)}$$

$$\boxed{\hat{\boldsymbol\beta}=(\mathbf X'\mathbf X)^{-1}\mathbf X'\mathbf y}\qquad\text{(ec. 10-13)}$$

Estructura de las matrices:

- $\mathbf X'\mathbf X$ es simétrica $p\times p$: en la **diagonal** van las sumas de cuadrados
  de las columnas de $\mathbf X$; **fuera de la diagonal**, las sumas de productos cruzados entre
  columnas.
- $\mathbf X'\mathbf y$ es $p\times1$: sumas de productos cruzados de las columnas de $\mathbf X$
  con $\mathbf y$.

Modelo ajustado y residuales:

$$\hat{\mathbf y}=\mathbf X\hat{\boldsymbol\beta}\quad\text{(ec. 10-14)},\qquad
\hat y_i=\hat\beta_0+\sum_{j=1}^{k}\hat\beta_jx_{ij},\qquad
\mathbf e=\mathbf y-\hat{\mathbf y}\quad\text{(ec. 10-15)}$$

### Estimación de $\sigma^2$

$$SS_E=\sum_{i=1}^{n}(y_i-\hat y_i)^2=\mathbf e'\mathbf e
=\mathbf y'\mathbf y-\hat{\boldsymbol\beta}'\mathbf X'\mathbf y\qquad\text{(ec. 10-16)}$$

- Grados de libertad: $n-p$. Se cumple $E(SS_E)=\sigma^2(n-p)$.
- Estimador insesgado (ec. 10-17):

$$\hat\sigma^2=\frac{SS_E}{n-p}=MS_E$$

### Propiedades de los estimadores

- **Insesgamiento:**
  $E(\hat{\boldsymbol\beta})=E[(\mathbf X'\mathbf X)^{-1}\mathbf X'(\mathbf X\boldsymbol\beta+\boldsymbol\varepsilon)]=\boldsymbol\beta$,
  porque $E(\boldsymbol\varepsilon)=\mathbf 0$ y $(\mathbf X'\mathbf X)^{-1}\mathbf X'\mathbf X=\mathbf I$.
- **Matriz de covarianza** (ecs. 10-18, 10-19):

$$\operatorname{Cov}(\hat{\boldsymbol\beta})\equiv E\{[\hat{\boldsymbol\beta}-E(\hat{\boldsymbol\beta})][\hat{\boldsymbol\beta}-E(\hat{\boldsymbol\beta})]'\}=\sigma^2(\mathbf X'\mathbf X)^{-1}$$

  Simétrica; el elemento diagonal $j$ es $V(\hat\beta_j)=\sigma^2C_{jj}$ y el elemento $(i,j)$ es
  $\operatorname{Cov}(\hat\beta_i,\hat\beta_j)=\sigma^2C_{ij}$, con
  $\mathbf C=(\mathbf X'\mathbf X)^{-1}$.

### Ejemplo 10-1 — Viscosidad de un polímero (datos no planeados)

- $n=16$ observaciones; $y$ = viscosidad (centistokes a 100 °C), $x_1$ = temperatura de reacción
  (°C, de 80 a 100), $x_2$ = velocidad de alimentación del catalizador (lb/h, de 8 a 13)
  (tabla 10-2). Modelo: $y=\beta_0+\beta_1x_1+\beta_2x_2+\varepsilon$ ($k=2$, $p=3$).
- Matrices:

$$\mathbf X'\mathbf X=\begin{bmatrix}16&1458&164\\1458&133{,}560&14{,}946\\164&14{,}946&1{,}726\end{bmatrix},\qquad
\mathbf X'\mathbf y=\begin{bmatrix}37{,}577\\3{,}429{,}550\\385{,}562\end{bmatrix}$$

$$(\mathbf X'\mathbf X)^{-1}=\begin{bmatrix}14.176004&-0.129746&-0.223453\\-0.129746&1.429184\times10^{-3}&-4.763947\times10^{-5}\\-0.223453&-4.763947\times10^{-5}&2.222381\times10^{-2}\end{bmatrix}$$

$$\hat{\boldsymbol\beta}=\begin{bmatrix}1566.07777\\7.62129\\8.58485\end{bmatrix}
\;\Rightarrow\;\hat y=1566.08+7.62x_1+8.58x_2$$

- Salida de Minitab (tabla 10-4), útil para validar software:

| Predictor | Coef | StDev | T | P |
|---|---|---|---|---|
| Constante | 1566.08 | 61.59 | 25.43 | 0.000 |
| Temp ($x_1$) | 7.6213 | 0.6184 | 12.32 | 0.000 |
| Feed Rate ($x_2$) | 8.585 | 2.439 | 3.52 | 0.004 |

  $S=16.36$, $R^2=92.7\%$, $R^2_{\text{ajustada}}=91.6\%$.

| Fuente | GL | SS | MS | F | P |
|---|---|---|---|---|---|
| Regresión | 2 | 44157 | 22079 | 82.50 | 0.000 |
| Error residual | 13 | 3479 | 268 | | |
| Total | 15 | 47636 | | | |

  Sumas de cuadrados secuenciales (Seq SS): Temp = 40841 (1 gl), Feed Rate = 3316 (1 gl).
  Valores más precisos usados en el texto: $\hat\sigma^2=MS_E=267.604$, $SS_R=44{,}157.1$,
  $S_{yy}=SS_T=47{,}635.9$, $R^2=0.92697$.
- Diagnósticos (tabla 10-3, columnas: $y_i$, $\hat y_i$, $e_i$, $h_{ii}$, residual
  studentizado, $D_i$, R-student). Valores extremos para contrastar con software:

| Obs. | $y_i$ | $\hat y_i$ | $e_i$ | $h_{ii}$ | $r_i$ | $D_i$ | R-student |
|---|---|---|---|---|---|---|---|
| 1 | 2256 | 2244.5 | 11.5 | 0.350 (máx.) | 0.87 | 0.137 | 0.87 |
| 6 | 2368 | 2389.3 | −21.3 | 0.265 | −1.52 | 0.277 | −1.61 |
| 8 | 2409 | 2383.6 | 25.4 (máx.) | 0.098 | 1.64 | 0.097 | 1.76 |
| 11 | 2440 | 2416.9 | 23.1 | 0.278 | 1.66 (máx.) | 0.354 (máx.) | 1.80 (máx.) |
| 14 | 2317 | 2316.9 | 0.1 | 0.185 | 0.01 | 0.000 | <0.01 |

- El resto del ejemplo (comentario del ajuste y gráficas de residuales, figs. 10-1 a 10-4) está
  en las págs. 400–401, **ausentes del escaneo**. Por las referencias posteriores (secc. 10-7) se
  sabe que el autor concluye que no hay puntos atípicos, de palanca ni influyentes.

### Ajuste de modelos de regresión en experimentos diseñados

Idea central: las estimaciones de efectos de un $2^k$ **son** estimaciones de mínimos cuadrados,
y la regresión permite analizar el experimento aunque el diseño haya quedado "dañado".

#### Ejemplo 10-2 — Regresión de un $2^3$ con 4 puntos centrales

- Rendimiento de un proceso químico; factores: temperatura (120/160 °C), presión (40/80 psig),
  concentración de catalizador (15/30 g/l); centro (140, 60, 22.5). 12 corridas (fig. 10-5).
- Codificación:
  $x_1=\dfrac{\text{Temp}-140}{20},\; x_2=\dfrac{\text{Presión}-60}{20},\; x_3=\dfrac{\text{Conc}-22.5}{7.5}$.
- Respuestas en orden estándar: 32, 46, 57, 65, 36, 48, 57, 68; centros: 50, 44, 53, 56.
- Modelo de efectos principales $y=\beta_0+\beta_1x_1+\beta_2x_2+\beta_3x_3+\varepsilon$:

$$\mathbf X'\mathbf X=\operatorname{diag}(12,8,8,8),\quad
\mathbf X'\mathbf y=\begin{bmatrix}612\\45\\85\\9\end{bmatrix},\quad
\hat{\boldsymbol\beta}=\begin{bmatrix}51.000\\5.625\\10.625\\1.125\end{bmatrix}$$

$$\hat y=51.000+5.625x_1+10.625x_2+1.125x_3$$

- Relación con los efectos: efecto de temperatura
  $T=\bar y_{T^+}-\bar y_{T^-}=56.75-45.50=11.25$ y $\hat\beta_1=11.25/2=5.625$.
  **En un $2^k$ el coeficiente de regresión es siempre la mitad del efecto.**

#### Ortogonalidad

- Si $\mathbf X'\mathbf X$ es **diagonal**: la inversa es trivial y
  $\operatorname{Cov}(\hat\beta_i,\hat\beta_j)=0$ (estimadores no correlacionados).
- Se logra cuando las columnas de $\mathbf X$ son **ortogonales** (producto interior cero entre
  columnas). Un diseño con esta propiedad es un **diseño ortogonal**.
- El factorial $2^k$ es ortogonal para ajustar el modelo de regresión lineal múltiple.
- Recomendación: si se pueden elegir los niveles de las $x$ antes de tomar datos, diseñar para
  que $\mathbf X'\mathbf X$ sea diagonal.

#### Ejemplo 10-3 — $2^3$ con una observación faltante

- Mismo experimento del ej. 10-2, pero se pierde la corrida 8 ($+,+,+$; $y=68$). Quedan 11
  observaciones. Se ajusta igual el modelo de efectos principales:

$$\mathbf X'\mathbf X=\begin{bmatrix}11&-1&-1&-1\\-1&7&-1&-1\\-1&-1&7&-1\\-1&-1&-1&7\end{bmatrix},\qquad
\mathbf X'\mathbf y=\begin{bmatrix}544\\-23\\17\\-59\end{bmatrix}$$

$$(\mathbf X'\mathbf X)^{-1}=\begin{bmatrix}
9.61538\times10^{-2}&1.92307\times10^{-2}&1.92307\times10^{-2}&1.92307\times10^{-2}\\
1.92307\times10^{-2}&0.15385&2.88462\times10^{-2}&2.88462\times10^{-2}\\
1.92307\times10^{-2}&2.88462\times10^{-2}&0.15385&2.88462\times10^{-2}\\
1.92307\times10^{-2}&2.88462\times10^{-2}&2.88462\times10^{-2}&0.15385\end{bmatrix}$$

$$\hat y=51.25+5.75x_1+10.75x_2+1.25x_3$$

- Conclusión: coeficientes muy parecidos a los del diseño completo; las conclusiones prácticas no
  cambian. **Costo:** se pierde la ortogonalidad ($\mathbf X'\mathbf X$ y su inversa ya no son
  diagonales), así que las estimaciones quedan correlacionadas.
- Procedimiento general para datos faltantes en un $2^k$: eliminar la fila, armar $\mathbf X$
  con las corridas disponibles y aplicar la ec. 10-13; no hace falta "estimar" el dato faltante.

#### Ejemplo 10-4 — Niveles imprecisos de los factores

- Mismo $2^3$ con centros, pero los niveles realmente alcanzados difieren de los nominales
  (tabla 10-5), sobre todo en temperatura; p. ej. corrida 1: (125, 41, 14) →
  $(-0.75,-0.95,-1.133)$; corrida 8: (165, 83, 30) → $(1.25, 1.15, 1)$. Las respuestas son las
  mismas del ej. 10-2.
- Procedimiento: construir $\mathbf X$ con los **niveles codificados reales** (no los nominales)
  y aplicar mínimos cuadrados.

$$\mathbf X'\mathbf X=\begin{bmatrix}12&0.60&0.25&0.2670\\0.60&8.18&0.31&-0.1403\\0.25&0.31&8.5375&-0.3437\\0.2670&-0.1403&-0.3437&9.2437\end{bmatrix},\qquad
\mathbf X'\mathbf y=\begin{bmatrix}612\\77.55\\161.50\\19.144\end{bmatrix}$$

$$\hat{\boldsymbol\beta}=\begin{bmatrix}50.36496\\5.41932\\10.16672\\1.07653\end{bmatrix}
\;\Rightarrow\;\hat y=50.36+5.42x_1+10.17x_2+1.08x_3$$

- Conclusión: muy poca diferencia con el ej. 10-2; la interpretación práctica no cambia.
  Discrepancias pequeñas en los niveles no importan; las grandes sí son motivo de preocupación y
  se manejan con regresión.
- Erratas del libro (pág. 406–407): el modelo ajustado aparece impreso como
  "$50.36+2x_1+\dots$" (el coeficiente correcto según el vector es 5.42); en la corrida 5 la
  tabla 10-5 muestra $x_3=1.14$ y la matriz $\mathbf X$ muestra $1.4$ (dudoso cuál se usó;
  con concentración 33 g/l la codificación da $(33-22.5)/7.5=1.4$).

#### Ejemplo 10-5 — Separación de alias (de-aliasing) en un factorial fraccionado

Problema: el **plegado (doblez) completo** de un diseño de resolución III (segunda fracción con
todos los signos invertidos) separa los efectos principales de las interacciones de dos
factores, pero exige un segundo grupo de corridas **del mismo tamaño** que el original. A menudo
basta con menos corridas si solo interesa separar ciertas interacciones; la regresión permite
ver cuáles.

Caso: diseño $2^{4-1}_{IV}$, fracción principal con $I=ABCD$ (tabla 8-3), 8 corridas. Resultan
grandes $A$, $B$, $C$, $D$ y la cadena de alias $AB+CD$. Se quiere el modelo

$$y=\beta_0+\beta_1x_1+\beta_2x_2+\beta_3x_3+\beta_4x_4+\beta_{12}x_1x_2+\beta_{34}x_3x_4+\varepsilon$$

1. Con las 8 corridas originales, en $\mathbf X$ la columna $x_1x_2$ es **idéntica** a la columna
   $x_3x_4$ → dependencia lineal → no se pueden estimar $\beta_{12}$ y $\beta_{34}$ a la vez.
   (El alias se ve como columnas iguales de $\mathbf X$.)
2. Alternativa obvia: correr la fracción alterna (8 corridas más, 16 en total).
3. Alternativa económica: agregar **una sola corrida** de la fracción alterna,
   $(x_1,x_2,x_3,x_4)=(-1,-1,-1,+1)$. En ella $x_1x_2=+1$ y $x_3x_4=-1$, las columnas dejan de
   ser idénticas y el modelo con ambas interacciones se puede ajustar; las magnitudes de
   $\hat\beta_{12}$ y $\hat\beta_{34}$ indican cuál interacción es la importante.
4. **Desventaja de la corrida única:** si hay efecto de tiempo/bloque entre las 8 primeras
   corridas y la novena (columna de bloque: $-1$ en las 8 primeras, $+1$ en la novena), los
   productos cruzados de la columna de bloque con las demás columnas no son cero: los bloques no
   son ortogonales a los tratamientos y el efecto de bloque contamina los coeficientes.
5. **Regla:** para conservar la ortogonalidad de los bloques hay que agregar un **número par** de
   corridas. Con estas cuatro se separan $AB$ y $CD$ y los bloques quedan ortogonales:

| $x_1$ | $x_2$ | $x_3$ | $x_4$ |
|---|---|---|---|
| −1 | −1 | −1 | +1 |
| +1 | −1 | −1 | −1 |
| −1 | +1 | +1 | +1 |
| +1 | +1 | +1 | −1 |

Procedimiento general de **aumento del diseño**: escribir la matriz $\mathbf X$ del modelo
reducido de interés, identificar las columnas dependientes y elegir corridas adicionales que
rompan la dependencia; evaluar cada estrategia con $(\mathbf X'\mathbf X)^{-1}$ (varianzas y
covarianzas de los coeficientes, ver problema 10-17). También existen **diseños generados por
computadora** para el aumento (cap. 11).

## 10-4 Prueba de hipótesis en la regresión múltiple

Supuesto adicional: $\varepsilon\sim NID(0,\sigma^2)$, de donde las $y_i$ son normales e
independientes con media $\beta_0+\sum_j\beta_jx_{ij}$ y varianza $\sigma^2$.

### 10-4.1 Prueba de significación de la regresión

Hipótesis (ec. 10-20):

$$H_0:\beta_1=\beta_2=\cdots=\beta_k=0\qquad H_1:\beta_j\neq0\ \text{para al menos una } j$$

Rechazar $H_0$ significa que al menos un regresor contribuye de manera significativa.

Partición (ec. 10-21): $SS_T=SS_R+SS_E$. Bajo $H_0$: $SS_R/\sigma^2\sim\chi^2_k$,
$SS_E/\sigma^2\sim\chi^2_{n-k-1}$, independientes.

Fórmulas de cálculo (ecs. 10-23 a 10-25):

$$SS_R=\hat{\boldsymbol\beta}'\mathbf X'\mathbf y-\frac{\left(\sum_{i=1}^{n}y_i\right)^2}{n},\qquad
SS_E=\mathbf y'\mathbf y-\hat{\boldsymbol\beta}'\mathbf X'\mathbf y,\qquad
SS_T=\mathbf y'\mathbf y-\frac{\left(\sum_{i=1}^{n}y_i\right)^2}{n}$$

Estadístico (ec. 10-22):

$$F_0=\frac{SS_R/k}{SS_E/(n-k-1)}=\frac{MS_R}{MS_E}$$

Rechazar $H_0$ si $F_0>F_{\alpha,k,n-k-1}$ (o si el valor $P<\alpha$).

Tabla ANOVA (tabla 10-6):

| Fuente de variación | Suma de cuadrados | Grados de libertad | Cuadrado medio | $F_0$ |
|---|---|---|---|---|
| Regresión | $SS_R$ | $k$ | $MS_R$ | $MS_R/MS_E$ |
| Error o residual | $SS_E$ | $n-k-1$ | $MS_E$ | |
| Total | $SS_T$ | $n-1$ | | |

Ejemplo (viscosidad, tabla 10-4): $F_0=82.50$, $P\approx0$ → al menos uno de $x_1$, $x_2$ tiene
coeficiente distinto de cero.

#### $R^2$ y $R^2$ ajustada

Coeficiente de determinación múltiple (ec. 10-26):

$$R^2=\frac{SS_R}{SS_T}=1-\frac{SS_E}{SS_T}$$

- Mide la reducción de variabilidad de $y$ lograda con los regresores.
- **Advertencia:** $R^2$ **siempre** aumenta al agregar un término, sea o no significativo; un
  $R^2$ grande no implica que el modelo sea adecuado ni que prediga bien.

$R^2$ ajustada (ec. 10-27):

$$R^2_{\text{ajustada}}=1-\frac{SS_E/(n-p)}{SS_T/(n-1)}=1-\left(\frac{n-1}{n-p}\right)(1-R^2)$$

- No necesariamente aumenta al agregar variables; con términos innecesarios suele **disminuir**.
- Regla: una diferencia considerable entre $R^2$ y $R^2_{\text{ajustada}}$ indica que
  probablemente se incluyeron términos no significativos.
- Viscosidad: $R^2_{\text{ajustada}}=1-(15/13)(1-0.92697)=0.915735$.

### 10-4.2 Pruebas de coeficientes individuales y de grupos de coeficientes

Motivación: agregar una variable siempre aumenta $SS_R$ y disminuye $SS_E$; hay que decidir si
el aumento justifica el término. Agregar una variable sin importancia puede **aumentar** $MS_E$
y empeorar el modelo.

#### Prueba $t$ para un coeficiente

$$H_0:\beta_j=0\qquad H_1:\beta_j\neq0$$

$$t_0=\frac{\hat\beta_j}{\sqrt{\hat\sigma^2C_{jj}}}=\frac{\hat\beta_j}{se(\hat\beta_j)}\qquad\text{(ecs. 10-28, 10-30)}$$

- $C_{jj}$ = elemento diagonal de $(\mathbf X'\mathbf X)^{-1}$ correspondiente a $\hat\beta_j$.
- **Error estándar** (ec. 10-29): $se(\hat\beta_j)=\sqrt{\hat\sigma^2C_{jj}}$.
- Rechazar $H_0$ si $|t_0|>t_{\alpha/2,\,n-k-1}$. Si no se rechaza, $x_j$ puede eliminarse.
- Es una prueba **parcial o marginal**: $\hat\beta_j$ depende de todos los demás regresores que
  están en el modelo.
- Viscosidad: $t=12.32$ (temperatura) y $t=3.52$, $P=0.004$ (alimentación); ambas contribuyen.

#### Método de la suma de cuadrados extra (prueba $F$ parcial)

Sirve para probar la contribución de un **subconjunto** de regresores dado que los demás están
en el modelo. Partición $\boldsymbol\beta=[\boldsymbol\beta_1',\boldsymbol\beta_2']'$ con
$\boldsymbol\beta_1$ de $r\times1$ y $\boldsymbol\beta_2$ de $(p-r)\times1$:

$$H_0:\boldsymbol\beta_1=\mathbf 0\qquad H_1:\boldsymbol\beta_1\neq\mathbf 0\qquad\text{(ec. 10-31)}$$

$$\mathbf y=\mathbf X_1\boldsymbol\beta_1+\mathbf X_2\boldsymbol\beta_2+\boldsymbol\varepsilon\qquad\text{(ec. 10-32)}$$

Pasos:

1. **Modelo completo:** $\hat{\boldsymbol\beta}=(\mathbf X'\mathbf X)^{-1}\mathbf X'\mathbf y$;
   $SS_R(\boldsymbol\beta)=\hat{\boldsymbol\beta}'\mathbf X'\mathbf y$ con $p$ gl (incluye la
   ordenada al origen); $MS_E=(\mathbf y'\mathbf y-\hat{\boldsymbol\beta}'\mathbf X'\mathbf y)/(n-p)$.
2. **Modelo reducido** ($H_0$ cierta): $\mathbf y=\mathbf X_2\boldsymbol\beta_2+\boldsymbol\varepsilon$
   (ec. 10-33); $\hat{\boldsymbol\beta}_2=(\mathbf X_2'\mathbf X_2)^{-1}\mathbf X_2'\mathbf y$;
   $SS_R(\boldsymbol\beta_2)=\hat{\boldsymbol\beta}_2'\mathbf X_2'\mathbf y$ con $p-r$ gl (ec. 10-34).
3. **Suma de cuadrados extra** (ec. 10-35), con $r$ gl:

$$SS_R(\boldsymbol\beta_1\mid\boldsymbol\beta_2)=SS_R(\boldsymbol\beta)-SS_R(\boldsymbol\beta_2)$$

4. Estadístico (ec. 10-36); $SS_R(\boldsymbol\beta_1\mid\boldsymbol\beta_2)$ es independiente
   de $MS_E$:

$$F_0=\frac{SS_R(\boldsymbol\beta_1\mid\boldsymbol\beta_2)/r}{MS_E}$$

   Rechazar $H_0$ si $F_0>F_{\alpha,r,n-p}$. El $MS_E$ del denominador es el del **modelo
   completo**.

Notas:

- Para una sola variable, $SS_R(\beta_j\mid\beta_0,\beta_1,\dots,\beta_{j-1},\beta_{j+1},\dots,\beta_k)$
  mide la contribución de $x_j$ **como si fuera la última en entrar**. Esta $F$ parcial equivale
  a la prueba $t$ ($t_0^2=F_0$), pero la $F$ parcial es más general porque admite conjuntos de
  variables.

#### Ejemplo 10-6 — Contribución de $x_2$ en el modelo de viscosidad

- $H_0:\beta_2=0$.
  $SS_R(\beta_2\mid\beta_1,\beta_0)=SS_R(\beta_1,\beta_2\mid\beta_0)-SS_R(\beta_1\mid\beta_0)$.
- $SS_R(\beta_1,\beta_2\mid\beta_0)=44{,}157.1$ (2 gl, la "SS del modelo" de la tabla 10-4).
- Modelo reducido: $\hat y=1652.3955+7.6397x_1$, con $SS_R(\beta_1\mid\beta_0)=40{,}840.8$ (1 gl;
  es el "Seq SS" de Temp en Minitab).
- $SS_R(\beta_2\mid\beta_0,\beta_1)=44{,}157.1-40{,}840.8=3316.3$ (1 gl; "Seq SS" de Feed Rate).
- $F_0=\dfrac{3316.3/1}{267.604}=12.3926$ → se rechaza $H_0$; $x_2$ contribuye
  significativamente. Comprobación: $t_0=3.5203$, $t_0^2=12.3925\approx F_0$.
- Errata: el libro imprime el valor crítico como $F_{0.05,1,13}=1.67$ (pág. 414); el valor
  tabulado correcto es 4.67. La conclusión no cambia.

## 10-5 Intervalos de confianza en regresiones múltiples

Mismo supuesto: errores $NID(0,\sigma^2)$.

### 10-5.1 Coeficientes individuales

$\hat{\boldsymbol\beta}$ es combinación lineal de las observaciones, así que
$\hat{\boldsymbol\beta}\sim N(\boldsymbol\beta,\sigma^2(\mathbf X'\mathbf X)^{-1})$ y (ec. 10-37)

$$\frac{\hat\beta_j-\beta_j}{\sqrt{\hat\sigma^2C_{jj}}}\sim t_{n-p},\qquad j=0,1,\dots,k$$

Intervalo de confianza de $100(1-\alpha)\%$ (ec. 10-38):

$$\hat\beta_j-t_{\alpha/2,n-p}\,se(\hat\beta_j)\le\beta_j\le\hat\beta_j+t_{\alpha/2,n-p}\,se(\hat\beta_j),
\qquad se(\hat\beta_j)=\sqrt{\hat\sigma^2C_{jj}}$$

**Ejemplo 10-7:** IC 95 % para $\beta_1$ en la viscosidad. $\hat\beta_1=7.62129$,
$\hat\sigma^2=267.604$, $C_{11}=1.429184\times10^{-3}$, $t_{0.025,13}=2.16$,
$se(\hat\beta_1)=0.6184$:

$$6.2855\le\beta_1\le8.9570$$

### 10-5.2 Respuesta media en un punto

Punto $\mathbf x_0=[1,x_{01},x_{02},\dots,x_{0k}]'$. Respuesta media
$\mu_{y|\mathbf x_0}=\mathbf x_0'\boldsymbol\beta$; estimador insesgado (ec. 10-39)
$\hat y(\mathbf x_0)=\mathbf x_0'\hat{\boldsymbol\beta}$ con varianza (ec. 10-40)

$$V[\hat y(\mathbf x_0)]=\sigma^2\mathbf x_0'(\mathbf X'\mathbf X)^{-1}\mathbf x_0$$

Intervalo de confianza de $100(1-\alpha)\%$ (ec. 10-41):

$$\hat y(\mathbf x_0)\pm t_{\alpha/2,n-p}\sqrt{\hat\sigma^2\,\mathbf x_0'(\mathbf X'\mathbf X)^{-1}\mathbf x_0}$$

## 10-6 Predicción de nuevas observaciones de la respuesta

Estimación puntual de una observación futura $y_0$ en $\mathbf x_0$:
$\hat y(\mathbf x_0)=\mathbf x_0'\hat{\boldsymbol\beta}$.

**Intervalo de predicción** de $100(1-\alpha)\%$ (ec. 10-42):

$$\hat y(\mathbf x_0)\pm t_{\alpha/2,n-p}\sqrt{\hat\sigma^2\left(1+\mathbf x_0'(\mathbf X'\mathbf X)^{-1}\mathbf x_0\right)}$$

- Diferencia con el IC de la media: el "$1+$" dentro de la raíz (variabilidad de la observación
  individual), por lo que siempre es más ancho.
- **Advertencia:** no extrapolar fuera de la región de los datos originales; un modelo que
  ajusta bien dentro de la región puede fallar fuera de ella. Aplica también al IC de la media.

## 10-7 Diagnósticos del modelo de regresión

Siempre hay que: 1) comprobar que el modelo ajustado aproxima bien al sistema real, y
2) verificar que no se violan los supuestos de mínimos cuadrados. Las gráficas de residuales de
los experimentos diseñados (probabilidad normal, residuales contra predichos y contra cada
regresor) se usan igual en regresión; además están los diagnósticos siguientes.

### 10-7.1 Residuales escalados y PRESS

#### Residual estandarizado (ec. 10-43)

$$d_i=\frac{e_i}{\hat\sigma},\qquad \hat\sigma=\sqrt{MS_E}$$

- Media cero y varianza aproximadamente 1.
- Regla: la mayoría debe caer en $-3\le d_i\le3$; fuera de ese intervalo, posible **punto
  atípico**. Un atípico puede ser un error de registro o una región donde el modelo aproxima mal
  la superficie verdadera; hay que examinarlo.

#### Matriz sombrero ("gorro") (ec. 10-44)

$$\hat{\mathbf y}=\mathbf X(\mathbf X'\mathbf X)^{-1}\mathbf X'\mathbf y=\mathbf H\mathbf y,\qquad
\mathbf H=\mathbf X(\mathbf X'\mathbf X)^{-1}\mathbf X'\ (n\times n)$$

- $\operatorname{Cov}(\mathbf e)=\sigma^2(\mathbf I-\mathbf H)$ (ec. 10-45): los residuales
  tienen varianzas distintas y están correlacionados.
- $V(e_i)=\sigma^2(1-h_{ii})$ (ec. 10-46), con $0\le h_{ii}\le1$ el elemento diagonal de
  $\mathbf H$.
- Consecuencias: usar $MS_E$ **sobreestima** $V(e_i)$; $h_{ii}$ mide la localización del punto
  en el espacio $x$; los residuales de puntos cercanos al centro tienen mayor varianza que los
  de puntos alejados. Las violaciones del modelo son más probables en puntos remotos y más
  difíciles de detectar con $e_i$ o $d_i$, porque allí los residuales tienden a ser pequeños.

#### Residual studentizado (ec. 10-47)

$$r_i=\frac{e_i}{\sqrt{\hat\sigma^2(1-h_{ii})}},\qquad \hat\sigma^2=MS_E$$

- Varianza constante $V(r_i)=1$ sin importar la localización de $\mathbf x_i$ (si la forma del
  modelo es correcta).
- En conjuntos grandes $d_i$ y $r_i$ casi coinciden; aun así se recomienda examinar los
  studentizados, porque un punto con residual grande **y** $h_{ii}$ grande es potencialmente muy
  influyente.

#### PRESS (Prediction Error Sum of Squares)

- Para cada $i$: ajustar el modelo con las $n-1$ observaciones restantes, predecir la
  observación apartada $\hat y_{(i)}$ y calcular el **residual PRESS**
  $e_{(i)}=y_i-\hat y_{(i)}$.

$$\text{PRESS}=\sum_{i=1}^{n}e_{(i)}^2=\sum_{i=1}^{n}[y_i-\hat y_{(i)}]^2\qquad\text{(ec. 10-48)}$$

- No hacen falta $n$ ajustes; con un solo ajuste (ecs. 10-49, 10-50):

$$e_{(i)}=\frac{e_i}{1-h_{ii}},\qquad \text{PRESS}=\sum_{i=1}^{n}\left(\frac{e_i}{1-h_{ii}}\right)^2$$

- Interpretación: $h_{ii}$ grande → residual PRESS grande → punto de **alta influencia**. Una
  diferencia grande entre $e_i$ y $e_{(i)}$ señala un punto donde el modelo ajusta bien, pero
  que sin él predeciría mal.
- $R^2$ de predicción (ec. 10-51):

$$R^2_{\text{Predicción}}=1-\frac{\text{PRESS}}{S_{yy}}$$

- Viscosidad: $\text{PRESS}=5207.7$, $R^2_{\text{Predicción}}=1-5207.7/47{,}635.9=0.8907$. Se
  espera explicar cerca del 89 % de la variabilidad en observaciones nuevas, frente al 93 % en
  los datos originales; capacidad predictiva satisfactoria.

#### R-student (residual studentizado externamente)

- $r_i$ usa $MS_E$ (escalación **interna**). La alternativa estima $\sigma^2$ sin la observación
  $i$ (ec. 10-52):

$$S_{(i)}^2=\frac{(n-p)MS_E-e_i^2/(1-h_{ii})}{n-p-1}$$

$$t_i=\frac{e_i}{\sqrt{S_{(i)}^2(1-h_{ii})}},\qquad i=1,\dots,n\qquad\text{(ec. 10-53)}$$

- Normalmente $t_i\approx r_i$; si la observación $i$ es influyente, $S_{(i)}^2$ difiere mucho
  de $MS_E$ y el R-student es **más sensible**.
- Bajo los supuestos usuales $t_i\sim t_{n-p-1}$, lo que da una prueba formal de puntos atípicos.
- Viscosidad: ningún R-student es inusualmente grande (máximo 1.80, obs. 11).

### 10-7.2 Diagnósticos de influencia

Un subconjunto pequeño de datos puede dominar el ajuste. Si los puntos influyentes son valores
"malos" se eliminan; si no lo son, igual conviene saber que controlan propiedades clave del
modelo.

#### Puntos de acción de palanca (leverage)

- $V(\hat{\mathbf y})=\sigma^2\mathbf H$ y $V(\mathbf e)=\sigma^2(\mathbf I-\mathbf H)$. El
  elemento $h_{ij}$ es la palanca que ejerce $y_j$ sobre $\hat y_i$.
- $\sum_{i=1}^{n}h_{ii}=\operatorname{rango}(\mathbf H)=\operatorname{rango}(\mathbf X)=p$, de
  modo que el promedio de las $h_{ii}$ es $p/n$.
- **Regla práctica:** $h_{ii}>2p/n$ → observación con acción de palanca alta.
- Viscosidad: $2p/n=2(3)/16=0.375$; el máximo $h_{ii}$ es 0.350 → sin puntos de palanca.

#### Distancia de Cook

Mide el cuadrado de la distancia entre $\hat{\boldsymbol\beta}$ (con los $n$ puntos) y
$\hat{\boldsymbol\beta}_{(i)}$ (sin el punto $i$) (ec. 10-54):

$$D_i=\frac{(\hat{\boldsymbol\beta}_{(i)}-\hat{\boldsymbol\beta})'\mathbf X'\mathbf X(\hat{\boldsymbol\beta}_{(i)}-\hat{\boldsymbol\beta})}{p\,MS_E},\qquad i=1,\dots,n$$

Fórmula de cálculo (ec. 10-55):

$$D_i=\frac{r_i^2}{p}\,\frac{V[\hat y(\mathbf x_i)]}{V(e_i)}=\frac{r_i^2}{p}\,\frac{h_{ii}}{1-h_{ii}}$$

- Dos componentes: $r_i^2$ (qué tan mal ajusta el modelo a $y_i$) y $h_{ii}/(1-h_{ii})$
  (distancia de $\mathbf x_i$ al centroide del resto de los datos). Cualquiera de los dos, o
  ambos, puede producir un $D_i$ grande.
- **Regla práctica:** $D_i>1$ → observación influyente.
- Viscosidad: máximo $D_i=0.354$ (obs. 11) → sin evidencia de observaciones influyentes.

### Resumen de diagnósticos y umbrales

| Diagnóstico | Fórmula | Criterio |
|---|---|---|
| Residual estandarizado | $d_i=e_i/\sqrt{MS_E}$ | $\lvert d_i\rvert>3$: atípico potencial |
| Residual studentizado | $r_i=e_i/\sqrt{MS_E(1-h_{ii})}$ | varianza 1; revisar los grandes |
| Residual PRESS | $e_{(i)}=e_i/(1-h_{ii})$ | grande frente a $e_i$: alta influencia |
| PRESS | $\sum[e_i/(1-h_{ii})]^2$ | cuanto menor, mejor predicción |
| $R^2_{\text{Predicción}}$ | $1-\text{PRESS}/S_{yy}$ | comparar con $R^2$ |
| R-student | $t_i=e_i/\sqrt{S_{(i)}^2(1-h_{ii})}$ | comparar con $t_{n-p-1}$ |
| Leverage | $h_{ii}$ (diagonal de $\mathbf H$) | $h_{ii}>2p/n$ |
| Distancia de Cook | $D_i=\dfrac{r_i^2}{p}\dfrac{h_{ii}}{1-h_{ii}}$ | $D_i>1$ |

## 10-8 Prueba de falta de ajuste

Cuándo se usa: hay **réplicas** en al menos algunos niveles de los regresores (p. ej. puntos
centrales en un $2^k$, secc. 6-6), lo que da una estimación del error puro independiente del
modelo. Permite probar si la forma del modelo (p. ej. lineal) es adecuada.

Partición: $SS_E=SS_{PE}+SS_{LOF}$.

Notación: $m$ niveles distintos $\mathbf x_i$ de los regresores; $n_i$ observaciones en el nivel
$i$; $y_{ij}$ la observación $j$ en $\mathbf x_i$; $n=\sum_{i=1}^{m}n_i$; $\bar y_i$ el promedio
en $\mathbf x_i$.

$$y_{ij}-\hat y_i=(y_{ij}-\bar y_i)+(\bar y_i-\hat y_i)\qquad\text{(ec. 10-56)}$$

$$\sum_{i=1}^{m}\sum_{j=1}^{n_i}(y_{ij}-\hat y_i)^2=\sum_{i=1}^{m}\sum_{j=1}^{n_i}(y_{ij}-\bar y_i)^2+\sum_{i=1}^{m}n_i(\bar y_i-\hat y_i)^2\qquad\text{(ec. 10-57)}$$

| Componente | Suma de cuadrados | Grados de libertad |
|---|---|---|
| Falta de ajuste | $SS_{LOF}=\sum_{i=1}^{m}n_i(\bar y_i-\hat y_i)^2$ (ec. 10-60) | $m-p$ |
| Error puro | $SS_{PE}=\sum_{i=1}^{m}\sum_{j=1}^{n_i}(y_{ij}-\bar y_i)^2$ (ec. 10-58) | $\sum(n_i-1)=n-m$ (ec. 10-59) |
| Residual | $SS_E$ | $n-p$ |

- $SS_{PE}$ es **independiente del modelo** (si la varianza es constante): solo usa la
  variabilidad de las $y$ dentro de cada nivel.
- $SS_{LOF}$ es una suma ponderada de las desviaciones entre el promedio de cada nivel y su valor
  ajustado; en la práctica se obtiene como $SS_{LOF}=SS_E-SS_{PE}$.

Estadístico (ec. 10-61):

$$F_0=\frac{SS_{LOF}/(m-p)}{SS_{PE}/(n-m)}=\frac{MS_{LOF}}{MS_{PE}}$$

Cuadrados medios esperados: $E(MS_{PE})=\sigma^2$ y (ec. 10-62)

$$E(MS_{LOF})=\sigma^2+\frac{\sum_{i=1}^{m}n_i\left[E(y_i)-\beta_0-\sum_{j=1}^{k}\beta_jx_{ij}\right]^2}{m-2}$$

(el libro imprime el denominador como $m-2$, que corresponde a la recta simple con $p=2$; en
general sería $m-p$ — dudoso, pág. 422).

- Si la función de regresión verdadera es lineal, el segundo término es cero,
  $E(MS_{LOF})=\sigma^2$ y $F_0\sim F_{m-p,\,n-m}$.
- **Decisión:** rechazar la adecuación del modelo si $F_0>F_{\alpha,m-p,n-m}$; en ese caso se
  abandona el modelo tentativo y se busca una ecuación más apropiada.
- Si no se rechaza, no hay evidencia sólida de falta de ajuste y $MS_{PE}$ y $MS_{LOF}$ suelen
  **combinarse** para estimar $\sigma^2$.
- Ilustración completa: ejemplo 6-6 (réplicas en los puntos centrales de un $2^2$).

## Reglas prácticas y advertencias del capítulo

1. En un $2^k$ con variables codificadas $\pm1$: $\hat\beta_j=\text{efecto}_j/2$; las
   estimaciones de efectos son de mínimos cuadrados.
2. Diseños ortogonales ($\mathbf X'\mathbf X$ diagonal) dan estimadores no correlacionados. Una
   corrida faltante o niveles inexactos rompen la ortogonalidad, pero el análisis por regresión
   sigue siendo válido y normalmente cambia poco las conclusiones.
3. Los alias se manifiestan como columnas idénticas (dependencia lineal) en $\mathbf X$. Para
   separarlos basta agregar corridas que rompan la dependencia; agregar un **número par** de
   corridas mantiene los bloques ortogonales.
4. $R^2$ nunca decrece al agregar términos; vigilar $R^2_{\text{ajustada}}$ y
   $R^2_{\text{Predicción}}$.
5. Las pruebas $t$ son marginales: dependen de qué otros regresores están en el modelo.
6. En la $F$ parcial el denominador es el $MS_E$ del modelo completo.
7. El intervalo de predicción es más ancho que el de la respuesta media; no extrapolar.
8. Umbrales: $|d_i|>3$, $h_{ii}>2p/n$, $D_i>1$.
9. Falta de ajuste: requiere réplicas genuinas; gl $m-p$ y $n-m$.

## 10-9 Problemas (solo referencia)

Págs. 422–426, problemas 10-1 a 10-18. Temas: regresión simple y múltiple con prueba de
significación e IC (10-1, 10-2, 10-6, 10-7), residuales (10-3, 10-4, 10-8), falta de ajuste
(10-5), efecto de la codificación sobre la diagonalidad de $\mathbf X'\mathbf X$ (10-9),
observaciones faltantes en el $2^4$ del ejemplo 6-2 (10-10, 10-11), modelo de segundo orden y
suma de cuadrados extra (10-12, 10-13), ANOVA de un factor como modelo lineal general (10-14),
ubicación de puntos para minimizar $V(\hat\beta_1)$ (10-15), mínimos cuadrados ponderados
(10-16) y aumento de diseños para separar alias: $2^{4-1}_{IV}$ del ejemplo 10-5 (10-17) y un
$2^{7-4}_{III}$ con $A+BD$, $B+AD$, $D+AB$ (10-18).
