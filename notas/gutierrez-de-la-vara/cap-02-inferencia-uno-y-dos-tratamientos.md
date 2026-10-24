# Capítulo 2 — Elementos de inferencia estadística: experimentos con uno y dos tratamientos

> Gutiérrez Pulido y De la Vara Salazar, *Análisis y diseño de experimentos*, 2.ª ed., págs. 18–59

Ficha técnica de consulta, con palabras propias. El capítulo presenta la inferencia estadística
(estimación y prueba de hipótesis) para **uno y dos tratamientos**, que es la base del diseño
de comparación simple. Es el complemento del capítulo 2 de Montgomery: trata lo mismo, pero
añade los **tres criterios equivalentes de rechazo**, el **tamaño de muestra para un error
máximo de estimación**, las **proporciones** y una discusión más explícita sobre la
significancia práctica.

Objetivos de aprendizaje declarados (pág. 18): identificar los elementos de la inferencia
estadística y su importancia en los diseños experimentales; explicar el papel de las
distribuciones de probabilidad, la estimación puntual y por intervalo; describir las pruebas
para la media y la varianza y los conceptos básicos de prueba de hipótesis; identificar las
pruebas para la igualdad de varianzas; distinguir las pruebas para comparar medias con
muestras independientes y con muestras pareadas.

Conceptos clave del capítulo: error tipo I, error tipo II, estadístico, estadístico de prueba,
estimador puntual, grados de libertad, hipótesis estadística, inferencia estadística, intervalo
de confianza, muestras pareadas, orden completamente al azar, potencia de la prueba, región de
aceptación, región de rechazo, significancia observada, significancia predefinida.

---

## Población y muestra, parámetros y estadísticos (págs. 20–21)

- **Población o universo**: colección o totalidad de posibles individuos, especímenes, objetos
  o medidas de interés. Puede ser **finita** (se pueden medir todos los individuos y conocer
  "exactamente" sus parámetros) o **infinita** (grande; medir todo es imposible o incosteable).
- **Parámetros**: características que, mediante su valor numérico, describen a un conjunto de
  elementos. Ejemplos: la proporción $p$ de defectuosos, la media $\mu$ de una variable.
- En la industria las poblaciones son materiales, productos, partes o procesos. Conviene
  imaginar un proceso como población infinita: el flujo no se detiene, no existe el último
  artículo mientras la empresa opere. Los procesos se estudian con muestras tomadas en algún
  punto del proceso.
- **Muestra representativa**: parte de la población, seleccionada adecuadamente, que conserva
  los aspectos clave de la población. Se logra con un **muestreo aleatorio**: todos los
  elementos tienen la misma oportunidad de ser incluidos. Métodos: simple, estratificado,
  sistemático y por conglomerados.
- **Inferencia estadística**: afirmaciones válidas sobre la población o proceso con base en la
  información de la muestra, para apoyar la toma de decisiones. Se divide en **estimación** y
  **prueba de hipótesis**.
- **Estadístico**: cualquier función de los datos muestrales que no contiene parámetros
  desconocidos (ejemplo: $\bar X$ para hacer afirmaciones sobre $\mu$). Todo estadístico es una
  **variable aleatoria**: su valor depende de los elementos seleccionados y varía de una muestra
  a otra. Por eso hay que conocer su distribución de probabilidad (figura 2.1: parámetros
  siempre desconocidos, estadísticos conocidos, inferencia de la muestra a la población).

## Distribuciones de probabilidad e inferencia (págs. 21–23)

- La **distribución de probabilidad** de $X$ relaciona los valores posibles de $X$ con la
  probabilidad de cada uno (tabla o fórmula). La distribución de $\bar X$ dice qué valores se
  espera que tome; así lo aleatorio "no es un capricho": al observar una realización se pueden
  corroborar o rechazar supuestos (prueba de hipótesis) o hacer estimaciones.
- Las cuatro distribuciones de mayor uso: **normal**, **T de Student**, **ji-cuadrada** y **F**
  (figura 2.2). Normal y T son simétricas y centradas en cero; ji-cuadrada y F son sesgadas y
  solo toman valores positivos. T, ji-cuadrada y F se definen a partir de la normal estándar.
- **Grados de libertad**: parámetros que definen por completo a T, ji-cuadrada y F; se
  determinan con los tamaños muestrales. Con $n = 20$: T con 19 g.l. para la media,
  ji-cuadrada con 19 g.l. para la varianza.
- La T tiende a la normal estándar cuando $n$ crece y es prácticamente la misma para
  $n > 45$; la diferencia es que la T tiene colas más anchas.
- Uso: normal y T para medias; ji-cuadrada para una varianza; F para **comparar varianzas**.
  La F es la distribución de mayor relevancia en diseño de experimentos porque el análisis de
  la variabilidad observada en un experimento se hace comparando varianzas.
- Excel: `DISTR.NORM(x, media, desv_estándar, acum)` con `acum = 1` da $P(X \le x)$ y con
  `acum = 0` da la densidad $f(x)$.

## Estimación puntual y por intervalo (págs. 23–29)

### Estimación puntual

- **Estimador puntual**: estadístico que genera un valor numérico simple para estimar el
  parámetro desconocido. Los recomendados:

| Parámetro | Estimador puntual |
|---|---|
| Media $\mu$ | $\hat\mu = \bar X$ |
| Varianza $\sigma^2$ | $\hat\sigma^2 = S^2$ |
| Proporción $p$ | $\hat p = x/n$ ($x$ = número de defectuosos en $n$) |

- El "gorro" denota un estimador; los estimadores no son únicos (la media se podría estimar
  con la mediana o la moda).

### Estimación por intervalo

- La estimación puntual varía de una muestra a otra; hay que saber qué tan precisa es. La
  variabilidad de un estimador se mide con su **error estándar**; para $\bar X$ se estima con
  $\hat\sigma_{\bar X} = S/\sqrt{n}$.
- **Intervalo de confianza** al $100(1-\alpha)$ % para $\theta$: dos estadísticos $L$ y $U$
  tales que

