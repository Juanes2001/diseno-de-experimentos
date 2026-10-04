# Capítulo 13 — Diseños anidados y de parcelas subdivididas

> Montgomery, págs. 557–589

> **Nota sobre el escaneo:** las págs. 576–577 del libro **no están en el PDF** (de la 575 se
> salta a la 578). Contenían la tabla 13-16 (ANOVA del ejemplo del papel), el final de la
> sección 13-4 y las ecuaciones 13-16 y 13-17. Lo que aquí aparece sobre ese tramo está marcado
> expresamente: la tabla 13-16 se **recalculó** a partir de los datos de la tabla 13-14 (que sí
> se lee), y las ecs. 13-16/13-17 se reconstruyen solo por el contexto de las págs. 575 y 578.

Ambos diseños suelen incluir factores aleatorios, así que se apoyan en las reglas de cuadrados
medios esperados (CME) del capítulo 12 (algoritmo tabular; modelo mixto **restringido** salvo
que se diga lo contrario).

---

## 13-1 Diseño anidado de dos etapas

### Cuándo se usa

- Los niveles del factor $B$ son *similares pero no idénticos* en cada nivel de $A$: $B$ está
  **anidado** (jerárquico) bajo $A$. Ejemplo: 3 proveedores, 4 lotes de cada proveedor, 3
  determinaciones de pureza por lote. El lote 1 del proveedor 1 no tiene nada que ver con el
  lote 1 del proveedor 2.
- **Criterio práctico para distinguir anidado de cruzado:** si los niveles del factor pueden
  renumerarse arbitrariamente (lotes 1–4, 5–8, 9–12, fig. 13-2) el factor está anidado.
- Como no todos los niveles de $B$ aparecen con todos los de $A$, **no puede haber interacción
  $AB$**.

### 13-1.1 Análisis estadístico

**Modelo (ec. 13-1):**

$$y_{ijk}=\mu+\tau_i+\beta_{j(i)}+\varepsilon_{(ij)k},\qquad i=1..a,\; j=1..b,\; k=1..n$$

- $\tau_i$: efecto del nivel $i$ de $A$; $\beta_{j(i)}$: efecto del nivel $j$ de $B$ dentro del
  nivel $i$ de $A$; $\varepsilon_{(ij)k}\sim NID(0,\sigma^2)$ (las réplicas se consideran
  anidadas en la combinación $ij$).
- Diseño **balanceado**: mismo $b$ en cada nivel de $A$ y mismo $n$.
- Fijos: $\sum_i\tau_i=0$ y $\sum_j\beta_{j(i)}=0$ para cada $i$. Aleatorios:
  $\tau_i\sim NID(0,\sigma_\tau^2)$, $\beta_{j(i)}\sim NID(0,\sigma_\beta^2)$.

**Partición (ecs. 13-3, 13-4):** $SS_T=SS_A+SS_{B(A)}+SS_E$, con
$abn-1=(a-1)+a(b-1)+ab(n-1)$.

**Fórmulas de cálculo (ecs. 13-5 a 13-8):**

$$SS_A=\frac{1}{bn}\sum_{i}y_{i..}^2-\frac{y_{...}^2}{abn}$$

$$SS_{B(A)}=\frac1n\sum_i\sum_j y_{ij.}^2-\frac{1}{bn}\sum_i y_{i..}^2
=\sum_{i=1}^{a}\left[\frac1n\sum_{j=1}^{b}y_{ij.}^2-\frac{y_{i..}^2}{bn}\right]$$

$$SS_E=\sum_i\sum_j\sum_k y_{ijk}^2-\frac1n\sum_i\sum_j y_{ij.}^2,\qquad
SS_T=\sum_i\sum_j\sum_k y_{ijk}^2-\frac{y_{...}^2}{abn}$$

($SS_{B(A)}$ es la SS entre niveles de $B$ calculada dentro de cada nivel de $A$ y sumada.)

**Tabla ANOVA (tabla 13-2):**

| Fuente | SS | gl | MS |
|---|---|---|---|
| $A$ | $bn\sum(\bar y_{i..}-\bar y_{...})^2$ | $a-1$ | $MS_A$ |
| $B$ dentro de $A$ | $n\sum\sum(\bar y_{ij.}-\bar y_{i..})^2$ | $a(b-1)$ | $MS_{B(A)}$ |
| Error | $\sum\sum\sum(y_{ijk}-\bar y_{ij.})^2$ | $ab(n-1)$ | $MS_E$ |
| Total | $\sum\sum\sum(y_{ijk}-\bar y_{...})^2$ | $abn-1$ | |

**Cuadrados medios esperados (tabla 13-1):**

| $E(MS)$ | $A$ fijo, $B$ fijo | $A$ fijo, $B$ aleatorio | $A$ aleatorio, $B$ aleatorio |
|---|---|---|---|
| $E(MS_A)$ | $\sigma^2+\dfrac{bn\sum\tau_i^2}{a-1}$ | $\sigma^2+n\sigma_\beta^2+\dfrac{bn\sum\tau_i^2}{a-1}$ | $\sigma^2+n\sigma_\beta^2+bn\sigma_\tau^2$ |
| $E(MS_{B(A)})$ | $\sigma^2+\dfrac{n\sum\sum\beta_{j(i)}^2}{a(b-1)}$ | $\sigma^2+n\sigma_\beta^2$ | $\sigma^2+n\sigma_\beta^2$ |
| $E(MS_E)$ | $\sigma^2$ | $\sigma^2$ | $\sigma^2$ |

