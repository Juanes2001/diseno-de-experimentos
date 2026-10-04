# Fichas técnicas de Montgomery — índice

Referencia permanente de *Diseño y análisis de experimentos* de Douglas C. Montgomery
(2.ª edición en español, Limusa-Wiley). Cada ficha resume, con palabras propias, el detalle
estadístico y de procedimiento de un capítulo: modelo, construcción del diseño, fórmulas del
análisis, verificación de supuestos, reglas prácticas y resultados clave de los ejemplos.

**Uso:** consultar estas fichas en lugar del libro. Para un tema, abrir solo la ficha del
capítulo correspondiente (tabla de abajo); no hace falta leerlas todas.

## Fichas por capítulo

| Cap. | Ficha | Págs. del libro | Contenido |
|---|---|---|---|
| 1 | [cap-01-introduccion.md](cap-01-introduccion.md) | 1–20 | Estrategia de experimentación, principios básicos (réplica, aleatorización, bloques), pautas para diseñar experimentos |
| 2 | [cap-02-experimentos-comparativos-simples.md](cap-02-experimentos-comparativos-simples.md) | 21–59 | Pruebas t, z, F y ji-cuadrada, intervalos de confianza, tamaño de muestra, comparaciones pareadas |
| 3 | [cap-03-un-factor-anova.md](cap-03-un-factor-anova.md) | 60–125 | ANOVA de un factor, adecuación del modelo, transformaciones, contrastes, comparaciones múltiples (Scheffé, Tukey, LSD, Duncan, Newman-Keuls, Dunnett), curvas OC, Kruskal-Wallis |
| 4 | [cap-04-bloques-cuadrados-latinos.md](cap-04-bloques-cuadrados-latinos.md) | 126–169 | Bloques completos aleatorizados, cuadrado latino y grecolatino, bloques incompletos balanceados |
| 5 | [cap-05-introduccion-factoriales.md](cap-05-introduccion-factoriales.md) | 170–217 | Factorial de dos factores y general, interacción, una observación por celda, superficies con factores cuantitativos, bloques en factoriales |
| 6 | [cap-06-factorial-2k.md](cap-06-factorial-2k.md) | 218–286 | Diseños 2², 2³ y 2^k, contrastes y efectos, una sola réplica (gráficas de probabilidad, Lenth), efectos de dispersión, puntos centrales |
| 7 | [cap-07-bloques-confusion-2k.md](cap-07-bloques-confusion-2k.md) | 287–302 | Confusión del 2^k en 2, 4 y 2^p bloques, contraste de definición, confusión parcial |
| **8** | [cap-08-factoriales-fraccionados-2k-p.md](cap-08-factoriales-fraccionados-2k-p.md) | 303–362 y 663–679 | **Tema 6 del curso.** Fracciones 2^(k-1), 2^(k-2) y 2^(k-p), alias, resolución III/IV/V, aberración mínima, doblez, Plackett-Burman, bloques en fraccionados; Tabla XII del apéndice (26 diseños con generadores y alias) |
| 9 | [cap-09-factoriales-3k-niveles-mixtos.md](cap-09-factoriales-3k-niveles-mixtos.md) | 363–391 | Diseños 3^k, componentes de interacción, confusión y fracciones 3^(k-p), niveles mixtos |
| 10 | [cap-10-modelos-de-regresion.md](cap-10-modelos-de-regresion.md) | 392–426 | Mínimos cuadrados matricial, pruebas e intervalos, diagnósticos (PRESS, R-student, leverage, Cook), falta de ajuste |
| 11 (A) | [cap-11a-superficies-de-respuesta.md](cap-11a-superficies-de-respuesta.md) | 427–472 | Ascenso más pronunciado, análisis canónico, respuestas múltiples y deseabilidad, diseño central compuesto, Box-Behnken, bloques, diseños óptimos |
| 11 (B) | [cap-11b-mezclas-evop-diseno-robusto.md](cap-11b-mezclas-evop-diseno-robusto.md) | 472–510 | Experimentos con mezclas, operación evolutiva, diseño robusto (Taguchi y enfoque de superficie de respuesta) |
| 12 | [cap-12-factores-aleatorios.md](cap-12-factores-aleatorios.md) | 511–556 | Efectos aleatorios, componentes de la varianza, modelo mixto, reglas de cuadrados medios esperados, pruebas F aproximadas, estudios R&R |
| 13 | [cap-13-anidados-parcelas-subdivididas.md](cap-13-anidados-parcelas-subdivididas.md) | 557–589 | Diseños anidados, factores anidados y cruzados, parcelas subdivididas, doble subdivisión, franjas |
| 14 | [cap-14-otros-topicos.md](cap-14-otros-topicos.md) | 590–629 | Box-Cox, modelo lineal generalizado, datos no balanceados, análisis de covarianza, mediciones repetidas |

