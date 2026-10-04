# Capítulo 14 — Otros tópicos de diseño y análisis

> Montgomery, págs. 590–629

> **Nota sobre el escaneo:** las págs. 628–629 (final de la sección de problemas) no están en
> el PDF (de la 627 se salta a la bibliografía, pág. 632). Todo el contenido teórico
> (págs. 590–626) se leyó completo.

Temas: transformaciones y respuestas no normales (Box-Cox, modelo lineal generalizado), datos
no balanceados en factoriales, análisis de covarianza y mediciones repetidas.

---

## 14-1 Respuestas y transformaciones no normales

### 14-1.1 Selección de una transformación: método de Box-Cox

**Para qué sirve una transformación** (tres propósitos): estabilizar la varianza, acercar la
respuesta a la normalidad y mejorar el ajuste del modelo (p. ej. eliminar interacciones). A
veces se logran varios a la vez. Casos típicos: conteos, proporciones, respuestas sesgadas a
la derecha.

**Familia de potencias:** $y^*=y^\lambda$. Box y Cox estiman $\lambda$ por máxima
verosimilitud junto con los demás parámetros del modelo.

**Transformación normalizada (ec. 14-1):**

$$y^{(\lambda)}=\begin{cases}\dfrac{y^\lambda-1}{\lambda\,\dot y^{\lambda-1}}, & \lambda\neq0\\[2mm]
\dot y\,\ln y, & \lambda=0\end{cases}
\qquad \dot y=\ln^{-1}\!\left[\frac1n\sum\ln y\right]\ \text{(media geométrica)}$$

**Procedimiento:**

1. Elegir una rejilla de valores de $\lambda$ (10 a 20 suelen bastar).
2. Para cada $\lambda$, calcular $y^{(\lambda)}$ y hacer el ANOVA estándar del modelo; anotar
   $SS_E(\lambda)$.
3. Graficar $SS_E(\lambda)$ contra $\lambda$; el estimador de máxima verosimilitud es el
   $\lambda$ que **minimiza** $SS_E(\lambda)$. Refinar la rejilla si se requiere más precisión.
4. Elegir un valor "simple" cercano al óptimo ($\lambda=0.5$ en vez de 0.58): la diferencia
   práctica es mínima y la interpretación mucho más fácil. $\lambda\approx1$ ⇒ no hace falta
   transformar.
5. Analizar los datos con $y^\lambda$ (o $\ln y$ si $\lambda=0$). También es válido usar
   $y^{(\lambda)}$; solo cambian escala y origen de los parámetros.

**Por qué no comparar directamente los $SS_E$ de $y^\lambda$:** cada $\lambda$ mide el error en
una escala distinta. El divisor $\dot y^{\lambda-1}$ reescala para hacer comparables los
$SS_E$; el término $(y^\lambda-1)/\lambda$ evita la degeneración en $\lambda=0$ (su límite es
$\ln y$).

**Intervalo de confianza aproximado $100(1-\alpha)\%$ para $\lambda$ (ec. 14-2):**

$$SS^*=SS_E(\lambda)\left(1+\frac{t^2_{\alpha/2,\nu}}{\nu}\right)$$

con $SS_E(\lambda)$ el mínimo y $\nu$ los gl del error. Se traza la horizontal a la altura
$SS^*$ sobre la gráfica; los cortes con la curva son los límites $\lambda^-$ y $\lambda^+$.
**Si el intervalo contiene $\lambda=1$, los datos no respaldan la necesidad de transformar.**

**Ejemplo 14-1 — Descarga pico (datos del ej. 3-5, un factor):**

| $\lambda$ | −1.00 | −0.50 | −0.25 | 0.00 | 0.25 | 0.50 | 0.75 | 1.00 | 1.25 | 1.50 |
|---|---|---|---|---|---|---|---|---|---|---|
| $SS_E(\lambda)$ | 7922.11 | 687.10 | 232.52 | 91.96 | 46.99 | 35.42 | 40.61 | 62.08 | 109.82 | 208.12 |

Mínimo en $\lambda\approx0.52$ con $SS_E\approx35.00$. IC 95 %:
$SS^*=35.00\,[1+(2.086)^2/20]=42.61$ ($t_{0.025,20}=2.086$) → $\lambda^-=0.27$,
$\lambda^+=0.77$. No contiene 1 → se justifica transformar; se usa raíz cuadrada
($\lambda=0.5$). Design-Expert (fig. 14-2, eje vertical $\ln SS_E$): mejor $\lambda=0.541377$,
IC (0.291092, 0.791862), recomienda raíz cuadrada.

### 14-1.2 Modelo lineal generalizado (GLM)

**Problemas de transformar:** (1) incomodidad de trabajar en la escala transformada; (2) más
grave: predicciones sin sentido en parte de la región (p. ej. raíz cuadrada predicha negativa
de un conteo, justo donde los conteos son bajos); (3) una sola transformación no garantiza
lograr a la vez varianza constante, normalidad y modelo simple.

