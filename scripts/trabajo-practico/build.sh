#!/usr/bin/env bash
# Regenera las figuras y la exposición del 17 oct 2026 (fundamentos del autocorrelador).
# Requiere matplotlib, numpy y python-pptx (entorno en ../../.venv).
set -euo pipefail
cd "$(dirname "$0")"
PY=../../.venv/bin/python; [ -x "$PY" ] || PY=python3
OUT=../../trabajo-practico/exposicion-17-oct
mkdir -p "$OUT/figuras"
$PY figuras.py "$OUT/figuras"
$PY render_pptx.py "$OUT/Autocorrelador_Fundamentos_y_Calibracion.pptx" "$OUT/figuras"
