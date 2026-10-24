# Estructura de la exposición: conocimiento no estadístico del autocorrelador de intensidad

Trabajo práctico · Diseño de Experimentos Avanzados (3008475) · UNAL 2026-II
Exposición del sábado 17 de octubre de 2026 (hito "Definir problema", jornada de asesorías).

## Idea que la exposición debe dejar instalada

> Antes de usar el autocorrelador para estudiar cualquier factor, hay que saber si mide bien.
> Por eso el trabajo práctico es un **diseño de comparación simple**: el ancho de pulso medido
> con la técnica de intensidad frente al **patrón**, que es el valor que reporta el fabricante
> del láser. Del resultado sale la calibración de la técnica y un diagnóstico del estado del láser.

Cómo se construye el argumento a lo largo de la exposición:

1. Bloques 1 a 4: toda la física, desde el pulso hasta la traza del autocorrelador.
2. Bloque 5: **todos** los factores que pueden cambiar el ancho medido. Se presentan completos,
   pero con un giro: son tantos y tan difíciles de separar que estudiarlos ahora no tiene sentido
   si no se sabe primero si el instrumento mide bien.
3. Bloque 6: la propuesta. Los factores no desaparecen: se convierten en **condiciones que se
   fijan** para que la comparación con el fabricante sea justa. Estudiarlos queda como trabajo
   futuro, sobre un instrumento ya calibrado.

## Criterios con que se armó

- **Estilo de la profesora** (ver `notas/clases/`): títulos en forma de pregunta, de lo general a
  lo particular, una idea por diapositiva, un esquema que ordene el tema antes de detallarlo.
  La hipótesis se escribe como H0/HA, que es como ella las redacta.
- **No es una exposición estadística.** La parte estadística se reduce a una diapositiva (23) que
  nombra el diseño y la hipótesis, porque es lo que la profesora debe aprobar en la asesoría.
- **Referencias:** los códigos entre corchetes ([A1], [E1]…) remiten a
  `bibliografia/autocorrelador-intensidad-referencias.txt`. "Montgomery cap. 2" remite a
  `notas/montgomery/cap-02-experimentos-comparativos-simples.md`.
- **Duración supuesta:** unos 20 minutos, 25 diapositivas. Si hay menos tiempo, se recortan las
  diapositivas 11 y 18–19 (se pueden fundir en una), nunca el bloque 6.
- **Lo que falta del montaje:** las diapositivas marcadas con ⚠ dependen de datos que aún no
  están en el repositorio (ver la lista al final).

## Mapa general

| Bloque | Pregunta que responde | Diapositivas | Tiempo | Expone |
|---|---|---|---|---|
| 0 | ¿Qué proponemos? | 1–2 | 1 min | — |
| 1 | ¿Qué queremos medir? | 3–5 | 3 min | Juan Esteban |
| 2 | ¿De dónde sale el pulso y qué dice el fabricante? | 6–8 | 3 min | Juan Esteban |
| 3 | ¿Cómo funciona el autocorrelador? | 9–13 | 5 min | Sebastián |
| 4 | ¿Cómo se pasa de la traza al ancho del pulso? | 14–16 | 2 min | Sebastián |
| 5 | ¿Qué puede cambiar el ancho medido? | 17–20 | 3 min | Juan Esteban |
| 6 | ¿Por qué empezar por calibrar? | 21–25 | 3 min | Sebastián |

La repartición de quién expone es una propuesta para que cada uno tenga bloques continuos.

---

## Bloque 0 · ¿Qué proponemos?

**1. Portada.** Título provisional: "Calibración de un autocorrelador de intensidad frente a la
especificación del fabricante: fundamentos físicos". Nombres, materia, fecha.

**2. ¿Qué vamos a proponer y cómo llegamos ahí?**
- Una frase con la propuesta: comparar el ancho de pulso medido con el autocorrelador contra el
  valor del fabricante, para calibrar la técnica y diagnosticar el láser.
- Agenda con los seis bloques. Anunciar desde el principio adónde se va hace que todo lo demás
  se escuche como argumento.

## Bloque 1 · ¿Qué queremos medir?

**3. ¿Por qué no basta con un detector para medir un pulso de femtosegundos?**
- Escalas: 1 fs = 10⁻¹⁵ s. Un fotodiodo rápido responde en decenas de picosegundos; un
  osciloscopio, en el mejor caso, en picosegundos. El pulso es entre 100 y 1000 veces más corto.
