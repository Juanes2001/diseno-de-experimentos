"""Inserta diapositivas de un .pptx generado en la presentación editada a mano, sin regenerarla.

Desde el 30 oct 2026 Juan Esteban edita a mano Tema6_Fraccionados_Montgomery_Gutierrez.pptx (borró
diapositivas), así que ./build.sh combinado ya no se puede usar sobre ese archivo: lo pisaría. Las
diapositivas nuevas se escriben en contenido_combinado.py, se generan aparte (solo esas) y se insertan
con este script después de la diapositiva cuyo título se indique.

Uso:
  python insertar_diapositivas.py DESTINO.pptx ORIGEN.pptx "Título de la diapositiva anterior" [SALIDA.pptx]
         [--reemplazar "Título de una diapositiva a borrar" ...]

Con --reemplazar se borran antes las diapositivas con esos títulos (p. ej. la versión vieja de una
diapositiva que se vuelve a insertar corregida).

Copia las formas, el fondo y las notas de cada diapositiva de ORIGEN. El número del pie de página de
las diapositivas insertadas se pone igual a su posición real. Si no se da SALIDA, sobrescribe DESTINO.
"""
import copy
import sys

from pptx import Presentation
from pptx.oxml.ns import qn


def _titulo(slide):
    t = slide.shapes.title
    return t.text_frame.text.strip() if t is not None else ""


def _layout_titulo(prs):
    for lay in prs.slide_layouts:
        if lay.name.lower() in ("title only", "solo el título", "solo título"):
            return lay
    return prs.slide_layouts[5]


def _nombres_unicos(prs):
    """python-pptx nombra las partes nuevas por conteo (slideN.xml); si se borraron diapositivas a mano,
    ese nombre puede existir ya y el .pptx queda con entradas duplicadas. Se renombran las repetidas."""
    import re
    from pptx.opc.packuri import PackURI
    partes = list(prs.part.package.iter_parts())
    usados = {str(p.partname) for p in partes}
    vistos = set()
    for p in partes:
        nombre = str(p.partname)
        if nombre in vistos:
            m = re.match(r"(.*?)(\d+)(\.xml)$", nombre)
            n = int(m.group(2))
            while f"{m.group(1)}{n}{m.group(3)}" in usados:
                n += 1
            p.partname = PackURI(f"{m.group(1)}{n}{m.group(3)}")
            usados.add(str(p.partname))
            nombre = str(p.partname)
        vistos.add(nombre)


def _borrar(prs, titulo):
    ids = prs.slides._sldIdLst
    pos = [i for i, s in enumerate(prs.slides) if _titulo(s) == titulo.strip()]
    if len(pos) != 1:
        sys.exit(f"Para reemplazar se esperaba una sola diapositiva con el título {titulo!r}; hay {len(pos)}.")
    sld = ids[pos[0]]
    prs.part.drop_rel(sld.rId)
    ids.remove(sld)
    print(f"Borrada la diapositiva {pos[0] + 1} ({titulo!r}).")


def insertar(destino, origen, despues_de, salida=None, reemplazar=()):
    dst = Presentation(destino)
    src = Presentation(origen)
    for t in reemplazar:
        _borrar(dst, t)
    pos = [i for i, s in enumerate(dst.slides) if _titulo(s) == despues_de.strip()]
    if len(pos) != 1:
        sys.exit(f"Se esperaba una sola diapositiva con el título {despues_de!r}; hay {len(pos)}.")
    pos = pos[0]
    ids = dst.slides._sldIdLst
    for k, s in enumerate(src.slides, 1):
        new = dst.slides.add_slide(_layout_titulo(dst))
        tree = new.shapes._spTree
        for sh in list(new.shapes):          # quitar los marcadores vacíos del diseño
            tree.remove(sh._element)
        for el in s.shapes._spTree:
            if el.tag in (qn("p:sp"), qn("p:graphicFrame"), qn("p:cxnSp"), qn("p:grpSp"), qn("p:pic")):
                tree.append(copy.deepcopy(el))
        bg = s._element.cSld.find(qn("p:bg"))
        if bg is not None:
            old = new._element.cSld.find(qn("p:bg"))
            if old is not None:
                new._element.cSld.remove(old)
            new._element.cSld.insert(0, copy.deepcopy(bg))
        if s.has_notes_slide:
            new.notes_slide.notes_text_frame.text = s.notes_slide.notes_text_frame.text
        # mover la diapositiva nueva (la última) a su lugar
        el = ids[-1]
        ids.remove(el)
        ids.insert(pos + k, el)
        # número del pie de página = posición real
        for sh in new.shapes:
            if sh.has_text_frame and sh.text_frame.text.strip().isdigit() and sh.top > 6.9 * 914400:
                sh.text_frame.paragraphs[0].runs[0].text = str(pos + k + 1)
    _nombres_unicos(dst)
    dst.save(salida or destino)
    print(f"Insertadas {len(src.slides)} diapositivas después de la {pos + 1} ({despues_de!r}).")


if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser(usage=__doc__)
    ap.add_argument("destino"); ap.add_argument("origen"); ap.add_argument("despues_de")
    ap.add_argument("salida", nargs="?")
    ap.add_argument("--reemplazar", action="append", default=[])
    a = ap.parse_args()
    insertar(a.destino, a.origen, a.despues_de, a.salida, a.reemplazar)
