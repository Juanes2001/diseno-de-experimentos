# Capítulo 4 — Bloques aleatorizados, cuadrados latinos y diseños relacionados

> Montgomery, págs. 126–169

> **Nota sobre el escaneo:** las páginas **136–137 del libro no están en el PDF** (de la 135 se
> salta a la 138). Contenían las figuras 4-4 a 4-6 (gráficas de residuales del ejemplo 4-1), el
> final de la sección 4-1.2 y el inicio de la 4-1.3 (aditividad). Lo que aquí se dice de esa parte
> se reconstruye solo de lo que se alcanza a leer en las págs. 135 y 138 y va marcado como tal.
> En este capítulo (2.ª ed. en español) **no aparece** una fórmula de eficiencia relativa del RCBD
> frente al diseño completamente aleatorizado en las páginas legibles; la comparación se hace
> solo numéricamente (tablas 4-5 vs. 4-6).

Mapa del capítulo:

| Diseño | Fuentes perturbadoras bloqueadas | Corridas | gl del error |
|---|---|---|---|
| RCBD (4-1) | 1 (bloques) | $ab$ | $(a-1)(b-1)$ |
| Cuadrado latino (4-2) | 2 (renglones, columnas) | $p^2$ | $(p-2)(p-1)$ |
| Cuadrado grecolatino (4-3) | 3 (renglones, columnas, letras griegas) | $p^2$ | $(p-3)(p-1)$ |
| BIBD (4-4) | 1, con bloques de tamaño $k<a$ | $N=ar=bk$ | $N-a-b+1$ |

---

## 4-1 Diseño de bloques completos aleatorizados (RCBD)

### Cuándo se usa

- Clasificación de los **factores perturbadores** (afectan la respuesta pero no interesan):
  - *desconocido y no controlable* → protección por **aleatorización**;
  - *conocido pero no controlable* (se puede medir) → **análisis de covarianza** (cap. 14);
  - *conocido y controlable* → **formación de bloques**, que elimina sistemáticamente su efecto
    de las comparaciones entre tratamientos.
- RCBD (*randomized complete block design*): cada bloque contiene **todos** los tratamientos
  ("completo"), una observación por tratamiento en cada bloque. Dentro de cada bloque el orden
  de los tratamientos se aleatoriza. Es la generalización de la prueba $t$ pareada (sec. 2-5).
- Los bloques son una **restricción sobre la aleatorización**: solo se aleatoriza dentro del bloque.
- Bloques típicos: unidades de equipo o máquinas, lotes de materia prima, personas, tiempo.
- Otro uso: probar la **robustez** de una variable de proceso frente a condiciones difíciles de
  controlar, haciendo que cada bloque sea una combinación de esos factores no controlables
  (Coleman y Montgomery).
- Ejemplo guía: 4 tipos de punta de un durómetro probadas en 4 ejemplares de metal (bloques);
  respuesta: dureza Rockwell C menos 40 (tabla 4-1). Con un CRD se necesitarían 16 ejemplares y
  la variabilidad entre ejemplares inflaría el error.

### 4-1.1 Análisis estadístico

**Modelo de los efectos** (ec. 4-1):

$$y_{ij} = \mu + \tau_i + \beta_j + \varepsilon_{ij}, \qquad i=1,\dots,a;\; j=1,\dots,b$$

- $\mu$: media global; $\tau_i$: efecto del tratamiento $i$; $\beta_j$: efecto del bloque $j$;
  $\varepsilon_{ij}\sim \text{NID}(0,\sigma^2)$.
- Inicialmente tratamientos y bloques fijos. Modelo sobreespecificado, con restricciones
  $\sum_{i=1}^a \tau_i = 0$, $\sum_{j=1}^b \beta_j = 0$.
- Modelo de las medias equivalente: $y_{ij} = \mu_{ij} + \varepsilon_{ij}$, con
  $\mu_{ij} = \mu + \tau_i + \beta_j$.

**Hipótesis:** $H_0: \mu_1 = \dots = \mu_a$ vs. $H_1$: al menos una $\mu_i \neq \mu_j$; equivalentemente
$H_0: \tau_1 = \dots = \tau_a = 0$ (porque $\mu_i = \frac{1}{b}\sum_j(\mu+\tau_i+\beta_j) = \mu+\tau_i$).

**Notación** (ecs. 4-2 a 4-5): $y_{i.}=\sum_j y_{ij}$, $y_{.j}=\sum_i y_{ij}$,
$y_{..}=\sum_i\sum_j y_{ij}$, $N=ab$; $\bar y_{i.}=y_{i.}/b$, $\bar y_{.j}=y_{.j}/a$, $\bar y_{..}=y_{..}/N$.

**Partición de la suma de cuadrados** (ecs. 4-7, 4-8; los productos cruzados se anulan):

$$\sum_i\sum_j (y_{ij}-\bar y_{..})^2 = b\sum_i(\bar y_{i.}-\bar y_{..})^2 + a\sum_j(\bar y_{.j}-\bar y_{..})^2 + \sum_i\sum_j (y_{ij}-\bar y_{i.}-\bar y_{.j}+\bar y_{..})^2$$

$$SS_T = SS_{\text{Tratamientos}} + SS_{\text{Bloques}} + SS_E$$

**Fórmulas de cálculo** (ecs. 4-9 a 4-12):

$$SS_T = \sum_i\sum_j y_{ij}^2 - \frac{y_{..}^2}{N},\qquad
SS_{\text{Trat}} = \frac{1}{b}\sum_{i=1}^a y_{i.}^2 - \frac{y_{..}^2}{N},\qquad
SS_{\text{Bloques}} = \frac{1}{a}\sum_{j=1}^b y_{.j}^2 - \frac{y_{..}^2}{N}$$

$$SS_E = SS_T - SS_{\text{Trat}} - SS_{\text{Bloques}}$$

**Cuadrados medios esperados** (tratamientos y bloques fijos):

$$E(MS_{\text{Trat}}) = \sigma^2 + \frac{b\sum_i \tau_i^2}{a-1},\qquad
E(MS_{\text{Bloques}}) = \sigma^2 + \frac{a\sum_j \beta_j^2}{b-1},\qquad
E(MS_E)=\sigma^2$$

Bajo normalidad, $SS_{\text{Trat}}/\sigma^2$, $SS_{\text{Bloques}}/\sigma^2$ y $SS_E/\sigma^2$ son
ji-cuadradas independientes (teorema 3-1).

**Tabla ANOVA** (tabla 4-2):