- Ningún detector electrónico ve la forma del pulso, solo su energía integrada.
- Idea central: **el pulso tiene que medirse a sí mismo**. Y un instrumento así no se puede
  verificar con un cronómetro: necesita una referencia (esto vuelve en el bloque 6).
- Figura: escala logarítmica de tiempos (respuesta del detector frente a la duración del pulso).

**4. ¿Qué es exactamente un pulso ultracorto?** [A1, B1]
- Campo eléctrico: E(t) = Re{A(t)·e^{iω₀t}}, con envolvente A(t) y portadora ω₀.
- Intensidad: I(t) ∝ |A(t)|². El ancho de pulso τₚ es el ancho a media altura (FWHM) de I(t).
- Formas de referencia: gaussiana y secante hiperbólica al cuadrado (sech²).
- Figura: portadora, envolvente e intensidad con el FWHM marcado.

**5. ¿Por qué un pulso corto necesita un espectro ancho?** [A1, recurso web J]
- Tiempo y frecuencia son pares de Fourier: Δν·τₚ ≥ K, con K = 0,441 (gaussiano) o 0,315 (sech²)
  (Diels y Rudolph, tabla 1.1 y ec. 1.30, pág. 10).
- Pulso **limitado por transformada**: cumple la igualdad; "holds for pulses without frequency
  modulation (unchirped) which are called 'bandwidth limited'" (Diels y Rudolph, pág. 10). Un pulso
  con chirp tiene un espectro más ancho que el límite de Fourier (pág. 18).
- Ejemplo numérico: 100 fs gaussiano a 800 nm requiere Δν = 4,41 THz, es decir Δλ ≈ 9,4 nm.
- Por esto el espectro es un segundo dato para comparar con el fabricante y para validar el ancho.

## Bloque 2 · ¿De dónde sale el pulso y qué dice el fabricante?

**6. ¿Cómo genera pulsos un láser de modo amarrado (mode-locking)?** [H3, H4, H6, A5]
- Muchos modos longitudinales separados Δν = c/(2nL) oscilan con fase fija (Diels y Rudolph,
  ec. 5.1, pág. 278); su suma es un tren de pulsos con periodo igual al tiempo de ida y vuelta
  en la cavidad, T = 2nL/c.
- Cuantos más modos en fase (mayor ancho de banda de ganancia), más corto el pulso.
- La teoría de Haus predice pulsos con forma sech² [H3] (pendiente de confirmar en el artículo;
  Diels y Rudolph asocian la sech² a los solitones, págs. 296 y 386). La práctica es suponer
  "a sech² or a Gaussian shape" (Diels y Rudolph, pág. 459).
- Figura: suma de N modos en fase frente a fases aleatorias.

**7. ¿Qué especifica el fabricante y cómo lo midió?** [K1] (variante asumida: X-780 ⚠)
- Láser: Calmar Laser, Carmel X (fibra, mode-locking pasivo por absorbedor saturable "Mendocino").
  Hoja de datos X-780, Rev. E (2025): λ = 780 ± 3 nm, ancho espectral 8–10 nm FWHM, 50 u 80 MHz,
  0,25 / 1,0 / 1,5 W según modelo (CFL-04/-10/-15RFF), M² < 1,1, haz de 1,25 mm.
- **Ancho de pulso: < 90 fs, un máximo garantizado**, no un valor nominal. Nota 2 de la tabla:
  "A sech² pulse shape (deconvolution factor of 0.65) is used to determine the pulse width from
  the second harmonic autocorrelation trace". Es la misma técnica nuestra: hay que deconvolucionar
  con sech² (0,65) y la prueba es de una cola (HA: μ_τ > 90 fs).
- Pág. 3: traza de autocorrelación típica (FWHM ≈ 0,14 ps → ≈ 90 fs) y espectro típico
  (λc = 781,3 nm, Δλ = 10,4 nm RMS). Con 9 nm y 90 fs, Δν·τₚ ≈ 0,40 (límite sech²: 0,315).
- Son datos del modelo, no de este equipo. Si vino con hoja de pruebas de fábrica, es el patrón
  más fuerte. ⚠ Falta: modelo exacto en la etiqueta del controlador, tasa de repetición, fecha de
  compra y horas de uso. Resumen completo en `notas/laser-carmel-x-ficha-tecnica.md`.