**Alternativa:** el modelo lineal generalizado (Nelder y Wedderburn; McCullagh y Nelder; Myers
y Montgomery), que unifica modelos lineales y no lineales con respuestas normales y no
normales.

**Componentes:**

1. **Distribución de la respuesta**: cualquier miembro de la **familia exponencial** (normal,
   Poisson, binomial, exponencial, gamma).
2. **Predictor lineal**: $\mathbf{x}'\boldsymbol\beta=\beta_0+\beta_1x_1+\dots+\beta_kx_k$
   (ecs. 14-3, 14-4: el modelo normal $y=\mathbf{x}'\boldsymbol\beta+\varepsilon$ es un caso
   particular).
3. **Función de enlace** $g$ (monótona y diferenciable) entre la media y el predictor:

$$g(\mu)=\mathbf{x}'\boldsymbol\beta\ \ (14\text{-}5),\qquad
E(y)=\mu=g^{-1}(\mathbf{x}'\boldsymbol\beta)\ \ (14\text{-}6)$$

| Enlace | Definición | Modelo para la media | Uso típico |
|---|---|---|---|
| Identidad | $\mu=\mathbf{x}'\boldsymbol\beta$ | $\mu=\mathbf{x}'\boldsymbol\beta$ | respuesta normal (regresión ordinaria) |
| Log (ec. 14-7) | $\ln\mu=\mathbf{x}'\boldsymbol\beta$ | $\mu=e^{\mathbf{x}'\boldsymbol\beta}$ (14-8) | conteos (Poisson); continuas con cola derecha (exponencial, gamma) |
| Logit (ec. 14-9) | $\ln\dfrac{\mu}{1-\mu}=\mathbf{x}'\boldsymbol\beta$ | $\mu=\dfrac{1}{1+e^{-\mathbf{x}'\boldsymbol\beta}}$ (14-10) | binomial (regresión logística) |

