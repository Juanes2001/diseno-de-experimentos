# Capítulo 5 — Introducción a los diseños factoriales

> Montgomery, págs. 170–217

Ficha técnica de consulta. Notación del libro: factor $A$ con $a$ niveles (renglones), factor
$B$ con $b$ niveles (columnas), $n$ réplicas; un punto en el subíndice indica suma sobre ese
índice y la barra, promedio. Las secciones siguen la numeración del libro.

Contenido: 5-1 definiciones · 5-2 ventaja del factorial · 5-3 factorial de dos factores ·
5-4 factorial general · 5-5 curvas y superficies de respuesta · 5-6 bloques en factoriales ·
5-7 problemas (solo índice temático).

---

## 5-1 Definiciones y principios básicos

**Diseño factorial.** En cada réplica completa se corren *todas* las combinaciones posibles de
los niveles de los factores. Con $a$ niveles de $A$ y $b$ de $B$ cada réplica tiene $ab$
combinaciones de tratamientos. Los factores dispuestos así se dicen **cruzados**.

**Efecto principal.** Cambio en la respuesta producido por un cambio en el nivel del factor.
Con dos niveles (bajo "−", alto "+") es la diferencia entre la respuesta promedio en el nivel
alto y la respuesta promedio en el nivel bajo:

$$A = \bar y_{A^+} - \bar y_{A^-}$$

Con más de dos niveles hay otras formas de definir el efecto (se tratan más adelante en el libro).

**Interacción.** Existe cuando la diferencia en la respuesta entre los niveles de un factor no
es la misma en todos los niveles del otro factor. En el $2\times 2$, la magnitud de $AB$ es la
mitad de la diferencia entre el efecto de $A$ con $B^+$ y el efecto de $A$ con $B^-$:

$$AB = \tfrac12\left[(\text{efecto de }A \mid B^+) - (\text{efecto de }A \mid B^-)\right]$$

### Ejemplos numéricos del texto (figs. 5-1 y 5-2)

Respuestas en los vértices, en el orden $(A^-B^-,\ A^+B^-,\ A^-B^+,\ A^+B^+)$:

| Caso | Datos | $A$ | $B$ | $AB$ |
|---|---|---|---|---|
| Fig. 5-1 (sin interacción) | 20, 40, 30, 52 | $\frac{40+52}{2}-\frac{20+30}{2}=21$ | $\frac{30+52}{2}-\frac{20+40}{2}=11$ | $1$ |
| Fig. 5-2 (con interacción) | 20, 50, 40, 12 | $\frac{50+12}{2}-\frac{20+40}{2}=1$ | — | $\frac{-28-30}{2}=-29$ |

En la fig. 5-2 el efecto de $A$ es $50-20=30$ con $B^-$ y $12-40=-28$ con $B^+$: el efecto
principal promedio ($A=1$) sugeriría erróneamente que $A$ no influye.

### Gráficas de interacción (figs. 5-3 y 5-4)

Respuesta contra niveles de $A$, una línea por nivel de $B$. Rectas aproximadamente paralelas
⇒ sin interacción; rectas no paralelas (o que se cruzan) ⇒ interacción. Sirven para interpretar
y comunicar interacciones significativas, pero **no deben ser la única técnica de análisis**:
su lectura es subjetiva y puede engañar.

### Representación con un modelo de regresión (factores cuantitativos)

$$y = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + \beta_{12}x_1x_2 + \varepsilon$$

con $x_1, x_2$ en **escala codificada** de $-1$ a $+1$ (niveles bajo y alto de $A$ y $B$) y
$x_1x_2$ la interacción. Relación con los efectos en el diseño de dos niveles:

- $\hat\beta_0$ = promedio de todas las respuestas.
- $\hat\beta_j$ = **la mitad** del efecto principal correspondiente; $\hat\beta_{12}$ = la mitad
  del efecto de interacción.
- Estas estimaciones son las de **mínimos cuadrados**.

Para la fig. 5-1: $\hat\beta_0=(20+40+30+52)/4=35.5$, $\hat\beta_1=21/2=10.5$,
$\hat\beta_2=11/2=5.5$, $\hat\beta_{12}=1/2=0.5$:

$$\hat y = 35.5 + 10.5x_1 + 5.5x_2 + 0.5x_1x_2$$

Como $\hat\beta_{12}$ es pequeño frente a los efectos principales, se elimina:
$\hat y = 35.5+10.5x_1+5.5x_2$.

**Superficie de respuesta y gráfica de contorno.** Sin interacción la superficie es un plano y
los contornos son rectas paralelas (fig. 5-5). Con interacción apreciable (el texto usa
$\hat y = 35.5+10.5x_1+5.5x_2+8x_1x_2$, fig. 5-6) el plano se "tuerce" y los contornos son
curvos: **la interacción es una forma de curvatura** del modelo de superficie de respuesta.

### Reglas y advertencias

- Cuando una interacción es grande, los efectos principales correspondientes tienen poco
  significado práctico; la interacción significativa suele **enmascarar** los efectos principales.
- Con interacción significativa, examinar los niveles de un factor manteniendo fijos los
  niveles del otro (efectos simples) para concluir sobre ese factor.
- Conocer la interacción $AB$ es más útil que conocer el efecto principal.

---

## 5-2 La ventaja de los diseños factoriales

Comparación con el experimento de **un factor a la vez** (fig. 5-7), dos factores a dos niveles:

- Un factor a la vez: combinaciones $A^-B^-$, $A^+B^-$, $A^-B^+$. Efecto de $A$:
  $A^+B^- - A^-B^-$; efecto de $B$: $A^-B^+ - A^-B^-$. Con dos observaciones por combinación
  (para promediar el error) se necesitan **6** observaciones.
- Factorial: se añade $A^+B^+$ y con **4** observaciones hay dos estimaciones de cada efecto
  ($A^+B^- - A^-B^-$ y $A^+B^+ - A^-B^+$ para $A$; análogo para $B$), que promediadas tienen
  la misma precisión que las del experimento de un factor a la vez.
- **Eficiencia relativa** $=6/4=1.5$ con dos factores; crece con el número de factores
  (fig. 5-8: aprox. 2.0 con 3 factores, 2.5 con 4, 3.0 con 5 y 3.5 con 6).

Ventajas resumidas por el autor:

1. Son más eficientes que los experimentos de un factor a la vez.
2. Son **necesarios** cuando puede haber interacciones: sin ellos se llega a conclusiones
   incorrectas (un factor a la vez extrapolaría que $A^+B^+$ es aún mejor si $A^+B^-$ y $A^-B^+$
   mejoran a $A^-B^-$; con interacción eso puede ser un error grave, ver fig. 5-2).
3. Permiten estimar los efectos de un factor en varios niveles de los demás, de modo que las
   conclusiones valen en un rango de condiciones experimentales.

