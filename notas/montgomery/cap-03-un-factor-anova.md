# Capítulo 3 — Experimentos con un solo factor: el análisis de varianza

> Montgomery, págs. 60–125 (texto: 60–119; problemas: 119–125)

Notación usada en todo el capítulo: $a$ = número de niveles (tratamientos) del factor, $n$ = réplicas
por tratamiento (o $n_i$ si no hay balanceo), $N = an$ (o $N=\sum n_i$) = total de observaciones.
El subíndice "punto" indica suma sobre el índice que reemplaza: $y_{i.}=\sum_j y_{ij}$,
$\bar y_{i.}=y_{i.}/n$, $y_{..}=\sum_i\sum_j y_{ij}$, $\bar y_{..}=y_{..}/N$ (ec. 3-3).

Ejemplo conductor de todo el capítulo (**ejemplo 3-1, resistencia a la tensión de una fibra
sintética**): factor = peso porcentual de algodón, $a=5$ niveles (15, 20, 25, 30, 35 %), $n=5$,
$N=25$, respuesta en lb/pulg². Totales $y_{i.}$ = 49, 77, 88, 108, 54; promedios
$\bar y_{i.}$ = 9.8, 15.4, 17.6, 21.6, 10.8; $y_{..}=376$, $\bar y_{..}=15.04$ (tabla 3-1).

---

## 3-1 Un ejemplo

- Experimento de un solo factor con $a$ niveles y $n$ réplicas, **completamente aleatorizado**.
- **Aleatorización del orden de corridas**: se numeran las $N$ corridas (1–5 para el nivel 1, 6–10
  para el nivel 2, …) y se sortean números entre 1 y $N$ sin repetición; el orden del sorteo es la
  secuencia de prueba. Protege contra variables perturbadoras desconocidas (p. ej. calentamiento
  de la máquina de prueba: si se corriera nivel por nivel, la deriva se confundiría con el factor).
- Antes de cualquier prueba formal: examinar los datos **gráficamente** (diagramas de caja por
  nivel, fig. 3-1; diagrama de dispersión de respuesta vs. nivel con los promedios, fig. 3-2).
- Por qué no hacer todas las pruebas $t$ por pares: con 5 medias hay 10 pares; si cada prueba tiene
  $1-\alpha = 0.95$, la probabilidad de no rechazar correctamente en las 10 (independientes) es
  $0.95^{10}=0.60$ → inflación fuerte del error tipo I. El procedimiento correcto para probar la
  igualdad de varias medias es el **análisis de varianza**.

## 3-2 El análisis de varianza

### Modelos para los datos

**Modelo de las medias** (ec. 3-1):

$$y_{ij}=\mu_i+\varepsilon_{ij},\qquad i=1,\dots,a;\; j=1,\dots,n$$

**Modelo de los efectos** (ec. 3-2), con $\mu_i=\mu+\tau_i$:

$$y_{ij}=\mu+\tau_i+\varepsilon_{ij}$$

- $\mu$: media global (común a todos los tratamientos); $\tau_i$: efecto del tratamiento $i$-ésimo;
  $\varepsilon_{ij}$: error aleatorio (medición, factores no controlados, diferencias entre unidades
  experimentales, ruido de fondo).
- Ambos son **modelos estadísticos lineales**. Se le llama modelo del análisis de varianza
  **simple o de un solo factor (una dirección)**; el diseño es **completamente aleatorizado**.
- Supuestos para las pruebas: $\varepsilon_{ij}\sim \text{NID}(0,\sigma^2)$, con $\sigma^2$ constante
  en todos los niveles ⇒ $y_{ij}\sim N(\mu+\tau_i,\sigma^2)$, mutuamente independientes.

### ¿Factor fijo o aleatorio?

| | Efectos fijos | Efectos aleatorios (componentes de la varianza) |
|---|---|---|
| Niveles | Elegidos expresamente por el experimentador | Muestra aleatoria de una población de niveles |
| Inferencia | Solo sobre los niveles estudiados | Sobre toda la población de niveles |
| Qué se prueba/estima | Medias de tratamientos; parámetros $\mu,\tau_i,\sigma^2$ | Variabilidad de las $\tau_i$ (son variables aleatorias) |

El modelo de efectos aleatorios se pospone al capítulo 12.

## 3-3 Análisis del modelo con efectos fijos

Hipótesis (equivalentes):

$$H_0:\mu_1=\mu_2=\dots=\mu_a \quad\text{vs.}\quad H_1:\mu_i\neq\mu_j \text{ para al menos un par } (i,j)$$

$$H_0:\tau_1=\tau_2=\dots=\tau_a=0 \quad\text{vs.}\quad H_1:\tau_i\neq 0 \text{ para al menos una } i$$

Con $\mu=\frac{1}{a}\sum_i\mu_i$ se tiene la restricción $\sum_{i=1}^a\tau_i=0$ (los efectos son
desviaciones respecto de la media global).

### 3-3.1 Descomposición de la suma de cuadrados total

Identidad fundamental del ANOVA (ec. 3-6); el producto cruzado se anula porque
$\sum_j (y_{ij}-\bar y_{i.})=0$:

$$\sum_{i=1}^{a}\sum_{j=1}^{n}(y_{ij}-\bar y_{..})^2 = n\sum_{i=1}^{a}(\bar y_{i.}-\bar y_{..})^2+\sum_{i=1}^{a}\sum_{j=1}^{n}(y_{ij}-\bar y_{i.})^2$$

$$SS_T = SS_{\text{Tratamientos}} + SS_E$$

- Grados de libertad: $N-1 = (a-1) + (N-a)$, con $N-a=a(n-1)$.
- $SS_E/(N-a)$ es la **estimación combinada (pooled)** de la varianza dentro de tratamientos:
  $\dfrac{(n-1)S_1^2+\dots+(n-1)S_a^2}{(n-1)+\dots+(n-1)}=\dfrac{SS_E}{N-a}$.
- $SS_{\text{Trat}}/(a-1)$ estima $\sigma^2$ **solo si** las medias son iguales
  (porque $\sum(\bar y_{i.}-\bar y_{..})^2/(a-1)$ estima $\sigma^2/n$).

Cuadrados medios y sus valores esperados:

$$MS_{\text{Trat}}=\frac{SS_{\text{Trat}}}{a-1},\qquad MS_E=\frac{SS_E}{N-a}$$

$$E(MS_E)=\sigma^2,\qquad E(MS_{\text{Trat}})=\sigma^2+\frac{n\sum_{i=1}^a\tau_i^2}{a-1}$$

### 3-3.2 Análisis estadístico

- $SS_T/\sigma^2\sim\chi^2_{N-1}$; $SS_E/\sigma^2\sim\chi^2_{N-a}$; bajo $H_0$,
  $SS_{\text{Trat}}/\sigma^2\sim\chi^2_{a-1}$.
- **Teorema de Cochran (teorema 3-1)**: si $Z_i\sim\text{NID}(0,1)$, $i=1,\dots,\nu$, y
  $\sum Z_i^2=Q_1+\dots+Q_s$ con $s\le\nu$ y $Q_i$ con $\nu_i$ g.l., entonces las $Q_i$ son
  ji-cuadradas independientes con $\nu_i$ g.l. **si y solo si** $\nu=\nu_1+\dots+\nu_s$.
  Como $(a-1)+(N-a)=N-1$, $SS_{\text{Trat}}/\sigma^2$ y $SS_E/\sigma^2$ son independientes.
- Estadístico de prueba (ec. 3-7):

$$F_0=\frac{SS_{\text{Trat}}/(a-1)}{SS_E/(N-a)}=\frac{MS_{\text{Trat}}}{MS_E}\;\sim\;F_{a-1,\,N-a}\ \text{bajo } H_0$$

- Región crítica de **una cola superior**: rechazar $H_0$ si $F_0>F_{\alpha,\,a-1,\,N-a}$ (o por valor $P$).

Fórmulas de cálculo (ecs. 3-8 a 3-10):