(En la ec. 14-10 el libro imprime el exponente sin signo menos visible,
$1/(1+e^{\mathbf{x}'\boldsymbol\beta})$; la inversa correcta del logit 14-9 es la escrita en
la tabla.)

- La varianza de la respuesta **no tiene que ser constante**: puede ser función de la media
  (Poisson: varianza = media).
- **Estimación:** máxima verosimilitud; para la familia exponencial equivale a **mínimos
  cuadrados ponderados iterativos**; con respuesta normal y enlace identidad se reduce a
  mínimos cuadrados ordinarios.
- **Inferencia y diagnósticos:** análogos al ANOVA de la teoría normal. El libro no desarrolla
  la devianza ni sus pruebas en este capítulo; remite a Myers y Montgomery y al material
  suplementario. Software citado: SAS PROC GENMOD, S-PLUS.
- Para usarlo hay que **especificar distribución y enlace**.

**Ejemplo 14-2 — Defectos en rejillas (problema 8-29; conteos, 16 corridas):**
- Mínimos cuadrados con raíz cuadrada modificada de Freeman-Tukey (Bisgaard y Fuller):
  $(\sqrt{y}+\sqrt{y+1})/2=2.513-0.996x_4-1.21x_6-0.772x_2x_7$. Dos valores predichos
  negativos (−0.47 en las corridas 10 y 16) y límites inferiores negativos → no se pueden
  destransformar todas las entradas.
- GLM Poisson con enlace log y el mismo predictor (Myers y Montgomery):
  $\hat y=\exp(1.128-0.896x_4-1.176x_6-0.737x_2x_7)$. Sin predicciones ni límites negativos.
- Tabla 14-1: las longitudes de los IC del 95 % para la media son **uniformemente menores con
  el GLM** (p. ej. obs. 1: 29.76 vs. 19.45; obs. 3: 6.09 vs. 1.47; obs. 12: 18.96 vs. 7.35).
- Matiz del autor: no es una crítica al análisis original, cuyo objetivo era cribado, no
  predicción.

**Ejemplo 14-3 — Hilado de estambre (Box y Draper; $3^3$, 27 corridas; ciclos hasta falla):**
- Mínimos cuadrados con transformación log (base 10):
  $\log\hat y=2.751+0.3617x_1-0.2739x_2-0.1711x_3$.
- GLM gamma con enlace log, mismo predictor:
  $\hat y=\exp(6.3489+0.8425x_1-0.6313x_2-0.3851x_3)$.
- Tabla 14-3: predicciones similares (obs. 1: 682.50 vs. 680.52; obs. 19: 3609.11 vs.
  3670.00), pero los IC del GLM son más cortos en todos los puntos (obs. 1: 237.67 vs. 209.39;
  obs. 19: 1257.81 vs. 1089.00) → posible mejor predictor.

---

## 14-2 Datos no balanceados en un diseño factorial

**Origen:** pérdida de observaciones en un diseño balanceado, o desbalance deliberado (celdas
costosas con menos corridas; celdas de más interés con más réplicas).

**Problema:** se pierde la **ortogonalidad** de efectos principales e interacciones; el ANOVA
usual ya no aplica.

Notación (dos factores, efectos fijos): $n_{ij}$ observaciones en la celda $ij$;
$n_{i.}=\sum_j n_{ij}$, $n_{.j}=\sum_i n_{ij}$, $n_{..}=\sum_i\sum_j n_{ij}$.

### 14-2.1 Datos proporcionales

Condición (ec. 14-11):

$$n_{ij}=\frac{n_{i.}\,n_{.j}}{n_{..}}$$

(los tamaños en dos filas o columnas cualesquiera son proporcionales). En este caso **vale el
ANOVA estándar** con fórmulas ligeramente modificadas:

$$SS_T=\sum_i\sum_j\sum_{k=1}^{n_{ij}}y_{ijk}^2-\frac{y_{...}^2}{n_{..}},\qquad
SS_A=\sum_i\frac{y_{i..}^2}{n_{i.}}-\frac{y_{...}^2}{n_{..}},\qquad
SS_B=\sum_j\frac{y_{.j.}^2}{n_{.j}}-\frac{y_{...}^2}{n_{..}}$$

$$SS_{AB}=\sum_i\sum_j\frac{y_{ij.}^2}{n_{ij}}-\frac{y_{...}^2}{n_{..}}-SS_A-SS_B,\qquad
SS_E=\sum_i\sum_j\sum_k y_{ijk}^2-\sum_i\sum_j\frac{y_{ij.}^2}{n_{ij}}$$

**Ejemplo (tabla 14-4/14-5, batería del ej. 5-1 modificada):** $n_{ij}$ = (4,4,2; 2,2,1;
2,2,1), $n_{..}=20$, $y_{...}=2160$; p. ej. $n_{11}=10(8)/20=4$.

| Fuente | SS | gl | MS | $F_0$ |
|---|---|---|---|---|
| Tipo de material | 8 170.400 | 2 | 4 085.20 | 5.00 |
| Temperatura | 16 090.875 | 2 | 8 045.44 | 9.85 |
| Interacción | 5 907.725 | 4 | 1 476.93 | 1.18 |
| Error | 8 981.000 | 11 | 816.45 | |
| Total | 39 150.000 | 19 | | |

Material y temperatura significativos (coincide con el ej. 5-1 completo), pero la interacción
ya no se detecta.

### 14-2.2 Métodos aproximados

Aplicables cuando el desbalance es leve; convierten el problema en uno balanceado. Se supone
$n_{ij}\ge1$ en todas las celdas. El analista decide cuándo la aproximación es tolerable.

**a) Estimación de observaciones faltantes.** Si solo unas pocas $n_{ij}$ difieren: en un
modelo con interacción, el valor que minimiza $SS_E$ es **el promedio de la celda**,
$\bar y_{ij.}$. Se trata como dato real y **se restan de los gl del error tantos gl como
valores estimados** (tabla 14-6: una celda con 3 en vez de 4 → 26 gl en vez de 27).

**b) Apartado de datos.** Si una celda tiene *más* observaciones que las demás (tabla 14-7:
una celda con 5, el resto 4), estimar valores en las otras ocho celdas equivaldría a inventar
~18 % de los datos; mejor **apartar al azar** una observación de la celda grande para quedar
balanceado con $n=4$. Conviene repetir el análisis apartando otra observación; si las
conclusiones cambian, se sospecha de un atípico.

**c) Método de las medias no ponderadas (Yates).** Se hace un ANOVA balanceado estándar sobre
los **promedios de celda** (para filas, columnas e interacción) y el error se obtiene de las
observaciones individuales:

$$MS_E=\frac{\sum_i\sum_j\sum_k(y_{ijk}-\bar y_{ij.})^2}{n_{..}-ab}\qquad\text{(ec. 14-12)}$$

Como $V(\bar y_{ij.})=\sigma^2/n_{ij}$, la varianza promedio de las medias de celda es

$$\bar V(\bar y_{ij.})=\frac{\sigma^2}{ab}\sum_i\sum_j\frac1{n_{ij}}\qquad\text{(ec. 14-13)}$$

y el cuadrado medio del error a usar en el ANOVA de las medias es

$$MS_E'=\frac{MS_E}{ab}\sum_i\sum_j\frac{1}{n_{ij}}\qquad\text{(ec. 14-14)}$$

con $n_{..}-ab$ gl. Es aproximado porque las SS de filas, columnas e interacción no son
ji-cuadradas; ventaja: sencillez. Funciona razonablemente si las $n_{ij}$ no difieren mucho.

**d) Cuadrados ponderados de las medias (Yates).** También usa las medias de celda, pero
pondera los términos en proporción inversa a sus varianzas (ver Searle; Speed, Hocking y
Hackney).

### 14-2.3 Método exacto