**8. ¿Qué le pasa al pulso entre la salida del láser y el autocorrelador?** [A1, A3, E4]
- Fase espectral en serie de Taylor: φ(ω) = φ₀ + φ₁(ω−ω₀) + ½φ₂(ω−ω₀)² + ⅙φ₃(ω−ω₀)³ + …
  φ₂ (GDD) ensancha el pulso y le da **chirp**, aunque el espectro no cambie.
- Pulso gaussiano limitado por transformada: τ_sal = τ_ent·√(1 + (4·ln2·GDD/τ_ent²)²). Es la
  ec. 1.125 de Diels y Rudolph (pág. 34), reescrita con el FWHM (τₚ = √(2 ln2)·τ_G, pág. 33).
- Ejemplo con 1 cm de BK7 a 800 nm: k″ ≈ 45 fs²/mm, calculado con n″ = 0,05 µm⁻² de la tabla 2.1
  de Diels y Rudolph (pág. 62); GDD ≈ 450 fs². Resultado: 100 fs → 100,8 fs; 30 fs → 51 fs.
- Mensaje para la comparación: todo el vidrio entre la salida del láser y el cristal (incluido el
  divisor de haz y la lente del autocorrelador) hay que contarlo, o se medirá un pulso más largo
  que el que entrega el láser.
- Figura: τ_sal contra GDD para varios τ_ent.

## Bloque 3 · ¿Cómo funciona el autocorrelador?

**9. ¿Cómo se mide algo más rápido que cualquier detector?** [A1, C2]
- Se divide el pulso en dos copias y una se retrasa un tiempo τ. Un proceso no lineal solo da
  señal cuando las dos copias se superponen; el detector lento integra esa señal.
- Barriendo τ se recorre el pulso "con el pulso mismo".
- El retardo sale de la diferencia de camino: τ = 2Δx/c (geometría del retrorreflector; Diels y
  Rudolph no lo escriben explícito). Mover el espejo 1 µm retrasa 6,67 fs.

**10. ¿Cómo está armado el autocorrelador?** [G1, G2, F10] ⚠
- Esquema tipo Michelson: divisor de haz → brazo fijo y brazo con retrorreflector sobre una
  plataforma motorizada o un piezoeléctrico → lente que enfoca ambos haces en el cristal no lineal
  → filtro que bloquea la fundamental → detector.
- Geometrías: **colineal** (haces superpuestos; aparecen franjas y fondo) y **no colineal** (haces
  cruzados en ángulo; señal sin fondo).
- Figura: esquema del montaje real, con cada componente rotulado.

**11. ¿Por qué hace falta un proceso no lineal?** [A1, B1]
- Con un detector lineal la señal es ∫|E(t) + E(t−τ)|² dt: solo contiene la autocorrelación del
  **campo**, cuya transformada de Fourier es el espectro (teorema de Wiener–Khinchin). Diels y
  Rudolph (pág. 460): "a first-order field autocorrelation does not carry any other information
  than that provided by a spectrometer".
- Se necesita una señal proporcional a I(t)·I(t−τ): un proceso de segundo orden.

**12. ¿Qué es la generación de segundo armónico (SHG)?** [H1, H2, A6, A7]
- Polarización no lineal: P = ε₀(χ⁽¹⁾E + χ⁽²⁾E² + …). El término χ⁽²⁾E² oscila a 2ω₀.
- Intensidad generada: I₂ω ∝ d_eff²·L²·I_ω²·sinc²(ΔkL/2), con Δk = k(2ω) − 2k(ω).
- **Ajuste de fase:** Δk = 0 con cristales birrefringentes (BBO, KDP) al ángulo adecuado.
- Compromiso del espesor L: "a compromise to be reached between bandwidth and sensitivity"
  (Diels y Rudolph, pág. 468). Si el cristal es demasiado largo, "the measured correlation width
  will be longer than the exact correlation length" (pág. 468): **sesgo hacia anchos mayores**.
- Desajuste de velocidad de grupo a 800 nm: BBO 187 fs/mm, KDP 77 fs/mm (Diels y Rudolph,
  tabla 3.2, pág. 176). Condición: L ≪ τₚ/|1/v₂ − 1/v₁| (ec. 3.108, pág. 175).
- Prueba práctica: el espectro del segundo armónico no debe ser más angosto que el cuadrado del
  espectro fundamental (pág. 468).
- Alternativa sin cristal: absorción de dos fotones en un LED o fotodiodo [F1, F2, G3].

