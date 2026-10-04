# Capítulo 12 — Experimentos con factores aleatorios

> Montgomery, págs. 511–556

Convención de notación del capítulo: $a, b, c$ = niveles de $A, B, C$; $n$ = réplicas; $N$ = total
de observaciones; $F_{\alpha,\nu_1,\nu_2}$ y $\chi^2_{\alpha,\nu}$ son puntos porcentuales
**superiores** (área $\alpha$ a la derecha).

## Introducción: factor fijo vs. factor aleatorio (pág. 511)

- **Factor fijo**: los niveles usados son los de interés específico; el *espacio inferencial* es
  ese conjunto concreto de niveles (o, si es cuantitativo, la región cubierta, vía regresión).
- **Factor aleatorio**: los niveles se eligen al azar de una población grande de niveles
  posibles y las conclusiones se extienden a **toda la población de niveles**. El interés pasa
  de las medias de tratamientos a los **componentes de la varianza**.
- El cap. 13 (anidados y parcelas subdivididas) reutiliza todo lo de este capítulo.

---

## 12-1 Modelo con efectos aleatorios (un solo factor)

### Cuándo se usa y supuestos
Un factor con muchísimos niveles posibles, de los que se toman $a$ al azar. Se supone la
población de niveles infinita (o lo bastante grande); el caso de población finita se remite a
Bennett y Franklin, y Searle y Fawcett.

### Modelo (ec. 12-1)

$$y_{ij} = \mu + \tau_i + \varepsilon_{ij}, \qquad i = 1,\dots,a;\; j = 1,\dots,n$$

- $\tau_i \sim \text{NID}(0, \sigma_\tau^2)$, $\varepsilon_{ij} \sim \text{NID}(0, \sigma^2)$, $\tau_i$ y
  $\varepsilon_{ij}$ independientes.
- **No** aplica la restricción $\sum \tau_i = 0$ del modelo de efectos fijos (nota al pie, pág. 512).
- Varianza de una observación: $V(y_{ij}) = \sigma_\tau^2 + \sigma^2$ (los **componentes de la
  varianza**).

### Hipótesis (ec. 12-3)

$$H_0: \sigma_\tau^2 = 0 \qquad H_1: \sigma_\tau^2 > 0$$

No tiene sentido probar efectos de tratamientos individuales. $\sigma_\tau^2 = 0$ ⇒ todos los
tratamientos son idénticos.

### Análisis
- La identidad $SS_T = SS_{\text{Tratamientos}} + SS_E$ (ec. 12-2) y **todos los cálculos del
  ANOVA son idénticos al caso de efectos fijos**; cambia la interpretación.
- $SS_E/\sigma^2 \sim \chi^2_{N-a}$; bajo $H_0$, $SS_{\text{Trat}}/\sigma^2 \sim \chi^2_{a-1}$,
  independientes.
- Estadístico (ec. 12-4): $F_0 = MS_{\text{Tratamientos}}/MS_E \sim F_{a-1,\,N-a}$ bajo $H_0$.
  Se rechaza si $F_0 > F_{\alpha,\,a-1,\,N-a}$ (cola superior).
- Cuadrados medios esperados (ecs. 12-5, 12-6):

$$E(MS_{\text{Tratamientos}}) = \sigma^2 + n\sigma_\tau^2, \qquad E(MS_E) = \sigma^2$$

| Fuente | SS | gl | MS | E(MS) | $F_0$ |
|---|---|---|---|---|---|
| Tratamientos | $SS_{\text{Trat}}$ | $a-1$ | $MS_{\text{Trat}}$ | $\sigma^2 + n\sigma_\tau^2$ | $MS_{\text{Trat}}/MS_E$ |
| Error | $SS_E$ | $N-a$ | $MS_E$ | $\sigma^2$ | |
| Total | $SS_T$ | $N-1$ | | | |

### Estimación de los componentes: método del análisis de varianza
Igualar cuadrados medios observados con sus esperados y despejar (ecs. 12-7, 12-8):

$$\hat\sigma^2 = MS_E, \qquad \hat\sigma_\tau^2 = \frac{MS_{\text{Tratamientos}} - MS_E}{n}$$

Con tamaños de muestra desiguales se sustituye $n$ por (ec. 12-9):

$$n_0 = \frac{1}{a-1}\left[\sum_{i=1}^{a} n_i - \frac{\sum_{i=1}^{a} n_i^2}{\sum_{i=1}^{a} n_i}\right]$$

Propiedades: **no requiere normalidad**; los estimadores son los mejores estimadores cuadráticos
insesgados (mínima varianza entre las funciones cuadráticas insesgadas de las observaciones).

### Estimaciones negativas de un componente de varianza (pág. 514)
El método ANOVA puede dar $\hat\sigma_\tau^2 < 0$. Opciones:
1. Aceptarla como evidencia de que el componente verdadero es cero y fijarla en 0 (intuitivo,
   pero altera las propiedades estadísticas de las otras estimaciones).
2. Reestimar con un método que siempre dé estimaciones no negativas (ver 12-7.3, REML).
3. Tomarla como señal de que el modelo lineal supuesto es incorrecto y replantear el problema.

Referencias: Searle; Searle, Casella y McCulloch; Burdick y Graybill.

### Intervalos de confianza
**Para $\sigma^2$ (exacto, ec. 12-10)**, ya que $(N-a)MS_E/\sigma^2 \sim \chi^2_{N-a}$:

$$\frac{(N-a)MS_E}{\chi^2_{\alpha/2,\,N-a}} \le \sigma^2 \le \frac{(N-a)MS_E}{\chi^2_{1-\alpha/2,\,N-a}}$$

**Para $\sigma_\tau^2$: no hay intervalo exacto.** $\hat\sigma_\tau^2$ se distribuye como
$u_1\chi^2_{a-1} - u_2\chi^2_{N-a}$ con
$u_1 = (\sigma^2 + n\sigma_\tau^2)/[n(a-1)]$, $u_2 = \sigma^2/[n(N-a)]$, combinación lineal sin
forma cerrada. Aproximaciones: sección 12-7.

**Para la proporción $\sigma_\tau^2/(\sigma_\tau^2+\sigma^2)$ (exacto, diseño balanceado)**. Este
cociente —la fracción de la varianza de una observación debida a diferencias entre
tratamientos— es la **correlación intraclase** (Montgomery no usa ese nombre en la sección).
Base:

$$\frac{MS_{\text{Trat}}/(n\sigma_\tau^2 + \sigma^2)}{MS_E/\sigma^2} \sim F_{a-1,\,N-a}$$

Límites para $\sigma_\tau^2/\sigma^2$ (ecs. 12-13a, 12-13b):

$$L = \frac{1}{n}\left(\frac{MS_{\text{Trat}}}{MS_E}\cdot\frac{1}{F_{\alpha/2,\,a-1,\,N-a}} - 1\right), \qquad
U = \frac{1}{n}\left(\frac{MS_{\text{Trat}}}{MS_E}\cdot\frac{1}{F_{1-\alpha/2,\,a-1,\,N-a}} - 1\right)$$

Intervalo de $100(1-\alpha)\%$ (ec. 12-14):

$$\frac{L}{1+L} \le \frac{\sigma_\tau^2}{\sigma_\tau^2 + \sigma^2} \le \frac{U}{1+U}$$

Recordar $F_{1-\alpha/2,\,\nu_1,\,\nu_2} = 1/F_{\alpha/2,\,\nu_2,\,\nu_1}$.

### Ejemplo 12-1 (telares, resistencia del tejido)
4 telares elegidos al azar, 4 determinaciones por telar ($a = 4$, $n = 4$, $N = 16$); totales por
telar 390, 366, 383, 388; $y_{..} = 1527$. ANOVA (tabla 12-2):

| Fuente | SS | gl | MS | $F_0$ | Valor P |
|---|---|---|---|---|---|
| Telares | 89.19 | 3 | 29.73 | 15.68 | <0.001 |
| Error | 22.75 | 12 | 1.90 | | |
| Total | 111.94 | 15 | | | |