**Pruebas que se derivan:**

| Caso | $H_0$ sobre $A$ | Estadístico | $H_0$ sobre $B(A)$ | Estadístico |
|---|---|---|---|---|
| $A$, $B$ fijos | $\tau_i=0$ | $MS_A/MS_E$ | $\beta_{j(i)}=0$ | $MS_{B(A)}/MS_E$ |
| $A$ fijo, $B$ aleatorio | $\tau_i=0$ | $MS_A/MS_{B(A)}$ | $\sigma_\beta^2=0$ | $MS_{B(A)}/MS_E$ |
| $A$, $B$ aleatorios | $\sigma_\tau^2=0$ | $MS_A/MS_{B(A)}$ | $\sigma_\beta^2=0$ | $MS_{B(A)}/MS_E$ |

Distribuciones de referencia: $F_{a-1,\,a(b-1)}$ o $F_{a-1,\,ab(n-1)}$ para $A$ según el
denominador; $F_{a(b-1),\,ab(n-1)}$ para $B(A)$.

**Truco con software factorial:** $SS_{B(A)}=SS_B+SS_{AB}$ y sus gl se suman igual
($a(b-1)=(b-1)+(a-1)(b-1)$). Un programa de factoriales sirve para anidados agrupando el
"efecto principal" del factor anidado con sus interacciones con el factor que lo contiene.

**Minitab (Balanced ANOVA):** `Q[1]` denota $\sum\tau_i^2/(a-1)$; en el ej. 13-1,
$12\,Q[1]=6\sum\tau_i^2$.

### Ejemplo 13-1 — Pureza de materia prima (proveedores fijos, lotes aleatorios)

$a=3$ proveedores, $b=4$ lotes por proveedor, $n=3$ determinaciones; datos codificados
$y=\text{pureza}-93$. Totales de proveedor: $-5,\ 4,\ 14$; $y_{...}=13$.

| Fuente | SS | gl | MS | $E(MS)$ | $F_0$ | P |
|---|---|---|---|---|---|---|
| Proveedores | 15.06 | 2 | 7.53 | $\sigma^2+3\sigma_\beta^2+6\sum\tau_i^2$ | 0.97 | 0.42 |
| Lotes (dentro de proveedores) | 69.92 | 9 | 7.77 | $\sigma^2+3\sigma_\beta^2$ | 2.94 | 0.02 |
| Error | 63.33 | 24 | 2.64 | $\sigma^2$ | | |
| Total | 148.31 | 35 | | | | |

(Minitab: SS 15.056, 69.917, 63.333; P = 0.416 y 0.017.)

- Conclusión: los proveedores no difieren; **los lotes de un mismo proveedor sí**. La fuente de
  variabilidad es lote a lote, así que el remedio no es elegir proveedor sino trabajar con los
  proveedores para reducir su variabilidad entre lotes.
- **Análisis incorrecto como factorial** (tabla 13-5, modelo mixto): Proveedores 15.06 (2 gl,
  $F=1.02$, P 0.42); Lotes 25.64 (3 gl, MS 8.55, $F=3.24$, P 0.04); $S\times B$ 44.28 (6 gl,
  MS 7.38, $F=2.80$, P 0.03); error 63.33 (24 gl). Produce una "interacción" sin
  interpretación práctica y puede llevar a creer que el efecto proveedor está enmascarado.
  Verificación: $25.64+44.28=69.92=SS_{B(A)}$; $3+6=9$ gl.

### 13-1.2 Verificación del diagnóstico

Con las restricciones usuales, $\hat\mu=\bar y_{...}$, $\hat\tau_i=\bar y_{i..}-\bar y_{...}$,
$\hat\beta_{j(i)}=\bar y_{ij.}-\bar y_{i..}$, de modo que $\hat y_{ijk}=\bar y_{ij.}$ y

$$e_{ijk}=y_{ijk}-\bar y_{ij.}\qquad\text{(ec. 13-9)}$$

Diagnósticos habituales: probabilidad normal, atípicos, residuales vs. ajustados. La gráfica
de **residuales vs. niveles de $A$** (fig. 13-3b) es especialmente útil: verifica que la
variabilidad dentro de los niveles de $B$ sea la misma para todos los niveles de $A$ (en el
ejemplo, dispersión similar en los tres proveedores).

### 13-1.3 Componentes de la varianza

Caso totalmente aleatorio (ecs. 13-10 a 13-12):

$$\hat\sigma^2=MS_E,\qquad \hat\sigma_\beta^2=\frac{MS_{B(A)}-MS_E}{n},\qquad
\hat\sigma_\tau^2=\frac{MS_A-MS_{B(A)}}{bn}$$

Caso mixto ($A$ fijo, $B$ aleatorio): los efectos fijos se estiman con
$\hat\tau_i=\bar y_{i..}-\bar y_{...}$ y los componentes de varianza con las dos líneas
inferiores del ANOVA. Ej. 13-1: $\hat\tau=(-28/36,\,-1/36,\,29/36)$; $\hat\sigma^2=2.64$;
$\hat\sigma_\beta^2=(7.77-2.64)/3=1.71$.

### 13-1.4 Diseños anidados por etapas (escalonados, *staggered*)

