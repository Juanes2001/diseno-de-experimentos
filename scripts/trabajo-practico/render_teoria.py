#!/usr/bin/env python3
"""Genera la teoría completa del diseño de comparación simple (HTML para imprimir en PDF).

Uso: render_teoria.py salida.html

Ensambla tres partes:
  I.   notas/montgomery/cap-02-experimentos-comparativos-simples.md
  II.  notas/gutierrez-de-la-vara/cap-02-inferencia-uno-y-dos-tratamientos.md
  III. Guía de decisión y aplicación (escrita aquí, en PARTE_III)
Las fórmulas en LaTeX ($...$ y $$...$$) se renderizan con KaTeX (CDN) al imprimir con Chrome.
"""
import html
import re
import sys
from pathlib import Path

import markdown

RAIZ = Path(__file__).resolve().parents[2]
FICHAS = [
    ("I", "Montgomery, capítulo 2: Experimentos comparativos simples",
     RAIZ / "notas/montgomery/cap-02-experimentos-comparativos-simples.md"),
    ("II", "Gutiérrez–De la Vara, capítulo 2: Elementos de inferencia estadística, experimentos con uno y dos tratamientos",
     RAIZ / "notas/gutierrez-de-la-vara/cap-02-inferencia-uno-y-dos-tratamientos.md"),
]

