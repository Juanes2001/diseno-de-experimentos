# Gutiérrez–De la Vara, cap. 8 — Diseños factoriales fraccionados 2^(k−p)

Gutiérrez Pulido, H. y De la Vara Salazar, R. (2008). *Análisis y diseño de experimentos* (2.ª ed.).
McGraw-Hill. Capítulo 8, págs. 259–293 (PDF local, págs. 276–311). Leído completo el 30 oct 2026.
Cifras de los ejemplos recalculadas en Python (vibración y semiconductores) y coinciden con el libro.

> **Para retomar desde otro dispositivo.** Esta ficha es la referencia para modificar la presentación de
> fraccionados (`scripts/tema-06/contenido.py`, se regenera con `bash scripts/tema-06/build.sh`). Pedir a
> Claude que lea esta ficha (secciones 1 y 3) y luego dar las indicaciones de qué diapositivas cambiar.
> Estado de la presentación al 30 oct 2026: 106 diapositivas, sin diseños saturados; resolución III en
> las diapositivas 85–97 y resoluciones IV y V desde la 98. Ojo: regenerar con `build.sh` pisa cualquier
> edición hecha a mano en PowerPoint sobre el `.pptx`.

## 1. Estilo de explicación (lo que distingue a este libro de Montgomery)

Es la referencia para simplificar la exposición del tema 6. Rasgos:

1. **Arranca por el porqué, con una tabla de conteo.** Antes de cualquier definición muestra la tabla 8.1
   (efectos «no ignorables» = principales + dobles, frente a «ignorables» = triples o más). El argumento es
   visual: a partir de k = 5 hay más efectos ignorables que importantes, así que el 2^k completo «acumula
   exceso de información» y se puede fraccionar sin perder lo valioso. Con k < 5 fraccionar sí cuesta.
2. **Dos «hechos insoslayables»** como marco de todo el capítulo: (1) se pierde información (efectos que no se
   estiman y menos g.l. para el error) y (2) cada efecto estimable tiene al menos un alias. Los ejemplos
   vuelven a señalar «han ocurrido los dos hechos».
3. **Primero el caso más pequeño, con contrastes a la vista.** El 2^(3−1) se explica con la tabla de signos:
   la fracción principal son los tratamientos con + en ABC; luego se escribe Contraste A = (a + abc − b − c)
   y Contraste BC = (a + abc − b − c) y se concluye «son iguales, luego A y BC son alias». Solo después
   introduce la multiplicación módulo 2 (A × ABC = A²BC = BC) como atajo «más práctico para diseños grandes».
4. **Alias en lenguaje llano:** «son el mismo efecto con nombres distintos; al estimar uno se estima el otro».
   Al estimar A en realidad se estima la suma A + BC «y no se sabe cuál predomina o si ambos afectan».
5. **Interpretación por jerarquía, dicha sin rodeos:** se supone que solo uno de los alias es responsable y se
   atribuye al de menor orden. Cuando los alias tienen la misma jerarquía (BE + CD) se decide por conocimiento
   del proceso o por cuáles efectos principales resultaron activos (herencia, sin usar esa palabra).
6. **Resolución como «qué tan bien se estudian los efectos importantes»**, con tres definiciones cortas
   (III, IV, V) y un ejemplo cada una (2^(3−1), 2^(4−1), 2^(5−1)). Regla práctica: la resolución es el número
   de letras de la palabra más corta; en un 2^(k−1) es el número de letras del generador.
7. **Construcción siempre en «dos pasos»** (2^(k−1), 2^(k−2) y 2^(k−p) con el mismo molde):
   1) escribir el factorial completo en los primeros k − p factores; 2) las columnas que faltan se obtienen
   multiplicando columnas según los generadores. Para la fracción complementaria se cambia el signo.
8. **Ejemplo integrador que demuestra la idea, no solo la aplica:** el 2^5 de semiconductores (cap. 6) se
   parte en sus dos mitades y se muestra que cada mitad da los mismos Pareto, Daniel, efectos y mejor
   tratamiento que el completo, a mitad de costo. El mensaje es «bastaba con una fracción».