- Problema: para tener gl razonables en la etapa superior se acaban con demasiados gl en las
  inferiores. Ej.: 10 lotes, 5 muestras/lote, 2 mediciones/muestra → 9 gl para lotes, 40 para
  muestras, 50 para mediciones.
- Solución: diseño anidado **no balanceado** escalonado (fig. 13-4): de cada lote solo dos
  muestras; una se mide dos veces y la otra una sola vez. Con $a$ lotes: $a-1$ gl para la
  etapa superior y **exactamente $a$ gl para cada etapa inferior**.
- Referencias del autor: Bainbridge; Smith y Beverly; Nelson; material suplementario.

---

## 13-2 Diseño anidado general de $m$ etapas

Ejemplo guía (fig. 13-5): 2 formulaciones de aleación; 3 hornadas por formulación; 2 lingotes
por hornada; 2 mediciones de dureza por lingote → anidado de tres etapas con dos réplicas.

**Modelo de tres etapas (ec. 13-13):**

$$y_{ijkl}=\mu+\tau_i+\beta_{j(i)}+\gamma_{k(ij)}+\varepsilon_{(ijk)l},\qquad
i=1..a,\ j=1..b,\ k=1..c,\ l=1..n$$

La variabilidad total se descompone en fuentes sucesivas (formulación, hornada a hornada,
prueba analítica; fig. 13-6): el diseño sirve para localizar la fuente dominante de variación
del proceso.

**ANOVA (tabla 13-7):**

| Fuente | SS | gl | MS |
|---|---|---|---|
| $A$ | $bcn\sum_i(\bar y_{i...}-\bar y_{....})^2$ | $a-1$ | $MS_A$ |
| $B$ (dentro de $A$) | $cn\sum_i\sum_j(\bar y_{ij..}-\bar y_{i...})^2$ | $a(b-1)$ | $MS_{B(A)}$ |
| $C$ (dentro de $B$) | $n\sum_i\sum_j\sum_k(\bar y_{ijk.}-\bar y_{ij..})^2$ | $ab(c-1)$ | $MS_{C(B)}$ |
| Error | $\sum\sum\sum\sum(y_{ijkl}-\bar y_{ijk.})^2$ | $abc(n-1)$ | $MS_E$ |
| Total | $\sum\sum\sum\sum(y_{ijkl}-\bar y_{....})^2$ | $abcn-1$ | |

(En el escaneo, las medias restadas en las filas $B(A)$ y $C(B)$ se leen con dificultad; la
forma anterior es la extensión directa de la tabla 13-2 que el propio texto indica.)

**CME con $A$ y $B$ fijos, $C$ aleatorio (tabla 13-8, algoritmo tabular):**

| Término | CME | Se prueba contra |
|---|---|---|
| $\tau_i$ | $\sigma^2+n\sigma_\gamma^2+\dfrac{bcn\sum\tau_i^2}{a-1}$ | $MS_{C(B)}$ |
| $\beta_{j(i)}$ | $\sigma^2+n\sigma_\gamma^2+\dfrac{cn\sum\sum\beta_{j(i)}^2}{a(b-1)}$ | $MS_{C(B)}$ |
| $\gamma_{k(ij)}$ | $\sigma^2+n\sigma_\gamma^2$ | $MS_E$ |
| $\varepsilon_{l(ijk)}$ | $\sigma^2$ | — |

Regla general: los estadísticos de prueba se determinan siempre a partir de los CME; para otros
supuestos fijo/aleatorio se repite el algoritmo (problemas 13-7 y 13-9 piden los casos
$A$ fijo–$B$,$C$ aleatorios y todo aleatorio).

---

## 13-3 Diseños con factores anidados y factoriales

Diseños **factoriales-anidados**: algunos factores cruzados y otros anidados.

### Ejemplo 13-2 — Tiempo de ensamblaje

3 dispositivos (*fixtures*, $F$, fijo), 2 arreglos del sitio de trabajo (*layouts*, $L$,
fijo), 4 operadores (aleatorios) **distintos para cada arreglo** → operadores anidados en
arreglos, $O(L)$; dispositivos y arreglos cruzados; 2 réplicas; orden aleatorio; 48
observaciones. Modelo mixto.

**Modelo (ec. 13-14):**

$$y_{ijkl}=\mu+\tau_i+\beta_j+\gamma_{k(j)}+(\tau\beta)_{ij}+(\tau\gamma)_{ik(j)}+\varepsilon_{(ijk)l},
\quad i=1,2,3;\ j=1,2;\ k=1..4;\ l=1,2$$

No existen $L\times O$ ni $F\times L\times O$ (los operadores no se cruzan con los arreglos).

**CME (tabla 13-10, modelo restringido):**

| Término | CME | Denominador de $F$ |
|---|---|---|
| $\tau_i$ (dispositivo) | $\sigma^2+2\sigma_{\tau\gamma}^2+8\sum\tau_i^2$ | $MS_{FO(L)}$ |
| $\beta_j$ (arreglo) | $\sigma^2+6\sigma_\gamma^2+24\sum\beta_j^2$ | $MS_{O(L)}$ |
| $\gamma_{k(j)}$ (operador en arreglo) | $\sigma^2+6\sigma_\gamma^2$ | $MS_E$ |
| $(\tau\beta)_{ij}$ | $\sigma^2+2\sigma_{\tau\gamma}^2+4\sum\sum(\tau\beta)_{ij}^2$ | $MS_{FO(L)}$ |
| $(\tau\gamma)_{ik(j)}$ | $\sigma^2+2\sigma_{\tau\gamma}^2$ | $MS_E$ |
| $\varepsilon_{(ijk)l}$ | $\sigma^2$ | — |

