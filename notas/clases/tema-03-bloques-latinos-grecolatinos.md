# Tema 3 — Diseños de bloques aleatorios, cuadrados latinos y grecolatinos

Registro del contenido de las diapositivas de la profesora (clase del 3 de octubre de 2026).
Pie de todas las diapositivas: *Alexander Correa Espinal & Faviana Gutiérrez Rôa — Universidad
Nacional de Colombia*; marca lateral "Diseño de Experimentos Intermedio".

- **Fuente:** fotos en `notas/Diseño por bloques Latino y grecolatino/WhatsApp Unknown 2026-10-03 at 6.56.46 PM/`.
  Todos los archivos se llaman `WhatsApp Image 2026-10-03 at <hora> PM[ (n)].jpeg`; abajo se
  cita solo la parte variable, p. ej. `6.55.12 (1)`.
- **Imágenes:** 41 fotos → **39 diapositivas distintas** (2 fotos repetidas, indicadas abajo).
- **Orden:** las diapositivas no muestran número; el orden se reconstruyó por el contenido
  (coincide con el orden por nombre de archivo). Las tablas ANOVA sí vienen numeradas del 1 al
  10 en su título, y la foto del n.º 10 quedó guardada antes que la del n.º 9.
- **Lo que NO aparece en las fotos:** portada/índice, ejemplos numéricos resueltos, tablas
  ANOVA con datos, capturas de Minitab u otro software, gráficas de residuos, diapositiva de
  conclusiones. Si la profesora las mostró, no quedaron fotografiadas.
- Convención: `(ilegible)` = no se lee; `(poco legible)` = lectura probable pero no segura.

---

## Parte A — Registro diapositiva por diapositiva

### 1. Factor de ruido — `6.55.11`

El factor de ruido es un factor de diseño que probablemente tiene un efecto sobre la respuesta,
pero que no es de interés. Si este factor es:

- **Desconocido & Incontrolable:** no se conoce su existencia y por tanto, no se pueden
  controlar sus niveles, se recomienda **aleatorizar**.
- **Conocido & Incontrolable:** si se conoce el valor que toma el factor de ruido en cada prueba
  experimental, utilizar el **análisis de covarianza** (ANCOVA).
- **Conocido & Controlable:** cuando se conocen las fuentes de variación y pueden ser
  controladas para eliminar su efecto, se recomienda **bloquear**.

Frase de cierre (manuscrita): *¡Forme bloques con lo que pueda y aleatorice lo que no pueda!*

### 2. Factores de bloque — `6.55.12`

Son las variables adicionales al factor de interés, que se incorporan de manera explícita en un
experimento comparativo para no sesgar la comparación.

No interesa analizar su efecto, sino que son un medio para estudiar de manera adecuada y eficaz
al factor de interés.

Ilustración: una casa y una ventana con cortinas por la que se ve una familia comiendo.
Leyenda: *Factor de tratamiento: Familia. Factor de bloque: Ventana.*

### 3. Aleatorización de los bloques — `6.55.12 (1)`

El hecho de que existan bloques hace que no sea práctico o incluso imposible aleatorizar en su
totalidad. Ej.: si el factor de bloqueo es día:

**Totalmente aleatorizado** (columnas = factor de bloqueo, celdas = factor de tratamiento):

| Jue | Lun | Mié | Mar |
|---|---|---|---|
| D | A | C | B |
| C | B | D | A |
| A | C | B | D |
| B | D | A | C |

Rotulado con signos de interrogación: *¿Cómo regresar el tiempo?* (los días no se pueden
desordenar).

→ **Parcialmente aleatorizado (sólo los tratamientos):**

| Lun | Mar | Mié | Jue |
|---|---|---|---|
| A | B | C | D |
| B | A | D | C |
| C | D | B | A |
| D | C | A | B |

### 4. Diseños de bloque — `6.55.12 (2)`

Esquema con tres cajas que salen de "Diseños de bloques":

| N.º de factores de bloque | Diseño |
|---|---|
| 1 factor de bloque | Diseño en bloques completos al azar |
| 2 factores de bloque | Diseño en cuadrado latino |
| 3 factores de bloque | Diseño en cuadrado grecolatino |

(Cada diseño tiene un color fijo que se mantiene en toda la presentación: DBCA rojo, DCL azul,
DCGL amarillo/naranja.)

### 5. Diseño en bloques completos al azar — DBCA — `6.55.14`

**Fuentes de variabilidad:** se tienen tres posibles "culpables":

- Factor de tratamiento: factor de interés.
- Factor de bloque: factor que probablemente tiene un efecto sobre la respuesta, pero no se
  tiene interés en él y se puede controlar.
- Error aleatorio.

**Completo:** en cada bloque se prueban todos los tratamientos, o sea, los bloques están
completos.

**Aleatorización:** se hace dentro de cada bloque; por lo tanto, no se realiza de manera total
como en el diseño completamente al azar.

### 6. Diseño en cuadrado latino — DCL — `6.55.14 (1)`

**Fuentes de variabilidad:** se tienen cuatro posibles "culpables":

- Factor de tratamiento (letras latinas).
- Factor de bloque I (renglones).
- Factor de bloque II (columnas).
- Error aleatorio.

**Cuadrado:** tiene restricción adicional de que los tres factores involucrados se prueban en la
misma cantidad de niveles.

**Latino:** se utilizan letras latinas $(A, B, C, \dots, a)$ para indicar a los tratamientos o
niveles del factor de interés.

### 7. Tabla ANOVA – DCL con réplicas — `6.55.15`

La desventaja de los diseños cuadrados latinos es que tienen pocos grados de libertad del error,
por lo cual se recomienda realizar réplicas. Para ello existen tres caminos:

1. Utilizar los mismos niveles en todos los bloques.
2. Utilizar los mismos niveles en un bloque, pero diferentes niveles en el otro bloque.
3. Utilizar diferente niveles en todos los bloques.

Para cada uno de estos casos se modifica el cálculo del ANOVA.

### 8. Tabla ANOVA – DCL con réplicas – ejemplo — `6.55.15 (1)`

*Suponga que se está estudiando el efecto en la velocidad de combustión de cinco diferentes
formulaciones para un cohete propulsor, obtenidas de un lote de materia prima que alcanza para
cinco pruebas y preparadas por varios operarios, los cuales tienen habilidades y experiencias
diferentes.*

- **Tratamiento:** cinco formulaciones.
- **Bloque 1:** cinco lotes de materia prima.
- **Bloque 2:** cinco operarios.
- **Diseño de cuadrado latino 5×5:** cada formulación debe ser preparada con cada uno de los
  cinco lotes de materia prima y por cada uno de los cinco operarios.

**Formas de replicar:**

1. Utilizar el mismo lote y el mismo operario en cada réplica.
2. Utilizar el mismo lote pero con diferente operario en cada réplica (o de forma equivalente
   el mismo operario pero con diferente lote).
3. Utilizar diferentes lotes y diferentes operarios.

(Es el ejemplo del propulsor de cohete de Montgomery; la diapositiva no trae datos.)