9. **Análisis gráfico primero, ANOVA después.** Pareto de efectos + gráfico de Daniel para decidir qué es
   activo; luego el «mejor ANOVA» mandando al error los efectos alineados (regla: al excluir un efecto se
   excluyen también todos sus alias). Interpretación con gráficas de efectos principales, de interacción y
   de cubo, y «el mejor tratamiento»; los factores inactivos se fijan por criterio económico.
10. **Tablas en lugar de teoría:** para elegir generadores remite a la tabla 8.8 (fracciones de resolución
    IV con hasta 64 corridas) o al software; «quizá lo más difícil es encontrar los mejores generadores».
11. **Glosario al margen:** cada concepto clave tiene una definición de una o dos líneas en el margen
    (efectos alias, generador, relación definidora, resolución III/IV/V, saturado, mínima aberración…).
12. **Vocabulario:** «relación definidora» (no «de definición»), «estructura de alias» completa y
    **reducida** (solo hasta dobles), «fracción principal» y «fracción complementaria», «efectos
    generadores», «colapsar» el diseño (proyectar), «mejor ANOVA», FV/SC/GL/CM/F0/valor-p, «el efecto se
    confunde con la media global» (para el generador).
13. **Recomendaciones prácticas explícitas:** no usar resolución III salvo que se acepte que solo importan
    los principales; con 5 < k ≤ 15 hay resolución IV en ≤ 32 corridas; si las corridas son baratas, ir
    directo a resolución V; «es más recomendable experimentar aunque sea con resolución III que no hacerlo».

## 2. Contenido por sección

### 2.1 Introducción (pág. 260–261)
- Motivación: k = 6 → 64 corridas, k = 7 → 128. Jerarquía: principales > dobles > triples > …
- Tabla 8.1 (efectos totales / no ignorables / ignorables): 2^2: 3/3/0; 2^3: 7/6/1; 2^4: 15/10/5;
  **2^5: 31/15/16**; 2^6: 63/21/42; 2^7: 127/28/99. Con un 2^(5−1) se estiman limpios los 15 importantes.
- Los dos hechos: se pierde información; todo efecto estimable tiene al menos un alias.

### 2.2 Fracción 2^(3−1) (págs. 261–264)
- No tiene sentido fraccionar el 2^2. De los C(8,4) = 70 grupos de 4 tratamientos, conviene sacrificar ABC.
- Fracción principal I = +ABC: a, b, c, abc. Complementaria I = −ABC: (1), ab, ac, bc.
- Ortogonalidad: cada factor dos veces en + y dos en −. ABC solo tiene signos + en la fracción: «se confunde
  con la media global».
- Alias por contrastes y por módulo 2: A + BC, B + AC, C + AB (8.1); en la complementaria A − BC, B − AC,
  C − AB (8.2). No se recomienda salvo que el costo lo obligue (principales aliados con dobles).

### 2.3 Resolución (pág. 265)
- III: principales no aliados entre sí, pero sí con dobles (2^(3−1), I = ABC).
- IV: principales libres de principales y dobles; dobles aliadas entre sí (2^(4−1), I = ABCD).
- V: principales y dobles aliados con triples o más (2^(5−1), I = ABCDE).
- Definición formal: resolución R si ninguna interacción de P factores es alias de una de menos de R − P.

### 2.4 Construcción de fracciones 2^(k−1) (págs. 265–266)
- Dos pasos: completo en k − 1 factores; la k-ésima columna = producto de las anteriores (resolución R = k).
- Ejemplo 8.1: 2^(4−1) con D = −ABC (fracción complementaria); ventaja: evita (−,−,−,−) y (+,+,+,+).

### 2.5 Experimento 2^(5−1): ejemplo integrador (págs. 266–269)
- Semiconductores, rendimiento. A abertura, B tiempo de exposición, C tiempo de revelado, D dimensión de la
  máscara, E tiempo de grabado. Tabla 8.4 con las dos fracciones (I = ±ABCDE), 16 datos cada una.
