# Bitácora de sesiones de trabajo

Registro de cada sesión de trabajo en el repositorio: qué se hizo, qué decisiones se tomaron y
qué queda pendiente. La entrada más reciente va arriba.

## 2026-10-23 (viernes) — Protocolo del diseño de comparación simple para la asesoría del 24 oct

### Hecho
- `git pull`: llegó un commit de Sebastián que ignora las fotos de clase de WhatsApp (`.gitignore`).
- Juan Esteban informa que el autocorrelador ya mide la autocorrelación de los pulsos y que el láser
  es el **Calmar Carmel CFL-05RFFUNC** (780 nm, 0,5 W). Se buscó en la red el ancho de pulso del
  fabricante para varias corrientes: **no existe**; Calmar da un solo máximo (< 90 fs, sech², 0,65)
  en el punto nominal y el sufijo UNC no está documentado. Detalle en
  `notas/laser-carmel-x-ficha-tecnica.md`.
- Se escribió el protocolo del experimento (PDF) en
  `trabajo-practico/protocolo/Protocolo_Comparacion_Simple_Ancho_de_Pulso.pdf`, generado por
  `scripts/trabajo-practico/render_protocolo.py` + `build_protocolo.sh` (Chrome, como la guía del
  tema 6). Una primera versión proponía hipótesis (t de una muestra, una cola contra 90 fs; dos
  corrientes como t pareada) y tablas de n; Juan Esteban aclaró que el láser es un pedido a la
  medida (sufijo UNC), ajustable de 0 a 7,12 A, con **hoja de pruebas de fábrica propia** que da el
  ancho de pulso a cada corriente nominal, y **decidió no fijar ninguna prueba de hipótesis hasta
  tener esos valores exactos**. La versión final (15 págs.): lo que ya se sabe del fabricante;
  formularios en blanco para los datos que faltan (numeral 1 identidad del equipo y numeral 2
  ancho por corriente, indispensables; 3 y 4 complementarios); hipótesis marcadas "por definir";
  definición de réplica, piloto de 5 trazas y n pendiente; procedimiento de medición completo con
  hoja de registro y reglas de exclusión; análisis descriptivo y supuestos; cronograma; lista de
  aprobación.
- Juan Esteban confirmó datos del equipo: 780 nm, 50 MHz, salida en espacio libre, serie 881139. Se
  llenaron en el numeral 1 del protocolo y en la ficha del láser.
- A pedido de Juan Esteban se generó la **teoría completa del diseño de comparación simple** en PDF
  (33 págs.): `trabajo-practico/teoria/Teoria_Diseno_de_Comparacion_Simple.pdf`, con
  `scripts/trabajo-practico/render_teoria.py` + `build_teoria.sh` (markdown → HTML, fórmulas con
  KaTeX desde CDN, PDF con Chrome). Parte I: ficha del cap. 2 de Montgomery; parte II: ficha nueva
  del cap. 2 de Gutiérrez–De la Vara (`notas/gutierrez-de-la-vara/`, leída del PDF con texto);
  parte III: mapa de decisión, una o dos colas, secuencia del análisis, fórmulas en Python y
  errores frecuentes.
- **Noticia:** el láser será retirado del laboratorio. Juan Esteban pidió tomar todos los datos antes del
  30 oct 2026, en 3 o 4 días con varias réplicas por día, y dejar días libres para desmontar el montaje.
  El protocolo (16 págs.) quedó con: situación en la portada y el resumen; plan de 3–4 sesiones (lun 26 a
  jue 29 oct) con 5 réplicas nominales + 4 por cada una de dos corrientes reducidas por sesión (13 trazas/día);
  puesta a punto incluida en la sesión 1; medición a tres corrientes aunque la hoja de pruebas no aparezca;
  potencia calculada a posteriori; **sin medición de temperatura ni humedad** (no hay medidores; se anota la
  hora y se declara como limitación); cronograma reescrito; sin casillas de firma.
- El protocolo tiene ahora un **anexo A de ecuaciones** (KaTeX): deconvolución y eje de retardo,
  estimadores, estadísticos candidatos (t de una muestra, IC, pareada, F, t combinada, Welch, χ²), las
  cuatro formas del número mínimo de réplicas (curvas OC, aproximación normal, t no central, error
  máximo E) y una tabla de la δ detectable con el plan de 3–4 sesiones según σ. 16 págs.
