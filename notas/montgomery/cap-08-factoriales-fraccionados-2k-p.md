# Capítulo 8 — Diseños factoriales fraccionados de dos niveles

> Montgomery, págs. 303–362 (capítulo 8) y págs. 663–679 (Tabla XII del apéndice: relaciones de alias de los diseños $2^{k-p}$ con $k \le 15$ y $n \le 64$).

**Convenciones de esta ficha.** Factores con letras mayúsculas ($A, B, \dots$; la letra $I$ se reserva para la identidad, por eso el noveno factor es $J$). Combinaciones de tratamientos en minúsculas ($(1), a, b, ab, \dots$). $\ell_X$ es la combinación lineal (contraste dividido entre $N/2$) que "estima" el efecto $X$ **más sus alias**; la flecha $\ell_A \to A + BC$ indica qué suma de efectos estima realmente. Los números de ecuación, tabla y figura son los del libro. Las cifras de los ejemplos 8-1, 8-2, 8-3, 8-4, 8-7 y 8-8 fueron recalculadas a partir de los datos y coinciden con el libro salvo donde se indica.

Índice rápido:

- 8-1 Introducción (ideas clave)
- 8-2 Fracción un medio $2^{k-1}$ (generador, relación de definición, alias, resolución, construcción, proyección, secuencias) — ejemplos 8-1, 8-2, 8-3
- 8-3 Fracción un cuarto $2^{k-2}$ — ejemplo 8-4
- 8-4 Diseño $2^{k-p}$ general (generadores, aberración mínima, tabla 8-14, análisis, proyección, bloques) — ejemplos 8-5, 8-6
- 8-5 Resolución III (saturados, doblez, Plackett-Burman) — ejemplos 8-7, 8-8
- 8-6 Resolución IV y V (diseños mínimos, doblez, fracciones irregulares, doblez parcial)
- 8-7 Resumen (tabla 8-29)
- Recetario: procedimiento general, fórmulas y advertencias
- Tabla XII del apéndice (26 diseños, a–z)

---

## 8-1 Introducción

**Problema que resuelven.** En un $2^k$ el número de corridas crece muy rápido. En un $2^6$ (64 corridas) solo 6 de los 63 grados de libertad son efectos principales y 15 son interacciones de dos factores; los 42 restantes corresponden a interacciones de tres o más factores. Si se acepta que las interacciones de orden superior son despreciables, basta correr una **fracción** del factorial completo para estimar efectos principales e interacciones de orden bajo.

**Uso principal: experimentos de tamizado (cribado, *screening*)**: muchos factores, etapa temprana del proyecto, objetivo de identificar los pocos factores con efectos grandes para estudiarlos después con más detalle.

**Tres ideas clave que justifican los fraccionados:**

1. **Principio de efectos esparcidos (escasez de efectos).** Con muchas variables, el sistema suele estar dominado por unos pocos efectos principales e interacciones de orden bajo.
2. **Propiedad de proyección.** Un fraccionado se proyecta en un diseño más fuerte (más grande, incluso completo o con réplicas) en el subconjunto de factores significativos.
3. **Experimentación secuencial.** Las corridas de dos o más fracciones se pueden combinar para ensamblar un diseño mayor que estime los efectos e interacciones de interés.

---

## 8-2 La fracción un medio del diseño $2^k$

### Definiciones básicas (con el $2^{3-1}$)

Un $2^{3-1}$ tiene $2^{3-1}=4$ corridas: la mitad de un $2^3$.

- **Generador / palabra.** Se eligen las corridas con signo $+$ en la columna $ABC$ de la tabla de signos del $2^3$ (tabla 8-1): $a, b, c, abc$. $ABC$ es el **generador** de la fracción (a un generador también se le llama **palabra**).
- **Relación de definición.** Como la columna identidad $I$ es siempre $+$, en esa fracción $I = ABC$. En general la relación de definición es el conjunto de todas las columnas iguales a la columna $I$.
- **Fracción principal:** $I = +ABC$ (corridas $a, b, c, abc$). **Fracción alterna o complementaria:** $I = -ABC$ (corridas $(1), ab, ac, bc$). Ambas pertenecen a la misma **familia**; juntas forman el $2^3$ completo (fig. 8-1).

Tabla de signos de la fracción principal (parte superior de la tabla 8-1):

| Corrida | $I$ | $A$ | $B$ | $C$ | $AB$ | $AC$ | $BC$ | $ABC$ |
|---|---|---|---|---|---|---|---|---|
| $a$ | + | + | − | − | − | − | + | + |
| $b$ | + | − | + | − | − | + | − | + |
| $c$ | + | − | − | + | + | − | − | + |
| $abc$ | + | + | + | + | + | + | + | + |

### Estimación y alias

Con 4 corridas hay 3 grados de libertad. Las combinaciones lineales para los efectos principales son

$$\ell_A = \tfrac12(a-b-c+abc),\qquad \ell_B = \tfrac12(-a+b-c+abc),\qquad \ell_C = \tfrac12(-a-b+c+abc)$$

y las de las interacciones de dos factores resultan idénticas:

$$\ell_{BC} = \tfrac12(a-b-c+abc),\qquad \ell_{AC} = \tfrac12(-a+b-c+abc),\qquad \ell_{AB} = \tfrac12(-a-b+c+abc)$$

Por tanto $\ell_A=\ell_{BC}$, $\ell_B=\ell_{AC}$, $\ell_C=\ell_{AB}$: no se puede distinguir $A$ de $BC$, etc. Dos o más efectos con esta propiedad se llaman **alias**. Notación: $\ell_A \to A+BC$, $\ell_B \to B+AC$, $\ell_C \to C+AB$.

**Regla para obtener los alias:** multiplicar el efecto por cada palabra de la relación de definición, usando que el cuadrado de cualquier columna es $I$ (aritmética módulo 2 sobre los exponentes):

$$A\cdot I = A\cdot ABC = A^2BC = BC \Rightarrow A = BC;\qquad B = AB^2C = AC;\qquad C = ABC^2 = AB$$

**Fracción alterna** ($I=-ABC$): los alias cambian de signo:

$$\ell'_A \to A-BC,\qquad \ell'_B \to B-AC,\qquad \ell'_C \to C-AB$$

En la práctica no importa cuál de las dos fracciones se corra.

### Combinación de las dos fracciones (des-aliasado)

Si se corren ambas fracciones se tiene el $2^3$ completo (en dos bloques de 4 corridas, con $ABC$ confundida con bloques). De forma equivalente, sumando y restando las combinaciones lineales:

$$\tfrac12(\ell_A+\ell'_A) = \tfrac12(A+BC+A-BC) \to A,\qquad \tfrac12(\ell_A-\ell'_A) \to BC$$

| $i$ | De $\tfrac12(\ell_i+\ell'_i)$ | De $\tfrac12(\ell_i-\ell'_i)$ |
|---|---|---|
| $A$ | $A$ | $BC$ |
| $B$ | $B$ | $AC$ |
| $C$ | $C$ | $AB$ |

### Resolución del diseño

**Definición general.** Un diseño es de **resolución $R$** si ningún efecto de $p$ factores es alias de otro efecto que contenga menos de $R-p$ factores. Se denota con subíndice romano: $2^{3-1}_{\mathrm{III}}$.

**Regla operativa.** La resolución es igual al **menor número de letras de cualquier palabra de la relación de definición** (diseños "de tres, cuatro y cinco letras").

| Resolución | Qué garantiza | Ejemplo |
|---|---|---|
| **III** | Ningún efecto principal es alias de otro principal; los principales sí son alias de interacciones de dos factores (2fi), y algunas 2fi pueden ser alias entre sí. | $2^{3-1}_{\mathrm{III}}$, $I=ABC$ |
| **IV** | Ningún principal es alias de otro principal ni de 2fi; las 2fi son alias entre sí. | $2^{4-1}_{\mathrm{IV}}$, $I=ABCD$ |
| **V** | Ningún principal ni 2fi es alias de otro principal o 2fi; las 2fi son alias de interacciones de tres factores. | $2^{5-1}_{\mathrm{V}}$, $I=ABCDE$ |

**Recomendación:** usar la resolución más alta compatible con el grado de fraccionamiento requerido; a mayor resolución, menos restrictivos son los supuestos sobre qué interacciones son despreciables para tener una interpretación única.

### Construcción de fracciones un medio (método del diseño básico)

1. Escribir el **diseño básico**: un factorial **completo** $2^{k-1}$ en los primeros $k-1$ factores (tiene el número correcto de renglones pero le falta una columna).
2. Agregar el factor $k$-ésimo igualando sus signos a los de la interacción de orden más alto de los otros: $K = ABC\cdots(K-1)$. Equivale a resolver el generador $I=ABC\cdots K$ para la columna faltante.
3. La fracción alterna se obtiene con $K = -ABC\cdots(K-1)$.

Se podría usar cualquier otra interacción para generar la columna $K$, pero entonces no se obtiene la resolución máxima. La máxima resolución de una fracción un medio es $R=k$.

Tabla 8-2 (las dos fracciones un medio del $2^3$):

| Corrida | $A$ | $B$ | $C=AB$ ($I=ABC$) | $C=-AB$ ($I=-ABC$) |
|---|---|---|---|---|
| 1 | − | − | + | − |
| 2 | + | − | − | + |
| 3 | − | + | − | + |
| 4 | + | + | + | − |

**Otra forma de verlo:** partir el $2^k$ en dos bloques confundiendo la interacción de orden más alto $ABC\cdots K$; cada bloque es una fracción $2^{k-1}$ de máxima resolución.

### Proyección de fracciones en factoriales

- Todo fraccionado de resolución $R$ contiene factoriales **completos** (posiblemente con réplicas) en cualquier subconjunto de $R-1$ factores.
- Si se cree que a lo sumo $R-1$ factores son importantes, un diseño de resolución $R$ es la elección adecuada: si se está en lo cierto, se proyecta en un factorial completo en los factores activos.
- El $2^{3-1}_{\mathrm{III}}$ se proyecta en un $2^2$ completo en cualquier par de factores (fig. 8-2).
- Como una fracción un medio tiene $R=k$: todo $2^{k-1}$ se proyecta en un factorial completo en cualquiera $k-1$ de los factores; en **dos réplicas** de un completo en cualquier subconjunto de $k-2$ factores; en **cuatro réplicas** en cualquier subconjunto de $k-3$; etcétera.

### Ejemplo 8-1 — $2^{4-1}_{\mathrm{IV}}$, índice de filtración (págs. 308–310)

**Contexto.** Se retoma el experimento del índice de filtración del ejemplo 6-2 (un $2^4$ sin réplicas; allí resultaron activos $A$, $C$, $D$, $AC$ y $AD$) y se simula lo que habría pasado corriendo solo media fracción. Factores: $A$ = temperatura, $B$, $C$ = concentración, $D$ = velocidad de agitación.

**Diseño.** $I=ABCD$ (fracción principal), diseño básico $2^3$ en $A,B,C$ y $D=ABC$ (tabla 8-3):

| Corrida | $A$ | $B$ | $C$ | $D=ABC$ | Tratamiento | Índice de filtración |
|---|---|---|---|---|---|---|
| 1 | − | − | − | − | $(1)$ | 45 |
| 2 | + | − | − | + | $ad$ | 100 |
| 3 | − | + | − | + | $bd$ | 45 |
| 4 | + | + | − | − | $ab$ | 65 |
| 5 | − | − | + | + | $cd$ | 75 |
| 6 | + | − | + | − | $ac$ | 60 |
| 7 | − | + | + | − | $bc$ | 80 |
| 8 | + | + | + | + | $abcd$ | 96 |

**Alias.** $A=BCD$, $B=ACD$, $C=ABD$, $D=ABC$; $AB=CD$, $AC=BD$, $AD=BC$. Cuatro principales + tres pares de 2fi = 7 grados de libertad.

**Estimaciones (tabla 8-4).** Ejemplo de cálculo: $\ell_A=\tfrac14(-45+100-45+65-75+60-80+96)=19.00$.

| Estimación | Estructura de alias |
|---|---|
| $\ell_A = 19.00$ | $A+BCD$ |
| $\ell_B = 1.50$ | $B+ACD$ |
| $\ell_C = 14.00$ | $C+ABD$ |
| $\ell_D = 16.50$ | $D+ABC$ |
| $\ell_{AB} = -1.00$ | $AB+CD$ |
| $\ell_{AC} = -18.50$ | $AC+BD$ |
| $\ell_{AD} = 19.00$ | $AD+BC$ |

**Interpretación.** $A$, $C$ y $D$ son grandes. Como $B$ no es importante, lo razonable es atribuir las cadenas $AC+BD$ y $AD+BC$ a $AC$ y $AD$ (**navaja de Ockham**: ante varias interpretaciones posibles, la más simple suele ser la correcta). Coincide con el análisis del $2^4$ completo.

**Proyección.** Al descartar $B$, el diseño se proyecta en una sola réplica de un $2^3$ en $A, C, D$ (fig. 8-4). Con $A$ bajo, $C$ tiene efecto positivo grande; con $A$ alto, el efecto de $C$ es muy pequeño (interacción $AC$). Con $A$ bajo, $D$ es despreciable; con $A$ alto, $D$ tiene efecto positivo grande (interacción $AD$).

**Modelo de regresión** ($x_1, x_3, x_4$ codifican $A, C, D$ en $[-1,+1]$; coeficiente = efecto/2; $\hat\beta_0$ = promedio de las 8 respuestas = 70.75):

$$\hat y = 70.75 + \left(\tfrac{19.00}{2}\right)x_1 + \left(\tfrac{14.00}{2}\right)x_3 + \left(\tfrac{16.50}{2}\right)x_4 + \left(\tfrac{-18.50}{2}\right)x_1x_3 + \left(\tfrac{19.00}{2}\right)x_1x_4$$

### Ejemplo 8-2 — $2^{5-1}_{\mathrm{V}}$ para mejorar el rendimiento de un proceso (págs. 311–315)

**Contexto.** Manufactura de un circuito integrado; respuesta = rendimiento. Factores: $A$ = ajuste de apertura (pequeña, grande), $B$ = tiempo de exposición (20 % abajo y arriba del nominal), $C$ = tiempo de desarrollo (30 s, 45 s), $D$ = tamaño de la máscara (pequeña, grande), $E$ = tiempo de grabado (14.5, 15.5 min). (En la tabla 8-6 del libro los nombres de $B$ y $C$ aparecen intercambiados respecto al texto y a la tabla 8-7.)

**Diseño.** Básico $2^4$ en $A,B,C,D$; $E=ABCD$; $I=ABCDE$. Resolución V: cada principal es alias de una interacción de 4 factores ($\ell_A\to A+BCDE$) y cada 2fi de una de 3 factores ($\ell_{AB}\to AB+CDE$).

Respuestas en orden estándar de $A,B,C,D$ (tabla 8-5), con $E=ABCD$: $e=8$, $a=9$, $b=34$, $abe=52$, $c=16$, $ace=22$, $bce=45$, $abc=60$, $d=6$, $ade=10$, $bde=30$, $abd=50$, $cde=15$, $acd=21$, $bcd=44$, $abcde=63$.

**Efectos, coeficientes y sumas de cuadrados (tabla 8-6):**

| Término | Coef. de regresión | Efecto estimado | Suma de cuadrados |
|---|---|---|---|
| Promedio global | 30.3125 | | |
| $A$ | 5.5625 | 11.1250 | 495.062 |
| $B$ | 16.9375 | 33.8750 | 4590.062 |
| $C$ | 5.4375 | 10.8750 | 473.062 |
| $D$ | −0.4375 | −0.8750 | 3.063 |
| $E$ | 0.3125 | 0.6250 | 1.563 |
| $AB$ | 3.4375 | 6.8750 | 189.063 |
| $AC$ | 0.1875 | 0.3750 | 0.563 |
| $AD$ | 0.5625 | 1.1250 | 5.063 |
| $AE$ | 0.5625 | 1.1250 | 5.063 |
| $BC$ | 0.3125 | 0.6250 | 1.563 |
| $BD$ | −0.0625 | −0.1250 | 0.063 |
| $BE$ | −0.0625 | −0.1250 | 0.063 |
| $CD$ | 0.4375 | 0.8750 | 3.063 |
| $CE$ | 0.1875 | 0.3750 | 0.563 |
| $DE$ | −0.6875 | −1.3750 | 7.563 |

**Gráfica de probabilidad normal de efectos (fig. 8-6):** sobresalen $A$, $B$, $C$ y $AB$ (en rigor $A+BCDE$, $B+ACDE$, $C+ABDE$, $AB+CDE$; se asume que las interacciones de 3 o más factores son despreciables).

**ANOVA (tabla 8-7):**

