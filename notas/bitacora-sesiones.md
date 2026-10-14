# Bitácora de sesiones de trabajo

Registro de cada sesión de trabajo en el repositorio: qué se hizo, qué decisiones se tomaron y
qué queda pendiente. La entrada más reciente va arriba.

## 2026-10-13 (martes) — Notación del 2^k en la exposición del tema 6

### Hecho
- Se hizo `git pull`: Sebastián subió `bibliografia/autocorrelador-intensidad-referencias.txt`.
- Al leer la guía, Juan Esteban notó que la diapositiva "La fracción un medio" usa la tabla de
  signos del 2³ y las etiquetas (1), a, b, ab… sin explicarlas. Se agregaron dos diapositivas al
  inicio de la sección 3 (ahora son las 13 y 14; la presentación queda en 67):
  - "¿Cómo se lee la tabla de un factorial 2^k?": columnas en mayúsculas (factores y efectos),
    filas en minúsculas (combinaciones de tratamientos), letra presente = nivel alto, (1) = todo
    bajo, orden estándar (Yates), la minúscula también denota la respuesta observada, la I se
    reserva para la identidad (fuente: Montgomery, cap. 6, secs. 6-2 a 6-4, págs. 218–240).
  - "¿Cómo se completa la tabla de signos del 2^k?": columnas de interacción como producto de
    signos, columna I, balance N/2, producto de columnas y letra² = I, ortogonalidad y contraste.
- Se regeneraron el PPTX y el PDF con `scripts/tema-06/build.sh` y se revisaron las dos
  diapositivas nuevas exportadas desde PowerPoint y las páginas 10–11 de la guía.

### Pendiente
- [ ] Seguir leyendo la guía y anotar qué más falta explicar (la exposición asumía conocida la
      maquinaria del 2^k del tema anterior; conviene revisar también Yates y la gráfica normal).
- [ ] Hacer commit y push de los cambios para que Sebastián los vea.

## 2026-10-11 (domingo) — Corroboración de la exposición del tema 6 contra Montgomery

### Hecho
- Se leyó de nuevo, página por página sobre el escaneo, el capítulo 8 completo (págs. 303–350;
  las 351–362 son problemas) y las págs. 242–243 y 254–255 del cap. 6 (procedimiento de
  análisis, tabla ANOVA del 2^k y método de Lenth), y se cotejó cada diapositiva y cada apartado
  de la guía (47 págs.). Toda la teoría, las definiciones, los generadores, las relaciones de
  definición, las cadenas de alias, las tablas 8-13, 8-14 y 8-29, los renglones de Plackett-Burman
  y las citas al libro coinciden con el texto.
- Se recalcularon desde los datos del libro todas las cifras de los cuatro ejemplos (efectos,
  contrastes, SS, ANOVA, F y p, R², R² ajustado y predicho, Lenth, Anderson-Darling, F* de
  dispersión, Bartlett, fracción alterna y doblez). Todo coincide con la guía y con el libro.
  Se confirman las tres erratas del libro ya anotadas (tabla 8-14, ejemplo 8-7, tabla 8-6).
- Correcciones hechas: (1) la guía decía que el principio de jerarquía no está en Montgomery;
  sí lo nombra en el ejemplo 8-6 (pág. 335), se corrigió en `contenido.py`; (2) la salida de
  Minitab de la pág. 45 de la guía salía recortada por la derecha (sin la columna Valor p ni el
  R² predicho) porque el bloque de texto fijo no cabía en media página; `render_guia.py` ahora
  apila esos bloques a todo el ancho. Se regeneraron el pptx y el PDF.
- `build.sh` ahora genera el PDF con Chrome sin abrirlo (ruta de Windows desde WSL) y usa el
  entorno `.venv` (pymupdf, python-pptx, numpy, scipy; ignorado por git).

### Pendiente
- Los mismos pendientes de la sesión del 3 de octubre (Minitab real, paper del caso, caso en la
  presentación, Gutiérrez–De la Vara, envío el 30 oct).

## 2026-10-03 (sábado) — Clase 6: bloques, latinos y grecolatinos; preparación del tema 6

### Hecho
- Se leyó completo el libro de Montgomery (2.ª ed. en español, escaneo sin capa de texto) y se
  dejó una ficha técnica por capítulo en `notas/montgomery/` (índice en su `README.md`). La
  ficha del capítulo 8 incluye la Tabla XII de alias del apéndice.
- Al escaneo le faltan diez páginas del libro: 136–137, 400–401, 576–577 y 628–631. El detalle
  de qué se perdió está en `notas/montgomery/README.md`. Los capítulos 6, 7 y 8 están completos.
- Se transcribió el contenido de las diapositivas de la profesora de los temas 2 (un solo
  factor) y 3 (bloques, latinos y grecolatinos) en `notas/clases/`, con su estructura didáctica.