### 9. Diseño en cuadrado grecolatino — DCGL — `6.55.17`

**Fuentes de variabilidad:** se tienen cinco posibles "culpables":

- Factor de tratamiento (letras latinas)
- Factor de bloque I (renglones)
- Factor de bloque II (columnas)
- Factor de bloque III (letras griegas)
- Error aleatorio

Nota al margen (manuscrita): *Las letras griegas pueden representar un factor de bloque o un
factor de tratamiento, siempre y cuando no tenga restricciones a la aleatorización.*

**Cuadrado:** tiene restricción adicional de que los cuatro factores involucrados se prueban en
la misma cantidad de niveles.

**Latino:** se utilizan letras latinas $(A, B, C, \dots, a)$ para indicar a los tratamientos o
niveles del factor de interés.

**Griego:** se utilizan letras griegas $(\alpha, \beta, \gamma, \dots, b)$ para indicar a los
tratamientos o niveles del tercer factor de bloque.

### 10. Tabla ANOVA – DCGL con réplicas — `6.55.17 (1)`

Si bien los diseños cuadrados grecolatinos no tienen la desventaja de los DCL en cuanto a los
grados de libertad del error, algunas veces el experimentador decide realizar réplicas, lo cual
conlleva a los cuatro casos:

1. Utilizar los mismos niveles en todos los bloques.
2. Utilizar los mismos niveles en dos bloques, pero diferentes niveles en uno de los bloques.
3. Utilizar diferentes niveles en dos bloques, pero los mismos niveles en el bloque restante.
4. Utilizar diferente niveles en todos los bloques.

Para cada uno de estos casos se modifica el calculo del ANOVA.

### 11. Efecto de bloque — `6.55.17 (2)`

El ANOVA proporciona una prueba para el efecto de los bloques, que en caso de rechazarse se
acepta que el efecto de un bloque es diferente de cero.

En la práctica se recomienda su interpretación para saber si valió la pena el esfuerzo de
controlar el factor de bloque. Si resulta significativa implica que el factor de bloque tiene
influencia sobre la variable respuesta y debe ser tomado en cuenta para mejorar su calidad; sin
embargo, si no se rechaza se tiene evidencia para no controlarlo en futuros experimentos sobre
la misma respuesta.

Otro supuesto en estos diseños, es que no existe efecto de interacción entre el factor de bloque
y el factor de tratamientos.

### 12. ¿Cuál es el modelo matemático del diseño? — Diseño en bloques completos al azar — `6.55.18`

$$Y_{ij} = \mu + \tau_i + \gamma_j + \varepsilon_{ij} \qquad \begin{cases} i = 1 \cdots a \\ j = 1 \cdots b \end{cases}$$

Cada término va en un círculo de color con una flecha a su rótulo:

- $\mu$: Media global (común a todos los tratamientos)
- $\tau_i$: Efecto del nivel o tratamiento de interés
- $\gamma_j$: Efecto del bloque
- $\varepsilon_{ij}$: Error aleatorio

### 13. ¿Cuál es el modelo matemático del diseño? — Diseño en cuadrado latino — `6.55.20`

$$Y_{ij} = \mu + \tau_i + \gamma_j + \delta_l + \varepsilon_{ijl}$$

(El lado izquierdo aparece escrito $Y_{ij}$ en la diapositiva, aunque el error lleva subíndices $ijl$.)

- $\mu$: Media global (común a todos los tratamientos)
- $\tau_i$: Efecto del nivel (letras latinas)
- $\gamma_j$: Efecto del bloque I (renglones)
- $\delta_l$: Efecto del bloque II (columnas)
- $\varepsilon_{ijl}$: Error aleatorio

### 14. ¿Cuál es el modelo matemático del diseño? — Diseño en cuadrado grecolatino — `6.55.20 (1)` y `6.55.20 (2)` (misma diapositiva, foto repetida)

$$Y_{ij} = \mu + \tau_i + \gamma_j + \delta_l + \varphi_m + \varepsilon_{ijlm}$$

(De nuevo el lado izquierdo aparece como $Y_{ij}$.)

- $\mu$: Media global (común a todos los tratamientos)
- $\tau_i$: Efecto del nivel (letras latinas)
- $\gamma_j$: Efecto del bloque I (renglones)
- $\delta_l$: Efecto del bloque II (columnas)
- $\varphi_m$: Efecto del bloque III (letras griegas)
- $\varepsilon_{ijlm}$: Error aleatorio

### 15. ¿Cuál es la hipótesis del diseño? — `6.55.20 (3)`

Recuadro **"Prueba para la media"**:

$$H_0: \mu_1 = \mu_2 = \dots = \mu_a = \mu$$
$$H_A: \mu_i \neq \mu_j \ \text{ para algún } i \neq j$$

Nota al margen (manuscrita): *Establecer las hipótesis (nula y alterna) para el factor de
interés, la cual es la misma para todos los diseños comparativos.*

También se puede escribir en forma equivalente como:

$$H_0: \tau_1 = \tau_2 = \dots = \tau_a = 0$$
$$H_A: \tau_i \neq 0 \ \text{ para algún } i$$

Donde $\tau_i$ es el efecto del tratamiento $i$ sobre la variable respuesta.

### 16. ¿Cómo debo recolectar los datos? — `6.55.24`

Recuerde iniciar estableciendo un protocolo de experimentación que garantice la estandarización
de la experimentación.

En cuanto a la aleatorización, el hecho de que existan bloques hace que no sea práctico o
incluso imposible aleatorizar en su totalidad. La imposibilidad de aleatorizar de bloque a
bloque, limita la aleatorización sólo al interior de los mismos, es decir, sólo se aleatoriza el
orden de las corridas dentro de cada bloque, lo cual evita sesgos en la comparación de los
tratamientos, pero no los impide en la comparación de los bloques.

### 17. ¿Cómo debo aleatorizar el diseño? — Diseño en bloques completos al azar — `6.55.24 (1)`

A partir del arreglo de datos en un diseño en bloques completos al azar, se aleatoriza el orden
de las corridas al interior de los bloques.

**Arreglo de datos DBCA** ($Y_{ij} \equiv$ medición que corresponde al tratamiento $i$ y al
bloque $j$):

| Trat. \ Bloque | 1 | 2 | 3 | … | b |
|---|---|---|---|---|---|
| 1 | $Y_{11}$ | $Y_{12}$ | $Y_{13}$ | … | $Y_{1b}$ |
| 2 | $Y_{21}$ | $Y_{22}$ | $Y_{23}$ | … | $Y_{2b}$ |
| 3 | $Y_{31}$ | $Y_{32}$ | $Y_{33}$ | … | $Y_{3b}$ |
| ⋮ | ⋮ | ⋮ | ⋮ | … | ⋮ |
| a | $Y_{a1}$ | $Y_{a2}$ | $Y_{a3}$ | … | $Y_{ab}$ |

→ **Ejemplo** (orden de las corridas ya aleatorizado dentro de cada bloque; 3 tratamientos, 4
bloques):

