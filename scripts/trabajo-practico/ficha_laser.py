#!/usr/bin/env python3
"""Extrae de la hoja de datos del Calmar Carmel X-780 (Rev. E, 10/1/2025) la traza de
autocorrelación y el espectro "típicos" (página 3) para la diapositiva 7.

Uso: ficha_laser.py <carpeta de figuras> [ruta del PDF]

El PDF (bibliografia/laser-carmel/Carmel.780.pdf) está ignorado por git; si no existe, el
script no hace nada y se conservan los PNG ya generados en la carpeta de figuras.
"""
import os
import sys

OUT = sys.argv[1]
PDF = sys.argv[2] if len(sys.argv) > 2 else os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "..", "..", "bibliografia", "laser-carmel",
    "Carmel.780.pdf")

if not os.path.exists(PDF):
    print("ficha_laser: no está", PDF, "- se conservan las figuras existentes")
    sys.exit(0)

import pymupdf  # noqa: E402

page = pymupdf.open(PDF)[2]  # "Optical Characterization"
# Las dos imágenes superiores de la página: traza (izquierda) y espectro (derecha).
imgs = []
for info in page.get_images(full=True):
    xref = info[0]
    for r in page.get_image_rects(xref):
        imgs.append((r.y0, r.x0, xref))
imgs.sort()
top = sorted(imgs[:2], key=lambda t: t[1])  # las dos más altas, de izquierda a derecha
for (y, x, xref), name in zip(top, ["fabricante_traza", "fabricante_espectro"]):
    pix = pymupdf.Pixmap(page.parent, xref)
    if pix.n - pix.alpha >= 4:
        pix = pymupdf.Pixmap(pymupdf.csRGB, pix)
    pix.save(os.path.join(OUT, name + ".png"))
    print("ficha_laser:", name, pix.width, "x", pix.height)