$$SS_T=\sum_{i=1}^a\sum_{j=1}^n y_{ij}^2-\frac{y_{..}^2}{N},\qquad SS_{\text{Trat}}=\frac1n\sum_{i=1}^a y_{i.}^2-\frac{y_{..}^2}{N},\qquad SS_E=SS_T-SS_{\text{Trat}}$$

**Tabla ANOVA, un factor, efectos fijos (tabla 3-3)**

| Fuente de variación | Suma de cuadrados | G.l. | Cuadrado medio | $F_0$ |
|---|---|---|---|---|
| Entre tratamientos | $SS_{\text{Trat}}=n\sum_i(\bar y_{i.}-\bar y_{..})^2$ | $a-1$ | $MS_{\text{Trat}}$ | $MS_{\text{Trat}}/MS_E$ |
| Error (dentro de tratamientos) | $SS_E=SS_T-SS_{\text{Trat}}$ | $N-a$ | $MS_E$ | |
| Total | $SS_T=\sum_i\sum_j(y_{ij}-\bar y_{..})^2$ | $N-1$ | | |

**Ejemplo 3-1 (resistencia a la tensión).** $SS_T=636.96$, $SS_{\text{Trat}}=475.76$,
$SS_E=161.20$ (tabla 3-4):

| Fuente | SS | G.l. | MS | $F_0$ | Valor $P$ |
|---|---|---|---|---|---|
| Peso porcentual del algodón | 475.76 | 4 | 118.94 | 14.76 | <0.01 |
| Error | 161.20 | 20 | 8.06 | | |
| Total | 636.96 | 24 | | | |

$F_{0.05,4,20}=2.87$, $F_{0.01,4,20}=4.43$; $P$ exacto $=9.11\times10^{-6}$. Se rechaza $H_0$: el
contenido de algodón afecta la resistencia media.

**Cálculos manuales.** Las fórmulas de cálculo usan totales (no promedios) por conveniencia y porque
están menos sujetas a redondeo. En la práctica se usa software.

**Ejemplo 3-2 (codificación de observaciones).** Restar una constante (15) a todas las observaciones
no cambia ninguna suma de cuadrados (636.96, 475.76, 161.20). Multiplicar por una constante (2)
multiplica las SS por su cuadrado ($SS_T=2547.84$, $SS_{\text{Trat}}=1903.04$, $SS_E=644.80$) pero el
cociente $F$ no cambia (14.76).

**Pruebas de aleatorización y ANOVA.** La prueba $F$ puede justificarse sin normalidad como
aproximación de una **prueba de aleatorización**: bajo $H_0$ todas las asignaciones de las
observaciones a tratamientos son igualmente probables (p. ej. 2 tratamientos × 5 obs.:
$10!/(5!5!)=252$ arreglos); se calcula $F$ para cada arreglo y se ubica el valor observado en esa
**distribución de aleatorización** (si solo 5 valores lo exceden, $\alpha=5/252=0.0198$). La $F$
de teoría normal aproxima bien esa distribución (ref. Box, Hunter y Hunter).

### 3-3.3 Estimación de los parámetros del modelo

Estimadores (ec. 3-11): $\hat\mu=\bar y_{..}$, $\hat\tau_i=\bar y_{i.}-\bar y_{..}$,
$\hat\mu_i=\hat\mu+\hat\tau_i=\bar y_{i.}$. Con errores normales, $\bar y_{i.}\sim\text{NID}(\mu_i,\sigma^2/n)$.

IC de $100(1-\alpha)\%$ para la media del tratamiento $i$ (ec. 3-12):

$$\bar y_{i.}-t_{\alpha/2,N-a}\sqrt{\frac{MS_E}{n}}\le\mu_i\le\bar y_{i.}+t_{\alpha/2,N-a}\sqrt{\frac{MS_E}{n}}$$

IC para la diferencia de dos medias (ec. 3-13):

$$\bar y_{i.}-\bar y_{j.}\pm t_{\alpha/2,N-a}\sqrt{\frac{2MS_E}{n}}$$

**Ejemplo 3-3.** $\hat\mu=15.04$; $\hat\tau_1=-5.24$, $\hat\tau_2=+0.36$, $\hat\tau_3=+2.56$,
$\hat\tau_4=+6.56$, $\hat\tau_5=-4.24$ (el libro imprime $\hat\tau_3=-2.56$; es errata de signo:
$17.60-15.04=+2.56$). IC 95 % para $\mu_4$: $21.60\pm2.086\sqrt{8.06/5}=21.60\pm2.65$, es decir
$18.95\le\mu_4\le24.25$.

**Intervalos de confianza simultáneos.** Las ecs. 3-12 y 3-13 son intervalos **uno a la vez**. Para
$r$ intervalos de $100(1-\alpha)\%$, la confianza simultánea es al menos $1-r\alpha$
($r\alpha$ = índice de error en el modo del experimento): con $r=5$, $\alpha=0.05$ → al menos 0.75;
con $r=10$ → al menos 0.50. **Método de Bonferroni**: sustituir $\alpha/2$ por $\alpha/(2r)$ en las
ecs. 3-12 y 3-13 para lograr confianza global de al menos $100(1-\alpha)\%$; funciona bien si $r$
no es muy grande.

### 3-3.4 Datos no balanceados

Con $n_i$ observaciones en el tratamiento $i$ y $N=\sum_i n_i$ (ecs. 3-14 y 3-15):

$$SS_T=\sum_{i=1}^a\sum_{j=1}^{n_i}y_{ij}^2-\frac{y_{..}^2}{N},\qquad SS_{\text{Trat}}=\sum_{i=1}^a\frac{y_{i.}^2}{n_i}-\frac{y_{..}^2}{N}$$

No se requiere ningún otro cambio en el ANOVA. Ventajas del diseño **balanceado**:
1. La prueba es relativamente insensible a desviaciones pequeñas de la igualdad de varianzas cuando
   los $n_i$ son iguales (no así con $n_i$ distintos).
2. La potencia de la prueba se maximiza con tamaños de muestra iguales.

## 3-4 Verificación de la adecuación del modelo

Supuestos: el modelo $y_{ij}=\mu+\tau_i+\varepsilon_{ij}$ describe los datos y
$\varepsilon_{ij}\sim\text{NID}(0,\sigma^2)$ con $\sigma^2$ constante. Si se cumplen, el ANOVA es una
prueba exacta. No confiar en el ANOVA sin verificar los supuestos mediante los **residuales**:

$$e_{ij}=y_{ij}-\hat y_{ij},\qquad \hat y_{ij}=\hat\mu+\hat\tau_i=\bar y_{i.}\quad\text{(ecs. 3-16, 3-17)}$$

Si el modelo es adecuado, los residuales deben estar **sin estructura**. El examen de residuales
debe ser parte automática de todo ANOVA.

### 3-4.1 El supuesto de normalidad

- Histograma de residuales (poco fiable con muestras pequeñas) o, mejor, **gráfica de probabilidad
  normal de los residuales**: debe parecer una recta; al juzgarla, dar más peso a los valores
  centrales que a los extremos.
- Ejemplo 3-1 (tabla 3-6, fig. 3-4): leve indicio de sesgo (cola derecha más larga, cola izquierda
  más "delgada"), sin desviación marcada de la normalidad.
- El ANOVA de efectos fijos es **robusto** a la no normalidad moderada (la $F$ se afecta poco). Colas
  mucho más gruesas o delgadas que la normal preocupan más que el sesgo. La no normalidad hace que el
  nivel de significación y la potencia reales difieran ligeramente de los nominales (potencia
  generalmente menor). El modelo de efectos aleatorios se afecta más severamente.
- **Puntos atípicos**: residual mucho mayor que los demás. Pueden distorsionar seriamente el ANOVA.
  Investigar primero errores de cálculo, codificación o copia; no descartar sin razones no
  estadísticas de peso; puede ser el dato más informativo. En el peor caso, hacer dos análisis (con
  y sin el punto). Verificación aproximada con **residuales estandarizados** (ec. 3-18):