$$P(L \le \theta \le U) = 1 - \alpha \qquad \text{(2.1)}$$

- Interpretación: si se tomaran 100 muestras independientes y se calculara el intervalo al 95 %
  en cada una, se espera que 95 de los 100 contengan el verdadero valor. En la práctica se
  obtiene un solo intervalo y se dice que tiene una confianza del $100(1-\alpha)$ %.
- La **longitud** del intervalo mide la precisión: crece con la varianza de la población y con
  la confianza exigida; decrece al aumentar $n$.

**Intervalo para una media** (población normal, $\mu$ y $\sigma^2$ desconocidas). Se parte del
estadístico $t = (\bar X - \mu)/(S/\sqrt n) \sim t_{n-1}$; con los valores críticos
$\pm t_{\alpha/2}$ y despejando $\mu$:

$$P\left(\bar X - t_{\alpha/2}\,\frac{S}{\sqrt n} \le \mu \le \bar X + t_{\alpha/2}\,\frac{S}{\sqrt n}\right) = 1 - \alpha \qquad \text{(2.2)}$$

- Para $n \ge 30$ el intervalo es aproximadamente $\bar X \pm 2S/\sqrt n$ (la media más menos
  dos veces su error estándar).

**Ejemplo 2.1 (grosor de discos de plástico, pág. 26).** Especificación $1.20 \pm 0.10$ mm.
Muestreo sistemático de una semana: 25 muestras de tamaño 5, $n = 125$, $\bar X = 1.179$ mm,
$S^2 = 0.00071$. Error estándar $S/\sqrt n = 0.0266/11.18 = 0.0024$. Como $n \ge 45$,
$t_{\alpha/2} \approx z_{\alpha/2} = 1.96$:

$$\bar X \pm t_{\alpha/2}\frac{S}{\sqrt n} = 1.179 \pm 1.96\,(0.0024) = 1.179 \pm 0.00466 \;\Rightarrow\; [1.174,\ 1.184]$$

El valor $0.00466$ es el **error de estimación**: hasta en esa cantidad puede diferir $\bar X$
de $\mu$.

**Tamaño de muestra para un error máximo $E$.** Como $E = t_{\alpha/2,\,n-1}\,S/\sqrt n$,

$$n = \frac{t^2_{\alpha/2,\,n-1}\,S^2}{E^2} \;\approx\; \frac{4S^2}{E^2} \quad (n > 30,\ t_{\alpha/2} \approx 2)$$

Ejemplo: con $E = 0.004$ y $S^2 = 0.00071$, $n = 4(0.00071)/(0.004)^2 = 177.5 \approx 178$.

**Intervalo para la varianza.** Bajo normalidad, $(n-1)S^2/\sigma^2 \sim \chi^2_{n-1}$, luego

$$\frac{(n-1)S^2}{\chi^2_{\alpha/2,\,n-1}} \le \sigma^2 \le \frac{(n-1)S^2}{\chi^2_{1-\alpha/2,\,n-1}} \qquad \text{(2.3)}$$

donde $P(X > \chi^2_{\alpha/2,\,n-1}) = \alpha/2$. El intervalo para $\sigma$ se obtiene
sacando raíz cuadrada a los extremos.

**Ejemplo 2.2 (rendimiento de formato de discos, pág. 27).** $n = 10$: 96.11, 91.06, 93.38,
88.52, 89.57, 92.63, 85.20, 91.41, 89.79, 92.62. $\bar X = 91.03$, $S = 2.99$. Con
$t_{0.025,9} = 2.26$:

$$\left[91.03 - 2.26\frac{2.99}{\sqrt{10}},\ 91.03 + 2.26\frac{2.99}{\sqrt{10}}\right] = [88.89,\ 93.17]$$

Para $\sigma$, con $\chi^2_{0.025,9} = 19.02$ y $\chi^2_{0.975,9} = 2.70$:

$$\left[\sqrt{\frac{9(2.99)^2}{19.02}},\ \sqrt{\frac{9(2.99)^2}{2.70}}\right] = [2.05,\ 5.46]$$

Si el intervalo es demasiado amplio, la única forma de ganar precisión es aumentar $n$.

**Intervalo para una proporción.** Si el número de defectuosos es binomial y $n$ es grande,
$\hat p$ es aproximadamente normal con media $p$ y varianza $p(1-p)/n$:

$$\hat p - Z_{\alpha/2}\sqrt{\frac{\hat p(1-\hat p)}{n}} \le p \le \hat p + Z_{\alpha/2}\sqrt{\frac{\hat p(1-\hat p)}{n}}$$

**Ejemplo 2.3 (pág. 29).** Lote de 2 000 artículos, $n = 100$, $x = 5$: $\hat p = 0.050$;
$0.050 \pm 1.96\sqrt{0.05(0.95)/100} = 0.050 \pm 0.043$, es decir $p$ entre 0.7 % y 9.3 %.
Tamaño de muestra para un error máximo $E$: $n = Z_{\alpha/2}^2\,\hat p(1-\hat p)/E^2$; con
$E = 0.03$, $n = (1.96)^2(0.05)(0.95)/(0.03)^2 \approx 203$. Si no se sabe nada de $p$, se
supone $\hat p = 0.5$ (caso más desfavorable).

**Tabla 2.1. Resumen de fórmulas para intervalos de confianza**

