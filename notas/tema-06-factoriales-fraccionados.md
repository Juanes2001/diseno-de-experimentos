# Tema 6 — Diseños Factoriales Fraccionados

Apuntes acumulados de la lectura del tema, para construir la exposición (ppt, enviar el
30 oct 2026) y el informe del caso (doc ICONTEC, 31 oct 2026). Cada apunte indica su fuente
(autor, capítulo y página).

## Fuentes prioritarias
- Montgomery, D. C. (2005). *Design and Analysis of Experiments*, cap. 8.
- Gutiérrez Pulido, H. y De la Vara Salazar, R. (2008). *Análisis y Diseño de Experimentos*, cap. 8.
- Complementarias: Box-Hunter-Hunter (cap. 6), Gunst y Mason, Wu y Hamada (caps. 5–6).

## Teoría
- Montgomery, cap. 8 (págs. 303–362) y Tabla XII del apéndice (págs. 663–679): ficha completa en
  `notas/montgomery/cap-08-factoriales-fraccionados-2k-p.md`. Base previa: cap. 6
  (`cap-06-factorial-2k.md`) y cap. 7 (`cap-07-bloques-confusion-2k.md`); separación de alias por
  regresión en el cap. 10 (`cap-10-modelos-de-regresion.md`, ejemplo 10-5).
- Gutiérrez–De la Vara, cap. 8: _pendiente de leer._

## Ejemplos resueltos
Recalculados desde los datos en `scripts/tema-06/contenido.py` (coinciden con el libro):
- Montgomery, ej. 8-1 (pág. 308): 2^(4−1) de resolución IV, índice de filtración; y ej. 8-3
  (pág. 315): fracción alterna que separa AC de BD y AD de BC.
- Montgomery, ej. 8-2 (pág. 311): 2^(5−1) de resolución V, rendimiento de un circuito integrado.
- Montgomery, ej. 8-4 (pág. 319): 2^(6−2) de resolución IV, contracción en moldeo por inyección;
  el libro incluye un análisis de efecto de dispersión (C), que se dejó fuera de la exposición porque no es
  teoría de fraccionados (viene de los caps. 3 y 6).
- Montgomery, ej. 8-7 (pág. 340): 2^(7−4) de resolución III con doblez completo, tiempo de
  enfoque del ojo.
- Montgomery, ej. 8-5 (pág. 327): elección de un 2^(7−3) de resolución IV para siete factores.
- Montgomery, ej. 8-6 (pág. 332): 2^(8−3) de resolución IV en cuatro bloques, máquina CNC (ANOVA
  literal de la tabla 8-18).
- Montgomery, ej. 8-8 (pág. 345): Plackett-Burman de 12 corridas con datos simulados (efectos
  recalculados; la tabla 8-26 imprime 12.667 para C, el valor correcto es 13.667).

## Caso (investigación para el informe)
_Pendiente: elegir paper; enviarlo a los compañeros a más tardar el miércoles 28 oct 2026._

Candidatos de acceso abierto con DOI en `bibliografia/papers-factoriales-fraccionados.txt`
(20 referencias). Sugeridos: Cacua et al. (2017), nanofluidos, 2^(6−2) de resolución IV, en
español (DOI 10.33131/24222208.288); y Rezende et al. (2018), pretratamiento de biomasa,
2^(5−1) de resolución V (DOI 10.1186/s13068-018-1200-2). El diseño está tomado del resumen:
falta leer el texto completo.

Búsqueda del 28 oct 2026 orientada a **electrónica y física** (sección E del mismo archivo, refs. 21–33).
Con el PDF leído y el diseño confirmado: Liu y Shrauner (2010), grabado por plasma de contactos de SiO2,
2^(5−1) con 16 corridas, regresión con interacciones dobles pero sin ANOVA (DOI 10.4283/jmag.2010.15.3.132);
Narula y Tan (2018), grafeno por PECVD, 2^(5−2) de resolución III, ANOVA en Minitab (DOI
10.3389/fmats.2018.00043); Figueroa et al. (2023), recubrimientos de h-BN, 2^(5−2) de resolución III con
tabla de alias y ANOVA (DOI 10.3390/nano13232992); Ning et al. (2020), Sb2Te3 por láser pulsado, 2^(5−1)
con E = ABCD y ANOVA (DOI 10.1016/j.actamat.2020.09.035, preprint arXiv 2009.05957); Verkouteren y Klouda
(1992), blancos de grafito para espectrometría de masas con acelerador, 2^(4−1) (DOI
10.1017/S0033822200063517). Bartsch et al. (2018), AlN por pulverización, es un fraccionado a **tres**
niveles (sirve para la presentación 3^k). En español no apareció nada de electrónica ni física.