Necesario con **celdas vacías** ($n_{ij}=0$) o desbalance fuerte. Se representa el ANOVA como
**modelo de regresión**, se ajusta y se usa la **prueba general de significación de la
regresión** (sumas de cuadrados extra). Advertencias: hay varias formas de hacerlo que dan
sumas de cuadrados distintas; las hipótesis probadas no siempre son análogas a las del caso
balanceado ni fáciles de interpretar. Software recomendado: SAS PROC GLM. Referencias: Searle;
Speed y Hocking; Hocking y Speed; Milliken y Johnson; material suplementario.

---

## 14-3 Análisis de covarianza (ANCOVA)

### Cuándo se usa

Existe una variable $x$ (**covariable** o variable concomitante) relacionada linealmente con
la respuesta $y$, que **no puede controlarse** pero sí medirse junto con $y$. El ANCOVA ajusta
$y$ por el efecto de $x$; sin ese ajuste, $x$ infla $MS_E$ y oculta diferencias reales entre
tratamientos. Es el análogo de la formación de bloques para factores perturbadores **no
controlables**; combina ANOVA y regresión.

### 14-3.1 Descripción del procedimiento (un factor, una covariable)

**Modelo (ec. 14-15):**

$$y_{ij}=\mu+\tau_i+\beta(x_{ij}-\bar x_{..})+\varepsilon_{ij},\qquad i=1..a,\ j=1..n$$

Forma equivalente (ec. 14-16): $y_{ij}=\mu'+\tau_i+\beta x_{ij}+\varepsilon_{ij}$, con
$\mu'=\mu-\beta\bar x_{..}$ (centrar en $\bar x_{..}$ conserva $\mu$ como media global; el
texto impreso dice "$\mu'+\beta\bar x_{..}$" al describir la relación).

**Supuestos:**
1. $\varepsilon_{ij}\sim NID(0,\sigma^2)$.
2. $\beta\neq0$ y la relación $y$–$x$ es **lineal**.
3. **Pendientes iguales** en todos los tratamientos (un solo $\beta$).
4. $\sum_i\tau_i=0$.
5. **La covariable no es afectada por los tratamientos.**

**Sumas de cuadrados y productos cruzados (ecs. 14-17 a 14-25):**

$$S_{yy}=\sum_i\sum_j y_{ij}^2-\frac{y_{..}^2}{an},\quad
S_{xx}=\sum_i\sum_j x_{ij}^2-\frac{x_{..}^2}{an},\quad
S_{xy}=\sum_i\sum_j x_{ij}y_{ij}-\frac{x_{..}y_{..}}{an}$$

$$T_{yy}=\frac1n\sum_i y_{i.}^2-\frac{y_{..}^2}{an},\quad
T_{xx}=\frac1n\sum_i x_{i.}^2-\frac{x_{..}^2}{an},\quad
T_{xy}=\frac1n\sum_i x_{i.}y_{i.}-\frac{x_{..}y_{..}}{an}$$

$$E_{yy}=S_{yy}-T_{yy},\qquad E_{xx}=S_{xx}-T_{xx},\qquad E_{xy}=S_{xy}-T_{xy}$$

($S$ = total, $T$ = tratamientos, $E$ = error; $S=T+E$. Las de productos cruzados pueden ser
negativas.)

**Estimadores de mínimos cuadrados:**

$$\hat\mu=\bar y_{..},\qquad \hat\tau_i=\bar y_{i.}-\bar y_{..}-\hat\beta(\bar x_{i.}-\bar x_{..}),\qquad
\hat\beta=\frac{E_{xy}}{E_{xx}}\quad(14\text{-}26)$$

**Error del modelo completo (ec. 14-27):**

$$SS_E=E_{yy}-\frac{E_{xy}^2}{E_{xx}},\qquad \text{gl}=a(n-1)-1,\qquad MS_E=\frac{SS_E}{a(n-1)-1}$$

**Modelo reducido sin tratamientos (ecs. 14-28, 14-29):**
$y_{ij}=\mu+\beta(x_{ij}-\bar x_{..})+\varepsilon_{ij}$, $\hat\beta=S_{xy}/S_{xx}$,

$$SS_E'=S_{yy}-\frac{S_{xy}^2}{S_{xx}},\qquad \text{gl}=an-2$$

**Prueba de tratamientos ajustados, $H_0:\tau_i=0$ (ec. 14-30):**

