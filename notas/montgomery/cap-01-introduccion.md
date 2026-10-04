# Capítulo 1 — Introducción

> Montgomery, págs. 1–20

Ficha técnica de consulta. Capítulo conceptual (sin fórmulas de análisis): define el
vocabulario del diseño experimental, compara estrategias de experimentación, fija los tres
principios básicos y da el procedimiento de 7 pasos para planear un experimento.

---

## 1-1 Estrategia de experimentación

### Definiciones

- **Experimento**: prueba o serie de pruebas en las que se cambian deliberadamente las
  variables de entrada de un proceso o sistema para observar e identificar las causas de los
  cambios en la respuesta de salida.
- **Proceso robusto**: el que resulta mínimamente afectado por fuentes externas de variabilidad.
- **Experimentador**: quien realiza el experimento.
- **Estrategia de experimentación**: el enfoque general para planear y conducir el experimento.
- **Confusión** (nota al pie, pág. 2): dos efectos están *confundidos* cuando no pueden
  separarse. Ejemplo del templado: si los ejemplares templados en aceite vienen de una hornada
  y los templados en agua salada de otra, el efecto del medio de templado y el de la hornada
  quedan confundidos; la forma de recolectar los datos arruinó las conclusiones posibles.

### Preguntas previas a cualquier experimento (ejemplo del templado, págs. 1–2)

Ingeniero metalúrgico que compara templado en aceite vs. en agua salada sobre la dureza de una
aleación de aluminio. Antes de correr hay que responder:

1. ¿Son esos dos los únicos tratamientos de interés?
2. ¿Hay otros factores que afecten la respuesta y deban investigarse o controlarse?
3. ¿Cuántas unidades experimentales por tratamiento (réplicas)?
4. ¿Cómo se asignan las unidades a los tratamientos y en qué orden se toman los datos?
5. ¿Qué método de análisis se usará?
6. ¿Qué diferencia en la respuesta media se considera importante?

### Modelo general de un proceso (figura 1-1)

Entradas → **Proceso** → salida $y$ (una o más respuestas). Sobre el proceso actúan:

- factores **controlables** $x_1, x_2, \dots, x_p$;
- factores **no controlables** $z_1, z_2, \dots, z_q$ (aunque pueden controlarse para los fines de
  una prueba).

Objetivos posibles del experimento:

1. Determinar qué variables influyen más en la respuesta $y$.
2. Determinar el ajuste de las $x$ influyentes para que $y$ esté casi siempre cerca del valor
   nominal deseado.
3. Determinar el ajuste de las $x$ influyentes para que la variabilidad de $y$ sea pequeña.
4. Determinar el ajuste de las $x$ influyentes para que los efectos de las no controlables
   $z_1,\dots,z_q$ sean mínimos.

### Comparación de estrategias (ejemplo del golf, págs. 3–7)

Factores candidatos (8): tipo de palo (grande/normal), tipo de pelota (goma de balata/tres
piezas), caminar o usar carrito, beber agua o cerveza, mañana/tarde, frío/calor, tipo de spikes,
viento/apacible. Por experiencia el autor descarta los factores 5–8 (efectos sin valor práctico)
y estudia los 4 primeros con un máximo de 8 rondas.

| Estrategia | En qué consiste | Desventajas / propiedades |
|---|---|---|
| **Mejor conjetura** | Elegir una combinación arbitraria, probarla y cambiar uno (o dos) niveles según el resultado. | Funciona si hay mucho conocimiento técnico y experiencia. (1) Si la conjetura inicial falla hay que seguir conjeturando sin garantía de éxito; (2) si da un resultado aceptable se tiende a parar sin garantía de haber hallado la mejor solución. |
| **Un factor a la vez** | Fijar una línea base de niveles y variar sucesivamente cada factor en su rango manteniendo los demás en el nivel base; se grafican las respuestas (fig. 1-2). | **No puede detectar interacciones.** Si existen (y son muy comunes), casi siempre da resultados deficientes. Siempre es menos eficiente que los métodos con base estadística. |
| **Factorial** | Los factores se varían *en conjunto*: se corren todas las combinaciones de niveles. | Enfoque correcto para varios factores. Hace el uso más eficiente de los datos: todas las observaciones sirven para estimar cada efecto. Permite estimar interacciones. |