Búsqueda del mismo día orientada a **mecatrónica** (sección F, refs. 34–40). El mejor es Şirinterlikçi et
al. (2009), exactitud y repetibilidad de un robot Fanuc M16iL: 2^(6−2) de resolución IV, 16 corridas, gráfico
de Daniel, ANOVA con p-valores, transformación logarítmica por residuales, alias explícitos; escrito para un
curso de DOE (The Technology Interface Journal, sin DOI, PDF libre en tiij.org). También Cui et al. (2023),
motor síncrono de imanes permanentes, 2^(6−2) IV por elementos finitos con análisis de alias y Pareto
(DOI 10.3390/electronics12245024). Freeman y Bauer (2026), hexápodo con aprendizaje por refuerzo,
fracciones 1/4 y 1/8 de un 2^7 (DOI 10.1177/17298806261431893, solo resumen). Ojo: en robótica casi
todo lo que dice "fractional" es control de orden fraccionario, no diseño fraccionado.

### Caso elegido (28 oct 2026): Cui et al. (2023), motor PMSM
PDF en `exposicion-tema-06/electronics-12-05024.pdf` (CC BY). Leído completo. Lo que usa del tema 6:
- 6 factores geométricos a dos niveles (tabla 1), 2^(6−2) con **E = ABC y F = BCD** (verificado con las 16
  corridas de la tabla 3): es exactamente el diseño del ejemplo 3 de la presentación (Montgomery, ej. 8-4,
  tabla 8-14), misma relación de definición I = ABCE = BCDF = ADEF y mismas 7 cadenas dobles (tabla 4 del
  paper = alias del ejemplo 3). Una sola réplica, 16 corridas por elementos finitos, orden estándar y orden
  de corrida (tabla 3).
- Justifica la resolución con una tabla corridas × factores (tabla 2 del paper), equivalente a la
  diapositiva «¿Cuántos factores caben en N corridas?» y a «Diseños recomendados hasta 32 corridas».
- Análisis: Pareto de efectos estandarizados con margen de error de Lenth (ME = t·PSE, ec. 2), «representante»
  de cada cadena, atribución por jerarquía y herencia (AC + BE → BE porque E es fuerte; AE + BC → A porque B y
  C no son activos). Sube α a 0.10 en el rizado para no quedarse con un solo factor. Gráficos de medias por
  nivel (= gráficos de efectos principales) como confirmación cualitativa.
- Después del tamizado sale del tema 6: diseño central compuesto de caras centradas en Minitab 20 sobre los 5
  factores activos, modelos cuadráticos (ec. 7–9, R² 98.7–100 %), optimización multiobjetivo con un algoritmo
  de lobo gris y validación con un prototipo en banco (par 117.85 N·m, rizado 12.70 %).
- **Lo que el paper NO trae** y el informe debe completar: tabla ANOVA, p-valores, residuales y validación de
  supuestos del fraccionado; tampoco dice cómo estimó el error para el Pareto. Recalculado con
  `scripts/tema-06/caso_cui.py` (Lenth, α = 0.05): eficiencia → E, A, D, F y AF = DE activos (el paper
  agrega AC = BE, que con Lenth queda por debajo del ME: 0.0385 < 0.0530); par medio → F, E, D, A, AE = BC,
  AD = EF, AF = DE (coincide con el paper); rizado → A, D, AF = DE y E ya al 5 % (el paper solo ve A al 5 % y
  necesita α = 0.10). La diferencia sugiere que el paper estimó el error con los 2 g.l. de las columnas de
  interacciones triples en vez de Lenth puro; conviene decirlo en el informe y presentar las dos lecturas.