| Parámetro | Límite inferior | Límite superior |
|---|---|---|
| $\mu$ | $\bar X - t_{\alpha/2}\,S/\sqrt n$ | $\bar X + t_{\alpha/2}\,S/\sqrt n$ |
| $\sigma^2$ | $(n-1)S^2/\chi^2_{\alpha/2,\,n-1}$ | $(n-1)S^2/\chi^2_{1-\alpha/2,\,n-1}$ |
| $p$ | $\hat p - z_{\alpha/2}\sqrt{\hat p(1-\hat p)/n}$ | $\hat p + z_{\alpha/2}\sqrt{\hat p(1-\hat p)/n}$ |
| $\mu_1 - \mu_2$ | $(\bar X_1 - \bar X_2) - t_{\alpha/2}\,S_p\sqrt{1/n_1 + 1/n_2}$ | $(\bar X_1 - \bar X_2) + t_{\alpha/2}\,S_p\sqrt{1/n_1 + 1/n_2}$ |
| $\sigma_1^2/\sigma_2^2$ | $\dfrac{S_1^2}{S_2^2}\,F_{1-\alpha/2,\,n_2-1,\,n_1-1}$ | $\dfrac{S_1^2}{S_2^2}\,F_{\alpha/2,\,n_2-1,\,n_1-1}$ |
| $p_1 - p_2$ | $(\hat p_1 - \hat p_2) - z_{\alpha/2}\sqrt{\frac{\hat p_1(1-\hat p_1)}{n_1} + \frac{\hat p_2(1-\hat p_2)}{n_2}}$ | $(\hat p_1 - \hat p_2) + z_{\alpha/2}\sqrt{\frac{\hat p_1(1-\hat p_1)}{n_1} + \frac{\hat p_2(1-\hat p_2)}{n_2}}$ |

con $S_p^2 = [(n_1-1)S_1^2 + (n_2-1)S_2^2]/(n_1+n_2-2)$ y $t_{\alpha/2}$ con $n_1+n_2-2$
grados de libertad en el renglón de $\mu_1 - \mu_2$. Los intervalos de dos parámetros informan
sobre la igualdad estadística de los parámetros de las dos poblaciones.

---

## Conceptos básicos de prueba de hipótesis (págs. 29–34)