- **Interacción**: uno de los factores no produce el mismo efecto sobre la respuesta en niveles
  diferentes de otro factor. Fig. 1-3: con palo normal la bebida casi no afecta la puntuación;
  con palo grande, beber agua da resultados mucho mejores que beber cerveza.
- Con las gráficas de un factor a la vez (fig. 1-2) se elegiría palo normal, carrito y agua, y
  la pelota parecería irrelevante; conclusión que puede ser errónea si hay interacciones.

### Diseño factorial $2^2$ del golf (figs. 1-4 y 1-5)

Factores: tipo de palo (G = grande, N = normal) y tipo de pelota (GB = goma de balata, TP =
tres piezas); dos **réplicas** (8 rondas). Puntuaciones en los vértices del cuadrado:

| | Palo G | Palo N |
|---|---|---|
| Pelota TP | 88, 91 | 92, 94 |
| Pelota GB | 88, 90 | 93, 91 |

Cálculo de efectos (diferencia de promedios de 4 observaciones contra 4):

$$\text{Efecto del palo} = \frac{92+94+93+91}{4} - \frac{88+91+88+90}{4} = 3.25$$

$$\text{Efecto de la pelota} = \frac{88+91+92+94}{4} - \frac{88+90+93+91}{4} = 0.75$$

$$\text{Interacción pelota-palo} = \frac{92+94+88+90}{4} - \frac{88+91+93+91}{4} = 0.25$$

- El efecto principal de un factor compara los dos lados opuestos del cuadrado; la interacción
  compara los promedios de las dos diagonales.
- Interpretación: pasar del palo grande al normal *aumenta* la puntuación 3.25 golpes por ronda
  (peor en golf). El autor indica que hay evidencia estadística razonablemente sólida de que
  el efecto del palo difiere de cero y no para los otros dos → jugar siempre con el palo grande.
- **Efectos principales**: efectos individuales de cada factor.

### Factoriales $2^k$ y fraccionados (figs. 1-6 a 1-8)

- $2^3$ (palo, pelota, bebida): 8 combinaciones = vértices de un cubo. Con 8 rondas (una por
  vértice) da la misma información sobre cada efecto principal que el $2^2$ con dos réplicas:
  4 corridas en cada nivel de cada factor.
- $2^4$ (se agrega manera de desplazarse): 16 corridas; geométricamente dos cubos (hipercubo).
- En general, $k$ factores a dos niveles requieren $2^k$ corridas: 10 factores → 1024 corridas;
  rápidamente impracticable.
- **Experimento factorial fraccionado**: variación del factorial en la que solo se corre un
  subconjunto de las combinaciones. Fig. 1-8: **fracción un medio** del $2^4$ con 8 corridas
  (en lugar de 16); da buena información sobre los efectos principales de los 4 factores y
  cierta información sobre sus interacciones. Con 4, 5 o más factores normalmente no es
  necesario probar todas las combinaciones. Se desarrollan en el capítulo 8.

---

## 1-2 Algunas aplicaciones típicas del diseño experimental

La experimentación es parte del proceso científico de aprendizaje: conjetura → experimento →
datos → nueva conjetura → nuevo experimento.

Beneficios de aplicar diseño experimental temprano en el desarrollo de un proceso:

1. Mejora del rendimiento del proceso.
2. Menor variabilidad y mayor conformidad con los requerimientos nominales.
3. Menor tiempo de desarrollo.
4. Menores costos globales.

Aplicaciones en **diseño de ingeniería** (productos):

1. Evaluar y comparar configuraciones básicas de diseño.
2. Evaluar materiales alternativos.
3. Seleccionar parámetros de diseño para que el producto funcione bien en una amplia variedad
   de condiciones de campo (producto **robusto**).
4. Determinar los parámetros clave del diseño que afectan el desempeño.

### Ejemplos del libro