PARTE_III = r"""
## Esquema de los nueve casos: qué distribución y qué protocolo usar

La pregunta que define el diseño de comparación simple es **qué se compara con qué** y **qué se
sabe de la varianza**. Tres preguntas en orden fijan el caso: (1) ¿el parámetro es una media,
una varianza o una proporción?; (2) ¿se compara una población con un patrón o dos poblaciones
entre sí?; (3) para medias, ¿las observaciones son pareadas?, ¿la varianza es conocida? y, si
no lo es, ¿se pueden suponer iguales las dos varianzas? El árbol lleva a uno de los nueve
casos; la tabla que sigue da el protocolo de cada uno.

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 600" width="100%" style="font-family:Calibri,Segoe UI,Arial,sans-serif;max-width:760px;display:block;margin:0 auto 3mm"><rect x="280" y="10" width="200" height="34" rx="4" fill="#e8f1f3" stroke="#0f4c5c" stroke-width="0.8"/><text x="380.0" y="30.5" text-anchor="middle" font-size="9.5" font-weight="400" fill="#142b33">¿Qué parámetro se compara?</text><rect x="60" y="80" width="150" height="30" rx="4" fill="#e8f1f3" stroke="#0f4c5c" stroke-width="0.8"/><text x="135.0" y="98.5" text-anchor="middle" font-size="9.5" font-weight="400" fill="#142b33">Una MEDIA (o dos)</text><rect x="470" y="80" width="130" height="30" rx="4" fill="#e8f1f3" stroke="#0f4c5c" stroke-width="0.8"/><text x="535.0" y="98.5" text-anchor="middle" font-size="9.5" font-weight="400" fill="#142b33">Una VARIANZA (o dos)</text><rect x="630" y="80" width="120" height="30" rx="4" fill="#e8f1f3" stroke="#0f4c5c" stroke-width="0.8"/><text x="690.0" y="98.5" text-anchor="middle" font-size="9.5" font-weight="400" fill="#142b33">Una PROPORCIÓN (o dos)</text><path d="M380,44 L380,62.0 L135,62.0 L135,80" fill="none" stroke="#5b6b73" stroke-width="0.9"/><path d="M380,44 L380,62.0 L535,62.0 L535,80" fill="none" stroke="#5b6b73" stroke-width="0.9"/><path d="M380,44 L380,62.0 L690,62.0 L690,80" fill="none" stroke="#5b6b73" stroke-width="0.9"/><rect x="60" y="140" width="150" height="40" rx="4" fill="#e8f1f3" stroke="#0f4c5c" stroke-width="0.8"/><text x="135.0" y="157.5" text-anchor="middle" font-size="9.5" font-weight="400" fill="#142b33">¿Una población frente a</text><text x="135.0" y="169.5" text-anchor="middle" font-size="9.5" font-weight="400" fill="#142b33">un patrón μ₀, o dos?</text><path d="M135,110 L135,125.0 L135,125.0 L135,140" fill="none" stroke="#5b6b73" stroke-width="0.9"/><rect x="10" y="215" width="120" height="34" rx="4" fill="#e8f1f3" stroke="#0f4c5c" stroke-width="0.8"/><text x="70.0" y="235.5" text-anchor="middle" font-size="9.5" font-weight="400" fill="#142b33">¿σ conocida?</text><path d="M135,180 L135,197.5 L70,197.5 L70,215" fill="none" stroke="#5b6b73" stroke-width="0.9"/><text x="73" y="211" font-size="8.5" fill="#e36414" font-weight="700">una</text><rect x="10" y="285" width="120" height="56" rx="4" fill="#0f4c5c" stroke="#0f4c5c" stroke-width="0.8"/><text x="70.0" y="304.5" text-anchor="middle" font-size="9.5" font-weight="700" fill="#fff">Caso 1 · Z₀</text><text x="70.0" y="316.5" text-anchor="middle" font-size="9.5" font-weight="700" fill="#fff">N(0,1)</text><text x="70.0" y="328.5" text-anchor="middle" font-size="9.5" font-weight="700" fill="#fff">ec. 2-35</text><rect x="10" y="365" width="120" height="56" rx="4" fill="#0f4c5c" stroke="#0f4c5c" stroke-width="0.8"/><text x="70.0" y="384.5" text-anchor="middle" font-size="9.5" font-weight="700" fill="#fff">Caso 2 · t₀</text><text x="70.0" y="396.5" text-anchor="middle" font-size="9.5" font-weight="700" fill="#fff">t con n−1 g.l.</text><text x="70.0" y="408.5" text-anchor="middle" font-size="9.5" font-weight="700" fill="#fff">ec. 2-37 / (2.8)</text><path d="M50,249 L50,285" stroke="#5b6b73" stroke-width="0.9"/><text x="54" y="270" font-size="8.5" fill="#e36414" font-weight="700">sí</text><path d="M100,249 L100,275 L140,275 L140,350 L70,350 L70,365" fill="none" stroke="#5b6b73" stroke-width="0.9"/><text x="104" y="270" font-size="8.5" fill="#e36414" font-weight="700">no</text><rect x="170" y="215" width="150" height="34" rx="4" fill="#e8f1f3" stroke="#0f4c5c" stroke-width="0.8"/><text x="245.0" y="235.5" text-anchor="middle" font-size="9.5" font-weight="400" fill="#142b33">¿Observaciones pareadas?</text><path d="M135,180 L135,197.5 L245,197.5 L245,215" fill="none" stroke="#5b6b73" stroke-width="0.9"/><text x="248" y="211" font-size="8.5" fill="#e36414" font-weight="700">dos</text><rect x="170" y="285" width="120" height="56" rx="4" fill="#0f4c5c" stroke="#0f4c5c" stroke-width="0.8"/><text x="230.0" y="304.5" text-anchor="middle" font-size="9.5" font-weight="700" fill="#fff">Caso 6 · t₀ = d̄/(S_d/√n)</text><text x="230.0" y="316.5" text-anchor="middle" font-size="9.5" font-weight="700" fill="#fff">t con n−1 g.l.</text><text x="230.0" y="328.5" text-anchor="middle" font-size="9.5" font-weight="700" fill="#fff">ec. 2-41 / (2.21)</text><path d="M210,249 L210,285" stroke="#5b6b73" stroke-width="0.9"/><text x="214" y="270" font-size="8.5" fill="#e36414" font-weight="700">sí</text><rect x="310" y="285" width="150" height="40" rx="4" fill="#e8f1f3" stroke="#0f4c5c" stroke-width="0.8"/><text x="385.0" y="308.5" text-anchor="middle" font-size="9.5" font-weight="400" fill="#142b33">¿σ₁², σ₂² conocidas?</text><path d="M290,249 L290,268 L385,268 L385,285" fill="none" stroke="#5b6b73" stroke-width="0.9"/><text x="294" y="264" font-size="8.5" fill="#e36414" font-weight="700">no</text><rect x="310" y="365" width="120" height="56" rx="4" fill="#0f4c5c" stroke="#0f4c5c" stroke-width="0.8"/><text x="370.0" y="384.5" text-anchor="middle" font-size="9.5" font-weight="700" fill="#fff">Caso 3 · Z₀</text><text x="370.0" y="396.5" text-anchor="middle" font-size="9.5" font-weight="700" fill="#fff">N(0,1)</text><text x="370.0" y="408.5" text-anchor="middle" font-size="9.5" font-weight="700" fill="#fff">ec. 2-33</text><path d="M345,325 L345,365" stroke="#5b6b73" stroke-width="0.9"/><text x="349" y="350" font-size="8.5" fill="#e36414" font-weight="700">sí</text><rect x="450" y="365" width="150" height="50" rx="4" fill="#e8f1f3" stroke="#0f4c5c" stroke-width="0.8"/><text x="525.0" y="381.5" text-anchor="middle" font-size="9.5" font-weight="400" fill="#142b33">¿Varianzas iguales?</text><text x="525.0" y="393.5" text-anchor="middle" font-size="9.5" font-weight="400" fill="#142b33">(gráfica normal o prueba F,</text><text x="525.0" y="405.5" text-anchor="middle" font-size="9.5" font-weight="400" fill="#142b33">caso 8)</text><path d="M430,325 L430,348 L525,348 L525,365" fill="none" stroke="#5b6b7a" stroke-width="0.9"/><text x="434" y="344" font-size="8.5" fill="#e36414" font-weight="700">no</text><rect x="400" y="450" width="120" height="56" rx="4" fill="#0f4c5c" stroke="#0f4c5c" stroke-width="0.8"/><text x="460.0" y="469.5" text-anchor="middle" font-size="9.5" font-weight="700" fill="#fff">Caso 4 · t₀ con S_p</text><text x="460.0" y="481.5" text-anchor="middle" font-size="9.5" font-weight="700" fill="#fff">t con n₁+n₂−2 g.l.</text><text x="460.0" y="493.5" text-anchor="middle" font-size="9.5" font-weight="700" fill="#fff">ec. 2-24 / (2.14)</text><rect x="540" y="450" width="120" height="56" rx="4" fill="#0f4c5c" stroke="#0f4c5c" stroke-width="0.8"/><text x="600.0" y="469.5" text-anchor="middle" font-size="9.5" font-weight="700" fill="#fff">Caso 5 · t₀ (Welch)</text><text x="600.0" y="481.5" text-anchor="middle" font-size="9.5" font-weight="700" fill="#fff">t con v g.l. (ec. 2-32)</text><text x="600.0" y="493.5" text-anchor="middle" font-size="9.5" font-weight="700" fill="#fff">ec. 2-31 / (2.15)</text><path d="M490,415 L490,432 L460,432 L460,450" fill="none" stroke="#5b6b73" stroke-width="0.9"/><text x="464" y="446" font-size="8.5" fill="#e36414" font-weight="700">sí</text><path d="M560,415 L560,432 L600,432 L600,450" fill="none" stroke="#5b6b73" stroke-width="0.9"/><text x="604" y="446" font-size="8.5" fill="#e36414" font-weight="700">no</text><rect x="470" y="140" width="130" height="34" rx="4" fill="#e8f1f3" stroke="#0f4c5c" stroke-width="0.8"/><text x="535.0" y="160.5" text-anchor="middle" font-size="9.5" font-weight="400" fill="#142b33">¿Una o dos?</text><path d="M535,110 L535,125.0 L535,125.0 L535,140" fill="none" stroke="#5b6b73" stroke-width="0.9"/><rect x="620" y="215" width="130" height="56" rx="4" fill="#0f4c5c" stroke="#0f4c5c" stroke-width="0.8"/><text x="685.0" y="234.5" text-anchor="middle" font-size="9.5" font-weight="700" fill="#fff">Caso 7 · χ²₀ = (n−1)S²/σ₀²</text><text x="685.0" y="246.5" text-anchor="middle" font-size="9.5" font-weight="700" fill="#fff">χ² con n−1 g.l.</text><text x="685.0" y="258.5" text-anchor="middle" font-size="9.5" font-weight="700" fill="#fff">ec. 2-45 / tabla 2.5 b</text><rect x="620" y="285" width="130" height="56" rx="4" fill="#0f4c5c" stroke="#0f4c5c" stroke-width="0.8"/><text x="685.0" y="304.5" text-anchor="middle" font-size="9.5" font-weight="700" fill="#fff">Caso 8 · F₀ = S₁²/S₂²</text><text x="685.0" y="316.5" text-anchor="middle" font-size="9.5" font-weight="700" fill="#fff">F con n₁−1, n₂−1 g.l.</text><text x="685.0" y="328.5" text-anchor="middle" font-size="9.5" font-weight="700" fill="#fff">ec. 2-48 / (2.19)</text><path d="M560,174 L560,200 L685,200 L685,215" fill="none" stroke="#5b6b73" stroke-width="0.9"/><text x="564" y="196" font-size="8.5" fill="#e36414" font-weight="700">una</text><path d="M510,174 L510,320 L600,320 L600,313 L620,313" fill="none" stroke="#5b6b73" stroke-width="0.9"/><text x="490" y="250" font-size="8.5" fill="#e36414" font-weight="700">dos</text><rect x="630" y="140" width="120" height="56" rx="4" fill="#0f4c5c" stroke="#0f4c5c" stroke-width="0.8"/><text x="690.0" y="159.5" text-anchor="middle" font-size="9.5" font-weight="700" fill="#fff">Caso 9 · z₀</text><text x="690.0" y="171.5" text-anchor="middle" font-size="9.5" font-weight="700" fill="#fff">N(0,1) aprox.</text><text x="690.0" y="183.5" text-anchor="middle" font-size="9.5" font-weight="700" fill="#fff">tabla 2.5 c / 2.6 d</text><path d="M690,110 L690,125.0 L690,125.0 L690,140" fill="none" stroke="#5b6b73" stroke-width="0.9"/><rect x="10" y="530" width="740" height="56" rx="4" fill="#fde8d7" stroke="#0f4c5c" stroke-width="0.8"/><text x="380.0" y="549.5" text-anchor="middle" font-size="9.5" font-weight="400" fill="#142b33">Supuestos de todos los casos: muestras aleatorias, orden de corridas aleatorizado (independencia), normalidad verificada con gráfica de probabilidad normal.</text><text x="380.0" y="561.5" text-anchor="middle" font-size="9.5" font-weight="400" fill="#142b33">Los casos 7 y 8 son muy sensibles a la no normalidad. Con n grande (> 30–45) la t se confunde con la normal y el caso 2 ≈ caso 1.</text><text x="380.0" y="573.5" text-anchor="middle" font-size="9.5" font-weight="400" fill="#142b33">Numeración de las ecuaciones: Montgomery (2-xx) / Gutiérrez–De la Vara (2.xx).</text></svg>

| Caso | Qué se compara | Condición sobre la varianza | Hipótesis nula | Estadístico | Distribución de referencia | Rechazo (bilateral) | Intervalo de confianza | Fuente |
|---|---|---|---|---|---|---|---|---|
| 1 | Una media con un patrón $\mu_0$ | $\sigma$ **conocida** (o $n$ grande, TLC) | $\mu = \mu_0$ | $Z_0 = \dfrac{\bar y - \mu_0}{\sigma/\sqrt n}$ | $N(0,1)$ | $\lvert Z_0 \rvert > Z_{\alpha/2}$ | $\bar y \pm Z_{\alpha/2}\,\sigma/\sqrt n$ | M ecs. 2-35, 2-36 |
| 2 | Una media con un patrón $\mu_0$ | $\sigma$ **desconocida**, población normal | $\mu = \mu_0$ | $t_0 = \dfrac{\bar y - \mu_0}{S/\sqrt n}$ | $t_{n-1}$ | $\lvert t_0 \rvert > t_{\alpha/2,\,n-1}$ | $\bar y \pm t_{\alpha/2,\,n-1}\,S/\sqrt n$ | M ecs. 2-37, 2-38; G ec. (2.8) |
| 3 | Dos medias, muestras independientes | $\sigma_1^2$, $\sigma_2^2$ **conocidas** | $\mu_1 = \mu_2$ | $Z_0 = \dfrac{\bar y_1 - \bar y_2}{\sqrt{\sigma_1^2/n_1 + \sigma_2^2/n_2}}$ | $N(0,1)$ | $\lvert Z_0 \rvert > Z_{\alpha/2}$ | $\bar y_1 - \bar y_2 \pm Z_{\alpha/2}\sqrt{\sigma_1^2/n_1 + \sigma_2^2/n_2}$ | M ecs. 2-33, 2-34 |
| 4 | Dos medias, muestras independientes | desconocidas pero **iguales** | $\mu_1 = \mu_2$ | $t_0 = \dfrac{\bar y_1 - \bar y_2}{S_p\sqrt{1/n_1 + 1/n_2}}$, $S_p^2 = \dfrac{(n_1-1)S_1^2 + (n_2-1)S_2^2}{n_1+n_2-2}$ | $t_{n_1+n_2-2}$ | $\lvert t_0 \rvert > t_{\alpha/2,\,n_1+n_2-2}$ | $\bar y_1 - \bar y_2 \pm t_{\alpha/2}\,S_p\sqrt{1/n_1 + 1/n_2}$ | M ecs. 2-24, 2-25, 2-30; G ec. (2.14) |
| 5 | Dos medias, muestras independientes | desconocidas y **distintas** | $\mu_1 = \mu_2$ | $t_0 = \dfrac{\bar y_1 - \bar y_2}{\sqrt{S_1^2/n_1 + S_2^2/n_2}}$ | $t_v$ aprox., $v$ de la ec. 2-32 | $\lvert t_0 \rvert > t_{\alpha/2,\,v}$ | $\bar y_1 - \bar y_2 \pm t_{\alpha/2,\,v}\sqrt{S_1^2/n_1 + S_2^2/n_2}$ | M ecs. 2-31, 2-32; G ecs. (2.15), (2.16) |
| 6 | Dos medias, observaciones **pareadas** | se trabaja con $d_j = y_{1j} - y_{2j}$ | $\mu_d = 0$ | $t_0 = \dfrac{\bar d}{S_d/\sqrt n}$ | $t_{n-1}$ | $\lvert t_0 \rvert > t_{\alpha/2,\,n-1}$ | $\bar d \pm t_{\alpha/2,\,n-1}\,S_d/\sqrt n$ | M ecs. 2-41 a 2-43; G ec. (2.21) |
| 7 | Una varianza con un valor $\sigma_0^2$ | normalidad (sensible) | $\sigma^2 = \sigma_0^2$ | $\chi_0^2 = \dfrac{(n-1)S^2}{\sigma_0^2}$ | $\chi^2_{n-1}$ | $\chi_0^2 > \chi^2_{\alpha/2,\,n-1}$ o $< \chi^2_{1-\alpha/2,\,n-1}$ | $\left[\dfrac{(n-1)S^2}{\chi^2_{\alpha/2,\,n-1}},\ \dfrac{(n-1)S^2}{\chi^2_{1-\alpha/2,\,n-1}}\right]$ | M ecs. 2-45, 2-46; G ec. (2.3) |
| 8 | Dos varianzas | normalidad (sensible) | $\sigma_1^2 = \sigma_2^2$ | $F_0 = S_1^2/S_2^2$ | $F_{n_1-1,\,n_2-1}$ | $F_0 > F_{\alpha/2,\,n_1-1,\,n_2-1}$ o $< F_{1-\alpha/2,\,n_1-1,\,n_2-1}$ | $\left[\dfrac{S_1^2}{S_2^2}F_{1-\alpha/2,\,n_2-1,\,n_1-1},\ \dfrac{S_1^2}{S_2^2}F_{\alpha/2,\,n_2-1,\,n_1-1}\right]$ | M ecs. 2-48 a 2-50; G ec. (2.19) |
| 9 | Una proporción con $p_0$, o dos proporciones | binomial aproximada por normal ($np > 10$) | $p = p_0$ / $p_1 = p_2$ | $z_0 = \dfrac{X - np_0}{\sqrt{np_0(1-p_0)}}$ / $z_0 = \dfrac{\hat p_1 - \hat p_2}{\sqrt{\hat p(1-\hat p)(1/n_1+1/n_2)}}$ | $N(0,1)$ aprox. | $\lvert z_0 \rvert > z_{\alpha/2}$ | $\hat p \pm z_{\alpha/2}\sqrt{\hat p(1-\hat p)/n}$ | G tablas 2.5 c, 2.6 d |

M = Montgomery; G = Gutiérrez–De la Vara. Para las alternativas de una cola se cambia
$\alpha/2$ por $\alpha$ y se rechaza solo en la cola que indica $H_A$ (tablas 2-3, 2-4 y 2-7 de
Montgomery; tablas 2.5 y 2.6 de Gutiérrez–De la Vara).

Protocolo común a los nueve casos, con lo que cambia en cada uno:

| Paso | Casos 1–6 (medias) | Casos 7–8 (varianzas) | Caso 9 (proporciones) |
|---|---|---|---|
| Diseño | Aleatorizar el orden y la asignación; en el caso 6, aleatorizar dentro de cada par | Ídem | Ídem; $n$ grande |
| Tamaño de muestra | Curvas OC con $d = \lvert\delta\rvert/\sigma$ (una media) o $\lvert\delta\rvert/2\sigma$ (dos medias); o $n \approx 4S^2/E^2$ | Curvas OC de $\chi^2$ y $F$ (apéndice de Montgomery) | $n = z_{\alpha/2}^2\,\hat p(1-\hat p)/E^2$ |
| Gráficas previas | Diagrama de puntos, caja, histograma | Las mismas, más atención a colas | Tabla de frecuencias |
| Supuestos | Independencia (orden de corrida); normalidad (gráfica de probabilidad normal, Anderson-Darling); casos 4 y 5: pendientes de las rectas o prueba $F$ | Normalidad **imprescindible** | $np_0 > 10$ |
| Decisión | Tres criterios equivalentes: valor crítico, valor $P$, intervalo de confianza | Ídem | Ídem |
| Reporte | $n$, media, $S$, EE, $t_0$ o $Z_0$, g.l., valor $P$, IC, diferencia observada y su significancia práctica | $n$, $S^2$, $\chi_0^2$ o $F_0$, g.l., valor $P$, IC | $\hat p$, $z_0$, valor $P$, IC |

Reglas para elegir:

- **¿Hay un valor de referencia externo** (especificación, fabricante, valor histórico)? Entonces
  es una media contra un valor. La varianza casi siempre es desconocida: prueba $t$.
- **¿Hay dos tratamientos y cada unidad experimental recibe solo uno?** Muestras independientes.
  Antes de la $t$ combinada, verificar la igualdad de varianzas con la gráfica de probabilidad
  normal (pendientes) o con la prueba $F$; si difieren claramente, usar la versión de varianzas
  distintas.
- **¿Las unidades son heterogéneas y cada una puede recibir ambos tratamientos**, o hay una
  fuente de variación conocida (día, turno, lote, sesión) con la que se pueden formar pares?
  Muestras pareadas: la diferencia dentro del par elimina el efecto del bloque. Es el primer
  caso de formación de bloques y conecta con el capítulo 4 de Montgomery.
- **¿Interesa la variabilidad y no la media?** Pruebas para varianzas, con la advertencia de que
  son muy sensibles a la no normalidad.
- **¿La respuesta es pasa/no pasa?** Proporciones (solo Gutiérrez–De la Vara).

## Una o dos colas

La dirección de $H_A$ se decide **antes** de ver los datos y depende de la afirmación que se
quiera probar, no del resultado.

| Afirmación que se quiere probar | $H_0$ | $H_A$ | Región de rechazo (prueba $t$) |
|---|---|---|---|
| "La media es distinta de $\mu_0$" | $\mu = \mu_0$ | $\mu \ne \mu_0$ | $\lvert t_0 \rvert > t_{\alpha/2}$ |
| "La media es mayor que $\mu_0$" | $\mu = \mu_0$ | $\mu > \mu_0$ | $t_0 > t_\alpha$ |
| "La media es menor que $\mu_0$" | $\mu = \mu_0$ | $\mu < \mu_0$ | $t_0 < -t_\alpha$ |

Lo que se desea demostrar va en $H_A$: solo se acepta como cierto si se rechaza $H_0$. Cuando el
valor de referencia es un **máximo garantizado** (una especificación del tipo "menor que"), un
resultado por debajo no contradice la garantía y la alternativa natural es de una cola; cuando
el valor de referencia es un **valor medido** (una calibración, un dato de fábrica), cualquier
desviación importa y la alternativa es de dos colas.

## Secuencia completa del análisis

Es el orden en que se presenta un diseño de comparación simple en el curso: títulos en forma de
pregunta, hipótesis como $H_0$/$H_A$, supuestos con prueba gráfica y analítica, resultados
reportados de forma literal.

1. **Planteamiento del problema.** Qué se compara, por qué, cuál es la variable respuesta y sus
   unidades, de dónde sale el valor de referencia o el segundo tratamiento.
2. **Hipótesis.** $H_0$ como igualdad; $H_A$ con su dirección justificada. Nivel de significancia
   $\alpha$ fijado de antemano (0.05 salvo que rechazar implique una decisión costosa).
3. **Diseño.** Unidad experimental, definición de réplica, número de réplicas (curvas OC de
   Montgomery con $\delta$, $\sigma$ previa y $\beta$; o error máximo $E$ de Gutiérrez–De la
   Vara), **aleatorización** del orden de las corridas y de la asignación del material, y si hay
   apareamiento, el criterio de los pares.
4. **Datos y gráficas simples.** Diagrama de puntos, histograma o diagrama de caja; medias,
   desviaciones estándar y errores estándar. Siempre antes de la prueba formal.
5. **Verificación de supuestos.**
    - *Independencia*: garantizada por la aleatorización; se revisa la gráfica de la respuesta (o
      de los residuos $y_{ij} - \bar y_i$) contra el orden de corrida, sin tendencias ni rachas.
      Prueba analítica opcional: Durbin-Watson.
    - *Normalidad*: gráfica de probabilidad normal (recta por los cuartiles 25 y 75, prueba del
      lápiz grueso) y prueba analítica (Anderson-Darling o Shapiro-Wilk, $P > 0.05$). Las
      desviaciones moderadas no afectan las pruebas para medias, pero sí a las de varianzas.
    - *Igualdad de varianzas* (dos muestras independientes): pendientes de las gráficas de
      probabilidad normal y prueba $F$ (o Bartlett, Levene).
6. **Estadístico de prueba y distribución de referencia.** Calcular el estadístico con la
   fórmula, indicar sus grados de libertad y el valor crítico.
7. **Decisión con los tres criterios equivalentes.** Estadístico frente al valor crítico;
   valor $P$ frente a $\alpha$; intervalo de confianza (al $100(1-\alpha)$ % si es bilateral, al
   $100(1-2\alpha)$ % si es unilateral, mirando de qué lado queda).
8. **Intervalo de confianza para el parámetro** (la diferencia de medias, la media, el cociente
   de varianzas): da la magnitud y la precisión, no solo la decisión.
9. **Significancia práctica.** ¿La diferencia estimada importa para el problema? Un valor $P$
   apenas mayor que $\alpha$ con una diferencia relevante es motivo para tomar más datos, no para
   cerrar el caso.
10. **Conclusión y recomendaciones** en el lenguaje del problema, con la salida literal del
    software (tabla con $n$, media, desviación estándar, error estándar, $t_0$, g.l., valor $P$,
    intervalo).

## Las fórmulas en Python

Cada prueba del capítulo se puede calcular directamente con la fórmula y verificar con la
función equivalente de `scipy.stats`. Las distribuciones de referencia son `norm`, `t`, `chi2` y
`f`; los valores críticos se obtienen con `.ppf(1 - alpha, gl)` y los valores $P$ con `.sf` (cola
superior) o `.cdf` (cola inferior).

| Prueba | Fórmula a mano | Verificación |
|---|---|---|
| $t$ de una muestra | `t0 = (y.mean() - mu0) / (y.std(ddof=1) / sqrt(n))`; $P$ con `t.sf(abs(t0), n-1)*2` (bilateral) o `t.sf(t0, n-1)` (cola superior) | `ttest_1samp(y, mu0, alternative=...)` |
| $t$ de dos muestras, varianzas iguales | `sp2 = ((n1-1)*s1**2 + (n2-1)*s2**2)/(n1+n2-2)`; `t0 = (y1.mean()-y2.mean())/sqrt(sp2*(1/n1+1/n2))` | `ttest_ind(y1, y2, equal_var=True)` |
| $t$ de dos muestras, varianzas distintas | `t0 = (y1.mean()-y2.mean())/sqrt(s1**2/n1 + s2**2/n2)`; `v` con la ec. 2-32 | `ttest_ind(y1, y2, equal_var=False)` |
| $t$ pareada | `d = y1 - y2`; `t0 = d.mean()/(d.std(ddof=1)/sqrt(n))` | `ttest_rel(y1, y2)` |
| Una varianza | `chi0 = (n-1)*s2/sigma0_2`; $P$ con `chi2.sf(chi0, n-1)` | — |
| Dos varianzas | `F0 = s1**2/s2**2`; $P$ bilateral `2*min(f.sf(F0, n1-1, n2-1), f.cdf(F0, n1-1, n2-1))` | — |
| Intervalo para $\mu$ | `y.mean() ± t.ppf(1-alpha/2, n-1) * s/sqrt(n)` | `t.interval(1-alpha, n-1, loc=y.mean(), scale=s/sqrt(n))` |
| Normalidad | gráfica: `y` ordenada contra `norm.ppf((j-0.5)/n)` | `anderson(y)`, `shapiro(y)`, `probplot(y)` |
| Tamaño de muestra y potencia | distribución $t$ no central: `nct.sf(t.ppf(1-alpha, n-1), n-1, delta/sigma*sqrt(n))` es la potencia | `statsmodels.stats.power.TTestPower().solve_power(...)` |

En Minitab las mismas pruebas están en Estadísticas › Estadísticas básicas (t de 1 muestra,
t de 2 muestras, t pareada, 1 varianza, 2 varianzas, Prueba de normalidad) y el tamaño de
muestra en Estadísticas › Potencia y tamaño de la muestra.

## Errores frecuentes

- Escribir $H_0$ como desigualdad, o poner en $H_0$ lo que se quiere demostrar.
- Decidir la dirección de $H_A$ después de ver los datos.
- Tratar como réplicas varias lecturas de la misma corrida (pseudorréplicas): se subestima el
  error experimental y la prueba rechaza de más.
- Correr todos los ensayos de un tratamiento y después todos los del otro: cualquier deriva en
  el tiempo se confunde con el efecto del tratamiento.
- Usar la prueba de muestras independientes con datos pareados: la heterogeneidad de las
  unidades oculta la diferencia (cofres: $t = 1.39$ en lugar de $9.70$).
- Parear cuando las unidades son homogéneas: solo se pierden $n - 1$ grados de libertad y el
  intervalo sale más ancho.
- Reportar solo "se rechaza" sin valor $P$ ni intervalo de confianza.
- Usar las pruebas de varianzas ($\chi^2$, $F$) sin revisar la normalidad: son muy sensibles a
  ella.
- Interpretar "no se rechaza $H_0$" como "las medias son iguales"; solo significa que no hubo
  evidencia suficiente con ese tamaño de muestra y esa variabilidad.
"""