$$F_0=\frac{(SS_E'-SS_E)/(a-1)}{SS_E/[a(n-1)-1]}\ \sim\ F_{a-1,\,a(n-1)-1}$$

**Tabla del ANCOVA como ANOVA "ajustado" (tabla 14-9):**

| Fuente | SS | gl | MS | $F_0$ |
|---|---|---|---|---|
| Regresión | $S_{xy}^2/S_{xx}$ | 1 | | |
| Tratamientos | $SS_E'-SS_E=S_{yy}-S_{xy}^2/S_{xx}-[E_{yy}-E_{xy}^2/E_{xx}]$ | $a-1$ | $(SS_E'-SS_E)/(a-1)$ | $MS_{\text{trat}}/MS_E$ |
| Error | $SS_E=E_{yy}-E_{xy}^2/E_{xx}$ | $a(n-1)-1$ | $MS_E$ | |
| Total | $S_{yy}$ | $an-1$ | | |

**Tabla de cálculo habitual (tabla 14-10):**

| Fuente | gl | $x$ | $xy$ | $y$ | $y$ ajustada | gl ajustados | MS |
|---|---|---|---|---|---|---|---|
| Tratamientos | $a-1$ | $T_{xx}$ | $T_{xy}$ | $T_{yy}$ | | | |
| Error | $a(n-1)$ | $E_{xx}$ | $E_{xy}$ | $E_{yy}$ | $SS_E$ | $a(n-1)-1$ | $MS_E$ |
| Total | $an-1$ | $S_{xx}$ | $S_{xy}$ | $S_{yy}$ | $SS_E'$ | $an-2$ | |
| Tratamientos ajustados | | | | | $SS_E'-SS_E$ | $a-1$ | $(SS_E'-SS_E)/(a-1)$ |

**Medias de tratamiento ajustadas (ec. 14-31)** — estimador de mínimos cuadrados de
$\mu+\tau_i$:

$$\bar y_{i.}\ \text{ajustada}=\bar y_{i.}-\hat\beta(\bar x_{i.}-\bar x_{..})$$

**Error estándar (ec. 14-32):**

$$S_{\bar y_{i.}\,\text{ajustada}}=\left[MS_E\left(\frac1n+\frac{(\bar x_{i.}-\bar x_{..})^2}{E_{xx}}\right)\right]^{1/2}$$

**Prueba de la pendiente, $H_0:\beta=0$ (ec. 14-33):**

$$F_0=\frac{E_{xy}^2/E_{xx}}{MS_E}\ \sim\ F_{1,\,a(n-1)-1}$$

**Residuales (ec. 14-34):** $\hat y_{ij}=\bar y_{i.}+\hat\beta(x_{ij}-\bar x_{i.})$,

$$e_{ij}=y_{ij}-\bar y_{i.}-\hat\beta(x_{ij}-\bar x_{i.})$$

Gráficas: $e$ vs. $\hat y$, $e$ vs. $x$, $e$ vs. tratamiento, probabilidad normal.

**Verificar que los tratamientos no afectan a $x$** (Cochran y Cox): ANOVA de un factor sobre
la covariable, $F_0=[T_{xx}/(a-1)]/[E_{xx}/(a(n-1))]$. Si la variabilidad de las $\bar x_{i.}$
se debe en parte a los tratamientos, el ANCOVA elimina parte del efecto de tratamiento.

### Ejemplo 14-4 — Resistencia de fibra de monofilamento (tabla 14-8)

3 máquinas, $n=5$; $y$ = resistencia a la ruptura (lb), $x$ = diámetro ($10^{-3}$ pulg).
Totales: $y_{i.}=207,\,216,\,180$; $x_{i.}=126,\,130,\,106$; $y_{..}=603$, $x_{..}=362$.

- $S_{yy}=346.40$, $S_{xx}=261.73$, $S_{xy}=282.60$; $T_{yy}=140.40$, $T_{xx}=66.13$,
  $T_{xy}=96.00$; $E_{yy}=206.00$, $E_{xx}=195.60$, $E_{xy}=186.60$.
- $SS_E'=346.40-(282.60)^2/261.73=41.27$ (13 gl); $SS_E=206.00-(186.60)^2/195.60=27.99$ (11
  gl); $SS_E'-SS_E=13.28$ (2 gl). (En la pág. 610 el libro imprime $186.60$ dentro de la
  fórmula de $SS_E'$; el resultado 41.27 corresponde a $S_{xy}=282.60$.)
- **Máquinas ajustadas:** $F_0=(13.28/2)/(27.99/11)=6.64/2.54=2.61$; $F_{0.10,2,11}=2.86$;
  **P = 0.1181** → no hay evidencia de diferencia entre máquinas.
- **Pendiente:** $\hat\beta=186.60/195.60=0.9540$; $F_0=[(186.60)^2/195.60]/2.54=70.08$ vs.
  $F_{0.01,1,11}=9.65$ → se rechaza $\beta=0$; el ajuste era necesario.
- **Medias ajustadas** ($\bar x_{..}=24.13$): $40.38$, $41.42$, $38.80$ (sin ajustar: 41.40,
  43.20, 36.00): quedan mucho más próximas.
- **Covariable vs. tratamientos:** $F_0=(66.13/2)/(195.60/12)=33.07/16.30=2.03<F_{0.10,2,12}=2.81$
  → las máquinas no producen diámetros distintos.