**13. ¿Qué señal registra el detector?** [A1, C4, C5]
- No colineal (sin fondo): A(τ) = ∫I(t)·I(t−τ) dt. Siempre es simétrica en τ.
- Colineal promediado: relación pico/fondo 3:1. Colineal con franjas (interferométrica): 8:1
  (Diels y Rudolph, pág. 462 y fig. 9.1, pág. 463).
- Esas relaciones sirven como control de alineación antes de cada medición.
- Figura: las tres trazas simuladas para un pulso sech².

## Bloque 4 · ¿Cómo se pasa de la traza al ancho del pulso?

**14. ¿Cómo se obtiene τₚ a partir de la traza?** [C6, A1, B1]
- τ_AC = k·τₚ, donde k depende de la forma supuesta. Valores de Sala et al. (1980), tabla II,
  pág. 993 (el artículo da τₚ/τ_G; k es su inverso). Diels y Rudolph (tabla 9.1, pág. 477)
  confirman 1,414 y 1,543:

  | Forma del pulso | τₚ/τ_AC | k = τ_AC/τₚ | Δν·τₚ |
  |---|---|---|---|
  | Cuadrada | 1 | 1 | 0,8859 |
  | Gaussiana | 0,7071 | 1,414 | 0,4413 |
  | sech² | 0,6482 | 1,543 | 0,3148 |
  | Lorentziana | 0,5000 | 2,000 | 0,2206 |
  | Exponencial de un lado | 0,5000 | 2,000 | 0,1103 |

  (La tabla original tiene 10 formas; estas bastan para la diapositiva. La "lorentziana" de
  Diels y Rudolph es otro perfil, [1 + (t/τ)²]⁻², con Δν·τₚ = 0,142: no mezclar las dos fuentes.)
- Diels y Rudolph ponen entre comillas el verbo: se asume una forma y se "determine" la duración
  con el factor conocido (pág. 459).
- Monmayrant et al. (2010, pág. 19): para estimar la duración "one has to make an assumption on
  the pulse profile", y citan a Sala.
- La misma traza da anchos que difieren un 9 % entre gaussiana y sech² (0,7071 frente a 0,6482)
  y un 41 % entre gaussiana y lorentziana: para comparar con el fabricante hay que usar **la
  misma forma que usó él**.
- Ojo: estos factores son de la autocorrelación de **intensidad**. En la interferométrica el
  factor es otro (Donnelly y Grossman usan 1,7 para gaussiana, pág. 683).

**15. ¿Cómo se calibra el eje de retardo?** [A1, G1]
- Posición del motor → τ = 2Δx/c (factor 2 por la ida y vuelta en el retrorreflector).
- Otra opción: insertar una lámina de vidrio de espesor conocido en un brazo y medir el
  corrimiento de la traza (Diels y Rudolph, fig. 9.6, pág. 470, con una lámina de 0,36 mm).
- Comprobaciones: desplazar el brazo una distancia conocida y medir cuánto se corre el pico
  (Sala et al. montaron el prisma en una platina de precisión de 50 mm "to enable calibration",
  pág. 992), o contar franjas de la traza interferométrica, una franja = λ/c (Donnelly y
  Grossman: 2,72 fs por franja con su espectro, pág. 683).
- Sala et al. reportan que la escala ps/V de su barrido es constante "to within ±10 percent over
  the central 2/3 of the display" (pág. 995): la linealidad del barrido también se verifica.
- Un error de escala en el retardo se traslada completo al ancho medido: es la primera
  calibración interna, previa a la comparación con el fabricante.

**16. ¿Qué no puede decirnos la autocorrelación de intensidad?** [D1, D2, D3, A2, I1–I6]
- No da la fase ni el chirp; es simétrica: "a chirped pulse can give exactly the same
  autocorrelation signal as a longer Fourier-limited pulse" (Monmayrant et al., pág. 19).
- Ambigüedad: Chung y Weiner construyen pulsos distintos con la misma autocorrelación y el mismo
  espectro; sus anchos FWHM difieren "on the order of 25%" (pág. 665). El ancho rms, en cambio,
  sí queda determinado por la autocorrelación (pág. 663).
- **Artefacto coherente** con trenes inestables: un pico angosto sobre un fondo ancho; el pico no
  es el pulso: "The correct pulse length is actually almost always indicated by the temporally
  much broader background" (Ratner et al., pág. 2874). Por eso se barre un rango de retardo
  amplio y se reporta siempre la traza medida (pág. 2876).