- Ambas fracciones detectan A, B, C y AB (Pareto fig. 8.2, Daniel fig. 8.3). Fracción principal recalculada:
  A = 10.875, B = 33.625, C = 10.625, AB = 7.125, D = −0.625, E = 0.375.
- Mejor tratamiento (A+, B+, C+); D y E por economía. «Bastaba con una fracción a la mitad»; ejercicio 18:
  incluso con un 2^(5−2) se llega a lo mismo.

### 2.6 Fracciones 2^(k−2) (págs. 269–272)
- Dos generadores de alto orden cuyo producto también sea de alto orden; tres «palabras» no estimables;
  cada efecto tiene tres alias. Número de palabras = número de alias de cada efecto.
- Ejemplo 8.2: 2^(5−2) con D = AB, E = AC; I = ABD = ACE = BCDE, resolución III (no existe mayor).
- Estructura completa (tabla 8.6) y **reducida** (tabla 8.7): A + BD + CE; B + AD; C + AE; D + AB; E + AC;
  BC + DE; BE + CD. Familia de cuatro fracciones según los signos; se elige por los tratamientos que se
  quieren incluir o evitar.

### 2.7 Fracción general 2^(k−p) (págs. 273–276)
- Fracción 1/2^p, p generadores de alto orden; construcción en los dos pasos; la relación definidora tiene
  2^p − 1 términos.
- Tabla 8.8: fracciones de resolución IV o más con hasta 64 corridas (p. ej. 2^(6−2)_IV: E = ABC, F = BCD;
  2^(7−3)_IV: E = ABC, F = BCD, G = ACD; 2^(8−4)_IV: E = BCD, F = ACD, G = ABC, H = ABD).
- Ejemplo 8.3: 2^(7−3)_IV, I = ABCE = ABFG = ACDG = ADEF = BCDF = BDEG = CEFG; alias reducidos: los siete
  principales limpios y siete grupos de tres dobles (AB + CE + FG, …).
- Asignación de factores: con temperatura, humedad, velocidad y ángulo en A, B, C, D se estiman sus seis
  dobles; si ángulo va en E aparecen AB + CE, AC + BE, AE + BC. «Un pequeño cambio en la asignación cambia
  radicalmente la estructura de alias».
- Efecto X = Contraste / 2^(k−p−1); SC_X = Contraste² / 2^(k−p), 1 g.l. Al excluir un efecto se excluyen
  todos sus alias.

### 2.8 Experimento 2^(7−4): ejemplo integrador (págs. 276–279)
- Equipo de afilado con exceso de vibración; siete factores de la herramienta; 8 corridas por costo.
  A grano (80, 120), B longitud (1, 2 pulg), C diámetro (1.0, 1.5), D rpm (15, 20 ×1000), E precarga,
  F estructura del material, G velocidad de alimentación. D = AB, E = AC, F = BC, G = ABC.
- Datos (orden estándar): 77.4, 68.3, 81.9, 66.2, 42.1, 78.3, 39.0, 68.4.
- 7 g.l., todos en efectos: cero para el error → Pareto y Daniel primero. Efectos recalculados:
  A = 10.20, B = −2.65, C = −16.50, D = −3.35, **E = 22.60**, F = −3.85, G = −0.05.
- Mejor ANOVA (tabla 8.15): A SC 208.08, F0 12.58, p 0.0239; C 544.5, 32.93, 0.0046; E 1021.52, 61.78,
  0.0014; error 66.14 con 4 g.l. (CM 16.535); total 1840.24 con 7. R²aj = 93.71 %.
- Mejor tratamiento: grano bajo, diámetro alto, precarga baja; vibración predicha mínima 40.55 (cubo).