- $\hat\sigma^2 = 1.90$; $\hat\sigma_\tau^2 = (29.73 - 1.90)/4 = 6.96$;
  $\hat\sigma_y^2 = 1.90 + 6.96 = 8.86$. La mayor parte de la variabilidad es **entre** telares.
- IC 95 % de la proporción: $F_{0.025,3,12} = 4.47$, $F_{0.975,3,12} = 1/F_{0.025,12,3} = 1/14.34 = 0.070$
  ⇒ $L = 0.625$, $U = 54.883$ ⇒ $0.39 \le \sigma_\tau^2/(\sigma_\tau^2+\sigma^2) \le 0.98$. Intervalo
  ancho por la muestra pequeña, pero $\sigma_\tau^2$ claramente no es despreciable.
- Uso práctico (fig. 12-1): separar fuentes de variabilidad. Si se eliminara la variación entre
  telares, la varianza de salida bajaría de 8.86 a 1.90 y caería la fracción fuera de
  especificaciones.

---

## 12-2 Diseño factorial de dos factores aleatorios

### Modelo (ec. 12-15)

$$y_{ijk} = \mu + \tau_i + \beta_j + (\tau\beta)_{ij} + \varepsilon_{ijk}, \quad i=1..a,\; j=1..b,\; k=1..n$$

Todos los términos (salvo $\mu$) son variables aleatorias independientes, normales, de media 0
y varianzas $\sigma_\tau^2$, $\sigma_\beta^2$, $\sigma_{\tau\beta}^2$, $\sigma^2$. Entonces (ec. 12-16):

$$V(y_{ijk}) = \sigma_\tau^2 + \sigma_\beta^2 + \sigma_{\tau\beta}^2 + \sigma^2$$

Hipótesis: $H_0:\sigma_\tau^2 = 0$, $H_0:\sigma_\beta^2 = 0$, $H_0:\sigma_{\tau\beta}^2 = 0$.

### Análisis
$SS_A, SS_B, SS_{AB}, SS_E, SS_T$ se calculan igual que con efectos fijos; lo que cambia son los
denominadores de las pruebas, que se deducen de los cuadrados medios esperados (ec. 12-17):

| Fuente | gl | E(MS) | $F_0$ | Distribución de referencia |
|---|---|---|---|---|
| $A$ | $a-1$ | $\sigma^2 + n\sigma_{\tau\beta}^2 + bn\sigma_\tau^2$ | $MS_A/MS_{AB}$ (ec. 12-19) | $F_{a-1,\,(a-1)(b-1)}$ |
| $B$ | $b-1$ | $\sigma^2 + n\sigma_{\tau\beta}^2 + an\sigma_\beta^2$ | $MS_B/MS_{AB}$ (ec. 12-20) | $F_{b-1,\,(a-1)(b-1)}$ |
| $AB$ | $(a-1)(b-1)$ | $\sigma^2 + n\sigma_{\tau\beta}^2$ | $MS_{AB}/MS_E$ (ec. 12-18) | $F_{(a-1)(b-1),\,ab(n-1)}$ |
| Error | $ab(n-1)$ | $\sigma^2$ | | |

Todas las pruebas son de cola superior. **Regla general: los cuadrados medios esperados son
siempre la guía para construir los estadísticos de prueba**; aquí los efectos principales se
prueban contra la interacción, no contra el error.

Estimadores por el método ANOVA (ec. 12-21):

$$\hat\sigma^2 = MS_E,\quad
\hat\sigma_{\tau\beta}^2 = \frac{MS_{AB} - MS_E}{n},\quad
\hat\sigma_\beta^2 = \frac{MS_B - MS_{AB}}{an},\quad
\hat\sigma_\tau^2 = \frac{MS_A - MS_{AB}}{bn}$$

### Estudios de repetibilidad y reproducibilidad (R&R) del sistema de medición
Factorial piezas × operadores con réplicas, ambos aleatorios, orden de medición completamente
aleatorizado. Descomposición:

$$\sigma_y^2 = \sigma_\tau^2 + \sigma_\beta^2 + \sigma_{\tau\beta}^2 + \sigma^2$$

- $\sigma_\tau^2$: variabilidad entre piezas (producto).
- **Repetibilidad** = $\sigma^2$ (misma pieza, mismo operador).
- **Reproducibilidad** = $\sigma_\beta^2 + \sigma_{\tau\beta}^2$ (variabilidad adicional por el
  operador).
- Varianza del calibrador: $\sigma^2_{\text{calibrador}} = \sigma^2 + \sigma_\beta^2 + \sigma_{\tau\beta}^2$
  (repetibilidad + reproducibilidad). Lo deseable es que sea pequeña frente a $\sigma_\tau^2$: el
  instrumento distingue entre gradaciones del producto.

### Ejemplo 12-2 (R&R: 20 piezas × 3 operadores × 2 mediciones)
$a = 20$ piezas, $b = 3$ operadores, $n = 2$; ambos aleatorios. Minitab Balanced ANOVA (tabla 12-4):

| Fuente | gl | SS | MS | F | P | Término de error | E(MS) |
|---|---|---|---|---|---|---|---|
| Pieza | 19 | 1185.425 | 62.391 | 87.65 | 0.000 | Pieza×Op. | $\sigma^2 + 2\sigma_{\tau\beta}^2 + 6\sigma_\tau^2$ |
| Operador | 2 | 2.617 | 1.308 | 1.84 | 0.173 | Pieza×Op. | $\sigma^2 + 2\sigma_{\tau\beta}^2 + 40\sigma_\beta^2$ |
| Pieza×Operador | 38 | 27.050 | 0.712 | 0.72 | 0.861 | Error | $\sigma^2 + 2\sigma_{\tau\beta}^2$ |
| Error | 60 | 59.500 | 0.992 | | | | $\sigma^2$ |
| Total | 119 | 1274.592 | | | | | |

- Componentes: $\hat\sigma_\tau^2 = (62.39-0.71)/6 = 10.28$; $\hat\sigma_\beta^2 = (1.31-0.71)/40 = 0.015$;
  $\hat\sigma_{\tau\beta}^2 = (0.71-0.99)/2 = -0.14$ (**negativa**); $\hat\sigma^2 = 0.99$.
  (Minitab: 10.2798, 0.0149, −0.1399, 0.9917.)
- Conclusión: efecto de piezas grande, operadores quizá un efecto pequeño, sin interacción.
- **Modelo reducido** (se elimina la interacción por $P = 0.861$; $y_{ijk} = \mu + \tau_i + \beta_j + \varepsilon_{ijk}$),
  tabla 12-5: Error con 98 gl, SS = 86.550, MS = 0.883; Pieza F = 70.64 (P = 0.000);
  Operador F = 1.48 (P = 0.232); ambos probados contra el error. E(MS): pieza
  $\sigma^2 + 6\sigma_\tau^2$, operador $\sigma^2 + 40\sigma_\beta^2$. Componentes:
  $\hat\sigma_\tau^2 = (62.39-0.88)/6 = 10.25$; $\hat\sigma_\beta^2 = (1.31-0.88)/40 = 0.0108$;
  $\hat\sigma^2 = 0.88$ (Minitab: 10.2513, 0.0106, 0.8832).
- $\hat\sigma^2_{\text{calibrador}} = \hat\sigma^2 + \hat\sigma_\beta^2 = 0.88 + 0.0108 = 0.8908$, pequeña frente
  a la variabilidad del producto.
- El autor considera el modelo reducido un enfoque sencillo que suele funcionar casi tan bien
  como los métodos elaborados. La etiqueta "unrestricted model" de Minitab es irrelevante
  cuando todos los factores son aleatorios.

---

## 12-3 Modelo mixto con dos factores

$A$ fijo, $B$ aleatorio. Mismo modelo lineal (ec. 12-22):
$y_{ijk} = \mu + \tau_i + \beta_j + (\tau\beta)_{ij} + \varepsilon_{ijk}$.