| Fuente | SS | gl | CM | $F_0$ | Valor $P$ |
|---|---|---|---|---|---|
| $A$ (apertura) | 495.0625 | 1 | 495.0625 | 193.20 | <0.0001 |
| $B$ (tiempo de exposición) | 4590.0625 | 1 | 4590.0625 | 1791.24 | <0.0001 |
| $C$ (tiempo de desarrollo) | 473.0625 | 1 | 473.0625 | 184.61 | <0.0001 |
| $AB$ | 189.0625 | 1 | 189.0625 | 73.78 | <0.0001 |
| Error | 28.1875 | 11 | 2.5625 | | |
| Total | 5775.4375 | 15 | | | |

$SS_{\text{Modelo}} = SS_A+SS_B+SS_C+SS_{AB} = 5747.25$, más del 99 % de la variabilidad total.

**Diagnósticos.** Gráfica normal de residuales (fig. 8-7) y residuales contra predichos (fig. 8-8): ambas satisfactorias.

**Conclusiones.** $A$, $B$, $C$ tienen efectos positivos grandes; la gráfica de la interacción $AB$ (fig. 8-9) confirma que el rendimiento es máximo con $A$ y $B$ altos. El $2^{5-1}$ se proyecta en **dos réplicas de un $2^3$** en cualesquiera tres factores; en $A,B,C$ los promedios de los vértices (fig. 8-10) son:

| $A$ | $B$ | $C$ | Promedio |
|---|---|---|---|
| − | − | − | 7.0 |
| + | − | − | 9.5 |
| − | + | − | 32.0 |
| + | + | − | 51.0 |
| − | − | + | 15.5 |
| + | − | + | 21.5 |
| − | + | + | 44.5 |
| + | + | + | 61.5 |

Mejor condición: $A$, $B$, $C$ altos. $D$ y $E$ tienen poco efecto y se pueden fijar donde convenga a otros objetivos (por ejemplo costo).

### Secuencias de diseños factoriales fraccionados

- Casi siempre es preferible correr primero una fracción (p. ej. $2^{4-1}_{\mathrm{IV}}$, 8 corridas), analizarla y luego decidir la siguiente serie de corridas.
- Si quedan ambigüedades, se corre la fracción alterna y se completa el $2^k$. Las dos mitades actúan como **bloques** con la interacción de orden más alto confundida (aquí $ABCD$): lo único que se pierde es información sobre esa interacción.
- Con frecuencia la primera fracción basta para pasar a la etapa siguiente. Opciones de seguimiento (fig. 8-11, adaptada de Box): (a) moverse a una nueva localización para explorar una tendencia aparente; (b) agregar otra fracción para resolver ambigüedades; (c) reescalar factores cuyos rangos resultaron inapropiados; (d) eliminar y agregar factores; (e) hacer réplicas para mejorar estimaciones o porque algunas corridas se hicieron mal; (f) aumentar el diseño para modelar una curvatura aparente.

### Ejemplo 8-3 — Fracción alterna para aislar interacciones (págs. 315–317)

**Contexto.** Continuación del ejemplo 8-1: se corre la fracción alterna $I=-ABCD$ ($D=-ABC$) para separar $AC$ de $BD$ y $AD$ de $BC$ sin depender del juicio del experimentador.

Respuestas (orden estándar de $A,B,C$): $d=43$, $a=71$, $b=48$, $abd=104$, $c=68$, $acd=86$, $bcd=70$, $abc=65$.

**Estimaciones de la fracción alterna:**

| Estimación | Estima |
|---|---|
| $\ell'_A = 24.25$ | $A-BCD$ |
| $\ell'_B = 4.75$ | $B-ACD$ |
| $\ell'_C = 5.75$ | $C-ABD$ |
| $\ell'_D = 12.75$ | $D-ABC$ |
| $\ell'_{AB} = 1.25$ | $AB-CD$ |
| $\ell'_{AC} = -17.75$ | $AC-BD$ |
| $\ell'_{AD} = 14.25$ | $AD-BC$ |

**Combinación de las dos fracciones:**

| $i$ | $\tfrac12(\ell_i+\ell'_i)$ | $\tfrac12(\ell_i-\ell'_i)$ |
|---|---|---|
| $A$ | $21.63 \to A$ | $-2.63 \to BCD$ |
| $B$ | $3.13 \to B$ | $-1.63 \to ACD$ |
| $C$ | $9.88 \to C$ | $4.13 \to ABD$ |
| $D$ | $14.63 \to D$ | $1.88 \to ABC$ |
| $AB$ | $0.13 \to AB$ | $-1.13 \to CD$ |
| $AC$ | $-18.13 \to AC$ | $-0.38 \to BD$ |
| $AD$ | $16.63 \to AD$ | $2.38 \to BC$ |

Coinciden exactamente con el análisis del $2^4$ completo (ej. 6-2). Las interacciones grandes son $AC$ y $AD$.

**Experimento de confirmación.** Agregar la fracción alterna es una forma de confirmación. Una alternativa más barata: usar el modelo para predecir la respuesta en un punto de interés del espacio de diseño (que no sea uno de los puntos ya corridos), correr ese ensayo (quizá varias veces) y comparar lo predicho con lo observado.

---

## 8-3 La fracción un cuarto del diseño $2^k$

### Definiciones

- Un $2^{k-2}$ tiene $2^{k-2}$ corridas y **dos generadores** $P$ y $Q$. $I=P$ e $I=Q$ son las **relaciones generadoras**.
- Los signos de $P$ y $Q$ ($\pm$) determinan cuál de las cuatro fracciones de la **familia** se obtiene; la **fracción principal** es la de $+P$ y $+Q$.
- **Relación de definición completa:** $I = P = Q = PQ$, donde $PQ$ es la **interacción generalizada** (producto módulo 2). $P$, $Q$ y $PQ$ son las **palabras**.
- Cada efecto tiene **tres alias** (se multiplica por cada palabra). Hay que elegir los generadores para que los efectos potencialmente importantes no queden aliados entre sí.

### Construcción (diseño básico)

1. Escribir un factorial completo en $k-2$ factores.
2. Asociar las dos columnas adicionales con interacciones elegidas de los primeros $k-2$ factores.

Equivalente: formar los cuatro bloques del $2^k$ confundiendo $P$ y $Q$ (y por tanto $PQ$) y quedarse con el bloque en que ambos son positivos.

### El $2^{6-2}_{\mathrm{IV}}$ con $I=ABCE$ e $I=BCDF$

Interacción generalizada: $(ABCE)(BCDF)=ADEF$. Relación de definición completa:

$$I = ABCE = BCDF = ADEF \quad\Rightarrow\quad \text{resolución IV}$$

Construcción (tabla 8-9): básico $2^4$ en $A,B,C,D$ (16 corridas), $E=ABC$, $F=BCD$. Columnas resultantes, corridas 1–16 en orden estándar:

- $E=ABC$: `− + + − + − − + − + + − + − − +`
- $F=BCD$: `− − + + + + − − + + − − − − + +`

**Estructura de alias completa (tabla 8-8):**

| Efectos principales | Interacciones de dos factores |
|---|---|
| $A = BCE = DEF = ABCDF$ | $AB = CE = ACDF = BDEF$ |
| $B = ACE = CDF = ABDEF$ | $AC = BE = ABDF = CDEF$ |
| $C = ABE = BDF = ACDEF$ | $AD = EF = BCDE = ABCF$ |
| $D = BCF = AEF = ABCDE$ | $AE = BC = DF = ABCDEF$ |
| $E = ABC = ADF = BCDEF$ | $AF = DE = BCEF = ABCD$ |
| $F = BCD = ADE = ABCEF$ | $BD = CF = ACDE = ABEF$ |
| | $BF = CD = ACEF = ABDE$ |

Las dos cadenas restantes solo contienen interacciones de tres factores: $ABD = CDE = ACF = BEF$ y $ACD = BDE = ABF = CEF$. Total: 6 + 7 + 2 = 15 grados de libertad. Si las interacciones de tres o más factores son despreciables, los efectos principales se estiman limpios.

### Fracciones alternas

Hay tres fracciones alternas: $(I=ABCE,\ I=-BCDF)$; $(I=-ABCE,\ I=BCDF)$; $(I=-ABCE,\ I=-BCDF)$. Se construyen cambiando el signo de la columna correspondiente. Ejemplo: con $F=-BCD$ la columna de $F$ queda `+ + − − − − + + − − + + + + − −`, la relación de definición es $I = ABCE = -BCDF = -ADEF$, y los alias cambian de signo: $A = BCE = -DEF = -ABCDF$, es decir $\ell_A \to A + BCE - DEF - ABCDF$.

### Proyección del $2^{k-2}$

- El $2^{6-2}_{\mathrm{IV}}$ se proyecta en **una réplica de un $2^4$ completo** en cualquier subconjunto de cuatro factores que **no** sea palabra de la relación de definición (hay 12 de esos subconjuntos: $ABCD$, $ABCF$, …).
- En los subconjuntos que **sí** son palabra ($ABCE$, $BCDF$, $ADEF$) se pliega en **dos réplicas de un $2^{4-1}$**.
- En **cualquier** subconjunto de tres factores: dos réplicas de un $2^3$; en cualquier par: cuatro réplicas de un $2^2$.
- En general, un $2^{k-2}$ se pliega en un factorial completo o en un fraccionado en algún subconjunto de $r \le k-2$ factores; los subconjuntos que forman factoriales completos son los que no son palabras de la relación de definición.

### Ejemplo 8-4 — $2^{6-2}_{\mathrm{IV}}$, moldeo por inyección (págs. 319–325)

**Contexto.** Contracción excesiva de piezas moldeadas por inyección. Factores: $A$ = temperatura de moldeo, $B$ = velocidad del enroscado (tornillo), $C$ = tiempo de retención, $D$ = duración del ciclo, $E$ = tamaño del vaciadero, $F$ = presión de retención. Respuesta: contracción ($\times 10$).

**Diseño.** El de la tabla 8-9 ($E=ABC$, $F=BCD$), 16 corridas. Respuestas en orden estándar de $A,B,C,D$ (tabla 8-10): 6, 10, 32, 60, 4, 15, 26, 60, 8, 12, 34, 60, 16, 5, 37, 52.

**Efectos (tabla 8-11):**

| Término (con sus alias de 2 factores) | Coef. de regresión | Efecto | Suma de cuadrados |
|---|---|---|---|
| Promedio global | 27.3125 | | |
| $A$ | 6.9375 | 13.8750 | 770.062 |
| $B$ | 17.8125 | 35.6250 | 5076.562 |
| $C$ | −0.4375 | −0.8750 | 3.063 |
| $D$ | 0.6875 | 1.3750 | 7.563 |
| $E$ | 0.1875 | 0.3750 | 0.563 |
| $F$ | 0.1875 | 0.3750 | 0.563 |
| $AB+CE$ | 5.9375 | 11.8750 | 564.063 |
| $AC+BE$ | −0.8125 | −1.6250 | 10.562 |
| $AD+EF$ | −2.6875 | −5.3750 | 115.562 |
| $AE+BC+DF$ | −0.9375 | −1.8750 | 14.063 |
| $AF+DE$ | 0.3125 | 0.6250 | 1.563 |
| $BD+CF$ | −0.0625 | −0.1250 | 0.063 |
| $BF+CD$ | −0.0625 | −0.1250 | 0.063 |
| $ABD$ | 0.0625 | 0.1250 | 0.063 |
| $ABF$ | −2.4375 | −4.8750 | 95.063 |

**Efectos de localización.** La gráfica normal (fig. 8-12) destaca $A$, $B$ y $AB$ (tentativamente, dada la cadena $AB+CE$). Interacción $AB$ (fig. 8-13): con $B$ bajo el proceso es insensible a la temperatura; con $B$ alto es muy sensible. Con $B$ bajo la contracción media ronda el 10 % sin importar la temperatura. Decisión inicial: $A$ y $B$ en nivel bajo.

Modelo:

$$\hat y = 27.3125 + 6.9375x_1 + 17.8125x_2 + 5.9375x_1x_2,\qquad e = y-\hat y$$

Gráfica normal de residuales (fig. 8-14): satisfactoria.

**Efectos de dispersión.** La gráfica de residuales contra $C$ (fig. 8-15) muestra mucha menos dispersión con $C$ bajo. Como el modelo ya eliminó los efectos de localización, los residuales informan sobre la variabilidad (válido solo si el modelo de localización es correcto, cap. 6). Estadístico para cada columna $i$ de la tabla de signos:

$$F_i^* = \ln\frac{S^2(i^+)}{S^2(i^-)}$$

donde $S(i^+)$ y $S(i^-)$ son las desviaciones estándar de los residuales en los niveles alto y bajo de la columna $i$. Si las varianzas son iguales, $F_i^*$ es aproximadamente normal con media cero; se grafican los $F_i^*$ en papel de probabilidad normal (fig. 8-16).

Residuales (corridas 1–16): −2.50, −0.50, −0.25, 2.00, −4.50, 4.50, −6.25, 2.00, −0.50, 1.50, 1.75, 2.00, 7.50, −5.50, 4.75, −6.00.

Tabla 8-12 (resumen):

| Columna | $S(i^+)$ | $S(i^-)$ | $F_i^*$ |
|---|---|---|---|
| $A$ | 3.80 | 4.60 | −0.38 |
| $B$ | 4.01 | 4.41 | −0.19 |
| $AB=CE$ | 4.33 | 4.10 | 0.11 |
| $C$ | **5.70** | **1.63** | **2.50** |
| $AC=BE$ | 3.68 | 4.53 | −0.42 |
| $AE=BC=DF$ | 3.85 | 4.33 | −0.23 |
| $E$ | 4.17 | 4.25 | −0.04 |
| $D$ | 4.64 | 3.59 | 0.51 |
| $AD=EF$ | 3.39 | 2.75 | 0.42 |
| $BD=CE$ (así impreso; la cadena es $BD=CF$) | 4.01 | 4.41 | −0.19 |
| $ABD$ | 4.72 | 3.51 | 0.59 |
| $BF=CD$ | 4.71 | 3.65 | 0.51 |
| $ACD$ | 3.50 | 3.12 | 0.23 |
| $F$ | 3.88 | 4.52 | −0.31 |
| $AF=DE$ | 4.87 | 3.40 | 0.72 |

Solo $C$ sobresale: **efecto de dispersión** real. Fijar el tiempo de retención en el nivel bajo reduce la variabilidad pieza a pieza.

**Proyección en $A,B,C$** (fig. 8-17; promedio y rango en cada vértice del cubo):

| $A$ | $B$ | $C$ | $\bar y$ | Rango $R$ |
|---|---|---|---|---|
| − | − | − | 7.0 | 2 |
| + | − | − | 11.0 | 2 |
| − | + | − | 33.0 | 2 |
| + | + | − | 60.0 | 0 |
| − | − | + | 10.0 | 12 |
| + | − | + | 10.0 | 11 (con los datos de la tabla 8-10 el rango calculado es 10) |
| − | + | + | 31.5 | 11 |
| + | + | + | 56.0 | 8 |

**Conclusión.** $B$ (velocidad del enroscado) bajo es la clave para reducir la contracción media; con $B$ bajo casi cualquier combinación de $A$ y $C$ da contracción baja. Pero $C$ bajo es la única elección razonable para mantener baja la variabilidad.

---

## 8-4 El diseño factorial fraccionado $2^{k-p}$ general

### Definiciones

- Fracción $1/2^p$ de un $2^k$: $2^{k-p}$ corridas; requiere **$p$ generadores independientes**.
- **Relación de definición completa:** los $p$ generadores más sus $2^p-p-1$ interacciones generalizadas ($2^p-1$ palabras en total).
- Cada efecto tiene $2^p-1$ alias (se multiplica por cada palabra).
- Solo se pueden estimar $2^{k-p}-1$ efectos (con sus alias).
- Para $k$ moderadamente grande se suele suponer despreciables las interacciones de tercer orden en adelante, lo que simplifica mucho la estructura de alias.

### Elección de generadores

**Criterio 1: máxima resolución.** Elegir los generadores para obtener la mayor resolución posible. Ejemplo: en el $2^{6-2}$, $E=ABC$, $F=BCD$ da $I=ABCE=BCDF=ADEF$ (resolución IV, la máxima). Con $E=ABC$, $F=ABCD$ se tendría $I=ABCE=ABCDF=DEF$ (resolución III): elección inferior, sacrifica información sobre interacciones sin necesidad.

**Criterio 2: aberración mínima.** La resolución no basta para distinguir diseños. Tres $2^{7-2}_{\mathrm{IV}}$ (tabla 8-13):