| Bloque 1 | Bloque 2 | Bloque 3 | Bloque 4 |
|---|---|---|---|
| $Y_{31}$ | $Y_{12}$ | $Y_{13}$ | $Y_{24}$ |
| $Y_{11}$ | $Y_{32}$ | $Y_{23}$ | $Y_{34}$ |
| $Y_{21}$ | $Y_{22}$ | $Y_{33}$ | $Y_{14}$ |

Flechas verdes rotuladas *Orden de las corridas*: se empieza en $Y_{31}$ (encerrado en un
círculo), se baja por el bloque 1, se pasa al bloque 2 y se baja, etc. (se corre bloque por
bloque).

### 18. ¿Cómo debo aleatorizar el diseño? — Diseño en cuadrado latino (1/3) — `6.55.24 (2)` y `6.55.25` (misma diapositiva, foto repetida)

No cualquier arreglo de letras latinas en forma de cuadrado es un cuadrado latino, cada letra
debe aparecer sólo una vez en cada renglón y en cada columna.

Es más fácil si se construye un cuadrado latino estándar, en el cual la primera columna y el
primer renglón tienen las letras en orden alfabético.

**Cuadrados latino estándar** (cuatro cuadrados 4×4):

| Cuadrado 1 (rojo, poco legible) | Cuadrado 2 (amarillo) | Cuadrado 3 (verde) | Cuadrado 4 (morado) |
|---|---|---|---|
| A B C D | A B C D | A B C D | A B C D |
| B C D A | B A D C | B D A C | B A D C |
| C D A B | C D B A | C A D B | C D A B |
| D A B C | D C A B | D C B A | D C B A |

Después se aleatorizan los renglones y luego las columnas (o viceversa), obteniendo el cuadrado
latino aleatorizado.

### 19. ¿Cómo debo aleatorizar el diseño? — Diseño en cuadrado latino (2/3) — `6.55.25 (1)`

**Cuadrado latino aleatorizado:**

| | | | |
|---|---|---|---|
| C | B | A | D |
| B | A | D | C |
| A | D | C | B |
| D | C | B | A |

**+ Bloques 1 y 2** (tabla vacía con B 1 en renglones 1–4 y B 2 en columnas 1–4)

→ **Ejemplo** (resultado): cada celda muestra la medición y la letra del tratamiento.

| B 1 \ B 2 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|
| 1 | $Y_{11C}$ (C) | $Y_{12B}$ (B) | $Y_{13A}$ (A) | $Y_{14D}$ (D) |
| 2 | $Y_{21B}$ (B) | $Y_{22A}$ (A) | $Y_{23D}$ (D) | $Y_{24C}$ (C) |
| 3 | $Y_{31A}$ (A) | $Y_{32D}$ (D) | $Y_{33C}$ (C) | $Y_{34B}$ (B) |
| 4 | $Y_{41D}$ (D) | $Y_{42C}$ (C) | $Y_{43B}$ (B) | $Y_{44A}$ (A) |

$Y_{ijl} \equiv$ Medición que corresponde al tratamiento $i$, en el nivel $j$ del factor renglón
y en el nivel $l$ del factor columna.

Finalmente se asigna el cuadrado latino aleatorizado (tratamientos) a los bloques (1 y 2).

### 20. ¿Cómo debo aleatorizar el diseño? — Diseño en cuadrado latino (3/3) — `6.55.25 (2)`

A la hora de correr el experimento se puede correr por columna o por renglón según convenga. Lo
que no es correcto es hacer todas las pruebas de un tratamiento, luego todas las de otro, y así
sucesivamente, puesto que se puede introducir ruido adicional debido a factores no controlables
que cambian con el tiempo.

Se repite la tabla B 1 × B 2 de la diapositiva 19 (solo las $Y$), con $Y_{11C}$ encerrada en un
círculo y flechas verdes que bajan por la columna 1 y siguen por la columna 2.
Leyenda: *Orden de las corridas por columnas (también puede ser por renglones)*.

### 21. ¿Cómo debo aleatorizar el diseño? — Diseño en cuadrado grecolatino (1/3) — `6.55.25 (3)`

Se deben construir el cuadrado latino estándar y el cuadrado griego estándar. Posteriormente
estos cuadrados se unen cuidando que cada par de letras aparezca sólo una vez en todo el
arreglo. Después deben ser aleatorizados por renglones y luego por columnas (o viceversa),
obteniendo el cuadrado greco-latino aleatorizado.

**Cuadrados latino estándar:** los mismos cuatro de la diapositiva 18.

**Cuadrados griego estándar:**

| Cuadrado 1 (rojo, poco legible) | Cuadrado 2 (amarillo) | Cuadrado 3 (verde) | Cuadrado 4 (morado, poco legible) |
|---|---|---|---|
| α β γ δ | α β γ δ | α β γ δ | α β γ δ |
| β γ δ α | β α δ γ | β δ α γ | β α δ γ |
| γ δ α β | γ δ β α | γ α δ β | γ δ α β |
| δ α β γ | δ γ α β | δ γ β α | δ γ β α |

### 22. ¿Cómo debo aleatorizar el diseño? — Diseño en cuadrado grecolatino (2/3) — `6.55.26`

**Cuadrado greco-latino aleatorizado:**

| | | | |
|---|---|---|---|
| Cβ | Bγ | Dδ | Aα |
| Bα | Cδ | Aγ | Dβ |
| Aδ | Dα | Bβ | Cγ |
| Dγ | Aβ | Cα | Bδ |

**+ Bloques 1 y 2** (tabla vacía B 1 × B 2) → **Ejemplo:**

| B 1 \ B 2 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|
| 1 | $Y_{11C\beta}$ (Cβ) | $Y_{12B\gamma}$ (Bγ) | $Y_{13D\delta}$ (Dδ) | $Y_{14A\alpha}$ (Aα) |
| 2 | $Y_{21B\alpha}$ (Bα) | $Y_{22C\delta}$ (Cδ) | $Y_{23A\gamma}$ (Aγ) | $Y_{24D\beta}$ (Dβ) |
| 3 | $Y_{31A\delta}$ (Aδ) | $Y_{32D\alpha}$ (Dα) | $Y_{33B\beta}$ (Bβ) | $Y_{34C\gamma}$ (Cγ) |
| 4 | $Y_{41D\gamma}$ (Dγ) | $Y_{42A\beta}$ (Aβ) | $Y_{43C\alpha}$ (Cα) | $Y_{44B\delta}$ (Bδ) |

$Y_{ijlm} \equiv$ Medición que corresponde al tratamiento $i$, en el nivel $j$ del factor
renglón, en el nivel $l$ del factor columna y en la $m$-ésima letra griega.

Finalmente se asigna el cuadrado greco-latino aleatorizado a los bloques (1 y 2).

### 23. ¿Cómo debo aleatorizar el diseño? — Diseño en cuadrado grecolatino (3/3) — `6.55.26 (1)`