### Modelo mixto restringido (el estándar del libro)
- $\tau_i$ fijos con $\sum_{i=1}^a \tau_i = 0$; $\beta_j \sim \text{NID}(0,\sigma_\beta^2)$;
  $\varepsilon_{ijk} \sim \text{NID}(0,\sigma^2)$.
- $(\tau\beta)_{ij}$ normal, media 0, varianza $[(a-1)/a]\,\sigma_{\tau\beta}^2$ (se define así para
  simplificar los E(MS)), con la **restricción** de sumar cero sobre el factor fijo:

$$\sum_{i=1}^{a} (\tau\beta)_{ij} = (\tau\beta)_{.j} = 0, \qquad j = 1,\dots,b$$

- Consecuencia: $\text{Cov}[(\tau\beta)_{ij}, (\tau\beta)_{i'j}] = -\frac{1}{a}\sigma_{\tau\beta}^2$ para $i \ne i'$;
  covarianza cero entre distintos $j$.

Cuadrados medios esperados (ec. 12-23) y pruebas:

| Fuente | gl | E(MS) restringido | $F_0$ | Referencia |
|---|---|---|---|---|
| $A$ (fijo) | $a-1$ | $\sigma^2 + n\sigma_{\tau\beta}^2 + \dfrac{bn\sum\tau_i^2}{a-1}$ | $MS_A/MS_{AB}$ | $F_{a-1,\,(a-1)(b-1)}$ |
| $B$ (aleatorio) | $b-1$ | $\sigma^2 + an\sigma_\beta^2$ | $MS_B/MS_E$ | $F_{b-1,\,ab(n-1)}$ |
| $AB$ | $(a-1)(b-1)$ | $\sigma^2 + n\sigma_{\tau\beta}^2$ | $MS_{AB}/MS_E$ | $F_{(a-1)(b-1),\,ab(n-1)}$ |
| Error | $ab(n-1)$ | $\sigma^2$ | | |

Hipótesis: $H_0:\tau_i = 0$; $H_0:\sigma_\beta^2 = 0$; $H_0:\sigma_{\tau\beta}^2 = 0$.

Estimadores:
- Efectos fijos (ec. 12-24): $\hat\mu = \bar y_{...}$, $\hat\tau_i = \bar y_{i..} - \bar y_{...}$.
- Componentes (ec. 12-25), descartando la ecuación del factor fijo:

$$\hat\sigma_\beta^2 = \frac{MS_B - MS_E}{an}, \qquad \hat\sigma_{\tau\beta}^2 = \frac{MS_{AB} - MS_E}{n}, \qquad \hat\sigma^2 = MS_E$$

  Procedimiento general para cualquier modelo mixto: eliminar los cuadrados medios que
  contienen factores fijos y resolver el sistema restante.
- **Error estándar de la media de un tratamiento del factor fijo** (para IC y comparaciones):

$$\left[\frac{\text{cuadrado medio usado para probar el efecto fijo}}{\text{n.º de observaciones en cada media}}\right]^{1/2} = \sqrt{\frac{MS_{AB}}{bn}}$$

  Es el del modelo de efectos fijos pero con $MS_{AB}$ en lugar de $MS_E$.

### Modelo mixto no restringido (alternativo)

$$y_{ijk} = \mu + \alpha_i + \gamma_j + (\alpha\gamma)_{ij} + \varepsilon_{ijk}$$

$\alpha_i$ fijos con $\sum\alpha_i = 0$; $\gamma_j$, $(\alpha\gamma)_{ij}$, $\varepsilon_{ijk}$ aleatorios no
correlacionados, media 0, varianzas $\sigma_\gamma^2$, $\sigma_{\alpha\gamma}^2$, $\sigma^2$. **No se impone
la restricción de suma cero** sobre la interacción. E(MS) (ec. 12-26):

| Fuente | E(MS) no restringido | $F_0$ |
|---|---|---|
| $A$ (fijo) | $\sigma^2 + n\sigma_{\alpha\gamma}^2 + \dfrac{bn\sum\alpha_i^2}{a-1}$ | $MS_A/MS_{AB}$ |
| $B$ (aleatorio) | $\sigma^2 + n\sigma_{\alpha\gamma}^2 + an\sigma_\gamma^2$ | $MS_B/MS_{AB}$ |
| $AB$ | $\sigma^2 + n\sigma_{\alpha\gamma}^2$ | $MS_{AB}/MS_E$ |
| Error | $\sigma^2$ | |

Único cambio en los estimadores (ec. 12-27): $\hat\sigma_\gamma^2 = (MS_B - MS_{AB})/(an)$.

### Restringido vs. no restringido

| Aspecto | Restringido | No restringido |
|---|---|---|
| Restricción sobre la interacción | $\sum_i (\tau\beta)_{ij} = 0$ | Ninguna |
| E(MS) del factor aleatorio | $\sigma^2 + an\sigma_\beta^2$ | incluye además $n\sigma_{\alpha\gamma}^2$ |
| Prueba del factor aleatorio | $MS_B/MS_E$ | $MS_B/MS_{AB}$ (más conservadora, pues en general $MS_{AB} > MS_E$) |
| Prueba del factor fijo | $MS_A/MS_{AB}$ | $MS_A/MS_{AB}$ |
| Prueba de la interacción | $MS_{AB}/MS_E$ | $MS_{AB}/MS_E$ |
| Covarianza entre dos observaciones del mismo nivel del factor aleatorio | positiva o negativa | solo positiva |

Relación entre parámetros: $\beta_j = \gamma_j + (\overline{\alpha\gamma})_{.j}$;
$(\tau\beta)_{ij} = (\alpha\gamma)_{ij} - (\overline{\alpha\gamma})_{.j}$ (el libro imprime signo "+" en
esta segunda relación, pág. 526; con "+" no se cumpliría la restricción de suma cero, así que
se anota como dudoso/errata probable);
$\sigma_\gamma^2 = \sigma_\beta^2 + \frac{1}{a}\sigma_{\alpha\gamma}^2$ (así impreso, pág. 526);
$\sigma_{\tau\beta}^2 = \sigma_{\alpha\gamma}^2$.

**Modelo de Scheffé** (ambos anteriores son casos especiales): $y_{ijk} = m_{ij} + \varepsilon_{ijk}$,
$m_{ij} = \mu + \tau_i + b_j + c_{ij}$, $E(m_{ij}) = \mu + \tau_i$, $\sum\tau_i = 0$, $c_{.j} = 0$; varianzas
y covarianzas de $b_j$, $c_{ij}$ expresadas mediante las de $m_{ij}$. Su análisis coincide con el
restringido, salvo que $MS_A/MS_{AB}$ no siempre sigue una $F$ bajo $H_0:\tau_i = 0$.

**Recomendación del autor**: la mayoría prefiere el **restringido** (más frecuente en la
literatura y algo más general); es el que se asume en el resto del libro. Si la estructura de
correlación de los componentes aleatorios no es grande, cualquiera sirve y difieren poco; con
correlaciones grandes puede convenir Scheffé. La elección debe dictarla los datos. Referencia:
Hocking. Ojo con el software: Minitab soporta ambos pero **por omisión usa el no restringido**.

### Ejemplo 12-3 (R&R con operadores fijos, modelo restringido)
Mismos datos del 12-2, pero solo hay 3 operadores (fijo) y las piezas son aleatorias. Tabla 12-6
(Minitab, modelo restringido), mismas SS/MS que la tabla 12-4:

| Fuente | F | P | Término de error | E(MS) |
|---|---|---|---|---|
| Pieza (aleat.) | 62.92 | 0.000 | Error | $\sigma^2 + 6\sigma^2_{\text{pieza}}$ |
| Operador (fijo) | 1.84 | 0.173 | Pieza×Op. | $\sigma^2 + 2\sigma^2_{\text{p×o}} + 40\,Q[2]$ |
| Pieza×Operador | 0.72 | 0.861 | Error | $\sigma^2 + 2\sigma^2_{\text{p×o}}$ |

$Q[2] = \sum\beta_j^2/(b-1)$ es la forma cuadrática del efecto fijo. Componentes:
$\hat\sigma^2_{\text{piezas}} = (62.39 - 0.99)/[(3)(2)] = 10.23$ (Minitab 10.2332);
$\hat\sigma^2_{\text{p×o}} = (0.71-0.99)/2 = -0.14$; $\hat\sigma^2 = 0.99$. De nuevo la interacción sale
negativa; ajustar el modelo reducido lleva a los mismos resultados del ejemplo 12-2.

### Ejemplo 12-4 (el mismo con el modelo no restringido)
Tabla 12-7: la pieza se prueba ahora contra la interacción, F = 87.65 (P = 0.000), con
E(MS) $= \sigma^2 + 2\sigma^2_{\text{p×o}} + 6\sigma^2_{\text{pieza}}$; operador F = 1.84 (P = 0.173), E(MS)
$= \sigma^2 + 2\sigma^2_{\text{p×o}} + Q[2]$; interacción F = 0.72 (P = 0.861). Componentes: pieza
10.2798, interacción −0.1399, error 0.9917. Conclusiones idénticas a las del restringido y
estimaciones muy similares.

---

## 12-4 Determinación del tamaño de la muestra con efectos aleatorios

Error tipo II en el modelo de un factor (ec. 12-28):

$$\beta = 1 - P\{F_0 > F_{\alpha,\,a-1,\,N-a} \mid \sigma_\tau^2 > 0\}$$

Bajo $H_1$, $F_0 = MS_{\text{Trat}}/MS_E$ sigue una **$F$ central** (no una no central como con efectos
fijos) con $a-1$ y $N-a$ gl —más precisamente, es un múltiplo de una $F$ central—, por eso
bastan tablas $F$ o las curvas de operación característica del apéndice, que grafican $\beta$
contra (ec. 12-29):

$$\lambda = \sqrt{1 + \frac{n\sigma_\tau^2}{\sigma^2}}$$

Curvas para $\alpha = 0.05$ y $0.01$. (El texto cita la "parte IV" del apéndice en la pág. 529 y la
"parte VI" en la pág. 530 y en la tabla 12-8 para las curvas de efectos aleatorios; la parte V
es la de efectos fijos. Verificar en el apéndice.)

$\lambda$ depende de $\sigma^2$ y $\sigma_\tau^2$ desconocidos: usar experiencia previa, o fijar el cociente
$\sigma_\tau^2/\sigma^2$ que interesa detectar.

**Criterio del incremento porcentual de la desviación estándar.** Si los tratamientos son
homogéneos la desviación estándar de una observación es $\sigma$; si difieren es
$\sqrt{\sigma^2 + \sigma_\tau^2}$. Con $P$ = incremento porcentual a partir del cual se quiere rechazar:

$$\frac{\sqrt{\sigma^2 + \sigma_\tau^2}}{\sigma} = 1 + 0.01P \;\Rightarrow\; \frac{\sigma_\tau^2}{\sigma^2} = (1+0.01P)^2 - 1$$

$$\lambda = \sqrt{1 + n[(1+0.01P)^2 - 1]} \quad \text{(ec. 12-30)}$$

**Parámetros de las curvas OC para dos factores (tabla 12-8):**

Modelo de efectos aleatorios:

| Factor | $\lambda$ | gl numerador | gl denominador |
|---|---|---|---|
| $A$ | $\sqrt{1 + \dfrac{bn\sigma_\tau^2}{\sigma^2 + n\sigma_{\tau\beta}^2}}$ | $a-1$ | $(a-1)(b-1)$ |
| $B$ | $\sqrt{1 + \dfrac{an\sigma_\beta^2}{\sigma^2 + n\sigma_{\tau\beta}^2}}$ | $b-1$ | $(a-1)(b-1)$ |
| $AB$ | $\sqrt{1 + \dfrac{n\sigma_{\tau\beta}^2}{\sigma^2}}$ | $(a-1)(b-1)$ | $ab(n-1)$ |

Modelo mixto (restringido):

| Factor | Parámetro | gl numerador | gl denominador | Parte del apéndice |
|---|---|---|---|---|
| $A$ (fijo) | $\Phi^2 = \dfrac{bn\sum_{i=1}^a \tau_i^2}{a[\sigma^2 + n\sigma_{\tau\beta}^2]}$ | $a-1$ | $(a-1)(b-1)$ | V |
| $B$ (aleatorio) | $\lambda = \sqrt{1 + \dfrac{an\sigma_\beta^2}{\sigma^2}}$ | $b-1$ | $ab(n-1)$ | VI |
| $AB$ | $\lambda = \sqrt{1 + \dfrac{n\sigma_{\tau\beta}^2}{\sigma^2}}$ | $(a-1)(b-1)$ | $ab(n-1)$ | VI |

### Ejemplo 12-5
$a = 5$ tratamientos al azar, $n = 6$, $\alpha = 0.05$, se quiere la potencia cuando $\sigma_\tau^2 = \sigma^2$:
$\lambda = \sqrt{1 + 6(1)} = 2.646$; con $a-1 = 4$ y $N-a = 25$ gl, $\beta \approx 0.20$ ⇒ potencia ≈ 0.80.

---

## 12-5 Reglas para los cuadrados medios esperados

**Alcance**: cualquier experimento **balanceado** factorial, anidado o factorial anidado. Quedan
excluidos los arreglos parcialmente balanceados (cuadrados latinos, bloques incompletos).
Aplicadas a un modelo mixto producen los E(MS) del **modelo restringido**. Alternativa siempre
válida: "fuerza bruta" (aplicar directamente el operador esperanza), laboriosa.

Principio para elegir el estadístico: cociente de cuadrados medios tal que el valor esperado
del **numerador** difiera del del **denominador** únicamente en el componente de varianza o
efecto fijo de interés.

**Regla 1.** El término de error $\varepsilon_{ij\ldots m}$ se escribe $\varepsilon_{(ij\ldots)m}$, con $m$ el
subíndice de la réplica. En dos factores: $\varepsilon_{ijk} \to \varepsilon_{(ij)k}$.

**Regla 2.** Además de $\mu$ y del error, el modelo contiene todos los efectos principales y las
interacciones que el experimentador suponga existentes. Con todas las interacciones entre $k$
factores hay $\binom{k}{2}$ dobles, $\binom{k}{3}$ triples, …, 1 de $k$ factores. Si un factor de un
término aparece entre paréntesis, no hay interacción entre ese factor y los demás del término
(anidamiento).

**Regla 3.** En cada término los subíndices se clasifican en: **vivos** (presentes y fuera de
paréntesis), **muertos** (presentes y dentro de paréntesis) y **ausentes** (están en el modelo
pero no en ese término). Ej.: en $(\tau\beta)_{ij}$, $i$ y $j$ vivos, $k$ ausente; en
$\varepsilon_{(ij)k}$, $k$ vivo, $i$ y $j$ muertos.

**Regla 4 (grados de libertad).** gl de un término = producto de los números de niveles de
cada subíndice muerto por (niveles − 1) de cada subíndice vivo. Ej.: $(\tau\beta)_{ij}$:
$(a-1)(b-1)$; $\varepsilon_{(ij)k}$: $ab(n-1)$.

**Regla 5.** Cada término tiene asociado un componente de varianza (efecto aleatorio) o un
factor fijo (efecto fijo). **Si una interacción contiene al menos un efecto aleatorio, toda la
interacción se considera aleatoria.** El componente de varianza lleva como subíndices las
letras griegas del efecto ($\sigma_\beta^2$, $\sigma_{\tau\beta}^2$). Un efecto fijo se representa por la
suma de cuadrados de sus parámetros dividida por sus gl, p. ej. $\sum_{i=1}^a \tau_i^2/(a-1)$.

**Regla 6 (tabla de E(MS)).** Construir una tabla con un renglón por cada componente del modelo
y una columna por cada subíndice; encima de cada subíndice anotar el número de niveles y si el
factor es fijo (F) o aleatorio (R). **Las réplicas siempre son aleatorias.**

- **a)** En cada renglón, escribir **1** si uno de los subíndices **muertos** del componente
  coincide con el subíndice de la columna.
- **b)** En cada renglón, si un subíndice (vivo) del componente coincide con el de la columna,
  escribir **0** si la columna es de un factor **fijo** y **1** si es de un factor **aleatorio**.
