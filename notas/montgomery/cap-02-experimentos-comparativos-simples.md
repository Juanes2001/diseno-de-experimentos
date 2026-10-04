# Capítulo 2 — Experimentos comparativos simples

> Montgomery, págs. 21–59

Ficha técnica de consulta. **Experimentos comparativos simples**: experimentos para comparar
dos **condiciones** (dos **tratamientos**, o dos **niveles** de un único **factor**). El capítulo
repasa los conceptos estadísticos básicos y desarrolla las pruebas $t$, $Z$, $\chi^2$ y $F$ para
medias y varianzas, los intervalos de confianza asociados, la elección del tamaño de muestra y
el diseño de comparaciones pareadas (primer caso de formación de bloques).

Mapa rápido de métodos:

| Situación | Estadístico | Distribución de referencia | Sección |
|---|---|---|---|
| Dos medias, varianzas desconocidas e iguales | $t_0$ con $S_p$ (ec. 2-24) | $t_{n_1+n_2-2}$ | 2-4.1 |
| Dos medias, varianzas desconocidas y distintas | $t_0$ (ec. 2-31) | $t_v$ aprox., $v$ de ec. 2-32 | 2-4.4 |
| Dos medias, varianzas conocidas | $Z_0$ (ec. 2-33) | $N(0,1)$ | 2-4.5 |
| Una media, varianza conocida | $Z_0$ (ec. 2-35) | $N(0,1)$ | 2-4.6 |
| Una media, varianza desconocida | $t_0$ (ec. 2-37) | $t_{n-1}$ | 2-4.6 |
| Dos medias, observaciones pareadas | $t_0 = \bar d/(S_d/\sqrt n)$ (ec. 2-41) | $t_{n-1}$ | 2-5 |
| Una varianza | $\chi_0^2$ (ec. 2-45) | $\chi^2_{n-1}$ | 2-6 |
| Dos varianzas | $F_0 = S_1^2/S_2^2$ (ec. 2-48) | $F_{n_1-1,\,n_2-1}$ | 2-6 |

---

## 2-1 Introducción

Ejemplo guía del capítulo: **fuerza de la tensión de adhesión del mortero de cemento portland**.
Se compara una formulación modificada (con emulsiones de látex de polímeros) con la formulación
sin modificar; 10 observaciones de cada una (tabla 2-1). Medias: $\bar y_1 = 16.76$ kgf/cm²
(modificado) y $\bar y_2 = 17.92$ kgf/cm² (sin modificar). La pregunta es si esa diferencia es
real o resultado de fluctuaciones del muestreo; se responde con una **prueba de hipótesis**
(o **prueba de significación**), que permite comparar en términos objetivos y con riesgos
conocidos.

## 2-2 Conceptos estadísticos básicos

- **Corrida**: cada observación del experimento. Las corridas difieren entre sí: hay **ruido**,
  llamado **error experimental** o simplemente **error**. Es un **error estadístico**: proviene
  de variación no controlada y generalmente inevitable.
- La respuesta es por tanto una **variable aleatoria**, **discreta** (conjunto de valores finito
  o contablemente infinito) o **continua** (el conjunto de valores es un intervalo).

### Descripción gráfica de la variabilidad

| Gráfica | Uso | Notas |
|---|---|---|
| **Diagrama de puntos** (fig. 2-1) | Conjuntos pequeños (hasta unas 20 observaciones) | Muestra localización (tendencia central) y dispersión. En el mortero: las formulaciones difieren en la media pero tienen aproximadamente la misma variación. |
| **Histograma** (fig. 2-2) | Datos numerosos | Eje horizontal dividido en intervalos (generalmente de igual longitud); rectángulo sobre el intervalo $j$ con área proporcional a $n_j$. Muestra tendencia central, dispersión y forma general de la distribución. |
| **Diagrama de caja** (y bigotes) (fig. 2-3) | Comparación de muestras | Caja del cuartil inferior (percentil 25) al superior (percentil 75), línea en la mediana (percentil 50), bigotes hasta (típicamente) mínimo y máximo. En el mortero: diferencia clara en la media, distribuciones razonablemente simétricas y de dispersión similar. |

### Distribuciones de probabilidad

- $y$ discreta: función de probabilidad $p(y)$, con $0 \le p(y_j) \le 1$,
  $P(y = y_j) = p(y_j)$ y $\sum_{j} p(y_j) = 1$. La probabilidad es la *altura* de $p(y_j)$.
- $y$ continua: función de densidad $f(y)$, con $f(y) \ge 0$,
  $P(a \le y \le b) = \int_a^b f(y)\,dy$ y $\int_{-\infty}^{\infty} f(y)\,dy = 1$. La
  probabilidad es el *área* bajo la curva.

### Media, varianza y valores esperados

$$\mu = E(y) = \begin{cases} \int_{-\infty}^{\infty} y f(y)\,dy & y \text{ continua} \\ \sum_{y} y\,p(y) & y \text{ discreta} \end{cases} \qquad \text{(ecs. 2-1, 2-2)}$$

$$\sigma^2 = \begin{cases} \int_{-\infty}^{\infty} (y-\mu)^2 f(y)\,dy & y \text{ continua} \\ \sum_{y} (y-\mu)^2 p(y) & y \text{ discreta} \end{cases} \qquad \text{(ec. 2-3)}$$

$$\sigma^2 = E[(y-\mu)^2], \qquad V(y) \equiv E[(y-\mu)^2] = \sigma^2 \qquad \text{(ecs. 2-4, 2-5)}$$

Reglas de los operadores $E$ y $V$ ($c$ constante; $y$ con media $\mu$ y varianza $\sigma^2$;
$y_1$, $y_2$ con medias $\mu_1$, $\mu_2$ y varianzas $\sigma_1^2$, $\sigma_2^2$):

| N.º | Regla | Condición |
|---|---|---|
| 1 | $E(c) = c$ | |
| 2 | $E(y) = \mu$ | |
| 3 | $E(cy) = cE(y) = c\mu$ | |
| 4 | $V(c) = 0$ | |
| 5 | $V(y) = \sigma^2$ | |
| 6 | $V(cy) = c^2 V(y) = c^2\sigma^2$ | |
| 7 | $E(y_1 + y_2) = \mu_1 + \mu_2$ | siempre |
| 8 | $V(y_1 + y_2) = V(y_1) + V(y_2) + 2\,\mathrm{Cov}(y_1, y_2)$ | siempre |
| 9 | $V(y_1 - y_2) = V(y_1) + V(y_2) - 2\,\mathrm{Cov}(y_1, y_2)$ | siempre |
| 10 | $V(y_1 \pm y_2) = \sigma_1^2 + \sigma_2^2$ | $y_1$, $y_2$ independientes |
| 11 | $E(y_1 \cdot y_2) = E(y_1)\cdot E(y_2) = \mu_1 \mu_2$ | $y_1$, $y_2$ independientes |
| 12 | $E(y_1 / y_2) \ne E(y_1)/E(y_2)$ en general | sean o no independientes |