---

## 5-3 Diseño factorial de dos factores

### 5-3.1 Un ejemplo y planteamiento general

**Experimento de la batería (tablas 5-1 y 5-4).** Respuesta: vida (h). Factor $A$: tipo de
material de la placa (3 niveles, cualitativo). Factor $B$: temperatura (15, 70 y 125 °F,
cuantitativo). $n=4$ baterías por combinación, 36 corridas en orden aleatorio. Preguntas:
(1) qué efectos tienen material y temperatura sobre la vida; (2) si existe un material que dé
vida larga de forma regular *sin importar la temperatura* (**diseño de productos robustos**: la
temperatura es controlable en el laboratorio pero no en el campo).

**Arreglo general (tabla 5-2).** $y_{ijk}$: respuesta con el nivel $i$ de $A$ ($i=1,\dots,a$),
el nivel $j$ de $B$ ($j=1,\dots,b$), réplica $k$ ($k=1,\dots,n$). Las $abn$ observaciones se
corren en orden aleatorio: es un **diseño completamente aleatorizado**.

**Modelo de los efectos (ec. 5-1):**

$$y_{ijk} = \mu + \tau_i + \beta_j + (\tau\beta)_{ij} + \varepsilon_{ijk}$$

- $\mu$: efecto promedio global; $\tau_i$: efecto del nivel $i$ de $A$; $\beta_j$: efecto del
  nivel $j$ de $B$; $(\tau\beta)_{ij}$: interacción; $\varepsilon_{ijk}$: error aleatorio
  $\text{NID}(0,\sigma^2)$.
- Efectos **fijos**, definidos como desviaciones de la media global:
  $\sum_i \tau_i = 0$, $\sum_j \beta_j = 0$, $\sum_i (\tau\beta)_{ij} = \sum_j (\tau\beta)_{ij} = 0$.

**Modelo de las medias:** $y_{ijk} = \mu_{ij} + \varepsilon_{ijk}$ con
$\mu_{ij} = \mu + \tau_i + \beta_j + (\tau\beta)_{ij}$.

**Modelo de regresión:** alternativa útil cuando uno o más factores son cuantitativos (sec. 5-5).

**Hipótesis (ecs. 5-2a, b, c):**

$$H_0:\tau_1=\dots=\tau_a=0 \quad\text{vs.}\quad H_1:\text{al menos una }\tau_i\neq 0$$
$$H_0:\beta_1=\dots=\beta_b=0 \quad\text{vs.}\quad H_1:\text{al menos una }\beta_j\neq 0$$
$$H_0:(\tau\beta)_{ij}=0\ \forall i,j \quad\text{vs.}\quad H_1:\text{al menos una }(\tau\beta)_{ij}\neq 0$$

### 5-3.2 Análisis estadístico del modelo con efectos fijos

**Totales y promedios (ec. 5-3):**

$$y_{i..}=\sum_{j}\sum_{k} y_{ijk},\ \ \bar y_{i..}=\frac{y_{i..}}{bn};\qquad
y_{.j.}=\sum_{i}\sum_{k} y_{ijk},\ \ \bar y_{.j.}=\frac{y_{.j.}}{an}$$
$$y_{ij.}=\sum_{k} y_{ijk},\ \ \bar y_{ij.}=\frac{y_{ij.}}{n};\qquad
y_{...}=\sum_i\sum_j\sum_k y_{ijk},\ \ \bar y_{...}=\frac{y_{...}}{abn}$$

**Partición de la suma de cuadrados total corregida (ecs. 5-4 y 5-5):**

$$\sum_i\sum_j\sum_k (y_{ijk}-\bar y_{...})^2 =
bn\sum_i(\bar y_{i..}-\bar y_{...})^2 + an\sum_j(\bar y_{.j.}-\bar y_{...})^2
+ n\sum_i\sum_j(\bar y_{ij.}-\bar y_{i..}-\bar y_{.j.}+\bar y_{...})^2
+ \sum_i\sum_j\sum_k (y_{ijk}-\bar y_{ij.})^2$$

$$SS_T = SS_A + SS_B + SS_{AB} + SS_E$$

Hace falta $n\ge 2$ para poder obtener $SS_E$.

**Grados de libertad.** $A$: $a-1$; $B$: $b-1$; $AB$: $(ab-1)-(a-1)-(b-1)=(a-1)(b-1)$;
error: $ab(n-1)$ ($n-1$ dentro de cada una de las $ab$ celdas); total: $abn-1$.

**Cuadrados medios esperados:**

$$E(MS_A)=\sigma^2+\frac{bn\sum_i\tau_i^2}{a-1},\quad
E(MS_B)=\sigma^2+\frac{an\sum_j\beta_j^2}{b-1},\quad
E(MS_{AB})=\sigma^2+\frac{n\sum_i\sum_j(\tau\beta)_{ij}^2}{(a-1)(b-1)},\quad
E(MS_E)=\sigma^2$$

Bajo las hipótesis nulas los cuatro cuadrados medios estiman $\sigma^2$; si hay efectos, el
cuadrado medio correspondiente supera a $MS_E$. Con el modelo adecuado y
$\varepsilon_{ijk}\sim\text{NID}(0,\sigma^2)$, cada cociente $MS/MS_E$ sigue una $F$ con los
grados de libertad del numerador indicados y $ab(n-1)$ en el denominador; región crítica en la
cola superior. (Nota al pie: la prueba $F$ puede verse como aproximación de una prueba de
aleatorización.)

**Tabla ANOVA, efectos fijos (tabla 5-3):**

| Fuente | SS | g.l. | MS | $F_0$ |
|---|---|---|---|---|
| Tratamientos $A$ | $SS_A$ | $a-1$ | $MS_A=SS_A/(a-1)$ | $MS_A/MS_E$ |
| Tratamientos $B$ | $SS_B$ | $b-1$ | $MS_B=SS_B/(b-1)$ | $MS_B/MS_E$ |
| Interacción | $SS_{AB}$ | $(a-1)(b-1)$ | $MS_{AB}=SS_{AB}/[(a-1)(b-1)]$ | $MS_{AB}/MS_E$ |
| Error | $SS_E$ | $ab(n-1)$ | $MS_E=SS_E/[ab(n-1)]$ | |
| Total | $SS_T$ | $abn-1$ | | |

**Fórmulas de cálculo manual (ecs. 5-6 a 5-10):**