| | Diseño A | Diseño B | Diseño C |
|---|---|---|---|
| Generadores | $F=ABC$, $G=BCD$ | $F=ABC$, $G=ADE$ | $F=ABCD$, $G=ABDE$ |
| Relación de definición | $I=ABCF=BCDG=ADFG$ | $I=ABCF=ADEG=BCDEFG$ | $I=ABCDF=ABDEG=CEFG$ |
| Patrón de longitud de palabras | $\{4,4,4\}$ | $\{4,4,6\}$ | $\{4,5,5\}$ |
| 2fi aliadas entre sí | $AB=CF$, $AC=BF$, $AD=FG$, $AG=DF$, $BD=CG$, $BG=CD$, $AF=BC=DG$ | $AB=CF$, $AC=BF$, $AD=EG$, $AE=DG$, $AF=BC$, $AG=DE$ | $CE=FG$, $CF=EG$, $CG=EF$ |

El diseño C tiene una sola palabra de longitud 4 (los otros, dos o tres): **minimiza el número de palabras de longitud mínima** en la relación de definición. Ese es el **diseño de aberración mínima**. Minimizar la aberración en un diseño de resolución $R$ asegura el número mínimo de efectos principales aliados con interacciones de orden $R-1$, el número mínimo de 2fi aliadas con interacciones de orden $R-2$, etc. (Fries y Hunter).

### Tabla 8-14 — Diseños $2^{k-p}$ seleccionados (máxima resolución y aberración mínima)

Todos los generadores admiten signo $\pm$ (el $+$ da la fracción principal). Los alias de los diseños con $n\le 64$ están en la Tabla XII del apéndice.

| $k$ | Fracción | Corridas | Generadores |
|---|---|---|---|
| 3 | $2^{3-1}_{\mathrm{III}}$ | 4 | $C=\pm AB$ |
| 4 | $2^{4-1}_{\mathrm{IV}}$ | 8 | $D=\pm ABC$ |
| 5 | $2^{5-1}_{\mathrm{V}}$ | 16 | $E=\pm ABCD$ |
| 5 | $2^{5-2}_{\mathrm{III}}$ | 8 | $D=\pm AB$, $E=\pm AC$ |
| 6 | $2^{6-1}_{\mathrm{VI}}$ | 32 | $F=\pm ABCDE$ |
| 6 | $2^{6-2}_{\mathrm{IV}}$ | 16 | $E=\pm ABC$, $F=\pm BCD$ |
| 6 | $2^{6-3}_{\mathrm{III}}$ | 8 | $D=\pm AB$, $E=\pm AC$, $F=\pm BC$ |
| 7 | $2^{7-1}_{\mathrm{VII}}$ | 64 | $G=\pm ABCDEF$ |
| 7 | $2^{7-2}_{\mathrm{IV}}$ | 32 | $F=\pm ABCD$, $G=\pm ABDE$ |
| 7 | $2^{7-3}_{\mathrm{IV}}$ (la tabla 8-14 impresa dice III; el texto, la tabla 8-15 y la Tabla XII(i) dicen IV, que es lo correcto) | 16 | $E=\pm ABC$, $F=\pm BCD$, $G=\pm ACD$ |
| 7 | $2^{7-4}_{\mathrm{III}}$ | 8 | $D=\pm AB$, $E=\pm AC$, $F=\pm BC$, $G=\pm ABC$ |
| 8 | $2^{8-2}_{\mathrm{V}}$ | 64 | $G=\pm ABCD$, $H=\pm ABEF$ |
| 8 | $2^{8-3}_{\mathrm{IV}}$ | 32 | $F=\pm ABC$, $G=\pm ABD$, $H=\pm BCDE$ |
| 8 | $2^{8-4}_{\mathrm{IV}}$ | 16 | $E=\pm BCD$, $F=\pm ACD$, $G=\pm ABC$, $H=\pm ABD$ |
| 9 | $2^{9-2}_{\mathrm{VI}}$ | 128 | $H=\pm ACDFG$, $J=\pm BCEFG$ |
| 9 | $2^{9-3}_{\mathrm{IV}}$ | 64 | $G=\pm ABCD$, $H=\pm ACEF$, $J=\pm CDEF$ |
| 9 | $2^{9-4}_{\mathrm{IV}}$ | 32 | $F=\pm BCDE$, $G=\pm ACDE$, $H=\pm ABDE$, $J=\pm ABCE$ |
| 9 | $2^{9-5}_{\mathrm{III}}$ | 16 | $E=\pm ABC$, $F=\pm BCD$, $G=\pm ACD$, $H=\pm ABD$, $J=\pm ABCD$ |
| 10 | $2^{10-3}_{\mathrm{V}}$ | 128 | $H=\pm ABCG$, $J=\pm ACDE$, $K=\pm ACDF$ |
| 10 | $2^{10-4}_{\mathrm{IV}}$ | 64 | $G=\pm BCDF$, $H=\pm ACDF$, $J=\pm ABDE$, $K=\pm ABCE$ |
| 10 | $2^{10-5}_{\mathrm{IV}}$ | 32 | $F=\pm ABCD$, $G=\pm ABCE$, $H=\pm ABDE$, $J=\pm ACDE$, $K=\pm BCDE$ |
| 10 | $2^{10-6}_{\mathrm{III}}$ | 16 | $E=\pm ABC$, $F=\pm BCD$, $G=\pm ACD$, $H=\pm ABD$, $J=\pm ABCD$, $K=\pm AB$ |
| 11 | $2^{11-5}_{\mathrm{IV}}$ | 64 | $G=\pm CDE$, $H=\pm ABCD$, $J=\pm ABF$, $K=\pm BDEF$, $L=\pm ADEF$ |
| 11 | $2^{11-6}_{\mathrm{IV}}$ | 32 | $F=\pm ABC$, $G=\pm BCD$, $H=\pm CDE$, $J=\pm ACD$, $K=\pm ADE$, $L=\pm BDE$ |
| 11 | $2^{11-7}_{\mathrm{III}}$ | 16 | $E=\pm ABC$, $F=\pm BCD$, $G=\pm ACD$, $H=\pm ABD$, $J=\pm ABCD$, $K=\pm AB$, $L=\pm AC$ |
| 12 | $2^{12-8}_{\mathrm{III}}$ | 16 | $E=\pm ABC$, $F=\pm ABD$, $G=\pm ACD$, $H=\pm BCD$, $J=\pm ABCD$, $K=\pm AB$, $L=\pm AC$, $M=\pm AD$ |
| 13 | $2^{13-9}_{\mathrm{III}}$ | 16 | los del $2^{12-8}$ más $N=\pm BC$ |
| 14 | $2^{14-10}_{\mathrm{III}}$ | 16 | los del $2^{13-9}$ más $O=\pm BD$ |
| 15 | $2^{15-11}_{\mathrm{III}}$ | 16 | los del $2^{14-10}$ más $P=\pm CD$ |

### Ejemplo 8-5 — Elegir un diseño para 7 factores (pág. 327)

**Objetivo.** Estimar los 7 efectos principales y tener una idea aproximada de las 2fi, suponiendo despreciables las interacciones de 3 o más factores ⇒ resolución IV.

**Opciones (tabla 8-14).** $2^{7-2}_{\mathrm{IV}}$ (32 corridas) o $2^{7-3}_{\mathrm{IV}}$ (16 corridas).

- $2^{7-3}_{\mathrm{IV}}$ (Tabla XII(i)): los 7 principales son alias de interacciones de 3 factores; las 2fi quedan aliadas en grupos de tres. Cumple el objetivo con 16 corridas.
- $2^{7-2}_{\mathrm{IV}}$ (Tabla XII(j)): además 15 de las 21 2fi se estiman de manera única; es más información de la necesaria.

**Diseño elegido (tabla 8-15).** Básico $2^4$ en $A,B,C,D$; $E=ABC$, $F=BCD$, $G=ACD$. Generadores $I=ABCE$, $I=BCDF$, $I=ACDG$. Relación de definición completa:

$$I = ABCE = BCDF = ADEF = ACDG = BDEG = CEFG = ABFG$$

Columnas (corridas 1–16): $E$: `− + + − + − − + − + + − + − − +`; $F$: `− − + + + + − − + + − − − − + +`; $G$: `− + − + + − + − + − + − − + − +`.

### Análisis de los $2^{k-p}$

El efecto $i$-ésimo se estima con

$$\ell_i = \frac{2(\text{Contraste}_i)}{N} = \frac{\text{Contraste}_i}{N/2},\qquad N=2^{k-p}$$

donde el contraste se forma con los signos de la columna $i$. Relaciones útiles (del cap. 6, usadas en las tablas de este capítulo): coeficiente de regresión $\hat\beta_i=\ell_i/2$; $\hat\beta_0=\bar y$; suma de cuadrados de un efecto con un grado de libertad $SS_i = (\text{Contraste}_i)^2/N = N\,\ell_i^2/4$. Con una sola réplica, el procedimiento es: gráfica de probabilidad normal de los efectos → modelo tentativo → ANOVA con los efectos descartados como error → análisis de residuales. Software citado: Design-Expert.

### Proyección del $2^{k-p}$

- Se reduce a un factorial completo o a un fraccionado en cualquier subconjunto de $r \le k-p$ factores. Los subconjuntos que dan fraccionados son los que **aparecen como palabras** en la relación de definición completa.
- Muy útil en tamizado cuando se sospecha que la mayoría de los factores tendrán efectos pequeños. Las conclusiones son tentativas: suele haber explicaciones alternativas basadas en interacciones de orden superior.
- **$2^{7-3}_{\mathrm{IV}}$ del ejemplo 8-5:** de los 35 subconjuntos de cuatro factores, 7 son palabras de la relación de definición; los otros 28 forman $2^4$ completos (uno obvio: $A,B,C,D$).
- **Estrategia de asignación (molino de bolas, 7 factores):** asignar los factores que se cree importantes y que pueden interactuar (velocidad del motor, modo de alimentación, tamaño de la alimentación, tipo de material) a las columnas del diseño básico $A,B,C,D$, y las "variables menores" (muesca, ángulo de la criba, nivel de vibración de la criba) a $E,F,G$. Si las menores resultan despreciables queda un $2^4$ completo en las variables clave.

### Separación en bloques de fraccionados

- Cuando no se pueden hacer todas las corridas en condiciones homogéneas, el fraccionado se **confunde en bloques**. La Tabla XII da los arreglos recomendados; el tamaño mínimo de bloque en esos arreglos es 8 corridas.
- **Procedimiento:** elegir para confundir con bloques una cadena de alias que solo contenga interacciones de orden alto. En el $2^{6-2}_{\mathrm{IV}}$ ($I=ABCE=BCDF=ADEF$) hay dos cadenas con solo interacciones de tres factores; la tabla XII(f) sugiere $ABD$ (y sus alias $CDE=ACF=BEF$).
- **Dos bloques de 8 (fig. 8-18):**
  - Bloque 1 (bloque principal): $(1)$, $abf$, $cef$, $abce$, $adef$ (impreso "$abef$" en la figura; debe ser $adef$ para pertenecer a la fracción), $bde$, $acd$, $bcdf$.
  - Bloque 2: $ae$, $acf$, $bef$, $bc$, $df$, $abd$, $cde$, $abcdef$.
- El bloque principal contiene las combinaciones con un número par de letras en común con $ABD$, es decir las que cumplen $L = x_1+x_2+x_4 = 0 \pmod 2$.

### Ejemplo 8-6 — $2^{8-3}_{\mathrm{IV}}$ en cuatro bloques, máquina CNC (págs. 332–337)

**Contexto.** Máquina CNC de cinco ejes para maquinar un propulsor de turbina. Respuesta: desviación estándar de la diferencia entre el perfil real y el especificado del álabe ($\times 10^3$ pulg), analizada como $\ln(\text{desv. estándar}\times 10^3)$.

| Factor | Bajo (−) | Alto (+) |
|---|---|---|
| $A$ = desviación en el eje $x$ (0.001 pulg) | 0 | 15 |
| $B$ = desviación en el eje $y$ (0.001 pulg) | 0 | 15 |
| $C$ = desviación en el eje $z$ (0.001 pulg) | 0 | 15 |
| $D$ = fabricante de la herramienta | 1 | 2 |
| $E$ = desviación del eje $a$ (0.001 grados) | 0 | 30 |
| $F$ = velocidad del areómetro (%) | 90 | 110 |
| $G$ = altura de la plantilla sujetadora (0.001 pulg) | 0 | 15 |
| $H$ = velocidad de alimentación (%) | 90 | 110 |

La máquina tiene cuatro areómetros, que se tratan como **bloques**.

**Elección del diseño.** Los ingenieros descartan interacciones de 3+ factores pero no las de dos. Candidatos: $2^{8-4}_{\mathrm{IV}}$ (16 corridas) y $2^{8-3}_{\mathrm{IV}}$ (32). El de 16 tiene muchas 2fi aliadas entre sí y no puede correrse en cuatro bloques sin confundir cuatro 2fi con bloques ⇒ se usa el **$2^{8-3}_{\mathrm{IV}}$ en cuatro bloques**: básico $2^5$ en $A$–$E$, $F=ABC$, $G=ABD$, $H=BCDE$. Con bloques quedan confundidas una cadena de interacciones de tres factores y la 2fi $EH$ (con sus alias de tres factores); $EH$ (eje $a$ × velocidad de alimentación) se considera muy improbable. Los datos completos (32 corridas, bloque y orden de corrida) están en la tabla 8-16.

**Efectos sobre $\ln(\text{desv. estándar}\times10^3)$ (tabla 8-17):**

| Término | Coeficiente | Efecto | SS |
|---|---|---|---|
| Promedio global | 1.28007 | | |
| $A$ | 0.14513 | 0.29026 | 0.674020 |
| $B$ | −0.10027 | −0.20054 | 0.321729 |
| $C$ | −0.01288 | −0.02576 | 0.005310 |
| $D$ | 0.05407 | 0.10813 | 0.093540 |
| $E$ | −2.531E−04 | −5.063E−04 | 2.050E−06 |
| $F$ | −0.01936 | −0.03871 | 0.011988 |
| $G$ | 0.05804 | 0.11608 | 0.107799 |
| $H$ | 0.00708 | 0.01417 | 0.001606 |
| $AB+CF+DG$ | −0.00294 | −0.00588 | 2.767E−04 |
| $AC+BF$ | −0.03103 | −0.06206 | 0.030815 |
| $AD+BG$ | −0.18706 | −0.37412 | 1.119705 |
| $AE$ | 0.00402 | 0.00804 | 5.170E−04 |
| $AF+BC$ | −0.02251 | −0.04502 | 0.016214 |
| $AG+BD$ | 0.02644 | 0.05288 | 0.022370 |
| $AH$ | −0.02521 | −0.05042 | 0.020339 |
| $BE$ | 0.04925 | 0.09851 | 0.077627 |
| $BH$ | 0.00654 | 0.01309 | 0.001371 |
| $CD+FG$ | 0.01726 | 0.03452 | 0.009535 |
| $CE$ | 0.01991 | 0.03982 | 0.012685 |
| $CG+DF$ | −0.00733 | −0.01467 | 0.001721 |
| $CH$ | 0.03040 | 0.06080 | 0.029568 |
| $DE$ | 0.00854 | 0.01708 | 0.002334 |
| $DH$ | 0.00784 | 0.01569 | 0.001969 |
| $EF$ | −0.00904 | −0.01808 | 0.002616 |
| $EG$ | −0.02685 | −0.05371 | 0.023078 |
| $EH$ | −0.01767 | −0.03534 | 0.009993 |
| $FH$ | −0.01404 | −0.02808 | 0.006308 |
| $GH$ | 0.00245 | 0.00489 | 1.914E−04 |
| $ABE$ | 0.01665 | 0.03331 | 0.008874 |
| $ABH$ | −0.00631 | −0.01261 | 0.001273 |
| $ACD$ | −0.02717 | −0.05433 | 0.023617 |

**Interpretación.** La gráfica normal (fig. 8-19) destaca $A$, $B$ y la cadena $AD+BG$. $AD$ (eje $x$ × fabricante) y $BG$ (eje $y$ × altura de la plantilla) no se pueden separar con estos datos, y como ambas incluyen un efecto principal grande, no hay una simplificación lógica "obvia". Se requiere conocimiento del proceso o más corridas (sec. 8-5). Suponiendo, por conocimiento del proceso, que la interacción real es $AD$:

**ANOVA (tabla 8-18)** — modelo con $A$, $B$, $D$ y $AD$ ($D$ se incluye por **jerarquía**):