**Covarianza** (ec. 2-6): $\mathrm{Cov}(y_1, y_2) = E[(y_1 - \mu_1)(y_2 - \mu_2)]$; mide la
asociación lineal. Independencia ⇒ $\mathrm{Cov} = 0$; el recíproco no es necesariamente cierto.

---

## 2-3 Muestreo y distribuciones de muestreo

### Muestras aleatorias, media y varianza muestrales

- **Muestreo aleatorio**: de una población de $N$ elementos se elige una muestra de $n$ de modo
  que cada una de las $N!/[(N-n)!\,n!]$ muestras posibles tenga la misma probabilidad. Ayuda
  práctica: tablas de números aleatorios (tabla XI del apéndice).
- **Estadístico**: cualquier función de las observaciones de una muestra que no contiene
  parámetros desconocidos.

$$\bar y = \frac{\sum_{i=1}^{n} y_i}{n} \quad \text{(ec. 2-7)} \qquad\qquad S^2 = \frac{\sum_{i=1}^{n} (y_i - \bar y)^2}{n-1} \quad \text{(ec. 2-8)}$$

- $S = \sqrt{S^2}$ es la **desviación estándar muestral** (mismas unidades que $y$).

### Propiedades de los estimadores

- **Estimador**: estadístico que corresponde a un parámetro desconocido (es variable aleatoria).
  **Estimación**: su valor numérico en una muestra concreta. Ejemplo: $n = 25$ ejemplares de una
  fibra textil, $\bar y = 18.6$ y $S^2 = 1.20$.
- Propiedades deseables: (1) **insesgado** (su valor esperado es el parámetro); (2) **varianza
  mínima** entre los insesgados.
- $E(\bar y) = \mu$ y $E(S^2) = \sigma^2$: ambos son insesgados. Demostración de la segunda con
  la **suma de cuadrados corregida** $SS = \sum_{i=1}^{n} (y_i - \bar y)^2$:

$$E(SS) = E\left[\sum_{i=1}^{n} y_i^2 - n\bar y^2\right] = \sum_{i=1}^{n} (\mu^2 + \sigma^2) - n(\mu^2 + \sigma^2/n) = (n-1)\sigma^2 \qquad \text{(ecs. 2-9, 2-10)}$$

### Grados de libertad

- $n - 1$ es el número de **grados de libertad** de $SS$. Resultado general: si $SS$ tiene $v$
  grados de libertad,

$$E\left(\frac{SS}{v}\right) = \sigma^2 \qquad \text{(ec. 2-11)}$$

- Los grados de libertad de una suma de cuadrados son el número de elementos independientes que
  contiene. En $SS = \sum (y_i - \bar y)^2$ hay $n$ elementos, pero $\sum (y_i - \bar y) = 0$,
  así que solo $n - 1$ son independientes.

### Distribuciones de muestreo

**Distribución de muestreo**: distribución de probabilidad de un estadístico.

**Normal.** $y \sim N(\mu, \sigma^2)$:

$$f(y) = \frac{1}{\sigma\sqrt{2\pi}}\, e^{-(1/2)[(y-\mu)/\sigma]^2}, \qquad -\infty < y < \infty \qquad \text{(ec. 2-12)}$$

- Estandarización: $z = (y - \mu)/\sigma \sim N(0, 1)$ (ec. 2-13). Tabla I del apéndice: normal
  estándar acumulada.
- **Teorema del límite central (teorema 2-1).** Si $y_1, \dots, y_n$ son independientes e
  idénticamente distribuidas con $E(y_i) = \mu$ y $V(y_i) = \sigma^2$ finitas, y
  $x = y_1 + \dots + y_n$, entonces

$$z_n = \frac{x - n\mu}{\sqrt{n\sigma^2}}$$

  tiene distribución aproximadamente $N(0,1)$ (en el límite $n \to \infty$). La aproximación
  puede ser buena con $n < 10$ en unos casos y requerir $n > 100$ en otros. Justifica el modelo
  normal para el error experimental cuando este surge de forma aditiva de varias fuentes
  independientes.

**Ji-cuadrada.** Si $z_1, \dots, z_k$ son NID(0, 1), entonces $x = z_1^2 + \dots + z_k^2 \sim
\chi^2_k$:

$$f(x) = \frac{1}{2^{k/2}\,\Gamma(k/2)}\, x^{(k/2)-1} e^{-x/2}, \qquad x > 0 \qquad \text{(ec. 2-14)}$$

- Asimétrica (sesgada); $\mu = k$, $\sigma^2 = 2k$. Tabla III del apéndice.
- Resultado clave: si $y_1, \dots, y_n$ es muestra aleatoria de $N(\mu, \sigma^2)$,

$$\frac{SS}{\sigma^2} = \frac{\sum_{i=1}^{n} (y_i - \bar y)^2}{\sigma^2} \sim \chi^2_{n-1} \qquad \text{(ec. 2-15)}$$

  Una suma de cuadrados de variables normales dividida por $\sigma^2$ sigue una ji-cuadrada.
- Como $S^2 = SS/(n-1)$ (ec. 2-16), la distribución de $S^2$ es $[\sigma^2/(n-1)]\,\chi^2_{n-1}$.

**$t$ de Student.** Si $z \sim N(0,1)$ y $\chi^2_k$ son independientes,

$$t_k = \frac{z}{\sqrt{\chi^2_k / k}} \qquad \text{(ec. 2-17)}$$

$$f(t) = \frac{\Gamma[(k+1)/2]}{\sqrt{k\pi}\,\Gamma(k/2)} \cdot \frac{1}{[(t^2/k) + 1]^{(k+1)/2}}, \qquad -\infty < t < \infty \qquad \text{(ec. 2-18)}$$

- $\mu = 0$, $\sigma^2 = k/(k-2)$ para $k > 2$. Con $k = \infty$ es la normal estándar. Tabla II.
- Si $y_1, \dots, y_n$ es muestra aleatoria de $N(\mu, \sigma^2)$:

$$t = \frac{\bar y - \mu}{S/\sqrt{n}} \sim t_{n-1} \qquad \text{(ec. 2-19)}$$

**$F$.** Si $\chi^2_u$ y $\chi^2_v$ son independientes,

$$F_{u,v} = \frac{\chi^2_u / u}{\chi^2_v / v} \qquad \text{(ec. 2-20)}$$