$$d_{ij}=\frac{e_{ij}}{\sqrt{MS_E}}$$

  Deben ser aproximadamente $N(0,1)$: ~68 % dentro de ±1, ~95 % dentro de ±2, prácticamente todos
  dentro de ±3. Un residual a más de 3 o 4 desviaciones estándar de cero es atípico potencial.
  Ejemplo 3-1: el mayor es $d_{13}=5.2/\sqrt{8.06}=5.2/2.84=1.83$ → sin problema.

### 3-4.2 Gráfica de los residuales en secuencia en el tiempo

- Graficar residuales en el orden temporal de recolección detecta **correlación** (rachas de
  residuales positivos/negativos ⇒ correlación positiva ⇒ violación de **independencia**). Es un
  problema serio y difícil de corregir; se previene con una aleatorización adecuada.
- También detecta cambios de la varianza con el tiempo (dispersión mayor en un extremo), p. ej. por
  aprendizaje o fatiga del experimentador o deriva del proceso.
- Ejemplo 3-1 (fig. 3-5): sin indicios de violación de independencia ni de varianza constante.

### 3-4.3 Gráfica de los residuales contra los valores ajustados

- Graficar $e_{ij}$ contra $\hat y_{ij}=\bar y_{i.}$: no debe mostrar patrón. Ejemplo 3-1 (fig.
  3-6): sin estructura.
- Defecto típico: **varianza no constante** en forma de embudo/megáfono abierto hacia afuera (el
  error crece con la magnitud de la respuesta; común cuando el error es un porcentaje constante de
  la lectura, y en distribuciones sesgadas donde la varianza es función de la media).
- Consecuencias de varianzas desiguales:
  - Balanceado, efectos fijos: la $F$ se afecta solo ligeramente.
  - No balanceado o una varianza mucho mayor que las demás: problema más grave. Si los niveles con
    mayor varianza tienen los $n_i$ **más pequeños**, el error tipo I real es **mayor** que el nominal
    (IC con confianza real menor); si tienen los $n_i$ **mayores**, el nivel de significación real es
    **menor** (confianza mayor). Razón adicional para usar **tamaños de muestra iguales**.
  - Efectos aleatorios: las varianzas desiguales alteran significativamente las inferencias sobre
    componentes de varianza incluso con diseños balanceados.
- Remedio usual: **transformación estabilizadora de la varianza** y ANOVA sobre los datos
  transformados (las conclusiones aplican a las poblaciones *transformadas*).
  - Poisson: raíz cuadrada, $y^*=\sqrt{y}$ o $y^*=\sqrt{1+y}$.
  - Lognormal: $y^*=\log y$.
  - Binomial (fracciones): $y^*=\arcsin\sqrt{y}$.
  - Sin transformación obvia: búsqueda empírica (ver abajo). En factoriales, otro criterio es
    minimizar el cuadrado medio de las interacciones (cap. 5); selección analítica en cap. 14
    (Box–Cox). La transformación suele además acercar el error a la normalidad.

#### Pruebas estadísticas para la igualdad de la varianza

$$H_0:\sigma_1^2=\sigma_2^2=\dots=\sigma_a^2\quad\text{vs.}\quad H_1:\text{no se cumple para al menos una }\sigma_i^2$$

**Prueba de Bartlett** (ec. 3-19); requiere muestras de poblaciones normales independientes:

$$\chi_0^2=2.3026\,\frac{q}{c}$$

$$q=(N-a)\log_{10}S_p^2-\sum_{i=1}^a(n_i-1)\log_{10}S_i^2$$

$$c=1+\frac{1}{3(a-1)}\left(\sum_{i=1}^a(n_i-1)^{-1}-(N-a)^{-1}\right),\qquad S_p^2=\frac{\sum_{i=1}^a(n_i-1)S_i^2}{N-a}$$

Rechazar $H_0$ si $\chi_0^2>\chi^2_{\alpha,\,a-1}$. **Advertencia**: Bartlett es muy sensible a la no
normalidad; no usarla si la normalidad está en duda.

**Ejemplo 3-4.** Ejemplo 3-1: $S_1^2=11.2$, $S_2^2=9.8$, $S_3^2=4.3$, $S_4^2=6.8$, $S_5^2=8.2$;
$S_p^2=8.06$; $q=0.45$; $c=1.10$; $\chi_0^2=2.3026(0.45)/(1.10)=0.93<\chi^2_{0.05,4}=9.49$ → no se
rechaza; las cinco varianzas son iguales.

**Prueba de Levene modificada** (robusta a la no normalidad): calcular las desviaciones absolutas
respecto de la **mediana** $\tilde y_i$ de cada tratamiento,

$$d_{ij}=|y_{ij}-\tilde y_i|,\qquad i=1,\dots,a;\; j=1,\dots,n_i$$

y aplicar el **estadístico $F$ del ANOVA usual** a las $d_{ij}$ (se prueba si la desviación media es
igual en todos los tratamientos).

**Ejemplo 3-5 (descarga pico).** Cuatro métodos de estimación de la frecuencia de inundaciones,
$n=6$ cada uno (tabla 3-7). $\bar y_{i.}$ = 0.71, 2.63, 7.93, 14.72; medianas $\tilde y_i$ = 0.520,
2.610, 7.805, 15.59; $S_i$ = 0.66, 1.09, 1.66, 2.77. ANOVA de los datos originales (tabla 3-8):
$SS_{\text{Métodos}}=708.3471$ (3 g.l., MS 236.1157), $SS_E=62.0811$ (20 g.l., MS 3.1041),
$SS_T=770.4282$ (23 g.l.), $F_0=76.07$, $P<0.001$. Residuales vs. ajustados en embudo (fig. 3-7).
Levene modificada: $F_0=4.55$, $P=0.0137$ → se rechaza la igualdad de varianzas; candidato a
transformación.

#### Selección empírica de una transformación

Si $\sigma_y\propto\mu^{\alpha}$ y se transforma $y^*=y^{\lambda}$ (ec. 3-20), entonces
$\sigma_{y^*}\propto\mu^{\lambda+\alpha-1}$ (ec. 3-21); tomando $\lambda=1-\alpha$ la varianza de
$y^*$ es constante.

**Tabla 3-9. Transformaciones para estabilizar la varianza** (en orden de "fuerza" creciente)

| Relación entre $\sigma_y$ y $\mu$ | $\alpha$ | $\lambda=1-\alpha$ | Transformación | Comentario |
|---|---|---|---|---|
| $\sigma_y\propto$ constante | 0 | 1 | Sin transformación | |
| $\sigma_y\propto\mu^{1/2}$ | 1/2 | 1/2 | Raíz cuadrada | Datos (conteos) de Poisson |
| $\sigma_y\propto\mu$ | 1 | 0 | Log | |
| $\sigma_y\propto\mu^{3/2}$ | 3/2 | −1/2 | Raíz cuadrada recíproca | |
| $\sigma_y\propto\mu^{2}$ | 2 | −1 | Recíproco | |

- Estimación empírica de $\alpha$ con réplicas: como $\sigma_{y_i}=\theta\mu_i^{\alpha}$,
  $\log\sigma_{y_i}=\log\theta+\alpha\log\mu_i$ (ec. 3-22). Graficar $\log S_i$ contra
  $\log\bar y_{i.}$; la **pendiente** de la recta estima $\alpha$.
- Regla práctica: las transformaciones tienen poco efecto a menos que
  $y_{\text{máx}}/y_{\text{mín}}$ sea mayor que 2 o 3.
- Continuación del ejemplo 3-5 (fig. 3-8): pendiente ≈ 1/2 ⇒ raíz cuadrada. ANOVA de
  $y^*=\sqrt{y}$ (tabla 3-10): $SS_{\text{Métodos}}=32.6842$ (3 g.l., MS 10.8947), $SS_E=2.6884$
  (**19** g.l., MS 0.1415), $SS_T=35.3726$ (22 g.l.), $F_0=76.99$, $P<0.001$. Se **resta 1 g.l. al
  error** por haber usado los datos para estimar $\alpha$. La gráfica de residuales mejora
  (fig. 3-9).