- **c)** En las posiciones que queden vacías, escribir el **número de niveles** de la columna.
- **d)** Para obtener el E(MS) de un componente: **cubrir** las columnas encabezadas por sus
  subíndices **vivos**; luego, en cada renglón que contenga **al menos los mismos subíndices**
  que el componente, multiplicar los números visibles y multiplicar ese producto por el factor
  fijo o componente de varianza correspondiente (regla 5). La suma de esas cantidades es el
  E(MS).

Ilustración (dos factores fijos, tabla 12-9):

| Factor | F, $a$, $i$ | F, $b$, $j$ | R, $n$, $k$ | E(MS) |
|---|---|---|---|---|
| $\tau_i$ | 0 | $b$ | $n$ | $\sigma^2 + \dfrac{bn\sum\tau_i^2}{a-1}$ |
| $\beta_j$ | $a$ | 0 | $n$ | $\sigma^2 + \dfrac{an\sum\beta_j^2}{b-1}$ |
| $(\tau\beta)_{ij}$ | 0 | 0 | $n$ | $\sigma^2 + \dfrac{n\sum\sum(\tau\beta)_{ij}^2}{(a-1)(b-1)}$ |
| $\varepsilon_{(ij)k}$ | 1 | 1 | 1 | $\sigma^2$ |