- La teoría (parte III) tiene ahora el **esquema de los nueve casos**: árbol de decisión en SVG
  (parámetro → una o dos poblaciones → pareadas → varianza conocida → varianzas iguales), tabla de
  los nueve casos con H0, estadístico, distribución, rechazo, IC y fuente, y el protocolo común por
  grupo de casos. 25 págs.
- **Plan definitivo acordado con Juan Esteban** (17 págs.): prueba piloto separada el sábado 24 oct (15 trazas,
  5 por corriente en orden sorteado, cronometradas; σ previa = la mayor S de las tres); esa noche n por curva OC con σ previa
  conservadora (1,56·S, límite superior del 80 % con n = 5), δ = 10 fs, α = 0,05, potencia 0,90; tres sesiones
  lun 26 a mié 28 con 13 trazas/día (5 N + 4 R1 + 4 R2), orden completamente aleatorizado dentro del día;
  jueves 29 de reserva. El día no es factor: balanceado, queda en el error con opción de bloquear después.
  Prohibido agrupar las réplicas por corriente; compromiso de pares consecutivos si el cambio es lento.
- Se dejó por escrito en la sección 4 del protocolo la justificación de δ = 10 fs (error sistemático de la
  forma supuesta ≈ 8 fs; 11 % de potencia pico; alcanzable con el plan) y la distinción entre la δ que
  importa (entrada de la curva OC, decisión de ingeniería) y la δ detectable (salida con n fijo por el plazo);
  la tabla del sábado por la noche tiene casillas para ambas y para la comprobación δ_det ≤ 10 fs.
- A pedido de Juan Esteban, el anexo A del protocolo quedó **solo con las fórmulas del caso 2** (una media
  frente al valor del fabricante, varianza desconocida): se quitaron la t pareada, la F, la t combinada, Welch,
  χ² y las versiones de dos muestras del tamaño de muestra; la tabla A.5 es solo de una muestra (n = 12, 15, 20).
- **Corrección importante:** las tres corrientes del diseño son **nominales**, cada una con su patrón en la
  hoja de pruebas (no "una nominal y dos reducidas", que venía de la versión sin hoja). Se corrigió en todo el
  protocolo: 5 réplicas por corriente y por día (15 trazas/día), n = 15 por corriente en tres días (20 en
  cuatro), piloto de 5 por corriente, sorteo de I1×5, I2×5, I3×5, tabla A.5 con n = 10, 15 y 20.
- δ dejó de estar "en el aire": la sección 4 tiene una **regla de precedencia** para fijarla con datos del
  fabricante (tolerancia τ0 ± t → δ = t; valor medido y máximo garantizado → δ = τmáx − τ0; banda de
  aceptación; estabilidad % rms; y solo si no hay nada, 10 fs), con piso δ ≥ 2u si declara incertidumbre.
  La sección 2 tiene casillas para esos cinco datos y el correo a Calmar los pide explícitamente.
- **Reescritura completa del protocolo en lenguaje simple** para la profesora (18 págs.): frases cortas,
  sin historia interna ni referencias al repo, un cuadro "En una frase" en la portada, resumen de una página,
  secciones con títulos directos (¿Qué sabemos?, ¿Qué falta?, ¿Hipótesis?, ¿Réplicas?, ¿Cómo se mide?,
  ¿Cómo se analiza?, ¿Calendario?, ¿Qué aprobar?) y el anexo de fórmulas del caso 2. El generador
  `render_protocolo.py` se reescribió entero (cuerpo de `build`).
- Aclaración de Juan Esteban: el piloto del sábado es **solo 5 réplicas por corriente** (15 trazas en total),
  únicamente para estimar el número de réplicas del experimento real. Se reescribieron las cinco menciones
  (resumen, sección 4, cronograma y lista de aprobación) para que el 15 no se lea como "por corriente".
- Se quitaron del protocolo todas las cantidades de réplicas por día de los días de medición (lun–mié):
  el n por corriente se calcula el sábado por la noche con la curva OC y se reparte por igual entre
  corrientes y días. Solo queda fijo el piloto (5 por corriente, 15 en total). La tabla "Réplicas por día"
  quedó en blanco y la tabla A.5 pasó a ser de apoyo con n = 6, 8, 10, 12, 15 y 20.