- Como las corridas son simulaciones determinísticas, no hay aleatorización física ni error experimental
  puro: el «error» del ANOVA son los efectos despreciados (diapositiva «Sin réplicas no hay error»).

### Caso alternativo (28 oct 2026): Şirinterlikçi et al. (2009), robot Fanuc M16iL
PDF en `exposicion-tema-06/TechnologyInterface-RepeatabilityandAccuracyofanIndustrialRobot.pdf`
(The Technology Interface Journal, vol. 9, n.º 2, ISSN 1523-9926; sin DOI). Leído completo, 10 págs.
- **Mismo 2^(6−2) IV** que el ejemplo 3 y que Cui. El paper no escribe los generadores, pero sus cadenas de
  alias (SW = PD, SM = DI, PI = WM, SP = WD, PM = WI) solo salen de I = SPWD = SMDI = PWMI, que con
  S = A, P = B, W = C, M = D, D = E, I = F es I = ABCE = BCDF = ADEF (E = ABC, F = BCD). Verificado.
- **Errata detectable con lo de la clase**: la fila «SC = PW = MD» de la tabla 5 no existe (no hay factor C);
  la cadena correcta es SD = PW = MI (es AE = BC = DF). Las otras seis cadenas están bien.
- Lo que coincide con la presentación: planeación con factores de control, mantenidos constantes y de
  ruido (Coleman y Montgomery; tablas 1–3) ≈ protocolo de 8 pasos; dos niveles, resolución IV elegida
  para separar principales de dobles; 16 corridas aleatorizadas, una réplica del diseño (35 repeticiones
  de posicionamiento por corrida solo para calcular AP y RP); gráfica de Daniel para descartar efectos,
  efectos descartados agrupados como error (9 g.l. en exactitud, 8 en repetibilidad) y ANOVA con SS, DOF,
  MS, F y p (tablas 4 y 5); hipótesis y decisión por cadena («no se puede saber si es SP o WD, por los
  alias, como explica Montgomery»); transformación logarítmica de la exactitud porque los residuales no
  eran normales; modelo de regresión con coeficientes (ec. 6 y 7); cita Montgomery 6.ª ed.
- Lo que el paper NO trae: los 16 datos, la matriz de diseño, la tabla de efectos, la gráfica de Daniel y las
  gráficas de residuales (solo las describe). Los |efectos| se recuperan de las SS (|efecto| = √SS/2):
  exactitud M 1.24, S 0.77, SM = DI 0.31; repetibilidad SP = WD 0.167, M 0.162, SM = DI 0.105.
- **Inconsistencia interna**: los coeficientes de las ecuaciones 6 y 7 son exactamente 1/4 de los que
  implican las SS de las tablas 4 y 5 (razón 4.00 en los cuatro términos). Las F y los p-valores no cambian
  con un factor de escala común, así que las conclusiones se sostienen, pero el informe debe señalarlo.
- Como caso para el informe es más corto y más didáctico que Cui (fue escrito para un curso de DOE), y
  permite reproducir la ANOVA desde las SS; pero no se pueden recalcular efectos ni residuales sin los datos.
  Cui sí publica los 16 datos pero no la ANOVA. Son complementarios.

## Ideas para la exposición
Versión del 25 oct 2026 en `exposicion-tema-06/` (presentación de 104 diapositivas y guía, solo teoría, sin Minitab; cada ejemplo abre con una diapositiva de enunciado: situación, objetivo y lo que se pide), organizada en el orden del capítulo 8: propósito y vocabulario, resolución, fracción un medio, secuencias, fracción un cuarto, caso general (análisis, proyección, bloques), resolución III (doblez, Plackett-Burman), resolución IV y V y cierre. Sigue la
estructura de la profesora registrada en `notas/clases/`.

Segunda parte (26 oct 2026): el tema también cubre los fraccionados 3^k, así que hay una presentación
aparte del capítulo 9, `Tema6_Factoriales_3k.pptx` (69 diapositivas) con su guía, generada con
`scripts/tema-06/build.sh 3k` desde `contenido_3k.py`; ficha del capítulo en
`notas/montgomery/cap-09-factoriales-3k-niveles-mixtos.md`. Se unirán cuando ambas estén editadas. Falta:
agregar el caso y contrastar con Gutiérrez–De la Vara.