Un estudio experimental busca responder preguntas y tomar decisiones; el experimentador tiene
creencias previas que quiere comprobar ("los tres proveedores tienen el mismo nivel de
calidad", "el tiempo de espera es de tres horas en promedio", "si aumentamos el reactivo se
elimina el problema"). Los pasos de cualquier procedimiento: **planteamiento de la hipótesis**,
**estadístico de prueba** y **criterio de rechazo**.

### Planteamiento de una hipótesis estadística

- **Hipótesis estadística**: afirmación sobre los valores de los parámetros de una población o
  proceso, que puede probarse con la información de una muestra representativa.
- Ejemplo: "este proceso produce menos de 8 % de defectuosos":

$$H_0: p = 0.08 \qquad H_A: p < 0.08 \qquad \text{(2.4)}$$

- $H_0$: **hipótesis nula**; se plantea como igualdad porque así se tiene una distribución de
  referencia específica. $H_A$: **hipótesis alternativa**. Estrategia: suponer $H_0$ verdadera y,
  si los datos la rechazan, aceptar $H_A$. La afirmación que se desea probar se acepta como
  cierta **solo si se rechaza** $H_0$.
- Si la afirmación es "este proceso produce 8 % de defectuosos", su falsedad se da tanto con
  menos como con más defectuosos:

$$H_0: p = 0.08 \qquad H_A: p \ne 0.08 \qquad \text{(2.5)}$$

- (2.4) es una alternativa **unilateral** (de un solo lado): solo se rechaza $H_0$ con valores
  de $\hat p$ significativamente menores que 0.08. (2.5) es **bilateral**: la evidencia en contra
  viene de valores pequeños o grandes. La elección depende de la afirmación que se quiera
  probar.
- El valor del parámetro en $H_0$ se elige de modo que **separe dos situaciones que llevan a
  acciones distintas** (0.08 era la proporción del mes anterior; tras un programa de mejora, no
  rechazar $H_0$ significa que el programa no funcionó).

### Estadístico de prueba

- Probar una hipótesis es investigar si lo afirmado por $H_0$ es verdad. Si los resultados la
  contradicen suficientemente, se rechaza; si no la contradicen claramente, no se rechaza: "la
  hipótesis nula es verdadera mientras no se demuestre lo contrario".
- **Estadístico de prueba**: número calculado a partir de los datos y de $H_0$ cuya magnitud
  permite discernir si se rechaza $H_0$. **Región (intervalo) de rechazo**: valores del
  estadístico que llevan a rechazar $H_0$; **región de aceptación**: valores donde no se rechaza.
- Para (2.4) y (2.5):

$$z_0 = \frac{\hat p - 0.08}{\sqrt{0.08(1 - 0.08)/n}} \qquad \text{(2.6)}$$

  que bajo $H_0$ es aproximadamente $N(0,1)$; se requiere $np > 10$ (aquí $n \ge 120$). Con
  $n = 150$ y $x = 20$: $\hat p = 0.13$ y $z_0 = 2.41$.

### Criterio de rechazo

- Si $H_0$ es verdad, el estadístico debería caer en el rango de valores más probables de su
  distribución (región de aceptación); si cae en una cola (región de rechazo) es evidencia de
  que el supuesto bajo el que se construyó es falso (figura 2.3).
- **Pruebas de una y dos colas.** Bilateral: la región de rechazo se reparte por igual entre
  las dos colas ($\alpha/2$ en cada una); se rechaza si $\lvert z_0 \rvert > z_{\alpha/2}$.
  Unilateral: la región de rechazo se concentra en una cola; para (2.4) se rechaza si
  $z_0 < -z_\alpha$.
- Ejemplo: bilateral al 95 %, $z_{\alpha/2} = 1.96$; $z_0 = 2.41 > 1.96$, se rechaza
  $H_0: p = 0.08$. Si hubiera $x = 15$ ($\hat p = 0.10$), $z_0 = 0.90 < 1.96$ y no se rechaza:
  $\hat p = 0.10$ no es evidencia suficiente contra $p = 0.08$.

### El riesgo de una decisión equivocada: errores tipo I y tipo II (pág. 33)

| Error | Definición | Probabilidad |
|---|---|---|
| Tipo I | Rechazar $H_0$ cuando es verdadera | $\alpha$ = significancia dada (predefinida) = probabilidad de la región de rechazo |
| Tipo II | Aceptar $H_0$ cuando es falsa | $\beta$ |
| Potencia | Rechazar $H_0$ cuando es falsa | $1 - \beta$ |

- $\alpha$ lo fija el investigador al planear el estudio; usualmente 0.05 o 0.01 según el riesgo
  admisible. Con $\alpha$ más pequeña se requiere más evidencia para rechazar. Si rechazar $H_0$
  implica una inversión fuerte, usar 0.01; si no, 0.05 basta. Un $\alpha$ menor no es
  necesariamente mejor: con $\alpha \le 0.01$ se truncan muchos cambios que serían positivos.
  $\alpha = 0.05$ significa que de cada 100 rechazos independientes, en promedio 95 son
  correctos.
- $\alpha$ se controla directamente; $\beta$ se controla indirectamente con el **tamaño de la
  muestra** (más datos, menor $\beta$, mayor potencia). Nota al pie: con muestras de cientos la
  potencia es excesiva y se llega a rechazar $H_0$ cuando es verdadera desde el punto de vista
  práctico.
- En la práctica suele ser más delicado el error tipo I (rechazar $H_0$ es objetar algo aceptado
  convencionalmente; no rechazar es seguir como hasta ahora), por lo que es común controlar
  solo $\alpha$. Pero $\beta$ también importa: se recomienda $\beta = 0.10$. Controlar $\beta$
  exige tamaños muestrales grandes o muchas repeticiones; el libro no lo enfatiza, pero da
  recomendaciones del número de repeticiones en cada diseño.

## Prueba para la media (págs. 34–36)

Interesa si $\mu$ es igual, mayor o menor que un valor conocido $\mu_0$ (por ejemplo, el
rendimiento de la semana anterior). Como en la mayoría de los problemas es irreal suponer
$\sigma^2$ conocida, el libro describe solo el caso de **varianza desconocida**.

$X \sim N(\mu, \sigma^2)$, ambas desconocidas:

$$H_0: \mu = \mu_0 \qquad H_A: \mu \ne \mu_0 \qquad \text{(2.7)}$$

$$t_0 = \frac{\bar X - \mu_0}{S/\sqrt n} \qquad \text{(2.8)}$$

- Bajo $H_0$, $t_0 \sim t_{n-1}$. Se rechaza $H_0$ si $\lvert t_0 \rvert > t_{\alpha/2}$, donde
  $P(t > t_{\alpha/2}) = \alpha/2$ (figura 2.4). Justificación: hay probabilidad $100(1-\alpha)$ %
  de que $t_0$ caiga entre $-t_{\alpha/2}$ y $t_{\alpha/2}$ si $H_0$ es verdadera; un $t_0$ fuera
  es evidencia de que $H_0$ es falsa. La región de rechazo $(-\infty, -t_{\alpha/2}) \cup
  (t_{\alpha/2}, \infty)$ está determinada por $\alpha$.
- Unilaterales:

$$H_0: \mu = \mu_0,\ H_A: \mu > \mu_0 \ \text{(2.9): rechazar si } t_0 > t_\alpha \qquad H_0: \mu = \mu_0,\ H_A: \mu < \mu_0 \ \text{(2.10): rechazar si } t_0 < -t_\alpha$$

**Ejemplo 2.4 (peso de costales de azúcar, págs. 35–36).** El vendedor afirma peso medio
50.1 kg con varianza 0.5. El comprador sospecha que el peso medio es menor:

$$H_0: \mu = 50.1 \qquad H_A: \mu < 50.1 \qquad \text{(2.11)}$$

con $\alpha = 0.05$. Tres bultos al azar de cada uno de cinco pedidos: $n = 15$,
$\bar X = 49.4$, $S^2 = 1.2$.

$$t_0 = \frac{\sqrt{15}\,(49.4 - 50.1)}{\sqrt{1.2}} = -2.47$$

$t_{0.05,14} = 1.76$; como $t_0 = -2.47 < -1.76$, se rechaza $H_0$: se rechaza la afirmación del
vendedor y la evidencia señala que el peso medio es menor (figura 2.5).

## Prueba para la varianza (págs. 36–37)

En el ejemplo de los costales la varianza declarada ($\sigma^2 = 0.5$) es bastante distinta de
la muestral ($S^2 = 1.2$); que sean distintas no significa que sean estadísticamente
diferentes, de ahí la prueba:

$$H_0: \sigma^2 = \sigma_0^2 \qquad H_A: \sigma^2 > \sigma_0^2$$

$$\chi_0^2 = \frac{(n-1)S^2}{\sigma_0^2}$$

- Bajo normalidad y $H_0$, $\chi_0^2 \sim \chi^2_{n-1}$. Se rechaza si $\chi_0^2 > \chi^2_\alpha$.
- Costales: $\chi_0^2 = 14(1.2)/0.5 = 33.6$; $\chi^2_{0.05,14} = 23.68$; $33.6 > 23.68$, se
  rechaza $H_0$: la varianza reportada por el vendedor es falsa y la variabilidad real es mayor.
- Alternativa bilateral: rechazar si $\chi_0^2 > \chi^2_{\alpha/2}$ o $\chi_0^2 < \chi^2_{1-\alpha/2}$.

## Tres criterios de rechazo o aceptación equivalentes (págs. 37–39)

Los tres llevan siempre a la misma decisión, pero algunos dan información adicional.

### Criterio 1 · Estadístico de prueba frente a valor crítico

 Rechazar si el estadístico cae en la región
de rechazo delimitada por el valor crítico. Es el método tradicional (previo a la
computación) y el que menos información adicional da. Hay que comparar los valores
adecuados según la alternativa.
### Criterio 2 · Significancia observada frente a significancia predefinida

 La **significancia
predefinida** $\alpha$ es el riesgo máximo que el experimentador acepta de rechazar $H_0$
indebidamente. La **significancia observada** o **valor-p** es el área bajo la distribución de
referencia **más allá** del valor del estadístico de prueba; en la T bilateral:

$$\text{valor-}p = P(T < -t_0) + P(T > t_0)$$

y en una prueba unilateral es el área a la derecha (o izquierda) de $t_0$. Se rechaza $H_0$
si **valor-p $< \alpha$**. Es mejor criterio que el anterior porque el valor-p es la evidencia
a favor de $H_0$: mide la contundencia del rechazo. Un valor-p de 0.0001 dice que el
estadístico observado prácticamente no tenía posibilidad de ocurrir si $H_0$ fuera
verdadera. Figura 2.6: $\lvert t_0 \rvert < t_{\alpha/2}$ ocurre exactamente cuando
valor-p $> \alpha$. Comparar $t_0$ con $t_{\alpha/2}$ es contrastar números; comparar
valor-p con $\alpha$ es contrastar probabilidades, más informativo.
### Criterio 3 · Intervalo de confianza

 Se rechaza $H_0$ si el valor declarado en $H_0$ queda fuera del
intervalo de confianza del parámetro. Hipótesis bilateral: intervalo al $100(1-\alpha)$ %.
Hipótesis **unilateral**: intervalo al $100(1 - 2\alpha)$ %, para que el área fuera de cada
extremo sea $\alpha$, y además hay que verificar que el intervalo quede **del lado que indica
$H_A$**. Costales ($\alpha = 0.05$, intervalo al 90 %):

$$\bar X \pm t_{0.05,14}\frac{S}{\sqrt n} = 49.40 \pm 1.76\,\frac{1.095}{3.873} = 49.40 \pm 0.497 = [48.9,\ 49.9]$$

50.1 no pertenece al intervalo y el intervalo está a la izquierda de 50.1 (como pide
$H_A: \mu < 50.1$): se rechaza $H_0$. Útil cuando el software da el intervalo pero no la
prueba, y cuando además de la decisión se quiere el intervalo del parámetro.

---

## Hipótesis para dos medias: comparación de dos tratamientos (págs. 39–43)

Comparar dos procesos o tratamientos: dos proveedores, dos materiales, dos máquinas, dos
métodos. Ejemplo: máquinas A y B que hacen la misma operación; datos $Y_{A1}, \dots, Y_{An}$ y
$Y_{B1}, \dots, Y_{Bn}$ (tabla 2.2).

**Para que la comparación sea justa**: la materia prima se asigna **al azar** a las máquinas
(cada una recibe material de calidad equivalente) y las $2n$ corridas se hacen en **orden
aleatorio** (se reparte por igual el efecto de las fuentes de variabilidad que actúan durante
las pruebas, como las ambientales). No es adecuado correr primero todas las de A y luego todas
las de B: sesga la comparación.

**Varianzas desconocidas pero iguales.** Procesos con medias $\mu_x$, $\mu_y$ y varianzas
$\sigma_x^2$, $\sigma_y^2$:

$$H_0: \mu_x = \mu_y \qquad H_A: \mu_x \ne \mu_y \qquad \text{(2.12)} \qquad\Longleftrightarrow\qquad H_0: \mu_x - \mu_y = 0 \qquad H_A: \mu_x - \mu_y \ne 0 \qquad \text{(2.13)}$$

Muestras de tamaños $n_x$ y $n_y$ (es recomendable $n_x = n_y = n$, pero no obligatorio). Si cada
proceso es normal y son independientes:

$$t_0 = \frac{\bar X - \bar Y}{S_p\sqrt{\dfrac{1}{n_x} + \dfrac{1}{n_y}}} \qquad \text{(2.14)} \qquad\qquad S_p^2 = \frac{(n_x - 1)S_x^2 + (n_y - 1)S_y^2}{n_x + n_y - 2}$$

- $t_0 \sim t_{n_x + n_y - 2}$ bajo $H_0$. Rechazar si $\lvert t_0 \rvert > t_{\alpha/2}$; si
  $H_A: \mu_x > \mu_y$, rechazar si $t_0 > t_\alpha$; si $H_A: \mu_x < \mu_y$, si $t_0 < -t_\alpha$.
  Equivalentemente, rechazar si valor-p $< \alpha$.

**Ejemplo 2.5 (dos centrifugadoras, págs. 41–42).** La calidad de la pintura látex depende del
tamaño de partícula; dos centrifugadoras lo miden y se sospecha que reportan valores distintos.
13 lecturas de un mismo lote con cada una:

| | Lecturas | $\bar X$ | $S^2$ |
|---|---|---|---|
| Centrifugadora A (x) | 4714, 4601, 4696, 4896, 4905, 4870, 4987, 5144, 3962, 4066, 4561, 4626, 4924 | 4684.00 | 124 732.00 |
| Centrifugadora B (y) | 4295, 4271, 4326, 4530, 4618, 4779, 4752, 4744, 3764, 3797, 4401, 4339, 4700 | 4408.92 | 112 020.00 |

Hipótesis bilateral (no hay conjetura sobre cuál reporta más), $\alpha = 0.05$, varianzas
iguales:

$$t_0 = \frac{4684.00 - 4408.92}{344.06\sqrt{1/13 + 1/13}} = 2.04$$

$t_{0.025,24} = 2.064$; $\lvert t_0 \rvert = 2.04 < 2.064$: **no se rechaza** $H_0$, las
centrifugadoras reportan en promedio el mismo tamaño. Pero el margen es escaso: valor-p
$= 0.053$; con $\alpha = 0.055$ se rechazaría. No es recomendable cambiar $\alpha$ a posteriori,
aunque hay situaciones en que se admiten riesgos hasta de $\alpha = 0.1$.

**Significancia práctica.** La diferencia observada $\bar X - \bar Y = 275.08$ estima la
diferencia de medias poblacionales. Si 275.08 es una diferencia relevante para la calidad,
eso favorece seguir verificando si es real (considerar $\alpha = 0.055$ o tomar más datos); si
es despreciable en la práctica, conviene aplicar estrictamente $\alpha = 0.05$ y concluir
igualdad.

**Varianzas desconocidas y distintas.** El caso de varianzas iguales es el más usado, pero a
veces no hay base para suponerlas iguales (dos proveedores sin datos históricos):

$$t_0 = \frac{\bar X - \bar Y}{\sqrt{\dfrac{S_x^2}{n_x} + \dfrac{S_y^2}{n_y}}} \qquad \text{(2.15)} \qquad\qquad v = \frac{\left(\dfrac{S_x^2}{n_x} + \dfrac{S_y^2}{n_y}\right)^2}{\dfrac{(S_x^2/n_x)^2}{n_x + 1} + \dfrac{(S_y^2/n_y)^2}{n_y + 1}} - 2 \qquad \text{(2.16)}$$

- Aproximadamente $t_v$. Rechazar si $\lvert t_0 \rvert > t_{\alpha/2, v}$ o valor-p $< \alpha$.
- Centrifugadoras sin suponer varianzas iguales: $t_0 = 2.04$, $v = 26$, valor-p $= 0.052$;
  misma decisión y valores prácticamente iguales.
- Nota: la fórmula (2.16) de este libro (con $n + 1$ en los denominadores y el $-2$ final) es la
  aproximación de Welch–Satterthwaite escrita de otra forma; la ec. 2-32 de Montgomery usa
  $n - 1$ sin el $-2$. Dan grados de libertad parecidos, no idénticos.

## Prueba para la igualdad de varianzas (págs. 43–44)

En lugar de suponer varianzas iguales o distintas, se puede verificar:

$$H_0: \sigma_x^2 = \sigma_y^2 \qquad H_A: \sigma_x^2 \ne \sigma_y^2 \qquad \text{(2.17)} \qquad\Longleftrightarrow\qquad H_0: \frac{\sigma_x^2}{\sigma_y^2} = 1 \qquad H_A: \frac{\sigma_x^2}{\sigma_y^2} \ne 1 \qquad \text{(2.18)}$$

$$F_0 = \frac{S_x^2}{S_y^2} \qquad \text{(2.19)}$$

- Bajo $H_0$, $F_0 \sim F_{n_x - 1,\ n_y - 1}$. La comparación de varianzas interesa por sí misma:
  a menor varianza, potencialmente mejor calidad (¿cuál centrifugadora tiene mayor error de
  medición?).
- Centrifugadoras: $F_0 = 1.11$. Como la F no es simétrica, el valor-p es el área a la derecha de
  1.11 más el área a la izquierda de $1/1.11 = 0.9$; Statgraphics da valor-p $= 0.85$. No se
  rechaza: misma variabilidad, precisión o error de medición; el valor-p tan grande hace la
  decisión contundente.
- Nota al pie: $F_{1-\alpha,\,n_1-1,\,n_2-1} = 1/F_{\alpha,\,n_2-1,\,n_1-1}$ (se intercambian los
  grados de libertad del numerador y del denominador).

## Comparación de proporciones (pág. 44)

$$H_0: p_1 = p_2 \qquad H_A: p_1 \ne p_2 \qquad\qquad z_0 = \frac{\hat p_1 - \hat p_2}{\sqrt{\hat p(1-\hat p)\left(\dfrac{1}{n_1} + \dfrac{1}{n_2}\right)}}, \qquad \hat p = \frac{x_1 + x_2}{n_1 + n_2}$$

- Rechazar si $\lvert z_0 \rvert > z_{\alpha/2}$ (unilateral: comparar con $z_\alpha$).
- Ejemplo: dos fármacos, $n_1 = n_2 = 100$, recuperados $x_1 = 65$ y $x_2 = 75$;
  $\hat p = 140/200 = 0.70$; $z_0 = (0.65 - 0.75)/\sqrt{0.7(0.3)(1/100 + 1/100)} = -1.543$;
  $\lvert z_0 \rvert < 1.96$: no hay evidencia de que un fármaco sea mejor.

---

## Poblaciones pareadas: comparación de dos medias con muestras dependientes (págs. 44–48)

- En las pruebas anteriores las dos muestras son **independientes**: la muestra del
  tratamiento 1 es independiente de la del tratamiento 2 y los datos se obtienen en **orden
  completamente al azar** (las unidades se asignan al azar a los tratamientos y las corridas se
  hacen en orden estrictamente aleatorio, para evitar sesgos que favorezcan a un tratamiento).
- En muchas situaciones no conviene o no es posible tomar muestras independientes; la mejor
  estrategia son **muestras pareadas**: los datos de ambos tratamientos se obtienen **por
  pares**, y cada par tiene algo en común (por ejemplo, la misma unidad experimental recibe
  ambos tratamientos). Ejemplos: los mismos pacientes reciben dos medicamentos en distintas
  ocasiones; las mismas piezas se miden con dos instrumentos.
- Al medir sobre la misma unidad las mediciones están relacionadas (no son independientes),
  pero la comparación es más justa y precisa: al mirar las diferencias dentro de la misma
  unidad se eliminan otras fuentes de variación. Si una pieza es grande, ambos instrumentos
  tenderán a reportar valores altos (fuerte correlación); las diferencias sobre la misma pieza
  se deben principalmente al sistema de medición.

**Ejemplo 2.6 (dos básculas, págs. 45–46).** ¿Están sincronizadas? 10 especímenes, cada uno
pesado en ambas básculas, orden al azar, mismo operador (tabla 2.3):

| Espécimen | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | Media |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Báscula 1 | 11.23 | 14.36 | 8.33 | 10.50 | 23.42 | 9.15 | 13.47 | 6.47 | 12.40 | 19.38 | 12.87 |
| Báscula 2 | 11.27 | 14.41 | 8.35 | 10.52 | 23.41 | 9.17 | 13.52 | 6.46 | 12.45 | 19.35 | 12.89 |
| Diferencia | −0.04 | −0.05 | −0.02 | −0.02 | −0.01 | −0.02 | −0.05 | 0.01 | −0.05 | 0.03 | −0.022 |

$H_0: \mu_1 = \mu_2$ contra $H_A: \mu_1 \ne \mu_2$ se plantea de forma equivalente sobre la
**media de la población de diferencias** $\mu_D$:

$$H_0: \mu_D = 0 \qquad H_A: \mu_D \ne 0 \qquad \text{(2.20)}$$

El problema de dos medias se convierte en el de **una media contra una constante** ($\mu_0 = 0$),
así que el estadístico es el caso particular de (2.8) aplicado a las $n$ diferencias:

$$t_0 = \frac{\bar d}{S_D/\sqrt n} \qquad \text{(2.21)}$$

Con $\bar d = -0.02$, $S_D = 0.0287$, $n = 10$: $t_0 = -0.02/(0.0287/\sqrt{10}) = -2.20$. Bajo
$H_0$, $t_0 \sim t_{n-1}$; se rechaza si $\lvert t_0 \rvert > t_{\alpha/2, n-1}$ o valor-p $< \alpha$.
Valor-p $= 0.055 > 0.05$: **no se rechaza**, no hay evidencia suficiente contra la sincronización.
Pero la conclusión es endeble: con $\alpha = 0.06$ se concluiría lo contrario; el experimentador
debería considerar asumir ese 6 % de riesgo.

Si en lugar de las diferencias se analizaran por separado las mediciones de cada báscula, el
efecto de las posibles diferencias entre instrumentos se mezclaría con la variabilidad propia
de las piezas; aun con dos grupos distintos de 10 especímenes, la variabilidad de las piezas
dentro de cada grupo más las diferencias entre grupos probablemente ocultaría el efecto de los
instrumentos. Las observaciones pareadas son necesarias para **eliminar fuentes de variabilidad**
que impedirían una comparación eficaz.

### Poblaciones pareadas: caso más general (págs. 47–48)

La prueba pareada busca que las diferencias observadas se deban a los tratamientos y no a la
heterogeneidad de los especímenes. Cuando no se pueden hacer dos mediciones sobre la misma
pieza (por ejemplo, el material tiene una historia larga: proveedores, lotes, turnos, días,
subprocesos), se identifican las **fuentes principales de variabilidad** y se parean los datos
con base en ellas.

**Ejemplo (impurezas en cofres levantados y bajados, págs. 47–48).** En una fábrica de autos se
conjetura que el número de impurezas en la pintura del cofre depende de si el auto pasó por los
hornos de secado con el cofre cerrado o abierto. No era adecuado usar muestras independientes
porque los **días** y los **turnos** influyen en las impurezas: esos dos factores se usaron como
**criterio de apareamiento** (tabla 2.4). Cada dato es el promedio de 10 autos (200 autos en
total). Aleatorización por parejas: antes de entrar al horno se sorteaba si el primero iba
levantado o bajado, y el segundo iba al contrario.

| Bloque | Día | Turno | Bajado | Levantado | Diferencia |
|---|---|---|---|---|---|
| 1 | Lunes | M | 3.4 | 2.7 | 0.7 |
| 2 | Lunes | T | 3.7 | 3.2 | 0.5 |
| 3 | Martes | M | 2.9 | 1.8 | 1.1 |
| 4 | Martes | T | 2.5 | 1.9 | 0.6 |
| 5 | Miércoles | M | 1.6 | 1.1 | 0.5 |
| 6 | Miércoles | T | 2.8 | 2.2 | 0.6 |
| 7 | Jueves | M | 3.7 | 2.8 | 0.9 |
| 8 | Jueves | T | 5.9 | 4.8 | 1.1 |
| 9 | Viernes | M | 4.8 | 4.3 | 0.5 |
| 10 | Viernes | T | 4.3 | 3.4 | 0.9 |
| | | Media | 3.56 | 2.82 | 0.74 |
| | | Desv. est. | 1.23 | 1.15 | 0.24 |

$$H_0: \mu_D = 0 \qquad H_A: \mu_D \ne 0 \qquad \text{(2.22)} \qquad\qquad t_0 = \frac{0.74}{0.2413/\sqrt{10}} = 9.70, \quad \text{valor-}p = 0.0000046$$

Se rechaza de manera contundente: el número de impurezas depende de la posición del cofre, y con
el cofre levantado hay menos. Se decidió levantar los cofres al entrar a los hornos, con una
reducción significativa de impurezas.

Lección: en la tabla 2.4 hay gran variabilidad entre días y entre turnos. Si se analizaran los
datos como **muestras independientes**, el estadístico sería $t = 1.39$ con valor-p $= 0.18$, y
se concluiría **equivocadamente** que no hay diferencia. El apareamiento por día y turno
aseguró unidades homogéneas, de modo que las diferencias dentro de un mismo día y turno se
deben en gran medida a los tratamientos.

---

## Resumen de fórmulas para procedimientos de prueba de hipótesis (págs. 49–50)

Con software conviene basarse en el criterio del valor-p: para cualquier hipótesis, se rechaza
$H_0$ si valor-p $< \alpha$.

**Tabla 2.5. Un parámetro**

| Hipótesis | Estadístico de prueba | Criterio de rechazo |
|---|---|---|
| a) $H_0: \mu = \mu_0$; $H_A: \mu \ne \mu_0$ / $\mu > \mu_0$ / $\mu < \mu_0$ | $t_0 = \dfrac{\bar X - \mu_0}{S/\sqrt n}$ | $\lvert t_0 \rvert > t_{\alpha/2}$ / $t_0 > t_\alpha$ / $t_0 < -t_\alpha$ |
| b) $H_0: \sigma^2 = \sigma_0^2$; $H_A: \sigma^2 \ne \sigma_0^2$ / $\sigma^2 > \sigma_0^2$ / $\sigma^2 < \sigma_0^2$ | $\chi_0^2 = \dfrac{(n-1)S^2}{\sigma_0^2}$ | $\chi_0^2 > \chi^2_{\alpha/2,\,n-1}$ o $\chi_0^2 < \chi^2_{1-\alpha/2,\,n-1}$ / $\chi_0^2 > \chi^2_{\alpha,\,n-1}$ / $\chi_0^2 < \chi^2_{1-\alpha,\,n-1}$ |
| c) $H_0: p = p_0$; $H_A: p \ne p_0$ / $p > p_0$ / $p < p_0$ | $z_0 = \dfrac{X - np_0}{\sqrt{np_0(1-p_0)}}$, $X$ = número de defectos | $\lvert z_0 \rvert > z_{\alpha/2}$ / $z_0 > z_\alpha$ / $z_0 < -z_\alpha$ |