- **Ejemplo 1-1 — Caracterización de un proceso** (págs. 8–9). Máquina de soldadura líquida
  para tarjetas de circuitos impresos; nivel de defectos ≈ 1 % de las juntas (más de 2000
  juntas por tarjeta, así que es demasiado). Factores controlables (7): temperatura de la
  soldadura, temperatura de precalentamiento, velocidad de la transportadora, tipo de fundente,
  gravedad específica del fundente, profundidad de la onda de soldadura, ángulo de la
  transportadora. Factores difíciles de controlar en producción (5): espesor de la tarjeta, tipo
  de componentes, disposición de los componentes, operador, rapidez de producción. Objetivo:
  **caracterizar** el proceso, es decir, identificar qué factores (controlables o no) afectan
  los defectos, estimar magnitud y dirección de los efectos y detectar interacciones. Se llama
  **experimento tamiz o de exploración** (*screening*); típicamente se usan **factoriales
  fraccionados**. Consecuencia: saber qué variables del proceso vigilar con cartas de control
  (control sobre entradas en lugar de sobre la salida).
- **Ejemplo 1-2 — Optimización de un proceso** (págs. 9–11). Tras la caracterización, se busca
  la región de los factores importantes que da la mejor respuesta. Proceso químico: rendimiento
  en función de tiempo de reacción y temperatura; condiciones actuales 145 °F y 2.1 h con
  rendimiento ≈ 80 %. La fig. 1-9 muestra **contornos** de rendimiento (60, 70, 80, 90, 95 %)
  de la **superficie de respuesta**. Un factorial $2^2$ inicial alrededor del punto actual
  (respuestas en los vértices: 82, 78, 70, 75; centro 80) indica moverse hacia mayor
  temperatura y menor tiempo; se hacen corridas en esa dirección (trayectoria de ascenso) y
  luego un segundo experimento —un **diseño central compuesto**— para ajustar un modelo
  empírico y estimar el óptimo. Es la **metodología de superficies de respuesta** (cap. 11).
- **Ejemplo 1-3 — Diseño de un producto** (pág. 11). Gozne de la puerta de un automóvil;
  respuesta: esfuerzo amortiguador (capacidad de retención del tope). Factores (5): distancia
  que se desplaza el cilindro, altura del resorte del pivote a la base, distancia horizontal
  del pivote al resorte, altura libre del resorte auxiliar, altura libre del resorte principal.
  Se construye un prototipo donde pueden variarse los cinco factores y se prueba con varias
  combinaciones de niveles para identificar los factores más influyentes y mejorar el diseño.

---

## 1-3 Principios básicos

**Diseño estadístico de experimentos**: proceso de planear el experimento de modo que se
recaben datos adecuados que puedan analizarse con métodos estadísticos y lleven a conclusiones
válidas y objetivas. Cuando los datos están sujetos a error experimental, la metodología
estadística es el único enfoque objetivo de análisis. Todo problema experimental tiene dos
aspectos inseparables: el **diseño** del experimento y el **análisis estadístico** de los datos
(el método de análisis depende directamente del diseño empleado).

Los tres principios básicos son **réplicas**, **aleatorización** y **formación de bloques**.

### 1. Realización de réplicas

- Réplica = repetición del experimento básico. En el ejemplo del templado, una réplica es tratar
  una muestra en aceite y otra en agua salada; cinco ejemplares por medio = cinco réplicas.
- Dos propiedades:
  1. Permite obtener una **estimación del error experimental**, que es la unidad básica de
     medida para decidir si las diferencias observadas son estadísticamente diferentes.
  2. Si se usa la media muestral para estimar el efecto de un factor, da una **estimación más
     precisa**:

$$\sigma_{\bar y}^2 = \frac{\sigma^2}{n}$$

  donde $\sigma^2$ es la varianza de una observación individual y $n$ el número de réplicas.
- Consecuencia práctica: con $n = 1$ y observaciones $y_1 = 145$ (aceite), $y_2 = 147$ (agua
  salada) no se puede inferir nada sobre el medio de templado: la diferencia puede ser puro
  error experimental. Con $n$ razonablemente grande y error pequeño, $\bar y_1 < \bar y_2$ sí
  permite concluir con certeza razonable.