Revise que cada letra (latinas y griegas) aparezca sólo una vez en cada renglón y en cada
columna y que cada par de letras aparezca sólo una vez en todo el arreglo. A la hora de correr
el experimento se puede correr por columna o por renglón según convenga. Lo que no es correcto
es hacer todas las pruebas de un tratamiento de forma consecutiva.

Nota al margen (manuscrita): *Existen cuadrados grecolatinos para todo $p \geq 3$ excepto para
$p = 6$.*

Se repite la tabla B 1 × B 2 de la diapositiva 22 (solo las $Y$), con $Y_{11C\beta}$ en un
círculo y flechas verdes por columnas. Leyenda: *Orden de las corridas por columnas (también
puede ser por renglones)*.

### 24. ¿Cómo debo analizar los datos recolectados? — `6.55.26 (2)`

1. Calcular el ANOVA correspondiente usando los datos.
2. Estimar el valor crítico con las tablas de distribución o el valor-p con *software*
   estadístico.
3. Aplicar el criterio de rechazo apropiado.
4. Verificar los supuestos del modelo.
5. Si se rechazó la hipótesis nula, realizar comparación de medias.
6. Informar la conclusión en términos del problema establecido por el investigador.

(Ilustración: tres engranajes de colores.)

### 25. ¿Cómo elijo el ANOVA apropiado? — `6.55.26 (3)`

Árbol de decisión que parte de **"1 Factor de interés +"**:

| Factores de bloque | Réplica | Niveles de los bloques entre réplicas | ANOVA |
|---|---|---|---|
| 1 factor de bloque | — | — | 1. DBCA |
| 2 factores de bloque | Sin réplica | — | 2. DCL |
| 2 factores de bloque | Con réplica | Todos los bloques con niveles =s | 3. DCL – Caso 1 |
| 2 factores de bloque | Con réplica | Un bloque con niveles =s y un bloque con niveles ≠s | 4. DCL – Caso 2 |
| 2 factores de bloque | Con réplica | Todos los bloques con niveles ≠s | 5. DCL – Caso 3 |
| 3 factores de bloque * | Sin réplica | — | 6. DCGL |
| 3 factores de bloque * | Con réplica | Todos los bloques con niveles =s | 7. DCGL – Caso 1 |
| 3 factores de bloque * | Con réplica | Dos bloques con niveles =s y un bloque con niveles ≠s | 8. DCGL – Caso 2 |
| 3 factores de bloque * | Con réplica | Un bloque con niveles =s y dos bloques con niveles ≠s | 9. DCGL – Caso 3 |
| 3 factores de bloque * | Con réplica | Todos los bloques con niveles ≠s | 10. DCGL – Caso 4 |

\* *También pueden ser 2 factores de tratamiento y 2 factores de bloque, siempre y cuando no
tengan restricciones de aleatorización.*

> **Nota sobre las tablas ANOVA (diapositivas 26–35):** columnas SV (fuente de variación), SS,
> DF, MS, $F_0$. En las fotos los puntos de los subíndices de los totales ($y_{i..}$, $y_{.j.}$,
> etc.) son muy pequeños; la **posición** del índice se transcribió según lo que se alcanza a
> ver y el patrón de la tabla, pero el número exacto de puntos es **poco legible**. Ojo: en las
> tablas ANOVA el tratamiento lleva el índice $j$ y los renglones el índice $i$, al revés que en
> los modelos de las diapositivas 12–14.

### 26. 1. Tabla ANOVA - DBCA — `6.55.27`

| SV | SS | DF | MS | $F_0$ |
|---|---|---|---|---|
| Trat. | $SS_{Trat} = \sum_{i=1}^{a} \frac{y_{i.}^2}{b} - \frac{y_{..}^2}{N}$ | $a-1$ | $MS_{Trat}$ | $\frac{MS_{Trat}}{MS_E}$ |
| Bloque | $SS_{Bloq} = \sum_{j=1}^{b} \frac{y_{.j}^2}{a} - \frac{y_{..}^2}{N}$ | $b-1$ | $MS_{Bloq}$ | $\frac{MS_{Bloq}}{MS_E}$ |
| Error | $SS_E = SS_T - SS_{Trat} - SS_{Bloq}$ | $(a-1)(b-1)$ | $MS_E$ | |
| Total | $SS_T = \sum_{j=1}^{b}\sum_{i=1}^{a} y_{ij}^2 - \frac{y_{..}^2}{N}$ | $N-1$ | | |

Nota al pie (manuscrita): *Ésta no es una prueba F exacta, sino aproximada, por la restricción
de aleatorización (sólo se aleatoriza dentro del bloque).* (La fila de bloque está sombreada.)

### 27. 2. Tabla ANOVA - DCL — `6.55.27 (1)`

| SV | SS | DF | MS | $F_0$ |
|---|---|---|---|---|
| Tratamiento (letras latinas) | $SS_{TRAT} = \frac{1}{p}\sum_{j=1}^{p} y_{.j.}^2 - \frac{y_{...}^2}{N}$ | $p-1$ | $MS_{Trat}$ | $\frac{MS_{Trat}}{MS_E}$ |
| Bloque 1 (renglones) | $SS_{Bloq1} = \frac{1}{p}\sum_{i=1}^{p} y_{i..}^2 - \frac{y_{...}^2}{N}$ | $p-1$ | $MS_{Bloq1}$ | $\frac{MS_{Bloq1}}{MS_E}$ |
| Bloque 2 (columnas) | $SS_{Bloq2} = \frac{1}{p}\sum_{k=1}^{p} y_{..k}^2 - \frac{y_{...}^2}{N}$ | $p-1$ | $MS_{Bloq2}$ | $\frac{MS_{Bloq2}}{MS_E}$ |
| Error | $SS_E = \text{sustracción}$ | $(p-2)(p-1)$ | $MS_E$ | |
| Total | $SS_T = \sum\sum\sum y_{ijk}^2 - \frac{y_{...}^2}{N}$ | $p^2-1$ | | |

### 28. 3. Tabla ANOVA - DCL con réplicas – Caso 1 — `6.55.27 (2)`

| SV | SS | DF | MS | $F_0$ |
|---|---|---|---|---|
| Trat. (letras latinas) | $SS_{TRAT} = \frac{1}{np}\sum_{j=1}^{p} y_{.j..}^2 - \frac{y_{....}^2}{N}$ | $p-1$ | $MS_{Trat}$ | $\frac{MS_{Trat}}{MS_E}$ |
| Bloque 1 (renglones) | $SS_{Bloq1} = \frac{1}{np}\sum_{i=1}^{p} y_{i...}^2 - \frac{y_{....}^2}{N}$ | $p-1$ | $MS_{Bloq1}$ | $\frac{MS_{Bloq1}}{MS_E}$ |
| Bloque 2 (columnas) | $SS_{Bloq2} = \frac{1}{np}\sum_{k=1}^{p} y_{..k.}^2 - \frac{y_{....}^2}{N}$ | $p-1$ | $MS_{Bloq2}$ | $\frac{MS_{Bloq2}}{MS_E}$ |
| Réplicas | $SS_{Réplic} = \frac{1}{p^2}\sum_{l=1}^{n} y_{...l}^2 - \frac{y_{....}^2}{N}$ | $n-1$ | $MS_{Réplic}$ | $\frac{MS_{Réplic}}{MS_E}$ |
| Error | $SS_E = \text{sustracción}$ | $(p-1)[n(p+1)-3]$ | $MS_E$ | |
| Total | $SS_T = \sum\sum\sum\sum y_{ijkl}^2 - \frac{y_{....}^2}{N}$ | $np^2-1$ | | |

