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
  incluye efecto de dispersión.
- Montgomery, ej. 8-7 (pág. 340): 2^(7−4) de resolución III con doblez completo, tiempo de
  enfoque del ojo.

## Caso (investigación para el informe)
_Pendiente: elegir paper; enviarlo a los compañeros a más tardar el miércoles 28 oct 2026._

Candidatos de acceso abierto con DOI en `bibliografia/papers-factoriales-fraccionados.txt`
(20 referencias). Sugeridos: Cacua et al. (2017), nanofluidos, 2^(6−2) de resolución IV, en
español (DOI 10.33131/24222208.288); y Rezende et al. (2018), pretratamiento de biomasa,
2^(5−1) de resolución V (DOI 10.1186/s13068-018-1200-2). El diseño está tomado del resumen:
falta leer el texto completo.

## Ideas para la exposición
Primera versión lista en `exposicion-tema-06/` (presentación y guía de estudio). Sigue la
estructura de la profesora registrada en `notas/clases/`. Falta: verificar la parte de Minitab
en el programa, agregar el caso y contrastar con Gutiérrez–De la Vara.