$$h(x) = \frac{\Gamma\!\left(\frac{u+v}{2}\right)\left(\frac{u}{v}\right)^{u/2} x^{(u/2)-1}}{\Gamma\!\left(\frac{u}{2}\right)\Gamma\!\left(\frac{v}{2}\right)\left[\left(\frac{u}{v}\right)x + 1\right]^{(u+v)/2}}, \qquad 0 < x < \infty \qquad \text{(ec. 2-21)}$$

- $u$ grados de libertad en el numerador y $v$ en el denominador. Tabla IV del apéndice.
- Dos poblaciones normales independientes con varianza común $\sigma^2$ y muestras de tamaños
  $n_1$ y $n_2$:

$$\frac{S_1^2}{S_2^2} \sim F_{n_1-1,\,n_2-1} \qquad \text{(ec. 2-22)}$$

---

## 2-4 Inferencias acerca de las diferencias en las medias, diseños aleatorizados

Supuesto de toda la sección: **diseño completamente aleatorizado**; los datos se consideran
como si fueran una muestra aleatoria de una distribución normal.

### 2-4.1 Prueba de hipótesis

**Situación** (fig. 2-9): $y_{11}, \dots, y_{1n_1}$ son las $n_1$ observaciones del nivel 1 del
factor y $y_{21}, \dots, y_{2n_2}$ las $n_2$ del nivel 2; muestras al azar de dos poblaciones
normales independientes $N(\mu_1, \sigma_1^2)$ y $N(\mu_2, \sigma_2^2)$.

**Modelo de los datos** (ec. 2-23):

$$y_{ij} = \mu_i + \varepsilon_{ij}, \qquad i = 1, 2; \quad j = 1, 2, \dots, n_i$$

- $y_{ij}$: observación $j$ del nivel $i$; $\mu_i$: media de la respuesta en el nivel $i$;
  $\varepsilon_{ij}$: componente del **error aleatorio**, $\varepsilon_{ij} \sim
  \text{NID}(0, \sigma_i^2)$. Por tanto $y_{ij} \sim \text{NID}(\mu_i, \sigma_i^2)$.

**Hipótesis estadísticas.** Una hipótesis estadística es un enunciado sobre los parámetros de
una distribución o de un modelo.

$$H_0: \mu_1 = \mu_2 \qquad H_1: \mu_1 \ne \mu_2$$

- $H_0$: **hipótesis nula**; $H_1$: **hipótesis alternativa** (aquí **de dos colas**).
- Procedimiento: tomar una muestra aleatoria, calcular un **estadístico de prueba** y rechazar
  o no $H_0$ según caiga en la **región crítica** (región de rechazo).
- Errores:

| | Definición | Probabilidad |
|---|---|---|
| Error tipo I | Rechazar $H_0$ siendo verdadera | $\alpha = P(\text{rechazar } H_0 \mid H_0 \text{ verdadera})$ — **nivel de significación** |
| Error tipo II | No rechazar $H_0$ siendo falsa | $\beta = P(\text{no rechazar } H_0 \mid H_0 \text{ falsa})$ |
| Potencia | | $1 - \beta = P(\text{rechazar } H_0 \mid H_0 \text{ falsa})$ |

- Procedimiento general: fijar $\alpha$ y diseñar la prueba para que $\beta$ sea
  convenientemente pequeña.

**Prueba $t$ de dos muestras** (varianzas iguales, $\sigma_1^2 = \sigma_2^2 = \sigma^2$):

$$t_0 = \frac{\bar y_1 - \bar y_2}{S_p\sqrt{\dfrac{1}{n_1} + \dfrac{1}{n_2}}} \qquad \text{(ec. 2-24)}$$

$$S_p^2 = \frac{(n_1 - 1)S_1^2 + (n_2 - 1)S_2^2}{n_1 + n_2 - 2} \qquad \text{(ec. 2-25)}$$

- $S_p^2$: estimación combinada (*pooled*) de la varianza común.
- **Distribución de referencia**: $t$ con $n_1 + n_2 - 2$ grados de libertad (describe el
  comportamiento de $t_0$ cuando $H_0$ es verdadera).
- Criterios de rechazo:

| Alternativa | Rechazar $H_0$ si |
|---|---|
| $H_1: \mu_1 \ne \mu_2$ | $\lvert t_0 \rvert > t_{\alpha/2,\,n_1+n_2-2}$ |
| $H_1: \mu_1 > \mu_2$ | $t_0 > t_{\alpha,\,n_1+n_2-2}$ |
| $H_1: \mu_1 < \mu_2$ | $t_0 < -t_{\alpha,\,n_1+n_2-2}$ |

- Justificación: $\bar y_1 - \bar y_2 \sim N[\mu_1 - \mu_2,\ \sigma^2(1/n_1 + 1/n_2)]$; si
  $\sigma$ fuera conocida y $H_0$ cierta,

$$Z_0 = \frac{\bar y_1 - \bar y_2}{\sigma\sqrt{\dfrac{1}{n_1} + \dfrac{1}{n_2}}} \sim N(0, 1) \qquad \text{(ec. 2-26)}$$

  y al sustituir $\sigma$ por $S_p$ la distribución pasa a ser $t_{n_1+n_2-2}$.

**Ejemplo del mortero de cemento portland** (págs. 35–36):

| | Mortero modificado | Mortero sin modificar |
|---|---|---|
| Media | $\bar y_1 = 16.76$ kgf/cm² | $\bar y_2 = 17.92$ kgf/cm² |
| Varianza | $S_1^2 = 0.100$ | $S_2^2 = 0.061$ |
| Desv. estándar | $S_1 = 0.316$ | $S_2 = 0.247$ |
| $n$ | 10 | 10 |

- $S_p^2 = [9(0.100) + 9(0.061)]/18 = 0.081$; $S_p = 0.284$.
- $t_0 = (16.76 - 17.92)/(0.284\sqrt{1/10 + 1/10}) = -9.13$.
- Con $\alpha = 0.05$: $t_{0.025,18} = 2.101$. Como $t_0 = -9.13 < -2.101$ se rechaza $H_0$: las
  fuerzas medias de las dos formulaciones difieren.

**Valores $P$.**

- Reportar solo "se rechazó con $\alpha = 0.05$" es pobre: no dice qué tan lejos cayó el
  estadístico dentro de la región crítica e impone un nivel de significación a los demás.
- **Valor $P$**: probabilidad de que el estadístico de prueba tome un valor al menos tan extremo
  como el observado cuando $H_0$ es verdadera; equivalentemente, el **menor nivel $\alpha$ con el
  que se rechazaría $H_0$** con esos datos.