### 29. 4. Tabla ANOVA - DCL con réplicas – Caso 2 — `6.55.27 (3)`

| SV | SS | DF | MS | $F_0$ |
|---|---|---|---|---|
| Trat. (letras latinas) | $SS_{TRAT} = \frac{1}{np}\sum_{j=1}^{p} y_{.j..}^2 - \frac{y_{....}^2}{N}$ | $p-1$ | $MS_{Trat}$ | $\frac{MS_{Trat}}{MS_E}$ |
| Bloque 1 (renglones) | $SS_{Bloq1} = \frac{1}{p}\sum_{l=1}^{n}\sum_{i=1}^{p} y_{i..l}^2 - \sum_{l=1}^{n}\frac{y_{...l}^2}{p^2}$ | $n(p-1)$ | $MS_{Bloq1}$ | $\frac{MS_{Bloq1}}{MS_E}$ |
| Bloque 2 (columnas) | $SS_{Bloq2} = \frac{1}{np}\sum_{k=1}^{p} y_{..k.}^2 - \frac{y_{....}^2}{N}$ | $p-1$ | $MS_{Bloq2}$ | $\frac{MS_{Bloq2}}{MS_E}$ |
| Réplicas | $SS_{Réplic} = \frac{1}{p^2}\sum_{l=1}^{n} y_{...l}^2 - \frac{y_{....}^2}{N}$ | $n-1$ | $MS_{Réplic}$ | $\frac{MS_{Réplic}}{MS_E}$ |
| Error | $SS_E = \text{sustracción}$ | $(p-1)(np-1)$ | $MS_E$ | |
| Total | $SS_T = \sum\sum\sum\sum y_{ijkl}^2 - \frac{y_{....}^2}{N}$ | $np^2-1$ | | |

### 30. 5. Tabla ANOVA - DCL con réplicas – Caso 3 — `6.55.28`

| SV | SS | DF | MS | $F_0$ |
|---|---|---|---|---|
| Trat. (letras latinas) | $SS_{TRAT} = \frac{1}{np}\sum_{j=1}^{p} y_{.j..}^2 - \frac{y_{....}^2}{N}$ | $p-1$ | $MS_{Trat}$ | $\frac{MS_{Trat}}{MS_E}$ |
| Bloque 1 (renglones) | $SS_{Bloq1} = \frac{1}{p}\sum_{l=1}^{n}\sum_{i=1}^{p} y_{i..l}^2 - \sum_{l=1}^{n}\frac{y_{...l}^2}{p^2}$ | $n(p-1)$ | $MS_{Bloq1}$ | $\frac{MS_{Bloq1}}{MS_E}$ |
| Bloque 2 (columnas) | $SS_{Bloq2} = \frac{1}{p}\sum_{l=1}^{n}\sum_{k=1}^{p} y_{..kl}^2 - \sum_{l=1}^{n}\frac{y_{...l}^2}{p^2}$ | $n(p-1)$ | $MS_{Bloq2}$ | $\frac{MS_{Bloq2}}{MS_E}$ |
| Réplicas | $SS_{Réplic} = \frac{1}{p^2}\sum_{l=1}^{n} y_{...l}^2 - \frac{y_{....}^2}{N}$ | $n-1$ | $MS_{Réplic}$ | $\frac{MS_{Réplic}}{MS_E}$ |
| Error | $SS_E = \text{sustracción}$ | $(p-1)[n(p-1)-1]$ | $MS_E$ | |
| Total | $SS_T = \sum\sum\sum\sum y_{ijkl}^2 - \frac{y_{....}^2}{N}$ | $np^2-1$ | | |

### 31. 6. Tabla ANOVA - DCGL — `6.55.28 (1)`

| SV | SS | DF | MS | $F_0$ |
|---|---|---|---|---|
| Tratamiento (letras latinas) | $SS_{TRAT} = \frac{1}{p}\sum_{j=1}^{p} y_{.j..}^2 - \frac{y_{....}^2}{N}$ | $p-1$ | $MS_{Trat}$ | $\frac{MS_{Trat}}{MS_E}$ |
| Bloque 1 (renglones) | $SS_{Bloq1} = \frac{1}{p}\sum_{i=1}^{p} y_{i...}^2 - \frac{y_{....}^2}{N}$ | $p-1$ | $MS_{Bloq1}$ | $\frac{MS_{Bloq1}}{MS_E}$ |
| Bloque 2 (columnas) | $SS_{Bloq2} = \frac{1}{p}\sum_{l=1}^{p} y_{...l}^2 - \frac{y_{....}^2}{N}$ | $p-1$ | $MS_{Bloq2}$ | $\frac{MS_{Bloq2}}{MS_E}$ |
| Bloque 3 (letras griegas) | $SS_{Bloq3} = \frac{1}{p}\sum_{k=1}^{p} y_{..k.}^2 - \frac{y_{....}^2}{N}$ | $p-1$ | $MS_{Bloq3}$ | $\frac{MS_{Bloq3}}{MS_E}$ |
| Error | $SS_E = \text{sustracción}$ | $(p-3)(p-1)$ | $MS_E$ | |
| Total | $SS_T = \sum\sum\sum\sum y_{ijkl}^2 - \frac{y_{....}^2}{N}$ | $p^2-1$ | | |

### 32. 7. Tabla ANOVA - DCGL con réplicas – Caso 1 — `6.55.29`

| SV | SS | DF | MS | $F_0$ |
|---|---|---|---|---|
| Tratamiento (letras latinas) | $SS_{TRAT} = \frac{1}{np}\sum_{j=1}^{p} y_{.j...}^2 - \frac{y_{.....}^2}{N}$ | $p-1$ | $MS_{Trat}$ | $\frac{MS_{Trat}}{MS_E}$ |
| Bloque 1 (renglones) | $SS_{Bloq1} = \frac{1}{np}\sum_{i=1}^{p} y_{i....}^2 - \frac{y_{.....}^2}{N}$ | $p-1$ | $MS_{Bloq1}$ | $\frac{MS_{Bloq1}}{MS_E}$ |
| Bloque 2 (columnas) | $SS_{Bloq2} = \frac{1}{np}\sum_{l=1}^{p} y_{...l.}^2 - \frac{y_{.....}^2}{N}$ | $p-1$ | $MS_{Bloq2}$ | $\frac{MS_{Bloq2}}{MS_E}$ |
| Bloque 3 (letras griegas) | $SS_{Bloq3} = \frac{1}{np}\sum_{k=1}^{p} y_{..k..}^2 - \frac{y_{.....}^2}{N}$ | $p-1$ | $MS_{Bloq3}$ | $\frac{MS_{Bloq3}}{MS_E}$ |
| Réplicas | $SS_{Réplic} = \frac{1}{p^2}\sum_{m=1}^{n} y_{....m}^2 - \frac{y_{.....}^2}{N}$ | $n-1$ | $MS_{Réplic}$ | $\frac{MS_{Réplic}}{MS_E}$ |
| Error | $SS_E = \text{sustracción}$ | $(p-1)[n(p+1)-4]$ | $MS_E$ | |
| Total | $SS_T = \sum\sum\sum\sum\sum y_{ijklm}^2 - \frac{y_{.....}^2}{N}$ | $np^2-1$ | | |