| Fuente | SS | gl | CM | $F_0$ | Valor $P$ |
|---|---|---|---|---|---|
| $A$ | 0.6740 | 1 | 0.6740 | 39.42 | <0.0001 |
| $B$ | 0.3217 | 1 | 0.3217 | 18.81 | 0.0002 |
| $D$ | 0.0935 | 1 | 0.0935 | 5.47 | 0.0280 |
| $AD$ | 1.1197 | 1 | 1.1197 | 65.48 | <0.0001 |
| Bloques | 0.0201 | 3 | 0.0067 | | |
| Error | 0.4099 | 24 | 0.0171 | | |
| Total | 2.6389 | 31 | | | |

El efecto de bloques es pequeño: los areómetros no difieren mucho.

**Diagnósticos.** La gráfica normal de residuales (fig. 8-20) sugiere colas algo más gruesas que las normales; podrían considerarse otras transformaciones.

**Conclusiones.** Interacción $AD$ (fig. 8-21): con el fabricante 1 ($D^-$) la respuesta crece mucho al pasar $A$ de bajo a alto; con el fabricante 2 ($D^+$) casi no cambia. Proyección en cuatro réplicas de un $2^3$ en $A,B,D$ (fig. 8-22); promedios de $\ln(\cdot)$ en los vértices:

| $A$ | $B$ | $D$ | Promedio |
|---|---|---|---|
| 0 | 0 | 1 | 0.9595 |
| 15 | 0 | 1 | 1.745 |
| 0 | 15 | 1 | 0.8280 |
| 15 | 15 | 1 | 1.370 |
| 0 | 0 | 2 | 1.504 |
| 15 | 0 | 2 | 1.310 |
| 0 | 15 | 2 | 1.247 |
| 15 | 15 | 2 | 1.273 |

Mejor condición: $A$ bajo (0), $B$ alto (0.015) y $D$ bajo (fabricante 1).

---

## 8-5 Diseños de resolución III

### Diseños saturados

- Se pueden construir diseños de resolución III para investigar hasta $k=N-1$ factores en $N$ corridas, con $N$ múltiplo de 4. Si $k=N-1$ el diseño está **saturado**.
- Casos importantes con $N$ potencia de 2: 4 corridas para hasta 3 factores ($2^{3-1}_{\mathrm{III}}$), 8 corridas para hasta 7 ($2^{7-4}_{\mathrm{III}}$), 16 corridas para hasta 15 ($2^{15-11}_{\mathrm{III}}$), 32 corridas para hasta 31 ($2^{31-26}_{\mathrm{III}}$).

### El $2^{7-4}_{\mathrm{III}}$ (fracción 1/16 del $2^7$)

Básico $2^3$ en $A,B,C$; $D=AB$, $E=AC$, $F=BC$, $G=ABC$. Generadores: $I=ABD$, $I=ACE$, $I=BCF$, $I=ABCG$ (tabla 8-19):

| Corrida | $A$ | $B$ | $C$ | $D=AB$ | $E=AC$ | $F=BC$ | $G=ABC$ | Tratamiento |
|---|---|---|---|---|---|---|---|---|
| 1 | − | − | − | + | + | + | − | $def$ |
| 2 | + | − | − | − | − | + | + | $afg$ |
| 3 | − | + | − | − | + | − | + | $beg$ |
| 4 | + | + | − | + | − | − | − | $abd$ |
| 5 | − | − | + | + | − | − | + | $cdg$ |
| 6 | + | − | + | − | + | − | − | $ace$ |
| 7 | − | + | + | − | − | + | − | $bcf$ |
| 8 | + | + | + | + | + | + | + | $abcdefg$ |

**Relación de definición completa** (generadores multiplicados de dos en dos, de tres en tres y los cuatro a la vez; 15 palabras):

$$I = ABD = ACE = BCF = ABCG = BCDE = ACDF = CDG = ABEF = BEG = AFG = DEF = ADEG = CEFG = BDFG = ABCDEFG$$

Cada efecto tiene 15 alias. Ejemplo:

$$B = AD = ABCE = CF = ACG = CDE = ABCDF = BCDG = AEF = EG = ABFG = BDEF = ABDEG = BCEFG = DFG = ACDEFG$$

Hay 16 diseños en la familia (los 16 arreglos de signos en $I=\pm ABD$, $I=\pm ACE$, $I=\pm BCF$, $I=\pm ABCG$); todos positivos = fracción principal.

**Alias simplificados** (despreciando interacciones de 3+ factores), **ec. 8-1** — coinciden con la Tabla XII(h):

$$
\begin{aligned}
\ell_A &\to A+BD+CE+FG\\
\ell_B &\to B+AD+CF+EG\\
\ell_C &\to C+AE+BF+DG\\
\ell_D &\to D+AB+CG+EF\\
\ell_E &\to E+AC+BG+DF\\
\ell_F &\to F+BC+AG+DE\\
\ell_G &\to G+CD+BE+AF
\end{aligned}
$$

### Diseños para menos factores por eliminación de columnas

- Del $2^{7-4}_{\mathrm{III}}$ saturado se obtienen diseños de resolución III para menos de 7 factores en 8 corridas **eliminando columnas**. Eliminando $G$ queda un $2^{6-3}_{\mathrm{III}}$ (tabla 8-20: $D=AB$, $E=AC$, $F=BC$; tratamientos $def, af, be, abd, cd, ace, bcf, abcdef$).
- **Regla:** al eliminar $d$ factores, la nueva relación de definición está formada por las palabras de la original que **no contienen ninguna de las letras eliminadas**. Para el $2^{6-3}_{\mathrm{III}}$:

$$I = ABD = ACE = BCF = BCDE = ACDF = ABEF = DEF$$

- Hay que cuidar qué columnas se eliminan: quitando $B, D, F, G$ queda un diseño de tres factores en ocho corridas que equivale a **dos réplicas de un $2^{3-1}$**; probablemente se preferiría un $2^3$ completo en $A, C, E$.
- $2^{15-11}_{\mathrm{III}}$: básico $2^4$ en $A,B,C,D$ y 11 factores nuevos igualados a las interacciones de dos, tres y cuatro factores de los cuatro originales. Cada uno de los 15 principales es alias de siete 2fi.

### Ensamblaje secuencial de fracciones: doblez (plegado, *fold over*)

Combinando fracciones en las que se han invertido ciertos signos se aíslan de forma sistemática los efectos de interés. La estructura de alias de una fracción con los signos de uno o más factores invertidos se obtiene haciendo el cambio de signo correspondiente en los alias de la fracción original.

#### Doblez de un solo factor

Junto a la fracción principal del $2^{7-4}_{\mathrm{III}}$ se corre una segunda con los signos de **solo la columna $D$** invertidos (columna $D$ de la segunda fracción: `− + + − − + + −`). La segunda fracción estima (**ec. 8-2**):

$$
\begin{aligned}
\ell'_A &\to A-BD+CE+FG\\
\ell'_B &\to B-AD+CF+EG\\
\ell'_C &\to C+AE+BF-DG\\
\ell'_D &\to D-AB-CG-EF \quad\text{(es decir, } \ell'_{-D} \to -D+AB+CG+EF)\\
\ell'_E &\to E+AC+BG-DF\\
\ell'_F &\to F+BC+AG-DE\\
\ell'_G &\to G-CD+BE+AF
\end{aligned}
$$

| $i$ | De $\tfrac12(\ell_i+\ell'_i)$ | De $\tfrac12(\ell_i-\ell'_i)$ |
|---|---|---|
| $A$ | $A+CE+FG$ | $BD$ |
| $B$ | $B+CF+EG$ | $AD$ |
| $C$ | $C+AE+BF$ | $DG$ |
| $D$ | $D$ | $AB+CG+EF$ |
| $E$ | $E+AC+BG$ | $DF$ |
| $F$ | $F+BC+AG$ | $DE$ |
| $G$ | $G+BE+AF$ | $CD$ |

**Regla general:** si a un fraccionado de resolución III o mayor se le agrega una fracción con los signos de **un solo factor** invertidos, el diseño combinado estima limpios el **efecto principal de ese factor y todas sus interacciones de dos factores**.

#### Doblez completo (reflexión)

Se agrega una segunda fracción con los signos de **todos** los factores invertidos. Rompe los vínculos de alias entre efectos principales e interacciones de dos factores: el **diseño combinado** estima todos los efectos principales libres de 2fi. Al invertir todos los signos, en realidad se cambian los signos de los **generadores con número impar de letras**.

### Ejemplo 8-7 — Doblez completo de un $2^{7-4}_{\mathrm{III}}$, tiempo de enfoque del ojo (págs. 340–343)

**Contexto.** Experimento de desempeño humano; respuesta = tiempo de enfoque del ojo (ms). Factores: $A$ = agudeza visual, $B$ = distancia del objetivo al ojo, $C$ = forma del objetivo, $D$ = nivel de iluminación, $E$ = tamaño del objetivo, $F$ = densidad, $G$ = sujeto. Se sospecha que solo unos pocos importan y que las interacciones de orden alto son despreciables.

**Primera fracción** (tabla 8-21; diseño de la tabla 8-19, corridas en orden aleatorio). Tiempos en orden de corridas 1–8: 85.5, 75.1, 93.2, 145.4, 83.7, 77.6, 95.0, 141.8.

Ejemplo de cálculo: $\ell_A=\tfrac14(-85.5+75.1-93.2+145.4-83.7+77.6-95.0+141.8)=20.63$.

| Estimación | Estima |
|---|---|
| $\ell_A = 20.63$ | $A+BD+CE+FG$ |
| $\ell_B = 38.38$ | $B+AD+CF+EG$ |
| $\ell_C = -0.28$ | $C+AE+BF+DG$ |
| $\ell_D = 28.88$ | $D+AB+CG+EF$ |
| $\ell_E = -0.28$ | $E+AC+BG+DF$ |
| $\ell_F = -0.63$ | $F+BC+AG+DE$ |
| $\ell_G = -2.43$ | $G+CD+BE+AF$ |

**Ambigüedad.** Los tres mayores son $\ell_A$, $\ell_B$, $\ell_D$. Interpretación más simple: $A$, $B$, $D$ activos. Pero también son lógicas: $A$, $B$ y $AB$; o $B$, $D$ y $BD$; o $A$, $D$ y $AD$. Como $ABD$ es palabra de la relación de definición, el diseño **no** se proyecta en un $2^3$ completo en $A,B,D$ sino en **dos réplicas de un $2^{3-1}_{\mathrm{III}}$** (fig. 8-23), donde $A=BD$, $B=AD$, $D=AB$. (Mala suerte en la asignación: si la iluminación se hubiera asignado a $C$ en vez de $D$ se habría proyectado en un $2^3$ completo.)

**Segunda fracción: doblez completo** (tabla 8-22; todos los signos invertidos, de modo que $D=-AB$, $E=-AC$, $F=-BC$, $G=ABC$). Corridas y tiempos: $abcg$ 91.3, $bcde$ 136.7, $acdf$ 82.4, $cefg$ 73.4, $abef$ 94.1, $bdfg$ 143.8, $adeg$ 87.3, $(1)$ 71.9.

| Estimación | Estima |
|---|---|
| $\ell'_A = -17.68$ | $A-BD-CE-FG$ |
| $\ell'_B = 37.73$ | $B-AD-CF-EG$ |
| $\ell'_C = -3.33$ | $C-AE-BF-DG$ |
| $\ell'_D = 29.88$ | $D-AB-CG-EF$ |
| $\ell'_E = 0.53$ | $E-AC-BG-DF$ |
| $\ell'_F = 1.63$ | $F-BC-AG-DE$ |
| $\ell'_G = 2.68$ | $G-CD-BE-AF$ |

**Diseño combinado:**

| $i$ | $\tfrac12(\ell_i+\ell'_i)$ | $\tfrac12(\ell_i-\ell'_i)$ |
|---|---|---|
| $A$ | $A = 1.48$ | $BD+CE+FG = 19.15$ |
| $B$ | $B = 38.05$ | $AD+CF+EG = 0.33$ |
| $C$ | $C = -1.80$ | $AE+BF+DG = 1.53$ |
| $D$ | $D = 29.38$ | $AB+CG+EF = -0.50$ |
| $E$ | $E = 0.13$ | $AC+BG+DF = -0.40$ |
| $F$ | $F = 0.50$ | $BC+AG+DE = -1.53$ (así impreso; con los datos del libro $\tfrac12(-0.63-1.63) = -1.13$) |
| $G$ | $G = 0.13$ | $CD+BE+AF = -2.55$ |

**Conclusión.** Los dos efectos mayores son $B$ y $D$; el tercero es $BD+CE+FG$, que razonablemente se atribuye a $BD$. Lo que en la primera fracción parecía el efecto de $A$ era la interacción $BD$. El analista siguió experimentando con $B$ (distancia) y $D$ (iluminación), con $A, C, E, F$ en ajustes estándar, y usó los sujetos como bloques.

### Relación de definición de un diseño de doblez

Cada fracción por separado tiene $L+U$ palabras usadas como generadores: $L$ palabras con el **mismo** signo en ambas fracciones y $U$ con signo **distinto**. El diseño combinado tiene $L+U-1$ generadores:

- las $L$ palabras de mismo signo, y
- $U-1$ palabras formadas por **productos pares independientes** de las palabras de signo distinto (productos tomados de dos en dos, de cuatro en cuatro, etc.).

**Ilustración (ejemplo 8-7).** Primera fracción: $I=ABD$, $I=ACE$, $I=BCF$, $I=ABCG$. Segunda: $I=-ABD$, $I=-ACE$, $I=-BCF$, $I=ABCG$. Aquí $L=1$, $U=3$, $L+U=4$. Generadores del combinado: $ABCG$ (mismo signo) y dos productos pares independientes, p. ej. $(ABD)(ACE)=BCDE$ y $(ABD)(BCF)=ACDF$. Relación de definición completa del diseño combinado:

$$I = ABCG = BCDE = ACDF = ADEG = BDFG = ABEF = CEFG$$

Es un $2^{7-3}_{\mathrm{IV}}$: el doblez completo de un resolución III produce un resolución IV.

### Diseños de Plackett-Burman

- Fraccionados de dos niveles para estudiar $k=N-1$ variables en $N$ corridas, con $N$ **múltiplo de 4**. Si $N$ es potencia de 2 son idénticos a los $2^{k-p}_{\mathrm{III}}$ saturados ya vistos. Interesan para $N=12, 20, 24, 28, 36$. Como no pueden representarse como cubos se llaman **diseños no geométricos**.

**Renglones generadores (tabla 8-23):**

| $k$ | $N$ | Renglón |
|---|---|---|
| 11 | 12 | `+ + − + + + − − − + −` |
| 19 | 20 | `+ + − − + + + + − + − + − − − − + + −` |
| 23 | 24 | `+ + + + + − + − + + − − + + − − + − + − − − −` |
| 35 | 36 | `− + − + + + − − − + + + + + − + + + − − + − − − − + − + − + + − − + −` |

**Construcción para $N=12, 20, 24, 36$:**

1. Escribir el renglón apropiado como primera columna (o primer renglón).
2. Generar la segunda columna (o renglón) desplazando cíclicamente los elementos una posición hacia abajo (o hacia la derecha) y colocando el último elemento en la primera posición.
3. Repetir hasta generar la columna (o renglón) $k$.
4. Agregar un renglón de signos negativos.

**Construcción para $N=28$ ($k=27$):** tres bloques $X$, $Y$, $Z$ de $9\times 9$ signos, dispuestos como

$$\begin{matrix} X & Y & Z\\ Z & X & Y\\ Y & Z & X\end{matrix}$$

más un renglón de signos negativos. Bloques (renglones de arriba abajo):

| $X$ | $Y$ | $Z$ |
|---|---|---|
| `+ − + + + + − − −` | `− + − − − + − − +` | `+ + − + − + + − +` |
| `+ + − + + + − − −` | `− − + + − − + − −` | `− + + + + − + + −` |
| `− + + + + + − − −` | `+ − − − + − − + −` | `+ − + − + + − + +` |
| `− − − + − + + + +` | `− − + − + − − − +` | `+ − + + + − + − +` |
| `− − − + + − + + +` | `+ − − − − + + − −` | `+ + − − + + + + −` |
| `− − − − + + + + +` | `− + − + − − − + −` | `− + + + − + − + +` |
| `+ + + − − − + − +` | `− − + − − + − + −` | `+ − + + − + + + −` |
| `+ + + − − − + + −` | `+ − − + − − − − +` | `+ + − + + − − + +` |
| `+ + + − − − − + +` | `− + − − + − + − −` | `− + + − + + + − +` |

El diseño de $N=12$, $k=11$ construido usando el renglón como **columna** aparece en la tabla 8-24; el del ejemplo 8-8 (tabla 8-25) usa el renglón como **renglón**.