**Tabla 2.6. Dos parámetros**

| Hipótesis | Estadístico de prueba | Criterio de rechazo |
|---|---|---|
| a) $H_0: \mu_1 = \mu_2$ (independientes, varianzas iguales) | $t_0 = \dfrac{\bar X_1 - \bar X_2}{S_p\sqrt{1/n_1 + 1/n_2}}$, $S_p^2 = \dfrac{(n_1-1)S_1^2 + (n_2-1)S_2^2}{n_1+n_2-2}$ | $\lvert t_0 \rvert > t_{\alpha/2,\,n_1+n_2-2}$ / $t_0 > t_{\alpha,\,n_1+n_2-2}$ / $t_0 < -t_{\alpha,\,n_1+n_2-2}$ |
| b) $H_0: \mu_1 = \mu_2$ (independientes, varianzas distintas) | $t_0 = \dfrac{\bar X_1 - \bar X_2}{\sqrt{S_1^2/n_1 + S_2^2/n_2}}$, $v$ de (2.16) | $\lvert t_0 \rvert > t_{\alpha/2,\,v}$ / $t_0 > t_{\alpha,\,v}$ / $t_0 < -t_{\alpha,\,v}$ |
| c) $H_0: \sigma_1^2 = \sigma_2^2$ | $F_0 = \dfrac{S_1^2}{S_2^2}$ | $F_0 > F_{\alpha/2,\,n_1-1,\,n_2-1}$ o $F_0 < F_{1-\alpha/2,\,n_1-1,\,n_2-1}$ / $F_0 > F_{\alpha,\,n_1-1,\,n_2-1}$ / $F_0 < F_{1-\alpha,\,n_1-1,\,n_2-1}$ |
| d) $H_0: p_1 = p_2$ | $z_0 = \dfrac{\hat p_1 - \hat p_2}{\sqrt{\hat p(1-\hat p)(1/n_1 + 1/n_2)}}$, $\hat p = \dfrac{X_1 + X_2}{n_1 + n_2}$ | $\lvert z_0 \rvert > z_{\alpha/2}$ / $z_0 > z_\alpha$ / $z_0 < -z_\alpha$ |
| e) $H_0: \mu_1 = \mu_2$ (muestras pareadas) | $t_0 = \dfrac{\bar d}{S_d/\sqrt n}$ | $\lvert t_0 \rvert > t_{\alpha/2,\,n-1}$ / $t_0 > t_{\alpha,\,n-1}$ / $t_0 < -t_{\alpha,\,n-1}$ |