- En la práctica muchos prueban varias transformaciones y eligen la que da la mejor gráfica de
  residuales vs. predichos.

### 3-4.4 Gráficas de los residuales contra otras variables

Graficar los residuales contra cualquier otra variable registrada que pudiera afectar la respuesta
(p. ej. espesor de la fibra, máquina de prueba). Un patrón indica que esa variable afecta la
respuesta: controlarla mejor en experimentos futuros o incluirla en el análisis.

## 3-5 Interpretación práctica de los resultados

### 3-5.1 Un modelo de regresión

- Factor **cuantitativo** (niveles sobre escala numérica: temperatura, presión, tiempo) vs.
  **cualitativo** (operadores, lotes, turnos). En el diseño y el ANOVA iniciales se tratan igual.
  Con factores cuantitativos interesa además una ecuación de interpolación (**modelo empírico**)
  ajustada por **mínimos cuadrados** (análisis de regresión, cap. 10).
- Ejemplo 3-1, $x$ = % de algodón (fig. 3-10):
  - Cuadrático: $\hat y=-39.9886+4.596x-0.0886x^2$ (subestima en 30 % y sobreestima en 25 %).
  - Cúbico: $\hat y=62.6114-9.0114x+0.4814x^2-0.0076x^3$ (mejor ajuste en 25 y 30 %).
- Regla: usar el polinomio de **menor orden** que describa adecuadamente el sistema; cuidado con el
  sobreajuste. El modelo sirve para predecir dentro de la región de experimentación y para
  optimización del proceso.

### 3-5.2 Comparaciones entre las medias de los tratamientos

Rechazar $H_0$ en el ANOVA dice que hay diferencias pero no *cuáles*. Los **métodos de comparaciones
múltiples** comparan medias individuales o grupos de medias, usando los totales $\{y_{i.}\}$ o los
promedios $\{\bar y_{i.}\}$.

### 3-5.3 Comparaciones gráficas de medias

Si todas las medias fueran iguales, los $\bar y_{i.}$ se comportarían como una muestra de una
distribución con desviación estándar $\sigma/\sqrt n$. Se dibuja una distribución $t$ **escalada**
con factor $\sqrt{MS_E/n}$ y se "desliza" sobre el eje donde están graficados los promedios: los
promedios que no pueden cubrirse simultáneamente como muestra típica de esa distribución
corresponden a medias diferentes. Ejemplo 3-1: factor de escala $\sqrt{8.06/5}=1.27$ (fig. 3-11);
30 % da resistencia mucho mayor que 20 y 25 % (similares entre sí), y 15 y 35 % (similares) dan las
más bajas. Es un procedimiento aproximado pero eficaz.

### 3-5.4 Contrastes

Un **contraste** es una combinación lineal de medias con coeficientes que suman cero:

$$\Gamma=\sum_{i=1}^a c_i\mu_i,\qquad\sum_{i=1}^a c_i=0;\qquad H_0:\sum_i c_i\mu_i=0\ \text{vs.}\ H_1:\sum_i c_i\mu_i\ne0\quad\text{(ec. 3-25)}$$

Ejemplos: $H_0:\mu_4=\mu_5$ → $c=(0,0,0,+1,-1)$; $H_0:\mu_1+\mu_2=\mu_4+\mu_5$ → $c=(+1,+1,0,-1,-1)$.

**Prueba $t$** (con totales, diseño balanceado). $C=\sum_i c_i y_{i.}$, $V(C)=n\sigma^2\sum_i c_i^2$
(ec. 3-26):

$$t_0=\frac{\sum_{i=1}^a c_i y_{i.}}{\sqrt{n\,MS_E\sum_{i=1}^a c_i^2}}\quad\text{(ec. 3-27)};\qquad\text{rechazar si } |t_0|>t_{\alpha/2,\,N-a}$$

**Prueba $F$** equivalente ($F_0=t_0^2$; ecs. 3-28 y 3-29):

$$F_0=\frac{MS_C}{MS_E}=\frac{SS_C/1}{MS_E},\qquad SS_C=\frac{\left(\sum_{i=1}^a c_i y_{i.}\right)^2}{n\sum_{i=1}^a c_i^2};\qquad\text{rechazar si }F_0>F_{\alpha,1,N-a}$$

**Intervalo de confianza para un contraste** (con promedios: $C=\sum c_i\bar y_{i.}$,
$V(C)=\frac{\sigma^2}{n}\sum c_i^2$; ec. 3-30):

$$\sum_{i=1}^a c_i\bar y_{i.}\pm t_{\alpha/2,N-a}\sqrt{\frac{MS_E}{n}\sum_{i=1}^a c_i^2}$$

Si el intervalo incluye el cero, no se rechaza $H_0$.

**Contraste estandarizado** (para poner varios contrastes en la misma escala, varianza $\sigma^2$):
$\sum_i c_i^* y_{i.}$ con $c_i^*=c_i\big/\sqrt{n\sum_i c_i^2}$.

**Tamaños de muestra desiguales**: la definición de contraste exige $\sum_i n_i c_i=0$, y

$$t_0=\frac{\sum_i c_i y_{i.}}{\sqrt{MS_E\sum_i n_i c_i^2}},\qquad SS_C=\frac{\left(\sum_i c_i y_{i.}\right)^2}{\sum_i n_i c_i^2}$$

### 3-5.5 Contrastes ortogonales

- Dos contrastes $\{c_i\}$ y $\{d_i\}$ son **ortogonales** si $\sum_i c_i d_i=0$ (balanceado) o
  $\sum_i n_i c_i d_i=0$ (no balanceado).
- Para $a$ tratamientos, un conjunto de $a-1$ contrastes ortogonales **particiona**
  $SS_{\text{Trat}}$ en $a-1$ componentes independientes de 1 g.l. cada uno; las pruebas sobre ellos
  son independientes.
- Los coeficientes deben elegirse según la naturaleza del experimento. Ejemplo con $a=3$ (control +
  dos niveles): $(-2,1,1)$ compara el promedio del factor con el control; $(0,-1,1)$ compara los dos
  niveles.
- Son para **comparaciones preplaneadas**: se especifican *antes* de ver los datos. Elegir
  comparaciones después de mirar los datos (**curioseo o sondeo de datos**, *data snooping*) infla
  el error tipo I; para ese caso sirve Scheffé.

**Ejemplo 3-6.** Contrastes ortogonales preplaneados sobre el ejemplo 3-1 (tabla 3-11):

| Hipótesis | Contraste (totales) | Valor | $SS_C$ | $F_0$ | Valor $P$ |
|---|---|---|---|---|---|
| $\mu_4=\mu_5$ | $C_1=-y_{4.}+y_{5.}$ | −54 | $(-54)^2/[5(2)]=291.60$ | 36.18 | <0.001 |
| $\mu_1+\mu_3=\mu_4+\mu_5$ | $C_2=y_{1.}+y_{3.}-y_{4.}-y_{5.}$ | −25 | $(-25)^2/[5(4)]=31.25$ | 3.88 | 0.06 |
| $\mu_1=\mu_3$ | $C_3=y_{1.}-y_{3.}$ | −39 | $(-39)^2/[5(2)]=152.10$ | 18.87 | <0.001 |
| $4\mu_2=\mu_1+\mu_3+\mu_4+\mu_5$ | $C_4=-y_{1.}+4y_{2.}-y_{3.}-y_{4.}-y_{5.}$ | 9 | $(9)^2/[5(20)]=0.81$ | 0.10 | 0.76 |

$291.60+31.25+152.10+0.81=475.76=SS_{\text{Trat}}$ (partición completa; cada uno con 1 g.l.,
$MS_E=8.06$ con 20 g.l.). Conclusión: difieren los niveles 4 y 5, y 1 y 3; el promedio de 1 y 3 no
difiere del de 4 y 5 al 5 %; el nivel 2 no difiere del promedio de los otros cuatro.