**ANOVA (tabla 13-11; Minitab en tabla 13-12):**

| Fuente | SS | gl | MS | $F_0$ | P |
|---|---|---|---|---|---|
| Dispositivos ($F$) | 82.80 | 2 | 41.40 | 7.54 | 0.01 (0.008) |
| Arreglos ($L$) | 4.08 | 1 | 4.09 | 0.34 | 0.58 |
| Operadores dentro de arreglos, $O(L)$ | 71.91 | 6 | 11.99 | 5.15 | <0.01 (0.002) |
| $FL$ | 19.04 | 2 | 9.52 | 1.73 | 0.22 |
| $FO(L)$ | 65.84 | 12 | 5.49 | 2.36 | 0.04 |
| Error | 56.00 | 24 | 2.33 | | |
| Total | 299.67 | 47 | | | |

- Totales de dispositivo: 404, 447, 401 → usar dispositivos 1 o 3. Arreglo sin efecto
  apreciable. Operadores difieren y hay interacción dispositivo × operador (algunos operadores
  rinden más con ciertos dispositivos → capacitación).
- Componentes de varianza (restringido): $\hat\sigma_\gamma^2=1.609$,
  $\hat\sigma_{\tau\gamma}^2=1.576$, $\hat\sigma^2=2.333$.
- **Modelo no restringido (tabla 13-13):** cambia la prueba de $O(L)$: su denominador pasa a
  ser $MS_{FO(L)}$ (12 gl) en lugar de $MS_E$ → $F=2.18$, P = 0.117 (antes 5.14, P 0.002);
  $\hat\sigma_\gamma^2=1.083$. Las demás líneas no cambian. (El párrafo de la pág. 573 describe
  los denominadores de forma confusa —menciona "arreglo × dispositivos, 2 gl"—; la salida de
  Minitab de la tabla 13-13 indica como término de error de `Operator(Layout)` el término 5,
  `Fixture*Operator(Layout)`.) Las conclusiones prácticas no cambian.

**Con un programa factorial** (tratando $F$, $O$, $L$ como tres factores cruzados):

| Análisis factorial | gl | Análisis factorial-anidado | gl |
|---|---|---|---|
| $SS_F$ | 2 | $SS_F$ | 2 |
| $SS_L$ | 1 | $SS_L$ | 1 |
| $SS_{FL}$ | 2 | $SS_{FL}$ | 2 |
| $SS_O$, $SS_{LO}$ | 3, 3 | $SS_{O(L)}=SS_O+SS_{LO}$ | 6 |
| $SS_{FO}$, $SS_{FOL}$ | 6, 6 | $SS_{FO(L)}=SS_{FO}+SS_{FOL}$ | 12 |
| $SS_E$ | 24 | $SS_E$ | 24 |
| $SS_T$ | 47 | $SS_T$ | 47 |

---

## 13-4 Diseño de parcelas subdivididas (*split-plot*)

### Cuándo se usa

Factorial en el que **no es posible aleatorizar completamente el orden de las corridas**
porque un factor es difícil o costoso de cambiar (o se aplica a unidades experimentales
grandes) y el otro es fácil de cambiar (unidades pequeñas). Equivale a dos experimentos
superpuestos, aplicados en momentos distintos.

### Ejemplo guía — Resistencia a la tensión del papel (tabla 13-14)

- Factor $A$: 3 métodos de preparación de la pulpa. Factor $B$: 4 temperaturas de cocción
  (200, 225, 250, 275 °F). 3 réplicas, una por día (días = bloques), 12 corridas por día.
- Ejecución real: cada día se prepara un lote de pulpa con un método, se divide en 4 muestras
  y cada muestra se cuece a una temperatura; se repite con los otros dos métodos.
- Un factorial completamente aleatorizado requeriría 36 lotes de pulpa; el de parcelas
  subdivididas requiere solo 9 (3 por bloque).

### Terminología y construcción

1. Cada réplica/bloque se divide en $a$ **parcelas completas**; a ellas se asignan al azar los
   niveles del factor $A$ = **tratamiento principal o de parcela completa**.
2. Cada parcela completa se divide en $b$ **subparcelas**; a ellas se asignan al azar los
   niveles de $B$ = **tratamiento de subparcela** (subtratamiento).
3. Hay dos aleatorizaciones independientes → **dos términos de error** (parcela completa y
   subparcela).

- Cualquier factor no controlado que cambie al cambiar de parcela completa queda **confundido**
  con el tratamiento principal. Por eso: **asignar a las subparcelas el factor de mayor
  interés**, si es posible (se prueba con más precisión y más gl).

### Modelo (ec. 13-15)

$$y_{ijk}=\mu+\tau_i+\beta_j+(\tau\beta)_{ij}+\gamma_k+(\tau\gamma)_{ik}+(\beta\gamma)_{jk}+(\tau\beta\gamma)_{ijk}+\varepsilon_{ijk},
\quad i=1..r,\ j=1..a,\ k=1..b$$

