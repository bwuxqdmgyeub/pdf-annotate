from __future__ import annotations

from pathlib import Path

import fitz

from pdf_annotate.core.document import DocumentModel


def flatten_annotations(document: DocumentModel, out_path: str | Path) -> Path:
    """Bake annotations into page content so downstream viewers see them."""
    if document._doc is None:
        raise RuntimeError("no document open")
    doc = fitz.open(document._doc.name)
    for page in doc:
        for annot in list(page.annots()):
            annot.update()
    doc.save(str(out_path), garbage=3, deflate=True)
    doc.close()
    return Path(out_path)


def export_page_png(document: DocumentModel, out_path: str | Path, dpi: int = 200) -> Path:
    page = document.current_page()
    pix = page.get_pixmap(dpi=dpi)
    pix.save(str(out_path))
    return Path(out_path)