**Estructura de alias compleja (alias parciales).** En los diseños no geométricos los alias son muy intrincados. En el de 12 corridas, cada efecto principal es **alias parcial** de todas las 2fi en las que no interviene: $AB$ es alias parcial de los nueve principales $C, D, \dots, K$, y cada principal es alias parcial de 45 interacciones de dos factores. En diseños mayores es aún más complejo. **Advertencia del autor: usar estos diseños con mucho cuidado.**

**Proyección.** Las propiedades proyectivas no son especialmente atractivas:

- El de 12 corridas se proyecta en tres réplicas de un $2^2$ completo en cualesquiera dos factores.
- En tres factores, la proyección es un $2^3$ completo **más** un $2^{3-1}_{\mathrm{III}}$ (fig. 8-24a). Por eso el Plackett-Burman de resolución III tiene **proyectividad 3**: se pliega en un factorial completo en cualquier subconjunto de tres factores. Un $2^{k-p}_{\mathrm{III}}$ solo tiene proyectividad 2.
- Las proyecciones en tres y cuatro factores (fig. 8-24b) **no son balanceadas**.

### Ejemplo 8-8 — Dificultades del Plackett-Burman con datos simulados (págs. 345–346)

**Modelo verdadero simulado:**

$$y = 200 + 8x_1 + 10x_2 + 12x_4 - 12x_1x_2 + 9x_1x_4 + \varepsilon,\qquad \varepsilon \sim \mathrm{NID}(0, 9)$$

Tres principales activos ($A$, $B$, $D$) y dos interacciones ($AB$, $AD$) entre $k=11$ factores ($A, B, \dots, H, J, K, L$).

**Diseño (tabla 8-25).** Plackett-Burman de 12 corridas: renglón 1 = `+ + − + + + − − − + −`; cada renglón siguiente es el anterior desplazado una posición a la derecha; renglón 12 todo negativo. Respuestas (corridas 1–12): 231, 207, 230, 217, 175, 176, 183, 185, 181, 220, 229, 168.

**Efectos estimados (tabla 8-26):**

| Variable | Coeficiente | Efecto | SS |
|---|---|---|---|
| Promedio global | 200.167 | | |
| $A$ | 6.333 | 12.667 | 481.333 |
| $B$ | 6.667 | 13.333 | 533.333 |
| $C$ | 6.833 | 12.667 (así impreso; con los datos es 13.667, consistente con el coeficiente y la SS) | 560.333 |
| $D$ | 17.000 | 34.000 | 3468.000 |
| $E$ | 6.833 | 13.667 | 560.333 |
| $F$ | 0.500 | 1.000 | 3.000 |
| $G$ | −1.167 | −2.333 | 16.333 |
| $H$ | 1.500 | 3.000 | 27.000 |
| $J$ | −6.333 | −12.667 | 481.333 |
| $K$ | −5.833 | −11.667 | 408.333 |
| $L$ | −0.167 | −0.333 | 0.333 |

**Conclusión.** Aparecen **siete** efectos grandes ($A, B, C, D, E, J, K$) cuando solo hay tres principales activos: las interacciones $AB$ y $AD$ contaminan parcialmente a los demás principales y no es evidente que algunos de esos efectos son en realidad interacciones. Un doblez resolvería en general los principales, pero suele dejar incertidumbre sobre las interacciones.

**Recomendación.** Si la elección está entre un geométrico $2^{11-7}_{\mathrm{III}}$ de 16 corridas y un Plackett-Burman de 12 que quizá haya que doblar (24 corridas), el geométrico puede ser mejor elección (Montgomery, Borror y Stanley). Bajo ciertas condiciones los alias de un no geométrico se pueden desenredar con técnicas de construcción de modelos de regresión (Hamada y Wu).

---

## 8-6 Diseños de resolución IV y V

### Resolución IV

- Un $2^{k-p}$ es de resolución IV si los principales están separados de las 2fi y algunas 2fi son alias entre sí. Si se suprimen las interacciones de 3+ factores, los principales se estiman directamente. Ejemplos: $2^{6-2}_{\mathrm{IV}}$ (tabla 8-10) y el $2^{7-3}_{\mathrm{IV}}$ que resulta de combinar las dos fracciones del ejemplo 8-7.
- **Regla de corridas mínimas:** todo $2^{k-p}_{\mathrm{IV}}$ debe tener **al menos $2k$ corridas**. Los de resolución IV con exactamente $2k$ corridas se llaman **diseños mínimos**.

**Obtención por doblado de un resolución III.** Al doblar un $2^{k-p}_{\mathrm{III}}$ (segunda fracción con todos los signos invertidos), los signos $+$ de la columna $I$ de la primera fracción se pueden cambiar a $-$ en la segunda y asociar el factor $(k+1)$-ésimo a esa columna. Resultado: un $2^{k+1-p}_{\mathrm{IV}}$. Tabla 8-27 (del $2^{3-1}_{\mathrm{III}}$ con $I=ABC$ al $2^{4-1}_{\mathrm{IV}}$ con $I=ABCD$):

| $D$ (columna $I$) | $A$ | $B$ | $C$ | |
|---|---|---|---|---|
| + | − | − | + | Diseño original $2^{3-1}_{\mathrm{III}}$ |
| + | + | − | − | |
| + | − | + | − | |
| + | + | + | + | |
| − | + | + | − | Segunda fracción, signos intercambiados |
| − | − | + | + | |
| − | + | − | + | |
| − | − | − | − | |

### Doblez de diseños de resolución IV

Objetivos posibles (Montgomery y Runger): (1) romper tantas cadenas de alias de 2fi como sea posible; (2) romper las 2fi de una cadena específica; (3) romper las 2fi que incluyen un factor específico.

**Procedimiento estándar:** correr una segunda fracción en la que se invierte el signo de **todos los generadores con número impar de letras** (equivale a invertir todos los factores).

- **$2^{6-2}_{\mathrm{IV}}$ del ejemplo 8-4:** generadores $I=ABCE$, $I=BCDF$ (como $E=ABC$, $F=BCD$ tienen tres letras, cambian de signo). Segunda fracción: $I=-ABCE$, $I=-BCDF$. Generador único del diseño combinado: $I=ADEF$. Sigue siendo resolución IV, pero las únicas 2fi con alias son $AD=EF$, $AE=DF$, $AF=DE$; todas las demás se estiman.
- **$2^{8-3}_{\mathrm{IV}}$ (32 corridas):** generadores $I=ABCF$, $I=ABDG$, $I=BCDEH$ (Tabla XII(m): seis pares de 2fi aliadas y un grupo de tres). Segunda fracción: $I=-ABCF$, $I=-ABDG$, $I=BCDEH$. Diseño combinado: generadores $I=CDFG$, $I=BCDEH$; relación completa

$$I = CDFG = BCDEH = BEFGH$$

  Resolución IV; solo quedan aliadas $CD=FG$, $CF=DG$, $CG=DF$.

**Advertencias:**

- Doblar un resolución III **garantiza** un combinado de resolución IV (principales separados de las 2fi).
- Doblar un resolución IV **no necesariamente** separa todas las 2fi: si la fracción original tiene alguna cadena con más de dos 2fi, el doblez no las separa completamente (ocurre en los dos ejemplos anteriores).
- Montgomery y Runger dan una tabla de dobleces recomendados para fracciones de resolución IV con $6\le k\le 10$.

### Resolución V

- Principales y 2fi no tienen como alias otros principales ni otras 2fi: se estiman de forma única todos los principales y todas las 2fi si las interacciones de 3+ factores son despreciables. La palabra más corta de la relación de definición debe tener cinco letras.
- Ejemplos: $2^{5-1}$ con $I=ABCDE$; $2^{8-2}_{\mathrm{V}}$ con $I=ABCDG$ e $I=ABEFH$.
- Los resolución V estándar son grandes cuando $k$ es moderadamente grande; por eso interesan las **fracciones irregulares de resolución V**, disponibles para $4\le k\le 9$: 12 corridas para $k=4$ (problema 8-22), **24 corridas para $k=5$** (tabla 8-28), 48 corridas para $k=6, 7, 8$ y 96 para $k=9$. Design-Expert las incluye.

**Tabla 8-28 — Fracción irregular de resolución V, 5 factores en 24 corridas.** Estructura: tres cuartas partes del $2^5$; dentro de cada combinación de $(D,E)$ aparecen 6 de las 8 combinaciones de $A,B,C$:

| $(D,E)$ | Combinaciones de $(A,B,C)$ presentes, en el orden de la tabla |
|---|---|
| $(-,-)$ | `−−−`, `−+−`, `++−`, `−−+`, `+−+`, `−++` |
| $(+,-)$ | `−−−`, `+−−`, `++−`, `+−+`, `−++`, `+++` |
| $(-,+)$ | `−−−`, `+−−`, `++−`, `+−+`, `−++`, `+++` |
| $(+,+)$ | `−−−`, `−+−`, `++−`, `−−+`, `+−+`, `−++` |

Permite estimar los 5 principales y las 10 2fi (interacciones de 3+ factores despreciables).

### Doblez parcial (semidoblez)

Un doblez completo de un diseño de resolución IV o V suele ser innecesario: en general solo hay una o dos (o muy pocas) interacciones aliadas de interés potencial, y sus alias se pueden separar agregando un **número pequeño de corridas** a la fracción original. Esta técnica se denomina a veces **doblez parcial**. El libro remite al ejemplo 10-5 y al material suplementario del capítulo; aquí no se desarrolla.

---

## 8-7 Resumen

- El $2^{k-p}$ es la herramienta de tamizado para identificar rápida y eficazmente el subconjunto de factores activos y obtener alguna información sobre interacciones.
- La **proyección** permite examinar los factores activos con más detalle.
- El **ensamblaje secuencial por doblez** es una manera muy eficaz de obtener información adicional sobre las interacciones señaladas como posibles en un experimento inicial.

**Tabla 8-29 — Diseños útiles del sistema $2^{k-p}$** (las celdas son el número de factores del experimento):

| Tipo de diseño | 4 corridas | 8 corridas | 16 corridas | 32 corridas |
|---|---|---|---|---|
| Factorial completo | 2 | 3 | 4 | 5 |
| Fracción un medio | 3 | 4 | 5 | 6 |
| Fracción de resolución IV | — | 4 | 6–8 | 7–16 |
| Fracción de resolución III | 3 | 5–7 | 9–15 | 17–31 |

Ejemplo de lectura: el diseño de 16 corridas es un factorial completo para 4 factores, una fracción un medio para 5, una fracción de resolución IV para 6 a 8 y una de resolución III para 9 a 15.

**8-8 Problemas (hojeado, no resumido).** Problemas 8-1 a 8-32: fracciones un medio de experimentos del cap. 6; $2^{5-2}$ y sus dobleces (8-4, 8-5, 8-19); efectos de dispersión con réplicas (resortes de hojas, 8-7 y 8-9; combadura de sustratos, 8-24; recubrimiento fotoprotector, 8-25); $2^{8-4}_{\mathrm{IV}}$ de la cata de vino (8-26); aceite de cacahuate (8-27); respuestas en proporción y conteo con transformaciones arcsen$\sqrt{\hat p}$, $\sqrt c$ y sus modificaciones de Freeman-Tukey (8-28, 8-29); fracción irregular de 12 corridas del $2^4$ (8-22) y de 24 corridas del $2^5$ (8-32).

---

## Recetario: procedimiento general, fórmulas y advertencias

### Procedimiento para planear y analizar un $2^{k-p}$

1. **Definir objetivo y supuestos:** cuántos factores, qué interacciones se está dispuesto a despreciar. De ahí sale la resolución requerida (III: solo principales, tamizado puro; IV: principales limpios y 2fi en cadenas; V: principales y 2fi limpios).
2. **Elegir el diseño** en la tabla 8-14 (máxima resolución, aberración mínima) y revisar sus alias en la Tabla XII.
3. **Asignar factores a columnas:** los que se creen importantes o que pueden interactuar, a las columnas del diseño básico o de modo que sus 2fi queden en cadenas distintas; cuidar que el subconjunto de factores probablemente activos no sea una palabra de la relación de definición (para que la proyección sea un factorial completo).
4. **Construir:** diseño básico completo en $k-p$ factores + columnas generadas. Si hace falta, **bloquear** confundiendo cadenas de orden alto (Tabla XII).
5. **Aleatorizar** el orden de corridas (dentro de bloques, si los hay) y correr.
6. **Estimar** los $2^{k-p}-1$ efectos (con sus alias): $\ell_i = \text{Contraste}_i/(N/2)$.
7. **Identificar efectos activos:** gráfica de probabilidad normal de los efectos; interpretar cadenas con navaja de Ockham, jerarquía y conocimiento del proceso.
8. **ANOVA** del modelo reducido (los efectos descartados forman el error) y **modelo de regresión** en variables codificadas ($\hat\beta = \ell/2$).
9. **Diagnósticos:** gráfica normal de residuales, residuales contra predichos y contra cada factor; considerar transformaciones (p. ej. logaritmo cuando la respuesta es una desviación estándar).
10. **Efectos de dispersión:** $F_i^*=\ln[S^2(i^+)/S^2(i^-)]$ sobre los residuales, graficados en probabilidad normal.
11. **Proyectar** en los factores activos (gráficas de cubo, de interacción).
12. **Seguimiento:** corrida de confirmación; fracción alterna, doblez completo, doblez de un factor o doblez parcial para resolver ambigüedades; o cualquiera de las opciones de la fig. 8-11.

### Fórmulas y reglas clave

| Concepto | Fórmula / regla |
|---|---|
| Corridas | $N = 2^{k-p}$ |
| Palabras de la relación de definición | $2^p-1$ ($p$ generadores + $2^p-p-1$ interacciones generalizadas) |
| Alias de cada efecto | $2^p-1$; se obtienen multiplicando el efecto por cada palabra (letras al cuadrado $= I$) |
| Efectos estimables | $2^{k-p}-1$ cadenas de alias |
| Resolución | longitud de la palabra más corta |
| Aberración mínima | entre diseños de máxima resolución, el de menos palabras de longitud mínima |
| Estimación de efectos | $\ell_i = 2(\text{Contraste}_i)/N$ |
| Coeficiente de regresión | $\hat\beta_i = \ell_i/2$; $\hat\beta_0=\bar y$ |
| Suma de cuadrados (1 gl) | $SS_i = (\text{Contraste}_i)^2/N = N\ell_i^2/4$ |
| Combinar fracciones | $\tfrac12(\ell_i+\ell'_i)$ y $\tfrac12(\ell_i-\ell'_i)$ |
| Proyección | resolución $R$ ⇒ factorial completo en cualquier subconjunto de $R-1$ factores; en general, completo en todo subconjunto de $r\le k-p$ factores que no contenga una palabra |
| Saturación (resolución III) | $k=N-1$ factores en $N$ corridas |
| Mínimo para resolución IV | $N \ge 2k$ |
| Doblez completo | invierte todos los signos = cambia el signo de los generadores con número impar de letras; III → IV |
| Doblez de un factor | aísla ese principal y todas sus 2fi |
| Relación de definición del doblez | $L$ palabras de igual signo + $U-1$ productos pares independientes de las de signo distinto |
| Eliminar factores | quedan las palabras que no contienen las letras eliminadas |
| Bloques | bloque principal: $L = \sum \alpha_i x_i = 0 \pmod 2$ para la interacción confundida |
| Efecto de dispersión | $F_i^* = \ln[S^2(i^+)/S^2(i^-)]$, aprox. normal con media 0 si no hay efecto |

### Advertencias del autor

- Las conclusiones de un fraccionado son **tentativas**: casi siempre hay explicaciones alternativas con interacciones aliadas; confirmar.
- Al elegir generadores, vigilar que los efectos potencialmente importantes no queden aliados entre sí; no sacrificar resolución innecesariamente.
- La asignación de factores a columnas importa (ejemplo 8-7: $ABD$ era una palabra y la proyección en $A,B,D$ no fue un factorial completo).
- Los residuales solo informan sobre dispersión si el modelo de localización es correcto.
- En la jerarquía de modelos se conservan los principales de las interacciones incluidas (ejemplo 8-6: $D$ entra por $AD$).
- Plackett-Burman no geométricos: alias parciales muy complejos; usar con mucho cuidado y preferir el geométrico cuando la diferencia de corridas es pequeña.
- El doblez de un resolución IV no siempre separa todas las 2fi; a menudo basta un doblez parcial.

---

## Tabla XII del apéndice — Relaciones de alias de los diseños $2^{k-p}$ con $k \le 15$ y $n \le 64$

> Montgomery, apéndice, págs. 663–679. Contiene 26 diseños, rotulados (a)–(z), que son los de la tabla 8-14 con $n \le 64$ (salvo el $2^{11-5}_{\mathrm{IV}}$ de 64 corridas, que no aparece en el apéndice). No incluye los de 128 corridas.