| Fuente | SS | gl | MS | $F_0$ |
|---|---|---|---|---|
| Tratamientos | $SS_{\text{Trat}}$ | $a-1$ | $SS_{\text{Trat}}/(a-1)$ | $MS_{\text{Trat}}/MS_E$ |
| Bloques | $SS_{\text{Bloques}}$ | $b-1$ | $SS_{\text{Bloques}}/(b-1)$ | (no se reporta) |
| Error | $SS_E$ | $(a-1)(b-1)$ | $SS_E/[(a-1)(b-1)]$ | |
| Total | $SS_T$ | $N-1$ | | |

**Prueba:** rechazar $H_0$ si $F_0 = MS_{\text{Trat}}/MS_E > F_{\alpha,\,a-1,\,(a-1)(b-1)}$.

**Sobre la prueba de los bloques** ($F_0 = MS_{\text{Bloques}}/MS_E$ contra $F_{\alpha,b-1,(a-1)(b-1)}$):

- Por los cuadrados medios esperados parecería válida, pero la aleatorización solo se aplicó a
  los tratamientos dentro de los bloques.
- Box, Hunter y Hunter: la $F$ del ANOVA se justifica solo por la aleatorización, sin normalidad
  (la $F$ normal aproxima la distribución de aleatorización); para bloques esa justificación no
  aplica, aunque si los errores son NID$(0,\sigma^2)$ el cociente sí puede usarse.
- Anderson y McLean: el cociente prueba la igualdad de medias de bloques **más** la restricción
  sobre la aleatorización ("error de la restricción").
- **Práctica recomendada:** no tratarlo como prueba $F$ exacta (por eso no va en la tabla ANOVA),
  pero sí examinar el cociente $MS_{\text{Bloques}}/MS_E$ como procedimiento aproximado: si es
  grande, la formación de bloques fue útil y redujo el ruido; si es pequeño, quizá no haga falta
  bloquear en experimentos futuros.

**Residuales y valores ajustados** (ec. 4-13):

$$\hat y_{ij} = \bar y_{i.} + \bar y_{.j} - \bar y_{..},\qquad e_{ij} = y_{ij} - \bar y_{i.} - \bar y_{.j} + \bar y_{..}$$

**Comparaciones múltiples** (tratamientos fijos y $F$ significativa): cualquier método de la
sección 3-5, sustituyendo el número de réplicas $n$ por el número de bloques $b$ y los gl del
error $a(n-1)$ por $(a-1)(b-1)$. Método gráfico: medias contra una distribución $t$ escalada con
factor $\sqrt{MS_E/b}$.

#### Ejemplo 4-1 — Prueba de dureza (4 puntas × 4 ejemplares)

- Datos codificados: $(y - 9.5)\times 10$. Totales de tratamiento: 3, 4, −2, 15; totales de
  bloque: −4, −3, 9, 18; $y_{..}=20$; $\sum\sum y_{ij}^2 = 154$.
- ANOVA (tabla 4-5, datos codificados):

| Fuente | SS | gl | MS | $F_0$ | Valor P |
|---|---|---|---|---|---|
| Tipo de punta | 38.50 | 3 | 12.83 | 14.44 | 0.0009 |
| Bloques (ejemplares) | 82.50 | 3 | 27.50 | | |
| Error | 8.00 | 9 | 0.89 | | |
| Total | 129.00 | 15 | | | |

- $F_{0.05,3,9}=3.86$ → el tipo de punta afecta la dureza media. El cuadrado medio de bloques es
  grande frente al error: los ejemplares difieren.
- **Análisis incorrecto como CRD** (tabla 4-6): $SS_E = 90.50$ con 12 gl, $MS_E = 7.54$,
  $F_0 = 1.70 < F_{0.05,3,12}=3.49$ → no se detectaría nada. Lección: no bloquear cuando se debe
  infla el error hasta ocultar diferencias reales.
- Salida de Design-Expert (figura 4-2, datos originales; SS = las codificadas ÷ 100): Block
  0.82, Model/A 0.38 (3 gl, MS 0.13, F = 14.44, P = 0.0009), Residual 0.080 (9 gl,
  MS 8.889E-003), Cor Total 1.29. Std. Dev. 0.094, Mean 9.63, C.V. 0.98, PRESS 0.25,
  $R^2$ = 0.8280, $R^2_{adj}$ = 0.7706, $R^2_{pred}$ = 0.4563, Adeq Precision 15.635.
- Medias de tratamiento: 9.57, 9.60, 9.45, 9.88 (el error estándar aparece impreso como 0.47,
  que corresponde a los datos codificados; en unidades originales sería 0.047).
- LSD de Fisher (error estándar de la diferencia 0.067):

| Par | Diferencia | $t$ | Prob > \|t\| |
|---|---|---|---|
| 1 vs 2 | −0.025 | −0.38 | 0.7163 |
| 1 vs 3 | 0.13 | 1.87 | 0.0935 |
| 1 vs 4 | −0.30 | −4.50 | 0.0015 |
| 2 vs 3 | 0.15 | 2.25 | 0.0510 |
| 2 vs 4 | −0.27 | −4.12 | 0.0026 |
| 3 vs 4 | −0.43 | −6.37 | 0.0001 |

- Conclusión: $\mu_1=\mu_2=\mu_3$ y la punta 4 da dureza media significativamente mayor.
  La gráfica con $t$ escalada (figura 4-3, factor $\sqrt{0.89/4}=0.47$) lo confirma.

### 4-1.2 Verificación de la adecuación del modelo

- Vigilar: no normalidad, desigualdad de varianza por tratamiento **o por bloque**, e
  **interacción bloque-tratamiento**. Herramienta principal: análisis de residuales.
- Gráficas: probabilidad normal de residuales; residuales contra tratamiento, contra bloque y
  contra valores ajustados $\hat y_{ij}$ (figuras 4-4 a 4-6, en págs. 136–137 no disponibles).
- Ejemplo 4-1 (datos codificados): residuales entre −1.00 y 1.50 (el mayor, 1.50, corresponde a
  $y=-1$, $\hat y=-2.50$); en Design-Expert ese punto tiene residual estudentizado 2.121 y
  $t$ de punto atípico 2.828. Sin indicios marcados de no normalidad ni puntos atípicos (pág. 135).
  El resto de la interpretación (pág. 136–137) no se pudo leer.

### 4-1.3 Otros aspectos del RCBD

#### Aditividad del modelo (inicio en págs. 136–137, no disponibles; lo siguiente es de la pág. 138)