CSS = """
@page { size: A4; margin: 20mm 18mm 20mm 18mm;
        @bottom-center { content: counter(page); font: 9pt Calibri, 'Segoe UI', Arial, sans-serif; color: #5b6b73; } }
* { box-sizing: border-box; }
body { font: 10.8pt/1.5 Calibri, 'Segoe UI', Arial, sans-serif; color: #142b33; margin: 0; }
h1, h2, h3, h4 { font-family: Cambria, Georgia, serif; color: #0f4c5c; line-height: 1.2; }
.portada { height: 250mm; display: flex; flex-direction: column; justify-content: center; page-break-after: always; }
.portada h1 { font-size: 28pt; margin: 0 0 6mm; page-break-before: auto; }
.portada .sub { font-size: 14pt; color: #5b6b73; margin: 0 0 16mm; }
.portada .meta { font-size: 11.5pt; }
.portada .como { margin-top: 14mm; background: #e8f1f3; border-radius: 6px; padding: 5mm 6mm; font-size: 10.5pt; }
.indice { page-break-after: always; } .indice h2 { page-break-before: auto; }
.indice ol { padding-left: 6mm; } .indice li { margin: 0.8mm 0; } .indice .p { font-weight: 700; margin-top: 3mm; list-style: none; margin-left: -6mm; }
h1 { font-size: 20pt; margin: 0 0 3mm; page-break-before: always; }
h1 .n { display: inline-block; background: #e36414; color: #fff; border-radius: 4px; padding: 0 3mm; font-size: 14pt; margin-right: 3mm; vertical-align: middle; }
h2 { font-size: 15pt; margin: 7mm 0 2mm; break-after: avoid; border-bottom: 0.6pt solid #0f4c5c; padding-bottom: 1mm; }
h3 { font-size: 12.5pt; margin: 5mm 0 2mm; break-after: avoid; }
h4 { font-size: 11pt; margin: 3mm 0 1.5mm; break-after: avoid; }
p { margin: 0 0 2.4mm; text-align: justify; }
blockquote { margin: 0 0 3mm; padding: 1.5mm 4mm; border-left: 1mm solid #e36414; color: #5b6b73; font-size: 10pt; }
table { border-collapse: collapse; width: 100%; margin: 2mm 0 3.5mm; font-size: 9.3pt; }
th { background: #0f4c5c; color: #fff; padding: 1.3mm 2mm; text-align: left; font-weight: 700; vertical-align: middle; }
td { padding: 1.1mm 2mm; border-bottom: 0.3pt solid #d5dee1; text-align: left; vertical-align: middle; }
tr { break-inside: avoid; }
ul, ol { margin: 0 0 3mm; padding-left: 6mm; } li { margin: 0 0 1.2mm; text-align: justify; }
li > ul, li > ol { margin-top: 1mm; }
code { font: 9pt 'Consolas', 'Courier New', monospace; background: #f4f8f9; padding: 0 1mm; border-radius: 2px; }
.katex-display { margin: 2mm 0 3mm; overflow: hidden; }
.katex { font-size: 1.03em; }
strong { color: #0f4c5c; }
hr { border: 0; border-top: 0.4pt solid #c9d6da; margin: 5mm 0; }
.ref { font-size: 9.8pt; margin: 0 0 2mm; padding-left: 6mm; text-indent: -6mm; text-align: left; }
"""