### 3-5.6 Método de Scheffé para comparar todos los contrastes

Cuándo: no se conocen de antemano los contrastes de interés, o interesan más de $a-1$
comparaciones (experimentos exploratorios; permite el sondeo de datos). El error tipo I es **a lo
sumo $\alpha$** para *cualquiera* de los contrastes posibles.

Para $m$ contrastes $\Gamma_u=c_{1u}\mu_1+\dots+c_{au}\mu_a$, $u=1,\dots,m$ (ec. 3-31):

$$C_u=\sum_{i=1}^a c_{iu}\bar y_{i.}\quad\text{(3-32)},\qquad S_{C_u}=\sqrt{MS_E\sum_{i=1}^a\frac{c_{iu}^2}{n_i}}\quad\text{(3-33)}$$

$$S_{\alpha,u}=S_{C_u}\sqrt{(a-1)F_{\alpha,\,a-1,\,N-a}}\quad\text{(3-34)}$$

Rechazar $H_0:\Gamma_u=0$ si $|C_u|>S_{\alpha,u}$. Intervalos simultáneos:
$C_u-S_{\alpha,u}\le\Gamma_u\le C_u+S_{\alpha,u}$ (confianza conjunta de al menos $1-\alpha$).

Ilustración con el ejemplo 3-1 ($\alpha=0.01$, $F_{0.01,4,20}=4.43$):
- $\Gamma_1=\mu_1+\mu_3-\mu_4-\mu_5$: $|C_1|=5.00$ (el libro imprime $C_1=5.00$; aritméticamente
  $9.80+17.60-21.60-10.80=-5.00$), $S_{C_1}=\sqrt{8.06(4)/5}=2.54$,
  $S_{0.01,1}=2.54\sqrt{4(4.43)}=10.69$ → no significativo.
- $\Gamma_2=\mu_1-\mu_4$: $C_2=-11.80$, $S_{C_2}=\sqrt{8.06(2)/5}=1.80$,
  $S_{0.01,2}=1.80\sqrt{4(4.43)}=7.58$ → significativo ($\mu_1\neq\mu_4$).

Scheffé puede usarse para pares de medias, pero **no es el más sensible** para ese fin.

### 3-5.7 Comparación de pares de medias de tratamientos

Hipótesis: $H_0:\mu_i=\mu_j$ vs. $H_1:\mu_i\neq\mu_j$ para toda $i\neq j$.

#### Prueba de Tukey

- Nivel de significación global **exactamente $\alpha$** con $n$ iguales y a lo sumo $\alpha$ con
  $n_i$ desiguales. Controla el error del experimento; excelente para sondeo de datos cuando interesan
  pares de medias.
- Usa el **rango studentizado** $q=\dfrac{\bar y_{\text{máx}}-\bar y_{\text{mín}}}{\sqrt{MS_E/n}}$;
  tabla VIII del apéndice: $q_\alpha(p,f)$, con $f$ = g.l. de $MS_E$.
- Dos medias difieren si $|\bar y_{i.}-\bar y_{j.}|$ excede (ec. 3-35):

$$T_\alpha=q_\alpha(a,f)\sqrt{\frac{MS_E}{n}}$$

- IC simultáneos de $100(1-\alpha)\%$ (ec. 3-36):
  $\bar y_{i.}-\bar y_{j.}\pm q_\alpha(a,f)\sqrt{MS_E/n}$, $i\neq j$.
- **Tukey–Kramer** (tamaños desiguales; ecs. 3-37 y 3-38):

$$T_\alpha=\frac{q_\alpha(a,f)}{\sqrt2}\sqrt{MS_E\left(\frac1{n_i}+\frac1{n_j}\right)},\qquad \bar y_{i.}-\bar y_{j.}\pm\frac{q_\alpha(a,f)}{\sqrt2}\sqrt{MS_E\left(\frac1{n_i}+\frac1{n_j}\right)}$$

**Ejemplo 3-7.** $q_{0.05}(5,20)=4.23$; $T_{0.05}=4.23\sqrt{8.06/5}=5.37$. Diferencias
($\bar y_{i.}-\bar y_{j.}$; * = significativa):

| Par | Dif. | Tukey (5.37) | LSD (3.75) |
|---|---|---|---|
| 1–2 | −5.6 | * | * |
| 1–3 | −7.8 | * | * |
| 1–4 | −11.8 | * | * |
| 1–5 | −1.0 | | |
| 2–3 | −2.2 | | |
| 2–4 | −6.2 | * | * |
| 2–5 | 4.6 | | * |
| 3–4 | −4.0 | | * |
| 3–5 | 6.8 | * | * |
| 4–5 | 10.8 | * | * |

Tukey (fig. 3-12): grupos $\{\mu_1,\mu_5\}$, $\{\mu_5,\mu_2\}$, $\{\mu_2,\mu_3\}$, $\{\mu_3,\mu_4\}$
no difieren (subrayados traslapados); el libro lo resume como tres grupos ($\mu_1$ y $\mu_5$;
$\mu_2$ y $\mu_3$; $\mu_4$) con pertenencia no del todo clara.

Nota: puede ocurrir que la $F$ global sea significativa y ninguna comparación por pares lo sea,
porque la $F$ considera simultáneamente *todos* los contrastes, no solo los de la forma
$\mu_i-\mu_j$.

#### Método de la diferencia significativa mínima (LSD) de Fisher

$$t_0=\frac{\bar y_{i.}-\bar y_{j.}}{\sqrt{MS_E\left(\frac1{n_i}+\frac1{n_j}\right)}}\quad\text{(3-39)}$$

$$\text{LSD}=t_{\alpha/2,\,N-a}\sqrt{MS_E\left(\frac1{n_i}+\frac1{n_j}\right)}\quad\text{(3-40)};\qquad\text{balanceado: }\text{LSD}=t_{\alpha/2,\,N-a}\sqrt{\frac{2MS_E}{n}}\quad\text{(3-41)}$$

Las medias $\mu_i$ y $\mu_j$ difieren si $|\bar y_{i.}-\bar y_{j.}|>\text{LSD}$. **Advertencia**: no
controla el error global; el error tipo I del experimento crece con $a$.

**Ejemplo 3-8.** $\text{LSD}=2.086\sqrt{2(8.06)/5}=3.75$. Solo los pares 1–5 y 2–3 **no** difieren
(fig. 3-13); el tratamiento 4 da resistencia significativamente mayor que todos los demás.

#### Prueba del rango múltiple de Duncan

1. Ordenar los $a$ promedios en forma ascendente.
2. Error estándar de cada promedio: $S_{\bar y_{i.}}=\sqrt{MS_E/n}$ (ec. 3-42). Con $n_i$
   desiguales, sustituir $n$ por la **media armónica** $n_h=a\big/\sum_{i=1}^a(1/n_i)$ (ec. 3-43).
3. De la tabla VII del apéndice obtener los rangos significativos $r_\alpha(p,f)$, $p=2,\dots,a$, y
   calcular los rangos de significación mínima (ec. 3-44): $R_p=r_\alpha(p,f)\,S_{\bar y_{i.}}$.
4. Comparar: mayor vs. menor contra $R_a$; mayor vs. segunda menor contra $R_{a-1}$; … hasta agotar
   las comparaciones con la mayor; luego segunda mayor vs. menor contra $R_{a-1}$, etc., hasta
   cubrir los $a(a-1)/2$ pares. ($p$ = número de medias en el rango que abarca el par.)
5. Para evitar contradicciones, no se declara significativa una diferencia entre dos medias que
   quedan entre otras dos que no difieren significativamente.