Tres maneras de probar $H_0: \mu_1 = \mu_2$: a) independientes con varianzas iguales,
b) independientes sin suponerlas iguales, e) pareadas.

## Uso de un software estadístico (págs. 49–51)

- **Statgraphics**: estimación y prueba para una media o desviación estándar en
  Describe → Numeric data → One-variable analysis (Confidence intervals; Hypothesis tests). Dos
  muestras independientes: Compare → Two samples → Two-sample comparison (Comparison of means,
  Comparison of standard deviations). Pareadas: Compare → Two samples → Paired-sample comparison.
- **Minitab**: Stat → Basic Statistics, y ahí la opción para una muestra, dos muestras o muestra
  pareada.
- **Excel**: Herramientas → Análisis de datos → Estadística descriptiva (nivel de confianza para
  la media); Prueba t para dos muestras suponiendo varianzas iguales; Prueba t para medias de
  dos muestras emparejadas; Prueba F para varianzas de dos muestras.

## Preguntas y ejercicios (págs. 51–59, solo ubicación)

Preguntas conceptuales 1–10 (población y muestra, prueba de hipótesis, estimación puntual y
por intervalo, papel de las distribuciones, estadístico de prueba, errores tipo I y II, los tres
criterios equivalentes, ejemplo de muestras pareadas). Ejercicios de estimación 11–14 (botellas,
nicotina, resistencia de envases, CO en bebidas); pruebas para una media y una varianza;
comparación de dos tratamientos; pruebas pareadas (33 en adelante).

