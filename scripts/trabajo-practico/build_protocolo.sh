#!/usr/bin/env bash
# Regenera el protocolo del experimento de comparación simple (HTML → PDF con Chrome).
# Requiere numpy y scipy (entorno en ../../.venv) e internet al imprimir (KaTeX desde el CDN). Si Chrome no está en la ruta de Windows,
# abrir el HTML en un navegador Chromium e imprimirlo en A4 sin encabezados ni pies.
set -euo pipefail
cd "$(dirname "$0")"
PY=../../.venv/bin/python; [ -x "$PY" ] || PY=python3
OUT=../../trabajo-practico/protocolo
NAME=Protocolo_Comparacion_Simple_Ancho_de_Pulso
mkdir -p "$OUT"
$PY render_protocolo.py "$OUT/$NAME.html"
CHROME="/mnt/c/Program Files/Google/Chrome/Application/chrome.exe"
if [ -x "$CHROME" ]; then
  TMP=/mnt/c/Users/Public/protocolo-tmp; mkdir -p "$TMP"
  cp "$OUT/$NAME.html" "$TMP/protocolo.html"
  "$CHROME" --headless=new --disable-gpu --no-first-run --user-data-dir='C:\Users\Public\protocolo-tmp\profile' \
    --no-pdf-header-footer --virtual-time-budget=30000 --print-to-pdf='C:\Users\Public\protocolo-tmp\protocolo.pdf' \
    "file:///C:/Users/Public/protocolo-tmp/protocolo.html" 2>/dev/null
  cp "$TMP/protocolo.pdf" "$OUT/$NAME.pdf"
  rm -rf "$TMP" "$OUT/$NAME.html"
  echo "pdf: $OUT/$NAME.pdf"
fi