### 33. 8. Tabla ANOVA - DCGL con réplicas – Caso 2 — `6.55.29 (1)`

Subtítulo (manuscrito): *Bloque 1 con diferentes niveles*

| SV | SS | DF | MS | $F_0$ |
|---|---|---|---|---|
| Tratamiento (letras latinas) | $SS_{TRAT} = \frac{1}{np}\sum_{j=1}^{p} y_{.j...}^2 - \frac{y_{.....}^2}{N}$ | $p-1$ | $MS_{Trat}$ | $\frac{MS_{Trat}}{MS_E}$ |
| Bloque 1 (renglones) | $SS_{Bloq1} = \frac{1}{p}\sum_{m=1}^{n}\sum_{i=1}^{p} y_{i...m}^2 - \sum_{m=1}^{p}\frac{y_{....m}^2}{p^2}$ | $n(p-1)$ | $MS_{Bloq1}$ | $\frac{MS_{Bloq1}}{MS_E}$ |
| Bloque 2 (columnas) | $SS_{Bloq2} = \frac{1}{np}\sum_{l=1}^{p} y_{...l.}^2 - \frac{y_{.....}^2}{N}$ | $p-1$ | $MS_{Bloq2}$ | $\frac{MS_{Bloq2}}{MS_E}$ |
| Bloque 3 (letras griegas) | $SS_{Bloq3} = \frac{1}{np}\sum_{k=1}^{p} y_{..k..}^2 - \frac{y_{.....}^2}{N}$ | $p-1$ | $MS_{Bloq3}$ | $\frac{MS_{Bloq3}}{MS_E}$ |
| Réplicas | $SS_{Réplic} = \frac{1}{p^2}\sum_{m=1}^{n} y_{....m}^2 - \frac{y_{.....}^2}{N}$ | $n-1$ | $MS_{Réplic}$ | $\frac{MS_{Réplic}}{MS_E}$ |
| Error | $SS_E = \text{sustracción}$ | $(p-1)(np-1)$ | $MS_E$ | |
| Total | $SS_T = \sum\sum\sum\sum\sum y_{ijklm}^2 - \frac{y_{.....}^2}{N}$ | $np^2-1$ | | |

(En la segunda sumatoria de los bloques con niveles diferentes el límite superior se lee $p$,
con índice $m=1$; por coherencia con el caso DCL debería ser $n$. Se transcribe como se ve.)

### 34. 9. Tabla ANOVA - DCGL con réplicas – Caso 3 — `6.55.30 (1)`

Subtítulo (manuscrito): *Bloque 1 y Bloque 2 con diferentes niveles*

| SV | SS | DF | MS | $F_0$ |
|---|---|---|---|---|
| Tratamiento (letras latinas) | $SS_{TRAT} = \frac{1}{np}\sum_{j=1}^{p} y_{.j...}^2 - \frac{y_{.....}^2}{N}$ | $p-1$ | $MS_{Trat}$ | $\frac{MS_{Trat}}{MS_E}$ |
| Bloque 1 (renglones) | $SS_{Bloq1} = \frac{1}{p}\sum_{m=1}^{n}\sum_{i=1}^{p} y_{i...m}^2 - \sum_{m=1}^{p}\frac{y_{....m}^2}{p^2}$ | $n(p-1)$ | $MS_{Bloq1}$ | $\frac{MS_{Bloq1}}{MS_E}$ |
| Bloque 2 (columnas) | $SS_{Bloq2} = \frac{1}{p}\sum_{m=1}^{n}\sum_{l=1}^{p} y_{...lm}^2 - \sum_{m=1}^{p}\frac{y_{....m}^2}{p^2}$ | $n(p-1)$ | $MS_{Bloq2}$ | $\frac{MS_{Bloq2}}{MS_E}$ |
| Bloque 3 (letras griegas) | $SS_{Bloq3} = \frac{1}{np}\sum_{k=1}^{p} y_{..k..}^2 - \frac{y_{.....}^2}{N}$ | $p-1$ | $MS_{Bloq3}$ | $\frac{MS_{Bloq3}}{MS_E}$ |
| Réplicas | $SS_{Réplic} = \frac{1}{p^2}\sum_{m=1}^{n} y_{....m}^2 - \frac{y_{.....}^2}{N}$ | $n-1$ | $MS_{Réplic}$ | $\frac{MS_{Réplic}}{MS_E}$ |
| Error | $SS_E = \text{sustracción}$ | $(p-1)(np-1)$ | $MS_E$ | |
| Total | $SS_T = \sum\sum\sum\sum\sum y_{ijklm}^2 - \frac{y_{.....}^2}{N}$ | $np^2-1$ | | |

(Los g.l. del error se leen $(p-1)(np-1)$, igual que en el Caso 2; así aparece en la
diapositiva, aunque no cuadra con la resta de los g.l. — verificar contra Montgomery antes de
usarlo.)

### 35. 10. Tabla ANOVA - DCGL con réplicas – Caso 4 — `6.55.30`

Subtítulo (manuscrito): *Bloque 1, Bloque 2 y Bloque 3 con diferentes niveles*

| SV | SS | DF | MS | $F_0$ |
|---|---|---|---|---|
| Tratamiento (letras latinas) | $SS_{TRAT} = \frac{1}{np}\sum_{j=1}^{p} y_{.j...}^2 - \frac{y_{.....}^2}{N}$ | $p-1$ | $MS_{Trat}$ | $\frac{MS_{Trat}}{MS_E}$ |
| Bloque 1 (renglones) | $SS_{Bloq1} = \frac{1}{p}\sum_{m=1}^{n}\sum_{i=1}^{p} y_{i...m}^2 - \sum_{m=1}^{p}\frac{y_{....m}^2}{p^2}$ | $n(p-1)$ | $MS_{Bloq1}$ | $\frac{MS_{Bloq1}}{MS_E}$ |
| Bloque 2 (columnas) | $SS_{Bloq2} = \frac{1}{p}\sum_{m=1}^{n}\sum_{l=1}^{p} y_{...lm}^2 - \sum_{m=1}^{p}\frac{y_{....m}^2}{p^2}$ | $n(p-1)$ | $MS_{Bloq2}$ | $\frac{MS_{Bloq2}}{MS_E}$ |
| Bloque 3 (letras griegas) | $SS_{Bloq3} = \frac{1}{p}\sum_{m=1}^{n}\sum_{k=1}^{p} y_{..k.m}^2 - \sum_{m=1}^{p}\frac{y_{....m}^2}{p^2}$ | $n(p-1)$ | $MS_{Bloq3}$ | $\frac{MS_{Bloq3}}{MS_E}$ |
| Réplicas | $SS_{Réplic} = \frac{1}{p^2}\sum_{m=1}^{n} y_{....m}^2 - \frac{y_{.....}^2}{N}$ | $n-1$ | $MS_{Réplic}$ | $\frac{MS_{Réplic}}{MS_E}$ |
| Error | $SS_E = \text{sustracción}$ | Sustracción | $MS_E$ | |
| Total | $SS_T = \sum\sum\sum\sum\sum y_{ijklm}^2 - \frac{y_{.....}^2}{N}$ | $np^2-1$ | | |