| Parte | Término | Significado |
|---|---|---|
| Parcela completa | $\tau_i$ | réplicas (bloques) |
| | $\beta_j$ | tratamiento principal $A$ |
| | $(\tau\beta)_{ij}$ | **error de la parcela completa** = réplicas × $A$ |
| Subparcela | $\gamma_k$ | tratamiento de subparcela $B$ |
| | $(\tau\gamma)_{ik}$ | réplicas × $B$ |
| | $(\beta\gamma)_{jk}$ | interacción $AB$ |
| | $(\tau\beta\gamma)_{ijk}$ | **error de la subparcela** = réplicas × $AB$ |

Las sumas de cuadrados se calculan como en un **factorial de tres factores (réplicas, $A$,
$B$) sin réplicas**.

### Cuadrados medios esperados (tabla 13-15; réplicas aleatorias, $A$ y $B$ fijos)

| | Término | CME | gl |
|---|---|---|---|
| Parcela completa | $\tau_i$ | $\sigma^2+ab\sigma_\tau^2$ | $r-1$ |
| | $\beta_j$ | $\sigma^2+b\sigma_{\tau\beta}^2+\dfrac{rb\sum\beta_j^2}{a-1}$ | $a-1$ |
| | $(\tau\beta)_{ij}$ | $\sigma^2+b\sigma_{\tau\beta}^2$ | $(r-1)(a-1)$ |
| Subparcela | $\gamma_k$ | $\sigma^2+a\sigma_{\tau\gamma}^2+\dfrac{ra\sum\gamma_k^2}{b-1}$ | $b-1$ |
| | $(\tau\gamma)_{ik}$ | $\sigma^2+a\sigma_{\tau\gamma}^2$ | $(r-1)(b-1)$ |
| | $(\beta\gamma)_{jk}$ | $\sigma^2+\sigma_{\tau\beta\gamma}^2+\dfrac{r\sum\sum(\beta\gamma)_{jk}^2}{(a-1)(b-1)}$ | $(a-1)(b-1)$ |
| | $(\tau\beta\gamma)_{ijk}$ | $\sigma^2+\sigma_{\tau\beta\gamma}^2$ | $(r-1)(a-1)(b-1)$ |
| | $\varepsilon_{(ijk)h}$ | $\sigma^2$ (no estimable) | 0 |

### Pruebas

| Efecto | Estadístico | Referencia |
|---|---|---|
| $A$ (parcela completa) | $MS_A/MS_{\text{Rép}\times A}$ | $F_{a-1,\,(r-1)(a-1)}$ |
| $B$ (subparcela) | $MS_B/MS_{\text{Rép}\times B}$ | $F_{b-1,\,(r-1)(b-1)}$ |
| $AB$ | $MS_{AB}/MS_{\text{Rép}\times AB}$ | $F_{(a-1)(b-1),\,(r-1)(a-1)(b-1)}$ |

No hay prueba para réplicas (bloques) ni para réplicas × $B$.

### ANOVA del ejemplo del papel (tabla 13-16)

> La tabla 13-16 está en la pág. 576, **ausente del escaneo**. Los valores siguientes se
> **recalcularon** con los datos de la tabla 13-14 siguiendo exactamente el modelo 13-15 y las
> pruebas de la tabla 13-15 (sirven igualmente para validar software).

| Fuente | SS | gl | MS | $F_0$ |
|---|---|---|---|---|
| Réplicas (bloques) | 77.56 | 2 | 38.78 | — |
| Método de preparación ($A$) | 128.39 | 2 | 64.19 | 7.08 |
| Error de parcela completa (réplicas × $A$) | 36.28 | 4 | 9.07 | |
| Temperatura ($B$) | 434.08 | 3 | 144.69 | 42.01 |
| Réplicas × $B$ | 20.67 | 6 | 3.44 | |
| $AB$ | 75.17 | 6 | 12.53 | 2.96 |
| Error de subparcela (réplicas × $AB$) | 50.83 | 12 | 4.24 | |
| Total | 822.97 | 35 | | |

Lectura: $A$ con $F_{2,4}=7.08$ (≈ nivel 5 %); $B$ con $F_{3,6}=42.0$ (muy significativo);
$AB$ con $F_{6,12}=2.96$ (≈ nivel 5 %). Valores P exactos del libro: no leídos (pág. 576
faltante).

### Resto de la sección (págs. 576–578)

- **(No leído, págs. 576–577 faltantes.)** Por el contexto de las págs. 575, 578 y 13-5.1, ese
  tramo introduce: (i) un modelo alternativo de parcelas subdivididas (ec. 13-16) en el que el
  error de parcela completa aparece como un término propio ($\theta$) y las interacciones con
  réplicas de la parte de subparcela se agrupan en un único error de subparcela —la ec. 13-19
  se declara "consistente con la ecuación 13-16"—; y (ii) la discusión de qué ocurre cuando un
  factorial se corre con una restricción de aleatorización no reconocida, con un modelo
  (ec. 13-17, forma exacta no verificada) que tiene dos componentes de error de varianzas
  $\sigma_\theta^2$ y $\sigma_\phi^2$. Verificar contra el libro físico si se necesita la forma
  literal.
- **Ecs. 13-18 (sí leídas, pág. 578)** — CME cuando hay un error de restricción no reconocido
  (situación análoga a un **submuestreo**, Ostle), $A$ y $B$ fijos:

$$E(MS_A)=\sigma_\theta^2+n\sigma_\phi^2+\frac{bn\sum\tau_i^2}{a-1},\quad
E(MS_B)=\sigma_\theta^2+n\sigma_\phi^2+\frac{an\sum\beta_j^2}{b-1}$$