$$SS_T=\sum_i\sum_j\sum_k y_{ijk}^2-\frac{y_{...}^2}{abn}$$
$$SS_A=\frac{1}{bn}\sum_i y_{i..}^2-\frac{y_{...}^2}{abn},\qquad
SS_B=\frac{1}{an}\sum_j y_{.j.}^2-\frac{y_{...}^2}{abn}$$
$$SS_{\text{Subtotales}}=\frac{1}{n}\sum_i\sum_j y_{ij.}^2-\frac{y_{...}^2}{abn},\qquad
SS_{AB}=SS_{\text{Subtotales}}-SS_A-SS_B$$
$$SS_E=SS_T-SS_{AB}-SS_A-SS_B = SS_T-SS_{\text{Subtotales}}$$

#### Ejemplo 5-1 — Diseño de la batería

Factorial $3\times 3$ con $n=4$. Totales (tabla 5-4): materiales $y_{i..}=998,\ 1300,\ 1501$;
temperaturas $y_{.j.}=1738,\ 1291,\ 770$; gran total $y_{...}=3799$.

Totales de celda $y_{ij.}$ (promedios $\bar y_{ij.}$ entre paréntesis):

| Material | 15 °F | 70 °F | 125 °F |
|---|---|---|---|
| 1 | 539 (134.75) | 229 (57.25) | 230 (57.50) |
| 2 | 623 (155.75) | 479 (119.75) | 198 (49.50) |
| 3 | 576 (144.00) | 583 (145.75) | 342 (85.50) |

ANOVA (tabla 5-5):

| Fuente | SS | g.l. | MS | $F_0$ | Valor P |
|---|---|---|---|---|---|
| Tipos de material | 10,683.72 | 2 | 5,341.86 | 7.91 | 0.0020 |
| Temperatura | 39,118.72 | 2 | 19,559.36 | 28.97 | 0.0001 |
| Interacción | 9,613.78 | 4 | 2,403.44 | 3.56 | 0.0186 |
| Error | 18,230.75 | 27 | 675.21 | | |
| Total | 77,646.97 | 35 | | | |

Valores críticos: $F_{0.05,4,27}=2.73$, $F_{0.05,2,27}=3.35$. Interacción y ambos efectos
principales significativos. Gráfica de promedios de celda contra temperatura (fig. 5-9): líneas
no paralelas. En general la vida es mayor a baja temperatura sin importar el material; de 15 a
70 °F la vida con el material 3 aumenta y con los materiales 1 y 2 disminuye; de 70 a 125 °F
disminuye con los materiales 2 y 3 y casi no cambia con el 1. **Conclusión:** el material 3 da
la menor pérdida de vida al cambiar la temperatura (el más robusto).

Salida de Design-Expert (fig. 5-10): $SS_{\text{Modelo}}=10{,}683.72+39{,}118.72+9613.78=59{,}416.22$
con 8 g.l., $MS=7427.03$, $F=11.00$, $P<0.0001$;
$R^2=SS_{\text{Modelo}}/SS_{\text{Total}}=59{,}416.22/77{,}646.97=0.7652$; $R^2$ ajustada 0.6956;
$R^2$ de predicción 0.5826; PRESS 32,410.22; desv. est. 25.98; media 105.53; C.V. 24.62;
Adeq Precision 8.178. Falta de ajuste con 0 g.l. (modelo saturado en las celdas); error puro
con 27 g.l.

#### Comparaciones múltiples

- Si el ANOVA indica diferencias entre medias de renglones o columnas, se aplican los métodos
  del capítulo 3 (Tukey, etc.).
- **Con interacción significativa**, las comparaciones entre las medias de un factor quedan
  oscurecidas por la interacción. Procedimiento: fijar el otro factor en un nivel específico y
  aplicar Tukey a las medias de celda en ese nivel, usando $MS_E$ del ANOVA como estimación de
  $\sigma^2$ (supone varianza igual en todas las combinaciones):

$$T_\alpha = q_\alpha\big(a,\ ab(n-1)\big)\sqrt{\frac{MS_E}{n}}$$

  (número de medias comparadas, g.l. del error; el divisor es $n$, las observaciones por celda).
- Ejemplo (materiales a 70 °F): medias 57.25 (mat. 1), 119.75 (mat. 2), 145.75 (mat. 3);
  $q_{0.05}(3,27)=3.50$ (interpolado en la tabla VIII);
  $T_{0.05}=3.50\sqrt{675.21/4}=45.47$.
  - 3 vs. 1: $88.50 > 45.47$ (difieren).
  - 3 vs. 2: $26.00 < 45.47$ (no difieren).
  - 2 vs. 1: $62.50 > 45.47$ (difieren).

  A 70 °F los materiales 2 y 3 tienen la misma vida media y el material 1 es significativamente
  menor.
- Alternativa: comparar **todas** las $ab$ medias de celda (en el ejemplo, 36 pares entre 9
  medias); esas diferencias incluyen la interacción y ambos efectos principales.

### 5-3.3 Verificación de la adecuación del modelo

Residuales (ecs. 5-11 y 5-12): el valor ajustado es el promedio de la celda,
$\hat y_{ijk}=\bar y_{ij.}$, así que

$$e_{ijk}=y_{ijk}-\bar y_{ij.}$$

Diagnósticos: (1) gráfica de probabilidad normal de los residuales; (2) residuales contra
$\hat y_{ijk}$; (3) residuales contra niveles de cada factor. Residual estandarizado:
$e_{ijk}/\sqrt{MS_E}$ (señal de alerta si $|\cdot|>2$).

Ejemplo 5-1 (tabla 5-6, figs. 5-11 a 5-14): normalidad sin problemas; el residual más negativo
es $-60.75$ (15 °F, material 1), estandarizado $-60.75/\sqrt{675.21}=-2.34$, el único con valor
absoluto mayor que 2. Ligera tendencia de la varianza a crecer con la vida; la celda 15 °F –
material 1 contiene los dos residuales extremos ($-60.75$ y $45.25$) y explica la ligera
desigualdad de varianzas. No hay error de registro evidente; el problema no es grave como para
alterar las conclusiones.

### 5-3.4 Estimación de los parámetros del modelo

Ecuaciones normales de mínimos cuadrados (ecs. 5-14a–d) para el modelo de los efectos:

$$\mu:\ abn\hat\mu+bn\sum_i\hat\tau_i+an\sum_j\hat\beta_j+n\sum_i\sum_j\widehat{(\tau\beta)}_{ij}=y_{...}$$
$$\tau_i:\ bn\hat\mu+bn\hat\tau_i+n\sum_j\hat\beta_j+n\sum_j\widehat{(\tau\beta)}_{ij}=y_{i..}$$
$$\beta_j:\ an\hat\mu+n\sum_i\hat\tau_i+an\hat\beta_j+n\sum_i\widehat{(\tau\beta)}_{ij}=y_{.j.}$$
$$(\tau\beta)_{ij}:\ n\hat\mu+n\hat\tau_i+n\hat\beta_j+n\widehat{(\tau\beta)}_{ij}=y_{ij.}$$

