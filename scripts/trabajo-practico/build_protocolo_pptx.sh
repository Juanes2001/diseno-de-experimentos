#!/usr/bin/env bash
# Regenera la presentación del protocolo de experimentación (verificación por nivel) y sus figuras.
# Requiere numpy, scipy, matplotlib y python-pptx (entorno en ../../.venv).
set -euo pipefail
cd "$(dirname "$0")"
PY=../../.venv/bin/python; [ -x "$PY" ] || PY=python3
OUT=../../trabajo-practico/protocolo
JSON=../../trabajo-practico/piloto/analisis_piloto.json
mkdir -p "$OUT/figuras"
$PY figuras_protocolo.py "$JSON" "$OUT/figuras"
$PY render_protocolo_pptx.py "$OUT/Protocolo_Experimentacion_Por_Nivel.pptx" "$OUT/figuras" "$JSON"