$$E(MS_{AB})=\sigma_\theta^2+n\sigma_\phi^2+\frac{n\sum\sum(\tau\beta)_{ij}^2}{(a-1)(b-1)},\qquad
E(MS_E)=\sigma_\theta^2$$

  Consecuencia: **no hay prueba para los efectos principales salvo que la interacción sea
  despreciable**; es la misma situación que un ANOVA de dos factores con una observación por
  celda. Si ambos factores son aleatorios, los efectos principales se prueban contra $AB$; si
  solo uno es aleatorio, el fijo se prueba contra $AB$.
- **Advertencia del autor:** si en un factorial resultan significativos *todos* los efectos
  principales e interacciones, revisar **cómo se corrió realmente el experimento**; puede haber
  restricciones de aleatorización no consideradas y los datos no deberían analizarse como un
  factorial.

---

## 13-5 Otras variantes del diseño de parcelas subdivididas

### 13-5.1 Parcelas subdivididas con más de dos factores

La parcela completa y/o la subparcela pueden tener estructura factorial propia.

**Ejemplo (horno de oxidación de obleas, fig. 13-7):** $2^4$ con 2 réplicas (32 ensayos).
$A$ = temperatura y $B$ = flujo de gas son difíciles de cambiar → parcela completa (4
combinaciones por réplica); $C$ = tiempo y $D$ = posición de la oblea son fáciles → un $2^2$
en orden aleatorio dentro de cada parcela completa. Solo 4 cambios de $A$, $B$ por réplica (8
en total).

**Modelo (ec. 13-19):** $\tau_i$ réplica; $\beta_j,\gamma_k,(\beta\gamma)_{jk}$ efectos de
parcela completa; $\theta_{ijk}$ **error de parcela completa**; $\delta_l,\lambda_m$ efectos
principales de subparcela; todas las demás interacciones entre los cuatro factores;
$\varepsilon_{ijklm}$ **error de subparcela**.

**ANOVA abreviado (tabla 13-17; réplicas aleatorias, factores fijos; las mayúsculas en el CME
denotan el término fijo correspondiente):**

| Fuente | gl | CME |
|---|---|---|
| Réplicas ($\tau_i$) | 1 | $\sigma_\varepsilon^2+16\sigma_\tau^2$ |
| $A$, $B$, $AB$ | 1 c/u | $\sigma_\varepsilon^2+8\sigma_\theta^2+(\text{efecto})$ |
| Error de parcela completa ($\theta_{ijk}$) | 3 | $\sigma_\varepsilon^2+8\sigma_\theta^2$ |
| $C$, $D$, $CD$, $AC$, $BC$, $AD$, $BD$, $ABC$, $ABD$, $ACD$, $BCD$, $ABCD$ | 1 c/u | $\sigma_\varepsilon^2+(\text{efecto})$ |
| Error de subparcela ($\varepsilon_{ijklm}$) | 12 | $\sigma_\varepsilon^2$ |
| Total | 31 | |

(El CME de réplicas se lee en el escaneo como $\sigma_\varepsilon^2+16\sigma_\tau^2$, tal cual
está impreso.)

- **Regla:** efectos principales e interacción *de parcela completa* ($A$, $B$, $AB$) → contra
  el error de parcela completa; **factores de subparcela y todas las demás interacciones**
  (incluidas las mixtas parcela × subparcela) → contra el error de subparcela.
- Si algún factor es aleatorio cambian las pruebas; puede no existir $F$ exacta → procedimiento
  de **Satterthwaite** (cap. 12).
- Estos experimentos tienden a ser grandes, pero la estructura *split-plot* facilita correrlos;
  puede reducirse el tamaño con un **factorial fraccionado** en los factores.

### 13-5.2 Parcelas con doble subdivisión (*split-split-plot*)

Dos niveles de restricción de aleatorización dentro de cada réplica.

**Ejemplo 13-3 — Absorción de cápsulas de antibiótico:** 3 técnicos ($A$), 3 concentraciones
de dosis ($B$), 4 espesores de pared ($C$); 4 réplicas (días = bloques); 36 observaciones por
réplica. Procedimiento dentro de un día:

1. Se asigna al azar una unidad de antibiótico a cada técnico → **parcelas completas** (primera
   restricción).
2. Cada técnico elige al azar el orden de las concentraciones → **subparcelas** (segunda
   restricción).
3. Dentro de cada concentración se prueban los 4 espesores en orden aleatorio →
   **sub-subparcelas** (sub-subtratamientos).

El libro solo plantea el diseño (los datos están en el problema 13-22); no hay ANOVA numérico.

**Modelo (ec. 13-20):**

$$\begin{aligned}
y_{ijkh}=\mu&+\tau_i+\beta_j+(\tau\beta)_{ij}+\gamma_k+(\tau\gamma)_{ik}+(\beta\gamma)_{jk}+(\tau\beta\gamma)_{ijk}\\
&+\delta_h+(\tau\delta)_{ih}+(\beta\delta)_{jh}+(\tau\beta\delta)_{ijh}+(\gamma\delta)_{kh}+(\tau\gamma\delta)_{ikh}+(\beta\gamma\delta)_{jkh}+(\tau\beta\gamma\delta)_{ijkh}+\varepsilon_{ijkh}
\end{aligned}$$