- Aproximación con tablas (mortero): $t_{0.0005,18} = 3.922$ y $\lvert t_0 \rvert = 9.13 >
  3.922$, luego $P < 2(0.0005) = 0.001$ (dos colas). Valor exacto reportado: $P = 3.68 \times
  10^{-8}$.

**Solución por computadora (tabla 2-2, Minitab, mortero).**

| | N | Mean | StDev | SE Mean |
|---|---|---|---|---|
| Modified | 10 | 16.774 | 0.309 | 0.098 |
| Unmod | 10 | 17.922 | 0.248 | 0.078 |

- IC 95 % para $\mu_{\text{mod}} - \mu_{\text{unmod}}$: $(-1.411,\ -0.885)$.
- $T = -9.16$, $P = 0.0000$, $DF = 18$, *Pooled StDev* $= 0.280$.
- "SE Mean" = error estándar de la media, $s/\sqrt{n}$.
- El $t$ difiere ligeramente del cálculo manual ($-9.13$) por redondeo; $P = 0.0000$ es un valor
  "por omisión" (muchos paquetes no reportan valores $P$ menores que 0.0001).

**Verificación de los supuestos de la prueba $t$.**

Supuestos: (1) ambas muestras provienen de poblaciones independientes normales; (2) varianzas
iguales; (3) observaciones independientes. La independencia es el supuesto crítico y se
satisface normalmente si el orden de las corridas (y la asignación de unidades y materiales) se
aleatorizó. Igualdad de varianzas y normalidad se verifican con la **gráfica de probabilidad
normal**.

Construcción de la gráfica de probabilidad normal:

1. Ordenar la muestra de menor a mayor: $y_{(1)} \le y_{(2)} \le \dots \le y_{(n)}$.
2. Graficar cada $y_{(j)}$ contra su frecuencia acumulada observada $(j - 0.5)/n$, en escala de
   probabilidad normal (normalmente $100(j - 0.5)/n$ en el eje vertical; algunas gráficas usan
   $100[1 - (j - 0.5)/n]$ o convierten la frecuencia acumulada en un valor $z$ normalizado).
3. Trazar una recta guiándose por los puntos centrales, no por los extremos; regla empírica:
   pasarla aproximadamente por los cuartiles 25 y 75.
4. Juzgar la cercanía con la **prueba del "lápiz grueso"**: si un lápiz grueso colocado sobre la
   recta cubre todos los puntos, la normal describe adecuadamente los datos. La decisión es
   subjetiva.

Lecturas adicionales de la gráfica:

- Media ≈ percentil 50; desviación estándar ≈ diferencia entre los percentiles 84 y 50.
- **Igualdad de varianzas**: comparar las **pendientes** de las rectas de las dos muestras;
  pendientes similares ⇒ varianzas similares (fig. 2-11a y 2-11b del mortero: ambas muestras
  pasan la prueba y tienen pendientes muy similares). Una desigualdad clara de pendientes exige
  la prueba de la sección 2-4.4.

Efecto de las violaciones:

- Violaciones pequeñas a moderadas de los supuestos no son preocupantes; **no** ignorar
  *ninguna* falla de la independencia ni los indicios claros de no normalidad: afectan tanto el
  nivel de significación como la potencia.
- Remedios: **transformaciones** (cap. 3) o procedimientos **no paramétricos**.

**Justificación alternativa: prueba de aleatorización.** Si el diseño está aleatorizado, la
prueba se justifica sin supuesto alguno sobre la forma de la distribución: si los tratamientos
no tienen efecto, las $20!/(10!\,10!) = 184\,756$ formas de repartir las 20 observaciones en
dos grupos de 10 son igualmente probables; si el $t_0$ observado es inusualmente grande o
pequeño respecto del conjunto de los 184 756 valores posibles, es evidencia de $\mu_1 \ne
\mu_2$. La prueba $t$ es una buena aproximación de la prueba de aleatorización, por lo que no es
necesario preocuparse en exceso por la normalidad (y basta una verificación sencilla como la
gráfica de probabilidad normal).

### 2-4.2 Elección del tamaño de la muestra

- Sea $\delta = \mu_1 - \mu_2$ la diferencia verdadera. $\beta$ depende de $\delta$ y de $n$.
- **Curva de operación característica (curva OC)**: gráfica de $\beta$ contra $\delta$ para un
  tamaño de muestra dado.
- Fig. 2-12: curvas OC para la prueba $t$ de dos colas con $\alpha = 0.05$, varianzas
  desconocidas pero iguales y $n_1 = n_2 = n$. Eje vertical: probabilidad de aceptar $H_0$
  ($\beta$). Eje horizontal:

$$d = \frac{\lvert \mu_1 - \mu_2 \rvert}{2\sigma} = \frac{\lvert \delta \rvert}{2\sigma}$$

- Las curvas están indexadas por $n^* = 2n - 1$ (los rótulos "n" de la figura son $n^*$:
  2, 3, 4, 5, 7, 10, 15, 20, 30, 40, 50, 75, 100).
- Lectura de las curvas:
  1. A mayor diferencia $\mu_1 - \mu_2$, menor $\beta$ para $n$ y $\alpha$ dados (las diferencias
     grandes se detectan más fácilmente).
  2. A mayor tamaño de muestra, menor $\beta$ para $\delta$ y $\alpha$ dados (la potencia se
     aumenta incrementando $n$).
- **Procedimiento**: (1) fijar la diferencia crítica $\delta$ que se quiere detectar; (2) fijar
  un valor previo (conservador) de $\sigma$; (3) calcular $d$; (4) fijar $\beta$ deseado; (5)
  leer $n^*$ en la curva; (6) $n = (n^* + 1)/2$.
- Ejemplo (mortero): $\delta = 0.5$ kgf/cm², $\sigma \le 0.25$ por experiencia previa ⇒
  $d = 0.5/(2 \cdot 0.25) = 1$; con $\beta = 0.05$ (potencia 95 %) se lee $n^* \approx 16$ ⇒
  $n = (16 + 1)/2 = 8.5 \approx 9$ por muestra. El experimentador usó 10, quizá por si la
  estimación previa de $\sigma$ era demasiado conservadora.
- $d$ depende de $\sigma$, desconocida: hace falta una estimación previa.

### 2-4.3 Intervalos de confianza

- En muchos experimentos de ingeniería ya se sabe que las medias difieren, así que interesa más
  un intervalo de confianza para $\mu_1 - \mu_2$ que la prueba.
- Definición: estadísticos $L$ y $U$ tales que

$$P(L \le \theta \le U) = 1 - \alpha \qquad \text{(ec. 2-27)}$$

  $L \le \theta \le U$ (ec. 2-28) es un **intervalo de confianza de $100(1-\alpha)$ %** para
  $\theta$; $L$ y $U$ son los límites de confianza inferior y superior y $1 - \alpha$ el
  **coeficiente de confianza**.
