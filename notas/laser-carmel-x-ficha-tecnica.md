# Láser del trabajo práctico: Calmar Laser, Carmel X (fibra, femtosegundos)

Hoja de datos consultada el 16 de octubre de 2026 para la diapositiva 7 de la exposición del
17 oct ("¿Qué especifica el fabricante y cómo lo midió?"). El equipo del laboratorio tiene la
etiqueta "Carmel fiber laser controller" (el controlador de rack 19", 2U); el modelo exacto
(sufijo CFL-xx, longitud de onda y tasa de repetición) **falta confirmarlo en la etiqueta del
controlador o del cabezal**. Mientras tanto se asume el **Carmel X-780**, que es la variante
original de la familia (el white paper de 2016 describe el Carmel como láser de 780 nm con
1550 nm opcional) y la más común en laboratorios de investigación.

## Fuentes (PDF en `bibliografia/laser-carmel/`, ignorados por git)

El sitio calmarlaser.com respondía con error 526 de Cloudflare el 16 oct 2026; los PDF se
bajaron de las copias de archive.org (URL original → copia):

| Documento | URL original | Copia archive.org |
|---|---|---|
| Carmel X-780, Rev. E, 10/1/2025 | calmarlaser.com/docs/datasheets/high_power/Carmel.780.pdf | web.archive.org/web/2026id_/… (misma ruta) |
| Carmel X-1550, Rev. B, 12/1/2025 | …/high_power/Carmel.1550.pdf | web.archive.org/web/20260309062640/… |
| Carmel X-780/1550, Rev. B, 05/01/2023 | …/high_power/Carmel.780-1550.pdf | web.archive.org/web/20260510003657/… |
| Carmel X-1030, Rev. B, 5/1/2023 | …/high_power/Carmel.1030.pdf | web.archive.org/web/20240524031831/… |
| Carmel X-515, Rev. B, 1/1/2024 | …/high_power/Carmel.515.pdf | web.archive.org/web/2026id_/… |
| White paper "Carmel X-series", Rev. 1.2, feb. 2016 | calmarlaser.com/docs/Carmel White Paper Rev 1.2 Feb 2016.pdf | web.archive.org/web/20241202084634/… |
| Catálogo Calmar Laser 2023 (71 págs.; Carmel en págs. 4–23) | calmarlaser.com/docs/datasheets/Calmar_Laser_Catalog_2023.pdf | web.archive.org/web/20260510003657/… |

Las hojas de datos tienen 4 páginas: (1) descripción, (2) tabla de especificaciones con notas al
pie, (3) "Optical Characterization" (traza de autocorrelación, espectro, perfil del haz y
estabilidad de potencia típicos), (4) dimensiones mecánicas.

## El dato clave para el experimento (cómo mide el fabricante)

Nota al pie 2 de la tabla de especificaciones, idéntica en todas las variantes:

> "A sech² pulse shape (deconvolution factor of 0.65) is used to determine the pulse width from
> the second harmonic autocorrelation trace."

Es decir: el fabricante mide con **autocorrelación de segundo armónico** (la misma técnica del
trabajo práctico) y convierte el FWHM de la traza al ancho del pulso con **τ_p = 0,65 · τ_AC**,
que es 1/1,543 de la sech² (Sala et al., tabla II; Diels y Rudolph). Para que la comparación sea
justa, hay que deconvolucionar con la misma forma.

Además:
- El ancho de pulso se especifica como **máximo** ("< 90 fs" en 780 nm, "< 100 fs" en 1030 y
  1550 nm), no como valor nominal: la hipótesis de la comparación es **de una cola**
  (H_A: μ_τ > τ_fab).
- Las especificaciones están "subject to change without prior notice" (nota 1), y la tasa de
  repetición de los modelos -04 y -05 se fija al comprar (nota 4): hay que leer el modelo en la
  etiqueta.
- El white paper (2016, pág. 4) afirma que "Pulse shape is transform-limited, and the pedestal is
  typically 20 dB lower than the signal"; la tabla del white paper (pág. 5) pone "Minimum Pulse
  Width < 90" con la misma nota sobre sech² y 0,65.
- No se encontró ninguna hoja de pruebas de fábrica de un equipo concreto; eso solo lo tiene el
  laboratorio, si vino con el equipo.

## Especificaciones ópticas por variante (página 2 de cada hoja de datos)

| Parámetro | X-780 (Rev. E 2025) | X-780/1550 (Rev. B 2023) | X-1550 (Rev. B 2025) | X-1030 (Rev. B 2023) | X-515 (Rev. B 2024) |
|---|---|---|---|---|---|
| Modelos | CFL-04RFF, -10RFF, -15RFF | CFL-04RCFF, -05RCFF, -10RCFF | CFL-ZCFF (Z = 04, 05, 10, 20, 25) | CFL-20UFF | CFL-04VFF |
| λ central (nm) | 780 ± 3 | 780 ± 3 (puerto 1) / 1550 ± 4 (puerto 2) | ~1550 | 1030 | 515 ± 3 |
| Ancho de pulso (fs) | < 90 | < 90 | < 100 | < 100 | < 100 |
| Potencia media (W) | 0,25 / 1,0 / 1,5 | 0,25–1,0 (780) / 0,5–2,0 (1550) | > 0,25 a > 2,5 según Z | > 2 | > 0,4 |
| Tasa de repetición (MHz) | 50 u 80 (-04); 80 (-10, -15) | 50 u 80 (-04, -05); 80 (-10) | 10–80 (se fija al comprar) | 80 (20–100 a pedido) | 80 (27–100 a pedido) |
| Energía por pulso (nJ) | > 5 o 3 / > 12,5 / > 18,7 | 5–12,5 (780) / 10–25 (1550) | hasta 50 | > 25 | > 5 |
| Ancho espectral FWHM (nm) | 8–10 | 8–10 (780) / > 30 (1550) | > 30 | ~20 | ~5 |
| Estabilidad de potencia 8 h (% rms) | < 1,0 | < 1,0 | < 0,3 | < 1,0 | < 1,0 |
| M² | < 1,1 | < 1,1 | < 1,1 | < 1,2 | < 1,2 |
| Diámetro del haz a la salida (mm) | 1,25 | 1,3 / 1,6 | 1,2 | 1,25 | 1,25 |
| Razón de extinción de polarización (dB) | > 20 | > 20 / > 18 | > 20 | > 18 | > 18 |
| Salida | espacio libre, haz colimado | ídem | ídem | ídem | ídem (filtro UV) |
| Pre-chirp opcional | hasta −62 000 fs² | — | — | — | — |
| Temperatura de operación (°C) | 17–38 | 17–38 | 17–38 | 17–38 | 17–38 |
| Calentamiento (min) | ~10 | < 10 | < 10 | ~15 | ~15 |

Comunes a toda la serie: controlador de rack 48,2 × 46,7 × 10 cm (19", 2U), 13,6 kg; cabezal
9,0 × 18 × 3,5 cm, 0,8 kg; cable blindado fijo de 1 m entre ambos; sincronización RF ~0,5 V por
SMA; RS-232 y puerto de monitoreo (versión OEM); interruptor de llave y parada de emergencia;
refrigeración por aire; absorbedor saturable propietario "Mendocino" (mode-locking pasivo);
vida esperada > 10 000 h.

## Caracterización típica del X-780 (página 3)

- **Traza de autocorrelación típica**: pico simétrico, sin pedestal visible, FWHM ≈ 0,14 ps en el
  eje de retardo (leído de la gráfica); con 0,65 da ≈ 90 fs. Extraída a
  `trabajo-practico/exposicion-17-oct/figuras/fabricante_traza.png` con
  `scripts/trabajo-practico/ficha_laser.py`.
- **Espectro típico** (analizador de espectro óptico, 5 dB/div): λ_c = 781,344 nm,
  Δλ = 10,354 nm (ancho RMS con umbral de 20 dB, K = 2; no es FWHM). Extraído a
  `figuras/fabricante_espectro.png`.
- Producto tiempo-ancho de banda con los valores de la tabla: Δλ = 9 nm a 780 nm equivale a
  Δν = c·Δλ/λ² ≈ 4,4 THz; con τ_p = 90 fs, Δν·τ_p ≈ 0,40 (límite sech²: 0,315; gaussiano: 0,441).
  Con 8 nm: ≈ 0,36. El pulso nominal está cerca del límite de Fourier pero no en él.
- Las trazas típicas del X-1030 y del X-515 traen el valor impreso: "pw = 91 fs" y "PW = 84 fs".

## Generaciones del Carmel: el ancho especificado cambió con los años

Juan Esteban indica que su equipo "alcanza hasta 250 fs". Eso no cuadra con el "< 90 fs" del
Carmel X actual, pero sí con la **primera generación** del Carmel (antes de la serie X). Hojas de
datos antiguas bajadas de archive.org a `bibliografia/laser-carmel/antiguas/`:

| Documento | Fecha | Modelo | Ancho de pulso especificado | Otros |
|---|---|---|---|---|
| Página de producto calmarlaser.com | sep. 2012 | Carmel CFL-05RFF0 | **0,3 ps** ("less than 300 fs", "< 0.3 ps @ 50 MHz") | 780 nm, 500 mW, 50 MHz, M² < 1,15, jitter ~60 fs, "front panel control knobs for flexible system adjustment" |
| Hoja de datos CFL-05RFF0, Rev. C | 12/4/2012 | CFL-05RFF0 | **< 100 fs (90 typ.)** | 780 ± 5 nm, > 500 mW, 50 MHz (10–50 a pedido), ~10 nm, > 100 kW pico, haz 0,7 mm; cabezal 3 × 13 × 9 cm y 0,1 kg; controlador 48 × 50 × 18 cm y 12 kg; fibra de 80 cm; 17–32 °C |
| Carmel X-780, Rev. H / Rev. I | jun. 2016 / ene. 2017 | CFL-04/05/10RFF | "Minimum Pulse Width < 90"; traza típica "interpolated pulse width of 87 fs based upon sech² shape" | ya con cabezal 9 × 18 × 3,5 cm y controlador 2U |
| Carmel X-780, Rev. A → Rev. E | 2020 → 2025 | CFL-04/10/15RFF | < 90 | ver tabla principal |
| Carmel 1350 / Carmel-F 1350 | 2019–2020 | CFL-01OFF | < 200 fs | 1350 nm, > 100 mW |
| Carmel X-925 | oct. 2018 | CFL-05TFF | < 100 fs | 925 nm |
| Carmel X-1750 | abr. 2021 | CFL-10WFF | < 80 fs | 1750 nm |

En todas, sin excepción, la nota al pie es la misma: forma sech² y factor 0,65 sobre la traza de
autocorrelación de segundo armónico. Lo que cambió fue el valor límite, no la forma de medirlo.

Cómo distinguir la generación mirando el equipo:
- **Primera generación (2012)**: cabezal diminuto (3 × 13 × 9 cm, 0,1 kg) unido por una fibra de
  80 cm; controlador alto (18 cm, ~4U) con perillas en el panel frontal; 50 MHz.
- **Serie X (2016 en adelante)**: cabezal de 9 × 18 × 3,5 cm (0,8 kg) con cable blindado de 1 m;
  controlador de 2U (10 cm) con interruptor de llave y parada de emergencia; 50 u 80 MHz.

Si el equipo es de la primera generación, el patrón debe ser el que diga **su propio documento**
(hoja de datos entregada, manual u hoja de pruebas), no la hoja de datos actual de la web. Un
"hasta 250 fs" puede venir de: (a) la especificación "< 0,3 ps" de 2012; (b) una hoja de pruebas
del equipo; (c) el ancho de la **traza** de autocorrelación (τ_AC), que para un pulso sech² de
~160 fs mide ~250 fs; o (d) el ancho a la salida de la fibra de entrega, ensanchado por
dispersión. Hay que ver el documento para saber cuál.

Nota de 2022 (Physics Today, ene. 2022, pág. 54): Calmar añadió a la serie X el sistema
"OptaPower" de estabilización de potencia y de ancho de pulso frente a cambios de temperatura
ambiente (17–32 °C): el ancho de pulso de estos láseres sí varía con la temperatura, lo que es
un factor para el experimento.

## Modelo confirmado por Juan Esteban (23 oct 2026): CFL-05RFFUNC

- **CFL-05RFF** = Carmel de 780 nm y 0,5 W (50 u 80 MHz, fijada al comprar). Sufijo **UNC**: no aparece
  en ningún documento de Calmar ni de distribuidores (GoPhotonics lista "CFL-05RFF" a secas); se asume
  código de pedido o de cliente. Pendiente pedir a sales@calmarlaser.com la hoja de pruebas del número
  de serie.
- Ancho especificado para el -05 según la revisión: CFL-05RFF0 (Rev. C, dic. 2012) **< 100 fs (90 típ.)**;
  página web sep. 2012 "< 300 fs"; Carmel X-780 Rev. H (jun. 2016) y Rev. I (ene. 2017) **< 90 fs** con
  traza típica "interpolated pulse width of 87 fs"; Rev. A 2020, catálogo 2023 y Rev. E 2025 < 90 fs.
  Siempre sech² y factor 0,65.
- **El fabricante no publica el ancho de pulso en función de la corriente** (ni de la potencia) en
  ninguna de las 11 hojas de datos, el white paper, el catálogo 2023 ni la nota de Physics Today 2022.
  Da un solo máximo en el punto nominal. Las curvas ancho–corriente que sí publica son de las series
  FPL y PSL (banda C, con perillas). La serie X no expone el control de corriente al usuario (panel:
  interruptor, llave, parada de emergencia; ajuste por RS-232). Consecuencia: un solo patrón (90 fs) a
  la corriente nominal; a otras corrientes solo cabe comparar el láser consigo mismo.
- **Datos confirmados del equipo (23 oct 2026)**: 780 nm, 50 MHz, salida en espacio libre, número de
  serie 881139, corriente ajustable de 0 a 7,12 A. Faltan: generación (forma del cabezal y del
  controlador), fecha de fabricación, opción de pre-chirp y la hoja de pruebas con el ancho por corriente.
- Protocolo del experimento en `trabajo-practico/protocolo/` (se regenera con
  `scripts/trabajo-practico/build_protocolo.sh`).

## Hoja de pruebas de fábrica del equipo (fotos del 24 oct 2026)

Fotos en `notas/WhatsApp Image 2026-10-24 at 4.45.12 PM.jpeg` y `… 5.25.36 PM.jpeg` (sección 4,
«Output Characterization», pág. 11 del documento del equipo).

**Tabla 4. Test result summary** (resultado con seed normalized current 4,04 y AMP pump current 7,0 A):

| Parámetro | Especificación | Resultado |
|---|---|---|
| Longitud de onda central (nm) | 780 | 779,2 |
| Ancho de pulso (fs) | < 80 | 70 |
| Tasa de repetición (MHz) | 50 | 50 |
| Potencia media (mW) | ≥ 500 | 587 |
| Energía por pulso (nJ) | > 10 | 11,7 |
| Ancho espectral (nm) | ~ 10 | 8,5 |
| Extinción de polarización (dB) | > 25 | 25,2 |
| Calidad del haz | M² ≤ 1,2 | M²x = M²y = 1,08 |
| Diámetro del haz a la salida (mm) | 0,7 (típico) | 0,66 (a 10 cm) |
| Circularidad (%) | ≥ 90 | 98 |
| Estabilidad de potencia en 8 h (%) | < 1 | 0,45 (RMS) |
| Salida | Espacio libre, haz colimado | Cumple |

**Tabla 5. Laser Output Characterization** (seed normalized current 4,04):

| AMP pump current (A) | Potencia (mW) | Ancho de pulso (fs) | Energía (nJ) |
|---|---|---|---|
| 3 | 44 | 248 | 0,9 |
| 4 | 114 | 170 | 2,3 |
| 5 | 218 | 107 | 4,4 |
| 6 | 378 | 76 | 7,6 |
| 7 | 579 | 54 | 11,6 |
| 7,23 | 607 | 51 | 12,1 |

Texto: potencia media 601 mW, estabilidad RMS 0,40 % y energía media 12,1 nJ a 7,23 A, después de
10 min de encendido. Las anotaciones a mano de la hoja (columnas de energía y «P₀») no son del
fabricante y no se usan.

Consecuencias para el diseño:
- **No hay tolerancia, banda de aceptación, estabilidad del ancho ni incertidumbre** del ancho de pulso:
  el patrón es un valor puntual sin varianza conocida → prueba t de una muestra (caso 2) por corriente,
  con δ por la regla 5 (10 fs) salvo en 7 A, donde τmáx − τ0 = 80 − 54 = 26 fs.
- **Niveles elegidos (24 oct 2026): 5, 6 y 7 A** (τ0 = 107, 76 y 54 fs). Son las corrientes altas, donde
  la señal de segundo armónico es mayor; 7,23 A supera el máximo de 7,12 A del controlador.
- **Discrepancia**: a 7,0 A la tabla 4 dice 70 fs y la tabla 5 dice 54 fs. Se usa la tabla 5 (mismo
  método para las tres corrientes); hay que mencionarlo en el informe.
- La especificación del equipo (< 80 fs) es más estricta que la de las hojas públicas (< 90 fs).

## Qué falta averiguar en el laboratorio

1. Modelo exacto en la etiqueta del controlador o del cabezal (CFL-04RFF, -10RFF, -15RFF; o si
   es doble, CFL-xxRCFF; o X-1550, CFL-ZCFF) y tasa de repetición.
2. Si existe una hoja de pruebas de fábrica ("test data sheet") del equipo, con su fecha: sería el
   patrón más fuerte (ancho medido de **este** láser, no el máximo del modelo).
3. Fecha de compra y horas de uso aproximadas (la vida esperada es > 10 000 h).
4. Si tiene la opción de pre-chirp negativo: cambia el ancho a la salida y hay que medir en la
   condición en que el fabricante especifica.