**Ejemplo 3-9.** Orden: $\bar y_{1.}=9.8$, $\bar y_{5.}=10.8$, $\bar y_{2.}=15.4$,
$\bar y_{3.}=17.6$, $\bar y_{4.}=21.6$; $S_{\bar y_{i.}}=1.27$; $r_{0.05}(2,20)=2.95$,
$r_{0.05}(3,20)=3.10$, $r_{0.05}(4,20)=3.18$, $r_{0.05}(5,20)=3.25$ ⇒ $R_2=3.75$, $R_3=3.94$,
$R_4=4.04$, $R_5=4.13$. Resultado: todos los pares difieren excepto 3–2 ($2.2<3.75$) y 5–1
($1.0<3.75$); idéntico al LSD en este ejemplo (fig. 3-14).

Propiedades: para $p=2$, $R_2$ = LSD. Nivel de protección $(1-\alpha)^{p-1}$ para medias separadas
$p$ pasos; el índice de error de declarar al menos una diferencia falsa es $1-(1-\alpha)^{p-1}$
(0.05 para adyacentes, 0.10 para $p=3$, …). Gran potencia; muy popular.

#### Prueba de Newman–Keuls

Igual mecánica que Duncan pero con valores críticos (ec. 3-45):

$$K_p=q_\alpha(p,f)\,S_{\bar y_{i.}},\qquad p=2,3,\dots,a$$

con $q_\alpha(p,f)$ del rango studentizado (tabla VIII). Más conservadora que Duncan: el error tipo
I del experimento es $\alpha$ para todas las pruebas con el mismo número de medias; como
$q_\alpha(p,f)>r_\alpha(p,f)$ para $p>2$, tiene menor potencia. Comparación ($\alpha=0.01$, $f=20$):

| $p$ | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|
| $r_{0.01}(p,20)$ | 4.02 | 4.22 | 4.33 | 4.40 | 4.47 | 4.53 | 4.58 |
| $q_{0.01}(p,20)$ | 4.02 | 4.64 | 5.02 | 5.29 | 5.51 | 5.69 | 5.84 |

#### ¿Qué método de comparación por pares debe usarse?

No hay respuesta precisa; hay desacuerdo entre especialistas. Según simulaciones Montecarlo de
Carmer y Swanson:
- **LSD** es muy eficaz para detectar diferencias reales si se aplica **solo después** de una $F$
  significativa al 5 % (LSD protegida).
- **Duncan** también tiene buen desempeño. LSD y Duncan son los más potentes de los vistos, pero no
  controlan el índice de error en el modo del experimento.
- **Tukey** controla el error global; por eso muchos lo prefieren.
- **Newman–Keuls**: más conservador que Duncan, menor potencia.

| Método | Estadístico crítico | Tabla | Controla error global | Uso típico |
|---|---|---|---|---|
| Scheffé | $S_{C_u}\sqrt{(a-1)F_{\alpha,a-1,N-a}}$ | $F$ | Sí (todos los contrastes) | Contrastes no planeados, sondeo |
| Tukey | $q_\alpha(a,f)\sqrt{MS_E/n}$ | VIII | Sí (todos los pares) | Todos los pares |
| LSD Fisher | $t_{\alpha/2,N-a}\sqrt{2MS_E/n}$ | $t$ | No | Pares, tras $F$ significativa |
| Duncan | $r_\alpha(p,f)\sqrt{MS_E/n}$ | VII | No | Pares, alta potencia |
| Newman–Keuls | $q_\alpha(p,f)\sqrt{MS_E/n}$ | VIII | Por tamaño de grupo | Pares, conservador |
| Dunnett | $d_\alpha(a-1,f)\sqrt{MS_E(1/n_i+1/n_a)}$ | IX | Sí ($a-1$ comparaciones) | Tratamientos vs. control |

### 3-5.8 Comparación de medias de tratamientos con un control (Dunnett)

Tratamiento $a$ = control; solo $a-1$ comparaciones: $H_0:\mu_i=\mu_a$ vs. $H_1:\mu_i\neq\mu_a$,
$i=1,\dots,a-1$. Se rechaza $H_0$ si (ec. 3-46):

$$|\bar y_{i.}-\bar y_{a.}|>d_\alpha(a-1,f)\sqrt{MS_E\left(\frac1{n_i}+\frac1{n_a}\right)}$$

con $d_\alpha(a-1,f)$ de la tabla IX (una o dos colas); $\alpha$ es el nivel de significación
**conjunto** de las $a-1$ pruebas.

**Ejemplo 3-10.** Tratamiento 5 como control; $d_{0.05}(4,20)=2.65$; diferencia crítica
$2.65\sqrt{2(8.06)/5}=4.76$. Diferencias con el control: 1–5 = −1.0; 2–5 = 4.6; 3–5 = 6.8; 4–5 = 10.8
⇒ solo $\mu_3\neq\mu_5$ y $\mu_4\neq\mu_5$.

**Regla de diseño**: asignar más observaciones al control ($n_a$) que a los demás ($n$), con
$n_a/n\approx\sqrt a$.

## 3-6 Muestra de salida de computadora

Salida de *Design-Expert* para el ejemplo 3-1 (fig. 3-15), útil para validar software:

- ANOVA: Model (A) SS 475.76, 4 g.l., MS 118.94, F 14.76, Prob > F < 0.0001; Residual 161.20,
  20 g.l., MS 8.06 (Lack of Fit 0.000 con 0 g.l.; Pure Error 161.20 con 20 g.l.); Cor Total 636.96,
  24 g.l.
- Std. Dev. = 2.84; Mean = 15.04; C.V. = 18.88; PRESS = 251.88; R-Squared = 0.7469;
  Adj R-Squared = 0.6963; Pred R-Squared = 0.6046; Adeq Precision = 9.294.
- Definiciones:
  - $R^2=SS_{\text{Modelo}}/SS_{\text{Total}}=475.76/636.96=0.746923$: proporción de variabilidad
    "explicada"; $0\le R^2\le1$.
  - $R^2$ ajustada: refleja el número de términos del modelo; útil al agregar o quitar términos.
  - C.V. $=(\sqrt{MS_E}/\bar y)\,100$: variabilidad no explicada como porcentaje de la media.
  - PRESS (*Prediction Error Sum of Squares*): qué tan bien predeciría el modelo un experimento
    nuevo; deseable pequeño. $R^2_{\text{Pred}}$ se basa en PRESS. Una diferencia mayor que 0.20
    entre $R^2_{\text{Pred}}$ y $R^2_{\text{ajustada}}$ señala un posible problema con el modelo o
    los datos.
  - "Adeq Precision": (predicción máxima − predicción mínima) / desviación estándar promedio de las
    predicciones (relación señal/ruido); deseable > 4.
- Medias de tratamientos: 9.80, 15.40, 17.60, 21.60, 10.80, error estándar 1.27
  ($=\sqrt{MS_E/n}$).
- Diferencias por pares (LSD de Fisher; error estándar 1.80, 1 g.l. cada una):

| Par | Dif. | $t$ | Prob > \|t\| |
|---|---|---|---|
| 1 vs 2 | −5.60 | −3.12 | 0.0054 |
| 1 vs 3 | −7.80 | −4.34 | 0.0003 |
| 1 vs 4 | −11.80 | −6.57 | <0.0001 |
| 1 vs 5 | −1.00 | −0.56 | 0.5838 |
| 2 vs 3 | −2.20 | −1.23 | 0.2347 |
| 2 vs 4 | −6.20 | −3.45 | 0.0025 |
| 2 vs 5 | 4.60 | 2.56 | 0.0186 |
| 3 vs 4 | −4.00 | −2.23 | 0.0375 |
| 3 vs 5 | 6.80 | 3.79 | 0.0012 |
| 4 vs 5 | 10.80 | 6.01 | <0.0001 |

- Diagnósticos por corrida: leverage = 0.200 en todas; mayor residual 5.20 (orden estándar 3),
  residual studentizado 2.048, distancia de Cook 0.210, *outlier t* 2.245.
- Gráficas de diagnóstico sugeridas: probabilidad normal de residuales studentizados; residuales
  studentizados vs. predichos; *outlier t* vs. orden de corrida; Box–Cox para transformaciones de
  potencia.