Para $E(MS_A)$: se cubre la columna $i$; renglones que contienen $i$: 1 (producto $bn$), 3
(producto $0\cdot n = 0$) y 4 (producto 1); el renglón 2 no contiene $i$.

Dos factores aleatorios (tabla 12-10):

| Factor | R, $a$, $i$ | R, $b$, $j$ | R, $n$, $k$ | E(MS) |
|---|---|---|---|---|
| $\tau_i$ | 1 | $b$ | $n$ | $\sigma^2 + n\sigma_{\tau\beta}^2 + bn\sigma_\tau^2$ |
| $\beta_j$ | $a$ | 1 | $n$ | $\sigma^2 + n\sigma_{\tau\beta}^2 + an\sigma_\beta^2$ |
| $(\tau\beta)_{ij}$ | 1 | 1 | $n$ | $\sigma^2 + n\sigma_{\tau\beta}^2$ |
| $\varepsilon_{(ij)k}$ | 1 | 1 | 1 | $\sigma^2$ |

Modelo mixto, $A$ fijo y $B$ aleatorio (tabla 12-11, versión restringida):

| Factor | F, $a$, $i$ | R, $b$, $j$ | R, $n$, $k$ | E(MS) |
|---|---|---|---|---|
| $\tau_i$ | 0 | $b$ | $n$ | $\sigma^2 + n\sigma_{\tau\beta}^2 + \dfrac{bn\sum\tau_i^2}{a-1}$ |
| $\beta_j$ | $a$ | 1 | $n$ | $\sigma^2 + an\sigma_\beta^2$ |
| $(\tau\beta)_{ij}$ | 0 | 1 | $n$ | $\sigma^2 + n\sigma_{\tau\beta}^2$ |
| $\varepsilon_{(ij)k}$ | 1 | 1 | 1 | $\sigma^2$ |

### Ejemplo 12-6 (tres factores aleatorios)
Modelo
$y_{ijkl} = \mu + \tau_i + \beta_j + \gamma_k + (\tau\beta)_{ij} + (\tau\gamma)_{ik} + (\beta\gamma)_{jk} + (\tau\beta\gamma)_{ijk} + \varepsilon_{ijkl}$.
Tabla 12-12:

| Factor | $i$ ($a$) | $j$ ($b$) | $k$ ($c$) | $l$ ($n$) | E(MS) |
|---|---|---|---|---|---|
| $\tau_i$ | 1 | $b$ | $c$ | $n$ | $\sigma^2 + cn\sigma_{\tau\beta}^2 + bn\sigma_{\tau\gamma}^2 + n\sigma_{\tau\beta\gamma}^2 + bcn\sigma_\tau^2$ |
| $\beta_j$ | $a$ | 1 | $c$ | $n$ | $\sigma^2 + cn\sigma_{\tau\beta}^2 + an\sigma_{\beta\gamma}^2 + n\sigma_{\tau\beta\gamma}^2 + acn\sigma_\beta^2$ |
| $\gamma_k$ | $a$ | $b$ | 1 | $n$ | $\sigma^2 + bn\sigma_{\tau\gamma}^2 + an\sigma_{\beta\gamma}^2 + n\sigma_{\tau\beta\gamma}^2 + abn\sigma_\gamma^2$ |
| $(\tau\beta)_{ij}$ | 1 | 1 | $c$ | $n$ | $\sigma^2 + n\sigma_{\tau\beta\gamma}^2 + cn\sigma_{\tau\beta}^2$ |
| $(\tau\gamma)_{ik}$ | 1 | $b$ | 1 | $n$ | $\sigma^2 + n\sigma_{\tau\beta\gamma}^2 + bn\sigma_{\tau\gamma}^2$ |
| $(\beta\gamma)_{jk}$ | $a$ | 1 | 1 | $n$ | $\sigma^2 + n\sigma_{\tau\beta\gamma}^2 + an\sigma_{\beta\gamma}^2$ |
| $(\tau\beta\gamma)_{ijk}$ | 1 | 1 | 1 | $n$ | $\sigma^2 + n\sigma_{\tau\beta\gamma}^2$ |
| $\varepsilon_{(ijk)l}$ | 1 | 1 | 1 | 1 | $\sigma^2$ |

Resultado clave: **no existe prueba exacta para ningún efecto principal** (no hay dos cuadrados
medios cuyo cociente aísle $bcn\sigma_\tau^2$, etc.). Sí hay pruebas exactas para las interacciones
dobles (contra $MS_{ABC}$) y la triple (contra $MS_E$). Solución: sección 12-6.

---

## 12-6 Pruebas F aproximadas

Problema: en factoriales con tres o más factores en modelos aleatorios o mixtos (y otros
diseños complejos) puede no existir estadístico exacto para ciertos efectos.

### Opción 1: suponer interacciones insignificantes
Si p. ej. $\sigma_{\tau\beta}^2 = \sigma_{\tau\gamma}^2 = \sigma_{\beta\gamma}^2 = 0$, aparecen pruebas exactas para los
efectos principales. Advertencias: debe haber algo en la naturaleza del proceso o conocimiento
previo sólido que lo justifique; no eliminar interacciones sin evidencia concluyente. Probar
primero las interacciones y luego fijar en cero las no significativas es práctica usada pero
**riesgosa**, porque cada decisión está sujeta a errores tipo I y II.

### Opción 2: agrupar (pooling) cuadrados medios
Si $F_0 = MS_{ABC}/MS_E$ no es significativo, ambos estiman $\sigma^2$ y pueden combinarse:

$$MS_{E'} = \frac{abc(n-1)MS_E + (a-1)(b-1)(c-1)MS_{ABC}}{abc(n-1) + (a-1)(b-1)(c-1)}$$

con $abc(n-1) + (a-1)(b-1)(c-1)$ gl. Riesgo: un error tipo II mete en el error un efecto real,
infla $MS_{E'}$ y dificulta detectar otros efectos. **Regla práctica del autor**:
- Si el $MS_E$ original tiene **6 o más gl**, no agrupar.
- Si tiene **menos de 6 gl**, agrupar solo si el $F$ del cuadrado medio a agrupar no es
  significativo con un $\alpha$ grande, p. ej. $\alpha = 0.25$.

### Opción 3: método de Satterthwaite
Se forman combinaciones lineales de cuadrados medios (ecs. 12-31, 12-32):

$$MS' = MS_r + \cdots + MS_s, \qquad MS'' = MS_u + \cdots + MS_v$$

elegidas de modo que $E(MS') - E(MS'')$ sea un múltiplo del efecto (parámetro o componente de
varianza) de la hipótesis nula. Estadístico (ec. 12-33):

$$F = \frac{MS'}{MS''} \;\dot\sim\; F_{p,\,q}$$

con grados de libertad (ecs. 12-34, 12-35):

$$p = \frac{(MS_r + \cdots + MS_s)^2}{MS_r^2/f_r + \cdots + MS_s^2/f_s}, \qquad
q = \frac{(MS_u + \cdots + MS_v)^2}{MS_u^2/f_u + \cdots + MS_v^2/f_v}$$

donde $f_i$ son los gl de $MS_i$. $p$ y $q$ no suelen ser enteros (interpolar en tablas $F$).

- Fundamento: numerador y denominador se distribuyen aproximadamente como múltiplos de
  ji-cuadradas, y como ningún cuadrado medio aparece en ambos, son independientes.
- Ejemplo de construcción (tres factores aleatorios, tabla 12-12), para $H_0:\sigma_\tau^2 = 0$:
  $MS' = MS_A + MS_{ABC}$, $MS'' = MS_{AB} + MS_{AC}$.
- **Cuidado con signos negativos** en las combinaciones. Gaylor y Hopper: si
  $MS' = MS_1 - MS_2$, la aproximación es razonable si

$$\frac{MS_1}{MS_2} > F_{0.025,\,f_2,\,f_1} \times F_{0.50,\,f_1,\,f_2} \quad\text{y}\quad f_1 \le 100,\; f_2 \ge f_1/2$$

### Ejemplo 12-7 (caída de presión en válvula de expansión de turbina)
$A$ = temperatura del gas (fijo, $a = 3$: 60, 75, 90 °F), $B$ = operador (aleatorio, $b = 4$),
$C$ = manómetro (aleatorio, $c = 3$), $n = 2$; $N = 72$. Modelo factorial completo de tres
factores, restringido. Tabla 12-14:

| Fuente | SS | gl | MS | E(MS) | $F_0$ | P |
|---|---|---|---|---|---|---|
| $A$ | 1023.36 | 2 | 511.68 | $\sigma^2 + bn\sigma_{\tau\gamma}^2 + cn\sigma_{\tau\beta}^2 + n\sigma_{\tau\beta\gamma}^2 + \dfrac{bcn\sum\tau_i^2}{a-1}$ | 2.22 | 0.17 |
| $B$ | 423.82 | 3 | 141.27 | $\sigma^2 + an\sigma_{\beta\gamma}^2 + acn\sigma_\beta^2$ | 4.05 | 0.07 |
| $C$ | 7.19 | 2 | 3.60 | $\sigma^2 + an\sigma_{\beta\gamma}^2 + abn\sigma_\gamma^2$ | 0.10 | 0.90 |
| $AB$ | 1211.97 | 6 | 202.00 | $\sigma^2 + n\sigma_{\tau\beta\gamma}^2 + cn\sigma_{\tau\beta}^2$ | 14.59 | <0.01 |
| $AC$ | 137.89 | 4 | 34.47 | $\sigma^2 + n\sigma_{\tau\beta\gamma}^2 + bn\sigma_{\tau\gamma}^2$ | 2.49 | 0.10 |
| $BC$ | 209.47 | 6 | 34.91 | $\sigma^2 + an\sigma_{\beta\gamma}^2$ | 1.63 | 0.17 |
| $ABC$ | 166.11 | 12 | 13.84 | $\sigma^2 + n\sigma_{\tau\beta\gamma}^2$ | 0.65 | 0.79 |
| Error | 770.50 | 36 | 21.40 | $\sigma^2$ | | |
| Total | 3950.32 | 71 | | | | |

- Denominadores exactos: $B$ y $C$ contra $MS_{BC}$; $AB$ y $AC$ contra $MS_{ABC}$; $BC$ y $ABC$
  contra $MS_E$. **Solo $A$ carece de prueba exacta.**
- Satterthwaite para $H_0:\tau_i = 0$: $MS' = MS_A + MS_{ABC} = 511.68 + 13.84 = 525.52$;
  $MS'' = MS_{AB} + MS_{AC} = 202.00 + 34.47 = 236.47$;
  $E(MS') - E(MS'') = bcn\sum\tau_i^2/(a-1)$; $F = 525.52/236.47 = 2.22$.
  $p = 525.52^2/(511.68^2/2 + 13.84^2/12) = 2.11 \approx 2$;
  $q = 236.47^2/(202.00^2/6 + 34.47^2/4) = 7.88 \approx 8$. $F_{0.05,2,8} = 4.46$ ⇒ no se rechaza;
  $P \approx 0.17$.
- Interpretación: $AB$ (temperatura × operador) grande, indicios de $AC$; las gráficas de
  interacción (fig. 12-2) sugieren efecto de temperatura grande con el operador 1 y el
  manómetro 3; los efectos principales de temperatura y operador pueden estar enmascarados por
  la interacción $AB$.
- **Minitab, modelo restringido (tabla 12-15)**: marca la prueba de $A$ como no exacta y usa una
  "prueba sintetizada" (Satterthwaite) con otro denominador:
  error MS $= MS_{AB} + MS_{AC} - MS_{ABC} = 222.63$, gl del error 6.97, $F = 2.30$, $P = 0.171$.
  Su valor esperado es $\sigma^2 + n\sigma_{\tau\beta\gamma}^2 + cn\sigma_{\tau\beta}^2 + bn\sigma_{\tau\gamma}^2$, también válido.
  Montgomery prefiere su combinación porque **no incluye cuadrados medios con signo negativo**.
  Resto de P: $B$ 0.069, $C$ 0.904, $AB$ 0.000, $AC$ 0.099, $BC$ 0.167, $ABC$ 0.788.
  Componentes de varianza: operador 5.909; manómetro −1.305; temp×operador 31.359;
  temp×manómetro 2.579; operador×manómetro 2.252; triple −3.780; error 21.403.
- **Minitab, modelo no restringido (tabla 12-16)**: ningún efecto principal tiene prueba exacta
  (E(MS) de $B$ incluye además $\sigma_{\tau\beta\gamma}^2$ y $\sigma_{\tau\beta}^2$; el de $C$, $\sigma_{\tau\beta\gamma}^2$ y
  $\sigma_{\tau\gamma}^2$). Pruebas sintetizadas:

  | Efecto | Error MS (síntesis) | gl error | F | P |
  |---|---|---|---|---|
  | Temperatura | $MS_{AB} + MS_{AC} - MS_{ABC} = 222.63$ | 6.97 | 2.30 | 0.171 |
  | Operador | $MS_{AB} + MS_{BC} - MS_{ABC} = 223.06$ | 7.09 | 0.63 | 0.616 |
  | Manómetro | $MS_{AC} + MS_{BC} - MS_{ABC} = 55.54$ | 5.98 | 0.06 | 0.938 |

  $BC$ se prueba ahora contra $MS_{ABC}$: $F = 2.52$, $P = 0.081$. Componentes: operador −4.544
  (negativo); manómetro −2.164; temp×operador 31.359; temp×manómetro 2.579; operador×manómetro
  3.512; triple −3.780; error 21.403. Conclusiones generales parecidas, salvo el gran cambio en
  el componente del operador. Como el manómetro no es significativo en ningún análisis, cabe
  reducir el modelo.

---

## 12-7 Temas adicionales sobre la estimación de los componentes de la varianza

### 12-7.1 Intervalos de confianza aproximados (Satterthwaite)

**Exacto** siempre que la función de interés sea el valor esperado de un solo cuadrado medio.
Para $\sigma^2$, con $f_E$ gl del error y $f_E MS_E/\sigma^2 \sim \chi^2_{f_E}$ (ec. 12-36):

$$\frac{f_E MS_E}{\chi^2_{\alpha/2,\,f_E}} \le \sigma^2 \le \frac{f_E MS_E}{\chi^2_{1-\alpha/2,\,f_E}}$$

**Aproximado** para un componente $\sigma_0^2$ que no es el valor esperado de un único cuadrado
medio. Se eligen $MS'$ y $MS''$ con $E(MS') - E(MS'') = k\sigma_0^2$ (ec. 12-37), y (ec. 12-38):

$$\hat\sigma_0^2 = \frac{MS' - MS''}{k} = \frac{1}{k}MS_r + \cdots + \frac{1}{k}MS_s - \frac{1}{k}MS_u - \cdots - \frac{1}{k}MS_v$$

$r\hat\sigma_0^2/\sigma_0^2$ sigue aproximadamente una $\chi^2_r$ con (ec. 12-39):

$$r = \frac{(\hat\sigma_0^2)^2}{\displaystyle\sum_{i=1}^{m}\frac{1}{k^2}\frac{MS_i^2}{f_i}}
= \frac{(MS_r + \cdots + MS_s - MS_u - \cdots - MS_v)^2}{\dfrac{MS_r^2}{f_r} + \cdots + \dfrac{MS_s^2}{f_s} + \dfrac{MS_u^2}{f_u} + \cdots + \dfrac{MS_v^2}{f_v}}$$

Intervalo aproximado de $100(1-\alpha)\%$ (ec. 12-40):

$$\frac{r\hat\sigma_0^2}{\chi^2_{\alpha/2,\,r}} \le \sigma_0^2 \le \frac{r\hat\sigma_0^2}{\chi^2_{1-\alpha/2,\,r}}$$

**Solo es utilizable si $\hat\sigma_0^2 > 0$.** $r$ casi nunca es entero (interpolar en la tabla
ji-cuadrada). Resultado general para $r$: Graybill.

#### Ejemplo 12-8
Modelo mixto del ejemplo 12-7; IC para $\sigma_{\tau\beta}^2$. $E(MS_{AB}) - E(MS_{ABC}) = cn\sigma_{\tau\beta}^2$, así
que $\hat\sigma_{\tau\beta}^2 = (MS_{AB} - MS_{ABC})/(cn)$. El libro calcula
$(134.91 - 19.26)/[(3)(2)] = 19.28$,
$r = (134.91-19.26)^2/[134.91^2/((2)(3)) + 19.26^2/((2)(3)(2))] = 4.36$, y con
$\chi^2_{0.025,r} = 11.58$, $\chi^2_{0.975,r} = 0.61$: $7.26 \le \sigma_{\tau\beta}^2 \le 137.81$ (95 %), consistente
con la prueba $F$ exacta significativa.

> Duda de exactitud: los valores $MS_{AB} = 134.91$ y $MS_{ABC} = 19.26$ usados en los ejemplos
> 12-8 y 12-9 (págs. 545–547) **no coinciden** con la tabla 12-14 ($MS_{AB} = 202.00$,
> $MS_{ABC} = 13.84$), con la que se obtendría $\hat\sigma_{\tau\beta}^2 = (202.00-13.84)/6 = 31.36$, que es
> lo que reporta Minitab (31.359). Al validar software, usar la tabla 12-14; las cifras del
> ejemplo sirven solo para seguir la mecánica.

### 12-7.2 Método de grandes muestras modificado (Graybill y Wang; Ting et al.)

Para componentes expresables como combinación lineal de cuadrados medios (ec. 12-41):

$$\hat\sigma_0^2 = \sum_{i=1}^{Q} c_i MS_i$$

Satterthwaite funciona bien cuando los gl de cada $MS_i$ son relativamente grandes y **todas las
$c_i$ son positivas**; este método es la alternativa, en especial con $c_i$ negativas.

**Todas las $c_i > 0$** — intervalo de $100(1-\alpha)\%$ (ec. 12-42):

$$\hat\sigma_0^2 - \sqrt{\sum_{i=1}^{Q} G_i^2 c_i^2 MS_i^2} \;\le\; \sigma_0^2 \;\le\; \hat\sigma_0^2 + \sqrt{\sum_{i=1}^{Q} H_i^2 c_i^2 MS_i^2}$$

$$G_i = 1 - \frac{1}{F_{\alpha,\,f_i,\,\infty}}, \qquad H_i = \frac{1}{F_{1-\alpha,\,f_i,\,\infty}} - 1$$

($F_{\alpha,f,\infty}$ equivale a $\chi^2_{\alpha,f}/f$.)

**Caso general con signos mixtos** (ec. 12-43):

$$\hat\sigma_0^2 = \sum_{i=1}^{P} c_i MS_i - \sum_{j=P+1}^{Q} c_j MS_j, \qquad c_i, c_j \ge 0$$

Límite de confianza **inferior** aproximado de $100(1-\alpha)\%$ (Ting et al., ec. 12-44):

$$L = \hat\sigma_0^2 - \sqrt{V_L}$$

$$V_L = \sum_{i=1}^{P} G_i^2 c_i^2 MS_i^2 + \sum_{j=P+1}^{Q} H_j^2 c_j^2 MS_j^2
+ \sum_{i=1}^{P}\sum_{j=P+1}^{Q} G_{ij}\, c_i c_j MS_i MS_j
+ \sum_{i=1}^{P-1}\sum_{t>i}^{P} G^*_{it}\, c_i c_t MS_i MS_t$$

$$G_i = 1 - \frac{1}{F_{\alpha,\,f_i,\,\infty}}, \qquad H_j = \frac{1}{F_{1-\alpha,\,f_j,\,\infty}} - 1, \qquad
G_{ij} = \frac{(F_{\alpha,\,f_i,\,f_j} - 1)^2 - G_i^2 F_{\alpha,\,f_i,\,f_j}^2 - H_j^2}{F_{\alpha,\,f_i,\,f_j}}$$

$$G^*_{it} = \left[\left(1 - \frac{1}{F_{\alpha,\,f_i+f_t,\,\infty}}\right)^2 \frac{(f_i+f_t)^2}{f_i f_t} - \frac{G_i^2 f_i}{f_t} - \frac{G_t^2 f_t}{f_i}\right](P-1) \;\text{ si } P > 1; \qquad G^*_{it} = 0 \text{ si } P = 1$$

Notas de lectura (pág. 546): en el tercer sumando de $V_L$ la impresión parece mostrar
$G_{ij}$ con un exponente; el ejemplo 12-9 lo usa **sin** elevar al cuadrado, que es lo anotado
aquí. En $G^*_{it}$ el último término aparece impreso como $G_i^2 f_t/f_i$; se anota $G_t^2$ por
simetría (ilegible/dudoso, pág. 546 — confirmar en Burdick y Graybill antes de usarlo con
$P > 1$). En la definición de $H_j$ el libro imprime el subíndice $f_i$.

El método se extiende a cocientes de componentes de varianza; referencia completa: Burdick y
Graybill.

#### Ejemplo 12-9
Límite inferior de 95 % para $\sigma_{\tau\beta}^2$ en el modelo del ejemplo 12-7:
$\hat\sigma_{\tau\beta}^2 = (MS_{AB} - MS_{ABC})/(cn) = 19.28$ (mismas cifras del ej. 12-8; ver la duda
anterior), $c_1 = c_2 = 1/6$, $f_1 = 6$, $f_2 = 12$, $P = 1$.
$G_1 = 1 - 1/F_{0.05,6,\infty} = 1 - 1/2.1 = 0.524$;
$H_2 = 1/F_{0.95,12,\infty} - 1 = 1/0.435 - 1 = 1.30$;
$G_{12} = [(3.00-1)^2 - (0.524)^2(3.00)^2 - (1.3)^2]/3.00 = -0.054$ (con $F_{0.05,6,12} = 3.00$);
$G^*_{1t} = 0$.
$V_L = (0.524)^2(1/6)^2(134.91)^2 + (1.3)^2(1/6)^2(19.26)^2 + (-0.054)(1/6)(1/6)(134.91)(19.26) = 152.36$;
$L = 19.28 - \sqrt{152.36} = 6.94$. Consistente con la prueba $F$ exacta.

### 12-7.3 Estimación de máxima verosimilitud y REML

- El método ANOVA es un **estimador de momentos**: directo y basado en cantidades familiares,
  pero puede dar estimaciones negativas y sus propiedades estadísticas no son las mejores.
- **Máxima verosimilitud**: elegir los parámetros que maximizan
  $L(\theta) = f(x_1;\theta)\cdot f(x_2;\theta)\cdots f(x_n;\theta)$, es decir, la probabilidad de los
  resultados muestrales bajo el modelo y la distribución del error supuestos. Referencia:
  Milliken y Johnson.
- Para el modelo aleatorio de dos factores, $V(y_{ijk}) = \sigma_y^2 = \sigma_\tau^2 + \sigma_\beta^2 + \sigma_{\tau\beta}^2 + \sigma^2$
  y (ec. 12-45):

| Caso | $\text{Cov}(y_{ijk}, y_{i'j'k'})$ |
|---|---|
| $i = i'$, $j = j'$, $k \ne k'$ | $\sigma_\tau^2 + \sigma_\beta^2 + \sigma_{\tau\beta}^2$ |
| $i = i'$, $j \ne j'$ | $\sigma_\tau^2$ |
| $i \ne i'$, $j = j'$ | $\sigma_\beta^2$ |
| $i \ne i'$, $j \ne j'$ | $0$ |

  Con $\mathbf{y}$ el vector $N \times 1$ ($N = abn$) y $\boldsymbol\Sigma$ su matriz de covarianza (el libro
  la escribe por bloques para $a = b = n = 2$), bajo normalidad conjunta:

$$L(\mu, \sigma_\tau^2, \sigma_\beta^2, \sigma_{\tau\beta}^2, \sigma^2) = \frac{1}{(2\pi)^{N/2}|\boldsymbol\Sigma|^{1/2}}
\exp\left[-\tfrac{1}{2}(\mathbf{y} - \mathbf{j}_N\mu)'\boldsymbol\Sigma^{-1}(\mathbf{y} - \mathbf{j}_N\mu)\right]$$

  ($\mathbf{j}_N$ = vector de unos). En la práctica se maximiza sujeto a componentes no negativos.
- **REML** (máxima verosimilitud restringida o residual): en esencia restringe las estimaciones
  de los componentes a valores **no negativos**; es la vía para evitar estimaciones negativas.
  Requiere software (SAS PROC MIXED, método REML).
- Matriz de covarianza de los parámetros aleatorios, todos mutuamente independientes
  (ec. 12-46), estructura simple (`TYPE=SIM`, valor por omisión, en el enunciado RANDOM):

$$\mathbf{G} = \begin{bmatrix} \sigma_\tau^2\mathbf{I} & 0 & 0 \\ 0 & \sigma_\beta^2\mathbf{I} & 0 \\ 0 & 0 & \sigma_{\tau\beta}^2\mathbf{I} \end{bmatrix}$$

- Lectura de la salida de PROC MIXED (tabla 12-17): parámetro de covarianza; cociente
  $\hat\sigma_i^2/\hat\sigma^2$; estimación REML; error estándar de muestras grandes
  $se(\hat\sigma_i^2) = \sqrt{V(\hat\sigma_i^2)}$; $Z = \hat\sigma_i^2/se(\hat\sigma_i^2)$ y su valor P; intervalo de
  teoría normal para muestras grandes

$$L = \hat\sigma_i^2 - Z_{\alpha/2}\,se(\hat\sigma_i^2), \qquad U = \hat\sigma_i^2 + Z_{\alpha/2}\,se(\hat\sigma_i^2)$$

  matriz asintótica de covarianza de las estimaciones; y medidas de ajuste (log-verosimilitud
  REML, AIC, criterio de Schwarz, $-2\log L$) para comparar modelos alternativos.

**REML para el ejemplo 12-2 (modelo aleatorio, tabla 12-17):**

| Parámetro | Cociente | Estimación | Error est. | Z | Pr > \|Z\| | Inferior 95 % | Superior 95 % |
|---|---|---|---|---|---|---|---|
| Operador | 0.01203539 | 0.01062922 | 0.03286000 | 0.32 | 0.7463 | −0.0538 | 0.0750 |
| Pieza | 11.60743820 | 10.25126446 | 3.37376878 | 3.04 | 0.0024 | 3.6388 | 16.8637 |
| Pieza×Operador | 0 | 0 | — | — | — | — | — |
| Residual | 1 | 0.88316339 | 0.12616620 | 7.00 | 0.0000 | 0.6359 | 1.1304 |

120 observaciones; log-verosimilitud REML −204.696; AIC −208.696; Schwarz −214.254;
$-2$ log-verosimilitud REML 409.3913. La estimación REML de la interacción es **cero**, y los
resultados coinciden muy de cerca con el modelo reducido ANOVA del ejemplo 12-2 (10.25,
0.0106, 0.88).

**REML para el ejemplo 12-3 (operador fijo, modelo mixto no restringido, tabla 12-18).**
Covarianzas de las observaciones (ec. 12-47): $\sigma_\beta^2 + \sigma_{\tau\beta}^2 + \sigma^2$ si
$i=i', j=j', k=k'$; $\sigma_\beta^2 + \sigma_{\tau\beta}^2$ si $i=i', j=j', k\ne k'$; $\sigma_\beta^2$ si $i\ne i', j=j'$; 0 si
$j \ne j'$. $\mathbf{G} = \text{diag}(\sigma_\beta^2\mathbf{I}, \sigma_{\tau\beta}^2\mathbf{I})$ (ec. 12-48). Resultados:
pieza 10.25126472 (error est. 3.37376895, Z = 3.04, P = 0.0024, IC 3.6388–16.8637);
pieza×operador 0; residual 0.88316337 (error est. 0.12616620, Z = 7.00, IC 0.6359–1.1304).
Prueba del efecto fijo operador (tipo III): gl 2 y 38, $F = 1.48$, $P = 0.2401$.
Log-verosimilitud REML −204.729; AIC −207.729; Schwarz −211.872; $-2\log L$ 409.4572.

---

## Resumen operativo

1. Los cálculos de SS, gl y MS **no cambian** al pasar de efectos fijos a aleatorios o mixtos;
   cambian los E(MS), los denominadores de las pruebas $F$ y lo que se estima.
2. Obtener siempre los E(MS) (reglas de 12-5) antes de formar cualquier $F$.
3. Dos factores aleatorios: $A$ y $B$ contra $MS_{AB}$; $AB$ contra $MS_E$.
4. Mixto restringido ($A$ fijo): $A$ contra $MS_{AB}$; $B$ y $AB$ contra $MS_E$. No restringido:
   $B$ contra $MS_{AB}$. Declarar cuál se usa y revisar el valor por omisión del software.
5. Medias del factor fijo en un modelo mixto: error estándar $\sqrt{MS_{AB}/(bn)}$.
6. Sin prueba exacta: Satterthwaite (preferir combinaciones sin signos negativos); agrupar solo
   con menos de 6 gl de error y con $\alpha = 0.25$.
7. Componente de varianza negativo: fijarlo en cero, ajustar el modelo reducido, o usar REML.
8. IC: exacto para $\sigma^2$ y para $\sigma_\tau^2/(\sigma_\tau^2+\sigma^2)$ en un factor; aproximado
   (Satterthwaite o grandes muestras modificado) para el resto.

## 12-8 Problemas (solo referencia)
Problemas 12-1 a 12-34 (págs. 552–556): un factor aleatorio (telares, lotes de calcio, hornos,
posiciones de obleas, blanqueadores), estudios R&R (12-9, 12-13, 12-28, 12-30), reanálisis de
problemas del cap. 5 con factores aleatorios o mixtos, deducción de E(MS) con 3 y 4 factores
(12-16 a 12-23), demostraciones (12-25: covarianza de la interacción restringida; 12-26:
insesgamiento del método ANOVA; 12-27: probabilidad de estimación negativa; 12-29: error
estándar de la media del factor fijo) e intervalos por Satterthwaite y grandes muestras
modificado (12-30 a 12-34).