- Residuales: $e_{11}=36-41.4-0.9540(20-25.2)=-0.4392$; sin anomalías (figs. 14-4 a 14-7).
- **Análisis incorrecto ignorando $x$ (tabla 14-12):** Máquinas SS 140.40, 2 gl, MS 70.20;
  error 206.00, 12 gl, MS 17.17; $F_0=4.09$, **P = 0.0442** → conclusión opuesta. Lección: las
  máquinas no difieren una vez eliminado el efecto lineal del diámetro; convendría reducir la
  variabilidad del diámetro dentro de las máquinas.

### 14-3.2 Solución por computadora (Minitab GLM, tabla 14-13)

| Fuente | gl | Seq SS | Adj SS | Adj MS | F | P |
|---|---|---|---|---|---|---|
| Diameter | 1 | 305.13 | 178.01 | 178.01 | 69.97 | 0.000 |
| Machine | 2 | 13.28 | 13.28 | 6.64 | 2.61 | 0.118 |
| Error | 11 | 27.99 | 27.99 | 2.54 | | |
| Total | 14 | 346.40 | | | | |

- Coeficientes: constante 17.177 (SE 2.783, $t=6.17$); Diameter 0.9540 (SE 0.1140, $t=8.36$);
  Machine 1: 0.1824 (SE 0.5950, $t=0.31$, P 0.765); Machine 2: 1.2192 (SE 0.6201, $t=1.97$,
  P 0.075). Media de la covariable 24.13 (desv. est. 4.324).
- Medias de mínimos cuadrados (= medias ajustadas, ec. 14-31): 40.38 (0.7236), 41.42
  (0.7444), 38.80 (0.7879).
- **Seq SS** = partición secuencial:
  $SS(\text{Modelo})=SS(\text{Diámetro})+SS(\text{Máquina}\mid\text{Diámetro})=305.13+13.28=318.41$.
  **Adj SS** = suma de cuadrados "extra" de cada término dados los demás:
  $SS(\text{Máquina}\mid\text{Diámetro})=13.28$ (prueba de tratamientos) y
  $SS(\text{Diámetro}\mid\text{Máquina})=178.01$ (prueba de $\beta=0$).
- El software puede hacer comparaciones múltiples por pares sobre las medias ajustadas.

### 14-3.3 Desarrollo mediante la prueba general de significación de la regresión

Función de mínimos cuadrados (ec. 14-36):
$L=\sum_i\sum_j[y_{ij}-\mu-\tau_i-\beta(x_{ij}-\bar x_{..})]^2$.

**Ecuaciones normales (ecs. 14-37):**

$$\mu:\ an\hat\mu+n\sum_i\hat\tau_i=y_{..}$$
$$\tau_i:\ n\hat\mu+n\hat\tau_i+\hat\beta\sum_j(x_{ij}-\bar x_{..})=y_{i.},\quad i=1..a$$
$$\beta:\ \sum_i\hat\tau_i\sum_j(x_{ij}-\bar x_{..})+\hat\beta S_{xx}=S_{xy}$$

Hay una dependencia lineal (la suma de las $a$ ecuaciones de $\tau_i$ da la de $\mu$); se
añade $\sum\hat\tau_i=0$. Solución (ecs. 14-38): $\hat\mu=\bar y_{..}$,
$\hat\tau_i=\bar y_{i.}-\bar y_{..}-\hat\beta(\bar x_{i.}-\bar x_{..})$,
$\hat\beta=(S_{xy}-T_{xy})/(S_{xx}-T_{xx})=E_{xy}/E_{xx}$.

**Reducción del modelo completo** ($a+1$ gl):

$$R(\mu,\tau,\beta)=\hat\mu y_{..}+\sum_i\hat\tau_i y_{i.}+\hat\beta S_{xy}
=\frac{y_{..}^2}{an}+T_{yy}+\frac{E_{xy}^2}{E_{xx}}$$

$$SS_E=\sum\sum y_{ij}^2-R(\mu,\tau,\beta)=E_{yy}-\frac{E_{xy}^2}{E_{xx}},\qquad
\text{gl}=an-(a+1)=a(n-1)-1\quad(14\text{-}39)$$

**Modelo reducido bajo $H_0$** (ec. 14-40; regresión lineal simple): ecuaciones normales
$an\hat\mu=y_{..}$, $\hat\beta S_{xx}=S_{xy}$;

$$R(\mu,\beta)=\frac{y_{..}^2}{an}+\frac{S_{xy}^2}{S_{xx}}\quad(2\ \text{gl})\qquad(14\text{-}42)$$

**Suma de cuadrados extra de tratamientos (ec. 14-43):**

$$R(\tau\mid\mu,\beta)=R(\mu,\tau,\beta)-R(\mu,\beta)
=S_{yy}-\frac{S_{xy}^2}{S_{xx}}-\left[E_{yy}-\frac{E_{xy}^2}{E_{xx}}\right]=SS_E'-SS_E$$

con $a+1-2=a-1$ gl, y (ec. 14-44)

$$F_0=\frac{R(\tau\mid\mu,\beta)/(a-1)}{SS_E/[a(n-1)-1]}$$