- Las guías de interpretación automáticas son genéricas; no sustituyen la redacción del informe.

## 3-7 Determinación del tamaño de la muestra

Más réplicas ⇒ capacidad de detectar efectos más pequeños.

### 3-7.1 Curvas de operación característica (OC)

Grafican $\beta$ (error tipo II) contra un parámetro que mide cuán falsa es $H_0$:

$$\beta=1-P\{F_0>F_{\alpha,\,a-1,\,N-a}\mid H_0\text{ falsa}\}\quad\text{(ec. 3-47)}$$

Si $H_0$ es falsa, $F_0\sim F$ **no central** con $a-1$ y $N-a$ g.l. y parámetro de no centralidad
$\delta$. Las curvas (parte V del apéndice; $\alpha=0.05$ y $0.01$) usan:

$$\Phi^2=\frac{n\sum_{i=1}^a\tau_i^2}{a\,\sigma^2}\quad\text{(ec. 3-48)}$$

Procedimiento:
1. Especificar las medias $\mu_1,\dots,\mu_a$ para las que se quiere rechazar con alta probabilidad;
   $\tau_i=\mu_i-\bar\mu$, $\bar\mu=\frac1a\sum\mu_i$.
2. Obtener una estimación de $\sigma^2$ (experiencia, experimento previo, prueba piloto o juicio).
   Si es incierta, repetir el cálculo para un rango de valores de $\sigma^2$.
3. Para valores tentativos de $n$: calcular $\Phi$, entrar a la curva con $\nu_1=a-1$,
   $\nu_2=a(n-1)$ y $\alpha$, leer $\beta$; aumentar $n$ hasta lograr la potencia $1-\beta$ deseada.

**Ejemplo 3-11.** $\mu$ = 11, 12, 15, 18, 19 ⇒ $\bar\mu=15$, $\tau$ = −4, −3, 0, 3, 4,
$\sum\tau_i^2=50$; $\sigma=3$; $\alpha=0.01$; potencia deseada ≥ 0.90.
$\Phi^2=n(50)/[5(3^2)]=1.11n$.

| $n$ | $\Phi^2$ | $\Phi$ | $a(n-1)$ | $\beta$ | Potencia |
|---|---|---|---|---|---|
| 4 | 4.44 | 2.11 | 15 | 0.30 | 0.70 |
| 5 | 5.55 | 2.36 | 20 | 0.15 | 0.85 |
| 6 | 6.66 | 2.58 | 25 | 0.04 | 0.96 |

⇒ al menos $n=6$ réplicas.

**Alternativa por diferencia máxima $D$**: si se quiere rechazar cuando dos medias cualesquiera
difieren en $D$, el valor **mínimo** de $\Phi^2$ es (ec. 3-49):

$$\Phi^2=\frac{nD^2}{2a\sigma^2}$$

Da un tamaño de muestra conservador (potencia al menos la especificada). Ejemplo: $D=10$,
$\sigma=3$, $a=5$ ⇒ $\Phi^2=n(10)^2/[2(5)(3^2)]=1.11n$ ⇒ $n=6$ con $\alpha=0.01$.

### 3-7.2 Especificación de un incremento de la desviación estándar

Si las medias difieren, la desviación estándar de una observación tomada al azar es
$\sqrt{\sigma^2+\sum_i\tau_i^2/a}$. Fijando un incremento porcentual $P$ a partir del cual se quiere
rechazar: $\sqrt{\sigma^2+\sum\tau_i^2/a}\,/\sigma=1+0.01P$, de donde (ec. 3-50):

$$\Phi=\frac{\sqrt{\sum_i\tau_i^2/a}}{\sigma/\sqrt n}=\sqrt{(1+0.01P)^2-1}\;\sqrt n$$

Ejemplo: $P=20\%$, potencia ≥ 0.90, $\alpha=0.05$ ⇒ $\Phi=\sqrt{1.2^2-1}\sqrt n=0.66\sqrt n$ ⇒
$n=9$.

### 3-7.3 Método para estimar el intervalo de confianza

Se especifica de antemano la semiamplitud deseada del IC para la diferencia de dos medias:
$\pm t_{\alpha/2,\,N-a}\sqrt{2MS_E/n}$, usando una estimación previa de $\sigma^2$ en lugar de
$MS_E$. Ejemplo ($\sigma=3$, 95 %, precisión deseada ±5 psi, $a=5$): $n=5$ ⇒
$\pm2.086\sqrt{2(9)/5}=\pm3.96$; $n=4$ ⇒ $\pm2.132\sqrt{2(9)/4}=\pm4.52$; $n=3$ ⇒
$\pm2.228\sqrt{2(9)/3}=\pm5.46$ ⇒ el menor tamaño que cumple es $n=4$. El mismo enfoque sirve para
intervalos simultáneos o para contrastes generales.

## 3-8 Identificación de efectos de dispersión

- **Efectos de localización**: el factor cambia la media. **Efectos de dispersión**: el factor
  cambia la variabilidad. Se estudian usando una medida de variabilidad (desviación estándar,
  varianza) como respuesta.
- Recomendación: usar $\log(s)$ o $\log(s^2)$ como respuesta (el logaritmo estabiliza la
  variabilidad de la distribución de la desviación estándar muestral).
- **Ejemplo de la fundición de aluminio** (tabla 3-12): 4 algoritmos para controlar la proporción
  de alúmina, $n=6$ corridas cada uno; respuestas: voltaje promedio de la celda y su desviación
  estándar ("ruido del crisol"). El ANOVA del voltaje promedio no muestra efecto de localización
  (problema 3-28). Para la dispersión se usa $y=-\ln(s)$ (todas las $s<1$). ANOVA (tabla 3-13):

| Fuente | SS | G.l. | MS | $F_0$ | Valor $P$ |
|---|---|---|---|---|---|
| Algoritmo | 6.166 | 3 | 2.055 | 21.96 | <0.001 |
| Error | 1.872 | 20 | 0.094 | | |
| Total | 8.038 | 23 | | | |

  Hay **efecto de dispersión**. Con la distribución $t$ escalada (factor
  $\sqrt{MS_E/n}=\sqrt{0.094/6}=0.125$; fig. 3-16) se ve que el algoritmo 3 produce más ruido
  (menor $-\ln s$) que los algoritmos 1, 2 y 4, que no difieren mucho entre sí. Los residuales no
  muestran problemas.

## 3-9 El enfoque de regresión para el análisis de varianza

**Prueba general de significación de la regresión**: se compara la reducción en la suma de
cuadrados al ajustar el modelo completo con la del modelo restringido a $H_0$; la diferencia es la
suma de cuadrados de la hipótesis.

### 3-9.1 Estimación de mínimos cuadrados de los parámetros del modelo

Minimizar $L=\sum_i\sum_j(y_{ij}-\mu-\tau_i)^2$ (ec. 3-51). Las derivadas parciales igualadas a cero
dan las $a+1$ **ecuaciones normales** (ec. 3-52):

$$N\hat\mu+n\hat\tau_1+n\hat\tau_2+\dots+n\hat\tau_a=y_{..}$$

$$n\hat\mu+n\hat\tau_i=y_{i.},\qquad i=1,\dots,a$$

- No son linealmente independientes (la suma de las últimas $a$ da la primera) ⇒ no hay solución
  única. Se impone una **restricción**, usualmente $\sum_i\hat\tau_i=0$ (ec. 3-53), que da
  $\hat\mu=\bar y_{..}$, $\hat\tau_i=\bar y_{i.}-\bar y_{..}$ (ec. 3-54).
- La solución depende de la restricción elegida, pero las **funciones estimables** se estiman de
  manera única sin importar la restricción: p. ej. $\tau_i-\tau_j$ (estimada por
  $\bar y_{i.}-\bar y_{j.}$) y $\mu_i=\mu+\tau_i$ (estimada por $\bar y_{i.}$). En general, es
  estimable toda combinación lineal de los miembros izquierdos de las ecuaciones normales.