- Por decisión de Juan Esteban se asume el autocorrelador como perfecto (no se escribe en el documento): se
  quitaron del protocolo el inventario de vidrio y la estimación del GDD, la calibración del eje de retardo,
  la verificación de linealidad del detector y el diagnóstico por chirp/instrumento. Queda: programa de
  análisis fijo, alineación verificada entre réplicas, barrido fijo, calentamiento y temperatura como limitación.
- Como las mediciones son en días seguidos, Juan Esteban decidió suponer que no habrá desalineaciones: se
  quitó la verificación pico/fondo de la definición de réplica, de los pasos de cada día y de cada réplica,
  de la hoja de registro y de las reglas de descarte. La réplica queda definida por bloquear el haz y
  reiniciar el barrido desde otra posición.
- Se verificó que calmarlaser.com (ya accesible) no tiene sección de soporte, descargas ni acceso
  con contraseña: la hoja de pruebas por corriente no está en la web, viaja con el equipo.

### Pendiente
- [ ] Llevar el protocolo a la asesoría del 24 oct y anotar las observaciones de la profesora.
- [ ] Sáb 24 oct: calibrar el eje de retardo, linealidad del detector, inventario óptico, script congelado;
      **piloto** (15 trazas, 5 por corriente, orden sorteado, cronometradas); por la noche S_piloto por corriente, n por curva OC, sorteo del orden de cada día.
- [ ] Lun 26 – mié 28 oct: sesiones 1–3 (13 trazas/día en orden sorteado); jue 29 de reserva; respaldar
      los archivos crudos en dos sitios.
- [ ] Leer la etiqueta del láser (serie, tasa de repetición, generación) y preguntar por la hoja de
      pruebas de fábrica; si no hay, escribir a sales@calmarlaser.com con el número de serie.
- [ ] Llenar los numerales 1 y 2 del protocolo con la etiqueta y la hoja de pruebas de fábrica
      (buscar en la caja, la memoria del software, la orden de compra o pedirla a Calmar con el
      número de serie); guardar las fotos en `bibliografia/laser-carmel/`.
- [ ] Con esos valores, escribir las hipótesis, los niveles de corriente y el n (siguiente asesoría).
- [ ] Registrar el protocolo en `trabajo-practico/bitacora-trabajo-practico.docx` (Parte I).
- [ ] Commit y push de los cambios de esta sesión y de las anteriores (hay archivos sin confirmar
      desde el 16 oct).

## 2026-10-16 (viernes) — Hoja de datos del láser para la exposición del 17 oct

### Hecho
- `git pull`: sin cambios.
- Juan Esteban identificó el láser: Calmar Laser, Carmel X (etiqueta "Carmel fiber laser
  controller"). Se bajaron las hojas de datos de todas las variantes (X-780, X-1550, X-780/1550,
  X-1030, X-515), el white paper de 2016 y el catálogo 2023 a `bibliografia/laser-carmel/`
  (ignorados por git). El sitio calmarlaser.com daba error 526; se usaron copias de archive.org.
- Resumen y tabla comparativa en `notas/laser-carmel-x-ficha-tecnica.md`; referencias [K1]–[K5]
  en `bibliografia/autocorrelador-intensidad-referencias.txt`.
- **Hallazgo clave:** el fabricante especifica el ancho como **máximo** ("< 90 fs" en 780 nm) y lo
  mide con autocorrelación de segundo armónico suponiendo sech² con factor 0,65 (nota 2 de la
  tabla, igual en todas las variantes). Por eso la hipótesis pasa a ser de una cola
  (H0: μ_τ = 90 fs; HA: μ_τ > 90 fs) y hay que deconvolucionar con la misma forma.
- Presentación regenerada (26 diapositivas): la 7 ya tiene la tabla con la hoja de datos y la
  traza de autocorrelación típica del fabricante (`figuras/fabricante_traza.png`, extraída del
  PDF con `scripts/trabajo-practico/ficha_laser.py`, que `build.sh` ejecuta si el PDF existe);
  la 22, la 23 (hipótesis de una cola) y la 25 se actualizaron en consecuencia. Se asumió la
  variante **X-780**; las cifras de la 1550 están en la nota por si fuera esa.
