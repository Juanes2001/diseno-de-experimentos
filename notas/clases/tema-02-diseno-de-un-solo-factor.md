# Tema 2 — Diseño de un solo factor (registro de las diapositivas de la profesora)

Curso: Diseño de Experimentos Avanzados (3008475), UNAL, 2026-II.
Pie de todas las diapositivas: *Alexander Correa Espinal & Faviana Gutiérrez Rôa – Universidad Nacional de Colombia*. Marca lateral: *Diseño de Experimentos Intermedio*.

**Fuente:** 49 fotografías del proyector en
`notas/Diseño de un solo factor/WhatsApp Unknown 2026-10-03 at 6.57.20 PM/`.
Todos los archivos se llaman `WhatsApp Image 2026-10-03 at <hora>.jpeg`; aquí se citan solo por la hora, p. ej. `6.56.04 PM (1)`.

**Cobertura:** 49 fotos = 46 diapositivas distintas (3 fotos son duplicados). Todas se leen bien; no hay imágenes ilegibles.

**Sobre el orden:** las diapositivas no muestran número. El orden de abajo se reconstruyó por contenido (títulos "1/3, 2/3…", la lista de pasos de "¿Cómo debo analizar los datos recolectados?" y la secuencia de nombres de archivo). Las posiciones dudosas están marcadas con **(posición dudosa)**.

**Diapositivas que faltan en las fotos** (se deducen de la numeración "k/n" de los títulos): Probabilidad normal 2/3 y 3/3; Predichos vs residuos 2/3 y 3/3; Residuos vs tiempo 2/3 y 3/3; Método de Fisher o LSD 3/3; Método de Tukey 2/2; Método de Duncan 3/3. Tampoco hay fotos de la portada, de una diapositiva de "cuándo usar el diseño", ni de capturas de pantalla de Minitab (solo las dos diapositivas introductorias del bloque de software).

**Convención de este registro:** el texto en letra normal es el cuerpo de la diapositiva; lo marcado como *Nota al margen* es el texto que la profesora pone en letra cursiva tipo manuscrita (comentarios y glosario de símbolos). Las *Notas de transcripción* son observaciones mías y no están en la diapositiva.

---

## Registro diapositiva por diapositiva

### 1. Tiempo de coagulación de la sangre en pollos **(posición dudosa: ejemplo motivador; en el orden de archivos aparece justo antes del bloque de comparaciones)**
Archivo: `6.55.56 PM (3)`

En la siguiente tabla se presentan los tiempos de coagulación de muestras de sangre extraída a 24 pollos alimentados con cuatro dietas diferentes A, B, C y D. Las dietas fueron asignadas aleatoriamente a los pollos y las muestras de sangre fueron extraídas y analizadas en el orden aleatorio indicado por los superíndices que están entre paréntesis. ¿Hay alguna evidencia que indique una diferencia real entre los tiempos medios de coagulación de las cuatro dietas?

| A | B | C | D |
|---|---|---|---|
| (20) 62 | (12) 63 | (16) 68 | (23) 56 |
| (2) 60 | (9) 67 | (7) 66 | (3) 62 |
| (11) 63 | (15) 71 | (1) 71 | (6) 60 |
| (10) 59 | (14) 64 | (17) 67 | (18) 61 |
| (5) 63 | (4) 65 | (13) 68 | (22) 63 |
| (24) 59 | (8) 66 | (21) 68 | (19) 64 |