## Diferencias de notación y de enfoque frente a Montgomery

| Aspecto | Montgomery (cap. 2) | Gutiérrez–De la Vara (cap. 2) |
|---|---|---|
| Hipótesis alternativa | $H_1$ | $H_A$ |
| Media muestral | $\bar y$ | $\bar X$ |
| Tamaño de muestra | Curvas OC: $\delta$, $\sigma$, $\beta$ | Error máximo de estimación $E$: $n \approx 4S^2/E^2$; $\beta = 0.10$ recomendado |
| Varianza conocida | Pruebas $Z$ (2-4.5, 2-4.6) | No se desarrolla (caso irreal en la práctica) |
| Proporciones | No | Intervalo, prueba para $p$ y para $p_1 = p_2$ |
| Criterios de decisión | Valor crítico, valor $P$ e IC | Los mismos tres, presentados como criterios **equivalentes** y con la regla del IC al $100(1-2\alpha)$ % para pruebas unilaterales |
| Supuestos | Gráfica de probabilidad normal, prueba de aleatorización | Se remite al cap. 3 (verificación de supuestos del ANOVA) |
| Grados de libertad con varianzas distintas | Ec. 2-32 (Welch con $n_i - 1$) | Ec. (2.16) (con $n_i + 1$ y $-2$) |
| Ejemplo pareado | Dureza con dos puntas (10 ejemplares) | Dos básculas (10 especímenes) y cofres por día y turno (10 bloques) |
