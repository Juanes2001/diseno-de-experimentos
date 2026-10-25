#!/usr/bin/env bash
# Informe del piloto del 24 oct 2026: análisis (scipy) → HTML con figuras → PDF con Chrome.
set -euo pipefail
cd "$(dirname "$0")"
PY=../../.venv/bin/python; [ -x "$PY" ] || PY=python3
OUT=../../trabajo-practico/piloto
LIBRO="${1:-$OUT/Piloto_Replicas_Autocorrelador.xlsx}"     # libro usado en el laboratorio
NAME=Informe_Piloto_Replicas
$PY analiza_piloto.py "$LIBRO" "$OUT/analisis_piloto.json" > /dev/null
$PY render_informe_piloto.py "$OUT/analisis_piloto.json" "$OUT/$NAME.html"
CHROME="/mnt/c/Program Files/Google/Chrome/Application/chrome.exe"
if [ -x "$CHROME" ]; then
  TMP=/mnt/c/Users/Public/informe-tmp; mkdir -p "$TMP"
  cp "$OUT/$NAME.html" "$TMP/informe.html"
  "$CHROME" --headless=new --disable-gpu --no-first-run --user-data-dir='C:\Users\Public\informe-tmp\profile' \
    --no-pdf-header-footer --virtual-time-budget=30000 --print-to-pdf='C:\Users\Public\informe-tmp\informe.pdf' \
    "file:///C:/Users/Public/informe-tmp/informe.html" 2>/dev/null
  cp "$TMP/informe.pdf" "$OUT/$NAME.pdf"
  rm -rf "$TMP" "$OUT/$NAME.html"
  echo "pdf: $OUT/$NAME.pdf"
fi