- Se construyó la exposición del tema 6 en `exposicion-tema-06/`: presentación (65
  diapositivas) y guía de estudio en PDF (45 páginas). Ambas se generan desde
  `scripts/tema-06/contenido.py`. Los cuatro ejemplos son de Montgomery (8-1, 8-2, 8-4 y 8-7,
  más la fracción alterna del 8-3) y todas las cifras se recalcularon desde los datos.
- Se buscaron artículos de acceso abierto que usan factoriales fraccionados para el caso del
  informe: 20 referencias con DOI en `bibliografia/papers-factoriales-fraccionados.txt`.
- Se contrastó toda la presentación y la guía contra las páginas del libro (caps. 3, 6 y 8) y
  la parte de Minitab contra la documentación de soporte de Minitab en español. No se encontró
  ningún error de cifras, tablas, generadores ni alias. Se corrigieron imprecisiones de redacción
  (definiciones de generador y palabra, proyección, hipótesis por cadena, alcance del doblez,
  Plackett-Burman, supuestos) y términos de Minitab ("Plegar diseño", "Normales (absolutos)",
  "Gráfica de cubo", "R-cuadrado"). La guía indica ahora qué no proviene del libro: las ANOVA de
  los ejemplos 1 y 3, Lenth en el ejemplo 2, Anderson-Darling, Durbin-Watson y Bartlett.
- Erratas del libro detectadas: la tabla 8-14 imprime el 2^(7−3) como resolución III (es IV);
  el ejemplo 8-7 imprime −1.53 donde los datos dan −1.13; la tabla 8-6 intercambia los nombres
  de los factores B y C del ejemplo 8-2.
- Confirmados contra el libro: los nombres de los factores del ejemplo 1 (pág. 246) y el año de
  la edición (© 2004, Limusa).

### Pendiente
- [ ] Correr el ejemplo 1 en Minitab, comparar con la salida de la diapositiva 60 y reemplazar
      las tablas dibujadas por capturas reales. Las rutas de menú y los nombres de opciones ya
      se cotejaron con la documentación de Minitab, pero no en el programa (no estaba instalado
      en el equipo donde se armó la presentación).
- [ ] Elegir el paper del caso entre los candidatos, leer el texto completo y confirmar diseño,
      ANOVA y supuestos. Enviarlo a los compañeros a más tardar el miércoles 28 oct 2026.
- [ ] Agregar el caso a la presentación (las reglas piden que la exposición lo incluya).
- [ ] Consultar Gutiérrez–De la Vara, cap. 8: la presentación solo usa Montgomery.
- [ ] Decidir si se suben al repo las fotos de las diapositivas de la profesora
      (`notas/Diseño de un solo factor/` y `notas/Diseño por bloques Latino y grecolatino/`);
      por ahora están solo en local.
- [ ] Enviar el ppt al correo de la materia el viernes 30 oct 2026.

## 2026-09-26 (sábado) — Clase 5: Diseños de un Solo Factor

### Hecho
- Se revisaron las reglas del curso directamente en `DOE - Generalidades.pdf` y
  `DOE - Programa Calendario.pdf`.
- Aclaración: el trabajo práctico **no tiene un informe aparte** sobre aspectos no estadísticos.
  Solo tiene dos entregas con nota, ambas el 12 dic 2026: informe (doc, ICONTEC, 15%) y
  exposición (ppt, 20%). Lo no estadístico (planteamiento con referencias, ejecución detallada,
  dificultades) va **dentro** del informe final. Los hitos "Elegir tema" (26 sep) y "Definir
  problema" (17 oct) no tienen formato ni nota asignados en los documentos del curso.
- Se creó `trabajo-practico/bitacora-trabajo-practico.docx`: bitácora (sesiones, corridas,
  materiales) + borrador del informe final con el contenido mínimo exigido, formato ICONTEC.
- Los PDF de `bibliografia/` quedan fuera del repo (`.gitignore`) por derechos de autor.
  Localmente están: Montgomery, Gutiérrez–De la Vara y Atkinson (1993).
- Se creó `notas/tema-06-factoriales-fraccionados.md` para acumular lo que se lea del tema 6.

### Pendiente
- [ ] Agregar a Sebastián como colaborador del repo (GitHub → Settings → Collaborators).
- [ ] Compartir con Sebastián los PDF de bibliografía por fuera del repo (Drive, etc.).
- [ ] **Elegir el tema del trabajo práctico** (vence hoy, 26 sep) y registrarlo en la bitácora.
- [ ] Confirmar con la profesora si "Elegir tema" / "Definir problema" requieren algo escrito.
- [ ] Confirmar la ciudad en la portada del .docx (se puso Medellín, por el aula M8B).
- [ ] Empezar la lectura del tema 6 (Montgomery cap. 8, Gutiérrez–De la Vara cap. 8).
- [ ] Buscar el paper del caso del tema 6 (enviarlo a los compañeros a más tardar el 28 oct).