- **Réplicas ≠ mediciones repetidas.**
  - Medir tres veces una dimensión crítica de la misma oblea grabada: son mediciones repetidas;
    su variabilidad refleja solo el sistema o instrumento de medición.
  - Cuatro obleas procesadas simultáneamente en un horno con un mismo flujo de gas y tiempo, y
    medidas después: tampoco son réplicas; reflejan diferencias entre obleas y otras fuentes de
    variabilidad *dentro* de esa corrida particular del horno.
  - Las réplicas reflejan las fuentes de variabilidad **entre** corridas y (potencialmente)
    **dentro** de ellas.

### 2. Aleatorización

- Piedra angular del uso de métodos estadísticos en el diseño experimental.
- Definición: tanto la **asignación del material experimental** como el **orden de las
  corridas** o ensayos individuales se determinan al azar.
- Por qué:
  1. Los métodos estadísticos requieren que las observaciones (o los errores) sean variables
     aleatorias independientes; la aleatorización suele hacer válido ese supuesto.
  2. Ayuda a "sacar del promedio" los efectos de factores extraños presentes. Ejemplo: si los
     ejemplares templados en aceite fueran sistemáticamente más gruesos que los del agua salada
     y el espesor afectara la dureza, habría un **sesgo sistemático** que invalidaría los
     resultados; la asignación aleatoria lo mitiga.
- Los programas de diseño suelen entregar las corridas en orden aleatorio (generador de números
  aleatorios), pero el experimentador sigue teniendo que asignar al azar el material, los
  operadores, los instrumentos, etc. Pueden usarse tablas de números aleatorios (tabla XI del
  apéndice).
- **Restricciones a la aleatorización**: cuando un factor es muy difícil de cambiar (p. ej. la
  temperatura de un proceso químico), la **aleatorización completa** es casi imposible. Existen
  diseños para tratar esas restricciones (ver en particular el cap. 13, parcelas subdivididas).

### 3. Formación de bloques

- Técnica de diseño para **mejorar la precisión** de las comparaciones entre los factores de
  interés.
- Se usa para reducir o eliminar la variabilidad transmitida por **factores perturbadores**
  (*nuisance factors*): factores que pueden influir en la respuesta pero en los que no hay
  interés específico.
- **Bloque**: conjunto de condiciones experimentales relativamente homogéneas. Ejemplo: dos
  lotes de materia prima necesarios para hacer todas las corridas de un proceso químico; cada
  lote es un bloque (la variabilidad dentro de un lote se espera menor que entre lotes).
- Regla típica: **cada nivel del factor perturbador pasa a ser un bloque**; las observaciones
  del diseño se dividen en grupos que se corren dentro de cada bloque.
- Se trata en los capítulos 4, 5, 7, 8, 9, 11 y 13; un ejemplo sencillo está en la sección
  2-5.1 (comparaciones pareadas).

Los tres principios forman parte de todo experimento.

---

## 1-4 Pautas generales para diseñar experimentos

Requisito previo: todos los participantes deben tener desde el principio una idea clara de qué
se va a estudiar, cómo se colectarán los datos y, al menos cualitativamente, cómo se analizarán.
Referencia para hojas de trabajo de planeación: Coleman y Montgomery [27].

**Tabla 1-1. Pautas generales para diseñar un experimento**

| Paso | Actividad | Etapa |
|---|---|---|
| 1 | Identificación y exposición del problema | Planeación previa al experimento |
| 2 | Elección de los factores, los niveles y los rangos (a) | Planeación previa al experimento |
| 3 | Selección de la variable de respuesta (a) | Planeación previa al experimento |
| 4 | Elección del diseño experimental | |
| 5 | Realización del experimento | |
| 6 | Análisis estadístico de los datos | |
| 7 | Conclusiones y recomendaciones | |

(a) En la práctica los pasos 2 y 3 suelen hacerse simultáneamente o en orden inverso.

### Paso 1. Identificación y enunciación del problema

- No es obvio en la práctica: cuesta reconocer que hay un problema que requiere experimentación
  y cuesta formular un enunciado claro con el que todos estén de acuerdo.