### 36. Comparaciones o pruebas de rango múltiples — `6.55.31`

Cuando se rechaza $H_0$ con la prueba de ANOVA, se confirma que existe diferencia en las medias
de los tratamientos, pero no sabemos cuáles tratamientos son diferentes. Para averiguarlo:

**Comparación de pares:**

| Método | Estadístico |
|---|---|
| Prueba de Tukey | $T_\alpha = q_\alpha(a, l)\sqrt{\dfrac{MS_E}{n}}$ |
| Método de Fisher (LSD) | $LSD = t_{\alpha/2,\,l}\sqrt{\dfrac{2MS_E}{n}}$ |
| Método de Duncan | $R_p = r_\alpha(p, l)\sqrt{\dfrac{MS_E}{n}}$ |
| Método de Dunnet | $D_\alpha = D_\alpha(a-1, l)\sqrt{\dfrac{2MS_E}{n}}$ |

Recuadro inferior izquierdo — valor de $n$ que se usa en cada diseño: **DBCA → $b$**,
**DCL → $p$**, **DCGL → $p$**. (La diapositiva no define $l$; por el contexto son los grados de
libertad del error.)

### 37. ¿Qué debemos verificar sobre el modelo? — `6.55.31 (1)`

La validez de los resultados obtenidos con un análisis de varianza depende de que los supuestos
del modelo se cumplan.

Para comprobar estos supuestos se utilizan los residuos del modelo $e_{ij}$ los cuales se
estiman como la diferencia entre el valor de la respuesta observada y el valor de la respuesta
estimada con el modelo, de otra forma se podría expresar como:

- **DBCA:** $e_{ij} = Y_{ij} - \hat{Y}_{ij} = Y_{ij} - \bar{Y}_{i.} - \bar{Y}_{.j} + \bar{Y}_{..}$
- **DCL:** $e_{ijk} = Y_{ijk} - \hat{Y}_{ijk} = Y_{ijk} - \bar{Y}_{i..} - \bar{Y}_{.j.} - \bar{Y}_{..k} + 2\bar{Y}_{...}$
- **DCGL:** $e_{ijkl} = Y_{ijkl} - \hat{Y}_{ijkl} = Y_{ijkl} - \bar{Y}_{i...} - \bar{Y}_{.j..} - \bar{Y}_{..k.} - \bar{Y}_{...l} + 3\bar{Y}_{....}$

### 38. Supuestos sobre los errores del modelo — `6.55.32`

Cuatro recuadros de color:

1. El error sigue una distribución normal
2. La varianza es constante
3. Las mediciones son independientes entre sí
4. La media de los errores es cero

### 39. ¿Cómo comprobar los supuestos del modelo? — `6.55.32 (1)`

Para comprobar los supuestos se pueden utilizar pruebas gráficas y/o analíticas.

| Tipo | Supuesto | Prueba |
|---|---|---|
| Pruebas gráficas | Normalidad | Probabilidad Normal; Histograma de Residuos |
| Pruebas gráficas | Varianza constante | Predichos vs Residuos; Niveles del Factor vs Residuos |
| Pruebas gráficas | Independencia | Residuos vs Tiempo |
| Pruebas analíticas | Normalidad | Shapiro-Wilks; Kolmogorov-Smirnov; Chi-Cuadrado |
| Pruebas analíticas | Varianza constante | Bartlett; Levene |
| Pruebas analíticas | Independencia | Durbin-Watson |

---

## Parte B — Índice de imágenes

| Archivo (`WhatsApp Image 2026-10-03 at … PM.jpeg`) | Diapositiva |
|---|---|
| `6.55.11` | 1 |
| `6.55.12` | 2 |
| `6.55.12 (1)` | 3 |
| `6.55.12 (2)` | 4 |
| `6.55.14` | 5 |
| `6.55.14 (1)` | 6 |
| `6.55.15` | 7 |
| `6.55.15 (1)` | 8 |
| `6.55.17` | 9 |
| `6.55.17 (1)` | 10 |
| `6.55.17 (2)` | 11 |
| `6.55.18` | 12 |
| `6.55.20` | 13 |
| `6.55.20 (1)`, `6.55.20 (2)` | 14 (repetida) |
| `6.55.20 (3)` | 15 |
| `6.55.24` | 16 |
| `6.55.24 (1)` | 17 |
| `6.55.24 (2)`, `6.55.25` | 18 (repetida) |
| `6.55.25 (1)` | 19 |
| `6.55.25 (2)` | 20 |
| `6.55.25 (3)` | 21 |
| `6.55.26` | 22 |
| `6.55.26 (1)` | 23 |
| `6.55.26 (2)` | 24 |
| `6.55.26 (3)` | 25 |
| `6.55.27` | 26 |
| `6.55.27 (1)` | 27 |
| `6.55.27 (2)` | 28 |
| `6.55.27 (3)` | 29 |
| `6.55.28` | 30 |
| `6.55.28 (1)` | 31 |
| `6.55.29` | 32 |
| `6.55.29 (1)` | 33 |
| `6.55.30 (1)` | 34 |
| `6.55.30` | 35 |
| `6.55.31` | 36 |
| `6.55.31 (1)` | 37 |
| `6.55.32` | 38 |
| `6.55.32 (1)` | 39 |

---

## Parte C — Estructura didáctica de la profesora

Lo que sigue se deduce solo de las 39 diapositivas fotografiadas.

### 1. Secuencia de bloques

La presentación **no** va diseño por diseño (todo DBCA, luego todo DCL…). Va **pregunta por
pregunta**, y dentro de cada pregunta recorre los tres diseños en paralelo, siempre en el mismo
orden (DBCA → DCL → DCGL, de menor a mayor complejidad):

