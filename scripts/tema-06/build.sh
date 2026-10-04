#!/usr/bin/env bash
# Regenera la presentación y la guía del tema 6 a partir de contenido.py.
# Requiere python-pptx. El PDF de la guía se obtiene imprimiendo el HTML desde un
# navegador basado en Chromium (Edge o Chrome), en A4 y sin encabezados ni pies.
set -euo pipefail
cd "$(dirname "$0")"
OUT=../../exposicion-tema-06
mkdir -p "$OUT"
python3 render_pptx.py "$OUT/Tema6_Factoriales_Fraccionados.pptx"
python3 render_guia.py "$OUT/Guia_Tema6_Factoriales_Fraccionados.html"