El modelo tiene $1+a+b+ab$ parámetros y está **sobreparametrizado**: hay $a+b+1$ dependencias
lineales, por lo que no hay solución única. Se imponen $a+b+1$ restricciones independientes
(ecs. 5-15a–d): $\sum_i\hat\tau_i=0$, $\sum_j\hat\beta_j=0$,
$\sum_i\widehat{(\tau\beta)}_{ij}=0$ para cada $j$, $\sum_j\widehat{(\tau\beta)}_{ij}=0$ para
cada $i$. Solución (ec. 5-16):

$$\hat\mu=\bar y_{...},\qquad \hat\tau_i=\bar y_{i..}-\bar y_{...},\qquad
\hat\beta_j=\bar y_{.j.}-\bar y_{...},\qquad
\widehat{(\tau\beta)}_{ij}=\bar y_{ij.}-\bar y_{i..}-\bar y_{.j.}+\bar y_{...}$$

y por tanto $\hat y_{ijk}=\hat\mu+\hat\tau_i+\hat\beta_j+\widehat{(\tau\beta)}_{ij}=\bar y_{ij.}$.

**Funciones estimables.** Los parámetros individuales no tienen estimación única (dependen de
las restricciones), pero sí la tienen las combinaciones lineales de los miembros izquierdos de
las ecuaciones normales. Ejemplo:
$\tau_i-\tau_u+\overline{(\tau\beta)}_{i.}-\overline{(\tau\beta)}_{u.}$, la "verdadera"
diferencia entre los niveles $i$ y $u$ de $A$: incluye un efecto de interacción promedio, y por
eso la interacción perturba las pruebas de los efectos principales.

### 5-3.5 Elección del tamaño de la muestra

Se usan las curvas de operación característica (parte V del apéndice) con el parámetro
$\Phi^2$ (tabla 5-7), modelo de efectos fijos:

| Factor | $\Phi^2$ | g.l. numerador | g.l. denominador |
|---|---|---|---|
| $A$ | $\dfrac{bn\sum_i\tau_i^2}{a\sigma^2}$ | $a-1$ | $ab(n-1)$ |
| $B$ | $\dfrac{an\sum_j\beta_j^2}{b\sigma^2}$ | $b-1$ | $ab(n-1)$ |
| $AB$ | $\dfrac{n\sum_i\sum_j(\tau\beta)_{ij}^2}{\sigma^2[(a-1)(b-1)+1]}$ | $(a-1)(b-1)$ | $ab(n-1)$ |

**Valor mínimo de $\Phi^2$** para una diferencia especificada $D$ (ecs. 5-17 a 5-19):

$$\text{entre dos medias de renglón: }\Phi^2=\frac{nbD^2}{2a\sigma^2};\qquad
\text{entre dos medias de columna: }\Phi^2=\frac{naD^2}{2b\sigma^2}$$
$$\text{entre dos efectos de interacción: }\Phi^2=\frac{nD^2}{2\sigma^2[(a-1)(b-1)+1]}$$

Ejemplo (batería): detectar $D=40$ h entre dos temperaturas, $\sigma\approx 25$, $\alpha=0.05$:
$\Phi^2=\dfrac{n(3)(40)^2}{2(3)(25)^2}=1.28n$.

| $n$ | $\Phi^2$ | $\Phi$ | $\nu_1$ | $\nu_2$ (error) | $\beta$ |
|---|---|---|---|---|---|
| 2 | 2.56 | 1.60 | 2 | 9 | 0.45 |
| 3 | 3.84 | 1.96 | 2 | 18 | 0.18 |
| 4 | 5.12 | 2.26 | 2 | 27 | 0.06 |

Con $n=4$, $\beta\approx 0.06$ (potencia cercana a 94 %): cuatro réplicas bastan, siempre que
la estimación de $\sigma$ no esté muy errada. Recomendación: repetir el cálculo con otros
valores de $\sigma$ para ver la sensibilidad.

### 5-3.6 El supuesto de no interacción en un modelo de dos factores

Modelo sin interacción (ec. 5-20):

$$y_{ijk}=\mu+\tau_i+\beta_j+\varepsilon_{ijk}$$

La interacción se agrupa con el error: $SS_E$ pasa a tener $abn-a-b+1$ g.l. **Advertencia:**
ignorar una interacción realmente presente altera de forma drástica la interpretación.

Batería bajo este modelo (tabla 5-8): material $F_0=5.95$, temperatura $F_0=21.78$, error
$SS=27{,}844.52$ con 31 g.l., $MS_E=898.21$ (total impreso 77,646.96).

**Diagnóstico de la interacción omitida.** Valores ajustados sin interacción:
$\hat y_{ijk}=\bar y_{i..}+\bar y_{.j.}-\bar y_{...}$. Se grafica $\bar y_{ij.}-\hat y_{ijk}$
(media de celda observada menos la estimada sin interacción) contra $\hat y_{ijk}$: cualquier
patrón sugiere interacción. En la fig. 5-15 las diferencias pasan de positivo a negativo y de
nuevo a positivo y a negativo ⇒ el modelo sin interacción es inadecuado.

### 5-3.7 Una observación por celda

Modelo con una sola réplica (ec. 5-21):
$y_{ij}=\mu+\tau_i+\beta_j+(\tau\beta)_{ij}+\varepsilon_{ij}$.

ANOVA (tabla 5-9, ambos factores fijos):

| Fuente | SS | g.l. | MS | MS esperado |
|---|---|---|---|---|
| Renglones ($A$) | $\sum_i \dfrac{y_{i.}^2}{b}-\dfrac{y_{..}^2}{ab}$ | $a-1$ | $MS_A$ | $\sigma^2+\dfrac{b\sum\tau_i^2}{a-1}$ |
| Columnas ($B$) | $\sum_j \dfrac{y_{.j}^2}{a}-\dfrac{y_{..}^2}{ab}$ | $b-1$ | $MS_B$ | $\sigma^2+\dfrac{a\sum\beta_j^2}{b-1}$ |
| Residual o $AB$ | sustracción | $(a-1)(b-1)$ | $MS_{\text{Residual}}$ | $\sigma^2+\dfrac{\sum\sum(\tau\beta)_{ij}^2}{(a-1)(b-1)}$ |
| Total | $\sum_i\sum_j y_{ij}^2-\dfrac{y_{..}^2}{ab}$ | $ab-1$ | | |

- $\sigma^2$ **no es estimable**: interacción y error no se pueden separar. No hay pruebas para
  los efectos principales a menos que la interacción sea cero.
- Si $(\tau\beta)_{ij}=0$, el modelo es $y_{ij}=\mu+\tau_i+\beta_j+\varepsilon_{ij}$ (ec. 5-22),
  $MS_{\text{Residual}}$ es estimador insesgado de $\sigma^2$ y los efectos principales se prueban
  con $MS_A/MS_{\text{Residual}}$ y $MS_B/MS_{\text{Residual}}$.