- Desarrollar todas las ideas sobre los objetivos; pedir aportes de todas las áreas (ingeniería,
  aseguramiento de calidad, manufactura, mercadotecnia, administración, cliente y **personal de
  operación**, que conoce a fondo el proceso y suele ser ignorado). Se recomienda un **enfoque
  de equipo**.
- Hacer una lista de los problemas o preguntas específicas que el experimento debe abordar.
- Tener presente el objetivo global:
  - proceso o sistema nuevo → **caracterización / tamizado** de factores;
  - sistema maduro, ya caracterizado → **optimización**;
  - otros objetivos: **confirmación** (¿se comporta igual que antes?), **descubrimiento** (¿qué
    pasa con nuevos materiales, variables, condiciones?), **estabilidad/robustez** (¿bajo qué
    condiciones se degrada la respuesta?).
- En esta etapa suele quedar claro que un único experimento grande y *comprensivo* no responde
  todas las preguntas clave y que conviene un **enfoque secuencial** con una serie de
  experimentos más pequeños.

### Paso 2. Elección de los factores, los niveles y los rangos

Clasificación de los factores que pueden influir en el desempeño:

| Clase | Subclase | Descripción |
|---|---|---|
| **Factores potenciales del diseño** (los que el experimentador podría querer variar) | Factores del diseño | Los realmente seleccionados para estudiarse en el experimento. |
| | Factores que se mantienen constantes | Pueden afectar la respuesta, pero no interesan en este experimento; se fijan en un nivel específico (p. ej. usar un solo grabador de plasma "típico"). |
| | Factores a los que se permite variar | P. ej. la falta de homogeneidad de las unidades experimentales o materiales; se ignora y se confía en la aleatorización para compensarla. |
| **Factores perturbadores** (pueden tener efectos grandes, pero no interesan) | Controlable | Sus niveles los puede fijar el experimentador (lotes de materia prima, días de la semana) → **formación de bloques**. |
| | No controlable pero medible | → **análisis de covarianza** (p. ej. humedad relativa del ambiente tratada como covariable). |
| | De ruido | Varía de manera natural e incontrolable en el proceso, pero puede controlarse para el experimento → buscar los ajustes de los factores controlables que minimicen la variabilidad transmitida: **estudio de robustez del proceso** (problema de diseño robusto). |

- Se suele suponer que los efectos de los factores mantenidos constantes y de los que se
  permite variar son relativamente pequeños.
- Tras elegir los factores del diseño hay que decidir: el **rango** de variación de cada uno
  (región de interés), los **niveles** específicos, cómo se controlarán en los valores deseados
  y cómo se medirán. Ejemplo de la soldadura líquida: 12 variables candidatas.
- Se requiere **conocimiento del proceso** (experiencia práctica + conocimientos teóricos).
  Investigar todos los factores que puedan ser importantes y no dejarse influir demasiado por la
  experiencia pasada, sobre todo en fases iniciales o con procesos no maduros.
- **Regla práctica para tamizado/caracterización**: mantener bajo el número de niveles —**dos
  niveles** funcionan bastante bien— y usar una región de interés **relativamente grande**
  (rangos amplios). Al aprender qué variables importan y qué niveles dan los mejores resultados,
  la región se estrecha.

### Paso 3. Selección de la variable de respuesta

- Debe proporcionar realmente información útil sobre el proceso bajo estudio.
- Lo más común es que la respuesta sea el promedio, la desviación estándar (o ambos) de la
  característica medida. Las respuestas múltiples no son la excepción.
- La **eficiencia de los instrumentos de medición** (error de medición) importa: si es
  inadecuada solo se detectarán efectos relativamente grandes o harán falta más réplicas. Opción
  cuando la capacidad de medición es pobre: medir varias veces cada unidad experimental y usar
  el promedio de las mediciones repetidas como respuesta observada.
- Definir las respuestas y cómo se medirán **antes** de correr el experimento. A veces se hacen
  experimentos diseñados para estudiar y mejorar el sistema de medición (ejemplo en el cap. 12).

Los pasos 1–3 constituyen la **planeación previa al experimento**; buena parte del éxito depende
de qué tan bien se haga. Rara vez una sola persona posee todo el conocimiento necesario: se
recomienda ampliamente el trabajo en equipo.

### Paso 4. Elección del diseño experimental