idéntico a la ec. 14-30: el desarrollo heurístico queda justificado.

### 14-3.4 Experimentos factoriales con covariables

- El ANCOVA se extiende a cualquier estructura de tratamientos con datos suficientes por
  combinación. Suponiendo **pendiente común**, la tabla es como la de 14-3.1; lo único que
  cambia es la SS de tratamientos: en un $2^2$ con $n$ réplicas,
  $T_{yy}=\frac1n\sum_i\sum_j y_{ij.}^2-y_{...}^2/[(2)(2)n]$, que luego se parte en $SS_A$,
  $SS_B$, $SS_{AB}$ ajustadas.
- **Número de réplicas:** en un $2^3$ con una pendiente distinta por celda (interacción
  covariable × tratamientos) se requieren al menos 2 réplicas solo para estimar intercepto y
  pendiente por celda (modelo saturado, 0 gl de error) → **mínimo 3 réplicas** para un ANCOVA
  completo en el caso más general.
- **Con réplicas limitadas, tres supuestos alternativos:**
  1. *La covariable no tiene efecto* (el más simple y típicamente el peor: si es falso, el
     análisis puede estar gravemente errado).
  2. *No hay interacción tratamiento × covariable* (pendiente común). Aunque sea falso, el
     efecto promedio de la covariable mejora la precisión; riesgo: si las pendientes se
     cancelan, el término de covariable puede parecer no significativo.
  3. *Algunas interacciones de orden superior son despreciables* y sus gl se usan para el
     error. Hacerlo con cuidado: la estimación del error será imprecisa con pocos gl.
- Advertencia sobre **"réplicas ocultas"**: al eliminar un factor de un $2^3$, las dos
  "réplicas" resultantes liberan gl para estimar parámetros, pero no deben tratarse como
  réplicas genuinas para error puro (la aleatorización no se hizo para ello).

**Ejemplo (tabla 14-14): $2^3$ con 2 réplicas y covariable $x$** (16 corridas; $SS_T=21\,992.0$,
$\bar y=25.02895$).

1. *Sin covariable:* $\hat y=25.03+11.20A+18.05B+7.24C-18.91AB+14.80AC$; $R^2=0.786$,
   $MS_E=470.82$; la observación $y=103.01$ es inusual.
2. *Pendiente común* (Minitab, tabla 14-15; error 7 gl, $MS_E=89.7$): $x$ $F=28.10$
   (P 0.001), $A$ 15.64 (0.005), $B$ 45.31 (0.000), $C$ 0.92 (0.370), $AB$ 40.58 (0.000),
   $AC$ 0.01 (0.913), $BC$ 0.09 (0.769), $ABC$ 0.37 (0.562); $\hat\beta_x=4.9245$ (SE 0.9290).
   *Modelo reducido* (tabla 14-16; términos $x$, $A$, $B$, $AB$; error 11 gl, SS 763.3,
   $MS_E=69.4$): $x$ $F=119.43$, $A$ 20.24 (P 0.001), $B$ 59.05, $AB$ 54.10;
   $\hat\beta_x=5.0876$ (SE 0.4655), constante −1.878.
3. *Pendientes distintas, suponiendo $ABC$ y $ABCx$ despreciables* (SAS PROC GLM, SS tipo III,
   tabla 14-17): modelo 13 gl, error 2 gl, $MS_E=1.40203$, $R^2=0.999872$. Significativos al
   5 %: $C$ (P 0.0378), $x$ (0.0273), $Ax$ (0.0390), $Bx$ (0.0143), $ABx$ (0.0041); no
   significativos: $A$ (0.2099), $B$ (0.0927), $AB$ (0.0731), $AC$ (0.9010), $BC$ (0.6304),
   $Cx$ (0.7908), $ACx$ (0.9726), $BCx$ (0.8470). Eliminando secuencialmente $ACx$ y $BCx$ el
   $MS_E$ baja a 0.7336; luego se eliminan $Cx$, $AC$ y $BC$.
   *Modelo final* (tabla 14-18; 8 gl de modelo, 7 de error, $MS_E=0.81080$, $R^2=0.999742$,
   $F=3389.61$): todos los términos con P ≤ 0.0018. Estimaciones: intercepto 10.2439,
   $A$ 2.7850, $B$ 3.6596, $C$ 5.4561, $AB$ −3.3637, $x$ 2.0472, $Ax$ 2.0632, $Bx$ 3.0341,
   $ABx$ −3.0342.

Conclusiones del autor: cada enfoque mejora sucesivamente el ajuste ($MS_E$: 470.82 → 89.7 →
69.4 → 0.81). Hay que **disponer de gl para el error** y eliminar términos **secuencialmente**
para no descartar efectos enmascarados por una mala estimación del error. Si hay motivos para
creer que la covariable no interactúa con los factores, asumirlo desde el inicio (y el software
puede imponerlo: Minitab de esa versión no modela covariable × tratamiento). Las pruebas
usuales de adecuación del modelo siguen siendo obligatorias.