#### Prueba de no aditividad de Tukey (un grado de libertad)

Supone una forma simple de la interacción: $(\tau\beta)_{ij}=\gamma\tau_i\beta_j$, con $\gamma$
constante desconocida (enfoque de regresión). Parte $SS_{\text{Residual}}$ en un componente de
no aditividad con 1 g.l. y un error con $(a-1)(b-1)-1$ g.l. (ecs. 5-23 a 5-25):

$$SS_N=\frac{\left[\displaystyle\sum_{i=1}^{a}\sum_{j=1}^{b} y_{ij}\,y_{i.}\,y_{.j}
- y_{..}\left(SS_A+SS_B+\frac{y_{..}^2}{ab}\right)\right]^2}{ab\,SS_A\,SS_B}$$

$$SS_{\text{Error}}=SS_{\text{Residual}}-SS_N,\qquad
F_0=\frac{SS_N}{SS_{\text{Error}}/[(a-1)(b-1)-1]}$$

Se rechaza la hipótesis de no interacción si $F_0>F_{\alpha,\,1,\,(a-1)(b-1)-1}$.

#### Ejemplo 5-2 — Impurezas de un producto químico

Factores: temperatura (100, 125, 150 °F; $a=3$) y presión (25, 30, 35, 40, 45; $b=5$), una
réplica. Totales: temperatura $23,\ 13,\ 8$; presión $9,\ 6,\ 13,\ 6,\ 10$; $y_{..}=44$.
$SS_A=23.33$, $SS_B=11.60$, $SS_T=166-129.07=36.93$, $SS_{\text{Residual}}=2.00$.
$\sum\sum y_{ij}y_{i.}y_{.j}=7236$;

$$SS_N=\frac{[7236-(44)(23.33+11.60+129.07)]^2}{(3)(5)(23.33)(11.60)}=\frac{[20.00]^2}{4059.42}=0.0985$$

| Fuente | SS | g.l. | MS | $F_0$ | Valor P |
|---|---|---|---|---|---|
| Temperatura | 23.33 | 2 | 11.67 | 42.97 | 0.0001 |
| Presión | 11.60 | 4 | 2.90 | 10.68 | 0.0042 |
| No aditividad | 0.0985 | 1 | 0.0985 | 0.36 | 0.5674 |
| Error | 1.9015 | 7 | 0.2716 | | |
| Total | 36.93 | 14 | | | |

Sin evidencia de interacción; ambos efectos principales significativos. (En el desarrollo, el
libro escribe una vez $36.96$ en lugar de $36.93$ para $SS_T$; es errata, pág. 193.)

**Relación con el DBCA.** El modelo de la ec. 5-22 tiene la misma forma que el de bloques
completos aleatorizados (ec. 4-1) y la prueba de Tukey sirve también para detectar interacción
bloque–tratamiento. Pero las situaciones experimentales difieren: en el factorial *todas* las
$ab$ corridas se aleatorizan; en el DBCA solo se aleatoriza **dentro del bloque** (el bloque es
una restricción sobre la aleatorización). La ejecución y la interpretación son distintas.

---

## 5-4 Diseño factorial general

$a$ niveles de $A$, $b$ de $B$, $c$ de $C$, …, con $n$ réplicas: $abc\cdots n$ observaciones.
Se necesita $n\ge 2$ para estimar el error si el modelo incluye todas las interacciones.

Reglas con **todos los factores fijos**:

- Cada efecto principal o interacción se prueba con $F_0=MS_{\text{efecto}}/MS_E$, cola superior.
- g.l. de un efecto principal = niveles − 1; g.l. de una interacción = producto de los g.l. de
  sus componentes.
- Con **factores aleatorios** el estadístico no siempre tiene $MS_E$ en el denominador: hay que
  examinar los cuadrados medios esperados (cap. 12).

**Modelo de tres factores (ec. 5-26):**

$$y_{ijkl}=\mu+\tau_i+\beta_j+\gamma_k+(\tau\beta)_{ij}+(\tau\gamma)_{ik}+(\beta\gamma)_{jk}
+(\tau\beta\gamma)_{ijk}+\varepsilon_{ijkl}$$

$i=1..a$, $j=1..b$, $k=1..c$, $l=1..n$.

**Tabla ANOVA de tres factores, efectos fijos (tabla 5-12):**

| Fuente | SS | g.l. | MS esperado | $F_0$ |
|---|---|---|---|---|
| $A$ | $SS_A$ | $a-1$ | $\sigma^2+\dfrac{bcn\sum\tau_i^2}{a-1}$ | $MS_A/MS_E$ |
| $B$ | $SS_B$ | $b-1$ | $\sigma^2+\dfrac{acn\sum\beta_j^2}{b-1}$ | $MS_B/MS_E$ |
| $C$ | $SS_C$ | $c-1$ | $\sigma^2+\dfrac{abn\sum\gamma_k^2}{c-1}$ | $MS_C/MS_E$ |
| $AB$ | $SS_{AB}$ | $(a-1)(b-1)$ | $\sigma^2+\dfrac{cn\sum\sum(\tau\beta)_{ij}^2}{(a-1)(b-1)}$ | $MS_{AB}/MS_E$ |
| $AC$ | $SS_{AC}$ | $(a-1)(c-1)$ | $\sigma^2+\dfrac{bn\sum\sum(\tau\gamma)_{ik}^2}{(a-1)(c-1)}$ | $MS_{AC}/MS_E$ |
| $BC$ | $SS_{BC}$ | $(b-1)(c-1)$ | $\sigma^2+\dfrac{an\sum\sum(\beta\gamma)_{jk}^2}{(b-1)(c-1)}$ | $MS_{BC}/MS_E$ |
| $ABC$ | $SS_{ABC}$ | $(a-1)(b-1)(c-1)$ | $\sigma^2+\dfrac{n\sum\sum\sum(\tau\beta\gamma)_{ijk}^2}{(a-1)(b-1)(c-1)}$ | $MS_{ABC}/MS_E$ |
| Error | $SS_E$ | $abc(n-1)$ | $\sigma^2$ | |
| Total | $SS_T$ | $abcn-1$ | | |

(En el renglón de $A$ el libro imprime "$\sigma+$"; es errata por $\sigma^2$, pág. 195.)

**Fórmulas de cálculo (ecs. 5-27 a 5-35):**