**Cómo leer esta sección.** Los generadores, la resolución y los arreglos de bloques son los impresos en el libro. La relación de definición y las cadenas de alias se **recalcularon** a partir de los generadores (multiplicación módulo 2) y se cotejaron con lo impreso; las palabras y los alias dentro de cada cadena aparecen aquí ordenados por longitud y alfabéticamente, no en el orden del libro. Todos los generadores están con signo $+$ (fracción principal). Los arreglos de bloques se verificaron: todos los efectos listados en una misma igualdad pertenecen a la misma cadena de alias, y ninguna cadena confundida contiene un efecto principal.

- Diseños de **≤ 32 corridas**: alias de los efectos principales (hasta orden 2 en resolución III; hasta orden 3 en resolución IV) y todas las cadenas de interacciones de dos factores.
- Diseños de **64 corridas**: generadores, relación de definición, resolución y resumen de qué queda aliado.
- "Bloques": interacción (con sus alias) que el libro recomienda confundir; para 4 bloques se dan las tres cadenas confundidas (dos independientes y su interacción generalizada).

**Resumen de los 26 diseños:**

| Rótulo | Diseño | Factores | Corridas | Resolución | Generadores |
|---|---|---|---|---|---|
| (a) | $2^{3-1}_{\mathrm{III}}$ | 3 | 4 | III | $C = AB$ |
| (b) | $2^{4-1}_{\mathrm{IV}}$ | 4 | 8 | IV | $D = ABC$ |
| (c) | $2^{5-2}_{\mathrm{III}}$ | 5 | 8 | III | $D = AB$, $E = AC$ |
| (d) | $2^{5-1}_{\mathrm{V}}$ | 5 | 16 | V | $E = ABCD$ |
| (e) | $2^{6-3}_{\mathrm{III}}$ | 6 | 8 | III | $D = AB$, $E = AC$, $F = BC$ |
| (f) | $2^{6-2}_{\mathrm{IV}}$ | 6 | 16 | IV | $E = ABC$, $F = BCD$ |
| (g) | $2^{6-1}_{\mathrm{VI}}$ | 6 | 32 | VI | $F = ABCDE$ |
| (h) | $2^{7-4}_{\mathrm{III}}$ | 7 | 8 | III | $D = AB$, $E = AC$, $F = BC$, $G = ABC$ |
| (i) | $2^{7-3}_{\mathrm{IV}}$ | 7 | 16 | IV | $E = ABC$, $F = BCD$, $G = ACD$ |
| (j) | $2^{7-2}_{\mathrm{IV}}$ | 7 | 32 | IV | $F = ABCD$, $G = ABDE$ |
| (k) | $2^{7-1}_{\mathrm{VII}}$ | 7 | 64 | VII | $G = ABCDEF$ |
| (l) | $2^{8-4}_{\mathrm{IV}}$ | 8 | 16 | IV | $E = BCD$, $F = ACD$, $G = ABC$, $H = ABD$ |
| (m) | $2^{8-3}_{\mathrm{IV}}$ | 8 | 32 | IV | $F = ABC$, $G = ABD$, $H = BCDE$ |
| (n) | $2^{8-2}_{\mathrm{V}}$ | 8 | 64 | V | $G = ABCD$, $H = ABEF$ |
| (o) | $2^{9-5}_{\mathrm{III}}$ | 9 | 16 | III | $E = ABC$, $F = BCD$, $G = ACD$, $H = ABD$, $J = ABCD$ |
| (p) | $2^{9-4}_{\mathrm{IV}}$ | 9 | 32 | IV | $F = BCDE$, $G = ACDE$, $H = ABDE$, $J = ABCE$ |
| (q) | $2^{9-3}_{\mathrm{IV}}$ | 9 | 64 | IV | $G = ABCD$, $H = ACEF$, $J = CDEF$ |
| (r) | $2^{10-6}_{\mathrm{III}}$ | 10 | 16 | III | $E = ABC$, $F = BCD$, $G = ACD$, $H = ABD$, $J = ABCD$, $K = AB$ |
| (s) | $2^{10-5}_{\mathrm{IV}}$ | 10 | 32 | IV | $F = ABCD$, $G = ABCE$, $H = ABDE$, $J = ACDE$, $K = BCDE$ |
| (t) | $2^{10-4}_{\mathrm{IV}}$ | 10 | 64 | IV | $G = BCDF$, $H = ACDF$, $J = ABDE$, $K = ABCE$ |
| (u) | $2^{11-7}_{\mathrm{III}}$ | 11 | 16 | III | $E = ABC$, $F = BCD$, $G = ACD$, $H = ABD$, $J = ABCD$, $K = AB$, $L = AC$ |
| (v) | $2^{11-6}_{\mathrm{IV}}$ | 11 | 32 | IV | $F = ABC$, $G = BCD$, $H = CDE$, $J = ACD$, $K = ADE$, $L = BDE$ |
| (w) | $2^{12-8}_{\mathrm{III}}$ | 12 | 16 | III | $E = ABC$, $F = ABD$, $G = ACD$, $H = BCD$, $J = ABCD$, $K = AB$, $L = AC$, $M = AD$ |
| (x) | $2^{13-9}_{\mathrm{III}}$ | 13 | 16 | III | $E = ABC$, $F = ABD$, $G = ACD$, $H = BCD$, $J = ABCD$, $K = AB$, $L = AC$, $M = AD$, $N = BC$ |
| (y) | $2^{14-10}_{\mathrm{III}}$ | 14 | 16 | III | $E = ABC$, $F = ABD$, $G = ACD$, $H = BCD$, $J = ABCD$, $K = AB$, $L = AC$, $M = AD$, $N = BC$, $O = BD$ |
| (z) | $2^{15-11}_{\mathrm{III}}$ | 15 | 16 | III | $E = ABC$, $F = ABD$, $G = ACD$, $H = BCD$, $J = ABCD$, $K = AB$, $L = AC$, $M = AD$, $N = BC$, $O = BD$, $P = CD$ |

### XII(a) $2^{3-1}_{\mathrm{III}}$ — 3 factores, fracción 1/2, 4 corridas, resolución III

- **Generadores:** $C = AB$.
- **Relación de definición** (1 palabra: 1 de 3 letras): $I = ABC$.
- **Alias de efectos principales** (hasta orden 2):

  - $A = BC$
  - $B = AC$
  - $C = AB$
- Grados de libertad: 3 = 3 (principales) + 0 (cadenas de 2 factores no ligadas a principales) + 0 (cadenas de orden ≥ 3).

### XII(b) $2^{4-1}_{\mathrm{IV}}$ — 4 factores, fracción 1/2, 8 corridas, resolución IV

- **Generadores:** $D = ABC$.
- **Relación de definición** (1 palabra: 1 de 4 letras): $I = ABCD$.
- **Alias de efectos principales** (hasta orden 3):

  - $A = BCD$
  - $B = ACD$
  - $C = ABD$
  - $D = ABC$
- **Cadenas de interacciones de dos factores** (se omiten alias de orden ≥ 3):

  - $AB = CD$
  - $AC = BD$
  - $AD = BC$
- Grados de libertad: 7 = 4 (principales) + 3 (cadenas de 2 factores no ligadas a principales) + 0 (cadenas de orden ≥ 3).

### XII(c) $2^{5-2}_{\mathrm{III}}$ — 5 factores, fracción 1/4, 8 corridas, resolución III

- **Generadores:** $D = AB$, $E = AC$.
- **Relación de definición** (3 palabras: 2 de 3 letras, 1 de 4 letras): $I = ABD = ACE = BCDE$.
- **Alias de efectos principales** (hasta orden 2):

  - $A = BD = CE$
  - $B = AD$
  - $C = AE$
  - $D = AB$
  - $E = AC$
- **Cadenas de interacciones de dos factores** (se omiten alias de orden ≥ 3):

  - $BC = DE$
  - $BE = CD$
- Grados de libertad: 7 = 5 (principales) + 2 (cadenas de 2 factores no ligadas a principales) + 0 (cadenas de orden ≥ 3).

### XII(d) $2^{5-1}_{\mathrm{V}}$ — 5 factores, fracción 1/2, 16 corridas, resolución V

- **Generadores:** $E = ABCD$.
- **Relación de definición** (1 palabra: 1 de 5 letras): $I = ABCDE$.
- **Efectos principales:** cada uno aliado solo con interacciones de 4 o más factores.
- **Interacciones de dos factores sin alias de orden ≤ 2** (10): $AB = CDE$, $AC = BDE$, $AD = BCE$, $AE = BCD$, $BC = ADE$, $BD = ACE$, $BE = ACD$, $CD = ABE$, $CE = ABD$, $DE = ABC$.
- Grados de libertad: 15 = 5 (principales) + 10 (cadenas de 2 factores no ligadas a principales) + 0 (cadenas de orden ≥ 3).
- **Bloques:** 2 bloques de 8: (la interacción no aparece impresa en esta edición).

### XII(e) $2^{6-3}_{\mathrm{III}}$ — 6 factores, fracción 1/8, 8 corridas, resolución III

- **Generadores:** $D = AB$, $E = AC$, $F = BC$.
- **Relación de definición** (7 palabras: 4 de 3 letras, 3 de 4 letras): $I = ABD = ACE = BCF = DEF = ABEF = ACDF = BCDE$.
- **Alias de efectos principales** (hasta orden 2):

  - $A = BD = CE$
  - $B = AD = CF$
  - $C = AE = BF$
  - $D = AB = EF$
  - $E = AC = DF$
  - $F = BC = DE$
- **Cadenas de interacciones de dos factores** (se omiten alias de orden ≥ 3):

  - $AF = BE = CD$
- Grados de libertad: 7 = 6 (principales) + 1 (cadenas de 2 factores no ligadas a principales) + 0 (cadenas de orden ≥ 3).

### XII(f) $2^{6-2}_{\mathrm{IV}}$ — 6 factores, fracción 1/4, 16 corridas, resolución IV

- **Generadores:** $E = ABC$, $F = BCD$.
- **Relación de definición** (3 palabras: 3 de 4 letras): $I = ABCE = ADEF = BCDF$.
- **Alias de efectos principales** (hasta orden 3):

  - $A = BCE = DEF$
  - $B = ACE = CDF$
  - $C = ABE = BDF$
  - $D = AEF = BCF$
  - $E = ABC = ADF$
  - $F = ADE = BCD$
- **Cadenas de interacciones de dos factores** (se omiten alias de orden ≥ 3):

  - $AB = CE$
  - $AC = BE$
  - $AD = EF$
  - $AE = BC = DF$
  - $AF = DE$
  - $BD = CF$
  - $BF = CD$
- Grados de libertad: 15 = 6 (principales) + 7 (cadenas de 2 factores no ligadas a principales) + 2 (cadenas de orden ≥ 3).
- **Bloques:** 2 bloques de 8: $ABD = CDE = ACF = BEF$.

### XII(g) $2^{6-1}_{\mathrm{VI}}$ — 6 factores, fracción 1/2, 32 corridas, resolución VI

- **Generadores:** $F = ABCDE$.
- **Relación de definición** (1 palabra: 1 de 6 letras): $I = ABCDEF$.
- **Efectos principales:** cada uno aliado solo con interacciones de 5 o más factores.
- **Interacciones de dos factores sin alias de orden ≤ 2** (15): $AB$, $AC$, $AD$, $AE$, $AF$, $BC$, $BD$, $BE$, $BF$, $CD$, $CE$, $CF$, $DE$, $DF$, $EF$.
- Grados de libertad: 31 = 6 (principales) + 15 (cadenas de 2 factores no ligadas a principales) + 10 (cadenas de orden ≥ 3).
- **Bloques:** 2 bloques de 16: $ABC = DEF$. 4 bloques de 8: $AB = CDEF$; $ACD = BEF$; $AEF = BCD$.

### XII(h) $2^{7-4}_{\mathrm{III}}$ — 7 factores, fracción 1/16, 8 corridas, resolución III

- **Generadores:** $D = AB$, $E = AC$, $F = BC$, $G = ABC$.
- **Relación de definición** (15 palabras: 7 de 3 letras, 7 de 4 letras, 1 de 7 letras): $I = ABD = ACE = AFG = BCF = BEG = CDG = DEF = ABCG = ABEF = ACDF = ADEG = BCDE = BDFG = CEFG = ABCDEFG$.
- **Alias de efectos principales** (hasta orden 2):

  - $A = BD = CE = FG$
  - $B = AD = CF = EG$
  - $C = AE = BF = DG$
  - $D = AB = CG = EF$
  - $E = AC = BG = DF$
  - $F = AG = BC = DE$
  - $G = AF = BE = CD$
- Grados de libertad: 7 = 7 (principales) + 0 (cadenas de 2 factores no ligadas a principales) + 0 (cadenas de orden ≥ 3).

### XII(i) $2^{7-3}_{\mathrm{IV}}$ — 7 factores, fracción 1/8, 16 corridas, resolución IV

- **Generadores:** $E = ABC$, $F = BCD$, $G = ACD$.
- **Relación de definición** (7 palabras: 7 de 4 letras): $I = ABCE = ABFG = ACDG = ADEF = BCDF = BDEG = CEFG$.
- **Alias de efectos principales** (hasta orden 3):

  - $A = BCE = BFG = CDG = DEF$
  - $B = ACE = AFG = CDF = DEG$
  - $C = ABE = ADG = BDF = EFG$
  - $D = ACG = AEF = BCF = BEG$
  - $E = ABC = ADF = BDG = CFG$
  - $F = ABG = ADE = BCD = CEG$
  - $G = ABF = ACD = BDE = CEF$
- **Cadenas de interacciones de dos factores** (se omiten alias de orden ≥ 3):

  - $AB = CE = FG$
  - $AC = BE = DG$
  - $AD = CG = EF$
  - $AE = BC = DF$
  - $AF = BG = DE$
  - $AG = BF = CD$
  - $BD = CF = EG$
- Grados de libertad: 15 = 7 (principales) + 7 (cadenas de 2 factores no ligadas a principales) + 1 (cadenas de orden ≥ 3).
- **Bloques:** 2 bloques de 8: $ABD = CDE = ACF = BEF = BCG = AEG = DFG$.

### XII(j) $2^{7-2}_{\mathrm{IV}}$ — 7 factores, fracción 1/4, 32 corridas, resolución IV

- **Generadores:** $F = ABCD$, $G = ABDE$.
- **Relación de definición** (3 palabras: 1 de 4 letras, 2 de 5 letras): $I = CEFG = ABCDF = ABDEG$.
- **Alias de efectos principales** (hasta orden 3):

  - $A$ (sin alias de orden ≤ 3)
  - $B$ (sin alias de orden ≤ 3)
  - $C = EFG$
  - $D$ (sin alias de orden ≤ 3)
  - $E = CFG$
  - $F = CEG$
  - $G = CEF$
- **Cadenas de interacciones de dos factores** (se omiten alias de orden ≥ 3):

  - $CE = FG$
  - $CF = EG$
  - $CG = EF$
- **Interacciones de dos factores sin alias de orden ≤ 2** (15): $AB = CDF = DEG$, $AC = BDF$, $AD = BCF = BEG$, $AE = BDG$, $AF = BCD$, $AG = BDE$, $BC = ADF$, $BD = ACF = AEG$, $BE = ADG$, $BF = ACD$, $BG = ADE$, $CD = ABF$, $DE = ABG$, $DF = ABC$, $DG = ABE$.
- Grados de libertad: 31 = 7 (principales) + 18 (cadenas de 2 factores no ligadas a principales) + 6 (cadenas de orden ≥ 3).
- **Bloques:** 2 bloques de 16: $ACE = AFG$. 4 bloques de 8: $ACE = AFG$; $BCE = BFG$; $AB = CDF = DEG$.

### XII(k) $2^{7-1}_{\mathrm{VII}}$ — 7 factores, fracción 1/2, 64 corridas, resolución VII

- **Generadores:** $G = ABCDEF$.
- **Relación de definición** (1 palabra: 1 de 7 letras): $I = ABCDEFG$.
- **Principales** aliados solo con interacciones de 6+ factores; las 21 **interacciones de dos factores** aliadas solo con interacciones de 5+ factores (ninguna cadena de 2 factores entre sí).
- **Bloques:** 2 bloques de 32: $ABC$. 4 bloques de 16: $ABC$; $CEF$; $CDG$.

### XII(l) $2^{8-4}_{\mathrm{IV}}$ — 8 factores, fracción 1/16, 16 corridas, resolución IV

