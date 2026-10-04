# Diseño de Experimentos

Proyecto de seguimiento de la materia **Diseño de Experimentos Avanzados (3008475)**,
Universidad Nacional de Colombia, semestre 2026-II. Profesora: Faviana Gutiérrez Rôa.

## Propósito

Seguir las temáticas, talleres y entregables de la materia. El usuario aporta bibliografía,
diapositivas con la teoría y software para los análisis. Las reglas completas del curso, el
calendario y la bibliografía están en `notas/generalidades-del-curso.md` — **leerlo antes de
preparar cualquier entregable**.

## Equipo y tema asignado

- Equipo: **Juan Esteban Rodríguez Ochoa** (usuario) y **Sebastián Zapata Henao**.
- Tema a exponer: **Tema 6 — Diseños Factoriales Fraccionados**, sábado **31 de octubre de 2026**.
- El repo es público y se usa para compartir avances con el compañero de equipo.

## Entregables del equipo (ver fechas exactas en las notas)

1. Exposición del tema 6 (ppt, 25%) — enviar 1 día antes (30 oct 2026).
2. Informe del caso del tema 6 (doc, ICONTEC, 20%) — el día de la exposición; el paper del
   caso se envía a los compañeros el miércoles previo (28 oct 2026).
3. Trabajo práctico de libre elección: exposición (ppt, 20%) + informe (doc, ICONTEC, 15%),
   12 dic 2026. Tema elegido el 26 sep, problema definido el 17 oct.
4. Taller (doc, 20%) — se recibe el 21 nov, se entrega el 5 dic 2026.

Todo se envía a doe_unal@yahoo.com. Retraso: −10 % por día, máximo 3 retrasos.

## Convenciones

- Idioma de notas, README y commits: español.
- Cada taller va en `talleres/taller-NN-<tema>/` con su enunciado, datos, código y solución.
- Los datos crudos van en `datos/`; no se modifican, se procesan desde `scripts/` o el taller.
- Bibliografía y diapositivas se guardan tal cual se reciben (PDF, PPTX, etc.). Los PDF de
  `bibliografia/` están ignorados por git (libros con derechos de autor; el repo es público).
- El trabajo práctico se documenta en `trabajo-practico/bitacora-trabajo-practico.docx`
  (Parte I bitácora, Parte II borrador del informe). Es binario: no editarlo en paralelo.
- Lo que se lea del tema 6 se acumula en `notas/tema-06-factoriales-fraccionados.md`
  (con fuente y página) para construir la exposición y el informe del caso.
- Al cerrar cada sesión, registrar lo hecho y lo pendiente en `notas/bitacora-sesiones.md`.
- Antes de resolver un taller o preparar la exposición, consultar las diapositivas y la
  bibliografía del tema; para el tema 6, priorizar Montgomery y Gutiérrez–De la Vara.
- **Montgomery ya está leído y resumido** en `notas/montgomery/` (una ficha técnica por
  capítulo; índice en `notas/montgomery/README.md`). Consultar la ficha del capítulo que
  haga falta en lugar de volver a leer el libro; el PDF es un escaneo sin texto y no está en
  el repo. El tema 6 corresponde a `cap-08-factoriales-fraccionados-2k-p.md`.
- **Las diapositivas de la profesora** están transcritas en `notas/clases/` (una nota por tema,
  con una sección final "Estructura didáctica de la profesora"). Las exposiciones del equipo
  siguen esa estructura: títulos en forma de pregunta, hipótesis como H0/HA, tablas ANOVA con
  columnas SV, SS, DF, MS, F0, P-Value, supuestos con prueba gráfica y analítica, y Minitab.
- **Exposición del tema 6**: presentación y guía de estudio en `exposicion-tema-06/`; se
  regeneran desde `scripts/tema-06/` (el contenido de ambas está en `contenido.py`).
- Los informes siguen Normas ICONTEC y deben incluir siempre: planteamiento del problema,
  justificación del diseño, plan experimental, análisis e interpretación, validación de
  supuestos, conclusiones y recomendaciones.
- Los resultados de análisis se reportan de forma literal (tablas ANOVA, p-valores, efectos),
  no resumidos.
- **Nunca subir al repo datos personales de terceros** (la lista de equipos con cédulas y
  correos, `notas/DOE - Equipos*.pdf`, está ignorada por git y se conserva solo localmente).