- Relativamente sencillo si la planeación previa se hizo bien. Implica decidir:
  - el **tamaño de la muestra** (número de réplicas);
  - un **orden de corridas** adecuado;
  - si hay **formación de bloques** u otras **restricciones sobre la aleatorización**.
- El software estadístico puede proponer diseños a partir del número de factores, niveles y
  rangos, y generar la hoja de trabajo con el orden aleatorizado. El autor prefiere **comparar
  varias alternativas** en lugar de aceptar sin más la recomendación del programa.
- Tener en mente los objetivos: en muchos experimentos de ingeniería ya se sabe que algunos
  niveles producirán respuestas distintas, así que interesa identificar **qué** factores causan
  la diferencia y estimar la **magnitud** del cambio. En otros casos el interés es verificar la
  uniformidad (p. ej. demostrar que no hay diferencia de rendimiento entre la condición
  estándar A y una alternativa más barata B).

### Paso 5. Realización del experimento

- Monitorear con atención el proceso para asegurar que todo se haga conforme a lo planeado; los
  errores en el procedimiento experimental en esta etapa suelen **destruir la validez
  experimental**.
- Es fácil subestimar la logística y la planeación en ambientes complejos de manufactura o de
  investigación y desarrollo.
- Recomendación (Coleman y Montgomery [27]): hacer **corridas piloto o de prueba** antes del
  experimento. Dan información sobre la consistencia del material experimental, una comprobación
  del sistema de medición, una idea aproximada del error experimental y la oportunidad de
  practicar la técnica experimental global; también permiten revisar las decisiones de los
  pasos 1–4.

### Paso 6. Análisis estadístico de los datos

- Usar métodos estadísticos para que los resultados y conclusiones sean objetivos y no
  apreciativos. Si el experimento se diseñó y ejecutó correctamente, los métodos necesarios no
  son complicados.
- Herramientas: software, **métodos gráficos simples**, pruebas de hipótesis e intervalos de
  confianza, **modelo empírico** (ecuación derivada de los datos que relaciona la respuesta con
  los factores importantes), **análisis residual** y verificación de la adecuación del modelo.
- Advertencia: los métodos estadísticos **no demuestran** que un factor tenga un efecto
  particular; solo dan pautas sobre la confiabilidad y validez de los resultados. Permiten medir
  el error posible de una conclusión o asignarle un nivel de confianza. Su ventaja principal es
  agregar objetividad a la toma de decisiones; combinados con buen conocimiento de ingeniería o
  del proceso y sentido común llevan a conclusiones sólidas.

### Paso 7. Conclusiones y recomendaciones

- Sacar conclusiones **prácticas** y recomendar un curso de acción. Los métodos gráficos son
  especialmente útiles para presentar los resultados.
- Realizar **corridas de seguimiento** y **pruebas de confirmación** para validar las
  conclusiones.
- La experimentación es **iterativa**: se formulan hipótesis tentativas, se experimenta, se
  reformulan. Generalmente es un gran error diseñar un único experimento comprensivo y extenso
  al principio de un estudio, porque al inicio no se conocen bien los factores importantes, sus
  rangos, el número de niveles ni las unidades de medición apropiadas. A lo largo del programa
  es común abandonar variables, incorporar otras, modificar la región de exploración o añadir
  respuestas.
- **Regla del 25 %**: como regla general, no invertir más del 25 % de los recursos disponibles
  en el primer experimento, para asegurar recursos para las corridas de confirmación y para
  alcanzar el objetivo final.

---

## 1-5 Breve historia del diseño estadístico

Cuatro eras:

1. **Era agrícola** — R. A. Fisher, años 1920 y principios de los 1930, Estación Agrícola
   Experimental de Rothamsted (cerca de Londres). Introdujo los tres principios básicos
   (aleatorización, réplicas, bloques), el diseño factorial y el análisis de varianza.