- Interpretación frecuentista: en muestreos repetidos, el $100(1-\alpha)$ % de los intervalos
  así construidos contiene el valor verdadero; no se sabe si el de esta muestra lo contiene.
- IC para $\mu_1 - \mu_2$ con varianzas iguales (ec. 2-30), derivado de que
  $[\bar y_1 - \bar y_2 - (\mu_1 - \mu_2)]/[S_p\sqrt{1/n_1 + 1/n_2}] \sim t_{n_1+n_2-2}$:

$$\bar y_1 - \bar y_2 - t_{\alpha/2,\,n_1+n_2-2}\,S_p\sqrt{\frac{1}{n_1} + \frac{1}{n_2}} \;\le\; \mu_1 - \mu_2 \;\le\; \bar y_1 - \bar y_2 + t_{\alpha/2,\,n_1+n_2-2}\,S_p\sqrt{\frac{1}{n_1} + \frac{1}{n_2}}$$

- Mortero, 95 %: $-1.16 \pm (2.101)(0.284)\sqrt{1/10 + 1/10} = -1.16 \pm 0.27$, es decir
  $-1.43 \le \mu_1 - \mu_2 \le -0.89$ kgf/cm². Como el intervalo no incluye 0, los datos no
  apoyan $\mu_1 = \mu_2$ al 5 %; la formulación sin modificar tiene mayor fuerza media.
  (Minitab: $-1.411$ a $-0.885$.)

### 2-4.4 Caso en que $\sigma_1^2 \ne \sigma_2^2$

Para $H_0: \mu_1 = \mu_2$ sin base para suponer varianzas iguales:

$$t_0 = \frac{\bar y_1 - \bar y_2}{\sqrt{\dfrac{S_1^2}{n_1} + \dfrac{S_2^2}{n_2}}} \qquad \text{(ec. 2-31)}$$

No se distribuye exactamente como $t$, pero $t$ es buena aproximación con grados de libertad

$$v = \frac{\left(\dfrac{S_1^2}{n_1} + \dfrac{S_2^2}{n_2}\right)^2}{\dfrac{(S_1^2/n_1)^2}{n_1 - 1} + \dfrac{(S_2^2/n_2)^2}{n_2 - 1}} \qquad \text{(ec. 2-32)}$$

- Usar esta versión cuando la gráfica de probabilidad normal indique claramente varianzas
  desiguales.
- El libro deja como ejercicio el IC correspondiente (problema 2-24); por analogía con la
  ec. 2-30 sería $\bar y_1 - \bar y_2 \pm t_{\alpha/2,\,v}\sqrt{S_1^2/n_1 + S_2^2/n_2}$ (fórmula
  no escrita explícitamente en el texto).

### 2-4.5 Caso en que se conocen $\sigma_1^2$ y $\sigma_2^2$

$$Z_0 = \frac{\bar y_1 - \bar y_2}{\sqrt{\dfrac{\sigma_1^2}{n_1} + \dfrac{\sigma_2^2}{n_2}}} \qquad \text{(ec. 2-33)}$$

- Si ambas poblaciones son normales, o las muestras son suficientemente grandes para aplicar el
  teorema del límite central, $Z_0 \sim N(0,1)$ bajo $H_0$. Rechazar si $\lvert Z_0 \rvert >
  Z_{\alpha/2}$.
- A diferencia de la prueba $t$, **no** requiere muestreo de poblaciones normales.
- IC de $100(1-\alpha)$ %:

$$\bar y_1 - \bar y_2 - Z_{\alpha/2}\sqrt{\frac{\sigma_1^2}{n_1} + \frac{\sigma_2^2}{n_2}} \;\le\; \mu_1 - \mu_2 \;\le\; \bar y_1 - \bar y_2 + Z_{\alpha/2}\sqrt{\frac{\sigma_1^2}{n_1} + \frac{\sigma_2^2}{n_2}} \qquad \text{(ec. 2-34)}$$

### 2-4.6 Comparación de una sola media con un valor especificado

$$H_0: \mu = \mu_0 \qquad H_1: \mu \ne \mu_0$$

El valor $\mu_0$ suele venir de (1) evidencia, conocimiento o experimentación previos; (2) una
teoría o modelo de la situación; (3) especificaciones contractuales.

**Varianza conocida** (población normal, o $n$ grande para aplicar el TLC):

$$Z_0 = \frac{\bar y - \mu_0}{\sigma/\sqrt{n}} \qquad \text{(ec. 2-35)}$$

- Rechazar si $\lvert Z_0 \rvert > Z_{\alpha/2}$.
- IC: $\bar y - Z_{\alpha/2}\,\sigma/\sqrt{n} \le \mu \le \bar y + Z_{\alpha/2}\,\sigma/\sqrt{n}$
  (ec. 2-36).

**Varianza desconocida** (supuesto adicional de población normal, aunque las desviaciones
moderadas de la normalidad no afectan seriamente):

$$t_0 = \frac{\bar y - \mu_0}{S/\sqrt{n}} \qquad \text{(ec. 2-37)}$$

- Rechazar si $\lvert t_0 \rvert > t_{\alpha/2,\,n-1}$.
- IC: $\bar y - t_{\alpha/2,\,n-1}\,S/\sqrt{n} \le \mu \le \bar y + t_{\alpha/2,\,n-1}\,S/\sqrt{n}$
  (ec. 2-38).

**Ejemplo 2-1** (págs. 45–46). Lotes de tela; el fabricante acepta el lote solo si la
resistencia media a la ruptura excede 200 psi; varianza conocida $\sigma^2 = 100$ psi².
$H_0: \mu = 200$ contra $H_1: \mu > 200$ (una cola). Con $n = 4$ y $\bar y = 214$:
$Z_0 = (214 - 200)/(10/\sqrt{4}) = 2.80$. Con $\alpha = 0.05$, $Z_{0.05} = 1.645$; se rechaza
$H_0$ y se concluye que la resistencia media del lote excede 200 psi.

### 2-4.7 Resumen de las pruebas para medias

**Tabla 2-3. Pruebas para medias con varianza conocida**