- El modelo es **aditivo**: el efecto del tratamiento es el mismo en todos los bloques. Ej.: si
  $\tau_1 = 5$ y $\beta_1=2$, $E(y_{11}) = \mu+7$; el tratamiento 1 siempre suma 5 unidades.
- Puede fallar si hay **interacción tratamiento-bloque** (ej.: una impureza en un lote que afecta
  solo a una formulación).
- La interacción también aparece al medir en la escala incorrecta: una relación multiplicativa
  $E(y_{ij}) = \mu\tau_i\beta_j$ se vuelve aditiva con logaritmo:
  $\ln E(y_{ij}) = \ln\mu + \ln\tau_i + \ln\beta_j$. No toda interacción se elimina con una
  transformación.
- Consecuencia: la interacción **infla $MS_E$** y perjudica la comparación de tratamientos; puede
  invalidar el ANOVA. Detectarla con residuales y otros diagnósticos.
- Si interesan ambos factores y su interacción → **diseños factoriales** (caps. 5–9).

#### Tratamientos y bloques aleatorios

- El procedimiento de prueba es el mismo si tratamientos o bloques (o ambos) son aleatorios;
  cambia la interpretación y los cuadrados medios esperados.
- Bloques aleatorios (caso frecuente): las comparaciones entre tratamientos valen para toda la
  **población de bloques** muestreada. $E(MS_{\text{Bloques}}) = \sigma^2 + a\sigma_\beta^2$.
- $E(MS_{\text{Trat}})$ siempre está libre de efectos de bloque; el estadístico siempre es
  $F_0 = MS_{\text{Trat}}/MS_E$.
- Con bloques aleatorios e interacción tratamiento-bloque, tanto $E(MS_{\text{Trat}})$ como
  $E(MS_E)$ contienen la interacción, así que la prueba de tratamientos sigue siendo válida,
  aunque no informa sobre la interacción.

#### Elección del tamaño de la muestra (número de bloques)

Más bloques → más réplicas y más gl del error. Se usan las curvas de operación característica
(apéndice, parte V) con (ec. 4-14):

$$\Phi^2 = \frac{b\sum_{i=1}^a \tau_i^2}{a\sigma^2},\qquad \nu_1 = a-1,\quad \nu_2=(a-1)(b-1)$$

En términos de la diferencia máxima $D$ a detectar (ec. 3-49 con $b$ en lugar de $n$):
$\Phi^2 = \dfrac{bD^2}{2a\sigma^2}$.

**Ejemplo 4-2:** dureza, $D=0.4$, $\sigma = 0.1$ (unidades originales), $a=4$ →
$\Phi^2 = 2.0b$. Con $b=3$: $\Phi=2.45$, 6 gl de error, $\beta\approx 0.10$ (potencia 0.90). Con
$b=4$: $\Phi=2.83$, 9 gl, $\beta\approx 0.03$ (potencia 0.97). Se eligen 4 bloques
($\alpha = 0.05$, $\nu_1=3$).

#### Estimación de valores faltantes (análisis aproximado)

- Un dato faltante rompe la **ortogonalidad** entre tratamientos y bloques.
- Dos enfoques: *aproximado* (estimar el dato, hacer el ANOVA usual y restar 1 gl al error) y
  *exacto* (sec. 4-1.4).
- Se elige $x$ que minimiza $SS_E$. Con $y'_{i.}$, $y'_{.j}$, $y'_{..}$ los totales del
  tratamiento, del bloque y general **sin** el dato faltante (ec. 4-15):