KATEX = (
    '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.16.11/katex.min.css">'
    '<script src="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.16.11/katex.min.js"></script>'
    '<script src="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.16.11/contrib/auto-render.min.js"></script>'
)
KATEX_RUN = (
    "<script>renderMathInElement(document.body,{throwOnError:false,delimiters:["
    '{left:"$$",right:"$$",display:true},{left:"$",right:"$",display:false}]});</script>'
)


def md_a_html(texto):
    """Convierte markdown a HTML protegiendo las fórmulas de LaTeX."""
    formulas = []

    def guardar(m):
        formulas.append(m.group(0))
        return f"QQMATH{len(formulas) - 1}QQ"

    texto = re.sub(r"\$\$.*?\$\$", guardar, texto, flags=re.S)
    texto = re.sub(r"\$[^$\n]+?\$", guardar, texto)
    # listas anidadas con sangría de 2 espacios → 4 (python-markdown las exige)
    texto = re.sub(r"(?m)^  (?=(\d+\. |- ))", "    ", texto)
    out = markdown.markdown(texto, extensions=["tables", "sane_lists"])
    out = re.sub(r"QQMATH(\d+)QQ", lambda m: html.escape(formulas[int(m.group(1))], quote=False), out)
    return out


def encabezados(texto):
    return [re.sub(r"\s*\(págs?\..*?\)\s*$", "", h) for h in re.findall(r"(?m)^## (.+)$", texto)]