| Hipótesis | Estadístico de prueba | Criterio de rechazo |
|---|---|---|
| $H_0: \mu = \mu_0$; $H_1: \mu \ne \mu_0$ | $Z_0 = \dfrac{\bar y - \mu_0}{\sigma/\sqrt{n}}$ | $\lvert Z_0 \rvert > Z_{\alpha/2}$ |
| $H_0: \mu = \mu_0$; $H_1: \mu < \mu_0$ | ídem | $Z_0 < -Z_\alpha$ |
| $H_0: \mu = \mu_0$; $H_1: \mu > \mu_0$ | ídem | $Z_0 > Z_\alpha$ |
| $H_0: \mu_1 = \mu_2$; $H_1: \mu_1 \ne \mu_2$ | $Z_0 = \dfrac{\bar y_1 - \bar y_2}{\sqrt{\sigma_1^2/n_1 + \sigma_2^2/n_2}}$ | $\lvert Z_0 \rvert > Z_{\alpha/2}$ |
| $H_0: \mu_1 = \mu_2$; $H_1: \mu_1 < \mu_2$ | ídem | $Z_0 < -Z_\alpha$ |
| $H_0: \mu_1 = \mu_2$; $H_1: \mu_1 > \mu_2$ | ídem | $Z_0 > Z_\alpha$ |

**Tabla 2-4. Pruebas para medias de distribuciones normales, varianza desconocida**

| Hipótesis | Estadístico de prueba | Criterio de rechazo |
|---|---|---|
| $H_0: \mu = \mu_0$; $H_1: \mu \ne \mu_0$ | $t_0 = \dfrac{\bar y - \mu_0}{S/\sqrt{n}}$ | $\lvert t_0 \rvert > t_{\alpha/2,\,n-1}$ |
| $H_0: \mu = \mu_0$; $H_1: \mu < \mu_0$ | ídem | $t_0 < -t_{\alpha,\,n-1}$ |
| $H_0: \mu = \mu_0$; $H_1: \mu > \mu_0$ | ídem | $t_0 > t_{\alpha,\,n-1}$ |
| $H_0: \mu_1 = \mu_2$; $H_1: \mu_1 \ne \mu_2$ | ver abajo según el caso | $\lvert t_0 \rvert > t_{\alpha/2,\,v}$ |
| $H_0: \mu_1 = \mu_2$; $H_1: \mu_1 < \mu_2$ | ídem | $t_0 < -t_{\alpha,\,v}$ |
| $H_0: \mu_1 = \mu_2$; $H_1: \mu_1 > \mu_2$ | ídem | $t_0 > t_{\alpha,\,v}$ |

Para dos medias:

- si $\sigma_1^2 = \sigma_2^2$: $t_0 = \dfrac{\bar y_1 - \bar y_2}{S_p\sqrt{1/n_1 + 1/n_2}}$ con
  $v = n_1 + n_2 - 2$;
- si $\sigma_1^2 \ne \sigma_2^2$: $t_0 = \dfrac{\bar y_1 - \bar y_2}{\sqrt{S_1^2/n_1 + S_2^2/n_2}}$
  con $v$ de la ec. 2-32.

(Nota: en la tabla 2-3 impresa la cuarta fila dice "$H_1: \mu_2 \ne \mu_2$"; es una errata por
$\mu_1 \ne \mu_2$.)

---

## 2-5 Inferencias acerca de las diferencias en las medias, diseños de comparaciones pareadas

### 2-5.1 El problema de las comparaciones pareadas

**Cuándo se usa.** Cuando las unidades experimentales son heterogéneas y cada unidad puede
recibir ambos tratamientos. Ejemplo: máquina de dureza con dos puntas distintas; se sospecha
que una produce lecturas diferentes de la otra.

- Diseño completamente aleatorizado posible: 20 ejemplares de metal, 10 asignados al azar a
  cada punta, prueba $t$ de dos muestras. **Desventaja**: si los ejemplares provienen de barras
  o temperaturas de fabricación distintas, su falta de homogeneidad infla el error experimental
  y dificulta detectar una diferencia real entre las puntas.
- **Diseño pareado**: cada ejemplar se divide en dos secciones; se asigna al azar una punta a
  cada mitad, y el orden en que se prueban las puntas en cada ejemplar también se elige al azar.
  Se corrió con 10 ejemplares (tabla 2-5, datos codificados).

**Modelo estadístico** (ec. 2-39):

$$y_{ij} = \mu_i + \beta_j + \varepsilon_{ij}, \qquad i = 1, 2; \quad j = 1, 2, \dots, 10$$

- $y_{ij}$: dureza con la punta $i$ en el ejemplar $j$; $\mu_i$: dureza media verdadera de la
  punta $i$; $\beta_j$: efecto del ejemplar $j$ (bloque); $\varepsilon_{ij}$: error aleatorio
  con media 0 y varianza $\sigma_i^2$.

**Análisis.** Diferencias pareadas (ec. 2-40):

$$d_j = y_{1j} - y_{2j}, \qquad j = 1, \dots, n$$

$$\mu_d = E(d_j) = \mu_1 + \beta_j - (\mu_2 + \beta_j) = \mu_1 - \mu_2$$

El efecto aditivo $\beta_j$ del ejemplar **se cancela**. Probar $H_0: \mu_1 = \mu_2$ equivale a

$$H_0: \mu_d = 0 \qquad H_1: \mu_d \ne 0$$

$$t_0 = \frac{\bar d}{S_d/\sqrt{n}} \qquad \text{(ec. 2-41)}$$

$$\bar d = \frac{1}{n}\sum_{j=1}^{n} d_j \qquad \text{(ec. 2-42)}$$

$$S_d = \left[\frac{\sum_{j=1}^{n} (d_j - \bar d)^2}{n - 1}\right]^{1/2} = \left[\frac{\sum_{j=1}^{n} d_j^2 - \frac{1}{n}\left(\sum_{j=1}^{n} d_j\right)^2}{n - 1}\right]^{1/2} \qquad \text{(ec. 2-43)}$$

- Rechazar $H_0$ si $\lvert t_0 \rvert > t_{\alpha/2,\,n-1}$. Es la **prueba $t$ pareada**.
- IC de $100(1-\alpha)$ % para $\mu_1 - \mu_2$: $\bar d \pm t_{\alpha/2,\,n-1}\,S_d/\sqrt{n}$.

**Ejemplo de la dureza** (tabla 2-5, págs. 48–51).

| Ejemplar | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| Punta 1 | 7 | 3 | 3 | 4 | 8 | 3 | 2 | 9 | 5 | 4 |
| Punta 2 | 6 | 3 | 5 | 3 | 8 | 2 | 4 | 9 | 4 | 5 |
| $d_j$ | 1 | 0 | −2 | 1 | 0 | 1 | −2 | 0 | 1 | −1 |

- $\sum d_j = -1$, $\sum d_j^2 = 13$; $\bar d = -0.10$;
  $S_d = \{[13 - \tfrac{1}{10}(-1)^2]/9\}^{1/2} = 1.20$.
- $t_0 = -0.10/(1.20/\sqrt{10}) = -0.26$; $t_{0.025,9} = 2.262$. Como $\lvert t_0 \rvert = 0.26
  < 2.262$ **no se rechaza** $H_0$: no hay evidencia de que las dos puntas produzcan lecturas de
  dureza diferentes.