2. **Era industrial** — catalizada por la metodología de superficies de respuesta (MSR) de Box
   y Wilson [20]. Los experimentos industriales difieren de los agrícolas en (1) **inmediatez**
   (la respuesta se observa casi de inmediato) y (2) **secuencialidad** (pocas corridas dan
   información crucial para planear el siguiente experimento). En los 30 años siguientes la MSR
   se extendió en las industrias química y de proceso, sobre todo en investigación y desarrollo;
   la aplicación a nivel de planta seguía limitada por la poca formación estadística de los
   ingenieros y la falta de software fácil de usar.
3. **Tercera era** — desde fines de los 1970, impulsada por el interés occidental en el
   mejoramiento de la calidad y por Genichi Taguchi: **diseño paramétrico robusto**, que busca
   (1) hacer los procesos insensibles a factores ambientales o difíciles de controlar,
   (2) fabricar productos insensibles a la variación transmitida por los componentes y
   (3) encontrar los niveles de las variables del proceso que lleven la media al valor deseado
   reduciendo a la vez la variabilidad en torno a él. Taguchi propuso factoriales altamente
   fraccionados y otros arreglos ortogonales con métodos de análisis propios; la revisión
   posterior (fines de los 1980) concluyó que sus conceptos y objetivos de ingeniería son
   sólidos, pero que hay **problemas sustanciales con su estrategia experimental y sus métodos
   de análisis de datos** (panel de *Technometrics*, mayo de 1992).
4. **Cuarta era** — consecuencias positivas de la controversia: uso más generalizado de los
   experimentos diseñados en industrias de piezas discretas (automotriz, aeroespacial,
   electrónica, semiconductores); renovado interés y nuevos enfoques, incluidas alternativas
   eficientes a los métodos técnicos de Taguchi (cap. 11); educación formal en diseño
   experimental dentro de los programas de ingeniería.

---

## 1-6 Resumen: uso de técnicas estadísticas en la experimentación

Cuatro recomendaciones para el uso correcto de la estadística:

1. **Usar los conocimientos no estadísticos del problema.** El conocimiento del campo (teoría
   física, experiencia) es invaluable para elegir factores y niveles, decidir cuántas réplicas
   correr e interpretar los resultados. La estadística no sustituye la reflexión sobre el
   problema.
2. **Mantener el diseño y el análisis tan simples como sea posible.** Los métodos relativamente
   simples son casi siempre los mejores. Si el diseño se hace con cuidado, el análisis será
   relativamente directo; si el diseño se estropea, ni la estadística más compleja salva la
   situación.
3. **Distinguir entre significación práctica y significación estadística.** Que dos condiciones
   produzcan respuestas medias estadísticamente diferentes no garantiza que la diferencia tenga
   valor práctico. Ejemplo: una modificación al sistema de inyección que mejora el rendimiento
   del combustible en 0.1 mi/gal es estadísticamente significativa, pero si cuesta \$1000
   probablemente carece de valor práctico.
4. **Los experimentos son generalmente iterativos.** Al principio nadie conoce con certeza los
   factores importantes, sus rangos, el número de niveles ni los métodos y unidades de medición
   adecuados; las respuestas aparecen sobre la marcha. Esto favorece el enfoque iterativo o
   secuencial. Aunque hay situaciones donde un experimento comprensivo es apropiado, como regla
   general no invertir más del **25 %** de los recursos (corridas, presupuesto, tiempo) en el
   experimento inicial.

---

## Glosario rápido del capítulo

| Término | Significado |
|---|---|
| Factor | Variable de entrada que se varía deliberadamente (o se controla) en el experimento. |
| Nivel | Valor específico de un factor usado en las corridas. |
| Tratamiento | Nivel de un factor o combinación de niveles de varios factores. |
| Corrida | Ensayo individual del experimento. |
| Réplica | Repetición independiente del experimento básico. |
| Efecto principal | Cambio en la respuesta media al cambiar el nivel de un factor. |
| Interacción | El efecto de un factor depende del nivel de otro. |
| Factor perturbador | Factor que influye en la respuesta pero no es de interés. |
| Bloque | Conjunto de condiciones experimentales relativamente homogéneas. |
| Confusión | Imposibilidad de separar los efectos de dos factores. |
| Experimento tamiz | Experimento para identificar los pocos factores importantes entre muchos. |
| Superficie de respuesta | Respuesta vista como función de los factores; sus contornos son líneas de respuesta constante. |