def build(out):
    partes = []
    for num, titulo, ruta in FICHAS:
        md = ruta.read_text(encoding="utf-8")
        md = re.sub(r"(?m)^# .*\n", "", md, count=1)  # el título lo pone el ensamblador
        partes.append((num, titulo, md))
    partes.append(("III", "Guía de decisión y aplicación en el curso", PARTE_III))

    o = ['<!doctype html><html lang="es"><head><meta charset="utf-8">',
         "<title>Teoría del diseño de comparación simple</title>", KATEX, f"<style>{CSS}</style></head><body>"]
    o.append(
        '<div class="portada"><h1>Diseño de comparación simple: teoría completa</h1>'
        '<p class="sub">Experimentos comparativos simples e inferencia con uno y dos tratamientos</p>'
        '<p class="meta">Diseño de Experimentos Avanzados (3008475)<br>Universidad Nacional de Colombia · 2026-II<br>'
        'Juan Esteban Rodríguez Ochoa · Sebastián Zapata Henao<br>Tema 1 del curso · Base estadística del trabajo práctico<br>'
        'Documento generado el 23 de octubre de 2026</p>'
        '<div class="como"><b>Cómo usar este documento.</b> La parte I sigue, sección por sección, el capítulo 2 de '
        'Montgomery (págs. 21–59): conceptos básicos, distribuciones de muestreo, pruebas para medias y varianzas, '
        'tamaño de muestra, intervalos de confianza y comparaciones pareadas, con todos sus ejemplos recalculados. La parte II '
        'sigue el capítulo 2 de Gutiérrez–De la Vara (págs. 18–59), que añade los tres criterios equivalentes de rechazo, '
        'el tamaño de muestra para un error máximo, las proporciones y la significancia práctica. La parte III es la '
        'síntesis para el curso: qué prueba usar en cada caso, una o dos colas, la secuencia completa del análisis, las '
        'fórmulas en Python y los errores frecuentes. Los números de ecuación y de página remiten a cada libro.</div></div>')

    # índice
    o.append('<div class="indice"><h2>Contenido</h2><ol>')
    for num, titulo, md in partes:
        o.append(f'<li class="p">Parte {num} · {html.escape(titulo)}</li>')
        for h in encabezados(md):
            o.append(f"<li>{md_a_html(h)[3:-4]}</li>")
    o.append("</ol></div>")

    for num, titulo, md in partes:
        o.append(f'<h1><span class="n">Parte {num}</span>{html.escape(titulo)}</h1>')
        o.append(md_a_html(md))

    o.append('<h1><span class="n">R</span>Referencias</h1>')
    refs = [
        "MONTGOMERY, Douglas C. <i>Diseño y análisis de experimentos</i>. 2 ed. México: Limusa Wiley, 2004. Capítulo 2, "
        "Experimentos comparativos simples, p. 21–59.",
        "GUTIÉRREZ PULIDO, Humberto y DE LA VARA SALAZAR, Román. <i>Análisis y diseño de experimentos</i>. 2 ed. México: "
        "McGraw-Hill, 2008. Capítulo 2, Elementos de inferencia estadística: experimentos con uno y dos tratamientos, p. 18–59.",
        "VIRTANEN, Pauli et al. SciPy 1.0: fundamental algorithms for scientific computing in Python. En: <i>Nature Methods</i>. "
        "2020, vol. 17, p. 261–272. (Módulo <code>scipy.stats</code>.)",
    ]
    o.append("".join(f'<p class="ref">{r}</p>' for r in refs))
    o.append(KATEX_RUN)
    o.append("</body></html>")
    Path(out).write_text("".join(o), encoding="utf-8")
    print("teoría:", out)


if __name__ == "__main__":
    build(sys.argv[1])
