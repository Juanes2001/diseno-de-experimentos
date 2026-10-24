#!/usr/bin/env bash
# Regenera la teoría del diseño de comparación simple (fichas de notas/ → HTML → PDF con Chrome).
# Requiere la biblioteca markdown (entorno en ../../.venv) y conexión a internet al imprimir
# (KaTeX se carga del CDN). Si Chrome no está en la ruta de Windows, abrir el HTML en un
# navegador Chromium e imprimirlo en A4 sin encabezados ni pies.
set -euo pipefail
cd "$(dirname "$0")"
PY=../../.venv/bin/python; [ -x "$PY" ] || PY=python3
OUT=../../trabajo-practico/teoria
NAME=Teoria_Diseno_de_Comparacion_Simple
mkdir -p "$OUT"
$PY render_teoria.py "$OUT/$NAME.html"
CHROME="/mnt/c/Program Files/Google/Chrome/Application/chrome.exe"
if [ -x "$CHROME" ]; then
  TMP=/mnt/c/Users/Public/teoria-tmp; mkdir -p "$TMP"
  cp "$OUT/$NAME.html" "$TMP/teoria.html"
  "$CHROME" --headless=new --disable-gpu --no-first-run --user-data-dir='C:\Users\Public\teoria-tmp\profile' \
    --no-pdf-header-footer --virtual-time-budget=30000 --print-to-pdf='C:\Users\Public\teoria-tmp\teoria.pdf' \
    "file:///C:/Users/Public/teoria-tmp/teoria.html" 2>/dev/null
  cp "$TMP/teoria.pdf" "$OUT/$NAME.pdf"
  rm -rf "$TMP" "$OUT/$NAME.html"
  echo "pdf: $OUT/$NAME.pdf"
fi