---

## 14-4 Mediciones repetidas

### Cuándo se usa

Las unidades experimentales son personas ("sujetos") u otras unidades muy heterogéneas; la
variabilidad entre sujetos inflaría $MS_E$. Se controla aplicando **cada uno de los $a$
tratamientos a cada sujeto**: diseño de mediciones repetidas (aquí, un solo factor).

### Modelo (ec. 14-45)

$$y_{ij}=\mu+\tau_i+\beta_j+\varepsilon_{ij},\qquad i=1..a\ (\text{tratamientos}),\ j=1..n\ (\text{sujetos})$$

- Tratamientos fijos, $\sum\tau_i=0$; sujetos = muestra aleatoria de una población:
  $E(\beta_j)=0$, $V(\beta_j)=\sigma_\beta^2$.
- Como $\beta_j$ es común a las $a$ mediciones del sujeto $j$, la covarianza entre $y_{ij}$ e
  $y_{i'j}$ no es cero; **se supone constante** para todos los tratamientos y sujetos
  (simetría compuesta).

### Partición

$$SS_T=SS_{\text{Entre sujetos}}+SS_{\text{Dentro de sujetos}}\ \ (14\text{-}46),\qquad an-1=(n-1)+n(a-1)$$

$$SS_{\text{Dentro de sujetos}}=SS_{\text{Tratamientos}}+SS_E\ \ (14\text{-}47),\qquad n(a-1)=(a-1)+(a-1)(n-1)$$

con $SS_{\text{Entre}}=a\sum_j(\bar y_{.j}-\bar y_{..})^2$,
$SS_{\text{Trat}}=n\sum_i(\bar y_{i.}-\bar y_{..})^2$,
$SS_E=\sum_i\sum_j(y_{ij}-\bar y_{i.}-\bar y_{.j}+\bar y_{..})^2$.

### ANOVA (tabla 14-20)

| Fuente | SS | gl | MS | $F_0$ |
|---|---|---|---|---|
| 1. Entre sujetos | $\sum_j\dfrac{y_{.j}^2}{a}-\dfrac{y_{..}^2}{an}$ | $n-1$ | | |
| 2. Dentro de sujetos | $\sum_i\sum_j y_{ij}^2-\sum_j\dfrac{y_{.j}^2}{a}$ | $n(a-1)$ | | |
| 3. (Tratamientos) | $\sum_i\dfrac{y_{i.}^2}{n}-\dfrac{y_{..}^2}{an}$ | $a-1$ | $SS_{\text{Trat}}/(a-1)$ | $MS_{\text{Trat}}/MS_E$ |
| 4. (Error) | línea (2) − línea (3) | $(a-1)(n-1)$ | $SS_E/[(a-1)(n-1)]$ | |
| 5. Total | $\sum_i\sum_j y_{ij}^2-\dfrac{y_{..}^2}{an}$ | $an-1$ | | |

**Prueba (ec. 14-48):** $H_0:\tau_1=\dots=\tau_a=0$;

$$F_0=\frac{SS_{\text{Trat}}/(a-1)}{SS_E/[(a-1)(n-1)]}\ \sim\ F_{a-1,\,(a-1)(n-1)}$$

**Equivalencia clave:** es el análisis de un **diseño de bloques completos aleatorizados con
los sujetos como bloques**. El libro no presenta ejemplo numérico en esta sección.

---

## Reglas prácticas y advertencias del capítulo

- Box-Cox: preferir $\lambda$ redondos; si el IC de $\lambda$ contiene 1, no transformar.
- Si importa predecir en la escala original y la transformación da valores imposibles
  (negativos), usar un GLM con enlace adecuado (log para conteos/gamma, logit para binomial);
  sus IC suelen ser más cortos.
- Desbalance: proporcional → ANOVA estándar modificado; leve → métodos aproximados (ajustando
  gl o $MS_E'$); fuerte o con celdas vacías → regresión (SS tipo III / prueba general).
- ANCOVA: comprobar que $\beta\neq0$, que las pendientes son comunes y que los tratamientos no
  afectan a la covariable; reportar medias **ajustadas** con su error estándar; ignorar una
  covariable relevante puede invertir la conclusión (ej. 14-4: P 0.0442 sin ajustar vs. 0.1181
  ajustado).
- Mediciones repetidas de un factor = RCBD con sujetos como bloques, bajo covarianza constante.

## 14-5 Problemas (solo referencia)

14-1 a 14-9: aplicar Box-Cox a experimentos de capítulos previos (5-22, 6-3, 8-23, 8-24,
8-25, 8-29, 11-14, 11-33, 11-34). 14-10 a 14-12: ANCOVA de un factor (carretillas y tiempo de
descarga; medias ajustadas y errores estándar; completar un ANCOVA dadas las sumas de cuadrados
y productos). Los problemas posteriores a 14-12 (págs. 628–629) no están en el escaneo.