- Validez: el método "work[s] well for simple pulses close to Fourier limited" (Monmayrant
  et al., pág. 19). Para este proyecto basta con el ancho; FROG o SPIDER solo se mencionan.

## Bloque 5 · ¿Qué puede cambiar el ancho medido?

**17. ¿Cuáles son las fuentes de variación del ancho medido?**
- Diagrama de causa y efecto (Ishikawa) con efecto "ancho de pulso medido τₚ" y cinco ramas:
  fuente, propagación, proceso no lineal, geometría y retardo, detección e interpretación.
- El ancho medido cambia porque **el pulso cambia** o porque **la medición lo deforma**.

**18. ¿Qué factores cambian el pulso que llega?** [H3–H7, E4, E5, A1]
- Fuente: potencia de bombeo, alineación de la cavidad, compensación de dispersión interna,
  temperatura, tiempo de calentamiento.
- Propagación: material y espesor de vidrio atravesado (GDD), compresor externo.
- Potencia alta en elementos ópticos: automodulación de fase (SPM).

**19. ¿Qué factores deforman la medición?** [E1, E2, E3, F6–F10, B3, D3]
- Cristal: espesor y desajuste de velocidad de grupo (alarga la traza, Diels y Rudolph pág. 468),
  ángulo de ajuste de fase.
- Geometría: ángulo de cruce y tamaño del haz, superposición de los brazos, enfoque.
- Retardo: calibración del motor, velocidad de barrido frente al tiempo de integración.
- Detección: saturación o no linealidad del detector, ruido, número de pulsos promediados. Si
  los pulsos del tren no son idénticos, el promedio deforma la traza: "it is important to verify
  that the pulse train is constituted of identical pulses, in amplitude (energy), duration and
  frequency" (Diels y Rudolph, págs. 465–466).
- Interpretación: forma supuesta, método de ajuste, nivel del fondo.

**20. ¿Qué hacemos con todos estos factores?**
- Son muchos, varios interactúan y algunos no se pueden medir por separado (por ejemplo, el
  chirp de la fuente y el GDD del montaje producen el mismo efecto en la traza).
- Si se varían ahora, cualquier efecto observado se confunde con un error del instrumento que
  todavía no se conoce.
- Decisión: en este trabajo **se fijan**. Tabla con columnas: factor · cómo se fija · por qué.
  Ejemplos: misma forma supuesta que el fabricante (sech²); medir lo más cerca posible de la
  salida del láser y descontar el GDD conocido del montaje; mismo tiempo de calentamiento antes
  de cada medición; potencia de entrada fija y por debajo de la saturación del detector; retardo
  calibrado; relación pico/fondo verificada antes de cada serie.
- Los que no se pueden fijar (fluctuaciones del láser, ruido) quedan como error experimental y
  son justamente lo que estiman las repeticiones de la comparación.

## Bloque 6 · ¿Por qué empezar por calibrar?

**21. ¿Por qué no estudiar directamente los factores?**
- Un estudio de factores mide **cambios** del ancho; si el instrumento tiene un sesgo que no se
  conoce, esos cambios no se pueden interpretar.
- Diels y Rudolph (pág. 457): "Any measurement technique introduces some perturbation on the
  parameter to be measured… A careful analysis of the diagnostic instrument is required to find
  its exact transfer function." Conocer esa función de transferencia es calibrar.
- El autocorrelador no se puede verificar con otro reloj (diapositiva 3): la única referencia
  disponible es el valor del fabricante, medido con una técnica equivalente.
- La comparación responde una pregunta práctica: ¿el láser sigue entregando lo que promete?
- Es el uso que la literatura le da a la técnica: la autocorrelación es "easy to set up, fast and
  simple to use for daily check, and also provide[s] an independent measurement" (Monmayrant
  et al., pág. 28). Sala et al. la presentan como "permanent, on-line pulsewidth monitor"
  (pág. 994), y muestran que desajustar la cavidad 5 µm cambia el pulso (pág. 995).
- Es factible con los recursos y el tiempo del semestre; el estudio de factores se apoya en ella.

**22. ¿Qué se compara exactamente?** ⚠
- **Patrón:** ancho de pulso máximo del fabricante, < 90 fs con sech² y factor 0,65 [K1]; ancho
  espectral 8–10 nm y tasa de repetición 50 u 80 MHz según el modelo.
- **Técnica:** ancho de pulso τₚ medido con el autocorrelador de intensidad, con la misma forma
  supuesta y en las condiciones fijadas en la diapositiva 20.