con $i=1..r$, $j=1..a$, $k=1..b$, $h=1..c$. Error de parcela completa: $(\tau\beta)_{ij}$;
error de subparcela: $(\tau\beta\gamma)_{ijk}$; error de sub-subparcela:
$(\tau\beta\gamma\delta)_{ijkh}$.

**CME (tabla 13-18; réplicas aleatorias, $A$, $B$, $C$ fijos):**

| Estrato | Término | CME | Se prueba contra |
|---|---|---|---|
| Parcela completa | $\tau_i$ | $\sigma^2+abc\,\sigma_\tau^2$ | — |
| | $\beta_j$ ($A$) | $\sigma^2+bc\,\sigma_{\tau\beta}^2+\dfrac{rbc\sum\beta_j^2}{a-1}$ | $(\tau\beta)$ |
| | $(\tau\beta)_{ij}$ | $\sigma^2+bc\,\sigma_{\tau\beta}^2$ | — |
| Subparcela | $\gamma_k$ ($B$) | $\sigma^2+ac\,\sigma_{\tau\gamma}^2+\dfrac{rac\sum\gamma_k^2}{b-1}$ | $(\tau\gamma)$ |
| | $(\tau\gamma)_{ik}$ | $\sigma^2+ac\,\sigma_{\tau\gamma}^2$ | — |
| | $(\beta\gamma)_{jk}$ ($AB$) | $\sigma^2+c\,\sigma_{\tau\beta\gamma}^2+\dfrac{rc\sum\sum(\beta\gamma)_{jk}^2}{(a-1)(b-1)}$ | $(\tau\beta\gamma)$ |
| | $(\tau\beta\gamma)_{ijk}$ | $\sigma^2+c\,\sigma_{\tau\beta\gamma}^2$ | — |
| Sub-subparcela | $\delta_h$ ($C$) | $\sigma^2+ab\,\sigma_{\tau\delta}^2+\dfrac{rab\sum\delta_h^2}{c-1}$ | $(\tau\delta)$ |
| | $(\tau\delta)_{ih}$ | $\sigma^2+ab\,\sigma_{\tau\delta}^2$ | — |
| | $(\beta\delta)_{jh}$ ($AC$) | $\sigma^2+b\,\sigma_{\tau\beta\delta}^2+\dfrac{rb\sum\sum(\beta\delta)_{jh}^2}{(a-1)(c-1)}$ | $(\tau\beta\delta)$ |
| | $(\tau\beta\delta)_{ijh}$ | $\sigma^2+b\,\sigma_{\tau\beta\delta}^2$ | — |
| | $(\gamma\delta)_{kh}$ ($BC$) | $\sigma^2+a\,\sigma_{\tau\gamma\delta}^2+\dfrac{ra\sum\sum(\gamma\delta)_{kh}^2}{(b-1)(c-1)}$ | $(\tau\gamma\delta)$ |
| | $(\tau\gamma\delta)_{ikh}$ | $\sigma^2+a\,\sigma_{\tau\gamma\delta}^2$ | — |
| | $(\beta\gamma\delta)_{jkh}$ ($ABC$) | $\sigma^2+\sigma_{\tau\beta\gamma\delta}^2+\dfrac{r\sum\sum\sum(\beta\gamma\delta)_{jkh}^2}{(a-1)(b-1)(c-1)}$ | $(\tau\beta\gamma\delta)$ |
| | $(\tau\beta\gamma\delta)_{ijkh}$ | $\sigma^2+\sigma_{\tau\beta\gamma\delta}^2$ | — |
| | $\varepsilon_{l(ijkh)}$ | $\sigma^2$ (no estimable) | — |

Erratas de impresión detectadas en la tabla 13-18 del libro (corregidas arriba según el
algoritmo tabular): en $\beta_j$ el libro imprime "$\sigma^2+\sigma_{\tau\beta}^2+\dots$" sin
el coeficiente $bc$ (la fila siguiente sí lo trae), y en $(\beta\gamma\delta)$ el divisor
impreso es $(b-1)(c-1)$.

- **Cada efecto fijo se prueba contra su interacción con réplicas.** No hay pruebas para
  réplicas ni para interacciones con réplicas.
- El análisis es como el de **una sola réplica de un factorial de cuatro factores** (réplicas,
  $A$, $B$, $C$).
- **Grados de libertad / número de réplicas:** el error de parcela completa tiene
  $(r-1)(a-1)$ gl. En el ej. 13-3: $(4-1)(3-1)=6$ gl para probar técnicos. Con $a=3$ son
  $2(r-1)$: 5 réplicas → 8, 6 → 10, 7 → 12. Recomendación: no menos de 4 réplicas; si hay
  recursos, 5 o 6 (cada réplica extra añade 2 gl; pasar de 4 a 5 aumenta la precisión en un
  tercio, de 5 a 6 un 25 % adicional).

### 13-5.3 Parcelas subdivididas en franjas (*strip-split-plot*)

- Uso amplio en agricultura, ocasional en industria.
- Construcción (fig. 13-9): dentro de cada réplica, $A$ se aplica a parcelas completas (p. ej.
  columnas) y $B$ se aplica a **franjas** ortogonales a ellas (filas), que son un *segundo
  conjunto de parcelas completas*. Los niveles de $A$ quedan confundidos con las parcelas
  completas y los de $B$ con las franjas; cada celda de cruce es la subparcela.