$$SS_T=\sum_i\sum_j\sum_k\sum_l y_{ijkl}^2-\frac{y_{....}^2}{abcn}$$
$$SS_A=\frac{1}{bcn}\sum_i y_{i...}^2-\frac{y_{....}^2}{abcn},\quad
SS_B=\frac{1}{acn}\sum_j y_{.j..}^2-\frac{y_{....}^2}{abcn},\quad
SS_C=\frac{1}{abn}\sum_k y_{..k.}^2-\frac{y_{....}^2}{abcn}$$
$$SS_{AB}=\frac{1}{cn}\sum_i\sum_j y_{ij..}^2-\frac{y_{....}^2}{abcn}-SS_A-SS_B
=SS_{\text{Subtotales}(AB)}-SS_A-SS_B$$
$$SS_{AC}=\frac{1}{bn}\sum_i\sum_k y_{i.k.}^2-\frac{y_{....}^2}{abcn}-SS_A-SS_C,\qquad
SS_{BC}=\frac{1}{an}\sum_j\sum_k y_{.jk.}^2-\frac{y_{....}^2}{abcn}-SS_B-SS_C$$
$$SS_{ABC}=\frac{1}{n}\sum_i\sum_j\sum_k y_{ijk.}^2-\frac{y_{....}^2}{abcn}
-SS_A-SS_B-SS_C-SS_{AB}-SS_{AC}-SS_{BC}$$
$$SS_E=SS_T-SS_{\text{Subtotales}(ABC)}$$

Consejo práctico: desplegar los datos en tres tablas de dos vías ($A\times B$, $A\times C$,
$B\times C$) para obtener los totales de celda.

#### Ejemplo 5-3 — Embotellado de un refresco

Respuesta: desviación promedio de la altura de llenado respecto del objetivo. Factores:
$A$ = % de carbonatación (10, 12, 14), $B$ = presión de operación (25, 30 psi), $C$ = rapidez
de línea (200, 250 bpm); $n=2$; 24 corridas aleatorizadas ($3\times2\times2$).
Totales: $y_{i...}=-4,\ 20,\ 59$; $y_{.j..}=21,\ 54$; $y_{..k.}=26,\ 49$; $y_{....}=75$;
$\sum y^2=571$; $SS_{\text{Subtotales}(ABC)}=328.125$.

ANOVA (tabla 5-14):

| Fuente | SS | g.l. | MS | $F_0$ | Valor P |
|---|---|---|---|---|---|
| % carbonatación ($A$) | 252.750 | 2 | 126.375 | 178.412 | <0.0001 |
| Presión ($B$) | 45.375 | 1 | 45.375 | 64.059 | <0.0001 |
| Rapidez de línea ($C$) | 22.042 | 1 | 22.042 | 31.118 | 0.0001 |
| $AB$ | 5.250 | 2 | 2.625 | 3.706 | 0.0558 |
| $AC$ | 0.583 | 2 | 0.292 | 0.412 | 0.6713 |
| $BC$ | 1.042 | 1 | 1.042 | 1.471 | 0.2485 |
| $ABC$ | 1.083 | 2 | 0.542 | 0.765 | 0.4867 |
| Error | 8.500 | 12 | 0.708 | | |
| Total | 336.625 | 23 | | | |

Los tres efectos principales son significativos y positivos (subir cualquiera eleva la
desviación); $AB$ muestra cierta interacción ($P=0.0558$), pequeña en la gráfica (fig. 5-16d).
Residuales sin motivo de preocupación (se deja como ejercicio). **Recomendación del ejemplo:**
presión baja (25 psi) y rapidez alta (250 bpm, maximiza la producción); la variabilidad del
llenado se reduce estrechando la distribución del nivel de carbonatación (fig. 5-17), lo que se
logró mejorando el control de la temperatura en manufactura.

---

## 5-5 Ajuste de curvas y superficies de respuesta

- Con un factor **cuantitativo** conviene ajustar una **curva de respuesta** (ecuación que
  relaciona $y$ con el factor) para interpolar en niveles intermedios no ensayados.
- Con al menos dos factores cuantitativos se ajusta una **superficie de respuesta**.
- Se ajustan por **regresión lineal** (mínimos cuadrados); ver sec. 3-5.1 y cap. 10.
- Un factor cuantitativo con $k$ niveles admite efectos polinomiales hasta grado $k-1$, cada
  uno con 1 g.l. (con 3 niveles: lineal y cuadrático). Las interacciones entre factores
  cuantitativos se parten en componentes de 1 g.l. (lineal × lineal, etc.).

**Principio de jerarquía.** Si un modelo contiene un término de orden superior (p. ej. $A^2B$),
debe contener también los términos de orden inferior que lo componen ($A^2$, $AB$, y los
efectos principales). Da consistencia interna al modelo. Matiz del autor: no siempre es buena
idea; muchos modelos predicen mejor sin los términos no significativos que la jerarquía obliga
a conservar.

#### Ejemplo 5-4 — Batería con temperatura cuantitativa

Mismos datos del ejemplo 5-1. $A$ = temperatura (cuantitativa, 3 niveles ⇒ lineal y
cuadrático), $B$ = material (cualitativo). Salida de Design-Expert (tabla 5-15), "Response
Surface Reduced Cubic Model":

| Fuente | SS | g.l. | MS | $F$ | Prob > F |
|---|---|---|---|---|---|
| Modelo | 59,416.22 | 8 | 7427.03 | 11.00 | <0.0001 |
| $A$ (temp. lineal) | 39,042.67 | 1 | 39,042.67 | 57.82 | <0.0001 |
| $B$ (material) | 10,683.72 | 2 | 5341.86 | 7.91 | 0.0020 |
| $A^2$ (temp. cuadrático) | 76.06 | 1 | 76.06 | 0.11 | 0.7398 |
| $AB$ | 2315.08 | 2 | 1157.54 | 1.71 | 0.1991 |
| $A^2B$ | 7298.69 | 2 | 3649.35 | 5.40 | 0.0106 |
| Residual (error puro) | 18,230.75 | 27 | 675.21 | | |
| Total corregido | 77,646.97 | 35 | | | |

Comprobaciones: $SS_A+SS_{A^2}=39{,}118.72$ (temperatura del ej. 5-1) y
$SS_{AB}+SS_{A^2B}=9613.77$ (interacción del ej. 5-1). $A^2$ y $AB$ no son significativos pero
$A^2B$ sí: se conservan todos por jerarquía.

Coeficientes en factores codificados ($A=-1,0,+1$ para 15, 70, 125 °F):

| Término | Coef. | Error est. | IC 95 % inf. | IC 95 % sup. |
|---|---|---|---|---|
| Intercepto | 107.58 | 7.50 | 92.19 | 122.97 |
| $A$ | −40.33 | 5.30 | −51.22 | −29.45 |
| $B[1]$ | −50.33 | 10.61 | −72.10 | −28.57 |
| $B[2]$ | 12.17 | 10.61 | −9.60 | 33.93 |
| $A^2$ | −3.08 | 9.19 | −21.93 | 15.77 |
| $AB[1]$ | 1.71 | 7.50 | −13.68 | 17.10 |
| $AB[2]$ | −12.79 | 7.50 | −28.18 | 2.60 |
| $A^2B[1]$ | 41.96 | 12.99 | 15.30 | 68.62 |
| $A^2B[2]$ | −14.04 | 12.99 | −40.70 | 12.62 |