### 3-9.2 Prueba general de significación de la regresión

Reglas para escribir las ecuaciones normales de **cualquier** diseño:
1. Hay una ecuación normal por cada parámetro del modelo.
2. El miembro derecho es la suma de todas las observaciones que contienen ese parámetro.
3. El miembro izquierdo es la suma de todos los parámetros (con acento circunflejo), cada uno
   multiplicado por el número de veces que aparece en el total del miembro derecho. (El miembro
   izquierdo es el valor esperado del derecho.)

Reducción en la suma de cuadrados = suma de (estimación del parámetro × miembro derecho de su
ecuación normal). Para el modelo completo (ec. 3-55):

$$R(\mu,\tau)=\hat\mu\,y_{..}+\sum_{i=1}^a\hat\tau_i\,y_{i.}=\sum_{i=1}^a\frac{y_{i.}^2}{n}\qquad(a\text{ g.l.})$$

Los g.l. de una reducción = número de ecuaciones normales linealmente independientes. Error
(ec. 3-56):

$$SS_E=\sum_i\sum_j y_{ij}^2-R(\mu,\tau)=\sum_i\sum_j y_{ij}^2-\sum_i\frac{y_{i.}^2}{n}\qquad(N-a\text{ g.l.})$$

Modelo reducido bajo $H_0$ ($y_{ij}=\mu+\varepsilon_{ij}$): una ecuación normal $N\hat\mu=y_{..}$,
$R(\mu)=y_{..}^2/N$ (1 g.l.). Entonces:

$$R(\tau\mid\mu)=R(\mu,\tau)-R(\mu)=\frac1n\sum_{i=1}^a y_{i.}^2-\frac{y_{..}^2}{N}=SS_{\text{Trat}}\qquad(a-1\text{ g.l.})$$

$$F_0=\frac{R(\tau\mid\mu)/(a-1)}{\left[\sum_i\sum_j y_{ij}^2-R(\mu,\tau)\right]/(N-a)}\sim F_{a-1,\,N-a}\text{ bajo }H_0$$

que es exactamente el estadístico del ANOVA de un factor.

## 3-10 Métodos no paramétricos en el análisis de varianza

### 3-10.1 La prueba de Kruskal–Wallis

Cuándo: el supuesto de normalidad no está justificado. $H_0$: los $a$ tratamientos son idénticos;
$H_1$: algunos tratamientos generan observaciones mayores que otros (en la práctica, prueba de
igualdad de medias).

Procedimiento:
1. Ordenar las $N$ observaciones de menor a mayor y reemplazarlas por sus rangos $R_{ij}$ (rango 1
   a la menor); en empates, asignar el rango promedio.
2. Calcular $R_{i.}$ = suma de rangos del tratamiento $i$.
3. Estadístico (ecs. 3-57 y 3-58):

$$H=\frac1{S^2}\left[\sum_{i=1}^a\frac{R_{i.}^2}{n_i}-\frac{N(N+1)^2}{4}\right],\qquad S^2=\frac1{N-1}\left[\sum_{i=1}^a\sum_{j=1}^{n_i}R_{ij}^2-\frac{N(N+1)^2}{4}\right]$$

   $S^2$ es la varianza de los rangos. Sin empates $S^2=N(N+1)/12$ y (ec. 3-59):

$$H=\frac{12}{N(N+1)}\sum_{i=1}^a\frac{R_{i.}^2}{n_i}-3(N+1)$$

   Con pocos empates puede usarse la forma simple.
4. Si $n_i\ge5$, $H\approx\chi^2_{a-1}$ bajo $H_0$: rechazar si $H>\chi^2_{\alpha,\,a-1}$.

**Ejemplo 3-12.** Ejemplo 3-1 con muchos empates (tabla 3-14): sumas de rangos $R_{i.}$ = 27.5,
66.0, 85.0, 113.0, 33.5; $\sum\sum R_{ij}^2=5497.79$;
$S^2=\frac1{24}\left[5497.79-\frac{25(26)^2}{4}\right]=53.03$;
$H=\frac1{53.03}\left[5245.0-\frac{25(26)^2}{4}\right]=19.25>\chi^2_{0.01,4}=13.28$; $P=0.0002$.
Misma conclusión que el ANOVA.

### 3-10.2 Comentarios generales sobre la transformación de rangos

- Aplicar la $F$ usual a los rangos da (ec. 3-60):

$$F_0=\frac{H/(a-1)}{(N-1-H)/(N-a)}$$

  monótona en $H$ ⇒ Kruskal–Wallis equivale al ANOVA usual sobre los rangos.
- La **transformación de rangos** sirve en diseños sin alternativa no paramétrica (procedimiento
  aproximado con buenas propiedades; Conover e Iman).
- Recomendación: ante dudas de normalidad o puntos atípicos, hacer el ANOVA con los datos originales
  **y** con los rangos. Si coinciden, los supuestos se satisfacen razonablemente y vale el análisis
  estándar; si difieren, preferir el análisis de rangos e investigar transformaciones, atípicos y el
  procedimiento experimental.

## 3-11 Problemas (solo referencia)

Problemas 3-1 a 3-35 (págs. 119–125). Ubicación de los relacionados con el texto:
- 3-21 / 3-22: Bartlett y Levene modificada sobre el problema 3-14 (baterías).
- 3-23 a 3-27: tamaño de muestra (curvas OC, incremento de $\sigma$, ancho de IC).
- 3-28 / 3-29: verificación del experimento de la fundición de aluminio (sección 3-8).
- 3-30: efectos de dispersión en máquina CNC (respuesta = desviación estándar).
- 3-31 / 3-32: ecuaciones normales con distintas restricciones y prueba general de regresión.
- 3-33 a 3-35: Kruskal–Wallis (incluye el efecto de un dato atípico).
- 3-16 / 3-17: conjuntos de datos pensados para transformación (tiempos de falla, conteos).

---

## Resumen operativo (flujo de análisis de un factor)

1. Aleatorizar completamente el orden de las $N$ corridas; preferir diseño balanceado.
2. Graficar (cajas, dispersión).
3. ANOVA: $F_0=MS_{\text{Trat}}/MS_E$ contra $F_{\alpha,a-1,N-a}$.
4. Residuales $e_{ij}=y_{ij}-\bar y_{i.}$: probabilidad normal, vs. orden temporal, vs. ajustados,
   vs. otras variables; residuales estandarizados para atípicos; Bartlett (si hay normalidad) o
   Levene modificada.
5. Si la varianza no es constante: transformar ($\lambda=1-\alpha$, pendiente de $\log S_i$ vs.
   $\log\bar y_{i.}$), restar 1 g.l. al error, repetir el diagnóstico.
6. Interpretación: regresión si el factor es cuantitativo; contrastes ortogonales si hay
   comparaciones preplaneadas; Scheffé para contrastes no planeados; Tukey / LSD / Duncan /
   Newman–Keuls para pares; Dunnett contra un control.
7. Si la normalidad es dudosa: Kruskal–Wallis o ANOVA sobre rangos como contraste.

## Erratas y discrepancias observadas en esta edición

- Ejemplo 3-3 (pág. 75): se imprime $\hat\tau_3=17.60-15.04=-2.56$; el valor correcto es $+2.56$.
- Sección 3-5.6 (pág. 95): se imprime $C_1=9.80+17.60-21.60-10.80=5.00$; aritméticamente es $-5.00$
  (no cambia la conclusión, se compara $|C_1|$).
- Ejemplo 3-9 (pág. 101): en la comparación "3 vs. 5" se imprime $R_3=3.95$; el valor calculado
  arriba es $R_3=3.94$.
- Pág. 99: el texto remite a la "ecuación 3-38" al deducir el intervalo de Tukey para tamaños
  iguales; el intervalo correspondiente es la ec. 3-36.
- Pág. 99: el texto dice que el LSD "utiliza el estadístico $F$"; la ec. 3-39 es un estadístico $t$.