### 2.9 Tópicos adicionales (págs. 279–285)
- **Comentarios sobre la resolución:** recomendaciones del punto 13 de la sección 1.
- **Aberración mínima:** dos 2^(7−2)_IV: d1: I = DEFG = ABCDF = ABCEG (W = (0,0,0,1,2,0,0), tres pares de
  dobles aliadas) frente a d2: I = ABCF = ADEG = BCDEFG (W = (0,0,0,2,0,1,0), seis pares). Gana d1.
- **Fracciones saturadas:** g.l. totales = número de factores (k + 1 corridas para k factores); son de
  resolución III. Ejemplo: el 2^(7−4) de la vibración.
- **Plackett-Burman:** N múltiplo de 4; primer renglón con (k + 1)/2 signos + y (k − 1)/2 −, los siguientes
  se obtienen desplazando, el último todo −. Tabla 8.16 (N = 12, k = 11; primer renglón
  + − + − − − + + + − +) y tabla 8.17 (N = 12, 20, 24, 36). Para menos factores, las primeras columnas.
- **Aclaración de ambigüedades con otra fracción:** si la primera da A + BC, la segunda debe dar A − BC;
  semisuma → A, semidiferencia → BC. Sobre el 2^(7−4) (ℓA → A + BD + CE + FG, etc.):
  - Caso 1, un factor dominante (A) y todas sus dobles: cambiar el signo de los generadores que contienen
    A: I = −ABD = −ACE = +BCF = −ABCG. Combinadas: A y AB, AC, AD, AE, AF, AG limpios; el resto sigue III.
  - Caso 2, todos los principales: cambiar el signo de los generadores de tres letras:
    I = −ABD = −ACE = −BCF = +ABCG. Combinadas: los siete principales limpios → resolución IV.
  (Es el doblez de un factor y el doblez completo de Montgomery, explicado sin ese nombre.)

### 2.10 Software (págs. 285–286)
- Statgraphics (Screening, Generators, Alias structure) y Minitab: Stat → DOE → Factorial → Create Factorial
  Design → 2-level factorial (default generators / specify generators); «Display Available Designs» muestra
  la resolución.

### 2.11 Ejercicios útiles para la exposición
- 4–6: preguntas conceptuales sobre 2^(5−1), 2^4 y 2^(8−4) (qué se pierde, criterio de selección, orden).
- 10–11: 2^(5−1) con datos y colapso a 2^3.
- 12: moldeo por inyección, 2^(7−3) con I = ABCE = BCDF = ACDG y cuatro centros (curvatura).
- 13: panificadora, 2^(6−2), dos respuestas (ATT y pH).
- 16–17: Ozzie's Bar (Box y Draper), 2^(6−3)_III con I = ABD = −ACE = BCF y segunda fracción para aislar D.

## 3. Diferencias con Montgomery (cap. 8) para decidir cambios en la presentación

| Aspecto | Montgomery | Gutiérrez–De la Vara |
|---|---|---|
| Motivación | Escasez de efectos, proyección, experimentación secuencial | Tabla 8.1 de efectos ignorables y los «dos hechos» |
| Alias | Desde la relación de definición | Primero comparando contrastes, después módulo 2 |
| Construcción | Diseño básico + generadores | «Dos pasos», el mismo molde para todo 2^(k−p) |
| Ejemplo eje | Filtrado (2^(4−1)), moldeo 2^(6−2), CNC con bloques | Semiconductores 2^(5−1) (dos mitades = completo) y vibración 2^(7−4) |
| Análisis | Gráfica normal, Lenth, ANOVA | Pareto + Daniel → «mejor ANOVA» → gráficas y mejor tratamiento |
| Bloques en fraccionados | Sí (sección completa) | No se tratan |
| Doblez | Nombre y teoría (fold over, reflexión) | «Aclaración de ambigüedades con otra fracción», casos 1 y 2 |
| Resolución IV/V, 2^(k−p) no regulares | Secciones propias | Solo comentarios y tabla 8.8 |
| Elección de generadores | Tablas y aberración mínima | Tabla 8.8, software y aberración mínima con W |