| # | Bloque | Diapositivas | Cant. | Contenido |
|---|---|---|---|---|
| 1 | Motivación / para qué sirve | 1–3 | 3 | Factor de ruido (3 casos → aleatorizar / ANCOVA / bloquear), definición de factor de bloque, por qué no se puede aleatorizar todo |
| 2 | Mapa de la familia de diseños | 4 | 1 | Esquema: 1, 2 o 3 factores de bloque → DBCA, DCL, DCGL |
| 3 | Definición y nomenclatura de cada diseño | 5, 6, 9 | 3 | "Fuentes de variabilidad" (los "culpables") + significado de cada palabra del nombre (Completo, Cuadrado, Latino, Griego) |
| 4 | Variantes (réplicas) | 7, 8, 10 | 3 | Por qué replicar, casos posibles, ejemplo verbal (cohete propulsor) |
| 5 | Interpretación del efecto de bloque | 11 | 1 | Para qué sirve probar el bloque; supuesto de no interacción |
| 6 | "¿Cuál es el modelo matemático del diseño?" | 12–14 | 3 | Un modelo por diseño, cada término rotulado |
| 7 | "¿Cuál es la hipótesis del diseño?" | 15 | 1 | Una sola diapositiva, común a los tres diseños |
| 8 | "¿Cómo debo recolectar los datos?" / "¿Cómo debo aleatorizar el diseño?" (protocolo experimental) | 16–23 | 8 | Protocolo + aleatorización paso a paso: 1 para DBCA, 3 para DCL, 3 para DCGL |
| 9 | "¿Cómo debo analizar los datos recolectados?" | 24 | 1 | Procedimiento en 6 pasos |
| 10 | "¿Cómo elijo el ANOVA apropiado?" | 25 | 1 | Árbol de decisión que numera las 10 tablas |
| 11 | Tablas ANOVA con fórmulas | 26–35 | 10 | Una tabla por diapositiva, numeradas 1–10 según el árbol |
| 12 | Comparaciones múltiples | 36 | 1 | Tukey, LSD, Duncan, Dunnett con sus fórmulas |
| 13 | Supuestos del modelo | 37–39 | 3 | Residuos por diseño, los 4 supuestos, pruebas gráficas y analíticas |

Peso relativo: aleatorización/protocolo (8) y tablas ANOVA (10) ocupan casi la mitad de las
diapositivas; los ejemplos numéricos y el software no aparecen en las fotos.

### 2. Cómo redacta las hipótesis

- Dos formas equivalentes, siempre juntas: en medias ($H_0: \mu_1 = \mu_2 = \dots = \mu_a = \mu$
  vs. $H_A: \mu_i \neq \mu_j$ para algún $i \neq j$) y en efectos
  ($H_0: \tau_1 = \dots = \tau_a = 0$ vs. $H_A: \tau_i \neq 0$ para algún $i$).
- Usa $H_A$ (no $H_1$) para la alterna.
- Solo plantea la hipótesis del **factor de interés** y aclara que "es la misma para todos los
  diseños comparativos". La prueba del bloque se comenta aparte, en texto (diapositiva 11).
- Cierra definiendo el símbolo: "Donde $\tau_i$ es el efecto del tratamiento $i$ sobre la
  variable respuesta".

### 3. Cómo redacta las conclusiones

No hay diapositiva de conclusiones de un ejemplo. La pauta está en el paso 6 del procedimiento:
"Informar la conclusión en términos del problema establecido por el investigador", y en la
lectura práctica del bloque (si es significativo valió la pena controlarlo; si no, hay evidencia
para no controlarlo en futuros experimentos).

### 4. Notación

- Respuesta $Y$ en mayúscula en modelos y arreglos; $y$ minúscula con notación de puntos para
  totales en las tablas ANOVA; $\bar{Y}$ con puntos para medias en los residuos; residuo $e$.
- Modelo de efectos: $\mu$ (media global), $\tau_i$ (tratamiento), $\gamma_j$ (bloque I /
  renglones), $\delta_l$ (bloque II / columnas), $\varphi_m$ (bloque III / letras griegas),
  $\varepsilon$ (error).
- $a$ = niveles del tratamiento, $b$ = bloques (DBCA); $p$ = tamaño del cuadrado; $n$ =
  réplicas; $N$ = total de observaciones.
- Tablas ANOVA con encabezados en inglés abreviado: **SV, SS, DF, MS, $F_0$**; subíndices en
  español abreviado ($SS_{Trat}$, $SS_{Bloq1}$, $SS_{Réplic}$, $SS_E$, $SS_T$). El error se
  obtiene por "sustracción". No hay columna de valor-p ni de F crítico.
- Siglas: DBCA, DCL, DCGL. Bloques rotulados "B 1" y "B 2" en los arreglos.
- Los índices no son consistentes entre el modelo y las tablas ANOVA (ver nota antes de la
  diapositiva 26).

### 5. Cómo presenta los ejemplos

- Ejemplos **genéricos y pequeños** (4×4, o 3 tratamientos × 4 bloques) con letras y símbolos
  $Y_{11C}$ en vez de números, construidos por pasos: cuadrado estándar → cuadrado aleatorizado
  → asignación a los bloques → orden de las corridas (flechas).
- Un único ejemplo con contexto real (cohete propulsor, de Montgomery), usado solo de forma
  verbal para identificar tratamiento, bloque 1, bloque 2 y las formas de replicar; sin datos.
- Analogías cotidianas para los conceptos (familia/ventana, días de la semana y "¿cómo regresar
  el tiempo?").

### 6. Uso de software

En las fotos **no aparece ninguna captura de software** (ni Minitab ni otro), ni menús, ni
salidas. La única mención es en el procedimiento de análisis: "estimar el valor crítico con las
tablas de distribución o el valor-p con *software* estadístico". Para saber cómo muestra el
software habría que revisar otra clase o preguntar.

### 7. Rasgos de estilo

- **Títulos en forma de pregunta** en primera persona: "¿Cuál es el modelo matemático del
  diseño?", "¿Cómo debo aleatorizar el diseño?", "¿Cómo elijo el ANOVA apropiado?", "¿Qué
  debemos verificar sobre el modelo?". El mismo título se repite en varias diapositivas
  seguidas, cambiando solo una etiqueta de color con el nombre del diseño.
- **Código de colores fijo por diseño** (DBCA rojo, DCL azul, DCGL amarillo/naranja) en
  etiquetas, tablas y árbol de decisión.
- Densidad de texto media-baja: 2–4 frases o una lista corta por diapositiva; palabras clave en
  **negrita**; las tablas ANOVA ocupan la diapositiva entera.
- Dos tipografías: texto formal para la teoría y letra tipo manuscrita para notas al margen,
  aclaraciones, leyendas y lemas ("¡Forme bloques con lo que pueda y aleatorice lo que no
  pueda!").
- Mucho uso de **esquemas**: árboles de decisión, diagramas de llaves, fórmulas con cada término
  en un círculo de color y flecha a su significado, tablas de arreglo con flechas del orden de
  corrida.
- Lenguaje cercano: "culpables" para las fuentes de variabilidad, imperativos al estudiante
  ("Recuerde iniciar…", "Revise que…").
- Advertencias explícitas de errores frecuentes ("Lo que no es correcto es hacer todas las
  pruebas de un tratamiento de forma consecutiva").
- Listas numeradas para procedimientos y para los casos, con la misma numeración reutilizada
  después en los títulos de las tablas.
- Ilustraciones tipo clipart en las diapositivas conceptuales; ninguna en las técnicas.
