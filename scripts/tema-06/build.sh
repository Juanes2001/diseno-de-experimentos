#!/usr/bin/env bash
# Regenera la presentación y la guía del tema 6 a partir del contenido elegido.
#   ./build.sh        → fraccionados 2^(k-p) (contenido.py)
#   ./build.sh 3k     → diseños 3^k y niveles mixtos (contenido_3k.py)
# Requiere python-pptx (hay un entorno en ../../.venv). El PDF de la guía se imprime
# desde Chrome sin abrirlo; si no está en esa ruta, abrir el HTML en un navegador
# basado en Chromium e imprimirlo en A4, sin encabezados ni pies de página.
set -euo pipefail
cd "$(dirname "$0")"
PY=../../.venv/bin/python; [ -x "$PY" ] || PY=python3
OUT=../../exposicion-tema-06
mkdir -p "$OUT"
if [ "${1:-}" = "3k" ]; then
  export CONTENIDO=contenido_3k; BASE=Tema6_Factoriales_3k; GUIA=Guia_Tema6_Factoriales_3k
else
  export CONTENIDO=contenido; BASE=Tema6_Factoriales_Fraccionados; GUIA=Guia_Tema6_Factoriales_Fraccionados
fi
$PY render_pptx.py "$OUT/$BASE.pptx"
$PY render_guia.py "$OUT/$GUIA.html"
CHROME="/mnt/c/Program Files/Google/Chrome/Application/chrome.exe"
if [ -x "$CHROME" ]; then
  # Chrome (Windows) no escribe en rutas de WSL: se imprime en una carpeta de Windows y se copia.
  TMP=/mnt/c/Users/Public/guia-tmp; mkdir -p "$TMP"
  cp "$OUT/$GUIA.html" "$TMP/guia.html"
  "$CHROME" --headless=new --disable-gpu --no-first-run --user-data-dir='C:\Users\Public\guia-tmp\profile' \
    --no-pdf-header-footer --virtual-time-budget=10000 --print-to-pdf='C:\Users\Public\guia-tmp\guia.pdf' \
    "file:///C:/Users/Public/guia-tmp/guia.html" 2>/dev/null
  cp "$TMP/guia.pdf" "$OUT/$GUIA.pdf"
  rm -rf "$TMP" "$OUT/$GUIA.html"
  echo "pdf: $OUT/$GUIA.pdf"
fi