*Nota al margen:* (#) orden de ejecución, obtenido aleatoriamente.

Gráfica: dibujo decorativo de pollitos alrededor de un comedero. (El borde derecho de la foto corta la última letra de algunas líneas del enunciado; el texto se completa sin ambigüedad.)

### 2. ¿Cuál es el modelo matemático del diseño?
Archivo: `6.56.04 PM`

$$Y_{ij} = \mu + \tau_i + \varepsilon_{ij} \qquad \begin{cases} i = 1 \cdots a \\ j = 1 \cdots n \end{cases}$$

Etiquetas con flechas sobre cada término (cada término resaltado con un círculo de color):
- $\mu$: Media global (común a todos los tratamientos).
- $\tau_i$: Efecto del nivel o tratamiento.
- $\varepsilon_{ij}$: Error aleatorio.

Gráfica: eje horizontal con los tratamientos $T_1, T_2, T_3, T_4, \ldots, T_a$; línea horizontal en la media global $\mu$; para cada tratamiento un punto $\mu_i$ por encima o por debajo de la línea y una llave que marca la distancia $\tau_i$ entre $\mu$ y $\mu_i$ ($\mu_1$ y $\mu_4$ por encima, $\mu_2$ y $\mu_3$ por debajo, $\mu_a$ ligeramente por encima).

### 3. Efectos fijos y efectos aleatorios
Archivo: `6.56.04 PM (1)`

**Modelo de efectos fijos:** es cuando se estudian todos los posibles tratamientos, porque son una población pequeña.

**Modelo de efectos aleatorios:** es cuando los tratamientos del factor son una muestra aleatoria de la población de tratamientos para ese factor, de modo que el efecto del tratamiento $i$ ($\tau_i$) pasa a ser una variable aleatoria con su propia varianza $\sigma_\tau^2$ que deberá estimarse a partir de los datos.

### 4. Diseño balanceado **(posición dudosa: el archivo quedó entre las diapositivas de homocedasticidad; por contenido va con el modelo / número de réplicas)**
Archivo: `6.56.20 PM (1)`

**Diseño balanceado:** es cuando se utiliza el mismo numero de repeticiones en cada tratamiento, que es lo más recomendable ($n_i = n$).

Si uno de los tratamientos resulta demasiado caro en comparación con los demás o cuando es muy retardado realizar las pruebas, se pueden plantear menos pruebas con éste, con lo cual sólo se podrán detectar diferencias grandes en los tratamientos.

Cuando uno de los tratamientos es un control (tratamiento de referencia), muchas veces es más fácil y económico de probar, y como se pretende comparar a todos los tratamientos restantes con el de control, se sugiere realizar más corridas en éste para que sus parámetros queden mejor estimados.

### 5. ¿Cuál es la hipótesis del diseño?
Archivo: `6.56.05 PM`

Recuadro titulado **Prueba para la media (Efectos fijos)**:

$$H_0: \mu_1 = \mu_2 = \ldots = \mu_a = \mu$$
$$H_A: \mu_i \neq \mu_j \ \text{para algún } i \neq j$$

*Nota al margen:* Con lo cual se quiere decidir si los tratamientos son iguales estadísticamente en cuanto a sus medias, frente a la alternativa de que al menos dos de ellos son diferentes.

También se puede escribir en forma equivalente como:

$$H_0: \tau_1 = \tau_2 = \ldots = \tau_a = 0$$
$$H_A: \tau_i \neq 0 \ \text{para algún } i$$

Donde $\tau_i$ es el efecto del tratamiento $i$ sobre la variable respuesta.

### 6. ¿Cómo debo recolectar los datos?
Archivo: `6.56.05 PM (1)`

Todas las corridas experimentales se deben realizar en un orden aleatorio o completamente al azar para evitar efectos sistemáticos de factores ajenos a la experimentación.

Asimismo, se sugiere establecer un protocolo de experimentación que garantice la estandarización de la experimentación.

Tabla (encabezado único "Tratamientos"):

| Tratamientos | | | | |
|---|---|---|---|---|
| $Y_{11}$ | $Y_{21}$ | $Y_{31}$ | $\ldots$ | $Y_{a1}$ |
| $Y_{12}$ | $Y_{22}$ | $Y_{32}$ | $\ldots$ | $Y_{a2}$ |
| $Y_{13}$ | $Y_{23}$ | $Y_{33}$ | $\ldots$ | $Y_{a3}$ |
| $\vdots$ | $\vdots$ | $\vdots$ | | $\vdots$ |
| $Y_{1n_1}$ | $Y_{2n_2}$ | $Y_{3n_3}$ | | $Y_{an_a}$ |

*Nota al margen:* Los datos recolectados deben tabularse para su posterior análisis.
- $T_i \equiv$ Tratamiento $i$
- $a \equiv$ Cantidad de tratamientos
- $n \equiv$ Cantidad de réplicas

### 7. ¿Cuántos datos debo recolectar? 1/3
Archivo: `6.56.06 PM`

En cualquier diseño de experimentos, es vital decidir el número de réplicas que se hará por cada tratamiento, el cual incidirá directamente en el tamaño de la muestra a recolectar.

En la práctica se suele utilizar un número de réplicas que varía entre cinco a diez, para diseños de un solo factor, pudiendo llegar hasta 30, según las siguientes consideraciones:
- A menor diferencia que se espera en los tratamientos, mayor será la cantidad de réplicas si se quieren detectar diferencias significativas, y viceversa.
- Si se espera mucha variación dentro de cada tratamiento, debido a la varianza de factores no controlados, entonces se necesitarán más réplicas.
- Si son cuatro o más tratamientos, se sugiere reducir el número de réplicas.
- Se debe tener en cuenta los costos y tiempo global del experimento.

### 8. ¿Cuántos datos debo recolectar? 2/3
Archivo: `6.56.06 PM (1)`

Si el experimentador tiene:
- El número de tratamientos que desea probar $a$
- Una propuesta inicial del número de réplicas por tratamiento que va a recolectar $n_0$
- Una idea aproximada de la desviación estándar del error aleatorio $\sigma$
- Una idea de la magnitud de las diferencias $d_T$ entre tratamientos que le interesa detectar.

El método LSD permite obtener una idea del número de réplicas por tratamiento y por el número total de corridas experimentales $N = a \times n$. Si de la expresión para la prueba de rangos múltiples LSD, despejamos $n$ y suponemos que se utiliza el mismo numero de repeticiones en cada tratamiento, se obtiene:

$$n = \frac{2\left(t_{\alpha/2,\,N-a}\right)^2 MS_E}{(LSD^2)}$$

### 9. ¿Cuántos datos debo recolectar? 3/3
Archivo: `6.56.07 PM`

**Ejemplo:** Si para el caso de los tiempos promedio de los $a = 4$ métodos de ensambles, se tiene idea de realizar $n_0 = 5$ pruebas, en cuanto a las diferencias, interesa detectar 2 minutos, $d_T = 2$, entre un método y otro, y se espera que cada método tenga una variabilidad intrínseca de $\sigma = 1.5$, debido a la presencia de factores no controlados.

Luego:

$$n = \frac{2\left(t_{\alpha/2,\,N-a}\right)^2 MS_E}{(LSD^2)}$$

$$n = \frac{2\left(t_{\alpha/2,\,a \times n_0 - a}\right)^2 \sigma}{(d_T^{\,2})} = \frac{2\left(t_{0.025,15}\right)^2 (1.5)^2}{2^2} = 5.1$$

Por tanto, $n = 5$ debería ser el número de pruebas por tratamiento.

*Nota de transcripción:* la diapositiva escribe $\sigma$ (sin cuadrado) en la expresión simbólica y $(1.5)^2$ en la numérica; y usa $t_{0.025,15}$ aunque $a \times n_0 - a = 16$. Se transcribe tal cual.

### 10. ¿Cómo debo analizar los datos recolectados?
Archivo: `6.56.07 PM (1)`

1. Calcular el ANOVA usando los datos.
2. Estimar el valor crítico con las tablas de distribución o el valor-p con *software* estadístico.
3. Aplicar el criterio de rechazo apropiado.
4. Verificar los supuestos del modelo.
5. Si se rechazó la hipótesis nula, realizar comparación de medias.
6. Informar la conclusión en términos del problema establecido por el investigador.

Gráfica: imagen decorativa de tres engranajes de colores con flechas.

### 11. Tabla ANOVA (descripción en palabras)
Archivos: `6.55.56 PM` y `6.55.56 PM (1)` (misma diapositiva, dos fotos)

Es una tabla resumen del análisis de varianza de un experimento, que sirve para probar las hipótesis de interés.

| Fuente de Variación | Suma de Cuadrados | Grados de Libertad | Cuadrados Medios | Estadístico de Prueba | P-Value |
|---|---|---|---|---|---|
| Tratamientos | Suma de cuadrados de los tratamientos | Grados de libertad de los tratamientos | Cuadrado medio de los tratamientos | Estadístico de prueba | $P(F_t > F_o)$ |
| Error | Suma de cuadrados del error | Grados de libertad del error | Cuadrado medio del error | | |
| Total | Suma de cuadrados totales | Grados de libertad del total | | | |

### 12. Tabla ANOVA (fórmulas)
Archivo: `6.56.08 PM`

| SV | SS | DF | MS | $F_O$ | P-Value |
|---|---|---|---|---|---|
| Trat. | $SS_{TRAT} = \sum_{i=1}^{a} \dfrac{y_{i.}^2}{n} - \dfrac{y_{..}^2}{N}$ | $a - 1$ | $MS_{TRAT} = \dfrac{SS_{TRAT}}{a-1}$ | $\dfrac{MS_{TRAT}}{MS_E}$ | $P(F_t > F_O)$ |
| Error | $SS_E = SS_T - SS_{TRAT}$ | $N - a$ | $MS_E = \dfrac{SS_E}{N-a}$ | | |
| Total | $SS_T = \sum_{i=1}^{a}\sum_{j=1}^{n} y_{ij}^2 - \dfrac{y_{..}^2}{N}$ | $N - 1$ | | | |

### 13. Procedimientos de Prueba de Hipótesis (tabla resumen de repaso) **(posición dudosa: en el orden de archivos va entre "Tabla ANOVA" y el ejemplo de los pollos)**
Archivo: `6.55.56 PM (2)`

Diapositiva sin título superior; el rótulo "Procedimientos de Prueba de Hipótesis" va al pie de la tabla. Las tres últimas columnas son los criterios de rechazo según la alternativa.

| # | $H_0$ | Estadístico | G.L. / Varianza | $H_A: \neq$ | $H_A: >$ | $H_A: <$ |
|---|---|---|---|---|---|---|
| 1 | $H_0: \mu = \mu_0$ | $z_0 = \dfrac{\bar{X} - \mu_0}{\sigma/\sqrt{n}}$ | | $\lvert z_0\rvert > z_{\alpha/2}$ | $z_0 > z_\alpha$ | $z_0 < -z_\alpha$ |
| 2 | $H_0: \mu = \mu_0$ | $t_0 = \dfrac{\bar{X} - \mu_0}{S/\sqrt{n}}$ | $\nu = n - 1$ | $\lvert t_0\rvert > t_{\alpha/2,\nu}$ | $t_0 > t_{\alpha,\nu}$ | $t_0 < -t_{\alpha,\nu}$ |
| 3 | $H_0: \mu_1 = \mu_2$ | $Z_0 = \dfrac{\bar{X}_1 - \bar{X}_2}{\sqrt{\dfrac{\sigma_1^2}{n_1} + \dfrac{\sigma_2^2}{n_2}}}$ | | $\lvert z_0\rvert > z_{\alpha/2}$ | $z_0 > z_\alpha$ | $z_0 < -z_\alpha$ |
| 4 | $H_0: \mu_1 = \mu_2$ | $t_0 = \dfrac{\bar{X}_1 - \bar{X}_2}{S_p\sqrt{\dfrac{1}{n_1} + \dfrac{1}{n_2}}}$ | $S_p^2 = \dfrac{(n_1-1)S_1^2 + (n_2-1)S_2^2}{n_1+n_2-2}$, $\ \nu = n_1 + n_2 - 2$ | $\lvert t_0\rvert > t_{\alpha/2,\nu}$ | $t_0 > t_{\alpha,\nu}$ | $t_0 < -t_{\alpha,\nu}$ |
| 5 | $H_0: \mu_1 = \mu_2$ | $t_0 = \dfrac{\bar{X}_1 - \bar{X}_2}{\sqrt{\dfrac{S_1^2}{n_1} + \dfrac{S_2^2}{n_2}}}$ | $\nu = \dfrac{\left(\dfrac{S_1^2}{n_1} + \dfrac{S_2^2}{n_2}\right)^2}{\dfrac{(S_1^2/n_1)^2}{n_1+1} + \dfrac{(S_2^2/n_2)^2}{n_2+1}} - 2$ | $\lvert t_0\rvert > t_{\alpha/2,\nu}$ | $t_0 > t_{\alpha,\nu}$ | $t_0 < -t_{\alpha,\nu}$ |
| 6 | $H_0: \mu_1 = \mu_2$ | $t_0 = \dfrac{\bar{d}}{S_d/\sqrt{n}}$ | $\nu = n - 1$ | $\lvert t_0\rvert > t_{\alpha/2,\nu}$ | $t_0 > t_{\alpha,\nu}$ | $t_0 < -t_{\alpha,\nu}$ |
| 7 | $H_0: \sigma_1^2 = \sigma_2^2$ | $F_0 = \dfrac{S_1^2}{S_2^2}$ | $\nu_1 = n_1 - 1$, $\ \nu_2 = n_2 - 1$ | $F_0 > F_{\alpha/2,\nu_1,\nu_2}$ | $F_0 > F_{\alpha,\nu_1,\nu_2}$ | $F_0 < F_{1-\alpha,\nu_1,\nu_2}$ |

(Los subíndices de las columnas de criterio son muy pequeños en la foto; se leen como se indica, coherentes con la tabla estándar.)

### 14. ¿Qué debemos verificar sobre el modelo?
Archivo: `6.56.14 PM`

La validez de los resultados obtenidos con un análisis de varianza depende del cumplimiento de los supuestos del modelo. La correcta aplicación de los tres principios básicos del diseño de experimentos: aleatorización, réplica y bloqueo permiten evitar que los supuestos del modelo se violen.

Para comprobar estos supuestos se utilizan los residuos del modelo $e_{ij}$ los cuales se estiman como la diferencia entre el valor de la respuesta observada $Y_{ij}$ y el valor de la respuesta estimada con el modelo $\hat{Y}_{ij}$, de otra forma se podría expresar como:

$$e_{ij} = Y_{ij} - \hat{Y}_{ij} = Y_{ij} - \bar{Y}_{i.}$$

### 15. Supuestos sobre los errores del modelo
Archivo: `6.56.15 PM`

Cuatro recuadros de colores, uno por supuesto:
- El error sigue una distribución normal
- La varianza es constante
- Las mediciones son independientes entre sí
- La media de los errores es cero

### 16. ¿Cómo comprobar los supuestos del modelo?
Archivo: `6.56.15 PM (1)`

Para comprobar los supuestos se pueden utilizar pruebas gráficas y/o analíticas.

Diagrama de árbol:

| Tipo de prueba | Supuesto | Herramienta |
|---|---|---|
| **Pruebas Gráficas** | Normalidad | Probabilidad Normal; Histograma de Residuos |
| | Varianza Constante | Predichos vs Residuos; Niveles del Factor vs Residuos |
| | Independencia | Residuos vs Tiempo |
| **Pruebas Analíticas** | Normalidad | Shapiro-Wilks; Kolmogorov-Smirnov; Chi-Cuadrado |
| | Varianza Constante | Bartlett; Levene |
| | Independencia | Durbin-Watson |

*Notas al margen:* (Pruebas gráficas) Son sencillas de realizar pero no son exactas. (Pruebas analíticas) Se usan para comprobar las dudas que puedan surgir de las pruebas gráficas.

### 17. Probabilidad normal 1/3
Archivo: `6.56.15 PM (2)`

El procedimiento gráfico para verificar el cumplimiento del supuesto de normalidad de los residuos consiste en graficar los residuos en papel o en la gráfica de probabilidad normal.

La gráfica del tipo $X - Y$ tiene las escalas de tal manera que si los residuos siguen una distribución normal, al graficarlos tienden a quedar alineados en una línea recta; por lo tanto, si claramente no se alinean se concluye que el supuesto de normalidad no es correcto.

Cabe enfatizar el hecho de que el ajuste de los puntos a una recta no tiene que ser perfecto, dado que el análisis de varianza resiste pequeñas y moderadas desviaciones al supuesto de normalidad.

(Faltan las fotos de Probabilidad normal 2/3 y 3/3.)

### 18. Histograma de residuos
Archivo: `6.56.15 PM (3)`

El histograma de residuos es una herramienta exploratoria para mostrar las características generales de los residuos incluyendo valores típicos, dispersión y forma.

- **Forma** — dos mini-histogramas: uno simétrico con una curva normal superpuesta, *¿Parecen estar distribuidos normalmente los residuos?*; otro con las barras crecientes hacia la derecha (asimétrico), *¿Están sesgados hacia la izquierda o hacia la derecha?*
- **Dispersión** — dos mini-histogramas: uno con las barras concentradas en el centro, encerradas en un óvalo rojo, *¿Están los residuos conglomerados ajustadamente alrededor de cierto valor?*; otro con dos líneas verticales rojas a los lados, *¿Se mantienen dentro de los límites establecidos?*
- **Atípicos** — *Si una o dos barras están lejos de las demás, esos puntos pueden ser valores atípicos.*

### 19. Predichos *vs* residuos 1/3
Archivo: `6.56.16 PM`

Una forma de verificar el supuesto de varianza constante (o que los tratamientos tienen la misma varianza) es graficando los predichos $(\hat{Y}_{ij})$ contra los residuos $(e_{ij})$, por lo general los predichos van en el eje horizontal y los residuos en el eje vertical.

Si los puntos en esta gráfica se distribuyen de manera aleatoria en una banda horizontal (sin ningún patrón claro y contundente), entonces es señal de que se cumple el supuesto de que los tratamientos tienen igual varianza.

Por el contrario, si los puntos se distribuyen con algún patrón claro y contundente, como una "corneta o embudo", o si existe predominancia de residuos positivos o predominancia de residuos negativos; entonces no se cumple el supuesto de varianza constante, lo cual indica que el error de pronóstico del modelo tiene una relación directa (positiva o negativa) con la magnitud del pronóstico (predicho).

(Faltan las fotos de Predichos vs residuos 2/3 y 3/3.)

### 20. Residuos *vs* tiempo 1/3
Archivo: `6.56.16 PM (1)`

La suposición de la independencia en los residuos puede verificarse si se grafica el orden en que se colectó un dato contra el residuo correspondiente.

Si al graficar en el eje horizontal el tiempo (orden de corrida) y en el eje vertical los residuos, se detecta una tendencia o patrón no aleatorio claramente definido dentro de una banda horizontal, el supuesto de independencia no se cumple, puesto que existe una correlación entre los errores. Una correlación positiva es indicada por un conglomerado de residuos con el mismo signo. Una correlación negativa es indicada por los cambios rápidos en los signos de residuos consecutivos.

(Faltan las fotos de Residuos vs tiempo 2/3 y 3/3.)

### 21. Pruebas analíticas de normalidad
Archivo: `6.56.16 PM (2)`

**Prueba de normalidad de Shapiro-Wilk:** Evalúa la normalidad calculando la correlación entre sus datos y las puntuaciones normales de sus datos. Si el coeficiente de correlación se encuentra cerca de 1, es probable que la población sea normal. Esta prueba evalúa la solidez de esta correlación; si se encuentra por debajo del valor crítico se rechaza la hipótesis nula.

**Prueba de normalidad de Kolmogorov-Smirnov:** Esta prueba compara la función de distribución acumulada empírica de los datos de su muestra, con la distribución esperada si los datos son normales. Si esta diferencia observada es suficientemente grande, la prueba rechazará la hipótesis nula de normalidad en la población. Si el valor p de esta prueba es menor que su nivel $\alpha$ elegido, se rechaza la hipótesis nula y se concluye que la población es no normal.

*Nota al margen:* La prueba de Kolmogorov-Smirnov tiene una potencia menor que la prueba de Shapiro-Wilk.

### 22. Prueba Shapiro-Wilks 1/3
Archivo: `6.56.17 PM`

Es la prueba más recomendada para probar la normalidad de una muestra cuando se trabaja con un numero pequeño de datos ($n < 30$). Se basa en medir el ajuste de los datos a una recta de probabilidad normal.

- Hipótesis a probar:
  - $H_0$: *Los datos se distribuyen normal*
  - $H_A$: *Los datos no se distribuyen normal*
- Ordenar los residuos de menor a mayor
- Obtener los coeficientes $a_i$
- Calcular el estadístico:

$$W = \frac{1}{(N-1)S^2}\left[\sum_{i=1}^{k} a_i\left(X_{(N-i+1)}\right) - X_{(i)}\right]^2$$

- Obtener el valor critico $W_{1-\alpha,N}$
- Se rechaza $H_0$ si: $W > W_{1-\alpha,N}$

*Notas al margen (glosario):*
- ■ Tabla de Shapiro-Wilks
- $a_i \equiv$ Coeficientes obtenidos de la tabla de Shapiro-Wilks donde $k \cong n/2$
- $N \equiv$ número de residuos
- $\alpha \equiv$ nivel de significancia prefijado
- $S^2 \equiv$ cuadrado medio del error

### 23. Prueba Shapiro-Wilks 2/3
Archivo: `6.56.17 PM (1)`

**Ejemplo:** Al comparar cuatro métodos de ensamble en cuanto al tiempo promedio [min] se obtienen los siguientes residuos:

| Tratamientos | A | B | C | D |
|---|---|---|---|---|
| Residuos | 1.25 | 1.5 | 1.75 | 0.5 |
| | 0.75 | 0.5 | 3.25 | 1.5 |
| | 0.25 | 1.5 | 1.75 | 0.5 |
| | 0.75 | 0.5 | 0.25 | 1.5 |

$\alpha = 0.05$, $n = 16$, $S^2 = 6.6$

$$k = \frac{n}{2} = \frac{16}{2} = 8$$

Hipótesis a probar:
- $H_0$: *Los datos se distribuyen normal*
- $H_A$: *Los datos no se distribuyen normal*

*Nota al margen:* Residuos ordenados de menor a mayor:

| $X_1$ | $X_2$ | $X_3$ | $X_4$ | $X_5$ | $X_6$ | $X_7$ | $X_8$ | $X_9$ | $X_{10}$ | $X_{11}$ | $X_{12}$ | $X_{13}$ | $X_{14}$ | $X_{15}$ | $X_{16}$ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | 0.25 | 0.50 | 0.50 | 0.50 | 0.50 | 0.75 | 0.75 | 1.25 | 1.50 | 1.50 | 1.50 | 1.50 | 1.75 | 1.75 | 3.25 |

*Nota de transcripción:* los residuos aparecen en valor absoluto (sin signo) en esta diapositiva; los mismos residuos con signo están en la diapositiva de Durbin-Watson 2/2.

### 24. Prueba Shapiro-Wilks 3/3
Archivo: `6.56.17 PM (2)`

Obtener coeficientes $a_i$ y calcular el estadístico $W$

| $i$ | $a_i$ | $\left(X_{(N-i+1)} - X_{(i)}\right)$ | $a_i\left(X_{(N-i+1)} - X_{(i)}\right)$ |
|---|---|---|---|
| 1 | 0.5056 | 3.25 − 0.25 = 3.0 | 1.5168 |
| 2 | 0.3290 | 1.75 − 0.25 = 1.50 | 0.4935 |
| 3 | 0.2521 | 1.75 − 0.50 = 1.25 | 0.3151 |
| 4 | 0.1988 | 1.50 − 0.50 = 1.0 | 0.1988 |
| 5 | 0.1447 | 1.50 − 0.50 = 1.0 | 0.1447 |
| 6 | 0.1005 | 1.50 − 0.50 = 1.0 | 0.1005 |
| 7 | 0.0593 | 1.50 − 0.75 = 0.75 | 0.0444 |
| 8 | 0.0196 | 1.25 − 0.75 = 0.50 | 0.0098 |

$\alpha = 0.05$, $N = 16$, $k = \dfrac{n}{2} = \dfrac{16}{2} = 8$

$$W = \frac{1}{(N-1)S^2}\left[\sum_{i=1}^{k} a_i\left(X_{(N-i+1)}\right) - X_{(i)}\right]^2 = \frac{1}{99} * 7.9732 = 0.0805$$

$$W_{0.95,16} = 0.981$$

(Una flecha apunta de $W$ hacia el valor crítico.) *Nota al margen:* Se acepta $H_0$ los residuos son normales.

### 25. Pruebas analíticas de varianza constante
Archivo: `6.56.18 PM`

**Prueba de Bartlett:** Utilícela cuando los datos provengan de distribuciones normales; la prueba de Bartlett no es sólida cuando los datos se apartan de la normalidad.

**Prueba de Levene:** Utilícela cuando los datos provengan de distribuciones continuas, pero no necesariamente distribuciones normales. Este método considera las distancias de las observaciones con respecto a la mediana de la muestra en lugar de la media de la muestra, esto hace que la prueba sea más sólida para las muestras más pequeñas.

**Prueba F:** utilícela en lugar de la prueba de Bartlett cuando compare sólo dos varianzas.

### 26. Prueba de Bartlett 1/2
Archivo: `6.56.18 PM (1)`

Es la prueba más recomendada para probar homogeneidad de varianzas de $a$ tratamientos independientes, cada uno con distribución normal, donde las varianzas son desconocidas.

- Hipótesis a probar:

$$H_0: \sigma_1^2 = \sigma_2^2 = \cdots = \sigma_a^2 = \sigma^2$$
$$H_A: \sigma_i^2 \neq \sigma_j^2 \ \text{para algún } i \neq j$$

- Calcular el estadístico:

$$\chi_0^2 = 2.3026\,\frac{q}{c}$$
$$q = (N-a)\log_{10} S_p^2 - \sum_{i=1}^{a}(n_i - 1)\log_{10} S_i^2$$
$$c = 1 + \frac{1}{3(a-1)}\left(\sum_{i=1}^{a}(n_i-1)^{-1} - (N-a)^{-1}\right)$$
$$S_p^2 = \frac{\sum_{i=1}^{a}(n_i-1)S_i^2}{N-a}$$

- Se rechaza $H_0$ si: $\chi_0^2 > \chi^2_{(\alpha,\,a-1)}$

*Notas al margen (glosario):*
- ■ Tabla de $\chi^2$
- $a \equiv$ número de niveles o tratamientos
- $n_i \equiv$ número de observaciones del tratamiento $i$
- $N \equiv$ número total de observaciones
- $\alpha \equiv$ nivel de significancia prefijado
- $S_i^2 \equiv$ varianza de cada tratamiento
- $S_p^2 \equiv$ varianza poblacional estimada

### 27. Prueba de Bartlett 2/2
Archivo: `6.56.18 PM (2)`

**Ejemplo:** Al comparar cuatro métodos de ensamble en cuanto al tiempo promedio [min] que requiere cada uno de ellos se obtuvo:

| Tratamientos | A | B | C | D |
|---|---|---|---|---|
| Observaciones | 6 | 7 | 11 | 10 |
| | 8 | 9 | 16 | 12 |
| | 7 | 10 | 11 | 11 |
| | 8 | 8 | 13 | 9 |
| $S_i^2$ | 0.92 | 1.67 | 5.58 | 1.67 |

- Hipótesis a probar:

$$H_0: \sigma_1^2 = \sigma_2^2 = \cdots = \sigma_a^2 = \sigma^2$$
$$H_A: \sigma_i^2 \neq \sigma_j^2 \ \text{para algún } i \neq j$$

$\alpha = 0.05$; $\ n_A = n_B = n_C = n_D = 4$

$$S_p^2 = \frac{\sum_{i=1}^{a}(n_i-1)S_i^2}{N-a} = \frac{29.50}{12} = 2.46$$
$$q = (N-a)\log_{10} S_p^2 - \sum_{i=1}^{a}(n_i-1)\log_{10} S_i^2 = 12(0.39) - 3.46 = 1.23$$
$$c = 1 + \frac{1}{3(a-1)}\left(\sum_{i=1}^{a}(n_i-1)^{-1} - (N-a)^{-1}\right) = 1 + \frac{1}{9} * 1.25 = 1.14$$
$$\chi_0^2 = 2.3026\,\frac{q}{c} = 2.3026 * \frac{1.23}{1.14} = 2.48 \quad\Rightarrow\quad \chi^2_{(0.05,3)} = 7.81$$

*Nota al margen:* Se acepta $H_0$ los residuos son homocedásticos.

### 28. Prueba de Durbin-Watson 1/2
Archivo: `6.56.18 PM (3)`

Es la prueba que permite diagnosticar la correlación entre residuos consecutivos; sin embargo, no detecta correlaciones entre residuos no consecutivos, lo cual también viola el concepto de independencia. Este tipo de correlación ocurre en un experimento cuando la contaminación no se refleja de inmediato, sino que actúa con retardo.

- Hipótesis a probar:

$$H_0: \rho = 0$$
$$H_A: \rho > 0$$

*Nota al margen:* > Es la situación más común, pudiendo también ser < y ≠; pero cambia el estadístico.

- Calcular el estadístico:

$$d = \frac{\sum_{i=2}^{N}(e_i - e_{i-1})^2}{\sum_{i=1}^{N}(e_i)^2}$$

- Decisión sobre $H_0$:
  - Si: $d < d_{L(\alpha,N,p)}$ se rechaza $H_0$
  - Si: $d > d_{U(\alpha,N,p)}$ no se rechaza $H_0$
  - Si: $d_L \le d \le d_U$ no hay decisión

*Notas al margen (glosario):*
- ■ Límites para la prueba Durbin-Watson
- $e_i \equiv$ residuos ordenados en el tiempo
- $N \equiv$ número total de residuos
- $\alpha \equiv$ nivel de significancia prefijado
- $p \equiv$ número de variables explicativas o términos en el modelo.
- $d_L \equiv$ límite inferior de la tabla Durbin-Watson
- $d_U \equiv$ límite superior de la tabla Durbin-Watson

### 29. Prueba de Durbin-Watson 2/2
Archivo: `6.56.19 PM`

**Ejemplo:** Al comparar cuatro métodos de ensamble en cuanto al tiempo promedio [min] se obtienen los siguientes residuos en el tiempo.

Observaciones con el orden de corrida como superíndice entre paréntesis:

| Tratamientos | A | B | C | D |
|---|---|---|---|---|
| Observaciones | 6 (12) | 7 (3) | 11 (6) | 10 (10) |
| | 8 (8) | 9 (1) | 16 (5) | 12 (15) |
| | 7 (7) | 10 (4) | 11 (14) | 11 (13) |
| | 8 (9) | 8 (2) | 13 (16) | 9 (11) |

- Hipótesis a probar:

$$H_0: \rho = 0$$
$$H_A: \rho > 0$$

*Nota al margen:* Residuos ordenados en el tiempo:

| $X_1$ | $X_2$ | $X_3$ | $X_4$ | $X_5$ | $X_6$ | $X_7$ | $X_8$ | $X_9$ | $X_{10}$ | $X_{11}$ | $X_{12}$ | $X_{13}$ | $X_{14}$ | $X_{15}$ | $X_{16}$ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0.5 | -0.5 | -1.5 | 1.5 | 3.25 | -1.75 | -0.25 | 0.75 | 0.75 | -0.5 | -1.5 | -1.25 | 0.5 | -1.75 | 1.5 | 0.25 |

$$d = \frac{\sum_{i=2}^{N}(e_i - e_{i-1})^2}{\sum_{i=1}^{N} e_i^{\,2}} = \frac{65.1875}{29.5} = 2.20$$

$$d_{L(0.05,16,1)} = 1.10 \qquad d_{U(0.05,16,1)} = 1.37$$

*Nota al margen:* No se rechaza $H_0$ los residuos son independientes.

### 30. Violación del supuesto de normalidad
Archivo: `6.56.19 PM (1)`

El ANOVA es robusto o permite desviaciones moderadas al supuesto de normalidad, debido a que algunas variables respuesta siguen otras distribuciones como ser poisson, binomial, gamma, etc. Son poco frecuentes la violación de este supuesto porque es la distribución estadística más común debido a que la normalidad aproximada se presenta naturalmente en muchas situaciones de medición física, biológica y social.

La falta de normalidad se puede solucionar realizando transformaciones de los datos. Sin embargo, la presencia de puntos aberrantes o atípicos puede afectar sensiblemente las conclusiones del experimento, por lo cual es recomendable investigar con detenimiento sus causas.

### 31. Causas que originan valores atípicos
Archivo: `6.56.19 PM (2)`

El valor atípico es un valor inusualmente grande o pequeño y existen varias causas que los originan:
- Error de entrada de datos: Corrija el error y vuelva a analizar los datos.
- Problema del proceso: Investigue el proceso para determinar la causa del valor atípico.
- Factor faltante: Determine si no consideró un factor que tiene influencia sobre el proceso.
- Probabilidad aleatoria: Investigue el proceso y el valor atípico para determinar si éste ocurrió por casualidad; realice el análisis con y sin el valor atípico para ver su impacto sobre los resultados.

### 32. Violación del supuesto de homocedasticidad 1/2
Archivo: `6.56.20 PM`

Si se observa evidencia contundente de heterocedasticidad, se debe analizar cómo afectan las conclusiones alcanzadas con el ANOVA y las pruebas de rangos múltiples:
- Si el mejor tratamiento es el que tiene menor dispersión, se debe mantener dicho tratamiento como la elección correcta.
- Si el mejor tratamiento es el que tiene la varianza más grande, no es recomendable mantenerlo como la elección correcta, sin transformar previamente los datos u observaciones de manera que se disminuyan las diferencias en la dispersión y se pueda comprender con mayor claridad lo que aconteció en el experimento.

### 33. Violación del supuesto de homocedasticidad 2/2
Archivo: `6.56.20 PM (2)`

Indistintamente cual sea el caso, siempre se debe investigar por qué no sea cumplido el supuesto de varianza constante. Una razón frecuente es que algunas variables tienen una dispersión directamente proporcional a su magnitud, de tal forma que si sus valores son pequeños, éstos tienden a ser más homogéneos en comparación con la variabilidad que tienen entre sí los valores grandes.

Algunos autores especifican que la desigualdad de la varianza afecta ligeramente las inferencias del ANOVA si el modelo contiene sólo factores fijos y tiene tamaños de muestras iguales o casi iguales. Sin embargo, afecta sustancialmente los modelos del ANOVA con efectos aleatorios y/o tamaños de muestras desiguales.

### 34. Transformación de datos
Archivo: `6.56.20 PM (3)`

Para corregir o minimizar los problemas de falta de normalidad y de heterocedasticidad, se realiza nuevamente el análisis pero esta vez sobre la respuesta transformada a una escala en la que los supuestos se cumplan.

Diagrama: óvalo central "Transformaciones posibles" al que apuntan cinco recuadros de colores:
- $Y' = \sqrt{Y}$
- $Y' = \ln(Y)$ o $Y' = \log_{10}(Y)$
- $Y' = Y^{-1/2}$
- $Y' = \operatorname{sen}^{-1}\left(\sqrt{Y}\right)$
- $Y' = Y^{-1}$

*Nota al margen:* Las transformaciones no eliminan las causas de incumplimiento de los supuestos, sino que permiten analizar mejor su efecto.

### 35. Violación del supuesto de independencia
Archivo: `6.56.21 PM`

La presencia de correlación (autocorrelación) se observa en experimentos donde cada medición tiene alguna contaminación de la medición inmediata anterior, lo cual evidencia deficiencias en la planeación y ejecución del experimento; asimismo, puede ser un indicador de que no se aplicó de forma correcta el principio de aleatorización, o de que conforme se fueron realizando las pruebas experimentales aparecieron factores que afectaron la respuesta observada.

En caso de tener problemas con este supuesto, las conclusiones que se obtienen del análisis son endebles y por ello es mejor revisar lo hecho y tratar de investigar el por qué no se cumplió el supuesto de independencia, de tal forma que pueda ser reconsiderada la situación.

*Nota al margen:* Las transformaciones a los datos podrían causar la aparición de autocorrelación en el modelo transformado, incluso cuando el modelo original no presentaba problemas de autocorrelación.

### 36. Comparaciones o pruebas de rango múltiples
Archivo: `6.55.58 PM`

Cuando se rechaza $H_0$ con la prueba de ANOVA, se confirma que existe diferencia en las medias de los tratamientos, pero no sabemos cuáles tratamientos son diferentes. Para averiguarlo:

Diagrama de árbol:

| Grupo | Métodos | Nota al margen |
|---|---|---|
| **Métodos de contraste** | Contraste; Contraste Ortogonal; Método de Scheffé | Comparación de medias entre alguno o algunos tratamientos específicos (foco de interés). |
| **Comparación de pares** | Prueba de Tukey; Método de Fisher (LSD); Método de Duncan; Método de Newman-Keuls; Método de Dunnet | Comparación entre todas las medias, se hace por pares, uno a la vez. |

Llaves a la derecha del grupo "Comparación de pares": Tukey / Fisher (LSD) / Duncan → *Son los más utilizados*; Dunnet → *Útil para comparación contra un patrón*.

### 37. Método de Fisher o LSD 1/3
Archivo: `6.55.59 PM`

**Diferencia mínima significativa – LSD:** es la diferencia mínima que debe haber entre dos medias muestrales, para considerar que dos tratamientos son diferentes.

- Hipótesis a probar:

$$H_0: \mu_i = \mu_j$$
$$H_A: \mu_i \neq \mu_j$$

- Calcular: $LSD = t_{\alpha/2,\,l}\sqrt{\dfrac{2MS_E}{n}}$
- Verificar la igualdad de los $\dfrac{a(a-1)}{2}$ posibles pares de medias, sin orden preestablecido.
- Se rechaza $H_0$ si: $\lvert\bar{Y}_{i.} - \bar{Y}_{j.}\rvert > LSD$

*Notas al margen (glosario):*
- ■ Tabla de Distribución T de Student
- $\alpha \equiv$ nivel de significancia prefijado
- $l \equiv$ grados de libertad del error
- $MS_E \equiv$ cuadrado medio del error
- $n \equiv$ número de observaciones del tratamiento. Cuando el número de observaciones de los tratamientos no es igual: $LSD = t_{\alpha/2,\,l}\sqrt{MS_E\left(\dfrac{1}{n_i} + \dfrac{1}{n_j}\right)}$
- $a \equiv$ número de tratamientos
- *Tiene potencia importante, porque declara significativas las más pequeñas diferencias.*

### 38. Método de Fisher o LSD 2/3
Archivos: `6.55.59 PM (1)` y `6.55.59 PM (2)` (misma diapositiva, dos fotos)

**Ejemplo:** Al comparar cuatro métodos de ensamble en cuanto al tiempo promedio [min] que requiere cada uno de ellos, se rechazó la $H_0$.

| Tratamientos | A | B | C | D |
|---|---|---|---|---|
| Observaciones | 6 | 7 | 11 | 10 |
| | 8 | 9 | 16 | 12 |
| | 7 | 10 | 11 | 11 |
| | 8 | 8 | 13 | 9 |
| $\bar{Y}_{i.}$ | 7.25 | 8.50 | 12.75 | 10.50 |

$MS_E = 2.46$, $\ l = N - a\ $ y $\ \alpha = 0.05$

$$LSD = t_{\alpha/2,\,l}\sqrt{\frac{2MS_E}{n}}$$
$$LSD = t_{0.025,\,12}\sqrt{2.46\left(\frac{2}{4}\right)} = 3.27$$

| Diferencia | Comparación | Decisión |
|---|---|---|
| $\mu_A - \mu_B$ | 1.25 < 3.27 | No significativa |
| $\mu_A - \mu_C$ | 5.50 > 3.27 | Significativa |
| $\mu_A - \mu_D$ | 3.25 < 3.27 | No Significativa |
| $\mu_B - \mu_C$ | 4.25 > 3.27 | Significativa |
| $\mu_B - \mu_D$ | 2.00 < 3.27 | No significativa |
| $\mu_C - \mu_D$ | 2.25 < 3.27 | No significativa |

*Nota de transcripción:* el valor $LSD = 3.27$ es el que muestra la diapositiva. Recalculando con $t_{0.025,12} = 2.179$ da $2.179\sqrt{1.23} \approx 2.42$, con lo que $\mu_A - \mu_D$ (3.25) sí sería significativa, como ocurre en el ejemplo de Dunnet. Conviene verificarlo antes de reutilizar el ejemplo.

(Falta la foto de Método de Fisher o LSD 3/3.)

### 39. Método de Tukey 1/2
Archivos: `6.56.00 PM` y `6.56.00 PM (1)` (misma diapositiva, dos fotos; en la primera la mano de la profesora tapa parte del texto, la segunda se lee completa)

- Hipótesis a probar:

$$H_0: \mu_i = \mu_j$$
$$H_A: \mu_i \neq \mu_j$$

- Calcular: $T_\alpha = q_\alpha(a, l)\sqrt{\dfrac{MS_E}{n}}$
- Verificar la igualdad de los $\dfrac{a(a-1)}{2}$ posibles pares de medias, sin orden preestablecido.
- Se rechaza $H_0$ si: $\lvert\bar{Y}_{i.} - \bar{Y}_{j.}\rvert > T_\alpha$

*Notas al margen (glosario):*
- ■ Tabla de rango estudentizado
- $\alpha \equiv$ nivel de significancia prefijado
- $l \equiv$ grados de libertad del error
- $a \equiv$ número de tratamientos
- $MS_E \equiv$ cuadrado medio del error
- $n \equiv$ número de observaciones del tratamiento. Cuando el número de observaciones de los tratamientos no es igual: $T_\alpha = \dfrac{q_\alpha(a,l)}{\sqrt{2}}\sqrt{MS_E\left(\dfrac{1}{n_i} + \dfrac{1}{n_j}\right)}$
- *Es un método conservador para comparar pares de medias de tratamientos.*

(Falta la foto de Método de Tukey 2/2.)

### 40. Método de Duncan 1/3
Archivo: `6.56.01 PM`

- Hipótesis a probar:

$$H_0: \mu_i = \mu_j$$
$$H_A: \mu_i \neq \mu_j$$

- Calcular: $R_p = r_\alpha(p, l)\sqrt{\dfrac{MS_E}{n}}$
- Verificar la igualdad de los $\dfrac{a(a-1)}{2}$ posibles pares de medias, siguiendo un orden preestablecido.
- Se rechaza $H_0$ si: $\lvert\bar{Y}_{i.} - \bar{Y}_{j.}\rvert > R_p$

*Notas al margen (glosario):*
- ■ Tabla de rangos significantes de Duncan
- $p = 2, 3, \ldots, a$
- $\alpha \equiv$ nivel de significancia prefijado
- $l \equiv$ grados de libertad del error
- $MS_E \equiv$ cuadrado medio del error
- $n \equiv$ número de observaciones del tratamiento. Cuando el número de observaciones de los tratamientos no es igual: $n = \dfrac{a}{\sum_{i=1}^{a}\frac{1}{n_i}}$
- $a \equiv$ número de tratamientos
- *Es un método conservador para comparar pares de medias de tratamientos, cuyo desempeño es similar al de las pruebas LSD.*

### 41. Método de Duncan 2/3
Archivo: `6.56.02 PM`

Orden prestablecido para las diferencias observadas entre las medias muestrales:

Diagrama: cinco recuadros apilados de arriba abajo —
1. $\bar{Y}_{i.}$ más grande
2. $\bar{Y}_{i.}$ segunda más grande
3. $\vdots$
4. $\bar{Y}_{i.}$ segunda más pequeña
5. $\bar{Y}_{i.}$ más pequeña

Flechas por la izquierda desde "más grande" hacia cada una de las demás: la que llega a "más pequeña" está rotulada ① $R_a$; la que llega a "segunda más pequeña", ② $R_{a-1}$; puntos suspensivos para las intermedias. Flechas por la derecha desde "segunda más grande": la que llega a "más pequeña" está rotulada ① $R_{a-1}$; la que llega a "segunda más pequeña", ② $R_{a-2}$.

*Notas al margen:*
- Primero se compara la diferencia entre la media más grande y la más pequeña con el rango $R_a$. Luego, la diferencia entre la media más grande y la segunda más pequeña se compara con el rango $R_{a-1}$. Estas comparaciones continúan hasta que la media mayor se haya comparado con todas las demás.
- Enseguida, se compara la diferencia entre la segunda media más grande y la media más pequeña con el rango $R_{a-1}$ y así sucesivamente.

(Falta la foto de Método de Duncan 3/3.)

### 42. Método de Dunnet 1/2
Archivo: `6.56.03 PM`

En ocasiones uno de los $a$ tratamientos a comparar es el tratamiento de control y el objetivo es comparar los $a - 1$ tratamientos restantes con dicho control. El tratamiento control se refiere a un tratamiento estándar o a la ausencia de tratamiento.

- Hipótesis a probar:

$$H_0: \mu_i = \mu_a$$
$$H_A: \mu_i \neq \mu_a$$

  Con $i = 1, 2, \ldots, a - 1$, donde $a$ es el tratamiento de control.
- Calcular: $D_\alpha = D_\alpha(a-1,\,l)\sqrt{\dfrac{2MS_E}{n}}$
- Probar las $a - 1$ hipótesis.
- Se rechaza $H_0$ si: $\lvert\bar{Y}_{i.} - \bar{Y}_{a.}\rvert > D_\alpha$

*Notas al margen (glosario):*
- ■ Tabla de Dunnet
- $\alpha \equiv$ nivel de significancia prefijado
- $l \equiv$ grados de libertad del error
- $MS_E \equiv$ cuadrado medio del error
- $n \equiv$ número de observaciones del tratamiento. Cuando el número de observaciones de los tratamientos no es igual: $D_\alpha = D_\alpha(a-1,\,l)\sqrt{MS_E\left(\dfrac{1}{n_i} + \dfrac{1}{n_a}\right)}$
- *Útil para la comparación de tratamientos con un control.*

### 43. Método de Dunnet 2/2
Archivo: `6.56.03 PM (1)`

**Ejemplo:** Al comparar cuatro métodos de ensamble en cuanto al tiempo promedio [min] que requiere cada uno de ellos, se rechazó la $H_0$.

(Misma tabla de datos; la columna A está resaltada como control.)

| Tratamientos | A | B | C | D |
|---|---|---|---|---|
| Observaciones | 6 | 7 | 11 | 10 |
| | 8 | 9 | 16 | 12 |
| | 7 | 10 | 11 | 11 |
| | 8 | 8 | 13 | 9 |
| $\bar{Y}_{i.}$ | 7.25 | 8.50 | 12.75 | 10.50 |

*Nota al margen:* $A \equiv$ Tratamiento de control

$MS_E = 2.46$, $\ l = N - a\ $ y $\ \alpha = 0.05$

$$D_\alpha = D_\alpha(a-1,\,l)\sqrt{\frac{2MS_E}{n}}$$
$$D_\alpha = D_{0.05}(3, 12)\sqrt{2.46\left(\frac{2}{4}\right)} = 2.97$$

| Diferencia | Comparación | Decisión |
|---|---|---|
| $\mu_B - \mu_A$ | 1.25 < 2.97 | No significativa |
| $\mu_C - \mu_A$ | 5.50 > 2.97 | Significativa |
| $\mu_D - \mu_A$ | 3.25 > 2.97 | Significativa |

### 44. Uso de software con Minitab®
Archivo: `6.56.21 PM (1)`

Diagrama en escalera (cuatro peldaños ascendentes, cada uno con un color):
1. Introducción de datos
2. Análisis de datos y verificación de supuestos
3. Comparación de medias
4. Verificación de supuestos analíticamente

### 45. ¿Cómo introducir los datos en Minitab®?
Archivo: `6.56.21 PM (2)`

Dos recuadros lado a lado:

| Opción de menú | Aclaración (nota al margen) | Formato de los datos |
|---|---|---|
| **Un solo factor** | (Método convencional) | **Datos apilados en una columna** |
| **Un solo factor desapilado** | (Método disponible sólo para diseños de un solo factor) | **Cada nivel en una columna separada** |

(No hay fotos de las capturas de pantalla de Minitab que siguen a esta diapositiva: no se registran menús, cuadros de diálogo ni salidas.)

### 46. Medidas de posición (no centrada) — Criterios para determinar los cuartiles **(posición dudosa; pertenece a otra presentación)**
Archivo: `6.56.02 PM (1)`

Diapositiva de otro mazo: el pie dice *Alexander Correa Espinal & Faviana Gutiérrez Rôa – Gerencia del Servicio – Universidad Nacional de Colombia* y la barra lateral es de iconos morados, no la de "Diseño de Experimentos". En el orden de archivos aparece entre Duncan 2/3 y Dunnet 1/2 (probable digresión de la profesora sobre cómo el software calcula cuartiles).

**Criterios para determinar los cuartiles**

- Minitab®: Utiliza las expresiones:

$$Q_1 = 0.25(n+1) \qquad Q_3 = 0.75(n+1)$$

- Microsoft Office Excel®: Utiliza las expresiones

$$Q_1 = 0.25(n-1)+1 \qquad Q_3 = 0.75(n-1)+1$$

| Método | Datos: 2, 4, 6, 8 — $Q_1$ | Datos: 2, 4, 6, 8 — $Q_3$ | Datos: 2, 4, 6, 8, 10 — $Q_1$ | Datos: 2, 4, 6, 8, 10 — $Q_3$ |
|---|---|---|---|---|
| Tukey | 3 | 7 | 4 | 8 |
| Moore y McCabe | 3 | 7 | 3 | 9 |
| Minitab® | 2.5 | 7.5 | 3 | 9 |
| Microsoft Office Excel® | 3.5 | 6.5 | 4 | 8 |

Gráfica: caricatura de un hombre confundido con humo saliendo de la cabeza.

---

## Tabla de correspondencia archivo → diapositiva

| Archivo (hora) | Diapositiva |
|---|---|
| 6.55.56 PM | 11. Tabla ANOVA (descripción) |
| 6.55.56 PM (1) | 11. Tabla ANOVA (descripción) — duplicado |
| 6.55.56 PM (2) | 13. Procedimientos de Prueba de Hipótesis |
| 6.55.56 PM (3) | 1. Tiempo de coagulación de la sangre en pollos |
| 6.55.58 PM | 36. Comparaciones o pruebas de rango múltiples |
| 6.55.59 PM | 37. Método de Fisher o LSD 1/3 |
| 6.55.59 PM (1) | 38. Método de Fisher o LSD 2/3 |
| 6.55.59 PM (2) | 38. Método de Fisher o LSD 2/3 — duplicado |
| 6.56.00 PM | 39. Método de Tukey 1/2 (parcialmente tapada) |
| 6.56.00 PM (1) | 39. Método de Tukey 1/2 — duplicado, completa |
| 6.56.01 PM | 40. Método de Duncan 1/3 |
| 6.56.02 PM | 41. Método de Duncan 2/3 |
| 6.56.02 PM (1) | 46. Medidas de posición (cuartiles) |
| 6.56.03 PM | 42. Método de Dunnet 1/2 |
| 6.56.03 PM (1) | 43. Método de Dunnet 2/2 |
| 6.56.04 PM | 2. ¿Cuál es el modelo matemático del diseño? |
| 6.56.04 PM (1) | 3. Efectos fijos y efectos aleatorios |
| 6.56.05 PM | 5. ¿Cuál es la hipótesis del diseño? |
| 6.56.05 PM (1) | 6. ¿Cómo debo recolectar los datos? |
| 6.56.06 PM | 7. ¿Cuántos datos debo recolectar? 1/3 |
| 6.56.06 PM (1) | 8. ¿Cuántos datos debo recolectar? 2/3 |
| 6.56.07 PM | 9. ¿Cuántos datos debo recolectar? 3/3 |
| 6.56.07 PM (1) | 10. ¿Cómo debo analizar los datos recolectados? |
| 6.56.08 PM | 12. Tabla ANOVA (fórmulas) |
| 6.56.14 PM | 14. ¿Qué debemos verificar sobre el modelo? |
| 6.56.15 PM | 15. Supuestos sobre los errores del modelo |
| 6.56.15 PM (1) | 16. ¿Cómo comprobar los supuestos del modelo? |
| 6.56.15 PM (2) | 17. Probabilidad normal 1/3 |
| 6.56.15 PM (3) | 18. Histograma de residuos |
| 6.56.16 PM | 19. Predichos vs residuos 1/3 |
| 6.56.16 PM (1) | 20. Residuos vs tiempo 1/3 |
| 6.56.16 PM (2) | 21. Pruebas analíticas de normalidad |
| 6.56.17 PM | 22. Prueba Shapiro-Wilks 1/3 |
| 6.56.17 PM (1) | 23. Prueba Shapiro-Wilks 2/3 |
| 6.56.17 PM (2) | 24. Prueba Shapiro-Wilks 3/3 |
| 6.56.18 PM | 25. Pruebas analíticas de varianza constante |
| 6.56.18 PM (1) | 26. Prueba de Bartlett 1/2 |
| 6.56.18 PM (2) | 27. Prueba de Bartlett 2/2 |
| 6.56.18 PM (3) | 28. Prueba de Durbin-Watson 1/2 |
| 6.56.19 PM | 29. Prueba de Durbin-Watson 2/2 |
| 6.56.19 PM (1) | 30. Violación del supuesto de normalidad |
| 6.56.19 PM (2) | 31. Causas que originan valores atípicos |
| 6.56.20 PM | 32. Violación del supuesto de homocedasticidad 1/2 |
| 6.56.20 PM (1) | 4. Diseño balanceado |
| 6.56.20 PM (2) | 33. Violación del supuesto de homocedasticidad 2/2 |
| 6.56.20 PM (3) | 34. Transformación de datos |
| 6.56.21 PM | 35. Violación del supuesto de independencia |
| 6.56.21 PM (1) | 44. Uso de software con Minitab® |
| 6.56.21 PM (2) | 45. ¿Cómo introducir los datos en Minitab®? |

---

## Estructura didáctica de la profesora

Lo que sigue se deduce solo de las 46 diapositivas fotografiadas; falta la apertura del mazo (portada, definición / cuándo usar el diseño) y casi todo el bloque de software, así que esos dos bloques no se pueden caracterizar.

### Secuencia de bloques y número de diapositivas

| # | Bloque | Diapositivas (registro) | Cantidad |
|---|---|---|---|
| 1 | Ejemplo motivador con datos reales y pregunta de investigación (pollos) | 1 | 1 |
| 2 | Modelo estadístico: ecuación con cada término rotulado y gráfica de $\mu$, $\mu_i$, $\tau_i$; efectos fijos vs aleatorios; diseño balanceado | 2–4 | 3 |
| 3 | Hipótesis del diseño (en medias y, equivalente, en efectos) | 5 | 1 |
| 4 | Protocolo experimental: cómo recolectar (aleatorización, protocolo, tabla de datos genérica) y cuántos datos (criterios prácticos, fórmula, ejemplo numérico) | 6–9 | 4 |
| 5 | Ruta de análisis en 6 pasos numerados | 10 | 1 |
| 6 | ANOVA: tabla en palabras y luego la misma tabla con fórmulas (+ tabla de repaso de pruebas de hipótesis) | 11–13 | 3 |
| 7 | Supuestos: qué verificar y residuos, lista de supuestos, mapa de pruebas gráficas/analíticas | 14–16 | 3 |
| 8 | Supuestos — pruebas gráficas (probabilidad normal, histograma, predichos vs residuos, residuos vs tiempo) | 17–20 (+6 no fotografiadas) | 4 (≈10 en el mazo) |
| 9 | Supuestos — pruebas analíticas (Shapiro-Wilks, Bartlett, Durbin-Watson), cada una con procedimiento y ejemplo calculado a mano | 21–29 | 9 |
| 10 | Qué hacer si se viola un supuesto (normalidad, atípicos, homocedasticidad, transformaciones, independencia) | 30–35 | 6 |
| 11 | Comparaciones múltiples: mapa de métodos y luego LSD, Tukey, Duncan, Dunnet, cada uno con procedimiento y ejemplo | 36–43 (+3 no fotografiadas) | 8 (≈11 en el mazo) |
| 12 | Software: escalera de 4 pasos en Minitab e introducción de datos | 44–45 (capturas no fotografiadas) | 2 |
| — | Digresión de otro mazo: criterios de cuartiles en Minitab vs Excel | 46 | 1 |

El peso está en supuestos (bloques 7–10: 22 de 46 diapositivas) y comparaciones múltiples (8); el modelo, las hipótesis y el ANOVA ocupan apenas 7 diapositivas.

Nota sobre el orden: la lista de la diapositiva 10 pone "verificar supuestos" (paso 4) antes de "comparación de medias" (paso 5), y así se ordenó este registro; en los nombres de archivo, en cambio, el bloque de comparaciones aparece antes que el del modelo. No se puede confirmar con las fotos cuál fue el orden real de proyección.

### Títulos y preguntas a la clase

- Los títulos de las diapositivas conceptuales son preguntas en primera persona que guían el proceso: *¿Cuál es el modelo matemático del diseño?*, *¿Cuál es la hipótesis del diseño?*, *¿Cómo debo recolectar los datos?*, *¿Cuántos datos debo recolectar?*, *¿Cómo debo analizar los datos recolectados?*, *¿Qué debemos verificar sobre el modelo?*, *¿Cómo comprobar los supuestos del modelo?*, *¿Cómo introducir los datos en Minitab®?*
- Los títulos de métodos son el nombre del método con contador "k/n" cuando ocupa varias diapositivas (*Método de Fisher o LSD 1/3*, *Prueba de Bartlett 2/2*).
- El histograma de residuos se explica con preguntas diagnósticas (*¿Parecen estar distribuidos normalmente los residuos?*, *¿Están sesgados…?*).
- El ejemplo motivador cierra con la pregunta de investigación (*¿Hay alguna evidencia que indique una diferencia real entre los tiempos medios…?*).

### Plantilla fija para cada prueba o método

Cada método (LSD, Tukey, Duncan, Dunnet, Shapiro-Wilks, Bartlett, Durbin-Watson) usa la misma plantilla en dos o tres diapositivas:

1. **Diapositiva 1/n — procedimiento.** A la izquierda, viñetas en este orden: frase de para qué sirve (opcional) → "Hipótesis a probar:" con $H_0$ y $H_A$ → "Calcular:" / "Calcular el estadístico:" con la fórmula → paso operativo ("Verificar la igualdad de los $a(a-1)/2$ posibles pares…", "Ordenar los residuos…") → "Se rechaza $H_0$ si: …". A la derecha, separado por una línea vertical punteada, un glosario en letra manuscrita: primero la tabla estadística que se necesita (■ Tabla de…), luego cada símbolo con "≡", la variante de la fórmula para tamaños desiguales y una frase de valoración del método (potente, conservador, útil para control).
2. **Diapositiva 2/n — ejemplo.** Empieza con "**Ejemplo:**" y el enunciado; tabla de datos con encabezado verde; parámetros ($MS_E$, $l$, $\alpha$); fórmula simbólica y debajo la misma con números sustituidos y el resultado; tabla o lista de decisiones.
3. **Conclusión** en una frase corta en letra manuscrita junto al resultado.

### Cómo redacta hipótesis y conclusiones

- Hipótesis siempre en par $H_0$ / $H_A$ (usa $H_A$, no $H_1$), simbólicas: $H_0: \mu_1 = \mu_2 = \ldots = \mu_a = \mu$ contra $H_A: \mu_i \neq \mu_j$ para algún $i \neq j$; da además la forma equivalente en efectos ($\tau_i = 0$) y una lectura en palabras al margen. Para normalidad las escribe en palabras (*Los datos se distribuyen normal / no se distribuyen normal*).
- Criterio de rechazo explícito con la fórmula: "Se rechaza $H_0$ si: estadístico > valor crítico de tabla". Trabaja con valores críticos de tablas en los ejemplos a mano; el valor-p se reserva para el software (paso 2 de la ruta de análisis) y en la tabla ANOVA aparece como $P(F_t > F_O)$.
- Conclusiones telegráficas, con decisión + interpretación: *Se acepta $H_0$ los residuos son normales*; *Se acepta $H_0$ los residuos son homocedásticos*; *No se rechaza $H_0$ los residuos son independientes*. En comparaciones: "diferencia < o > valor crítico → *Significativa* / *No significativa*" para cada par.
- La ruta de análisis exige cerrar informando "la conclusión en términos del problema establecido por el investigador".

### Notación

- Modelo: $Y_{ij} = \mu + \tau_i + \varepsilon_{ij}$, $i = 1 \cdots a$, $j = 1 \cdots n$.
- $a$ = número de tratamientos; $n$ = réplicas por tratamiento ($n_i$ si no es balanceado); $N$ = total de observaciones ($N = a \times n$); $T_i$ = tratamiento $i$.
- Notación de puntos: $y_{i.}$, $y_{..}$, $\bar{Y}_{i.}$.
- ANOVA con siglas en inglés: SV, SS, DF, MS, $F_O$, P-Value; $SS_{TRAT}$, $SS_E$, $SS_T$, $MS_{TRAT}$, $MS_E$.
- $l$ = grados de libertad del error; $\alpha$ = nivel de significancia prefijado (siempre 0.05 en los ejemplos).
- Residuos $e_{ij} = Y_{ij} - \hat{Y}_{ij} = Y_{ij} - \bar{Y}_{i.}$; varianzas $S_i^2$, $S_p^2$, $\sigma^2$, $\sigma_\tau^2$.
- Valores críticos: $t_{\alpha/2,l}$, $q_\alpha(a,l)$, $r_\alpha(p,l)$, $D_\alpha(a-1,l)$, $\chi^2_{(\alpha,a-1)}$, $W_{1-\alpha,N}$, $d_{L(\alpha,N,p)}$, $d_{U(\alpha,N,p)}$.
- Tratamientos de los ejemplos rotulados A, B, C, D; unidades entre corchetes ([min]).

### Cómo presenta los ejemplos

- Un **ejemplo corrido único** — "cuatro métodos de ensamble, tiempo promedio [min]", $a = 4$, $n = 4$, $MS_E = 2.46$ — se reutiliza en tamaño de muestra, LSD, Dunnet, Shapiro-Wilks, Bartlett y Durbin-Watson, repitiendo la tabla de datos en cada diapositiva y añadiendo la fila que se necesita ($\bar{Y}_{i.}$, $S_i^2$, orden de corrida).
- Un **ejemplo motivador distinto** (coagulación en pollos, $a = 4$, $n = 6$) con el orden aleatorio de ejecución como superíndice entre paréntesis.
- Los cálculos se muestran a mano y completos: fórmula general, sustitución numérica, resultado, comparación con el valor de tabla y decisión.

### Uso del software

- Minitab® es el software de referencia. Se introduce al final con una escalera de cuatro pasos: introducción de datos → análisis de datos y verificación de supuestos → comparación de medias → verificación de supuestos analíticamente.
- Para introducir datos distingue las dos opciones del menú de ANOVA de un factor: "Un solo factor" (datos apilados en una columna, método convencional) y "Un solo factor desapilado" (cada nivel en una columna separada, solo para un factor).
- Compara criterios de Minitab con Excel (cuartiles), lo que sugiere que acepta ambos pero advierte de las diferencias de cálculo.
- Las capturas de menús, cuadros de diálogo y salidas no fueron fotografiadas, así que no se puede describir cómo las presenta.

### Rasgos de estilo

- Fondo azul claro degradado; título en negrita gris oscuro arriba a la izquierda; pie con autores y universidad; marca lateral del curso en verde.
- Dos tipografías con función distinta: sans-serif para el contenido formal y una letra tipo manuscrita cursiva para comentarios, glosarios de símbolos y conclusiones.
- Tablas con encabezado verde y borde verde; todos los datos de los ejemplos van en tabla.
- Mapas conceptuales / árboles con cajas de colores para clasificar opciones (pruebas gráficas vs analíticas, métodos de contraste vs comparación de pares, transformaciones posibles, lista de supuestos).
- Densidad alta de texto: párrafos completos justificados de 3 a 8 líneas en las diapositivas conceptuales; las diapositivas de método son más esquemáticas (viñetas + fórmulas + glosario).
- Términos clave en negrita al inicio de la definición (**Modelo de efectos fijos:**, **Prueba de Bartlett:**, **Diferencia mínima significativa – LSD:**).
- Pocas imágenes decorativas (pollitos, engranajes, caricatura); las gráficas son esquemas propios, no salidas de software.
- Tono prescriptivo e impersonal ("se debe", "se sugiere", "Utilícela cuando…", "Corrija el error…").