## Dónde buscar cada diseño o método

| Necesito… | Ficha |
|---|---|
| Comparar dos tratamientos | cap. 2 |
| Un factor con varios niveles; comparaciones múltiples | cap. 3 |
| Controlar una, dos o tres fuentes de variabilidad perturbadora | cap. 4 |
| Varios factores con todos los cruces | cap. 5 (general), cap. 6 (dos niveles), cap. 9 (tres niveles y mixtos) |
| Factorial 2^k que no cabe en un solo bloque | cap. 7 |
| Tamizado con muchos factores y pocas corridas | **cap. 8** (y cap. 9 para tres niveles) |
| Ajustar un modelo, diagnosticar, datos faltantes en un 2^k | cap. 10 |
| Optimizar una respuesta | cap. 11 (A) |
| Formulaciones o mezclas; robustez frente a factores de ruido | cap. 11 (B) |
| Factores aleatorios, componentes de la varianza, sistemas de medición | cap. 12 |
| Factores anidados o difíciles de cambiar | cap. 13 |
| Respuesta no normal, covariables, datos no balanceados | cap. 14 |

Para el tema 6, la ruta de lectura es: cap. 6 → cap. 7 → cap. 8, con el cap. 10 como apoyo
para el análisis por regresión.

## Fuente y limitaciones

- El PDF usado es un escaneo sin capa de texto (692 páginas); se leyó visualmente, página
  por página. El PDF no se guarda en el repositorio porque este es público.
- **Al escaneo le faltan diez páginas del libro**:
  - 136–137 (cap. 4): gráficas de residuales del ejemplo 4-1 e inicio de la discusión de aditividad.
  - 400–401 (cap. 10): cierre del ejemplo 10-1 y sus gráficas de residuales.
  - 576–577 (cap. 13): tabla 13-16 (ANOVA del ejemplo de parcelas subdivididas) y ecs. 13-16
    y 13-17. La tabla se recalculó a partir de los datos y está marcada como tal.
  - 628–631: problemas finales del cap. 14 e inicio de la bibliografía.
- Correspondencia entre página del libro y página del PDF: +15 (págs. 1–135), +13 (138–399),
  +11 (402–575), +9 (578–627), +5 (632 en adelante).
- Cada ficha marca las erratas aparentes del libro, las cifras dudosas y lo que es añadido
  propio (resúmenes operativos, fórmulas generales que el libro solo muestra con números).
- Las fichas dan los resultados clave de los ejemplos, pero en general **no copian las tablas
  de datos completas**. Excepción: los ejemplos pequeños del cap. 8 incluyen el vector de
  respuestas. Para reproducir otros ejemplos en software hay que tomar los datos del libro.
- No se transcribieron las tablas estadísticas del apéndice (I–XI: normal, t, ji-cuadrada, F,
  curvas OC, Duncan, rango studentizado, Dunnett, polinomios ortogonales, números
  aleatorios); esos valores se obtienen con software. La Tabla XII sí está, en la ficha del cap. 8.
- El material suplementario al que remite el libro (algoritmo de Yates, relaciones señal/ruido
  de Taguchi, doblez parcial, entre otros) no forma parte del PDF.
