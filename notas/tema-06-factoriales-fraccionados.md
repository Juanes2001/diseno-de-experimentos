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

## Ideas para la exposición
Versión del 25 oct 2026 en `exposicion-tema-06/` (presentación de 104 diapositivas y guía, solo teoría, sin Minitab; cada ejemplo abre con una diapositiva de enunciado: situación, objetivo y lo que se pide), organizada en el orden del capítulo 8: propósito y vocabulario, resolución, fracción un medio, secuencias, fracción un cuarto, caso general (análisis, proyección, bloques), resolución III (doblez, Plackett-Burman), resolución IV y V y cierre. Sigue la
estructura de la profesora registrada en `notas/clases/`. Falta:
agregar el caso y contrastar con Gutiérrez–De la Vara.