- `.venv` no tenía matplotlib ni python-pptx en este equipo; se instalaron.
- A pedido de Juan Esteban se quitaron de las diapositivas los recuadros "Pendiente" que
  quedaban (7, 10 y 22) y la fila "Medición de este equipo" de la tabla de la 7. Lo que falta
  averiguar sigue registrado abajo y en `notas/laser-carmel-x-ficha-tecnica.md`.

### Pendiente
- [ ] Leer en la etiqueta del controlador o del cabezal el modelo exacto (CFL-04/-10/-15RFF, doble
      salida RCFF, o X-1550) y la tasa de repetición; si no es 780 nm, cambiar las cifras de las
      diapositivas 7, 22 y 23 en `render_pptx.py` con la tabla de la nota.
- [ ] Preguntar en el laboratorio si el láser vino con hoja de pruebas de fábrica (con fecha) y
      cuántas horas de uso lleva.
- [ ] Revisar la diapositiva 7 abriendo el pptx en PowerPoint (aquí no hay LibreOffice para
      renderizar). El esquema real del montaje (diapositiva 10) sigue sin confirmarse.

## 2026-10-15 (jueves) — Trabajo práctico: referencias y estructura de la exposición del 17 oct

### Hecho
- Tema del trabajo práctico: autocorrelador de intensidad para medir anchos de pulso. El sábado
  17 oct se expone el conocimiento no estadístico (física del experimento y factores que cambian
  el ancho medido).
- `bibliografia/autocorrelador-intensidad-referencias.txt`: 58 referencias con DOI verificado en
  Crossref, más un mapa preliminar de factores.
- `trabajo-practico/estructura-exposicion-no-estadistica.md`: estructura de 22 diapositivas en
  seis bloques, títulos en forma de pregunta, con referencias, figuras por preparar y reparto
  propuesto entre los dos expositores.

### Pendiente
- [ ] Conseguir los libros de la sección A de las referencias (Diels–Rudolph primero).
- [ ] Completar los datos del montaje marcados con ⚠ en la estructura (láser, detector,
      geometría, barrido, ópticas, espectrómetro, parámetros variables).
- [ ] Armar las diapositivas y las figuras; registrar el tema en la bitácora del .docx.

### Hecho (continuación)
- Se creó `bibliografia/papers/` con seis PDF (Diels–Rudolph, Sala, Chung–Weiner, Ratner,
  Donnelly–Grossman, Monmayrant). `.gitignore` ahora excluye `bibliografia/**/*.pdf`.
- **Enfoque decidido:** el trabajo práctico es un diseño de comparación simple, técnica de
  intensidad frente al patrón (datos del fabricante), para calibrar y diagnosticar el láser. Los
  factores que cambian el ancho se exponen completos, pero se fijan; estudiarlos es trabajo futuro.
- Se reestructuró la exposición (25 diapositivas) hacia ese argumento y se verificaron las cifras
  contra los PDF, con página. Corrección: Δν·τₚ de la lorentziana es 0,2206 (Sala, tabla II), no
  0,142; el factor 2,0 de la lorentziana no está en Diels–Rudolph, solo en Sala.

### Pendiente (continuación)
- [ ] Conseguir la ficha técnica del láser (ancho nominal, cómo lo midió el fabricante).
- [ ] Confirmar en Haus (1975) que el absorbedor saturable rápido da pulsos sech².

### Hecho (presentación)
- Se generó la presentación de la exposición del 17 oct (26 diapositivas):
  `trabajo-practico/exposicion-17-oct/Autocorrelador_Fundamentos_y_Calibracion.pptx`. Se
  regenera con `scripts/trabajo-practico/build.sh` (figuras simuladas en `figuras.py`, diapositivas
  en `render_pptx.py`). Fuente: Bahnschrift (Windows 10/11), ecuaciones en Cambria Math. Notas del
  orador con la explicación y las páginas de cada fuente. Revisada exportando desde PowerPoint.
- Se recreó `.venv` (python-pptx, matplotlib, numpy, scipy, pymupdf).

### Pendiente (presentación)
- [ ] Llenar la diapositiva 7 (ficha técnica del láser) y los recuadros "Pendiente" de las
      diapositivas 10 (esquema real) y 22 (valores del patrón y n).

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