**Modelo:**

$$y_{ijk}=\mu+\tau_i+\beta_j+(\tau\beta)_{ij}+\gamma_k+(\tau\gamma)_{ik}+(\beta\gamma)_{jk}+\varepsilon_{ijk},
\quad i=1..r,\ j=1..a,\ k=1..b$$

$(\tau\beta)_{ij}$ y $(\tau\gamma)_{ik}$ son los errores de parcela completa de $A$ y de $B$;
$\varepsilon_{ijk}$ es el "error de subparcela" con el que se prueba $AB$.

**ANOVA abreviado (tabla 13-19; $A$, $B$ fijos, réplicas aleatorias):**

| Fuente | SS | gl | CME |
|---|---|---|---|
| Réplicas (bloques) | $SS_{\text{Réplicas}}$ | $r-1$ | $\sigma_\varepsilon^2+ab\sigma_\tau^2$ |
| $A$ | $SS_A$ | $a-1$ | $\sigma_\varepsilon^2+b\sigma_{\tau\beta}^2+\dfrac{rb\sum\beta_j^2}{a-1}$ |
| Error$_A$ de parcela completa | $SS_{WP_A}$ | $(r-1)(a-1)$ | $\sigma_\varepsilon^2+b\sigma_{\tau\beta}^2$ |
| $B$ | $SS_B$ | $b-1$ | $\sigma_\varepsilon^2+a\sigma_{\tau\gamma}^2+\dfrac{ra\sum\gamma_k^2}{b-1}$ |
| Error$_B$ de parcela completa | $SS_{WP_B}$ | $(r-1)(b-1)$ | $\sigma_\varepsilon^2+a\sigma_{\tau\gamma}^2$ |
| $AB$ | $SS_{AB}$ | $(a-1)(b-1)$ | $\sigma_\varepsilon^2+\dfrac{r\sum\sum(\beta\gamma)_{jk}^2}{(a-1)(b-1)}$ |
| Error de subparcela | $SS_{SP}$ | $(r-1)(a-1)(b-1)$ | $\sigma_\varepsilon^2$ |
| Total | $SS_T$ | $rab-1$ | |

Pruebas: $A$ vs. Error$_A$; $B$ vs. Error$_B$; $AB$ vs. error de subparcela. (Tres errores.)

---

## Resumen comparativo de estructuras de error

| Diseño | Restricciones de aleatorización | Errores | Qué se prueba contra qué |
|---|---|---|---|
| Factorial en bloques | 1 (bloque) | 1 | todo vs. error |
| Parcelas subdivididas | parcela completa | 2 (o rép × cada efecto) | $A$ vs. rép×$A$; $B$ vs. rép×$B$; $AB$ vs. rép×$AB$ |
| Doble subdivisión | parcela y subparcela | 3 estratos | cada efecto fijo vs. su interacción con réplicas |
| En franjas | parcelas de $A$ y franjas de $B$ | 3 | $A$ vs. Error$_A$; $B$ vs. Error$_B$; $AB$ vs. error subparcela |

## Reglas prácticas y advertencias del capítulo

- Preguntar siempre si los niveles de un factor son "los mismos" en todos los niveles del otro;
  si pueden renumerarse arbitrariamente, el factor está anidado y **no** se estima interacción.
- En anidados con factor anidado aleatorio, el factor superior se prueba contra el anidado, no
  contra el error: los gl del denominador dependen del número de niveles anidados, no de $n$.
- Analizar un anidado como factorial produce "efectos" e "interacciones" espurios.
- En parcelas subdivididas, identificar el factor difícil de cambiar; analizar como factorial
  completamente aleatorizado subestima el error del factor de parcela completa.
- El factor de mayor interés debe ir a la subparcela.
- Restringido vs. no restringido en modelos mixtos solo cambia las pruebas de los términos
  aleatorios (ej. 13-2), rara vez las conclusiones prácticas.

## 13-6 Problemas (solo referencia)

13-1 a 13-4 anidados de dos etapas; 13-5 a 13-9 anidado de tres etapas y CME (restringido/no
restringido); 13-10 verificar tabla 13-1; **13-11 y 13-12 anidado no balanceado** (ANOVA y CME
con constantes $c_0,c_1,c_2$ para componentes de varianza); 13-13 a 13-18
factoriales-anidados; 13-19 a 13-21 parcelas subdivididas; 13-22 a 13-25 doble subdivisión
(datos del ej. 13-3 y pregunta sobre cómo aleatorizar bajo cada diseño).

Constantes del problema 13-12 ($A$, $B$ aleatorios, $b_i$ niveles de $B$ en el nivel $i$ de
$A$, $n_{ij}$ réplicas, $N$ total, $b=\sum b_i$): $E(MS_A)=\sigma^2+c_1\sigma_\beta^2+c_2\sigma_\tau^2$,
$E(MS_{B(A)})=\sigma^2+c_0\sigma_\beta^2$, $E(MS_E)=\sigma^2$, con

$$c_0=\frac{N-\sum_i\left(\sum_j n_{ij}^2/n_{i.}\right)}{b-a},\quad
c_1=\frac{\sum_i\left(\sum_j n_{ij}^2/n_{i.}\right)-\sum_i\sum_j n_{ij}^2/N}{a-1},\quad
c_2=\frac{N-\sum_i n_{i.}^2/N}{a-1}$$