**Variables indicadoras** del factor cualitativo (codificación de suma cero):

| | Material 1 | Material 2 | Material 3 |
|---|---|---|---|
| $B[1]$ | 1 | 0 | −1 |
| $B[2]$ | 0 | 1 | −1 |

Ecuaciones en factores reales (una por material, $T$ en °F):

- Material 1: $\widehat{\text{vida}}=169.38017-2.48860\,T+0.012851\,T^2$
- Material 2: intercepto $159.62397$; el libro imprime $-0.17901\,T+0.41627\,T^2$
  (dudoso, pág. 202).
- Material 3: intercepto $132.76240$; el libro imprime $+0.89264\,T-0.43218\,T^2$
  (dudoso, pág. 202).

> Nota de exactitud: los coeficientes impresos de los materiales 2 y 3 no reproducen las medias
> de celda del ejemplo 5-1. El modelo está saturado (9 parámetros, 9 celdas), de modo que cada
> ecuación debe pasar por las tres medias de su material; resolviendo con las medias de la
> tabla 5-4 se obtiene (cálculo propio, no del libro):
> material 2: $159.62397-0.17335\,T-0.0056612\,T^2$;
> material 3: $132.76240+0.90289\,T-0.010248\,T^2$.
> Los interceptos coinciden con los impresos; usar estos valores para validar software.

La fig. 5-18 muestra las tres curvas de vida contra temperatura (comparar con la fig. 5-9).

#### Ejemplo 5-5 — Vida de una herramienta de corte

Factores cuantitativos: $A$ = ángulo de la herramienta (15, 20, 25°), $B$ = velocidad de corte
(125, 150, 175 pulg/min); $3\times 3$ con $n=2$, datos codificados. Totales: ángulo
$-1,\ 16,\ 9$; velocidad $-2,\ 12,\ 14$; $y_{...}=24$. Design-Expert (tabla 5-17), "Response
Surface Reduced Order 4 Model":

| Fuente | SS | g.l. | MS | $F$ | Prob > F |
|---|---|---|---|---|---|
| Modelo | 111.00 | 8 | 13.87 | 9.61 | 0.0013 |
| $A$ | 49.00 | 1 | 49.00 | 33.92 | 0.0003 |
| $B$ | 16.00 | 1 | 16.00 | 11.08 | 0.0088 |
| $A^2$ | 0.000 | 1 | 0.000 | 0.000 | 1.0000 |
| $B^2$ | 1.33 | 1 | 1.33 | 0.92 | 0.3618 |
| $AB$ | 8.00 | 1 | 8.00 | 5.54 | 0.0431 |
| $A^2B$ | 2.67 | 1 | 2.67 | 1.85 | 0.2073 |
| $AB^2$ | 42.67 | 1 | 42.67 | 29.54 | 0.0004 |
| $A^2B^2$ | 8.00 | 1 | 8.00 | 5.54 | 0.0431 |
| Residual (error puro) | 13.00 | 9 | 1.44 | | |
| Total corregido | 124.00 | 17 | | | |

$R^2=0.8952$; $R^2$ ajustada 0.8020; $R^2$ de predicción 0.5806; PRESS 52.00; desv. est. 1.20;
media 1.33; C.V. 90.14; Adeq Precision 8.237. $AB$, $A^2B$, $AB^2$ y $A^2B^2$ son los
componentes lineal × lineal, cuadrático × lineal, lineal × cuadrático y cuadrático × cuadrático
de la interacción. Se conservan todos los términos por jerarquía.

Ecuación en factores codificados ($-1,0,+1$):

$$\hat y = 2.00+3.50A+2.00B+0.000A^2+1.00B^2-1.00AB-1.00A^2B-4.00AB^2-3.00A^2B^2$$

Errores estándar: intercepto 0.85; $A$ y $B$ 0.60; $A^2$ y $B^2$ 1.04; $AB$ 0.42; $A^2B$ y
$AB^2$ 0.74; $A^2B^2$ 1.27. VIF: 3.00 en todos salvo $AB$ (1.00) y $A^2B^2$ (5.00).

Ecuación en factores reales (ángulo $=x_A$, velocidad $=x_B$):

$$\hat y=-1068.0+136.3x_A+14.48x_B-4.08x_A^2-0.0496x_B^2-1.864x_Ax_B+0.056x_A^2x_B
+0.0064x_Ax_B^2-0.000192x_A^2x_B^2$$

Conclusión (figs. 5-19 y 5-20): la vida máxima se obtiene con velocidad cercana a 150 y ángulo
de 25°. (El texto dice "150 rpm" aunque la tabla 5-16 da la velocidad en pulg/min.) La
exploración de superficies de respuesta se desarrolla en el cap. 11.

---

## 5-6 Formación de bloques en un diseño factorial

**Cuándo.** No es posible o práctico aleatorizar por completo todas las corridas (lotes de
materia prima que solo alcanzan para $ab$ corridas, días, operadores…). Cada bloque contiene
**una réplica completa** del factorial y el orden se aleatoriza **dentro** del bloque.

**Modelo, dos factores en bloques completos (ec. 5-37):**

$$y_{ijk}=\mu+\tau_i+\beta_j+(\tau\beta)_{ij}+\delta_k+\varepsilon_{ijk}$$

$\delta_k$: efecto del bloque $k$ ($k=1..n$). **Supuesto:** la interacción bloques ×
tratamientos es insignificante; si existe no puede separarse del error (el error está formado
en realidad por $(\tau\delta)_{ik}$, $(\beta\delta)_{jk}$ y $(\tau\beta\delta)_{ijk}$).

**ANOVA (tabla 5-18):**

| Fuente | SS | g.l. | MS esperado | $F_0$ |
|---|---|---|---|---|
| Bloques | $\dfrac{1}{ab}\sum_k y_{..k}^2-\dfrac{y_{...}^2}{abn}$ | $n-1$ | $\sigma^2+ab\sigma_\delta^2$ | |
| $A$ | $\dfrac{1}{bn}\sum_i y_{i..}^2-\dfrac{y_{...}^2}{abn}$ | $a-1$ | $\sigma^2+\dfrac{bn\sum\tau_i^2}{a-1}$ | $MS_A/MS_E$ |
| $B$ | $\dfrac{1}{an}\sum_j y_{.j.}^2-\dfrac{y_{...}^2}{abn}$ | $b-1$ | $\sigma^2+\dfrac{an\sum\beta_j^2}{b-1}$ | $MS_B/MS_E$ |
| $AB$ | $\dfrac{1}{n}\sum_i\sum_j y_{ij.}^2-\dfrac{y_{...}^2}{abn}-SS_A-SS_B$ | $(a-1)(b-1)$ | $\sigma^2+\dfrac{n\sum\sum(\tau\beta)_{ij}^2}{(a-1)(b-1)}$ | $MS_{AB}/MS_E$ |
| Error | sustracción | $(ab-1)(n-1)$ | $\sigma^2$ | |
| Total | $\sum\sum\sum y_{ijk}^2-\dfrac{y_{...}^2}{abn}$ | $abn-1$ | | |