- **Generadores:** $E = BCD$, $F = ACD$, $G = ABC$, $H = ABD$.
- **Relación de definición** (15 palabras: 14 de 4 letras, 1 de 8 letras): $I = ABCG = ABDH = ABEF = ACDF = ACEH = ADEG = AFGH = BCDE = BCFH = BDFG = BEGH = CDGH = CEFG = DEFH = ABCDEFGH$.
- **Alias de efectos principales** (hasta orden 3):

  - $A = BCG = BDH = BEF = CDF = CEH = DEG = FGH$
  - $B = ACG = ADH = AEF = CDE = CFH = DFG = EGH$
  - $C = ABG = ADF = AEH = BDE = BFH = DGH = EFG$
  - $D = ABH = ACF = AEG = BCE = BFG = CGH = EFH$
  - $E = ABF = ACH = ADG = BCD = BGH = CFG = DFH$
  - $F = ABE = ACD = AGH = BCH = BDG = CEG = DEH$
  - $G = ABC = ADE = AFH = BDF = BEH = CDH = CEF$
  - $H = ABD = ACE = AFG = BCF = BEG = CDG = DEF$
- **Cadenas de interacciones de dos factores** (se omiten alias de orden ≥ 3):

  - $AB = CG = DH = EF$
  - $AC = BG = DF = EH$
  - $AD = BH = CF = EG$
  - $AE = BF = CH = DG$
  - $AF = BE = CD = GH$
  - $AG = BC = DE = FH$
  - $AH = BD = CE = FG$
- Grados de libertad: 15 = 8 (principales) + 7 (cadenas de 2 factores no ligadas a principales) + 0 (cadenas de orden ≥ 3).
- **Bloques:** 2 bloques de 8: $AB = EF = CG = DH$.

### XII(m) $2^{8-3}_{\mathrm{IV}}$ — 8 factores, fracción 1/8, 32 corridas, resolución IV

- **Generadores:** $F = ABC$, $G = ABD$, $H = BCDE$.
- **Relación de definición** (7 palabras: 3 de 4 letras, 4 de 5 letras): $I = ABCF = ABDG = CDFG = ACEGH = ADEFH = BCDEH = BEFGH$.
- **Alias de efectos principales** (hasta orden 3):

  - $A = BCF = BDG$
  - $B = ACF = ADG$
  - $C = ABF = DFG$
  - $D = ABG = CFG$
  - $E$ (sin alias de orden ≤ 3)
  - $F = ABC = CDG$
  - $G = ABD = CDF$
  - $H$ (sin alias de orden ≤ 3)
- **Cadenas de interacciones de dos factores** (se omiten alias de orden ≥ 3):

  - $AB = CF = DG$
  - $AC = BF$
  - $AD = BG$
  - $AF = BC$
  - $AG = BD$
  - $CD = FG$
  - $CG = DF$
- **Interacciones de dos factores sin alias de orden ≤ 2** (13): $AE = CGH = DFH$, $AH = CEG = DEF$, $BE = CDH = FGH$, $BH = CDE = EFG$, $CE = AGH = BDH$, $CH = AEG = BDE$, $DE = AFH = BCH$, $DH = AEF = BCE$, $EF = ADH = BGH$, $EG = ACH = BFH$, $EH = ACG = ADF = BCD = BFG$, $FH = ADE = BEG$, $GH = ACE = BEF$.
- Grados de libertad: 31 = 8 (principales) + 20 (cadenas de 2 factores no ligadas a principales) + 3 (cadenas de orden ≥ 3).
- **Bloques:** 2 bloques de 16: $ABE = CEF = DEG$. 4 bloques de 8: $ABE = CEF = DEG$; $ABH = CFH = DGH$; $EH = BCD = ADF = ACG = BFG$.

### XII(n) $2^{8-2}_{\mathrm{V}}$ — 8 factores, fracción 1/4, 64 corridas, resolución V

- **Generadores:** $G = ABCD$, $H = ABEF$.
- **Relación de definición** (3 palabras: 2 de 5 letras, 1 de 6 letras): $I = ABCDG = ABEFH = CDEFGH$.
- **Principales** aliados solo con interacciones de 4+ factores; las 28 **interacciones de dos factores** aliadas solo con interacciones de 3+ factores (ninguna cadena de 2 factores entre sí).
- **Bloques:** 2 bloques de 32: $CDE = FGH$. 4 bloques de 16: $CDE = FGH$; $ACF$; $BDH$.

### XII(o) $2^{9-5}_{\mathrm{III}}$ — 9 factores, fracción 1/32, 16 corridas, resolución III

- **Generadores:** $E = ABC$, $F = BCD$, $G = ACD$, $H = ABD$, $J = ABCD$.
- **Relación de definición** (31 palabras: 4 de 3 letras, 14 de 4 letras, 8 de 5 letras, 4 de 7 letras, 1 de 8 letras): $I = AFJ = BGJ = CHJ = DEJ = ABCE = ABDH = ABFG = ACDG = ACFH = ADEF = AEGH = BCDF = BCGH = BDEG = BEFH = CDEH = CEFG = DFGH = ABCDJ = ABEHJ = ACEGJ = ADGHJ = BCEFJ = BDFHJ = CDFGJ = EFGHJ = ABCFGHJ = ABDEFGJ = ACDEFHJ = BCDEGHJ = ABCDEFGH$.
- **Alias de efectos principales** (hasta orden 2):

  - $A = FJ$
  - $B = GJ$
  - $C = HJ$
  - $D = EJ$
  - $E = DJ$
  - $F = AJ$
  - $G = BJ$
  - $H = CJ$
  - $J = AF = BG = CH = DE$
- **Cadenas de interacciones de dos factores** (se omiten alias de orden ≥ 3):

  - $AB = CE = DH = FG$
  - $AC = BE = DG = FH$
  - $AD = BH = CG = EF$
  - $AE = BC = DF = GH$
  - $AG = BF = CD = EH$
  - $AH = BD = CF = EG$
- Grados de libertad: 15 = 9 (principales) + 6 (cadenas de 2 factores no ligadas a principales) + 0 (cadenas de orden ≥ 3).
- **Bloques:** 2 bloques de 8: $AB = CE = FG = DH$.

### XII(p) $2^{9-4}_{\mathrm{IV}}$ — 9 factores, fracción 1/16, 32 corridas, resolución IV

- **Generadores:** $F = BCDE$, $G = ACDE$, $H = ABDE$, $J = ABCE$.
- **Relación de definición** (15 palabras: 6 de 4 letras, 8 de 5 letras, 1 de 8 letras): $I = ABFG = ACFH = ADFJ = BCGH = BDGJ = CDHJ = ABCEJ = ABDEH = ACDEG = AEGHJ = BCDEF = BEFHJ = CEFGJ = DEFGH = ABCDFGHJ$.
- **Alias de efectos principales** (hasta orden 3):

  - $A = BFG = CFH = DFJ$
  - $B = AFG = CGH = DGJ$
  - $C = AFH = BGH = DHJ$
  - $D = AFJ = BGJ = CHJ$
  - $E$ (sin alias de orden ≤ 3)
  - $F = ABG = ACH = ADJ$
  - $G = ABF = BCH = BDJ$
  - $H = ACF = BCG = CDJ$
  - $J = ADF = BDG = CDH$
- **Cadenas de interacciones de dos factores** (se omiten alias de orden ≥ 3):

  - $AB = FG$
  - $AC = FH$
  - $AD = FJ$
  - $AF = BG = CH = DJ$
  - $AG = BF$
  - $AH = CF$
  - $AJ = DF$
  - $BC = GH$
  - $BD = GJ$
  - $BH = CG$
  - $BJ = DG$
  - $CD = HJ$
  - $CJ = DH$
- **Interacciones de dos factores sin alias de orden ≤ 2** (8): $AE = BCJ = BDH = CDG = GHJ$, $BE = ACJ = ADH = CDF = FHJ$, $CE = ABJ = ADG = BDF = FGJ$, $DE = ABH = ACG = BCF = FGH$, $EF = BCD = BHJ = CGJ = DGH$, $EG = ACD = AHJ = CFJ = DFH$, $EH = ABD = AGJ = BFJ = DFG$, $EJ = ABC = AGH = BFH = CFG$.
- Grados de libertad: 31 = 9 (principales) + 21 (cadenas de 2 factores no ligadas a principales) + 1 (cadenas de orden ≥ 3).
- **Bloques:** 2 bloques de 16: $AEF = BEG = CEH = DEJ$. 4 bloques de 8: $AEF = BEG = CEH = DEJ$; $AB = FG = DEH = CEJ$; $CD = BEF = AEG = HJ$.

### XII(q) $2^{9-3}_{\mathrm{IV}}$ — 9 factores, fracción 1/8, 64 corridas, resolución IV

- **Generadores:** $G = ABCD$, $H = ACEF$, $J = CDEF$.
- **Relación de definición** (7 palabras: 1 de 4 letras, 4 de 5 letras, 2 de 6 letras): $I = ADHJ = ABCDG = ACEFH = BCGHJ = CDEFJ = ABEFGJ = BDEFGH$.
- **Principales:** libres de interacciones de dos factores; alias de tres factores: $A = DHJ$, $D = AHJ$, $H = ADJ$, $J = ADH$; el resto de principales no tiene alias de orden ≤ 3.
- **Interacciones de dos factores:** 30 de 36 quedan sin alias de dos factores; cadenas aliadas: $AD = HJ$, $AH = DJ$, $AJ = DH$.
- **Bloques:** 2 bloques de 32: $CFG$. 4 bloques de 16: $CFG$; $AGJ = BEF = DGH$; $ADE = EHJ$.

### XII(r) $2^{10-6}_{\mathrm{III}}$ — 10 factores, fracción 1/64, 16 corridas, resolución III

- **Generadores:** $E = ABC$, $F = BCD$, $G = ACD$, $H = ABD$, $J = ABCD$, $K = AB$.
- **Relación de definición** (63 palabras: 8 de 3 letras, 18 de 4 letras, 16 de 5 letras, 8 de 6 letras, 8 de 7 letras, 5 de 8 letras): $I = ABK = AFJ = BGJ = CEK = CHJ = DEJ = DHK = FGK = ABCE = ABDH = ABFG = ACDG = ACFH = ADEF = AEGH = AGJK = BCDF = BCGH = BDEG = BEFH = BFJK = CDEH = CDJK = CEFG = DFGH = EHJK = ABCDJ = ABEHJ = ACDFK = ACEGJ = ACGHK = ADEGK = ADGHJ = AEFHK = BCDGK = BCEFJ = BCFHK = BDEFK = BDFHJ = BEGHK = CDFGJ = EFGHJ = ABCHJK = ABDEJK = ACEFJK = ADFHJK = BCEGJK = BDGHJK = CFGHJK = DEFGJK = ABCDEHK = ABCEFGK = ABCFGHJ = ABDEFGJ = ABDFGHK = ACDEFHJ = BCDEGHJ = CDEFGHK = ABCDEFGH = ABCDFGJK = ABEFGHJK = ACDEGHJK = BCDEFHJK$.
- **Alias de efectos principales** (hasta orden 2):

  - $A = BK = FJ$
  - $B = AK = GJ$
  - $C = EK = HJ$
  - $D = EJ = HK$
  - $E = CK = DJ$
  - $F = AJ = GK$
  - $G = BJ = FK$
  - $H = CJ = DK$
  - $J = AF = BG = CH = DE$
  - $K = AB = CE = DH = FG$
- **Cadenas de interacciones de dos factores** (se omiten alias de orden ≥ 3):

  - $AC = BE = DG = FH$
  - $AD = BH = CG = EF$
  - $AE = BC = DF = GH$
  - $AG = BF = CD = EH = JK$
  - $AH = BD = CF = EG$
- Grados de libertad: 15 = 10 (principales) + 5 (cadenas de 2 factores no ligadas a principales) + 0 (cadenas de orden ≥ 3).
- **Bloques:** 2 bloques de 8: $AG = CD = BF = EH = JK$.

### XII(s) $2^{10-5}_{\mathrm{IV}}$ — 10 factores, fracción 1/32, 32 corridas, resolución IV

- **Generadores:** $F = ABCD$, $G = ABCE$, $H = ABDE$, $J = ACDE$, $K = BCDE$.
- **Relación de definición** (31 palabras: 10 de 4 letras, 16 de 5 letras, 5 de 8 letras): $I = ABJK = ACHK = ADGK = AEFK = BCHJ = BDGJ = BEFJ = CDGH = CEFH = DEFG = ABCDF = ABCEG = ABDEH = ABFGH = ACDEJ = ACFGJ = ADFHJ = AEGHJ = BCDEK = BCFGK = BDFHK = BEGHK = CDFJK = CEGJK = DEHJK = FGHJK = ABCDGHJK = ABCEFHJK = ABDEFGJK = ACDEFGHK = BCDEFGHJ$.
- **Alias de efectos principales** (hasta orden 3):

  - $A = BJK = CHK = DGK = EFK$
  - $B = AJK = CHJ = DGJ = EFJ$
  - $C = AHK = BHJ = DGH = EFH$
  - $D = AGK = BGJ = CGH = EFG$
  - $E = AFK = BFJ = CFH = DFG$
  - $F = AEK = BEJ = CEH = DEG$
  - $G = ADK = BDJ = CDH = DEF$
  - $H = ACK = BCJ = CDG = CEF$
  - $J = ABK = BCH = BDG = BEF$
  - $K = ABJ = ACH = ADG = AEF$
- **Cadenas de interacciones de dos factores** (se omiten alias de orden ≥ 3):

  - $AB = JK$
  - $AC = HK$
  - $AD = GK$
  - $AE = FK$
  - $AF = EK$
  - $AG = DK$
  - $AH = CK$
  - $AJ = BK$
  - $AK = BJ = CH = DG = EF$
  - $BC = HJ$
  - $BD = GJ$
  - $BE = FJ$
  - $BF = EJ$
  - $BG = DJ$
  - $BH = CJ$
  - $CD = GH$
  - $CE = FH$
  - $CF = EH$
  - $CG = DH$
  - $DE = FG$
  - $DF = EG$
- Grados de libertad: 31 = 10 (principales) + 21 (cadenas de 2 factores no ligadas a principales) + 0 (cadenas de orden ≥ 3).
- **Bloques:** 2 bloques de 16: $AK = EF = DG = CH = BJ$. 4 bloques de 8: $AK = EF = DG = CH = BJ$; $AJ = CDE = CFG = DFH = EGH = BK$; $AB = CDF = CEG = DEH = FGH = JK$.

### XII(t) $2^{10-4}_{\mathrm{IV}}$ — 10 factores, fracción 1/16, 64 corridas, resolución IV

- **Generadores:** $G = BCDF$, $H = ACDF$, $J = ABDE$, $K = ABCE$.
- **Relación de definición** (15 palabras: 2 de 4 letras, 8 de 5 letras, 4 de 6 letras, 1 de 8 letras): $I = ABGH = CDJK = ABCEK = ABDEJ = ACDFH = AFHJK = BCDFG = BFGJK = CEGHK = DEGHJ = ACEFGJ = ADEFGK = BCEFHJ = BDEFHK = ABCDGHJK$.
- **Principales:** libres de interacciones de dos factores; alias de tres factores: $A = BGH$, $B = AGH$, $C = DJK$, $D = CJK$, $G = ABH$, $H = ABG$, $J = CDK$, $K = CDJ$; el resto de principales no tiene alias de orden ≤ 3.
- **Interacciones de dos factores:** 33 de 45 quedan sin alias de dos factores; cadenas aliadas: $AB = GH$, $AG = BH$, $AH = BG$, $CD = JK$, $CJ = DK$, $CK = DJ$.
- **Bloques:** 2 bloques de 32: $AGJ = CEF = BHJ$. 4 bloques de 16: $AGJ = CEF = BHJ$; $AGK = DEF = BHK$; $CD = BFG = AFH = JK$.

### XII(u) $2^{11-7}_{\mathrm{III}}$ — 11 factores, fracción 1/128, 16 corridas, resolución III

- **Generadores:** $E = ABC$, $F = BCD$, $G = ACD$, $H = ABD$, $J = ABCD$, $K = AB$, $L = AC$.
- **Relación de definición:** 127 palabras (12 de 3 letras, 26 de 4 letras, 28 de 5 letras, 24 de 6 letras, 20 de 7 letras, 13 de 8 letras, 4 de 9 letras). Palabras de 3 y 4 letras: $ABK = ACL = AFJ = BEL = BGJ = CEK = CHJ = DEJ = DGL = DHK = FGK = FHL = ABCE = ABDH = ABFG = ACDG = ACFH = ADEF = AEGH = AEKL = AGJK = AHJL = BCDF = BCGH = BCKL = BDEG = BDJL = BEFH = BFJK = CDEH = CDJK = CEFG = CFJL = DFGH = DFKL = EGJL = EHJK = GHKL$.
- **Alias de efectos principales** (hasta orden 2):

  - $A = BK = CL = FJ$
  - $B = AK = EL = GJ$
  - $C = AL = EK = HJ$
  - $D = EJ = GL = HK$
  - $E = BL = CK = DJ$
  - $F = AJ = GK = HL$
  - $G = BJ = DL = FK$
  - $H = CJ = DK = FL$
  - $J = AF = BG = CH = DE$
  - $K = AB = CE = DH = FG$
  - $L = AC = BE = DG = FH$