- **Variable respuesta:** τₚ en fs. Respuesta secundaria: Δλ medido con espectrómetro, si hay
  uno, para calcular Δν·τₚ.
- **Repeticiones:** n mediciones independientes (realinear o rebarrer entre una y otra), en
  orden y días que capturen la variación real del láser y del montaje.

**23. ¿Cuál es la hipótesis del experimento?** [Montgomery cap. 2, sec. 2-4.6]
- Diseño de comparación simple: una media frente a un valor especificado.
  - H0: μ_τ = 90 fs (el ancho medido está en el límite garantizado: láser e instrumento en
    especificación)
  - HA: μ_τ > 90 fs (el pulso es más largo que lo que garantiza el fabricante)
- Montgomery menciona las especificaciones como origen válido del valor de referencia.
- Es de una cola porque la hoja de datos da un máximo ("< 90 fs"), no un valor nominal [K1]: un
  pulso más corto no contradice al fabricante. Se rechaza H0 si t0 > t_{α, n−1}.
- Si el laboratorio tiene otro instrumento de referencia (un autocorrelador comercial), la
  comparación pasa a ser de dos tratamientos o pareada (Montgomery secs. 2-4 y 2-5). Pregunta
  para la asesoría.

**24. ¿Qué podremos concluir sobre el láser?** [A1, D1, D2]
- Árbol de decisión para la diapositiva:
  - τₚ ≈ fabricante y Δν·τₚ cerca del límite → láser e instrumento en especificación; la técnica
    queda calibrada (se reporta el sesgo y su incertidumbre).
  - τₚ mayor y espectro igual al nominal → el pulso tiene chirp: dispersión no compensada en el
    láser o en el camino.
  - τₚ mayor y espectro más angosto → menos modos en fase: el láser perdió desempeño (bombeo,
    alineación, degradación del medio).
  - τₚ menor que el nominal → sospechar del instrumento: calibración del retardo, forma
    supuesta o artefacto coherente.
- El espectro es lo que permite separar "el láser cambió" de "el instrumento mide mal". Donnelly
  y Grossman hacen exactamente eso: comparan el ancho medido con el límite calculado desde el
  espectro; "If the two match, the pulse is transform limited, if not, there is a nonlinear
  phase" (págs. 682–683).
- Limitación que hay que declarar: aun con espectro, la forma del pulso no queda fija (≈25 %,
  Chung y Weiner); la conclusión es sobre el ancho bajo la forma supuesta.

**25. ¿Qué sigue? y referencias.**
- Trabajo futuro: con el instrumento calibrado, un diseño factorial sobre los factores del
  bloque 5 (por ejemplo, espesor de vidrio y potencia).
- Referencias en Normas ICONTEC, solo las citadas. Base mínima: [A1], [A6], [B1], [C2], [C6],
  [D1], [E1], [H3], [G1] y Montgomery.

---

## Figuras que hay que preparar

| Diap. | Figura | Cómo se obtiene |
|---|---|---|
| 3 | Escala de tiempos detector frente a pulso | Dibujo propio |
| 4 | Portadora, envolvente e intensidad | Script (Python) |
| 6 | Suma de modos en fase frente a fases aleatorias | Script |
| 8 | τ_sal contra GDD | Script, con la fórmula de la diapositiva |
| 10 | Esquema del montaje real | Dibujo propio a partir de fotos del montaje |
| 13 | Tres tipos de traza para un pulso sech² | Script |
| 17 | Diagrama de Ishikawa | Dibujo propio |
| 24 | Árbol de decisión del diagnóstico | Dibujo propio |

## Datos que faltan (⚠)

1. **Láser** (diapositiva 7): la hoja de datos del Carmel X-780 ya está [K1]. Falta confirmar en
   la etiqueta del controlador el modelo exacto (CFL-04/-10/-15RFF, o la variante de 1550 nm), la
   tasa de repetición, si vino con hoja de pruebas de fábrica (con fecha) y las horas de uso.
2. Detector y proceso no lineal: cristal (tipo, espesor) o fotodiodo por absorción de dos fotones.
3. Geometría: colineal o no colineal; ángulo de cruce si es no colineal.
4. Barrido del retardo: motor o piezoeléctrico, paso mínimo, recorrido total.
5. Elementos ópticos entre la salida del láser y el cristal (para estimar el GDD acumulado).
6. Si hay espectrómetro (diapositivas 5, 22 y 24) y si hay otro autocorrelador de referencia.