- Minitab (tabla 2-6): Tip 1: media 4.800, StDev 2.394, SE 0.757; Tip 2: media 4.900, StDev
  2.234, SE 0.706; Difference: media −0.100, StDev 1.197, SE 0.379. IC 95 % de la diferencia
  media: $(-0.956,\ 0.756)$; $T = -0.26$, $P = 0.798$ (≈ 0.80; no se rechaza con ningún nivel de
  significación razonable).

### 2-5.2 Ventajas del diseño de comparaciones pareadas

- El **diseño de comparaciones pareadas** ilustra el principio de formación de bloques
  (sección 1-3) y es un caso especial del **diseño de bloques aleatorizados** (cap. 4). El
  **bloque** es una unidad experimental relativamente homogénea (aquí, cada ejemplar de metal) y
  representa una **restricción sobre la aleatorización completa**: los tratamientos solo se
  aleatorizan dentro del bloque.
- **Costo en grados de libertad**: con $2n = 20$ observaciones, el estadístico $t$ pareado tiene
  solo $n - 1 = 9$ grados de libertad (frente a $2n - 2 = 18$ del análisis independiente): se
  "pierden" $n - 1$. A más grados de libertad, más sensible la prueba.
- **Ganancia**: se elimina una fuente adicional de variabilidad (la diferencia entre
  ejemplares). Indicador: comparar $S_d$ con el $S_p$ que resultaría de tratar los mismos datos
  como dos muestras independientes. En el ejemplo $S_p = 2.32$ frente a $S_d = 1.20$: el pareo
  redujo la estimación de la variabilidad en cerca de 50 %.
- En términos de IC de 95 % para $\mu_1 - \mu_2$:

| Análisis | Fórmula | Resultado |
|---|---|---|
| Pareado | $\bar d \pm t_{0.025,9}\,S_d/\sqrt{n} = -0.10 \pm (2.262)(1.20)/\sqrt{10}$ | $-0.10 \pm 0.86$ |
| Independiente (combinado) | $\bar y_1 - \bar y_2 \pm t_{0.025,18}\,S_p\sqrt{1/n_1 + 1/n_2} = 4.80 - 4.90 \pm (2.101)(2.32)\sqrt{1/10 + 1/10}$ | $-0.10 \pm 2.18$ |

  El intervalo pareado es sensiblemente más angosto: propiedad de **reducción del ruido** de la
  formación de bloques.
- **Advertencia**: formar bloques no siempre es la mejor estrategia. Si la variabilidad dentro
  de los bloques es igual a la variabilidad entre bloques, la varianza de $\bar y_1 - \bar y_2$
  es la misma con cualquier diseño, y bloquear solo hace perder $n - 1$ grados de libertad, lo
  que produce un IC más ancho.

---

## 2-6 Inferencias acerca de las varianzas de distribuciones normales

**Cuándo se usa.** Cuando lo que interesa comparar es la variabilidad (p. ej. variabilidad de un
equipo de llenado, o de dos métodos de análisis químico).

**Advertencia central**: a diferencia de las pruebas para medias, las pruebas para varianzas son
**bastante más sensibles al supuesto de normalidad**.

### Una varianza contra un valor especificado

$$H_0: \sigma^2 = \sigma_0^2 \qquad H_1: \sigma^2 \ne \sigma_0^2 \qquad \text{(ec. 2-44)}$$

$$\chi_0^2 = \frac{SS}{\sigma_0^2} = \frac{(n-1)S^2}{\sigma_0^2} \qquad \text{(ec. 2-45)}$$

- $SS = \sum_{i=1}^{n} (y_i - \bar y)^2$; distribución de referencia $\chi^2_{n-1}$.
- Rechazar $H_0$ si $\chi_0^2 > \chi^2_{\alpha/2,\,n-1}$ o si $\chi_0^2 <
  \chi^2_{1-(\alpha/2),\,n-1}$ (puntos porcentuales $\alpha/2$ superior e inferior).
- IC de $100(1-\alpha)$ % para $\sigma^2$:

$$\frac{(n-1)S^2}{\chi^2_{\alpha/2,\,n-1}} \;\le\; \sigma^2 \;\le\; \frac{(n-1)S^2}{\chi^2_{1-(\alpha/2),\,n-1}} \qquad \text{(ec. 2-46)}$$

### Igualdad de dos varianzas

$$H_0: \sigma_1^2 = \sigma_2^2 \qquad H_1: \sigma_1^2 \ne \sigma_2^2 \qquad \text{(ec. 2-47)}$$

$$F_0 = \frac{S_1^2}{S_2^2} \qquad \text{(ec. 2-48)}$$

- Muestras aleatorias independientes de tamaños $n_1$ y $n_2$ de dos poblaciones normales.
- Distribución de referencia: $F$ con $n_1 - 1$ g. l. en el numerador y $n_2 - 1$ en el
  denominador.
- Rechazar $H_0$ si $F_0 > F_{\alpha/2,\,n_1-1,\,n_2-1}$ o si $F_0 <
  F_{1-(\alpha/2),\,n_1-1,\,n_2-1}$.
- La tabla IV solo trae la cola superior; la cola inferior se obtiene con

$$F_{1-\alpha,\,v_1,\,v_2} = \frac{1}{F_{\alpha,\,v_2,\,v_1}} \qquad \text{(ec. 2-49)}$$

- IC de $100(1-\alpha)$ % para el cociente $\sigma_1^2/\sigma_2^2$:

$$\frac{S_1^2}{S_2^2}\,F_{1-\alpha/2,\,n_2-1,\,n_1-1} \;\le\; \frac{\sigma_1^2}{\sigma_2^2} \;\le\; \frac{S_1^2}{S_2^2}\,F_{\alpha/2,\,n_2-1,\,n_1-1} \qquad \text{(ec. 2-50)}$$

  (obsérvese el orden de los grados de libertad: $n_2 - 1$ primero).

**Tabla 2-7. Pruebas para las varianzas de distribuciones normales**