- **Cadenas de interacciones de dos factores** (se omiten alias de orden ≥ 3):

  - $AD = BH = CG = EF$
  - $AE = BC = DF = GH = KL$
  - $AG = BF = CD = EH = JK$
  - $AH = BD = CF = EG = JL$
- Grados de libertad: 15 = 11 (principales) + 4 (cadenas de 2 factores no ligadas a principales) + 0 (cadenas de orden ≥ 3).
- **Bloques:** 2 bloques de 8: $AE = BC = DF = GH = KL$.

### XII(v) $2^{11-6}_{\mathrm{IV}}$ — 11 factores, fracción 1/64, 32 corridas, resolución IV

- **Generadores:** $F = ABC$, $G = BCD$, $H = CDE$, $J = ACD$, $K = ADE$, $L = BDE$.
- **Relación de definición** (63 palabras: 25 de 4 letras, 27 de 6 letras, 10 de 8 letras, 1 de 10 letras): $I = ABCF = ABGJ = ABKL = ACDJ = ACHK = ADEK = ADFG = AEHJ = AFHL = BCDG = BCHL = BDEL = BDFJ = BEGH = BFHK = CDEH = CEGL = CEJK = CFGJ = CFKL = DGHL = DHJK = EFGK = EFJL = GJKL = ABCEGK = ABCEJL = ABDEFH = ABDGHK = ABDHJL = ABEFGL = ABEFJK = ACDEFL = ACDGKL = ACEFGH = ACGHJL = ADEGJL = ADFJKL = AEGHKL = AFGHJK = BCDEFK = BCDJKL = BCEFHJ = BCGHJK = BDEGJK = BDFGKL = BEHJKL = BFGHJL = CDFGHK = CDFHJL = DEFGHJ = DEFHKL = ABCDEGHJ = ABCDEHKL = ABCDFGHL = ABCDFHJK = ABCFGJKL = ACDEFGJK = ACEFHJKL = BCDEFGJL = BCEFGHKL = CDEGHJKL = ABDEFGHJKL$.
- **Alias de efectos principales** (hasta orden 3):

  - $A = BCF = BGJ = BKL = CDJ = CHK = DEK = DFG = EHJ = FHL$
  - $B = ACF = AGJ = AKL = CDG = CHL = DEL = DFJ = EGH = FHK$
  - $C = ABF = ADJ = AHK = BDG = BHL = DEH = EGL = EJK = FGJ = FKL$
  - $D = ACJ = AEK = AFG = BCG = BEL = BFJ = CEH = GHL = HJK$
  - $E = ADK = AHJ = BDL = BGH = CDH = CGL = CJK = FGK = FJL$
  - $F = ABC = ADG = AHL = BDJ = BHK = CGJ = CKL = EGK = EJL$
  - $G = ABJ = ADF = BCD = BEH = CEL = CFJ = DHL = EFK = JKL$
  - $H = ACK = AEJ = AFL = BCL = BEG = BFK = CDE = DGL = DJK$
  - $J = ABG = ACD = AEH = BDF = CEK = CFG = DHK = EFL = GKL$
  - $K = ABL = ACH = ADE = BFH = CEJ = CFL = DHJ = EFG = GJL$
  - $L = ABK = AFH = BCH = BDE = CEG = CFK = DGH = EFJ = GJK$
- **Cadenas de interacciones de dos factores** (se omiten alias de orden ≥ 3):

  - $AB = CF = GJ = KL$
  - $AC = BF = DJ = HK$
  - $AD = CJ = EK = FG$
  - $AE = DK = HJ$
  - $AF = BC = DG = HL$
  - $AG = BJ = DF$
  - $AH = CK = EJ = FL$
  - $AJ = BG = CD = EH$
  - $AK = BL = CH = DE$
  - $AL = BK = FH$
  - $BD = CG = EL = FJ$
  - $BE = DL = GH$
  - $BH = CL = EG = FK$
  - $CE = DH = GL = JK$
  - $EF = GK = JL$
- Grados de libertad: 31 = 11 (principales) + 15 (cadenas de 2 factores no ligadas a principales) + 5 (cadenas de orden ≥ 3).
- **Bloques:** 2 bloques de 16: $AB = CF = GJ = KL$. 4 bloques de 8: $AB = CF = GJ = KL$; $AD = FG = CJ = EK$; $BD = CG = FJ = EL$.

### XII(w) $2^{12-8}_{\mathrm{III}}$ — 12 factores, fracción 1/256, 16 corridas, resolución III

- **Generadores:** $E = ABC$, $F = ABD$, $G = ACD$, $H = BCD$, $J = ABCD$, $K = AB$, $L = AC$, $M = AD$.
- **Relación de definición:** 255 palabras (16 de 3 letras, 39 de 4 letras, 48 de 5 letras, 48 de 6 letras, 48 de 7 letras, 39 de 8 letras, 16 de 9 letras, 1 de 12 letras). Palabras de 3 y 4 letras: $ABK = ACL = ADM = AHJ = BEL = BFM = BGJ = CEK = CFJ = CGM = DEJ = DFK = DGL = EHM = FHL = GHK = ABCE = ABDF = ABGH = ACDG = ACFH = ADEH = AEFG = AEJM = AEKL = AFJL = AFKM = AGJK = AGLM = BCDH = BCFG = BCJM = BCKL = BDEG = BDJL = BDKM = BEFH = BHJK = BHLM = CDEF = CDJK = CDLM = CEGH = CHJL = CHKM = DFGH = DHJM = DHKL = EFJK = EFLM = EGJL = EGKM = FGJM = FGKL = JKLM$.
- **Alias de efectos principales** (hasta orden 2):

  - $A = BK = CL = DM = HJ$
  - $B = AK = EL = FM = GJ$
  - $C = AL = EK = FJ = GM$
  - $D = AM = EJ = FK = GL$
  - $E = BL = CK = DJ = HM$
  - $F = BM = CJ = DK = HL$
  - $G = BJ = CM = DL = HK$
  - $H = AJ = EM = FL = GK$
  - $J = AH = BG = CF = DE$
  - $K = AB = CE = DF = GH$
  - $L = AC = BE = DG = FH$
  - $M = AD = BF = CG = EH$
- **Cadenas de interacciones de dos factores** (se omiten alias de orden ≥ 3):

  - $AE = BC = DH = FG = JM = KL$
  - $AF = BD = CH = EG = JL = KM$
  - $AG = BH = CD = EF = JK = LM$
- Grados de libertad: 15 = 12 (principales) + 3 (cadenas de 2 factores no ligadas a principales) + 0 (cadenas de orden ≥ 3).
- **Bloques:** 2 bloques de 8: $AE = BC = FG = DH = KL = JM$.

### XII(x) $2^{13-9}_{\mathrm{III}}$ — 13 factores, fracción 1/512, 16 corridas, resolución III

- **Generadores:** $E = ABC$, $F = ABD$, $G = ACD$, $H = BCD$, $J = ABCD$, $K = AB$, $L = AC$, $M = AD$, $N = BC$.
- **Relación de definición:** 511 palabras (22 de 3 letras, 55 de 4 letras, 72 de 5 letras, 96 de 6 letras, 116 de 7 letras, 87 de 8 letras, 40 de 9 letras, 16 de 10 letras, 6 de 11 letras, 1 de 12 letras). Palabras de 3 y 4 letras: $ABK = ACL = ADM = AEN = AHJ = BCN = BEL = BFM = BGJ = CEK = CFJ = CGM = DEJ = DFK = DGL = DHN = EHM = FGN = FHL = GHK = JMN = KLN = ABCE = ABDF = ABGH = ABLN = ACDG = ACFH = ACKN = ADEH = ADJN = AEFG = AEJM = AEKL = AFJL = AFKM = AGJK = AGLM = AHMN = BCDH = BCFG = BCJM = BCKL = BDEG = BDJL = BDKM = BEFH = BEKN = BFJN = BGMN = BHJK = BHLM = CDEF = CDJK = CDLM = CEGH = CELN = CFMN = CGJN = CHJL = CHKM = DEMN = DFGH = DFLN = DGKN = DHJM = DHKL = EFJK = EFLM = EGJL = EGKM = EHJN = FGJM = FGKL = FHKN = GHLN = JKLM$.
- **Alias de efectos principales** (hasta orden 2):

  - $A = BK = CL = DM = EN = HJ$
  - $B = AK = CN = EL = FM = GJ$
  - $C = AL = BN = EK = FJ = GM$
  - $D = AM = EJ = FK = GL = HN$
  - $E = AN = BL = CK = DJ = HM$
  - $F = BM = CJ = DK = GN = HL$
  - $G = BJ = CM = DL = FN = HK$
  - $H = AJ = DN = EM = FL = GK$
  - $J = AH = BG = CF = DE = MN$
  - $K = AB = CE = DF = GH = LN$
  - $L = AC = BE = DG = FH = KN$
  - $M = AD = BF = CG = EH = JN$
  - $N = AE = BC = DH = FG = JM = KL$
- **Cadenas de interacciones de dos factores** (se omiten alias de orden ≥ 3):

  - $AF = BD = CH = EG = JL = KM$
  - $AG = BH = CD = EF = JK = LM$
- Grados de libertad: 15 = 13 (principales) + 2 (cadenas de 2 factores no ligadas a principales) + 0 (cadenas de orden ≥ 3).
- **Bloques:** 2 bloques de 8: $AF = BD = EG = CH = JL = KM$.

### XII(y) $2^{14-10}_{\mathrm{III}}$ — 14 factores, fracción 1/1024, 16 corridas, resolución III

- **Generadores:** $E = ABC$, $F = ABD$, $G = ACD$, $H = BCD$, $J = ABCD$, $K = AB$, $L = AC$, $M = AD$, $N = BC$, $O = BD$.
- **Relación de definición:** 1023 palabras (28 de 3 letras, 77 de 4 letras, 112 de 5 letras, 168 de 6 letras, 232 de 7 letras, 203 de 8 letras, 112 de 9 letras, 56 de 10 letras, 28 de 11 letras, 7 de 12 letras). Palabras de 3 y 4 letras: $ABK = ACL = ADM = AEN = AFO = AHJ = BCN = BDO = BEL = BFM = BGJ = CEK = CFJ = CGM = CHO = DEJ = DFK = DGL = DHN = EGO = EHM = FGN = FHL = GHK = JLO = JMN = KLN = KMO = ABCE = ABDF = ABGH = ABLN = ABMO = ACDG = ACFH = ACJO = ACKN = ADEH = ADJN = ADKO = AEFG = AEJM = AEKL = AFJL = AFKM = AGJK = AGLM = AGNO = AHLO = AHMN = BCDH = BCFG = BCJM = BCKL = BDEG = BDJL = BDKM = BEFH = BEJO = BEKN = BFJN = BFKO = BGLO = BGMN = BHJK = BHLM = BHNO = CDEF = CDJK = CDLM = CDNO = CEGH = CELN = CEMO = CFLO = CFMN = CGJN = CGKO = CHJL = CHKM = DELO = DEMN = DFGH = DFLN = DFMO = DGJO = DGKN = DHJM = DHKL = EFJK = EFLM = EFNO = EGJL = EGKM = EHJN = EHKO = FGJM = FGKL = FHJO = FHKN = GHLN = GHMO = JKLM = JKNO = LMNO$.
- **Alias de efectos principales** (hasta orden 2):

  - $A = BK = CL = DM = EN = FO = HJ$
  - $B = AK = CN = DO = EL = FM = GJ$
  - $C = AL = BN = EK = FJ = GM = HO$
  - $D = AM = BO = EJ = FK = GL = HN$
  - $E = AN = BL = CK = DJ = GO = HM$
  - $F = AO = BM = CJ = DK = GN = HL$
  - $G = BJ = CM = DL = EO = FN = HK$
  - $H = AJ = CO = DN = EM = FL = GK$
  - $J = AH = BG = CF = DE = LO = MN$
  - $K = AB = CE = DF = GH = LN = MO$
  - $L = AC = BE = DG = FH = JO = KN$
  - $M = AD = BF = CG = EH = JN = KO$
  - $N = AE = BC = DH = FG = JM = KL$
  - $O = AF = BD = CH = EG = JL = KM$
- **Cadenas de interacciones de dos factores** (se omiten alias de orden ≥ 3):

  - $AG = BH = CD = EF = JK = LM = NO$
- Grados de libertad: 15 = 14 (principales) + 1 (cadenas de 2 factores no ligadas a principales) + 0 (cadenas de orden ≥ 3).
- **Bloques:** 2 bloques de 8: $AG = EF = CD = BH = JK = LM = NO$.

### XII(z) $2^{15-11}_{\mathrm{III}}$ — 15 factores, fracción 1/2048, 16 corridas, resolución III

- **Generadores:** $E = ABC$, $F = ABD$, $G = ACD$, $H = BCD$, $J = ABCD$, $K = AB$, $L = AC$, $M = AD$, $N = BC$, $O = BD$, $P = CD$.
- **Relación de definición:** 2047 palabras (35 de 3 letras, 105 de 4 letras, 168 de 5 letras, 280 de 6 letras, 435 de 7 letras, 435 de 8 letras, 280 de 9 letras, 168 de 10 letras, 105 de 11 letras, 35 de 12 letras, 1 de 15 letras). Palabras de 3 y 4 letras: $ABK = ACL = ADM = AEN = AFO = AGP = AHJ = BCN = BDO = BEL = BFM = BGJ = BHP = CDP = CEK = CFJ = CGM = CHO = DEJ = DFK = DGL = DHN = EFP = EGO = EHM = FGN = FHL = GHK = JKP = JLO = JMN = KLN = KMO = LMP = NOP = ABCE = ABDF = ABGH = ABJP = ABLN = ABMO = ACDG = ACFH = ACJO = ACKN = ACMP = ADEH = ADJN = ADKO = ADLP = AEFG = AEJM = AEKL = AEOP = AFJL = AFKM = AFNP = AGJK = AGLM = AGNO = AHKP = AHLO = AHMN = BCDH = BCFG = BCJM = BCKL = BCOP = BDEG = BDJL = BDKM = BDNP = BEFH = BEJO = BEKN = BEMP = BFJN = BFKO = BFLP = BGKP = BGLO = BGMN = BHJK = BHLM = BHNO = CDEF = CDJK = CDLM = CDNO = CEGH = CEJP = CELN = CEMO = CFKP = CFLO = CFMN = CGJN = CGKO = CGLP = CHJL = CHKM = CHNP = DEKP = DELO = DEMN = DFGH = DFJP = DFLN = DFMO = DGJO = DGKN = DGMP = DHJM = DHKL = DHOP = EFJK = EFLM = EFNO = EGJL = EGKM = EGNP = EHJN = EHKO = EHLP = FGJM = FGKL = FGOP = FHJO = FHKN = FHMP = GHJP = GHLN = GHMO = JKLM = JKNO = JLNP = JMOP = KLOP = KMNP = LMNO$.
- **Alias de efectos principales** (hasta orden 2):

  - $A = BK = CL = DM = EN = FO = GP = HJ$
  - $B = AK = CN = DO = EL = FM = GJ = HP$
  - $C = AL = BN = DP = EK = FJ = GM = HO$
  - $D = AM = BO = CP = EJ = FK = GL = HN$
  - $E = AN = BL = CK = DJ = FP = GO = HM$
  - $F = AO = BM = CJ = DK = EP = GN = HL$
  - $G = AP = BJ = CM = DL = EO = FN = HK$
  - $H = AJ = BP = CO = DN = EM = FL = GK$
  - $J = AH = BG = CF = DE = KP = LO = MN$
  - $K = AB = CE = DF = GH = JP = LN = MO$
  - $L = AC = BE = DG = FH = JO = KN = MP$
  - $M = AD = BF = CG = EH = JN = KO = LP$
  - $N = AE = BC = DH = FG = JM = KL = OP$
  - $O = AF = BD = CH = EG = JL = KM = NP$
  - $P = AG = BH = CD = EF = JK = LM = NO$
- Grados de libertad: 15 = 15 (principales) + 0 (cadenas de 2 factores no ligadas a principales) + 0 (cadenas de orden ≥ 3).