$$SS_E = x^2 - \frac{1}{b}(y'_{i.}+x)^2 - \frac{1}{a}(y'_{.j}+x)^2 + \frac{1}{ab}(y'_{..}+x)^2 + R$$

  y de $dSS_E/dx=0$ (ec. 4-16):

$$x = \frac{a\,y'_{i.} + b\,y'_{.j} - y'_{..}}{(a-1)(b-1)}$$

- **Ilustración** (tabla 4-7, falta punta 2 en ejemplar 3, datos codificados):
  $y'_{2.}=1$, $y'_{.3}=6$, $y'_{..}=17$ → $x = [4(1)+4(6)-17]/9 = 1.22$. ANOVA aproximado
  (tabla 4-8):

| Fuente | SS | gl | MS | $F_0$ | Valor P |
|---|---|---|---|---|---|
| Tipo de punta | 39.98 | 3 | 13.33 | 17.12 | 0.0008 |
| Bloques | 79.53 | 3 | 26.51 | | |
| Error | 6.22 | 8 | 0.78 | | |
| Total | 125.73 | 14 | | | |

- **Varios faltantes:** (a) escribir $SS_E$ como función de todos, derivar respecto a cada uno e
  igualar a cero; o (b) usar la ec. 4-16 **iterativamente**: fijar un valor arbitrario para el
  primero, estimar el segundo, reestimar el primero, etc., hasta converger. Siempre se resta
  **1 gl del error por cada dato faltante**.

### 4-1.4 Estimación de parámetros y prueba general de significación de la regresión

**Ecuaciones normales** (ec. 4-18), para el modelo 4-17 con efectos fijos:

$$\mu:\; ab\hat\mu + b\sum_i\hat\tau_i + a\sum_j\hat\beta_j = y_{..}$$
$$\tau_i:\; b\hat\mu + b\hat\tau_i + \sum_j\hat\beta_j = y_{i.}\quad (i=1,\dots,a)$$
$$\beta_j:\; a\hat\mu + \sum_i\hat\tau_i + a\hat\beta_j = y_{.j}\quad (j=1,\dots,b)$$

Hay dos dependencias lineales → dos restricciones (ec. 4-19): $\sum_i\hat\tau_i=0$,
$\sum_j\hat\beta_j=0$. Solución (ec. 4-21):

$$\hat\mu = \bar y_{..},\qquad \hat\tau_i = \bar y_{i.}-\bar y_{..},\qquad \hat\beta_j = \bar y_{.j}-\bar y_{..}$$

$$\hat y_{ij} = \hat\mu+\hat\tau_i+\hat\beta_j = \bar y_{i.}+\bar y_{.j}-\bar y_{..}$$

**Reducciones en suma de cuadrados:**

| Modelo | Reducción | gl |
|---|---|---|
| Completo $\mu+\tau_i+\beta_j$ | $R(\mu,\tau,\beta) = \sum_i \dfrac{y_{i.}^2}{b} + \sum_j \dfrac{y_{.j}^2}{a} - \dfrac{y_{..}^2}{ab}$ | $a+b-1$ |
| Reducido $\mu+\beta_j$ | $R(\mu,\beta) = \sum_j \dfrac{y_{.j}^2}{a}$ | $b$ |
| Reducido $\mu+\tau_i$ | $R(\mu,\tau) = \sum_i \dfrac{y_{i.}^2}{b}$ | $a$ |

- $SS_E = \sum\sum y_{ij}^2 - R(\mu,\tau,\beta)$, con $(a-1)(b-1)$ gl.
- $R(\tau\mid\mu,\beta) = R(\mu,\tau,\beta)-R(\mu,\beta) = \sum_i y_{i.}^2/b - y_{..}^2/ab = SS_{\text{Trat}}$ ($a-1$ gl).
- $R(\beta\mid\mu,\tau) = R(\mu,\tau,\beta)-R(\mu,\tau) = \sum_j y_{.j}^2/a - y_{..}^2/ab = SS_{\text{Bloques}}$ ($b-1$ gl).
- No se usa para el RCBD balanceado, pero es el método para diseños de bloques más generales
  (sec. 4-4) y para datos faltantes.

**Análisis exacto del valor faltante:** el análisis aproximado produce un $MS_{\text{Trat}}$
sesgado ($E(MS_{\text{Trat}}) > E(MS_E)$ bajo $H_0$) → **reporta demasiados resultados
significativos**. El análisis exacto trata el diseño como no balanceado (tratamientos y bloques no
ortogonales) y aplica la prueba general de significación de la regresión (problema 4-26).

---

## 4-2 Diseño de cuadrado latino

### Cuándo se usa

- Elimina **dos** fuentes de variabilidad perturbadora: bloqueo sistemático en dos direcciones
  (renglones y columnas), que son **dos restricciones sobre la aleatorización**.
- Cuadrado latino $p\times p$: $p$ renglones, $p$ columnas, $p$ tratamientos (letras latinas);
  cada letra aparece **exactamente una vez en cada renglón y en cada columna**. Renglones y
  columnas son ortogonales a los tratamientos. $N=p^2$ corridas.
- También sirve para estudiar tres factores (renglones, columnas, letras) con $p$ niveles cada
  uno en $p^2$ corridas cuando no hay restricciones de aleatorización, **suponiendo que no hay
  interacción** entre ellos.
- Ejemplo guía: 5 formulaciones de carga propulsora (A–E), 5 lotes de materia prima (renglones),
  5 operadores (columnas); respuesta: rapidez de combustión.

### Modelo (ec. 4-22)

$$y_{ijk} = \mu + \alpha_i + \tau_j + \beta_k + \varepsilon_{ijk},\qquad i,j,k = 1,\dots,p$$

- $\alpha_i$: efecto del renglón $i$; $\tau_j$: efecto del tratamiento $j$; $\beta_k$: efecto de
  la columna $k$; $\varepsilon_{ijk}\sim\text{NID}(0,\sigma^2)$.
- Modelo de efectos **completamente aditivo** (sin interacción renglón-columna-tratamiento).
- Solo dos de los tres subíndices bastan para identificar una observación.

### ANOVA (ec. 4-23, tabla 4-10)

$$SS_T = SS_{\text{Renglones}} + SS_{\text{Columnas}} + SS_{\text{Tratamientos}} + SS_E$$

| Fuente | SS | gl | MS | $F_0$ |
|---|---|---|---|---|
| Tratamientos | $\dfrac{1}{p}\sum_{j=1}^p y_{.j.}^2 - \dfrac{y_{...}^2}{N}$ | $p-1$ | $SS/(p-1)$ | $MS_{\text{Trat}}/MS_E$ |
| Renglones | $\dfrac{1}{p}\sum_{i=1}^p y_{i..}^2 - \dfrac{y_{...}^2}{N}$ | $p-1$ | $SS/(p-1)$ | |
| Columnas | $\dfrac{1}{p}\sum_{k=1}^p y_{..k}^2 - \dfrac{y_{...}^2}{N}$ | $p-1$ | $SS/(p-1)$ | |
| Error | por sustracción | $(p-2)(p-1)$ | $SS_E/[(p-2)(p-1)]$ | |
| Total | $\sum_i\sum_j\sum_k y_{ijk}^2 - \dfrac{y_{...}^2}{N}$ | $p^2-1$ | | |

- Prueba: $F_0 = MS_{\text{Trat}}/MS_E \sim F_{p-1,\,(p-2)(p-1)}$ bajo $H_0$.
- Los cocientes $MS_{\text{Renglones}}/MS_E$ y $MS_{\text{Columnas}}/MS_E$ pueden formarse, pero
  al ser restricciones sobre la aleatorización quizá no sean pruebas apropiadas.

**Residuales:**

$$e_{ijk} = y_{ijk}-\hat y_{ijk} = y_{ijk} - \bar y_{i..} - \bar y_{.j.} - \bar y_{..k} + 2\bar y_{...}$$

### Cuadrado latino estándar y aleatorización

- **Estándar:** primer renglón y primera columna en orden alfabético. Siempre se obtiene uno
  escribiendo el primer renglón en orden alfabético y cada renglón siguiente como el anterior
  recorrido un lugar a la izquierda (cíclico).
- Tabla 4-13:

| Tamaño | 3×3 | 4×4 | 5×5 | 6×6 | 7×7 | $p\times p$ |
|---|---|---|---|---|---|---|
| N.º de cuadrados estándares | 1 | 4 | 56 | 9408 | 16 942 080 | — |
| N.º total de cuadrados latinos | 12 | 576 | 161 280 | 818 851 200 | 61 479 419 904 000 | $p!\,(p-1)!\times$ (n.º de estándares) |

- **Aleatorización correcta:** elegir al azar el cuadrado. En la práctica: tomar un cuadrado de
  una tabla (Fisher y Yates) y **ordenar al azar renglones, columnas y letras**.

### Valor faltante (ec. 4-24)

$$y_{ijk} = \frac{p\,(y'_{i..} + y'_{.j.} + y'_{..k}) - 2y'_{...}}{(p-2)(p-1)}$$

con las primas indicando los totales de renglón, tratamiento y columna (y el gran total) que
contienen el valor faltante.

### Ejemplo 4-3 — Carga propulsora (cuadrado latino 5×5)

- Diseño estándar cíclico (tabla 4-9); datos codificados restando 25. Totales de lotes
  (renglones): −14, 9, 5, 3, 7; de operadores (columnas): −18, 18, −4, 5, 9; de formulaciones
  A–E: 18, −24, −13, 24, 5; $y_{...}=10$; $\sum y^2 = 680$.
- ANOVA (tabla 4-12):

| Fuente | SS | gl | MS | $F_0$ | Valor P |
|---|---|---|---|---|---|
| Formulaciones | 330.00 | 4 | 82.50 | 7.73 | 0.0025 |
| Lotes de materia prima | 68.00 | 4 | 17.00 | | |
| Operadores | 150.00 | 4 | 37.50 | | |
| Error | 128.00 | 12 | 10.67 | | |
| Total | 676.00 | 24 | | | |

- Conclusión: las formulaciones difieren en rapidez de combustión media. Hay indicios de
  diferencias entre operadores (bloquear fue buena precaución); no hay evidencia sólida de
  diferencias entre lotes, aunque bloquear por lote suele ser buena idea.

### Réplicas de cuadrados latinos

Problema: los cuadrados pequeños dan pocos gl de error (3×3: 2; 4×4: 6). Se replica $n$ veces;
$N = np^2$. El ANOVA depende de **cómo** se replica. Notación: $y_{ijkl}$ = renglón $i$,
tratamiento $j$, columna $k$, réplica $l$.

| Caso | Qué se repite | gl renglones | gl columnas | gl error |
|---|---|---|---|---|
| 1 | Mismos renglones y mismas columnas en cada réplica | $p-1$ | $p-1$ | $(p-1)[n(p+1)-3]$ |
| 2 | Mismas columnas, renglones nuevos en cada réplica (o viceversa) | $n(p-1)$ | $p-1$ | $(p-1)(np-1)$ |
| 3 | Renglones y columnas nuevos en cada réplica | $n(p-1)$ | $n(p-1)$ | $(p-1)[n(p-1)-1]$ |

En los tres casos: tratamientos con $p-1$ gl, réplicas con $n-1$ gl, total $np^2-1$,
$F_0 = MS_{\text{Trat}}/MS_E$. Sumas de cuadrados (tablas 4-14 a 4-16):

- Tratamientos: $\dfrac{1}{np}\sum_{j} y_{.j..}^2 - \dfrac{y_{....}^2}{N}$
- Réplicas: $\dfrac{1}{p^2}\sum_{l=1}^n y_{...l}^2 - \dfrac{y_{....}^2}{N}$
- Renglones, caso 1: $\dfrac{1}{np}\sum_i y_{i...}^2 - \dfrac{y_{....}^2}{N}$; casos 2 y 3
  (renglones **dentro de** réplicas): $\dfrac{1}{p}\sum_{l=1}^n\sum_{i=1}^p y_{i..l}^2 - \sum_{l=1}^n \dfrac{y_{...l}^2}{p^2}$
- Columnas, casos 1 y 2: $\dfrac{1}{np}\sum_k y_{..k.}^2 - \dfrac{y_{....}^2}{N}$; caso 3
  (columnas dentro de réplicas): $\dfrac{1}{p}\sum_{l=1}^n\sum_{k=1}^p y_{..kl}^2 - \sum_{l=1}^n \dfrac{y_{...l}^2}{p^2}$
- Error: por sustracción. Total: $\sum\sum\sum\sum y_{ijkl}^2 - y_{....}^2/N$.

Hay otros análisis que admiten interacción tratamientos × cuadrados (problema 4-19, modelo
$y_{ijkh} = \mu+\rho_h+\alpha_{i(h)}+\tau_j+\beta_{k(h)}+(\tau\rho)_{jh}+\varepsilon_{ijkh}$).

### Diseños alternados (entrecruzados, *crossover*) y efectos residuales

- Situación: los **periodos** son un factor; $p$ tratamientos se prueban en $p$ periodos usando
  $np$ unidades experimentales (sujetos).
- Ejemplo: 2 fluidos de restitución (A, B) en 20 sujetos. Periodo 1: mitad de los sujetos (al
  azar) recibe A y la otra mitad B; tras un periodo de lavado que elimina el efecto fisiológico,
  se intercambian.
- Se analiza como **10 cuadrados latinos 2×2**: renglones = periodos, columnas = sujetos,
  letras = fluidos (figura 4-7).
- ANOVA (tabla 4-17):

| Fuente | gl |
|---|---|
| Sujetos (columnas) | 19 |
| Periodos (renglones) | 1 |
| Fluidos (letras) | 1 |
| Error | 18 |
| Total | 39 |

  $SS_{\text{Sujetos}}$: SC corregida entre los 20 totales de sujetos; $SS_{\text{Periodos}}$:
  SC corregida entre renglones; $SS_{\text{Fluidos}}$: SC corregida entre totales de letras.
- **Efecto residual (*carryover*):** si el tratamiento de un periodo influye en la respuesta del
  siguiente, se requieren diseños balanceados para efectos residuales (Cochran y Cox; John).

---

## 4-3 Diseño de cuadrado grecolatino

### Cuándo se usa y construcción

- Se superponen dos cuadrados latinos $p\times p$ (uno con letras latinas, otro con griegas)
  **ortogonales**: cada letra griega aparece exactamente una vez con cada letra latina.
- Controla **tres** fuentes de variabilidad extraña (bloqueo en tres direcciones), o permite
  estudiar cuatro factores (renglones, columnas, latinas, griegas) con $p$ niveles en $p^2$ corridas.
- Existen para todo $p\ge 3$ **excepto $p=6$**.
- Ejemplo 4×4 (tabla 4-18):

| Renglón | Col 1 | Col 2 | Col 3 | Col 4 |
|---|---|---|---|---|
| 1 | Aα | Bβ | Cγ | Dδ |
| 2 | Bδ | Aγ | Dβ | Cα |
| 3 | Cβ | Dα | Aδ | Bγ |
| 4 | Dγ | Cδ | Bα | Aβ |

### Modelo (ec. 4-25)

$$y_{ijkl} = \mu + \theta_i + \tau_j + \omega_k + \Psi_l + \varepsilon_{ijkl},\qquad i,j,k,l=1,\dots,p$$

$\theta_i$: renglón; $\tau_j$: letra latina; $\omega_k$: letra griega; $\Psi_l$: columna;
$\varepsilon_{ijkl}\sim\text{NID}(0,\sigma^2)$. Bastan dos subíndices para identificar una observación.

### ANOVA (tabla 4-19)

| Fuente | SS | gl |
|---|---|---|
| Letras latinas | $SS_L = \dfrac{1}{p}\sum_j y_{.j..}^2 - \dfrac{y_{....}^2}{N}$ | $p-1$ |
| Letras griegas | $SS_G = \dfrac{1}{p}\sum_k y_{..k.}^2 - \dfrac{y_{....}^2}{N}$ | $p-1$ |
| Renglones | $\dfrac{1}{p}\sum_i y_{i...}^2 - \dfrac{y_{....}^2}{N}$ | $p-1$ |
| Columnas | $\dfrac{1}{p}\sum_l y_{...l}^2 - \dfrac{y_{....}^2}{N}$ | $p-1$ |
| Error | por sustracción | $(p-3)(p-1)$ |
| Total | $\sum\sum\sum\sum y_{ijkl}^2 - \dfrac{y_{....}^2}{N}$ | $p^2-1$ |

Cada efecto se prueba con $MS/MS_E$ contra $F_{p-1,\,(p-3)(p-1)}$ (cola superior).

### Ejemplo 4-4 — Carga propulsora con montajes de prueba (grecolatino 5×5)

- Se añade al ejemplo 4-3 el factor *montaje de prueba* (letras griegas α–ε). Totales por letra
  griega: 10, −6, −3, −4, 13 → $SS_{\text{Montajes}} = \frac{1}{5}[10^2+6^2+3^2+4^2+13^2] - 10^2/25 = 62.00$.
- ANOVA (tabla 4-21):

| Fuente | SS | gl | MS | $F_0$ | Valor P |
|---|---|---|---|---|---|
| Formulaciones | 330.00 | 4 | 82.50 | 10.00 | 0.0033 |
| Lotes de materia prima | 68.00 | 4 | 17.00 | | |
| Operadores | 150.00 | 4 | 37.50 | | |
| Montajes de prueba | 62.00 | 4 | 15.50 | | |
| Error | 66.00 | 8 | 8.25 | | |
| Total | 676.00 | 24 | | | |

- Las formulaciones difieren al 1 %. Frente al ejemplo 4-3 el error baja (128 → 66) pero también
  los gl (12 → 8): menos gl puede hacer la prueba menos sensible.

### Hipercuadrados

Superposición de tres o más cuadrados latinos mutuamente ortogonales. Con el conjunto completo
de $p-1$ cuadrados ortogonales se estudian hasta $p+1$ factores, pero se consumen los
$(p+1)(p-1)=p^2-1$ gl → hace falta una estimación **independiente** del error. No debe haber
interacciones entre los factores.

---

## 4-4 Diseños de bloques incompletos balanceados (BIBD)

### Cuándo se usa y construcción

- Cuando no caben todos los tratamientos en cada bloque (limitaciones del aparato, de las
  instalaciones o del tamaño físico del bloque): **bloques incompletos aleatorizados**.
- **BIBD** (*balanced incomplete block design*): cualquier par de tratamientos aparece junto el
  mismo número de veces; se usa cuando todas las comparaciones entre tratamientos son igualmente
  importantes.
- Construcción directa: $a$ tratamientos, bloques de tamaño $k<a$ → tomar $\binom{a}{k}$ bloques
  con todas las combinaciones. A menudo existe un BIBD con menos bloques (tablas en Fisher y
  Yates, Davies, Cochran y Cox).
- El orden de los tratamientos dentro de cada bloque se aleatoriza.

**Parámetros:**

| Símbolo | Significado |
|---|---|
| $a$ | número de tratamientos |
| $b$ | número de bloques |
| $k$ | tratamientos por bloque ($k<a$) |
| $r$ | veces que aparece cada tratamiento (réplicas) |
| $\lambda$ | veces que cada par de tratamientos aparece en un mismo bloque |
| $N$ | $N = ar = bk$ |

$$\lambda = \frac{r(k-1)}{a-1}\quad\text{(debe ser entero)}$$

Justificación: el tratamiento 1 está en $r$ bloques con $k-1$ compañeros en cada uno; esas
$r(k-1)$ posiciones deben contener a los otros $a-1$ tratamientos $\lambda$ veces cada uno:
$\lambda(a-1)=r(k-1)$. Si $a=b$ el diseño es **simétrico**.

### 4-4.1 Análisis estadístico (intrabloques)

**Modelo** (ec. 4-26): $y_{ij} = \mu+\tau_i+\beta_j+\varepsilon_{ij}$,
$\varepsilon_{ij}\sim\text{NID}(0,\sigma^2)$.

**Partición:** $SS_T = SS_{\text{Trat(ajustados)}} + SS_{\text{Bloques}} + SS_E$. El ajuste de
tratamientos es necesario porque cada tratamiento está en un conjunto distinto de $r$ bloques,
de modo que los totales sin ajustar $y_{i.}$ están contaminados por diferencias entre bloques.

$$SS_T = \sum_i\sum_j y_{ij}^2 - \frac{y_{..}^2}{N}\quad(4\text{-}27),\qquad
SS_{\text{Bloques}} = \frac{1}{k}\sum_{j=1}^b y_{.j}^2 - \frac{y_{..}^2}{N}\quad(4\text{-}28)$$

**Totales de tratamiento ajustados** (ec. 4-30), con $n_{ij}=1$ si el tratamiento $i$ está en el
bloque $j$ y 0 si no:

$$Q_i = y_{i.} - \frac{1}{k}\sum_{j=1}^b n_{ij}\,y_{.j},\qquad i=1,\dots,a;\qquad \sum_i Q_i = 0$$

$$SS_{\text{Trat(ajustados)}} = \frac{k\sum_{i=1}^a Q_i^2}{\lambda a}\quad(4\text{-}29),\qquad
SS_E = SS_T - SS_{\text{Trat(ajustados)}} - SS_{\text{Bloques}}\quad(4\text{-}31)$$

**Tabla ANOVA** (tabla 4-23):

| Fuente | SS | gl | MS | $F_0$ |
|---|---|---|---|---|
| Tratamientos (ajustados) | $k\sum Q_i^2/(\lambda a)$ | $a-1$ | $SS/(a-1)$ | $MS_{\text{Trat(aj)}}/MS_E$ |
| Bloques (sin ajuste) | $\frac{1}{k}\sum y_{.j}^2 - y_{..}^2/N$ | $b-1$ | $SS/(b-1)$ | |
| Error | por sustracción | $N-a-b+1$ | $SS_E/(N-a-b+1)$ | |
| Total | $\sum\sum y_{ij}^2 - y_{..}^2/N$ | $N-1$ | | |

**Contrastes y comparaciones múltiples** (factor fijo): los contrastes se forman con los
**totales ajustados** $Q_i$, no con $y_{i.}$:

$$SS_C = \frac{k\left(\sum_{i=1}^a c_i Q_i\right)^2}{\lambda a\sum_{i=1}^a c_i^2}$$

Efectos ajustados $\hat\tau_i = kQ_i/(\lambda a)$, con error estándar (ec. 4-32):

$$S = \sqrt{\frac{k\,MS_E}{\lambda a}}$$

**Evaluar los bloques:** partición alternativa
$SS_T = SS_{\text{Trat (sin ajuste)}} + SS_{\text{Bloques(ajustados)}} + SS_E$. Para un diseño
**simétrico** ($a=b$) hay fórmula simple (ecs. 4-33, 4-34):

$$Q'_j = y_{.j} - \frac{1}{r}\sum_{i=1}^a n_{ij}\,y_{i.},\qquad
SS_{\text{Bloques(ajustados)}} = \frac{r\sum_{j=1}^b (Q'_j)^2}{\lambda b}$$

Advertencia: $SS_T \neq SS_{\text{Trat(aj)}} + SS_{\text{Bloques(aj)}} + SS_E$, por la no
ortogonalidad de tratamientos y bloques.

#### Ejemplo 4-5 — Catalizadores (BIBD $a=4$, $b=4$, $k=3$, $r=3$, $\lambda=2$, $N=12$)

- 4 catalizadores, lotes de materia prima como bloques (cada lote alcanza para 3 corridas);
  respuesta: tiempo de reacción. Disposición (tabla 4-22): bloque 1 = {1,3,4}, bloque 2 =
  {1,2,3}, bloque 3 = {2,3,4}, bloque 4 = {1,2,4}.
- Totales: tratamientos $y_{i.}$ = 218, 214, 216, 222; bloques $y_{.j}$ = 221, 224, 207, 218;
  $y_{..}=870$; $\sum\sum y^2 = 63\,156$.
- $SS_T = 81.00$; $SS_{\text{Bloques}} = 55.00$.
- $Q_1=-9/3$, $Q_2=-7/3$, $Q_3=-4/3$, $Q_4=20/3$ →
  $SS_{\text{Trat(aj)}} = 3[(9/3)^2+(7/3)^2+(4/3)^2+(20/3)^2]/(2\cdot 4) = 22.75$; $SS_E=3.25$.
- $Q'_1=7/3$, $Q'_2=24/3$, $Q'_3=-31/3$, $Q'_4=0$ → $SS_{\text{Bloques(aj)}} = 66.08$;
  $SS_{\text{Trat (sin ajuste)}} = 11.67$.
- ANOVA (tablas 4-24 y 4-25):

| Fuente | SS | gl | MS | $F_0$ | Valor P |
|---|---|---|---|---|---|
| Tratamientos (ajustados) | 22.75 | 3 | 7.58 | 11.66 | 0.0107 |
| Tratamientos (sin ajuste) | 11.67 | 3 | | | |
| Bloques (sin ajuste) | 55.00 | 3 | | | |
| Bloques (ajustados) | 66.08 | 3 | 22.03 | 33.90 | 0.0010 |
| Error | 3.25 | 5 | 0.65 | | |
| Total | 81.00 | 11 | | | |

- Conclusión: el catalizador tiene efecto significativo sobre el tiempo de reacción.
- **Minitab GLM** (tabla 4-26): Catalyst Seq SS 11.667, Adj SS 22.750, Adj MS 7.583, F = 11.67,
  P = 0.011; Block Seq SS 66.083, Adj SS 66.083, Adj MS 22.028, F = 33.89, P = 0.001; Error
  3.250 (5 gl), Adj MS 0.650; Total 81.000. ("Adj SS" = sumas de cuadrados ajustadas.)
- **Tukey 95 %** (error estándar de la diferencia 0.6982):

| Comparación | Diferencia | IC inferior | IC superior | T | P ajustado |
|---|---|---|---|---|---|
| 2 − 1 | 0.2500 | −2.327 | 2.827 | 0.3581 | 0.9825 |
| 3 − 1 | 0.6250 | −1.952 | 3.202 | 0.8951 | 0.8085 |
| 4 − 1 | 3.6250 | 1.048 | 6.202 | 5.1918 | 0.0130 |
| 3 − 2 | 0.3750 | −2.202 | 2.952 | 0.5371 | 0.9462 |
| 4 − 2 | 3.3750 | 0.798 | 5.952 | 4.8338 | 0.0175 |
| 4 − 3 | 3.000 | 0.4228 | 5.577 | 4.297 | 0.0281 |

  El catalizador 4 difiere de los otros tres.

### 4-4.2 Estimación de mínimos cuadrados de los parámetros

Ecuaciones normales (ec. 4-35):

$$\mu:\; N\hat\mu + r\sum_i\hat\tau_i + k\sum_j\hat\beta_j = y_{..}$$
$$\tau_i:\; r\hat\mu + r\hat\tau_i + \sum_j n_{ij}\hat\beta_j = y_{i.}$$
$$\beta_j:\; k\hat\mu + \sum_i n_{ij}\hat\tau_i + k\hat\beta_j = y_{.j}$$

Con $\sum\hat\tau_i=\sum\hat\beta_j=0$: $\hat\mu=\bar y_{..}$. Eliminando los $\hat\beta_j$
(ec. 4-36) y usando $\sum_j n_{ij}n_{pj}=\lambda$ ($p\neq i$), $n_{pj}^2=n_{pj}$:

$$r(k-1)\hat\tau_i - \lambda\sum_{p\neq i}\hat\tau_p = kQ_i\quad(4\text{-}37)$$

y como $\sum_{p\neq i}\hat\tau_p=-\hat\tau_i$ y $r(k-1)=\lambda(a-1)$:

$$\lambda a\,\hat\tau_i = kQ_i\;\Rightarrow\; \hat\tau_i = \frac{kQ_i}{\lambda a},\qquad i=1,\dots,a\quad(4\text{-}39)$$

Ejemplo 4-5: $\hat\tau_1=-9/8$, $\hat\tau_2=-7/8$, $\hat\tau_3=-4/8$, $\hat\tau_4=20/8$.

### 4-4.3 Recuperación de información interbloques

- El análisis de 4-4.1 es **intrabloques**: elimina las diferencias entre bloques; todo contraste
  de tratamientos es una comparación dentro de bloques. Es válido con bloques fijos o aleatorios.
- Yates: si los $\beta_j$ son **variables aleatorias no correlacionadas con media 0 y varianza
  $\sigma_\beta^2$**, los totales de bloque aportan información adicional sobre los $\tau_i$
  (**análisis interbloques**).

**Modelo para los totales de bloque** (ec. 4-40):

$$y_{.j} = k\mu + \sum_{i=1}^a n_{ij}\tau_i + \Big(k\beta_j + \sum_{i=1}^a \varepsilon_{ij}\Big)$$

Minimizando $L=\sum_j\big(y_{.j}-k\mu-\sum_i n_{ij}\tau_i\big)^2$ se obtienen (ecs. 4-41 a 4-43):

$$\tilde\mu = \bar y_{..},\qquad
\tilde\tau_i = \frac{\sum_{j=1}^b n_{ij}\,y_{.j} - kr\,\bar y_{..}}{r-\lambda}$$

Los estimadores interbloques $\tilde\tau_i$ e intrabloques $\hat\tau_i$ no están
correlacionados; ambos son insesgados, con

$$V(\hat\tau_i) = \frac{k(a-1)}{\lambda a^2}\,\sigma^2\ \text{(intrabloques)},\qquad
V(\tilde\tau_i) = \frac{k(a-1)}{a(r-\lambda)}\,(\sigma^2 + k\sigma_\beta^2)\ \text{(interbloques)}$$

(En el libro, pág. 162, la segunda varianza aparece rotulada "intrabloques" y la ec. 4-44 escribe
$\hat\tau_i$ dos veces; son erratas: corresponden a interbloques y a $\tilde\tau_i$.)

**Estimador combinado** de varianza mínima insesgado: $\tau_i^* = \alpha_1\hat\tau_i + \alpha_2\tilde\tau_i$
con $\alpha_1 = u_1/(u_1+u_2)$, $\alpha_2=u_2/(u_1+u_2)$, $u_1 = 1/V(\hat\tau_i)$,
$u_2=1/V(\tilde\tau_i)$ (ponderaciones inversas a las varianzas). Simplificado (ec. 4-45):

$$\tau_i^* = \frac{kQ_i(\sigma^2+k\sigma_\beta^2) + \Big(\sum_{j} n_{ij}\,y_{.j} - kr\,\bar y_{..}\Big)\sigma^2}{(r-\lambda)\sigma^2 + \lambda a(\sigma^2+k\sigma_\beta^2)}$$

**Estimación de las varianzas:**

- $\hat\sigma^2 = MS_E$ (error intrabloques).
- Cuadrado medio de bloques ajustados, caso general (ec. 4-46):

$$MS_{\text{Bloques(ajustados)}} = \frac{\dfrac{k\sum_i Q_i^2}{\lambda a} + \sum_j\dfrac{y_{.j}^2}{k} - \sum_i\dfrac{y_{i.}^2}{r}}{b-1},\qquad
E[MS_{\text{Bloques(aj)}}] = \sigma^2 + \frac{a(r-1)}{b-1}\sigma_\beta^2$$

- Si $MS_{\text{Bloques(aj)}} > MS_E$ (ec. 4-47):

$$\hat\sigma_\beta^2 = \frac{[MS_{\text{Bloques(aj)}} - MS_E](b-1)}{a(r-1)}$$

  y si $MS_{\text{Bloques(aj)}}\le MS_E$, se toma $\hat\sigma_\beta^2=0$.

**Estimador combinado operativo** (ecs. 4-48a, 4-48b):

$$\tau_i^* = \begin{cases}
\dfrac{kQ_i(\hat\sigma^2+k\hat\sigma_\beta^2) + \Big(\sum_j n_{ij}\,y_{.j} - kr\,\bar y_{..}\Big)\hat\sigma^2}{(r-\lambda)\hat\sigma^2 + \lambda a(\hat\sigma^2+k\hat\sigma_\beta^2)}, & \hat\sigma_\beta^2>0\\[2ex]
\dfrac{y_{i.} - (1/a)\,y_{..}}{r}, & \hat\sigma_\beta^2 = 0
\end{cases}$$

**Ejemplo 4-5 (continuación):** $\sum_j n_{ij}y_{.j}$ = 663, 649, 652, 646; $\bar y_{..}=72.50$;
$r-\lambda=1$. $\hat\sigma^2 = 0.65$, $MS_{\text{Bloques(aj)}}=22.03$ →
$\hat\sigma_\beta^2 = (22.03-0.65)(3)/[4(3-1)] = 8.02$.

| Parámetro | Intrabloques | Interbloques | Combinada |
|---|---|---|---|
| $\tau_1$ | −1.12 | 10.50 | −1.09 |
| $\tau_2$ | −0.88 | −3.50 | −0.88 |
| $\tau_3$ | −0.50 | −0.50 | −0.50 |
| $\tau_4$ | 2.50 | −6.50 | 2.47 |

Las combinadas quedan muy cerca de las intrabloques porque la varianza de las interbloques es
relativamente grande.

---

## 4-5 Problemas (solo referencia)

Temas útiles para practicar o validar software: 4-1 a 4-7 y 4-13 (RCBD); 4-8, 4-9 (regresión y
estimación de parámetros); 4-10 (curvas OC); 4-11, 4-12, 4-26 (valores faltantes, aproximado y
exacto); 4-14 a 4-21 (cuadrados latinos, valor faltante, varios cuadrados); 4-22 a 4-25
(grecolatinos, hipercuadrado 5×5); 4-27 a 4-37 (BIBD, contrastes, análisis interbloques;
4-36: no existe BIBD con $a=8$, $r=8$, $k=4$, $b=16$); 4-38 (bloques incompletos extendidos,
$a<k<2a$, con $\lambda = 2r-b+\lambda^*$).

---

## Resumen de reglas prácticas

- Bloquear lo conocido y controlable; aleatorizar contra lo demás. No bloquear cuando se debe
  puede ocultar efectos reales (tabla 4-6: $F_0$ pasa de 14.44 a 1.70).
- No reportar la $F$ de bloques como prueba formal; usar $MS_{\text{Bloques}}/MS_E$ como guía.
- Revisar siempre residuales contra tratamientos, bloques y ajustados; un patrón curvo o
  desigual sugiere interacción bloque-tratamiento o escala incorrecta (probar logaritmo).
- Dato faltante: estimar con ec. 4-16 (RCBD) o 4-24 (latino) y restar 1 gl al error por cada
  dato; el análisis aproximado es liberal, el exacto usa la prueba general de regresión.
- Cuadrado latino/grecolatino: suponen ausencia total de interacción; pocos gl de error en
  tamaños pequeños → replicar, y analizar según cómo se replicó (casos 1–3).
- BIBD: verificar $N=ar=bk$ y $\lambda=r(k-1)/(a-1)$ entero; comparar tratamientos con los $Q_i$
  ajustados; las SS ajustadas de tratamientos y bloques no suman $SS_T$.
- Recuperación interbloques: solo con bloques aleatorios; aporta poco cuando
  $\hat\sigma_\beta^2$ es grande frente a $\hat\sigma^2$.