| Hipótesis | Estadístico de prueba | Criterio de rechazo |
|---|---|---|
| $H_0: \sigma^2 = \sigma_0^2$; $H_1: \sigma^2 \ne \sigma_0^2$ | $\chi_0^2 = \dfrac{(n-1)S^2}{\sigma_0^2}$ | $\chi_0^2 > \chi^2_{\alpha/2,\,n-1}$ o $\chi_0^2 < \chi^2_{1-\alpha/2,\,n-1}$ |
| $H_0: \sigma^2 = \sigma_0^2$; $H_1: \sigma^2 < \sigma_0^2$ | ídem | $\chi_0^2 < \chi^2_{1-\alpha,\,n-1}$ |
| $H_0: \sigma^2 = \sigma_0^2$; $H_1: \sigma^2 > \sigma_0^2$ | ídem | $\chi_0^2 > \chi^2_{\alpha,\,n-1}$ |
| $H_0: \sigma_1^2 = \sigma_2^2$; $H_1: \sigma_1^2 \ne \sigma_2^2$ | $F_0 = \dfrac{S_1^2}{S_2^2}$ | $F_0 > F_{\alpha/2,\,n_1-1,\,n_2-1}$ o $F_0 < F_{1-\alpha/2,\,n_1-1,\,n_2-1}$ |
| $H_0: \sigma_1^2 = \sigma_2^2$; $H_1: \sigma_1^2 < \sigma_2^2$ | $F_0 = \dfrac{S_2^2}{S_1^2}$ | $F_0 > F_{\alpha,\,n_2-1,\,n_1-1}$ |
| $H_0: \sigma_1^2 = \sigma_2^2$; $H_1: \sigma_1^2 > \sigma_2^2$ | $F_0 = \dfrac{S_1^2}{S_2^2}$ | $F_0 > F_{\alpha,\,n_1-1,\,n_2-1}$ |

En las pruebas de una cola para dos varianzas, la varianza muestral que la alternativa supone
mayor va en el numerador y siempre se rechaza en la cola superior.

Las pruebas para más de dos varianzas se tratan en la sección 3-4.3 del capítulo 3.

**Ejemplo 2-2** (págs. 53–54). Variabilidad de dos tipos de equipo de prueba; se sospecha que el
equipo antiguo (tipo 1) tiene mayor varianza. $H_0: \sigma_1^2 = \sigma_2^2$ contra
$H_1: \sigma_1^2 > \sigma_2^2$. Con $n_1 = 12$, $n_2 = 10$, $S_1^2 = 14.5$, $S_2^2 = 10.8$:
$F_0 = 14.5/10.8 = 1.34$. Valor crítico $F_{0.05,11,9} = 3.10$; **no se rechaza** $H_0$
(evidencia insuficiente de que la varianza del equipo antiguo sea mayor).
IC de 95 % para $\sigma_1^2/\sigma_2^2$ (ec. 2-50) con $F_{0.025,9,11} = 3.59$ y
$F_{0.975,9,11} = 1/F_{0.025,11,9} = 1/3.92 = 0.255$:

$$\frac{14.5}{10.8}(0.255) \le \frac{\sigma_1^2}{\sigma_2^2} \le \frac{14.5}{10.8}(3.59) \quad\Longrightarrow\quad 0.34 \le \frac{\sigma_1^2}{\sigma_2^2} \le 4.81$$

---

## Resumen de intervalos de confianza de $100(1-\alpha)$ %

| Parámetro | Condiciones | Intervalo | Ec. |
|---|---|---|---|
| $\mu$ | $\sigma$ conocida | $\bar y \pm Z_{\alpha/2}\,\sigma/\sqrt{n}$ | 2-36 |
| $\mu$ | $\sigma$ desconocida, normal | $\bar y \pm t_{\alpha/2,\,n-1}\,S/\sqrt{n}$ | 2-38 |
| $\mu_1 - \mu_2$ | varianzas conocidas | $\bar y_1 - \bar y_2 \pm Z_{\alpha/2}\sqrt{\sigma_1^2/n_1 + \sigma_2^2/n_2}$ | 2-34 |
| $\mu_1 - \mu_2$ | varianzas desconocidas iguales | $\bar y_1 - \bar y_2 \pm t_{\alpha/2,\,n_1+n_2-2}\,S_p\sqrt{1/n_1 + 1/n_2}$ | 2-30 |
| $\mu_1 - \mu_2$ | datos pareados | $\bar d \pm t_{\alpha/2,\,n-1}\,S_d/\sqrt{n}$ | pág. 51 |
| $\sigma^2$ | normal | $\left[\dfrac{(n-1)S^2}{\chi^2_{\alpha/2,\,n-1}},\ \dfrac{(n-1)S^2}{\chi^2_{1-\alpha/2,\,n-1}}\right]$ | 2-46 |
| $\sigma_1^2/\sigma_2^2$ | normales independientes | $\left[\dfrac{S_1^2}{S_2^2}F_{1-\alpha/2,\,n_2-1,\,n_1-1},\ \dfrac{S_1^2}{S_2^2}F_{\alpha/2,\,n_2-1,\,n_1-1}\right]$ | 2-50 |

## Reglas prácticas y advertencias del capítulo

1. Empezar siempre con gráficas simples (diagrama de puntos, histograma, diagramas de caja)
   antes de las pruebas formales.
2. Reportar el **valor $P$**, no solo "rechazo/no rechazo" con un $\alpha$ fijo.
3. Complementar la prueba con el **intervalo de confianza**: da magnitud y precisión de la
   diferencia.
4. La **independencia** es el supuesto crítico de la prueba $t$ y se protege aleatorizando el
   orden de las corridas y la asignación del material. Las desviaciones moderadas de la
   normalidad importan poco para medias (la prueba $t$ aproxima la prueba de aleatorización),
   pero mucho para las pruebas de varianzas ($\chi^2$ y $F$).
5. Verificar normalidad e igualdad de varianzas con gráficas de probabilidad normal (recta por
   los cuartiles 25 y 75, prueba del lápiz grueso, comparación de pendientes).
6. Si las varianzas difieren claramente, usar la prueba de la sección 2-4.4 (ecs. 2-31 y 2-32).
7. Elegir el tamaño de muestra con curvas OC a partir de la diferencia $\delta$ que importa
   detectar, de una estimación previa de $\sigma$ y de la potencia deseada.
8. Parear (bloquear) cuando las unidades experimentales son heterogéneas; no hacerlo cuando la
   variabilidad dentro de los bloques es igual a la variabilidad entre bloques, porque solo se
   pierden grados de libertad.

## 2-7 Problemas (solo ubicación)

Problemas 2-1 a 2-25 (págs. 54–59). Temas: pruebas $Z$ y $t$ de una media (2-1 a 2-8), dos
medias con varianzas conocidas (2-9, 2-10), dos medias y dos varianzas (2-11 a 2-13, 2-17 a
2-19), una varianza (2-14), prueba $t$ pareada (2-15, 2-16), desarrollos teóricos (2-20 a 2-25:
estadístico para $H_0: 2\mu_1 = \mu_2$, asignación óptima de $N$ observaciones, deducción de las
ecs. 2-46 y 2-50, IC con varianzas desiguales, datos donde la $t$ pareada es grande y la
combinada pequeña).