Es el ANOVA factorial con el error reducido en la suma de cuadrados de bloques. El libro no da
estadístico $F$ para bloques.

#### Ejemplo 5-6 — Detección de objetivos en radar

Respuesta: nivel de intensidad al detectarse el objetivo. Factores fijos: desorden de terreno
$G$ (bajo, intermedio, alto) y tipo de filtro $F$ (2). Bloques: 4 operadores elegidos al azar;
dentro de cada operador las 6 combinaciones se corren en orden aleatorio ($3\times2$ en DBCA).
Totales de operadores: 572, 579, 597, 530; $y_{...}=2278$; $SS_{\text{Bloques}}=402.17$.

| Fuente | SS | g.l. | MS | $F_0$ | Valor P |
|---|---|---|---|---|---|
| Desorden de terreno ($G$) | 335.58 | 2 | 167.79 | 15.13 | 0.0003 |
| Tipo de filtro ($F$) | 1066.67 | 1 | 1066.67 | 96.19 | <0.0001 |
| $GF$ | 77.08 | 2 | 38.54 | 3.48 | 0.0573 |
| Bloques | 402.17 | 3 | 134.06 | | |
| Error | 166.33 | 15 | 11.09 | | |
| Total | 2047.83 | 23 | | | |

$G$ y $F$ significativos al 1 %; la interacción solo al 10 % (evidencia ligera).

### Dos restricciones sobre la aleatorización: factorial en cuadrado latino

Si hay dos restricciones, cada una con $p$ niveles, y el número de combinaciones de
tratamientos del factorial es exactamente $p$ ($p=ab\cdots m$), el factorial puede correrse en
un **cuadrado latino $p\times p$**: las letras latinas son las combinaciones de tratamientos.

Variante del ejemplo 5-6: solo caben 6 corridas por día ⇒ días (renglones) y operadores
(columnas, ahora 6) como restricciones; cuadrado latino $6\times6$ con las letras
$A=f_1g_1$, $B=f_1g_2$, $C=f_1g_3$, $D=f_2g_1$, $E=f_2g_2$, $F=f_2g_3$ (tabla 5-21). Los 5 g.l.
entre letras se parten en filtro (1), desorden de terreno (2) e interacción (2).

Modelo (ec. 5-38):

$$y_{ijkl}=\mu+\alpha_i+\tau_j+\beta_k+(\tau\beta)_{jk}+\theta_l+\varepsilon_{ijkl}$$

$\alpha_i$: días ($i=1..6$); $\tau_j$: desorden de terreno ($j=1..3$); $\beta_k$: filtro
($k=1,2$); $\theta_l$: operadores ($l=1..6$).

ANOVA (tabla 5-22), con la fórmula general de los g.l.:

| Fuente | SS | g.l. | Fórmula g.l. | MS | $F_0$ | Valor P |
|---|---|---|---|---|---|---|
| Desorden de terreno, $G$ | 571.50 | 2 | $a-1$ | 285.75 | 28.86 | <0.0001 |
| Tipo de filtro, $F$ | 1469.44 | 1 | $b-1$ | 1469.44 | 148.43 | <0.0001 |
| $GF$ | 126.73 | 2 | $(a-1)(b-1)$ | 63.37 | 6.40 | 0.0071 |
| Días (renglones) | 4.33 | 5 | $ab-1$ | 0.87 | | |
| Operadores (columnas) | 428.00 | 5 | $ab-1$ | 85.60 | | |
| Error | 198.00 | 20 | $(ab-1)(ab-2)$ | 9.90 | | |
| Total | 2798.00 | 35 | $(ab)^2-1$ | | | |

(El libro imprime 36 g.l. para el total; la fórmula $(ab)^2-1$ y la suma de los renglones dan
35: errata, pág. 210.) Totales útiles: tratamientos por filtro 1813 y 1583; por desorden 1072,
1135, 1189; $y_{....}=3396$; renglones 563, 568, 568, 568, 565, 564; columnas 572, 579, 597,
530, 561, 557.

Otros aspectos de bloques en factoriales (confusión, etc.): caps. 7, 8, 9 y 13.

---

## 5-7 Problemas (solo índice temático)

- 5-1 a 5-8: factoriales de dos factores con réplicas (ANOVA, residuales, condiciones de
  operación, IC para diferencia de medias en 5-3, ajuste de modelo en 5-8).
- 5-9, 5-10: modelo de regresión y prueba de Tukey sobre los datos de 5-1.
- 5-11: modelo sin interacción. 5-12: deducir los cuadrados medios esperados con una
  observación por celda.
- 5-13, 5-14: una observación por celda y prueba de no aditividad.
- 5-15: tres factores con una sola réplica (qué usar como error).
- 5-16, 5-17: factoriales de tres factores.
- 5-18: tamaño de muestra con curvas OC.
- 5-19 a 5-21: factoriales con réplicas como bloques.
- 5-22: transformación $\ln(y)$. 5-23: ajuste de superficie de respuesta
  $y=\beta_0+\beta_1x_1+\beta_2x_2+\beta_{22}x_2^2+\beta_{12}x_1x_2+\varepsilon$.

---

## Resumen operativo

1. Aleatorizar por completo las $abn$ corridas (o dentro de bloques si hay restricciones).
2. Ajustar el modelo de efectos con interacción; ANOVA con $F_0=MS/MS_E$ (efectos fijos).
3. **Probar primero la interacción.** Si es significativa, interpretar con la gráfica de medias
   de celda y comparar niveles de un factor fijando el otro (Tukey con $\sqrt{MS_E/n}$).
4. Verificar supuestos con $e_{ijk}=y_{ijk}-\bar y_{ij.}$: normalidad, varianza constante
   contra ajustados y contra cada factor.
5. Con $n=1$: no hay estimación de $\sigma^2$ salvo que se suponga aditividad; verificarla con
   la prueba de Tukey de 1 g.l.
6. Tamaño de muestra: curvas OC con $\Phi^2$ mínimo para una diferencia $D$.
7. Factores cuantitativos: descomponer en efectos polinomiales de 1 g.l., ajustar curva o
   superficie de respuesta y respetar (con criterio) la jerarquía.
